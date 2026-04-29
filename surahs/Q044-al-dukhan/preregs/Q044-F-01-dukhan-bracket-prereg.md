---
finding_id: Q044-F-01
title: Q 44:10 + Q 41:11 are the corpus's only two attestations of the noun *dukhān* (دخان)
date_locked: 2026-04-28
seed: 20260428
phase: B+
test_family: per-surah
---

# Q044-F-01 pre-registration: dukhān-bracket lexical hapax-pair

## Hypothesis (direction-locked)

The lexeme *dukhān* (Arabic: دخان; the surface noun "smoke", not derivatives like *adkhān*, *dakhana*) appears in **exactly two surahs** in the canonical Hafs-Kufan no-tashkeel Quran corpus:
- Q 41:11 (cosmogonic): heavens-as-smoke at creation.
- Q 44:10 (eschatological): sky-bringing-smoke at the Hour.

Both occurrences fall within the ḥawāmīm-7 cluster (HM-7 = {Q 40, 41, 42, 43, 44, 45, 46}).

**Pre-committed direction**: the count of *dukhān* (ال + دخان exact form, including in idafa/preposition contexts) in the corpus is exactly 2.

**Pre-committed location**: both occurrences are within the HM-7 cluster (positions 41 and 44 in the mushaf).

## Null hypothesis

H₀: *dukhān* appears more than 2× in the corpus, OR not exclusively within HM-7.

## Operationalization

- **Tashkeel level**: no-tashkeel (project default).
- **Source file**: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
- **Match form**: exact substring `دخان` (4 letters: د-خ-ا-ن).
- **Counting unit**: number of verses containing the substring.

## Verdict criteria

- **VINDICATED**: count = 2, both in HM-7 (Q 41:11 and Q 44:10).
- **DIRECTIONAL**: count = 2 but not both in HM-7.
- **FALSIFIED / NULL**: count ≠ 2.

## Garden-of-forking-paths log (BEFORE running)

- Tashkeel level locked: no-tashkeel.
- Counting unit locked: verse-occurrences (not word-occurrences within verses).
- Match-form locked: exact substring `دخان`. Variants like `الدخان` (def. art.) or in iḍāfa `دخانا` will be detected as substring matches; root-level matches (e.g., *dakhana* verb) will NOT match.
- Direction-of-effect locked: the count is 2 OR is contradicted.

## Replication plan

- Re-run on `quran-text/quran-min-tashkeel.json` (substring match should hold under min-tashkeel).
- Re-run on `quran-text/quran-full-tashkeel.json` (substring match may fail if shadda/sukūn break the substring).

## Bonferroni

This is a single-hypothesis-direction test (k=1). α = 0.05.

## Run script

`/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/scripts/Q044_F_01_dukhan_bracket.py`.

## Output

`/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-01.json`.
