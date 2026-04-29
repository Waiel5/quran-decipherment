---
title: Negation Taxonomy of the Quran — a full computational audit of bāb al-nafī
phase: phase-b-hypotheses
agent: negation-taxonomy-run-1
date: 2026-04-12
rules:
  canonical_corpus: Quranic Arabic Corpus morphology v0.4 (Dukes)
  negation_detection: POS:NEG tag (all instances) + root lys (laysa) + lemma gayor (ghayr) + lemma <il~aA (exception illā)
  counts_are_per-token_unless_noted: true
  no_pre-registration: exploratory inventory
  basmala_policy: counted only in Surah 1 (QAC convention)
  verse_numbering: hafs-kufan
dependencies:
  morphology: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  arabic_text: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  revelation_order: /Users/grey/Downloads/quran/data/revelation-order.csv
  paired_opposites: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/paired-opposites-network.md
  rhetorical_questions: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/rhetorical-questions.md
  ring_centers: /Users/grey/Downloads/quran/findings/phase-c-structures/ring-center-semantics.md
outputs:
  per_surah_csv: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/negation-per-surah.csv
status: inventory + analysis complete
---

# Negation Taxonomy of the Quran

The Quran argues. And a large fraction of its argument moves through
negation — through saying what is *not* the case. Classical Arabic
grammar, aware of this, devoted a dedicated chapter to the topic: *bāb
al-nafī* (the chapter on negation). Ibn Hishām's *Mughnī al-Labīb*, al-
Zarkashī's *Burhān* (**[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 57" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; nawʿ number retagged per MW-6 mechanical scan; substantive classical doctrine (ḥurūf al-nafī chapter) unchanged; statistical finding unaffected; candidate correct locus: nawʿ 32 *al-adawāt* pending Phase-2 secondary-triangulation]** — *ḥurūf al-nafī*), and al-Suyūṭī's *Itqān*
all distinguish at least six grammatical particles that negate, each with
a different scope over tense, aspect, verbal vs. nominal predication, and
absoluteness. English flattens all of these to "not"; Arabic does not.

This document quantifies that distinction across all 114 surahs.

## 0. Headline numbers

| metric | count |
|---|---:|
| Total NEG-tagged tokens in QAC v0.4 | **2,688** |
| + copular laysa (ROOT:lys, tagged V) | + 89 |
| + nominal ghayr (LEM:gayor, tagged N) | + 147 |
| + exception-marker illā (LEM:<il~aA, tagged RES/EXP) | + 663 |
| **grand total (negation-bearing tokens)** | **3,587** |
| Surahs with **zero** negation tokens (by any count above) | **11** (Q 97, 99, 101, 102, 103, 104, 106, 108, 110, 113, 114) |
| Surahs with ≥1 negation per verse on average | 25 |
| Densest negation surah | **Q 60 Al-Mumtaḥanah** (1.15 neg/verse, Medinan) |
| Rarest negation surah among non-zero | Q 100 Al-ʿĀdiyāt (0.09) |

**Per-lemma distribution of NEG-tagged particles:**

| particle | lemma | tokens | % of NEG |
|---|---|---:|---:|
| **lā** | laA | 1,406 | 52.3% |
| **mā** | maA | 705 | 26.2% |
| **lam** | lam | 353 | 13.1% |
| **in** (negative conditional) | <in | 114 | 4.2% |
| **lan** | lan | 106 | 3.9% |
| **kaylā** ("so that…not") | kaY | 3 | 0.1% |
| **lammā** (not-yet) | l~am~aA | 1 | <0.1% |

Add **laysa** (89 tokens, 85 verses) and **ghayr** (147 tokens, 142
verses); these are not POS-tagged NEG because laysa is conjugated as a
(quasi-)verb and ghayr is a noun of exception. Structurally both are
negations. Finally, **illā** (663 tokens in 555 verses) is the exception-
complement that turns any preceding negation into a restriction-formula
(*lā…illā*, *mā…illā*) — the single most rhetorically-loaded device in
the Quran's theological register.

**The Quran negates something, on average, once every 2.35 verses.**

---

## 1. The seven particles — scope, tense, and theological register

Classical grammar's division (summarised from Ibn Hishām, al-Zarkashī,
and al-Suyūṭī):

| particle | governs | tense-scope | force |
|---|---|---|---|
| **lā** (laA) | imperfect (jussive→prohibitive; indicative→simple); nominals; with zero copula | present/habitual/absolute | widest |
| **mā** (maA) | mostly perfect verb; also nominal; + illā | past denial | definite |
| **lam** (lam) | jussive imperfect | past (meaning) | past-negation |
| **lan** (lan) | subjunctive imperfect | future | emphatic / absolute future |
| **laysa** (lys) | nominal sentence (as quasi-verb) | present copula | "is not" |
| **in** (<in) | nominal or verbal; classical + illā construction | timeless | often exceptive |
| **ghayr** (gayor) | noun / attributive phrase | exceptive | "other than" |

lā is the general-purpose negator (it covers every mode except the
specialised ones). mā handles the simple past denial and — crucially —
combines with illā to produce the exception-formula. lam takes a
jussive imperfect to denote past negation while lan takes a subjunctive
imperfect to denote absolute-future negation: the contrast between them
is one of the most theologically exploited particle-pairs in the Quran.

### 1a. Meccan/Medinan balance

Running each particle against the Egyptian-standard Meccan/Medinan
classification:

| particle | total | Meccan | Medinan | % Meccan |
|---|---:|---:|---:|---:|
| lā | 1,406 | 877 | 529 | 62.4% |
| mā | 705 | 526 | 179 | **74.6%** |
| lam | 353 | 205 | 148 | 58.1% |
| ghayr | 147 | 93 | 54 | 63.3% |
| in (neg) | 114 | 103 | 11 | **90.4%** |
| lan | 106 | 48 | 58 | **45.3%** |
| laysa | 89 | 48 | 41 | 53.9% |

**Reference baseline.** The Meccan share of total Quranic verses is
~68% (varies by counting rule). Three particles deviate meaningfully:

- **mā** is over-represented in Meccan (74.6%). Meccan discourse is
  heavily polemic ("they did **not** come to their senses", "they did
  **not** believe"), and past-denial is the mode of that polemic.
- **negative in** is almost exclusively Meccan (90.4%). This is the
  classical-Arabic literary register's conditional-negation; Medinan
  legal language uses *lā* and *lam* instead.
- **lan** is the one particle that *inverts* — Medinan 54.7%. Medinan
  law frequently uses absolute-future negation in oaths and covenants
  ("they will **never** harm you", "you shall **never** …").

The other particles track the Meccan base rate within noise.

---

## 2. Per-surah negation density

(Full table in `negation-per-surah.csv`.) Top 15 by density (negations
per verse), all-inclusive count:

| rank | surah | period | verses | negations | density |
|---:|---|---|---:|---:|---:|
| 1 | **60 Al-Mumtaḥanah** | Medinan | 13 | 15 | **1.15** |
| 2 | **35 Fāṭir** | Meccan | 45 | 48 | **1.07** |
| 3 | 6 Al-Anʿām | Meccan | 165 | 151 | 0.92 |
| 4 | 58 Al-Mujādilah | Medinan | 22 | 20 | 0.91 |
| 5 | 10 Yūnus | Meccan | 109 | 91 | 0.83 |
| 6 | 46 Al-Aḥqāf | Meccan | 35 | 29 | 0.83 |
| 7 | **2 Al-Baqarah** | Medinan | 286 | 229 | 0.80 |
| 8 | 9 Al-Tawbah | Medinan | 129 | 103 | 0.80 |
| 9 | 34 Saba' | Meccan | 54 | 43 | 0.80 |
| 10 | 11 Hūd | Meccan | 123 | 97 | 0.79 |
| 11 | 33 Al-Aḥzāb | Medinan | 73 | 56 | 0.77 |
| 12 | 59 Al-Ḥashr | Medinan | 24 | 18 | 0.75 |
| 13 | **112 Al-Ikhlāṣ** | Meccan | 4 | 3 | **0.75** |
| 14 | 28 Al-Qaṣaṣ | Meccan | 88 | 65 | 0.74 |
| 15 | 63 Al-Munāfiqūn | Medinan | 11 | 8 | 0.73 |

Observations:

- **Al-Mumtaḥanah (60) tops the list** at 15 negations in 13 verses.
  This is a Medinan "loyalty" surah: "do **not** take My enemy and your
  enemy as allies… do **not** take… do **not**…" — legal-prohibitive
  density.
- **Al-Ikhlāṣ (112)** scores 0.75 *in 4 verses* — and all 3 of its
  negations are of the same particle (**lam**), concentrated in vv 3-4:
  *lam yalid · wa-lam yūlad · wa-lam yakun lahū kufuwan aḥad* (He
  begets not · nor is He begotten · nor is there any equal to Him).
  **Three past-tense-jussive negations in succession** — the Quran's
  densest packed apophatic formula. The surah defines God by saying
  three things God is not.
- **The 11 zero-negation surahs** are all short Meccan (97 Al-Qadr, 99
  Al-Zalzalah, 101 Al-Qāriʿah, 102 Al-Takāthur, 103 Al-ʿAṣr, 104 Al-
  Humazah, 106 Quraysh, 108 Al-Kawthar, 110 Al-Naṣr, 113 Al-Falaq, 114
  Al-Nās). These are declarative/eschatological/doxological. **Whatever
  short Meccan does, it doesn't negate.**

This aligns with a finding from our chronological-revelation work: the
Quran's rhetorical device-mix shifts sharply across periods. Negation
is a mode of *argument*, and argument is mostly what we call "middle-
late Meccan" and "Medinan". Short Meccan is the Quran in its
declarative-eschatological mode.

---

## 3. *lā ilāha illā…* — the foundational formula

The Shahāda — the Islamic monotheistic declaration — is syntactically
a **negation-plus-exception**: *lā ilāha illā Allāh* ("there is no god
but God"). The *lā* is an absolute-negation-of-genus (*lā al-nāfiya
li-l-jins*); the *illā* introduces the single exception that constitutes
the positive claim. Monotheism is declared as an exception to a
universal negation. This is itself a remarkable piece of grammatical
theology.

**Every occurrence of the formula in the Quran** (scan: NEG:laA + N:ilah
root Alh + RES/EXP:illā + [target] within 8-token window):

| total occurrences | 37 |
|---|---:|
| …with target = **huwa** (He) | **30** |
| …with target = Allāh | 2 |
| …with target = **anta** (You, vocative) | 1 |
| …with target = **anā** (I, divine self-speech) | 3 |
| …with target = *alladhī* (the One who…) | 1 |

**The Quran's default Shahāda form is *lā ilāha illā huwa*, not *lā
ilāha illā Allāh*.** 30 of 37 instances (81%) use the third-person
pronoun. The classical Shahāda with *Allāh* appears only twice in
Quranic form (the popular ritual *Allāh* version is rare; *huwa* is the
Quranic norm).

The *huwa* occurrences span the whole Quran — Al-Baqarah 2:163, Āyat
al-Kursī 2:255, Āl ʿImrān 3:2, 3:6, 3:18 (×2 — the verse has the
formula twice, bracketed by *lā ilāha illā huwa* · witnesses · *lā
ilāha illā huwa*), An-Nisāʾ 4:87, al-Anʿām 6:102, 6:106, al-Aʿrāf
7:158, al-Tawbah 9:31, 9:129, Hūd 11:14, al-Raʿd 13:30, Ṭāhā 20:8,
20:98, al-Muʾminūn 23:116, al-Naml 27:26, al-Qaṣaṣ 28:70, 28:88, Fāṭir
35:3, al-Zumar 39:6, Ghāfir 40:3, 40:62, 40:65, al-Dukhān 44:8, **al-
Ḥashr 59:22 and 59:23** (the Khawātim passage — the double declaration
at the densest divine-name concentration in the Quran), al-Taghābun
64:13, al-Muzzammil 73:9.

Three of the four "**I am God**" first-person formulas (*lā ilāha illā
ana*) are at Ṭāhā 20:14 (Moses' Sinai theophany), al-Anbiyāʾ 21:25, and
al-Naḥl 16:2. The one *illā anta* is at Al-Anbiyāʾ 21:87 — **Jonah's
prayer from the fish-belly**: *lā ilāha illā anta subḥānaka innī kuntu
mina al-ẓālimīn*. A vocative Shahāda spoken under water.

Cross-refs to our divine-names work: Q 59:22-23 is the densest divine-
name passage in the Quran; the Shahāda formula *frames* that octet
(v22 opens with it, v23 opens with it). The Khawātim al-Ḥashr is
structurally the Shahāda's maximal elaboration: a negation-exception
statement followed by eight rare names.

---

## 4. *lan tarānī* — absolute-future negation at Sinai

Q 7:143. Moses asks: *rabbi arinī anẓur ilayka* — "my Lord, show me, let
me look at You." The reply: *lan tarānī* — "you will **never** see Me."

The particle *lan* governs a subjunctive imperfect and encodes absolute-
future negation — stronger than *lā*. Classical grammar (al-Zamakhsharī
famously in the *Kashshāf*) debated whether *lan* implies **perpetual**
negation ("never, ever") or merely **prospective** negation ("not at
this time"); Ibn Mālik and the majority rejected al-Zamakhsharī's
Muʿtazilī reading that *lan* means permanent impossibility (which
would foreclose the beatific vision of God in the next life — a point
Sunnī theology insists on). Our count of Quranic *lan* + *r'y* (root
رأي) in a near-window: **1** — Q 7:143 *lan tarānī*. The formula is
a Quranic hapax in that exact form. Everywhere else in the Quran where
a human is told they will not see God, a different formula is used.

This is quite striking. The *lan tarānī* construction is unique; it
is not a Quranic formula but a Quranic **event**. That is what sits
behind the classical-theological weight assigned to Q 7:143: the
grammar marks it as singular.

More broadly, *lan* appears 106 times, the top 10 negated roots (after
*tarānī*):

- *lan taftaqiru* (will never be poor), *lan tufliḥū* (will never
  succeed), *lan taḍurrū* (will never harm), *lan yakhluqū* (will
  never create — the challenge-verses about the fly), *lan yanālahum*
  (will never reach them), *lan yudkhalahā* (will never enter).

*lan* is the particle of **cosmic closure**: what will absolutely
never happen. It is a future-tense boundary-marker.

---

## 5. *mā kāna li-X* — the humility-formula

A classical construction: *mā kāna li-Muḥammadin an yukhdhiba…* — "it
was not for Muhammad to…"; *mā kāna li-nabīyin…* — "it was not for a
prophet to…". The formula asserts *moral impossibility*: a past-denial
framed to assert that some hypothesised action was never appropriate
for the named subject.

Scan: NEG:maA + V(kwn) + P:li + [X] in a verse — **54 verses**.
Distribution:

- Al-Baqarah 2:114, 2:143
- Āl ʿImrān 3:79, 3:145, 3:161, 3:179
- Al-Nisāʾ 4:92
- Al-Māʾidah 5:116
- Al-Anʿām 6:111
- Al-Aʿrāf 7:13, 7:39, 7:43, 7:89, 7:101
- Al-Anfāl 8:33, 8:67
- Al-Tawbah 9:17, 9:70, 9:113, 9:114, 9:115, 9:120, 9:122 (Tawbah is
  the densest single-surah host)
- Yūnus 10:13, 10:15, 10:74, 10:100
- Hūd 11:20, 11:117
- Yūsuf 12:38, 12:76, 12:81
- Al-Raʿd 13:38
- Ibrāhīm 14:11, 14:22
- Maryam 19:35 (*mā kāna li-llāhi an yattakhidha min waladin* —
  **Christological: "it was not for God to take a son"**)
- Al-Nūr 24:16
- Al-Furqān 25:18
- Al-Naml 27:60
- Al-Qaṣaṣ 28:68, 28:81
- Al-ʿAnkabūt 29:40
- Al-Rūm 30:9
- Al-Aḥzāb 33:36, 33:53
- Saba' 34:21
- Fāṭir 35:44
- Ṣāffāt 37:30
- Ṣād 38:69
- Ghāfir 40:21, 40:78
- Al-Shūrā 42:46, 42:51
- Al-Zukhruf 43:13

Three specialisations are visible:

1. **Prophetic impossibility**: *mā kāna li-nabīyin* / *mā kāna
   li-rasūlin* — things prophets never do. Q 3:79, 3:161, 8:67, 33:36.
2. **Christological impossibility**: *mā kāna li-llāhi an yattakhidha
   min waladin* (Q 19:35). This is the theological core of the
   Quranic rebuttal of divine sonship — stated in the grammatical
   form of "moral impossibility".
3. **Communal impossibility**: *mā kāna li-l-muʾminīn* / *mā kāna
   li-ahli l-madīnah* (Q 9:120). Medinan law using the same formula
   for community obligations.

The formula is Quranic across both Meccan and Medinan strata — but
its heaviest concentration in Al-Tawbah (7 instances in 129 verses)
marks Al-Tawbah as the "covenantal-impossibility" surah *par
excellence*.

---

## 6. Divine apophatic negation — *lā yaʿlamu, lā yāʾkhudhuhu…*

What is God **not**? Any negation with a 3rd-person-masculine-singular
imperfect verb governed by *lā*, in a verse containing a divine
reference (Allāh / huwa / rabb-ka): **173 occurrences.** Top negated
predicates (by root):

| root | count | gloss |
|---|---:|---|
| **hdy** (guide) | **25** | "God does not guide…" (wrongdoers, disbelievers, the unjust) |
| **ḥbb** (love) | **19** | "God does not love…" (the arrogant, the corrupters, the transgressors) |
| ḍrr (harm) | 9 | harm does not touch God / God is not harmed |
| nfʿ (benefit) | 8 | benefit does not belong to the idols |
| ʿlm (know) | 7 | apophatic: not "God does not know" (that never occurs) but "they/others do not know what God knows" — in divine-subject verses |
| flḥ (succeed) | 5 | "wrongdoers do not succeed" |
| ʾkhdh (seize) | 4 | **Ayat al-Kursī's "lā taʾkhudhuhu sinatun wa lā nawm"** |
| ḥll (make-lawful) | 4 | |
| khlf (break/contradict promise) | 4 | "God does not break His promise" |
| ḍyʿ (waste) | 4 | "God does not waste the reward of…" |

The apophatic grammar has two sub-registers:

- **Moral apophasis** — lists of what God does *not* love: arrogance
  (*mustakbirīn*, 3x), corrupters (*mufsidīn*, 3x), betrayers (*khāʾinīn*),
  transgressors (*muʿtadīn*), the proud (*fakhūr*), those-who-rejoice-
  in-evil (*fariḥīn*), those-who-exult (*mariḥīn*), the unjust (*ẓālimīn*).
  The "beloved of God" list is defined by these 19 negatives.
- **Ontological apophasis** — what does not happen to God:
  *sinatun wa-lā nawm* (Q 2:255 — slumber/sleep);
  *khalfa al-mīʿād* (Q 3:9 — breaking promise);
  *yuḍīʿu al-muḥsinīn* (Q 9:120 — wasting the-doers-of-good);
  *yukallifu nafsan illā wusʿahā* (Q 2:286 — tasking beyond capacity).

### 6a. Āyat al-Kursī (Q 2:255) — the densest apophatic verse

Q 2:255's 50-word architecture is structured around three *lā*
negations stacked in the first half:

1. *lā ilāha illā huwa* — the Shahāda (§3 above)
2. *lā taʾkhudhuhu sinatun wa-lā nawm* — slumber and sleep do not take Him
3. *man dhā lladhī yashfaʿu ʿindahū **illā** bi-idhnihī* — no one can
   intercede except with His permission (negation-by-restriction, the
   same *illā*-form as the Shahāda)

**Three successive negation-exception constructions** structure the
opening half of the verse, before the kataphatic half opens with
*yaʿlamu mā bayna aydīhim wa-mā khalfahum* ("He knows…") — and
ends with *wa-lā yaʾūduhū ḥifẓuhumā* (their preservation does not
weigh Him down). Four *lā*s in one verse, each denying a different
limitation. This is the Quran's premier apophatic construction.

---

## 7. Prohibitive *lā* vs. declarative *lā*

The particle *lā* is the same word whether it functions as:

- **Prohibitive** (+ jussive, 2nd-person): *lā taʾkulū* — "do not eat!"
- **Declarative** (+ indicative, 3rd- or 1st-person): *lā yaʿlamūn* —
  "they do not know."

Scan: for every *lā* followed within 2 tokens by a verb, classify by
whether the verb carries 2nd-person marking:

| type | tokens | unique verses |
|---|---:|---:|
| Prohibitive (2nd-person directed) | 197 | 183 |
| Declarative (3rd/1st-person) | 825 | 702 |

**Declarative lā outnumbers prohibitive lā by ~4.2:1.** This is
revealing. The Quran's *lā* is overwhelmingly descriptive-polemical ("they
do not know", "they do not believe", "they do not see"), not
prescriptive-legal. The most famous commands — "do not kill", "do not
approach…", "do not eat…" — are structurally outnumbered by polemical
"they do not X" observations about the unbelieving.

The distinction matters because English translations flatten both
"lā" usages to "not"/"do not", losing the classical grammarian's
distinction between *al-lā al-nāhiya* (prohibitive lā) and *al-lā al-
nāfiya* (declarative lā). In morphological reality they are
distinguished by the verb's jussive vs. indicative inflection — and
thus recoverable from the corpus.

---

## 8. *lā ikrāha fī al-dīn* (Q 2:256) — the "no compulsion" verse

Q 2:256 opens with **NEG:laA + N:ikrāh** — a **nominal absolute
negation** (*lā al-nāfiya li-l-jins*, "the *lā* that negates the
genus"). Classical grammar is explicit: when *lā* is immediately followed
by a bare (indefinite, unmarked) noun in the accusative, it does not
merely negate an instance but the **entire category**. *lā rayba fī-hi*
(2:2 — "there is no doubt *of any kind* in it") uses the same
construction. *lā ikrāha* therefore means "there is no compulsion **of
any kind**", not "there is not a compulsion" or "there is not this
particular compulsion".

Token sequence at Q 2:256 (from the morphology):

```
laA^ [NEG, lā al-nāfiya]    → absolute-genus negation
<ikoraAha [N, ikrāh]         → "compulsion" (acc. to negated-genus rule)
fiY [P]  {l d~iyni [DET N]   → "in the religion"
qad [CERT] t~abay~ana [V]    → "indeed has-become-clear" (past perfect)
{l r~u$odu [DET N]           → "the right-guidance"
mina {lo gaY~i [P DET N]     → "from the delusion/error"
```

The verse uses **maximum-absolute negation** (*lā al-nāfiya li-l-jins*)
to deliver the strongest possible categorical claim available in
Classical Arabic grammar. Critical for later Islamic legal/political
discourse: the claim is not merely "this compulsion is not right" but
"no compulsion of any kind exists / is permitted / belongs-in the
religion." The grammar forecloses interpretive attempts to scope-
restrict.

The verse continues with a second negation: *mani yakfur bi-l-ṭāghūt
wa-yuʾmin bi-llāhi fa-qad istamsaka bi-l-ʿurwati al-wuthqā **lā**
infiṣāma lahā* — "has grasped the firmest handhold, **no** breaking of
it." The second *lā* is the same genus-negation construction (the
knot has no-breaking-whatsoever). The verse is structured as a
**double absolute-genus negation** — compulsion is absolutely negated
at the start, cleavability is absolutely negated at the end. The
positive content (*tabayyana al-rushdu mina al-ghayy*, "right has
become clear from error") is sandwiched between two categorical
negations. This is the Quran's rhetorical signature: assert by
bracketing within impossibility.

---

## 9. *ghayr* at Al-Fātiḥa 1:7 — the Quran's opening ghayr

Q 1:7 closes the Quran's first surah: *ṣirāṭa lladhīna anʿamta
ʿalayhim **ghayri** al-maghḍūbi ʿalayhim wa-lā al-ḍāllīn* — "the path
of those whom You have blessed, **not** of those upon whom wrath is
brought nor of those gone astray."

The Quran's first negative particle is **ghayr** (not *lā*).
Token-by-token:

```
Sira`Ta                N   (the path of)
{l~a*iyna              REL (those who)
>anoEamota             V   (You have blessed)
Ealayohimo             P   (upon them)
*gayori                N   (other-than / not-of)    ← the negation
{lo magoDuwbi          N   (those-with-wrath-upon-them)
Ealayohimo             P   (upon them)
wa laA                 CONJ NEG  (and not)           ← second negation
{l D~aA^l~iyna         N   (the astray)
```

The surah pivots on **two successive negations of the final noun-
phrase**. *ghayr* is exceptive-nominal; *wa-lā* is reinforcing-
particle negation. The classical question — which tafsir consumes
considerable energy on — is whether the two negated categories
(maghḍūb / ḍāllīn) are **the same group under different descriptions**
or **two distinct groups**. Al-Ṭabarī (cf. *Jāmiʿ al-Bayān*) collects
hadith identifying *al-maghḍūb ʿalayhim* with the Jews and *al-ḍāllīn*
with the Christians (Tirmidhī, *Jāmiʿ* 2954). Al-Rāzī in *Mafātīḥ
al-Ghayb* prefers a non-ethnic reading: *maghḍūb* = those who know
the truth and reject it; *ḍāllīn* = those who seek the truth and miss
it. Al-Zamakhsharī treats *ghayr* here as exceptive-appositional — the
two negative categories specify who "those You have blessed" are
**not**. Either reading, the grammatical structure is: the surah's
final rhetorical move is **double negation of two opposite failures
of worship** (knowing-rejection and unknowing-miss).

This is, at minimum, a remarkable structural fact: the Quran's opening
surah ends with a double-negation, and uses *ghayr* as its primary
negator rather than any particle from the main NEG inventory. *ghayr*
only 147 times across the whole Quran, but it leads the opening.

---

## 10. *fa-lā uqsimu* — the oath paradox

Eight verses in the Quran open with **lā + uqsimu** (root qsm, "to
swear"):

- Q 56:75 *fa-lā uqsimu bi-mawāqiʿi al-nujūm* (positions of the stars)
- Q 69:38 *fa-lā uqsimu bi-mā tubṣirūn*
- Q 70:40 *fa-lā uqsimu bi-rabbi al-mashāriqi wa-l-maghārib*
- Q 75:1 *lā uqsimu bi-yawmi al-qiyāmah*
- Q 75:2 *wa-lā uqsimu bi-l-nafsi al-lawwāmah*
- Q 81:15 *fa-lā uqsimu bi-l-khunnas*
- Q 84:16 *fa-lā uqsimu bi-l-shafaq*
- Q 90:1 *lā uqsimu bi-hādhā al-balad*

**Grammatical puzzle.** "I do **not** swear by…" looks like it means
"I decline to swear." But in every case the following content *is* an
oath — stars, the Day of Resurrection, the shifting stars, the sunset
glow, the self-reproaching soul, the city (Mecca). Classical grammar
has three readings:

1. *lā* is **pleonastic** (*lā zāʾida*) — the particle adds nothing
   semantic; the meaning is simply "I swear." This is the majority
   Basran reading (Ibn Hishām *Mughnī* §lā, type 4).
2. *lā* is **negating an implicit prior question** — "[no, stop
   disputing,] I do swear". A discourse-level anaphoric *lā*.
3. *lā* is **emphatic** — the negation amplifies the oath, on the
   logic that "what I am about to swear by is so obvious it does not
   even need a swearing." This is al-Zamakhsharī's preferred reading
   and the more rhetorical-theological one.

The distribution of these eight verses is itself striking: seven of
the eight are **late Meccan** (56, 69, 70, 75 twice, 81, 84) and one
(Q 90:1) is **very early Meccan**. All eight introduce cosmic or
eschatological oaths. **There is no *fa-lā uqsimu* in any Medinan
surah** — this is a Meccan rhetorical device, tied to the oath-cluster
style of the Quran's middle period. The construction is puzzling
because it places the grammatical paradox at the oath's head: the oath
must resolve the negation to be intelligible. The reader is made to
do grammatical work at the moment of entering a cosmic oath. Classical
*bāb al-qasam* chapters (Ibn Qayyim's *Tibyān fī Aqsām al-Qurʾān*)
treat these eight instances as a self-contained rhetorical family.

---

## 11. Negation at ring-centers

For the 4 Bonferroni-surviving sub-surah rings plus Hud (per
`/findings/phase-c-structures/ring-center-semantics.md`):

| ring | center verse(s) | negation tokens at center |
|---|---|---|
| Al-Baqarah 131-144 (z=+9.69) | v137 | — |
|  | v138 | — |
|  | **v143** | **mā ×2** ("the Qibla that you were on … *mā kānat* / *mā kāna* …") |
| Al-Qamar 21-30 (z=+6.46) | v25 | — (rhetorical Q: *a-ulqiya l-dhikru ʿalayhi min bayninā*) |
|  | v26 | — |
| ʿAbasa 1-9 (z=+6.09) | v5 | — (*ammā man istaghnā* — conditional, positive) |
| Al-Kahf 83-91 (z=+5.19) | v87 | — |
| **Hud (whole)** | v62 | — (Thamūd rejecting Ṣāliḥ: rhetorical Q, no NEG token) |

**Result: 1 of 5 Bonferroni ring centers (20%) contains a NEG-tagged
token**, specifically Al-Baqarah 2:143. This is **below the Quran-wide
NEG-verse base rate** (2688 NEG tokens / 6236 verses ≈ 43% of verses
contain at least one NEG; we'd expect 2 of 5). The ring-center
structural pivot does *not* consistently use negation as its
morphology.

However:

- **2:143** uses *mā kāna* — the humility-formula of §5 — at the Qibla
  pivot: "and We did not make the Qibla you were on except to know…"
  The negation is humility-of-purpose.
- **Three of the five centers carry a rhetorical question instead**
  (2:138 *man aḥsanu*, 54:25 *a-ulqiya*, 11:62 *a-tanhānā*). The ring
  structurally-marked moment is **interrogative, not negative** — a
  finding from the rhetorical-questions agent (§4).
- **ʿAbasa 80:5**'s *istaghnā* is a *positive* verb ("made himself
  self-sufficient") — and the ring structurally exposes it as a
  negative moral act through its positioning (the beggar Ibn Umm
  Maktūm comes, and the Prophet turns to the self-sufficient
  stranger). The ring draws a moral negation without grammatical
  negation.

**Novel finding.** Rings and questions cluster (p ≈ 0.012, not
pre-registered; see rhetorical-questions.md §4). Rings and negations
do not — and when they co-occur (2:143), the negation is the *mā
kāna li-X* humility-formula, the most oblique of all Quranic
negation-forms. **The ring-center's argumentative mode is question,
not negation.**

---

## 12. Cross-references to paired opposites

Negation and antithesis are closely related. The paired-opposites
work (`paired-opposites-network.md`) found that 20 of 27 antonym pairs
are significantly enriched in same-verse co-occurrence. Several of
those opposite-pairs are *themselves grammatically structured around
negation*:

- **faith_vs_disbelief** (Amn/kfr): the root *kfr* means "to cover /
  to deny / to reject" — it is **lexical negation incorporated into a
  trilateral**. 465 verses contain *kfr*; the overwhelming majority
  contrast with *Amn*.
- **truth_vs_falsehood** (Ḥqq/bṭl): *bāṭil* is "that which is null/
  void" — semantically a nominal negation of *ḥaqq*. 34 verses.
- **light_vs_darkness** (nūr/ẓlm): *ẓulumāt* derives from *ẓlm* = "to
  wrong/injure/darken" — its grammatical register is *intensive
  negation of light*.

Additionally, the *paired-opposites* agent's §7 finding — that
**mercy/wrath and reward/punishment co-occur at or BELOW chance** —
fits the negation picture. These opposites are grammatically
separated: mercy is stated without its antonym in the same verse
(the Quran's anti-Manichean prose). The Quran's negation grammar
tends to *not* stage mercy-vs-wrath inside the same breath; that
contrast is assembled by the reader across adjacent verses.

Where the Quran does stage antithesis inside one verse (east/west,
sun/moon, secret/open, ease/difficulty), the staging uses *wa-* or
*aw-* conjunctions rather than an explicit negation. Negation and
antithesis are **overlapping but non-identical** rhetorical channels.

---

## 13. *mā lakum min ilāhin ghayruhū* — the prophetic refrain

A specific formula that combines *mā*, *min* (partitive), *ilāh* (god),
and *ghayr* (exceptive): "you have no god **other than** Him."
9-fold occurrence (verbatim or near-verbatim) across the prophets:

- Noah: Q 7:59, Q 11:25-26, Q 23:23
- Hūd: Q 7:65, Q 11:50
- Ṣāliḥ: Q 7:73, Q 11:61
- Shuʿayb: Q 7:85, Q 11:84
- (also Q 23:32 attributed)

Pharaoh then **inverts** the formula at Q 26:29 and Q 28:38:
*la-ittakhadhtu ilāhan ghayrī* — "I shall take a god **other than
me**." The *ghayr* particle appears on both sides of the prophetic
controversy: prophets use *ghayr* to deny plurality, Pharaoh uses
*ghayr* to usurp divinity.

This is catalogued as a closed formulaic family in our intra-Quranic
cross-reference agent; here the point is that **ghayr** specifically
is the grammatical operator the Quran assigns to the monotheism
debate. *ghayr* (147 tokens total) is used in the single most-
repeated theological formula in prophetic-narrative (9 instances of a
single phrase), but also in Fātiḥa's closing, and also in Pharaoh's
imperial inversion. *ghayr* is the particle of **theological
otherness**: the exceptive-nominal that draws the boundary between
the true God and the false alternatives.

---

## 14. Novel observations

Summarising what this inventory found that I have not seen reported:

1. **The Quran's default Shahāda form is *lā ilāha illā huwa* (30
   instances), not *lā ilāha illā Allāh* (2 instances).** Popular
   ritual practice inverts the Quranic distribution. The *huwa*
   version is the text's native form.

2. **Al-Ikhlāṣ packs 3 *lam* past-tense negations into 2 verses (vv 3-
   4), delivering the densest apophatic grammar in the Quran**. The
   whole theological meaning of the surah is carried by 3 instances
   of the same particle, three different negated verbs.

3. **Q 2:256's "lā ikrāha" uses the strongest absolute-genus
   negation available in classical grammar**, and the verse is
   bracketed between two such negations (ikrāh at start, infiṣām at
   end). The categorical scope is grammatical, not merely rhetorical.

4. **Ring-centers prefer rhetorical questions over negations as their
   structural-pivot device.** Only 1 of 5 Bonferroni rings has a
   NEG-tagged token at center — below base rate. Negation-and-
   questioning are *both* rhetorical marking devices, but the Quran
   assigns each to a different structural role.

5. **The *ghayr* particle carries the Quran's monotheism debate.**
   Fātiḥa 1:7 (exclusion from blessed path), 9 prophetic refrains
   (*mā lakum min ilāhin ghayruhū*), and Pharaoh's 2 imperial
   inversions together saturate the textual function of *ghayr*
   with theological-boundary work. The nominal-exceptive particle
   is grammatically where the monotheism question happens.

6. **Meccan/Medinan divergence of *lan*.** Every other negation
   particle is Meccan-tilted; *lan* alone is Medinan-tilted (54.7%).
   The particle of absolute-future negation is *law*-inflected by
   community-covenantal discourse.

7. **Declarative *lā* outnumbers prohibitive *lā* 4.2:1.** The Quran's
   *lā* is overwhelmingly polemical-descriptive ("they do not know"),
   not legal-prescriptive ("do not do X"). Command-lā is the minor
   register. This may be the text's single most under-appreciated
   asymmetry.

8. **The 11 zero-negation surahs are all short Meccan.** They are
   doxological/eschatological/declarative — and the absence of
   negation is itself a structural marker of that genre.

9. **Āyat al-Kursī stacks four *lā* + one *illā* in 50 words.** The
   verse's structural grammar is a negation-cascade terminating in a
   restriction-to-divine-will, then opening to a kataphatic knowing-
   statement, then closing with a final "does not burden Him."

10. **The *fa-lā uqsimu* oath-paradox is a Meccan-only device (8/8
    instances).** It disappears entirely from Medinan discourse.

---

## 15. Classical prior art

- **Ibn Hishām, *Mughnī al-Labīb***, under entry *lā* (types 1-6),
  *mā* (types 1-5), *lam*, *lan*, *laysa*, *ghayr*, and the entry on
  pleonastic *lā*. The canonical classical reference.
- **Al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān***, **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 57" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; nawʿ number retagged per MW-6 mechanical scan; substantive classical doctrine unchanged; statistical finding unaffected; candidate correct locus: nawʿ 32 *al-adawāt* pending Phase-2 secondary-triangulation]** *al-ḥurūf
  al-nafī* — dedicates a chapter to Quranic negation particles.
- **Al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān***, multiple nawʿ entries
  on particle usage.
- **Al-Zamakhsharī, *al-Kashshāf***, on Q 7:143 *lan tarānī* (the
  Muʿtazilī reading that *lan* is perpetual, rebutted by Sunnī
  orthodoxy) and on Q 56:75 *fa-lā uqsimu* (emphatic-negation
  reading).
- **Al-Rāzī, *Mafātīḥ al-Ghayb***, on Q 1:7 *ghayr al-maghḍūb*
  (non-ethnic reading) and Q 2:256 *lā ikrāha* (absolute-genus scope).
- **Ibn Qayyim al-Jawziyya, *al-Tibyān fī Aqsām al-Qurʾān***, on the
  *fa-lā uqsimu* oath family.
- **Ibn Taymiyya**, on declarative vs. prohibitive *lā* in legal
  exegesis.
- **Al-Jurjānī, *Dalāʾil al-Iʿjāz***, theoretical foundation for why
  particle choice is theologically consequential (each particle
  carries a distinct rhetorical force).

**Novel relative to classical:**

- Full computational inventory (2,688 NEG + 89 laysa + 147 ghayr +
  663 illā = 3,587 negation-bearing tokens) is not reported in any
  classical source.
- Meccan/Medinan distribution per particle, including *lan*'s Medinan
  tilt, is a modern computational observation.
- Ratio of declarative lā to prohibitive lā (4.2:1) is new.
- The Shahāda-formula distribution (30 *huwa* / 2 *Allāh* / 3 *ana* /
  1 *anta*) is a computational census.
- The negation-at-ring-centers result (20% vs. 43% base rate) is new.
- The 54-verse *mā kāna li-X* census is new.

---

## 16. Limitations

- **Morphology trust**: QAC v0.4 is near-complete but has known
  systematic edge-cases (e.g. the Al-Rahman refrain mis-tag in the
  rhetorical-questions agent). Our negation counts rely on its
  POS:NEG tagging + lemma-specific add-ons (laysa, ghayr). If a
  particle is mis-tagged elsewhere, our count is off by that amount.
- **Period classification**: Egyptian-standard Meccan/Medinan is the
  reference; alternative orderings (Nöldeke 4-phase) might shift
  per-period numbers at the margin.
- **The "divine-apophatic" filter** (§6) uses a simple heuristic
  (verse contains Allāh/huwa + lā + 3MS verb). This may count
  false positives (verses where the 3MS verb isn't God's) and miss
  false negatives (where the divine subject is implicit). A
  dependency-parse pass would tighten the count.
- **Nominal/exceptive negations not in POS:NEG** — our augmentation
  (laysa, ghayr, illā) is principled but selective; other
  constructions (e.g. *ladā* with negative semantic, compound
  prepositions) are not counted.
- **No pre-registration** for the ring-center and Meccan/Medinan
  statistical comparisons. Treat as exploratory.

---

## 17. Outputs

- `/findings/phase-b-hypotheses/negation-per-surah.csv` — 114 rows,
  per-surah counts of each particle, period, total negation, density.
- Journal: `/journal/negation-taxonomy-run-1.md`.

---

The Quran negates, on average, once every 2.35 verses. It has six
grammatical particles for doing so, each with its own tense-scope and
theological register. Its foundational creed is syntactically a
negation-exception (*lā…illā*). Its most famous "no compulsion" verse
uses the strongest-scope negation in the Arabic language. Its opening
surah ends with a double-negation of two opposite failures of worship.
Its shortest theological surah (Al-Ikhlāṣ) packs three past-tense
negations into two verses to define God by what He is not. And its
default Shahāda, in its native Quranic form, says *there-is-no-god
but-**He***, with the exception-pronoun doing the positive
work. Negation is not absence in this text; it is the grammar of its
theology.
