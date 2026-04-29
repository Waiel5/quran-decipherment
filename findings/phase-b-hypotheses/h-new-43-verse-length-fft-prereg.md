---
id: H-NEW-43
title: Corpus-Wide Verse-Length Spectrum — does the 6,236-point verse-length series have non-baseline spectral peaks?
status: PRE-REGISTERED (not yet executed)
registered: 2026-04-15
spec_locked_at: 2026-04-15
bonferroni_family: 2026-04-15-Fresh-Wave-3
bonferroni_k: 3
alpha_bon: 0.0167
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
primary_corpus: quran-text/quran-no-tashkeel.json
---

# [[h-new-43-verse-length-fft|H-NEW-43]] — Corpus-Wide Verse-Length FFT

## Question

Existing finding (findings/phase-b-hypotheses/verse-length-sequences.md) examined per-surah spectra for palindrome detection but NOT the full-corpus 6,236-point verse-length signal's frequency-domain structure. This test asks:

**Does the verse-length time series, taken as a single 6,236-point signal concatenated surah-by-surah in canonical mushaf order, have non-trivial spectral peaks that matched-Arabic baselines do NOT produce?**

If yes: the canonical order encodes rhythmic structure observable at frequency-domain level (without needing per-surah analysis). If no: the mushaf verse-length series is spectrally flat / 1/f-noise-like, consistent with compositional-independence across surahs.

## Procedure

1. **Signal construction.** Concatenate verse-lengths in canonical mushaf order: `L = [L_1_1, L_1_2, ..., L_1_7, L_2_1, ..., L_114_6]`. Length N = 6,236.
2. **Pre-processing.** Subtract per-surah mean (removes surah-length step-function trend; surah-order confound collapses into low-frequency component which we DISCARD by analyzing only k > N/114 ≈ 55).
3. **Spectrum.** Compute periodogram |FFT(L)|². Retain k ∈ [55, N/2].
4. **Peak detection.** Find top-K peaks with K = 10. For each peak, estimate significance vs a red-noise (AR(1)) null: fit AR(1) to L, simulate 10,000 AR(1) surrogates matched to L's mean/variance/AR(1) coefficient, compute peak-amplitude distribution under null.
5. **Three baselines.** Repeat identical pipeline with Bukhārī, Jāḥiẓ, Muʿallaqāt verse/sentence-length sequences length-matched and cut to 6,236 points. These are NULL-MODEL-CONTROL baselines, not the primary null.
6. **Primary null test.** Is the maximum peak z-score in Quran significantly > max peak z-score in baseline distributions? **Bonferroni inner k = 10** (top-10 peaks) → α_cell = 0.0167 / 10 = 1.67 × 10⁻³.
7. **MW-5 POSITIVE CONTROL.** Construct a synthetic positive-control signal: 6,236 points with an injected sinusoid at frequency f₀ = 0.01 cycles/verse, amplitude = 0.2σ, embedded in red noise matched to Quran. This MUST be detected at α_cell. Otherwise the pipeline is broken.

## Specific frequency-of-interest pre-register

Three pre-specified "frequencies of interest" with prior justification:
- **f_fibonacci** — peak near 1/21 or 1/34 (Fibonacci-interval recurrence)
- **f_mushaf-bipartition** — peak near 1/57 (half the 114 surahs)
- **f_sevenths** — peak near 1/7, 1/14, 1/21 (classical seven-part manzil partition)

These are PRE-REGISTERED; any significant peak at these frequencies is a directed hit; any other peak is an EXPLORATORY hit. Bonferroni across 3 directed + 10 undirected = 13 tests → α_inner = 0.0167 / 13 = 1.28 × 10⁻³.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| ≥1 directed frequency hit at α_inner | DIRECTED-PASS — specific pre-predicted rhythm confirmed |
| ≥3 undirected peaks at α_inner AND above baseline max | EXPLORATORY-PASS (tier-2) |
| Positive-control sinusoid not detected | NULL-BROKEN |
| 0 peaks at α_inner | NULL — verse-length signal is spectrally featureless beyond AR(1) |

## Garden-of-forking-paths log

- Choice to subtract per-surah mean: LOCKED here; the alternative (global mean subtraction) is a separate test
- Choice of canonical mushaf order (vs revelation-chronology order): both will be computed but only mushaf is PRIMARY; chronology-order is separate test H-NEW-43.1
- AR(1) vs AR(2) null: AR(1) LOCKED (parsimony; AR(2) is separate test)
- Top-K undirected peaks K=10 LOCKED
- Specific-frequency set (Fibonacci, 1/57, 1/7) LOCKED before any spectral plot viewed

## Mechanism interpretation

- DIRECTED-PASS at 1/7 → supports classical manzil-structure being rhythmically (not just topically) encoded
- DIRECTED-PASS at 1/57 → supports mushaf-bipartite structure
- DIRECTED-PASS at Fibonacci → rare, theologically striking, requires follow-up at word-level
- EXPLORATORY-PASS → rhythmic structure exists but doesn't match any pre-posited classical division
- NULL → verse-length is spectrally featureless; structural coherence lives at other axes (semantic, rhyme) not rhythmic

## Prior art

- Sayoud (2020) computed word-count surah-level statistics, no spectral analysis at corpus level
- Miller (2019) *Quranic Arithmology* discusses 7-based numerology qualitatively, no FFT
- No published paper computes the full 6,236-point verse-length periodogram against a matched-Arabic AR(1) null

## Integrity commitment

Publish periodogram + null quantiles + positive-control output alongside PASS or NULL verdict.

---

## AMENDMENTS (post-audit-032, 2026-04-15, pre-execution, tightening-only)

**Amendment 43-A (inner-k denominator lock).** Inner Bonferroni is locked at **k = 13** (3 pre-specified directed frequencies + top-10 undirected peaks), α_inner = 0.0167 / 13 = **1.28 × 10⁻³**. This supersedes the k=10 / α_cell = 1.67×10⁻³ language in §Procedure step 6, which was a drafting error. All peak-significance tests (directed or exploratory) use α_cell = 1.28 × 10⁻³. Tightening only; self-verifying per 2026-04-14 Bonferroni-asymmetry standard.

**Amendment 43-B (AR(1) goodness-of-fit threshold).** Pre-commit the AR(1) fit method as OLS (Yule-Walker is mathematically equivalent for stationary series and acceptable). Residuals MUST pass Ljung-Box test at p > 0.05 at lag 10. If Ljung-Box fails, the AR(1) null is disqualified and the verdict is NULL-BROKEN. No post-hoc switch to AR(2). Pre-committed before execution.
