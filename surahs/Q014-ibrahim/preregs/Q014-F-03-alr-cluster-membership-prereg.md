---
surah: 14
test_id: Q014-F-03
title: Q 14 ALR-cluster FR-membership distinctiveness
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
bonferroni_k: 3
bonferroni_family: Q014-F-family-2026-05-08
alpha_bon: 0.0167
---

# Q014-F-03 — Pre-registration: Q 14 ALR-cluster FR-membership distinctiveness

## 1. Hypothesis (locked before observation)

**Background**: Q 14 is a member of the ALR muqaṭṭaʿāt cluster {Q 10, 11, 12, 14, 15}. The al-Biqāʿī muqaṭṭaʿāt-content-munāsaba doctrine asserts that letter-family clusters are content-cohesive. H-NEW-610 establishes that this is FALSIFIED at whole-surah scale across 4 letter-family replications (full-29, ḥawāmīm-7, ALM-6, ALR-5). This test re-evaluates the claim from Q 14's perspective with a permutation null.

**H1 (direction-locked, one-tailed)**: Q 14's mean FR-content distance to its 4 ALR siblings is **CLOSER than to a randomly-sampled 4-surah subset** of non-ALR-non-Q14 surahs. i.e., d̄(Q14 → ALR-siblings) < d̄(Q14 → random-4).

**H0 (null)**: d̄(Q14 → ALR-siblings) ≥ d̄(Q14 → random-4) (no preferential FR-cluster cohesion).

**Direction LOCKED**: closer to ALR-siblings than random.

## 2. Operational definition

**Distance matrix**: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular` (1-indexed, symmetric).

**ALR cluster**: {10, 11, 12, 13, 15}. Note: Q 13 is technically ALMR (4-letter) but is included as a mushaf-adjacent letter-family-related surah per the Q013 specialist's convention; alternatively, ALR-strict = {10, 11, 12, 15} (4 siblings, excluding Q 13). We test BOTH operationalizations.

**Test (a) — strict ALR**:
- ALR-strict-siblings = {10, 11, 12, 15} (4 surahs; excludes Q 13).
- d̄_obs = mean( D[14, s] for s in {10, 11, 12, 15} )
- ALR-internal-strict-pairwise = pairs of (s, t) for s, t in {10, 11, 12, 15}; mean.
- Δ_strict = d̄_obs − ALR-internal-strict-pairwise.

**Test (b) — ALR-extended (with Q 13)**:
- ALR-ext-siblings = {10, 11, 12, 13, 15} (5 surahs; includes Q 13).
- d̄_obs_ext = mean( D[14, s] for s in {10, 11, 12, 13, 15} )

**Permutation null**:
- For 10,000 random samples (seed 20260508):
  - Sample 4 surahs from {1, ..., 114} \ ({14} ∪ ALR-strict).
  - Compute d̄_random = mean( D[14, s] for s in random-4 ).
  - Count fraction of trials where d̄_random ≤ d̄_obs.
- p_perm_strict = fraction.
- Repeat for 5-surah samples → p_perm_ext.

## 3. Test statistic

**Primary**: p_perm_strict (probability that random 4-surah subset is at least as close as the ALR-strict-siblings).

**Secondary**: p_perm_ext (5-surah).

**Tertiary** (descriptive): the per-pair distances from Q 14 to each ALR-sibling.

## 4. Success / Failure thresholds

- **CONFIRMED**: p_perm_strict ≤ α_bon = 0.0167 (Bonferroni-k=3 for the Q 14 family).
- **DIRECTIONAL**: p_perm_strict ≤ 0.05.
- **NULL**: p_perm_strict > 0.05.
- **PRE-COMMIT VIOLATION**: d̄(Q14 → ALR-strict) > corpus-mean d̄(Q14 → random-4) — i.e. Q 14 is FR-FARTHER from ALR than from random.

## 5. Honest limits known a priori

- H-NEW-610 NULL on letter-family content-cohesion suggests the test is inherently low-power: the ALR cluster's internal-pairwise mean (0.955 from Q013-F-04) is essentially the corpus pairwise mean (0.957 from same). Random surahs are approximately as FR-close to the ALR cluster on average. **Predicted result: NULL or DIRECTIONAL, NOT CONFIRMED**.
- Q 13 inclusion (ALR-extended) might inflate the apparent cohesion via the Q 13 ↔ Q 14 bilateral mutual-nearest pair, which Q014-F-02 verifies independently. The ALR-strict test (excluding Q 13) is the cleaner test of the al-Biqāʿī cluster-content claim.
- The 4-surah random sample is a conservative null — sampling from non-ALR surahs only. Sampling from any 4-surah subset of the corpus (including ALR-internal subsets) would be a separate, more permissive null.

## 6. Rules-tuple

`(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, mushaf order, Hafs-Kufan, Mashriqi)`.

## 7. Replication / cross-finding context

This test re-runs the same logic as Q013-F-04 (which got NULL at α_bon = 0.01, p_perm = 0.143). If Q014-F-03 also returns NULL, this **REPLICATES the H-NEW-610 letter-family-content-NULL finding** from a 6th specialist run (4 prior NULLs in H-NEW-610: full-29, ḥawāmīm-7, ALM-6, ALR-5; plus Q013-F-04 NULL on the same ALR-cluster from Q 13's perspective; this would be the 6th replication).

## 8. SHA256 lock

To be computed at write-time. Embedded in `scripts/Q014_F_all_tests.py`.
