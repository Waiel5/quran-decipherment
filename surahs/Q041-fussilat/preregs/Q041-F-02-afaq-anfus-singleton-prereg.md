---
prereg_id: Q041-F-02
title: Q 41:53 *fī l-āfāqi wa-fī anfusihim* — āfāq corpus-singleton + co-occurrence uniqueness
date: 2026-05-09
seed: 20260509
locked_at: 2026-05-09T23:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q041-F-02 — *āfāq* corpus-singleton + *āfāq* × *anfus* co-occurrence

## 1. Hypotheses (direction-locked)

**H1 (direction-locked)**: The orthographic-string *الآفاق* (al-āfāq, with alif-madda Unicode `U+0622` for the `ā`) appears in **EXACTLY ONE verse** in the Qurʾān: Q 41:53. Q 41 is the sole carrier of the *āfāq* lexeme in the corpus.

**H2 (direction-locked)**: The co-occurrence of *āfāq*-substring AND *anfus*-substring (root `n-f-s` reflexive plural) in the SAME verse occurs in EXACTLY ONE verse: Q 41:53.

**H3 (direction-locked)**: The full collocation pattern *في الآفاق وفي أنفس* (*"in the horizons and in [the] selves"*) is a corpus-singleton (1 attestation, Q 41:53).

## 2. Null

**H0_1**: *āfāq* (آفاق / الآفاق with U+0622) appears in 0, 2, 3, … verses.
**H0_2**: *āfāq* × *anfus* co-occurs in 0, 2, 3, … verses.
**H0_3**: The full collocation appears in 0, 2, 3, … verses.

## 3. Operationalization

- Tashkeel level: **no-tashkeel** (`/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`).
- Token level: orthographic substring.
- *āfāq* search pattern: regex `آفاق` — Unicode `U+0622` (ALEF WITH MADDA ABOVE) + `U+0641` + `U+0627` + `U+0642`. The form `الآفاق` is the surface form in Q 41:53.
- *anfus* search pattern: regex `أنفس` — Unicode `U+0623` (ALEF WITH HAMZA ABOVE) + `U+0646` + `U+0641` + `U+0633`.
- Co-occurrence: both substrings present in the same verse, in either order.
- Collocation: literal substring `في الآفاق وفي أنفس` (with U+0622 in *al-āfāq*, U+0623 in *anfus*).

## 4. Direction locks

- H1: 1 attestation, at Q 41:53. Anything else = NULL.
- H2: 1 attestation, at Q 41:53. Anything else = NULL.
- H3: 1 attestation, at Q 41:53. Anything else = NULL.

## 5. Bonferroni

k = 3 sub-hypotheses → α_corrected = 0.05 / 3 ≈ 0.01667.

Each test is a deterministic substring search, so the relevant statistic is the attestation count. Significance is the corpus-singleton outcome; if the verse-count is greater than 1, that is the empirical result and the test is NULL.

## 6. Success / failure criteria

- **VINDICATION**: all three H1, H2, H3 = singleton at Q 41:53.
- **PARTIAL**: 1-2 of {H1, H2, H3} singleton, others NULL.
- **NULL**: any H_i breaks corpus-uniqueness (count ≠ 1 OR not at Q 41:53).

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q041-F-02.json`: SHA, hypotheses, search patterns, attestation lists, verdicts.

## 9. Rationale

Q 41:53 *sa-nurīhim āyātinā fī al-āfāqi wa-fī anfusihim* is the **classical anchor for modern *iʿjāz ʿilmī* literature**. Empirically grounding the test in corpus-uniqueness establishes:

1. Whether the verse's lexical singularity supports its disproportionate apologetic prominence.
2. Whether *al-āfāq* (horizons) is a corpus-rare term, or a common one re-purposed.
3. Whether the *āfāq* × *anfus* pairing is a textual hapax.

This test is purely descriptive-empirical and direction-locked. The classical reading (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr) is eschatological-historical regardless of the lexical singularity; this test does not adjudicate classical-vs-modern hermeneutics.

## 10. Cross-references

- [[Q041-fussilat/05-classical-claims-audit|Q 41 claims audit §6]]
- [[Q041-fussilat/03-tafsir-survey|Q 41 tafsīr §9]]
