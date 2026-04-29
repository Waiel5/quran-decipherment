---
id: H-NEW-278
title: Length-normalized MST rerun for OQ-19 (literal NM-36 operationalization)
phase: B
status: FAIL-COLLAPSE - Cell A FAIL, Cell B FAIL, MW-5 PASS
date: 2026-04-18
specialist: codex
parent: h-new-131
grandparent: h-new-134
seed: 20260418
rules_tuple: "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; Fisher-Rao arccos-Bhattacharyya; MST via Kruskal; no-tashkeel; QAC v0.4)"
bonferroni: k=2 alpha_bon=0.025 family=h-new-278-length-normalized-mst
pre_reg: findings/phase-b-hypotheses/h-new-278-length-normalized-mst-prereg.md
prereg_sha256: 8a1a31b5b7675c8f0a66b4a4e839cc3a94d06aeb250fba6d072231fa0e398a5f
script: scripts/h_new_278_length_normalized_mst.py
output_json: findings/phase-b-hypotheses/csv/h-new-278.json
verdict: COLLAPSE-UNDER-LITERAL-LENGTH-NORMALIZATION - under the literal NM-36 transform `count / N_i` before flat `alpha=0.5` smoothing, Q108 falls from degree 24 to degree 1, exits the top-3 entirely, and loses decisively to Q7 (15 vs 1).
---

# [[h-new-278-length-normalized-mst|H-NEW-278]] - Length-normalized MST rerun

## Headline

This is the smallest formal rerun of the OQ-19 length-normalization
question using the **literal `NM-36` operationalization**:

1. divide each surah's root-count vector by its own total STEM-root-token
   count `N_i`
2. then apply the ordinary flat Dirichlet `alpha = 0.5`
3. then rebuild the Fisher-Rao MST

Under that locked transform, **Q 108's hub anomaly collapses**.

- Baseline replication: Q 108 degree **24**, Q 7 degree **10**, Q 112 degree **8**
- Literal length-normalized rerun: Q 108 degree **1**, Q 7 degree **15**, Q 112 degree **1**
- Length-normalized top-3: **Q 7, Q 2, Q 17**
- Q 108 is **not** top-3 and is not even a secondary hub; it is a leaf

Both pre-registered cells fail. The MW-5 label-permutation control passes.

## Locked result

### Baseline replication

The parent pipeline reproduces exactly:

| Rank | Surah | Degree |
|---:|---:|---:|
| 1 | Q 108 | 24 |
| 2 | Q 7 | 10 |
| 3 | Q 112 | 8 |

So the starting point matches [[h-new-134-formal-prophet-named-signature|H-NEW-134]] / [[h-new-131-q108-supernode|H-NEW-131]] exactly.

### Literal NM-36 length-normalized MST

After replacing raw counts with `count / N_i` before smoothing:

| Rank | Surah | Degree |
|---:|---:|---:|
| 1 | Q 7 | 15 |
| 2 | Q 2 | 9 |
| 3 | Q 17 | 9 |
| 4 | Q 9 | 8 |
| 5 | Q 25 | 8 |

Key tracked surahs:

| Surah | Baseline degree | Length-normalized degree |
|---|---:|---:|
| Q 108 | 24 | **1** |
| Q 7 | 10 | **15** |
| Q 112 | 8 | **1** |

Q 108's only MST neighbor in the length-normalized rerun is **Q 89**.

### Cell A - top-3 replication

Baseline top-3 ids: `{108, 7, 112}`

Length-normalized top-3 ids: `{7, 2, 17}`

Overlap: `{7}` only.

Pre-registered PASS rule:

- Q 108 must remain top-3
- and at least 2 of the 3 baseline top-3 ids must survive

Observed:

- Q 108 top-3? **No**
- overlap count = **1**

**Cell A = FAIL.**

### Cell B - Q 108 vs Q 7

Pre-registered PASS rule: `deg(Q108) > deg(Q7)`.

Observed:

- `deg(Q108) = 1`
- `deg(Q7) = 15`

So the sign is not merely weakened; it **reverses strongly**.

**Cell B = FAIL.**

### MW-5 label-permutation control

The locked label permutation (seed `20260418`) behaves as expected:

- degree multiset unchanged: **PASS**
- Q 108 permuted degree changes from `1 -> 3`: **PASS**

So the code path is behaving like a genuine label-sensitive rerun, not a
hard-coded ranking report.

## Interpretation

The honest conclusion is narrow but clear:

**Under the literal `NM-36` length-normalization, Q 108's MST super-hub
claim does not survive.**

That means OQ-19 now has two distinct length-correction outcomes on the
books:

- **[[h-new-131-1-length-normalized-mst|H-NEW-131.1]]**: per-surah-`alpha_i` residualization left Q 108 as a
  degree-16 top hub
- **[[h-new-278-length-normalized-mst|H-NEW-278]]**: literal `count / N_i` before flat `alpha=0.5` smoothing
  collapses Q 108 to degree 1

These are not arithmetic contradictions. They are different
length-correction families. The lesson is methodological:

> one may no longer cite "length-normalized MST" generically as evidence
> that Q 108 is structurally robust. The answer depends sharply on which
> normalization family is used.

For the literal `NM-36` family specifically, the result is a **collapse**,
not a survival.

## Why the collapse is plausible

Q 108 has only **7** total STEM-root tokens, and only **4** of those fall
inside the locked top-500 feature space. So after the `count / N_i`
transform, Q 108 contributes only `4 / 7 = 0.5714` empirical mass across
the selected 500 dimensions before smoothing, whereas the Dirichlet prior
contributes `250` total units (`500 x 0.5`) to every surah equally.

In other words, the literal NM-36 transform erases the short-surah token
mass advantage very aggressively. Under that harsher correction, the hub
structure shifts toward longer broad-vocabulary surahs, led by **Q 7**.

## What this changes

- It strengthens the claim that the original degree-24 Q 108 super-hub
  observation is **not** robust to every reasonable length correction.
- It narrows the safe summary of OQ-19:
  Q 108 is robust under some correction families and collapses under
  others.
- It makes **normalization-family specificity** part of the live question,
  not a technical footnote.

## Limits

1. **Single feature space**: top-500 QAC STEM roots only.
2. **Alpha fixed at 0.5**: this is deliberate for comparability with the
   parent baseline.
3. **Literal NM-36 denominator** uses total STEM-root tokens, not top-500
   token count. That makes the correction harsher for surahs with lower
   top-500 coverage, including Q 108. This is a design choice locked from
   the `NM-36` wording, not a post-result tweak.
4. **Deterministic decision rules**: the two scored cells are bright-line
   replication tests on deterministic outputs, not Monte Carlo p-value
   tests.

## Bottom line

For the specific OQ-19 question posed by `NM-36`, the answer is:

**No. Q 108 does not stay top-3 under the literal length-normalized MST
rerun. It falls to degree 1, while Q 7 rises to degree 15 and becomes the
top hub.**
