---
id: h-new-228
title: SA minimum conditional-entropy ordering — mushaf is NOT near-optimum (gap ≈ 0.51)
phase: B (hypothesis)
date: 2026-04-17
status: PASS (gating: SA beats mushaf from all 3 starts) + descriptive GAP ≈ 0.51
seed: 20260419
parent_findings: [h-new-171]
rules_tuple: (114 surahs Hafs-Kūfan, no-tashkeel, QAC-STEM roots, top-K=100, Dirichlet α=0.5, L1-norm, Fisher-Rao, rank-exp kernel, 2-opt SA)
prereg_sha256: (see JSON)
---

# [[h-new-228-sa-min-entropy-ordering|H-NEW-228]] — Simulated annealing finds H_min ≈ 16.5 bits; mushaf (50.15) is **not** near-optimum

## Headline

Simulated annealing on the same rank-exp conditional-entropy cost
as [[h-new-171-entropy-rate-mushaf|H-NEW-171]] finds orderings with **H ≈ 16.5 bits**, down from
mushaf's **50.15 bits** and null-mean **82.92 bits**. All three
starts (mushaf, Nöldeke, random) converge to within 1.3 bits
of each other, suggesting 16.5 is near the global minimum.

**gap_fraction = (H_mushaf − H_SA-min) / (H_null_mean − H_SA-min) = 0.507.**

The mushaf sits almost exactly *halfway* between the SA-optimum
and the random-null mean. It is clearly structured (z = −8.94 vs
null per [[h-new-171-entropy-rate-mushaf|H-NEW-171]]), but not minimum-entropy optimised: roughly 34 bits
of further compression are reachable, yet the canonical order
leaves them on the table.

## Numbers

| Metric | Value (bits) |
|---|---:|
| H_mushaf | 50.15 |
| H_noldeke | 44.25 |
| H_random_start | 81.86 |
| H_null_mean ([[h-new-171-entropy-rate-mushaf|H-NEW-171]]) | 82.92 |
| **H_SA_min (best of 3)** | **16.45** |
| H_SA_max (worst of 3) | 17.71 |
| SA-spread across starts | 1.25 |
| greedy-NN from s1 ([[h-new-171-entropy-rate-mushaf|H-NEW-171]] MW-5) | 20.92 |

| SA start | H_start | H_best | Beat mushaf? |
|---|---:|---:|---|
| mushaf (seed 20260419) | 50.15 | **16.45** | yes |
| noldeke (seed 20260420) | 44.25 | 17.71 | yes |
| random (seed 20260421) | 81.86 | 16.70 | yes |

- 3 / 3 runs found orderings with H < H_mushaf (gating passes at
  α_bon = 0.05, k = 1).
- SA beats greedy-NN (20.92 → 16.45, a 4.5-bit improvement),
  confirming greedy-NN is locally but not globally optimal.
- Inter-start spread 1.25 bits is small relative to the 34-bit
  mushaf-to-optimum gap, indicating the SA-bound is plausibly
  close to the global minimum.

## Verdict

**Gating: PASS.** SA reliably beats the mushaf from all three
starts (mushaf, Nöldeke, random).

**Descriptive conclusion: mushaf is NOT near-optimum on root
conditional entropy.** gap_fraction ≈ 0.51 places the mushaf in
the "modestly-structured" category — closer to random than to the
SA-optimum.

## Interpretation

[[cross-finding-011-mushaf-fisher-rao-confirmed|Cross-finding-011]] and [[h-new-171-entropy-rate-mushaf|H-NEW-171]] establish that the mushaf is
structured relative to random permutations: about 33 bits/step
below null. This test re-frames that result:

**Mushaf ≠ minimum-entropy ordering on roots.** The 34-bit further
compression reachable by SA implies the canonical arrangement
optimises for something *other than* pure root-distribution
proximity. Candidate principles include:

1. Thematic / narrative continuity (not tested here)
2. Prosodic / phonological continuity
3. Decreasing-length bias (Nöldeke-adjacent heuristic)
4. Liturgical / recitation-cycle constraints
5. **No single optimisation** — heterogeneous mix of organising
   principles

The fact that **Nöldeke's chronology (H = 44.25)** is lower than
the mushaf (50.15) is suggestive: chronology explains ~6 bits of
the mushaf's 33-bit structure, with 24+ bits from other features.

## Relationship to prior findings

- **Consistent with [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s L_mushaf/L_2opt ≈ 1.11**:
  there, mushaf total path is 11% longer than optimal;
  here, mushaf entropy is ~50 % of the way from optimum to null.
  Different summaries of the same "structured but not TSP-optimal"
  fact.
- **Tightens [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]**: the mushaf is neither at the
  geometric optimum (shortest tour) nor at the information-theoretic
  optimum (lowest conditional entropy). Whatever orders the mushaf
  is NOT a minimum-entropy root-continuity heuristic.

## What this does NOT show

- SA-min = 16.45 is an **upper bound** on the true global minimum
  for this cost function; a stronger optimiser might find lower.
- Descriptive gap_fraction is not a pre-registered significance
  test. No claim is made about whether 0.51 is "large" or "small"
  in some absolute sense; it is a *quantitative frame* for the
  mushaf's position on the structured-optimum ↔ null spectrum.
- The mushaf may still be near-optimum under a DIFFERENT cost
  function (not tested). Only root conditional entropy is
  addressed here.
- No semantic claim: we do NOT conclude the mushaf was "designed"
  to minimise or NOT-minimise anything. The finding is geometric.

## Limitations

- Heuristic optimiser; no optimality certificate.
- Same feature substrate as parent (QAC-STEM roots, K=100); not
  an independent replication of [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]].
- 2-opt neighbourhood may miss better optima reachable by larger
  moves (e.g. 3-opt, Or-opt); acceptance-rate ≈ 24 % suggests
  reasonable but not aggressive mixing.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-228-sa-min-entropy-ordering-prereg.md`
- Script: `scripts/h_new_228_sa_min_entropy_ordering.py`
- Results JSON: `findings/phase-b-hypotheses/csv/h-new-228.json`
