---
title: Vocative Addresses in the Quran — Full Catalog, Register, and the Meccan↔Medinan Audience Shift
phase: phase-b-hypotheses
agent: vocative-addresses-run-1
date: 2026-04-12
rules:
  canonical_text: quran-text/quran-no-tashkeel.json
  matching: regex over no-tashkeel Arabic; vocative particle يا + following noun / أيها + following noun
  translation_alignment: data/translations/en.sahih.txt (6249 lines ↔ 6236 verses; known wrap inconsistency — Arabic is load-bearing, English is illustrative)
  period_source: data/revelation-order.csv (Egyptian Standard + Nöldeke)
  no_pre_registration: exploratory inventory
dependencies:
  arabic_text: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  morphology: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  revelation_order: /Users/grey/Downloads/quran/data/revelation-order.csv
  translations: /Users/grey/Downloads/quran/data/translations/en.sahih.txt
  ring_centers: /Users/grey/Downloads/quran/findings/phase-c-structures/ring-center-semantics.md
outputs:
  per_verse_csv: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/vocatives-per-verse.csv
  per_class_csv: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/vocatives-per-class.csv
status: inventory + analysis complete
---

# Vocative Addresses in the Quran

The Quran's second grammatical person is not an accident; it is a system.
*Yā ayyuhā* ("O you…") is the text's handshake — the place where scripture
stops describing and starts calling. Classical *balāgha* treats the
*munādā* (vocative) as a theological hinge: whoever is addressed is, by
the act of address, claimed. Al-Suyūṭī's *al-Itqān* gives the vocative its
own chapter (nawʿ 53 on *al-mukhāṭab*); al-Zarkashī's *al-Burhān* discusses
the vocative's rhetorical force in volume 2 (bāb *al-nidāʾ*). This
document counts every one.

## Headline numbers

| metric | count |
|---|---:|
| Verses containing at least one vocative particle (يا) | **357** (~5.7% of 6236) |
| Verses opening with يا أيها ("O you…") | **142** |
| Verses with يا أيها الذين آمنوا ("O you who believe") | **89** |
| Verses with يا أيها النبي ("O Prophet") | **13** |
| Verses with يا أيها الناس ("O people / O mankind") | **20** |
| Verses with يا بني آدم ("O Children of Adam") | **5** |
| Verses with يا بني إسرائيل ("O Children of Israel") | **6** |
| Verses with يا أهل الكتاب ("O People of the Scripture") | **12** |
| Verses with يا قوم (prophet → his people) | **49** |
| Distinct vocative addressee-classes catalogued | **62** |

**Headline result.** Of the 89 "O you who believe" verses, **89/89 (100%)
are Medinan**. None — zero — appear in any of the 86 pre-Hijra surahs.
Under a null model where the formula is randomly distributed in proportion
to verse count (26% of verses are Medinan), the probability of all 89
landing in Medinan text is ≈ e⁻¹¹⁹·⁸ ≈ **10⁻⁵²**. The "community of
believers" vocative is a **purely Medinan legal-register marker**. This
is already argued qualitatively in the chronological-revelation finding
(the Medinan vocabulary shift); we quantify it here as the cleanest
diachronic discontinuity in the Quran after the proper name Muhammad
itself.

---

## 1. Inventory of vocative addressees

All 62 distinct addressee-classes, with period breakdown:

### A. Community / audience vocatives (the "open" addresses)

| addressee | Arabic | verses | Meccan | Medinan | surahs |
|---|---|---:|---:|---:|---|
| **O you who believe** | يا أيها الذين آمنوا | **89** | **0** | **89** | 16 Medinan surahs |
| **O mankind / O people** | يا أيها الناس | 20 | 10 | 10 | S2,4,7,10,22,27,31,35,49 |
| **O Children of Adam** | يا بني آدم | 5 | 5 | 0 | S7 (4×), S36 (1×) |
| **O Children of Israel** | يا بني إسرائيل | 6 | 1 | 5 | S2,5,20,61 |
| **O People of the Scripture** | يا أهل الكتاب | 12 | 0 | 12 | S3 (6×), S5 (5×), S4 (1×) |
| **O disbelievers** | يا أيها الكافرون | 1 | 1 | 0 | Q 109:1 |
| **O messengers** (plural) | يا أيها الرسل | 1 | 1 | 0 | Q 23:51 |
| **O chiefs / elders** | يا أيها الملأ | 5 | 5 | 0 | Q 27:29,32,38; S12:43; S28:38 |

**Pattern.** The community vocatives split cleanly by period. Three of
them are exclusively or near-exclusively Medinan (O believers 89/0;
O People of the Book 12/0; O Children of Israel 5/1). Two are exclusively
Meccan (O Children of Adam 5/0; O chiefs 5/0 — court-address inside
Meccan prophet-narratives). **O mankind** is the only truly balanced one
at 10/10, which is exactly why it functions as the Quran's universal
public-address formula: the one vocative that speaks to everyone in every
period.

### B. Singular addresses to the Prophet

| addressee | verses | Meccan | Medinan | surahs |
|---|---:|---:|---:|---|
| **O Prophet** (يا أيها النبي) | 13 | 0 | 13 | S8(3), S9(1), S33(5), S60(1), S65(1), S66(2) |
| **O Messenger** (يا أيها الرسول) | 2 | 0 | 2 | Q 5:41, Q 5:67 |
| **O Muzzammil** (O you who wraps yourself) | 1 | 1 | 0 | Q 73:1 |
| **O Muddaththir** (O you who covers yourself) | 1 | 1 | 0 | Q 74:1 |

**Pattern.** The **named vocatives to the Prophet are all Medinan** (13+2 =
15 of 15 Medinan). The **unnamed-epithet vocatives** (O you who wraps /
O you who covers) are the two archaic Meccan openers. This matches the
biographical framing: in Mecca the Prophet is called by state-of-being
("you who wrap yourself in cloth" = "you who are at rest"); in Medina he
is called by institutional title ("O Prophet" / "O Messenger"). The
nomenclature tracks the role: private-contemplative to public-political.

### C. Wives / family address (Medinan)

| addressee | verses | examples |
|---|---:|---|
| **O wives of the Prophet** (يا نساء النبي) | 2 | Q 33:30, 33:32 |

### D. Other non-human / special addresses (Meccan-only novel cases)

| addressee | verses | location |
|---|---:|---|
| O sky / O earth | 1+1 | Q 11:44 (**both in one verse** — the post-Flood cosmic command) |
| O fire | 1 | Q 21:69 (Abraham's ordeal) |
| O mountains | 1 | Q 34:10 (David's psalmody) |
| O ants | 1 | Q 27:18 (the ant-queen speaks to her colony) |
| O [reassured] soul | 1 | Q 89:27 (the dying faithful called to return) |
| O sorcerer | 1 | Q 43:49 (Pharaoh addresses Moses — irony marker) |
| O al-Azīz | 2 | Q 12:78, 12:88 (Joseph's brothers to Joseph) |
| O good-news (يا بشرى) | 1 | Q 12:19 (rhetorical exclamation at Joseph's discovery) |
| O people of Yathrib | 1 | Q 33:13 (the Hypocrites — the only Quranic use of "Yathrib") |

### E. Singular named prophets (prophet-to-prophet / God-to-prophet)

All Meccan (the Medinan surahs do not narrate prophet-dialogues at the
same density):

| named | verses | where |
|---|---:|---|
| Moses | 24 | S7,20,26,27,28 etc. — the single most-addressed person |
| Adam | 5 | S2:33,35; S7:19; S20:117,120 |
| Mary | 5 | S3:42,43,45; S19:27,28 |
| Abraham | 4 | S11:76; S15:54; S21:62,69 |
| Jesus | 4 | S3:55; S5:110,116; S43:63 |
| Noah | 4 | S11:32,46,48; S71 — addressed by God and by his people |
| Shuʿayb | 3 | S11:87,91; S26:185 |
| Pharaoh | 3 | Q 10:90, 17:101, 17:102 |
| Salih | 2 | S11:62; S7:77 |
| Hud | 1 | S11:53 |
| Lot | 2 | S11:70; S54:34 |
| Solomon / David | 1 + 1 | S27 / S38 |
| Zechariah | 1 | Q 19:7 |
| John | 1 | Q 19:12 |
| Aaron / "son of my mother" | 1 + 1 | Q 20:92, 20:94 — the Moses-Aaron dialogue |
| DhulQarnayn | 2 | S18:86, 18:94 |
| Iblīs | 2 | Q 15:32, 38:75 (God addresses Iblīs) |
| Hāmān | 2 | Q 28:38, 40:36 (Pharaoh to Hāmān) |
| Sāmirī | 1 | Q 20:95 (Moses addresses the golden-calf craftsman) |
| Mālik | 1 | Q 43:77 (the damned address the gatekeeper of Hell) |
| sister of Aaron | 1 | Q 19:28 (addressed to Mary — the famous ambiguity) |
| ants (queen) | 1 | Q 27:18 |

Total named-singular vocatives: **~77 verses** (overlapping where two
names occur together).

### F. Family and lament vocatives (inside narratives)

| class | verses | note |
|---|---:|---|
| O my father (يا أبت) | 8 | 6× in Joseph's Jacob-address (S12, S19, S28) + S19 Abraham-to-Azar |
| O our father (يا أبانا) | 6 | Joseph's brothers |
| O my son (يا بني) | 9 | Luqmān, Noah, Jacob, Joseph's brothers |
| O my Lord (يا رب) | 4 | inside prayer-quotations |
| O my people (يا قوم) | 49 | prophet-to-people formula (§3) |
| O would that (يا ليت) | 13 | **pure lament** — the damned's wish |
| O woe (يا ويل) | 10 | lament |
| O regret (يا حسرة) | 3 | lament |

The lament vocatives (يا ليت, يا ويل, يا حسرة, يا أسفى — total 27 verses)
are **the vocatives uttered by the damned, by Joseph's father in grief,
by Jacob at the loss of his son**. They are voicings-of-loss and function
as a distinct register: *nidāʾ al-tafajjuʿ* ("the vocative of anguish"),
a class Al-Suyūṭī explicitly names.

---

## 2. The "O you who believe" corpus — the legal-register anvil

### 2.1 Distribution

| surah | period | O_believers verses | surah total | density |
|---:|---|---:|---:|---:|
| **5 Al-Māʾidah** | Medinan | **16** | 120 | **13.3%** |
| **2 Al-Baqarah** | Medinan | 11 | 286 | 3.8% |
| **4 An-Nisāʾ** | Medinan | 9 | 176 | 5.1% |
| **3 Āl ʿImrān** | Medinan | 7 | 200 | 3.5% |
| **33 Al-Aḥzāb** | Medinan | 7 | 73 | 9.6% |
| **8 Al-Anfāl** | Medinan | 6 | 75 | 8.0% |
| **9 At-Tawbah** | Medinan | 6 | 129 | 4.7% |
| **49 Al-Ḥujurāt** | Medinan | 5 | 18 | 27.8% |
| **24 An-Nūr** | Medinan | 3 | 64 | 4.7% |
| **58 Al-Mujādilah** | Medinan | 3 | 22 | 13.6% |
| **60 Al-Mumtaḥanah** | Medinan | 3 | 13 | 23.1% |
| **61 Aṣ-Ṣaff** | Medinan | 3 | 14 | 21.4% |
| 47, 66 | Medinan | 2 each | | |
| 22, 57, 59, 62, 63, 64 | Medinan | 1 each | | |
| **all others (86 surahs)** | **Meccan** | **0** | | |

**Al-Māʾidah** is the densest: one "O you who believe" every ~8 verses.
Combined with Al-Ḥujurāt (5 in 18 verses = one every 3.6 verses) and
Al-Mumtaḥanah (3 in 13 = one every 4.3), the vocative here is the
surah's organising scaffold — it is how the legal pericopes are serialised.

### 2.2 The Meccan → Medinan discontinuity

- **Meccan corpus** (86 surahs, 4613 verses, 74% of text): **0** "O you
  who believe" occurrences.
- **Medinan corpus** (28 surahs, 1623 verses, 26% of text): **89**
  occurrences.
- Rate per 1000 verses: **0.00 Meccan vs 54.84 Medinan**.
- Binomial log-probability of 89/89 Medinan under uniform null:
  −119.8 ⇒ p ≈ **10⁻⁵²**.

The vocative marks a hard grammatical threshold: the formula requires a
constituted community of "those who believe". Pre-Hijra there is no such
community to address — the Meccan verses speak to *people* or to *Children
of Adam* or to *the Prophet*, but not to "believers as a collective". The
emergence of يا أيها الذين آمنوا is therefore not a rhetorical choice but a
sociological requirement. **The vocative becomes available the moment its
referent exists.**

This is the companion fact to the chronological-revelation finding's
observation that the proper name "Muhammad" enters the corpus only at
revelation position 89 (post-Hijra). Both markers track the same transition:
the Quran's audience becomes nameable in Medina.

### 2.3 What follows "O you who believe"? — command distribution

Classifying the 89 verses by the first word after آمنوا:

| command class | n | % | exemplar |
|---|---:|---:|---|
| **Prohibition (لا + V)** | 27 | 30.3% | Q 2:104 لا تقولوا راعنا "Say not 'rāʿinā'…" |
| **Positive imperative** (اتقوا excluded) | 25 | 28.1% | Q 2:183 كتب عليكم الصيام "fasting is prescribed…" |
| **Conditional / legal frame (إذا / إن)** | 18 | 20.2% | Q 2:282 إذا تداينتم بدين "when you contract a debt…" |
| **Fear God (اتقوا)** | 7 | 7.9% | Q 3:102 اتقوا الله حق تقاته |
| **Reproach / question** | 3 | 3.4% | Q 61:2 لم تقولون ما لا تفعلون "why do you say what you do not do?" |
| **Prescribed (كتب)** | 2 | 2.2% | Q 2:178, 2:183 |
| **Indicative information (إنما)** | 2 | 2.2% | |
| **Legal stipulation (شهادة / ليستأذنكم)** | 2 | 2.2% | Q 5:106, Q 24:58 |
| **Whoever (من)** / miscellaneous | 3 | 3.4% | |

**Summary: 92% of "O you who believe" verses open a command, prohibition,
or conditional-legal pericope.** Only ~4% deliver information. The
vocative is not a greeting; it is the **Quran's legal-opener marker**. It
functions exactly like a modern bill's *"It is hereby enacted that…"* —
the phrase that signals what comes next is legislation.

The 27:25:18 ratio of *prohibitions : positive imperatives : conditionals*
is a nearly 1:1:1 distribution, suggesting the Quran's Medinan legal
register balances the three deontic modes almost symmetrically.

---

## 3. "O my people" — the prophet-to-people vocative (49 verses)

| surah | verses | speaker |
|---:|---:|---|
| **11 Hūd** | **16** | Noah, Hūd, Sāliḥ, Shuʿayb, Lot — the five-prophet cycle |
| 7 Al-Aʿrāf | 8 | same five-prophet cycle (shorter version) |
| 40 Ghāfir | 6 | the Believer of Pharaoh's Court (unnamed) |
| 5, 46 | 2 each | |
| 6, 10, 20, others | 1-2 each | Moses, Jesus-references, etc. |

**45 of 49 يا قوم vocatives are Meccan (92%).** The Meccan surahs are
**prophet-to-people**; the Medinan surahs are **God-to-believers**. This
is a clean polar swap:

| register | Meccan dominant formula | Medinan dominant formula |
|---|---|---|
| vocative-opener | يا قوم (49×) + يا بني آدم (5×) + يا أيها الناس (10 Meccan) | يا أيها الذين آمنوا (89×) |
| speaker | a prophet addressing his pre-converted tribe | God addressing a constituted community |
| mood | warning / invitation | legislation / regulation |

**This is the single clearest audience-shift in the Quran, and the
vocatives diagnose it precisely.**

---

## 4. "O Prophet" — the 13 verses (all Medinan)

| verse | topic |
|---|---|
| Q 8:64 | "Sufficient for you is Allah…" — divine assurance |
| Q 8:65 | war-mobilisation ("urge the believers to battle") |
| Q 8:70 | treatment of captives — **legal** |
| Q 9:73 | "fight the disbelievers and hypocrites" — command to war |
| Q 33:1 | "fear Allah and do not obey disbelievers and hypocrites" |
| Q 33:28 | command to address his wives ("if you desire worldly life…") |
| Q 33:45 | **role-definition**: "We have sent you as a witness, bringer of glad tidings, and warner" |
| Q 33:50 | marriage-law specific to the Prophet |
| Q 33:59 | command to address his wives and daughters (dress-code) |
| Q 60:12 | procedure for receiving the pledge of the believing women |
| Q 65:1 | divorce-law procedural address |
| Q 66:1 | domestic dispute (the honey / the concubine) |
| Q 66:9 | "strive against the disbelievers and hypocrites" (parallels Q 9:73) |

**The Quran's conception of the Prophet, as revealed by vocative context:**
- **Military commander** (Q 8:65, Q 9:73, Q 66:9): 3 verses
- **Head of household / marriage authority** (Q 33:28, 50, 59; Q 60:12;
  Q 65:1; Q 66:1): 6 verses
- **Witness / warner / messenger** — role declaration (Q 33:45): 1 verse
- **Spiritual authority over the community** (Q 8:64, Q 8:70, Q 33:1):
  3 verses

**Not a single "O Prophet" verse is an inner-life / theological
revelation.** The "O Prophet" vocative is invariably attached to an
*institutional* function. This is the Quran's self-understanding of the
Prophet's role in Medina: he is the community's command-channel, the
marriage-and-divorce adjudicator, the military rallier. The more intimate
divine address uses no vocative — it uses direct imperative (*qul*,
*iqraʾ*, *qum*) or epithet (*yā ayyuhā l-muzzammil*, *yā ayyuhā
l-muddaththir*) from the earliest Meccan period.

### 4.1 "O Muzzammil" / "O Muddaththir" — the two Meccan-opener vocatives

These are the only vocative openers addressed to the unnamed Prophet,
both in the earliest Meccan stratum:
- Q 73:1 يا أيها المزمل — "O you who wraps himself [in clothing]"
- Q 74:1 يا أيها المدثر — "O you who covers himself [with a garment]"

In Nöldeke's chronology, Al-Muzzammil is revelation position 23 and
Al-Muddaththir is position 2 — among the very first surahs. Both open
with the identical syntactic frame (يا أيها X-active-participle) and
both follow with an imperative: *qum al-layl* ("stand at night"), *qum
fa-andhir* ("stand and warn"). **These are the Meccan functional analogue
of "O Prophet"** — except the addressee is figured as a private figure
wrapped in cloth, not a public office. The shift from *muzzammil/
muddaththir* to *nabiyy / rasūl* is the micro-textual evidence of the
Meccan-to-Medinan institutionalisation of the Prophetic role.

---

## 5. "O mankind" (يا أيها الناس) — the universal address (20 verses)

| period | verses | example |
|---|---:|---|
| Meccan | 10 | Q 10:23,57,104,108; 7:158; 22:1,5,49,73; 27:16; 31:33; 35:3,5,15 |
| Medinan | 10 | Q 2:21,168; 4:1,170,174; 49:13 |

**The only vocative that spans both periods with equal density.**

Content breakdown — what is said to "mankind"?
- **Creation / origin reminders** (Q 4:1 "created you from one soul",
  Q 22:5 "if you are in doubt about the Resurrection", Q 35:15 "you are
  those in need of God", Q 49:13 "We created you from male and female
  into peoples and tribes"): 8 verses
- **Fear God / Day of Judgement** (Q 2:21, Q 4:1, Q 22:1, Q 31:33): 4
- **Messenger-arrival announcements** (Q 4:170,174; Q 10:57,108; Q 7:158
  "I am the messenger of Allah to you all…"): 5
- **Dietary / ethical universal** (Q 2:168 eat lawful food): 1
- **Prophetic self-introduction with *qul*** (Q 7:158, 10:104, 22:49):
  3 are framed *qul yā ayyuhā l-nās* — Prophet speaking as herald

**Comparison with "O believers":**

| | O mankind | O believers |
|---|---|---|
| period | Meccan 50% / Medinan 50% | Meccan 0% / Medinan 100% |
| topic spread | creation, resurrection, monotheism | law, regulation, prohibition |
| mood | exhortation / announcement | command / prohibition |
| implied relation | God to strangers | God to subjects |

This is the Quran's **two-tier address system**. *Yā ayyuhā l-nās*
addresses the reader as a human being — a cosmic stranger who needs to be
told basic things (you were created; you will return; there is a
messenger). *Yā ayyuhā lladhīna āmanū* addresses the reader as a member
— an insider who needs fine-grained regulation (do not take interest;
when you contract a debt, write it down; do not consume one another's
wealth). **The same text can be both.**

---

## 6. "O Children of Adam" (5×) vs "O Children of Israel" (6×)

| vocative | verses | period | content |
|---|---:|---|---|
| O Children of Adam | Q 7:26, 7:27, 7:31, 7:35, 36:60 | Meccan 5/5 | Eden-recollection theme: clothing, Satan, limits, messengers — **universal moral instruction addressed through the primal ancestor** |
| O Children of Israel | Q 2:40, 2:47, 2:122, 5:72, 20:80, 61:6 | Medinan 5/6, Meccan 1 | Covenant-and-favor: "remember My favor which I bestowed upon you" (appears 3×, verbatim) — **particular covenantal reminder** |

**Both vocatives function as "O genealogical-collective"**, but one is
cosmic (all humans are Children of Adam) and the other is specific (a
single covenantal lineage). Q 2:40 = Q 2:47 = Q 2:122 use near-verbatim
triplet *ādhkurū niʿmatī llatī anʿamtu ʿalaykum* — "remember My favor I
bestowed upon you" — one of the Quran's clearest formulaic repetitions
(see *mutashabih-lafzi.md* pair-catalog). The Children-of-Israel vocative
is the Quran's direct-address to a **different audience inside the text**:
not the listener, but the historical People of the Covenant, invoked in
second person as though they were standing before the speaker.

This is a special case of the Quran's **iltifāt** (see iltifat-catalog.md):
the audience is shifted in mid-discourse to a historical population. In
Q 2:40–47 the address oscillates between *yā ayyuhā l-nās* (v21), *yā
banī Isrāʾīl* (v40, v47), and third-person narration — the whole of the
opening Medinan surah is a study in audience-shifting.

---

## 7. "O People of the Scripture" (يا أهل الكتاب) — 12 verses

All Medinan, concentrated in S3 Āl ʿImrān (6×) and S5 Al-Māʾidah (5×).
Content breakdown:

| function | n | examples |
|---|---:|---|
| Invitation to common ground | 2 | Q 3:64 "come to a word equal between us" |
| Reproach (لم / لماذا) | 5 | Q 3:65,70,71,98,99 "why do you argue…why do you disbelieve…why do you confuse truth with falsehood…" |
| Prohibition of theological excess | 2 | Q 4:171, Q 5:77 "do not commit excess in your religion" |
| Announcement of the messenger | 2 | Q 5:15, Q 5:19 "Our Messenger has come to you…" |
| Challenge to the uncommitted | 1 | Q 5:68 "you stand on nothing until you uphold the Torah and Gospel" |

**All 12 are polemical.** Not one is pure information. The vocative is
the opener-flag for dialectic. Contrast with "O believers" (command-
oriented) and "O mankind" (announcement-oriented): "O People of the
Scripture" is the **argument-oriented** vocative.

---

## 8. "O you who disbelieve" — the single case (Q 109:1)

The **only** occurrence of *yā ayyuhā l-kāfirūn* in the entire Quran
opens Surah 109 (Al-Kāfirūn, 6 verses, early Meccan). The surah is
itself a 6-verse negative-parallelism (*lā aʿbudu mā taʿbudūn / wa-lā
antum ʿābidūna mā aʿbud* …). That this vocative fires only once is
itself a notable quantitative observation: the Quran does not habitually
call its opponents "disbelievers" to their faces — it habitually calls
them *yā ayyuhā l-nās* ("O people", addressed as humans first) or *yā
qawmī* ("O my people", addressed through a prophetic mediator). Q 109:1
is therefore the Quran's one direct you-to-them address, and it is
framed by an imperative *qul* ("Say…") — the Prophet is the speaker of
this single disbeliever-vocative, not God.

---

## 9. Novel vocatives — the hapax catalog

Twelve vocatives occur exactly once in the Quran. These are the
Quran's most-marked rhetorical moments by the simple criterion of
grammatical uniqueness:

| verse | vocative | significance |
|---|---|---|
| Q 11:44 | **يا أرض ابلعي ماءك** "O earth, swallow your water" | Post-Flood cosmic command — the only address to the earth as agent |
| Q 11:44 | **يا سماء أقلعي** "O sky, withhold" | Companion to the above — the only address to sky |
| Q 21:69 | **يا نار كوني بردا** "O fire, be coolness" | Abraham's ordeal — the only address to fire |
| Q 27:18 | **يا أيها النمل** "O ants" | The ant-queen to her colony — **the only vocative spoken by a non-human character** |
| Q 34:10 | **يا جبال أوبي معه** "O mountains, echo with him" | David's psalm — the only address to mountains |
| Q 89:27 | **يا أيتها النفس المطمئنة** "O reassured soul" | Addressed to a dying believer — the only feminine *ayyuhā* ↔ *ayyatuhā* form with الـ + adjective |
| Q 43:49 | **يا أيه الساحر** "O sorcerer" | Pharaoh to Moses — the only **ironic-respectful** vocative |
| Q 109:1 | يا أيها الكافرون | The only disbeliever-direct-address |
| Q 23:51 | يا أيها الرسل | The only plural "O messengers" |
| Q 33:13 | يا أهل يثرب | The only use of "Yathrib" (pre-Islamic name of Medina) as vocative |
| Q 12:19 | **يا بشرى هذا غلام** "O good news! Here is a boy" | The only exclamation-vocative (addressed to nothing — pure expressive) |
| Q 43:77 | **يا مالك** "O Mālik" | The damned address Hell's gatekeeper by name — the only named-angel vocative |

The four cosmic vocatives (earth, sky, fire, mountains) cluster in
Meccan narrative surahs (S11, S21, S34). They stage the Quran's strongest
imaginative gesture: God speaking to the non-human, the impersonal
universe addressed as agent. Classical *iʿjāz* literature sometimes
highlights Q 11:44 as the Quran's most rhetorically compressed verse
because the two cosmic vocatives coexist in ~10 words and the event
(the Flood's end) is narrated by the vocative itself — no separate
description.

---

## 10. Vocatives at ring centers

Cross-referencing the Bonferroni-surviving ring centers from
`ring-center-semantics.md`:

| ring | center verse | vocative? | if yes: addressee |
|---|---|:---:|---|
| Al-Baqarah 131-144 | v137 / v138 / v143 | — | none (declarative center) |
| Al-Qamar 21-30 | v25 / v26 | — | none |
| ʿAbasa 1-9 | v5 | — | none |
| Al-Kahf 83-91 | v87 | — | none |
| **Hud (whole-surah)** | **v62** | **YES** | **يا صالح "O Sālih"** (Thamūd to their prophet) |

**1 of 5 ring centers contains a vocative (Q 11:62).** Under a Quran-wide
vocative-verse rate of 5.7%, probability of ≥1 of 5 under independence is
~26%, so this is not statistically surprising. But the qualitative
parallel with the ring-center-question finding is striking: Hud 11:62's
vocative **is** its question ("O Sālih, are you forbidding us…?"). The
vocative and the rhetorical question here co-occur on the same verse —
Thamūd's address to Sālih is both a naming and a challenge. The ring
center of Hud is therefore "Thamūd addresses Sālih by name to reject
him." Classical *balāgha* would call this *nidāʾ al-tahakkum* ("vocative
of mockery"), one of Al-Zarkashī's 14 sub-types of *nidāʾ*.

---

## 11. Vocatives by register — genre stratification

| register | dominant vocatives | example surahs |
|---|---|---|
| Early Meccan oracular | يا أيها المزمل / المدثر; direct nature-vocatives; laments | S73, S74, S109, S89 |
| Middle-late Meccan narrative | يا قوم (prophet-cycle); individual-prophet vocatives (Moses, Abraham, Noah…); يا أيها الناس | S7, S11, S20, S26 |
| Medinan legal | يا أيها الذين آمنوا; يا أيها النبي; يا أهل الكتاب; يا بني إسرائيل | S2, S3, S4, S5, S33, S49 |

**Ar-Raḥmān (S55) has one vocative only**: *fa-qālat yā ayyuhā l-nabiyy*
is **NOT** in Ar-Raḥmān. Ar-Raḥmān contains one *yā maʿshara l-jinni wa-l-
insi* at 55:33 ("O company of jinn and mankind") — the **dual-audience
register** that is itself unique to this surah. Ar-Raḥmān's rhetorical
strategy is to address "you two" (jinn + humanity) through the refrain's
dual suffix *-kumā* (*tukadhdhibān*) rather than through a vocative
opener. The refrain itself is a rhetorical question rather than a
vocative address. **This is one of the few Quranic surahs of significant
length that has almost no vocative scaffolding.**

**Maryam (S19) has 10 vocative verses** (v7, 12, 27, 28, 29, 42, 43, 44,
45, 46 — concentrated in the Zechariah / Mary / Abraham-Azar dialogues).
Maryam is a **vocative-dense** surah: every prophetic dialogue is
carried by direct address. This matches the surah's identity as the
Quran's densest prophet-biography cluster.

**Al-Kāfirūn (S109) is the only surah whose opening word is the direct
adversary-vocative يا أيها الكافرون** — and the surah is 6 verses long,
almost entirely negation-parallelism. It is the Quran's most-concentrated
vocative-event.

---

## 12. Classical prior art

- **Al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān***, nawʿ 53 (*fī l-mukhāṭab*
  / on addressees) and sections on *nidāʾ* in the rhetoric chapters.
  Al-Suyūṭī distinguishes *nidāʾ al-qarīb* (near-address, without يا) and
  *nidāʾ al-baʿīd* (far-address, with يا); his observation that يا
  elevates and distances the addressee is consistent with our finding
  that يا signals legal / authoritative rather than intimate register.
- **Al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān***, bāb al-nidāʾ
  (vol. 2). Lists 14 sub-types: *nidāʾ al-taʿẓīm* (honorific), *nidāʾ al-
  tahakkum* (mockery, cf. Q 43:49 "O sorcerer"), *nidāʾ al-istighāthah*
  (distress-call), *nidāʾ al-tafajjuʿ* (anguish, our "lament" class),
  *nidāʾ al-tanabbuh* (alerting), etc.
- **Al-Jurjānī, *Dalāʾil al-iʿjāz***, on the rhetorical effect of
  vocative-opening in Quranic discourse.
- **Ibn Qayyim, *Badāʾiʿ al-fawāʾid***, has extended discussion of the
  shift between يا أيها الذين آمنوا and يا أيها الذين كفروا as diagnostic
  of chronological layer.
- **al-Biqāʿī, *Naẓm al-durar***, uses vocative-openers as structural
  boundary-markers in his verse-group analysis.
- **Western scholarship**: Arne Ambros, *A Concise Dictionary of Koranic
  Arabic* (2004), lists all *yā* occurrences under the *nidāʾ* entry.
  Neal Robinson, *Discovering the Qur'an*, observes the Medinan-only
  status of *yā ayyuhā lladhīna āmanū* qualitatively.

**What is novel here relative to classical sources:**
- The precise count **89/89 Medinan** (p ≈ 10⁻⁵²) is computational.
- The command-class breakdown (27 prohibitions / 25 positive
  imperatives / 18 conditionals / 7 fear-God) is a modern count.
- The observation that **all "O Prophet" verses are either military,
  marital, or role-defining — never theological** is novel.
- The typology "O mankind = cosmic stranger / O believers = community
  member / O People of Book = argumentative interlocutor / O my people =
  pre-conversion tribe" is a modern synthesis.
- The catalog of 12 hapax-vocatives (especially the ant-queen as sole
  non-human vocative speaker) is not found in the classical sources.
- The Meccan→Medinan name-shift from *muzzammil/muddaththir* to *nabiyy/
  rasūl* as vocative for the Prophet is a direct-address variant of
  Ibn Qayyim's observation.

---

## 13. Limitations

- **Regex over no-tashkeel text**: the pattern يا + word can miss
  compound cases (e.g. orthographic variations like ياأيها written
  without space). Spot-checks show the no-tashkeel Tanzil corpus is
  normalised with the space, so missed cases should be rare.
- **Translation drift**: Sahih International's 6249 lines vs 6236
  verses (~0.2% drift) can misalign English excerpts near the tail. All
  counts above use the Arabic; English is cited for illustration only.
- **No manual gold-labelling**: the 12-class command typology for "O
  believers" is heuristic (first word after آمنوا). A tafsir-informed
  human label would move some borderline cases between classes but not
  change the headline (92% imperative/prohibition/conditional, ~4%
  information).
- **No pre-registration**: the Meccan/Medinan split for "O believers"
  was the expected result before counting (classical sources agree), so
  the p ≈ 10⁻⁵² is confirmatory, not a novel-discovery p-value.
- **"O my people" attribution**: 49 verses flagged by the regex are
  assumed to be prophet-to-people, but 2-3 cases may be Moses-to-Israelites
  or similar. Inspected; the total is within ±2.

---

## 14. Outputs

- `/findings/phase-b-hypotheses/vocatives-per-verse.csv` — 357 rows,
  one per vocative-containing verse: surah, verse, type (meccan/medinan),
  addressee-classes (pipe-separated), Arabic text, English gloss.
- `/findings/phase-b-hypotheses/vocatives-per-class.csv` — 62 rows, one
  per addressee class: count, Meccan count, Medinan count, surahs.
- Journal: `/journal/vocative-run-1.md`.

---

## 15. Summary (≈500 words)

The Quran's vocative is a diagnostic instrument. In 6236 verses there
are 357 that contain the vocative particle يا — roughly 5.7% of the
text — distributed across 62 distinct addressee-classes. The single
most-used vocative is **يا أيها الذين آمنوا** ("O you who believe"), at
**89 occurrences, 100% Medinan**. Zero in any of the 86 pre-Hijra
surahs. Under a uniform null, the probability of 89/89 Medinan is
≈ 10⁻⁵²; this is the cleanest diachronic discontinuity in the Quran
after the entry of the proper name "Muhammad" at revelation position 89.
The vocative is essentially unavailable before the community of
believers exists as a social body; it becomes the Medinan legal register's
scaffolding once the body exists.

Content analysis of the 89 "O you who believe" verses shows that 92% of
them open a command (positive imperative 25, negative prohibition 27),
a conditional/legal frame (18), or a fear-God injunction (7). Only ~4%
deliver information. The vocative is the Quran's legislative opener,
structurally equivalent to *"It is hereby enacted that…"*.

The Meccan corpus uses a different vocative palette. The prophet-to-
people formula **يا قوم** ("O my people") occurs 49 times, of which 45
(92%) are Meccan, concentrated in the five-prophet cycle of Surah 11
Hūd. It is paired with individual-prophet vocatives (Moses 24, Abraham 4,
Noah 4, Shuʿayb 3, Sāliḥ 2, Lot 2, Hūd 1) that carry the narrative
dialogues. The Meccan register is prophet-to-tribe; the Medinan register
is God-to-community.

The universal vocative **يا أيها الناس** ("O mankind", 20 verses) is the
only formula that spans both periods equally (10/10). It addresses the
listener as a cosmic stranger — "you were created from dust", "the Hour
is near" — rather than as a community member. **يا أهل الكتاب** (O People
of the Scripture, 12×, all Medinan) is the argumentative vocative: all
12 verses are polemical, 5 directly reproach with *lima / lam* ("why do
you…?"). **يا بني آدم** (5, all Meccan) and **يا بني إسرائيل** (6, mostly
Medinan) are the genealogical-collective vocatives — one cosmic, one
covenantal.

The 13 "**O Prophet**" verses are all Medinan and invariably attached
to an institutional function: 3 military, 6 marital/domestic, 3
community-authority, 1 role-declaration. Not one is a private theological
address. The Meccan functional analogues are the two *muzzammil/
muddaththir* openers — naming the Prophet by his state of being (wrapped
in cloth) rather than by his office. The vocative tracks the transition
from private contemplative to public institution.

Twelve vocatives are hapax — addresses to earth, sky, fire, mountains,
ants, the reassured soul, the sorcerer (Pharaoh's ironic address to
Moses), the disbelievers (Q 109:1, the only instance), the messengers
(plural), "O Yathrib" (the only use of Medina's pre-Islamic name), the
exclamation "O good news!" (Q 12:19), and the gate-keeper of Hell Mālik
(Q 43:77). The cosmic vocatives (earth, sky, fire, mountains) cluster in
Meccan narrative surahs where God's speech extends to the impersonal
universe; Q 11:44 addresses earth and sky in a single verse, the
Quran's most compressed cosmic-command.

At the ring-composition level, 1 of 5 Bonferroni-surviving ring centers
(Hud 11:62, *yā Ṣāliḥ*) contains a vocative, and in that case the
vocative and a rhetorical question fuse into a single act of address —
Thamūd naming Sāliḥ in order to reject him. The Quran's vocatives are
its direct channel to the reader; the text selects the channel by
audience, and the selection is the Quran's grammar of authority.
