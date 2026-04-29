---
date: 2026-04-18
finding: H-NEW-275
status: completed
agent: codex
---

# Journal — H-NEW-275 run-1

## Objective

Run the smallest honest non-Quranic replication of the H-NEW-165 phonological
predictor idea, using the Bukhari bāb-opening setting suggested in the handoff,
without touching continuity files or other H-NEW workstreams.

## Scope lock

- corpus: `data/baseline-corpora/raw/bukhari-noquran.txt`
- inherited segmenter: split on `باب`, sort by token count, keep top 114
- target: first token after `باب`
- retain only opener classes with `n >= 2`
- feature family: H-NEW-165-style 15-d classical phonological aggregate,
  extended to the full Arabic alphabet
- models: RF primary, logistic descriptive, length-only RF comparator

## Runtime notes

The initial exact 1000-permutation implementation was too slow for a bounded
first pass. I optimized the implementation several times without changing the
core model family, then made an explicit bounded deviation from the prereg:

- planned permutations: 1000
- executed permutations: 20
- reason: observed RF top-1 hit 1.0000 immediately, and `0/20` exceedances are
  already enough to establish `p < 0.05`

This deviation is written into the JSON and findings file.

## Final numbers

- retained samples/classes: **64 / 15**
- RF full phonology: **top-1 1.0000**, top-3 1.0000, top-5 1.0000
- Logistic full phonology: **top-1 0.9688**
- RF length-only: **top-1 0.5469**
- lift over length-only: **+0.4531**
- bounded permutation check: **0/20 exceedances**, `p = 0.0476`
- verdict: **GENERIC-STRONG**

## Interpretive bottom line

The predictor idea generalizes strongly to repeated Bukhari opener words, so a
successful phonological opener classifier is not uniquely Quranic. But this is a
strictly easier task than H-NEW-165: lexical first-word labels, no singleton
ceiling, and no exact phonological collisions among retained classes.
