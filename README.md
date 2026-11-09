# McLaren 6WD Sumobot

A RAC chassis project for remote-controlled robot sumo: six JGB37-550 gearmotors, custom silicone tires, two IBT-2 drivers and two 3S LiPo packs. Each driver and pack serve one side.

**Rev D Workshop is the latest published fit prototype.** It uses the team's adapted split sleeves and widened motor-rail returns. The native package was extracted and rebuilt in a separate folder in SolidWorks 2025.

![Rev D workshop isometric view](cad/rev-d-workshop/Native%20assembly%20view.png)

| Start here | What is included |
| --- | --- |
| [Rev D workshop build](cad/rev-d-workshop) | Native assembly, 40 referenced parts, STEP, first-fit print files, pilot laser profiles and hardware list |
| [Rev C CAD and exports](cad/rev-c) | SolidWorks 2025 assembly, 36 part files, assembled STEP, individual STEP exports and views |
| [Motor mount review](cad/rev-c/Motor%20mount%20review.md) | Positive gearbox restraint, printed clamp fit, hardware, height and ground clearance |
| [Fabrication joint review](docs/fabrication-joint-review.md) | Team proposals for front support and rear corners, plus the joints to finish before cutting |
| [Rev C build and shopping list](cad/rev-c/Build%20and%20shopping%20list.md) | Sheet parts, PETG print settings, fasteners and bench checks |
| [Motor supplier check](cad/rev-c/Motor%20source%20verification.md) | Electrobes dimensions and the unresolved interface details |
| [Parts and quantities](cad/rev-c/Parts%20and%20quantities.csv) | Make, print, source or reuse for each CAD part |
| [CAD verification](docs/cad-verification.md) | Saved native checks, scope and limitations |
| [Earlier CAD](cad) | Rev A and Rev B preserved for comparison |
| [Research brief](docs/research-and-design-brief.md) | Initial rules research, sizing and wedge tradeoffs |

Download the native Rev D archive from [Releases](https://github.com/MuhammadIsmail0331/mclaren-6wd-sumobot/releases). Extract the full archive and open `SolidWorks/McLaren 6WD - Workshop.SLDASM` with its part files beside it. Keep revisions in separate folders because some component names are reused.

The package includes eight STL print files and five flat motor/floor DXFs. The DXFs are **not a complete chassis flat-pattern set**. The scoop, formed members and proposed joints still need shop-specific bend and joining details. Print one motor clamp pair and verify the delivered gearbox interface before batching the motor mounts or rails.

Rev C measures **292 x 290 x 110 mm** in CAD. It fits geometrically within a 304.8 mm square and does not fit a 250 mm square. Confirm the current event's rules independently. The native model uses fixed component placements; its interference audit is a geometric fit check, not an impact-strength or manufacturing approval.

Open an issue with dimensions, a CAD screenshot, a test result or the organiser's current rulebook. Include the revision used. Existing motor, sheet-metal, drivetrain and competition-rule validation issues remain open until the physical checks are recorded.

See the [RAC competition calendar](https://github.com/MuhammadIsmail0331/pakistan-robotics-competition-calendar) for related events.
