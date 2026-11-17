# CAD verification

## Club, hex-wheel and V3 evidence added 18 November 2026

| Saved set | Recorded evidence | Limits |
|---|---|---|
| Club chassis | Reopened/rebuilt; 108 fixed instances, 25 part files, no external dependencies | Physical gearbox/holder/weld tests remain open |
| Integrated hex wheels | Reopened/rebuilt; 120 instances, 27 robot references; 294 x 290 x 102 mm | Fixed placements; no FEA, casting or impact test |
| V3 wheel/tool | Three final STLs watertight, one body each, mm scale; revised rim BRep valid; zero overlap with saved adapter reference | Not integrated into native robot; actual print/coupler fit untested |

See [Club native audit](../cad/club-build/Native%20SolidWorks%20verification.json),
[hex-wheel final verification](../cad/hex-wheels/Checks/Final%20verification.json),
and [V3 geometry check](../cad/wheel-v3-test/Checks/Geometry%20check.json).
The V3 base/wall section at Z=8 mm has no crossing boundaries or sampled boundary
midpoints inside the other part, with 0.225 mm minimum section gap; this is one
section, not a complete mesh collision proof. The mould base's native file gave
future-version error 8192 in SolidWorks 2025, so supplied author STL exports were
checked instead. Original native mould feature trees were not inspected.

V3 wall samples: rim minimum 1.498 / fifth percentile 1.998 mm, base 2.207 / 4.000,
wall 2.139 / 3.977. The rim retains a local thin lower recess feature that is below
the generic 1.6 mm unsupported FDM guide; support/inspect it during the first print.
The hub's nominal walls are 3.0 mm at the barrel entry and 3.34 mm at hex corners.
Mesh sampling and passing package checks are not exhaustive wall or strength proofs.

The original report dates and values are preserved. Publication does not imply
that physical tests happened today. Known holder floor-hole work remains open.

## Rev C: archived fit prototype

SolidWorks 2025 rebuilt the native Rev C assembly with **162 component instances and 36 unique native part documents**. It was reopened, its referenced component paths checked, and all 36 parts plus the assembly reported no pending saved changes. Native saving returned success with zero reported errors and warnings.

| Check | Recorded result |
| --- | --- |
| Bounds | X -140 to 152 mm; Y 0 to 110 mm; Z -145 to 145 mm |
| Overall envelope | 292 x 290 x 110 mm |
| Reference motor shaft/rim regions | 6 |
| Reference rim/cast-tread regions | 72 |
| Face screws entering unthreaded gearbox reference | 36 |
| Other modeled intersection regions | 0 |

The 36 screw regions reflect 2.5 mm of nominal engagement in a simplified gearbox without modeled threaded holes. They do not establish the real motor's safe thread depth. The 78 existing wheel-interface regions model the team's reference hardware. The earlier washer-to-cap and clamp-bolt-to-battery-panel clashes were removed before the final run.

The full 110 mm height is recorded in the assembly construction log. The later interference audit began in the drivetrain/service display, so its `GetBox(0)` line reports 60 mm with upper covers hidden; that visible-display box is not the complete robot envelope. The final saved-state run restored all components.

The native evidence is in [Rev C Verification](../cad/rev-c/Verification). Public text logs use project-relative paths. The complete assembly and component geometry are in [Rev C CAD](../cad/rev-c).

Both final motor-clamp STL meshes are watertight single bodies. Sampled minimum thickness is 2.772 mm for each; the fifth-percentile values are 3.530 mm for the saddle and 3.286 mm for the cap. These exceed the included DfAM reference's generic 1.6 mm unsupported FDM-wall default. This is a mesh/printability comparison, not a mechanical strength result. The orientation and wall-thickness reports are included with the revision.

Rev C uses fixed placements and nominal 1.0 mm steel. Actual motor dimensions, clamp fit, wheel deformation, terminals, wiring, loaded ground clearance, sheet grade, bend development, fastener preload and physical joint behaviour require bench/shop checks. No impact or weld simulation has been run. The [front-gusset and rear-corner proposals](fabrication-joint-review.md) are not present in this saved geometry and have not been checked for interference.

## Rev B: archived baseline

The saved Rev B assembly rebuilt with 102 instances and 33 native part documents. It has the same 292 x 290 x 110 mm envelope. Its 78 reported interference regions were confined to the simplified shaft/rim and rim/tread interfaces. Face and clamp fastener envelopes were not included in that audit.

Keep the older revisions for comparison. Their existence does not resolve the open motor-coupon, thin-sheet joint, drivetrain and current competition-rule checks.
