---
surah: 8
test_id: Q008-F-03
title: Q 8 in the qitāl-fī-sabīl-Allāh cluster {Q 8, 9, 47, 48, 61} — FR cohesion test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q008-F-03-qital-cluster
alpha_bon: 0.025
---

# Q008-F-03 — Pre-registration: qitāl-cluster FR cohesion test

## 1. Hypothesis (locked before observation)

The 5 surahs Q 8 al-Anfāl, Q 9 al-Tawba, Q 47 Muḥammad, Q 48 al-Fatḥ, Q 61 al-Ṣaff are all anchored on the *qitāl-fī-sabīl-Allāh* (fighting-in-the-path-of-God) thematic constellation:
- Q 8: Battle of Badr legal apparatus + post-Badr ethics.
- Q 9: Tabūk expedition + treaty-renunciation.
- Q 47: Muḥammad / Battle of Badr commemoration.
- Q 48: Hudaybiyya conquest.
- Q 61: *innallāha yuḥibbu al-ladhīna yuqātilūna fī sabīlihi ṣaffā* (the *ṣaff*-naming verse).

**Direction (locked):** the 5-surah set forms an FR-cohesive cluster — its mean intra-cluster Fisher-Rao distance is BELOW the random-5-subset null mean (one-tailed; cluster-cohesion).

- **H1 (locked):** mean(d_FR(s, t)) for s, t ∈ {8, 9, 47, 48, 61}, s < t (n = 10 pairs) is below the random-5-subset null mean at α_bon = 0.0125 (Bonferroni-2).
- **H2 (locked):** Q 8's mean-distance-to-other-4 cluster members is below the corpus-mean of Q 8 to all 113 others.

**H0:** the cluster is no more FR-cohesive than a random 5-subset.

## 2. Operational definition

- **FR matrix**: pre-computed from `findings/phase-b-hypotheses/csv/h-new-111.json` (`D_matrix_upper_triangular`).
- **Cluster definition**: {Q 8, Q 9, Q 47, Q 48, Q 61} — pre-locked classical thematic-grouping.
- **Intra-cluster mean**: mean of the C(5, 2) = 10 pairwise FR distances.
- **Q 8 row mean**: mean of (FR(8, 9), FR(8, 47), FR(8, 48), FR(8, 61)) = 4 distances.
- **Corpus-mean for Q 8**: mean of FR(8, s) for s ∈ {1, ..., 114} \ {8} = 113 distances.

## 3. Test statistic

- **D_intra** = mean intra-cluster FR.
- **D_q8_cluster** = Q 8's mean distance to other 4 cluster members.
- **D_q8_corpus** = Q 8's mean distance to all 113 others.
- **diff_q8** = D_q8_cluster - D_q8_corpus.

## 4. Permutation null

- **Null A (cluster-cohesion)**: 10,000 random 5-subsets of {1, ..., 114}; for each, compute the C(5, 2) = 10 pairwise FR mean. Empirical p = (number of random subsets with mean ≤ D_intra) / 10,000.
- **Null B (Q 8 specific)**: 10,000 random 4-subsets of {1, ..., 114} \ {8}; for each, compute Q 8's mean distance to the 4. Empirical p = (number of random 4-subsets with mean ≤ D_q8_cluster) / 10,000.

Seed = 20260509.

## 5. Success / Failure

- **CONFIRMED**: H1 perm-p ≤ 0.0125 AND H2 D_q8_cluster < D_q8_corpus (joint at Bonferroni-2 α_bon = 0.0125).
- **DIRECTIONAL**: one of H1, H2 passes; other does not.
- **NULL**: H1 perm-p > 0.0125 (cluster is no more cohesive than random).

## 6. Honest limits known a priori

- The cluster is THEMATICALLY-FORMAL (qitāl-fī-sabīl-Allāh anchoring), not FR-LATENT. The expectation is that thematic-cohesion may NOT translate to FR-content-cohesion (the lesson from H-NEW-1010 and the Hawamim-NULL: letter-axis ⊥ content-axis often).
- Q 8 is FR-far from Q 9 (rank 9, FR=0.911); Q 8's FR-rank-1 nearest neighbor is Q 3 (FR=0.807, NOT in this thematic cluster). The cluster's FR-cohesion is THEREFORE NOT GUARANTEED a priori.
- This is a pre-registered NULL-DISCOVERY test as much as a confirmation test — if the cluster is NOT FR-cohesive, the finding is informative.

## 7. Rules-tuple

`(no-tashkeel, FR-on-roots, pre-locked-thematic-cluster-set, basmala-counted-only-in-Q1, Hafs-Kufan)`.

## 8. Bonferroni

k = 2 (cluster + Q 8 specific); α_bon = 0.0125.

## 9. Coordination

Q 9 specialist's Q009-F-X tests do not include this 5-cluster cohesion test. Q 47, Q 48, Q 61 specialists do not yet exist. No duplication.

## 10. SHA256 lock

Computed at write-time; embedded into `scripts/Q008_F_03_qital_cluster.py`; verified at runtime.
