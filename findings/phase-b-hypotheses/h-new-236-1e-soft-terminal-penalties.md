# [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] — Soft terminal penalties on the top-50 scaffold: no parsimony recovery; only parsimony-conflict signal survives

**Finding ID**: [[h-new-236-1e-soft-terminal-penalties|h-new-236-1e]]  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-1e-soft-terminal-penalties-prereg.md`  
**Seed**: 20260421  
**Parent**: [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] / [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]]  
**Grandparent**: [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] -> [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] -> [[h-new-236-generative-simulator|H-NEW-236]] -> [[cross-finding-020-the-complete-equation|cross-finding-020]]  
**Bonferroni**: k=3, alpha_bon = 0.01667  
**Verdict**: **SOFT TERMINAL MECHANISM SHOWS PARSIMONY CONFLICT ONLY.** No tested lambda achieves even the primary target (`L_mufassal_short` inside + `L_path` inside), let alone strict 4/4 closure.

---

## Headline

This run asked a narrow question:

> can rhyme / liturgical terminal structure work as a **soft preference**
> even though it failed as a hard adjacency law in [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]?

Answer on the locked lambda grid `{0.05, 0.10, 0.20}`:

- **No strict 4/4 passes**
- **No primary passes**
- `lambda = 0.05` is a **near-miss** but still too weak to close the local block
- `lambda = 0.10` and `0.20` do close the local block, but they
  recreate the same global over-correction pattern seen in the hard
  rhyme/liturgical cells

So the soft version does not rescue parsimony.

---

## 1. Positive control

The `lambda = 0` soft-code-path control reproduces the inherited top-50
baseline:

- `L_path` inside, percentile `55.0`
- `L_mufassal_short` still outside high, percentile `100.0`, `z = +10.41`
- `L_tail_91_114` inside, percentile `25.8`
- `Block-chi2` outside high, percentile `100.0`

**MW-5 positive control PASS**: the soft-penalty implementation behaves
like the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 baseline when lambda is zero.

---

## 2. Locked lambda results

| Cell | Lambda | `L_path` | `L_mufassal_short` | `L_tail_91_114` | `Block-chi2` | Verdict |
|---|---:|---|---|---|---|---|
| `cell_a_lambda_0p05` | 0.05 | inside, pct `6.5` | outside high, pct `99.9`, `z = +2.78` | inside, pct `6.8` | outside high, pct `99.8` | `SOFT-NULL` |
| `cell_b_lambda_0p10` | 0.10 | outside low, pct `1.3` | inside, pct `81.7`, `z = +0.88` | outside low, pct `0.8` | inside, pct `78.8` | `SOFT-PARSIMONY-CONFLICT` |
| `cell_c_lambda_0p20` | 0.20 | outside low, pct `0.1` | inside, pct `46.6`, `z = -0.08` | outside low, pct `0.2` | inside, pct `48.7` | `SOFT-PARSIMONY-CONFLICT` |

Top-level JSON summary:

- `strict_4of4_cells = []`
- `primary_only_cells = []`
- `parsimony_conflict_cells = [cell_b_lambda_0p10, cell_c_lambda_0p20]`
- `overall_verdict = SOFT TERMINAL MECHANISM SHOWS PARSIMONY CONFLICT ONLY`

---

## 3. Interpretation

### 3.1 Weak soft pressure is too weak

At `lambda = 0.05`:

- global path and tail remain inside
- but `L_mufassal_short` is still outside high
- `Block-chi2` also remains outside
- terminal gap closure reaches **59.64%**
- mean weighted terminal preference satisfaction rises to **14.10 / 22**

So weak rhyme/liturgical pressure does not reach the local block, but it
does get materially closer than the raw top-50 baseline.

### 3.2 Medium and strong soft pressure reproduce the old conflict

At `lambda = 0.10` and `0.20`:

- `L_mufassal_short` enters the simulator family
- `Block-chi2` enters too
- but `L_path` and `L_tail_91_114` both fail low

This is the same structural signature already seen in:

- [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] hard `M_R`
- [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] hard `M_L`
- [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] targeted Juz 30 injection

So softening the covariates does **not** change the basic geometry of
the problem. It only moves the breakpoint.

### 3.3 Narrow soft sweet spot hypothesis

The three locked lambdas imply a narrow untested interpolation band:

- `0.05` keeps `L_path` and `L_tail` inside but misses local closure
- `0.10` closes the local block but breaks `L_path` and `L_tail`

So if a genuine soft-only sweet spot exists at all, it is likely narrow
and somewhere between **`lambda ~ 0.07-0.08`**.

That is a **post-hoc interpolation clue**, not a landed finding. It was
not part of the locked grid and should be treated only as a bounded next
move if the project decides a finer soft sweep is worth spending a test
family on later.

### 3.3 Why this fits the new [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] clue

### 3.4 Why this fits the new [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] clue

[[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] showed that the decisive `95 -> 100` hard-hinge tranche is:

- `92-93`
- `99-100`
- `100-101`
- `101-102`
- `109-110`

Only two of those five edges overlap the soft covariate families at all:

- `92-93` overlaps the rhyme set
- `109-110` overlaps the liturgical set

The remaining three are outside both. So [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]]'s failure is
coherent with [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] rather than surprising:

> the missing parsimony information is mostly **not** reducible to soft
> rhyme / liturgical weighting alone.

---

## 4. Consequence for the frontier

[[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] eliminates an attractive parsimony rescue route.

What remains highest-EV:

- **[[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]]** late-tail scaffold repair
- broader `H-NEW-236.2` style observable coverage under `M_H`
- only after that, any finer-grained prosodic softening beyond the
  coarse rhyme / liturgical sets used here

The project state after [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] is clearer:

- hard top-100 scaffold closes
- hard-hinge parsimony bracket is `(95, 100]`
- soft rhyme/liturgical pressure does **not** recover a lower-cost
  closure

---

## 5. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1e-soft-terminal-penalties-prereg.md`
- Script: `scripts/h_new_236_1e_soft_terminal_penalties.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-236-1e.json`
