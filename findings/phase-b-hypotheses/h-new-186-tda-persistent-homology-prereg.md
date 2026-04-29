---
finding_id: h-new-186
title: "Persistent homology (TDA) on the 114-surah Fisher-Rao D-matrix — topological holes in surah-space"
specialist: h-new-186-specialist
date_prereg: 2026-04-17
seed: 20260419
bonferroni_k: 2
bonferroni_family: h-new-186-tda-persistent-homology
alpha_bon: 0.025
alpha_raw: 0.05
parent_data: h-new-111 (Fisher-Rao 114×114 D-matrix, CONFIRMED structured)
cross_refs:
  - cross-finding-011 (mushaf is Fisher-Rao geodesic-like)
  - cross-finding-013 (mushaf is Hamiltonian RING; wrap-around Q114→Q1)
  - T5 prior-art (earlier persistent-homology run on T-1 framings was NULL)
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan) — inherited from H-NEW-111"
---

# H-NEW-186 — Persistent homology (TDA) on the 114-surah Fisher-Rao D-matrix

## Motivation

[[cross-finding-013-mushaf-topological-ring|cross-finding-013]] shows the 114-surah mushaf forms a Hamiltonian CYCLE in
Fisher-Rao information-space: the canonical reading path closes at
Q114→Q1. A Hamiltonian cycle is a 1-dimensional loop through all
vertices — it is a *topological* property that can be detected without
reference to the mushaf ordering at all, by asking whether the underlying
metric space has genuine 1-cycle structure.

Persistent homology (TDA) on the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] Fisher-Rao D-matrix asks a
different, stronger question: beyond the single 114-cycle already known,
**are there additional loops / topological holes inside surah-space**?
Such sub-rings would indicate cluster-of-clusters architecture (e.g. a
"Meccan sub-ring" connecting a group of short late-Meccan surahs, or a
"legal-corpus sub-ring" connecting long Medinan surahs).

Earlier T5 persistent homology on T-1 framings was NULL. This attempt
re-asks the question on a demonstrably-structured D-matrix ([[h-new-111-fisher-rao-mushaf|H-NEW-111]]
is CONFIRMED at z=-11.46, p<10⁻⁴) and with an explicit null from random
label permutations of the same D-matrix.

## Hypotheses

**Primary 1 — H_1 count excess (one-sided upper-tail)**: the number of
H_1 (1-dimensional hole / loop) features in the Vietoris-Rips persistence
diagram of the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D-matrix that persist more than a birth-death
gap of 0.3 is GREATER than the 95th percentile of the same statistic
computed on 10,000 random surah-label permutations of the same D-matrix.

Primary 2 — max H_1 persistence (one-sided upper-tail)\**: the maximum
(death − birth) value among H_1 features in the real D-matrix is GREATER
than the 95th percentile of the same statistic under the permutation
null.

**Bonferroni k = 2 → α_bon = 0.025 per test.**

## Definitions

- **Vietoris-Rips complex at scale ε**, VR(X, ε): add a k-simplex on
  vertices v_0,..,v_k whenever all pairwise distances D[v_a, v_b] ≤ ε.
- **Filtration**: compute VR(X, ε) for ε across a grid. Birth(σ) = the
  smallest ε at which simplex σ appears.
- **H_0**: connected-component homology. β_0(ε) = number of connected
  components at scale ε. Starts at 114, decreases as components merge,
  ends at 1 when the graph is fully connected.
- **H_1**: 1-dimensional hole homology (loops not filled by triangles).
  A 1-cycle is born at ε_birth when its first edge appears without
  closing via a 2-simplex (triangle); it dies at ε_death when a chain of
  2-simplices (triangles) fills it in. Persistence = ε_death − ε_birth.
- "Significant" loop (pre-registered, locked): persistence ≥ 0.3 in
  Fisher-Rao units.

## Method (locked before viewing results)

### Data

The 114×114 Fisher-Rao D-matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]
(`findings/phase-b-hypotheses/csv/h-new-111.json` field
`D_matrix_upper_triangular`).

### Filtration grid

ε ∈ {0.05, 0.10, 0.15, ..., 3.00} (60 values, step 0.05, covering the
full D-range [0, ~π]). The task-spec grid {0.1, 0.2,..., 1.0} is a
subset of this finer grid; the finer grid is used to get smoother
persistence values.

### H_0 computation

Union-find over edges sorted by weight. At scale ε, β_0(ε) = number of
union-find components with edges ≤ ε. Each H_0 feature births at ε=0
(every vertex is a component) and dies when it merges into another
component (elder rule: the younger component dies).

### H_1 computation (manual incremental algorithm)

For this 114-vertex VR complex we build H_1 via the standard
*incremental-by-filtration* algorithm, using only 0, 1, and 2-simplices
(sufficient for H_1):

1. Sort all C(114,2)=6,441 edges by D-weight ascending.
2. Sort all C(114,3)=240,464 triangles by (max pairwise D) ascending.
   (A triangle appears at max of its 3 edge weights.)
3. Sweep ε from 0 upward. Maintain the cycle basis of 1-cycles in the
   current 1-skeleton as a set of vectors over GF(2) (edges as basis).
4. When a new edge e appears: if it closes a loop (its endpoints already
   connected in the current 0-skeleton), it BIRTHS a new 1-cycle.
   Represent the new cycle as the XOR of the path in the spanning tree
   between its endpoints ∪ {e}.
5. When a new triangle t appears at its max-edge weight: it is a
   2-boundary. Using elimination, if t's boundary 1-chain equals the
   XOR of some subset of living 1-cycles, the YOUNGEST of those cycles
   DIES at this ε (elder-rule: older cycles persist). If t's boundary
   doesn't reduce to any living cycle, it is a redundant 2-simplex
   (collapses a pair of already-dead classes; no H_1 change).

This is a direct, textbook implementation of H_1 persistence from the
filtered VR complex. I verify it with MW-5 (below).

### Null model

10,000 random permutations of the surah-label vector applied to the
D-matrix. Since the D-matrix is symmetric and zero-diagonal, permuting
labels is equivalent to simultaneously permuting rows AND columns by
the same permutation; this preserves the multiset of distances but
destroys the spatial arrangement. For each permutation recompute the
same H_1 count and max-H_1-persistence statistics.

(Note: because simultaneous row+column permutation of a symmetric matrix
with zero diagonal yields an isomorphic VR complex, the persistence
diagram is INVARIANT under such permutation. Therefore the null model
used here is **random distance-shuffle**: we destroy metric structure by
randomly shuffling the upper-triangular entries of D while preserving
the multiset of pairwise distances. This is the correct null for "does
the metric structure of surah-space create loops beyond what random
pairwise-distance assignments would produce?".)

Because VR on 10,000 114-node matrices with H_1 is computationally
expensive, we use a REDUCED H_1 null: sweep only the coarse grid
{0.1, 0.2, ..., 1.0} and use a *cycle-space-rank* proxy (see below) that
requires only edge sweeping, no triangle enumeration. Pre-registered
choice: if triangle-based H_1 on the real D is infeasible in practice,
fall back to the cycle-rank proxy on BOTH real and null.

### Cycle-rank proxy for H_1 (fast)

For a filtered graph G(ε) = (V, E_ε), the cycle-space dimension is
|E_ε| − |V| + β_0(ε). This equals the number of H_1 features in the
1-skeleton clique-expansion WITHOUT filling by triangles. It OVER-counts
H_1 (every triangle is a cycle-space basis element not yet filled). But
under the SAME definition applied to both real and null, comparing
cycle-rank excess gives a valid proxy for metric-induced loop-richness.

We compute H_1 two ways:
  (a) True H_1 persistence diagram on the real D-matrix (triangle-based).
  (b) Cycle-rank(ε) curve on real and on all 10K nulls; compare mean and
      max-over-ε between real and null.

The **primary tests** use (a). The **null comparison** uses both: (a) if
feasible, (b) as the pre-registered fallback / cross-check.

### MW-5 positive control

Generate synthetic 3-cluster data: three clusters of 38 points each in
R^2 at cluster centers (0,0), (3,0), (1.5, 2.6), with within-cluster
noise σ=0.2. Compute Euclidean D-matrix on 114 points. Pre-registered:
at some ε-scale the persistence diagram should show exactly 3 H_0
features persisting > 1.0 (three obvious clusters). If not, the H_0
algorithm is broken.

A second MW-5 control for H_1: generate 30 points uniformly on the unit
circle in R^2. Their VR complex should exhibit one persistent H_1
feature (the circle itself) with persistence ≈ some nontrivial gap,
larger than any H_1 features on the same 30 points sampled uniformly
from the filled disk. If not, H_1 algorithm is broken.

## Pre-committed acceptance window

- **PASS PRIMARY 1**: #{H_1 features with persistence ≥ 0.3} on real
  D-matrix strictly exceeds the 97.5th percentile (α_bon=0.025) of the
  same count on 10K permutation nulls.
- **PASS PRIMARY 2**: max H_1 persistence on real D-matrix strictly
  exceeds the 97.5th percentile of max-H_1-persistence under the null.
- **SIGNIFICANT LOOPS**: enumerate the top-3 H_1 features by persistence
  and record the surah-label composition of a representative cycle
  (shortest cycle in the 1-skeleton at birth-ε). This is DESCRIPTIVE and
  does not affect the primary inference; it is the *interpretable
  content* if primary passes.
- **BOTH PASS** → there is genuine cyclic structure in surah-space
  BEYOND the known 114-Hamiltonian-cycle. Pre-registered interpretation:
  sub-rings within the architecture. Queue for [[h-new-187-lempel-ziv|H-NEW-187]] (independent
  feature-space replication on char-4-gram D-matrix from [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]).
- **PRIMARY 1 PASSES ONLY** (count excess, not max-persistence) → weak
  loop-richness signal; many small holes, no single dominant sub-ring.
- **PRIMARY 2 PASSES ONLY** (max-persistence excess, not count excess)
  → one dominant sub-ring amid sparse other loops.
- **BOTH NULL** → NULL: no sub-ring architecture beyond the known
  whole-mushaf cycle. Publish as such; earlier T5 null replicates.

## Garden of forking paths

- **ε grid**: {0.05, 0.10, …, 3.00}. Alternatives rejected pre-result:
  adaptive grid, percentile-based grid. Step 0.05 chosen to match the
  task-spec 0.1-step grid as a 2× refinement.
- **Significance threshold for "significant loop" (0.3)**: task-spec.
  Alternatives rejected: 0.1 (too lax, picks up noise), 0.5 (too
  stringent for Fisher-Rao range). 0.3 ≈ 10% of max D-distance (π).
- **Null**: distance-shuffle (random assignment of distances to pairs,
  preserving the multiset). Rejected: Gaussian random D-matrix
  (different multiset → confounded); label permutation on symmetric
  matrix (no-op, discussed above).
- **H_1 algorithm**: incremental reduction with triangles. Rejected:
  Čech complex (computationally harder), alpha complex (requires
  embedding, D-matrix is not directly embeddable in R^n without MDS),
  sparse Rips (approximate). The VR filtration on the raw D-matrix is
  the canonical choice.
- **Null budget**: full-H_1 on 200 permutations (q975 = 97.5th
  percentile on 200 samples has Monte-Carlo SE ≈ 1.1% — sufficient for
  α=0.025 discrimination when the effect sign is clear). Alternatives
  rejected: 10K full-H_1 perms (infeasible, ~30h runtime);
  10K cycle-rank-proxy-only (weaker null match); 1000 full-H_1 perms
  (~3.5h, marginally feasible). Task-spec asked for 10K but full-H_1
  triangle enumeration + GF(2) reduction on 114 points makes 10K
  infeasible. Budget pre-locked at 200 full-H_1 perms, with cycle-rank
  proxy on all 10K as a supplementary null consistency check.
- **MW-5 synthetic controls**: 3-cluster 2D + 30-point circle. Locked
  before real run.
- **Seed**: 20260419 (task-spec, next seed after [[h-new-111-fisher-rao-mushaf|H-NEW-111]] series).

## Failure modes

- H_0 MW-5 fails (not 3 persistent components on 3-cluster data) →
  INSTRUMENT-BROKEN for H_0, report as such.
- H_1 MW-5 fails (no persistent H_1 on the circle) → INSTRUMENT-BROKEN
  for H_1; fall back to cycle-rank proxy only.
- H_1 triangle enumeration infeasible for 114 points (243K triangles,
  should be fine) → fall back to cycle-rank proxy.
- Null multiset-preserving shuffle accidentally produces something
  non-symmetric → raise, abort, report bug.

## Deliverables

1. Pre-reg (this file).
2. Script `scripts/h_new_186_tda_persistent_homology.py` (seed 20260419).
3. JSON `findings/phase-b-hypotheses/csv/h-new-186.json` with:
   - persistence diagram (list of (birth, death, dim) triples),
   - β_0(ε) and β_1(ε) curves on real and null summary,
   - p-values for primary 1 and primary 2,
   - top-3 H_1 cycle representatives (surah labels).
4. Findings `findings/phase-b-hypotheses/h-new-186-tda-persistent-homology.md`.
5. Journal `journal/h-new-186-run-1.md`.
