---
surah: 60
test_id: Q060-F-01
title: Q 60 fits the H-NEW-1080 short-Medinan FR cluster — embedding test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q060-F-01-block-embedding
alpha_bon: 0.05
---

# Q060-F-01 — Pre-registration: Q 60 short-Medinan-block embedding test

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction LOWER):** Q 60's mean Fisher-Rao distance to the other 9 members of the H-NEW-1080 short-Medinan block (Q 57-66) is **lower** than the mean distance from Q 60 to a random 9-subset of the rest of the corpus.

**H0:** Q 60's mean to the cluster ≥ mean to a random 9-subset.

**Direction:** LOWER (Q 60 is a member of, not an outlier to, the short-Medinan cluster).

## 2. Operational definition

- **Source matrix**: `findings/phase-b-hypotheses/csv/h-new-111.json` (treated as fixed ex-ante under MW-6).
- **Cluster definition**: H-NEW-1080 (Q 57-66, ten consecutive Medinan surahs, the canonical "qiṣār al-Madanī" classification per al-Suyūṭī *al-Itqān*).
- **Test statistic**: mean Fisher-Rao distance from Q 60 to the OTHER 9 cluster members (i.e., {Q 57, 58, 59, 61, 62, 63, 64, 65, 66}).
- **Null model**: 10,000 random draws of a 9-element subset from {1..114}\{60}; for each draw, compute mean FR distance from Q 60 to the random 9.

## 3. Permutation null

- n_perm = 10,000
- seed = 20260509
- one-tailed lower-side p-value = (# null draws where mean ≤ observed) / n_perm

## 4. Decision rule

- **PASS**: p ≤ α_bon = 0.05
- **NULL**: p > 0.05

This is a single test (k=1), no Bonferroni adjustment needed; α_bon = 0.05.

## 5. Pre-commit violation handling

If observed mean is HIGHER than null mean (direction reversed), the result is filed as DIRECTION-REVERSED-NULL with full disclosure. No silent flip.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, FR-content-feature, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Auxiliary descriptive (not part of primary test)

- Q 60's rank within the 10-member cluster (sorted by mean-to-others-in-cluster) is reported descriptively.
- Q 60's substitutability rank against all 104 non-cluster surahs is reported descriptively.

These are NOT formal hypotheses; they characterize Q 60's position within the cluster.

## 8. Coordination

This test extends the H-NEW-1080 cluster-cohesion finding (CONFIRMED at p=0.049) by asking the per-member question for Q 60 specifically. No other Q 60 specialist test depends on the outcome.

## 9. SHA256 lock

The locked text of this pre-reg file is hashed at completion-time and included in the result JSON.
