---
id: H-NEW-184
title: Latent Semantic Analysis — 114 surahs × top-1000 roots
phase: B
status: PRE-REGISTERED
date: 2026-04-17
seed: 20260419
---

# [[h-new-184-lsa-semantic-axes|H-NEW-184]] — LSA / SVD semantic axes

## Background

H-NEW-176 did PCA on a 114 × 500 word-distribution matrix (Hellinger sqrt). Result:
- PC1 = Meccan/Medinan (9.26% var; heavy loadings on Allah, jīm/lām pause marks, Medinan grammar)
- Surah-space is HIGH-DIMENSIONAL (only 19% variance in first 3 PCs)

Hypothesis: TF-IDF weighting on **roots** (not surface words) will:
1. Reveal *content-specific* axes distinct from the stylistic/pause-mark-driven PC1
2. Give different loadings (roots of theological/narrative categories, not function words)
3. Enable cleaner semantic-nearest-neighbour geometry

## Method

1. Parse `data/morphology/quranic-corpus-morphology-0.4.txt` for all ROOT tags.
2. Build 114 × K root-count matrix with top-K = 1000 roots by total occurrence.
3. TF-IDF weighting: `tfidf[s,r] = tf[s,r] * log(114 / df[r])`; row-normalise (L2).
4. Truncated SVD, k=20. Extract singular vectors U ∈ ℝ^{114×20}, singular values σ, V ∈ ℝ^{1000×20}.
5. Interpret top-3 SVs by top-positive / top-negative root loadings in V.
6. Project 114 surahs onto SV1, SV2, SV3; list extreme surahs.
7. Cosine similarity in LSA-k=20 space between all 114×114 pairs.
8. LSA-M1 test: for each surah s, find argmax_j≠s cosine(s, j). Count how often |s - j| = 1 in mushaf order.

## Pre-registered tests (bonferroni_k = 3)

- **T1 (SV1 = Meccan/Medinan)**: project 114 surahs onto SV1, compute AUC against binary (M/Md) label. Pass if AUC > 0.70.
- **T2 (LSA-M1 mushaf-neighbour)**: count of surahs whose LSA-nearest-neighbour is adjacent (|Δ|=1) in mushaf. Permutation null by shuffling surah labels 10 000× (seed 20260419). One-sided; pass if empirical > 99.5th pctile (α=0.05/3 ≈ 0.0167, but we use 99.5th ≈ 0.005 as conservative).
- **T3 (explained variance > null)**: top-3 SV squared singular values share vs null (per-root-column permutation). Pass if z > +3.

Seed: 20260419.

Bonferroni α corrected per test: 0.05/3 = 0.0167.

## Paths

- Script: `scripts/h_new_184_lsa.py`
- Output: `findings/phase-b-hypotheses/h-new-184-lsa-semantic-axes.md`
- Data: `data/morphology/quranic-corpus-morphology-0.4.txt`
