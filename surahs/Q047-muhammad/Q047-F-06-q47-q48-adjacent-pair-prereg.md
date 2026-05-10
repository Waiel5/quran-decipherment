---
test_id: Q047-F-06
title: "Q 47 ↔ Q 48 mushaf-adjacent pair — in_all_three cohesion via H-NEW-130 family + FR pair-rank"
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q047-F-06-q47-q48-pair
alpha_bon: 0.025
direction_locked: true
rules_tuple: (no-tashkeel, QAC-stem-root + char-4-gram + verse-length-histogram, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q047-wave-J-specialist
parent_findings:
  - H-NEW-130 (FR-root residuals)
  - H-NEW-130b (char-4gram residuals)
  - H-NEW-130c (verse-length residuals)
  - H-NEW-111 (FR distance matrix)
  - cross-finding-011 (mushaf Fisher-Rao geometry)
classical_anchors:
  - al-Bukhārī, *Ṣaḥīḥ*, kitāb al-tafsīr — pairing of Q 47:22 tafsīr-bāb (#4623-4625) with Q 48 Hudaybiyya tafsīr-bāb (#4627-4633), indicating editorial-cluster treatment.
  - al-Biqāʿī, *Naẓm al-Durar* — Q 46→Q 47→Q 48 munāsabah (war-permission→war-instruction→conquest-promise sequence).
  - Ibn Kathīr on Q 47, on the linkage *bi-mā nuzzila ʿalā Muḥammad* (Q 47:2) ↔ *Muḥammadun rasūlu llāh* (Q 48:29).
---

# Q047-F-06 Pre-registration — Q 47 ↔ Q 48 mushaf-adjacent pair

## Hypothesis

Per al-Biqāʿī's munāsabah Q 46→Q 47→Q 48 (war-permission → war-instruction → conquest) and al-Bukhārī's editorial pairing of the Q 47:22 tafsīr-bāb with the Q 48 Hudaybiyya bāb, the Q 47-Q 48 adjacency is an architecturally **cohesive** pair, NOT a boundary-jump. The H-NEW-130 family identifies adjacency-pairs that are EITHER cohesive (small consecutive distance, *not* a jump) OR boundaries (large jump, *in_all_three* of the top-15 jump lists).

We pre-register two complementary sub-tests:

### Test A (cohesion-direction)
Q 47 ↔ Q 48 is in the bottom-15 (cheapest) consecutive adjacencies in **all three** D-matrices (FR-root, char-4-gram, verse-length-histogram). This would mean the Q 47→Q 48 transition is among the corpus's tightest editorial seams across all three feature axes.

### Test B (FR-pair rank)
Q 47-Q 48 FR distance is in the bottom-25th percentile of all 6,441 surah-pairs (i.e., FR-rank ≤ 1610 of 6441).

## Pre-committed prediction (DIRECTION LOCKED)

**Direction A**: Q 47-Q 48 ∈ bottom-15 of consecutive-adjacency distances in h-new-130 (root), h-new-130b (char-4gram), AND h-new-130c (verse-length).

**Direction B**: rank_low(Q 47-Q 48 FR distance) ≤ 1610 (top quartile, i.e., bottom-25% of pair-distances).

## Test (Bonferroni-2)

Family size k = 2.
α_corrected = 0.05 / 2 = 0.025.

For Test A (combinatoric): p = (15/113)^3 ≈ 0.0023 under independence null (each of 3 boundary-tests has ≈13% rate). Bonferroni corrected: 0.025 threshold.
For Test B (pair-rank): p_low = rank/6441; threshold ≤ 0.025 means rank ≤ 161.

## Direction-of-effect lock

Pre-committed:
- VINDICATED-FULL: Test A passes (in_all_three) AND Test B passes (rank ≤ 161).
- VINDICATED-PARTIAL: Test A passes OR Test B passes.
- DIRECTIONAL: Q 47-Q 48 in bottom-25% on FR-root pair-rank only (rank ≤ 1610).
- NULL: neither.

## Garden-of-forking-paths log

- BEFORE running: noted that h-new-130 family's "in_all_three" is documented in h-new-130c.top15_largest_jumps as boundary-pairs (largest jumps). Cohesion-pairs (smallest jumps) are NOT separately catalogued in the JSONs — we have to compute the bottom-15 ourselves from the consecutive_mushaf_distances dict. The brief's "in_all_three=True per H-NEW-130/130b/130c" specifies the boundary-list direction, which is the SEMANTIC OPPOSITE of the cohesion-direction we want (cohesive pair = NOT a boundary = NOT in top-15 jumps).
- BEFORE running: chose the COHESION direction (bottom-15) to match the brief's intent ("Q 47-Q 48 is a cohesive pair, not a boundary"). This is a brief-interpretation choice documented BEFORE viewing the result.
- BEFORE running: Test B's quartile threshold (rank ≤ 1610) is conservative; a stricter "bottom-decile" (rank ≤ 644) would be more demanding but the existing comprehensive overview's FR(Q47,Q48) = 0.889 vs corpus median 0.957 strongly suggests bottom-25%.
- BEFORE running: alternative MW-3 framing — al-Biqāʿī's munāsabah is binary-coarse, predicting only that Q 47-Q 48 is "more cohesive than average"; that's Test B. Test A is the much stricter top-15 universalist claim.

## Honest limits

1. The H-NEW-130 family's "in_all_three" attribute is documented in the JSON for BOUNDARY pairs (jumps), not cohesion pairs. We re-purpose the consecutive_mushaf_distances data to compute cohesion ranks ourselves. This is a fair use of the same data but is a CHOICE point logged here.
2. The pre-existing Q 47 comprehensive overview reports FR(Q47,Q48) = 0.889 (a known value). Test B is therefore not blinded; it is a verification-and-rank step. The honest framing is: this codifies the existing observation against a pre-committed quartile threshold and a corrected Bonferroni-2 envelope.
3. Test A is genuinely novel and blinded (we have not pre-viewed the bottom-15 lists from h-new-130b/c).
4. If Q 47-Q 48 is mid-pack (rank 50-80) in any of the three D-matrices, Test A fails — this would CONSTRAIN al-Biqāʿī's claim to a coarser corpus-quartile level, not a top-15 universal-seam level.
