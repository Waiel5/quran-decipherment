---
id: H-NEW-3030
title: "Pre-registration — how much power did the sajdah-locus test actually have? An exact minimum-detectable-effect computation, and the surah-level confound contrast"
author: Waiel Al-Shujaa
date: 2026-08-09
status: PRE-REGISTERED — written and SHA-256-locked before any statistic in §4-§6 was computed
frontier_item: F-8 (HANDOFF/FRONTIER-MAP-2026-08-07.md:234)
prior_work: [H-NEW-2950, H-NEW-1330, H-NEW-1331, H-NEW-1510]
method_parents: [findings/TIED-OUTCOME-DEFECT.md, findings/ABSENCE-CLAIMS.md, findings/UNIT-DRIFT-DEFECT.md, findings/PROXY-CLAIMS.md]
seed: 20260509
---

# H-NEW-3030 — pre-registration

## 0. Why this exists, and what it is NOT

**F-8 has already been executed.** `h-new-2950-sajdah-loci.md` (2026-08-08) ran the census and the
exact test and returned NULL on imperative density (p = 0.4335) and second-person address
(p = 0.3588). **This pre-registration does not re-litigate that verdict and claims no novelty for
reproducing it.**

It exists because H-NEW-2950 **asserted** a power property it never computed, and because the
confound named in the F-8 brief was never contrasted. Its §4.4 reads:

> "The binding constraint at n = 15 is power, not p-resolution. The floors are small; what is
> scarce is the ability to detect a modest effect."

The three quantities it reports under the heading "power" are **p-value floors** — the smallest
attainable p — which are a statement about *resolution*, not about *power*. **No power was
computed, no minimum detectable effect was stated, and no alternative hypothesis was ever
specified.** Under `findings/PROXY-CLAIMS.md` and STANDING RULE 3 of 2026-08-07
(*"Never ASSERT a robustness property — COMPUTE it"*), an uncomputed power claim carrying a
published NULL is exactly the class of defect that rule names.

This pre-registration therefore locks:

- **Deliverable A** — an independent replication of the glyph census (documentary, no null model).
- **Deliverable B** — the **power computation**: an exact minimum detectable effect (MDE) for the
  H-NEW-2950 design, under two pre-specified alternative families and one model-free form.
- **Deliverable C** — the **confound contrast** the F-8 brief named and H-NEW-2950 did not run:
  a within-surah null *against* a corpus-wide null, plus a surah-level arm.

---

## 1. Honest disclosure — this pre-registration is NOT blind, and exactly which parts are not

**H-NEW-2950 is published and I have read it. I know the observed values before locking this
file.** Recording this plainly, because a pre-registration that conceals prior knowledge of the
outcome is worse than none.

| component | blind? | why it matters, or does not |
|:--|:--|:--|
| **B — power / MDE** | **YES, fully** | Power and the critical value **S\*** are functions of the *null distribution over the pools* alone. Neither depends on the observed statistic. Knowing the observation cannot bias a quantity it does not enter. |
| **C1 — within-surah arm** | **NO** | Reproduces H-NEW-2950's primary. Registered as a **replication**, explicitly claims no novelty, and **cannot** contribute a new PASS to this finding (§7.4). |
| **C2 — corpus-wide arm** | **YES** | Never run. No prior observation exists. |
| **C3 — surah-level arm** | **YES** | Never run. No prior observation exists. |
| **A — census** | n/a | A codepoint count. Documentary; carries no p-value. |

**Consequence, locked:** the headline verdict of H-NEW-3030 may rest only on **B, C2 and C3**.

---

## 2. Hypotheses

**H_B (power).** The H-NEW-2950 design, at n = 15 with surah- and length-matched pools, has
adequate power to detect a moderate elevation of imperative density and second-person address at
the sajdah loci.

**H_C (confound).** Any elevation at the sajdah loci is a property of the *loci*, not of the
*surahs that contain them* — i.e. it survives a within-surah null and is not merely inherited from
sajdah-bearing surahs being imperative-dense overall.

Both are stated in the direction that would make F-8 interesting. Both may fail.

---

## 3. Rules-tuple

**Primary tuple:**
`(no-tashkeel for the glyph census cross-check; QAC-v0.4 segment for features; QAC distinct word-index for length; verse as unit of analysis; basmala-counted-only-in-Q1; Ḥafṣ-Kūfan; Mashriqī)`

**Second tuple (sensitivity, locked):** pool width **K = 10** in place of K = 15, matching
H-NEW-2950's replication arm. Every quantity in B and C is computed at both widths.

**Third tuple (diagnostic only, NOT gated):** `ROOT:sjd` **included** rather than excluded — the
circular form. Reported to quantify the definitional component; **cannot support any PASS.**

---

## 4. Instrument, and the anti-circularity exclusion

- QAC v0.4, `data/morphology/quranic-corpus-morphology-0.4.txt`,
  SHA-256 `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46`.
- Glyph source `quran-text/quran-full-tashkeel.json`,
  SHA-256 `382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715`;
  cross-checked against `quran-text/quran-no-tashkeel.json`,
  SHA-256 `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a`.

**Features (identical to H-NEW-2950 §4.1, deliberately — a replication that changes the instrument
is not a replication):**

| id | definition |
|:--|:--|
| **F1 (primary)** | imperative count — segment has `POS:V` and `IMPV` |
| **F2** | second-person count — `(?:^\|\|)(?:PRON:)?2(?:MS\|MP\|FS\|FP\|D)(?:$\|\|)` |
| length | count of distinct QAC word indices in the verse |

**F3 (divine names) is DROPPED**, and this is a tightening, not a loosening: H-NEW-2950's own
post-hoc showed F3 to be residual circularity (p = 0.0023 → 0.209 once divine names governed by
the prostration verb are removed). Carrying it would inflate the family size and re-import a known
artefact. Dropping it reduces k from 3 to 2 per arm and therefore **tightens α**.

**Anti-circularity exclusion (locked):** every feature count removes all QAC segments carrying
`ROOT:sjd`. The tradition selected these loci *because they speak of prostration*; counting the
prostration word measures the selection rule, not the text.

---

## 5. Tie fractions — mandated by `findings/TIED-OUTCOME-DEFECT.md` §5

Computed over all 6,236 QAC verses **before** choosing a test, as that rule requires. These are
corpus-level properties and do not reveal any locus value.

| outcome | tied at zero | fraction |
|:--|--:|--:|
| **F1 imperative, per verse** | 4,967 / 6,236 | **0.7965** |
| **F2 second-person, per verse** | 3,177 / 6,236 | **0.5095** |
| F1 per surah | 21 / 114 | 0.1842 |
| F2 per surah | 6 / 114 | 0.0526 |

> **Both per-verse outcomes exceed the 50 % threshold at which `TIED-OUTCOME-DEFECT.md` §3 forbids
> a parametric p. Every primary test in this pre-registration is therefore EXACT** — a full
> convolution over the product space, never an asymptotic approximation. No parametric test appears
> anywhere in this design, including as a secondary.

This is also the reason the power computation must be exact rather than analytic: at a 79.65 % tie
fraction there is no usable normal approximation to invert for a sample-size formula.

---

## 6. Deliverable B — the power computation (locked before computing)

### 6.1 The critical value, model-free

For each axis and pool set, let `p_0` be the exact null pmf of **S = Σ_i X_i**, one uniform draw
per pool (H-NEW-2950's null, unchanged).

> **S\* := min{ s : P_0(S ≥ s) < α }** — the smallest total that would clear the gate.

Reported as a raw count alongside the null mean. No alternative model is required for S\*.

### 6.2 B1 — the quantile alternative (PRIMARY power model)

Under **H_A(q)**, each locus draws uniformly from the **top ⌈q·m⌉ members of its own pool by
value** (m = pool size, values sorted ascending, ties broken by taking the higher-valued members
first). q = 1 recovers H_0 exactly; q → 0 places every locus at its pool maximum.

> **Power(q) := P_{H_A(q)}(S ≥ S\*)**, computed by the same exact convolution.
> **MDE_q := the largest q at which Power(q) ≥ 0.80.**

Chosen as primary because it is non-parametric, respects each pool's actual support and its ties,
and states the effect in the one unit a reader can check by hand: *where in its own matched
neighbourhood does each locus have to sit?*

### 6.3 B2 — the exponential-tilt alternative (SECONDARY, rate-ratio form)

Under **H_A(θ)**, pool i's pmf is tilted: `p_θ(x) ∝ p_0(x)·e^{θx}`.

> **MDE_RR := E_θ[S] / E_0[S]** at the θ where Power(θ) = 0.80, found by bisection on θ ≥ 0.

Reported because "rate ratio" is this project's standing effect-size language
(INVESTIGATION-PROTOCOL correction notices) and because a Lehmann-type tilt is the conventional
exact-power alternative.

### 6.4 B3 — the lit-locus count (model-free, interpretive)

Starting from the configuration in which every locus takes its pool's **modal** value, promote
loci to their **pool maximum** one at a time, in the order that raises S fastest, until S ≥ S\*.

> **j\* := the number of promotions required.**

Interpretation, locked in advance: *at least j\* of the 15 loci must be the single most
imperative-dense verse in their entire matched neighbourhood before this design can register
anything at all.*

### 6.5 The locked power verdict rule

Applied to the **primary axis F1 at K = 15**:

| verdict | condition |
|:--|:--|
| **UNDERPOWERED-FATAL** | S\* exceeds the attainable ceiling Σ_i max(pool_i) — no configuration can reject |
| **UNDERPOWERED-SEVERE** | MDE_q ≤ 0.10 **or** MDE_RR ≥ 3.0 |
| **UNDERPOWERED-MODERATE** | MDE_q ∈ (0.10, 0.25] **or** MDE_RR ∈ [2.0, 3.0) |
| **ADEQUATE** | MDE_q > 0.25 **and** MDE_RR < 2.0 |

Where the two criteria disagree, **the more severe verdict is taken.** This is locked now,
before either number exists, precisely so that a disagreement cannot be resolved in whichever
direction proves convenient.

**The power verdict is reported in the abstract of the finding, not in its limits section.**

---

## 7. Deliverable C — the confound contrast

### 7.1 The three nulls

| arm | pool for locus/surah *i* | what it controls | what it leaves free |
|:--|:--|:--|:--|
| **C1** (replication) | {verse *i*} + K nearest-length non-sajdah verses **of the same surah** | surah **and** length | — |
| **C2** (new) | {verse *i*} + K nearest-length non-sajdah verses **from the whole corpus** | length (more tightly) | surah |
| **C3** (new) | {surah *i*} + K nearest-length non-sajdah **surahs**, K = 7 | surah length | — |

C1 and C2 use K = 15 primary / K = 10 sensitivity. Ties in |Δlength| are broken deterministically
by (surah, verse) ascending, so no seed enters pool construction.

Statistic in every arm: **S = Σ of raw integer counts**, a sum with **no denominator**
(`UNIT-DRIFT-DEFECT.md` Screen A: not a ratio). p is the **exact** upper-tail convolution.

### 7.2 Directions — LOCKED, with justification

**All arms one-sided UPPER.** Justification, stated before any result:

1. F-8's hypothesis is that the loci are *extreme* on these axes — over-representation, not
   difference. A two-sided test would answer a question nobody asked.
2. Prostration is a **commanded** act. The mechanism under test, if real, is that these verses
   carry directive force; directive force raises imperative and second-person counts. There is no
   coherent account under which textual marking of a prostration point would *lower* them.
3. H-NEW-2950 locked upper on the same axes. A replication that flips the direction is not one.

**A reversal (observed below null expectation) is a pre-commit violation and is published as NULL
with full prominence**, per INVESTIGATION-PROTOCOL §1.8. It may not be re-read as a two-sided pass.

### 7.3 Bonferroni

Family = {C1, C2, C3} × {F1, F2} = **k = 6**.

> **α = 0.05 / 6 = 0.00833333**

Both raw and corrected p reported. The census (A) and the power computation (B) carry no p-value
and are not members of the family.

### 7.4 The decision rule — EXACT, and the runner's verdict function must match this section line by line

Let `p(arm, axis)` be the exact one-sided upper p, and `dir(arm, axis)` be true iff observed >
null expectation.

**Primary test: C1-F1.**

```
PASS(arm, axis)  :=  dir(arm, axis) AND p(arm, axis) < 0.00833333
```

**Headline verdict, evaluated in this order — first match wins:**

1. `if PASS(C1,F1) and PASS(C1,F2)`  → **SUPPORTED-BOTH-AXES**
2. `elif PASS(C1,F1)`                → **SUPPORTED-PRIMARY**
3. `elif not dir(C1,F1)`             → **NULL — PRE-COMMIT VIOLATION (reversed)**
4. `elif PASS(C2,F1) or PASS(C2,F2) or PASS(C3,F1) or PASS(C3,F2)`
                                     → **CONFOUND-EXPLAINED**
5. `else`                            → **NULL**

**Locked interpretation of outcome 4, written now so it cannot be re-read later:**

> **C2 and C3 do not control for surah. A pass in either while C1 fails localises the signal at
> surah level — which is precisely the confound the F-8 brief named — and is therefore evidence
> AGAINST F-8's claim that the individual loci are textually marked, not evidence for it.**
> **CONFOUND-EXPLAINED may never be reported as support for F-8.**

**Locked constraint from §1:** because C1 is not blind, outcomes 1 and 2 are recorded as
**replication of H-NEW-2950**, claim no novelty, and are reported alongside H-NEW-2950's published
p-values in the same table.

**C3 carries a known bias, stated in advance.** Sajdah surahs are long, so for the longest of them
the K nearest-length non-sajdah surahs are systematically *shorter*, biasing the observed sum
**upward** — toward a PASS. Therefore: **a C3 NULL is strong** (it fails even under a bias toward
passing), and **a C3 PASS is ambiguous** between surah-level marking and length bias and must be
reported as ambiguous. Mean |Δ length| per pool is reported as the diagnostic.

### 7.5 Novelty gate

A PASS at §7.4 is labelled **PASS-DIRECTED**. It is upgraded to **PASS-NOVELTY** only if
`min(1, 6·p) < 0.005`. Matches H-NEW-2950's gate structure at this family's k.

---

## 8. Runtime enforcement

1. `EXPECTED_PREREG_SHA` = SHA-256 of this file, embedded in
   `findings/phase-b-hypotheses/scripts/h-new-3030.py`, verified at runtime; mismatch → `SystemExit`
   **before any run directory is created**.
2. QAC and both Qurʾān-text SHAs verified identically.
3. Locus set asserted against the census; any change → `SystemExit`.
4. Run directory `findings/phase-b-hypotheses/runs/h-new-3030/<UTC timestamp>/` created with
   `os.makedirs(..., exist_ok=False)`; every file opened `'x'`. **No run directory is ever deleted.**
5. Seed **20260509**. Seeds enter only the Monte-Carlo *correctness cross-check* of the exact
   convolution — never the inference, which is exact and deterministic.
6. `--self-check` unit-tests the convolution, the pool builder, the tilt and the quantile
   restriction against hand-computed values.

---

## 9. Power statement — written before the numbers exist

**n = 15.** This is not a large-sample design and no amount of exactness makes it one. The
pre-committed expectation, recorded now:

> I expect this design to be **UNDERPOWERED-SEVERE** on F1. The reasoning is available in advance
> and requires no result: 79.65 % of all verses carry zero imperatives once `ROOT:sjd` is removed,
> so most pools consist mostly of zeros, and a sum over 15 such pools has a null distribution
> concentrated on very small integers with large atoms. **Large atoms in the null are the
> signature of a design that can only see enormous effects.**

If that expectation is borne out, **the finding's headline is that F-8 was never answerable at
n = 15 by this instrument** — which is a materially different claim from H-NEW-2950's "NULL, and a
NULL is not evidence of absence." The first says the experiment could not have detected the effect;
the second says it did not. **Only a computed MDE distinguishes them, and that is this
pre-registration's reason for existing.**

If instead the design proves ADEQUATE, then H-NEW-2950's NULL is stronger than it claimed for
itself, and I will say so with equal prominence. **I do not know which of these will happen.**

---

## 10. Garden-of-forking-paths log

Decisions taken **before** any statistic in §6-§7 was computed, with the alternatives that were
available and rejected:

| # | decision | alternatives rejected | why |
|:--|:--|:--|:--|
| 1 | Reuse H-NEW-2950's pool builder and feature regexes **verbatim** | write a fresh instrument | A replication arm that changes the instrument is not a replication, and any divergence would be uninterpretable — instrument difference or effect? |
| 2 | Drop F3 (divine names) | keep it; keep it as diagnostic | Known circular from 2950's post-hoc. Dropping **tightens** α (k: 9 → 6). Per `feedback_bonferroni_tightening_vs_loosening`, a tightening self-verifies. |
| 3 | Quantile alternative as PRIMARY power model, tilt as secondary | tilt primary; normal-approximation power; simulation-only | Quantile is non-parametric, exact, and interpretable without a model. The tilt is reported because rate-ratio is the project's standing effect language. |
| 4 | 80 % power threshold | 90 %, 50 % | Convention. Locked before computation; the full curve is reported so any reader may apply their own threshold. |
| 5 | MDE severity bands at q ≤ 0.10 / ≤ 0.25 and RR ≥ 3.0 / ≥ 2.0 | other cut-points | Set to correspond to "top decile" and "top quartile" of a locus's own neighbourhood — thresholds a reader can interpret without reference to this design. |
| 6 | C3 surah pool K = 7 | K = 13, K = 5 | Only 100 non-sajdah surahs exist and the sajdah surahs skew long; K = 7 keeps the length match usable. **Chosen before any C3 statistic was computed.** |
| 7 | Corpus-wide tie in \|Δlength\| broken by (surah, verse) ascending | random tie-break under seed | Deterministic beats seeded here — pool construction should not depend on a seed at all. |
| 8 | Report both raw and Bonferroni p in every cell | corrected only | Protocol §1.5. |
| 9 | §1 disclosure of non-blindness written into the pre-registration itself | omit; mention in the finding | An undisclosed non-blind pre-registration is the failure mode the whole apparatus exists to prevent. |

**No statistic from §6 or §7 had been computed when this file was written.** The only numbers
computed in advance are §5's tie fractions, which `TIED-OUTCOME-DEFECT.md` §5 **requires** be
stated in the pre-registration, and the §4 file hashes.

---

## 11. What would falsify each deliverable

- **B is falsified** if the computed MDE shows the design ADEQUATE — in which case my §9
  expectation is wrong, published as such, and H-NEW-2950's NULL gains strength.
- **C is falsified** as a confound account if C2 and C3 both NULL while C1 also NULLs — no signal
  at any level, and the confound explanation is unnecessary because there is nothing to explain.
- **A is falsified** if the glyph census returns anything other than the 15 loci H-NEW-2950
  reports, in which case that finding's census is wrong and this becomes a correction.

---

*Pre-registered 2026-08-09 by Waiel Al-Shujaa, before computation. Bismillāhi al-Raḥmāni al-Raḥīm.*
