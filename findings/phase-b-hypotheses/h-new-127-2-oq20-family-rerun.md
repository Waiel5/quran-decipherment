---
finding_id: h-new-127-2
title: "H-NEW-127.2 rerun: alternate OQ-20 family with geometric MW control"
phase: B
status: POSITIVE (n_pass = 3/5; MW controls pass)
date: 2026-04-18
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-1
pre_reg: findings/phase-b-hypotheses/h-new-127-2-rerun-prereg.md
pre_reg_sha256: d5fef06982648aa8a4cf35c470c67d9f34aae3b61597692b73736e25482f73a1
journal: journal/h-new-127-2-run-1.md
seed: 20260418
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf verse order, Hafs-Kufan, K=300 top global roots, Dirichlet alpha=0.5, Fisher-Rao angular distance; all five surahs use uniform full-verse permutation null)"
verdict: POSITIVE
---

# [[h-new-127-2-oq20-family-rerun|H-NEW-127.2]] - alternate OQ-20 family rerun

## Headline

This is the first OQ-20 scope-extension after [[h-new-127-1-oq20-family-rerun|H-NEW-127.1]], but on the
alternate pre-locked family `{Q1, Q18, Q28, Q78, Q112}` instead of the
original long/refrain-heavy set.

The preregistered family statistic was:

- `n_pass = #{surahs with one-sided p < 0.01}`
- verdict rule: **POSITIVE** iff `n_pass >= 3` and the geometric MW control
  bank passes

Observed result:

- `n_pass = 3 / 5`
- MW control bank: **PASS**
- family verdict: **POSITIVE**

## Exact outputs

### Primary family observable

| Sura | n_v | L_canon | null mean | null sd | z | p (one-sided lower) | Pass |
|---:|---:|---:|---:|---:|---:|---:|:---:|
| 1 | 7 | 1.161789 | 1.218288 | 0.056468 | -1.000550 | 0.204779522048 | FAIL |
| 18 | 110 | 32.416877 | 33.436290 | 0.211122 | -4.828546 | 0.000099990001 | PASS |
| 28 | 88 | 27.251392 | 28.674068 | 0.190346 | -7.474145 | 0.000099990001 | PASS |
| 78 | 40 | 5.738927 | 6.433836 | 0.103936 | -6.685926 | 0.000099990001 | PASS |
| 112 | 4 | 0.468030 | 0.480444 | 0.031545 | -0.393525 | 0.505349465053 | FAIL |

Family count:

- `n_pass = 3 / 5`
- threshold: `n_pass >= 3`
- verdict: **POSITIVE**

### Control bank

- greedy-nearest-neighbor shorter than canonical on all five surahs: `True`
- greedy-nearest-neighbor + 2-opt shorter than canonical on all five surahs:
  `True`

So the geometric MW control bank passes cleanly. There is no Q55-specific
salvage logic here; all five surahs use the same within-surah uniform null.

### Corpus stats

- total STEM root tokens: `49,968`
- distinct roots: `1,642`
- top-K coverage: `0.834634`

## Interpretation

This is a bounded replication on a different locked family, not a broader
corpus search. The result is directionally consistent with the original
Fisher-Rao verse-order signal: three of the five alternate surahs are
significantly shorter in canonical order than their within-surah uniform
permutation nulls, and the geometric control bank does not fail.

The two non-passing surahs are Q1 and Q112. The family still clears the
pre-registered threshold because the decision rule was `n_pass >= 3`.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-127-2-rerun-prereg.md`
- Script: `scripts/h_new_127_2_oq20_family_rerun.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-2.json`
- Journal: `journal/h-new-127-2-run-1.md`

## Verdict

**POSITIVE**: `n_pass = 3 / 5` and the geometric MW control bank passes.
