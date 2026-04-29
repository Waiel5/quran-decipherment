---
id: H-NEW-265
title: "v1-w1 qul-openers micro-cluster — opener-stripped coherence test"
status: NULL — 0/3 Bonferroni cells PASS; MW-5 positive control valid on all 3 cells
date: 2026-04-18
agent: h-new-265-specialist
prereg: findings/phase-b-hypotheses/h-new-265-qul-openers-microcluster-prereg.md
script: scripts/h_new_265_qul_openers_microcluster.py
json: findings/phase-b-hypotheses/csv/h-new-265.json
journal: journal/h-new-265-run-1.md
seed: 20260418
n_perm: 10000
bonferroni_family: h-new-265-qul-openers-microcluster
bonferroni_k: 3
alpha_bon: 0.0167
rules_tuple: "(QAC STEM roots; target = Q72/Q109/Q112/Q113/Q114; opener-stripped windows; per-cell token-mass-matched null; MW-5 = musabbiḥāt inner-5)"
---

# [[h-new-265-qul-openers-microcluster|H-NEW-265]] — v1-w1 qul-openers micro-cluster

## Headline

The five v1-w1 `qul`-openers — **Q 72, Q 109, Q 112, Q 113, Q 114** —
do **not** survive as a coherent lexical micro-cluster once the trivial
shared opener is stripped away and the null is matched on the actual
token mass used by each cell.

Under the locked [[h-new-265-qul-openers-microcluster|H-NEW-265]] design:

- **0/3** opener-stripped cells pass Bonferroni
  (`alpha_bon = 0.0167`)
- **MW-5 passes on all 3 cells** using the musabbiḥāt inner-5
  `{57,59,61,62,64}` at nominal `p = 0.0001` each

So the clean answer to the bounded question is:

**No evidence that the `qul` quintet forms a stable structural family
beyond the bare shared opener itself.**

## Primary results

### Target set

`QUL_5 = {72, 109, 112, 113, 114}`

Statistic in every cell:

- mean pairwise root-set Jaccard across the 10 within-set surah pairs
- one-sided upper test against a 10,000-draw matched 5-set null

### Three locked cells

| Cell | Operationalization | Observed | Null mean | z | p_perm | Bonferroni verdict |
|---|---|---:|---:|---:|---:|---|
| A | v1 residual roots after dropping w1 | 0.0500 | 0.0133 | +2.14 | 0.0579 | NULL |
| B | v1-v3 residual roots after dropping v1-w1 | 0.0512 | 0.0227 | +1.54 | 0.0702 | NULL |
| C | whole-surah roots excluding trivial opener root `qwl` | 0.0379 | 0.0259 | +1.18 | 0.0975 | NULL |

No cell reaches `0.0167`. Overall verdict: **NULL**.

## What the pairwise structure actually looks like

The quintet does not behave like a 5-way family. Its limited overlap
collapses almost entirely to the already-known **muʿawwidhatān pair**
Q 113 + Q 114:

- **Cell A**: Q 113 ↔ Q 114 = `0.50`; all other 9 pairs = `0.00`
- **Cell B**: Q 113 ↔ Q 114 = `0.20`; next-best Q 112 ↔ Q 114 = `0.125`
- **Cell C**: Q 113 ↔ Q 114 = `0.176`; next-best Q 112 ↔ Q 114 = `0.067`

Q 72 is the main spoiler. Once `qul` itself is removed, Q 72's lexical
continuation and full-surah root inventory do not align with the four
short tail surahs strongly enough to produce a 5-way micro-cluster.

So [[h-new-265-qul-openers-microcluster|H-NEW-265]] does **not** deny that there is a local family inside the
set. It says the family is **not the full quintet** under this stricter,
opener-stripped operationalization.

## MW-5 positive control

Positive control set:

- `MUSABBIHAT_INNER_5 = {57, 59, 61, 62, 64}`

The control was tested under the **same stripped logic**:

- Cells A and B drop the literal first word
- Cell C removes the trivial opener-root `sbH`

### MW-5 results

| Cell | Control observed | Control null mean | p_perm | Verdict |
|---|---:|---:|---:|---|
| A | 0.6406 | 0.0392 | 0.0001 | PASS |
| B | 0.1866 | 0.0699 | 0.0001 | PASS |
| C | 0.2497 | 0.1625 | 0.0001 | PASS |

This matters. The instrument can detect a real opener-family **after**
the opener itself is stripped. The `qul` quintet's 0/3 is therefore a
validated null, not a broken pipeline.

## Interpretation

[[h-new-74-qul-distribution|H-NEW-74]] remains correct at its own level:
**{72,109,112,113,114} is the exact v1-w1 `qul` opener set**.

[[h-new-265-qul-openers-microcluster|H-NEW-265]] adds a scope limit:

- As a **literal opener inventory**, the quintet is real.
- As an **opener-stripped structural family**, the quintet is not
  supported.

The strongest surviving substructure is the expected short-tail refuge
pair **Q 113 + Q 114**, with some weaker spillover to Q 112. Q 109 and
especially Q 72 do not stay close enough to upgrade the five surahs into
a unified lexical micro-cluster.

In short:

**the shared opener is exact; the deeper five-way family is not.**

## Honest limits

- All three cells are lexical-root Jaccard variants at different scales,
  so they are correlated. Effective independent evidence is less than 3.
- The matched null uses a transparent but still heuristic rule:
  nearest-12 by log token mass within each cell.
- This finding tests only a lexical opener-stripped family. It does not
  adjudicate liturgical, hadith, or recitational familyhood.
- Because the target set was already known from [[h-new-74-qul-distribution|H-NEW-74]], a positive
  result here would have been capped at **PASS-DIRECTED**. The present
  null does not require that distinction for the verdict.

## Verdict

**NULL.** [[h-new-265-qul-openers-microcluster|H-NEW-265]] finds **0/3** Bonferroni-significant cells for the
five v1-w1 `qul`-openers after opener stripping, while MW-5 passes on
all three cells. The formal answer to the bounded question is:

**these five surahs do not form a coherent structural family beyond the
trivial shared opener under the locked lexical micro-cluster test.**
