---
id: H-NEW-269
title: "qul imperative addressee-pattern test"
status: PARTIAL-CLASS-ONLY — 1/4 Bonferroni cells PASS; MW-5 positive control valid
date: 2026-04-18
agent: h-new-269-specialist
prereg: findings/phase-b-hypotheses/h-new-269-qul-addressee-pattern-prereg.md
script: scripts/h_new_269_qul_addressee_pattern.py
json: findings/phase-b-hypotheses/csv/h-new-269.json
journal: journal/h-new-269-run-1.md
seed: 20260418
n_perm: 5000
bonferroni_family: h-new-269-qul-addressee-pattern
bonferroni_k: 4
alpha_bon: 0.0125
rules_tuple: "(332 canonical qul tokens from Leeds QAC v0.4; no-tashkeel normalized token windows; QAC STEM roots; opener-family stripping; matched nonclass qul null on residual 6-word root mass)"
---

# [[h-new-269-qul-addressee-pattern|H-NEW-269]] — qul imperative addressee-pattern test

## Headline

The 332 canonical `qul` imperatives do **not** support a broad
multi-class addressee/rhetorical taxonomy at this resolution.

Under the locked [[h-new-269-qul-addressee-pattern|H-NEW-269]] design:

- four coarse opener families were tested
- those four families covered **117 / 332 tokens** (**35.2%**)
- only **one** family survived Bonferroni after its opener marker was
  stripped away
- MW-5 passed cleanly

So the bounded answer is:

**one narrow `qul` class exists beyond raw opener frequency, but the
larger visible families are mostly opener-frequency phenomena under this
6-word residual-root test.**

## Primary results

### Corpus frame

- canonical `qul` tokens: **332**
- unique `qul` verses: **306**
- inferential family tokens: **117** (**35.2%**)
- descriptive residue (`OTHER`): **215** (**64.8%**)

### Bonferroni family (`k = 4`, `alpha_bon = 0.0125`)

| Cell | Locked class | n | Share of 332 | Observed Jaccard | Null mean | Null q95 | z | p_perm | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| A | `VOCATIVE_ADDRESS` | 16 | 4.8% | 0.0442 | 0.0387 | 0.0704 | +0.317 | 0.3221 | NULL |
| B | `INTERROGATIVE_OR_CHALLENGE` | 55 | 16.6% | 0.0372 | 0.0394 | 0.0530 | -0.288 | 0.5767 | NULL |
| C | `SELF_OR_DEVOTIONAL` | 27 | 8.1% | 0.0249 | 0.0410 | 0.0639 | -1.286 | 0.9256 | NULL |
| D | `RESTRICTIVE_DECLARATION` | 19 | 5.7% | **0.1142** | 0.0406 | 0.0683 | **+4.879** | **0.0008** | **PASS** |

Overall family verdict: **PARTIAL-CLASS-ONLY**.

## What actually survives

### The real class: `qul innama ...`

The only class that remains coherent after opener stripping is the
`RESTRICTIVE_DECLARATION` family:

- observed residual mean pairwise Jaccard = **0.1142**
- matched-null mean = **0.0406**
- excess above null = about **2.8x**
- Bonferroni-surviving `p_perm = 0.0008`

This is a genuine narrow class, not just the fact that `innama`
itself is common.

Representative members:

- Q 7:33 `qul innama harrama rabbi ...`
- Q 13:36 `qul innama umirtu an a'buda llaha ...`
- Q 18:110 `qul innama ana basharun mithlukum ...`
- Q 21:45 `qul innama undhirukum bil-waHy ...`

The strongest within-class pair is:

- **Q 18:110 ↔ Q 41:6**, residual Jaccard = **1.00**

after stripping `innama`, both continue as tightly aligned messenger /
revelation declarations.

### What does NOT survive

The large visible families do not survive the stricter test:

- `qul ya ...` is descriptively obvious but not residual-coherent once
  `ya` (and `ayyuhā` when present) is removed
- interrogative / challenge openers are numerous, but as a bundle they
  are too heterogeneous after opener stripping
- the self / devotional bucket mixes prayer, refuge, and prophetic
  self-description, and lands **below** the matched-null mean

This matters. [[h-new-269-qul-addressee-pattern|H-NEW-269]] is not denying that these opener families are
real at the surface. It says they do **not** become validated residual
classes under this particular locked continuation test.

## MW-5 positive control

Feasible control:

- `qul a-ra'aytum / a-ra'aytakum ...`
- `n = 13`

Same machinery, same 6-word residual-root window, same matched null.

| Control | n | Observed | Null mean | Null q95 | z | p_perm | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| `ARAYTUM` family | 13 | **0.1596** | 0.0409 | 0.0742 | **+6.622** | **0.0002** | PASS |

MW-5 therefore validates the instrument. The pipeline can recover a
real repeated `qul` continuation-template after opener stripping. The
three null cells are interpretable nulls, not a broken test.

## Interpretation

The conservative reading is:

- the `qul` corpus visibly contains several opener families
- but most of those families do **not** persist as short-range residual
  lexical classes once the opener marker is removed
- the main exception is the **restrictive `innama` declaration**
  register

So the answer to the headline question is not "no classes at all" and
not "many robust classes." It is:

**one narrow rhetorical class is recoverable beyond raw frequency;
broader addressee-pattern taxonomies are not supported by this locked
test.**

## Honest limits

- The class family is opener-visible and deliberately coarse. This is a
  validation test, not an unsupervised discovery pipeline.
- The residual window is only **6 words**. Some downstream addressee
  cues fall later in the verse.
- Root-set Jaccard ignores word order and multiplicity.
- The `SELF_OR_DEVOTIONAL` bucket is heterogeneous by design; a future
  split into prayer vs messenger self-description would require a new
  preregistration.
- `OTHER` is large (**215 tokens**) and was not subdivided here.
- A few verses contain multiple `qul` tokens, so token windows are not
  perfectly independent.

## Bottom line

`[[h-new-269-qul-addressee-pattern|H-NEW-269]]` lands as **PARTIAL-CLASS-ONLY**.

The broad claim "the `qul` corpus contains several distinct residual
addressee/rhetorical classes beyond opener frequency" is **not**
supported. The narrower claim

> **`qul innama ...` forms a real residual rhetorical class**

**is supported** under the locked matched-null test, with MW-5 positive
control passing strongly.
