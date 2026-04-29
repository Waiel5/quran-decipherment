---
finding_id: h-new-225
title: "Adversarial search — can ANY ordering of 114 surahs beat the mushaf path length?"
specialist: (autonomous)
date_prereg: 2026-04-17
seed: 20260419
bonferroni_k: 1
bonferroni_family: h-new-225-adversarial
alpha_bon: 0.05
K_top_roots: 500
dirichlet_alpha: 0.5
length_control: "MW-1 via L1-normalization (inherited from parent D-matrix H-NEW-111)"
rules_tuple: "(114 surahs Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya, open Hamiltonian path, mushaf-initialized 2-opt + 100-random-start ACO/SA search)"
perms: 0  # not a permutation test; direct optimization
verdict_ceiling: "PASS (empirical refinement of M1's near-optimality claim — locates the gap between L_mushaf and the best achievable L_search)"
parent_model: "H-NEW-111 (L_mushaf / L_2opt = 1.107); H-NEW-144 (cyclic 2-opt ratio 1.0945)"
---

# [[h-new-225-adversarial-search|H-NEW-225]] — Adversarial search for shorter-than-mushaf orderings

## Motivation

[[h-new-111-fisher-rao-mushaf|H-NEW-111]] established that the mushaf's Fisher-Rao open-path length
(L_mushaf = 85.76) is 11.46 SD below random and within 10.7% of an
approximate TSP optimum (L_2opt = 77.47, from greedy-NN + 2-opt over
all 114 starts). [[h-new-144-cyclic-tsp|H-NEW-144]] tightened the cyclic ratio to 1.0945.

Both parents leave one question answered only indirectly: **if we
SEARCH ADVERSARIALLY for an ordering that beats the mushaf — using
2-opt local improvement initialized AT the mushaf plus stochastic
metaheuristics (simulated annealing) from 100 diverse random starts —
how much shorter than 85.76 can we get?**

This is the strongest empirical test of optimality the D-matrix
permits without an exact solver. If 2-opt-from-mushaf finds ANY
swaps that reduce L below 85.76, mushaf is not even a local optimum.
If 100-restart SA cannot find anything below ~77, mushaf is
demonstrably ~10.7% above a strong heuristic floor (consistent with
[[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s bound).

## Hypothesis

**Primary (single cell, no Bonferroni family)**: Let L_search_min be
the minimum open-path length found by the combined search:
 - 2-opt local search initialized at the mushaf ordering itself
 - Simulated annealing (SA) + 2-opt polishing from 100 random starts
   (seeds 20260419..20260518)

**Claim**: L_search_min is STRICTLY LESS than L_mushaf = 85.76.
(i.e., there EXIST orderings shorter than the mushaf — mushaf is NOT
globally optimal on this metric.)

This is an ADVERSARIAL test: the null is "mushaf is unbeatable even
by 10 million random + 2-opt iterations". Given [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s L_2opt =
77.47 < 85.76, the answer is certainly YES — but this pre-reg commits
to quantifying the gap:
 - **gap_abs** := L_mushaf − L_search_min
 - **gap_rel** := L_mushaf / L_search_min

## Pre-registered decision rule (k=1, α_bon=0.05)

Because this is an existence question with a known-positive parent
finding ([[h-new-111-fisher-rao-mushaf|H-NEW-111]] already exhibited L_2opt = 77.47 < 85.76), there
is no meaningful null hypothesis to reject via p-value. The
pre-registered decision rule is ratio-threshold:

- **PASS (gap exists, mushaf non-optimal)**: gap_rel > 1.01 (at least
  1% shorter ordering exists).
- **EXTREME-GAP (mushaf far from optimum)**: gap_rel > 1.15.
- **SURPRISE-NULL (mushaf unbeatable)**: gap_rel ≤ 1.01 → mushaf is
  itself a 2-opt + SA local optimum in this 114-node space → STRONG
  evidence of deliberate near-optimal design at the information-
  geometric axis.

Expected outcome (theorist): PASS with gap_rel ≈ 1.107 (matching
[[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s 2-opt ratio), i.e., L_search_min ≈ 77.47.

If L_search_min is **lower** than [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s L_2opt = 77.47, this
TIGHTENS the parent's upper-bound of the true TSP optimum — a
self-verifying tightening amendment.

## MW-5 positive control

Reproduce L_mushaf = 85.76 ± 0.01 from the reloaded D-matrix before
running any search. Ensures D-matrix reload is correct.

## Specification

### Data
- D-matrix: reload `findings/phase-b-hypotheses/csv/h-new-111.json`'s
  `D_matrix_upper_triangular` field (6441 pairs for 114 nodes).
- No new feature extraction.

### Procedure

1. **MW-5**: load D-matrix, verify L_mushaf = 85.76 ± 0.01.
2. **Mushaf-init 2-opt**: Run full 2-opt (max 50 passes, standard
   best-improvement on open path) starting from σ* = [1..114]. Record
   L_mushaf_2opt and the first N swaps that reduce length (if any).
3. **SA + 2-opt from 100 random starts**:
   - For seed ∈ {20260419, 20260420, ..., 20260518} (100 seeds):
     - Random shuffle of [1..114].
     - Simulated annealing: T_0 = 5.0, cooling factor 0.995, 10,000
       proposal iterations. Proposal: random 2-opt reversal or random
       swap (50/50). Metropolis accept.
     - 2-opt polish after SA.
     - Record final length.
   - L_sa_min := min over 100 restarts.
4. **L_search_min := min(L_mushaf_2opt, L_sa_min, L_2opt_parent_77.47)**.
5. Compute gap_abs and gap_rel vs L_mushaf.
6. Report where in the rank-ordering of 100 restarts mushaf-initialized
   2-opt falls (rank-in-distribution).

### Seed

Primary RNG seed: 20260419 (matches [[h-new-144-cyclic-tsp|H-NEW-144]]'s family).
SA-restart seeds: 20260419..20260518 (100 consecutive).

### Garden-of-forking-paths (locks)

1. **D-matrix reused from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]** (K=500, α_dir=0.5, Fisher-Rao,
   L1-normalized). No re-extraction; ensures direct comparability.
2. **100 SA restarts, 10K iterations each**, T_0 = 5.0, cooling 0.995,
   mixed 2-opt-reversal + swap proposal (50/50). Committed pre-run.
3. **Bonferroni k=1** (single PASS/EXTREME/SURPRISE-NULL decision cell).
4. **α_bon = 0.05** (descriptive, not used as p-value gate).
5. **L_search_min is min over ALL searches run** (mushaf-2opt, 100-SA,
   and the parent [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s L_2opt = 77.47 brought in as a known
   upper bound).

## Falsifiability

- **PASS** (expected): L_search_min < L_mushaf. Mushaf is NOT optimal
  at this metric, and the gap is ~10% (matching [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s ratio).
  Does NOT invalidate [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s significance result — it merely
  quantifies the gap empirically.
- **SURPRISE-NULL** (shock): L_search_min ≥ L_mushaf. Mushaf is a
  local optimum robust to 100-restart SA + 2-opt. Promotes M1's
  "near-optimal" language dramatically.
- **EXTREME-GAP**: gap_rel > 1.15. Mushaf is further from optimum than
  [[h-new-111-fisher-rao-mushaf|H-NEW-111]] reported — likely indicates SA found a region 2-opt missed;
  update [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s ratio in the ledger.

## Expected outcome

- L_search_min ≈ 77.4 ± 0.3 (matching or slightly tightening [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s
  L_2opt = 77.47).
- gap_abs ≈ 8.3, gap_rel ≈ 1.107.
- Mushaf-init 2-opt converges to L ≈ 79-81 (2-opt from ordered starts
  is known to find sub-optimal basins).
- PASS on the existence cell; no SURPRISE.

## Runtime

- MW-5: <1 s
- Mushaf-2opt: <5 s (50 passes × 114 × 114 D-lookups)
- 100-SA × 10K iter: ~1-3 min
- Total: <5 minutes

## Interpretation logic

This test does not revise [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s conclusion; it refines the
empirical claim. Specifically:

- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]] (PRIMARY)**: L_mushaf vs 10K random. z=−11.46. UNCHANGED.
- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]] (SECONDARY A)**: ratio 1.107. UPDATED to the final
  L_search_min from [[h-new-225-adversarial-search|H-NEW-225]] if that's lower than 77.47.
- **M1 near-optimality**: strengthened if L_search_min is close to
  77.47 (search not finding anything dramatically better); weakened if
  search finds substantially lower (indicating heuristic escape).

## Connection to prior findings

- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** (parent): L_mushaf = 85.76, L_2opt = 77.47 from greedy
  + 2-opt. We use its D-matrix verbatim.
- **[[h-new-144-cyclic-tsp|H-NEW-144]]** (sibling): cyclic ratio 1.0945. Different problem (cycle
  not open path); we stay open-path for direct [[h-new-111-fisher-rao-mushaf|H-NEW-111]] comparability.
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (CONFIRMED): M1 open-path geodesic claim.
- **[[cross-finding-013-mushaf-topological-ring|cross-finding-013]]** (CONFIRMED): M1 cyclic claim.

## Files

- Pre-reg (this file):
  `findings/phase-b-hypotheses/h-new-225-adversarial-search-prereg.md`
- Script: `scripts/h_new_225_adversarial_search.py`
- JSON output: `findings/phase-b-hypotheses/csv/h-new-225.json`
- Findings file: `findings/phase-b-hypotheses/h-new-225-adversarial-search.md`
- Journal: `journal/h-new-225-run-1.md`
