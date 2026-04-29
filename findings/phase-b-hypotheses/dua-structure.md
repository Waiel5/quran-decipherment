---
title: Duʿā Structure in the Quran — the Grammar of Supplication
phase: phase-b-hypotheses
agent: dua-run-2
date: 2026-04-12
rules:
  canonical_text: quran-text/quran-no-tashkeel.json
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt (Leeds QAC v0.4)
  matching: morphology-driven — stem LEM:rab~|ROOT:rbb + SUFFIX PRON person/number
  translation_alignment: data/translations/en.sahih.txt
  no_pre_registration: exploratory inventory + prayer-form synthesis
dependencies:
  arabic_text: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  morphology: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  translations: /Users/grey/Downloads/quran/data/translations/en.sahih.txt
  fatiha_deep_dive: /Users/grey/Downloads/quran/findings/phase-c-structures/al-fatiha-deep-dive.md
  vocative_catalog: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/vocative-addresses.md
status: inventory + structural analysis complete
---

# Duʿā Structure in the Quran

The Quran is not only spoken *to* its audience; it is spoken *from*
its audience back to God. Embedded inside the revelation are the
prayers the revelation itself teaches — seeded into narrative,
attached to law-verses, opened at Fātiḥa, closed at the end of
Baqarah. These embedded supplications form a recognisable literary
genre with a stable grammar: a vocative hinge (*rabbanā* "our Lord"
or *rabbī* "my Lord"), followed by one or more imperative verbs
addressed directly to God, often closed by a self-describing
predicate (*innaka antā al-samīʿ al-ʿalīm* — "indeed You are the
Hearer, the Knower"). Classical scholarship calls the genre *duʿā*;
al-Suyūṭī in *al-Itqān* devotes nawʿ 70 to it; Ibn al-Qayyim's
*al-Dāʾ wa-al-Dawāʾ* treats it as the ritual technology of faith.
This document counts, maps, and classifies every Quranic instance.

## Headline numbers

| metric | count |
|---|---:|
| Verses containing *rabbanā* (1P possessive) | **98** |
| Total *rabbanā* tokens (several verses use it multiple times) | **111** |
| Verses containing *rabbī* (1S possessive) | **154** |
| Total *rabbī* tokens | **168** |
| Verses with *rabbaka* (God-to-prophet / 2MS) | 219 |
| Verses with *rabbakum* (addressing an audience / 2MP) | 117 |
| Verses with *rabbuhu / rabbuhum* (3rd-person narrative) | 195 |

The classical figure of "~43 rabbanā" refers to direct-petition
openings — *rabbanā* immediately followed by an imperative or
subjunctive. The broader lexical census is 98 verses. Both counts
are load-bearing: the higher one shows the distribution of the
collective possessive across exegetical discourse; the narrower one
isolates the *prayer-formula* proper.

## 1. The *rabbanā* catalog (98 verses)

Full distribution by surah (verses, sorted):

```
 2: 127, 128, 129, 139, 200, 201, 250, 285, 286               (9)
 3: 7, 8, 9, 16, 53, 147, 191, 192, 193, 194                  (10)
 4: 75, 77                                                     (2)
 5: 83, 84, 114                                                (3)
 6: 23, 27, 30, 128                                            (4)
 7: 23, 38, 43, 44, 47, 53, 89, 125, 126, 149                  (10)
10: 85, 88                                                     (2)
14: 37, 38, 40, 41, 44                                         (5)
16: 86                                                         (1)
17: 108                                                        (1)
18: 10, 14                                                     (2)
20: 45, 50, 73, 134                                            (4)
21: 112                                                        (1)
22: 40                                                         (1)
23: 106, 107, 109                                              (3)
25: 21, 65, 74                                                 (3)
26: 50, 51                                                     (2)
28: 47, 53, 63                                                 (3)
32: 12                                                         (1)
33: 67, 68                                                     (2)
34: 19, 26                                                     (2)
35: 34, 37                                                     (2)
36: 16                                                         (1)
37: 31                                                         (1)
38: 16, 61                                                     (2)
40: 7, 8, 11                                                   (3)
41: 14, 29, 30                                                 (3)
42: 15                                                         (1)
43: 14                                                         (1)
44: 12                                                         (1)
46: 13, 34                                                     (2)
50: 27                                                         (1)
59: 10                                                         (1)
60: 4, 5                                                       (2)
66: 8                                                          (1)
68: 29, 32                                                     (2)
72: 2, 3                                                       (2)
76: 10                                                         (1)
```

**Observations.**
- Three surahs carry the plurality of *rabbanā* invocations:
  Baqara (9), Āl ʿImrān (10), Aʿrāf (10). These three are also the
  three non-Fātiḥa surahs that contain the complete root-set of
  Al-Fātiḥa (cf. deep-dive §10). The congregational voice of
  supplication clusters in the three surahs that most fully
  instantiate Fātiḥa's vocabulary.
- In Āl ʿImrān, five consecutive verses (3:191–194) and three more
  (3:7–9, 3:16, 3:147, 3:53) give *rabbanā* — a ratio of 10 rabbanā
  in 200 verses, the densest stretch in the Quran. Āl ʿImrān
  presents itself as the Quran's most prayer-saturated surah.
- In Aʿrāf, the *rabbanā* uses cluster inside the eschatological
  "people of the Fire / people of the Heights" scene (7:38, 43, 44,
  47, 53) — supplication appears in both praise (7:43 paradise
  residents) and regret (7:38 damned souls, 7:23 Adam/Eve). The
  same lexical formula carries both states.
- *Rabbanā* in Āl ʿImrān 3:191–194 forms a four-step structure
  (realisation → petition → confession → promise-claim) that
  mirrors the four-step Fātiḥa movement (§ 3).

## 2. The *rabbī* catalog — prophet-voice (154 verses)

The singular possessive *rabbī* is the prophet's voice — the
private address, before the community is constituted. It appears
disproportionately in the seven "prophet-narrative surahs":

| surah | *rabbī* verses |
|---|---:|
| Hūd (11)          | 11 |
| Aʿrāf (7)         | 11 |
| Kahf (18)         |  9 |
| Muʾminūn (23)     |  9 |
| Yūsuf (12)        |  8 |
| Shuʿarāʾ (26)     |  8 |
| Qaṣaṣ (28)        |  8 |
| Āl ʿImrān (3)     |  7 |
| Anʿām (6)         |  7 |
| Maryam (19)       |  7 |
| Ṭā-Hā (20)        |  6 |
| Isrāʾ (17)        |  5 |
| Sabaʾ (34)        |  5 |
| Ibrāhīm (14)      |  4 |
| Nūḥ (71)          |  4 |

The ordering is striking. Hūd and Aʿrāf top the list — both are
"cycle-of-messengers" surahs (Noah, Hūd, Ṣāliḥ, Lot, Shuʿayb, Mūsā).
Every messenger speaks *rabbī* as he first confronts his people:
the singular is the formula of *solitary prophetic address*.
The plural *rabbanā* only activates when a community has been
formed — Abraham at the Kaʿba (community of progeny to come),
Moses and the magicians (converts), the companions of the Cave
(wakened youths).

**Grammatical inference.** The rabbī → rabbanā transition is itself
a prayer-shape: the prophet begins in solitude (*rabbī iġfir lī
wa-li-wālidayya* — Nūḥ 71:28), and the umma that follows him
inherits his prayer as its own (*rabbanā iġfir lanā wa-li-ikhwāninā*
— Ḥashr 59:10). The same imperative verb (*iġfir*) survives the
pronoun shift; what changes is whose shoulders carry it.

## 3. Al-Fātiḥa as prayer-form

Classical scholarship calls Al-Fātiḥa *umm al-Kitāb* — the prayer-
template of the whole Book. The Fātiḥa deep-dive (phase-c-structures/
al-fatiha-deep-dive.md) establishes the v5 iltifāt pivot
computationally: 13 words (praise, 3P) | 4 words (pivot, 2P) | 12
words (petition, 2P). With basmala included, v5 is the *exact*
geometric midpoint by words and letters (13 | 4 | 12 words; 61 | 19 |
63 letters — and 19 is also the letter count of the basmala itself).

The resulting **three-part prayer-grammar** is:

1. **Praise** (ḥamd): *al-ḥamdu li-llāh, rabb al-ʿālamīn…* The
   addressee is named in the 3rd person. This is the *taʿẓīm* move —
   magnification through description.
2. **Covenant affirmation** (iltifāt pivot): *iyyāka naʿbudu
   wa-iyyāka nastaʿīn*. The pronoun switches to 2nd person. The
   sentence performs what it says — by saying "You we worship" to
   God, the prayer enacts worship.
3. **Petition** (masʾala): *ihdinā al-ṣirāṭ al-mustaqīm…* Second
   person is retained; imperative verbs appear. The content of the
   petition is *guidance* — the most general possible petition,
   containing all specific petitions as instances.

Every rabbanā / rabbī prayer in the Quran can be mapped onto this
three-part form. The praise phase is often compressed to the
vocative itself (*rabbanā* = "O our Lord" — already an act of
*taʿẓīm* because the possessive acknowledges sovereignty). The
covenant affirmation is marked by *innanā āmannā* ("we have
believed") — a speech-act of declaration of allegiance. The
petition is the imperative stack that follows. A Fātiḥa-shaped
prayer in miniature:

> **Q 3:16** — *rabbanā* (vocative) | *innanā āmannā* (affirmation) |
> *fa-ġfir lanā dhunūbanā wa-qinā ʿadhāba al-nār* (petition)

A full-length mirror of Fātiḥa is **Q 3:191–194**:
- v 191: meditation on creation (*khalaqta hādhā bāṭilan*, 3P on God,
  vocative *rabbanā*) — **praise phase**
- v 192: recognition of divine action (*innaka man tudkhil al-nār
  fa-qad akhzaytahu*, 2P on God) — **affirmation phase**
- v 193: confession (*āmannā*) + petition (*fa-ġfir lanā*)
- v 194: climactic petition (*ātinā mā waʿadtanā ʿalā rusulik*)

The prayer cycles through the same three grammars as Fātiḥa, over
four verses. This is not coincidence; it is **the form
re-instantiating itself**.

## 4. Abraham's prayers (Q 14:35–41, 2:126–129, 26:83–89)

Abraham is the Quran's archetypal supplicant. He appears across
three prayer-cycles, each with distinct grammar:

### Q 14:35–41 — the Mecca prayer
Seven consecutive verses of duʿā. Structure:
- v 35: *rabbī* — *ijʿal hādhā al-balad āmin…* (make this city
  secure; distance me and my sons from idols)
- v 36: *rabbī* — observation (*innahunna aḍlalna…*), then
  consequence (whoever follows me is mine; whoever disobeys — *You*
  are still forgiving-merciful)
- v 37: *rabbanā* — declaration (I have settled my progeny…); then
  *rabbanā* again — *li-yuqīmū al-ṣalāt* (that they may establish
  prayer)
- v 38: *rabbanā* — knowledge-claim (*innaka taʿlamu*…)
- v 39: doxology (*al-ḥamdu li-llāh*) — a full Fātiḥa-style
  *ḥamd* injection mid-prayer
- v 40: *rabbī* — *ijʿalnī muqīm al-ṣalāt* (make me an establisher
  of prayer) | *rabbanā* — *wa-taqabbal duʿāʾī* (accept my
  supplication — the prayer asks for its own acceptance)
- v 41: *rabbanā* — *iġfir lī wa-li-wālidayya wa-li-l-muʾminīn*

The **rabbī ↔ rabbanā alternation** traces Abraham's audience:
*rabbī* when he speaks for himself (vv 35a, 36, 40a); *rabbanā*
when the umma (Ishmael, Isaac, their descendants, future believers)
is in view (vv 37, 38, 40b, 41). The whole sequence is **structured
by pronoun-shift** — the grammar of duʿā visible in the surface
form.

### Q 2:127–129 — the Kaʿba-foundation prayer
Three tight verses, all *rabbanā*:
- v 127: *rabbanā taqabbal minnā — innaka anta al-samīʿ al-ʿalīm*
  (vocative + imperative "accept" + self-describing predicate)
- v 128: *rabbanā wa-jʿalnā muslimayni laka…* — *taʾib ʿalaynā —
  innaka anta al-tawwāb al-raḥīm*
- v 129: *rabbanā wa-bʿath fīhim rasūlan minhum… — innaka anta
  al-ʿazīz al-ḥakīm*

The **closing-formula pattern** is diagnostic: each verse ends with
*innaka anta al-X al-Y* (al-Samīʿ al-ʿAlīm / al-Tawwāb al-Raḥīm /
al-ʿAzīz al-Ḥakīm). The formula names the divine attribute that is
invoked by the specific petition:
- "accept" → "the Hearer, the Knower"
- "turn to us, make us Muslims" → "the Accepter-of-Repentance,
  the Merciful"
- "raise a messenger" → "the Mighty, the Wise"

This is the **self-describing predicate** technique: the prayer
names the divine attribute on which it relies, at the moment it
relies on it.

### Q 26:83–89 — the Shuʿarāʾ prayer
Seven lines, all in the singular *rabbī* voice, but listing plural
concerns:
- v 83: *rabbī hab lī ḥukman wa-alḥiqnī bi-l-ṣāliḥīn* (grant me
  judgment; join me to the righteous)
- v 84: *wa-jʿal lī lisāna ṣidqin fī al-ākhirīn* (a tongue of truth
  among later generations)
- v 85: *wa-jʿalnī min warathati jannat al-naʿīm*
- v 86: *wa-ġfir li-abī — innahu kāna min al-ḍāllīn*
- v 87: *wa-lā tukhzinī yawma yubʿathūn*
- v 88: *yawma lā yanfaʿu mālun wa-lā banūn*
- v 89: *illā man atā llāha bi-qalbin salīm*

The climax (*illā man atā llāha bi-qalbin salīm*) is not petition
but ethical aphorism — the prayer turns into wisdom in its final
breath. This is a **prayer-to-aphorism pivot** pattern visible in
several long duʿās.

## 5. Moses at the burning bush (Q 20:25–35)

Eleven verses, all *rabbī*, all imperatives:

> *rabbī-shraḥ lī ṣadrī | wa-yassir lī amrī | wa-ḥlul ʿuqdatan min
> lisānī | yafqahū qawlī | wa-jʿal lī wazīran min ahlī | Hārūna
> akhī | ushdud bihi azrī | wa-ashrikhu fī amrī | kay nusabbiḥaka
> kathīran | wa-nadhkuraka kathīran — innaka kunta binā baṣīran*

The structure is a **cascade of six imperatives** (ishraḥ, yassir,
iḥlul, ijʿal, ushdud, ashrikh), followed by a **purpose clause**
(*kay nusabbiḥaka… nadhkuraka*), closed by a **self-describing
predicate** (*innaka kunta binā baṣīran*). This is the purest
imperative-stack duʿā in the Quran — the verse unit is dissolved
into a single breathless cascade, letting the petition outrun the
verse-boundary. Twenty:25–28 expand the breast for speech; 20:29–32
request Aaron as helper; 20:33–35 tie the purpose to *dhikr*
(remembrance of God). The prayer's final act (the purpose clause)
is to **ask for the ability to continue the prayer** — grant us
speech, give us a helper, so that we may glorify You.

## 6. Noah (Q 71:26–28, 26:117–118)

Two very different Noah-prayers:

### Q 71:26–28 — the late Noah
- v 26: *rabbī lā tadhar ʿalā al-arḍi min al-kāfirīna dayyāran* (do
  not leave on earth, of the disbelievers, an inhabitant)
- v 27: predicate (*if You leave them, they will mislead Your
  servants*)
- v 28: *rabbī iġfir lī wa-li-wālidayya wa-li-man dakhala baytī
  muʾminan wa-li-l-muʾminīna wa-l-muʾmināt — wa-lā tazid
  al-ẓālimīna illā tabāran*

This is the Quran's **most spatially-bounded prayer** — it
explicitly names "my house" (*baytī*) as a space of inclusion. It
is also the only rabbī prayer that couples a positive petition
(forgive believers) with a **negative petition** (do not increase
the wrongdoers). This negative-imperative form (*lā tazid*) is
structurally identical to *lā tuzigh* (Q 3:8) and *lā tuʾākhidhnā*
(Q 2:286) — a Quranic sub-genre of **prayers-against-worsening**.

### Q 26:117–118 — the earlier Noah
- v 117: *rabbī inna qawmī kadhdhabūn* (complaint — my people have
  denied me)
- v 118: *fa-ftaḥ baynī wa-baynahum fatḥan wa-najjinī wa-man
  maʿiya min al-muʾminīn*

A two-step **complaint → petition** form. The Shuʿarāʾ narrative
uses this template for every prophet: Noah (26:117), Hūd (implied),
Ṣāliḥ, Lūṭ, Shuʿayb — all follow *"my people rejected me → judge
between us and save me"*. The repetition is recognisably liturgical.

## 7. Zechariah for John (Q 3:38–41, 19:4–6)

Two distinct tellings of the same prayer. In **Q 3:38**:
> *rabbī hab lī min ladunka dhurriyyatan ṭayyibah — innaka samīʿu
> al-duʿāʾ* (grant me from Yourself a goodly progeny — indeed You
> are the Hearer of supplication)

The closing predicate names the attribute: *samīʿ al-duʿāʾ*, the
Hearer of supplication. This is one of only two occurrences of this
compound epithet in the Quran (also at 14:39 — Abraham's prayer).
Both are *rabbī* prayers asking for progeny.

In **Q 19:4–6** — the Maryam telling — the prayer expands:
- v 4: *rabbī innī wahana al-ʿaẓmu minnī wa-ishtaʿala al-raʾsu
  shayban wa-lam akun bi-duʿāʾika rabbi shaqiyyan* (description of
  old age + claim that supplication has never been in vain)
- v 5: *wa-innī khiftu al-mawāliya min warāʾī wa-kānat imraʾatī
  ʿāqiran fa-hab lī min ladunka waliyyan* (fear of heirs +
  petition)
- v 6: *yarithunī wa-yarithu min āli Yaʿqūb wa-jʿalhu rabbi
  raḍiyyan* (specification: let him inherit; make him, my Lord,
  pleasing)

The Maryam version uses an **autobiographical preamble** — Zechariah
narrates his condition (*wahana al-ʿaẓm* — the bone has weakened;
*ishtaʿala al-raʾs shaybā* — the head has flamed with white) before
making the petition. This is the **condition-stated duʿā**
pattern, distinct from the *direct-imperative* duʿā of Q 3:38.
Both are valid, both are attested. The pattern is a literary choice:
the longer form lingers on need; the shorter form cuts to petition.

## 8. Mary (Q 3:36–37)

- v 36 (Hannah, Mary's mother, speaking): *rabbi innī waḍaʿtuhā
  unthā* (my Lord, I have delivered a female)

This is the single instance of *rabbī* voiced by a non-prophet woman
in the Quran. The context: Hannah had vowed her unborn child to the
Temple assuming a son; the child was a daughter. The prayer
*describes* rather than *petitions*: the whole verse is a
declaration to God, followed by the blessing "I seek refuge in You
for her" (*wa-innī uʿīdhuhā bika*). The **refuge-formula**
(*uʿīdhu bika*) is the same root-logic as the opening of the
Muʿawwidhāt (Q 113, 114). Here it is a mother protecting her
infant, anticipating the adult believer's *aʿūdhu bi-rabbi al-nās*.

- v 37: Allah accepts the child (*fa-taqabbalahā rabbuhā bi-qabūlin
  ḥasanin*) — the narrative **answers** the prayer in the next
  verse. Note the verb *taqabbala* (accept) is precisely the verb
  Abraham uses at Q 2:127 (*rabbanā taqabbal minnā*); Abraham's
  prayer for acceptance is the form; Hannah's / Mary's story is the
  enacted instance.

## 9. Imperative request-types

The full taxonomy of Quranic request-verbs in duʿā is tractable.
Ranked by frequency in *rabbanā* verses (98 verses scanned):

| imperative | root | gloss | occurrences |
|---|---|---|---:|
| `iġfir / aġfir` | gfr | forgive | 10 |
| `ātinā` | Aty | grant us | 7 |
| `ijʿal` | jEl | make / render | 6 |
| `qinā / qi-nā ʿadhāb al-nār` | wqy | shield us | 4 |
| `unṣur-nā` | nSr | help / grant victory | 3 |
| `akhrij-nā` | xrj | bring us out | 3 |
| `taqabbal` | qbl | accept | 2 |
| `tub ʿalaynā` | twb | turn to us / relent | 2 |
| `afrigh ʿalaynā` | frg | pour out upon us (patience) | 2 |
| `thabbit` | vbt | make firm (footsteps) | 2 |
| `irḥam-nā` | rHm | have mercy | 2 |
| `hab lanā` | whb | bestow / endow | 2 |
| `uktub lanā` | ktb | decree / write | 2 |
| `tawaffanā` | wfy | take us fully (die as Muslims) | 2 |
| `adkhil-nā` | dxl | admit us (to paradise) | 2 |
| `lā tuzigh` | zyg | do not let [our hearts] swerve | 1 |
| `lā tuḥammilnā` | Hml | do not burden us | 1 |
| `lā tuʾākhidhnā` | Axd | do not take us to task | 1 |

The imperatives cluster into **six canonical request-acts**:

1. **Forgive** (*iġfir, kaffir, ʿfu*) — the dominant act. Every
   long duʿā includes a forgiveness-petition.
2. **Grant** (*ātinā, hab, irzuq*) — the positive-supply request.
   Grant-verbs often take double objects: grant us [progeny,
   mercy, firmness…].
3. **Make / render** (*ijʿal, ushdud*) — the transformational
   request. Used when the prayer is for identity-change (*jʿalnā
   muslimayn*, *jʿalnī muqīm al-ṣalāt*).
4. **Shield** (*qinā, ḥāfiẓ*) — the protective-against request.
   Often appears as the "close" of a paradise-petition: *qinā
   ʿadhāb al-nār*.
5. **Accept** (*taqabbal, tub*) — the meta-request: accept the
   very prayer being made. Abraham's Kaʿba prayer (2:127) and his
   Mecca prayer (14:40) both use it.
6. **Do not** (*lā tuzigh, lā tuʾākhidhnā, lā tuḥammil, lā
   takhzinā, lā tadhar*) — the **negative imperative** family.
   These are the most intimate duʿā-acts: they presuppose enough
   covenantal familiarity to ask God *not* to do something.

The negative-imperative family forms a signature of the mature
prayer: Fātiḥa itself does not use it (only affirmative *ihdinā*);
it appears at Q 2:286 (three negatives in one verse), Q 3:8
(*rabbanā lā tuzigh qulūbanā*), Q 71:26 (*lā tadhar*), Q 60:5
(*lā tajʿalnā fitnatan*). The movement from positive-only duʿā
(Fātiḥa) to positive-plus-negative duʿā (Baqarah end, Āl ʿImrān,
Mumtaḥinah) is a **developmental arc** across the scripture — the
community learns to petition against, not only for.

## 10. Q 2:201 — the paradise-prayer

> *rabbanā ātinā fī al-dunyā ḥasanatan wa-fī al-ākhirati ḥasanatan
> wa-qinā ʿadhāba al-nār*
> (Our Lord, give us in this world [that which is] good, and in
> the Hereafter [that which is] good, and protect us from the
> punishment of the Fire.)

The most recited duʿā in the Quran after Fātiḥa itself. Its
structure is **ternary**:
1. Positive petition — this-world good (*fī al-dunyā ḥasanatan*)
2. Positive petition — hereafter good (*fī al-ākhirati ḥasanatan*)
3. Negative-target petition — shield from hellfire (*qinā ʿadhāba
   al-nār*)

The parallelism is exact: *ātinā + fī + X + ḥasanatan* mirrored
twice, closed by a contrasting *qinā*. The prayer includes all
three ontic zones: *dunyā* (this world), *ākhira* (next world),
*nār* (fire). Nothing is outside its scope.

The verse is **framed contrastively** by Q 2:200. Q 2:200 describes
those who only pray for this-world goods (*rabbanā ātinā fī
al-dunyā* — period, full stop); the Quran comments that such people
"have no share in the Hereafter" (*wa-mā lahu fī al-ākhirati min
khalāq*). Q 2:201 then presents the correct form — adding "and in
the Hereafter" and "shield us from Fire". **The two verses are a
before-and-after diptych on how to pray for good.** The Quran
teaches duʿā not abstractly but by showing the wrong form first.

The *ḥasanah* pair also appears at Q 7:156 (Moses' prayer for his
people), Q 16:122 (about Abraham), Q 28:77 (advice to Qārūn),
Q 22:11 (the half-believer). The noun *ḥasanah* anchors a small
cross-surah theme of "the good" as something to be asked for.

## 11. Q 2:285–286 — the end-of-Baqarah prayer

These are the most theologically packed duʿā-verses in the Quran.
Hadith literature (Muslim 808) calls them the two verses "given to
Muhammad from the treasures beneath the Throne" at the night
journey.

**Q 2:285**: frames the prayer. The believers declare: *samiʿnā
wa-aṭaʿnā — ghufrānaka rabbanā wa-ilayka al-maṣīr* (we have heard
and obeyed; Your forgiveness, our Lord, and to You is the
destination). The declarative *samiʿnā wa-aṭaʿnā* is itself a
speech-act of covenant (cf. [covenant-language.md](covenant-language.md)).
The petition is compressed to a single noun: *ghufrānaka* — "Your
forgiveness" as direct object of an implied *naṭlubu* (we seek).

**Q 2:286**: the extended prayer. Structure:
- Preamble: *lā yukallifu llāhu nafsan illā wusʿahā* (Allah does
  not burden a soul beyond its capacity) — God speaks first,
  setting the covenant that the prayer will then lean on.
- Petition cascade (five imperatives, three of them negative):
  1. *rabbanā lā tuʾākhidhnā in nasīnā aw akhṭaʾnā*
  2. *rabbanā wa-lā taḥmil ʿalaynā iṣran kamā ḥamaltahu ʿalā
     alladhīna min qablinā*
  3. *rabbanā wa-lā tuḥammilnā mā lā ṭāqata lanā bihi*
  4. *wa-ʿfu ʿannā wa-ġfir lanā wa-rḥamnā* (three consecutive
     positive verbs: pardon, forgive, have mercy — ascending
     intimacy)
  5. *anta mawlānā fa-nṣurnā ʿalā al-qawm al-kāfirīn* (You are our
     protector, so help us against the disbelieving people)

The verse contains **three *rabbanā* vocatives** (an exceptional
cluster; only 3:193 and 14:37/40 rival it). It **alternates
negative-imperative triples and positive-imperative triples**. It
closes with a **self-describing predicate** (*anta mawlānā*) —
echoing 2:127's *innaka anta al-samīʿ al-ʿalīm*. And it ends with
**a petition to win** (*fa-nṣurnā*) — the only Quranic duʿā that
closes on *naṣr* (victory/help).

The Baqarah ḫātima is thus structurally a **complete duʿā-system**:
praise (285) → affirmation (*samiʿnā wa-aṭaʿnā*) → cascading
petition (286) → self-describing predicate (*anta mawlānā*). It is
Fātiḥa's four moments expanded to surah-closing scale. **If Fātiḥa
is the Quran's opening prayer, Q 2:285–286 is its terminal prayer**
— and placed, not incidentally, at the end of the longest surah,
where the reader has absorbed the full body of covenantal teaching
between the two.

## 12. Synthesis — the Quranic duʿā template

Every Quranic prayer fits a four-slot grammar:

```
  [VOCATIVE]    → rabbanā  / rabbī
  [AFFIRMATION] → innanā āmannā / samiʿnā wa-aṭaʿnā / innaka taʿlam…
  [PETITION]    → imperative stack (positive and/or negative)
  [PREDICATE]   → innaka anta al-X al-Y
```

Not every prayer fills every slot. Short prayers collapse slots
(Fātiḥa v 6 is pure petition; Q 21:87 is pure affirmation:
*lā ilāha illā anta subḥānaka innī kuntu min al-ẓālimīn*). Long
prayers (Q 2:286, 3:191–194, 14:35–41, 20:25–35) fill all four.
The pattern is stable across Meccan and Medinan registers, across
prophet-voice and community-voice, across narrative and liturgy.

Three structural findings:

1. **The pronoun-shift is the prayer's hinge.** Whether within a
   single prayer (Fātiḥa v 5, Abraham's 14:35–41) or across a
   narrative (Noah alone → Noah with followers), the duʿā genre is
   defined by the shift from 3P-about-God to 2P-to-God. The
   iltifāt of Fātiḥa is not a rhetorical trick; it is the
   *definitional* grammatical feature of supplication.
2. **The self-describing predicate names the attribute.** Almost
   every long duʿā closes by naming the divine attribute that the
   petition relies on. The petition "accept from us" closes with
   "the Hearer, the Knower"; the petition "turn to us" closes with
   "the Accepter-of-Repentance"; the petition "help us" closes
   with "our Protector". This is a liturgical version of the
   [razi-99names-test.md](razi-99names-test.md) finding that
   attribute-choice is contextually motivated.
3. **The negative imperative is an advanced form.** Positive-only
   duʿā (Fātiḥa, Q 3:16) is the entry-level form; positive-plus-
   negative duʿā (Q 2:286, 3:8, 71:26) is the mature form. The
   Quran teaches the second form by example, typically in
   surah-closing positions and in the extended-prayer episodes
   of the major prophets.

The duʿā genre in the Quran is thus not a scattered collection of
prayers but a coherent literary system, with recognisable openings,
middles, and closes, with stable pronoun-logic, and with a finite
inventory of imperative acts. Fātiḥa inaugurates the genre; Q 2:286
closes it; ninety-six other rabbanā verses and one hundred fifty-
four rabbī verses fill the space between them.

## Cross-references
- [al-fatiha-deep-dive.md](../phase-c-structures/al-fatiha-deep-dive.md)
  — iltifāt pivot geometry
- [iltifat-catalog.md](iltifat-catalog.md) — the 2P-shift generalised
- [vocative-addresses.md](vocative-addresses.md) — the broader
  vocative system
- [covenant-language.md](covenant-language.md) — *samiʿnā
  wa-aṭaʿnā* as covenant speech-act
- [razi-99names-test.md](razi-99names-test.md) — contextual
  motivation of divine-attribute choice
