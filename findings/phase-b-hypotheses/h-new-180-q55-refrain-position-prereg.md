# [[h-new-180-q55-refrain-position-result|H-NEW-180]] — Q 55 al-Raḥmān refrain-position mathematical structure (PRE-REG)

**Seed:** 20260419
**Bonferroni k:** 2 (uniformity-KS + FFT peak-vs-null)
**Date registered:** 2026-04-17

## Background
Q 55 has 78 verses; its signature refrain — "فَبِأَىِّ ءالاءِ رَبِّكُما تُكَذِّبانِ" ("So which of the favours of your Lord will you two deny?") — recurs throughout. [[h-new-178-alpha-beta-manifold|H-NEW-178]] found Q 55 the extreme outlier in (α,β) residual space (−0.285), attributable to refrain-flattened rank-frequency. [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] flagged it anti-geodesic. This test probes whether the refrain-position sequence itself carries a mathematical signature (uniform pillar vs accelerating crescendo vs other periodic structure).

## Data
- `quran-text/quran-min-tashkeel.json`, sura index 54 (1-indexed Q 55).
- Refrain match string (tashkeel-stripped): `فبأي ءالاء ربكما تكذبان` (also tolerant match via leading regex `^\s*ف?ب?ـ?أ?ي.*تكذبان`).
- Binary presence vector **r** of length N=78.

## Primary statistics
1. **Gap distribution.** Compute deltas `Δ_i = p_{i+1} − p_i` for refrain positions `p_1..p_K`.
   - KS-test Δ vs uniform-spacing expectation (spacing = N/K).
   - Report mean, sd, min, max, monotone-trend (Spearman rho of Δ_i vs i).
2. **Fourier.** Real FFT of centered binary vector r − mean(r), length 78. Identify dominant frequency k*, report peak power P*, phase.
3. **FFT null.** 10 000 random binary permutations of r (fixed K); p = frac(P_null ≥ P*).
4. **Monotonic-trend null.** Sign-flip permutation of Δ indices to bootstrap |rho| null.

## Decision rule
- **CONFIRM periodic**: FFT p < 0.025 AND Δ sd/mean < 0.15.
- **CONFIRM accelerating**: Spearman rho |ρ| > 0.5 with p < 0.025, otherwise UNIFORM or OTHER.
- **NULL**: neither.
- Bonferroni α = 0.05 / 2 = 0.025 per test.

## Synthetic control (MW-5)
Inject refrain every 3rd verse in a 78-long binary, verify FFT recovers k=26 (period 3).

## Garden-of-forking paths
- Refrain detection: stripped-tashkeel exact substring `فبأي ءالاء` AND ends with `تكذبان`.
- Only verses where the verse IS the refrain (not containing other words).
- FFT uses numpy rfft; power = |X[k]|^2; k=0 excluded.
- Monotone test: Spearman over ordered Δ_i.
- No post-hoc changes once run.

## Files
- `findings/phase-b-hypotheses/h-new-180-q55-refrain-position-result.md`
- `scratch/h-new-180/run.py`, `gaps.csv`, `fft.csv`
