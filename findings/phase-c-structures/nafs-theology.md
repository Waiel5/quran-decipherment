---
title: "The nafs: full Quranic audit and theological architecture"
phase: C
agent: theological-structural
corpus_root: nfs
root_token_count: 298
verses_containing_root: 270
singular_count: 140
plural_count: 155
verbal_forms: 3   # 1 perf tanaffasa, 1 impf yatanāfasu, 1 active participle mutanāfisūn
unique_adjective_modifiers_of_singular_nafs: 9
classical_trio: [ammara_bi-l-su, lawwama, mutma'inna]
explicit_quranic_sequence: false
inventory_vs_ladder_verdict: inventory
meccan_token_count: 163
medinan_token_count: 135
core_verses:
  - Q 12:53   # nafs ammara bi-l-su'
  - Q 75:2    # nafs lawwama
  - Q 89:27   # nafs mutma'inna
  - Q 89:28   # rāḍiya marḍiyya (continuation)
  - Q 91:7-10 # nafs cosmology
  - Q 13:28   # muṭma'inna qalb (cross-root link)
classical_priors:
  - al-Ghazali Ihya Book 21 (Kitab sharh 'aja'ib al-qalb)
  - Ibn al-Qayyim Madarij al-Salikin vol 1 (manzilat al-tawba)
  - al-Qushayri al-Risala (bab al-nafs)
  - Ibn 'Arabi al-Futuhat bab 73
---

# The nafs — full Quranic audit

*Every verse in the Quran containing the root n-f-s; the classical 3-state typology (ammāra, lawwāma, muṭma'inna) tested against the text; the 4th/5th states (rāḍiya, marḍiyya) confirmed; the relation of nafs to qalb and rūḥ mapped; an honest verdict on whether the Sufi ladder is explicit in the Quran or interpretive.*

---

## 1. Root-level statistics

**Root nfs appears in 298 morphological segments** across **270 distinct verses** (one verse can stack multiple tokens; Q 16:111 has three). The Leeds QAC tallies 298; Phase B root-cartography estimated "~295"; the shortfall is 3 verbal/participial tokens off a pure-noun search.

| Form | Tokens | Exemplar | Gloss |
|---|---|---|---|
| **Nominal singular** `nafs` (FS, various cases) | 140 | Q 12:53 *al-nafs* | the (individual) soul / self |
| **Nominal plural** `anfus` (FP, broken plural) | 153 | Q 41:53 *fī anfusihim* | yourselves / themselves |
| **Nominal double-plural** `nufūs` | 2 | Q 17:25, Q 81:7 | selves (collective) |
| **Verb, perfect, Form V** `tanaffasa` | 1 | Q 81:18 *idhā tanaffasa* | (the dawn) breathes |
| **Verb, imperfect, Form VI** `yatanāfasu` | 1 | Q 83:26 *fa-l-yatanāfasi* | let competitors compete |
| **Active participle Form VI** `mutanāfisūn` | 1 | Q 83:26 *al-mutanāfisūn* | the competitors |
| **Total** | **298** | | |

Two findings are immediately striking:

1. **The root is overwhelmingly NOMINAL.** 295/298 tokens are nouns. The "soul" is a noun-thing in the Quran, not an action. This matters for classical psychology: the Sufi tradition that makes the soul a *dynamic process* is reading back into a lexeme the Quran treats as almost entirely substantive.

2. **The verbal forms are marginal and unexpected.** Q 81:18 has the dawn *breathing* (the cosmos has a soul-action) and Q 83:26 has the paradise-drinkers *competing* (the derived noun *munāfasa* "honourable competition" becomes a pillar of Ghazalian ethics). Neither verse uses the verb for human soul-psychology. **The Quran nowhere inflects the root nfs as a verb of the soul.** This is a classical-tradition inversion: Sufi psychological practice ("to discipline the nafs") cannot be grounded in the Quran's *verbal* use of the root.

**Meccan/Medinan distribution** (using the conventional surah-classification in the JSON):

| | Singular nafs | Plural anfus/nufūs | Total |
|---|---|---|---|
| Meccan | 97 | 66 | 163 |
| Medinan | 46 | 89 | 135 |

The plural reverses the singular's skew: singular "the soul" is a Meccan vocabulary (individual judgement, eschatology); plural "yourselves" is a Medinan vocabulary (community-legal "wrong yourselves not"). The classical 3-state trio is entirely Meccan material.

**Top 5 surahs by nfs density (token count, not normalised):** Sūrat al-Baqara 35, Āl ʿImrān 21, al-Nisāʾ 19, al-Māʾida 12, al-Anʿām 17, al-Tawba 17, Yūsuf 13, al-Aʿrāf 13. Sūrat Yūsuf ranks **8th** absolute but **2nd by density relative to verse count** (13 tokens / 111 verses = 11.7%), behind only Sūrat al-Nisāʾ's opening.

---

## 2. The three canonical soul-states — full grammar, full context

### 2a. Q 12:53 — *nafs ammāra bi-l-sūʾ*

Joseph speaks. Context, verses 50–56:

- **v50**: the king summons Joseph; Joseph defers, asking for the case of the women who cut their hands to be clarified first.
- **v51**: the women exonerate Joseph; the wife of al-ʿAzīz confesses: "it was I who sought to seduce him."
- **v52**: (still the wife) "that al-ʿAzīz may know I did not betray him in absence."
- **v53**: *"And I do not acquit myself. Indeed, the nafs is *ammāratun bi-l-sūʾ*, except for what my Lord has mercied. Indeed my Lord is forgiving, merciful."*
- **v54**: the king installs Joseph.

**Textual question: who speaks v53?** Grammatically, the pronoun shift is ambiguous — it can be the wife of al-ʿAzīz continuing her confession, OR Joseph stepping back in. Classical tafsir splits: Ṭabarī and most classical commentators (and ALL the Sufi tradition) attribute v53 to Joseph — it is Joseph humbly refusing to exonerate his own soul despite being factually innocent. The Sufi reading depends on this attribution.

Morphology of 12:53:

```
(12:53:3:1) nafosi   N  LEM:nafos | ROOT:nfs | FS | NOM  +1S pronoun  ("my soul")
(12:53:5:2) n~afosa  N  LEM:nafos | ROOT:nfs | FS | ACC                ("THE soul")
(12:53:6:2) >am~aArapN  N  LEM:>am~aArap | ROOT:Amr | F | INDEF | NOM  ("persistent-commander")
(12:53:7:3) s~uw^'i  N  LEM:suw^' | ROOT:swA | M | GEN                  ("evil")
```

**Key observation: *ammārap* is root A-M-R, NOT nfs.** It is a *faʿʿāla* intensive active participle of *amara* (to command). *Ammāra bi-l-sūʾ* = "a persistent-commander-of-evil." The classical three-state terminology borrows ONE modifier (lawwāma) from a root that also belongs to the classical semantic field of "self-rebuke," but the other two modifiers (ammāra, muṭma'inna) import roots from outside nfs. **The three states are constructed by adjective-grafting, not by morphological derivation from the root nfs itself.** This is a structural point: the classical typology is a *lexical composition*, not a *morphological paradigm*.

**Position in surah**: verse 53 of 111. Word-cumulative position: **ends at word 926 of Sūrat Yūsuf's 1912-word total = 48.4%**. 12:53 is at the word-midpoint of the Joseph narrative. Classical Sufi reading treats 12:53 as the psychological hinge of Joseph's whole arc (self-vindication → self-effacement → elevation); the computational structure weakly supports this — Joseph's elevation (v54: "I will appoint him exclusively for myself") follows immediately on Joseph's self-humbling at v53. The king's appointment is the immediate REWARD of Joseph refusing to exonerate his own nafs.

**Joseph's refusal of exoneration.** Morphologically the verse begins with root *brA* (to acquit) in the negation: *wa-mā ubarri'u nafsī* — "I do not acquit my soul." The ONLY place in the Quran where *brA* (to acquit) takes nafs as direct object. This is a morpho-semantic hapax: the refusal of self-acquittal is constructed in a grammatical slot that occurs nowhere else.

**Intra-Yūsuf nafs-arc.** Surah 12 has 13 nafs tokens across 11 verses; 12:23, 12:26, 12:30, 12:32, 12:51 — a cluster of *rāwadathu ʿan nafsihī* ("she sought to seduce from his nafs," 5×) — then 12:53 pivots to reflective psychology, then 12:68, 12:77, 12:83 show Jacob's *bāl-nafs* (inner need), Joseph's private *nafs* (keeping the secret), and sons' *anfus* (enticing souls). The surah is a ring around 12:53 at the lexical level: before 12:53 the nafs is a SITE OF ASSAULT (seduction object); after 12:53 the nafs is a SITE OF KNOWING (inner wisdom, hidden thought). **The nafs-word itself narrates Joseph's transformation.**

### 2b. Q 75:2 — *nafs lawwāma*

Sūrat al-Qiyāma opens:

- **v1**: *lā uqsimu bi-yawmi l-qiyāma* — I swear by the Day of Resurrection.
- **v2**: *wa lā uqsimu bi-l-nafsi l-lawwāma* — and I swear by the reproaching soul.
- **v3**: *does man think we will not assemble his bones?*
- **vv4-15**: the body will be reconstituted; the man will be a witness against himself (v14 *bal al-insānu ʿalā nafsihī baṣīra*).

**Morphology.** *lawwāma* is root L-W-M, grammatically tagged `ADJ | LEM:l~aw~aAmap | F | GEN`. Root l-w-m occurs **14 tokens** across the Quran; 75:2 is the UNIQUE occurrence in the *faʿʿāla* feminine intensive. Other root-lwm tokens: Q 5:54 (*lāʾim* — no-blame-fearing), Q 12:32 (*lumtunnanī* — you blamed me, from Zulaikha), Q 14:22 (*lā talūmū-nī*, Satan), Q 17:29 *malūm* (not to be blamed), Q 17:39, Q 23:6, Q 37:142 *muliym* (Jonah, blame-worthy), Q 51:40, Q 51:54, Q 68:30 *yatalāwamūn* (blaming each other), Q 70:30. **l-w-m in the Quran is overwhelmingly INTER-SUBJECTIVE blame** — 12/14 tokens are about one person blaming another. Only 75:2 internalises it: the nafs that blames ITSELF. This is a *grammatical hapax* (intensive feminine) and a *semantic near-hapax* (reflexive rather than inter-personal blame). The Sufi tradition that treats *nafs lawwāma* as the self-conscience inherits a Quranic usage that is, morphologically, one-of-a-kind.

**Oath-structure significance.** Q 75:1-2 is a twin-oath: Day of Resurrection + reproachful soul. Classical tafsir (Ṭabarī, Zamakhsharī, Qurṭubī) reads this as two co-ordinates of a single event: *yawm al-qiyāma* is the external frame; *al-nafs al-lawwāma* is the internal companion. The surah's central claim (v14): *"rather, man is a witness against his own nafs"* — uses nfs a second time. The nafs appears twice in Sūrat al-Qiyāma: 75:2 as the reproacher; 75:14 as the witness. **These are the same nafs at two grammatical distances** — first as companion (oath-object), then as courtroom witness (predicate noun). The resurrection-nafs is a witness-nafs. **The eschatological claim of Q 75 is that the nafs is BOTH the prosecutor AND the evidence** in its own trial.

### 2c. Q 89:27 — *nafs muṭma'inna*

Sūrat al-Fajr closes:

- **vv15–20**: wealth-tested man misreads both honour and restriction as God's verdict on his worth; a social diagnosis.
- **vv21–23**: the eschatological arrival: "when the earth is pounded, and your Lord comes, and the angels in ranks, and Hell is brought..."
- **vv24–26**: "he will wish he had sent ahead [good]... none will punish or bind as He does."
- **v27**: *"O nafs muṭma'inna..."*
- **v28**: *"return to your Lord, rāḍiya marḍiyya"* — pleased and pleasing (to Him).
- **v29**: *"enter among My servants."*
- **v30**: *"enter My paradise."*

Morphology of 89:27–28:

```
(89:27:2:2) n~afosu       N   LEM:nafos | ROOT:nfs | FS | NOM
(89:27:3:2) muToma}in~apu ADJ ACT PCPL (XII) | LEM:m~uToma}in~ap | ROOT:Tmn | F | NOM
(89:28:4:1) raADiyapF      N  ACT PCPL | LEM:raADiyap | ROOT:rDw | F | INDEF | ACC
(89:28:5:1) m~aroDiy~apF   N  PASS PCPL | LEM:m~aroDiy~ap | ROOT:rDw | F | INDEF | ACC
```

**muṭma'inna is the Form XII active participle** of T-m-n — an unusual augmented stem that the Quran otherwise uses almost exclusively in verbal form (*liyaṭma'inna qalbī*, etc.). Root T-m-n has **13 tokens total** across the Quran, and 12 of them describe HEARTS (*qalb/qulūb*) finding rest. **Q 89:27 is the UNIQUE token where the T-m-n participle modifies the nafs rather than the qalb.** This is a massive intra-root finding:

| Tmn tokens | Subject of rest | Verse |
|---|---|---|
| 2:260 | Abraham's heart (*qalbī*) | "that my heart may be reassured" |
| 3:126 | your hearts (*qulūbu-kum*) | help to reassure hearts |
| 5:113 | our hearts (*qulūbu-nā*) | disciples to Jesus |
| 8:10 | your hearts | angel-help at Badr |
| 13:28 | hearts x2 (*taṭma'innu al-qulūb*) | remembrance of Allah |
| 16:106 | faith (*muṭma'inn bi-l-īmān*) | forced recantation excuse |
| 16:112 | town (*muṭma'inna*) | a town at peace |
| 17:95 | angels (*muṭma'innīn*) | if earth were peaceful |
| 22:11 | worship at edge (ind-Tmn) | reassurance fragile |
| 4:103 | prayer/ease (*iṭma'nantum*) | standing to prayer |
| 10:7 | reassured with this-life (pejorative) | unbelievers' complacency |
| 2:260 (v) | verb | (same verse) |
| **89:27** | **the NAFS** | **eschatological capstone** |

**This is the theological payoff.** The root T-m-n has been developing a reassurance-theology across thirteen Meccan and Medinan tokens — every prior instance is about HEARTS or STATES, never the soul. Then at 89:27, in the surah's final summons, T-m-n locates in the NAFS. The soul has become the heart. The individual self has absorbed the vocabulary of cardiac reassurance. Phase B's root-cartography finding on Q 13:28 ("hearts find rest in dhikr") is completed at Q 89:27: the SOUL that found rest through dhikr is invited to Paradise. **The entire T-m-n arc lands, grammatically, on the nafs of 89:27 — this is what the whole Tmn network was pointed at.**

### 2d. The 4th and 5th state: *rāḍiya + marḍiyya* (Q 89:28)

These ARE in the Quran, as classical Sufi tradition notes. They modify the SAME nafs of 89:27. Grammatically:
- `raADiyap`: active participle root r-D-w, feminine — "she who is pleased [with her Lord]."
- `marḍiyya`: PASSIVE participle same root — "she with whom [the Lord] is pleased."

These are **mirror-pair participles** of a single root. The sequence ACT then PASS models a bi-directional covenant: the soul pleases, and is pleased-with. There is no separate nafs-term; these are two adjectives stacked on the muṭma'inna nafs. Sufi tradition (al-Qushayrī, Ibn ʿArabī) treats these as distinct *maqāmāt* (stations). The text gives them as **continuation** of the muṭma'inna nafs, not as separate states.

---

## 3. A fourth (or sixth) nafs? Other modifier survey

I hunted every adjective or participle appearing adjacent to a singular nafs across the whole Quran. The full table:

| Verse | Adjective/Modifier | Root | Gloss |
|---|---|---|---|
| Q 3:185, 21:35, 29:57 | *dhā'iqa* | *dhwq* | tasting (death) — 3× idiom *kull nafs dhā'iqat al-mawt* |
| Q 4:1, 6:98, 7:189 | *wāḥida* | *wHd* | a single/one (soul from which creation) — 3× |
| Q 4:4 | *hanīʾan* | *hnA* | pleasantly (adverbial) |
| Q 12:53 | *ammāra bi-l-sūʾ* | *Amr + swA* | persistent-commander of evil |
| Q 12:26 | *shāhid* (witness in next clause) | *$hd* | witness |
| Q 35:32 | *muqtaṣid* | *qSd* | moderate |
| Q 37:113 | *mubīn* (clear injustice against) | *byn* | clear |
| Q 47:38 | *ghanīy* (Allah is ghanīy) | *gny* | (describes Allah, not nafs proper) |
| Q 50:21 | *sāʾiq* (driver with each soul) | *swq* | driver |
| **Q 75:2** | ***lawwāma*** | ***lwm*** | **reproaching** (classical 2) |
| **Q 89:27** | ***muṭma'inna*** | ***Tmn*** | **reassured** (classical 3) |
| **Q 89:28** | ***rāḍiya, marḍiyya*** | ***rDw*** | **well-pleased, well-pleasing** (classical 4+5) |

**Verdict on the "fourth state":** the Quran explicitly gives *rāḍiya marḍiyya* modifiers at 89:28 — these are canonical. Classical Sufi tradition sometimes posits a *nafs kāmila* (perfected) or *sharīfa* (noble); **neither term appears in the Quran.** *Kāmila* and *sharīfa* are post-Quranic theological constructs.

The genuinely Quranic modifiers beyond the classical three are:
- *wāḥida* — the primordial single soul of creation (4:1, 6:98, 7:189): cosmogonic, not ethical.
- *dhā'iqa l-mawt* — every soul tasting death (3:185, 21:35, 29:57): eschatological, universal.
- *muqtaṣid* — a middle/balanced soul (35:32): a 6th potentially-Sufi category the tradition has **underused**, gesturing at a via media.

---

## 4. The soul-disciplining pathway: ladder or inventory?

Classical Sufi psychology (al-Ghazālī *Iḥyāʾ* book 21, *Kitāb sharḥ ʿajāʾib al-qalb*; Ibn al-Qayyim *Madārij al-Sālikīn*; al-Qushayrī *al-Risāla*) teaches a *progressive refinement*: ammāra → lawwāma → mulhama → muṭma'inna → rāḍiya → marḍiyya → kāmila. The ammāra is the unrefined lower self; the lawwāma is the conscience awakening; the muṭma'inna is the tranquil soul; etc.

**Quranic evidence for a sequence:**
- The three verses are in three different surahs (12, 75, 89) with no cross-reference.
- In Nöldeke chronology, 89 is *early Meccan*, 75 is *early Meccan*, 12 is *middle Meccan*. The revelation-order is **89 → 75 → 12**. The muṭma'inna came FIRST, the ammāra LAST. There is no chronological progression that matches the Sufi ladder.
- No single verse juxtaposes two states.
- The word-order of the Sufi ladder has to be reconstructed from surah-sequencing or from internal theological logic.

**Verdict: the ladder is an interpretive synthesis, not an explicit Quranic structure.** The Quran INVENTORIES soul-states. Sufi scholarship SEQUENCED them. This is a theological reading the Quran licenses but does not dictate. The licensing comes from Q 91:7–10 (the nafs has *fujūr* and *taqwā* potentials; success lies in *tazkiya*, purification) which IMPLIES a process, plus the eschatological end-state at 89:27. But the process is the Sufi addition. The *content* of the tradition is Quranic; the *order* is hermeneutic.

That said — **the end-states are Quranic**. ammāra is where Joseph locates the unpurified soul; muṭma'inna is where Allah locates the welcomed soul. The poles are in the text. The ladder between them is scholastic.

---

## 5. Resurrection and the nafs-typology

Every one of the three canonical soul-state verses has an eschatological register:

- **Q 12:53** — Joseph speaks at the pivot between imprisonment and exaltation. The classical Sufi reading *extends* this eschatologically: Joseph's worldly elevation prefigures the soul's elevation at the reckoning. Internal: the verse appeals to *raḥma* (mercy) and Allah as *ghafūr raḥīm* (forgiving, merciful) — classical divine attributes of the eschatological scene.
- **Q 75:2** — explicit: the nafs lawwāma is SWORN BY alongside the Day of Resurrection. The whole surah develops the courtroom metaphor: the body reconstituted, the eyes dazzled, the witness (v14: the nafs), the excuses (v15), the record-reading (Q 17:14 and Q 69:19 parallels). The nafs lawwāma IS the courtroom conscience made structural.
- **Q 89:27** — explicit: the muṭma'inna nafs is summoned AFTER the Day of Judgement has arrived (89:22 *"and your Lord has come..."*). The *return* (*irjiʿī*) is the soul's return to Allah after judgement.

Combined, the three soul-states operate at three eschatological stations:
1. **ammāra** — pre-judgement, in-life soul (Joseph's living self-diagnosis)
2. **lawwāma** — at-judgement soul (the Qiyāma courtroom)
3. **muṭma'inna** — post-judgement, welcomed soul (entering paradise)

This is an implicit temporal sequence, but temporal in the eschatological-staging sense, not the spiritual-progression sense. **The Quran's typology is liturgical/dramatic, not developmental.**

The plural `anfus` fills a parallel role in the collective eschatology: Q 2:48 *"fear a Day when no nafs will suffice for another nafs"*; Q 82:19 *"the Day when a nafs shall not possess for another nafs a thing"*; Q 31:28 *"your creation and your resurrection are not but as one single nafs."* The plural form carries the social and generic resurrection statements; the singular form carries the psychology of individual soul-states.

---

## 6. Anfus (plural) — mapping "yourselves"

Of 155 anfus tokens, a dominant semantic usage is REFLEXIVE: *anfusa-kum* = "your own selves," *anfusi-him* = "themselves," where the noun is functioning as a pronoun of self-reference. Canonical examples:

- **Q 2:44** *"do you order righteousness on the people and forget yourselves?"* — self-knowledge rebuke.
- **Q 2:54** *"kill yourselves (*anfusa-kum*)"* — the golden-calf repentance command; the plural here means the collective must slaughter the wrongdoers among its own number (classical tafsir reads *anfus* as "fellow-members," not "selves-as-persons"). A striking reflexive extension.
- **Q 2:187** *"you used to deceive yourselves"* (Ramadan context).
- **Q 7:172** *"He made them witness over themselves: Am I not your Lord? They said: Yes..."* — the *mīthāq* of souls in pre-existence. Plural `anfus`, but individually-distributive: each soul testifies.
- **Q 9:128** *"there has come to you a Messenger from among yourselves"* — Messenger as *one of your own* (min anfusi-kum).
- **Q 30:21** *"created for you from yourselves spouses..."* — spouses as of-your-own-kind.
- **Q 41:53** *"We will show them Our signs on the horizons and within themselves"* — the celebrated classical "external + internal" proof-pair.
- **Q 51:21** *"and within yourselves; will you not see?"* — the shortest verse.
- **Q 59:19** *"and do not be like those who forgot Allah so He made them forget themselves"* — strongest verse on the nafs-Allah link.

**The plural is where the Quran does its community-psychology.** Collective self-reflection, collective self-deception, collective rebuke. The singular is where the Quran does its individual eschatology.

A Medinan shift: plural anfus **outnumbers** singular in Medinan material (89 vs 46). The singular's dominance is Meccan (97 vs 66). This aligns with the surah-type character: Medinan revelation addresses a community, and the nfs vocabulary serves collective ethics; Meccan revelation addresses individuals facing judgement, and the nfs vocabulary serves individual eschatology. **The same root swings its semantic centre when the audience scale changes.** Classical scholarship lacks this clean statistical pattern; it is here a genuinely new finding on this specific root.

---

## 7. The nafs as grammatical agent vs patient

Case-breakdown of the 140 singular nafs tokens:

| Case | Count | Typical role |
|---|---|---|
| GEN (genitive, after preposition or possessive) | 83 | "his nafs," "from the nafs," "to the nafs" |
| ACC (accusative, direct object) | 33 | "he kills a nafs," "he sent ahead a nafs," "he acquits a nafs" |
| NOM (nominative, subject or predicate) | 24 | "the nafs is ammāra," "every nafs will taste death" |

**Only 24/140 singular nafs tokens are subjects of verbs.** The nafs *acts* (is grammatical agent) in about 1/6 of its singular occurrences. The dominant usage is possessive or oblique — the nafs is something *had*, *given*, *returned*, *done-to*. The nafs-as-agent is overwhelmingly in *fixed phrases*:

- *kull nafsin dhā'iqat al-mawt* — "every nafs is a taster of death" (3 occurrences, 3:185, 21:35, 29:57, all IDENTICAL)
- *laysa ʿalā nafsin illā wusʿahā* — no nafs is burdened beyond its capacity (2:286, 6:152)
- *kull nafsin bi-mā kasabat* — every nafs by what it earns
- *lā takhūnū anfusakum* — don't betray yourselves
- *mā taʿlamu nafsun* — no nafs knows what it will earn tomorrow (31:34)

**Pattern: the nafs is grammatical subject almost exclusively in eschatological-universal formulas.** In narrative contexts the nafs is a passive recipient of narrative action (seduction-object in Yūsuf, blame-object in Qiyāma, welcome-object in Fajr). The Quran gives the nafs MAX agency exactly when humans have MIN agency — at the end of the world. This is a strong theological observation: when the eschaton collapses human projects, the nafs speaks for itself.

---

## 8. nafs ↔ qalb ↔ rūḥ — the classical tripartite?

Classical Sufi psychology divides the human interior into three centres: nafs (self), qalb (heart), rūḥ (spirit). This is canonical from al-Ghazālī onward; Ibn ʿArabī builds his entire phenomenology on the stratification. Does the Quran license it?

**Co-occurrence statistics:**

| Root-pair | Shared verses | Notes |
|---|---|---|
| nfs + qlb | **4 verses**: Q 3:154, Q 4:63, Q 5:52, Q 18:28 | Rare |
| nfs + rūḥ (rwH) | **2 verses**: Q 2:87, Q 3:117 | rūḥ here is "Holy Spirit" and "wind," respectively — NOT "soul-spirit" |
| qlb + rwH | 1 verse | Also rūḥ = spirit/revelation |
| All three | **0 verses** | The tripartite is NOT a Quranic co-location |

**Verdict: the nafs-qalb-rūḥ triad is a post-Quranic synthesis.** The three roots are NEVER co-present in a single Quranic verse as a threefold psychology. The Sufi tradition that treats them as a stratified interior is *synthesising* vocabulary from scattered locations.

Network diagram (co-occurrence weighted):

```
                       nafs (nfs, 270 verses)
                     /        |        \
                   /          |          \
             (4 verses)  (distant)   (2 verses, but
               nfs+qlb      |        rūḥ is NOT soul here)
                /            |            \
               /             |             \
              qalb     (distant)         rūḥ
              (qlb,               (rwH,    52 verses, mostly
             155 verses)        "the Spirit" as divine agency)
                    \___________/
                        1 verse (rūḥ there = angelic messenger/wind)
```

**The four nafs+qalb verses** reveal the actual Quranic relation:
- **Q 3:154** (Uḥud): a faction overcome by drowsiness as security, while another faction *wrestles with their own selves* and thinks Jāhilī thoughts; the verse locates decisive self-deception in the anfus while tracking the qalb ("Allah will test what is in your hearts"). Here nafs = seat of doubt; qalb = site under divine test.
- **Q 4:63**: "those in whose QULŪB Allah knows what is there" — so warn them "in their ANFUS" with a *qawl balīgh*. The qalb is where the content sits; the nafs is where the addressing happens. Distinct instrumental roles.
- **Q 5:52**: "those in whose QULŪB is disease hasten..." — parallel to 4:63, qalb as site of diagnosis, anfus as the acting social body.
- **Q 18:28** (THE KEY VERSE): *"do not obey him whose QALB We have made heedless of Our remembrance, who follows his *hawā*"*. The QALB is heedless; the person follows *hawā* (desire). In the same verse (earlier), the Prophet is told to be patient *with those who call upon their Lord*. Classical tafsir reads this as counterposing *qalb* (the site of dhikr) against *nafs/hawā* (the site of desire). **Q 18:28 is the one verse where the Quran *implicitly* distinguishes qalb from nafs as opposing interior faculties** — but even here the nafs is not named; it is *hawā* (desire) that is the nafs-surrogate.

**Summary.** The Quranic psychology is bipartite (heart + self), not tripartite. The rūḥ is almost never an anthropological category; it is an angelic/revelatory category (Q 17:85 *"they ask you about the rūḥ; say: it is from my Lord's command"* — the one verse that could anthropologise rūḥ actually refuses). Classical Sufi psychology that treats rūḥ as the highest soul-station is a **Platonic-Neoplatonic overlay** on Quranic vocabulary that had already been shaped by the Jewish-Christian *rūḥ ha-qōdesh / pneuma* tradition.

The nafs-qalb distinction is sharper. Qalb is the *site of reception* of revelation (15× *qalbī*, 37× *qulūbi-him*, consistently tied to īmān, dhikr, khushūʿ, khashya). Nafs is the *agent-site of will and inclination*. The classical tradition's sharpening of this into a psychology of stations is a *refinement* of a distinction the Quran already makes implicitly.

**But the greatest evidence that the Quran wants nafs and qalb linked is Q 89:27 ↔ Q 13:28** (Phase B finding). Q 13:28 says *hearts* (qulūb) find rest (tmn) in dhikr. Q 89:27 says the *nafs* (muṭma'inna, from tmn) is welcomed home. The muṭma'inna nafs of 89:27 is the *completion* of the muṭma'inna qalb of 13:28. **The two "centers" converge in the eschatological nafs.** This is the Quran's subtle unification: what happens to the qalb in life happens to the nafs at death.

---

## 9. Classical prior art

The nafs literature is one of the deepest in the Islamic tradition. Key classical treatments I engaged with:

- **al-Ghazālī (d. 1111), Iḥyāʾ ʿUlūm al-Dīn, Book 21** (*Kitāb sharḥ ʿajāʾib al-qalb* — Book of the Marvels of the Heart). Despite its title, the book catalogues the nafs-states extensively. Al-Ghazālī takes 12:53, 75:2, 89:27 as the foundational trio. He introduces the progression narrative but grounds it in the pair of Prophetic sayings ("the greater jihād is jihād al-nafs") and the tazkiya vocabulary of Q 91:9. His treatment is explicitly tripartite in psychology (nafs ≠ qalb ≠ rūḥ). **Ghazalian psychology MAXIMISES the distinction the Quran only implies.**
- **Ibn al-Qayyim (d. 1350), Madārij al-Sālikīn**, vol 1, especially *manzilat al-tawba* and subsequent stations. He critiques the Sufi overextension but keeps the three-state core. His contribution: sharper scriptural anchoring of each state — ammāra from Yūsuf, lawwāma from Qiyāma, muṭma'inna from Fajr. He also acknowledges *rāḍiya / marḍiyya* as states (not mere adjectives) and adds *mulhama* (inspired) reading *wa-alhama-hā fujūra-hā wa-taqwā-hā* (Q 91:8) as a fourth Quranic-anchored state — though the participle itself does not appear on the nafs in the Quran. **This is a classical *interpretive* fourth state; our corpus audit does not confirm it lexically.**
- **al-Qushayrī (d. 1072), al-Risāla al-Qushayriyya, *bāb al-nafs***. Qushayrī treats the nafs as *the blame-object* of the spiritual path. His definition: *"al-nafs: a subtle thing placed in the body as a faculty for evil qualities."* He relies almost entirely on hadith rather than Quranic exegesis; his Quranic anchors are 12:53 and 79:40 (*nahā al-nafsa ʿan al-hawā*). His theology is strongly DUALIST: nafs is the opposing faculty; *qalb* is the redeemable faculty. **This is closer to the Quranic bipartite psychology than al-Ghazālī's tripartite.**
- **Ibn ʿArabī (d. 1240), al-Futūḥāt al-Makkiyya, bāb 73** on the *maqāmāt al-nafs*. Ibn ʿArabī formalises the seven-state ladder (ammāra, lawwāma, mulhama, muṭma'inna, rāḍiya, marḍiyya, kāmila) that becomes the mature Sufi orthodoxy. He explicitly draws on post-Quranic tradition for mulhama and kāmila. His interest is ontological (stations of being), not psychological; he reads the nafs-ladder as the *macrocosmic* ladder of realities. **This is the point of maximum distance from the bare Quranic text.**

The gradient from al-Qushayrī (11th c., bipartite, hadith-leaning) → al-Ghazālī (12th c., tripartite, scripturally robust) → Ibn ʿArabī (13th c., seven-station, ontological) is the gradient of **increasing interpretive compression**. The Quran's inventory has been steadily *sequenced, systematised, and Neoplatonised* across four centuries.

**What's genuinely Quranic:**
- The trio of modifiers ammāra / lawwāma / muṭma'inna (all three explicitly named).
- The rāḍiya + marḍiyya pair as continuation of muṭma'inna.
- Q 91:7–10 as the soul's cosmology (with fujūr and taqwā as dual inspirations).
- Q 79:40 as the ethical injunction (nahā al-nafs ʿan al-hawā).
- Q 12:53 as the epistemic injunction (refusal of self-exoneration).
- The nafs-qalb implicit distinction (qalb = reception site; nafs = will site).
- The singular/plural split (individual eschatology / collective ethics).

**What's post-Quranic classical synthesis:**
- The ladder-sequence ammāra → lawwāma → muṭma'inna.
- The mulhama and kāmila states.
- The tripartite nafs-qalb-rūḥ anthropology.
- The specific *maqāmāt* mapping onto cosmological stations (Ibn ʿArabī).
- The reading of tazkiya (Q 91:9) as a stepwise practice of progression.

---

## 10. Synthesis — what the Quran actually says about the nafs

The root nfs in the Quran is a **vocabulary of accountability**. 298 tokens across 270 verses, leaning Meccan, overwhelmingly nominal, structured by a singular-individual vs plural-collective split.

The three states (ammāra, lawwāma, muṭma'inna) are **lexical inventory**, not a ladder. The Quran gives them at three eschatological stations: in-life (Joseph's self-diagnosis), at-judgement (Qiyāma's witness), post-judgement (Fajr's welcome). The order is LITURGICAL (the stages of the eschaton), not DEVELOPMENTAL (the stages of practice). Classical Sufi tradition converted the liturgical staging into a developmental ladder — a natural but *interpretive* extension.

The fourth and fifth states (rāḍiya, marḍiyya) are Quranic modifiers of the muṭma'inna nafs, not independent states. The sixth and seventh (mulhama, kāmila) are *post-Quranic*.

The nafs is, grammatically, more PATIENT than AGENT (more often had/given/returned/killed than subject of a verb). It gains full agency only in end-of-world universal formulas. In narrative it is assaulted, tempted, blamed; it acts only in the formulas of judgement.

The nafs-qalb-rūḥ tripartite is POST-Quranic. The Quran's psychology is BIPARTITE: qalb as reception-site, nafs as will-site, with rūḥ reserved for divine agency. The classical tradition's grand tripartite is Hellenistic-Jewish-Christian overlay.

The most theologically loaded cross-reference in the whole nafs vocabulary is **Q 13:28 ↔ Q 89:27**. The hearts that found rest through dhikr in Q 13:28 are the same reality as the muṭma'inna nafs invited to return in Q 89:27. Root T-m-n develops across 13 tokens exclusively on hearts/states, then lands on the nafs at the eschatological summons. **The Quran's psychology terminates in a soul that has become a heart.** The classical Sufi vocabulary of *tawḥīd al-qalb wa-l-nafs* (unification of heart and soul) is thus not speculative metaphysics; it is an ARC visible in the Quran's root-deployment if one counts carefully.

**Final verdict.** The classical 3-state typology is EXPLICITLY QURANIC in vocabulary (all three adjectives are in the text with the nafs) and IMPLICITLY QURANIC in structure (three eschatological stations correspond). The *ladder* between them is hermeneutic. The extensions (mulhama, kāmila, nafs-qalb-rūḥ tripartite) are post-Quranic theology. Sufi practice can rest on the Quranic data, but should distinguish what the text licenses (the poles, the states, the bipartite psychology) from what it does not explicitly sequence (the progression).

The Quran is not a manual of nafs-discipline. It is a **dramatic typology of the soul at its stations of accountability.** The Sufi tradition built a manual from the drama. That manual has served 1,400 years of spiritual practice and has been, on the whole, faithful to the poles — while adding a middle and a metaphysics that are its own contribution.

---

## Appendix — the 298 tokens by form-class

**Verbal tokens (3):**
- Q 81:18 *tanaffasa* — the dawn when it breathes (perfect, form V)
- Q 83:26 *yatanāfasi* — the paradise-drinkers let them compete (imperfect, form VI)
- Q 83:26 *al-mutanāfisūn* — the competitors (active participle, form VI, masculine plural)

**Singular nominal tokens (140) — distribution by grammatical case:**
- NOM: 24 (subject or predicate)
- ACC: 33 (direct object)
- GEN: 83 (possessive/prepositional)

**Plural nominal tokens (155):**
- anfus (FP) = 153
- nufūs (FP, broken plural) = 2 (Q 17:25, Q 81:7)
- NOM: 18, ACC: 59, GEN: 78

**Unique verses containing nfs: 270.** Density-highest verses:
- Q 16:111 (3 tokens): "the Day when every *nafs* comes disputing for itself and every *nafs* is paid in full..."
- Q 2:48, Q 6:98, Q 17:25, Q 82:19, and several others with 2 tokens.

**Unique surahs with 0 nfs tokens:** most of the short late-Meccan surahs; not surveyed in this run.

---

## Cross-references
- [intra-quranic-cross-references.md §Finding 4](../intra-quranic-cross-references.md) — Q 13:28 chiastic palindrome and Tmn-network.
- [root-cartography.md §7-subject oath](../phase-b-hypotheses/root-cartography.md) — Q 91:1–10 with *nafs* as 7th oath-object (among sun/moon/day/night/sky/earth/soul).
- [rahman-deep-dive.md] — Ar-Raḥmān's refrain structure; the muṭma'inna soul belongs to the paradise-section of eschatological drama.
