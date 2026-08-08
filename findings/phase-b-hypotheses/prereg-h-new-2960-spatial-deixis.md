---
title: "Pre-registration — H-NEW-2960: the spatial-deixis census, and whether proximal/distal tracks this-world vs Hereafter"
author: Waiel Al-Shujaa
date: 2026-08-08
status: PRE-REGISTERED — locked before any contingency cell was computed
frontier_item: F-4 (HANDOFF/FRONTIER-MAP-2026-08-07.md:206)
method_parents: [findings/UNIT-DRIFT-DEFECT.md, findings/PROXY-CLAIMS.md, findings/ABSENCE-CLAIMS.md]
model_finding: findings/phase-b-hypotheses/h-new-2950-sajdah-loci.md
script_path: findings/phase-b-hypotheses/scripts/h-new-2960.py
seed_primary: 20260509
seed_replication: 20260519
---

# H-NEW-2960 — pre-registration

## 0. Two deliverables of different epistemic kinds

**Deliverable 1 — the proximal/distal census — is documentary, not inferential.** It partitions
the 1,059 QAC `POS:DEM` segments by a morphological rule and enumerates the result. It has no
null model, no direction and no p-value. It was executed before this pre-registration was
written; registering a census would be theatre. Its numbers appear in §2 because the inferential
design is built on top of them and a reader must be able to see exactly what was known when the
direction was locked.

**Deliverable 2 — the deixis × topical-frame test — is inferential and is what this document
locks.** Everything in §§3–9 was fixed before any contingency cell, odds ratio or p-value
existed.

**What was looked at before locking, stated so it cannot be discovered later** (garden-of-forking-paths
log, per `feedback_specialist_judgment_overrides_team_lead_method` discipline):

| looked at | why it is not peeking |
|:--|:--|
| `POS:DEM` = 1,059, and the full FORM × LEM cross-tab | Deliverable 1. It is the census. |
| the prefix profile of DEM-bearing words (`ka+` on 126 of them) | instrument calibration — it determines that a robustness arm is needed at all |
| `POS:INL` occurs in exactly 29 surahs, all at verse 1 (Q 42 also at verse 2) | confirms the muqaṭṭaʿāt set is derivable in code rather than hand-typed |
| lemma inventories of `ROOT:Axr` and `ROOT:dnw` | instrument calibration — confirms which lemma strings QAC actually emits |
| **the marginals of the primary 2×2**: 15 proximal / 34 distal; 31 ESCH-frame / 18 DUNYA-frame; N = 49 | **the marginals are ancillary.** The primary test is conditional on them (Fisher) or holds them fixed by construction (the permutation null). Seeing a margin does not constrain a cell. This was measured to decide whether the test is worth running at all, and it is recorded here because the honest place for a power check is before the lock, not after. |
| **not looked at:** any cell of any contingency table, any odds ratio, any p-value | — |

---

## 1. The question, and the frontier claim being tested

`HANDOFF/FRONTIER-MAP-2026-08-07.md:206` (F-4):

> Proximal demonstratives cluster on present/this-world referents, distal on the Hereafter and
> on scripture-as-object (`dhālika l-kitāb`).

Its own stated confound is that `dhālika l-kitāb` and the muqaṭṭaʿāt-opening formulae will
dominate the distal count, and its own prior is *"CONFIRMED but at risk of CBM: the effect may be
entirely carried by ~20 formulaic phrases."*

---

## 2. The deixis partition — a morphological rule, not a list

**The rule, stated as a function:**

> **DEIXIS(t) = DISTAL if the `FORM` of the `POS:DEM` segment ends in the addressee-kāf enclitic;
> PROXIMAL otherwise.**
>
> Regex, in Buckwalter as QAC emits it: `(?:ka|ki|kumo|kumu|kumaA|kum|kun~a)$`

This is the classical Arabic criterion. The *kāf al-khiṭāb* on `dhāli-**ka**`, `til-**ka**`,
`ulāʾi-**ka**`, `dhāli-**kum**` is what marks a demonstrative as pointing away from the speaker
and toward (or beyond) the addressee; its absence leaves the bare proximal base with the
*hāʾ al-tanbīh* — `hā-dhā`, `hā-dhihi`, `hā-ʾulāʾi`. **No surah, verse, lemma or form is
hard-coded.** `PROXY-CLAIMS.md` §3 Screen A flags "any hard-coded list of forms that is not
produced by a rule in code"; this design has none, and that is deliberate.

**Verification against an independent partition, run before locking.** Partitioning instead by
QAC *lemma* — proximal {`ha` *aA`, `*aA`, `ha` *a` n`, `ha` tayon`, `hunaA`, `ha` ka*aA`},
distal {`*a` lik`, `>uwla` ^}ik`, `>uwlaA^'`, `tilokum`, `*a` nik`} — gives **729 distal / 330
proximal, identical, with zero disagreements on 1,059 tokens.** Two independently constructed
partitions agreeing exactly is worth more than either alone (`UNIT-DRIFT-DEFECT.md` §8). The
regex is the registered instrument; the lemma partition is reported as its check.

**Exact QAC matching, locked.** A segment enters the inventory iff its `FEATURES` field contains
the literal substring `POS:DEM`. Nothing is matched on Arabic script or on Buckwalter substrings
of the surface form; the brief's rule — *lemma-disambiguated, never raw substring matching* — is
honoured by matching the annotation, not the text.

**Two asymmetries in QAC's `DEM` category, declared now so they cannot be presented later as
results:**

1. **The locative axis is one-sided.** `hunā` ("here", 4 tokens) is tagged `POS:DEM`;
   `hunālika` ("there") is tagged `POS:T` (8) and `POS:LOC` (1) and is therefore **not in the
   inventory at all**. The proximal count carries a locative that the distal count does not.
   Four tokens out of 1,059; disclosed, not corrected, because correcting it would mean
   hand-adding a form.
2. **`hākadhā`** ("thus", 1 token) contains a *kāf* that is not the addressee-kāf. The rule is a
   **suffix** match, so `ha` ka*aA` — which ends in `*aA` — is correctly left proximal. This was
   checked before locking and is the reason the rule is anchored to the end of the form.

---

## 3. The confound decision, made before counting — SEPARATELY MODEL, DO NOT EXCLUDE

The brief requires this decision to be registered before any count. **It is: model the formulae,
do not delete them.**

Two reasons, and the second is the operative one.

1. **Excluding is itself a hand-assignment.** "Drop the opening formulae" requires me to decide
   which phrases are formulae, which is a curated list under a different name
   (`PROXY-CLAIMS.md` §3 Screen A).
2. **Deletion cannot answer the question the frontier map actually asks.** Its prior is that the
   effect *is* the formulae. Deleting them and reporting what remains discards the measurement of
   how much they carried. The registered design instead measures that quantity directly (§7).

The primary tests therefore run on the **full** demonstrative inventory. Four registered
robustness arms reduce it, each by a rule stated in code:

| arm | rule | tokens removed (measured before locking) |
|:--|:--|--:|
| **D1** | drop DEM tokens in **verses 1–3 of every surah containing a `POS:INL` segment** — the muqaṭṭaʿāt openings, derived in code from QAC, not from a stored list of 29 surahs | **17** |
| **D2** | drop DEM tokens whose word carries a `ka+` prefix segment — *ka-dhālika* "thus", a manner connective and not a spatial pointer | **126** |
| **D3** | drop the top-*m* most frequent **DEM phrase types** corpus-wide, *m* ∈ {1, 2, 3, 5, 10} | reported at run |
| **D4** | D1 ∧ D2 jointly | — |

**D3 is the arm that decides interpretation**, and its phrase type is defined mechanically:

> **phrase type = (FORM of the DEM segment, FORM of the first `STEM` segment of the next word in
> the same verse).** A DEM that is verse-final has next-word `∅`. Types are ranked by
> **corpus-wide** token frequency over all 1,059 DEM tokens — **not** by frequency within the
> eligible test set, so the ranking cannot be tuned by the test.

---

## 4. The referent-classification rule — and an explicit statement of what I cannot write

**I cannot write a function that classifies the *referent* of a demonstrative, and I am not going
to pretend otherwise.**

The referent of an anaphoric demonstrative is a discourse entity. Recovering it requires either
a dependency parse with coreference resolution, or human judgement. The judgement route is
precisely the defect `PROXY-CLAIMS.md` catalogues and is refused here. The parse route is
unavailable on disk, and that absence is stated with its search per `ABSENCE-CLAIMS.md` §4:

> **Search.** `ls -la data/syntax/` returns exactly one file,
> `data/syntax/UD-QURAN-SOURCE.md` (1,754 bytes), whose own front-matter reads
> `status: external reproducibility input; binary not committed`. No treebank, CoNLL-U file or
> dependency table is present in that directory. **Positive control on the search:** the same
> `ls` in `data/morphology/` returns the QAC file this design does use, so the command and the
> path convention are working. Scope: `data/syntax/` only. This is an **ABSENT** verdict for a
> dependency parse *in that directory*, not a claim that no parse could be produced.

**What I can write as a function is the verse's topical FRAME**, and the substitution of frame
for referent is itself an empirical claim, declared here per `PROXY-CLAIMS.md` §1:

> **The claim being substituted in: that a demonstrative in a verse whose topical frame is the
> Hereafter is more likely to have a Hereafter referent. This is untested and I do not test it.**
> Every verdict below is a verdict about **frame**, not about **referent**, and the finding will
> say so in its headline. F-4 as written is therefore **not** decided by this run; a weakened
> version of it is.

### 4.1 C1 — the closed antonym pair (PRIMARY instrument)

The corpus lexicalises the this-world/Hereafter opposition itself, in one matched pair:
*al-ḥayāt al-**dunyā*** against *al-**ākhira***. Using it requires naming no third word.

> **frame(v) = ESCH** if verse *v* contains ≥1 segment with `LEM:A^xir` and none with
> `LEM:d~unoyaA`;
> **frame(v) = DUNYA** if the reverse;
> **UNCLASSIFIED** if both or neither.

Free parameters: **none**. Curated members: **none beyond the pair itself**, and the pair is the
text's own antithesis rather than my selection from a field of candidates. Both are matched on
`LEM:`, so `ākhar` "another" (`LEM:A^xar`, 70 tokens) is excluded by lemma and not by my
judgement — this is the brief's lemma-disambiguation requirement doing real work, since a
substring search on the root ʾ-KH-R would have swept it in.

**Sensitivity S1, registered now.** The whole lemma `A^xir` also carries `ākhirīn` "later
generations" (10 tokens), which is not eschatological. Restricting the ESCH marker to the
**feminine-singular form class** — `FORM` beginning `'aAxirap` — is a second mechanical rule and
gives a smaller, cleaner marker set. **Both are run and both are reported.** Per
`UNIT-DRIFT-DEFECT.md` §6 rule 6: if the two disagree, both are reported and the stricter is
taken.

### 4.2 C2 / C3 — the generated lexicon (SECONDARY instruments, for power)

C1 classifies only 49 demonstrative tokens. That is thin, and the honest response is not to
curate a bigger word list but to **generate** one (`PROXY-CLAIMS.md` §4, final clause).

1. **Training set:** the C1-classified verses only — verses with exactly one of the two seed
   lemmas. Verses carrying both are excluded from training.
2. **Candidate lemmas:** every `LEM:` value on a segment whose `POS` is in {`N`, `PN`, `ADJ`,
   `V`}. **`POS:DEM`, `POS:PRON` and every function POS are excluded by construction**, so the
   generated lexicon cannot contain a demonstrative and cannot learn the thing being tested.
   The two seed lemmas are removed from the output lexicon so the expansion adds new vocabulary
   rather than restating its own seeds.
3. **Score:** the Monroe–Colaresi–Quinn informative-Dirichlet log-odds z, with prior counts
   taken from the corpus-wide lemma distribution and α₀ = 100.
4. **Lexicon:** the top *k* lemmas by z in each direction. **k is a declared free parameter and
   is reported at two values, k = 25 (C2) and k = 50 (C3)**, per `UNIT-DRIFT-DEFECT.md` §6.1
   requirement 2.
5. **Classification:** for a verse *v*, let *e* and *d* be its token counts from the ESCH and
   DUNYA lexicons. `frame(v) = ESCH` if *e* > *d*; `DUNYA` if *d* > *e*; `UNCLASSIFIED` if equal
   (including 0–0).

---

## 5. The statistic, the null, and why the null is clustered

**Statistic:** `S = the number of DISTAL tokens in ESCH-frame verses` — a raw integer count, the
[distal, ESCH] cell of the 2×2. Odds ratio and the full table are reported alongside.

**The clustering problem, and it is real.** A verse can contain several demonstratives (the 49
C1-eligible tokens sit in 42 verses). Tokens in one verse share a frame **by construction**, so
they are not independent observations and Fisher's exact test — which assumes they are — will be
anticonservative.

> **Primary p is therefore a verse-clustered permutation:** permute the ESCH/DUNYA labels across
> the eligible **verses**, holding the number of ESCH and DUNYA verses fixed at their observed
> values; each verse's demonstrative tokens travel with it; recompute S. Both margins of the
> token table are then free to move exactly as clustering allows, which is the point.
> **200,000 draws, seed 20260509**, replication seed **20260519**.
>
> `p = (1 + #{S* ≥ S_obs}) / (1 + N_draws)`.

**Fisher's exact test is reported alongside as the unclustered comparison, and is not the gate.**
If the two disagree the permutation is taken, because it is the one whose assumptions hold.

**Direction, locked now:** one-sided **upper** on S. **Proximal → this-world, distal → Hereafter**,
exactly as the brief instructs. A result in the opposite direction is reported as such and cannot
pass.

---

## 6. Unit-drift and proxy screens, applied to this design before it was built

| screen | status |
|:--|:--|
| **A — is the statistic a ratio with a unit count in the denominator?** | **No.** S is an integer cell count of a contingency table. There is no density, no rate, no per-verse normalisation. This target was chosen because the defect structurally cannot reach it. |
| **B — ordering or grouping with unit-size drift?** | The comparison is categorical, not positional. Long verses do carry more demonstratives *and* more marker words, which would matter for a density; for a permutation of verse labels holding the verse set fixed, each verse contributes its own token count identically under null and observation. **Registered diagnostic:** report mean verse word-count in ESCH-frame vs DUNYA-frame eligible verses, so a reader can see the channel even though the statistic does not divide by it. |
| **C — is any quantity hand-assigned?** | The deixis partition is a regex (§2). The muqaṭṭaʿāt set is derived from `POS:INL` (§3). The C1 frame rule names one antonym pair and nothing else; C2/C3 are generated (§4.2). **The naming of the pair is the one irreducible choice, and §4 states it as a claim rather than burying it.** |

---

## 7. Gates and the verdict logic — locked

**Registered primary family: three tests — C1, C2, C3.** Bonferroni α = 0.05 / 3 =
**0.0166667**.

**C1 is the primary.** The verdict logic, fixed here:

| condition | verdict |
|:--|:--|
| C1 permutation p < 0.0166667, **and** the association still clears the gate after D3 at *m* = 5 | **CONFIRMED** |
| C1 p < 0.0166667, **but** it fails the gate after D3 at *m* = 5 | **CONFIRMED-BUT-FORMULAIC** |
| C1 p ≥ 0.0166667 | **NULL** — whatever C2 and C3 do |
| C1 fails, C2 **and** C3 both pass | **NULL on the registered primary**, with the secondary reported as a **descriptive observation requiring its own prospective pre-registration.** It cannot rescue, upgrade or create a verdict. |
| S in the direction opposite to the lock | **NULL, direction reversed** — reported with the reversal stated in the headline |

**The D1–D4 arms are diagnostics of an association, not independent tests.** They are not in the
Bonferroni family, and none of them can produce a PASS that the primary did not.

**Novelty gate**, matching the house convention: min(1, 3p) < 0.005.

---

## 8. The power statement, written before the numbers exist

**N = 49 demonstrative tokens in 42 verses on the primary instrument. This test is
underpowered, and I am recording that now rather than after a null.**

The permutation floor is `1/(1+200000) = 5.0 × 10⁻⁶`, so p-resolution is not the binding
constraint; **power is.** With 42 eligible verses split 31/18 at token level, only a large
association will clear α = 0.0167.

> **A NULL on C1 is not evidence that the deictic axis is unrelated to eschatological reference.**
> It is evidence that any relation is not large enough for 49 tokens under a verse-clustered null
> to reveal. This sentence is written before any cell is computed and will be repeated unchanged
> in the finding.

Equally: **the census stands regardless.** Deliverable 1 is not conditioned on Deliverable 2 and
does not weaken if every inference nulls.

---

## 9. Run discipline

- Immutable run directory `findings/phase-b-hypotheses/runs/h-new-2960/<UTC-timestamp>/`,
  created with `os.makedirs(..., exist_ok=False)`; every file inside written with mode `'x'`.
- **No file inside the run directory is ever rewritten** (`UNIT-DRIFT-DEFECT.md` §7). There are
  no checkpoints; if any are added they go outside the run directory.
- **No run directory is ever deleted.**
- Manifest carries repo-relative paths only, plus the git commit at run time, the QAC SHA-256,
  and the SHA-256 of this file.
- **The SHA-256 of this pre-registration is embedded as a literal in the script and verified at
  runtime; a mismatch aborts before the run directory is created.**
- The finding file is not written to its final path until the run directory exists.

**Instrument SHA-256** — `data/morphology/quranic-corpus-morphology-0.4.txt` =
`a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46`.

---

*Locked 2026-08-08 by Waiel Al-Shujaa, before any contingency cell existed.
Bismillāhi al-Raḥmāni al-Raḥīm.*
