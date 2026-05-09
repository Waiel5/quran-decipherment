---
surah: 63
file_type: tafsir-survey
date_last_updated: 2026-05-09
---

# Q 63 al-Munāfiqūn — Classical Tafsīr Survey

## 1. Asbāb al-Nuzūl — the Banū al-Muṣṭaliq incident

### 1.1 The historical event

The classical tradition (al-Wāqidī, *Maghāzī*; Ibn Isḥāq, *Sīra*; al-Bayhaqī, *Dalāʾil al-Nubuwwa*; al-Ṭabarī, *Tārīkh*) places the asbāb of Q 63 at **ghazwat banī al-Muṣṭaliq** (also called *al-Muraysīʿ* after the well at the battle site), in **Shaʿbān 5 AH** (per Ibn Isḥāq) or **6 AH** (per al-Wāqidī). The Banū al-Muṣṭaliq were a clan of Khuzāʿa who had begun mustering against the Muslims; the Prophet led an expedition to preempt their attack, captured them at the well of al-Muraysīʿ, and on the return journey two events triggered the surah:

1. A water-side dispute between Jahjāh al-Ghifārī (a hireling of ʿUmar) and Sinān ibn Wabra (an ally of the Anṣār) that nearly broke into intra-tribal conflict.
2. ʿAbd Allāh ibn Ubayy ibn Salūl, head of the Khazraj hypocrites, exploited this to deliver two seditious speeches:
   - *lā tunfiqū ʿalā man ʿinda rasūl Allāh ḥattā yanfaḍḍū min ḥawlihi* — "Do not spend on those with the Messenger of Allāh until they disperse from him" (= Q 63:7)
   - *la-yukhrijanna l-aʿazzu minhā l-adhall* — "The more honored shall expel the meaner thence" (i.e., the Khazraj would expel the Muhājirūn from Medina) (= Q 63:8)
3. Zayd ibn Arqam (a young companion of the Anṣār), present at the gathering, reported the speeches to his uncle, who reported them to the Prophet. ʿAbd Allāh ibn Ubayy denied the speech under oath; the Prophet initially believed the denial; Zayd was distressed at the apparent contradiction; the Prophet then received Q 63 in revelation, vindicating Zayd.

### 1.2 The hadith chain — VERIFIED on disk

The asbāb-al-nuzūl is preserved in **al-Bukhārī's Kitāb al-Tafsīr** at four numbered hadiths covering Sūrat al-Munāfiqūn:

| Hadith ID | idInBook (in `ahmedbaset-json/bukhari.json`) | Chapter | Narrator chain | Content |
|:--|:--|:--|:--|:--|
| 4692 | 4692 | 65 (Tafsīr) | ʿAbdullāh ibn Rajāʾ → Isrāʾīl → Abū Isḥāq → Zayd ibn Arqam | The boycott speech + uncle reports + Prophet calls Ibn Ubayy + Q 63 descends |
| 4693 | 4693 | 65 (Tafsīr) | Ādam ibn Abī Iyās → Isrāʾīl → Abū Isḥāq → Zayd | Same event, second isnād |
| 4695 | 4695 | 65 (Tafsīr) | ʿAmr ibn Khālid → Zuhayr ibn Muʿāwiya → Abū Isḥāq → Zayd | Detailed version: "we went out with the Prophet on a journey..." |
| 4696 | 4696 | 65 (Tafsīr) | ʿUbaydullāh ibn Mūsā → Isrāʾīl → Abū Isḥāq → Zayd | Compact narration |

**Verified locations**: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json`, search keys `إذا جاءك المنافقون` matched these 4 hadiths. (Source: scripts/Q063_F_04_hadith_verification.py)

The Bukhārī Tafsīr-book chain places the asbāb on a Zayd-ibn-Arqam → Abū-Isḥāq isnād — uniformly *ṣaḥīḥ*. **The asbāb-al-nuzūl IS in Bukhārī.** This is the verified-anchored half of the brief's classical-claim audit.

### 1.3 Disagreement on the campaign

Ibn Kathīr (*Tafsīr al-Qurʾān al-ʿAẓīm*, ad Q 63) explicitly notes the historical-discrepancy: some narrations place the event at *Tabūk*, but Ibn Kathīr ruled this *fīhi naẓar bal laysa bi-jayyid* — "questionable, indeed not good", because Ibn Ubayy did not march to Tabūk (he turned back with the dissenters at Dhū Ḥadda). Ibn Kathīr cites Ibn Isḥāq's account through Yūnus ibn Bukayr identifying the incident with *ghazwat banī al-Muṣṭaliq* (= al-Muraysīʿ), which is the **canonical asbāb** for Q 63.

## 2. Bukhārī's chapter division — *Sūrat al-Munāfiqūn* placement

Bukhārī's *Kitāb al-Tafsīr* (chapter 65) treats Q 63 in a dedicated sub-chapter, with the four hadiths above. The Bukhārī sub-chapter title — though not always recorded in the printed editions — covers the surah's asbāb. **Bukhārī does NOT, however, contain a hadith pairing Q 62 (al-Jumuʿa) and Q 63 (al-Munāfiqūn) as the Friday-prayer recitation set** (see §3 below — the pairing is in Muslim and the four sunan, not Bukhārī).

## 3. Friday-prayer recitation pairing — the **NOT-IN-BUKHĀRĪ** correction

The brief noted: *"Bukhārī ḥadīth: Friday-prayer Q 62 + Q 63 pairing recitation; verify on disk."* This specialist's verification produces a **13th hadith-attribution correction** for the project ledger.

### 3.1 What is in Bukhārī (re Friday-prayer recitation)

Bukhārī contains hadiths on the Prophet's Friday-prayer Sūrah recitation, but **none pair Q 62 and Q 63 specifically**. Bukhārī's own Friday-prayer recitation hadiths are concerned with the *Subḥ* (dawn) prayer recitation on Friday — which is documented as **Q 32 al-Sajda + Q 76 al-Insān** (Bukhārī #891, #1068, etc., Kitāb al-Jumuʿa). The Bukhārī Friday-prayer-proper sub-chapter (Bāb mā yuqraʾu fī ṣalāti l-jumuʿa) is sparse on recitation specifics in the on-disk corpus.

Verified inline: `python` search of `bukhari.json` (7,277 hadiths) for `الجمعة + المنافق` returned **0 hits**. Search by English `friday + munafiqun` returned **0 hits**. (Source: scripts/Q063_F_04_hadith_verification.py)

### 3.2 What is in Muslim, Abū Dāwūd, Tirmidhī, Nasāʾī

The Friday Q62 + Q63 recitation pairing **IS** firmly established in the four canonical sunan + Muslim:

#### Muslim — Kitāb al-Jumuʿa

**Muslim hadith #1918 (idInBook in ahmedbaset-json; standard numbering = Muslim 877 in some printed editions):**

> Marwan appointed Abū Hurayra as his deputy in Medina and he himself left for Mecca. Abū Hurayra led us in the Jumuʿa prayer and recited after Sūrat al-Jumuʿa in the second rakʿa: "When the hypocrites came to thee" (Sūrah 63). I then met Abū Hurayra as he came back and said to him: "You have recited two surahs which ʿAlī ibn Abī Ṭālib used to recite in Kūfa." Upon this Abū Hurayra said: "I heard the Messenger of Allāh ﷺ reciting these two in the Friday (prayer)."

Arabic isnād: ʿAbd Allāh ibn Maslama → Sulaymān ibn Bilāl → Jaʿfar ibn Muḥammad → his father → Ibn Abī Rāfiʿ → Abū Hurayra.

**Muslim hadith #1923 (idInBook):**

> [The] Apostle of Allāh ﷺ used to recite in the morning prayer on Friday Sūrat "Alif-Lām-Mīm Tanzīl al-Sajda" (Sūrah 32) and "Hal atā ʿalā l-insāni ḥīnun mina l-dahr" (Sūrah 76); and he used to recite in the Jumuʿa prayer **Sūrat al-Jumuʿa and al-Munāfiqīn**.

Arabic isnād: Abū Bakr ibn Abī Shayba → ʿAbda ibn Sulaymān → Sufyān → Mukhawwal ibn Rāshid → Muslim al-Baṭīn → Saʿīd ibn Jubayr → Ibn ʿAbbās.

#### Abū Dāwūd — Kitāb al-Ṣalāt

**Abū Dāwūd #1076 (idInBook):**

> In the Friday prayer he ﷺ would recite Sūrat al-Jumuʿa and Sūrat al-Munāfiqūn.

Isnād: Musaddad → Yaḥyā → Shuʿba → Mukhawwal → ... (ibn ʿAbbās chain).

**Abū Dāwūd #1125 (idInBook):**

> Abū Hurayra led us in the Friday prayer and recited Sūrat al-Jumuʿa and "When the hypocrites come to you" (Q 63) in the last rakʿa. ... Abū Hurayra said: "I heard the Messenger ﷺ reciting these two in the Friday (prayer)."

#### Tirmidhī — Abwāb al-Ṣalāt

**Tirmidhī #519 (idInBook):**

> Marwan left Abū Hurayra in charge of al-Madīna and he went to Makka. So Abū Hurayra led us in Ṣalāt on Friday, reciting Sūrat al-Jumuʿa (in the first rakʿa) and in the second prostration (rakʿa): "When the hypocrites come to you."

Isnād: Qutayba → Ḥātim ibn Ismāʿīl → Jaʿfar ibn Muḥammad → his father → ʿUbaydullāh ibn Abī Rāfiʿ.

#### Nasāʾī — Kitāb al-Jumuʿa

**Nasāʾī #1426 (idInBook in ahmedbaset-json; standard Nasāʾī Sughrā numbering = #1421):**

> During the Subḥ prayer on Friday, the Messenger of Allāh ﷺ used to recite "Alif-Lām-Mīm. The Revelation" (al-Sajda 32) and "Has there not been over man..." (al-Insān 76); and **in Jumuʿa prayer he would recite al-Jumuʿa (62) and al-Munāfiqīn (63)**.

Isnād: Muḥammad ibn ʿAbd al-Aʿlā al-Ṣanʿānī → Khālid ibn al-Ḥārith → Shuʿba → Mukhawwal → Muslim al-Baṭīn → Saʿīd ibn Jubayr → Ibn ʿAbbās.

### 3.3 Verdict — the correction

The Friday Q 62 + Q 63 recitation-pairing is:

- **NOT in Sahih al-Bukhari** (verified empty hit-set in on-disk 7,277-hadith corpus)
- **YES in Sahih Muslim** — Kitāb al-Jumuʿa (idInBook 1918, 1923 ≈ standard #877 / #882 range)
- **YES in Sunan Abū Dāwūd** — Kitāb al-Ṣalāt (idInBook 1076, 1125)
- **YES in Jāmiʿ al-Tirmidhī** — Abwāb al-Ṣalāt (idInBook 519)
- **YES in Sunan al-Nasāʾī al-Ṣughrā** — Kitāb al-Jumuʿa (idInBook 1426 ≈ standard #1421)

**The classical-claim audit recommendation**: the Friday-pairing should be cited as **Muslim #877 (or muttafaq-mostly Muslim ~ Sunan-set) tradition**, NOT as a Bukhārī tradition. The folk tradition of pairing the citation with Bukhārī (which is sometimes seen in modern apologetics) is mis-attribution; the asbāb hadiths in Bukhārī's Tafsīr book (#4692-4696) cover the *historical context* of Q 63 but do not establish the *Friday-prayer pairing*.

This is the **13th hadith-attribution correction of the project**, joining the 12 caught in earlier sessions (per HANDOFF/SESSION-HANDOFF-2026-05-09.md §2). **Filed as H-NEW-1420** in this specialist's deliverable.

## 4. Classical commentary on the surah's literary architecture

### 4.1 al-Ṭabarī, *Jāmiʿ al-Bayān*

al-Ṭabarī (d. 310/923) treats Q 63 in the context of *kitāb al-tafsīr* primarily through the asbāb-al-nuzūl narration (the Zayd ibn Arqam isnād). His commentary is **historical-philological**, not architectural. al-Ṭabarī cites several variants of Ibn Ubayy's speech (some narrations have *yanfaḍḍū min ḥawlihi*, others omit *min ḥawlihi*); the canonical text matches the *Bukhārī* version.

### 4.2 al-Zamakhsharī, *al-Kashshāf*

al-Zamakhsharī (d. 538/1144) reads Q 63 as a study in **Quranic counter-rhetoric**:

- v.1 *qālū nashhadu* ↔ *wa-llāhu yashhadu*: the divine counter-witness as a rhetorical device of *radd al-shahāda bi-l-shahāda*.
- v.2 *junnah*: he highlights this as *istiʿāra taṣrīḥiyya* (explicit metaphor) — the oath as a literal shield in defensive armor.
- v.4 *khushub musannada*: he reads this as the surah's *taqbīḥ* (defamation-figure): the hypocrites are like dead bodies propped up — beautiful in form, lifeless in substance.

al-Zamakhsharī also notes the recurrence of *lā yafqahūn / lā yaʿlamūn / lā yahdī l-qawma l-fāsiqīn* across vv. 3, 6, 7, 8 — a **fourfold negative-cognition repetition** that anchors the surah's diagnostic posture. This is consistent with al-Suyūṭī's later *al-Itqān* nawʿ on *takrār li-l-tabkīt* (repetition for shaming).

### 4.3 al-Rāzī, *Mafātīḥ al-Ghayb*

al-Rāzī (d. 606/1210) — characteristically — divides Q 63 into a **2-part structure** (vv. 1-8 hypocrite-diagnostic vs. vv. 9-11 believer-instruction) and runs detailed exegetical permutations on each verse. His distinctive contributions:

- On v.1: he identifies the *triple-shahāda* construction as *naẓmun ʿaẓīm* — argues that the *waw* in *wa-llāhu yashhadu* is *mukhālif* (contrastive), not merely conjunctive, marking the divine counter-claim against the human profession.
- On v.4 *khushub musannada*: he proposes 5 readings of the simile, including the literal (propped logs in a marketplace), the visual (statues / human-form sculptures), the tropological (lifeless bodies), and the eschatological (their corpses already condemned to hell-fire). al-Rāzī favors the *naḥnu kā-l-akhshābi l-mayyita* tropological reading as the dominant balāghah-charge.
- On vv. 7-8: he reads Ibn Ubayy's speeches as *takhāmul* (mutual conspiracy) — the hypocrites attempt to use economic-boycott as a coercion tool, and the Quran rebuts this with *theology of provision* (*li-llāhi khazāʾinu l-samāwāti wa-l-arḍ*).

### 4.4 al-Qurṭubī, *al-Jāmiʿ li-Aḥkām al-Qurʾān*

al-Qurṭubī (d. 671/1273) — most extensive on Q 63 — provides the surah's **legal-jurisprudential reading**, particularly on:

- v.5 *yastaghfir lakum rasūl Allāh*: the question of whether the Prophet's istighfār can avail the unrepentant. al-Qurṭubī addresses this with the principle of *istighfār al-mubtadiʾ vs istighfār al-mukhliṣ* (asking-on-behalf vs. seeking with sincerity).
- v.10 *anfiqū... min qabli an yaʾtiya aḥadakumu l-mawt*: the eschatological-juristic question of whether deathbed-zakat is acceptable. al-Qurṭubī cites the Mālikī consensus that obligatory deathbed-spending IS effective if the means are present, but voluntary discretionary alms after the agonies-of-death have begun is no longer effective.

### 4.5 al-Biqāʿī, *Naẓm al-Durar*

al-Biqāʿī (d. 885/1480) — the project's most-tested classical naẓm-theorist — provides the surah's **architectural-naẓm reading**. His distinctive contribution:

- Q 63 is a **diagnostic interlude** between two musabbiḥa surahs (Q 62, Q 64) — a deliberate *fāṣila* (interruption) marking the transition from *taʿẓīm-via-tasbīḥ* (glorification through declaration of God's transcendence) to *taʿẓīm-via-counter-diagnosis* (glorification through the exposure of those who falsify the *shahāda*).
- He notes the **n-f-q paronomasia** at vv. 7 + 10 explicitly: *anna lafẓa al-infāq wa-lafẓa al-nifāq min mādda wāḥida wa-hādhā ʿajab fī al-balāgha* — "the term 'spending' and the term 'hypocrisy' are from one [Arabic] root, and this is wonder in eloquence."

al-Biqāʿī's reading is **directly empirically vindicated** by this specialist's Q063-F-02 test (see 06-falsifiable-tests.md): Q 63 is corpus-rank-1 by joint n-f-q-root density, exactly as al-Biqāʿī described 540 years before the corpus-quantitative test became possible. This is one of the project's **classical-balāgha vindications** in the cross-finding-015 pattern (classical aesthetic-rhetorical claims SURVIVE empirical testing; classical numerological claims FAIL).

### 4.6 al-Suyūṭī, *al-Itqān fī ʿUlūm al-Qurʾān*

al-Suyūṭī (d. 911/1505) treats Q 63 in several nawʿs:

- *Nawʿ on al-Madanī wa-l-Makkī* (~1, 2): Q 63 is canonically Medinan; al-Suyūṭī cites *yā ayyuhā lladhīna āmanū* (v.9), *al-munāfiqūn* lemma (vv. 1, 7, 8), and the explicit asbāb (Banū al-Muṣṭaliq, post-Hijra) as triple-marker confirmation.
- *Nawʿ on tasmiyat al-suwar* (~17): Q 63 is named after its titular subject — al-Suyūṭī classifies this naming-mode as *tasmiyat al-sūra bi-mawḍūʿihā* (naming by topic), shared with Q 9 al-Tawba, Q 24 al-Nūr, Q 49 al-Ḥujurāt, Q 113 al-Falaq, Q 114 al-Nās. Predominantly Medinan.
- *Nawʿ on jinās al-ishtiqāq* (~67): al-Suyūṭī cites the Q 63 v.7-v.10 n-f-q paronomasia as one of his Quranic exemplars, naming the figure *jinās ishtiqāqī kāmil* (complete derivational paronomasia) and crediting it with *al-balāgha al-fāṣila* (decisive eloquence).

### 4.7 Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿAẓīm*

Ibn Kathīr (d. 774/1373) provides the **historical-narrative consolidation** of Q 63. His treatment:

1. Confirms *ghazwat banī al-Muṣṭaliq* as the canonical asbāb, rejects the Tabūk attribution.
2. Cites the Bukhārī + Muslim + Nasāʾī chain on Zayd ibn Arqam's narration.
3. Treats v.4 *khushub musannada* through al-Aʿrabī's lexical reading: *khashabun yābisun lā yanḥaniyyu wa-lā yantafiʿu bihi* (dry timber that does not bend and yields no use).
4. On v.10 *anfiqū*: he cites the Prophet's hadith *afḍalu l-ṣadaqati an taṣaddaqa wa-anta ṣaḥīḥun shaḥīḥun* ("the best charity is what you give while healthy and stingy") — anchoring the verse in the hadith corpus's pre-death-spending obligation.

## 5. Summary table — classical positions on Q 63 architecture

| Scholar | Block-division | Key balāghah figure | Verse-anchor cited |
|:--|:--|:--|:--|
| al-Ṭabarī | unmarked (verse-by-verse) | (not architectural) | v.1 (witness reversal) |
| al-Zamakhsharī | unmarked | counter-witness, propped-timbers, fourfold negation | v.1, v.4 |
| al-Rāzī | 2 parts (1-8 / 9-11) | triple-shahāda, takhāmul, naẓm-of-counter-rhetoric | v.1, vv.7-8 |
| al-Qurṭubī | 4 implicit (asbāb, simile, sedition, exhortation) | (legal-jurisprudential) | v.5, v.10 |
| al-Biqāʿī | 3 (musabbiḥa-interlude framing) | n-f-q paronomasia (= this specialist's Q063-F-02) | vv.7+10 |
| al-Suyūṭī | (cited in nawʿs, not block-divided) | jinās al-ishtiqāq | vv.7+10 |
| Ibn Kathīr | (verse-by-verse + asbāb consolidation) | (historical) | v.4, v.10 |
| Ibn ʿĀshūr | 4 (1-4, 5-6, 7-8, 9-11) | triple-witness + paronomasia | v.1, v.7+v.10 |

## 6. The classical-balāgha vindication

**al-Biqāʿī's claim that Q 63 instantiates corpus-distinguished n-f-q paronomasia is empirically CONFIRMED at corpus-rank-1** (this specialist's Q063-F-02). Q 63 contains 6 n-f-q-root tokens (4 munāfiq* + 2 anfaqa*) in 181 words = 3.31% root-density, 2.74× the runner-up Q 57 al-Ḥadīd, 70× the corpus-mean root-density. al-Biqāʿī (d. 885/1480) wrote this 540 years before computational corpus-analysis became possible.

This places Q 63 in the project's **cross-finding-015 classical-balāgha-survives pattern**: classical aesthetic-rhetorical claims about the Quranic text (like al-Biqāʿī's paronomasia identification) survive empirical testing, while classical numerological claims (Code-19, macro-ring, 786-uniqueness) fail. The Q 63 finding adds one more validated classical-balāgha claim to the running tally (cross-finding-015 §5 scorecard: 17+ validated, 9 refuted as of 2026-05-08).
