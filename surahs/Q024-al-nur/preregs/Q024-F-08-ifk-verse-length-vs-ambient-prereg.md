---
finding_id: Q024-F-08
title: "Ifk pericope (Q 24:11-20) verse-length distribution vs ambient Q 24 verses"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: 10000
bonferroni_k: 4
alpha_raw: 0.05
alpha_bonferroni: 0.0125
direction: ifk verses are LONGER than ambient Q 24 verses (narrative-pericope expansion)
---

# Q024-F-08 — Ifk pericope (Q 24:11-20) verse-length distribution

## Hypothesis (LOCKED before observation)

Narrative-pericope passages in the Quran typically expand verse-length relative to legal-prose, exhortation, or refrain-rhyme passages. The al-ifk story (Q 24:11-20) is the longest narrative pericope in Q 24 and is the corpus's central instance of a Medinan moral-narrative defense-of-the-Prophet's-household.

Pre-registered direction: **the al-ifk pericope (verses 11-20) has a higher mean verse-length (in no-tashkeel orthographic words) than the ambient Q 24 verses (verses 1-10 + 21-64 = 54 verses)**.

This is a content-genre prediction: narrative expansion should be empirically visible at the verse-length level.

## Method (LOCKED)

1. Load Q 24 from `quran-text/quran-no-tashkeel.json`.
2. For each verse `v` in Q 24:
   - Strip mushaf marks {۞, ۖ, ۗ, ۚ, ۛ, ۜ}.
   - Word-count = number of whitespace-separated tokens after stripping.
3. Partition:
   - `ifk` = verses 11–20 (10 verses).
   - `ambient` = verses 1–10 + 21–64 (54 verses).
4. Compute:
   - `mean_ifk`, `mean_ambient`, `Δ = mean_ifk − mean_ambient`.
   - `median_ifk`, `median_ambient`.
5. Permutation null: 10,000 random 10-verse subsets of Q 24; compute the empirical distribution of `mean_subset − mean_complement`.
6. p_one-sided = fraction of permutations with `Δ_perm ≥ Δ_observed`.

## Rules-tuple (LOCKED)

`(no-tashkeel, orthographic-token, words, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`

## Direction (LOCKED)

**Δ > 0** (ifk longer than ambient). The direction is positive — narrative pericopes expand. Reversed direction (Δ < 0, ifk shorter than ambient) = pre-commit violation, NULL with prominence.

## Success criteria

- Δ > 0 AND p_one-sided < α_Bonferroni (0.0125): **CONFIRMED**.
- Δ > 0 AND p_one-sided < 0.05 but > 0.0125: **DIRECTIONAL**.
- Δ > 0 AND p_one-sided > 0.05: **WEAK-DIRECTIONAL**, reported as descriptive.
- Δ < 0: **NULL with pre-commit-violation flag**, published with prominence.

## Honest limits (pre-registered)

- Verse-segmentation in Hafs-Kufan is conventional. Q 24 has 64 verses by the standard count; this is the count used.
- The ambient set (54 verses) mixes registers (legal-prose vv. 1-10, marriage rules vv. 32-34, light-parable vv. 35-46, cosmic signs vv. 41-46, hypocrite contrast vv. 47-57, home-entry vv. 58-61, closing vv. 62-64). The hypothesis is that the ifk *narrative* register expands verse-length above this register-mix average.
- Counter-hypothesis (acknowledged): the cosmic-signs block (vv. 41-46) and the al-ifk narrative are both expansive; if the cosmic-signs block dominates the ambient distribution, the ambient mean may be near or above ifk's mean, producing a negative Δ. This is a real risk to the pre-registered direction.
- The pre-reg locks the comparison to verse-mean word-count. Alternative metrics (letter-count, syllable-count) are NOT permitted post-hoc.

## Seed

20260509

## Pre-registration SHA256

Computed at write-time; embedded in `Q024_F_08_ifk_verse_length.py` and verified at runtime.
