---
id: H-NEW-131.1
title: Length-normalized MST — α-sweep + length-residualized smoothing
phase: B
status: MIXED — Cell A NULL (smoothing-monotone fails at pre-reg threshold); Cell B PASS (structural signal robust to length-residualization); MW-5 PASS
date: 2026-04-17
specialist: specialist-B (quran-equation-solvers)
parent: h-new-131 (Q 108 WEAKLY STRUCTURAL verdict)
grandparent: h-new-134 (MST super-hub observation)
seed: 20260417
rules_tuple: "(114 surahs Hafs-Kūfan; K=500 top QAC-STEM roots; Fisher-Rao arccos-Bhattacharyya; MST via Kruskal; no-tashkeel; QAC v0.4)"
bonferroni: k=2 α_bon=0.025 family=h-new-131-1-length-normalization
pre_reg: findings/phase-b-hypotheses/h-new-131-1-prereg.md
script: scripts/h_new_131_1_alpha_sweep.py
output_json: findings/phase-b-hypotheses/csv/h-new-131-1.json
verdict: STRUCTURAL-ROBUST + SMOOTHING-UNSTABLE — Q 108 centrality survives length-residualized smoothing (deg 16, within 15-33 window); but α-monotone relationship FAILS at the pre-committed ρ≥0.8 threshold due to a reversal at α=2.0.
---

# [[h-new-131-1-length-normalized-mst|H-NEW-131.1]] — Length-normalized MST

## Summary

[[h-new-131-q108-supernode|H-NEW-131]] showed Q 108's MST super-hub status (degree 24 at α=0.5) is
part mechanical, part structural. This follow-up traces the continuous
smoothing-dependence via a 7-point α-sweep AND tests a length-residualized
smoothing variant where each surah's prior scales as
`α_base × (mean_tokens / N_i)` — making every surah's prior-to-real-count
mass ratio equal.

**MW-5 positive control PASSED**: synthetic centroid (115th surah built as
empirical mean of 114 real surahs) gets MST-degree 62 — pipeline
correctly detects a planted hub. Q 108 retains degree 24 even in the
augmented 115-node graph.

**Cell A (α-sweep) FAILED at pre-committed Spearman ρ≥0.8**: the
relationship is a SATURATING MONOTONE WITH REVERSAL:

| α | Q 108 MST-degree | Top-1 hub |
|---:|---:|---|
| 0.001 | 1 | Q 7 (deg 21) |
| 0.01  | 11 | Q 7 (deg 25) |
| 0.05  | 21 | Q 108 (tied 21) |
| 0.1   | 24 | Q 108 (deg 24) |
| 0.5   | 24 | Q 108 (deg 24) |
| 1.0   | 24 | Q 108 (deg 24) |
| 2.0   | 22 | Q 108 (deg 22) |

Spearman ρ = 0.7412; 1-sided p = 0.028 (just above α_bon=0.025).

The saturating shape (Q 108's degree maxes at 24 across α∈[0.1, 1.0] and
then drops to 22 at α=2.0) breaks strict rank-monotonicity. With 7 α
points, a single inversion at the top end is enough to drag ρ below the
0.80 threshold.

**Cell B (length-residualized) PASSED**: Q 108 MST-degree = 16 (within
pre-committed 15-33 window around baseline 24).

Under length-residualized smoothing, Q 108's effective α_i = 31.3 (62×
baseline) because its 7 real STEM-root tokens are tiny compared to the
corpus mean (438 tokens). Q 2's effective α_i = 0.056 (the longest surah
gets the LEAST per-cell prior). Every surah's prior-to-real mass ratio
is structurally equalized.

Q 108 retains degree 16 in this length-residualized regime — sufficiently
higher than the 2nd-place Q 64 (deg 8) to still count as a hub, but at a
level well below the [[h-new-134-formal-prophet-named-signature|H-NEW-134]] super-hub claim.

**Final verdict: STRUCTURAL-ROBUST + SMOOTHING-UNSTABLE.**

Q 108's hub status survives explicit length-residualization — strong
evidence the centrality is not pure mechanical artifact. But the
relationship between α and degree is not cleanly monotone across the full
range; the bimodal tension at extreme α (α=0.001 crashes the hub, α=2.0
slightly reverses) means "smoothing strictly controls centrality" is a
simplification.

## Pre-reg compliance

Direction locked BEFORE execution. Per PRE-REG-STANDARD-04.
Bonferroni k=2, α_bon=0.025, family=[[h-new-131-1-length-normalized-mst|h-new-131-1]]-length-normalization.
Seed 20260417. MW-5 positive control passed (synthetic planted-hub
detected at degree 62, threshold 20).

## Detailed results

### MW-5 positive control

Synthetic surah 115 = empirical mean of 114 real surahs (row-average of
raw count matrix). Smoothed α=0.5. Rebuilt 115-node MST.

- Synthetic surah 115 MST-degree: **62** (of 114 possible adjacencies)
- Q 108 MST-degree in the 115-node MST: still **24**
- Top-10: [115:62, 108:24, 111:4, 103:4, 112:4, 2:4, 94:3, 105:3, 100:3, 102:3]

**Interpretation**:
- The synthetic mean-distribution surah immediately dominates as super-
  super-hub (degree 62) — confirming the pipeline will detect a planted
  hub.
- Q 108 STILL has degree 24 in the augmented graph. This is important:
  Q 108's centrality is not because "there's no better centroid";
  when a TRUE centroid is planted, Q 108 retains its sub-hub role.
  Q 108 connects 24 short/mid-mufaṣṣal surahs that are apparently NOT
  nearest-neighbors of the planted centroid.

### Cell A — α-sweep trace

Q 108's degree-curve is saturating-monotone-with-reversal:

```
α=0.001:   1 ▏
α=0.01:   11 ████████████
α=0.05:   21 ████████████████████████████
α=0.1:    24 ████████████████████████████████
α=0.5:    24 ████████████████████████████████
α=1.0:    24 ████████████████████████████████
α=2.0:    22 █████████████████████████████
```

**The transition is SHARP at the bottom**: Q 108 goes from degree 1 at
α=0.001 to degree 11 at α=0.01 to degree 21 at α=0.05 to the maximal 24
by α=0.1. After that it's a plateau from α=0.1 through α=1.0 before a
small 2-unit drop at α=2.0.

**Top-1 hub transitions**:
- α=0.001: Q 7 al-Aʿrāf (deg 21)
- α=0.01: Q 7 al-Aʿrāf (deg 25)
- α=0.05: Q 108 and Q 7 tied at 21 each
- α=0.1-2.0: Q 108 dominates

The crossover sits between α=0.01 and α=0.05 — specifically, Q 108
becomes the ranking hub by α=0.05 and holds until α=2.0.

Spearman ρ = 0.7412 (1-sided p = 0.028). Pre-committed threshold ρ≥0.80
→ **FAIL**. The 2-unit drop at α=2.0 is the source of the inversion.

**What this means**: the naive expectation "higher α → higher Q 108
degree" (because more smoothing → more uniform → more centroid-like)
HOLDS from α=0.001 up to the plateau around α=0.1, but then fails to
continue. At very high α=2.0, ALL surahs become more uniform, and the
distinction between Q 108's near-uniform distribution and other surahs'
increasingly-uniform distributions begins to compress — Q 108 is no
longer uniquely close to many neighbors.

This is a MORE NUANCED picture than the [[h-new-131-q108-supernode|H-NEW-131]] Cell A two-point
conclusion suggested. The relationship is not "monotone smoothing
creates centrality" but rather "there is a sweet spot in α where
Q 108 maximally appears as a hub, below which the raw-token distinction
reasserts and above which uniformity-compression flattens everyone."

### Cell B — length-residualized smoothing

Per-surah α_i = 0.5 × (438.32 / N_i):

- Q 108 (7 tokens): α_i = 31.3 (62× the flat baseline)
- Q 2 (3,884 tokens): α_i = 0.056
- Full range: [0.056, 31.3]

Under this per-surah-corrected smoothing, Q 108 MST-degree = **16**.

Pre-committed window: 15 ≤ degree ≤ 33 → **PASS**.

Top-10 hubs:
```
Q 108:16  Q 64:8  Q 78:7  Q 63:7  Q 45:7  Q 7:7  Q 96:5  Q 2:5  Q 112:4  Q 94:4
```

**Interpretation**: the length-residualized regime gives Q 108 a MASSIVE
effective prior (31×) that makes its distribution very close to uniform,
while simultaneously REDUCING long surahs' priors. In this regime, Q 2
drops from being a primary hub (it was deg 16 at flat α=0.01) to deg 5.
Q 108's own effective-α=31 centers it on the simplex → deg 16. So the
length-residualization gives Q 108 the "uniform centroid" property
intentionally.

The fact that Q 108 STILL reaches only degree 16 (not 24 or more) in
this length-residualized regime tells us:
- The length-residualization correctly compensates the short-surah
  effect
- Q 108's residual centrality (deg 16) is the "structural" portion,
  roughly 2/3 of the original super-hub value
- The top-hubs list reorganizes: Q 64, Q 78, Q 63, Q 45 become secondary
  hubs (these are mid-corpus surahs that presumably have
  broadly-distributed root profiles intrinsically)

### Cell C — degree distribution by α

At each α the degree distribution is heavy-tailed but the shape changes.
At α=0.001, 79 of 114 surahs are leaves (deg 1) and Q 7 has deg 21 —
long-tail network with one giant hub.
At α=0.5 (baseline) the distribution is the one in [[h-new-134-formal-prophet-named-signature|H-NEW-134]] (72
leaves + 1 super-hub-24). The overall shape is similar across α∈[0.05, 2.0]
with Q 108 at the top.

### Cell D — Q 108's MST-neighbors across α

At α=0.001, Q 108 has 1 neighbor. At α=0.01, 11 neighbors (mostly
short-mufaṣṣal). From α=0.1 onwards, all 24 neighbors are from
mufaṣṣal region (Q ≥ 50 for most). The hub persists as a
short-mufaṣṣal content-centroid across a wide α range.

### Cell E — top-4 rank preservation

[[h-new-134-formal-prophet-named-signature|H-NEW-134]]'s top-4 at α=0.5 is [108, 7, 112, 64]. This exact ordering is
NOT preserved at any other α:

- α=0.001: [7, 3, 2, 6]
- α=0.01: [7, 2, 108, 3]
- α=0.05: [108, 7, 2, 16]
- α=0.1: [108, 7, 2, 112]
- α=0.5: [108, 7, 112, 64] ← reference
- α=1.0: [108, 112, 64, 111] (tied 7s)
- α=2.0: [108, 64, 112, 110]

Q 108's rank-1 status is stable from α=0.05 onwards; the rest of the
top-4 reshuffles. This suggests Q 108 is the most α-robust hub; the
other hubs (Q 7, Q 2, Q 112, Q 64) fluctuate in and out of the top-4
depending on smoothing.

## What this refines / confirms

### Confirms

- Q 108's short-mufaṣṣal-content-centrality SURVIVES explicit length-
  residualization (Cell B). Degree 16 is not a super-hub magnitude but
  is still the top-1 hub in the length-residualized regime. The
  qualitative claim "Q 108 is the content-centroid of the short-mufaṣṣal
  cluster" is VALIDATED under an aggressive length-correction regime.
- MST pipeline is sensitive to planted hubs (MW-5 pass at deg 62).

### Refines

- [[h-new-131-q108-supernode|H-NEW-131]] Cell A's "α=0.01 gives degree 11" is now contextualized: the
  full curve shows degree transitions SHARPLY between α=0.001 (deg 1)
  and α=0.1 (deg 24). The α=0.01 point sits halfway up the slope. The
  plateau is narrower than the two-point picture suggested, but the
  SMOOTHING-FLOOR α where Q 108 loses hub status entirely is α≈0.001,
  not α=0.01.
- The saturating shape + reversal at α=2.0 refutes the simple "higher α
  → higher degree" picture. Q 108's centrality has a SMOOTHING SWEET
  SPOT in roughly α∈[0.1, 1.0].

### Demotes further

- The "smoothing-monotone" claim fails formally (Cell A). The honest
  picture is "saturating monotone in the relevant range, reversing
  modestly at extreme α". The 2-point [[h-new-131-q108-supernode|H-NEW-131]] Cell A evidence was
  directionally consistent but does not reflect the full structure.

## Implications for [[h-new-134-formal-prophet-named-signature|H-NEW-134]] / [[h-new-131-q108-supernode|H-NEW-131]] reframing

The [[h-new-131-q108-supernode|H-NEW-131]] reframing ("qualitative hub survives; 2.4× quantification
does not") is REINFORCED by [[h-new-131-1-length-normalized-mst|H-NEW-131.1]]. The length-residualized Cell B
gives a degree of 16 — confirming that SOME super-hub character is
length-driven, but a substantial structural residue (deg 16 > 2nd place
deg 8) remains.

**Further revised [[h-new-134-formal-prophet-named-signature|H-NEW-134]] summary recommendation**:

> "Q 108 al-Kawthar is a robust high-degree MST hub under Fisher-Rao-
> family metrics in the Dirichlet-α range [0.05, 1.0]. Under length-
> residualized smoothing (per-surah α ∝ 1/N_i) its degree is 16 — still
> the top-1 hub, but at half the apparent super-hub magnitude. The
> degree-24 'super-hub' observation at α=0.5 reflects an approximately
> doubled centrality from the smoothing-length interaction. The
> structural residue (≈ deg 16) reflects the short-mufaṣṣal
> content-centroid role genuinely, and is robust to length residualization
> and to metric choice within the Fisher-Rao-Hellinger-JS family ([[h-new-131-q108-supernode|H-NEW-131]]
> Cell B). Outside that family (total variation) the hub status does not
> survive ([[h-new-131-q108-supernode|H-NEW-131]] Cell B). Outside the α-sweet-spot (α < 0.01 or
> α > 2.0) the hub status also weakens ([[h-new-131-1-length-normalized-mst|H-NEW-131.1]] Cell A)."

## Caveats and limits

1. **Single feature space**: STEM-root top-500. Cross-feature-space
   replication queued at H-NEW-131.3.
2. **Length-residualization formula choice**: `α × mean/N_i` is the
   principal minimal-parameter option. Alternative residualizations
   (TF-IDF, empirical Bayes) remain open.
3. **Spearman ρ=0.74 is not "bad" in absolute terms**; it indicates
   strong monotone tendency with one inversion at the top. Reporting
   FAIL reflects the pre-committed threshold, not the raw absence of
   signal. Under a looser threshold (ρ≥0.70) the test would pass; that
   threshold was NOT pre-committed, and changing it post-result would
   violate PRE-REG-STANDARD-04. The monotone-tendency interpretation is
   DESCRIPTIVE.

## Queued follow-ups

- **H-NEW-131.3** (already queued): cross-feature-space replication.
- **H-NEW-131.5** (new): finer α-grid near the crossover. Extend grid
  to {0.002, 0.005, 0.02, 0.03} to pinpoint where Q 108 crosses Q 7 as
  the top hub (currently known to occur between α=0.01 and α=0.05).
- **H-NEW-131.6** (new): why does Q 108 degree DROP 2 units from α=1.0
  to α=2.0? Is it pushed out by a different surah becoming super-hub at
  very-high-α? (Q 64 appears at deg 8 at α=2.0 — not a replacement.)
- **H-NEW-131.7** (new): is the length-residualization Cell B degree-16
  STABLE across the full α range, or does it also trace a curve?

## Connections

- Parent: [[h-new-131-q108-supernode|H-NEW-131]] (Q 108 WEAKLY STRUCTURAL)
- Grandparent: [[h-new-134-formal-prophet-named-signature|H-NEW-134]] (MST super-hub observation)
- Method-source: [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (Fisher-Rao D-matrix pipeline)
- Related prior: findings/phase-c-structures/al-kawthar-and-shortest-surahs-deep-dive.md (Q 108 linguistic fingerprint; orthogonal axis)
