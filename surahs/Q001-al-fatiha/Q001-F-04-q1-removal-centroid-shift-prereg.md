---
surah: 1
test_id: Q001-F-04
title: FR-centroid shift under Q 1 removal — empirical "umm al-Kitāb" probe
file_type: pre-registration
date_locked: 2026-04-28
seed: 14104
---

# Q001-F-04 — Pre-registration: Centroid-shift on Q 1 removal

## 1. Hypothesis

**H1 (two-tailed):** Q 1 al-Fātiḥa is the most "centroidal" surah in Fisher-Rao stem-root distance space (per H-NEW-111). Therefore, removing Q 1 from the corpus shifts the corpus mean-pairwise-distance MORE than removing any other randomly-chosen surah of comparable size.

**H1 — refined statistic:** mean-pairwise-distance on the 113-surah remaining set, after removing each candidate surah X. We pre-commit:
- Q 1's d̄_113 (mean over the 113×112/2 = 6328 remaining pairs) will be in the BOTTOM-3 across all 114 candidate-removals (i.e., its removal lowers corpus mean distance the most → Q 1 acts as a centroid-anchor that pulls other surahs toward it).

Direction: LOCKED. Q 1 → bottom-3 rank.

## 2. Test statistic

Let D be the 114×114 FR distance matrix (from h-new-111.json). For each surah X ∈ {1..114}:
- d̄(X) = mean of D[i,j] for i<j, i ≠ X, j ≠ X.

Rank d̄(X) ascending; smaller = removing X causes the biggest "shrink" of corpus mean.

## 3. Null prediction (corpus-prior)

Under uniform null, rank of Q 1 ~ Uniform(1..114). p(Q 1 in bottom-3) = 3/114 ≈ 0.026.

## 4. Success / Failure

- VINDICATED: Q 1 is in bottom-3 (p=0.026, single-test).
- DIRECTIONAL: Q 1 is in bottom-10 (p=0.088).
- NULL: Q 1 is not in bottom-10.

## 5. Rules-tuple (LOCKED)

- Tashkeel: no-tashkeel (FR-roots default)
- Token: stem-root (QAC v0.4)
- Counting unit: probability vector over root frequencies
- Basmala: counted only in Q 1
- Reading: Hafs-Kufan
- Distance: Fisher-Rao on probability simplex
- Source: pre-computed h-new-111.json D_matrix_upper_triangular

## 6. Pre-commit guardrails

Direction LOCKED. Single-test α=0.05. We use h-new-111.json's pre-computed matrix — no re-derivation.

## 7. Note on prior

The H-NEW-750 row for Q 1 already reports mean_content_distance = 0.7789, vs corpus mean 0.9235 (from h-new-111). This is descriptive — Q 1 is BELOW the corpus mean. The current test asks whether Q 1's CENTRALITY (low mean distance to others) makes Q 1 the most centroid-anchoring surah, NOT just whether Q 1's own mean-distance is low (we already know that).
