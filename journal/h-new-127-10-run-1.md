---
finding_id: h-new-127-10
title: "H-NEW-127.10 pooled within-phase rank test for residual coarse-prefix OQ-20 structure"
phase: B
status: NULL (T_obs = 12.936835; p_perm_upper = 0.960252)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-8
pre_reg: findings/phase-b-hypotheses/h-new-127-10-pooled-within-phase-rank-prereg.md
pre_reg_sha256: 07e726e1d2cb68031a8e8c4f98fe02cec90184cc91e10577389937e23fd9145f
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = coarse_prefix(sinai_genre); conditioning axis = neuwirth_phase; statistic = sum of within-phase Kruskal-Wallis H values over informative phase blocks only; informative block rule = at least two coarse-prefix classes present and at least one class count > 1; outer null shuffles coarse-prefix labels only within each informative phase block, preserving observed counts; 114 surahs)"
verdict: NULL
---

# H-NEW-127.10 - run log

## Command

```bash
python3 scripts/h_new_127_10_oq20_pooled_within_phase_rank_test.py
```

## Exact outputs

| Quantity | Value |
|---|---:|
| Surahs | 114 |
| Total phase blocks | 10 |
| Informative phase blocks | 4 |
| Surahs in informative blocks | 107 |
| Excluded single-class blocks | 5 |
| Excluded all-singleton blocks | 1 |
| Observed pooled statistic `T` | 12.936834627435609 |
| Descriptive `df_sum` | 21 |
| Null mean `T` | 20.999698317048875 |
| Null sd `T` | 4.905395325490233 |
| `n_perm_ge_obs` | 19205 / 20000 |
| Permutation `p` | 0.96025198740063 |
| Verdict | NULL |

## Phase contribution table

| Phase | `n` | `df` | Observed `H_phase` | Null mean `H_phase` | Null sd `H_phase` | Unadjusted upper-tail `p` |
|---|---:|---:|---:|---:|---:|---:|
| early-Meccan | 48 | 11 | 2.9392857142856883 | 10.994652011054448 | 3.506967006846617 | 0.9980000999950003 |
| middle-Meccan | 16 | 5 | 5.647058823529413 | 4.97859954044118 | 2.171382773391492 | 0.3619319034048298 |
| late-Meccan | 22 | 2 | 1.8326745718049864 | 2.0083913043477573 | 1.605372331657573 | 0.46992650367481625 |
| Medinan-long | 21 | 3 | 2.517815517815521 | 3.018055461205454 | 2.100941065009024 | 0.5136743162841858 |

## Excluded blocks

| Phase | Reason | `n` | Coarse-prefix counts |
|---|---|---:|---|
| liturgical-opening | single-class | 1 | liturgical 1 |
| early-Meccan/Medinan-disputed | single-class | 1 | eschatological 1 |
| late-Meccan/middle-Meccan | single-class | 1 | narrative 1 |
| late-Meccan/Medinan-border | single-class | 1 | scripture 1 |
| late-Meccan/Medinan-hybrid | single-class | 1 | hybrid 1 |
| Medinan-short | all-singletons | 2 | hymnic 1, polemical 1 |

## Notes

- This test removed phase from the scoring rule itself by computing rank
  separation separately inside each informative phase and pooling only those
  phasewise `H` values.
- The result is not merely nonsignificant; the observed pooled statistic falls
  below the center of the conditional null.
- The strongest flattening occurs in `early-Meccan`, where the observed
  phasewise `H` is much smaller than its conditional-null mean.

## Artifacts

- Prereg: `findings/phase-b-hypotheses/h-new-127-10-pooled-within-phase-rank-prereg.md`
- Script: `scripts/h_new_127_10_oq20_pooled_within_phase_rank_test.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-10.json`
- Finding: `findings/phase-b-hypotheses/h-new-127-10-pooled-within-phase-rank.md`
