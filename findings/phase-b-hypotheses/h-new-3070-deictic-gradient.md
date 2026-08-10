---
title: "H-NEW-3070 — F-4's deictic gradient is not a gradient: the proximal/distal shift is a single Medinan step, it survives every length channel, and it is not formulaic"
author: Waiel Al-Shujaa
date: 2026-08-09
status: PASS on the locked rule — with the locked hypothesis's own SHAPE refuted post-hoc
frontier_item: F-4 (HANDOFF/FRONTIER-MAP-2026-08-07.md:254) — CLAUSE 2 ONLY
prior_work_on_this_item: findings/phase-b-hypotheses/h-new-2960-spatial-deixis.md
prereg_path: findings/phase-b-hypotheses/prereg-h-new-3070-deictic-gradient.md
prereg_sha256: 83bdecc61c8e82df366f05f1112121ff23678d17d0c6bf25c4e39955e9a17bee
script_path: findings/phase-b-hypotheses/scripts/h-new-3070.py
posthoc_script_path: findings/phase-b-hypotheses/scripts/h-new-3070-posthoc.py
posthoc2_script_path: findings/phase-b-hypotheses/scripts/h-new-3070-posthoc2.py
run_dir: findings/phase-b-hypotheses/runs/h-new-3070/20260809T075716Z
posthoc_run_dir: findings/phase-b-hypotheses/runs/h-new-3070-posthoc/20260809T075944Z
posthoc2_run_dir: findings/phase-b-hypotheses/runs/h-new-3070-posthoc2/20260809T080716Z
git_commit_at_lock: e7654b403ff161585154d7ade503868e37b909c1
method_parents:
  - findings/UNIT-DRIFT-DEFECT.md
  - findings/PROXY-CLAIMS.md
  - findings/TIED-OUTCOME-DEFECT.md
  - findings/phase-b-hypotheses/cross-finding-029-the-deciding-parameter.md
model_finding: findings/phase-b-hypotheses/h-new-3030-sajdah-glyph.md
---

# H-NEW-3070 — the deictic gradient across the Nöldeke phases

## 0. STEP-0 FIRST — most of F-4 was already answered, and this finding does not touch it

**F-4 clause 1 was executed by H-NEW-2960 on 2026-08-08 and returned NULL.** That lane's
front-matter names `frontier_item: F-4`. It is the **fifth** confirmed staleness case against the
frontier map, after F-3, F-5, F-8 and F-10, and the map's F-4 entry still carries no
answered-status pointer. Its census (1,059 = 330 proximal + 729 distal), its eschatological test
(OR 2.743, exact p = 0.0605 against α = 0.0167, **NULL**) and its formulae arms are **not
re-litigated, not replicated, and claimed as novelty by nothing below.**

**Clause 2 — "giving a measurable deictic gradient across the Nöldeke phases" — was never
touched.** `grep -niE "noldeke|chronolog|revelation-order|meccan|medinan|gradient"` returns **zero**
matches in both `h-new-2960-spatial-deixis.md` and its pre-registration; `data/revelation-order.csv`
is not opened by `scripts/h-new-2960.py`. **This finding covers clause 2 and nothing else.**

**A ledger gap, reported rather than fixed here: H-NEW-2960 has no entry in
`MASTER-FINDINGS-LEDGER.md`.** `grep -c 2960` returns 1, and that hit is an incidental mention
inside another finding's prose. A future lane obeying the map's own binding rule — grep the ledger
before designing — **would not find it.**

---

## 1. Verdict in one paragraph

**The locked rule returns PASS, and the locked hypothesis's stated shape is wrong.** Distal
demonstratives skew later in the Nöldeke sequence at **S1 = +0.532 phase units** (token level) and
**Spearman ρ = +0.381** (surah level), and both clear α = 0.025 **under the worst of nine length
settings** — p = 0.0029 and 0.0022, the worst channel being **mean verse length at decile
stratification** in both cases. **The map's CBM prior is refuted:** dropping the 17
muqaṭṭaʿāt-opening demonstratives changes nothing (p 0.0029 → 0.0024), and dropping **369 of 1,059
tokens — 34.8 % of the corpus's demonstratives, every muqaṭṭaʿāt opening, every *ka-dhālika*, and
every token of the ten most frequent phrase types** — leaves the effect size *larger* than the full
inventory's (S1 0.560 against 0.532) and still significant. **But the word "gradient" in F-4 is
wrong.** The phase profile is **not monotone** — Early Meccan 0.561, Middle Meccan **0.498**, Late
Meccan 0.677, Medinan 0.847 — and post-hoc, **with Medinan removed the effect dies at the worst
channel** (p = 0.118 / 0.178). What exists is **one step at the Meccan→Medinan boundary**, not a
gradient across four phases.

**Four things went against me and are reported at full prominence in §6:** one registered arm
fails, one rules-tuple fails, one of my own three justifications for the locked direction is
refuted by my own probe, and the design's power at the strictest control is marginal.

---

## 2. What was measured

| | |
|:--|--:|
| `POS:DEM` / `POS:LOC` / `POS:T` | **1,059 / 669 / 1,166** — all three of the map's figures, verified independently |
| distal / proximal (addressee-kāf rule) | **729 / 330** — reproduces H-NEW-2960 exactly |
| kāf-rule vs lemma-partition disagreements | **0** of 1,059 |
| surahs carrying ≥ 1 demonstrative | 88 of 114 |
| muqaṭṭaʿāt surahs derived from `POS:INL` | **29**, matching H-NEW-2960's derivation |
| permutations · seed | 10,000 · 20260509 |
| α, Bonferroni k = 2 | **0.025** |

QAC SHA-256 `a1d12923…5d8c46` — the same file H-NEW-2960 used, verified by hash in the manifest.
The census reproduction is an **independent third-party replication** of H-NEW-2960's headline
count and is reported as such and no more.

**Tie fraction of the per-surah distal share = 0.2273** (modal value 1.0, 20 surahs), stated in the
pre-registration before the run as [[TIED-OUTCOME-DEFECT]] §5 requires. Below the 50 % threshold,
so the exact-test trigger does not fire; a permutation null is used regardless. **In the run
itself, the fraction of null draws exactly equal to the observed statistic is 0.000000 across every
verdict-bearing cell**, with 7,517–9,804 distinct null values out of 10,000 draws. The defect is
absent by measurement, not by assumption.

---

## 3. The primary result, and the channel table that governs it

**H1** = mean phase ordinal of distal tokens − that of proximal tokens.
**H2** = Spearman ρ(phase ordinal, per-surah distal share) over the 88 surahs.
Both verdict-bearing; both units reported per [[UNIT-DRIFT-DEFECT]]; **the worst of nine length
settings governs**, per the brief's length-channel rule.

| setting | H1 p | H2 p |
|:--|--:|--:|
| L0 unstratified | 0.00010 | 0.00010 |
| L1 verse count · quintile / decile | 0.00010 / 0.00010 | 0.00040 / 0.00040 |
| L2 word count · quintile / decile | 0.00010 / 0.00010 | 0.00010 / 0.00010 |
| **L3 mean verse length · quintile** | 0.00200 | 0.00120 |
| **L3 mean verse length · decile** | **0.00290** ← worst | **0.00220** ← worst |
| L4 demonstrative count · quintile / decile | 0.00010 / 0.00010 | 0.00010 / 0.00020 |

> **The dominant channel is MEAN VERSE LENGTH, by a wide margin.** It is the only channel that
> moves either p-value off the permutation floor: a **29× swing on H1** (0.00010 → 0.00290) and
> **22× on H2**. Verse count, word count and demonstrative-count exposure do nothing at all.

**This is the third independent confirmation of the same channel ordering in this project.**
H-NEW-3010 saw a ~70× swing; the frontier map's own F-3 correction measured mean verse length at
ρ = +0.5467 against verse count at ρ = +0.0719. **Had I locked "residualise on surah length" a
priori — the phrasing the map uses — I would have reported p = 0.0001 and been reporting the wrong
number by a factor of 29.**

**Permutation freedom, computed not assumed.** L3 at decile is also the tightest stratification:
**7 of 10 strata are informative** (contain ≥ 2 distinct phase labels), covering 70.5 % of surahs.
Every other setting is 100 % informative. So the worst p comes from the control with the least
freedom, which is the expected and honest ordering — and it still clears α.

---

## 4. With and without the formulae — the decisive arm the brief named

| arm | tokens | H1 obs | H1 p worst | H2 obs | H2 p worst |
|:--|--:|--:|--:|--:|--:|
| **A0** full inventory | 1,059 | +0.532 | **0.0029** | +0.381 | **0.0022** |
| **A1** drop 17 muqaṭṭaʿāt openings | 1,042 | +0.540 | 0.0024 | +0.382 | 0.0023 |
| **A2** drop 126 *ka-dhālika* | 933 | **+0.605** | 0.0022 | **+0.410** | 0.0030 |
| **A3** drop 247 top-10 phrase-type tokens | 812 | +0.479 | **0.0292 FAILS** | +0.358 | 0.0154 |
| **A4** drop all of the above — 369 tokens | 690 | **+0.560** | 0.0154 | +0.380 | 0.0201 |

> **The map's prior — "the effect may be entirely carried by ~20 formulaic phrases" — is refuted.**
> Removing **34.8 % of every demonstrative in the corpus**, including all 17 opening formulae, all
> 126 *ka-dhālika*, and every token of the ten commonest phrase types, leaves H1's effect size
> **larger** than the full inventory's (+0.560 against +0.532) and H2's essentially unchanged
> (+0.380 against +0.381). **The p-values rise only because n falls from 1,059 to 690.**

**This is the second axis on which F-4's CBM prior has now failed, and the first failure is
H-NEW-2960's result, not mine.** On the eschatological axis **that lane** found the same signature
in the opposite direction from the map's prediction: its odds ratio *rose* from **2.74 to 3.00**
when the top ten phrase types were dropped, and to **4.19** when *ka-dhālika* was dropped. Two
lanes, two different tests, same answer: **the demonstrative signal in this corpus is not carried by
its frequent formulae.**

> **A prior that fails in the direction opposite to the one predicted is more informative than one
> that merely fails**, and the frontier map still records the wrong prior for F-4 — *"CONFIRMED but
> at risk of CBM: the effect may be entirely carried by ~20 formulaic phrases."* Two independent
> measurements now say the ~20 formulaic phrases are, if anything, **diluting** it.

**And the confound can reach this test, which it could not reach H-NEW-2960's.** There, 0 of the
17 openings were in the eligible set, so the deletion arm was vacuous. Here all 17 are inside the
test and **26 of the 29 muqaṭṭaʿāt surahs are Middle- or Late-Meccan** (16 Late, 10 Middle, 2
Medinan, 1 Early). **A1 is a real deletion that really changes the token set, and it changes
nothing.**

---

## 5. THE SHAPE IS WRONG — post-hoc, non-registered, and it is the most important thing here

Everything in this section is **post-hoc, was not pre-registered, and can only weaken the locked
verdict.** It does not change it. It changes what the verdict *means*.

### 5.1 The phase profile is not monotone

Distal share by phase, with surah-clustered bootstrap 95 % CIs (5,000 resamples):

| phase | tokens | distal share | CI 95 % |
|:--|--:|--:|:--|
| Early Meccan | 57 | 0.5614 | [0.4464, 0.6875] |
| **Middle Meccan** | 249 | **0.4980** | [0.4124, 0.5804] |
| Late Meccan | 381 | 0.6772 | [0.6229, 0.7491] |
| **Medinan** | 372 | **0.8468** | [0.8161, 0.8812] |

**Early → Middle runs the wrong way.** Only two of the three steps are separable at all: Middle vs
Late (CIs 0.5804 / 0.6229 — just clear of each other) and Late vs Medinan (0.7491 / 0.8161).

### 5.2 The three adjacent steps, tested

| step | H1 obs | H1 p worst | H2 obs | H2 p worst |
|:--|--:|--:|--:|--:|
| Early → Middle Meccan | **−0.038** | 0.907 | **−0.072** | 0.713 |
| Middle → Late Meccan | +0.179 | 0.032 | +0.437 | 0.055 |
| **Late Meccan → Medinan** | +0.233 | **0.0127** | +0.498 | **0.0040** |

**Only the Meccan→Medinan step survives.** The first step is *negative* on both units.

### 5.3 Delete Medinan and the effect dies

| Meccan-only (Early + Middle + Late, 687 tokens, 65 surahs) | value |
|:--|--:|
| H1 observed | +0.187 |
| H1 p — **best** channel (L4 quintile) | 0.0023 |
| H1 p — **worst** channel (L3 decile) | **0.1176** |
| H2 p — best / **worst** | 0.0147 / **0.1782** |

> **A 51× p-swing across length channels on H1, and the worst channel fails.** Within Mecca there
> is no deictic trend that survives a mean-verse-length control. **F-4's "gradient across the
> Nöldeke phases" does not exist. What exists is a step change at the Meccan/Medinan boundary.**

**And this NULL is well powered, which is what makes it usable.** This finding's headline rests on
an absence, so per [[cross-finding-029]] §3.2 the absence carries an MDE
(`runs/h-new-3070-posthoc2/20260809T080716Z`):

| Meccan-only NULL — power audit | value |
|:--|--:|
| S\* — critical value at the worst channel | 0.2190 |
| S_max attainable | 0.5714 |
| **UNTESTABLE-AT-THIS-N branch** | **did not fire** |
| **MDE at 80 % power (simulated)** | **0.2609** |
| power against a 0.25-phase-unit effect | **0.737** (H1) / **0.835** (H2) |
| observed | +0.1869 — **below S\*** |

> **The Meccan-internal design could have detected an effect half the size of the one the whole
> corpus shows (MDE 0.261 against the full-corpus 0.532), and it did not.** At a quarter-phase-unit
> effect it had 74–84 % power. **This is a strong NULL, not an underpowered one** — *could not have
> detected* does not apply here, and that had to be computed to be known. Any real within-Mecca
> trend is smaller than 0.26 phase units.

Consistently, the binary rules-tuple **R4 (Meccan / Medinan) passes strongly** — H1 p_worst
0.0011, H2 0.0101 — while the fine-grained **R2 (Egyptian-standard revelation-order rank) fails**
(§6.2). A binary contrast beating a 114-point rank ordering is the signature of one step, not a
slope.

### 5.4 The mechanism, descriptively

Lemma counts by phase (Early / Middle / Late / Medinan):

| lemma | E | M | L | Med |
|:--|--:|--:|--:|--:|
| `dhālik` (distal) | 26 | 101 | 193 | 200 |
| `ulāʾik` (distal) | 6 | 22 | 62 | 114 |
| **`hādhā` (proximal)** | 24 | 122 | 122 | **49** |

**The Medinan step is driven as much by the collapse of proximal *hādhā* as by distal growth.**
*hādhā* is flat at 122 across Middle and Late Meccan and falls to 49 in Medinan — while the corpus
mass rises. The Meccan polemical *mā hādhā illā…* deixis, pointing at the contested present
recitation, is a Meccan-register form that Medinan largely drops.

---

## 6. What went against me — at full prominence

### 6.1 One registered arm FAILS

**A3 (drop the top-10 phrase types) returns H1 p_worst = 0.0292 > α = 0.025.** It is not in the
locked decision rule — §8 gates CONFIRMED-BUT-FORMULAIC on A1 and A4 only, fixed before the run —
so the verdict is unaffected. **Reporting it anyway is the point.** The non-monotonicity is real
and odd: A3 fails while A4, which drops *strictly more* tokens (369 against 247), passes at 0.0154.
The explanation is visible in the table: A2 shows that dropping *ka-dhālika* **strengthens** the
effect, so A4 = A3 + a strengthening deletion. **It remains the case that one of my five registered
arms did not clear the gate.**

### 6.2 One rules-tuple FAILS

| tuple | H1 obs | H1 p worst | H2 obs | H2 p worst | |
|:--|--:|--:|--:|--:|:--|
| **R1** Nöldeke phase × kāf (PRIMARY) | +0.532 | 0.0029 | +0.381 | 0.0022 | PASS |
| **R2** Egyptian revelation order × kāf | +12.558 | **0.0299** | +0.308 | **0.0738** | **FAILS BOTH** |
| R3 Nöldeke phase × lemma partition | +0.532 | 0.0029 | +0.381 | 0.0022 | PASS |
| R4 Meccan/Medinan binary × kāf | +0.268 | 0.0011 | +0.382 | 0.0101 | PASS |

> **The result is chronology-instrument dependent.** Under the Tanzil/Egyptian-standard revelation
> order — a perfectly respectable chronology, and the one carried by the same file that 87 scripts
> in this repository read (measured, `grep -rl`) — **the
> effect fails at α = 0.025 on both hypotheses.** §5 explains why (a 114-point rank test is diluted
> when the true structure is a single binary step, and the two chronologies disagree on 4 surahs'
> Medinan status), but an explanation is not a rescue. **A reader who prefers the Egyptian standard
> to Nöldeke should read this finding as NULL.**

**And R3 is not corroboration.** It returns numbers *identical to R1 to five decimals* because the
kāf rule and the lemma partition agree on all 1,059 tokens — it is the same function twice, not an
independent check. Presenting it as a third passing tuple would be padding, and it is withdrawn as
evidence.

### 6.3 One of my own justifications for the locked direction is REFUTED

Pre-registration §1.1 anchor 3 justified the upward lock partly on the *ulāʾika* group-verdict
formula (*ulāʾika humu / lladhīna / aṣḥābu*, 107 tokens) as the distal's dominant communal-legal
use. **Post-hoc, dropping all 206 `ulāʾik` tokens leaves the effect essentially untouched** — H1
+0.447 at p_worst 0.0037, H2 **+0.38212 against the full inventory's +0.38112**, a difference in
the fourth decimal.

> **The direction I locked was right and the reason I gave for locking it was wrong.** A stated
> mechanism that survives deletion of its own carrier is not the mechanism. §5.4's *hādhā*-collapse
> is a better candidate and is descriptive only — it was not registered and carries no p-value.

*(`ulāʾika` is 100 % distal by construction — all 206 tokens carry the addressee-kāf — so the
converse probe on that lemma alone is undefined, and is reported as undefined rather than dropped.)*

### 6.4 Power at the strictest control is marginal

Computed per pre-registration §9 although the verdict is PASS, not NULL:

| quantity | worst channel (L3 decile) | L0 unstratified |
|:--|--:|--:|
| S\* — critical value at α = 0.025 | 0.4956 | 0.2756 |
| S_max attainable given marginals | 1.0531 | 1.0531 |
| **UNTESTABLE-AT-THIS-N branch** | **did not fire** | did not fire |
| MDE at 80 % power (simulated) | **0.5359** | 0.3235 |
| power against a 0.25-phase-unit effect | **0.000** (H1) / 0.149 (H2) | 0.348 / 0.540 |

> **The observed S1 = 0.5318 sits essentially ON the 80 %-power threshold of 0.5359 at the worst
> channel.** The design is adequately powered for the effect it found and **has near-zero power
> against a quarter-phase-unit effect** under that control. A smaller true effect of the same sign
> would have been missed. The untestable branch was computed and did not fire, per H-NEW-3030's
> precedent — that distinction had to be computed to be known.

**Limit on the power block itself:** the simulation assumes P(distal) is **linear in phase**, and
§5.1 shows the real profile is not. The MDE is therefore an estimate under a model the data
violates, and is reported as an approximation rather than an exact figure.

### 6.5 I predicted the dominant channel correctly and FAILED TO PRE-REGISTER THE PREDICTION

Before the pre-registration was written and before any statistic was computed, I stated in writing
that I expected **mean verse length** to dominate, reasoning from the frontier map's F-3 correction
(mean verse length ρ = +0.5467 against verse count ρ = +0.0719). §3 shows that is exactly what
happened — 29× on H1, 22× on H2, with the other three channels doing nothing.

**That prediction is not in the pre-registration.** §5 of the prereg says only *"No channel is
locked a priori"* and never names which channel I expected to win. `grep -niE "dominant|expect|
predict"` over the prereg confirms it: the word does not appear in that sense anywhere.

> **So this is a correct prediction with weak evidential standing, and it is reported as such.**
> It was made prospectively and in writing, but not in the artefact that exists to make predictions
> binding. **A prediction recorded outside the pre-registration is a claim about my memory, not a
> lock.** I am not counting it as a confirmed hypothesis; the channel result stands on its own as a
> measurement, and the third-time-in-a-row concordance with H-NEW-3010 and the F-3 correction is
> what carries weight, not my having said so first.

**The pre-registration is NOT being amended to add it.** [[feedback_prereg_immutability]] forbids
editing a pre-registration after its run, and the SHA lock in the script would break if I did —
which is the mechanism working as designed. The gap is recorded here instead.

### 6.6 My own power block is INVALID for rules-tuple R2, and I caught it from its own output

The post-hoc power audit was run for both published NULLs. For R2 it returned
`MDE = nan` and `power against a 0.25-unit effect = 0.000`. **Those numbers are meaningless and are
withdrawn.** `power_block`'s MDE bisection searches δ ∈ [0, 3] and its reference effect is 0.25 —
both hard-coded for the **4-point phase ordinal**. R2's statistic lives on the **114-point
revelation-order rank** (observed S1 = 12.56, S\* = 12.69, S_max = 30.80), where 3.0 is a trivially
small effect and the search can never reach 80 % power. **The routine silently returned a
well-formed number on the wrong scale** — the exact failure shape [[cross-finding-029]] §2 names.

**The N1 Meccan-only power block in §5.3 is unaffected and valid**: it uses the same 1–3 phase
ordinal, its MDE of 0.2609 sits well inside the search range, and S_max = 0.5714 confirms the scale.
**R2's failure is therefore reported without a power statement**, and §6.2's conclusion — that the
result is chronology-instrument dependent — rests on its p-values, which are computed by permutation
and are unaffected by this defect.

---

## 7. Honest limits

1. **The headline claim is narrower than F-4.** What survives is *Medinan demonstratives are more
   distal than Meccan ones* (0.847 against ~0.60), robust to four length channels at two bin widths
   and to deleting a third of the tokens. **That is not "a deictic gradient across the Nöldeke
   phases."**
2. **Adjacency to `cross-finding-028-formal`, and it is worse than mere correlation.** cf-028 codes
   register at the *person*-deixis grain (iltifāt, 1↔2↔3); this is *spatial* deixis, a different
   axis on the same corpus — but the register it separates (legal-Medinan) is the same one cf-028
   separates. `findings/AUDIT-REGISTER-PHASE-COLLINEARITY.md` (2026-08-09, a parallel lane, read
   after this run) shows the two are **not separable even in principle for a large part of the
   corpus**: the legal register is **0 Meccan / 15 Medinan** and narrative is **26 Meccan / 0
   Medinan**, so **49 of 115 surahs (43 %) sit in a register occurring in exactly one phase**, and a
   register-stratified permutation against phase has *nothing to permute* in those strata.
   **"Is this deictic step independent of register?" is therefore not answerable by stratification**,
   and I am not claiming it is. What this finding measures is the *phase* contrast; how much of it
   is the legal register wearing a chronology label is **open and, for those 49 surahs, structurally
   unanswerable.** That audit also independently corroborates §5's reading — legal *is* Medinan is
   "the substantive content of the periodisation itself," which is precisely why a step and not a
   gradient is what turns up.
3. **Referent is not measured.** As in H-NEW-2960 §3.1: the referent of a demonstrative is a
   discourse entity needing a dependency parse with coreference, and `data/syntax/` holds one
   1,754-byte README and no treebank. **This finding measures where distal *forms* occur, never
   what they point at.** F-4's clause about *scripture-as-object* is therefore untested by this
   work as well as by H-NEW-2960.
4. **Chronology is an inherited hypothesis, not data.** Nöldeke's four-phase scheme is a
   19th-century reconstruction. §6.2 shows the verdict moves when it is swapped. Every result here
   is conditional on it.
5. **This finding inherits H-NEW-2960's partition rule.** If that rule is ever found wrong, this
   falls with it. Recorded as a dependency in the pre-registration's forking-paths log entry 12.
6. **`hunālika` and `thamma` are outside `POS:DEM`** (H-NEW-2960 §1.5) and outside this object too.
   The deictic field is wider than the category counted.

---

## 8. What this settles, and what it queues

**Settled:**
- **F-4 clause 2 is answered, and F-4's own word for it is wrong.** The shift is a Medinan **step**
  (p_worst 0.0029 / 0.0022 under R1), not a gradient: with Medinan removed the Meccan-internal
  effect fails at 0.118 / 0.178, and the Early→Middle step is *negative*.
- **Mean verse length is the dominant length channel**, 29× on H1 and 22× on H2 — a third
  independent confirmation of the [[cross-finding-029]] rule, and the only channel that matters.
- **The CBM prior fails on this axis too.** 369 of 1,059 tokens deleted; effect size unchanged.
- **The census replicates independently**: 1,059 = 330 + 729, 0 kāf-vs-lemma disagreements.
- **The result is chronology-instrument dependent** and fails under the Egyptian standard.

**Queued (each needs its own prospective pre-registration):**
- **H-NEW-3071** — the *hādhā*-collapse of §5.4 as its own hypothesis: is the Meccan polemical
  proximal a register marker in its own right, tested against the legal/narrative labels rather
  than against chronology?
- **H-NEW-3072** — spatial deixis and person deixis (cf-028's iltifāt) entered jointly. **Note the
  constraint before designing it:** per `AUDIT-REGISTER-PHASE-COLLINEARITY.md` §3 a
  register-stratified test against phase is degenerate for 43 % of the corpus, so the two honest
  designs are **ablation** (drop the collinear registers, test on the ~66 informative surahs, report
  the reduced n *and its MDE*) or **reframe** (accept register and phase are partly one variable and
  stop claiming to separate them). The stratified-and-report-a-number route is not available.
- **The frontier map needs F-4 marked PARTIALLY ANSWERED**, and `MASTER-FINDINGS-LEDGER.md` needs
  an H-NEW-2960 entry — the trap in §0 is live for the next lane.

---

## Sources

- `data/morphology/quranic-corpus-morphology-0.4.txt` — QAC v0.4, SHA-256 `a1d12923…5d8c46`.
- `data/revelation-order.csv` — SHA-256 `74f52ec1…16fb7`, 114 rows, complete, no blanks.
- Pre-registration `prereg-h-new-3070-deictic-gradient.md`, SHA-256 `83bdecc6…7bee`, embedded in
  the script and verified at runtime before the run directory was created.
- Run `runs/h-new-3070/20260809T075716Z/{result,manifest}.json`; post-hoc
  `runs/h-new-3070-posthoc/20260809T075944Z/`; power audit of the published NULLs
  `runs/h-new-3070-posthoc2/20260809T080716Z/`. **None deleted.**
- Prior work, not re-litigated: `h-new-2960-spatial-deixis.md`.
- Method: `UNIT-DRIFT-DEFECT.md`, `PROXY-CLAIMS.md`, `TIED-OUTCOME-DEFECT.md`,
  `cross-finding-029-the-deciding-parameter.md`. Model: `h-new-3030-sajdah-glyph.md`.
- Constraint on limit 2 and on H-NEW-3072, from a parallel lane and read after this run:
  `findings/AUDIT-REGISTER-PHASE-COLLINEARITY.md` (2026-08-09).
