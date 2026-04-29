---
surah: 1
test_id: Q001-F-03
title: Q 1 rhyme entropy compared to other 7-verse surahs and short-surah baseline
file_type: pre-registration
date_locked: 2026-04-28
seed: 14103
---

# Q001-F-03 — Pre-registration: Rhyme-entropy of Q 1 vs short-surah baseline

## 1. Hypothesis

**H1 (two-tailed):** Q 1's rhyme entropy (0.683 nats, per H-NEW-750) is DIFFERENT from the corpus distribution of short surahs (≤10 verses).

We do not pre-commit a direction — Q 1 may be unusually unified (low entropy → "more chiastic") or unusually diverse (high entropy → "richer rhyme palette"). HONESTY: both Wikipedia/classical descriptions emphasize Q 1's unified -m / -n / -īn rhyme; one might have predicted LOW entropy. Empirically Q 1 is 0.683 — moderate.

## 2. Comparison set

- Set A: All surahs with ≤10 verses (call this "short-surah baseline"). N ~ 30-40 surahs from Q 87-114 region.
- Set B: All surahs with EXACTLY 7 verses. By inspection, only Q 1 and Q 107 — too small for stats. Report as descriptive only.

## 3. Test

For each surah in set A, the rhyme-entropy is taken from H-NEW-750 (`per_surah` field). Compute:
- z-score of Q 1's entropy in set A.
- Two-tailed p-value (Gaussian approximation + bootstrap).

## 4. Success / Failure

- DIRECTIONAL_DISTINCT: |z| > 1.5 → Q 1 is materially distinctive.
- NULL: |z| ≤ 1.0 → Q 1 is typical of short surahs.

## 5. Rules-tuple

- Tashkeel: min-tashkeel (rhyme-relevant)
- Token: final-letter of last verse-word
- Counting unit: verse
- Basmala: counted as V1 in Q 1
- Reading: Hafs-Kufan

## 6. Pre-commit guardrails

Direction is two-tailed; pre-committed.
