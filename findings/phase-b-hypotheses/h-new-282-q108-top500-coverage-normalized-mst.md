---
id: H-NEW-282
title: Top-500 coverage-normalized MST follow-up for OQ-19
phase: B
status: FAIL-COLLAPSE
date: 2026-04-18
agent: codex
parents:
  - H-NEW-131
  - H-NEW-131.1
  - H-NEW-278
  - H-NEW-279
open_question: OQ-19
seed: 20260418
prereg: findings/phase-b-hypotheses/h-new-282-q108-top500-coverage-normalized-mst-prereg.md
script: scripts/h_new_282_q108_top500_coverage_normalized_mst.py
json: findings/phase-b-hypotheses/csv/h-new-282.json
journal: journal/h-new-282-run-1.md
rules_tuple: "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; Fisher-Rao arccos-Bhattacharyya; Dirichlet alpha=0.5; MST via Kruskal; no-tashkeel; QAC v0.4)"
---

# [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] — Top-500 coverage-normalized MST follow-up for OQ-19

## Headline

[[h-new-278-length-normalized-mst|H-NEW-278]] showed that Q108 collapses under the literal NM-36
length-normalization because each surah is divided by its **total**
stem-root token mass `N_i` before flat `alpha = 0.5` smoothing.

The obvious objection was denominator choice:

> maybe the collapse is driven only by using all stem-root tokens in the
> denominator rather than the surah's mass **inside the locked top-500
> feature space**.

[[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] tests exactly that and nothing broader.

It does **not** rescue Q108.

- baseline: `Q108 = 24`, `Q7 = 10`
- H-278 comparator: `Q108 = 1`, `Q7 = 15`
- H-282 candidate: `Q108 = 1`, `Q7 = 18`
- Q108 is **not** top-3
- overall verdict = **FAIL-COLLAPSE**

So the H-278 collapse is not a mere denominator bookkeeping artifact.

## What was changed

Three denominator families are now directly on the board:

1. **Baseline**
   raw top-500 counts + flat `alpha = 0.5`
2. **H-278 comparator**
   `count[i,r] / total_stem_root_tokens_in_surah_i`
3. **H-282 candidate**
   `count[i,r] / top500_token_mass_in_surah_i`

H-282 is explicitly **not** claimed as a canonical normalization family.
It is a bounded adjudication probe aimed at one narrow question:

> was H-278's collapse caused mainly by dividing Q108 by total stem-token
> mass even though only 4 of its 7 tokens lie inside the top-500 feature
> space?

Answer: no.

## Core numbers

### Baseline replication

| Rank | Surah | Degree |
|---:|---:|---:|
| 1 | Q108 | 24 |
| 2 | Q7 | 10 |
| 3 | Q112 | 8 |

### H-278 literal normalization

| Rank | Surah | Degree |
|---:|---:|---:|
| 1 | Q7 | 15 |
| 2 | Q2 | 9 |
| 3 | Q17 | 9 |

Tracked values:

- `Q108 = 1`
- `Q7 = 15`
- `Q108` competition rank = `40`

### H-282 top-500-mass normalization

| Rank | Surah | Degree |
|---:|---:|---:|
| 1 | Q7 | 18 |
| 2 | Q9 | 9 |
| 3 | Q25 | 8 |

Tracked values:

- `Q108 = 1`
- `Q7 = 18`
- `Q108` competition rank = `42`
- `Q108` top-3? **No**
- `Q108` nearest MST neighbor remains `Q89`

## Denominator adjudication

The decisive summary from the JSON is simple:

| Question | Result |
|---|---|
| Does Q108 return to top-3 under top-500-mass normalization? | **No** |
| Does Q108 beat Q7 under top-500-mass normalization? | **No** |
| Does Q108 even improve versus H-278? | **No** |
| Does Q108's competition rank improve versus H-278? | **No** |

In fact the candidate normalization is slightly harsher than H-278 for
Q108:

- H-278 rank = `40`
- H-282 rank = `42`

So the collapse persists and may even deepen.

## Why this matters

Q108's short-surah hub story now has a more exact shape.

### What survives

- [[h-new-279-metric-robustness-mst|H-NEW-279]] still says Q108 is a metric-robust top-tier hub **inside the
  fixed smoothed baseline geometry**
- the anomaly is real there

### What fails

- H-278 showed literal length normalization destroys the anomaly
- H-282 now shows this is **not** merely because Q108 has low top-500
  coverage and got penalized by the wrong denominator

So the right reading is now:

> the Q108 hub is robust across metrics within the original smoothed
> simplex, but it is not robust across plausible normalization families,
> and the collapse is not explained away by a simple denominator fix.

That is a stronger and cleaner OQ-19 refinement than H-278 alone.

## Token-mass context

The denominator dispute was worth testing because Q108 is unusually tiny:

- Q108 total stem-root tokens = `7`
- Q108 top-500 tokens = `4`
- Q108 top-500 coverage = `0.5714`

Compare Q7:

- Q7 total stem-root tokens = `2144`
- Q7 top-500 tokens = `1992`
- Q7 top-500 coverage = `0.9291`

Even after correcting the denominator to match feature-space coverage,
Q108 still does not recover. So the fragility is broader than that one
coverage mismatch.

## Bottom line

[[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] rules out the simplest rescue story for H-278.

Q108's collapse under normalization is **not** just an artifact of using
the wrong denominator. A top-500-coverage-normalized Fisher-Rao MST still
leaves Q108 at degree `1`, outside the top-3, and far behind Q7.
