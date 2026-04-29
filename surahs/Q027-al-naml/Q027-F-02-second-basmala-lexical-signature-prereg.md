---
finding_id: Q027-F-02
title: Q 27:30 (second basmala) lexical-signature audit vs Q 1:1 basmala
date_preregistered: 2026-04-28
phase: B+
---

# Q027-F-02 — The second basmala (Q 27:30) — lexical signature audit

## Background
Q 27:30 is the ONLY verse outside surah-openings that contains the entire phrase *bismi llāhi al-raḥmāni al-raḥīm*. The verse reads:

*innahu min sulaymāna wa-innahu bismi llāhi al-raḥmāni al-raḥīm*

This raises a structurally meaningful question: is the basmala-phrase in Q 27:30 lexically isomorphic to Q 1:1 (the formal basmala), or does it differ by even a single token under the no-tashkeel orthographic rule-tuple?

## Hypothesis
The basmala-phrase substring inside Q 27:30 (defined as tokens from `بسم` to `الرحيم`) matches Q 1:1 token-for-token under (no-tashkeel, orthographic).

## Direction (LOCKED before observation)
Token-set, token-multiset, AND token-sequence between the two slices match exactly.

## Test statistic
- Q1_tokens = orthographic tokens of Q 1:1.
- Q27_30_basmala_slice = orthographic tokens of Q 27:30 from `بسم` onwards.
- match_exact = (Q1_tokens == Q27_30_basmala_slice).
- Levenshtein on token-sequences (0 if exact).

## Method
1. Load Q 1:1 from no-tashkeel JSON.
2. Load Q 27:30 from no-tashkeel JSON.
3. Tokenize both (whitespace, strip pause markers).
4. Locate `بسم` in Q 27:30; take from there to end.
5. Compare.

## Cross-validate
Repeat the same comparison under min-tashkeel and full-tashkeel JSON. If diacritics diverge between Q 1:1 and Q 27:30, document the divergence.

## Success criteria (descriptive — NO p-value test)
This is a deterministic existence check, not a probabilistic test. Result is CONFIRMED if exact match, DIVERGENT if not, with documentation of any divergence.

## Anti-hallucination
- Corpus file (no-tashkeel): `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Cross-validate (min-tashkeel): `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json`
- Cross-validate (full-tashkeel): `/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json`
