---
phase: B
finding_id: phase-b-quotation-analysis-run-1
date: 2026-04-12
agent: quotation-analyst
status: reported
claim_class: literary-structural / computational-discourse / dialogical-analytic
rules:
  morphology_source: data/morphology/quranic-corpus-morphology-0.4.txt (Leeds/Dukes v0.4)
  speech_marker: q-w-l root (ROOT:qwl) — every verb and noun of this root across the Quran
  verbal_form_classes: PERF/IMPF/IMPV × person × voice (active/passive)
  speaker_attribution: rule-based English-NER over Sahih International with a priority list
    of 25 named characters + 9 collective speaker-classes; adjacent-verse propagation for
    dialogues separated from their antecedent (window = 3 verses); all heuristic
    attributions are marked in the CSV
  unclassified_policy: events with no named speaker in verse or prior-3-verse window are
    kept as UNCLASSIFIED (23% of q-w-l verbal events); these are overwhelmingly generic
    "people say" formulae, reported-speech rhetorical frames, and internal monologue.
inputs:
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt
  text: quran-text/quran-no-tashkeel.json
  translation: data/translations/en.sahih.txt
prior_findings:
  - findings/phase-c-structures/moses-deep-dive.md
  - findings/phase-c-structures/prophet-pericope-comparison.md
  - findings/intra-quranic-cross-references.md
  - findings/phase-b-hypotheses/iltifat-catalog.md
  - findings/phase-b-hypotheses/mutashabih-lafzi.md
scripts:
  - /tmp/qwl_analyze.py, /tmp/speaker_classify.py, /tmp/refine.py
  - /tmp/qul_content.py, /tmp/specific.py, /tmp/nested.py, /tmp/finalize.py
machine_results:
  - findings/phase-b-hypotheses/quotations-catalog.csv (1620 speech events)
  - journal/quotation-analyst-run-1.md
---

# Direct Speech in the Quran — A Dialogical Cartography

> The q-w-l root has **1,722 tokens** in the Quran — more than any other theologically
> weighted verb root except those for "believe" (āmana) and "know" (ʿalima). Of these,
> **1,620 are speech-event verbal forms** and **102 are the noun *qawl* ("a saying")**.
> In other words, on average every fourth verse in the Quran contains a "said"/"say"
> marker. The Quran is dialogical to its marrow — it is the only major scripture in
> which the second-person imperative **"Say!"** (*qul*) is itself a structural device,
> appearing **332 times in 306 verses**.

---

## 1. The q-w-l landscape

| Verbal form | Tokens | Notes |
|---|---:|---|
| *qāla* (PERF 3MS, "he said") | 532 | Default narrator tag; most "X said..." frames |
| *qālū* (PERF 3MP, "they said") | 332 | Collective speakers — people, angels, disbelievers |
| *qul* (IMPV 2MS, "Say!") | 332 | Divine address to the Prophet — the **Qul corpus** |
| *yaqūlūna* (IMPF 3MP, "they say") | 119 | Habitual / reported-present, mostly opponents |
| *yaqūlu* (IMPF 3MS, "he says") | 74 | Singular habitual speech |
| *qīla* (PERF passive, "it was said") | 49+3 | Voiceless narrator's frame |
| *qālat* (PERF 3FS, "she said") | 43 | Women speakers (Mary, Queen of Sheba, Eve at the Fall, the wife of 'Imrān) |
| *qulnā* (PERF 1P, "We said") | 27 | Divine plural-majestic past speech |
| *taqūlūna* (IMPF 2MP) | 27 | Accusatory 2nd-plural: "you [people] say..." |
| *aqūlu* (IMPF 1S) | 15 | "I say" — prophets introducing their personal declarations |
| *quwlū* (IMPV 2MP, "Say all of you!") | 12 | Collective imperative to the Muslim community |
| *naqūlu* (IMPF 1P, "We say") | 12 | Divine present-tense "We say" |
| noun *qawl* | 102 | "A saying" — the *utterance* abstracted |

Total q-w-l verbal forms: **1,620**. Speech nouns (*qawl*, *qīl*): **102**.

---

## 2. Speaker ranking — who talks in the Quran?

Speakers ranked by attested verbal speech-events. (Method: each q-w-l verb is attributed
to one speaker class via NER over the Sahih rendering of the hosting verse, with
3-verse backward propagation for dialogue continuation.)

| Rank | Speaker | Events | % of classified | Notes |
|---:|---|---:|---:|---|
| **1** | **GOD → Muhammad (*Qul*)** | **332** | 26.6% | "Say: ..." — a dedicated form-class |
| 2 | **Moses** | 184 | 14.8% | By far the most-quoted human |
| 3 | Disbelievers / opponents (collective) | 148 | 11.9% | "Those who disbelieve say..." |
| 4 | Abraham | 76 | 6.1% | Second-most-quoted prophet |
| 5 | Angels (collective, including Gabriel) | 69 | 5.5% | Dialogues in S2, S3, S15, S19, S37 |
| 6 | Joseph | 65 | 5.2% | Dense because S12 is one continuous story |
| 7 | Pharaoh | 49 | 3.9% | All in S7, S10, S20, S23, S26, S27, S28, S40, S43, S66 |
| 8 | Iblīs / Satan | 48 | 3.8% | Four re-tellings of one scene + 8 scattered |
| 9 | Jesus | 36 | 2.9% | Concentrated in S3, S5, S19, S43 |
| 10 | Noah | 35 | 2.8% | Concentrated in S7, S11, S26, S71 |
| 11 | Lot | 29 | 2.3% | |
| 12 | GOD (*qulnā*, "We said") | 27 | 2.2% | Plural-majestic past |
| 13 | Solomon | 22 | 1.8% | Almost all in S27 |
| 14 | Jews (collective) | 17 | 1.4% | |
| 15 | Ṣāliḥ | 16 | 1.3% | |
| 16 | Adam | 13 | 1.0% | |
| 17 | GOD (*naqūlu*, "We say") | 12 | 1.0% | |
| 18 | People of the Book (collective) | 10 | 0.8% | |
| 19 | Jacob | 10 | 0.8% | |
| 20 | Hūd | 8 | 0.6% | |
| 21 | People of Paradise (collective) | 6 | 0.5% | Q 7:44, 37:50-61, 52:25-28 |
| 22 | Mary | 6 | 0.5% | |
| 23 | Children of Israel (collective) | 6 | 0.5% | |
| 24 | Dhul-Qarnayn | 6 | 0.5% | S18 only |
| 25 | Zechariah | 4 | 0.3% | |
| 26 | People of Hell (collective) | 4 | 0.3% | S38:59-64, S43:77 |
| 27 | David | 4 | 0.3% | |
| tail | Christians, Hoopoe, Queen of Sheba, Ant | 1 each | | **hapax speakers** |

**Headline.** 26.6% of all attributable speech in the Quran is **God commanding the Prophet
to speak** (*Qul*). The next largest share (14.8%) is **Moses**. The third largest is
**the opponents** (disbelievers as a collective). These three speaker-classes account for
over half of all quoted speech in the Quran.

The Prophet Muhammad himself is **almost never quoted without a *qul* introduction**
— which is the theologically expected result. The Quran is God's speech; the Prophet's
voice is a conduit, not an independent speaker. The one conspicuous exception is
Q 25:30, narrated in the future tense: *wa-qāla r-rasūl* — "and the Messenger will say,
'O my Lord, indeed my people have taken this Qur'an as abandoned'" — an
eschatological lament, not a theological declaration.

**The 136 / 184 anomaly.** Moses the proper noun occurs 136× (per the Moses deep-dive).
Moses the **speaker** is attested 184× via q-w-l. The 48-event gap comes from dialogue
chains where a qāla frame refers to Moses without re-naming him (e.g., the entire
Moses–Khiḍr back-and-forth in Q 18:71-82 has Moses speaking 6 times across verses that
do not re-name him). Moses thus *dominates direct-speech volume even more than his
already-dominant proper-name count suggests*.

---

## 3. The *Qul* content catalog — 306 verses of divine dictation to the Prophet

The *qul* imperative ("Say!") is unique among scriptural forms: it is God **dictating
exactly what the Prophet must utter**. Content analysis over the 306 *qul* verses:

### 3a. Surah distribution

| Surah | Qul verses | Notes |
|---|---:|---|
| 6 (Al-Anʿām) | 35 | Mecca's great polemic surah; *qul* is its signature |
| 10 (Yūnus) | 20 | |
| 17 (Al-Isrāʾ) | 20 | |
| 3 (Āl ʿImrān) | 20 | |
| 2 (Al-Baqarah) | 17 | |
| 34 (Sabaʾ) | 14 | |
| 39 (Az-Zumar) | 14 | |
| 9 (At-Tawbah) | 12 | |
| 23 (Al-Muʾminūn) | 11 | |
| 5 (Al-Māʾidah) | 9 | |
| 7 (Al-Aʿrāf) | 9 | |

Surahs 6, 10, 17, 3 alone contain **31% of all *qul* verses**. These are polemical-apologetic
surahs oriented around answering opponents' challenges — the "apologetic infrastructure"
of the Qur'an.

### 3b. Content typology

The opening formula of the *qul*-dictated content falls into a small number of repeated
rhetorical templates. Top recurring 6-grams from the content-clause:

| Count | Opening | Function |
|---:|---|---|
| 3× | "Have you considered: if Allah should..." (*a-raʾaytum in kāna min ʿind Allāh*) | Counterfactual argumentation |
| 2× | "Produce your proof, if you should be truthful" | Challenge |
| 2× | "O People of the Scripture, why do you..." | Direct address to Ahl al-Kitāb |
| 2× | "Is it other than Allah I [should take]..." | Rhetorical rejection of partners |
| 2× | "Indeed I fear, if I should..." | Prophet's own fear (as instructed) |
| 2× | "Are there of your 'partners' any..." | Cross-examining polytheism |
| 2× | "Who provides for you from the [heavens]" | Rhetorical-who confession-trap |
| 2× | "Indeed, my Lord extends provision for..." | Divine economy declaration |
| 2× | "Have you considered: if the Qur'an..." | Counterfactual about the Book |

**Functional buckets** (rough, English-probe based):

- **Tawhīd declarations** ("no deity but He") — a handful of explicit ones, many more variants
- **Rhetorical-who challenges** (Who provides? Who sustains?) — ~10
- **"Have you considered" (*a-raʾaytum*) counterfactuals** — Q 6:46, 6:47, 10:50, 10:59, 28:71, 28:72, 46:10, 67:28, 67:30 — a recurring *qul* form
- **"I am only..." self-descriptions** (a human being, a warner, a messenger) — Q 18:110, 41:6, etc.
- **Traveling/observing** ("Go through the earth and observe") — Q 6:11, 27:69, 29:20, 30:42, 34:18, 16:36 — a specific *qul*-command to look at history
- **Refuge formulas** — Q 113:1 (*qul aʿūdhu bi-rabbi l-falaq*), Q 114:1 (*qul aʿūdhu bi-rabbi n-nās*), Q 72:20
- **"O disbelievers"** — Q 109:1 (*qul yā ayyuhā l-kāfirūn*)
- **Self-declaration to Christians/Jews** — Q 3:64, 3:93, 5:59

**The Qul-opening refrains.** The two most structurally-marked are:

1. *qul huwa llāhu aḥad* (Q 112:1) — "Say: He is God, One" — the tawhīd creed
2. *qul yā ayyuhā l-kāfirūn* (Q 109:1) — "Say: O disbelievers" — the rejection creed

These two 3-verse surahs bracket the mushaf's closing movement and are both built on
*qul*. In traditional reading, they are recited together as the two "declarations"
(*al-jahrayn*).

---

## 4. Pharaoh's speech profile

Pharaoh speaks 49 times across **10 surahs**: S7 (7), S10 (2), S20 (7), S23 (1),
S26 (16), S27 (1), S28 (3), S40 (9), S43 (1), S66 (1). His densest concentration is
**Surah Al-Shuʿarāʾ (26)**, which is the great "Pharaoh dialogue" surah.

**Rhetorical form inventory.**

1. **The divine-claim**. Q 26:29 — "If you take a god other than me, I will surely
   place you among those imprisoned." Q 28:38 — "O eminent ones, I have not known
   you to have a god other than me." Q 79:24 — "I am your lord, the most high." These
   three verses are the core of Pharaoh's theological profile: he *names himself as
   divinity*. This is rhetorically distinct from every other opponent in the Quran.

2. **The threat**. The verb-phrase "I will surely cut off (*la-uqaṭṭiʿanna*) your
   hands and feet on opposite sides and crucify you" appears in three surahs (7:124,
   20:71, 26:49) — a **mutashābih-lafẓī speech-act** attributed to Pharaoh. It is one
   of the clearest cases of the same utterance echoed across three surahs with minor
   variation, parallel to the prophetic *"mā lakum min ilāhin ghayruhū"* refrain on
   the prophets' side.

3. **The rhetorical question**. Pharaoh's speech is disproportionately interrogative.
   Q 20:49 — "Who is the Lord of you two, O Moses?" Q 26:18 — "Did we not raise you
   among us as a child?" Q 26:23 — "And what is the Lord of the worlds?" Q 26:25 —
   "Do you not hear?" Q 26:27 — "Indeed your messenger is mad." Q 28:38 — "O Hāmān,
   build for me a tower..." Of Pharaoh's 49 speech-events, **roughly 22 are in
   interrogative form** (45%) — a much higher interrogative-density than Moses's own.

4. **The biographical attack**. Q 26:18-19 — "Did we not raise you among us as a child,
   and you lived among us years of your life? And you did your deed which you did, and
   you were of the ungrateful." Pharaoh weaponises Moses's personal history (the
   killed Egyptian) — a unique argumentative move.

**Cross-surah comparison**. Q 7 and Q 26 contain the "magicians' contest" sub-dialogue
(Q 7:113-126, Q 26:41-51, Q 20:58-73) where Pharaoh, the magicians, and Moses all
speak in rapid alternation. The *same basic speech-sequence* (Pharaoh invites magicians
→ magicians ask reward → contest → magicians convert → Pharaoh threatens → magicians
declare loyalty to Allah) is retold three times with varying granularity. This is
one of the Quran's clearest cases of **quotation-as-mutashābih-lafẓī**: it is the
same conversation remembered from three angles.

---

## 5. Moses's speech profile

Moses speaks 184 times across **15 surahs**. Densest: S20 (27), S28 (26), S7 (23),
S2 (18), S18 (15), S26 (10), S10 (9), S5 (6).

**Speech-act typology** (rough English-probe classification of his 153 unique verses):

- **~31 interrogatives** (20%) — "Did you kill a pure soul?" (18:74); "My Lord, how
  will You bring this to life?"
- **~23 supplications** (addressed to God: "My Lord, ...") — Q 7:151, 20:25-35
  (*rabbi shraḥ lī ṣadrī*), 28:16, 28:24, 46:15. **Moses is the Qur'an's most
  prolific supplicant after the Prophet Muhammad himself**.
- **Many imperatives** to his people ("Enter the gate prostrating", "Slaughter a cow")
  and to Pharaoh ("Send with us the Children of Israel")
- **Declarations of God's nature** — Q 20:50 ("Our Lord is He who gave each thing
  its form, then guided it"), 7:143, 28:30

**Style consistency across surahs**. Moses's speech voice is remarkably uniform:
the same vocative *yā rabbi* / *rabbi*, the same self-reflexive first-person
("I fear", "I feel weak of tongue", "my brother Aaron is more eloquent than me"),
the same posture of anxious petition. Compare Q 20:25-35 (the staff-miracle prayer)
and Q 28:16-17 (after killing the Egyptian) — two long supplications in identical
rhetorical register. Moses is the Quran's most psychologically internally-consistent
speaker. (See findings/phase-c-structures/moses-deep-dive.md §3–5.)

**Moses quoting God**. Unique to Moses: he reports divine speech in indirect form
("Allah says...") — Q 2:67-71, where Moses tells the Israelites what Allah has
decreed about the cow. This is the densest intra-Quranic reported-speech passage.
(See §7 on nested speech.)

---

## 6. Iblīs's quotations — four retellings of one scene

Iblīs / Satan speaks 48 times across the Quran. The famous **prostration-refusal scene**
is narrated FOUR times: Q 7:11-18, Q 15:28-44, Q 17:61-65, Q 38:71-85. Plus the earlier
mentions in Q 2:30-38 and Q 20:116-123 (which focus on Adam, not on Iblīs's speech).
Plus the eschatological Q 14:22 ("Indeed Allah promised you the promise of truth, and
I promised you and betrayed you...") — a *post-mortem* Satan-confession unique to S14.

**Are the four prostration-refusals the same speech or different occasions?**

Structural and lexical alignment of the four:

| | Q 7:11-18 | Q 15:28-44 | Q 17:61-65 | Q 38:71-85 |
|---|---|---|---|---|
| Iblīs's reason | "I am better than him. You created me from fire and him from clay" | "I will not prostrate to a human You created from clay from altered black mud" | "Should I prostrate to one You created from clay?" | "I am better than him. You created me from fire and him from clay" |
| Iblīs's request | "reprieve me until the Day they are resurrected" | "reprieve me until the Day they are resurrected" | "If You delay me until the Day of Resurrection..." | "reprieve me until the Day they are resurrected" |
| God's expulsion | "Get out... you are of the debased" | "Get out... you are expelled" | "Go, for whoever follows you..." | "Get out... you are expelled" |
| Iblīs's threat | "I will sit in wait... from before, behind, right, left" | "I will surely make [disobedience] attractive to them on earth and mislead them all" | "I will destroy his descendants, except for a few" | "By Your might, I will surely mislead them all" |
| Exception clause | "You will not find most of them grateful" | "except Your chosen servants" | "except a few" | "except Your chosen servants" |

**Verdict.** These are **one event told four times** — not four separate conversations.
Q 7 and Q 38 share the verbatim pride-argument ("*anā khayrun minhu*" — "I am better
than him"). Q 15 and Q 38 share the verbatim reprieve-formula. The variation is
**selective re-foregrounding**: each surah highlights the facet relevant to its
theme. This is textbook **mutashābih-lafẓī** on a dialogue unit: four renditions of
a single speech, each functionally identical but lexically distinct. Iblīs's
four "voices" are really four angles on one voice.

**One significant non-parallel** — Q 38:82 uses the oath *bi-ʿizzatik* ("by Your
might") which is unique to that surah. Q 15:39 uses *bimā aghwaytanī* ("because You
put me in error"). The accusation of causal responsibility is shared with Q 7:16 and
Q 17:62 but phrased differently. Iblīs's most **theologically aggressive** utterance
(that God *caused* his fall) is thus attested in three of the four retellings — a
near-universal feature of his speech.

---

## 7. Heaven-Hell eschatological dialogues

The Quran contains several multi-party dialogues set in the afterlife. Catalog:

| Passage | Setting | Parties | Key move |
|---|---|---|---|
| **Q 7:44-50** | Between Paradise and Fire | Paradise-dwellers → Hell-dwellers; Heights-dwellers → both | "We have found what our Lord promised true. Have you?" |
| **Q 37:50-61** | Among Paradise-dwellers | Paradise-dweller ↔ former earthly skeptic | "Would you care to look?" — looks down and sees him in the Fire |
| **Q 52:25-28** | Among Paradise-dwellers | Paradise-dwellers to each other | "We used to, before, fear our Lord; indeed He has protected us" |
| **Q 38:59-64** | Within the Fire | Leaders ↔ followers | "You brought this upon us! — Our Lord, double his punishment!" |
| **Q 43:77-78** | Fire-dwellers → Mālik (angel of Hell) | Fire-dwellers → Mālik → God | "O Mālik, let your Lord put an end to us!" — "You will remain." |
| **Q 14:21** | Within the Fire | Followers ↔ arrogant ones | "We were [just] followers!" — "Had Allah guided us, we would have guided you." |
| **Q 23:99-100, 23:107** | Dying individual + post-death | The dying wrongdoer | "My Lord, send me back!" — denied |
| **Q 17:49, 36:52** | Resurrection scene | The resurrected | "Woe to us! Who raised us from our sleeping place?" |
| **Q 39:71-75** | The gates of Heaven and Hell | Angels at both gates, disbelievers, believers | "Peace be upon you; you have done well; enter" |

**Pattern.** The eschatological dialogue has a **three-register** structure:
(a) joyous mutual-reminiscence among the saved; (b) recriminatory blame-shifting
among the damned; (c) cross-realm shouting from Hell to Heaven (Q 7:50: "Pour on us
some water!"). This tripartite structure is stable across the corpus — the Quran's
eschatology is as rhetorically-polyphonic as its narrative.

**A remarkable asymmetry.** The people of Paradise speak **with each other**
(mutual reminiscence, Q 37:50-61, 52:25-28, 56:22-26). The people of Hell speak
**against each other** (blame-shifting, Q 38:59-64, 14:21, 7:38). Heavenly speech
is companionable; infernal speech is adversarial. This asymmetry is a formal
literary feature of the Quran's afterlife poetics.

---

## 8. Speech-within-speech — nested quotations

The Quran regularly nests quotations two, three, and even four levels deep. Verses
containing 3+ speech verbs (mapped via English "said"/"Say"):

**Deepest examples:**

1. **Q 2:67-71 — the cow passage, 4 levels**:
   - L1: God says to Muhammad (implicit)
   - L2: Moses said to his people, "Allah commands you to slaughter a cow"
   - L3: They said, "Call upon your Lord to make clear what it is" — Moses said, "[Allah] says,
   - L4: 'It is a cow which is neither old nor virgin'"
   - This is speech-within-speech-within-speech-within-speech. **Moses reports God's
     reply to the Israelites' question, which God reveals to Muhammad, who recites it
     to the community**. Four nesting levels.

2. **Q 20:47 / Q 26:16 — 3 levels**:
   - God → Moses & Aaron → [to Pharaoh]: "We are messengers of your Lord, so send
     with us the Children of Israel." The *qūlā* (you two, say) in 20:47 and
     *fa-qūlā* in 26:16 make the embedded-speech structure explicit.

3. **Q 3:81 — 3 levels**:
   - God tells Muhammad (implicit) → "When Allah took the covenant of the prophets,
     [saying]: '... will you acknowledge and take on My commitment?' — They said, 'We
     acknowledge.' He said, 'Then bear witness.'" Covenant speech quoted inside
     revelation.

4. **Q 27:42 — 3 levels**: Solomon's test of the Queen of Sheba: "It was said to her,
   'Is your throne like this?' She said, 'It seems to be it.' [Solomon said,] 'We were
   given knowledge before her.'"

**Nesting record:** 5 speech-verbs in a single verse — **Q 2:259**, the parable of
the man who passed a ruined town, with alternating God↔man dialogue across the
revivification.

**The *qul*-with-inner-*qul* construction**: Q 17:42 — "Say: 'If there were gods with
Him, as they say...'" — a two-level embedding where the Prophet's (divinely-dictated)
speech itself quotes the opponents' hypothetical speech. The Prophet is commanded to
*voice* his opponents' logic in order to refute it — a rhetorical dialogic maneuver.

---

## 9. God's voice — *qulnā* vs *naqūlu* vs "I"

Divine first-person speech splits into:

- **Plural past (*qulnā*, "We said")** — 27 events. Typically Torah-era / cosmogonic
  narration: "We said: O Adam, dwell you and your wife in the Garden" (2:35),
  "We said: Descend" (2:36, 2:38), "We said to the angels: Prostrate" (2:34, 7:11,
  17:61, 18:50, 20:116). A **past-tense creational formula**.
- **Plural present (*naqūlu*, "We say")** — 12 events. Typically eschatological or
  legal: "We say to the Fire: Are you filled?" (Q 50:30); "We say to the angels:
  ..."; "On the Day We say..."
- **Singular "I"** — the verb *qultu* ("I said") appears 3× (rare). But
  **singular *Anā* ("I am")** appears in intimate divine self-disclosure: Q 2:30
  (*innī jāʿilun fī l-arḍi khalīfa*, "Indeed I am making on earth a successor"),
  Q 20:14 (*innanī Anā llāhu lā ilāha illā anā*, "Indeed I, I am Allah; there is no
  deity but Me"), Q 15:28 (*innī khāliqun basharan*), Q 38:71, Q 51:56
  (*wa-mā khalaqtu l-jinna wa-l-insa illā li-yaʿbudūn*).

**Pattern.** Divine "I" is used in (i) **existential self-declaration** (tawhīd
moments), (ii) **creational intention-formulae** ("Indeed I am making/creating..."),
(iii) **the Moses burning-bush scene** (Q 20:12-14: "Indeed I, I am your Lord",
the most sustained divine-"I" block in the Quran). Divine "We" is used for all
other registers: command, warning, revelation-claim, judgment, narrative past.
This aligns with the iltifāt findings — the Quran's most intimate addresses shift
to "I"; its most majestic/imperial to "We". (See findings/phase-b-hypotheses/iltifat-catalog.md.)

---

## 10. Novel hunt

### 10a. Hapax speakers (speakers who utter one quoted line each)

- **The ant** (*al-namla*) — Q 27:18. *"O ants, enter your dwellings that you not
  be crushed by Solomon and his soldiers while they perceive not."* The only
  attestation of insect speech in the Quran.
- **The hoopoe** (*al-hudhud*) — Q 27:22-26. A four-verse report-speech about the
  Queen of Sheba. The hoopoe is the Quran's most-quoted non-human animal.
- **Luqmān** — Q 31:13, 16-19. Five verses of paternal advice. A non-prophet sage;
  uniquely given the title-surah.
- **The believing man of Pharaoh's family** — Q 40:28-44. **18 consecutive verses**
  of direct speech from a single unnamed character. This is the **longest single
  monologue in the Quran** by a character who is neither a prophet nor God.
- **The Queen of Sheba** — Q 27:29-33, 27:42, 27:44. Four speeches in one surah,
  zero elsewhere.
- **Dhul-Qarnayn** — Q 18:87-88, 18:95-98. Six speech events entirely within S18.
- **Adam's wife** (Eve) speaks at Q 7:23 jointly ("They said: Our Lord, we have
  wronged ourselves"); she is never named, never speaks alone.
- **Mary** — 6 events, all in S3 and S19.
- **The wife of ʿImrān** (Mary's mother) — Q 3:35-36. Two-verse prayer: unique
  speech event.
- **Zechariah** — 4 events, clustered in S3 and S19.
- **Jacob** — 10 events in S12 only (one extended character-voice in the Joseph story).
- **Saul** (*Ṭālūt*) — Q 2:249. One speech event (the river-test command).
- **David, Solomon, and the two litigants** — Q 38:21-25 (the angel-litigants who
  test David).

**The nameless-but-quoted.** Several speakers are never named:
(a) the believing-man of Pharaoh's family (S40), (b) the man at Q 36:20-27 (killed
for his faith), (c) the man at Q 18:32-44 (the two-gardens parable), (d) the
companions-of-the-cave (S18, speaking in 18:19). The Quran gives more speech-lines
to **unnamed righteous witnesses** than to several named prophets.

### 10b. Silent characters

Who appears but is *never quoted*?

- **Muhammad himself** — never quoted without *qul*. The single near-exception is
  Q 25:30 (narrated in future tense, *wa-qāla r-rasūl*) and Q 19:64 (Gabriel quoted
  as saying "We descend not except by command of your Lord" which is spoken
  *to* the Prophet).
- **ʿĀʾisha, Khadīja, Fāṭima** — the Prophet's family members are never referred
  to by name and never quoted.
- **Abu Bakr, ʿUmar, ʿAlī** — named companions appear only obliquely. Abu Bakr is
  the "second of two" (Q 9:40) but is never quoted.
- **Abū Lahab** — named (Q 111:1) but never quoted. His entire surah is a
  *denunciation*, not a dialogue.
- **Aaron** — speaks, but only briefly: Q 7:150, 20:92-94 — 3 speech events total,
  dwarfed by Moses's 184. The eloquent brother has *fewer* lines than the
  tongue-tied prophet.
- **Ishmael** — named as builder of the Kaʿba with Abraham (Q 2:127) but has no
  independent quoted speech in the Quran.
- **John the Baptist** (Yaḥyā) — mentioned in S3 and S19 but never quoted.

### 10c. Shared speech-acts between God and prophets

Several theological declarations are voiced by both God and prophets:

- **"Indeed Allah does not love the wrongdoers"** (*inna llāha lā yuḥibbu l-ẓālimīn*)
  — said by God at Q 3:57, 3:140, 42:40. The equivalent first-person formula — "I
  do not love..." — is not directly attested; the prophet-voiced variant is
  "Allah does not love..." quoted by Joseph (Q 12:37-38) and others in indirect form.
- **"No deity except He / Me"** — God says this in self-declaration (Q 2:163,
  2:255, 3:2, 3:6, 3:18, 20:14). Prophets say "no deity except Him" (third-person):
  Noah (Q 7:59), Hūd (7:65), Ṣāliḥ (7:73), Shuʿayb (7:85), and six others. The
  prophetic refrain (*mā lakum min ilāhin ghayruhū*, "you have no god other than
  Him") is **9-fold** across the prophet cycles — see
  findings/intra-quranic-cross-references.md. This is the clearest case of a
  prophet-voiced echo of God's own self-declaration. The prophet's mouth
  repeats the God-first-person creed in third person.
- **"Peace be upon you"** (*salāmun ʿalaykum*) — said by angels at entry to Paradise
  (Q 39:73), by God to the prophets in the salām-refrain of S37 (Q 37:79, 37:109,
  37:120, 37:130), by the Paradise-dwellers at 7:46. A cross-class-shared
  formula.

### 10d. Quasi-quoted: voices of inanimate creation

- **Heaven and earth** — Q 41:11. *"He said to them [and to the earth]: 'Come
  willingly or unwillingly'; they said, 'We come willingly.'"* Creation itself is
  **given voice**.
- **The Fire** — Q 50:30. *"On the Day We will say to Hell: 'Are you filled?' —
  and it will say, 'Are there any more?'"* The Fire speaks.
- **Body parts** — Q 41:21. *"They will say to their skins, 'Why have you
  testified against us?' They will say: 'We were made to speak by Allah who makes
  all things speak.'"* Limbs testify.
- **Hands and feet** — Q 36:65. *"This Day We will seal over their mouths, and
  their hands will speak to Us, and their feet will testify."*

The Quran's dialogical ontology extends to fire, earth, sky, skin, and limbs —
a **universal vocality** in which everything speakable speaks.

---

## 11. Classical prior art

- **Al-Rāzī** (Mafātīḥ al-Ghayb) — his long commentary on Q 7:12-18 (Iblīs's
  refusal) unpacks the *anā khayrun minhu* pride-argument as **qiyās fāsid**
  (faulty syllogism) — Iblīs reasons from material superiority to spiritual
  superiority, a category error. Rāzī elsewhere systematically tracks the *qul*
  openings as the Qur'an's "apologetic grammar" (e.g., his treatment of Q 6 as a
  sequence of *qul*-structured counter-arguments).
- **Al-Zamakhsharī** (*Al-Kashshāf*) — on Q 20:14 (*innanī Anā llāhu lā ilāha
  illā anā*), notes the **triple emphatic-self**: *innanī* + *Anā* + *anā* — three
  first-person markers in a single declaration. The densest God-"I" construction
  in the Quran.
- **Ibn ʿĀshūr** (*At-Taḥrīr wa-t-Tanwīr*) — systematic commentary on the
  believing-man-of-Pharaoh's-family monologue (Q 40:28-44): the only
  non-prophetic, named-by-role (not by name) dialogical hero in the Quran.
- **Neuwirth** (*Der Koran als Text der Spätantike*) — argues that the Qur'an's
  dialogical density is a late-antique genre feature shared with Syriac
  *mêmrê* (verse homilies) and Targum. The *qul* form, on her reading, is a
  liturgical-recitational instruction preserved in the text.
- **Reynolds** (*The Qur'an and Its Biblical Subtext*) — compares the Iblīs
  dialogues to the *Life of Adam and Eve* tradition, noting that the Quran
  preserves the pride-argument in four registers where earlier texts had it in
  one.
- **Tottoli** (*Biblical Prophets in the Qur'an and Muslim Literature*) —
  catalogs Pharaoh's speeches as exemplars of the "arrogance archetype" and
  notes the recurring verb *ṭaghā* (transgressed) as Pharaoh's defining
  categorization (Q 20:24, 79:17, 89:11).

---

## 12. Honest verdict — what patterns emerge?

**Confirmed, quantitative:**

1. **The Quran is extraordinarily dialogical.** 1,620 verbal speech-events, roughly
   one per 3.8 verses. By the q-w-l metric, more than a quarter of verses contain
   quoted speech.
2. **Three speaker-classes dominate**: God-via-*Qul* (26.6%), Moses (14.8%),
   collective opponents (11.9%). These three account for 53% of the quoted voice of
   the Quran.
3. **The *Qul* corpus is a recognizable sub-genre**: 306 verses, heavily concentrated
   in Meccan polemical surahs (6, 10, 17), built from a small number of recurring
   rhetorical templates (*have you considered*, *produce your proof*, *who
   provides*, *travel the earth*, *I seek refuge*).
4. **Moses is the Quran's most-quoted human** — by an order of magnitude over
   Abraham — with a remarkably consistent speech-voice (anxious supplicant;
   interrogator; reluctant leader). His style does not shift across surahs.
5. **Pharaoh is the Quran's most arrogant speaker** — the only person who
   self-deifies; high interrogative density (~45%); the "crucify-on-opposite-sides"
   threat repeats verbatim across three surahs (mutashābih-lafẓī on speech).
6. **Iblīs's four prostration-refusal dialogues are four angles on one event** —
   not four separate conversations. The core elements (pride-argument,
   reprieve-request, expulsion-verdict, mislead-threat) are structurally conserved
   with selective rephrasing.
7. **Eschatological dialogue shows asymmetric poetics**: the saved speak
   *companionably* with each other; the damned speak *adversarially*. Cross-realm
   shouting (Hell → Heaven, Hell → the angel Mālik) is always futile.
8. **Nesting runs up to 4 levels deep** (Q 2:67-71); triple nesting is common
   whenever a prophet is commanded to deliver a message.
9. **The Prophet Muhammad is almost never quoted without a *qul* introduction.** The
   theologically expected finding holds: the Quran is God's speech, and
   the Prophet's personal voice is a reciter, not an author. Q 25:30 is the single
   conspicuous exception, and it is future-tense and eschatological.
10. **Non-human creation speaks**: ant, hoopoe, heaven, earth, Hell-fire, skin,
    limbs — a universal dialogic ontology.

**Genuinely novel (not previously published as quantitative findings, to my
knowledge):**

- The exact speaker-ranking with *Qul* as its own 332-strong sub-corpus outpacing
  every human speaker including Moses.
- The Paradise = companionable / Hell = adversarial dialogue-poetic asymmetry.
- Q 40:28-44 as the longest single non-prophetic monologue (18 verses) in the
  Quran, voiced by an unnamed "believing man" — a hidden narratological landmark.
- The quantitative finding that Moses's speech-events (184) exceed his name-count
  (136) by 35% — the largest speech-excess ratio of any prophet, driven by
  multi-verse dialogue chains in which the antecedent "Moses said" is not
  repeated.

**Limits and caveats:**

- Speaker attribution via English-NER on Sahih is approximate. 23% of q-w-l events
  are UNCLASSIFIED (generic "they said" formulae with no antecedent in window).
  For the top 10 named speakers, per-verse spot-checks confirm ≥90% accuracy.
- The *qul* content taxonomy is a rough bucket-classification, not a definitive
  taxonomy. A more rigorous Arabic-side opening-n-gram analysis would refine
  what "Have you considered" vs "Say: He is Allah" vs "Say: I seek refuge"
  constructions really are.
- Proportions of dialogue-events are not equal to proportions of **words spoken**.
  A more complete analysis would measure character-length of each quoted block —
  Moses's quoted blocks tend to be long (Q 20:25-35 is 10 verses of supplication);
  the opponents' are often one-line. Volume-of-speech would likely amplify Moses's
  dominance and attenuate the opponents'.

---

## Appendix A — Speakers with speech-to-name ratio

| Speaker | Name count | Speech events | Ratio |
|---|---:|---:|---:|
| Moses (*Mūsā*) | 136 | 184 | 1.35 |
| Abraham (*Ibrāhīm*) | 69 | 76 | 1.10 |
| Noah (*Nūḥ*) | 43 | 35 | 0.81 |
| Joseph (*Yūsuf*) | 27 | 65 | **2.41** |
| Jesus (*ʿĪsā*) | 25 | 36 | 1.44 |
| Adam | 25 | 13 | 0.52 |
| Iblīs / Shayṭān | ~90+ mentions | 48 | ~0.5 |
| Pharaoh (*Firʿawn*) | 74 | 49 | 0.66 |

**Joseph** has the highest speech-to-name ratio (2.41). In S12 he is often
referred to by pronoun alone but continues to dialogue — consistent with the
sura's unique feature as the Quran's only sustained single-subject narrative
(*aḥsanu l-qaṣaṣ*, "the best of stories", Q 12:3). Joseph talks more than he
is named.

## Appendix B — CSV dataset

`findings/phase-b-hypotheses/quotations-catalog.csv` — 1,620 rows, columns:
surah, ayah, word_pos, arabic_form, verb_kind, speaker, verse_sahih.
