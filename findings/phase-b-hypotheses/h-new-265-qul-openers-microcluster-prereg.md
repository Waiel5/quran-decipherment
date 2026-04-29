---
id: H-NEW-265
title: "v1-w1 qul-openers micro-cluster — opener-stripped coherence test"
status: PRE-REGISTERED 2026-04-18
spec_locked_at: 2026-04-18
bonferroni_family: h-new-265-qul-openers-microcluster
bonferroni_k: 3
alpha_bon: 0.0167
seed: 20260418
n_perm: 10000
match_k_nearest: 12
rules_tuple: "(Hafs-Kufan Quran; Leeds QAC v0.4 STEM roots; target set fixed from H-NEW-74 Cell 3; opener-stripped lexical windows; per-cell token-mass-matched 5-set null)"
prior_work_consulted:
  - findings/phase-b-hypotheses/h-new-74-qul-distribution.md
  - findings/phase-b-hypotheses/cross-finding-010-extended-network.md
  - findings/phase-b-hypotheses/h-new-103-musabbihat-4form.md
author: h-new-265-specialist
---

# [[h-new-265-qul-openers-microcluster|H-NEW-265]] — v1-w1 qul-openers micro-cluster

## Question

Do the five surahs whose very first word is `qul` —
**{Q 72, Q 109, Q 112, Q 113, Q 114}** — form a coherent structural
family **once the trivial shared opener itself is stripped away**?

This is intentionally a **tight micro-cluster test**, not a large new
taxonomy. The scope is bounded to three lexical-root cells operating at
three scales:

1. immediate continuation after the opener,
2. early-window continuation in v1-v3,
3. whole-surah content after removing the opener-root.

## Provenance disclosure

The target set is NOT newly discovered here. It was already locked by
[[h-new-74-qul-distribution|H-NEW-74]] Cell 3 as the exact v1-w1 `qul` opener quintet:
{Q 72, 109, 112, 113, 114}. This finding is therefore a **post-hoc
follow-up on a known set**, but with a newly pre-registered
operationalization that asks a narrower question: does the quintet stay
coherent **after stripping the opener itself**?

Consequences:

- The inferential family is locked here before the [[h-new-265-qul-openers-microcluster|H-NEW-265]] run.
- If the family passes, the ceiling is **PASS-DIRECTED**, not
  "confirmed as a new canonical cluster" without replication on a
  different data dimension.
- A null result is still decisive for the bounded question asked here.

## Locked sets

### Target set

`QUL_5 = {72, 109, 112, 113, 114}`

### MW-5 positive control

`MUSABBIHAT_INNER_5 = {57, 59, 61, 62, 64}`

Rationale: this is a known 5-surah opener-family already used elsewhere
in the project. Crucially, it is also appropriate for an
**opener-stripped** test:

- Cells A and B remove the literal first word, so the control is not
  allowed to win merely by sharing `sabbaḥa / yusabbiḥu`.
- Cell C removes the trivial opener-root `sbH` from the control, just as
  it removes `qwl` from the target.

If the control fails under these stripped conditions, the null is too
weak or the instrument is mis-specified.

## Data sources

- Morphology: `data/morphology/quranic-corpus-morphology-0.4.txt`
- Metadata / names / verse counts:
  `quran-text/quran-no-tashkeel.json`

Only QAC STEM roots are used for the inferential cells.

## Locked cells

All three cells use the same set-level statistic:

`T = mean pairwise root-set Jaccard across the 10 within-set surah pairs`

Direction for all three cells: **ONE-SIDED UPPER**
(more lexical coherence than matched random 5-sets).

### Cell A — Immediate-continuation coherence

For each surah:

- take **verse 1 only**
- drop **word 1**
- collect the set of QAC STEM roots remaining in the verse

Example intuition:

- target strips `qul ...`
- control strips `sabbaḥa / yusabbiḥu ...`

Statistic:

- `T_A = mean pairwise Jaccard` over these opener-stripped v1 root sets

### Cell B — Early-window coherence

For each surah:

- take **verses 1-3**
- drop **word 1 of verse 1 only**
- collect the set of QAC STEM roots in that window

Statistic:

- `T_B = mean pairwise Jaccard` over these opener-stripped v1-v3 root sets

This asks whether any family resemblance survives beyond the first line.

### Cell C — Whole-surah coherence beyond the opener-root

For the **target set**, collect the set of all QAC STEM roots in the
surah after excluding root `qwl`.

For the **MW-5 control**, collect the set of all QAC STEM roots in the
surah after excluding root `sbH`.

Statistic:

- `T_C = mean pairwise Jaccard` over these opener-root-stripped whole-surah root sets

This is the broadest cell and the cleanest answer to the question
"beyond the trivial shared opener, is there still a family?"

## Null model (locked)

### Why matched null is required

The target quintet contains four very short surahs and one moderate short
surah (Q 72). Because lexical-root set size is strongly constrained by
available token mass, **MW-1 requires size-matching at the primary-test
level**. An unrestricted random-5 null would overstate coherence for
small-window or short-surah sets.

### Matching rule

For each cell separately:

1. Compute each surah's **cell-specific STEM-token mass**:
   - Cell A: number of STEM tokens in v1 after dropping w1
   - Cell B: number of STEM tokens in v1-v3 after dropping v1-w1
   - Cell C: number of STEM tokens in the full surah after excluding the
     trivial opener-root (`qwl` for target runs, `sbH` for MW-5 runs)
2. For each reference surah `s`, rank all other surahs by:
   - absolute difference in `log(token_mass + 1)`
   - then absolute difference in raw token mass
   - then surah number
3. Keep the **12 nearest** surahs as the match-candidate list for `s`.
4. A null draw samples one candidate for each of the 5 reference surahs,
   **without replacement**, greedily resolving the most constrained slot first.
5. Compute the same `T` statistic on the sampled 5-set.

Repeat `N_PERM = 10,000` times.

This is intentionally simple, local, and auditable. It matches the
window-size actually used by the cell, not an unrelated global length.

## MW-5 rule (locked)

Run the musabbiḥāt inner-5 through the same three cells and their own
cell-specific matched nulls.

**MW-5 PASS criterion**:

- Cell A control p < 0.05
- Cell B control p < 0.05
- Cell C control p < 0.05

If any of the three fail, verdict = **NULL-BROKEN**.

## Bonferroni family and decision rule

Three inferential cells:

- `k = 3`
- `alpha_bon = 0.05 / 3 = 0.0167`

Cell verdict:

- PASS iff `p_perm < 0.0167`

Overall verdict mapping:

- MW-5 fail on any cell -> **NULL-BROKEN**
- 0/3 PASS with MW-5 valid -> **NULL**
- 1/3 PASS with MW-5 valid -> **DIMENSION-SPECIFIC**
- 2-3/3 PASS with MW-5 valid -> **PASS-DIRECTED**

The natural interpretation of a 1/3 result is:
the family is only local to that one scale, not a stable whole-surah
micro-cluster.

## What will NOT be changed after lock

- No extra cells
- No alternate distance metrics
- No unrestricted null as a rescue or replacement
- No redefinition of the five-surah target
- No switch from musabbiḥāt inner-5 to another positive control
- No post-hoc change to `k = 3`

## Honest limits

- The three cells are **correlated** because all are lexical-root based.
  Effective independent evidence is less than 3.
- The matched null uses a heuristic local neighborhood (`k=12 nearest`);
  this is transparent and bounded, but still a design choice.
- The finding does **not** adjudicate recitational or devotional
  familyhood in hadith/tafsir terms. It asks only whether an
  opener-stripped lexical micro-cluster exists.
- Q 72 is much longer than the other four. If the quintet is really a
  "4+1" rather than a unified 5, this design should honestly return
  NULL or at most a local-scale partial.

## Deliverables

1. Script: `scripts/h_new_265_qul_openers_microcluster.py`
2. JSON: `findings/phase-b-hypotheses/csv/h-new-265.json`
3. Findings markdown:
   `findings/phase-b-hypotheses/h-new-265-qul-openers-microcluster.md`
4. Journal: `journal/h-new-265-run-1.md`

## Lock summary

- seed = `20260418`
- perms = `10000`
- Bonferroni `k=3`, `alpha_bon=0.0167`
- target = `{72,109,112,113,114}`
- MW-5 = `{57,59,61,62,64}`
- all cells one-sided upper
- all cells opener-stripped
- all nulls token-mass-matched at the cell level
