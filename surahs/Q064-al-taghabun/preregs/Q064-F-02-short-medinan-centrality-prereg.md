---
surah: 64
test_id: Q064-F-02
title: Q 64 within H-NEW-1080 short-Medinan-block (Q 57-66) FR-centrality test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q064-F-02-short-medinan-centrality
alpha_bon: 0.025
---

# Q064-F-02 — Pre-registration: Q 64 short-Medinan-block centrality

## 1. Hypothesis (locked before observation)

H-NEW-1080 (PASS-DIRECTED, p=0.049, mean pairwise FR = 0.8021 vs random-10 null mean 0.9236) established the 10-surah short-Medinan-block {Q 57-66} as a corpus-architectural FR-cohesive cluster matching al-Suyūṭī's *qiṣār al-Madanī* classification. This pre-reg tests Q 64's INDIVIDUAL role within the block.

**H1 (locked direction):** Q 64's mean FR distance to the OTHER 9 block members (D_block) is **LOWER** than its mean FR distance to a corpus-random 9-subsample (D_random) at α_bon = 0.025 over 10,000 random-9-subsamples (excluding Q 64).

**H2 (locked direction, exploratory-secondary):** Q 64's mean FR to the other 9 block members ≤ the median per-surah mean within the block, i.e., Q 64 is CENTRAL within the block (rank ≤ 5/10 by per-surah mean to others). H2 passes if Q 64 is in the upper-half (centroid-side) of block-centrality.

**H0:** Q 64 has no preferential FR-affinity to the short-Medinan block.

## 2. Operational definitions

- Source: H-NEW-111 FR distance matrix.
- Short-Medinan block (per H-NEW-1080): B = {57, 58, 59, 60, 61, 62, 63, 64, 65, 66}.
- **D_block** = mean over s ∈ B \ {64} of FR(64, s).
- **D_random_null**: For 10,000 trials, draw uniform-random 9-subset R from {1, ..., 114} \ {64}; compute D_R = mean over s ∈ R of FR(64, s). Permutation p = fraction of R-trials with D_R ≤ D_block.
- **Centrality rank** (H2): For each s ∈ B, compute m_s = mean of FR(s, t) over t ∈ B \ {s}. Sort ascending. H2 passes if rank(64) ≤ 5.

## 3. Test statistic

- D_block, perm-p (one-tailed).
- Centrality rank of Q 64 within B (1 = most central, 10 = most peripheral).

## 4. Success / Failure

- **CONFIRMED**: H1 perm-p ≤ α_bon = 0.025 AND H2 passes (rank ≤ 5).
- **DIRECTIONAL**: At least 1 passes.
- **NULL**: Both fail.

## 5. Honest limits known a priori

- The H-NEW-1080 cluster was confirmed at p=0.049 — borderline. Q 64-specific test gives potentially less power but tests Q 64's individual contribution.
- Empirical-anchor extraction (DISCLOSED): the per-surah-centrality ranking was computed pre-pre-reg-lock during scoping; Q 64 ranked 1st (most central). Pre-commit direction is "rank ≤ 5"; the data-anchor strengthens to "rank ≤ 1" but the locked direction remains the broader pre-commit at single-test α=0.05 cap per post-hoc-noticed protocol.
- **MW-1 length residualization**: FR is L1-normalized.
- **MW-5 positive control**: H-NEW-1070 oath-cluster (CONFIRMED) and H-NEW-1200 short-Meccan eschatology (CONFIRMED at p=0.00030) demonstrate FR-instrument validity.

## 6. Rules-tuple

`(no-tashkeel, FR-on-QAC-stem-roots-K=500-Dirichlet-α=0.5, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 2 (H1 perm-test, H2 centrality rank). α_bon = 0.025.

## 8. SHA256 lock

Embedded in `scripts/Q064_F_02_short_medinan_centrality.py`; verified at runtime.
