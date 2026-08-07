---
id: H-NEW-2540
title: Form II→V and Form III→VI as directed reductions in overt dependency-object realization
date: 2026-08-07
author: Waiel Al-Shujaa
status: DUAL-FAMILY SUPPORT (Quran-internal; dependency-annotation-limited)
prereg: prereg-h-new-2540-form-v-valency.md
prereg_sha256: affe3762bd942a0612b86d7bb4ef60e27b76802ba49fd9510e9880881eb4ab5e
run: runs/h-new-2540/20260807T002308Z/
seed: 20260509
family: MORPH-2026-07-11-A
---

# H-NEW-2540 — The muṭāwaʿa relation, measured

**Verdict: DUAL-FAMILY SUPPORT. H1 PASS · H2 PASS. No pre-commit violation.
Dependency-annotation-limited; Quran-internal pending a matched Classical-Arabic control.**

Pre-reg SHA-256 `affe3762…4ab5e`, runtime-verified. Seed 20260509 (Null A),
20260510 (H1 Null B), 20260511 (H2 Null B). 10,000 permutations per Monte-Carlo
null. Family of four registered inferences; Bonferroni α = 0.0125, project
novelty rule stricter, so the **raw decision gate is 0.00125**.

This is the project's first use of a **dependency treebank**. The instrument is new;
the finding is a measurement of something classical grammarians described
qualitatively for twelve centuries and nobody had ever quantified.

---

## 1. The claim

For a root *r*, classical Arabic morphology relates Form V (*tafaʿʿala*) to Form II
(*faʿʿala*) as its **muṭāwiʿ** — the "obedient" or resultative-reflexive counterpart.
*ʿallama-hu* (he taught him) → *taʿallama* (he learned). The narrow, testable
consequence:

> P(overt direct object | Form II, root *r*) > P(overt direct object | Form V, root *r*)

Locked before computation. The analogous Form III→VI (*fāʿala* → *tafāʿala*)
was registered as a low-power secondary.

**This is a directed, lossy relation, not an involution.** No inverse V→II operation
is claimed. Lexicalized counterexamples remain counterexamples (§5).

---

## 2. Results

Statistic: weighted within-root smoothed rate difference
`T = Σ w_r (p_rA − p_rB) / Σ w_r`, with `p = (y+0.5)/(n+1)` and harmonic weight
`w = 2 n_A n_B/(n_A+n_B)`.

| | H1 — II→V | H2 — III→VI |
|:--|:--|:--|
| eligible roots | 23 (≥2 tokens/form) | 12 (≥1 token/form) |
| **T** (weighted) | **+0.4895** | **+0.3454** |
| unsmoothed macro | +0.5323 | +0.6195 |
| **Mantel-Haenszel OR** | **21.08** | **22.53** |
| Null A (root sign-flip) | p = 9.999×10⁻⁵ *(MC floor)* | **p = 0.000488** *(exact, all 2¹²=4096)* |
| Null B (token-label) | p = 9.999×10⁻⁵ *(MC floor)* | p = 9.999×10⁻⁵ |
| gate 0.00125 | **PASS** | **PASS** |

Pooled: Form II heads an overt object in **260/347 = 74.9%** of eligible tokens;
Form V in **52/256 = 20.3%**. A 54.6-point gap on lexically matched roots.

**Robustness**

- **Leave-one-root-out: 0.4565 – 0.5293.** No single root carries the effect.
- **Meccan +0.4258 / Medinan +0.4593** — both positive, near-identical. Not chronology.
- **≥1-token sensitivity: 37 roots, T = +0.4828, MH-OR = 21.30** — same answer, wider net.
- **Lineage: 19,356 verbs joined, 100% form agreement, 100% root agreement, 0 unmatched
  either direction, 0 duplicate locations.** The prereg required 100% or abort.
- **Passive orthogonality control: +0.1208** against the +0.4895 object effect. Explicit
  `PASS` verbs are excluded throughout; the residual passive-rate difference is a quarter
  of the object effect. This is a **derivational** contrast, not Form V being covertly passive.

**On the smoothing.** `(y+0.5)/(n+1)` shrinks toward 0.5, so when `n_II > n_V` (17/23 roots)
and the pooled rate exceeds 0.5, it biases `T` *toward* the hypothesis, and Null A's
sign-flip distribution is symmetric about zero and does not absorb that bias. Two things
settle it: the **unsmoothed** macro difference is **larger** (+0.5323 > +0.4895), so
smoothing shrinks rather than manufactures the effect; and **Null B conditions on the
margins**, holding `n_A`, `n_B` and the root's positive total fixed, so it is immune to the
bias by construction. The prereg's insistence on two nulls is what makes this checkable.

---

## 2b. Post-hoc corroboration through an EQTB-free channel

**Not pre-registered. This is a robustness check, not a confirmatory test, and it is
reported as such.** It was run after the primary result, prompted by the circularity
threat in §7.2.

The primary outcome depends on EQTB `Obj` edges. If the treebank's annotators used
morphological form as a cue when assigning those edges, the finding is partly circular.
So: re-measure the same contrast through a channel that touches **no dependency
annotation at all** — the **attached object pronoun**, a clitic that is visible in QAC's
morphological segmentation alone. A verb carries one iff a `PRON` segment follows it
inside the same orthographic word and its person/gender/number differs from the verb's
own subject agreement.

| | Form II | Form V | gap | roots A>B / A<B / tied | exact sign test |
|:--|:--|:--|:--|:--|:--|
| II vs V | 107/347 = **0.308** | 24/256 = **0.094** | **+0.215** | 18 / 1 / 4 | **p = 3.8×10⁻⁵** |
| III vs VI | 13/47 = **0.277** | **0/33 = 0.000** | **+0.277** | 5 / 0 / 7 | p = 0.031 |

**No Form VI token of any paired root carries an object pronoun — zero out of 33.**

The direction and the root-level pattern replicate through a channel that requires only
that QAC correctly segmented a clitic — a far lower-inference judgment than a dependency
edge. The absolute rates are much lower (0.308 vs 0.749) because a suffixed pronoun is
only one way to realize an object; full nominal objects are invisible to this channel.
That is expected and is why this corroborates rather than replaces the primary test.

**What this does and does not settle.** It does not make the result independent — same
roots, same tokens, and QAC is EQTB's own upstream source for morphology. It does
substantially narrow threat §7.2: for the circularity story to survive, the bias would
have to sit in QAC's *segmentation of enclitic pronouns*, which is close to an
orthographic fact, rather than in EQTB's syntactic judgments. Human review of the
blinded validation sample remains the thing that would actually close it.

---

## 3. The perfect dissociations

Six roots split 100% / 0% — every Form II token heads an object, no Form V token does.
All verified against QAC v0.4 and `quran-text/quran-no-tashkeel.json`.

| root | Form II | Form V |
|:--|:--|:--|
| **ز ك و** | 12/12 | 0/8 |
| **ي س ر** | 11/11 | 0/2 |
| **م ت ع** | 16/16 | 0/11 |
| **ط ه ر** | 9/9 | 0/5 |
| **ب ر أ** | 2/2 | 0/5 |
| **ك ب ر** | 4/4 | 0/2 |

### ي س ر — the same theme, the valency flipped

- **Form II, Q 54:17, 54:22, 54:32, 54:40** — *wa-laqad **yassarnā l-Qurʾāna** li-l-dhikr*
  — "We have made **the Qurʾān** easy for remembrance." *al-Qurʾān* is the direct object.
- **Form V, Q 73:20** — *fa-qraʾū mā **tayassara min al-Qurʾān*** — "recite what is made
  easy **of** the Qurʾān." Same root, same theme; *al-Qurʾān* is demoted to a *min*-oblique
  and the verb takes no object at all.

The al-Qamar refrain and the tahajjud verse say the same thing about the same book from
opposite ends of the valency relation.

### ك ب ر — the valency *is* the theology

- **Form II** always takes God as its object: Q 2:185 *li-**tukabbirū Llāha***; Q 17:111
  *wa-**kabbirhu** takbīrā*; Q 74:3 *wa-rabbaka fa-**kabbir***.
- **Form V** never takes an object, and both occurrences are the archetypal sin: Q 7:13,
  Iblīs — *mā yakūnu laka an **tatakabbara** fīhā*; Q 7:146 — *alladhīna **yatakabbarūna**
  fī l-arḍ*.

Magnification directed outward at God is transitive. Magnification turned back on the self
is intransitive — and is arrogance. The morphology carries the distinction.

### ز ك و — who purifies whom

- **Form II**: *yuzakkī-**him*** — Q 2:129, 2:151, 3:164 — the Messenger "purifies **them**."
- **Form V**: Q 20:76 *jazāʾu man **tazakkā***; Q 79:18 (Mūsā to Firʿawn) *hal laka ilā an
  **tazakkā***; Q 80:3, 80:7 *laʿallahu **yazzakkā***.

Prophetic agency takes an object; human self-reform does not.

### ط ه ر — both forms inside one verse

**Q 5:6, the ablution verse, contains both**: *li-**yuṭahhira-kum*** (Form II — God purifies
**you**) and *fa-**ṭṭahharū*** (Form V — "purify yourselves," no object). One verse, one root,
two forms, and the split falls exactly on the divine-agent / human-agent line.

---

## 4. Form III→VI, confirmed by exact enumeration

With only 12 paired roots, Null A was **enumerated exhaustively** — all 4,096 sign-flip
assignments — giving an exact p = 2/4096 = 0.000488, not a Monte-Carlo estimate.

**ب ر ك** is the showcase: Form III *bāraknā **fī**-hā* (Q 7:137, 17:1, 21:71) always governs
an oblique *fī*; Form VI *tabāraka* (Q 7:54, 23:14, 25:1) is the frozen doxological formula
*tabāraka lladhī*, invariably objectless.

**Honest power note.** With 12 roots the smallest attainable exact p is 1/4096 = 0.000244
against a gate of 0.00125, so only the two most extreme sign-flip outcomes can pass. H2 is
therefore a near-degenerate test: it passes, but "passes" here means "T is essentially
maximal." Treat H2 as corroborating H1's direction in a second form-pair, not as
independently strong evidence.

---

## 5. The counterexamples (4/23) — and why they are the right ones

Equal prominence. Four roots do not obey the relation, and each fails for a reason
classical grammarians already named.

- **ع ل م** (II 33/38 vs V 2/2, diff −0.13). *ʿallama* is **ditransitive** (teach someone
  something), so its muṭāwiʿ retains one object. Both Form V tokens sit in a single verse,
  Q 2:102 — *wa-**yataʿallamūna mā yaḍurruhum** wa-lā yanfaʿuhum*. This is one lexical
  context, not a broad refutation, and the ditransitive carve-out is textbook.
- **و ف ي** (II 8/9 vs V 20/20, diff −0.11). Form V *tawaffā* is lexicalized as a transitive
  theological verb with God as agent — Q 3:193 *wa-**tawaffanā** maʿa l-abrār*. Most Form V
  tokens of this root are explicitly `PASS` (*yutawaffawna*) and were excluded by design;
  what remains is a specialized sense that overrides the muṭāwaʿa.
- **م ن ي**, **د ب ر** — exactly 0.00, both forms saturated.

The relation is a strong tendency with principled exceptions. That is what the pre-registration
claimed it was, and it is why the pre-reg forbade calling it a semantic algebra.

---

## 6. What is and is not novel

**Not novel:** the direction. Muṭāwaʿa is standard classical morphology — Sībawayhi and the
whole ṣarf tradition. Any first-year Arabic student learns *ʿallama* → *taʿallama*. Reporting
this as a discovery would be dishonest.

**Novel:**
1. **It had never been measured.** The relation was stated qualitatively for twelve centuries
   and never quantified on any corpus.
2. **The magnitude.** MH-OR ≈ 21 in both families is far larger than "tendency" suggests.
3. **The within-root design.** Comparing II against V *of the same root* removes lexical
   identity as a confound — this is what makes it a measurement rather than an aggregate
   impression.
4. **III→VI.** The *fāʿala*/*tafāʿala* muṭāwaʿa is much less discussed than II/V; here it is
   confirmed by exhaustive enumeration.
5. **The passive-orthogonality control**, separating derivational valency from inflectional voice.
6. **The counterexample roster** — the four failures are lexicalized in theologically specific
   ways, and that roster is itself a result.

---

## 7. Honest limits

1. **Dependency-annotation-limited.** The outcome is *realized dependency-object profile*, not
   semantic valency. An omitted, oblique, incorporated or context-recoverable participant stays
   semantically present without an EQTB `Obj` edge; conversely `Obj` includes clausal and
   quotational complements. `validation-sample.tsv` (75 rows, 8 strata, blinded) is written with
   **blank review columns**; until qualified reviewers report precision, recall and
   **differential error by form**, every number here is annotation-limited. Differential error
   by form would be fatal, and only human review can rule it out.
2. **Circularity risk, unresolved.** If EQTB annotators used morphological form as a cue when
   assigning `Obj` edges, the result is partly circular. Nothing in this run excludes that. It
   is the single most important open threat.
3. **Not Quran-specific.** No claim that this is a property of the Qurʾān rather than of
   Classical Arabic. Establishing that requires a matched Classical-Arabic dependency-treebank
   control, which is not registered and not run. Per prereg §7 this is
   **QURAN-INTERNAL SUPPORT**, not a full Phase-B finding.
4. **Small N.** 23 and 12 roots. H2 is near-degenerate (§4).
5. **Eligibility threshold.** ≥2 tokens/form is a researcher degree of freedom; the ≥1
   sensitivity (37 roots, T = +0.4828) gives the same answer, which is reassuring but was
   registered as a sensitivity, not a primary.

---

## 8. Provenance

- Pre-registration committed in three versions **before any corpus computation**
  (`333e5fa0c` → `df8a4c9d4` → `1f6d31f89`); each amendment strictly tightened.
- The analysis script as first written embedded the SHA of amendment 2 and implemented its
  looser gates. It was brought into conformance with the final locked prereg **before the
  first run**: raw gate 0.005 → **0.00125** (4× stricter), lineage gate 95%-warn →
  **100%-or-abort**, Null B seeds 20260510/20260511 as locked, and the superseded
  `object-edges-sample.tsv` replaced by the required blinded `validation-sample.tsv` +
  `validation-key.json`. No run directory existed at the time of correction, so no result
  was ever seen under the looser gate. **The finding passes the stricter gate.**
- Inputs verified by SHA-256 at runtime: QAC v0.4 `a1d12923…`, EQTB `Quranic.csv` `a303c24c…`,
  revelation order `74f52ec1…`, `quran-no-tashkeel.json` `253f72f3…`. The EQTB hash was
  recorded in the pre-registration before the file was ever on this machine.
- Immutable run: `findings/phase-b-hypotheses/runs/h-new-2540/20260807T002308Z/`.
- **Determinism check.** The analysis was executed twice, from two different input paths, with
  every seed a fixed literal. `result.json`, `validation-sample.tsv` and `validation-key.json`
  were **byte-for-byte identical** across both executions. The first execution was superseded
  before publication and was never committed; the committed run is the reproducible one.
  Anyone with the two hashed inputs can regenerate this result exactly.

---

## 9. Cross-references

- **cross-finding-028-formal** (register-coded discourse grammar) — that law codes register at
  the *particle and person-deixis* grain. This adds a **derivational-morphology** grain to the
  same picture: the corpus's grammatical distinctions are load-bearing at every level examined.
- **The retirement/vindication ledger** — the recurring signature holds again. Classical
  grammatical and census scholarship verifies under proper nulls; modern numerology does not.
  Muṭāwaʿa joins al-Dānī's *kallā* census and al-Biqāʿī's naẓm on the vindicated side.
- **h-new-2510** (divine-self-reference density, NULL) — both findings say the same thing from
  opposite directions: token-level *density* could not recover a theological class, but
  token-level *grammatical form* separates agency cleanly. Structure lives in the grammar, not
  in the counting.
