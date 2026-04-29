---
prereg_id: Q043-F-05
title: Q 43:57-65 ʿĪsā-passage christological-token density vs corpus-prior null
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T19:25:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q043-F-05 — Q 43:57-65 ʿĪsā-block density

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The Q 43:57-65 contiguous block (the ʿĪsā christological passage, 9 verses) has christological-token density (substrings *عيسى* + *مريم*) per 1000 tokens **above the 99th percentile** of all length-9 contiguous-verse-window densities computed across the corpus.

## 2. Null

**H0**: Q 43:57-65 christological density is within the corpus distribution of 9-verse-windows (i.e., not in the upper 1%).

## 3. Operationalization

- Tashkeel level: **no-tashkeel**.
- Source: `quran-text/quran-no-tashkeel.json`.
- Christological tokens: words containing substring `عيسى` (ʿĪsā) OR `مريم` (Maryam). The composite `ابن مريم` (ibn Maryam) is captured by the *مريم* substring.
- Window definition: every contiguous 9-verse window across the corpus (sliding within each surah; windows that cross surah-boundaries are excluded).
- Per-window density = (christological-tokens) / (total tokens) × 1000.
- Test: Q 43:57-65 density vs the percentile rank in the full corpus 9-window-density distribution.

## 4. Direction lock

Pre-committed: **Q 43:57-65 density ≥ 99th percentile of corpus 9-windows**.

If observed direction reversed: NULL.

## 5. Bonferroni

Member of Q 43 family k=4. α_corrected = 0.0125. Density-rank is exact-corpus-rank, not parametric.

## 6. Success / failure criteria

- **VINDICATED**: Q 43:57-65 density at or above corpus 99th percentile of 9-windows.
- **DIRECTIONAL**: Q 43:57-65 density at corpus 95-98th percentile.
- **NULL**: Q 43:57-65 density below 95th percentile.
- **PRE-COMMIT VIOLATION**: Q 43:57-65 density below corpus median.

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q043-F-05.json` with: Q 43 block density, corpus 9-window distribution percentiles, Q 43 percentile rank, top-10 highest-density 9-windows.

## 9. Rationale

The classical exegetical tradition (al-Ṭabarī, Ibn Kathīr, al-Rāzī ad Q 43:57-65) treats this 9-verse block as the most extended Meccan ʿĪsā christological passage. The empirical lemma-density test formalizes the claim that this block is christologically saturated relative to the corpus baseline — and pre-commits to a precise threshold (99th percentile).

## 10. Honest limits

- The substring-match for *مريم* will catch all Maryam-references; for *عيسى* it catches only the explicit name. The lexical-coverage is anchored on these two surface forms.
- 9-window scan within-surah (not crossing boundaries) means Q 19 (the Maryam-surah) will produce many overlapping high-density windows — Q 19 windows likely dominate the top of the distribution.
- This test is **about Q 43:57-65 specifically**, not the surah Q 43 as a whole.
- The corpus 9-window distribution is heavily zero-inflated (most windows have zero christological tokens); the percentile rank is therefore concentrated in the upper tail.
