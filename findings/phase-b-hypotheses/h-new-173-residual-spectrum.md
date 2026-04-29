# [[h-new-173-residual-spectrum|H-NEW-173]] — Spectral analysis of M1 residual sequence

**Date**: 2026-04-17
**Pre-reg**: `[[h-new-173-residual-spectrum|h-new-173]]-residual-spectrum-prereg.md` (SHA-256 hashed at runtime)
**Seed**: 20260419
**Status**: PRIMARY + SECONDARY pass Bonferroni-2. MW-5 positive control passes.

## Residual sequence

`r_i = D[i, i+1]` from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] Fisher-Rao D-matrix. Length N=113.
- mean = 0.7589
- variance = 0.0580
- min = 0.2256 (shortest consecutive-pair distance in M1)
- max = 1.1776

## PRIMARY (spectrum)

Bonferroni-corrected over 55 k-bins (k=2..56), 10 000 permutations.

- Minimum Bonferroni-adjusted p = **0.0110 at k=2** (period T = 56.5) ⇒ PASS at α=0.025.
- Top-3 peaks by raw power:
  - **k=2, T=56.5, power=53.54, p_bonf=0.011** ← dominant, significant
  - k=5, T=22.6, power=14.13, p_bonf=1.0 (NS after correction)
  - k=3, T=37.7, power=13.46, p_bonf=1.0
- Next tier: k=11 (T=10.3, power=7.5), k=7 (T=16.1, power=6.2), k=19 (T=5.95, power=4.2). None significant after Bonferroni.

Interpretation: the residual spectrum is dominated by a single ultra-low-frequency component (one full half-cycle across the whole mushaf). There is no significant short-period architectural rhythm (7, 11, 14, 19 do NOT emerge).

## SECONDARY (autocorrelation)

Bonferroni-corrected over 30 lags. All lags 1..25 have |ρ| significant at the per-perm floor (p_bonf = 0.003). ACF is **monotonically decaying**:
- ρ(1) = +0.862
- ρ(7) = +0.667
- ρ(14) = +0.499
- ρ(25) = +0.214
- ρ(30) = +0.103 (crosses noise floor around lag 26)

No bump, no trough, no periodic revival. Classic long-memory / trend-plus-noise profile, not an oscillator.

## MW-5 positive control

Synthetic `1 + 0.2·sin(2πi/11) + N(0, 0.05)` recovers peak at k=10 (top), k=11 (2nd). Pipeline can detect period=11 when planted. PASS.

## Verdict

**The 11% "structured residual" from [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] is not an oscillation but a monotone drift** along the mushaf axis. Consecutive Fisher-Rao distances are large early (surahs 1–30, muqaṭṭaʿāt-heavy long Medinan bloc) and shrink toward the end (short Meccan mufaṣṣal). The signature is one of smooth non-stationarity, not hidden architectural rhythm.

[[h-new-130-fisher-rao-residuals|H-NEW-130]]'s boundary-concentration result is entirely compatible with this: boundaries sit at specific one-off transitions (length tiers, period changes), not at periodic beats. Reinterpretation: M1's residual is a **ramp**, and the top-15 spikes from [[h-new-130-fisher-rao-residuals|H-NEW-130]] are local deviations on top of that ramp at known structural seams.

## Caveats / next moves

- Detrending with the k=2 mode and re-running spectrum could expose weaker hidden periods; not pre-committed here.
- The monotone decay is partly a consequence of the length-profile: the mushaf is roughly length-sorted. Fisher-Rao residuals inherit that. A length-residualised variant (regress `r` on length of `S_i + S_{i+1}`, then spectrum the residual of the residual) is the logical H-NEW-173b.
- The NON-detection of period ≈ 7, 11, 14, 19 is itself publishable: classical ḥarf-ʿadad numerology would predict such rhythms; we see none at FWER 0.025 after single-bin Bonferroni over k=2..56.

## Files

- Script: `scripts/h_new_173_residual_spectrum.py`
- Data: `findings/phase-b-hypotheses/csv/h-new-173.json`
- Pre-reg: `findings/phase-b-hypotheses/h-new-173-residual-spectrum-prereg.md`
- Journal: `journal/h-new-173-run-1.md`
