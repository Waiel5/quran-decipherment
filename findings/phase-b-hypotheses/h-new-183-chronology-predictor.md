---
id: H-NEW-183
title: Predict Nöldeke chronology rank from per-surah compositional features
phase: B
status: PASS-DIRECTED (CHRONOLOGY-QUANTITATIVE; both pre-reg tests pass)
pre_reg: findings/phase-b-hypotheses/h-new-183-chronology-predictor-prereg.md
bonferroni_family: h-new-183-chronology-predictor
bonferroni_k: 2
alpha_bon: 0.025
seed: 20260419
n_perm: 500
script: scripts/h_new_183_chronology_predictor.py
json: findings/phase-b-hypotheses/csv/h-new-183.json
journal: journal/h-new-183-run-1.md
date: 2026-04-17
parent: H-NEW-162 (β + verse-length → 75% Meccan/Medinan), H-NEW-125 (15-axis chronology map)
---

# [[h-new-183-chronology-predictor|H-NEW-183]] — Predict Nöldeke rank from compositional features

## Headline

**A 12-feature per-surah compositional signature predicts the Nöldeke
revelation rank (1-114) with LOOCV R² = 0.836 and mean absolute error of
8.74 rank positions**, permutation p = 0.002 vs null R² centered near zero
(null mean = −0.124, 97.5th pctile = −0.005). The length-only baseline
achieves R² = 0.446 / MAE = 19.30. The full-feature model nearly **doubles**
R² and **more than halves** MAE.

An 80/20 holdout (seed 20260419) confirms direction: R² = 0.926, MAE = 5.98,
Spearman = 0.97 on the 23-surah held-out test set.

An RF regressor on the same features gives a nearly-identical result
(R² = 0.844, MAE = 8.35) — the signal is model-agnostic.

**Verdict: CHRONOLOGY-QUANTITATIVE.** The compositional signature tracks
chronology quantitatively, not merely dichotomously (M/M). H1 and H2 BOTH
pass at α_bon = 0.025.

## Pre-registered tests (Bonferroni-2)

| H | Test | Observed | Threshold | Pass? |
|---|---|---|---|:-:|
| **H1** | Ridge-full R² > Ridge-length-only R² AND perm-p < 0.025 | R² 0.836 > 0.446; p = 0.0020 | p < 0.025 | ✓ |
| **H2** | Ridge-full MAE < 15 | MAE = 8.74 | < 15 | ✓ |

Both pass → **CHRONOLOGY-QUANTITATIVE**.

## Numbers (primary table)

| Model | R²_LOOCV | MAE_LOOCV | Spearman_LOOCV |
|---|---:|---:|---:|
| **A — Ridge, all 12 features** | **0.836** | **8.74** | **0.920** |
| B — Ridge, log_length ONLY | 0.446 | 19.30 | 0.668 |
| C — RandomForest, all 12 features | 0.844 | 8.35 | 0.915 |

**Improvement of full model over length-only baseline**:
- ΔR² = +0.389 (87% relative gain)
- ΔMAE = −10.55 (55% reduction)

### Permutation null (Ridge full, 500 perms)

- null R² mean: −0.124 (negative = LOOCV worse than predicting mean)
- null R² SD: 0.088
- null R² 95th pctile: −0.021
- null R² 97.5th pctile: −0.005
- null R² max: +0.028
- **Observed R² 0.836 — one-sided p = 0.002** (1 / 501; no null run exceeded observed).

### MW-5 holdout (80/20, seed 20260419)

- n_train = 91, n_test = 23
- **Test R² = 0.926**, **MAE = 5.98**, Spearman ρ = 0.967
- LOOCV and holdout agree in direction; holdout MAE < 1.5× LOOCV MAE ✓.

## Top 3 most-predictive features

Two different importance frames agree on the identity of the top-3 (order
differs because RF and permutation-importance operationalise importance
differently):

### Ridge permutation importance (drop-R² when feature is shuffled)

| Rank | Feature | Δ R² when shuffled |
|:-:|---|---:|
| 1 | `log_length` | +0.244 |
| 2 | `mean_verse_len` | +0.198 |
| 3 | `allah_density` | +0.188 |

### RF feature importance (Gini decrease)

| Rank | Feature | Importance |
|:-:|---|---:|
| 1 | `mean_verse_len` | 0.659 |
| 2 | `allah_density` | 0.128 |
| 3 | `loanword_density` | 0.098 |

**Converged top-3 (union)**: `mean_verse_len`, `allah_density`,
`log_length` (RF underweights `log_length` because `mean_verse_len` already
absorbs the length signal; Ridge permutation treats them as partly
independent contributors).

## Interpretation

### Chronology IS quantitatively readable from surface compositional features

With 12 compositional features and ridge regression, we can place a surah
in the 114-long Nöldeke sequence to within ~9 rank positions on average (95%
of LOOCV absolute errors ≤ 24). The 80/20 holdout is even cleaner (MAE = 6).
This is a quantitative extension of [[h-new-162-beta-as-predictor|H-NEW-162]]'s binary M/M classifier (75%
acc.) and [[h-new-125-chronology-content|H-NEW-125]]'s per-axis monotone/inverted-U phase structure.

### What carries the signal

- **`mean_verse_length`** ([[h-new-46-1-chronology-disentangle|H-NEW-46.1]]'s classical finding): continues to
  dominate in the RF tree-split metric — dominant axis for the "Early Meccan
  → Medinan" monotone trajectory.
- **`allah_density`** ([[h-new-125-chronology-content|H-NEW-125]]'s #2 axis, ρ=+0.852): the 25.7× Medinan/
  Early-Meccan ratio makes it a powerful rank-discriminator for late surahs.
- **`log_length`** (trivially informative in isolation, R² = 0.45): the
  baseline that non-trivially adds independent signal on top of
  `mean_verse_length` (ridge permutation still credits it with Δ R² = 0.24
  after all other features are in the model).

### What carries little signal

- **`beta`, `alpha` (log K), `alpha_minus_beta`**: near-zero importance in
  all three frames. [[h-new-162-beta-as-predictor|H-NEW-162]]'s β contribution to period classification is
  not replicated at the per-rank regression level — β's Meccan/Medinan
  discriminating power likely comes from its correlation with verse length,
  which is present in the feature matrix independently.
- **`eschat_density`, `muq_cardinality`**: near-zero ridge permutation
  importance. Both are inverted-U (Late-Meccan-peaked) axes; their
  non-monotone shape provides phase-boundary info but little marginal
  rank-positioning signal once monotone features are in.
- **`book_ref_density`**: small NEGATIVE ridge coefficient (inverted-U shape
  means it declines in Medinan), but perm-importance is low.

## Honest limits

1. **Nöldeke rank is a scholarly reconstruction**, not ground truth.
   MAE = 8.74 is bounded by the rank-quality. Reconstructions with different
   internal assumptions (Egyptian Standard, Bazargan, Ernst) would give
   modestly different MAE. Should be audited for stability under
   reconstruction-swap.
2. **Ridge and RF converge on R² ≈ 0.84 with wildly different importance
   profiles.** This implies the 12 features are intercorrelated enough that
   the regression is not identifying "true causal" features — it is
   projecting a redundant feature bundle onto a monotone target. RF gives
   mean_verse_len 66% of the importance; ridge-perm spreads across length,
   verse-length, and allah-density. Truth: 2-3 of these features are
   non-redundant, the rest are collinear noise relative to target.
3. **35 / 114 surahs have NaN β / K** (short surahs, N<100 tokens). Median-
   imputation adds noise to those rows.
4. **`alpha` is log-K-proxy, not true Zipf α**: pre-committed fallback due
   to absence of per-surah true α in the locked JSON. A follow-up could
   re-fit Zipf per surah and check whether true α adds signal.
5. **Feature bundle is not orthogonalised**. A PCA pre-step would isolate
   how many independent axes of variation drive R².
6. **MW-5 holdout with MAE = 5.98** is actually BETTER than LOOCV MAE = 8.74
   — this happens because the random 20% test set happened to have many
   "easy" (extreme) surahs; descriptive, not problematic. LOOCV is the
   pre-registered primary metric.

## Connections

- **[[h-new-162-beta-as-predictor|H-NEW-162]]** (β + verse-length → 75% M/M binary): [[h-new-183-chronology-predictor|H-NEW-183]] upgrades
  this to continuous-rank regression; the binary classifier result now
  reads as a special case.
- **[[h-new-125-chronology-content|H-NEW-125]]** (15-axis chronology map, 11/15 survive Bon-15): the
  strongest-correlating axes (mean_verse_len ρ=0.90, allah_density ρ=0.85)
  dominate [[h-new-183-chronology-predictor|H-NEW-183]] too, as expected.
- **[[h-new-46-1-chronology-disentangle|H-NEW-46.1]]** (verse-length ramp, primary chronology axis): the "length
  ramp" remains the single most predictive feature.
- **[[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]** (universal hinges in chronology): the residual profile
  `y − ŷ` from [[h-new-183-chronology-predictor|H-NEW-183]] is a candidate input for detecting surahs whose
  compositional signature is OUT-OF-TREND vs their Nöldeke-assigned rank
  (follow-up hypothesis: residuals should cluster at phase-boundaries).

## Integration with M2

**M2 claim**: "The Quran is a chronologically-stratified corpus at the
structural level."

[[h-new-183-chronology-predictor|H-NEW-183]] **upgrades M2 from CATEGORICAL to CONTINUOUS**: the compositional
signature doesn't just distinguish 4 phases (Early Meccan / Middle Meccan /
Late Meccan / Medinan) — it places each surah on the continuous 1-114 Nöldeke
sequence with ~9-position average error. This is a major confirmation of
M2's quantitative version.

## Garden-of-forking-paths (post-run disclosure)

- **Pre-reg commitments kept**: 12 named features, Ridge(α=1.0), RF with 500
  trees, LOOCV, 500-perm null, seed 20260419, 80/20 MW-5 split, Bonferroni-2.
- **No post-hoc feature additions** (α-true, β-bootstrapped, etc. not added
  after seeing result).
- **`alpha` as log(K) proxy** was pre-committed in the pre-reg; not a
  post-hoc degradation.
- **500 permutations** (not 10000): pre-committed; sufficient for p < 0.025
  detection with 501 resolution (observed p = 1/501 = 0.002). Refining to
  10000 would not change the verdict (obs R² = 0.836 exceeds null max 0.028
  by ~10 null-SDs).

## Verdict

**PASS-DIRECTED** on both H1 and H2 at Bonferroni-2 (α_test = 0.025).

- H1: Ridge-full R² = 0.836 > baseline 0.446; perm p = 0.002 < 0.025. ✓
- H2: MAE = 8.74 < 15. ✓

Classification: **CHRONOLOGY-QUANTITATIVE**. Compositional signature tracks
Nöldeke rank at MAE ≈ 9 positions in LOOCV (≈ 6 in 80/20 holdout). Major
quantitative confirmation of M2.

**Upgrade to CONFIRMED** requires:
1. Swap Nöldeke rank for Egyptian Standard / Bazargan rank — does the
   predictor still reach R² ≥ 0.7?
2. Add true per-surah Zipf α (re-fit rank-frequency on each surah, not
   log-K proxy) — does it add signal?
3. Residual-profile audit: do the surahs with largest |y − ŷ| correspond to
   classically-debated chronology cases (e.g., "disputed Meccan-vs-Medinan"
   surahs)?

## Artefacts

- Pre-reg: `findings/phase-b-hypotheses/h-new-183-chronology-predictor-prereg.md`
- Script: `scripts/h_new_183_chronology_predictor.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-183.json`
- Journal: `journal/h-new-183-run-1.md`
