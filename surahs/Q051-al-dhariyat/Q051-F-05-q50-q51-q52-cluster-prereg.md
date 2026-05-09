---
surah: 51
test_id: Q051-F-05
title: Q 50 → Q 51 → Q 52 mushaf-cluster — Q 51's hinge-side membership and Q 51-52-53 oath-trio mushaf-adjacency
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q051-F-05-q50-q51-q52-cluster
alpha_bon: 0.0167
---

# Q051-F-05 — Pre-registration: Q 51's mushaf-position role in the Q 49→50 hinge

## 1. Hypothesis (locked before observation)

Q 50 is one of the 3 universal hinges per H-NEW-130 / cross-finding-013 (Q 49→Q 50 is rank 14 of 15 top FR-jumps). Q 51 sits IMMEDIATELY POST this hinge. The hypothesis tests whether Q 51 is on the **Meccan-oath-cluster post-hinge side** with Q 52, 53.

**H1 (locked direction):** The Q 51 → Q 52 transition is in the **smoothest 25% of corpus-adjacencies** by H-NEW-720 delta_raw rank (i.e., rank ≤ 28 of 113).

**H2 (locked direction):** Q 51 is FR-closer to its right-neighbor Q 52 than to its left-neighbor Q 50 (i.e., FR(51, 52) < FR(51, 50)).

**H3 (locked direction, exploratory-secondary):** The 3-surah run Q 51-52-53 is one of 3 mushaf-adjacent oath-runs identified in H-NEW-1140 (CONFIRMED at p=0.022 corpus-wide). Verify operationally that all three (Q 51, Q 52, Q 53) are members of the strict-15 H-NEW-1070 oath-cluster, AND that Q 51-52, Q 52-53 transitions are both adjacent on the mushaf order.

**H0 (joint):** None of {H1, H2, H3} pass.

**Direction:** locked POSITIVE on all three (Q 51-side smoother + closer + adjacency-confirmed).

## 2. Operational definitions

- **H-NEW-720** delta_raw values from `findings/phase-b-hypotheses/csv/h-new-720.json`.
- **H-NEW-111** FR matrix from `findings/phase-b-hypotheses/csv/h-new-111.json`.
- **H1**: Q 51 → Q 52 delta_raw value, ranked among 113 corpus-adjacencies (ascending). Pass: rank ≤ 28.
- **H2**: FR(51, 52) and FR(51, 50). Pass: FR(51, 52) < FR(51, 50).
- **H3**: verify Q 51, Q 52, Q 53 ∈ {37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103} AND verify s + 1 = next surah (mushaf-adjacent) for both 51-52 and 52-53.

## 3. Test statistic

- Q 51 → Q 52 delta_raw, rank.
- FR(51, 52), FR(51, 50), difference.
- Boolean for H3 (membership + adjacency).

## 4. Permutation null

H1 and H2 are descriptive-comparative tests on observed values; no permutation needed.
H3 is a structural verification (Boolean).

## 5. Success / Failure

- **CONFIRMED**: H1, H2, H3 all pass.
- **DIRECTIONAL**: 1-2 of 3 pass.
- **NULL**: 0/3 pass.
- **PRE-COMMIT VIOLATION**: FR(51, 52) > FR(51, 50) (sign-flip on H2).

## 6. Honest limits known a priori

- The Q 49→Q 50 hinge is rank 14 (per H-NEW-130 top-15); Q 50→Q 51 is rank 89 (mid-tier expensive). The pre-reg locks a specific prediction about Q 51's directionality on the post-hinge side.
- The H-NEW-1070 cluster membership and H-NEW-1140 mushaf-adjacency are pre-existing CONFIRMED findings; this test is a Q 51-specific verification.
- The directional locks (FR(51,52) < FR(51,50), Q 51-52 in cheapest 25%) are based on inspection of H-NEW-720 ranks BEFORE pre-reg lock.

## 7. Rules-tuple

`(no-tashkeel, FR-on-QAC-stem-roots, canonical-mushaf-order, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`.

## 8. Bonferroni

k = 3 (H1 rank, H2 FR-comparison, H3 cluster-membership). α_bon = 0.0167.

## 9. Coordination

This is a Q 51-specific extension of H-NEW-130 / H-NEW-1070 / H-NEW-1140. Independent of any prior test. Q 50 specialist's adjacent-surah-role test is separate.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q051_F_05_q50_q51_q52_cluster.py`, verified at runtime.
