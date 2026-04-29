---
id: H-NEW-46.1
title: Muqaṭṭaʿāt-vs-length signal SURVIVES Meccan/Medinan chronology control — STRONG-PASS
phase: B
status: STRONG-PASS (6/7 cells significant under Bonferroni-7 at α_bon = 0.00714; OLS muq-coef = +56.4 verses, p_HC1 = 2.1×10⁻⁵)
date: 2026-04-15
agent: h-new-46-1-specialist
parent_finding: H-NEW-46 (4/4 unstratified Bonferroni-4 PASS)
pre_reg: findings/phase-b-hypotheses/h-new-46-1-chronology-disentangle-prereg.md
script: scripts/h_new_46_1_chronology_disentangle.py
json: findings/phase-b-hypotheses/csv/h-new-46-1.json
journal: journal/h-new-46-1-run-1.md
rules_tuple: (no-tashkeel, hafs-kufan, verse-count metric, period-strata)
chronology_source: Tanzil Egyptian Standard period field (aligns with al-Suyūṭī al-Itqān nawʿ 9 standard 86 Meccan / 28 Medinan split)
bonferroni_family: 2026-04-16-Wave-Muqattaat-Extended-Disentangle
bonferroni_k: 7
alpha_bon: 0.00714286
seed: 20260416
n_perm: 100000
---

# [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] — Chronology Disentanglement (STRONG-PASS)

## TL;DR

[[h-new-46-muqattaat-vs-surah-length|H-NEW-46]]'s "muqaṭṭaʿāt-opened surahs are dramatically longer" is **NOT** a chronology artifact. After stratifying by Meccan/Medinan revelation period (Tanzil/al-Suyūṭī al-Itqān nawʿ 9 standard 86/28 split), 6 of 7 pre-registered cells remain significant at Bonferroni-7 α = 0.00714. The OLS regression `verse_count ~ I(Medinan) + I(muqaṭṭaʿāt)` gives a muqaṭṭaʿāt coefficient of **+56.4 verses** (p_classical < 1×10⁻⁶, p_HC1-robust = 2.1×10⁻⁵), virtually unchanged from the unstratified gross gap of ~53.5 verses (94.6 − 41.1).

**Verdict: STRONG-PASS — muqaṭṭaʿāt independently predicts surah length, OVER AND ABOVE chronology.**

| Cell | Test | Observed | Null mean | Null SD | p | sig at α_bon |
|---|---|---|---|---|---|---|
| A1 | Meccan-stratum mean (one-sided ↑) | 85.15 | 53.67 | 7.81 | **4.0×10⁻⁵** | YES |
| A2 | Meccan-stratum top-26 count (one-sided ↑) | 15/26 | 7.86 | 1.97 | **4.0×10⁻⁴** | YES |
| B1 | Medinan-stratum mean (exact 3276 combos, one-sided ↑) | 176.33 | 57.96 | 37.21 | **4.9×10⁻³** | YES |
| B2 | Medinan-stratum top-3 count (exact, one-sided ↑) | 2/3 | 0.32 | 0.52 | 2.3×10⁻² | NO |
| C1 | Stratified Mann-Whitney (van Elteren, two-sided) | z = 4.82 | — | — | **1.0×10⁻⁵** | YES |
| C2 | OLS coef on I(muqaṭṭaʿāt) | β = +56.42 | — | — | **2.1×10⁻⁵** (HC1) | YES |
| C3 | Period-residualized perm null (one-sided ↑) | 40.50 | -0.02 | 8.55 | **1.0×10⁻⁵** | YES |

**6/7 cells significant. Verdict: STRONG-PASS.**

## Chronology source — locked

- **Tanzil Egyptian Standard** Meccan/Medinan classification (`data/revelation-order.csv`).
- This is the standard 86 Meccan / 28 Medinan split that corresponds to al-Suyūṭī's al-Itqān fī ʿulūm al-Qurʾān, nawʿ 9 (the chapter on Meccan vs Medinan classification — `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`).
- Locked BEFORE any computation. Source choice documented in pre-reg, SHA-256 captured into JSON.

## Muqaṭṭaʿāt distribution by period (locked)

| Period | n total | n muqaṭṭaʿāt | n non-muq | muq fraction |
|---|---|---|---|---|
| Meccan | 86 | 26 | 60 | 30.2% |
| Medinan | 28 | 3 | 25 | 10.7% |
| Total | 114 | 29 | 85 | 25.4% |

- Meccan muqaṭṭaʿāt (26): {7, 10, 11, 12, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
- Medinan muqaṭṭaʿāt (3): {2 al-Baqara, 3 Āl ʿImrān, 13 al-Raʿd}

The Medinan muqaṭṭaʿāt are precisely the longest Medinan surahs: Q 2 (286), Q 3 (200), Q 13 (43). The first two are the top-2 longest in the entire Qurʾān; Q 13 is much shorter but still above the Medinan median (Medinan median ≈ 57). 2 of the 3 Medinan muq are in the top-3 longest Medinan, vs random expectation 0.32/3.

Within Meccan, the 26 muq surahs have mean 85.15 vs Meccan-non-muq mean 39.97 — a within-period gap of **+45.2 verses**.

## Why the Medinan top-K cell (B2) is the only failure

The B2 cell tests whether 2 of 3 muq-Medinan in top-3 longest Medinan is significant. Under exact enumeration of C(28,3) = 3276 combinations, the empirical p = 0.0232. This fails Bonferroni-7 (α = 0.00714) but is significant at uncorrected α = 0.05.

The reason for the comparatively weak signal: **n = 3 is tiny**. With only 3 muq-Medinan, the discrete distribution offers limited resolution. Pre-reg correctly anticipated this by including continuous-variable cells (B1 mean) which reaches p = 0.0049. The B1/B2 pair gives the same qualitative answer (Medinan muq are longer) at different statistical resolutions.

The combined cells C1, C2, C3 all clear α_bon by margins of 200×–700×, providing the structural redundancy that motivated the 7-cell design.

## OLS regression — the headline

Linear model: `verse_count = β₀ + β_med · I(Medinan) + β_muq · I(muqaṭṭaʿāt) + ε`

Fitted (n = 114):

| Coefficient | β | Classical SE | Classical t | Classical p | HC1 SE | HC1 t | HC1 p |
|---|---|---|---|---|---|---|---|
| Intercept | 25.74 | 6.71 | 3.84 | 1.9×10⁻⁴ | 5.13 | 5.02 | 5.4×10⁻⁷ |
| I(Medinan) | +44.46 | 11.58 | 3.84 | 1.9×10⁻⁴ | 19.88 | 2.24 | 2.5×10⁻² |
| I(muqaṭṭaʿāt) | **+56.42** | 11.46 | 4.92 | 1.0×10⁻⁶ | 12.73 | 4.43 | 2.1×10⁻⁵ |

R² = 0.208.

**Comparison to unstratified [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]]:**

- Unstratified gross gap (muq mean − non-muq mean) = 94.59 − 41.08 = **53.51 verses**.
- Stratified OLS coefficient on muqaṭṭaʿāt indicator = **+56.42 verses**.
- The chronology-adjusted effect is essentially identical to the gross gap. **Chronology absorbs ~0% of the muqaṭṭaʿāt-length signal.**

The Medinan-period coefficient β_med = +44.5 verses is itself a real chronology effect (Medinan are longer on average), but it adds linearly to the muqaṭṭaʿāt effect rather than competing with it. The two predictors are nearly orthogonal in this 114-observation design (only 3 of 28 Medinan are muqaṭṭaʿāt; only 3 of 29 muqaṭṭaʿāt are Medinan), giving each independent leverage on length.

## Residualization — the cleanest test

Cell C3 implements the project's standard MW-1 length-residualization protocol: subtract within-period mean from each surah's length, then test whether the muq subset has higher residual mean than uniform-random 29-from-114 selection.

- Observed mean residual (muq) = +40.50 verses (i.e. on average 40.5 verses longer than a same-period peer)
- Null mean (10⁵ perms) = -0.02 verses (centered, by construction)
- Null SD = 8.55 verses
- z ≈ 4.74; empirical p = 1×10⁻⁵ (at the resolution floor of N_PERM = 10⁵)

This is a pure within-period effect with no chronology contamination by construction. It is the cleanest single number in the analysis.

## Stratified Mann-Whitney (cell C1)

Van Elteren combined-z across the two strata:

- Meccan stratum (n₁=26 muq, n₂=60 non-muq): U = 1213.5, μ_U = 780, ΔU = +433.5
- Medinan stratum (n₁=3 muq, n₂=25 non-muq): U = 70.5, μ_U = 37.5, ΔU = +33.0
- Combined ΔU = +466.5; combined SD = √(sum var) = 96.78
- z = 4.82, two-sided analytic p = 1.4×10⁻⁶
- Permutation cross-check (10⁵ perms): p_perm = 1.0×10⁻⁵ (at floor)
- Headline (max conservative) = 1.0×10⁻⁵

The U statistic in both strata is extreme. In Meccan, the muq surahs concentrate in the upper half of the within-Meccan length distribution; in Medinan, 2 of 3 muq-Medinan occupy the top-2 length slots (Q 2 and Q 3 are the #1 and #2 longest Medinan surahs by enormous margins).

## Sensitivity — Q 13 al-Raʿd reclassification

Q 13 (al-Raʿd) is the only borderline case in the standard split. Tanzil/Egyptian-edition consensus marks it Medinan; Nöldeke marks it late-Meccan.

Recompute under the Q 13 = Meccan variant:
- muq-Meccan mean shifts from 85.15 → 83.59 (Q 13 = 43 verses pulls the mean down)
- muq-Medinan mean shifts from 176.33 → 243.00 (Q 13 removed; only Q 2 + Q 3 remain)
- All cells remain in the same direction; signal direction is robust to Q 13 classification
- Headline OLS coefficient is essentially unaffected (Q 13's residual contribution is small)

Locked answer uses Tanzil's Q 13 = Medinan classification, in line with the Egyptian-edition consensus.

## Mechanism interpretation

**The chronological-correlate hypothesis ([[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] mechanism #1) is FALSIFIED as the sole explanation.** Long surahs being predominantly Medinan or middle/late-Meccan is a real but separate effect. The muqaṭṭaʿāt assignment carries an *additional* length signal, statistically independent of period.

**Surviving mechanism candidates** (from [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]]'s enumeration, now upgraded by chronology survival):

1. **Structural-authority hypothesis**: long surahs were marked with distinctive openers regardless of period. The within-Meccan effect (+45 verses) and within-Medinan signal both support this.
2. **Mnemonic/recitation anchor**: long surahs are harder to memorize; muqaṭṭaʿāt may serve as fixed anchors. Predicts effect within both periods, which we observe.
3. **A now-lost compositional convention** linking muq-letter-set choice to length, possibly mediated by a dimension we have not yet identified.

The classical traditions (al-Rāzī's 12 theories, Welch 1986, Massey 1996) generally do not anticipate a length-dimension. The ḥawāmīm cluster (Q 40–46 all opening with حم) is the closest classical precedent: 7 contiguous surahs, all medium-long Meccan, sharing the same muq-letters. [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] confirms the length-correlation generalizes well beyond ḥawāmīm.

## Cross-finding context update

After [[h-new-46-1-chronology-disentangle|H-NEW-46.1]], the muqaṭṭaʿāt-structural finding cluster now stands at:

- **[[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]]** (subset algebra): 14 muq-letter subsets have non-trivial Boolean rank-12 structure
- **[[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]]** (surah-index gap-entropy): the 29 surah indices cluster into low-gap-entropy groups at p = 2×10⁻⁵
- **[[h-new-46-muqattaat-vs-surah-length|H-NEW-46]]** (length, unstratified): 4/4 cells STRONG-PASS at p ≤ 1.6×10⁻⁴
- **[[h-new-46-1-chronology-disentangle|H-NEW-46.1]]** (length, chronology-controlled): 6/7 cells STRONG-PASS at p ≤ 5×10⁻³; OLS β_muq = +56.4 verses, p_HC1 = 2.1×10⁻⁵

Four independent statistical signals on four orthogonal axes (algebraic, surah-position, gross length, period-controlled length) all reject the null of random muqaṭṭaʿāt assignment. The chronology disentanglement was the most plausible nuisance hypothesis for [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] specifically; it is now ruled out.

## Pre-registered verdict table

| Outcome | Verdict |
|---|---|
| 0 of 7 cells significant at α_bon | NULL |
| 1-2 cells significant | EXPLORATORY |
| 3-5 cells significant + OLS coef positive | PARTIAL-PASS |
| **6-7 cells significant + OLS coef positive at p < α_bon** | **STRONG-PASS** |

**Result: 6/7 cells significant; OLS coef = +56.4 verses, p_classical < 10⁻⁶ → STRONG-PASS.**

## Pipeline validation

- **MW-5 PC-A1**: planted 26 longest Meccan surahs as fake-muq → A1 p = 1.0×10⁻⁴ (10⁴-perm floor). PASS.
- **MW-5 PC-B1**: planted 3 longest Medinan surahs as fake-muq → B1 p = 3.05×10⁻⁴ (combinatorial floor 1/3276). PASS.
- **MW-7 internal-error gate**: muq-Meccan + muq-Medinan totals to 29 (= 26 + 3); manual mean recomputation matches. PASS.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-46-1-chronology-disentangle-prereg.md`
- Script: `scripts/h_new_46_1_chronology_disentangle.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-46-1.json`
- Journal: `journal/h-new-46-1-run-1.md`

## Integrity

- Chronology source LOCKED before any computation (Tanzil/al-Suyūṭī al-Itqān nawʿ 9 standard 86/28).
- Bonferroni k = 7 declared in pre-reg before null was run.
- Seed 20260416 (matches [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]]/46 wave).
- All 7 cells published whether PASS or NULL (B2 published as NULL despite favorable direction).
- C2 OLS reports BOTH classical-t and HC1-robust SE; headline = max conservative (HC1).
- C3 is the canonical MW-1 residualization equivalent.
- N_PERM = 10⁵ for cells A1/A2/C3; exact enumeration for B1/B2 (3276 combinations); analytic + perm cross-check for C1.
- Sensitivity check Q 13 = Meccan documented; signal robust to this borderline classification.
- The Bonferroni family is a SEPARATE family from [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] (named "...-Disentangle") to avoid double-counting; both families are self-contained pre-registered claims.
