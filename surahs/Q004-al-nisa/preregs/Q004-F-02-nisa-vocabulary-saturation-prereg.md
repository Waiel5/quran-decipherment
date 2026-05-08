---
finding_id: Q004-F-02
title: Q 4 al-Nisāʾ family-vocabulary saturation
status: PRE-REGISTERED
date: 2026-05-07
specialist: Q004-al-nisa-specialist
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q004-novel-tests-2026-05-07
alpha_bon: 0.01
direction: HIGHER (Q 4 is corpus-MAX in family-vocabulary density per 100 words; cross-corpus distinct vs Q 65 al-Ṭalāq)
acceptance_window: rank 1 of 114 on family-vocabulary density
---

# Q004-F-02 — Nisāʾ-vocabulary saturation: pre-registration

## Hypothesis

Q 4 is named al-Nisāʾ ("Women") and is classically held (al-Biqāʿī, *Naẓm al-Durar*; Ibn Kathīr, *Tafsīr*; al-Rāzī on Q 4:11) to be the corpus's locus of family-law vocabulary. This test asks: does the surah's lexical fingerprint *quantitatively* match its name?

## Operationalisation

- Text: `quran-no-tashkeel.json` (default rules-tuple).
- Lexicon (locked, family-law focus):
  `["النساء", "نساء", "نسائكم", "نساءهن", "الزوج", "الزوجة", "أزواج", "أزواجا", "زوجها", "اليتيم", "اليتامى", "يتيما", "يتامى", "المهر", "أجورهن", "الصداق", "صدقات", "الميراث", "وارث", "ورثة", "الطلاق", "طلقتم", "طلقتموهن", "طلقها", "أمهات", "بنات", "أخت", "أخوات", "أخ", "إخوة", "أب", "آباؤكم", "أمكم", "أمهاتكم"]`
- For each surah, count substring occurrences in no-tashkeel text. Compute density = count / words(s) × 100.
- Primary test: Q 4 rank 1 on family-vocabulary density.
- Cross-corpus distinctness test: vs Q 65 al-Ṭalāq (smaller, also legal-family) — Q 4 / Q 65 density ratio.

## Null model

- MW-2 corpus-prior null: 10000 permutations of token-to-surah assignment under seed=20260507; evaluate Q 4's percentile.
- Surah-label-scramble: shuffle the (count, words) pairs across surahs; report fraction of permutations where Q 4 (or rather, the surah ASSIGNED Q 4's count) lands at rank 1.

## Direction & alternative

- DIRECTION-LOCKED: HIGHER (Q 4 rank 1).
- If rank 2-3 with Q 65 ahead: DIRECTIONAL-PARTIAL (note: Q 65 is short, so density may exceed Q 4's despite Q 4's absolute leadership in occurrence count).
- If rank > 5: NULL.

## Bonferroni

- Family: Q004-novel-tests-2026-05-07, k=5; α_bon = 0.01.

## Honest limits

- Density-per-100-words favors short surahs; the absolute-count test is reported alongside the density test.
- Q 65 al-Ṭalāq is 12 verses, 289 words — its density may exceed Q 4's. The pre-registered direction is rank 1 by density, but BOTH metrics are reported. If absolute-count = rank 1 but density = rank 2 (with Q 65 #1), this is reported as DIRECTIONAL-PARTIAL with explanatory note.
- Substring matches are over-inclusive: "بنات" matches in non-family contexts too. Lexicon was built from family-law nawʿ + Ibn Kathīr Q 4 aḥkām block.
