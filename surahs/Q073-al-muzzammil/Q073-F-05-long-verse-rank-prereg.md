---
surah: 73
test_id: Q073-F-05
title: Q 73:20 "the long verse" corpus-rank distinction within Early-Meccan / non-muq surahs
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q073-F-05-long-verse-rank
alpha_bon: 0.025
---

# Q073-F-05 — Pre-registration: Q 73:20 "the long verse" corpus-rank distinction within Early-Meccan / non-muq surahs

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** Q 73:20 is in the **top-25** longest verses of the entire corpus (rank ≤ 25 out of 6,236).

**H1b (one-tailed, locked direction):** Among Early-Meccan surahs (Nöldeke phase I, per `data/revelation-order.csv`), Q 73:20 is the **maximum-length verse** (rank 1 within Early-Meccan).

**H0:** Q 73:20 is below corpus rank 25 OR not the max-length within Early-Meccan.

**Direction:** Q 73:20 is an EXTREME OUTLIER in length within its chronological cohort (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json`.
- **Length metric**: **word count** (whitespace-tokenized after harakat-stripping).
- **Early-Meccan reference**: `data/revelation-order.csv`, filter `noldeke_phase == 'Early Meccan'`.

## 3. Test statistic

- L_q73v20 = word-count of Q 73:20.
- corpus_rank = rank of Q 73:20 in descending order of all 6,236 verses by word-count.
- early_meccan_rank = rank of Q 73:20 within Early-Meccan verses only.

## 4. Permutation null

H1a: a corpus-rank claim is a categorical lookup, not stochastic. Threshold: rank ≤ 25 (in top 0.4% of 6,236). Single-test α = 0.05 (descriptive).

H1b: same — categorical comparison among Early-Meccan verses (a fixed subset). Threshold: rank = 1.

(No permutation null is needed for descriptive corpus-rank lookups; PASS is observed-as-expected.)

## 5. Success / Failure

- **CONFIRMED**: H1a AND H1b both pass.
- **DIRECTIONAL**: H1a only (corpus-extreme but not Early-Meccan-extreme — possible if a Q 17 Late-Meccan/early-Medinan verse is longer).
- **NULL**: H1a fails (Q 73:20 not in top-25 corpus-wide).
- **PRE-COMMIT VIOLATION**: Q 73:20 is below the median verse-length (extremely unlikely given the brief; flagged anyway).

## 6. Honest limits known a priori

- The brief states "Q 73:20 is the long verse" — a classical descriptor. This test asks whether the descriptor is empirically supported at the rank-extremum level, OR whether it's simply "long for an Early-Meccan surah" (a relative descriptor).
- Q 2:282 (the longest verse in the corpus, the *āyat al-dayn* / debt-verse) is over 130 words — this is the **corpus rank-1**. Q 73:20 cannot be rank-1 corpus-wide. The H1a question is whether it's in the top-25 (≈ top 0.4%).
- Most Early-Meccan surahs are short with short verses (cf. Q 91 al-Shams, Q 99 al-Zalzala, Q 100 al-ʿĀdiyāt, Q 103 al-ʿAṣr). Q 73:20 being an Early-Meccan max-length verse is a notable architectural feature — Q 73 itself is short (20 verses) but its v.20 is exceptionally long. This is a distinctive **internal-asymmetry** signature.

## 7. Pre-commit attestation

- The descriptor "the long verse" is a fact of pre-flight observation; the corpus rank computation is locked at run-time without prior peek.
- No corpus-wide ranking of Q 73:20 has been computed by this specialist before lock.

## 8. Decision rule

1. Tokenize all 6,236 verses by whitespace; compute word-count.
2. Rank descending; locate Q 73:20.
3. Filter Early-Meccan subset (per Nöldeke csv); rank within.
4. Apply success matrix.

## 9. Bonferroni declaration

- bonferroni_k = 2 (H1a, H1b).
- bonferroni_family = Q073-F-05-long-verse-rank.
- alpha_bon = 0.025 per axis (descriptive — α threshold not strictly applied since no perm null).

## 10. Connection to existing findings

- **H-NEW-700** (rhyme-distribution): Q 73 has 90% alif-rhyme dominance (20 verses). Q 73:20 is included in the alif-rhyme stream.
- **H-NEW-66** (verse-twin network): Q 2:282 (corpus rank-1 in length, the *āyat al-dayn*) is a major attractor (24 connections per H-NEW-66). Q 73:20 may be similarly hub-like in terms of within-surah length anomaly.
- **H-NEW-1300** (IMPV-qrA): Q 73:20 contains 2 of the 6 corpus IMPV-qrA segments. Its length and concentration of imperative-imperatives makes it a candidate "concentrated injunction" verse — testing whether the LENGTH itself is the structural marker.
