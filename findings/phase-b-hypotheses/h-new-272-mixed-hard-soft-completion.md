# [[h-new-272-mixed-hard-soft-completion|H-NEW-272]] — Mixed hard-soft completion at the OQ-15 frontier: clean negative; neither the exact five-edge tranche nor the two-edge overlap complement completes the real `lambda = 0.07` soft sweet spot

**Finding ID**: `[[h-new-272-mixed-hard-soft-completion|h-new-272]]`  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-272-mixed-hard-soft-completion-prereg.md`  
**Pre-reg SHA-256**: `51e024376c341b269172546f27d44cefed83a10e2d0eccf760a79dffd280d7e7`  
**Seed**: `20260421`  
**Parents**: [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] / [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]]  
**Grandparent**: [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] / [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] -> [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] -> [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] -> [[h-new-236-generative-simulator|H-NEW-236]] -> [[cross-finding-020-the-complete-equation|cross-finding-020]]  
**Bonferroni**: `k = 2`, `alpha_bon = 0.025`  
**Verdict**: **`MIXED-HARD-SOFT-COMPLETION-FAILS`**. The fixed `lambda = 0.07` soft sweet spot does not become a strict completion when paired with either locked hard complement. `strict_4of4_cells = []`. `primary_only_cells = []`.

---

## Headline

[[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] showed that the soft terminal family has a real but incomplete
sweet spot at `lambda = 0.07`: it reaches primary closure but still misses
`L_tail_91_114`.

[[h-new-272-mixed-hard-soft-completion|H-NEW-272]] tested the narrowest obvious completion story:

- keep `lambda = 0.07` fixed
- keep the top-50 hard scaffold fixed
- add either:
  - the exact five-edge decisive `95->100` tranche from [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]], or
  - the two-edge overlap subset `(92,93)` and `(109,110)`

The answer is cleanly negative.

Both inferential cells do the same thing:

- `L_mufassal_short` stays inside
- `Block-chi2` stays inside
- `W_wrap` stays inside
- `L_path` falls outside low
- `L_tail_91_114` stays outside low

So the tested hard add-ons do not complete the soft sweet spot. They convert it
into the same old parsimony-conflict geometry.

---

## 1. Positive control

The mixed-code positive control exactly reproduced the parent [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]]
`lambda = 0.07` cell:

- parent verdict: `SOFT-CLOSES-PRIMARY`
- control verdict: `SOFT-CLOSES-PRIMARY`
- max abs sim-mean drift across
  `L_path / W_wrap / L_mufassal_short / L_tail_91_114` = `0.0`

**Positive control PASS**: the mixed runner did not drift from the parent soft
sweet-spot cell.

---

## 2. Locked inferential cells

| Cell | Added hard edges | Mixed verdict | `L_path` | `L_mufassal_short` | `L_tail_91_114` | `W_wrap` | `Block-chi2` |
|---|---|---|---|---|---|---|---|
| `cell_a_lambda0p07_plus_exact_tranche` | exact tranche `(92,93) (99,100) (100,101) (101,102) (109,110)` | `MIXED-PARSIMONY-CONFLICT` | outside low, pct `0.6`, CI `[85.973434, 87.219061]` | inside, pct `53.6`, CI `[16.207932, 16.822269]` | outside low, pct `0.1`, CI `[9.408069, 11.849264]` | inside, pct `35.4` | inside, pct `52.2` |
| `cell_b_lambda0p07_plus_overlap_pair` | overlap pair `(92,93) (109,110)` | `MIXED-PARSIMONY-CONFLICT` | outside low, pct `1.2`, CI `[85.855207, 87.053530]` | inside, pct `85.1`, CI `[16.093426, 16.640130]` | outside low, pct `0.4`, CI `[9.152790, 11.816409]` | inside, pct `39.1` | inside, pct `85.1` |

Top-level JSON summary:

- `strict_4of4_cells = []`
- `primary_only_cells = []`
- `overall_verdict = MIXED-HARD-SOFT-COMPLETION-FAILS`

---

## 3. What changed relative to the parent `lambda = 0.07` cell

The parent [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] `lambda = 0.07` cell was a true primary pass:

- `L_path` inside
- `L_mufassal_short` inside
- `L_tail_91_114` just outside low

Both hard complements made the parent state worse in the same direction.

### 3.1 Exact five-edge tranche

Relative to the parent `lambda = 0.07` soft-only cell, the exact tranche caused:

- `L_path sim_mean` drift `+0.238852`
- `L_tail_91_114 sim_mean` drift `+0.499058`
- `L_mufassal_short sim_mean` drift `+0.229791`
- weighted preference satisfaction mean drift `-5.548`

The exact mixed cell still kept the local/block side inside:

- `L_mufassal_short sim_mean = 16.502963`
- `Block-chi2` empirical percentile `52.2`

But the globals were clearly worse:

- `L_path sim_mean = 86.603643`, empirical percentile `0.6`
- `L_tail_91_114 sim_mean = 10.672472`, empirical percentile `0.1`

### 3.2 Two-edge overlap complement

Relative to the parent `lambda = 0.07` soft-only cell, the overlap pair caused:

- `L_path sim_mean` drift `+0.097414`
- `L_tail_91_114 sim_mean` drift `+0.390723`
- `L_mufassal_short sim_mean` drift `+0.088943`
- weighted preference satisfaction mean drift `-4.442`

This is the milder of the two hard complements, but it still fails in the same
way:

- `L_path sim_mean = 86.462205`, empirical percentile `1.2`
- `L_tail_91_114 sim_mean = 10.564137`, empirical percentile `0.4`
- `L_mufassal_short` remains inside
- `Block-chi2` remains inside

So even the smallest overlap complement does not preserve the parent primary
pass.

---

## 4. Interpretation

[[h-new-272-mixed-hard-soft-completion|H-NEW-272]] sharpens the OQ-15 frontier in a useful way.

### 4.1 What it establishes

1. The [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] soft sweet spot is real and reproducible.
   The positive control matched the parent cell exactly.
2. The tested tiny hard complements do not complete that sweet spot.
   Neither the exact decisive tranche nor the two-edge overlap subset lands
   strict closure.
3. The failure mode is not vague.
   The mixed cells keep the local/block observables inside but push `L_path`
   back outside low while leaving `L_tail_91_114` outside low.

### 4.2 What it means mechanistically

The hard complements tested here do not behave like a missing final patch on
top of the soft mechanism. They compete with it.

The strongest evidence for that is the joint drift pattern:

- path gets longer
- tail gets longer
- weighted soft-family satisfaction falls

So the hard complements do not merely "finish" the soft sweet spot. They
partially undo the very soft structure that made `lambda = 0.07` work.

### 4.3 What [[h-new-272-mixed-hard-soft-completion|H-NEW-272]] does not claim

1. It does not rule out every mixed model.
2. It does rule out the narrowest, most defensible first-pass mixed completion
   family built directly from [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] and [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]].
3. It does not upgrade the hard five-edge tranche into a completion law. In the
   mixed setting too, that tranche remains insufficient.

---

## 5. Bottom line

The parsimony frontier remains intact.

The real `lambda = 0.07` soft-only sweet spot exists, but the two most obvious
tiny hard completions do not finish it. Both convert the soft sweet spot into
`MIXED-PARSIMONY-CONFLICT`.

That is a clean negative, and it is a useful one.

---

## 6. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-272-mixed-hard-soft-completion-prereg.md`
- Script: `scripts/h_new_272_mixed_hard_soft_completion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-272.json`
- Journal: `journal/h-new-272-run-1.md`
