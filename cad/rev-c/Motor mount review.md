# Motor mounts — McLaren 6WD Rev C

Use a steel gearbox face mount plus a short printed saddle and removable cap for each motor. The gearbox screws prevent housing rotation; the rear clamp supports the motor body against rocking. This revision is a fit prototype for the purchased hardware. Confirm body diameter, shaft eccentricity, front pattern and safe thread depth on the real motor, and print one pair before making six.

![Mount heights and load path](Views/Motor%20mount%20dimensions.png)

## What I found in the teammate STEP

SolidWorks measured one solid body, 63.6 mm across the feet, 40.2 mm tall and 82.9 mm along the motor. Its bore is Ø37.4 mm and its four foot holes are Ø4.5 mm. The foot-hole screws attach the holder to the deck; they do not draw a split cap around the motor. A round clearance sleeve provides no geometric key against rotation. A properly tightened split clamp can resist torque by friction, but this uploaded sleeve has no dedicated tightening mechanism. Its end lips do not replace the gearbox face screws.

The feet are 63.6 mm wide while our motor stations are 62 mm apart. Adjacent unchanged holders would overlap by 1.6 mm. The full sleeve also needs checking against the motor vents, terminal exit and wheel hub. An N20 holder is a different case: the rectangular gearbox can be keyed by its shape.

The holder's bore centre is 18.4 mm above its mounting feet. With a 57 mm wheel and 1 mm deck, that arrangement places the deck underside about 9.1 mm above ground, assuming the shaft eccentricity is horizontal. Our target is 6 mm. The supplied motor reference has a 6 mm shaft eccentricity; its orientation must be controlled at the front rail. Rotating the gearbox changes the relationship between the motor body and shaft height.

The Probot screenshot supports using short arched carriers and a stiff surrounding frame. It does not reveal every hidden fixing. The revision follows a defined load path rather than assuming the concealed details in that image.

## What changed in our CAD

| Part | Rev C change and purpose |
|---|---|
| 02 steel face rail | Added six Ø3.4 clearance holes per motor on a nominal Ø31 pitch circle, centred on the motor housing. Three Ø12.6 shaft-boss openings remain centred on the wheel axles. |
| 23 steel face doubler | Widened and offset the local reinforcement to cover the complete eccentric gearbox pattern. One 1 mm rail plus one 1 mm doubler gives a 2 mm nominal face stack. |
| 04 saddle and 05 cap | Short 14 mm body support, 59 mm overall width, Ø37.0 prototype bore. The older Ø37.4 bore was loose against the Ø36.8 motor reference. Kept a 0.6 mm free split for clamp adjustment. |
| 05 cap | Raised flat washer seats to Y = 37.5 mm so standard Ø9 M4 washers clear the curved arch. The arch has 3.3 mm nominal radial material. |
| 13 battery panel | Added small edge notches so the rear clamp nuts and bolt ends clear the removable covers. |
| 29–31 hardware references | Added all 36 gearbox screws and 12 clamp bolt/washer/locknut sets. They are simplified purchased hardware envelopes, not parts to print. |

The saved assembly contains 162 fixed component instances and 36 unique native part files. The full robot remains 292 × 290 × 110 mm; this revision does not meet a 250 × 250 mm entry limit. The assembly is a positioned fit model; it does not simulate suspension or use a complete mating scheme.

## Height and clearance

For an undeformed Ø57 wheel, axle height is 57 / 2 = 28.5 mm. With floor underside at 6 mm and 1 mm sheet, deck top is 7 mm. Therefore axle-to-deck-top height is 28.5 − 7 = **21.5 mm**. All six axles use the same height. The housing/shaft offset is horizontal in the assembly.

The rear saddle's locating geometry provides that height. Its bottom material is 3 mm beneath the nominal bore. A real Ø36.8 body has 0.1 mm nominal radial clearance in the Ø37.0 bore before print error and clamp adjustment. Do not force an oversized can into a tight print or crush the housing to close the split. Adjust the bore to the measured motor and the test print.

The underside backing strip is at 5–6 mm above ground. With a 2.2 mm button head beneath it, the lowest modeled clamp hardware is at **2.8 mm**. The scoop toe underside is separately at **2 mm**. Tire compression, sheet distortion and ring seams reduce these margins. For example, 1 mm tire compression would reduce these two clearances to 1.8 mm and 1 mm respectively; this is a sensitivity example, not a measured tire deflection. Keep the floor at 6 mm until the complete loaded robot is gauged on the real surface.

## Print and fabrication

Print **six saddles and six caps**, after a one-pair trial. Use PETG, 0.20 mm layers, 4–5 walls and around 25–35% infill in regions that have a core. Use 5 top and bottom layers as a starting point. The thin arch is already mostly walls, so increasing whole-part infill to 100% wastes material without providing a corresponding arch improvement. Preview the ears and holes in the slicer. Tighten locknuts evenly enough to remove movement; do not bottom out the split by force.

Print the clamp on its flat axial end, with the motor bore axis vertical. This keeps the arch and ears continuous within each layer. The horizontal Ø4.5 bolt holes may need clean-up with a drill and local support depending on the printer. The orientation comparison finds zero down-facing support area for a base-down saddle, but that changes the layer direction through the loaded ears. It is an available material-saving alternative to assess with a test part. Keep the cap on its axial end.

SolidWorks gives **14.12 cm³ per pair**, about **17.9 g solid-equivalent PETG** at an assumed 1.27 g/cm³. Six pairs are about 108 g solid equivalent. The teammate sleeve mesh is about 40.87 cm³ per motor, or 52 g at the same assumed density: the short split design uses roughly 65% less solid-equivalent volume. Actual sliced grams depend on walls, infill, brim and supports.

Laser-cut the floor, face rails, return strips, face doublers and backing strips from measured **1.0 mm steel** for the modeled stack. There are five flat DXF files in `Mount laser DXF`, with quantities and instructions in its README. The Ø31 six-M3 face pattern is a manufacturer-family nominal; verify it on a purchased motor before batch cutting. If uncertain, omit those small holes from the laser job and transfer-drill the rail and doubler together using the real gearbox pattern.

Join each rail to its return strip square, then attach it to the floor. Fixture the rail and floor to avoid weld distortion. The local doubler needs secure shear transfer to the rail. The backing strip distributes the two M4 clamp loads into the thin floor. Substituting 0.8 mm changes both stiffness and screw engagement; it is not the same stack. Use the thickest confirmed stock for the motor rails and floor, and recheck engagement if the actual stack differs.

## Hardware for the six motor mounts

| Buy | Used | Quantity |
|---|---|---:|
| M3 × 5 button-head or equivalent low-head steel machine screw, with 0.5 mm flat washer | Gearbox front face through rail + doubler | 36; buy 40–42 after confirming the real thread |
| M4 × 40 button-head steel screw | Through backing strip, floor, saddle and cap | 12; buy 15–16 |
| M4 flat washer, Ø9 outside × about 0.8 thick | Above each cap, beneath nut | 12 plus spares |
| M4 nylon-insert locknut, 7 mm across flats | Secures each clamp through-bolt | 12 plus spares |
| M5 × 12 low-profile screw, washer and locknut | Rail-return-to-floor joints | 8 sets for the two rails |

The modeled M3 × 5 with 2 mm steel and a 0.5 mm washer gives **2.5 mm nominal engagement**. This is a stack calculation, not a verified safe depth for your actual gearbox. Measure safe thread depth and confirm the thread before purchasing all 36. Use L = actual steel stack + washer thickness + permitted engagement. A longer screw requires an appropriate spacer/washer adjustment and another wheel-clearance check. Never force a screw tip into the gearbox. The modeled screw-head end is at 104.15 mm from the centreline on each side, and wheel inner face at 107 mm: nominal axial head clearance is 2.85 mm.

For the M4 clamp stack, underside bearing plane is Y = 5 and cap seat Y = 37.5, giving 32.5 mm before the top washer/nut. The model's 0.8 mm washer and 5 mm locknut end at Y = 43.3; a 40 mm under-head screw ends at Y = 45. This leaves about 1.7 mm protrusion. Confirm the purchased head and nut envelopes. Motors use bolted caps; padded straps remain only for the batteries.

## Verification and the remaining physical check

The native assembly rebuilt successfully. Final interference detection reports 114 intersections: 78 are the existing simplified shaft/rim/cast-tread interfaces and 36 are the gearbox screws entering a motor reference without modeled threaded holes. There are **no other reported intersections**. Earlier washer-to-cap and bolt-to-cover clashes were removed. The model check does not prove impact strength, clamp preload retention or real thread fit.

Both final clamp STL meshes are watertight, single bodies. The sampled wall minima are 2.772 mm; fifth-percentile thicknesses are 3.530 mm for the saddle and 3.286 mm for the cap. These exceed the DfAM skill's generic 1.6 mm unsupported FDM wall default. This is a geometric printability check, not a load rating. The report JSONs and orientation candidates are included in `Verification`; their support-volume figures are coarse upper bounds. Hole accuracy, real bridge quality and heat/impact behaviour remain printer and material dependent.

Fit one motor and wheel to one rail/doubler and one printed pair. Establish the front screw location first, then snug the rear clamp without forcing the motor off axis. Check that the wheel turns freely, the motor cannot twist or rock, the split still has adjustment and the front screws do not bottom. Check terminals, cooling openings and assembly tool access. With the full battery load installed, verify all six tires contact a flat board, and gauge screw heads, side guards and scoop on a representative seam. Run a controlled forward/reverse and pushing trial, then inspect the warm mount for slip, cracking, loosened nuts or softened plastic before making the complete batch.

## References

- [ASLONG manufacturer catalogue](https://www.aslongdcmotor.com/photo/aslongdcmotor/document/26544/catalog%20aslong%20motor_PDF00.pdf): JGB37-550 family drawing; six M3 mounting holes and nominal Ø31 pitch circle. Delivered motor details still govern.
- [Prusa PETG guidance](https://help.prusa3d.com/article/petg_2059): PETG for mechanical parts and the effect of perimeter count on strength.
- The supplied teammate STEP and the team's existing motor reference were inspected locally in SolidWorks 2025. The teammate mesh was measured with the installed DfAM tool; its private source copy is kept separately from this deliverable.
