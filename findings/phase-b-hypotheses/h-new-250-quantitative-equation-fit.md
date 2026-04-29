---
id: H-NEW-250
title: "Quantitative fit of cross-finding-020's Complete Equation — Ridge R² = 0.890 clears 0.88 target, but variance decomposition INVERTS the CF-020 76/15/5/4 allocation"
phase: B
status: STRONG-PASS (Cell-1 FULL) + VARIANCE-DECOMPOSITION-CONTRADICTORY
date: 2026-04-17
executed_by: specialist (H-NEW-250 run-1)
parent: cross-finding-020 (the Complete Equation); H-NEW-192; H-NEW-233; H-NEW-183
seed: 20260419
rules_tuple: (no-tashkeel; all 114 surahs; LOOCV Ridge α=1.0; principle-labeled feature blocks; LOBO variance-decomposition; seed 20260419; 100-perm null)
bonferroni_family: h-new-250-quantitative-equation-fit
bonferroni_k: 4
alpha_bon: 0.0125
verdict: STRONG-PASS on Cell-1 (R²=0.890 > 0.88 target, p=0.0099 < 0.0125); PASS on all 4 block-alone cells; but the variance decomposition re-allocates: M1 block dominates marginal contribution (71.7%), not M5 (13.5%) as CF-020 predicted
---

# [[h-new-250-quantitative-equation-fit|H-NEW-250]] — Quantitative Fit of the Complete Equation

## Headline

| Cell | Fit | R² LOOCV | MAE | vs target |
|---|---|---:|---:|---|
| **Cell-1 FULL (all 4 blocks)** | Ridge 32-feat | **0.8899** | 6.50 | **+0.010 over 0.88 target → PASS** |
| Cell-2 M5-only (14 feat) | Ridge | 0.8041 | 8.85 | > 0.70 target → PASS |
| Cell-3 M1-only (8 feat) | Ridge | **0.8683** | 7.92 | > 0.40 target → PASS |
| Cell-4 M2-only (6 feat) | Ridge | 0.5539 | 16.47 | > 0.40 target → PASS |
| CLASS-only (4 feat, descriptive) | Ridge | −0.018 | 28.75 | LOOCV-structural NULL |
| Baselines for comparison | | | | |
| [[h-new-192-mushaf-position-decomposition|H-NEW-192]] Ridge (15 feat) | — | 0.759 | 10.81 | — |
| [[h-new-192-mushaf-position-decomposition|H-NEW-192]] RF (15 feat) | — | 0.817 | 7.96 | — |
| [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] Ridge (29 feat) | — | 0.740 | 10.66 | — |
| [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] RF (29 feat) | — | 0.849 | 7.24 | — |
| [[h-new-183-chronology-predictor|H-NEW-183]] Nöldeke Ridge | — | 0.836 | 8.74 | — |

Permutation null (100× Ridge on permuted y): null R² mean = −0.319, max = −0.084, **p = 0.0099 < α_bon = 0.0125 → PASS**.

**Pre-reg verdict: STRONG PASS on Cell-1.** The principle-labeled 32-feature Ridge **beats [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] 29-feature Ridge by +0.15 R²** and beats [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] RF by +0.04 R². This is the project's highest-R² LOOCV mushaf-position predictor to date. Signal is real; R² > Nöldeke ceiling 0.836 by +0.054.

## Why Ridge cleared 0.88 here when [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] Ridge plateaued at 0.74

[[h-new-233-ensemble-mushaf-predictor|H-NEW-233]]'s 29 features were heavily multicollinear (phonological vectors + length-correlated entropy/KL). This set is principle-labeled with **hard block-indicator features** — `is_tiwal`, `is_hawamim`, `is_medinan_back`, `is_alm`, `is_short_bracket`, `fiedler_community` — which are sparse (non-zero on 8, 7, 20, 6, 7 surahs respectively) and directly encode the CLASSICAL MUSHAF BLOCK STRUCTURE. These are LOW-MULTICOLLINEARITY, HIGH-SIGNAL features that Ridge handles cleanly. The M1 block alone reaches R² = 0.868 — these block indicators capture position-within-mushaf almost as well as the full feature set.

This is a methodological finding in its own right: **the mushaf's block architecture is Ridge-linearly encodable** as a small set of classical indicator variables, once those indicators are explicitly pre-registered (not post-hoc mined).

## Variance decomposition: LOBO dominance inverts CF-020's allocation

CF-020 stipulated (from [[h-new-192-mushaf-position-decomposition|H-NEW-192]] Ridge subset analysis): compositional **76%** + structural-M1 **15%** + M2 marginal **5%** + CLASS Q 1 **4%**.

[[h-new-250-quantitative-equation-fit|H-NEW-250]] LOBO marginals (normalized to % of total positive marginal):

| Block | Alone R² | LOBO drop-ΔR² | LOBO share | CF-020 expected |
|---|---:|---:|:-:|:-:|
| M1 | 0.868 | **+0.0617** | **71.7%** | 15% |
| M5 | 0.804 | +0.0116 | 13.5% | 76% |
| CLASS | −0.018 | +0.0128 | 14.9% | 4% |
| M2 | 0.554 | −0.0006 | 0.0% | 5% |

**Interpretation**: M1 block (structural placement indicators) carries the **marginal** variance — removing M1 costs 6.17 R² points; removing M5 costs only 1.16 R² points; removing M2 costs NOTHING (ΔR² = −0.0006, redundant given M1+M5).

**Alone-R² is more balanced**: M1 alone = 0.868; M5 alone = 0.804; M2 alone = 0.554. All three principles carry substantial **shared** variance; but when forced to choose, **M1's block indicators are the uniquely most-informative axis**.

### Reconciling with CF-020

CF-020's 76/15/5/4 estimate came from [[h-new-192-mushaf-position-decomposition|H-NEW-192]] which did **NOT include M1 block indicators as features** — [[h-new-192-mushaf-position-decomposition|H-NEW-192]]'s 15 features were all M5/M2 compositional. [[h-new-192-mushaf-position-decomposition|H-NEW-192]]'s residual analysis identified M1 as the 20%-residual EXPLANATION (via Q 1 Δ=−104, Q 8 ṭiwāl Δ=−32, Q 40 ḥawāmīm Δ=+32, etc.), but never actually measured M1's predictive share when given explicit M1 features. Once M1 gets explicit block-indicator features, it SWAMPS M5's marginal contribution because M5's contribution was partly an M1-block-indicator proxy (long surahs → ṭiwāl block, short surahs → short-bracket block).

**CF-020 weight update proposed**:

- Old allocation ([[h-new-192-mushaf-position-decomposition|H-NEW-192]] inference): f_M5 ~76% + g_M1 ~15% + h_M2 ~5% + δ_class ~4%.
- **New allocation ([[h-new-250-quantitative-equation-fit|H-NEW-250]] LOBO-marginal)**: g_M1 ~**70%** + (f_M5 ∪ δ_class) ~**28%** + h_M2 ~**2%** (absorbed by M1∪M5).
- **Honest re-read**: when M1 and M5 share the length axis (long surahs ≈ ṭiwāl block), attributing to one vs the other is a labeling choice. The alone-R² numbers (M5=0.804 / M1=0.868 / M2=0.554) show that **the 4 principles are strongly INTER-CORRELATED; there is no clean orthogonal decomposition.** CF-020 §2.2 acknowledged this ("NOT independent decomposition axes") but gave a 76/15/5/4 point-estimate. [[h-new-250-quantitative-equation-fit|H-NEW-250]] supplies two endpoints that bracket the true Shapley: 13.5/71.7/0/14.9 (LOBO marginal) vs 36.1/39.0/24.9/0 (alone-normalized).

## Top-10 residuals — which principle is missing for each?

| Rank | Q | Pos | Pred_full | Resid | Most-needed principle (from LOBO-Δ|resid|) |
|:-:|:-:|:-:|:-:|:-:|---|
| 1 | **1** | 1 | 82.4 | **−81.4** | **M1** (Q 1 LOOCV dummy is zeroed → M1 block indicators too coarse to place fātiḥa at 1) |
| 2 | 8 | 8 | 33.6 | −25.6 | CLASS (Q 8's compositional proxies point to ṭiwāl-end; no dedicated Q 8 dummy) |
| 3 | 67 | 67 | 44.8 | +22.2 | CLASS (Q 67 al-Mulk short-Medinan-ish; no dummy) |
| 4 | 32 | 32 | 52.5 | −20.5 | M1 (alm-block Q 32 requires `is_alm` indicator strength) |
| 5 | 2 | 2 | −17.4 | +19.4 | M2 (Q 2 ṭiwāl-head; ridge extrapolates negative because log_length pushes below 0) |
| 6 | 7 | 7 | −10.6 | +17.6 | M5 (Q 7 al-Aʿrāf very long alm; pushes below 0 similarly) |
| 7 | 72 | 72 | 55.4 | +16.6 | M5 |
| 8 | 25 | 25 | 40.5 | −15.5 | M5 |
| 9 | 15 | 15 | 30.2 | −15.2 | M1 (ṭiwāl-end Q 15; mushaf uses block-indicator edge) |
| 10 | 62 | 62 | 76.9 | −14.9 | M1 (Q 62 Medinan-back edge; `is_medinan_back` 47-66 doesn't extend cleanly) |

**Principle-tally of top-10 residuals**: M1 missing for 4, M5 missing for 4, M2 missing for 1, CLASS missing for 2. M1 and M5 are both under-parameterized in this discrete-block formulation. CLASS misses Q 8 and Q 67, suggesting Class-A should extend beyond {Q 1, 112, 113, 114} to capture ṭiwāl-head and late-Medinan ambiguity.

**Q 1 remains the largest residual under this fit** (|resid| = 81.4) — unchanged in direction from [[h-new-192-mushaf-position-decomposition|H-NEW-192]]'s |Δ| = 104. The `is_q1_fatiha` CLASS dummy cannot help Q 1 at LOOCV because when Q 1 is held out, its indicator is 0 (not 1) for training — the dummy cannot carry information about Q 1 itself. This LOOCV-structural limitation means **CLASS dummies contribute 0 to Cell-1's R² in the predictive-out-of-sample sense**, confirming the pre-reg caveat.

## Comparison to [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]]

| Metric | [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] | [[h-new-250-quantitative-equation-fit|H-NEW-250]] | Δ |
|---|---:|---:|---:|
| Features | 29 (compositional + phonological + complexity) | 32 (11 M5 + 8 M1 + 6 M2 + 4 CLASS; 3 mode dummies; 1 duplicate log_length) | +3 |
| Ridge LOOCV R² | 0.740 | **0.890** | **+0.150** |
| RF LOOCV R² | 0.849 | not run | — |
| MAE Ridge | 10.66 | **6.50** | **−4.16 positions** |
| Beats Nöldeke ceiling (0.836)? | RF only | **Ridge yes** (+0.054) | — |

**The step change comes from explicit M1 block indicators.** [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] had all-continuous features; [[h-new-250-quantitative-equation-fit|H-NEW-250]] adds 6 sparse categorical block indicators that linearly encode the classical mushaf architecture. Ridge can exploit categorical sparsity far better than it could phonological-vector collinearity.

This has an interpretive implication beyond prediction: **the mushaf's block structure is classical-tradition-derivable as a small set of names** (ṭiwāl, ḥawāmīm, alm, Medinan-back, short-bracket, Fiedler community) that collectively predict position to MAE = 6.5 — better than any continuous-feature ensemble tried so far.

## Honest limits

1. **Ridge + LOOCV optimism**: with 32 features on 114 samples, LOOCV-Ridge can overfit. The 100-perm null mean (−0.319) is far below 0, and max (−0.084) is still negative, so the 0.89 signal is strongly non-random. But the exact 0.89 number may be +0.02 optimistic vs held-out-block validation.
2. **M1 block indicators are manually pre-registered** from classical tradition. They are NOT feature-engineered from the data; they encode 14 centuries of classical mushaf-structure knowledge as binary indicators. The high R² is partly a measurement of **how much the classical tradition already knew** about mushaf structure.
3. **CLASS dummies are LOOCV-structurally-useless** by construction. They are INTERPRETIVE, not PREDICTIVE. Reported honestly.
4. **log_length is shared between M5 and M1**: the `log_length_M1` duplicate in the M1 block is a robustness choice. Under M1 attribution (robust variant), M5 alone = 0.802 (vs 0.804 primary); the share estimate is robust to this choice.
5. **M2 is effectively ABSORBED by M1+M5** in this decomposition: LOBO-ΔR² = −0.0006 means dropping M2 slightly IMPROVES the fit. This reflects the fact that noldeke_rank + late_meccan_phase + muq_cardinality + qul/book-ref/eschat densities are COLLINEAR with M5 features (KL, entropy, TTR) AND with M1 block indicators (is_medinan_back is phase-aligned). M2 as a principle is NOT refuted, but as a **predictively-marginal contributor given M1+M5**, its share is ~0.
6. **Garden-of-forking paths**: pre-reg locked blocks before any R² result. The 4-block / 32-feature split was committed in the pre-reg file before the script ran. No post-hoc feature tweaking.

## Updating [[cross-finding-020-the-complete-equation|cross-finding-020]]

The Complete Equation statement is NOT refuted — all 4 principles remain identifiable, and the equation still holds descriptively. What [[h-new-250-quantitative-equation-fit|H-NEW-250]] refines:

1. **The 76/15/5/4 allocation from [[h-new-192-mushaf-position-decomposition|H-NEW-192]] undercounts M1** because [[h-new-192-mushaf-position-decomposition|H-NEW-192]] didn't include M1 block indicators. The more accurate bracket is **{alone: 36/39/25/0 ; LOBO-marginal: 14/72/0/15}**, with true Shapley somewhere between.

2. **M2 is redundant given M1+M5** at the predictive level. This does NOT mean M2 is unreal — classical chronology stratification is well-documented by Nöldeke and the 4-phase tradition — it means that at the mushaf-position prediction task, M2's axes are fully captured by M1 (block structure) + M5 (length + vocabulary). This is consistent with CF-020 §2.2's honest disclaimer about non-orthogonality.

3. **Q 1 is the largest irreducible residual (|resid| = 81)** — same direction as [[h-new-192-mushaf-position-decomposition|H-NEW-192]]'s Δ=−104. The CLASS dummy cannot fix it at LOOCV. Q 1's P3 liturgical-frame status persists as **absolutely-necessary classical prior information**, confirming CF-020's δ_class interpretation.

4. **Classical structural knowledge is Ridge-linearly tractable**: the 6 block-indicator features (ṭiwāl, ḥawāmīm, alm, Medinan-back, short-bracket, Fiedler) encode 14 centuries of classical mushaf-structure knowledge as binary columns and predict position to MAE = 8 positions on M1 alone. This is SECONDARY-TRIANGULATED vindication of classical block-structure traditions (al-Suyūṭī, al-Zarkashī, al-Rāzī).

## Verdict

**STRONG-PASS on Cell-1 (full equation R² > 0.88 at p = 0.0099)**. The 4-principle framing DOES quantitatively fit with R² = 0.890 — exceeding the pre-committed 0.88 target and beating both the Nöldeke ceiling (0.836) AND [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]]'s 0.849 RF. The Complete Equation's math HOLDS.

**VARIANCE-DECOMPOSITION re-allocation**: the CF-020 76/15/5/4 point-estimate was biased toward M5 by [[h-new-192-mushaf-position-decomposition|H-NEW-192]]'s feature omission of M1 indicators. Under principle-labeled LOBO analysis, **M1 carries 72% of marginal variance; M5 + CLASS together carry the remaining 28%; M2 is redundant given M1+M5**. This REFINES (does not refute) CF-020; the refined allocation is **M1-block-structure-dominant** rather than compositional-dominant.

**Top residual pattern**: Q 1 at −81 (sui-generis-liturgical); ṭiwāl-head (Q 2, Q 7, Q 8) and block-edges (Q 15, Q 32, Q 62, Q 67) are under-parameterized at the current block-indicator resolution. Future work could add edge-distance features (how close to block boundaries) to tighten these.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-250-quantitative-equation-prereg.md`
- Script: `scripts/h_new_250_equation_fit.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-250.json`
- Journal: `journal/h-new-250-run-1.md`
- This file: `findings/phase-b-hypotheses/h-new-250-quantitative-equation-fit.md`
