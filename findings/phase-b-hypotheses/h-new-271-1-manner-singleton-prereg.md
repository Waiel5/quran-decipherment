---
id: H-NEW-271-1
title: 1-D mean_manner singleton propagation follow-up to H-NEW-271
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-19
agent: codex
parent_1: H-NEW-271
parent_2: H-NEW-232
open_question: OQ-1 at the singleton layer under 1-D collapse
seed: 20260419
n_perm: 1000
bonferroni_family: h-new-271-1-singleton
bonferroni_k: 2
alpha: 0.05
alpha_bon: 0.025
rules_tuple: "(canonical 29 muq surahs; locked H-NEW-271 codebook; singleton propagation restricted to the single mean_manner axis; z-scored against the 19 multi-member surahs only; Euclidean nearest-centroid in 1-D; nearest multi-member surah reported descriptively for comparability with H-NEW-232; inherited H-NEW-232 accepted-cluster sets verbatim; label-shuffle maxT null over the 19 multi-member surahs; seed 20260419)"
direction_primary: "determine whether the H-NEW-271 1-D mean_manner collapse preserves any nontrivial singleton-layer structure relative to H-NEW-232, with a nontrivial residual bar of 6/10 matches and a comparability bar of 8/10"
---

# [[h-new-271-1-manner-singleton|H-NEW-271.1]] - 1-D mean_manner singleton propagation follow-up

## Question

[[h-new-271-muq-minimal-phon-family|H-NEW-271]] showed that the locked classical-tajwid codebook can be collapsed to
the single `mean_manner` axis without losing the muq cluster ceiling at the
multi-member level.

This follow-up asks a narrower question:

> If we keep only that winning 1-D axis, does any nontrivial singleton-layer
> structure survive when we propagate the 19 multi-member surahs to the 10
> singleton letter-sets by nearest-centroid / nearest-neighbor comparison?

The comparison target is [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]:

- [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] on the full 15-dim codebook achieved 8/10 singleton matches.
- This follow-up asks how much of that singleton-layer structure survives after
  collapsing all the way down to the single `mean_manner` axis.

## Locked feature source

The feature source is the exact [[h-new-271-muq-minimal-phon-family|H-NEW-271]] codebook. This follow-up does not
modify that codebook and does not introduce any new features.

Only the `mean_manner` coordinate is retained for the singleton-layer test.
The singleton comparison uses the same [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] a-priori accepted cluster
sets verbatim:

- `ALMS -> {ALM}`
- `ALMR -> {ALM, ALR}`
- `KHYAS -> {HM, TSM}`
- `TH -> {TSM}`
- `TS -> {TSM}`
- `YS -> {ALM, ALR}`
- `S -> {TSM}`
- `HMASQ -> {HM}`
- `Q -> {HM, TSM}`
- `N -> {ALM, ALR}`

## Inferential design

### Scored quantity

For each singleton:

1. Compute its `mean_manner` score from the locked [[h-new-271-muq-minimal-phon-family|H-NEW-271]] codebook.
2. Z-score that 1-D quantity against the 19 multi-member surahs only.
3. Compute the four multi-member centroids in 1-D.
4. Assign the singleton to its nearest centroid.
5. Also report the nearest multi-member surah descriptively.
6. Count a match when the nearest centroid cluster belongs to the singleton's
   inherited a-priori accepted set.

### Null model

Permutation null:

- shuffle the 19 multi-member labels
- preserve the 6/5/6/2 cluster sizes
- recompute centroids in 1-D
- recompute the singleton match count
- repeat `n_perm = 1000`

Arm-wise maxT is not needed here because there is only one locked feature space.
The permutation tail is the inferential guardrail.

## Decision bars

Two locked bars are used for direct comparison to [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]:

- `Cell A`: at least `6/10` singleton matches and `p_perm < 0.025`
- `Cell B`: at least `8/10` singleton matches and `p_perm < 0.025`

Interpretation:

- `Cell A` passing would mean a nontrivial residual singleton structure survives
  the 1-D collapse.
- `Cell B` passing would mean the 1-D collapse preserves the [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] level.

## Expected outcome

The locked hypothesis is intentionally conservative:

- the 1-D collapse may preserve some residual singleton coherence
- but the full [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] level is not assumed

The analysis is designed to answer the question honestly rather than to force a
parsimony claim beyond the evidence.

## Deliverables

- Script: `scripts/h_new_271_1_manner_singleton.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-271-1.json`
- Findings: `findings/phase-b-hypotheses/h-new-271-1-manner-singleton.md`
- Journal: `journal/h-new-271-1-run-1.md`

