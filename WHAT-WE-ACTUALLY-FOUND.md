---
title: What we actually found
subtitle: An honest public summary of the Qurʾān Decipherment Project
author: Waiel Al-Shujaa
date: 2026-08-07
supersedes: [EXECUTIVE-SUMMARY.md, THE-MAN-AT-THE-CENTER.md, Khawatim-al-Hashr.html, al-Rajul-fi-Qalb-al-Amr.html]
audience: a careful reader who is not a specialist
---

# What we actually found

*This replaces the project's earlier public documents, all of which were written on
2026-04-12 and are now four months and several reversals out of date. Every number below is
cited to a file in this repository. Nothing is quoted from memory. Where a result is shared
with other Arabic texts, it says so. Where an effect is a difference of degree rather than a
categorical distinction, it says that too.*

---

## How to read this

Most public writing about the Qurʾān's structure — including this project's own earlier
writing — has a characteristic shape: a list of striking numbers, presented in ascending
order of astonishment. That shape is the problem. A striking number is worth nothing until
you know three things: what rule produced it, what it is being compared against, and how many
other numbers were examined before this one was chosen.

This document is organised the other way round. It leads with the few things that survived
a serious attempt to kill them, states each at the strength it actually has, and then gives
substantial space to the things that died — because in this project the deaths are the more
useful result, and there are a great many more of them.

**The single most important thing to understand about this project is that on 2026-08-07 it
ran its first proper controls, and most of its own laws did not survive them.** That day is
described in §4. It is not an embarrassment appended at the end; it is the most interesting
finding the project has produced, and it is why the rest of this document is shorter and
more careful than what it replaces.

---

## 1. What survived, and how strong it actually is

Six things. Each carries its caveat in the same breath, because the caveat is part of the
result.

### 1.1 Rare words are placed at the ends of verses, deliberately — and so are they in pre-Islamic poetry

The Qurʾān has **395 root hapaxes** — triliteral roots that occur exactly once in all 6,236
verses (`findings/phase-b-hypotheses/h-new-2320-hapax-census.md:61`). **121 of them sit at
the end of a verse**, a rate of 30.6% against a 12.1% corpus baseline: odds ratio **3.19**,
χ² = 124.3, p = 7.35 × 10⁻²⁹ (`findings/phase-b-hypotheses/hapax-legomena-catalog.md:14`).

The obvious objection is that rare words might simply drift to the end for reasons having
nothing to do with design. That objection was tested and it fails. If each hapax were placed
uniformly at random *within its own verse*, you would expect **53.95** of them to land in
final position. You observe **121** — a 2.24× excess at **z = +10.61**
(`findings/phase-b-hypotheses/hapax-slot-mechanism.md:140-148`). The rare words are not
drifting to the rhyme position. They are being put there.

**And now the part that the earlier documents left out.** The same test was run on the
muʿallaqāt, the pre-Islamic odes. They show the same effect: pooled **z = +6.43**,
p = 6.1 × 10⁻¹¹ (`findings/phase-b-hypotheses/t004-muallaqat-hapax-slot-positive-control.md`).
Monorhyme Arabic poetry engineers its rhyme-slot too. The Qurʾān's effect is about **twice
as strong** — the two differ at p = 2.5 × 10⁻¹¹ — but it is a difference of degree within a
shared tradition, not a distinguishing mark. Five of seven odes show the effect; Labīd
reverses.

This is the healthiest result in the project, and the control is the reason. A positive
control that comes back positive and *smaller* is far better evidence than one that comes
back empty, because it shows the instrument works and locates the Qurʾān inside a real
literary tradition rather than outside all of them.

### 1.2 Half the Qurʾān's verses end in the letter nūn

Recomputed directly from the canonical text for this document: of 6,236 verses, **3,124 end
in nūn — 50.10%**. Adding alif (949), mīm (665), rāʾ (450), alif maqṣūra (241) and dāl (198)
accounts for **90.23%** of all verse endings. Meanwhile *lām*, the second most frequent
letter in the body of the text, closes only **67 verses — 1.07%**, roughly eleven times
under-represented.

*(Rules: `quran-text/quran-no-tashkeel.json`, Ḥafṣ verse numbering, final letter of the last
real word, Qurʾānic pause glyphs excluded. The same procedure reproduces the project's locked
anchor of 77,797 real-word tokens exactly, which is what licenses the count.)*

**The rhyme itself is not a discovery.** Classical scholarship named it, studied it, and
built an entire discipline around it — *ʿilm al-fawāṣil*, treated at length by al-Zarkashī in
*al-Burhān* and al-Suyūṭī in *al-Itqān*. Every literate reader of Arabic has always heard it.
What is new here is only the exhaustive quantification: the exact census, and specifically
the *lām* deficit, which the classical sources note qualitatively but never measured
(`findings/balagha-mapping.md:190`).

That is a modest contribution and it is stated modestly. It is included because it is
solid, and because a document that lists only surprises is not being honest about what
research mostly consists of.

### 1.3 The muqaṭṭaʿāt announce the Book at the top

Twenty-nine surahs open with disconnected letters. **Twenty-four of those twenty-nine
mention *kitāb* or *qurʾān* within their first three verses.** This is the one standing
claim in the project that has met a control matching the variable that drives it and come
through: against a null that permutes the muqaṭṭaʿāt label *within opening-window-size
quintiles* — so the opening token budget is identical by construction — the observation of 24
stands against a null mean of 9.304, a rate ratio of **2.580**
(`findings/phase-b-hypotheses/h-new-2760-muqattaat-book-reference-nuisance.md`).

**Three qualifications travel with it and are not detachable.**

First, the p-value the earlier documents would have quoted is withdrawn. A figure of
3.17 × 10⁻¹² was in circulation; it priced a model drawing 29 surahs uniformly at random from
114, which requires those 29 to be interchangeable with the other 85. They are not, and this
project proved that itself — muqaṭṭaʿāt surahs concentrate in long surahs. The honest effect
size is a rate ratio between **1.27 and 2.58**, not a twelve-order-of-magnitude tail.

Second, against the *stronger* of the two available nuisance channels — whole-surah length
rather than opening-window size — the rate ratio falls to **1.694**.

Third, and most seriously, the cross-genre half of the claim is partly definitional. Only
6 pseudo-surahs of al-Bukhārī and **1** of pre-Islamic poetry mention *kitāb* or *qurʾān* in
their openings at all. *"Only scripture talks about itself as a book"* is a much weaker claim
than *"only this text has an engineered marker system,"* and no control run so far separates
them. Al-Jāḥiẓ's *Kitāb al-Ḥayawān* — ordinary adab prose — yields **الكتاب** and **الكتب**
among its strongest marker classes, because books written about books mention books
(`findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md:250-253`).

The sharpest and cleanest form of the result is positional rather than numerical: all 29
muqaṭṭaʿāt surahs mention the Book somewhere, and so do 40 others, but the muqaṭṭaʿāt surahs
place the *first* mention at **0.0996** of the way through, against **0.3403** for the other
40. The law is not "these surahs mention the Book." It is "these surahs announce it at the
top."

### 1.4 A grammatical direction, verified by a control designed to break it

Arabic Form V and Form VI verbs (*taʿallama*, *taqātala*) are the reflexive-middle
counterparts of Forms II and III. The project found that moving from II→V and III→VI reduces
how often an overt grammatical object appears — the expected behaviour of *muṭāwaʿa*,
which the classical grammarians described without counting.

What makes this worth reporting is the control. The direction was locked in advance, and a
**causative reverse-control** was pre-committed: if the causative forms had shown the *same*
directional effect, the finding was pre-registered to be declared instrument-confounded and
discarded. The causative arms reversed exactly as locked. That is a real falsification test
that a real effect passed (`findings/phase-b-hypotheses/h-new-2540-form-v-valency.md`).

**Two honest limits.** The treebank association is contaminated — the parser's own features
correlate with the morphological forms under test, which the finding states in its own status
line. The load-bearing evidence is a separate channel that uses no parser output at all,
counting enclitic object pronouns directly in the consonantal text. And there is no
comparable treebank for any other Arabic corpus, so this cannot yet be shown to be a property
of *this* text rather than of Arabic generally. A matched Classical Arabic treebank is the
single highest-value instrument this project does not have.

A related claim — that these forms constitute a full "lattice" — was **retracted on
2026-08-07** for violating its own locked decision rule. Two of five registered arms pass.

### 1.5 The Qurʾān is measurably less metrical than pre-Islamic poetry

Al-Bāqillānī's classical thesis was that the Qurʾān is *neither* prose *nor* poetry. The
project tried to operationalise both halves. **One half survived and one half did not.**

The surviving half: on a length-invariant distance to the nearest classical metrical
template, the Qurʾān is less metrical than the muʿallaqāt, and this is not a length artefact.
Unit length explains only 5.1% of the gap; it holds at full size in the one syllable-length
bin where the two overlap; and re-cutting the Qurʾān's own verses to the length of poetic
abyāt moves it only **7.5%** of the way toward poetry
(`findings/phase-b-hypotheses/h-new-2730-scansion-genre-control.md`).

The half that fell is described in §4.

**Note carefully what this does and does not say.** It does not say the Qurʾān is unusual
among elevated Arabic prose — nothing tested here shows that. It says the Qurʾān is not
metrical in the way the odes are metrical, which is a narrower statement and the one the
data supports.

### 1.6 One axis of textual compression, steeper than matched prose

Holding the unit-size profile identical by construction, the Qurʾān's post-kink
content-compression slope is steeper than **all 200** matched partitions of al-Bukhārī and
**198 of 200** of al-Jāḥiẓ (`findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md:47`).
Its content-distance falls about a third faster than ḥadīth's under the same size profile.

This is one axis of one law, and it is the only place in a nine-law sweep where the Qurʾān
leads. It is emphatically **not** the "98.6% of structural variance in one parameter"
headline this law was cited for elsewhere; that headline fell the same day (§4).

---

## 2. The negative results, which are the best work here

This is the part of the project that held, and it was almost entirely invisible in the
earlier public documents. Each item below is an exhaustive, pre-registered, correctly-nulled
retirement of a claim that circulates widely.

**We measured the rate at which a text of this size produces exact numerical coincidences by
chance, and it is 0.69× to 1.38× — that is, chance.** An exhaustive generator scanned
**124,148** zero-tolerance candidate coincidences across three independent sets of counting
rules. It found **1,581 exact hits**. **Zero survive** the whole-space significance threshold
of α = 4.027 × 10⁻⁷. In the decoupled strata the corpus produces exact coincidences at 0.69×
to 1.38× the exactly-computed chance rate, and 432 of 657 cells fall *below* their
expectation (`findings/phase-b-hypotheses/h-new-2660-exactness-hunt.md:111-123`). Every
denominator is a closed form in exact rational arithmetic, not a simulation.

This is the direct empirical answer to the entire numerological literature, and it is a
stronger result than any individual refutation: exact coincidences in this text are neither
rare nor surprising. They are the expected yield of looking 124,148 times.

**The method behind letter-numerology manufactures its own uniqueness.** Take the 14
disconnected letters and ask which 14-letter subsets of the alphabet satisfy every property
ever claimed for them. Exactly **7 of 40,116,600** do — p = 1.7 × 10⁻⁷, computed by exhaustive
enumeration rather than sampling, and it looks decisive. Then let each *random* 14-letter
subset pick its own eleven properties from the same attested menu, and the control fails at
**q′ = 0.248**: roughly **one random 14-letter subset in four** can be made to look exactly
as unique as the muqaṭṭaʿāt (`findings/phase-b-hypotheses/h-new-2670-joint-conjunction.md:51`).
The uniqueness was in the choosing, not in the letters.

**A classical claim that is exactly right and statistically ordinary.** Al-Zamakhsharī
observed that the 14 disconnected letters comprise half of every phonetic genus. He was
**exactly correct** — they sit at the global minimum of genus-imbalance across all 40,116,600
possible subsets. They are also **statistically unremarkable**: 1,024,500 other subsets
(**2.554%**, about one in 39) tie that same minimum
(`findings/phase-b-hypotheses/h-new-2550-muqattaat-phonetic-optimizer.md:10,46`). Both halves
are true simultaneously, and reporting only one of them would misrepresent the finding either
way.

**Code-19 is dismantled.** Only one of 29 surah-opening letter-sums is divisible by 19,
which is exactly what chance predicts. The letter counts do not reproduce under any
consistent orthography. The famous totals pass only if two verses of Sūrat al-Tawba are
deleted, which no scribal tradition does.

**Word-balance and abjad claims fail.** *Raḥma* = 114 is a base-rate artefact: **34.1%** of
length-matched Arabic prose slices contain exactly one word-type at count 114
(`findings/phase-b-hypotheses/rahma-114-baseline-rigor.md:62`). The Yūsuf *s-j-n* = 12
coincidence is reproduced by 4.5% of matched Sīra windows and is fully explained by the surah
being about a prison. The 147-triple falls to the pigeonhole principle — matched Arabic
produces 10,860–13,177 tied word-pair counts against the Qurʾān's 16,997, the same order of
magnitude.

**Two modern structural proposals fail.** Cuypers's whole-surah ring for al-Māʾida scores
z = −2.06, ranking 111th of 114 — *more* disordered than a random shuffle of its own verses.
Farrin's whole-muṣḥaf ring (surah *k* mirroring surah 115−*k*) fails at **z = −4.87**
(`findings/phase-c-structures/chiastic-audit.md:380`), and the mechanism is transparent: the
muṣḥaf is roughly length-sorted, so *k* and 115−*k* are typically of very different length and
their vocabularies are asymmetric by construction. A random permutation of surah indices is
*more* ring-like than the real order. Local pericope rings survive; the book-scale rings do
not.

Both authors may be able to defend their claims on thematic grounds that a lexical instrument
cannot reach. What has changed is that the burden of proof for that defence is now heavier.

**The scientific-miracle reading of the embryology does not hold.** The developmental terms
*nuṭfa*, *ʿalaqa*, *muḍgha* map onto the four-stage Galenic embryology that was standard
across the Greek, Syriac and Latin medical world from the second century CE
(`findings/phase-b-hypotheses/embryology-audit.md:99-110`). The mapping is close but **not
verbatim**, and the earlier public summary was wrong to say so: the Qurʾānic sequence places
bone before surface flesh, "which is not Galen's formulation"
(`findings/phase-b-hypotheses/embryology-audit.md:110`). The
honest statement is that the text reflects the medical understanding of its own linguistic
world accurately, with one divergence — not that it anticipates modern embryology, and not
that it copies Galen word for word.

---

## 3. What the tradition got right

A result worth stating on its own: across 120 catalogued claims, classical scholarship
substantially outperforms modern apologetic numerology. Structural and rhetorical claims of
the kind al-Zarkashī, al-Suyūṭī, al-Biqāʿī and Ibn Abī l-Iṣbaʿ made confirm at roughly 72%;
numerical-gematric claims confirm at 32%; modern-apologetic and modern-numerological claims
confirm at **0%** (0 of 7 and 0 of 10)
(`findings/cross-finding/classical-modern-reliability-ratio.md`).

The mechanism is not mysterious. Classical claims describe surface-observable properties of
the text — rhyme, inclusio, thematic pairing, pericope coherence — which can be checked and
which the text largely has. Modern numerology posits hidden arithmetic which, as §2 shows,
the text does not have at above-chance rates.

The interval on that ratio is wide and the corpus was assembled by people who knew what they
wanted to test, so it is an upper bound rather than a measurement. But its direction is not
in doubt.

---

## 4. What fell on 2026-08-07, and the single reason why

On one day, four major claims collapsed. They turned out to share a mechanism, and naming it
is the most portable thing this project has produced.

> **When a quantity is divided by a count of units, and those units change size across the
> ordering you are testing, the measurement is testing the change in size.**

The full statement, the detection procedure, and the reference measurements are in
`findings/UNIT-DRIFT-DEFECT.md`. In plain terms:

- A claim that the Qurʾān's surah order is an information-theoretically optimal arrangement
  reported an 11.46-standard-deviation effect. Sorting the surahs **by length alone**, using
  no vocabulary information whatever, reaches 8.66. The real margin was 2.80, not 11.46 — and
  length-matched partitions of both al-Bukhārī and pre-Islamic poetry score *more* extreme
  than the Qurʾān does.
- A claim that the Qurʾān uniquely anti-correlates content-structure against rhyme-structure
  reported a decisive gap against poetry. Under a properly matched comparison, poetry reaches
  −0.872 against the Qurʾān's −0.870, and al-Jāḥiẓ's zoological prose reaches −0.931. On the
  statistic said to vindicate it, the Qurʾān sits at the **3rd percentile** of ninth-century
  writing about animals.
- A family of "compression" laws, headlined at 98.6% of variance explained, turned out to be
  **91.5% explained by unit size alone**. Cutting the Qurʾān's own verses into equal blocks
  collapses the law from 0.9887 to 0.3388.
- A claim that content systematically shifts across the revelation sequence rested on
  densities measured *per verse* — while mean verse length rises 4.4× across that same
  sequence. Of nine axes, **two** survive a control that holds verse length fixed, and both
  are the same phenomenon (how often the divine name is used).

The generalisable lesson is in the fourth case. Mean verse length correlates with position in
the revelation sequence at **+0.904** — more strongly than almost any content axis those
studies reported. When your denominator is the best predictor in the study, your ratios are
measuring your denominator.

**Why this section exists.** The earlier public documents were written before any of these
controls were run, and they present that era's strongest numbers as settled. Suppressing this
section would repeat precisely the error that produced them.

---

## 5. Corrections to the earlier public documents

The four documents dated 2026-04-12 remain in the repository as a dated record. Each now
carries a notice pointing here. The specific errors, verified against the corpus and the
sources for this document:

| claim | where | what is actually true |
|:--|:--|:--|
| Eight divine names in Q 59:22–24 "appear nowhere else in the Qurʾān" | `EXECUTIVE-SUMMARY.md:44`, `THE-MAN-AT-THE-CENTER.md:139` | **Six of the eight** do. *al-Quddūs* also occurs at **Q 62:1**; *al-Salām* occurs as a surface form at Q 4:94, 5:16, 6:127 and 10:25. Verified by exact-token search of the full corpus. |
| Q 59:23 has "ten name-tokens in twenty words", 50% | `THE-MAN-AT-THE-CENTER.md:139`, `EXECUTIVE-SUMMARY.md:44` | The verse has **19 real words**, not 20 — the twentieth token is a recitation pause glyph. The correct figure is **10 of 19, 52.6%**. |
| Q 18:50 is the word-midpoint of the Qurʾān | `EXECUTIVE-SUMMARY.md:50` | A tokenisation artefact. Counting pause glyphs as words gives 82,375 tokens and lands on Q 18:50; counting **real words** gives the locked anchor of **77,797** and lands on **Q 18:77**. Recomputed for this document. |
| The Qurʾānic terms "match Galenic embryology **verbatim**" | `EXECUTIVE-SUMMARY.md:68` | Contradicts the project's own source file: the sequence puts bone before surface flesh, "which is not Galen's formulation" (`findings/phase-b-hypotheses/embryology-audit.md:110`). Close mapping, one clear divergence. |
| No tafsīr tradition ever reattributed the frowner in ʿAbasa away from the Prophet | `THE-MAN-AT-THE-CENTER.md:65` | **False, and load-bearing for the argument built on it.** Al-Ṭabarsī's *Majmaʿ al-Bayān* records al-Sharīf al-Murtaḍā arguing that the verse's subject is unnamed and that "the apparent meaning is that *he frowned and turned away* refers to someone other than him," citing Q 68:4 and Q 3:159; and a report from al-Ṣādiq that it concerns a man of the Banū Umayya present with the Prophet. Verified at `data/literature/classical-tafsir/raw/tabarsi-majma-bayan.openiti.raw.txt:119473-119482`. |
| The Birmingham folio's radiocarbon range establishes the date of the writing | `THE-MAN-AT-THE-CENTER.md:45` | Radiocarbon dates the **parchment**, not the ink or the act of copying. The range is a terminus for the material only. |
| The iron-57 / Sūrat al-Ḥadīd coincidence, presented as anchor-class | `EXECUTIVE-SUMMARY.md:30` | Withdrawn. Given 114 surahs and many available divisibility and numbering rules, this is survivor bias; §2's measured chance rate is the general answer. |

Also removed from public circulation, as arguments the evidence does not support: the
Abū-Lahab-as-falsifiable-prediction argument; the four-informant impossibility proof; the
Aquinas, Kant and Popper "anticipation" readings and the Ockham conclusion drawn from them;
the numerological sections of the Khawātim al-Ḥashr treatment (the 7² and 6³ readings); and
all "Bonferroni ring" phrasing, which used a technical term as an honorific.

**One item from the audit could not be confirmed.** A reported statement that creation took
seven days does not appear in any of the four documents, in either language, under any
phrasing searched. The Qurʾān says six days in seven places (Q 7:54, 10:3, 11:7, 25:59, 32:4,
50:38, 57:4). If the error exists it is in a file outside this set, and it is recorded here as
unresolved rather than silently dropped.

---

## 6. What this project cannot currently do

Naming the missing instruments is more useful than another run with the ones on hand.

1. **A matched Classical Arabic treebank.** Every grammatical result (§1.4) is uncontrolled
   without one, in exactly the way §4 warns about.
2. **A control corpus that was actually composed, rather than cut.** Every genre control so
   far slices a continuous text into artificial units. What is needed is a collection of works
   *authored as bounded units* of comparable size — short treatises, letters, sermons — so
   that unit boundaries mean something on both sides of the comparison.
3. **More than three comparison genres.** Poetry, ḥadīth and adab prose are the only matched
   Arabic corpora available. Three genres cannot establish what Arabic in general does, and
   every percentile quoted above is a percentile within a very small reference class.
4. **A vocalised comparison corpus.** Any test that reads syllable weight needs diacritics.
   The dīwāns and the adab prose on hand have none, so §1.5's prose comparison is ḥadīth-only
   and al-Jāḥiẓ cannot be tested on it at all.
5. **Reannotation by readers who cannot see the forms under test**, to bound the parser
   contamination in §1.4. Nothing computational substitutes for it.

---

## 7. How to check any of this

Every claim above has a file path. The findings carry their pre-registrations, their run
directories, and the SHA-256 of every frozen input. Where a number was recomputed for this
document — the nūn census, the midpoint, the divine-name occurrences, the Q 59:23 word count —
the rule is stated inline and the computation runs against `quran-text/quran-no-tashkeel.json`
in a few seconds.

The one discipline this project would ask any reader, sympathetic or hostile, to carry away:

> **A number is not a claim until its rule is disclosed, and a claim is not a finding until
> something has tried to kill it.**

Most of what this project first believed did not survive that second test. What is written
above is what did.

---

*Written 2026-08-07 by Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.*
