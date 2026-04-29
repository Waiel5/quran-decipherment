---
preregistration_id: muawwidhat-cluster-F-01
title: Muʿawwidhāt-3 cluster cohesion — Q 112+113+114 vs corpus-wide-3-surah controls
date: 2026-04-28
phase: B+
seed: 20260428
status: PRE-REGISTERED-LOCKED
---

# muʿawwidhāt cluster F-01 — Pre-registration: cluster cohesion

## Hypothesis (H1)

The 3-surah cluster {Q 112, Q 113, Q 114} has higher mean-pairwise FR-distance cohesion (lower mean-distance) than ≥99% of randomly-sampled 3-surah subsets from the corpus.

This tests whether the muʿawwidhāt-3 (folk-extended) cluster forms a real FR-geometric cluster, beyond what would be expected by chance.

## Method

1. Compute mean pairwise FR-distance for {Q 112, Q 113, Q 114}: this is `(D[112][113] + D[112][114] + D[113][114]) / 3`.
2. Generate 10000 random 3-surah subsets (with seed-locked sampling).
3. Compute mean pairwise FR-distance for each; build null distribution.
4. Compute permutation p-value: fraction of nulls with mean ≤ observed.

## Direction

LOCKED: H1 PASSES if permutation p ≤ 0.01 (i.e., {Q 112, Q 113, Q 114} mean pairwise distance is below 1st percentile of random-3-subsets).

## Bonferroni

This is a single corpus-level test (not in a Q-NN family); α = 0.05 single-test, or 0.01 strict pre-reg.

## Pre-commit honesty

If permutation p > 0.01, the cluster cohesion claim is published as NULL or DIRECTIONAL (depending on p-value).
