---
finding_id: h-new-132
title: "Q7 Al-A'raf vs Q11 Hud prophet-cycle parallelism"
date: 2026-04-18
status: PARTIAL-PASS
pre_reg: findings/phase-b-hypotheses/h-new-132-prophet-cycle-parallelism-prereg.md
seed: 20260418
bonferroni_k: 2
bonferroni_family: h-new-132-q7-q11-prophet-cycle
alpha_bon: 0.025
rules_tuple: (QAC-v0.4 morphology roots; POS!=PN for primary/secondary, POS=PN lemmas for positive control; Hafs-Kufan verse numbering; basmala counted only in Surah 1; Fisher-Rao arccos-Bhattacharyya on L1-normalized window distributions; exact 5! assignment null)
---

# [[h-new-132-prophet-cycle-parallelism|H-NEW-132]] — Q7 Al-A'raf vs Q11 Hud prophet-cycle parallelism

## Headline

**The shared five-prophet cycle in Q7 and Q11 is assignment-recoverable, but
not cleanly nearest-neighbor recoverable once prophet names are removed.**

Using PN-stripped QAC root distributions on the five shared prophet blocks
(Noah, Hud, Salih, Lot, Shuayb), the canonical Q7 <-> Q11 mapping is the
**unique minimum** among all `5! = 120` bijections:

- `p_primary = 1/120 = 0.00833`
- diagonal mean Fisher-Rao distance = **0.7186**
- off-diagonal mean Fisher-Rao distance = **0.7760**
- mean gap = **0.0575**

But the stricter row-wise nearest-neighbor criterion fails:

- observed recovery = **2/5**
- exact `p_secondary = 0.200`

Per the pre-registered verdict map, this is a **PARTIAL-PASS**.

## Why this is only partial

The primary test enforces a **one-to-one assignment** across the full 5x5
matrix. Under that criterion, the canonical prophet order wins outright. The
runner-up differs only by swapping **Noah <-> Hud**, and even that worse fit is
still larger by only **0.0223** distance units.

The secondary test drops the one-to-one constraint and asks whether each Q7
block's *single closest* Q11 block is its canonical counterpart. That does **not**
happen. Four rows collapse toward the Q11 **Salih** block:

- Noah -> Salih
- Hud -> Salih
- Salih -> Salih
- Lot -> Lot
- Shuayb -> Salih

So the signal is real at the **cycle-assignment** level, but not at the
**row-wise unique fingerprint** level. Q11 Salih behaves like a centroid-like
formulaic block that attracts multiple Q7 rows once one-to-one matching is
removed.

## Pre-registered windows

### Q7 Al-A'raf

- Noah: 7:59-64
- Hud: 7:65-72
- Salih: 7:73-79
- Lot: 7:80-84
- Shuayb: 7:85-93

### Q11 Hud

- Noah: 11:25-49
- Hud: 11:50-60
- Salih: 11:61-68
- Lot: 11:77-83
- Shuayb: 11:84-95

Moses was excluded in advance because Q11:96-99 is only a short coda, not a
scale-matched counterpart to Q7:103-160.

## Results

### Primary — exact assignment on PN-stripped root distributions

| Quantity | Value |
|---|---:|
| Number of shared blocks | 5 |
| Number of bijections | 120 |
| Observed canonical sum-distance | **3.5928** |
| Rank among all assignments | **1 / 120** |
| Assignments with sum-distance <= observed | **1** |
| Exact one-sided p | **0.00833** |
| Bonferroni alpha | 0.025 |
| **Primary pass** | **Yes** |

### Canonical diagonal distances

| Prophet | Q7 <-> Q11 distance |
|---|---:|
| Noah | 0.7782 |
| Hud | 0.7331 |
| Salih | **0.6226** |
| Lot | 0.6693 |
| Shuayb | 0.7896 |

Salih is the tightest matched pair; Shuayb and Noah are the loosest.

### Distance matrix

| Q7 row \\ Q11 col | Noah | Hud | Salih | Lot | Shuayb |
|---|---:|---:|---:|---:|---:|
| Noah | 0.7782 | 0.6748 | **0.6537** | 0.6607 | 0.7246 |
| Hud | 0.8588 | 0.7331 | **0.6779** | 0.7494 | 0.7960 |
| Salih | 0.8955 | 0.7190 | **0.6226** | 0.7545 | 0.7791 |
| Lot | 0.8803 | 0.8015 | 0.7215 | **0.6693** | 0.7909 |
| Shuayb | 0.9206 | 0.7953 | **0.7788** | 0.8878 | 0.7896 |

This table shows exactly why the two cells split: the diagonal is globally best
as a bijection, but several rows have a smaller local distance to Q11 Salih
than to their own canonical counterpart.

### Secondary — row-wise nearest-neighbor recovery

| Quantity | Value |
|---|---:|
| Observed hits | **2 / 5** |
| Exact p | **0.2000** |
| Bonferroni alpha | 0.025 |
| **Secondary pass** | **No** |

Correct rows: **Salih, Lot**

Missed rows: **Noah, Hud, Shuayb**

### Positive control — PN-only exact assignment

| Quantity | Value |
|---|---:|
| Observed canonical sum-distance | **2.7870** |
| Rank among all assignments | **1 / 120** |
| Exact p | **0.00833** |
| Margin to runner-up | **0.4815** |
| **Positive control** | **PASS** |

The pipeline is therefore functioning correctly. The weak row-wise recovery is
not an extraction bug; it is a property of the PN-stripped root geometry.

## Interpretation

This is a narrower and more successful follow-up than the broad [[h-new-197-prophet-cycle|H-NEW-197]]
"shared sequential template across all prophet retellings" test, which went
NULL. [[h-new-132-prophet-cycle-parallelism|H-NEW-132]] says:

- **Yes**: Q7 and Q11 share enough whole-cycle structure that the canonical
  five-block assignment is uniquely recoverable without prophet names.
- **No**: that structure is not sharp enough for each block to be its own clean
  nearest neighbor after PN stripping.

The most plausible reading is that these two surahs share a **family-level
prophet-cycle diction**, but several of the blocks remain highly formulaic and
therefore partially interchangeable at the local row level. Q11 Salih appears
to be the most centroid-like of the five.

## Honest limits

1. **The primary is distributional, not sequential.** It tests root-distribution
   assignment, not verse-order template alignment. That broader sequential claim
   remains unconfirmed by [[h-new-197-prophet-cycle|H-NEW-197]].

2. **Lot is asymmetric by construction.** Q11 Lot is embedded after the
   Abraham-guest transition, while Q7 Lot is a short self-contained rebuke. This
   was disclosed in advance and not repaired post hoc.

3. **Generic prophet-cycle diction remains in the feature space.** We removed
   PN tokens, but not generic roots like `qwl`, `qwm`, `rbb`, `Ebd`, `kwn`.
   That is a legitimate part of the diction, but it also explains why one block
   can become a centroid.

4. **The margin is real but not huge.** The runner-up swaps Noah and Hud and is
   only **0.0223** worse than canonical. This is enough for exact significance
   at `1/120`, but it is not a massive separation.

## Verdict

**PARTIAL-PASS.** The canonical Q7/Q11 prophet-cycle mapping is uniquely
recoverable under the pre-registered exact assignment test, but the stronger
row-wise nearest-neighbor recovery criterion fails.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-132-prophet-cycle-parallelism-prereg.md`
- Script: `scripts/h_new_132_prophet_cycle_parallelism.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-132.json`
- Journal: `journal/h-new-132-run-1.md`
