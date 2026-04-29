# [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] — Extended hinges-constrained simulator: top-30 closes L_path exactly; top-50 collapses ḥawāmīm; the remaining causal-generative miss is isolated to mufaṣṣal-short

**Finding ID**: [[h-new-236-1a-extended-hinges|h-new-236-1a]]  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-1a-extended-hinges-prereg.md`  
**Pre-reg SHA-256**: `cf373a6a7b27847cfb0d9c4f6ccf42e934cf942e5e3b704505f55c65144183fe`  
**Seed**: 20260419  
**Parent**: [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] (top-15 hinges; 73% residual closure)  
**Grandparent**: [[h-new-236-generative-simulator|H-NEW-236]] → [[cross-finding-020-the-complete-equation|cross-finding-020]] (the complete equation)  
**Rules tuple**: `(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per [[h-new-111-fisher-rao-mushaf|H-NEW-111]], stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq constraints + TOP-K-HINGE-PRESERVATION for K in {30, 50})`  
**Verdict**: **MIXED / NEAR-GENERATIVE-CLOSURE — both top-30 and top-50 move empirical L_path INSIDE the simulated 95% CI, but both cells remain 3/4 overall because Block-χ² stays OUTSIDE HIGH, driven entirely by mufaṣṣal-short (Q 78-114). Top-50 fully closes ḥawāmīm; the remaining residual is now a single isolated block-level miss.**

---

## Headline

**[[h-new-236-1a-extended-hinges|H-NEW-236.1a]] confirms Reading A from [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] for ḥawāmīm but not for mufaṣṣal-short.**

Extending the hinge set from [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s top-15 to the pre-registered **top-30** and **top-50** consecutive Fisher-Rao jumps produces the following:

- **Cell A top-30**: empirical **L_path = 85.759655** lands essentially EXACTLY on the simulator mean **85.759788** and sits **inside** the simulated 95% CI **[85.113, 86.403]** at percentile **48.1**. Relative to [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]'s residual 1.7319-unit gap, this is **100.01% closure**.
- **Cell B top-50**: empirical **L_path** remains **inside** the simulated 95% CI **[85.167, 86.222]** at percentile **59.1**; simulator mean **85.697486**; remaining gap **0.0622 units** = **96.41% closure** of the [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] residual.
- **Neither cell reaches 4/4.** Both remain **3/4 overall** because **Block-χ²** stays outside the simulator distribution.
- The failing Block-χ² signal is now **almost entirely mufaṣṣal-short**:
  - **top-30**: ḥawāmīm is CLOSED (z = -0.040), mufaṣṣal-short remains **z = +10.90**
  - **top-50**: ḥawāmīm is CLOSED EXACTLY (**z = 0.0; zero variance because the block is fully hinge-locked**), mufaṣṣal-short remains **z = +10.66**

**Interpretation**: the causal-generative layer is now effectively solved at the global path-length level, but not yet at the block-distribution level. The remaining miss is no longer "R12 = ḥawāmīm + mufaṣṣal-short"; it has narrowed to a single residual: **mufaṣṣal-short within-block cost-excess.**

---

## 1. Primary-cell decisions

Per pre-reg §6, each cell was judged on two standards:

1. Does empirical **L_path** enter the simulator 95% CI?  
2. Do **all 4 observables** pass?

| Cell | Hinge set | L_path gap vs sim mean | Empirical L_path inside sim 95% CI? | 4/4 pass? | Pre-reg outcome |
|---|---:|---:|:---:|:---:|---|
| **A** | top-30 | **-0.00013** | **YES** (pct 48.1) | NO (3/4) | **NEAR-GENERATIVE-CLOSURE** |
| **B** | top-50 | **+0.06217** | **YES** (pct 59.1) | NO (3/4) | **NEAR-GENERATIVE-CLOSURE** |

The pre-registered "EQUATION-COMPLETE" threshold required **all 4 observables PASS**. That threshold is **not met**.

However, the strongest causal-generative question from [[h-new-236-generative-simulator|H-NEW-236]] and [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] was whether extending the hinge set would bring the empirical mushaf **inside** the simulator distribution on **L_path**. That answer is now unequivocally **YES** for both top-30 and top-50.

---

## 2. Observable-by-observable results

### Cell A — top-30 hinges

| Observable | Empirical | Sim mean | Sim 95% CI | Percentile of empirical | Verdict |
|---|---:|---:|---:|---:|---|
| **O1 L_path** | 85.759655 | **85.759788** | [85.113164, 86.403400] | 48.1 | **INSIDE** |
| O2 W_wrap | 0.388370 | 0.462195 | [0.338400, 0.626456] | 33.3 | **INSIDE** |
| O3 Block-χ² | 119.78 | — | sim 97.5 pct = 7.44 | 100.0 | **OUTSIDE HIGH** |
| O4 L_tail_91_114 | 8.639798 | 9.354958 | [7.946615, 10.939555] | 29.0 | **INSIDE** |

**Pass count**: 3/4.

### Cell B — top-50 hinges

| Observable | Empirical | Sim mean | Sim 95% CI | Percentile of empirical | Verdict |
|---|---:|---:|---:|---:|---|
| **O1 L_path** | 85.759655 | **85.697486** | [85.166949, 86.222065] | 59.1 | **INSIDE** |
| O2 W_wrap | 0.388370 | 0.457400 | [0.338400, 0.626456] | 34.4 | **INSIDE** |
| O3 Block-χ² | 115.52 | — | sim 97.5 pct = 5.24 | 100.0 | **OUTSIDE HIGH** |
| O4 L_tail_91_114 | 8.639798 | 9.459305 | [7.970010, 10.929007] | 25.6 | **INSIDE** |

**Pass count**: 3/4.

**Key comparative fact**: top-30 gives the better **L_path** fit; top-50 gives the better **block-level** fit for ḥawāmīm. The extra 20 hinges do not improve the one surviving failure because that failure now lives entirely in a region still unconstrained by the hinge set.

---

## 3. Block-χ² decomposition: what remains unsolved?

### Cell A — top-30

| Block | Empirical | Sim mean | Sim std | z | z² | Status |
|---|---:|---:|---:|---:|---:|---|
| L_ṭiwāl | 5.7244 | 5.8868 | 0.1650 | -0.98 | 0.97 | CLOSED |
| L_ḥawāmīm | 5.2054 | 5.2091 | 0.0920 | -0.04 | 0.00 | CLOSED |
| **L_mufaṣṣal-short** | **16.5149** | **15.6060** | **0.0834** | **+10.90** | **118.81** | **OPEN** |

### Cell B — top-50

| Block | Empirical | Sim mean | Sim std | z | z² | Status |
|---|---:|---:|---:|---:|---:|---|
| L_ṭiwāl | 5.7244 | 5.9592 | 0.1749 | -1.34 | 1.80 | CLOSED |
| **L_ḥawāmīm** | **5.2054** | **5.2054** | **0.0000** | **0.0** | **0.00** | **EXACTLY CLOSED** |
| **L_mufaṣṣal-short** | **16.5149** | **15.6194** | **0.0840** | **+10.66** | **113.72** | **OPEN** |

This is the decisive structural fact of [[h-new-236-1a-extended-hinges|H-NEW-236.1a]]:

1. **Top-30 already solves the global path-length problem.**
2. **Top-50 fully solves ḥawāmīm.**
3. **The only surviving miss is mufaṣṣal-short.**

In other words, [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]]'s Reading A ("the top-15 hinge list is a truncation") is **validated for ḥawāmīm**, but **not sufficient for mufaṣṣal-short**.

---

## 4. Why mufaṣṣal-short survives both cells

The reason is visible in the pre-computed hinge ranking itself:

- **Top-30** contains **no mufaṣṣal-short internal edges**
- **Top-50** still contains **no mufaṣṣal-short internal edges**
- The first mufaṣṣal-short internal edge remains **Q 78 -> Q 79 at rank 73**

So the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] result is not paradoxical. Extending from top-15 to top-50 successfully locks:

- the missing **ḥawāmīm** structure
- more of the middle and mufaṣṣal-long spine

But it still leaves **Q 78-114** largely free to re-optimise under within-block Fisher-Rao minimisation. The empirical mushaf keeps this region **~0.90 FR units longer** than the simulated mean:

- top-30: 16.5149 vs 15.6060
- top-50: 16.5149 vs 15.6194

This is the single surviving causal-generative miss.

---

## 5. Revised interpretation of the residual

[[h-new-236-generative-simulator|H-NEW-236]] gave a 6.31-unit L_path gap.  
[[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] reduced it to 1.73 units and proposed **R12 = ḥawāmīm + mufaṣṣal-short**.  
[[h-new-236-1a-extended-hinges|H-NEW-236.1a]] now sharpens that picture:

- **top-30**: residual on L_path is effectively zero
- **top-50**: residual on L_path is negligible (+0.062)
- **ḥawāmīm** is closed
- **mufaṣṣal-short** is the lone survivor

So the residual should now be restated as:

> **R12a — mufaṣṣal-short within-block cost-excess**

The ḥawāmīm half of R12 has been resolved by hinge-extension. The mufaṣṣal-short half has not.

This means the causal-generative layer is no longer blocked by a broad "missing hinge set." It is blocked by a **specific terminal block mechanism**.

---

## 6. What this means for [[cross-finding-020-the-complete-equation|cross-finding-020]] / OQ-15

### What is now confirmed

- The **global path-length** of the empirical mushaf is generatively recoverable under the 4-principle simulator once the hinge set is extended to top-30 or top-50.
- The **ḥawāmīm residual** of [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] was indeed a hinge-truncation artifact.
- M1.3 is not just "top-15 hinges"; it is a broader preserved-jump scaffold whose first 30 edges already recover the empirical **L_path** exactly.

### What is not yet confirmed

- The simulator still does **not** reproduce the empirical mushaf on the **block-distribution** observable.
- That miss is now isolated to **mufaṣṣal-short**.
- Therefore the strict pre-registered "all 4 observables PASS" standard for **EQUATION-COMPLETE** is still not met.

### Updated OQ-15 causal-generative verdict

**OQ-15 moves from "advanced but not closed" to "near-closed, with one isolated unresolved terminal-block mechanism."**

The honest state is:

- **Descriptive layer**: CLOSED and strengthened.
- **Quantitative layer**: CLOSED and strengthened.
- **Causal-generative layer**: **NEAR-COMPLETE, not yet fully complete**.

If one is asking specifically "can the model generate mushaf-equivalent global path length?" the answer is now **yes**.  
If one is asking "can it reproduce the full 4-observable profile?" the answer remains **not yet**.

---

## 7. Classical-scholarship integration

The classical implications sharpen rather than weaken:

1. **Ibn Taymiyya's moderated tawqīfī position** is strengthened.  
   The mushaf behaves like a block-structured order with deliberate preserved pivots, but the terminal short-surah region carries an additional organising pressure beyond generic FR minimisation.

2. **al-Zarkashī / al-Suyūṭī / al-Biqāʿī block knowledge** remains the correct scaffold.  
   The top-30 / top-50 preserved jumps recover the global path length without any need to abandon the classical block architecture.

3. **The remaining unsolved region is exactly where classical recitational/liturgical intuitions are strongest**: the short mufaṣṣal closing region.  
   That is a natural place to expect a mechanism not exhausted by root-distribution geometry alone.

This shifts the next question from:

> "Are hinges the right mechanism?"

to:

> "What is the terminal organising principle of Q 78-114 that keeps this block above its FR-minimum?"

---

## 8. Honest limits

1. **Top-30 and top-50 are still top-K truncations.** They do not include the first mufaṣṣal-short internal edge (rank 73), so they cannot be expected to solve that block completely.
2. **As K grows, the generator becomes less parsimonious.** A top-113 hinge set would trivially reproduce the canonical path. The meaningful fact here is that **top-30 already closes L_path**, not that arbitrarily many hinges could do so.
3. **Block-χ² remains a strict criterion.** It is useful precisely because it exposes where L_path closure can conceal a surviving local miss.
4. **Top-50 slightly worsens the exact L_path match relative to top-30.** More hinges do not monotonically improve every observable; they can overconstrain one region while leaving the actual surviving miss untouched.
5. **This run still uses the [[h-new-236-generative-simulator|H-NEW-236]] / 236.1 block partition and SA schedule.** Rule-tuple sensitivity and hotter-SA variants remain separate queued tests, not folded into this result.

---

## 9. Next moves

- **[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]** — explicit terminal-block mechanism test for mufaṣṣal-short. This is now the single highest-EV causal-generative follow-up.
- **[[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] / 236.1d** — targeted rank-73+ hinge extension restricted to mufaṣṣal-short, rather than a blunt top-K expansion.
- **[[h-new-260-q54-q55-dyad|H-NEW-260]]** — Q 54+Q 55 dyad deep-dive remains ready to execute, but it is now secondary to the newly isolated mufaṣṣal-short residual if the goal is closing OQ-15 first.

---

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1a-extended-hinges-prereg.md`
- Script: `scripts/h_new_236_1a_extended_hinges.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-236-1a.json`
- Journal: `journal/h-new-236-1a-run-1.md`
- Parent finding: `findings/phase-b-hypotheses/h-new-236-1-hinges-constrained-simulator.md`
- Equation synthesis: `findings/phase-b-hypotheses/cross-finding-020-the-complete-equation.md`

## 11. Final statement

**[[h-new-236-1a-extended-hinges|H-NEW-236.1a]] lands the strongest causal-generative advance of Wave-5's follow-up cycle: extending preserved Fisher-Rao hinges to top-30 or top-50 moves the empirical mushaf inside the simulator's L_path distribution, and top-50 exactly reproduces the ḥawāmīm block.**

The Complete Equation is therefore **not blocked by a diffuse residual**. It is blocked by **one isolated unresolved mechanism**:

> **mufaṣṣal-short (Q 78-114) remains systematically longer than its within-block FR-minimum, even after top-50 hinge preservation.**

That is the remaining frontier for causal-generative closure.
