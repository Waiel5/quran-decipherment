---
id: cross-finding-030
title: Three ways a control fails silently — it does not discriminate, it does not apply, or it duplicates the treatment
date: 2026-08-10
author: Waiel Al-Shujaa
type: methodological
status: CONVERGENT — three anchors, three distinct mechanisms, all from 2026-08-10
---

# Cross-finding 030 — three ways a control fails silently

**Scope, stated first.** Like [[cross-finding-029-the-deciding-parameter]], this is a law about the
**instrument, not the text.** It asserts nothing about the Quran.

Cross-finding 029 said: *a free parameter you did not record decided your verdict.* This is its
complement. **The parameter here is not free — it is a control, deliberately chosen, explicitly
reported. And it still failed.** Three lanes on one day, three different mechanisms, none of which
announces itself.

---

## 1. The three anchors

| # | mechanism | anchor | what it looked like |
|--:|:--|:--|:--|
| 1 | **the control does not DISCRIMINATE** | [[h-new-3150-mubalagha-fasila]] | a rhyme control that merged two classes behaving oppositely |
| 2 | **the control does not APPLY** | [[AUDIT-TANWIN-DELETION-2690]] | a positive control blind to the encoding that broke |
| 3 | **the control DUPLICATES the treatment** | [[h-new-3120-asbab-chronology]] | ρ(control, treatment) = +0.79 to +0.91 |

### 1.1 Mechanism 1 — the control does not discriminate

H-NEW-3150 controlled for rhyme shape by extracting the rhyme from the **unvocalised** lemma. Arabic
writes long *ī* and the *ay* diphthong with the same letter, so:

| | unvocalised rhyme | verse-final rate |
|:--|:--|--:|
| *khayr, ghayr, ṭayr* | ير | **0 of 186 — 0.0%** |
| *khabīr, qadīr, naṣīr* | ير | **59 of 71 — 83.1%** |

**A never-final set and a usually-final set were pooled into one "rhyme class."** The comparison arm
did not rhyme with the treatment arm, and that merger supplied the entire +51% result.

**Signature:** the control runs, reports strata, and its strata are not homogeneous in the thing it
claims to hold fixed.

### 1.2 Mechanism 2 — the control does not apply

H-NEW-2690's positive control was three vocalised muʿallaqāt, scanned at 0.771 accuracy, 3 of 3
poems identified. It passed and **could not have failed**: the scanner deleted 6,643 tanwīn from the
Quran and **0** from every control corpus, because the muʿallaqāt do not use the Uthmānī codepoints
that broke.

**Signature:** the control corpus does not exercise the feature that breaks. An accuracy figure that
looks like validation is structurally incapable of being evidence about the defect.

### 1.3 Mechanism 3 — the control duplicates the treatment

H-NEW-3120 controlled a chronology hypothesis on mean verse length. But mean verse length **is**
chronology at surah granularity — ρ = +0.79 to +0.91, running 4.47 → 9.99 → 15.88 → 19.73 words per
verse across the four phases. The p-value moves monotonically with that collinearity: 0.0002 at
ρ=0.00, 0.0004 at 0.36, 0.0022 at 0.68, **0.2541 at 0.91**.

**Signature:** the stricter the control, the more it removes the effect — because it *is* the effect.

---

## 2. Why all three are invisible

Each produces a **well-formed control that is reported honestly and does the wrong thing**:

- Mechanism 1 reports strata. They are just not homogeneous.
- Mechanism 2 reports an accuracy. It is just measured on the wrong features.
- Mechanism 3 reports a residual. It is just the treatment's own shadow.

**In none of the three does the analyst omit a control, hide one, or choose one post hoc.** All three
lanes pre-registered theirs. That is what makes this distinct from 029 and worth its own file: **029
is a failure of disclosure; 030 is a failure of a disclosed thing.**

## 3. The three checks, one line each

| mechanism | check | cost |
|:--|:--|:--|
| does not discriminate | is the control variable **homogeneous within its strata** on the outcome? Compute the outcome rate per stratum member class. | one groupby |
| does not apply | does the **control corpus exercise the feature** the treatment corpus exercises? Count the feature in both. | one count |
| duplicates the treatment | what is **ρ(control, treatment)**? Report it beside every p. | one correlation |

All three were caught this way, and all three by the lane that built the control — not by an
outside reviewer.

## 4. What this does NOT license

**It does not license distrusting controls in general.** The correct response to a control that may
fail in one of these ways is to *run the one-line check*, not to discount the control.

Two of the three anchors ran the check and passed it: H-NEW-3080 takes its p as the maximum over all
non-degenerate length channels and survives; H-NEW-3130's within-root null is a control that works so
well it reproduces 95.7% of its own effect — which is a control **succeeding**, and the finding is
correspondingly NULL.

**A control that kills your result is doing its job.** Mechanism 3 is the only one of the three where
that inference is unsafe, and it is unsafe in a specific, measurable way: at ρ ≈ 0.9 no surah-level
design can separate "the control is right" from "the control is the treatment."

## 5. Honest limit

**Three anchors on one day is not three independent draws**, for the same reason 029 §2.2 gives:
these lanes were briefed to report their confounds before their primary tests, which is the
instruction that makes a broken control visible. Under a different briefing regime all three would
have produced clean-looking results. **This documents what a discipline surfaces, not a base rate.**

Related: [[cross-finding-029-the-deciding-parameter]] · [[AUDIT-TANWIN-DELETION-2690]] ·
[[h-new-3120-asbab-chronology]] · [[h-new-3150-mubalagha-fasila]] · [[UNIT-DRIFT-DEFECT]]

---

## 6. Extension 2026-08-11 — mechanism 1 applies to the STRATIFIER, not only the outcome

[[h-new-3190-translation-invariance]] registered **SUPPORTED** and its own lane refuses to believe
it. The reason is mechanism 1 in a place this file did not think to look.

The design stratifies on **`d`, the absolute token-edit distance** between two verses. But:

> **d = 3 on a 5-token verse is 60% of the verse. d = 3 on a 20-token verse is 15%.**

So the strata pool *nearly identical* pairs with *almost entirely different* ones — **strata not
homogeneous in the thing they claim to hold fixed**, which is exactly §1.1. The lane ran three length
channels on the **outcome** and none on the **stratifier**.

Its own locked §4.1 asserted the stratifier was safe *"because d is an exact integer count, not a
proxy."* **Exact is not the same as homogeneous**, and that sentence is now the cleanest one-line
statement of how mechanism 1 hides.

### 6.1 The hand-check that caught it — in the agreement direction

Pairs admitted as "near-twins" that **all ten translations agree are far apart**:

- **Q 23:3 ↔ Q 70:32**, d = 3 — *"who turn away from ill speech"* vs *"who are to their trusts and
  promises attentive."* Shared material: `والذين هم`.
- **Q 21:107 ↔ Q 36:17**, d = 3 — *"We sent you only as a mercy to the worlds"* vs *"we are
  responsible only for clear notification."* Shared material: `وما … إلا`.

Different verses on a shared syntactic frame. [[h-new-2380-near-twin-census]] set L ≥ 8, d ≤ 2
*precisely* to exclude that class; this lane widened to L ≥ 5, d ≤ 3 for power and re-admitted it.

### 6.2 The contrast is monotone in pool impurity

| relative-edit cap | n | contrast |
|:--|--:|--:|
| ≤ 0.15 | 92 | **−0.2333** |
| ≤ 0.20 | 132 | +0.0769 |
| ≤ 0.30 | 156 | +0.1723 |
| full pool | 417 | **+0.3580** |

**The result is a function of how much impurity is admitted.** And the pre-registered sensitivity on
H-NEW-2380's own window runs **negative on all three channels**.

### 6.3 And it declines to claim the reversal — because it computed the power

On the purest subset the contrast is −0.2333 with **p(reverse) = 0.317 and a null SD of 0.526**;
MDE ≈ 1.48. **On genuine near-twins the design has no power at all.** So F-18's honest status is
**UNTESTABLE at n ≈ 92**, not answered and not reversed. Refusing a reversal that would have been
more interesting than the null is the same discipline as refusing a favourable power figure.

### 6.4 The reusable measurement — the translator-noise floor

On the **59 exact Arabic twins** the mean cross-language rank spread is **0.6131**; on pairs whose
Arabic differs it is **0.4957**.

> **The ten translations disagree 1.24× MORE about verse pairs whose Arabic is *identical* than about
> pairs whose Arabic differs.**

Mechanism: with identical Arabic some translators produce identical output and others do not, so the
spread is maximal; with different Arabic everyone differs, so it compresses. **Any
translation-invariance instrument must clear that floor first.** This one does not.

