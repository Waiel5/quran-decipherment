---
id: H-NEW-2920
title: "The hand-built-proxy census — 25 hand-assigned quantities in this repository, and three of them measured against computed alternatives"
phase: B
status: COMPLETE — census descriptive and not pre-registered; the three tests pre-registered, locked, run, verdicts diffed against the prereg's §6
date: 2026-08-08
author: Waiel Al-Shujaa
prereg: findings/phase-b-hypotheses/prereg-h-new-2920-proxy-validation.md
prereg_sha256: adb194fb759d72f88ffb4600448c84b4faa14bf9236b34e9d5dbea534b4e4cdb
run: runs/h-new-2920/20260807T225701Z
run_posthoc: runs/h-new-2920/20260807T225823Z-posthoc
run_aborted: runs/h-new-2920/20260807T225604Z
script: findings/phase-b-hypotheses/scripts/h-new-2920.py
script_posthoc: findings/phase-b-hypotheses/scripts/h-new-2920-posthoc.py
seed: 20260808
seed_replication: 20260818
rule_document: findings/PROXY-CLAIMS.md
calibration_parent: H-NEW-860.1
verdict: "T1 H-NEW-150's liturgical score PARTIAL (ρ_op = +0.43 to +0.50; its headline does not survive substitution, ρ = −0.056 to +0.027); T2 the Nöldeke rank PARTIAL (ρ = +0.7714 between raters, 14/15 signs agree, but every axis shrinks and 2 of 11 stop surviving); T3 Q036-F-01's reconstructed rubric NOISE (ρ = −0.040 against the formal count; and it does not reproduce the rubric it names as its source, ρ = +0.5571 with 30 of 38 values different)"
---

# H-NEW-2920 — the hand-built-proxy census

## 0. The answer, in one place

H-NEW-860.1 established that one hand-built proxy in this repository carried no
discriminative information: a 0–10 fadāʾil rubric correlated with the formal count at
**ρ = +0.055** over the range where it operated. The obvious next question is whether that is
one bad rubric or a class of defect. **This finding answers it: it is a class, and the class
is not uniform.**

1. **25 hand-assigned quantities are catalogued** (§2), ranked by consequence and each cited to
   `file:line`. Fourteen feed a published correlation, a standing law, or a locked test family.
   Eleven are descriptive. One is a boundary case — a composite whose *weights* rather than
   whose values are hand-chosen, and it is the most-cited quantity in the repository.
2. **Three were measured against computed alternatives, and they came back differently.**
   None reproduced the 860 rubric's total failure, and none was clean.

| test | proxy | agreement with the computed alternative | class |
|:--|:--|--:|:--|
| **T1** | H-NEW-150's hand-coded liturgical-prominence score | **ρ_op = +0.4319** (naming) to **+0.5030** (union) | **PARTIAL** |
| **T2** | the Nöldeke chronology rank | **ρ = +0.7714** against the Egyptian standard | **PARTIAL** |
| **T3** | `Q036_F_01`'s reconstructed 860 rubric | **ρ = −0.0396** against the formal count | **NOISE** |

3. **The two PARTIALs fail in opposite ways, and the difference is the most useful thing here.**
   H-NEW-150's score **ranks** the surahs it selected respectably and **selects** them badly:
   45 surahs with non-zero formal reception carry a score of 0, including **Q 4 al-Nisāʾ, the
   corpus's second-most-cited surah**, and the 27 it did score capture only **54.1 %** of all
   naming links. The Nöldeke rank is the mirror: it agrees with a second rater on **direction**
   (14 of 15 axis signs) and disagrees on **magnitude** everywhere, shrinking every coefficient
   in H-NEW-125's map. Its ρ = +0.7714 **independently reproduces H-NEW-212's published +0.771**
   from a separately built harness.
4. **The 860 rubric and the 150 score fail in mirror-image ways, and that is why one number
   cannot summarise a proxy.** The 860 rubric was respectable full-corpus (+0.374) and useless
   in-range (+0.055) — it could tell presence from absence and could not rank. The 150 score is
   the exact opposite: **+0.4319 in-range and +0.0663 full-corpus.** It can rank and cannot
   select. **Reporting only one of the two coefficients would have called each proxy sound.**
5. **Neither host headline survives substitution.** H-NEW-150's ρ = +0.3121 (p_perm = 0.0002)
   becomes **−0.0556** with the formal naming count, **+0.0217** with quotation, **+0.0265**
   with the union — all null under 10,000-draw permutation at both seeds. H-NEW-125's
   Bonferroni-surviving set falls from 11 axes to **9** under the alternative rater.
6. **And one published NULL reverses, which was not what this test was looking for.**
   H-NEW-150's SECONDARY FAIL — *"the more important finding"*, a residual ρ = 0.0859 read as a
   length confound — is a **residualisation artefact**. The score has 87 tied zeros; OLS
   residualisation against log length replaces that single tied rank with **66 distinct values
   ordered at ρ = +1.0000 with log verses**. A rank-based partial correlation, which cannot
   manufacture order among ties, returns **+0.3174 (p = 0.0006)** — essentially the raw value.
   **The length confound H-NEW-150 diagnosed does not exist** (ρ = −0.138 for the score and
   +0.016 for degree against log verses). Its correlation is real and is a property of the hand
   score, not of ḥadīth reception.

---

## 1. Scope, and what a census by detection cue can and cannot find

The sweep covers `findings/`, `surahs/` and `scripts/` — 2,335 markdown files and 809 Python
files — by the cue vocabulary in §4 of this document and in `findings/PROXY-CLAIMS.md` §3.

**It finds quantities that declare themselves hand-assigned.** A hand-assignment never
described as one is invisible to it, and this must be said rather than implied, because
`findings/UNIT-DRIFT-DEFECT.md` §8's lesson is precisely that two applications of a screen can
agree perfectly while both are blind to a class the screen never asks about. **The honest claim
is that these 25 exist, not that no others do.**

The census is **descriptive and deliberately not pre-registered** (prereg §preamble). Only the
three tests in §3 are locked.

---

## 2. The census, ranked by consequence

Ranked on the counting rule of `UNIT-DRIFT-DEFECT.md` §6.2 — distinct `.md` files under
`findings/` + `surahs/` referencing the host claim, excluding `/runs/`, `/scripts/`, any
`prereg` filename, the claim's own file and its own sub-finding family.

### 2.1 Tier 1 — feeds a published correlation, a standing law, or a locked test family

| # | proxy | file:line | what it stands in for | computable from data on disk? | citing files |
|--:|:--|:--|:--|:--|--:|
| **1** | **0–10 fadāʾil "rough rubric"**, 36 surahs | `h-new-860-hadith-architectural-alignment.md:64, 74, 80` | corpus-wide ḥadīth attention per surah | **YES — and DONE.** 50,884 records; **ρ = +0.055** (H-NEW-860.1 §5) | **61** |
| **2** | **Nöldeke chronology rank** | `data/revelation-order.csv` col `noldeke_order`; consumed at `scripts/h_new_125_chronology_content.py:512` | order of revelation | **PARTIAL — TESTED HERE (T2).** No ground truth exists; a second rater's ordering sits in the same file | 20 (H-NEW-125) |
| **3** | **liturgical-prominence score**, 0–17 hand-coded | `h-new-150-liturgical-hub-prereg.md:60-71`; limits at `h-new-150-liturgical-hub.md:188-195` | classical liturgical prominence per surah | **YES — TESTED HERE (T1)** | 7 |
| **4** | **three semantic root sets** — `LEGAL_ROOTS` (5 roots), `ESCHAT_ROOTS` (4), `BOOK_ROOTS` (4) | `scripts/h_new_125_chronology_content.py:286, 299, 317` | legal / eschatological / book-reference content density — **3 of H-NEW-125's 11 surviving axes** | **PARTIAL.** No gold-standard semantics on disk; `data/morphology/root-cooccurrence-graph.json` permits a seed-expansion sensitivity test. **NOT REACHED** | 20 |
| **5** | **hand-picked classical divine-name pairs** | `h-new-170-99name-network-prereg.md:21`; result at `h-new-170-99name-network.md:95` | the classical pairing tradition | **YES — AND ALREADY DONE.** H-NEW-170 ran the exhaustive 99-name network and reports *"not only hand-picked pairs, and the classical pairs are NOT doing"* the work. **A validated proxy, and the project did it correctly** | 21 (H-NEW-140) |
| **6** | **oath-opener list**, hand-coded from tafsīr | `h-new-154-q50-composite-prereg.md:125` | Qurʾānic oath openings | **YES — AND ALREADY DONE.** `h-new-85-oath-openers-prereg.md:192` states the parent *"used a hand-built rule; this re-runs it from the QAC morphology"*; `h-new-2210-qasam-jawab-inventory.md:24` is *"a morphology-grounded GENERATOR (not a curated list)"*. **NOT REACHED — the agreement figure is still uncomputed** | 2 / 10 / 19 |
| **7** | **`Q036_F_01` reconstructed 860 rubric**, 20 surahs | `surahs/Q036-yasin/scripts/Q036_F_01_recitation_frequency_weighted_centrality.py:59-99` | H-NEW-860's rubric — **a proxy of a proxy** | **YES — TESTED HERE (T3)** | 5 |
| **8** | **hand-coded classical-cross-reference flag** (axis 8 of a 10-axis composite) | `ism-azam-composite-test.md:65`, sensitivity at `:228` | tafsīr-canon attention per verse | **YES.** Five tafsīr corpora on disk — al-Ṭabarsī, al-Suyūṭī *Durr*, al-Zamakhsharī, plus `suyuti-itqan.openiti.raw.txt` (`ABSENCE-CLAIMS.md` §6 FALSE #5). **NOT REACHED** | 4 |
| **9** | **Rule-F surface-form allow-lists**, assembled by substring | `h-new-2020-word-balance-scan.md:174`; `prereg-h-new-2020-word-balance-scan.md:269` | morphological form classes | **YES — QAC morphology.** NOT REACHED | 2 |
| **10** | **20-class hand-coded opening taxonomy** (Axis C) | `h-new-1390-opening-linked-content-divergent.md:164` — *"alternative taxonomies could change the C_strict count by ±5 pairs"* | opening subclass | PARTIAL. NOT REACHED | 1 |
| **11** | **the governor rule** — a backward-scan heuristic | `h-new-2640-modality-register.md:291` — *"The governor rule is mine … a hand-built heuristic"* | syntactic governor of a modal | **PARTIAL.** A treebank exists for this corpus (none matched). NOT REACHED | 1 |
| **12** | **manually curated liturgically-significant 4-grams** | `h-new-50-bismillah-114-prereg.md:68` | liturgically significant phrases | **YES.** NOT REACHED | 3 |
| **13** | **five hand-picked balance axes** | `h-new-2550-muqattaat-phonetic-optimizer.md:230` — *"holds on five hand-picked axes"* | phonetic genus balance | **PARTIALLY DONE** — the finding itself enumerates all 40,116,600 subsets on the primary axis | 2 |
| **14** | **hand-coded thematic similarity matrix** | `surahs/Q002-al-baqara/Q002-F-04-ring-structure.md:71` — *"Hand-coded thematic similarity matrix (not lexical)"* | thematic similarity between verse pairs | PARTIAL. NOT REACHED | — |

### 2.2 Tier 2 — descriptive, catalogue, or illustrative

No published correlation or standing law rests on these. They are listed because a descriptive
proxy becomes load-bearing the moment a later finding cites it as a fact.

| proxy | file:line | computable? | citing files |
|:--|:--|:--|--:|
| 32 supplementary similes added from "the standard rhetorical catalog" | `parables-catalog.md:34` | YES — a `ka-` + vehicle generator over QAC | 10 |
| hell-name occurrences classified by discourse type | `paradise-hell-names.md:259` — *"I classified each hell-name occurrence"* | PARTIAL | 8 |
| all 114 surahs classified by theme "via Sahih semantic probes" | `intra-quranic-cross-references.md:53` | PARTIAL | 8 |
| ring-centre semantic categorisation | `ring-center-semantics.md:603` — *"The categorisation in §2 is mine, done by eye"* | PARTIAL | 8 |
| semantic plausibility of word-pairs "judged by author eyeballing" | `word-pair-symmetry.md:446` | NO — superseded by the generator in H-NEW-2010 | 8 |
| hand-picked jinās showcases | `jinas-wordplay.md:1148` — *"Hand-picked … for maximum semantic-play yield"* | YES — the detection passes are generators | 14 |
| "Author's curated list" of numerical coincidences | `numerical-coincidences.md:2147` | **DONE** — H-NEW-2660's exhaustive generator scanned 124,148 candidates | 10 |
| hand-curated *raḥma* surface-form list | `rahma-114-baseline-rigor.md:440` | YES — QAC | 6 |
| convergence table "hand-curated by reading every finding file end-to-end" | `convergence-analysis.md:14` | PARTIAL | 7 |
| root-graph communities "named by inspection of their top-degree members" | `graph-theory-roots.md:206` | PARTIAL — the communities themselves are computed; only the labels are hand-made | 2 |
| `formulaic_presence` target-phrase set | `derived-equations.md:154` (declares itself *"Not hand-curated by verse, only by phrase"*) | YES | 1 |

### 2.3 The boundary case, and it is the largest quantity in the repository

**UAS — H-NEW-840, 366 external citing files.** It is **not** hand-assigned per surah: it is an
equal-weight sum of three z-scores and every value is computed. What is hand-assigned is the
**choice of the three components and the equal weighting**, and it carries a size loading of
**ρ = +0.608** with log surah word count (H-NEW-860.1 §7.1) that no ratio-screen catches,
because UAS divides by nothing.

It already carries `status: SYNTHESIS` and three correction notices. H-NEW-860.1 §7.4 proposed
**Screen A′** for exactly this shape — *is either variable a composite, index, or hand score
whose construction loads on unit size?* — and this census is the second independent arrival at
the same conclusion. **It belongs in the census as a boundary case and it is not counted among
the 25 hand-assigned quantities**, because calling a computed composite "hand-built" would
inflate the count and blur the defect.

---

## 3. The three tests

Locked in `prereg-h-new-2920-proxy-validation.md`, SHA-256
`adb194fb759d72f88ffb4600448c84b4faa14bf9236b34e9d5dbea534b4e4cdb`, verified by the runner at
startup. Classification rule, verbatim from prereg §6:

```
NOISE               <- |rho_op| < 0.20  AND  the headline fails to reproduce
CARRIES INFORMATION <- rho_op >= 0.60   AND  the headline reproduces, same sign,
                       still significant at the host's own bar
PARTIAL             <- anything else that is measurable
NOT-YET-TESTABLE    <- no formal alternative computable from data on disk
```

`ρ_op` is the agreement over the **proxy's own operating range** — the units it actually
scored — because H-NEW-860.1 §5 showed the full-corpus figure is inflated by the
presence-versus-absence split. Both are reported for every arm.

### 3.0 Does the instrument work?

Before any coefficient, the naming matcher was rebuilt from scratch in this runner and scored
against H-NEW-860.1's published output.

| check | result |
|:--|:--|
| records scanned, nine canonical books | **40,943** — matches the published count exactly |
| naming links, this re-implementation | **394 over 58 surahs** |
| naming links, published H-NEW-860.1 | **394 over 58 surahs** |
| ρ(this run's per-surah counts, published per-surah counts) | **+1.0000** |

An independently written implementation of the locked rule reproduces the published instrument
exactly. `norm()` is self-tested at runtime against a fixed vocalised basmala and every Arabic
character class is built from integer codepoints, per H-NEW-860.1 §2.1.

---

### 3.1 T1 — H-NEW-150's liturgical-prominence score → **PARTIAL**

**The proxy.** A hand-coded 0–17 score, 27 surahs non-zero, defined at
`h-new-150-liturgical-hub-prereg.md:60-71` (17 points for Q 1; 3 per prescribed occasion; 2 per
daily dhikr occasion; 1 per nightly-recitation ḥadīth). Its own finding says
*"Scoring is hand-coded and subjective … reflects my judgment about relative liturgical weight"*
(`h-new-150-liturgical-hub.md:188-195`). Published primary **ρ = 0.3121, p_perm = 0.0002**, a
PASS at its own α_bon = 0.025. **Reproduced here to four decimals: +0.3121.**

**The agreement.**

| formal instrument | operating range (n = 27) | full corpus (n = 114) |
|:--|--:|--:|
| **F1 — naming count, nine books** *(locked primary)* | **ρ = +0.4319**, p = 0.0245 | ρ = +0.0663, p = 0.484 |
| F2 — naming restricted to liturgical chapters (54 of 429) | ρ = +0.4724, p = 0.0128 | ρ = +0.2307, p = 0.0135 |
| quotation count | ρ = +0.4956, p = 0.0086 | ρ = +0.2508, p = 0.0071 |
| union (quotation ∪ naming) | **ρ = +0.5030**, p = 0.0075 | ρ = +0.2494, p = 0.0074 |

**Read the two columns together, and note that they invert the 860 pattern.** The 860 rubric
scored +0.374 full-corpus and +0.055 in-range: it could separate presence from absence and
could not rank. **The 150 score is +0.0663 full-corpus and +0.4319 in-range: it ranks and
cannot select.** Two proxies, two opposite profiles, and either one alone would have produced
the wrong general lesson.

**The headline re-run — it does not survive.**

| substitution | ρ with cluster degree | p (scipy) | p_perm, seed 20260808 / 20260818 | partial ρ controlling log surah words |
|:--|--:|--:|--:|--:|
| published hand score | **+0.3121** | 0.00072 | 0.0002 | — |
| **F1 naming** | **−0.0556** | 0.557 | 0.5533 / 0.5542 | −0.0634 (p = 0.503) |
| quotation | +0.0217 | 0.819 | 0.8138 / 0.8173 | +0.0315 (p = 0.740) |
| union | +0.0265 | 0.780 | 0.7727 / 0.7797 | +0.0374 (p = 0.693) |

**Three formal reception instruments, no correlation with cluster-network degree in any of
them.** The liturgical-hub link is a property of the hand score.

**The selection failure, which is where the score actually breaks.**

- **45 surahs carry a formal naming count and a liturgical score of 0.** The largest is
  **Q 4 al-Nisāʾ — 38 naming links and 232 quotation records, the second-most-cited surah in
  the nine books — scored 0.** Then Q 25 al-Furqān (16 / 32), Q 5 al-Māʾida (11 / 119),
  Q 9 al-Tawba (11 / 89), Q 48 al-Fatḥ (11 / 35), Q 33 al-Aḥzāb (7 / 130).
- **The 27 scored surahs capture 213 of 394 naming links — 54.1 %.**
- **Top-10 overlap is 4 of 10** against naming and 4 of 10 against quotation.

**And the honest correction to my own locked instrument choice.** The prereg made F1 primary on
the reasoning that *"a liturgical prescription names rather than quotes"*. **That reasoning is
measurably wrong for short surahs**, and the data say so plainly. Of the 14 scored surahs with
zero naming links, most are heavily *quoted*:

| surah | score | naming | **quotation** |
|:--|--:|--:|--:|
| Q 112 al-Ikhlāṣ | 4 | 0 | **111** |
| Q 109 al-Kāfirūn | 1 | 0 | **55** |
| Q 113 al-Falaq | 3 | 0 | **36** |
| Q 88 al-Ghāshiya | 2 | 0 | **20** |
| Q 114 al-Nās | 3 | 0 | **18** |
| Q 63 al-Munāfiqūn | 3 | 0 | **15** |
| Q 67 al-Mulk | 3 | 0 | **0** *(instrument artefact — H-NEW-860.1 §9.1: the tradition cites it by a four-word title the locked N = 5 span cannot see)* |

**The tradition quotes the short liturgical surahs and names the long ones**, and
H-NEW-860.1 §10.2 measures a further **159 naming events** the no-alias rule discards
(`فاتحة الكتاب` 58, `أم الكتاب` 23, `المعوذتين` 16), absorbed mostly by Q 1, Q 2, Q 113
and Q 114 — the rubric's own top of list.

**This does not change the verdict, and that is the point of reporting all four arms.** ρ_op
runs from +0.4319 to +0.5030 across every instrument, all four inside PARTIAL, and the headline
re-run is null on all three reception channels including the one with no blind spot for short
surahs. **The locked answer and the better answer agree.**

**Drift declaration** — `UNIT-DRIFT-DEFECT.md` §5, discharged:

| variable | ρ with log surah word count | ρ with log verse count |
|:--|--:|--:|
| liturgical score | −0.1028 (p = 0.276) | −0.1382 (p = 0.142) |
| cluster degree | −0.0121 (p = 0.899) | +0.0161 (p = 0.865) |
| F1 naming | **+0.6596** (p = 1.5 × 10⁻¹⁵) | +0.5849 |
| quotation | +0.4847 | +0.3282 |

**Neither variable in H-NEW-150's published correlation is size-loaded.** That is a CLEAN result
on the unit-drift screens and it should be credited as one. The size loading is entirely on the
side of the *formal* instrument — which is why the substitution changes the answer.

#### 3.1a The reversal — H-NEW-150's own NULL is an artefact **(POST-HOC)**

Post-hoc, in its own run directory, changing no locked verdict.

H-NEW-150's SECONDARY arm residualised both variables against `log(n_verses)` by OLS and
correlated the residuals: **ρ = 0.0859, p = 0.185, FAIL.** The finding calls this
*"the more important finding"* and explains it with a length-extremity mechanism —
*"the CORRELATION is between surah-length-extremity and both variables"*.

**The published residual reproduces exactly (+0.0859, Δ = 0.000000). The mechanism does not.**

- ρ(liturgical score, |log verses − median|) = **+0.1754** (p = 0.062);
  ρ(cluster degree, |log verses − median|) = **+0.0004** (p = 0.996).
  **The asserted length-extremity channel is absent from the degree variable entirely.**
- **The score has 87 tied zeros of 114.** Before residualising they are one tied rank. After,
  they occupy **66 distinct values spanning −1.1488 to −0.4221, ordered at ρ = +1.0000 with log
  verses.** Residualising a zero-inflated score against length **replaces the tie with a pure
  length ordering**, and the residual coefficient is then substantially a length-versus-degree
  correlation computed over 87 surahs that carry no liturgical information at all.
- A **rank-based partial Spearman**, which cannot manufacture order among ties, returns
  **+0.3174 (p = 0.0006)** — the raw value, essentially untouched.

**So H-NEW-150 has two errors pointing in opposite directions, and they do not cancel.** Its
primary is real and is not a length confound; its secondary FAIL is an artefact of the control
rather than a property of the data. And its primary still does not survive replacing the hand
score with a formal count. **The correct terminal statement is that the liturgical-hub
correlation is a property of one rater's liturgical scoring, neither confirmed nor explained by
surah length, and not reproduced by any formal measure of ḥadīth reception.**

This is `UNIT-DRIFT-DEFECT.md` §4.1's shape again — **a flagged NULL that reverses** — arriving
from a third direction: not a mis-specified null this time, but a control applied to a
zero-inflated variable.

**T1 CLASSIFICATION: PARTIAL** (ρ_op = +0.4319 on the locked primary, above the 0.20 NOISE
floor and below the 0.60 CARRIES bar; headline does not reproduce).

---

### 3.2 T2 — the Nöldeke chronology rank → **PARTIAL**

**What this test is and is not.** There is no computable ground truth for revelation chronology,
and this finding does not pretend otherwise. What is computable is **inter-rater agreement
between the two independent orderings sitting in the same file**: `data/revelation-order.csv`
carries both `noldeke_order` and `revelation_order` (the Tanzīl Egyptian standard).

**The agreement.**

> **ρ(Nöldeke, Egyptian standard) = +0.7714** (p = 1.0 × 10⁻²³), Kendall τ = +0.5771.
> **38 of 114 surahs sit more than 20 rank places apart.** The largest: **Q 99 al-Zalzala by 68
> places**, Q 82 by 56, Q 84 and Q 55 by 54, Q 79 by 50, Q 83 by 49, Q 7 by 48, Q 1 by 43.

#### An absence claim of my own, checked and FALSE — and it improves the result

**This coefficient had already been computed in this repository, and my first draft of this
section said it had not.** `h-new-212-alt-chronology-fisher-rao.md:54-63` publishes
**ρ(Egyptian, Nöldeke) = +0.771** as a diagnostic, alongside **four** chronologies rather than
two — Nöldeke 1860, Bell 1937, Egyptian Standard 1924, Blachère 1947 — with
ρ(Bell, Nöldeke) = +0.954, ρ(Blachère, Egyptian) = +0.963 and ρ(Bell, Blachère) = +0.689.

The claim was caught by running `ABSENCE-CLAIMS.md` §3's grep against my own sentence before
publishing it. **Two consequences, and both are gains:**

1. **The two harnesses agree to three decimals — +0.771 against +0.7714, separately built.**
   That is an instrument confirmation the census would not otherwise have had, and it is worth
   more than the originality claim it replaces.
2. **What had genuinely never been done is the rater swap on H-NEW-125's axes**, which is the
   part of T2 that carries the result. H-NEW-212 measured chronology-against-chronology and
   chronology-against-mushaf; **no finding has re-scored a published content map under a second
   rater.** That is the honest, narrower statement of what is new here.

**And H-NEW-212 supplies a mechanism this test did not have.** It sorts the four chronologies
into *"length-sorted (Egyptian, Blachère)"* and *"style-sorted (Nöldeke, Bell)"*. **On the data
measured here, that labelling is the wrong way round for the pair in play:**

| ordering | ρ with log surah word count | ρ with mean verse length |
|:--|--:|--:|
| **Nöldeke rank** | **+0.6775** | **+0.9038** |
| Egyptian standard | +0.4436 | +0.6690 |

**Nöldeke is the more size-loaded of the two orderings**, by half again on the word-count
channel — consistent with H-NEW-212's own ρ(mushaf, Nöldeke) = −0.655 against
ρ(mushaf, Egyptian) = −0.406, since the mushaf is length-descending (H-NEW-226: τ = +0.84).
H-NEW-125's axes are **per-verse densities**, which is exactly `UNIT-DRIFT-DEFECT.md`'s setup.
**So the shrinkage below is not only rater noise: it is what a size-loaded ordering losing half
its size loading does to a family of per-verse densities.** *(Flagged for the ledger keeper —
H-NEW-212's two-schools labelling of the Egyptian/Nöldeke pair does not match the size
measurement, and the correction belongs in the file that carries it.)*

**The rater swap on H-NEW-125's own numbers.** Every axis value is taken **verbatim** from
`csv/h-new-125.json` — nothing is re-derived — so every difference below is attributable to the
ordering alone. Permutation p, 10,000 draws, against H-NEW-125's own α_bon = 0.00333.

| axis | ρ \| Nöldeke | ρ \| Egyptian | Δ | survives |
|:--|--:|--:|--:|:--|
| mean_verse_length | **+0.9038** | **+0.6690** | **−0.2348** | both |
| divine_name_density | +0.8973 | +0.6258 | −0.2714 | both |
| allah_density | +0.8520 | +0.6590 | −0.1929 | both |
| loanword_density | +0.8329 | +0.5699 | −0.2630 | both |
| eschatological_density | +0.7096 | +0.5167 | −0.1929 | both |
| legal_term_density | +0.7039 | +0.5657 | −0.1382 | both |
| book_reference_density | +0.5744 | +0.4166 | −0.1577 | both |
| **qul_density** | +0.5421 | **+0.2607** | **−0.2813** | **Nöldeke only** |
| prophet_narrative_density | +0.5304 | +0.3114 | −0.2190 | both |
| personal_pronoun_density | +0.4956 | +0.3808 | −0.1148 | both |
| **surah_length** | +0.3903 | **+0.2482** | −0.1421 | **Nöldeke only** |
| muq_cardinality | +0.2547 | +0.0290 | −0.2257 | neither |
| rhyme_letter_diversity | +0.1789 | +0.1409 | −0.0380 | neither |
| refrain_density | +0.0023 | +0.0484 | +0.0461 | neither |
| oath_density | −0.0041 | +0.0183 | +0.0224 | neither |

- **The published passing set reproduces exactly under Nöldeke: 11 of 15, same axes.** The
  instrument is correct.
- **Under the alternative rater it is 9 of 15.** `qul_density` and `surah_length` stop
  surviving. No axis is gained.
- **Sign agreement is 14 of 15** — only `oath_density`, which is null under both at |ρ| < 0.02,
  flips.
- **Thirteen of fifteen coefficients shrink**, several by more than 0.25.

**The consequence for `UNIT-DRIFT-DEFECT.md` §3's drift table, which is the operationally
important part.** That table records the Nöldeke block's strongest channel as mean verse length
at **ρ = +0.9038**, and instructs future sessions to control against the strongest channel.
Under the alternative rater the same channel is **+0.6690**, verse count falls from +0.3903 to
+0.2482, and log word count from +0.6775 to +0.4436. **The drift figures are themselves
rater-specific, and a control calibrated on the Nöldeke value is calibrated on the larger of
two defensible numbers.** That is the conservative direction — but it should be recorded, not
discovered later.

**Two limits, both fixed before the run.** The orderings are **not independent in provenance** —
the Egyptian standard and Nöldeke's sequence draw on an overlapping body of *asbāb al-nuzūl*
reports, and the CSV's own source string names one file for both — so high agreement shows
reproducibility across rater communities and **not** correctness. And T2's operationalisation of
"the headline reproduces" — identical surviving axis set — was fixed at run time rather than at
lock time and is disclosed as a researcher degree of freedom; the counts are published so a
reader preferring a looser reading can apply it.

**T2 CLASSIFICATION: PARTIAL** (ρ = +0.7714, above the NOISE floor and above the CARRIES
threshold; but the surviving axis set is not identical, so the headline does not reproduce).

**The honest one-line reading: the chronology ordering is directionally rater-robust and
quantitatively rater-dependent.** No chronology *direction* in this repository is at risk. Every
chronology *magnitude* is an upper estimate.

---

### 3.3 T3 — `Q036_F_01`'s reconstructed rubric → **NOISE**

`surahs/Q036-yasin/scripts/Q036_F_01_recitation_frequency_weighted_centrality.py:59-99` builds a
114-entry weight table whose own docstring says: *"For surahs not at 10, we use a hand-coded
approximation drawn from H-NEW-860's structure"* and *"This is the LOCKED weights table per the
pre-reg. Modifying these post-hoc would violate the pre-reg."*

**It is a proxy of a proxy, and it does not reproduce the proxy it names as its source.**

| measurement | value |
|:--|--:|
| surahs scored by the reconstruction | **20** |
| surahs scored by the published H-NEW-860 rubric | **36** |
| of the published 36, dropped by the reconstruction | **18** — Q 6, 7, 17, 20, 23, 25, 32, 50, 57, 59, 61, 62, 63, 76, 78, 88, 97, 99 |
| scored by the reconstruction but absent from the published 36 | 2 — Q 56, Q 75 |
| values differing across the union support | **30 of 38** |
| **ρ(reconstruction, published rubric)** over the union support | **+0.4878** (p = 0.0019) |
| ρ(reconstruction, published rubric) over the published 36 | +0.5571 (p = 0.00042) |
| **ρ(reconstruction, formal quotation count)** over its own 20 | **−0.0396** (p = 0.868) |
| ρ(reconstruction, formal naming count) over its own 20 | −0.2208 (p = 0.350) |

**Half the source rubric's surahs are missing and four-fifths of the retained values are
different, in a table the script calls locked and pre-registered.** Against the formal count it
is at ρ = −0.0396 — statistically indistinguishable from the parent's +0.055 and on the wrong
side of zero.

**State what is new here and what is inherited, because they are not the same.** The NOISE label
against the formal count is largely **inherited**: H-NEW-860.1 already measured the parent
rubric as carrying no discriminative information, so a faithful derivative could not have scored
well. **The new information is the +0.4878 — a derived table that does not reproduce its own
declared source.** That failure is independent of whether the source was any good.

**T3 CLASSIFICATION: NOISE** (ρ_op = −0.0396, |ρ| < 0.20; the headline cannot reproduce because
the parent is already retired).

---

## 4. The detection cues, with their yield

Recorded so the next sweep starts from a measured list rather than an invented one. Counts are
raw grep hits over `findings/` + `surahs/` + `scripts/`, `*.md` and `*.py`, excluding `/runs/`.

| cue | hits | signal quality |
|:--|--:|:--|
| `0-10` / `0–10` | 112 | low — mostly ranges and version strings |
| `eyeball` | 65 | **high for provenance, low for proxies** — most hits are honest post-hoc-origin disclosures in preregs, which is the discipline working |
| `by inspection` | 39 | **low** — dominated by *"closed-form hypergeometric, reproducible by inspection"*, the opposite of a hand-assignment |
| `hard-coded` | 31 | medium |
| `manually` | 25 | medium |
| `subjective` | 18 | **high** |
| `hand-built` | 15 | **high** |
| `coded as` | 15 | low |
| `hand-coded` | 12 | **highest single-cue precision** |
| `hand-curated` | 11 | **high** |
| `judged by` | 6 | high |
| `impressionistic` | 6 | high — but usually describing a *classical* claim being tested, not a project proxy |
| `hand-tagged` | 6 | high |
| `curated list` | 6 | high |

**The two cues worth running first are `hand-coded` and `hand-curated`.** `by inspection` and
`eyeball` are the two worth running last: both are dominated by the project *disclosing* its own
post-hoc origins, which is a virtue and not a defect, and a sweep that treats them as hits will
drown.

**The cue that found nothing and should have found something.** `researcher-judged`,
`we classified`, `qualitative score` and `hand-assigned` return **zero hits each**. A proxy is
described in this repository as *"mine"*, *"hand-coded"*, or *"my judgment"* — first person and
informal — never in the vocabulary an auditor would naturally reach for.

---

## 5. Honest limits

1. **The census finds only self-declaring proxies** (§1). It is a lower bound.
2. **T1's F1 systematically under-counts short liturgical surahs** (§3.1), and the prereg's
   stated reason for making naming primary is refuted by the data. All four arms are reported
   and they agree on the classification; the locked one is the one labelled primary.
3. **T2 cannot validate chronology** and its two orderings share provenance (§3.2).
4. **T2's "headline reproduces" rule was fixed at run time**, not at lock time. Disclosed;
   both the set comparison and the counts are published.
5. **T3's NOISE label is partly inherited** from the parent's retirement (§3.3). The +0.4878 is
   the part that is new.
6. **Eleven Tier-1 proxies were not reached**, listed by name in §2.1 and again in §6. Three
   proxies done properly was the instruction and it is what happened; the rest are the next
   session's queue, not a claim that they are sound.
7. **The 0.20 and 0.60 thresholds are a convention**, anchored on H-NEW-860.1's +0.055 and fixed
   before any coefficient existed. They are not a law and a reader may re-classify from the
   published coefficients.
8. **No claim about the Qurʾān rests on any coefficient in this finding.** What has been tested
   is whether three hand-assigned measurements track computable ones.

---

## 6. What was not reached, so the next session starts here

In consequence order, each with its computable alternative already identified:

1. **H-NEW-125's `LEGAL_ROOTS` / `ESCHAT_ROOTS` / `BOOK_ROOTS`** — 3 of the 11 surviving axes
   rest on 13 hand-chosen roots total. Test: seed-expansion sensitivity over
   `data/morphology/root-cooccurrence-graph.json`, plus leave-one-root-out. **Highest
   consequence of the unreached set.**
2. **The oath-opener list (H-NEW-154) against H-NEW-85's QAC re-run and H-NEW-2210's
   generator.** Both computed alternatives already exist on disk; **only the agreement figure is
   missing**, and this is the cheapest remaining test in the queue. **It is also the one most
   likely to return CARRIES INFORMATION**, and that result is worth as much as a condemnation.
3. **`ism-azam-composite-test` axis 8** against a formal tafsīr-attention count over the five
   corpora `ABSENCE-CLAIMS.md` §6 FALSE #5 established are on disk.
4. **H-NEW-2020's Rule-F allow-lists** against QAC morphology.
5. **H-NEW-140's classical divine-name pairs** — H-NEW-170 already ran the exhaustive network;
   the agreement coefficient between the hand-picked pairs and the computed network has not been
   published as a number.
6. Then, in order: H-NEW-1390's 20-class taxonomy, H-NEW-2640's governor rule, H-NEW-50's
   4-gram set, Q002-F-04's thematic matrix, and the Tier-2 catalogue proxies.

---

## 7. Run record

- Locked run `runs/h-new-2920/20260807T225701Z/` — `result.json`, `console.log`, `MANIFEST.txt`
  (SHA-256 of all 16 inputs and both outputs). Mode `'x'`, `exist_ok=False`, written once at
  completion; no file inside it rewritten.
- Post-hoc run `runs/h-new-2920/20260807T225823Z-posthoc/`.
- **`runs/h-new-2920/20260807T225604Z/` is empty and is left in place deliberately.** The first
  invocation created its directory and aborted on a `TypeError` — H-NEW-860's rubric stores
  unscored surahs as `null`, not `0`, and the runner coerced without a guard. **A run directory
  is never deleted in this repository**, so the empty one stands as the record that an attempt
  was made and failed. It contains no results and none are missing.

**A defect in that rule as implemented, found while checking this run's own directories.**
**Git cannot track an empty directory.** H-NEW-860.1's aborted
`runs/h-new-860-1/20260807T221825Z-posthoc/` is **absent from `git ls-files`** while its two
sibling run directories are tracked in full. *"A run directory is never deleted"* therefore
holds in the working tree and **silently fails at the commit boundary** for exactly the case it
was written for — the aborted run. The record of a failed attempt survives only in the finding's
prose, which is the weakest place it could live.

**The fix is one line and belongs in the runner, not in a commit habit** — the same shape as
`UNIT-DRIFT-DEFECT.md` §7's correction: write an `ABORTED.txt` into the directory at creation
time, carrying the timestamp and the invocation, so a crashed run leaves a tracked artifact
rather than an untrackable void. *(Not applied retroactively here — that would mean writing into
another finding's run directory.)*

---

## 8. What should change in the repository

1. **`findings/PROXY-CLAIMS.md` is written** — the third rule document, alongside
   `UNIT-DRIFT-DEFECT.md` and `ABSENCE-CLAIMS.md`.
2. **H-NEW-150 needs two notices, not one.** Its SECONDARY FAIL should be marked as a
   residualisation artefact (§3.1a), and its PRIMARY PASS should be marked as not surviving
   substitution of a formal count. **Both, or the file will be read as half-corrected.**
3. **`UNIT-DRIFT-DEFECT.md` §3's drift table should record that its Nöldeke block is
   rater-specific** — mean verse length +0.9038 under Nöldeke, +0.6690 under the Egyptian
   standard (§3.2).
4. **H-NEW-125's *"PERVASIVE CHRONOLOGY"* should be restated as 9–11 of 15 depending on the
   rater**, with the two rater-sensitive axes named.
5. **`Q036_F_01`'s weights table should be marked as not reproducing its declared source**
   (§3.3).
5a. **H-NEW-212's "length-sorted (Egyptian, Blachère) / style-sorted (Nöldeke, Bell)" labelling
   should be corrected for the pair in play** — measured here, **Nöldeke is the more
   size-loaded ordering** (ρ = +0.6775 with log surah word count against the Egyptian standard's
   +0.4436; +0.9038 against +0.6690 on mean verse length). The correction belongs in the file
   that carries the labelling, per `ABSENCE-CLAIMS.md` §4.
6. **UNIT-DRIFT §3 should gain Screen A′ as H-NEW-860.1 §7.4 proposed.** This census is the
   second independent arrival at that gap.

---

## 9. Cross-references

- **[[h-new-860-1-fadail-formal-count|H-NEW-860.1]]** — the calibration parent; ρ = +0.055.
- **`findings/PROXY-CLAIMS.md`** — the rule this finding establishes.
- **`findings/UNIT-DRIFT-DEFECT.md`** — §5 discharged in §3.1; §3's Nöldeke block amended in
  §3.2; §4.1's reversing-NULL shape recurs in §3.1a; §6.2's counting rule used throughout §2.
- **`findings/ABSENCE-CLAIMS.md`** — §6 FALSE #3 licensed the 860 rubric; FALSE #5 is why the
  ism-azam axis-8 test in §6 is runnable.
- **[[h-new-150-liturgical-hub|H-NEW-150]]** — T1's host.
- **[[h-new-125-chronology-content|H-NEW-125]]** — T2's host.
- **[[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]** — published ρ(Egyptian, Nöldeke) = +0.771
  before this finding did, reproduced here at +0.7714; supplies the four-chronology context and
  the two-schools labelling that §3.2 corrects.
- **[[h-new-840-unified-architectural-score|H-NEW-840]]** — the boundary case, §2.3.
- **[[h-new-170-99name-network|H-NEW-170]]** and **[[h-new-2210-qasam-jawab-inventory|H-NEW-2210]]** —
  the two places this project replaced a curated list with a generator on its own initiative.

---

*Run 2026-08-08 by Waiel Al-Shujaa against a pre-registration locked before any agreement
coefficient existed. One rubric could tell presence from absence and not rank; another can rank
and cannot select; a scholarly ordering agrees on direction and not on magnitude. A hand-built
proxy is not automatically noise — but it is automatically an unmeasured claim.
Bismillāhi al-Raḥmāni al-Raḥīm.*
