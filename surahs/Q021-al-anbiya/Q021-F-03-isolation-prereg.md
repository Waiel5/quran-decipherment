---
surah: 21
test_id: Q021-F-03
title: True-isolate lexical dispersion — Q 21's mean FR-distance to its 5 nearest neighbors vs corpus
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 1
bonferroni_family: Q021-F-03-isolation-single-cell
alpha_bon: 0.05
direction: HIGHER (Q 21 mean d-to-5-nearest > corpus median)
---

# Q021-F-03 — Pre-registration: Q 21 lexical-isolation test

## 1. Hypothesis (locked)

**H1 (one-tailed, locked):** Q 21's mean Fisher-Rao (root-bag) distance to its 5 nearest neighbors among the 113 other surahs is **HIGHER than the corpus median** of the same metric — i.e., Q 21 is more *lexically isolated* (its closest neighbors are farther away) than half the corpus.

**H0:** Q 21's mean-d-to-5-nearest is at or below the corpus median.

**Direction (LOCKED):** Q 21 ∈ top-half (HIGHER d) on the *lexical isolation* metric.

This test independently checks the H-NEW-126 "true-isolate" classification. If Q 21 is truly lexically isolated, it should empirically rank above the corpus median on this metric.

## 2. Disclosure

The author has NOT yet computed Q 21's mean-d-to-5-nearest. Direction is locked above. The author has computed the H-NEW-590 outlier-strength and H-NEW-750 mean_content_distance for Q 21 (both are mid-corpus, not extreme), but the mean-d-to-5-nearest specifically has not been computed.

## 3. Operational definition

**Pipeline** (replicates H-NEW-111 methodology):
- Per-surah QAC v0.4 STEM ROOT counts.
- Top-K=500 root selection (matches H-NEW-111 lock).
- Dirichlet-α=0.5 smoothing.
- L1-normalize to probability vectors.
- Pairwise Fisher-Rao distance: d(p, q) = 2·arccos(Σ √(p_i · q_i)).
- Per-surah, compute mean-d-to-5-nearest-neighbors (excluding self).
- Test statistic: Q 21's rank on this metric vs the 114-element distribution.

## 4. Test statistic

- **Primary**: Q 21's percentile rank on `mean_d_to_5_nearest`.
- **Secondary**: Q 21's absolute mean-d-to-5-nearest value, with corpus median for reference.

## 5. Success / Failure criteria (Bonferroni k=1, α = 0.05)

- **Strict success (CONFIRMED)**: Q 21 is in the top-30 most-isolated surahs (≥ 73 percentile).
- **DIRECTIONAL**: Q 21 in top-half (> 50 percentile).
- **NULL**: Q 21 ≤ 50 percentile (Q 21 is *not* lexically isolated; the H-NEW-126 true-isolate label is structurally-cluster-based, not lexically-distance-based).
- **Pre-commit violation**: Q 21 in bottom-30 (≤ 27 percentile, very-low-isolation pole).

## 6. Honest limits known a priori

- "Lexical isolation" measured by mean-d-to-5-nearest is one of several reasonable isolation metrics. Alternatives include: median-d-to-corpus, max-similarity-to-any-other-surah, sum of TSP-adjacency-costs to neighbors. The pre-reg locks the *mean-d-to-5-nearest* operationalization specifically.
- The H-NEW-126 true-isolate classification is *cluster-system-invariance*-based ("invisible to all 20 cluster-detection systems"), not *distance*-based. Q 21 could pass H-NEW-126 (cluster-invisible) while failing Q021-F-03 (distance-non-isolated). The two tests probe different facets of "isolation".
- The test runs FR distance on top-K=500 STEM roots. Other rule-tuples (top-K=100, top-K=1000, char-4-gram) are NOT tested in this single-cell pre-reg; rules-tuple-fragility is not certified by this test.

## 7. Rules-tuple

`(QAC-v0.4-STEM-roots, top-K=500, Dirichlet-α=0.5, L1-normalize, Fisher-Rao, no-tashkeel)`.

## 8. SHA256 lock

To be computed at runtime by `scripts/Q021_F_03_isolation_test.py`. Embedded in script and verified at execution.
