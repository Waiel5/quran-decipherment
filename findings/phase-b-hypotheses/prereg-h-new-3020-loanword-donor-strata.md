---
id: H-NEW-3020
title: Is the donor-language field a measurement? Jeffery (1938) against al-Suyūṭī (Itqān nawʿ 38), and the F-5 stratification under a rater swap
date: 2026-08-09
status: LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
family: LOAN-2026-08-09-A
parent: H-NEW-2700 (which executed F-5 and returned NULL/REVERSED); grandparent H-NEW-125 axis 15
seed: 20260509
seed_replication: 20260519
n_permutations: 10000
tests_in_family: 8
alpha_bonferroni: 0.00625
corrected_novelty_gate: 0.005
raw_p_gate: 0.000625
---

# PRE-REGISTRATION — H-NEW-3020

Written **before any statistic relating a donor language to a revelation phase has been
computed**. §2 lists exhaustively what was inspected first, **including one peek that
partially contaminates H1 and is declared as such**. The final SHA-256 of this file is
embedded as a fixed literal in `findings/phase-b-hypotheses/scripts/h-new-3020.py` and
verified at runtime; the run must abort with `SystemExit` on mismatch.

---

## 1. Why this is not a re-run of F-5

**Frontier hypothesis F-5** (`HANDOFF/FRONTIER-MAP-2026-08-07.md` §F-5) was already
executed on 2026-08-07 as **H-NEW-2700**
(`findings/phase-b-hypotheses/h-new-2700-loanword-donor-strata.md`), which returned NULL on
all four registered hypotheses, three of them direction-REVERSED, stable across three
rules-tuples. **This pre-registration does not re-run it and does not re-derive it.**

F-5's own text names the confound that H-NEW-2700 could not close:

> *"Jeffery's etymologies are contested and the donor-language field is his judgement, not
> consensus. A negative result could be an artefact of his classification."*

H-NEW-2700 addressed this **within a single rater** — by subsetting on the registry's own
`confidence` column (its T2) and by broadening the Aramaic family (its T3). Its honest-limit
§5.8 states the residue exactly: *"The registry is a compiled encoding of Jeffery, not
Jeffery. `source_language` is one scholar's judgement transcribed by another hand into a
TSV."* Subsetting one rater's labels cannot measure whether that rater's labels track
anything. **A second rater can.**

`findings/PROXY-CLAIMS.md` §4 requirement 3 makes this obligatory rather than optional: any
hand-assigned quantity used in a statistic must carry *"either an agreement coefficient
against a computed alternative, or an absence claim meeting `ABSENCE-CLAIMS.md` §4."*
§5 adds the specific procedure for an **inherited scholarly classification** — a category
whose rule is prose and which therefore has no computed ground truth — namely the
**rater swap**: re-score the published axes under a second rater, changing nothing but the
rater. The worked precedent is `noldeke_order` versus the Tanzīl Egyptian standard.

**`source_language` has never been validated against anything.** This pre-registration
supplies the second rater, and it is on disk.

### 1.1 The second rater

`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, **lines 9198–9424** —
al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, **nawʿ 38** (`فيما وقع فيه بغير لغة العرب`),
the alphabetical roster introduced at line 9198 by
`وهذا سرد الألفاظ الواردة في القرآن من ذلك مرتبة على حروف المعجم` and closed at line 9425 by
`فهذا ما وقفت عليه من الألفاظ المعربة في القرآن بعد الفحص الشديد سنين`.

This is a **per-word donor-language assignment by a named classical authority (d. 911 AH),
independent of Jeffery (1938), and it has never been parsed by any script in this
repository.** H-NEW-2700 used only the registry's derived binary column
`suyuti_naw_38_attested` (present/absent), **not al-Suyūṭī's donor assignments**. The
distinction is the whole point of this test: the binary column answers *"is it foreign?"*;
nawʿ 38 answers *"foreign from where?"* — which is the field under audit.

**Provenance check per `PROXY-CLAIMS.md` §6.1 (the death-date test).** This file is from the
OpenITI tree, which embeds `010.AuthorNAME` / `011.AuthorDIED` / `020.BookTITLE` per file
and which `PROXY-CLAIMS.md` §6.1 records as **10 for 10** on label accuracy. The
attribution to al-Suyūṭī (d. 911) is not a slug. **The script must re-verify the three
metadata lines at runtime and abort if the author or death date does not match.**

### 1.2 The classical-anchor situation, restated exactly

H-NEW-2700 §7 established, and this pre-registration inherits without re-asserting:
the English *Itqān* PDF on disk **does not contain nawʿ 38**, so no page is cited from it;
al-Suyūṭī's own monograph *al-Muhadhdhab fīmā waqaʿa fī l-Qurʾān min al-muʿarrab* (named at
line 9117) is **not on disk** and nothing is cited from it.

Two positions from the nawʿ bear directly on **this** test rather than on F-5's:

1. **Ibn Jarīr al-Ṭabarī's *tawārud al-lughāt*** (line 9127–9129) —
   `إنما اتفق فيها توارد اللغات فتكلمت بها العرب والفرس والحبشة بلفظ واحد` — that the
   reports of Persian, Ethiopic or Nabataean words record a **convergence of tongues**, not
   a borrowing. H-NEW-2700 §5.3 correctly recorded that no permutation speaks to this.
   **It still does not.** But it predicts something this test *can* see: if the attributions
   are convergence-driven rather than contact-driven, independent raters should disagree
   about the donor, because there is no fact of the matter to agree about. **Low agreement is
   consistent with Ibn Jarīr and does not establish him.**
2. **The reconciling travel-contact position** (line 9130–9134) —
   `كان للعرب العاربة ... بعض مخالطة لسائر الألسنة في أسفارهم فعلقت من لغاتهم ألفاظا` — the
   classical statement of the channel mechanism F-5 tested. It is the warrant for H2/H3.

---

## 2. What was inspected before this lock — exhaustive

Registry structure, the nawʿ 38 extraction, and join feasibility. **No phase distribution,
no donor × phase statistic, and no density-by-phase quantity of any kind was computed,
viewed or estimated.** H2 and H3 are unpeeked. **H1 is partially peeked; see item 7 and
§8.**

1. **Registry shape.** `data/loanwords/jeffery-1938-loanwords.tsv` has **506 lines**:
   **201 comment lines, one header, 304 data rows**. The brief for this task and
   `HANDOFF/FRONTIER-MAP-2026-08-07.md` both report "506 rows"; that is the line count.
   H-NEW-2700 §8 already published this correction and it is confirmed here independently.
2. **Donor-label ambiguity in the registry**, computed and locked as a reported quantity:
   `source_language` is single-valued for all 304 rows, but **169 of 304 (55.6 %) carry a
   label that names two donors** — `hebrew-aramaic-shared` 163, `syriac-aramaic-shared` 6.
   Single-donor labels: 135 (44.4 %). `confidence`: HIGH 160, MEDIUM 47, LOW 97.
   **Rows that are unambiguous on both criteria — a single-donor label AND HIGH confidence —
   number 91 of 304 (29.9 %).** ARAM-narrow 23 rows, persian 35 rows.
3. **`suyuti_naw_38_attested`**: yes 113, no 187, disputed 4. **`luxenberg_disputed`**: yes 3.
4. **nawʿ 38 extraction shape.** Lines 9198–9424 yield **125 paragraphs** and, after the
   attachment rule of §3.3, **117 headword entries**. Of these: **97 carry at least one
   donor family**, **22 (22.7 % of the labelled) name two or more mutually exclusive donor
   families in al-Suyūṭī's own report**, 11 carry only an unspecified-foreign marker
   (`أعجمي` / `العجم` / `غير عربية`), and 9 carry no language marker at all. Per-family
   entry counts: ethiopic 25, aramaic 22, hebrew 19, persian 17, syriac 15, greek 10,
   coptic 6, indic 3, zanji 2, berber 2, turkish 1, hawrani 1.
5. **QAC join feasibility for the nawʿ 38 roster**, tier-1 key only: 85 of 117 join via
   `LEM` (11 of them on a multi-lemma key), 10 more via `FORM`, 22 fail. The two-tier key of
   §3.4 was **not** exercised in feasibility and is adopted unchanged from the parent.
6. **Registry ↔ nawʿ 38 overlap**, tier-1 key with definite-article stripping: **53 shared
   join keys**, of which **43 carry a donor family from al-Suyūṭī**.
7. **⚠ THE PEEK.** A **40-row printout of the paired labels** — Jeffery `source_language`
   beside the extracted al-Suyūṭī families, word by word — was displayed during feasibility.
   **I have seen a large part of the H1 contingency material.** No coefficient was computed
   and no permutation was run, but the qualitative pattern was visible. **§8.1 records what
   this does and does not license, and §4.1 fixes H1's direction on a priori grounds that
   are independent of it.**
8. `data/revelation-order.csv`: 114 rows; `noldeke_phase` ∈ {Early Meccan 48, Middle Meccan
   21, Late Meccan 21, Medinan 24}.
9. `findings/phase-b-hypotheses/scripts/h-new-2700.py` lines 24–120 — the parent's SHA
   gates, Buckwalter map, two-tier key and ambiguity gate, adopted here unchanged.

---

## 3. Instruments — locked

### 3.1 Frozen inputs, SHA-256 verified at runtime, abort on mismatch

| input | path |
|:--|:--|
| this pre-registration | `findings/phase-b-hypotheses/prereg-h-new-3020-loanword-donor-strata.md` |
| Jeffery registry | `data/loanwords/jeffery-1938-loanwords.tsv` |
| al-Suyūṭī *Itqān* | `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` |
| QAC v0.4 morphology | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| chronology | `data/revelation-order.csv` |

The *Itqān* file must additionally pass the **provenance gate**: its OpenITI header must
declare `011.AuthorDIED` = 911 and an `010.AuthorNAME` containing `السيوطي`. Abort otherwise.

### 3.2 The nawʿ 38 span — locked by content, not by line number

The script must **locate** the span by searching for the two literal Arabic anchors below
and abort if either is absent or out of order. Line numbers 9198 / 9425 are recorded for
reference only and must not be hard-coded as the extraction boundary.

- start anchor: `وهذا سرد الألفاظ الواردة في القرآن من ذلك مرتبة على حروف المعجم`
- end anchor: `فهذا ما وقفت عليه من الألفاظ المعربة في القرآن`

### 3.3 Entry segmentation — locked

1. Drop lines matching `^#\s*PageV\d+P\d+\s*$` (page sigla).
2. A line beginning `~~` continues the current paragraph.
3. A line beginning `#` starts a new paragraph.
4. A paragraph whose text begins `{HEADWORD}` opens a new **entry**; the headword is the
   brace content.
5. **A paragraph that does not begin with a brace is appended to the immediately preceding
   entry.** (al-Suyūṭī continues several entries across paragraphs — e.g. `ملكوت`,
   `هيت لك` — and the donor attribution sometimes falls in the continuation.)

### 3.4 Donor-family extraction from al-Suyūṭī — locked vocabulary, gated

**The assignment of words to families is entirely al-Suyūṭī's. What is hand-assigned here is
only the decoding of Arabic language-names into family labels**, which is declared as a
rules-tuple dependency in §5 and listed in full so a reader can re-derive it.

A family is credited to an entry iff a marker below appears **in the entry body, excluding
the headword itself**, in one of two gated frames (`PROXY-CLAIMS.md` §6.1 failure mode 4 —
gate every name, never match a bare noun):

- **nisba frame**: the adjective stem, optionally prefixed `ب` / `بال` / `ال`, optionally
  suffixed `ة` / `ين`.
- **construct frame**: `بلغة` / `بلسان` / `بكلام` (with or without the `ب`) followed by the
  definite people-noun.

| family | nisba stem | people-noun |
|:--|:--|:--|
| ethiopic | حبشي | الحبشة |
| aramaic | نبطي | النبط |
| syriac | سرياني | السريان |
| hebrew | عبراني، عبري | اليهود |
| persian | فارسي | الفرس |
| coptic | قبطي | القبط |
| greek | رومي، يوناني | الروم، اليونان |
| zanji | زنجي | الزنج |
| berber | بربري | البربر |
| indic | هندي | الهند |
| turkish | تركي | الترك |
| hawrani | حوراني | — |

`أعجمي` / `أعجمية` / `العجم` / `عجمي` / `غير عربي` is recorded as
**unspecified-foreign** and is **NOT a family**. `أهل المغرب` / `أهل الغرب` is recorded and
is **NOT a family** (it names a region, not a tongue; the two entries carrying it are
reported).

### 3.5 Join keys — locked, adopted unchanged from H-NEW-2700 §3.2

Buckwalter→Arabic 1:1; strip short vowels and taṭwīl; `وٰ`/`يٰ`→`ا`; **tier 1** dagger
alif→`ا`, **tier 2** dagger alif deleted; then `ٱأإآ`→`ا`, `ؤئ`→`ء`, `ة`→`ه`, `ى`→`ي`,
delete `ء`. A leading `ال` is stripped when the remainder exceeds one character.
**Long-ā-blind keys are rejected** (the parent's rejected variant A, which silently matched
`قرآن` to *qarn*). Tier 1 is tried first; tier 2 only if tier 1 misses.

**Ambiguity gate, inherited:** a key resolving to more than one distinct QAC lemma is
**excluded** and counted. Multiword headwords (`هيت لك`, `الملة الآخرة`) are excluded and
counted.

### 3.6 The outcome — locked

For a lemma type *t* with QAC attestations at verse loci, and `noldeke_phase` mapped
Early Meccan = 1, Middle Meccan = 2, Late Meccan = 3, Medinan = 4:

> **φ(t) = token-weighted mean phase index over t's attestations.**

Each **type counts once** in every statistic below. This is the parent's type-level
co-primary instrument (H-NEW-2700 H4), chosen because the parent's own §1.1 established
that a token-level statistic on this data is substantially a test of two words
(`قرآن` 70 tokens, `رحمن` 57).

---

## 4. Hypotheses and DIRECTIONS — locked and justified

### 4.1 H1 — the two raters agree above chance

> **Statistic:** Cohen's **κ** between Jeffery's `source_language` and al-Suyūṭī's nawʿ 38
> family, over the overlap roster, both mapped into the common scheme of §5.
> **LOCKED DIRECTION: κ > 0.**

**Justification, and it is deliberately independent of §2.7's peek.** Two competent
philologists working on the same words, if the donor-language field records a fact about
those words, must agree more often than labels shuffled at random. There is no coherent
theory on which independent raters agree *below* chance. **The direction is forced a priori;
it is not inferred from the printout.** What the peek could have contaminated — the choice of
statistic, the mapping scheme, the roster — is fixed in this document and may not be
altered after the run (`CONTINUE-PROMPT.md` STANDING RULES 2026-08-08 §1).

**What each outcome means, fixed now so it cannot be dressed up afterwards:**

- **κ high** — the field is a measurement; H-NEW-2700's negative is about the text.
- **κ near zero** — the field is **rater-dependent**, and *no* donor-stratified inference on
  this registry is interpretable, **in either direction**. This retires the instrument, not
  the subject matter (`PROXY-CLAIMS.md` §6). It would mean F-5 is **not decidable** with the
  data on disk, which is a different and stronger statement than F-5 being false.
- **κ intermediate** — `PROXY-CLAIMS.md` §6 PARTIAL: report direction as the finding and
  magnitude as an upper estimate, naming the rater beside every coefficient (§5 of that
  document).

### 4.2 H2 — F-5's channel prediction, under the second rater

> **Statistic:** Δ_S = φ̄(PERS) − φ̄(ARAM) over **al-Suyūṭī's** roster, types equally weighted.
> **LOCKED DIRECTION: Δ_S > 0.**

**Justification.** This is F-5's original prediction verbatim — Syriac/Aramaic religious
vocabulary peaks Late Meccan, Persian administrative/material vocabulary peaks Medinan,
therefore Persian later than Aramaic — carried over unchanged from
`HANDOFF/FRONTIER-MAP-2026-08-07.md` §F-5 and from H-NEW-2700's co-primary H4. **The
direction is inherited, not chosen**, and it is the direction H-NEW-2700 found reversed under
Jeffery's labels. Locking the *original* direction rather than the parent's observed one is
the conservative choice: it keeps this a test of F-5 and not a test of H-NEW-2700, and it
means a second reversal is a second honest pre-commit violation rather than a confirmation
of something already seen.

### 4.3 H3 — the same, under the first rater, on the same words

> **Statistic:** Δ_J = φ̄(PERS) − φ̄(ARAM) over the **overlap roster** using **Jeffery's**
> labels. **LOCKED DIRECTION: Δ_J > 0.**

**Justification.** Identical to §4.2. H3 exists so that H2 and H3 differ in **exactly one
thing that is not the rater** — H2's roster is al-Suyūṭī's, H3's is the intersection — and
so that the declared descriptive quantity Δ_S|overlap (§6) differs from Δ_J|overlap in
**nothing but the rater**. That triple is the rater swap of `PROXY-CLAIMS.md` §5.

---

## 5. Rules-tuples — three, primary declared

The common label scheme is {ARAM, PERS, HEB, ETH, GRK, COPT, OTHER}. **ARAM = Aramaic ∪
Syriac** throughout, matching H-NEW-2700's ARAM_NARROW. `نبطي` (Nabataean) → aramaic is the
standard identification in the classical lexicographical tradition and is treated as a
**tuple axis**, not an assumption.

| | Jeffery mapping | al-Suyūṭī mapping | nabaṭī |
|:--|:--|:--|:--|
| **T1 — PRIMARY (strict)** | two-donor labels (`hebrew-aramaic-shared`, `syriac-aramaic-shared`) **excluded** | multi-family entries **excluded** | → aramaic |
| **T2 (broad)** | `hebrew-aramaic-shared` → HEB; `syriac-aramaic-shared` → ARAM | multi-family → **first-named family** in al-Suyūṭī's own order | → aramaic |
| **T3 (nabaṭī sceptical)** | as T1 | as T1, but `نبطي` credits **no** family | excluded |

`latin`, `south-arabian` → OTHER. `zanji`, `berber`, `indic`, `turkish`, `hawrani` → OTHER.
Entries naming **both** ARAM and PERS are excluded from H2/H3 under every tuple (they carry
no discriminating information for a difference of means); the count is reported.

**The primary verdict is T1.** T2 and T3 are reported in full beside it. Rules-tuple
sensitivity is bidirectional (`feedback_rules_tuple_bidirectional`): a tuple that
rehabilitates the direction is as reportable as one that kills it.

**Declared rules-tuple for every number in this study:**
`(no-tashkeel, QAC-lemma-type, type-counted-once, basmala-per-QAC, Hafs-Kufan, Mashriqi,
Nöldeke-phase-rater)`. Per `PROXY-CLAIMS.md` §5 the Nöldeke rank is itself an inherited
hand-assignment with a published rater-swap coefficient of ρ = +0.7714 against the Tanzīl
Egyptian standard (`h-new-212-alt-chronology-fisher-rao.md:54-63`); **every phase-indexed
number below inherits that uncertainty and the finding must say so.**

---

## 6. The nuisance channels — REPORTED BEFORE THE PRIMARY RESULT

The finding **must** print these before stating any Δ or κ, and the script must emit them in
`result.json` under a key that sorts before the primary block.

1. **ρ(φ(t), log token count of t)** — Spearman, over all joined types. Loanwords are rare
   words and rare-word behaviour interacts with everything.
2. **ρ(φ(t), log mean host-surah word count)** — Spearman, the surah-length channel named in
   the brief and the channel `UNIT-DRIFT-DEFECT.md` §3 requires be declared for every score.
3. **Token-count contrast between the ARAM and PERS strata** — median and range, under T1.
   If the strata differ in frequency, Δ is partly a frequency contrast.
4. **Group sizes** n(ARAM), n(PERS) under every tuple, for both raters.

**Null C (§7) exists because of channel 1** and is the pre-registered response to it: if the
strata differ in frequency, a label permutation that ignores frequency is the wrong null.

---

## 7. Null models — permutation only, no parametric p as primary

10,000 permutations, `random.Random` seeded; replication at seed + 10.
`SEED_NULL_A = 20260509`, `SEED_NULL_B = 20260510`, `SEED_NULL_C = 20260511`.

| null | what is randomised | applies to |
|:--|:--|:--|
| **A — label** | donor labels permuted across the roster, marginals preserved | H1, H2, H3 |
| **B — phase** | `noldeke_phase` permuted across the 114 surahs, φ recomputed | H2, H3 |
| **C — frequency-stratified label** | donor labels permuted **within token-count terciles** | H2, H3 |

Null C is the matched null this project earned the hard way: H-NEW-2760's muqaṭṭaʿāt result
survived only because the label was permuted *within* size quintiles, making the nuisance
budget identical by construction. Terciles are used rather than quintiles because the strata
here are an order of magnitude smaller; if any tercile contains fewer than 2 types from
either stratum, **Null C is reported as UNDERPOWERED and its p-value is not used to gate**,
and that fallback is locked here rather than decided at the console.

**p-value convention:** one-sided in the locked direction,
`p = (1 + #{draw ≥ observed}) / (n_perm + 1)`, floor 9.999 × 10⁻⁵.

### 7.1 Family size and gate

**8 registered inferences**: H1 × {A, B} = 2 (B for H1 = permute the *other* rater's
labels), H2 × {A, B, C} = 3, H3 × {A, B, C} = 3.

- α_Bonferroni = 0.05 / 8 = **0.00625**
- corrected novelty gate = **0.005** (project convention, stricter than Bonferroni)
- **RAW_P_GATE = 0.005 / 8 = 0.000625**

This is deliberately the **same family size and the same gate as H-NEW-2700**, so the two
studies' verdicts are directly comparable. The gate is achievable at 10,000 permutations
(floor 9.999 × 10⁻⁵ < 6.25 × 10⁻⁴).

---

## 8. THE EXACT DECISION RULE

> A registered hypothesis **PASSES** iff
> **(i)** the observed statistic's sign matches its locked direction in §4, **and**
> **(ii)** **every** null registered for it in §7 yields raw permutation p < **0.000625**.
>
> Otherwise the hypothesis is **NULL**.
> If the observed sign is **opposite** to the locked direction, the verdict is
> **"NULL, REVERSED"** and is published as a pre-commit violation with full prominence
> (`INVESTIGATION-PROTOCOL.md` §1.8).
>
> A Null C reported UNDERPOWERED per §7 is **excluded from clause (ii)** and the hypothesis
> is then gated on A and B alone, with the exclusion stated in the verdict line.
>
> **No aggregation across hypotheses. Per-hypothesis verdicts only.** The four nulls of the
> pillar laws randomise different things and are not commensurable
> (`CONTINUE-PROMPT.md`); the same applies here.

The primary verdict is **T1**. T2 and T3 are reported at equal prominence and may not be
promoted to primary after the fact.

**Before the run, the script's verdict function must be diffed against this section line by
line** (STANDING RULE 2026-08-07 §1). The diff must be recorded in the finding's provenance.

### 8.1 What the §2.7 peek does and does not license

- It **does not** invalidate H1's direction, which §4.1 fixes on a priori grounds.
- It **does** mean H1's *p-value* is a weaker object than a fully blind one. **The
  deliverable of H1 is the coefficient κ, which is a descriptive measurement of a
  hand-assigned quantity and stands independently of any null.**
- It **does not** touch H2 or H3: **no phase-indexed quantity has been computed, viewed or
  estimated at any point.**
- The finding **must** repeat this disclosure in its own provenance section. A limitation
  recorded only in a pre-registration is a limitation nobody reads.

---

## 9. Power — stated before the run, not after

The strata are small: 23 ARAM and 35 PERS rows in the registry before any join loss, and
al-Suyūṭī's roster carries 22 aramaic + 15 syriac and 17 persian **entries** before the
multi-family exclusions of §5 and the QAC join loss of §3.5.

**H2 and H3 are powered only to detect a very large effect.** A NULL on either is therefore
**weak evidence of absence** and must be reported as such — it is not a refutation of the
contact-channel hypothesis. H-NEW-2700's honest-limit §5.1 said the same of its own H4, and
what rescued that negative was the *size* of the reversal and its stability, not its n.

**H1 is the well-powered arm** — 43 paired labels on the overlap roster before the §5
exclusions — and it is the arm this study exists for.

---

## 10. Declared descriptive quantities — no gate, MW-7 ceiling if used inferentially

Pre-registered as descriptive so that computing them is not a forking path, and barred from
carrying a verdict:

1. **Δ_S|overlap** — al-Suyūṭī's labels restricted to the overlap roster. With Δ_J (H3) this
   is the like-for-like rater swap: same words, same instrument, **only the rater changes**.
2. Per-family entry and token counts for both raters.
3. The **within-al-Suyūṭī disagreement rate** — entries naming ≥ 2 mutually exclusive
   families — which measures how contested these etymologies were *inside* the classical
   tradition, independent of Jeffery.
4. Agreement of the registry's derived `suyuti_naw_38_attested` column against the actual
   nawʿ 38 roster extracted here. **This is a direct check on the registry compiler's own
   accuracy** and is reported whichever way it falls.
5. Cross-tabulation of the two raters' labels, full matrix.

---

## 11. Garden-of-forking-paths log

1. **F-5 was found to be already executed.** The assigned brief and
   `HANDOFF/FRONTIER-MAP-2026-08-07.md` both present F-5 as untouched; it was run on
   2026-08-07 as H-NEW-2700. **The scope was changed from "execute F-5" to "audit the
   instrument F-5 depends on" before any statistic was computed**, on the ground that
   re-running a completed test duplicates work while its named confound stays open. The
   original hypothesis is nonetheless carried forward unchanged as H2/H3 so that F-5 is
   re-tested under the new rater rather than dropped.
2. **The "506 rows" figure in the brief is a line count.** Corrected to 304 data rows before
   locking; H-NEW-2700 had already published the same correction.
3. **The extraction vocabulary of §3.4 was built by reading al-Suyūṭī's text**, necessarily
   before locking. It was fixed by scanning for language-names, not by checking which
   assignment produced which result — no assignment was ever compared against a phase or
   against Jeffery while the vocabulary was being written. **The gated-frame requirement was
   adopted before any output was inspected**, on `PROXY-CLAIMS.md` §6.1's failure mode 4.
4. **`أهل المغرب` was considered as a berber marker and rejected** before locking, on the
   ground that it names a region rather than a tongue. Two entries carry it (`أب`, `يصهر`);
   neither is ARAM or PERS, so the decision cannot move the primary. Recorded because it was
   a real choice.
5. **The peek of §2.7** — declared above, consequences fixed in §8.1.
6. **No smoke run will be written into `findings/`.** If one is needed for correctness it
   goes to a scratch directory outside the repository, self-declares `SMOKE_RUN: true`, and
   is disclosed in the finding.
7. **Run directories are write-once** — `os.makedirs(exist_ok=False)`, files opened `'x'`.
   **No run directory will be deleted, including a superseded or byte-identical one**
   (STANDING RULE 2026-08-07 §2). Manifest paths are repository-relative.
8. **This pre-registration will not be edited after its run, for any reason, including to
   correct an error in it** (STANDING RULE 2026-08-08 §1). Corrections go in the finding.

---

*Locked 2026-08-09 by Waiel Al-Shujaa, before any donor × phase statistic existed.
Bismillāhi al-Raḥmāni al-Raḥīm.*
