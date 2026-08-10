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
