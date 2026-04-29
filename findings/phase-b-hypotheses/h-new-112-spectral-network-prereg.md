---
id: H-NEW-112
title: Spectral graph-theoretic analysis of the H-NEW-89 meta-cluster incidence network
phase: B
status: PRE-REGISTERED 2026-04-17
spec_locked_at: 2026-04-17 (BEFORE running spectral computation)
agent: h-new-112-specialist
parent_findings:
  - H-NEW-89 (meta-cluster network — degree-based analysis; Q 62 degree-4 hub)
  - cross-finding-009 (meta-cluster network synthesis)
bonferroni_family: h-new-112-spectral-analysis
bonferroni_k: 2
alpha_bon: 0.025
amendment_audit_035: "C3 demoted to descriptive-only per audit-035; an algorithmic threshold (≥3 communities) is not a hypothesis test. Bonferroni-2 tightening self-verifies (per project rule feedback_bonferroni_tightening_vs_loosening)."
direction_primary: spectral gap > random-ER with matched edge-count at permutation p<0.025
direction_secondary_fiedler: sign-partition of v_2 correlates with at least ONE known classification at χ² p<0.025
descriptive_communities: number of spectral communities via eigengap heuristic (DESCRIPTIVE; not Bonferroni-counted)
seed: 20260417
n_perm: 10000
rules_tuple: (no-tashkeel; 114-node surah graph; surah-surah adjacency A = M·Mᵀ from H-NEW-89 incidence; weighted by shared-cluster count; self-loops removed; disconnected/isolate nodes attached via ε=1e-9 regularizer for L_norm well-definition)
---

# [[h-new-112-spectral-network|H-NEW-112]] — Spectral Graph-Theoretic Analysis of the Meta-Cluster Network (Pre-Registration)

## Question

[[h-new-89-meta-cluster-network|H-NEW-89]] built a bipartite (114 surah × 11 cluster) incidence matrix M and reported
degree statistics on its unipartite projection. That is a vertex-local, first-order description.

Spectral graph theory reveals ALGEBRAIC INVARIANTS not visible in degree statistics:

1. The **algebraic connectivity** λ₂ (Fiedler value) — quantifies global connectedness
2. The **spectral gap** λ_{k+1} − λ_k — distinguishes tight-community networks from random
3. The **Fiedler vector** v₂ — reveals natural bipartition structure
4. Higher eigenvectors — enable spectral community detection (k-means on top-k eigenvectors)

These are FUNCTIONAL INVARIANTS — they do not change under edge permutation within cluster-systems
but DO change drastically under random-graph nulls. If the meta-cluster network has genuine
architecture, spectral quantities should deviate significantly from random-graph expectations.

## Data source

- [[h-new-89-meta-cluster-network|H-NEW-89]] incidence matrix M (114 × 11) reconstructed from the locked cluster list in
  `findings/phase-b-hypotheses/csv/h-new-89.json` / `scripts/h_new_89_meta_cluster_network.py`.
- The 11 cluster systems and their memberships are LOCKED from [[h-new-89-meta-cluster-network|H-NEW-89]] and MUST NOT be altered.

## Locked construction (fixed before computation)

### Step 1 — Incidence matrix M
`M[s, c] = 1` if surah s ∈ cluster c, else 0. Dimensions: 114 × 11.

### Step 2 — Surah-surah weighted adjacency
`A = M · Mᵀ` (114 × 114). `A[s, t]` = number of clusters shared by surahs s and t.
**Remove self-loops**: set diagonal to 0. Keep WEIGHTED (do not threshold).

### Step 3 — Degree matrix and Laplacians
- Degree: `d[s] = Σ_t A[s, t]` (weighted degree)
- Combinatorial Laplacian: `L = D − A`
- Normalized Laplacian: `L_norm = I − D^(−1/2) A D^(−1/2)` with regularization
  `d_eff[s] = max(d[s], ε)` for ε = 1e−9 to handle isolate nodes (degree 0).
  Isolate nodes remain isolated in the spectrum (they contribute eigenvalue ≈ 1 in L_norm's
  canonical form; we track this and report).

### Step 4 — Eigendecomposition
Compute full spectrum {λ_1, ..., λ_114} of L_norm (sorted ascending) and eigenvectors
{v_1, ..., v_114}. λ_1 should equal 0 for the lone connected component; λ_1 ≈ 0 repeated
for each connected component (including isolates).

### Step 5 — Primary statistic: spectral gap
- **k = 3** is the locked community count (matches primary direction hypothesis:
  muqaṭṭāʿat / musabbiḥāt-Khawātim / mufaṣṣal-rest).
- Spectral gap := λ_{k+1} − λ_k = λ_4 − λ_3 in L_norm
- Null: Erdős-Rényi G(n=114, m=E) with matched edge count E (and weight-matched
  via edge-weight permutation — MW-1: degree-distribution-matched via configuration-model
  secondary null).
- One-sided direction: observed gap > null gap

### Step 6 — Secondary: Fiedler vector v_2
- v_2 sign partition: P_+ = {s : v_2[s] > 0}, P_− = {s : v_2[s] < 0}
- Test against 3 known binary classifications:
  - Meccan vs Medinan (from quran-no-tashkeel.json `type` field)
  - muqaṭṭāʿat-opened vs not (29 muqaṭṭāʿat surahs)
  - long vs short (median split of verse count: 114 surahs split at median)
- χ² test of independence between v_2 sign and each classification (2×2 table).
- PASS-secondary-fiedler if AT LEAST ONE of the three χ² tests passes p < α_bon = 0.0167.

### Step 7 — Secondary: spectral community detection
- Normalized spectral clustering: k-means on the rows of the matrix of top-k eigenvectors
  [v_2, v_3, ..., v_{k+1}] with k estimated by the eigengap heuristic (largest gap among
  λ_2..λ_10).
- Report: number of communities, community assignments, community bridge-surahs
  (surahs with highest participation in multiple communities by normalized spectral embedding).
- PASS-secondary-communities if k_eigengap ≥ 3.

## Locked metrics (inferential cells)

**AMENDMENT (audit-035, 2026-04-17)**: C3 demoted to DESCRIPTIVE-ONLY per audit-035's
MW-2 / Bonferroni-asymmetry rule. An algorithmic threshold ("≥3 communities") is not a
hypothesis test — it is a descriptor. The community-count output is reported descriptively
in the findings but NOT counted in the Bonferroni family. This is TIGHTENING (Bonferroni-2
instead of Bonferroni-3, α_bon strengthened from 0.0167 to 0.025 for the remaining 2
inferential cells). Tightening self-verifies per project rule.

| Cell | Name | Test | Direction | Bonferroni |
|---|---|---|---|---|
| **C1** | Spectral gap primary | λ_4 − λ_3 vs ER(n=114, m=E) null | observed > null (one-sided upper) | α_bon = 0.025 |
| **C2** | Fiedler sign-partition | χ² vs known binary labels (Meccan/Medinan, muqaṭṭāʿat, long/short) | AT LEAST ONE χ² < α_bon | α_bon = 0.025 |
| ~~C3~~ | Community count (k_eigengap) | **DEMOTED to descriptive** | reported descriptively | not counted |

**Family**: [[h-new-112-spectral-network|h-new-112]]-spectral-analysis; k=2 (after audit-035 tightening); α_bon = 0.05 / 2 = 0.025.

**PASS criterion**: ≥ 2 of 2 inferential cells pass at α_bon (i.e., both C1 AND C2 must pass for PASS).
MARGINAL: 1 of 2 cells pass. NULL: 0 of 2 cells pass.

## Null models (MW-1: match edge-count AND degree-distribution)

Primary null for C1:
- **ER(n=114, m=E_obs)**: edge-count-matched Erdős-Rényi. 10,000 draws.
- Edges drawn uniformly from the (114 choose 2) pair set without replacement.
- Weights redistributed from observed weight-multiset (weight-matched permutation).

Secondary null for C1 (robustness):
- **Configuration-model**: degree-preserving rewiring. Preserves each surah's weighted
  degree. Uses edge-swap algorithm with 10·E swaps.
- **Barabási-Albert scale-free**: m_attach = round(E / n). Tests whether spectral gap
  is distinguishable from preferential-attachment networks.
- **Stochastic-block-model** with 3 planted blocks of size {29, 9, 76} (muqaṭṭāʿat /
  musabbiḥāt+Friday+Khawātim union / rest). Tests whether the observed gap is larger
  than a planted-3-block model — a sharper benchmark.

Report: (observed_gap, ER_p, CM_p, BA_p, SBM_p) with primary C1 decision on ER p.

## MW-5 positive control

Before testing observed data: run the full pipeline on a **synthetic planted-3-block
network** with 114 nodes partitioned as {38, 38, 38} in 3 equal blocks, intra-block
edge probability p_in = 0.3, inter-block p_out = 0.02. Expected: C1 and C3 must FIRE
strongly (spectral gap >> ER null; k_eigengap = 3). If positive control fails, the
pipeline is broken and the observed result is discarded (GATE).

## Q 62 saddle/peak test (secondary-descriptive, not Bonferroni-counted)

Per the task motivation, locate Q 62 al-Jumuʿah's position in the sorted Fiedler vector
v_2 and in the top-k spectral embedding. Report:
- v_2[Q62] value and rank among 114 surahs
- Local neighborhood: v_2 values of Q 62's A-neighbors
- Is Q 62 at an eigenvector saddle (neighbors have OPPOSITE signs) or peak (same sign
  with Q 62 extreme)? Saddle = bridge role; peak = community-central role.

## Anti-HARK pre-commitments

- All 3 cells reported regardless of significance.
- Full spectrum + Fiedler vector + community assignments dumped to JSON.
- Q 62 descriptive stats reported whatever the spectral outcome.
- If positive control MW-5 fails: HARD FAIL, do not report observed.
- If primary C1 passes but MW-5 passes: legitimate PASS on C1.
- NULL PASS (0 of 3 cells): publish with equal prominence; do NOT retry with different k.
- Garden-of-forking-paths log (below) captures all branchings I considered BEFORE viewing data.

## Garden-of-forking-paths (locked before run)

Choices fixed BEFORE seeing spectral numbers:

1. **Weighted adjacency A = M·Mᵀ** (not unweighted threshold): the cluster-share count
   IS the natural cluster-network weight. Thresholding loses information.
2. **Normalized Laplacian L_norm = I − D^(−1/2)AD^(−1/2)**: standard in spectral clustering
   literature (Ng-Jordan-Weiss 2001). Combinatorial L is reported auxiliary only.
3. **k = 3 locked for primary gap**: corresponds to the 3 plausible communities
   (muqaṭṭāʿat-front / musabbiḥāt+Friday+Khawātim-back / mufaṣṣal-rest) per [[h-new-89-meta-cluster-network|H-NEW-89]]
   qualitative synthesis. Not optimized post-hoc.
4. **ε = 1e−9 regularizer for isolate degrees**: ensures L_norm is well-defined with
   isolates. Alternative (dropping isolates from graph) would change spectrum length.
   We KEEP isolates for comparability to [[h-new-89-meta-cluster-network|H-NEW-89]]'s 114-surah frame.
5. **ER edge-count matched** as primary null (not edge-density matched with weights dropped):
   preserves stochastic structure. Weight-matched permutation handles weight component
   separately (principled decomposition).
6. **Eigengap heuristic for community count k_eigengap**: standard in spectral clustering;
   alternative = silhouette score or modularity optimization. Eigengap is ALGEBRAIC
   (matches the spectral-theoretic framing); modularity is DIFFERENT family.
7. **3 known binary classifications for Fiedler** (Meccan/Medinan, muqaṭṭāʿat, long/short):
   chosen BEFORE data view as the canonical 3 known partitions. "Surah type" (Meccan/
   Medinan) is most stable; muqaṭṭāʿat is the project's strongest structural axis;
   long/short tests length-bias.
8. **Median split for long/short**: not 25th/75th percentile. Median is the natural
   binary split for "long vs short".
9. **Isolates contribute λ=1 eigenvalues in L_norm**: this is a known artifact of the
   normalization. We track the number of isolates (21 per [[h-new-89-meta-cluster-network|H-NEW-89]]) and expect ~21
   eigenvalues near 1 in the spectrum. This is NOT pathology; it's the algebra.
10. **Full spectrum + Fiedler vector dumped to JSON**: even if analysis is null,
    downstream work can reuse the spectrum.

## Cross-cutting predictions (pre-view)

- **Prior 1**: Spectral gap will PASS ER null. Argument: [[h-new-89-meta-cluster-network|H-NEW-89]] already shows
  cluster-contiguity generates non-random structure; spectral gap should reflect this.
- **Prior 2**: Fiedler bipartition MAY align with front-back hub axis (Q 2-3 front
  pair vs Q 59-62 back pair per [[h-new-89-meta-cluster-network|H-NEW-89]]). This is a content prediction, not a
  Bonferroni-protected claim.
- **Prior 3**: Community count ≥ 3 is LIKELY given the 11-cluster design; primary
  communities expected are (a) muqaṭṭāʿat الم+الر+ḥm+طسم union (front-middle), (b)
  musabbiḥāt+Friday+Khawātim+Muʿawwidhatān union (back), (c) mufaṣṣal-only rest, +
  21 isolates as a degenerate 4th "non-community".
- **Prior 4**: Q 62 will be a SADDLE in v_2 (degree-4 hub = structural bridge). If
  Q 62 is a PEAK, it means Q 62 is CENTRAL to one community; if SADDLE, Q 62 bridges
  multiple communities.

These priors are disclosed for transparency; they do NOT constitute post-hoc bias.

## Files produced

- Pre-reg: `findings/phase-b-hypotheses/h-new-112-spectral-network-prereg.md` (this file)
- Script: `scripts/h_new_112_spectral_network.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-112.json` (full spectrum + Fiedler + communities)
- Findings: `findings/phase-b-hypotheses/h-new-112-spectral-network.md`
- Journal: `journal/h-new-112-run-1.md`

## Status
PRE-REGISTERED 2026-04-17 BEFORE script execution. Seed 20260417 locked.
