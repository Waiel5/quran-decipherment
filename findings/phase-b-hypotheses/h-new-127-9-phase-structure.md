---
finding_id: h-new-127-9
title: "H-NEW-127.9 direct phase-structure test for locked per-surah compression z-scores"
phase: B
status: POSITIVE (H_obs = 81.878622; p_perm_upper = 0.000050)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-8
pre_reg: findings/phase-b-hypotheses/h-new-127-9-phase-structure-prereg.md
pre_reg_sha256: 424559a1e84d5768dd78beaf08077811b3f98115970e4e17dc32d13fbcd8d3a6
journal: journal/h-new-127-9-run-1.md
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = neuwirth_phase; Kruskal-Wallis H; outer null permutes phase labels across surahs preserving class counts; 114 surahs)"
verdict: POSITIVE
---

# [[h-new-127-9-phase-structure|H-NEW-127.9]] - direct phase-structure test for locked per-surah compression z-scores

## Result

This bounded follow-up asked the direct OQ-20 chronology question using only
locked repository artifacts:

- `z_s = -gzip_z` from `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`
- phase axis = exact `neuwirth_phase` from
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`
- omnibus test = Kruskal-Wallis `H`
- outer null = phase-label shuffle across surahs preserving the exact observed
  phase counts

Observed omnibus statistic:

- `H = 81.87862170247757`
- `df = 9`
- phase-shuffle null mean `H = 8.994918270453827`
- phase-shuffle null sd `H = 3.2414620825464104`
- `n_perm_ge_obs = 0 / 20000`
- upper-tail permutation `p = 0.00004999750012499375`
- verdict: **POSITIVE**

## Interpretation

The direct answer is yes: the locked OQ-20 compression observable is strongly
phase-structured. This is not a weak mediation hint anymore; the phase axis
itself carries a large omnibus separation under an exact class-count-preserving
null.

The main structure sits in the large non-singleton phases. On both mean and
median `z_s`, the major chronology ladder rises sharply:

- `early-Meccan`: strongly negative
- `middle-Meccan`: near zero to mildly positive
- `late-Meccan`: clearly positive
- `Medinan-long`: strongest positive

That pattern makes the earlier phase-aware collapses in [[h-new-127-7-jurjani-tier-phase-aware-control|H-NEW-127.7]] and
[[h-new-127-8-coarse-prefix-phase-aware-control|H-NEW-127.8]] unsurprising: if phase already organizes the raw compression
observable this strongly, later genre-tier projections can inherit that
structure.

The caution is also clear. The locked phase inventory includes several
singleton disputed labels and one tiny `Medinan-short` class (`n = 2`) that
does not sit on the main rising ladder. Those cells should not be overread
individually. But the permutation null preserves the exact sparse class-count
profile, so the omnibus significance already prices in that sparsity.

## Phase Counts And Descriptive `z_s`

| Phase | `n` | Mean `z_s` | Median `z_s` |
|---|---:|---:|---:|
| liturgical-opening | 1 | -0.849270 | -0.849270 |
| early-Meccan | 48 | -2.938245 | -3.351075 |
| early-Meccan/Medinan-disputed | 1 | -1.323874 | -1.323874 |
| middle-Meccan | 16 | 1.015769 | 0.863518 |
| late-Meccan/middle-Meccan | 1 | 1.421778 | 1.421778 |
| late-Meccan | 22 | 4.435758 | 4.611284 |
| late-Meccan/Medinan-border | 1 | 4.295127 | 4.295127 |
| late-Meccan/Medinan-hybrid | 1 | 6.305419 | 6.305419 |
| Medinan-short | 2 | 0.036530 | 0.036530 |
| Medinan-long | 21 | 6.817694 | 5.396568 |

## Scope

- All 114 surahs were included.
- The compression scores were not recomputed.
- The exact locked `neuwirth_phase` labels were used as-is.
- No label pooling, residualization, or continuity-file edits were performed.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-127-9-phase-structure-prereg.md`
- Script: `scripts/h_new_127_9_oq20_phase_structure.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-9.json`
- Journal: `journal/h-new-127-9-run-1.md`

## Verdict

**POSITIVE**: the locked OQ-20 compression observable is directly and strongly
stratified by the exact locked `neuwirth_phase` axis.
