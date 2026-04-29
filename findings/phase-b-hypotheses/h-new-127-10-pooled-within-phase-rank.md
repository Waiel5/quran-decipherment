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
journal: journal/h-new-127-10-run-1.md
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = coarse_prefix(sinai_genre); conditioning axis = neuwirth_phase; statistic = sum of within-phase Kruskal-Wallis H values over informative phase blocks only; informative block rule = at least two coarse-prefix classes present and at least one class count > 1; outer null shuffles coarse-prefix labels only within each informative phase block, preserving observed counts; 114 surahs)"
verdict: NULL
---

# [[h-new-127-10-pooled-within-phase-rank|H-NEW-127.10]] - pooled within-phase rank test for residual coarse-prefix OQ-20 structure

## Result

This bounded residual follow-up asked the sharp post-`127.8` / post-`127.9`
question: once the direct phase ladder is removed from the scoring rule itself,
does any coarse-prefix OQ-20 structure survive inside phase?

Locked inputs and design:

- `z_s = -gzip_z` from
  `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`
- coarse class = literal first hyphen-delimited token of `sinai_genre`
- conditioning axis = exact locked `neuwirth_phase`
- statistic = `T = sum(H_phase)`, where `H_phase` is Kruskal-Wallis `H`
  computed separately inside each informative phase block
- informative phase rule = at least two coarse-prefix classes present and at
  least one class count `> 1`
- outer null = shuffle coarse-prefix labels only within each informative phase
  block, preserving the exact observed counts inside that block

Observed pooled within-phase statistic:

- `T = 12.936834627435609`
- descriptive `df_sum = 21`
- null mean `T = 20.999698317048875`
- null sd `T = 4.905395325490233`
- `n_perm_ge_obs = 19205 / 20000`
- upper-tail permutation `p = 0.96025198740063`
- verdict: **NULL**

## Interpretation

The honest read is hard negative for the residual branch. The OQ-20
coarse-prefix story does not survive once phase is removed from both the null
and the scoring rule. On this stricter design, the observed pooled within-phase
separation is not merely below threshold; it is below the center of its own
conditional null.

That matters. [[h-new-127-8-coarse-prefix-phase-aware-control|H-NEW-127.8]] already said the global coarse-prefix omnibus did not
beat a phase-aware null. [[h-new-127-10-pooled-within-phase-rank|H-NEW-127.10]] goes further and shows that when the test
looks only at within-phase rank separation, the data do not even lean in the
positive residual direction.

So the cleanest current OQ-20 reading is:

- strong direct phase backbone from [[h-new-127-9-phase-structure|H-NEW-127.9]]
- positive unrestricted class structure from [[h-new-127-3-compression-class-mapping|H-NEW-127.3]] / [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]]
- no clean residual coarse-prefix support after conditioning on phase at the
  statistic level

The strongest flattening happens in `early-Meccan`, whose observed
within-phase `H` is far below its own conditional-null mean.

## Informative Phase Contributions

Only four phase blocks met the preregistered informative-block rule. Together
they cover `107 / 114` surahs.

| Phase | `n` | `df` | Observed `H_phase` | Null mean `H_phase` | Null sd `H_phase` | Unadjusted upper-tail `p` |
|---|---:|---:|---:|---:|---:|---:|
| early-Meccan | 48 | 11 | 2.939286 | 10.994652 | 3.506967 | 0.998000 |
| middle-Meccan | 16 | 5 | 5.647059 | 4.978600 | 2.171383 | 0.361932 |
| late-Meccan | 22 | 2 | 1.832675 | 2.008391 | 1.605372 | 0.469927 |
| Medinan-long | 21 | 3 | 2.517816 | 3.018055 | 2.100941 | 0.513674 |

These phase-level p-values are descriptive only. The preregistered inferential
claim is the pooled `T` above.

## Phase Diagnostics

Informative phase blocks:

| Phase | `n` | Coarse-prefix counts |
|---|---:|---|
| early-Meccan | 48 | address 3, admonition 2, apotropaic 2, creedal 1, eschatological 12, exhortative 1, historical 1, hymn 2, hymnic 2, oath 15, polemical 6, prophetic 1 |
| middle-Meccan | 16 | eschatological 2, hymnic 1, narrative 8, oath 1, scripture 2, tripartite 2 |
| late-Meccan | 22 | exhortative 1, narrative 9, scripture 12 |
| Medinan-long | 21 | exhortative 3, historical 2, legal 13, polemical 3 |

Excluded blocks by preregistered rule:

| Phase | Reason | `n` | Coarse-prefix counts |
|---|---|---:|---|
| liturgical-opening | single-class | 1 | liturgical 1 |
| early-Meccan/Medinan-disputed | single-class | 1 | eschatological 1 |
| late-Meccan/middle-Meccan | single-class | 1 | narrative 1 |
| late-Meccan/Medinan-border | single-class | 1 | scripture 1 |
| late-Meccan/Medinan-hybrid | single-class | 1 | hybrid 1 |
| Medinan-short | all-singletons | 2 | hymnic 1, polemical 1 |

## Scope

- All 114 surahs were read from locked repository artifacts.
- The compression scores were not recomputed.
- The coarse-prefix labels were generated exactly as in [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] and
  [[h-new-127-8-coarse-prefix-phase-aware-control|H-NEW-127.8]].
- The exact locked phase labels were used as-is.
- No relabeling, continuity edits, or post hoc phase pooling were performed.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-127-10-pooled-within-phase-rank-prereg.md`
- Script: `scripts/h_new_127_10_oq20_pooled_within_phase_rank_test.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-10.json`
- Journal: `journal/h-new-127-10-run-1.md`

## Verdict

**NULL**: the clean pooled within-phase rank test finds no residual
coarse-prefix OQ-20 structure after conditioning on the locked
`neuwirth_phase` backbone.
