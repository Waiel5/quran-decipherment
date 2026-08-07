---
finding_id: H-NEW-2740
title: The rasm/imlāʾ divergence set is a lexicon, not a distribution
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
prereg: findings/phase-b-hypotheses/prereg-h-new-2740-rasm-divergence.md
prereg_sha256: 6eee19757e437067679e7286c4d3823ef17589dacdf0ff84c22bd5c27cbb2db7
seeds: 20260509 primary / 20260519 replication
frontier_item: F-9
status: >-
  0 of 5 registered inferences pass. One (I3b) is a pre-commit direction reversal,
  published as NULL. The descriptive arm returns LEXICALLY-DETERMINED at 0.9574:
  95.7 % of rasm divergence is a deterministic property of the word-form, so
  "are divergences clustered?" reduces to "is the vocabulary clustered?".
verdict: >-
  NULL on every registered inference. The naive verse-final enrichment is 1.93×
  at p = 1e-4; conditioned on lexical identity it is p = 0.10. A classical-claim
  audit against al-Suyūṭī's al-Itqān nawʿ 76 returns three EXACT vindications
  (إبرهم, كتاب, سموات), one vindication with caveats (badal-wāw), and one
  NOT-TESTABLE that exposes the study's instrument ceiling.
---

# H-NEW-2740 — The rasm/imlāʾ divergence set

**Pre-reg SHA-256 `6eee1975…2db7`, runtime-verified. Six frozen inputs SHA-verified.
`data/alt-text/quran-uthmani-txt.txt` was read by zero scripts in this repository
before this run.**

---

## Headline

Frontier item F-9 asked whether the words whose ʿUthmānī spelling diverges from
standard orthography cluster by register or position. **They do not, and the reason
is more interesting than the question.**

**95.74 % of rasm divergence is a deterministic function of the word-form.** Of
14,690 orthographic types in the corpus, 12,605 never diverge, 1,990 always diverge,
and **95 alternate**. The rasm is a *list*, not a rule and not a distribution — which
is exactly what makes al-Dānī's *al-Muqniʿ* a catalogue of items rather than a
grammar. Once you know the word, you know its spelling.

That fact **dissolves the question as posed**. Any positional or register clustering
of divergent tokens is, to 95.7 %, the clustering of the vocabulary itself. The only
place a genuine orthographic conditioning effect can live is the 95 alternating
types, and there the corpus supplies **131 informative tokens** — and every test on
them returns NULL.

| # | registered inference | statistic | p | verdict |
|:--|:--|--:|--:|:--|
| **I1** | divergence concentrates in frequent vocabulary (length-stratified) | Δ = **+0.0142** | 0.272 | **NULL** (direction held) |
| **I2** | longer rasm variant enriched verse-finally (within-lexeme) | 25 vs null 22.0 | 0.101 | **NULL** |
| **I3a** | register heterogeneity, omnibus (within-lexeme) | 0.289 vs null 0.225 | 0.276 | **NULL** |
| **I3b** | defective rate higher in eschatological than legal register | **−0.0029** | 0.546 | **NULL — PRE-COMMIT VIOLATION, direction reversed** |
| **I4** | relative position within surah (within-lexeme, two-sided) | +0.136 | 0.064 | **NULL** |

**0 of 5 pass at the Bonferroni α = 0.01.** Both seeds agree.

**And the trap the design was built to avoid fired exactly as predicted.** The
*unconditioned* verse-final divergence rate is **15.17 % against 7.86 %** elsewhere —
a **1.93× enrichment**, 946 observed against a null mean of 524.5, permutation
**p = 1.0 × 10⁻⁴** (the floor at 10,000 draws). Conditioned on lexical identity the
same effect is **p = 0.10**. Verse-final words are rhyme words, rhyme words are the
sound-plural and active-participle templates (ٱلْعَٰلَمِينَ، ٱلظَّٰلِمِينَ، خَٰلِدُونَ), and those
templates are precisely where the rasm omits its alif. **The naive number is real
arithmetic and a worthless inference**, and it is the number this finding would have
reported if the pre-registration had not required lexical conditioning.

---

## 1. The instrument, and what the systematic layers cost

Both texts are 6,236 verses; word counts differ (82,260 vs 82,627) because the
ʿUthmānī text joins words the simple text separates. The pre-registered merge rule
aligned **6,236/6,236 verses** with 366 FASL merges.

**A naive diff would have reported 22,389 divergent tokens (27.2 %).** Four symmetric
normalisations — each applied to *both* texts, so none can manufacture a divergence —
remove **15,470 of them, 69.1 % of the naive diff**:

| layer | what it quarantines | tokens removed | exceptionlessness test | result |
|:--|:--|--:|:--|:--|
| **N1** | ٱ alef wasla → ا | **10,850** | count of ٱ in the simple text | **0 — SYSTEMATIC** |
| **N2** | ى → ي (yāʾ dotting) | **3,508** | word-final ي in the ʿUthmānī skeleton | **0 of 6,016 — SYSTEMATIC** |
| **N3** | آ → ا (madda) | **272** | count of آ in the ʿUthmānī skeleton | **0 — SYSTEMATIC** |
| **N4** | hamza carriers → bare skeleton | **840** | none — conservative by construction | quarantined |

N2 is the sharpest of these: the ʿUthmānī text contains **6,046 word-final ى and not
one word-final ي**, against the simple text's 3,469 and 2,595. That is a dotting
convention with zero counterexamples in 82,260 tokens, and treating it as rasm
divergence would have inflated the headline by a fifth.

**Residual rasm divergence set: 6,919 tokens = 8.41 % of tokens, in 2,093 distinct
skeleton-pairs.**

## 2. The typology

Classified by edit operation, mapped onto the six-fold scheme **al-Suyūṭī states
verbatim** in *al-Itqān fī ʿulūm al-Qurʾān*, al-nawʿ al-sādis wa-l-sabʿūn (*fī marsūm
al-khaṭṭ wa-ādāb kitābatihi*):

> قلت، وسنحصر أمر الرسم في **الحذف** و**الزيادة** و**الهمز** و**البدل** و**الفصل**، وما فيه **قراءتان** فكتب على إحداها

(`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`: the section
opens at line 23216, this sentence is at line 23255, and the six *qawāʿid* follow at
lines 23257 *al-ḥadhf*, 23336 *al-ziyāda*, 23397 *al-badal* [*al-hamz* preceding it],
23418 *al-waṣl wa-l-faṣl*, 23453 *mā fīhi qirāʾatān*.)

> **Erratum against the pre-registration.** Pre-reg §5 cites this sentence at line
> **23252**; the correct line is **23255**. The quoted Arabic, the file, and the
> section opening at 23216 are right; only the line number is wrong. **The
> pre-registration has deliberately not been edited** — its SHA
> `6eee1975…2db7` is embedded in the runner and recorded in four run manifests, and
> silently correcting a locked file would break the only chain that makes the lock
> mean anything. The error is recorded here instead.

| class | tokens | distinct pairs | classical name | examples |
|:--|--:|--:|:--|:--|
| **HADHF-ALIF** | **5,389** | 1,598 | al-ḥadhf | السموت \| السماوات · الكتب \| الكتاب · الظلمين \| الظالمين |
| **FASL** | 366 | 58 | al-waṣl wa-l-faṣl | يايها \| ياايها · يقوم \| ياقوم |
| **BADAL-YA-ALIF** | 343 | 189 | al-badal | التورية \| التوراة · اتيهم \| اتاهم |
| **HADHF-YA** | 269 | 85 | al-ḥadhf | النبين \| النبيين · يحي \| يحيي |
| **BADAL-WAW-ALIF** | 177 | 20 | al-badal | الصلوة \| الصلاة · الحيوة \| الحياة · الزكوة \| الزكاة |
| **MIXED** | 100 | 28 | — | ابرهم \| ابراهيم · اسريل \| اسراييل |
| **ZIYADA-ALIF** | 96 | 47 | al-ziyāda | اولوا \| اولو · يدعوا \| يدعو |
| **HADHF-LAM** | 75 | 6 | al-ḥadhf | اليل \| الليل · الذين \| اللذين |
| **ZIYADA-WAW** | 50 | 27 | al-ziyāda | الربوا \| الربا · الملوا \| الملا · جزوا \| جزا |
| **HADHF-WAW** | 35 | 19 | al-ḥadhf | داود \| داوود · يستون \| يستوون |
| **ZIYADA-YA** | 10 | 9 | al-ziyāda | باييد \| بايد · تلقاي \| تلقا |
| **BADAL-OTHER** | 6 | 5 | al-badal | بصطة \| بسطة · ويبصط \| ويبسط |
| **ZIYADA-OTHER** | 2 | 1 | — | يذا \| يا |
| **HADHF-OTHER** | 1 | 1 | al-ḥadhf | نجي \| ننجي |
| **HAMZ** (quarantined by N4) | 840 | — | al-hamz | — |

**ḥadhf al-alif alone is 78 % of the divergence set.** The tail is long and thin:
seven classes together account for under 300 tokens.

**Systematic vs genuine, stated as the split the brief asked for:**

- **15,470 tokens (69.1 % of the naive diff) are SYSTEMATIC** — three exceptionless
  dotting/diacritic conventions plus the hamza quarantine.
- **6,919 tokens (30.9 %) are genuine rasm divergence.**
- **Within that genuine set, 6,624 tokens (95.74 %) are lexically invariant** — the
  word determines the spelling — and only **295 tokens** belong to types that are
  written two ways.

## 3. The alternating set — where the whole question actually lives

95 orthographic types alternate. After stratifying on the pausal form (the rasm does
not encode iʿrāb, so two tokens differing only in case-ending are the same rasm
target) the analysis set is **86 strata / 1,237 tokens / 131 informative
minority-cell tokens**. A sample:

| tokens | word | rasm variants |
|--:|:--|:--|
| 416 | قَال | قال 412 · **قل 4** |
| 58 | إِبْرَاهِيم | ابرهيم 43 · **ابرهم 15** |
| 47 | كِتَاب | كتب 44 · **كتاب 3** |
| 22 | آيَاتِنَا | ايتنا 21 · اياتنا 1 |
| 17 | الْمَلَأ | الملا 13 · الملوا 4 |
| 14 | جَزَاء | جزا 11 · جزوا 3 |
| 13 | سُبْحَان | سبحن 12 · سبحان 1 |
| 13 | ثَمُود | ثمود 12 · ثمودا 1 |
| 10 | الرِّيَاح | الريح 9 · الرياح 1 |
| 10 | الْأَمْثَال | الامثال 5 · الامثل 5 |

This inventory is the empirical counterpart of the classical *al-Muqniʿ* genre: a
list of named exceptions, each of which the tradition records individually because
**no rule generates it**.

## 4. The registered inferences, in full

Bonferroni α = 0.05/5 = 0.01. 10,000 permutations. Every arm is identical at seed
20260519 to four decimal places; only permutation p-values move, by ≤ 0.006.

**I1 — frequency concentration. NULL, direction held.** Pooled across 11
skeleton-length strata over 14,594 types, divergent types are
**Δ = +0.0142 log₁₀-frequency** above non-divergent ones (null mean +0.0002),
**p = 0.272**. The locked prediction — that scribal abbreviation targets frequent
words — points the right way and is nowhere near significant. Length was stratified
out because it is the mechanical confound running the other way.

**I2 — verse-final position. NULL.** 25 longer-variant tokens fall verse-finally
against a null mean of 22.0, **p = 0.101**. Declared underpowered before the run: the
expected count is ~22 events. **See §5 for why this arm is the most important NULL
in the finding.**

**I3a — register omnibus. NULL.** 0.289 against null 0.225, **p = 0.276**.

**I3b — register contrast. PRE-COMMIT VIOLATION, published as NULL.** The locked
direction was *defective spelling higher in `eschatological_mufassal` than in
`legal_medinan`*, on the reasoning that defective → plene is the direction of Arabic
orthographic development and those two registers are the early/late contrast. The
observed contrast is **−0.0029** — the wrong sign, and negligible (p = 0.546). The
prediction is recorded at SHA `6eee1975…` from before the run and it failed. **There
is no chronological orthographic gradient here to find**, at least not one this
corpus's 61 eschatological-register tokens could reveal.

**I4 — position within surah. NULL, and instructively so.** Two-sided, +0.136,
**p = 0.064** under the pre-registered instrument. §6 records what happened when the
instrument was repaired, and why the answer is still NULL.

## 5. The trap, quantified (MW-7 capped, descriptive, no verdict, no α cell)

This was computed after the run to quantify what the pre-registered conditioning
bought. It adds no cell and changes no verdict.

| | divergence rate |
|:--|--:|
| verse-final tokens | **946 / 6,236 = 15.17 %** |
| non-final tokens | **5,973 / 76,024 = 7.86 %** |
| **enrichment** | **1.93×** |
| unconditioned permutation p (labels shuffled across all tokens) | **1.0 × 10⁻⁴** (floor) |
| **the same effect, conditioned on lexical identity (I2)** | **p = 0.101** |

**A finding that shuffled divergence labels against verse position would have
published a 1.93× enrichment at p < 10⁻⁴ and called the rasm fāṣila-conditioned.**
It is not. It is that the corpus puts sound-plural and participle templates at verse
ends, and those templates are where the alif is dropped. The register rates show the
same thing from the other side — even *unconditioned* they are flat
(liturgical 7.74 %, eschatological 8.19 %, narrative 8.61 %, legal 8.62 %), so there
was never a register effect to condition away.

## 6. An instrument defect, found after the run, and its consequence

The pre-registration (§9.5) declared the greedy merge rule "a heuristic … verified
only by 6,236/6,236 coverage, not by hand-checking every merge." **That declared risk
materialised.** On **4 verses of 6,236** — Q 18:86, Q 18:94, Q 28:38, Q 40:36 — the
greedy rule takes a locally cheap unmerged step at يَٰهَٰمَٰنُ / يَٰذَا and then shifts every
remaining token of the verse by one, pairing عَلَى against ٱلطِّينِ. Total skeleton edit
cost over the 363 merge verses: greedy 970, exact 938.

A **declared robustness re-run** (`scripts/h-new-2740-robustness-dp.py`) replaces the
greedy rule with an exact dynamic-programming alignment minimising total edit
distance over the whole verse, imports the primary script unmodified, and overrides
only `align_verse`. **The primary script is byte-identical to what ran.**

Under repair the descriptive results barely move (divergence 6,919 → 6,909; lexical
determinism 0.9574 → 0.9579) and four of five inferences are unchanged. **I4 moves to
p = 0.0091 (0.0075 at the replication seed) — nominally through α = 0.01.**

**It does not survive leave-one-stratum-out, and the verdict stays NULL.**

| | Δ relative position | p (two-sided) |
|:--|--:|--:|
| all 83 strata | **+0.1523** | 0.0083 |
| **drop the قَال stratum** | **+0.0249** | **0.480** |
| drop آيَاتِنَا | +0.1477 | 0.011 |
| drop وَرَاء | +0.1603 | 0.004 |

**One stratum contributes +0.1381 of the +0.1523.** It is قَال, and its minority cell
is **four tokens**: Q 21:112, Q 23:112, Q 23:114 and Q 43:24, where the rasm is قل
without alif while the vocalisation supplied is *qāla*. Three of the four sit at
relative position ≥ 0.949 — at the very end of their surahs. **The entire "positional
law" is n = 4.** Reported as **NULL, non-robust**, on three independent grounds: the
pre-registered instrument returns p = 0.064; the passing instrument was selected
after seeing the primary result; and the effect is one stratum with four minority
tokens. This project has published a verdict off a single arm on a tiny denominator
before (H-NEW-2650), and the correction is not worth repeating.

*A word on those four tokens.* A rasm that omits the alif is compatible with more
than one vocalisation, which is the situation al-Suyūṭī's sixth category (*mā fīhi
qirāʾatān fa-kutiba ʿalā iḥdāhumā*) describes. **His enumerated list in that
qāʿida, as extracted from the file, does not name this word**, so no attribution is
made — the fact is reported, the citation is not invented.

## 7. Classical-claim audit — al-Suyūṭī, *al-Itqān*, nawʿ 76

Descriptive verifications, no p-values, no α cells.

**C2 — إبرهم. EXACTLY VINDICATED.** al-Suyūṭī: *وحذفت الياء من "إبرهم" في البقرة*.
**All 15 tokens spelled ابرهم are in Q 2, and there are none anywhere else in the
corpus.** The other 43 tokens of the name are ابرهيم. An exact, closed, falsifiable
claim about a single surah, stated in the 10th/16th century, that holds token for
token.

**C3 — كتاب written plene in exactly four places. EXACTLY VINDICATED.** al-Suyūṭī
names four: *"لكل أجل كتاب"، "كتاب معلوم"، "كتاب ربك"، "كتاب مبين" في النمل*. Against
**226 defective** tokens of the word, the plene spelling occurs at exactly
**Q 13:38, Q 15:4, Q 18:27 and Q 27:1** — the last being وَكِتَابٍ مُّبِينٍ, in Sūrat
al-Naml. **4 of 4, no more and no fewer.**

**C4 — سموات plene only in Fuṣṣilat. EXACTLY VINDICATED.** al-Suyūṭī: *فإن كان في
الكلمة ألف ثانية حذفت أيضا، إلا "سبع سموات" في فصلت*. Of 190 tokens of the word, the
ʿUthmānī skeletons are السموت (182), سموت (4), والسموت (3) and **سموات exactly once —
Q 41:12, Fuṣṣilat**.

**C1 — the *badal*-by-wāw closed list. VINDICATED, with two notes.** al-Suyūṭī names
eight: الصلوة، الزكوة، الحيوة، الربوا، الغدوة، مشكوة، النجوة، منوة. **Every lexeme
recovered by the BADAL-WAW-ALIF class is on his list and no lexeme is off it** —
حياة، زكاة، صلاة، غداة، مشكاة، مناة، نجاة, across 177 tokens and 20 clitic-bearing
forms. *Note 1:* ربا is recovered under ZIYADA-WAW rather than BADAL-WAW-ALIF,
because ٱلرِّبَوٰا۟ carries both a wāw for the alif and an otiose alif, and the
edit-operation classifier assigns the token to one class. *Note 2:* al-Suyūṭī
appends *غير مضافات* ("not when annexed"); the corpus writes صَلَوٰتَكَ (Q 9:103) and
أَصَلَوٰتُكَ (Q 11:87) with the wāw although both are annexed. That phrase is terse and
another reading of it may be intended; the discrepancy is recorded, not adjudicated.

**C5 — the *ziyāda*-alif of الظنونا، الرسولا، السبيلا (Q 33). NOT-TESTABLE.**
**Tanzil's simple text writes all three with the alif**, so no divergence exists for
any diff between these two files to detect. This is the study's declared ceiling
(§5 of the pre-registration) made concrete on the single most famous item in the
*ziyāda* chapter. What the class *does* recover is al-Suyūṭī's first *ziyāda* rule —
*زيدت ألف بعد الواو آخر اسم مجموع … وآخر فعل* — as اولوا، يدعوا، يتلوا، يرجوا.

**Two unregistered recoveries worth recording.** The classifier independently
surfaced two items al-Suyūṭī names in qāʿida 6: **بَصْۜطَةً (Q 7:69) and وَيَبْصُۜطُ
(Q 2:245)**, written with ṣād where standard orthography has sīn — his
*"بصطة في الأعراف … بالصاد لا غير"*; and **نُـۨجِى (Q 21:88)** for نُنجِي — his
*"ننج المؤمنين بنون واحدة"*. Neither was searched for; both fell out of the edit
classifier.

**Anchors not on disk, and therefore not cited:** al-Dānī *al-Muqniʿ fī rasm maṣāḥif
al-amṣār*; Abū Dāwūd *Mukhtaṣar al-tabyīn*. al-Dānī is cited **only as quoted inside
al-Itqān** (line 23243). `findings/classical-sources/dani-23-site-supplement.tsv` is
al-Dānī's *al-Bayān fī ʿadd āy*, a **verse-counting** work, and is **not** used here.

## 8. Controls — what a genre control would and would not mean

**Stated because the standard matched-partition control does not apply, and silence
would be the dishonest option.**

1. **It cannot be constructed, and not merely for want of data.** The H-NEW-2680 /
   2720 control cuts al-Bukhārī or al-Jāḥiẓ into 114 pseudo-surahs and re-runs the
   statistic. Here the statistic is a **diff between two orthographic editions of one
   text**. There is no ʿUthmānic rasm for ḥadīth or for adab prose; a pseudo-surah
   partition has nothing to diff against. The control has **no analogue**.
2. **What that buys.** "A partition of al-Bukhārī also does this" is unavailable as a
   refutation. That is a real advantage over the nine laws that fell on 2026-08-07,
   and it is the reason F-9 was worth running today.
3. **What it does not buy — and this must travel with the result.** The absence of
   the Arabic-genre control does **not** make anything here a property of *this text*.
   The relevant reference class is not another Arabic text; it is **another scribal
   tradition**. Item-specific defective spellings concentrated in a fixed lexicon are
   a general property of manuscript transmission under scribal economy. Had I1
   passed, it would have been evidence about **scribal practice**, not about the
   composition of the corpus, and would have had to be reported that way.
   **This finding claims no discrimination of any kind.**
4. **The controls that were run.** Every inference uses a within-corpus permutation
   null; I2–I4 condition on lexical identity **exactly**, by stratification; I1
   stratifies out orthographic length. §5 shows what that conditioning was worth: it
   turned a p = 10⁻⁴ artefact into a p = 0.10 non-result.
5. **The missing instrument, named.** A second Arabic text carrying both an attested
   divergent scribal orthography and a modern normalisation, at comparable scale.
   Not on disk, and plausibly not existing.

## 9. Honest limits

1. **The Tanzil ceiling is the largest limit and it is not small.** The divergence
   set is bounded by what Tanzil's simple text chooses to normalise. Two whole
   classical classes are invisible: the **tāʾ-maftūḥa *badal*** (رحمت، نعمت، سنت،
   كلمت، لعنت، شجرت، بقيت، فطرت …) — the ة count is **identical in both texts,
   2,344 = 2,344** — and the **Q 33 *ziyāda* items** of C5. Every count here is a
   count of *Tanzil-visible* divergence and must never be quoted as "the rasm".
2. **I2, I3a, I3b and I4 are underpowered by construction**, and this was declared
   before the run: 86 strata, 131 informative tokens, ~22 expected verse-final events,
   61 eschatological-register tokens. **Their NULLs bound only large effects.** The
   informative statement they carry is not "there is no effect" but "the corpus
   supplies almost no lexically-conditioned orthographic variation to have an effect
   in" — which is the same fact the descriptive arm reports at 95.74 %.
3. **I1 is well powered and its NULL is the more meaningful one** — 14,594 types,
   11 strata — but it tests only which *types* diverge, not which *token* gets which
   variant.
4. **N4 quarantines real hamza divergence** together with convention. It is symmetric
   and shrinks the divergence set, so it is conservative, but HAMZ is a bucket, not
   an analysis.
5. **The register labels are a surah-level proxy** from `h-new-2500`'s four-rule
   decision procedure, reused verbatim and marginal-verified against `h-new-2530`;
   every token in a surah inherits one label. That is coarse for a token-level test.
6. **The alignment defect of §6 was found only because the alternating inventory was
   read by eye.** Four verses in 6,236 is small, but the coverage criterion the
   pre-registration locked would not have caught it, and nothing else in the pipeline
   would have either. Coverage is not correctness.
7. **One reading tradition, one verse division.** Ḥafṣ ʿan ʿĀṣim, Kūfan count. The
   qirāʾāt dimension of al-Suyūṭī's sixth category is touched descriptively only.
8. **The typology was curated by inspecting the diff**, openly and necessarily, before
   any inference was locked. It is post-hoc with respect to the data and prior to
   every statistic. §10 of the pre-registration records exactly what was seen first.

## 10. What should change in the project record

- **`STATE-OF-THE-PROJECT-2026-08-07.md` §5.5 is wrong on one point.** It lists
  "a rasm/imlāʾ divergence set" among instruments "not on disk". **The divergence set
  is constructible from on-disk data** — 6,919 tokens, 2,093 skeleton-pairs, built
  here from two files that were already present. What is genuinely missing is
  qirāʾāt data and a *fuller* normalisation than Tanzil's, per §9.1. **Flagged for
  the ledger keeper; not mine to edit.**
- **`data/alt-text/quran-uthmani-txt.txt` is no longer an idle asset.**
- The four alignment-defect verses (§6) are a hazard for any future work that aligns
  these two files; the DP aligner in `h-new-2740-robustness-dp.py` is reusable.

## 11. Garden of forking paths

- **Choices made after seeing data: one, disclosed in full.** The DP-alignment
  robustness re-run of §6 was written after the primary run, on noticing a spurious
  stratum (`عَلَى → الطين`) in the alternating inventory. It moved I4 from p = 0.064
  to p = 0.009. **The verdict was kept at NULL**, on the pre-registered instrument
  and on leave-one-out. Had the repair been adopted as primary, this finding would
  have claimed a positional law resting on four tokens.
- **The typology (pre-reg §5) was curated from the observed diff before locking**, and
  the pre-registration's §10.1 lists every quantity computed before the lock.
- **The stratification key was chosen on power grounds before any outcome**
  (74 strata / 109 informative → 86 / 131), with the linguistic justification given
  in the pre-registration and the ordering disclosed there.
- **I1 was added to the design after the descriptive work showed I2–I4 would be
  thin**, with its direction locked before computation, and this is recorded in
  pre-reg §10.4 rather than hidden.
- **Bonferroni k = 5 counts I3a and I3b separately**, which tightens α rather than
  loosening it.
- **The post-run classical-audit refinements** (allowing proclitics for C3, and the
  correct query for C4) changed C3 from 3/4 to **4/4** and confirmed C4 at 1/1. Both
  are descriptive verifications with no α, and both corrected a query, not a claim.
- **Run directories are never deleted.** Primary, replication and both robustness
  runs are retained.

## 12. Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2740-rasm-divergence.md`
  (SHA-256 `6eee19757e437067679e7286c4d3823ef17589dacdf0ff84c22bd5c27cbb2db7`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2740.py` (SHA-gated)
- Robustness script: `findings/phase-b-hypotheses/scripts/h-new-2740-robustness-dp.py`
- Runs (immutable, never deleted), each with a repo-relative `manifest.json`:
  `findings/phase-b-hypotheses/runs/h-new-2740/`
  — `…-primary-seed20260509`, `…-replication-seed20260519`,
  `…-robustness-dp-align-seed20260509`, `…-robustness-dp-align-seed20260519`

---

*Run 2026-08-07 by Waiel Al-Shujaa. The rasm is a list, and al-Dānī was right to
write it as one. Five pre-registered inferences returned nothing; the one number
worth having is 95.74 %. Bismillāhi al-Raḥmāni al-Raḥīm.*
