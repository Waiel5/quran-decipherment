---
title: "H-NEW-3120 — F-12's asbāb instrument is a scrape boundary, and the length control that kills the textual test is 0.906 collinear with the thing being tested"
author: Waiel Al-Shujaa
date: 2026-08-09
status: NULL on the locked rule — with the instrument audit as the substantive result, and a control-collinearity finding that generalises beyond this lane
frontier_item: F-12 (HANDOFF/FRONTIER-MAP-2026-08-07.md)
prereg_path: findings/phase-b-hypotheses/prereg-h-new-3120-asbab-chronology.md
prereg_sha256: bede8fc660467763a26e1068ec2d0a3dce044491c1da9c1f6718837210539caa
script_path: findings/phase-b-hypotheses/scripts/h-new-3120.py
posthoc_script_path: findings/phase-b-hypotheses/scripts/h-new-3120-posthoc.py
run_dir: findings/phase-b-hypotheses/runs/h-new-3120/20260809T090141Z
posthoc_run_dir: findings/phase-b-hypotheses/runs/h-new-3120-posthoc/20260809T090419Z
qac_sha256: a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46
method_parents:
  - findings/ABSENCE-CLAIMS.md
  - findings/PROXY-CLAIMS.md
  - findings/UNIT-DRIFT-DEFECT.md
  - findings/TIED-OUTCOME-DEFECT.md
  - findings/AUDIT-H-NEW-206-LENGTH-CONFOUND.md
  - findings/phase-b-hypotheses/cross-finding-029-the-deciding-parameter.md
bears_on: findings/phase-b-hypotheses/h-new-3070-deictic-gradient.md
---

# H-NEW-3120 — F-12, asbāb al-nuzūl as a chronology instrument

## 1. Verdict in one paragraph

**Asbāb coverage is a LENGTH instrument, not a chronology instrument — and that is true even after
the artefact is removed.** Mean verse length beats chronology in both windows: **+0.8206 against
+0.7350** with the truncation present, **+0.6394 against +0.5774** inside the clean window 1–77.
F-12 proposed to measure chronology; what its variable actually tracks is how long the verses are.
Separately and additionally, the variable is unusable at all, because the only asbāb source on disk
**stops at surah 77** (the 37 absent surahs being 35/37 Early Meccan), so coverage *is* the
indicator `surah ≤ 77` and returns **ρ = +0.7350 at p = 1.29×10⁻²⁰** — a spectacular measurement of
where a scraper stopped. **The artefact-free substitute — the text's own retrospective particle
*ʾiḏ* against chronology — returns NULL on the locked rule**: H1 +0.0363 at p_worst 0.2541,
H2 ρ = +0.4718 at p_worst 0.7023, both correct-signed, both failing α = 0.025 at the
mean-verse-length control. **And the most useful thing here is why.** That control is
**ρ = +0.9058 collinear with the Nöldeke phase ordinal itself**, and the p-value rises
*monotonically* with how closely the control duplicates the treatment (0.000→0.0002, 0.357→0.0004,
0.677→0.0022, 0.906→0.2541). **At surah level in this corpus, "mean verse length" and
"chronological phase" are very nearly the same variable, so the standing "worst length channel
governs" rule will return NULL for any chronological hypothesis whether or not it is true.**
Measured, new, and §6 states exactly what it does and does not license.

> **Relation to what is already committed.** The truncation, the blend, the tuple non-independence
> and the truncation-confound collinearity are recorded in
> [[AUDIT-TWO-BLOCKED-INSTRUMENTS-2026-08-10]] Part II (commit 329) and the
> `HANDOFF/CONTINUE-PROMPT.md:225` annotation. **They are summarised here, not re-derived.** What is
> new in this file and in neither of those: **the length-instrument channel table (§3.3), the
> generalised zero-entry method (§3.1.1), the whole of Arm A (§4–5), and the control-collinearity
> result (§6).**

---

## 2. Step 0 — what already existed

The brief required the grep before design, and it changed the design.

**Prior asbāb work:** `findings/phase-b-hypotheses/asbab-nuzul.md` (2026-04-12), status
`exploratory`, which says of itself *"No pre-registered null was defined for sabab-attribution
itself."* Treated as hypotheses, not data. **One of its numbers is refuted below (§7.4).**

**Prior chronology-instrument work, none on coverage:** `h-new-125`, `h-new-212`/`h-new-222`
(⛔ pillar-2 correction), `h-new-46.1`, `h-new-2350`, `h-new-267`, `h-new-224`, `h-new-229`.
Ledger §274's **MW-2 domain split** places a lexical-content channel like *ʾiḏ* on the side where
Nöldeke chronology is a real axis. **`PROXY-CLAIMS.md:192`: ρ(Nöldeke, Egyptian) = +0.7714** — so
the two chronology instruments used here as rules-tuples are **not independent**, and are not
presented as such.

**F-12's specific question is unasked anywhere — and it is instrument-blocked.**

---

## 3. THE INSTRUMENT AUDIT — the substantive result

### 3.1 The source is truncated at surah 77

`data/literature/classical-tafsir/spa5k-tafsir-api/en-asbab-al-nuzul-by-al-wahidi/` holds
**surahs 1..77 exactly, gapless**, and nothing from 78..114. The absent block is **34 Meccan /
3 Medinan**, by Nöldeke phase **35 Early Meccan / 2 Medinan**.

**Two distinct absence-encodings coexist in the directory, and that is the proof:**

| encoding | instances | meaning |
|:--|:--|:--|
| file present, **zero entries** | **Q 72, Q 77** | the source says "no occasion here" |
| **file absent entirely** | **Q 78–114** | ingestion never reached it |

If al-Wāḥidī genuinely carried nothing for juzʾ 30 we would see 37 more zero-entry files, exactly
like Q 72 and Q 77. Coverage inside the block is **sparse and scattered — 1,089 entries against
5,672 verses = 19%**, Q 2 at 0.45 down to Q 67 at 0.07, only Q 1 complete. **Selectivity is
expressed at verse level throughout; a contiguous gapless surah-level cut on top of it is an
ingestion boundary, not an editorial judgement.**

**Comparator control:** `en-al-jalalayn`, `ar-tafsir-ibn-kathir`, `en-tafsir-ibn-abbas` each carry
**114 surah-level `.json` files**; the asbāb edition carries **77**. *(Counting note, because the
same fact appears in two units across the record: the committed audit and the CONTINUE-PROMPT
annotation state "**228 files each; this one has 152**", counting all top-level entries — 114 JSON
+ 114 per-verse directories, against 77 + 75. Both counts are correct and describe the same tree.
Stated explicitly so the two numbers are not read as a discrepancy.)*

**Absence claim with its search stated, per [[ABSENCE-CLAIMS]]:** `find` repo-wide (excluding
`.git`, `.claude/worktrees`) for `*asbab* *wahidi* *nuzul* *lubab* *wahidy* *waahid*` returns 5
hits, all accounted for; `editions.json` (27 editions) holds exactly one asbāb edition, id 86,
source altafsir.com. **No al-Wāḥidī coverage of surahs 78–114 exists on disk.**

### 3.1.1 THE TRANSFERABLE METHOD — when silence has a representation, check which silence you have

The generalisable part of §3.1 is not a fact about al-Wāḥidī. It is a discharge procedure for
absence claims, and it is stronger than the argument from silence that [[ABSENCE-CLAIMS]] warns
against.

> **A dataset that can represent "this unit has no value" gives you two distinguishable silences.
> Find out whether the format has such a representation, then check which one your gap is.**

| silence | how it appears here | what it means |
|:--|:--|:--|
| **encoded absence** | Q 72, Q 77 — file present, zero entries | the source says "nothing here" |
| **structural absence** | Q 78–114 — no file at all | the pipeline never reached it |

**The presence of the first kind is what makes the second kind evidential.** Had every surah with
no sabab simply been missing, the two would be indistinguishable and the truncation would be a
conjecture. Because Q 72 and Q 77 exist *and are empty*, the format demonstrably can say "no
occasion here" — so 37 consecutive files that do not exist are not the source's silence.

**Two supporting checks make it airtight, and both generalise:**

1. **A sibling control in the same tree** — three other editions carry all 114, so the gap is
   edition-specific, not an artefact of the format or the scrape as a whole.
2. **Selectivity at a finer grain** — coverage inside the block is scattered at 19% (1,089/5,672),
   from 0.45 to 0.07. **A gapless cut at the coarse grain sitting on top of scattered selectivity
   at the fine grain is an ingestion boundary**, because a genuine editorial pattern would be
   scattered at both.

**The screen, for reuse:** *does the format encode a null? · is there an instance of the encoded
null? · is my gap that, or is it missing structure? · does a sibling dataset in the same tree have
what mine lacks? · is selectivity at the finer grain scattered while the coarse cut is contiguous?*
Any dataset with per-unit records supports this test, and it costs one `ls` and one count.

### 3.2 The source is a blend — independently re-verified, not inherited

`PROXY-CLAIMS.md:384-486` established this directory is **al-Wāḥidī 28% + a Persian Sufi commentary
72%** (Maybudī on style), refuted by *Shaykh al-Islām Anṣārī* (d. 481) quoted at `20/5` when
al-Wāḥidī died 468. **Re-classified here independently:** of 1,089 non-empty entries, **353 (32.4%)
carry al-Wāḥidī isnād/revelation formulae, 393 (36.1%) the Sufi register, 2 both, 341 (31.3%)
neither → ambiguous fraction 31.5%.** My classifier is the more permissive of the two; both agree
the directory is a blend. **All 7 verses of Q 1 are the Sufi text.**

### 3.3 Coverage is a LENGTH instrument — the channel table

Per-surah coverage rate, Spearman. Three length variables, none locked.

| channel | naive F-12 (all 114, absent = 0) | clean window 1–77 |
|:--|--:|--:|
| verse count | +0.4995 | **−0.0678** |
| word count | +0.7244 | +0.2571 |
| **mean verse length** | **+0.8206** | **+0.6394** |
| Nöldeke phase ordinal | +0.7350 | +0.5774 |
| **Egyptian standard rank** | **+0.5187** | **+0.3944** |
| Medinan binary | +0.4984 | +0.5472 |
| **mushaf index** | **−0.7665** | −0.3237 |
| tie fraction | **0.3772** | 0.0779 |

**THIS IS THE HEADLINE, not a footnote to the truncation.** Mean verse length beats chronology in
**both** windows — +0.8206 vs +0.7350 naive, +0.6394 vs +0.5774 clean. **Remove the artefact
entirely and the thing F-12 proposed to measure is still better explained by how long the verses
are than by when they were revealed.** The hypothesis is not merely blocked; its construct is
mis-specified.

**And verse count — the channel almost everyone means by "surah length" — is the weakest in both
windows and is nothing at all in the clean window (−0.0678).** That ordering is now confirmed four
times independently in this project:

| # | finding | evidence for the ordering |
|--:|:--|:--|
| 1 | `h-new-3010-conditional-register` | ~70× p-swing between length channels |
| 2 | `h-new-3070-deictic-gradient` §3 | 29× on H1, 22× on H2; mean verse length the only channel to move either off the permutation floor |
| 3 | F-3 correction (frontier map) | mean verse length ρ = +0.5467 against verse count ρ = +0.0719 |
| 4 | **this finding** | **1,270× on H1, 7,024× on H2** (§4.1); and on the coverage channel the two disagree in *sign* |

> **Four independent confirmations is where a pattern stops being an observation and becomes a
> property of the corpus.** §6 supplies the mechanism that was missing from the first three:
> mean verse length dominates because it is **ρ = +0.906 collinear with chronological phase**.

The naive instrument's tie fraction of 0.3772 is 37 surahs tied at exactly zero — the 37 never
ingested. **ρ(coverage, mushaf index) = −0.7665 is the scrape boundary showing through.**

> These p-values are **parametric** Spearman p's on an outcome that is 37.7% tied. Per
> [[TIED-OUTCOME-DEFECT]] they are liberal by 13–57× and are quoted as descriptive only. Nothing
> in §3 carries a verdict.

### 3.4 The circularity named in the brief, quantified

| | value |
|:--|--:|
| covered verse entries: Medinan / Meccan | 536 / 553 |
| **fraction of covered verses Medinan** | **0.4922** |
| corpus baseline Medinan verse share | 0.2603 |
| **enrichment** | **1.89×** |
| **enrichment within the clean window 1–77** | **1.74×** |

**The confound survives removal of the truncation.** Instrument and outcome share the construct —
the [[AUDIT-H-NEW-206-LENGTH-CONFOUND]] defect. Worse: on this data the two cannot be separated,
because "the tradition attends to Medinan legal verses" and "the scraper stopped at 77" are the
same variable.

---

## 4. ARM A — the pre-registered test, and it is NULL

**Channel:** QAC `LEM:<i*` — the particle *ʾiḏ*, **239 segments, POS:T for all 239**, surface forms
`<i*o` 224 / `<i*i` 12 / `<i*` 3. The distinct lemma `<i*aA` (*ʾiḏā*, 409) is excluded **by lemma,
not by string**, which is why this count is trustworthy where a string match is not (§7.4).

**Tie fraction of per-surah density = 0.5965 — above the 0.50 gate, so the exact trigger fires.**
Only 50 of 114 surahs carry any *ʾiḏ*. The design already uses a permutation null throughout, which
is [[TIED-OUTCOME-DEFECT]] §3's prescribed remedy; **no parametric p is verdict-bearing anywhere in
Arm A.**

### 4.0 Which side of the MW-2 domain split this outcome sits on — declared, and then complicated

Ledger §274 records the **MW-2 domain split**: Nöldeke chronology is a **hidden-axis pseudo-confound**
on structural/geometric axes (R-002 Fiedler, R-004 geometric-inversion, R-010 canonical-order
recovery) but a **genuine axis** on lexical-content axes, the anchor case being the kitāb/qurʾān
shift at z = −3.75. **Which side an outcome sits on decides whether a chronology correlation is
informative or circular**, so it is declared before the result.

**Declaration: *ʾiḏ* density is a LEXICAL-CONTENT axis — the genuine side.** Justification, three
points, none of which is "it is made of words":

1. **The unit is a lexeme, not a geometry.** The measurement is the count of one QAC lemma. It
   involves no distance matrix, no eigenvector, no ordering of surahs, and no adjacency — the three
   structural constructs on which MW-2 found chronology to be a pseudo-confound.
2. **It is the same *kind* of object as the anchor case.** kitāb/qurʾān is a two-lexeme frequency
   contrast across phase; *ʾiḏ* is a one-lexeme frequency measure across phase. If the split holds
   anywhere it holds here.
3. **It is not derived from any ordering.** A pseudo-confound arises on axes that are themselves
   computed from surah order or from a similarity structure that encodes it. *ʾiḏ* counts are
   invariant to how the surahs are arranged.

**So a chronology correlation here would have been informative, and it is on that basis that the
NULL is reported as a real result rather than a foregone one.**

> **But this finding complicates the MW-2 split rather than simply sitting inside it, and that
> should be recorded.** §6 measures **ρ(mean verse length, Nöldeke phase ordinal) = +0.9058**. Mean
> verse length is a *structural* property of a surah. If phase and a structural quantity are that
> nearly the same variable at surah level, then the clean partition of axes into
> "structural = pseudo-confound" and "lexical-content = genuine" is **not clean at the surah unit** —
> a lexical-content correlation with phase is also, to within ρ = 0.906, a correlation with a
> structural quantity. **This does not refute MW-2** (its anchor case, kitāb/qurʾān, was established
> at z = −3.75 and nothing here touches it, and MW-2's own claim is about which axes carry a
> *spurious* chronology signal). **It does mean the split cannot be applied at surah granularity
> without reporting the collinearity**, and I have not tested whether the kitāb/qurʾān result
> survives a mean-verse-length control. **That is a live, cheap, and currently unasked question**,
> and it is flagged rather than answered here.

### 4.1 The channel table — and both chronology instruments

| setting | R1 Nöldeke H1 p | R1 H2 p | R2 Egyptian H1 p | R2 H2 p |
|:--|--:|--:|--:|--:|
| L0 unstratified | 0.0002 | 0.0001 | 0.0010 | 0.0017 |
| L1 verse count · quintile | 0.0004 | 0.0004 | 0.0016 | 0.0634 |
| L1 verse count · decile | 0.0007 | 0.0009 | 0.0043 | 0.1086 |
| L2 word count · quintile | 0.0022 | 0.2018 | 0.0118 | 0.4608 |
| L2 word count · decile | 0.0044 | 0.2118 | 0.0193 | 0.5226 |
| **L3 mean verse length · quintile** | **0.2541** ← worst H1 | 0.5397 | **0.4884** | 0.9164 |
| **L3 mean verse length · decile** | 0.2397 | **0.7023** ← worst H2 | 0.4100 | 0.8666 |

H1 obs **+0.0363**, H2 obs **ρ = +0.4718** — both correct-signed, both failing α = 0.025.

**VERDICT: NULL.** Neither hypothesis clears its clause at the worst channel.

**S3 confirmed — the Egyptian standard is weaker at every single setting**, replicating
H-NEW-3070 §6.2's instrument-dependence on an independent channel. The two chronologies disagree on
the Medinan status of exactly **4 surahs: Q 13, Q 55, Q 76, Q 99.**

**The swing is the largest recorded in this project: H1 0.0002 → 0.2541 = 1,271×; H2 0.0001 →
0.7023 = 7,024×.** H-NEW-3010 saw ~70×, H-NEW-3070 saw 29×. **Verse count does almost nothing
(0.0002 → 0.0004).** Anyone locking "control for surah length" as verse count — the frontier map's
own phrasing — would have published p = 0.0004 and a confirmed chronology finding.

### 4.2 Unit check, per [[UNIT-DRIFT-DEFECT]]

| unit | value |
|:--|--:|
| **U1 token-level** — mean Nöldeke phase ordinal of the 239 *ʾiḏ* tokens | **2.0669** |
| mean phase ordinal of all verses | 1.5393 |
| **difference** | **+0.5277** |
| **H1/H2 surah-level** (verdict-bearing) | NULL at worst channel |

The token-level statistic is strongly later-shifted; the surah-level one does not survive the
control. **Reporting only the token-level number would have been the unit-drift defect exactly.**

### 4.3 Phase profile — descriptive

| phase | surahs | *ʾiḏ* tokens | verses | tokens/verse | mean surah density |
|:--|--:|--:|--:|--:|--:|
| Early Meccan | 48 | 13 | 1,219 | 0.0107 | 0.0064 |
| Middle Meccan | 21 | 63 | 1,898 | 0.0332 | 0.0263 |
| Late Meccan | 21 | 58 | 1,656 | 0.0350 | 0.0324 |
| **Medinan** | 24 | 105 | 1,463 | **0.0718** | **0.0534** |

**Monotone across all four phases** — unlike H-NEW-3070's deictic profile, which reversed at
Middle Meccan. So on the raw profile this channel looks like a *gradient*, not a step. It does not
survive the control either way.

---

## 5. THE SHAPE VERDICT IS "STEP-REPLICATED" AND IT SHOULD NOT BE BELIEVED

The locked rule returns **STEP-REPLICATED** (S1 true, S2 true). **Both legs are hollow and I am
reporting that rather than the label.**

- **S1 (binary beats rank) is true — but it compares two failing p-values.** 0.2541 < 0.7023 is a
  comparison between two tests that detected nothing. It carries no evidence about shape.
- **S2 (Meccan-internal null) is true but UNDERPOWERED**, which the corrected power audit
  (§5.1) establishes and the locked run's own routine got wrong.

**The shape prediction is therefore untested, not confirmed.** §4.3's monotone profile mildly
favours *gradient* over *step* on this channel, in the opposite direction to the locked shape
label. **I am not claiming that either; the design cannot separate them.**

### 5.1 The power audit — and the locked run's MDE was wrong

The locked run returned **MDE 0.0351 < observed 0.0363 < critical 0.0457**, which cannot all be
true of one design: a shift smaller than the observed effect cannot have 80% power in a test the
observed effect failed. **The cause was mine:** the MDE routine built synthetic datasets by
permuting density *globally*, destroying the density-by-stratum association and producing a
too-tight synthetic null. **Corrected in a separate post-hoc run — the locked run is retained
untouched, per standing rule 2 — by permuting WITHIN strata.**

| | H1 full corpus | H1m Meccan-internal |
|:--|--:|--:|
| worst channel | L3 mvl quintile | L3 mvl decile |
| observed | +0.0363 | +0.0200 |
| critical value | 0.0458 | 0.0290 |
| **obs / crit** | **0.793** | **0.689** |
| s_max attainable | 0.0782 | 0.0546 |
| **UNTESTABLE branch** | **did not fire** | **did not fire** |
| **MDE at 80% power (corrected)** | **0.040** | **0.085** |
| power at δ = 0.03 / 0.04 | 0.523 / 0.803 | 0.058 / 0.083 |

**The full-corpus NULL is marginal, not decisive** — MDE 0.040 against an observed 0.0363, roughly
70% power at the observed effect size. **The Meccan-internal NULL is weak: its MDE of 0.085 is
2.3× the whole corpus's Meccan-vs-Medinan effect (0.0363) and above its own maximum attainable
statistic (0.0546).** Its power curve is also non-monotone (0.237 at δ=0.05, 0.230 at 0.06, 1.000
at 0.09), reflecting instability from decile-stratifying 90 surahs. **"No Meccan-internal gradient"
is not a claim this design can make.**

> **Contrast with H-NEW-3070, which is the anchor I locked shape against.** Its Meccan-internal
> null had MDE 0.261 against a corpus effect of 0.532 — MDE at *half* the corpus effect, a genuinely
> strong null. Mine is at 2.3× the corpus effect. **The two are not comparable and I am not
> claiming to have replicated it.**

---

## 6. THE CONTROL IS 0.906 COLLINEAR WITH THE TREATMENT — the transferable result

Standing rule 4 says check every control for tautology. This one does not survive the check.

| control | ρ(control, Nöldeke phase ordinal) | ρ(control, Medinan binary) | H1 p |
|:--|--:|--:|--:|
| L0 none | 0.0000 | — | **0.0002** |
| verse count | +0.3570 | −0.0278 | **0.0004 / 0.0007** |
| word count | +0.6769 | +0.2360 | **0.0022 / 0.0044** |
| **mean verse length** | **+0.9058** | +0.6035 | **0.2541 / 0.2397** |

**The p-value is monotone in how closely the control duplicates the treatment.** Mean verse length
by phase: Early **4.42** → Middle **9.56** → Late **16.90** → Medinan **19.63**. That is not a
nuisance variable that happens to correlate with phase; **at the surah level it very nearly *is*
the phase variable.**

Conditioning on it removes the contrast under test. The quintile strata show it directly:

| mvl quintile | n | Medinan | Meccan | phases present |
|--:|--:|--:|--:|:--|
| 0 | 23 | 0 | 23 | {Early} only — **zero permutation freedom** |
| 1 | 24 | 0 | 24 | {Early, Middle} |
| 2 | 21 | 2 | 19 | {Early, Middle, Medinan} |
| 3 | 23 | 5 | 18 | {Middle, Late, Medinan} |
| 4 | 23 | 17 | 6 | {Late, Medinan} |

Only **0.600 of L3 strata are informative** (contain ≥2 phase labels), covering **0.588** of
surahs — against **1.000** for L0, verse count and word count quintiles. **The control that decides
the verdict is the one with the least permutation freedom, and it has the least freedom because it
is nearly the treatment.**

### 6.1 What this does and does not license

**It does not prove over-control.** A control that better proxies a genuine confounder also produces
a rising p, and the observed monotonicity is consistent with *both* readings:

- **(a) length is the real driver** — *ʾiḏ* lives in long narrative verses, and chronology only
  correlates because chronology correlates with verse length; or
- **(b) the control is a near-duplicate of the treatment**, and conditioning on it removes the
  signal along with the confound.

**This design cannot distinguish (a) from (b), and neither can any surah-level design in this
corpus, because at surah level the two variables are ρ = +0.906 collinear.** That is the finding.

**What it does license is a warning about a standing project rule.** "Worst length channel governs"
is a sound rule when the channels are nuisance variables. **When the outcome is chronology, mean
verse length is not a nuisance variable, and the rule will return NULL for any chronological
hypothesis regardless of its truth.** Any lane testing chronology should report the collinearity of
each control alongside its p, as this table does.

### 6.2 This bears on H-NEW-3070, and I am flagging it rather than quietly relying on it

H-NEW-3070 (2026-08-09) is my shape anchor and it is being used by other lanes. **Within the Meccan
subset, ρ(mean verse length, Meccan phase ordinal) = +0.8858** — and even verse count reaches
+0.6427 there, so *every* length control is heavily collinear within Mecca. H-NEW-3070's
Meccan-internal NULL (p_worst 0.118 / 0.178 at L3 decile, published with MDE 0.261 as a *strong*
null) rests on that same control. **Its headline PASS is if anything strengthened by this — it
cleared a control 0.906 collinear with its own treatment. But its within-Mecca null is subject to
the over-control reading above, and its MDE was computed against the control, not against the
control's collinearity.** I have not recomputed H-NEW-3070 and make no claim about what it would
show; this is a flag for that lane, not a correction of it.

---

## 7. WHAT WENT AGAINST ME

**7.1 The primary test failed.** Both registered hypotheses are NULL. The direction I locked was
correct on both (+0.0363, ρ = +0.4718) and neither survived the control.

**7.2 My own MDE routine was wrong and I caught it only because its output was self-contradictory.**
MDE < observed < critical is impossible; had the three numbers been merely implausible rather than
arithmetically inconsistent I would probably have published them. The corrected audit is in a
separate run directory; the wrong one is retained.

**7.3 ARM B WAS DESTROYED BY MY OWN SEQUENCING, AND I THEN DEFENDED IT ON THE WRONG GROUND.**
The brief required a circularity assessment before testing. Carrying it out meant computing
ρ(coverage, Nöldeke phase) in the clean window — **which is exactly the statistic a bounded Arm B
would have tested.** I saw the answer (+0.5774) before I could pre-register it. Arm B is therefore
**descriptive only, not pre-registered**, excluded from the Bonferroni family, carrying no verdict.
Logged in prereg §6.2 before the run, not after.

**Arm B was then declined twice, and the second refusal corrected my reasoning.** I had argued to
keep it by promising its MDE — **which answers a power objection.** The objection was
**interpretability**: 31.5% of the entries in the coverage variable have unresolved provenance
between al-Wāḥidī and Maybudī's Persian Sufi commentary. **A perfectly-powered estimate on a
variable where a third of the observations may be a different author's mysticism is not a weak
result, it is an uninterpretable one** — power says whether an effect is detectable, not what the
variable means. My own §3.4 number made it worse rather than better: the Medinan enrichment
**persists at 1.74× inside the clean window**, so Arm B would have estimated a confounded contrast
on a variable of unknown authorship. **Arm B was not run.** It becomes worth running if a provenance
classifier ever drops the ambiguous fraction below ~10%.

*(Distinguishing what was run from what was not: §3.3's coverage channel table is the **instrument
audit** — descriptive correlations establishing what the variable is. It is not Arm B, which would
have been a pre-registered chronology test on that variable, and which does not exist.)*

**7.4 The prior number I locked my direction from is refuted.** `asbab-nuzul.md` §2.1 reports
**156 *ʾiḏ* tokens** (106 Meccan + 50 Medinan) from a string match requiring word-initial
space-preceded `إذ`. **QAC gives 239** for `LEM:<i*` — a **35% undercount**, consistent with the
string rule missing prefixed forms (وإذ, فإذ). Its 1.34× Medinan ratio rests on 65% of the tokens.
**Recomputed on the full inventory the per-verse ratio is 0.0718 / 0.0281 = 2.56× Medinan**
(Medinan 105 tokens / 1,463 verses; Meccan 134 / 4,773) — directionally the same, **1.9× larger
than the published 1.34×**, and still NULL under the control.

**7.5 My pre-registration was ambiguous and I had to disambiguate it before running.** §3.1's S2
originally read *"NULL at α = 0.025 on both units"*, where §3.2 defines "unit" as token-vs-surah
level while S2 meant the two statistic forms. **Caught while diffing the verdict function against
the decision section, before any run**, and fixed in the prereg then (nothing had been run, so
immutability had not yet attached); the SHA was recomputed and re-embedded. Had I found it after
the run it would have been a finding, not a fix.

**7.6 The shape verdict the locked rule emits is not usable**, for the reasons in §5. I am
reporting the label the rule produced and the reasons not to believe it, rather than suppressing
either.

**7.7 A smoke test with 200 permutations was run before the locked run**, to validate code paths.
It gave a preliminary indication of the L0-vs-L3 swing. No forking path was created — the
pre-registration was already hashed and the SHA gate would have refused any edited version — but
it is disclosed rather than left unmentioned.

---

## 8. WHAT THIS COSTS THE FRONTIER MAP

`HANDOFF/CONTINUE-PROMPT.md:225` lists **"al-Wāḥidī *asbāb* (0 scripts)"** among *"idle assets
worth opening."* It is now opened. **It is truncated at surah 77 and 72% not al-Wāḥidī**, and the
"0 scripts" that made it look untouched is also why nobody had found that out. **An asset's
idleness is not evidence of its usability**, and the recommendation should be amended to say so.

`PROXY-CLAIMS.md:477-486` already records **4 `surahs/` loci citing this folder as al-Wāḥidī when
they quote the Sufi text** (Q 48:1, Q 71:13, Q 58:12, Q 38:1). Nothing in this finding changes
that count; it is repeated because those citations are still live.
