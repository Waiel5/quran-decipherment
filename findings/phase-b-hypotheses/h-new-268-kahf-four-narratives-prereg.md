---
id: H-NEW-268
title: Q18 Al-Kahf four-narrative structural spacing test
phase: B
status: PRE-REGISTERED
registered: 2026-04-18
script: scripts/h_new_268_kahf_four_narratives.py
data_out: findings/phase-b-hypotheses/csv/h-new-268.json
bonferroni_k: 3
alpha: 0.05
alpha_bon: 0.0166666667
rules_tuple: "(Q18 only; 110 verses; four locked narrative blocks 9-26 / 32-44 / 60-82 / 83-98; ordered-placement exact null with fixed lengths 18/13/23/16)"
direction_primary: "POSITIVE — the four narrative starts exhibit a palindromic-expansion spacing pattern stronger than ordered placement alone would predict."
---

# [[h-new-268-kahf-four-narratives|H-NEW-268]] — Q18 Al-Kahf four-narrative structural spacing test

## Motivation

The project already has strong qualitative and mixed quantitative
evidence on Al-Kahf:

- the classical four-trials reading (faith / wealth / knowledge /
  power),
- [[h-new-90-kahf-narrative-structure|H-NEW-90]]'s weak lexical-parallelism result,
- the Kahf deep-dive's observation that the surah's four main
  narratives are separated by visible interludes and that the last two
  narratives are tightly contiguous.

What is still untested is a much narrower claim: whether the **verse
spacing** of the four main narrative blocks shows a concrete,
pre-specifiable symmetry pattern. This finding therefore ignores lexical
content and tests only a bounded geometric claim over the four locked
block ranges.

## Locked block boundaries

Per the prior Kahf workstream's modal/classical framing, the four main
narrative blocks are frozen as:

1. Sleepers of the Cave: **18:9-26** (18 verses)
2. Two Gardens parable: **18:32-44** (13 verses)
3. Moses and al-Khiḍr: **18:60-82** (23 verses)
4. Dhū l-Qarnayn: **18:83-98** (16 verses)

Excluded interludes / frame material are therefore:

- 18:1-8
- 18:27-31
- 18:45-59
- 18:99-110

No boundary expansion or contraction is permitted in this run.

## Observable

Let narrative starts be `s1 < s2 < s3 < s4`. Define the three
start-to-start arc lengths:

- `d1 = s2 - s1`
- `d2 = s3 - s2`
- `d3 = s4 - s3`

For the locked Q18 boundaries these are expected to be:

- observed tuple = `(23, 28, 23)`

The concrete symmetry claim is the **palindromic-expansion pattern**
`d1 = d3 < d2`, i.e. equal outer arcs with a wider central arc.

## Null model (frozen)

The null is an **ordered-placement exact null**:

- keep the four narrative lengths fixed at `(18, 13, 23, 16)`,
- keep their order fixed,
- place them anywhere inside a 110-verse surah subject only to
  non-overlap and staying within 1..110.

Equivalently: distribute the residual `110 - (18 + 13 + 23 + 16) = 40`
verses across 5 non-negative gap slots:

- before block 1,
- between blocks 1/2,
- between blocks 2/3,
- between blocks 3/4,
- after block 4.

This yields an exact finite state space of `C(44, 4) = 135,751`
placements. The script will enumerate all 135,751; no Monte Carlo
approximation is needed.

Uniform weighting over these placements is locked.

## Primary test family (Bonferroni k = 3)

Family-wise alpha = 0.05. Per-cell alpha:

- `alpha_bon = 0.05 / 3 = 0.0166666667`

### Cell A — outer-arc equality

Hypothesis: `d1 = d3` occurs less often than chance under the ordered
placement null.

Statistic: indicator `[d1 = d3]`.

One-sided exact p-value:

- `p_A = P_null(d1 = d3)`

PASS rule: `p_A < alpha_bon`.

### Cell B — central arc widest

Hypothesis: the middle start-gap is strictly the widest arc.

Statistic: indicator `[d2 > max(d1, d3)]`.

One-sided exact p-value:

- `p_B = P_null(d2 > max(d1, d3))`

PASS rule: `p_B < alpha_bon`.

### Cell C — joint palindromic-expansion shape

Hypothesis: the full spacing shape `d1 = d3 < d2` is rare under the
ordered placement null.

Statistic: indicator `[d1 = d3 and d2 > d1]`.

One-sided exact p-value:

- `p_C = P_null(d1 = d3 < d2)`

PASS rule: `p_C < alpha_bon`.

## Descriptive outputs (non-inferential)

The script may additionally report, descriptively only:

- the exact frequency of the observed tuple `(23, 28, 23)`,
- observed gap-slot decomposition,
- null means for `|d1 - d3|` and `d2`,
- a word/letter-count note if easily derived from existing verse-level
  files.

These descriptives are not part of the Bonferroni family.

## Verdict mapping

- 0/3 PASS: **NULL**
- 1/3 PASS: **DIMENSION-SPECIFIC**
- 2/3 PASS: **PASS-DIRECTED**
- 3/3 PASS: **STRONG PASS**

## MW-5 positive control

Use a planted symmetric arrangement in the same 110-verse frame with the
same block lengths and zero outer padding:

- gap slots = `(0, 5, 35, 0, 0)`
- starts = `(1, 24, 72, 95)`
- start-gap tuple = `(23, 48, 23)`

This planted case should satisfy all three shape indicators and be
reported by the script as an obvious positive-control hit. The MW is
diagnostic only; it is not part of the Bonferroni family.

## Garden-of-forking-paths log

- I chose **start-to-start arc lengths** rather than block centers,
  ends, or word-mass centroids because the visible candidate structure
  in the locked ranges is a spacing claim, not a content claim.
- I froze a **small 3-cell family** rather than a larger menu of
  geometric scores to keep the test bounded.
- I used the simplest exact null consistent with the wording of the
  claim: ordered placement with fixed block lengths inside Q18's 110
  verses. No literary-weighting or "plausibility" weighting is allowed.
- The exact observed tuple `(23, 28, 23)` is allowed as a descriptive
  output only; the inferential family is defined by the broader shape
  predicates above.

## Honest limits (stated before run)

- This is a **spacing** test only. It does not test lexical overlap,
  ring composition, thematic parallelism, or classical exegesis in
  general.
- The result will depend on the locked four-block segmentation.
  Alternative boundary theories would require a new pre-reg.
- The uniform ordered-placement null is intentionally austere. It does
  not model rhetorical preferences for openings, middles, or closings.
- The four-block geometry is visible once the boundaries are fixed; this
  is not a blind corpus scan. Any positive result should therefore be
  framed as a bounded spacing signature, not as a complete theory of
  Al-Kahf.

## Deliverables

1. This pre-reg
2. `scripts/h_new_268_kahf_four_narratives.py`
3. `findings/phase-b-hypotheses/csv/h-new-268.json`
4. `findings/phase-b-hypotheses/h-new-268-kahf-four-narratives.md`
5. `journal/h-new-268-run-1.md`

-- end pre-reg --
