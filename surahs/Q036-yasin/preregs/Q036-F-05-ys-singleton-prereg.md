---
finding_id: Q036-F-05
title: Q 36 Yāsīn — YS muqaṭṭāʿat is a corpus-EXACT singleton
date: 2026-05-09
phase: B+
seed: 20260509
type: pre-registration
status: locked-before-run
---

# Q036-F-05 — YS muqaṭṭāʿat is the unique surah-opener in the corpus

## 1. Hypothesis

H₀ (null): The two-letter sequence "يس" appears as the opening verse of ≥ 2 surahs (i.e., it is not a singleton among muqaṭṭāʿat openers).

H₁ (directional, pre-committed): The two-letter sequence "يس" appears as the opening verse of **exactly one** surah in the corpus — Q 36. No other surah opens with this combination, neither in isolation nor as part of a longer muqaṭṭāʿat string.

## 2. Direction (locked BEFORE observation)

- **Singleton claim** (pre-committed): Q 36's "يس" is a 1/114 occurrence.
- **PASS condition**: exactly one surah has verse 1 == "يس" (after stripping any prefixed bismillah marker that may appear at the start of v.1 for some encodings).
- **FAIL / NULL condition**: any other surah has verse 1 == "يس", or "يس" appears as a substring of any other muqaṭṭāʿat-opening string.

Acceptable variant lens: also check the same singleton claim against `quran-min-tashkeel.json` and `data/alt-text/quran-uthmani-consonantal.json` for cross-script stability.

## 3. Rules-tuple

`(no-tashkeel, orthographic-grapheme, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi, surah-opening-verse-only)`

Cross-validate also under: `(min-tashkeel, ...)` and `(Uthmani-consonantal, ...)`.

## 4. Data sources

- `quran-text/quran-no-tashkeel.json` (primary)
- `quran-text/quran-min-tashkeel.json` (cross-validation 1)
- `data/alt-text/quran-uthmani-consonantal.json` (cross-validation 2)
- Known classical muqaṭṭāʿat catalog (29 surahs): Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68

## 5. Procedure (deterministic — no permutations needed)

1. Load each of the 114 surahs; extract verse-1 text after stripping basmala if present.
2. For each surah s, check whether v1 == "يس" (exact match, no surrounding text).
3. Also check whether "يس" appears as a *prefix* of v1 of any other surah, indicating a non-isolated occurrence.
4. Print the full list of muqaṭṭāʿat-opening strings (29 surahs) for completeness.
5. Cross-validate against the 2 alternative variants.

## 6. Success criteria (PASS-DIRECTED)

- PRIMARY: Exactly 1 surah has verse 1 == "يس". This surah is Q 36.
- ROBUSTNESS: Result holds under min-tashkeel and Uthmani-consonantal lenses.

If both pass, verdict is **PASS-DIRECTED-CORPUS-EXACT**.

## 7. Failure / NULL criteria

- If any other surah's verse 1 equals "يس" or is a prefix-match: NULL with prominence.
- If the variant-cross-check disagrees: RULES-TUPLE-FRAGILE.

## 8. MW protections

- MW-1: instrument (string-equality) pre-locked.
- MW-2: not applicable (deterministic count); reporting full enumeration.
- MW-6: instrument-control = list of 29 muqaṭṭāʿat openers (broader reference set).
- MW-7: post-hoc cap not triggered (deterministic enumeration of pre-locked universe).

## 9. Honest limits

- "Singleton" here refers to the 2-letter YS combination as an entire verse. The letter ي appears alone in countless contexts (suffixes, pronouns); the letter س appears alone in many. The claim is that the 2-letter ordered string "يس", as a standalone v1, occurs once.
- The 29-letter muqaṭṭāʿat catalog itself is the classical convention; we test within it.

## 10. Seed and SHA

Seed: 20260509 (n/a for deterministic test; documented for journaling).
Pre-reg SHA-256 to be computed at file-lock; embedded into the run script.
