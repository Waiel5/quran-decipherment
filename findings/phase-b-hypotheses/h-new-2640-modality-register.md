---
id: H-NEW-2640
title: Modality and register — does the mood system separate deontic command from epistemic certainty? (NULL on all four registered inferences)
date: 2026-08-07
author: Waiel Al-Shujaa
phase: B
status: NULL — 4/4 registered inferences fail; two also show reversed direction
verdict: NULL. Modality, measured as an unweighted per-surah marker density, does not separate the three registers, and adds nothing to the cross-finding-028 vector. Legal-Medinan separability does NOT rise above 8/20 — it falls.
prereg: prereg-h-new-2640-modality-register.md
prereg_sha256: 0b300fdb19c351b1692dc06b7163480bdbed642702c02dbf1bf7e9272065de89
run: runs/h-new-2640/20260807T010101Z/
posthoc_runs: [runs/h-new-2640/20260807T010345Z-posthoc/, runs/h-new-2640/20260807T010530Z-posthoc/, runs/h-new-2640/20260807T010706Z-posthoc/]
incidental_reruns: [runs/h-new-2640/20260807T010345Z/, runs/h-new-2640/20260807T010529Z/, runs/h-new-2640/20260807T010705Z/]
determinism: result.json byte-identical (sha256 1c13fe9a…) across all four primary executions
seed: 20260509
seed_replication: 20260519
family: MODALITY-2026-08-07-A
parents: [H-NEW-2500, H-NEW-2530, cross-finding-028-formal]
---

# H-NEW-2640 — The ṭalab/khabar division, measured and not found

**Verdict: NULL.** All four pre-registered inferences fail at α_bon = 0.0125. Two of the
four also show a **reversed** direction — the modality features make the
cross-finding-028 classifier *worse*, and the un-split raw jussive separates registers
*better* than the carefully split deontic index. Pre-reg SHA-256
`0b300fdb…5de89`, runtime-verified; four frozen inputs SHA-verified; seed 20260509,
replication 20260519, 10,000 permutations, two nulls, three rules-tuples.

**cross-finding-028-formal does not gain a fifth column.** It still has no mood feature,
and on this evidence it should not have one.

---

## 1. The registered result

| | inference | statistic | locked direction | observed | perm-p (Null A) | verdict |
|:--|:--|:--|:--|--:|--:|:--|
| **I1** | deontic × register | ANOVA F of D_resid | argmax = `legal_medinan` | F = **0.027**, argmax `narrative` | **0.9787** | **NULL** |
| **I2** | epistemic × register | ANOVA F of E_resid | argmax = `eschatological_mufassal` | F = **0.074**, argmax `narrative` | **0.9310** | **NULL** |
| **I3** | orthogonality | Δ = LOO₈ − LOO₆ | Δ ≥ 0 | **Δ = −0.0879** | **0.9622** | **NULL, direction reversed** |
| **I4** | confound demo | Δ_F = F(D) − F(rawJUS) | Δ_F > 0 | **Δ_F = −0.4334** | **0.6816** | **NULL, direction reversed** |

Held under **every** robustness lens: Null B (label shuffle stratified within surah-length
tertiles) gives 0.9510 / 0.8951 / 0.9622 / 0.7290; the seed-20260519 replication gives
0.9782 / 0.9357 / 0.9588 / 0.6715; rules-tuples T2 and T3 fail identically. Nothing
rescues it.

**On the two "reversed" labels — an honest correction to my own gate design.**
Pre-registration §9 lists two failure modes (p ≥ α; direction reversed) and **gives no
precedence rule when both occur**, so the script labels every non-pass with a wrong
direction as `REVERSED-PRECOMMIT-VIOLATION`. That over-labels I1 and I2. With F = 0.027
and F = 0.074 there is no effect to reverse; the argmax of a null effect is arbitrary.
**The correct reading of I1 and I2 is NULL, not reversal.** I3 and I4 *are* genuine
directional reversals — Δ and Δ_F both came out negative against a locked positive — but
at p = 0.96 and p = 0.68 the reversals are themselves inside the null band. So: four
NULLs, two of which point the wrong way without significance. The gate flaw is mine and
is recorded here rather than quietly rewritten.

---

## 2. The deliverable asked for: the classifier delta

**Legal-Medinan separability does not rise above 8/20. Overall accuracy falls.**

| vector | LOO accuracy | narrative | **legal** | eschatological |
|:--|--:|--:|--:|--:|
| H-NEW-2530 six features (published baseline) | **0.76923** | 25/31 | **8/20** | 37/40 |
| + D_resid, E_resid (**registered**) | **0.68132** | 25/31 | **8/20** | 29/40 |
| + raw D, raw E (*post-hoc, §5*) | 0.70330 | 25/31 | *10/20* | 30/40 |

The registered eight-feature vector leaves the legal row **untouched at 8/20** and destroys
eight of the eschatological classifier's 37 correct calls (37 → 29), ten of which now
misclassify as legal. Modality does not sharpen the legal↔eschatological soft boundary
that cross-finding-028-formal flagged as its open follow-up; it blurs it further.

The six-feature baseline was reproduced **exactly** — accuracy 0.76923 and the published
confusion matrix cell-for-cell — before anything was added (MW-6.2).

---

## 3. Per-register densities, before and after the jussive split and the length control

Deliverable table. `D` = deontic index, `E` = epistemic, `J` = **raw** `MOOD:JUS` (the
naive instrument), `N_lam` = the *lam*-negation confound, `C_cond` = conditional jussive.

**Raw, per 1,000 word-tokens (unweighted mean of per-surah densities):**

| index | narrative | legal_medinan | eschatological | argmax |
|:--|--:|--:|--:|:--|
| **D** deontic | 25.09 | **33.24** | 27.69 | legal ✓ *matches lock* |
| **E** epistemic | 56.05 | 34.76 | **58.15** | eschat ✓ *matches lock* |
| J raw `MOOD:JUS` | 17.57 | **27.29** | 17.60 | legal |
| N_lam | 4.23 | 5.53 | **12.73** | eschat |
| C_cond | 6.79 | **12.02** | 0.21 | legal |

**After OLS residualisation on [log n_verses, mean words/verse] — the primary variable:**

| index | narrative | legal_medinan | eschatological | argmax | F |
|:--|--:|--:|--:|:--|--:|
| **D** deontic | **0.654** | 0.510 | −0.762 | narrative ✗ | 0.027 |
| **E** epistemic | **2.476** | −1.517 | −1.160 | narrative ✗ | 0.074 |
| J raw `MOOD:JUS` | 2.393 | **2.610** | −3.160 | legal | 0.461 |
| N_lam | −0.647 | −0.524 | **0.764** | eschat | — |
| C_cond | 2.525 | **2.694** | −3.304 | legal | — |

**The raw contrast has exactly the predicted sign for both indices, and it does not
survive.** That is the whole finding in two rows.

---

## 4. The confound — real, but not for the reason anyone expected

The brief for this test warned that `MOOD:JUS` is dominated by *lam* + past-negation and
that testing it raw would "measure negation, not modality." The split was mandatory and
it was done. The corpus-wide result:

| jussive class | n | % | modal content |
|:--|--:|--:|:--|
| `N_lam` (*lam* / *lammā* negation) | 351 | 24.8% | none |
| `D_pro_la` (prohibitive *lā tafʿal*) | 330 | 23.3% | **deontic** |
| `C_cond` + `C_cond_rel` + `C_apodosis` + `C_jawab_talab` | 521 | 36.7% | conditional syntax |
| `X_neg_la` (ambiguous *lā*) | 110 | 7.8% | disputed (tuple T2) |
| `D_lam_amr` (lām al-amr) | 78 | 5.5% | **deontic** |
| `R_other` | 28 | 2.0% | unresolved |
| **total** | **1,418** | | |

**Only 408 of 1,418 jussives (28.8%) are deontic.** The warning was right about the
magnitude. But the *mechanism* is not what was predicted, and the measurement says so:

- ***lam*-negation is register-flat.** Pooled rates 4.38 / 4.90 / 5.99 per 1,000 tokens,
  spread 1.61, descriptive p = **0.251**. It has no register structure at all. It
  **dilutes** the raw jussive signal; it does not distort it.
- **The conditional jussive is the strongest register signal in the entire mood system.**
  Pooled 4.35 / **11.04** / 1.69, spread 9.35, descriptive p = **0.00070** — a larger,
  cleaner effect than the deontic index itself.

So a raw-`MOOD:JUS` test would not have been "measuring negation." It would have been
measuring **conditional syntax**, which is H-NEW-2630's registered territory and
H-NEW-2250's before that — and it would have reported a borrowed result as a modality
finding. The split was necessary. It was necessary for a different reason than stated,
and stripping the conditionals out is precisely what left nothing behind.

This is also why I4 reversed: F(rawJUS) = 0.461 vs F(D) = 0.027. The naive instrument
out-separates the careful one **17-fold**, because the naive instrument is carrying
someone else's signal.

---

## 5. Post-hoc diagnostics — NOT pre-registered, MW-7-capped at single-test α = 0.05

These carry **no** confirmatory standing and **no** Bonferroni protection. They were
written to be reported whatever they returned, and they are reported in full. They exist
to answer one fair objection: *is the null an artefact of the residualisation?*

**P2 — No.** The two length covariates absorb only **R² = 0.036** of D's variance and
**0.061** of E's. The residualisation is not eating the effect. *(This overturned my own
first reading of the result, which had blamed the length control.)*

**P1 — No.** Feeding the classifier the **raw** indices also hurts it: Δ = −0.066 (vs
−0.088 residualised). Raw E alone Δ = −0.044; raw D alone Δ = −0.066. **No variant of
this feature pair improves the classifier.** Legal recall does reach 10/20 with raw D+E,
purchased by losing ten eschatological calls.

**P5/P3 — The instrument is the binding constraint.** 20 of 91 surahs have fewer than 50
word-tokens; the range is 10 to 6,116. The registered statistic is an **unweighted mean of
per-surah densities**, so Q 108 al-Kawthar — two imperatives in ten words, density 200 per
1,000 — counts as heavily as al-Baqara. The top of the deontic ranking is almost entirely
this artefact (Q 108, 110, 96, 93, 94, 112, 106, 114), and Q 81/82/85/90 sit at exactly
0.00. Within-register variance swamps between-register variance, which is why F ≈ 0.03.

**P4 — And here is what that cost.** Pooling over tokens instead of averaging over surahs:

| index | narrative | legal_medinan | eschatological | argmax | vs lock | spread | desc. p |
|:--|--:|--:|--:|:--|:--|--:|--:|
| **D** deontic | 28.53 | **34.16** | 24.13 | legal | ✓ **matches** | 10.03 | **0.0077** |
| **E** epistemic | **56.01** | 35.10 | 45.34 | narrative | ✗ **fails** | 20.91 | 0.0104 |
| J raw `MOOD:JUS` | 14.92 | **25.45** | 12.76 | legal | — | 12.69 | 0.0021 |
| N_lam | 4.38 | 4.90 | **5.99** | eschat | — | 1.61 | 0.2509 |
| C_cond | 4.35 | **11.04** | 1.69 | legal | — | 9.35 | 0.0007 |

**Read this carefully, because it is the most consequential thing in the file.**

- The **deontic** half of the hypothesis survives a pooled estimator with the locked
  direction intact and a descriptive p of 0.0077. **I cannot claim it.** The registered
  statistic was the surah-mean ANOVA and it returned p = 0.979. Under MW-7 a post-hoc
  estimator swap carries a single-test ceiling and no confirmatory standing. What this
  licenses is a **new pre-registration**, not a rescued verdict. Anything else would be
  choosing the estimator after seeing the answer.
- The **epistemic** half fails on **direction** under *both* estimators. Narrative, not
  eschatological, is the most emphatically-marked register — pooled 56.01 vs 45.34. That
  is a real negative result about the hypothesis, not about the instrument, and it is not
  repairable by re-estimating. *qad*, the oath-lām, the nūn al-tawkīd and *inna* cluster
  in **narrative**, where they mark reported speech and the affirmations inside it, rather
  than in eschatological warning where the ṭalab/khabar reading predicted them.

---

## 6. What this does to the classical claim

The ṭalab/khabar division is real morphology and nobody is disputing it. What was tested
is a **distributional** corollary the tradition never asserted: that the two halves sort
by register. On the registered instrument they do not. On a pooled instrument, half of it
might — the command half — and the certainty half points the wrong way.

The tradition is not damaged by this. al-Suyūṭī's claim is about what a verse *contains*,
not about how markers distribute across genres. The distributional reading was mine, it
was falsifiable, and it failed.

**Classical citations — verified by opening the files.**

- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, Eng. trans. A. J. W. Mol**,
  `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`:
  - **p. 127** (on Q 2:124): the verse "combines **the message and the requisition**, the
    affirmation and the negation, the emphasis and the omission, good news and a warning,
    and the promise and the threat." *Message* = khabar, *requisition* = ṭalab —
    al-Suyūṭī's own preferred analysis, and the exact division operationalized here.
  - **p. 249** (on Q 7:31, and on Q 28:7 citing Ibn al-ʿArabī): a verse "contains two each
    of **the imperative, the prohibitive, the communicative, and the annunciative forms**."
    The amr / nahy / khabar four-way, mapping onto D (imperative + prohibitive) and
    E (communicative + annunciative).

**Anchors NOT used, and why.**

- **al-Sakkākī, *Miftāḥ al-ʿulūm*** — named in `KNOWLEDGE-GRAPH.md` line 137 as the anchor
  for this division. **The text is not in the repository.** No passage is cited from it.
- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*** — the PDF *is* on disk at
  `data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf`, and it is
  **unreadable by machine**: 29.5 MB, 1,568 pages, Producer *"Adobe Acrobat 7.05 Image
  Conversion Plug-in"*, no text layer. `pdftotext -layout` returns 1,568 page breaks and
  **zero characters**. **No passage is cited from it.** *Standing data gap: the project's
  single most-cited classical source for ʿulūm al-Qurʾān is, on disk, an image stack. An
  OCR pass or an OpenITI Burhān would unlock a source that several findings currently
  reference through al-Suyūṭī rather than directly.*

---

## 7. Two corrections to the QAC feature strings as documented

Both were caught by re-verifying every count before locking the pre-registration, as
instructed. **The totals in `HANDOFF/FRONTIER-MAP-2026-08-07.md` are correct; the feature
strings naming them do not exist**, and a future run that trusted the label would match
nothing.

| as documented | reality in QAC v0.4 |
|:--|:--|
| `POS:EMPH` 1,244 | **There is no `POS:EMPH` tag.** EMPH is a *clitic* tag: prefix `l:EMPH+` = **1,001** (lām al-tawkīd) + suffix `+n:EMPH` = **243** (nūn al-tawkīd) = 1,244. |
| `POS:FUT` 161 | `POS:FUT` alone = **42** (all `LEM:sawof`). The other **119** are the prefix atom `sa+`. 42 + 119 = 161. |

Verified unchanged: `MOOD:JUS` 1,418 · `MOOD:SUBJ` 1,330 · `POS:CERT` 414 · `POS:PRO` 332.

**And the standing rule, demonstrated on the annotation file itself:**

| test | result |
|:--|--:|
| `'POS:PRO' in FEATURES` (substring) | **3,633** |
| `'POS:PRO' in FEATURES.split('\|')` (atom) | **332** |

**10.9× inflation**, because `POS:PRON` — pronoun — contains `POS:PRO` as a prefix. The
project's rule that substring counting on Arabic particles lies applies to the *feature
strings* as much as to the Arabic. This test is asserted at runtime (MW-6.6) and aborts on
mismatch.

---

## 8. Honest limits

1. **The estimator was the wrong choice, and I locked it.** An unweighted mean of
   per-surah densities over surahs spanning 10 to 6,116 tokens is a low-power instrument
   for sparse markers. §5/P4 shows a pooled estimator would have behaved very differently
   on the deontic half. That was a pre-registration error of *instrument design*, not of
   discipline — the pre-registration is what makes it visible instead of invisible.
   **It does not license retro-fitting the verdict.**
2. **Over-control was my first hypothesis and it was wrong.** I initially read the null as
   the length residualisation eating a real effect. P2 (R² = 0.036 / 0.061) refutes that.
   Recorded because the wrong diagnosis was reached first.
3. **Marking ≠ speech-act.** The indices count morphological exponents. A command issued
   as *kutiba ʿalaykum* (a khabar-form legal formula) or as a rhetorical question is
   invisible to D; certainty asserted with no particle is invisible to E. F-15 on the
   frontier map targets exactly the legal-formula frames this misses.
4. **Double-counting inside E.** *la-qad* carries both `l:EMPH+` and `POS:CERT` and counts
   twice. Marker-token count, not clause count. Disclosed, not corrected.
5. **The genre proxy is H-NEW-2500's coarse surah-scale surrogate** — inherited, and Q 2 is
   both legislative and narrative. A pericope-scale re-test is cross-finding-025's standing
   prescription and is not run here.
6. **QAC-annotation-limited**, and QAC's PRO/NEG split of prohibitive *lā* is inconsistent
   (Q 2:102:34 `laA takofuro` is tagged `POS:NEG` though plainly prohibitive). That is why
   tuple T2 exists; T2 changes nothing (F_D 0.027 → 0.027).
7. **Quran-internal.** No matched Classical-Arabic control corpus. Any register effect
   found here could be a property of Classical Arabic generally.
8. **The governor rule is mine.** The §3.2 backward-scan is a hand-built heuristic, not a
   parse. It was fixed on corpus-wide totals before any register split and is asserted
   cell-for-cell at runtime, but 28 jussives remain `R_other` and the `C_apodosis` /
   `C_jawab_talab` distinction is the weakest part of it.

---

## 9. Provenance

- Pre-registration written and SHA-256'd **before any register-split computation**. Only
  corpus-wide marginals and the governor-rule calibration were computed beforehand, and
  those are written into the pre-registration itself as locked instrument values (§3.3).
- Primary run: `runs/h-new-2640/20260807T010101Z/`.
- **Seven run directories exist and all seven are retained.** The count needs explaining,
  and the explanation is a mistake of mine worth recording:
  - 1 primary — `20260807T010101Z`.
  - 3 post-hoc — `20260807T010345Z-posthoc` (P1–P3), `20260807T010530Z-posthoc`
    (adds P4/P5), `20260807T010706Z-posthoc` (adds the conditional-jussive pooled rate).
    Each superseded the last.
  - 3 **incidental** — `20260807T010345Z`, `20260807T010529Z`, `20260807T010705Z`. The
    post-hoc script re-uses the primary script by importing it, precisely so that every
    SHA is re-verified and every index rebuilt from the frozen inputs rather than
    re-implemented. I did not anticipate that importing it would also trigger its
    run-directory write. Each post-hoc invocation therefore emitted a spare primary run.
  - **Nothing was deleted.** Pre-registration §8 has no exception for spare, superseded or
    uncommitted directories, and the standing correction at
    `h-new-2540-form-v-valency.md` §8.1 exists because that exact judgment call was made
    wrongly before. Seven cluttered directories are the intended cost of the rule.
- **Determinism, obtained free from the accident.** The four primary executions ran at
  four different times from four different invocation paths, and their `result.json` files
  are **byte-identical**, SHA-256 `1c13fe9a09f0ab95db5d1bd7a693ed4c343e9748873b315aab12f5d0380e1514`.
  Manifests differ only in `utc` and the script hash. Anyone with the four hashed inputs
  regenerates these numbers exactly.
- Frozen inputs SHA-256-verified at runtime: QAC v0.4 `a1d12923…`, `h-new-2530.json`
  `5ca17050…`, `h-new-2500.json` `a63aef25…`, `quran-no-tashkeel.json` `253f72f3…`.
- MW-6 fail-fast controls, all asserted at runtime: register marginals 31/20/40/23
  reproduced from the pointer H-NEW-2530 itself records; the six-feature LOO reproduced at
  0.76923 with the published confusion matrix cell-for-cell; twelve marker totals; the
  nine-way jussive split summing to 1,418; corpus geometry 77,429 tokens / 6,236 verses /
  114 surahs; the substring-vs-atom exhibit. The optimised LOO used in the permutation
  loops is gated against the exact H-NEW-2530 implementation on the observed data and
  refuses to run if they disagree.
- **Not committed to git.** Ledger and cross-finding updates are deliberately left
  undone — seven other tests are running against the same shared files in this wave, and
  an uncommitted edit to `MASTER-FINDINGS-LEDGER.md` or
  `cross-finding-028-formal-…md` would collide. Handoff item, below.

## 10. Handoff

1. **cross-finding-028-formal gains nothing.** Its open follow-up #2 — "resolve the
   legal↔eschatological blur with a legal-specific feature" — is **not** solved by
   modality. Modality makes the blur worse. F-15 (legal-formula frames drawn from
   al-Qurṭubī's *aḥkām* headings) remains the live candidate.
2. **A new pre-registration is warranted for the deontic half alone**, with a **pooled
   token-weighted rate** as the registered statistic and a stated minimum surah size. It
   must be locked *before* looking, and it must cite §5/P4 of this file as the post-hoc
   origin of the estimator choice so the provenance of the idea is on the record.
3. **The epistemic half should not be re-run.** It fails on direction under both
   estimators. Narrative is the emphatic register.
4. **H-NEW-2630 (conditionals) should know** that the conditional jussive is a pooled
   register separator at descriptive p = 0.0007 (legal 11.04 vs eschatological 1.69 per
   1,000 tokens) — measured here only to be excluded, and offered as a covariate.
5. **Data gap:** al-Zarkashī's *al-Burhān* is an image-only scan. OCR or OpenITI
   acquisition would unlock the project's most-cited ʿulūm al-Qurʾān source.

---

*H-NEW-2640 — NULL, 2026-08-07, Waiel Al-Shujaa. The prediction was locked, the direction
was locked, and the corpus declined. The instrument error is recorded because the
pre-registration is what made it visible. Bismillāhi al-Raḥmāni al-Raḥīm.*
