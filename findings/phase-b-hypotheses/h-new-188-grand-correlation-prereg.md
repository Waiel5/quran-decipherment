---
id: H-NEW-188
title: Grand correlation/covariance matrix of all per-surah structural measures + factor analysis
phase: B
status: PRE-REG (execution pending)
date: 2026-04-17
executed_by: autonomous-agent
seed: 20260419
bonferroni_k: 2
bonferroni_family: h-new-188-grand-correlation
alpha_bon: 0.025
parents: H-NEW-172 (α), H-NEW-159 (β), H-NEW-163 (dispersion), H-NEW-125 (all content-axes per-surah), H-NEW-141 (Pattern-B within-Late-Meccan NULL)
---

# [[h-new-188-grand-correlation|H-NEW-188]] — Grand correlation matrix of per-surah measures

## Hypothesis

Across all 114 surahs, a single correlation/covariance matrix over ~16 structural
measures will reveal:
1. Loading patterns that define a small number of interpretable latent factors
   (top-3 factors explain ≥ 50 % of variance).
2. The Pattern-B bundle (qul + book_reference + eschatological + loanword + muq_cardinality)
   will load jointly on one factor with average |loading| > 0.4 — i.e. the bundle
   is a coherent factor corpus-wide, even though within-Late-Meccan it is
   incoherent ([[h-new-141-pattern-b-within-late-meccan|H-NEW-141]] NULL).

## Pre-registered tests (bonferroni_k = 2)

1. **Factor analysis loading patterns** — PCA on 114×M standardized feature matrix;
   inspect top-3 components. Report loadings, % variance, hierarchical clustering of
   features by 1−|r|. Descriptive but pre-registered as primary.

2. **Pattern-B bundle coherence** — test whether the 5 Pattern-B axes cluster
   together (projection onto any single principal component: mean absolute loading
   |L̄| > 0.4 for the 5 axes on a shared top-3 PC).
   Null: random 5-axis subset mean |L̄| (10 000 permutations of 5 axes drawn from M).
   PASS if observed |L̄| exceeds 95th percentile of null (one-sided).

## Data sources

- [[h-new-125-chronology-content|H-NEW-125]] JSON (`findings/phase-b-hypotheses/csv/h-new-125.json`):
  per-surah values for 15 axes — surah_length, mean_verse_length, muq_cardinality,
  allah_density, qul_density, prophet_narrative_density, legal_term_density,
  eschatological_density, book_reference_density, oath_density, divine_name_density,
  personal_pronoun_density, rhyme_letter_diversity, refrain_density, loanword_density,
  plus noldeke_rank (auxiliary).
- [[h-new-172-zipf-per-chapter|H-NEW-172]] per-surah CSV — α (zipf), β (Heap), dispersion.
- [[h-new-168-q16-q25-dispersion|H-NEW-168]] per-surah CSV — dispersion for all 114 (fallback).

Derived feature list (M = 18):
surah_length, mean_verse_length, muq_cardinality, allah_density, qul_density,
prophet_narrative_density, legal_term_density, eschatological_density,
book_reference_density, oath_density, divine_name_density, personal_pronoun_density,
rhyme_letter_diversity, refrain_density, loanword_density, alpha_zipf, beta_heap,
dispersion, noldeke_rank.

Handling of missing α/β: retain rows with missingness; use pairwise-complete
Pearson correlations. For PCA, use median-imputation within feature; sensitivity
analysis: listwise-complete (drop any surah with any NaN).

## Analysis

- Pearson correlation matrix (pairwise-complete), Spearman sensitivity.
- Hierarchical clustering by 1 − |r| with complete-linkage.
- PCA via SVD on z-scored (median-imputed) matrix; eigenvalues, cumulative
  variance, top-3 component loadings.
- Pattern-B bundle: among each of PC1, PC2, PC3, compute mean absolute loading
  of the 5 bundle axes; report max across the three PCs. Null via 10 000
  random 5-axis draws from M = 19 features (or M − {bundle-axis}).

## Pre-registered predictions

- Length axes (surah_length, mean_verse_length, α, β, dispersion) form a
  clear "size/compositional" factor (expected).
- Pattern-B bundle coherence (corpus-wide): agnostic. [[h-new-141-pattern-b-within-late-meccan|H-NEW-141]] found NULL
  within Late-Meccan; prediction here is tentative PASS corpus-wide because
  Nöldeke-rank is a known latent driver of several Pattern-B axes.

## Deliverables

- `findings/phase-b-hypotheses/csv/h-new-188.json` — full numeric output
- `findings/phase-b-hypotheses/csv/h-new-188-corrmatrix.csv` — Pearson matrix
- `findings/phase-b-hypotheses/csv/h-new-188-loadings.csv` — PC loadings
- `findings/phase-b-hypotheses/h-new-188-grand-correlation.md` — narrative write-up
- Seed: 20260419

## Garden-of-forking-paths log

- Feature set frozen at 19 axes above before execution.
- Pairwise-complete used as primary (most surahs retain valid values for content axes;
  only α/β miss 21/35 surahs).
- Standardization: z-score across surahs. Imputation: feature median.
- Factor method: PCA (SVD). Rotation: none for primary; varimax as sensitivity.
- Bundle test on max-over-PC1..PC3 pre-registered, to avoid cherry-picking a single PC.
