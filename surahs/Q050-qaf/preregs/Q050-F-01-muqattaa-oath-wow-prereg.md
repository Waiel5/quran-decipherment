---
finding_id: Q050-F-01
title: "Q 50:1 *qāf wa-l-Qurʾān al-majīd* — uniqueness of muqaṭṭaʿ-letter immediately followed by oath-particle wāw"
date_pre_registered: 2026-05-07
status: PRE-REGISTERED
seed: 20260507
n_perm: 0 (exhaustive corpus enumeration)
bonferroni_k: 1
bonferroni_family: Q050-F-01-singletons
alpha_raw: 0.05
alpha_bon: 0.05
direction: "POSITIVE — Q 50:1 is predicted to be the ONLY verse in the Quran where a muqaṭṭaʿ-letter sequence is immediately followed by the oath-particle wāw (و)."
rules_tuple: "(no-tashkeel, orthographic-token, exact substring match after Quranic-mark stripping, basmala-not-counted-in-Q50, Hafs-Kufan, mushaf-order)"
---

# Q050-F-01 — muqaṭṭaʿ + oath-wāw uniqueness audit

## Hypothesis (LOCKED)

Q 50:1 reads `ق ۚ والقرآن المجيد` — the singleton-letter ق immediately followed by an oath formula opening with the particle wāw (و). Across the 29 muqaṭṭaʿāt-opener surahs, the predicted result is that Q 50 is the **only** verse-1 where a muqaṭṭaʿ-letter sequence (ALM, ALR, etc.) is immediately followed by an oath-particle wāw construction (والـ + noun-genitive).

The standard muqaṭṭaʿāt-followed-by formula is muqaṭṭaʿ + book-reference (cross-finding-008): e.g., Q 2:2 *dhālika al-kitābu*, Q 12:1 *tilka āyātu al-kitābi al-mubīn*, Q 26:2 *tilka āyātu al-kitābi al-mubīn*. NO classical scholar (al-Suyūṭī *Itqān*, al-Zarkashī *Burhān*, al-Rāzī *Mafātīḥ*) catalogues a separate "muqaṭṭaʿ + oath-wāw" pattern.

## Direction (LOCKED)

POSITIVE — Q 50:1 is hypothesized to be a corpus-singleton on the construction "muqaṭṭaʿ-letter(s) + immediately-following oath-particle wāw + definite-article noun-genitive."

## Operationalization

For each of the 29 muqaṭṭaʿāt-opener surahs (per al-Suyūṭī catalogue: Q 2, 3, 7, 10-15, 19, 20, 26, 27, 28, 29-32, 36, 38, 40-46, 50, 68), inspect verse 1's first non-muqaṭṭaʿ token after the letters.

A construction matches the test iff (after stripping mushaf-marks ۚ ۖ ۗ ۛ etc.):
- Verse 1 begins with one of the canonical muqaṭṭaʿ-letter sequences.
- The first non-muqaṭṭaʿ token after the letter(s) is `وَ`+definite-article noun (i.e., starts with `وال` in no-tashkeel orthography).

Compare also Q 36:1 (يس) and Q 38:1 (ص) which are also singleton or two-letter openers.

## Rules-tuple (LOCKED)

`(no-tashkeel, orthographic-token, exact substring match after Quranic-mark stripping, basmala-not-counted-in-Q50, Hafs-Kufan, mushaf-order)`

## Success criteria

| Metric | Predicted | Verdict if matched |
|:--|:--|:--|
| Q 50:1 matches the construction | YES | (necessary) |
| Number of OTHER muqaṭṭaʿāt-surah verse-1's matching the same construction | 0 | **CONFIRMED** (Q 50 is unique) |
| Number of OTHER muqaṭṭaʿāt-surah verse-1's matching | 1 (specifically Q 38:1 *ص والقرآن ذي الذكر*) | **CONFIRMED-PAIR** (with Q 38) |
| Number of OTHER muqaṭṭaʿāt-surah verse-1's matching | ≥ 2 | **NULL** (pattern not unique) |

## Failure criteria

If any 3rd muqaṭṭaʿāt-surah verse-1 has the muqaṭṭaʿ + oath-wāw construction → NULL.

## Notes

- Q 38:1 (`ص والقرآن ذي الذكر`) is a sibling case — likewise singleton-letter + oath-wāw. The pre-reg explicitly anticipates the Q 50 / Q 38 PAIR result; this is part of the singleton-letter triplet (Q 38, Q 50, Q 68) cohort under cross-finding-026.
- This test is corpus-exact-substring; null distribution is not needed (pure enumeration). Bonferroni-k=1 (single test).
- The CONFIRMED-PAIR verdict would empirically *vindicate* a NEW classical pattern — "singleton-muqaṭṭaʿ + oath-of-Quran" — that is NOT catalogued in al-Suyūṭī's nawʿ on muqaṭṭaʿāt openings.

## Output files

- Pre-reg: this file (`preregs/Q050-F-01-muqattaa-oath-wow-prereg.md`).
- Script: `scripts/Q050_F_01_muqattaa_oath_wow.py`.
- JSON: `csv/Q050-F-01.json`.
- Findings: in `06-novel-findings.md` §Q050-F-01.
