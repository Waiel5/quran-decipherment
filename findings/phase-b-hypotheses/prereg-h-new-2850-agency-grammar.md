---
id: H-NEW-2850
title: "Pre-registration — does derivational verb form track the grammatical subject's agency class?"
date: 2026-08-07
author: Waiel Al-Shujaa
status: PRE-REGISTERED — locked before any form × subject-type quantity was computed
family: MORPH-2026-08-07-B
parents: [H-NEW-2540, H-NEW-2600, H-NEW-2650]
---

# Pre-registration — H-NEW-2850

**Nothing in §6–§9 may be changed after this file is committed. The analysis script
embeds this file's SHA-256 as a literal and aborts on mismatch.**

---

## 0. Provenance, and the exposure log — read this before anything else

This pre-registration is **not fully blind**, and the parts that are not blind are named
here rather than discovered later by an auditor.

### 0.1 Where the hypothesis came from

`h-new-2540-form-v-valency.md` §3 records three roots whose form alternation coincides with a
divine/human split in the subject or object:

- **ك ب ر** — Form II occurs 4× with God as its object; Form V occurs 2×, objectless, and both
  are the sin of arrogance.
- **ط ه ر** — Q 5:6 contains *li-yuṭahhira-kum* (Form II, God purifies you) and *fa-ṭṭahharū*
  (Form V, purify yourselves) in one verse.
- **ي س ر** — Q 54:17 *yassarnā l-Qurʾāna* against Q 73:20 *mā tayassara min al-Qurʾān*.

**Three roots is an anecdote.** This test asks whether the pattern is general.

### 0.2 The direction is locked from doctrine, not from those three roots

Using the motivating cases to fix the predicted direction would be circular. The directions in
§6 are therefore derived **only** from the muṭāwaʿa/causative doctrine already relied on by
H-NEW-2540 and H-NEW-2600, restated here in argument form:

> Forms II (*faʿʿala*) and IV (*afʿala*) are causative/factitive relative to Form I: they add
> an **external causer** argument. The *muṭāwiʿ* forms (V for II, VI for III, VII and VIII for
> I) denote the undergoing of that action by the affected participant, with the causer removed
> from the syntax. The argument position an external causer occupies therefore **exists** in
> the causative member of each pair and **does not exist** in the *muṭāwiʿ* member.

The prediction follows only if an external causer is, in this corpus, more often divine than a
non-external agent is. **That premise is about the corpus's content, not about Arabic**, and it
is stated as a premise rather than smuggled in. It is exactly the premise the transitivity
conditioning in §8 exists to interrogate.

### 0.3 Everything I inspected before locking — complete list

Design of a subject classifier requires looking at the corpus. I looked at the following, all
of it on the **subject side** or **counts only**, and I list it so that any of it can be held
against the result:

1. QAC v0.4 file format; total verb segments **19,356**; active (non-`PASS`) verbs with a root
   and exactly one agreement feature, **18,216**.
2. Part-of-speech and case of the word immediately following a verb (all 19,356 verbs).
3. Lemma frequency of post-verbal nominative nominals — top 45 lemmas, 487 distinct.
4. The 142 tokens of `rab~` in the nominative immediately after a verb; first 60 read
   individually to check for the human-master sense.
5. **`(verb form) × (grammatical person)` for all 18,216 active verbs.** *This is the exposure
   that matters and it is stated in full below.*
6. Coverage of four candidate explicit-subject window rules, overall and **by verb form**.
7. Agreement between the forward-window and backward-window explicit-subject rules on the 317
   verbs where both fire: **0.7571**.
8. Counts of eligible roots per form pair at ≥1 and ≥2 tokens, under two candidate classifiers
   — **token counts only, with no divine/non-divine rate attached**.
9. Count of 1P verbs with a *q-w-l* verb earlier in the same verse (400 of 1,832) and of
   2nd-person verbs in a verse carrying a vocative plus a divine name (461 of 4,455).
10. EQTB `rel_label` vocabulary; `Subj` edges whose head is a verb (4,136, of which only ~630
    are nominal) — checked as a candidate second subject channel and **rejected on coverage**.

### 0.4 The exposure that is not blind, stated plainly

Item 5 above is a table I should describe exactly, because it anticipates part of the result:

| form | 1st person | 2nd person | 3rd person | total | share 1st |
|:--|--:|--:|--:|--:|--:|
| I | 1271 | 2902 | 7522 | 11695 | 0.109 |
| II | 289 | 236 | 635 | 1160 | **0.249** |
| III | 26 | 81 | 203 | 310 | 0.084 |
| IV | 680 | 649 | 1874 | 3203 | **0.212** |
| V | 28 | 113 | 263 | 404 | **0.069** |
| VI | 1 | 26 | 50 | 77 | 0.013 |
| VII | 0 | 7 | 44 | 51 | 0.000 |
| VIII | 66 | 337 | 545 | 948 | 0.070 |
| X | 18 | 103 | 233 | 354 | 0.051 |

Because the classifier in §4 maps **1P → DIVINE** (the majestic *naḥnu*), this table largely
determines the outcome of any arm that uses the 1P channel. **I saw it before locking.**

Three consequences, all binding:

1. **The locked directions in §6 are unchanged by it.** They were fixed by §0.2 and by the task
   as posed, both of which predate this measurement. The reader may verify that the doctrine
   argument does not reference person at all.
2. **The classifier that uses the person channel (`C-WIDE`, §4.4) is demoted to a registered
   secondary.** The primary confirmatory classifier is `C-STRICT`, which uses **no person
   information whatsoever** and whose outcome no table I inspected anticipates.
3. **A person-composition arm is registered explicitly** (§7.4) so that the person effect is
   *reported as itself* rather than laundered through an agency label.

### 0.5 What I did not compute

No divine-rate by form. No divine-rate by (root, form). No arm gap. No test statistic. No
p-value. No census roster. The first time any of those exists will be inside the immutable run
directory produced by the script that verifies this file's hash.

---

## 1. The question

> Does Arabic derivational verb form correlate with the **agency class of the grammatical
> subject** — divine versus human/other — beyond what transitivity alone explains?

The alternative to be excluded is the mundane one: divine subjects may simply take more objects
because divine action is narrated transitively as a matter of content, and form already tracks
transitivity (H-NEW-2540, H-NEW-2600, H-NEW-2650). If conditioning on transitivity removes the
association, the answer is **"the three showcase roots are vivid but not general"**, and that is
a full result, not a failure.

---

## 2. Frozen inputs

Verified by SHA-256 at runtime; `SystemExit` on any mismatch.

| input | path | SHA-256 |
|:--|:--|:--|
| QAC v0.4 morphology | `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| Quran text (no tashkeel) | `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |
| revelation order | `data/revelation-order.csv` | `74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7` |
| EQTB `Quranic.csv` *(secondary only)* | supplied by path at run time | `a303c24cf51b90f6cd5eb0fb25d6c591977a7797743d16e0dedc76a5af5ae0b7` |

The QAC hash is byte-identical to the one in the H-NEW-2540/2600/2650 run manifests, so every
comparison here is against the same corpus the parents used.

**EQTB is contamination-limited for morphology questions** — its syntax was initially produced
by a parser whose inputs included `verb_form` (H-NEW-2540 §7.2). It is used **only** as a
secondary transitivity variable (§5.2), never for the subject variable, and never as primary.

---

## 3. Unit of analysis

One row per **active verb token**: a QAC segment with `POS:V`, without `|PASS`, carrying a
`ROOT:` feature and exactly one person/gender/number agreement token. The script asserts
agreement multiplicity `== 1` for every verb and aborts otherwise (inherited from H-NEW-2650
§2.2, where this was verified for all 19,356 verbs).

Verb form is read from the QAC `(II)`…`(XII)` marker; absence of a marker means Form I.

---

## 4. Subject classification — the locked rules

Every rule below is mechanical. **None of them can see the verb's derivational form**, so none
can introduce a form-correlated bias by construction. This is asserted in code, not claimed in
prose: the classifier functions receive no form argument.

### 4.1 The divine lexicon (closed, locked)

`L_div = { {ll~ah , rab~ , raHoma`n }` (Buckwalter lemmas: Allāh, *rabb*, al-Raḥmān).

**Why so small.** Most of the ninety-nine names are also used of creatures in this corpus
(*ʿazīz* of the ruler of Egypt, *raʾūf*/*raḥīm* of the Prophet at Q 9:128, *ʿalīm*, *ḥalīm*,
*karīm*), so a wide lexicon buys coverage with misclassification. `rab~` retains a known
human-master sense (Q 12:23, 12:41–42). **The script counts every `rab~` classified as a divine
subject that falls inside Q 12:20–12:50 and reports it as the measured error bound**; no token
is hand-removed.

### 4.2 `S-EXPL` — explicit nominal subject (no person information used)

For a verb at word *w* of verse *(s,v)* whose agreement is **3rd person**:

1. Scan words *w+1, w+2, …* within the same verse.
2. Stop at the first word that contains a verb segment (clause boundary) — no subject found.
3. Stop at the first word carrying **exactly one** case-marked segment. If that case is `NOM`,
   that word's lemma is the subject; if `ACC` or `GEN`, no post-verbal subject is found.
4. Words with zero or more than one case-marked segment are skipped, not terminated on.

Label: **DIVINE** iff the lemma ∈ `L_div`, else **NONDIVINE**.

Restricting to 3rd person is a precision requirement, not a convenience: a nominative nominal
following a 1P or 2nd-person verb cannot be that verb's subject.

### 4.3 `S-EXPL-EXT` — the extended explicit rule (registered sensitivity only)

`S-EXPL`, and if it finds nothing then, in order:

- **BWD**: scan backwards from *w−1*, stopping at the first verb-bearing word; if the first
  word carrying exactly one case-marked segment is `NOM`, take it (SV order).
- **PROP**: else inherit the subject of the nearest preceding verb *in the same verse* that has
  an explicit subject of its own **and identical agreement** (coordination shares a subject).

`S-EXPL` and `S-EXPL-EXT` disagree; the forward-versus-backward agreement was measured at
**0.7571** on the 317 verbs where both fire (§0.3 item 7), and the script recomputes and reports
it. **`S-EXPL-EXT` is a sensitivity arm and is not part of the confirmatory family.**

### 4.4 The person channels, and the two classifiers

- **`S-1P`** — agreement `1P` → **DIVINE**. The majestic *naḥnu*.
- **`S-2P`** — agreement 2nd person → **NONDIVINE**. An addressee in this corpus is a creature.
- **1S** → **UNCLASSIFIED**. First-person singular is God at Q 51:56 and a human at hundreds of
  other places, with no mechanical discriminator. Declared ambiguous; counted; not used.
- **3rd person with no explicit subject** → **UNCLASSIFIED**. Resolving *huwa* to God requires
  coreference, which no rule here performs. Declared ambiguous; counted; not used.

Two classifiers are locked:

| classifier | rules, in priority order | uses person? | role |
|:--|:--|:--|:--|
| **`C-STRICT`** | `S-EXPL` | **no** | **PRIMARY confirmatory** |
| **`C-WIDE`** | `S-EXPL` → `S-1P` → `S-2P` | yes | secondary confirmatory |

`C-STRICT` is primary **because of §0.4**: it is the arm no table I inspected anticipates. It
is also the arm with the least power, and that trade is deliberate and is not to be revisited
after seeing the result.

### 4.5 Known error modes of `S-1P` and `S-2P`, declared in advance

- **Quoted human "we".** *qālū āmannā* (Q 2:14) is a human 1P inside quoted speech and
  `S-1P` will call it DIVINE. A *q-w-l*-in-verse test excludes 400 of 1,832 1P verbs but
  over-excludes badly — Q 2:58 *naghfir lakum* is divine and follows God's own *qulnā*. **The
  test is therefore registered as a reported sensitivity (`S-1P-QCUT`), not as the rule.**
- **Duʿāʾ addressed to God.** *rabbanā ighfir lanā* is a 2nd-person verb whose subject is God;
  `S-2P` will call it NONDIVINE. 461 of 4,455 2nd-person verbs sit in a verse carrying both a
  vocative and a divine name; this count is reported as the upper bound on that error, and the
  arm excluding them is reported as sensitivity `S-2P-VCUT`.

Both sensitivities are reported for every arm. Neither may replace the locked rule.

### 4.6 Inter-rule agreement — what will be reported

1. `S-EXPL`(FWD) vs BWD on verbs where both fire — the number quoted in §0.3 item 7.
2. `S-EXPL` vs `S-EXPL-EXT` on the subset where the extension found a *different* subject.
3. `C-STRICT` vs `C-WIDE` on their overlap (identical by construction — reported as such, and
   **not** presented as evidence of anything).
4. `S-EXPL` vs the EQTB `Subj` edge on the tokens where EQTB supplies a nominal subject for a
   verb — a genuinely independent construction, on ~630 tokens. Contamination-flagged.
5. A **blinded validation sample** (§10.3) for human scoring, review columns left blank.

---

## 5. Transitivity

### 5.1 `T1` — overt attached object pronoun (PRIMARY, parser-free)

**`RULE-NEW` of H-NEW-2650 §3, inherited verbatim**, including its `EMPH`/`REL` skip. Over
every post-verb `SUFFIX`-type `PRON` segment, with `f` = surface stripped to bare letters,
`p` = PGN, `s` = slot index, `g` = verb agreement, `a` = aspect:

1. `f` starts `h` or `k` → OBJECT
2. `f` starts `t`, `w`, `y`, `u` → SUBJECT
3. `p = 1S` → OBJECT
4. `p = 1P` → SUBJECT iff `s = 0` and `g = 1P` and `a = PERF`; else OBJECT
5. otherwise → SUBJECT

`T1 = 1` iff at least one clitic classifies as OBJECT. **Coverage is asserted at 100% at
runtime; the script aborts otherwise.**

**The naive rule — discard every following `PRON` whose PGN matches subject agreement — is
forbidden.** H-NEW-2650 §4 measured that it deletes **311 genuine objects at a form-correlated
rate** (FN 0.0752 for Form II against 0.1429 for Form V, 0.1780 for Form VIII).

### 5.2 `T2` — EQTB `Obj` edge (SECONDARY, contaminated)

`T2 = 1` iff some EQTB token carries `rel_label == "Obj"` with `ref_token_id` equal to the
verb's token. Reported second, always flagged, and **never used to overturn a `T1` result**:
because EQTB's parser had `verb_form` among its inputs, stratifying on `T2` partially
stratifies on the predictor and over-controls.

---

## 6. The arms and their locked directions

`G(A→B) = P(divine subject | form A) − P(divine subject | form B)`, within root.

| arm | pair | relation | **locked sign** | reasoning (§0.2) |
|:--|:--|:--|:--:|:--|
| **M1** | II → V | *faʿʿala* → *tafaʿʿala* | **+** | V is the *muṭāwiʿ* of II; the external-causer slot exists in II and not in V |
| **M2** | I → VIII | *faʿala* → *iftaʿala* | **+** | VIII is a *muṭāwiʿ*/middle of I |
| **M3** | III → VI | *fāʿala* → *tafāʿala* | **+** | VI is the reciprocal *muṭāwiʿ* of III; low power expected |
| **C1** | I → II | base → causative | **−** | II **adds** the external causer, so II should carry *more* divine subjects than I |
| **C2** | I → IV | base → causative | **−** | IV **adds** the external causer, so IV should carry *more* divine subjects than I |

**C1 and C2 are the falsification control and they are the reason this design can fail.** They
run in the opposite direction to M1–M3 under the same instrument. This is the same reverse-control
structure H-NEW-2600 registered, and it is registered here for the same reason: a design in
which every arm is predicted positive cannot distinguish a real effect from an instrument that
says yes to everything.

Arms **I → VII** and **IV → VII** are described but **not registered**: H-NEW-2600 §4 found 2
and 0 eligible roots respectively. They will be reported descriptively if data exists.

---

## 7. Statistics and nulls

### 7.1 Eligibility

Within-root pairing, **≥2 classified tokens per form per root**, `PASS` excluded throughout —
identical to H-NEW-2600 and H-NEW-2650. A ≥1-token sensitivity is reported, and is a
sensitivity, not a primary.

### 7.2 Statistics per arm

Inherited verbatim from H-NEW-2540 §2 so that the family remains comparable:

- **Pooled within-root gap** over eligible roots.
- **Weighted smoothed statistic** `T = Σ w_r (p_rA − p_rB) / Σ w_r`, `p = (y+0.5)/(n+1)`,
  `w = 2 n_A n_B / (n_A + n_B)`. The **unsmoothed macro difference is reported beside it**,
  because smoothing biases `T` toward the hypothesis when `n_A ≠ n_B` (H-NEW-2540 §2).
- **Mantel–Haenszel odds ratio** across roots.
- **Exact two-sided binomial sign test** over discordant roots — parameter-free, and the
  primary inferential statistic, as in H-NEW-2650 §5.
- **Null B — margin-preserving token-label permutation.** Within each root, hold `n_A`, `n_B`
  and the root's total DIVINE count fixed and reallocate DIVINE labels at random across that
  root's A ∪ B tokens; recompute `T`. **10,000 permutations, seed 20260509**, replication seed
  **20260519**. Null B is preferred over a root sign-flip null for the reason given in
  H-NEW-2540 §7.7: a sign-flip distribution is symmetric about zero and does not absorb the
  smoothing bias, whereas Null B conditions on the margins and is immune to it by construction.

### 7.3 Multiplicity

Confirmatory family: **5 arms × 2 classifiers × {unconditioned, transitivity-conditioned} = 20
inferences.** Bonferroni α = 0.05/20 = **0.0025**.

**The binding decision gate is the project's stricter novelty gate, raw p < 0.0005**, matching
H-NEW-2600 and H-NEW-2650. Both the exact sign test and Null B must clear it for an arm to
count as PASS. Sensitivities (§4.3, §4.5, ≥1-token, chronology, leave-one-root-out) are
reported and are **not** counted in the family.

### 7.4 The person-composition arm — reported, not laundered

Because §0.4 makes the person channel non-blind, the script reports, for every form,
`P(1P | form)`, `P(2nd | form)`, `P(3rd | form)` with the same within-root pairing and the same
sign test, **labelled as a person-composition result and not as an agency result.** If the
`C-WIDE` arms pass and `C-STRICT` does not, the honest reading is that the corpus's *person
deixis* tracks derivational form, which is a different and weaker claim than the one under test,
and the finding will say so in those words.

---

## 8. The confound that decides this — transitivity conditioning

This is the section the result turns on.

Divine subjects may take more objects because divine action is narrated transitively, and form
already tracks object realization (H-NEW-2540: Form II 74.9% vs Form V 20.3% on EQTB; 0.3516 vs
0.1016 on the parser-free channel). **An agency effect that disappears once transitivity is held
fixed is a restatement of the parent finding, not a new one.**

For every arm and every classifier:

1. **Stratified gap.** Report `G(A→B)` computed **separately within `T1 = 1` and `T1 = 0`**,
   with the eligible-root count and sign test in each stratum.
2. **Cochran–Mantel–Haenszel.** Strata = **(root × `T1`)**. Report `OR_CMH`, the CMH χ² and its
   two-sided p. This is the registered residual.
3. Repeat 1–2 with `T2` in place of `T1`, flagged as EQTB-contaminated and secondary.

**Locked reading:**

- If `OR_CMH` retains the arm's locked direction **and** clears p < 0.0005, the association
  survives transitivity conditioning **for that arm**.
- If `OR_CMH` crosses 1, or reverses, or fails the gate while the unconditioned test passed,
  the arm is recorded as **transitivity-explained**.
- If a stratum is empty or has zero eligible roots, that is reported as *no power in stratum*
  and **must not** be read as either outcome.

---

## 9. The decision rule

Evaluated on `C-STRICT` first (primary), then on `C-WIDE` (secondary). The two verdicts are
reported separately and neither may be used to rescue the other.

- **`INSTRUMENT-CONFOUNDED`** — if **both** C1 and C2 come out with a **positive** gap, i.e. the
  same sign as the muṭāwaʿa arms. The instrument then says yes to everything and **the finding
  is NULL regardless of any other arm**. Pre-committed, exactly as H-NEW-2600 pre-committed its
  own escape hatch.
- **`AGENCY-TRACKED`** — if (a) all five arms' signs match §6, **and** (b) at least one M arm and
  at least one C arm clear p < 0.0005 on **both** the exact sign test and Null B, **and**
  (c) the §8 `OR_CMH` for each of those arms retains its locked direction at p < 0.0005.
- **`AGENCY-TRANSITIVITY-EXPLAINED`** — if (a) and (b) hold but (c) fails.
- **`NULL`** — anything else, including failure for want of power.

**A `NULL` or `AGENCY-TRANSITIVITY-EXPLAINED` verdict is reported with the same prominence,
the same table layout and the same word count as a positive one.** The census in §10 is
delivered in full under every verdict.

**The verdict logic in the script will be diffed line-by-line against this section before any
number is quoted anywhere**, because H-NEW-2600's published verdict was retracted for
implementing a looser rule than it registered.

---

## 10. Deliverables, owed under every verdict

### 10.1 The census roster — owed regardless of outcome

`census-roster.tsv`, one row per **classified** active verb token:

`location · surah · verse · root · form · aspect · agreement · subject_label ·
subject_lemma · rule_fired · T1 · T2 · verse_text`

### 10.2 The dissociation roster — the deliverable the task names

`dissociation-roster.tsv`: **every root** for which the causative member (II or IV) takes a
divine subject and the *muṭāwiʿ* member (V, VI, VII or VIII) does not, **or the reverse**, with
per-root counts for both forms and the **complete list of locations** for every token on both
sides. Perfect dissociations (100%/0%) are marked. Ordered by root; **not** filtered to
"interesting" roots.

### 10.3 Blinded validation sample

`validation-sample.tsv`, stratified by (verb form × subject label), ≤10 per cell, seed 20260509.
Columns `sample_id · verb_location · verb_surface · verse_text` then **blank** review columns
`review_subject_is_divine · review_subject_span · review_notes`. The file carries **no form
label and no rule verdict**; the mapping goes to `validation-key.json`. I will not fill the
review columns in.

### 10.4 Coverage and the ambiguous classes

Reported in full, with counts, per form:

- classified / unclassified, by rule fired;
- **1S** verbs (ambiguous by declaration);
- 3rd-person verbs with no explicit subject (ambiguous by declaration);
- 3rd-person verbs whose forward window terminates on `ACC`/`GEN`;
- 1P verbs with a *q-w-l* verb earlier in the verse (`S-1P-QCUT` candidates);
- 2nd-person verbs in a verse with a vocative and a divine name (`S-2P-VCUT` candidates);
- `rab~`-subject tokens inside Q 12:20–12:50 (the human-master error bound).

### 10.5 The classifiability denominator — the unit-drift clause

`findings/UNIT-DRIFT-DEFECT.md` §5 requires any ratio statistic to declare the drift of its
denominator across the comparison. **The denominator here is the count of *classified* verb
tokens, and classifiability is form-correlated**: measured at 0.084–0.235 across forms for
`S-EXPL` and 0.373–0.532 for `C-WIDE` (§0.3 item 6). Therefore:

1. Coverage by form is quoted **beside** every headline gap, not in a footnote.
2. A **conservative-denominator sensitivity** is run for every arm, in which the denominator is
   **all** active tokens of that (root, form) and every UNCLASSIFIED token is scored
   NON-divine. This can only shrink a divine-rate; if an arm's sign survives it, differential
   classifiability cannot be manufacturing that arm.

---

## 11. Run discipline

- This file's SHA-256 is embedded in the script as a literal and verified at runtime;
  `SystemExit` on mismatch.
- Frozen inputs verified by SHA-256 at runtime (§2).
- Immutable run directory `findings/phase-b-hypotheses/runs/h-new-2850/<UTC>/`, created with
  `os.makedirs(..., exist_ok=False)`; every output opened with mode `'x'`.
- **The script never overwrites a file inside its own run directory** (UNIT-DRIFT-DEFECT §7).
  Any checkpoint goes to a path **outside** the run directory.
- Manifest records **repo-relative** input paths and no tooling identifiers.
- **No run directory is ever deleted**, including a superseded or uncommitted one
  (H-NEW-2540 §8.1).
- Seeds are fixed literals: 20260509 primary, 20260519 replication, 10,000 permutations.
- A determinism re-run is executed and both run directories are retained.

---

## 12. What is claimed, and what is not

**Not claimed under any verdict:**

- That any of this is novel Arabic grammar. Muṭāwaʿa and the causative function of II/IV are
  textbook.
- That it is Qurʾān-specific. There is no matched Classical-Arabic dependency treebank or
  agency-annotated control corpus, and without one nothing here separates a property of this
  corpus from a property of Classical Arabic. Per the project's Phase-B rule this is at best
  **QURAN-INTERNAL SUPPORT**.
- **Any theological significance.** The output is a grammatical fact about a classification of
  grammatical subjects. Interpretation belongs to the reader and to the exegetical tradition,
  and the finding will not supply one.

**Known limits, declared before the run:**

1. The subject classifier is a rule, not ground truth. Its own error rate is unmeasured until
   §10.3 is scored by a qualified human reviewer.
2. `S-1P` and `S-2P` carry the declared errors of §4.5.
3. "Divine subject" is a *referential* class imposed on a *grammatical* variable. A verb whose
   subject is an angel, a prophet acting on God's command, or a personified natural force is
   NONDIVINE here, and reasonable analysts would classify some of those differently.
4. `T1` measures **overt enclitic object realization**, not transitivity. A verb with a full
   nominal object is `T1 = 0`. Conditioning on `T1` is therefore a **partial** control, and an
   arm surviving it has not been shown to survive conditioning on transitivity proper. This is
   the single largest inferential weakness of §8 and it is stated here rather than in a
   post-hoc limits section.
5. Power is low on `C-STRICT` by construction, and a NULL there may mean nothing more than that.
   The eligible-root counts will be quoted beside every NULL.

---

*Pre-registered 2026-08-07 by Waiel Al-Shujaa, before any form × subject-type quantity existed.
The exposure log in §0 is part of the registration and not an appendix to it.
Bismillāhi al-Raḥmāni al-Raḥīm.*
