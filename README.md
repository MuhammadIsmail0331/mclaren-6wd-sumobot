# McLaren 6WD Sumobot

A RAC student sumobot built around six JGB37-550 gearmotors, custom silicone tyres,
two IBT-2 drivers and two separate 3S LiPo supplies. The Club design combines a
1 mm welded steel frame with printed long motor holders and insulating trays.

**Latest full native assembly:** [Club with hex wheels](cad/hex-wheels).
**Latest wheel-only test:** [V3 rim and mould — one of each](cad/wheel-v3-test).
The V3 test rim has not yet been inserted into the complete native assembly.

![Club hex-wheel assembly](cad/hex-wheels/Views/Club%20hex%20wheels.png)

| Need | Start here |
|---|---|
| Open the full robot in SolidWorks 2025 | [Hex-wheel assemblies and parts](cad/hex-wheels/SolidWorks) |
| Print one V3 wheel/tool test | [Three STLs and casting sequence](cad/wheel-v3-test) |
| Cut, bend and fixture the Club steel | [Laser profiles](cad/club-build/Laser%20DXF) and [shop diagrams](cad/club-build/Shop%20handoff) |
| Print holders, battery trays and electronics tray | [Club chassis print order](cad/club-build/Print%20STL/PRINT%20ORDER.txt) |
| Buy fasteners | [Counts, lengths and fit restrictions](docs/fasteners-and-supplies.md) |
| Wire the two packs | [Power distribution and bench checks](docs/power-distribution.md) |
| Compare revisions | [Revision guide](docs/revision-guide.md) |
| Inspect the evidence | [CAD verification](docs/cad-verification.md) |
| Download a complete package | [Releases](https://github.com/MuhammadIsmail0331/mclaren-6wd-sumobot/releases) |

Extract each native revision into its own folder and keep its referenced parts
beside its assembly. The Club hex-wheel assembly contains 120 fixed instances
and resolves 27 unique part definitions. It is a geometric fit prototype, not a
motion-mated simulation or a demonstrated competition result.

The nominal Club outline is **294 x 290 x 102 mm**, so it does not fit a 250 mm-square
class. Current competition limits, actual mass, tyre deflection, weld quality,
loaded clearance, motor screw fit, current and failsafe behaviour require physical
checks. The requested four-floor-hole long-holder revision is still outstanding;
the saved model has two floor bolts per holder.

The V3 STL set is intended for one coupler dry fit and one successful silicone cast
before printing the other five rims. Its supplied mould is a continuous ring with
a printed pin; the earlier hex-wheel tool instead has two removable wall halves
and a metal centre bolt. Their instructions and hardware are kept separate.

Earlier [Workshop](cad/rev-d-workshop), [Rev C](cad/rev-c), [fabrication review](docs/fabrication-joint-review.md)
and [research brief](docs/research-and-design-brief.md) remain available for comparison.
See the separate [Pakistan robotics competition calendar](https://github.com/MuhammadIsmail0331/pakistan-robotics-competition-calendar).

Next checks: [one V3 fit/casting trial](https://github.com/MuhammadIsmail0331/mclaren-6wd-sumobot/issues/18),
[the four-floor-hole holder request](https://github.com/MuhammadIsmail0331/mclaren-6wd-sumobot/issues/19),
[motor station](https://github.com/MuhammadIsmail0331/mclaren-6wd-sumobot/issues/5),
[steel fabrication](https://github.com/MuhammadIsmail0331/mclaren-6wd-sumobot/issues/6),
and [electrical measurements](https://github.com/MuhammadIsmail0331/mclaren-6wd-sumobot/issues/7).
Report a measurement, test result or current organiser rulebook with the revision
and part ID. CAD-only checks do not close physical validation tasks.
