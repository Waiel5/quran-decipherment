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

1. Grep the finding for a denominator: `_density`, `per verse`, `per 100 v`, `per word`,
   `/ n_verses`, `words per verse`, `normalised by length`, `mean unit size`.
2. Identify the ordering. Look it up in the §3 table. If it is not there, **measure the
   drift before proceeding** — one Spearman correlation, and it is not optional.
3. Grep for a size-fixing null using the §3 Screen-C vocabulary. Verify it targets the
   **strong** channel for that ordering, not merely a size-shaped word.
4. If A ∧ B ∧ ¬C: flag it, and name the one number that would settle it — usually the
   per-word re-normalisation, the size-only baseline, or the partial correlation controlling
   log unit size.
5. **Do not change a verdict on the strength of the screens alone.** The screens identify
   what needs a measurement; only the measurement decides.

**The cheapest decisive diagnostics, in order of cost:**

- **Per-word re-normalisation.** For a per-100-verse density, per-word density is
  `density ÷ mean verse length` exactly — no new data required, and it is a one-line change.
- **The size-only baseline.** Run the published model on the unit-size columns alone. If it
  reaches the published R², the remaining features are decoration.
- **Partial correlation controlling log unit size.** One number, and it can change sign.
- **Self re-cut.** Cut the corpus's own stream to equal size, or to another arm's length
  profile, and re-measure. This is the strongest of the four because it uses no baseline
  text and so escapes the "a partition is not a composed book" caveat entirely.

---

*Written 2026-08-07 by Waiel Al-Shujaa, on the day four laws fell to one mechanism.
A rate is a ratio, and the divisor is part of the claim. Bismillāhi al-Raḥmāni al-Raḥīm.*
