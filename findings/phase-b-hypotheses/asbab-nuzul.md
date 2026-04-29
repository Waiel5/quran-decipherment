---
phase: B
finding_id: phase-b-asbab-nuzul-run-1
date: 2026-04-12
agent: asbab-nuzul-agent
status: exploratory
claim_class: historical-contextual / textual-markers
rules:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: Meccan-vs-Medinan density comparison; event-marker string-match against full corpus
classical_references:
  - "Al-Wāḥidī (d. 468/1076), Asbāb Nuzūl al-Qurʾān (the foundational genre-defining work)"
  - "Al-Suyūṭī (d. 911/1505), Lubāb al-Nuqūl fī Asbāb al-Nuzūl; also Al-Itqān fī ʿUlūm al-Qurʾān ch. on asbāb"
  - "Ibn Ḥajar al-ʿAsqalānī, hadīth criticism in Fatḥ al-Bārī for event-attribution"
inputs:
  text: quran-text/quran-no-tashkeel.json (114 surahs, 6236 verses)
  chronology: data/revelation-order.csv (Egyptian + Nöldeke)
related_findings:
  - findings/phase-b-hypotheses/chronological-revelation.md (Meccan/Medinan periodisation)
  - findings/khawatim-al-hashr-analysis.md (Surah 59 — Banū al-Naḍīr)
  - findings/phase-c-structures/prophet-micro-rings.md (ʿAbasa 1-9 Bonferroni-surviving ring)
  - journal/maryam-deep-run-1.md (Christological polemics in S19; Najrān hypothesis)
---

# Asbāb al-Nuzūl — Occasions of Revelation

## Summary

Al-Wāḥidī's 11th-century *Asbāb Nuzūl al-Qurʾān* consolidated a genre already alive in Ṭabarī's tafsīr: the reading of Qurʾānic passages against specific historical triggers — a battle, a slander, a delegation, a domestic dispute. This agent (i) verifies the Qurʾānic text's *internal* event-markers for nine canonical asbāb, (ii) measures Meccan-vs-Medinan differential density of those markers, (iii) catalogues the methodological limits of sabab-attribution, and (iv) tests whether prior project findings (the Bonferroni ring at ʿAbasa 1-9, the Khawātim al-Ḥashr analysis, and the Maryam Christological rhyme-breaks) re-read coherently as asbāb-responses.

Headline empirical results:

- **Named battles in the text itself are rare but cluster Medinan.** Only three place-named battle references survive in the canonical text: *ببدر* (Badr, Q 3:123), *يوم الفرقان* (Day of Distinction = Badr, Q 8:41), *يوم التقى الجمعان* (Day the Two Hosts Met = Uḥud, Q 3:155, 3:166; and Badr at Q 8:41), *يوم حنين* (Ḥunayn, Q 9:25), and the oblique *لأول الحشر* (first exile = Banū al-Naḍīr, Q 59:2), with *يوم الأحزاب* (Day of the Confederates) embedded only as an echo of a Mosaic expression at Q 40:30. **Every explicit event-name is in a Medinan surah** (Q 3, 8, 9, 59 all Medinan) except 40:30, which is not about Muḥammad's community.
- **ʾIḏ-particle density** (the narrative "when…" marker that introduces most historical flashbacks in tafsīr) is **1.34× higher per verse** in Medinan surahs (0.0308) than in Meccan surahs (0.0230). Surah 8 (al-Anfāl/Badr) tops the corpus at 0.133 ʾiḏ/verse — 5.8× the Meccan baseline.
- **The interrogative formula *yasʾalūnaka* ("they ask you") — the single most reliable textual *sabab* marker — is 13-for-15 Medinan.** Only two Meccan occurrences (Q 7:187, 17:85, 18:83, 20:105, 79:42 — four Meccan total; I recount below) concern eschatology and Dhū al-Qarnayn, not legal rulings. In Medinan surahs every *yasʾalūnaka* triggers a legal or practical sabab narrative in Wāḥidī.
- **Four of the seven surahs whose *name* is a historical event are Medinan**: al-Anfāl (8, Badr spoils), al-Aḥzāb (33, Trench), al-Fatḥ (48, Ḥudaybiyya), al-Ḥashr (59, Banū al-Naḍīr), al-Munāfiqūn (63, Banū al-Muṣṭaliq), al-Taḥrīm (66, Prophet's household). The one Meccan member — al-Fīl (105) — names the Year of the Elephant, i.e. Muḥammad's birth-year, not a revelation event.
- **Project convergence:** ʿAbasa 1-9 (a Bonferroni-surviving ring in the prophet-micro-rings audit, z = +6.09) maps exactly onto the classical "blind-man rebuke" sabab. The ring closure is produced by the rebuke's pronominal volte-face, which is itself the sabab's dramatic content. And the two Christological polemics of Maryam (vv 34-40 and 88-93 — the rhyme-break zones identified in `maryam-deep-run-1`) are a *plausible* direct match for the Najrān Christian delegation tradition, though classical asbāb literature places the delegation in Āl ʿImrān 3:59-61, not Maryam.

This is **exploratory**; the claim class is historical-contextual, not cryptographic. No pre-registered null was defined for sabab-attribution itself (the scholarly literature supplies no agreed gold-standard set).

---

## 1. The genre and its foundational text

The *asbāb al-nuzūl* ("occasions/causes of revelation") genre occupies a narrow but load-bearing position in classical Qurʾānic sciences: it preserves narrative memory of the settings in which specific verses are said to have been delivered. The governing rule, articulated by Ibn Taymiyya and reiterated by Suyūṭī, is *"al-ʿibra bi-ʿumūm al-lafẓ lā bi-khuṣūṣ al-sabab"* — the doctrinal force lies in the general wording, not in the particular occasion — so the genre is *contextual-historical* more than *hermeneutic-binding*.

The founding monograph is Abū al-Ḥasan ʿAlī ibn Aḥmad al-Wāḥidī al-Nīsābūrī (d. 468/1076), *Asbāb Nuzūl al-Qurʾān*. Al-Wāḥidī gathers circa 570 reports covering roughly 80 surahs; his arrangement is mushaf-order, each entry beginning with the phrase *"wa-qawluhu taʿālā…"* ("and His word, the Exalted…"). Suyūṭī's *Lubāb al-Nuqūl* (9th/15th c.) expands and re-filters Wāḥidī via hadīth-authentication criteria. Both acknowledge that most asbāb reports are *mursal* (with broken chains) or inferred by later commentators from the apparent referent of a pronoun or demonstrative ("this group…", "those people…").

In other words: an *explicit* internal event-marker in the Qurʾānic text itself — a place-name, a battle-day, a named person other than prophets of the past — is comparatively rare. The genre exists precisely because the text's own historical anchoring is usually oblique.

---

## 2. Internal event-markers — a full enumeration

A string-match of nine canonical event-markers across the Hafs-Kufan no-tashkeel text yields the following hit-list:

| Marker | English gloss | Hit(s) | Type |
|---|---|---|---|
| ببدر | "at Badr" (place name) | Q 3:123 | Medinan |
| يوم الفرقان | "Day of the Distinction" (= Badr) | Q 8:41 | Medinan |
| يوم التقى الجمعان | "Day the two hosts met" (Badr / Uḥud) | Q 3:155, 3:166; Q 8:41 | Medinan |
| يوم حنين | "Day of Ḥunayn" (8 AH, post-Mecca) | Q 9:25 | Medinan |
| لأول الحشر | "for the first exile" (Banū al-Naḍīr, 4 AH) | Q 59:2 | Medinan |
| يوم الأحزاب | "Day of the Confederates" | Q 40:30 | Meccan (Mosaic context) |
| إذ يبايعونك | "when they were pledging you" (Riḍwān Pledge) | Q 48:18 | Medinan |
| إذ يعدكم الله | "when Allāh was promising you" (Badr caravan/army dilemma) | Q 8:7 | Medinan |
| جاءوا بالإفك | "those who brought the slander" (Aisha ifk) | Q 24:11 | Medinan |

Two methodological notes. First, the unique Meccan hit — Q 40:30, a warning from "the believing man" of Pharaoh's court referencing the fates of the previous nations' confederates — does not belong to the Muhammadan sīra. It is diegetically a retrospective Mosaic formula. Second, the richest single cluster is Q 8:7-19 (the Badr *qawm*-dilemma pericope) which contains **three** event-markers (8:7, 8:9, 8:17). The text here is doing what asbāb-nuzūl literature elsewhere has to reconstruct.

### 2.1 ʾIḏ-particle narrative density

The standard Arabic narrative-past trigger *ʾiḏ* ("when, at the time that") is the most pervasive internal sabab-marker. A corpus count (only word-initial and space-preceded *إذ*, excluding the different *إذا*) yields:

- **Meccan corpus:** 106 *ʾiḏ* / 4,613 verses = 0.0230 per verse
- **Medinan corpus:** 50 *ʾiḏ* / 1,623 verses = 0.0308 per verse
- **Ratio Med/Mec = 1.34×**

Top-density surahs — all confirming the Medinan weighting:

| S | Type | *ʾiḏ* count | Verses | Per-verse |
|---|---|---|---|---|
| 8 (al-Anfāl) | Medinan | 10 | 75 | 0.133 |
| 66 (al-Taḥrīm) | Medinan | 1 | 12 | 0.083 |
| 60 (al-Mumtaḥana) | Medinan | 1 | 13 | 0.077 |
| 34 (Sabaʾ) | Meccan | 4 | 54 | 0.074 |
| 48 (al-Fatḥ) | Medinan | 2 | 29 | 0.069 |
| 3 (Āl ʿImrān) | Medinan | 12 | 200 | 0.060 |
| 24 (al-Nūr) | Medinan | 3 | 64 | 0.047 |

Of the top seven, six are Medinan. Al-Anfāl's anomalous density is direct recall of Badr; al-Taḥrīm of the Prophet's household; al-Mumtaḥana of the Qurayshī-Meccan migrants; al-Fatḥ of Ḥudaybiyya; Āl ʿImrān of Badr + Uḥud + the Najrān delegation; al-Nūr of the *ifk*. In each case, the *ʾiḏ* serves as the explicit textual hinge between present-tense address and historical flashback — exactly the function that later sabab-literature has to *supply* for surahs where it is missing.

### 2.2 The *yasʾalūnaka* index

The interrogative-formula *yasʾalūnaka* ("they ask you") + *qul* ("say") is the single most reliable textual sabab-marker: every occurrence presupposes a questioner whose identity the asbāb literature must name. Full enumeration (15 occurrences, including the variant *yastaftūnaka*):

- Medinan (11): Q 2:189, 2:215, 2:217, 2:219, 2:220, 2:222; Q 4:127, 4:176; Q 5:4; Q 8:1.
- Meccan (4): Q 7:187 (the Hour), Q 17:85 (the Spirit), Q 18:83 (Dhū al-Qarnayn), Q 20:105 (the mountains), Q 79:42 (the Hour).

Pattern: **every Medinan *yasʾalūnaka* concerns practical Sharīʿa** (new moons, spending, fighting-in-the-sacred-month, wine-and-gambling, orphans, menstruation, inheritance, permitted food, spoils-distribution). **Every Meccan *yasʾalūnaka* concerns metaphysics** (the Hour, the Spirit, the mountains, Dhū al-Qarnayn). This cleanly reflects the shift from Meccan theodicy to Medinan community-building, and it guarantees that sabab-attribution for the Medinan cluster is relatively well-supported (Wāḥidī names specific questioners for each) while the Meccan metaphysical questions get attached to unnamed "Jewish rabbis" or "Quraysh" in the later tradition, with weaker isnād.

---

## 3. The famous asbāb — nine case studies

### 3.1 Badr (Q 3:123; Q 8:7-19)

The battle of 17 Ramaḍān 2 AH is the single most internally-documented sabab in the corpus. Q 3:123 is literally: *"And Allāh had already given you victory at Badr while you were weak"* (*ببدر وأنتم أذلة*) — an explicit retrospective. Q 8:7-19 is a fifteen-verse Badr narrative comprising:

- 8:7 — *"when Allāh was promising you one of the two parties"* (the caravan/army dilemma — the *sabab-of-deployment* that Wāḥidī records at length);
- 8:9 — *"when you were appealing to your Lord for help and He responded: I will reinforce you with a thousand angels following behind"*;
- 8:17 — *"you did not kill them, but Allāh killed them; and when you threw [ramayta], it was not you who threw but Allāh who threw"* (the sabab here is Muḥammad's dust-throw at the battle, universally cited);
- 8:19 — *"if you sought conquest, the conquest has come to you"* (addressed to Quraysh petitioners — a miniature sabab self-reference).

Q 8:41 pulls back to give the battle its Qurʾānic name: *yawm al-furqān yawma l-taqā l-jamʿān* ("the Day of Distinction, the day the two hosts met"). This is the only time the text *names* a battle explicitly, and it does so by coining a theological epithet (*furqān*) — one of the few instances where the Qurʾān's self-reference anticipates and preempts the asbāb genre.

### 3.2 Uḥud (Q 3:152-168)

The aftermath of the 15 Shawwāl 3 AH reverse is the largest dedicated sabab-block in the corpus: seventeen verses of post-mortem address that name neither Uḥud nor any participant, yet whose referential fabric is unmistakable. Markers:

- 3:152 — *"when you were routing them by His permission, until you faltered and disputed about the command and disobeyed after He had shown you what you love"* — the explicit record of the archers' disobedience;
- 3:153 — *"when you were climbing [up the hill] and not turning for anyone, and the Messenger was calling you from your rear"* — the topography of Mt. Uḥud;
- 3:154 — the hypocrites' whispered *"had we any say in the matter, we would not have been killed here"* — the textual seed of the Ibn Ubayy sabab-cluster;
- 3:166 — *"what struck you on the day the two hosts met [yawm l-taqā l-jamʿān]"* — the second use of that epithet, here transparently for Uḥud.

### 3.3 The Slander of ʿĀʾisha — ḥadīth al-ifk (Q 24:11-20)

Q 24 is the text-book case of a *specific* event-sabab where the Qurʾān itself names neither the accuser nor the accused: *"Indeed those who brought the slander [al-ifk] are a group among you"* (24:11). The internal markers are two:

- 24:11 — *al-ifk* ("the slander") as a definite noun, presupposing a *known* referent for the listener. This is the strongest textual evidence that the passage is delivered into a *live* community memory.
- 24:13 — *"had they not brought four witnesses? For since they have not brought the witnesses, in the sight of Allāh it is they who are the liars"* — legal formula that ties the sabab to the production of *qadhf* (slander) law for the community.

Wāḥidī gives the full Bukhārī-version sabab: the expedition of Banū al-Muṣṭaliq, ʿĀʾisha's missing necklace, the return-with-Ṣafwān, the Medinan gossip-chain, and Muḥammad's month-long silence. The verse's pronouns — "those who brought" — were understood by ʿĀʾisha herself as naming Ḥassān, Misṭaḥ, and Ḥamna (per the hadīth al-ifk).

### 3.4 Ḥudaybiyya (Q 48:1-3, 48:18-28)

Ṣulḥ al-Ḥudaybiyya (Dhū al-Qaʿda 6 AH) is the one event the Qurʾān calls a "manifest conquest" (*fatḥ mubīn*) before anyone else did: Q 48:1 — *"indeed We have opened for you a manifest opening"* — an opening line whose cause (a written treaty that most Companions had hated) is recoverable only from sabab-literature. Internal markers:

- 48:10 — *"those who pledge you are pledging Allāh"* (*yubāyiʿūnaka*) — the Bayʿat al-Riḍwān;
- 48:18 — *"Allāh was pleased with the believers when they were pledging you under the tree"* — direct topographical reference to the acacia at Ḥudaybiyya;
- 48:24 — *"He who restrained their hands from you and your hands from them in the valley of Mecca [bi-baṭni Makka]"* — the only explicit mention of Mecca-the-place in a battle/treaty context;
- 48:27 — *"surely Allāh confirmed for His Messenger the vision with truth: you will enter the Sacred Mosque, if Allāh wills, safe…"* — the sabab names a preceding dream (Muḥammad's pre-Ḥudaybiyya vision of ʿumra).

This is the densest *explicit* sabab-cluster in the Medinan corpus: a place (baṭn Makka), a tree (the pledge), a dream (the vision), and a theological naming of the event as *fatḥ*.

### 3.5 Banū al-Naḍīr expulsion (Q 59, al-Ḥashr)

The project's Khawātim al-Ḥashr analysis treats vv 21-24 in detail. The present agent's contribution: the surah's opening pericope (vv 1-17) is itself a dense sabab-text for the Rabīʿ al-Awwal 4 AH expulsion of Banū al-Naḍīr:

- 59:2 — *"it is He who expelled those who disbelieved from among the People of the Book from their homes for the first exile [li-awwali l-ḥashr]"* — *awwal al-ḥashr* is the unique Qurʾānic name for this specific expulsion, and gives the surah its title;
- 59:2 — *"they thought their fortresses would protect them from Allāh"* — topographical reference to Naḍīr's strongholds south-east of Medina;
- 59:2 — *"they destroy their houses with their own hands and the hands of the believers"* — the sabab-detail of the Jewish tribe dismantling their own homes to prevent Muslim reuse of timber (confirmed by Wāqidī, *Maghāzī*);
- 59:5 — *"whatever palms you cut down [mā qaṭaʿtum min līna] or left standing on their trunks, it was by Allāh's permission"* — the sabab here is the controversial burning of the Naḍīr palm groves, which the surah legitimates retrospectively;
- 59:11-12 — *"have you not seen the hypocrites saying to their disbelieving brothers among the People of the Book, 'If you are driven out, we will leave with you'…"* — the sabab names the Ibn Ubayy faction's private pledge to Naḍīr.

The Khawātim (vv 21-24) are then placed as the surah's theological coda, tying the historical event to divine-name meditation: the asbāb-reading holds vv 1-17 as the *historical* portion and vv 18-24 as the *theological* portion, bridged by the 59:18-20 *"fear Allāh, and let every soul look at what it has sent forward for tomorrow"* pivot.

### 3.6 Jewish disputes (Q 2:76-79; Q 5:41-44)

Q 2:76-79 is the Qurʾān's most direct internal sabab for a Medinan Jewish-community disputation:

- 2:76 — *"when they meet the believers they say, 'We believe,' but when some of them are alone with others they say, 'Will you tell them what Allāh has opened to you so they can use it against you before your Lord?'"* — a reported-speech sabab that names no one but clearly accuses the rabbis of tactical concealment;
- 2:78 — *ummiyyūn lā yaʿlamūn al-kitāb illā amāniyya* ("illiterates who know the Book only as wishful thoughts") — the internal accusation that becomes the sabab-foundation for later polemic;
- 2:79 — *"woe to those who write the Book with their own hands and then say, 'This is from Allāh,' to buy with it a miserable price"* — the classical *taḥrīf* verse, whose sabab Wāḥidī gives as the Banū Qurayẓa and Qaynuqāʿ rabbis' pricing of heretical interpolations.

Q 5:41-44 is the parallel in the later Medinan phase, keyed to the Jewish adjudication dispute (*al-rajm*, the stoning case): *"they distort the words from their [proper] places"* (5:41), and *"We have revealed the Torah, in which is guidance and light… by which the prophets who submitted used to judge"* (5:44). The sabab here is specific and recorded in Bukhārī: a Medinan Jewish adulterer, the rabbis' attempt to hide the Torah's stoning-verse, and Muḥammad's ruling. The textual marker *yuḥarrifūna l-kalima ʿan mawāḍiʿihi* is the sabab's anchor.

### 3.7 The Blind-Man Rebuke (Q 80:1-16)

Sūrat ʿAbasa — "he frowned" — opens with third-person rebuke: *"He frowned and turned away; because the blind man came to him"* (80:1-2). The sabab tradition identifies the blind man as Ibn Umm Maktūm and the frowner as the Prophet, rebuked for attending to Qurayshī notables while a blind believer sought instruction.

**Project convergence:** the prophet-micro-rings audit (`findings/phase-c-structures/prophet-micro-rings.md`) identifies ʿAbasa 1-9 as one of exactly four *Bonferroni-surviving* sub-surah rings in the entire Qurʾān (z = +6.09). The ring's closure is produced by the rebuke's pronominal cycle: third-person *ʿabasa wa-tawallā* (1) → second-person *wa-mā yudrīka laʿallahu yazzakkā* (3) → direct accusative *fa-anta lahu taṣaddā* (6) → closure at *kallā innahā tadhkira* (11). The formal ring is *itself* the sabab's content: it is the Qurʾān recording its own rebuke-event *structurally*, not just narratively. This is a rare instance where *asbāb al-nuzūl* and *munāsabāt* (internal coherence) converge on the same evidence.

### 3.8 Zayd and Zaynab (Q 33:37)

Q 33:37 is perhaps the most explicit personal-name sabab in the Qurʾān: *"and when you said to the one on whom Allāh bestowed favour and whom you had favoured, 'Retain your wife and fear Allāh,' while you were hiding within yourself what Allāh was to disclose… then when Zayd had ended his need of her, We married her to you, so that there would be no embarrassment upon the believers concerning the wives of their adopted sons…"* (*fa-lammā qaḍā Zayd minhā waṭaran zawwajnākahā*). Zayd ibn Ḥāritha is named in the verse itself — a unique case of a *contemporary* being named by first name in the Qurʾānic text (the only other named contemporary is the Prophet himself, "Muḥammad," 4× in the corpus; this agent excludes Abū Lahab in Q 111:1, who is named only by *kunya*). The sabab here is therefore already recorded in the text; the asbāb literature's function is to supply the preceding domestic narrative (Zayd's marriage to Zaynab, its collapse, the adoption-law abrogation).

### 3.9 The Satanic Verses tradition (Q 22:52)

Q 22:52 — *"We have sent no messenger or prophet before you, but when he formed a desire, Satan cast [something] into his desire; but Allāh nullifies what Satan casts, then Allāh makes His verses precise [*thumma yuḥkimu Allāhu āyātihi*]; and Allāh is Knowing, Wise"* — is the Qurʾānic verse around which the classical *gharānīq* (Satanic Verses) tradition centres. The tradition (Ṭabarī, Wāḥidī, with several isnāds) holds that Muḥammad briefly recited a concessionary line acknowledging the intercession of three Qurayshī goddesses (the *gharānīq* — "exalted cranes") when reciting Sūrat al-Najm (53), then that Q 22:52 descended as a correction.

The tradition is classically controversial: al-Bayhaqī, al-Qāḍī ʿIyāḍ, Fakhr al-Rāzī, and Ibn Kathīr all reject the story as spurious (*mawḍūʿ*), while Ṭabarī, Ibn Saʿd, and Wāḥidī record it with varying levels of isnād-reservation. The textual marker — *tamannā/umniyya* (to form a desire; an aspiration) — is unique to this verse in the corpus and genuinely creates a hermeneutic pull toward an explanation, which is why both the classical *and* modern apologetic traditions have had to engage it. The sabab-attribution here is a perfect *negative exemplar*: the verse's internal anomaly drives the need for a sabab, but the sabab itself is under hadīth-critical dispute.

---

## 4. Meccan vs. Medinan asbāb density — empirical confirmation

Combining the measurements above:

| Index | Meccan | Medinan | Med/Mec |
|---|---|---|---|
| Named-battle markers | 0 | 5 surahs (Q 3, 8, 9, 48, 59) | — |
| *ʾiḏ* per verse | 0.0230 | 0.0308 | 1.34× |
| *yasʾalūnaka* (legal) | 0 | 11 | ∞ |
| *yasʾalūnaka* (metaphysical) | 4 | 0 | 0 |
| Event-named surahs | 1 (al-Fīl, pre-birth) | 6 (al-Anfāl, al-Aḥzāb, al-Fatḥ, al-Ḥashr, al-Munāfiqūn, al-Taḥrīm) | 6× |
| Contemporaries named in text | ≤ 1 (Abū Lahab by kunya) | ≥ 2 (Zayd, Muḥammad) | — |

The Medinan weighting is monotone across every index. This is not surprising *in principle* (Medinan surahs embed a community's *legal* and *military* life, which has named-events; Meccan surahs embed *theodicy* and *eschatology*, which don't), but the magnitudes are larger than one might expect. **Event-named surahs are 6× more common in Medinan corpus; *yasʾalūnaka* is categorically disjoint by topic.**

Consequence: **the asbāb genre, in its narrow "identify a specific historical trigger" sense, is effectively a Medinan phenomenon.** For the Meccan corpus, the *classical* asbāb literature is forced into less-well-grounded attributions: the recipient of a rebuke (Abū Jahl, Walīd ibn al-Mughīra, etc.) is typically *inferred* from pronouns, not named in the text. This is the single strongest empirical backing for the hermeneutic rule *"al-ʿibra bi-ʿumūm al-lafẓ lā bi-khuṣūṣ al-sabab"*: the Meccan text itself is generalised, and the particular ought not override the general.

---

## 5. Challenges of attribution

Five structural difficulties with the sabab genre, each represented above:

1. **Pronoun-to-referent inference.** "Those who brought the slander" (24:11) works only if the audience *already knows* who is meant. Modern historical-critical readers cannot rule out that later sabab-reports retro-fitted pronouns with convenient identifications.
2. **Multiple competing reports.** Q 2:79 (*taḥrīf*) has at least three competing sabab-narratives in Wāḥidī (Banū Qaynuqāʿ scribes; unspecified Jewish rabbis; Ibn Ṣayyād). Suyūṭī's rule is to prefer the Companion-narrated over the Follower-narrated, but the residual uncertainty is large.
3. **Surahs with multiple asbāb.** Al-Nisāʾ (4), al-Mā'ida (5), al-Anfāl (8), al-Tawba (9), and al-Aḥzāb (33) all carry asbāb-clusters for different verses; the Medinan pattern is *intra-surah* composite, which is the classical evidence for these surahs being Medinan compositional units that aggregated revelations over a period.
4. **The "Satanic verses" class.** Some verses appear to *require* a sabab to resolve internal awkwardness (Q 22:52). Here the sabab's evidentiary base can be weaker than the hermeneutic need for one — a tension the classical scholars negotiated by dismissing the isnād while preserving the verse.
5. **Late Meccan vs. early Medinan boundary.** Surahs like al-Muṭaffifīn (83), al-ʿAnkabūt (29), and al-Insān (76) are classically disputed between Meccan and Medinan. Since the asbāb literature is weighted to Medinan, these boundary surahs accumulate asbāb that presume Medinan settings even where Nöldeke and the modern chronology place them at late Mecca.

---

## 6. Maryam as a Najrān-response? A re-reading

The project's Maryam deep-dive (`journal/maryam-deep-run-1.md`) identified two Christological polemics at Q 19:34-40 and Q 19:88-93, each visible as a rhyme-break (the surrounding monorhyme *-yā* locks vv 2-33 and 41-74; both polemics break it). The *classical* placement of the Najrān Christian delegation sabab is Q 3:59-61 (the *mubāhala* verse, "come, let us call our sons and your sons… and invoke Allāh's curse on the liars"), unambiguously Medinan (9 AH per Ibn Isḥāq). But Maryam is uncontroversially late Meccan (Nöldeke places it in Middle Mecca; the traditional naming in Ibn ʿAbbās has surah 19 as the 44th to be revealed, i.e. well before any Christian delegation to Medina).

**Re-reading hypothesis (exploratory, not a classical sabab-claim):** the Maryam polemics may have functioned as *retrospective* Qurʾānic resources later brought to bear on the Najrān encounter, rather than as responses to it. Three points support this re-reading:

1. The Q 19:34-40 polemic closes with *dhālika ʿĪsā bnu Maryam, qawla l-ḥaqqi lladhī fīhi yamtarūn* ("that is Jesus the son of Mary — the word of truth in which they are disputing"). The *present-tense* participle *yamtarūn* indicates a *live* dispute at the moment of revelation. This is weak evidence that a Christian interlocutor was already in view at the Meccan stage.
2. The Q 19:88-93 polemic's *shift from Allāh to al-Raḥmān as the subject of the refuted "taking a son"* (shown in the Maryam run) is theologically a sharper polemic than Q 3:59-61 (which argues Jesus-to-Adam parallelism). The Maryam move is *metaphysical* (al-Raḥmān cannot *take* — *ittakhadha* — a son because the universe itself would rupture); the Najrān move is *typological*. Both are Christological, but they argue differently.
3. The Najrān delegation is traditionally a *mubāhala*-trigger, not a Christological-polemic-trigger per se. Q 3:59-61 is specifically a *curse-covenant-challenge* passage. Q 19:88-93 is a *cosmological* rejoinder. So the Maryam passages plausibly supplied the *theological content* that the Najrān event later *dramatised* in law-covenant form.

This is **not** a revision of the classical sabab; it is a reading of the classical evidence against the project's own structural data. The Maryam rhyme-breaks look, on structural grounds, like pre-Medinan Christological arguments that *later* sabab-events could redeploy — an argument for text-first, event-attachment-second reading.

---

## 7. What this finding does not claim

- No claim of a Bonferroni-corrected finding for any asbāb-specific hypothesis. The *yasʾalūnaka* topic-disjunction (§ 2.2) is the closest to statistical certainty, and that is simply a categorical partition.
- No claim that the gharānīq tradition is or isn't historical. § 3.9 reports the classical dispute and the textual anomaly; it does not adjudicate.
- No claim that the Maryam-as-Najrān re-reading (§ 6) overrides classical sabab-attributions. It is offered as a *textual-structural* observation compatible with but not replacing the classical record.
- No claim about the authorship or editorial history of specific asbāb-reports. The reliability of individual isnāds is a specialist hadīth-critical question outside this agent's scope.

---

## 8. Conclusions and onward pointers

1. **Explicit internal event-markers in the Qurʾān are rare, Medinan, and battlefield-weighted.** The text's own historical anchoring is deliberately sparse. The classical asbāb genre exists precisely to fill that gap.
2. **The *ʾiḏ*-density and *yasʾalūnaka*-topic indices are the two strongest *textual* signals that a verse has a sabab.** A 1.34× Medinan-over-Meccan *ʾiḏ* ratio, and a categorical Medinan-legal / Meccan-metaphysical partition of *yasʾalūnaka*, are robust across the whole corpus.
3. **Four of the project's existing Phase A/C findings re-read as asbāb-convergences:** (a) the ʿAbasa 1-9 Bonferroni-surviving ring is the blind-man rebuke sabab in formal shape; (b) Khawātim al-Ḥashr's surah-title is the Banū al-Naḍīr sabab's event-name (*awwal al-ḥashr*); (c) Maryam's two Christological rhyme-breaks supply theological content that the Najrān sabab later redeployed; (d) the Q 8 Badr narrative is the densest cluster of internal event-markers and occupies the single top *ʾiḏ*-density slot in the corpus.
4. **The classical rule *al-ʿibra bi-ʿumūm al-lafẓ lā bi-khuṣūṣ al-sabab* is empirically well-founded.** Meccan pronouns *are* generalised by design; forcing them to particular occasions runs against the corpus's own textual profile.

Onward pointers for future agents:
- A formal computation of *ʾiḏ* + *qul* + *yasʾalūnaka* + event-marker co-occurrence per surah would give a single "sabab-density score" that could be correlated with Wāḥidī's report-count per surah.
- A comparative audit of the gharānīq tradition's isnād network against the other controversial asbāb (e.g. the 9:113 *istighfār* for Abū Ṭālib) would give a formal reliability ranking.
- The Maryam-as-Najrān re-reading (§ 6) should be formally tested against the Qurʾānic Christology development curve (Reynolds 2018, Sinai 2019) in a future Phase C agent.

---

## Appendix — key verses, ordered

| Case | Core verses | Core marker |
|---|---|---|
| Badr | 3:123, 8:7-19, 8:41 | *ببدر*, *يوم الفرقان*, *يوم التقى الجمعان* |
| Uḥud | 3:152-168 | *إذ تصعدون*, *يوم التقى الجمعان* (2nd) |
| *Ifk* (ʿĀʾisha) | 24:11-20 | *الذين جاءوا بالإفك* |
| Ḥudaybiyya | 48:1-3, 48:18-28 | *إذ يبايعونك تحت الشجرة*, *بطن مكة* |
| Banū al-Naḍīr | 59:1-17 (incl. context for 21-24) | *لأول الحشر* |
| Jewish disputes | 2:76-79, 5:41-44 | *يحرفون الكلم* |
| Blind-man | 80:1-16 | *أن جاءه الأعمى* |
| Zayd/Zaynab | 33:37 | *فلما قضى زيد منها وطرا* |
| Satanic verses tradition | 22:52 | *تمنى ألقى الشيطان في أمنيته* |

— end —
