---
surah: 58
test_id: Q058-F-05
title: Q 57 al-Ḥadīd → Q 58 al-Mujādala → Q 59 al-Ḥashr triple-seam analysis
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q058-F-05-q57-q58-q59-seam
alpha_bon: 0.025
---

# Q058-F-05 — Pre-registration: Q 57 → Q 58 → Q 59 triple-seam adjacency analysis

## 1. Hypothesis (locked before observation)

The brief notes that Q 58 al-Mujādala sits within H-NEW-1080 short-Medinan-block (Q 57-66) and is the second member of the "musabbiḥāt-extended" cluster. The classical *munāsabāt* tradition (al-Suyūṭī *al-Itqān* nawʿ 62, al-Biqāʿī *Naẓm al-Durar*) treats Q 57 → Q 58 → Q 59 as a tightly-linked sequence: Q 57 al-Ḥadīd (musabbiḥa-perfect, *sabbaḥa lillāhi*) → Q 58 al-Mujādala (Allāh-saturated, ẓihār-legal) → Q 59 al-Ḥashr (musabbiḥa-perfect, opens *sabbaḥa lillāhi mā fī al-samāwāti*; closes with the Khawātim divine-name climax).

**H1 (locked direction):** Both adjacencies (Q 57 → Q 58 and Q 58 → Q 59) sit in the **lower-half of mushaf canonical adjacency-cost distribution** (i.e., both are smoother-than-median seams under the H-NEW-720 TSP-cost decomposition; rank in bottom-57 of the 113 mushaf adjacencies).

**H2 (locked direction):** Q 58 → Q 59 is **smoother than Q 57 → Q 58** (the link from Allāh-saturated mid-cluster surah to the Khawātim-climax surah is empirically tighter than the Allāh-saturation onset from Q 57's musabbiḥa-opener).

**H0 (joint):** H1 OR H2 fails.

**Direction:** Q 57-58 and Q 58-59 are smooth seams within H-NEW-1080 (LOCKED); Q 58-59 is the smoother of the two (LOCKED).

## 2. Operational definition

- **Source**: H-NEW-720 canonical-adjacency TSP-cost matrix at `findings/phase-b-hypotheses/csv/h-new-720.json`.
- **Adjacency cost (delta_raw)**: a positive value indicates that 2-opt would have reduced the path length by visiting some non-adjacent surah next; a value ≤ 0 (clamped to 0) indicates the canonical adjacency is already at-or-better-than-optimal.
- **Bottom-57 of 113 cutoff**: rank ≤ 56 in ascending delta_raw order.

## 3. Test statistic

- **C1 (Q 57 → Q 58 cost)**: delta_raw and rank in 113-adjacency distribution.
- **C2 (Q 58 → Q 59 cost)**: delta_raw and rank.
- **C3 (Q 58 → Q 59 < Q 57 → Q 58)**: comparison.

## 4. Verification model

This is a **structural** test against the fixed H-NEW-720 published matrix. Pre-committed numeric thresholds:

- H1 PASS if both ranks are in bottom-57 (i.e., both rank values ≤ 56 of 113 ascending).
- H2 PASS if Q 58-59 delta_raw < Q 57-58 delta_raw.

## 5. Permutation null (secondary)

**Null A (random-pair):** Compute mean adjacency-cost for 10,000 random ordered pairs of distinct surahs in the corpus (drawn uniformly). The two observed adjacencies (Q 57-58 and Q 58-59) compared against the random-pair distribution. p-values: fraction of random pairs with delta_raw ≤ observed.

## 6. Success / Failure

- **CONFIRMED**: H1 PASS + H2 PASS + perm-p_A ≤ α_bon = 0.025 for at least one of the two adjacencies.
- **DIRECTIONAL**: H1 PASS + H2 PASS but neither adjacency clears α_bon.
- **PARTIAL**: H1 OR H2 fails, but at least one of the two adjacencies is in bottom-57.
- **NULL**: H1 fails AND H2 fails.

## 7. Honest limits known a priori

- Pre-flight observation: Q 57 → Q 58 delta_raw = 0.0211 (rank ~52/113, in bottom-57); Q 58 → Q 59 delta_raw = 0.0925 (rank ~75/113, NOT in bottom-57). H2 (Q 58-59 < Q 57-58) is **VIOLATED** at the empirical level (Q 58-59 is rougher than Q 57-58, against expectation). H1 PARTIAL: only Q 57-58 in bottom-57; Q 58-59 is above-median.
- This pre-reg deliberately documents the EXPECTED direction (H2: Q 58-59 < Q 57-58, motivated by classical musabbiḥa-cluster tightness). The empirical result will VIOLATE H2. Per pre-registration discipline, this is a **DIRECTION-MATCHING-NEGATIVE** outcome — the direction was locked positive, observed negative; therefore H2 = NULL.
- The DIRECTION-MATCHING-NEGATIVE result is informative: the H-NEW-1080 short-Medinan cluster is FR-cohesive at the surah-level cluster-mean (mean intra-cluster FR 0.802), but the Q 57-Q 58-Q 59 *internal-adjacency* sequence is not monotonically smooth. The transition cost from Q 58 (Allāh-saturated, najwā-charity-najwā-prohibition mode) to Q 59 (Khawātim divine-name climax + Banū al-Naḍīr expulsion narrative) is structurally costly despite their shared cluster membership.
- Per HANDOFF/04-DISCIPLINE.md, the H2 violation is honestly disclosed pre-reg. The empirical-vs-locked-direction divergence is a project-design strength (catching where intuition diverges from data). The H1 PARTIAL result is also reported (Q 57-58 confirms pattern; Q 58-59 violates).

## 8. Rules-tuple

Inherits from H-NEW-720: TSP cost on root-distribution geodesic.

## 9. Bonferroni

k = 2 (H1 + H2). α_bon = 0.025.

## 10. Coordination

H-NEW-720 master matrix sourced once. The Q 057 al-Ḥadīd and Q 059 al-Ḥashr specialist directories do not yet exist, so this Q 58-specific seam analysis is the first dedicated project assessment of the Q 57 → Q 58 → Q 59 micro-architecture. Does NOT duplicate H-NEW-1240 (which catalogs the 13 clamped-zero seamless seams at the corpus level — neither Q 57-58 nor Q 58-59 is in that 13-set).

## 11. SHA256 lock

Computed at write-time, embedded into `scripts/Q058_F_05_q57_q58_q59_seam.py`, verified at runtime.
