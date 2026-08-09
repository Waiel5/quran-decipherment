---
id: H-NEW-3020
title: The donor-language field is PARTIAL, not a measurement — Jeffery and al-Suyūṭī agree on about half the words, and F-5's reversal replicates under the second rater
date: 2026-08-09
author: Waiel Al-Shujaa
status: H1 NULL at the primary tuple (κ = 0.386, fails one of two nulls at 0.00080 against a 0.000625 gate) and PASS at T2; H2 NULL-REVERSED in all three tuples; H3 UNDERPOWERED TO THE POINT OF NO TEST (n_ARAM = 1)
prereg: prereg-h-new-3020-loanword-donor-strata.md
prereg_sha256: a552d357cabe8fdee20d0a29fc405668289ca149b18b2888063c3de859bbfb60
run: runs/h-new-3020/20260809T070002Z/
parent: H-NEW-2700 (which executed frontier hypothesis F-5); grandparent H-NEW-125 axis 15
seed: 20260509
seed_replication: 20260519
family: LOAN-2026-08-09-A
verdict_summary: PARTIAL per findings/PROXY-CLAIMS.md §6
---

# H-NEW-3020 — Two raters, half agreement, and a reversal that survives the swap

**Verdict, in one paragraph.** Jeffery's donor-language field — the axis frontier hypothesis
F-5 depends on entirely — had never been checked against a second rater. It has now been
checked against al-Suyūṭī's own donor assignments in *al-Itqān* nawʿ 38, extracted from the
on-disk Arabic text. **They agree on 52.4 % of the words they both label (κ = 0.386, n = 21)
under the strict tuple, and on 39.5 % (κ = 0.282, n = 43) under the broad one.** That is
**PARTIAL** in the sense of `findings/PROXY-CLAIMS.md` §6: the field carries real
information and cannot carry a magnitude. **F-5's channel prediction was re-tested under the
second rater and reversed again** — Δ = φ̄(Persian) − φ̄(Aramaic/Syriac) = **−0.576**, against
a locked direction of Δ > 0, in all three rules-tuples. H-NEW-2700 found **−0.911** on the
same statistic with Jeffery's labels. **The reversal is not Jeffery's classification. It
survives changing the rater, the roster and the century.**

Pre-reg SHA-256 `a552d357…bbfb60`, runtime-verified, plus SHA gates on all four data inputs
and a provenance gate on the *Itqān* file. 10,000 permutations per null, replication at
seed + 10. Family of **8** registered inferences; Bonferroni α = 0.00625, project novelty
convention stricter, **raw decision gate 0.000625** — deliberately the same family size and
gate as H-NEW-2700 so the two are comparable.

---

## 0. Scope correction: F-5 was already executed

The brief for this work and `HANDOFF/FRONTIER-MAP-2026-08-07.md` §F-5 both present F-5 as
untouched. **It was executed on 2026-08-07 as H-NEW-2700**
(`findings/phase-b-hypotheses/h-new-2700-loanword-donor-strata.md`), which returned NULL on
all four registered hypotheses, three direction-reversed, across three rules-tuples. The
frontier map is stale on this entry and should be corrected.

Rather than re-run a completed test, this study attacks the confound F-5's own text names
and H-NEW-2700 could not close — *"the donor-language field is his judgement, not
consensus"* — and it carries F-5's original prediction forward unchanged as H2/H3 so the
hypothesis is re-tested rather than dropped. The scope change was made and logged
(pre-reg §11.1) **before any statistic was computed.**

A second correction, independently confirming H-NEW-2700 §8: **the registry has 304 data
rows, not 506.** 506 is the line count — 201 comment lines, one header, 304 rows.

---

## 1. The nuisance channels — reported before the primary, as pre-registered

Pre-reg §6 required these to be computed and published **before** any Δ or κ. Over the 306
pooled joined types:

| channel | Spearman ρ |
|:--|--:|
| φ(type) × log token count | **+0.2201** |
| **φ(type) × log mean host-surah word count** | **+0.7519** |

**The second number is the important one and it is large.** The phase index is not a clean
chronology variable: **57 % of its rank variance is shared with the size of the surahs a word
lives in.** Medinan surahs are long, Early-Meccan surahs are short, and a word's φ is a
token-weighted average over its hosts. Any donor-stratified contrast in φ is therefore partly
a contrast in *which size of surah each stratum's vocabulary inhabits*.

This is `findings/UNIT-DRIFT-DEFECT.md` §3's channel, declared here rather than discovered
later. It applies to **H-NEW-2700's φ statistic identically** — that finding residualised its
*density* arms on log surah length but its type-level co-primary φ is the same construction
as this one, and the loading was not published.

The strata also differ in frequency: median token count **3.5** for the Aramaic/Syriac stratum
against **1.0** for Persian (T1). Null C exists for exactly this reason and permutes labels
within token-count terciles.

---

## 2. The two censuses — how much of each rater's judgement is unambiguous

### 2.1 Jeffery's registry (`data/loanwords/jeffery-1938-loanwords.tsv`, 304 rows)

`source_language` is single-valued for every row, **but 169 of 304 (55.6 %) carry a label
that names two donors**: `hebrew-aramaic-shared` 163, `syriac-aramaic-shared` 6. Single-donor
labels: 135 (44.4 %).

Adding the registry's own `confidence` column: **91 rows of 304 — 29.9 % — are unambiguous on
both criteria, a single-donor label AND HIGH confidence.**

> **Seven of ten rows in the loanword registry are either uncertain about the donor, or name
> two donors, or both.** That fraction is part of this result, as the brief required. It is
> also the reason the primary Aramaic/Syriac stratum is 23 rows before any join loss: the bulk
> of the registry's Aramaic content is inside a label that will not say whether it is Aramaic
> or Hebrew.

Per-donor row counts: hebrew-aramaic-shared 163, hebrew 53, persian 35, syriac 13, greek 11,
ethiopic 9, south-arabian 7, syriac-aramaic-shared 6, aramaic 4, latin 3.

### 2.2 al-Suyūṭī's nawʿ 38 (extracted here; **never parsed by any script before**)

`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, the alphabetical *sard*
between the two locked content anchors: **118 headword entries**.

| | entries |
|:--|--:|
| naming at least one donor family | **97** |
| **naming two or more mutually exclusive families** | **22** |
| unspecified-foreign only (`أعجمي` / `العجم` / `غير عربية`) | 12 |
| region marker only (`أهل المغرب`) | 2 |
| no language marker at all | 7 |

> **22 of 97 — 22.7 % — carry two or more incompatible donor attributions inside al-Suyūṭī's
> own report.** `سري` is Nabataean, Syriac *and* Greek on three different authorities;
> `فردوس` Nabataean and Greek; `السجل` Ethiopic and Persian; `الرحمن` Hebrew on al-Mubarrad
> and Thaʿlab. **The classical tradition did not agree with itself about donor language on
> nearly a quarter of the words it labelled**, and that is measured here for the first time,
> independently of Jeffery.

Per-family entry counts: ethiopic 25, aramaic 22, hebrew 19, persian 17, syriac 15, greek 10,
coptic 6, indic 3, zanji 2, berber 2, turkish 1, hawrani 1.

---

## 3. H1 — the rater agreement. The arm this study exists for.

**Locked direction κ > 0.** Gate: both nulls at raw p < 0.000625.

| tuple | pairs | **κ** | raw agreement | p (permute al-Suyūṭī) | p (permute Jeffery) | verdict |
|:--|--:|--:|--:|--:|--:|:--|
| **T1 — strict (PRIMARY)** | 21 | **+0.3860** | **52.4 %** | 0.00080 | 0.00060 | **NULL** |
| T2 — broad | 43 | +0.2820 | 39.5 % | 1.0×10⁻⁴ | 1.0×10⁻⁴ | **PASS** |
| T3 — nabaṭī-sceptical | 19 | +0.4221 | 57.9 % | 0.00100 | 0.00080 | NULL |

Replication at seed + 10 (T1): κ identical at +0.3860 (the statistic is deterministic);
p = 0.00100 and 0.00090 — **both nulls fail at the replication seed**, so the T1 NULL is
stable rather than a single-seed accident.

### 3.1 The verdict split is a Monte-Carlo artefact and must be read as one

**The direction is positive in every tuple and the coefficient is stable at 0.28–0.42.** The
PASS/NULL split is not a disagreement about the effect; it is a resolution limit:

- A raw gate of 0.000625 at 10,000 permutations means **at most 5 draws** may equal or exceed
  the observation, since p = (1 + k)/10001.
- T1 had **k = 7** and **k = 5** at the primary seed, **k = 9** and **k = 8** at the
  replication seed. **The seed-to-seed movement is larger than the distance to the gate.**
- T2 passed at the floor — **k = 0**, no permutation of 10,000 reached the observed κ — and
  is unambiguous.

> **A gate of 6.25 × 10⁻⁴ is below the resolution a 10,000-permutation null can deliver for a
> statistic on 21 pairs.** Reporting T1 as "NULL" and T2 as "PASS" without this sentence would
> be reporting Monte-Carlo noise as a finding. **The transportable quantity is κ, not the
> gate outcome** — which is what pre-reg §4.1 fixed in advance and §8.1 required be repeated
> here.

### 3.2 What the two raters actually do with the same words

T1 confusion (21 pairs, Jeffery | al-Suyūṭī). The diagonal is 11 of 21:

```
PERS|PERS 6    ETH|ETH 3     GRK|GRK 2
PERS|ETH 1     GRK|ARAM 1    ARAM|PERS 1   HEB|PERS 1   ETH|ARAM 1
OTHER|PERS 1   HEB|ARAM 1    OTHER|GRK 1   OTHER|ETH 1  HEB|ETH 1
```

**Persian is where they agree** — 6 of Jeffery's 7 Persian assignments are Persian for
al-Suyūṭī too (*tannūr*, *zanjabīl*, *surādiq*, *kāfūr*, *kanz*, *yāqūt*). Everything else
scatters. `بيع` is Syriac for Jeffery and Persian for al-Suyūṭī; `دينار` Latin against
Persian; `جهنم` Hebrew against Persian; `الأرائك` Persian against Ethiopic; `حواريون`
Ethiopic against Nabataean; `الصراط` Latin against Greek.

Under T2, which admits Jeffery's two-donor labels as Hebrew, the single largest off-diagonal
cell is **HEB | ARAM = 7** — the words Jeffery files under `hebrew-aramaic-shared` are the
words al-Suyūṭī calls Nabataean. That is not noise; it is a systematic difference in how the
two raters cut the Northwest-Semitic space, and it is why the broad tuple has a *lower* κ on
*more* data.

---

## 4. H2 and H3 — F-5's prediction, re-tested under the second rater

**Locked direction Δ = φ̄(PERS) − φ̄(ARAM) > 0**, carried unchanged from F-5 and from
H-NEW-2700's co-primary H4. Phase index Early = 1 → Medinan = 4; each type counts once.

### 4.1 H2 — al-Suyūṭī's labels, al-Suyūṭī's roster

| tuple | n ARAM | n PERS | φ̄ ARAM | φ̄ PERS | **Δ** | p_A label | p_B phase | p_C freq | verdict |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|:--|
| **T1 (PRIMARY)** | 14 | 12 | 2.805 | 2.229 | **−0.5759** | 0.925 | 0.951 | 0.739 | **NULL, REVERSED** |
| T2 | 20 | 13 | 2.714 | 2.211 | −0.5026 | 0.940 | 0.923 | 0.813 | **NULL, REVERSED** |
| T3 | 7 | 12 | 3.151 | 2.229 | −0.9222 | 0.982 | 0.981 | 0.950 | **NULL, REVERSED** ¹ |

¹ Null C UNDERPOWERED per pre-reg §7 and excluded from the gate; the verdict rests on A and B.
Replication at seed + 10 (T1): Δ identical, p = 0.931 / 0.954 / 0.731.

**Zero entries named both an Aramaic/Syriac and a Persian donor**, so the §5 exclusion never
fired.

The Persian stratum is **0.58 phases EARLIER** than the Aramaic/Syriac stratum. F-5 required
it to be later. **This is a pre-commit violation and is published as one.**

Its roster is why. al-Suyūṭī's Persian words are *abārīq* (ewers), *tannūr* (oven), *jahannam*,
*dīnār*, *zanjabīl* (ginger), *sijjīl*, *surādiq* (canopy), *kāfūr* (camphor), *misk* (musk),
*maqālīd* (keys), *nūn*, *yāqūt* (ruby) — **material and Paradise-furnishing vocabulary, not
administration.** His Aramaic/Syriac words are *akwāb*, *tatbīr*, *taḥt*, *ḥawāriyyūn*,
*ribbiyyūn*, *safara*, *sujjadan*, *Sīnāʾ*, *shahr*, *ʿabadtu*, *al-Qayyūm*, *malakūt*,
*manāṣ*, *warāʾ*. **This independently reproduces H-NEW-2700 §2's post-hoc diagnosis on a
roster that finding never saw** — the premise that Quranic Persian is Sasanian administrative
vocabulary is false, under either rater.

### 4.2 H3 — Jeffery's labels on the overlap roster: no test

| tuple | n ARAM | n PERS | Δ | verdict |
|:--|--:|--:|--:|:--|
| T1 | **1** | 13 | −1.0115 | NULL, REVERSED — **but n_ARAM = 1** |
| T2 | 3 | 13 | −0.5507 | NULL, REVERSED — n_ARAM = 3 |
| T3 | **1** | 13 | −1.0115 | NULL, REVERSED — n_ARAM = 1 |

> **H3 is reported as a failed arm, not as evidence.** A difference of means with one
> observation in a group is not a measurement, and the registered permutation p-values
> (0.93, 0.73, 1.00) describe an object that should not be interpreted. The single T1
> Aramaic/Syriac word is `طوبى`.
>
> **The reason is itself the finding**: the 54 words the two rosters share contain almost no
> Jeffery-Aramaic, because Jeffery's Aramaic content is locked inside `hebrew-aramaic-shared`
> — the 55.6 % ambiguous bloc of §2.1. **The registry's ambiguity does not merely add noise;
> it empties the stratum the hypothesis is about.**

---

## 5. The rater swap — same 54 words, only the rater changes

Pre-registered as descriptive (§10.1), no gate, MW-7 ceiling. This is the
`findings/PROXY-CLAIMS.md` §5 procedure, applied to a second proxy family.

| tuple | Δ under **Jeffery** (n ARAM, n PERS) | Δ under **al-Suyūṭī** (n ARAM, n PERS) |
|:--|--:|--:|
| T1 | **−1.0115** (1, 13) | **−0.1614** (6, 7) |
| T2 | −0.5507 (3, 13) | −0.2047 (9, 8) |
| T3 | −1.0115 (1, 13) | −0.9614 (2, 7) |

**The sign is identical in all three tuples. The magnitude differs by 2.7× to 6.3×.** And the
raters do not only disagree word by word — **they carve the strata to different sizes on
identical inputs**: 1 versus 6 Aramaic/Syriac words, 13 versus 7 Persian.

> This is `PROXY-CLAIMS.md` §5's rule confirmed on new material:
> **an inherited classification is directionally robust and quantitatively rater-dependent.**
> Report the direction as the finding, the magnitude as an upper estimate, and **name the
> rater in the same breath as the coefficient.**

---

## 6. An audit of the registry's own al-Suyūṭī column

Pre-registered descriptive (§10.4). The registry's `suyuti_naw_38_attested` flag against the
nawʿ 38 roster actually extracted from al-Suyūṭī's text:

| registry flag | in the extracted roster | not in it |
|:--|--:|--:|
| `yes` (113) | **36** | **77** |
| `no` (187) | **19** | 168 |
| `disputed` (4) | 0 | 4 |

**Both directions need stating carefully, and only one of them is a defect.**

- **The 77 are largely not an error.** The locked span is al-Suyūṭī's alphabetical *sard*
  only. A **post-hoc** check (labelled as such, MW-7 ceiling) finds 3 of the 77 in the
  versified appendix that follows the end anchor, and 11 are flagged *"Personal name"* in
  the registry's own notes — and nawʿ 38 explicitly sets proper names aside as *not* the
  locus of dispute (`الأعلام ليست محل خلاف`, line 9147). The column encodes a **broader**
  reading of "occurs in nawʿ 38" than the roster does. **The two are not interchangeable, and
  that is worth knowing; it is not a charge of error.** 63 remain unaccounted by either route.
- **The 19 are harder to explain benignly.** These are words the registry says al-Suyūṭī does
  **not** list, which appear as headwords in his alphabetical roster — including four rows the
  registry rates HIGH confidence: `سفرة`, `مرجان`, `يهود`, `حرم`. Also `أكواب`, `ربيون`,
  `سجل`, `سجين`, `فردوس`, `مرقوم`, `هدنا`, `وردة`, `وزر`, `سقر`, `يس`.

**And one flat data error, found incidentally.** Line 234 of the TSV gives `arabic_lemma`
= `فردوس` with `romanized` = `farāsh` and the note *"Carpet, couch; Pers. farš"*. The Arabic
lemma for *farsh* is `فرش`; `فردوس` is *firdaws*, already on line 231. **One of the 304 rows
carries the wrong Arabic word**, which is also why the file has 303 unique lemmas for 304 rows.

---

## 7. What this does to H-NEW-2700 and H-NEW-125

- **H-NEW-2700 is strengthened, not overturned.** Its central worry — that its negative might
  be an artefact of Jeffery's contested etymologies — is now answered with an actual second
  rater rather than with subsets of the first. Its co-primary reversal (Δ = −0.911) reproduces
  in sign and order of magnitude under al-Suyūṭī's labels on a different roster
  (Δ = −0.576). **F-5's channel prediction fails under both raters.**
- **But H-NEW-2700's honest-limit §5.8 needs upgrading from a caveat to a number.** It said
  *"`source_language` is one scholar's judgement transcribed by another hand."* It is now
  measured: **κ = 0.386, 52.4 % raw agreement.** Under `PROXY-CLAIMS.md` §6 that is
  **PARTIAL**, and PARTIAL is not a soft NOISE — the field carries real information about a
  real thing. What it cannot carry is a magnitude.
- **A second nuisance channel is added to both findings**: ρ(φ, log host-surah size) = +0.7519.
  H-NEW-2700 residualised its density arms on log surah length but published no size loading
  for its type-level φ. That loading is large and should travel with the co-primary.
- **⛔ CORRECTION, 2026-08-09, entered after a ledger grep this study should have run before
  its own pre-registration.** An earlier draft of this section said *"H-NEW-125 axis 15 is
  untouched."* **That is false.** `h-new-2770-chronology-content-length-nuisance.md` demoted
  it on 2026-08-07:

  | quantity | value |
  |:--|--:|
  | `loanword_density` ρ vs Nöldeke rank, **per verse** (published) | +0.8329 |
  | same axis **per word** | **+0.0547** |
  | ρ(`loanword_density`, mean verse length) | **+0.8869** |
  | partial ρ controlling log mean verse length | +0.1594 (p = 0.0159, fails its gate) |

  **Ninety-three per cent of the parent axis is the denominator**, and the axis correlates
  more strongly with mean verse length (+0.887) than with chronology (+0.833) — it is
  H-NEW-2770's single most denominator-driven axis of the fifteen. The token total reproduces
  exactly (6,156).

  **Consequence for this study:** the axis F-5 proposed to split was already substantially a
  verse-length measurement before anyone split it. That does not change any number in §§1–6 —
  φ is a type-level phase index, not a per-verse density, and no result here is derived from
  axis 15 — but it removes the last reason to treat a donor-split of that axis as load-bearing.
  **This study's own ρ(φ, log host-surah words) = +0.7519 is the same confound family,
  independently measured on a different statistic.**

---

## 8. Honest limits

1. **H1's primary tuple rests on 21 paired labels.** κ = 0.386 has a wide interval at that n.
   The broad tuple's 43 pairs give κ = 0.282. **The honest statement is a range, 0.28–0.42,
   not a point.**
2. **H1 was partially peeked** (pre-reg §2.7, §8.1). A 40-row printout of the paired labels
   was visible during feasibility, before the pre-registration was locked. The direction
   κ > 0 is forced a priori and was not inferred from it, and the statistic, mapping and
   roster were fixed in the pre-registration and not altered afterwards — **but H1's p-values
   are a weaker object than fully blind ones, and the deliverable is κ.** H2 and H3 are
   unpeeked: no phase-indexed quantity was computed or viewed before the lock.
3. **H3 is not a test** (§4.2). n_ARAM = 1.
4. **H2's strata are 14 and 12 types.** Pre-reg §9 declared before the run that H2 and H3 are
   powered only for a very large effect. **A NULL here is weak evidence of absence.** What
   carries weight is not the p-value but that the *sign* reverses under an independent rater,
   an independent roster, and three tuples.
5. **The donor-family decoding in pre-reg §3.4 is mine.** al-Suyūṭī assigns the words; I
   assign Arabic language-names to family labels. The full vocabulary is published in the
   pre-registration so a reader can re-derive or dispute it. `نبطي` → Aramaic is the standard
   identification and is treated as a tuple axis (T3), not an assumption.
6. **The extraction covers the alphabetical roster only.** The versified appendix — Ibn
   al-Subkī's 27 words, Ibn Ḥajar's 24, al-Suyūṭī's own additions — falls outside the locked
   span and contributes no labels. It is where 3 of §6's 77 live.
7. **Both raters are hand-assignments; neither is ground truth.** Agreement between two
   judgements is not correctness of either. If Ibn Jarīr al-Ṭabarī's *tawārud al-lughāt* is
   right — that these are convergences between tongues rather than borrowings (*Itqān* nawʿ
   38, line 9127) — then there is no fact for the raters to agree about, and **moderate
   agreement is exactly what that position predicts.** No permutation here speaks to it.
   This does not establish Ibn Jarīr; it notes that the result is consistent with him.
8. **The Nöldeke sequence is itself an inherited hand-assignment**, reproducing the Tanzīl
   Egyptian standard at only ρ = +0.7714 (`h-new-212-alt-chronology-fisher-rao.md:54-63`).
   Every φ inherits that uncertainty. **This study has two rater-dependent axes, not one.**
9. **The join is lossy and not at random.** Of 118 al-Suyūṭī entries, 88 resolve (74 tier-1
   lemma, 4 tier-2, 10 form-level); 17 unmatched, 11 blocked by the ambiguity gate, 2
   multiword. Of 304 registry rows, 218 resolve. H-NEW-2700 §5.2 already identified join loss
   as the binding constraint and it remains unrepaired.
10. **No cross-corpus control.** Nothing here shows these patterns are specific to this corpus
    rather than general to seventh-century Ḥijāzī Arabic.

---

## 9. Provenance

- Pre-registration written and SHA-256'd **before any donor × phase statistic existed**.
  Pre-reg §2 lists exhaustively what was inspected first, **including the peek at §2.7**.
- **Verdict-logic diff performed before publication**, as required by the STANDING RULE of
  2026-08-07 §1. Pre-reg §8: *"PASSES iff (i) the observed statistic's sign matches its locked
  direction in §4, and (ii) every null registered for it in §7 yields raw permutation
  p < 0.000625."* Script: `direction_ok = stat > 0` (all three §4 locks are `> 0`);
  `all_gates = all(p < RAW_GATE ...)` with `RAW_GATE = CORRECTED_GATE / TESTS_IN_FAMILY =
  0.005 / 8 = 0.000625`; `PASS` iff both; `NULL, REVERSED` iff `stat < 0`; `NULL` otherwise;
  Null C dropped from the gate when flagged UNDERPOWERED and the exclusion printed in the
  verdict line. **Match, clause for clause.** Two corrections were made to the script *before*
  the run to bring it into literal agreement with §8: the `stat == 0` case was routed to plain
  `NULL` rather than `NULL, REVERSED`, and a dead T3 branch inside the T2 mapping was removed.
- **An internal tension in the pre-registration is recorded rather than repaired.** §7's table
  lists Null B as applying to "H2, H3", while §7.1 explicitly assigns H1 the pair {A, B} with
  B defined as permuting the other rater's labels, and counts the family as 8 on that basis.
  The script implements §7.1. **Per the STANDING RULE of 2026-08-08 §1 the pre-registration
  has not been edited; the discrepancy is reported here.**
- **Inputs SHA-verified at runtime, run aborts on mismatch**: prereg `a552d357…`, Jeffery TSV
  `d12ebac9…`, *Itqān* `a067ebb3…`, QAC v0.4 `a1d12923…`, revelation order `74f52ec1…`.
- **Provenance gate on the classical source**, per `PROXY-CLAIMS.md` §6.1: the run aborts
  unless the OpenITI header declares `011.AuthorDIED :: 911` and an `010.AuthorNAME`
  containing `السيوطي`. Both verified. The nawʿ 38 span is located by **content anchors**, not
  by line number, and the run aborts if either anchor is missing or out of order.
- **One 200-permutation smoke run** for correctness, written to a scratch directory **outside
  the repository**, self-declaring `SMOKE_RUN: true`. Its structural fields and deterministic
  statistics were visible before the 10,000-permutation run; **no gate, direction, seed,
  statistic, tuple or family size was changed as a result** — the deterministic statistics are
  identical between the two runs by construction and only the p-values differ.
- Immutable run: `findings/phase-b-hypotheses/runs/h-new-3020/20260809T070002Z/`, created with
  `os.makedirs(exist_ok=False)` and files opened `'x'`. **No run directory was deleted.**
  Manifest paths are repository-relative.
- **This study is uncommitted at time of writing.**

### 9.1 Garden-of-forking-paths log

1. **F-5 was found already executed** and the scope was changed from "execute F-5" to "audit
   the instrument F-5 depends on", before any statistic was computed (pre-reg §11.1). F-5's
   original prediction is carried forward unchanged as H2/H3.
2. **The "506 rows" figure in the brief is a line count**; corrected to 304 before locking.
3. **The extraction vocabulary of pre-reg §3.4 was necessarily built by reading al-Suyūṭī's
   text**, by scanning for language-names — never by checking which assignment produced which
   result. No assignment was compared against a phase or against Jeffery while it was written.
   The gated-frame requirement was adopted before any output was inspected, on
   `PROXY-CLAIMS.md` §6.1 failure mode 4.
4. **`أهل المغرب` was considered as a Berber marker and rejected before locking**, as naming a
   region rather than a tongue. Two entries carry it (`أب`, `يصهر`); neither is Aramaic or
   Persian, so the choice cannot move the primary.
5. **The peek** of pre-reg §2.7, consequences fixed in §8.1 and restated in §8.2 above.
6. **The §6 versified-appendix check and the `farāsh` row are POST-HOC**, generated by reading
   the result. Both are labelled, carry the MW-7 single-test ceiling, and are diagnostics of
   this study's own instrument and of the registry — not findings about the text.
7. **The feasibility parse returned 117 headword entries and the locked parse returns 118**,
   because the locked span is defined by content anchors and begins one line after the start
   anchor while the feasibility slice used a hard-coded index. **The locked instrument is
   authoritative** and no number in this finding comes from the feasibility parse.

---

## 10. Cross-references

- **[[h-new-2700-loanword-donor-strata]]** — the parent, which executed F-5. Strengthened by
  §7; its honest-limit §5.8 is upgraded from a caveat to κ = 0.386; a size loading of +0.7519
  is added to its type-level co-primary.
- **[[h-new-125-chronology-content]] axis 15** — untouched (§7).
- **`findings/PROXY-CLAIMS.md`** — this is §4 requirement 3 discharged for
  `source_language`, and §5's rater swap executed on a second proxy family. **Verdict:
  PARTIAL.** The §6 table gains a row, and the "operating range versus full set" pairing has
  an analogue here: the two raters agree best on Persian and scatter everywhere else, so the
  field **selects a Persian stratum reliably and ranks the Northwest-Semitic space badly.**
- **`findings/UNIT-DRIFT-DEFECT.md`** — ρ(φ, log host-surah size) = +0.7519 is a new entry for
  its drift table, and it applies to H-NEW-2700's co-primary as well as to this one.
- **`HANDOFF/FRONTIER-MAP-2026-08-07.md` §F-5** — **stale**; F-5 was executed on 2026-08-07.
  The map should record H-NEW-2700 and this study against that entry.
- **The retirement ledger** — this is an **instrument audit**, not a retirement. It retires
  neither the loanword registry nor the contact-channel question. It fixes the precision at
  which the donor-language axis can be used: **direction yes, magnitude no, and never without
  naming the rater.**

---

*Run 2026-08-09 by Waiel Al-Shujaa. Two philologists a millennium apart, asked the same
question about the same words, agree about half the time — and the answer they disagree about
is the one four separate findings had been resting on. Bismillāhi al-Raḥmāni al-Raḥīm.*
