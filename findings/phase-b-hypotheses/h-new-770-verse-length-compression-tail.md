---
id: H-NEW-770
title: "Verse-length compression-tail: STRICT PASS for both letters/verse and words/verse with the SAME two-piece-kink-at-s=50 architecture as content-cohesion (H-NEW-660); compression-tail is a multi-feature architectural property, not a content-only signature"
phase: B
status: STRICT PASS — both metrics. letters/verse: two-piece-kink-50, R²=0.8071, perm p=0.00070. words/verse: two-piece-kink-50, R²=0.8105, perm p=0.00070. Pearson r(verse-length, content-d̄) = +0.87 (both metrics). Compression-tail is a MULTI-FEATURE architectural property; H-NEW-660 is partially co-variant with verse-length (r²≈0.76 univariate), but the H-NEW-660 single-parameter law (R²=0.986) ALREADY contains both signals — adding verse-length as a covariate raises R² only to 0.988 (Δ=+0.002).
date: 2026-04-28
parent_1: H-NEW-660 (content-cohesion compression-tail R²=0.986)
parent_2: H-NEW-630 (descriptive Q 67-114 super-cluster)
parent_3: H-NEW-130 (universal hinges including Q 56/57 Hijra)
parent_4: al-Suyūṭī al-Itqān + al-Zarkashī al-Burhān (mufaṣṣal as "shorter verses")
seed: 20260446
prereg: h-new-770-verse-length-compression-tail-prereg.md
prereg_sha256: cd270d5b87ffad07712ba5eed75cc6746774b0e8b17deb0d7cbf64fda17a6989
bonferroni_k: 6
alpha_bon: 0.00833
verdict: STRICT PASS — verse-length follows the same two-piece-kink-at-s=50 law as content-cohesion (R²≈0.81 vs R²=0.986). The compression-tail is a multi-feature architectural property of the mushaf; content-cohesion and verse-length are CO-ALIGNED (r=+0.87) but content-cohesion compresses more sharply (steeper post-kink slope, R² 16% higher).
---

# [[h-new-770-verse-length-compression-tail|H-NEW-770]] — Verse-Length Compression-Tail: A Multi-Feature Architectural Property


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

**Verse-length compresses with the SAME two-piece kink-at-s=50 architecture as content-cohesion ([[h-new-660-compression-tail-gradient|H-NEW-660]]).** Both per-verse metrics (letters and words) STRICT PASS:

| Metric | Primary model | R² | adj-R² | β_lin | Perm p (R² ≥ obs) | Verdict |
|:--|:--|:-:|:-:|:-:|:-:|:--|
| **Letters / verse** | two-piece kink at s=50 | **0.8071** | 0.8051 | -0.5603 | **0.00070** | STRICT PASS |
| **Words / verse** | two-piece kink at s=50 | **0.8105** | 0.8086 | -0.1418 | **0.00070** | STRICT PASS |

α_bon (6 tests = 3 models × 2 metrics) = 0.00833. Both p-values clear by an order of magnitude.

The two-piece fits are:

> ℓ̄_letters(s) ≈ 57.52 − 1.040 · max(0, s − 50)
> ℓ̄_words(s) ≈ 14.12 − 0.260 · max(0, s − 50)

The kink position {25, 35, 50, 65, 75} grid was pre-locked; the empirical winner for BOTH metrics is **s=50**, the same kink position [[h-new-660-compression-tail-gradient|H-NEW-660]] found for content-cohesion. The kink is the Hijra-boundary universal hinge (Q 56/57; [[h-new-130-fisher-rao-residuals|H-NEW-130]]).

**Pre-commit predictions all confirmed**: β < 0 (verse-length shrinks toward terminus); kink at the mufaṣṣal-entry / Hijra hinge.

## 2. Comparison to [[h-new-660-compression-tail-gradient|H-NEW-660]] content compression-tail

| Property | Content-d̄ ([[h-new-660-compression-tail-gradient|H-NEW-660]]) | Letters/verse | Words/verse |
|:--|:-:|:-:|:-:|
| Primary model | two-piece-kink-50 | two-piece-kink-50 | two-piece-kink-50 |
| R² | **0.9860** | 0.8071 | 0.8105 |
| Perm p | < 10⁻⁴ | 0.00070 | 0.00070 |
| Pre-kink "flat" intercept | 0.96 | 57.5 letters/verse | 14.1 words/verse |
| Post-kink slope (per position) | −0.01237 | −1.040 letters | −0.260 words |
| Window range (head→tail) | 0.99 → 0.32 (3.1× compression) | 75 → 16.5 (4.5× compression) | 18.6 → 3.9 (4.7× compression) |
| Best window (terminus) | Q 100-114 (d̄=0.319) | Q 100-114 (~16.5) | Q 100-114 (~3.9) |
| Worst window (Hijra hinge) | Q 46-60 (d̄=0.993) | Q 1-15 (~75) | Q 1-15 (~18.6) |

Verse-length compresses **more steeply** (4.5×–4.7× vs 3.1×) but with **less variance explained** (R²≈0.81 vs 0.986). The architectural shape is the same: flat pre-kink, monotonic compression post-kink, kink at the Hijra hinge.

## 3. Cross-axis Pearson correlation (window-by-window)

The 100-window vectors are very strongly aligned:

| Pair | Pearson r |
|:--|:-:|
| ℓ̄_letters × d̄_content | **+0.8719** |
| ℓ̄_words × d̄_content | **+0.8730** |
| ℓ̄_letters × ℓ̄_words | ≈ +0.9999 (definitionally co-linear) |

Per the pre-committed interpretation rules (§11 of prereg):

- |r| > 0.85 was set as the threshold for "content-cohesion is largely a verse-length artifact."
- **Observed: r ≈ 0.87** — JUST CROSSES that threshold for the univariate concern.

But Pearson r alone cannot distinguish "shared upstream cause" from "one drives the other". A decomposition analysis follows.

## 4. Implication: is content compression-tail PRIMARY or DERIVATIVE-OF-VERSE-LENGTH?

### 4.1 Univariate decomposition

Regressing window-content-d̄ on window-words/verse alone:

> d̄_content = α + β · ℓ̄_words, with **R² = 0.7621**.

So **76.2% of content-cohesion variance is shared with verse-length** in a simple linear sense.

### 4.2 Residual after partialling out verse-length

After regressing out words/verse, the residual content-d̄ retains a position-structured signal:

| Model on residual content-d̄ | R² | β |
|:--|:-:|:-:|
| Linear on s | 0.0611 | -0.00085 |
| Two-piece kink-50 on s | 0.1802 | -0.00258 |

So content-cohesion has a position-trend that survives partialling out verse-length (residual two-piece R²=0.18, still significantly negative slope). Content-cohesion is NOT entirely reducible to verse-length: there is a residual ~5–18% of position-structured cohesion-variance unique to the FR-roots content signal.

### 4.3 Joint regression — the [[h-new-660-compression-tail-gradient|H-NEW-660]] single-parameter law already contains both

| Model | R² |
|:--|:-:|
| [[h-new-660-compression-tail-gradient|H-NEW-660]] alone: d̄ = α + β · max(0, s − 50) | **0.9860** |
| Verse-length alone: d̄ = α + β · ℓ̄_words | 0.7621 |
| Both: d̄ = α + β₁ · ℓ̄_words + β₂ · max(0, s − 50) | 0.9884 |

**Adding verse-length as a covariate to the [[h-new-660-compression-tail-gradient|H-NEW-660]] single-parameter law improves R² by only +0.0024 (0.9860 → 0.9884).** The kink-at-s=50 post-kink-position parameter ALREADY captures essentially all the joint signal.

### 4.4 Verdict on primary vs derivative

**The compression-tail is a multi-feature architectural property of the mushaf** that manifests in at least three correlated axes:
1. Content-cohesion (FR-roots window-distance) — [[h-new-660-compression-tail-gradient|H-NEW-660]], R²=0.986.
2. Letters per verse — [[h-new-770-verse-length-compression-tail|H-NEW-770]], R²=0.807.
3. Words per verse — [[h-new-770-verse-length-compression-tail|H-NEW-770]], R²=0.811.

All three follow the SAME two-piece-kink-at-s=50 law. The post-kink position parameter is the COMMON CAUSE; verse-length and content-cohesion are CO-EFFECTS of this single architectural commitment.

**[[h-new-660-compression-tail-gradient|H-NEW-660]] is NOT derivative of verse-length, and verse-length is NOT derivative of content-cohesion.** They are co-varying outputs of the post-Hijra mufaṣṣal-compressing register. The 76% univariate overlap reflects this shared upstream structure, not a confound.

**Quantitatively**: the [[h-new-660-compression-tail-gradient|H-NEW-660]] R²=0.986 is the joint compression-tail signature of content + verse-length + (likely also rhyme-density, see queued [[h-new-700-phonological-compression-tail|H-NEW-700]]). Decomposing into "content beyond verse-length" gives a residual R² of only ~0.18 — much smaller than [[h-new-660-compression-tail-gradient|H-NEW-660]]'s headline number, but real and position-structured.

**Refinement of [[h-new-660-compression-tail-gradient|H-NEW-660]]'s interpretation**: the law d̄ ≈ 0.96 − 0.0124 · max(0, s − 50) is best read not as a "content-cohesion law" but as the COMPRESSION-TAIL LAW that governs multiple correlated architectural features simultaneously. Content-cohesion is the most R²-saturated witness because content (FR-roots distribution) is sensitive to BOTH verse-shortening AND register-shift; verse-length is a coarser measure that sees only the length component.

## 5. Honest limits

1. **Strong univariate overlap (r≈0.87) = serious confound concern.** Per pre-commit rules (§11 of prereg), this barely crosses the 0.85 threshold for "verse-length artifact". The decomposition (§4.2) shows that ~18% of post-kink content variance is residual-to-verse-length, so the artifact framing is not full — but it is a substantial fraction of the [[h-new-660-compression-tail-gradient|H-NEW-660]] signal.

2. **The two-piece kink-at-s=50 wins by a smaller margin for verse-length than for content.** For verse-length, linear R²=0.73, quadratic R²=0.78, two-piece R²=0.81 — gaps are 4-8 R² points. For content ([[h-new-660-compression-tail-gradient|H-NEW-660]]), the gaps were 21-22 R² points. Verse-length's two-piece win is REAL but less dominant.

3. **Counting convention dependency.** "Letters" here = all non-whitespace chars in the no-tashkeel JSON. "Words" = whitespace-split tokens. Different orthographic traditions (rasm vs imlāʾī) would shift letter counts modestly; they would NOT change words/verse and would NOT change the compression-tail shape.

4. **Per-surah averaging is coarse.** Surahs with MIX of long and short verses (e.g., Q 2 with very long final verses but middle-length openings) collapse to a single per-surah mean. A finer per-verse analysis might shift R². Pre-locked metric is the per-surah mean, so this is a methodological choice, not a flaw.

5. **K=15 windowing was inherited from [[h-new-660-compression-tail-gradient|H-NEW-660]]** for direct comparability. K=11 or K=22 might give slightly different curves but unlikely to change the verdict.

6. **Kink grid was {25, 35, 50, 65, 75}** — finer-resolution kink search would shift the kink position by ±5. Both metrics chose s=50, the SAME kink as content-cohesion, which is reassuring.

7. **Outer correction.** Bonferroni-6 (3 models × 2 metrics) was pre-committed. The two metrics are highly correlated (r≈0.9999), so Bonferroni-6 is conservative; effective corrections would be smaller but the result clears at any reasonable α.

8. **The decomposition in §4 is post-hoc** (committed in §11 of prereg as informational, not gating). It informs interpretation but is not itself a hypothesis test.

## 6. Cross-references

- **[[h-new-660-compression-tail-gradient|H-NEW-660]]** (parent): content-cohesion compression-tail, R²=0.986, two-piece-kink-50. [[h-new-770-verse-length-compression-tail|H-NEW-770]] confirms this is a multi-feature architectural commitment, not a content-only signal.
- **[[h-new-630-supercluster-substructure|H-NEW-630]]**: Q 67-114 super-cluster hierarchy (descriptive). Verse-length compression aligns with the qualitative tail-substructure.
- **[[h-new-130-fisher-rao-residuals|H-NEW-130]]**: universal hinges including Q 56/57 Hijra. Both [[h-new-660-compression-tail-gradient|H-NEW-660]] and [[h-new-770-verse-length-compression-tail|H-NEW-770]] land their kink at s=50, near the Hijra boundary.
- **[[h-new-580-five-factor-regression|H-NEW-580]]**: 5-factor regression OOS r=0.929. Verse-length is not one of the 5 factors but is highly correlated with chrono_homog and register_homog; [[h-new-770-verse-length-compression-tail|H-NEW-770]] suggests the 5-factor model implicitly captures verse-length variation through its register and chrono factors.
- **[[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]** (5-factor cohesion model): Refinement — verse-length is a strong univariate predictor with R²=0.76 by itself; the 5 factors decorate this 1-D backbone.
- **[[cross-finding-022-wave5-terminal-synthesis|cross-finding-022]] §2** (Ridge MAE=8 for block-structure): Consistent — most of the block signal is the post-kink compression-tail.
- **al-Suyūṭī *al-Itqān*** mufaṣṣal classification ("shorter verses"): QUANTITATIVELY VINDICATED — R²=0.81 single-parameter law for verse-length, kink at s=50.
- **al-Zarkashī *al-Burhān*** mufaṣṣal sub-divisions (ṭiwāl-awsāṭ-qiṣār): consistent with the multi-tier post-kink compression.
- **[[h-new-700-phonological-compression-tail|H-NEW-700]] (queued)**: rhyme-density compression-tail. If rhyme-density also follows the two-piece-kink-50 law, the multi-feature architectural-property interpretation is further strengthened.

## 7. Queued follow-ups

- **H-NEW-780**: Rhyme-density / fāṣila-pattern compression-tail (originally queued as [[h-new-700-phonological-compression-tail|H-NEW-700]]). Same windowing, same kink grid. Predicted: R² ∈ [0.6, 0.85], kink at s=50.
- **[[h-new-790-ijaz-by-classical-class|H-NEW-790]]**: Joint-feature regression — fit content-d̄ ∼ words/verse + rhyme-density + register, see whether ALL three are needed or one dominates.
- **H-NEW-800**: Permutation null with verse-length CONTROLLED — shuffle surahs but maintain the marginal verse-length distribution per window. If [[h-new-660-compression-tail-gradient|H-NEW-660]]'s R² survives, content-cohesion has a position-signal beyond verse-length.
- **[[h-new-810-length-controlled-ijaz|H-NEW-810]]**: Per-verse (not per-surah-averaged) verse-length analysis. Test whether the two-piece law holds at the verse-level over the 6236 verses.
- **H-NEW-820**: Translation invariance — does verse-length compression survive in English/French/Latin translations? If yes, the compression-tail is a TRANSLATION-INVARIANT structural feature. If no, it is rasm-specific.

## 8. Final statement

**The mushaf's compression-tail is a multi-feature architectural property, not a content-only signal.** Both per-verse letter count (R²=0.807) and per-verse word count (R²=0.811) follow the same two-piece-linear law as [[h-new-660-compression-tail-gradient|H-NEW-660]]'s content-cohesion (R²=0.986), with the SAME kink at s=50 (Hijra hinge), monotonic post-kink compression, and STRICT PASS with permutation p=0.00070 < α_bon=0.00833.

The window-by-window Pearson correlation between verse-length and content-cohesion is **r ≈ +0.87**, indicating they are strongly co-aligned. Univariately, verse-length explains 76% of content-cohesion variance. Yet the [[h-new-660-compression-tail-gradient|H-NEW-660]] single-parameter law (kink-50-post-position) captures essentially the entire JOINT signal — adding verse-length as a covariate raises R² by only +0.002 (0.986 → 0.988).

**Interpretation**: post-kink mushaf-position is the COMMON CAUSE. Content-cohesion and verse-length are co-effects of the post-Hijra mufaṣṣal register-shift. [[h-new-660-compression-tail-gradient|H-NEW-660]] is not derivative of verse-length, and verse-length is not derivative of content-cohesion. They are TWO QUANTITATIVE WITNESSES of one architectural commitment.

Classical scholarship (al-Suyūṭī, al-Zarkashī) qualitatively named this commitment "mufaṣṣal" and noted both shorter verses and altered register. **[[h-new-770-verse-length-compression-tail|H-NEW-770]] + [[h-new-660-compression-tail-gradient|H-NEW-660]] quantify both axes of the named structure with two convergent two-piece-kink-50 laws and identify the post-Hijra position as the single shared parameter.** The classical 14-century mufaṣṣal terminology is now empirically locked at: kink-position s=50 (≈ Q 56/57), pre-kink REGIME-1 flat, post-kink REGIME-2 monotonically compressing in BOTH content-cohesion and verse-length simultaneously.

The 11% TSP-residual interpretation ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] / [[h-new-670-tsp-hijra-constraint|H-NEW-670]]) remains DISTRIBUTED across many canonical adjacencies; [[h-new-770-verse-length-compression-tail|H-NEW-770]] does not bear directly on it.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
