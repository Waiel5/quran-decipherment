---
id: Q033-F-04
title: Q 33:72 (amāna verse) lexical distinctness test
date_locked: 2026-04-28
phase: B+
seed: 20260428
rules_tuple: (no-tashkeel, orthographic-token, words, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q033-F-04 — Q 33:72 amāna verse distinctness (PRE-REG)

## Hypothesis (locked direction)

Q 33:72 has a more lexically distinctive token-signature relative to surrounding Q 33 verses than the median Q 33 verse does.

Operationalized: define distinctness(v) = 1 − mean Jaccard(v, w) for w in Q33 \ {v}. Higher = more distinct. Hypothesis: distinctness(v.72) ranks in the top 10% of Q 33's 73 verses.

## Method

1. Load Q 33 verses (no-tashkeel).
2. For each verse v, compute distinctness(v) = 1 − mean_{w≠v} Jaccard(tokens(v), tokens(w)).
3. Rank Q 33 verses by distinctness; report rank of v.72.

## Locked direction

v.72 ranks ≤ 8 of 73 (top 11%).

## Success criteria

- VINDICATION: rank ≤ 8 of 73.
- FALSIFICATION: rank > 30 of 73.

## Bonferroni

k=1. α=0.05.

## Honest limits

Long verses tend to have more unique tokens, inflating distinctness. v.72 is reasonably long. We will report distinctness CONTROLLING FOR verse length (residual from a regression on word-count) as a secondary check.
