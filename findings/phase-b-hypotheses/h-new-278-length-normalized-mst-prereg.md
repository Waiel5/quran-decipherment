---
finding_id: h-new-278
title: "Length-normalized MST rerun for OQ-19 (literal NM-36 operationalization)"
specialist: codex
date_prereg: 2026-04-18
seed: 20260418
parent_finding: h-new-131
parent_data: findings/phase-b-hypotheses/csv/h-new-131.json
grandparent: h-new-134 (exploratory MST super-hub observation); h-new-131.1 (alternative length-correction path)
bonferroni_k: 2
bonferroni_family: h-new-278-length-normalized-mst
alpha_bon: 0.025
alpha_raw: 0.05
rules_tuple: "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; Fisher-Rao arccos-Bhattacharyya; MST via Kruskal; no-tashkeel; QAC v0.4)"
pre_reg_standard: PRE-REG-STANDARD-04
---

# [[h-new-278-length-normalized-mst|H-NEW-278]] - Length-normalized MST rerun

## Why this rerun exists

OQ-19 remains open on the narrow question: if we apply the **literal**
length-normalization seed from `NM-36`, does Q 108 still look like an
MST hub?

This is deliberately narrower than [[h-new-131-1-length-normalized-mst|H-NEW-131.1]]. That earlier follow-up
used a **per-surah alpha-scaling** correction
`alpha_i = alpha_base x mean_tokens / N_i`, which left Q 108 as a degree-16
hub. `NM-36`, however, proposed a different and harsher operation:

> divide each surah's root-count vector by its own token count first,
> then apply ordinary Dirichlet-alpha smoothing.

The present run does exactly that, without adding alpha-sweeps, metric
families, or extra feature spaces.

## Locked design

### Shared pipeline

- Parse QAC v0.4 morphology file.
- Keep only `STEM` segments with a `ROOT`.
- Build corpus-global top-500 roots by frequency.
- For each surah, build its 500-dimensional root-count vector.
- Distance metric: Fisher-Rao `2 * arccos(sum sqrt(p_i q_i))`.
- Graph: complete 114-node graph.
- Extract MST by Kruskal.
- Tie-breaking for ranking hubs: sort by `(degree desc, surah_id asc)`.

### Baseline replication

Replicate the [[h-new-134-formal-prophet-named-signature|H-NEW-134]] / [[h-new-131-q108-supernode|H-NEW-131]] baseline exactly:

- raw top-500 counts
- flat Dirichlet `alpha = 0.5` on each of 500 cells
- L1 normalization after smoothing

Expected baseline top-3:

1. Q 108 degree 24
2. Q 7 degree 10
3. Q 112 degree 8

This is a sanity gate, not a scored cell.

### Length-normalized rerun

For each surah `i` and root cell `r`, define

`x[i,r] = count[i,r] / N_i`

where `N_i` is the surah's **total STEM-root-token count** in QAC v0.4.

Then apply the same flat Dirichlet smoothing as baseline:

`y[i,r] = x[i,r] + 0.5`

Then L1-normalize `y[i,*]` to the simplex, compute Fisher-Rao distances,
and rebuild the MST.

This follows the `NM-36` wording literally. It is intentionally distinct
from [[h-new-131-1-length-normalized-mst|H-NEW-131.1]]'s per-surah-alpha residualization.

## Primary cells

### Cell A - top-3 replication check (PRIMARY 1 of 2)

Compare the baseline top-3 hub set `{108, 7, 112}` against the
length-normalized top-3.

Locked decision rule:

- **PASS** if Q 108 remains in the length-normalized top-3 **and**
  at least 2 of the 3 baseline top-3 surahs remain in the
  length-normalized top-3.
- **FAIL** otherwise.

Interpretation:

- PASS = the hub hierarchy substantially replicates after literal
  length-normalization.
- FAIL = the original top-hub structure does not replicate under the
  literal NM-36 correction.

### Cell B - Q 108 vs Q 7 degree check (PRIMARY 2 of 2)

Compare Q 108 and Q 7 directly under the length-normalized MST.

Locked directional rule:

- **PASS** if `deg(Q108) > deg(Q7)`.
- **FAIL** otherwise.

This operationalizes the narrow OQ-19 question: does Q 108 remain the
dominant hub over the main baseline rival once length is normalized away?

## MW-5 control

Because `NM-36` explicitly called for a surah-to-distribution permutation
control, run one deterministic label permutation using seed `20260418`:

- keep the length-normalized probability vectors fixed
- randomly permute which surah id each vector is assigned to
- rebuild the MST and degree table

Expected behavior:

- the **degree multiset** must stay identical, because only labels moved
- the **label-level conclusions** must scramble

Locked MW-5 PASS condition:

- degree multiset unchanged, **and**
- Q 108's permuted degree differs from its empirical length-normalized
  degree

Failure means label-handling or reporting logic is suspect, and the run
is held `INSTRUMENT-BROKEN`.

## Garden of forking paths

- **Literal NM-36 denominator** = total STEM-root-token count `N_i`, not
  top-500 count and not mean-token alpha-scaling. This was chosen to
  match the `NM-36` wording as directly as possible.
- **Alpha fixed at 0.5** to preserve comparability with [[h-new-134-formal-prophet-named-signature|H-NEW-134]] /
  [[h-new-131-q108-supernode|H-NEW-131]]. Altering alpha would turn this into an alpha-sweep or a new
  residualization family.
- **Top-3 replication threshold = 2 of 3 plus Q 108 retained**. Exact
  top-3 identity would be too brittle; 1 of 3 would be too weak to count
  as replication.
- **Cell B direction = Q108 > Q7** because the specific OQ-19 anomaly is
  Q 108 outranking the main baseline competitor.
- **Permutation control is single-seed deterministic**, not Monte Carlo,
  because MW-5 here is a code-path sanity check rather than a new null
  family.

## Deliverables

- Pre-reg: `findings/phase-b-hypotheses/h-new-278-length-normalized-mst-prereg.md`
- Script: `scripts/h_new_278_length_normalized_mst.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-278.json`
- Findings: `findings/phase-b-hypotheses/h-new-278-length-normalized-mst.md`
- Journal: `journal/h-new-278-run-1.md`

## Pre-committed verdict table

| Cell A | Cell B | MW-5 | Final verdict |
|---|---|---|---|
| PASS | PASS | PASS | REPLICATES - Q 108 remains a genuine top-tier hub under literal NM-36 length-normalization |
| PASS | FAIL | PASS | PARTIAL-REPLICATION - top-3 survives but Q 108 no longer outranks Q 7 |
| FAIL | PASS | PASS | PARTIAL-REPLICATION - Q 108 beats Q 7 but broader top-3 structure reorganizes |
| FAIL | FAIL | PASS | COLLAPSE-UNDER-LITERAL-LENGTH-NORMALIZATION - Q 108 hub anomaly does not survive the NM-36 rerun |
| -- | -- | FAIL | INSTRUMENT-BROKEN - label-permutation control failed |
