---
prereg_id: H-NEW-3130
title: "Is the per-surah distribution over derived verb forms a register signature independent of root vocabulary?"
frontier_item: F-6
author: Waiel Al-Shujaa
date: 2026-08-09
status: PRE-REGISTERED — written and hashed before any register x form quantity was computed
seed_null_a: 20260509
seed_null_b: 20260510
n_perms: 10000
k_bonferroni: 6
alpha_bon: 0.008333333333333333
binding_raw_gate: 0.001
---

# Pre-registration — H-NEW-3130 (frontier item F-6)

## 0. The prior, stated first and stated honestly

**Six pre-registered attempts to extend `cross-finding-028` with a fresh count against register
have returned NULL or reversed. Zero for six.**

| finding | added feature | verdict |
|:--|:--|:--|
| H-NEW-2630 | realis/irrealis conditionals | NULL-REVERSED |
| H-NEW-2640 | modality | NULL, 4/4 fail, two reversed |
| H-NEW-2700 | loanword donor language | ALL FOUR NULL, co-primary reversed |
| H-NEW-3010 | conditionals, Neuwirth–Sinai labels | NULL, 0 of 12 |
| H-NEW-3020 | donor language, second rater | NULL at primary tuple (κ = 0.386) |
| H-NEW-3040 | modality, eight length channels | DIRECTIONAL not PASS (3/8) |

`findings/AUDIT-CF028-SCOPE-VS-ANCHORS.md` §7 gives the mechanism, and it is not a run of bad
luck. The legal register is **defined** by counting the substrings `يا أيها الذين آمنوا` and
`كتب عليكم` (`h-new-2500.py:60`). A candidate feature that shares that construct separates almost
by definition; one that does not has nothing to recover. **This is the seventh fresh count. My
prior is that it fails.**

**I record one respect in which F-6 differs from the six, and it points the wrong way for the
hypothesis.** See §2.4: the legal marker contains a Form IV verb, so my predictor is
construct-linked to the label — in the direction *opposite* to my locked prediction.

The FRONTIER-MAP's own Prior lines scored 1 for 6 across executed items. I am not inheriting that
optimism.

---

## 1. Hypothesis

> The distribution over derived verb forms I–X is a per-surah signature that predicts register
> **independently of root vocabulary**. Form IV (causative/declarative) should mark divine-agency
> narrative; Forms V/VI (reflexive/reciprocal) should mark community/legal discourse.

The load-bearing word is **independently**. A form profile that merely re-expresses which roots a
surah uses is not a stylistic fingerprint. §5.2 is therefore the primary test, not a robustness
check.

---

## 2. Data, and four facts about it that constrain the design

Source: `data/morphology/quranic-corpus-morphology-0.4.txt` (Quranic Arabic Corpus v0.4).
Register labels: `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`, 114 surah rows.
Both SHA-256-pinned in the runner and verified at runtime.

### 2.1 The counts in the F-6 brief are not verb counts — UNIT DRIFT, verified before design

The brief quotes IV 4,585 · II 1,615 · VIII 1,161 · III 497 · V 466 · X 459 · VI 106 · VII 63 ·
XII 13 · IX 11 · XI 1. Those reproduce exactly, but only over **every POS carrying a form tag**:
VERB 7,009 + N 1,778 + ADJ 170 + PN 20 = **8,977**. The nominals are maṣdars and participles.

Verb-only (`POS:V`), which is what "distribution over verb forms" denotes:

| form | I | II | III | IV | V | VI | VII | VIII | IX | X | XI | XII |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| verb tokens | **12,347** | 1,300 | 334 | 3,487 | 414 | 77 | 51 | 963 | 5 | 369 | **0** | 9 |

The deverbal-nominal decision moves Form IV by 1,098 tokens (31 %). It is a rules-tuple (§6, T1/T2),
not a detail. This is the `findings/UNIT-DRIFT-DEFECT.md` failure mode caught before the run.

### 2.2 Form I does not exist in QAC and must be *derived*

**Zero verb tokens carry an explicit `(I)`.** 12,347 verbs carry no form tag at all. Form I is
therefore inferred as *"verb with no form tag"*, which makes it 63.8 % of all verbs. This is an
inference about the annotation scheme, not a reading of it. Consequence: in tuple T2 (all POS)
Form I is undefined for nominals, so T2's profile runs over II–X only and is **not** commensurable
with T1's. Declared, not hidden.

### 2.3 Which forms can carry a test, stated rather than assumed

Tested set (8): **I, II, III, IV, V, VI, VIII, X**.
Excluded as too sparse on verbs: **VII (51) · XII (9) · IX (5) · XI (0)**. Form XI has **no verb
token in the corpus**; the brief's "XI 1" is a single deverbal nominal.

**Form VI is retained only inside the pooled V+VI arm.** Alone it has 77 tokens, **77 of 114
surahs have zero**, and its per-surah share has a **69.3 % tie fraction** — above the 50 % bar, so
VI alone is reportable only under an exact test and is **descriptive, never verdict-bearing**.
Measured tie fractions of the verdict-bearing shares: Form IV **34.2 %**, V+VI **37.7 %** — both
below 50 %, so the permutation test stands for the locked arms. (Rule: any arm whose tie fraction
exceeds 50 % is switched to an exact test.)

### 2.4 NEW — the legal marker contains a Form IV verb

`(2:104:3:1) 'aAmanu V STEM|POS:V|PERF|(IV)|LEM:'aAmana|ROOT:Amn|3MP`

`آمنوا` **is Form IV**. The substring that *defines* the legal register in `h-new-2500.py`
therefore contains one token of the feature under test — the first time in this family that the
§7 construct-overlap runs *through* the predictor rather than around it.

Measured: **91 full vocative occurrences = 2.6 % of all Form IV verb tokens**, in 22 surahs led by
Q5 (16), Q2 (11), Q4 (9), Q33 (7), Q3 (7), Q8 (6). Root `Amn` supplies **537 Form IV verbs
(15.4 %)** overall.

**Direction of the resulting bias: it inflates Form IV in LEGAL surahs, i.e. against locked
prediction D1 (Form IV → narrative).** It is conservative for D1 and would be fatal to any
legal-side reading of Form IV. Handled three ways: (i) the label source is a declared deciding
parameter (§6, R1–R3) with the scholar-assigned Neuwirth–Sinai labels — which do **not** use the
substring — as **primary**; (ii) a marker-ablated arm dropping those 91 tokens; (iii) the
`h-new-2500` proxy is secondary only.

---

## 3. Directions, LOCKED and justified from published in-house anchors

Both directions are locked one-sided. Neither is a guess from a grammar textbook — each is the
sign this project already **measured**.

**D1 — Form IV share is HIGHER in narrative than in non-narrative. Locked POSITIVE.**
Justification: H-NEW-2600's causative reverse-controls HOLD, and H-NEW-2650 re-measured the arm at
I→IV = **−0.0633, p = 1.21×10⁻⁶** — Form IV takes overt direct objects *more* often than Form I.
Form IV is valency-increasing: it introduces an external causer acting on a patient. Narrative of
divine agency is exactly the discourse in which an external agent acts on patients.

**D2 — Form V+VI share is HIGHER in legal than in non-legal. Locked POSITIVE.**
Justification: H-NEW-2540/2650's muṭāwaʿa arm, II→V = **+0.2500, p = 4.01×10⁻⁵** — Form V takes
objects *less* often than Form II. V is detransitivising (mediopassive of II), VI reciprocal (of
III). Both background the external agent and foreground participants acting on themselves or each
other, which is the argument structure of community-directed legal discourse.

**Inherited-instrument declaration.** The root-held-fixed design is **INHERITED from H-NEW-2540**
(within-root cells, ≥2 tokens per form per root, weighted smoothed rate difference,
leave-one-root-out). Dependency stated in full: **2540's primary channel is EQTB
parser-contaminated** — the parser had verb form among its inputs — so what I inherit is its
*design*, not its authority. My test uses **QAC only and no treebank**, so the contamination does
not propagate; but the directions in D1/D2 are anchored on the parser-free §2b pronoun channel
(validated by H-NEW-2650, false-hit rate 0.0000 on all eight forms), **not** on the contaminated
primary.

---

## 4. What "independently of root vocabulary" means here, and how much room there is for it

### 4.1 The confound, quantified

Of 943 verb roots, **594 (63 %) occur in exactly one form**. Token-weighted: **6,352 of 19,356 verb
tokens (32.8 %) sit on single-form roots**, where form is *fully determined* by root and carries
zero independent information. Only the **13,004 tokens (67.2 %) on multi-form roots** can move
under a root-held-fixed test. This is the map's named confound, measured before the run.

### 4.2 A lemma-level control would be a TAUTOLOGY, and this answers the lemma-vs-root directive

The brief requires both levels, citing H-NEW-3090's 126× lemma/root p-swing. **At this
construct the two levels are not two settings of one knob — one of them is degenerate.**

> **0 of 1,475 verb lemmas carry more than one form.** In QAC the lemma *is* form-specific
> (`LEM:'aAmana` is Form IV by definition).

A lemma-held-fixed control therefore removes **100 %** of form variance by construction: the
residual is identically zero and the null and the observation coincide. Running it would produce a
clean, well-formed, meaningless NULL. Per the standing rule *"check every control for tautology"*
(learned from H-NEW-2600's 17/34 coin-flip), **it is not run as a control, and the reason is the
finding.** Root is the only level at which the control has content.

The meaningful lemma/root contrast that *does* survive is the **counting unit** — tokens versus
distinct lemma types — and that is registered as tuple T3 and reported at both levels.

### 4.3 Two independent root controls

- **ROOT-A (primary).** Null B: permute form labels **within root** across tokens, holding each
  token's surah fixed. Preserves every root's corpus-wide form distribution and every surah's root
  inventory; destroys only surah-specific allocation of forms within a root. Direct surah-level
  analogue of 2540's within-root design.
- **ROOT-B (secondary).** Residualised profile `d_s(f) = p_s(f) − e_s(f)`, where
  `e_s(f) = Σ_r n_s(r)·q_r^{(−s)}(f) / Σ_r n_s(r)` is the root-expected profile built from
  **leave-one-surah-out** root form distributions `q_r^{(−s)}` (LOSO to prevent self-inclusion
  driving `d_s` toward 0). Tested under Null A.

---

## 5. Statistics and tests

Per surah `s`, over the 8-form set `F`: counts `n_s(f)`, profile `p_s(f) = n_s(f) / Σ_F n_s(f)`.

### 5.1 H1 — does the form profile predict register at all?

Statistic **S1 = leave-one-out nearest-centroid classification accuracy** of register label from
`p_s`, Euclidean distance, classes with n ≥ 5 only (drops `liturgical`, n = 1, Q1 — a singleton
class has no centroid when left out). Null A: shuffle register labels across surahs, 10,000 perms,
seed 20260509. One-sided (accuracy above null).

- **H1-RAW**: S1 on `p_s` under Null A.
- **H1-ROOT**: S1 on `p_s` recomputed under Null B (seed 20260510). **PRIMARY.**

### 5.2 D1, D2 — the locked directional arms

`D1 = mean_{narrative} p_s(IV) − mean_{¬narrative} p_s(IV)`, one-sided positive.
`D2 = mean_{legal} [p_s(V)+p_s(VI)] − mean_{¬legal} [·]`, one-sided positive.
Each under Null A (RAW) and Null B (ROOT).

### 5.3 Length: three variables, all run, WORST is the headline

No single channel is locked. Every inference is computed under four settings and the **maximum
(worst) p across them is the headline**; the **dominant** channel — the one moving the p-value
most — is named in the finding.

`L0` none · `L1` residualised on log(verse count) · `L2` on log(word count) ·
`L3` on log(mean verse length). Residualisation is OLS of each form share on the log length
variable across surahs; the statistic is recomputed on residuals.

### 5.4 Effective n, and a structural limit that is fatal to the causal reading of D1/D2

Under this file's coarsening (§6, C1), `sinai_genre` × phase:

| register | Meccan | Medinan | |
|:--|--:|--:|:--|
| eschat | 15 | 0 | degenerate |
| **narrative** | **26** | **0** | **degenerate — D1's target class** |
| **legal** | **0** | **17** | **degenerate — D2's target class** |
| oath | 15 | 0 | degenerate |
| hymn | 8 | 1 | |
| polemic | 6 | 1 | |
| other | 17 | 4 | |
| liturgical | 0 | 0 | degenerate |

**75 of 114 surahs (65.8 %) sit in a phase-degenerate register stratum. Nominal n = 114; effective
n against phase = 39.**

> **Both of my locked directional arms target perfectly phase-degenerate classes.** Narrative is
> 26/0 and legal is 0/17. Per `findings/AUDIT-REGISTER-PHASE-COLLINEARITY.md` §3, no estimator
> recovers a within-stratum contrast from a stratum with one level. **D1 and D2 therefore cannot
> be separated from Meccan/Medinan phase by any amount of stratification, and I am not going to
> claim otherwise after the fact.** A pass on D1 or D2 licenses *"the form profile distinguishes
> these surahs"* and **not** *"register rather than phase drives it"*. This is stated before the
> run so it cannot be quietly dropped after one.

My 65.8 % sits above the audit's 36.8–57.0 % range because my coarsening assigns `eschat`
differently — which is the audit's own point that **the coarsening is a deciding parameter**, and
is why C2 (§6) exists.

### 5.5 If the verdict is NULL

Report, per `h-new-3030` §3.5: (a) the **MDE** — smallest effect reaching the binding gate, in
share-difference units for D1/D2 and accuracy points for H1; (b) the **power curve** against
effect size; (c) the **UNTESTABLE-AT-THIS-N branch**, computed not assumed — `S_max` = maximum
attainable statistic (1.0 for LOO accuracy; the maximum attainable share difference given observed
marginals for D1/D2) and `S*` = value needed to hit the gate. **The branch fires iff S* > S_max**,
and whether it fired is stated either way.

---

## 6. Rules-tuples (≥2 required; 3 axes registered)

| axis | setting | role |
|:--|:--|:--|
| **T1** | verb tokens only, Form I = untagged verbs, 8 forms | **PRIMARY** |
| T2 | all form-tagged POS (V+N+ADJ+PN), forms II–X, no Form I | robustness — the brief's counts |
| T3 | distinct lemma **types** not tokens | robustness — the non-degenerate lemma/root contrast |
| **R1** | `sinai_genre`, coarsening C1 | **PRIMARY** — scholar-assigned, no substring overlap |
| R2 | `neuwirth_genre`, coarsening C1 | robustness — second rater |
| R3 | `sinai_genre`, coarsening C2 | robustness — coarsening as deciding parameter |
| **L0–L3** | four length settings | all run, worst = headline |
| A1 | marker-ablated: drop the 91 `يا أيها الذين آمنوا` Form IV tokens | robustness for §2.4 |
| M2 | minimum 20 verb tokens per surah (n = 87) | robustness — profile noise floor |

**C1** = first match in order `legal, narrative, oath, hymn, eschat, polemic, liturg`, else `other`.
**C2** = first match in order `oath, eschat, legal, narrative, hymn, polemic, liturg`, else `other`.
Both applied to the lowercased genre string. The two orders differ on composite labels, which is
exactly where coarsening bites.

---

## 7. Decision rule — EXACT, and the runner's verdict function is diffed against this section

Confirmatory family **k = 6**: {H1-RAW, H1-ROOT, D1-RAW, D1-ROOT, D2-RAW, D2-ROOT}, all at
**T1 × R1**. Bonferroni α = 0.05/6 = **0.008333**. Following the stricter precedent of this
morphology family (H-NEW-2540 raw gate 0.00125; H-NEW-2600 raw gate 0.0005), the **binding raw
gate is p < 0.001**. Tightening only — per the standing rule, a tightening is self-verifying.

An arm **PASSES** iff *(a)* its observed direction matches the direction locked in §3 **and**
*(b)* its **worst** p across L0–L3 is **< 0.001**. Both conditions. Everything outside the six is
descriptive and cannot alter the verdict.

Verdict, evaluated in this order:

1. **`UNTESTABLE-AT-THIS-N`** — iff `S* > S_max` for H1-ROOT (§5.5).
2. **`NULL`** — iff H1-RAW does not PASS.
3. **`ROOT-EXPLAINED`** — iff H1-RAW PASSES and H1-ROOT does not PASS.
   *Reading: the fingerprint is real but is a coarse root profile. The named confound wins.*
4. **`CONFIRMED`** — iff H1-ROOT PASSES **and** at least one of {D1-ROOT, D2-ROOT} PASSES.
5. **`DIRECTIONAL`** — iff H1-ROOT PASSES and neither D1-ROOT nor D2-ROOT PASSES.

Exactly one verdict is reachable. No other verdict string may be emitted.

---

## 8. Forking-paths log — every choice made before the run

1. **Step-0 grep, run before any design** (required by the brief; recorded here per protocol).
   Searched `findings/`, `MASTER-FINDINGS-LEDGER.md`, `HANDOFF/` for: derived form, wazn, verb
   form I–X, Form IV, Form V, muṭāwaʿa, valency, h-new-2540, h-new-2600, stylistic fingerprint,
   per-surah signature, form profile, form distribution, morphological signature/fingerprint.
   - The earlier keyword screen's two flags are **both false positives**: `h-new-750`
     (rhyme-dispersion + entropy) and `h-new-213` (repetition unit) contain no morphology.
   - Real neighbours: **H-NEW-2540** (root × form-pair → P(overt object); primary channel
     EQTB-contaminated), **H-NEW-2600** (5 form-pairs; `LATTICE-STRUCTURED` **retracted**, 2 of 5
     arms pass), **H-NEW-2650** (validates the parser-free channel), **H-NEW-2850** (form →
     subject agency class, **NULL** on both classifiers).
   - **All four are token- or root-level with a grammatical outcome. None is surah-level. None
     touches register or genre.** F-6's unit (surah) and outcome (register) are unoccupied. The
     only corpus hits for "form profile / distribution over verb forms / morphological
     fingerprint" are the FRONTIER-MAP lines defining F-6 itself.
   - Ledger ends at §10.161; highest existing artefact `prereg-h-new-3090`. **3130 is free.**
2. **0-of-6 prior written into §0** rather than inherited from the map's optimism.
3. **Verb-only chosen as PRIMARY over the brief's all-POS counts** (§2.1). Reason: the hypothesis
   says "verb forms". Both run.
4. **Form I derived from absence of a tag** (§2.2). No alternative exists in QAC.
5. **VII/IX/XI/XII dropped for sparsity, and said so** (§2.3), per the brief's instruction not to
   include them silently. XI has zero verb tokens.
6. **V+VI pooled rather than tested separately** — decided by the measured 69.3 % tie fraction on
   VI, before any register contrast.
7. **Neuwirth–Sinai chosen as primary label source over the `h-new-2500` proxy** — because §2.4
   found the proxy's defining substring contains a Form IV verb. Chosen on a construct argument,
   not on a p-value; no register × form quantity had been computed.
8. **Lemma-level control dropped as tautological** (§4.2), with the tautology measured (0 of 1,475
   lemmas multi-form) rather than asserted.
9. **Two root controls registered instead of one** (§4.3), because a single one could not
   distinguish "no surah-specific allocation" from "estimator artefact".
10. **No minimum-token filter in the primary** — a 20-token floor drops 27 surahs and they are
    overwhelmingly the short oath/eschatological surahs, so the filter is confounded with the
    grouping variable. Registered as robustness arm M2 instead.
11. **Class-size floor n ≥ 5 for the classification arm** — drops only `liturgical` (Q1).
12. **Binding gate tightened from Bonferroni 0.008333 to 0.001** to match this family's
    precedent. Tightening only.
13. **Phase-degeneracy limit stated before the run** (§5.4), including that it lands on both
    locked arms' target classes.
14. **What was computed before this file was hashed**, disclosed in full: corpus form counts;
    lemma→form and root→form cardinalities; per-surah verb-token counts; tie fractions of the
    Form IV / V+VI / VI shares; register label frequencies; the register × **phase** crosstab; the
    91 marker-token count. **No register × form quantity, no statistic in §5, and no p-value of
    any kind was computed before hashing.** The register × phase crosstab is a property of the
    label file alone and contains no morphology.

## 9. Honest limits, declared in advance

- **No matched Classical-Arabic control corpus with register labels exists on disk.** Nothing here
  can separate a property of *this text* from a property of Classical Arabic. Ceiling is
  QURAN-INTERNAL. This governs the whole morphology line (H-NEW-2540 §, same limit).
- **Register labels are one scholarly tradition's** (Neuwirth/Sinai), assigned at surah level to
  texts that are internally heterogeneous. A long surah is not one register.
- **D1/D2 cannot be separated from phase** (§5.4).
- **QAC's form tagging is itself an annotation**, unvalidated against an independent Arabic
  morphological analyser here.
- **A surah-level profile is a coarse instrument**: 27 surahs have fewer than 20 verb tokens and 7
  have zero Form IV.
