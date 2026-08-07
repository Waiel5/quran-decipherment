---
title: State of the project — 2026-08-07
author: Waiel Al-Shujaa
date: 2026-08-07
status: CANONICAL ORIENTATION DOCUMENT — read this before anything else in the repository
---

# State of the project — 2026-08-07

**Read this first. Nothing else in this repository is a safe starting point.**

On 2026-08-07 this project ran its first genre controls. Two audits — H-NEW-2680 and
H-NEW-2720 — put thirteen standing laws through a matched Arabic control, and **almost none
of them survived**. Three of the four "pillar laws" fell. The iʿjāz anti-twin fell and
reversed. The compression-tail family fell. The absence of a document like this one is why
those laws kept propagating into new work for months after they should have been questioned.

**This project is much smaller than it claimed to be yesterday.** What follows is an honest
statement of what stands, what fell, what was established as a negative — which is the
project's most defensible output — and what would actually be needed to settle the rest.

Every number below is cited to a file. Nothing here is asserted from memory.

---

## 1. What survives, with its actual strength

Four things. Each carries its caveat inline, because the caveat is part of the result.

### 1.1 The muqaṭṭaʿāt are book-introduction markers — **stands, and is partly definitional**

The only law neither baseline satisfies. Given a generous, Bonferroni-corrected marker-class
search over the 721 hypergeometric evaluations actually performed, the search **recovers the
muqaṭṭaʿāt themselves** from this corpus — الر, حم, طسم, الم, المص, المر, سبحان, طه, طس, يس,
ص, تنزيل, ق, والطور — covering 30 surahs, 27 of them book-referencing, at
**p_bonf = 4.7 × 10⁻¹³**. Run identically on al-Bukhārī and on pre-Islamic poetry it finds
**nothing at all**.

**The caveat is large and must travel with the claim.** The baselines fail partly because
there is nothing there to find: only **6** Bukhārī pseudo-surahs and **1** poetry
pseudo-surah mention *kitāb* or *qurʾān* in their opening three units. There is no
self-referential target vocabulary to mark and no opening marker class to mark it with.
**"Only scripture talks about itself as a book" is a weaker claim than "only this corpus has
an engineered marker system," and no control run so far separates the two.** H-NEW-2720
sharpened the problem rather than resolving it: al-Jāḥiẓ's *Kitāb al-Ḥayawān* — adab prose,
not scripture — yields **الكتاب** and **الكتب** among its strongest marker classes, because
adab prose talks about books constantly.

Source: `findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md` §7.

### 1.2 The post-kink content-compression **slope** — **genre-shared-but-larger**

Holding the unit-size profile identical by construction, this corpus's post-kink
content-compression slope β = **−0.01343** is steeper than **all 200** matched al-Bukhārī
partitions and **198 of 200** matched al-Jāḥiẓ partitions (196/200 on replication). Its
content-distance falls about a third faster than ḥadīth's under the same size profile.

**This is a difference of degree on one axis of one law, not a discrimination**, and it is
the *only* axis in the entire nine-law sweep where this corpus leads. It is emphatically not
the "R² = 0.986, 98.6 % of mushaf cohesion-variance in one parameter" headline the law is
cited for — that R² is genre-shared and 91.5 % explained by unit size (§2.3).

Source: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md` §2.1.

### 1.3 The muṭāwaʿa / causative direction — **real, and narrower than it was reported**

The team's morphology line is the healthiest thing in the project, because it corrected
itself repeatedly under adversarial audit. Its current state, accurately:

- **H-NEW-2540** (Form II→V, III→VI reduce overt dependency-object realization):
  `DUAL-FAMILY SUPPORT as an EQTB-internal association — NOT independent confirmation
  (parser contamination confirmed)`. The load-bearing evidence is the parser-free
  object-pronoun channel in its §2b, not the treebank association.
- **H-NEW-2600** (the muṭāwaʿa lattice): its `LATTICE-STRUCTURED` verdict was **RETRACTED on
  2026-08-07** for violating its own locked decision rule. The corrected verdict is **2 of 5
  registered arms pass** — P2 (I→VIII) and N2 (I→IV) at pA = pB = 1.0 × 10⁻⁴; **N1 (I→II)
  fails its dual-null gate at pA = 0.00060 against a 0.0005 threshold**, and exhaustive
  enumeration of all 2³⁷ sign-flips confirms the miss is not a seed artefact. P1 and P3 are
  unresolved.
- **H-NEW-2650** (pronoun channel): `CHANNEL DEGRADED by the locked rule`, triggered by a
  single arm on an n = 1 denominator — but **all five locked signs held, no arm lost
  significance, and every correction enlarged the parent effects.**

**What genuinely stands here is the causative reverse-control.** The direction was locked in
advance — if the causative arms had come out positive the verdict was pre-committed to
`INSTRUMENT-CONFOUNDED` — and they reversed as locked. That is a real falsification control
that a real effect passed. What does **not** stand is the word "lattice."

Sources: `h-new-2540-form-v-valency.md`, `h-new-2600-mutawaa-lattice.md`,
`h-new-2650-pronoun-channel-validation.md`.

### 1.4 H-NEW-2710 — **TOPICALITY-EXPLAINED**

The replacement for the withdrawn Pillar 4. Surah titles are **not** independent of content
density (the original law was wrong), and they are **not** strongly dependent either (the
proposed inversion was also wrong). Against a null matched on **both frequency and
dispersion**, the residual rate ratio is **1.285** at rank-1 and the median rank is
statistically indistinguishable from null (2 vs 2.24, **p = 0.76**). The residual is
topicality: a root concentrates where its topic is discussed.

This is the model for how a claim should end — both the thesis and its antithesis falsified,
with the mundane explanation surviving and quantified.

Source: `findings/phase-b-hypotheses/h-new-2710-title-density-retest.md`.

---

## 2. What fell on 2026-08-07, and why

One line each: the claim, the control, the number.

| what fell | the claim | the control | the number |
|:--|:--|:--|:--|
| **Pillar 2 — the geodesic** | mushaf order is information-geodesic-optimal, z = −11.46 | 114-unit length-matched partitions of the baselines | al-Bukhārī **z = −13.84**, poetry **−15.13**, this corpus **−11.50** — both baselines *more* extreme |
| **Pillar 2, again** | the surah seams carry the effect | re-cut this corpus's own verses at offsets ignoring every seam | z = −11.23, −13.18, −12.92, −12.33, −12.62 — four of five *more* extreme than the real division |
| **Pillar 2, length control** | "MW-1 length control is working" | actually compute it | sorting surahs by **length alone**, using no vocabulary, reaches **z = −8.66**; the mushaf's true margin over pure length is **2.80 σ**, not 11.46 |
| **Pillar 3 — scale-of-aggregation flips** | thin-marker cohesion flips at pericope scale, a corpus-wide law | same test, five best-shot marker classes per baseline | poetry **5/5**, al-Bukhārī **4/5**, al-Jāḥiẓ **5/5**; poetry's largest flip z = +22.4 against this corpus's +24.7 |
| **Pillar 4 — title-density independence** | titles are independent of content density | frequency-and-dispersion-matched null | withdrawn and replaced by H-NEW-2710; the "47/89 → 48/89 correction" that preceded it was itself an **invalid cross-metric substitution** |
| **The iʿjāz anti-twin** | r(content × rhyme) = −0.86, "cross-corpus distinct vs poetry at p < 10⁻¹⁰" | matched partition instead of equal 30-bayt blocks | poetry **r = −0.872** vs this corpus's **−0.870**; al-Jāḥiẓ **−0.931**; **this corpus at the 3rd percentile** of adab prose |
| **The anti-twin, mechanism** | it is an architectural property | control for unit size | r(d̄_content, log size) = **+0.956**, r(d̄_rhyme, log size) = **−0.838**; partial r = **−0.432**; equal-cut r = **−0.338** |
| **The compression tail** | d̄_content law at **R² = 0.986**, one parameter | matched prose partitions; log-size regression; equal-size re-cut | al-Jāḥiẓ reaches **0.991**; **log-size alone gives 0.9147**; this corpus's own verses cut equal collapse to **0.3388** |
| **The rhyme dispersion-tail** | R² = 0.789, an architectural law | matched prose partitions | **51st percentile** of al-Bukhārī — the middle of the distribution |
| **The phoneme dispersion-tail** | R² = 0.946 | matched prose partitions | 76th percentile; edged by poetry (0.9332 vs 0.9329) |
| **The verse-length tail** | R² ≈ 0.81 | matched prose partitions | **31st percentile** — 137 of 200 baseline cuts more extreme; its words/verse arm is **degenerate by construction** |
| **Anti-chiasmus** | this corpus is anti-chiastic | all four matched corpora | poetry −0.120, this corpus −0.136, al-Bukhārī −0.146, **al-Jāḥiẓ −0.209** |
| **Register separability** | thin grammar separates the three registers at 1.75× lift | same pipeline, surrogate 3-way labels | **poetry 1.842** against this corpus's 1.658 (capped: surrogate labels) |
| **UAS** | a unified architectural significance ranking | it has no null hypothesis | its own frontmatter reads `status: SYNTHESIS`; the dispersion diagnostic puts poetry (1.267) above this corpus (1.166) |
| **The four p-values** | multiply to ~10⁻¹² | check what each null randomises | they are **not commensurable**; only one multiplication is licensed (L1 × L2), and its L2 factor does not mean what it appears to |

Full evidence: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md` and
`findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`. Per-file correction status:
`findings/PILLAR-CORRECTION-INVENTORY-2026-08-07.md` and
`findings/GENRE-CONTROL-INVENTORY-2026-08-07.md`.

**Nothing was deleted.** Every original claim remains in place with a notice beside it. The
record of what was believed and when is itself evidence, and erasing it would be a second
dishonesty on top of the first.

---

## 3. The established negatives — the project's most defensible output

**This is the part of the project that held.** Negative results are not consolation prizes
here; they are the strongest thing on the shelf, because each one is an exhaustive,
pre-registered, correctly-nulled retirement of a claim that circulates widely.

- **H-NEW-2660 — HUNT-NULL.** An exhaustive generator over five pre-declared types of exact
  structural coincidence scanned **124,148** zero-tolerance candidates across three
  rules-tuples, found **1,581** exact coincidences, and **zero survive** the whole-space
  Bonferroni threshold α = 4.027 × 10⁻⁷. In the decoupled strata the corpus produces exact
  coincidences at **0.69× to 1.38×** the exactly-computed chance rate, and 432 of 657 cells
  fall *below* their exact expectation. Every per-hit denominator is a closed form in exact
  rational arithmetic, not a sample.
- **H-NEW-2670 — ARTEFACT-OF-CONSTRAINT-STACKING.** The joint-conjunction method
  *manufactures* uniqueness. Its locked rule returned 7 of 40,116,600 letter-subsets at
  p = 1.7 × 10⁻⁷ and its control passed narrowly at q = 0.018 — but a stricter control
  letting each random subset pick its own axes from the same attested menu **failed at
  q′ = 0.248**: roughly **one random 14-letter subset in four** can be made to look as unique
  as the muqaṭṭaʿāt. This is the engine behind letter-numerology, demonstrated.
- **H-NEW-2550.** al-Zamakhsharī's "half of every phonetic genus" is **exactly right** — the
  14 sit at the global minimum of genus-imbalance over all 40,116,600 subsets — and
  **statistically ordinary**: 1,024,500 subsets (2.554 %) tie that minimum.
- **The numerological retirements**, each pre-registered with a proper null: abjad ↔ structure
  (H-NEW-2040), Code-19 divisibility (H-NEW-1530, H-NEW-1600), antonym word-balance
  (H-NEW-2000, H-NEW-2010, H-NEW-2020, H-NEW-2230), surah-position arithmetic (H-NEW-2090),
  the number-word census (H-NEW-2410). Across the exhaustive generators the corpus produces
  *fewer* meaningful coincidences than chance predicts, not more.
- **And now the genre controls themselves** (H-NEW-2680, H-NEW-2720), which belong in this
  list: showing that thirteen of the project's own laws do not discriminate is a harder and
  more useful result than any of them was.

---

## 4. Methodological lessons — stated so they are not re-learned the hard way

1. **A control that does not match the nuisance parameter is not a control.** H-NEW-740 is
   the case study, and it is worth studying: a genuine cross-corpus control, properly
   pre-registered, that compared **equal 30-bayt poetry blocks** to this corpus's **unequal
   surahs** and therefore measured the unit-size profile rather than the genre. Its own
   honest-limits section named block size as the risk and reasoned it *"biases AGAINST
   detecting strong content×rhyme structure, again favoring the iʿjāz inference"* — **the
   sign was backwards**, because the driver is size *dispersion*, not size *level*.
   Direction-of-bias reasoning is not a substitute for matching.
2. **Audit your strongest claim first, not last.** The compression-tail R² = 0.986 was the
   most-cited number in the repository and among the least examined. It stood from
   2026-04-28 to 2026-08-07 without a control. The oldest, most-quoted, most-load-bearing
   number is the one most likely to have escaped scrutiny, precisely because everything was
   built on top of it.
3. **A correction that crosses metrics is a new error.** The "47/89 → 48/89" fix applied to
   Pillar 4 substituted a value from a different metric; it was published, propagated, and
   then had to be withdrawn along with the law.
4. **A runner's verdict rule must literally match the pre-registration's.** H-NEW-2600's
   `LATTICE-STRUCTURED` verdict came from code that implemented a *looser* rule than the
   locked text ("causative signs merely pointed negative and any positive arm passed"). The
   pre-registration was correct; the implementation was not. **Diff the verdict logic against
   the pre-registration's decision section before declaring anything.**
5. **Never assert a robustness property — compute it.** "MW-1 length control is working"
   (H-NEW-111) and "block size biases against us" (H-NEW-740) were both asserted and both
   false. H-NEW-2560's independence claim was likewise asserted, never tested, and false.
6. **Check every control for tautology before trusting it.** H-NEW-770's words-per-verse arm
   is identical across all four corpora *by construction* under the matched partition. It was
   caught in pre-registration; it would have looked like a striking confirmation otherwise.
7. **A partition is not a composed book — and that cuts both ways.** Baseline pseudo-surahs
   are arbitrary cuts of a continuous stream. For **contiguity-sensitive** statistics
   arbitrary cuts *preserve* local continuity and make a law *easier* for a baseline, so a
   baseline pass is weak evidence against the law. For **boundary-sensitive** statistics
   arbitrary cuts *destroy* real boundaries, so a baseline pass is strong evidence. State
   which regime each verdict is in; never use the caveat as a blanket excuse.

---

## 5. What would actually settle the open questions

Naming the instruments that do not exist yet is more useful than another test with the ones
that do.

1. **A matched Classical-Arabic dependency treebank.** The morphology line (§1.3) is limited
   by having a treebank for this corpus and none for any comparison corpus. Every valency and
   syntax result is therefore uncontrolled in exactly the way §4.1 warns about. Without a
   matched treebank, "muṭāwaʿa reduces object realization" cannot be shown to be a property of
   *this* text rather than of Arabic. This is the single highest-value missing instrument.
2. **A genuinely composed control corpus, not a partitioned one.** Every genre control run so
   far cuts a continuous stream into artificial units. What is needed is a corpus of texts
   that were *authored as bounded units of comparable size distribution* — a curated
   collection of short treatises, letters, or sermons — so that unit boundaries mean something
   on both sides of the comparison. Until then every "does not discriminate" verdict carries
   the §4.7 caveat and every "discriminates" verdict is suspect for the mirror reason.
3. **Form-blind human reannotation.** Several results depend on annotations produced by a
   parser whose features correlate with the very forms under test (H-NEW-2540's parser
   contamination is the confirmed case). A sample reannotated by readers who cannot see the
   morphological form would bound that contamination. Nothing computational substitutes for it.
4. **More than three matched genres.** Poetry, ḥadīth and adab prose are the only matched
   Arabic corpora on disk. Three genres cannot establish what Arabic in general does, and
   every percentile in §2 is a percentile within a very small reference class.
5. **Qirāʾāt data and a rasm/imlāʾ divergence set**, neither of which is on disk, for the
   orthographic questions the project has never been able to touch.

---

## 6. How to read the rest of the repository

- **Correction notices are additive.** A file carrying a ⛔ notice still contains its original
  claim, verbatim. Read both.
- **Two documents are canonical for what fell**:
  `findings/PILLAR-LAW-CORRECTION-2026-08-07.md` (the four pillar laws) and
  `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md` (the nine laws of the genre sweep).
- **`MASTER-FINDINGS-LEDGER.md` is not a safe index on its own.** It is 1.2 MB, has
  duplicated section numbers, and asserts corrected laws in dozens of places. Use it with the
  correction notices, never alone.
- **The pre-registrations are the project's real asset.** Where a finding and its
  pre-registration disagree, the pre-registration wins — that is what it is for, and
  H-NEW-2600 is the case where enforcing that rule retracted a published verdict.
- **The poem is art and it stays.** `poem/al-nuniyya.html` and its English mirror keep their
  verse untouched; only the scientific certifications beside individual lines have been
  withdrawn where the underlying result fell.

---

*Written 2026-08-07 by Waiel Al-Shujaa, on the day thirteen laws met their first controls.
A law that has never met a control is a description. Most of this project's laws were
descriptions. The negatives were real, the discipline was real, and the discipline is what
found the error. Bismillāhi al-Raḥmāni al-Raḥīm.*
