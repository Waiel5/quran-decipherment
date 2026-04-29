# [[h-new-173-residual-spectrum|H-NEW-173]] — Spectral analysis of M1 residual sequence (Fisher-Rao consecutive-pair distances)

**Pre-registered**: 2026-04-17
**Seed**: 20260419
**Status**: PRE-COMMITTED before results inspected

## Motivation

- [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]: `L_mushaf = 85.76` vs optimal (2-opt) `L_2opt = 77.47` → ~11% "structured residual" above the geodesic optimum.
- [[h-new-130-fisher-rao-residuals|H-NEW-130]]: the 15/15 largest consecutive-pair residuals all hit pre-committed structural boundaries (muqaṭṭaʿāt, length tiers, period shifts).
- [[h-new-173-residual-spectrum|H-NEW-173]] (this): treat the FULL 113-long sequence `r_i = D[i, i+1]` for i in 1..113 as a time-series indexed by mushaf position. Does it have a hidden rhythm (periodicity, strong lag-autocorrelation)?

## Data source

- Input: `findings/phase-b-hypotheses/csv/h-new-111.json` → `D_matrix_upper_triangular` (locked 2026-04-09; SHA inherited).
- Sequence: `r_i = D[i, i+1]` for i=1..113 (length 113).

## Hypotheses (Bonferroni-2, α_fam = 0.05, α_test = 0.025)

**PRIMARY (H1)**: The FFT power spectrum of `r` has at least one discrete-frequency bin whose power exceeds the 97.5th percentile of power at that bin under the null (random permutation of `r`, 10000 draws), for at least ONE k in 2..56 (Nyquist half-range) — Bonferroni-corrected across all k (family-wise error rate within test). The test is significant if any bin's empirical p-value, after Bonferroni correction over k-bins within the FFT, passes α_test = 0.025.

**SECONDARY (H2)**: At least one lag ℓ ∈ {1,..,30} has autocorrelation `|ρ(ℓ)|` exceeding the 97.5th percentile of permutation null, Bonferroni-corrected over the 30 lags, at α_test = 0.025.

Bonferroni-2 across {H1, H2}. Each test is internally Bonferroni-corrected over its scan grid. Combined α_fam = 0.05; α_per_test = 0.025.

## Pre-committed rule tuple

- Normalization: raw r (no detrending, no centering — we test for structure INCLUDING mean).
- FFT: numpy.fft.rfft on r (length 113). Power = |FFT|^2. We scan k = 2..56 (omit DC & k=1 to avoid trivial Nyquist edge; this is the pre-committed scan range).
- Autocorrelation: biased ACF `ρ(ℓ) = sum_{i=1..N-ℓ} (r_i − r̄)(r_{i+ℓ} − r̄) / sum_{i=1..N} (r_i − r̄)^2`.
- Null: shuffle `r` uniformly at random, recompute stat. 10000 perms, seed 20260419.
- Bonferroni within H1: over 55 k-bins. Within H2: over 30 lags.

## MW (measure-what) controls

- **MW-1**: report descriptive stats (mean, var, min, max) of r.
- **MW-5 (positive control)**: synthetic `r_synthetic_i = 1 + 0.2*sin(2π*i/11) + ε_i` with ε~N(0,0.05) should show a spectral peak at k≈113/11≈10.3 (nearest bin k=10). Seed for noise: 20260419+1. Confirms pipeline can detect periodicity when present.
- **MW-robust**: also report the single-bin raw p-value (uncorrected) for the top-3 peaks to diagnose weak-but-pre-specified signal.

## Pre-committed output paths

- Script: `scripts/h_new_173_residual_spectrum.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-173.json`
- Finding: `findings/phase-b-hypotheses/h-new-173-residual-spectrum.md`
- Journal: `journal/h-new-173-run-1.md`

## Interpretation grid (pre-committed)

- PRIMARY passes: periodicity exists → investigate period-length for classical/architectural correlates (7, 10, 11, 14, 19, 29 would each have distinct plausible readings).
- SECONDARY passes alone: local dependence without pure sinusoid → M1 residual is Markovian / block-structured.
- Both fail: residual is effectively independent noise around the 2-opt optimum (structural boundaries without rhythm).
- MW-5 MUST recover period=11 peak; else pipeline invalid.
