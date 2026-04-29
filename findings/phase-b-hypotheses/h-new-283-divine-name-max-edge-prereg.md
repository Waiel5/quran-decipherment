---
id: H-NEW-283
title: Divine-name surah max-edge under fixed-margin null
phase: B
status: PRE-REGISTERED 2026-04-18
date: 2026-04-18
agent: codex
parent_hypothesis: H-NEW-263
follow_up: H-NEW-276
seed: 20260694
inherited_alpha_bon: 0.025
n_perm: 10000
accepted_swaps_per_perm: 500
rules_tuple: "(repo divine-name detections from findings/phase-b-hypotheses/divine-names-by-verse.csv; same 114-surah x attested-name binary incidence matrix as H-NEW-263/H-NEW-276; weighted projection W=B·Bᵀ with diagonal zeroed; primary statistic M=max_{i<j} shared_names(i,j); fixed-margin bipartite double-edge-swap null; 10000 permutations; 500 accepted swaps/perm)"
---

# [[h-new-283-divine-name-max-edge|H-NEW-283]] — Divine-name surah max-edge under fixed-margin null

## Question

Is the strongest observed pairwise surah overlap in the repo's divine-name
incidence network unusually large under the same fixed-margin null family used
by [[h-new-263-divine-name-surah-network|H-NEW-263]]/H-NEW-276?

## Lock

This follow-up does **not** reopen the observed construction.

1. Same source table: `findings/phase-b-hypotheses/divine-names-by-verse.csv`
2. Same surah x attested-name binary incidence matrix
3. Same weighted projection `W = B·Bᵀ`
4. Same fixed-margin bipartite double-edge-swap null family
5. Same swap depth: `500` accepted swaps per permutation
6. Same seed: `20260694`

The only inferential object is the corpus-level maximum edge weight:

`M = max_{i<j} shared_names(i,j)`

The adjusted p-value is the upper-tail permutation probability:

`p_adj = P_null(M >= M_obs)`

## Descriptive caveat

`Q 2 ↔ Q 3` with overlap `10` is reported descriptively only unless it is the
unique achiever of `M_obs`. The inferential cell is the max-edge statistic, not
the pairwise target.

## Inference

The decision threshold is inherited conservatively from the parent line:

- `alpha = 0.025`

## MW-5 positive control

Retain the cheap parent-line control from [[h-new-263-divine-name-surah-network|H-NEW-263]], but target the new
statistic directly: a synthetic planted-pair matrix should produce an extreme
max edge under the same fixed-margin swap null. If that control fails, the
pipeline is broken and the observed max-edge result is not interpretable.

## Deliverables

- Script: `scripts/h_new_283_divine_name_max_edge.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-283.json`
- Findings: `findings/phase-b-hypotheses/h-new-283-divine-name-max-edge.md`
- Journal: `journal/h-new-283-run-1.md`
