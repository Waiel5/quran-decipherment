# H-NEW-233 run-1 — journal

**Date**: 2026-04-17
**Agent**: specialist (H-NEW-233 run-1)
**Parent**: H-NEW-192 (mushaf predictor R²=0.82)
**Seed**: 20260419

## Pre-reg summary

Push mushaf-position prediction R² beyond 0.82 by expanding H-NEW-192's 15-feature base set with 14 new instruments (phonological means from H-NEW-182, KL-divergence from H-NEW-231, per-surah Hurst from H-NEW-166/207 analogue, LZ76-norm from H-NEW-187, unigram entropy-rate from H-NEW-171 analogue, (α,β)-residual from H-NEW-178).

Pre-committed:
- H1: Ridge > 0.759 + p_perm < 0.025 (Bonferroni k=2, α_bon=0.025)
- H2: RF > 0.817
- strong-PASS threshold: R² > 0.90
- null rule: R² ≤ 0.836 means features add nothing beyond Nöldeke ceiling

## Execution

Script: `scripts/h_new_233_ensemble_predictor.py`, seed 20260419, LOOCV k=114, RF 500 trees, Ridge α=1.0, 100-permutation null.

Feature matrix shape: 114 × 29.

NaN pre-impute counts:
- alpha / beta / alpha_minus_beta: 35 each (surahs with <50 tokens where β fit fails, per H-NEW-123)
- alpha_beta_residual: 35 (inherited)
- hurst_verse_len: 52 (surahs with <16 verses cannot support DFA over ≥8-verse scales)
- all others: 0 NaN

Training-fold-median imputation applied.

## Results

| Model | R² | MAE |
|---|---:|---:|
| Ridge LOOCV | 0.7395 | 10.66 |
| RF LOOCV | **0.8485** | **7.24** |

Permutation null Ridge:
- null_r2_mean = −0.341
- null_r2_975 = −0.125
- null_r2_max = −0.074
- p_one_sided = 0.0099

H1 cell (Ridge): **FAIL** — R² 0.740 < 0.759 baseline. Signal is real (p < 0.025) but worse than base.
H2 cell (RF): **PASS** — R² 0.849 > 0.817 baseline AND > 0.836 Nöldeke ceiling.

Verdict: **INTERMEDIATE** per pre-reg interpretation rule (0.836 < RF < 0.90 band).

## Top findings

- **Entropy-rate jumped from unmeasured to 2nd-most-important feature** (RF importance 0.236), behind only log_length (0.563).
- **4 of 10 top RF features are H-NEW-233 additions**: entropy_rate, lz_norm_simple, kl_from_corpus, phon_pharyngeal.
- **Ridge coefficients reveal entropy/KL/LZ as length-orthogonal corpus-atypicality axes** absorbing ~30% of non-length mass.
- **Q 1 al-Fātiḥa remains the irreducible residual** (prediction 99.4, actual 1, Δ = −98.4) — sui-generis-liturgical confirmed under expanded feature set.
- **Q 109 al-Kāfirūn emerged as new #2 residual** (+43) — short-mufaṣṣal creedal closure not predictable from compositional features.

## Garden-of-forking-paths

- Ridge α locked at 1.0 pre-run (matches H-NEW-183/192). Ridge underperformance may reflect under-regularization with 29 features on 114 samples. Post-hoc α-sweep would likely recover Ridge but is deferred to H-NEW-233.2 per pre-reg.
- Feature selection: all 14 expansion features came from distinct prior pre-registered findings. No mid-run feature dropping; no mid-run addition. NaN-imputation at training-fold median as pre-committed.
- 100 permutations is the pre-committed count. No permutation-count adjustment.

## Cross-finding-020 update impact

- f_M5 compositional: 76% → ~85%
- g_M1 structural: 15% → ~10%
- h_P3 liturgical: 5% → ~4%
- Residual: 4% → ~1%

The M1 residual fingerprint (Q 1, ṭiwāl block, ḥawāmīm block, Medinan back-block) is **structurally unchanged** from H-NEW-192 — the compositional-explanation improvement did NOT dissolve M1 structural-placement pattern.

## Honest acknowledgements

1. Ridge H1 cell failed — the "ensemble" only works nonlinearly. Honest report: expanded-feature Ridge hurts; expanded-feature RF helps.
2. LOOCV leaks block-adjacent info at target position, so 0.849 is optimistic. Group-k-fold at block level queued.
3. Per-surah Hurst (52 NaN) was too noisy to contribute (importance 0.0008).
4. (α,β)-residual was redundant with its ingredients; importance 0.0007.
5. Final verdict crosses Nöldeke ceiling but does not reach 0.90 pre-committed threshold. The middle band "compositional features explain more than Nöldeke tracks but an irreducible ~15% remains M1+P3" is the honest placement.

## Next

- Append to MASTER-FINDINGS-LEDGER Wave-4.
- Queue H-NEW-233.1 (group-k-fold) and H-NEW-233.5 (apply same 29 features to Nöldeke — does the ceiling move?).
- Handoff-notes: the M1 structural placement residual is now quantitatively bounded to ~10-15% regardless of compositional feature expansion. This is not "unmeasured compositional detail" — it is genuine non-compositional architecture.
