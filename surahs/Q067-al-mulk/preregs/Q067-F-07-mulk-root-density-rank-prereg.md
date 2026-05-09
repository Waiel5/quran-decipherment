---
finding_id: Q067-F-07
title: mulk-root density across the 114 corpus — does Q 67 rank in top-5 by density?
date_locked: 2026-05-09
phase: B+
seed: 20260509
n_perm: 10000
rules_tuple: (no-tashkeel, QAC-stem-roots, density-per-root-token, Hafs-Kufan)
---

# Q067-F-07 — Pre-registration

## Hypothesis

Q 67 al-Mulk is named after the *mlk* root. If the surah's naming convention is tracked at the lexical-density level, then Q 67 should rank in the top 5 of the 114 surahs by per-root-token *mlk* density (counts of QAC stem-root `mlk` ÷ surah total QAC stem-root tokens).

## Pre-registered direction (LOCKED)

**TOP-5**: Q 67 rank by *mlk*-stem density per 1000 root-tokens is ≤ 5 of 114.

## Companion to Q067-F-04

Q067-F-04 already tested *over-concentration vs uniform random null* at the QAC token level and found NULL (p = 0.58 hypergeometric). This Q067-F-07 reframes the same data as a **comparative-rank test** across the 114 corpus surahs — a different statistical lens. The directional pre-registration is independent: rank-in-top-5 is a stronger claim than "above uniform expectation."

## Success criterion

**PASS-DIRECTED**:
- Q 67 rank ≤ 5 of 114 by density (counts per 1000 root-tokens).

**NULL**:
- Q 67 rank > 5 of 114.

## MW protections

- **MW-1 (instrument-prior)**: Density measure pre-locked as QAC stem-root count / total stem-root tokens × 1000.
- **MW-2 (corpus-prior)**: All 114 surahs ranked; rank itself is the statistic.
- **MW-3 (alternative-models)**: Also compute raw count rank (no length normalization) — secondary.
- **MW-5 (replication)**: Cross-check via the Q067-F-04 JSON output's existing rank fields.
- **MW-7 (post-hoc cap)**: Rank threshold ≤ 5 pre-locked.

## Failure conditions

- Q 67 rank > 5: NULL — name-tracks-density does NOT hold for Q 67 by rank.
- Q 67 rank in 5-15: NULL-near-miss (not pre-registered as a separate verdict).

## Honest limits

- The QAC root `mlk` encompasses surface forms beyond the surah's titular *al-mulk* (e.g., *malāʾika* angels, *malik* king, *malakūt*). The mlk root family is broader than the *mulk*-noun used in v. 1.
- The corpus has natural variation in surah length; the density normalization addresses but does not eliminate length-confounding.

## Output

`/Users/grey/Downloads/quran/surahs/Q067-al-mulk/csv/Q067-F-07.json`
