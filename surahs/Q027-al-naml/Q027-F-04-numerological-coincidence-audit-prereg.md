---
finding_id: Q027-F-04
title: Q 1 ↔ Q 27 number-coincidence audit (rigorous null-test)
date_preregistered: 2026-04-28
phase: B+
---

# Q027-F-04 — Numerological-coincidence audit, Q 1 ↔ Q 27

## Background
Popular numerology around the second basmala includes claims such as:
- "Q 1 has the basmala as v.1, Q 27 has the basmala as v.30: 30 − 1 = 29 = Q 1's word-count."
- "Sum 1 + 27 = 28 = something."
- "Q 27 is the 27th surah; basmala appears in v. 30; Q 27 has 93 verses."
The user's prompt explicitly directs: "verify all numerical claims rigorously with rules-tuple discipline."

## Hypothesis (NULL-default, falsificationist)
Numerical "coincidences" between Q 1 and Q 27 along basmala-axis are NULL once subjected to permutation testing on the family of plausible coincidence patterns.

## Direction (LOCKED before observation)
- The relevant "coincidence" relations (subtraction/addition/equality with verse-counts, word-counts, or surah-numbers) — when subjected to a 10000-permutation null over alternative pairings — are statistically un-distinguished from random.

## Test family (pre-committed; do NOT enlarge post-observation)
For Q 1 (7 verses, includes basmala as v.1, word-count W_1) and Q 27 (93 verses, includes basmala as v.30, word-count W_27):

1. **C1**: Does (v_basmala_in_Q27 − v_basmala_in_Q1) = W_1 hold? (i.e., does 30 − 1 = 29 = W_1?)
2. **C2**: Does (Q_index_27 + Q_index_1) = W_1 + 1 hold? (i.e., 28 = 29?)
3. **C3**: Does (v_basmala_in_Q27 − Q_index_27) = some integer of Q 1 properties?
4. **C4**: Does Q 27's verse count (93) divide / relate to 19 (Code-19), 7, 28, or 114?

## Method
- All numbers computed from disk (no-tashkeel for word-count, Hafs-Kufan verse-counts).
- For C1–C3: deterministic check — TRUE/FALSE.
- For C4: permutation over the corpus' 114 verse-counts: how often does a random surah's verse-count satisfy similar relations?
- Bonferroni α_corrected = 0.05 / 4 = 0.0125 across coincidence-tests within this family; PLUS k=4 novel tests in the surah → final α = 0.05 / 16 = 0.003125 if applied to the full investigation family. We apply the surah-investigation family α = 0.0125 here, and within-test family α = 0.0125, so all coincidence checks must pass at p < 0.0125.

## Success criteria (LOCKED)
A "coincidence" is declared CONFIRMED only if BOTH:
- The relation is deterministically true, AND
- A permutation null demonstrates the relation is unlikely under H0 (p < 0.0125).
A relation that is true but reproduces ≥ 1.25% of permuted outcomes is FALSIFIED-AS-NUMEROLOGY.

## Failure criteria
- ≥ 1 of C1–C4 true and null-significant → DIRECTIONAL (further work).
- All 4 NULL → CONFIRMED-NULL on the popular numerology, in the spirit of MASTER-FINDINGS-LEDGER's prior rejections of Code-19 and 6236/114 numerology.

## Anti-hallucination
- Verse-counts: `/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv` (cross-checked vs JSON).
- Word-counts: computed from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
- Q 1:1 = basmala (v.1, by Hafs-Kufan tradition).
- Q 27:30 location confirmed in three tashkeel variants.
