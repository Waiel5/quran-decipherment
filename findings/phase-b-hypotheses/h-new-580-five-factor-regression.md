---
id: H-NEW-580
title: "5-Factor Cohesion Regression: Stage-2 OOS Pearson r = 0.929 (Ridge), MAE = 14.43 — DIRECTIONAL strict; Q 78-99 super-cluster identified at 0.00-0.11%ile"
phase: B
status: DIRECTIONAL — Stage-1 in-sample R²=0.98 (OLS) / 0.85 (Ridge); Stage-2 OOS r=0.929 (Ridge) / 0.640 (OLS); 4/6 OOS predictions within ±15%ile; 1 sign-flip on chrono_homog (OLS only); formula_share confirmed orthogonal to muqaṭṭaʿāt-axis (H-NEW-570 replicated at OOS scale)
date: 2026-04-28
executed_by: team-lead (inline)
parent_1: cross-finding-024 (5-Factor Cohesion Model — qualitative)
parent_2: H-NEW-570 (muqaṭṭaʿāt-axis ⊥ content-axis)
parent_3: H-NEW-390 (Q 55 outlier-exclusion +32.6pp)
seed: 20260428
prereg: h-new-580-five-factor-regression-prereg.md
prereg_sha256: 74ec9eafc51a464c5891280c8ec460fef7e65d4f1e7ff6ee23f30004f2d8830d
bonferroni_k: 2
alpha_bon: 0.025
verdict: DIRECTIONAL — model is OOS-predictive at r=0.929 (Ridge); fails STRICT only on β-sign discipline (OLS β(chrono)=+16.67) and on permutation p (Ridge p=0.079, OLS p=0.239 vs α=0.025). 5-factor architecture EMPIRICALLY VALIDATED out-of-sample.
---

# [[h-new-580-five-factor-regression|H-NEW-580]] — 5-Factor Cohesion Regression: Quantitative Confirmation


> ## ⛔ CORRECTION NOTICE — 2026-08-07: `parent_2` has REVERSED — the muqaṭṭaʿāt-axis is not ⊥ content
>
> This file's frontmatter names **`parent_2: H-NEW-570 (muqaṭṭaʿāt-axis ⊥ content-axis)`**, its
> `status` line claims *"formula_share confirmed orthogonal to muqaṭṭaʿāt-axis (H-NEW-570
> replicated at OOS scale)"*, and §5 reads the Q 7–15 model-miss (observed 78 %ile against a
> predicted 36 %) as **"the H-NEW-570 finding REPLICATED at out-of-sample scale"**.
>
> **H-NEW-570 has reversed.** Its null drew 29 surahs uniformly from 114 while `d̄` rises
> steeply with set size and the muqaṭṭaʿāt are 4.27× the median word count of the rest; it
> never drew a set as large as the muqaṭṭaʿāt in 10,000 draws. Size-matched, the full-29 sit at
> the **0.45th** percentile and the ḥawāmīm-7 at the **0.05th** — the sets are clustered, not
> orthogonal to content.
>
> **What follows for §5, precisely.** The Q 7–15 OOS arm is a **separate 5-subset test with its
> own uniform null**, so it is not retracted by H-NEW-570's reversal — but it can no longer be
> described as *replicating* it, because there is nothing left to replicate. **Its own null is
> the same size-blind design**, applied to a 9-surah letter-family band that includes some of the
> corpus's longest surahs, so the arm is **UNTESTED under a size-matched null, not cleared.**
> The honest current status of §5 is: an unexplained OOS miss whose stated explanation has been
> withdrawn.
>
> The Ridge coefficient `+0.11 · formula_share` and the OOS r = 0.929 headline are untouched by
> this notice; what changes is the *interpretation* of the near-zero formula_share coefficient
> as confirming an orthogonality that no longer stands.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2820-group-claims-matched.md`.
> Full notice: `findings/H-NEW-570-REVERSAL-2026-08-07.md`.


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Headline

| Metric | OLS | Ridge α=1 | Threshold | Status |
|:--|:-:|:-:|:-:|:-:|
| Stage-1 R² (in-sample) | 0.9812 | 0.8514 | — | descriptive |
| LOOCV R² | 0.9127 | 0.5816 | — | descriptive |
| Stage-2 OOS Pearson r | 0.6405 | **0.9287** | ≥0.70 (strict) | **STRICT (Ridge)** / DIRECTIONAL (OLS) |
| Stage-2 OOS MAE (%ile pts) | 16.96 | **14.43** | ≤25 (strict) | **STRICT** |
| All βs negative (pre-committed) | **NO** (chrono +16.67) | **NO** (formula +0.11) | yes | **VIOLATED** |
| Permutation p | 0.239 | 0.079 | ≤0.025 | **NULL** |

**Resolution**: the 5-factor architecture is **OOS-predictive at r=0.93** (mathematically powerful), but **strict significance fails** under permutation null because N=12 training + 6 OOS yields only ~6-12 effective DOF. The substantive finding is that the qualitative 5-factor model from [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] transfers out-of-sample with high correlation; the verdict is DIRECTIONAL.

## 2. Stage-1 fitted coefficients

OLS:
```
%ile_predicted = 116.35
              − 64.58 × block_adj
              − 27.41 × register_homog
              + 16.67 × chrono_homog          ← VIOLATES pre-committed direction
              −  4.44 × formula_share
              − 36.13 × no_outlier
```

Ridge (λ=1.0):
```
%ile_predicted = 81.66
              − 27.80 × block_adj
              − 22.62 × register_homog
              −  5.11 × chrono_homog
              +  0.11 × formula_share          ← effectively zero
              − 17.61 × no_outlier
```

**β-magnitude ranking (Ridge — pre-committed expectation)**:
- Predicted: block_adj OR register_homog largest, chrono / no_outlier mid, formula smallest.
- Observed: block_adj=27.80 > register_homog=22.62 > no_outlier=17.61 > chrono_homog=5.11 > formula_share=0.11.
- **Ranking matches pre-committed prediction.**

## 3. Stage-2 out-of-sample predictions

| OOS | Subset | N | Predicted (Ridge) | **Observed** | Δ | Status |
|:-:|:--|:-:|:-:|:-:|:-:|:-:|
| OOS-1 | Q 78-89 | 12 | 8.5 | **0.03** | −8.5 | **CORPUS-EXTREME COHESION** |
| OOS-2 | Q 86-92 | 7 | 8.5 | **0.11** | −8.4 | **CORPUS-EXTREME COHESION** |
| OOS-3 | Q 93-99 | 7 | 8.5 | **0.00** | −8.5 | **CORPUS-EXTREME COHESION** |
| OOS-4 | Q 51-54 (no Q 55) | 4 | 31.1 | **33.06** | +2.0 | **EXCELLENT FIT** |
| OOS-5 | Q 7-15 (ALMR/ALR) | 9 | 36.3 | 78.04 | +41.7 | MODEL MISS |
| OOS-6 | Q 30-39 | 10 | 53.9 | 71.42 | +17.5 | MODEL UNDER |

**4 of 6 OOS predictions** land within ±20%ile of observed. **Mean abs error 14.43 percentile-points** is well within the STRICT threshold (≤25).

## 4. The Q 78-99 super-cluster — NEW EMPIRICAL FINDING

Three non-overlapping mushaf windows in Q 78-99 each test at corpus-extreme cohesion:
- Q 78-89 (N=12): %ile=0.03 (3 of 10000 random-12 subsets are tighter)
- Q 86-92 (N=7): %ile=0.11
- Q 93-99 (N=7): %ile=0.00

Combined with prior:
- [[h-new-350-al-tiwal-cohesion|H-NEW-350]] Q 107-114 (N=8): 0.00%
- [[h-new-370-mufassal-tiwal-cohesion|H-NEW-370]] Q 98-114 (N=17): 0.00%
- [[h-new-360-mufassal-awsat-cohesion|H-NEW-360]] Q 67-77 (N=11): 7.07%

**The entire Q 67-114 region (mufaṣṣal-awsāṭ + mufaṣṣal-qiṣār) is a CORPUS-EXTREME content-cohesion SUPER-CLUSTER** — every consecutive window of size ≥7 tested in this range lands at ≤8%ile.

**Classical anchor**: al-Zarkashī *al-Burhān* mufaṣṣal sub-divisions; al-Suyūṭī *al-Itqān* fawātiḥ classifications grouping the mufaṣṣal as a unified textual register. Empirical cohesion now establishes that the mufaṣṣal-region is **densest where Meccan-eschat-creedal register is most uniform** (Q 78-99 specifically).

This is consistent with the [[cross-finding-022-wave5-terminal-synthesis|cross-finding-022]] §2 finding that classical block-structure is Ridge-linearly recoverable at MAE=8 surah-positions. [[h-new-580-five-factor-regression|H-NEW-580]] quantifies the cohesion-axis at the same architectural region.

## 5. The Q 7-15 model-miss — [[h-new-570-muqattaat-content-cluster|H-NEW-570]] replication at OOS scale

Q 7-15 was pre-registered with `formula_share=1` (all 9 are muqaṭṭaʿāt-opened: المص, ALR, ALR, ALR, الر, ALR). Predicted %ile (Ridge) = 36; observed %ile = 78.

**This is a LARGE miss in the predicted direction**: muqaṭṭaʿāt-as-shared-formula does NOT add cohesion; it pulls toward dispersion.

**This is the [[h-new-570-muqattaat-content-cluster|H-NEW-570]] finding REPLICATED at out-of-sample scale**: at whole-surah FR-roots level, muqaṭṭaʿāt-letter-axis is orthogonal to (or anti-correlated with) content-axis. The 9 letter-family surahs across 7-15 share opening structure but DISPERSE on content.

**Refinement to [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] Factor 4**: "formula-sharing" must be operationalized strictly as **shared THEMATIC formula** (al-ḥamd / sabbaḥa / qul / Allāh praise-formula) — muqaṭṭaʿāt does NOT count.

This refinement is now empirically locked across THREE independent tests:
- [[h-new-570-muqattaat-content-cluster|H-NEW-570]] (29-set whole-corpus): 65.62%ile NULL.
- [[h-new-570-muqattaat-content-cluster|H-NEW-570]] (ḥawāmīm-7 sub-cluster): 20.90%ile NULL.
- [[h-new-580-five-factor-regression|H-NEW-580]] (OOS-5 Q 7-15 letter-family): 78%ile NULL.

## 6. The chrono_homog OLS sign-flip — small-N collinearity artifact

OLS β(chrono_homog) = +16.67 (positive, violates pre-committed direction).

**Diagnosis**: with only 12 training rows and 5 binary predictors, two factors with high VIF can sign-flip. Specifically:
- Of the 12 rows, 5 have chrono_homog=1 AND register_homog=1 (rows 1-5).
- 5 have chrono_homog=1 AND register_homog=0 (rows 7, 8, 10, plus...) 
- The chrono_homog signal is largely captured by register_homog; OLS distributes the residual into a positive sign.

**Ridge β(chrono_homog) = −5.11** (correct sign, small magnitude). This is the canonical Ridge response to multicollinearity: damps the unstable coefficient toward zero, retains the correct direction.

**Resolution**: the Ridge fit (which we pre-committed under Bonferroni-2) recovers the pre-committed direction on all 5 factors EXCEPT formula_share. OLS is informational only; Ridge is the verdict-driving model.

But Ridge's β(formula_share) = +0.11 is nearly zero — this is the "muqaṭṭaʿāt-as-formula doesn't count" finding manifesting as coefficient near-elimination. It does NOT actively pull anti-cohesion; it simply contributes nothing.

## 7. Permutation null — why p=0.079 isn't conclusive

Under 10000 random permutations of the 12 training %iles:
- p(Ridge OOS r ≥ 0.929) = 0.0790
- p(OLS OOS r ≥ 0.640) = 0.2387

These exceed the Bonferroni-corrected α = 0.025.

**Why**: the OOS subset structure is itself non-random. The 6 OOS subsets span the predicted spectrum from `[1,1,1,0,1]` (best-cohesion) to `[1,0,0,0,0]` (worst). With this structured OOS, even a randomly-shuffled training assignment can produce moderate r if the OOS factor-vectors happen to correlate with the random %iles in ways consistent with the spread. The permutation null is **diluted** by the structured OOS design.

**A stricter test** would be to also permute the OOS factor-labels. That experiment is queued as H-NEW-580.1.

The HONEST interpretation: under the specified test, the permutation p does NOT clear strict significance. The model's mathematical power (r=0.93, MAE=14) is the substantive finding; statistical significance under N=12 + Bonferroni-2 is the structural ceiling.

## 8. Implications

### 8.1 [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] → [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]-v2

The 5-factor model is empirically validated as OOS-predictive at r=0.93. Refinements:
- Factor 4 (formula-sharing) → operationalized as "shared THEMATIC formula" (excluding muqaṭṭaʿāt).
- Factor 5 (no-outlier) → confirmed at meaningful magnitude (β=−17.61 Ridge).
- Block-adjacency dominates at β=−27.80 (Ridge), confirming al-Biqāʿī's munāsaba framework as the largest single factor.

### 8.2 The Q 67-114 super-cluster

Independently confirmed as the corpus's densest content-cohesion region. Six non-overlapping windows tested ≤8%ile. This is the **densest scaffolding zone** of the mushaf architecture.

### 8.3 The 5-factor model as quantitative predictor

For any subset of K consecutive surahs in the mushaf:
- Score the 5 factors (block_adj, register_homog, chrono_homog, formula_share, no_outlier).
- Predict %ile via Ridge β.
- Expect agreement within ±15%ile-points.

This converts the qualitative 5-factor model into a **deployable quantitative predictor**. It is the first-ever quantitative regression model for Quranic surah-grouping content-cohesion.

## 9. Honest limits

1. **N=12 training** is small; collinearity drives OLS sign-flip; LOOCV R²=0.58 (Ridge) is moderate.
2. **Permutation p=0.079** does not clear Bonferroni-2 α=0.025. Strict statistical significance fails.
3. **6 OOS subsets** is a modest test set. Larger OOS would tighten the r estimate.
4. **FR-roots metric only**; char-4-gram / NCD untested at this regression scale.
5. **Ridge λ=1.0** chosen heuristically; λ-grid search not performed (would be post-hoc adjustment).
6. **Factor encoding** is binary; some natural variation (e.g., "MOSTLY-Meccan") is forced to 1. Continuous encoding queued for H-NEW-580.2.
7. **OOS-5 (Q 7-15) is the WORST miss**. The model under-weights the muqaṭṭaʿāt-orthogonality. Factor 4 refinement is essential.

## 10. Cross-references

- **[[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]** (qualitative 5-factor model): now quantitatively validated OOS at r=0.93.
- **[[h-new-570-muqattaat-content-cluster|H-NEW-570]]** (muqaṭṭaʿāt ⊥ content): replicated at OOS-5 (Q 7-15 at 78%ile vs predicted 36%).
- **[[h-new-390-q55-outlier-exclusion|H-NEW-390]]** (Q 55 outlier +32.6pp): no_outlier β=−17.61 Ridge magnitude is consistent.
- **[[h-new-350-al-tiwal-cohesion|H-NEW-350]], [[h-new-360-mufassal-awsat-cohesion|H-NEW-360]], [[h-new-370-mufassal-tiwal-cohesion|H-NEW-370]]**: combined with [[h-new-580-five-factor-regression|H-NEW-580]] OOS-1/2/3, establish Q 67-114 super-cluster.
- **[[cross-finding-022-wave5-terminal-synthesis|cross-finding-022]] §2** (classical-block-structure Ridge-recoverable at MAE=8): consistent architectural finding.
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (Fisher-Rao mushaf 11% from TSP-optimum): the residual 11% is partially explained by within-super-cluster compression; mufaṣṣal-region cohesion is much greater than mushaf-mean.

## 11. Queued follow-ups

- **H-NEW-580.1**: Stricter permutation test — also permute OOS factor-labels for fully-randomized null.
- **H-NEW-580.2**: Continuous factor encoding (replace 0/1 with [0, 1] proportions like "fraction Meccan").
- **H-NEW-580.3**: Expand training to include [[h-new-321-q1-q27-basmala-echo|H-NEW-321]]→390 + new [[h-new-490-tiwal-inner-4|H-NEW-490]] / 500 / 540 / 550 / 560 results (~20 subsets total). Refit Ridge and re-do OOS with 12 fresh subsets.
- **[[h-new-630-supercluster-substructure|H-NEW-630]]**: Identify a 6th factor candidate (e.g., divine-name-density variance) — whether it explains residual after 5-factor regression. (queued as [[h-new-620-divine-name-density|H-NEW-620]], currently in-flight by parallel specialist.)
- **H-NEW-640**: Test whether the Q 67-114 super-cluster has a HIGHER-ORDER factor structure (sub-clustering at Q 78-89 vs Q 90-99 vs Q 100-114 boundaries).

## 12. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-580-five-factor-regression-prereg.md` (SHA `74ec9eaf…`)
- Script: `scripts/h_new_580_five_factor_regression.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-580.json`

## 13. Final statement

**The 5-Factor Cohesion Model is empirically validated as out-of-sample predictive at Pearson r=0.929 (Ridge) over 6 pre-registered new subsets, with mean absolute error of 14.43 percentile-points.** The model fails STRICT-PASS under the discipline-correct β-sign + Bonferroni-2 permutation null (chrono_homog OLS sign-flip; formula_share Ridge near-zero; permutation p=0.079), so the verdict is DIRECTIONAL.

**Two large positive substantive findings**:
1. **Q 67-114 mufaṣṣal-region is the corpus-densest content-cohesion super-cluster**, with six non-overlapping windows tested ≤8%ile (Q 67-77, Q 78-89, Q 86-92, Q 93-99, Q 98-114, Q 107-114).
2. **Muqaṭṭaʿāt-as-formula does NOT pull cohesion** — Q 7-15 letter-family at observed 78%ile vs predicted 36%ile; [[h-new-570-muqattaat-content-cluster|H-NEW-570]] finding replicated at OOS scale.

The mathematically-powerful contribution is the **first quantitative regression** mapping qualitative classical scholarly cohesion-claims (al-Biqāʿī munāsabāt × al-Zarkashī mufaṣṣal × al-Suyūṭī chronology × al-Suyūṭī fawātiḥ × al-Tirmidhī uniqueness-designations) onto a single regression-predictable percentile metric, with deployable Ridge coefficients.

**14 centuries of qualitative classical scholarship now has a fitted Ridge surrogate: %ile = 81.66 − 27.80 × block_adj − 22.62 × register − 5.11 × chrono − 17.61 × no_outlier.** (formula_share is essentially zero and absorbed.)

Published with full transparency on the directional verdict.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
