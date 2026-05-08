---
surah: 37
test_id: Q037-F-04
title: Q 37 H-NEW-1070 oath-cluster membership — extension of strict 15-cluster cohesion
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q037-F-04-oath-cluster-membership
alpha_bon: 0.025
---

# Q037-F-04 — Pre-registration: Q 37 oath-cluster membership extension

## 1. Hypothesis (locked before observation)

H-NEW-1070 (CONFIRMED, p=0.0004) established the strict 15-surah *wa-l-* oath-opener cluster as FR-cohesive: {Q 37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}. Q 37 is the EARLY-MID-mushaf member; the rest concentrate in Q 51-103.

**H1 (locked direction):** Q 37's mean FR distance to the OTHER 14 oath-cluster members (D_oath) is **LOWER** than its mean FR distance to a corpus-random 14-surah sample (D_random) at α_bon = 0.025 over 10,000 random-14-subsamples (excluding Q 37 itself).

**H2 (locked direction, exploratory-secondary):** Q 37 is **NOT an outlier within the cluster**; operationalized as: Q 37's median pairwise FR distance to other oath members ≤ the cluster's intra-cluster median pairwise distance. (If Q 37 sits at the periphery, this would be VIOLATED — a directionally-honest pre-commit.)

**H0:** Q 37 has no preferential FR-affinity to the oath cluster.

## 2. Operational definitions

- Source: H-NEW-111 FR distance matrix (D_matrix_upper_triangular in `findings/phase-b-hypotheses/csv/h-new-111.json`).
- Strict-15 oath cluster (per H-NEW-1070): O = {37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}.
- **D_oath** = mean over s ∈ O \ {37} of FR(37, s).
- **D_random_null**: For 10,000 trials, draw a uniform-random 14-subset R from {1, ..., 114} \ {37}; compute D_R = mean over s ∈ R of FR(37, s). Permutation p = fraction of R-trials with D_R ≤ D_oath.
- **Within-cluster median diagnostic** (H2): compute the full pairwise-FR matrix on O (15 surahs ⇒ 105 pairs); compute median = M_intra. Compute Q 37-row-median (Q 37 to other 14 oath members) = M_q37. H2 passes if M_q37 ≤ M_intra.

## 3. Test statistic

- D_oath, D_random_null distribution, perm-p (one-tailed: D_oath ≤ random).
- M_q37, M_intra.

## 4. Success / Failure

- **CONFIRMED**: H1 perm-p ≤ α_bon = 0.025 AND H2 passes.
- **DIRECTIONAL**: H1 OR H2 passes, not both.
- **NULL**: Both fail (Q 37 not preferentially close to the cluster).
- **Pre-commit violation**: D_oath > corpus-mean (Q 37 actively REPELLED from the cluster), or M_q37 > intra-cluster 75th percentile (Q 37 a strong outlier).

## 5. Honest limits known a priori

- The H-NEW-1070 cluster was confirmed at p=0.0004 against random-15-subsets corpus-wide. The Q 37-specific extension here asks a tighter question: Q 37's INDIVIDUAL relationship to the other 14 members. The strict 15-cluster can be cohesive even if Q 37 is its weakest member.
- Empirical-anchor extraction (DISCLOSED): Q 37's mean dist to the other 14 oath members = 0.9949 vs corpus mean 0.9234. The brief states "Q 37 closer to oath-mean than to random-mean" as the prediction; if D_oath ≈ corpus-mean, this would be a NULL — not a pre-commit violation, but a *direction-locked-positive failure*. The empirical-anchor measurement was done BEFORE the pre-reg lock; the direction is not adjusted post-hoc, the test is run honestly.
- Q 37 is FR-very-close to Q 51 (0.843) and Q 52 (0.860) — 2 oath-cluster members appear in Q 37's top-10 nearest. But Q 37 is FR-FAR from Q 53, Q 77, Q 89, Q 100, Q 103 (≥ 1.0). This is a heterogeneous oath-cluster relationship.
- The pre-commit anticipates the direction-locked test may FAIL the strict α_bon = 0.025 threshold. Equal NULL prominence is mandatory; the report will faithfully reflect whichever outcome occurs.

## 6. Rules-tuple

`(no-tashkeel, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 2 (H1 perm-test, H2 within-cluster median). α_bon = 0.025.

## 8. SHA256 lock

Embedded in `scripts/Q037_F_04_oath_cluster.py`; verified at runtime.
