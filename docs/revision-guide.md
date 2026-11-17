# Choose the right revision

| Folder | What it represents | Robot native assembly | Wheel/tool status |
|---|---|---|---|
| `cad/rev-a` through `cad/rev-c` | Earlier archived studies | Preserved | Earlier wheel references |
| `cad/rev-d-workshop` | More elaborate bolted Workshop prototype | 180 instances, 40 part definitions | Preserved older interface |
| `cad/club-build` | Lower-hardware welded Club chassis | 108 instances, 25 part definitions | Earlier rim references |
| `cad/hex-wheels` | Club with brass couplers | 120 instances, 27 referenced definitions | Integrated 15 Nov rim; split mould and metal centre bolt |
| `cad/wheel-v3-test` | Latest rim/mould trial, 17 Nov | **No full assembly update** | V3 centre adaptation; author's printed-pin base and one-piece wall |

For the full robot, open `cad/hex-wheels/SolidWorks/McLaren 6WD - Club hex wheels.SLDASM`.
Keep all 35 part documents and 3 assemblies in that same extracted folder; 27 of
the definitions are referenced by the full robot. For the next wheel test, use
the three STLs and instructions in `cad/wheel-v3-test`. Do not mix the two moulds'
hardware, orientation or fill instructions. Chassis prints remain in `club-build`.

The latest integrated Club envelope is 294 x 290 x 102 mm. It does not fit a
250 mm-square class. A 304.8 mm square would accommodate this nominal CAD outline,
but the organiser's current inspection rules, mass and actual fabricated size
must be checked independently. No event eligibility is certified here.

The four-floor-hole request is unimplemented. The saved Club holder uses two
floor bolts and one active clamp bolt; the gearbox face screws are a separate
positive motor restraint. A real motor's mounting thread/depth remains to verify.

The team designed the V2/V3 rim/holder and supplied mould concepts. Shaheer's native
rim is retained as the V3 donor; Soban's supplied mould meshes are retained without
shape changes. The central coupler adaptation, packaging and recorded CAD/mesh
checks were assisted by Codex. Supplier-derived components are simplified fit
references unless the individual file says otherwise.

No new CAD or physical work was performed during the 18 November publication.
It packages the saved work and exposes unresolved tests; a GitHub merge or passing
artifact check does not certify a robot or a manufacturing process.
