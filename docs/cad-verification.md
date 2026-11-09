# CAD verification

## Rev C: latest saved fit prototype

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
