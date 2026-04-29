---
id: H-NEW-250
title: "Quantitative fit of cross-finding-020's 4-principle Complete Equation — principle-labeled feature blocks with variance decomposition"
phase: B
status: PRE-REGISTERED
date: 2026-04-17
executed_by: specialist (H-NEW-250 run-1)
parent: cross-finding-020 (the Complete Equation); H-NEW-192 (15-feature R²=0.817 RF); H-NEW-233 (29-feature R²=0.849 RF); H-NEW-183 (Nöldeke ceiling R²=0.836)
seed: 20260419
rules_tuple: (no-tashkeel; all 114 surahs; LOOCV Ridge α=1.0; principle-labeled feature blocks; hierarchical variance-decomposition via dominance analysis / leave-one-block-out; seed 20260419)
bonferroni_family: h-new-250-quantitative-equation-fit
bonferroni_k: 4
alpha_bon: 0.0125
alpha_fam: 0.05
direction: "PASS if full-equation Ridge LOOCV R² > 0.88 AND p_perm < 0.0125; subset-M5 expected to dominate (~76% variance share per CF-020)"
verdict: PENDING
---

# [[h-new-250-quantitative-equation-fit|H-NEW-250]] — Pre-registration: quantitative fit of the Complete Equation

## Motivation

[[cross-finding-020-the-complete-equation|Cross-finding-020]] posits a descriptive decomposition:

```
rank_π*(s) ≈ f_M5(ℓ, v, mode) + g_M1(D, B, H, community)
           + h_M2(τ, m, p) + δ_class(s) + residual(s)
```

with **subjective** weight estimates ~76/20/6/4 ([[h-new-192-mushaf-position-decomposition|H-NEW-192]] informed).
This has been presented descriptively but NOT fit as a formal
regression with EXPLICIT principle-labeled feature blocks and
hierarchical variance decomposition. [[h-new-192-mushaf-position-decomposition|H-NEW-192]] (R²=0.817 RF, 15
compositional features) and [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] (R²=0.849 RF, 29 features)
used mixed-block feature sets that entangle compositional (M5) with
M2 chronology-markers and did not isolate M1 structural-placement
indicators. This pre-reg fixes the decomposition into 4 non-
overlapping principle blocks + a sui-generis class block, fits Ridge
LOOCV on all blocks jointly and on each block alone, and partitions
variance between principles via LEAVE-ONE-BLOCK-OUT (LOBO) dominance
analysis.

## Pre-committed protocol

### Feature blocks (principle-labeled; locked)

**Block f_M5 — compositional (length + vocabulary + mode; 11 features)**

1. `log_length` — log token count
2. `verse_count` — total verse count
3. `mean_verse_length` — mean tokens per verse
4. `type_token_ratio` — lexical diversity
5. `dispersion` ([[h-new-168-q16-q25-dispersion|H-NEW-168]]) — per-surah concept dispersion
6. `beta` (Heap β) — vocabulary-growth exponent
7. `alpha_minus_beta` — Zipf-vs-Heap axis
8. `kl_from_corpus` ([[h-new-231-kl-divergence-per-surah|H-NEW-231]]) — corpus-atypicality
9. `entropy_rate_surah` — per-surah unigram entropy (bits)
10. `lz_norm_simple` ([[h-new-187-lempel-ziv|H-NEW-187]]) — LZ76 normalized compressibility
11. `mode_indicator` — 5-level compositional mode from CF-020 §4:
    - mode_A_length_extremity: {2, 3, 50, 59, 62, 112, 113, 114}
    - mode_B_refrain: {55, 77, 78, 83, 52}
    - mode_D_inclusio: {4, 33, 59, 60, 63, 65} (top Medinan-inclusio per [[h-new-189-medinan-inclusio|H-NEW-189]])
    - mode_E_linear: Meccan non-inclusio
    - mode_C_default: remainder
    Encoded as 4 dummy vars (mode_C = reference).

**Block g_M1 — structural placement (hinges / blocks / community; 8 features)**

1. `dist_to_hinge` — minimum distance to universal hinges {(14,15), (49,50), (56,57)} per [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b
2. `is_tiwal` — indicator for Q 2-9 (sabʿ al-ṭiwāl block)
3. `is_hawamim` — indicator for Q 40-46 (ḥawāmīm block)
4. `is_medinan_back` — indicator for Q 47-66 Medinan-dominant block
5. `is_alm` — indicator for surahs opened with الم (2, 3, 29, 30, 31, 32)
6. `is_short_bracket` — indicator for Q 108-114 (short-terminal wrap)
7. `fiedler_community` — ±1 from [[h-new-185-ring-laplacian|H-NEW-185]] spectral partition (Q 13..77 → −1; Q 78..114∪1..12 → +1)
8. `log_length` — length-extremity hub proxy (same numeric column; shared with M5 by design; for M1-alone subset fit this is admitted since length-extremity IS the M1 hub mechanism per [[h-new-150-liturgical-hub|H-NEW-150]]; for LOBO decomposition the column is attributed to M5 and M1 alternately and dominance is averaged — documented below)

**Block h_M2 — chronology + markers + Pattern-B (6 features)**

1. `noldeke_rank` — from [[h-new-183-chronology-predictor|H-NEW-183]] ground-truth per-surah Nöldeke rank
2. `late_meccan_phase` — indicator (noldeke_phase ∈ {"Late Meccan", "Medinan"})
3. `muq_cardinality` — from [[h-new-125-chronology-content|H-NEW-125]]
4. `qul_density` — Pattern-B
5. `book_ref_density` — Pattern-B
6. `eschat_density` — Pattern-B (eschatological vocabulary density)

**Block δ_class — sui-generis / Class-A dummies (4 features)**

1. `is_q1_fatiha` — indicator Q 1
2. `is_q112_ikhlas` — indicator Q 112
3. `is_q113_falaq` — indicator Q 113
4. `is_q114_nas` — indicator Q 114

Total (full equation): 11 + 8 + 6 + 4 = **29 principle-labeled features** (the shared `log_length` is counted once; it appears in the M5 block; M1's `is_*` block indicators are the surrogate for length-extremity when log_length is removed).

### Models

Ridge regression LOOCV (α=1.0, z-scored in-fold, training-fold-median imputation). This matches [[h-new-192-mushaf-position-decomposition|H-NEW-192]] / [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] protocol. RF is NOT used here because the pre-reg goal is **interpretable variance decomposition via linear coefficients and LOBO subtraction**, not prediction-maximization.

### Four Bonferroni cells (k=4, α_bon = 0.0125)

- **Cell-1 (FULL)**: Ridge LOOCV with all 4 blocks jointly. Direction: R² > 0.88 AND p_perm < 0.0125.
- **Cell-2 (M5-only)**: Ridge LOOCV on block-M5 alone. Direction: R² > 0.70 (per CF-020 76% allocation, sqrt is ~0.87, but LOOCV one-block Ridge with 11 features typically tracks [[h-new-192-mushaf-position-decomposition|H-NEW-192]] 15-feature ≈ 0.75 — so 0.70 floor).
- **Cell-3 (M1-only)**: Ridge LOOCV on block-M1 alone. Direction: R² > 0.40 (block indicators alone are coarse).
- **Cell-4 (M2-only)**: Ridge LOOCV on block-M2 alone. Direction: R² > 0.40.

δ_class alone is NOT a Bonferroni cell; with 4 surahs of active indicators it contributes a fixed effect — reported descriptively only.

### Variance decomposition — LOBO dominance

For each block X_k, compute LOBO-ΔR² = R²(FULL) − R²(FULL \ X_k). This is the **marginal contribution** of block X_k given the other blocks. Report (i) per-block LOBO-ΔR²; (ii) single-block-alone R²; (iii) implied-variance-share via Shapley-like averaging over inclusion orders (we compute the 2 endpoints — alone and LOBO-marginal — which bracket true Shapley). The `log_length` ambiguity between M5 and M1 is resolved by attributing it to M5 in the primary decomposition (it is canonically an M5 axis per CF-020); in a robustness test we re-attribute to M1 and report the delta.

### Residual diagnostics

Top-10 |resid_full| surahs. For each, decompose the residual by computing (pred_full − pred_m5_only − pred_m1_only − pred_m2_only − pred_class_only) to see which block UNDER-predicts — the "missing principle" for that surah.

### Permutation null

100 permutations of y (seed 20260419), Ridge LOOCV on full feature matrix each permutation, retain R² distribution. p = (#null ≥ observed + 1) / (N_perm + 1).

### MW-5 cheat control

Permuted-target run should collapse R² toward 0 (within null). Reported as part of permutation null.

### Garden-of-forking-paths (pre-commit)

- Seed locked: 20260419.
- Feature blocks locked as above.
- Mode-indicator categorical encoding locked (4 dummies; mode_C reference).
- Fiedler-community sign convention locked per [[h-new-185-ring-laplacian|H-NEW-185]] JSON.
- Hinge set locked to [[h-new-130-fisher-rao-residuals|H-NEW-130]] universal 3 hinges.
- Mushaf-block indicators locked to classical tradition (ṭiwāl Q 2-9, ḥawāmīm Q 40-46, alm {2,3,29,30,31,32}, short-bracket Q 108-114, Medinan-back Q 47-66).
- log_length attribution in decomposition locked to M5 primary, M1 robustness.
- Ridge α locked at 1.0.
- LOOCV k=114 locked.
- 100 permutations for null.
- Dominance analysis: alone + LOBO-marginal; no post-hoc Shapley approximations.

## Interpretation rules (pre-committed)

- **R²_full > 0.88 AND variance split ≈ 76/15/5/4**: [[cross-finding-020-the-complete-equation|cross-finding-020]] equation QUANTITATIVELY VALIDATED.
- **R²_full > 0.88 BUT variance split DIFFERS (e.g., 85/5/5/5)**: CF-020 principle-weights need updating; update the 76/20/6/4 allocation accordingly.
- **0.85 ≤ R²_full ≤ 0.88**: directionally supportive but below target; the 29-feature principle-labeled framing does not beat [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]]'s 29-feature mixed framing — honest disclosure.
- **R²_full < 0.85**: the 4-principle framing LOSES vs [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]]'s 0.849; equation refinement required; update CF-020.
- **One principle dominates unexpectedly (e.g., M5 alone R² > 0.88)**: the other principles may be REDUNDANT given M5; refine the principle-weighting to drop low-marginal principles.
- **Top-10 residuals cluster by principle**: the missing-principle pattern identifies under-parameterized axes.

## Bonferroni family

k=4 (Cell-1 Full, Cell-2 M5-only, Cell-3 M1-only, Cell-4 M2-only), α_bon = 0.0125, α_family = 0.05.

## Honest limits (pre-commit)

- Ridge + LOOCV is optimistic on 114 samples with 29 features; the 0.88 target is aggressive given [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] Ridge plateaued at 0.740 (though RF reached 0.849).
- Block-indicator M1 features are COARSE surrogates for the Fisher-Rao-geodesic mechanism; a feature like `fisher_rao_dist_to_neighbors` would be richer but would entangle with the Ridge's target (mushaf position).
- δ_class dummies with 4 active cases are near-perfectly-fittable by construction; they carry ~0 LOOCV information (held-out surah has its own dummy column zeroed for training fold but the indicator is still constant 0 for the held-out row unless that surah is in the class). The contribution of δ_class is INTERPRETATIVE, not predictive — this is explicitly acknowledged.
- The 4-principle framing enforces orthogonality where CF-020 itself explicitly states the principles overlap (M5 length is also an M2 axis per §2.2). The fit is a CANONICAL-FACTORIZATION not an ORTHOGONAL one.

## Files on completion

- Script: `scripts/h_new_250_equation_fit.py`
- Findings: `findings/phase-b-hypotheses/h-new-250-quantitative-equation-fit.md`
- JSON: `findings/phase-b-hypotheses/csv/h-new-250.json`
- Journal: `journal/h-new-250-run-1.md`
- Ledger: append Wave-5 entry in MASTER-FINDINGS-LEDGER.md
