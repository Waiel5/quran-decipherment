---
finding_id: Q010-F-01
title: Yūnus token concentration in Q 10 — eponymous-name density
date_locked: 2026-04-28
seed: 1042898
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q010-F-01 — Yūnus-token concentration in Q 10

## Hypothesis (DIRECTION-LOCKED)
The token *yūnus* (يونس) — the prophet's name and the surah's name — is concentrated in Q 10 vs the rest of the corpus. Direction: **Q 10 contains a strictly larger fraction of total *yūnus* tokens than expected under uniform distribution by word-count.**

## Data
- Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Tokenisation: whitespace-split; orthographic equality after stripping non-Arabic-letter characters.
- Target token: exact orthographic form `يونس`.

## Test
1. Count total occurrences of token `يونس` across the 114 surahs.
2. Count occurrences in Q 10 specifically.
3. Compute concentration = q10_count / total_count.
4. Expected baseline under uniform-by-word-count = q10_words / total_words.
5. Verdict CONFIRMED if concentration > 1.5× expected baseline AND total_count >= 2.

## Comparison
Compare to the pre-existing Q012-F-03 finding: *yūsuf* token has 92.6% concentration in Q 12.

## Falsification
NULL if Q 10 concentration ≤ baseline; or if total_count = 0 (impossibility — name appears at least once at Q 10:98).

## Pre-registered limits
- This is a token-equality test under no-tashkeel, orthographic-token. Different rules-tuples (e.g., morphological lemma counting all forms) may produce different results.
- The token's rarity in Q 10 itself would be a striking finding (the surah named after a prophet whose name barely appears).

## Honest expectation
Eyeballing prior data (yūnus appears at Q 10:98 in the famous *qawm Yūnus* passage and possibly in Q 4:163, Q 6:86, Q 37:139, Q 21:87 — but only as `يونس`, the proper noun without bin-Mattā or dhū-al-nūn alternates), the surface count is plausibly low. If only 1 occurrence in Q 10 vs 1 elsewhere, the **eponymous-naming asymmetry** is itself the finding: *Q 10 is named after a prophet who appears in it a single time*, contrasting starkly with Q 12 Yūsuf.
