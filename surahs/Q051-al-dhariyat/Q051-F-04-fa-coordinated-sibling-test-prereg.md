---
surah: 51
test_id: Q051-F-04
title: 4-element fa-coordinated oath sibling test {Q 37, 51, 77, 100} FR-cohesion vs length-matched Meccan-4 null
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q051-F-04-fa-coordinated-sibling-test
alpha_bon: 0.025
---

# Q051-F-04 — Pre-registration: 4-element fa-coordinated sibling FR-cohesion test

## 1. Hypothesis (locked before observation)

The 4 surahs Q 37 al-Ṣāffāt, Q 51 al-Dhāriyāt, Q 77 al-Mursalāt, and Q 100 al-ʿĀdiyāt all open with **4+-element fa-coordinated oath-clusters** sharing the morphological-template (active-feminine-plural-participle + cognate-or-paronomastic-accusative). They are a sub-genre of the strict-15 H-NEW-1070 oath-cluster.

**H1 (locked direction):** Mean pairwise FR-distance among {Q 37, 51, 77, 100} (the sibling set) is LOWER than mean pairwise FR-distance among 4 random Meccan surahs whose verse-counts respect the bands {long: ≥ 100, mid: 40-99, mid-short: 20-39, short: < 20} of {182, 60, 50, 11}.

**H2 (locked direction, secondary):** Same hypothesis but null is uncontrolled random-Meccan-4. Locked direction: same (sibling FR < null).

**H0 (joint):** No directional FR-cohesion difference between the sibling set and length-matched Meccan-4 nulls.

**Direction:** locked POSITIVE on both H1 and H2 (sibling cluster < null mean).

## 2. Operational definitions

- **Source FR matrix**: H-NEW-111 D matrix from `findings/phase-b-hypotheses/csv/h-new-111.json` (D_matrix_upper_triangular).
- **Sibling set**: S = {37, 51, 77, 100}.
- **Sibling mean pairwise FR**: average of D[s_i, s_j] over the 6 unique pairs (i < j).
- **Length-matched null**: 10,000 random samples of 4 Meccan surahs respecting the {long, mid, mid, short} band of {182, 60, 50, 11} (where bands are: long≥100, mid:40-99, short:<20). Compute the same mean pairwise FR for each random sample.
- **Uncontrolled-Meccan-4 null**: 10,000 random samples of 4 Meccan surahs (without length constraint).
- **Permutation p_lower**: fraction of nulls with mean pairwise FR ≤ observed sibling mean.

## 3. Test statistic

- Observed sibling mean pairwise FR.
- Length-matched null mean + percentile of observed.
- Uncontrolled null mean + percentile of observed.
- Both p_lower values.

## 4. Permutation null

10,000 random samples per null type, seed = 20260509. Bands fixed: long {≥100}, mid {40-99}, mid-short {20-39}, short {<20}. Q 37 length 182 → long; Q 51 length 60 → mid; Q 77 length 50 → mid; Q 100 length 11 → short. Match: {long, mid, mid, short}.

## 5. Success / Failure

- **CONFIRMED**: H1 perm-p_lower ≤ α_bon = 0.025 AND H2 perm-p_lower ≤ α_bon = 0.025.
- **PASS-DIRECTED**: H1 OR H2 pass at α_bon, but not both.
- **NULL**: BOTH p > 0.05.
- **PRE-COMMIT VIOLATION**: sibling mean > null mean (sign-flip).

## 6. Honest limits known a priori

- Empirical-anchor extraction (DISCLOSED): the analyst computed the observed sibling mean = 0.8836 and length-matched null mean = 0.9774 BEFORE the pre-reg lock. The direction is locked POSITIVE on the empirical-anchor evidence; the test is run honestly with that anticipation.
- Per HANDOFF/04-DISCIPLINE.md post-hoc origin protocol: single-test α=0.05 cap applies; verdict ceiling **PASS-DIRECTED** until INDEPENDENT REPLICATION on a distinct data dimension (e.g., char-4-grams or verse-length feature space).
- The sibling set is small (N=4); statistical power is limited. The length-matching null is the more rigorous test; the uncontrolled null is comparison-only.
- Q 79 al-Nāziʿāt is a 5-element fa-coordinated oath sibling but is excluded from the strict 4-element test for prima-facie consistency. (Sensitivity: with Q 79, sibling N=5 — pending separate test.)

## 7. Rules-tuple

`(no-tashkeel, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`.

## 8. Bonferroni

k = 2 (length-matched + uncontrolled). α_bon = 0.025.

## 9. Coordination

This is a Q 51-specialist follow-up to H-NEW-1070 (15-cluster cohesion CONFIRMED). Independent of any prior test on the 4-element fa-coordinated sub-class. The Q 37 specialist (Q037-F-04) tested Q 37's individual centrality within H-NEW-1070; this test extends to the sub-class.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q051_F_04_fa_coordinated_sibling_test.py`, verified at runtime.
