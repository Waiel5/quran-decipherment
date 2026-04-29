---
finding_id: h-new-131.1
title: "Length-normalized MST — continuous trace of Q 108 centrality vs Dirichlet α (and a length-residualization variant)"
specialist: specialist-B (quran-equation-solvers)
date_prereg: 2026-04-17
seed: 20260417
parent_finding: h-new-131
parent_data: findings/phase-b-hypotheses/csv/h-new-131.json
grandparent: h-new-134 (MST super-hub observation); h-new-111 (Fisher-Rao D-matrix source)
bonferroni_k: 2
bonferroni_family: h-new-131-1-length-normalization
alpha_bon: 0.025
alpha_raw: 0.05
rules_tuple: "(114 surahs Hafs-Kūfan; K=500 top QAC-STEM roots; Fisher-Rao arccos-Bhattacharyya; MST via Kruskal; no-tashkeel; QAC v0.4)"
pre_reg_standard: PRE-REG-STANDARD-04
---

# [[h-new-131-1-length-normalized-mst|H-NEW-131.1]] — Length-normalized MST: α-sweep + length-residualization

## Motivation

[[h-new-131-q108-supernode|H-NEW-131]] found that Q 108's MST-super-hub status (degree 24 at α=0.5) is
PARTLY mechanical (length-via-smoothing) and PARTLY structural. Cell A
showed Q 108 drops to degree 11 at α=0.01, and Q 7 / Q 2 take over as the
top hubs. Cell B showed that under total-variation (L1) the super-hub
collapses to degree 6.

Two questions remain:

1. **Continuous α-trace**: Between α=0.5 and α=0.01, how does Q 108's
   degree actually transition? Is it monotone, sharp, or oscillatory?
   Where does the smoothing/structural crossover sit?

2. **Explicit length-residualization**: The α-sweep varies smoothing,
   which is *one* form of length confound. An alternative is to
   length-normalize the raw counts directly (e.g., divide by total
   tokens) BEFORE smoothing, so that per-surah token-count has
   structurally no effect on the distribution shape. Does this give a
   different answer from the α-sweep?

## Design

### Cell A — continuous α-sweep (PRIMARY 1 of 2)

Seven α values pre-committed: α ∈ {0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 2.0}.

For each α:
- Smooth-and-normalize raw counts → 114 probability distributions on K=500-simplex.
- Compute Fisher-Rao D-matrix (same formula as [[h-new-111-fisher-rao-mushaf|H-NEW-111]]).
- Compute MST via Kruskal.
- Record Q 108's degree, and degrees of all 114 surahs.
- Record top-5 MST-hubs by degree at each α.

**H_A_0 (null)**: Q 108's MST-degree does NOT exhibit monotone decrease
as α drops from 2.0 to 0.001.

**H_A_1 (structural-mechanism)**: Q 108's degree is a MONOTONIC function
of α (higher α → higher Q 108 degree), confirming the smoothing-dependence
quantified in [[h-new-131-q108-supernode|H-NEW-131]].

**Formal test — Spearman rank correlation** between α and Q 108's degree
across the 7 α values. Pass condition: ρ ≥ 0.8 with 1-sided p < 0.025 by
the Fisher-r-z approximation (α_bon=0.025 per Bonferroni-2 family). If the
degree sequence is monotone-non-decreasing, ρ = 1.0 exactly.

**Decision consequences**:
- Monotone (ρ=1, p<0.025): confirms smoothing-as-length-mechanism
  quantitatively. Q 108's degree is PREDICTABLE from α.
- Non-monotone: indicates structural component is more subtle than
  "smoothing makes Q 108 uniform-centroid". Report.

### Cell B — length-residualization via per-surah L1-count (PRIMARY 2 of 2)

The [[h-new-111-fisher-rao-mushaf|H-NEW-111]] / [[h-new-134-formal-prophet-named-signature|H-NEW-134]] pipeline already L1-normalizes AFTER smoothing.
But the smoothing uses a FLAT Dirichlet prior (same α on every cell for
every surah), so short surahs get MORE prior mass relative to their
token count than long surahs do. Length-residualization proper = make
the prior scale WITH the surah's own raw-token count.

Proposed residualization (pre-committed):

    prior_mass_per_cell(surah_i) = α_base × (mean_surah_tokens / surah_i_tokens)

where `α_base = 0.5` (baseline) and `mean_surah_tokens` is the across-
114-surah mean STEM-root-token count. This makes every surah's smoothed
distribution have the SAME ratio of prior-mass to real-count-mass —
eliminating the "Q 108's 7 tokens get swamped by prior" effect.

Alternative residualization considered and REJECTED pre-result:
- Per-surah multiplicative scaling after normalization (does not change
  simplex position; no effect on Fisher-Rao).
- Subtracting a uniform distribution with weight proportional to 1/length
  (unprincipled; would need arbitrary constant).
- Permuting short-surah labels (changes null model not estimate).

Under this length-residualized smoothing, build D-matrix, MST, record
Q 108's degree.

**H_B_0 (null)**: Under length-residualized smoothing, Q 108's MST-degree
differs from α=0.5 baseline (24) by ≥ 10 (i.e., drops to ≤ 14 or rises
to ≥ 34).

**H_B_1 (robustness)**: Q 108's MST-degree under length-residualized
smoothing is WITHIN 9 of baseline 24 (i.e., 15-33).

**Decision**: a degree in 15-33 → residualization PASSES (structural
signal robust to the length correction). A degree ≤ 14 or ≥ 34 → length
residualization MATERIALLY CHANGES the observation.

Bright-line decision; no p-value. This is a descriptive robustness check
on a descriptive quantity.

### Non-inferential exploratory reads (no Bonferroni slot)

- Cell C: degree distribution full histogram at each α (heavy-tailed vs
  exponential; just plotted).
- Cell D: identify Q 108's nearest neighbors at each α. Do they stay in
  the short-mufaṣṣal cluster (Q ≥ 78) or migrate elsewhere?
- Cell E: is the rank-order of the top-4 hubs ([[h-new-134-formal-prophet-named-signature|H-NEW-134]] at α=0.5:
  Q 108, Q 7, Q 112, Q 64) preserved across α, or does it reorganize?

## Bonferroni accounting

- Family = [[h-new-131-1-length-normalized-mst|h-new-131-1]]-length-normalization
- k = 2 inferential slots (Cell A Spearman-rank, Cell B degree-range)
- α_bon = 0.05 / 2 = 0.025
- Cells C/D/E are descriptive; no Bonferroni slot.

## Garden of forking paths

- **α set {0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 2.0}** chosen to
  log-symmetrically span four orders of magnitude centered on the
  baseline α=0.5. Alternatives considered and REJECTED pre-result:
  {0.1, 0.5, 1.0} (too coarse to trace transition), {α=0 exactly} (numerical
  divergence), arbitrary grid like {0.2, 0.4, 0.6, 0.8} (not symmetric).
- **Residualization formula** = `α_base × (mean/N_i)` chosen as the
  minimal-parameter length-inverse scaling that preserves the Jeffreys-
  prior intent. Alternatives REJECTED pre-result: multiplicative count
  rescaling (doesn't change simplex position), TF-IDF weighting (redefines
  feature space; requires separate pre-reg), empirical-Bayes
  hyperprior fit (over-flexible).
- **Spearman ρ ≥ 0.8 threshold**: corresponds to ρ for a 7-point sequence
  where one adjacent pair is inverted (which would still be monotone
  enough to support the claim). Alternatives REJECTED: ρ = 1.0 exact
  (too strict — would fail under any floating-point rounding), ρ ≥ 0.5
  (too weak — admits sequences with two inversions).
- **Cell B degree-range ±9**: chosen as the gap between Q 108's α=0.5
  degree (24) and the Cell A α=0.01 observation (11) → 13-gap. Setting
  ±9 requires Cell B to survive a correction that's at most 2/3 of the
  smoothing-α effect. Alternatives REJECTED: ±5 (too strict — virtually
  guarantees NULL given Cell A already showed 13-unit change), ±15 (too
  permissive — would admit near-total collapse).
- **Direction A is 1-sided** (higher α → higher degree) per [[h-new-131-q108-supernode|H-NEW-131]] Cell
  A observation and the uniform-centroid theoretical argument.

## MW-5 positive control

**Planted-hub synthetic control** (option requested by audit-036):

Before running Cells A and B, verify that the MST pipeline DETECTS a
planted hub. Procedure:

- Take the raw count matrix.
- Construct a synthetic 115th "surah" whose distribution is the EMPIRICAL
  AVERAGE of all 114 real surahs (i.e., perfect centroid). Assign it
  index 115.
- Rebuild 115×500 matrix; smooth with α=0.5; Fisher-Rao → 115×115 D; MST.
- EXPECTED: the synthetic centroid surah should have LARGE MST-degree
  (by construction, it's the nearest neighbor of many real surahs).

Pass condition: synthetic surah's MST-degree ≥ 20. Failure = pipeline
insensitive to genuine hubs, verdict INSTRUMENT-BROKEN, abeyance.

If MW-5 passes, proceed to Cells A / B. If it fails, no results reported.

## Deliverables

- Pre-reg (this file).
- Script: `scripts/h_new_131_1_alpha_sweep.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-131-1.json`
- Findings: `findings/phase-b-hypotheses/h-new-131-1-length-normalized-mst.md`
- Journal: `journal/h-new-131-1-run-1.md`

Null and pass published with equal prominence.

## Pre-committed verdict table

| Cell A (α-sweep Spearman) | Cell B (length-resid degree in 15-33) | MW-5 | Final verdict |
|---|---|---|---|
| PASS (ρ≥0.8, p<0.025) | PASS (15-33) | PASS (≥20) | STRUCTURAL-ROBUST + SMOOTHING-MONOTONE — structural signal survives length correction AND α-smoothing relationship is quantitatively confirmed |
| PASS | FAIL | PASS | SMOOTHING-MONOTONE + STRUCTURE-LENGTH-CONFOUND — Q 108 centrality tied to length |
| FAIL | PASS | PASS | STRUCTURAL-ROBUST + SMOOTHING-UNSTABLE — structure survives but not monotone with α |
| FAIL | FAIL | PASS | BOTH-FAIL — Q 108 centrality is neither monotone in α nor robust to length correction |
| — | — | FAIL | INSTRUMENT-BROKEN — pipeline cannot detect synthetic hub, results held in abeyance |
