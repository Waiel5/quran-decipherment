# [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] — OQ-18 within-zone name-class contrast

## Summary

Inside the fixed `Q16..Q25` zone, the target subset
`{16,21,22,23,25}` is exactly the locked concept/object-named set
carried over from [[h-new-126-isolate-core|H-NEW-126]] Cell B. Under the exact `C(10,5)=252`
within-zone null, it is the unique maximum of the preregistered
binary contrast.

## Result

Primary statistic:

`Delta_name(S) = mean_{q in S} I[label(q)=concept/object] - mean_{q in Z\\S} I[label(q)=concept/object]`

Observed at `S* = {16,21,22,23,25}`:

- target mean concept/object rate = `1.0`
- complement mean concept/object rate = `0.0`
- observed `Delta_name(S*) = 1.0`
- exact upper-tail `p = 1/252 = 0.003968253968253968`
- exact descending rank = `1 / 252`

Null summary across all 252 five-surah subsets:

- null mean = `0.0`
- null median = `0.0`
- null min = `-1.0`
- null max = `1.0`

Verdict: **PASS-DIRECTED**

## Interpretation

This result is structurally strong but also categorical: the target
subset is the entire concept/object-named class inside the zone, so the
exact-null maximum is a label-isolation result rather than a subtle
graded contrast. That remains a valid bounded finding under the locked
design, but it should be read as a mechanistic confirmation of the
[[h-new-126-isolate-core|H-NEW-126]] label structure, not as evidence of additional hidden
gradients.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-286-oq18-within-zone-name-class-contrast-prereg.md`
- Script: `scripts/h_new_286_oq18_within_zone_name_class_contrast.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-286.json`
- Journal: `journal/h-new-286-run-1.md`
