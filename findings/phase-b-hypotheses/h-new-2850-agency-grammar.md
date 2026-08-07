---
id: H-NEW-2850
title: Does derivational verb form track the grammatical subject's agency class?
date: 2026-08-07
author: Waiel Al-Shujaa
status: "NULL under the locked decision rule, on both classifiers. The association is large, its five locked signs all hold under C-WIDE, and it SURVIVES transitivity conditioning — but no arm clears the registered root-level gate, and the pre-registration required it."
prereg: prereg-h-new-2850-agency-grammar.md
prereg_sha256: 7e7e98f7a60617df76c42abf66547e639baebd6cd5801990f17e3ae5239b4f2c
run: runs/h-new-2850/20260807T101603Z/
run_replication: runs/h-new-2850/20260807T101641Z/
seed: 20260509
family: MORPH-2026-08-07-B
eqtb_used: secondary-only
---

# H-NEW-2850 — Form and agency, measured

**Verdict: `NULL` on `C-STRICT` (primary) and `NULL` on `C-WIDE` (secondary), under the
decision rule locked at prereg §9.**

The verdict is not close, and it is also not the whole story, so both halves are stated here
before anything else:

> **What failed.** The pre-registration required, for any arm to count, that **both** the exact
> root-level sign test **and** Null B clear a raw p of 0.0005. **Null B clears it on four of
> five `C-WIDE` arms and two of five `C-STRICT` arms. The root-level sign test clears it on
> none — its best value anywhere is 5.40 × 10⁻³.** Under the locked conjunction, no arm passes,
> so the verdict is `NULL`.
>
> **What did not fail.** All five `C-WIDE` signs match their locked directions, **including
> both causative reverse-controls**, so the pre-committed `INSTRUMENT-CONFOUNDED` escape hatch
> was available and the data did not take it. The pooled association is large — divine-subject
> rate 0.5089 for Form II against 0.1176 for Form V. **And it survives the confound that was
> supposed to kill it**: conditioning on overt object realization leaves every well-powered arm
> pointing the same way, in both strata, at CMH odds ratios of 6.21, 3.22, 0.292 and 0.217.

**The honest one-line reading: the effect is carried by token weight and not by root-level
unanimity.** Ten roots of fourteen point the predicted way on II→V, not eighteen of nineteen as
in the parent object-realization result. A token-level null screams; a root-level test shrugs.
The pre-registration made the root-level test binding, and it should stay binding.

---

## 1. What was asked, and what the anecdote was

`h-new-2540-form-v-valency.md` §3 records three roots whose form alternation appears to coincide
with a divine/human split: **ك ب ر**, **ط ه ر** and **ي س ر**. Three roots is an anecdote. This
test asked whether derivational form correlates with the **agency class of the grammatical
subject** across the whole corpus, and — decisively — whether any such correlation survives
being conditioned on transitivity, since form is already known to track object realization
(H-NEW-2540, H-NEW-2600, H-NEW-2650).

**§7 below reports what happened to those three roots when they were actually measured. It is
not what the anecdote suggests.**

---

## 2. The subject classifier

### 2.1 Rules

Locked at prereg §4 and applied mechanically. **The classifier functions take no verb-form
argument**, so they cannot introduce a form-correlated bias by construction; this is a property
of the code, not a claim in prose.

- **`S-EXPL`** — for a **3rd-person** verb, scan forward inside the verse; stop at the first
  verb-bearing word (clause boundary) or the first word carrying exactly one case-marked
  segment. If that case is `NOM`, its lemma is the subject. **DIVINE** iff the lemma is one of
  the three in the closed lexicon `{ Allāh, rabb, al-Raḥmān }`, else **NONDIVINE**.
- **`S-1P`** — 1P agreement → DIVINE (the majestic *naḥnu*).
- **`S-2P`** — 2nd person → NONDIVINE (an addressee in this corpus is a creature).
- **1S**, and **3rd person with no explicit subject**, → **UNCLASSIFIED**. Resolving *huwa* to
  God needs coreference and no rule here performs it.

Two classifiers: **`C-STRICT` = `S-EXPL` alone**, which uses no person information at all and is
the **primary**; **`C-WIDE` = `S-EXPL` → `S-1P` → `S-2P`**, the secondary.

**Why the low-power rule is primary.** The pre-registration's §0.4 records that I saw the
form × person contingency table before locking. Since `S-1P` maps 1P → DIVINE, that table
anticipates any arm using the person channel. `C-STRICT` is anticipated by nothing I looked at,
so it was made primary despite having a fifth of the coverage. That trade was locked in advance
and is not revisited here.

### 2.2 Coverage — and the denominator declaration

`C-STRICT` classifies **2,903 / 18,216 = 15.94 %** of active verbs; `C-WIDE` **9,190 = 50.45 %**
(composition: 4,455 `S-2P`, 2,903 `S-EXPL`, 1,832 `S-1P`).

`findings/UNIT-DRIFT-DEFECT.md` §5 requires a ratio statistic to declare its denominator's drift
across the comparison. **The denominator here is classified verb tokens, and classifiability is
form-correlated.** Quoted beside the headline, not in a footnote:

| form | active | `C-STRICT` coverage | `C-WIDE` coverage |
|:--|--:|--:|--:|
| I | 11695 | 0.1811 | 0.5078 |
| II | 1160 | 0.1207 | 0.5319 |
| III | 310 | 0.0839 | 0.4161 |
| IV | 3203 | 0.1180 | 0.5011 |
| V | 404 | 0.1782 | 0.5050 |
| VI | 77 | 0.1688 | 0.5195 |
| VII | 51 | **0.2353** | **0.3725** |
| VIII | 948 | 0.1034 | 0.5021 |
| X | 354 | 0.0989 | 0.4209 |

**The registered conservative-denominator sensitivity settles whether this drives anything.**
Scoring every UNCLASSIFIED token as non-divine and using *all* active tokens as the denominator —
which can only shrink a divine rate — **every `C-WIDE` sign still holds**: M1 +0.2413,
M2 +0.0803, M3 +0.1333, C1 −0.1580, C2 −0.1690 (C2 at p = 1.94 × 10⁻⁴, the best root-level
p-value in the whole analysis). Differential classifiability is not manufacturing the arms.

### 2.3 Inter-rule agreement

| comparison | n | agreement |
|:--|--:|--:|
| forward-window vs backward-window explicit subject, both present | 317 | **0.7571** |
| `S-EXPL` vs the **EQTB `Subj` edge**, both present | 1981 | **1.0000** |
| `C-STRICT` vs `C-WIDE` on their overlap | 2903 | 1.0000 *by construction — not evidence* |

The EQTB comparison is the meaningful one: an independently built dependency annotation assigns
the same divine/non-divine call on all 1,981 tokens where both channels fire. **It is
contamination-flagged** — EQTB's syntax was parser-initialised with `verb_form` among its inputs
(H-NEW-2540 §7.2) — and it is reported as corroboration of the *rule*, not of the finding.

The **forward-vs-backward figure of 0.7571 is the honest measure of how much noise the extended
rule adds**, and it is why `S-EXPL-EXT` was registered as a sensitivity and never as primary.

### 2.4 The ambiguous classes, in full

| class | n | disposition |
|:--|--:|:--|
| 3rd person, no explicit subject in its clause | **8,479** | UNCLASSIFIED — needs coreference |
| 2nd person (addressee) | 4,455 | NONDIVINE by `S-2P` |
| 1st person plural | 1,832 | DIVINE by `S-1P` |
| **1st person singular** | **547** | UNCLASSIFIED — God at Q 51:56, human elsewhere, no discriminator |
| 1P verbs with a *q-w-l* verb earlier in the verse | 420 | possible quoted human "we"; `S-1P-QCUT` sensitivity |
| 2nd-person verbs in a verse with a vocative + divine name | 461 | possible duʿāʾ addressed to God; `S-2P-VCUT` sensitivity |
| `rabb`-subject tokens inside Q 12:20–12:50 | **3** | the declared human-master error bound |

Forward-window terminators for 3rd-person verbs: `NOM` 2,903 · `ACC` 2,682 · `VERB` 2,826 ·
`GEN` 2,087 · verse-end 884.

**The `rabb` error bound came back clean.** The three flagged tokens are `(12:33:1:1)`
*rabbi l-sijnu aḥabbu* (Yūsuf addressing God), `(12:34:1:2)` *fa-stajāba lahu rabbuhu*, and
`(12:37:14:1)` *ʿallamanī rabbī*. **All three are genuinely divine; the measured error is zero
out of three.** The lexicon's known weak point did not fire.

---

## 3. Results — the form × subject-type table

Pooled divine-subject rate by form, over classified tokens. **Both columns are reported because
their agreement is the single most informative thing in this file.**

| form | | `C-WIDE` (uses person) | | `C-STRICT` (**no person information**) |
|:--|--:|--:|--:|--:|
| | div/n | rate | div/n | rate |
| **II** *(causative)* | 314/617 | **0.5089** | 73/140 | **0.5214** |
| **IV** *(causative)* | 745/1605 | **0.4642** | 167/378 | **0.4418** |
| III | 32/129 | 0.2481 | 10/26 | 0.3846 |
| **I** *(base)* | 1451/5939 | **0.2443** | 532/2118 | **0.2512** |
| X | 19/149 | 0.1275 | 8/35 | 0.2286 |
| VI *(muṭāwiʿ)* | 4/40 | 0.1000 | 3/13 | 0.2308 |
| VIII *(muṭāwiʿ)* | 54/476 | 0.1134 | 13/98 | 0.1327 |
| V *(muṭāwiʿ)* | 24/204 | **0.1176** | 5/72 | **0.0694** |
| VII *(muṭāwiʿ)* | 0/19 | **0.0000** | 0/12 | **0.0000** |
| **all** | 2643/9190 | 0.2876 | 811/2903 | 0.2794 |

**The two causatives sit at 0.44–0.52, the base form at 0.24–0.25, and the four *muṭāwiʿ* forms
at 0.00–0.23 — and the person-free classifier reproduces the ordering.** That is the answer to
the pre-registration's own §0.4 worry: this is not merely the corpus's person deixis wearing an
agency label. `C-STRICT` never sees a person feature and it puts Form II at 0.5214 against Form
V at 0.0694.

### 3.1 The five arms

Within-root, ≥2 classified tokens per form per root, `PASS` excluded. `gap` is the pooled
within-root difference; `T` is the weighted smoothed statistic of H-NEW-2540 §2, with the
unsmoothed macro difference beside it; sign test is the exact two-sided binomial over discordant
roots; Null B is the margin-preserving token-label permutation, 10,000 draws, two-sided.

**`C-WIDE` (secondary)**

| arm | pair | locked | roots | rate A | rate B | gap | T (macro) | MH-OR | roots +/−/= | **sign test** | **Null B** | sign |
|:--|:--|:--:|--:|--:|--:|--:|--:|--:|:--|--:|--:|:--|
| M1 | II→V | + | 14 | 0.6094 | 0.0833 | **+0.5260** | +0.3562 (+0.3107) | 7.42 | 10/3/1 | 9.23 × 10⁻² | **1.0 × 10⁻⁴** | HELD |
| M2 | I→VIII | + | 21 | 0.3165 | 0.1042 | **+0.2122** | +0.1947 (+0.1053) | 3.55 | 13/5/3 | 9.63 × 10⁻² | **1.0 × 10⁻⁴** | HELD |
| M3 | III→VI | + | 1 | 1.0000 | 0.6000 | +0.4000 | +0.3452 | ∞ | 1/0/0 | 1.00 | 0.179 | HELD, no power |
| **C1** | I→II | **−** | 19 | 0.1647 | 0.3774 | **−0.2127** | −0.2635 (−0.3233) | **0.234** | 5/13/1 | 9.63 × 10⁻² | **1.0 × 10⁻⁴** | **HELD** |
| **C2** | I→IV | **−** | 47 | 0.1478 | 0.4544 | **−0.3066** | −0.3312 (−0.1969) | **0.185** | 12/31/4 | **5.40 × 10⁻³** | **1.0 × 10⁻⁴** | **HELD** |

**`C-STRICT` (primary)**

| arm | pair | locked | roots | rate A | rate B | gap | T (macro) | MH-OR | roots +/−/= | sign test | Null B | sign |
|:--|:--|:--:|--:|--:|--:|--:|--:|--:|:--|--:|--:|:--|
| M1 | II→V | + | 4 | 0.8095 | 0.0909 | **+0.7186** | +0.6269 (+0.4292) | 7.96 | 3/1/0 | 0.625 | **1.0 × 10⁻⁴** | HELD |
| M2 | I→VIII | + | 5 | 0.3333 | 0.2188 | +0.1146 | +0.0392 (+0.1457) | 1.26 | 2/2/1 | 1.00 | 0.742 | HELD |
| M3 | III→VI | + | **0** | — | — | — | — | — | — | — | — | **no eligible roots** |
| C1 | I→II | **−** | 3 | 0.4800 | 0.4000 | +0.0800 | +0.0255 | 1.32 | 2/1/0 | 1.00 | 0.950 | **FLIPPED** |
| **C2** | I→IV | **−** | 14 | 0.0938 | 0.4960 | **−0.4022** | −0.5158 (−0.4811) | **0.032** | 1/11/2 | 6.35 × 10⁻³ | **1.0 × 10⁻⁴** | **HELD** |

`1.0 × 10⁻⁴` is the Monte-Carlo floor, 1/10001.

**`C-STRICT` fails clause (a) of the decision rule**: M3 has no eligible roots at all, and C1's
sign flips on **three roots**, which is a sample size at which a sign carries no information. The
primary classifier's answer is therefore *"this design cannot resolve the question at this
coverage"* rather than *"the effect is absent"*, and the eligible-root counts are quoted so a
reader can see which it is.

**Leave-one-root-out.** Every `C-WIDE` arm is robust to dropping any single root: M1
[+0.4734, +0.5562], M2 [+0.1607, +0.2574], C1 [−0.4474, −0.1656], C2 [−0.3319, −0.2508], all
matching their locked signs throughout. On `C-STRICT`, C1 does **not** survive it
([−0.0455, +0.5833]) — again the three-root problem.

---

## 4. The confound that was supposed to decide this — and did not kill it

The pre-registration named the alternative explanation plainly: **divine subjects may simply take
more objects because divine action is narrated transitively, and form already tracks object
realization.** If that is all this is, conditioning on transitivity should remove it.

`T1` = the verb carries an overt attached object pronoun, by **`RULE-NEW` of H-NEW-2650 §3,
inherited verbatim** (100 % classifier coverage asserted at runtime over all 12,496 post-verb
`SUFFIX PRON` tokens). The naive PGN-discard rule — which H-NEW-2650 measured as deleting 311
genuine objects at a form-correlated rate — appears nowhere in this script.

**Cochran–Mantel–Haenszel, strata = (root × `T1`):**

| arm | classifier | `OR_CMH` | p | strata | gap at `T1`=0 | gap at `T1`=1 |
|:--|:--|--:|--:|--:|--:|--:|
| M1 II→V | C-WIDE | **6.21** | 1.31 × 10⁻⁸ | 13 | +0.5030 (12 roots) | +0.6333 (2 roots) |
| M2 I→VIII | C-WIDE | **3.22** | 7.83 × 10⁻⁶ | 20 | +0.2054 (18) | +0.1750 (4) |
| C1 I→II | C-WIDE | **0.292** | 5.66 × 10⁻⁵ | 20 | −0.1434 (15) | −0.3971 (2) |
| C2 I→IV | C-WIDE | **0.217** | 2.07 × 10⁻²⁸ | 42 | −0.2354 (32) | −0.4781 (12) |
| M1 II→V | C-STRICT | **8.18** | 2.44 × 10⁻⁵ | 4 | +0.7000 (3) | +1.0000 (1) |
| C2 I→IV | C-STRICT | **0.030** | 1.55 × 10⁻²¹ | 13 | −0.3239 (9) | −0.6985 (3) |
| M2 I→VIII | C-STRICT | 2.59 | 0.262 | 5 | +0.3239 (2) | 0.0000 (1) |
| C1 I→II | C-STRICT | 2.11 | 0.632 | 3 | +0.5455 (2) | −0.1667 (1) |

**Every well-powered arm keeps its locked direction inside *both* object-clitic strata, and the
CMH odds ratios sit on opposite sides of 1 exactly as the doctrine predicts.** The association
is not a restatement of the object-realization finding.

**The secondary EQTB-conditioned arm (contaminated, reported as such).** Stratifying on the EQTB
`Obj` edge instead of the clitic: M1 `OR` = 7.41 (p = 2.43 × 10⁻⁵), M2 = 2.94
(p = 5.57 × 10⁻⁵), C2 = 0.165 (p = 3.41 × 10⁻³⁴) — but **C1 weakens materially**, to `OR` = 0.383
at p = 3.38 × 10⁻³, and its `T2` = 0 stratum **reverses** to +0.0254 on 4 roots. Because EQTB's
parser had `verb_form` among its inputs, stratifying on `T2` partially stratifies on the
predictor and over-controls; per prereg §5.2 this arm may not overturn the `T1` result, and it
does not. It is recorded because C1 is the arm a sceptic should press on.

**The limit that caps all of this, stated at prereg §12.4 and not softened now.** `T1` measures
**overt enclitic object realization**, not transitivity. A verb with a full nominal object scores
`T1` = 0. Conditioning on `T1` is a **partial** control, and nothing above shows the association
survives conditioning on transitivity proper. That would need an uncontaminated object
annotation, which does not exist for this corpus.

---

## 5. Why the verdict is `NULL` anyway

The decision rule (prereg §9) required, for an arm to count toward `AGENCY-TRACKED`, that it
clear p < 0.0005 on **both** the exact sign test and Null B. The two disagree sharply:

| arm (C-WIDE) | Null B (token-level) | exact sign test (root-level) | roots +/− |
|:--|--:|--:|:--|
| M1 II→V | **1.0 × 10⁻⁴** ✅ | 9.23 × 10⁻² ❌ | 10/3 |
| M2 I→VIII | **1.0 × 10⁻⁴** ✅ | 9.63 × 10⁻² ❌ | 13/5 |
| C1 I→II | **1.0 × 10⁻⁴** ✅ | 9.63 × 10⁻² ❌ | 5/13 |
| C2 I→IV | **1.0 × 10⁻⁴** ✅ | 5.40 × 10⁻³ ❌ | 12/31 |

**This disagreement is the result, not an inconvenience.** Null B permutes labels across tokens
within a root and so treats a root's thirty tokens as thirty pieces of evidence; the sign test
asks only whether the root points the right way and so treats it as one. The parents' object
finding was near-unanimous at the root level — 18/1, 30/3, 31/3 in H-NEW-2650 §5 — and cleared
both. **Agency is not**: 10/3, 13/5, 5/13, 12/31. The effect is real in magnitude and
inconsistent across the lexicon.

`findings/UNIT-DRIFT-DEFECT.md` §6 step 6 is explicit: *"If two nulls disagree, report both and
take the stricter."* The stricter is the root-level test. It fails. **The verdict is `NULL` and
I am not overriding it**, for the reason recorded in H-NEW-2600's retraction: a runner that
implements a looser rule than the one registered defeats pre-registration entirely.

**What a reader may take from a `NULL` here.** Not "form does not track agency" — the
association is large, directional, sign-consistent across five arms including two reverse
controls, robust to leave-one-root-out, robust to a conservative denominator, and it survives
transitivity conditioning. What the `NULL` says is that **the evidence is token-weighted rather
than lexically general**, and this project's registered bar for a confirmatory claim is lexical
generality.

---

## 6. The census — owed under every verdict, and delivered

`census-roster.tsv` — **9,190 rows**, one per classified active verb: location, surah, verse,
root, form, aspect, agreement, subject label, subject lemma, rule fired, `T1`, `T2`, verse text.

`dissociation-roster.tsv` — **42 root × form-pair cells** across **33 distinct roots**, every
cell where a causative member (II or IV) and a *muṭāwiʿ* member (V, VI, VII, VIII) of the same
root differ in divine-subject rate, with **every occurrence located on both sides**. Not filtered
to interesting roots.

- **36 of 42 cells run causative-more-divine**, 6 run *muṭāwiʿ*-more-divine.
- **By distinct root: 27 unanimously causative-more-divine, 4 unanimously the other way, 2
  mixed.** Exact two-sided sign test over the 31 unanimous roots: **p = 3.40 × 10⁻⁵**.
- **Nine perfect dissociations** (100 % / 0 %), eight of them causative-more-divine:

| root | pair | causative | *muṭāwiʿ* |
|:--|:--|:--|:--|
| **ص ل ي** | IV → VIII | 3/3 divine | 0/2 |
| **ب د ل** | IV → V | 1/1 | 0/2 |
| **ف ي أ** | IV → V | 3/3 | 0/1 |
| **ن ش ر** | IV → VIII | 1/1 | 0/3 |
| **ق ر ب** | II → VIII | 1/1 | 0/4 |
| **ر ض و** | IV → VI | 1/1 | 0/1 |
| **س و ي** | II → VIII | 2/2 | 0/15 |
| **ز ي ل** | II → V | 1/1 | 0/1 |
| **أ ذ ن** | II → V | 0/3 | **2/2** ← the one that runs the other way |

The largest cells: **ن ز ل** IV→V 87/93 against 1/6; **ن ج و** II→VI 24/30 against 0/3;
**ب ي ن** II→V 18/22 against 0/11; **ر أ ي** IV→VI 16/26 against 0/2.

**This roster is a descriptive deliverable, not a registered inference.** Its p-value is quoted
because it is the strongest root-level number in the analysis and suppressing it would be
dishonest, but it must not be read as a test: the 42 cells are not independent — نزل contributes
both II→V and IV→V, and the roster is by construction restricted to roots where the two rates
already differ.

---

## 7. The three showcase roots, measured — and this is the part that matters most

The anecdote that motivated the whole test does not survive contact with a mechanical subject
classifier. All three are in the census; here is what they actually contain.

### ك ب ر — the showcase is about the **object**, not the subject

The root has exactly four Form II tokens in the corpus and **all four are second-person** — two
imperative, `(17:111:20:2)` *kabbirhu* and `(74:3:2:2)` *fa-kabbir*, and two imperfect after
purposive *li-*, `(2:185:38:3)` and `(22:37:14:2)` *li-tukabbirū*. **The subject in every one of
them is the human addressee.** God is the *object* of the magnifying, which is precisely what
H-NEW-2540 §3 observed — but that is a fact about the object slot, and this test measures the
subject slot. (H-NEW-2540 §3 reports the count as 4 and names three verses; the fourth is
Q 22:37.)

**Per-form divine-subject counts for ك ب ر: I 0/2 · II 0/4 · V 0/1 · X 0/12. Not a single divine
subject anywhere in the root**, and the root does not appear in the dissociation roster at all.

H-NEW-2540 §3's line *"the valency **is** the theology"* is therefore about direction of
transitivity, not about who acts. **It should not be cited as evidence that form tracks agency.**

### ط ه ر — runs the **wrong way**, and the reason is an error in my own rule

**II 0/3 divine · V 1/2 divine.** The showcase root comes out *muṭāwiʿ*-more-divine.

Two things produced that, and the first is a coverage failure severe enough to state as a number.
**ط ه ر has nine Form II tokens in the corpus. The classifier can see three of them, and they are
the three imperatives** — `(22:26:11:2)` *ṭahhir bayt-ī*, `(2:125:17:1)` *ṭahhirā bayt-ī*,
`(74:4:2:2)` *fa-ṭahhir* — whose subjects are human. **The six it cannot see are exactly the
divine-agent ones**: `(3:42:8:2)` *ṭahhara-ki*, `(5:41:57:1)`, `(8:11:11:2)`, `(9:103:5:1)`,
`(33:33:24:2)`, and — **`(5:6:56:2)` *li-yuṭahhira-kum*, the actual showcase verse**. All six are
3rd person with no explicit nominal subject, so their divine agent is recoverable only by
coreference, which no rule here performs. The showcase root's evidence is not weak in this test;
it is invisible to it.

Second, and worse: the single "divine" Form V token, `(9:108:20:1)` *yataṭahharū*, **is a false
positive of my own `S-EXPL` rule**, verified segment by segment:

```
w20  yataTah~aru + wA@   (V, Form V, 3MP)
w21  wa (CONJ) + {ll~ahu (PN, NOM)
w22  yuHib~u    (V)
```

`wa-llāhu` is the subject of *yuḥibbu* at word 22, not of *yataṭahharū* at word 20. The rule took
it because the clause boundary is carried by a conjunction **prefixed to the noun**, so no
verb-bearing word intervenes.

**I measured how often that happens.** Of the 2,903 `S-EXPL` classifications, **79 (2.72 %)** have
a clause-linking prefix on the subject word, and **43 of the 811 divine calls (5.30 %)** are of
that kind. It is form-correlated and it runs in the effect-inflating direction for C2:
**Form X 14.29 % · Form IV 3.97 % · Form I 2.55 % · Form II 0.71 %.** Form IV is the causative in
C2, so spurious `Allāhu` subjects land preferentially on the arm's B side, where the locked
direction wants them. The absolute numbers are small — 15 Form IV tokens corpus-wide — but
**the direction of the bias favours my own hypothesis and a reader is entitled to know that.**
A corrected rule would reject a `NOM` whose word carries a clause-linking prefix; that rule was
not registered and is not applied here.

### ي س ر — supports the direction, but has nothing to compare against

**Form II 9/10 divine** — the four al-Qamar refrains `(54:17, 54:22, 54:32, 54:40)` plus
`(19:97)`, `(44:58)`, `(87:8)`, `(92:7)`, `(92:10)`, all *yassarnā* with the majestic 1P; the one
non-divine token is `(20:26:1:2)` *yassir lī amrī*, Mūsā's supplication, whose subject is God as
addressee and which `S-2P` therefore mis-scores NONDIVINE — the declared duʿāʾ error of prereg
§4.5, firing exactly where predicted.

**Form V: zero classified tokens.** Q 73:20 *mā tayassara* is 3MS with no explicit subject. So
ي س ر cannot appear in the dissociation roster either.

### What this section establishes

**Of the three roots that motivated this hypothesis, none supports it as stated.** One measures
the object slot rather than the subject slot; one runs the wrong way on a classification that
inspection shows to be a rule error; one has no testable counterpart. **The corpus-wide roster
nonetheless runs 27 roots to 4 in the predicted direction.** The generalisation is better
supported than the anecdotes that prompted it — which is an unusual and slightly humbling shape
for a result to have, and it is the reason the census was made a deliverable owed under every
verdict.

---

## 8. Sensitivities — all registered, all reported

Every registered sensitivity, with its locked-sign outcome. **48 of the 50 signed cells hold
their locked direction**; the two that do not are both `C-STRICT` cells at 3 and 4 roots.

| sensitivity | M1 | M2 | M3 | C1 | C2 |
|:--|:--|:--|:--|:--|:--|
| **conservative denominator, C-WIDE** | +0.2413 HELD | +0.0803 HELD | +0.1333 HELD | −0.1580 HELD | **−0.1690 HELD, p = 1.94 × 10⁻⁴** |
| conservative denominator, C-STRICT | +0.0776 HELD | +0.0379 HELD | −0.2000 **FLIP** (4 roots) | −0.0041 HELD | −0.0426 HELD |
| `S-1P-QCUT` (drop 1P in a *q-w-l* verse) | +0.5242 HELD | +0.1971 HELD | +0.4000 HELD | −0.1908 HELD | −0.3182 HELD |
| `S-2P-VCUT` (drop 2P in duʿāʾ verses) | +0.5472 HELD | +0.2224 HELD | +0.4000 HELD | −0.2039 HELD | −0.3265 HELD |
| `C-WIDE-EXT` (backward + coordination) | +0.4560 HELD | +0.1811 HELD | +0.4464 HELD | −0.1891 HELD | −0.2650 HELD |
| `C-STRICT-EXT` | +0.4596 HELD | +0.2822 HELD | no roots | −0.0051 HELD | −0.2006 HELD |
| ≥1-token eligibility, C-WIDE | +0.4814 HELD | +0.2020 HELD | +0.3798 HELD | −0.3229 HELD | −0.3497 HELD |
| Meccan only, C-WIDE | +0.5491 HELD | +0.1971 HELD | +0.2500 HELD | −0.2429 HELD | −0.4275 HELD |
| Medinan only, C-WIDE | +0.5891 HELD | +0.3484 HELD | no roots | −0.3911 HELD | −0.3325 HELD |
| `C-STRICT` primary | +0.7186 HELD | +0.1146 HELD | no roots | +0.0800 **FLIP** (3 roots) | −0.4022 HELD |

Meccan and Medinan agree closely on every arm, so this is not a chronological artefact. The two
person-channel cuts change nothing, so the declared quoted-speech and duʿāʾ errors are not
carrying the arms.

**The person-composition arm, reported as a person result and not as an agency result**
(prereg §7.4). Within-root, over *all* active tokens, using 1P agreement as the outcome:
M1 +0.1637 (11/4/8, p = 0.119), M2 +0.0424 (17/8/14, p = 0.108), C1 −0.1539 (6/21/10,
p = 5.93 × 10⁻³), C2 −0.1264 (16/39/25, p = 2.67 × 10⁻³). **Form II is 0.2078 first-person-plural
against Form V's 0.0470 and Form VII's 0.0000.** So the corpus's person deixis does track
derivational form, in the same direction — but §3's `C-STRICT` column shows the ordering survives
with the person channel removed entirely, so person is a contributor and not the mechanism.

**Descriptive arms.** I→VII: `C-WIDE` +0.6667 on 5 roots (4/0/1, p = 0.125); `C-STRICT` +0.7333
on 2 roots. IV→VII: **zero eligible roots**, as in H-NEW-2600 §4. Form VII remains too rare in
this corpus to test, and **no Form VII token in the corpus has a divine subject under either
classifier (0/19 and 0/12).**

---

## 9. Honest limits

1. **The classifier is a rule, not ground truth.** Its own error rate is unmeasured until the
   blinded sample of §10 is scored by a qualified human reviewer. §7 documents one confirmed
   false positive found by inspection and quantifies its class at 2.72 % of all classifications
   and **5.30 % of divine ones, form-correlated and running in the direction that favours the
   hypothesis.**
2. **`T1` is not transitivity** (§4, last paragraph). This is the largest inferential weakness
   in the file and it was declared before the run, not after.
3. **Coverage is 15.94 % on the primary classifier.** `C-STRICT`'s M3 arm has no eligible roots
   and its C1 arm has three. Those arms are unresolved, not negative.
4. **8,479 third-person verbs carry no explicit subject** and are invisible to this test — the
   single largest gap, and it is precisely where the showcase verse Q 5:6 lives.
5. **"Divine subject" is a referential class imposed on a grammatical variable.** An angel, a
   prophet acting on command, or a personified natural force scores NONDIVINE here, and
   reasonable analysts would classify some of those differently.
6. **Not novel grammar.** Muṭāwaʿa and the causative function of II/IV are textbook. What is new
   here is a corpus-wide measurement of the *subject* side, and its principal finding is a
   `NULL` against a registered gate.
7. **Not Qurʾān-specific.** There is no matched Classical-Arabic corpus with agency annotation,
   so nothing here separates a property of this corpus from a property of Classical Arabic. Per
   the project's Phase-B rule this is at most **QURAN-INTERNAL**, and given the `NULL` verdict it
   is not even that.
8. **No theological claim is made or implied.** The output is a grammatical fact about a
   classification of grammatical subjects. Interpretation belongs to the reader and to the
   exegetical tradition.
9. **The `C-WIDE` arm is not blind.** Prereg §0.4 records that I saw the form × person table
   before locking. `C-STRICT` is blind; it is also the arm with the least power.

---

## 10. Provenance and run discipline

- Pre-registration `prereg-h-new-2850-agency-grammar.md`, SHA-256
  `7e7e98f7a60617df76c42abf66547e639baebd6cd5801990f17e3ae5239b4f2c`, **committed at
  `044815a75` before any form × subject-type quantity existed**, embedded as a literal in the
  script and verified at runtime with `SystemExit` on mismatch.
- The runner was **committed at `12e414ba7` before the confirmatory run**, so git independently
  timestamps the script's final state — the conformance gap recorded at H-NEW-2540 §8.1 is not
  repeated.
- Frozen inputs verified by SHA-256 at runtime. QAC `a1d12923…8c46` is byte-identical to the
  hash in the H-NEW-2540/2600/2650 run manifests, so every comparison is against the same corpus
  the parents used. EQTB `a303c24c…e0b7`, **secondary only**.
- **Determinism.** Two run directories, **both retained**: `20260807T101603Z` (primary) and
  `20260807T101641Z` (replication). `result.json`, `census-roster.tsv`,
  `dissociation-roster.tsv`, `validation-sample.tsv` and `validation-key.json` are
  **byte-for-byte identical** across both.
- **No run directory was deleted.** A third directory, `20260807T101421Z`, is a **smoke run at
  `N_PERM = 60`** written into the runs tree by an output-path substitution that silently failed.
  It is retained with a notice at `runs/h-new-2850/SMOKE-NOTICE-20260807T101421Z.md` rather than
  removed, per the standing correction at H-NEW-2540 §8.1. Its permutation p-values are floored
  at 1/61 and mean nothing; everything else in it agrees with the retained runs.
- The script writes each output exactly once, with mode `'x'`, into a directory created with
  `exist_ok=False`, and never overwrites a file inside its own run directory
  (UNIT-DRIFT-DEFECT §7).
- **Verdict logic was diffed clause by clause against prereg §9 before any number was quoted**,
  and `result.json` records each clause's truth value separately
  (`clause_a_all_five_signs_match`, `clause_b_*_arms_passing_gate`,
  `clause_c_transitivity_conditioned`, `escape_hatch_both_causative_arms_positive`).
- Seeds 20260509 / 20260519, 10,000 permutations, all fixed literals. Family k = 20,
  Bonferroni α = 0.0025, binding gate 0.0005.
- **Blinded validation sample**: `validation-sample.tsv`, 176 rows stratified by form × subject
  label, ≤10 per cell, carrying no form label and no rule verdict; the mapping is in
  `validation-key.json`. **The review columns are blank and I have not filled them in.**

---

## 11. Cross-references

- **h-new-2540-form-v-valency.md** — the parent. Its §3 ك ب ر showcase is an **object**-slot
  observation and §7 above shows it carries no subject-slot effect; that section should carry a
  note saying so.
- **h-new-2650-pronoun-channel-validation.md** — `RULE-NEW` is inherited verbatim as `T1`.
- **h-new-2600-mutawaa-lattice.md** — the reverse-control design is inherited; its
  `INSTRUMENT-CONFOUNDED` escape hatch is re-registered here and again went untaken.
- **UNIT-DRIFT-DEFECT.md** — §5's denominator declaration (§2.2 above) and §6's
  "if two nulls disagree, take the stricter" (§5 above), both applied.
- **h-new-2510** (divine-self-reference density, NULL) — the two agree: token-level *density*
  could not recover a theological class, and token-level *form* recovers a large but lexically
  inconsistent one.

---

*H-NEW-2850 logged 2026-08-07 by Waiel Al-Shujaa. The three roots that started this do not
support it; the other thirty do, and not by enough. Bismillāhi al-Raḥmāni al-Raḥīm.*
