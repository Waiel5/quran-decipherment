# Angels in the Quran — a complete catalog

**Agent:** Phase B — angels-run-1
**Date:** 2026-04-12
**Method:** Full enumeration of lemma `malak` (ROOT `mlk`, angel-sense) in the Leeds Quranic Arabic Corpus v0.4, cross-checked against `quran-no-tashkeel.json`. Named-angel proper nouns counted by their own lemmas. Angel-descriptions (oath-taking ranks, death-takers, throne-bearers, hell-keepers, etc.) traced through the verses where they occur even when the word *malak* is absent.

---

## 1. Headline counts

| Item | Count | Notes |
|---|---|---|
| Lemma `malak` (angel) — all morphological forms combined | **88** | 73 plural, 2 dual (2:102), 13 singular |
| Distinct verses containing lemma `malak` | **86** | Two verses hold two tokens each: 6:8 and 17:95 |
| Distinct surahs containing lemma `malak` | 37 of 114 |  |
| Lemma `shayṭān` / `shayāṭīn` (Satan / devils) | **88** | 70 singular, 18 plural |
| Distinct verses with `shayṭān` | 78 |  |
| Distinct surahs with `shayṭān` | 36 |  |

**Unexpected finding:** the lemma for angel and the lemma for Satan occur the *same* number of times (88) across the whole Quran. Because Quranic vocabulary has heavy-tailed frequency, a chance match at precisely 88 is not statistically impossible (many lemmas in this frequency band), but it is striking that the two principal supernatural counter-agents of the book land on the identical integer. (Note: Iblīs is a separate lemma from root `bls`; counted separately he adds 11 occurrences, breaking the tie — so the parity is strictly *malak* vs *shayṭān*, with Iblīs on a third axis.)

Full token-form breakdown for `mlk` root (both angel and king/kingdom senses, for methodological transparency):

| Lemma | Count | Meaning |
|---|---|---|
| `malak` | 88 | angel (this catalog) |
| `mulk` (`mulok`) | 48 | kingdom, dominion (divine-attribute, not angelic) |
| `malakūt` | 4 | greater dominion |
| `malik` (sing.) | 15 | king (human or divine) |
| `mālik` (`mā`lik`) | 3 | owner / sovereign (2 are divine, 1 in 1:4 "Master of the Day of Judgement") |
| `mā`lik2` | 1 | **MĀLIK, hell-warden (Q 43:77) — disambiguated lemma in QAC** |
| `mamlūk` | 1 | owned-slave (16:75) |
| `malīk` | 1 | King (54:55) |
| **Total `mlk` root** | **206** | |

---

## 2. Named angels — verified verse by verse

### 2.1 Jibrīl / Gabriel — exactly 3 occurrences

| Verse | Form | Context |
|---|---|---|
| Q 2:97 | `jibrīla` (GEN) | "whoever is an enemy of Gabriel — he brought it down on your heart" |
| Q 2:98 | `jibrīla` (GEN) | Paired with Mīkāl in a single verse: "Allāh, His angels, His messengers, Gabriel, Michael" |
| Q 66:4 | `jibrīlu` (NOM) | "Allāh is his protector, and Gabriel and the righteous of the believers" |

Three tokens is the whole lexical footprint. The Spirit (al-Rūḥ, see §3) is widely interpreted as Gabriel under another name, especially at Q 19:17 ("We sent to her Our Spirit who assumed a well-proportioned human form"), Q 26:193 ("Rūḥ al-Amīn brought it down on your heart" — echoing 2:97), and Q 16:102 ("Rūḥ al-Qudus brought it down from your Lord"). Even so, at the level of proper nouns the name *Jibrīl* appears only 3×.

### 2.2 Mīkāʾīl / Michael — exactly 1 occurrence

- Q 2:98, form `mīkāla` — hapax. QAC lemma `mīkāl`. The single Michael-naming in the Quran.

The Quran therefore has asymmetric archangel naming: Gabriel 3×, Michael 1×. Contrast Luke 1 (NT), which also names only two archangels — same asymmetry (Gabriel speaking, Michael named only in Jude and Revelation). The Qumran material names Michael more heavily; the Quran aligns with the New Testament pattern.

### 2.3 Mālik — hell-warden, exactly 1 occurrence

- Q 43:77, `mālikū` (NOM, vocative). "They will call out: 'O Mālik, let your Lord put an end to us!'" QAC tags this as PN with a *disambiguated* lemma `mā`lik2` — the morphology annotators specifically distinguished it from the ordinary word for "owner/master" (`mā`lik` at 1:4 etc.). The text itself does not explicitly call Mālik an angel; the identification rests on context (he governs the fire of Jahannam) and on 74:31 which gives "over it are nineteen ... We have made the keepers of the Fire only angels."

### 2.4 Hārūt and Mārūt — one occurrence each

- Q 2:102, `hārūta wa-mārūta`. QAC tags both as PN (proper name) rather than as appositives of *malakayn*. Semantic crux: the preceding word is `al-malakayn` — dual of *malak*, "the two angels." Read naturally this makes Hārūt and Mārūt angels at Babylon. A well-known *qirāʾa* attributed to Ibn ʿAbbās reads `al-malikayn` (the two *kings*) instead, and under that reading they are sorcerer-kings, not angels. The canonical Ḥafṣ ʿan ʿĀṣim reading (the text in our corpus) has them as angels; the ambiguity is real and classical.

Under the canonical reading, Hārūt and Mārūt are the only angels in the Quran described as being sent specifically to *test* ("innamā naḥnu fitnatun — we are but a trial, so do not disbelieve") and whose teaching is nevertheless said to enable harm (splitting husband and wife). They are the only named angels whose moral status reads as ambiguous in the text. Classical tafsīr of this verse is extensive; here I only log the lexical data. Their parallel-naming with internal rhyme (Hārūt/Mārūt) mirrors other Quranic pairings (Yajūj/Majūj, Qabīl/Habīl in tradition) — an onomastic marker of doubles.

### 2.5 The Spirit (al-Rūḥ) — 21 occurrences, identity contested

The root `rwH` produces the lemma `rūḥ` 21 times (+ `rīḥ` wind, 29 — separate meaning). Of the 21:

- 4× as **Rūḥ al-Qudus** (the Holy Spirit): Q 2:87, 2:253, 5:110, 16:102 — three of which specifically back the mission of ʿĪsā ibn Maryam.
- 1× **Rūḥ al-Amīn** (the Trustworthy Spirit): Q 26:193 — "the Trustworthy Spirit brought it down on your heart" — verbal echo of Q 2:97's description of Jibrīl as "he brought it down on your heart." This is the strongest internal cross-reference licensing the classical identification Rūḥ = Jibrīl.
- 1× in human-shape: Q 19:17 — "We sent to her Our Spirit; he took for her the form of a well-proportioned man."
- 1× paired-and-separated with angels: Q 78:38 — "the Day the Spirit and the angels will stand in rows." The Spirit is listed *alongside* angels, not *as* an angel — an argument against the simple identification.
- 1× again paired-and-separated: Q 70:4 — "the angels and the Spirit ascend to Him."
- 1× **Laylat al-Qadr**: Q 97:4 — "the angels and the Spirit descend therein."
- Several times as a "command from My Lord" (e.g. 17:85), as God's own breath breathed into Adam (15:29, 38:72, 32:9, 21:91, 66:12), as a strengthening into believers (58:22), as revelation itself (40:15, 42:52), as the angel who appears to Maryam (19:17, 16:2).

**Adjudication.** The Quran does not explicitly equate al-Rūḥ with Jibrīl. When listing ranks (70:4, 78:38, 97:4) it always pairs the Spirit *with* the angels, implying distinctness; when describing revelation (26:193 vs 2:97) the verbal formulae are identical, implying identity. The text preserves both possibilities. Classical tafsīr overwhelmingly equates them; rationalist moderns often argue for a distinct cosmic rank. For this catalog, I log the Spirit as an ambiguous 6th named figure: either the highest angel or a non-angelic cosmic agent adjacent to the angels.

---

## 3. Unnamed angel groups — inventory

### 3.1 Throne-bearers (ḥamalat al-ʿarsh)

- Q 40:7: "those who bear the Throne and those around it glorify with praise of their Lord" — no number given; present-tense activity.
- Q 69:17: "the angels shall be on its sides, and eight bear the Throne of your Lord above them on that Day" — the number **eight** (`thamāniyah`), and crucially *on that Day* (yawmaʾidhin), not now.

**Classical seven vs Quranic eight.** The "seven throne-bearers" doctrine familiar from 1 Enoch and some hadith material has *no Quranic warrant*. The Quran is silent on the current number and specifies **eight** only *on the Day of Judgment*. The clean reading is:

- Present: some number of angels carry/surround the Throne; the Quran does not say how many.
- Eschaton: specifically eight.

Some classical scholars (e.g. Ibn Kathīr) harmonize by saying the number grows from 4 (or 7) to 8 on that Day. This is tafsīr-side reasoning, not textual.

### 3.2 The 19 over Hellfire (Q 74:30-31)

- "Over it are nineteen" (ʿalayhā tisʿata ʿashar). Then v31: "We have not made the keepers of the Fire (aṣḥāb al-nār) except angels, and We have not made their number except as a trial..."
- This is the Quranic foundation for the "Code 19" numerological tradition (Rashad Khalifa) and, more conservatively, for all classical attempts to read 19 as structurally loaded. For the angel-catalog it simply locks: 19 angels guard hell.

### 3.3 Recording angels — `kirām kātibīn` (Q 82:10-12)

- v10: `ḥāfiẓīn` — guardians.
- v11: `kirāmān kātibīn` — noble scribes.
- v12: "they know what you do."
- This is the unique Quranic locus for the scribe-angels of deeds. Note neither *Raqīb* nor *ʿAtīd* (the names classical tradition gives to the right-shoulder and left-shoulder scribes) appears; those names are hadith-derived, not Quranic. The Quran has Q 50:17-18 (the "two seated ones" receiving speech) and 50:21 (every soul arrives with a driver and a witness, sā'iq and shahīd) — plural, anonymous.

### 3.4 Death-angel(s)

Singular: Q 32:11 — `malak al-mawt alladhī wukkila bikum` ("the angel of death who has been entrusted with you"). Singular, definite, never named. The name *ʿIzrāʾīl* is hadith/folklore, not Quranic.

Plural: Q 6:61 (*rusulunā yatawaffawnahu*, "Our messengers take his soul"), Q 4:97 (the angels take those who wronged themselves), Q 16:28 and 16:32 (the two faces of death-taking — see §4), Q 8:50 and 47:27 (angels "strike their faces and their backs" of the disbelievers at death).

The text therefore gives both a singular *malak al-mawt* (32:11) and a plurality of angel-agents. Classical harmonization: one chief with many subordinates. The Quran itself is consistent with either reading.

### 3.5 Badr (Q 8:9-12) and Uhud (Q 3:124-125)

- Badr — Q 8:9: "I will reinforce you with a thousand (alf) of the angels in succession (murdifīn)."
- Badr — Q 8:12: "When your Lord revealed to the angels: 'I am with you, so make firm those who believe...'"
- Uhud (or pre-Uhud exhortation) — Q 3:124: "Is it not enough for you that your Lord should reinforce you with three thousand (thalāthat ālāf) of the angels sent down?"
- Q 3:125: "Yes — if you are steadfast and mindful of God, and they come upon you suddenly, your Lord will reinforce you with five thousand (khamsat ālāf) of the angels *musawwimīn*" — the last word classically glossed "bearing distinguishing marks" or "swift-sweeping."

**Did the Quran claim angels fought on the Muslim side at Badr?** Yes — 8:12 is explicit: "I will cast terror into the hearts of those who disbelieve; *so strike above the necks and strike from them every fingertip.*" The imperatives are addressed *to the angels* (v12 opens "idh yūḥī rabbuka ilā l-malāʾikati"). This is the single Quranic passage where angels receive a direct combat order. 8:9 frames them as reinforcement (*mumiddukum*); 8:12 shifts to direct order. So the Quranic claim is stronger than mere presence or morale-support: at Badr, angels are addressed as combatants.

Uhud is different. Q 3:124-125 is in the past-tense subjunctive ("Is it not enough...?") and conditioned on Muslim steadfastness. Classical sīra identifies 3:124 as a recollection of Badr mentioned *during* the Uhud aftermath, not a claim that angels fought at Uhud. The numbers (1,000 → 3,000 → 5,000) read as a rhetorical escalation offered as reassurance, with the 5,000 conditional on steadfastness.

Number-progression detail: the root `>lf` (thousand) appears with angels exactly in these three places (8:9, 3:124, 3:125) and nowhere else in association with angels. The progression 1,000→3,000→5,000 is itself a mini-structure (step of 2,000 between each).

### 3.6 Oath-ranks — the opening-verse angel bands

- Q 37:1-3: `al-ṣāffāt ṣaffā / fa-l-zājirāt zajrā / fa-l-tāliyāt dhikrā` ("by those who arrange in ranks, and those who drive, and those who recite the reminder"). Feminine-plural participles; classical consensus these are angels.
- Q 77:1-5: `al-mursalāt ʿurfā / fa-l-ʿāṣifāt ʿaṣfā / wa-l-nāshirāt nashrā / fa-l-fāriqāt farqā / fa-l-mulqiyāt dhikrā` — five ranks.
- Q 79:1-5: `al-nāziʿāt gharqā / wa-l-nāshiṭāt nashṭā / wa-l-sābiḥāt sabḥā / fa-l-sābiqāt sabqā / fa-l-mudabbirāt amrā` — five ranks.

These three surahs open with angel-oath clusters totaling 3 + 5 + 5 = **13 participial descriptions of angelic activity**. Classical tafsīr takes all 13 as angelic duties (not wind, as some moderns argue for 77 and 79). Note that none of these passages uses the lemma *malak* — the identification is purely from context and tafsīr tradition. They are counted in the catalog as angelic only in that secondary sense.

### 3.7 The Zabāniyah (Q 96:18)

- `sa-nadʿu al-zabāniyah` — "We shall call the Zabāniyah." The word is a hapax. Classical gloss: the muscular chief-executor angels of hell, possibly a loanword. Companion to the 19-keepers (74:30) and to Mālik (43:77) in forming the Quran's hell-angel triad.

### 3.8 Guardian-angels in life

- Q 13:11: `lahu muʿaqqibātun min bayni yadayhi wa-min khalfihi yaḥfaẓūnahu min amr Allāh` ("he has trailing guardians before him and behind him who guard him by command of God"). The lemma `muʿaqqibāt` is *feminine* plural, a hapax. Classical tafsīr: night-and-day shift-angels. Different vocabulary from 82:11's `kātibīn`.
- Q 6:61: "He is the subjugator over His servants, and He sends over you *ḥafaẓah* (guardians) until, when death comes..." — another lemma again (`ḥafaẓah`).

So the Quran uses *three different nouns* for watching angels: `muʿaqqibāt` (13:11), `ḥafaẓah` (6:61), `ḥāfiẓīn kirām kātibīn` (82:10-11). Classical tradition harmonizes; the text uses varied vocabulary.

### 3.9 Angels at the birth-annunciations

- Q 3:42-45: angels address Maryam ("yā Maryam, Allāh has chosen you…" and "yā Maryam, Allāh gives you glad tidings of a Word from Him"). Plural.
- Q 19:17: "We sent to her Our Spirit" — singular, and the Spirit, not *malak*.
- Q 11:69-73, 15:51-56, 51:24-30: "Our messengers" (*rusulunā*) visit Ibrāhīm — classical identification as angels is standard. Lot narrative continues at 15:57-77, 11:77-83.
- Q 3:39, Q 19:7 (Zakariyā): angel-announcement of Yaḥyā.

### 3.10 Angels at the Fall / the Prostration

- Q 2:30-34, Q 7:11, Q 15:28-31, Q 17:61, Q 18:50, Q 20:116, Q 38:71-74 — all seven tellings of "prostrate to Adam." Angels are collective, anonymous. Iblīs's refusal is the structural foil (and classically the question: was he an angel who fell, or a jinn all along? Q 18:50 answers explicitly: `kāna mina l-jinn`).

---

## 4. The "peaceful-faced" vs "harsh-faced" opposition

The Quran builds a two-panel angelology using a single structural trick: *the same death-event, viewed from two angles*.

### Peaceful-faced / ṭayyibīn

- Q 16:32 — "those whom the angels take in death *while they are pure* (ṭayyibīn), saying `salāmun ʿalaykum` — enter Paradise for what you used to do."
- Q 13:23-24 — angels enter upon the righteous "from every gate, saying `salāmun ʿalaykum` for what you bore with patience."
- Q 41:30-31 — "Those who say 'Our Lord is Allāh' and then stand firm — the angels descend upon them: 'Do not fear and do not grieve... we are your allies in the worldly life and the Hereafter.'"

### Harsh-faced / ghilāẓ shidād

- Q 8:50 — "If you could see when the angels take the souls of the disbelievers — *striking their faces and their backs* — and 'taste the burning punishment.'"
- Q 47:27 — "How then, when the angels take them in death, *striking their faces and their backs*?" (near-verbatim repetition of 8:50)
- Q 16:28 — "Those whom the angels take in death *wronging themselves* — they will offer submission: 'we were not doing wrong.' ... Enter the gates of Hell."
- Q 66:6 — over the Fire are "angels stern, severe (`ghilāẓun shidād`), who do not disobey Allāh in what He commands them, and do what they are ordered."
- Q 74:30-31 — 19 keepers of hell, angels.
- Q 96:18 — Zabāniyah.

**The structural claim.** Q 16:28 and Q 16:32 are *back-to-back in the same surah*, four verses apart, describing the same event (the angel-reception of the soul at death) in opposite registers. This is the densest face-and-back pairing in the Quran:

- 16:28 — wrongers of themselves → salam-submission of fear → hell.
- 16:32 — pure-ones → salām-greeting of welcome → paradise.

The word `salām` appears in both — with opposite valence: forced peace-submission in 16:28, greeting-of-peace in 16:32. This is *formal* iltifāt: the same lexical element inverted by context.

Nearly identical pairing at book-scale: 8:50 vs 13:23-24 (facing-striking vs gate-greeting). And 66:6 (harsh hell-keepers) sits in the same surah as 66:4 (Jibrīl as ally of the Prophet), juxtaposing harsh-protective and harsh-punitive angels in a single surah.

---

## 5. The malāʾika vs shayāṭīn opposition, mapped

### Frequencies

- `malak` lemma: 88 tokens.
- `shayṭān` lemma: 88 tokens.
- Parity at 88 is exact.

### Surah-level distribution

- Both appear in 22 surahs.
- Only-malak (no shayāṭīn in the surah): 15 surahs — 11, 13, 32, 33, 34, 39, 42, 53, 66, 69, 70, 74, 78, 89, 97. Biased toward eschatological Meccan surahs (the angel-heavy late-Meccan cluster: 32, 53, 69, 70, 74, 78, 89, 97 — six of the eight are tiny and terminal).
- Only-shayāṭīn: 14 surahs — 5, 14, 19, 24, 26, 27, 28, 29, 31, 36, 58, 59, 67, 81. Biased toward narrative or polemical surahs.

### Verse-level co-occurrence

**Exactly TWO verses in the whole Quran contain both `malak` and `shayṭān`:**

1. **Q 2:102** — Sulaymān / Hārūt / Mārūt / Babylon. "The devils taught humans sorcery, and what was sent down on the *two angels* at Babylon, Hārūt and Mārūt." The devils and the angels appear in the same verse because the verse is explicitly about the *boundary between permitted and forbidden supernatural knowledge*. The angels say "we are a trial — do not disbelieve"; the devils exploit. Same verse, opposite polarity.
2. **Q 7:20** — Eden. "Satan whispered to them: your Lord forbade you this tree only lest you become *angels* (malakayn, in the dual, or *immortal* — reading varies) or be among the eternal." Again the two lemmas meet at a boundary-crossing: Satan's temptation is specifically *to become like angels*.

**Finding:** the single semantic axis on which the Quran puts angels and devils in the same verse is the *transgression of the angelic/satanic boundary by humans*. Sorcery at Babylon; angel-envy in Eden. At every other occurrence the two categories are lexically segregated. This is a strong structural claim not noted, to my knowledge, in classical tafsīr — it is visible only when all 88+88 occurrences are tabulated.

### The polarity in the text

Where the two overlap at surah level without same-verse co-occurrence, one typically sets up the other:

- Surah 2 has malak 10× and shayṭān 7×. Shayṭān is the first named supernatural actor after God (2:14, 2:36). Angels appear first at 2:30 (prostration), and the only same-verse is 2:102.
- Surah 7 has 2 malak and 8 shayṭān. The prostration is at 7:11 (malak); the seduction at 7:20 (both, in the boundary verse).
- Surah 6 has 7 malak and 6 shayṭān, all in polemic passages.

The Quran's angelology is therefore the opposite of Zoroastrian dualism: the two orders are *not* coequal combatants, they are lexically distinct populations with a single-boundary overlap at two specific human-test episodes.

---

## 6. The "eight throne-bearers on that Day" in depth

Q 69:17 in literal word-order: "wa-l-malaku ʿalā arjāʾihā, wa-yaḥmilu ʿarsha Rabbika fawqahum yawmaʾidhin thamāniyah" — "and the angels will be on its sides, and above them on that Day eight will bear the Throne of your Lord."

**Three interpretive cruxes, all visible from the text alone:**

1. `al-malaku` is singular with the definite article — collective usage ("the angel-kind"), a common Arabic idiom. So the surrounding angels are unnumbered.
2. The number `thamāniyah` (eight, feminine grammatical gender) is unspecified whether it is eight *angels* or eight *ranks* or eight *something else*. The feminine gender of the numeral is an elegance-question — if the implied head-noun is `malāʾika` (broken plural, takes feminine agreement), `thamāniyah` is correct; if the implied head is `anfus` or `firaq`, also feminine. The Quran does not name the eight.
3. `yawmaʾidhin` ties the eight strictly to the Day.

**So: is the current number seven?** The Quran does not say. Classical tafsīr pulls the number seven from hadith (e.g. "The number of throne-bearers now is four; on the Day of Judgment, eight"). Those traditions exist, but the *Quran* has only the single number eight, and only for the eschaton.

**Comparison:** the Ezekiel throne-vision has four living creatures (Ezek 1:5), multiplied to eight only at the apocalyptic climax. 1 Enoch 40 has four archangels of the presence, then (in chap. 71) multiplied. The Quran's "eight on that Day" has no straightforward parallel; the closest inner-Quranic structural analogue is Q 74:30's nineteen over hellfire — another eschatological-fixed number over a throne-like station (hell-throne vs divine-Throne).

### Numerical aside

`thamāniyah` (eight) in Q 69:17 sits in a surah of 52 verses (al-Ḥāqqah). The word *thamāniyah* appears only 3 times total in the Quran: Q 69:17, Q 28:27 (Moses and the eight years of shepherding service for Shuʿayb), and Q 18:22 (the Seven Sleepers: "they say they were seven and the eighth of them was their dog" — where `thāminuhum kalbuhum`). Three occurrences of "eight," each at an eschatological or ambiguous-counting pivot. The 69:17 usage is the only one attaching eight to angels.

---

## 7. Compact catalog — every angelic entity in the Quran

| Designation | Arabic | Locus | Count | Status |
|---|---|---|---|---|
| Jibrīl (Gabriel) | جبريل | 2:97, 2:98, 66:4 | 3 | named |
| Mīkāl (Michael) | ميكال | 2:98 | 1 | named, hapax |
| Mālik (hell-warden) | مالك | 43:77 | 1 | named, hapax |
| Hārūt | هاروت | 2:102 | 1 | named, hapax, disputed |
| Mārūt | ماروت | 2:102 | 1 | named, hapax, disputed |
| Rūḥ al-Qudus | روح القدس | 2:87, 2:253, 5:110, 16:102 | 4 | title, ID debated |
| Rūḥ al-Amīn | روح الأمين | 26:193 | 1 | title |
| al-Rūḥ | الروح | 19:17, 17:85, 70:4, 78:38, 97:4 etc. | 21 total rūḥ | title, ID debated |
| Throne-bearers (now) | حملة العرش | 40:7 | no number | group |
| Throne-bearers (eschaton) | 8 | 69:17 | 8 | group, numbered |
| Hell-keepers | خزنة جهنم | 74:30, 40:49, 67:8, 39:71-72 | 19 | group, numbered |
| Zabāniyah | الزبانية | 96:18 | hapax | group |
| Noble scribes | كرام كاتبين | 82:11 | — | group |
| Guardians | حفظة | 6:61 | — | group |
| Trailing guardians | معقبات | 13:11 | hapax | group |
| Angel of death | ملك الموت | 32:11 | singular | named-by-office |
| Death-takers | الملائكة يتوفون | 4:97, 8:50, 16:28, 16:32, 47:27 | — | group |
| Harsh angels | ملائكة غلاظ شداد | 66:6 | — | group |
| Angels of Badr | ألف من الملائكة مردفين | 8:9, 8:12 | 1,000 | group, numbered |
| Angels of Uhud-reassurance | ٣٠٠٠ ، ٥٠٠٠ مسومين | 3:124-125 | 3,000 / 5,000 | group, numbered, conditional |
| Rank-ordering angels | الصافات | 37:1-3 | — | group |
| Sent-forth bands | المرسلات etc. | 77:1-5 | 5 ranks | group |
| Soul-extracting bands | النازعات etc. | 79:1-5 | 5 ranks | group |
| Annunciation-angels | رسلنا | 3:42-45, 11:69 ff., 15:51 ff., 19:17, 51:24 | several | group / individual |
| Prostration-angels | الملائكة اسجدوا | 2:34, 7:11, 15:28-31, 17:61, 18:50, 20:116, 38:71-74 | all | group |

---

## 8. Summary findings

1. **Exact-88 parity** between lemma *malak* and lemma *shayṭān* — statistically suggestive, theologically resonant.
2. **Same-verse co-occurrence of angels and devils is restricted to exactly 2 verses (2:102 and 7:20)** — both are boundary-crossing temptation scenes. Outside these, the lexicons are disjoint.
3. **Jibrīl is named 3×, Mīkāl 1×, Mālik 1×, Hārūt/Mārūt 1× each.** No other angel bears a proper name in the Quran — ʿIzrāʾīl, Isrāfīl, Raqīb, ʿAtīd, Munkar, Nakīr are all post-Quranic tradition.
4. **At Badr the Quran explicitly orders angels into combat** (8:12 direct imperative "strike above the necks"). At Uhud the Quran only *recalls* angelic support as rhetorical reassurance. So "angels fought at Badr" is textually grounded; "angels fought at Uhud" is not.
5. **The peaceful/harsh angel pairing is formal**: Q 16:28 and 16:32 are the pivot — same verse-family, same root (death-taking), opposite register, same lexical word *salām* with inverted valence.
6. **"Seven throne-bearers now / eight on that Day"** is tafsīr, not Quran. The Quran gives only the eschatological eight (69:17). Present-tense throne-bearing (40:7) has no number.
7. **The 19 (74:30) is the only numerically fixed angelic corps in present time** — contrasted with the 8 that emerge only *yawmaʾidhin*.
8. **Three different lexemes** for guardian-angels (`muʿaqqibāt`, `ḥafaẓah`, `kirām kātibīn`) — the Quran does not use a single technical term; classical tradition harmonized them.
9. The oath-ranks of surahs 37, 77, 79 add 13 feminine-plural participial descriptions of angelic activity *without* using the lemma *malak* — the angels are described only by their verbs. This is the Quran's iconographic mode: the angel is known by its action, not its name.
10. **al-Rūḥ is ambiguous**: textually it is *listed beside* the angels (70:4, 78:38, 97:4) yet functions *as* an angel (19:17, 26:193 // 2:97). The Quran does not resolve the identification; classical tafsīr does.

---

*End of catalog. 88 angel-tokens. 5 named angels (6 if Rūḥ counts). 19 over hell. 8 at the Throne on that Day. And exactly 2 verses where the two orders meet.*
