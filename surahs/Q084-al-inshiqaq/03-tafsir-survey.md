---
surah: 84
surah_name_ar: الإنشقاق
surah_name_translit: al-Inshiqāq
file_type: tafsir-survey
date_last_updated: 2026-05-30
phase: B+
verdict: 6 mufassirūn surveyed (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Suyūṭī) — all cited scholar+work+passage from on-disk sources
---

# Q 84 al-Inshiqāq — Tafsīr Survey

Six classical commentaries surveyed, source files cited per passage. The recurring exegetical
questions are: (1) the **deleted apodosis** of the *idhā…* cascade (vv 1-5); (2) the meaning of
*wa-adhinat li-rabbihā wa-ḥuqqat* (vv 2/5); (3) the addressee and force of *kādiḥun … kadḥan
fa-mulāqīh* (v 6); (4) the referent of *la-tarkabunna ṭabaqan ʿan ṭabaq* (v 19); and (5) whether
the v 21 sajda is among the *ʿazāʾim al-sujūd* (the obligatory-prostration verses). The spa5k API
files (`data/literature/classical-tafsir/spa5k-tafsir-api/`) supply al-Ṭabarī, al-Qurṭubī, and
Ibn Kathīr per-verse; al-Zamakhsharī and al-Rāzī are read from the OpenITI raw concatenations.

## 1. al-Ṭabarī, *Jāmiʿ al-bayān* (on Q 84:1-2, 6)

Source: `data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafsir-al-tabari/84/{1,2,6}.json`.

- **v 1** (`84/1.json`): *"idhā al-samāʾu taṣaddaʿat wa-taqaṭṭaʿat fa-kānat abwāban"* — "when the
  heaven cracks and is rent apart, becoming gates." al-Ṭabarī reads *inshaqqat* as a sundering of
  the sky into openings (cf. Q 78:19 *fa-kānat abwāban*).
- **v 2** (`84/2.json`): *wa-adhinat li-rabbihā wa-ḥuqqat* = *"wa-samiʿat … li-rabbihā wa-aṭāʿat lahu
  fī amrihi iyyāhā"* — "it **listened** to its Lord and **obeyed** Him in what He commanded it." He
  derives *adhina* from *istimāʿ* (giving ear), citing the prophetic report *"mā adhina Allāhu
  li-shayʾin ka-adhanihi li-nabiyyin yataghannā bi-l-Qurʾān"* and a line of poetry. *Ḥuqqat* = it was
  made to do so as its right/due (*ḥuqqat lahā an tafʿal*).
- **v 6** (`84/6.json`): *innaka kādiḥun ilā rabbika kadḥan fa-mulāqīh* = *"innaka **ʿāmilun** ilā
  rabbika ʿamalan **fa-mulāqīh bihi** khayran kāna ʿamaluka dhālika aw sharran"* — "you are **acting**
  toward your Lord a work, and you will **meet Him with it**, be that work good or evil." He cites
  Ibn ʿAbbās (via the Muḥammad-b.-Saʿd family isnād) for the gloss.

**Empirical correlate.** al-Ṭabarī's *kādiḥ = ʿāmil* (toiling = acting) and *fa-mulāqīh = meeting
Him with one's work* fixes v 6 as the surah's individual-accountability pivot — the verse that
Q084-F-02 confirms is the corpus-EXACT locus of the root k-d-ḥ.

## 2. al-Zamakhsharī, *al-Kashshāf* (on Q 84:1-6)

Source: `data/literature/classical-tafsir/raw/zamakhshari-kashshaf.openiti.raw.txt` (Sūrat
al-Inshiqāq block, located by the `# إذا السماء انشقت` section header).

al-Zamakhsharī's signature contribution is the **deleted-apodosis** *iʿjāz*: the *jawāb al-sharṭ*
(answer to "when…") is suppressed: *"ḥudhifa jawābu idhā li-yadhhaba al-muqaddaru kulla madhhab — aw
iktifāʾan bi-mā ʿulima fī mithlihā min sūratay al-Takwīr wa-l-Infiṭār"* ("the apodosis of *idhā* is
deleted so the implied [answer] may range over every possibility — or as sufficient by what is known
in the like of it from al-Takwīr and al-Infiṭār"). He notes that *wa-adhinat li-rabbihā* is *istiʿāra*
(metaphor): the heaven's compliance is figured as a *listening-and-obeying*, and *ḥuqqat* = *"ḥuqqa
lahā an tasmaʿa wa-tanqād"* (it was its due to hear and submit). On the v 2 ≡ v 5 repetition he holds
*"idhā ikhtalafa wajhu al-kalāmi lam yakun takrāran"* — the two are not mere repetition because the
first attaches to the heaven (vv 1-2) and the second to the earth (vv 3-5).

## 3. al-Rāzī, *Mafātīḥ al-ghayb* (on Q 84:1-12)

Source: `data/literature/classical-tafsir/raw/razi-mafatih-al-ghayb.openiti.raw.txt` (Sūrat
al-Inshiqāq block).

- **The suspended apodosis.** al-Rāzī catalogues **multiple scholarly positions** on the missing
  *jawāb idhā*: (i) al-Kashshāf's deliberate deletion (the answer ranges over all possibilities);
  (ii) al-Farrāʾ's "known by repetition" (sufficient from al-Takwīr/al-Infiṭār); (iii) the apodosis
  is *fa-ammā man ūtiya kitābahu* [= v 7] (al-Kisāʾī-style); (iv) the apodosis is *yā ayyuhā al-insānu
  innaka kādiḥun* [= v 6, the *fa-mulāqīh* reading]; and (v) a *taqdīm/taʾkhīr* reading. He treats the
  competing reconstructions as the surah's defining structural crux.
- **The kādiḥ embryo-analogy.** al-Rāzī glosses *kādiḥ* with the striving of the human from conception
  to the meeting with God ("*yā ayyuhā al-insānu innaka kādiḥun*" — the relentless toil that ends only
  at the *liqāʾ*), reading the surah as a unified arc from cosmic dissolution to individual reckoning.
- **The book *warāʾa ẓahrih* (v 10).** al-Rāzī surveys positions on how the book is given "behind the
  back," harmonizing with Q 69:25's *bi-shimālih*: al-Kalbī's reading that the left hand is twisted
  behind the back, and the view that the two phrases describe the same disgrace from different angles.

## 4. al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān* (on Q 84:1, 6, 19, 21)

Source: `data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafseer-al-qurtubi/84/{1,6,19,21}.json`.

- **v 1** (`84/1.json`): *"Sūrat al-Inshiqāq — **makkiyya fī qawl al-jamīʿ**, wa-hiya **khams
  wa-ʿishrūn āya**"* ("Meccan by the statement of all; it is twenty-five verses"). *Inshaqqat* =
  *inṣadaʿat*; one of the *ashrāṭ al-sāʿa* (portents of the Hour). This is the textual anchor for the
  Meccan + 25-verse claims (00-overview, 05-claims-audit Claim 1-2).
- **v 6** (`84/6.json`): *al-insān* = the human **genus** (*"al-murādu bi-l-insāni al-jins, ay yā bna
  Ādam"*) on Qatāda's authority — though Muqātil names **al-Aswad b. ʿAbd al-Asad** and a report names
  **Ubayy b. Khalaf** as a specific addressee. *Al-kadḥ fī kalām al-ʿArab: al-ʿamal wa-l-kasb* (toil =
  work and earning), with two pre-Islamic poetic *shawāhid* (Ibn Muqbil and another). Ibn ʿAbbās (via
  al-Ḍaḥḥāk): *kādiḥ* = *rājiʿ ilā rabbika* (returning to your Lord) → *fa-mulāqīh* = meeting your Lord,
  or meeting your record of deeds since the work is done.
- **v 19** (`84/19.json`): *la-tarkabunna ṭabaqan ʿan ṭabaq* — qirāʾāt split on *la-tarkabanna* (2nd
  masc. sing., address to the Prophet: "you shall mount state after state / heaven after heaven") read
  by Ibn ʿAbbās, al-Shaʿbī, Ibn Masʿūd vs *la-tarkabunna* (2nd masc. plur., address to mankind: "you
  shall pass through stage after stage — sperm, clot, lump, alive, dead, rich, poor"). The verse's
  referent (the heaven's transformations / the Prophet's ascending ranks / the human's developmental
  stages / the Day's terrors) is the chief exegetical fork.
- **v 21 (the sajda)** (`84/21.json`): *lā yasjudūn* = *lā yuṣallūn* (they do not pray). Cites the
  Ṣaḥīḥ report that **Abū Hurayra** recited *idhā al-samāʾu inshaqqat* and prostrated, reporting the
  Prophet did so. He then records the **legal disagreement**: **Mālik** held *"innahā laysat min
  ʿazāʾim al-sujūd"* (it is NOT among the obligatory-prostration verses, reading *lā yasjudūn* as "they
  do not yield/obey"); **Ibn al-ʿArabī** held *"al-ṣaḥīḥ annahā minhu"* (the sound view is that it IS),
  "the Medinan transmission from Mālik supports it, and Qurʾān and Sunna reinforce it." This Mālik ↔
  Ibn al-ʿArabī split is audited in 05-classical-claims-audit (Claim 4).

## 5. Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm* (on Q 84:1, 6, 21)

Source: `data/literature/classical-tafsir/spa5k-tafsir-api/en-tafisr-ibn-kathir/84/{1,6}.json`
(English); Arabic at `ar-tafsir-ibn-kathir/84/`.

- **v 1** (`en-tafisr-ibn-kathir/84/1.json`): section-titled *"The Prostration of Recitation in Surat
  Al-Inshiqaq."* Ibn Kathīr opens the surah with the **full sajda-isnād chain**: the **Mālik → Abū
  Salama** report (Abū Hurayra prostrating while leading prayer, *"recorded by Muslim and an-Nasāʾī on
  the authority of Mālik"*) and the **Bukhārī → Abū Rāfiʿ** report (the ʿishāʾ-prayer narration: *"I
  prostrated behind Abū al-Qāsim ﷺ, and I will never cease prostrating during its recitation until I
  meet him"*). He confirms the surah is "revealed in Makkah." This is the textual basis for the
  04-hadith-corpus sajda roster.
- **v 6**: *kādiḥun* = "laboring" toward the meeting with the Lord — Ibn Kathīr ties *fa-mulāqīh* to the
  inescapable *liqāʾ* and (in the Arabic) cites the Jābir-narrated counsel *"iʿmal mā shiʾta fa-innaka
  mulāqīh"* as the verse's prophetic echo (flagged in 04 as a tafsīr-citation; not located as a numbered
  ḥadīth in the on-disk 9-book set).
- **vv 7-15**: the right-hand party's *ḥisāb yasīr* glossed by the ʿĀʾisha *"man nūqisha al-ḥisāba
  ʿudhdhib … innamā dhālika al-ʿarḍ"* hadith (the "easy reckoning = display, not interrogation"
  tradition — Bukhārī, Muslim, Tirmidhī; see 04); the behind-back party's book given via the left hand
  twisted back (harmonized with Q 69:25).

## 6. al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*

Source: `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` (the *ʿadad al-āy* and
*sujūd al-tilāwa* nawʿs).

- **Verse count.** al-Suyūṭī records the variant counts for al-Inshiqāq: *"al-Inshiqāq: ʿishrūn wa-thalāth,
  wa-qīla arbaʿ, wa-qīla khams"* (23 / 24 / 25), with **25** the Kūfan-Ḥafṣ count adopted here
  (`suyuti-itqan.openiti.raw.txt` near offset 238467; see 00-overview).
- **The sajda.** al-Inshiqāq's v 21 is listed among the recitation-prostration verses; al-Suyūṭī
  classifies it with the *ʿazāʾim/sujūd al-mufaṣṣal* — the three mufaṣṣal prostrations (al-Najm 53,
  al-Inshiqāq 84, al-ʿAlaq 96) whose obligation the Mālikīs disputed but the Ṣaḥīḥayn affirmed.

## 7. Points of agreement / disagreement

| Question | al-Ṭabarī | al-Zamakhsharī | al-Rāzī | al-Qurṭubī | Ibn Kathīr |
|:--|:--|:--|:--|:--|:--|
| Meccan? | yes | yes (after al-Infiṭār) | yes | **yes, by consensus** | yes |
| *adhinat* (v 2) | **samiʿat wa-aṭāʿat** | *istiʿāra* (listen+submit) | listen+submit | listen+submit | — |
| apodosis of *idhā* | implied | **deliberate deletion** | **multi-position survey** | implied (= v 6/7) | implied |
| *al-insān* (v 6) | genus | genus | genus (embryo-arc) | **genus; or al-Aswad / Ubayy** | genus |
| *ṭabaqan ʿan ṭabaq* (v 19) | states/stages | — | — | **4-way fork** (Prophet/heaven/man/Day) | states |
| v 21 sajda obligatory? | (recited+prostrated) | — | — | **Mālik no / Ibn al-ʿArabī yes** | yes (Ṣaḥīḥayn) |

The defining structural fault-line is the **deleted apodosis** (al-Zamakhsharī's *iʿjāz* device vs
al-Rāzī's multi-position survey); the defining legal fault-line is the **Mālik ↔ Ibn al-ʿArabī**
split on whether v 21's sajda is among the *ʿazāʾim*. Both are audited empirically in 05.

## 8. Honest limits

- al-Zamakhsharī and al-Rāzī are read from full OpenITI raw concatenations; the Sūrat-84 blocks were
  located by the `# {verse-text}` headers and read in context, not from clean per-verse extractions.
- al-Rāzī's enumeration of apodosis-positions is summarized from the *Mafātīḥ* block; the exact count
  of distinct positions he lists varies by edition (00-overview cites "six"); the load-bearing fact is
  that he treats the suspended *jawāb idhā* as the surah's central crux, which all editions agree on.
- The Jibrīl *fa-innaka mulāqīh* counsel (v 6) is an Ibn-Kathīr tafsīr-citation; it is NOT located as a
  numbered ḥadīth in the on-disk 9-book database and is flagged accordingly in 04.

---

*Six commentaries cited scholar + work + passage from on-disk sources. 2026-05-30.*
