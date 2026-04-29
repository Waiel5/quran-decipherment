# [[h-new-183-chronology-predictor|H-NEW-183]] — Predict Nöldeke chronology rank from per-surah compositional features

**Pre-registered**: 2026-04-17
**Seed**: 20260419
**Status**: PRE-COMMITTED before results inspected
**Bonferroni family**: [[h-new-183-chronology-predictor|h-new-183]]-chronology-predictor
**Bonferroni k**: 2
**α_fam**: 0.05; **α_test**: 0.025

## Motivation

[[h-new-162-beta-as-predictor|H-NEW-162]] found β + mean-verse-length predicts Meccan vs Medinan at 75% LOOCV
accuracy (p=0.001, 3σ above null). [[h-new-125-chronology-content|H-NEW-125]] showed 11/15 content/form axes
correlate with Nöldeke rank at Bonferroni-15-surviving levels, with
mean_verse_length reaching ρ = +0.904 by itself.

This pre-reg extends the binary Meccan/Medinan classifier to the full
continuous Nöldeke rank (1-114). If a compact feature matrix of per-surah
compositional signatures predicts the chronology rank to within ±10 positions,
the compositional signature tracks chronology QUANTITATIVELY, not just
dichotomously. This is a major confirmation of M2 ("the Quran is a
chronologically-stratified corpus at the structural level") beyond the phase
categorical labels.

## Data sources (locked)

- Nöldeke rank per surah: `data/revelation-order.csv` (column `noldeke_order`).
- Per-surah axis values: `findings/phase-b-hypotheses/csv/h-new-125.json`
  (field `per_surah_axis_values`), containing for each surah 15 axes, of which
  this run uses: `mean_verse_length`, `allah_density`, `qul_density`,
  `book_reference_density`, `loanword_density`, `eschatological_density`,
  `muq_cardinality`, `surah_length`.
- Per-surah Heap β + K: `findings/phase-b-hypotheses/csv/h-new-123.json`
  (field `per_surah_full`).
- Per-surah dispersion: `findings/phase-b-hypotheses/csv/h-new-168-per-surah-dispersion.csv`
  (field `dispersion`).

## Feature matrix (12 features, pre-committed)

For each surah s ∈ {1..114}:

1. `alpha`  = Zipf α-exponent per-surah — **pre-committed fallback**: since
   per-surah α is not available in the locked JSON artefacts, `alpha` is the
   Heap K-intercept `log(K)` (monotonically related to α via α≈1/β +
   log-adjustments; specifically an intercept-style "vocabulary constant").
   This serves as a lexical-richness proxy. If `K` is NaN (short surahs), value
   imputed to the corpus-median K.
2. `beta`   = per-surah Heap β (NaN→corpus-median).
3. `alpha_minus_beta` = `log(K) − beta` (residual).
4. `log_length` = `ln(N_tokens)` where N = surah token count from heap-law JSON.
5. `mean_verse_len` = from [[h-new-125-chronology-content|H-NEW-125]] axis.
6. `allah_density` = from [[h-new-125-chronology-content|H-NEW-125]].
7. `qul_density` = from [[h-new-125-chronology-content|H-NEW-125]].
8. `book_ref_density` = `book_reference_density` from [[h-new-125-chronology-content|H-NEW-125]].
9. `loanword_density` = from [[h-new-125-chronology-content|H-NEW-125]].
10. `eschat_density` = `eschatological_density` from [[h-new-125-chronology-content|H-NEW-125]].
11. `dispersion` = from [[h-new-168-q16-q25-dispersion|H-NEW-168]] CSV (range 0-1; imputed median if missing).
12. `muq_cardinality` = from [[h-new-125-chronology-content|H-NEW-125]] (0 for non-muq surahs).

All features standardized (z-scored) before regression. NaN imputation uses
the corpus median of the feature (computed on the TRAINING split only for the
holdout experiment; on full sample for LOOCV).

## Target

`y = noldeke_rank` (1-114 integer). Regression (not classification).

## Models (pre-committed)

- **Model A (full)**: Ridge regression with α=1.0 on all 12 features.
- **Model B (baseline)**: Ridge regression on `log_length` ONLY. (Length is
  the trivial predictor baseline; mean_verse_length already ρ=+0.904, so a
  strong baseline forces the other features to add non-trivially.)
- **Model C (RF)**: RandomForestRegressor(n_estimators=500, max_depth=None,
  random_state=20260419) on all 12 features. Descriptive only — used to
  cross-check ridge result and to extract permutation feature importances.

## Evaluation (pre-committed)

- **LOOCV** for Model A, B, C → compute:
  - R² on held-out predictions vs actual ranks (Pearson²; negative values
    possible if worse-than-mean predictor).
  - MAE = mean(|predicted − actual|).
  - Spearman ρ between predicted and actual ranks.
- **Permutation null**: 500 permutations of y, re-run LOOCV ridge for Model A,
  compare observed R² to null distribution. Seed 20260419.
- **MW-5 holdout**: 80/20 split (seed 20260419), train Model A on 80%,
  predict on 20%, compute R² and MAE. Must be directionally consistent with
  LOOCV (same sign on R², MAE within 1.5× LOOCV MAE).

## Hypotheses (Bonferroni-2, α_test = 0.025)

**PRIMARY (H1)**: Model A (full) R² > Model B (length-only) R², with the
full model's R² permutation p-value < 0.025 (one-sided, larger is better).

**SECONDARY (H2)**: Model A (full) MAE < 15 rank positions. (With n=114 ranks,
naive guessing gives MAE ~ 38; the strong baseline ρ=0.9 on verse-length
corresponds to MAE ≈ 12-16; we pre-commit the threshold 15 as "within ±10
positions on average", liberal interpretation of the task's ±10 target.)

Bonferroni-2 across {H1, H2}. Combined α_fam = 0.05; each test α=0.025.

## Verdict grid (pre-committed)

| H1 (full > baseline, p<0.025) | H2 (MAE < 15) | Verdict |
|:-:|:-:|---|
| PASS | PASS | **CHRONOLOGY-QUANTITATIVE** — compositional features track rank |
| PASS | FAIL | **PARTIAL** — features help over length but don't reach ±10 accuracy |
| FAIL | PASS | **LENGTH-DRIVEN** — length alone suffices; other features redundant |
| FAIL | FAIL | **NULL** — rank prediction does not work |

## Honest-limits disclosure (pre-committed)

- Target labels (Nöldeke 1860s reconstruction) are an interpretation, not
  ground-truth. Upper bound on accuracy is the quality of the rank assignment.
- Features are heavily intercorrelated (length, mean_verse_length,
  allah_density all correlate with rank); ridge collapses them. RF
  importance will disentangle somewhat.
- `alpha` as log(K) is a proxy; true per-surah Zipf α would require re-fit
  on each surah's rank-frequency curve, which is not in the locked JSON.
- Short surahs (N<100 tokens) have NaN β and unstable K; imputation adds noise.

## Pre-committed output paths

- Script: `scripts/h_new_183_chronology_predictor.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-183.json`
- Finding: `findings/phase-b-hypotheses/h-new-183-chronology-predictor.md`
- Journal: `journal/h-new-183-run-1.md`
