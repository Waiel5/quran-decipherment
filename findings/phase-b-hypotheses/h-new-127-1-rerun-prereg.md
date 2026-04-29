---
finding_id: h-new-127-1
title: "H-NEW-127.1 rerun: Q55-repaired OQ-20 family with fixed-refrain null"
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-280
date_prereg: 2026-04-18
seed: 20260418
bonferroni_k: 5
bonferroni_family: h-new-127-1-oq20-family-rerun
alpha_bon: 0.01
alpha_raw: 0.05
direction_primary: "n_pass = count of locked surahs with one-sided p < 0.01; positive iff n_pass >= 3 and MW controls pass; negative iff n_pass <= 2 or MW controls fail"
length_control: "MW-1 via L1-normalization of per-verse distributions"
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf verse order, Hafs-Kufan, K=300 top global roots, Dirichlet alpha=0.5, Fisher-Rao angular distance; Q2/Q7/Q12/Q36 use uniform full-verse permutation null; Q55 uses fixed-refrain-slot null from H-NEW-280)"
perms: 10000
surahs_locked:
  - 2
  - 7
  - 12
  - 36
  - 55
verdict_ceiling: "POSITIVE if n_pass >= 3 and MW controls pass; NEGATIVE otherwise"
---

# [[h-new-127-1-oq20-family-rerun|H-NEW-127.1]] — Q55-repaired OQ-20 family rerun

## Motivation

[[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] showed a 4/5 verse-level Fisher-Rao replication of the parent
surah-scale effect, but Q55 failed its pre-locked length-sort MW control
because the refrain verses are nearly identical in length and cluster under
that baseline. [[h-new-280-q55-refrain-constrained-fr-null|H-NEW-280]] then tested the smallest honest salvage for Q55:
keep the 31 refrain slots fixed and permute only the 47 non-refrain verses.

This rerun keeps the original five surahs from [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] and makes only the
minimal correction needed after [[h-new-280-q55-refrain-constrained-fr-null|H-NEW-280]]:

- Q2, Q7, Q12, Q36 keep the original uniform full-verse permutation null.
- Q55 uses the fixed-refrain-slot null from [[h-new-280-q55-refrain-constrained-fr-null|H-NEW-280]].
- The MW control bank is geometric rather than length-sort based, so it is
  robust to refrain structure.

## Hypothesis

Primary family observable:

- `n_pass = #{surahs with one-sided p < 0.01}`

Decision rule:

- **POSITIVE** iff `n_pass >= 3` and the pre-locked MW control bank passes.
- **NEGATIVE** iff `n_pass <= 2` or any control fails.

## Locked method

- Corpus, feature space, and metric are inherited unchanged from [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]]:
  QAC STEM roots, top `K = 300` global roots, Dirichlet `alpha = 0.5`,
  L1-normalized verse distributions, Fisher-Rao angular distance.
- Surahs are locked to the original five from [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]]:
  Q2, Q7, Q12, Q36, Q55.
- Nulls are locked per surah:
  - Q2/Q7/Q12/Q36: uniform random permutation of all verses within the surah.
  - Q55: fixed refrain slots at the [[h-new-280-q55-refrain-constrained-fr-null|H-NEW-280]] positions; permute only the
    47 non-refrain verses.
- `PERMS = 10,000`, seed `20260418`.

## MW control bank

The pre-locked control bank is the same geometric comparator already computed
in [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]], now promoted to the actual control gate:

- For each of the five surahs, the best greedy-nearest-neighbor path followed
  by 2-opt refinement must be shorter than the canonical verse order.
- Operationally: `L_2opt_best < L_canon` for all five surahs.
- If any surah fails this gate, the run is instrument-broken and the family
  verdict is NEGATIVE regardless of `n_pass`.

This replaces the invalid Q55 length-sort control from [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]]. The control
is robust to refrain structure because it is path-geometric, not length-based.

## Acceptance window

- **POSITIVE**: `n_pass >= 3` and all MW controls pass.
- **NEGATIVE**: `n_pass <= 2` or any MW control fails.

## Scope boundary

This rerun does not reopen the five-surah family, add new surahs, change `K`,
change `alpha`, or change the Fisher-Rao metric. The only Q55 adjustment is
the fixed-refrain-slot null inherited from [[h-new-280-q55-refrain-constrained-fr-null|H-NEW-280]].

## Deliverables

- Script: `scripts/h_new_127_1_oq20_family_rerun.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-1.json`
- Findings: `findings/phase-b-hypotheses/h-new-127-1-oq20-family-rerun.md`
- Journal: `journal/h-new-127-1-run-1.md`
