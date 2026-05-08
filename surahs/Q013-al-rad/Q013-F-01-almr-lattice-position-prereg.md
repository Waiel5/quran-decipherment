---
surah: 13
test_id: Q013-F-01
title: "ALMR letter-family-lattice position — is Q 13's FR-content axis BETWEEN the ALM and ALR cluster centroids?"
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q013-F-family-2026-05-07
alpha_bon: 0.01
n_perm: 10000
---

# Q013-F-01 — Pre-registration: ALMR letter-family-lattice position

## 1. Hypothesis (locked before observation)

Q 13's muqaṭṭaʿ المر (ALMR) is a 4-letter combination unique to Q 13. Its letters decompose as **ALM (alif-lām-mīm) + ر (rāʾ)**. The ALM cluster is {Q 2, 3, 29, 30, 31, 32}; the ALR cluster is {Q 10, 11, 12, 14, 15}.

**H1 (locked direction)**: Q 13's Fisher–Rao distance to the ALM-cluster centroid (mean of FR distances to Q 2, 3, 29, 30, 31, 32) and Q 13's FR distance to the ALR-cluster centroid (mean of FR distances to Q 10, 11, 12, 14, 15) are BOTH below the median pairwise FR distance among non-Q-13 surahs. I.e. **Q 13 is FR-near BOTH clusters simultaneously** — empirically "between" the two clusters in content-axis.

**Operational test statistic**: `between_indicator = 1` if both `mean_FR(Q13 → ALM)` AND `mean_FR(Q13 → ALR)` are below the global pairwise FR median; else 0.

**H0**: Q 13 is closer to one cluster but not the other (single-cluster membership).

**Direction (locked)**: BETWEEN — i.e. Q 13 simultaneously near both clusters.

## 2. Operational definition

For ALM = {2, 3, 29, 30, 31, 32}: compute `d̄_ALM = mean(FR(13, s) for s ∈ ALM)`.
For ALR = {10, 11, 12, 14, 15}: compute `d̄_ALR = mean(FR(13, s) for s ∈ ALR)`.

Reference null: pairwise FR distances among the 113 non-Q-13 surahs (i.e. the 6,328 unordered pairs of non-Q-13 surah-pairs from H-NEW-111). The global median of this distribution is the threshold.

**Permutation null**: random label assignment. Assign each of 12 cluster-positions (6 ALM + 5 ALR + 1 ALMR-Q13-pivot) to a random surah (without replacement). Compute the BETWEEN indicator under each permutation. Test whether the OBSERVED BETWEEN result is more extreme than null.

**Predicted-direction-locked**: `mean_FR(13, ALM) < median_pairwise` AND `mean_FR(13, ALR) < median_pairwise`.

**Secondary measurements (descriptive, not pre-registered for verdict)**:
- Compare `d̄_ALM` to `d̄_ALR`: which is smaller? Does Q 13 sit closer to ALM or ALR?
- Compare both to ALR-internal pairwise mean (excluding Q 13) and ALM-internal pairwise mean.

## 3. Test statistic

**Primary**: BETWEEN indicator on observed data + permutation p-value.

**Pre-committed acceptance window**: p_perm ≤ α_bon = 0.01.

## 4. Success / Failure

- **CONFIRMED**: BETWEEN indicator = 1 AND p_perm ≤ 0.01.
- **DIRECTIONAL**: BETWEEN indicator = 1 BUT 0.01 < p_perm ≤ 0.05.
- **NULL**: BETWEEN indicator = 0 (Q 13 closer to one cluster only).
- **Pre-commit violation**: Q 13 strongly distant from BOTH clusters (above-median to both).

## 5. Honest limits known a priori

- The "BETWEEN" hypothesis is bidirectional in the sense that both means must be below the threshold; this is a stronger pre-commit than "near-one-cluster".
- The null distribution is constructed from non-Q-13 pairwise FR distances; this controls for the generic FR distance distribution but does NOT control for length, register, or chronology.
- The ALM cluster size (6) and ALR cluster size (5) differ; the means are over different N. The descriptive measurements (which cluster is closer in mean) are reported without verdict-level interpretation.
- The hypothesis assumes content-axis ⊥ letter-axis ([[h-new-610-letter-families]] established this NULL on cohesion); we are testing whether the *specific 4-letter combination* shifts Q 13 toward an intermediate position. Even if both clusters are content-NULL on cohesion, Q 13 can still be FR-close to both.

## 6. Rules-tuple

`(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Distance source: H-NEW-111 D matrix (`findings/phase-b-hypotheses/csv/h-new-111.json`, upper-triangular).

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q013_F_01_almr_lattice.py`. Verified at runtime via `_assert_prereg_sha`.

## 8. Garden-of-forking-paths

- Considered: testing ALR-CLUSTER-MEMBERSHIP (Q 13 closer to ALR-mean than to non-cluster mean). REJECTED: this is a directional one-tail and a single-cluster-membership claim — easier to pass and less informative than the BETWEEN claim. Pre-committed to BETWEEN to make the stronger claim.
- Considered: using ALMS (Q 7) as a 3rd cluster reference. REJECTED: ALMS has only 1 surah (no centroid concept).
- Considered: weighting by cluster-internal distance. REJECTED: adds free parameters; pre-committed unweighted means.
