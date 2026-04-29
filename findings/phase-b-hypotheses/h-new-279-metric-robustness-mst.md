---
id: H-NEW-279
title: Metric-robustness MST
phase: B
status: PASS-BOUNDED — Q108 is a metric-robust top-tier MST hub, but not a metric-invariant super-hub by magnitude
date: 2026-04-18
specialist: codex
parent: h-new-134
parent_followups:
  - h-new-131
  - h-new-131.1
seed: 20260418
rules_tuple: "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; Dirichlet alpha=0.5; MST via Kruskal; QAC v0.4)"
pre_reg: findings/phase-b-hypotheses/h-new-279-metric-robustness-mst-prereg.md
script: scripts/h_new_279_metric_robustness_mst.py
output_json: findings/phase-b-hypotheses/csv/h-new-279.json
verdict: METRIC-ROBUST TOP-TIER HUB — Q108 ranks top-3 on all 5 locked primary metrics, but the original super-hub magnitude is not metric-invariant because total-variation demotes it to rank-2 at degree 6.
---

# [[h-new-279-metric-robustness-mst|H-NEW-279]] — Metric-robustness MST

## Summary

NM-37 asked whether the `Q108 al-Kawthar` MST anomaly survives a broader
distance family or whether it is mostly a Fisher-Rao artifact. This run
locks the smallest clean non-redundant first pass available on disk:

- `Fisher-Rao`
- `Jensen-Shannon`
- `Total variation`
- `Euclidean L2`
- `Cosine-angle`

with `Hellinger` kept only as a diagnostic redundancy check, not a counted
primary metric.

**Result**: `Q108` is a **metric-robust top-tier hub**. Under the locked
competition-rank criterion, it is top-3 on **5/5** primary metrics and
rank-1 on **4/5** of them. But the **magnitude** of the original
Fisher-Rao super-hub claim is NOT metric-invariant: total-variation drops
`Q108` from degree `24` to degree `6`, leaving it at rank `2` behind
`Q64`.

So the honest update to OQ-19 is:

> the claim "Q108 is a top-tier MST hub" is metric-robust on the locked
> alpha=0.5 simplex;
> the stronger claim "Q108 has a universally extreme super-hub magnitude"
> is false.

## Pre-reg compliance and sanity checks

- Fisher-Rao baseline replication passed exactly:
  `Q108 degree = 24` as in [[h-new-131-q108-supernode|H-NEW-131]].
- Diagnostic redundancy check passed:
  `Hellinger` reproduced the exact same MST edge set as `Fisher-Rao`.
- No deviations from the locked pre-reg.

These matter because the run is not introducing a new feature space or a
new smoothing regime. It is isolating metric choice only.

## Per-metric Q108 results

| Metric | Q108 degree | Q108 rank | Read |
|---|---:|---:|---|
| Fisher-Rao | **24** | **1** | baseline super-hub |
| Jensen-Shannon | **24** | **1** | exact FR replication at the MST level |
| Total variation | 6 | 2 | strong demotion in magnitude, but still top-tier |
| Euclidean L2 | 22 | **1** | near-FR super-hub magnitude |
| Cosine-angle | 21 | **1** | near-FR super-hub magnitude |
| Hellinger (diagnostic) | 24 | 1 | exact FR redundancy check |

Primary pre-registered rule:

- `Q108` counts as a metric-robust hub if it ranks top-3 on at least 4 of
  the 5 primary metrics.

Observed:

- `Q108` top-3 count = **5 / 5**
- final verdict = **METRIC-ROBUST HUB**

## Consensus hub table

Top-3 appearance counts across the 5 primary metrics:

| Surah | Top-3 appearances |
|---|---:|
| Q108 | **5** |
| Q7 | 4 |
| Q112 | 3 |
| Q64 | 2 |
| Q3 | 1 |

This is useful because the secondary hub structure shifts more than the
Q108 result does. `Q7`, `Q112`, and `Q64` move around by metric; `Q108`
does not leave the top tier.

## What changes relative to [[h-new-131-q108-supernode|H-NEW-131]]

[[h-new-131-q108-supernode|H-NEW-131]] used an absolute-degree rule (`>= 15`) and therefore treated
total-variation as a failure for the robust-super-hub claim. [[h-new-279-metric-robustness-mst|H-NEW-279]]
uses a rank-based rule because the purpose here is metric comparison, and
absolute degree magnitudes are not directly comparable across distance
families.

Under that cleaner rank-based read:

- `TV` does **not** preserve the Fisher-Rao magnitude
- but `TV` **does** preserve Q108 as a near-top hub (`rank 2`)

So the broad escape route

> "Q108 is only central under Fisher-Rao-like metrics"

is now too strong. The better reading is narrower:

> "Q108's *extreme* degree depends on metric family, but its *top-tier hub
> standing* does not."

## OQ-19 interpretation

Taken together with the earlier runs:

- [[h-new-131-q108-supernode|H-NEW-131]]: smoothing matters and TV compresses the degree sharply
- [[h-new-131-1-length-normalized-mst|H-NEW-131.1]]: length-residualized smoothing still leaves `Q108` at
  degree `16`
- [[h-new-279-metric-robustness-mst|H-NEW-279]]: once the baseline simplex is fixed, `Q108` remains top-tier
  across every locked non-redundant metric in this bounded pass

The cumulative picture is now:

- **mechanical-only** is no longer plausible
- **Fisher-Rao-only** is also no longer plausible for top-tier rank
- the remaining open question is **mechanism**, not mere existence:
  why does this very short surah sit so close to so many others even after
  length correction and metric variation?

That mechanism question remains open. OQ-19 is refined again, not fully
closed.

## Caveats

1. This was intentionally bounded to **5** primary metrics, not `7`.
   That was a design constraint, not a convenience choice:
   `Hellinger` would have been redundant and `KL` would have required an
   extra symmetrization choice not already locked on disk for this line.
2. The run keeps `alpha = 0.5` fixed on purpose. It should be read
   together with [[h-new-131-q108-supernode|H-NEW-131]] / 131.1, not as a replacement for those
   smoothing probes.
3. The verdict is about **hub rank robustness**, not about a new
   inferential p-value. Metric outcomes are dependent; this was a bounded
   robustness table, not a significance test.

## Bottom line

`Q108 al-Kawthar` is the **only** surah that stays top-3 across all 5
locked primary metrics in this bounded first pass. The strong claim that
its exact degree-24 super-hub magnitude is universal is false, but the
weaker and still important claim that it is a **metric-robust top-tier MST
hub** is now supported.
