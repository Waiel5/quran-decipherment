---
id: Q017-F-04
title: Q 17 Children-of-Israel narrative concentration — corpus density vs Q 17 density
date_locked: 2026-04-28
phase: B+
seed: 20260428
rules_tuple: (no-tashkeel, orthographic-token, lemma "إسرائيل", surah-level-density, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q017-F-04 — Banī Isrāʾīl (Children of Israel) narrative concentration in Q 17 (PRE-REG)

## Hypothesis (locked direction)

Q 17, classically named **Banī Isrāʾīl** (al-Bukhārī ḥadīth #4502, Ibn Masʿūd's *al-ʿitāq al-uwal*), has a Children-of-Israel narrative concentration sufficient to justify the alternative classical naming. Specifically:

(A) Q 17 contains the lemma "إسرائيل" (Isrāʾīl) at a per-word density above the corpus-mean among surahs that use the term.

(B) Among surahs that use "إسرائيل", Q 17 ranks within the top quartile for raw token count of the lemma OR per-word density.

Direction: Q 17 ranks ≤ rank-25 (top quartile of 114 surahs) by either count OR density of "إسرائيل".

## Method

1. Load `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
2. Tokenize each surah by whitespace; count tokens containing the substring "إسرائيل" (this catches both the standalone form and possessive constructs like "بنى إسرائيل").
3. Compute per surah: `count_israil` and `density_israil = count_israil / total_words`.
4. Rank all 114 surahs by both metrics.
5. Verify Q 17's rank.

## Cross-corpus check

Compare Q 17's count and density to:
- Q 2 al-Baqara (the Cow surah, well-known for extended Children-of-Israel narrative)
- Q 7 al-Aʿrāf (also has extensive Banī Isrāʾīl content)
- Q 5 al-Māʾida, Q 26 al-Shuʿarāʾ, Q 27 al-Naml — all use the term

## Success criteria

- DIRECTIONAL VINDICATION: Q 17 rank ≤ 25 by count OR density.
- DIRECTIONAL FALSIFICATION: Q 17 rank > 25 in both count and density.

## Bonferroni

Two metrics (k=2): α_corrected = 0.025.

## NULL

If Q 17 fails on both metrics, publish as NULL — the classical Banī-Isrāʾīl naming is then *reception-history*-driven (which surahs early companions associated with the term) rather than text-density-driven.

## Classical anchor

Al-Bukhārī ḥadīth #4502, #4533, #4787 record Ibn Masʿūd: "fī Banī Isrāʾīli wa-l-Kahfi wa-Maryama wa-Ṭāhā wa-l-Anbiyāʾi: innahunna mina al-ʿitāqi al-uwali wa-hunna min tilādī" — naming five surahs (Q 17, 18, 19, 20, 21) as Ibn Masʿūd's "earliest learnt" / "old property". Q 17 is named **first** in the list of five. The claim being tested: does Q 17's textual density of Banī-Isrāʾīl content support its primacy in this hadith?
