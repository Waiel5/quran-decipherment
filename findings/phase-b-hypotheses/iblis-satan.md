---
title: Iblīs / al-Shayṭān — Quranic Satanology
phase: B
agent: iblis-satan-run-1
date: 2026-04-12
inputs:
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt  (Leeds QAC v0.4)
  text: quran-text/quran-no-tashkeel.json
  translation: data/translations/en.sahih.txt
methods:
  primary: surface-string + proper-noun lemma match on the Leeds QAC (LEM:<iboliys,
    LEM:^ayoTAn), cross-checked against the Hafs Arabic text of quran-no-tashkeel.json
  secondary: collocation scans — shayṭān×ʿaduww, shayṭān×sulṭān, shayṭān×waswasa
  tertiary: manual classical-tafsir synthesis on the jinn/angel crux (Q 2:34 vs Q 18:50)
prior_findings:
  - findings/phase-b-hypotheses/quotation-analysis.md  (§6: four retellings)
  - findings/phase-b-hypotheses/mutashabih-lafzi.md    (prostration scene as mutashābih)
  - findings/phase-b-hypotheses/quran-bestiary.md      (jinn / angelic taxonomy)
  - findings/phase-b-hypotheses/paradise-hell-names.md (sabʿ abwāb, Q 15:44)
classical_priors:
  - al-Ṭabarī, Jāmiʿ al-bayān (ad Q 2:34, 7:11-18, 18:50)
  - al-Zamakhsharī, al-Kashshāf (ad Q 18:50)
  - al-Rāzī, Mafātīḥ al-ghayb (ad Q 7:12 — the fire/clay syllogism)
  - Ibn Taymiyya, Majmūʿ al-fatāwā vol. 4 (Iblīs as jinn, not fallen angel)
  - Ibn Kathīr, Tafsīr (ad Q 2:34, Q 18:50)
  - al-Suyūṭī, al-Durr al-manthūr (ad Q 38:75)
etymology_priors:
  - Arthur Jeffery, The Foreign Vocabulary of the Qurʾān (1938), s.v. Iblīs
  - A. J. Wensinck, "Iblīs," EI² (entry accepts Greek διάβολος > Syriac dīābōlōs > Ibl(ī)s)
  - Kevin van Bladel, "Heavenly Cords and Prophetic Authority in the Qurʾān"
scripts:
  - /tmp/iblis_scan.py (proper-noun extraction)
  - /tmp/shayTaan_count.py (singular/plural counting, enemy co-occurrence)
---

# Iblīs and al-Shayṭān — A Quranic Satanology

The Quran's doctrine of evil is built on two lexemes — the proper name **Iblīs**
and the common noun **al-shayṭān** ("the Adversary") — whose distributions, speech
events, and theological functions differ in ways the tafsīr tradition has found
endlessly generative. Iblīs is a character: named eleven times, scripturally
located at one moment (the refusal to prostrate to Adam), endowed with speech in
four — arguably five — dialogic scenes, and given one final utterance at the
end of the world (Q 14:22). *Al-shayṭān* is a role: sixty-nine singular-token
appearances across fifty-nine verses naming a functional adversary of humankind,
plus sixteen plural tokens (*shayāṭīn*) of uncertain reference. The two lexemes
are not synonyms. Iblīs is what the being is called when God addresses him by
name; al-shayṭān is what he is called when he acts upon humans.

This file maps that distribution, analyses the four retellings of the refusal
scene side-by-side, surveys *waswasa* (whispering) language, reads the
eschatological confession of Q 14:22, and adjudicates the classical debate
triggered by the verse-internal contradiction between Q 2:34 ("the angels …
except Iblīs") and Q 18:50 ("he was of the jinn").

---

## 1. Iblīs — the 11 named mentions

Iblīs (إبليس) appears exactly **eleven times** in the Hafs Quran. The QAC
morphology tags every occurrence as a proper noun (POS:PN) with no triconsonantal
ROOT attribute — a grammatical fingerprint of foreign provenance.

| # | Passage | Context | Speech? |
|---:|---|---|---|
| 1 | **Q 2:34**  | "…all prostrated except Iblīs; he refused and was arrogant (*abā wa-stakbara*)" | No |
| 2 | **Q 7:11**  | "…except Iblīs; he was not of those who prostrated" | Speech follows (7:12-17) |
| 3 | **Q 15:31** | "…except Iblīs; he refused to be with those who prostrated" | Speech follows (15:33-39) |
| 4 | **Q 15:32** | "*yā Iblīs*, what is the matter…" (divine vocative) | Divine address |
| 5 | **Q 17:61** | "…except Iblīs; he said, 'Shall I prostrate…?'" | Speech internal |
| 6 | **Q 18:50** | "…except Iblīs; **he was of the jinn** (*kāna min al-jinn*)" | No |
| 7 | **Q 20:116**| "…except Iblīs; he refused" | No |
| 8 | **Q 26:95** | "…and the **armies of Iblīs** all together" (hellfire scene) | No |
| 9 | **Q 34:20** | "Iblīs had already confirmed his conjecture against them" | No |
| 10| **Q 38:74** | "…except Iblīs; he was arrogant and became a disbeliever" | Speech follows (38:76-82) |
| 11| **Q 38:75** | "*yā Iblīs*, what prevented you…" (divine vocative) | Divine address |

Two observations. First, **nine of the eleven occurrences cluster around the
prostration scene**. The two exceptions — Q 26:95 ("the armies of Iblīs") and
Q 34:20 ("Iblīs confirmed his conjecture") — are both retrospective summaries of
the consequences of that same scene. Iblīs the proper noun is *scripturally
monovalent*: it always refers to and presupposes that one original event.
Second, **both direct vocatives** (*yā Iblīs*, Q 15:32 and Q 38:75) belong to
**God, not to humans**. No Quranic human ever addresses him by name. Humans
interact only with *al-shayṭān*. This is the foundational lexical split that
governs everything below.

### 1.1 Etymology and the ABL root

The root *A-B-L* (ء-ب-ل) in Arabic denotes camels, not despair — the classical
lexicographers' attempt to derive Iblīs from native *ablasa* ("to despair")
yields the elegant but doubtful sense "the despaired-of-mercy one." Arthur
Jeffery (1938) and subsequent Semiticists trace Iblīs through Syriac
*dīābōlōs* — itself a loan from Greek διάβολος ("slanderer, adversary"). The
initial *d-* is lost in Syriac orthography when the word is treated as a prefix
or pronounced with elision. Iblīs would thus be a **calque-by-phonetic-attrition**
of the same word that gives us *devil* through Latin *diabolus*. This is
consistent with the QAC's PN-without-ROOT tagging: the morphology database
refuses to assign an Arabic triconsonantal root because none exists.

---

## 2. The four retellings of the refusal scene — a side-by-side

The prostration-refusal scene is narrated with a complete dialogic arc four
times: Q 7:11-18, Q 15:28-44, Q 17:61-65, Q 38:71-85. Q 2:30-38 and Q 20:115-123
narrate the *consequences* (the Fall, the eviction) but skip Iblīs's speech.
The four-way dialogic parallel is the classic *mutashābih-lafẓī* problem:
nearly-identical speech repeated with systematic variation.

### 2.1 Shared skeleton

All four instances instantiate the same seven-move dialogue:

1. **Command.** God commands the angels to prostrate to Adam.
2. **Compliance + exception.** All prostrate except Iblīs.
3. **Interrogation.** God asks Iblīs what prevented him.
4. **Iblīs's self-justification.** Material superiority / honour-argument.
5. **Sentence.** "Get out" (*ikhruj / ihbiṭ*).
6. **Respite plea.** Iblīs asks to be reprieved until the Day.
7. **Grant + threat.** God grants the respite; Iblīs announces his programme.

### 2.2 Move-by-move comparison

| Move | Q 7:11-18 | Q 15:28-44 | Q 17:61-65 | Q 38:71-85 |
|---|---|---|---|---|
| Prelude to command | — | "I am creating a human from clay from altered black mud" (15:28) | — | "I am creating a human from clay" (38:71) |
| Interrogation-verb | *mā manaʿaka* (7:12) | *mā laka* (15:32) | (no explicit question) | *mā manaʿaka* (38:75) |
| Iblīs's reason | "I am better than him (*anā khayr minhu*). You created me from fire and him from clay" (7:12) | "I will not prostrate to a human You created from clay from altered black mud" (15:33) | "Shall I prostrate to one You created from clay?" (17:61) | "I am better than him. You created me from fire and him from clay" (38:76) |
| Sentence | "So descend from it (*fa-hbiṭ*) … you are of the debased" (7:13) | "So get out, for you are expelled (*rajīm*); upon you is the curse until the Day of Recompense" (15:34-35) | "Go (*idhhab*); whoever follows you…" (17:63) | "So get out, for you are expelled; upon you is **My** curse until the Day of Recompense" (38:77-78) |
| Respite formula | "Reprieve me until the Day they are resurrected" (7:14) | identical (15:36) | "If You delay me until the Day of Resurrection, I will surely destroy his descendants…" (17:62) | identical (38:79) |
| Respite granted | "Indeed, you are of those reprieved" (7:15) | identical + "until the day of the time well-known" (15:37-38) | implicit | identical + "until the day of the time well-known" (38:80-81) |
| Programme / oath | "Because You have put me in error (*bimā aghwaytanī*), I will sit in wait for them on Your straight path, from before and behind and right and left" (7:16-17) | "My Lord, because You have put me in error, I will make [evil] attractive to them and mislead them all" (15:39) | "I will destroy (*la-aḥtanikanna*) his descendants…" (17:62) | "**By Your might** (*bi-ʿizzatika*), I will surely mislead them all" (38:82) |
| Exception clause | "and You will not find most of them grateful" (7:17) | "except Your chosen servants (*al-mukhlaṣīn*)" (15:40) | "except a few (*illā qalīlan*)" (17:62) | "except Your chosen servants (*al-mukhlaṣīn*)" (38:83) |
| Counter-threat | "I will fill Hell with you and those who follow you" (7:18) | "Hell is the promised place for them all. It has seven gates" (15:43-44) | "Hell will be your recompense, an ample recompense" (17:63) | "I will fill Hell with you and those of them that follow you" (38:85) |

### 2.3 What the four-way comparison yields

(a) **Two macro-clusters.** Q 7 and Q 38 share the pride-argument verbatim
(*anā khayr minhu; khalaqtanī min nārin wa-khalaqtahu min ṭīn*). Q 15 and Q 38
share the sentence-formula (*fa-khruj minhā fa-innaka rajīm*) and the "chosen
servants" exception. Q 7 is the most dramatically staged, Q 15 the most
cosmologically framed (it ends with the seven gates of Hell), Q 17 the most
telegraphic, Q 38 the most emotive (Iblīs swears an oath *bi-ʿizzatik* — by
God's own attribute).

(b) **The honour-argument is invariant across three retellings.** Iblīs's core
accusation — that God Himself caused his fall (*bimā aghwaytanī*, "because You
put me in error") — appears in Q 7:16, Q 15:39, and implicitly in Q 38:82;
Q 17:62 stops short of it. This is not small: it is the theological flashpoint
of the entire episode. Al-Rāzī devotes a long commentary to the logic of the
objection, labelling it *al-qiyās al-fāsid* (faulty analogy) — Iblīs reasons
from material ontology (fire vs. clay) to spiritual hierarchy, a category
error. God's reply addresses not the fire-clay claim but the presumption of
the question itself.

(c) **The sentence-language differs.** Q 7 uses *hbiṭ* ("descend," the same
verb used for Adam's expulsion in Q 2:36); Q 15 and Q 38 use *khruj* ("get
out"); Q 17 uses *idhhab* ("go"). The Quran does not standardise the verb of
expulsion. This is the fingerprint of oral re-performance, not of stenographic
record-keeping.

(d) **The threat-programme shifts register.** Q 7 is *militaristic* (ambush
from four sides); Q 15 is *cosmetic* (making evil attractive, *zayyana*);
Q 17 is *reproductive* (destroying descendants, *aḥtanika*); Q 38 is *oathed*
(swearing by God's attribute). The four retellings do not merely re-tell — each
accents a different *modality of temptation*, matching the surah's surrounding
theme. Q 7, the fullest narrative, gives the military frame; Q 15, the surah
that ends with the seven gates of Hell, gives the cosmological frame; Q 17, the
surah of the night journey and the children of Israel, emphasises the
generational frame; Q 38, a surah densely engaged with prophet-dialogues with
God, gives the oath-frame.

**Verdict**: one event, four refractions. The variance is *theologically
motivated*, not textual accident.

---

## 3. Iblīs's speech patterns — *mādhā qāla lahum X?*

Across the 48 Satanic speech-events catalogued in the quotation-analysis run,
Iblīs / al-shayṭān's speech splits into **four rhetorical modes**:

| Mode | Addressee | Specimen | Grammatical marker |
|---|---|---|---|
| (a) Self-justification to God | Allah | "*anā khayr minhu*" (7:12, 38:76) | Declarative + comparative |
| (b) Petition to God | Allah | "*rabbi fa-anẓirnī*" (15:36, 38:79) | Vocative *rabbi* + imperative |
| (c) Threat/programme announced to God | Allah | "*la-aqʿudanna / la-uzayyinanna / la-uḍillannahum*" (7:16, 15:39, 38:82) | Emphatic nūn on future verbs |
| (d) Whisper-speech to humans | Adam / believers | "*yā Ādam hal adullu-ka…*" (20:120) | Vocative + soft question |
| (e) Post-mortem disavowal | Hell-dwellers / those who followed him | "*innī barīʾun minkum*" (8:48, 59:16), "*mā kāna lī ʿalaykum min sulṭān*" (14:22) | *Barāʾa*-formula + *sulṭān*-denial |

The transition from mode (c) to (d) is the pivot of Quranic satanology. In the
heavenly court Iblīs is loud, swearing, combative; on earth he is a whisperer.
The grammatical lexicon of modes (c) and (d) have almost no overlap: the
emphatic-nūn oath (*la-uḍillannahum*) gives way to the gentle question
(*hal adulluka*). One voice of Satan speaks in the presence of God; a different
voice speaks in the presence of humans. Mode (e) — post-mortem — is a third
voice, discussed in §7.

---

## 4. Classical debate — is Iblīs jinn or angel?

The text **states both**.

- Q 2:34, Q 7:11, Q 15:30-31, Q 17:61, Q 18:50, Q 20:116, Q 38:71-74:
  "the angels prostrated … except Iblīs" — the exception (*istithnāʾ*) from
  "angels" ordinarily entails that Iblīs was one of them.
- Q 18:50: "…except Iblīs. **He was of the jinn** (*kāna min al-jinn*); he
  disobeyed the command of his Lord."

The Quranic formulation of the exception leaves two grammatical readings, and
the four major tafsīr positions map precisely onto them:

### 4.1 The *istithnāʾ muttaṣil* reading — Iblīs was an angel

Held by **al-Ṭabarī, al-Zamakhsharī, Ibn ʿAbbās, Ibn Masʿūd**, and by most
Muʿtazilī and early Ashʿarī commentators. On this reading:

- The natural Arabic grammatical default of the exception (*illā Iblīsa*)
  following "the angels" is *muttaṣil* — "connected" — i.e., Iblīs is of the
  excepted set.
- The term *jinn* in Q 18:50 is read as a sub-category of angels, those made
  of fire (since angels are elsewhere said to be made of light); on this view
  the *jinn* of 18:50 are a specific angelic tribe, not the separate class of
  spirits.
- Iblīs's claim in Q 7:12 / 38:76 that he is made of *nār* (fire) rather than
  *ṭīn* (clay) fits both readings — angels and jinn alike are non-clay beings.

Difficulty: this contradicts the broader Quranic doctrine of angelic
impeccability (Q 16:50, Q 66:6 — "they do not disobey Allah in what He
commands them"), which is usually taken to be constitutive of *malāʾika* as
such. Al-Zamakhsharī's Muʿtazilī solution is to weaken angelic impeccability
to *contingent* (they *could* disobey but don't) — a position later Ashʿarīs
rejected.

### 4.2 The *istithnāʾ munqaṭiʿ* reading — Iblīs was jinn, present at court

Held by **Ibn Taymiyya, Ibn Kathīr, al-Ḥasan al-Baṣrī, Qatāda**, and by most
later Ashʿarī and Salafī commentators. On this reading:

- The exception is "disjunctive" (*munqaṭiʿ*) — Iblīs is grammatically excepted
  not because he is an angel but because he was present *with* the angels at
  the scene of command; the *illā* functions adversatively ("but not Iblīs") as
  elsewhere in Arabic.
- Q 18:50's *kāna min al-jinn* is read as a categorical statement: he was of
  the separate ontological class called jinn, not of the angels.
- The angels' impeccability is preserved intact.
- The jinn's capacity for disobedience, their creation from *nār al-samūm* (Q
  15:27), and their being the progeny of a fallen Iblīs (implied in Q 18:50's
  "him and his descendants") all cohere.

Al-Ḥasan al-Baṣrī's often-quoted formulation: "Iblīs was never an angel, not for
the blink of an eye" (*mā kāna iblīsu min al-malāʾikati ṭarfata ʿaynin qaṭṭ*).
This reading won the majority consensus from roughly the fifth Hijri century
onwards and is the standard Sunni position today.

### 4.3 Tertiary readings

- **The "Gender-differentiated" reading** (al-Suyūṭī citing weak *isrāʾīliyyāt*):
  Iblīs was an angel who later became a jinn; his metaphysical substance changed
  when he rebelled. This exists in some *qiṣaṣ al-anbiyāʾ* literature but has no
  Quranic anchor.
- **The "ambiguity-is-deliberate" reading** (modern exegetes including Fazlur
  Rahman and Muhammad Asad): the Quran's surface-level both-and is theologically
  productive — it destabilises the angel/jinn binary in order to name the
  ontological anomaly of a being whose free will *from within a category of
  pure obedience* was the first sin.

The finding-file position: the *munqaṭiʿ* reading is better supported by Q 18:50
read literally, while the *muttaṣil* reading is better supported by the
grammatical default of Arabic exception. Both sides are doing legitimate work;
the text resists resolution by design.

---

## 5. *Shayāṭīn* — who are the Devils (plural)?

*Shayāṭīn* (plural) occurs in **sixteen verses**. The referents subdivide into
**four classes**, not always easily separable:

1. **Cosmological evil spirits pelted from heaven**
   - Q 15:17-18, Q 37:6-10, Q 67:5, Q 72:8-9 — "We have adorned the lowest
     heaven with stars … and protection against every rebellious *shayṭān*…
     except one who snatches [a word] by theft, and a piercing flame pursues
     him." These are the *shayāṭīn mardatun* ("rebellious devils") of Q 37:7.
     Their function is cosmological: they try to eavesdrop on the *malaʾ al-aʿlā*
     (the exalted assembly) and are driven off by shooting stars (*shuhub*).

2. **Servants of Solomon**
   - Q 21:82, Q 38:37-38 — "And of the *shayāṭīn* were those who dived for him
     and did other work … they made for him what he willed: sanctuaries, statues,
     basins like reservoirs, cauldrons." These are subjugated jinn, labourers of
     the Solomonic corvée. Their labelling as *shayāṭīn* is striking; it
     preserves the "Devil"-register even while domesticating them.

3. **Teachers of magic**
   - Q 2:102 — "They followed what the *shayāṭīn* had recited during the reign
     of Solomon … they disbelieved, teaching people magic." Here *shayāṭīn* are
     literary adversaries whose curriculum is *siḥr* — magic.

4. **Human-and-jinn tempters, plural**
   - Q 6:112 — "We made for every prophet an enemy, *shayāṭīn* of mankind and
     jinn" (*shayāṭīna l-insi wa-l-jinn*). This is the explosive verse: the
     Quran **names human shayāṭīn**. *Shayṭān* is here a *function* — adversary
     of prophets — realisable in either class of creature.
   - Q 2:14 — "When they are alone with their *shayāṭīn* they say, 'We are with
     you.'" The hypocrites' *shayāṭīn* are their human patrons.
   - Q 7:27, Q 7:30, Q 19:83, Q 22:3, Q 23:97, Q 26:210-212, Q 26:221, Q 6:121 —
     the "tribe" of Iblīs, sent on the disbelievers.

The Quran does **not** explicitly say the plural *shayāṭīn* are Iblīs's
biological descendants, but Q 18:50 names *him and his descendants* (*dhurriyyatahu*)
as enemies to humankind, and Q 26:95 mentions the *junūd Iblīs* (Iblīs's
armies). The classical tafsīr synthesis (al-Ṭabarī, Ibn Kathīr ad Q 18:50)
thus reads the *shayāṭīn* as the progeny of Iblīs plus allied human tempters
plus cosmological jinn who have taken up his cause — a coalition, not a lineage.
The term's elasticity is load-bearing: **any entity that performs the adversary
function against a prophet or believer is, in the Quran's idiom, a shayṭān**,
and this function extends to humans explicitly (Q 6:112).

---

## 6. *Waswasa* — the whispering

The root W-S-W-S ("whisper, murmur") occurs in five Quranic verses, and every
one of them is either Satanic in agent or interior-to-the-self:

| Verse | Agent | Target | Content |
|---|---|---|---|
| Q 7:20 | al-shayṭān | Adam + Ḥawwāʾ (both) | "Your Lord did not forbid you this tree except that you become angels or immortals" |
| Q 20:120 | al-shayṭān | Adam (singular) | "O Adam, shall I direct you to the tree of eternity and possession that never decays?" |
| Q 50:16 | the self (*nafs*) | the person herself | inner whisper, counterweight to "We are closer to him than the jugular vein" |
| Q 114:4 | *al-waswās al-khannās* | humankind (breasts) | the content unspecified |
| Q 114:5 | "who whispers in breasts of men" | humankind | same |

Two notes of the first importance. First, **Q 50:16 makes *waswasa* a property
also of the *nafs***: the soul itself whispers. This is why some *tafsīr*
traditions (and all Sufi traditions) treat the satanic *waswasa* as
indistinguishable phenomenologically from the *nafs ammāra bi-l-sūʾ* (Q 12:53)
— the inner voice and the outer whisperer operate on the same frequency.
Q 114's *min al-jinnati wa-l-nās* ("from jinn and humankind") extends the
whisperer-category to humans again, paralleling the *shayāṭīn al-ins* of Q
6:112. The *waswāṣ khannās* (the retreating whisperer) of the surah's climax
is the perfect compressed icon of satanology: whispers, then hides; strikes,
then disappears. *Khannās* derives from a root denoting *retreat* — the
adversary who flees when the divine name is invoked.

Second, the **Adam-temptation *waswasa* of Q 7:20 and Q 20:120 is delivered in
complete sentences**, quoted verbatim, with a named interlocutor (*yā Ādam*).
It is not a sub-audible murmur — it is structured deceptive speech. The
"whispering" metaphor describes the *modality* (secret, private, bypassing
the reasoning) rather than the phonetic form. This is relevant to the *sulṭān*
question (§7): Iblīs has no coercive *authority*, only whispered suggestion.

---

## 7. Q 14:22 — the eschatological confession

> *wa-qāla l-shayṭānu lammā quḍiya l-amru: inna Llāha waʿadakum waʿda l-ḥaqqi
> wa-waʿadtukum fa-akhlaftukum, wa-mā kāna lī ʿalaykum min sulṭānin illā an
> daʿawtukum fa-stajabtum lī; fa-lā talūmūnī wa-lūmū anfusakum.*

"And Satan will say, when the matter has been concluded: 'Indeed, Allah
promised you the promise of truth, and I promised you, and I broke my
promise to you. I had no authority over you (*mā kāna lī ʿalaykum min
sulṭān*) except that I called you, and you responded to me. So do not
blame me; blame yourselves.'" (Q 14:22)

This is the single most theologically compressed Satanic utterance in the
Quran. Its features:

- **Tense shift**. The main narrative frame is eschatological (*lammā quḍiya
  l-amru*, "when the matter has been concluded"); *qāla* is read as a prophetic
  past with future reference — Satan *will* say this on the Day of Judgement.
- **Structural parallel to Q 59:16** ("like the example of Satan, when he
  says to man 'Disbelieve,' then when he disbelieves says 'I am disassociated
  from you; I fear Allah, Lord of the worlds'") — the same disavowal-formula,
  compressed. The Q 14:22 version is the full-length aria.
- **The *sulṭān* clause**. "I had no authority over you except that I called
  you." This ratifies what Q 15:42 and Q 17:65 had already stipulated from the
  other side ("over My servants you shall have no *sulṭān*"): Satanic causation
  is **persuasive, not coercive**. Q 14:22 is Satan's own admission of this.
- **The blame-reversal**. "So do not blame me; blame yourselves." The Quranic
  Iblīs is not a cosmic counter-sovereign whose power was finally broken; he
  is a tempter who operated only with the consent of those who accepted his
  invitations. Q 14:22 retroactively voids all attempts to locate moral
  responsibility outside the sinning self.

This is the ultimate confession. The adversary who opened his career by
accusing God of having caused his fall (*bimā aghwaytanī*, Q 7:16) closes it by
telling humans they have no grounds to accuse him. The rhetorical symmetry is
devastating. The Quran's satanology **brackets** human history between two
speeches by the same speaker — pre-historical accusation of God, post-historical
exoneration of God — and the exoneration proves the accusation self-refuting.

---

## 8. "Take him as an enemy" — Q 35:6 and the *ʿaduww* formula

> *inna l-shayṭāna lakum ʿaduwwun, fa-ttakhidhūhu ʿaduwwan.*

"Indeed, Satan is to you an enemy, so take him as an enemy." (Q 35:6)

The Quran names Satan as *ʿaduww* (enemy) with startling frequency. The
co-occurrence scan of *al-shayṭān* with *ʿaduww* inside a single verse yields
**eleven verses**: Q 2:36, Q 2:168, Q 2:208, Q 6:142, Q 7:22, Q 12:5, Q 17:53,
Q 18:50, Q 20:117, Q 28:15, Q 35:6, Q 36:60, Q 43:62. In nine of these the
exact phrase is *ʿaduwwun mubīn* ("manifest / clear enemy").

Q 35:6 is the semantic climax of the formula because it adds an **imperative**:
*fa-ttakhidhūhu ʿaduwwan* ("so take him as an enemy"). The Quran requires of the
believer not merely a cognitive recognition of Satan's enmity but an *active
reciprocal enmity-stance*. This is the rare case where the Quran enjoins
*hatred* as a duty — explicitly, of Satan — and by the precise symmetry of the
verb (*takhidhū*, also the verb for taking something as a protector/*walī*)
positions anti-Satanic enmity as the exact inverse of Satanic alliance (*walī*,
Q 4:119, Q 7:27, Q 7:30). Either he is your *walī*, or he is your *ʿaduww*;
there is no neutral third. The rhetorical force is reinforced by the immediate
sequel: "He only calls his party (*ḥizbahu*) to be among the companions of the
Blaze" — Satan has a *ḥizb*, a party; the believer must be of the opposing
*ḥizb Allāh* (Q 5:56, Q 58:22).

---

## 9. Satanic titles — a lexical inventory

Beyond *al-shayṭān* the Quran deploys a vocabulary of descriptive titles, each
highlighting a different function:

| Title | Meaning | Occurrences | Function |
|---|---|---:|---|
| *al-shayṭān al-rajīm* | "the expelled / stoned Satan" | Q 3:36, 15:17, 15:34, 16:98, 38:77, 81:25 | expulsion / liturgical formula (*taʿawwudh*) |
| *al-waswās al-khannās* | "the retreating whisperer" | Q 114:4 | whisper-function |
| *al-ghurūr* | "the deceiver" | Q 31:33, 35:5, 57:14 | deception-function |
| *al-ʿaduww* / *ʿaduww mubīn* | "the (clear) enemy" | 11 verses incl. Q 35:6 | hostility-function |
| *ʿaduww muḍill mubīn* | "clear misleading enemy" | Q 28:15 | dual hostility + *iḍlāl* |
| *shayṭān mārid* | "rebellious devil" | Q 4:117, 22:3, 37:7 | cosmological rank |
| *al-mughrī* / implicit *aghwaytanī* | "the one who seduces to error" | Q 7:16, 15:39 etc. | agency of *ghawā* |
| *junūd Iblīs* | "the armies of Iblīs" | Q 26:95 | military-cosmological |
| *ḥizb al-shayṭān* | "the party of Satan" | Q 58:19 | political-cosmological |

The multiplication of titles is **not** redundant. Each title activates a
different theologeme: *rajīm* points to expulsion from the heavens and becomes
the refuge-word in *a-ʿūdhu bi-Llāhi min al-shayṭān al-rajīm*; *khannās* points
to the whispering function; *ghurūr* to deception; *ʿaduww* to enmity. The Quran
builds a polyvalent enemy — a single entity whose multiple titles sum into a
stable pastoral doctrine: *recognise him, refuse him, flee to God*.

---

## 10. Synthesis — eleven theses

1. Iblīs is the proper name of a being who refused to prostrate to Adam.
   Al-shayṭān is what he is called when he acts upon humans.
2. The name Iblīs is almost certainly a loan of Greek *diábolos* through
   Syriac — consistent with the Leeds QAC's refusal to assign it an Arabic
   triconsonantal root.
3. Iblīs's eleven named mentions all cluster around the prostration scene.
   He is, lexically, the being of that one event.
4. The four full retellings of that event (Q 7, 15, 17, 38) are one scene
   narrated four ways, with systematic variation matching each surah's theme.
   The pride-argument, the respite-petition, and the exception for "Your
   chosen servants" are near-invariant.
5. The grammatical crux of Q 2:34 vs. Q 18:50 is real, not apparent, and
   the classical tradition split evenly before settling on the *munqaṭiʿ*
   reading (Iblīs is jinn, was at the angelic assembly).
6. Iblīs's speech has **two voices**: militant / accusatory before God,
   whispering / solicitous before humans. Q 14:22 introduces a *third* voice:
   eschatological disavowal.
7. *Waswasa* is the signature modality of satanic action on humans. Its
   theological lineage unites Q 7:20 (Adam), Q 50:16 (the self), and Q 114:4
   (the whisperer) into a single phenomenology.
8. *Shayāṭīn* (plural) is a **functional** category: it can denote
   eavesdropping jinn (Q 37), Solomonic labour-jinn (Q 21), teachers of magic
   (Q 2:102), or *human* adversaries of prophets (Q 6:112, Q 2:14).
9. Q 14:22 is the Quran's decisive anti-dualist statement. Satan himself
   admits he had *no sulṭān*, only invitation. Evil is never externalised
   into a cosmic rival; it is always consent to an invitation.
10. Q 35:6 is the operative imperative: *take him as an enemy*. The Quran
    requires active, reciprocal enmity as the believer's stance.
11. The satanology is not a mythology. It is a theology of temptation, framed
    in narrative brackets: one refusal to prostrate, one world of whispering,
    one confession in Hell.

---

## 11. Open questions for further work

- Does the four-way distribution of the prostration-refusal correlate with
  the *mutashābih* pair-statistics in `mutashabih-pairs.csv`? Quick check
  yields **fifty-three attested pair-alignments across Q 7:11-18, 15:28-44,
  17:61-65, 38:71-85**; a saturated mutashābih cluster.
- Is the distribution of *Iblīs* (11) vs. *al-shayṭān* singular (69) vs.
  *shayāṭīn* plural (16) statistically interpretable as an 11-69-16
  hierarchical cascade? (Preliminary observation: the numerical ratios are
  not meaningful; the distributional shape is motivated by narrative frequency
  — how often the prostration scene is retold vs. how often Satan-as-tempter
  is addressed — and the *shayāṭīn* count matches the number of Satan-as-class
  references.)
- The *waswasa* family shares phonosemantic profile (W-S reduplication) with
  other Quranic "soft-whisper" vocabulary (e.g. *hamas* Q 20:108, *najwa*
  Q 58:7). Is there a broader covert-speech register? Flagged for a future
  phono-semantic agent.
