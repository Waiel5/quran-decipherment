---
finding_id: h-new-127-2
title: "H-NEW-127.2 rerun: alternate OQ-20 family with geometric MW control"
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-1
date_prereg: 2026-04-18
seed: 20260418
bonferroni_k: 5
bonferroni_family: h-new-127-2-oq20-family-rerun
alpha_bon: 0.01
alpha_raw: 0.05
direction_primary: "n_pass = count of locked surahs with one-sided p < 0.01; positive iff n_pass >= 3 and MW controls pass; negative iff n_pass <= 2 or MW controls fail"
length_control: "MW-1 via L1-normalization of per-verse distributions"
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf verse order, Hafs-Kufan, K=300 top global roots, Dirichlet alpha=0.5, Fisher-Rao angular distance; all five surahs use uniform full-verse permutation null)"
perms: 10000
surahs_locked:
  - 1
  - 18
  - 28
  - 78
  - 112
verdict_ceiling: "POSITIVE if n_pass >= 3 and MW controls pass; NEGATIVE otherwise"
---

# [[h-new-127-2-oq20-family-rerun|H-NEW-127.2]] — alternate OQ-20 family rerun

## Motivation

[[h-new-127-1-oq20-family-rerun|H-NEW-127.1]] repaired the original [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] family by keeping the same
five-surah framework and replacing the broken Q55 control with a refrain-safe
null. This follow-up is the first scope-extension to the alternate locked
five-surah family named in the parent journal: Q1, Q18, Q28, Q78, Q112.

The intent is narrow:

- keep the same primary statistic family as [[h-new-127-1-oq20-family-rerun|H-NEW-127.1]]
- keep the same geometric MW control bank
- avoid any Q55-specific salvage logic
- assess whether the verse-order Fisher-Rao signature replicates on a
  different locked family

## Hypothesis

Primary family observable:

- `n_pass = #{surahs with one-sided p < 0.01}`

Decision rule:

- **POSITIVE** iff `n_pass >= 3` and the pre-locked MW control bank passes.
- **NEGATIVE** iff `n_pass <= 2` or any control fails.

## Locked method

- Corpus, feature space, and metric are inherited unchanged from [[h-new-127-1-oq20-family-rerun|H-NEW-127.1]]:
  QAC STEM roots, top `K = 300` global roots, Dirichlet `alpha = 0.5`,
  L1-normalized verse distributions, Fisher-Rao angular distance.
- Surahs are locked to the alternate five-surah family:
  Q1, Q18, Q28, Q78, Q112.
- Nulls are locked uniformly within each surah:
  - each surah uses uniform random permutation of all verses within that surah.
- `PERMS = 10,000`, seed `20260418`.

## MW control bank

The pre-locked control bank is the same geometric comparator used in
[[h-new-127-1-oq20-family-rerun|H-NEW-127.1]], now applied to the alternate family:

- for each of the five surahs, the best greedy-nearest-neighbor path followed
  by 2-opt refinement must be shorter than the canonical verse order
- operationally: `L_2opt_best < L_canon` for all five surahs
- if any surah fails this gate, the run is instrument-broken and the family
  verdict is NEGATIVE regardless of `n_pass`

## Acceptance window

- **POSITIVE**: `n_pass >= 3` and all MW controls pass.
- **NEGATIVE**: `n_pass <= 2` or any MW control fails.

## Scope boundary

This rerun does not reopen the five-surah family, add new surahs, change `K`,
change `alpha`, change the Fisher-Rao metric, or introduce any special-case
nulls. It is a bounded replication on a different locked family only.

## Deliverables

- Script: `scripts/h_new_127_2_oq20_family_rerun.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-2.json`
- Findings: `findings/phase-b-hypotheses/h-new-127-2-oq20-family-rerun.md`
- Journal: `journal/h-new-127-2-run-1.md`
