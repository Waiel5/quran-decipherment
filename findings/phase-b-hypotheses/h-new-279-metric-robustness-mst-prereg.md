---
id: H-NEW-279
title: "Metric-robustness MST — bounded five-metric pass for the Q108 hub anomaly"
phase: B
status: PRE-REGISTERED-FOR-BOUNDED-RUN
date: 2026-04-18
specialist: codex
seed: 20260418
parent_backdrop:
  - h-new-134 (exploratory Q108 MST super-hub observation)
  - h-new-131 (Fisher-Rao / JS / TV robustness + smoothing probe)
  - h-new-131.1 (length-residualized smoothing)
scope_note: "This run isolates metric choice only. Smoothing choice is locked at the H-NEW-131 baseline alpha=0.5 because H-NEW-131 and H-NEW-131.1 already handled the smoothing question directly."
rules_tuple: "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; Dirichlet alpha=0.5 on every cell; same QAC v0.4 parser and top-K construction as H-NEW-111 / H-NEW-131; MST via Kruskal on complete 114-node graph)"
primary_metric_family:
  - fisher_rao
  - jensen_shannon
  - total_variation
  - euclidean_l2
  - cosine_angle
diagnostic_metric:
  - hellinger
exclusions:
  hellinger: "Excluded from the primary family because it is a strict monotone transform of the Bhattacharyya coefficient and therefore should yield the same Kruskal MST as Fisher-Rao."
  kullback_leibler: "Excluded because metric-robustness would require an extra symmetrization convention (Jeffreys / symmetrized KL / other) that is not already locked on disk for this MST line."
  earth_mover: "Excluded because no ground metric over the 500 roots is defined in the parent pipeline."
family_role: "bounded descriptive robustness classification; no p-values are claimed because the metric outcomes are highly dependent and the goal is rank-robustness, not a new null-hunting exercise"
---

# [[h-new-279-metric-robustness-mst|H-NEW-279]] — Metric-robustness MST

## Question

After [[h-new-131-q108-supernode|H-NEW-131]] and [[h-new-131-1-length-normalized-mst|H-NEW-131.1]], the remaining open slice of OQ-19 is
not "does smoothing matter?" That is already answered: yes, partly. The
remaining slice is narrower:

> once the input distributions are held fixed at the [[h-new-131-q108-supernode|H-NEW-131]] baseline,
> is `Q108 al-Kawthar` still a hub across a non-redundant family of
> distance metrics, or is the hub status mostly a Fisher-Rao-family
> artifact?

This run is deliberately bounded and descriptive. It does not try to
solve OQ-19 by itself. It just locks a clean metric-family table.

## Why five metrics, not seven

NM-37 suggested `6+` or `7` distances. The cleanest on-disk first pass is
smaller:

- `Hellinger` is not counted because, for Kruskal MST purposes, it is
  redundant with `Fisher-Rao`: both are strict monotone transforms of the
  same Bhattacharyya overlap.
- `KL` is not counted because "metric-robustness" would require choosing a
  symmetric KL convention that the parent MST line has not already locked.
- Distances that need an external geometry on roots are out-of-scope
  because the current pipeline only has simplex probabilities, not a root
  ground-distance matrix.

So the primary family is the smallest clean non-redundant set available
from the existing data and parent code:

1. `Fisher-Rao`
2. `Jensen-Shannon`
3. `Total variation`
4. `Euclidean L2`
5. `Cosine-angle`

## Locked operationalization

### Shared input

1. Parse QAC v0.4 exactly as in [[h-new-111-fisher-rao-mushaf|H-NEW-111]] / [[h-new-131-q108-supernode|H-NEW-131]]:
   STEM segments only, root from `ROOT:*`, surah-level aggregation.
2. Lock `K = 500` top global roots by corpus count.
3. Build the `114 x 500` count matrix.
4. Apply Dirichlet `alpha = 0.5` to every cell.
5. L1-normalize each row to the probability simplex.

No other feature-space changes are allowed.

### Distances

For each pair of smoothed surah probability vectors `p, q`:

- `Fisher-Rao`: `2 * arccos(sum_i sqrt(p_i * q_i))`
- `Jensen-Shannon`: `sqrt(0.5 * KL(p||m) + 0.5 * KL(q||m))`, `m=(p+q)/2`
- `Total variation`: `0.5 * sum_i |p_i - q_i|`
- `Euclidean L2`: `sqrt(sum_i (p_i - q_i)^2)`
- `Cosine-angle`: `arccos( dot(p,q) / (||p||_2 ||q||_2) )`

Diagnostic only:

- `Hellinger`: `sqrt(0.5 * sum_i (sqrt(p_i) - sqrt(q_i))^2 )`

### MST / hub readout

For each metric:

1. Build the full `114 x 114` distance matrix.
2. Compute the MST by Kruskal.
3. Compute node degree in the MST.
4. Compute `Q108`'s hub rank using **competition ranking**:
   `rank = 1 + number of surahs with strictly larger degree`.

This is rank-based, not absolute-degree-based, because degree magnitudes
can shift by metric even when relative hub standing is the relevant
question.

## Primary decision rule

Let `c` be the number of the 5 primary metrics for which `Q108` has
hub-rank `<= 3`.

- `c >= 4`: **METRIC-ROBUST HUB**
- `c in {2, 3}`: **PARTIAL METRIC-ROBUSTNESS**
- `c = 1`: **METRIC-SPECIFIC**
- `c = 0`: **NOT ROBUST**

This is the only primary verdict rule.

## Secondary descriptive outputs

These are descriptive only and do not alter the main verdict:

- per-metric Q108 degree
- per-metric Q108 hub rank
- top-10 hubs for each metric
- top-3-appearance counts for all surahs across the 5 primary metrics
- whether diagnostic `Hellinger` reproduces the Fisher-Rao MST edge set

## Sanity / instrument checks

### MW-5 style parent replication

The Fisher-Rao baseline must reproduce the already-landed [[h-new-131-q108-supernode|H-NEW-131]]
result:

- `Q108` MST degree under `Fisher-Rao`, `alpha=0.5` must equal `24`

If this fails, the instrument is declared broken and the run is not
promoted.

### Diagnostic redundancy check

`Hellinger` should reproduce the same MST edge set as `Fisher-Rao`. If it
does not, the likely cause is an implementation bug or a tie-handling
problem, and the run is held in abeyance.

## Garden of forking paths

- `alpha` is fixed at `0.5` because this task is metric-robustness only.
  Reopening `alpha` would conflate NM-36 with NM-37 after those questions
  were already partially answered by [[h-new-131-q108-supernode|H-NEW-131]] and [[h-new-131-1-length-normalized-mst|H-NEW-131.1]].
- Rank `<= 3` is chosen, not a raw degree threshold, because the metric
  scales are incomparable and some metrics yield flatter degree
  distributions.
- The threshold `4/5` is the bounded analog of NM-37's original
  `5/7` idea: Q108 should clear a strong majority of non-redundant
  metrics before being called metric-robust.
- `Cosine-angle` is used, not `1 - cosine`, because the angle form is the
  cleaner geometric distance.

## Deliverables

- Script: `scripts/h_new_279_metric_robustness_mst.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-279.json`
- Findings: `findings/phase-b-hypotheses/h-new-279-metric-robustness-mst.md`
- Journal: `journal/h-new-279-run-1.md`
