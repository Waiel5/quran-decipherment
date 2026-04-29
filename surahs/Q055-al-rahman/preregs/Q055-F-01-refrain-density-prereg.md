---
finding_id: Q055-F-01
title: 31-fold refrain density audit (fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān)
phase: B+
date_locked: 2026-04-28
seed: 20260428
n_perm: 0  # exact-count test, no permutation needed for the count itself
bonferroni_k: 2  # (count, rank)
alpha_bon: 0.025
script: surahs/Q055-al-rahman/scripts/Q055_F_01_refrain_density.py
---

# Q055-F-01 — Refrain density audit pre-registration

## Hypothesis

H1a: The phrase *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* (فبأي آلاء ربكما تكذبان) appears EXACTLY 31 times as a stand-alone āya within Q 55, stable across all three tashkeel variants.

H1b: Q 55 ranks #1 across the 114-surah corpus in (a) maximum-repeated-≥4-word-phrase count and (b) maximum identical-verse repetition count, both computed in no-tashkeel orthographic-token level.

## Direction (LOCKED before observation)

- Count direction: count = 31 (single value).
- Rank direction: lower rank number is better (1 = top); Q 55 = 1.

Counter-direction (Q 55 not corpus-#1 in either rank, OR count ≠ 31, OR variant inconsistency) = NULL.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

- Cross-validate with `min-tashkeel` and `full-tashkeel` for the count (must match 31 in all three).
- Normalization: NFD-strip diacritics, replace `[إأآٱ]→ا`, `ءا→ا` (madda-alif), `ى→ي`.

## Success criteria

- Count = 31 across all 3 variants → CONFIRMED
- Rank-1 in BOTH phrase and verse repetition → CONFIRMED
- Rank ∈ {2, 3} → DIRECTIONAL
- Rank > 3 OR count ≠ 31 → NULL

## Failure conditions

- Count differs by variant.
- Q 55 not top-3 in either rank metric.

## Pre-commit honesty

If the rank result is reversed, publish as NULL with full prominence.
