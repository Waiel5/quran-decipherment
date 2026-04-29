---
id: H-NEW-580
title: "Pre-reg — 5-Factor Cohesion Regression with out-of-sample subset prediction"
phase: B
date_committed: 2026-04-28
hypothesis_origin: cross-finding-024 §9 queued follow-up — convert qualitative 5-factor model to quantitative regression
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260428
---

# [[h-new-580-five-factor-regression|H-NEW-580]] — 5-Factor Cohesion Regression: Pre-Registration

## 1. Context

[[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] (2026-04-21) established a **qualitative 5-factor model**:

> content-cohesion ≈ f( block-adjacency × content-register-homogeneity × chronology-homogeneity × formula-sharing × no-outlier-surahs )

[[h-new-580-five-factor-regression|H-NEW-580]] converts this into a **fitted regression** with two stages:

- **Stage 1 (TRAINING)** — OLS + Ridge on the 12 subsets in [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] §3.
- **Stage 2 (OUT-OF-SAMPLE)** — Predict %ile for **6 NEW pre-registered subsets** whose factor-labels are committed BEFORE %ile is observed.

This design defeats the in-sample circularity of LOOCV on a model whose 12 anchor subsets were themselves used to discover the 5 factors.

## 2. Stage-1 training data (frozen by construction)

12 subsets from [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] §3, factor-labels frozen as below:

| # | Subset | %ile_observed | block_adj | register_homog | chrono_homog | formula_share | no_outlier |
|---|--------|--------------:|----------:|---------------:|-------------:|--------------:|-----------:|
| 1 | Q 107-114 | 0.0 | 1 | 1 | 1 | 0 | 1 |
| 2 | Q 98-114 (mufaṣṣal-qiṣār-17) | 0.0 | 1 | 1 | 1 | 0 | 1 |
| 3 | Q 57-66 (Medinan half) | 4.8 | 1 | 1 | 1 | 0 | 1 |
| 4 | Q 67-77 (mufaṣṣal-awsāṭ) | 7.1 | 1 | 1 | 1 | 0 | 1 |
| 5 | Musabbiḥāt block-5 | 8.1 | 1 | 1 | 1 | 1 | 1 |
| 6 | Q 2-9 (ṭiwāl) | 17.3 | 1 | 0 | 0 | 0 | 1 |
| 7 | Ḥawāmīm-5/6 (MW-5) | 21.0 | 1 | 0 | 1 | 1 | 1 |
| 8 | Q 50-56 minus Q 55 | 37.5 | 1 | 0 | 1 | 0 | 1 |
| 9 | Mufaṣṣal-ṭiwāl Q 50-66 | 50.1 | 1 | 0 | 0 | 0 | 0 |
| 10 | Meccan half Q 50-56 | 70.1 | 1 | 0 | 1 | 0 | 0 |
| 11 | al-Ḥāmidāt | 75.0 | 0 | 0 | 0 | 1 | 1 |
| 12 | Q 1 + Q 27 Basmala | 81.0 | 0 | 0 | 0 | 0 | 1 |

Encoding rules (locked):
- `block_adj`: 1 if all members are mushaf-contiguous; 0 otherwise.
- `register_homog`: 1 if all members share a single content register (creedal / eschat / legal / ethics); 0 if mixed.
- `chrono_homog`: 1 if all members same Nöldeke phase OR all Meccan / all Medinan; 0 if Hijra-spanning. ("MOSTLY-Meccan" = 1 if ≤1 transitional.)
- `formula_share`: 1 if a shared opening formula (al-ḥamd / sabbaḥa / qul / muqaṭṭaʿāt) is present in ALL members; 0 else. (PARTIAL = 0.)
- `no_outlier`: 1 if no member is in {Q 55, Q 1, Q 112, Q 9} OR if the candidate-outlier is explicitly removed; 0 if a confirmed outlier is present.

## 3. Stage-2 out-of-sample test subsets (factor-labels committed pre-run)

These 6 subsets are independent of the 12 training subsets. Their factor-labels are committed below; their `%ile_observed` is computed only AFTER the regression is fit on Stage-1.

| # | Subset (mushaf range) | block_adj | register_homog | chrono_homog | formula_share | no_outlier | Notes |
|---|----------------------|-----:|-----:|-----:|-----:|-----:|-------|
| OOS-1 | Q 78-89 (juzʾ-30 entry block) | 1 | 1 (eschat-uniform) | 1 (all Meccan) | 0 | 1 | classical eschat-block |
| OOS-2 | Q 86-92 | 1 | 1 (eschat) | 1 (Meccan) | 0 | 1 | mufaṣṣal-qiṣār subset |
| OOS-3 | Q 93-99 | 1 | 1 (creedal) | 1 (Meccan) | 0 | 1 | mufaṣṣal-qiṣār subset |
| OOS-4 | Q 51-54 (Meccan musabbiḥāt-precursor minus Q 55) | 1 | 0 (mixed Meccan) | 1 (Meccan) | 0 | 1 | Q 55 excluded |
| OOS-5 | Q 7-15 (ALMR + ALR cluster) | 1 | 0 (mixed prophet) | 0 (Hijra-spanning across some) | 1 (muqaṭṭaʿāt all) | 1 | letter-family block |
| OOS-6 | Q 30-39 | 1 | 0 (mixed) | 0 (mixed) | 0 (Q 36-38 muq, Q 30-32 muq, Q 33-35 not, Q 39 not) | 0 (Q 38 ص singleton) | mixed window |

Predicted ranges (informational, not gating):
- OOS-1, OOS-2, OOS-3 (4 factors aligned): predicted %ile = 0-15
- OOS-4 (4 factors aligned but register mixed): predicted %ile = 25-45
- OOS-5 (3 factors mixed): predicted %ile = 50-75
- OOS-6 (4 factors mixed): predicted %ile = 60-90

## 4. Pre-committed direction of effect

**ALL 5 coefficients should be NEGATIVE** (more factor-presence → lower %ile = more cohesion):
- β(block_adj) < 0
- β(register_homog) < 0
- β(chrono_homog) < 0
- β(formula_share) < 0
- β(no_outlier) < 0

Direction is locked. A positive coefficient on any factor counts as VIOLATION OF MODEL.

## 5. Pre-committed pass/fail thresholds

### Stage-1 in-sample (description-only, NOT gating)
- Report fitted R² and coefficient signs. Not used for verdict.

### Stage-2 out-of-sample (THIS IS THE GATE)
Predicted-vs-observed (`r_pred`) and mean abs error (`MAE_pred`) over the 6 OOS subsets:

- **STRICT PASS**: `r_pred ≥ 0.70` AND `MAE_pred ≤ 25` percentile-points AND all 5 coefficients have predicted-negative sign.
- **DIRECTIONAL**: `r_pred ≥ 0.50` AND `MAE_pred ≤ 35`.
- **NULL**: anything weaker.

### Permutation null
Shuffle the 12 Stage-1 %iles among the 12 factor-rows (10000 perms, seed=20260428), refit OLS, predict the 6 OOS subsets using their TRUE factor labels, compute `r_pred_null`. Report empirical p-value of observed `r_pred` exceeding the null distribution.

## 6. Bonferroni structure

- Two model fits (OLS, Ridge α=1.0) → Bonferroni-2.
- α corrected = 0.05 / 2 = 0.025 per fit on the permutation-test for `r_pred`.

## 7. Methodology rules invoked

- **MW-7 (post-hoc cap)**: not applicable — [[h-new-580-five-factor-regression|H-NEW-580]] is a primary regression with pre-committed OOS subsets; no single-test cap needed.
- **PRE-REG-STANDARD-04**: hypothesis (5-factor multiplicative), null (random factor-row permutation), direction (all β negative), bonferroni (k=2), test (OLS + Ridge OOS), DOF, success criteria — all locked herein.
- **MW-1 (instrument-prior)**: factor-encoding rules above.
- **MW-2 (corpus-prior)**: %ile is computed against 10000 random-K-subset null on FR-roots distance matrix [[h-new-111-fisher-rao-mushaf|h-new-111]].json.
- **MW-3 (alternatives-tested)**: Ridge α=1.0 included alongside OLS as alternative fit.
- **MW-5 (replication)**: Stage-2 OOS subsets are the replication test.

## 8. Specific predictions (will be checked)

If the 5-factor model is REAL:
1. Stage-1 R² ≥ 0.85 (12 subsets, 5 binary predictors).
2. All 5 βs negative, with |β| ranking: block_adj or register_homog largest, chrono_homog/no_outlier mid, formula_share smallest.
3. Stage-2 OOS-1, OOS-2, OOS-3 all observed %ile ≤ 20 (model predicts these as best-cohesion subsets).
4. Stage-2 OOS-5, OOS-6 observed %ile ≥ 50.
5. Stage-2 r_pred ≥ 0.70.

## 9. What would FALSIFY the model

- Any β positive (factor pulls anti-cohesion when its presence should add cohesion).
- Stage-2 r_pred < 0.50.
- Stage-2 MAE > 35.
- OOS-1 / OOS-2 / OOS-3 observed %ile > 30 (would falsify the multiplicative-factors claim).

## 10. Hash

This pre-registration is locked at SHA256 to be computed and recorded in the run script BEFORE any %ile of OOS subsets is observed.

## 11. Files

- Script: `scripts/h_new_580_five_factor_regression.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-580.json`
- Findings: `findings/phase-b-hypotheses/h-new-580-five-factor-regression.md` (post-run)

*Bismillāhi al-Raḥmāni al-Raḥīm.*
