# [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] — OQ-18 pairwise name-class localization

## Summary

Inside the fixed `Q16..Q25` zone, the [[h-new-126-isolate-core|H-NEW-126]] / [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]]
concept/object label does localize the pairwise root-overlap structure
under the same root-set Jaccard instrument used in [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] /
[[h-new-285-oq18-within-zone-contrast|H-NEW-285]]. The effect is real but not maximal: the observed assignment
is strong enough to pass the exact relabeling null, yet it is only rank
`8 / 252` rather than the unique optimum.

## Result

Primary statistic:

`Delta_pair(L) = mean_jaccard(++) - mean_jaccard(other pairs)`

where `++` are pairs with both surahs in the positive
concept/object-named class and `other` is the union of `+-` and `--`
pairs.

Observed at the locked positive set
`L* = {Q16, Q21, Q22, Q23, Q25}`:

- mean Jaccard across `++` pairs = `0.34138556942690185`
- mean Jaccard across `other` pairs = `0.31251771040264437`
- observed `Delta_pair(L*) = 0.02886785902425748`
- exact upper-tail `p = 8 / 252 = 0.031746031746031744`
- exact descending rank = `8 / 252`

Descriptive split of the non-`++` mass:

- mean Jaccard across `+-` pairs = `0.3154574405982288`
- mean Jaccard across `--` pairs = `0.30516838491368325`

Null summary across all 252 five-positive relabelings:

- null mean = `0.0`
- null median = `0.0003531727521774719`
- null min = `-0.03169181948860378`
- null max = `0.0346190439274357`

Verdict: **PASS-DIRECTED**

## Interpretation

The name-class mechanism does reach the pair level: the concept/object
surahs are, on average, more mutually overlapping than the remaining
within-zone pairs, and that survives the exact `5-of-10` relabeling
null.

But it does **not** fully explain the pair table. The observed label
assignment is only the `8th` best of `252`, so the pair structure is not
identical to the categorical [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] split. In particular, the top
seven relabelings by this statistic all include `Q17`, which means there
is a real boundary leak around `Q17` even though the locked [[h-new-126-isolate-core|H-NEW-126]]
name class still passes honestly.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-286-1-oq18-pairwise-name-class-localization-prereg.md`
- Script: `scripts/h_new_286_1_oq18_pairwise_name_class_localization.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-286-1.json`
- Journal: `journal/h-new-286-1-run-1.md`
