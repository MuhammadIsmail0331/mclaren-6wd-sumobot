# Integrated Club hex-wheel prototype — 15 November 2026

This is the latest saved full native robot assembly: **120 fixed instances and
27 unique referenced part definitions**, all local to its SolidWorks folder.
The folder contains 35 part documents and 3 assemblies in total because the wheel,
tooling, gauges and reference definitions also live here.

![Club hex-wheel assembly](Views/Club%20hex%20wheels.png)

Open `SolidWorks/McLaren 6WD - Club hex wheels.SLDASM` with the entire folder
extracted. `Wheel and coupler.SLDASM` and `Split mould - assembly.SLDASM` are
separate inspection assemblies. Placements are fixed, not motion mates.

- [Design, fit assumptions and casting instructions](START%20HERE.md)
- [Native files](SolidWorks), [exchange geometry](STEP), [STLs](Print%20STL)
- [Print order](PRINT%20ORDER.txt), [verification](Checks/Final%20verification.json)
- [Wheel/tool hardware](Hardware%20for%20wheels%20and%20mould.md)
- [Preserved Club sheet/holder design](../club-build)

The integrated rim has a 23 mm hub and 4 mm retaining web. Its four-part tool uses
two separate wall halves and a removable metal centre bolt. These are the earlier
15 November designs. The **later V3 rim and supplied one-piece-ring mould are a
[separate test set](../wheel-v3-test)**; do not mix their print/tool instructions.

CAD checks preserve the 294 x 290 x 102 mm envelope. No physical print, casting,
impact or FEA result is claimed. The real coupler, motor and fabricated chassis
must pass the documented fit checks before batching.
