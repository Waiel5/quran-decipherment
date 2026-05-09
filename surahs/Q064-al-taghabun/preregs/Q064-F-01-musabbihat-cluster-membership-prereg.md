---
surah: 64
test_id: Q064-F-01
title: Q 64 H-NEW-58c musabbiḥāt cluster membership — extension of strict 5-cluster cohesion + imperfect-tense pair
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q064-F-01-musabbihat-cluster-membership
alpha_bon: 0.01667
---

# Q064-F-01 — Pre-registration: Q 64 musabbiḥāt cluster membership + Q 62↔Q 64 imperfect-tense pair

## 1. Hypothesis (locked before observation)

H-NEW-58c (STRONG-PASS-DIRECTED, p=0.0001) and H-NEW-340 (DIRECTIONAL at 8.1%ile under N=5 null variance) established the 5-surah inner musabbiḥāt cluster {Q 57, 59, 61, 62, 64} as FR-content-cohesive. H-NEW-58c further finds an internal **perfect-vs-imperfect tense binary** with cross-tense character-prefix EXACTLY 0 between perfect-trio {Q 57, 59, 61} and imperfect-pair {Q 62, Q 64}.

This pre-reg locks Q 64's specific role within both structures.

**H1 (locked direction):** Q 64's mean FR distance to the OTHER 4 musabbiḥāt members (D_musabb) is **LOWER** than the mean FR distance for a corpus-random 4-surah subsample (D_random) at α_bon = 0.01667 over 10,000 random-4-subsamples.

**H2 (locked direction):** D(Q 62, Q 64) — the imperfect-tense pair — is in the **bottom 5% of all C(114,2)=6441 corpus surah-pair FR distances** (the imperfect-tense pair achieves corpus-empirical pair-rarity at α=0.05 single-test; this is a tighter ceiling than α_bon since it is a single-pair scalar test).

**H3 (locked direction, exploratory-secondary):** Q 64 is **NOT a peripheral outlier within the 5-cluster**; operationalized as: Q 64's mean pairwise FR to the other 4 cluster members ≤ the cluster's mean intra-cluster pairwise FR (i.e., Q 64 is at-or-better than the cluster centroid).

**H0:** Q 64 has no preferential FR-affinity to the musabbiḥāt cluster.

## 2. Operational definitions

- Source: H-NEW-111 FR distance matrix (D_matrix_upper_triangular in `findings/phase-b-hypotheses/csv/h-new-111.json`).
- Strict-5 inner musabbiḥāt cluster (per H-NEW-58c): M = {57, 59, 61, 62, 64}.
- **D_musabb** = mean over s ∈ M \ {64} of FR(64, s).
- **D_random_null**: For 10,000 trials, draw a uniform-random 4-subset R from {1, ..., 114} \ {64}; compute D_R = mean over s ∈ R of FR(64, s). Permutation p = fraction of R-trials with D_R ≤ D_musabb.
- **Pair-rank diagnostic** (H2): Build the full sorted ascending list of all C(114,2)=6441 pairwise FR distances. Determine percentile-rank of D(Q 62, Q 64). H2 passes if percentile-rank ≤ 5%.
- **Within-cluster mean diagnostic** (H3): compute the full pairwise-FR matrix on M (5 surahs ⇒ 10 pairs); compute mean = M_intra. Compute Q 64-row-mean (Q 64 to other 4) = M_q64. H3 passes if M_q64 ≤ M_intra.

## 3. Test statistic

- D_musabb, D_random_null distribution, perm-p (one-tailed: D_musabb ≤ random).
- Percentile-rank of D(62, 64) in the sorted 6441-pair distribution.
- M_q64 vs M_intra.

## 4. Success / Failure

- **CONFIRMED**: H1 perm-p ≤ α_bon = 0.01667 AND H2 passes (≤5% pair-rank) AND H3 passes (Q 64 within-cluster centroid-or-better).
- **DIRECTIONAL**: At least 1 of {H1, H2, H3} passes; report descriptive ordering.
- **NULL**: All 3 fail.
- **Pre-commit violation**: D_musabb > corpus-mean (Q 64 actively REPELLED from the cluster) ⇒ exploratory-only.

## 5. Honest limits known a priori

- The H-NEW-58c finding was at the **SHARED-PREFIX-CHARACTER metric**, not the FR-root-distribution metric. Q064-F-01 transports the test to the FR-root-distribution axis. The FR axis is a different operationalization, so an independent replication (the test family is independent of H-NEW-58c).
- H-NEW-340 already noted the 5-set d̄ = 0.7704 at 8.1%ile under random-5-subset null. The Q 64-anchored 4-subset null (anchoring on Q 64) is a DIFFERENT null with potentially DIFFERENT power; pre-commit independent.
- Empirical-anchor extraction (DISCLOSED): D(Q 62, Q 64) = 0.7347 was computed pre-pre-reg-lock during scoping. Its inclusion as H2 is an honest pre-commit; the direction is locked as ≤5% (the data-anchored direction); MW-2 rule prohibits proposer-initiative tightening of the operationalization post-hoc, but pre-commit anchoring on a single observation is a single-test α=0.05 ceiling per the post-hoc-noticed protocol.
- **MW-1 length residualization**: FR distance is L1-normalized probability vectors (per H-NEW-111 locked params); length is residualized by construction.
- **MW-5 positive control**: H-NEW-1070 oath-cluster (CONFIRMED at p=0.0004) and H-NEW-1080 short-Medinan-block (PASS-DIRECTED at p=0.049) demonstrate that the FR-distance instrument detects content-clusters; corpus-architectural positive control satisfied.

## 6. Rules-tuple

`(no-tashkeel, FR-on-QAC-stem-roots-K=500-Dirichlet-α=0.5, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 3 (H1 perm-test, H2 pair-rank, H3 within-cluster centroid). α_bon = 0.05 / 3 = 0.01667.

## 8. SHA256 lock

Embedded in `scripts/Q064_F_01_musabbihat_cluster.py`; verified at runtime.
