---
finding_id: h-new-144
title: "Cyclic-TSP benchmark for M1: is the mushaf Hamiltonian-CYCLE near-optimal?"
specialist: (unassigned; queued for next-session / specialist-b / inline team-lead)
date_prereg: 2026-04-17
seed: 20260419
bonferroni_k: 2
bonferroni_family: h-new-144-cyclic-tsp
alpha_bon: 0.025
alpha_raw: 0.05
direction_primary_ratio: "R := L_cycle(σ*) / L_min_cycle ≤ 1.15 (pre-registered threshold)"
direction_secondary_perm: "L_cycle(σ*) < null-permutation cyclic-length; one-sided lower-tail p < 0.025"
K_top_roots: 500
dirichlet_alpha: 0.5
length_control: "MW-1 via L1-normalization of per-surah distributions"
rules_tuple: "(114 surahs Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya, cyclic path, Lin-Kernighan-3 approximation)"
perms: 10000
verdict_ceiling: "PASS (refines M1 cross-finding-013; does not promote above CONFIRMED — M1 is already CONFIRMED)"
parent_model: "scratch/theorist-2026-04-17-m1-merger.md §5; scratch/theorist-2026-04-17-unified-equation.md"
---

# [[h-new-144-cyclic-tsp|H-NEW-144]] — Cyclic-TSP benchmark for M1

## Motivation

Per theorist T-P analysis (`scratch/theorist-2026-04-17-m1-merger.md`
§5), [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] CONFIRMED M1 (Structured Hamiltonian-cycle
mushaf ordering) via the conjunction of:
- [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] (Hamiltonian-PATH geodesic; L_mushaf/L_2opt ≈
  1.107 on roots)
- [[h-new-137-wrap-around-closure|H-NEW-137]] + [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] (wrap-around edge short)
- [[h-new-130-fisher-rao-residuals|H-NEW-130]] + [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] (structured hinges)

But the CYCLE version of the ratio L_cycle / L_min_cycle has NOT
been computed. [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s 2-opt benchmark is the open-path
TSP-2opt, not the cyclic-TSP-2opt. If the mushaf-cycle is much
further from its optimum than the mushaf-path is from its own, M1's
"near-optimal cycle" claim is weaker than currently asserted.

[[h-new-144-cyclic-tsp|H-NEW-144]] fills this gap. It is a REFINEMENT of a CONFIRMED finding,
not a novel prediction — the verdict ceiling is PASS (additional
support for M1) or PARTIAL/DEMOTE (M1 demoted from "near-optimal
cycle" to "significantly-short-but-not-near-optimal cycle").

## Hypothesis

**Primary (H1, ratio)**. Let L_cycle(σ*) = Σᵢ₌₁¹¹⁴ d_FR(σ*(i),
σ*(i+1 mod 114)) be the Fisher-Rao path length of the mushaf CYCLE
(including the wrap-around Q 114 → Q 1 edge). Let L_min_cycle be the
approximate minimum-cycle-length on the 114-node Fisher-Rao distance
graph, computed via Lin-Kernighan-3 (an improvement over the 2-opt
bound used in [[h-new-111-fisher-rao-mushaf|H-NEW-111]]).

**Claim**: R := L_cycle(σ*) / L_min_cycle ≤ 1.15 (pre-registered
threshold).

**Secondary (H2, permutation)**. L_cycle(σ*) < null-distribution
cyclic-length across 10,000 random-permutation cyclic paths.
One-sided lower-tail p < α_bon = 0.025.

## Pre-registered Bonferroni family

**k = 2** (primary ratio + secondary permutation). **α_bon = 0.05/2 =
0.025**.

- **PASS (both cells)**: R ≤ 1.15 AND permutation p < 0.025 → M1's
  "near-optimal cycle" claim EARNS explicit cyclic-TSP benchmark
  validation. M1 CONFIRMED status remains CONFIRMED (no promotion
  higher; already at top verdict).
- **PARTIAL-A (ratio only)**: R ≤ 1.15 AND permutation p fails —
  very unlikely given z = −11 on path, z = −4 on closure. If this
  occurs, pipeline bug likely; investigate.
- **PARTIAL-B (permutation only)**: R > 1.15 AND permutation p <
  0.025. Cycle is significantly short vs null but not near-optimal.
  **Demote** M1's modifier from "structured geodesic cycle" to
  "structured significantly-short cycle". Keep [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] as
  CONFIRMED on the topology claim; downgrade the "near-optimal"
  language in future references.
- **DEMOTE (neither passes)**: R > 1.25 AND permutation p fails.
  M1's cycle claim is REFUTED at the near-optimality axis; retain
  [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] as path-geodesic-with-wrap-around but drop
  the unified "structured Hamiltonian cycle" language.
  **Highly unlikely given existing parent confirmations.**

## MW-5 positive control

Before executing H1/H2, verify that L_mushaf (open-path version,
without the Q 114 → Q 1 edge) reproduces [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s result
of 85.76 ± 0.5 on roots. This ensures the D-matrix pipeline is sound.

## Specification

### Data

- D-matrix: reuse `findings/phase-b-hypotheses/csv/h-new-111.json`
  (precomputed 114×114 Fisher-Rao distance matrix on top-500 QAC-STEM
  roots, Dirichlet-0.5, L1-normalized, basmala in Q 1 only)
- No new feature extraction required

### Procedure

1. **MW-5 check**: load D-matrix, verify L_mushaf_path = Σᵢ₌₁¹¹³
   D[σ*(i), σ*(i+1)] matches 85.76 ± 0.5
2. **L_cycle computation**: L_cycle(σ*) = L_mushaf_path + D[σ*(114),
   σ*(1)]
3. **L_min_cycle approximation**: run Lin-Kernighan-3 on the cyclic
   TSP problem. Initial tour: canonical mushaf. Maximum iterations:
   1000. Convergence: no improvement in 100 iterations.
   - Implementation: use `python-tsp` library or equivalent;
     Lin-Kernighan-3 with 10 random-restart seeds, take best.
   - Seed for restarts: 20260419, 20260420, ..., 20260428 (10 seeds).
4. **Compute R**: L_cycle(σ*) / L_min_cycle
5. **Permutation null**: 10,000 random permutations of {1, ..., 114};
   for each permutation π, compute L_cycle(π). One-sided p =
   (#{perm_L_cycle ≤ observed L_cycle(σ*)} + 1) / 10,001.

### Seed

Seed 20260419 for the permutation RNG.
Seeds 20260419–20260428 for the 10 Lin-Kernighan-3 restarts.

### Garden-of-forking-paths (locks)

1. **K = 500 roots, Dirichlet α = 0.5** — matches [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]
   parent
2. **Fisher-Rao primary metric** — no cross-metric replication at this
   pre-reg (that would be a separate H-NEW-144b follow-up)
3. **L_min_cycle via Lin-Kernighan-3 with 10 restarts** — commits to
   this heuristic; Concorde-exact would be a separate future pre-reg
4. **Bonferroni k=2, α_bon=0.025** — no additional cells added mid-run
5. **R_threshold = 1.15** — pre-registered; NOT adjusted post-hoc based
   on observed value
6. **10,000 permutations** — fixed count; seed 20260419

## Falsifiability

- PASS: M1 "near-optimal cycle" language earns explicit benchmark
  validation
- PARTIAL-B (likely if at all): forces downgrade of "near-optimal"
  modifier
- DEMOTE (very unlikely): forces retraction of cycle-claim

## Expected outcome (theorist prediction)

- **R ≈ 1.08-1.12** (cycle closure ADDS a short edge to an
  already-short path; ratio should tighten or stay similar to the
  1.107 path-ratio from [[h-new-111-fisher-rao-mushaf|H-NEW-111]])
- **Permutation p = 0.0001 (floor)** — L_cycle will be z ≈ −11 or
  deeper below random-cycle null

## Runtime

- MW-5: < 1 second
- L_cycle computation: < 1 second
- Lin-Kernighan-3 with 10 restarts on 114-node: 1-3 minutes total
- Permutation null (10K × 114-edge sum on precomputed D): ~30 seconds
- **Total: < 5 minutes**

## Verdict ceiling

**PASS** (refines M1 which is already CONFIRMED at [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]).
The pre-reg's primary value is:
1. Closes an acknowledged refinement gap ([[cross-finding-013-mushaf-topological-ring|cross-finding-013]] §"TSP
   optimality is upper-bounded")
2. Potentially triggers modifier-downgrade ("near-optimal" →
   "significantly-short") if R > 1.15
3. Provides the cyclic-TSP benchmark for future feature-space
   replications

## Connection to other findings

- Direct parent: [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] (M1 CONFIRMED; cycle-TSP gap noted)
- Grandparent: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] (open-path geodesic CONFIRMED;
  2-opt ratio 1.107)
- Co-descendant: [[h-new-144-cyclic-tsp|H-NEW-144]] candidate (content/length decomposition;
  complementary refinement of M1's mechanism)
- Theorist context: `scratch/theorist-2026-04-17-m1-merger.md` §5
  (T-P.2 rationale)

## Handoff

Execution path:
1. Open `findings/phase-b-hypotheses/csv/h-new-111.json`
2. MW-5 verify path length
3. Write `scripts/h_new_142_cyclic_tsp.py` with Lin-Kernighan-3 loop
4. Run; write results to `findings/phase-b-hypotheses/csv/h-new-144.json`
5. Author findings file `findings/phase-b-hypotheses/h-new-144-cyclic-tsp.md`
6. Journal at `journal/h-new-144-run-1.md`

## Files

- Pre-reg (this file):
  `findings/phase-b-hypotheses/h-new-144-cyclic-tsp-prereg.md`
- Parent D-matrix:
  `findings/phase-b-hypotheses/csv/h-new-111.json`
- Parent finding (M1 CONFIRMED):
  `findings/phase-b-hypotheses/cross-finding-013-mushaf-topological-ring.md`
- Theorist context:
  `scratch/theorist-2026-04-17-m1-merger.md`
