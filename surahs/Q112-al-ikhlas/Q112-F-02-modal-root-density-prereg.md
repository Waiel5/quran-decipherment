---
preregistration_id: Q112-F-02
title: Q 112 modal-root-density mechanism for FR-centroid status
date: 2026-04-28
phase: B+
seed: 20260428
status: PRE-REGISTERED-LOCKED
---

# Q112-F-02 — Pre-registration: Q 112 modal-root density

## Hypothesis (H1)

Q 112's root-distribution is heavily weighted toward corpus-modal roots — specifically: the fraction of Q 112's root-tokens that fall in the corpus's top-K most-frequent roots is **above the corpus mean** for K=20 and K=50 (multiple-comparison corrected).

This is the **mechanism hypothesis** for the FR-centroid result of Q112-F-01: the FR-centrality is hypothesized to be driven by Q 112's vocabulary being concentrated in the corpus-most-common roots.

## Null hypothesis (H0)

Q 112's modal-root-fraction is at-or-below the corpus mean. Under the null, Q 112's vocabulary is unrelated to the corpus modal distribution.

## Data

- `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` — QAC v0.4 morphology with ROOT annotations.

## Method

1. Compute corpus root-frequency table (across all 114 surahs).
2. Identify top-20 and top-50 most-frequent roots.
3. For each surah s, compute fraction_in_top_K(s) = #(s's root-tokens in top-K) / #(s's root-tokens).
4. Locate Q 112's rank.

## Direction

LOCKED: Q 112 modal-root-fraction expected ABOVE corpus median for both K=20 and K=50. Specifically, **Q 112 in top-20 of 114 by modal-root-fraction at K=20**.

## Success criteria

- Pass: Q 112 rank ≤ 20 / 114 by fraction_in_top_20.
- Bonferroni-corrected: family of 4 Q 112 tests, α = 0.0125. Rank ≤ 20 / 114 corresponds to p ≤ 20/114 = 0.175 — does NOT pass Bonferroni unless rank is much higher (rank ≤ 1.4 = top-1; equivalently top decile).
- Strict pass: rank ≤ 11 / 114 (passes α = 0.0125 under uniform null).

## Pre-commit honesty

If Q 112's modal-root-fraction is at or below corpus median, this is published as NULL with full prominence. The mechanism hypothesis would be falsified, but Q112-F-01's FR-centroid status would still stand (as an unexplained empirical fact requiring an alternative mechanism).
