---
id: h-new-164
title: "H-NEW-164: Fourier spectrum of 114 verse-count integer sequence"
status: reject-null (descriptive; structural trend, not hidden period)
date: 2026-04-17
seed: 20260419
variant: no-tashkeel
prereg: h-new-164-fourier-verse-count-prereg.md
---

# [[h-new-164-fourier-verse-count|H-NEW-164]] — Fourier spectrum of the 114 verse-count integer sequence

## TL;DR

The canonical-order verse-count sequence x[n] (n=0..113) has a DFT power
spectrum overwhelmingly dominated by the k=1 mode (33.2 % of variance),
which is **significantly larger than any random permutation of the same
114 integers produces** (p < 1e-4 over 10,000 permutations; null 99th
percentile 0.139, observed 0.332). The cumulative-sum sequence shows the
same signature even more strongly (57.9 % at k=1, p < 1e-4).

**Interpretation caveat:** this is *not* a hidden-period discovery. The
k=1 dominance is the Fourier footprint of the well-known monotone
descending-length convention of mushaf ordering (big surahs at the
front, short surahs at the back). What the permutation null confirms is
that this descending trend is *much* stronger than random, i.e., mushaf
order is not a random permutation of the surah multiset. This is a
re-expression, in the frequency domain, of the Nöldeke/Flügel ordering
observation.

## Results — primary sequence (verse counts)

| rank | k  | P_norm  | period (114/k) |
|------|----|---------|----------------|
| 1    | 1  | 0.332   | 114            |
| 2    | 2  | 0.099   | 57             |
| 3    | 7  | 0.077   | 16.3           |
| 4    | 3  | 0.061   | 38             |
| 5    | 6  | 0.038   | 19             |

- Observed max P_norm = **0.332** at k=1.
- Null 95th percentile = 0.115; 99th percentile = 0.139; null max = 0.231.
- p = (1 + # perms ≥ 0.332) / 10001 = **9.999e-05** → reject null.

## Results — secondary sequence (cumulative sum)

| rank | k  | P_norm  |
|------|----|---------|
| 1    | 1  | 0.579   |
| 2    | 2  | 0.173   |
| 3    | 3  | 0.064   |
| 4    | 4  | 0.039   |
| 5    | 5  | 0.025   |

- Observed max P_norm = **0.579** at k=1.
- Null 99th percentile = 0.143; null max = 0.258.
- p = **9.999e-05** → reject null.

The cumsum shows textbook integration-of-trend behaviour: monotone
low-pass spectrum with 1/k-like fall-off. The permutation null would
show this for *any* monotone ordering of the same multiset, so the
statistical rejection is driven by the same underlying descending-length
convention as the primary.

## Honest verdict

- **Statistical verdict:** canonical mushaf order is not a random
  permutation of the surah-length multiset — a frequency-domain
  confirmation of the descending-length ordering principle. This is a
  **known** fact; H-164 is a null-check that our spectral pipeline
  registers it at the expected signal strength.

- **What we did NOT find:** no hidden non-trivial period (e.g. a peak
  at k=7, k=19, or similar) that would exceed the null once the
  monotone trend is accounted for. The k=7 peak (3rd largest in primary,
  P_norm=0.077) is below the null 95th percentile (0.115) — **not
  significant** after permutation test.

- **Scope:** exploratory / descriptive peak-hunting with a hard
  α=0.05 cap. We publish the significant k=1 result but flag it as
  *structural-trend-induced* and therefore theologically uninteresting
  unless a future variant (detrended, or block-means) reveals a
  residual periodic peak. Recommended follow-up: repeat after removing
  the best-fit monotone envelope (e.g. subtract spline-fit trend of
  ranked surah lengths, or analyze residuals from a length-rank power
  law).

## MW-5 check

Synthetic sinusoid length 114 with f0=7: P_norm[7] = 1.000, argmax_k=7.
Pipeline is correctly registering periodic signal.

## Files

- Script: `scripts/h_new_164_fourier_verse_count.py`
- JSON:   `findings/phase-b-hypotheses/csv/h-new-164.json`
- Pre-reg: `findings/phase-b-hypotheses/h-new-164-fourier-verse-count-prereg.md`
- Journal: `journal/h-new-164-run-1.md`
