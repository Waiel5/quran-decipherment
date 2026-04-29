---
surah: 10
surah_name: Yūnus
file_type: hadith-corpus
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — 9-book corpus scanned; key Q 10-relevant chains catalogued
---

# Q 10 Yūnus — Hadith corpus

Pre-flight: hadith scanned via `surahs/Q010-yunus/scripts/scan_hadith_q010.py` against the 9-book canonical corpus at `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`. Output JSON at `surahs/Q010-yunus/csv/Q010-hadith-scan.json`. Total raw hits: 139 (across 9 books).

## 1. Match-pattern catalogue

The scanner used 9 patterns:

| Pattern | Total hits |
|:--|--:|
| YUNUS_ENGLISH (Yūnus appearing as transmitter or person) | 128 |
| JONAH_ENGLISH (English-translation Jonah-mentions) | 9 |
| YUNUS_BIN_MATTA (canonical phrasing of the prophet Yūnus) | 1 |
| SURAT_YUNUS (direct mention of "sūrat Yūnus") | 1 |
| QAWM_YUNUS, AWLIYA_VERSE, Q10_98, Q10_101, Q10_OPENING | 0 each (in Arabic-strict pattern) |

Most YUNUS_ENGLISH hits are ISNAD-CHAIN occurrences of transmitters named Yūnus (e.g., Yūnus b. Yazīd al-Aylī, Yūnus b. ʿUbayd, Yūnus b. Muḥammad al-Mu'addib). These are NOT relevant to Q 10. The empirically-relevant subset is the JONAH_ENGLISH cluster + the lone SURAT_YUNUS hit + the YUNUS_BIN_MATTA hit.

## 2. Canonical "I am not better than Yūnus b. Mattā" hadith — Bukhārī cluster

Bukhari hadith #3274, 4397, 4398, 4424, 4425, 4598, 4599 (idInBook):

> *"None has the right to say that I am better than Yūnus b. Mattā"* — Narrated ʿAbd Allāh b. Masʿūd, Abū Hurayra, and Ibn ʿAbbās in different chains. (`csv/Q010-hadith-scan.json` bukhari hits)

Arabic transmission (Bukhārī 3274): *wa-lā aqūlu inna aḥadan afḍalu min Yūnus b. Mattā* — "I do not say that anyone is better than Yūnus b. Mattā".

This is a **canonical Sunni hadith** that appears 6× in Bukhārī alone (in different *abwāb*: kitāb aḥādīth al-anbiyāʾ, kitāb tafsīr, etc.). The hadith is a Prophet-said-it statement of equal-prophet-dignity. It is the most-recurrent Yūnus-related ḥadīth in the Sunni canon.

It has analogues in:
- **Abū Dāwūd #4671, #4672**: with slight variant ("It is not fitting for a prophet to say: I am better than Yūnus b. Mattā") — narrators include Ibn ʿAbbās, ʿAbd Allāh b. Jaʿfar.
- **Abū Dāwūd #202**: in Ibn al-ʿAlīya's al-arbaʿat-aḥādīth list, includes "the tradition about Yūnus son of Mattā" as one of four core traditions transmitted.

## 3. Q 10:62-64 *awliyāʾ Allāh* and the *ruʾyā ṣāliḥa* hadith corpus

ibn Kathīr (Q 10 commentary on v. 62-64) catalogues at least 12 chains for the *awliyāʾ Allāh / lahum al-bushrā fī al-ḥayāti al-dunyā* tradition. Of these, the canonical chain in the 9-book corpus:

- **Bukhārī (#6989-7000 cluster, kitāb al-taʿbīr / book of dream interpretation)**: *al-ruʾyā al-ṣāliḥa min al-rajul al-ṣāliḥ juzʾun min sittatin wa-arbaʿīna juzʾan min al-nubuwwa* — "the good vision of the righteous man is one of forty-six parts of prophecy". The hadith is repeatedly applied (in classical exegesis) to Q 10:64 *lahum al-bushrā fī al-ḥayāti al-dunyā wa-fī al-ākhirah*.
- **Muslim, kitāb al-ruʾyā**: same corpus, with variants on the fraction (44, 46, 70 parts).
- **Tirmidhī, abu-Dāwūd, al-Nasāʾī**: parallel chains with similar phrasing.
- **Aḥmad, *Musnad***: ʿUbāda b. al-Ṣāmit chain — the Prophet's reply to ʿUbāda's question identifying Q 10:64's *bushrā* as the *ruʾyā ṣāliḥa*. Cited in `data/literature/classical-tafsir/raw/ibn-kathir-openiti-Q010.txt` lines 929-944.

**Note on data scan**: the scanner found `darimi-1423` matched SURAT_YUNUS pattern with the Q 10:64 verse fragment *lahum al-bushrā fī al-ḥayāti al-dunyā [Q 10 v. 64]*, and the response is the Prophet identifying it as the good dream tradition. This is the cleanest direct hit in the 9-book scan.

The *awliyāʾ* + *taḥābbū fī Allāh* tradition cluster (Bukhārī, Muslim, Aḥmad) — in which the Prophet identifies the *awliyāʾ Allāh* as those whose mutual love is in God, with no kinship or wealth among them, who will sit on platforms of light, "not afraid when others fear, not grieving when others grieve" (echoing Q 10:62) — is canonically attributed to multiple Companions. ibn Kathīr's catalogue (Q 10 lines 908-913, 950-979) provides the most accessible citation map.

## 4. Q 10:98 *qawm Yūnus* in the hadith corpus

The 9-book scan returned **zero direct text-matches** for the verse fragment *illā qawma Yūnusa* in Arabic-strict regex form. The qawm-Yūnus episode is treated PRIMARILY through tafsir riwāya (Qatāda, Ibn Masʿūd) rather than through a self-standing hadith.

Indirect hits via "Jonah son of Mattā" (the Bukhari cluster above) reflect the prophet-himself rather than his people. The episode of mass repentance is hadith-light, narrated more in tafsir-riwāyah (al-Ṭabarī, ibn Kathīr) than in the canonical hadith collections.

## 5. Faḍāʾil sūrat Yūnus

The Sunni 9-book scan found **no faḍāʾil-of-Q-10** chain meeting the strict-recitation pattern. al-Ṭabarsī (Imāmī, *Majmaʿ al-bayān*) cites a non-Sunni transmission attributed to Imām al-Ṣādiq:

> *"Whoever recites Q 10 every two or three months will not be among the heedless on the Day of Judgment and will be among the *muqarrabīn* of God."* (`data/literature/classical-tafsir/raw/tabarsi-openiti-Q010.txt` line 1)

This is a TWELVER-SHĪʿĪ faḍāʾil tradition, not corroborated in Bukhārī, Muslim, or any of the 9-book Sunni corpus. As such, the fadāʾil-prominence of Q 10 in the Sunni hadith is **LOW** compared to e.g. Q 1 al-Fātiḥa (with its *umm al-Kitāb* corpus), Q 36 Yāsīn (*qalb al-Qurʾān*), Q 67 al-Mulk (*al-Munjiya*), Q 112 al-Ikhlāṣ (*thuluth al-Qurʾān*), Q 2 al-Baqara (*sanām al-Qurʾān*).

This is consistent with H-NEW-860 (hadith-architectural-alignment): high-UAS surahs (Q 33 rank 1, Q 1 rank 2, Q 2 rank 3, Q 9 rank 4, Q 12 rank 6) generally have HIGHER faḍāʾil density. Q 10 (UAS rank 8) has notably LOW faḍāʾil density in the Sunni corpus, while still architecturally significant. This is a mild inversion of the H-NEW-860 pattern and is worth flagging as a potential exception.

## 6. Asbāb al-nuzūl

al-Wāḥidī's *Asbāb al-nuzūl* (English translation; data file at `data/literature/classical-tafsir/raw/asbab-nuzul-wahidi-en-Q002.txt` for Q 2 — Q 10 not yet extracted in this corpus). Classical sources for Q 10 *asbāb*:

- **vv. 2 *qadam ṣidq***: revealed in response to mushrik mockery of Muḥammad as "merely a human"; multiple chains in al-Suyūṭī's *al-Durr al-manthūr*.
- **v. 38 *fa'tū bi-sūratin mithlihī***: revealed in response to the Quraysh's *iftirāʾ* charge; the Quran's challenge to produce one surah of its quality is dated to the period of intensified mushrik denial.
- **v. 94 *fa-in kunta fī shakkin***: per al-Zamakhsharī, this verse may be Medinan; the *asbāb* tradition holds that the Prophet was instructed to reference the People of the Book to corroborate the contents; classical mufassirūn unanimously deny that the Prophet himself was in actual doubt (interpreting it as *iltifāt* directed to the listening community).
- **v. 98 *qawm Yūnus***: tradition (al-Ṭabarī chain via Qatāda, Ibn Masʿūd, Mujāhid) — the verse is part of the Meccan-period polemical-narrative cycle; not tied to a specific occasion, but occurring in the closing-argument stretch of the surah.

## 7. Honest limits

- The scanner used regex-strict patterns. The Quran-quotation patterns *لا خوف عليهم ولا هم يحزنون* and *قل انظروا* may appear in hadith with diacritical variants the scanner missed; manual inspection would expand the citation map.
- *Yūnus* as a transmitter name dominates the YUNUS_ENGLISH hit count (128 hits) and most are NOT Q 10-relevant. Distinguishing transmitter-Yūnus from prophet-Yūnus required filtering by pattern + context.
- The *al-ruʾyā al-ṣāliḥa* hadith corpus is large (cf. Bukhārī k. al-taʿbīr) but the scanner did not match it because the verse-fragment pattern was strict. ibn Kathīr's Q 10 commentary is the most accessible classical bridge.
- al-Ṭabarsī's Q 10 faḍāʾil tradition is Imāmī-only and would require Twelver-Shīʿī hadith corpora (al-Kāfī, *Wasāʾil al-Shīʿa*) for full chain validation; those are NOT in the 9-book Sunni corpus.

## 8. Cross-reference table

| Verse | Hadith chain | Source(s) |
|:--|:--|:--|
| Q 10:62 | *innamā al-awliyāʾ alladhīna idhā ru'ū dhukira allāh* | ibn Kathīr Q10 v. 62 (al-Bazzār chain) |
| Q 10:62-63 | *taḥābbū fī Allāh* (mutual love in God) cluster | ibn Kathīr v. 62 (Aḥmad, Abū Mālik al-Ashʿarī chain); Bukhari k. adab partials |
| Q 10:64 | *al-ruʾyā al-ṣāliḥa min al-mubashshirāt* | Bukhārī k. al-taʿbīr; Muslim k. al-ruʾyā; Aḥmad ʿUbāda b. al-Ṣāmit chain (ibn-Kathir Q10 v. 64) |
| Q 10:98 | *qawm Yūnus / ahl Naynawā* repentance narrative | al-Ṭabarī riwāya (Qatāda, Mujāhid); 9-book canonical: minimal |
| Q 10:overall | *anā lā aqūlu aḥad afḍal min Yūnus b. Mattā* (cross-Quranic) | Bukhārī #3274, 4397, 4398, 4424, 4425, 4598, 4599; Abū Dāwūd #4671, 4672 |
| Q 10:overall recitation | Imām al-Ṣādiq faḍāʾil | al-Ṭabarsī (Imāmī, NOT in 9-book Sunni) |
