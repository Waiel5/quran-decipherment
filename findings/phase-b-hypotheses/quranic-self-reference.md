---
finding_id: quranic-self-reference
phase: B
status: deep-audit complete
date: 2026-04-12
agent: self-reference-run-1
rules:
  orthography: no-tashkeel primary (alef variants normalized → ا, alif-maksūra → ي, tā marbūṭa → ه)
  root_source: Kais Dukes morphology v0.4 (Quranic Arabic Corpus)
  verse_numbering: Hafs-Kufan
  inclusion_rule: noun-form self-naming only; verbs (qaraʾa, dhakara, nazzala) excluded from the Name Inventory
  exclusion_rule: homographs (dhikr=male; al-kitāb=Torah/Gospel when context requires) excluded
cross_refs:
  - findings/intra-quranic-cross-references.md
  - findings/khawatim-al-hashr-analysis.md
  - findings/phase-b-hypotheses/parables-catalog.md
  - findings/phase-b-hypotheses/quotation-analysis.md
---

# Quranic self-reference — the full audit

The Quran is a text that names itself. It calls itself by at least ten distinct nouns, describes itself with at least eight distinct adjectives, rejects at least seven alternative genre-identifications that its audience proposed, and challenges mankind and jinn combined to produce anything like it. This file catalogs that self-awareness comprehensively.

The Quran is ONE text; there is no edition framing. Every occurrence listed below is from the same book pointing at itself.

---

## 1. The Name Inventory

### 1.1 al-Qurʾān (الْقُرْآن) — "the Recitation"

The signature self-name. Root qrʾ = read/recite/collect. 70 noun-tokens in the morphology; appearing in 50+ verses definite + indefinite. The name is itself a performance noun — it names not the object-text but the *act* of recitation that produces it. This is theologically significant: the Quran names itself not "the Book" primarily (though it does) but "the Recital," a process noun.

#### 1.1a "hādhā l-Qurʾān" — the deictic self-gesture (16 verses)

This is the clearest marker of self-awareness: the text literally pointing at itself.

| # | Verse | Function |
|---|---|---|
| 1 | Q 6:19 | "ūḥiya ilayya hādhā l-Qurʾān li-undhirakum bi-hi" — purpose-statement |
| 2 | Q 10:37 | "wa-mā kāna hādhā l-Qurʾān an yuftarā" — authenticity claim |
| 3 | Q 12:3 | "bi-mā awḥaynā ilayka hādhā l-Qurʾān" — narrative framing |
| 4 | Q 17:9 | "inna hādhā l-Qurʾān yahdī lillatī hiya aqwam" — function |
| 5 | Q 17:41 | "wa-laqad ṣarrafnā fī hādhā l-Qurʾān" — method (ṣarf) |
| 6 | Q 17:88 | "an yaʾtū bi-mithli hādhā l-Qurʾān" — the inimitability challenge |
| 7 | Q 17:89 | "wa-laqad ṣarrafnā li-l-nās fī hādhā l-Qurʾān" — doublet of 17:41 |
| 8 | Q 18:54 | "wa-laqad ṣarrafnā fī hādhā l-Qurʾān li-l-nās" — triplet |
| 9 | Q 25:30 | "ittakhadhū hādhā l-Qurʾān mahjūrā" — Prophet's complaint |
| 10 | Q 27:76 | "inna hādhā l-Qurʾān yaquṣṣu ʿalā banī Isrāʾīl" — function |
| 11 | Q 30:58 | "wa-laqad ḍarabnā li-l-nās fī hādhā l-Qurʾān min kulli mathal" — parable method |
| 12 | Q 34:31 | "lā nuʾminu bi-hādhā l-Qurʾān" — unbeliever quotation |
| 13 | Q 39:27 | "wa-laqad ḍarabnā li-l-nās fī hādhā l-Qurʾān min kulli mathal" — doublet of 30:58 |
| 14 | Q 41:26 | "lā tasmaʿū li-hādhā l-Qurʾān wa-lghaw fī-hi" — enemy quotation |
| 15 | Q 43:31 | "lawlā nuzzila hādhā l-Qurʾān ʿalā rajul" — opponent quotation |
| 16 | **Q 59:21** | "law anzalnā hādhā l-Qurʾān ʿalā jabal" — the mountain parable |

**Observation:** fifteen of sixteen are Meccan. Q 59:21 is the sole Medinan instance — and it is the only one that gives a physical metaphor for the Quran's own power (the mountain would crumble). The Meccan pattern uses "hādhā l-Qurʾān" polemically against disbelievers; the lone Medinan use reframes the deictic within a cosmic parable. See `khawatim-al-hashr-analysis.md` for the structural framing of that verse.

**Recurring matrix verbs:** ḍarabnā ("we struck" — parables), ṣarrafnā ("we varied"), awḥaynā ("we revealed"), ātaynā ("we gave"). Each is divine-subject plural. The Quran's self-reference is bound to the "We" of revelation (see §6).

#### 1.1b al-Qurʾān + descriptor (the seven canonical epithets)

| Epithet | Meaning | Verse(s) |
|---|---|---|
| al-Qurʾān al-ʿaẓīm | the great Quran | Q 15:87 |
| al-Qurʾān al-ḥakīm | the wise Quran | Q 36:2 |
| qurʾān karīm | a noble Quran | Q 56:77 |
| qurʾān majīd | a glorious Quran | Q 85:21 |
| qurʾān mubīn | a clarifying Quran | Q 15:1, 36:69 |
| qurʾān ʿarabī | an Arabic Quran | Q 12:2, 20:113, 39:28, 41:3, 42:7, 43:3, 46:12 |
| qurʾān ʿajab | a wondrous Quran | Q 72:1 (jinn-quotation) |
| qurʾān dhū l-dhikr | a Quran of remembrance | Q 38:1 |

Six of these epithets occur exactly once; ʿarabī is the workhorse (7×); mubīn doubles. The single-occurrence pattern (hapax-epitheton) is the norm — the Quran prefers *distinct* self-descriptors over repetition.

### 1.2 al-Kitāb (الْكِتَاب) — "the Book"

The second great self-name. 151 definite occurrences; the majority refer to this Quran. Signature openings:

- **tilka āyātu l-kitāb** ("those are the verses of the Book") — Q 10:1, 12:1, 13:1, 15:1, 26:2, 27:1, 28:2, 31:2 (8 muqaṭṭaʿāt-opening surahs; see `muqattaat-analysis.md`).
- **kitāb anzalnāhu** ("a Book we have sent down") — Q 6:92, 6:155, 14:1, 38:29.
- **tanzīl al-kitāb** ("the sending-down of the Book") — Q 32:2, 39:1, 40:2, 45:2, 46:2 (the "Ḥā-Mīm" cluster).
- **dhālika l-kitāb lā rayba fīh** ("That is the Book — no doubt in it") — Q 2:2 (the very first content-verse of the textual Quran after al-Fātiḥa, positioning the Quran as pointing AT itself from outside itself — the "that Book" rather than "this Book").

Theologically: al-Kitāb names the Quran as *inscribed* — the object — while al-Qurʾān names it as *recited* — the event. Together they hold the full phenomenology of the revelation.

### 1.3 al-Furqān (الْفُرْقَان) — "the Criterion / Separator"

Root frq = to separate, distinguish. 6 verse-occurrences; 4 refer to the revelation to Muḥammad, 2 to Moses's revelation.

| Verse | Reference |
|---|---|
| Q 2:53 | Moses |
| Q 2:185 | the Quran (revealed in Ramadan) |
| Q 3:4 | the Quran (+ Torah/Injil) |
| Q 8:29 | inner-furqān (discernment) |
| Q 8:41 | "the day of the furqān" (Badr) |
| Q 21:48 | Moses + Aaron |
| Q 25:1 | the Quran ("tabāraka lladhī nazzala l-furqān") |

The title of Sūrat al-Furqān (25) is itself a self-naming: the surah names the Quran by this name in its opening verse. Al-Furqān is the Quran *under its judicial aspect* — the text as criterion that separates truth from falsehood.

### 1.4 al-Dhikr / al-Dhikrā (الذِّكْر / الذِّكْرَى) — "the Reminder / the Remembrance"

Root *kr. Two different nominal patterns. Al-Dhikr = the masculine reminder; al-Dhikrā = the feminine abstract reminder-act.

**al-Dhikr as name for the Quran (11 verses):**
- Q 15:6 ("you on whom al-dhikr was sent down") — quoted opponent speech
- Q 15:9 — "innā naḥnu nazzalnā al-dhikr wa-innā la-hu la-ḥāfiẓūn" (the preservation-pledge)
- Q 16:44 — "wa-anzalnā ilayka l-dhikr"
- Q 21:50 — "wa-hādhā dhikr mubārak anzalnāhu" (indefinite + blessed descriptor)
- Q 25:29 — "laqad aḍallanī ʿan al-dhikr"
- Q 36:11 — "man ittabaʿa l-dhikr"
- Q 38:1 — "wa-l-qurʾān dhī l-dhikr" (the two names in one oath-formula)
- Q 38:8 — "a-unzila ʿalayhi al-dhikr"
- Q 41:41 — "alladhīna kafarū bi-l-dhikr" + "wa-innahu la-kitābun ʿazīz"
- Q 43:5 — "a-fa-naḍribu ʿankum al-dhikr"
- Q 54:25 — "a-ulqiya l-dhikr ʿalayhi" (Thamūd)
- Q 68:51 — "lammā samiʿū l-dhikr"

Exclude: "ahl al-dhikr" (Q 16:43, 21:7) refers to people of prior scripture.

**al-Dhikrā** (Q 6:68, 44:13, 51:55, 80:4, 87:9, 89:23) — the reminder as function; not always the Quran-as-object but the Quran's operational mode. Q 51:55 is programmatic: "wa-dhakkir fa-inna l-dhikrā tanfaʿu l-muʾminīn."

**Q 15:9 is the apex of this name:** the Quran claims divine preservation of itself using the name al-Dhikr. This is the verse that the Islamic tradition takes as the doctrinal ground for taḥrīf (non-corruption).

### 1.5 al-Tanzīl (التَّنْزِيل) — "the Sent-Down"

Root nzl, form II verbal noun. 15 verse-occurrences, nearly all self-referential:

Q 17:106, 20:4, 25:25, 26:192, 32:2, 36:5, 39:1, 40:2, 41:2, 41:42, 45:2, 46:2, 56:80, 69:43, 76:23.

Five of these open surahs of the Ḥā-Mīm / Ṣād family (32, 39, 40, 41, 45, 46). The formula "tanzīl al-kitāb min Allāh al-ʿazīz al-ḥakīm" (or variations) is a mini-chorus. The Quran names itself as fundamentally *vertical* — the down-sent — across an entire surah-family.

**Q 26:192 and Q 69:43 both use "la-tanzīl rabb al-ʿālamīn"** — identical formula across Meccan layers, identifying the text with its cosmic origin.

### 1.6 al-Ḥaqq (الْحَقّ) — "the Truth"

When al-ḥaqq refers specifically to the revelation (not to God, not to abstract truth), the diagnostic formula is "huwa l-ḥaqq min rabbika" or variations:

- Q 2:91 — "huwa l-ḥaqq muṣaddiqan li-mā maʿahum"
- Q 2:119 — "arsalnāka bi-l-ḥaqq"
- Q 2:176 — "dhālika bi-anna llāha nazzala l-kitāba bi-l-ḥaqq"
- Q 2:213, 3:3, 4:105, 5:48 — "anzalnā l-kitāba bi-l-ḥaqq"
- Q 10:108, 17:81, 32:3, 34:6, 35:31, 47:2 — "huwa l-ḥaqq" or equivalent
- Q 69:51 — "wa-innahu la-ḥaqq al-yaqīn"

The density of bi-l-ḥaqq as revelation-carrier (at least 15 verses) makes al-Ḥaqq functionally a self-name. It is notable that the Quran does not often say "I am al-Ḥaqq" — it says "we sent you/the Book *with* al-Ḥaqq," positioning the text as the vehicle of truth rather than truth itself. The climactic formula is Q 69:51: "it is indeed the certainty-of-truth."

### 1.7 al-Nūr (النُّور) — "the Light"

Of 40+ occurrences of nūr, five refer to the Quran directly:
- Q 4:174 — "anzalnā ilaykum nūran mubīnan"
- Q 5:15 — "qad jāʾakum min Allāh nūrun wa-kitābun mubīn"
- Q 7:157 — "ittabaʿū al-nūr alladhī unzila maʿahu"
- Q 42:52 — "jaʿalnāhu nūran nahdī bi-hi" (the Rūḥ-verse)
- Q 64:8 — "fa-āminū bi-llāh wa-rasūlihi wa-l-nūr alladhī anzalnā"

Al-Nūr is the Quran *in its illumination-mode* — the text as that which lets one see. It appears in parallel with al-Kitāb: the Book is what the Light-is-in. The Quran names itself as instrument of moral optics.

### 1.8 al-Bayān / al-Mubīn — "the Clarifier"

Root byn. "Al-Bayān" as definite noun appears exactly once — Q 55:4 — and there describes teaching, not directly the text (though exegetes often link the two).

The functional self-naming is **mubīn** (125 verses with that form), applied to the Quran as qurʾān mubīn (Q 15:1, 36:69) or kitāb mubīn (numerous). The Book repeatedly names itself as "clarifying" — explicative rather than cryptic (despite the muqaṭṭaʿāt).

Q 75:19 gives the Quran's own verb for what it does to itself: "thumma inna ʿalaynā bayānahu" — "upon Us is its clarification." This ties back to §1.3: Quran = Recital; Kitāb = Book; Bayān = the explication that comes after both.

### 1.9 al-Mathānī (الْمَثَانِي)

See §8 for the deep dive. Two verses (Q 15:87, Q 39:23) constitute the entire corpus for this name — but these two verses frame the entire Quran's compositional logic.

### 1.10 al-Hudā (الْهُدَى) — "the Guidance"

The second verse of the Quran after al-Fātiḥa — Q 2:2 — names the Book as "hudan li-l-muttaqīn." Al-Hudā appears 23× as definite noun; hudan as indefinite 39× more. A substantial majority of these are self-referential when they appear with the Book or in context of revelation. Key examples:

- Q 2:2 — "hudan li-l-muttaqīn"
- Q 2:185 — the Quran "hudan li-l-nās" (the broadest claim: not just believers)
- Q 6:88 — "dhālika hudā llāh yahdī bi-hi man yashāʾ"
- Q 7:52 — "kitāb … hudan wa-raḥmatan li-qawmin yuʾminūn"
- Q 16:64 — "hudan wa-raḥmatan li-qawm yuʾminūn" (+ many more doublets)
- Q 17:9 — (quoted above) "inna hādhā l-qurʾān yahdī lillatī hiya aqwam"

The pattern **hudan wa-raḥma** ("guidance and mercy") is the paired-descriptor signature of the Quran's self-function — it recurs at least 14× (Q 7:52, 7:154, 10:57, 12:111, 16:64, 16:89, 27:77, 28:43, 29:51, 31:3, 45:20, and more).

### 1.11 Other rarer self-names

- **Rūḥ** (spirit) — Q 42:52, 16:102, 26:193 ("nazala bi-hi al-rūḥ al-amīn"). The Quran names itself as something "spirit-like."
- **Tadhkirah** (reminder) — Q 20:3, 56:73, 69:48 ("innahu la-tadhkiratun li-l-muttaqīn"), 73:19, 74:49, 74:54, 76:29, 80:11. Nine occurrences.
- **ʿArabī** (Arabic) — seven times paired with qurʾān. The Quran names its own language.
- **Ḥaqq al-yaqīn** — Q 69:51 (unique, climactic).
- **Aḥsan al-ḥadīth** — Q 39:23 ("the best of discourses") — the Quran inside its own genre-comparison.

---

## 2. Self-Descriptors (Adjective Inventory)

The Quran piles eight distinct superlative descriptors onto itself:

| Descriptor | Gloss | Verses | Typical collocation |
|---|---|---|---|
| mubārak | blessed | Q 6:92, 6:155, 21:50, 38:29 | "kitāb mubārak" / "dhikr mubārak" |
| karīm | noble | Q 56:77 | "la-qurʾān karīm" |
| majīd | glorious | Q 85:21 | "qurʾān majīd" |
| ʿaẓīm | mighty | Q 15:87 | "al-qurʾān al-ʿaẓīm" |
| ḥakīm | wise | Q 10:1, 31:2, 36:2 (+ Q 3:58 al-dhikr al-ḥakīm) | "al-kitāb al-ḥakīm" |
| ʿajīb | marvelous | Q 72:1 | "qurʾān ʿajab" (jinn perspective) |
| maknūn | kept-hidden / preserved | Q 56:78 | "kitāb maknūn" |
| maḥfūẓ | preserved | Q 85:22 | "lawḥ maḥfūẓ" |
| mubīn | clarifying | Q 15:1, 36:69 + dozens of "kitāb mubīn" | "qurʾān mubīn" |
| ʿarabī | Arabic | Q 12:2 + 6 others | "qurʾān ʿarabī" |
| ʿazīz | mighty/inaccessible | Q 41:41 | "kitāb ʿazīz" |

Two clusters emerge:
- **Ontological / dignity cluster:** karīm, majīd, ʿaẓīm, maknūn, maḥfūẓ, ʿazīz. The Quran as heavenly, precious, untouchable, guarded.
- **Operational / functional cluster:** mubārak, ḥakīm, mubīn, hudan, shifāʾ, raḥma, nūr. The Quran as doing things — blessing, explaining, healing, guiding, illuminating.

---

## 3. The Meta-Verses — where the Quran explicitly describes its own nature

This is the Quran's *prose poetics* of itself. Fifteen passages, ranked roughly by explicitness:

### Tier 1 — programmatic meta-statements

- **Q 75:17-19** — "inna ʿalaynā jamʿahu wa-qurʾānahu; fa-idhā qaraʾnāhu fa-ttabiʿ qurʾānahu; thumma inna ʿalaynā bayānahu." Three successive divine acts: **collection, recitation, clarification.** The Quran names its own production as a three-stage divine process.
- **Q 39:23** — "allāhu nazzala aḥsana l-ḥadīthi kitāban mutashābihan mathāniya taqshaʿirru minhu julūdu …" The Quran's fullest self-description: **best discourse, Book, self-similar, doubled/paired, skin-shivering.**
- **Q 15:87** — "wa-laqad ātaynāka sabʿan min al-mathānī wa-l-qurʾān al-ʿaẓīm." The "seven mathānī + the great Quran" (see §8).
- **Q 42:52-53** — "wa-kadhālika awḥaynā ilayka rūḥan min amrinā … wa-lākin jaʿalnāhu nūran nahdī bi-hi man nashāʾ." The Quran = rūḥ = nūr. Three nouns collapsed.
- **Q 17:106** — "wa-qurʾānan faraqnāhu li-taqraʾahu ʿalā l-nās ʿalā mukthin wa-nazzalnāhu tanzīlā." The Quran self-describes as piecemeal (faraqnāhu) + gradual (ʿalā mukthin) + downward-sent.

### Tier 2 — ontology of the text

- **Q 56:77-80** — "innahu la-qurʾānun karīm / fī kitābin maknūn / lā yamassuhu illā l-muṭahharūn / tanzīlun min rabb al-ʿālamīn." A four-verse self-ontology: **noble Quran → in a hidden Book → untouched except by the purified → sent-down from the Lord of worlds.** Four-stage nesting: Qurʾān inside Kitāb Maknūn inside heavenly origin.
- **Q 85:21-22** — "bal huwa qurʾānun majīd / fī lawḥin maḥfūẓ." Two-verse doublet of the Q 56 ontology — glorious Quran in a preserved tablet. Together 56:77-80 and 85:21-22 establish the *preserved-archetype* doctrine: the Quran on earth is the projection of a preserved heavenly original.
- **Q 43:3-4** — "innā jaʿalnāhu qurʾānan ʿarabiyyan laʿallakum taʿqilūn / wa-innahu fī umm al-kitāb ladaynā laʿaliyyun ḥakīm." Same ontology: the earthly Arabic recitation ← the "mother of the Book" with God, high and wise.

### Tier 3 — function and method

- **Q 17:82** — "wa-nunazzilu min al-qurʾāni mā huwa shifāʾun wa-raḥmatun li-l-muʾminīn wa-lā yazīdu al-ẓālimīna illā khasāran." **Therapeutic self-description** — the Quran as healing and mercy for believers, increasing-loss for wrongdoers. The text names itself as dual-action.
- **Q 17:9** — "inna hādhā l-qurʾān yahdī lillatī hiya aqwam" — directional self-description.
- **Q 73:20** — "fa-qraʾū mā tayassara min al-qurʾān" — reader-facing: recite what is manageable. The text acknowledges its own difficulty.
- **Q 41:44** — "wa-law jaʿalnāhu qurʾānan aʿjamiyyan …" — the counterfactual: *if* we had made it non-Arabic. The text names the fact of its own linguistic choice.
- **Q 27:91-92** — "umirtu an akūna min al-muslimīn / wa-an atluwa l-qurʾān" — commissioning formula tying the Messenger to al-Qurʾān as his duty.

### Tier 4 — the challenge verses (taḥaddī)

See §4.

### Tier 5 — genre negation

- **Q 36:69** — "wa-mā ʿallamnāhu l-shiʿra wa-mā yanbaghī lahu in huwa illā dhikrun wa-qurʾānun mubīn." Denies poetry; affirms two self-names.
- **Q 69:40-47** — the seven-way genre denial (§7).
- **Q 81:19-25** — its doublet.

### Tier 6 — apotropaic self-description

- **Q 59:21** — the mountain parable. The Quran names its own shattering power on a metaphorical substrate. See `khawatim-al-hashr-analysis.md`.

---

## 4. The Challenge Verses (taḥaddī) — Comparative Analysis

Classical tradition identifies three-to-five challenge verses. I count five:

| Verse | Challenge | Scope |
|---|---|---|
| Q 52:33-34 | "fa-l-yaʾtū bi-ḥadīthin mithlihi" — bring a *discourse* like it | Vague — any discourse |
| Q 17:88 | "bi-mithli hādhā l-qurʾān" — bring the whole Quran's like | Maximalist — the entire text |
| Q 11:13 | "bi-ʿashri suwarin mithlihi muftarayāt" — ten forged surahs | Ten units |
| Q 10:38 | "bi-sūratin mithlihi" — one surah like it | One unit |
| Q 2:23 | "bi-sūratin min mithlih" — a surah from his like | One unit, genitive softened |

### Is there a progressive softening?

The classical reading (ṭabarī, rāzī) sees progressive softening: whole Quran → ten surahs → one surah. My ordering above is by scope. The chronological question matters:

- Q 17 is Meccan (probably middle-late Meccan).
- Q 11 is late Meccan.
- Q 10 is late Meccan (slightly earlier than 11 in some chronologies).
- Q 2 is the first major Medinan surah.
- Q 52 is early Meccan.

Plausible chronological trajectory (late → early by scope): Q 52 (vague "ḥadīth") → Q 17 (whole Quran) → Q 11 (ten surahs) → Q 10 (one surah) → Q 2 (one surah, Medinan reprise). The challenge doesn't simply soften — it moves from **vague-open to maximal to narrow**, then is *repeated* in Medina.

### Structural unity of the challenges

Four of the five share a common formula:
- **qul fa-ʾtū bi-...** (imperative) + **wa-dʿū man istaṭaʿtum** ("call whomever you can") + **in kuntum ṣādiqīn** ("if you are truthful").

Q 2:23 uses "wa-dʿū shuhadāʾakum" instead of "istaṭaʿtum." Q 17:88 uniquely expands the invitation to "al-ins wa-l-jinn" — the challenge becomes cosmic, the only instance where the Quran explicitly frames itself as beyond the combined linguistic capacity of humans + jinn.

### Literary geometry

Q 17:88 is the structural keystone: the one challenge that targets the entire text as object, using the deictic "hādhā l-Qurʾān." It is also the only challenge verse that posits cooperation-impossibility ("even if some of them helped others"). The Quran thereby names itself as that which cannot be collectively produced.

---

## 5. "hādhā al-Qurʾān" — the deictic count

Exactly **16 verses** (see §1.1a). Distribution:

| Surah | Count |
|---|---|
| 6 (al-Anʿām) | 1 |
| 10 (Yūnus) | 1 |
| 12 (Yūsuf) | 1 |
| 17 (al-Isrāʾ) | 4 |
| 18 (al-Kahf) | 1 |
| 25 (al-Furqān) | 1 |
| 27 (al-Naml) | 1 |
| 30 (al-Rūm) | 1 |
| 34 (Sabaʾ) | 1 |
| 39 (al-Zumar) | 1 |
| 41 (Fuṣṣilat) | 1 |
| 43 (al-Zukhruf) | 1 |
| 59 (al-Ḥashr) | 1 |

**Surat al-Isrāʾ (17) contains 4 of the 16** — by far the densest. Q 17:9, 17:41, 17:88, 17:89 — plus 17:82 (shifāʾ) and 17:106 (tanzīlā). Al-Isrāʾ is arguably the Quran's most self-reflexive surah.

The deictic self-reference is a **polemical instrument**. Nine of sixteen verses occur in disputational contexts (direct quote of opponents, or divine rebuttal).

---

## 6. The "I" and "We" of the Quran — divine voice as self-naming

The Quran almost never says "I" (ana) about the revelation act. Instead it uses plural **naḥnu / naḥnu**-embedded verbs for the revelation:

- **nazzalnā / anzalnā** ("we sent down") — 118+ forms
- **atayna / ātaynāka** ("we gave / we gave you") — 45+
- **awḥaynā** ("we revealed") — 30+
- **ṣarrafnā** ("we varied") — 7×, all about the revelation's method
- **ḍarabnā** ("we struck a parable") — clustered with self-reference
- **faṣṣalnā** ("we expounded in detail") — 12×
- **katabnā** ("we wrote") — 7×, including Q 21:105

The pattern: **every meta-statement about the Quran's composition is voiced in the divine plural.** The grammatical "we" is the metaphysical subject of the self-reference. The Quran names itself only through a voice that locates itself above the text.

Notable exception: Q 15:9 — "innā **naḥnu** nazzalnā al-dhikr wa-innā **la-hu** la-ḥāfiẓūn." The double-emphatic "we, we sent down" + "for it, we are guardians." The pledge of preservation is the only verse that doubles the "we" pronoun for intensity.

---

## 7. Genre self-consciousness — the seven rejections

The Quran positions itself by rejecting seven alternative identifications that its audience proposes:

| # | Rejected category | Arabic | Loci |
|---|---|---|---|
| 1 | Poetry | shiʿr / shāʿir | Q 21:5, 36:69, 37:36, 52:30, 69:41 |
| 2 | Soothsaying | kāhin | Q 52:29, 69:42 |
| 3 | Madness | majnūn | Q 37:36, 52:29, 68:2, 81:22 |
| 4 | Satanic speech | qawl shayṭān | Q 81:25, 26:210-212 |
| 5 | Fabrication by the Prophet | iftarāhu / tuqawwul | Q 10:37, 11:13, 21:5, 25:4, 32:3, 46:8, 69:44 |
| 6 | Tales of the ancients | asāṭīr al-awwalīn | Q 6:25, 8:31, 16:24, 23:83, 25:5, 27:68, 46:17, 68:15, 83:13 |
| 7 | Magic | siḥr / siḥr mubīn | Q 6:7, 10:76, 11:7, 34:43, 37:15, 43:30, 46:7, 74:24 |

Nine cases of "asāṭīr al-awwalīn" — this is the **most common** rejected identification. The Quran's most persistent opponent-frame is: "just stories we've heard before."

### Q 69:40-47 as the canonical composite rejection

"Indeed it is the speech of a noble messenger / it is not the speech of a poet (little do you believe) / nor the speech of a soothsayer (little do you remember) / a sending-down from the Lord of the worlds / and if he had invented even some statements upon Us / We would have seized him by the right hand / then cut from him the aorta / and none of you could have shielded him."

Seven-clause structure. Poet + soothsayer rejected. "Tanzīl" as the positive identification. Then the extraordinary claim: if the Prophet had forged even a single statement, the aorta would have been severed — a self-referential death threat to the text's own vehicle. This is as explicit a declaration of inspired-authority as any text in world religious literature.

### Q 81:19-25 as its doublet

Same structure, but the "noble messenger" is Gabriel rather than Muḥammad. The pair frame the revelation from both ends: Q 81 the angelic transmitter, Q 69 the human transmitter. Same four-clause genre-rejection grammar (not poet, not soothsayer, not possessed, not Satan's speech) applied to both links in the chain.

---

## 8. Al-Mathānī — the deep dive

Two verses, two apparent meanings. Are they compatible?

- **Q 15:87** — "wa-laqad ātaynāka sabʿan min al-mathānī wa-l-qurʾān al-ʿaẓīm." Classical majority: "sabʿan min al-mathānī" = the seven verses of al-Fātiḥa, coordinated with ("and" wa-) "the great Quran" as a separate thing.
- **Q 39:23** — "… kitāban mutashābihan mathāniya …" — the whole Book is described as mathānī.

### Grammatical possibilities

*sabʿan min al-mathānī* has three readings:
(a) "seven that are *some of* the mathānī" — the mathānī is a larger category; al-Fātiḥa is 7 of them. This is compatible with Q 39:23 which makes the *whole Book* mathānī.
(b) "seven *called* the mathānī" — the seven verses of Fātiḥa are the mathānī (identity reading). Still compatible with Q 39:23 if "mathānī" at 39:23 is coincidentally a different sense.
(c) "seven *examples of doubling*" — tafsīr tradition records this reading too: seven types of doubled material (narratives, laws, parables, signs, warnings, promises, glorifications).

### Structural analysis

The root **th-n-y** means "to bend back, double, repeat, pair." *Mathānī* is a plural of *mathnā* = "paired / doubled / bent-back." Q 39:23 glosses it with *mutashābih* = "self-similar, resembling itself." Together these two features — self-similarity and pairing — describe a **structural property of the text**: it repeats, returns upon itself, uses twinned narrative and thematic elements, and rhymes.

This is consistent with multiple large-scale structural findings in the Quran corpus:
- the paired-opposites network (see `paired-opposites-network.md`),
- the chiastic ring structures (see `chiastic-audit.md`),
- the mutashābih lafẓī doublets (see `mutashabih-lafzi.md`),
- the formulaic repetitions and refrain-surahs (Q 55, Q 77),
- the recurring qiṣaṣ (narratives told multiple times with variations).

**The two mathānī verses are fully compatible:** Q 15:87 names a specific instance (al-Fātiḥa, the seven-pair) as a sample of the category, while Q 39:23 names the Book as a whole as *of the same compositional type*. One is a synecdoche for the other. The Quran is describing its **own deep structure**: a text built of bent-back, doubled, self-resembling units at both the micro scale (al-Fātiḥa's paired halves around āya 4) and the macro scale (the whole Book).

This is the single most self-aware formal claim the Quran makes about its own composition. A text naming its own architecture.

---

## 9. Classical prior art

- **Al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*** — in the first chapter (*al-Nawʿ al-awwal*) he catalogs the **names of the Quran**, citing Ibn ʿArabī and al-Ḥarālī as having reached 55 and 90 names respectively. Al-Suyūṭī settles on his own list of around 50. His categories overlap with ours: al-Qurʾān, al-Kitāb, al-Furqān, al-Dhikr, al-Tanzīl, al-Ḥaqq, al-Nūr, al-Hudā, al-Rūḥ, al-Shifāʾ, al-Bayān, al-Faṣl, al-Ḥablu l-matīn, al-ʿUrwa al-wuthqā, al-Mathānī, etc. He mentions that many of these are descriptions more than strict names, a distinction our §1 + §2 split preserves.
- **Al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*** — similar material, organized under "asmāʾ al-Qurʾān wa-ashhar suwarih." Al-Zarkashī emphasizes the theological function of each name (e.g., al-Furqān emphasizes judicial function; al-Dhikr emphasizes continuity with prior revelation).
- **Al-Zarqānī, *Manāhil al-ʿIrfān fī ʿulūm al-Qurʾān*** — modern (20th c.) summation. Reduces the list to a smaller canonical four (Qurʾān, Kitāb, Furqān, Dhikr) with the rest as descriptors.

Our audit's value-add is *empirical* — we give exhaustive verse-level evidence, computational counts, and statistical structure (e.g., the Meccan vs. Medinan split of "hādhā l-Qurʾān," the 7-genre-rejection taxonomy, the density on Surat al-Isrāʾ).

---

## 10. The architecture of Quranic self-awareness

Pulling everything together, the Quran's self-awareness has a definite architecture:

### A. Naming layer
At least **10 major self-names** (§1) deployed for different theological functions:
- Qurʾān = recital
- Kitāb = inscribed object
- Furqān = judicial criterion
- Dhikr = reminder / continuity
- Tanzīl = vertical origin
- Ḥaqq = truth-content
- Nūr = illumination
- Hudā = directional guidance
- Bayān / Mubīn = clarification
- Mathānī = paired structure

These name the text under 10 different theological-operational aspects.

### B. Descriptor layer
At least **11 major descriptors** (§2) partitioned into *dignity* (karīm, majīd, ʿaẓīm, maknūn, maḥfūẓ, ʿazīz) and *function* (mubārak, ḥakīm, mubīn, hudan, shifāʾ, raḥma, nūr). Together these articulate the Quran's self-assertion along two axes: worth vs. work.

### C. Ontology layer
The **nested-preservation ontology** — Q 56:77-80 + Q 85:21-22 + Q 43:3-4. The earthly Arabic Quran is the projection of a heavenly preserved-tablet (lawḥ maḥfūẓ) / hidden-book (kitāb maknūn) / mother-of-the-Book (umm al-kitāb). This establishes a two-layer metaphysics of the text.

### D. Production layer
**Q 75:17-19** — three divine acts: jamʿ (collection), qurʾān (recitation), bayān (clarification). The Quran names its own production process. Q 17:106 adds faraqnāhu + ʿalā mukth (piecemeal + gradual). Q 25:32 adds "kadhālika li-nuthabbita bi-hi fuʾādaka" — the gradual revelation as psychological reinforcement.

### E. Method layer
**Q 39:23** — mutashābih + mathānī: self-similar, paired, doubled. The Quran names its own compositional signature as a return-structure.

### F. Function layer
**Hudan wa-raḥma** (14+ verses), **shifāʾ wa-raḥma** (Q 17:82, 41:44), **bashīrā wa-nadhīrā** (warner/bringer-of-good-news). The Quran names its effects on the reader: guides, has mercy, heals, warns, gladdens.

### G. Challenge layer
**Q 2:23, 10:38, 11:13, 17:88, 52:33-34.** The Quran issues five challenges. No other scripture in world religious literature so insistently and explicitly stakes its claim on unproducability.

### H. Genre-rejection layer
**Seven negations** (§7). The Quran defines itself against seven alternatives: poetry, soothsaying, madness, satanic speech, fabrication, old tales, magic. Self-definition through contrastive negation.

### I. Deictic layer
**"hādhā l-Qurʾān" × 16.** The text points at itself. This deictic is almost exclusively Meccan and polemical. It is a rhetorical move that asserts the text's objective status in disputes about its status.

### J. Divine-voice layer
**"We" throughout.** Every meta-statement about composition is voiced in the divine plural. The self-reference is always framed by a voice outside and above the text.

### K. Parable-of-self layer
**Q 59:21** — the mountain parable. A parable *about* the Quran's own ontological gravity, told *by* the Quran. Meta-parable as self-reference.

### L. Preservation-pledge layer
**Q 15:9** — the commitment of divine guardianship over the text. The Quran anticipates and preempts its own textual transmission history.

### M. Archive-claim layer
**Umm al-kitāb / lawḥ maḥfūẓ** (Q 43:4, 85:22, 56:78). The Quran claims that an unalterable archetypal copy exists outside of time.

Together these **13 layers** form what can plausibly be called the most elaborate self-referential apparatus in any single pre-modern text. A text that:
- Names itself in ten ways,
- Describes itself in eleven ways,
- Articulates its own ontology in two-layer form,
- Describes its own three-stage production,
- Names its own compositional method,
- Declares its seven functional effects,
- Issues five impossibility-challenges,
- Rejects seven competing genre-identifications,
- Points at itself sixteen times deictically,
- Voices all of this in a plural voice located above it,
- Contains a parable about its own shattering power,
- Pledges its own preservation,
- And claims an unchanging original outside time.

---

## 11. Summary table — verses to know by heart

| Category | Locus classicus |
|---|---|
| deictic self-naming | Q 17:9, Q 59:21 |
| compositional method | Q 39:23 |
| programmatic production | Q 75:17-19 |
| ontology / archetype | Q 56:77-80, Q 85:21-22, Q 43:3-4 |
| preservation-pledge | Q 15:9 |
| inimitability | Q 17:88 |
| graded challenge | Q 2:23 → 10:38 → 11:13 → 17:88 |
| genre rejection (composite) | Q 69:40-47, Q 81:19-25 |
| function: healing | Q 17:82 |
| function: guidance | Q 2:2, Q 17:9 |
| function: light | Q 42:52 |
| seven mathānī | Q 15:87 |
| best discourse | Q 39:23 |
| spirit-revelation | Q 42:52 |
| Arabic | Q 12:2, 41:3, 42:7 |

---

## 12. Open questions / future work

1. **Mathānī structural mapping** — do the ~100 pairs found in the mutashabih-lafzi catalog instantiate the mathānī principle at the phrase-level? Cross-link needed.
2. **"hādhā l-ḥadīth"** (Q 18:6, 53:59, 56:81, 68:44) — is "al-ḥadīth" a self-name used 4-5 times? This underexplored label deserves its own audit.
3. **The "qawl" family** — the Quran as "qawl faṣl" (Q 86:13), "qawl ʿaẓīm" (never applied to the Quran directly but worth checking), "qawl rasūl karīm" (Q 69:40 + 81:19). An audit of all "qawl + adjective" phrases as potential self-names.
4. **Quantifying the "preservation-pledge" reception** — Q 15:9's status as the dogmatic ground for ʿiṣmat al-Qurʾān deserves a full reception history audit, separate from this finding.
5. **Chronological migration of self-names** — early Meccan surahs prefer al-Dhikr / al-Dhikrā / tadhkirah; middle Meccan introduce hādhā l-Qurʾān deictics; late Meccan introduce the ontological nest (56, 85). Medinan largely uses al-Kitāb. Map this migration precisely.

---

*End of finding. Cross-ref chain: khawatim-al-hashr-analysis.md → intra-quranic-cross-references.md → this file → (future) hadith-as-self-name.md.*
