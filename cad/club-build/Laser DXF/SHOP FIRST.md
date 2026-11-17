# RML cut and forming notes

Use the DXFs at 1:1 in **millimetres**. Scale check the C01 base at **250 × 288 mm**. All DXF entities on the CUT layer are cut paths. Bend lines are in the separate table and drawing. Apply kerf compensation on the machine.

**Start with T01 and one C04.** Use the same measured 1.0 mm steel planned for the structure. Check the Ø4.5 bolt hole, Ø12.6 boss coupon and 22 × 4 strap slot. Reuse the successful C04 as one of the six doublers. If only 0.8 mm is available, prove the bend and weld settings and confirm with the supervisor before using that stock on the frame.

| ID | Qty | Fabrication |
| --- | ---: | --- |
| C01 Base | 1 | Flat. Twelve M4 holes and four rounded slots for 20 mm straps. |
| C03 Mount backing strip | 2 | Flat. Mount under the base to spread the holder load. |
| C04 Gearbox doubler | 6 | Flat. Confirm the Ø12.6 locator. Transfer drill the real gearbox through rail and doubler together. |
| C08 Scoop support web | 5 | Flat. Seat against the actual formed scoop. Fixture from Z = −124, −62, 0, +62, +124 mm. |
| C09 Floor spine | 1 | Flat plate installed upright on the floor centreline. |
| C02 Motor rail | 2 | One 90° fold to form the bottom foot inboard. Left/right mirrored. Bend datum is the bottom-foot free edge. Keep the inside gearbox face at Z = ±100 mm. |
| C05 Wheel guard | 2 | One inward 90° top return, starting from the guard's lower long edge. Mirror left/right. The front 30 mm relief clears the scoop. |
| C06 Rear wall | 1 | One inward 90° top return. Datum is the lower edge. Weld both rear corners to the side guards. |
| C07 Scoop | 1 | Three bends measured from the forward toe. First rotate the next face up 18°, then another 42° to 60°, then turn back 60° to the horizontal top lip. |
| C10 Electronics bridge | 1 | Two 90° bends so both notched ends land on the floor and the middle span sits above them. Start measuring from either end. Fit notches over the centre spine. |

The formed blanks are developed for **1.0 mm sheet, 1.5 mm inside radius and K = 0.40**. The C07 blank is **282 × 160.736 mm** and its bend centres are **15.982, 41.127 and 142.896 mm from the toe edge**. Ask the brake operator to prove the radius and development with a same-stock strip before cutting or forming the full-width pieces. Bend sequence and springback correction depend on the available die and punch. If the trial needs a different development, update the fold data before the production cut. [Protolabs forming guidance](https://www.protolabs.com/services/sheet-metal-fabrication/design-guidelines/)

The motor pattern is deliberately transfer-drilled. The nominal 3-hole CAD pattern is on a 31 mm circle, offset 6 mm from the shaft, with at least 3.88 mm of metal beside the screw holes in the modeled doubler. Keep at least 3 mm of solid metal to a cut edge or boss opening when laying out the measured pattern. Clamp the loose template or rail away from the motor during drilling. Deburr, then confirm the selected screws seat without bottoming or catching a wheel.
