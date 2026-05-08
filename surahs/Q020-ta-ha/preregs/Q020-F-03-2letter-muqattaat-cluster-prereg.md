---
finding_id: Q020-F-03
title: Two-letter muqaṭṭaʿ trio (Q20 ṬH, Q27 ṬS, Q36 YS) joint multi-axis cluster test
date: 2026-05-07
seed: 20260507
phase: B+
specialist: Q020-ta-ha-specialist
bonferroni_k: 4
bonferroni_family: "{FR-distance trio cohesion} + {sig_A spread tightness} + {top-rhyme-letter consensus} + {mean_d corpus-rank consensus}"
alpha_bon: 0.0125
direction_locked: trio is empirically tighter than random-3 baseline on AT LEAST 2 of 4 axes
status: PRE-REGISTERED
---

# Q020-F-03 — 2-letter muqaṭṭaʿ trio joint cluster test

## Hypothesis (direction-locked)

The three two-letter muqaṭṭaʿ surahs Q 20 (طه), Q 27 (طس), Q 36 (يس) form a multi-axis cluster TIGHTER than a random-3 baseline on at LEAST 2 of 4 axes.

Axes:
1. **FR-distance**: trio mean intra-distance (3 pairs) ≤ random-3 baseline 5th percentile.
2. **sig_A spread**: trio sig_A range (max-min) ≤ random-3 baseline 5th percentile.
3. **Top-rhyme-letter consensus**: ≥ 2 of 3 share top final letter (binary; tested vs {trio randomly drawn agree 2/3}).
4. **mean_d corpus-rank consensus**: trio mean of `mean_content_distance` ranks within 1 SD of trio centroid (tightness).

## Pre-committed thresholds

- **PASS (≥2 of 4)**: CONFIRMED.
- **DIRECTIONAL (1 of 4)**: 2-letter trio is empirically a sub-cluster on ONE axis only.
- **NULL (0 of 4)**: 2-letter family is letter-only-without-multi-axis content/rhyme/sig signature, consistent with H-NEW-610 muqaṭṭaʿāt content-orthogonality (al-Suyūṭī epistemic humility VINDICATED at the 2-letter sub-level).

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.
H-NEW-111 (FR), H-NEW-750 (sig_A, rhyme-top, mean_d) values used as-is from disk.

## Null model

10000 random-3 surah samples from {1..114}; for each, compute the 4 axis statistics; tabulate baselines. Permutation seed 20260507.

## Honest limits

- N=3 trio; tests have low power.
- Q 36 YS may differ structurally from Q 20+Q 27 due to YS being part of the YS-only family vs ṬS/ṬH sharing ṭāʾ.
- The pre-reg specifies "≥2 of 4" up-front, not Bonferroni-strict-all-4; the trio is small and the test is a JOINT cluster claim, so partial-axis support is informative.
