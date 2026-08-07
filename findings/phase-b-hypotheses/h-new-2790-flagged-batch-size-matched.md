---
finding_id: H-NEW-2790
title: Five flagged claims through one size-matched null — the mushaf predictors are size, the chronology predictor keeps a small real residual, and the qul density claim sits on its own bar
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
target_claims: [H-NEW-192, H-NEW-183, H-NEW-233, H-NEW-74 Cell 6, H-NEW-231]
prereg: findings/phase-b-hypotheses/prereg-h-new-2790-flagged-batch.md
prereg_sha256: 6bb7e77a100810e31743734cd105407d6d21cf6d477dee1a9096c5ebde6014a8
run: findings/phase-b-hypotheses/runs/h-new-2790/20260807T053241Z/
rule_applied: findings/UNIT-DRIFT-DEFECT.md
method_parent: [H-NEW-2770, H-NEW-2760, H-NEW-2680]
seeds: 20260509 primary / 20260519 replication
n_perm: 500 Ridge / 100 RF / 10000 Kruskal-Wallis
status: >-
  Eight model cells and one density cell against a null that permutes the ordering within
  quantile bins of its own strongest drift channel. Under the locked primary stratification:
  five GENRE-SHARED-BUT-LARGER, one DOES-NOT-SURVIVE, two DID-NOT-REPRODUCE, and one
  SEED-FRAGILE. Under the pre-registered SECONDARY stratification every mushaf-position cell
  fails, three of six falling BELOW their own null mean. The calibration arm passed at
  rho = -0.9858 and both locked harness-invalidator directions held. Section 9 adds a post-hoc,
  descriptive reconciliation with an independent sweep of the same repository; it moves no
  verdict and is quarantined as such.
verdict: >-
  The mushaf-position predictors are size predictors. A SINGLE column - log surah word count,
  no vocabulary at all - reaches LOOCV R2 = 0.8378, beating H-NEW-192's reconstructed
  15-feature model (0.8026) by 0.0352 and H-NEW-233's published 29-feature Ridge model
  (0.7395) by 0.0983. At decile stratification a random size-matched RELABELLING of mushaf
  order is predicted BETTER than the true order, in both seeds. H-NEW-183 is the one predictor
  that survives every arm: its 12 features beat the strongest size baseline by +0.0413 (Ridge)
  and +0.0735 (RF) and clear the finer null at p = 0.0099 in both seeds - but its published
  "length-only baseline achieves R2 = 0.446" prices the wrong channel, and a one-column
  baseline on the right channel reaches 0.8005. H-NEW-74 Cell 6 survives per WORD in both
  seeds and straddles its own Bonferroni bar per VERSE.
---

# H-NEW-2790 — Five flagged claims, one harness, one size-matched null

**Pre-reg SHA-256 `6bb7e77a…6014a8`, runtime-verified. Twelve frozen inputs SHA-verified.
The feature matrices and the LOOCV routines are lifted from the frozen published scripts
`h_new_183_chronology_predictor.py` and `h_new_233_ensemble_predictor.py` as SHA-checked
modules; the parallel permutation worker is asserted **bit-identical** to the lifted routine
at startup (`0.845648348555`, exact equality, not a tolerance). Nothing was re-implemented.
Run 4,344 s.**

---

## 0. What this is

`findings/UNIT-DRIFT-DEFECT.md` established the rule: **when a density is divided by a unit
count whose size drifts across the ordering under test, the measure is testing the drift.**
It flags claims; it does not retire them. This is the batch that runs the tests.

Five claims, taken in load-bearing order by computed citation count, each through the same
arms: **A1** a size-only baseline (same model, same LOOCV, size columns only, no vocabulary),
**A2** a null permuting the ordering *within quantile bins of its own strongest drift
channel* — primary k = 5, secondary k = 10 — **A3** per-word re-normalisation of every
density feature, **A4** replication at a second seed. Directions, thresholds and the verdict
rule were locked before any of these numbers existed.

---

## 1. The nuisance channels reproduce the drift table exactly

Measured before the null was designed, as the standing rule requires:

| ordering | channel | ρ measured here | `UNIT-DRIFT-DEFECT` §3 |
|:--|:--|--:|--:|
| **mushaf position** | **log word count** | **−0.9342** | −0.9342 |
| mushaf position | verse count | −0.8446 | −0.8446 |
| mushaf position | mean verse length | −0.7131 | −0.7131 |
| **Nöldeke rank** | **mean verse length** | **+0.9038** | +0.9038 |
| Nöldeke rank | log word count | +0.6892 | +0.6892 |
| Nöldeke rank | verse count | +0.3903 | +0.3903 |

All six to four decimals. Cross-check ρ(mushaf, Nöldeke) = −0.6551. **The drift table is
independently confirmed**, and each claim's primary channel was locked on the measurement.

---

## 2. The instrument reproduces — except where no instrument exists

| cell | published | recomputed at the published seed | tol | reproduced |
|:--|--:|--:|--:|:-:|
| **H-NEW-233 Ridge** | 0.7395490015311565 | **0.7395490015311572** | 0.03 | **✓ to 15 digits** |
| **H-NEW-233 RF** | 0.848516936603147 | **0.848516936603147** | 0.05 | **✓ exactly** |
| **H-NEW-183 Ridge** | 0.836 | **0.8356** | 0.03 | **✓** |
| **H-NEW-183 RF** | 0.844 | **0.8438** | 0.05 | **✓** |
| **H-NEW-74 Cell 6** | H = 35.36 | **35.3570** (untied); qul total **332** exactly | 1.0 | **✓** |
| H-NEW-192 Ridge, RECON-A | 0.759 | 0.8026 | 0.03 | **✗** |
| H-NEW-192 Ridge, RECON-B | 0.759 | 0.8041 | 0.03 | **✗** |
| H-NEW-192 RF, RECON-A | 0.817 | 0.8485 | 0.05 | ✓ |
| H-NEW-192 RF, RECON-B | 0.817 | 0.8467 | 0.05 | ✓ |

**Where a computation exists, it reproduces — two of them to fifteen significant digits.**
Nothing here says any published arithmetic is wrong. What is challenged throughout is what the
numbers *measure*. **H-NEW-192 is the exception, and it is a defect of the record rather than
of a result** — §6.

One incidental detail: H-NEW-74's published `H = 35.36` is the **tie-uncorrected**
Kruskal–Wallis statistic; the tie-corrected value is **40.4086**, because 57 of 114 surahs have
`qul_density = 0`. The permutation p is unaffected — the tie correction is a constant factor of
the *pooled* value multiset, which every label permutation leaves invariant. Both are published.

---

## 3. The result — every cell, direction and magnitude

`S1` = the single strongest drift channel, one column. `S3` = `{log word count, verse count,
mean verse length}`, three columns, **no vocabulary, no morphology, no phonology**.
`ΔR² = R²_full − R²_S3`. Seed 20260509; the replication is §4.3.

| cell | ordering | R²_full | **S1** | **S3** | **ΔR²** | k=5 null mean | k=5 p | **k=10 null mean** | **k=10 p** | per-word | locked verdict |
|:--|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--|
| **C1** 192 RECON-A Ridge | mushaf | 0.8026 | **0.8378** | 0.8365 | **−0.0339** | 0.7191 | 0.0020 | **0.8101** | **0.7129** | 0.7923 | `DID-NOT-REPRODUCE` |
| **C1** 192 RECON-A RF | mushaf | 0.8414 | 0.7813 | 0.8119 | +0.0296 | 0.7581 | 0.0099 | **0.8224** | **0.2381** | 0.8486 | `GENRE-SHARED-BUT-LARGER` |
| **C1** 192 RECON-B Ridge | mushaf | 0.8041 | **0.8378** | 0.8365 | **−0.0324** | 0.7177 | 0.0020 | **0.8092** | **0.6832** | 0.7892 | `DID-NOT-REPRODUCE` |
| **C1** 192 RECON-B RF | mushaf | 0.8401 | 0.7813 | 0.8119 | +0.0282 | 0.7584 | 0.0099 | **0.8227** | **0.3333** | 0.8517 | `GENRE-SHARED-BUT-LARGER` |
| **C2** 183 Ridge | Nöldeke | 0.8356 | 0.8005 | 0.7943 | **+0.0413** | 0.7298 | 0.0020 | 0.7676 | **0.0099** | 0.8146 | `GENRE-SHARED-BUT-LARGER` |
| **C2** 183 RF | Nöldeke | 0.8432 | 0.7135 | 0.7697 | **+0.0735** | 0.7541 | 0.0099 | 0.7656 | 0.0476 | 0.8391 | `GENRE-SHARED-BUT-LARGER` |
| **C3** 233 RF | mushaf | 0.8460 | 0.7813 | 0.8119 | +0.0341 | 0.7581 | 0.0099 | **0.8245** | **0.1429** | 0.8511 | `GENRE-SHARED-BUT-LARGER` |
| **C3** 233 Ridge | mushaf | 0.7395 | **0.8378** | 0.8365 | **−0.0969** | 0.6724 | 0.0479 | **0.7629** | **0.8812** | 0.7688 | **`DOES-NOT-SURVIVE`** |

**The bolded S1 column is the finding.** `log(surah word count)` is one number per surah with
no vocabulary, no theology, no morphology and no register, and under Ridge LOOCV it predicts
mushaf position at **R² = 0.8378** — beating H-NEW-192's reconstructed 15-feature compositional
model (0.8026) by **0.0352** and H-NEW-233's published 29-feature Ridge model (0.7395) by
**0.0983**.

**C4 — H-NEW-74 Cell 6**, the one density claim, on its own statistic:

| arm | H | ε² | p, MVL-stratified (primary / replication) | p, free shuffle |
|:--|--:|--:|--:|--:|
| per **verse** (published form) | 40.4086 | 0.3401 | **0.00710 / 0.00870** | 1.0 × 10⁻⁴ |
| per **word** (re-normalised) | 34.5016 | 0.2864 | **0.00440 / 0.00350** | 1.0 × 10⁻⁴ |

Its own Bonferroni bar is α = 0.05/6 = **0.00833**. Stratified null means 31.17 and 24.28.
Phase means per verse 1.74 / 4.89 / 8.95 / 4.93, reproducing the published table; `qul` total
recovered as **332** exactly.

**C5 — H-NEW-231, the calibration arm.** ρ(KL divergence, log₁₀ token count) = **−0.9858**,
Pearson −0.8763, LOOCV R² from length alone **0.7552**. **Locked direction D4 passes** — the
harness recovers a known length-dominated result at ρ = −0.99. **D1 also passes** — size alone
reaches R² ≥ 0.70 on mushaf position, at 0.8365. Both were registered as harness invalidators:
*"if D1 or D4 fails, every verdict in this batch is void."* Neither failed.

---

## 4. Verdicts

### 4.1 The locked rule

Diffed clause-by-clause against pre-registration §6 before execution and again after.

```
DID-NOT-REPRODUCE        A0 outside its tolerance
DOES-NOT-SURVIVE         A2 p >= 0.01  OR  R2_S3 >= R2_full - 0.02
GENRE-SHARED-BUT-LARGER  A2 p <  0.01  AND 0.02 <= (R2_full - R2_S3) < 0.10
SURVIVES                 A2 p <  0.01  AND (R2_full - R2_S3) >= 0.10
```

`GENRE-SHARED-BUT-LARGER` is the team's label and **there is no genre arm in this batch**. It
carries here only its within-corpus sense: **the effect is largely the denominator, with a
real but small residual above it.** Nothing here compares this corpus to al-Bukhārī,
al-Jāḥiẓ or poetry, and no verdict may be read as such a comparison.

**One clause of my own pre-registration needed reading, and the stricter reading was taken.**
The C4 rule says `p_per_word >= alpha_pub` without saying which null the per-word p comes
from. The runner uses the per-word statistic **under the same size-matched null** — the
demanding reading, since the lenient one (per-word against a free shuffle) returns
p = 1.0 × 10⁻⁴ and would pass automatically. Both are published in §3 so a reader can apply
either. **The choice makes no difference to the verdict**: checked explicitly, the lenient
reading returns `SURVIVES` at 20260509 and `DOES-NOT-SURVIVE` at 20260519 — identically
`SEED-FRAGILE` — because it is the **per-verse** arm that straddles the bar, on either
reading of the per-word clause.

| claim | locked verdict | the one number |
|:--|:--|:--|
| **H-NEW-183** | `GENRE-SHARED-BUT-LARGER` | **+0.0413** (Ridge) / +0.0735 (RF) above the strongest size baseline; **the only claim that also clears the finer null**, p = 0.0099 in both seeds |
| **H-NEW-74 Cell 6** | **`SEED-FRAGILE`** — SURVIVES at 20260509, DOES-NOT-SURVIVE at 20260519 | per-verse p = 0.00710 / 0.00870 against α = 0.00833; **per-word p = 0.00440 / 0.00350 clears in both** |
| H-NEW-233 (RF cell) | `GENRE-SHARED-BUT-LARGER` | +0.0341 above size at k=5; **p = 0.1429 at k=10** |
| H-NEW-233 (Ridge cell) | **`DOES-NOT-SURVIVE`** | one size column beats 29 features by **0.0983** R² |
| H-NEW-192 (RF) | `GENRE-SHARED-BUT-LARGER` | +0.0296 above size at k=5 — **3 % of variance, not 80 %**; p = 0.2381 at k=10 |
| H-NEW-192 (Ridge) | `DID-NOT-REPRODUCE` | and no code in this repository produces its published numbers (§6) |
| H-NEW-231 | calibration passed | ρ = −0.9858; its own title was right. **Cite it as CLEAN.** |

### 4.2 The locked primary stratification was the more lenient of the two registered

**This must be stated plainly, because the verdicts above rest on it.** The pre-registration
locked k = 5 as primary and k = 10 as secondary. **At k = 10 every mushaf-position cell fails,
and three of the six fall BELOW their own null mean** — a random relabelling of mushaf position
*within decile bins of log word count* is predicted **better** by these compositional features
than the true mushaf order is.

| cell | observed | k=10 null mean | k=10 p | seed 20260519 |
|:--|--:|--:|--:|--:|
| 192 RECON-A Ridge | 0.8026 | **0.8101** | 0.7129 | 0.8145 / 0.7624 |
| 192 RECON-B Ridge | 0.8041 | **0.8092** | 0.6832 | 0.8139 / 0.7426 |
| **233 Ridge** | 0.7395 | **0.7629** | **0.8812** | 0.7650 / 0.8515 |
| 192 RECON-A RF | 0.8414 | 0.8224 | 0.2381 | 0.8215 / 0.0476 |
| 192 RECON-B RF | 0.8401 | 0.8227 | 0.3333 | 0.8216 / 0.0476 |
| 233 RF | 0.8460 | 0.8245 | 0.1429 | 0.8271 / 0.1429 |
| **183 Ridge** | **0.8356** | 0.7676 | **0.0099** | 0.7703 / **0.0099** |
| 183 RF | 0.8432 | 0.7656 | 0.0476 | 0.7674 / 0.0476 |

**This is the H-NEW-2680 shape exactly** — the baseline is more extreme than the corpus — and a
pass/fail report would have hidden it. I am not restating the verdicts, because the primary
arm was locked in advance and changing it after seeing the result is the error this project
retracted H-NEW-2600 for. **What I am doing is reporting that the locked primary was the
weaker test, that the registered secondary is unambiguous, and that the secondary agrees with
the size-only baseline while the primary does not.** A reader who wants the strict answer on
C1 and C3 should take the k = 10 row.

### 4.3 Replication

**Eight of nine cells return an identical classification at seed 20260519.** Every Ridge cell
is bit-identical (Ridge's fit is deterministic; only the permutation draws differ). RF values
move by at most **0.0101** — on the `S3` baseline, not on any full model, whose largest move is
0.0067 — and every ΔR² stays inside its band. The single divergence is **C4**, whose per-verse
Monte-Carlo p is 0.00710 at one seed and 0.00870 at the other against a bar of 0.00833. That is
not a change in the effect; it is a bar running through the middle of the estimate. That is what
`SEED-FRAGILE` is for and it is applied.

---

## 5. The three results that matter most

### 5.1 The "8 % mushaf–chronology gap" is the above-size residual, and it inverts the reading

H-NEW-192's headline inference is not an R². It is a **difference**:

> **Mushaf is ~8% LESS PREDICTABLE than Nöldeke from the same features.** … The ~20% residual
> … **IS the M1 structural placement signal.**

Published, that gap is 0.836 − 0.759 = **0.077**. Decomposed:

| | mushaf position | Nöldeke rank | difference |
|:--|--:|--:|--:|
| size-only baseline `S3` | **0.8365** | **0.7943** | mushaf **+0.0422** more predictable from size alone |
| model above size (`ΔR²`, Ridge) | **−0.0339** | **+0.0413** | Nöldeke **+0.0752** |

**The published gap of 0.077 and the above-size residual gap of 0.0752 agree to within
0.002.** The whole "8 % gap" is one fact: **Nöldeke rank carries compositional signal above
surah size and mushaf position does not.**

**That agreement should be read as suggestive, not exact**, because the mushaf half of it is
computed on a reconstruction of H-NEW-192's feature set rather than on the original, which no
longer exists (§6). What does *not* depend on the reconstruction is the sign and the order of
magnitude: RECON-B gives −0.0324 against RECON-A's −0.0339, and H-NEW-233's own published
29-feature Ridge model — no reconstruction involved — gives **−0.0969**, further negative
still. **Every mushaf-position model tested here has a negative above-size residual under
Ridge; the Nöldeke model is the only positive one.**

That inverts the inference rather than merely weakening it. The gap was read as *the mushaf
having an extra organizing principle beyond composition*. What it measures is that **the
mushaf ordering is more nearly a pure size ordering than the chronological ordering is** —
which is not a hidden principle, it is the sabʿ al-ṭiwāl → mathānī → mufaṣṣal arrangement the
tradition has described for twelve centuries.

**The "~20 % residual IS the M1 structural placement signal" claim is neither supported nor
refuted here.** What is shown is that the ~80 % it is a residual *from* is size, not
composition — so the residual is not "what is left after composition", and the arithmetic
that produced the 20 % does not license the interpretation attached to it.

### 5.2 H-NEW-183's published control priced the wrong channel — and the claim survives anyway

H-NEW-183 reports that its 12 features **"nearly double R²"** against a *"length-only baseline
[that] achieves R² = 0.446"*.

That baseline is **one column**, `log_length`, read from its own frozen output:
`csv/h-new-183.json → model_B_ridge_length_only.features == ["log_length"]`, `r2 = 0.44620`.
Measured on the frozen matrix: ρ(`log_length`, Nöldeke rank) = **+0.6775**; ρ(`log_length`,
whitespace log word count) = **+0.9995**; ρ(`log_length`, verse count) = +0.9096. **It is the
word-count channel — the middle of three — not the weakest and not the strongest.** The
strongest against Nöldeke rank is mean verse length at ρ = +0.9038, which H-NEW-183 did not use.

| baseline | columns | R² |
|:--|:--|--:|
| published "length-only" | `log_length` | 0.4462 |
| **S1 here** | **mean verse length alone** | **0.8005** |
| **S3 here** | log word count + verse count + mean verse length | **0.7943** |
| full 12-feature model | — | 0.8356 |

**One column on the correct channel reaches 0.8005 where the published baseline reached
0.446.** The model's honest advantage over size is **+0.0413 R²**, not a doubling.

**This corroborates `UNIT-DRIFT-DEFECT` §5's figure of 0.799**, which S1 and S3 bracket at
0.8005 and 0.7943 — while correcting that section's description of the *channel*: it states the
published baseline used *"verse count only (ρ = +0.390)"*; the source and the data both say log
word count (ρ = +0.6775). The mechanism the section teaches is untouched; the example's channel
label is wrong, and the published control was better than the section implies.

**And H-NEW-183 is the one predictor in this batch that survives everything.** It is the only
cell that clears the finer k = 10 null — at p = 0.0099, in both seeds, on the Ridge model —
and it does so on the ordering whose drift channel it did *not* control for. A small, real,
replicated effect: **+0.0413 R² of Nöldeke rank is compositional and not length.**

### 5.3 H-NEW-233's fourteen expansion features add 5.4 millionths of R²

A **15-feature** subset of H-NEW-233's own matrix — its `BASE_FEATURES`, used here as
H-NEW-192's RECON-A — reaches RF LOOCV **0.8485115815718597** at the published seed. Its own
**29-feature** model reaches **0.848516936603147**.

**The difference is 0.0000054 R².** The fourteen "expansion" features — nine phonological
means, KL divergence, Hurst exponent, LZ76 norm, entropy rate, and the α–β residual — together
move LOOCV R² by five parts in a million.

H-NEW-233's verdict is `PASS — beats H-NEW-192 baseline`, on H2 = *"RF R² > 0.817"*. That 0.817
is a hard-coded literal no code reproduces (§6), and the model it is meant to beat is matched to
five decimal places by fifteen of its own columns.

---

## 6. A defect of the record, not of a result: H-NEW-192 is not reproducible

Its `executed_by` field records an inline, unscripted run, and its Files section reads
`Script: inline (seed 20260419)`. There is no script path anywhere in the finding.

1. **No script exists.** There is no `h_new_192*.py` and no `csv/h-new-192.json`. A
   repository-wide search finds two files containing its numbers —
   `scripts/h_new_233_ensemble_predictor.py` and `scripts/h_new_250_equation_fit.py` — and in
   both they are **hard-coded literals**: `"h_new_192_baseline_ridge": 0.759`,
   `"h_new_192_baseline_rf": 0.817`. **No code in this repository computes 0.759 or 0.817.**
   **And in H-NEW-233 they are not annotations — they are the decision rule.** At
   `scripts/h_new_233_ensemble_predictor.py:531-533`, under the comment `# Pre-reg tests`:

   ```python
   # Pre-reg tests
   H1 = bool(r2_A > 0.759 and p_ridge < 0.025)
   H2 = bool(r2_B > 0.817)
   ```

   **H-NEW-233's published verdict is gated on two thresholds that no code in this repository
   reproduces.** Its `H2_rf_beats_baseline: true` is a comparison against a literal.
2. **Its feature set is under-specified.** The finding names **10** of its **15** features; two
   of the ten — `divine_name_density`, `legal_density` — are absent from H-NEW-233's
   `BASE_FEATURES` while the other eight are present. No journal entry and no CSV records the
   remaining five.
3. **Two reconstructions were pre-registered; both miss the Ridge number** by +0.044 and +0.045
   against a 0.03 tolerance, and both land inside tolerance on RF. They agree with each other
   to **0.0015** (Ridge) and **0.0018** (RF) — an order of magnitude tighter than either misses
   the published Ridge value by — so the miss is not reconstruction noise.

This is not an accusation that the numbers are wrong. It is the statement that **they cannot be
checked**, and that a claim which cannot be checked should not be carrying two downstream
scripts and the "complete equation" work. **Twelve markdown files across `findings/` and
`surahs/` assert both 0.759 and 0.817**, excluding this finding and its pre-registration —
among them `cross-finding-020-the-complete-equation.md`,
`cross-finding-021-mushaf-information-theoretic-optimality.md`,
`h-new-250-quantitative-equation-fit.md` and
`h-new-230-mushaf-nöldeke-block-decomposition.md`. (Scope matters for this count and should be
quoted with it: mine excludes stale worktree copies but *includes* pre-registrations, two of
which are in the twelve. The independent sweep counted fifteen on a slightly different scope.
The disagreement is bookkeeping; the fact is not.)

---

## 7. A methodological result: bin width is part of the null, and the coarse bin is not a control

Worth recording because it cost me an assumption and because it changes how the next batch
should be built.

**At k = 5 the C1 Ridge cells beat their size-matched null at p = 0.0020 while being beaten
outright by a single size column.** The two arms contradicted each other. At k = 10 they agree:
the models fall below the null mean, exactly as the baseline said.

The reason is mechanical, and it is the same defect the rule document already names, one level
up. **The model contains the nuisance variable as a feature.** Quintile bins leave 23 surahs
free to permute inside each, so a model holding `log_length` and `mean_verse_len` still predicts
the permuted target *within* bins using precisely the channel the stratification was meant to
neutralise. **A coarse stratification does not hold size fixed; it holds a five-level
approximation of size fixed, and leaves the model the residual to exploit.**

Three consequences, offered for `UNIT-DRIFT-DEFECT` §6:

1. **For a claim whose statistic is a fitted model containing size as a feature, the size-only
   baseline is the decisive arm** and the stratified null is a supporting one. The baseline
   asks the question that matters — *do the features add anything over size?* — and cannot be
   gamed by bin width.
2. **A stratified permutation null must declare its bin width as part of the null**, and report
   at least two. A single k is a free parameter that moves the answer from p = 0.0020 to
   p = 0.7129 on the same data.
3. **A stratified permutation is decisive for a correlation** — which is what H-NEW-2770 tested,
   correctly, since a Spearman ρ holds no size column — **and is not decisive for a regression
   that contains the stratifying variable.**

---

## 8. What survives, and at exactly its strength

**Two things survive, and both are smaller than they were published as.**

**(a) H-NEW-183's above-size residual — the strongest result in this batch.** Twelve
compositional features predict Nöldeke rank **+0.0413 R² (Ridge) and +0.0735 R² (RF) better
than the best size-only baseline**, and this is the only cell that clears the finer k = 10 null,
at p = 0.0099 in both seeds. **This is a real, replicated, size-independent chronological
signal.** It is also about 5 % of the published R², not the "nearly doubles" the finding claims,
because 0.8005 of its 0.8356 is reachable from mean verse length alone.

**(b) H-NEW-74 Cell 6 — real per WORD, on its bar per VERSE.** The honest statement is precise:

- **Per word the effect is robust**: p = 0.00440 and 0.00350 against α = 0.00833, comfortably
  inside in both seeds, with ε² = 0.2864 — a fall of only **15.8 %** from the per-verse 0.3401.
  **Late Meccan surahs say *qul* more often per word, not merely per verse.**
- **Per verse — the published form — it straddles its own bar**: p = 0.00710 and 0.00870 against
  0.00833. `SEED-FRAGILE`.
- **The matched null costs it roughly seventy-fold in p.** Against the free shuffle p = 1.0 ×
  10⁻⁴ (the floor at 10,000 draws); against the size-matched null 7.1 × 10⁻³. **The published
  `p = 1.02 × 10⁻⁷` is an asymptotic χ² against a free-shuffle null and is not the strength of
  this effect once verse length is held fixed.**

The honest headline is therefore not *"the qul-corpus is overwhelmingly a Late-Meccan
phenomenon"* at p = 10⁻⁷, but:

> **Late Meccan surahs say *qul* more often per WORD, and that survives a null matching mean
> verse length at p ≈ 0.004 — while the published per-verse form of the same claim sits exactly
> on its own Bonferroni bar.**

**This is the more interesting half of the result**, because it runs opposite to the pattern
this project has found all day: **the re-normalised statistic is the *stronger* one.** Every one
of H-NEW-2770's eleven axes weakened under per-word re-normalisation. Here the per-word form
clears its bar and the per-verse form does not — which is what it should look like when a
density claim is about words rather than about its denominator.

---

## 9. Post-hoc reconciliation with the independent sweep — descriptive only, no verdict moves

**Everything in this section was computed AFTER the verdicts above and after seeing them.**
It exists because a second lane screened the same repository independently and published an
inventory with numbers that touch mine. None of it is in the pre-registration, none of it
enters a decision rule, and no classification in §4 changes. It is reported because
reconciling two independent screens is worth more than either screen alone.

### 9.1 The other lane's size baseline reproduces exactly — and mine is not the same quantity

The sweep reported a size-only baseline of **0.799** for H-NEW-183 and correctly flagged that
it was a scratchpad figure with no run directory. On this harness:

| baseline | columns | Ridge R² |
|:--|:--|--:|
| **their two-column arm** | `log_length + mean_verse_len` | **0.7988** |
| mean verse length alone (my `S1`) | 1 | 0.8005 |
| **my `S3`** | log word count + verse count + mean verse length | 0.7943 |
| published "length-only" | `log_length` | 0.4462 |

**Their 0.7988 reproduces to four decimals.** The distinction they drew is real and worth
keeping: **H-NEW-183's feature matrix contains no verse-count column at all**, so their arm
answers *"what could H-NEW-183 have done with its own columns"* and mine answers *"what does
size explain in principle."* Note the ordering — **my three-column S3 is the LOWEST of the
three size baselines**, because verse count is nearly collinear with log word count
(ρ = +0.9096) and the extra column costs a little Ridge shrinkage for nothing. **All three
land in 0.794–0.801**, so the §5.2 conclusion is insensitive to which is used.

### 9.2 The mushaf channel — a live instance of the rule's own §5 clause

**This was not a slip in a message. It was the live instruction in the rule document.**
`findings/UNIT-DRIFT-DEFECT.md` §3 is the table a future session is told to use — its §6 step 2
says *"Look it up in the §3 table"* and step 3 says *"verify it targets the **strong** channel."*
In the version live when this pre-registration was locked (commit `b39b564ee`, lines 65–67) the
mushaf block read:

```
| **mushaf position** | **verse count**       | **−0.8446** |   <- bolded
| **mushaf position** | **mean verse length** | **−0.7131** |   <- bolded
|   mushaf position   |   log word count      |   −0.9342   |   <- not bolded
```

**Bolding is how that table signals which channel is primary, and the strongest channel is the
unbolded one.** A session following the document's own procedure would have locked verse count.
My pre-registration locked log word count instead only because the rule's *other* instruction —
rank the channels on the data before locking — was followed, and the two instructions
disagreed. Measured single-column Ridge LOOCV predicting mushaf position:

| channel | ρ with mushaf position | size-only Ridge R² |
|:--|--:|--:|
| **log word count** | **−0.9342** | **0.8378** |
| verse count | −0.8446 | 0.5386 |
| mean verse length | −0.7131 | 0.4133 |

**This matters more than a bookkeeping note.** Had verse count been locked as the primary
channel, the size baseline would have been **0.5386** — and H-NEW-192's reconstructed
15-feature model at 0.8026 would have cleared it by **+0.264 R²**, returning `SURVIVES` at the
top of the band. **The claim would have passed.** It is the "control on the weak channel"
clause of `UNIT-DRIFT-DEFECT` §5 reappearing **inside the document that states it**, in the
table that document tells the next session to trust — and it is the sharpest available argument
for that rule's own instruction to rank channels on the data before locking one. The two
instructions are not redundant; here one was wrong and the other caught it.

**The completing half of the table, which the sweep supplied and which explains how the error
was easy to make:**

| ordering | channel | ρ | size-only Ridge R² |
|:--|:--|--:|--:|
| **mushaf** | **log word count** | −0.9342 | **0.8378** |
| mushaf | verse count | −0.8446 | 0.5386 |
| mushaf | mean verse length | −0.7131 | 0.4133 |
| **Nöldeke** | **mean verse length** | +0.9038 | **0.8005** |
| Nöldeke | log word count | +0.6775 | 0.4462 |
| Nöldeke | verse count | +0.3903 | 0.0961 |

**The strongest channel is a different variable for each ordering, and the ranking fully
inverts**: log word count is strongest for mushaf and middling for Nöldeke; mean verse length
is strongest for Nöldeke and *weakest* for mushaf. **A channel cannot be carried across
orderings**, and ρ alone does not make this visible — −0.8446 and −0.9342 look adjacent, while
0.5386 and 0.8378 do not. **The size-only R², not the correlation, is the number that belongs
in a channel table**, because it is the bar the model must actually clear.

### 9.3 The sweep's item #6 — H-NEW-74's top-10 ranking — is not what I tested

I tested H-NEW-74 **Cell 6** (the phase Kruskal–Wallis). The sweep flags a different statistic
in the same file: the **top-10 surahs by qul density per 100 verses**. Re-cut per word, using
the exact identity `per-word = per-verse ÷ mean verse length`:

| | top 10 |
|:--|:--|
| per 100 **verses** (published) | Q34, Q62, Q6, Q112, Q13, Q10, Q39, Q67, Q113, Q17 |
| per 100 **words** | Q112, Q114, Q113, Q109, Q67, Q72, Q62, Q34, Q6, Q17 |

**Seven of ten survive.** Q10, Q13 and Q39 leave; Q72, Q109 and Q114 enter — and the leader
changes from Q34 (27.78 per 100 verses) to Q112 (6.67 per 100 words).

**The per-word ranking is arguably the better one on the finding's own terms.** H-NEW-74's
Cell 3 independently establishes the surah-initial *qul* set as **{72, 109, 112, 113, 114}**.
The per-**word** top ten contains **four** of those five; the published per-**verse** top ten
contains **two**. A denominator change that brings a ranking into agreement with the same
finding's other passing cell is evidence the per-word form is measuring the intended thing.

**This is a descriptive re-cut, not a test.** No null was run against it and it carries no
verdict.

---

## 10. Honest limits

1. **Conditioning on size may remove mechanism, not only confound — and for the mushaf this is
   near-certain.** The classical arrangement *is* a length arrangement. A size-matched null on
   mushaf position removes the organizing principle the tradition names. **The correct reading
   of C1 and C3 is not "the mushaf ordering is unstructured" but "these models measure the
   length arrangement and attribute it to composition."** Pre-registered as limit §10.1 and
   load-bearing for how the verdicts should be read.
2. **LOOCV R² on n = 114 is optimistically biased**, equally in every arm — which is why ΔR² is
   quoted throughout and why no single R² is a generalisation estimate.
3. **C1's verdict rests on a reconstruction.** Both are published; neither is H-NEW-192's actual
   matrix, which no longer exists in any form.
4. **The RF A2 bar is coarse by construction.** At 100 draws the locked rule requires the
   observed value to exceed the null maximum, so every passing RF cell reports p = 0.0099
   identically; the informative quantity is the margin, +0.0401 to +0.0452 at k = 5.
5. **Nöldeke chronology is a scholarly reconstruction, not data.** C2 and C4 inherit its
   uncertainty; nothing here tests it.
6. **No genre arm.** Nothing here compares this corpus to any other.
7. **C4's per-verse verdict is a Monte-Carlo boundary case, not a substantive disagreement
   between seeds.** With 10,000 draws the standard error on p ≈ 0.0083 is **0.00091**. The two
   estimates are **1.76 SE apart**, and they sit **1.36 SE below** and **0.40 SE above** the bar
   respectively — both consistent with a true p of about 0.008, which is the bar. More draws
   would settle which side it falls on; they would not make it a large effect, and the
   per-**word** arm is 4–5 SE clear of the bar in both seeds regardless.
8. **Five claims is not the inventory.** §11.

---

## 11. Garden of forking paths

- **Everything in §§3–8 was computed after the lock at SHA `6bb7e77a…`.** Recorded in prereg §9
  before the run: the citation ranking, each candidate's correction status, the six
  nuisance-channel correlations, the published headlines, the absence of a script for
  H-NEW-192, and the source-level reading that H-NEW-183's baseline is `log_length`. **The
  pre-registration predicted the §5.2 result and recorded that it contradicted the repository's
  own rule document, before running it.**
- **The nuisance channel was ranked on measurement, not judgement**, for both orderings.
- **D1 and D4 were declared as harness invalidators.** Both passed.
- **One implementation defect, found by the calibration arm and disclosed because that is what
  the arm is for.** My first KL implementation for C5 summed the divergence **only over token
  types present in each surah**, dropping the smoothed mass on unseen types — where the length
  dependence lives. It returned ρ = +0.0745 and would have read as a harness failure. Corrected
  to sum over the full vocabulary it returns ρ = −0.9858. **The bug was in my own calibration
  code, not in any tested claim, and no tested value was computed before it was fixed.**
- **Three engineering defects in the permutation harness, none of which touched a value.**
  `multiprocessing` with `fork` deadlocked against sklearn's thread pools; with `spawn` each
  worker re-executed the SHA preamble; and `joblib`'s default `batch_size="auto"` assigned every
  draw to a single worker while the rest idled at 0 % CPU. All three were wall-clock faults.
  **The permutation draw sequence is generated serially before any parallel dispatch, so
  parallelism cannot change a number**, and the parallel worker is asserted bit-identical to the
  lifted serial routine at startup.
- **The k = 5 / k = 10 divergence was not anticipated.** Both were pre-registered, k = 5 as
  primary; had only k = 5 been registered this finding would have reported a materially more
  favourable result for C1 and C3. **I have not restated the verdicts on the strength of the
  secondary arm** — that is the H-NEW-2600 error — but §4.2 gives the secondary its full weight.
- **Run directories are never deleted.** Eight calibration runs are retained beside the primary
  under `runs/h-new-2790-SMOKE/`, including the ones that failed on the harness defects above.
- **A run-immutability defect, and it is a design decision of mine rather than an accident.**
  Facing a multi-hour run on a saturated machine, I made the runner write `results.json`
  **incrementally, after every claim**, carrying `"partial": true` until completion — so a crash
  or a kill could not lose hours of work. That makes a file *inside the run directory* mutable
  while the run is in flight, which is in direct tension with this project's rule that a run
  directory is immutable. It then happened exactly as that tension predicts: commit `0db7171e2`
  captured `results.json` at `"partial": true` with 10 primary and 6 replication cells, and the
  completed file — 10 and 10, flag removed — was captured at `80bb535bf`. **Neither commit was
  mine; both were made by other lanes running `git add -A` while my run was executing.** But the
  commit is the trigger, not the cause: **the cause is that I wrote a mutable file under the
  name the run record is supposed to occupy.** The right fix is not "do not commit partial
  runs", which depends on nobody else's tooling touching the tree at the wrong moment; it is
  **write progress to a separate `progress.json` and write `results.json` exactly once, at
  completion**, so the run record is never mutable and no commit at any instant can capture it
  mid-flight. That is a one-line change and it is not made here, because changing the runner
  after the run would itself modify the record; it is registered as the correction for the next
  harness. **No published value is affected** — the completed `results.json` is what every
  number in this finding is read from, and the partial file was a strict prefix of it.

---

## 12. Flagged claims NOT reached — where the next session starts

The batch was five. Two independent screens of the same repository exist: mine, applied while
this pre-registration was being written, and the sweep's, which reached me after the lock. The
merged list below is authoritative and uses the **corrected** form of the sweep's ranking
metric — **distinct in-scope `.md` files citing the ID, over `findings/` + `surahs/`, preregs
excluded, stale worktree trees excluded, and a claim's own sub-findings excluded.** That last
clause was not in the original metric and adding it reorders the queue; the two clauses that
had to be added, and why, are set out below. The metric is still better than raw mention
counts, which double-count long files — but it required two corrections before it ranked
anything correctly, and it is reported here with them rather than on trust.

**The two highest-priority flagged claims in the repository were NOT reached by this batch.**

| pri | claim | external citers | statistic | denominator | ordering **or grouping** | strongest channel |
|--:|:--|--:|:--|:--|:--|:--|
| **1** | **H-NEW-126** — isolate core | **32** | cluster membership of {Q16, 21, 22, 23, 25} against random non-cluster surahs, across 20 cluster systems | per-surah density vectors | **grouping** — a five-surah core vs the rest | measure the group size contrast first; no ordering exists |
| **2** | **H-NEW-570** — muqaṭṭaʿāt content cluster | **27** | eight density measures, muq vs non-muq | verse count | **grouping** — 29 vs 85 | **mean verse length, 2.98× between the groups** (see below) |
| **3** | **cross-finding-012 / 016 / 017** — the Late-Meccan apparatus | **47** (union, not the summed 80) | Kendall's W = 0.8929 joint peak of four content axes; the B6/B7 staircase | **verse count** | Nöldeke bins B1–B8 | mean verse length (climbs **4.05 → 20.97**, 5.2×) |
| 4 | **H-NEW-2210** — qasam-jawāb inventory | 18 | per-surah oath rates | verse count | mushaf | **likely CLEAN-by-nullity** — `oath_density` is already null per-verse at ρ = −0.004 |
| 5 | **H-NEW-19** — extended classical anchors | 17 | nine density measures | verse count | mushaf | log word count |
| 6 | **H-NEW-49** — surah name class | 15 | six density measures | verse count | **grouping** — name class | adjacent to the withdrawn Pillar 4 |
| 7 | **H-NEW-236 Cell B** | 8 | ρ(mushaf position, KL) = +0.9201, sold as a "compositional-vocabulary gradient" | surah token count | mushaf | log word count (−0.9342) |
| 8 | **H-NEW-136 / 141 / 129** | 13 | the same four per-100-verse Pattern-B axes as pri-3 | verse count | Nöldeke / phase | mean verse length |
| 9 | **H-NEW-88** — letter-set predictor | 17 | multi-class RF for the muqaṭṭaʿāt letter-set | mixed | grouping | **not computed by either lane — a genuine open arm** |
| 10 | **H-NEW-74 Cells 1–5** | 22 | including the top-10-by-density ranking, re-cut descriptively in §9.3 but never tested | verse count | surah ranking | mean verse length |
| 11 | `surahs/Q047-muhammad/00-overview-comprehensive.md:132-136` | — | "highest Muhammad-naming density", 1.828 vs 1.783 | words | 4-surah ranking | **needs no run** — both numerators are **1**, so the density is exactly 1/length and the whole 2.5 % margin is that Q 47 is 2.5 % shorter |
| — | H-NEW-142, 123, 234 | 27 / 7 / 11 | — | — | — | **expected to come back CLEAN or already-dead**: H-NEW-142 is self-downgraded to SPECULATIVE-DESCRIPTIVE; H-NEW-123's β and K are fitted exponents, not ratios, and `N` is the size variable rather than a denominator |

**The top two were invisible to a screen written for orderings, and that is a hole in the rule
rather than an oversight.** H-NEW-126 compares a five-surah core against random non-cluster
surahs; H-NEW-570 compares muqaṭṭaʿāt against non-muqaṭṭaʿāt. **Neither is an ordering**, so
Screen B — "does unit size drift monotonically along this sequence" — is structurally incapable
of seeing them. **A grouping needs no trend to carry the defect. It only needs the groups to
differ in size.** Measured here on the split this project uses most, and reproducing the
sweep's figures exactly:

| muqaṭṭaʿāt (29) vs non-muqaṭṭaʿāt (85) | median muq | median non | ratio |
|:--|--:|--:|--:|
| mean verse length | 15.13 | 5.08 | **2.98×** |
| verse count | 85.00 | 26.00 | **3.27×** |
| word count | 928.00 | 214.00 | **4.34×** |

**Any per-verse density compared across that split is reading a threefold difference in verse
length** — and the direction is not an inference, it is this project's own `h-new-46`
STRONG-PASS result that muqaṭṭaʿāt surahs concentrate in long surahs. Screen B has since been
widened to "the ordering *or the grouping*", with a grouping-channel table beside the ordering
one.

**Two are already nearly settled, and neither needs a full run.** Pri-7 (H-NEW-236 Cell B): the
sweep computed ρ(mushaf position, **−log word count**) = **+0.9342**, *higher than the claimed
+0.9201 using no vocabulary at all*, and H-NEW-231 independently publishes ρ(log-length, KL)
= −0.967. Pri-11 (Q 047) is settled by inspection — both numerators are 1. Pri-9 (H-NEW-88) is
the one genuine open arm neither lane has touched; as a mushaf-side density model, §3's `S1`
column — **0.8378 from one size column** — is the number it must beat.

**Pri-3 carries a caveat that must be inherited.** The sweep's per-word re-normalisation moves
**3 of 4 peaks out of the Late-Meccan zone** (qul B7→B4, eschatological B6→B3, loanword B7→B4;
only `book_reference` holds at B7) — but its B1–B4 bin edges are *reconstructed octiles*,
because only the B6/B7/B8 rank ranges are published. B5–B8 reproduce the published table
exactly. **Anyone rerunning this must recover the exact bin edges from the runner rather than
trust the reconstruction.**

**CLEAN — named, per the rule's §4, so no run is spent on them:** H-NEW-239 (per-word density
plus a token-preserving null that exposes the short-surah inflation bias and finds the real
gradient running against it); **H-NEW-590** (tested by the sweep: ρ(Δ%ile, |log size deviation|)
= +0.062 over all 114 — with the caveat that Q 1's +27.09 is confounded at |log dev| = 4.90
while the corpus-wide ranking is not); **H-NEW-231** (clean by disclosure, and confirmed here at
ρ = −0.9858 against its published −0.967); H-NEW-46 (not a ratio); H-NEW-770's words-per-verse
arm (declared degenerate in pre-registration); H-NEW-91; and the per-1000-token work in
`surahs/Q009-al-tawba/06-novel-findings.md:43-93`.

**The two screens agreed on every claim they both saw** — no claim was ranked FLAGGED by one
and CLEAN by the other. But they did **not** agree on coverage, and the disagreement was
diagnostic rather than cosmetic: **the two highest-priority claims in the repository were
invisible to one of the screens by construction**, because Screen B was written for orderings
and both are groupings. Screen B has since been widened to cover both. **Running the same rule
twice, independently, is what found the hole** — a single application would have reported
convergence and missed 59 external citations' worth of flagged claims.

**The ranking did not converge at first, and resolving it changed the queue.** Two independent
implementations of the same one-sentence metric differed by up to 2.3×, which meant the metric
was under-specified as written. Two causes were found, both in the sweep's implementation and
both since corrected:

1. **The stated exclusion was not in the command** — preregs were described as excluded by
   filename and were not. Adding it brought most of the gap to zero (H-NEW-183 to 13, matching
   mine exactly).
2. **The metric itself was wrong**, and this is the substantive one: **a claim's own
   sub-findings were counted as citations of it.** H-NEW-236 has **11 own-family citers** —
   `h-new-236-1`, `-1a` … `-1h`, `-2a`, `-2b`, and the generative-simulator parent. A finding
   citing its own children measures productivity, not load-bearing-ness.

Excluding a claim's own family, the two counts now agree closely and **agree exactly on the two
that matter** — H-NEW-126 at **32** and H-NEW-183 at **12**:

| claim | external citers | own family | effect |
|:--|--:|--:|:--|
| **H-NEW-126** | **32** | 2 | **heads the unreached queue** |
| **H-NEW-570** | 27 | 1 | second |
| H-NEW-192 | 17 | 1 | — |
| H-NEW-183 | 12 | 1 | — |
| **H-NEW-236** | **8** | **11** | **falls from #1 to mid-pack** |

**A triage worked top-down from the original list would have started on the wrong claim.** The
sweep also reported the cross-finding-012/016/017 cluster at 80 by *summing* its three members,
which double-counts every file citing more than one — the honest union is **47**.

**Neither count is asserted here as exact**; small residual gaps remain and the two
implementations still differ by a few files on some IDs. What is established is that
**"load-bearing" needs a specified counting rule — with the family-exclusion and no-summing
clauses — before it can order a worklist**, and that a citation count cannot see a real
dependency anyway: H-NEW-233's hard-coded threshold on H-NEW-192 (§6) is a dependency no
citation count detects.

**One category neither screen has.** H-NEW-192 is not FLAGGED-vs-CLEAN at all; it is
**UNVERIFIABLE** — no script, an under-specified feature set, and headline numbers that exist
in this repository only as hard-coded literals (§6). A screen that only asks "is there a
size-fixing null?" cannot catch a claim that has no computation to null. That deserves to be a
third outcome alongside FLAGGED and CLEAN.

---

## 13. What should change in the project record

Flagged, not applied — a correction to another finding's file is not mine to make.

- **`h-new-192-mushaf-position-decomposition.md`** needs a correction notice on three counts:
  its numbers are not reproducible from the repository (§6); its "80 % compositional" is reached
  and beaten by one size column (§3); and its "8 % gap" is the above-size residual difference
  and inverts on inspection (§5.1). Its `verdict: STRONG PASS` should not stand unamended.
- **`h-new-233-ensemble-mushaf-predictor.md`**: its H2 PASS was scored against an unreproducible
  literal; its fourteen expansion features move LOOCV R² by 5.4 × 10⁻⁶ (§5.3); its Ridge cell
  `DOES-NOT-SURVIVE`, beaten by one size column by 0.0983 R².
- **`h-new-183-chronology-predictor.md`**: *"The length-only baseline achieves R² = 0.446 …
  nearly doubles R²"* should carry the corrected baseline of **0.8005** and the honest advantage
  of **+0.0413**. Its surviving residual should be stated — it is the strongest result in this
  batch and it deserves to be cited at that strength, not at 0.836.
- **`h-new-74-qul-distribution.md`**: Cell 6 should quote **p = 0.0044 per word and 0.0071 per
  verse under a mean-verse-length-matched null** beside its `p = 1.02 × 10⁻⁷`, note the
  `SEED-FRAGILE` per-verse boundary, and label its published `H = 35.36` tie-uncorrected.
- **`findings/UNIT-DRIFT-DEFECT.md`**, four items:
  1. §5's H-NEW-183 example names the wrong channel (verse count, ρ = +0.390) for a baseline
     that is log word count (ρ = +0.6775). **Its 0.799 figure is confirmed** — reproduced here
     at **0.7988** on its own two-column arm (§9.1).
  2. §6's diagnostic ordering should be amended per §7: **for a fitted model containing size as
     a feature the size-only baseline is decisive and the stratified null is not**, and any
     stratified null must declare and report **at least two bin widths**.
  3. **The mushaf ordering's strongest channel is log word count, not verse count** (§9.2).
     Locking verse count would have set the size baseline at 0.5386 instead of 0.8378 and
     returned `SURVIVES` for a claim that a one-column baseline beats outright. This is the
     rule's own §5 clause biting inside the inventory built to enforce it, and it is the
     strongest available case for the "rank the channels on the data first" instruction.
  4. **A third outcome is needed beside FLAGGED and CLEAN: UNVERIFIABLE** — a claim with no
     computation to null at all (§6). The three screens cannot see it, because Screen C asks
     what null exists and the answer presupposes a statistic that can be recomputed.
- **`STATE-OF-THE-PROJECT-2026-08-07.md`**: rows in §2 for H-NEW-192 and H-NEW-233; and in §1,
  H-NEW-183's +0.0413 above-size residual and H-NEW-74 Cell 6's per-word survival, both at their
  measured strength and not above it.

---

## 14. Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2790-flagged-batch.md`
  (SHA-256 `6bb7e77a100810e31743734cd105407d6d21cf6d477dee1a9096c5ebde6014a8`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2790.py` — pre-reg SHA-gated; lifts the
  H-NEW-183 and H-NEW-233 matrices and LOOCV as SHA-verified modules; asserts the parallel
  permutation worker bit-identical to the lifted serial routine
- JSON: `findings/phase-b-hypotheses/csv/h-new-2790.json`
- Runs (immutable, never deleted):
  `findings/phase-b-hypotheses/runs/h-new-2790/20260807T053241Z/` (primary, 4,344 s) and
  `runs/h-new-2790-SMOKE/` (eight calibration runs), each with a `manifest.json` recording every
  frozen input SHA in repository-relative form

---

*Run 2026-08-07 by Waiel Al-Shujaa. A rate is a ratio and the divisor is part of the claim —
and when the divisor is a feature of the model, the baseline settles it and the permutation
does not. Bismillāhi al-Raḥmāni al-Raḥīm.*
