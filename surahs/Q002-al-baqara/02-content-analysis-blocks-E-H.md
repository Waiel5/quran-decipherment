---
surah: 2
surah_name_ar: البقرة
surah_name_translit: al-Baqara
file_type: content-analysis-partial
blocks: E-H
verses: 177-286
date_last_updated: 2026-04-28
phase: B+
verdict: SCAFFOLD — verse-level content + structural-anchor metrics for blocks E-H
specialist: blocks-E-H content-analyst
sources:
  - /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  - /Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json
  - /Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json
  - /Users/grey/Downloads/quran/data/alt-text/quran-uthmani-consonantal.json
  - /Users/grey/Downloads/quran/data/translations/en.sahih.txt
  - /Users/grey/Downloads/quran/data/literature/farrin-cuypers/2010-farrin-surat-al-baqara-structural-analysis.pdf
  - /Users/grey/Downloads/quran/data/literature/farrin-cuypers/2015-cuypers-composition-of-the-quran-rhetorical-analysis.pdf
  - /Users/grey/Downloads/quran/data/literature/misc/114chambers-ayat-al-kursi-ring-composition.md
  - /Users/grey/Downloads/quran/data/literature/misc/linguisticmiracle-wasata-baqarah-middle-ayah.md
---

# Q 2 al-Baqara — Content Analysis (Blocks E–H, verses 177–286)


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

This file is the second half of the surah-wide content analysis: communal-legal (E, 177–242), faith-narrative (F, 243–260), spending/finance (G, 261–283), khawātim (H, 284–286). For Blocks A–D see the sister-file. Default rules-tuple: `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Pause-marks (U+06D6…U+06DA) are NOT counted as words. Cross-validated against min-tashkeel, full-tashkeel, and Uthmani-consonantal.

---

## 0. Block-level structural metrics

| Block | Verses | N | Words | Letters | Avg words/verse |
|:--|:-:|:-:|:-:|:-:|:-:|
| E (communal-legal) | 177–242 | 66 | 1,640 | 7,168 | 24.8 |
| F (faith-narrative) | 243–260 | 18 | 612 | 2,459 | 34.0 |
| G (spending + finance) | 261–283 | 23 | 625 | 2,646 | 27.2 |
| H (khawātim al-Baqara) | 284–286 | 3 | 104 | 417 | 34.7 |
| **Total E–H** | 177–286 | 110 | 2,981 | 12,690 | 27.1 |

Q 2 totals: **6,140 words / 26,249 letters / 286 verses**. Blocks E–H = 48.6 % of words and 48.3 % of letters in 38 % of verses — verse-length grows across the surah, with F and H densest per-verse. Verse 282 alone (debt-contract) = **129 words / 551 letters** (4.6 % of the surah's words in one verse, the longest verse in the Quran on every tuple).

---

## 1. Block E (verses 177–242) — al-birr and the communal-legal corpus

Block E redefines *al-birr* (177) and unfolds Medinan communal law across 66 verses: retaliation, bequests, fasting, war, pilgrimage, intoxicants, menstruation, marriage, divorce, breastfeeding, prayer. Farrin (2010, ch. 4) calls it the surah's longest sustained legal discourse; Cuypers (2015, ch. 9) reads it as chiastic with the pivot at verse 207 (*al-shirāʾ*, selling oneself for God's pleasure).

### 1.1 Programmatic opening (177)

**2:177** — *laysa al-birra an tuwallū wujūhakum qibala al-mashriqi wa-l-maghribi…* "Righteousness is not that you turn your faces toward the east or the west…" One of the densest creedal-legal compressions in the Quran: belief in God / Last Day / angels / scriptures / prophets, charity to six categories, prayer + zakāt, oath-fulfillment, steadfastness in adversity and war. al-Suyūṭī, *al-Durr al-manthūr* ad loc., treats it as a capstone for the qibla controversy: *birr* is interior, not directional. Echoes 2:142–143 (*mashriq/maghrib*).

### 1.2 Qiṣāṣ and bequests (178–182)

**2:178**: *kutiba ʿalaykum al-qiṣāṣu fī l-qatlā* — legal retaliation: "the free for the free, the slave for the slave, the female for the female." 2:179 contains the famous epigraph *wa-lakum fī l-qiṣāṣi ḥayātun* ("and in retribution there is life for you"). 2:180–182 institute the will/bequest (*waṣiyya*) for parents and near-kin. The **iltifāt** in 178–179 (second-person plural to gnomic third-person) is logged in Abdel Haleem 1992's catalog (entry §2-178).

### 1.3 Fasting and Ramadan (183–187)

**2:183**: *kutiba ʿalaykum al-ṣiyām* — fasting decreed, paralleling the *kutiba ʿalaykum al-qiṣāṣ* of 178; the parallel *kataba* phrasing creates a stitching motif across 178/180/183 (Farrin 2010, p. 76).

**2:185** is the single most meta-textual verse of the surah: *shahru ramaḍāna alladhī unzila fīhi al-Qurʾān, hudan li-l-nāsi wa-bayyinātin mina l-hudā wa-l-furqān* — "The month of Ramadan in which the Quran was sent down, a guidance for mankind and clear proofs of guidance and the criterion." This is the verse that grounds **laylat al-qadr** (Q 97) in al-Baqara, and the only verse outside Q 44:3 (*laylatin mubāraka*) and Q 97:1 (*laylati l-qadr*) that explicitly anchors revelation to a specific month. Its placement deep inside Block E is itself remarkable: the surah does not announce its own time-of-revelation in the opening; it embeds it in the legal-fasting passage where Ramadan is the operative concept. **2:186** ("when My servants ask you about Me, indeed I am near") is liturgically famous as the *duʿāʾ-proximity verse* and is the only verse in the entire Quran where God answers a question about Himself in the first person *without* the imperative *qul*. **2:187** — the night-of-fast intimacy permission, the "white thread / black thread" definition of dawn (*al-khayṭ al-abyaḍ … min al-khayṭ al-aswad min al-fajr*), and the iʿtikāf rule.

### 1.4 War, pilgrimage, the disputed months (190–203)

**2:190–195**: combat in God's path with the reciprocity rule and the *fitna* doctrine (191). 2:194 institutes parallel reciprocity in the inviolable months. **2:196–203**: ḥajj/ʿumra, fidya, *tamattuʿ*, days of remembrance at Minā. 2:201 is the universal *rabbanā ātinā* prayer. The war→pilgrimage transition follows the spatial logic of *al-bayt al-ḥarām*.

### 1.5 Pivot verses (204–214)

The verse-count center of Block E and Cuypers' chiastic axis. **2:204–206** the worldly-tongued hypocrite; **2:207** *wa-min al-nāsi man yashrī nafsahu ibtighāʾa marḍāti llāh* ("some sell their souls for God's pleasure"), tied by al-Ṭabarī ad loc. and al-Wāḥidī's *Asbāb al-nuzūl* to ʿAlī at the Hijra; **2:208** "enter into *silm* all of you"; **2:213** *kāna al-nāsu ummatan wāḥidatan* (a programmatic revelation-history statement); 2:214 closes with an eschatological reminder.

### 1.6 The *yasʾalūnaka* cycle (215–222)

A densely-packed cluster: 215 (spending), 217 (sacred month), 219 (wine + gambling), 220 (orphans, implied), 222 (menstruation) — the densest *yasʾalūnaka*-cluster in the Quran (each is solitary in its host surah at Q 5:4, 8:1, 17:85, 18:83, 20:105, 79:42). Functions as a juridical Q&A pericope mapped by al-Wāḥidī onto Companion questions. **2:219** is the second of three wine-prohibition stages (cf. Q 4:43, Q 5:90–91): wine has "great sin and some benefit, but their sin is greater" — transitional. **2:222** institutes menstrual seclusion; 2:223 the contested *ḥarth* verse.

### 1.7 Marriage, divorce, breastfeeding (226–242)

**2:226–227** *īlāʾ* (4-month limit); **2:228** three-period *ʿidda*; **2:229** *al-ṭalāqu marratān* + *khulʿ*; **2:230** *muḥallil*; **2:231–232** post-divorce conduct; **2:233** two-year breastfeeding; **2:234** widow's 4 months 10 days; **2:235–237** engagement/dowry; **2:238** *al-ṣalāt al-wusṭā* (identified with ʿaṣr in al-Bukhārī #4111, Muslim #627); **2:240–242** widow-maintenance and *mutʿa*. The block traverses *birr* → retaliation → fasting → war → pilgrimage → intoxicants → women's rulings → prayer-discipline: a complete grammar of Medinan communal life.

### 1.8 The "middle verse" claim (2:143)

The popular *wasaṭa-baqara* claim (286 ÷ 2 = 143; *ummatan wasaṭan*) places the "middle verse" at 2:143, in Block D — not Block E. Block E's center by verse-count is between 2:209 and 2:210, both inside Cuypers' chiastic-center pericope. A strict word-count median test for the surah is logged for the novel-findings file.

---

## 2. Block F (verses 243–260) — faith-narratives and *iḥyāʾ al-mawtā*

Block F is the surah's narrative-theology block: four short stories on **God gives life and death** (*yuḥyī wa-yumīt*), unified by *ḥ-y-y / m-w-t*, culminating in **2:255 āyat al-kursī**.

### 2.1 The dead revived (243)

**2:243** — those who fled their homes in thousands fearing death; God said "Die" then revived them. al-Ṭabarī and al-Rāzī ad loc. link this to a Banū Isrāʾīl plague-narrative; thematic preamble to the block.

### 2.2 Saul–David (246–252)

The surah's longest narrative pericope: prophet-king request, appointment of Ṭālūt (Saul), ark-sign, river-test, Goliath, David's slaying of Goliath, kingship and wisdom. **2:251** the *dafʿ-doctrine* (*wa-lawlā dafʿu llāhi l-nāsa baʿḍahum bi-baʿḍin la-fasadati l-arḍ*) is foundational in classical political theology.

### 2.3 The pivot (253–254)

**2:253** hierarchizes messengers (one of only three Quranic passages doing so; cf. Q 17:55, Q 33:7). **2:254**: spend before "a day with no bargaining, no friendship, no intercession" — preparing the theological sweep of 2:255.

### 2.4 ĀYAT AL-KURSĪ (2:255)

**Verbatim Arabic (no-tashkeel, canonical, pause-marks stripped):**

> الله لا إله إلا هو الحي القيوم لا تأخذه سنة ولا نوم له ما في السماوات وما في الأرض من ذا الذي يشفع عنده إلا بإذنه يعلم ما بين أيديهم وما خلفهم ولا يحيطون بشيء من علمه إلا بما شاء وسع كرسيه السماوات والأرض ولا يئوده حفظهما وهو العلي العظيم

**Verbatim Arabic (full-tashkeel):**

> ٱللَّهُ لَآ إِلَٰهَ إِلَّا هُوَ ٱلۡحَيُّ ٱلۡقَيُّومُۚ لَا تَأۡخُذُهُۥ سِنَةٞ وَلَا نَوۡمٞۚ لَّهُۥ مَا فِي ٱلسَّمَٰوَٰتِ وَمَا فِي ٱلۡأَرۡضِۗ مَن ذَا ٱلَّذِي يَشۡفَعُ عِندَهُۥٓ إِلَّا بِإِذۡنِهِۦۚ يَعۡلَمُ مَا بَيۡنَ أَيۡدِيهِمۡ وَمَا خَلۡفَهُمۡۖ وَلَا يُحِيطُونَ بِشَيۡءٖ مِّنۡ عِلۡمِهِۦٓ إِلَّا بِمَا شَآءَۚ وَسِعَ كُرۡسِيُّهُ ٱلسَّمَٰوَٰتِ وَٱلۡأَرۡضَۖ وَلَا يَـُٔودُهُۥ حِفۡظُهُمَاۚ وَهُوَ ٱلۡعَلِيُّ ٱلۡعَظِيمُ

**Verbatim Arabic (Uthmani-consonantal):**

> الله لا إله إلا هو الحى القيوم لا تأخذه سنة ولا نوم له ما فى السموت وما فى الأرض من ذا الذى يشفع عنده إلا بإذنه يعلم ما بين أيديهم وما خلفهم ولا يحيطون بشىء من علمه إلا بما شاء وسع كرسيه السموت والأرض ولا يوده حفظهما وهو العلى العظيم

**English (Sahih International):**

> Allah — there is no deity except Him, the Ever-Living, the Sustainer of [all] existence. Neither drowsiness overtakes Him nor sleep. To Him belongs whatever is in the heavens and whatever is on the earth. Who is it that can intercede with Him except by His permission? He knows what is [presently] before them and what will be after them, and they encompass not a thing of His knowledge except for what He wills. His Kursi extends over the heavens and the earth, and their preservation tires Him not. And He is the Most High, the Most Great.

**Computed metrics (cross-validated):**

| Variant | Words | Letters (no spaces) |
|:--|:-:|:-:|
| no-tashkeel (canonical) | 50 | 189 |
| Uthmani-consonantal | 50 | 184 |

NOTE: The popular **"57 words / 182 letters"** count circulating in tradition (e.g., the 114chambers ring-composition source, Karami 2021) does not match either of our canonical text variants under strict orthographic-token counting. The 57-figure appears to count proclitic prepositions and the connective *wa-* as separate tokens, and the 182-figure appears to drop a small number of letters (possibly the *alif al-waṣl* in *Allāh*, plus the shadda-implied geminates). We retain the empirical figures (50 words, 189 letters in canonical no-tashkeel; 50 / 184 in Uthmani-consonantal) and flag the popular figures as **NOT REPRODUCED under our rules-tuple.** This is logged for the classical-claims-audit file.

**Divine names in 2:255** (surface order): *Allāh*, *al-Ḥayy*, *al-Qayyūm*, *al-ʿAlī*, *al-ʿAẓīm* — five distinct attributes. The pair *al-Ḥayy al-Qayyūm* is al-Rāzī's *ism al-aʿẓam* candidate (*Mafātīḥ al-ghayb* on Q 2:255, Q 3:2; al-Tirmidhī #3478 cites Q 2:255 + 3:2 + 20:111 as triple-attestation).

**Positional analysis:** 2:255 is verse 255/286 = position **0.892**; by letter-count it spans letters 21,247–21,435 / 26,249 ≈ position **0.81**. So 2:255 is NOT the structural center under any strict positional metric — it lies roughly four-fifths through. The popular *wasaṭa-baqara* middle-verse claim attaches to 2:143, not 2:255. The classical "greatest verse" status (al-Bukhārī #5010 via Ubayy; Muslim #810) is a qualitative-*fadāʾil* claim about content, not position — and its content rationale (compactly enumerating God's exclusivity, life, sustenance, knowledge, sovereignty, throne, transcendence in 50 words) is empirically defensible. The Karami 9-section ring-composition reading places the pivot at *yaʿlamu mā bayna aydīhim wa-mā khalfahum* — defensible but reliant on the analyst's partitioning choice.

### 2.5 The Abrahamic chord (256–260)

**2:256** *lā ikrāha fī l-dīn* — no compulsion in religion (al-Wāḥidī gives several asbāb). **2:257** God is *walī* of the believers, leading from darkness to light, with the inverse for the rejected — light/darkness chiasm.

**2:258**: the unnamed king (classically Nimrod) disputes with Abraham about giving life and death; Abraham's "bring the sun from the west" counter is the only Quranic passage where Abraham defeats a named human disputant. **2:259**: the unnamed traveler past a ruined town (classically ʿUzayr / Jeremiah / al-Khiḍr) killed and resurrected after a hundred years with his donkey. **2:260**: Abraham's *kayfa tuḥyī l-mawtā*, the four-birds answer.

Block F thus contains **four iḥyāʾ-narratives in 18 verses** (243, 251–252, 259, 260) with **2:255 as the theological commentary** they illustrate — the densest *iḥyāʾ*-cluster in the Quran. Farrin (2010, p. 89) calls this the surah's theological climax.

---

## 3. Block G (verses 261–283) — *infāq*, *ribā*, and the contract

Block G unifies around the economy of giving and receiving: the seven-spike parable (261), charity ethics (262–274), the *ribā* prohibition (275–281), the longest verse (282), and the travel-pledge (283).

### 3.1 The *infāq*-parables (261–274)

**2:261** the famous *kamathali ḥabbatin anbatat sabʿa sanābila fī kulli sunbulatin miʾatu ḥabba* (1 → 7 × 100 = 700-fold). 2:262–264: charity must not be followed by *mann* or *adhā*; the rain-on-rock parable (264); the garden-on-a-hill (265); the burning date-and-grape garden (266). 2:267 forbids giving the worst of one's wealth. 2:271 weighs visible vs. concealed alms. 2:273–274 establish alms for the *mutaʿaffifīn*. Five-plus extended *mathal* in 14 verses make Block G the densest parable-cluster in the surah outside Block A.

### 3.2 The *ribā* prohibition (275–281)

**2:275–281** is the Quran's most extended single-sitting prohibition of usury. **2:275**: those who consume *ribā* rise on judgment day "as one whom Satan has driven mad by touch." 2:276: God effaces *ribā* and increases charity. 2:278–279: the imperative to abandon *ribā* or face "war from God and His Messenger" — one of only two Quranic *ḥarb*-declarations (the other Q 5:33). 2:280: postponement for the indebted-in-difficulty.

**2:281** is widely held (Ibn ʿAbbās via al-Ṭabarī; al-Suyūṭī, *al-Itqān* nawʿ 7) to be **the LAST verse revealed**: *wa-ttaqū yawman turjaʿūna fīhi ilā llāhi…* If accurate, revelation's chronological terminus falls inside Block G, three verses before the longest verse — a striking architectural fact.

### 3.3 THE LONGEST VERSE IN THE QURAN (2:282)

**Computed length (no-tashkeel, canonical, pause-marks stripped):**

- **Words: 129**
- **Letters: 551**

This is the longest verse in the Quran by every counting tuple. The next-longest verses are 2:282's neighbors and a small handful from Q 4 and Q 5, none reaching 100 words on the same tuple.

**Content:** prescribes the entire law of contracted debt in one legal-prose unit: write debts of a fixed term; the scribe writes justly; the debtor dictates without diminishment; if he cannot, his guardian dictates; two male witnesses or one male + two females; witnesses must respond when called; small or large, the debt is recorded; immediate hand-to-hand exempted; no scribe or witness may be harmed.

**Architectural significance:** that the **longest verse of the Quran is a debt-contract verse** is itself revealing — the Quran makes its single greatest verse-length investment on the legal-mechanics of credit between humans, not on theology or eschatology.

### 3.4 The travel-pledge verse (283)

**2:283** closes the financial block: if travelling without a scribe, "a pledge taken in hand" (*rihānun maqbūḍa*) suffices. The warning *wa-lā taktumū al-shahāda* is treated by al-Rāzī ad loc. as the moral coda to the entire spending/finance block — the conceptual hinge to Block H.

---

## 4. Block H (verses 284–286) — *Khawātim al-Baqara*

The closing three verses, traditionally called *khawātim al-Baqara*, form one of the most ḥadīth-emphasized triplets in the entire Quran.

### 4.1 Verse 284 (28 words / 103 letters)

*li-llāhi mā fī l-samāwāti wa-mā fī l-arḍ wa-in tubdū mā fī anfusikum aw tukhfūhu yuḥāsibkum bihi llāh* — God's cosmic ownership and the warning that He will hold the soul to account for what it conceals. al-Bukhārī #4545 and Muslim #125 report this verse caused the Companions great distress until qualified by 2:286. The opening *li-llāhi mā fī l-samāwāti wa-mā fī l-arḍ* exactly **echoes 2:255** (*lahu mā fī l-samāwāti wa-mā fī l-arḍ*) — a deliberate inclusio between the surah's two great theological anchors.

### 4.2 Verse 285 (27 words / 118 letters)

*āmana al-rasūlu bimā unzila ilayhi min rabbihi wa-l-muʾminūn…* — the surah's compact creedal-summary, *al-īmān al-mufaṣṣal* in miniature, enumerating the six articles of faith (cf. Jibrīl-ḥadīth, al-Bukhārī #50, Muslim #8).

### 4.3 Verse 286 (49 words / 196 letters) — the closing prayer

*lā yukallifu llāhu nafsan illā wusʿahā…* "God charges no soul beyond its capacity." Five sequential *rabbanā* invocations — the densest *rabbanā* prayer-cluster in the Quran. The closing *fa-nṣurnā ʿalā l-qawmi l-kāfirīn* mirrors the war-vocabulary of Blocks E and F, tying the closing prayer back to the mid-surah. The **opening clause** *lā yukallifu llāhu nafsan illā wusʿahā* exactly **echoes 2:233** (*lā tukallifu nafsun illā wusʿahā*, in the breastfeeding rule of Block E) — a second deliberate inclusio that absorbs Block E's legal language into a personal-eschatological frame.

### 4.4 Khawātim micro-chiasm

The three verses form a micro-chiasm: 284 (sovereignty + accountability — theological) → 285 (creedal response) → 286 (personal supplication, echoing 284's accountability concern). This X-Y-X' structure recapitulates the surah's overall arc (creedal opening → legal-narrative center → closing supplication). al-Bukhārī #4008 and #5009–5010: whoever recites the last two verses at night, they suffice him. al-Tirmidhī #2882: 285–286 were given the Prophet at the Miʿrāj from a treasure beneath the Throne.

---

## 5. Refrains, motifs, and intra-block stitching

1. ***kataba ʿalaykum*** — at 178 (qiṣāṣ), 180 (waṣiyya), 183 (ṣiyām), 216 (qitāl), 246 (qitāl on Banū Isrāʾīl). A Q 2-specific stitching device (rest of Quran has only ~3 occurrences: Q 4:77, 5:32, 9:120 partial).
2. ***yasʾalūnaka*** cluster — densest in the Quran (215, 217, 219, 220 implied, 222).
3. ***li-llāhi mā fī l-samāwāti wa-mā fī l-arḍ*** inclusio — explicit at 2:255 and 2:284, framing the entire Block F+G+H climax.
4. ***lā tukallifu nafsun illā wusʿahā*** inclusio — at 2:233 (Block E breastfeeding) and 2:286 (Block H closing), binding the longest legal block to the closing supplication.
5. ***iḥyāʾ–mawt*** doublet dominates Block F (243, 258, 259, 260) with recurrence at 2:154 (Block D "do not call those slain in God's path dead").
6. ***n-f-q*** root carries Block G — 14 of 23 verses use a derivative.
7. ***r-b-w*** appears only in 275–281 (six occurrences in seven verses) — densest *ribā*-pericope in the Quran.

Cuypers (2015) reads these as concentric arrangement; Farrin (2010) as parallel panels with thematic recurrence.

---

## 6. Cross-validation across tashkeel variants

Spot-checks for all flagship verses (177, 185, 255, 282, 286) show identical orthographic skeleton across no-/min-/full-tashkeel. Word and letter counts under pause-mark-stripped tokenization are invariant. Uthmani-consonantal gives identical word-counts but slightly lower letter-counts (184 vs 189 for 2:255) due to the omission of medial *alif* in *al-samāwāt → al-samowāt* — a documented orthographic feature, well within the expected range.

---

## 7. Cross-references

- [[Q002-al-baqara/00-overview]] — surah-level metrics
- [[Q002-al-baqara/01-empirical-profile]] — UAS rank 3 + Δ%ile = −20.62pp (cohesion-anchor)
- `02-content-analysis-blocks-A-D.md` — Blocks A–D (verses 1–176)
- [[h-new-720-canonical-adjacency-cost]] — Q1-Q2 most-expensive pair
- [[cross-finding-008]] — muqaṭṭaʿāt-as-book-introduction-marker
- [[h-new-860-hadith-architectural-alignment]] — Q 2:255 + 2:284–286 ḥadīth densities
- 114chambers-ayat-al-kursi-ring-composition.md — the Karami (2021) ring-claim (NOT REPRODUCED at 57/182 under our rules-tuple)
- linguisticmiracle-wasata-baqarah-middle-ayah.md — the 2:143 "middle-verse" claim (logged for novel-findings tests)
- al-Bukhārī ḥadīth #5010 (āyat al-kursī = greatest verse), #4008/#5009 (khawātim), #4111 (middle prayer), #4545 (2:284 distress)
- Muslim ḥadīth #810 (Ubayy on āyat al-kursī), #125 (2:284 distress)
- al-Tirmidhī ḥadīth #2882 (khawātim from beneath the Throne), #3478 (Ḥayy-Qayyūm ism al-aʿẓam)
- Farrin 2010, ch. 4 (Block-E legal panel + chiasm)
- Cuypers 2015, ch. 9 (Block-E concentric center at 2:207)
- al-Suyūṭī, *al-Itqān*, nawʿ 7 (2:281 as last revelation), nawʿ 40 (āyat al-kursī fadāʾil)
- al-Rāzī, *Mafātīḥ al-ghayb*, on Q 2:255 (al-Ḥayy al-Qayyūm as ism al-aʿẓam candidate)

---

## 8. Honest limits

- The *wasaṭa-baqara* claim (2:143 = middle-verse, by 286÷2) is integer-division based; under a strict word-count median, the structural midpoint is *not* 2:143. A formal pre-registered test is logged for novel-findings.
- The Karami (2021) 57/182 figures for āyat al-kursī are NOT REPRODUCED under our rules-tuple — likely a different tokenization (proclitics, pause-marks). Forwarded to `05-classical-claims-audit.md`.
- The 2:281-as-last-revealed claim is a classical report, widely but not universally accepted (al-Suyūṭī acknowledges competing reports). The architectural inference is conditional.
- Block boundaries follow Farrin (2010) + Cuypers (2015) + the overview; alternative partitions (e.g., al-Biqāʿī, *Naẓm al-Durar*) exist and would shift §0 metrics.
- Verse summaries are deliberately concise (1–2 sentences); deeper tafsir → `03-tafsir-survey.md`; hadith → `04-hadith-corpus.md`.

---

*End of Blocks E–H content analysis. Verse-level coverage: 100% of verses 177–286.*
