---
finding_id: Q082-F-01
title: Q 82 doubled wa-mā-adrāka-mā corpus-uniqueness verification (H-NEW-1190 sub-finding)
phase: B+
date_locked: 2026-05-09
seed: 20260509
n_perm: 0  # exact-count test
bonferroni_k: 1
alpha_bon: 0.05
script: surahs/Q082-al-infitar/scripts/Q082_F_01_doubled_wa_ma_adraka.py
parent_findings: H-NEW-1190
---

# Q082-F-01 — Doubled *wa-mā adrāka mā* corpus-uniqueness pre-registration

## Hypothesis

H1: Q 82 al-Infiṭār is the corpus's UNIQUE surah where the *wa-mā adrāka mā* meta-question is DOUBLED — first as *wa-mā adrāka mā yawm al-dīn* (Q 82:17) and again as *thumma mā adrāka mā yawm al-dīn* (Q 82:18) — both meta-questioning the SAME concept (*yawm al-dīn*) in immediate succession.

H1a: No other surah in the corpus contains a verse-pair where two consecutive verses BOTH meta-question the same noun-phrase via the *adrāka mā* pattern.

H1b: The doubled meta-question with *thumma* connector is corpus-EXACT in Q 82:17-18.

## Direction (LOCKED before observation)

- DOUBLED-meta-question count in Q 82 with same referent (*yawm al-dīn*): 1 (single occurrence in corpus)
- Same-verse-pattern count in any other surah: 0 (zero across the rest of the corpus)
- *thumma mā adrāka mā* construction count corpus-wide: target value = exactly 1 (Q 82:18 only)

Counter-direction (any of: doubling found in another surah, *thumma* construction found elsewhere) = NULL.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Cross-validate across all 3 tashkeel variants (no-/min-/full-) for the count.

## Operationalization

For each verse v in the corpus:
1. Detect *(wa-)mā adrāka mā* pattern: regex `(و|ف|ث|ال)?ما\s+ادراك\s+ما` on no-tashkeel string
2. Extract the meta-questioned NP (the next 1-3 words after *adrāka mā*)
3. For each (surah, verse-N, NP) triple, check whether (surah, verse-N+1, same-NP) also bears the pattern
4. Count corpus-wide hits

For *thumma mā adrāka mā*:
- regex anchored to *thumma* explicitly: `\bثم\s+ما\s+ادراك\s+ما\b`

## Success criteria

- Q 82 = 1 doubled meta-pair, all other surahs = 0 doubled meta-pairs → CONFIRMED
- *thumma mā adrāka mā* count = 1 corpus-wide (Q 82:18 only) → CONFIRMED
- Either count > 1 OR another surah has a doubling → NULL

## Failure conditions

- Doubled meta-pair found in any other surah at any concept.
- *thumma* construction found at any verse other than Q 82:18.

## Pre-commit honesty

If hypothesis fails (e.g., doubling exists elsewhere), publish as NULL with full prominence.

## Connection to existing findings

H-NEW-1190 confirmed the *wa-mā adrāka mā* 10-surah cluster (Q 69, 74, 77, 82, 83, 86, 90, 97, 101, 104; FR-cohesive at p=0.00068). This sub-finding asks the corpus-uniqueness question that H-NEW-1190 did NOT pre-register: is Q 82's DOUBLED *adrāka* construction unique? If CONFIRMED, this is a corpus-EXACT sub-pattern within the H-NEW-1190 cluster.
