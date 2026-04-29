---
id: Q033-F-03
title: ḥijāb-passage internal-cohesion test (vv. 28-34, 53, 59)
date_locked: 2026-04-28
phase: B+
seed: 20260428
rules_tuple: (no-tashkeel, orthographic-token, words, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q033-F-03 — ḥijāb-passage internal cohesion (PRE-REG)

## Hypothesis (locked direction)

The ḥijāb-cluster verses (vv. 28-34, 53, 59) are MORE lexically cohesive among themselves than a random size-matched sample of Q 33 verses.

## Method

1. Identify ḥijāb-cluster set: V_HIJAB = {28, 29, 30, 31, 32, 33, 34, 53, 59} (n=9).
2. For each verse, compute its multiset of orthographic tokens.
3. Define pairwise lexical-cohesion: Jaccard similarity of token sets between two verses.
4. Cohesion(V) = mean of pairwise Jaccard for all C(|V|,2) pairs.
5. Observed cohesion: cohesion(V_HIJAB).
6. NULL: 10000 random size-9 samples of verses from Q 33. Permutation p-value = fraction with cohesion ≥ observed.

## Locked direction

V_HIJAB cohesion > random-sample cohesion (right-tailed test).

## Success criteria

- VINDICATION: permutation p < 0.05.
- FALSIFICATION: p > 0.50 (random-or-worse).
- NULL/RULES-TUPLE-FRAGILE: 0.05 < p < 0.50.

## Honest limits

Token-set Jaccard is a coarse cohesion measure; common Quranic tokens (Allāh, kāna, etc.) inflate Jaccard. We will report TF-IDF-weighted Jaccard as a secondary check.

## Bonferroni

k=1 (single test family). α=0.05.
