---
finding_id: Q010-F-02
title: ALR-cluster Fisher-Rao cohesion test — Q 10 within {Q 10, 11, 12, 14, 15}
date_locked: 2026-04-28
seed: 1042899
rules_tuple: (no-tashkeel, orthographic-token, QAC-stem-roots, Hafs-Kufan, Mashriqi)
---

# Q010-F-02 — ALR-cluster Fisher-Rao cohesion

## Hypothesis (DIRECTION-LOCKED)
The 5 ALR-marked surahs {Q 10, 11, 12, 14, 15} form a content-cohesive cluster in Fisher-Rao distance space — i.e., mean intra-cluster pairwise distance is **strictly lower** than mean cross-cluster (random-5) distance.

Sub-hypothesis: Q 10's mean pairwise distance to ALR-cluster siblings ≤ Q 10's mean to random non-ALR surahs.

## Data
- Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (114×114 FR matrix on QAC stem-roots).

## Test
1. Compute mean pairwise FR distance within ALR-5 (10 pairs).
2. Generate 10000 random samples of size-5 surah sets (excluding any element of ALR-5).
3. Permutation p = fraction of random size-5 sets with smaller mean than ALR-5.
4. CONFIRMED if perm-p ≤ 0.05 AND ALR-mean is strictly less than overall corpus mean.
5. NULL if perm-p > 0.05 OR direction is reversed.
6. Per-surah analog: rank Q 10's mean-distance-to-ALR-siblings against its mean-distance-to-(rest-of-corpus).

## Bonferroni
Two tests in family (ALR-mean test + Q 10 sub-test); α_corrected = 0.05/2 = 0.025.

## Replication
- H-NEW-600 already FALSIFIED whole-surah ALR-5 cohesion at 56.25%ile (i.e., NULL — but at the corpus-FR-cohesion test, not pairwise FR).
- This test is a NARROWER pairwise-FR variant: pairwise-mean instead of cluster-cohesion.

## Pre-committed expectation
NULL is the most-likely outcome given H-NEW-600. The pre-commit direction is "intra < cross" — if this test reproduces NULL, that is published with full prominence. It strengthens the H-NEW-600 finding that ALR is a NAME-CLASS cluster (per H-NEW-97) NOT a content-cluster.

## Honest expectation under prior empirical evidence
The prior strongly suggests ALR-cluster intra-mean ≈ corpus mean — i.e., NULL. We pre-commit to publishing this NULL with the same prominence as a confirmation.
