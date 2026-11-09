# McLaren 6WD workshop handoff

Use this folder for the first fit and workshop trials. It supersedes the previous Rev D fit folder for the motor holder. Open **SolidWorks/McLaren 6WD - Workshop.SLDASM** in SolidWorks 2025 with all its part files in the same folder. The assembly shows all six revised holders and both widened rail returns. The previous saddle and cap components are still in the assembly and hidden. Part 32 comes from Shaheer's original SolidWorks file and retains his feature history with the chassis-fit operations added.

If SolidWorks requests a rebuild after opening the extracted archive, press **Ctrl+Q**. Keep the assembly and its 40 part files together when sharing the folder.

## Tuesday split

| Group | Start with | Release check |
| --- | --- | --- |
| Tires | Check the existing mold, rims and shaft fit. Cast one representative tire before committing the batch. | Gauge loaded diameter and width, concentricity, tread bond and retention on the actual shaft. Bring six assemblies to a flat plate to check that all contact. |
| RML and workshop | Take the pilot DXFs, one motor and wheel, measured stock and sample fasteners. Ask the operator for a small same-stock laser, bend and join trial. | Confirm mm scale, kerf, grade/thickness, bore and fastener fit, brake tooling, and joint method. Keep the base flat after joining. |
| Club print | Send the single-holder test order in this folder. | Fit to one motor and one face rail before printing the other five. |
| Electronics | Inventory the hardware and test one motor and one driver on a supervised current-limited bench supply. | Verify each branch at increasing load, then both sides together with proper protection and radio failsafe. |

## Design and geometry check

- **Holder 32.** Maximum width 60.75 mm on a 62 mm motor pitch. Length 32 mm. Shaheer's Ø37.4 mm bore, split sleeve, and one original clamp-screw station are retained. The wider original jaw area leaves 2.5 mm of nominal plastic outside the jaw hole and a minimum 1.25 mm envelope gap to the next holder. The STL sampled minimum wall is 1.98 mm. The shorter ends clear the floor stiffener and rail. The remaining sleeve needs the steel gearbox face rail for positive rotation and axial restraint. Its end stop was outside the fit length. Two new local feet use the existing 49 mm floor hole spacing. Nominal shaft height remains 28.5 mm.
- **Motor hardware.** Two M4×20 low-head bolts secure each foot through the steel backer and floor. A separate M4×20 squeezes the original jaw. Use 2.0 mm total spacer thickness under its head and an Ø8 mm narrow washer under its locknut. The spacer keeps the protruding screw clear of the pack panel. Verify hand tool access before installing the pack covers. Ø9 mm washers fit the floor bolt seats. Confirm purchased nut and head dimensions against the fit sample.
- **Solid model audit.** The native assembly rebuilt and saved with 180 instances, including 12 hidden previous mount components. Its envelope is 292 × 290 × 110 mm. SolidWorks counted 114 expected reference intersections at the wheel models and unthreaded gearbox screw holes, plus 12 jaw hardware edge contacts below 0.002 mm³ each. Check real washer seating and tool access on the first print. The visible STEP cross-check found the known reference overlaps and no additional overlaps above 0.02 mm³. Rubber deflection, weld distortion, wiring and actual hardware fit need the bench checks below.
- **Fit clearance.** Nominal underside clearance is 6 mm at the floor, 2.8 mm below the modeled M4 floor bolt heads and about 2 mm at the scoop toe. Guard return to tread is about 2 mm vertically. Test with both packs, all electronics and hardware. Verify tires spin and steer under load without rubbing or lifting another wheel.

## Sheet metal before the full cut

Use measured **1.0 mm nominal steel** for the initial structural trial. If all available sheet is 0.8 mm, trial the joining method and assess the floor, nose and rail supports before substituting. Two sheets require load transfer between them to behave as a single laminate. Keep the bending and joining work separate from installed electronics, batteries and printed parts.

| Part | Workshop disposition |
| --- | --- |
| 01 base and 24 backing strips | Flat pilot profiles, base 243 × 286 mm, backer 186 × 20 mm. Check at 1:1 scale. Before cutting the full floor, agree on the scoop attachment and rear tabs. The nose row leaves 1.75 mm of steel from hole edge to base edge. Check actual backing, washer placement, and an off-centre push. |
| 02 motor rail and 23 local face doubler | Transfer-drill versions contain the Ø12.6 mm locating openings only. Measure the real boss and eccentricity before using those openings. Make one 23 coupon and fit the screw heads behind a real wheel. Use a separate template to transfer the measured pattern to the steel layers. |
| 03 motor rail return | The original Rev C flange leaves 0.25 mm of steel at one hole edge. Use the widened shop-review profile, 195 × 14.5 mm, minimum 2.75 mm hole-edge ligament, with the same hole centers. The STEP check clears the stiffener, deck posts and scoop feet. Gauge the 0.5 mm nominal margin to the nearest deck spacer in the real assembly. Ask the shop to choose a one-piece bend or a properly fixtured separate joint and confirm the final flange before batch cutting. |
| 06 scoop and 26 underlay | Formed solids. The three outer-scoop angle increments are 14°, 20°, 24°. Bend allowance, tooling, and a complete unfolded blank are pending. Make a short strip coupon using the shop's actual stock and brake. Gauge the real toe height and nested skin before a full-width blank. |
| 07 and 08 nose ribs and feet | Five each. Fit ribs against the actual formed skin. Rev C's small 08 tabs leave about 1.25 mm from the M5 hole edge to one end. Shop should detail a wider backing or attachment and test the steel subassembly before the batch. |
| 09, 10 and 27 side guards, brackets and returns | Verify actual tire sweep and fastener access. The 10 angle is an undrilled fit model. Transfer drill from the actual guard and floor after trial assembly. Detail the folded return or joining method. |
| 11 and 28 rear wall and return | Detail two rear corner connections and the floor tabs. Prefer folded returns or bolted internal angles with two separated fasteners per leg where space allows. |
| 19 upper front closure | Define the attachment clips, cover service access and any gussets into structural steel. The gussets and rear corner joints are still separate design work. |

The folder has five pilot DXFs. It has no released SolidWorks shop drawings or full scoop/guard flat-pattern package. The original Rev C narrow 03 return and nominal unverified gearbox-hole patterns are superseded for workshop use.

## Bench acceptance before six prints or a match

1. Gauge both battery packs, their plugs and cable exit. The CAD pack envelope is 100 × 35 × 27 mm before wires. Verify padding and straps hold each pack independently. Verify the two real driver PCB hole patterns, terminal height and access using a 1:1 paper check or one print.
2. Slip the first holder onto a real motor. Run the jaw bolt through the actual washer stack. Verify that the jaw tightens while there is still a gap, the case cannot turn or slide by hand, the print does not whiten or crack, and the terminals and vents remain accessible. Check the grip after a supervised warm motor test.
3. Gauge the gearbox's mounting thread, pattern and safe depth, then test one rail stack and mounted tire. The starting M3×5 screw plus 0.5 mm washer would engage about 2.5 mm through 2.0 mm steel. That is a modeled stack, pending a physical depth check.
4. Weigh the finished robot with both packs and all hardware. Check the assembled outer dimensions, ring material, edge rules, control mode and failsafe with the organizer. Bahria's TechFusion page lists 14 November 2026 and Sumo Wars (7 kg). The page does not publish the footprint or the full technical rulebook. Confirm those separately with the organizers before committing to TechFusion. [Official TechFusion event](https://www.techfusionbu.com/)

## Circuit bench checklist

- Bring six motors, two IBT-2 boards, two labeled 3S packs, balance charger, per-cell checker, ESP32, buck converter, matching XT60s, insulated cable, multimeter and current measurement. Bring a safe stand to lift all tires for powered tests. Identify battery condition, capacity, discharge rating and connector polarity.
- Fit a fuse close to each pack positive and an accessible means to isolate both drive branches. Keep pack positives separate. Give each driver its own high-current feed and return. Establish a defined logic ground reference per the actual IBT-2 board, with no motor return through jumper wires, breadboard or ESP32 ground traces. Keep high-current wiring off the breadboard. Add abrasion protection, heat shrink, strain relief and covered terminals.
- Measure the buck output before connecting the ESP32. Use the board's rated supply input and verify logic voltage at the particular driver module's inputs. If the board's input buffer needs a higher guaranteed logic level, use a compatible logic translator. Implement driver enable default-off and test loss of command and brownout recovery.
- Verify each motor direction on the stand before paralleling the three motors on a side. Measure startup and push current progressively on a supervised, current-limited test. The Infineon chip's 43 A current-limiting figure is not a continuous rating for an IBT-2 module, connector or PCB. Use measured branch current, wire and connector ratings, thermal behavior and the supervisor's approval to select protection. Keep any edge or opponent sensors dependent on the event control rules. [Infineon BTS7960 datasheet](https://www.infineon.com/assets/row/public/documents/10/57/infineon-bts7960-ds-en.pdf)
