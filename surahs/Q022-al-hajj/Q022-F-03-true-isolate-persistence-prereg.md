---
test_id: Q022-F-03
title: "Q 22 true-isolate persistence under 8 alternative similarity metrics"
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 8
bonferroni_family: Q022-F-03-isolate-persistence
alpha_bon: 0.00625
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q022-al-hajj-specialist
---

# Q022-F-03 Pre-registration — Q 22 true-isolate persistence

## Hypothesis

H-NEW-126 identifies Q 22 as a member of the 5-surah TRUE-ISOLATE core {Q 16, 21, 22, 23, 25} — surahs immune to all 20 cluster-membership systems. Under Fisher-Rao on QAC roots (H-NEW-111), Q 22's mean distance to the rest of the corpus is 0.988 (slightly below corpus median 0.95).

If Q 22's isolation is robust, it should persist under DIFFERENT similarity instruments. Pre-committed: under each of 8 alternative metrics, Q 22's mean distance to its nearest 3 neighbors should rank in the **HIGHEST quartile** (≥86/114) — i.e. Q 22 is far even from its closest matches.

## Pre-committed prediction

**Direction-locked**: across 8 metrics, ≥6 of 8 (75%) place Q22's mean-distance-to-top-3-nearest in the top quartile (rank ≥86/114, i.e. higher distance than 75% of surahs).

## 8 metrics

1. M1: Fisher-Rao on QAC roots (H-NEW-111 baseline).
2. M2: Cosine on TF orthographic-token vectors (no tashkeel).
3. M3: Cosine on TF-IDF orthographic-token vectors.
4. M4: Jaccard on unique-token sets.
5. M5: Cosine on character-3-gram vectors (no-tashkeel).
6. M6: Cosine on character-4-gram vectors.
7. M7: Bhattacharyya on top-200 root frequency vectors.
8. M8: Cosine on final-letter (rhyme) distribution per surah (rules-tuple: min-tashkeel for rhyme).

Bonferroni-8 → α_bon = 0.05/8 = 0.00625.

## Per-metric test

For each metric, compute pairwise distance matrix among 114 surahs. Compute mean of Q 22's three smallest non-self distances. Compare against the same statistic for each of 113 other surahs. Q 22's rank ∈ [1,114]. PASS if rank ≥ 86 (top-quartile isolated).

## Aggregate test

Hits = number of metrics where Q22's mean-top-3-distance ranks ≥86.
- VINDICATED: hits ≥ 6 of 8.
- DIRECTIONAL: hits = 4-5 of 8.
- NULL: hits ≤ 3 of 8.

## Direction-of-effect lock

Predicted: hits ≥ 6/8.
If hits ≤ 3, the H-NEW-126 isolate-status is METRIC-SPECIFIC and should be flagged as such.

## Garden-of-forking-paths log

- BEFORE running: 8 metrics chosen for orthogonality (root vs surface vs n-gram vs rhyme).
- BEFORE running: nearest-3 chosen because: (a) top-1 is too noisy, (b) full-corpus mean is dominated by far-tail and thus not a good test of isolation, (c) top-3 captures "is the surah genuinely a neighbor of anyone."
- Coordination note: Q025-F-01 (Q025 specialist) leads cross-isolate persistence test on the {Q16,Q21,Q22,Q23,Q25} cluster. This Q022-F-03 is Q22-only and should NOT be conflated.

## Success criteria

- VINDICATED: ≥6/8 metrics show Q22 in top-quartile-isolation.
- DIRECTIONAL: 4-5/8.
- NULL: ≤3/8.
