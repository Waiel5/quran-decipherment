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
journal: journal/h-new-127-11-run-1.md
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = jurjani_predicted_asyndeton_tier; conditioning axis = neuwirth_phase; statistic = sum of within-phase Kruskal-Wallis H values over informative phase blocks only; informative block rule = at least two tier classes present and at least one class count > 1; outer null shuffles tier labels only within each informative phase block, preserving observed counts; 114 surahs)"
verdict: NULL
---

# [[h-new-127-11-pooled-within-phase-tier-rank|H-NEW-127.11]] - pooled within-phase rank test for residual Jurjani-tier OQ-20 structure

## Result

This is the tier-axis analogue of [[h-new-127-10-pooled-within-phase-rank|H-NEW-127.10]]. The question was no longer
whether the classical-tier bridge is positive on the full corpus. [[h-new-127-6-jurjani-tier-bridge|H-NEW-127.6]]
already showed that. The question was whether any of that signal survives once
chronology is removed from both the null and the scoring rule itself.

Locked inputs and design:

- `z_s = -gzip_z` from
  `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`
- tier class = exact locked `jurjani_predicted_asyndeton_tier`
- conditioning axis = exact locked `neuwirth_phase`
- statistic = `T = sum(H_phase)`, where `H_phase` is Kruskal-Wallis `H`
  computed separately inside each informative phase block
- informative phase rule = at least two tier classes present and at least one
  class count `> 1`
- outer null = shuffle tier labels only within each informative phase block,
  preserving the exact observed counts inside that block

Observed pooled within-phase statistic:

- `T = 3.8966578908851446`
- descriptive `df_sum = 5`
- null mean `T = 4.985948668988414`
- null sd `T = 2.6853964924100544`
- `n_perm_ge_obs = 12219 / 20000`
- upper-tail permutation `p = 0.6109694515274237`
- verdict: **NULL**

## Interpretation

The residual Jurjani-tier branch does not survive this stricter test either.
Once the chronology backbone is respected blockwise and the scoring rule itself
is restricted to within-phase rank structure, the observed pooled tier
separation sits slightly below the center of its own conditional null.

That sharpens OQ-20 materially:

- [[h-new-127-6-jurjani-tier-bridge|H-NEW-127.6]] showed a strong full-corpus tier alignment
- [[h-new-127-7-jurjani-tier-phase-aware-control|H-NEW-127.7]] showed that this alignment does not survive a first phase-aware
  global null
- [[h-new-127-11-pooled-within-phase-tier-rank|H-NEW-127.11]] now shows that the pooled within-phase residual tier signal is
  also dead

Combined with [[h-new-127-10-pooled-within-phase-rank|H-NEW-127.10]], the honest OQ-20 reading is now harsher than
"phase-mediated." Both the coarse-prefix and Jurjani-tier residual branches
collapse when chronology is taken as the backbone. The live question is no
longer which one survives best inside phase. It is whether **any**
interpretable post-chronology residual structure remains at all.

## Informative Phase Contributions

Only four phase blocks met the preregistered informative-block rule. Together
they cover `107 / 114` surahs.

| Phase | `n` | `df` | Observed `H_phase` | Null mean `H_phase` | Null sd `H_phase` | Unadjusted upper-tail `p` |
|---|---:|---:|---:|---:|---:|---:|
| early-Meccan | 48 | 1 | 1.408163 | 0.987260 | 1.159686 | 0.273936 |
| middle-Meccan | 16 | 1 | 0.221719 | 0.981933 | 1.245625 | 0.693115 |
| late-Meccan | 22 | 2 | 2.048593 | 2.017088 | 1.570441 | 0.426179 |
| Medinan-long | 21 | 1 | 0.218182 | 0.999668 | 1.344882 | 0.675266 |

These phase-level p-values are descriptive only. The preregistered inferential
claim is the pooled `T` above.

## Phase Diagnostics

Informative phase blocks:

| Phase | `n` | Tier counts |
|---|---:|---|
| early-Meccan | 48 | HIGH 46, MED 2 |
| middle-Meccan | 16 | HIGH 13, MED 3 |
| late-Meccan | 22 | HIGH 4, LOW 1, MED 17 |
| Medinan-long | 21 | LOW 15, MED 6 |

Excluded blocks by preregistered rule:

| Phase | Reason | `n` | Tier counts |
|---|---|---:|---|
| liturgical-opening | single-class | 1 | HIGH 1 |
| early-Meccan/Medinan-disputed | single-class | 1 | HIGH 1 |
| late-Meccan/middle-Meccan | single-class | 1 | MED 1 |
| late-Meccan/Medinan-border | single-class | 1 | MED 1 |
| late-Meccan/Medinan-hybrid | single-class | 1 | MED 1 |
| Medinan-short | all-singletons | 2 | LOW 1, MED 1 |

## Scope

- All 114 surahs were read from locked repository artifacts.
- The compression scores were not recomputed.
- The exact locked Jurjani-tier labels were used as-is.
- The exact locked phase labels were used as-is.
- No relabeling, continuity edits, or post hoc phase pooling were performed.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-127-11-pooled-within-phase-tier-rank-prereg.md`
- Script: `scripts/h_new_127_11_oq20_pooled_within_phase_tier_rank_test.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-11.json`
- Journal: `journal/h-new-127-11-run-1.md`

## Verdict

**NULL**: the clean pooled within-phase rank test finds no residual
Jurjani-tier OQ-20 structure after conditioning on the locked
`neuwirth_phase` backbone.
