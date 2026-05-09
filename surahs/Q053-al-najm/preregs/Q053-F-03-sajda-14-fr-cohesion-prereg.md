---
surah: 53
test_id: Q053-F-03
title: "Sajda-14 cluster FR-content cohesion test (functional-classification cohesion-NULL hypothesis)"
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q053-F-family-2026-05-09
alpha_bon: 0.0167
---

# Q053-F-03 — Pre-registration: 14 sajda-surahs FR-content cohesion

## 1. Hypothesis (locked before observation)

**H1 (REVERSE-DIRECTION test, one-tailed)**: The 14 sajda-surahs (Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96) form a **content-cohesive cluster** in the project's Fisher-Rao surah-distance matrix.

**Direction (reverse-prediction)**: We expect this hypothesis to FAIL. The classical *sujūd al-tilāwah* classification is a **functional-liturgical** classification (where to prostrate during recitation), NOT a content-fingerprint classification. Predicting FAILURE here adds the sajda-classification to the project's catalog of *functional-classifications without content-cohesion* (alongside H-NEW-68 Friday-recitation-cluster NULL, H-NEW-69 14-vs-14 alphabet-split NULL).

**H0 (positive cohesion claim)**: Sajda-14 within-cluster pairwise mean FR distance < corpus-wide pairwise mean FR (i.e., the 14 are FR-cohesive).

**H1 (the predicted null direction)**: Sajda-14 within-cluster pairwise mean FR ≥ corpus-wide pairwise mean OR is statistically indistinguishable from random 14-subsets.

**REVERSE-DIRECTION LOCKING**: This is a NULL-prediction test. The expected and predicted outcome is non-cohesion. Per HANDOFF/04-DISCIPLINE.md, reverse-direction tests must be explicitly disclosed.

## 2. Operational definition

**Sajda-14 set**: Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96 — verified by direct corpus scan for the ۩-marker in `quran-no-tashkeel.json` (15 sajda-marked verses across 14 distinct surahs; Q 22 is the only surah with two sajda-verses, vv 18 and 77).

**Cohesion metric**: Pairwise mean Fisher-Rao distance over the 14 sajda-surahs:
`d_sajda = mean(d_FR(i, j) for i, j in sajda_14 with i < j)` — n_pairs = C(14, 2) = 91.

**Baseline**: corpus-wide pairwise mean FR over all C(114, 2) = 6,441 pairs.

**Permutation null**: 20,000 random 14-subsets of {1, 2, ..., 114}; for each, compute the same within-cluster pairwise mean. The empirical-permutation-p is the fraction of random-subset means strictly less than (or equal to) the observed sajda-14 mean.

## 3. Test statistic

**Primary (REVERSE-direction-locked)**: Permutation-p of `d_sajda ≤ random_14_subset_mean`.

**Secondary**: z-score of `d_sajda` against the random-14-subset distribution.

## 4. Success / Failure thresholds

- **NULL CONFIRMED (predicted)**: perm-p > 0.5 (i.e., sajda-14 cohesion is at-or-above corpus-baseline, rejecting the cohesion claim).
- **DIRECTIONAL TOWARD COHESION**: perm-p < 0.10.
- **WEAK COHESION**: 0.05 < perm-p ≤ 0.10.
- **COHESION CONFIRMED** (would falsify our reverse-direction prediction): perm-p ≤ 0.0167 (Bonferroni-k=3 family-level α).

## 5. Honest limits known a priori

- The Fisher-Rao matrix uses root-distribution as the primary feature; sajda-surahs may share content-cohesion at orthogonal feature spaces (verse-length, char-4-gram, named-entity). Cross-replication on h-new-111b (char-4-gram) and h-new-111c (verse-length) is OUT OF SCOPE for this test.
- Sajda-classification is a fiqh-tradition; the 14-list is canonized in classical-fiqh literature (al-Suyūṭī *al-Itqān* nawʿ 71). The 14 are not an arbitrary statistical-grouping but a tradition-canonized classification — making the cohesion-null doubly-informative.
- A reverse-direction NULL here does not refute the sajda-classification's value in fiqh; it confirms only that the classification is functional-liturgical and not content-fingerprint based.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, root-distribution-vector via H-NEW-111 default, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Permutation null

n_perm = 20,000 random 14-subsets of {1, 2, ..., 114} drawn with seed 20260509.
- Each random-subset's within-cluster pairwise mean FR is computed identically to `d_sajda`.
- Empirical-permutation-p = fraction of random-subset means ≤ observed `d_sajda`.

## 8. Garden-of-forking-paths log

- The reverse-direction prediction (NULL is expected) is SPECIALLY-DECLARED. The classical sujūd-al-tilāwah classification is functional, not content-fingerprint based; predicting cohesion-NULL is the principled prediction.
- The 14-list was verified by direct corpus scan BEFORE the cohesion-test. The verification (15 sajda-marked verses across 14 distinct surahs, with Q 22 contributing 2) was reported in [`01-empirical-profile.md`](01-empirical-profile.md) §10.
- The pre-test informational scan (NOT result-viewing for the primary test) computed `d_sajda = 0.9414` and corpus baseline = 0.9235 — direction-of-the-finding (within-cluster slightly higher than corpus baseline) is in the predicted direction. The formal SHA-locked test re-runs the computation with the locked seed.
- 20,000 perms is conservative for a single-statistic permutation test; n_perm = 10,000 would suffice for the family-level α = 0.0167. The 20K choice was made BEFORE result-viewing for stability.
- The metric is pairwise mean (not min, not max, not median) — chosen as the standard cluster-cohesion metric. Alternative metrics (e.g., mean-nearest-neighbor) would be alternative tests; this test pre-locks the pairwise-mean.

## 9. SHA256 lock

To be computed at write-time. Embedded in `scripts/Q053_F_all_tests.py`.
