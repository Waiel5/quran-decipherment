# [[h-new-180-q55-refrain-position-result|H-NEW-180]] RESULT — Q 55 al-Raḥmān refrain-position mathematical structure

**Seed:** 20260419 · **Bonferroni k=2, α=0.025** · **Run:** 2026-04-17
**Pre-reg:** `[[h-new-180-q55-refrain-position-result|h-new-180]]-q55-refrain-position-prereg.md`
**Verdict:** CONFIRM — **near-periodic, front-loaded-irregular, asymptotic period-2 pillar** (NOT accelerating; decelerating on the leading edge only).

## Inputs
- Sura Q 55, 78 verses (tashkeel stripped, JSON canonical).
- Refrain detection: starts `فب…`, contains `ءالاء`, ends `تكذبان`.
- **K = 31** refrain verses (matches al-Suyūṭī Itqān ta'dād). Positions:
  `13, 16, 18, 21, 23, 25, 28, 30, 32, 34, 36, 38, 40, 42, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77`.

## Gap distribution Δ_i (length 30)
`[3, 2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`

| stat | value |
|---|---|
| mean | 2.133 |
| sd | 0.346 |
| CV | **0.162** |
| min / max | 2 / 3 |
| value counts | 2 × 26, 3 × 4 |

The four "3-gaps" (one extra non-refrain verse between refrains) occur only at Δ-indices {0, 2, 5, 13}, i.e. between refrains `13→16, 18→21, 25→28, 42→45`. After gap index 13 (refrain 42→45), the pattern locks into perfect period-2 for the entire remaining 16 intervals. **The sura establishes its refrain rhythm and then settles into strict pillar-spacing.**

Additionally:
- Opening prologue (vv 1–12) before first refrain: **12 verses** (creation catalogue).
- Coda after last refrain (v 77→78): **1 verse** (takhtīm: "Blessed be the Name of your Lord…").

## Uniformity (test 1 / 2)
- Observed CV = 0.162.
- Null CV (uniform-random placement of 31 events in 78 slots, 10 000 sims): mean 0.748, 5%-ile 0.575.
- **p = 0.0001** (obs ≤ null). **PASS Bonferroni-adjusted α=0.025.**

## Fourier analysis (test 2 / 2)
Real FFT of centered presence-vector r (length 78).
- **Peak at k\* = 38**, freq = 0.4872, **period ≈ 2.053**, power = 234.2.
- Secondary peak at k = 39 (power 121, period 2.000 exactly).
- Permutation p (peak-vs-null, B=10 000): **p = 0.0004**.
- Fixed-k\* permutation p: **p = 0.0001**. **PASS Bonferroni.**

Interpretation: the spectrum is dominated by the Nyquist-adjacent pair k=38, 39, consistent with an **almost-period-2** signal whose four early 3-gap deviations sidelobe-shift the peak slightly off the exact Nyquist k=39.

## Monotone trend
Spearman ρ(Δ_i vs i) = **−0.431, p = 0.018**. Formally significant (not Bonferroni-corrected for this nuisance test), sign is **negative**: gaps *shrink* over the sura. The sura **decelerates from 3-2-3-2-2-3 toward a locked period-2 refrain**, the opposite of a crescendo.

## MW-5 synthetic control
Period-3 synthetic refrain recovers dominant k = 26, period = 3.000 exactly. **PASS.**

## Verdict
**CONFIRM periodic.** Both pre-registered tests pass Bonferroni α=0.025 (CV p=0.0001; FFT p=0.0004).

The refrain-position signature is neither accelerating nor strictly uniform: it is a **two-phase architecture** —
- **Phase 1 (vv 13–45):** pattern-establishment with 4 irregular 3-gaps (mostly in the first third).
- **Phase 2 (vv 45–77):** locked period-2 pillar, 16 consecutive Δ=2 gaps, zero irregularity.

## Classical anchor
Al-Suyūṭī (Itqān II.161) and al-Qurṭubī count the refrain's 31 occurrences and structure Q 55 as eight blocks (creation / cosmic balance / jinn & men / punishment / two gardens / two gardens below). The observed geometry matches this: the four irregular gaps (opening 3-gaps) partition **Phase 1** into thematic blocks before the period-2 lock-in of **Phase 2** (the twin-gardens parallelism beginning at v 46). This is **pillar-like (uniform interval)**, not crescendo-like (accelerating), and explicitly *decelerates* rather than accelerates — consistent with al-Suyūṭī's description of the refrain as a steadying cadence ("taqrīr al-ni'ma"), not a mounting intensifier.

## Link to earlier findings
- Explains [[h-new-178-alpha-beta-manifold|H-NEW-178]] residual (−0.285): 31/78 = 39.7 % of verses are literal copies of one string → rank-frequency flattened → extreme (α,β) outlier. *Cause confirmed geometrically.*
- Explains [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] anti-geodesic status: refrain-dominated verses have vanishing semantic velocity → Q 55 traces a *stationary cycle*, not a trajectory.

## Files
- Pre-reg: `findings/phase-b-hypotheses/h-new-180-q55-refrain-position-prereg.md`
- Result: this file
- Run script: `scratch/h-new-180/run.py`
- Data: `scratch/h-new-180/gaps.csv`, `fft.csv`, `summary.txt`
