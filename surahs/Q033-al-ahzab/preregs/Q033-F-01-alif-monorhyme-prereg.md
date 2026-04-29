---
id: Q033-F-01
title: Alif-monorhyme purity test — corpus-wide ranking and pre-Islamic poetry control
date_locked: 2026-04-28
phase: B+
seed: 20260428
rules_tuple: (min-tashkeel, orthographic-token, last-letter-of-verse-after-stripping-final-mark, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q033-F-01 — Alif-monorhyme purity (PRE-REG)

## Hypothesis (locked direction)

Q 33 al-Aḥzāb has the highest alif-final-letter rate of any surah in the Quranic corpus.
Direction: Q 33 ranks #1 (or tied for #1).

## Method

1. Load `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json`.
2. For each surah, for each verse: take the verse text, strip trailing whitespace and tashkeel marks (ـ ً ٌ ٍ َ ُ ِ ّ ْ ٰ), find the last letter character.
3. Define alif-finals as `{ا, آ, أ, إ, ى, ٰ}` — the alif-shaped graphemes that mark the *-ā* / *-ī* (alif maqṣūra) rhyme.
4. Compute alif-final-rate per surah = count(alif-final verses) / count(verses).
5. Rank all 114 surahs.
6. NULL: Q 33 is not rank #1.

## Cross-corpus control

Compute alif-final-rate over baseline poetry corpus (al-Muʿallaqāt: imru-al-qais, antara, labid, tarafa, zuhayr, harith, amr-bin-kulthum) — the same metric on `data/baseline-corpora/raw/muallaqa-*.txt`. Compare distribution.

## Success criteria

- DIRECTIONAL VINDICATION: Q 33 ranks #1 strictly.
- TIED-VINDICATION: Q 33 ranks tied #1 with one or more other surahs.
- DIRECTIONAL FALSIFICATION: Q 33 ranks below top-3.

## Bonferroni

This is a single direction-of-effect test (k=1) — α=0.05.

## NULL

Direction reversed = published as NULL with full prominence.
