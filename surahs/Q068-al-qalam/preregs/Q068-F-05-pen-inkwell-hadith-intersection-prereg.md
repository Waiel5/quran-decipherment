---
finding_id: Q068-F-05
title: "Q 68 hadith citation density — does Q 68:1 dominate Q 68's hadith citation profile?"
date_pre_registered: 2026-05-07
status: PRE-REGISTERED
seed: 20260507
n_perm: 0 (descriptive plus binomial test)
bonferroni_k: 1
bonferroni_family: "Q068-F-05 (single test on most-cited verse)"
alpha_raw: 0.05
alpha_bon: 0.05
direction: "POSITIVE — Q 68:1 expected to be the most-cited Q 68 verse across the 9 books, at higher than uniform-distribution rate"
---

# Q068-F-05 — PEN-INKWELL HADITH INTERSECTION

## Hypothesis

The "pen-creation" / *kataba al-qalam mā kāna wa-mā huwa kāʾin* hadith-complex (Tirmidhī's *qadar* tradition; Abū Dāwūd's *qadar* tradition; Ibn ʿAbbās narrations on ن) is interpretively anchored in **Q 68:1** *Nūn. wa-l-qalam wa-mā yasṭurūn* ("Nūn. By the Pen and what they inscribe").

Empirical prediction: across the 9 canonical hadith collections, **Q 68:1 is the most-cited Q 68 verse**, at a frequency higher than uniform random distribution across the 52 verses of Q 68 would predict.

## Locked operationalization

For each of the 9 canonical collections (al-Bukhārī, Muslim, al-Tirmidhī, Abū Dāwūd, al-Nasāʾī, Ibn Mājah, Mālik *Muwaṭṭaʾ*, Aḥmad *Musnad*, al-Dārimī):
- Index all hadith records (using `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/{book}.json`).
- For each Q 68 verse v ∈ {1, ..., 52}: find hadith records whose Arabic text contains a normalized substring match for that verse's distinctive tokens. The "distinctive substring" for each verse is the contiguous 4+-word phrase from the verse most likely to be QURAN-quote (excluding short formulaic words like *wa-*, *fa-*, *qāla*).
- For each verse: count how many distinct hadith records cite it (across all 9 books).
- Identify the verse with the maximum citation count — call it v_max.
- Pre-registered prediction: v_max == 1, AND citation-count(v=1) > citation-count(any other v).

## Rules-tuple (LOCKED)

Hadith Arabic text matching uses:
- Normalize: alif-variants (أ إ آ → ا), yāʾ-variants (ى → ي), tāʾ marbūṭa (ة → ه), strip all tashkeel marks ([َُِْٰٓـ ً ٌ ٍ ّ]).
- Match: case-insensitive contiguous substring.
- For Q 68:1, the distinctive 4-word phrase is *والقلم وما يسطرون* (the bare ن alone is too short and too common to disambiguate).
- For other verses, the distinctive phrase is the LONGEST contiguous content-word sequence with at least 4 words, picked deterministically before observation.

## Null distribution

**Binomial test** at uniform-distribution null:
- Total Q 68 hadith citations = T (sum across 52 verses).
- Under uniform null: P(verse v cited) = 1/52 for any v.
- Expected citations to v=1 under null: T/52.
- Observed citations to v=1: x_1.
- One-sided binomial p = P(X ≥ x_1 | n=T, p=1/52).

## Direction (LOCKED)

POSITIVE: x_1 ≥ x_v for all v ∈ {2..52}, AND x_1 > T/52 at p < 0.05.

If x_1 < T/52 (Q 68:1 is cited LESS than uniform): pre-commit violation, reported as NULL with prominence.

## Success / failure criteria

| Verdict | Criterion |
|:--|:--|
| **VINDICATED** | Q 68:1 is the unique modal verse AND binomial p < 0.05 |
| **DIRECTIONAL** | Q 68:1 is among top-3 modal verses but not unique max |
| **NULL** | Q 68:1 is below median citation count |
| **DIRECTION_REVERSED** | Q 68:1 cited at less than uniform rate |

## Honest limits

- Hadith corpus matching is substring-based, not semantic; verse-citations may be missed if the hadith paraphrases or quotes a partial sub-phrase.
- The 9-book corpus has uneven Arabic-text quality (some entries lack Arabic text); the test counts only ones with Arabic text.
- Verse 1's bare ن is excluded as a substring marker due to ambiguity.
- The most-cited verse in PRACTICE may not be a *prediction-verifying* verse (e.g., Q 68:4 *innaka la-ʿalā khuluqin ʿaẓīm* is famous via the Prophet's-character hadith, Ibn Mājah #2067). The test's null is uniform-distribution, NOT a competing-verse model.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q068_F_05_pen_inkwell_hadith_intersection.py`.
- JSON: `csv/Q068-F-05.json`.
- Findings: in `06-novel-findings.md`.
