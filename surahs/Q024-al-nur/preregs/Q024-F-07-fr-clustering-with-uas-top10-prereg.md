---
finding_id: Q024-F-07
title: "Q 24 mean Fisher-Rao distance to UAS top-10 vs corpus mean"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: 10000
bonferroni_k: 4
alpha_raw: 0.05
alpha_bonferroni: 0.0125
direction: Q 24 mean FR-distance to UAS-top-10-others < Q 24 mean FR-distance to whole corpus
---

# Q024-F-07 — Q 24 clusters with the UAS top-10 on Fisher-Rao distance

## Hypothesis (LOCKED before observation)

The Unified Architectural Score (UAS, H-NEW-840) identifies the corpus's top-10 most-architecturally-prominent surahs: **{33, 1, 2, 9, 24, 12, 55, 10, 23, 17}**. These surahs share elevated outlier-strength + canonical-adjacency-cost + iʿjāz-signature. If the UAS captures a real architectural property, Q 24 should cluster with the other nine top-10 surahs on an independent metric — Fisher-Rao distance over QAC root-frequency vectors (H-NEW-111).

Pre-registered direction: **Q 24's mean Fisher-Rao distance to the other 9 top-10 UAS surahs is LOWER than Q 24's mean Fisher-Rao distance to the entire corpus (113 other surahs).**

This is a test of cross-metric convergence: UAS is a structural-anomaly composite; FR is a content-distribution distance. If both are tracking the same underlying property, distances should align.

## Method (LOCKED)

1. Load the FR distance matrix from `findings/phase-b-hypotheses/csv/h-new-111.json` (key `D_matrix_upper_triangular`, reconstructed to 114×114).
2. Define UAS-top-10 = {33, 1, 2, 9, 24, 12, 55, 10, 23, 17} (verified against `h-new-840.json` key `top_15`, top 10 entries).
3. Compute:
   - `d_top9 = mean({FR(24, s) : s ∈ top-10, s ≠ 24})` — mean to 9 fellow top-10 members.
   - `d_corpus = mean({FR(24, s) : s ∈ 1..114, s ≠ 24})` — mean to all 113 others.
   - `Δ = d_top9 − d_corpus`. Pre-registered direction: **Δ < 0**.
4. Permutation null: draw 10,000 random 9-element subsets of `{1..114} \ {24}` and compute the analogous mean. The two-sided p-value is the fraction of permutations whose absolute Δ exceeds the observed.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-STEM-roots-top-500, Dirichlet-α=0.5, L1-normalized probability vectors, Fisher-Rao angular = 2·arccos(Σ √(p_i · p_j)), Hafs-Kufan, mushaf-order)`

This is the rules-tuple of H-NEW-111 verbatim; the test inherits its parameter-lock.

## Direction (LOCKED)

Δ < 0 (top-9 < corpus). Reversed direction (Δ > 0) = pre-commit violation, NULL with prominence.

## Success criteria

- Δ < 0 AND permutation p_raw < α_Bonferroni (0.0125): **CONFIRMED**.
- Δ < 0 AND permutation p_raw < 0.05 but > 0.0125: **DIRECTIONAL**.
- Δ < 0 AND p_raw > 0.05: **WEAK-DIRECTIONAL**, reported as descriptive.
- Δ > 0: **NULL with pre-commit-violation flag**.

## Honest limits (pre-registered)

- The UAS itself is built on outlier-strength + canonical-cost + iʿjāz signature, NOT on FR distance. FR is genuinely independent of the UAS construction. But: outlier-strength uses FR-related distances in its definition (the H-NEW-590 construction). Strict independence requires confirming that the UAS-FR overlap is at the *macro-architectural* level, not at the *direct-formula* level.
- The "top-10" cutoff is conventional (could be top-5, top-15). The test is run at top-10 as the published UAS landmark.
- The permutation is over random 9-subsets of the corpus. This tests whether Q 24's affinity to the UAS-top-10 is greater than expected under random sampling; it does NOT test whether Q 24 is *the most* central member of the top-10 cluster.
- Q 24's mean FR distance to the corpus (1.0704) places it at rank 105 / 114 — Q 24 is *more distant* from the corpus average than 92% of surahs. This is consistent with Q 24's outlier status. The pre-registered test compares two means *for Q 24*, not Q 24's absolute distance to the corpus.

## Seed

20260509

## Pre-registration SHA256

Computed at write-time; embedded in `Q024_F_07_fr_clustering_uas_top10.py` and verified at runtime.
