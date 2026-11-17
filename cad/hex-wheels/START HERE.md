# McLaren 6WD - hex wheel revision

15 November 2026. Uses Shaheer's supplied native rim as the donor, with the
brass 6 mm-bore / 12 mm-hex coupling selected by the team. This is a prototype
fit release. It includes native SolidWorks 2025 assemblies and parts, STEP,
and six unique STL designs with their printing quantities.

Open `SolidWorks/McLaren 6WD - Club hex wheels.SLDASM` for the complete robot.
Open `SolidWorks/Wheel and coupler.SLDASM` to inspect the wheel interface.
Open `SolidWorks/Split mould - assembly.SLDASM` for the casting tool and bolts.
Keep the referenced SLDPRT files alongside these assemblies. These are fixed
placement assemblies, not motion-mated mechanisms. The rim retains its original
native feature history with the hub features added. New mould/reference parts
are native solid parts imported from the supplied STEP geometry.

Use `PRINT ORDER.txt` and `Views/Print and assembly guide.png` for the workshop.
Use only this revision's P04 STL for the new hex wheel. The old D-hole rims are
not the wheel printing order. Steel DXFs and the P01 motor holders are unchanged.

## What changed in Shaheer's rim

The approximately 40 mm outside rim and 33 mm width, outer slots, fins, transverse
silicone-key holes and fillets are preserved from his native file. Exact Boolean
comparison found zero changed volume outside the central radius of 11.5 mm.
The three small inner relief openings were filled to strengthen the drive hub.

| Interface | Revised dimension |
|---|---:|
| Cast tyre | 57 mm diameter x 33 mm width |
| Hub outside diameter | 23 mm |
| Hex socket | 12.4 mm across opposite flats |
| Metal hex engagement | 6 mm |
| Barrel-entry relief | 15 mm diameter x 15 mm deep |
| Minimum nominal wall around barrel entry | 4 mm |
| Radial wall at hex corner | 4.34 mm |
| M4 through clearance | 4.5 mm |
| Outer screw/washer recess | 9.4 mm diameter x 8 mm deep |
| Flat retaining web | 4 mm |
| Wheel screw | M4 x 10, with a 1 mm flat washer |

The original model retained a D-hole segment and placed its shallow hex at the
motor-side mouth. At the existing wheel position this would bury the adapter
barrel into the motor boss. Recessing the hex keeps the wheel position unchanged.
The adapter's motor-side end is nominally 4 mm beyond the raised boss end, with
about 10.5-11.5 mm of shaft engagement for the supplier/CAD shaft lengths.
Nominal tyre gaps remain 5 mm between adjacent wheels, 4 mm to the outer guard,
and 5 mm from tyre inner face to the outer doubler face. Check these after casting
and under load because flash, runout, tyre deformation and weld distortion vary.

## Mould and casting

The mould follows Soban's removable-base and split-wall concept from the shared
screenshots. A model file for his new mould was not included, so this is a new
matching tool rather than an edited copy of his CAD. Its two wall halves separate
radially; there is no need to force a cured tyre through a closed ring. No wall
draft is used, keeping the tyre cylindrical at 57 mm over the complete 33 mm width.

1. Dry-assemble the tool first. The base locating pilot must enter the rim's outer
   recess freely. Deburr the pilot and plain M4 holes if needed without enlarging
   the tyre cavity. Place the rim with its outer screw-access face against the base.
2. Assemble the two wall halves on the base and fit the two side bolts and nuts.
   Fit the M4 x 50 centre bolt from underneath, through the rim and separate top cap.
   Use washers and gently snug the top nut. The cap keeps silicone out of the hub.
3. Seal external mould seams with tape or a small compatible sealant bead. Use a
   release treatment suitable for the actual silicone on mould surfaces only;
   keep release off the rim's grip features. Test a little of the actual mixture
   on the printed plastic/release combination before using a full batch.
4. Wet the rim's grip holes with the same silicone mixture, then fill the annulus
   slowly to the wall top. Estimated filled silicone volume is about 54 mL per tyre,
   excluding mixing losses. Follow the actual silicone maker's ratio and cure time;
   the chat does not establish the formulation currently being used.
5. After full cure, remove the centre nut/cap and side bolts. Lift the wall halves
   slightly to clear the 1.2 mm locating lip, separate them sideways, and remove the
   wheel from the base. Do not lever against a printed centre shaft. Trim seam flash.

Fit the brass coupler to the motor first, tighten its short grub screws, then slide
the rim on and fit the outer M4 screw and washer. The coupler stays removable and
is not cast into the tyre. There is no motor shaft or printed D-key inside the mould.

## Verification and limits

The saved 120-component full assembly reopened, resolved all 27 unique references
within its package and rebuilt. Geometry checks preserve the 294 x 290 x 102 mm
robot envelope. The exact changed-component audit found no unexpected solid
overlaps. Native interference results distinguish the simplified, unmodelled metal
threads from physical collisions; tiny pre-existing holder/hardware edge contacts
remain documented. The rim's native and STEP volumes were compared separately.

All six exported STL meshes are watertight, single connected bodies and consistent
with millimetre scale. DfAM reports are in `Checks`. Original outer fillets include
isolated sampled thicknesses around 1.44 mm; the rim's sampled fifth percentile is
about 3 mm. These local retained features are not the strengthened drive hub. The
4 mm/4.34 mm nominal hub walls and 4 mm retaining web are geometric dimensions,
not tested material strength. The STL wall-ray samples are not an exhaustive
minimum-thickness proof. Review the small bridge roofs in the slicer.

No FEA, impact test, measured print fit or casting trial was performed. The published
images define the outer coupling geometry; they do not prove the internal thread
and shaft-stop depths of the delivered batch. A single hub test and complete wheel
trial are required before the batch. The motor product lists a 14.5 mm shaft, while
the old team reference model has 15.5 mm, which is why the dry axle stack is checked.

## Sources and preserved originals

- Electrobes coupling page and its dimensioned product images: 6 mm shaft option,
  12 mm hex, 6 mm hex length, 12 mm barrel, 18 mm overall, M4 retention/set screws.
  https://electrobes.com/product/hex-coupler-3mm-4mm-5mm-bore-motor-hex-brass-shaft-coupling-flexible-connector-for-car-wheel-tires-shaft-motor/
- Electrobes JGB37-550 12 V 160 RPM motor, 6 mm D shaft, listed shaft length 14.5 mm.
  https://electrobes.com/product/jgb37-550-dc-12v-160rpm-high-torque-metal-gear-dc-motor/
- Team-referenced GrabCAD coupling model. The web reader returned HTTP 403; its
  CAD download was not verified. The assembly coupler is explicitly a simplified
  reference made from the supplier's dimensioned images, not a downloaded exact model.
  https://grabcad.com/library/4mm-5mm-6mm-stainless-steel-hex-shaft-coupling-1
- Original supplied SLDPRT and STEP are preserved in `Original Shaheer`. They differ
  slightly in outer relief geometry (about 17.48 cubic mm); the native file is the
  authoritative donor for this revision. The exported native rim matches the new STEP.
- Private chat and people/contact details are excluded from this handoff.
