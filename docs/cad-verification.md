# Rev B CAD verification

The final SolidWorks 2025 audit rebuilt the saved assembly with **102 component instances**. The assembly contains 33 part documents. Model extents in the audit were −140 to 152 mm in X, 0 to 110 mm in Y, and −145 to 145 mm in Z.

| Check | CAD result |
| --- | --- |
| Overall size | 292 × 290 × 110 mm |
| Plan-view margin against 304.8 mm per side of the envelope | 12.8 mm in length and 14.8 mm in width across the full outline |
| Motor shaft against rim reference | 6 reported regions |
| Rim against cast tread reference | 72 reported regions |
| Other modeled interferences | 0 reported |

The two reported interfaces model existing fitted hardware. The interference tool reports regions, so a single rim-to-tread pair can contribute several entries. Reference parts represent fit envelopes. Fastener heads, wiring, terminals, rubber deflection, bend development and structural loads were outside this audit.

Open the assembly with all components resolved and run **Evaluate → Interference Detection** for any new revision. Compare the floor and scoop with the shop’s material and bend coupon before issuing flats. Measure the fully assembled bot for competition inspection.
