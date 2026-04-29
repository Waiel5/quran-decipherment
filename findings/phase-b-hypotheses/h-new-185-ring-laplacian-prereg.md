---
finding_id: h-new-185
title: "Spectral graph Laplacian analysis of the mushaf ring"
specialist: h-new-185-specialist
date_prereg: 2026-04-17
seed: 20260419
bonferroni_k: 2
bonferroni_family: h-new-185-ring-laplacian
alpha_bon: 0.025
alpha_raw: 0.05
parent_findings:
  - cross-finding-013 (mushaf = structured Hamiltonian cycle, CONFIRMED)
  - H-NEW-111 (Fisher-Rao distance matrix D source, CONFIRMED via H-NEW-111b)
rules_tuple: "(no-tashkeel, QAC-STEM root tokens K=500, QAC v0.4, Dirichlet-0.5, L1-norm, mushaf ring topology, Hafs-Kufan, Fisher-Rao angular distance)"
perms: 10000
verdict_ceiling: "PASS (not CONFIRMED; requires replication on char-4-gram feature space before CONFIRMED)"
---

# [[h-new-185-ring-laplacian|H-NEW-185]] — Spectral graph Laplacian analysis of the mushaf ring

## Motivation

[[cross-finding-013-mushaf-topological-ring|cross-finding-013]] CONFIRMED that the canonical 114-surah mushaf is a
structured Hamiltonian cycle in Fisher-Rao content space (Principle M1).
This pre-registered test probes the **spectral properties** of the
implied ring graph, asking two questions that a Hamiltonian cycle per se
does not determine:

1. **Fiedler partition (λ_1 eigenvector)**: does the ring decompose into
   two content-coherent communities whose boundary aligns with a known
   mushaf axis (e.g., muq-opening / non-muq, or long-form / short-form,
   or front-half / back-half at the Q 50 pivot documented in
   [[cross-finding-019-q50-qaf-composite-hub-exemplar|cross-finding-019]])?
2. **Spectral gap (λ_2 − λ_1)**: is the community structure unusually
   tight compared to what would be expected from a random Hamiltonian
   cycle with the same edge-weight distribution?

A ring-graph with uniformly random edge weights has a predictable
low-frequency spectrum (Fiedler ≈ sinusoid around the cycle; gap
determined by edge-weight variance). The mushaf's observed
Fisher-Rao edge weights may yield a spectrum that is EITHER typical
of a random-weighted cycle (null) OR unusually structured (signal
for additional global organization beyond the Hamiltonian-cycle
geodesic property).

## Hypothesis

**Primary 1 (H1a — Fiedler partition alignment)**: The sign of the
Fiedler-vector (eigenvector of λ_1 of the normalized Laplacian of the
weighted mushaf ring) PARTITIONS the 114 surahs into two contiguous
arcs of the cycle whose partition-point(s) align with a pre-specified
axis at p < 0.025 (Bonferroni-adjusted). The pre-specified alignment
axes (one of the following; chosen by PRE-REG WITHOUT looking at data):

- Axis A: the Q 50 mid-mushaf pivot documented in CF-019. Alignment
  ≡ the sign-flip boundary within 5 surahs of Q 50.
- Axis B: long-form / short-form split, equivalent to the surah-length
  median. Alignment ≡ the sign-flip coincides within 5 rank-positions
  of the length-median boundary.

**Locked axis choice before computation: AXIS A** (Q 50 mid-mushaf
pivot). Justification: CF-019 Q 50 has been independently identified
as the mushaf's structural pivot; we predict the Fiedler partition
crosses near this pivot because the ring's content-geometric balance
point is the same point.

**Primary 2 (H1b — Spectral gap signal)**: The spectral gap
Δ = λ_2 − λ_1 of the mushaf ring Laplacian is LARGER than the 97.5%-
ile of Δ values over 10,000 random Hamiltonian cycles constructed by
randomly permuting the 114 surah-ID-to-ring-position assignment (i.e.,
re-wiring the consecutive edges while preserving the unweighted ring
structure). One-sided upper-tail test.

Interpretation: a large Δ means the Fiedler partition is a DOMINANT
mode of the graph — the two communities are tightly defined and
further subdivision (λ_2) is much costlier. A small Δ means
community structure is diffuse.

## Method (locked before results viewed)

### Graph construction

- Nodes: V = {1, 2, ..., 114} (mushaf surah IDs).
- Edges: E = {(i, i+1) : i = 1..113} ∪ {(114, 1)}  — 114 edges,
  pure 2-regular cycle.
- Edge weights: w(i, j) = d_FR(S_i, S_j), the Fisher-Rao angular
  distance from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s D matrix (K_top=500 roots,
  Dirichlet α=0.5, L1-normalized).
- Edge "affinity" for Laplacian: A_ij = 1 / (w_ij + ε) with
  ε = 1e-6, so closer surahs (smaller FR distance) have LARGER
  affinity. This is the standard conversion from a distance
  matrix to a graph Laplacian affinity.

### Laplacian

- Degree d_i = Σ_j A_ij (only two non-zero terms per node: ring
  neighbors).
- Unnormalized: L = D_diag − A.
- Normalized (LOCKED): L_sym = D^(-1/2) (D_diag − A) D^(-1/2).

### Spectrum

- Compute all 114 eigenvalues and eigenvectors of L_sym using
  `scipy.linalg.eigh` (symmetric solver).
- Sort ascending: λ_0 = 0 ≤ λ_1 ≤ λ_2 ≤ ... ≤ λ_113.
- Fiedler vector v_1 = eigenvector of λ_1. Fiedler sign-partition:
  { i : v_1[i] > 0 } vs { i : v_1[i] < 0 }.

### Tests

**H1a (Fiedler alignment to Axis A)**:
- Define the sign-boundary(ies) of v_1 around the ring. For a ring,
  Fiedler sign flips at 2 points (two arcs). Identify both
  sign-flip positions along the ordered ring (1 → 2 → ... → 114 → 1).
- PASS iff one of the two sign-flip positions lies within ±5 ring
  positions of surah 50 (so position ∈ {45, 46, ..., 55}).
- Null: under random edge-weight re-wiring (10,000 perms, seed
  20260419), compute the empirical distribution of distance from
  Q 50 to nearest sign-flip. p = fraction of perms with distance
  ≤ observed.
- Bonferroni α_bon = 0.025 (k=2).

**H1b (Spectral gap)**:
- Observed Δ = λ_2 − λ_1.
- Null: for each of 10,000 random perms, build L_sym with the SAME
  edge weight set but re-assigned to random ring positions; compute
  Δ_null.
- p = (# perms with Δ_null ≥ Δ_obs + 1) / (10,001).
- Bonferroni α_bon = 0.025.

### Descriptives (not part of primary tests)

- λ_1, λ_2, λ_3, and the top-3 eigenvalue sequence.
- Top-10 surahs by eigenvector centrality in the λ_2 eigenspace
  (abs(v_2)). Descriptive only — surfaces structural-hub candidates.
- Top-10 surahs by absolute Fiedler value (hubs of each community).
- Identification of the 2 sign-flip arcs (start position, end
  position, arc length).

### Garden-of-forking-paths log

All of the following were LOCKED before any computation:
1. Affinity = 1/(w+ε), ε=1e-6. (Not heat-kernel or Gaussian
   affinity; those add a bandwidth hyperparameter σ.)
2. Laplacian = normalized symmetric (L_sym), not random-walk
   (L_rw) or unnormalized.
3. Null model = random re-wiring of edge weights to ring
   positions (preserves edge-weight MULTISET; tests whether the
   SPECIFIC assignment to ring positions matters).
4. Axis choice: AXIS A (Q 50 pivot). ±5 tolerance.
5. Bonferroni k=2 (H1a + H1b).
6. Seed 20260419 for re-wiring permutations.
7. Only eigenvalues/eigenvectors from `scipy.linalg.eigh`; if
   numerical issues arise, switch to `np.linalg.eigh` (documented
   fallback).

### Verdict mapping

| Outcome (H1a) | Outcome (H1b) | Verdict |
|:---|:---|:---|
| p < 0.025 | p < 0.025 | PASS-DIRECTED (upgrade ceiling to CONFIRMED requires char-4-gram replication) |
| p < 0.025 | p ≥ 0.025 | WEAK-PASS (Fiedler-axis only) |
| p ≥ 0.025 | p < 0.025 | WEAK-PASS (gap only) |
| p ≥ 0.025 | p ≥ 0.025 | NULL |

MW-1 (length control): already achieved at parent [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (L1
normalization of root distributions). No new length control needed.

MW-5 (positive control): the unweighted 114-cycle has a known
Fiedler vector = cosine around the ring, λ_1 = 2(1 − cos(2π/114))
≈ 0.00304. We verify the weighted-graph's λ_0 = 0 (sanity) before
running the primary tests.

## Data sources

- D matrix: `findings/phase-b-hypotheses/csv/h-new-111.json` field
  `D_matrix_upper_triangular`.
- CF-019 pivot: Q 50 mid-mushaf pivot (from [[cross-finding-019-q50-qaf-composite-hub-exemplar|cross-finding-019]]).

## Output

- `findings/phase-b-hypotheses/csv/h-new-185.json`: λ spectrum,
  Fiedler vector, sign-flip positions, null distribution summaries,
  p-values, top-centrality surahs.
- `findings/phase-b-hypotheses/h-new-185-ring-laplacian.md`:
  write-up.
