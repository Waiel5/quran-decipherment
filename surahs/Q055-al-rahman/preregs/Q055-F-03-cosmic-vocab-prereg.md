---
finding_id: Q055-F-03
title: Cosmic-vocabulary density audit
phase: B+
date_locked: 2026-04-28
seed: 20260428
bonferroni_k: 6
alpha_bon: 0.0083
script: surahs/Q055-al-rahman/scripts/Q055_F_03_cosmic_vocab.py
---

# Q055-F-03 — Cosmic-vocabulary density pre-registration

## Hypothesis

The classical reading of Q 55 as the corpus's most "cosmic" surah (a creation-as-mercy hymn) predicts unusually high density of cosmic lemmas: samāʾ, arḍ, shams, qamar, najm, baḥr.

## Direction (LOCKED)

- Q 55 ranks corpus top-3 in summed cosmic density per 100 words.

Counter-direction (Q 55 not top-3) = NULL.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, Hafs-Kufan)`. Surface-form match: token's prefix (after stripping وفبكل / ال) starts with the lemma stem; token length ≤ stem-length + 4.

## Family

6 lemmas → Bonferroni α = 0.05/6 = 0.0083 for any per-lemma density claim. The OVERALL composite-density rank does NOT need Bonferroni (single test).

## Success criteria

- Q 55 rank ∈ {1, 2, 3} → CONFIRMED
- Q 55 rank ∈ {4, ..., 10} → DIRECTIONAL
- Q 55 rank > 10 → NULL
