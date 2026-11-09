# Rev C verification records

- `assemble-revc.log` records the complete assembly build: 162 instances, successful rebuild, extents -140/0/-145 to 152/110/145 mm, and successful save.
- `sw-revc-audit.txt` records the final interference and export run. Its 60 mm visible-display box was queried with upper covers hidden; use the construction log for the complete 110 mm height. Hidden bodies were included in the interference calculation. The recorded 114 intersections are classified in `interference-classification.json`.
- `revc-saved-state.txt` records all component paths, restored full-assembly views, and the saved flags of 36 parts plus the assembly. All final flags are false.
- The JSON mesh reports refer to the final clamp exports. Their measurements are geometric checks, not load-test results.

Public text copies replace local workspace prefixes with project-relative labels and remove trailing formatting spaces. Geometry files are unchanged from the saved Rev C. The front/rear joint proposals are not included in these audits.
