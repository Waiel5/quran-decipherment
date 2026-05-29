---
surah: 2
surah_name: al-Baqara
file_type: pre-registration
test_id: Q002-F-08
date_registered: 2026-05-29
phase: B+
status: LOCKED-BEFORE-RUN
seed: 20260509
rules_tuple: (no-tashkeel, orthographic-token, whitespace-words, sajda-stripped, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q002-F-08 — Does al-Baqara MONOPOLISE the corpus's longest verses?

## Motivation

Q002-F-05 locked Q 2:282 as the rank-1 longest verse (z = +12.31). In its prose it
NOTED, without a pre-registered test, that Q 2 also holds several other top-50 long
verses. The deep-close-read brief (T4) asks a sharper, falsifiable question:

> Is Q 2 the ONLY surah holding 2-or-more of the corpus's TOP-10 longest verses?

This is a "monopoly" / concentration claim. It is the verse-length analogue of the
established al-sabʿ al-ṭiwāl content-class hypothesis: long legal/procedural verses
should cluster in the long Medinan surahs, and al-Baqara — the longest surah — should
dominate.

## Hypothesis (DIRECTION LOCKED)

**H1 (monopoly):** Q 2 is the ONLY surah among all 114 that holds ≥ 2 of the corpus
top-10 longest verses (by whitespace word count, no-tashkeel, sajda-stripped). LOCKED
DIRECTION: Q 2 holds ≥ 2 AND no other surah holds ≥ 2.

**H2 (plurality):** Even if H1 fails (other surahs also hold 2+), Q 2 holds the MOST
top-10 long verses of any surah (strict plurality). LOCKED DIRECTION: argmax = Q 2.

## Metric (MW-1 locked)

- Per-verse word count = len(whitespace_split(norm(text))), norm = collapse-whitespace
  + strip sajda/recitation marks, on `quran-text/quran-no-tashkeel.json`. Identical
  tokenisation to Q002-F-05's `_verse_words`.
- Rank all 6,236 verses descending by word count; ties broken by letter count then by
  (surah, verse) ascending. Take the top-10. Count how many fall in each surah.

## Null / significance

- This is a deterministic count, not a sampled statistic — no permutation null is
  meaningful for "is Q 2 the unique holder." The success criterion is the exact
  monopoly condition above.
- MW-2 robustness instead of a perm-null: re-run the top-N count for N ∈ {10, 15, 20}
  and report whether Q 2's plurality holds across all three (a deterministic
  sensitivity sweep). Primary claim is N = 10.

## Failure / NULL conditions

- If ANY surah other than Q 2 holds ≥ 2 of the top-10 → H1 NULL (monopoly FALSIFIED).
  This is published with full prominence as a pre-commit-honoured NULL.
- If some other surah holds ≥ as many top-10 verses as Q 2 → H2 NULL too.

## MW protections

- MW-1: tokenisation + ranking rule locked pre-run.
- MW-3: alternative metric — repeat the whole count by LETTER count (not word count)
  as a second top-10 definition; report whether the monopoly/plurality verdict is
  rules-tuple-stable across word-count vs letter-count.
- MW-7: any threshold (e.g. "top-12 instead of top-10") noticed after the run carries
  α = 0.05 single-test ceiling and is flagged RULES-TUPLE-FRAGILE.

## Honesty note

If the strict monopoly (H1) fails because Q 4 / Q 24 also hold 2 of the top-10, the
honest refined finding is "Q 2 is the ONLY surah holding 3+ of the top-10" (if true),
reported under MW-7 as a post-hoc refinement, not as the pre-registered claim.
