---
id: H-NEW-269
title: "qul imperative addressee-pattern test"
status: PRE-REGISTERED 2026-04-18
spec_locked_at: 2026-04-18
bonferroni_family: h-new-269-qul-addressee-pattern
bonferroni_k: 4
alpha_bon: 0.0125
seed: 20260418
n_perm: 5000
window_words_after_strip: 6
rules_tuple: "(332 canonical qul tokens from Leeds QAC v0.4; no-tashkeel normalized token windows; QAC STEM roots; opener-family stripping; matched nonclass qul null on residual 6-word root mass)"
prior_work_consulted:
  - findings/phase-b-hypotheses/h-new-74-qul-distribution.md
  - findings/phase-b-hypotheses/quotation-analysis.md
  - journal/imperative-run-1.md
author: h-new-269-specialist
---

# [[h-new-269-qul-addressee-pattern|H-NEW-269]] — qul imperative addressee-pattern test

## Question

Among the **332 canonical `qul` imperatives** (`POS:V`, `IMPV`,
`LEM:qaAla`, `2MS`), do a few coarse **quoted-speech addressee or
rhetorical-context families** remain coherent **after their trivial
opener-marker is stripped away**, or are the apparent classes mostly
just raw opener-frequency artifacts?

This is intentionally narrow. It does **not** attempt a full discourse
parser for the `qul` corpus. It asks a smaller empirical question:
if we lock a few obvious opener families in advance, do any of them
still behave like real classes once the family label itself is removed?

## Provenance disclosure

This finding is **not blind** to the existence of obvious `qul`
openers. Prior descriptive work already surfaced repeated families such
as:

- `qul ya ...`
- `qul a-ra'aytum ...`
- `qul innama ...`
- `qul inni ...` / `qul rabbi ...`

That descriptive visibility is exactly why this test is framed as a
**conservative follow-up**. The inferential claim is not "these openers
exist" but the stricter question:

> after stripping the opener token that defines the family, is the
> immediate continuation still more coherent than matched random `qul`
> continuations?

If not, the family is treated as a **frequency phenomenon only**.

## Data and unit of analysis

- Morphology / roots:
  `data/morphology/quranic-corpus-morphology-0.4.txt`
- Surface token windows:
  `quran-text/quran-no-tashkeel.json`
- Unit: **individual `qul` tokens**, not unique verses

The token-level unit is locked because the question concerns the 332
imperatives themselves. If multiple `qul` tokens occur in the same
verse, each is retained as a separate token-window.

## Canonical `qul` filter

Keep only QAC segment-lines satisfying all four conditions:

- `POS:V`
- `IMPV`
- `LEM:qaAla`
- `2MS`

Expected total from prior work: **332** tokens.

## Locked class family

Classification uses the **first normalized token after `qul`** in the
same verse.

Four inferential classes are locked:

### Cell A — `VOCATIVE_ADDRESS`

Condition:

- first token after `qul` is `يا`

Strip rule:

- strip `يا`
- if the next token is `ايها`, strip that too

Interpretation:

- explicit downstream addressee in the dictated speech

### Cell B — `INTERROGATIVE_OR_CHALLENGE`

Condition: first token after `qul` is one of

- `من`
- `ما`
- `هل`
- `ارايتم`
- `ارايتكم`
- `هاتوا`
- `فاتوا`
- `اغير`
- `افلا`

Strip rule:

- strip the first token only

Interpretation:

- rhetorical question, challenge, or confession-trap opening

### Cell C — `SELF_OR_DEVOTIONAL`

Condition: first token after `qul` is one of

- `اني`
- `انني`
- `انا`
- `رب`
- `ربي`
- `اعوذ`
- `اللهم`
- `حسبي`

Strip rule:

- strip the first token only

Interpretation:

- prophetic self-positioning, prayer, refuge, or delegated first-person
  declaration

### Cell D — `RESTRICTIVE_DECLARATION`

Condition:

- first token after `qul` is `انما`

Strip rule:

- strip the first token only

Interpretation:

- restrictive / exclusivizing declaration

### Descriptive residue

All remaining `qul` tokens are assigned to `OTHER`.

`OTHER` is reported descriptively only and is **not** an inferential
cell.

## Residual window (locked)

For every `qul` token:

1. identify the class-specific opener tokens to strip
2. after stripping, keep the **next up to 6 words** in the same verse
3. convert those words to a **set of QAC STEM roots**

This 6-word window is intentionally local. It asks whether the opener
family persists into the immediate continuation, not whether the entire
verse or surah belongs to a global semantic theme.

## Statistic (all four cells)

For each cell, compute:

`T = mean pairwise Jaccard(root_set_i, root_set_j)`

across all within-class token pairs.

Direction for every inferential cell: **one-sided upper**.

Interpretation:

- high `T` means the class remains lexically coherent even after its
  trivial opener token has been stripped

## Null model (locked)

For each class separately:

1. let `n_class` be the number of class members
2. let the candidate pool be **all non-class `qul` tokens**
3. for every class member, compute its residual 6-word STEM-token mass
4. rank pool tokens by:
   - absolute difference in `log(mass + 1)`
   - then absolute difference in raw mass
   - then token index
5. keep the nearest `max(40, 2 * n_class)` pool tokens as that member's
   candidate list
6. one null draw samples one candidate for each class member,
   **without replacement**, greedily resolving the most constrained slot
   first
7. compute the same `T`

Repeat `N_PERM = 5000` times per cell.

### Why this null

The raw family-defining signal lives in the first token. The null
therefore does **not** randomize the opener labels themselves; instead,
it asks whether the **residual continuation** is more coherent than
random `qul` continuations of similar short-window mass.

This is the literal operationalization of "beyond raw frequency".

## MW-1 length control

MW-1 is handled at the null level by matching on the exact residual
6-word STEM-token mass used by the statistic. No extra residualization
is applied.

## MW-5 positive control (locked)

Feasible control:

- tokens whose first token after `qul` is `ارايتم` or `ارايتكم`

Rationale:

- this is an already-visible repeated `qul` template
- it uses the same token-level unit, same opener-stripping logic, same
  residual-root Jaccard statistic, and same matched-null machinery
- if this narrow counterfactual family does **not** register as coherent
  after stripping its opener, the instrument is not sensitive enough for
  the present task

MW-5 procedure:

- strip the first token (`ارايتم` / `ارايتكم`)
- keep the next up to 6 words
- compare mean pairwise root-set Jaccard against matched non-control
  `qul` tokens under the same null machinery

**MW-5 pass rule**:

- empirical upper-tail `p_perm < 0.05`

If MW-5 fails, `[[h-new-269-qul-addressee-pattern|H-NEW-269]]` is reported as `NULL-BROKEN`.

## Bonferroni family and decision rule

Inferential family size:

- `k = 4`
- `alpha_bon = 0.05 / 4 = 0.0125`

Per-cell verdict:

- PASS iff `p_perm < 0.0125`

Overall verdict:

- MW-5 fail -> `NULL-BROKEN`
- 0/4 PASS with MW-5 valid -> `NULL`
- 1/4 PASS with MW-5 valid -> `PARTIAL-CLASS-ONLY`
- 2-4/4 PASS with MW-5 valid -> `PASS-DIRECTED`

Interpretation discipline:

- `PASS-DIRECTED` means multiple opener families remain coherent beyond
  their opener token
- `PARTIAL-CLASS-ONLY` means one narrow family survives but the corpus
  does not support a broad multi-class taxonomy under this design
- `NULL` means the family structure is mostly opener-frequency only at
  this resolution

## Descriptive outputs allowed

The script may also report descriptively:

- class counts and shares
- class unique-verse counts
- top first tokens after `qul`
- top within-class token pairs by residual Jaccard
- example members of each class

These descriptive rows do **not** add inferential cells or change the
Bonferroni family.

## What will NOT be changed after lock

- no fifth inferential class
- no switch from token-level to verse-level unit
- no widening from 6-word window to whole-verse or whole-surah window
- no alternate similarity metric
- no null built from unrestricted random draws
- no post-hoc split of the `OTHER` residue
- no replacing the MW-5 control with a different family

## Honest limits

1. **Class family is coarse and opener-visible.** This is deliberate.
   The test is about residual coherence after opener stripping, not a
   hidden-class discovery problem.
2. **Six words is a narrow window.** Some later addressee cues or
   theological payloads fall outside the retained window.
3. **Root-set Jaccard ignores order and multiplicity.** It is a
   conservative lexical-coherence measure, not a discourse parser.
4. **Cells are correlated.** All four use the same `qul` corpus and the
   same residual-root machinery. Bonferroni is conservative.
5. **Same-verse dependence remains.** A few verses contain multiple
   `qul` tokens, so token windows are not fully independent.
6. **A positive result would still be bounded.** Even 2-4 passing cells
   would support only these locked opener families, not a full rhetoric
   of the `qul` corpus.
