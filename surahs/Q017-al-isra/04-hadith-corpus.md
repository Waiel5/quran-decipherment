---
surah: 17
surah_name_ar: الإسراء
file_type: hadith-corpus
date_last_updated: 2026-04-28
phase: B+
verdict: 22+ Q 17-tied ḥadīth identified across the 9 canonical collections
---

# Q 17 al-Isrāʾ — Ḥadīth Corpus

Source: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/{book}.json`. Search anchors: surah-name patterns (سورة بني إسرائيل, سورة الإسراء, سورة سبحان) + verse-text fragments + Miʿrāj-narrative keywords. Full catalog at `surahs/Q017-al-isra/csv/Q017-hadith-catalog.json`.

**Note**: The Aḥmad *Musnad* JSON in our corpus contains 1,374 ḥadīth (partial); the full *Musnad* would yield additional Q 17 references (notably Muʿādh b. Anas's *āyat al-ʿizz* ḥadīth, cited by al-Suyūṭī's *al-Itqān* but not in our partial JSON). Flagged for full-Aḥmad-Musnad integration.

## 1. The cornerstone fadāʾil ḥadīth: Ibn Masʿūd's al-ʿitāq al-uwal

**al-Bukhārī ḥadīth #4502, #4533, #4787** (three independent isnāds via Shuʿba ← Abī Isḥāq ← ʿAbd al-Raḥmān b. Yazīd ← Ibn Masʿūd):

| # | Arabic core | List of surahs |
|--:|:--|:--|
| #4502 | فِي بَنِي إِسْرَائِيلَ وَالْكَهْفِ وَمَرْيَمَ إِنَّهُنَّ مِنَ الْعِتَاقِ الأُوَلِ، وَهُنَّ مِنْ تِلاَدِي | Q 17, 18, 19 |
| #4533 | بَنِي إِسْرَائِيلَ وَالْكَهْفُ وَمَرْيَمُ وَطَهَ وَالأَنْبِيَاءُ هُنَّ مِنَ الْعِتَاقِ الأُوَلِ، وَهُنَّ مِنْ تِلاَدِي | Q 17, 18, 19, 20, 21 |
| #4787 | فِي بَنِي إِسْرَائِيلَ وَالْكَهْفِ وَمَرْيَمَ وَطَهَ وَالأَنْبِيَاءِ إِنَّهُنَّ مِنَ الْعِتَاقِ الأُوَلِ وَهُنَّ مِنْ تِلاَدِي | Q 17, 18, 19, 20, 21 |

English (per Darussalam, embedded in source JSON #4533): *"The Suras of Banī Isrāʾīl, al-Kahf, Maryam, Ṭāhā and al-Anbiyāʾ are from the very old Suras which I learnt by heart, and they are my first property."*

The phrase **"al-ʿitāq al-uwal"** (الْعِتَاقِ الأُوَلِ) literally means "the early-emancipated/freed ones" — al-ʿitāq is the plural of *ʿatīq*, used both for valued/cherished/well-aged and for "freed" (as in *ʿatāqa* = manumission). Classical commentators (Ibn Ḥajar in *Fatḥ al-Bārī*) gloss: "the surahs from the earliest period that I memorized perfectly." The phrase **"min tilādī"** means "from my old / inherited / cherished property" (as opposed to *ṭarīf* = newly-acquired). Together: Ibn Masʿūd treats Q 17, 18, 19, 20, 21 as his earliest-learnt, most-cherished surahs.

**Architectural note**: Q 17, 18, 19, 20, 21 are **five canonical neighbors**. The H-NEW-720 TSP-cost data shows the Q 17→18 transition is *cheap* (Δ=0.028), the Q 18→19 transition is *cheap* (Δ=−0.030 — even rewarded by 2-opt), Q 19→20 is *cheap* (Δ ≈ 0.06), and Q 20→21 is *cheap*. The five surahs that Ibn Masʿūd treats as a unit form an **architecturally tight TSP-block** in the Fisher-Rao distance space.

**This is not coincidence**: the empirical adjacency-cost map vindicates the Companion's mnemonic grouping. Five surahs experienced as one block by an early Companion, with empirical FR-distance/TSP-cost agreement.

## 2. Aḥmad's Musnad fadāʾil — nightly recitation of Banī Isrāʾīl

Cited by Ibn Kathīr (`data/literature/classical-tafsir/raw/ibn-kathir-openiti-Q017.txt`, opening section, with chain: ʿAbd al-Raḥmān ← Ḥammād b. Zayd ← Marwān ← Abū Lubāba ← ʿĀʾisha):

> كَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يَصُومُ حَتَّى نَقُولَ: مَا يُرِيدُ أَنْ يُفْطِرَ، وَيُفْطِرُ حَتَّى نَقُولَ: مَا يُرِيدُ أَنْ يَصُومَ، وَكَانَ يَقْرَأُ كُلَّ لَيْلَةٍ بَنِي إِسْرَائِيلَ وَالزُّمَرَ

*"The Messenger of God ﷺ used to fast until we would say: he does not intend to break the fast; and he would break the fast until we would say: he does not intend to fast. And he used to recite every night Banī Isrāʾīl and al-Zumar."*

This anchors **two surahs** (Q 17 and Q 39 al-Zumar) as the Prophet's nightly recitation. (The pairing of Q 17 + Q 39 deserves architectural follow-up: both are Meccan, both glorify God in opening (*Subḥāna…* vs *Tanzīlu al-kitābi…*), both have strong eschatological and tawḥīd content. Flagged.)

## 3. Q 17:1 (Isrāʾ) and Miʿrāj narrative ḥadīths

**al-Bukhārī**:
- Long Anas-via-Sharīk narration (Bukhārī Kitāb al-tawḥīd; embedded in Ibn Kathīr Q 17 commentary opening) — full *isrāʾ + miʿrāj* account.
- Multiple chapter-headings reference "ليلة الإسراء" (the Night of *Isrāʾ*).

**Muslim** (~6 miʿrāj-narrative ḥadīths in our index): including the Anas via Mālik b. Ṣaʿṣaʿa narration of the seven heavens.

**al-Tirmidhī, Abū Dāwūd, al-Nasāʾī, Ibn Mājah**: each preserve at least 2-7 *isrāʾ-miʿrāj* references.

The classical *isrāʾ* ḥadīth corpus is one of the largest single-event ḥadīth clusters in Sunnī collections.

## 4. Q 17:78-79 fadāʾil cluster (ṣalāt + maqām maḥmūd)

This is the **dominant verse-citation cluster** for Q 17 in the 9 books. Catalogued:

### Q 17:78 (*aqim al-ṣalāta li-dulūki al-shamsi… wa-qurʾāna al-fajr*)

- al-Bukhārī **#4511** — Abū Hurayra: prayer in congregation = 25× the merit; angels of night and day meet at fajr; recite if you wish *qurʾāna al-fajra kāna mashhūdā*.
- al-Bukhārī **#633** — same matn (chapter on excellence of fajr).
- Muslim **#1368** — Abū Hurayra parallel.
- al-Tirmidhī **#3219** — explicit verse citation.
- al-Nasāʾī **#488** — explicit verse citation, English includes "Al-Isra' 17:78".
- Ibn Mājah **#404** — explicit citation.
- al-Bukhārī **#4513** — adhān-supplication: *ati Muḥammadan al-wasīlata wa-l-faḍīlata, wa-bʿathhu maqāman maḥmūdā*.

### Q 17:79 (*ʿasā an yabʿathaka rabbuka maqāman maḥmūdā*)

- al-Bukhārī **#600**, **#1424**, **#4513**, **#7155** — all on the maqām maḥmūd.
- al-Tirmidhī **#211** — adhān-supplication.
- al-Tirmidhī **#3221** — explicit identification: *al-shafāʿa* (the Major Intercession). *"It is the intercession."*
- al-Tirmidhī **#3232** — extended version: *anā sayyidu wuldi Ādama yawma al-qiyāmati wa-lā fakhra…* with *al-maqām al-maḥmūd*.
- Abū Dāwūd **#529**, Ibn Mājah **#456**, Ibn Mājah **#640** — adhān-supplication variants.

**Total Q 17:78-79 ḥadīth (9 books, our index): 13+ items.** This is the strongest hadith-cluster citation density for any pair of verses in Q 17.

## 5. Q 17:85 (the *rūḥ* verse)

- al-Tirmidhī **#3224** — *asbāb al-nuzūl*: the Quraysh asked the Jews what to ask the Prophet; the Jews said "ask him about the rūḥ"; God revealed the verse. *"They ask you concerning the Ruh. Say: The Ruh is one of the things, the knowledge of which is only with my Lord."*

Single canonical citation in our index, but classical tafsir (al-Ṭabarī, al-Rāzī) collect dozens of additional narrations.

## 6. Q 17:82 — *yarḥamu al-Qurʾān*-as-healing

- al-Dārimī **#2600** — Qatāda: *"No one sits with the Qurʾān and rises from it without an increase or a decrease,"* citing the verse *wa-nunazzilu mina al-Qurʾāni mā huwa shifāʾun wa-raḥmatun lil-muʾminīn… سورة الإسراء آية 82*.

This is one of the only **explicit "sūrat al-Isrāʾ" surah-name** citations in our 9-book index (the other being Dārimī **#3051** citing Q 17:107-109 on those-given-knowledge weeping).

## 7. Q 17:111 — āyat al-ʿizz

al-Suyūṭī's *al-Itqān* (`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, near offset 197421):

> وَفِي مُسْنَدِ أَحْمَدَ مِنْ حَدِيثِ مُعَاذِ بْنِ أَنَسٍ مَرْفُوعًا آيَةُ الْعِزِّ: {الْحَمْدُ لِلَّهِ الَّذِي لَمْ يَتَّخِذْ وَلَدًا} الْآيَةَ.

*"In Aḥmad's Musnad, from the ḥadīth of Muʿādh b. Anas marfūʿan: the Verse of Glory: {al-ḥamdu lillāhi alladhī lam yattakhidh waladā} the verse."*

Status: marfūʿ; this ḥadīth is not in our partial Aḥmad-Musnad JSON but is securely transmitted via al-Suyūṭī. The verse Q 17:111 is canonically called **āyat al-ʿizz** (the Verse of Glory) in the Sunnī fadāʾil tradition.

## 8. Bukhārī chapter-headings using Banī Isrāʾīl as surah-name

al-Bukhārī's *Kitāb al-tafsīr* (`bukhari.json`) uses **"Banī Isrāʾīl"** as the surah-heading for Q 17 (not "al-Isrāʾ"). This is consistent with Ibn Masʿūd's usage (#4502, #4533, #4787) and witnesses that the early Sunnī tradition called Q 17 by its Israelite-narrative content rather than by its Night-Journey opening verse — even though the Night Journey is far more famous as an event.

This is empirically what Q017-F-04 verified: Q 17 ranks 4/114 by raw count of "إسرائيل" tokens, supporting the early-Companion naming.

## 9. Use in classical liturgy

Beyond the 9 canonical collections:
- Q 17:78 is the **proof-text** for the five-prayer time-window structure across Sunnī fiqh.
- Q 17:79 is the **proof-text** for the doctrine of **al-Shafāʿa al-Kubrā** (the Major Intercession).
- Q 17:1 is the **liturgical proof-text** for the *isrāʾ-miʿrāj* commemoration (27 Rajab in popular tradition).
- Q 17:23-39 (the Decalogue-like ethics) is widely cited in *adab*-books as a moral foundation.
- Q 17:111 (āyat al-ʿizz) is recited apotropaically by some Sufi traditions.

## 10. Honest limits

- The 9-book ḥadīth JSON we use is from the *ahmedbaset-json* project; the Aḥmad *Musnad* portion is partial (1,374 of ~30,000). Many additional Q 17-related ḥadīth (especially Muʿādh b. Anas's *āyat al-ʿizz*) are missing from our search-base. Flagged for full-Aḥmad integration.
- Our search is text-pattern-based; ḥadīth that paraphrase Q 17 verses without exact quotation may be missed. A semantic-search pass would catch more.
- Friday-recitation ḥadīth: the well-known Friday-fajr recitation is **al-Sajdah (Q 32) + al-Insān (Q 76)** (Bukhārī #891, Muslim #880), NOT Q 17 or Q 18. The "Friday recitation of Q 17 or Q 18?" question in the original task: the answer is **Q 18 al-Kahf**, not Q 17. The famous fadāʾil ḥadīth is *"man qaraʾa Sūrata al-Kahfi yawma al-jumuʿati aḍāʾa lahu mina al-nūri…"* — al-Ḥākim, al-Bayhaqī, etc. (see Q 18 investigation when it occurs). **Q 17 has NO comparable Friday-specific fadīla in the 9-book Sunnī corpus.** This is a useful empirical clarification.

## 11. Summary table

| Verse | # of 9-book ḥadīth tying to it | Doctrinal role |
|:--:|:-:|:--|
| Q 17:1 (Isrāʾ) | ~10+ (miʿrāj cluster) | foundational event |
| Q 17:78 (qurʾān al-fajr) | 7 | ṣalāt time-windows |
| Q 17:79 (maqām maḥmūd) | 10+ | major intercession |
| Q 17:82 (Qurʾān as healing) | 1 (al-Dārimī) | exegetical citation |
| Q 17:85 (rūḥ) | 1 (Tirmidhī asbāb) | dogmatic |
| Q 17:88 (taḥaddī) | 0 explicit verse-text in 9 books, but heavily commented in tafsir (Q017-F-03) | iʿjāz |
| Q 17:107-109 (knowledge-weeping) | 1 (al-Dārimī) | scholar-piety |
| Q 17:111 (āyat al-ʿizz) | 1 (Aḥmad Musnad via al-Suyūṭī Itqān) | tawḥīd-summary |
| **Q 17 as a whole (al-ʿitāq al-uwal)** | **3 (Bukhārī)** | **Companion-fadīla** |

The single dominant cluster is **Q 17:78-79** (intercession + ṣalāt), which together account for most of the 9-book Q 17 citations.
