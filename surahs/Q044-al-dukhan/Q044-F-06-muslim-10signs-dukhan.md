---
finding_id: Q044-F-06
surah: 44
surah_name: al-Dukhān
file_type: hadith-verification
date: 2026-05-10
verdict: VERIFIED-PARTIAL
prereg_sha: a3a29927abfd04ef9f5c72199751d0f7a0ad526294422cc0fc1d42fefdce8ce3
---

# Q044-F-06 — Muslim 10-signs-of-hour hadith verification (dukhān)

## Verdict

**VERIFIED-PARTIAL.** The pre-committed direction was "at least one of Muslim #2901, #2902 contains دخان." Observed: Muslim #2901 and #2902 (in the on-disk ahmedbaset numbering) are both Hajj/Umra hadiths about circumambulation — NOT the 10-signs-of-hour hadith. The 10-signs-of-hour hadith with دخان IS present in Muslim's on-disk corpus at **idInBook #7106** and **#7107**.

## Findings

- Muslim corpus on disk has 7459 hadiths.
- 10 hadiths in Muslim contain the word دخان (diacritic-stripped match).
- 2 of those (#7106 and #7107) explicitly list دخان as one of the *ʿashar āyāt* (10 signs of the Hour).
- #2901 and #2902 are unrelated (Hajj/Umra).

## Sample text (#7106 from disk, diacritic-stripped)

> اطلع النبي صلى الله عليه وسلم علينا ونحن نتذاكر فقال "ما تذاكرون". قالوا نذكر الساعة. قال "إنها لن تقوم حتى ترون قبلها عشر آيات". فذكر **الدخان** والدجال والدابة وطلوع الشمس من مغربها ونزول عيسى ابن مريم صلى الله عليه وسلم ويأجوج ومأجوج وثلاثة خسوف خسف بالمشرق وخسف بالمغرب وخسف بجزيرة العرب وآخر ذلك نار تخرج من اليمن تطرد الناس إلى محشرهم.

## Interpretation

The classical citation tradition often gives the 10-signs hadith as "Muslim #2901" using Abdul-Baqi's continuous numbering through Sahih Muslim. The on-disk corpus (ahmedbaset-json) uses a per-book *idInBook* counter that puts the same hadith at #7106-7107 (Kitāb al-Fitan section). The hadith and its content are verified: **the 10-signs hadith DOES list dukhān as one of the eschatological signs, in Sahih Muslim, narrated from Ḥudhayfa b. Asīd via Abū al-Ṭufayl, via Furāt al-Qazzāz**.

The classical-tradition linkage between Q 44:10 (*yawma taʾtī al-samāʾu bi-dukhānin mubīn*) and the 10-signs hadith is therefore **empirically anchored on disk**. The exact-number direction-lock failed (pre-commit honored) but the substantive citation is verified.

## Anti-hallucination check

Per Protocol §2.11, this finding cites:
- File: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json`
- Hadith idInBook: #7106 (and #7107 in parallel)
- Narrator chain: Ḥudhayfa b. Asīd → Abū al-Ṭufayl → Furāt al-Qazzāz → Sufyān b. ʿUyayna (or Shuʿba) → al-ḥadīth.

The corrected citation for future work: **Muslim, Ṣaḥīḥ, idInBook #7106 (or Kitāb al-fitan wa-ashrāṭ al-sāʿah), narrated via Ḥudhayfa b. Asīd.**

## Cross-references

- [[Q044-al-dukhan/Q044-F-01|Q044-F-01]] — dukhān bracket pattern (literal/eschatological tafsir debate).
- [[Q044-al-dukhan/04-hadith-corpus|Q 44 hadith corpus]] — needs update with the corrected hadith number.

## Honest limits

- Numbering convention differs across editions; the on-disk corpus uses *idInBook* (per-book counter), not Abdul-Baqi continuous.
- A separate test of #7106/#7107 as the *primary* 10-signs locus could be pre-registered as a follow-up.
- The 10 hadiths containing دخان in Muslim include some related to general fire-smoke imagery (not eschatological); the 2 explicit 10-signs loci are the primary classical citations.

## Files

- pre-reg: `preregs/Q044-F-06-bukhari-10-signs-prereg.md`
- script: `scripts/Q044_F_06_muslim_10signs_dukhan.py`
- output: `csv/Q044-F-06.json`
