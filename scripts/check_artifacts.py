"""Check the published CAD handoff without opening CAD or installing dependencies."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import re
import struct
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ("cad/club-build", "cad/hex-wheels", "cad/wheel-v3-test")
TEXT = {".md", ".txt", ".json", ".log", ".csv", ".svg"}


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def stl(path, manifold=False):
    data = path.read_bytes()
    require(len(data) >= 84, f"Short STL: {path}")
    count = struct.unpack_from("<I", data, 80)[0]
    require(count > 0 and len(data) == 84 + 50 * count, f"Malformed binary STL: {path}")
    edges = Counter()
    if manifold:
        for index in range(count):
            values = struct.unpack_from("<12fH", data, 84 + 50 * index)
            vertices = [tuple(round(x, 5) for x in values[a:a+3]) for a in (3, 6, 9)]
            require(len(set(vertices)) == 3, f"Collapsed STL triangle: {path}")
            for a, b in zip(vertices, vertices[1:] + vertices[:1]):
                edges[tuple(sorted((a, b)))] += 1
        require(all(n == 2 for n in edges.values()), f"Open/non-manifold STL edge: {path}")
    return count


def main():
    manifest = ROOT / "cad/ARTIFACTS.sha256"
    require(manifest.exists(), "Missing CAD artifact manifest")
    declared = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        path = Path(name)
        require(not path.is_absolute() and ".." not in path.parts, f"Unsafe manifest path: {name}")
        require(name not in declared, f"Duplicate manifest entry: {name}")
        declared[name] = digest
        require((ROOT / path).is_file(), f"Missing artifact: {name}")
        require(sha256((ROOT / path).read_bytes()).hexdigest() == digest, f"Hash mismatch: {name}")
    actual = {p.relative_to(ROOT).as_posix() for f in FOLDERS for p in (ROOT/f).rglob("*") if p.is_file()}
    require(actual == set(declared), "Manifest must cover exactly the three new CAD folders")

    for folder, parts, assemblies in (("club-build", 25, 1), ("hex-wheels", 35, 3)):
        files = list((ROOT / "cad" / folder / "SolidWorks").iterdir())
        require(sum(p.suffix.lower() == ".sldprt" for p in files) == parts, f"Wrong part count: {folder}")
        require(sum(p.suffix.lower() == ".sldasm" for p in files) == assemblies, f"Wrong assembly count: {folder}")

    audit = json.loads((ROOT / "cad/hex-wheels/Checks/Final verification.json").read_text())
    require(audit["native_saved_assemblies"]["robot"] == 120, "Unexpected native robot instance count")
    require(audit["external_native_part_dependencies"] == 0, "Unexpected external CAD references")
    require(not audit["native_unexpected_interferences_above_0_02_mm3"], "Recorded unexpected interference")

    v3 = ROOT / "cad/wheel-v3-test"
    report = json.loads((v3 / "Checks/Geometry check.json").read_text())
    prints = list((v3 / "Print STL").glob("*.stl"))
    require(len(prints) == 3, "V3 test must contain exactly three print STLs")
    for path in prints:
        entry = report["parts"][path.name]
        require(entry["sha256"] == sha256(path.read_bytes()).hexdigest(), f"V3 report/file mismatch: {path.name}")
        require(entry["watertight"] and entry["winding_consistent"] and entry["body_count"] == 1, f"Invalid recorded mesh: {path.name}")
        require(stl(path, manifold=True) == entry["triangles"], f"V3 triangle count mismatch: {path.name}")
        box = entry["bounds_mm"]
        require(all(0 < box[1][i] - box[0][i] <= limit for i, limit in enumerate((220, 220, 250))), f"V3 print exceeds bed: {path.name}")

    forbidden_name = re.compile(r"whatsapp|brave|session[_ -]?\d|cart.*\.(png|jpe?g)$", re.I)
    private_text = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]|cart_link_id=|github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]+|\+92\s?\d[\d -]{8,}")
    for name in actual:
        path = ROOT / name
        require(not forbidden_name.search(name), f"Private filename: {name}")
        require(path.stat().st_size < 95_000_000, f"Oversize Git artifact: {name}")
        if path.suffix.lower() in TEXT:
            text = path.read_text(encoding="utf-8")
            require(not private_text.search(text), f"Private path/token/contact/cart data: {name}")
        if path.suffix.lower() == ".stl":
            stl(path)

    # Check local Markdown links in the new handoff and project navigation.
    markdown = [ROOT/"README.md", *(ROOT/"docs").glob("*.md")]
    markdown += [ROOT/name for name in actual if name.endswith(".md")]
    for path in markdown:
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            link = link.strip("<>")
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
                continue
            target = unquote(link.split("#", 1)[0])
            require((path.parent / target).exists(), f"Broken link in {path.relative_to(ROOT)}: {link}")
    print(f"PASS: {len(actual)} hashed CAD artifacts; native file counts; three V3 closed meshes; print-bed bounds; local links; public-text checks.")
    print("These checks do not run SolidWorks, slice parts, or validate physical fit, strength, casting or electrical safety.")


if __name__ == "__main__":
    main()
