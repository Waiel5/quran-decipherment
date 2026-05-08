---
test_id: Q056-F-02
title: Sābiqūn-block (Q 56:10-26) vocabulary uniqueness — corpus-rare paradise-vocabulary count
date: 2026-05-07
phase: B+
status: PRE-REGISTERED
investigator: Q056-al-waqia-specialist
seed: 20260507
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q056-F-02-sabiqun-vocab
alpha_bon: 0.05
direction: Locked: count of "rare-or-hapax-in-paradise-context" tokens in vv 10-26 ≥ 3
acceptance: ≥ 3 tokens with corpus_count ≤ 5 AND tokens are content-words (not function words)
failure: < 3 tokens meet criteria
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q056-F-02 Pre-Registration — Sābiqūn vocabulary uniqueness

## Hypothesis

The Sābiqūn paradise-description (vv 10-26) contains specific lexical items that are HAPAX-RARE in the Quran corpus. Pre-committed: ≥ 3 content-word tokens with corpus-frequency ≤ 5.

## Method

1. Extract all orthographic tokens (no-tashkeel) from Q 56:10-26.
2. Filter: keep only tokens of length ≥ 4 graphemes (excludes function words like *fī*, *min*, *lā*, *wa-*, *ʿalā*).
3. For each token, count corpus-wide occurrences (case-insensitive, no-tashkeel).
4. Count tokens with corpus_count ≤ 5.

## Pre-committed enumeration of candidates

The user-seed identified: *muqarrabūn*, *surur mawḍūnah*, *mawḍūnah*, *ḥūr ʿīn*, *akwāb*, *mawḍūʿah*, *ladayhim*. Test will count rarity over the full vocabulary of vv 10-26, not pre-filter.

## Acceptance / failure

- ≥ 3 tokens with corpus_count ≤ 5: VINDICATED
- < 3 tokens with corpus_count ≤ 5: NULL (Sābiqūn vocabulary is corpus-typical)

## Rules-tuple

Primary: no-tashkeel orthographic tokens. Re-run on min-tashkeel orthographic forms — must agree.
