---
finding_id: H-NEW-3130
title: "The derived-form fingerprint is a root-inventory fingerprint: a within-root shuffle reproduces 95.7% of the register-classification accuracy, and the flagship Form IV prediction is REVERSED — but its sign is decided by the counting unit, not by the text"
author: Waiel Al-Shujaa
date: 2026-08-09
frontier_item: F-6
prereg: findings/phase-b-hypotheses/prereg-h-new-3130-derived-form-fingerprint.md
prereg_sha256: a95d6c1513b53ca07fb7309016374b0a8760d61ec2d5b37b5f7730f15e7e5869
runs:
  - runs/h-new-3130/20260809T085958Z   # first confirmatory run, retained
  - runs/h-new-3130/20260809T090605Z   # re-run after the §6.1 residualise fix; PRIMARY cell byte-identical
  - runs/h-new-3130-posthoc/20260809T091051Z
seed_null_a: 20260509
seed_null_b: 20260510
n_perms: 10000
k_bonferroni: 6
alpha_bon: 0.008333
binding_raw_gate: 0.001
verdict: NULL — 0 of 6 confirmatory arms pass; the primary confound test is decisively lost
---

# H-NEW-3130 — is the per-surah derived-verb-form distribution a register signature?

## Abstract

**Verdict `NULL`. Zero of six pre-registered arms pass.** The interesting half is not the NULL; it
is *how* it fails.

> **The per-surah verb-form profile classifies register at 33.63 % against a 14.17 % label-shuffle
> baseline — and a shuffle that permutes form labels *within root*, holding each token's surah
> fixed, reproduces 32.19 of those 33.63 points. 95.7 % of the apparent stylistic fingerprint is
> the surah's root inventory.**

The map named root identity as the confound and asked for it to be tested with root held fixed.
It was, by two independent controls, and the confound does not merely intrude — it accounts for
almost the whole effect.

**The flagship directional prediction is REVERSED.** Form IV was locked POSITIVE for narrative;
observed **−0.0285** and negative in all four length channels. Narrative surahs have the
second-*lowest* Form IV share of seven registers (0.1602); legal surahs have **more** Form IV
(0.2128) than narrative.

**And the reversal's sign is a property of the analyst's counting unit, not of the corpus** — the
single most transferable result here:

| counting unit | D1 (Form IV: narrative − rest) | |
|:--|--:|:--|
| verb tokens (the hypothesis as stated) | **−0.0285** | reversed |
| all form-tagged POS (**the counts in the F-6 brief**) | **+0.0433** | locked direction |
| distinct lemma types | +0.0029 | ~zero, sign flips across channels |

Neither alternative is significant (T2 D1-RAW p = 0.13–0.20; D1-ROOT p = 0.54–0.98). **Had the
brief's token counts been used uncritically, this finding would have reported a directional
near-miss instead of a reversal.** The discrepancy was caught in the Step-0 census, before design.

**`cross-finding-028`'s extension base rate is now 0 of 7.**

---

## 1. What was tested

Prereg `a95d6c15…5869`, embedded in `scripts/h-new-3130.py` and verified at runtime with
`SystemExit` on mismatch. QAC SHA `a1d12923…8c46` — byte-identical to the hash in the
H-NEW-2540 / 2600 / 2650 / 2850 run manifests. Genre labels `16ec35b2…4572a`.
Seeds 20260509 (register shuffle) / 20260510 (within-root form shuffle), 10,000 permutations,
k = 6, Bonferroni α = 0.008333, **binding raw gate p < 0.001**.

Per surah: profile `p_s(f)` over eight forms **I, II, III, IV, V, VI, VIII, X**.
- **H1** — leave-one-out nearest-centroid classification of register from `p_s`.
- **D1** — Form IV share, narrative vs rest. Locked **POSITIVE**.
- **D2** — Form V+VI share, legal vs rest. Locked **POSITIVE**.

Each under **Null A** (shuffle register labels; profiles fixed) and **Null B** (shuffle form labels
*within root*, surah fixed; profiles recomputed). Null B preserves every root's corpus-wide form
distribution and every surah's root inventory, destroying only surah-specific allocation — the
surah-level analogue of H-NEW-2540's within-root design.

**Directions were locked from this project's own measurements, not from a grammar.** D1 rests on
H-NEW-2650's I→IV = −0.0633, p = 1.21×10⁻⁶ (Form IV is valency-*increasing*); D2 on II→V =
+0.2500, p = 4.01×10⁻⁵ (Form V is detransitivising). **Instrument declared INHERITED from
H-NEW-2540 with its dependency stated: 2540's primary channel is EQTB parser-contaminated.** This
runner uses QAC only and no treebank, so the contamination does not propagate; the anchors above
are from the parser-free pronoun channel validated by H-NEW-2650 (false-hit rate 0.0000 on all
eight forms), not from the contaminated primary.

---

## 2. Result — the confirmatory family

Binding gate p < 0.001. An arm passes iff its locked direction holds **and** its **worst** p across
the four length channels clears the gate.

| arm | observed L0/L1/L2/L3 | p L0/L1/L2/L3 | worst | dir OK | PASS |
|:--|:--|:--|--:|:--|:--|
| H1-RAW | 0.3363 / 0.3097 / 0.3186 / 0.2212 | 0.00010 / 0.00020 / 0.00010 / **0.03850** | 0.0385 | yes | **no** |
| **H1-ROOT** | 0.3363 / 0.3097 / 0.3186 / 0.2212 | 0.4057 / 0.4621 / 0.2471 / **0.9313** | 0.9313 | **no** | **no** |
| D1-RAW | **−0.0285 / −0.0180 / −0.0270 / −0.0330** | 0.9059 / 0.7893 / 0.8917 / 0.9451 | 0.9451 | **no — REVERSED** | **no** |
| D1-ROOT | −0.0285 / −0.0180 / −0.0270 / −0.0330 | 0.9265 / 0.9820 / 0.9942 / 0.9673 | 0.9942 | **no — REVERSED** | **no** |
| D2-RAW | +0.0068 / +0.0090 / +0.0141 / +0.0141 | 0.2732 / 0.2478 / 0.1960 / 0.2002 | 0.2732 | yes | **no** |
| D2-ROOT | +0.0068 / +0.0090 / +0.0141 / +0.0141 | 0.6610 / 0.3861 / **0.0429** / 0.1153 | 0.6610 | yes | **no** |

`L0` none · `L1` log verse count · `L2` log word count · `L3` log mean verse length.

## 2.1 The root confound, which is the actual finding

| | null mean accuracy | observed | p |
|:--|--:|--:|--:|
| **Null A** — shuffle register labels | 0.1417 (sd 0.0402) | 0.3363 | **0.00010** |
| **Null B** — shuffle forms within root | **0.3219** (sd 0.0383) | 0.3363 | **0.4057** |

Against a null that knows nothing, the profile is a strong classifier (z ≈ +4.8). Against a null
that knows only *which roots each surah uses*, it is worth **1.4 accuracy points and p = 0.41**.

**A second, independent root control agrees on direction and disagrees on degree** (§4.2), and the
disagreement is reported rather than resolved in the hypothesis's favour.

## 2.2 Length: a 385× p-swing, and the dominant channel is mean verse length

H1-RAW runs **p = 0.00010 at L0 and p = 0.03850 at L3** — a **385× swing**, larger than the ~70×
that made H-NEW-3010 an anchor of `cross-finding-029`. **Had a single length channel been locked,
as five of the six prior extensions did, this arm would have read as a clean pass at p = 10⁻⁴.**
The dominant channel is **L3, mean verse length**, and §4.3 shows why: what the classifier can
actually find are the long registers.

The coarsening choice is a second deciding parameter of the same size: H1-RAW's worst-channel p is
**0.0385 under C1** and **0.0002 under C2** — a ~190× swing from re-ordering the head-term
precedence alone. **C1 and C2 disagree about the label of exactly six surahs — Q37, Q44, Q54, Q67,
Q89, Q97 — and those six move the headline p by two orders of magnitude.** That is a sharper
demonstration of `AUDIT-REGISTER-PHASE-COLLINEARITY`'s claim that the coarsening is a deciding
parameter than the audit itself was able to give.

**The verdict is nevertheless stable across it**, because H1-ROOT still fails at p = 0.41 under C2.
The raw arm is coarsening-dependent; the confound test is not.

## 2.3 Robustness tuples (descriptive — cannot alter the verdict)

| cell | H1-RAW p_worst | H1-ROOT p_worst | D1 (L0) | D2 (L0) |
|:--|--:|--:|--:|--:|
| **PRIMARY T1 × R1** | 0.0385 | 0.9313 | **−0.0285** | +0.0068 |
| marker-ablated (drop the 91 Form IV marker tokens) | 0.0240 | 0.9268 | −0.0248 | +0.0076 |
| min 20 verb tokens (n = 86) | **0.0007** | 0.2207 | −0.0285 | +0.0080 |
| R2 Neuwirth labels | 0.0561 | 0.8757 | −0.0285 | +0.0084 |
| R3 coarsening C2 | **0.0002** | 0.4119 | −0.0241 | +0.0068 |
| T2 all form-tagged POS | 0.0006 | 0.2223 | **+0.0433** | +0.0160 |
| T3 lemma types | 0.0538 | 0.4673 | +0.0029 | +0.0134 |

**Two cells clear the gate on H1-RAW and neither survives H1-ROOT.** The min-20 filter was
pre-registered as confounded with the grouping variable (it drops the short oath and
eschatological surahs) and is not verdict-bearing. **In every one of the seven cells the root
control fails.**

**The §2.4 construct overlap is not driving anything**: removing the 91 Form IV tokens inside
`يا أيها الذين آمنوا` moves D1 from −0.0285 to −0.0248. The overlap is real, it was measured before
the run, and it turns out to be immaterial.

---

## 3. Why D1 reversed — and why the reversal is not a finding about the Quran

Post-hoc descriptive shares (`runs/h-new-3130-posthoc/20260809T091051Z`):

| register | n | Form IV share | V+VI share | **root-expected IV** | residual IV | mean verse len |
|:--|--:|--:|--:|--:|--:|--:|
| other | 23 | 0.2186 | 0.0212 | 0.2018 | +0.0168 | 12.87 |
| **legal** | 17 | **0.2128** | 0.0395 | 0.2007 | +0.0121 | 19.41 |
| eschat | 16 | 0.1926 | 0.0343 | 0.1758 | +0.0169 | 4.64 |
| oath | 15 | 0.1840 | **0.0674** | 0.1826 | +0.0014 | 4.34 |
| **narrative** | 26 | **0.1602** | 0.0192 | 0.1648 | **−0.0046** | 10.80 |
| hymn | 9 | 0.1487 | 0.0554 | 0.1668 | −0.0181 | 5.19 |
| polemic | 7 | 0.0845 | 0.0137 | 0.1176 | −0.0331 | 10.48 |

Narrative's Form IV share is 0.1602 and its **root-expected** share is 0.1648 — the residual is
**−0.0046, essentially zero**. Narrative surahs are not choosing against Form IV; the roots
narrative uses are simply not Form IV roots. The reversal is a lexical fact restated, which is the
confound speaking in D1 exactly as it speaks in H1.

Note also that the locked prediction is wrong in a second, independent way: **oath has the highest
V+VI share (0.0674), not legal (0.0395)** — so D2's construct is likewise misassigned even where
its sign is nominally right.

**But the sign itself is not stable under the counting unit**, so none of this should be read as
"the Quran puts less Form IV in narrative". See the abstract's table and §5.1. What is stable is
that **no counting unit produces a significant effect in either direction.**

---

## 4. Power, and the two things this NULL does and does not license

### 4.1 The UNTESTABLE-AT-THIS-N branch was computed, and it did NOT fire

`S* = 0.4336` against `S_max = 1.0000` for H1-ROOT. The design *can* reject in principle, so the
H1 NULL is a real NULL and not an instrument failure.

**MDE, per arm:**

| arm | S* needed | S_max attainable | mean share baseline | **MDE as multiple of baseline** |
|:--|--:|--:|--:|--:|
| D1 | 0.0717 | 0.1540 | 0.1821 | **0.394×** |
| D2 | 0.0575 | 0.0985 | 0.0337 | **1.705×** |

**D2's NULL is close to vacuous and should not be cited as evidence of absence.** It could only
have detected a legal-vs-rest gap larger than **171 % of the mean V+VI share itself** — against a
corpus whose strongest surviving laws run 1.27–2.58× (the `h-new-3030` §3.5 comparison). D1's
0.394× is a meaningful floor, and the observed effect is in the wrong direction anyway.

### 4.2 The two root controls disagree in degree — and I registered a null for only one

- **ROOT-A** (within-root shuffle, pre-registered, verdict-bearing): 95.7 % of accuracy is
  root-carried; p = 0.2471–0.9313.
- **ROOT-B** (residualised profile `d_s = p_s − e_s`, LOSO root expectation): accuracy falls
  0.3363 → **0.2655**, still above the 0.1449 label-shuffle null at **p = 0.0016**.

**This is a defect in my pre-registration, stated at full prominence.** §4.3 registered a null for
ROOT-B's D1 and D2 arms and registered only an *observed accuracy* for ROOT-B's H1 — so the p-value
above is **post-hoc and not verdict-bearing**. This is the H-NEW-2680 error in miniature: a clause
registered three paragraphs above the decision section and then not wired into it.

The two controls are not contradictory — they answer different questions. ROOT-A asks *"is this
surah's allocation of forms within its own roots special?"* (no). ROOT-B asks *"does anything
survive removing the root expectation?"* (some — 26.6 % vs 14.5 %). **Neither supports the
hypothesis as stated**, because D1 on the residualised profile is still **−0.0103, p = 0.878** —
wrong direction. And ROOT-B's p = 0.0016 would fail the 0.001 gate even if it had been registered.

### 4.3 What the 33.6 % is actually made of

Per-register recall of the H1 classifier at L0:

| register | n | recall |
|:--|--:|--:|
| narrative | 26 | **0.731** |
| legal | 17 | **0.588** |
| polemic | 7 | 0.286 |
| other | 23 | 0.217 |
| eschat | 16 | 0.125 |
| **oath** | 15 | **0.000** |
| **hymn** | 9 | **0.000** |

**The classifier finds narrative and legal and nothing else.** Those are the two long registers
(mean verse length 10.80 and 19.41, against 4.34 for oath and 5.19 for hymn). This is why L3
destroys the arm, and it is the concrete mechanism behind the 385× swing: *"register signature"*
here means *"long surahs are separable from short ones"*.

### 4.4 Effective n

Under coarsening C1, **75 of 114 surahs sit in a phase-degenerate register stratum; effective n
against phase is 39.** Degenerate: `narrative` 26/0, `legal` 0/17, `oath` 15/0, `eschat` 15/0,
`liturgical`.

> **Both locked directional arms target perfectly phase-degenerate classes.** As pre-registered in
> §5.4, D1 and D2 **cannot be separated from Meccan/Medinan phase by any amount of stratification**.
> Had either passed, it would have licensed *"the form profile distinguishes these surahs"* and not
> *"register rather than phase drives it"*. This was stated before the run and is not being
> discovered after it.

---

## 5. Instrument facts established here that are reusable

### 5.1 The counting unit decides the sign — the deciding parameter for this hypothesis

Per `cross-finding-029` §3, the finding names the single choice its verdict was most sensitive to
and reports the verdict under an alternative setting. **For D1 it is the counting unit, and it
flips the sign** (−0.0285 / +0.0433 / +0.0029 for verb tokens / all form-tagged POS / lemma types).
For H1 it is **mean verse length** (385×) and, second, the **coarsening order** (~190×). The
verdict is unchanged under all of them, because the root control fails in every cell.

### 5.2 QAC leaves Form I untagged — 12,347 verbs

**Zero verb tokens carry an explicit `(I)`.** Form I must be *derived* as "verb with no form tag",
making it 63.8 % of all verbs. Any future form-distribution work on this corpus that filters on the
form tag will silently drop two-thirds of the verbs.

### 5.3 A lemma-level control on verb form is a TAUTOLOGY

**0 of 1,475 verb lemmas carry more than one form.** In QAC the lemma *is* form-specific
(`LEM:'aAmana` is Form IV by definition), so a lemma-held-fixed control removes 100 % of form
variance by construction and returns a well-formed, meaningless NULL. It was not run as a control,
and the tautology was measured rather than assumed (standing rule 4, from H-NEW-2600's 17/34 coin
flip).

**This is the honest answer to the lemma-vs-root directive** derived from H-NEW-3090's 126× swing:
at this construct the two levels are not two settings of one knob — **one of them is degenerate.**
The non-degenerate contrast is the counting unit (§5.1), and it was run at both levels.

### 5.4 The confound, quantified

**594 of 943 verb roots (63 %) occur in exactly one form.** Token-weighted, **6,352 of 19,356 verb
tokens (32.8 %) sit on single-form roots**, where form carries zero information beyond root.

### 5.5 The form counts circulating in the F-6 brief are all-POS counts

IV 4,585 · II 1,615 · VIII 1,161 … are **VERB 7,009 + N 1,778 + ADJ 170 + PN 20 = 8,977**
form-tagged tokens including maṣdars and participles. Verb-only: **I 12,347 · IV 3,487 · II 1,300 ·
VIII 963 · V 414 · X 369 · III 334 · VI 77 · VII 51 · XII 9 · IX 5 · XI 0.** **Form XI has no verb
token in the corpus.** Forms VII / IX / XI / XII are too sparse to carry a test and were excluded
by name, not silently.

### 5.6 Form VI cannot be tested alone

77 tokens, zero in 77 of 114 surahs, **69.3 % tie fraction** — above the 50 % bar, so it is
exact-test-only and descriptive. Verdict-bearing shares: Form IV **34.2 %**, V+VI **37.7 %**, both
below 50 %, so the permutation test stands for the locked arms.

---

## 6. What I got wrong, at full prominence

### 6.1 A residualisation bug that silently returned p = 1.00000 for a whole tuple

`residualise()` computed its column mean over all 114 rows. Under tuple T2, five surahs
(**Q109, Q111, Q112, Q113, Q114**) have no form-tagged token at all, so their profile rows are NaN
— and one NaN row makes the column mean NaN, which poisons **every** row. The T2 cell in the first
run reported `D1 = +0.0433` at L0 and **NaN at L1/L2/L3**, with `H1-RAW p_worst = 1.00000`.

**It produced a well-formed, publishable artefact** — a p-value of exactly 1.0 reads as a decisive
NULL, not as a crash. That is the `cross-finding-029` signature: nothing downstream failed.

**Bounded by computation, not by assertion** (standing rule 3): T1 and T3 have **zero** NaN rows,
so the confirmatory family could not be affected. Verified after the fix by comparing the two runs'
`PRIMARY_T1_R1` objects — **byte-identical**, and six of seven cells unchanged; only `T2_allpos_R1`
differs.

**Both run directories are retained** (standing rule 2). The first run
`20260809T085958Z` is *not* deleted despite being superseded; the fix was re-run to an **additional**
directory `20260809T090605Z`. The repaired T2 is what §2.3 and the abstract report — and it is the
cell that carries the sign flip, so the bug sat directly on the most transferable result in this
finding.

### 6.2 A pre-registration gap: ROOT-B's H1 arm has no registered null

See §4.2. Registered for D1/D2, not for H1. The post-hoc p = 0.0016 is labelled as post-hoc
everywhere it appears and is not verdict-bearing. It would have failed the gate regardless.

### 6.3 A declared tightening in the runner

Prereg §7(a) says an arm passes if "its observed direction matches the direction locked in §3",
without naming a channel. The runner requires the locked direction in **all four** length channels
(`all(...)`), which is stricter than any single-channel reading. Per the standing rule a tightening
is self-verifying and needs no ratification — recorded here so it is not discovered later.
**It changed nothing**: D1 is negative in all four channels and D2 positive in all four.

### 6.4 The verdict-rule diff, and what was compared

Per the H-NEW-2600 lesson, the runner's verdict function was diffed against prereg §7 line by line
**before** the run. Compared, item by item: (i) family membership — the six arm names and the
`T1 × R1` cell; (ii) the gate constant 0.001 and that the comparison is strict `<`; (iii) that
`arm_passes` conjoins direction **and** p with `and`, not `or`; (iv) that the p used is the
**worst** across L0–L3, not the best or L0; (v) the five verdict strings and their exact
conditions; (vi) their **evaluation order**; (vii) that robustness cells never reach `decide()`.
All seven matched. The diff is reproduced as a comment block above `decide()` in the runner.

---

## 7. Honest limits

- **No matched Classical-Arabic corpus with register labels exists on disk.** Nothing here
  separates a property of *this text* from a property of Classical Arabic. Ceiling is
  QURAN-INTERNAL, and given the NULL, not even that. This limit governs the whole morphology line.
- **Register labels are one tradition's** (Neuwirth/Sinai), assigned at surah level to internally
  heterogeneous texts. A 286-verse surah is not one register. **R2 is a much weaker robustness
  axis than its presence in the table suggests**: the `neuwirth_genre` and `sinai_genre` columns of
  the same TSV disagree, under coarsening C1, about **3 surahs out of 114 (Q2, Q3, Q6)**. It is a
  within-source check, **not a second rater** — no independent register roster exists here, so
  nothing like H-NEW-3020's κ = 0.386 could be computed, and the near-identical D1 values across R1
  and R2 are close to arithmetically guaranteed rather than a replication.
- **D1/D2 are inseparable from phase** (§4.4).
- **QAC's form tagging is itself an annotation**, unvalidated here against an independent
  morphological analyser.
- **The classifier is nearest-centroid on an 8-dimensional composition** — a deliberately simple
  instrument. A stronger classifier might extract more from `p_s`; it would also have to beat the
  Null B baseline of 0.3219, which is the number that matters and which no classifier choice
  changes.
- **27 surahs have fewer than 20 verb tokens**; their profiles are noisy, and they are
  disproportionately the oath and eschatological surahs the classifier already cannot find.

## 8. Relation to prior work

Distinct from the three real neighbours, all of which are token- or root-level with a *grammatical*
outcome: **H-NEW-2540** (root × form-pair → P(overt object); primary channel EQTB
parser-contaminated), **H-NEW-2600** (five form-pairs; `LATTICE-STRUCTURED` retracted, 2 of 5 arms
pass), **H-NEW-2850** (form → subject agency class; NULL on both classifiers). **None is
surah-level and none touches register.** The two hits from an earlier keyword screen —
`h-new-750` (rhyme dispersion + entropy) and `h-new-213` (repetition unit) — contain no morphology
and are false positives.

**This is the seventh pre-registered attempt to extend `cross-finding-028` with a fresh count
against register, and the seventh to fail** (after H-NEW-2630, 2640, 2700, 3010, 3020, 3040).
`AUDIT-CF028-SCOPE-VS-ANCHORS.md` §7 predicted it: a feature that does not share the construct used
to *define* the legal register has nothing to recover. F-6 was the first candidate whose predictor
**did** overlap that construct — `آمنوا` is a Form IV verb — and the overlap turned out to be 2.6 %
of Form IV tokens and immaterial to the result. **The 0-of-N record is now 0 of 7, and §7's
mechanism survives the one test that could have complicated it.**
