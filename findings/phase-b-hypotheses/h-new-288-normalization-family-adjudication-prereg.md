---
id: H-NEW-288
title: "Normalization-family adjudication for OQ-19"
phase: B
status: PRE-REGISTERED-FOR-BOUNDED-RUN
date: 2026-04-19
specialist: codex
seed: 20260419
parent_backdrop:
  - h-new-278 (literal count / N_i collapse under Fisher-Rao)
  - h-new-279 (5-metric robustness on the baseline alpha=0.5 simplex)
  - h-new-282 (top-500 denominator rescue fails under Fisher-Rao)
  - h-new-284 (5-metric robustness of the length-residualized residue)
scope_note: "This run is a direct family adjudication. It holds the H-NEW-279 five-metric panel fixed and compares the two competing length-control families already on the board: literal count / N_i normalization versus per-surah alpha_i residualization. No new feature space, no new denominator family, no new null-hunting."
rules_tuple: "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; MST via Kruskal; no-tashkeel; QAC v0.4; primary metrics = Fisher-Rao / Jensen-Shannon / total variation / Euclidean L2 / cosine-angle)"
family_role: "bounded descriptive adjudication; no p-values claimed because the five metric outcomes are dependent and the point is to separate normalization families, not to introduce a synthetic null"
---

# [[h-new-288-normalization-family-adjudication|H-NEW-288]] - Normalization-family adjudication for OQ-19

## Question

After [[h-new-278-length-normalized-mst|H-NEW-278]], [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]], and [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]], the clean remaining question
is not whether one more normalization can be invented. It is:

> under the same locked five-metric MST panel, which length-control
> family actually owns the surviving Q108 hub residue?

The two live families already on disk are:

1. **Literal normalization family** from [[h-new-278-length-normalized-mst|H-NEW-278]]:
   divide each surah's top-500 count vector by its total STEM-root token
   count `N_i`, then add flat `alpha = 0.5`.
2. **Residualized smoothing family** from [[h-new-131-1-length-normalized-mst|H-NEW-131.1]] / [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]]:
   keep raw counts, but use per-surah
   `alpha_i = alpha_base * (mean_surah_tokens / N_i)`.

[[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] already ruled out the simplest denominator-only rescue inside
the literal family, so this run compares the two family heads directly.

## Locked pipeline

### Shared parser / feature space

1. Parse QAC v0.4 exactly as in [[h-new-278-length-normalized-mst|H-NEW-278]] / [[h-new-279-metric-robustness-mst|H-NEW-279]] / [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]]:
   `STEM` segments only, root from `ROOT:*`, surah-level aggregation.
2. Lock `K = 500` top global roots by corpus frequency.
3. Build the `114 x 500` surah-level count matrix.
4. Keep the [[h-new-279-metric-robustness-mst|H-NEW-279]] primary metric family fixed:
   Fisher-Rao, Jensen-Shannon, total variation, Euclidean L2,
   cosine-angle.
5. Use the same MST construction and competition rank readout as
   [[h-new-279-metric-robustness-mst|H-NEW-279]] / [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]].

### Family A: literal normalization

For surah `i`, let `N_i` be total STEM-root tokens in the surah.

`x_lit[i,r] = count[i,r] / N_i`

then

`p_lit[i,r] = (x_lit[i,r] + 0.5) / sum_r(x_lit[i,r] + 0.5)`

This is exactly the [[h-new-278-length-normalized-mst|H-NEW-278]] family, now rerun across the [[h-new-279-metric-robustness-mst|H-NEW-279]]
five-metric panel.

### Family B: residualized smoothing

Let

`alpha_i = 0.5 * (mean_surah_tokens / N_i)`

and define

`p_res[i,r] = (count[i,r] + alpha_i) / sum_r(count[i,r] + alpha_i)`

This is exactly the [[h-new-131-1-length-normalized-mst|H-NEW-131.1]] / [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] family.

## Primary statistics

For each family, define:

- `C_lit = number of metrics with rank(Q108) <= 3 under p_lit`
- `C_res = number of metrics with rank(Q108) <= 3 under p_res`

Primary separation statistic:

- `Delta_C = C_res - C_lit`

This is the only statistic used for the main family adjudication.

## Decision rule

This is descriptive and bounded:

- `Delta_C >= 3` and `C_res >= 4`
  => **RESIDUALIZED-FAMILY-DOMINANCE**
- `Delta_C in {1, 2}` and `C_res > C_lit`
  => **PARTIAL-RESIDUALIZED-ADVANTAGE**
- `Delta_C = 0`
  => **NO-FAMILY-SEPARATION**
- `Delta_C < 0`
  => **LITERAL-FAMILY-ADVANTAGE**

Interpretation:

- `RESIDUALIZED-FAMILY-DOMINANCE` means the surviving Q108 hub residue is
  not a generic length-corrected phenomenon. It belongs mainly to the
  residualized smoothing family.
- `NO-FAMILY-SEPARATION` means the present evidence does not distinguish
  the two length-control families at the metric-family level.

## Secondary descriptive outputs

These do not alter the verdict:

- per-metric `Q108` degree and competition rank under each family
- top-10 hubs under each family and metric
- `Q108` MST neighbors under each family and metric
- family-wise summary table of `Q108` top-3 hits

## Sanity / inheritance checks

These inherited anchors must be reproduced:

1. Literal-family Fisher-Rao must match [[h-new-278-length-normalized-mst|H-NEW-278]]:
   `Q108 degree = 1`, `Q7 degree = 15`.
2. Residualized-family Fisher-Rao must match [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]] / [[h-new-131-1-length-normalized-mst|H-NEW-131.1]]:
   `Q108 degree = 16`, `Q108 rank = 1`.

If either anchor fails, the run is `INSTRUMENT-BROKEN`.

## Deliverables

- Pre-reg:
  `findings/phase-b-hypotheses/h-new-288-normalization-family-adjudication-prereg.md`
- Script:
  `scripts/h_new_288_normalization_family_adjudication.py`
- JSON:
  `findings/phase-b-hypotheses/csv/h-new-288.json`
- Findings:
  `findings/phase-b-hypotheses/h-new-288-normalization-family-adjudication.md`
- Journal:
  `journal/h-new-288-run-1.md`
