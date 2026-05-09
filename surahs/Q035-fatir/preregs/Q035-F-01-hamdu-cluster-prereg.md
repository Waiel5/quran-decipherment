---
surah: 35
test_id: Q035-F-01
title: Fisher-Rao cohesion of the al-ḥamdu li-llāh opener cluster {Q 1, 6, 18, 34, 35}
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q035-F-01-hamdu-cluster
alpha_bon: 0.025
---

# Q035-F-01 — Pre-registration: al-ḥamdu li-llāh cluster FR-cohesion test

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction):** The 5-surah al-ḥamdu li-llāh opener cluster {Q 1, Q 6, Q 18, Q 34, Q 35} is **FR-cohesive at a level above corpus-mean**: the mean pairwise Fisher-Rao distance among the 5 cluster members is LOWER than the random-5-subset null distribution.

**H2 (one-tailed, locked direction):** Q 35 is the **least-peripheral** member of the cluster: Q 35's mean FR distance to other 4 members is in the bottom-half (≤ median) of the 5-member centrality ranking.

**H0 (joint):** H1 fails AND H2 fails.

**Direction:** Cluster has below-corpus-mean pairwise FR distance (H1) AND Q 35 is non-peripheral (H2).

## 2. Operational definition

- **Source**: `findings/phase-b-hypotheses/csv/h-new-111.json` D-matrix (Fisher-Rao angular, 500 root-token features, Dirichlet α=0.5, mushaf-ordered).
- **Cluster**: {Q 1, Q 6, Q 18, Q 34, Q 35} (the 5 al-ḥamdu li-llāh openers per al-Zarkashī *al-Burhān* 1/181, project-confirmed CC-048).
- **Cluster cohesion metric**: mean pairwise FR distance over C(5,2) = 10 pairs.
- **Cluster centrality (per member)**: mean FR distance to other 4 members.

## 3. Test statistic

- D_cluster = mean over 10 pairs of (FR_ij where i,j ∈ cluster, i ≠ j).
- D_random = mean over 10 pairs of (FR_ij) for a random 5-subset of {1..114}.
- Z_cohesion = (D_cluster - mean(D_random)) / SD(D_random) (one-tailed left).

## 4. Permutation null

**Null model**: draw n_perm = 10000 random 5-subsets (without replacement, excluding the cluster members so the empirical sample is one of the 113-choose-5 random-baseline, with seed 20260509).

For each random 5-subset, compute mean pairwise FR distance. Compare to D_cluster.

**p-value**: fraction of random 5-subsets with mean pairwise FR ≤ D_cluster.

## 5. Success / Failure

- **CONFIRMED**: H1 passes (p ≤ α_bon = 0.025) AND H2 passes (Q 35 in bottom-half of centrality ranking).
- **DIRECTIONAL**: H1 passes alone (p ≤ 0.025) but Q 35 is in top-half of cluster centrality.
- **NULL**: H1 fails (p > 0.025).
- **PRE-COMMIT VIOLATION**: D_cluster > corpus-mean + 1 SD (cluster is AT or ABOVE the null mean — opposite of the locked direction).

## 6. Honest limits known a priori

- **Coordination with Q 34 specialist**: the brief explicitly notes that EITHER the Q 34 OR Q 35 specialist runs this cluster test, the other references it. Per check at session start, **the Q 34 al-Sabaʾ specialist folder is empty (only placeholder dirs)** — no Q 34 cluster test has been run as of 2026-05-09. Therefore Q 35 specialist runs this test as the cluster-test owner; future Q 34 work should reference these results.
- **al-Biqāʿī's munāsabah claim** (Q35-CC-06): predicts shared-opener → smooth transition. The cluster as a whole does NOT necessarily inherit this prediction at the full-content-FR level — opening-shared can be naẓm-level munāsabah without full content cohesion.
- **Cluster size 5 is small**: n=10 pairs gives moderate statistical power; the test is well-powered to detect strong effects (effect size > 0.5 SD) but underpowered for weak signals.
- **Post-hoc concern**: the al-ḥamdu cluster set is fixed by classical claim (al-Zarkashī CC-048), NOT chosen post-hoc by Q 35 specialist. There is no garden-of-forking-paths concern for cluster-membership selection.

## 7. Rules-tuple

`(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, Hafs-Kufan, mashriqi)` — inherited from H-NEW-111.

## 8. Bonferroni

k = 2 (H1 cluster cohesion + H2 Q 35 centrality). α_bon = 0.05 / 2 = 0.025.

## 9. Coordination

- This test is a CLUSTER-LEVEL test that relates to the CC-048 al-Zarkashī claim. It is the project's first FR-cohesion test on the al-ḥamdu cluster.
- Q 34 al-Sabaʾ specialist may reference this result without re-running.
- Cross-finding family: this test feeds into the OQ-3 question (book-introduction-marker network completeness).

## 10. SHA256 lock

This pre-reg's SHA256 will be computed post-write and embedded in `scripts/Q035_F_01_hamdu_cluster.py` for runtime verification.
