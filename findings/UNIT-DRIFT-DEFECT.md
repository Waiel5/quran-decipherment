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

> **When a density is divided by a unit count, and that unit's size varies systematically
> across the comparison being made, the measure is testing the variation in size.**

A rate is a ratio. The divisor is part of the claim. If the divisor is itself a strong
correlate of the thing being compared, the ratio measures the divisor and not the numerator.

**"The comparison" covers both shapes.** An *ordering* — mushaf position, Nöldeke rank, juzʾ
position — where unit size drifts monotonically along it. And a *grouping* — muqaṭṭaʿāt vs
non-muqaṭṭaʿāt, Meccan vs Medinan, cluster-core vs the rest — where the groups simply differ
in size, with no trend required. The rule was first written for orderings only and was blind
to groupings for its first day; §3 Screen B records the extension.

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

### Screen B — the ordering *or the grouping*
Does the comparison run across an **ordering with monotone unit-size drift**, or across a
**grouping whose groups differ systematically in unit size**?

> **Extended 2026-08-07.** This screen originally read *ordering* only, and was therefore
> structurally blind to a whole class of claims: those comparing **two groups** rather than
> tracking a sequence. A grouping needs no monotone trend to carry the defect — it only needs
> the groups to differ in size. H-NEW-2790's screen caught this from the other direction; the
> generalisation is recorded here so the two screens agree.

The grouping channels measured in this repository:

| grouping | size gap (median) | source |
|:--|:--|:--|
| **muqaṭṭaʿāt vs non-muqaṭṭaʿāt** (29 vs 85) | mean verse length **2.98×**, verse count **3.27×**, word count **4.34×** | H-NEW-2780; the direction is H-NEW-46's own STRONG-PASS finding that muqaṭṭaʿāt surahs concentrate in long surahs |
| Meccan vs Medinan | inherits the Nöldeke drift above | H-NEW-125 / H-NEW-2770 |
| any cluster-core vs random-non-cluster comparison | unmeasured — **measure before using** | — |

**The muqaṭṭaʿāt split is the trap to watch**, because the project uses it constantly and its
own `h-new-46` established the confound. Any per-verse density compared across it is measuring
a 3× difference in verse length unless something holds size fixed.

The orderings in this repository that carry such drift are already measured. **Use this
table; do not re-derive it.**

Channels are listed **strongest first within each ordering**, and the strongest is bolded.
**The strongest channel differs between the two orderings — it is not the same variable — so
read the block for your ordering and do not carry a channel across.**

`ρ` is the Spearman correlation with the ordering. `size-only R²` is single-channel Ridge
LOOCV predicting the ordering from that column alone, on H-NEW-183's frozen pipeline; it is
the operationally decisive number for any model-shaped claim, because it is the bar the model
must clear.

| ordering | drift channel | ρ | size-only R² | source |
|:--|:--|--:|--:|:--|
| **mushaf position** | **log word count** ← strongest | **−0.9342** | **0.8377** | H-NEW-2780; confirmed 0.8378 by H-NEW-2790 |
| mushaf position | verse count | −0.8446 | 0.5386 | H-NEW-2680 §8.1; R² H-NEW-2780/2790 |
| mushaf position | mean verse length | −0.7131 | 0.4133 | H-NEW-2780 |
| **Nöldeke / revelation rank** | **mean verse length** ← strongest | **+0.9038** | **0.8005** | H-NEW-2770 §2; R² H-NEW-2780, bracketed by H-NEW-2790 |
| Nöldeke / revelation rank | surah word count | +0.6892 | — | H-NEW-2770 §2 |
| Nöldeke / revelation rank | `log_length` *(= log word count; H-NEW-183's baseline feature)* | +0.6775 | 0.4462 | H-NEW-2780; identity confirmed against `findings/phase-b-hypotheses/csv/h-new-123.json` → `N` |
| Nöldeke / revelation rank | verse count | +0.3903 | 0.0961 | H-NEW-2770 §2; H-NEW-125 axis 1 |
| surah-length rank | verse count | 1.000 by construction | — | — |

Nöldeke-rank bins (B1…B8) inherit the drift: mean verse length climbs monotonically
**4.05 → 20.97** words from B1 to B8, a **5.2×** rise (H-NEW-2780).

**Note the sign asymmetry.** Mushaf order and Nöldeke order drift in *opposite* directions
on verse length. A claim that holds on both orderings is not thereby robust — it may simply
be reading the same denominator twice.

> **⚠ This table previously got its own rule wrong, and the error is instructive enough to
> keep on the record.** Until 2026-08-07 it bolded **verse count (−0.8446)** as the mushaf
> channel and left log word count unbolded at the bottom of the block. A session following §6
> step 3 would have locked verse count as primary — **size-only R² 0.5386** — and a
> 15-feature model of mushaf position at 0.8026 would have cleared that by +0.264 and returned
> SURVIVES. Against the true strongest channel at **0.8377** the same model **fails**. The
> verdict turned entirely on which row of this table was bolded. Caught by H-NEW-2790 while
> building against it; all three single-channel R² values independently reproduced. **This is
> §5's "control on the weak channel" clause occurring inside the document that states it** —
> which is the best evidence available that ranking channels by measurement rather than by
> intuition is not optional.

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
screened for first. See §6.3.

### 4.1 The sharpest case: a flagged NULL can REVERSE into a positive result

**Added 2026-08-07 from H-NEW-2820, and it is the case that most changes how this rule should be
read.** Every other flagged claim in this document was an *over*claim waiting to be cut down.
H-NEW-570 was the opposite:

> **A published NULL — "the muqaṭṭaʿāt are not a content cluster", 30 external citing files —
> was an artefact of its own null. Size-matched, the muqaṭṭaʿāt-29 move from the 65.62nd
> percentile to the 0.45th and the ḥawāmīm-7 from 20.90 to 0.05. The sets ARE clustered.**

Three things follow that the rest of this document did not say.

1. **The defect is direction-agnostic.** A denominator that inflates a statistic for the group
   under test produces a *false negative* exactly as readily as a false positive. The screens in
   §3 were written while cutting down overclaims and their prose reads that way; **apply them
   with equal suspicion to any claim of absence.**
2. **A retired NULL propagates worse than a retired positive.** Downstream work inherits a
   positive as a citation; it inherits a NULL as **evidence of absence** — as a reason not to
   pursue something, or as a contrast case propping up a different claim. H-NEW-1760's whole
   frame is "whole-surah NULL → rescued at pericope scale"; H-NEW-600's is "the parent
   generalization VINDICATED". Neither survives its parent's reversal, and neither would have
   been found by grepping for the *number*.
3. **The cheapest decisive diagnostic in this document is not in the §6 list, and it should be.**
   Before computing anything, ask: **does the null model ever draw a comparison set like the
   observed one on the nuisance channel?** For H-NEW-570 the answer was **0 of 10,000**. That is
   one line of code, it needs no new statistic, and it settles the claim before any p-value —
   *a null that cannot draw the thing it compares against is not a comparison.* The mirror fact
   is equally cheap and equally decisive: for the muqaṭṭaʿāt split a size-matched comparison
   group **cannot be built from the 85 non-muqaṭṭaʿāt at all** (bin 3 of 5 needs 14 donors and
   contains 9), which is `h-new-46`'s STRONG-PASS stated as an impossibility.

**Add the grouping channel to §3's table when working the muqaṭṭaʿāt split:** dominant channel
for a Fisher–Rao `d̄` over root distributions is **log word count** (ρ = **+0.8998**), with log
root-set size second (+0.8554) and log verse count third (+0.8395) — *not* the same ranking as
for H-NEW-126's Jaccard, where log root-set size leads at +0.9398. **Rank on the data every
time; the winner changes between statistics on the same grouping.**

Sources: `findings/phase-b-hypotheses/h-new-2820-group-claims-matched.md`;
`findings/H-NEW-570-REVERSAL-2026-08-07.md`.

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

  **Rank by size-only R², not by ρ, whenever the claim is a fitted model.** The two orderings
  differ on which channel wins, and the gap is decisive: on mushaf position, log word count
  reaches R² **0.8377** while verse count reaches **0.5386** — a model scoring 0.80 passes
  against one and fails against the other. §3's own table got this wrong for months and the
  worked counterfactual is recorded there.

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

0. **First, check the claim is computable at all** (§6.3). Does a script exist that produces
   its headline number, and does a result JSON contain it? If neither, stop — it is
   UNVERIFIABLE, and no null run against it will mean anything.
1. Grep the finding for a denominator: `_density`, `per verse`, `per 100 v`, `per word`,
   `/ n_verses`, `words per verse`, `normalised by length`, `mean unit size`.
2. Identify the ordering. Look it up in the §3 table and **read only the block for your
   ordering** — the strongest channel is not the same variable for mushaf order as for
   Nöldeke rank. If your ordering is not in the table, **measure every candidate channel
   before proceeding**; one Spearman correlation each, and it is not optional.
3. Grep for a size-fixing null using the §3 Screen-C vocabulary. Verify it targets the
   channel with the **highest size-only R²** for that ordering, not merely a size-shaped
   word and not the first size variable you find. **This is the step that has failed most
   often** — in H-NEW-183, in H-NEW-2760, and once in §3's own table.
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

### 6.2 Ranking a worklist: specify the counting rule or do not rank

**Added 2026-08-07 after two careful implementations of the same one-sentence metric disagreed
by up to 2.3× and produced different orderings.** "Rank by load-bearing-ness" is not a
specification. If a triage is going to be worked top-down, the count must be reproducible, and
the following is the rule this repository uses.

**Count = the number of distinct `.md` files that reference the claim, where:**

- **scope** is `findings/` + `surahs/`, recursively;
- **excluded** are any path containing `/runs/` or `/scripts/`, any filename containing
  `prereg`, and any tooling or worktree directory;
- **the match** is the regex `h-new-<id>\b`, case-insensitive — the `\b` is load-bearing, since
  it stops `h-new-12` matching `h-new-125` while still allowing `h-new-236` to match a
  reference to `h-new-236-2a`;
- **and — the clause that actually matters — files belonging to the claim's own sub-finding
  family are excluded**, together with the file containing the claim itself. *(A claim's own
  file is not a citation of it. This resolves a 12-vs-11 discrepancy between two
  implementations: the larger count was including the target file.)*

**That last clause changes the answer, not just the number.** A finding with a large family of
sub-findings accumulates citations from its own children, which measure productivity, not
load-bearing-ness. Measured here:

| claim | all files | **external** | its own family |
|:--|--:|--:|--:|
| H-NEW-126 | 34 | **32** | 2 |
| H-NEW-570 | 31 | **30** | 1 |
| H-NEW-74 | 23 | **22** | 1 |
| H-NEW-192 | 20 | **19** | 1 |
| **H-NEW-236** | 26 | **14** | **12** |

H-NEW-236 was ranked **first** on a raw count and sits mid-pack on an external one, because
twelve of its citations are its own `-1a` … `-2b` sub-findings. **A triage ordered by the raw
count would have worked the wrong claim first.**

Two further rules follow from the same episode:

- **Never report a cluster's load by summing its members.** Summing cross-finding-012/016/017
  gave 80; the honest **union of external citing files is 47**. Summing double-counts every
  file that cites more than one member, which for a tightly cross-referencing cluster is most
  of them.
- **A count is a rough guide, not a queue.** Even fully specified, it measures how often a claim
  is *mentioned*, which is not the same as how much rests on it. H-NEW-233's verdict depends on
  H-NEW-192 through a hard-coded threshold (§6.3) — a dependency no citation count can see.

### 6.3 A fourth outcome: UNVERIFIABLE

FLAGGED / CLEAN is not an exhaustive partition. A third state exists and this repository
contains at least one load-bearing instance of it:

> **UNVERIFIABLE — the claim's headline numbers are not produced by any code in the
> repository.**

**H-NEW-192 is the case.** Its finding file declares `Script: inline`
(`findings/phase-b-hypotheses/h-new-192-mushaf-position-decomposition.md:129`); there is no `h_new_192*.py`, and no
`findings/phase-b-hypotheses/csv/h-new-192.json`. Its headline **R² = 0.759 (Ridge) and
0.817 (RF)** exist in this
repository **solely as hard-coded literals** in two *other* findings' scripts —
`scripts/h_new_233_ensemble_predictor.py:532-533,571-572` and
`scripts/h_new_250_equation_fit.py:670-671`. **Nothing computes them.** The finding also names
only 10 of the 15 features it claims to use.

**And they are load-bearing as thresholds, not merely as citations.** H-NEW-233's
pre-registered decision rule is literally `H1 = bool(r2_A > 0.759 ...)` and
`H2 = bool(r2_B > 0.817)` — a downstream verdict gated on numbers no code in the repository
reproduces. Fifteen markdown files assert both values, including
`findings/phase-b-hypotheses/cross-finding-020-the-complete-equation.md`.

**Screen this before the other three, because it is cheaper and it dominates them.** A number
that cannot be recomputed cannot be flagged *or* cleared — running a size-matched null against
an unreproducible baseline measures nothing. The check is two commands: does a script exist that
produces this number, and does a result JSON contain it? If neither, the claim is UNVERIFIABLE
and the correct next step is to reproduce it from scratch, not to audit it.

---

*Written 2026-08-07 by Waiel Al-Shujaa, on the day four laws fell to one mechanism.
A rate is a ratio, and the divisor is part of the claim. Bismillāhi al-Raḥmāni al-Raḥīm.*

---

## 7. A process note on run immutability — CORRECTED ATTRIBUTION

**Recorded 2026-08-07, then corrected the same day.** The H-NEW-2790 run directory's
`results.json` was written multiple times: it carried `"partial": true` at one point and was
later completed, with the flag removed and 297 lines of cells added.

**My first diagnosis was wrong, and the wrong diagnosis produced the wrong fix.**

I originally recorded this as *my* error at the commit step — "a run marked partial should not
have been committed as one" — and the remedy I wrote was "never commit a partial run." A second
lane contested the attribution and was right. The cause is in the script's design, verifiable at
`findings/phase-b-hypotheses/scripts/h-new-2790.py:733-737`:

```
def snapshot(partial=True):
    with open(os.path.join(rundir, "results.json"), "w", ...)
```

**The script writes progressive snapshots to `results.json` inside the run directory during
execution**, then overwrites it once more at completion (`:806`). It overwrites a file inside an
"immutable" run directory several times per run **regardless of whether anyone ever commits it.**

The commits were incidental in the strict sense: **the two that captured the file mid-flight
(`0db7171e2` at `partial: true`, `80bb535bf` after completion) were made by neither the lane that
owned the run nor the author of this document** — they were other lanes' `git add -A` firing
while the run was executing. Every lane commits under one shared identity, so git cannot
attribute them, and it does not need to: the defect is in the write pattern and would exist in a
tree that was never committed at all. "Never commit a partial run" would not have prevented it,
depends on every lane's tooling behaving at every instant, and following that remedy would have
left the real defect in place in every future script.

**The correct standing rule:**

> **A run script must never overwrite a file inside its own run directory.** Write the result
> once, at completion. If progress must be checkpointed — and for long batch runs it should be —
> write snapshots to a path OUTSIDE the immutable run directory, or to distinct
> `snapshot-NNN.json` files that are never rewritten.

An immutable run directory whose contents are rewritten by the very script that owns it provides
no guarantee at all. The directory was never the protection; **write-once** is.

**The generalisable lesson, which is why this is in the rule document rather than a changelog:**
a self-reported error with a plausible-sounding cause is still an unverified claim. I accepted my
own diagnosis without checking the script, and it took a second lane reading the code to find the
real mechanism. **Diagnose from the artifact, not from the narrative** — including, and
especially, when the narrative is your own confession.

---

## 8. Run these screens twice, independently — agreement is not coverage

**This is the most transferable thing the 2026-08-07 session produced, and it is a fact about
the screens rather than about any claim.**

Two lanes applied §3's three screens to the same repository, independently, on the same day.
**They agreed on every claim they both saw.** Every ordering-shaped claim one flagged, the other
flagged; the diagnostics reproduced to four decimals across separately built harnesses.

That agreement was worth almost nothing, because one screen was **structurally blind to an
entire class of claims**. §3 Screen B originally asked only about *orderings*. The two
highest-priority flagged claims in the repository — H-NEW-126 at 32 external citations and
H-NEW-570 at 30 — compare **groups**, not sequences. They were invisible to that screen by
construction. **Fifty-nine external citations' worth of flagged claims sat outside the screen's
reach while the screen reported clean convergence.**

**A single application of this rule would therefore have produced a confident, mutually
corroborated, incomplete answer.** Nothing inside that application could have revealed the gap,
because the gap was in the question being asked, not in the answering.

Three consequences, all of them cheap:

1. **Run the screens twice, from independently written implementations.** Not a re-read of the
   same list — a second construction of the search.
2. **When two applications agree, ask what they both could not see** before treating agreement
   as coverage. Convergence between two instances of the same blind spot is indistinguishable
   from convergence on the truth.
3. **Prefer a disagreement to an agreement.** Every disagreement in this session resolved into a
   correction: the channel identity, the stratification bin width, the ranking metric, the
   run-write pattern, and this screen's own scope. Not one agreement produced anything.

The same session supplied the case in miniature: **§3's drift table stated the wrong primary
channel, and only a second lane building against it noticed.** A rule document is not
self-checking, and neither is a screen.
