# H-NEW-286.1 run journal

Date: 2026-04-19
Operator: codex

## Scope

Run the preregistered exact pairwise localization test for the
H-NEW-286 concept/object-vs-other label inside the fixed `Q16..Q25`
zone, using the same surah-level root-set Jaccard representation as
H-NEW-281 / H-NEW-285.

## Locked design

- zone fixed to `Q16..Q25`
- positive label fixed to `{16,21,22,23,25}`
- negative label fixed to `{17,18,19,20,24}`
- representation fixed to surah-level QAC root sets
- pair score fixed to set Jaccard
- primary statistic fixed to
  `Delta_pair(L) = mean_jaccard(++) - mean_jaccard(other pairs)`
- exact space fixed to all `C(10,5) = 252` five-positive assignments
- direction fixed to one-sided upper-tail

## Exact outputs

- observed positive set = `{16, 21, 22, 23, 25}`
- number of `++` pairs = `10`
- number of `+-` pairs = `25`
- number of `--` pairs = `10`
- mean Jaccard across `++` pairs = `0.34138556942690185`
- mean Jaccard across `+-` pairs = `0.3154574405982288`
- mean Jaccard across `--` pairs = `0.30516838491368325`
- mean Jaccard across `other` pairs = `0.31251771040264437`
- observed `Delta_pair(L*) = 0.02886785902425748`
- exact rank = `8 / 252`
- exact upper-tail `p = 0.031746031746031744`
- verdict = `PASS-DIRECTED`

Null summary:

- null mean = `0.0`
- null median = `0.0003531727521774719`
- null min = `-0.03169181948860378`
- null max = `0.0346190439274357`

## Continuity note

The pair-level mechanism is real but not perfectly aligned with the
categorical H-NEW-286 split. The observed label map passes exactly, but
seven relabelings score higher on the pairwise statistic, and all seven
include `Q17`. That marks `Q17` as the main leakage point in the
pair-overlap structure.

## Files written

- `findings/phase-b-hypotheses/h-new-286-1-oq18-pairwise-name-class-localization-prereg.md`
- `scripts/h_new_286_1_oq18_pairwise_name_class_localization.py`
- `findings/phase-b-hypotheses/csv/h-new-286-1.json`
- `findings/phase-b-hypotheses/h-new-286-1-oq18-pairwise-name-class-localization.md`
- `journal/h-new-286-1-run-1.md`
