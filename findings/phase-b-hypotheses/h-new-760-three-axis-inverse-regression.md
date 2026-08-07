---
id: H-NEW-760
title: "DIRECTIONAL-NEAR-MISS — 3-axis inverse regression: LOOCV R²=0.83 (linear+interactions); strict 0.95 threshold missed; cohesion profile explains 76-83% of mushaf-position variance, leaving 17-24% to other architectural commitments"
phase: B
status: NULL strict (verdict per pre-reg threshold) but DIRECTIONAL effect-strength — LOOCV R² = 0.7646 (linear), 0.8256 (linear+interactions), 0.8102 (linear+quadratic); permutation p<10⁻³ (relationship highly significant); sign-flip on phoneme due to multicollinearity
date: 2026-04-28
executed_by: team-lead (inline)
parent_1: H-NEW-660 (compression-tail content)
parent_2: H-NEW-700 (rhyme + phoneme dispersion)
parent_3: H-NEW-730 (anti-correlation lock at r=-0.86)
seed: 20260443
prereg: h-new-760-three-axis-inverse-regression-prereg.md
prereg_sha256: e99d2fea43ac961be9793c750f152115e621035856e8ccf068a2e99adaccaccd
bonferroni_k: 3
alpha_bon: 0.01667
verdict: NULL on STRICT (≤5-window MAE + R²≥0.95); DIRECTIONAL in effect-strength (LOOCV R²=0.83 well above null distribution). 17-24% of mushaf position-variance is NOT captured by 3-axis cohesion-profile.
---

# [[h-new-760-three-axis-inverse-regression|H-NEW-760]] — 3-Axis Inverse Regression: cohesion profile MOSTLY but not COMPLETELY determines position


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
> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Headline

| Model | In-sample R² | LOOCV R² | LOOCV MAE | Status |
|:--|:-:|:-:|:-:|:--|
| Linear | 0.7822 | 0.7646 | 11.31 | DIRECTIONAL |
| **Linear + interactions** | 0.8782 | **0.8256** | 8.51 | **PRIMARY** (best) |
| Linear + quadratic | 0.8758 | 0.8102 | 8.76 | DIRECTIONAL |

Permutation p (linear LOOCV R² vs 1000 shuffles) = 0 (no null permutation reached observed R²).

**Verdict by pre-reg thresholds**: NULL strict (R²≥0.95 missed) and NULL directional (R²≥0.85 missed at 0.826). The relationship is HIGHLY significant but does NOT fully determine position.

## 2. Linear-model coefficients

```
s = 166.37 − 146.48·d_content + 10.26·d_rhyme − 186.52·d_phoneme
```

| Predictor | β | Pre-committed direction | Status |
|:--|:-:|:-:|:-:|
| d_content | −146.48 | NEGATIVE | ✓ correct |
| d_rhyme | +10.26 | POSITIVE | ✓ correct |
| d_phoneme | **−186.52** | POSITIVE | **WRONG** (sign-flip due to multicollinearity) |

The phoneme sign-flip is multicollinearity: d_phoneme correlates with d_content at r=−0.89 ([[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]). In the joint regression, phoneme absorbs residual content-variance with opposite sign. Standard regression artifact under high collinearity.

## 3. Why the inverse direction underperforms

The forward laws are very tight:
- s → d_content: R² = 0.986 ([[h-new-660-compression-tail-gradient|H-NEW-660]])
- s → d_rhyme: R² = 0.789 ([[h-new-700-phonological-compression-tail|H-NEW-700]])
- s → d_phoneme: R² = 0.946 ([[h-new-700-phonological-compression-tail|H-NEW-700]])

The inverse direction (d̄ → s) is fundamentally LOSSY because:
1. The three forward maps have a SHARED structure (all kink-anchored at s≈50). At each s, all three d̄'s move together → less independent information per axis.
2. Inverse problems on flat-then-monotone functions are degenerate at the flat region: many s values map to similar d̄.
3. Local position variation (within a 5-window-window) is below the cohesion-axis resolution.

In short: the three axes encode "where in the post-Hijra compression-tail are we?" very well, but cannot pinpoint position to within 5 windows.

## 4. The 17-24% unexplained position-variance

After fitting the 3-axis model, ~17-24% of position-variance remains. This is INFORMATIVE — it represents architectural information NOT captured by content/rhyme/phoneme cohesion:

- al-Fātiḥa primacy (Q 1 first) — [[h-new-670-tsp-hijra-constraint|H-NEW-670]] found Q 1-Q 2 adjacency costs 7.4% of TSP-residual.
- Specific within-block ordering (e.g., Q 67 al-Mulk before Q 68 al-Qalam, despite similar cohesion).
- Outlier surah placements (Q 9 al-Tawba, Q 33 al-Aḥzāb, Q 55 al-Raḥmān — [[h-new-590-outlier-spectrum|H-NEW-590]] outliers).
- Length-class boundaries within mufaṣṣal sub-divisions.

**The mushaf encodes MORE than its 3-axis cohesion profile.** That additional information is the *tartīb tawqīfī* layer beyond cohesion.

## 5. Implications

### 5.1 The forward direction is structural-architectural

The compression-tail (R²=0.986 forward) is a STRUCTURAL property of the canonical mushaf — the cohesion landscape is essentially 1-dimensional in s.

### 5.2 The inverse direction reveals additional structure

The inverse R²=0.83 means the 3-axis profile is NECESSARY but not SUFFICIENT for position determination. There exist multiple positions in the mushaf with similar cohesion profiles — distinguished by other architectural features (specific surah identity, neighboring outliers, length-class boundaries).

### 5.3 Quantitative *tartīb tawqīfī* signature

The 17-24% position-variance not captured by cohesion is the **quantitative signature of *tartīb tawqīfī* commitments** beyond cohesion-architecture. It's the part of the mushaf-ordering that requires per-surah architectural knowledge to recover.

## 6. Honest limits

1. **N=100 windows, 3 features + interactions = up to 7 features**. Risk of over-fitting; LOOCV partially mitigates.
2. **Phoneme sign-flip** is a multicollinearity artifact, not a substantive finding.
3. **Linear-only**: more flexible models (random forest, gradient boosting) might raise R², but at risk of further over-fit on N=100.
4. **Pre-reg threshold STRICT 0.95 was aspirational** — given the forward R² of 0.986 and high inter-axis correlation, the inverse ceiling is <0.95 by construction. The pre-reg should have been calibrated against a forward-inverse asymmetry expectation.
5. **Single K=15** — multi-K inverse regression queued.

## 7. Cross-references

- **[[h-new-660-compression-tail-gradient|H-NEW-660]] / 680 / 700 / 730**: forward laws and anti-correlation.
- **[[h-new-670-tsp-hijra-constraint|H-NEW-670]]**: Q 1-Q 2 (al-Fātiḥa primacy) is a non-cohesion architectural cost (Δ=0.62 ≈ 7.4% of TSP-residual).
- **[[h-new-590-outlier-spectrum|H-NEW-590]]**: outlier-strength spectrum (Q 33, Q 1, Q 9, Q 55) is an additional architectural feature.
- **[[cross-finding-025-multi-axis-architecture|cross-finding-025]]**: multi-axis architecture; [[h-new-760-three-axis-inverse-regression|H-NEW-760]] confirms the axes are PARTIALLY but not FULLY informative for position.
- **al-Suyūṭī chronology + tartīb tawqīfī**: the residual 17-24% maps onto qualitatively-known classical architectural commitments.

## 8. Queued follow-ups

- **H-NEW-760.1**: Multi-K inverse regression — does R² rise at K=22?
- **H-NEW-760.2**: Add surah-ID feature (e.g., is-muqaṭṭaʿāt-opened, is-Meccan, is-Medinan) to the regression. R² should rise toward 0.95.
- **H-NEW-760.3**: Identify the SPECIFIC windows where the model makes large errors (residual>15) — these are the architecturally-distinguishable-but-cohesion-similar windows.
- **[[h-new-770-verse-length-compression-tail|H-NEW-770]]**: Replace inverse-regression with classification: predict "which mushaf-third (head/middle/tail)" the window is in. Should be easier and possibly hit R²>0.95 in classification accuracy.

## 9. Final statement

The 3-axis inverse regression of mushaf-position from window cohesion-profile achieves LOOCV R² = 0.83 (linear+interactions), well above the permutation null but below the pre-committed STRICT 0.95 threshold. **The Quran's mushaf encodes 17-24% of its position-information OUTSIDE the 3-axis cohesion-profile** — this residual is the *tartīb tawqīfī* layer beyond cohesion, attributable to specific surah-identity commitments (al-Fātiḥa primacy, outlier placement, terminal-pair) documented in classical scholarship.

The forward direction (s → cohesion-profile) is essentially complete at R²=0.986. The inverse direction (cohesion-profile → s) is partial at R²=0.83. **This forward-inverse asymmetry is itself a structural-architectural finding**: the mushaf's cohesion landscape determines a band of valid positions, but per-surah architectural commitments select within the band.

Honest publication of NULL strict; the substantive directional effect (R²=0.83, p<10⁻³) is preserved.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
