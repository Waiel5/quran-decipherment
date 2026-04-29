---
id: h-new-228
title: Simulated annealing for MINIMUM conditional entropy ordering — is the mushaf near-optimum?
phase: B (hypothesis)
date: 2026-04-17
status: PRE-REGISTERED
seed: 20260419
parent_findings: [h-new-171]
rules_tuple: (114 surahs Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-Surah-1, QAC-STEM roots, top-K=100, Dirichlet α=0.5, L1-norm, Fisher-Rao, rank-exponential kernel for H)
bonferroni_k: 1
---

# [[h-new-228-sa-min-entropy-ordering|H-NEW-228]] — SA-minimum conditional entropy ordering

## Motivation

[[h-new-171-entropy-rate-mushaf|H-NEW-171]] established H_mushaf(s_{i+1}|s_i) = 50.15 bits, z = −8.94
vs null mean 82.92. The mushaf is FAR from random. But is it
**near-optimal** in the minimum-entropy sense, or merely
"structured"? Greedy-NN from surah 1 gave mean_rank = 14.04 and
H = 20.92 bits — an existence proof that orderings with H < 50.15
exist. SA on the same cost function will characterise the feasible
minimum.

## Hypothesis

**H1** (alternative): SA can find orderings with H < H_mushaf.
Quantity of interest: H_min_SA, the best H found over 3 SA runs
(seeds: mushaf-start, Nöldeke-start, random-start).

Because we already know from MW-5 that greedy-NN achieves H ≈ 21,
H_min_SA < 50.15 is essentially certain. The *scientific* question
is the **gap**: (H_mushaf − H_min_SA) / (H_null_mean − H_min_SA).

**Decision rule (descriptive, not pass/fail gating):**

- gap_fraction := (H_mushaf − H_min_SA) / (H_null_mean − H_min_SA)
- gap_fraction < 0.10 ⇒ mushaf is "near-optimum" (within 10 % of
  the structured-minimum → null-mean span)
- 0.10 ≤ gap_fraction < 0.50 ⇒ "structured but not optimal"
- gap_fraction ≥ 0.50 ⇒ "modestly structured" (closer to null than
  to SA-optimum)

## Primary test (gating)

Single two-sided test: **is H_mushaf within the SA-trajectory distribution?**
We test whether mushaf's H is plausibly drawn from the family of
"well-optimised but not-fully-converged" orderings, by checking:

- H_mushaf < SA-minimum of random-start run (control that SA actually
  moves below 50.15)

bonferroni_k = 1 because this is a single gating test. α_bon = 0.05.

p is empirical: proportion of 3 independent SA runs (different
starts) that end up with H < 50.15. If all 3 do (p = 0), H1 is
supported.

## SA protocol (locked)

- **Cost**: conditional entropy H_hat(s_{i+1}|s_i) in bits,
  computed identically to [[h-new-171-entropy-rate-mushaf|H-NEW-171]] (rank-exp kernel, K=100 roots,
  Dirichlet α=0.5, Fisher-Rao, L1-norm)
- **Proposal**: 2-opt swap (reverse a contiguous segment). Segment
  length uniform in [2, 30].
- **Temperature schedule**: geometric. T_0 = 5.0 bits,
  T_final = 0.001 bits, n_steps = 500 000 per run.
  β = (T_final/T_0)^(1/n_steps).
- **Acceptance**: Metropolis. Accept if ΔH ≤ 0, else with prob
  exp(−ΔH/T).
- **Starts**:
  1. mushaf order (1..114)
  2. Nöldeke chronology order (from data/revelation-order.csv)
  3. Single random permutation seeded by SEED
- **Seeds**: master SEED = 20260419. Run-seeds: SEED+0, SEED+1,
  SEED+2.

## Secondary: multi-start robustness

Report H_best per start; sigma-gap between best and 2nd-best = a
robustness proxy. If all 3 starts converge to the same H (±0.5 bits),
the SA landscape is likely smooth and H_min_SA is plausibly global.

## What this test CAN conclude

1. Existence of orderings strictly better than mushaf (already
   known from greedy-NN; SA will tighten the bound).
2. Quantitative gap: mushaf's position in the structured-optimum
   ↔ random-null span.
3. Whether the mushaf sits on a natural plateau (gap_fraction
   small) or is "loosely structured" (gap_fraction large).

## What this test CANNOT conclude

- Does NOT identify the global minimum (SA is heuristic). H_min_SA
  is an UPPER bound on the true minimum.
- Does NOT test any alternative kernel / feature space. Only the
  root-distribution substrate locked in [[h-new-171-entropy-rate-mushaf|H-NEW-171]].
- gap_fraction is a descriptive summary, not a pre-registered test
  of a semantic hypothesis. We do NOT claim "the mushaf was
  designed for minimum root-entropy."

## Files

- Pre-reg: this file
- Script: `scripts/h_new_228_sa_min_entropy_ordering.py`
- Results JSON: `findings/phase-b-hypotheses/csv/h-new-228.json`
- Result MD: `findings/phase-b-hypotheses/h-new-228-sa-min-entropy-ordering.md`
