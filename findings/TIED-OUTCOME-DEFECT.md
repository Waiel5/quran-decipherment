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

---

## 7. Triage — and the filter that makes the screen usable

A first keyword sweep of findings mentioning counts or incidence, **excluding pre-registrations**
(per `UNIT-DRIFT-DEFECT.md` §9.1 — a sweep that hits pre-registrations will propose the exact edit
the rules forbid), returned **34 candidates**. That list is too crude to act on directly, and
treating it as 34 defective findings would be its own error.

**The sharpening comes from the defect's own direction. This defect is LIBERAL — it manufactures
findings.** Therefore:

- **A finding that NULLed under a parametric test on a tied outcome is DOUBLY SAFE.** It failed
  even under a test biased toward passing it. Re-testing it exactly can only move it further from
  significance. **These need no re-test**, and most of the 34 are in this class — the retired
  numerology series (H-NEW-2000, 2010, 2020, 2040, 2090), the exactness hunt, the conjunction
  tests, and the audits.
- **Only findings that PASSED on a parametric test over a tied outcome are at risk.** That is the
  actual triage list, and it is much shorter.

**The screen, stated correctly:**

> Tie fraction above ~50% **AND** a parametric primary test **AND** a passing verdict.
> All three, or there is nothing to re-test.

Applying the direction of a defect to prune its own candidate list is the general move here. A
defect that only inflates cannot have harmed a null, and a sweep that ignores this generates work
proportional to the corpus rather than to the risk.

**Not yet done:** enumerating which of the 34 actually passed on a parametric test over a tied
outcome. That requires reading each verdict and primary-test choice, and is the next step.

### 7.1 The triage list — candidates, not verdicts

Applying all three conditions (counts/incidence mentioned · no exact test mentioned · verdict not
already NULL) to findings only, **20 candidates remain** of the original 34. **This is a candidate
list and not a defect list**, and the distinction is the point: several entries are audits from
this same week that used exact or permutation methods without matching the keyword, and several
have multi-line YAML verdicts the screen could not read.

**Resolving each requires reading its actual outcome variable and primary test.** That has not
been done and is recorded as unfinished rather than asserted.

**The strongest single candidate is `h-new-1780-sahihayn-vs-sunan-distribution.md`** — verdict
`DESCRIPTIVE-CONFIRMED`, and its outcome is **per-surah ḥadīth citation counts**, which is exactly
the distribution H-NEW-2980 measured at **86% tied at zero**. It is the closest structural match
in the corpus to the case that established this rule, and it should be re-tested first.

Also worth reading before dismissing: `h-new-71-allah-distribution` (6 of 7 cells PASS),
`h-new-89-meta-cluster-network` (PASS, 2 of 3 cells), `h-new-45-muqattaat-surah-index-number-theory`
(PARTIAL-PASS), `h-new-263-divine-name-surah-network` (PASS-STRUCTURE-NO-HUB), and
`h-new-2080-rhyme-scan` (PASS-BOTH — though its outcome is a proportion rather than a sparse
count, so it is likely safe).

**A keyword screen produces candidates. Only reading the outcome variable produces a verdict.**
Publishing the candidate list as though it were a defect list would be the same error as
publishing a parametric p on a tied outcome — a number that looks like an answer and is not one.

### 7.2 First candidate read — and it CLEARS

`h-new-1780-sahihayn-vs-sunan-distribution.md` was §7.1's **strongest candidate**: verdict
`DESCRIPTIVE-CONFIRMED`, outcome apparently per-surah ḥadīth counts — the closest structural match
in the corpus to the case that established this rule.

**Reading its outcome variable clears it.** Its verdict is `DESCRIPTIVE-CONFIRMED`, and its own
honest-limits section states the finding measures **"the GRADE-MIX OF CITATIONS THE PROJECT HAS
MADE, not the GRADE-MIX OF ALL CLASSICAL ḤADĪTH on these surahs."** It is a **census of the
project's own citation practice**, not an inferential test against a null. **There is no
parametric p on a tied outcome to correct**, because there is no parametric p.

**A cleared candidate is worth exactly as much as a confirmed one**, and this one validates the
§7.1 discipline in the direction that matters: the keyword screen flagged it, the verdict field
flagged it, and **only reading the outcome variable resolved it — as clean.**

**Method note for the remaining candidates:** the decisive question is not *"does this finding
involve counts?"* nor *"did it pass?"* but **"is there a parametric p, computed on an outcome that
is mostly tied, carrying a verdict?"** A descriptive census, a Bonferroni-corrected permutation
test, and an exact enumeration are all immune regardless of how sparse their counts are. **The
defect lives in the test, not in the data.**
