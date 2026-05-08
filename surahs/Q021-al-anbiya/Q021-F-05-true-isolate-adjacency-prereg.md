---
surah: 21
test_id: Q021-F-05
title: True-isolate Q21+Q22 adjacent-pair joint structural test
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 2
bonferroni_family: Q021-F-05-isolate-adjacency-2-cells
alpha_bon: 0.025
direction: ⚠️ TWO-COMPONENT — direction-locked separately for each cell (see §4)
---

# Q021-F-05 — Pre-registration: Q 21 + Q 22 true-isolate joint adjacency

## 1. Hypothesis (locked)

The **true-isolate cluster {Q 16, 21, 22, 23, 25}** (per H-NEW-126) is "invisible to all 20 cluster-detection systems". Q 21 and Q 22 are the only **adjacent** pair within this cluster (Q 16 is isolated 5 positions before; Q 23 is adjacent to Q 22 but Q 22-Q 23 is also a within-isolate-cluster pair; Q 25 is 3 positions after Q 22). The Q 21–Q 22 adjacency is the project's first jointly-characterized true-isolate adjacent-pair.

⭐ **Test question**: Is the Q 21–Q 22 adjacency *structurally coherent* (low FR-distance + low TSP-cost) — suggesting genuine internal sub-structure within the true-isolate cluster — OR is it just two consecutive isolates that happen to be near each other in the mushaf?

**Hypothesis cells:**

- **Cell A — FR-distance**: Q 21–Q 22 pairwise Fisher-Rao distance is **LOWER** than the median pairwise FR-distance among the C(5,2)=10 within-cluster pairs of {Q 16, 21, 22, 23, 25}.
- **Cell B — TSP-cost**: Q 21–Q 22 canonical-adjacency TSP-cost (rank in H-NEW-720 distribution) is **HIGHER than median** — i.e., the Q 21–Q 22 transition is *expensive*, contradicting cell-A "structural coherence" if both were true.

**Joint interpretation**:
- Cell A passes AND Cell B fails (low-rank TSP-cost) → **STRUCTURAL-COHERENCE** verdict (the Q 21–Q 22 pair is genuinely a sub-cluster).
- Cell A passes AND Cell B passes (high TSP-cost) → **INCOHERENT** (FR-near but mushaf-expensive).
- Cell A fails AND Cell B passes → **NEAR-NEIGHBOR-BUT-NOT-CLUSTER** (Q 21–Q 22 are FR-distant despite mushaf-adjacent — classical isolated-pair).
- Cell A fails AND Cell B fails → **INDEPENDENT** (no joint structure).

## 2. Disclosure

The author has computed:
- Q 21–Q 22 TSP-cost = 0.1776, rank 16 / 113 (Cell B locked direction implies "above median = HIGHER").
- The author has NOT yet computed pairwise FR-distances among {Q 16, 21, 22, 23, 25}.

Direction for both cells is locked above. Cell A (FR-distance) is the genuinely-novel cell.

## 3. Operational definition

**Cell A** — Compute pairwise FR-distance among {Q 16, 21, 22, 23, 25} (C(5,2) = 10 pairs) using the same FR-roots pipeline as Q021-F-03 (top-K=500 STEM roots, Dirichlet-α=0.5, L1-normalize, Fisher-Rao). Test: rank of d(Q 21, Q 22) within the 10 within-cluster pairs.

**Cell B** — Use H-NEW-720 fraction_residual ranking. Q 21–Q 22 rank already known: 16 / 113 (top-15 expensive boundary, above corpus median rank 57 / 113).

## 4. Test statistic & direction

| Cell | Statistic | Locked direction |
|:--|:--|:--|
| A | rank of d(Q 21, Q 22) among 10 within-cluster pairs | < 5.5 (LOW: pre-committed to **structural-coherence**) |
| B | rank of TSP-cost in H-NEW-720 (1=most-expensive) | < 57 (HIGH-COST: pre-committed to **expensive-boundary**) |

**Already-observed B**: rank 16 / 113 → Cell B passes (HIGH-COST direction confirmed before pre-reg lock).

**Cell A is the locked-but-not-yet-observed test.**

## 5. Success / Failure criteria (Bonferroni k=2, α = 0.05/2 = 0.025)

- **Cell A pass**: rank ≤ 5 (within-cluster top-half nearer-pairs) AND rank-1 = top-MOST-similar pair → STRONG.
- **Cell A directional**: rank 5 or 6 (just-above-median).
- **Cell A fail**: rank 6+ (FR-distant within the cluster).

The 4-quadrant joint-interpretation in §1 is the headline reading.

## 6. Honest limits known a priori

- The 5-surah within-cluster sample (10 pairs) is small. Significance cannot be tested by a permutation null on 10 pairs alone; we report the rank descriptively.
- TSP-cost rank (cell B) is already-observed; the test is partly post-hoc on cell B. We MW-7 cap cell B at α=0.05 single-test (no Bonferroni penalty applied to cell B's already-observed result, but interpretation requires cell A to be the genuinely novel test).
- "Structural coherence" is operationalized as FR-roots-distance + TSP-cost combination. Other operationalizations (rhyme, content register, tafsir munāsaba) are not tested here. Q 21 + Q 22 is a multi-axis concept; Q021-F-05 covers the QAC-roots facet only.

## 7. Rules-tuple

`(QAC-v0.4-STEM-roots, top-K=500, Dirichlet-α=0.5, L1-normalize, Fisher-Rao, H-NEW-720-canonical-adjacency-rank)`.

## 8. SHA256 lock

To be computed at runtime by `scripts/Q021_F_05_isolate_adjacency.py`. Embedded in script and verified at execution.
