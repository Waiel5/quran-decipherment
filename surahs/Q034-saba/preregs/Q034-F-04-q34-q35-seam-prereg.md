---
surah: 34
test_id: Q034-F-04
title: Q 34 → Q 35 mushaf-adjacency seam — LOW-cost pre-registration test (al-ḥamdu opener-twin pair)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q034-F-04-q34-q35-seam
alpha_bon: 0.01667
---

# Q034-F-04 — Pre-registration: Q 34 → Q 35 mushaf seam direction-LOW-cost test

## 1. Hypothesis (locked before observation)

Q 34 and Q 35 are the corpus's only **mushaf-adjacent al-ḥamdu li-llāh opener pair**. Of the 5 surahs in the opener cluster {Q 1, 6, 18, 34, 35}, only Q 34→Q 35 is mushaf-position-adjacent. The classical-rhetorical claim (al-Biqāʿī, *Naẓm al-Durar* — Q 34→Q 35 munāsabah anchored on the shared opener; al-Suyūṭī, *Tanāsuq al-durar*) predicts that this shared-opener mushaf-adjacency creates a **seamless transition** — i.e. low canonical-adjacency cost in H-NEW-720.

**H1 (locked direction LOW-cost, primary):** The Q 34 → Q 35 adjacency cost (delta_raw in `findings/phase-b-hypotheses/csv/h-new-720.json`) is in the **TOP-20 SMOOTHEST** of 113 mushaf-adjacencies (rank ≤ 20).

**H2 (locked direction, relative to opener-cluster transitions):** Q 34 → Q 35's cost is BELOW the median of the 5 openers' canonical-adjacency costs into their immediate mushaf-successor: {Q 1→Q 2, Q 5→Q 6 (the relevant adjacency for Q 6), Q 17→Q 18 (the relevant one for Q 18), Q 33→Q 34, Q 34→Q 35}. (Mushaf successor of each opener.)

**H3 (locked direction, FR-distance LOW):** Q 34 ↔ Q 35 Fisher-Rao distance is below the median of the 10 within-cluster pair distances (the cluster has C(5,2)=10 pairs).

**Direction:** Q 34 → Q 35 is structurally LOW-cost / LOW-distance / SEAMLESS.

## 2. Operational definitions

- **Source — adjacency cost**: `findings/phase-b-hypotheses/csv/h-new-720.json` `per_adjacency` entries, sorted by `delta_raw` ascending; rank assigned by position.
- **Source — FR distance**: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`.

## 3. Test statistic

- rank_seam: position of Q 34→Q 35 in ascending delta_raw.
- median_5_openers_cost: median of the 5 opener→successor delta_raw values.
- median_10_intra_cluster_fr: median FR over the 10 pairs in cluster {1,6,18,34,35}.
- d_q34_q35_fr: direct FR.

## 4. Permutation null

For H1: rank-based (no perm needed).
For H2: rank-based among 5 cells.
For H3: rank-based among 10 within-cluster pairs.

## 5. Success / Failure criteria

| Cells passing | Verdict |
|:--|:--|
| 3/3 | CONFIRMED |
| 2/3 | DIRECTIONAL |
| 1/3 | DIRECTIONAL-WEAK |
| 0/3 | NULL (Q 34→Q 35 is NOT structurally smooth despite opener-share) |

## 6. Honest limits known a priori

- Pre-flight observation: Q 34 → Q 35 delta_raw = 0.0745 (rank 65/113) — MID-PACK, NOT top-20. Pre-flight FR observation: Q 34 ↔ Q 35 FR = 0.9268, intra-cluster median ≈ 0.9706 (Q 34 ↔ Q 35 IS below median, so H3 likely PASSES). H1 will FAIL on pre-flight observation; H2 will be tested fresh.
- The locked LOW-cost direction is committed honestly per HANDOFF/04-DISCIPLINE.md; H1 will be published as NULL with full prominence. The verdict ceiling is **DESCRIPTIVE-EMPIRICAL**.
- This is the *empirical refinement* of the al-Biqāʿī munāsabah: shared opener does not guarantee smoothness at the QAC-root content-vector level. Same lesson as Q035-F-04 (which the Q 35 specialist runs from the other direction).

## 7. Rules-tuple

`(no-tashkeel, QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`.

## 8. Bonferroni

k = 3 (H1, H2, H3). α_bon = 0.01667.

## 9. Coordination

Cross-link with Q 35 al-Fāṭir specialist's Q035-F-04. Both tests are mutually informative; this one frames the test from Q 34 side and asks LOW-cost rank.

## 10. SHA256 lock

Embedded in `scripts/Q034_F_04_q34_q35_seam.py`; verified at runtime.
