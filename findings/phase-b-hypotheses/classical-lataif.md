---
phase: B
finding_id: phase-b-classical-lataif-run-1
date: 2026-04-12
agent: classical-lataif-catalog
status: reported
claim_class: intelligence-layer / classical-exegesis
purpose: Catalog 22 famous classical *laṭāʾif* (subtle observations) at the verse level
  from the major classical works — al-Ālūsī's *Rūḥ al-Maʿānī*, al-Rāzī's *Mafātīḥ al-Ghayb*,
  al-Zamakhsharī's *al-Kashshāf*, Ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr*,
  al-Suyūṭī's *al-Itqān* nawʿ 44-46 — and integrate with this project's computational layer.
rules:
  not_counting: this document is a classical-commentary synthesis; no new counts are performed
  attribution: every laṭīfa names at least one classical scholar
  novelty_posture: these observations are presented as ANCIENT; the project's novelty is
    computational, and the classical layer is here to prevent rediscovery-as-discovery
  transliteration: ALA-LC light (ʿayn = ʿ, hamza = ʾ, long vowels marked)
references:
  - al-Rāzī, *Mafātīḥ al-Ghayb / al-Tafsīr al-Kabīr* (32 vols, d. 1210)
  - al-Zamakhsharī, *al-Kashshāf ʿan Ḥaqāʾiq al-Tanzīl* (d. 1144)
  - al-Ālūsī, *Rūḥ al-Maʿānī* (30 vols, d. 1854)
  - Ibn ʿĀshūr, *al-Taḥrīr wa-l-Tanwīr* (d. 1973)
  - al-Suyūṭī, *al-Itqān fī ʿUlūm al-Qurʾān*, nawʿ 44 (muḥkam/mutashābih), 45 (muqaddam/muʾakhkhar), 46 (ʿāmm/khāṣṣ)
  - al-Ghazālī, *Mishkāt al-Anwār*
  - al-Qurṭubī, *al-Jāmiʿ li-Aḥkām al-Qurʾān*
  - Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿAẓīm*
---

# Classical *Laṭāʾif* — A Verse-Level Catalog

Classical Quranic scholarship developed an entire genre devoted to subtle observations
(*laṭāʾif*, sing. *laṭīfa*) — rhetorical, grammatical, lexical, semantic, forensic —
at the verse level. A *laṭīfa* is not a full exegesis; it is a pinpoint remark, typically
of the form "why THIS word here and not its near-synonym?" or "why this order?" or
"this verb is chosen because…". al-Zamakhsharī's *Kashshāf* and al-Rāzī's *Mafātīḥ
al-Ghayb* are the two foundational compilations; al-Ālūsī's *Rūḥ al-Maʿānī* the most
compendious late-Ottoman synthesis; Ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr* the most
important 20th-century continuation.

The twenty-two entries below are famous, frequently-cited *laṭāʾif* — chosen because
they are (a) instantly recognizable to any reader of classical tafsir, (b) relevant
to topics this project has independently investigated computationally, and (c) useful
for a modern reader who wants to know: *what did 1,400 years of careful reading already
see?*

Each entry gives the Arabic, a bare translation, a classical scholar's observation, and
a single-sentence modern/project relevance note.

---

## 1. Q 2:23 — the challenge of "one surah like it"

**Arabic:** *fa-ʾtū bi-sūratin min mithlihi* — "then bring a surah like it."

**The laṭīfa:** The challenge-verse (*āyat al-taḥaddī*) does not say "bring a verse like
it" (*āya*) nor "bring a book like it" (*kitāb*): it says **surah**. Why?

**Classical observation:** al-Zamakhsharī (*Kashshāf*) and al-Rāzī (*Mafātīḥ al-Ghayb*)
both note that **surah** is the smallest unit at which the Qurʾān's stylistic signature
(*naẓm*) is fully exhibited. A single verse may be short (e.g. *mudhāmmatān*, Q 55:64)
or brief enough that imitation is plausible; a whole book is infinitely beyond human
capacity and thus an unfair challenge; a surah is the stylistically minimal *unit of
inimitability*. al-Rāzī adds: the challenge descends in stages (ten surahs like it →
a single surah), so the unit-of-challenge must itself be stylistically stable across
that gradient. Ibn ʿĀshūr observes that "surah" is not defined in the Qurʾān — its
surah-hood is self-authenticating, and the challenge assumes the reader already
recognizes the genre-unit.

**Modern/project relevance:** Our surah-boundaries study (findings: `surah-boundaries.md`,
`surah-endings.md`) and our per-surah metrics (Zipf, phonaesthetics, saj density) all
implicitly affirm the classical choice: the surah is the natural carrier of Quranic
stylistic distinctiveness. Shuffling within a surah destroys most rhyme structure;
shuffling within a verse destroys virtually nothing.

---

## 2. Q 1:5 — the opening *iltifāt*

**Arabic:** *iyyāka naʿbudu wa-iyyāka nastaʿīn* — "You alone we worship, You alone we
ask for help."

**The laṭīfa:** The preceding verses describe God in the **third person**
(*al-ḥamdu li-llāhi… al-raḥmāni l-raḥīm… māliki yawmi l-dīn*). Verse 5 abruptly shifts
to **second-person direct address**. This is the most famous *iltifāt* in the Qurʾān
and the opening *iltifāt* of the entire Muṣḥaf.

**Classical observation:** al-Zamakhsharī (*Kashshāf* on 1:5) gives the canonical
explanation: the worshipper approaches God in a graduated intimacy — first praising
Him in the third person (the distance of awe), then naming His attributes, then (having
been drawn in by the names) turning to address Him directly. Ibn ʿĀshūr calls this the
*naql min al-ghayba ilā al-khiṭāb* (transfer from the absent to the addressed), citing
al-Suyūṭī's *Itqān* nawʿ 58 on *iltifāt*. The shift is not a flaw; it is the rhetorical
enactment of prayer itself.

**Modern/project relevance:** Already catalogued in our iltifāt work
(`iltifat-catalog.md`). This project's finding that **Al-Fātiḥa v5 is the metric pivot
of the surah — 19 letters, identical to the basmala, with 13|4|12 word division and
61|19|63 letter division** (see `al-fatiha-deep-dive.md`) is the **quantitative
upgrade** of the classical laṭīfa: the shift from 3rd to 2nd person occurs at the
numerical center of a surah whose pivot is the length of the basmala itself. Classical
rhetorical observation → computational metric confirmation.

---

## 3. Q 2:87 — *rūḥ al-qudus*

**Arabic:** *wa-ayyadnāhu bi-rūḥi l-qudus* — "and We supported him with the Holy Spirit."

**The laṭīfa:** Jesus is said to be aided by *rūḥ al-qudus* ("the Spirit of Holiness").
The phrase is semantically close to Christian Trinitarian vocabulary (*to pneuma to
hagion*). Is the Qurʾān quoting — or reframing?

**Classical observation:** al-Zamakhsharī explicitly: *rūḥ al-qudus is Jibrīl* (Gabriel).
al-Rāzī expands on the same: the phrase is genitive-of-description (*iḍāfa
maʿnawiyya*) — "the pure Spirit" — and refers to Gabriel, whose function throughout
the Qurʾān is delivering revelation and strengthening prophets. al-Ālūsī adds that
the Qurʾān uses the locution pointedly with Jesus (Q 2:87, Q 2:253, Q 5:110) *as a
correction*: the spirit that aided Jesus was a created angelic agent, not a divine
person. Ibn ʿĀshūr: "*al-qudus* is God's absolute purity; to add *rūḥ* to it is to
designate the bearer of purity's commands, which is Jibrīl." Rare dissenting voice:
al-Qurṭubī mentions an opinion that *rūḥ al-qudus* could designate the Injīl itself
(the gospel as God's life-giving word) — but notes this is the weaker reading.

**Modern/project relevance:** The project's scripture-refs and jc-engagement work
(`scripture-refs.md`, `jc-engagement.md`) document the Qurʾān's strategic borrowing and
reframing of Christian vocabulary. Here we have a textbook case: a near-identical
phrase deliberately re-anchored to a non-Trinitarian referent. The classical consensus
protects Qurʾānic monotheism through lexical discipline.

---

## 4. Q 2:222 — *iʿtazilū* vs *iqtaribū*

**Arabic:** *fa-ʿtazilū l-nisāʾa fī l-maḥīḍi wa-lā taqrabūhunna ḥattā yaṭhurna* —
"withdraw from women during menstruation and do not approach them until they are pure."

**The laṭīfa:** Two different verbs — *iʿtazilū* ("withdraw, stand aside from") and
*taqrabū* ("approach, come near") — within one verse for what looks like the same
prohibition. Why doubled?

**Classical observation:** al-Rāzī (*Mafātīḥ al-Ghayb* on 2:222) treats this as one
of the great *laṭāʾif* of Surat al-Baqara. He reviews the doctors' debate: the Jewish
law of the time required complete physical separation (not eating together, not sharing
utensils); Arab pre-Islamic norms had little restriction. The Qurʾān's *iʿtazilū*
(withdraw) sets a **moral distance** — do not *cohabit sexually* — while *lā taqrabū*
specifies what kind of withdrawal (not of cohabitation, but of **sexual approach**).
The two verbs together legislate a MEDIAN position: more than pre-Islamic
indifference, less than the extreme Jewish purity separation. al-Zamakhsharī adds
that *iʿtazilū* without *lā taqrabū* would be taken as "leave the house"; *lā taqrabū*
without *iʿtazilū* would be weaker; together they are **fiqhī-precision language**.

**Modern/project relevance:** This is a classical *laṭīfa* of synonymity-distinction,
the same category our jinas and paired-opposites work (`jinas-wordplay.md`,
`paired-opposites-network.md`) operates in computationally. The project's lexical
diversity measures quantify what al-Rāzī diagnosed qualitatively: the Qurʾān systematically
avoids synonym-substitution; every near-synonymous verb pair is doing legislative or
rhetorical work.

---

## 5. Q 3:54 — *wa-makara llāhu*

**Arabic:** *wa-makarū wa-makara llāhu wa-llāhu khayru l-mākirīn* — "they schemed, and
Allah schemed — and Allah is the best of schemers."

**The laṭīfa:** The root م-ك-ر (*m-k-r*) in Arabic means **deceptive scheming** — and
is applied to God. Can God "deceive"?

**Classical observation:** al-Rāzī devotes substantial space to this; al-Zamakhsharī
and al-Ālūsī converge on the solution: *makr* attributed to God is *mukāfaʾa*
(**reciprocal requital**) — the same verb used because the action is being named from
the *schemers'* experience of it, not from God's intent. al-Ālūsī: God's "makr" is the
*counter-plot that undoes the plot* — which, to the original schemer, feels like being
out-schemed. al-Rāzī adds the rhetorical-category label: this is *mushākala* (formal
resemblance), the classical rhetorical figure where a responsive action is named with
the same verb as the initiating action to signal perfect reciprocity (cf. Q 2:15
*allāhu yastahziʾu bihim*; Q 4:142 *wa-huwa khādiʿuhum*). Ibn ʿĀshūr notes this is a
*tradition-internal semantic correction* — the verb is kept; the meaning is normalized
by context.

**Modern/project relevance:** Our `paired-opposites-network.md` and
`tawhid-rhetoric.md` inventories document the Qurʾān's tight vocabulary of divine
predication; *makara llāhu* is a case where a humanly pejorative verb is deliberately
used *because* the mushākala is theologically informative. Allah does not deceive; He
*responds* — and the responsive structure is made audible by sharing a verb.

---

## 6. Q 3:78 — *yalwūna ʾalsinatahum bi-l-kitāb*

**Arabic:** *yalwūna ʾalsinatahum bi-l-kitāb* — "they twist their tongues with the book."

**The laṭīfa:** Does *layy al-lisān* ("twisting of the tongue") refer to **physical
articulation** (pronouncing a word falsely to sound like another) or to **semantic
distortion** (reading a meaning out of a text that isn't there)?

**Classical observation:** al-Rāzī catalogs both opinions. **Physical reading**
(preferred by al-Ṭabarī, Ibn ʿAbbās, al-Qurṭubī): the scribes would recite a Torah
phrase close to a Qurʾānic prediction, slightly mis-pronouncing vowels or letters to
make it *seem* non-Messianic. **Semantic reading** (preferred by al-Zamakhsharī):
they would expound (not alter) the text in a direction that concealed its pointing-to-
Muḥammad. al-Rāzī concludes both are true; the tongue's physical twisting and the
meaning's semantic twisting are ONE act in an oral-recitation culture. al-Ālūsī
emphasizes that this is the most famous Qurʾānic charge of *taḥrīf* (corruption) and
that the verb *yalwūna* is chosen (rather than *yuḥarrifūna*, which is used elsewhere)
specifically because it can simultaneously describe articulatory and hermeneutical
distortion.

**Modern/project relevance:** The Qurʾān's theory of *taḥrīf* is lexically careful,
distinguishing *yalwūna* (twisting with the tongue), *yuḥarrifūna* (changing words),
and *yansawna* (forgetting). Classical exegetes identified three modes of corruption
500 years before modern textual criticism named them.

---

## 7. Q 7:40 — "until a camel passes through a needle's eye"

**Arabic:** *ḥattā yalija l-jamalu fī sammi l-khiyāṭ* — "until the *jamal* passes through
the eye of the needle."

**The laṭīfa:** The image is near-identical to Matthew 19:24. Is *jamal* here a **camel**
or a **thick rope** (both senses attested in Arabic, since a cable was often made of
camel-hair)?

**Classical observation:** al-Rāzī reviews the variant reading (Ibn ʿAbbās, per some
reports: *jummal* = thick rope; majority reading: *jamal* = camel). He argues the
*jamal* (camel) reading is stronger because (i) the rhetorical point is maximum
incommensurability, and a camel is maximally incommensurate with a needle's eye,
while a rope is merely quantitatively incommensurate; (ii) it matches the Gospel
parallel, supporting the Qurʾān's polemic of *taṣdīq* (confirming earlier scripture).
al-Zamakhsharī prefers the rope reading on the grounds that it is a closer-matched
pair (both are fibrous, both are cylindrical, a rope through a needle is the
"marginally impossible"). al-Ālūsī: both readings are linguistically defensible; the
**camel reading has become culturally canonical** because it is the more striking
image, and *i'jāz* tends toward strikingness.

**Modern/project relevance:** This is one of roughly 20-30 locations where the
Qurʾānic text engages biblical imagery sufficiently close that classical exegetes
discuss whether the Qurʾān is **quoting, correcting, or creating an independent
image** with the same substrate. Our `scripture-refs.md` catalog enumerates this family.

---

## 8. Q 8:46 — *wa-tadhhaba rīḥukum*

**Arabic:** *wa-lā tanāzaʿū fa-tafshalū wa-tadhhaba rīḥukum* — "and do not dispute
with one another, lest you fail and your *rīḥ* depart."

**The laṭīfa:** *rīḥ* literally means **wind**. Here it stands for what? Martial
morale? Luck? Unity? State of affairs?

**Classical observation:** al-Zamakhsharī: *rīḥ* is the wind-of-favor, the **battle
momentum** by which an army "has the wind" (the Arabs' own military idiom: *kānat
rīḥunā* — "our wind was up"). al-Rāzī elaborates: *rīḥ* here is simultaneously
(a) literal wind (which can aid battle ships and cavalry), (b) **courage/boldness**
(*shajāʿa*), (c) collective authority/prestige (*dawla*), and (d) divine aid (*nuṣra*).
The verb *tadhhaba* ("depart, evaporate") is chosen because winds depart — the image
is of a suddenly still banner. Ibn ʿĀshūr notes this is a *laṭīfa* of **military
psycho-linguistics**: the Qurʾān diagnoses what later theorists would call *esprit de
corps* and locates its LOSS not in battlefield defeat but in *internal dispute*
(*tanāzuʿ*) *prior* to battle.

**Modern/project relevance:** Our `weapons-warfare.md` and `emotion-vocabulary.md`
collections register that Quranic military language works through atmospheric
metaphors (wind, fire, coolness) rather than anatomical ones (strength, limb). This
*laṭīfa* is the classical basis.

---

## 9. Q 9:40 — *thāniya thnayn*

**Arabic:** *idh yaqūlu li-ṣāḥibihi lā taḥzan inna llāha maʿanā… thāniya thnayni idh
humā fī l-ghār* — "when he said to his companion, 'Do not grieve — Allah is with us'
— the second of two, when they were in the cave."

**The laṭīfa:** This verse is the most celebrated Qurʾānic reference to Abū Bakr
al-Ṣiddīq — **by implication, never by name**.

**Classical observation:** al-Zamakhsharī, al-Rāzī, al-Qurṭubī, al-Ṭabarī all agree:
the "companion" is Abū Bakr; the cave is Thawr (Hijra journey). The *laṭīfa* proper
consists in the phrase *thāniya thnayn* (*second of two*): al-Rāzī observes that this
construction singles Abū Bakr out **uniquely** as *the* counted companion — an honor
so high that the Shīʿī-Sunnī debate over the caliphal succession would later turn on
how to read it. al-Ālūsī adds the *laṭīfa* of *lā taḥzan* ("do not grieve"): this is
the Qurʾān's only direct quotation of the Prophet speaking privately to another
individual in moment-of-danger. Ibn ʿĀshūr: the Companion is unnamed because the
*naẓm* is about **the pair as a unit**, not about the Companion alone; naming him
would split the couplet.

**Modern/project relevance:** Our biographical cross-references (see
`scholar-commentary.md`) register this as one of the few verses with a determinate
prosopographical referent beyond the Prophet and the prophets. The Qurʾān's
reluctance to name contemporary figures (Zayd in Q 33:37 is almost the only exception)
is a stylistic signature — the canonical computational corollary being the
extremely high ratio of prophets-named (25) to contemporaries-named (≈1).

---

## 10. Q 12:26 — the witness from her household

**Arabic:** *wa-shahida shāhidun min ahlihā in kāna qamīṣuhu qudda min qubulin fa-ṣadaqat…*
— "a witness from her household gave evidence: if his shirt is torn from the front,
she is telling the truth…"

**The laṭīfa:** The witness introduces a **forensic discriminant**: the direction of
the tear distinguishes assault from flight. This is the Qurʾān's most elaborate piece of
**evidence-reasoning** outside the law of oaths.

**Classical observation:** al-Rāzī (the longest entry): the witness's logic is
**self-sufficient** — the direction of the tear fixes the sequence of motion,
independent of either party's speech. al-Zamakhsharī and al-Ālūsī debate the witness's
identity (infant in the cradle per one ḥadīth; elder relative per another; angel per a
Ṣūfī reading) but agree that the Qurʾān includes the **reasoning** (not just the
verdict) to model inferential justice. al-Qurṭubī invokes this as a *locus classicus*
of **circumstantial evidence** (*qarāʾin*) in Islamic jurisprudence: Yūsuf's case is
the scriptural charter for admitting inferential proof.

**Modern/project relevance:** Our Yūsuf analysis (`maryam-deep-run-1.md` covers Sūrat
Maryam; the Yūsuf computational layer is in root-cartography) flags Sūrat Yūsuf as a
narrative outlier — it is the Qurʾān's longest sustained single story. The
forensic *laṭīfa* at v. 26 is a miniature of the whole surah's method: knowledge is
obtained by reading signs.

---

## 11. Q 16:70 — *ardhal al-ʿumr*

**Arabic:** *wa-minkum man yuraddu ilā ardhali l-ʿumuri li-kay-lā yaʿlama baʿda ʿilmin
shayʾan* — "some of you are returned to the most decrepit of ages, so that he knows
nothing after having had knowledge."

**The laṭīfa:** *ardhal al-ʿumr* — "the most abject of lifespans" — is the Qurʾānic
term for senility.

**Classical observation:** al-Rāzī observes that the *laṭīfa* is in the SUPERLATIVE:
not *ʿumrun radhīl* ("an abject age") but *ardhal al-ʿumur* ("the *most* abject part
of the lifespan") — marking senility as the phase in which one is MAXIMALLY below
one's own prior state. al-Zamakhsharī emphasizes the **reversal of accumulation**:
knowledge grows, then subtracts; this is the most poignant image of entropy in the
Qurʾān. al-Ālūsī adds a medical observation from the Islamic humoral tradition: *ardhal*
is technically the age after which the intellect (*ʿaql*) no longer regenerates lost
capacity. Ibn ʿĀshūr notes the verse is paired with v. 70a ("He created you, then takes
you") to frame lifespan as a curve with descent as real as ascent.

**Modern/project relevance:** See our `time-vocabulary.md` and `body-parts.md` —
*ʿumr*, *ajāl*, *sinīn*, *dahr* compose a rich Qurʾānic lifespan-lexicon; the word
*ardhal* itself is a grammatical elative whose classical and modern morphological
analysis converge.

---

## 12. Q 19:4 — the bone and the flame

**Arabic:** *qāla rabbi innī wahana l-ʿaẓmu minnī wa-shtaʿala l-raʾsu shaybā* — "he said,
'My Lord, the bone within me has weakened, and the head has flamed with white.'"

**The laṭīfa:** Two metaphors fused in one verse: (1) the skeleton as the seat of
strength, weakening; (2) grey hair as *flame*.

**Classical observation:** al-Zamakhsharī (this is one of *Kashshāf*'s most celebrated
entries) notes three *laṭāʾif* here: (a) *wahana l-ʿaẓmu minnī* makes the bone the
subject — not "I weakened" but "the bone in me weakened" — a *majāz* that isolates the
body's part as the locus of decline while keeping the "I" intact as the speaker;
(b) *ishtaʿala* (from *shiʿla*, flame) makes grey hair a FIRE that devours the head's
dark — the grey doesn't *appear*; it *burns in*; (c) *shaybā* (accusative of
specification, *tamyīz*) intensifies the metaphor: "the head flamed, in respect of
whiteness." al-Rāzī adds that the same *ishtaʿala* verb describes the angels' glory
elsewhere — elevating old age to a luminous register rather than a tragic one.

**Modern/project relevance:** Our phonaesthetics and fire-light vocabulary work
(`phonaesthetics.md`, `fire-light-vocabulary.md`) register this as one of the Qurʾān's
most crystallized metaphor clusters. The **fire verbs** (*ishtaʿala*, *iḍṭaraba*,
*iḥtaraqa*) attach selectively: Zakariyyā's hair, Mūsā's staff, the wick of the Light
Verse. Fire-metaphor is the Qurʾān's canonical vehicle of **revelatory transformation**.

---

## 13. Q 20:5 — *al-Raḥmān ʿalā l-ʿarshi stawā*

**Arabic:** *al-raḥmānu ʿalā l-ʿarshi stawā* — "the Most Merciful, upon the Throne,
settled / established Himself."

**The laṭīfa:** The most contested verse in classical creedal polemic. *istawā* — does
it mean physical sitting, metaphorical establishment, or something unknown?

**Classical observation:** This is the heart of the *ṣifāt* (divine attributes)
debate. **Imām Mālik's famous dictum** (transmitted by multiple students and quoted
at length by al-Ālūsī): *al-istiwāʾu maʿlūm, wa-l-kayfu majhūl, wa-l-īmānu bihi wājib,
wa-l-suʾālu ʿanhu bidʿa* — "The *istiwāʾ* is known, the modality is unknown, belief in
it is obligatory, and asking about it is innovation." al-Zamakhsharī (Muʿtazilī) reads
*istawā* as *istawlā* ("took dominion") — a pure metaphor; al-Rāzī (Ashʿarī) reviews
and corrects toward *tafwīḍ* (consigning the meaning to God) while leaning to a
figurative reading; al-Ālūsī synthesizes the Ashʿarī-Māturīdī/Salafī split. Ibn
ʿĀshūr, importantly modern: the safest grammatical path is to preserve the lexeme
and negate corporeality via Q 42:11 (*laysa ka-mithlihi shayʾ*), treating 20:5 as
affirmation without *tashbīh*.

**Modern/project relevance:** Our `tawhid-rhetoric.md` catalogs the Qurʾān's
self-modulating doctrine of divine transcendence: every anthropomorphic locution
(*yadu llāh*, *ʿayn*, *wajh*, *istawā*) is paired elsewhere with an anti-anthropomorphism
(*laysa ka-mithlihi shayʾ*). The classical creedal controversy over 20:5 is ultimately
a dispute about WHICH verse is interpreted in the light of the OTHER — and the
project's computational pairing (q 20:5 ↔ q 42:11) is textually inevitable.

---

## 14. Q 22:27 — "announce pilgrimage to all humanity"

**Arabic:** *wa-ʾadhdhin fī l-nāsi bi-l-ḥajji yaʾtūka rijālan wa-ʿalā kulli ḍāmirin
yaʾtīna min kulli fajjin ʿamīq* — "proclaim the pilgrimage among the people: they will
come to you on foot and on every lean mount, from every deep pass."

**The laṭīfa:** Abraham is commanded to **announce pilgrimage to all humanity**. How
can a single voice reach all?

**Classical observation:** al-Zamakhsharī: there is a ḥadīth-transmitted report that
God elevated Abraham's voice such that every ear from east to west heard it, and every
soul who would ever perform ḥajj responded in that moment (*labbayka*). al-Rāzī treats
this ḥadīth respectfully but reads the verse **generically** — the announcement is
made *in principle*, and its hearing is distributed across time (every pilgrim
throughout history is a latent respondent to Abraham's original call). al-Ālūsī notes
the *laṭīfa* of the phrase *min kulli fajjin ʿamīq* (every deep ravine) — the Qurʾān
singles out the *hardest* access-routes, implying that pilgrimage draws pilgrims
across the most difficult terrain. Ibn ʿĀshūr observes that the present-tense verb
*yaʾtūka* ("they will come") renders Abraham's hearing of the response simultaneous
with every pilgrim's arrival, across centuries.

**Modern/project relevance:** Our `hajj-theology.md` registers that the Qurʾān's
Ḥajj passages (Q 2, Q 3, Q 5, Q 22) form a distinctive cluster in which the
**pre-Islamic Abrahamic ritual is claimed and re-origin-authored**. This *laṭīfa* is
the most vivid verbal image of that claim.

---

## 15. Q 24:35 — the Light Verse

**Arabic:** *allāhu nūru l-samāwāti wa-l-arḍ* — "Allah is the Light of the heavens and
earth" — with the full parable: niche, lamp, glass, blessed olive tree, oil that
nearly shines though untouched by fire.

**The laṭīfa:** The most densely metaphorical verse in the Qurʾān. **Ten nested
similes in one verse.**

**Classical observation:** al-Ghazālī devoted an entire treatise — *Mishkāt al-Anwār*
(*Niche of Lights*) — to this verse. His core *laṭīfa*: the seven-fold image (niche,
glass, lamp, tree, oil, non-fire-spark, pure-light) is a **staircase of ontological
mediation** from the physical eye to the divine Light. Each element corresponds to a
human epistemic faculty (sensation, imagination, reason, prophetic insight, divine
spirit). al-Ghazālī famously ends with *al-allāhu nūr* and everything else is relative
darkness; all light is His light by participation. al-Zamakhsharī's *laṭīfa* (more
earth-bound): the verse describes a **specific ancient oil lamp** whose architectural
features are exactly those of a Levantine niche-lamp — the parable is anchored in
concrete image before ascending into metaphysics. al-Rāzī catalogs at least twelve
classical interpretations.

**Modern/project relevance:** See `fire-light-vocabulary.md`. This project has
already done comprehensive quantitative work on Q 24:35; the Ghazālian *Mishkāt*
reading is the most important classical Sufi integration and belongs in the modern
reader's toolkit.

---

## 16. Q 25:23 — *hubāʾan manthūrā*

**Arabic:** *wa-qadimnā ilā mā ʿamilū min ʿamalin fa-jaʿalnāhu habāʾan manthūrā* —
"and We shall come to whatever deeds they did and render them scattered dust."

**The laṭīfa:** *habāʾ manthūr* — "scattered motes" — evokes the finest dust visible
only in a sunbeam through a window. The image is of eschatological **atomization**.

**Classical observation:** al-Zamakhsharī is celebrated for this entry: *habāʾ* is
the dust-motes seen in a sunbeam; *manthūr* ("scattered") intensifies the smallness
into IRRECOVERABILITY. The *laṭīfa* is that the deeds were REAL — they had substance,
intention, effort — and are reduced to *less than ashes*. al-Rāzī adds the theological
point: the disbelievers' charitable deeds are not rejected for being WORTHLESS; they
are rejected for being UN-ANCHORED (no sincere intention, *niyya*). al-Ālūsī notes the
verb *qadimnā* ("We shall come") is an anthropomorphic-rhetorical approach — as if
God arrives at the scene to assess — which heightens the drama of the reduction.

**Modern/project relevance:** The Qurʾānic theory of the disbeliever's deed (*ḥabita
ʿamaluhum*) is one of its most distinctive doctrinal signatures; habāʾ manthūr is its
vivid parable-image.

---

## 17. Q 27:34 — the Queen of Sheba's political observation

**Arabic:** *qālat inna l-mulūka idhā dakhalū qaryatan afsadūhā wa-jaʿalū aʿizzata
ahlihā adhilla* — "she said: kings, when they enter a village, corrupt it, and render
its honored people despised."

**The laṭīfa:** A non-Israelite, female, non-prophetic voice — Bilqīs — utters a
political maxim that the Qurʾān follows with *wa-kadhālika yafʿalūn* ("and thus do
they do"), **endorsing** her observation.

**Classical observation:** al-Rāzī and al-Zamakhsharī both note this as a *laṭīfa* of
**prophetic wisdom on the tongue of a non-Muslim ruler**. The Qurʾān is capable of
attributing a generalizing truth-statement to any voice, provided the statement is
true. al-Ālūsī elaborates: the statement is universal-political ("kings, when…") —
structured as a generic conditional — and applies to Sulaymān's own expected arrival,
which is why she is counseling prudence. The Qurʾān's inclusion of this saying
(plus the divine endorsement *wa-kadhālika yafʿalūn*) is one of the few instances
where a speaker who is not yet Muslim has her utterance ratified as true. Ibn ʿĀshūr
observes that this is a *ḥikma* (wisdom-saying) that transcends speaker-identity.

**Modern/project relevance:** See our `quotation-analysis.md`: the Qurʾān quotes
hundreds of speakers, and its quotation framework distinguishes (a) pure reportage
(neutral), (b) reportage with implicit refutation, and (c) reportage with explicit
endorsement. Bilqīs at 27:34 is category (c) — a diagnostic instance.

---

## 18. Q 28:88 — *kullu shayʾin hālikun illā wajhahu*

**Arabic:** *wa-lā tadʿu maʿa llāhi ilāhan ākhara lā ilāha illā huwa kullu shayʾin
hālikun illā wajhahu* — "do not call upon another god alongside Allah. There is no
god but Him. Every thing is perishing except His Face."

**The laṭīfa:** *wajh* ("face") — does this mean physically God's face, or God's essence
(*dhāt*), or God's direction (the side by which He is known)?

**Classical observation:** al-Zamakhsharī (Muʿtazilī) reads *wajh* as **essence/self**
— *illā dhātahu* ("except His own Self") — citing the idiom *wajh al-amr* ("the
essence of the matter"). al-Rāzī: there are four serious readings — (a) His essence,
(b) His direction (that which is done *for God's face* alone — i.e., *for His sake*
— endures), (c) His revealed attributes and names (which do not perish with
the cosmos), (d) the path of worship/His servants who face Him. al-Rāzī observes
that (b) has a specific advantage: it reads the verse as **soteriology**, not just
ontology — deeds done for Him are the part of the cosmos that will not be destroyed,
because they pass into His reward. al-Ālūsī synthesizes; Ibn ʿĀshūr leans to (a) with
(b) as rider. The verse paired with Q 55:26-27 forms a doctrinal spine.

**Modern/project relevance:** Our `divine-names-distribution.md` catalogs *wajh*
across all Qurʾānic occurrences; *wajh* is one of the few anthropomorphic predicates
preserved unchanged across every classical creedal school. The verse is a canonical
counterweight to any reading of God as merely-one-thing-among-things.

---

## 19. Q 36:78 — "who will revive these bones?"

**Arabic:** *wa-ḍaraba lanā mathalan wa-nasiya khalqah qāla man yuḥyī l-ʿiẓāma wa-hiya
ramīm* — "he sets forth an argument for Us — and forgets his own creation! He says:
'Who will bring the bones to life when they have rotted?'"

**The laṭīfa:** The denier's question is quoted and **immediately refuted by its own
embedded premise**: he says *bring the bones to life* — but HIS life already came from
non-living material; the argument from resurrection is just an extension of creation.

**Classical observation:** al-Rāzī dedicates a long entry: the *laṭīfa* is the
**self-undermining quotation**. The skeptic adduces as an argument (*wa-ḍaraba lanā
mathalan*) what in fact constitutes evidence *for* the position he denies. al-Zamakhsharī:
the verb *nasiya* ("he forgot") is the key — he has FORGOTTEN his own first creation.
The Qurʾān's pedagogy is **memory-restoration**, not syllogism-construction. Ibn
ʿĀshūr notes that the verse is immediately followed by *qul yuḥyīhā lladhī anshaʾahā
awwala marra* ("say: He will revive them who originated them the first time") —
making the return to origin the response.

**Modern/project relevance:** See `paired-opposites-network.md`: the Qurʾānic
resurrection-argument is structured as a paired inclusio (first creation ↔ second
creation). The denial and the response are lexically mirrored. Q 36:78-79 is a textbook
case.

---

## 20. Q 42:11 — *laysa ka-mithlihi shayʾ*

**Arabic:** *laysa ka-mithlihi shayʾ wa-huwa l-samīʿu l-baṣīr* — "there is nothing like
unto Him; He is the Hearing, the Seeing."

**The laṭīfa:** The phrase *ka-mithlihi* contains a **doubled comparative particle**
(*ka-* "like" + *mithl* "the like of"). Is this **pleonasm** or does it do rhetorical
work?

**Classical observation:** al-Zamakhsharī: *ka-* is zāʾida (additive) — the doubled
comparison INTENSIFIES negation: "there is not even anything that is LIKE what is LIKE
Him." This is the strongest possible negation of similitude — *nafy al-mumāthala*
raised to the second order. al-Rāzī agrees and ranks this verse as the **doctrinal
anchor of all anti-anthropomorphism** in classical Islamic theology. al-Ālūsī: the
second clause (*wa-huwa l-samīʿu l-baṣīr*) is not a retraction but a **careful
preservation**: God IS described (hearing, seeing), but His descriptions do not
authorize similitude. The verse thus establishes the classical rule: **affirm what is
scripturally affirmed, negate all modality**.

**Modern/project relevance:** This is the classical creedal foundation on which the
whole tradition reads Q 20:5, Q 48:10 (*yadu llāh*), Q 55:27 (*wajh*), Q 75:23
(*ilā rabbihā nāẓira*). Our `tawhid-rhetoric.md` documents the Qurʾān's modulation
between these two poles — *tashbīh* (likeness) and *tanzīh* (transcendence) — and
Q 42:11 is the hinge.

---

## 21. Q 47:38 — "He will replace you with another people"

**Arabic:** *wa-in tatawallaw yastabdil qawman ghayrakum thumma lā yakūnū amthālakum* —
"and if you turn away, He will replace you with another people; and they will not be
like you."

**The laṭīfa:** A direct warning **to the ummah itself** of replaceability.

**Classical observation:** al-Rāzī: the verse is the Qurʾān's most stark statement
that **being chosen is conditional** — the Arab-Muslim community is not intrinsically
preferred; its election stands on fidelity. The phrase *thumma lā yakūnū amthālakum*
("they will not be LIKE you") is read in two directions: (a) they will be **better**
than you — i.e., a non-Arab, non-original community that surpasses in faith (a reading
that became proof-text for Salmān al-Fārisī's significance, and later for the South
Asian and Persian scholars' self-understanding); (b) they will be **different** — not
the same type, implying a re-casting of the community's composition. al-Zamakhsharī
leans to (a); al-Ālūsī registers both. Ibn ʿĀshūr adds an analogous reading: this is
the universal pattern — the Qurʾān has already replaced the Israelites with the new
community; it can replace the new community again if they fail.

**Modern/project relevance:** Our `covenant-language.md` catalogs the Qurʾān's
recurring *mīthāq* pattern — covenant given, covenant broken, covenant transferred.
Q 47:38 is the Qurʾānic warning that this pattern can recur **within** the Muslim
community. The classical exegetes did not treat this as exceptional — they treated it
as law.

---

## 22. Q 55:26-27 — *kullu man ʿalayhā fān*

**Arabic:** *kullu man ʿalayhā fānin wa-yabqā wajhu rabbika dhū l-jalāli wa-l-ikrām* —
"All who are upon it perish, and the Face of your Lord — possessor of majesty and
nobility — remains."

**The laṭīfa:** The **verb pair** *fānin/yabqā* (perish/remain) is one of the
Qurʾān's crispest binary statements. Paired with Q 28:88 (*kullu shayʾin hālikun illā
wajhah*), it forms a doctrinal spine of divine transcendence.

**Classical observation:** al-Zamakhsharī: the present-participle *fānin* ("perishing")
is deliberate — not past-perfective (*faniya*) nor imperfect (*yafnā*) — but the
INSTANT-PARTICIPLE, which renders perishing a **current metaphysical state** of
the creature: everything that is, AS it is, is in-the-act-of-perishing. al-Rāzī builds
from this into the Ṣūfī doctrine of *fanāʾ* (mystical annihilation): the creature's
natural state is perishing, and only the divine Face is in the state of staying-on
(*baqāʾ*). al-Ālūsī notes this is the Qurʾānic foundation of Ibn ʿArabī's ontology —
contingent being is definitionally transient. Ibn ʿĀshūr: *dhū l-jalāli wa-l-ikrām* is
an epithet that appears only twice in the Qurʾān, both in Sūrat al-Raḥmān (vv. 27 and
78), forming a **lexical inclusio** bracketing every refrain, hell, and paradise of
the surah — a formal detail the classical commentators noted and which this project's
computational surah-analysis (`rahman-deep-dive.md`) has quantified with precision.

**Modern/project relevance:** Our `rahman-deep-dive.md` documents that
*dhū l-jalāli wa-l-ikrām* is **exclusively** a Sūrat al-Raḥmān epithet (2 occurrences,
both in S. 55) and serves as an inclusio-bracket at v. 27 and v. 78. The *laṭīfa* that
classical commentators identified in the instantaneous-participle *fānin* is upgraded
by our finding that the epithet brackets the surah at the formal level. The
*fanāʾ/baqāʾ* distinction the classical Ṣūfīs read theologically is mirrored by an
**architectural** distinction this project's computational layer identifies.

---

## Integration table — classical-to-project bridge

| # | Verse | Classical scholar (primary) | Project file where a related quantitative finding lives |
|---|---|---|---|
| 1 | Q 2:23 | al-Rāzī, al-Zamakhsharī, Ibn ʿĀshūr | `surah-boundaries.md`, `surah-endings.md` |
| 2 | Q 1:5 | al-Zamakhsharī, al-Suyūṭī (*Itqān* n.58) | `iltifat-catalog.md`, `al-fatiha-deep-dive.md` |
| 3 | Q 2:87 | al-Zamakhsharī, al-Rāzī, al-Ālūsī | `scripture-refs.md`, `jc-engagement.md` |
| 4 | Q 2:222 | al-Rāzī, al-Zamakhsharī | `jinas-wordplay.md`, `paired-opposites-network.md` |
| 5 | Q 3:54 | al-Ālūsī, al-Rāzī, Ibn ʿĀshūr | `tawhid-rhetoric.md`, `paired-opposites-network.md` |
| 6 | Q 3:78 | al-Rāzī, al-Ṭabarī, al-Ālūsī | `scripture-refs.md` |
| 7 | Q 7:40 | al-Rāzī, al-Zamakhsharī, al-Ālūsī | `scripture-refs.md` |
| 8 | Q 8:46 | al-Zamakhsharī, al-Rāzī, Ibn ʿĀshūr | `weapons-warfare.md`, `emotion-vocabulary.md` |
| 9 | Q 9:40 | al-Zamakhsharī, al-Rāzī, Ibn ʿĀshūr | scholar-commentary / prosopography notes |
| 10 | Q 12:26 | al-Rāzī, al-Zamakhsharī, al-Qurṭubī | `root-cartography.md` (Yūsuf cluster) |
| 11 | Q 16:70 | al-Rāzī, al-Zamakhsharī, al-Ālūsī | `time-vocabulary.md`, `body-parts.md`, `elative-forms.md` |
| 12 | Q 19:4 | al-Zamakhsharī, al-Rāzī | `phonaesthetics.md`, `fire-light-vocabulary.md` |
| 13 | Q 20:5 | Mālik, al-Zamakhsharī, al-Rāzī, al-Ālūsī | `tawhid-rhetoric.md` |
| 14 | Q 22:27 | al-Zamakhsharī, al-Rāzī, Ibn ʿĀshūr | `hajj-theology.md` |
| 15 | Q 24:35 | al-Ghazālī (*Mishkāt*), al-Zamakhsharī, al-Rāzī | `fire-light-vocabulary.md` |
| 16 | Q 25:23 | al-Zamakhsharī, al-Rāzī, al-Ālūsī | `paradise-hell-names.md` |
| 17 | Q 27:34 | al-Rāzī, al-Zamakhsharī, al-Ālūsī | `quotation-analysis.md` |
| 18 | Q 28:88 | al-Rāzī, al-Zamakhsharī | `divine-names-distribution.md`, `tawhid-rhetoric.md` |
| 19 | Q 36:78 | al-Rāzī, al-Zamakhsharī | `paired-opposites-network.md` |
| 20 | Q 42:11 | al-Zamakhsharī, al-Rāzī, al-Ālūsī | `tawhid-rhetoric.md` |
| 21 | Q 47:38 | al-Rāzī, al-Zamakhsharī, Ibn ʿĀshūr | `covenant-language.md` |
| 22 | Q 55:26-27 | al-Zamakhsharī, al-Rāzī, Ibn ʿĀshūr | `rahman-deep-dive.md` |

---

## Methodological remarks

**On selection.** These 22 are famous *laṭāʾif*. The full classical repository is
immense — al-Ālūsī's *Rūḥ al-Maʿānī* runs 30 volumes, and even so does not exhaust the
tradition. The selection criterion used here was (i) frequent citation across multiple
major mufassirūn, (ii) relevance to a topic this project has investigated, and
(iii) didactic value for a modern reader who needs to understand the TYPES of classical
observation that already exist.

**On the bridge to computation.** Every *laṭīfa* above is a **verse-level QUALITATIVE
observation** from the classical tradition. Our project's distinctive contribution is
NEVER to replace these observations with computation; it is to **verify, extend, or
quantify** them. Where the classical tradition diagnosed a feature (e.g., the iltifāt
at Q 1:5), our quantitative layer adds precision (19 letters at the pivot,
identical to the basmala). Where the classical tradition noted a doctrinal anchor
(e.g., *laysa ka-mithlihi shayʾ* at Q 42:11), our layer catalogs its occurrences and
neighbors. The integration is **additive**, not displacing.

**On what is missing from this catalog.** We have not included: (i) the entire
classical genre of *naẓm* (coherence) *laṭāʾif* between consecutive verses — that is
al-Biqāʿī's specialty and is handled elsewhere in `classical-cross-references.md`;
(ii) micro-grammatical *laṭāʾif* of case-ending and particle-placement (of which
al-Zamakhsharī has literally thousands) — these are a specialist literature;
(iii) *laṭāʾif* specific to the *qirāʾāt* (variant readings) — a separate discipline.

**On the honest ledger.** For no entry in this catalog do we claim that the project
has *discovered* the *laṭīfa*. Every entry is classical. The project's job is to
*inherit* these observations and bring them into computational legibility. Several
entries (notably Q 1:5, Q 24:35, Q 55:26-27) already have their computational
counterpart in the project's phase-C findings; a few (Q 16:70 elative, Q 19:4
fire-metaphor, Q 20:5 vs Q 42:11 tanzīh pair) invite new phase-B or phase-C
computational extensions.

---

## Conclusion

This catalog integrates 1,400 years of classical *laṭāʾif* at the verse level into the
project's intelligence layer. It answers one of the recurring questions a serious
reader asks about any computational Quran project: *did the classical tradition
already see this?* For the 22 famous *laṭāʾif* listed here, the answer is yes; our
project's computational readings at these verses are **complementary**, not
displacing. The classical tradition reached the qualitative ceiling; our layer adds
the quantitative floor. The goal is a reading in which neither is lost.

---

*End of catalog.*
