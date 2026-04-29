---
test_id: Q002-F-05
title: Q 2:282 (āyat al-dayn / debt-contract verse) — extreme-length distinctness vs all 6,236 verses
target_claim: Classical commentaries (al-Qurṭubī, al-Ṭabarī) note Q 2:282 is the longest verse in the Quran (āyat al-dayn). We test: how statistically extreme is its length, and is its length-rank consistent with a content-based vs random-fluctuation explanation?
date_locked: 2026-04-28
phase: B+
status: PRE-REGISTERED
seed: 20260428
---

# Pre-registration — Q002-F-05: Q 2:282 length extremity

## 1. Hypothesis (LOCKED)

**H1**: Q 2:282 is rank 1 of 6,236 verses by word-count (no-tashkeel) AND its length-z-score (z = (length - corpus_mean) / corpus_sd) > 8.0.

**H0**: rank > 1 OR z ≤ 8.0.

**Direction (LOCKED)**: rank=1 AND extreme-z.

## 2. Operationalisation

- Word count = whitespace-tokenization on no-tashkeel (post-sajda-mark removal).
- corpus_mean and corpus_sd over all 6,236 verses.

## 3. Distinctness control

Compare to:
- 2nd-longest verse: gap = (length_Q2:282 - length_2nd) / sd. Pre-registered threshold: gap > 5σ would be "uniquely-long" by length-distribution.

## 4. Success / failure

- **VINDICATED**: rank=1, z>8, gap>5σ.
- **DIRECTIONAL**: rank=1, z≤8 OR gap ≤ 5σ.
- **NULL**: rank > 1.

## 5. MW-3: alternative metric (letter count)

Also compute by letter-count (no-tashkeel, no-spaces) — does Q 2:282 still rank 1?

## 6. Output paths

- Script: `/Users/grey/Downloads/quran/scripts/Q002_F_05_q2_282_length.py`
- JSON: `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/csv/Q002-F-05.json`
- Findings: `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/Q002-F-05-q2-282-length.md`

*Locked 2026-04-28.*
