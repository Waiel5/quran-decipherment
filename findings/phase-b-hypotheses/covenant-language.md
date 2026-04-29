---
phase: B
finding_id: phase-b-covenant-language-run-1
date: 2026-04-12
agent: covenant-deep-agent
status: reported
claim_class: thematic / lexical-semantic
rules:
  orthography: no-tashkeel
  word_definition: QAC lemma/root
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: none (exhaustive root-extraction); chronological signal compared to the Phase-B chronological-revelation F-test framework
inputs:
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt (Dukes/QAC v0.4)
  text: quran-text/quran-no-tashkeel.json (114 surahs, 6236 verses)
  translation: data/translations/en.sahih.txt (Saheeh International)
  chronology: data/revelation-order.csv (Egyptian + Nöldeke)
scratch:
  - scratch/covenant/root-Ehd.tsv
  - scratch/covenant/root-wEd.tsv
  - scratch/covenant/root-wvq.tsv
  - scratch/covenant/root-byE.tsv
  - scratch/covenant/root-Eqd.tsv
  - scratch/covenant/verse-lists.txt
  - scratch/covenant/covenant-verses-full.txt
---

# Covenant-Language Audit — ʿahd / waʿd / mīthāq / bayʿa / ʿaqd

## 0. Headline

Covenant vocabulary is **the single largest diachronic signal in the Quran's
legal-theological register**, cleaner and more categorical than most of the
quantitative metrics reported in `chronological-revelation.md`. The five
roots split on **two orthogonal axes at once**:

1. **Root × period:** `waʿd` (promise) is Middle/Late-Meccan-heavy and
   eschatological; `mīthāq` / `bayʿa` / `ʿaqd` are Medinan-heavy and
   community-legal; `ʿahd` bridges the two, occurring across all four
   Nöldeke phases.
2. **Root × semantic frame:** `waʿd` = unilateral divine speech-act
   (promise/threat, resurrection); `ʿahd` = bilateral-but-asymmetric
   covenant (God → Adam, Israel, believers); `mīthāq` = ratified /
   witnessed covenant (always comes with juridical weight); `bayʿa` =
   ritualised human-to-God pledge (historical events); `ʿaqd` = legal
   contract (marriage, oaths, knots). Covenant is the Quran's
   **governing legal-theological framework**: every major relationship
   between God and humanity — from Adam's first forgetting to
   Hudaybiyya to the Last Day — is described as one or another kind of
   binding agreement.

The **primordial covenant of Q 7:172** ("a-lastu bi-rabbikum") is
lexically *outside* all five covenant roots. It is built on roots `Ax*`
(taking) and `$hd` (bearing witness). This is itself a finding — the
foundational covenant is *structurally unique* in the corpus.

## 1. Per-root inventory

Unique-verse counts from QAC `ROOT:` field. Meccan/Medinan column uses the
`quran-no-tashkeel.json` `type` field (Egyptian tradition). Nöldeke phase
distribution from `data/revelation-order.csv`.

| Root | Surface | Gloss | Total occ | Unique verses | Unique surahs | Meccan verses | Medinan verses |
|---|---|---|---:|---:|---:|---:|---:|
| `Ehd` | ʿahd / ʿāhada | covenant, pledge (noun & verb) | 46 | 36 | 17 | 14 | 22 |
| `wEd` | waʿd / waʿada / mīʿād | promise (noun, verb, appointed time) | 151 | 130 | 51 | 101 | 29 |
| `wvq` | mīthāq / mawthiq / wuthqā | firm/ratified covenant, handhold | 34 | 29 | 13 | 5 | 24 |
| `byE` | bayʿ / bāyaʿa / biyaʿ | sale, pledge-of-allegiance, synagogues | 15 | 11 | 8 | 1 | 10 |
| `Eqd` | ʿaqd / ʿuqda / ʿaqada | contract, knot, binding | 7 | 7 | 5 | 2 | 5 |
| **Total** | — | — | **253** | ≈213 unique | — | 123 | 90 |

### Nöldeke-phase distribution (verse counts)

| Root | Early Meccan | Middle Meccan | Late Meccan | Medinan | Total |
|---|---:|---:|---:|---:|---:|
| `Ehd` | 1 | 8 | 7 | 20 | 36 |
| `wEd` | 8 | 52 | 44 | 26 | 130 |
| `wvq` | 1 | 0 | 6 | 22 | 29 |
| `byE` | 0 | 0 | 1 | 10 | 11 |
| `Eqd` | 1 | 1 | 0 | 5 | 7 |

Observations:
- `wEd` peaks in Middle Meccan (52 verses) and Late Meccan (44). This is
  the **Meccan eschatological register** — the promise/threat vocabulary
  of Hell, Paradise, the Day.
- `wvq`, `byE`, `Eqd` are effectively Medinan roots (only 1, 0, 1 Early-
  Meccan verses respectively). They are the **community-legal register**.
- `Ehd` is genuinely diachronic: 1 / 8 / 7 / 20 across the four phases,
  a monotonic ramp consistent with the general Medinan legal-vocabulary
  expansion flagged in `chronological-revelation.md` §3 (ttr_lemma
  Medinan recovery, `Hll`/`nfq` Spearman top-12).

### Lemma inventory

| Root | Lemma | N | Semantic role |
|---|---|---:|---|
| `Ehd` | `Eahod` | 29 | covenant (noun) |
| `Ehd` | `Ea`hada` / `Eahida` | 17 | to make/keep covenant (verb) |
| `wEd` | `waEada` | 70 | to promise (verb) |
| `wEd` | `waEod` | 49 | promise (noun) |
| `wEd` | `m~awoEid` | 12 | appointed time/place (noun) |
| `wEd` | `waEiyd` | 6 | threat (noun — punishment-promise) |
| `wEd` | `m~iyEaAd` | 5 | appointed meeting / Day of Judgment |
| `wEd` | other forms | 9 | — |
| `wvq` | `m~iyva`q` | 25 | ratified covenant |
| `wvq` | `m~awoviq` | 3 | solemn promise |
| `wvq` | `wuvoqaY` | 2 | al-ʿurwa al-wuthqā (handhold) |
| `wvq` | other | 4 | — |
| `byE` | `bayoE` | 7 | trade, sale (6 commercial, 1 doctrinal-metaphor 9:111) |
| `byE` | `baAyaEa` | 6 | pledge allegiance (Form III) |
| `byE` | `biyaE` | 1 | synagogues (22:40) |
| `byE` | `tabaAyaEo` | 1 | transact a sale (2:282) |
| `Eqd` | `Euqodap` | 4 | knot (20:27, 113:4) / marriage contract |
| `Eqd` | `Euquwd` | 1 | contracts (5:1) |
| `Eqd` | `Eaqadato` / `Eaq~ad` | 2 | to bind / bound by oath |

## 2. Covenant inventory: with WHOM?

Systematic cross-reference of covenant-verses to the human/divine party.

| Covenant type | Key verses | Root(s) used | Period |
|---|---|---|---|
| **Primordial covenant with all souls** | **7:172–173** | `Ax*` + `$hd` (NOT any of the five roots) | Late Meccan |
| Covenant with Adam | 20:115, 36:60 | `Ehd` | Mid/Late Meccan |
| Covenant with all prophets (mīthāq al-nabiyyīn) | 3:81, 33:7 | `wvq` | Medinan |
| Covenant with Noah, Abraham, Moses, Jesus | 33:7 (named with Muhammad) | `wvq` | Medinan |
| Covenant with Abraham | 2:124, 2:125 | `Ehd` | Medinan |
| Covenant with Jacob's sons | 12:66, 12:80 | `wvq` (mawthiq) | Late Meccan |
| Covenant with Children of Israel (Torah covenant) | 2:40, 2:63, 2:83–85, 2:93, 2:100, 4:154–155, 5:12–13, 5:70, 7:169, 20:80, 20:86 | `Ehd` + `wvq` both | Medinan (mostly) |
| Covenant with Christians (People of Gospel) | 5:14 | `wvq` | Medinan |
| Covenant with People of the Book (conceal/reveal) | 3:187 | `wvq` | Medinan |
| Covenant with believers (bayʿa) | 48:10, 48:18, 60:12, 9:111 | `byE` (Form III) | Medinan |
| Covenant with believers ("we hear and obey") | 5:7, 57:8 | `wvq` | Medinan |
| Treaties with polytheists / non-Muslims | 8:56, 8:72, 9:1, 9:4, 9:7, 9:12, 4:90, 4:92 | `Ehd`, `wvq` | Medinan (Tawba context) |
| Marriage covenant | 2:235, 2:237, 4:21 | `Eqd`, `wvq` | Medinan |
| Oaths in general (ayman ʿaqqadtum) | 4:33, 5:1, 5:89 | `Eqd` | Medinan |
| Satan's covenant with children of Adam | 36:60 | `Ehd` (do NOT worship Satan) | Late Meccan |
| Satan's false promise | 2:268, 4:120, 14:22, 17:64 | `wEd` | Medinan 2:268, Meccan rest |

The Torah covenant with Banī Isrāʾīl is by far the densest (at least
**12 distinct verses** referring to it — 2:40, 2:63, 2:83, 2:84, 2:93,
2:100, 4:154, 4:155, 5:12, 5:13, 5:70, 7:169, plus 20:80/86 invoking
Moses's promise and 2:80/2:124-125 tangentially). No other covenant-
partner comes close.

## 3. The primordial covenant (Q 7:172) — structurally unique

The verse reads (Sahih translation): *"And [mention] when your Lord took
from the children of Adam — from their loins — their descendants and
made them testify of themselves, [saying to them], 'Am I not your Lord?'
They said, 'Yes, we have testified.' [This] — lest you should say on the
day of Resurrection, 'Indeed, we were of this unaware.'"*

**Finding: 7:172 uses none of the five covenant roots.** Its governing
verbs are `Ax*` (*akhadha*, took — 4:1:1) and `$hd` (*ashhada*, made
witness — 10:1:1). The covenant-family lexeme closest to it in frame is
`m~iyva`q`, but that word does not appear in the verse. Q 7:172 is
the Quran's foundational covenant-event yet is linguistically
**outside the covenant vocabulary**. Classical exegesis (al-Rāzī's
*Mafātīḥ al-Ghayb* ad loc., Ibn Taymiyya in *Darʾ Taʿāruḍ*) treats
7:172 as the universal `mīthāq`, but the word `mīthāq` is supplied by
the tradition, not by the verse itself. This is consistent with the
observation that the rest of the Quran's "first-covenant" lexical
cluster — `banī Ādam`, `dhurriyya`, `ashhada `alā anfusihim` — is
distinct from the later `ʿahd/mīthāq` terminology.

Three other verses form the primordial-covenant intertext without using
the five roots: 2:30 (Adam as khalīfa), 15:28-33 (Adam + angels), 33:72
(*ʿaraḍnā al-amāna* — the offered trust). The **amāna** of 33:72 is the
closest semantic neighbour of the 7:172 event and again is outside the
five-root set.

## 4. The covenant-breaking formula

*alladhīna yanquḍūna ʿahd Allāh min baʿdi mīthāqihi* ("those who break
the covenant of Allah after its ratification") is the Quran's signature
covenant-violation formula. It pairs `Ehd` and `wvq` in the same clause.

Exhaustive occurrences of root `nqD` (break):

| Verse | Period | Fate / context |
|---|---|---|
| 2:27 | Medinan | "It is those who are the losers" (*al-khāsirūn*) |
| 4:155 | Medinan | Cursing, sealed hearts, disbelief |
| 5:13 | Medinan | Curse, hardened hearts, textual distortion |
| 8:56 | Medinan | No fear of Allah (precedes 8:57–58 military order) |
| 13:20 | Medinan | (positive) — *those who fulfil* and do not break |
| 13:25 | Medinan | Curse, evil abode (*sūʾ al-dār*) |
| 16:91 | Meccan | (prospective) — *do not break oaths after confirming them* |
| 16:92 | Meccan | Day-of-Resurrection reckoning |
| 94:3 | Early Meccan | (metaphorical — weighed on your back) |

**Seven non-metaphorical breakings, 5 Medinan / 2 Meccan.** The
classical "covenant formula" (2:27 + 13:25) appears verbatim in two
separate surahs — the **only instance of a complete legal formula
duplicated across surahs in my scan of the five roots** — and is one
of the strongest mutashābih-lafẓī pairs in the corpus. Its fate-clause
differs: 2:27 names *al-khāsirūn*, 13:25 names *al-laʿna* + *sūʾ al-dār*.
The structure is fixed, the sanction varies — a hallmark of parallel
formulaic revision.

## 5. Children of Israel covenant — the dense nucleus

Mapped comparison of the six core passages:

| Passage | Root | Content of covenant | Violation named | Sanction |
|---|---|---|---|---|
| 2:40 | Ehd | "Fulfil My covenant, I fulfil yours" — reciprocal formula | (preceded by 2:27 violation) | fear Me |
| 2:63 | wvq | "Take what We have given with determination" | (followed by 2:65 Sabbath-breakers → apes) | mount raised over them |
| 2:83 | wvq | Worship Allah alone + parents, relatives, orphans, needy + speak good + ṣalāh + zakāh | turned away | implicit |
| 2:84 | wvq | Do not shed blood / evict | acknowledged but broke (2:85) | humiliation + severer punishment |
| 2:93 | wvq | "Take with strength and listen" | "We heard and disobeyed" | calf worshipped into their hearts |
| 2:100 | Ehd | Every time they took a covenant, some threw it away | — | most do not believe |
| 4:154 | wvq | Tūr raised, Sabbath, gate of humility | Sabbath transgression | — |
| 4:155 | wvq | Break of covenant + disbelief in signs + killing prophets + "hearts are wrapped" | (compound) | hearts sealed |
| 5:12 | wvq | Establish ṣalāh, give zakāh, believe messengers, loan good loan → Paradise | conditional on not-disbelieving | gardens or strayed |
| 5:13 | wvq | Break → We cursed them | textual distortion + forgetting | hardened hearts, deceit |
| 5:70 | wvq | Messengers sent; some denied, some killed | denial/killing | (context: blinded & deaf) |
| 7:169 | wvq | Covenant of the Scripture: speak only truth about Allah | studied but took worldly goods | home of Hereafter lost |

Structural observation: **`wvq` dominates this cluster (10 of 12
verses).** Israel's covenant is always the *ratified* covenant
(*mīthāq*), never merely a *ʿahd*. This asymmetry is consistent across
surahs: `ʿahd` is the act; `mīthāq` is the ratification-bond; the Torah
covenant is invariantly presented as ratified, and its violation is
correspondingly grave.

A second observation: 2:63 / 2:93 / 4:154 all pair `mīthāq` with the
**raising of the Mount (Sinai)** — three occurrences of a fixed
cosmological image tied to a single covenant. See Psalm 68:8–17 / Exod
19 parallel; the trope is non-Quranic in origin but deployed
formulaically in the Medinan corpus.

## 6. waʿd Allāh — the promise-of-Allah catalog

Of the 130 verses with root `wEd`, rough content-based triage (machine-
classified on the Sahih translation, see `scratch/covenant/`):

| Category | N | Sample verses |
|---|---:|---|
| Allah promises reward / Paradise / forgiveness | 28 | 4:95, 4:122, 5:9, 9:72, 10:4, 13:31, 14:47, 22:72, 24:55, 48:29 |
| Allah promises punishment / Hell / destruction | ~25 | 7:44, 11:17, 11:45, 13:35, 15:43, 36:63, 39:20, 40:28, 46:35, 47:15 |
| Promise of Resurrection / Day of Meeting | ~15 | 3:9, 3:194, 19:75, 28:61, 38:53, 40:55, 50:20, 85:2 ("al-yawm al-mawʿūd") |
| Moses's 30+10 nights appointment | 4 | 2:51, 7:142, 20:59, 20:97 |
| Satan's false promise | 4 | 2:268, 4:120, 14:22, 17:64 |
| Polemical "bring-what-you-promise-us" | ~8 | 7:70, 7:77, 10:48, 11:32, 21:38, 27:71 |
| Battle/emigration promise (Medinan) | ~6 | 3:152, 8:7, 33:12, 33:22, 48:20 |

The `waʿd` register therefore is **overwhelmingly eschatological**:
roughly two-thirds of occurrences concern the Day of Judgment as the
day-when-the-promise-is-fulfilled. The Meccan-heavy distribution
(101/130 = 78% Meccan) matches the known Meccan apocalyptic style.

**The `mīʿād` cluster (8 occurrences across 3:9, 3:194, 8:42, 13:31,
39:20 as noun; 50:20 *al-yawm al-mawʿūd* as pasive participle) is the
grammatical link between covenant and eschatology.** `mīʿād` is formed
from the same root as `waʿd`, but its sense is *the appointed place/time
where the promise is kept*. Q 3:9 "Our Lord, surely You will gather the
people for a Day about which there is no doubt. Indeed, Allah does not
fail in His promise (al-mīʿād)" makes this explicit: the Day of
Judgment *is* the covenant-fulfillment moment. Compare Q 85:2 *al-yawm
al-mawʿūd* (passive participle) — "the Promised Day." Fulfillment of
covenant = Day of Judgment is a structural Quranic equation.

## 7. Chronological distribution — verification

The task predicted Medinan-heavy covenant language. Verified with nuance:

| Root | Meccan share | Medinan share | Verdict |
|---|---:|---:|---|
| `wEd` | 78% (101/130) | 22% | **Meccan-heavy** (contra expectation) |
| `Ehd` | 39% | 61% | Medinan-leaning |
| `wvq` | 17% | 83% | **Strongly Medinan** |
| `byE` | 9% | 91% | **Almost exclusively Medinan** |
| `Eqd` | 29% | 71% | Medinan-leaning |

The **net direction** of the theological-legal register *is* Medinan
(73/123 non-`wEd` verses = Medinan), but the single largest root
(`wEd`) is overwhelmingly Meccan. The Meccan promise-vocabulary and the
Medinan mīthāq-vocabulary are **two genetically related but
pragmatically distinct covenant idioms**. Meccan: God's unilateral
speech-act about the eschaton. Medinan: bilateral ratified agreement
about community life. The transition is itself part of the diachronic
shift from apocalyptic preaching to community charter.

7:172 is Late Meccan (Egyptian tradition) / Late Meccan (Nöldeke) —
consistent with the task framing.

## 8. The Pledge of Ridwan (bayʿat al-Ridwān) — Q 48:10, 48:18

Surah al-Fatḥ contains the Quran's only named historical pledge-event:

- **48:10** *"Indeed, those who pledge allegiance to you are actually
  pledging allegiance to Allah. The hand of Allah is over their hands.
  So he who breaks his word only breaks it to the detriment of himself.
  And he who fulfils that which he has promised (`ʿāhada ʿalayhu`) Allah
  — He will give him a great reward."*
- **48:18** *"Certainly was Allah pleased with the believers when they
  pledged allegiance to you, [O Muhammad], under the tree, and He knew
  what was in their hearts, so He sent down tranquillity (`sakīna`)
  upon them and rewarded them with an imminent conquest."*

Observations:
1. **Only event in the Quran where `bāyaʿa` is used of a specific
   historical pledge.** (60:12 — women's pledge — is a rule, not a named
   event; 48:10 and 48:18 are the same event at Ḥudaybiyya.)
2. **Triple-root concentration in 48:10.** The single verse uses `byE`
   (yubāyiʿūnaka), `Ehd` (ʿāhada ʿalayhu), and implicit `nqD` (naqaḍa).
   It is the **densest covenant-vocabulary verse in the corpus** — three
   of the five roots + the breaking-verb in 21 Arabic words.
3. **"Hand of Allah over their hands"** is a literal identity between
   horizontal (human-Prophet) and vertical (human-Allah) covenant. The
   bayʿa collapses the two planes. This is the most explicit
   christological-analogue structure in the covenant corpus: the
   Prophet's hand *is* Allah's hand at the moment of ratification.
4. Q 9:111 extends the same logic backward: *"Allah has purchased
   (*ishtarā*) from the believers their lives and their properties [in
   exchange] for Paradise... so rejoice in your transaction (*baʿaykumu*)
   which you have contracted."* Three roots again: `$ry` (purchase),
   `byE` (transaction/pledge), `Ehd` (covenant). The pledge-of-
   allegiance is re-described as a *commercial* exchange with Paradise
   as the purchased good — a transfer of the covenant frame from the
   pledge-hands at Ḥudaybiyya to the entire believer-to-God relation.

## 9. Covenant and law

Covenant is structurally *upstream* of the ḥudūd / sharīʿa / ḥukm
vocabulary. Roots `Hkm` (judgment, 210 occ), `Hdd` (limits/ḥudūd, 25
occ), and `$rE` (sharaʿa / sharīʿa, 5 occ including 5:48, 42:13, 42:21,
45:18) are the primary law-terms. Verses that explicitly pair covenant
and law:

- **5:1** opens *"O you who have believed, fulfil [all] contracts
  (awfū bi-l-ʿuqūd)"* — the sole plural `ʿuqūd` in the Quran, and it
  is the opening verse of the Quran's most legally dense surah
  (al-Māʾida). Immediately followed by dietary law, then 5:7 recalls
  the covenant with believers, then 5:12–13 recalls the mīthāq of
  Israel, then 5:38 is the theft ḥadd, then 5:44–50 on divine
  judgment (ḥukm), then 5:48 *sharʿatan wa-minhājan*. Al-Māʾida
  therefore reads as a **single structural argument**: covenant →
  community duties → ḥudūd → sharīʿa. Covenant is the axiom; law is
  derived.

- **2:27 / 13:25**: covenant-breaking is described as **"severing that
  which Allah has ordered to be joined" (*yaqṭaʿūna mā amara Allāh bihi
  an yūṣala*)** — the same verb (`qṭʿ`) used in the theft-ḥadd of 5:38.
  Covenant-breaking is conceptually a juridical cut.

- **16:91** "Do not break oaths (`aymān`) after their ratification
  (`tawkīd`) while you have made Allah, over you, a witness" — three
  covenant-family terms (`wafā'u bi-ʿahd`, `aymān`, `tawkīd`) pile up
  in one verse, with the divine witness clause making the oath
  actionable.

- **5:89**: expiation (`kaffāra`) for broken oaths (`ayman ʿaqqadtum`) —
  the only explicit covenant-breaking → ritual expiation conversion in
  the corpus. Covenant violation has a **legal remedy built into the
  covenant system itself**.

The relation: **every ḥadd presupposes a covenant.** 5:1 is its
declaration. Covenant is the frame; law is the content.

## 10. "You took a covenant from Our Messenger" — Q 3:187

*"And [mention, O Muhammad], when Allah took a covenant from those who
were given the Scripture, [saying], 'You must make it clear to the
people and not conceal it.' But they threw it away behind their
backs..."*

The standard reading: the covenant is from **People of the Scripture**
(the preceding context is about the Book). But the classical
*iltifāt*-sensitive readings (al-Rāzī, Ibn ʿAṭiyya) note that the
formula *"Allah took a covenant from those given the Book"* in 3:187
forms a triptych with:

- **3:81** — covenant of *the prophets* to support every messenger
  confirming what they have (*mīthāq al-nabiyyīn*)
- **33:7** — covenant of prophets named in sequence: Muhammad, Noah,
  Abraham, Moses, Jesus — *mīthāqan ghalīẓā* (a solemn covenant)

Read together, 3:81 + 3:187 + 33:7 suggest a three-way covenant-chain:
(i) God takes covenant from the prophets to preach; (ii) the prophets
take covenant from their communities to believe; (iii) the communities
(People of the Book in 3:187) take covenant to **make clear** the
Scripture. Muhammad appears by name only in 33:7 (consistent with
`chronological-revelation.md` §10: the proper name "Muḥammad" is
post-Hijra only, and 33:7 is position 90). The covenant from the
Messenger is therefore inside a Medinan triptych that retrospectively
names the Prophet for the first time in this register.

`mīthāqan ghalīẓā` ("solemn covenant") appears **three times** in the
Quran — 4:21, 4:154, 33:7 — two Torah-covenant contexts and one
all-prophets context. The marriage covenant of 4:21 uses the same
phrase as the Sinai covenant. This is a deliberate intertext: marriage
is cast as a sacramental analogue of the Sinai covenant.

## 11. Covenant and eschatology

Summary of the link surfaces:

| Lexeme | N | Eschatological role |
|---|---:|---|
| `waʿd Allāh` (Allah's promise) | ≥15 | The divine guarantee of Resurrection / Judgment |
| `mīʿād` (appointed meeting) | 5 | Day of Judgment as *al-mīʿād* (3:9, 3:194, 13:31, 39:20, 8:42) |
| `mawʿid` (appointed time/place) | 12 | 18:58, 20:58, 34:30 etc. |
| `al-yawm al-mawʿūd` | 1 | 85:2 — "the Promised Day" |
| `waʿīd` (threat) | 6 | 14:14, 20:113, 50:14, 50:20, 50:28, 50:45 |

Four out of six `waʿīd` occurrences are in Surah Qāf (50), where the
surah's refrain ties together covenant-breaking, the Day, and the
threat-promise. Q 50:20 *"And the Horn will be blown — that is the Day
of Threat (`yawmu al-waʿīd`)"* — the Day is literally named *the
waʿīd-day*. Covenant-fulfillment and covenant-threat converge on one
eschatological event: **the yawm al-wāqiʿa is the yawm al-mīʿād is the
yawm al-waʿīd**. One day, three names, one root (`wEd`) for the last two.

## 12. Classical prior art

- **al-Rāzī, *Mafātīḥ al-Ghayb*, ad Q 7:172**: the foundational
  commentary reading. Rāzī treats the verse as the universal `mīthāq`
  (despite the word not appearing) and argues for *fiṭra*-style innate
  theism grounded in a pre-eternal witnessing. The *Tafsīr al-Kabīr*
  devotes ~40 folio pages to this single verse.
- **Ibn Taymiyya, *Darʾ Taʿāruḍ al-ʿAql wa-l-Naql* III.275ff.** and the
  *Majmūʿ al-Fatāwā*: argues that the covenant of 7:172 is not an
  actual pre-existent event but a description of the in-created *fiṭra*
  — a notable dissent from Rāzī.
- **Ibn ʿAṭāʾillāh al-Iskandarī, *al-Ḥikam* (especially hikma ~4 and
  ~180)**: the spiritual-covenant reading — the servant's *ʿahd* with
  God is renewed in every moment of remembrance; the breaking of the
  covenant is merely forgetting.
- **al-Bāqillānī, *al-Tamhīd***: juridical readings of 5:1 (fulfil
  contracts) as the principle that *all* obligations — ritual, civil,
  political — are legally `ʿuqūd` and therefore enforceable.
- **Ibn Kathīr ad Q 48:10**: bayʿat al-Ridwān under the tree at
  Ḥudaybiyya; traditional narrative basis.
- Modern: **Wadad Kadi (el-Qadi), "The Primordial Covenant and Human
  History in the Qurʾān," *Proceedings of the American Philosophical
  Society* 147.4 (2003), 332–338** — the most-cited English treatment
  of Q 7:172. Kadi argues the primordial covenant is the *hermeneutic
  key* to Quranic history: all subsequent covenants repeat and refer
  back to it.

## 13. Novel observations worth flagging

1. **`waʿd` vs `mīthāq` split is genuinely diachronic** — Meccan
   eschatological register vs Medinan community-legal register.
   Nöldeke-phase counts are lopsided enough (8/52/44/26 vs 1/0/6/22)
   that this should be treatable as a quantitative claim.
2. **Q 7:172 lies outside the five-root covenant vocabulary.** The
   foundational covenant is lexically distinct from its descendants.
3. **Q 48:10 is the highest-density covenant verse in the corpus**
   (three of five roots + `nqD` breaking-verb).
4. **`mīthāqan ghalīẓā` triptych** (4:21, 4:154, 33:7) ties marriage,
   Sinai, and all-prophets with a single fixed phrase — a structural
   signal that the *same covenant-grammar* governs all three.
5. **The 2:27 / 13:25 doublet** is one of the strongest
   mutashābih-lafẓī pairs in the Quran; its sanction-clause varies
   while the opening formula is fixed.
6. **"Fulfilment of covenant = Day of Judgment"** collapses across
   three root-derivatives: `mīʿād`, `mawʿūd`, `waʿīd`. The eschaton
   *is* the covenant-moment.
7. **Surah 5 (al-Māʾida) reads as a covenant-to-law syllogism** across
   5:1 → 5:7 → 5:12–13 → 5:38 → 5:44–50 → 5:48.

## 14. Pre-registration status

Not pre-registered. Exhaustive root-extraction from QAC is deterministic
(no degrees of freedom in the set of verses). The period-counts and
Nöldeke phase-counts are descriptive. Claims (1)–(3) and (7) above are
candidates for Phase-C pre-registration with 1.5-permutation tests on
period labels.

## 15. Data artifacts

- `scratch/covenant/root-{Ehd,wEd,wvq,byE,Eqd}.tsv` — per-root
  location + lemma + form tables.
- `scratch/covenant/verse-lists.txt` — plain lists by root.
- `scratch/covenant/covenant-verses-full.txt` — full Sahih text for
  every covenant-verse, annotated with Meccan/Medinan period.
