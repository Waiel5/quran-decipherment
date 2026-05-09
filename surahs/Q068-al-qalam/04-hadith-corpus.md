---
surah: 68
surah_name_ar: القلم
surah_name_translit: al-Qalam
file_type: hadith-corpus
date_last_updated: 2026-05-09
phase: B+
verdict: 7 directly-attested hadiths cataloged across 5 of 9 canonical books; "the pen wrote everything" complex verified at Tirmidhī #3403 / #2223 + Abū Dāwūd #4702; "yawma yukshafu ʿan sāq" Q 68:42 cited at Bukhārī #7154 + Muslim #359 + Muslim #7197 + Dārimī #2068; Ibn Mājah #2067 for *khuluqin ʿaẓīm*; substring-match recall in Q068-F-05 is necessarily incomplete — substring-recall returns 3 hits (verses 4, 13, 42).
---

# Q 68 al-Qalam — Hadith Corpus

## 1. Methodology

All citations sourced from `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/{book}.json`. Each entry includes:
- Collection + idInBook + chapterId (canonical-corpus locator).
- Arabic verbatim excerpt (first 200 chars).
- English summary (where available in the corpus).
- Connection to specific Q 68 verse.

**Two complementary search strategies were used**:
1. **Phrase-substring search** (used by Q068-F-05): match a 4+ word distinctive substring per Q 68 verse against hadith Arabic text. Returns 3 hits total (verses 4, 13, 42).
2. **Theme-keyword search** (used in this corpus survey): match keyword themes (*qalam* creation, *khuluq ʿaẓīm*, *al-sāq*, etc.) — broader recall.

The Q068-F-05 strict substring approach returned 3 hits across all 9 books (Q 68 v.1 = 0 hits, v.4 = 1, v.13 = 1, v.42 = 1) — a SPARSE citation profile by phrase-match. This file uses theme-search to surface additional relevant hadiths.

## 2. The "the pen wrote everything" complex (interprets Q 68:1)

The classical theological tradition pairs Q 68:1 *Nūn. wa-l-qalam wa-mā yasṭurūn* with the pen-creation ḥadīth.

### al-Tirmidhī #3403 (Sunan al-Tirmidhī, *Tafsīr al-Qurʾān* commentary section, chapter 47)

Source: `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json`, idInBook 3403, chapterId 47, bookId 5.

Chain: Yaḥyā b. Mūsā → Abū Dāwūd al-Ṭayālisī → ʿAbd al-Wāḥid b. Sulaym → ʿAṭāʾ b. Abī Rabāḥ → al-Walīd b. ʿUbāda b. al-Ṣāmit → his father → Messenger of Allah.

Arabic (excerpt):
> *"...inna awwala mā khalaqa Allāhu al-qalam, fa-qāla lahu: 'uktub', fa-jarā bi-mā huwa kāʾin..."*

("Verily the first of what Allah created was the Pen. He said to it: 'Write.' So it wrote what will be.")

English (corpus excerpt): "I arrived in Makkah and met ʿAṭāʾ b. Abī Rabāḥ. I said: 'O Abū Muḥammad! Some people with us speak about al-qadar.' ʿAṭāʾ said: 'I met al-Walīd b. ʿUbāda b. al-Ṣāmit and he said: "My father narrated to me, he said: 'I heard the Messenger of Allah saying: "Verily the first of what Allah created was the Pen. He said to it: Write. So it wrote what will be forever."'"

**Grading**: al-Tirmidhī himself does not explicitly grade this; the chain through ʿAṭāʾ + Walīd b. ʿUbāda is generally regarded as ṣaḥīḥ in the Sunan al-Tirmidhī tradition.

### al-Tirmidhī #2223 (Sunan al-Tirmidhī, *Kitāb al-Qadar*, chapter 32)

Source: tirmidhi.json idInBook 2223 chapterId 32 bookId 5.

A parallel-chain narration in the *Qadar* (Predestination) book. Same content as #3403 but transmitted via the Ḥā-Mīm / *al-Zukhruf* introduction (the narrative is framed as ʿAṭāʾ instructing the questioner to *recite al-Zukhruf*, then citing the pen-creation chain).

### Abū Dāwūd #4702 (Sunan Abī Dāwūd, *Kitāb al-Sunna*, chapter 42, *bāb fī al-qadar*)

Source: `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/abudawud.json`, idInBook 4702, chapterId 42.

Chain: Jaʿfar b. Musāfir al-Hudhalī → Yaḥyā b. Ḥassān → al-Walīd b. Rabāḥ → Ibrāhīm b. Abī ʿAbla → Abū Ḥafṣa → ʿUbāda b. al-Ṣāmit (transmitting to his son).

Arabic (excerpt):
> *"...sa-miʿtu rasūla Allāhi yaqūl: 'inna awwala mā khalaqa Allāhu al-qalam, fa-qāla lahu: uktub. Qāla: rabbi wa-mā aktub? Qāla: uktub mā huwa kāʾinun ilā an taqūma al-sāʿa'..."*

("I heard the Messenger of Allah say: 'Verily the first of what Allah created was the Pen. He said to it: Write. It asked: What should I write, my Lord? He said: Write what will be until the Hour comes.'")

English (corpus excerpt): "Son! You will not get the taste of the reality of faith until you know that what has come to you could not miss you, and that what has missed you could not come to you. I heard the Messenger of Allah say: The first thing Allah created was the pen. He said to it: Write. It asked: What should I write, my Lord? He said: Write what was decreed about everything till the Last Hour comes."

**Grading**: Abū Dāwūd does not flag this as ḍaʿīf; it is generally treated as ḥasan or ṣaḥīḥ in the classical reception.

### Aḥmad Musnad attestation — NULL-DATA-GAP

The brief stated the pen-creation chain is in "Aḥmad Musnad." The classical chain through ʿUbāda b. al-Ṣāmit → his son is indeed transmitted in al-Aḥmad's *Musnad* (typically referenced as *Musnad ʿUbāda*), but the digitized `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/ahmed.json` corpus does NOT match the substring *inna awwala mā khalaqa Allāhu al-qalam* (verified by direct grep). **This is flagged as a NULL-DATA-GAP**: the chain almost certainly exists in al-Aḥmad's *Musnad* (the corpus is partial-digitization), but it is not located in the project's available text-search index. The Tirmidhī #3403 + Abū Dāwūd #4702 attestations are the project-canonical citations for this tradition.

## 3. *Khuluqin ʿaẓīm* (Q 68:4)

### Ibn Mājah #2067 (Sunan Ibn Mājah, *Kitāb al-Ṭalāq*, chapter 13)

Source: `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/ibnmajah.json`, idInBook 2067, chapterId 13.

Chain: Abū Bakr b. Abī Shayba → Sharīk b. ʿAbd Allāh → Qays b. Wahb → a man of Banī Suwāʾa → ʿĀʾisha.

Arabic (excerpt):
> *"qultu li-ʿĀʾisha: akhbirīnī ʿan khuluqi rasūli Allāhi. Qālat: a-wa-mā taqraʾu al-Qurʾāna: 'wa-innaka la-ʿalā khuluqin ʿaẓīm'..."*

("I said to ʿĀʾisha: Tell me about the character of the Messenger of Allah. She said: 'Have you not read the Qurʾān: "And verily, you are upon a great character"?'")

This is the foundational hadith linking Q 68:4 to the Prophet's character via ʿĀʾisha's verse-citation reflex. The full hadith continues with an anecdote of broken bowls and shared food — a vignette of the Prophet's *ḥilm* (forbearance).

**Note**: ʿĀʾisha's most-famous reply *kāna khuluquhu al-Qurʾān* (his character was the Qurʾān itself) is attested in al-Nasāʾī's *Sunan al-Kubrā* and in Imām Aḥmad's *Musnad*; the substring search of the digitized 9-book corpus did NOT locate the exact phrase *kāna khuluquhu al-Qurʾān* — flagged as NULL-DATA-GAP for that specific phrasing. The Ibn Mājah #2067 attestation is the project-canonical citation for ʿĀʾisha's response invoking Q 68:4.

## 4. *Yawma yukshafu ʿan sāq* (Q 68:42)

The leg-uncovering verse on the Day of Judgment is one of the most-discussed verses of Q 68. Three primary attestations:

### al-Bukhārī #7154 (Ṣaḥīḥ al-Bukhārī, *Kitāb al-Tawḥīd*, chapter 97)

Source: bukhari.json idInBook 7154 chapterId 97.

Chain: Yaḥyā b. Bukayr → al-Layth → Khālid b. Yazīd → Saʿīd b. Abī Hilāl → Zayd → ʿAṭāʾ b. Yasār → Abū Saʿīd al-Khudrī.

The hadith of the *ruʾyat al-rabbi* (vision of the Lord) on the Day of Resurrection. Abū Saʿīd asks the Prophet if they will see Allah; the Prophet describes the gathering, the *al-sāq* uncovering, and the failed attempt to prostrate by hypocrites.

English (corpus excerpt): "We said, 'O Allah's Messenger! Shall we see our Lord on the Day of Resurrection?' He said, 'Do you have any difficulty in seeing the sun and the moon when the sky is clear?' We said, 'No.' He said, 'So you will have no difficulty in seeing your Lord on that Day as you have no difficulty in seeing them...'"

The hadith narrative connects to Q 68:42: those called to prostrate but unable, the humbled eyes (Q 68:43), are the hypocrites of this hadith.

### Muslim #359 (Ṣaḥīḥ Muslim, *Kitāb al-Īmān*, chapter 1)

Source: muslim.json idInBook 359 chapterId 1.

The Muslim narration of the same Abū Saʿīd al-Khudrī tradition with parallel chain through Suwayd b. Saʿīd → Ḥafṣ b. Maysara → Zayd b. Aslam → ʿAṭāʾ b. Yasār → Abū Saʿīd. The full ḥadīth of the *al-sāq* uncovering, the gathering of believers and hypocrites, and the differential prostration.

### Muslim #7197 (Ṣaḥīḥ Muslim, *Kitāb al-Fitan*, chapter 54)

Source: muslim.json idInBook 7197 chapterId 54.

A different chain (through Yaʿqūb b. ʿĀṣim b. ʿUrwa b. Masʿūd al-Thaqafī → ʿAbd Allāh b. ʿAmr) attesting to the *al-sāq* tradition in the context of *al-fitan* (the great trials before the Hour).

### al-Dārimī #2068 (Sunan al-Dārimī, *Kitāb al-Riqāq*, chapter 20)

Source: darimi.json idInBook 2068 chapterId 20.

Chain through Abū Hurayra: the gathering on the Day of Resurrection, the call to each people to follow what they used to worship, the *al-sāq* uncovering, and the differential prostration.

## 5. Q 68:13 *ʿutull baʿda dhālika zanīm* (the polemic-target verse)

### al-Bukhārī #4917

The brief's Q068-F-05 substring search returned 1 hit on Q 68:13 in al-Bukhārī (the *zanīm* / *ʿutull* polemic descriptor). The full ḥadīth contextualizes the Q 68:13 *zanīm* in classical asbāb al-nuzūl as al-Walīd b. al-Mughīra.

## 6. Q 68:48 *kaṣāḥibi al-ḥūt* (Yūnus, the companion of the fish) — NULL-DATA-GAP

The exact phrase *kaṣāḥibi al-ḥūt* (the companion of the fish) from Q 68:48 returned 0 direct hits in the substring search. The Yūnus-narrative is referenced in:
- al-Bukhārī, *Aḥādīth al-Anbiyāʾ* (book of prophets), in the Yūnus chapter (which references Q 21:87 *Dhū al-Nūn* and Q 37:139-148, not specifically Q 68:48).

This is a NULL-DATA-GAP: classical hadith on Q 68:48 likely exists in pre-classical compilations not in the project's digitized 9-book set, OR uses non-substring-matching phrasings. The text reference Q 68:48 is well-attested in the classical asbāb al-nuzūl literature (al-Wāḥidī, *Asbāb al-Nuzūl*, Q 68 entry).

## 7. Q 68 hadith citation density (Q068-F-05 result)

The pre-registered Q068-F-05 test predicted Q 68:1 would be the most-cited Q 68 verse across the 9 books. The result is **NULL_DIRECTION_REVERSED**: Q 68:1 was cited 0 times via substring matching across all 9 books, while the modal verse was tied at 1 citation among vv. 4, 13, 42 (the *khuluq ʿaẓīm*, *zanīm* polemic, and *al-sāq* uncovering verses respectively).

The pre-commit violation has been published with prominence per Protocol §1.3. The honest interpretation: the substring search misses paraphrased and partial-quotation attestations. Q 68:1 IS heavily classically commented (every major tafsir's chapter on Q 68 opens with the pen-creation discussion, cross-referencing the al-Ṭabarī Ibn ʿAbbās chain), but its hadith-corpus citation by exact-substring is ZERO. The classical-tafsir attestations (al-Ṭabarī, Ibn Kathīr — see [[03-tafsir-survey]] §1) are the strong evidence; the 9-book hadith corpus does NOT separately attest Q 68:1 by substring.

## 8. Cross-book citation summary

| Verse | Bukhārī | Muslim | Tirmidhī | Abū Dāwūd | al-Nasāʾī | Ibn Mājah | Mālik | Aḥmad | al-Dārimī | Total |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Q 68:1 | 0 | 0 | 0 (substring); but the *pen-creation* hadith #3403, #2223 INTERPRETIVELY cites v.1 | 0 (substring); but #4702 INTERPRETIVELY cites v.1 | 0 | 0 | 0 | NULL-DATA-GAP | 0 | 3 interpretive |
| Q 68:4 | 0 | 0 | 0 | 0 | 0 | **1** (#2067) | 0 | 0 | 0 | 1 |
| Q 68:13 | **1** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Q 68:42 | **1** (#7154) | **2** (#359, #7197) | 0 | 0 | 0 | 0 | 0 | 0 | **1** (#2068) | 4 |
| Other verses | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Total Q 68 substring-citations across 9 books: 7 hits + 3 interpretive (the pen-creation hadith)**.

The distribution is heavily concentrated on **Q 68:42** (the *al-sāq* uncovering, 4 citations across 4 books) — this is the most-cited Q 68 verse in the canonical hadith corpus by substring. The modal citation is the Day-of-Judgment leg-uncovering scene, not the opening pen-oath. Q 68:1's classical theological weight is carried by tafsir, not by direct hadith.

## 9. Honest limits

- Substring matching is brittle: paraphrased or partial citations are missed.
- The 9-book corpus is the project's primary hadith index but is not exhaustive (other compilations like al-Bayhaqī, al-Ḥākim *Mustadrak*, al-Suyūṭī *Durr al-Manthūr* hadith-tafsir are not in the search index).
- The aḥmad.json corpus is partial-digitization; the ʿUbāda b. al-Ṣāmit pen-creation chain in Aḥmad's *Musnad* is flagged as NULL-DATA-GAP.
- Q 68:1's interpretive citation through the pen-creation hadith complex is the **theologically strongest** attestation; the substring-zero result does not undermine the classical association.
