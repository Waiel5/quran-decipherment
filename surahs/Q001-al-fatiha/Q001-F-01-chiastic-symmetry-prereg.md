---
surah: 1
test_id: Q001-F-01
title: Chiastic-symmetry score for Q 1 al-Fātiḥa
file_type: pre-registration
date_locked: 2026-04-28
seed: 14101
---

# Q001-F-01 — Pre-registration: Chiastic-symmetry score

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Q 1 al-Fātiḥa exhibits chiastic (ABCBA) word-overlap symmetry. The pairwise word-overlap between mirrored verse-pairs (V1↔V7, V2↔V6, V3↔V5) — measured as Jaccard on word-stems — is HIGHER than expected under a within-surah random-pairing null.

**H0:** Mirrored-pair Jaccard mean = random-pair Jaccard mean.

**Direction:** Mirrored > Random (LOCKED).

## 2. Test statistic

For Q 1 (no-tashkeel, orthographic-token, basmala-counted-as-V1):
- M_obs = mean over the three mirror pairs (V1,V7), (V2,V6), (V3,V5) of Jaccard(word-set, word-set).
- V4 acts as the pivot (excluded from pairings).

## 3. Null distribution

Permutation null: enumerate ALL non-mirror pairings of the 6 non-pivot verses {V1..V3,V5..V7} into 3 unordered pairs. Total pairings of 6 items into 3 unordered pairs = 15. The mirror pairing is one of 15.

For each pairing, compute mean Jaccard. Rank M_obs in this distribution.

Permutation p-value = (rank of M_obs from top) / 15.

## 4. Success / Failure

- Success (signal): M_obs is in the TOP-2 of 15 (one-tailed p ≤ 2/15 ≈ 0.133). Not classically "significant" but informative given finite null.
- Strict success: M_obs is the SINGLE TOP value (p ≤ 1/15 ≈ 0.067).
- Failure: M_obs is below the median rank (rank > 8 of 15).

## 5. Auxiliary tests (descriptive, not gate)

A. Letter-overlap version: Jaccard on character sets, same null.
B. Theme-anchor: count shared **stems** in classical morphology root-mapping.

## 6. Rules-tuple (LOCKED)

- Tashkeel: no-tashkeel
- Token: orthographic-word (split on whitespace)
- Counting unit: word
- Basmala: counted as V1 of Q 1 (Hafs)
- Reading: Hafs-Kufan
- Script: Mashriqi

## 7. Pre-commit guardrails

- Direction is fixed BEFORE running the script.
- The script is run ONCE; no parameter tuning post-observation.
- Both the strict-rank and the auxiliary letter-test results are reported.

## 8. Bonferroni

This is a single primary test. Auxiliary tests carry post-hoc α-cap (MW-7).
