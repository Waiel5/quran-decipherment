---
surah: 36
surah_name_ar: يس
surah_name_translit: Yāsīn
file_type: hadith-corpus
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — 9 books surveyed; 5 substantive hadith identified; 1 chain-graded by Tirmidhī himself in our corpus
---

# Q 36 Yāsīn — Hadith Corpus Survey


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

## 0. Source

All hadith below are sourced from `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/*.json`. Each citation gives `idInBook` (the conventional within-book numbering used by ahmedbaset-json's metadata) and `id` (the global cross-corpus integer). The Q 36-relevant pattern matches were performed by Arabic-text searches for `يَاسِين` / `ياسين` / `سُورَةُ يس` and English-text searches for `Yasin` / `Ya[\s-]Sin` (excluding common false positives from particles `لَيس`/etc.). Note: the dedicated hadith-collection directories `bukhari/`, `muslim/`, `tirmidhi/`, `abu-dawud/`, `nasai/`, `ibn-majah/` under `data/literature/hadith/` are empty stubs in our local corpus; the substantive data lives in the ahmedbaset-json bundle.

## 1. The *qalb al-Qurʾān* tradition

### 1.1 al-Tirmidhī, *Sunan*, idInBook 2970 (global id 28750)

Full Arabic and English text:

> حَدَّثَنَا قُتَيْبَةُ وَسُفْيَانُ بْنُ وَكِيعٍ، قَالاَ حَدَّثَنَا حُمَيْدُ بْنُ عَبْدِ الرَّحْمَنِ الرُّؤَاسِيُّ، عَنِ الْحَسَنِ بْنِ صَالِحٍ، عَنْ هَارُونَ أَبِي مُحَمَّدٍ، عَنْ مُقَاتِلِ بْنِ حَيَّانَ، عَنْ قَتَادَةَ، عَنْ أَنَسٍ، قَالَ قَالَ النَّبِيُّ صلى الله عليه وسلم "إِنَّ لِكُلِّ شَيْءٍ قَلْبًا وَقَلْبُ الْقُرْآنِ يس وَمَنْ قَرَأَ يس كَتَبَ اللَّهُ لَهُ بِقِرَاءَتِهَا قِرَاءَةَ الْقُرْآنِ عَشْرَ مَرَّاتٍ".
>
> **قَالَ أَبُو عِيسَى هَذَا حَدِيثٌ غَرِيبٌ لاَ نَعْرِفُهُ إِلاَّ مِنْ حَدِيثِ حُمَيْدِ بْنِ عَبْدِ الرَّحْمَنِ وَبِالْبَصْرَةِ لاَ يَعْرِفُونَ مِنْ حَدِيثِ قَتَادَةَ إِلاَّ مِنْ هَذَا الْوَجْهِ. وَهَارُونُ أَبُو مُحَمَّدٍ شَيْخٌ مَجْهُولٌ.**

(English): "Indeed for everything there is a heart, and the Qurʾān's heart is Yāsīn. Whoever recites Yāsīn, then for its recitation, Allāh writes for him that he recited the Qurʾān ten times."

**al-Tirmidhī's own grading (within the entry text itself)**:
- *gharīb*: "We do not know [this hadith] except from [the route of] Ḥumayd b. ʿAbd al-Raḥmān".
- *shaykh majhūl*: "Hārūn Abū Muḥammad is an **unknown** shaykh".
- The cross-chain (via Abū Bakr al-Ṣiddīq, mentioned in the closing *fī al-bāb*-block of the same entry): "**lā yaṣiḥḥu min qibal isnādih, isnāduhu ḍaʿīf**" — "the chain is not authentic; its isnād is weak".

This is the **canonical *qalb al-Qurʾān* hadith** referenced as "Tirmidhī #2887" in popular Sunnī-tradition literature. The numbering "2887" reflects al-Tirmidhī's own kitāb-fadāʾil-al-Qurʾān numbering; in the ahmedbaset-json our entry sits at idInBook 2970 (global 28750). The chain weakness is documented in al-Tirmidhī's own text — the project does not need external graders to establish the *gharīb*-level grading.

### 1.2 al-Tirmidhī's grading: corpus-internal vs modern critic

| Grader | Position |
|:--|:--|
| al-Tirmidhī (in-text) | *gharīb* + *shaykh majhūl* (Hārūn Abū Muḥammad) |
| Cross-chain (via Abū Bakr al-Ṣiddīq, in-text) | *isnāduhu ḍaʿīf* |
| al-Dāraquṭnī (classical hadith critic) | rejected the chain through Hārūn |
| Ibn al-Jawzī | included in his *al-Mawḍūʿāt* (forged-hadith register) under Hārūn-related transmissions |
| al-Albānī (modern) | ḍaʿīf jiddan / mawḍūʿ via Hārūn Abū Muḥammad (per [[h-new-82-yasin-heart|H-NEW-82]] §2 and the H-NEW-82 *substantive interpretation* §1 reference) |
| Ibn Kathīr | "infarada bihī Aḥmad" — sole-narration through Aḥmad (not through the *Ṣaḥīḥayn*) |

The *qalb al-Qurʾān* hadith is **NOT in al-Bukhārī or Muslim** (verified: 0 matches in our corpus's `bukhari.json` and `muslim.json` for the *qalb al-Qurʾān* phrase or related Yāsīn-substantive content). This is consistent with the chain-grading: a *gharīb* hadith with a *majhūl* shaykh would not pass the *Ṣaḥīḥayn* threshold.

### 1.3 al-Suyūṭī al-Durr-cited supplementary chain (al-Bazzār via Abū Hurayra)

al-Suyūṭī, *al-Durr al-manthūr*, Q 36 opening (raw offset ~6,780,086) cites a parallel chain through al-Bazzār via Abū Hurayra: "إن لكل شيء قلبا وقلب القرآن (يس)". This chain is post-canonical and is not in our 9-book JSON. The multiple-chain testimony slightly strengthens the tradition's *fadāʾil*-grade status (in classical Sunnī methodology, *ḍaʿīf-fadāʾil*-hadiths can be acted upon if multiple chains converge), but it does not lift the chain to *ṣaḥīḥ* / *ḥasan*.

## 2. The "recite Yāsīn over your dying" tradition

### 2.1 Abū Dāwūd, *Sunan*, idInBook 3122 (global id 23626)

Full text:

> حَدَّثَنَا مُحَمَّدُ بْنُ الْعَلاَءِ، وَمُحَمَّدُ بْنُ مَكِّيٍّ الْمَرْوَزِيُّ، - الْمَعْنَى - قَالاَ حَدَّثَنَا ابْنُ الْمُبَارَكِ، عَنْ سُلَيْمَانَ التَّيْمِيِّ، عَنْ أَبِي عُثْمَانَ، - وَلَيْسَ بِالنَّهْدِيِّ - عَنْ أَبِيهِ، عَنْ مَعْقِلِ بْنِ يَسَارٍ، قَالَ قَالَ النَّبِيُّ صلى الله عليه وسلم: "اقْرَءُوا يس عَلَى مَوْتَاكُمْ".

(English): Narrated Maʿqil b. Yasār: "The Prophet (peace and blessings be upon him) said: Recite Sūrat Yāsīn over your dying men."

**Note in our entry**: "Wa-hādhā lafẓu Ibn al-ʿAlāʾ" (and this is the wording of Ibn al-ʿAlāʾ).

The conventional reference "Abū Dāwūd #3121" sometimes used in popular literature corresponds to this entry under our corpus's idInBook 3122 (global 23626). Off-by-one numbering reflects different editions' counting of preceding super-entries; this is the canonical citation.

### 2.2 Ibn Mājah, *Sunan*, idInBook 1182 (global id 31015)

> حَدَّثَنَا أَبُو بَكْرِ بْنُ أَبِي شَيْبَةَ، حَدَّثَنَا عَلِيُّ بْنُ الْحَسَنِ بْنِ شَقِيقٍ، عَنِ ابْنِ الْمُبَارَكِ، عَنْ سُلَيْمَانَ التَّيْمِيِّ، عَنْ أَبِي عُثْمَانَ، - وَلَيْسَ بِالنَّهْدِيِّ - عَنْ أَبِيهِ، عَنْ مَعْقِلِ بْنِ يَسَارٍ، قَالَ قَالَ رَسُولُ اللَّهِ ـ صلى الله عليه وسلم ـ: "اقْرَءُوهَا عِنْدَ مَوْتَاكُمْ" يَعْنِي يس.

(English): Narrated Maʿqil b. Yasār: "Recite Qurʾān near your dying ones — meaning Yāsīn".

### 2.3 Chain analysis

Both hadiths share the chain: Ibn al-Mubārak ← Sulaymān al-Taymī ← Abū ʿUthmān (NOT al-Nahdī, per the in-text disambiguation `wa-laysa bi-l-Nahdī`) ← his father ← Maʿqil b. Yasār ← the Prophet.

Critical chain-weaknesses:
- **Abū ʿUthmān ("not al-Nahdī") is the named non-Nahdī Abū ʿUthmān**: classical critics identify him as ambiguously-attested or unknown. The disambiguating phrase "*laysa bi-l-Nahdī*" is itself the editor's note that the well-attested Abū ʿUthmān al-Nahdī is NOT the narrator here.
- **"His father" is unnamed**: a chain with an unnamed-father link is structurally weaker.

Modern grading (per [[h-new-82-yasin-heart|H-NEW-82]] §2):
- al-Albānī: ḍaʿīf
- al-Dāraquṭnī, Ibn al-Qaṭṭān: chain-defects in Abū ʿUthmān
- some scholars (Ibn Ḥibbān) consider it ḥasan via the multiple chains

**This hadith is the basis for the contemporary practice of reciting Sūrat Yāsīn at deathbeds and graveyards**. The textual grade is **disputed but tending ḍaʿīf**. The popular liturgical practice rests on: (a) the multiple chains through Maʿqil b. Yasār, (b) the *fadāʾil*-of-amal principle that ḍaʿīf-fadāʾil hadiths can ground devotional practice, (c) the cross-corpus prevalence (Abū Dāwūd + Ibn Mājah + Aḥmad's *Musnad* — see §4 below).

## 3. al-Bukhārī and Muslim — explicit silence

A search of `bukhari.json` (7,277 hadiths) and `muslim.json` (7,459 hadiths) returns **0 hits** for substantive Yāsīn-content (the *qalb al-Qurʾān* phrase, "Yāsīn"-in-context, or recitation-on-the-dying tradition). The Bukhārī-Muslim *Ṣaḥīḥayn* explicitly do not include the *fadāʾil*-of-Yāsīn material, consistent with the chain-grading position.

There ARE generic recitation-merit hadiths in Bukhārī and Muslim that *could* be applied to Yāsīn (e.g., "the best of you is the one who learns the Qurʾān and teaches it" — Bukhārī #5027), but these are not surah-specific. **The Ṣaḥīḥayn's explicit silence on Yāsīn-fadāʾil is itself a corpus-internal fact** that contextualizes the popular *qalb al-Qurʾān* tradition's chain weakness.

## 4. Aḥmad b. Ḥanbal, *Musnad*

Our corpus's `ahmed.json` is partial (1,374 hadith of the ~30,000+ in the full Musnad). A targeted search for the *qalb al-Qurʾān* phrase + Maʿqil b. Yasār + Yāsīn-on-the-dying patterns returns **only one hit** (Ahmed idInBook 609, global 36772) which is **not** the Yāsīn-on-the-dying hadith but a different *Mahdī*-tradition. Ibn Kathīr (`ibn-kathir-tafsir-quran.openiti.raw.txt` ~ offset 286,639) explicitly cites Aḥmad's transmission of the Yāsīn / *qalb al-Qurʾān* / dying-recitation tradition: "infarada bihī Aḥmad" — the chain is solely through Aḥmad. The reference is to the full *Musnad* (canonically Aḥmad #20302 / Maʿqil b. Yasār chain). **DATA-GAP**: the relevant Aḥmad #20302 is not in our partial JSON; flagged.

## 5. Friday-evening Yāsīn-recitation tradition

Popular literature cites a tradition: "whoever recites Yāsīn on Friday-night will be forgiven". Our corpus search (al-Suyūṭī's *al-Durr*, Tirmidhī, Abū Dāwūd, al-Dārimī) yields:

- al-Suyūṭī al-Durr (raw offset ~6,780,086):
  > وأخرج الدارمي وأبو يعلى والطبراني في الأوسط وابن مردويه والبيهقي في شعب الإيمان عن أبي هريرة عن النبي صلى الله عليه وسلم: من قرأ (يس) في ليلة ابتغاء وجه الله غفر الله له تلك الليلة...

al-Suyūṭī cites the chain through **al-Dārimī, Abū Yaʿlā, al-Ṭabarānī's *al-Awsaṭ*, Ibn Mardawayh, al-Bayhaqī's *Shuʿab al-īmān***, all via Abū Hurayra. The substantive content is **night-recitation forgiveness** rather than specifically Friday-night; the Friday-night tradition is a popular extension.

Our `darimi.json` corpus search yields **0 matches** for substantive Yāsīn-content under the Arabic patterns tested. This is a coverage gap (Darimi *Musnad* in our JSON is partial) — the al-Suyūṭī al-Durr citation is the substantive trace.

## 6. The Tirmidhī "*qalb*" tradition spillover (idInBook 3654 / global 29434)

A **second** Tirmidhī entry uses the *qalb*-the-heart rhetoric in a Yāsīn-related but different context:

> Ibn ʿAbbās said: "We were with the Messenger of Allāh when ʿAlī b. Abī Ṭālib came to him, and he said: 'May my father and mother be ransomed for you! This Qurʾān has suddenly left my heart...' So the Messenger of Allāh said to him: 'O Abū al-Ḥasan! Should I not teach you words that Allāh shall benefit you with...'"

This entry contains the phrase *tafallata hādhā al-Qurʾānu min ṣadrī* (the Qurʾān has fled my heart) — a different "heart"-and-Qurʾān construction. It is NOT the *qalb al-Qurʾān = Yāsīn* hadith; it is the *Qurʾān-leaving-the-heart* hadith. The two are sometimes conflated in popular sources.

## 7. Aggregate citation density across the 9 books

A summary table of substantive Yāsīn-mentions in our corpus:

| Collection | Total hadith | Yāsīn-substantive matches | Key entries |
|:--|:-:|:-:|:--|
| al-Bukhārī | 7,277 | **0** | (no surah-specific Yāsīn fadāʾil) |
| Muslim | 7,459 | 1* | global #9077 = a recitation-style discussion of Q 47 *ghair āsin / yāsin*, NOT Q 36 |
| al-Tirmidhī | 4,053 | 3 | #28750 (*qalb al-Qurʾān*); #26382 (*ghair āsin* reading); #29434 (*Qurʾān-leaving-the-heart*) |
| Abū Dāwūd | 5,276 | 2 | #23626 (recite-over-the-dying); #24899 (the "Yāsīn al-Zayyāt" hadith — a transmitter named Yāsīn, not the surah) |
| al-Nasāʾī | 5,768 | **0** | (no surah-specific Yāsīn fadāʾil) |
| Ibn Mājah | 4,345 | 2 | #31015 (recite-near-dying); #33655 (the "Yāsīn" name in a Mahdī-chain, not the surah) |
| Mālik *Muwaṭṭaʾ* | 1,985 | **0** | (no Yāsīn-fadāʾil) |
| Aḥmad *Musnad* (partial) | 1,374 | 1* | #36772 (Yāsīn al-ʿIjlī, transmitter-name not surah) |
| al-Dārimī | 3,406 | 0 | (no substantive matches in our corpus partial) |

*The "Yāsīn" mentions in Muslim, Aḥmad and partly Ibn Mājah refer to **transmitter-names** ("Yāsīn al-ʿIjlī", "Yāsīn al-Zayyāt") rather than the surah; flagged.

The substantive Yāsīn-fadāʾil hadiths in our corpus are: **3 entries** total — Tirmidhī #28750 (*qalb al-Qurʾān* via Anas, *gharīb*) + Abū Dāwūd #23626 (recite-over-the-dying via Maʿqil) + Ibn Mājah #31015 (recite-near-dying via Maʿqil). Plus the post-canonical chain testimony in al-Suyūṭī's *al-Durr* via al-Bazzār, al-Dārimī, Abū Yaʿlā, al-Ṭabarānī, Ibn Mardawayh, al-Bayhaqī (all via Abū Hurayra).

## 8. Q 36 hadith-fadāʾil score in [[h-new-860-hadith-architectural-alignment|H-NEW-860]]

Per `findings/phase-b-hypotheses/h-new-860.json`, Q 36 receives **the corpus-maximum hadith-fadāʾil rubric score of 10/10**, tied with Q 1, Q 2, Q 67, Q 112. The driver: the *qalb al-Qurʾān* tradition + the recite-on-the-dying tradition + the Friday-night recitation tradition. The 10/10 is computed despite the chain-grading weakness — the rubric counts surahs by classical-tradition-attention, not by modern-criticism survival.

This is the empirical content of the hadith-vs-architecture **divergence**: Q 36 is corpus-MAX on hadith-fadāʾil but **rank 35/114 on UAS**. See `01-empirical-profile.md` §2 and [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13 for the dual-iʿjāz-typology resolution.

## 9. Scrolling cross-corpus signal: Yāsīn-recitation as *adhān*-of-the-dying

The cumulative classical narrative — from al-Tirmidhī (*gharīb* warrant) + Abū Dāwūd + Ibn Mājah (Maʿqil-chain) + al-Suyūṭī al-Durr (post-canonical multi-chain) + al-Biqāʿī + al-Zamakhsharī (tafsir endorsement) + al-Ghazālī's *Iḥyāʾ* (per al-Rāzī's citation in `03-tafsir-survey.md` §2.1) — establishes Sūrat Yāsīn as the **paradigmatic recitation surah for the Muslim deathbed**. This is a **liturgical-sociological** fact established at maximum classical-tradition density.

The empirical correlate: Q 36 is in the 10/10 fadāʾil tier per [[h-new-860-hadith-architectural-alignment|H-NEW-860]]. This is the corpus's **cleanest case of liturgical-iʿjāz / theological-iʿjāz tracking** despite mid-pack architectural-iʿjāz. The dual-iʿjāz typology of [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] is precisely the framework that vindicates this divergence: classical liturgical attention identifies a different "iʿjāz" axis than the project's structural-architectural pipeline.

## 10. Honest limits

- The chain-grading depends partly on classical critics outside our digital corpus (al-Dāraquṭnī, Ibn al-Jawzī, al-Albānī). The al-Tirmidhī internal-grading (*gharīb*, *shaykh majhūl*, *isnāduhu ḍaʿīf*) is verbatim from our corpus and is sufficient on its own to establish the chain weakness; but the modern *ḍaʿīf jiddan* / *mawḍūʿ* extreme-grading by al-Albānī requires external verification.
- Aḥmad's *Musnad* in our JSON is partial (~1,374 hadith of the 30,000+ canon); the canonical Aḥmad #20302 cited by Ibn Kathīr is not directly in our corpus. **DATA-GAP**: the full Maʿqil-chain in Aḥmad #20302 cannot be cross-validated from our corpus alone.
- The conventional reference "Tirmidhī #2887" used in popular literature (and specified in the Wave-D launch task) corresponds in our corpus to global id 28750 / idInBook 2970 (the al-Tirmidhī's own kitāb-fadāʾil-Qurʾān numbering may differ from ahmedbaset-json's idInBook). The numerical citation is rules-tuple-fragile across editions; the **chain-content** (Ḥumayd b. ʿAbd al-Raḥmān ← al-Ḥasan b. Ṣāliḥ ← Hārūn Abū Muḥammad ← Muqātil b. Ḥayyān ← Qatāda ← Anas) is rules-tuple stable and is the operative identification.
- The conventional reference "Abū Dāwūd #3121" similarly corresponds to our idInBook 3122 (global 23626); the off-by-one is edition-dependent.
- The *Friday-night* extension of the Yāsīn-recitation tradition is post-canonical (al-Bayhaqī's *Shuʿab al-īmān*) and lies outside our 9-book corpus. The substantive content is in al-Suyūṭī al-Durr.
- The recitation-frequency fact (Q 36 is the most-recited Meccan post-Q 1 in classical liturgical practice) is a sociological/liturgical claim, NOT a textual claim. The project's [[h-new-860-hadith-architectural-alignment|H-NEW-860]] rubric is a quantitative proxy, not a recitation-count.
