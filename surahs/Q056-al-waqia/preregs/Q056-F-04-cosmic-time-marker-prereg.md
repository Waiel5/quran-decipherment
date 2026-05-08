---
test_id: Q056-F-04
title: Cosmic-time-marker density — Q 56 vs Q 53 (al-Najm), Q 85 (al-Burūj), corpus baseline
date: 2026-05-07
phase: B+
status: PRE-REGISTERED
investigator: Q056-al-waqia-specialist
seed: 20260507
n_perm: 0
bonferroni_k: 1
bonferroni_family: Q056-F-04-cosmic-density
alpha_bon: 0.05
direction: Locked: Q 56 is in TOP-5 surahs by cosmic-time-marker density (count per 100 words)
acceptance: Q 56's rank in top-5 (rank ≤ 5 of 114)
failure: Q 56 rank > 5
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q056-F-04 Pre-Registration — Cosmic-time-marker density

## Hypothesis

Q 56 contains the famous *fa-lā uqsimu bi-mawāqiʿ al-nujūm* (Q 56:75) cluster. Pre-commit: the cosmic-time-marker token-set:

`COSMIC = {النجم, النجوم, نجم, نجوم, موقع, مواقع, الشمس, شمس, القمر, قمر, الفلك, فلك, البروج, برج}`

— gives Q 56 a top-5 density (count per 100 words) among 114 surahs.

## Method

1. For each surah, count occurrences of any token in COSMIC.
2. Compute density = count / total_words × 100.
3. Rank Q 56.

## Acceptance / failure

- Q 56 rank ≤ 5: VINDICATED
- Q 56 rank > 5: NULL

Honest expectation: Q 53 al-Najm ("the star"), Q 85 al-Burūj ("the constellations"), and possibly Q 91 al-Shams will outrank Q 56 because their NAMES are cosmic markers and they are short surahs (denominator effect). The pre-commit is whether Q 56 — despite being long — STILL achieves top-5.
