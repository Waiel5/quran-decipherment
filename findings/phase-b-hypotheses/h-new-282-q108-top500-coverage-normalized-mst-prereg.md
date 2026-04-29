---
id: H-NEW-282
title: "Top-500 coverage-normalized MST follow-up for OQ-19"
phase: B
status: PRE-REGISTERED-FOR-BOUNDED-RUN
date: 2026-04-18
specialist: codex
seed: 20260418
parent_backdrop:
  - h-new-131 (baseline Q108 Fisher-Rao MST hub)
  - h-new-131.1 (per-surah-alpha residualization)
  - h-new-278 (literal count / N_i collapse)
  - h-new-279 (metric robustness on fixed alpha=0.5 simplex)
scope_note: "This is a bounded denominator-adjudication follow-up. It does not claim that top-500-mass normalization is the uniquely correct length correction; it tests whether H-NEW-278's collapse was specifically driven by using total STEM-root tokens in the denominator rather than the locked top-500 feature-space mass."
rules_tuple: "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; Fisher-Rao arccos-Bhattacharyya; Dirichlet alpha=0.5; MST via Kruskal; no-tashkeel; QAC v0.4)"
family_role: "bounded descriptive adjudication; no p-values claimed"
---

# [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] - Top-500 coverage-normalized MST follow-up

## Why this run exists

[[h-new-278-length-normalized-mst|H-NEW-278]] established that the literal `NM-36` rerun

`count[i,r] / N_i`

before flat `alpha = 0.5` smoothing collapses the Q108 hub claim:
`Q108 degree = 1`, `Q7 degree = 15`, and the top-3 becomes `{Q7, Q2, Q17}`.

But that literal denominator uses each surah's **total STEM-root-token
count** `N_i`, including tokens that do not live inside the locked
top-500 feature space. Since the MST itself only sees the top-500
dimensions, a narrower adjudication question is still open:

> was the collapse specifically driven by dividing by total surah token
> mass rather than by the surah's own token mass inside the same top-500
> feature space the MST uses?

This follow-up tests exactly that and nothing broader.

## Design honesty

This run is defensible only as a **bounded denominator-isolation probe**.
It is **not** promoted as the uniquely correct length normalization.

Why:

- the denominator now depends on the locked feature truncation (`K=500`)
- so the transform is feature-space-relative, not a corpus-global length
  correction
- that makes it useful for adjudicating [[h-new-278-length-normalized-mst|H-NEW-278]]'s collapse mechanism,
  but not for declaring `count / top500_mass` the new canonical family

If the result rescues Q108, the honest read is:

> denominator choice inside this feature family matters materially.

If it does not rescue Q108, the honest read is:

> the [[h-new-278-length-normalized-mst|H-NEW-278]] collapse is not mainly explained by off-space token mass
> leakage.

## Locked pipeline

### Shared parser / feature space

1. Parse QAC v0.4 exactly as in [[h-new-131-q108-supernode|H-NEW-131]] / [[h-new-278-length-normalized-mst|H-NEW-278]].
2. Keep only `STEM` segments with a `ROOT`.
3. Build the global top-500 root list by corpus frequency.
4. Build the `114 x 500` surah-level raw count matrix.
5. Use Fisher-Rao distance and Kruskal MST exactly as in the parent line.

### Three probability constructions

#### A. Baseline replication

For each surah and root cell:

`p_base[i,r] = (count[i,r] + 0.5) / sum_r(count[i,r] + 0.5)`

Expected replication:

- `Q108 degree = 24`
- `Q7 degree = 10`
- baseline top-3 = `{108, 7, 112}` with ordered table
  `[(108, 24), (7, 10), (112, 8)]`

#### B. [[h-new-278-length-normalized-mst|H-NEW-278]] comparator replication

Let `N_i` be total STEM-root tokens in surah `i`.

`x_total[i,r] = count[i,r] / N_i`

then

`p_total[i,r] = (x_total[i,r] + 0.5) / sum_r(x_total[i,r] + 0.5)`

Expected replication:

- `Q108 degree = 1`
- `Q7 degree = 15`
- top-3 ordered table `[(7, 15), (2, 9), (17, 9)]`

This is an instrument-comparator gate, not the new target result.

#### C. [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] coverage-normalized candidate

Let `M_i = sum_r count[i,r]` be surah `i`'s token mass **inside the
locked top-500 feature space**.

Define:

`x_cov[i,r] = count[i,r] / M_i`

then

`p_cov[i,r] = (x_cov[i,r] + 0.5) / sum_r(x_cov[i,r] + 0.5)`

This keeps the numerator and denominator inside the same observed feature
space and therefore isolates the denominator-choice question directly.

## Sanity / instrument checks

### Comparator replication gate

The script must reproduce both landed comparison anchors:

- baseline `[(108, 24), (7, 10), (112, 8)]`
- [[h-new-278-length-normalized-mst|H-NEW-278]] comparator `[(7, 15), (2, 9), (17, 9)]`

If either anchor fails, the run is `INSTRUMENT-BROKEN`.

### MW-5 label-permutation sanity check

Run one deterministic label permutation on the [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] coverage-
normalized probability vectors using seed `20260418`.

PASS requires:

- degree multiset unchanged
- Q108's permuted degree differs from its empirical [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] degree

Failure also yields `INSTRUMENT-BROKEN`.

## Locked readouts

For the [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] candidate record:

- ordered top-10 hub table
- `Q108` degree
- `Q7` degree
- whether `Q108` is top-3
- overlap with baseline top-3
- overlap with [[h-new-278-length-normalized-mst|H-NEW-278]] top-3
- `Q108` rank improvement or non-improvement versus [[h-new-278-length-normalized-mst|H-NEW-278]]

Top-3 tables use the same ordering as [[h-new-278-length-normalized-mst|H-NEW-278]]:
sort by `(degree desc, surah_id asc)`.

## Locked verdict rule

Let the [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] coverage-normalized result be the candidate result.

- `STRONG-DENOMINATOR-RESCUE`
  if `Q108` is top-3 **and** `deg(Q108) > deg(Q7)`.
- `PARTIAL-DENOMINATOR-RESCUE`
  if strong rescue fails, but `Q108` improves versus [[h-new-278-length-normalized-mst|H-NEW-278]] on both:
  `degree` and competition `rank`.
- `NO-DENOMINATOR-RESCUE`
  otherwise.
- `INSTRUMENT-BROKEN`
  if either comparator replication gate fails or MW-5 fails.

Interpretation:

- `STRONG` means the denominator swap alone materially restores the
  original anomaly.
- `PARTIAL` means the denominator matters, but not enough to recover the
  original hub claim.
- `NO-RESCUE` means [[h-new-278-length-normalized-mst|H-NEW-278]]'s collapse is not mainly explained by the
  total-token denominator.

## Deliverables

- Pre-reg: `findings/phase-b-hypotheses/h-new-282-q108-top500-coverage-normalized-mst-prereg.md`
- Script: `scripts/h_new_282_q108_top500_coverage_normalized_mst.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-282.json`
- Findings: `findings/phase-b-hypotheses/h-new-282-q108-top500-coverage-normalized-mst.md`
- Journal: `journal/h-new-282-run-1.md`
