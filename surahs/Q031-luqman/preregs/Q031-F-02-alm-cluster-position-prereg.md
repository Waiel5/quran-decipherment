---
test: Q031-F-02
title: Q 31 FR-position within the 6-surah ALM cohort
test_type: rank-within-cluster + permutation-null
direction_locked: NULL (pre-registered as expecting NO preferential cohesion of Q 31 with other 5 ALM surahs vs random 5-surah comparators)
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q031-luqman-specialist
alpha_bon: 0.025
acceptance_window:
  primary: Q 31 mean-FR-distance to 5 ALM-siblings should be NEAR the corpus-mean of random-5-subset distances (NOT preferentially close)
  secondary: Q 31 should be FR-closer to its top-12 nearest non-ALM neighbors than to its 5 ALM siblings
date_locked: 2026-05-09
---

# Q031-F-02 — Pre-registration

## 1. Rationale

Q 31 is one of 6 ALM-opened surahs {Q 2, Q 3, Q 29, Q 30, Q 31, Q 32}. The pre-registered question: does Q 31's Fisher-Rao root-distribution distance to its 5 ALM-siblings cluster preferentially below the corpus-baseline distance distribution?

The expected NULL direction is grounded in cross-finding-006 (muqaṭṭaʿāt = letter-axis ⊥ content-axis): muqaṭṭaʿāt are an orthographic-marker cluster, not a content-thematic cluster.

The ALM-cluster's overall pairwise FR mean is 0.9257 vs corpus 0.9234 — already at-corpus-baseline. The question is whether Q 31 specifically is preferentially close to its ALM-siblings compared to random 5-surah comparator subsets.

## 2. Hypothesis

**H1 (NULL-direction)**: mean(FR(Q 31, ALM-other-5)) is statistically indistinguishable from mean(FR(Q 31, random-5-subset)) — i.e. Q 31's ALM-membership does NOT predict ALM-cohesion. Permutation p ≥ 0.025.
**H2 (DIRECTION-positive)**: Q 31's mean FR to its ALM-siblings is HIGHER (i.e. less close, less cohesive) than its mean FR to its top-12 nearest non-ALM neighbors.

## 3. Method

- Corpus: `findings/phase-b-hypotheses/csv/h-new-111.json` D_matrix_upper_triangular (6,441 pairwise distances).
- ALM-siblings of Q 31: {Q 2, Q 3, Q 29, Q 30, Q 32}.
- Compute D_alm_q31 = mean of {FR(Q 31, Q 2), FR(Q 31, Q 3), FR(Q 31, Q 29), FR(Q 31, Q 30), FR(Q 31, Q 32)}.
- Top-12 nearest non-ALM neighbors of Q 31: from FR-row, exclude Q 31 itself + 5 ALM-siblings + take 12 nearest = {Q 45, Q 64, Q 22, Q 62, Q 35, Q 13, Q 112, Q 1, Q 61, Q 96, Q 91, Q 14}. Compute D_top12_q31 = mean of FR to these 12.
- Permutation null: 10,000 random 5-subsets from the 113 non-Q31 surahs (excluding Q 31). Compute mean(FR(Q 31, subset)). One-tailed p = P(perm_mean ≤ observed D_alm_q31).
- Bonferroni: k=2 (H1 perm-test + H2 direction-comparison-with-no-perm).

## 4. Pre-committed acceptance window

- NULL CONFIRMED (the pre-registered direction): perm-p ≥ α_bon = 0.025 — Q 31 is NOT preferentially FR-close to ALM-siblings.
- UNEXPECTED-COHESION (would falsify H1 NULL prediction): perm-p < α_bon — Q 31 IS preferentially close to ALM-siblings (would suggest sub-cohesion within ALM cluster, falsifying cross-finding-006).

For H2:
- DIRECTION-CONFIRMED: D_top12_q31 < D_alm_q31 (top-12 non-ALM closer than ALM).
- DIRECTION-REVERSED: D_alm_q31 < D_top12_q31 (ALM closer than top-12 non-ALM).

## 5. Garden-of-forking-paths log

- The expectation of NULL is GROUNDED in established corpus-finding cross-finding-006 (muqaṭṭaʿāt letter-axis ⊥ content-axis; replicated 4× including Q032-F-03 NULL).
- The top-12 cohort definition was set BEFORE looking at the FR-data: top-12 nearest by FR distance, which are listed in `01-empirical-profile.md` §2.
- Pre-reg writer is committing to publish whichever direction is found — this is an honest test of the established cross-finding-006 prediction at the Q 31 single-surah level.

## 6. Honest limits

- The N=5 ALM-sibling-subset is small; permutation null on 5-subsets has finite-sample noise.
- The top-12 comparison is descriptive (no-perm); H2 is an intuitive sanity-check, not a Bonferroni-cell.
- If both H1 NULL and H2 confirm, the result REPLICATES cross-finding-006 at Q 31 level.
- If H1 fails NULL (i.e. ALM-cohesion appears), this would be a SURPRISING result requiring follow-up.

## 7. Direction lock

LOCKED NULL on H1 (Q 31 has NO preferential ALM-cohesion); LOCKED positive on H2 (top-12 non-ALM closer than 5 ALM).

## 8. SHA-locking

This pre-reg file's SHA256 will be computed at write-time and verified at run-time.

## 9. Cross-references

- [[h-new-111-fisher-rao-mushaf]] — FR distance matrix.
- [[cross-finding-006]] — muqaṭṭaʿāt letter-axis ⊥ content-axis.
- [[surahs/Q032-al-sajda]] §6.3 Q032-F-03 — replicate-NULL on the 3-ALM-exception subset.
