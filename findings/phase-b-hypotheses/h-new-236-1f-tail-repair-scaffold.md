# [[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]] — Late-tail scaffold repair sweep from [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A: no hard-prefix repair; late-tail-only scaffold is insufficient

**Finding ID**: [[h-new-236-1f-tail-repair-scaffold|h-new-236-1f]]  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-1f-tail-repair-scaffold-prereg.md`  
**Pre-reg SHA-256**: `9498db4f7de8b4404fc32bc6bafbd0435fd88b45ea26f8f98ddaacbbeead6ba3`  
**Seed**: 20260423  
**Parents**: [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] / [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]  
**Grandparent**: [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] -> [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] -> [[h-new-236-generative-simulator|H-NEW-236]] -> [[cross-finding-020-the-complete-equation|cross-finding-020]]  
**Bonferroni**: k=11, alpha_bon = 0.004545454545454545  
**Verdict**: **NO LATE-TAIL-ONLY HARD-PREFIX REPAIR.** Starting from [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A, no cumulative prefix of the ten locked late-tail M_H edges returns both empirical `L_path` and empirical `L_tail_91_114` to the simulator 95% CI while keeping empirical `L_mufaṣṣal-short` and `Block-χ²` inside. The best local-closed cell is still `k=0`, the unmodified [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A base. Late-tail hard-adjacency additions move the simulator in the wrong direction overall.

---

## Headline

This run tested the narrowest possible repair hypothesis left open by
[[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] and [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]:

> if the [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A over-correction is caused by a missing
> late-tail scaffold, then adding only the [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] late-tail M_H
> edges should eventually pull `L_path` and `L_tail_91_114` back inside
> without reopening the local mufaṣṣal-short block.

That does **not** happen.

- `k=0..5` keep the local block closed, but `L_path` and
  `L_tail_91_114` stay outside low in every cell
- `k=6`, `k=9`, and `k=10` actually **reopen** the local block
- `k=7` and `k=8` re-close the local block marginally, but still leave
  both global observables fully outside
- `W_wrap` stays inside for all 11 cells, so it is not the point of
  failure

The sweep therefore gives a clean negative answer:

> the late-tail scaffold is **not sufficient by itself as a hard
> adjacency prefix** on top of [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A.

---

## 1. Positive control

The pre-registered `k=0` anchor is exactly the [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A
mechanism under a new seed. It reproduces the parent with negligible
drift:

- `|Δ L_path sim_mean| = 0.000276`
- `|Δ L_tail_91_114 sim_mean| = 0.003405`
- `|Δ L_mufaṣṣal-short sim_mean| = 0.000088`

Qualitative pattern also matches exactly:

- empirical `L_mufaṣṣal-short` inside sim 95% CI
- empirical `Block-χ²` inside sim 95% CI
- empirical `L_path` outside low
- empirical `L_tail_91_114` outside low

**Positive control PASS**. The negative result is therefore not an
instrument failure.

---

## 2. Locked cumulative sweep

Late-tail edges were added cumulatively in the pre-registered order:

`(91,92), (92,93), (95,96), (96,97), (97,98), (98,99), (99,100),
 (100,101), (101,102), (109,110)`

### 2.1 Cell-by-cell results

| k | Added through | `L_path` sim mean / pct | `L_tail_91_114` sim mean / pct | `L_mufaṣṣal-short` sim mean / pct | `Block-χ²` | Verdict |
|---|---|---|---|---|---|---|
| 0 | base only | `86.5084`, pct `1.9` | `10.5066`, pct `0.6` | `16.4415`, pct `64.2` | `1.86` inside | `LOCAL-CLOSED-GLOBAL-NOT-YET-REPAIRED` |
| 1 | `91-92` | `86.6574`, pct `0.3` | `10.6189`, pct `0.4` | `16.5659`, pct `35.1` | `2.10` inside | same |
| 2 | `92-93` | `86.6185`, pct `0.2` | `10.6244`, pct `0.4` | `16.5474`, pct `40.2` | `1.85` inside | same |
| 3 | `95-96` | `86.7809`, pct `0.2` | `10.6668`, pct `0.0` | `16.6776`, pct `17.6` | `3.13` inside | same |
| 4 | `96-97` | `86.8276`, pct `0.0` | `10.7190`, pct `0.1` | `16.7431`, pct `9.3` | `3.84` inside | same |
| 5 | `97-98` | `86.8859`, pct `0.0` | `10.7776`, pct `0.0` | `16.8110`, pct `4.7` | `5.07` inside | same |
| 6 | `98-99` | `86.9532`, pct `0.0` | `10.8545`, pct `0.0` | `16.8571`, pct `2.4` | `6.55` outside | `NO-REPAIR` |
| 7 | `99-100` | `86.9309`, pct `0.0` | `10.7817`, pct `0.0` | `16.8361`, pct `2.7` | `6.01` inside | `LOCAL-CLOSED-GLOBAL-NOT-YET-REPAIRED` |
| 8 | `100-101` | `86.9480`, pct `0.0` | `10.7907`, pct `0.0` | `16.8672`, pct `3.1` | `6.25` inside | same |
| 9 | `101-102` | `86.9852`, pct `0.0` | `10.7831`, pct `0.0` | `16.9047`, pct `1.6` | `7.00` outside | `NO-REPAIR` |
| 10 | `109-110` | `87.0607`, pct `0.0` | `10.8329`, pct `0.0` | `16.9831`, pct `0.3` | `10.09` outside | `NO-REPAIR` |

There is **no** primary repair cell and **no** family 4/4 repair cell.

### 2.2 What actually changes across the sweep

The sweep direction is clear and unfavorable:

1. `L_path` gets worse almost immediately.
   The base cell already overshoots with sim mean `86.5084` against
   empirical `85.7597`. By `k=10`, the sim mean is `87.0607`.

2. `L_tail_91_114` also gets worse.
   The base cell starts at sim mean `10.5066` against empirical
   `8.6398`. By `k=10`, the sim mean is `10.8329`.

3. The local block is initially stable but drifts toward failure.
   `L_mufaṣṣal-short` stays inside through `k=5`, falls outside at
   `k=6`, returns barely inside at `k=7` and `k=8`, then fails again at
   `k=9` and `k=10`.

4. `Block-χ²` shows the same instability.
   It stays inside through `k=5`, fails at `k=6`, recovers narrowly at
   `k=7` and `k=8`, and fails again at `k=9` and `k=10`.

So the late-tail prefix does not counter-balance the front-loaded Juz'
30 hinges. It compounds their over-correction.

---

## 3. Interpretation

### 3.1 The split-terminal picture is not confirmed by this hard-prefix design

The motivating hypothesis was:

- front-loaded Juz' 30 hinges are real and causal
- a distributed late-tail scaffold might counter-balance them

The present run supports only the first half. It does **not** support
the second half in the form tested here.

What is falsified is not the broad intuition that late-tail structure
matters. What is falsified is the stronger procedural claim:

> "Take [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A, add the late-tail M_H edges as hard
> cumulative adjacencies, and the global path/tail will recover."

That claim fails cleanly.

### 3.2 The best local-closed cell is still the unmodified base

Among all cells that keep both `L_mufaṣṣal-short` and `Block-χ²`
inside, `k=0` remains the closest to empirical on both global
observables:

- `|L_path emp - sim_mean| = 0.7488` at `k=0`
- `|L_tail emp - sim_mean| = 1.8668` at `k=0`

Every later local-closed cell is worse on both measures.

That is the strongest single-sentence summary of the result.

### 3.3 The hard late-tail edges interact nonlinearly with the local block

The odd pattern at `k=6..10` matters:

- adding `98-99` is enough to push the local block outside
- adding `99-100` and `100-101` brings the local block back inside, but
  only marginally
- adding `101-102` and then `109-110` pushes it outside again

So the late-tail scaffold is not behaving like a smooth repair knob.
Its hard-adjacency implementation induces a more brittle geometry than
the motivating story predicted.

---

## 4. How the new `95 -> 100` clue fits

The new local clue from [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] is that the decisive `95 -> 100`
top-100 tranche is:

`(92,93), (99,100), (100,101), (101,102), (109,110)`

with only:

- `(92,93)` overlapping the [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] rhyme set
- `(109,110)` overlapping the liturgical set

and the other three edges structurally independent of both soft
covariate families.

That clue remains **interesting**, but [[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]] does **not** support
promoting it to a landed repair claim.

Why not:

1. This sweep tested a **cumulative prefix**, not the `95 -> 100`
   tranche in isolation.
2. The first cell containing the structurally independent core
   `99-100` / `100-101` is `k=8`, and that cell still leaves both global
   observables fully outside.
3. The first cell containing the full `95 -> 100` tranche is `k=10`,
   and that cell reopens the local block while still failing both
   globals.

So the honest read is:

> the `95 -> 100` tranche remains a valid future target because it is
> mostly outside rhyme/liturgical covariates, but this run does not show
> that it works as a hard-prefix repair on top of [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A.

---

## 5. Consequence for the frontier

[[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]] eliminates one clean mechanism candidate.

What is now less plausible:

- "late-tail-only hard adjacency repair" as the missing counter-weight

What remains plausible:

- an **isolated** test of the [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] `95 -> 100` tranche rather
  than the broader cumulative prefix
- a **soft-weighted** tail scaffold rather than a hard adjacency law
- interaction between late-tail structure and some non-tail edge subset
  that is present in top-100 but absent from this run

So this finding narrows the target without closing the terminal
parsimony question.

---

## 6. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1f-tail-repair-scaffold-prereg.md`
- Script: `scripts/h_new_236_1f_tail_repair_scaffold.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-236-1f.json`
- Journal: `journal/h-new-236-1f-run-1.md`
