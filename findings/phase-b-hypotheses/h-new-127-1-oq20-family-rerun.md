---
finding_id: h-new-127-1
title: "H-NEW-127.1 rerun: Q55-repaired OQ-20 family with fixed-refrain null"
phase: B
status: POSITIVE (n_pass = 4/5; MW controls pass)
date: 2026-04-18
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-280
pre_reg: findings/phase-b-hypotheses/h-new-127-1-rerun-prereg.md
pre_reg_sha256: 5f11a6995be0faf68a9b27f83d8799f824aa5f1c6172c034c481fe9be5525b6b
journal: journal/h-new-127-1-run-1.md
seed: 20260418
rules_tuple: (no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf verse order, Hafs-Kufan, K=300 top global roots, Dirichlet alpha=0.5, Fisher-Rao angular distance; Q2/Q7/Q12/Q36 use uniform full-verse permutation null; Q55 uses fixed-refrain-slot null from H-NEW-280)
verdict: POSITIVE
---

# [[h-new-127-1-oq20-family-rerun|H-NEW-127.1]] - Q55-repaired OQ-20 family rerun

## Headline

The original [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] five-surah verse-level family is preserved, but Q55 is
repaired with the [[h-new-280-q55-refrain-constrained-fr-null|H-NEW-280]] fixed-refrain-slot null. Under that rerun:

- 4 of 5 surahs pass the one-sided `p < 0.01` threshold
- the geometric MW control bank passes on all 5 surahs
- the family verdict is therefore **POSITIVE**

Q55 remains negative under the corrected null, which is the point of the
repair: it no longer shows the original anti-geodesic reversal, but it still
does not cross the primary family threshold.

## Numbers

### Primary family observable

| Sura | Null model | L_canon | Null mean | Null SD | z | p (one-sided lower) | Pass |
|---:|---|---:|---:|---:|---:|---:|:---:|
| 2 | uniform full-verse permutation | 104.301933 | 108.497535 | 0.406264 | -10.327271 | 0.000099990001 | PASS |
| 7 | uniform full-verse permutation | 65.805001 | 68.270149 | 0.304785 | -8.088166 | 0.000099990001 | PASS |
| 12 | uniform full-verse permutation | 32.794547 | 34.265214 | 0.218188 | -6.740365 | 0.000099990001 | PASS |
| 36 | uniform full-verse permutation | 19.129451 | 19.519040 | 0.135554 | -2.874044 | 0.003999600040 | PASS |
| 55 | fixed refrain slots | 13.639165 | 13.693339 | 0.118168 | -0.458439 | 0.312168783122 | FAIL |

Family count:

- `n_pass = 4 / 5`
- threshold: `n_pass >= 3`
- family verdict: **POSITIVE**

### Control bank

The pre-locked control bank is geometric, not length-based:

- best greedy-nearest-neighbor path shorter than canonical on all five surahs:
  `True`
- best greedy-nearest-neighbor + 2-opt shorter than canonical on all five surahs:
  `True`
- Q55 refrain positions verified against [[h-new-83-rahman-refrain-extension|H-NEW-83]]: `True`

So the control bank passes cleanly. This is the smallest honest repair after
[[h-new-280-q55-refrain-constrained-fr-null|H-NEW-280]]: it keeps the original five surahs, keeps the original null on the
other four surahs, and only replaces the invalid Q55 length-sort baseline with
the fixed-refrain-slot null.

## Secondary values

| Sura | L_greedy_best | L_2opt_best | L_canon / L_2opt |
|---:|---:|---:|---:|
| 2 | 87.676814 | 85.718611 | 1.216794 |
| 7 | 55.818742 | 54.297138 | 1.211942 |
| 12 | 28.503595 | 27.885987 | 1.176022 |
| 36 | 16.370041 | 15.840863 | 1.207602 |
| 55 | 5.672339 | 5.501191 | 2.479311 |

## Interpretation

The rerun does exactly what it was supposed to do:

1. It preserves the four strong [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] passes.
2. It removes the Q55 artifact caused by the broken length-sort MW control.
3. It keeps Q55 from becoming a primary pass under the corrected null.

So the family-level takeaway is not "all five pass." It is:

- the family remains positive at `4/5`
- Q55 is still a genuine negative under the corrected refrain-aware null
- the control bank now behaves as intended

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-127-1-rerun-prereg.md`
- Script: `scripts/h_new_127_1_oq20_family_rerun.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-1.json`
- Journal: `journal/h-new-127-1-run-1.md`

## Verdict

**POSITIVE**: `n_pass = 4 / 5` and the MW control bank passes.
