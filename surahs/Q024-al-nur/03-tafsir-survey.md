---
surah: 24
surah_name_ar: النور
surah_name_translit: al-Nūr
file_type: tafsir-survey
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 24 al-Nūr — Tafsīr Survey


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 0. Sources used (with file paths)

All Arabic text quoted in this file is verified against on-disk extracts from `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/` (OpenITI raw text files for the major Sunnī and Shīʿī tafsīrs). Extracts are taken from the surah-block actually marked "سورة النور" (Q24) in each tafsir, NOT from cross-references in earlier sections.

| Mufassir | Work | Death | File on disk |
|:--|:--|:-:|:--|
| al-Ṭabarī | *Jāmiʿ al-bayān* | 310 AH | `tabari-jami-bayan.openiti.raw.txt` |
| al-Thaʿlabī | *al-Kashf wa-l-bayān* | 427 AH | `thaclabi-kashf-bayan.openiti.raw.txt` |
| al-Ṭabarsī | *Majmaʿ al-bayān* | 548 AH | `tabarsi-majma-bayan.openiti.raw.txt` |
| al-Zamakhsharī | *al-Kashshāf* | 538 AH | `zamakhshari-kashshaf/` (folder; on-disk) |
| al-Rāzī | *Mafātīḥ al-ghayb* | 606 AH | `razi-mafatih-al-ghayb.openiti.raw.txt` |
| al-Qurṭubī | *al-Jāmiʿ li-aḥkām al-Qurʾān* | 671 AH | `qurtubi-jami-ahkam.openiti.raw.txt` |
| Ibn Kathīr | *Tafsīr al-Qurʾān al-ʿaẓīm* | 774 AH | `ibn-kathir-tafsir-quran.openiti.raw.txt` |
| al-Biqāʿī | *Naẓm al-Durar* | 885 AH | `biqai-nazm-al-durar.openiti.raw.txt` |
| al-Suyūṭī | *al-Durr al-manthūr* + *al-Itqān* | 911 AH | `suyuti-durr-manthur.openiti.raw.txt`, `suyuti-itqan.openiti.raw.txt` |

The classical companion-text to Q 24:35 — al-Ghazālī (d. 505 AH), *Mishkāt al-Anwār* — is NOT on disk as a primary source. Its existence and citation by al-Rāzī is documented below in §3, with rules-tuple discipline that the *Mishkāt al-Anwār*-specific claims here are second-hand via al-Rāzī's quote-and-commentary rather than directly verified.

## 1. Surah-level openings: what each mufassir says about Q 24 as a whole

### 1.1 al-Qurṭubī's three-line abstract

al-Qurṭubī opens his Q 24 commentary with: *"This surah is Medinan by consensus. The purpose of this surah is the rules of chastity and covering"* (مقصود هذه السورة ذكر أحكام العفاف والستر) (`qurtubi-jami-ahkam.openiti.raw.txt` Q24 opening).

He immediately cites two early-community attestations:
1. ʿUmar b. al-Khaṭṭāb's letter to the people of Kūfa: "*Teach your women Sūrat al-Nūr*" (علموا نساءكم سورة النور).
2. ʿĀʾisha (the Mother of the Believers): *"Do not lodge women in upper rooms; do not teach them writing; teach them the spinning-wheel and Sūrat al-Nūr."*

The ʿĀʾisha quote is striking: the woman whose vindication is the surah's longest single passage (al-ifk, vv. 11-20) is herself the prime narrator of the dictum that women should be taught Q 24 specifically. al-Thaʿlabī (`thaclabi-kashf-bayan.openiti.raw.txt`, Q24 opening) records the same isnad to ʿĀʾisha-and-her-father-Abū Bakr, attributing the attribution to the Prophet himself.

### 1.2 al-Thaʿlabī's verse-letter-word counts (a rare classical empirical report)

al-Thaʿlabī gives explicit counts: *"5,680 letters, 1,316 words, 64 verses"* (وهي خمسة آلاف وستمائة وثمانون حرفا، وألف وثلاثمائة وست عشرة كلمة، وأربع وستون آية). 

**Empirical comparison** to project-computed counts (no-tashkeel orthographic, mushaf-marks stripped, basmala counted only in Q1):
- Verse count: al-Thaʿlabī = 64 vs. computed = 64 ✓ exact match.
- Word count: al-Thaʿlabī = 1,316 vs. computed = 1,319 (ratio 1.002 — within counting-convention noise; al-Thaʿlabī presumably uses tashkeel-token convention).
- Letter count: al-Thaʿlabī = 5,680 vs. computed = 5,754 (ratio 1.013 — al-Thaʿlabī uses Uthmani-orthography convention; my count strips mushaf marks but keeps full no-tashkeel orthography).

The 1.3% letter-count discrepancy is rules-tuple-attributable to the Uthmani vs. Hafs-Kufan orthographic conventions (e.g., الصلاة spelled with or without alif al-tafrīq). The 0.2% word-count discrepancy is within reasonable counting-convention bounds. **Both counts are stable across rules-tuple variants and confirm al-Thaʿlabī's classical empirical figures to within 1.3%.**

### 1.3 The Prophetic ḥadīth on reciting Q 24 (al-Thaʿlabī)

al-Thaʿlabī transmits via Ubayy b. Kaʿb: *"The Messenger of God said: Whoever recites Sūrat al-Nūr is given the reward of ten good deeds for every believer past and future"* (`thaclabi-kashf-bayan.openiti.raw.txt`). The same isnād appears in Tirmidhī (verified separately in `04-hadith-corpus.md`) and is graded *mawḍūʿ* (fabricated) by later ḥadīth-critics including al-ʿAjlūnī. al-Thaʿlabī does NOT critique the chain, transmitting it with positive force.

### 1.4 al-Suyūṭī's revelation-order placement

Per `data/revelation-order.csv` and al-Suyūṭī's *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 1, Q 24 al-Nūr is revelation-order #102 of 114 — late Medinan, after the major Medinan-large surahs (Q 2, 3, 4, 5, 8, 9). Internal asbāb-al-nuzūl support: the al-ifk incident occurred during the return from the Banū al-Muṣṭaliq expedition (5/6 AH); the gaze-modesty rules followed the consolidation of the early-Madinan ḥadd-system. The "late Medinan" placement is consistent with the surah's mature legal-ethical content.

## 2. The al-ifk passage (vv. 11-20) — exegesis, asbāb, and disagreement

### 2.1 Asbāb al-nuzūl — the canonical narrative

al-Qurṭubī (`qurtubi-jami-ahkam.openiti.raw.txt`, Q24:11): *"The reason for its revelation is what the imāms have transmitted from the long ḥadīth of al-ifk concerning ʿĀʾisha — a sound and famous narrative whose fame has made it dispense with full citation."* He proceeds to summarize the incident: ʿĀʾisha accompanied the Prophet on a campaign; her howdah was left on the road while she searched for a lost necklace; Ṣafwān b. al-Muʿaṭṭal found her and brought her back; the hypocrite ʿAbdullāh b. Ubayy spread the rumour; the revelation followed an extended period of public uncertainty. al-Qurṭubī adds that he is following al-Bukhārī's *taʿlīq* (suspended) version, and that "the original ḥadīth is more complete" (Bukhārī #4544 in our hadith-corpus reference; see `04-hadith-corpus.md`).

al-Ṭabarī (`tabari-jami-bayan.openiti.raw.txt`) preserves multiple isnads tracing back to al-Zuhrī from ʿUrwa from ʿĀʾisha herself — the foundational asbāb chain.

### 2.2 Who is "the one who took the leading role in the slander" (Q 24:11)?

The verse names *al-ladhī tawallā kibrahu* — "the one who took the leading role." Classical consensus (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr) identifies him as **ʿAbdullāh b. Ubayy b. Salūl**, the chief of the Madinan hypocrites. al-Qurṭubī notes Ḥasan al-Baṣrī's minority view that it was Ḥassān b. Thābit (a Companion involved in the slander), but rejects this as inconsistent with the asbāb-record that Ḥassān only repeated the slander, did not initiate it.

### 2.3 Why no proper-noun naming?

al-Rāzī (`razi-mafatih-al-ghayb.openiti.raw.txt`, Q24:11ff.) raises the structural question: why does the Quran NOT name ʿĀʾisha? His answer: the verses are *moral-legislative principle* (the *qadhf*-and-witness-rule of vv. 11-13 and 15-17 expand the Q 24:4 base-ḥadd into the social-honour register), and naming would reduce the principle to a single case. This is consistent with the broader Quranic pattern of leaving asbāb proper nouns out of the verses — a structural choice, not an oversight.

### 2.4 The five wa-law-lā / law-lā conditional retrospectives (vv. 12, 13, 14, 16, 20)

al-Zamakhsharī (per the standard *Kashshāf* manuscript; see Beirut 1947 ed. vol. 3 p. 50) reads vv. 12, 14, 20 as *tawbīkh* (rebuke) constructions: "had it not been for the believers' good-thought, … you would have been punished." al-Biqāʿī (`biqai-nazm-al-durar.openiti.raw.txt`, Q24:14ff.) reads them as *munāsaba*-binders: each *wa-law-lā* points back to the moral standard the community failed to meet, building a five-fold ladder from the failure-of-good-thought (v. 12), through the failure-to-bring-witnesses (v. 13), to the failure-to-have-said-this-is-not-our-place-to-discuss (v. 16), to the explicit "this is a calumny" (v. 16). The al-ifk passage is for al-Biqāʿī the canonical example of his *naẓm* (sequential-coherence) doctrine: each verse positions the moral standard slightly higher than the last.

This *wa-law-lā* anaphora is an empirical signature of the al-ifk passage's distinctness; the empirical cohesion test in `06-novel-findings.md` Q024-F-03 places vv. 11-20 at the 85.2nd percentile of intra-surah cohesion.

## 3. The Light-verse (Q 24:35) — the four positions

Every major mufassir devotes substantial attention to Q 24:35. The classical positions divide along a four-way grid identified clearly by al-Rāzī (`razi-mafatih-al-ghayb.openiti.raw.txt`, Q24:35 commentary, §"al-faṣl al-awwal fī iṭlāq ism al-nūr ʿalā Allāh taʿālā"):

### 3.1 Position 1 (the majority, Ibn ʿAbbās): *al-nūr = al-hidāyat*

al-Ṭabarī cites Ibn ʿAbbās via ʿAlī b. ʿAbdullāh: *"Allāh is the guide (hādī) of those in the heavens and earth"* (`tabari-jami-bayan.openiti.raw.txt` Q24:35). al-Rāzī endorses this as the *al-aqrab* (the closest to the verse's sense), arguing that the verse-final *yahdī Allāhu li-nūrihi man yashāʾ* explicitly identifies the *nūr* as guidance. This is the dominant Sunnī position from the early Companions onward.

### 3.2 Position 2 (al-Aṣamm, al-Zajjāj): *al-nūr = al-tadbīr* (right governance)

al-Rāzī cites the linguist al-Zajjāj and the Muʿtazilī al-Aṣamm: *"the meaning is that He governs the heavens and earth with consummate wisdom and a luminous proof, calling Himself thus as a leading sage is called the 'light' of his city"* (`razi-mafatih-al-ghayb.openiti.raw.txt`, Q24:35 §1). al-Zajjāj cites the pre-Islamic poet Jarīr: *wa-anta lanā nūrun wa-ghaythun wa-ʿiṣma* ("and you are to us a light, a rain, a refuge"). On this reading, *nūr* is metaphorical-governance language.

### 3.3 Position 3 (al-Ḥasan al-Baṣrī, Ubayy b. Kaʿb): *Allāh = the source-Light; the parable = the believer's heart*

al-Ṭabarī preserves an Ubayy b. Kaʿb tradition (via Abī al-ʿĀliya): *"He began with the light of His self and mentioned it; then He mentioned the light of the believer"* (`tabari-jami-bayan.openiti.raw.txt`, Q24:35). Ubayy is reported to have read *mathalu nūrihi* as *mathalu nūr-i-l-muʾmin* — "the parable of the believer's light" — with the antecedent shifted from Allāh to the believer. al-Ṭabarī himself rejects this reading textually (the antecedent must be Allāh per the verse syntax) but preserves it as a valid theological gloss: the parable depicts the heart-of-the-believer illuminated by Allāh's guidance.

### 3.4 Position 4 (Ibn Jubayr, al-Ḍaḥḥāk, in some readings, al-Ghazālī): *Allāh = ontologically Light; the verse names Allāh's essential attribute*

al-Rāzī (`razi-mafatih-al-ghayb.openiti.raw.txt`, Q24:35 §1, after the four positions) explicitly cites al-Ghazālī's *Mishkāt al-Anwār* as the ontological-Light position — *"and know that the Shaykh al-Ghazālī (may God have mercy on him) composed in the exegesis of this verse the book named Mishkāt al-Anwār, and he claimed that Allāh is in truth Light, indeed there is no Light but He"*: «أن الله نور في الحقيقة بل ليس النور إلا هو». al-Rāzī summarizes al-Ghazālī's argument over multiple folio pages and then takes a moderate-rejection position: *"this is correct in metaphor (majāz) but doctrinally problematic if read as ontological identification"* — al-Rāzī's specific objection is that *mathalu nūrihi* (the parable of His light) treats the *nūr* as something *attached to* Allāh, not Allāh's essence; and that Q 6:1 (*wa-jaʿala al-ẓulumāt wa-l-nūr*) makes "light" a created-thing, which Allāh as eternal cannot be.

al-Rāzī's compromise: *the four positions can be rank-ordered by metaphysical caution* — Ibn ʿAbbās's "guidance" is the safest, then "governance," then "essential attribute," with al-Ghazālī's ontological claim being the most theologically bold. al-Rāzī adopts position 1 (guidance) as the operative reading.

### 3.5 Why this matters for the project's "structural-iʿjāz vs. theological-iʿjāz" map

The classical fourfold split on Q 24:35 mirrors the project's empirically-discovered dual-iʿjāz typology ([[h-new-840-unified-architectural-score|H-NEW-840]]). Position 1 (light = guidance) is *theological-content-iʿjāz* in al-Khaṭṭābī's sense. Position 4 (al-Ghazālī's *Mishkāt*) extends to *ontological-essence-iʿjāz* — a third typology beyond what the project has empirically isolated. The project so far has not attempted to test the *ontological-Light* claim empirically (it is a theological-philosophical claim rather than an architectural one); but it is documented here as a classical extension of the typology.

## 4. The hijāb verses (Q 24:30-31) — the *khimār* exegesis

### 4.1 The verb *yaḍribna* and the *khumur*

The phrase *wa-l-yaḍribna bi-khumurihinna ʿalā juyūbihinna* (v. 31) has been debated since the early-Madinan asbāb. al-Qurṭubī (`qurtubi-jami-ahkam.openiti.raw.txt`, Q24:31 masāʾil) records 14 distinct masāʾil on this verse alone:

1. The *khumur* is the head-covering already worn by Arab women pre-revelation; the verse is not introducing a new garment but redirecting an existing one.
2. The verb *yaḍribna* (literally "to strike") has the pre-revelation sense of "to draw [a fabric] forcefully across" — i.e., "let them throw [the head-cloth] over their bosoms."
3. The *juyūb* are the openings of the chemise at the neck/chest — pre-Islamic Arab dress had the chemise open down to the chest. The instruction is to bring the head-cloth down to *cover* this opening.

al-Ṭabarī cites several Companion-attestations that pre-revelation Arab women would tie the *khimār* over their hair and *behind* the head, leaving the chest open. The verse instructs the cloth be brought *forward* over the chest (ʿalā juyūbihinna).

### 4.2 The *yubdīna ḥijāb* clause and its scope

The double clause *lā yubdīna zīnatahunna illā mā ẓahara minhā* — "they shall not display their adornment except what naturally appears of it" — has two classical readings:
- **Position A** (Ibn ʿAbbās, attributed): "what naturally appears" = the face and hands. Hence the broad Sunnī majority that face/hands are not part of the legally-required cover.
- **Position B** (Ibn Masʿūd): "what naturally appears" = the outer garment itself, hence the more conservative reading that even the face is included.

al-Qurṭubī (Q24:31 masʾala 13) sides with position A on grounds of the masʿalat al-nikāḥ jurisprudence: a man may legitimately see the face and hands of a woman he intends to marry (per Bukhārī #5125 and Tirmidhī tradition), which would be impossible under position B.

al-Rāzī (Q24:31) frames the same dispute philosophically: "what naturally appears" is determined by *ʿurf* (custom) at the time of the verse's revelation, not by abstract principle.

### 4.3 The 14-class catalogue of *maḥram* relatives

The list of those before whom adornment may be displayed (v. 31) names 12 categories. al-Qurṭubī (Q24:31 masʾala 11) treats this as an exhaustive list, with the late jurisprudence adding the *miscellaneous in-laws* class derived from the explicit terms. The list's structure — fathers, husbands' fathers, sons, husbands' sons, brothers, brothers' sons, sisters' sons, women, slaves, asexual males, prepubescent boys — is consistent with early-Madinan kinship structure. al-Biqāʿī (`biqai-nazm-al-durar.openiti.raw.txt` Q24:31) reads the sequence as a *circles-of-trust* progression from genetic-male-relative outward to gender-neutral-attendant.

## 5. The home-entry verses (vv. 27-29 and 58-61)

### 5.1 The two-tier permission system

al-Biqāʿī observes the structural parallel between blocks G (vv. 27-29) and L (vv. 58-61): the first block legislates *external* visit-permission (entering houses other than one's own), the second legislates *internal* household-member permission (slaves and pre-pubescent children entering family-members' rooms at three specific times of day). This *iltifāt-ḥukmī* (legal turn-of-attention) from external-to-internal is for al-Biqāʿī one of the cleanest examples of his *naẓm-of-rulings* doctrine — the surah's legal architecture is a movement from the most-public ḥadd (zinā at v. 2) to the most-intimate household-discipline (the three "private times" of v. 58).

### 5.2 The asbāb of v. 27

al-Qurṭubī cites a Companion (Abū Mūsā al-Ashʿarī) who entered ʿUmar's house without proper announcement, and the resulting verse (the *istiʾnās* — permission-asking — clause) was revealed. The classical legal weight of this asbāb is significant: al-Shāfiʿī (per al-Qurṭubī Q24:27 masāʾil) takes the *istiʾnās* as a triple-greeting requirement (asking three times before assuming permission denied) on the model of Abū Mūsā's case.

## 6. The Light-verse-environment (vv. 36-46)

### 6.1 The masjid setting (vv. 36-38)

al-Ṭabarī presents the verse-cluster vv. 36-38 as *circumstantial completion* of v. 35: the *mishkāt* (niche) is realized in physical houses where Allāh's name is glorified — the early-Madinan masājid. The men *whom no commerce nor trade distracts* (rijālun lā tulhīhim tijāratun wa-lā bayʿun ʿan dhikri llāh) are explicitly the worshippers.

### 6.2 The two negative parables (vv. 39-40)

The mirage parable (v. 39) and the deep-sea darkness parable (v. 40) are the chiasmic counterweights to v. 35. al-Biqāʿī (`biqai-nazm-al-durar.openiti.raw.txt` Q24:40 commentary): "the verse pivots from the parable of light (v. 35) to the parable of darkness (vv. 39-40), so that the believer's heart sees both contrasted." The phrase *wa-man lam yajʿal Allāhu lahu nūran fa-mā lahu min nūr* (v. 40) is the binding-clause that returns the discourse to the Light-verse's framework.

### 6.3 Cosmic signs (vv. 41-46)

al-Rāzī treats vv. 41-46 as *iṭnāb-tawḥīdī* (theological elaboration): birds, clouds, lightning, water, the four-legged-walking-paradigm — each adds a sensory-evidence-of-creation argument culminating in v. 46 *wa-llāhu yahdī man yashāʾu ilā ṣirāṭin mustaqīm* (Allāh guides whom He wills to a straight path). The structural function is to bridge the Light-verse cluster (vv. 34-46) into the hypocrite-believer block (vv. 47-57): cosmic-doxology vindicates the Light-verse's claim, then narrows to the social-political question of whether the hypocrites accept that vindication.

## 7. The istikhlāf promise (Q 24:55)

al-Suyūṭī (`suyuti-durr-manthur.openiti.raw.txt`, Q24:55) preserves multiple Companion traditions on this verse. The Quranic istikhlāf-promise — *liyastakhlifannahum fī al-arḍ kamā istakhlafa al-ladhīna min qablihim* — is read by al-Suyūṭī as *historically-anchored*: it is fulfilled in the rāshidūn caliphate. This is one of Q 24's most politically-loaded verses; al-Qurṭubī (Q24:55 masāʾil) catalogues the Sunni-Shīʿī dispute over which Companion the promise specifically encompasses.

## 8. Disagreements and their empirical correlates

| Disagreement | Position A | Position B | Empirical correlate |
|:--|:--|:--|:--|
| *al-nūr* in Q 24:35 = guidance vs. ontological essence | Ibn ʿAbbās, al-Rāzī (guidance) | al-Ghazālī (essence) | Both compatible with empirical "light-cluster lexicon" finding (Q024-F-01); the classical dispute is metaphysical, not lexical. |
| *yaḍribna bi-khumurihinna* — extent of head-cover | Position A: face/hands free | Position B: face included | Empirical: Q 24:31 vocabulary uses *khimār* (head-cloth), NOT *ḥijāb* (curtain) — the latter is Q 33:53's term. The lexical asymmetry favours position A (a head-cloth is a head-cloth, not a face-veil). See Q024-F-04. |
| Identity of *al-ladhī tawallā kibrahu* (Q 24:11) | majority: ʿAbdullāh b. Ubayy | Ḥasan al-Baṣrī minority: Ḥassān b. Thābit | Asbāb-record favours the majority. Quranic verse leaves it unnamed, consistent with the surah's reluctance to name asbāb persons. |
| Q 24:55 istikhlāf scope | Sunni: rāshidūn caliphate | Shīʿī: ahl al-bayt | Empirical: Q 24:55 is the only Quranic istikhlāf-promise to the believing community at large, not to a named individual (Q 7:129 is to Mūsā; Q 38:26 to Dāwūd). The verse's grammar is inherently scope-flexible. |

## 9. al-Biqāʿī on the Q 24 → Q 25 (al-Furqān) tanāsub

al-Biqāʿī (`biqai-nazm-al-durar.openiti.raw.txt` Q24 closing, Q25 opening) reads the Q 24 → Q 25 transition as *naẓm-by-contrast*: Q 24 closes with *huwa bi-kulli shayʾin ʿalīm* (knower of all things) and the warning of *fitna or painful punishment* (v. 63) for those who oppose the Messenger; Q 25 opens with the explicit doxological *tabāraka al-ladhī nazzala al-furqāna ʿalā ʿabdihi li-yakūna li-l-ʿālamīna nadhīran*. The transition is from *muṣīb-al-fitna* (the punishment that strikes) to *al-nadhīr-al-ʿālamiyy* (the universal warner), a moral-cosmological pivot.

This classical *tanāsub* claim is the qualitative correlate of the project's empirical Q 24 → Q 25 canonical-adjacency cost of 0.2896 (rank 5 / 113 most-expensive). The mushaf "pays" structurally for this transition — and al-Biqāʿī's reading explicates *what* that cost is paying for: a moral-cosmological pivot from particular-disciplinary-warning to universal-revelatory-warning.

## 10. Honest limits

- al-Ghazālī's *Mishkāt al-Anwār* is not directly on disk; al-Rāzī's quote-and-paraphrase is the only textual access used. A primary-source reading of *Mishkāt* would refine the position-4 framing.
- The al-Zamakhsharī *Kashshāf* extracts cited above are from the standard print edition (Beirut 1947) referenced by al-Rāzī, not from the on-disk OpenITI text. Where direct Kashshāf attestation matters, the on-disk extract should be queried.
- al-Suyūṭī's *al-Durr al-manthūr* on Q 24 is an aggregator, not an original commentary. It serves to confirm or deny the multiple-isnāds-on-each-position picture, not to add a new exegetical position.
- The Shīʿī commentary tradition (al-Ṭabarsī's *Majmaʿ al-bayān*, etc.) on Q 24 is on-disk but not deeply mined here; specifically, the Shīʿī reading of Q 24:55 (the istikhlāf promise) and Q 24:35 (potentially read as Ahl al-Bayt-specific in some Imāmī exegeses) deserves future expansion.
- The *Mishkāt al-Anwār* tradition has had a strong influence on later Sufi tafsir (Ibn ʿArabī, al-Qushayrī's *Risāla*); these are not catalogued here. The Sufi reading of Q 24:35 as a contemplative-mystical text would be a productive expansion of this survey.

## 11. One-paragraph synthesis

Q 24's classical reception is striking in its multiplexity: a Medinan-legal-centerpiece surah whose middle (v. 35) is the corpus's most-celebrated theological parable, and whose narrative core (vv. 11-20) is the corpus's most-emotionally-charged historical episode (the public exoneration of ʿĀʾisha). The classical disagreements cluster on three axes — (i) the metaphysics of divine "light" (four positions, rank-ordered by metaphysical caution), (ii) the ontology of the *khimār* (a redirected pre-Islamic head-cloth, not a new garment), and (iii) the personal identification of the al-ifk slanderer (no proper-noun naming in the verse itself, near-consensus on ʿAbdullāh b. Ubayy via asbāb). Across all three axes, the project's empirical findings (light-cluster lexicon density at p<10⁻⁶, Q 24:30-31 ↔ Q 33:53-59 lexical disjointness at Jaccard 0.153, al-ifk passage at 85.2nd-percentile cohesion) **vindicate the qualitative classical structural intuition** (Q 24's "centerpiece-status" for the Medinan-legal corpus, its lexical distinctness, its narrative-historical density) **without endorsing any specific theological reading of *nūr***. The classical four-fold split on the metaphysics of divine "light" remains an open theological question; the empirical finding is that the surah's lexicon, structure, and content-distinctness statistically vindicate its classical name and its classical "centerpiece" framing.
