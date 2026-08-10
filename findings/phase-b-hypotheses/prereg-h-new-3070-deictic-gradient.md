---
title: "Pre-registration — H-NEW-3070: does the proximal/distal deictic balance shift across the Nöldeke phases?"
author: Waiel Al-Shujaa
date: 2026-08-09
status: PRE-REGISTERED — locked before any phase-conditional deixis quantity was computed
frontier_item: F-4 (HANDOFF/FRONTIER-MAP-2026-08-07.md:254) — SECOND CLAUSE ONLY
supersedes_nothing: true
prior_work_on_this_item: findings/phase-b-hypotheses/h-new-2960-spatial-deixis.md
method_parents:
  - findings/UNIT-DRIFT-DEFECT.md
  - findings/PROXY-CLAIMS.md
  - findings/ABSENCE-CLAIMS.md
  - findings/TIED-OUTCOME-DEFECT.md
  - findings/phase-b-hypotheses/cross-finding-029-the-deciding-parameter.md
model_finding: findings/phase-b-hypotheses/h-new-3030-sajdah-glyph.md
script_path: findings/phase-b-hypotheses/scripts/h-new-3070.py
seed_primary: 20260509
n_permutations: 10000
git_commit_at_lock: e7654b403ff161585154d7ade503868e37b909c1
---

# H-NEW-3070 — pre-registration

## 0. SCOPE — what this tests, and the far larger part of F-4 it refuses to touch

**F-4 is two claims joined by a comma, and only one of them is open.**

The frontier map's F-4 reads: *"Proximal demonstratives cluster on present/this-world referents,
distal on the Hereafter and on scripture-as-object (`dhālika l-kitāb`), **giving a measurable
deictic gradient across the Nöldeke phases**."*

**Clause 1 — the eschatological-reference claim — was executed on 2026-08-08 by H-NEW-2960 and
returned NULL.** That lane's front-matter names `frontier_item: F-4` outright. It is not
re-litigated here, it is not replicated here, and this pre-registration claims **no novelty
whatsoever** for anything in it. Its results, for the reader's orientation only:

| H-NEW-2960 result | value |
|:--|:--|
| census | 1,059 `POS:DEM` = 330 proximal + 729 distal |
| eschatological arm (dunyā/ākhira antonym pair) | OR 2.743, exact clustered-permutation p = 0.0605, n = 49 |
| gate | α = 0.0167 → **NULL** |
| bracketing sensitivity | p = 0.269 (over-exclusive marker rule) |
| muqaṭṭaʿāt confound | **0 of 17 opening demonstratives eligible**; Q 2:2 UNCLASSIFIED; deletion changes nothing |
| drop-the-formulae arm | OR **rises** 2.74 → 3.00 (top-10 dropped) → 4.19 (`ka-dhālika` dropped) |

**Clause 2 — the chronological gradient — was never touched.** `grep -niE
"noldeke|nöldeke|chronolog|revelation-order|meccan|medinan|gradient"` over
`h-new-2960-spatial-deixis.md` and `prereg-h-new-2960-spatial-deixis.md` returns **zero** matches
in either file. `data/revelation-order.csv` is not opened by `scripts/h-new-2960.py`. **This
pre-registration covers clause 2 and nothing else.**

**This is the H-NEW-3030 pattern, deliberately.** That lane found F-8 already executed by
H-NEW-2950 and, instead of re-running it, did the two things the brief demanded which the prior
lane had not done. The same posture is taken here.

### 0.1 What is genuinely new, stated as a list so it can be checked against H-NEW-2960

1. **The chronological axis.** Never computed for deixis by any lane.
2. **The multi-channel length sweep** mandated by [[cross-finding-029]] §3.1 rule 2. H-NEW-2960
   stratified on **one** channel (verse length, quintiles/deciles) and only on its secondary
   instrument. Four channels are run here, and the **worst** governs.
3. **A confound that can actually reach the test.** In H-NEW-2960 the muqaṭṭaʿāt openings were
   *outside the eligible set by construction* (0 of 17), so the deletion arm was vacuous — it
   changed nothing because it could not. **On the chronological axis all 17 are inside the test**,
   and the 29 muqaṭṭaʿāt surahs are heavily Late-Meccan. The leave-the-formulae-out arm is
   therefore live here for the first time, and it is the decisive analysis.

## 1. The hypothesis, and the direction — LOCKED AND JUSTIFIED

> **H: the DISTAL share of demonstratives increases across the Nöldeke phases**
> (Early Meccan → Middle Meccan → Late Meccan → Medinan).

**One-sided, upper. Locked before any phase-conditional deixis quantity was computed.**

### 1.1 Why this direction and not its opposite — three in-house anchors

The direction is not free. A competing prediction exists and must be dismissed on the record:
Early Meccan is the *eschatological-warning* register, and if distal tracks the Hereafter (F-4
clause 1) then distal should be **high early** and the gradient should run **downward**. That
prediction is rejected on the following grounds, all of which are prior in-house results:

1. **Clause 1 is NULL.** H-NEW-2960 found no usable distal↔Hereafter association (p = 0.0605,
   bracketed to 0.269). The premise of the downward prediction does not hold in this corpus, so it
   cannot license a direction.
2. **Scripture-as-object is a LATE-MECCAN apparatus.** `cross-finding-012-late-meccan-scripture-announcement`
   and `cross-finding-016-late-meccan-apparatus-deep-dive` establish the scripture-announcement
   layer as Late Meccan. Its signature formula is distal — `tilka āyātu l-kitāb`, and per
   MASTER-FINDINGS-LEDGER line 919 the *tilka āyāt al-X* opening occurs in Q 10, 12, 13, 15, 26,
   27, 28, 31, **all muqaṭṭaʿāt-opened**. F-4's own parenthesis (`dhālika l-kitāb`) is this layer.
3. **The distal's dominant corpus use is the anaphoric group-verdict formula.** H-NEW-2960 §1.4
   ranks phrase types corpus-wide: *ulāʾika humu* (58), *ulāʾika lladhīna* (28), *ulāʾika aṣḥābu*
   (21) — **107 tokens in three formulae**. This is communal-adjudicative discourse, which
   `cross-finding-028-formal` locks as the legal-Medinan register. Additionally the 47
   addressee-kāf plural forms (*dhālikum* 28 + *dhālikumu* 11 + *dhālikum* 8) are second-person
   address forms, and cf-028-formal finds legal-Medinan to be the most 2↔3-direct-address register
   (f_iltifāt = −0.671, the most negative of the three).

Conversely the **proximal** side is the Meccan polemical deixis — *mā hādhā illā…* ("this is
nothing but…"), which appears in H-NEW-2960's top-10 as *hādhā illā* (15 tokens) — pointing at the
present, contested Prophet and recitation.

**Two of the three anchors point at Late Meccan and one at Medinan, so the locked direction is a
monotone increase rather than a single-phase peak.** If the true shape is a Late-Meccan peak with
a Medinan fall-back, a monotone test is *conservative* against it, and that is accepted as the
cost of locking one direction.

### 1.2 The pre-registered risk that this is CBM

**My honest prior is that this will fail the length sweep.** The structural facts in §2.3 show
Early Meccan carrying 57 of 1,059 demonstratives across 24 surahs — Early Meccan surahs are the
short mufaṣṣal tail. H-NEW-2960 §7 separately measured that **distal share climbs monotonically
with verse length** (0.622 in the shortest quintile to 0.741 in the longest). Those two facts
alone can manufacture the entire locked gradient with no deictic content at all. **If the
unstratified arm passes and the stratified arms do not, the finding is that the gradient is
length, and that is the headline.**

## 2. Instruments — all three are functions, none is a list

### 2.1 The deixis partition — reused, not rebuilt

> **DEIXIS(t) = DISTAL if the QAC `FORM` of the `POS:DEM` segment ends in the addressee-kāf
> enclitic, PROXIMAL otherwise.** Regex `(?:ka|ki|kumo|kumu|kumaA|kum|kun~a)$`

This is H-NEW-2960's rule verbatim, adopted because it has already been validated against an
independently constructed lemma partition with **0 disagreements on all 1,059 tokens**. Rebuilding
it would create a second instrument where a validated one exists. **It was re-executed
independently for this pre-registration and reproduces 1,059 = 330 proximal + 729 distal exactly**
(§2.3). No surah, verse, lemma or form is hard-coded.

### 2.2 The chronology — the rules-tuple axis

`data/revelation-order.csv`, 114 rows, complete over mushaf 1–114, no blanks. Four fields are
usable and they **disagree with each other**, which is why chronology is the rules-tuple axis
rather than a fixed choice:

| field | values | note |
|:--|:--|:--|
| `noldeke_phase` | Early Meccan 48 · Middle Meccan 21 · Late Meccan 21 · Medinan 24 | **primary**, ordinal 1–4 |
| `revelation_order` | 1–114, all distinct | Tanzil Egyptian standard |
| `noldeke_order` | 1–114, all distinct | Nöldeke rank |
| `period` | Meccan 86 · Medinan 28 | **disagrees with `noldeke_phase` on 4 surahs** (28 vs 24 Medinan) |

That 4-surah disagreement is recorded now, before any test, as a declared rules-tuple dependency.

### 2.3 Structural quantities measured BEFORE locking — and why that is permitted

[[TIED-OUTCOME-DEFECT]] §5 **requires** the tie fraction of the outcome to be stated in the
pre-registration. The following were therefore computed pre-lock. **They are exposure and shape
quantities only. No quantity crossing deixis with chronology was computed** — the direction in §1
was fixed from the three published anchors, not from data.

| quantity | value |
|:--|--:|
| `POS:DEM` tokens | 1,059 (= map's figure, verified) |
| `POS:LOC` / `POS:T` | 669 / 1,166 (both = map's figures, verified) |
| distal / proximal | 729 / 330 (= H-NEW-2960, reproduced exactly) |
| surahs with ≥1 DEM | 88 of 114 |
| **DEM tokens by phase** | Early Mec **57** · Middle Mec 249 · Late Mec 381 · Medinan 372 |
| **surahs-with-DEM by phase** | Early Mec 24 · Middle Mec 20 · Late Mec 21 · Medinan 23 |
| surahs with < 5 DEM tokens | 35 of 88 |
| **tie fraction, per-surah distal share** | **0.2273** (modal value 1.0, 20 surahs) |
| share exactly 0.0 / exactly 1.0 | 7 / 20 (boundary fraction 0.3068) |
| distinct share values | 45 |

**Tie-fraction consequence, stated as the rule requires:** 0.2273 is below the 50 % threshold at
which [[TIED-OUTCOME-DEFECT]] §3 forbids a parametric primary. **The trigger does not fire.**
A permutation null is used anyway, per §7.3 of that document (permutation nulls are immune
regardless), so the question is moot by construction — but it was measured rather than assumed.

**Early Meccan carries 5.4 % of the demonstratives from 21 % of the phase-weighted surah mass.
This is the single most important number in this pre-registration** and it is why §1.2 predicts
failure.

## 3. The statistics — two units, because unit choice is itself a deciding parameter

[[UNIT-DRIFT-DEFECT]] requires both units be reported. Both are verdict-bearing.

**H1 — token-level, surah-clustered.**
> **S1 = mean(phase ordinal | DISTAL tokens) − mean(phase ordinal | PROXIMAL tokens).**
> Locked direction: **S1 > 0**.

Weights each surah by how many demonstratives it actually contains. Long surahs dominate.

**H2 — surah-level, unweighted.**
> **S2 = Spearman ρ(phase ordinal, per-surah distal share)** over the 88 surahs with ≥ 1 DEM.
> Locked direction: **S2 > 0**.

Weights Q 112 equally with Q 2. Long surahs cannot dominate.

**Neither carries a minimum-token threshold**, because a threshold is a free parameter and
[[cross-finding-029]] §3 is precisely about free parameters deciding verdicts. The 35 surahs with
< 5 tokens are noisy under H2 and that noise is accepted rather than tuned away.

## 4. The null — permutation, and at the correct unit

> **Permute the phase labels among the 88 surahs that enter the statistic. Tokens travel with
> their surah.** 10,000 permutations, seed **20260509**.

Phase is a **surah-level** property, so the surah is the exchangeable unit. Permuting tokens
individually would destroy the clustering and be anticonservative — the error H-NEW-2960 §3.3
avoided for the same reason. The 26 surahs with zero demonstratives are excluded from the label
pool: their labels cannot affect either statistic, and including them would permute labels onto
units that contribute nothing.

**p = (1 + #{S_null ≥ S_obs}) / (1 + 10000)**, one-sided upper. Floor 9.999 × 10⁻⁵.

**Null-distribution tie diagnostic (required output, not optional):** the run must report, for
every cell, the number of distinct values in the null distribution and the fraction of draws
exactly equal to S_obs. **If ties in the null exceed 50 % for any verdict-bearing cell, that
cell's p must be recomputed by exact enumeration** per [[TIED-OUTCOME-DEFECT]] §3, and the run
must say so.

## 5. THE LENGTH-CHANNEL SWEEP — the mandated core of this design

[[cross-finding-029]] §3.1 rule 2: *"length is at least three variables (verse count, word count,
mean verse length). Name the channel, and run all of them."* H-NEW-3010 saw a ~70× p-swing across
channels; H-NEW-3040 saw its verdict flip 3 PASS / 5 NULL across eight. **No channel is locked a
priori.**

Four per-surah channels, all computed from QAC:

| id | channel |
|:--|:--|
| **L1** | verse count |
| **L2** | word count |
| **L3** | **mean verse length** (words / verses) |
| **L4** | demonstrative count — the *exposure* channel |

**L4 is included because it is the channel this design is most exposed to and the one
cross-finding-029's three named channels would have missed.** A surah's demonstrative count is its
exposure, and exposure is confounded with phase (§2.3).

**Control = stratified permutation.** Phase labels are permuted only *within* strata formed by
rank-binning the 88 surahs on the channel. Two bin widths, both run, per
[[UNIT-DRIFT-DEFECT]] §6.1: **quintiles (5) and deciles (10)**. Ties in the channel value broken
deterministically by ascending surah number.

**9 settings per (H, arm, tuple):** L0 unstratified, plus L1–L4 × {quintile, decile}.

**Power diagnostic, required output:** for each stratified setting, report the number of strata
containing ≥ 2 distinct phase labels ("informative strata") and the share of surahs inside them.
**A stratification that leaves no permutation freedom produces p → 1 for arithmetic reasons and
not evidential ones, and must not be read as a refutation.** This is stated now so it cannot be
claimed afterwards.

## 6. Arms — the formula-exclusion list, PRE-REGISTERED as required

The brief requires the exclusion list be fixed before computing. It is a **function**, not a
stored list of surahs:

| arm | rule | expected n dropped |
|:--|:--|--:|
| **A0** | full inventory | 0 |
| **A1** | **drop every `POS:DEM` token in vv. 1–3 of any surah containing a `POS:INL` segment** | 17 |
| **A2** | drop every `POS:DEM` token whose word carries a `ka+` prefix (*ka-dhālika*) | 126 |
| **A3** | drop every token of the **top-10 corpus-wide** DEM phrase types (DEM form + next word's first stem), ranked over the whole corpus, never within a subgroup | — |
| **A4** | **A1 ∪ A2 ∪ A3 — drop all of them** | — |

**The 29 muqaṭṭaʿāt surahs are derived in code from `POS:INL`. No stored list of 29 surahs is read
anywhere.** H-NEW-2960 verified this derivation returns exactly {2, 3, 7, 10, 11, 12, 13, 14, 15,
19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}.

**A1 and A4 are the decisive arms.** Per the brief: if removing ~20 formulaic phrases kills the
effect, that is the finding and it goes in the abstract.

## 7. Rules-tuple — four settings, ≥ 2 as required

| id | chronology | deixis rule |
|:--|:--|:--|
| **R1** | `noldeke_phase` ordinal 1–4 | kāf-suffix — **PRIMARY** |
| **R2** | `revelation_order` rank 1–114 (Egyptian standard) | kāf-suffix |
| **R3** | `noldeke_phase` ordinal 1–4 | **lemma partition** |
| **R4** | `period` binary Meccan=1 / Medinan=2 | kāf-suffix |

Under R2 the phase ordinal in S1/S2 is replaced by the revelation-order rank; the statistics are
otherwise identical.

## 8. THE DECISION RULE — locked, exact, and to be diffed line by line against the verdict function

Let `p_worst(H, arm, tuple)` = **max** of the one-sided p over all 9 length settings of §5.

> **PASS** iff, for tuple **R1** and arm **A0**:
> `p_worst(H1, A0, R1) < 0.025` **AND** `p_worst(H2, A0, R1) < 0.025`
> **AND** both observed statistics are strictly positive (direction as locked in §1).
>
> **NULL** otherwise.
>
> **If and only if the verdict is PASS**, the formula arms are then read:
> **CONFIRMED-BUT-FORMULAIC** iff PASS holds for A0 but fails for **A1 or A4** under the same
> `p_worst` rule. This verdict **takes precedence in the abstract over the bare PASS.**
>
> **A NULL verdict is not downgraded or upgraded by any other arm, tuple, or channel.**
> R2/R3/R4 and A1–A4 are robustness reporting only and **cannot create, rescue or upgrade a
> verdict.** They are reported at equal prominence whatever they show.

**α = 0.05 / 2 = 0.025**, Bonferroni over the **two verdict-bearing hypotheses H1 and H2.**

**Why the 9 channels are NOT in the Bonferroni denominator:** the rule takes the **worst** channel,
which is a *minimum-over-settings of significance*, i.e. strictly conservative. Correcting for
multiplicity on top of taking the worst would double-penalise the same conservatism. The tuples
and arms are likewise not in the denominator because they are barred from bearing a verdict.
**This reasoning is fixed now so it cannot be re-derived after seeing the numbers**, per
[[feedback_bonferroni_tightening_vs_loosening]] — and note it is the *tightening* direction
(taking the worst of 9) that is being self-applied, which that rule permits.

## 9. If the verdict is NULL — the MDE and power statement, specified before the numbers exist

[[cross-finding-029]] §3.2 and the brief both require it. On a NULL the run must report:

1. **S\*** — the smallest value of the statistic that would clear α = 0.025 under the observed
   null, per verdict-bearing cell.
2. **S_max** — the largest attainable value of the statistic given the observed marginals (all
   distal tokens in the latest phase, all proximal in the earliest). **If S\* > S_max the design
   could not have rejected under any data and the verdict is UNTESTABLE-AT-THIS-N, not NULL.**
   This branch must be computed and reported either way — H-NEW-3030's branch did not fire and
   only computing it established that.
3. **MDE as a phase-shift** — the difference in mean phase ordinal between distal and proximal
   tokens required for 80 % power, by simulation under the observed exposure structure.
4. **Power against a modest true effect** — the power to detect a shift of 0.25 phase units.

## 10. Run discipline

- **Pre-registration SHA-256** computed over this file after locking, embedded as the literal
  `EXPECTED_PREREG_SHA` in `scripts/h-new-3070.py`, **re-verified at runtime before the run
  directory is created**; mismatch → `SystemExit`.
- Run directory `findings/phase-b-hypotheses/runs/h-new-3070/<UTC>/` created with
  `os.makedirs(exist_ok=False)`; every artefact written with `open(..., 'x')`.
- **No run directory is ever deleted**, including from failed runs.
- Seed 20260509, 10,000 permutations, NumPy `default_rng`, RNG named here so §8's channel results
  are reproducible.
- `--self-check` verifies the deixis rule on four forms including `hākadhā` (proximal — its kāf is
  not final) and `ulāʾikum` (distal), and verifies the permutation p against a hand-computable
  case.
- This pre-registration is **immutable after the run** per [[feedback_prereg_immutability]].

## 11. Forking-paths log — every choice, and the Step-0 grep first

**Entry 1 — THE STEP-0 PRIOR-WORK GREP, run before any design existed.** Commands:
`grep -rniE "demonstrat|hadha|dhalika|POS:DEM|deixis|deictic|proximal|distal" MASTER-FINDINGS-LEDGER.md`
and `grep -rliE "demonstrativ|POS:DEM|deixis|deictic|proximal|distal|dhalika|hadha" findings/`.
**Result: F-4 clause 1 is ALREADY ANSWERED by H-NEW-2960 (2026-08-08), which names F-4 in its own
front-matter.** The census and the eschatological test were therefore **not** rebuilt. A second
grep established clause 2 is untouched (§0). **A third fact was found and is reported to the team
lead rather than acted on here: H-NEW-2960 has no entry in MASTER-FINDINGS-LEDGER.md** — the only
hit is an incidental cross-reference inside another finding's prose — so a future lane obeying the
map's binding rule by grepping the ledger alone would not find it.

**Entry 2 — direction.** A downward gradient was a live competing prediction (Early Meccan =
eschatological warning). Rejected on three published anchors, §1.1, all of which predate this
design. Locked upward. Recorded because the opposite lock was available and defensible.

**Entry 3 — the monotone-vs-peak choice.** A Late-Meccan peak with Medinan fall-back is plausible
(anchors 2 and 3 disagree on the endpoint). A monotone test was chosen because it needs no extra
parameter; it is conservative against a peak shape, and that cost is accepted rather than hidden.

**Entry 4 — unit.** Token-level and surah-level give different answers in principle and both are
registered as verdict-bearing rather than choosing one. Per [[UNIT-DRIFT-DEFECT]].

**Entry 5 — no minimum-token threshold.** A threshold on demonstratives per surah would be a free
parameter of exactly the kind [[cross-finding-029]] indicts. None is used.

**Entry 6 — L4, the exposure channel.** Added beyond cross-finding-029's three named channels
because §2.3 shows exposure is itself phase-confounded. Adding a channel can only make the
worst-of-9 rule harder to pass.

**Entry 7 — permutation unit.** Surah, not token. Chosen because phase is a surah property.

**Entry 8 — the zero-demonstrative surahs.** 26 surahs excluded from the label pool. Their labels
cannot enter either statistic; the alternative was reviewed and rejected as adding null variance
with no exchangeability gain.

**Entry 9 — bin widths.** Quintiles and deciles, matching H-NEW-2960's precedent so the two lanes'
length controls are comparable. Both reported; the worst governs.

**Entry 10 — what was measured before locking.** §2.3's table, and nothing else. **No quantity
crossing deixis with chronology was computed before this file was written**, which is the only
pre-lock constraint that matters for the direction in §1.

**Entry 11 — Bonferroni denominator.** k = 2, reasoning fixed in §8 before any number exists.

**Entry 12 — reusing H-NEW-2960's partition rule rather than writing a fresh one.** A fresh rule
would be a second uncalibrated instrument; the existing one has a 0-disagreement cross-check. It
was independently re-executed and reproduces 330/729 exactly. Recorded as a dependency: **if
H-NEW-2960's rule is ever found wrong, this finding falls with it.**
