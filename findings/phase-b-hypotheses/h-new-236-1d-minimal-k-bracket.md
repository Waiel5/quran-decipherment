# [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] — Minimal-K bracket search for strict 4/4 closure: only K=100 passes; hard-hinge parsimony bracket tightens to (95, 100]

**Finding ID**: [[h-new-236-1d-minimal-k-bracket|h-new-236-1d]]  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-1d-minimal-k-bracket-prereg.md`  
**Pre-reg SHA-256**: `837fd117b987a3b387a260a429dac7d1870af1977e2d10b594616056df12c54a`  
**Seed**: 20260421  
**Parent**: [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] (top-100 strict pass)  
**Grandparent**: [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] (top-30 / top-50 close `L_path` but not `L_mufassal_short`)  
**Rules tuple**: `(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per [[h-new-111-fisher-rao-mushaf|H-NEW-111]], stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq + TOP-K-HINGE-PRESERVATION, seed 20260421)`  
**Bonferroni**: k=6, alpha_bon = 0.00833  
**Verdict**: **The hard-hinge parsimony bracket tightens from `(50, 100]` to `(95, 100]`.** On the locked grid `{73, 80, 85, 90, 95, 100}`, only `K=100` achieves strict 4/4 closure. No tested K below 100 closes strictly.

---

## Headline

This run did **not** find an earlier strict-passing hinge cutoff. The
hard-hinge story is now sharper:

- `K=50` was already known to fail strictly from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] / [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]
- `K=73`, the first cutoff containing any internal `mufassal-short`
  edge, still fails
- `K=85` and `K=90` repair the local `mufassal-short` block and keep
  `L_path` inside, but **still fail on `L_tail_91_114`**
- `K=95` regresses and fails again on both `L_mufassal_short` and the
  tail
- only `K=100` closes all four observables

So the tested hard-hinge minimum is not "somewhere in the 70s or 80s."
It sits at the extreme top of the tested bracket.

---

## 1. Locked grid result

| Cell | Strict 4/4? | `L_path` | `L_mufassal_short` | `L_tail_91_114` | `Block-chi2` | Interpretation |
|---|:---:|---|---|---|---|---|
| `K=73` | NO | outside high, pct 100.0 | z = +3.79, outside high | inside, pct 4.4 | outside high, pct 100.0 | first internal `mufassal-short` hinge is not enough |
| `K=80` | NO | outside high, pct 100.0 | z = +2.65, outside high | outside low, pct 2.2 | outside high, pct 98.0 | still under-specified |
| `K=85` | NO | inside, pct 87.4 | z = +1.15, inside | outside low, pct 1.1 | inside, pct 73.6 | local block repaired, tail still wrong |
| `K=90` | NO | inside, pct 77.4 | z = +0.77, inside | outside low, pct 1.5 | inside, pct 55.7 | same pattern as `K=85` |
| `K=95` | NO | outside high, pct 99.9 | z = +2.67, outside high | outside high, pct 99.9 | outside high, pct 99.1 | non-closing regression |
| `K=100` | **YES** | inside, pct 93.1 | z = +1.44, inside | inside, pct 93.1 | inside, pct 85.0 | **first strict pass** |

**Positive control**: fresh-seed `K=50` reproduces the inherited
non-closing baseline. `mw5_positive_control_ok = True`.

**Primary output**:

- `smallest_tested_strict_pass_k = 100`
- `tested_bracket = (95, 100]`
- `non_monotonic_after_first_pass = False`

---

## 2. What changed across the grid

### 2.1 Entry into `mufassal-short` is not sufficient

The first internal `mufassal-short` edge enters the canonical
Fisher-Rao ranking at:

- `Q 78 -> 79`, rank `73`, distance `0.720817`

That matters, but [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] shows it is **not** enough to close the
residual by itself. `K=73` and `K=80` both still fail strictly.

### 2.2 The 80s solve the local block but not the tail

The most informative cells are `K=85` and `K=90`:

- both put `L_mufassal_short` inside the simulator distribution
- both put `Block-chi2` inside
- both keep `L_path` inside
- **both still miss `L_tail_91_114` low**

That is the clearest new structural signal from this run. The late tail
is not just a by-product of local `mufassal-short` closure. It remains a
separate constraint even after the block-level miss is repaired.

### 2.3 The 95-cell regression matters

`K=95` is especially informative because it nearly closes the bracket
but still fails:

- `L_path` falls just outside high at percentile `99.9`
- `L_mufassal_short` reopens to `z = +2.67`
- `L_tail_91_114` also flips to outside high at percentile `99.9`

So the path to closure is **not monotone smooth** across the tested
hard-hinge grid. A high-K scaffold can still be misbalanced until the
final late-tail tranche is present.

---

## 3. The decisive new clue: the K=95 -> K=100 tranche is pure late-tail structure

The five edges added between the last failing cell and the first passing
cell are:

- `Q 92 -> 93`
- `Q 99 -> 100`
- `Q 100 -> 101`
- `Q 101 -> 102`
- `Q 109 -> 110`

This is not a diffuse whole-mushaf patch. It is a **pure late-tail
tranche**.

That is the strongest new mechanistic clue produced by [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]].
The hard-hinge bracket no longer says merely "closure needs more than
50." It now says:

> the last strict step from failure to closure is carried by a compact
> set of **late-tail adjacencies**.

This directly supports the emerging split-terminal reading:

- front-loaded Juz 30 hinges matter
- but the closing `Q 91-114` tail also needs its own distributed scaffold

That is exactly the mechanism family queued in [[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]].

---

## 4. Interpretation

### What [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] confirms

1. **Hard-hinge closure is real but expensive.** The first strict pass
   remains `K=100`.
2. **The bracket is now materially tighter.** The hard-hinge minimum is
   no longer `(50, 100]`; it is `(95, 100]` on tested values.
3. **Tail control is a distinct constraint.** The `K=85` and `K=90`
   cells show that local block closure is possible before full strict
   closure, but the tail still refuses to align.
4. **The final closing information is late-tail specific.** The
   `K=95 -> 100` delta is carried entirely by late-tail edges.

### What [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] does not show

1. It does **not** prove that `K=100` is the true minimum. The honest
   claim remains a tested bracket `(95, 100]`.
2. It does **not** rescue hard-hinge parsimony by itself. If anything,
   it makes the hard-hinge result *less* parsimonious than the earlier
   `(50, 100]` bracket suggested.
3. It does **not** adjudicate soft-weighted mechanisms. That remains the
   job of the queued soft-penalty branch.

---

## 5. Consequence for the frontier

[[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] changes the next-move logic.

The best next move is **not** another blunt hard-K sweep first. The
highest-EV follow-up is now:

- isolate the late-tail tranche directly
- test whether those `Q 91-114` edges can repair the over-correcting
  [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] base with far fewer added hard constraints
- compare that against soft rhyme / liturgical weighting

In other words, [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] makes the late-tail scaffold hypothesis
more credible, not less.

---

## 6. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1d-minimal-k-bracket-prereg.md`
- Script: `scripts/h_new_236_1d_minimal_k_bracket.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-236-1d.json`

