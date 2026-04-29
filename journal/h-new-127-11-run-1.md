---
finding_id: h-new-127-11
title: "H-NEW-127.11 pooled within-phase rank test for residual Jurjani-tier OQ-20 structure"
phase: B
status: NULL (T_obs = 3.896658; p_perm_upper = 0.610969)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-7
pre_reg: findings/phase-b-hypotheses/h-new-127-11-pooled-within-phase-tier-rank-prereg.md
pre_reg_sha256: c7af1444b369cf13ac25a64914d357e8164b33f7e6d99133658dd5c376a05762
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = jurjani_predicted_asyndeton_tier; conditioning axis = neuwirth_phase; statistic = sum of within-phase Kruskal-Wallis H values over informative phase blocks only; informative block rule = at least two tier classes present and at least one class count > 1; outer null shuffles tier labels only within each informative phase block, preserving observed counts; 114 surahs)"
verdict: NULL
---

# H-NEW-127.11 - run log

## Command

```bash
python3 scripts/h_new_127_11_oq20_pooled_within_phase_tier_rank_test.py
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
| Observed pooled statistic `T` | 3.8966578908851446 |
| Descriptive `df_sum` | 5 |
| Null mean `T` | 4.985948668988414 |
| Null sd `T` | 2.6853964924100544 |
| `n_perm_ge_obs` | 12219 / 20000 |
| Permutation `p` | 0.6109694515274237 |
| Verdict | NULL |

## Phase contribution table

| Phase | `n` | `df` | Observed `H_phase` | Null mean `H_phase` | Null sd `H_phase` | Unadjusted upper-tail `p` |
|---|---:|---:|---:|---:|---:|---:|
| early-Meccan | 48 | 1 | 1.408163265306115 | 0.987260204081623 | 1.1596856399095943 | 0.27393630318484075 |
| middle-Meccan | 16 | 1 | 0.22171945701358453 | 0.9819330316741646 | 1.2456253767278431 | 0.6931153442327883 |
| late-Meccan | 22 | 2 | 2.0485933503836264 | 2.0170878574750226 | 1.5704410573748167 | 0.4261786910654467 |
| Medinan-long | 21 | 1 | 0.2181818181818187 | 0.9996675757575978 | 1.34488164763737 | 0.6752662366881655 |

## Informative blocks

| Phase | `n` | Tier counts |
|---|---:|---|
| early-Meccan | 48 | HIGH 46, MED 2 |
| middle-Meccan | 16 | HIGH 13, MED 3 |
| late-Meccan | 22 | HIGH 4, LOW 1, MED 17 |
| Medinan-long | 21 | LOW 15, MED 6 |

## Excluded blocks

| Phase | Reason | `n` | Tier counts |
|---|---|---:|---|
| liturgical-opening | single-class | 1 | HIGH 1 |
| early-Meccan/Medinan-disputed | single-class | 1 | HIGH 1 |
| late-Meccan/middle-Meccan | single-class | 1 | MED 1 |
| late-Meccan/Medinan-border | single-class | 1 | MED 1 |
| late-Meccan/Medinan-hybrid | single-class | 1 | MED 1 |
| Medinan-short | all-singletons | 2 | LOW 1, MED 1 |

## Notes

- This test is the exact tier-axis analogue of H-NEW-127.10.
- The observed pooled within-phase statistic is below the center of the
  conditional null, so the result is not a near-miss.
- Early-Meccan is the only informative phase whose observed `H_phase` sits
  above its own conditional-null mean; the pooled result remains clearly null.
- With H-NEW-127.10 and H-NEW-127.11 both negative, the honest OQ-20 frontier
  is no longer residual coarse-vs-tier adjudication but whether any
  post-chronology residual structure exists at all.

## Artifacts

- Prereg: `findings/phase-b-hypotheses/h-new-127-11-pooled-within-phase-tier-rank-prereg.md`
- Script: `scripts/h_new_127_11_oq20_pooled_within_phase_tier_rank_test.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-11.json`
- Finding: `findings/phase-b-hypotheses/h-new-127-11-pooled-within-phase-tier-rank.md`
