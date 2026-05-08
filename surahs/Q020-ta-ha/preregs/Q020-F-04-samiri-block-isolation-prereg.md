---
finding_id: Q020-F-04
title: Sāmirī episode (Q 20:85-98) lexical isolation within Q 20
date: 2026-05-07
seed: 20260507
phase: B+
specialist: Q020-ta-ha-specialist
bonferroni_k: 1
bonferroni_family: "Q020-Samiri-block (single test, in-surah window cosine null)"
alpha_bon: 0.05
direction_locked: greater (Sāmirī-block cosine-distance to surah-mean-vector > MEAN of cosine-distances of all other 14-verse contiguous windows in Q 20)
status: PRE-REGISTERED
---

# Q020-F-04 — Sāmirī episode lexical isolation

## Hypothesis (direction-locked)

The Sāmirī-episode contiguous block Q 20:85-98 (14 verses) has cosine-distance to the Q 20 surah-mean-vector that is GREATER than the mean cosine-distance of all 14-verse contiguous windows within Q 20.

Operationalization: word-token TF vector per window (no-tashkeel orthographic). Surah-mean = mean of all 14-verse-window TF vectors. Cosine distance = 1 − (window·surah_mean / (||window||·||surah_mean||)).

## Pre-committed thresholds

- **PASS (CONFIRMED)**: Sāmirī block (window starting v.85) is in the TOP-3 most-distant 14-verse windows of Q 20 (i.e. rank ≤ 3 of (135-14+1)=122 candidate windows), AND permutation p ≤ 0.05.
- **DIRECTIONAL**: rank 4-12 (top decile) AND p > 0.05.
- **NULL**: rank > 12.

## Null model

Permutation null: shuffle Q 20 verse-token lists 10000 times; recompute the 14-verse-window cosine distances; recompute the rank of the v.85-98 window position. Seed 20260507.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## Honest limits

- The Sāmirī-block boundary (v.85-98) is per al-Ṭabarī / Ibn Kathīr classical division. A 13-verse or 15-verse block would shift the window slightly; the 14-verse selection is locked.
- Cosine-distance is one similarity metric; FR (probability vectors) and char-n-gram NCD might differ.
- Surah-mean as reference is one choice; alternative is global Quran-mean. We use surah-mean to test in-surah isolation specifically.
