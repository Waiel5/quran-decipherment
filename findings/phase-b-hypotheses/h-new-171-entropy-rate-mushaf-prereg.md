---
id: h-new-171
title: Entropy rate of the mushaf surah-sequence — k-NN conditional-entropy test
phase: B (hypothesis)
date: 2026-04-17
status: PRE-REGISTERED
seed: 20260419
rules_tuple: (114 surahs Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-Surah-1, canonical mushaf order, QAC-STEM roots, top-K=100, frequency-based TF, Dirichlet-smoothed L1-normalized, Fisher-Rao arccos-Bhattacharyya distance)
parent_findings: [cross-finding-011]
---

# [[h-new-171-entropy-rate-mushaf|H-NEW-171]] — Entropy rate H(x_n | x_{1..n-1}) of the mushaf surah-sequence

## Motivation

`[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]` established that the canonical mushaf ordering is
Fisher-Rao information-geodesic optimal under morphological-root and
character-4-gram feature spaces (L_mushaf ≈ 11σ below random mean).

This test provides an **independent information-theoretic measurement**
of the same claim: if the mushaf is structured, then the next surah
given the previous surah should be predictable — the sequence should
have **low conditional entropy** H(s_{i+1} | s_i).

We operationalise this via **k-NN rank prediction**: for each
consecutive pair (s_i, s_{i+1}) in the mushaf, compute the rank of
s_{i+1} among the 113 nearest neighbours of s_i (in Fisher-Rao
distance). If mushaf order reflects structural adjacency, the mean
rank will be low. Under the random-permutation null, the mean rank
is ≈ (113+1)/2 = 57.

## Feature space (locked)

- QAC-STEM root tokens per surah from `data/morphology/quranic-corpus-morphology-0.4.txt`.
- Top **K = 100** roots by global frequency across all 114 surahs (NOTE: this is a
  different K than the K=500 used in [[h-new-111-fisher-rao-mushaf|H-NEW-111]]; the task request specifies
  top-100 explicitly, so this is an independent measurement at a sparser
  feature set).
- Dirichlet smoothing α = 0.5 on per-surah root counts.
- L1-normalize to probability vectors.
- Pairwise distance: Fisher-Rao angular = 2·arccos(Σ √(p_i · p_j)).

## Primary test (pre-registered)

Define, for an ordering (x_1, ..., x_{114}):

  rank(x_i → x_{i+1}) := position of x_{i+1} in the sorted list of
                        Fisher-Rao distances from x_i to the other 113
                        surahs, where rank 1 = nearest neighbour.

  mean_rank(ordering) := (1/113) Σ_{i=1..113} rank(x_i → x_{i+1})

**Test 1 (PRIMARY):** mean_rank(mushaf) < mean_rank(null)

- Null: 10,000 uniform random permutations of {1..114}, seed 20260419.
- p-value: (1 + #{perm : mean_rank(perm) ≤ mean_rank(mushaf)}) / (N + 1)
- Direction: one-sided lower-tail.
- Rejection: p < 0.025 (α_bon = 0.025 under Bonferroni-k=2).

## Secondary test (pre-registered)

**Test 2 (SECONDARY):** conditional entropy H(s_{i+1} | s_i) < null.

Estimate P(s_{i+1} | s_i) from the rank distribution via a rank-based
exponential kernel: for each i, define

  p_hat(s_j | s_i) ∝ exp(−r_{i,j})

where r_{i,j} is the rank of s_j among s_i's neighbours (1 = nearest,
113 = farthest). Normalise so Σ_j p_hat(· | s_i) = 1. Then the
empirical conditional entropy over the observed sequence is

  H_hat(x_{i+1} | x_i) := −(1/113) Σ_{i=1..113} log₂ p_hat(x_{i+1} | x_i)

- Null: same 10,000 permutations.
- p-value: one-sided lower-tail.
- Rejection: p < 0.025 (α_bon = 0.025 under Bonferroni-k=2).

## Bonferroni correction

Two pre-registered tests → α_bon = 0.05 / 2 = 0.025.

## Directional prediction

Both tests predict **mushaf < null** (mushaf has lower mean-rank and
lower conditional entropy than random-permutation null).

## Meta-watchdog MW-5 (positive control)

A greedy-NN ordering (starting from surah 1) should give mean_rank
≈ 1 by construction. If it does not, the instrument is broken and
the primary verdict is marked INSTRUMENT-BROKEN regardless of p-value.

## Meta-watchdog MW-1 (length normalization)

Per-surah distributions are L1-normalized to probabilities before
distance computation, so raw surah length does not drive the signal.

## Parameters — locked

- K_TOP = 100
- DIRICHLET_ALPHA = 0.5
- PERMS = 10,000
- SEED = 20260419
- Distance: Fisher-Rao angular
- α_bon = 0.025
- Direction: one-sided lower-tail (mushaf < null)
- Rank kernel for H_hat: exponential in rank, exp(−r)

## What would REFUTE the hypothesis

- mean_rank(mushaf) ≥ mean_rank(null) → refutes M1 structured-sequence claim on root features.
- p_primary ≥ 0.025 → insufficient evidence against null.
- If MW-5 fails → instrument broken.

## Relationship to [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]

If `[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]` (path-length geodesicity) and this test
(rank/entropy) both confirm at α_bon, that's two independent
information-theoretic lines of evidence for the same M1 claim from
the same feature substrate. It's not fully independent replication
(same root features), so the credit is "consistency check" not "new
replication."

## Outputs

- JSON: `findings/phase-b-hypotheses/csv/h-new-171.json`
- Writeup: `findings/phase-b-hypotheses/h-new-171-entropy-rate-mushaf.md`
- Script: `scripts/h_new_171_entropy_rate_mushaf.py`

---

Pre-registered 2026-04-17. SHA-256 of this file will be committed to
script output as tamper evidence.
