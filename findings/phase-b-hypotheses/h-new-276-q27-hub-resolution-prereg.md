---
id: H-NEW-276
title: Deep-null resolution of the H-NEW-263 hub question
phase: B
status: PRE-REGISTERED 2026-04-18
date: 2026-04-18
agent: codex
seed: 20260694
parent_hypothesis: H-NEW-263
inherited_alpha_bon: 0.025
n_perm: 10000
accepted_swaps_per_perm: 500
hub_threshold: 2
rules_tuple: "(inherit H-NEW-263 observed construction unchanged: repo divine-name detections from findings/phase-b-hypotheses/divine-names-by-verse.csv; surah x distinct-name binary incidence; attested names only; weighted projection W=B·Bᵀ with diagonal zeroed; hub screen W>=2; S2/Z2/Zmax cell only; fixed-margin bipartite double-edge-swap null; 10000 permutations; 500 accepted swaps/perm)"
---

# [[h-new-276-q27-hub-resolution|H-NEW-276]] — Deep-null resolution of the [[h-new-263-divine-name-surah-network|H-NEW-263]] hub question

## Question

Does the `[[h-new-263-divine-name-surah-network|H-NEW-263]]` conclusion "structure yes, hub no" survive a much deeper
fixed-margin null for the already-locked hub cell, and does Q 27 remain the
lead candidate under that unchanged test?

## Lock

This follow-up does **not** reopen the observed construction:

1. Same source table: `findings/phase-b-hypotheses/divine-names-by-verse.csv`
2. Same binary surah x attested-name incidence matrix
3. Same weighted projection `W = B·Bᵀ`
4. Same conservative hub screen `W >= 2`
5. Same hub statistic family:
   - `S2[i] = Σ_j W[i,j] * 1[W[i,j] >= 2]`
   - `Z2[i] = (S2[i] - mean_null_i) / sd_null_i`
   - `Zmax = max_i Z2[i]`
6. Same null family:
   - fixed row sums
   - fixed column sums
   - accepted 2x2 double-edge swaps
   - `500` accepted swaps per permutation

Only one thing changes: `n_perm` increases from `300` to `10000`.

## Inference

The effective decision threshold is inherited unchanged from `[[h-new-263-divine-name-surah-network|H-NEW-263]]`:

- `alpha = 0.025`

That choice is deliberate. This is a follow-up on the old Cell B, not a chance
to relax the family-wise threshold.

## Reporting

- Primary result: `p_exist = P(max Z2_null >= Zmax_obs)` under the deeper null
- Candidate focus: Q 27's rank, `Z2`, raw upper-tail `p_raw`, and family-wise
  adjusted `p_adj` from the same max-null distribution
- No new inferential cells

## Deliverables

- Script: `scripts/h_new_276_q27_hub_resolution.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-276.json`
- Findings: `findings/phase-b-hypotheses/h-new-276-q27-hub-resolution.md`
- Journal: `journal/h-new-276-run-1.md`
