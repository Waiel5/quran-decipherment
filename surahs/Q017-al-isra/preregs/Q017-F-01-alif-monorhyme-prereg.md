---
id: Q017-F-01
title: Q 17 al-Isrāʾ alif-monorhyme purity — corpus rank verification
date_locked: 2026-04-28
phase: B+
seed: 20260428
rules_tuple: (min-tashkeel, orthographic-token, last-letter-of-verse-after-stripping-final-mark, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q017-F-01 — Alif-monorhyme purity, Q 17 corpus rank (PRE-REG)

## Hypothesis (locked direction)

Q 17 al-Isrāʾ has alif-final-letter rate ≥ 0.99 and ranks within the top-10 surahs by alif-final purity, alongside Q 18 al-Kahf and the alif-monorhyme cluster identified in Q033-F-01.

Direction: Q 17 alif-rate ∈ [0.99, 1.0]; corpus rank ≤ 10.

## Method

1. Load `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json`.
2. For each surah, for each verse: strip tashkeel marks (ـ ً ٌ ٍ َ ُ ِ ّ ْ ٰ) and Quran-marks (pause marks ۖ ۚ ۗ etc.); take the last Arabic letter character.
3. Define alif-finals as `{ا, آ, أ, إ, ى, ٰ}` — alif-shaped graphemes that mark the *-ā* / *-ī* (alif maqṣūra) rhyme.
4. Compute alif-final-rate per surah = count(alif-final verses) / count(verses).
5. Rank all 114 surahs.
6. Compare with Q 33 al-Aḥzāb (rank 11, 0.9863) and Q 18 al-Kahf (rank 1, 1.0000) baselines from Q033-F-01.

## Success criteria

- DIRECTIONAL VINDICATION: Q 17 rate ∈ [0.99, 1.00] AND rank ≤ 10.
- TIED-VINDICATION: rate = 1.000 (perfect monorhyme) — still vindicated under direction.
- DIRECTIONAL FALSIFICATION: rate < 0.99 OR rank > 10.

## Bonferroni

Single direction-of-effect test (k=1) — α=0.05.

## NULL

Direction reversed = published as NULL with full prominence. The pre-computed sig_A=−2.40 in H-NEW-750 is consistent with high alif-purity (high *top_final_letter_frac* drives low rhyme entropy, which drives low sig_A); this prereg verifies that empirical anchor.

## Cross-corpus reference

Compare Q 17 to Q 33 (98.6%, rank 11) and to Q 18 (100%, rank 1). Q 17 is canonically adjacent to Q 18 — does the alif-monorhyme purity transition smoothly across the Q 17 → Q 18 mushaf boundary? (Q17-Q18 TSP-cost is 0.028, lowest in Q's neighborhood per H-NEW-720.)
