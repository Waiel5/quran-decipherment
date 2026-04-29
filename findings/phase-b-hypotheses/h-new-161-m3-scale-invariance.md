# [[h-new-161-m3-scale-invariance|H-NEW-161]] — M3 scale-invariance: NOT a simple fractal; has a crossover

**Finding ID**: [[h-new-161-m3-scale-invariance|h-new-161]]
**Date**: 2026-04-17
**Specialist**: specialist-a
**Parent**: [[h-new-48-poetic-meter|H-NEW-48]] + [[h-new-149-m3-verse-level-fractal|H-NEW-149]] + [[h-new-157-m3-triple-fractal|H-NEW-157]] (multi-scale M3)
**Verdict**: **NULL on strict scale-invariance (log-linear fractal); PASS on monotone-growth-with-scale regime k ≥ 5**

## Headline

**M3 distinctiveness does NOT follow a simple power-law decay with scale.** KS D values for Quran-vs-Bukhārī at windows k ∈ {1, 2, 3, 5, 7, 10, 15, 20, 30, 50}:

| k | D | p |
|---:|---:|---:|
| 1 | 0.173 | 10⁻⁷⁸ |
| 2 | 0.088 | 10⁻²⁰ |
| 3 | 0.083 | 10⁻¹⁸ |
| 5 | 0.154 | 10⁻⁶² |
| 7 | 0.191 | 10⁻⁹⁵ |
| 10 | 0.216 | 10⁻¹²² |
| 15 | 0.251 | 10⁻¹⁶³ |
| 20 | 0.273 | 10⁻¹⁹³ |
| 30 | 0.296 | 10⁻²²⁷ |
| 50 | 0.318 | 10⁻²⁶⁰ |

**D has a MINIMUM at k=2-3** (~0.08-0.09), then MONOTONICALLY INCREASES through k=50 (approaching chapter-level D=0.500 at n=114).

This is a CROSSOVER pattern, not a scale-invariant power-law.

## Log-linear fit

Attempting log(D) = a · log(k) + b across all 10 scales:
- Slope a = +0.306 (D GROWS with k)
- Intercept b = −2.31
- R² = 0.64 (moderate)

The fit captures the k ≥ 5 regime roughly but misses the k=1 → k=2-3 DIP. A two-regime model would fit better.

## Interpretation

### Why the crossover at k=2-3

At k=1 (single verse/chunk): Quran vs Bukhārī differ at the LOCAL prosodic level — Quran has shorter verses on average. D=0.17 captures this.

At k=2-3: aggregation AVERAGES OUT local variation within each corpus. The two distributions become more similar because the mean converges to within-corpus averages faster than between-corpus differences emerge. D DROPS to 0.08-0.09.

At k ≥ 5: aggregation reveals BETWEEN-corpus differences more systematically. Quran's compact-verse structure stays compact; Bukhārī's variable-chunk structure accumulates more variance. D GROWS.

At k → chapter size (~50-75): we approach [[h-new-149-m3-verse-level-fractal|H-NEW-149]]'s D=0.50 chapter-level result.

### M3 is meso-scale-enhanced, not scale-invariant

The finding is that M3's distinctiveness is STRONGEST at AGGREGATION SCALES, not at either the local (single verse) or the raw-pool (corpus) level. Specifically:

- Local verse (k=1): moderate D=0.17 — direct prosodic comparison but noisy.
- Mid-scale (k=5-20): D grows 0.15 → 0.27 as aggregation reveals genre-scale structure.
- Chapter (k=ch): D=0.50 — full genre separation.
- Corpus (pool): D ≈ 0.5 same as chapter (pooling loses structure).

**The Quran prosodic fingerprint is a MESO-SCALE phenomenon** — visible most clearly at aggregation scales between k=10 and chapter-size.

### This REFINES M3's status

[[h-new-157-m3-triple-fractal|H-NEW-157]] called M3 a "multi-scale fractal principle". [[h-new-161-m3-scale-invariance|H-NEW-161]] refines: M3 is NOT scale-invariant in the strict sense (no power-law decay). It is a PREFERRED-SCALE phenomenon with a crossover around k=2-3 where meso-scale aggregation begins to dominate local noise.

In the [[cross-finding-014-five-principle-unified-equation|cross-finding-014]] 5-principle model, M3 should be described as "meso-scale-prosodic-distinctiveness", not "fractal".

## Honest limits

1. **Only 10 scales tested**; finer granularity might reveal more structure.
2. **Bukhārī chunking by narration-markers** is noisy; Quran chunking by verse is clean. The asymmetry might inflate D at small k and bias the crossover.
3. **Large sample sizes inflate p-values**. The interesting observable is D (effect size), not p.
4. **Only one comparison corpus** (Bukhārī). A different corpus might show a different crossover.

## Connections

- **[[h-new-48-poetic-meter|H-NEW-48]] / cross-finding-007**: M3 at verse-level.
- **[[h-new-149-m3-verse-level-fractal|H-NEW-149]]**: M3 at chapter-level.
- **[[h-new-157-m3-triple-fractal|H-NEW-157]]**: M3 at triple-level (one data point; falls in the dip region).
- **[[cross-finding-014-five-principle-unified-equation|cross-finding-014]]**: M3 description should be "meso-scale" not "fractal".

## Verdict

**NULL on strict scale-invariance** (log-linear fit R²=0.64; crossover at k=2-3 invalidates single-exponent power-law).

**PASS on monotone-growth regime k ≥ 5** (D rises from 0.15 to 0.32 as k rises from 5 to 50; log-linear slope +0.31).

**Refined status**: M3 is a MESO-SCALE-enhanced prosodic-distinctiveness signature, not a scale-invariant fractal. The distinction is strongest at aggregation scales between k=10 and k=chapter-size.
