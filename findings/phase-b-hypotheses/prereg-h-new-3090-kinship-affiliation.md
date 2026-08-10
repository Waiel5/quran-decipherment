---
id: H-NEW-3090
title: Pre-registration — Biological-kinship vs affiliative vocabulary across the Hijra, held at fixed register
author: Waiel Al-Shujaa
date: 2026-08-09
status: PRE-REGISTERED — LOCKED BEFORE RUN
frontier_item: F-20 (HANDOFF/FRONTIER-MAP-2026-08-07.md:366-371)
seed: 20260509
n_perms: 10000
---

# H-NEW-3090 — pre-registration

## 0. Step-0 prior-art grep (run BEFORE any design; binding rule, FRONTIER-MAP:201-205)

Commands actually run:

```
grep -rniE "kinship|walad|rahim|nasab|ikhwa|awliya|mawla|affiliation|mu.akhat" --include='*.md' -l .
grep -niE "kinship|walad|mawla|awliya|ikhwa|nasab|affiliation|brotherhood|mu.akhat|tribal" MASTER-FINDINGS-LEDGER.md
find . -iname '*kinship*'
grep -rniE "H-NEW-267" --include='*.md' -l .
```

**Result — F-20 is NOT a full re-derivation, but it is partially pre-empted.**

| # | What exists | Bearing on F-20 |
|:--|:--|:--|
| 1 | **No dedicated H-NEW finding** for kinship-vs-affiliation anywhere in `findings/` or the ledger. | The phase test itself is genuinely new. |
| 2 | **H-NEW-267** (`h-new-267-mecca-medina-vocabulary-frontier.md`, PASS-DIRECTED, AUC 1.000 both directions, prereg SHA `554bfb1f4ee27f6d4febf3ad4f62ca8d660892a6a1d5ad8d21c8e7f203eb265a`) lists **`mwl` — the root of *mawlā* — among its six "sharp stable roots toward Medinan"** (stable score 1.640769, full log-odds 1.759607, **8 Late-Meccan vs 54 Medinan tokens**). | **One of F-20's three affiliative terms is already a published Medinan marker.** Any Medinan-affiliative result carried by *mawlā* re-derives H-NEW-267's own table and must be reported as such, not as new. |
| 3 | **H-NEW-277** — broad-root ablation on the same Late-Meccan→Medinan frontier. | The frontier is already ablation-tested at root level. |
| 4 | `kinship-vocabulary.md` (2026-04-12) — inventory + four qualitative hypotheses H-K1..H-K4. **It never tests phase.** Its **H-K1** states that *walad* is the Qurʾān's *abstract theological* offspring-word and that "the theological-denial cluster is the largest single use of `walad`" (17 of 47 verses). | **Prior art inside this project already contradicts F-20's premise** that *walad* indexes biological kinship. This is pre-declared as the leading explanation for any Meccan loading of the BIO class. |
| 5 | FRONTIER-MAP's own prior for F-20: *"CONFIRMED but CBM-leaning — it may simply restate the Hijra."* | Adopted. See §7 decision ladder, which contains **RESTATES THE HIJRA** as a named terminal verdict. |

## 1. Hypothesis

**F-20 as stated.** Biological kinship terms (*walad*, *raḥim*, *nasab*) and affiliative terms
(*ikhwa*, *awliyāʾ*, *mawlā*) are in complementary distribution across Meccan/Medinan, tracking the
replacement of tribal by confessional affiliation.

**The question this pre-registration actually answers**, in order of priority:

1. **Does the kinship/affiliation contrast survive when discourse register is held fixed?**
   If not, the honest verdict is **RESTATES THE HIJRA** and that phrase goes in the finding's title.
2. **Do the six terms F-20 names measure what F-20 says they measure?** This is a
   `findings/PROXY-CLAIMS.md` question and it is co-primary, not an appendix.

## 2. Data and rules-tuples

**Corpus.** `quran-text/quran-min-tashkeel.json` (Tanzil Uthmani, Ḥafṣ-Kūfan) for text;
`data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4, Buckwalter) for all lemma/root/POS
assignment and for all unit counts. A "word" is a distinct `(sūra, āya, word)` triple; a "verse" is a
distinct `(sūra, āya)`. Only rows carrying `STEM` are counted as content tokens.

**Phase.** `data/revelation-order.csv`, column `period` ∈ {Meccan, Medinan}, joined on `mushaf_order`.
86 Meccan / 28 Medinan.

**Register.** `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`, column `neuwirth_genre`
(56 distinct values over 114 sūras), coarsened by **first-match precedence** — the rule is locked here
and implemented verbatim in code:

```
1. 'legal'                                            -> LEGAL
2. 'narrative' or 'qaṣaṣ'                              -> NARRATIVE
3. 'eschatolog'                                        -> ESCHATOLOGICAL
4. 'scripture-reflective'                              -> SCRIPTURE
5. 'oath'|'hymn'|'liturgical'|'apotropaic'|'creedal'   -> HYMNIC_OATH
6. otherwise                                           -> EXHORT_POLEM
```

### 2.1 The three rules-tuples (≥2 required; two are verdict-bearing)

| tuple | definition | role |
|:--|:--|:--|
| **R1 — LEMMA-LITERAL** | Exactly the six terms F-20 names, at QAC **lemma** level. **BIO** = `LEM:walad`, `LEM:>aroHaAm`, `LEM:nasab`. **AFF** = `LEM:<ixowapN`, `LEM:waliY~`, `LEM:mawolaY\``, `LEM:mawa\`liY`, `LEM:mawa\`liy`. | **PRIMARY, verdict-bearing** |
| **R2 — ROOT-LITERAL** | The same six terms taken at **root** level: **BIO** = roots {`wld`, `rHm`, `nsb`}, **AFF** = roots {`Axw`, `wly`}, all STEM tokens. | **Contamination diagnostic only — NOT verdict-bearing.** It deliberately admits the root collisions (`rHm`→*raḥma*/*al-Raḥmān*, `wly`→*tawallā*, `nsb`→*anṣāb*). Its gap from R1 measures how much of any root-level effect is collision. |
| **R3 — SENSE-CLEAN ABLATION** | R1 restricted to tokens on which **two independent raters agree**, and whose agreed sense **equals the class F-20 assigns to that lemma**. Raters defined in §3. | **verdict-bearing** |

**Declared before locking (full disclosure of what I had already seen).** The QAC lemma census in
§2.2 was computed *before* this pre-registration was written, and I therefore knew the token totals
and the fact that four of the seven `<ixowapN` tokens sit in Sūrat Yūsuf. **I had not computed, seen,
or estimated any Meccan/Medinan split, any density, any contrast, or any p-value for any term.** The
census fixed the inventory; it did not touch the outcome variable.

### 2.2 Locked inventory (QAC v0.4 STEM token counts, computed 2026-08-09)

**BIO (R1) — 71 tokens**: `walad` 56 · `>aroHaAm` 12 · `nasab` 3.
**AFF (R1) — 114 tokens**: `waliY~` 86 · `mawolaY\`` 18 · `mawa\`liY`/`mawa\`liy` 3 · `<ixowapN` 7.

Root-level totals for R2: `wld` 102 · `rHm` 339 · `nsb` 3 (BIO = 444); `Axw` 96 · `wly` 232 (AFF = 328).

## 3. The proxy census and the second rater (PROXY-CLAIMS §4)

The F-20 inventory is a **hand-assigned word list** — it is a category whose assignment rule is prose.
`findings/PROXY-CLAIMS.md` §4 requires that the finding state (1) that it is hand-assigned and by what
rule, (2) its operating range, and (3) an agreement coefficient against an alternative. All three are
pre-committed here.

### 3.1 Rater A — Arabic-morphology co-occurrence rule (computed from QAC alone)

For each token *t* of a class lemma, over the STEM tokens of *t*'s own verse:

1. **DIVINE** if a token with `ROOT:Alh` or `LEM:r~aHoma\`n` occurs within **3 STEM positions** of *t*.
2. else **BIO** if any *other* token in the verse has `ROOT` ∈ {`Abw`, `Amm`, `bny`, `zwj`, `wld`, `nsl`, `*rr`, `Emm`, `xwl`, `Axw`}.
3. else **AFF**.

### 3.2 Rater B — the Sahih International translator's judgement (independent of QAC)

`data/translations/en.sahih.txt`, line *n* = the *n*-th verse in mushaf order. Over the lower-cased
English of *t*'s verse:

- `BIO_LEX`  = {brother, sister, kinship, womb, parent, father, mother, son, daughter, offspring, child, children, relative, kin, lineage, born, beget}
- `AFF_LEX`  = {ally, allies, protector, guardian, patron, friend, helper, supporter, associate}
- **DIVINE** if any `AFF_LEX` word occurs within **3 English words** of "allah".
- else **BIO** if `BIO_LEX` ∩ verse ≠ ∅ and `AFF_LEX` ∩ verse = ∅.
- else **AFF** if `AFF_LEX` ∩ verse ≠ ∅ and `BIO_LEX` ∩ verse = ∅.
- else **AMBIGUOUS**.

Rater B is a *different human's* sense judgement, encoded in the choice of English word, read by a
declared keyword rule. It shares no input with Rater A beyond the verse identity.

### 3.3 Pre-committed reporting

- **Cohen's κ(A, B)** over the **operating range** (tokens where B ≠ AMBIGUOUS) — **primary** — and over
  the **full set** (AMBIGUOUS treated as its own category) — both reported, per PROXY-CLAIMS §4's
  select-versus-rank clause.
- **Per-term census**: for each of the six terms, the count and share of tokens that are DIVINE, that
  are cross-class (assigned the class F-20 does *not* give the lemma), and that are agreed-in-class.
  **The unambiguous fraction IS part of the result.**
- **Size loading** (UNIT-DRIFT-DEFECT.md, and PROXY-CLAIMS §4's Screen A′): Spearman ρ between each
  per-sūra class count and log word-count, reported for BIO and AFF separately.

## 4. The register confound, and why the primary within-register arm is an ablation

**Computed before locking, from the two label files, no outcome variable involved:**

| coarsened register | Meccan | Medinan | mixed? |
|:--|--:|--:|:--|
| NARRATIVE | 27 | 0 | **no** |
| LEGAL | 0 | 15 | **no** |
| ESCHATOLOGICAL | 23 | 2 | yes |
| HYMNIC_OATH | 14 | 2 | yes |
| SCRIPTURE | 11 | 1 | yes |
| EXHORT_POLEM | 11 | 8 | yes |

**The two registers the F-20 confound is about are perfectly collinear with phase at sūra granularity.**
A within-stratum permutation cannot move a label in the LEGAL or NARRATIVE stratum: those 42 sūras
contribute exactly zero permutable information. The mixed strata hold 59 Meccan against **13** Medinan.

Therefore the headline within-register arm is a **legal-register ablation**, which does not require
mixed strata and answers the confound directly ("is the affiliative rise a legal-register effect?"), and
the stratified permutation is retained as a secondary arm with its degeneracy reported.

## 5. Tests, channels, and statistics

### 5.1 The three tests

- **T1 — FULL.** All 114 sūras, Meccan vs Medinan. This is the CBM baseline; a pass here alone means
  nothing new (H-NEW-267 already separates the same boundary at AUC 1.000).
- **T2 — LEGAL-ABLATED. THIS IS THE HEADLINE.** Drop every sūra with coarsened register `LEGAL`
  (15 sūras, all Medinan). N = 99 (86 Meccan, 13 Medinan). If the contrast dies here it was register.
- **T3 — REGISTER-STRATIFIED.** Restricted to the four mixed strata (72 sūras). Statistic = token-mass-weighted
  mean of the within-stratum contrast. Null permutes phase labels **within** strata only.

### 5.2 The four length channels (MANDATORY — the length-channel rule)

Length is at least three variables. All four channels are run for every test and every rules-tuple; **none
is privileged; the WORST is the headline.** For sūra *s* with `AFF_s`, `BIO_s`, word count `W_s`, verse
count `V_s`, mean verse length `MVL_s = W_s / V_s`:

| channel | per-sūra quantity | test statistic Δ |
|:--|:--|:--|
| **RATIO** | — (pooled) | `S(Medinan) − S(Meccan)` where `S(g) = ΣAFF_g / (ΣAFF_g + ΣBIO_g)`. Length-free by construction. |
| **PER_WORD** | `c_s = (AFF_s − BIO_s) / W_s` | `mean(c_s | Medinan) − mean(c_s | Meccan)` |
| **PER_VERSE** | `c_s = (AFF_s − BIO_s) / V_s` | same |
| **MVL_RESID** | residual of `(AFF_s − BIO_s)/W_s` after OLS on `log(MVL_s)` over the sūras included in that test | same |

**Which channel is DOMINANT for this grouping will be reported explicitly**, as the channel whose
p-value is furthest from the others.

### 5.3 Locked direction, and its justification

**Δ > 0 in every channel** — the affiliative class stands relatively higher in Medinan, the biological
class relatively higher in Meccan. One-sided. Justified before the run by four independent grounds:

1. The confessional-brotherhood and *walāya* verses are Medinan: Q 49:10 (*innamā al-muʾminūna ikhwatun*),
   Q 33:5 (*ikhwānukum fī al-dīn wa-mawālīkum*), Q 8:72–75, Q 33:6.
2. The *muʾākhāt* is a post-Hijra event in the sīra (§8).
3. **H-NEW-267 independently places `mwl` on the Medinan side** (8 vs 54 tokens) — an out-of-sample
   directional prior from a different instrument.
4. The *walad*-denial polemic, which `kinship-vocabulary.md` identifies as the largest single use of the
   dominant BIO term, targets Meccan *mushrik* and Christological claims and sits in Meccan sūras
   (112, 19, 21, 23, 25, 43, 72, 6, 17, 18).

**Note that ground 4 predicts the right direction for the wrong reason** — it is a Christology effect, not
a kinship effect. This is pre-declared as the leading alternative explanation for any BIO-Meccan loading,
and §6.3 is the arm that separates them.

### 5.4 Null model

**Permutation, 10 000 permutations, seed 20260509**, `numpy.random.default_rng(20260509)`.

- T1, T2: permute the phase-label vector over the included sūras (marginals preserved exactly).
- T3: permute phase labels **within each mixed stratum** independently.

One-sided p with the standard add-one correction: `p = (1 + #{Δ_perm ≥ Δ_obs}) / (1 + N_perm)`.

**Tie rule.** For each cell the fraction of permutations with `Δ_perm == Δ_obs` exactly is computed. **If
that fraction exceeds 0.50, the cell's p is replaced by an exact one-sided Fisher p** on the 2×2 token
table (phase × {AFF, BIO}) and the cell is flagged `EXACT`.

## 6. Additional pre-committed arms

- **6.1 mawlā-ablation.** Re-run T1 and T2 with the `mawlā` lemmas removed from AFF. H-NEW-267 already
  owns `mwl`; if the result needs *mawlā*, it is a re-derivation of H-NEW-267 and will be labelled so.
- **6.2 Yūsuf-ablation.** Re-run T1 and T2 with Sūra 12 removed, since four of the seven `<ixowapN` tokens
  are its biological brothers.
- **6.3 walad-sense split.** Partition `walad` tokens into DIVINE and non-DIVINE by Rater A, and report
  T1/T2 on the non-DIVINE remainder. This separates the kinship reading from the Christology reading.

These three are **descriptive ablations, not inferential cells**; they consume no Bonferroni slots and
cannot change the verdict. They exist to attribute it.

## 7. Bonferroni, decision rule, verdict ladder

**Family**: 3 tests × 4 channels × 2 verdict-bearing rules-tuples (R1, R3) = **k = 24**.
**α_bon = 0.05 / 24 = 0.00208333**. (R2 is diagnostic and consumes no slot. This α is *tighter* than the
union question requires, because the verdict rule below is an intersection over channels; tightening is
self-verifying per `feedback_bonferroni_tightening_vs_loosening`.)

**A CELL PASSES** iff `Δ_obs > 0` **AND** `p < 0.00208333`.

**A TEST PASSES under a rules-tuple** iff **all four of its channels pass** — i.e. the worst channel passes.

**VERDICT LADDER — evaluated strictly in order; the first matching rung is the verdict:**

1. **NULL** — if T1 does not pass under R1. *(Then state MDE and power, §7.1.)*
2. **RESTATES THE HIJRA** — if T1 passes under R1 but **T2 does not pass under R1**. The register confound
   stands; the phrase goes in the finding's title.
3. **PROXY-DEPENDENT** — if T2 passes under R1 but **not** under R3. The result exists only in the
   unaudited word list.
4. **PASS-DIRECTED (weak within-register)** — if T2 passes under both R1 and R3 but **T3 fails** in the
   RATIO channel under R1.
5. **PASS-WITHIN-REGISTER** — if T2 passes under R1 and R3 **and** T3's RATIO channel passes under R1.

The ladder is exhaustive and mutually exclusive. Nothing else may be published as the verdict.

### 7.1 Power (mandatory if a NULL is published)

For the headline test T2, in every channel and under R1, the **minimum detectable effect** is estimated by
adding a constant δ to the Medinan sūras' per-sūra contrast, sweeping δ upward, and running 500 simulated
permutation tests per δ. The MDE is the smallest δ reaching `p < α_bon` in ≥80 % of simulations. Reported
in the channel's own units **and** as a multiple of the observed Δ.

## 8. Classical anchor — a declared change of role

The *muʾākhāt* (brothering) tradition. `data/baseline-corpora/raw/sira-ibn-hisham.txt` has been read by
this project **only as a corpus baseline** — a bag of Arabic prose for length- and register-matching.
**Using it as a historical source is a change of role and is declared here as such.**

Located by grep, reported as line locators only:

- line **8582** — chapter heading `المؤاخاة بين المهاجرين والأنصار` ("the brothering between the Muhājirūn and the Anṣār")
- lines **8583–8623** — the *muʾākhāt* pericope, opening `قال ابن إسحاق: وآخى رسول الله ﷺ بين أصحابه`
- lines **23313–23315** — a second notice naming pairs

**What this may and may not be used for.** It may be used for one thing only: to establish that the
brothering tradition **exists in the sīra and is placed after the Hijra**, which is what makes §5.3's
directional lock a prediction rather than a guess. It is **not** evidence that the Qurʾānic vocabulary
shifted, it is **not** dated independently of the text it accompanies, and no historicity claim is made.
No citation is reported that was not opened at the line given. Per the death-date rule, note that Ibn
Hishām (d. 218/833) is a recension of Ibn Isḥāq (d. 150/767) and the passage above is attributed in the
text itself to Ibn Isḥāq (`قال ابن إسحاق`).

## 9. Forking-paths log

Every choice made before the run, and the reason.

1. **Step-0 grep run before any design** (§0). Result: no dedicated finding exists; H-NEW-267 already owns
   `mwl`; `kinship-vocabulary.md` H-K1 already contradicts F-20's premise. *This entry is the check that
   determines whether to run at all, and it is logged before the entries about how to run.*
2. **Register × phase crosstab computed before locking the design** (§4) — an outcome-free feasibility
   check on two label files. It changed the design: the primary within-register arm became an **ablation**
   rather than a stratified permutation, because LEGAL and NARRATIVE are perfectly collinear with phase.
3. **QAC lemma census computed before locking** (§2.2). Disclosed in full at §2.1. Fixed the inventory.
   No phase split was computed.
4. **Lemma level chosen as PRIMARY over root level.** Root `rHm` carries 339 tokens of which 12 are the
   intended `>aroHaAm`; root `wly` carries 232 of which 86 are `waliY~`. Root-level counting would measure
   *raḥma* and *tawallā*. R2 retains root level as a *contamination diagnostic* so the size of this choice
   is reported rather than hidden.
5. **Contrast (AFF − BIO) chosen as the statistic** rather than two separate one-class tests, because F-20
   claims **complementary distribution**, which is a claim about the contrast. The RATIO channel makes the
   contrast length-free.
6. **Four channels, worst-is-headline**, per H-NEW-3010 (70× p-swing) and H-NEW-3040 (verdict flip, 3 PASS
   / 5 NULL). No channel is privileged.
7. **α_bon = 0.05/24** rather than 0.05/12: the verdict rule is an intersection over channels, so k=12
   would have sufficed for the union question; 24 is chosen because tightening is self-verifying.
8. **Direction locked to Δ > 0** on four independent grounds (§5.3), one of which (ground 4) predicts the
   right sign for a reason that would *falsify* the hypothesis's interpretation. That asymmetry is why
   arm 6.3 exists.
9. **Second rater chosen as the Sahih International translation** rather than a second hand pass by me.
   No Arabic lexicon is on disk (`find data -iname '*lex*' -o -iname '*lane*' -o -iname '*dict*'` returns
   nothing), so the translator is the only independent human sense-judgement available. Precedent:
   H-NEW-3020's Jeffery vs al-Suyūṭī κ = 0.386.
10. **Ablations 6.1–6.3 declared as descriptive, consuming no Bonferroni slots**, so that they cannot be
    used to rescue a failing verdict.
11. **Verdict ladder ordered so that the CBM outcome has a named rung** (rung 2, RESTATES THE HIJRA) with
    a mandated title change. The failure mode this project's frontier map predicted is the one made
    easiest to report.
12. **Not done, and why**: no verse-level register instrument was built. Building one would have meant
    hand-assigning register markers — precisely the defect under audit in this lane — and it is left as
    stated future work rather than smuggled in as a rescue arm.

## 10. Run discipline

- Immutable run directory `runs/h-new-3090/<UTC>/` created with `os.makedirs(..., exist_ok=False)`;
  every artefact written with `open(path, 'x')`. **No run directory is ever deleted.**
- This file is SHA-256'd and the digest embedded in `scripts/h-new-3090.py` as `EXPECTED_PREREG_SHA`,
  verified at runtime with `SystemExit` on mismatch.
- **This file is never edited after the run**, for any reason including to correct an error in it.
  Corrections go in the finding.
- The script's verdict function is diffed against §7 line by line before the run.
