---
title: The unit-drift defect — a mechanically detectable error in ratio statistics
author: Waiel Al-Shujaa
date: 2026-08-07
status: STANDING METHODOLOGICAL RULE — applies to every future ratio statistic in this repository
established_by: [H-NEW-740, H-NEW-2720, H-NEW-2730, H-NEW-2770]
applied_by: H-NEW-2780
---

# The unit-drift defect

## 1. The rule

> **When a density is divided by a unit count, and that unit's size drifts across the
> ordering being tested, the measure is testing the drift.**

A rate is a ratio. The divisor is part of the claim. If the divisor is itself a strong
correlate of the predictor, the ratio measures the divisor and not the numerator.

This is not a family of accidents. It is one error with one mechanism, and it is detectable
by inspection — **without recomputation** — using the three screens in §3.

---

## 2. The four cases that established it

Four major claims fell to this single mechanism on 2026-08-07. They are listed with the
number that settled each, because the rule is only as credible as its evidence.

| case | the claim | the denominator | the number that settled it |
|:--|:--|:--|:--|
| **H-NEW-125** → H-NEW-2770 | 11 of 15 content axes track the revelation sequence — "PERVASIVE CHRONOLOGY" | **verse count** (densities are `100 × count / n_verses`) | mean verse length rises **4.4×** across the Nöldeke sequence and correlates with rank at **ρ = +0.904** — stronger than most axes it reported. Under a null permuting rank *within mean-verse-length quintiles*, surviving axes fall **9 → 2**. `loanword_density` goes from ρ = +0.833 per verse to **+0.055 per word**. |
| **H-NEW-2690** → H-NEW-2730 | this corpus sits between poetry and prose in metricality | **unit length** (`d_min` is normalised by unit length) | re-cutting this corpus's **own verses** to ḥadīth sentence lengths moves `d_min` **99.4 %** of the way to ḥadīth's value — *using no baseline text at all*. |
| **H-NEW-660 / 730 / 770** → H-NEW-2720 | the compression tail (R² = 0.986) and the iʿjāz anti-twin (r = −0.86) are architecture | **unit size** (Fisher-Rao d̄ over units of unequal size) | log unit size **alone** explains **91.5 %** of the compression tail and **half** the anti-twin. Cut this corpus's own verses to equal size and R² collapses **0.9887 → 0.3388**. |
| **H-NEW-740** | the anti-twin discriminates this corpus from poetry at Δ Fisher-z = −6.42 | **block size profile** | it compared **equal 30-bayt** poetry blocks to this corpus's **unequal** surahs. Under a matched partition poetry reaches **r = −0.872** against this corpus's −0.870. Its honest-limits section named block size as the risk **and got the sign backwards**. |

**H-NEW-740 is the case worth studying.** It had a genuine, pre-registered cross-corpus
control and still got its answer backwards, because direction-of-bias reasoning is not a
substitute for matching. The driver was size **dispersion**, not size **level**.

---

## 3. The detection screens

A claim is **FLAGGED** if it hits all three. Apply them to the *statistic*, not to the prose.

### Screen A — the measure
Is the headline statistic a ratio with a **unit count in the denominator**?

Includes: per-verse, per-surah, per-word, per-pericope, per-window densities; anything
called a *rate*; any "normalised count"; any measure divided by, or tiled to, unit length;
any distance averaged over units of unequal size.

### Screen B — the ordering
Does the comparison run across an **ordering with monotone unit-size drift**?

The orderings in this repository that carry such drift are already measured. **Use this
table; do not re-derive it.**

| ordering | drift channel | Spearman ρ | source |
|:--|:--|--:|:--|
| Nöldeke / revelation rank | **mean verse length** | **+0.9038** | H-NEW-2770 §2; reproduced by H-NEW-2780 |
| Nöldeke / revelation rank | surah word count | +0.6892 | H-NEW-2770 §2 |
| Nöldeke / revelation rank | `log_length` *(= log word count; H-NEW-183's baseline feature)* | +0.6775 | H-NEW-2780; identity confirmed against `csv/h-new-123.json` `N` |
| Nöldeke / revelation rank | verse count | +0.3903 | H-NEW-2770 §2; H-NEW-125 axis 1 |
| **mushaf position** | **verse count** | **−0.8446** | H-NEW-2680 §8.1; reproduced by H-NEW-2780 |
| **mushaf position** | **mean verse length** | **−0.7131** | H-NEW-2780 (new) |
| mushaf position | log word count | −0.9342 | H-NEW-2780 (new) |
| surah-length rank | verse count | 1.000 by construction | — |

Nöldeke-rank bins (B1…B8) inherit the drift: mean verse length climbs monotonically
**4.05 → 20.97** words from B1 to B8, a **5.2×** rise (H-NEW-2780).

**Note the sign asymmetry.** Mushaf order and Nöldeke order drift in *opposite* directions
on verse length. A claim that holds on both orderings is not thereby robust — it may simply
be reading the same denominator twice.

### Screen C — the null
Does **any** null model hold unit size fixed?

Qualifying controls: stratified permutation within size quintiles; matched-partition
baselines with the size profile identical by construction; re-cutting the corpus's own
stream to equal size or to another arm's length profile; per-word (per-token)
re-normalisation; partial correlation controlling log unit size; regression on log size as
a competing predictor.

**Absence is the defect.** A control on the *weak* size channel does not qualify — see §5.

---

## 4. What FLAGGED means, and what it does not

**Flagging is not retiring.** A flagged claim may well survive its test; several already
have. H-NEW-2770's two theonym axes survived every arm. H-NEW-2730's poetry leg survived
every length control applied to it. Pillar 1 survived its nuisance parameter.

What flagging means is that **the claim has not yet been separated from its denominator**,
and no reader should treat it as established until it has been.

Equally, a claim that already holds size fixed is **CLEAN** and should be cited as such.
Getting this right deserves the credit, and naming the clean cases is part of the rule.

**FLAGGED / CLEAN is not an exhaustive partition.** A third outcome — **UNVERIFIABLE**, where
no code in the repository produces the claim's headline number — dominates both and must be
screened for first. See §6.2.

---

## 5. The standing requirement

**Any statistic in this repository that is a ratio must declare, in the finding itself, the
drift of its denominator across the ordering under test.**

Concretely, a finding reporting a ratio-statistic across an ordering must state:

1. **What the denominator is**, in words, as a quantity — not merely as a unit label.
2. **Its correlation with the ordering**, measured on the data, quoted beside the headline.
3. **Which null holds it fixed** — or an explicit statement that none does.

Three further clauses, each earned by a specific failure:

- **Rank the candidate nuisance channels on the data before locking one as primary.**
  H-NEW-2760 locked the weaker of two channels a priori (ρ = +0.1678) when the stronger was
  available (ρ = +0.4583), and its rate ratio fell from 2.580 to 1.694 against the stronger
  one. A cheap descriptive measurement of each candidate, *before* locking, ranks them
  correctly. H-NEW-2770 did this and it worked.

- **A control that does not use the strongest channel is not a control.** H-NEW-183 ran a
  length baseline on its `log_length` feature alone and reported that its 12-feature model beat
  it, 0.836 against 0.446. `log_length` is **log word count** — `_safe_log(N)` where `N` is
  H-NEW-123's token count, confirmed on the data (Q 1 al-Fātiḥa has `N = 29`, its word count,
  against 7 verses). That is the **middle** of the three channels at ρ = **+0.6775** with
  Nöldeke rank, not the weakest. But it is not the strongest either: **mean verse length at
  ρ = +0.9038 was never used as a baseline — it sat inside the feature set being defended.**
  Adding it takes the size-only baseline from 0.446 to **0.799**, against the full model's
  0.836. The control was real; it simply tested the wrong one of the two size channels it had
  in hand.

  *(Corrected 2026-08-07. This clause first read "verse count only (ρ = +0.390)", which
  misidentified the feature. The correction was supplied by the H-NEW-2790 lane from the frozen
  `model_B_ridge_length_only.features` field and independently re-measured here:
  ρ(`log_length`, Nöldeke rank) = +0.6775, ρ(`log_length`, verse count) = +0.9096,
  ρ(`log_length`, word count) = 1.000. The clause holds at reduced strength — the gap between
  the published baseline and a properly-channelled one is smaller than the original wording
  implied.)*

- **Normalisation is not invariance.** `d_min` divides by unit length and was described as
  "length-invariant by construction", yet length alone explains **28.7 %** of its variance,
  because a minimum over many templates falls as the string shortens. A statistic can be
  invariant in its *units* and not in its *distribution*. Only a measurement settles which.

---

## 6. How to apply this mechanically in a future session

0. **First, check the claim is computable at all** (§6.2). Does a script exist that produces
   its headline number, and does a result JSON contain it? If neither, stop — it is
   UNVERIFIABLE, and no null run against it will mean anything.
1. Grep the finding for a denominator: `_density`, `per verse`, `per 100 v`, `per word`,
   `/ n_verses`, `words per verse`, `normalised by length`, `mean unit size`.
2. Identify the ordering. Look it up in the §3 table. If it is not there, **measure the
   drift before proceeding** — one Spearman correlation, and it is not optional.
3. Grep for a size-fixing null using the §3 Screen-C vocabulary. Verify it targets the
   **strong** channel for that ordering, not merely a size-shaped word.
4. If A ∧ B ∧ ¬C: flag it, and name the one number that would settle it — the size-only
   baseline for a model-shaped claim (§6.1), otherwise the per-word re-normalisation or the
   partial correlation controlling log unit size.
5. **Do not change a verdict on the strength of the screens alone.** The screens identify
   what needs a measurement; only the measurement decides.
6. **If two nulls disagree, report both and take the stricter.** Disagreement between a
   lenient and a strict setting of the same null is a result about the null, and suppressing
   it is how a free parameter becomes a finding (§6.1).

**The cheapest decisive diagnostics.** *Which one to reach for first depends on the shape of
the claim — see the rule immediately below.*

- **The size-only baseline.** Run the published model on the unit-size columns alone. If it
  reaches the published R², the remaining features are decoration. **It has no free
  parameter, which is why it leads for any model-shaped claim.**
- **Per-word re-normalisation.** For a per-100-verse density, per-word density is
  `density ÷ mean verse length` exactly — no new data required, and it is a one-line change.
- **Partial correlation controlling log unit size.** One number, and it can change sign.
- **Self re-cut.** Cut the corpus's own stream to equal size, or to another arm's length
  profile, and re-measure. This is the strongest of the four because it uses no baseline
  text and so escapes the "a partition is not a composed book" caveat entirely.

### 6.1 A stratified permutation null is not decisive for a model that contains the stratifying variable

**Added 2026-08-07 from H-NEW-2790, which nearly lost a finding to this.** It is the unit-drift
rule applied one level up, to the *null* rather than to the statistic.

Stratified permutation — permute the target within quintiles of the drift channel — is the
H-NEW-2770 design, and **for a correlation it is decisive and remains so**: a Spearman ρ holds
no size column, so binning genuinely removes the channel. H-NEW-2770's verdict is untouched by
what follows.

**For a fitted model that contains size as a feature it is not decisive, because the bin width
is a free parameter that the model can see through.** Coarse bins leave substantial size
variation *inside* each bin — at quintiles on 114 units, about 23 units per bin — and the model
predicts the permuted target within bins using exactly the channel the stratification was meant
to neutralise. A finer stratification holds size more nearly fixed and is therefore the
stricter test.

The measured consequence, on H-NEW-192's model:

| null | result |
|:--|:--|
| permute within **quintiles** of the drift channel | p = 0.0020 — an apparent clean pass |
| permute within **deciles** | p = 0.7129; three of six mushaf cells fall **below their own null mean** in both seeds; H-NEW-233's Ridge cell reaches p = 0.8812 |
| **size-only baseline** (no free parameter) | a single size column beats the full model, **0.8378 against 0.8026** |

One free parameter moved the answer from p = 0.0020 to p = 0.7129 **on identical data**, while
the parameter-free diagnostic agreed with the stricter setting. At deciles a random relabelling
of mushaf position within size bins is predicted *better* by these features than the true mushaf
order is.

**Three requirements follow.**

1. **For a claim whose statistic is a fitted model containing size as a feature, run the
   size-only baseline FIRST.** It cannot be gamed by bin width.
2. **A stratified permutation null must declare its bin width as part of the null, and report
   at least two.** A single *k* is an undeclared researcher degree of freedom. If the two
   disagree, the finer bin is the honest one and the disagreement is itself the result.
3. **State which regime the claim is in.** Stratified permutation is decisive for a
   correlation; it is not decisive for a regression containing the stratifying variable.

*(H-NEW-2790 pre-registered both k values with k = 5 primary, so its locked verdicts stand on
the more lenient arm; its §4.2 gives the stricter arm full weight and says which a reader
should take.)*

### 6.2 A fourth outcome: UNVERIFIABLE

FLAGGED / CLEAN is not an exhaustive partition. A third state exists and this repository
contains at least one load-bearing instance of it:

> **UNVERIFIABLE — the claim's headline numbers are not produced by any code in the
> repository.**

**H-NEW-192 is the case.** Its finding file declares `Script: inline`
(`h-new-192-mushaf-position-decomposition.md:129`); there is no `h_new_192*.py`, and no
`csv/h-new-192.json`. Its headline **R² = 0.759 (Ridge) and 0.817 (RF)** exist in this
repository **solely as hard-coded literals** in two *other* findings' scripts —
`scripts/h_new_233_ensemble_predictor.py:532-533,571-572` and
`scripts/h_new_250_equation_fit.py:670-671`. **Nothing computes them.** The finding also names
only 10 of the 15 features it claims to use.

**And they are load-bearing as thresholds, not merely as citations.** H-NEW-233's
pre-registered decision rule is literally `H1 = bool(r2_A > 0.759 ...)` and
`H2 = bool(r2_B > 0.817)` — a downstream verdict gated on numbers no code in the repository
reproduces. Fifteen markdown files assert both values, including
`cross-finding-020-the-complete-equation.md`.

**Screen this before the other three, because it is cheaper and it dominates them.** A number
that cannot be recomputed cannot be flagged *or* cleared — running a size-matched null against
an unreproducible baseline measures nothing. The check is two commands: does a script exist that
produces this number, and does a result JSON contain it? If neither, the claim is UNVERIFIABLE
and the correct next step is to reproduce it from scratch, not to audit it.

---

*Written 2026-08-07 by Waiel Al-Shujaa, on the day four laws fell to one mechanism.
A rate is a ratio, and the divisor is part of the claim. Bismillāhi al-Raḥmāni al-Raḥīm.*

---

## 7. A process note on run immutability — a partial run is not yet a run record

**Recorded 2026-08-07 because it happened here.** The H-NEW-2790 run directory
`20260807T053241Z/results.json` was committed while it still carried `"partial": true`, and was
subsequently **completed in place** — the flag removed and 297 lines of additional cells added.

Under the standing rule ("nothing in a run directory may be overwritten, including uncommitted
and superseded ones") that is a modification of a committed run record.

**The honest reading, and the resolution:**

- The file declared itself incomplete. Finishing an in-progress computation is not the same act
  as revising a finished result, and the added cells extend the run rather than altering any
  verdict already in it. The three-line deletion is the `partial` flag itself.
- **But the error was mine, at the commit step.** A run marked `partial: true` is not yet a run
  record and should not have been committed as one. Once committed it acquires the immutability
  guarantee whether or not it was ready for it.

**Standing addition to the rule:** never commit a run directory whose result declares itself
partial. Either wait for completion, or — if the partial state must be preserved — commit it and
then write the completion to a **new** timestamped directory, retaining both. The immutability
guarantee is only meaningful if what it protects was finished when it was made.
