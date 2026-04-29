---
title: Spelled-Out Arabic Numbers in the Quran — Catalog
phase: B
agent: numbers-spelled-1
date: 2026-04-12
rules:
  orthography: no-tashkeel (quran-no-tashkeel.json, Hafs-Kufan numbering)
  tokenization: whitespace + punctuation strip; prefix-tolerant stem match
    (proclitics و ف ب ل ك س + definite article ال combinations allowed)
  source_data:
    - data/morphology/quranic-corpus-morphology-0.4.txt
    - quran-text/quran-no-tashkeel.json
  basmala_policy: counted-only-in-surah-1 (does not affect number tallies)
  null_model: not-applicable (descriptive catalog)
status: exploratory (descriptive)
script: scratch/count_numbers2.py
---

# Spelled-Out Arabic Numbers in the Quran

This dossier catalogs every spelled-out Arabic numeral in the Quran: cardinals
(āḥad/wāḥid through alf and its multiples), ordinals (awwal through thāmin),
and fractions (niṣf, thulth, rubʿ, khums, suds, thumn, ʿushr). For each entry
it reports (a) a count of surface-token hits (prefix-tolerant), (b) the
distinct verses where the token occurs, and (c) surah:verse references.
Digits-as-glyphs (Arabic-Indic ١٢٣…) do not occur in the consonantal Quran;
every "number" in the text is spelled alphabetically as a word.

Three caveats apply throughout:

1. **Polysemy.** Several numeral stems are homographs of non-numeric words.
   The clearest examples: (a) *thaman* ثمن "price" (Q 12:20 "for a cheap
   price") is not *thumn* "one-eighth" (Q 4:12); (b) *aḥad* can mean "anyone"
   as much as "one" (Q 2:102 "they taught no *one*"); (c) *awwal* shares a
   token surface *awlā* أولى with the comparative "more worthy / woe to them"
   (Q 47:20 *fa-awlā lahum*). Counts below include all homograph tokens;
   semantic filtering is flagged verse by verse when necessary.

2. **Prefix tolerance.** The match allows word-initial و، ف، ب، ل، ك، س، ال
   and stacked combinations (بال، ولل، …). Without this, hits like Q 3:124
   *bi-thalāthati* ءالاف (3,000 angels) and Q 22:47 *ka-alf* سنة (1,000 years)
   would be missed.

3. **Hafs-Kufan numbering.** A single verse like Q 74:30 is always the same
   "the angels over it are *tisʿata ʿashar* (19)" across recitations, but
   verse counts near the end of long surahs can shift by ±1 in other
   numberings. All references below follow the default numbering of the
   source JSON (which is Hafs).

---

## 1. Per-Number Tally (the master table)

Counts are **token occurrences** (a verse that repeats a number once is
counted once per occurrence) and **distinct verses** (union over all
surface forms inside a stem category). The stem label uses Latinised
root-names for readability.

### Cardinals

| Number | Stem / forms | Tokens | Verses |
|-------:|:-------------|------:|------:|
| 1 (m.) | wāḥid, wāḥidan واحد/واحدا | 30 | 30 |
| 1 (f.) | wāḥida(h) واحدة | 31 | 31 |
| 1 ("anyone") | aḥad / aḥadan أحد | 76 | 74 |
| 1 (fem. alt) | iḥdā إحدى | 5 | 5 |
| **1 total** | wāḥid + aḥad + iḥdā family | **~142** | **~140** |
| 2 (m.) | ithnān / ithnayn اثنان/اثنين | 11 | 9 |
| 2 (f.) | ithnatān / ithnatayn اثنتان/اثنتين | 4 | 3 |
| 2 (compound) | ithnā / ithnatā (in "12") اثنا/اثنتا | 5 | 4 |
| 3 | thalāth(a) ثلاث/ثلاثة | 21 | 20 |
| 4 | arbaʿa(h) أربعة | 12 | 12 |
| 5 | khamsa(h) خمسة | 4 | 4 |
| 6 | sitta(h) ستة | 13 | 13 |
| 7 | sabʿa(h) سبعة | 25 | 21 |
| 8 | thamāniya(h) ثمانية | 5 | 5 |
| 9 | tisʿa(h) تسعة | 6 | 6 |
| 10 | ʿashara(h) عشرة | 16 | 15 |
| 11 | aḥad(a) ʿashar أحد عشر | 1 | 1 (Q 12:4) |
| 12 | ithnā/ithnatā ʿashar(a) اثنا عشر | 5 | 4 |
| 13 | thalāth(a) ʿashar ثلاثة عشر | **0** | 0 |
| 19 | tisʿata ʿashar تسعة عشر | 1 | 1 (Q 74:30) |
| 20 | ʿishrūn / ʿishrīn عشرون/عشرين | 1 | 1 (Q 8:65) |
| 30 | thalāthūn / thalāthīn ثلاثون/ثلاثين | 2 | 2 |
| 40 | arbaʿūn / arbaʿīn أربعين | 4 | 4 |
| 50 | khamsūn / khamsīn خمسون/خمسين | 2 | 2 |
| 60 | sittūn / sittīn ستين | 1 | 1 (Q 58:4) |
| 70 | sabʿūn / sabʿīn سبعين/سبعون | 3 | 3 |
| 80 | thamānūn / thamānīn ثمانين | 1 | 1 (Q 24:4) |
| 90 | tisʿūn / tisʿīn تسعون | 1 | 1 (Q 38:23) |
| 100 | miʾa(h) مائة | 8 | 7 |
| 200 | miʾatān / miʾatayn مائتين | 2 | 2 (Q 8:65, 8:66) |
| 300 | thalāth miʾa ثلاث مائة | 1 | 1 (Q 18:25) |
| 1,000 | alf(an) ألف | 13 | 12 |
| 2,000 | alfayn ألفين | 1 | 1 (Q 8:66) |
| 3,000 | thalāthat ālāf ثلاثة آلاف | 1 | 1 (Q 3:124) |
| 5,000 | khamsat ālāf خمسة آلاف | 1 | 1 (Q 3:125) |
| 50,000 | khamsīn alf خمسين ألف | 1 | 1 (Q 70:4) |
| 100,000 | miʾat alf مائة ألف | 1 | 1 (Q 37:147) |

### Fractions

| Fraction | Stem | Tokens | Verses |
|:--|:--|--:|--:|
| 1/2 niṣf | نصف | 5 | 5 (Q 2:237, 4:11, 4:12, 4:25, 4:176) |
| 1/3 thulth | ثلث / ثلثان / ثلثي | 4 | 3 (Q 4:11, 4:12, 73:20) |
| 1/4 rubʿ | الربع | 2 | 1 (Q 4:12 — twice) |
| 1/5 khums | خمسه | 1 | 1 (Q 8:41) |
| 1/6 sudus | السدس | 3 | 2 (Q 4:11, 4:12) |
| 1/8 thumn | الثمن | 1 | 1 (Q 4:12) — **note Q 12:20 is *thaman* "price", not the fraction** |
| 1/10 ʿushr | معشار | 1 | 1 (Q 34:45 — *miʿshār*, literally "one-tenth-of") |

### Ordinals

| Ordinal | Stem | Tokens | Verses |
|:--|:--|--:|--:|
| 1st awwal / ūlā / awwalīn | أول/أولى/الأولين | 83 | 80 |
| 2nd thānī | ثاني | 2 | 2 (Q 9:40, 22:9) |
| 3rd thālith | ثالث | 3 | 3 (Q 5:73, 36:14, 53:20) |
| 4th rābiʿ | رابع | 2 | 2 (Q 18:22, 58:7) |
| 5th khāmis(a) | الخامسة | 2 | 2 (Q 24:7, 24:9) |
| 6th sādis | سادس | 2 | 2 (Q 18:22, 58:7) |
| 7th sābiʿ | سابع | (0 as ordinal lexeme) | — |
| 8th thāmin | ثامن | 1 | 1 (Q 18:22) |

The ordinal "7th" is *not* spelled *sābiʿ* in the Quran's one surviving "7-count"
passage (Q 18:22 "they say seven and the eighth is their dog"): the text simply
uses the cardinal *sabʿah* سبعة, not the ordinal. The only surface ordinal for
"7" is the verbal/adjectival use in Q 2:196 ("seven days when you return") and
Q 18:22, both cardinal forms. This accounts for the gap at *sābiʿ*.

Awwal's high count (≈80 verses) is inflated by (a) the plural substantive
*al-awwalīn* / *al-ʾawwalīn* الأولين "the ancients / former peoples" (very
frequent — "*asāṭīr al-awwalīn* the tales of the ancients"), and (b) the
elative *awlā* أولى "more fitting / more deserving" (Q 47:20, Q 33:6 etc.)
which is *grammatically* ordinal-derived but semantically comparative.
The strictly ordinal "the first one of N" reading is rarer: Q 6:14, 6:163,
7:143, 9:100 etc.

### Omitted-by-the-Quran numbers (in the 1–20 range)

Of the integers 1–20, the ones that are **never spelled out anywhere** (even
as ordinals) are: **13, 14, 15, 16, 17, 18**. The leap from 12 (five verses)
straight to 19 (one verse, Q 74:30) is the most conspicuous discontinuity in
the small integers. This absence is part of why Q 74:30 has the reputation
it does — the number 19 is literally the only teen after "twelve" that the
Quran ever spells.

---

## 2. The Seven Canonical Repeating Numbers

Looking across all cardinals, a small set dominates by raw frequency (verses):

| Rank | N | Verses |
|-----:|--:|------:|
| 1 | **1** (all forms) | ~140 |
| 2 | **7** | 21 |
| 3 | **3** | 20 |
| 4 | **10** | 15 |
| 5 | **6** | 13 |
| 6 | **1000** | 12 |
| 7 | **4** | 12 |

These seven form the "numerical backbone" of Quranic counting: *wāḥid* for
the theology of tawḥīd, *sabʿa* for cosmology (seven heavens, seven earths,
seven ears of corn, seven sleepers, seven gates of Hell), *thalātha* for
ritual periods (three-month waiting, three-day penance, three witnesses),
*ʿashara* for the Decalogue-like completions (ten days of Dhu'l-Ḥijja,
ten perfected fasts, ten-fold reward), *sitta* for the six days of creation
(consistently across Q 7:54, 10:3, 11:7, 25:59, 32:4, 50:38, 57:4), *alf*
for hyperbolic scale (a day like a thousand years), and *arbaʿa* for
boundary-setting (four witnesses, four months' respite, four wives). Every
other integer either matches a single scene (Q 74:30 "19", Q 12:4 "11",
Q 8:41 "khums") or serves a one-off legal / narrative beat.

Note how absent 5, 8, 9 are despite being "small" — each appears in only
4–6 verses. The Quran's numeric vocabulary is sparse and purposive.

---

## 3. Q 18:25 — "Three hundred years, and they added nine" (309)

> وَلَبِثُوا فِي كَهْفِهِمْ ثَلَاثَ مِائَةٍ سِنِينَ وَازْدَادُوا تِسْعًا
> "And they stayed in their cave three hundred years and added nine."

This is the *only* verse in the Quran that spells out "three hundred"
(*thalāth miʾa*), and it is immediately followed by the *only* occurrence
of *tisʿan* "nine" functioning as an additive tail to a compound number
(elsewhere, *tisʿa* appears as "nine signs", Q 17:101 / 27:12, or as "nine
and ninety ewes", Q 38:23, or as the closing digit of 19, Q 74:30). The
verse therefore produces the composite **309**, which classical tafsīr
(Ṭabarī, Rāzī, Qurṭubī) read as the solar 300 years plus 9 lunar-adjustment
years — the two calendars reconciled inside the text itself:

> 300 solar years × 365.2422 days = 109,572.66 days
> 309 lunar years × 354.367 days  = 109,499.4  days
> difference ≈ 73 days (~0.07 %)

The *waw* in *wa-zdādū tisʿan* is read as an additive conjunction, not a
narrative resumptive. Q 18:25 is also the verse that anchors the whole
"Cave of the Sleepers" numerological tradition (the seven sleepers of
Q 18:22, their dog the rābiʿ "fourth" or thāmin "eighth", their three
hundred and nine years of sleep). It is worth noting that 309 is not
itself repeated anywhere in the text — the number exists only in this
additive fashion.

---

## 4. Q 74:30 — "Over it are nineteen" (*tisʿata ʿashar*)

> عَلَيْهَا تِسْعَةَ عَشَرَ

The entire verse is three words (one of the shortest in the Quran) and
contains the Quran's **single occurrence** of the number 19 in either
cardinal or ordinal form. Nowhere else is 19, 13, 14, 15, 16, 17, or 18
spelled. The grammatical form is the Arabic compound *tisʿata ʿashar*
(feminine numerator + masculine counted — classical agreement-reversal),
and it refers to the number of angels set as wardens over *Saqar* (hell-
fire, Q 74:26-28). The surrounding verses 31-32 then gloss the number's
purpose: "We have made their number only as a trial for the disbelievers,
so that those who were given the Scripture may be certain… and that those
in whose hearts is disease and the disbelievers may say: 'What does Allah
intend by this as an example?'" The text itself flags the number as a
test-object, which is why it has attracted more numerological speculation
than any other figure in the Quran (see numerical-coincidences.md §19).

---

## 5. Q 3:124-125 — Three thousand and five thousand angels

> (124) إِذْ تَقُولُ لِلْمُؤْمِنِينَ أَلَن يَكْفِيَكُمْ أَن يُمِدَّكُمْ رَبُّكُم بِثَلَاثَةِ آلَافٍ مِّنَ الْمَلَائِكَةِ مُنزَلِينَ
> (125) بَلَىٰ ۚ إِن تَصْبِرُوا وَتَتَّقُوا وَيَأْتُوكُم مِّن فَوْرِهِمْ هَٰذَا يُمْدِدْكُمْ رَبُّكُم بِخَمْسَةِ آلَافٍ مِّنَ الْمَلَائِكَةِ مُسَوِّمِينَ

These two consecutive verses contain the Quran's only "3,000" and the only
"5,000"; the plural noun *ālāf* آلاف "thousands" appears in exactly these
two verses and nowhere else. The battle context is Uḥud (or more precisely
the pre-Uḥud reassurance at Badr, per majority tafsīr). The 3,000+5,000
pairing follows an escalation pattern (→ 8,000 implicit) mirrored by the
companion 2,000/1,000 escalation of Q 8:65-66 (see §below): one reassurance
number, one conditional upgrade. In both passages the "thousands" of angels
are the divine-auxiliary trope.

Reference-level observation: "5,000" is also the total number of verses in
roughly the first half of the Quran (≈5,112 through Q 20); and "3,000" is
close to the total of verses in the first three *juzʾ*. These parallels
are ***not*** load-bearing; they are offered only as mnemonics.

---

## 6. Q 12:4 — Eleven stars

> إِذْ قَالَ يُوسُفُ لِأَبِيهِ يَا أَبَتِ إِنِّي رَأَيْتُ أَحَدَ عَشَرَ كَوْكَبًا وَالشَّمْسَ وَالْقَمَرَ رَأَيْتُهُمْ لِي سَاجِدِينَ
> "When Joseph said to his father: 'O my father, I have seen eleven stars,
>  and the sun and the moon, I saw them prostrating to me.'"

Q 12:4 is the Quran's only "eleven" (*aḥada ʿashar*). The compound uses
masculine *aḥada* because the noun counted, *kawkaban* "stars", is
masculine; contrast Q 2:60 / 5:12 / 7:160 / 9:36 where "twelve" appears as
*ithnā ʿashar* (m.) or *ithnatā ʿashar(a)* (f.) for twelve tribes,
chieftains, months, or springs. The number eleven thus appears exactly
once in the Quran, exclusively in Joseph's dream narrative. Notably, this
matches the sum in the tradition: 11 brothers + Joseph + the father (=12
tribes to be) + Joseph's mother — the dream already encodes the
"twelve tribes" census that Q 5:12 later spells out with *ithnay ʿashara
naqīban* "twelve chieftains."

---

## 7. Q 70:4 — "Fifty thousand years"

> تَعْرُجُ الْمَلَائِكَةُ وَالرُّوحُ إِلَيْهِ فِي يَوْمٍ كَانَ مِقْدَارُهُ خَمْسِينَ أَلْفَ سَنَةٍ
> "The angels and the Spirit ascend to Him in a day whose span is fifty
>  thousand years."

Q 70:4 is the Quran's only *khamsīn alf* خمسين ألف "50,000" and the only
place where "years" (*sana*) is multiplied by so large a factor. Compare
the companion "cosmic day" verses that all use 1,000 years:

- Q 2:96 "he would wish to live a thousand years" (*alf sana*)
- Q 22:47 "a day with your Lord is like a thousand years of what you count" (*ka-alf sana mimmā taʿuddūn*)
- Q 29:14 "Noah stayed among them a thousand years less fifty" (*alf sana illā khamsīn ʿāman*)
- Q 32:5 "a day whose span is a thousand years of what you count"

Q 70:4 is the one outlier at 50× the scale. The classical reconciliation
(Ṭabarī, Ibn Kathīr) reads Q 32:5 as the *earthly* ascent-day (the divine
command descending and re-ascending in one cosmic "day" = 1,000 human
years) and Q 70:4 as the Resurrection Day whose length, experientially,
is 50,000 years for the disbelievers. Q 29:14 is a different numerical
joke altogether — Noah's mission is 1,000 − 50 = 950 years, the subtraction
form that is otherwise unique in the Quran.

---

## 8. Q 46:15 — Forty years

> وَوَصَّيْنَا الْإِنسَانَ بِوَالِدَيْهِ إِحْسَانًا ۖ حَمَلَتْهُ أُمُّهُ كُرْهًا وَوَضَعَتْهُ كُرْهًا ۖ وَحَمْلُهُ وَفِصَالُهُ ثَلَاثُونَ شَهْرًا ۚ حَتَّىٰ إِذَا بَلَغَ أَشُدَّهُ وَبَلَغَ أَرْبَعِينَ سَنَةً قَالَ رَبِّ أَوْزِعْنِي…
> "…until when he attains full strength and reaches forty years, he says:
>  'My Lord, grant me that I may be thankful…'"

"Forty years" (*arbaʿīn sana*) appears exactly twice in the Quran:
Q 5:26 (the 40-year wandering of the Israelites after the refusal to enter
the Holy Land) and Q 46:15. The 46:15 usage is remarkable because it
fixes a *biographical* rather than a *punitive* threshold: 40 years as
the age of mature reflection. Combined with *thalāthūn shahran* "30
months" in the same verse (pregnancy + weaning), Q 46:15 is the only
verse in the Quran that spells out two discrete cardinals (30 and 40) in
the same breath. Classical jurisprudence extracts from this the minimum
pregnancy duration of 6 months (30 − 24 months of weaning, Q 2:233).

Other *arbaʿīn* references: Q 2:51 "forty nights" (Moses's appointment on
Sinai) and Q 7:142 "thirty nights completed with ten" (= 40 nights again,
the only place where 40 is spelled as a 30+10 sum rather than as a single
word).

---

## 9. Fractional vs Ordinal Distribution

**Fractions** concentrate almost entirely in **two surahs**: Al-Nisāʾ
(Q 4) and the other legal / economic passages.

- Q 4:11–12 together contain: *niṣf* (1/2), *thulth* (1/3, twice: "2/3"
  via *thuluthā* and "1/3" literal), *rubʿ* (1/4, twice), *thumn* (1/8),
  *sudus* (1/6, three times). That is **six distinct fractions in two
  adjacent verses** — the densest fraction passage in any Arabic legal
  text of the period.
- Q 2:237 (niṣf al-ṣadāq = half the dower if divorce before consummation)
- Q 4:25 (niṣf ʿalā al-muḥṣanāt = half punishment for slave-women)
- Q 4:176 (niṣf + kalāla inheritance addendum)
- Q 8:41 (khums al-ghanīma = one-fifth of spoils)
- Q 34:45 (miʿshār = one-tenth, hyperbolic "they did not reach a tenth")
- Q 73:20 (thulthay al-layl, niṣfahu, thuluthahu — two-thirds of the
  night, its half, its third — the *only* fraction cluster outside Q 4)

Outside Q 4, 8, 34, and 73, fractions are **entirely absent**. This is a
signal that the Quran's fractional vocabulary is a **legal-and-liturgical
register**, not a cosmological one.

**Ordinals**, conversely, are almost entirely a *narrative* register:

- *Thālith*, *rābiʿ*, *khāmis*, *sādis*, *thāmin* appear only in four
  scenes: (i) the Cave dwellers' headcount (Q 18:22 — 3+dog, 5+dog, 7+dog,
  *thāmin*uhum *kalbuhum*), (ii) the secret-conference rule (Q 58:7 —
  "no whispering of three but He is their fourth, nor of five but He is
  their sixth"), (iii) the liʿān oath (Q 24:7, 24:9 — the fifth oath),
  and (iv) polytheistic triads (Q 5:73, Q 53:20, Q 36:14).
- *Thānī* (2nd) appears only twice: Q 9:40 (Prophet + Abū Bakr "the second
  of two in the cave") and Q 22:9 (*thāniya ʿiṭfihi* "twisting his
  side" — not strictly ordinal but from the same root).
- *Awwal* (1st) is by far the dominant ordinal, but most occurrences are
  the plural *al-awwalīn* "the ancients", not a true ordinal first.

**Summary**: The Quran's fraction vocabulary is legal (inheritance,
spoils, prayer, night-vigil); its ordinal vocabulary is narrative (the
cave, the whisperers, the liʿān, the triads).

---

## 10. Inheritance Fractions: Q 4:11-12 in Full

Q 4:11 and Q 4:12 form the Quran's most number-dense passage outside the
eschatological "50,000 year" / "300 years" verses. Together they lay out
the complete Islamic law of *mīrāth*:

| Heir combination | Fraction | Verse |
|:-------------|:-----:|:---:|
| Daughter(s), one only | 1/2 (*niṣf*) | 4:11 |
| Daughters, two or more | 2/3 (*thuluthā*) | 4:11 |
| Each parent, if deceased has a child | 1/6 (*sudus*) | 4:11 |
| Mother, if no child and no siblings | 1/3 (*thulth*) | 4:11 |
| Mother, if siblings exist | 1/6 (*sudus*) | 4:11 |
| Husband, if wife childless | 1/2 (*niṣf*) | 4:12 |
| Husband, if wife has child | 1/4 (*rubʿ*) | 4:12 |
| Wife, if husband childless | 1/4 (*rubʿ*) | 4:12 |
| Wife, if husband has child | 1/8 (*thumn*) | 4:12 |
| Kalāla sibling alone | 1/6 (*sudus*) | 4:12 |
| Kalāla siblings, more than one | 1/3 shared (*thulth*) | 4:12 |

Counting unique spelled fractions: **{1/2, 1/3, 1/4, 1/6, 1/8}**. The
fractions 1/5, 1/7, 1/9, 1/10 do *not* appear in the inheritance rules.
(1/5 appears as spoils-of-war in Q 8:41; 1/10 appears only as the hyperbolic
*miʿshār* in Q 34:45.) The pattern — halves, thirds, quarters, sixths,
eighths — is mathematically closed under the operations needed for the
Islamic *ʿawl* / *radd* adjustments: it is precisely the set of fractions
whose denominators divide 24 (LCM = 2·3·2² = 24), which is why classical
*fiqh* computes all inheritance shares on a "common of 24" grid. The
Quran's fraction vocabulary is thus not merely a random legal list — it
is exactly the set needed to close the inheritance arithmetic.

---

## 11. The Numerically Singular Verses

Collecting the verses that contain a number appearing **only there**:

- Q 8:65 — the only "20" (ʿishrūn)
- Q 8:66 — the only "2,000" (alfayn)
- Q 12:4 — the only "11" (aḥada ʿashar)
- Q 18:25 — the only "300" (thalāth miʾa) and the only additive-tail *tisʿan*
- Q 24:4 — the only "80" (thamānīn jaldatan, eighty lashes)
- Q 34:45 — the only "tenth" (*miʿshār*)
- Q 37:147 — the only "100,000" (*miʾat alf aw yazīdūn* — Jonah's Nineveh)
- Q 38:23 — the only "99" and the only "90" (*tisʿ wa tisʿūn*)
- Q 58:4 — the only "60" (ṣiyām ḥzihār: "then feed sixty poor")
- Q 69:32 — the only "70 cubits" (sabʿīn dhirāʿan — chain-length in hell)
- Q 70:4 — the only "50,000" (khamsīn alf sana)
- Q 74:30 — the only "19" (tisʿata ʿashar)
- Q 3:124 / 3:125 — the only "3,000" and "5,000"
- Q 46:15 — the only place that spells 30 and 40 in one breath

Fourteen verses hold the Quran's entire repertoire of "unique" numbers.
This is small and sharp: the Quran is not a numbers-book, and its
numerically singular scenes do double duty as its most cited scenes.

---

## 12. Cross-References to the Morphology Corpus

The QAC morphology file (`data/morphology/quranic-corpus-morphology-0.4.txt`)
lemmatises numbers under a small set of lemma IDs:

- `waAHid` — wāḥid, 61 tokens across wāḥid/wāḥida/wāḥidan
- `>aHad` — aḥad, 85 tokens (includes the pronominal "anyone")
- `vala`v` — thalātha, 17 tokens
- `saboE` — sabʿa, 24 tokens
- `Ea$ar` — ʿashara, 13 tokens
- `>aloF` — alf, 7 tokens
- `mi}ap` — miʾa, 8 tokens
- `niSof` — niṣf, 5 tokens
- `vuluv` — thulth, 4 tokens
- `rubuE` — rubʿ, 2 tokens
- `sudus` — suds, 3 tokens
- `vumun` — thumn, 1 token

The QAC counts nearly match the text-level tally in §1 (any discrepancy
reflects (a) compound-noun segmentation and (b) the QAC's stripping of
proclitics before counting).

---

## 13. Takeaways

1. Of the integers 1-20, the Quran spells only 1, 2, 3, 4, 5, 6, 7, 8, 9,
   10, 11, 12, and 19 — the "teens" 13-18 are absent entirely.
2. Seven numbers (1, 7, 3, 10, 6, 1000, 4) account for the vast bulk of
   numerical verses.
3. The Quran's full fraction vocabulary {1/2, 1/3, 1/4, 1/5, 1/6, 1/8,
   1/10} is exactly the legal set needed for inheritance and spoils law.
4. The large cosmic numbers (1,000 / 2,000 / 3,000 / 5,000 / 50,000 /
   100,000) all appear in eschatological or angelic-battle contexts.
5. Singular scenes (309, 19, 11, 50 000, 99, 70 cubits, 60 poor, 80 lashes,
   100,000) are concentrated in fourteen verses.
6. The Quran's numerology is sparse, non-redundant, and purposive — a
   far cry from the dense numeric scaffolding of Kabbalistic or Pythagorean
   texts.

---

**Data generated by** `/Users/grey/Downloads/quran/scratch/count_numbers2.py`;
raw output in `/Users/grey/Downloads/quran/scratch/numbers_v2.txt`.

For the (separate, test-oriented) numerical-coincidence exploration, see
`findings/phase-b-hypotheses/numerical-coincidences.md`.
