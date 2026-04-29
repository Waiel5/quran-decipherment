# [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] — Targeted mufaṣṣal-short hinges collapse R12a locally but overcorrect the global path

**Finding ID**: [[h-new-236-1c-targeted-mufassal-hinges|h-new-236-1c]]  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-1c-targeted-mufassal-hinges-prereg.md`  
**Pre-reg SHA-256**: `001eff4e16af49c9f8b40e1e00ec827e0612cfe3b3b375ee12a82bc89453f67e`  
**Seed**: 20260419  
**Parent**: [[h-new-236-1a-extended-hinges|H-NEW-236.1a]]  
**Grandparent**: [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] -> [[h-new-236-generative-simulator|H-NEW-236]] -> [[cross-finding-020-the-complete-equation|cross-finding-020]]  
**Rules tuple**: `(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per [[h-new-111-fisher-rao-mushaf|H-NEW-111]], stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq constraints + TOP-50-GLOBAL-HINGE-PRESERVATION + TOP-JUZ30-INTERNAL-HINGE-PRESERVATION for m in {5, 10})`  
**Verdict**: **MIXED / LOCAL-CLOSURE-GLOBAL-OVERCORRECTION** — adding a very small set of internal Juzʾ-30 hinges on top of the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 scaffold makes empirical `L_mufaṣṣal-short` and `Block-χ²` fall fully inside the simulator distribution, but both cells then overshoot the global `L_path` and `L_tail_91_114` observables in the opposite direction. The terminal residual is therefore **not** "missing hinges" alone; it is a **balance problem** between front-loaded Juzʾ-30 hinges and a separately preserved short late tail.

---

## Headline

[[h-new-236-1a-extended-hinges|H-NEW-236.1a]] had isolated the last causal-generative miss to:

> **R12a = mufaṣṣal-short within-block cost-excess**

[[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] tests the cleanest possible omitted-hinge explanation:

- keep the **successful top-50 global hinge scaffold fixed**
- add only the strongest internal Juzʾ-30 consecutive jumps from
  [[h-new-255-juz30-mini-cycle|H-NEW-255]]
- ask whether the terminal residual disappears

It does disappear locally:

- **Cell A (`+5` internal Juzʾ-30 hinges)** closes **91.79%** of the
  remaining mufaṣṣal-short mean-gap and moves both
  `L_mufaṣṣal-short` and `Block-χ²` inside the simulator 95% CI
- **Cell B (`+10`)** slightly over-closes the block
  (**109.57%** closure; empirical now below the simulator mean) and
  also places both `L_mufaṣṣal-short` and `Block-χ²` inside

But both cells fail the full simulator in a new way:

- `L_path` becomes **too high in the simulator** relative to the
  empirical mushaf
- `L_tail_91_114` becomes **far too high in the simulator**

So the surviving frontier is no longer "which internal terminal
hinges matter?" The answer to that is now **clear: they matter a lot**.

The new frontier is:

> **What counter-balances those front-loaded Juzʾ-30 hinges so that the
> canonical mushaf keeps Q 91-114 unusually short while preserving the
> major internal Juzʾ-30 jumps?**

---

## 1. Cell results

Baseline from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50:

- empirical `L_mufaṣṣal-short = 16.514906`
- simulator mean `15.619384`
- residual mean-gap `Δ0 = 0.895522`
- `Block-χ² = 115.52`

### Cell A — top-50 + Juzʾ-30 top-5

Added hinges:

- `Q 78→79`
- `Q 79→80`
- `Q 88→89`
- `Q 83→84`
- `Q 80→81`

Results:

| Observable | Empirical | Sim mean | Sim 95% CI | Percentile | Verdict |
|---|---:|---:|---:|---:|---|
| `L_path` | 85.759655 | **86.508699** | [85.828143, 87.105225] | 1.9 | **OUTSIDE LOW** |
| `W_wrap` | 0.388370 | 0.437404 | [0.338400, 0.624428] | 40.7 | **INSIDE** |
| `Block-χ²` | 1.8607 | — | sim 97.5 pct = 7.27 | 59.9 | **INSIDE** |
| `L_tail_91_114` | 8.639798 | **10.503231** | [8.985741, 11.960730] | 0.6 | **OUTSIDE LOW** |
| `L_mufaṣṣal-short` | 16.514906 | **16.441384** | [16.057827, 16.734746] | 64.2 | **INSIDE** |

Key closure numbers:

- mufaṣṣal-short mean-gap: `0.073522`
- closure vs [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50: **91.79%**
- Block-χ² reduction: `115.52 -> 1.86` (**98.39% reduction**)
- Overall scorecard: **2/4**

### Cell B — top-50 + Juzʾ-30 top-10

Added hinges:

- Cell A plus:
  `Q 89→90`, `Q 84→85`, `Q 98→99`, `Q 82→83`, `Q 97→98`

Results:

| Observable | Empirical | Sim mean | Sim 95% CI | Percentile | Verdict |
|---|---:|---:|---:|---:|---|
| `L_path` | 85.759655 | **86.669950** | [86.059105, 87.290287] | 0.2 | **OUTSIDE LOW** |
| `W_wrap` | 0.388370 | 0.416754 | [0.338400, 0.528920] | 49.7 | **INSIDE** |
| `Block-χ²` | 2.1142 | — | sim 97.5 pct = 8.02 | 65.9 | **INSIDE** |
| `L_tail_91_114` | 8.639798 | **10.657000** | [9.135404, 12.193969] | 0.4 | **OUTSIDE LOW** |
| `L_mufaṣṣal-short` | 16.514906 | **16.600570** | [16.253020, 16.865261] | 25.9 | **INSIDE** |

Key closure numbers:

- mufaṣṣal-short mean-gap: `-0.085664` (over-closure)
- closure vs [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50: **109.57%**
- Block-χ² reduction: `115.52 -> 2.11` (**98.17% reduction**)
- Overall scorecard: **2/4**

---

## 2. What closed, exactly?

This run gives a strong answer to the narrow mechanistic question.

### What [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] confirms

1. **The surviving [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] terminal residual was highly local and
   hinge-sensitive.**
   A tiny number of added internal Juzʾ-30 jumps is enough to collapse
   `L_mufaṣṣal-short` from a `+10.66σ` miss to:
   - `+0.43σ` in Cell A
   - `-0.56σ` in Cell B

2. **`Block-χ²` is no longer the bottleneck once these hinges are
   preserved.**
   Both cells move the empirical block statistic comfortably inside the
   simulator distribution:
   - Cell A percentile = `59.9`
   - Cell B percentile = `65.9`

3. **[[h-new-255-juz30-mini-cycle|H-NEW-255]]'s internal Juzʾ-30 jump structure is not merely
   descriptive.**
   It has genuine causal-generative bite inside the [[h-new-236-generative-simulator|H-NEW-236]] family.

### What [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] falsifies

It falsifies the strongest simple reading:

> "R12a is just the omitted internal Juzʾ-30 hinge list."

If that were the whole story, then once the omitted hinges were added,
the entire simulator should improve or at least remain globally stable.
Instead:

- `L_path` flips from a slight under-constraint at top-50
  (`emp - sim_mean = +0.062`)
  to a strong **over-correction**:
  - Cell A: `emp - sim_mean = -0.749`
  - Cell B: `emp - sim_mean = -0.910`
- `L_tail_91_114`, which was already inside at top-50, becomes
  dramatically too long in the simulator:
  - top-50 baseline mean `9.459`
  - Cell A mean `10.503`
  - Cell B mean `10.657`
  - empirical remains `8.640`

The added terminal hinges therefore solve the local block cost but
destroy the global balance.

---

## 3. Revised interpretation of the terminal frontier

[[h-new-236-1a-extended-hinges|H-NEW-236.1a]] had already shown:

- global `L_path` can be matched
- ḥawāmīm can be closed
- the only visible remaining miss is mufaṣṣal-short

[[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] adds the missing refinement:

- **front-loaded internal Juzʾ-30 hinges are real and load-bearing**
- but they are **not sufficient by themselves**
- the canonical mushaf must also preserve a **countervailing
  tail-shortening pressure** in the back end of the terminal block

The surviving causal-generative problem is therefore best restated as a
two-force balance:

1. **Preserve the major internal Juzʾ-30 jumps**
2. **Keep Q 91-114 unusually short overall**

The simulator can now satisfy either side much more easily than it can
satisfy **both at once**.

That is a materially sharper scientific statement than the pre-run one.

---

## 4. Implication for OQ-15

OQ-15 does **not** close here.

What changes is the shape of the remaining uncertainty.

### State after [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]]

- **Descriptive layer**: closed
- **Quantitative layer**: closed
- **Causal-generative layer**: still open, but now localized to a
  **terminal balancing mechanism**, not to a diffuse residual and not to
  a generic "missing hinge list"

The next question is no longer:

> "Should we add more terminal hinges?"

It is:

> "What late-tail compression / liturgical / prosodic / recitational
> pressure lets the mushaf keep the key Juzʾ-30 jumps while still making
> Q 91-114 as short as it empirically is?"

---

## 5. Classical-scholarship integration

This result strengthens rather than weakens the classical frame.

1. **The terminal short-mufaṣṣal really does behave as a specially
   organized region.**
   Its internal jumps are not noise; preserving a few of them radically
   changes the simulator.

2. **But the region is not reducible to a raw high-jump list.**
   The canonical order maintains those jumps while also protecting a
   short closing tail. That is exactly the kind of coupled recitational /
   liturgical ordering pressure classical scholarship would expect in the
   closing surahs.

3. **[[h-new-255-juz30-mini-cycle|H-NEW-255]] and [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] now fit together tightly.**
   Juzʾ 30 is a mini-geodesic open path with scale-specific hinges, but
   the mushaf-scale terminal architecture imposes an additional whole-tail
   constraint not captured by Juzʾ-30 local hinges alone.

---

## 6. Honest limits

1. **This was a targeted hinge test, not a new mechanism test.**
   It tells us omitted internal hinges are important; it does not tell us
   what the compensating late-tail mechanism is.
2. **The pre-registered added hinges come from a prior landed result
   ([[h-new-255-juz30-mini-cycle|H-NEW-255]]).**
   That is methodologically acceptable here, but the carry-over should be
   described honestly as a mechanistic follow-up to a prior descriptive
   ranking.
3. **A 2/4 score does not demote the local success.**
   The entire value of the finding is that the local success coexists with
   global failure, which constrains the next model much more sharply.
4. **Top-10 is already an over-correction on `L_mufaṣṣal-short`.**
   That does not mean the real mechanism is "fewer than 10" in a literal
   sense; it means the simulator needs another balancing force if these
   jumps are to be preserved without inflating the tail.

---

## 7. Next moves

- **Highest EV**: a terminal balancing-mechanism test, not another blunt
  top-K sweep.
- Candidate directions:
  - a **late-tail compression** test focused on Q 91-114
  - a **split-terminal** model that preserves the front Juzʾ-30 hinges
    while separately constraining the back tail
  - a **prosodic / recitational pressure** variant for the terminal block
    rather than a pure Fisher-Rao hinge extension

## 8. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1c-targeted-mufassal-hinges-prereg.md`
- Script: `scripts/h_new_236_1c_targeted_mufassal_hinges.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-236-1c.json`
- Journal: `journal/h-new-236-1c-run-1.md`

## 9. Final statement

**[[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] shows that the strongest internal Juzʾ-30 hinges are
causally real but not causally sufficient.** They collapse the isolated
mufaṣṣal-short residual and make `Block-χ²` pass, yet they overshoot the
global path and especially the Q 91-114 tail.

The complete equation is therefore not waiting for "more terminal
hinges" in the generic sense. It is waiting for the **terminal
counter-balance** that lets the mushaf preserve those hinges while still
closing short.
