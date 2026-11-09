# McLaren 6WD Rev C

Read **Motor mount review.md** first for the revised motor hardware and test-fit requirements.

Use this fit revision for the team's 0.8–1.0 mm sheet supply. Rev A called out thicker stock even though the team chat recorded about 1 mm. Rev C uses **1.0 mm nominal steel** for the floor, motor rails, scoop, guards and their reinforcements. Use a micrometer at several points and confirm the material with the shop. 0.8 mm is a candidate for the upper electronics closure or another lightly loaded panel. Substitution on the floor, motor mounts or nose needs its own fit and load check.

## Laser cut, form or join

| CAD parts | Quantity | Workshop operation |
|---|---:|---|
| 01 floor | 1 | Laser cut from 1.0 mm. Keep it flat when joining the hat sections. |
| 02 rail, 03 return strip, 23 gearbox doubler | 2 rails, 2 returns, 6 doublers | Laser cut. Form a return integrally if the shop can hold the flange and hole location, or join the separate return as shown. Transfer-drill the motor face patterns through both layers using the real gearbox. Confirm screw engagement and head height with a tire installed. |
| 24 underfloor clamp backing strip, 25 floor hat stiffener | 2 of each | Laser cut the backing strips. Fold or fabricate the 10 mm-deep hats, then join their toes to the floor. The hats are 68 mm long and sit between motor stations. The backing strips spread clamp-bolt load into the floor. |
| 06 three-bend scoop, 26 underlay, 07 rib, 08 rib foot | 1 scoop, 1 underlay, 5 ribs, 5 feet | Laser cut blanks, form the scoop and liner separately, then fixture and join. Three rotations are 14°, 20° and 24°. The nested underlay starts at X = 135.5 mm, 16.5 mm behind the front edge. The rounded 1 mm outer skin runs continuously through the toe. Join ribs to the liner and their feet. The nose assembly bolts to the floor. |
| 09 side guard, 27 top return, 10 guard angle | 2 walls, 2 returns, 4 angles | Laser cut and form or join. The 11 mm return points inward above the tread, with 2 mm nominal clearance from the tread top to the return underside. Transfer drill the guard angle to match the real guard and floor holes. |
| 11 rear bumper, 28 rear return, 19 upper front closure | 1 each | Laser cut and join the bumper/return. Fit rear fixing tabs and upper closure clips after hardware fit. Small standard angles or 1 mm shop-made tabs are suitable for the removable covers. |

The CAD shows formed shapes. Brake radius, die opening, minimum flange, bend sequence, and flat development require a same-stock coupon and shop confirmation. Confirm joining on scrap and keep weld distortion out of the axle datums. Deburr the scoop, corners, openings and any cable pass. [Protolabs sheet metal guidelines](https://www.protolabs.com/services/sheet-metal-fabrication/design-guidelines/) · [SendCutSend bending guidance](https://sendcutsend.com/services/cnc-bending/)

Flat-sheet bending stiffness scales with thickness cubed. At the same span, 0.8 mm has about **51%** of the bending stiffness of 1.0 mm. Two 1 mm layers that slip behave closer to two individual sheets. A fully composite 2 mm section has eight times the stiffness of one 1 mm sheet. Actual joined stiffness depends on shear transfer, fastener spacing and contact. Stiffen broad spans by giving the section depth. Use the double skin, ribs and backers where loads enter the chassis.

The toe still warrants a physical load check. In a simple 20 mm-wide cantilever strip model, a 50 N load 16.5 mm from support gives about **248 MPa** bending stress for 1.0 mm and **387 MPa** for 0.8 mm. This is a sensitivity calculation with assumed contact width and idealized support. The nose liner, shell and neighboring ribs distribute real loads. Test the middle and outer corners and measure the loaded toe clearance on a representative ring seam. The nominal outer toe underside is 2 mm above the floor.

## 3D print

| CAD parts | Quantity | Material and print start |
|---|---:|---|
| 04 motor saddle and 05 motor cap | 6 pairs, after one test pair | Plain PETG, print on the flat axial end with the bore axis vertical. 0.20 mm layers, 4–5 walls, 5 top and bottom layers, about 25–35% infill in thicker regions. The arch has about 3.3 mm radial material. The part's ears take the bolt load through the walls and washers. Check that horizontal bolt holes print cleanly and clear them with a 4.5 mm drill if needed. |
| 12 insulated LiPo tray and 13 access panel | 2 each | PETG. Print flat, 3 walls, modest infill where a core exists. Thin floors and walls will be mostly perimeters and skins. Use thin foam and 20 mm straps for each battery. |
| 15 electronics deck, 18 side riser, 20 lid, 21 rear closure | 1 deck, 2 sides, 1 lid, 1 rear | PETG, print flat. 3 walls, 4–5 top and bottom layers, about 15–20% where a core exists. Largest footprint is the 145 × 198 mm lid. Put washers under cover screws. |

The printed motor mount is a **bolted saddle and cap**, with a 37.0 mm prototype bore, 14 mm axial width, and a 0.6 mm split. The steel face rail and gearbox screws establish alignment and take torque reaction. The clamp restrains rocking and distributes impact load into the backer. Fit thin compliant anti-slip strips only as needed. Use a sample motor to check bore size, pad fit and alignment, then test forward/reverse torque and check the print again warm. Keep clear of terminals, seams and motor vents. The diameter and axial station come from the team's simplified motor STEP. Compare against the six real motors before batching parts. The modular layout is inspired by the team's ProBot references. [ProBot](https://www.probotjo.com/) · [Prusa PETG and perimeters guidance](https://help.prusa3d.com/article/petg_2059)

Use the slicer's measured grams and preview. Inspect the clamp ears, arch and bolt holes for continuous walls. Keep infill low in covers and trays, and use a local modifier around loaded clamp ears only if the test part needs it. Parts 14, 16 and 17 in CAD represent purchased hardware. Part 22 is a tire envelope for the existing cast wheels.

SolidWorks volumes for the saddle and cap total 14.12 cm³ per motor. At an assumed PETG density of 1.27 g/cm³, that is about **17.9 g per pair** at solid-equivalent density, or **108 g for six pairs**. Use the slicer for the actual print estimate, including perimeter count, brim and any supports.

## Buy or source

Lengths below are prototype starting lengths for the modeled stack. Take one assembled joint to the shop to verify nut, head and washer dimensions. Buy low-profile steel machine screws, flat washers and nylon-insert locknuts for through-joints. Use wide washers against thin steel and PETG where the footprint allows them. Keep underside screw heads and protruding threads within measured ground clearance. Use the low head below and put the locknut on top for clamp joints.

| Item | Starting quantity | Used for |
|---|---:|---|
| M4 × 40 button-head screws, M4 washers and locknuts | 12 sets, buy 15–16 | Two through each motor saddle/cap, floor and backing strip. The nominal material stack to the cap top is 32.5 mm before washers and nut. |
| M5 × 12 low-profile screws, wide M5 washers and M5 locknuts | 21 sets, buy 25 | 8 rail-to-floor, 5 scoop feet, 4 guard angles to floor, 4 walls to angles. Drill mating angles after fitting. |
| M4 × 60 screws and M4 × 45 mm through-sleeves | 4 sets | Deck-to-floor stack. Buy rigid sleeves or cut and deburr tube. A rigid 40 + 5 mm sleeve stack is another way to reach the modeled height. Use the insulated deck and keep conductive sleeves and hardware away from PCB pads. |
| M3 × 50 screws, M3 locknuts, 35 mm nylon clearance sleeves | 8 sets | Pack access panel. For female–female threaded M3 spacers, use separate short screws at each end matched to thread depth. |
| 4 mm insulating M3 sleeves, M3 × 12 screws, nylon washers and nuts | 8 sets, confirm first | Two driver modules. Confirm hole diameter and pitch on the actual IBT-2. Use insulating spacers and verify terminal/underside clearance. |
| M3 × 8 or M3 × 10 pan-head screws and nuts, small cover angle tabs | ~8–12 sets | Removable electronics panels. Drill the tabs in place. The rear armor uses up to three M4 joints with separate tabs if it is bolted instead of welded. |
| M3 × 5 low-head gearbox screws and 0.5 mm washers | 36 sets; confirm motor first | Nominal 2 mm steel face stack gives 2.5 mm engagement. Verify actual thread, safe depth, pitch circle and wheel clearance. |
| Padded straps, foam, grommets and insulated hardware | 2 straps plus shop stock | LiPo retention, cable protection and board insulation. A strap is for each battery. The motor caps bolt down. |

For electronics hardware, Alpha Electronics on College Road, Rawalpindi lists M3 nylon spacers through 35 mm. Confirm whether the listed spacers are threaded or plain clearance, and take the driver board to check the short spacers. Use a metric fastener shop for the M4 and M5 steel hardware. [Alpha Electronics spacer listing](https://alphaelectronics.pk/product/m3-double-pass-hexagonal-nylon-spacer-10mm-35mm/) · [eVision PCB spacers and grommets](https://www.evselectro.com/pcb-spacers-standoffs)

## First bench checks

1. Measure the 1.0 mm stock, real motor can and gearbox pattern, and one installed wheel stack. Print one clamp pair and fit one rail coupon with the actual screw heads.
2. Check the batteries and board plugs, clamp slip, fastener access and heated motor fit. Verify the 2 mm nominal guard-to-tread vertical margin with the real wheel.
3. Form a scoop coupon. Gauge the assembled floor and scoop on the loaded robot, test center and corner pushes, and check that the ring surface remains undamaged. Confirm joint and fastener sizes before ordering the full cut or print batch.

## SolidWorks verification

Rev C rebuilt with 162 instances and a 292 × 290 × 110 mm bounding box. Of 114 reported intersections, 78 belong to simplified wheel interfaces and 36 to screws entering an unthreaded gearbox reference. No other intersections were reported. See **Motor mount review.md** for the revision details, measured print geometry, clearances and physical checks. The native assembly uses fixed component placements; the export is an assembled fit model. Sheet-metal bend development still needs shop confirmation.
