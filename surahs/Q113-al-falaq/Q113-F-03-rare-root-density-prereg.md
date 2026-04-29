---
preregistration_id: Q113-F-03
title: Q 113 corpus-rare-root density (lexical-typology marker)
date: 2026-04-28
phase: B+
seed: 20260428
status: PRE-REGISTERED-LOCKED
---

# Q113-F-03 — Pre-registration: Q 113 corpus-rare root density

## Hypothesis (H1)

Q 113's 4-evil typology entries (vv.2-5) are each marked by a corpus-rare root (low-frequency in QAC v0.4). Quantitatively: the fraction of Q 113's distinct roots that are **corpus-rare** (≤5 attestations across all 114 surahs) is **above** the corpus mean for short surahs (≤10 verses).

## Method

1. From `data/morphology/quranic-corpus-morphology-0.4.txt`, compute root-frequency table.
2. Define "corpus-rare" = root with ≤5 total attestations.
3. For each surah s with n_verses ≤ 10, compute fraction_rare(s) = (# distinct rare roots in s) / (# distinct roots in s).
4. Rank Q 113.

## Direction

LOCKED: Q 113 fraction_rare ≥ 90th percentile among short surahs (n ≤ 10 verses).

## Pre-commit honesty

If Q 113 is below 90th percentile, NULL.
