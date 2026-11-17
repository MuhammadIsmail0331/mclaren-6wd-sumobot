# V3 rim and mould — print one of each

Prepared 17 November 2026. This is the latest wheel-only test set, based on
Shaheer's V3 rim and Soban's supplied mould. **It is not integrated into the full
native robot assembly.** Print one rim, one base and one wall, not six rims yet.

| File | Quantity | Orientation |
|---|---:|---|
| [Rim](Print%20STL/01%20Rim%20-%20print%20ONE.stl) | 1 | Axis upright; outside screw recess down |
| [Mould base](Print%20STL/02%20Mould%20base%20-%20print%20ONE.stl) | 1 | Plate down, pin up |
| [Mould wall](Print%20STL/03%20Mould%20wall%20-%20print%20ONE.stl) | 1 | Ring upright, tabs up |

PETG, 0.20 mm layers, 100% scale in millimetres. All three fit a 220 x 220 x 250 mm
printer. Detailed settings and the dry-fit/casting sequence are in
[PRINT ONE EACH](PRINT%20ONE%20EACH.txt).

Only the rim's centre interface was changed: a recessed 12.4 mm AF hex, 15 mm
barrel entry, 4.5 mm retaining web and plain 4.5 mm screw hole. Geometry beyond
radius 10.51 mm is unchanged from the supplied native donor. Revised geometry
is STEP/STL; the preserved original SLDPRT does not contain those modifications.

Both mould geometries are unchanged author STL exports, rotated for printing.
The native base returned future-version error 8192 in SolidWorks 2025; native
mould feature trees were not inspected. Their originals are preserved for users
with a compatible SolidWorks version.

**Fill silicone flush with the 33 mm rim, 3 mm below the 36 mm main wall top.**
Mask the central hub recesses and seal the outside joint. The supplied wall is
one continuous ring, not the earlier tool's two removable halves. Test axial
demoulding and lift the wheel straight off the slender pin.

All three meshes are watertight single bodies. Local inherited rim features
include a sampled 1.498 mm wall; do not treat this as a strength approval.
[Changes and measurement limits](WHAT%20CHANGED.md) and [reports](Checks) record
what was checked. Actual coupler fit, printer tolerance and one successful cast
must be recorded before approving a batch.
