# [[h-new-166-multi-scale-hurst|H-NEW-166]] — Multi-scale Hurst exponent cascade (pre-registration)

**Finding ID**: [[h-new-166-multi-scale-hurst|h-new-166]]-prereg
**Date**: 2026-04-17
**Agent**: autonomous-test-H-NEW-166
**Parent**: H-NEW-35 / fractal-self-similarity.md (H=0.88 single-scale Hurst on 6236 verse-lengths)
**Seed**: 20260419 (numpy default_rng)
**Status**: PRE-REGISTERED BEFORE DATA ANALYSIS

## Background

H-NEW-35 (canonical: `findings/phase-b-hypotheses/fractal-self-similarity.md`, H-F1)
reported Hurst (R/S) = 0.884 and DFA-α = 0.921 on the Quran's 6236-verse
verse-length sequence, vs matched Arabic prose max H ≈ 0.46 (Mu'allaqat
poetry, otherwise ≤ 0.39). That analysis returned a *single-scale* Hurst
slope. If the Quran's long-range memory is **mono-fractal** H(n) is
essentially constant across scale n; if **multi-fractal**, H(n) varies
(and MF-DFA H(q) has width Δ > 0.05).

## Rules tuple

- Orthography: `no-tashkeel`
- Word definition: whitespace-split orthographic tokens (real words)
- Verse length metric: **words per verse** (not letters — per the task
  spec). For robustness, letter-count is run as a secondary.
- Verse numbering: hafs-kufan (6236 verses)
- Basmala policy: basmala counted only in surah 1 (follows H-NEW-35 convention)
- Bukhārī segmentation: narrator-formula cuts (حدثنا / أخبرنا / قال / عن
  / بَاب) per [[h-new-149-m3-verse-level-fractal|H-NEW-149]] M3 convention. Chunk = tokens between consecutive
  cuts. Use the same 6236 chunks used in H-NEW-35 stringent baseline if
  available; else re-derive.
- RNG seed: 20260419

## Method

### 1. DFA multi-scale

Let `L[i]` be word-count of verse `i`, i=1..N, N=6236.

Standard DFA-1 (order-1 polynomial detrending):
1. Integrate: `Y[k] = Σ_{i≤k}(L[i] − mean(L))`.
2. For each window size `n ∈ S`, partition Y into
   `⌊N/n⌋` non-overlapping segments. Fit order-1 polynomial per
   segment. Compute residual RMS per segment, average (squared) across
   segments, take sqrt → F(n).
3. Report log–log slope of F(n) vs n over the requested scale set
   **S = {10, 20, 50, 100, 200, 500, 1000}** (task-specified).

Additional sliding-slope test: compute scale-resolved Hurst by fitting
slope of `log F(n)` within a *rolling window* of 3 consecutive scales
in S. If rolling-slope variation exceeds 0.05 across S, treat as
evidence of scale-dependent H (primary test).

### 2. MF-DFA (multifractal DFA)

For q ∈ Q = {−3, −2, −1, 0, 1, 2, 3}:

`F_q(n) = ( (1/N_s) Σ_ν [F²(ν,n)]^(q/2) )^(1/q)` for q≠0
`F_0(n) = exp( (1/(2 N_s)) Σ_ν ln F²(ν,n) )`

Scaling: `F_q(n) ~ n^h(q)`. Fit log-log slope per q.

**Primary statistic**: `Δh = max(h(q)) − min(h(q))` over Q.
Pre-registered threshold: Δh > 0.05 ⇒ multifractal; Δh ≤ 0.05 ⇒ mono-fractal.

### 3. Bukhārī comparison

Use [[h-new-149-m3-verse-level-fractal|H-NEW-149]]'s 114 longest bab-segments → chunk each by narrator-formula
tokens, concatenate to produce a word-per-chunk sequence matched to
length 6236 (truncate or pad-ignore to match). Run identical DFA + MF-DFA
pipeline. Report h(q) table and Δh side-by-side.

### 4. Bonferroni plan (Bonferroni-2)

**Primary**: Is Quran's scale-resolved H constant across scales (rolling
window slope range < 0.05)?
**Secondary**: Is MF-DFA Δh > 0.05 (multifractal)?

Family k = 2. Corrected α = 0.025 for each leg.

Both tests use bootstrap null: 1000 bootstrap resamples (with
replacement) of the verse-length series (paired-block bootstrap, block
size 20) to compute 95% CI on slopes. A test *passes* if the point
estimate lies outside the null CI at corrected α.

### 5. MW-5 Monte-Carlo calibration

Generate 200 fractional Brownian motion (fBm) sequences with H=0.88,
N=6236, using Davies-Harte exact synthesis. For each, compute h(q) for
q ∈ Q and report mean ± SD of Δh. A genuine monofractal should give
Δh distribution centered near 0 with SD ~ 0.01–0.03. If our Quran Δh
lies *inside* the fBm null distribution → mono-fractal confirmed (at
H=0.88). If outside → multifractal.

### Pre-specified interpretive decision table

| Quran Δh | Quran rolling-H range | Verdict |
|---|---|---|
| ≤ 0.05 | ≤ 0.05 | **MONO-FRACTAL** (confirms H-NEW-35 as complete description) |
| > 0.05 | ≤ 0.05 | **WEAK multifractal** (MF structure without scale-dependent mean H) |
| ≤ 0.05 | > 0.05 | **Scale-crossover mono-fractal** (Hurst regime shift but no q-multifractality) |
| > 0.05 | > 0.05 | **FULL MULTIFRACTAL** (H varies by both q and n) |

## Garden-of-forking-paths log (pre-data-touch)

Choices fixed **before** analysis:
- Scale set S = {10, 20, 50, 100, 200, 500, 1000} — per task spec, not
  optimized.
- q set Q = {−3,−2,−1,0,1,2,3} — per task spec.
- DFA polynomial order = 1 (DFA-1). Higher orders not explored.
- Rolling window for scale-resolved H = 3 consecutive scales.
- Metric: **words per verse** (primary); letters per verse secondary.
- Bonferroni-2 family (primary scale-invariance vs secondary Δh width),
  not Bonferroni-1; the two tests address conceptually different
  manifestations of multifractality.
- MW-5 uses H=0.88 (reported value from H-NEW-35, R/S). Alternative
  would be DFA-α=0.92; both are pre-declared acceptable, but we report
  H=0.88 as primary because the task spec sets this anchor.
- Bukhārī alignment: truncate-to-6236 (ignore tail) rather than
  loop/pad; [[h-new-149-m3-verse-level-fractal|H-NEW-149]] already certifies the 114 longest bab-segments
  provide ≥ 6236 chunks.
- Null: block-bootstrap (block = 20) for CI; surrogate fBm for
  multifractal calibration.

## Artifacts (planned)

- `scratch/h-new-166/run.py` — analysis script
- `scratch/h-new-166/h_new_166.json` — numerical outputs
- `scratch/h-new-166/dfa-quran.csv`, `dfa-bukhari.csv` — F(n) tables
- `scratch/h-new-166/mfdfa-quran.csv`, `mfdfa-bukhari.csv` — h(q) tables
- `scratch/h-new-166/mw5-fbm-calibration.json` — fBm null distribution
- `findings/phase-b-hypotheses/h-new-166-multi-scale-hurst.md` — report

## Checklist

- [x] Rules tuple pre-registered
- [x] Scale set, q set, metric, seed, block size all pre-declared
- [x] Bonferroni family k=2 pre-declared
- [x] MW-5 calibration pre-declared at H=0.88
- [x] Interpretive decision table pre-declared
- [ ] DFA implementation unit-tested against known fBm H before Quran run
- [ ] Bukhārī baseline alignment executed
- [ ] Null / bootstrap / surrogate fBm executed
- [ ] Result published with honest verdict
