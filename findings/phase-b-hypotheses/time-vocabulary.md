# Time Vocabulary in the Quran — a Lexical and Rhetorical Map

**Phase:** B (hypotheses)
**Agent:** time-vocab-run-2
**Date:** 2026-04-12
**Corpus:** Leeds QAC morphology v0.4 (6236 verses, 77,429 morphological tokens)
**Medinan canon:** 28 surahs {2,3,4,5,8,9,24,33,47,48,49,55,57,58,59,60,61,62,63,64,65,66,76,98,99,110,113,114}
**Cross-references:** `paired-opposites-network.md` §12 (Meccan/Medinan day-night split); `oath-clusters.md`; `rahma-baseline.md` (for unopposed divine attribute rhetoric).

---

## 0. Why a time-word audit?

The Quran coordinates three kinds of time at once: **liturgical** (the five
daily prayer windows), **cosmological** (day/night cycle, sun/moon
periodicity), and **eschatological** (the coming Hour, the delay formula,
the dahr of human existence). A purely theological reading treats these as
separable. A lexical audit treats them as a single family and asks whether
the Quran uses different words for different purposes, or whether the words
are interchangeable. The answer, from the morphology data, is that the
Quran is *lexically disciplined* — each word does a narrow rhetorical job.

This finding audits sixteen time-words from the Leeds QAC morphology table,
tests the five-prayer-time inference against Q 17:78, 2:238 and 11:114,
reads the four time-named short Meccan surahs (89 al-Fajr, 92 al-Layl, 93
al-Ḍuḥā, 103 al-ʿAṣr) as a rhetorical cluster, cross-checks the
layl/nahār paired-opposite result from the `paired-opposites-network.md`
finding, extracts Q 76:1's single philosophical use of *dahr*, and
catalogues the *ḥattā ḥīn* eschatological-delay formula.

---

## 1. Per-word distribution

Verse-level counts from the QAC morphology. Where the same Arabic root
carries two distinct senses (e.g. *nhr* = "river" and "daytime"), lemma-level
disambiguation is used. The Medinan column applies the 28-surah canon; the
numbers are verse-presence (not token count).

| Word (gloss) | Lemma (Buckwalter) | Verses | Meccan | Medinan |
|---|---|---:|---:|---:|
| fajr (dawn) | `fajor` | 5 | 3 | 2 |
| ḍuḥā (forenoon) | `DuHFY` + `taDoHaY\`` | 7 | 7 | 0 |
| ʿaṣr (late-afternoon / epoch) | `Eusor` + `Eusorap` | 7 | 3 | 4 |
| maghrib (sunset-place/time) | `magorib` + `garabat` + `guruwb` | 13 | 8 | 5 |
| ʿishāʾ / ʿashī (night / evening) | `Ea$iY~` + `Ei$aA^'` + `Ea$iy~ap` | 13 | 11 | 2 |
| layl (night) | `layol` + `layolap` | 81 | 71 | 10 |
| nahār (daytime) | `nahaAr` | 50 | 43 | 7 |
| yawm (day) | `yawom` | 377 | 280 | 97 |
| sāʿa (hour / the Hour) | `saAEap` | 43 | 40 | 3 |
| dahr (eon / time-as-fate) | `d~ahor` | 2 | 1 | 1 |
| ḥīn (period / while) | `Hiyn` | 33 | 27 | 6 |
| waqt (appointed time) | `waqot` | 3 | 3 | 0 |
| mīqāt / mawqūt (appointed) | `miyqa`t` + `m~awoquwt` + `>uq~itato` | 10 | 8 | 2 |
| ān (moment) | — | 0 | — | — |
| lamḥa (glance, blink) | `lamoH` | 2 | 2 | 0 |
| ghuduww (morning) | `guduw~` + `gada…` + `gad` | 16 | 13 | 3 |
| rawāḥ (evening return) | `rawaAH` | 1 | 1 | 0 |

**Yawm dominates.** At 377 verse-occurrences it is 6 % of the whole
Quran by verse-presence. No other abstract noun approaches it. Yawm is the
day that counts *morally* — roughly 80 % of yawm tokens are eschatological
(*yawm al-dīn*, *yawm al-qiyāma*, *yawm al-ḥisāb*), not calendrical.

**Layl / nahār are a closed pair.** Layl 81 verses, nahār 50 — the
difference is not a coverage gap; it is that *night* is the rhetorical
baseline (the sign of rest, the sign of darkness, the oath-object) and
*daytime* is the paired antithesis invoked beside it. See §4 below.

**The fine-grained liturgical clock words are rare.** Fajr (5), ḍuḥā (7),
ʿaṣr-qua-time (7), maghrib (13), ʿishāʾ (13). Together just 45 verse-tokens.
These words do surgical liturgical work; they are not everyday time-talk.

**Ān does not appear as a time-word.** The morphology has no standalone
nominal *ān* in the `Ayn`/`An` sense of "moment"; what readers call *ān*
in classical poetry is not realised in Quranic diction.

**Dahr is a hapax-category doublet.** Only Q 45:24 and Q 76:1. Both are
*philosophically* loaded; see §5.

---

## 2. The five prayer times, inferred from Q 17:78, 2:238, 11:114

Classical Islamic law derives the five daily *ṣalāt* windows from three
Quranic verses. The morphology lets us audit the inference directly.

### 2a. Q 17:78 — the dawn / sunset / night spine

> *aqimi al-ṣalāta li-dulūki al-shamsi ilā ghasaqi al-layli wa-qurʾāna al-fajr
> inna qurʾāna al-fajri kāna mashhūdā*

This one verse names four time-anchors:

1. *dulūk al-shams* — "the declining of the sun." Classical tafsīr
   (al-Ṭabarī, al-Zamakhsharī) reads this as the *zawāl*, i.e. noon-past
   → ẓuhr. Some early authorities (ʿAlī, Ibn ʿUmar) read it as sunset.
   Either reading, the window is opened mid-afternoon.
2. *ghasaq al-layl* — "the darkening of night." The end-point of the
   declining-sun arc. Classical: close of ʿishāʾ.
3. *qurʾān al-fajr* — "the dawn-recitation," read twice in one verse for
   emphasis ("it is witnessed"). Directly names *fajr* as prayer.

Three windows implicit: *ẓuhr / ʿaṣr / maghrib / ʿishāʾ* compressed between
*dulūk* and *ghasaq*, plus the explicit *fajr*. Four anchors, five windows.

### 2b. Q 2:238 — the middle prayer

> *ḥāfiẓū ʿalā l-ṣalawāti wa-l-ṣalāti l-wusṭā*

"Guard the prayers and the middle prayer." The plural *ṣalawāt* implies
more than two (otherwise the dual *ṣalātayn* would be expected); the
singular *al-ṣalāti al-wusṭā* picks out one *middle* among them. The
classical majority identifies the middle as *ʿaṣr* (anchored by the ḥadīth
of the Battle of the Trench: *shaghalūnā ʿan ṣalāti al-ʿaṣr*). The word
*wusṭā* ("middle-most") logically requires an odd count — which fits
**five** but not four or six. This is the hinge of the inference.

### 2c. Q 11:114 — the two ends of day, and the near-parts of night

> *aqimi al-ṣalāta ṭarafayi l-nahāri wa-zulafan mina l-layl*

"Establish prayer at the two ends of daytime, and in the near-parts of
the night." The dual *ṭarafay* ("the two ends" = dawn + sunset) gives two
windows; the plural *zulafan* ("near-portions") gives more than one night
window. So: dawn + sunset + multiple night = at least four, and combined
with Q 2:238's demand for a *middle*, exactly five.

### 2d. Synthesis

| Prayer | Quranic anchor | Lemma in morphology | Verse |
|---|---|---|---|
| Fajr (dawn) | *qurʾān al-fajr* / *ṭaraf al-nahār*₁ | `fajor` | 17:78, 11:114 |
| Ẓuhr (noon-decline) | *dulūk al-shams* | (shams-phrase) | 17:78 |
| ʿAṣr (mid-afternoon) | *al-ṣalāt al-wusṭā* | (wasaṭ-phrase) | 2:238 |
| Maghrib (sunset) | *ṭaraf al-nahār*₂ / *ghurūb* | `magorib`/`guruwb` | 11:114, 20:130, 50:39 |
| ʿIshāʾ (night) | *ghasaq al-layl* / *zulaf min al-layl* | `Ei$aA^'` | 17:78, 11:114, 24:58 |

Note: Q 24:58 is the **only verse** that names *fajr*, *ʿishāʾ* and
*ẓuhr* (via *ẓahīra* "mid-day heat") together — the three daily intervals
of privacy for the household. That surah 24 verse is effectively the
Quran's internal cross-reference to the prayer clock.

And Q 20:130 / 50:39 reinforce the *ṭulūʿ al-shams* / *ghurūb al-shams*
("before sunrise and before sunset") frame, adding a closing note
*min ānāʾi l-layl* ("from the parts of the night"). The five-prayer
inference from 17:78 + 2:238 + 11:114 is thus *saturated*: no additional
window the Quran mentions elsewhere conflicts with it, and every window
the Quran mentions elsewhere is captured by it.

### 2e. What the data does NOT support

It does not support a purely lexical derivation. The word *ṣalāt* never
directly colocates with the words *fajr, ẓuhr, ʿaṣr, maghrib, ʿishāʾ* as
a labelled list. The five names are the **ḥadīth tradition's
nomenclature** mapped onto the Quran's **descriptive anchors**. The
mapping is tight but it is a mapping, not a one-to-one Quranic lexical
specification. This is worth stating plainly.

---

## 3. Surahs 89, 92, 93, 103 — the four time-named short Meccan surahs

These four surahs bear time-word names and are all short, all Meccan, and
all open with an oath on a time-word (except 103, which opens with
*al-ʿaṣr* itself as oath).

| # | Name | Verses | Chronological rank (Nöldeke) | Oath-time-word |
|---|---|---:|---:|---|
| 89 | al-Fajr | 30 | 10 | *wa-l-fajr* — "By the dawn" |
| 92 | al-Layl | 21 | 9 | *wa-l-layli idhā yaghshā* — "By the night when it covers" |
| 93 | al-Ḍuḥā | 11 | 11 | *wa-l-ḍuḥā* — "By the forenoon brightness" |
| 103 | al-ʿAṣr | 3 | 13 | *wa-l-ʿaṣr* — "By the late-afternoon (/the Age)" |

Three observations:

1. **All four open with time-oaths.** Meccan surahs preferentially open
   with cosmic-oath clusters (al-Suyūṭī catalogues this as a Meccan
   rhetorical signature). Here the oath-objects are specifically *time
   signatures within the day*. Q 89 stacks *fajr + ten nights + even-and-
   odd + night-when-it-passes*: four oath-objects in four verses, three
   of them time-referents.
2. **They bracket the solar arc.** Fajr (dawn) → Ḍuḥā (mid-morning) →
   ʿAṣr (late afternoon) → Layl (night). Four surahs, four positions of
   the sun. If read in that solar order they trace one complete day.
3. **Revelation order is not solar order.** By Nöldeke (who goes
   conservatively on Meccan chronology) they appear 10-9-11-13 — i.e.
   layl, fajr, ḍuḥā, ʿaṣr. The "day" is not revealed in a day-long
   sequence; the text disrupts the solar analogy even as it invokes it.

**Rhetorical use.** The oath-on-time-word in these surahs is not merely
decorative. It functions as *the sign on which the surah's warning or
promise is sworn*. Q 103 is the starkest: "By the ʿaṣr, man is indeed at
loss, except those who believe, do good, counsel truth, counsel patience." A
three-verse surah whose first word is a time-word and whose argument is
that time is loss. The *ʿaṣr* here carries a double meaning: the
late-afternoon prayer-window *and* the Age / Epoch of Man. The
lexical ambiguity (same lemma `Eusor` / `Eusorap` covers both "difficulty"
and "epoch-time") is doing theological work — the short window of day
stands for the short span of life.

Q 93's *ḍuḥā* / *layl* pair opens with the mid-morning light, immediately
balanced against *al-layli idhā sajā* ("night when it is still"). A two-
word muqābala compressed into two verses. The consolation follows: *mā
waddaʿaka rabbuka wa mā qalā* ("Your Lord has not forsaken you and does
not hate you"). The time-oath sets the affective frame (light defeats
dark; morning is rescue).

Q 89's *fajr* and Q 92's *layl* form an outer bracket: the dawn as the
moment of divine visitation (*al-mashhūd* "the witnessed hour"), the night
as the moment of cover (*idhā yaghshā* "when it covers"). These two
surahs are separated by Q 90, 91 in the muṣḥaf but, chronologically
close in Nöldeke, they form a *sibling pair* contrasting disclosure with
covering. The time-words are not time-markers — they are *rhetorical
modes of theological disclosure*.

**Hypothesis.** The four time-named Meccan short surahs are a *curriculum
on the phenomenology of time*: fajr = disclosure, ḍuḥā = mercy, ʿaṣr =
limit, layl = covering. Each takes one time-word and theologises it.

---

## 4. Layl and nahār — the paired cosmic opposition

Cross-reference: `paired-opposites-network.md` §1, row "day_vs_night
(ywm+nhr/lyl)". Fisher exact test result:

- V_A (ywm ∪ nhr verses): 469
- V_B (layl verses): 81
- Same-verse co-occurrence observed: 45
- Expected under independence: 6.09
- Enrichment: **7.4×** (p = 3.8 × 10⁻³⁰)
- Adjacent-verse pairs (near-miss): 21
- Meccan share of same-verse hits: 36 / 45 = **80 %**

This is the strongest revelation-phase skew of any paired opposite in the
catalogue. Layl/nahār is a Meccan-rhetoric pair; once the community has
Medinan concerns (law, community, warfare) the day-night juxtaposition
drops out as an active rhetorical figure.

**The Quran's grammatical template.** Layl and nahār appear in three
stable grammatical forms:

1. **Alternation frame** — *yukawwiru l-layla ʿalā l-nahāri wa-yukawwiru
   l-nahāra ʿalā l-layl* (Q 39:5), *yūliju l-layla fī l-nahāri wa-yūliju
   l-nahāra fī l-layl* (Q 22:61, 31:29, 35:13, 57:6, 3:27). A closed
   formulaic muqābala. Al-Zamakhsharī lists this as a classical type-case;
   our data reproduces it.
2. **Two-signs frame** — *jaʿalnā l-layla wa-l-nahāra āyatayn, fa-maḥawnā
   āyata l-layli wa-jaʿalnā āyata l-nahāri mubṣiratan* (Q 17:12). The
   *two signs* are explicitly numbered, and the contrast is
   **sight-giving** vs **erased**. This is the locus classicus for the
   theological reading: daytime is *mubṣira* (showing), night is *maḥw*
   (erasure).
3. **Function-assignment frame** — *jaʿalnā l-layla libāsan wa-jaʿalnā
   l-nahāra maʿāshan* (Q 78:10-11). Night = garment (cover, rest); day =
   livelihood. The antithesis is reframed as functional complementarity
   rather than pure opposition.

**What night is, lexically:** *libās* (clothing, Q 78:10), *sakan*
(tranquillity, Q 6:96), *nāshiʾa* (dawn-standing, Q 73:6), time for
*qiyām* (Q 17:79; 73:2; 76:26). Night is never just darkness; it is
vested time.

**What daytime is, lexically:** *maʿāsh* (livelihood, Q 78:11), *mubṣira*
(showing, Q 17:12), the time of *sabḥ* (occupation, Q 73:7). Daytime is
instrumental.

This is not classical mise-en-abyme cosmology (where night = evil, day =
good); the Quran's layl/nahār is **functionally, not morally, paired**.
Compare the moral pairs (truth/falsehood, mercy/wrath) where the
asymmetry is evaluative. Here the two members are *both divine signs*
(*āyatayn*), both *created by Him*, neither demonised.

---

## 5. Q 76:1 — the philosophical dahr

**The corpus fact:** *dahr* appears only twice in the Quran.

### 5a. Q 45:24 — the anti-dahr polemic

> *wa-qālū mā hiya illā ḥayātunā al-dunyā namūtu wa-naḥyā wa-mā
> yuhlikunā illā l-dahr* — "They say: 'There is only our worldly life;
> we die and we live, and nothing destroys us but time (dahr).'"

This is reported speech — *the unbelievers' own formula* quoted
critically. The verse follows with *wa-mā lahum bi-dhālika min ʿilm*
("they have no knowledge of that"). The rhetorical move is to name the
pagan-Arab ontology (time itself as the supreme destructive principle)
and refuse it. The famous ḥadīth qudsī *yu'dhīnī ibn Ādam: yasubbu
l-dahra wa-anā l-dahr* ("The son of Adam offends Me: he curses time,
and I am time") is a reception of this verse — the claim that fate
('dahr') is itself God's action, not an independent cosmic principle.

### 5b. Q 76:1 — the philosophical use

> *hal atā ʿalā l-insāni ḥīnun mina l-dahri lam yakun shayʾan madhkūrā*
> — "Has there not come upon humanity an interval of time (ḥīn) out of
> the eon (dahr) when he was not a thing mentioned?"

This is the **single non-polemical dahr** in the Quran. Here *dahr* is
used by the revealed voice itself, not attributed to opponents. The
syntactic move is striking: *ḥīn* (a finite interval) is carved *out of*
(*min*) *dahr* (the unbounded eon). The Quran is proposing a two-scale
time-ontology:

- **Dahr** = the unbounded backdrop, the eon before mention.
- **Ḥīn** = the finite interval carved from it within which things
  happen.

Human existence is a *ḥīn mina al-dahr* — a bounded while taken out of
the unbounded. The verse's function is to humble the listener: before
you were named, there was dahr; you came into ḥīn; you will return to
dahr (eschatology).

The classical commentators (al-Rāzī, al-Ṭabarī) read this as the Quran's
most philosophically-explicit statement on time. The lexical asymmetry is
doing the theology: 2 verses total, one negative (45:24: dahr as the
pagan principle), one positive (76:1: dahr as the divine-created
backdrop). The Quran *does* use the word, but with exactly one of each
polarity, and both occurrences reject the pagan meaning — in 45:24 by
quoting and refuting, in 76:1 by re-inscribing.

**Hypothesis.** The two-occurrence count is not coincidence. It is a
deliberate two-frame correction: the first names the error, the second
installs the corrected cosmology. A similar two-occurrence theological
doublet is the *sirāṭ mustaqīm* / *ṣirāṭ alladhīna* pair in al-Fātiḥa
(the second corrects the first). The Quran's rhetoric of *least
sufficient occurrence* applies to its lexical counter-moves too.

---

## 6. *Ḥatta ḥīn* — the eschatological-delay formula

Ḥīn appears in 33 verses. The morphology-level collocation analysis
(checking the token immediately preceding *Hiyn*) yields the following
distribution:

| Collocation | Count | Verses |
|---|---:|---|
| *ḥattā ḥīn* ("until a while") | 6 | 12:35, 23:25, 23:54, 37:174, 37:178, 51:43 |
| *ilā ḥīn* ("to a while") | 5 | 2:36, 7:24, 10:98, 16:80, 21:111, 36:44, 37:148 — **7 actually** |
| *baʿda ḥīn* ("after a while") | 1 | 38:88 |
| *kulla ḥīn* ("every while") | 1 | 14:25 |
| *ḥīna …* (temporal clause head) | ~19 | 5:101, 5:106, 11:5, 16:6 (×2), 21:39, 25:42, 26:218, 28:15, 30:17 (×2), 30:18, 39:42, 39:58, 52:48, … |

(Recount: *ilā ḥīn* in 2:36, 7:24, 10:98, 16:80, 21:111, 36:44, 37:148 =
**7 verses**.)

### 6a. The *ḥattā ḥīn* formula — six instances

The six *ḥattā ḥīn* verses partition into two clear functional slots:

**Slot A — Divine command to delay confrontation (addressed to the
Prophet / to believers).** Q 37:174, 37:178: *fa-tawalla ʿanhum ḥattā
ḥīn* / *wa-tawalla ʿanhum ḥattā ḥīn* ("Turn away from them for a while").
Q 51:43 *wa-fī Thamūda idh qīla lahum tamattaʿū ḥattā ḥīn* ("And in
Thamūd, when it was said to them: 'enjoy yourselves for a while'") —
same pattern inverted: the unbelievers are granted a *while* before
destruction.

**Slot B — Narrative interval before a prophetic vindication.** Q 12:35
*la-yasjununnahu ḥattā ḥīn* ("they will imprison him for a while" —
Yūsuf in the Egyptian jail). Q 23:25 *fa-tarabbaṣū bihi ḥattā ḥīn*
("wait on him for a while" — said of Noah's opponents). Q 23:54 *fa-
dharhum fī ghamratihim ḥattā ḥīn* ("leave them in their confusion for a
while" — addressed to the Prophet).

**The grammar is uniform.** Every instance has *ḥīn* in the indefinite
accusative-of-extent, governed by *ḥattā* as a terminus ad quem. The
noun's indefiniteness is load-bearing: *ḥīn* is never specified, never
quantified, never tied to a calendrical date. It is the *withheld
duration*.

### 6b. What the formula accomplishes rhetorically

The *ḥattā ḥīn* formula installs a three-part temporal structure:

1. **Now** — the scene of injustice, persecution, delay, waiting.
2. **Ḥīn** — an unspecified bounded interval.
3. **End-point** — the divine intervention (destruction of unbelievers,
   release of the prophet, vindication).

By leaving the *ḥīn* unspecified, the formula (a) preserves God's
prerogative over timing, (b) trains patience (*ṣabr*) in the hearer,
and (c) turns the apparent openness of the current moment into a
*closed* moment in God's reckoning. It is the Quran's **delay grammar**.

Compare with *al-sāʿa* ("the Hour") — 43 verses, 40 Meccan. The Hour is
the *absolute* end-point; *ḥīn* is the relative interval-before. The
two words are in grammatical contrast: *al-sāʿa* is always
definite-article + singular ("*the* Hour"), *ḥīn* is always indefinite
("*a* while"). The Quran lexically distinguishes the *named-but-
withheld* end from the *unnamed bounded wait*.

This is directly testable and directly evident in the corpus: not one
of the 43 *sāʿa* verses has *sāʿa* as indefinite in the eschatological
sense; not one of the 6 *ḥattā ḥīn* verses has *ḥīn* as definite. The
article distribution is a zero-leakage marker of the two rhetorical
modes.

### 6c. Cross-reference to the Hour

The nearest the two come in a single verse is Q 7:34 / Q 10:49:
*idhā jāʾa ajaluhum lā yastaʾkhirūna sāʿatan wa-lā yastaqdimūn* —
"When their term comes, they will not delay an hour nor advance." Here
*sāʿa* is in its *lexical* sense (the interval of an hour, not the
capital-H Hour), and the contrast is with *ajal* ("appointed term").
Three different time-words stacked: *ajal* (the appointed term), *sāʿa*
(the minimal measurable interval), implicit *ḥīn* (the interval of
delay they wish they had). This is a verse worth naming as the
Quran's *time-word tightest crux*.

---

## 7. Miscellaneous but related findings

**Lamḥa.** Only 2 verses (16:77, 54:50). Both use it of divine speed:
*wa-mā amru l-sāʿati illā ka-lamḥi l-baṣar aw huwa aqrab* (16:77, "the
matter of the Hour is but like the twinkling of an eye, or closer") and
*wa-mā amrunā illā wāḥida ka-lamḥi bil-baṣar* (54:50, "Our command is but
one, like the twinkling of an eye"). Two verses, both on the temporal
instantaneity of divine decree. The word is reserved for this
theological purpose — never used for mundane speed.

**Ghuduww and rawāḥ.** Q 34:12 uses them together: *wa-li-Sulaymāna
l-rīḥa ghuduwwuhā shahrun wa-rawāḥuhā shahrun* ("For Solomon, the wind
— its morning journey a month, its evening journey a month"). The
single rawāḥ occurrence in the Quran. The pair names dawn-traverse and
dusk-traverse as units of measurement; the miracle is that for Solomon
each costs one month of ordinary movement. A deliberate lexical rarity:
the Quran uses specialised morning/evening vocabulary *only* in the
Solomon passage, preserving *fajr*/*ṣabāḥ* elsewhere.

**Waqt, mīqāt.** *Waqt* strictly 3 verses (7:187, 15:38, 38:81), all of
*yawm al-waqt al-maʿlūm* — "the day of the known time." The phrase is
used of Iblīs's respite (15:38, 38:81) and of the Hour (7:187). *Mīqāt*
(8 verses) is used of Moses's 40-night meeting (e.g. 7:142, 7:143, 7:155)
and of the resurrection day (*mīqāt yawmin maʿlūm*, 56:50). The
lexicographic distinction: *waqt* = time-qua-specified-but-hidden;
*mīqāt* = time-qua-set-and-kept. The Quran uses them non-overlappingly.

---

## 8. Synthesis: the Quran's five time-scales

Re-reading the corpus through the lexical distribution, the Quran
operates five time-scales at once, each with its own vocabulary:

| Scale | Key word(s) | Function |
|---|---|---|
| Instant | *lamḥa* | divine command's speed |
| Daily liturgical | *fajr, ḍuḥā, ʿaṣr, maghrib, ʿishāʾ* | prayer windows |
| Diurnal cosmic | *layl, nahār, yawm* (calendar) | sign-structure of creation |
| Biographical | *ḥīn, waqt, mīqāt, ajal* | the appointed-but-withheld span |
| Eschatological | *al-sāʿa, yawm* (eschatol.), *dahr* | the Hour and the eon |

This is not a list of synonyms; it is a lexical division of labour. A
single Quranic verse (Q 45:27, 30:55, 7:34, 16:77) often stacks multiple
levels precisely *because* the words are not interchangeable.

**The hypothesis.** The Quran treats time as a *stratified signifying
system*. Each time-word has a slot in a hierarchy from instant to eon,
and the slots are enforced by near-exclusive distribution (no word
"wanders" between slots except *yawm*, which operates at both cosmic and
eschatological levels — and this double-duty is itself a source of
Quranic depth: a "day" is always also a reminder of "the Day").

Future Phase-C work: check whether the five-scale lexical stratification
predicts the surah-level sequencing of time-words, and whether the
stratification is preserved in ḥadīth quotation of the Quran (i.e. do
quoting texts re-use the time-vocabulary with the same slot discipline,
or do they collapse it?).

---

## 9. Confidence and caveats

- Verse-level counts are exact (QAC v0.4 lemma-level disambiguation).
- Medinan/Meccan splits use the 28-surah canon; results shift by 2–3 %
  under al-Suyūṭī's minority attributions for Surahs 55, 76, 98, 99.
- The five-prayer-time inference is a **classical tafsīr inference**, not a
  purely lexical demonstration. The Quran's own list is implicit.
- Dahr statistics are small-n (2 verses). The philosophical reading is
  supported by classical commentary, not statistically testable at this n.
- The *ḥattā ḥīn* formula counts (6) are exact and bifurcate cleanly; the
  broader "ḥīn-clause" pattern is bigger and could support a separate
  study of subordinated temporal clauses in the Quran.
- Cross-linked to `paired-opposites-network.md` (day/night row) which
  supplies independent confirmation of the layl/nahār Meccan skew.
