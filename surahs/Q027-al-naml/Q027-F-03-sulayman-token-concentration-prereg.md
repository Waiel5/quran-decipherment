---
finding_id: Q027-F-03
title: Sulaymān-token concentration in Q 27 vs corpus
date_preregistered: 2026-04-28
phase: B+
---

# Q027-F-03 — Sulaymān-token concentration

## Hypothesis
Q 27 carries the largest share of orthographic *Sulaymān* attestations (`سليمان` and any allographic variant) of any surah in the Quran, BUT the concentration is LOWER than the *yūsuf* concentration in Q 12 (Q012-F-03, 92.6%). Sulaymān is named in 7 surahs (Q 2, 4, 6, 21, 27, 34, 38), so cross-surah dispersal is structurally guaranteed.

## Null distribution
Permutation null: under H0, *Sulaymān*-tokens distribute proportional to per-surah token-length. 10000 multinomial permutations, seed 42.

## Direction (LOCKED before observation)
- max-surah for *Sulaymān* attestations is Q 27 (one-sided rank test).
- Q 27 concentration > "uniform-by-length" expectation (one-sided).
- Q 27 concentration < 0.92 (declared lower bound, distinguishing it from Yūsuf).

## Test statistic
`q27_share` = (# Sulaymān-tokens in Q 27) / (# Sulaymān-tokens corpus-wide).

## Bonferroni
α_corrected = 0.0125 (k=4 in this investigation family).

## Success criteria
- Q 27 has the maximum surah count of *Sulaymān* attestations.
- p_perm(q27_share >= observed) < 0.0125.

## Rules tuple
`(no-tashkeel, orthographic-exact-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Match string: any token containing the substring `سليمان` or `سليمن`.

## Anti-hallucination
- Corpus file: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
