---
finding_id: Q082-F-02
title: Q 82-Q 84 architectural CORE-pair cohesion + Q 81→82, Q 82→83, Q 83→84, Q 84→85 CORE-glue analysis
phase: B+
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 4
alpha_bon: 0.0125
script: surahs/Q082-al-infitar/scripts/Q082_F_02_core_glue.py
parent_findings: H-NEW-1200, H-NEW-720
---

# Q082-F-02 — H-NEW-1200 CORE-pair cohesion + 4-transition CORE-glue analysis

## Hypothesis

H1 (CORE-pair cohesion): Q 82-Q 84 is one of the 4 architectural CORE pairs in H-NEW-1200 Sub-cluster A (the 4 idhā-cosmic-event short-Meccan opener surahs {Q 81, 82, 84, 99}). Within the 4-CORE, all 6 pairwise FR distances are below the corpus-wide pairwise FR percentile (loose threshold: each pair below 50th percentile).

H2 (CORE-glue, mushaf adjacencies):
- Q 81→82, Q 82→83, Q 83→84, Q 84→85: each is below the median TSP-residual cost for canonical adjacencies (median ≈ 0.06 in H-NEW-720).
- The 4-transition mean cost is below the random-pair mean by at least 2 standard deviations.

H3 (Sub-cluster A consistency): Q 82 mean distance to {Q 81, Q 84, Q 99} below Q 82 mean distance to all other 110 surahs.

## Direction (LOCKED before observation)

- Each of the 6 4-CORE pairwise FR distances < corpus pairwise FR median (≈ 0.92).
- Each of the 4 mushaf-transitions < median per-adjacency cost (≈ 0.06 per H-NEW-720 stats).
- Q 82 mean dist to 4-CORE − {Q 82} = 3 surahs < Q 82 mean dist to corpus.

Counter-direction (any test reverses) = NULL on that cell.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

FR distances from H-NEW-111 frozen JSON (root-distribution Fisher-Rao on top-300 root frequency vectors per surah).

## Operationalization

(a) Load H-NEW-111 D_matrix_upper_triangular into pairwise FR dict.
(b) Compute 6 4-CORE pairs: (81,82), (81,84), (81,99), (82,84), (82,99), (84,99); compare each to corpus median pairwise FR.
(c) Compute Q 81→82, 82→83, 83→84, 84→85 from H-NEW-720; compare to per-adjacency median (~0.06).
(d) Compute Q 82 mean dist to {Q 81, Q 84, Q 99} versus Q 82 mean dist to all-other-110.
(e) Permutation null: shuffle 4-CORE labels across 100 random 4-surah subsets matched on length (verses ±25%), compute the mean intra-cluster FR; compare observed Q {81,82,84,99} mean to null.

## Success criteria

- 6/6 pairs below corpus pairwise FR median: CORE-PAIR-CONFIRMED
- 4/4 transitions below H-NEW-720 per-adjacency median: CORE-GLUE-CONFIRMED
- 4-CORE perm-test p < 0.05: SUB-CLUSTER-A-CORE-CONFIRMED

## Failure conditions

- Any of the 6 4-CORE pairs above corpus-median.
- Any of the 4 transitions above per-adjacency median.
- 4-CORE perm p > 0.05.

## Pre-commit honesty

If a transition is above median or a pair is above corpus-median, publish that as PARTIAL/NULL on the relevant cell.

## Connection to existing findings

H-NEW-1200 already CONFIRMED the 14-cluster eschatology meta-cluster (p=0.00030). The 4-CORE = Sub-cluster A SHORT idhā-opener architectural class (Q 56 excluded from the 4-CORE due to its mid-Meccan length 96 verses). This pre-reg formally tests the 4-CORE as a coherent architectural unit AND its mushaf-glue (Q 81→82, 82→83, 83→84, 84→85) — extending H-NEW-720 with a CORE-targeted lens.
