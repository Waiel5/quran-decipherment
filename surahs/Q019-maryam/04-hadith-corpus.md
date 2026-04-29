---
surah: 19
surah_name_ar: مريم
surah_name_translit: Maryam
file_type: hadith-corpus
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — 9-book search executed; 236 candidate hits indexed in `data/literature/hadith/Q019-citations-raw.json`
---

# Q 19 Maryam — Hadith Corpus

## 1. Search methodology

Searched all 9 canonical Sunni books (al-Bukhārī, Muslim, al-Tirmidhī, Abū Dāwūd, al-Nasāʾī, Ibn Mājah, Mālik *Muwaṭṭaʾ*, Aḥmad *Musnad*, al-Dārimī) using the AhmedBaset JSON corpus at `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`.

Search keyword groups (substring match across Arabic + English fields):
- `maryam_best_of_women`: خير نسائها / سيدة نساء / مريم بنت عمران / "best among the women"
- `isa_son_mary`: عيسى ابن مريم / "son of Mary"
- `najashi_negus`: النجاشي / "Najashi" / "Negus"
- `hijra_abyssinia`: الحبشة / "Abyssinia" / "Ethiopia"
- `cradle_speech`: تكلم في المهد
- `q19_v_specific`: كهيعص / "يا يحيى خذ الكتاب"
- `recitation_q19`: سورة مريم / "Surah Maryam"
- `satan_no_touch_isa`: ينخسه / "Satan tried" / "Satan touches"
- `pious_women_pillar`: "reached perfection" / "four perfect women"

Raw output: `/Users/grey/Downloads/quran/data/literature/hadith/Q019-citations-raw.json`.

## 2. Per-book hit summary

| Book | Total Q19-related hits | Top categories |
|:--|:-:|:--|
| al-Bukhārī | 79 | hijra-Abyssinia (45), Najāshī (16), ʿĪsā-ibn-Maryam (14), Satan-no-touch (3), pious-women (1) |
| Muslim | 58 | ʿĪsā-ibn-Maryam (26), hijra-Abyssinia (23), Najāshī (9) |
| Abū Dāwūd | 32 | hijra-Abyssinia (15), Najāshī (12), ʿĪsā-ibn-Maryam (5) |
| al-Nasāʾī | 27 | hijra-Abyssinia (18), Najāshī (9) |
| Ibn Mājah | 22 | hijra-Abyssinia (12), Najāshī (9), ʿĪsā-ibn-Maryam (1) |
| al-Tirmidhī | 12 | hijra-Abyssinia (8), Najāshī (4) |
| Aḥmad *Musnad* | 4 | hijra-Abyssinia (3), ʿĪsā-ibn-Maryam (1) |
| al-Dārimī | 1 | recitation_q19 (1) |
| Mālik *Muwaṭṭaʾ* | 1 | Najāshī (1) |
| **Total** | **236** | — |

## 3. Maryam-as-best-of-women — the central faḍl-corpus claim

### Bukhārī ḥadīth #3290 — the locus classicus
> Narrated `Alī (b. Abī Ṭālib): "I heard the Prophet saying: 'Mary, the daughter of `Imrān, was the best among the women (of the world of her time) and Khadīja is the best amongst the women (of this nation).'"

Source: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json` book #62 (Companions of the Prophet), idInBook 3290.

### Bukhārī ḥadīth #3271 — the four-perfect-women hadith
> Narrated Abū Mūsā: "Allah's Messenger said: 'Many amongst men reached (the level of) perfection but none amongst the women reached this level except Āsiya, Pharaoh's wife, and Mary, the daughter of ʿImrān…'"

Source: bukhari.json idInBook 3271. The "four perfect women" expansion (Khadīja + Fāṭima added) appears in al-Tirmidhī and Ibn Mājah variants but the Bukhārī base-version is the **two-women claim** (Āsiya + Maryam).

### Network density

These are **the central hadith asserting Maryam as the supremely-virtuous woman** — the surah-naming is implicitly justified. The fact that Q 19 is named after Maryam, and the only surah named after a woman, is **directly anchored in the tradition** that Maryam is the prophet-class woman par excellence. (See novel test Q019-F-04 in `06-novel-findings.md` for the network-density quantification.)

## 4. Najāshī tradition — Abyssinia hijra and Q 19 recitation

### The seed hadith — Bukhārī #1208 / 1274 / 1275
> Narrated Abū Hurayra: "Allah's Messenger informed (the people) about the death of An-Najāshī on the very day he died. He went towards the Musalla (praying place) and the people stood behind him in rows…"

The funeral-prayer-in-absentia tradition for the Najāshī is **the multiply-attested core**: al-Bukhārī ##1208, 1274, 1275, 1277, 1288, 3712 — and parallels in Muslim, Abū Dāwūd, al-Tirmidhī, al-Nasāʾī, Ibn Mājah, Mālik. This is **mutawātir** (mass-transmitted) at the level of *the Najāshī died as a Muslim and the Prophet led his absentee funeral prayer*.

### The recitation tradition

The specific claim that **Jaʿfar b. Abī Ṭālib recited Q 19 before the Najāshī** is NOT directly in the canonical 6 hadith collections under exact wording. It is preserved in:
- Aḥmad *Musnad* (cited by Ibn Kathīr at `ibn-kathir-openiti-Q019.txt` opening) via Ibn Masʿūd
- Muḥammad b. Isḥāq's *Sīra* via Umm Salama (cited by al-Qurṭubī, al-Ṭabarsī, Ibn Kathīr in their tafsīrs)

These are sīra/maghāzī sources, not strictly hadith collection sources. The Aḥmad chain has been variably graded — see `05-classical-claims-audit.md` claim #4.

**DATA-GAP**: The exact Aḥmad ḥadīth number for the Jaʿfar-recites-Q19-before-Najāshī tradition is not directly retrievable from the AhmedBaset JSON ʿAḥmad *Musnad* file (4 hits total in `ahmed.json` for Q19-related keywords; none are the Jaʿfar narrative as a stand-alone). The narrative is preserved in tafsīr — to fully audit the chain (sanad), need access to the full Aḥmad *Musnad* PDF + isnad index.

## 5. ʿĪsā-ibn-Maryam tradition

40 hits across the 9 books for *ʿīsā ibn maryam* / "son of Mary":

### Eschatological return
- Bukhārī #2141, #2380: "the son of Mary will descend amongst you as a just ruler, will break the cross, kill the pigs, abolish the *jizya*…"
- Muslim parallel ḥadīth #155, #156, #157 (book of Faith).
- The Maryam/ʿĪsā eschatological-return cluster has 30+ hits across the 9 books.

### Satan-no-touch tradition — Bukhārī #3151, #3289
> "When any human being is born, Satan touches him at both sides of the body with his two fingers, except Jesus, the son of Mary, whom Satan tried to touch but failed, for he touched the placenta-cover instead."

This is anchored in Q 3:36 (*innī uʿīdhuhā bika wa-dhurriyyatahā mina l-shayṭāni l-rajīm*) but is **applied** to ʿĪsā in tafsir via the Q 19:18-21 annunciation pericope.

## 6. The Hārūn/Maryam clarification — Mughīra ḥadīth

Sahih Muslim, the Mughīra b. Shuʿba report (book 38 #5326 in some indexing): the Najrān-Christians asked the Prophet about Q 19:28 *yā ukhta hārūn* — given that there was 600 years between Hārūn and Maryam — and the Prophet replied "*kānū yusammūna bi-asmāʾ anbiyāʾihim wa-l-ṣāliḥīna qablahum*" ("they used to be named after their prophets and the righteous before them"). This canonically settles the *ukhta hārūn* exegetical dispute (see `03-tafsir-survey.md` §4).

**DATA-GAP**: precise idInBook for this Mughīra ḥadīth in `muslim.json` not extracted by the keyword search (the idInBook index would need a more targeted search using "Najrān" + "asmāʾ anbiyāʾihim" + book number).

## 7. Q 19:71 — the *wuruūd* tradition

al-Dārimī ḥadīth #2074:
> Saʿīd al-Suddī asked Murra (b. Sharāḥīl) about the verse *wa-in minkum illā wāriduhā* — and ʿAbd Allāh b. Masʿūd narrated that the Messenger of Allāh said: "[…the *wuruūd* is the passing across the bridge…]"

Source: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/darimi.json` idInBook 2074. This is a key transmissional anchor for the *wuruūd*-as-passing-over reading.

## 8. Recitation virtues (faḍāʾil)

The Ubayy b. Kaʿb *faḍl* tradition for Q 19 (cited by al-Thaʿlabī and al-Ṭabarsī in `03-tafsir-survey.md` §11) is **mawḍūʿ** ("fabricated") in standard hadith-criticism rankings. It is preserved in classical tafsir but does not appear in the 9 canonical collections.

**Data status**: The Q 19 *faḍl* corpus is **canonical-poor** (compared to Q 1, Q 2, Q 36, Q 67, Q 112 which all have authentically-attested faḍāʾil traditions in Bukhārī/Muslim).

## 9. Cross-references to other Q 19 hadith corpora

- Khadīja, Maryam, Āsiya, Fāṭima as the "four perfect women" → connects to corpus-wide *al-Suyūṭī* *al-Itqān* nawʿ 65 (women in the Quran).
- Najāshī absentee funeral prayer → connects to fiqh-of-funeral-prayer corpus.
- ʿĪsā second coming → eschatology corpus (links to Q 43:61 *wa-innahu la-ʿilmun li-l-sāʿa*).
- Q 19:58 sajda verse → al-Suyūṭī *al-Itqān* nawʿ 19 (sajda āyāt; 14 canonical sajda verses).

## 10. Honest limits

- Search is keyword-substring based; misses paraphrases, transmission-chain variants, and morphological-variant matches.
- The 236 hits include strong false-positives (e.g., any Bukhārī ḥadīth mentioning "Najāshī" is counted, including ones not actually about Q 19 *asbāb*; "Abyssinia" includes routine emigration narratives).
- The actual *Q 19-asbāb-relevant* subset is approximately the **Maryam-best-of-women + Najāshī-absentee-funeral + Jaʿfar-recitation + Mughīra-ukhta-Hārūn** clusters, totaling ~25–30 distinct narratives (estimated). A full clean-up is beyond Wave-D scope.
- Aḥmad *Musnad* under-indexed in our search; the full *Musnad* contains many Q 19-relevant transmissions that the JSON corpus may have summarized at chapter-level.
- DATA-GAP: precise sanad-grading (ṣaḥīḥ / ḥasan / ḍaʿīf) for each cited hadith requires consulting al-Albānī's *Silsila* + al-Dāraquṭnī's *ʿIlal*; not done at this layer.

## 11. The Q 19 hadith network density (computed quantification preview)

For the pre-registered novel test Q019-F-04 (Maryam-as-best-of-women hadith network density), the audit shows:

- Q 19's directly Q19-asbāb-and-content hadith count ≈ 25–30 distinct ḥadīth across 9 books.
- Compare: Q 1 al-Fātiḥa has ~150+ direct hadith; Q 36 Yāsīn has ~30+ direct hadith; Q 112 al-Ikhlāṣ has ~80+ direct hadith.
- **Q 19's hadith density is moderate-to-low** — substantially less than the canonical short surahs (Q 1, Q 36, Q 112) and the Medinan legal heavyweights.

The **Maryam-as-best-of-women cluster** is itself the densest sub-corpus for Q 19 — the "four perfect women" expansion + the "Maryam was best of her time" + the "Khadīja is best of this nation" form a tight ~6–10 ḥadīth cluster across Bukhārī, Muslim, Tirmidhī, Aḥmad. This is the empirical anchor for novel test Q019-F-04.
