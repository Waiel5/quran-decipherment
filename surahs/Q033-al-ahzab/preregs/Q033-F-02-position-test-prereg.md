---
id: Q033-F-02
title: Q 33:40 (khātam al-nabiyyīn) structural-midpoint position test
date_locked: 2026-04-28
phase: B+
seed: 20260428
rules_tuple: (no-tashkeel, orthographic-token, words, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q033-F-02 — Q 33:40 position test (PRE-REG)

## Hypothesis (locked direction)

Q 33:40 (the *khātam al-nabiyyīn* verse) is at or near the structural midpoint of Q 33.
Operationalized: the cumulative word-count up to and including v.40, divided by the total word-count of Q 33, is ≈ 0.5 (closer than ±0.10).

Verse-index midpoint is 40/73 = 0.548 — already near-middle.
We test the stricter word-count midpoint claim.

## Method

1. Load `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
2. For Q 33: compute cumulative word-count after each verse.
3. Compute word_midpoint_position(v.40) = cum_words(40) / total_words(Q33).
4. Compare to 0.5.

## Null distribution

- Permutation: shuffle the 73 verse word-counts 10000 times; for each shuffled ordering, compute the cumulative-word-position of the verse-token that holds the original v.40 (i.e., v.40's word-count value placed at position 40 in shuffled order). Record fraction of permutations with cum_pos closer to 0.5 than observed. *Wait — that's not the right null*.
- Better null: under what fraction of (i, n)=(40, 73) random verse-length distributions on Q 33 length, does cum_pos(40) fall within ±0.05 of 0.5?
- We'll use a simpler position-test: compute cum_pos for ALL 73 verses; the question is which verses fall within ±0.05 of midpoint. Report rank of v.40's |cum_pos − 0.5|.

## Success criteria

- DIRECTIONAL VINDICATION: |cum_pos(v.40) − 0.5| < 0.05 (i.e., within 5pp of word-midpoint).
- TIE-RANK: rank of |cum_pos − 0.5| ≤ 5 among 73 verses.
- FALSIFICATION: |cum_pos(v.40) − 0.5| > 0.10 (more than 10pp off midpoint).

## Honest limits

This is a post-hoc structural test. The classical *khātam al-nabiyyīn* claim is theological, not structural. We are merely asking: does v.40 sit at a quantitative-architectural focal-point?

## Bonferroni

k=1 family — α=0.05. We are NOT testing a multi-comparison family here (just one verse's position).
