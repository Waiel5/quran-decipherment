---
test_id: Q022-F-05
title: "Q21-Q22-Q23 true-isolate triplet cohesion under FR-roots"
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q022-F-05-isolate-triplet
alpha_bon: 0.05
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q022-al-hajj-specialist
---

# Q022-F-05 Pre-registration — Q21-Q22-Q23 isolate-triplet cohesion

## Hypothesis

Q 21, Q 22, Q 23 are three consecutive members of the H-NEW-126 true-isolate core {Q 16, 21, 22, 23, 25}. Each is "abstract-argumentative discourse" (per H-NEW-126 / cross-finding-026 §13), concept/object-named, and immune to all 20 cluster systems. By construction, true-isolates should NOT exhibit cluster-cohesion — that's what makes them isolates.

## Pre-committed prediction

**Direction-locked**: the joint cohesion of the {Q21, Q22, Q23} triplet (mean pairwise FR-distance among the 3) should be **NOT enriched** vs the distribution of all 112 consecutive triplets in the mushaf. Specifically:

- Predicted direction: triplet's mean FR-distance is NEAR-MEDIAN (between 25th and 75th percentile) — neither significantly tighter nor looser than chance.
- Falsification: if the triplet is in the BOTTOM-quartile (rank ≤ 28), this is a discovery of hidden inter-isolate cohesion (positive surprise). If in TOP-quartile (rank ≥ 84), this confirms the isolate-by-construction null but is the predicted direction.

## Test

1. Compute `D` = 114×114 FR-roots distance matrix from H-NEW-111.
2. For all consecutive triplets (s, s+1, s+2) where s ∈ [1, 112], compute `T(s) = mean(D[s,s+1], D[s,s+2], D[s+1,s+2])`.
3. Locate target T(21) for triplet {Q21, Q22, Q23}.
4. Compute target's rank among 112 triplets.
5. Permutation null (sanity): random-triplet means under 10000 random index-permutation samples.

## Direction-of-effect lock

Predicted regions:
- **NEAR-MEDIAN (25th-75th %ile)** = pre-committed default — confirms "isolate-without-mutual-cohesion."
- **TOP-quartile (≥75th %ile, high distance)** = consistent with stronger isolate framing (isolates are FAR even from each other).
- **BOTTOM-quartile (<25th %ile, low distance)** = SURPRISE = hidden inter-isolate cohesion = enriched-cluster-discovery.

The predicted direction = **NOT BOTTOM quartile**.

## Success criteria

- DEFAULT-VINDICATED (no surprise): T(21) in [25th, 100th] %ile of triplet distribution → confirms isolate behavior.
- NULL-WITH-SURPRISE: T(21) < 25th %ile → triplet IS unexpectedly cohesive → surprise finding, single-test α=0.05 cap (post-hoc would be needed for an independent confirmation).

## Coordination note

Q021-F-05 separately tests Q21+Q22 dyad. This Q022-F-05 extends to Q21+Q22+Q23 triplet. Different unit of analysis (3 instead of 2). NOT a duplicate.

## Garden-of-forking-paths log

- BEFORE running: 112 consecutive triplets is the natural null universe — every position s∈[1,112] yields a triplet.
- BEFORE running: mean of 3 pairwise distances chosen over alternatives (max, min) because mean is the natural cohesion statistic; max would test "outlier-pair" instead.
- BEFORE running: FR-roots is the project-default (H-NEW-111). A single instrument is sufficient because the prediction is direction-locked AND the result will be cross-checked by Q022-F-03 (8-metric persistence) which targets isolation, not cohesion.
