---
finding_id: H-NEW-2790
title: Five flagged claims through one size-matched null — the mushaf predictors are size, the chronology predictor keeps a small real residual, and one density claim survives
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
target_claims: [H-NEW-192, H-NEW-183, H-NEW-233, H-NEW-74 Cell 6, H-NEW-231]
prereg: findings/phase-b-hypotheses/prereg-h-new-2790-flagged-batch.md
prereg_sha256: 6bb7e77a100810e31743734cd105407d6d21cf6d477dee1a9096c5ebde6014a8
run: findings/phase-b-hypotheses/runs/h-new-2790/
rule_applied: findings/UNIT-DRIFT-DEFECT.md
method_parent: [H-NEW-2770, H-NEW-2760, H-NEW-2680]
seeds: 20260509 primary / 20260519 replication
status: >-
  Eight model cells and one density cell, all against a null that permutes the ordering
  within quantile bins of its own strongest drift channel. One SURVIVES (H-NEW-74 Cell 6),
  five are GENRE-SHARED-BUT-LARGER in its within-corpus sense, one DOES-NOT-SURVIVE, and two
  DID-NOT-REPRODUCE. The calibration arm passed at rho = -0.9858.
verdict: >-
  The mushaf-position predictors are size predictors. A SINGLE column — log surah word count,
  no vocabulary at all — reaches LOOCV R2 = 0.8378, beating H-NEW-192's reconstructed
  15-feature model (0.8026) and H-NEW-233's published 29-feature Ridge model (0.7395) outright.
  Under Random Forest a small real residual above size remains, and it is 0.028 to 0.034 R2 —
  about 3 % of variance, not the ~80 % H-NEW-192 attributes to composition. H-NEW-183 is the
  healthiest of the three: its 12 features beat the strongest size baseline by +0.0413 (Ridge)
  and +0.0735 (RF), but its published "length-only baseline achieves R2 = 0.446" prices the
  wrong baseline — a size-only baseline on the correct channel reaches 0.8005.
---

# H-NEW-2790 — Five flagged claims, one harness, one size-matched null

**Pre-reg SHA-256 `6bb7e77a…6014a8`, runtime-verified. Twelve frozen inputs SHA-verified.
The feature matrices and the LOOCV routines are lifted from the frozen published scripts
`h_new_183_chronology_predictor.py` and `h_new_233_ensemble_predictor.py` as SHA-checked
modules; the parallel permutation worker is asserted **bit-identical** to the lifted routine
at startup (`0.845648348555`, exact equality, not a tolerance). Nothing was re-implemented.**

---

## 0. What this is

`findings/UNIT-DRIFT-DEFECT.md` established the rule: **when a density is divided by a unit
count whose size drifts across the ordering under test, the measure is testing the drift.**
It flags claims; it does not retire them. This is the batch that runs the tests.

Five claims, taken in load-bearing order by computed citation count, each put through the
same three arms: **A1** a size-only baseline (same model, same LOOCV, size columns only, no
vocabulary), **A2** a null that permutes the ordering *within quintiles of its own strongest
drift channel*, **A3** per-word re-normalisation of every density feature. Directions,
thresholds and the verdict rule were locked at the SHA above before any of these numbers
existed.

---

## 1. The nuisance channels reproduce the drift table exactly

Measured on this corpus, before the null was designed, as the standing rule requires:

| ordering | channel | ρ measured here | `UNIT-DRIFT-DEFECT` §3 |
|:--|:--|--:|--:|
| **mushaf position** | **log word count** | **−0.9342** | −0.9342 |
| mushaf position | verse count | −0.8446 | −0.8446 |
| mushaf position | mean verse length | −0.7131 | −0.7131 |
| **Nöldeke rank** | **mean verse length** | **+0.9038** | +0.9038 |
| Nöldeke rank | log word count | +0.6892 | +0.6892 |
| Nöldeke rank | verse count | +0.3903 | +0.3903 |

All six to four decimals. Cross-check ρ(mushaf, Nöldeke) = −0.6551. **The drift table is
independently confirmed** and the primary channel for each claim was locked on it.

---

## 2. The instrument reproduces — except where no instrument exists

| cell | published | recomputed at the published seed | tolerance | reproduced |
|:--|--:|--:|--:|:-:|
| **H-NEW-183 Ridge** | 0.836 | **0.8356** | 0.03 | **✓** |
| **H-NEW-183 RF** | 0.844 | **0.8438** | 0.05 | **✓** |
| **H-NEW-233 RF** | 0.8485 | **0.8485** | 0.05 | **✓ exact to 4 dp** |
| **H-NEW-233 Ridge** | 0.7395 | **0.7395** | 0.03 | **✓ exact to 4 dp** |
| **H-NEW-74 Cell 6** | H = 35.36 | **35.3570** (untied) | 1.0 | **✓** |
| H-NEW-192 Ridge, RECON-A | 0.759 | 0.8026 | 0.03 | **✗** |
| H-NEW-192 Ridge, RECON-B | 0.759 | 0.8041 | 0.03 | **✗** |
| H-NEW-192 RF, RECON-A | 0.817 | 0.8485 | 0.05 | ✓ |
| H-NEW-192 RF, RECON-B | 0.817 | 0.8467 | 0.05 | ✓ |

**Nothing here says any published computation is wrong** where a computation exists. Four of
four reproducible headline numbers reproduce, two of them exactly. What is challenged
throughout is what the numbers *measure*.

**H-NEW-192 is the exception, and it is a defect of the record rather than of a result** —
see §6.

**One incidental reproduction detail is worth recording**: H-NEW-74's published `H = 35.36` is
the **tie-uncorrected** Kruskal–Wallis statistic. The tie-corrected value is `H = 40.4086`,
because 57 of 114 surahs have `qul_density = 0` and the tie mass is large. The permutation
p-value is unaffected either way — the tie correction is a constant factor of the *pooled*
value multiset, which every label permutation leaves invariant — so this changes no inference.
Both are published here.

---

## 3. The result — every cell, direction and magnitude

`R²_full` = the published model. `S1` = the single strongest drift channel, one column.
`S3` = `{log word count, verse count, mean verse length}`, three columns, **no vocabulary,
no morphology, no phonology**. `ΔR²` = `R²_full − R²_S3`. All LOOCV, all seed 20260509.

| cell | ordering | R²_full | **S1** | **S3** | **ΔR²** | A2 null mean | A2 null max | A2 p | per-word | verdict |
|:--|:--|--:|--:|--:|--:|--:|--:|--:|--:|:--|
| **C1** H-NEW-192 RECON-A Ridge | mushaf | 0.8026 | **0.8378** | 0.8365 | **−0.0339** | 0.7191 | 0.8005 | 0.0020 | 0.7923 | `DID-NOT-REPRODUCE` |
| **C1** H-NEW-192 RECON-A RF | mushaf | 0.8414 | 0.7813 | 0.8119 | **+0.0296** | 0.7581 | 0.7962 | 0.0099 | 0.8486 | `GENRE-SHARED-BUT-LARGER` |
| **C1** H-NEW-192 RECON-B Ridge | mushaf | 0.8041 | **0.8378** | 0.8365 | **−0.0324** | 0.7177 | 0.8011 | 0.0020 | 0.7892 | `DID-NOT-REPRODUCE` |
| **C1** H-NEW-192 RECON-B RF | mushaf | 0.8401 | 0.7813 | 0.8119 | **+0.0282** | 0.7584 | 0.7995 | 0.0099 | 0.8517 | `GENRE-SHARED-BUT-LARGER` |
| **C2** H-NEW-183 Ridge | Nöldeke | 0.8356 | 0.8005 | 0.7943 | **+0.0413** | 0.7298 | 0.8020 | 0.0020 | 0.8146 | `GENRE-SHARED-BUT-LARGER` |
| **C2** H-NEW-183 RF | Nöldeke | 0.8432 | 0.7135 | 0.7697 | **+0.0735** | 0.7541 | 0.7994 | 0.0099 | 0.8391 | `GENRE-SHARED-BUT-LARGER` |
| **C3** H-NEW-233 RF | mushaf | 0.8460 | 0.7813 | 0.8119 | **+0.0341** | 0.7581 | 0.8059 | 0.0099 | 0.8511 | `GENRE-SHARED-BUT-LARGER` |
| **C3** H-NEW-233 Ridge | mushaf | 0.7395 | **0.8378** | 0.8365 | **−0.0969** | 0.6724 | 0.7904 | 0.0479 | 0.7688 | **`DOES-NOT-SURVIVE`** |

**The bolded S1 column is the finding.** `log(surah word count)` is one number per surah,
carries no vocabulary, no theology, no morphology and no register, and under Ridge LOOCV it
predicts mushaf position at **R² = 0.8378** — **better than H-NEW-192's reconstructed
15-feature compositional model (0.8026) and better than H-NEW-233's published 29-feature
Ridge model (0.7395), by 0.0352 and 0.0983 R² respectively.**

**C4 — H-NEW-74 Cell 6**, the one density claim, tested on its own statistic:

| arm | H (tie-corrected) | ε² | p, MVL-stratified | p, free shuffle |
|:--|--:|--:|--:|--:|
| per **verse** (published form) | 40.409 | 0.3401 | **0.00710** | 0.00010 |
| per **word** (re-normalised) | 34.502 | 0.2864 | **0.00440** | 0.00010 |

Stratified null mean 31.173 (per verse) and 24.283 (per word); 95th percentiles 37.027 and
30.167. Phase means per verse 1.74 / 4.89 / 8.95 / 4.93, reproducing the published table.

**C5 — H-NEW-231, the calibration arm.** ρ(KL divergence, log₁₀ token count) = **−0.9858**,
Pearson −0.8763, LOOCV R² from length alone **0.7552**. Locked direction **D4 passes**: the
harness recovers a known length-dominated result at ρ = −0.99, so a harness failure is not
what is producing the verdicts above. **D1 also passes** — size alone reaches R² ≥ 0.70 on
mushaf position, at 0.8365.

---

## 4. Verdicts against the locked rule

Diffed clause-by-clause against pre-registration §6 before execution and again after.

```
DID-NOT-REPRODUCE        A0 outside its tolerance
DOES-NOT-SURVIVE         A2 p >= 0.01  OR  R2_S3 >= R2_full - 0.02
GENRE-SHARED-BUT-LARGER  A2 p <  0.01  AND 0.02 <= (R2_full - R2_S3) < 0.10
SURVIVES                 A2 p <  0.01  AND (R2_full - R2_S3) >= 0.10
```

`GENRE-SHARED-BUT-LARGER` is the team's label and **there is no genre arm in this batch**. It
carries here only its within-corpus sense: **the effect is largely the denominator, with a
real but small residual above it.** Nothing in this finding compares this corpus to
al-Bukhārī, al-Jāḥiẓ or poetry, and no verdict here may be read as such a comparison.

| claim | verdict | the one number |
|:--|:--|:--|
| **H-NEW-74 Cell 6** | **`SURVIVES`** | ε² falls 0.3401 → 0.2864 per word (−15.8 %), and both arms clear its own α = 0.00833 |
| H-NEW-183 | `GENRE-SHARED-BUT-LARGER` | +0.0413 (Ridge) / +0.0735 (RF) above the strongest size baseline |
| H-NEW-233 (RF cell) | `GENRE-SHARED-BUT-LARGER` | +0.0341 above size; but its Ridge cell is beaten by size by −0.0969 |
| H-NEW-233 (Ridge cell) | **`DOES-NOT-SURVIVE`** | one size column beats 29 features by 0.0969 R²; A2 p = 0.0479 |
| H-NEW-192 (RF) | `GENRE-SHARED-BUT-LARGER` | +0.0296 above size — **3 % of variance, not 80 %** |
| H-NEW-192 (Ridge) | `DID-NOT-REPRODUCE` | and no code in this repository produces its published numbers (§6) |
| H-NEW-231 | calibration passed | ρ = −0.9858; the finding's own title was right |

---

## 5. The two results that matter most

### 5.1 The "8 % mushaf–chronology gap" is the above-size residual, and it inverts the reading

H-NEW-192's headline inference is not an R². It is a **difference**:

> **Mushaf is ~8% LESS PREDICTABLE than Nöldeke from the same features.** … The ~20% residual
> … **IS the M1 structural placement signal.**

Published, that gap is 0.836 − 0.759 = **0.077**. Here is the same gap decomposed:

| | mushaf position | Nöldeke rank | difference |
|:--|--:|--:|--:|
| size-only baseline `S3` | **0.8365** | **0.7943** | mushaf **+0.0422** more predictable from size alone |
| full model above size (`ΔR²`, Ridge) | **−0.0339** | **+0.0413** | Nöldeke **+0.0752** |

**The published gap of 0.077 and the above-size residual gap of 0.0752 agree to within
0.002.** The entire "8 % gap" is accounted for by one fact: **Nöldeke rank carries
compositional signal above surah size and mushaf position does not.**

That reverses the inference rather than merely weakening it. The gap was read as *the mushaf
having an extra organizing principle beyond composition*. What it measures is that **the
mushaf ordering is more nearly a pure size ordering than the chronological ordering is** —
which is not a discovery about a hidden principle, it is the ṭiwāl → mathānī → mufaṣṣal
arrangement the tradition has described since before any of this was computed.

**The "~20 % residual IS the M1 structural placement signal" claim is not supported by this
test and is not refuted by it either.** What is shown is that the ~80 % it is a residual
*from* is size, not composition, so the residual is not "what is left after composition."

### 5.2 H-NEW-183's published control priced the wrong baseline

H-NEW-183 reports that its 12-feature model **"nearly doubles R²"** against a *"length-only
baseline [that] achieves R² = 0.446"*.

That baseline is **one column**, `log_length` — read from its own frozen output,
`csv/h-new-183.json → model_B_ridge_length_only.features == ["log_length"]`. Measured on the
frozen matrix: ρ(`log_length`, Nöldeke rank) = **+0.6775**; ρ(`log_length`, whitespace log
word count) = **+0.9995**. **It is the word-count channel — the middle of three — not the
strongest.** The strongest against Nöldeke rank is mean verse length at ρ = +0.9038, and
H-NEW-183 did not use it.

| baseline | columns | R² |
|:--|:--|--:|
| published "length-only" | `log_length` | 0.446 |
| **S1 here** | **mean verse length alone** | **0.8005** |
| **S3 here** | log word count + verse count + mean verse length | **0.7943** |
| full 12-feature model | — | 0.8356 |

**A single column on the correct channel reaches 0.8005 where the published baseline reached
0.446.** The model's honest advantage over size is **+0.0413 R²**, not a doubling.

**This corroborates `UNIT-DRIFT-DEFECT` §5's figure of 0.799** — S1 and S3 bracket it at
0.8005 and 0.7943 — while correcting that section's description of the *channel*: it states
the published baseline used "verse count only (ρ = +0.390)"; the source and the data both say
log word count (ρ = +0.6775). The mechanism the section teaches is unaffected; only the
example's channel label is wrong, and the published control was somewhat better than the
section implies.

**H-NEW-183 remains the healthiest claim of the three predictors**, and its RF cell carries
the largest genuine above-size residual anywhere in this batch at **+0.0735**.

---

## 6. A defect of the record, not of a result: H-NEW-192 is not reproducible

H-NEW-192's frontmatter reads `executed_by: team-lead (inline, autonomous loop)` and its
Files section reads `Script: inline (seed 20260419)`.

1. **No script exists.** A repository-wide search finds two files containing its numbers —
   `scripts/h_new_233_ensemble_predictor.py` and `scripts/h_new_250_equation_fit.py` — and in
   both they appear as **hard-coded literals**: `"h_new_192_baseline_ridge": 0.759`,
   `"h_new_192_baseline_rf": 0.817`. **No code in this repository computes 0.759 or 0.817.**
2. **Its feature set is under-specified.** The finding names **10** of its **15** features;
   two of the ten — `divine_name_density`, `legal_density` — are absent from H-NEW-233's
   `BASE_FEATURES`, while the other eight are present. Neither the finding, nor a journal
   entry, nor any CSV records the remaining five.
3. **Two reconstructions were pre-registered and both miss the Ridge number** by +0.044 and
   +0.045 against a 0.03 tolerance, while both land inside tolerance on RF.

**H-NEW-233's pre-registered PASS condition was scored against these literals.** Its H2 test
is *"RF R² > 0.817"*, and 0.817 is a number no code produces. Worse for that test: a
**15-feature** subset of H-NEW-233's own matrix reaches **0.8485** at the published seed — the
same value to four decimals as its own 29-feature model. **On this evidence H-NEW-233's
fourteen "expansion" features add nothing measurable**, and its headline — *"29-feature
ensemble … +0.032 (beats)"* — is a comparison against an unreproducible baseline.

This is not an accusation that the numbers are wrong. It is the statement that **they cannot
be checked**, and that a claim which cannot be checked should not be carrying two downstream
scripts and the "complete equation" work. **Eleven markdown files in `findings/` assert both
0.759 and 0.817** — excluding this finding and its pre-registration — among them
`cross-finding-020-the-complete-equation.md`,
`cross-finding-021-mushaf-information-theoretic-optimality.md`,
`h-new-250-quantitative-equation-fit.md` and
`h-new-230-mushaf-nöldeke-block-decomposition.md`.

---

## 7. A methodological result: a stratified permutation null is the *weaker* of the two arms here

Worth recording because it cost me the assumption going in, and because it changes how the
next batch should be designed.

**For six of the eight model cells, A2 and A1 disagree, and A1 is right.** C1-RECON-A/Ridge
beats its size-matched null at **p = 0.0020** — the observed 0.8026 exceeds all but one of 500
stratified draws — and is nonetheless **beaten outright by one size column** (0.8378).

The reason is mechanical. **The model contains the nuisance variable as a feature.** A
quintile stratification leaves 23 surahs per bin free to permute, so a model holding
`log_length` and `mean_verse_len` still predicts the permuted target *within* bins using
exactly the channel the stratification was meant to neutralise. The null asks "is this mapping
non-random given coarse size?" — and the answer is yes, because size is in the model.

**The size-only baseline asks the question that matters: do the features add anything over
size?** For the mushaf cells under Ridge the answer is no, by −0.034 and −0.097 R².

The standing rule's own §6 ranks these diagnostics by cost and puts "the size-only baseline"
second. **On this evidence it should be first for any claim whose statistic is a fitted model
containing size as a feature**, and the stratified null should be treated as a supporting arm
rather than the decisive one. A stratified permutation is decisive for a *correlation* — which
is what H-NEW-2770 tested, correctly — and is not decisive for a *regression that contains the
stratifying variable*.

---

## 8. What survives, and at exactly its strength

**H-NEW-74 Cell 6 — the qul-density × Nöldeke-phase effect — SURVIVES.** It is the only
`SURVIVES` in the batch, and it earns it:

- The effect holds **per word**, not only per verse: ε² = 0.2864 against 0.3401, a fall of
  **15.8 %**, far inside the 50 % clause.
- It clears its own published bar **under a mean-verse-length-matched null in both
  normalisations**: p = 0.00710 per verse and p = 0.00440 per word, against α = 0.00833.

**And it must be quoted with its weakening, which is large.** Against the free shuffle the
p-value is **1.0 × 10⁻⁴** (the floor at 10,000 draws); against the size-matched null it is
**7.1 × 10⁻³**. **The matched null costs this effect roughly seventy-fold in p and leaves it
inside its own bar with little room.** The published `p = 1.02 × 10⁻⁷` is an asymptotic χ²
value against a free-shuffle null and is not the strength of this effect once verse length is
held fixed.

The honest headline is therefore not *"the qul-corpus is overwhelmingly a Late-Meccan
phenomenon"* at p = 10⁻⁷, but:

> **Late Meccan surahs say *qul* more often per WORD, not merely per verse, and the phase
> difference survives a null that matches mean verse length — at p = 0.0044 to 0.0071, not
> 10⁻⁷.**

This is the same shape as H-NEW-2770's surviving theonym axes, and it is worth more than what
fell around it: it is a per-verse density claim that turned out **not** to be its denominator,
in a batch where four model cells were.

**H-NEW-183's above-size residual also stands** at +0.0413 (Ridge) and +0.0735 (RF) — small,
real, and correctly labelled `GENRE-SHARED-BUT-LARGER` rather than a survivor, because 95 % of
its published R² is reachable from size columns alone.

---

## 9. Honest limits

1. **Conditioning on size may remove mechanism, not only confound — and for the mushaf this is
   near-certain.** The classical arrangement *is* a length arrangement: sabʿ al-ṭiwāl, then
   mathānī, then mufaṣṣal. A size-matched null on mushaf position therefore removes the
   organizing principle the tradition names. **The correct reading of C1 and C3 is not "the
   mushaf ordering is unstructured" but "these models measure the length arrangement, and
   attribute it to composition."** This was pre-registered as limit §10.1 and it is load-bearing
   for how the verdicts should be read.
2. **LOOCV R² on n = 114 is optimistically biased**, equally in every arm — which is why ΔR²
   is quoted throughout and why no single R² should be read as a generalisation estimate.
3. **C1's verdict rests on a reconstruction.** Both reconstructions are published, they agree
   with each other to 0.0015 (Ridge) and 0.0018 (RF), and neither is H-NEW-192's actual
   matrix, which no longer exists in any form.
4. **Nöldeke chronology is a scholarly reconstruction, not data.** C2 and C4 inherit its
   uncertainty; nothing here tests it.
5. **No genre arm.** Nothing here compares this corpus to any other. `GENRE-SHARED-BUT-LARGER`
   is used in its within-corpus sense only, as stated in §4.
6. **The RF A2 bar is coarse by construction.** At 100 draws the rule requires the observed
   value to exceed the maximum of the null, giving p = 0.0099 exactly whenever it does. Every
   RF cell that beats its null reports that same p; the informative quantity for those cells is
   the margin (observed minus null max), which ranges from +0.0401 (C3/RF: 0.8460 vs 0.8059) to
   +0.0452 (C1-RECON-A/RF).
7. **Five claims is not the inventory.** §11.

---

## 10. Garden of forking paths

- **Everything in §§3–8 was computed after the lock at SHA `6bb7e77a…`.** Known and recorded
  in prereg §9 before the run: the citation ranking, each candidate's correction status, the
  six nuisance-channel correlations, the published headlines, the absence of a script for
  H-NEW-192, and the source-level reading that H-NEW-183's baseline is `log_length`. **The
  prereg predicted the §5.2 result and recorded that it contradicted the repository's own rule
  document, before running it.**
- **The nuisance channel was ranked on measurement, not judgement**, for both orderings.
- **Locked directions D1 and D4 were declared as harness invalidators** — "if D1 or D4 fails,
  every verdict in this batch is void." Both passed (0.8365 ≥ 0.70; ρ = −0.9858).
- **One implementation defect, found by the calibration arm and disclosed because that is what
  the arm is for.** My first KL implementation for C5 summed the divergence **only over token
  types present in each surah**, dropping the smoothed mass on unseen types — where the length
  dependence lives. It returned ρ = +0.0745 and would have read as a harness failure. Corrected
  to sum over the full vocabulary, it returns ρ = −0.9858. **The bug was in my own calibration
  code, not in any tested claim, and no tested value was computed before it was fixed.**
- **Three engineering defects in the permutation harness, none of which touched a value.**
  `multiprocessing` with `fork` deadlocked against sklearn's thread pools; with `spawn` each
  worker re-executed the SHA preamble; and `joblib`'s default `batch_size="auto"` assigned
  every draw to a single worker while the rest idled at 0 % CPU. All three were wall-clock
  faults. **The permutation draw sequence is generated serially before any parallel dispatch,
  so parallelism cannot change a single number**, and the parallel worker is asserted
  bit-identical to the lifted serial routine at startup.
- **Run directories are never deleted.** The three calibration runs are retained beside the
  primary under `runs/h-new-2790-SMOKE/`.

---

## 11. Flagged claims NOT reached — where the next session starts

The batch was five. The screen A ∧ B ∧ ¬C scan over every uncorrected finding in
`findings/` produced a longer list, ordered by computed citation count. **Not reached, in
priority order:**

| claim | cites | statistic | ordering |
|:--|--:|:--|:--|
| **H-NEW-126** — isolate core | 197 | cluster membership of {Q16, 21, 22, 23, 25} across 20 systems | mushaf / cluster systems |
| **H-NEW-88** — letter-set predictor | 167 | per-surah letter-set densities | mushaf |
| **H-NEW-19** — extended classical anchors | 163 | nine density measures | mushaf |
| **H-NEW-136** — muq cardinality Pattern-B | 144 | eight density measures | mushaf |
| **H-NEW-142** — universal hinges | 119 | chronology-reversal magnitude | mushaf × Nöldeke |
| **H-NEW-570** — muqaṭṭaʿāt content cluster | 101 | eight density measures | muq/non-muq |
| **H-NEW-123** — Heaps' law | 90 | β, K per surah | mushaf |
| **H-NEW-49** — surah name class | 87 | six density measures | name class |
| **H-NEW-234** — Q55 unified profile | 65 | nine densities across fifteen orderings | mushaf |
| **H-NEW-2210** — qasam-jawāb inventory | 51 | per-surah oath rates | mushaf |
| **H-NEW-74 Cells 1–5** | 75 | the other five cells of a claim whose Cell 6 survives here | — |

**H-NEW-231 was reached but only as a calibration arm** and is not a tested claim; its own
title already declares length dominant, and this run confirms it at ρ = −0.9858. It should be
cited as **CLEAN** under the rule's §4, which asks that clean cases be named.

I also did not receive the sweep's own FLAGGED inventory before locking, so this worklist is
my own screen applied independently. **Where the two lists differ, the difference itself is
worth an hour**: two independent applications of the same three screens disagreeing would say
the screens are not yet mechanical enough to be a standing rule.

---

## 12. What should change in the project record

Flagged, not applied — a correction to another finding's file is not mine to make.

- **`h-new-192-mushaf-position-decomposition.md` needs a correction notice on two counts**: its
  numbers are not reproducible from the repository (§6), and its "80 % compositional" is
  reached and beaten by one size column (§3). Its `verdict: STRONG PASS` should not stand
  unamended.
- **`h-new-233-ensemble-mushaf-predictor.md`**: its H2 PASS was scored against an
  unreproducible baseline, and a 15-feature subset of its own matrix matches its 29-feature R²
  to four decimals. Its Ridge cell `DOES-NOT-SURVIVE` outright.
- **`h-new-183-chronology-predictor.md`**: the sentence *"The length-only baseline achieves
  R² = 0.446 … nearly doubles R²"* should carry the corrected baseline of **0.8005** and the
  honest advantage of **+0.0413**.
- **`h-new-74-qul-distribution.md`**: Cell 6 **survives**, and should quote **p = 0.0071 under
  a mean-verse-length-matched null** beside its `p = 1.02 × 10⁻⁷`, together with the per-word
  ε² of 0.2864. Its published `H = 35.36` should be labelled tie-uncorrected.
- **`findings/UNIT-DRIFT-DEFECT.md` §5**: the H-NEW-183 example names the wrong channel
  (verse count, ρ = +0.390) for a baseline that is log word count (ρ = +0.6775). **Its 0.799
  figure is confirmed** at 0.7943–0.8005. §6's diagnostic ordering should be amended per §7
  above: for a fitted model containing size as a feature, the size-only baseline is the
  decisive arm and the stratified null is not.
- **`STATE-OF-THE-PROJECT-2026-08-07.md`** should gain rows in §2 for H-NEW-192 and H-NEW-233,
  and H-NEW-74 Cell 6 belongs in §1 as a second surviving density claim beside the theonym
  axes — at p = 0.0071, not 10⁻⁷.

---

## 13. Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2790-flagged-batch.md`
  (SHA-256 `6bb7e77a100810e31743734cd105407d6d21cf6d477dee1a9096c5ebde6014a8`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2790.py` — pre-reg SHA-gated; lifts the
  H-NEW-183 and H-NEW-233 matrices and LOOCV as SHA-verified modules; asserts the parallel
  permutation worker bit-identical to the lifted serial routine
- JSON: `findings/phase-b-hypotheses/csv/h-new-2790.json`
- Runs (immutable, never deleted): `findings/phase-b-hypotheses/runs/h-new-2790/` (primary)
  and `runs/h-new-2790-SMOKE/` (three calibration runs), each with a `manifest.json` recording
  every frozen input SHA in repository-relative form

---

*Run 2026-08-07 by Waiel Al-Shujaa. A rate is a ratio, the divisor is part of the claim — and
when the divisor is a feature of the model, the baseline settles it and the permutation does
not. Bismillāhi al-Raḥmāni al-Raḥīm.*
