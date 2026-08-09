---
title: "The tied-outcome defect — a parametric p on a mostly-tied outcome is not approximately right, it is 13–57× wrong"
date: 2026-08-09
author: Waiel Al-Shujaa
status: STANDING METHODOLOGICAL RULE
established_by: [H-NEW-3000, H-NEW-2980]
family: [UNIT-DRIFT-DEFECT.md, ABSENCE-CLAIMS.md, PROXY-CLAIMS.md]
---

# The tied-outcome defect

## 1. The rule

> **Before choosing a test, measure what fraction of the outcome is tied. If a large share of
> observations share one value — usually zero — a parametric p is not approximately right. It is
> wrong by more than an order of magnitude, and it is wrong in the liberal direction.**

Parametric tests assume a continuous outcome. A count where most observations are zero violates
that assumption so severely that the resulting p-value is not a rough guide to the exact one — it
is a different number.

## 2. The case that established it

**H-NEW-3000** related a per-verse structural score to per-verse ḥadīth reception. **Reception is
86% tied at zero** — H-NEW-2980 measured it: only **749 of 5,371** eligible verses (13.9%) carry a
single citation, and the top 20 verses carry **21.3%** of all reception.

The pre-registered design happened to give **one** relationship both a parametric p and an exact
permutation null — `struct_z_composite` × `n_hadith`, registered as I1 and I2:

| test | p |
|:--|--:|
| parametric | **0.00015** |
| exact permutation | **0.0085** |

**A factor of 57.** Across the design the liberal bias ran **13–57×**.

The locked decision rule returned **SUPPORTED** on the parametric route. The exact tests return
**NULL**. Both are published, and the finding's §6 states plainly that the locked verdict should
not be believed.

## 3. The detection screen — one measurement, before the test is chosen

1. **Compute the tie fraction of the outcome.** What share of observations hold the modal value?
2. **Above ~50%, a parametric p is not usable.** Use an exact permutation null, or a rank test
   with an exact tie correction.
3. **Where both are available, report both.** Their disagreement is a diagnostic, and in
   H-NEW-3000 it was visible *inside the locked run itself* — nobody had to go looking.

## 4. Why this is a fourth defect class, not a special case

It has the same shape as the three in `UNIT-DRIFT-DEFECT.md`, `ABSENCE-CLAIMS.md` and
`PROXY-CLAIMS.md`:

- **mechanically detectable** without recomputation — one `value_counts()` on the outcome;
- **invisible when wrong**, because the parametric p looks like an ordinary small number;
- **liberal**, so it manufactures findings rather than suppressing them.

And it **compounds with the others**. A count outcome is exactly the kind of quantity that also
invites a per-unit rate — at which point `UNIT-DRIFT-DEFECT.md` applies too, and a single analysis
carries two defects that each make the other harder to see.

## 5. The standing requirement

**Any test on a count, an incidence, or any outcome that can be zero must state its tie fraction
in the pre-registration, and must justify a parametric choice against it.** Where the tie fraction
exceeds 50%, the pre-registration must specify an exact or rank-based test as primary.

## 6. Credit where it belongs

H-NEW-3000's lane was not asked to run the exact tests. It ran them, found its own locked verdict
unsupported, and led with that. **The second such self-disqualification in a week** — H-NEW-2960
discarded a p = 0.0028 instrument because its strongest *this-world* term was *qiyāma*, the
Resurrection. Neither was instructed to.
