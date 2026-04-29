---
id: h-new-164-fourier-verse-count
title: "H-NEW-164: Fourier spectrum of the 114 verse-count integer sequence"
date_prereg: 2026-04-17
seed: 20260419
bonferroni_k: 1
alpha_bon: 0.05
direction: descriptive-peak-hunting
alpha_cap: 0.05
status: pre-registered
---

# [[h-new-164-fourier-verse-count|H-NEW-164]] — Pre-registration

## Hypothesis

The 114 verse-count integer sequence (in canonical mushaf order) has a
power-spectrum peak (from DFT) that exceeds what would be produced by a
random permutation of the same 114 integers.

This is an **exploratory, descriptive peak-hunting** test. We do NOT
claim any particular frequency *a priori*. We simply ask: is the maximum
power in the spectrum of the canonical-order sequence unusually large
compared to random permutations of the same multiset?

## Rationale

The canonical mushaf order shows a rough monotone-decreasing verse count
with conspicuous exceptions (Al-Fatiha = 7 at position 1; short surahs at
end). Any structural periodicity — e.g. a compositional meter at the
level of surah-boundaries — would manifest as a frequency peak in the
sequence's DFT. This is agnostic to *which* frequency would carry signal.

## Method

1. Load the corpus via `from tools.loader import load_quran` (variant
   `no-tashkeel`). The verse count per surah is taken as
   `s.total_verses` for each of the 114 surahs.
2. Form the 1-D array `x` of length 114. Compute
   `F = numpy.fft.fft(x - mean(x))` (mean-detrended so F[0]=0).
3. Power spectrum `P[k] = |F[k]|^2` for k = 1..57 (Nyquist).
4. Normalize by total variance: `P_norm[k] = P[k] / sum(P[1..57])`.
5. Top-5 peaks identified by sorting `P_norm[k]` descending.
6. Null: 10,000 random permutations of the same 114 integers (seeded
   RNG). For each, compute the maximum `P_norm[k]` over k=1..57.
7. p-value: `p = (# perms with max_peak >= observed_max_peak + 1) /
   (N_perm + 1)`.
8. Compare observed `max_peak` to the null 95th percentile.

## Decision rule

- `p < alpha_bon (= 0.05)` with k=1 Bonferroni → reject null;
  declare a significant peak (descriptive only, post-hoc on k).
- `p >= 0.05` → publish NULL with equal prominence.

## Minimal-worked-example MW-5

A synthetic sinusoidal sequence `x_syn[n] = sin(2*pi*n*f0/114)` with
`f0 = 7` and length 114 must produce a clear peak at k=7 with
`P_norm[7] > 0.5`, else the pipeline is broken.

## Secondary analysis

Same pipeline applied to the **cumulative sum** sequence
`cum[i] = sum(x[0:i+1])` for i=0..113. Because cumulative sums induce
a 1/k low-frequency drift in the spectrum (integration in time =
1/(jω) in frequency), we expect trivial low-frequency dominance and
control for this with the permutation null (same trivial trend since
same multiset → same cumulative-sum family).

## Pre-registered YAML

```yaml
id: h-new-164
bonferroni_k: 1
alpha_bon: 0.05
direction: descriptive-peak-hunting
alpha_cap: 0.05
seed: 20260419
n_perm: 10000
sequence_primary: verse_counts
sequence_secondary: cumsum_verse_counts
variant: no-tashkeel
mw_5: "synthetic sinusoid length 114 must produce P_norm[f0] > 0.5"
```

## Files

- Script: `scripts/h_new_164_fourier_verse_count.py`
- JSON:   `findings/phase-b-hypotheses/csv/h-new-164.json`
- Finding: `findings/phase-b-hypotheses/h-new-164-fourier-verse-count.md`
- Journal: `journal/h-new-164-run-1.md`
