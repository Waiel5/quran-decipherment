# H-NEW-173 journal — run 1

**Date**: 2026-04-17
**Seed**: 20260419
**Pre-reg SHA-256** (runtime-computed): see stderr of `scripts/h_new_173_residual_spectrum.py`

## What ran

Loaded the 113-long sequence `r_i = D[i, i+1]` from `findings/phase-b-hypotheses/csv/h-new-111.json` (Fisher-Rao mushaf D-matrix, upper-triangular form). Computed:
- `numpy.fft.rfft` power spectrum (57 bins; pre-committed scan range k=2..56 = 55 tests).
- Biased ACF lags 0..30; Bonferroni over lags 1..30 = 30 tests.
- 10 000 uniform-shuffle permutations for each test. Independent RNGs (SEED, SEED+2).
- MW-5 positive control: synthetic sin-with-period-11 + Gaussian noise, SEED+1.

## Results (summary)

| Test | Statistic | Value | p_bonf | Pass @α=0.025? |
|---|---|---|---|---|
| PRIMARY spectrum | min p_bonf over k=2..56 | 0.0110 at k=2 (T=56.5) | 0.0110 | YES |
| SECONDARY ACF | min p_bonf over lags 1..30 | 0.0030 at lag=1 (ρ=+0.862) | 0.0030 | YES |
| MW-5 positive control | top-k of synthetic sin11 | k=10 (exp. ≈10.27) | — | YES |

## Interpretation

- **One dominant spectral mode: k=2, T=56.5.** Single half-cycle over the whole mushaf ⇒ a monotone ramp, not a hidden rhythm.
- **ACF decays monotonically** from ρ(1)=0.862 to ρ(25)=0.214 without revival ⇒ smooth non-stationary series, not oscillator.
- **No short-period peaks** (k=11 T=10.3, k=7 T=16, k=19 T=6, k=14 T=8) reach Bonferroni significance. The classical numerology-of-letters rhythms (7, 11, 14, 19) are NOT expressed in the Fisher-Rao consecutive-distance sequence.
- Consistent with H-NEW-130: those 15 top residuals are local spikes on top of the k=2 ramp, coincident with structural seams.

## Operational notes

- Naive DFT was originally used, but replaced with numpy.fft.rfft for speed (10 000 perms × 113 pts). Final runtime < 1 min.
- Both primary and secondary tests' p_raw floor = 1/10001; i.e. zero permutations beat the observed statistic at k=2 and at lag=1. This means the true p values could be much smaller than the reported floor; 10 000 is adequate for Bonferroni α=0.025 / n∈{30,55} decisions but wouldn't discriminate finer structure.
- Pre-committed scan ranges were honored exactly; no post-hoc widening.

## Output artifacts

- `findings/phase-b-hypotheses/csv/h-new-173.json` — full residual sequence, power spectrum, ACF, permutation p-values.
- `findings/phase-b-hypotheses/h-new-173-residual-spectrum.md` — finding writeup.

## Next moves (suggested, NOT yet committed)

- **H-NEW-173b**: regress `r_i` on `log(wordcount_i) + log(wordcount_{i+1})` (or surah-length class) and spectrum the residual-of-residual. The k=2 ramp likely reflects the mushaf's descending-length architecture; removing it may or may not expose hidden short rhythms.
- Cross with cross-finding-017 (B6-B7 staircase) to check whether the ramp aligns with that step function.
