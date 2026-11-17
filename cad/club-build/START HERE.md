# McLaren 6WD club build

**Wheel update — 15 November 2026:** the current robot with the brass hex couplers and revised rims is in [McLaren-6WD-Hex-Wheels](../hex-wheels/START%20HERE.md). Open its `SolidWorks/McLaren 6WD - Club hex wheels.SLDASM` and use its new wheel/mould print order. The steel design and P01 holders from this Club folder are retained.

This lower-cost revision uses a welded 1 mm steel frame, Shaheer's long PETG sleeves, two strapped battery trays and a single insulated electronics tray. The professional workshop revision has its own native package and GitHub release.

## What to send

- Open `SolidWorks/McLaren 6WD - Club build.SLDASM` with all 25 parts beside it.
  This is the preserved 108-instance Club baseline with earlier wheel references.
  Use the [hex-wheel assembly](../hex-wheels) for the integrated brass-coupler build.
- Use `Laser DXF` and the two `Shop handoff` diagrams for the shop. Profiles are
  1:1 in millimetres for measured 1 mm steel; final bend development depends on
  the shop coupon. Transfer-drill the real gearbox mounting pattern.
- The chassis print quantities are in `Print STL/PRINT ORDER.txt`: one holder
  trial, six total after approval, two battery trays and one electronics tray.
- [V3 wheel test](../wheel-v3-test) is a later separate rim/mould trial and has
  not been inserted into either native robot assembly.
- The holder has two floor bolts per motor. The requested four-hole floor layout
  remains unfinished; this handoff must not be read as a four-bolt design.

## What was removed

The steel floor has **12 M4 mount holes and four strap slots**, down from 52 round holes. The side guards, rear wall, scoop, five scoop webs, floor spine and electronics bridge have no round mounting holes. Their structural joints use fixtured welds. The local gearbox doublers and underfloor strips remain because the 1 mm sheet takes load at those points.

The **electronic mounting hardware count is zero**. Two ties secure the insulating PETG tray over its welded bridge. Put the IBT-2 boards on the tray's raised ribs and tie each board at two positions so the underside has an air gap. Foam tape works for the ESP32 and buck on a clean insulating pad. Add a tie or strain relief to keep plugs and wires from pulling them off. The scoop shields the boards from the front. The top remains open for ventilation and service.

The battery covers, threaded standoffs, PCB screws, outer cover fasteners and M5 chassis bolts are omitted. Two hook-and-loop straps thread through the steel base and PETG trays. They hold the batteries directly to the chassis. Use a thin pad under the batteries and smooth, sleeved strap exits. Route the XT60 and balance leads toward the centre where they remain accessible. Keep the straps clear of the leads.

## Shaheer's long holder

The sleeve retains the original **Ø37.4 mm bore, split, both original jaw holes and rear stop tabs**. It surrounds 72.5 mm of the roughly 76.5 mm modeled motor body. The overall printed length is 75.5 mm. A 20 mm opening between the rear tabs gives the terminals and wires an exit. The local feet match the existing floor holes. The lower outboard area clears the formed motor rail foot.

Use two M4×20 low button-head bolts through the floor and backing strip per motor, plus one M4×20 through the **outboard** jaw hole. The inboard jaw hole remains part of Shaheer's sleeve and sits beside the floor screw. Leave that hole empty in this assembly. The gearbox face screws provide positive rotation and axial restraint. The PETG sleeve locates the motor can and steadies it behind the face rail.

Both floor holes and both clamp stations are plain Ø4.5 mm clearance holes in CAD. The inner clamp hole is 3.8 mm from the nearest floor bolt centre, so it stays empty. Test one real motor with the wheels spinning and a supervised load. Confirm the stop tabs clear the terminals, the jaw grips before its gap closes, and the motor stays within its temperature limit.

## Battery fit

The pictured ZOP Power 3S 1,000 mAh pack is about **73 × 34 × 16 mm**. Both club trays accommodate a modeled **86 × 38 × 23 mm** pack body. The printed cavity is 39 mm wide and the open end leaves space to route leads. A shorter pack takes a small piece of soft packing at the end to prevent sliding.

The 1,000–1,100 mAh, 20–25C label range corresponds to **20–27.5 A per pack on paper**. Actual pack condition, voltage sag and the startup current of three motors on one driver determine usable current. Test each branch on a supervised current-limited bench setup. Use a fuse and accessible disconnect per pack, select the fuse and wire from measured current and component ratings, and keep motor current off the breadboard. [Infineon BTS7960 datasheet](https://www.infineon.com/assets/row/public/documents/10/57/infineon-bts7960-ds-en.pdf)

## Assembly order

1. Check the exact gearbox boss and shaft location using one C04 coupon and a real wheel. Select three widely spaced mounting positions on the actual gearbox. Confirm thread, safe screw depth and tire-side head clearance. The nominal face pattern in CAD uses alternating holes at 120°.
2. Verify the cutter and brake against the T01 and scoop strip coupons. Cut the flat frame parts and approved formed blanks. Dry-fit the rails, tires, guards and scoop in the fixture. The two motor shafts on opposite sides share the same height.
3. Fixture the base flat. Tack the bare steel rails, guards and rear wall, then recheck wheel stations and square. Fit the centre spine and electronics bridge. Form and seat the scoop on all five webs before joining. Put the webs at Z = −124, −62, 0, +62 and +124 mm. Run the shop's qualified short weld sequence on this thin sheet. [TWI welding distortion guidance](https://www.twi-global.com/media-and-events/insights/preventing-and-correcting-weld-material-distortion)
4. Deburr and clean every cut edge and strap slot. Install the motor hardware, printed parts, battery straps and electronics after the steel work. Fit insulation and strain relief around all cable exits and cover exposed power terminals.
5. With both packs and all hardware installed, check all six tire contacts, wheel sweep, floor flatness and the scoop toe over a ring seam. CAD ground clearance is 6 mm under the floor, 2.8 mm under the M4 heads and 2 mm at the toe. Apply a supervised centre push and corner push before competition.

## What the checks cover

The reopened club assembly STEP contains 108 components, including hardware and reference envelopes, at **294 × 290 × 102 mm**. Exact solid checks found the expected wheel and gearbox reference overlaps. The checked cut profiles have at least 4.25 mm of remaining metal at a cut feature in production parts. The tightest strap or round-hole edge clearance in the floor is 8.5 mm. Final bend allowance, fit after welding, tire compression, actual motor vents, electrical current and impact strength require the bench and shop checks.
