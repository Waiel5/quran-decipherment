---
finding_id: h-new-111
title: "Fisher-Rao information-geodesic test of mushaf order"
specialist: h-new-111-specialist
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 3
bonferroni_family: h-new-111-fisher-rao-mushaf
alpha_bon: 0.0167
alpha_raw: 0.05
direction_primary: "L_mushaf < L_random at permutation p < 0.0167 (one-sided lower-tail)"
direction_secondary_ratio: "L_mushaf / L_min < 2.0 is 'geodesic-like' (descriptive)"
direction_secondary_nold: "Nöldeke path length vs mushaf path length (two-sided exploratory)"
K_top_roots: 500
dirichlet_alpha: 0.5
length_control: "MW-1 via L1-normalization of per-surah distributions (each p_i sums to 1 regardless of surah length)"
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)"
perms: 10000
verdict_ceiling: "PASS (not CONFIRMED until independent replication on a distinct feature set)"
---

# [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Fisher-Rao information-geodesic test of mushaf order

## Motivation

The Quran's mushaf ordering is known not to be chronological (Nöldeke, classical
chronologies diverge from it, see [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] and [[h-new-51-1-noldeke-replication|H-NEW-51.1]]). If the mushaf
ordering is not random, what criterion could it be optimizing? This
pre-registered test asks whether CONSECUTIVE surahs in the mushaf tend to be
closer in the information-geometric sense (Fisher-Rao distance on the simplex
of per-surah root distributions) than random re-orderings would predict.

The test is **information-geometric**, not lexical: it uses the Fisher-Rao
metric on the probability simplex, which is the unique (up to scale)
Riemannian metric invariant under sufficient statistics (Čencov 1982).
For discrete distributions it reduces to the angular (Bhattacharyya /
Hellinger-angle) distance:

    D_FR(p, q) = 2 · arccos( Σ_k sqrt(p_k · q_k) )

This is bounded in [0, π] and is a true metric on the simplex.

## Hypothesis

**Primary (H1)**: The total Fisher-Rao path-length over the mushaf order,
`L_mushaf = Σ_{i=1..113} D_FR(p_i, p_{i+1})`, is SHORTER than would be
expected under a uniform random permutation of the 114 surahs. One-sided
lower-tail test.

**Secondary A (descriptive ratio)**: `L_mushaf / L_min < 2.0`, where `L_min`
is the TSP-optimal (or strong approximation) path length on the same 114
distributions. A ratio near 1 means the mushaf is geodesically near-optimal;
a ratio near 2 means it's "geodesic-like"; much larger means it's far from
geodesic.

**Secondary B (two-sided exploratory)**: Is the Nöldeke chronological path
length `L_nold` SHORTER or LONGER than `L_mushaf`? If shorter, the Quran's
chronological reception order is more information-geometrically coherent than
its canonical order. If longer, the canonical order is MORE coherent than
chronology — a non-trivial finding given the chronological order is generally
taken as the "natural" one in historical-critical scholarship.

## Method (locked before results viewed)

### Data

- Corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
  (no-tashkeel Hafs-Kūfan, 114 surahs, 6,236 verses).
- Root tokens: QAC v0.4 STEM segments (same root-token convention as
  [[h-new-91-rare-root-density|H-NEW-91]]). Source: `data/morphology/quranic-corpus-morphology-0.4.txt`.
- Chronology: `data/revelation-order.csv` (Tanzil Egyptian Standard +
  Wikipedia Nöldeke merge; 114 rows with `noldeke_order`).

### Feature space

- **K = 500** top roots (by global QAC-STEM frequency). LOCKED before
  computation. No post-hoc K tuning.
- Each surah i gets a raw count vector c_i over those 500 roots (counting
  only STEM-segment root attributions; non-root tokens are NOT counted in
  the denominator).
- Dirichlet smoothing with **α = 0.5** (Jeffreys prior) added to every
  count cell, THEN L1-normalized to get a probability vector p_i on the
  500-simplex. This handles zero probabilities and implements the MW-1
  length control (normalization removes surah-length scale; only the
  distribution shape remains).

### Distance

Fisher-Rao angular distance:

    D[i,j] = 2 · arccos( Σ_k sqrt(p_i[k] · p_j[k]) )

Clipped to [0, π]. Symmetric, zero on diagonal.

### Primary test

- `L_mushaf = Σ_{i=1..113} D[i, i+1]` (consecutive-surah distances along
  mushaf order).
- **Null**: 10,000 uniformly random permutations of the 114 surahs,
  recompute `L_perm = Σ D[π(i), π(i+1)]`.
- `p_primary = (#{L_perm ≤ L_mushaf} + 1) / (PERMS + 1)` (one-sided,
  lower-tail; +1 conservatism).

### Secondary A: geodesic-optimality ratio

- Compute `L_min` via greedy nearest-neighbor from each of the 114 possible
  start-surahs, then 2-opt local improvement on the best. This is NOT
  guaranteed optimal TSP on 114 nodes, but produces a tight upper bound
  on the optimum. Report both `L_greedy_best` and `L_2opt`.
- Ratio `L_mushaf / L_2opt` descriptive; no formal test.

### Secondary B: Nöldeke vs mushaf

- Build the Nöldeke permutation σ (1..114 by `noldeke_order`).
- `L_nold = Σ D[σ(i), σ(i+1)]`.
- Compare `L_nold` to the SAME 10,000-permutation null.
- `p_nold = 2 · min(#{L_perm ≤ L_nold}, #{L_perm ≥ L_nold}) / PERMS` (two-sided).
- Also report sign of `L_mushaf - L_nold`.

### MW-5 positive control

A synthetic ordering constructed by greedy-nearest-neighbor from surah 1
should fire as p < 0.001 under the same null. If it does not, the null
is BROKEN (instrument failure) and the primary result is inadmissible.

### MW-1 length residualization

Built into the method: each p_i is L1-normalized so its entries sum to 1.
Total surah length drops out of the distance. A long surah and a short surah
with the same ROOT-PROPORTIONS will have D = 0.

## Pre-committed acceptance window

- **PRIMARY PASS**: `p_primary < 0.0167` (Bonferroni 3 family).
- **SECONDARY A**: ratio `L_mushaf / L_2opt < 2.0` reported as "geodesic-like";
  `< 1.2` as "near-optimal"; else "not geodesic-like".
- **SECONDARY B**: `p_nold < 0.0167` fires as "chronology path also short";
  additionally report the sign `L_mushaf < L_nold` (mushaf shorter than
  chronology — unexpected) vs `L_mushaf > L_nold` (chronology shorter —
  consistent with the "chronology was the original order" hypothesis).

## Garden of forking paths

- This is a **NEW test**. No prior-finding anchor exists. I am not
  eyeballing results before locking the method.
- K = 500 is the team-lead recommendation; I am accepting it as-is.
  Alternatives considered and REJECTED pre-result: K ∈ {100, 250, 1000}.
- Dirichlet α = 0.5 (Jeffreys) is the team-lead recommendation; accepted.
  Alternatives rejected pre-result: no-smoothing (creates NaN in log),
  α = 1 (uniform, heavier smoothing), tf-idf reweighting.
- Distance choice: Fisher-Rao angular = Bhattacharyya arccos. This IS the
  team-lead spec. Alternatives rejected pre-result: Hellinger (L2 on
  sqrt-probs, equivalent up to monotone transform so would give same
  primary p-value), KL-divergence (asymmetric, not a metric), Jensen-Shannon
  (metric but not Fisher-Rao).
- Null model: uniform random permutation of 114 surahs. Alternative
  rejected: length-stratified permutation — but MW-1 normalization already
  removes length, so uniform perm is the right null.
- TSP algorithm: 114 nodes is solvable optimally with Held-Karp in 2^114
  which is intractable; exact TSP on 114 nodes requires Concorde or
  similar (not available here). I am using greedy-NN + 2-opt, which gives
  a tight UPPER bound on `L_min`. Therefore `L_mushaf / L_2opt` is an
  UPPER BOUND on the true ratio, so if it passes "near-optimal" it is
  a fortiori true of the real optimum.

## Failure modes and how they would be reported

- Positive control fails → report INSTRUMENT BROKEN, primary result held in
  abeyance.
- Primary p ≥ 0.0167 → **NULL**: mushaf order is NOT information-
  geometrically optimized under this metric; publish with equal prominence.
- Primary passes but ratio ≥ 2.0 → mushaf is SHORTER-than-random but still
  far from optimal; "locally coherent but not globally geodesic".
- Nöldeke two-sided p passes AND `L_nold < L_mushaf` → chronology is MORE
  coherent than mushaf; striking finding, queue for [[h-new-112-spectral-network|H-NEW-112]] independent
  replication.
- Nöldeke two-sided p passes AND `L_nold > L_mushaf` → mushaf is MORE
  coherent than chronology; supports the theological "ordered at
  revelation-end" tradition.

## Deliverables

1. Pre-reg (this file).
2. Script `scripts/h_new_111_fisher_rao_mushaf.py` (seed 20260417,
   deterministic).
3. JSON `findings/phase-b-hypotheses/csv/h-new-111.json` with D-matrix
   (flattened), L_mushaf, L_random quantiles, L_min estimates, p-values.
4. Findings `findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf.md`.
5. Journal `journal/h-new-111-run-1.md`.
