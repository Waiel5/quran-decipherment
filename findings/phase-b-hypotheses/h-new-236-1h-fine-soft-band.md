# [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] — Fine soft interpolation inside the [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] near-miss band: a real but narrow primary-only sweet spot at lambda = 0.07; strict closure still fails on the tail

**Finding ID**: [[h-new-236-1h-fine-soft-band|h-new-236-1h]]  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-1h-fine-soft-band-prereg.md`  
**Pre-reg SHA-256**: `8431ff02d79edbcdbe60d6166b9fd7dd089ff733fc02707b1f353f284664977f`  
**Seed**: 20260421  
**Parent**: [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] / [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]]  
**Grandparent**: [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] / [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] -> [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] -> [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] -> [[h-new-236-generative-simulator|H-NEW-236]] -> [[cross-finding-020-the-complete-equation|cross-finding-020]]  
**Rules tuple**: `(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per [[h-new-111-fisher-rao-mushaf|H-NEW-111]], stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq + TOP-50-HINGE-BASELINE + SOFT-TERMINAL-PREFERENCE-PENALTY, seed 20260421)`  
**Bonferroni**: k=4, alpha_bon = 0.0125  
**Verdict**: **The [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] near-miss band contains a genuine but narrow primary-only soft sweet spot at `lambda = 0.07`.** This does **not** deliver strict closure. The first primary pass appears at `0.07`, but `L_tail_91_114` still misses low, and by `0.08` the run has already crossed into parsimony-conflict.

---

## Headline

[[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] suggested that if a soft-only rescue existed at all, it would have
to live in a very narrow band between `0.05` and `0.10`.

[[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] confirms that this was a real clue, not noise, but only in a
limited sense:

- `lambda = 0.06` is still `SOFT-NULL`
- `lambda = 0.07` reaches `SOFT-CLOSES-PRIMARY`
- `lambda = 0.08` and `0.09` are already `SOFT-PARSIMONY-CONFLICT`
- **no cell reaches strict 4/4 closure**

So the soft route is not simply null. It can close the declared primary target
on a razor-thin band. But it still does not solve the full terminal equation.

---

## 1. Positive control

The `lambda = 0` soft-code-path control reproduces the inherited [[h-new-236-1a-extended-hinges|H-NEW-236.1a]]
top-50 baseline:

- positive-control `L_mufassal_short z = +10.408`
- parent [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 `z = +10.664`
- tolerance `|delta z| <= 2.0` passes comfortably

**MW-5 positive control PASS**: the fine-band runner preserves the [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]]
code path and does not introduce baseline drift.

---

## 2. Locked fine-grid result

| Cell | Lambda | `L_path` | `L_mufassal_short` | `L_tail_91_114` | `Block-chi2` | Verdict |
|---|---:|---|---|---|---|---|
| `cell_a_lambda_0p06` | 0.06 | inside, pct `3.7` | outside high, pct `98.4`, `z = +2.09` | inside, pct `3.4` | outside high, pct `98.1` | `SOFT-NULL` |
| `cell_b_lambda_0p07` | 0.07 | inside, pct `2.9` | inside, pct `96.3`, `z = +1.81` | outside low, pct `2.3` | inside, pct `96.5` | `SOFT-CLOSES-PRIMARY` |
| `cell_c_lambda_0p08` | 0.08 | outside low, pct `1.8` | inside, pct `90.4`, `z = +1.33` | outside low, pct `2.5` | inside, pct `88.9` | `SOFT-PARSIMONY-CONFLICT` |
| `cell_d_lambda_0p09` | 0.09 | outside low, pct `1.4` | inside, pct `87.0`, `z = +1.13` | outside low, pct `0.9` | inside, pct `84.2` | `SOFT-PARSIMONY-CONFLICT` |

Top-level JSON summary:

- `strict_4of4_cells = []`
- `primary_only_cells = [cell_b_lambda_0p07]`
- `parsimony_conflict_cells = [cell_c_lambda_0p08, cell_d_lambda_0p09]`
- `overall_verdict = FINE SOFT BAND FINDS PRIMARY-ONLY CLOSURE`

---

## 3. What the winning cell actually does

### 3.1 `lambda = 0.07` is a real primary pass

The key cell is `cell_b_lambda_0p07`:

- `L_path` empirical `85.759655` lies **inside** the sim 95% CI
  `[85.740898, 86.916152]`
- `L_mufassal_short` empirical `16.514906` lies **inside** the sim 95% CI
  `[16.012956, 16.529269]`
- `Block-chi2` is also **inside** with empirical percentile `96.5`
- weighted terminal preference satisfaction rises to mean `14.608 / 22`
  (`66.4%`)

This is not an artifact of a looser threshold. It is a genuine primary pass by
the pre-registered criterion.

### 3.2 Why it still fails strict closure

The same `lambda = 0.07` cell still misses the tail:

- empirical `L_tail_91_114 = 8.639798`
- sim 95% CI = `[8.665691, 11.719130]`
- empirical percentile = `2.3`

So the miss is small but real. The soft-only sweet spot closes the local block
and preserves global path fit, but it still leaves the terminal tail too short.

Sim-pass count for `lambda = 0.07` is therefore `3/4`, not `4/4`.

---

## 4. Boundary shape across the band

[[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] shows a clean phase transition across the narrow grid.

### 4.1 `0.06` is still too weak

At `lambda = 0.06`:

- `L_path` stays inside
- `L_tail_91_114` stays inside
- but `L_mufassal_short` is still outside high
- terminal gap closure reaches `67.47%`

So the weak side still undershoots the local block.

### 4.2 `0.07` is the only landed sweet spot

At `lambda = 0.07`:

- local block enters
- path remains inside
- `Block-chi2` enters too
- only the tail remains outside
- terminal gap closure reaches `73.01%`

This is the first and only landed primary pass in the fine band.

### 4.3 `0.08` and `0.09` cross into the old conflict regime

At `lambda = 0.08` and `0.09`:

- `L_mufassal_short` stays inside
- `Block-chi2` stays inside
- but `L_path` falls outside low
- `L_tail_91_114` also stays outside low

That is the same old parsimony-conflict geometry already seen in [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]],
just exposed more sharply. The crossover from primary pass to conflict occurs
between `0.07` and `0.08`.

---

## 5. Interpretation

### 5.1 What [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] genuinely establishes

1. **The [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] near-miss was not just noise.** There is a real narrow
   soft-only band where the top-50 scaffold plus soft rhyme/liturgical pressure
   can satisfy the declared primary criterion.
2. **That band is very narrow.** On the locked grid, it is represented by
   exactly one cell: `lambda = 0.07`.
3. **Strict closure still fails for a specific reason.** The residual failure is
   not the local block anymore. It is the short tail `Q91-114`.

### 5.2 What [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] does not establish

1. It does **not** show a full soft replacement for the hard `M_H` top-100
   scaffold.
2. It does **not** rescue soft parsimony at the full-equation level, because
   strict `4/4` closure still does not land.
3. It does **not** remove the [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] clue that late-tail structure beyond
   the rhyme/liturgical family still matters.

The cleanest summary is:

> the fine soft sweep finds a **primary-only** sweet spot, not a full closure.

---

## 6. Consequence for the frontier

[[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] upgrades the soft route from "coarse near-miss" to "real but
partial mechanism."

What this means for the frontier:

- the soft rhyme/liturgical family is **causal enough** to close the primary
  local-vs-global target on a narrow band
- but it is still **insufficient** for strict closure because the tail remains
  underexplained
- this aligns with [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] rather than contradicting it: the late-tail
  hard tranche still looks like missing information outside the soft family

So the honest post-H-NEW-236.1h position is stronger and more precise:

- soft weighting is not null
- soft weighting is not enough
- the unresolved residue is increasingly concentrated in late-tail structure

---

## 7. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1h-fine-soft-band-prereg.md`
- Script: `scripts/h_new_236_1h_fine_soft_band.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-236-1h.json`
- Journal: `journal/h-new-236-1h-run-1.md`
