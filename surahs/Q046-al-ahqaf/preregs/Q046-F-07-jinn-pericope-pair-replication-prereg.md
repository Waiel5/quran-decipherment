---
prereg_id: Q046-F-07
title: Q 46:29-32 jinn-pericope ↔ Q 72:1-19 root-Jaccard pair (Q072-F-03 replication)
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q046-F-07 — Q 46-jinn-pericope ↔ Q 72-jinn-surah replication

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The 4-verse pericope **Q 46:29-32** (the jinn-listening-to-Quran pericope) shares **higher root-Jaccard overlap with Q 72** (al-Jinn, 28 verses) than with random length-matched verse-blocks from the rest of the corpus (10000-permutation null).

This replicates the Q072-F-03 jinn-pericope-pair test from the Q 46 direction. The brief explicitly flags this as a cross-direction replication of Q072-F-03.

## 2. Null / negation

**H0**: Q 46:29-32 ↔ Q 72 Jaccard is ≤ the null distribution median.

## 3. Operationalization

- Source: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4) for stem-roots; `quran-text/quran-no-tashkeel.json` for verse indices.
- Pericope: Q 46:29-32 (4 verses) — root-set extracted.
- Target: Q 72 root-set (full 28-verse surah).
- Observed metric: Jaccard(P_4646:29-32, Q72) = |A ∩ B| / |A ∪ B|.
- Null: 10000 permutations sampling 4 contiguous verses from non-Q72 non-Q46 surahs with ≥4 verses; compute Jaccard against Q 72's root-set.
- One-sided upper-tail p = (# null Jaccards ≥ observed) / 10000.

## 4. Direction lock

Pre-committed: **observed > null median**.

## 5. Bonferroni

k=3 (Q 46 family). α_corrected = 0.0167.

## 6. Success / failure criteria

- **PASS-DIRECTED** (replicates Q072-F-03): p < 0.0167 AND observed > null median.
- **DIRECTIONAL**: observed > null median, p ≥ 0.0167.
- **NULL**: observed ≤ null median (would weaken the Q072-F-03 finding by failing the cross-direction replication).

## 7. Seed

`20260509`. `n_perm = 10000`.

## 8. Output

JSON to `csv/Q046-F-07.json`: pericope_roots, q72_roots, observed_jaccard, null_stats, p_one_sided, replicates_Q072_F_03 (bool), verdict.

## 9. Rationale

Q 46:29-32 and Q 72 are the corpus's two jinn-listening-to-Quran loci. Q072-F-03 (Q 72 specialist) confirmed pair-tightness from the Q 72 direction; this is the inverse-direction MW-5 (replication) test. Failure here would weaken the cross-finding; success would lock the jinn-pair as one of the strongest cross-surah verse-pericope pairs in the corpus.

## 10. Honest limits

- The 4-verse pericope is short; root-set Jaccard is sensitive to small variations.
- Q 72 is short (28 verses); the comparison-corpus is therefore mostly larger surahs.
- The sampling null draws contiguous 4-verse blocks; non-contiguous shuffle null would be a stronger control but is not run here (would belong in a follow-up).
