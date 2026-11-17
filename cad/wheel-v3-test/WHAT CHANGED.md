# Shaheer V3 test parts

The rim opened and rebuilt in SolidWorks 2025 with no rebuild errors. Its native
SLDPRT is the donor; the supplied STEP differs by approximately 1.33 mm3. Original
native files are preserved in Originals. An earlier supplied STL is a different
rim revision and was not used for the new rim print.

Only the central mounting interface was changed for the saved Club wheel position:

- Fill/re-cut inside the original 21 mm diameter central hub.
- Hex socket 12.4 mm across flats, with its working 6 mm seat recessed 15 mm from
  the motor-facing rim end, instead of leaving the coupler barrel towards the motor.
- 15 mm diameter entry clears the barrel and the previously checked short grubs.
- Keep 4.5 mm retaining web, plain 4.5 mm screw clearance, and 9.4 mm diameter
  outside screw recess, now 7.5 mm deep.
- Computed geometry outside radius 10.51 mm is unchanged (Boolean difference 0).
  The tyre-grip geometry and 33 mm rim width are preserved.
- Revised centre is supplied as STEP and STL, not as an edited native feature tree.
  The whole robot assembly has not been replaced/rebuilt in this test-only task.

The mould base returned SolidWorks load error 8192 (future-version document).
Rather than repeated opening attempts, both mould shapes were taken from the
author's matching-name STL exports in the supplied WhatsApp ZIP. Their geometries
are unchanged; only placement/orientation was normalized for printing. The native
mould feature trees were not inspected. SolidWorks error reference:
https://help.solidworks.com/2025/English/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFileLoadError_e.html

The base has a 4.2 mm pin and an existing approximately 0.5 mm root fillet.
The wall's nominal bore is 57 mm and its main height 36 mm, with 8 mm tabs above.
Fill only to the 33 mm rim top. The ring has notches but is one connected piece;
it does not pull apart into two halves. Axial demoulding needs release and a trial.

All three exact final STLs measured watertight, consistently wound, one connected
body and plausible millimetre scale. FDM checks used dfam-check's 45 degree
default and its 1.2 mm supported / 1.6 mm unsupported wall guidance:

| Part | Sampled minimum / fifth percentile wall, mm | Finding |
|---|---|---|
| Rim | 1.498 / 1.998 | Local inherited lower recess wall is below the unsupported-wall guide; keep its geometry for the requested first print, support the lower overhangs and inspect for damage. Hub nominal walls are 3.0 mm around the barrel and 3.34 mm at hex corners. |
| Base | 2.207 / 4.000 | Sampled walls exceed the default wall guides; the tall pin remains handling-sensitive. |
| Wall | 2.139 / 3.977 | Sampled walls exceed the default wall guides. |

Upright rim support area is 1.6% of surface area; sideways orientations are about
21%. Both mould parts show zero counted support area upright. Sampling is not an
exhaustive feature/strength assessment. No slicing, print, physical fit, casting,
temperature test or FEA was performed. Preserve the trial-first instruction.

Additional checks: revised rim BRep valid; exact overlap with the saved brass
adapter reference is 0.0 mm3. At Z=8 mm, the assembled mould clip/wall sections
have no crossing segments or sampled boundary midpoints inside the other
part; minimum section gap is 0.225 mm. This is a section check, not a complete
3D interference or physical printer-fit test.
