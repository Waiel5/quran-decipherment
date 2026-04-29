---
id: H-NEW-233
title: Ensemble mushaf-position predictor — expanded-feature-set Ridge + RF LOOCV push toward 0.90+
phase: B
status: PRE-REGISTERED
date: 2026-04-17
executed_by: specialist (H-NEW-233 run-1)
parent: H-NEW-192 (mushaf position predictor R²=0.82)
seed: 20260419
rules_tuple: (no-tashkeel; all 114 surahs; LOOCV; seed 20260419; features z-scored in-fold; training-fold-median imputation; Ridge α=1.0; RF n_estimators=500; 100-perm null; per-feature z-score computed on training fold only)
bonferroni_k: 2
bonferroni_family: h-new-233-ensemble-mushaf-predictor
alpha_bon: 0.025
direction: PASS if R² > 0.82 (Ridge or RF beats H-NEW-192 baseline)
verdict: PENDING
---

# [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] — Pre-registration: ensemble mushaf-position predictor

## Motivation

[[h-new-192-mushaf-position-decomposition|H-NEW-192]] established Ridge LOOCV R² = 0.759, RF LOOCV R² = 0.817 on 15 compositional features for mushaf-position prediction. [[h-new-183-chronology-predictor|H-NEW-183]] established Nöldeke-rank LOOCV R² = 0.836 from the same base feature set. The 0.08 gap (mushaf − Nöldeke) quantifies the M1 structural-placement + P3 liturgical-frame residual per [[cross-finding-020-the-complete-equation|cross-finding-020]].

This pre-reg locks an expanded-feature-set ensemble predictor to test whether additional per-surah instruments (phonological vectors, KL-divergence, α-β residuals, Hurst, dispersion, LZ76, entropy rate, divine-name density) push R² beyond 0.82 toward the Nöldeke-ceiling of 0.836 and potentially into 0.90+ territory.

## Pre-committed protocol

### Feature set (locked)

**Base 15 features ([[h-new-192-mushaf-position-decomposition|H-NEW-192]] set)** — from [[h-new-123-heap-law|H-NEW-123]], [[h-new-125-chronology-content|H-NEW-125]], [[h-new-168-q16-q25-dispersion|H-NEW-168]]:
1. `alpha` (log K proxy)
2. `beta` (Heap β)
3. `alpha_minus_beta`
4. `log_length` (log N tokens)
5. `mean_verse_len`
6. `allah_density` (divine-name density)
7. `qul_density`
8. `book_ref_density`
9. `loanword_density`
10. `eschat_density`
11. `dispersion` ([[h-new-168-q16-q25-dispersion|H-NEW-168]]/163)
12. `muq_cardinality`
13. `verse_count`
14. `type_token_ratio`
15. `refrain_score`

**Expansion features ([[h-new-233-ensemble-mushaf-predictor|H-NEW-233]] additions)** — from [[h-new-182-phonological-vectors|H-NEW-182]], [[h-new-187-lempel-ziv|H-NEW-187]], [[h-new-231-kl-divergence-per-surah|H-NEW-231]], plus recomputed per-surah instruments:
16-24. **Phonological vectors ([[h-new-182-phonological-vectors|H-NEW-182]] surah means)**: `phon_labial`, `phon_alveolar`, `phon_palatal`, `phon_velar`, `phon_pharyngeal`, `phon_glottal`, `phon_emphatic`, `phon_voiced`, `phon_continuant`.
25. **KL-divergence from corpus ([[h-new-231-kl-divergence-per-surah|H-NEW-231]])**: `kl_from_corpus` — Dirichlet-smoothed α=0.5, computed per surah from no-tashkeel tokens.
26. **Per-surah Hurst exponent (H-NEW-207 analogue)**: `hurst_verse_len` — DFA on word-counts-per-verse, global slope over surah-internal scales ≥8 verses. NaN for surahs with fewer than 16 verses; training-median imputed.
27. **LZ76-norm complexity ([[h-new-187-lempel-ziv|H-NEW-187]])**: `lz_norm_simple` — lz_count / (n_chars / log(n_chars)).
28. **Entropy rate ([[h-new-171-entropy-rate-mushaf|H-NEW-171]] analogue)**: `entropy_rate_surah` — token-unigram entropy per surah in bits (Shannon), computed on no-tashkeel words. Simple proxy for [[h-new-171-entropy-rate-mushaf|H-NEW-171]]'s conditional entropy (full k-NN conditional not per-surah-decomposable).
29. **α, β manifold residual ([[h-new-178-alpha-beta-manifold|H-NEW-178]])**: `alpha_beta_residual` — residual of α when regressed on β + log_length jointly (off-manifold axis).

Total: **29 features** (15 base + 14 expansion).

### Models

- **Model A**: Ridge regression, α=1.0, LOOCV.
- **Model B**: Random Forest, n_estimators=500, max_depth=None, LOOCV.

### Preprocessing (in-fold)

- Missing values imputed to training-fold median.
- Features z-scored (StandardScaler) on training fold only for Ridge.
- RF fed raw (imputed) features.

### Permutation null

100 permutations of mushaf target (seed 20260419), Ridge LOOCV each, retain R² distribution.

### Statistical tests (pre-committed)

- **H1 (Ridge-beats-H-NEW-192-Ridge-baseline)**: Ridge R² > 0.759, p_perm < 0.025 (one-sided, Bonferroni k=2).
- **H2 (RF-beats-H-NEW-192-RF-baseline)**: RF R² > 0.817, p_perm < 0.025 (one-sided).

### Bonferroni family

k=2 (Ridge + RF primary cells), α_bon = 0.025 per test, α_family = 0.05.

### MW-5 cheat control

Permute targets → expected R² ≈ 0. Included via the 100-perm null.

### Garden-of-forking-paths log (pre-commit)

- Seed locked: 20260419.
- Feature set locked: 29 above.
- No mid-run feature selection or exclusion.
- Ridge α locked at 1.0 (matches [[h-new-183-chronology-predictor|H-NEW-183]]/192).
- RF params locked at (500, None).
- Imputation locked: training-fold median only.
- z-scoring locked: StandardScaler on training fold for Ridge; raw for RF.
- LOOCV k=114 locked.

## Interpretation rules (pre-committed)

- **R² > 0.90**: M1+M5 residual drops to <10% — majority of mushaf-structure is compositionally derivable. M2+P3 constitute <10% liturgical bracket. Update [[cross-finding-020-the-complete-equation|cross-finding-020]] weights.
- **R² ≤ 0.836 (Nöldeke ceiling)**: additional features do NOT add beyond chronology ceiling — M1 structural placement is the irreducible organizing principle.
- **R² 0.836 < x < 0.90**: intermediate; new features capture some but not all of the M1+M5 residual; update [[cross-finding-020-the-complete-equation|cross-finding-020]] equation weights with new split.

## Honest limits (pre-committed)

1. Small-N (114 surahs) — LOOCV optimistically biased.
2. 29 features on 114 samples = 1 feature per ~4 samples; multicollinearity and overfitting risks for Ridge; RF more robust.
3. Post-hoc feature expansion — garden-of-forking-paths risk: we chose these features after observing [[h-new-192-mushaf-position-decomposition|H-NEW-192]] residuals. Mitigation: every feature was introduced by a prior pre-registered hypothesis ([[h-new-165-phonological-predictor|H-NEW-165]]/166/171/178/182/187/231).
4. LOOCV still optimistic on grouped structure (e.g., block-residual may leak). Honest number is the 100-perm null gap, not the raw R².
5. Phonological surah means are summary statistics; finer within-surah phonological structure is not captured.
6. Per-surah Hurst is noisy for short surahs (<16 verses); imputation dampens signal.

## Files

- Pre-reg: this file
- Script: `/Users/grey/Downloads/quran/scripts/h_new_233_ensemble_predictor.py`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-233-ensemble-mushaf-predictor.md`
- Output JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-233.json`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-233-run-1.md`

## Classical anchor

al-Biqāʿī *Naẓm al-Durar* — implicit principle that each surah's mushaf position reflects coherent editorial logic (mushaf ordering tawqīfī per majority; ijtihādī per minority). Our test: how much of that logic is compositionally derivable from per-surah instruments?
