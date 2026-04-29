---
id: H-NEW-268
title: Q18 Al-Kahf four-narrative structural spacing test
phase: B
status: PUBLISHED 2026-04-18 (run-1)
parent_prereg: h-new-268-kahf-four-narratives-prereg.md
script: scripts/h_new_268_kahf_four_narratives.py
data_json: findings/phase-b-hypotheses/csv/h-new-268.json
---

# [[h-new-268-kahf-four-narratives|H-NEW-268]] — Q18 Al-Kahf four-narrative structural spacing test

## Headline

Using the locked four-block segmentation of Al-Kahf

- 18:9-26
- 18:32-44
- 18:60-82
- 18:83-98

the four narrative starts fall at **9, 32, 60, 83**, producing the
start-gap tuple **(23, 28, 23)**.

Under the exact ordered-placement null over all **135,751** placements
of blocks with the same verse lengths `(18, 13, 23, 16)` inside a
110-verse surah, the joint **palindromic-expansion** shape
`d1 = d3 < d2` occurs in **1089 / 135,751 = 0.00802** of placements.
That survives the locked Bonferroni-3 threshold
`alpha_bon = 0.01667`.

The simpler component claims do **not** survive:

- outer equality alone: `p = 0.03233`
- middle-widest alone: `p = 0.13341`

**Verdict: DIMENSION-SPECIFIC.** There is a real small-large-small
spacing signature in the verse-index geometry of the four Q18 narrative
starts, but this is **not** a full confirmation of broad four-way
symmetry.

## Numbers

### Locked geometry

| block | verses | length | words | letters |
|---|---:|---:|---:|---:|
| Sleepers | 9-26 | 18 | 336 | 1412 |
| Gardens | 32-44 | 13 | 168 | 656 |
| Moses-Khiḍr | 60-82 | 23 | 302 | 1213 |
| Dhū l-Qarnayn | 83-98 | 16 | 186 | 703 |

Observed gap-slot decomposition:

- before block 1: **8** verses
- between 1 and 2: **5**
- between 2 and 3: **15**
- between 3 and 4: **0**
- after block 4: **12**

This yields the observed start-gap tuple:

- `d1 = 32 - 9 = 23`
- `d2 = 60 - 32 = 28`
- `d3 = 83 - 60 = 23`

### Primary family (Bonferroni k = 3)

| Cell | Claim | Observed | Exact p | Pass? |
|---|---|---:|---:|---:|
| A | outer arcs equal (`d1 = d3`) | yes | **0.03233** | no |
| B | middle arc widest (`d2 > max(d1,d3)`) | yes | **0.13341** | no |
| C | joint palindromic-expansion (`d1 = d3 < d2`) | yes | **0.00802** | **yes** |

Null descriptives:

- total placements: **135,751**
- residual gap verses: **40**
- null mean outer-gap difference `|d1-d3|`: **9.53**
- null mean middle gap `d2`: **21.0**

### Descriptive only

The exact observed tuple **(23, 28, 23)** occurs in only
**21 / 135,751 = 0.0001547** placements. This number is descriptive,
not part of the pre-registered Bonferroni family.

### MW-5 positive control

The planted symmetric arrangement with gap slots `(0, 5, 35, 0, 0)`
produces starts `(1, 24, 72, 95)` and the tuple **(23, 48, 23)**.

- Cell A: true
- Cell B: true
- Cell C: true
- exact tuple frequency: **1 / 135,751 = 7.37e-06**

The positive control therefore fires as expected.

## Interpretation

This finding is best read as a **bounded spacing result**.
The four narrative starts in Al-Kahf are not just "roughly spread out";
they instantiate a specific **small-large-small** arc pattern with
equal outer spans and an expanded middle span.

What the result does **not** show:

- it does not prove lexical parallelism across the four narratives,
- it does not prove a global ring structure across all four blocks,
- it does not overturn [[h-new-90-kahf-narrative-structure|H-NEW-90]]'s weak/negative lexical-parallelism
  result.

Instead, [[h-new-268-kahf-four-narratives|H-NEW-268]] complements [[h-new-90-kahf-narrative-structure|H-NEW-90]]. The earlier test said the four
stories are **not unusually lexically parallel**. This test says their
**start positions** nevertheless exhibit a real, nontrivial geometric
regularity under a tightly-defined null.

The mechanism is visible from the locked lengths and interludes:

- block 1 plus its following interlude gives `18 + 5 = 23`
- block 2 plus its following interlude gives `13 + 15 = 28`
- block 3 plus its following gap gives `23 + 0 = 23`

So the symmetric outer spacing is achieved not by equal block lengths,
but by compensatory placement of the interludes.

## Honest limits

- This is a **verse-index** test only. No lexical, rhetorical, or
  thematic measure enters the null.
- The result depends on the locked four-block segmentation. Alternative
  boundary theories would require a new pre-reg.
- The null is intentionally austere: all ordered placements consistent
  with the same four lengths are weighted equally.
- The geometry becomes visible once the block ranges are fixed, so this
  should be framed as a bounded structural signature, not as a blind
  discovery of hidden architecture.
- Because only **1 of 3** Bonferroni cells passes, the correct label is
  **DIMENSION-SPECIFIC**, not a stronger symmetry verdict.

## Connections

- **[[h-new-90-kahf-narrative-structure|H-NEW-90]]**: complements the earlier weak lexical-parallelism result.
  Q18's four narratives need not be lexically parallel in order to show
  spacing regularity.
- **Al-Kahf deep-dive**: gives the literary backdrop for the four-trials
  framing and for treating 18:9-26 / 32-44 / 60-82 / 83-98 as the main
  narrative blocks.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-268-kahf-four-narratives-prereg.md`
- Script: `scripts/h_new_268_kahf_four_narratives.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-268.json`
- Journal: `journal/h-new-268-run-1.md`
