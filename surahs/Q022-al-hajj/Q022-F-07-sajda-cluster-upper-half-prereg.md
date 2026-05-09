---
test_id: Q022-F-07
title: "Q 22 is in the UPPER HALF of the H-NEW-1330 14-surah sajda set by FR-distance"
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q022-F-07-sajda-cluster-upper-half
alpha_bon: 0.05
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q022-al-hajj-specialist
---

# Q022-F-07 Pre-registration — Q 22 in upper-half of sajda-cluster by FR distance

## Hypothesis

H-NEW-1330 established CONFIRMED-NULL: the 14 classical-Sunnī sajda-surahs {Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96} do NOT form a Fisher-Rao cohesive cluster on root-distribution (p_perm = 0.571, length-matched p = 0.110; PC passes at p = 0.00020). Independent replication by Q053-F-03 at p_perm = 0.588.

If H-NEW-1330 is correctly NULL because the sajda-trigger is too thin a marker to drive root-frequency cohesion, then Q 22 — itself a TRUE-ISOLATE per H-NEW-126 — should be a LESS-COHESIVE member, not a more-cohesive one. Specifically, Q 22's mean FR-distance to the OTHER 13 sajda-surahs should rank in the upper half (rank > 7 of 14) of within-cluster cohesion measures.

This is a COMPLEMENT to H-NEW-1330: not a contradiction, but a refinement — Q 22 contributes to the NULL by being itself isolated from the other sajda-surahs.

## Pre-committed prediction

**Direction-locked**: Q 22's mean Fisher-Rao distance to the 13 other sajda-surahs is in the **UPPER HALF** by rank among the 14 sajda-surah members. Specifically, rank > 7 (rank 8-14), where rank-1 = lowest-distance (most cohesive) and rank-14 = highest-distance (least cohesive).

## Test (Bonferroni-1, α=0.05)

1. **T1 — within-cluster rank**: Compute mean(D[Q22, Q_s]) for s ∈ sajda-set\{22}. Compute the same for each of the 14 surahs, ranking them ascending. Q 22's rank ∈ [1, 14].
   - PASS if rank > 7 (Q 22 in the LESS-cohesive half).

2. **T2 — permutation null (descriptive context)**: Sample 10,000 random "rank-of-target-among-14-members" under random 14-surah subsets and confirm the test has appropriate power. Not used for p-value; the test is a within-set rank comparison.

## Direction-of-effect lock

Predicted: Q 22 rank > 7 (upper half = less cohesive).
If Q 22 rank ≤ 7 (lower half = more cohesive), publish as NULL pre-commit violation — would suggest Q 22 is unexpectedly cohesive with the sajda-set, against H-NEW-1330's marker-thickness reasoning.

## Success criteria

- VINDICATED: rank > 7 (rank ∈ [8, 14]).
- BORDERLINE: rank = 7 (median; report as DIRECTIONAL).
- NULL: rank < 7 (Q 22 in cohesive half).

## Cross-references

- H-NEW-1330 sajda-cluster CONFIRMED-NULL (Q22 specialist confirms; Q53 specialist replicates).
- H-NEW-1331 sajda × muqaṭṭāʿat 1.97× over-representation PASS-DIRECTED — Q 22 is in the 7 NON-muqaṭṭāʿat sajda group, consistent with Q22's structural distance from the sajda-set's most-cohesive members.
- H-NEW-126 true-isolate-core {Q 16, 21, 22, 23, 25}: Q 22 already certified as instrument-immune.
- cross-finding-025 marker-thickness rule.

## Garden-of-forking-paths log

- BEFORE running: ranked the 14 sajda-surahs by mean FR-distance to other-13 because this is the natural within-set cohesion measure.
- BEFORE running: pre-committed direction = upper-half (rank > 7) because (a) Q 22 is a certified TRUE-ISOLATE in H-NEW-126, and (b) H-NEW-1331 places Q 22 in the 7 NON-muqaṭṭāʿat sajda subset which is structurally heterogeneous.
- BEFORE running: chose strict upper-half (>7) over weak upper-half (≥7) to lock direction sharply.

## Honest limits

- Single FR-roots instrument (H-NEW-111 baseline); same instrument as H-NEW-1330.
- Within-set rank is a 14-member ordering — limited resolution. Rank-7 vs rank-8 is a 1-position margin.
- The hypothesis is structurally tight: Q 22 has to be in 7 of 14 positions to PASS. By chance alone P(rank > 7) = 7/14 = 0.50; the prediction is informed by H-NEW-126 + H-NEW-1331, not arbitrary.

## Significance interpretation

Within-set rank alone has chance-baseline 0.50; this test is therefore a directional COMPLEMENT test of the H-NEW-1330 NULL, not an independent statistical-significance assertion. The verdict-statement will reflect this: VINDICATED means "the marker-thickness explanation is consistent with Q 22's specific position in the cluster," not "Q 22 is significantly less-cohesive than chance."
