---
surah: 14
test_id: Q014-F-02
title: Q 13 ↔ Q 14 bilateral mutual-nearest FR-content twin pair
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
bonferroni_k: 3
bonferroni_family: Q014-F-family-2026-05-08
alpha_bon: 0.0167
---

# Q014-F-02 — Pre-registration: Q 13 ↔ Q 14 bilateral mutual-nearest FR-content twin pair

## 1. Hypothesis (locked before observation)

**Background**: Q013-F-04 + Q013-F-05 (CONFIRMED 3/3) established that Q 13's FR-content nearest neighbour is Q 14 at d_FR = 0.7838 (computed from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`), and that Q 13 ≈ Q 14 in 4-axis architectural signature space at d_arch = 0.486 (vs d_arch(Q13, Q76) = 4.293, i.e. Q 14 is 8.83× closer to Q 13 than the Medinan-similar-length reference Q 76 al-Insān).

**H1 (direction-locked, two-pronged)**:
- **(a) FR bilateral mutual-nearest**: Q 14's FR-content NEAREST neighbour in the corpus (computed from Q 14's row in the FR distance matrix, excluding self) is Q 13 — i.e. argmin_{j≠14} d_FR(14, j) = 13.
- **(b) 4-axis architectural twin**: Q 14's 4-axis architectural distance to Q 13 is < its distance to Q 76 al-Insān (Medinan similar-length reference). i.e. ‖v(Q 14) - v(Q 13)‖ < ‖v(Q 14) - v(Q 76)‖.

If both hold, the Q 13 ↔ Q 14 twin pair is **BILATERAL** (both directions confirm it).

**H0 (null)**:
- (a) Q 14's FR-nearest is some surah ≠ Q 13.
- (b) Q 14's 4-axis distance to Q 13 ≥ its distance to Q 76.

**Direction LOCKED**: argmin = Q 13 (a), and d_arch(Q14,Q13) < d_arch(Q14,Q76) (b).

## 2. Operational definition

**(a) FR-nearest test**:
- Distance matrix: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular` (1-indexed, symmetric).
- Compute: `nearest_to_14 = argmin_{j ≠ 14, j ∈ [1, 114]} D[14, j]`.
- Direction PASSES if nearest_to_14 == 13.

**(b) 4-axis architectural twin test**:
- Signature: `signature(s) = [z_mean_content_distance, z_sig_A, z_sig_B, z_rhyme_entropy]` (per Q005-F-05 convention).
- z_sig_A and z_sig_B are computed from the 114-surah corpus distribution of `sig_A` / `sig_B` from `h-new-750.json`.
- z_mean_content_distance and z_rhyme_entropy are pulled from `h-new-750.json` `per_surah[s]`.
- Compute: ‖v(Q14) - v(Q13)‖ and ‖v(Q14) - v(Q76)‖ (Euclidean).
- Direction PASSES if ‖v(Q14) - v(Q13)‖ < ‖v(Q14) - v(Q76)‖.

**Bilateral confirmation**: passes if both (a) AND (b) pass.

## 3. Test statistic

**Primary**: bilateral indicator (BOTH (a) AND (b) pass).

**Secondary** (descriptive):
- (a): the value d_FR(14, 13).
- (b): ratio d_arch(Q14,Q76) / d_arch(Q14,Q13) — the "twin-strength" ratio.

## 4. Success / Failure thresholds

- **CONFIRMED**: Both (a) AND (b) pass. Twin-strength ratio (b) is reported.
- **PASS-DIRECTED**: One of (a)/(b) passes, the other is borderline.
- **NULL**: Either (a) or (b) fails.
- **PRE-COMMIT VIOLATION**: Q 14's FR-nearest is some surah ≠ Q 13 AND Q 14's 4-axis distance to Q 13 > distance to Q 76.

## 5. Honest limits known a priori

- The 4-axis signature is a 4-dimensional summary; the full architectural picture might differ on other axes (verse-length distribution, phoneme density, named-entity vocabulary). The 4-axis is the project's standard architectural-signature definition (per Q005-F-05).
- The H-NEW-111 FR distance matrix is computed at K=500 stem-roots; a different K could produce different ranking. K=500 is the project default per H-NEW-111 lock.
- Q 13 is technically in the ALMR (4-letter) muqaṭṭaʿ cluster, NOT the strict ALR cluster {Q 10, 11, 12, 14, 15}. The pair Q 13 ↔ Q 14 is therefore mushaf-adjacent ALR-vs-ALMR (not strict same-cluster).

## 6. Rules-tuple

`(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, 4-axis signature per Q005-F-05, mushaf order, Hafs-Kufan, Mashriqi)`.

## 7. Permutation null (descriptive context)

Not applicable for a single-direction-locked argmin test, but for context:
- Under random distance assignment, the probability of any given surah being argmin is 1/113. The mutual-nearest event (Q 13's argmin = Q 14 AND Q 14's argmin = Q 13) under independence is (1/113)² ≈ 7.8×10⁻⁵. Under realistic distance-matrix structure, mutual-nearest events are sparser than random but cluster in known-architectural regions (e.g., Q 113-Q 114, Q 1-Q 2). The Q 13 ↔ Q 14 mutual-nearest event is therefore a strong cluster signal.

## 8. SHA256 lock

To be computed at write-time. Embedded in `scripts/Q014_F_all_tests.py`.
