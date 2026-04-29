---
finding_id: Q055-F-02
title: Dual-pronoun *kumā* / *humā* density audit
phase: B+
date_locked: 2026-04-28
seed: 20260428
bonferroni_k: 2  # (kumā-only, dual-total)
alpha_bon: 0.025
script: surahs/Q055-al-rahman/scripts/Q055_F_02_kuma_density.py
---

# Q055-F-02 — kumā density pre-registration

## Hypothesis

Q 55, owing to its dual-jinn-and-mankind address (per the classical interpretation of *rabbikumā*), has the highest density of dual-form pronominal suffixes in the corpus. We measure word-final attachments `-كما` and `-هما`.

## Direction (LOCKED)

- Q 55 corpus-#1 in kumā-density per 100 words.
- Q 55 also corpus-#1 in dual-total density (kumā + humā) per 100 words.

Counter-direction (Q 55 not top-3 in either metric) = NULL.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, Hafs-Kufan)`. Diacritics stripped; alif normalized; word-final-suffix-only counts (token must end in كما / هما and be longer than 3 chars to avoid bare pronouns).

## Success criteria

- Q 55 rank=1 in kumā-density → CONFIRMED
- Q 55 rank ∈ {2, 3} → DIRECTIONAL
- Q 55 rank > 3 → NULL
