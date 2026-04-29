# H-NEW-690 — Run 1 Journal

**Date:** 2026-04-28
**Hypothesis:** Compression-tail-alone (H-NEW-660 law: two-piece-kink-50, R² ≥ 0.95, β ∈ [−0.015, −0.010]) generates orderings whose FR-TSP-residual matches canonical mushaf's ~11%.
**Pre-reg SHA:** `21d56df2bcf132dd219846ce7152df2e089e876a85dc5b089e8a30257efadfda`
**Seed:** 20260437
**Verdict:** **NULL** (compression-tail is necessary but NOT sufficient).

## Pipeline

1. Locked pre-reg at `findings/phase-b-hypotheses/h-new-690-causal-generative-prereg.md`. SHA computed and embedded in script.
2. Loaded FR distance matrix from `findings/phase-b-hypotheses/csv/h-new-111.json` (D_matrix_upper_triangular, 6441 pairs, 114 surahs).
3. Locked anchors from cross-finding-011 / h-new-111: L_canonical=85.759656, L_2opt=77.466858, canonical residual=10.705%.
4. Sanity-evaluated canonical → R²=0.9860, β=−0.01237, L=85.7597. Matches H-NEW-660 fit exactly. Constraint-OK.
5. Ran MH chain: 10000 steps, 1000 burn-in, sample every 100 steps. T=1.0 on FR-tour-length.
6. Warm-up failed: greedy descent from random permutation could not reach feasibility within 5000 attempts (start R²=0.090, start cd=8.61). Pre-registered fallback engaged: chain started from canonical.
7. Chain stats: 10000 proposals, 4697 accepted, 5281 (52.81%) constraint-feasible. 90 samples collected (sampler indexed first sample at step 1100; minor bookkeeping deviation from pre-reg-stated "100 samples", documented in §5 of findings).
8. Computed residuals, percentiles, histogram, verdict.

## Result

| Metric | Value |
|---|---|
| n_samples | 90 |
| Median residual | 24.95% |
| P25–P75 | 23.75% – 25.84% |
| Min / Max | 21.76% / 28.45% |
| Canonical residual | 10.70% |
| Canonical's percentile in ensemble | 0.0% (below the entire ensemble) |
| % at residual ≤ 11.5% (STRONG threshold) | 0/90 = 0.0% |
| % at residual ≤ 12.0% (DIRECTIONAL threshold) | 0/90 = 0.0% |
| % at residual ≤ 13.0% (NULL threshold) | 0/90 = 0.0% |

NULL pre-registered (< 10% at ≤ 13%) is met by a wide margin (0%).

## Robustness check (post-run, exploratory)

3 additional seeds (99991, 4242, 12345) at 5000 steps each, all starting from canonical:

| Seed | Feasible/5000 | Median residual | Min | Max |
|---|---|---|---|---|
| 99991 | 2666 (53%) | 25.40% | 20.99% | 28.90% |
| 4242 | 2774 (55%) | 25.20% | 20.89% | 28.01% |
| 12345 | 2632 (53%) | 24.11% | 19.80% | 28.40% |

All four chains (including main run) converge to median residuals 24-26% with mins ~20-22%. **No constrained ordering at any seed reached residual ≤ 13%.** NULL verdict is robust.

## Trajectory diagnostic (start at canonical)

| Step | L | Residual | R² |
|---|---|---|---|
| 0 | 85.76 | 10.70% | 0.9860 |
| 10 | 87.02 | 12.34% | 0.9830 |
| 50 | 90.66 | 17.03% | 0.9534 |
| 100 | 91.63 | 18.28% | 0.9676 |
| 500 | 96.02 | 23.95% | 0.9567 |
| 5000 | 95.97 | 23.89% | 0.9549 |

Chain escapes canonical's basin in <50 steps; reaches typical-set (~24-25%) within ~500 steps; remains stable for the rest of the run.

## Key interpretation

Compression-tail-respecting subset of S₁₁₄ has substantial volume (~53% of swap proposals from inside it stay inside it). Within that subset, typical TSP-residual is ~25%, **not** ~11%. Canonical is at the extreme low end of the subset, suggesting additional architectural constraints push it down past compression-tail's typical performance.

Quantitatively: compression-tail accounts for ~(34.7 − 25.0) / (34.7 − 10.7) = **40%** of the random-to-canonical TSP-optimality gap. The remaining 60% is carried by other principles documented in cross-finding-018 (multi-principle architecture).

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-690-causal-generative-prereg.md`
- Script: `scripts/h_new_690_causal_generative.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-690.json`
- Findings: `findings/phase-b-hypotheses/h-new-690-causal-generative.md`

## Honest deviations from pre-reg

1. **Sample count: 90 instead of 100.** Sampler indexing started at step `n_burn + sample_every` = 1100, gave 90 samples through step 10000 instead of 100. Does not affect verdict (0% across all thresholds; canonical not reachable).
2. **Warmup fell back to canonical-start.** Pre-registered fallback explicitly allowed for this case.

No other deviations.

## Queued follow-ups

H-NEW-690b/c/d/e enumerated in §7 of findings (alternate feature spaces, multi-constraint extension, loosened tolerance, cooler MH temp).

*wa-Allāhu aʿlam.*
