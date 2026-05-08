---
test_id: Q022-F-04
title: "Q 22 pilgrimage-vocabulary density per 100 words exceeds Q 2"
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q022-F-04-pilgrimage-density
alpha_bon: 0.05
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q022-al-hajj-specialist
---

# Q022-F-04 Pre-registration — Pilgrimage-vocabulary density

## Hypothesis

Q 22 al-Ḥajj is the only surah in the Quran whose name AND major theme is the pilgrimage-rite (al-Suyūṭī, *al-Itqān*, nawʿ 1). Q 2 al-Baqara contains the corpus's largest CUMULATIVE block of pilgrimage legislation (Q 2:158, 196-203 — the *manāsik* passages). Q 5 al-Māʾida contains additional pilgrimage law (Q 5:1-2, 95-97 — *iḥrām* and *hady*).

If Q 22's NAMING reflects density (not just volume), then per-100-words pilgrimage-vocabulary rate should be HIGHER in Q 22 than in either Q 2 or Q 5, despite the latter having more total mentions.

## Pre-committed prediction

**Direction-locked**: pilgrimage-vocabulary rate per 100 words

`rate(Q22) > rate(Q2)` AND `rate(Q22) > rate(Q5)`

## Vocabulary set (locked before run)

Pilgrimage roots — surface-form matches in no-tashkeel text:

- ḥajj root (ح-ج-ج): الحج, حج, الحجّ, حجوا
- ʿumra root (ع-م-ر-ة, narrow): عمرة, العمرة (NOT generic عمر which is ʿumr/lifetime)
- kaʿba: الكعبة, كعبة, البيت (when in context "the House"; ambiguity flagged)
- *manāsik* (ن-س-ك): منسك, مناسك, منسكا, نسك, ناسكوها
- *ṭawāf* (ط-و-ف): طواف, الطائفين, طوفوا, يطوف, طافوا
- *hady* (ه-د-ي narrow): الهدي, هدي (sacrificial-animal sense; ambiguity with hidāya ا-ل-ه-د-ى flagged)
- *naḥr* (ن-ح-ر): نحر, المنحر, وانحر
- *badanah* (ب-د-ن): بدنة, البدن
- al-masjid al-ḥarām: الحرام (in the locked compound-context), المسجد الحرام
- al-Ṣafā wa-al-Marwa: الصفا, المروة
- iḥrām (ح-ر-م): حرم (root sense), محرم, إحرام (ambiguity with general ḥarām flagged)

Counting rule: a token counts if any of the surface-forms above is the WORD or a substring with ≤3 char prefix-difference (e.g., الحج matches; cumulative = 1 per token).

Disambiguation rule: when ambiguity flagged (e.g., عمر, البيت, الحرام without context), inspect surrounding words within ±2 tokens; require pilgrimage-context. (For aggregate density tests, we use the unambiguous-only count as PRIMARY; ambiguous-included as SECONDARY.)

## Test

Single comparison (Bonferroni-1, α=0.05):
- Compute `rate_Q22 = (count_Q22 / words_Q22) * 100`
- Compute `rate_Q2`, `rate_Q5` analogously.
- PASS if `rate_Q22 > max(rate_Q2, rate_Q5)`.

For permutation context (not p-value, just descriptive): compute rate for all 114 surahs; report Q22's rank.

## Direction-of-effect lock

Predicted: `rate(Q22) > rate(Q2) AND rate(Q22) > rate(Q5)`.
If `rate(Q22) ≤ rate(Q2) OR rate(Q22) ≤ rate(Q5)`, publish as NULL.

## Success criteria

- VINDICATED: Q22 strictly higher than both AND ranks #1 of 114 surahs (or top-2).
- DIRECTIONAL: Q22 higher than Q2 OR Q5 but not both.
- NULL: Q22 ≤ both.

## Garden-of-forking-paths log

- BEFORE running: stem list locked from al-Suyūṭī's *aḥkām al-ḥajj* keyword inventory plus al-Qurṭubī's pilgrimage-passage word concordance.
- BEFORE running: per-100-words denominator chosen because Q 2 (6,166 words) is 4.8× longer than Q 22 (1,282 words); raw counts would mechanically favor Q 2.
