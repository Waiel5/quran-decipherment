---
surah: 38
test_id: Q038-F-05
title: Singleton anti-cluster — Q 38 FR distance to nearest letter-family cluster centroid vs nearest non-clustered surah
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 1
bonferroni_family: Q038-F-05-singleton-anti-cluster
alpha_bon: 0.05
---

# Q038-F-05 — Pre-registration: singleton anti-cluster placement

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Q 38 (singleton-letter ص) is **more FR-distant from the centroid of the four multi-member muqaṭṭaʿāt clusters (ALM-6, ALR-5, HM-7, TSM-3)** than to its nearest non-muqaṭṭaʿāt non-cluster surah.

In words: Q 38 sits **outside** any of the four canonical letter-family clusters and **near** an unclustered surah, consistent with H-NEW-232's finding that singleton placement is interpretively (not classifiably) coherent.

**H0:** Q 38 is no farther from cluster centroids than from the nearest non-cluster surah; OR Q 38 is closer to a cluster centroid than to any non-cluster surah.

**Direction:** ANTI-CLUSTERED (LOCKED). Q 38's nearest non-cluster surah should be FR-closer than Q 38's nearest cluster centroid.

## 2. Operational definition

**Cluster surahs (per al-Suyūṭī al-Itqān nawʿ 40):**
- ALM-6: Q 2, 3, 29, 30, 31, 32.
- ALR-5: Q 10, 11, 12, 14, 15.
- HM-7: Q 40, 41, 42, 43, 44, 45, 46.
- TSM-3: Q 26, 27, 28.

**Cluster centroid** = mean of FR distance vectors over the cluster's members. Centroid distance to Q 38 = mean( FR(Q 38, m) for m in cluster).

**Non-cluster non-muqaṭṭaʿāt surahs**: the 114 minus the 29 muqaṭṭaʿāt minus Q 38 itself. Find Q 38's nearest FR-neighbor among these.

**Test statistic**: `Δ = min_centroid_dist − min_noncluster_dist`. H1 predicts Δ > 0 (centroid further than nearest non-cluster).

## 3. Test statistic

- Primary: signed Δ. Direction-locked > 0.
- Secondary: rank of each cluster centroid among Q 38's 113 FR distances.
- Tertiary: Q 38's nearest singleton (Q 50, Q 68) for comparison.

## 4. Success / Failure

- **Strict success (CONFIRMED)**: Δ > 0; AND no cluster centroid is in Q 38's top-5 nearest neighbors.
- **Directional**: Δ > 0 but a cluster centroid IS in top-5 nearest neighbors.
- **NULL**: Δ ≤ 0 (Q 38 is closer to a cluster centroid than to nearest non-cluster surah) — pre-commit violation.

## 5. Honest limits known a priori

- The "centroid" is an aggregate; if a single cluster member is FR-very-close to Q 38, that pulls the centroid in but the cluster as a whole may be far. The test uses centroid (mean), pre-committed.
- H-NEW-232 already established that Q 38 ص → TSM cluster phonologically (a-priori match). This test asks whether **content (FR-roots)** also shows TSM-affinity, OR whether content places Q 38 elsewhere. These two axes (phonology vs content) are empirically orthogonal at the muq-cluster level (per H-NEW-610 ALR-5 NULL on whole-surah cohesion).
- Q 38 ص → Q 50 ق affinity (Q038-F-01) operates at the verse-level (opening pair); this test operates at the surah-level (FR row). The two are independent.

## 6. Rules-tuple

`(no-tashkeel, QAC-STEM root tokens, FR-angular distance per H-NEW-111, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Coordination with cross-finding-026 and H-NEW-232

This test re-evaluates Q 38's position in muqaṭṭaʿāt-space using the FR-roots metric (H-NEW-111) rather than the phonological metric (H-NEW-165). Phonological vs content axes are known to be orthogonal at the cluster level (H-NEW-610 NULL). The pre-committed direction (ANTI-CLUSTERED on FR-roots) is consistent with H-NEW-610's finding.

## 8. SHA256 lock

To be computed at run-time. Embedded in `scripts/Q038_F_05_anti_cluster.py`.
