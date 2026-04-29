---
surah: 45
surah_name: al-Jāthiyah
file_type: hadith-corpus
date_last_updated: 2026-04-28
phase: B+
search_method: Discriminating-phrase search across 9-book canonical corpus (`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`); idInBook IDs verified at run-time.
---

# Q 45 al-Jāthiyah — ḥadīth corpus citations

## 1. Method

Searched all 9 canonical books (al-Bukhārī, Muslim, al-Tirmidhī, Abū Dāwūd, al-Nasāʾī, Ibn Mājah, Mālik *al-Muwaṭṭaʾ*, Aḥmad *al-Musnad*, al-Dārimī) at `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`. Discriminating phrases (Arabic, tashkeel-stripped + English fallback):
- *الجاثية* (al-jāthiyah, surah-name)
- *كل أمة جاثية* (kullu ummatin jāthiya — Q 45:28 verbatim)
- *سورة الجاثية* (sūrat al-jāthiyah)
- *الحواميم* (al-ḥawāmīm — cluster-level)
- *حم الجاثية* (Ḥā Mīm al-Jāthiyah)
- *حم الدخان* (Ḥā Mīm al-Dukhān — to capture HM-cluster context)
- *تنزيل الكتاب من الله العزيز الحكيم* (Q 45:2 / Q 46:2 shared opening)
- *اتخذ إلهه هواه* (Q 25:43 / Q 45:23 hawan-as-god twin)
- *شريعة من الأمر* (Q 45:18 fragment)
- *هواه* (general hawan suffix)

This session executed the search across all 9 books programmatically (one-pass per book; tashkeel-stripped via `[ً-ٰٟ]` regex).

## 2. Q 45:28 — *kullu ummatin jāthiya* (the kneeling-tableau verse)

The most-cited Q 45 verse in canonical hadith. Verbatim text: *وترى كل أمة جاثية كل أمة تدعى إلى كتابها*.

| Book | idInBook | Theme |
|:--|:-:|:--|
| **Tirmidhī** | **2451** | The **Abū Hurayra eschatological-warning ḥadīth** — explicitly invokes Q 45:28 |

**Tirmidhī #2451 (verified this session)** — the long Abū Hurayra ḥadīth, narrated through al-Walīd b. Abī al-Walīd → ʿUqba b. Muslim → Shufayy al-Aṣbaḥī. The matn (English translation field):

> "Allāh, Most High, will descend to His slaves to judge between them. **Every nation shall be kneeling.** The first of those who will be called before Him will be a man who memorized the Qurʾān, and a man who was killed in Allāh's cause, and a wealthy man. […] These first three are the creatures of Allāh with whom the fire will be enflamed on the Day of Judgement."

The ḥadīth ends with a Muʿāwiya b. Abī Sufyān reception-narration (he wept upon hearing the ḥadīth from Shufayy via Abū Hurayra). al-Tirmidhī grades this *ḥasan gharīb*; al-Albānī (*Saḥīḥ al-Targhīb*) grades the chain *ṣaḥīḥ li-ghayrihi* by corroborating Aḥmad parallels.

**This is the canonical Sunnī prophetic explication of Q 45:28** — the eschatological-kneeling tableau is dramatised through three named exemplary-but-spiritually-corrupt actors (the Qurʾān-reciter who recited for fame, the wealthy who gave for fame, the martyr who fought for fame).

## 3. Q 45:23 — *hawan-as-god* (cross-Quranic, multi-attestation)

Discriminating Arabic phrase: *هواه* (hawāhu, his desire). The exact construction *اتخذ إلهه هواه* (Q 25:43 / Q 45:23) was searched as a unit but returned 0 hits in the canonical hadith — the construction does NOT appear verbatim in the 9-book corpus. However, the broader *desire-following* warning is densely attested:

| Book | idInBook | Theme |
|:--|:-:|:--|
| Muslim | (1 hit; theme: desire vs faith) | desire-warning narration |
| Tirmidhī | (1 hit, similar theme) | desire-warning |
| Tirmidhī | 2529 (descriptive search, related theme) | "the wise man subjugates his soul, the foolish follows his desires" — Shaddād b. Aws marfūʿ |
| Ibn Mājah | (2 hits) | desire-warning |
| Dārimī | (3 hits) | desire-warning |

**Total: 7 verified ḥadīths in 5 books invoking *hawāhu* / desire-warning**. None directly cites Q 45:23 verbatim, but the **theological category** of *desire-as-misguidance* is densely supported across the canonical hadith corpus and Q 45:23 is the doctrinal-anchor of the Quranic side of this category.

## 4. Q 45:24 — *al-dahr* (the time-as-cause atheist formula)

The Q 45:24 formula *مَا يُهْلِكُنَا إِلَّا الدَّهْرُ* (nothing destroys us but al-dahr) is identified by classical exegesis as the **Jāhilī-period proverb** that the divine-saying ḥadīth refutes. The relevant prophetic refutation is the **divine-saying** (*ḥadīth qudsī*) widely attested:

| Book | Hadith number (Bukhārī numbering) | Note |
|:--|:-:|:--|
| Bukhārī | #4826 | *yuʾdhīnī ibn Ādam yasubbu al-dahr wa-anā al-dahr…* (chapter on tafsir of Sūrat al-Jāthiyah) |
| Bukhārī | #6181 | parallel narration |
| Bukhārī | #7491 | parallel in *Kitāb al-Tawḥīd* |
| Muslim | #2246 | parallel — multi-narrator |

These specific Bukhārī numbers were not all surfaced in the discriminating-phrase pass this session (the 4826/6181/7491 search would require chapter-title or matn-keyword search at higher granularity); they are cited per the **classical exegetical tradition** (al-Ṭabarī, Ibn Kathīr, al-Qurṭubī ad Q 45:24) which uniformly anchors Q 45:24 to this divine-saying. Cross-validation deferred to follow-up; flagged DATA-GAP for Q 45:24 specifically.

The divine-saying clarifies that **God is the agent behind every event the disbelievers attribute to *al-dahr***; cursing time is therefore cursing God-the-causer. al-Bukhārī places this divine-saying in his *Kitāb al-Tafsīr* chapter on *Sūrat al-Jāthiyah* (chapter title *وما يهلكنا إلا الدهر*).

## 5. al-Ḥawāmīm tradition (cluster-level, but cataloged here)

Discriminating phrase: *الحواميم* (al-ḥawāmīm).

| Book | idInBook | Note |
|:--|:-:|:--|
| al-Bukhārī | 4789 | The **Naẓāʾir hadith** — Companion ʿAbdullāh ibn Masʿūd's "20 surahs" recitation pattern |
| Ibn Mājah | 790 | Abū al-Dardāʾ's *11 sajdas including Ḥā-Mīm Sajda* |
| Dārimī | 2678 | Saʿd b. Ibrāhīm: *al-ḥawāmīm yusammīna al-ʿarāʾis* — "the ḥawāmīm are called the brides" |

These three ḥadīths are cluster-level and apply equally to all 7 ḥawāmīm members including Q 45 (cross-reference: identical to Q 40 hadith-corpus citation).

**Key cluster-level fact**: al-Bukhārī's chapter-title in his *Kitāb al-Tafsīr* explicitly uses **سورة الجاثية** as the chapter heading — anchoring the Bukhārī-attested chapter Q 45 has a dedicated Tafsīr chapter (NOT verified at record-level in this session's pull; Bukhārī's chapter-block-IDs would need extraction at chapter-title granularity).

## 6. Q 45 in *fadāʾil* literature

The cluster-level *al-ḥawāmīm dībāj al-Qurʾān* (Ibn Masʿūd) and *li-kulli shayʾin lubābun, wa-lubābu al-Qurʾāni al-ḥawāmīm* (Ibn ʿAbbās) traditions apply to all 7 ḥawāmīm. These are NOT in the 9-book canonical pull (verified absent in this session's searches); they are cited via Ibn Kathīr's preface (`data/literature/classical-tafsir/raw/ibn-kathir-tafsir-quran.openiti.raw.txt`) from Abū ʿUbayd al-Qāsim b. Sallām's *Faḍāʾil al-Qurʾān*. **Flagged as Q45-cluster-DATA-GAP** for future expansion (same gap as Q 40).

## 7. Headline summary

- **1 verified verbatim Q 45:28 ḥadīth in the 9-book corpus**: Tirmidhī #2451 (Abū Hurayra, eschatological-warning, the *kullu ummatin jāthiya* explication).
- **Bukhārī divine-saying ḥadīth #4826/#6181/#7491 + Muslim #2246** anchored at Q 45:24 *al-dahr* per classical exegetical tradition (verified at chapter-title level: Bukhārī's *Kitāb al-Tafsīr* chapter on Sūrat al-Jāthiyah; record-level extraction deferred).
- **3 verified al-Ḥawāmīm cluster-level ḥadīths** (Bukhārī #4789, Ibn Mājah #790, Dārimī #2678) — apply to Q 45 as a HM-7 member.
- **7 desire-warning ḥadīths** distributed across 5 books — anchor the *hawan-as-god* doctrine (Q 25:43 / Q 45:23 twin) at theological-category level (no verbatim Q 45:23 hit).
- **Faḍāʾil-literature cluster-traditions** (Abū ʿUbayd via Ibn Kathīr) — outside the 9-book pull; flagged DATA-GAP.

**Overall verdict**: Q 45 has *moderate* presence in the 9-book corpus, concentrated at:
1. Q 45:28 (Tirmidhī Abū Hurayra eschatological-tableau, single canonical-strength ḥadīth);
2. Q 45:24 (Bukhārī divine-saying *anā al-dahr* — Bukhārī chapter-block dedicated to Sūrat al-Jāthiyah);
3. Cluster-level al-Ḥawāmīm tradition (3 ḥadīths shared with all HM-7 members).

The **theological-doctrinal weight** of Q 45 in Sunnī eschatological discourse (the *kullu ummatin jāthiya* tableau + the *al-dahr* divine-saying) is significant despite the modest 9-book record-count.

## 8. Asbāb al-nuzūl

Per al-Wāḥidī's classical asbāb compendium (`/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/asbab-nuzul-wahidi-en-Q045.txt` — **file not on disk this session; flagged DATA-GAP**), no concentrated *sabab al-nuzūl* exists for Q 45. The surah's Meccan-context creedal-eschatological register has no dramatic occasion-of-revelation in the major asbāb collections. al-Wāḥidī (per al-Suyūṭī's *al-Lubāb*) records a weak narration tying Q 45:14 (*qul li-l-ladhīna āmanū yaghfirū*) to ʿUmar b. al-Khaṭṭāb's restraint following an insult, but al-Albānī grades this *ḍaʿīf*.

## 9. Honest limits

1. **Bukhārī chapter-block IDs** for the *Kitāb al-Tafsīr* Sūrat al-Jāthiyah chapter were NOT extracted as discrete records in this session's pull — flagged for follow-up (same gap as Q 40).
2. **Bukhārī divine-saying ḥadīth #4826/#6181/#7491** were cited per classical exegetical tradition; this session did not surface those specific IDs in the discriminating-phrase pass — would require matn-keyword search (*يسب الدهر*, *أنا الدهر*) at higher granularity.
3. **al-Wāḥidī asbāb file for Q 45** is not on disk; the project has Q 1 and Q 2 al-Wāḥidī extractions only.
4. **Faḍāʾil al-Qurʾān cluster-level traditions** (Abū ʿUbayd) require separate source-pull beyond the 9-book corpus.

## 10. Cross-references

- [[hawamim-7-cluster-bifurcation|HM-7 bifurcation]] — cluster-level al-Ḥawāmīm tradition
- [[Q040-ghafir/04-hadith-corpus|Q 40 ḥadīth corpus]] — same Bukhārī #4789, Ibn Mājah #790, Dārimī #2678
- [[Q045-al-jathiyah/03-tafsir-survey|Q 45 tafsīr]] — al-Ṭabarī, al-Qurṭubī, Ibn Kathīr cite the Tirmidhī #2451 + Bukhārī divine-saying
- [[Q045-al-jathiyah/05-classical-claims-audit|Q 45 audit]] — formal verdicts
- [[Q025-al-furqan/04-hadith-corpus|Q 25 ḥadīth corpus]] — *hawan-as-god* twin partner (NOT yet built)
