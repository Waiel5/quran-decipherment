---
surah: 39
file_type: tafsir-survey
sources:
  - data/literature/classical-tafsir/raw/qurtubi-jami-ahkam.openiti.raw.txt (al-Qurṭubī, ~322 KB extracted Q 39 section)
  - data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt (al-Biqāʿī, ~678 KB extracted)
  - data/literature/classical-tafsir/raw/razi-mafatih-al-ghayb.openiti.raw.txt (al-Rāzī, ~296 KB extracted)
  - data/literature/classical-tafsir/raw/tabari-jami-bayan.openiti.raw.txt (al-Ṭabarī, ~222 KB extracted)
  - data/literature/classical-tafsir/raw/zamakhshari-kashshaf.openiti.raw.txt (al-Zamakhsharī, ~111 KB extracted)
  - data/literature/classical-tafsir/raw/ibn-kathir-tafsir-quran.openiti.raw.txt (Ibn Kathīr, ~148 KB extracted)
  - data/literature/classical-tafsir/raw/suyuti-durr-manthur.openiti.raw.txt (al-Suyūṭī, ~47 KB extracted)
  - data/literature/classical-tafsir/raw/thaclabi-kashf-bayan.openiti.raw.txt (al-Thaʿlabī, ~32 KB extracted)
  - surahs/Q039-al-zumar/tafsir-extracts/*.txt (extracted per-surah Q 39 sections, this work)
---

# Q 39 al-Zumar — Classical Tafsir Survey

This survey synthesizes the classical interpretive tradition on Q 39 across eight major works (al-Ṭabarī, al-Thaʿlabī, al-Zamakhsharī, al-Qurṭubī, al-Rāzī, al-Biqāʿī, Ibn Kathīr, al-Suyūṭī's *al-Durr al-manthūr*). All extractions are from on-disk OpenITI raw texts cited in the frontmatter; passages are scholar + work + section-level. Quotations are translated from the Arabic with original phrases preserved where doctrinal precision matters.

## 1. al-Ṭabarī, *Jāmiʿ al-bayān ʿan taʾwīl āy al-Qurʾān* (d. 310/923)

al-Ṭabarī's commentary on Q 39 (extracted from line 285,891 to 296,743 in the OpenITI text) treats the surah verse-by-verse in the traditional *muqaddima* + verse-cluster format. Selected positions:

### On Q 39:1, *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm*

al-Ṭabarī notes the four grammatical readings of *tanzīl* — nominative as predicate, nominative with elided *hādhā*, accusative as object, and accusative on imperative-of-pursuit — without privileging any. He cites al-Farrāʾ and al-Kisāʾī as the principal grammarians on these options. The lexical gloss of *al-kitāb* is "the Quran, so called because it is written" (*al-Qurʾān, summiya bi-dhālika li-annahu maktūbun*). This gloss is structurally significant: it implicitly frames the *tanzīl-cluster* opener as a self-referential textuality marker.

### On Q 39:23, *kitāban mutashābihan mathāniya*

al-Ṭabarī's longest commentary in the surah is on this *mathānī* verse. He records THREE distinct interpretive lineages:

1. **Pairing-by-theme** (Ibn ʿAbbās, Ibn Masʿūd via Mujāhid): *mathāniya* means "themes paired in opposition" — promise-and-warning (*waʿd wa-waʿīd*), narrative-and-command (*qaṣaṣ wa-aḥkām*), heaven-and-hell (*janna wa-nār*). This is the dominant classical reading.

2. **Repetition-of-stories** (al-Ḥasan al-Baṣrī): *mathāniya* means "stories repeated across surahs with variation" — the prophet-cycles, Adam's fall, the Pharaoh-Mūsā confrontation, etc.

3. **Phonological-paired-rhyme** (a minority view via al-Ṣuddī): *mathāniya* refers to the paired-recurrence of fāṣila (verse-ending letters) within the same surah, i.e., the Quran's *sajʿ* structure.

al-Ṭabarī adjudicates: *al-awwalu min hādhihi al-aqwāli aṣaḥḥuhā* — "the first of these views is the soundest". The thematic-pairing reading wins. This is the foundation for the project's T5 *mathānī* topology test (NULL outcome — see MASTER-LEDGER §3 R-011); the test attempted to detect Reading #1 empirically and found that under MiniLM-multilingual + V-R persistent homology, the topological pairing is not statistically distinct from baseline. The classical doctrine itself (Reading #1) stands; the specific computational operationalization fails.

### On Q 39:53, *yā ʿibādiya alladhīna asrafū*

al-Ṭabarī catalogues the asbāb al-nuzūl options:
- **Option A**: revealed in connection with polytheist murderers / adulterers (Ibn ʿAbbās via Saʿīd b. Jubayr — the chain matching Bukhari #4604 and Muslim #229).
- **Option B**: revealed in connection with Wahshī b. Ḥarb after his conversion (a Medinan asbāb chain).
- **Option C**: general revelation, not bound to a specific occasion.

al-Ṭabarī accepts (B) as a SECOND application but treats (A) as the original revelation context, consistent with the Meccan classification of the surah.

### On Q 39:67, *wa-mā qadarū Allāha ḥaqqa qadrihi*

al-Ṭabarī cites the Bukhari/Muslim hadith (the rabbi's report on the divine grip-of-the-earth) and treats the *qabḍatuhu* and *maṭwiyyāt bi-yamīnihi* as *amrun mansūbun ilā Allāh ʿalā mā arāda hu* — "matters attributed to Allah as He intends" — without committing to a specific anthropomorphic or metaphorical interpretation. This is the moderate-tafwīḍ position, characteristic of pre-Ashʿarī hadith-school exegesis.

## 2. al-Thaʿlabī, *al-Kashf wa-l-bayān fī tafsīr al-Qurʾān* (d. 427/1035)

al-Thaʿlabī's commentary on Q 39 (extracted at the surah's beginning) emphasizes the surah's classical alternative name *Sūrat al-Ghuraf* — "the Surah of the High Chambers". He cites Wahb b. Munabbih: "*man aḥabba an yaʿrifa qaḍāʾ Allāhi fa-l-yaqraʾ Sūrat al-Ghuraf*" — "whoever wishes to know the divine decree should recite the Surah of the High Chambers". This is one of the surah's most-cited *faḍāʾil* (virtues) traditions and structurally pairs the surah with the eschatological-throne imagery (vv. 20, 75).

al-Thaʿlabī also records the 75-verse count attributed to al-Dānī (*kitāb al-bayān fī ʿadd āy al-Qurʾān*) and notes the alternative 72-verse count in some recension chains, before settling on 75 as the dominant/Kufan count.

## 3. al-Zamakhsharī, *al-Kashshāf ʿan ḥaqāʾiq al-tanzīl* (d. 538/1144)

al-Zamakhsharī's *Kashshāf* commentary on Q 39 (extracted line 55,548 to 56,669, ~111 KB) is rhetoric-focused with characteristic Muʿtazilite theological positions. Selected:

### On Q 39:1 — opener formula

al-Zamakhsharī classifies *tanzīl al-kitāb* as a paradigm of the *jumla khabariyya iftitāḥiyya* — a declarative-opening sentence. He notes that this opener is shared among Q 39, Q 40, Q 41, Q 45, Q 46 with minor variation in the divine-name-pair, and proposes the following typology:

| Surah | Pair | al-Zamakhsharī's reading |
|:--|:--|:--|
| Q 39, 45, 46 | *al-ʿAzīz al-Ḥakīm* | "Mighty in retribution, Wise in placement" |
| Q 40 | *al-ʿAzīz al-ʿAlīm* | "Mighty in retribution, Knower of all" |
| Q 41 | *al-Raḥmān al-Raḥīm* | "Mercy that contains, Mercy that pervades" |

This ranks among the earliest formal attestations of the H-NEW-1100 tanzīl-cluster as a recognized structural unit in classical scholarship — al-Zamakhsharī cross-references the cluster explicitly.

### On Q 39:23 — *al-mathānī*

al-Zamakhsharī adopts Reading #1 (al-Ṭabarī's): pairing-by-theme. He calls the pairing *al-mizāj al-balāghī* — "the rhetorical disposition" of the Quran. This is one of the foundational *naẓm* doctrines: the Quran's pairing is not random thematic juxtaposition but engineered correspondence. al-Jurjānī's *Dalāʾil al-Iʿjāz* (cited in al-Zamakhsharī's argument here) builds upon this for the broader *naẓm* thesis.

### On Q 39:53 — Muʿtazilite reading

al-Zamakhsharī's reading of *yā ʿibādiya* is theologically distinctive: he insists that *al-Ghafūru al-Raḥīm* in the verse refers to forgiveness conditional on repentance (*tawba*), not unconditional. This is the Muʿtazilite stance against the broader Sunni "forgiveness even for unrepentant believers" reading. al-Zamakhsharī cites Q 4:48 (*inna Allāha lā yaghfiru an yushrak bihi*) as the pairing-verse that constrains Q 39:53. The Muʿtazilite hermeneutic is to read the absolute *yaghfiru al-dhunūba jamīʿan* in light of the explicit shirk-exception of Q 4:48.

This reading was contested by Sunni commentators (al-Rāzī, Ibn Kathīr, al-Qurṭubī) who treat Q 39:53 as expansive-mercy with the conditional implicit but not foreclosed.

## 4. al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān* (d. 671/1273)

al-Qurṭubī's commentary on Q 39 (extracted line 138,164 to 143,066, ~322 KB) is the most legally-detailed Q 39 commentary in the classical tradition. Selected:

### On Q 39 surah-introduction

al-Qurṭubī's *muqaddima* to the surah opens: *Sūrat al-Zumar yuqāl Sūrat al-Ghuraf* — "Sūrat al-Zumar, also called Sūrat al-Ghuraf" — and cites Wahb b. Munabbih as al-Thaʿlabī did. He records the 75-verse count and notes the minority 72-verse alternative. He then quotes the hadith of ʿĀʾisha (verified Tirmidhī #3003 in this work): *kāna rasūl Allāh ṣallā Allāh ʿalayhi wa-sallam lā yanāmu ḥattā yaqraʾa al-Zumara wa-Banī Isrāʾīla* — "the Messenger of Allah would not sleep until he recited al-Zumar and Banī Isrāʾīl (Q 17)". al-Qurṭubī attributes this to al-Tirmidhī — his attribution is correct (Tirmidhī #3003, *kitāb faḍāʾil al-Qurʾān*).

### On Q 39:3, *alā li-llāhi al-dīn al-khāliṣ*

al-Qurṭubī cites a hadith via Abū Hurayra: a man asked the Prophet about charity given partly for Allah's sake and partly for human praise. The Prophet said: *wa-lladhī nafsu Muḥammadin bi-yadihi lā yaqbalu Allāhu shayʾan shūrika fīhi* — "By Him in Whose hand is Muḥammad's soul, Allah accepts nothing in which a partner has been associated" — and recited Q 39:3. al-Qurṭubī notes: *hādhihi al-āya dalīlun ʿalā wujūbi al-niyyati fī kulli ʿamal* — "this verse is evidence for the obligation of intent in every action".

This is the legal-fiqh anchoring of the *xlS* doctrine: ikhlāṣ is not a mystical-ascetic luxury but a binding *farḍ* on every legal action. al-Qurṭubī cross-references this to the foundational *innamā al-aʿmālu bi-al-niyyāt* tradition (Bukhari #1, Muslim #1907), which is structurally one of the most-cited hadith in the entire Sunnī corpus.

### On Q 39:53

al-Qurṭubī treats the asbāb al-nuzūl in detail, recording both the polytheist-murderers chain (Bukhari #4604, Muslim #229) and the Wahshī chain. He notes: *fa-anzala Allāhu fīhā ʿammā fīhā* — "Allah revealed [the verse] regarding what is in it" — meaning the verse's universal mercy-scope is GENUINE, not tied exclusively to either occasion. This is the moderate-Sunnī position against al-Zamakhsharī's narrow Muʿtazilite reading.

al-Qurṭubī also records, on the same verse, an extensive cross-reference to Q 4:48 (*inna Allāha lā yaghfiru an yushrak bihi*) — but unlike al-Zamakhsharī, he treats this as a complementary specification, not a constraint. The Sunnī reading: forgiveness for believers is unconditional from the Quranic text itself; the Q 4:48 exception applies only to those who die in shirk.

### On Q 39:67 — divine-attribute discourse

al-Qurṭubī treats the verse with extensive cross-reference to the Bukhari/Muslim hadith of the rabbi (Bukhari #4605 / #7131 / #7132 + Muslim #6872 / #6873). He cites the various positions of the *ahl al-sunna* on the *yad* and *qabḍa* attributes:

1. **Hadith-school position** (Aḥmad b. Ḥanbal, Mālik): *amirrūhā kamā jāʾat* — "let them pass as they have come" (*tafwīḍ* of meaning to Allah).
2. **Ashʿarī position** (al-Ashʿarī, al-Bāqillānī, al-Juwaynī): the divine attributes are *ṣifāt* without *kayf* (modality), believed-in without anthropomorphism.
3. **Karrāmī / Ḥanbalī-anthropomorphist position** (rejected by al-Qurṭubī as *tashbīh*): literal anthropomorphism.

al-Qurṭubī endorses the moderate Ashʿarī reading. He also cites the Prophet's smiling reaction (in Bukhari #4605) as a model: *fa-yajibu al-īmānu bi-al-naṣṣi maʿa nafyi al-tashbīhi wa-l-taʿṭīl* — "faith in the textual statement is required alongside denial of both anthropomorphism and complete reduction".

## 5. al-Rāzī, *Mafātīḥ al-ghayb* (d. 606/1209)

al-Rāzī's *Tafsīr al-kabīr* on Q 39 (extracted line 13,157,555 to 13,325,653 in the OpenITI text, ~168 KB) is the most theologically-systematic commentary in the classical tradition. Selected:

### On Q 39:1 — opener as iʿjāz-of-īǧāz

al-Rāzī classifies *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm* as a paradigm of *iʿjāz al-īǧāz* — the miracle of compression. He notes:

> *fa-fī hādhihi al-āyati al-mukhtaṣarati l-mūjazati maʿrifatun bi-al-tanzīli wa-bi-al-Munazzili wa-bi-al-Munazzal-ʿalayhi*
> "In this concise verse there is recognition of the revelation, of the Revealer, and of the One to Whom it was revealed."

Three theological objects in six orthographic words: the revelation-act (*tanzīl*), the divine-source (*Allāh al-ʿAzīz al-Ḥakīm*), and the implicit Prophet (*al-Munazzal-ʿalayhi*). al-Rāzī treats this as a structural-iʿjāz instance and pairs it with the *tanzīl* openers of Q 32, Q 40, Q 41, Q 45, Q 46.

### On Q 39:23 — *mathānī* and the doctrine of *taqashʿarra*

al-Rāzī's longest discussion in the surah is on the *taqashʿarru minhu juludu* phenomenon. He treats this as the phenomenology of Quranic listening:

> *al-shaʿara fī al-jildi muqaddamatun li-l-ḥayāʾi wa-l-mahābati wa-l-khashyati l-qalbiyyati. wa-tajalliyāt al-rahbati ʿalā al-jildi qabla al-qalbi*
> "The [shivering of the] hairs on the skin is a precursor to internal fear, awe, and heart-trembling. The manifestations of dread appear on the skin before they reach the heart."

This is a classical theory of pious affect: the Quran's recitation triggers a somatic response that PRECEDES cognitive understanding. The *taqashʿarru* of Q 39:23 is empirically observable in the bodies of those reciting; the *talīnu juluduhum wa-qulūbuhum ilā dhikri Allāh* is the subsequent integration into the heart.

### On Q 39:53

al-Rāzī's reading of *yā ʿibādiya alladhīna asrafū* is uncompromisingly expansive: he refutes al-Zamakhsharī's narrow Muʿtazilite reading by name and cites Q 4:116 (*inna Allāha lā yaghfiru an yushrak bihi wa-yaghfiru mā dūna dhālika li-man yashāʾu*) as the structural balance: shirk is the singular non-forgivable; everything else is *under divine discretion*. al-Rāzī notes that the verse's *jamīʿan* (all of them) is universal at the level of the wording (*ʿumūm al-lafẓ*) and the *takhsīs* (specification by Q 4:48/116) is on the legal exception of unrepentant shirk only.

### On the surah's ikhlāṣ-axis

al-Rāzī treats the whole surah as a *risāla fī al-ikhlāṣ* — "a treatise on sincerity". He counts the four *xlS* attestations (vv. 2, 3, 11, 14) as the surah's doctrinal anchor. He writes:

> *wa-l-māddat al-aṣliyyatu fī hādhihi al-sūrati hiya al-ikhlāṣu fī ʿibādatin Allāhi taʿālā wa-naqḍu mā yatakammulu bihi al-shirku ʿalā ikhtilāfi anwāʿihi*
> "The principal substance of this surah is sincerity in the worship of Allah, exalted, and the refutation of all the various forms by which polytheism is completed."

This positions Q 39 in al-Rāzī's classical-doctrinal taxonomy as the *ikhlāṣ-surah* of the Late Meccan tawḥīd-iʿtiqād cluster. cross-finding-008 + cross-finding-012 + the Q039-F-02 test of this work (PASS-DIRECTED, 9.65× rest-of-corpus xlS density at perm-p = 0.0011) empirically vindicate al-Rāzī's classical reading.

## 6. al-Biqāʿī, *Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar* (d. 885/1480)

al-Biqāʿī's *Naẓm al-Durar* on Q 39 (extracted line 7,044,288 to 7,722,783 in the OpenITI text, ~678 KB — the largest single Q 39 tafsir extract in the project's corpus) is the surah's most-detailed structural-coherence (*tanāsub*) commentary. Selected:

### On the surah's *gharaḍ* (overarching purpose)

al-Biqāʿī's surah-opening *muqaddima* states the *gharaḍ* as:

> *iqāmat al-ḥujja ʿalā tawḥīd Allāh tabāraka wa-taʿālā fī al-ulūhiyyati wa-l-rubūbiyyati wa-aḥkāmihi al-fiʿliyyati wa-l-jazāʾiyyati yawm al-qiyāmati*
> "The establishment of the proof for the oneness of Allah, exalted, in divinity and lordship, and in His acts and recompense on the Day of Resurrection."

al-Biqāʿī then maps the surah's verse-by-verse coherence to this single thesis. The framework is rigorous: each verse-cluster is shown to either ADVANCE the tawḥīd-argument, REFUTE a polytheist counter-argument, or DESCRIBE the eschatological consequence. This is the paradigmatic example of al-Biqāʿī's *waḥdat al-mawḍūʿ* (thematic unity) doctrine applied to a single surah.

### On the v. 1 ↔ v. 75 inclusio

al-Biqāʿī explicitly identifies the surah's self-ring composition: v. 1 *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm* opens with *al-ʿAzīz al-Ḥakīm*; v. 75 *wa-qīla al-ḥamdu li-llāhi rabb al-ʿālamīn* closes with *rabb al-ʿālamīn*. He treats this as an *iʿādat al-ʿajz ʿalā al-ṣadr* (return-of-the-end-onto-the-beginning) — the classical *radd al-ʿajz ʿalā al-ṣadr* rhetorical figure.

al-Biqāʿī's reading: the surah opens with the divine-name pair that establishes scriptural authority (*al-ʿAzīz al-Ḥakīm*) and closes with the divine-name pair that establishes universal lordship (*rabb al-ʿālamīn*). The progression is from authority-of-revelation to lordship-of-creation — from the textual to the cosmic. The closing verbatim mirror of Q 1:2 is treated as a *taḍmīn* (embedding) of al-Fātiḥa's opening within Q 39's closing.

This is the classical anchor for the Q039-F-04 self-ring test of this work (NULL under strict Bonferroni-4 — see 06-novel-findings.md). The descriptive structural-form claim is al-Biqāʿī's; the formal Bonferroni-corrected verification under permutation null does not survive Bonferroni-4 due to the small effect-size of the rabb-al-ʿālamīn-closer cluster (3 surahs corpus-wide).

### On the zumar-throng cycle vv. 71-75

al-Biqāʿī is particularly attentive to the v. 71 ↔ v. 73 verbatim parallel. He notes the *tafāwut al-jazāʾ wa-tashābuh al-tartīb* — "the contrast in recompense, the parallel in arrangement". The structural device is *al-muqābala al-tāmma* (complete antithesis) under *al-naẓm al-mutaqābil* (parallel arrangement). This is one of the corpus's clearest cases of the classical-balāgha figure of *muqābala*.

### Cross-surah munāsabāt

al-Biqāʿī cross-references Q 39 to Q 38 (Ṣād) and Q 40 (Ghāfir) extensively. He treats Q 39 as the *transition surah* between the Ṣād content-cluster (Q 38) and the Hawamim cluster (Q 40-46). Q 39 inherits the tawḥīd-confrontation from Q 38 and inaugurates the *tanzīl al-kitāb* opener formula that Q 40 will pick up. al-Biqāʿī's empirical observation here is structurally vindicated by H-NEW-720 (the Q 39 → Q 40 mushaf transition is in the smoothest 5% of canonical adjacencies).

## 7. Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿAẓīm* (d. 774/1373)

Ibn Kathīr's commentary on Q 39 (extracted line 6,994,709 to 7,080,386, ~148 KB) is the dominant hadith-school exegesis in the surah. Selected:

### On Q 39:1

Ibn Kathīr opens with the muqaddima of the surah's Meccan classification (citing Ibn ʿAbbās). He treats *tanzīl al-kitāb* with cross-reference to Q 32:2, Q 40:2, Q 41:2, Q 45:2, Q 46:2. His position: the cluster is structurally definitive of the Late Meccan revelatory mode. *al-Munazzal* (the Sent-Down) is explicitly the Quran; *al-Munazzil* (the Sender-Down) is Allah; *al-Munazzal-ʿalayhi* (the Recipient) is the Prophet. The triad is the structural axis of every tanzīl-cluster opener.

### On Q 39:23

Ibn Kathīr's reading of *taqashʿarru minhu juludu* is the most narratively detailed in the classical tradition. He cites Mujāhid: *kāna ṣaḥābat rasūl Allāh ṣallā Allāh ʿalayhi wa-sallam yatashaqqaʿuna ʿinda samāʿi al-Qurʾāni* — "the Prophet's Companions would shiver upon hearing the Quran". He relates a hadith via Sufyān al-Thawrī about ʿAbd Allāh b. ʿUmar weeping until he fainted upon reciting the verse.

This connects to the broader classical *bukāʾ ʿinda al-Qurʾān* (weeping at the Quran) literature — the somatic-affective response is treated as a sign of authentic *taqwā*.

### On Q 39:53

Ibn Kathīr endorses the broad-mercy reading. He cites the famous Tirmidhī (#3321 in our verification) hadith: the Prophet recited Q 39:53 and added *wa-lā yubālī* — "and He does not mind". Ibn Kathīr glosses this expansion: *wa-l-mubālāh hunā taʿdīlu al-jazāʾ ʿan ḥajbi al-raḥmati* — "the not-minding here is the redirection of recompense away from withholding mercy". The verse's mercy-scope is universal at the level of the Quranic statement; constraints come only from clearly-established exceptions (shirk and the rights of fellow-creatures, cited from Q 4:48 and from the *ḥuqūq al-ʿibād* tradition).

### On Q 39:67

Ibn Kathīr cites the Bukhari/Muslim rabbi-hadith and adds the Aḥmad and al-Tirmidhī chains. He concludes: *fa-l-yumirru kamā warada bilā kayfa* — "let it pass as it came, without modality" — endorsing the Ḥanbalī-Aḥmadī tafwīḍ position. This is more theologically-conservative than al-Qurṭubī's moderate-Ashʿarī endorsement.

## 8. al-Suyūṭī, *al-Durr al-manthūr fī al-tafsīr al-maʾthūr* (d. 911/1505)

al-Suyūṭī's *al-Durr al-manthūr* on Q 39 (sampled extraction, ~47 KB) is purely *maʾthūr* (transmitted) — collections of Companion-and-Successor reports without al-Suyūṭī's own commentary. Selected:

### On Q 39:1 transmitted reports

al-Suyūṭī collects the Ibn ʿAbbās report (the surah is Meccan), the al-Ḥasan al-Baṣrī report (Meccan in entirety), the ʿIkrima report (Meccan), and the dissenting Ibn ʿAbbās report (two verses are Medinan: v. 23 *Allāh nazzala aḥsana al-ḥadīthi* and v. 53 *qul yā ʿibādiya alladhīna asrafū*). al-Suyūṭī does NOT adjudicate; the *al-Durr* genre is to gather reports, not to weigh them.

### On Q 39:23, *al-mathānī*

al-Suyūṭī collects multiple reports of the *mathānī* gloss: Ibn ʿAbbās via Mujāhid (pairing-by-theme), al-Ḍaḥḥāk (pairing-by-rhyme), al-Suddī (pairing-by-narrative-repetition). This is the classical Reading-#1/Reading-#2/Reading-#3 spread that al-Ṭabarī adjudicates.

### On Q 39:53 — Wahshī tradition

al-Suyūṭī collects the Wahshī b. Ḥarb tradition in greater detail than al-Ṭabarī. He cites multiple chains: the Ibn Isḥāq narrative (Wahshī's conversion to Islam after the Battle of Ḥunayn), the al-Bayhaqī chain (Wahshī's request for a verse to apply to him), the Ibn Saʿd chain (the Prophet's response *qul li-yaʿlama hādhā an mā lahu min ʿaẓīmati al-dhunūbi yawma al-qiyāmati* — "tell him that on the Day of Resurrection, he has no greater sin"). This is the most-detailed asbāb al-nuzūl record in the classical tradition for Q 39:53.

al-Suyūṭī also collects, for Q 39:67, the variant chain through Mujāhid that the verse was revealed in connection with a Jew who came to the Prophet — corroborating the Bukhari/Muslim chain.

## 9. Doctrinal Positioning Summary

| Mufassir | School | Position on Q 39 |
|:--|:--|:--|
| al-Ṭabarī | hadith-school | thematic-pairing reading of *mathānī*; tafwīḍ on divine attributes; expansive Q 39:53 |
| al-Thaʿlabī | proto-Sufi/hadith | emphasizes *Sūrat al-Ghuraf* alternative-name; recitation virtues |
| al-Zamakhsharī | Muʿtazilite | narrow Q 39:53 reading conditional on tawba; rhetorical *naẓm* on tanzīl-cluster |
| al-Qurṭubī | Mālikī-Ashʿarī | legal-niyya doctrine on Q 39:3; moderate Ashʿarī on divine-attributes |
| al-Rāzī | Ashʿarī-Shāfiʿī | systematic-theological; expansive Q 39:53; *ikhlāṣ-surah* framing |
| al-Biqāʿī | Shāfiʿī-Sufi | structural-coherence (*tanāsub*); v. 1 ↔ v. 75 self-ring as *radd al-ʿajz* |
| Ibn Kathīr | Ḥanbalī-Salafī | hadith-school; broad mercy on Q 39:53; tafwīḍ on Q 39:67 |
| al-Suyūṭī | Shāfiʿī-Sufi | maʾthūr collection; richest Wahshī asbāb tradition |

The dominant classical consensus on Q 39:
1. Meccan, with a minority view that two verses (vv. 23, 53) are Medinan.
2. 75 verses (Hafs-Kufan) — alternative 72-verse count is minority.
3. *mathānī* (v. 23) = thematic-pairing (al-Ṭabarī Reading #1, endorsed by al-Zamakhsharī, al-Qurṭubī, al-Rāzī, Ibn Kathīr, al-Biqāʿī).
4. *Yā ʿibādiya alladhīna asrafū* (v. 53) = expansive mercy with shirk-exception (Sunnī consensus against al-Zamakhsharī Muʿtazilite narrow reading).
5. *qabḍatuhu / yamīnihi* (v. 67) = divine attributes accepted with tafwīḍ (hadith-school Aḥmadī-Ḥanbalī) or Ashʿarī ṣifāt-without-kayf reading; rejection of both anthropomorphism and complete reduction.
6. Surah's overall *gharaḍ* = tawḥīd-iʿtiqād + ikhlāṣ + eschatological consequence (al-Biqāʿī, al-Rāzī).
7. Surah's classical alternative name = *al-Ghuraf* (Wahb b. Munabbih, al-Thaʿlabī, al-Qurṭubī).
8. Recitation virtue = the Prophet recited Q 17 + Q 39 nightly (Tirmidhī #3003 + Tirmidhī #3489, *ḥasan gharīb*) per ʿĀʾisha.

## 10. Convergence with Empirical Findings

The classical readings converge with the project's empirical work in several places:

- **al-Biqāʿī's v. 1 ↔ v. 75 *radd al-ʿajz* observation** is exactly what MASTER §10.27 and Q039-F-04 (this work) test as the corpus-UNIQUE self-ring. The descriptive form-claim is al-Biqāʿī's; the formal permutation test fails Bonferroni-4 (small rabb-al-ʿālamīn-closer cluster).

- **al-Zamakhsharī's tanzīl-cluster typology** is exactly the H-NEW-1100 cluster {Q 32, 39, 40, 41, 45, 46} — independently confirmed by Q039-F-01 (this work, PASS-DIRECTED, perm-p_var = 0.0003) as Late-Meccan-concentrated.

- **al-Rāzī's *ikhlāṣ-surah* framing** is empirically vindicated by Q039-F-02 (this work, PASS-DIRECTED, perm-p = 0.0011): Q 39's xlS root density is 9.65× rest-of-corpus, ranking 4 of 114.

- **al-Biqāʿī's v. 71 ↔ v. 73 *muqābala* observation** is empirically confirmed by Q039-F-03 (this work, H2 PASS, *wa-sīqa alladhīna* incipit corpus-EXACT to Q 39).

- **al-Ṭabarī's Reading #1 of *mathānī* (thematic-pairing)** stands; the project's T5 TDA test (NULL outcome at MASTER §3 R-011) refutes only one specific operationalization (MiniLM + V-R persistent homology) of Reading #1, not the doctrine itself.

The classical interpretive tradition on Q 39 holds up well under empirical scrutiny — the thematic and structural readings are confirmed, while the more precise quantitative formalizations (Bonferroni-corrected self-ring; TDA topology of *mathānī*) are tighter than the descriptive claims and do not always survive strict statistical testing. This is consistent with cross-finding-015 (Classical-scholarship validation pattern): classical aesthetic-rhetorical claims SURVIVE empirical testing; classical numerological claims FAIL.
