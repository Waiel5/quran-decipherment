---
surah: 55
file_type: hadith-corpus
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — hadith corpus indexed; CRITICAL CORRECTION on the "ʿarūs" attribution
---

# Q 55 al-Raḥmān — Hadith Corpus


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

This file indexes all ḥadīth in the project's available hadith corpus that cite Q 55, the *Night of the Jinn*, the *fa-bi-ayyi ālāʾi* refrain, or the *ʿarūs al-Qurʾān* honorific. Sources extracted from `data/literature/hadith/ahmedbaset-json/db/by_book/`.

## ⚠ CRITICAL CORRECTION on the "ʿarūs al-Qurʾān" hadith

The project's surah-overview file (`00-overview.md` §2) states:

> "ʿArūs al-Qurʾān (عروس القرآن) — 'The Bride of the Quran' — al-Tirmidhī ḥadīth #3291 (also al-Bayhaqī)."

**This attribution is INCORRECT.** Verification:
- al-Tirmidhī #3291 in the project's hadith corpus is the Q 33 *az-zawj-an-asl* / *zayd ibn ḥāritha* hadith (related to Q 33:37, the Zaynab marriage controversy). It does NOT contain the *ʿarūs al-Qurʾān* phrase.
- The "*li-kulli shayʾin ʿarūsun wa-ʿarūsu al-Qurʾāni al-Raḥmān*" tradition is found in **Mishkāt al-Maṣābīḥ #2083** (book 14, chapter 8), narrated by ʿAlī b. Abī Ṭālib, with the explicit attribution: *rawāhu al-Bayhaqī fī Shuʿab al-Īmān*.
- The hadith does NOT appear in any of the 9 canonical books (Bukhārī, Muslim, al-Tirmidhī, Abū Dāwūd, al-Nasāʾī, Ibn Mājah, Mālik, Aḥmad, al-Dārimī) on a strict-text search across the AhmedBaset corpus.

**Corrected attribution**: al-Bayhaqī, *Shuʿab al-Īmān*, on the authority of ʿAlī b. Abī Ṭālib; cited in Mishkāt al-Maṣābīḥ #2083 (`other_books/mishkat_almasabih.json`); cited in al-Biqāʿī, *Naẓm al-durar*, vol. 19 p.139 (Q 55 chapter opening); not found in the 9 canonical books.

**Isnād grading**: al-Bayhaqī's *Shuʿab al-Īmān* is a *fadāʾil* compendium known for relaxed isnād standards. Modern critics (e.g., Ibn al-Ṣalāḥ, *al-Muqaddima*) classify Bayhaqī's *Shuʿab* as containing many *ḍaʿīf* (weak) and *mawḍūʿ* (fabricated) reports. Without a separate isnād-trace in this corpus, we record the hadith as **ḍaʿīf in canonical-grading** but **classically authoritative-by-citation** (al-Biqāʿī, Ibn Kathīr, al-Suyūṭī all cite it).

**This correction must be propagated to `00-overview.md` §2 and §9.** See [[05-classical-claims-audit]] §1.

---

## 1. The "Night of the Jinn" hadith — al-Tirmidhī #3375 (THE primary Q 55 hadith)

**Source**: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json`, `idInBook=3375`, `chapterId=47` (Kitāb tafsīr al-Qurʾān).

**Arabic**:
> حَدَّثَنَا عَبْدُ الرَّحْمَنِ بْنُ وَاقِدٍ أَبُو مُسْلِمٍ السَّعْدِيُّ، حَدَّثَنَا الْوَلِيدُ بْنُ مُسْلِمٍ، عَنْ زُهَيْرِ بْنِ مُحَمَّدٍ، عَنْ مُحَمَّدِ بْنِ الْمُنْكَدِرِ، عَنْ جَابِرٍ، رضى الله عنه قَالَ خَرَجَ رَسُولُ اللَّهِ ﷺ عَلَى أَصْحَابِهِ فَقَرَأَ عَلَيْهِمْ سُورَةَ الرَّحْمَنِ مِنْ أَوَّلِهَا إِلَى آخِرِهَا فَسَكَتُوا فَقَالَ: "لَقَدْ قَرَأْتُهَا عَلَى الْجِنِّ لَيْلَةَ الْجِنِّ فَكَانُوا أَحْسَنَ مَرْدُودًا مِنْكُمْ، كُنْتُ كُلَّمَا أَتَيْتُ عَلَى قَوْلِهِ ﴿فَبِأَيِّ آلاءِ رَبِّكُمَا تُكَذِّبَانِ﴾ قَالُوا: لَا بِشَيْءٍ مِنْ نِعَمِكَ رَبَّنَا نُكَذِّبُ فَلَكَ الْحَمْدُ". قَالَ أَبُو عِيسَى: هَذَا حَدِيثٌ غَرِيبٌ لاَ نَعْرِفُهُ إِلاَّ مِنْ حَدِيثِ الْوَلِيدِ بْنِ مُسْلِمٍ عَنْ زُهَيْرِ بْنِ مُحَمَّدٍ.

**English**:
> Jābir said: "The Messenger of Allah came out to his Companions and recited Sūrat al-Raḥmān from its beginning to its end. They were silent. He said: 'I recited it to the Jinn on the Night of the Jinn — they had a better response than you. Each time I came to His saying *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān*, they said: *lā bi-shayʾin min niʿamika rabbanā nukadhdhibu fa-laka al-ḥamd* — We do not deny any of Your favors, our Lord; to You is praise.'"

**al-Tirmidhī's own grading**: *gharīb* (rare/uncommon) — "we do not know it except from the hadith of al-Walīd b. Muslim from Zuhayr b. Muḥammad."

**Isnād critique** (cited in the same Tirmidhī text):
- al-Imām Aḥmad b. Ḥanbal: "It seems Zuhayr b. Muḥammad who fell to Syria is not the one narrated from in Iraq — they may have switched names due to the *manākīr* (rejected reports) narrated from him."
- al-Bukhārī: "The Syrians narrate *manākīr* from Zuhayr b. Muḥammad; the Iraqis narrate *muqāriba* (acceptable, close-to-mainstream) reports from him."

**Modern grading consensus**:
- al-Albānī (*Ḍaʿīf al-Tirmidhī*) marks it *ḍaʿīf*.
- Sunan Tirmidhī editions in the project corpus retain Tirmidhī's *gharīb* tag without further upgrade.
- The hadith is supported by parallel *night of the jinn* traditions in Muslim, Abū Dāwūd, Ibn Mājah, al-Tirmidhī (other isnāds) — but the Q-55-recitation specific is unique to this Jābir narration.

**This hadith is ALSO recorded in Mishkāt al-Maṣābīḥ #806** (other_books/mishkat_almasabih.json), explicitly attributed to al-Tirmidhī with the *gharīb* grade.

---

## 2. The "Night of the Jinn" event — corroborating hadiths

**Sahih Muslim #909, #912** (no Q 55 mention; establishes the event):
- Muslim #909 (chapter on jinn): ʿAlqama asks Ibn Masʿūd whether any companion was with the Prophet on the *Night of the Jinn*; Ibn Masʿūd: "None of us was with him; we lost him one night and feared he had been kidnapped or murdered; in the morning he returned from the direction of Ḥirāʾ."
- Muslim #912: Ibn Masʿūd: "I was not with the Messenger of Allah on the Night of the Jinn, and I wished I had been."
- These establish the event but do NOT cite the surah.

**al-Tirmidhī #3342** (Kitāb tafsīr): a fuller Ibn Masʿūd narration with similar detail.

**Sunan Abū Dāwūd #84, #85** (Kitāb al-ṭahāra): the *nabīdh-ablution* hadith — "on the Night of the Jinn the Prophet asked Ibn Masʿūd what was in his water-skin; he said *nabīdh*; the Prophet said: 'A good date and pure water.'"

**Sunan Ibn Mājah #118, #119** (Kitāb al-ṭahāra): variants of the *nabīdh-ablution* hadith.

**Mishkāt al-Maṣābīḥ #446**: collates the Abū Dāwūd / Aḥmad / Tirmidhī chains; explicit caveat from al-Tirmidhī himself that "Abū Zayd is *majhūl*" (unknown).

These corroborate the *Night of the Jinn* event historically without citing Q 55.

---

## 3. The "ʿArūs al-Qurʾān" hadith — Mishkāt al-Maṣābīḥ #2083

**Source**: `data/literature/hadith/ahmedbaset-json/db/by_book/other_books/mishkat_almasabih.json`, `idInBook=2083`, `chapterId=8`, `bookId=14`.

**Arabic**:
> وَعَنْ عَلِيٍّ رَضِيَ اللَّهُ عَنْهُ قَالَ: سَمِعْتُ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسلم يَقُول: «لكل شَيْء عروس وعروس الْقُرْآن الرَّحْمَن». رَوَاهُ الْبَيْهَقِيّ فِي شعب الْإِيمَان.

**English** (translation by author): "From ʿAlī, may Allah be pleased with him: I heard the Messenger of Allah ﷺ say: 'Everything has a bride; the bride of the Quran is al-Raḥmān.' Narrated by al-Bayhaqī in *Shuʿab al-Īmān*."

**Isnād trace**: The Mishkāt does not provide the full Bayhaqī isnād here. al-Bayhaqī's *Shuʿab al-Īmān* is the primary collector; the hadith in *Shuʿab* is well-attested but with weak chains (commonly graded *ḍaʿīf*, occasionally *mawḍūʿ* by stricter critics).

**Verdict on isnād**: ḌAʿĪF (weak) by canonical hadith-grading; **CLASSICALLY AUTHORITATIVE** in *fadāʾil al-suwar* literature (al-Biqāʿī, Ibn Kathīr, al-Suyūṭī, Mishkāt all transmit it).

---

## 4. Other Q 55 references in canonical books — null result

A strict-text search across the 9 canonical books for the following patterns returned NO hits beyond those above:
- *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* (the refrain itself)
- *al-Raḥmānu ʿallama al-Qurʾān* (Q 55:1-2)
- *kullu man ʿalayhā fān* (Q 55:26)
- *hal jazāʾ al-iḥsān illā al-iḥsān* (Q 55:60)

The hadith corpus does NOT have the *fadāʾil* density for Q 55 that it has for Q 36 (Yāsīn — al-Tirmidhī "*qalb al-Qurʾān*"), Q 67 (al-Mulk — al-Tirmidhī "*al-munjiya*"), or Q 112 (al-Ikhlāṣ — Bukhārī "*thuluth al-Qurʾān*"). The single primary attestation is the Tirmidhī Jābir hadith #3375 (*gharīb*) plus the Bayhaqī *ʿarūs* tradition (*ḍaʿīf*).

---

## 5. Summary table of hadith citations

| Source | ID-in-book | Topic | Isnād grade |
|:--|:--|:--|:--|
| al-Tirmidhī | #3375 | Recitation of Q 55 to jinn; refrain answered | *gharīb* (al-Tirmidhī) → *ḍaʿīf* (al-Albānī) |
| al-Tirmidhī | #3342 | Night of the Jinn (event, no Q 55) | sound (Ibn Masʿūd narration) |
| Sahih Muslim | #909 | Night of the Jinn (event) | ṣaḥīḥ |
| Sahih Muslim | #912 | Ibn Masʿūd not present | ṣaḥīḥ |
| Sunan Abū Dāwūd | #84, #85 | Nabīdh-ablution on Night of Jinn | mixed; Abū Zayd *majhūl* |
| Sunan Ibn Mājah | #118, #119 | Same nabīdh-ablution | mixed |
| Mishkāt al-Maṣābīḥ | #806 | Tirmidhī Jābir hadith (transmitted) | *gharīb* (Tirmidhī's grade) |
| **Mishkāt al-Maṣābīḥ** | **#2083** | **ʿArūs al-Qurʾān (Bayhaqī)** | **ḍaʿīf** |

## 6. Implication for empirical-architectural reading

**The Q 55 hadith corpus is THIN.** The *Night of the Jinn* tradition (Tirmidhī Jābir #3375) has only one weak chain. The *ʿarūs* honorific has only one weak chain (Bayhaqī).

This thin hadith density is consistent with H-NEW-860's finding that classical *fadāʾil* hadith density tracks **theological-iʿjāz** (Q 112, 114, 67, 36) more strongly than **structural-iʿjāz** (Q 33, 1, 2, 9, 24, 12, **55**, 10, 23, 17). Q 55 is high on UAS rank but mid-low on hadith density — it is a *structurally significant* surah whose classical religious profile is built on its **content** (*ʿarūs* aesthetic appreciation) rather than on prophetic recitation-instruction.

This is a CONFIRMATION of the H-NEW-840 / H-NEW-860 dual-iʿjāz typology: structural and theological iʿjāz are empirically orthogonal axes.

## Honest limits

- The AhmedBaset corpus may not include all isnād-traces; verification against the printed *Shuʿab al-Īmān* (al-Bayhaqī, ed. al-Ḥamīd) would strengthen the isnād grading.
- The hadith collection's "id-in-book" numbering follows sunnah.com conventions; al-Tirmidhī numbering varies between editions — Sunan al-Tirmidhī (Bashshār ʿAwwād) gives the same Jābir Q 55 hadith at slightly different number depending on chapter-counting. The text is the load-bearing identifier, not the integer.
- The PROJECT'S OVERVIEW FILE (`00-overview.md`) cites Tirmidhī #3291 for *ʿarūs al-Qurʾān*; this is wrong and must be corrected. The actual sources are al-Bayhaqī's *Shuʿab al-Īmān* (via Mishkāt #2083) and al-Biqāʿī's *Naẓm al-durar* chapter title.
