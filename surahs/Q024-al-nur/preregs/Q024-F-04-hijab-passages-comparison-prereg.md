---
finding_id: Q024-F-04
title: "Q 24:30-31 vs Q 33:53-59 — the two 'hijab passages' lexical comparison"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 2024
direction: descriptive (no direction-of-effect locked)
---

# Q024-F-04 — The two "hijab passages" lexical comparison

## Hypothesis

The Quran has two passages classically labeled "hijab verses": Q 24:30-31 (the gaze-modesty + khimār verses) and Q 33:53-59 (the wives-of-the-Prophet ḥijāb-curtain). Despite both being labeled "hijab passages," they are lexically distinct: their root-Jaccard overlap is below 0.30 (i.e., they share less than 30% of their distinct roots).

## Sub-hypothesis

The actual word *ḥijāb* (root *Ḥjb*) appears only in Q 33:53, NOT in Q 24:30-31. The word *khimār* / *khumur* (root *xmr*) appears only in Q 24:31, NOT in Q 33:53-59.

## Rules-tuple

`(no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan)`

## Direction-locked

- Direction A: Jaccard(Q24:30-31, Q33:53-59) < 0.30. CONFIRMS the lexical-distinction claim.
- Direction A: 0.30 ≤ Jaccard < 0.50. DIRECTIONAL.
- Direction A: Jaccard ≥ 0.50. NULL on lexical distinction.

- Direction B: Q 24:30-31 contains *xmr*, Q 33:53-59 does NOT. CONFIRMS asymmetric khimar.
- Direction C: Q 33:53-59 contains *Ḥjb*, Q 24:30-31 does NOT. CONFIRMS asymmetric hijab.

## Output

- Pre-reg: this file.
- Script: `scripts/Q024_F_04_hijab_passages.py`.
- JSON: `csv/Q024-F-04.json`.
