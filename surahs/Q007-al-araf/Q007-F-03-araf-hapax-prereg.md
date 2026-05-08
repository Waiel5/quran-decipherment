---
surah: 7
test_id: Q007-F-03
title: aʿrāf (heights/ramparts) eschatological-third-place corpus-hapax
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 4
bonferroni_family: Q007-F-01..F-04
alpha_bon: 0.0125
direction_locked: positive — al-aʿrāf in the "third-place between heaven and hell" sense is corpus-hapax exclusive to Q 7
rules_tuple: (no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q007-F-03 — Pre-registration: aʿrāf-as-third-place corpus-hapax

## 1. Hypothesis (locked before observation)

**H1**: The orthographic token `الأعراف` ("the heights/ramparts," definite article + plural of `ʿurf`) appears in the corpus EXCLUSIVELY in Q 7. Specifically:
- Total corpus occurrences of the literal string `الأعراف` ≤ 2.
- All such occurrences are in Q 7.
- The semantic role — "an eschatological third-place between Garden and Fire, with men (rijāl) on it who recognize people by signs" — is a corpus-unique theological geography.

**H0**: `الأعراف` is a generic Arabic word that appears in multiple surahs in non-eschatological senses.

## 2. Operational definition

Three counts:
1. `n_orthographic` = count of literal `الأعراف` tokens in `quran-text/quran-no-tashkeel.json` corpus-wide.
2. `n_q7` = count of `الأعراف` in Q 7 specifically.
3. `n_root_Erf` = count of QAC stem `Erf` (root ʿ-r-f, "to know/recognize") in Q 7 (the surah's name-root, not the eschatological place sense).

Then:
- `surah_unique_for_alaaraaf` := (n_orthographic == n_q7).
- `is_hapax_2` := (n_orthographic ≤ 2).
- `concentration_q7_root_Erf` := count of root `Erf` in Q 7 / total corpus root `Erf` count.

## 3. Test statistic

**Primary**: binary `surah_unique_for_alaaraaf == True` AND `is_hapax_2 == True`.

**Secondary**: rank of Q 7 by absolute-count of `الأعراف` (must be 1/114).

**Bonferroni-corrected NULL**: probability under random distribution of 2 corpus-token-occurrences across 114 surahs (weighted by surah length in tokens) that BOTH end up in the same surah. Using `quran-text/quran-no-tashkeel.json` token counts for 114 surahs, compute analytic-binomial probability.

## 4. Success / Failure

- **CONFIRMED**: surah_unique == True AND n_orthographic ≤ 2 AND analytic null-probability ≤ 0.0125.
- **DIRECTIONAL**: surah_unique == True but n_orthographic > 2 (the term appears elsewhere too).
- **NULL**: surah_unique == False (term appears in other surahs).

## 5. Honest limits

1. The pre-reg is **EXTREMELY DIRECTIONAL** — the prediction is essentially trivially observable (Q 7 IS named al-Aʿrāf; the term is the surah's eponym). The interesting empirical claim is the **2-occurrence-cap** plus the **third-place semantic role**. The test passes on counts; the semantic role must be cross-checked against tafsir (al-Ṭabarī, al-Rāzī, al-Qurṭubī).
2. There is no analytic competitor surah; this is essentially measuring whether the surah's *eponymic term is its own*. The novel finding is the **eschatological-third-place-as-hapax** (semantic uniqueness), not the orthographic-uniqueness.
3. The token `aʿrāf` (without `al-`) might appear elsewhere; we count both definite and indefinite forms in a follow-up.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token-exact-string, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q007_F_03_araf_hapax.py`.
