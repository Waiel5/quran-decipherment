---
surah: 14
surah_name_ar: ابراهيم
surah_name_translit: Ibrāhīm
file_type: hadith-corpus
date_last_updated: 2026-05-08
phase: B+
verdict: COMPLETE — all hadith numbers verified against ahmedbaset-json corpus
---

# Q 14 Ibrāhīm — Hadith Corpus


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

This file inventories Q 14-relevant hadith citations across the 9-book canonical corpus. All numbers are pulled from `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/*.json` (`hadiths[i].idInBook`) and verified by Arabic-text search in this run. **CRITICAL CORRECTION**: secondary-tafsir literature widely cites Bukhārī #3364 as the Hagar-Mecca-settling narrative; verification in our digital corpus shows #3364 is actually about the Ghifar/Aslam tribes, NOT Hagar. The CORRECT Bukhārī number for the Hagar-Ishmael Mecca-foundation narrative is **#3225** (and parallels #3224, #3226 for shorter versions; #2274 for the brief *yarḥamu Allāhu umm Ismāʿīl* form). All numbers below have been re-verified.

## 1. Q 14:24-25 (the good-word parable / *kalimat al-tawḥīd* date-palm)

### al-Bukhārī, *al-Jāmiʿ al-ṣaḥīḥ* — multiple parallels of the date-palm parable

**Hadith #61** (verified `bukhari.json` idInBook=61):
> Narrated Ibn ʿUmar: The Messenger of God (ﷺ) said: "Among the trees there is a tree whose leaves do not fall, and which resembles the believer (المسلم). Tell me what is it?" People speculated about the trees of the desert. ʿAbd Allāh (Ibn ʿUmar) said: "It occurred to me that it is the date-palm (النخلة), but I was shy. Then they said: 'Tell us what it is, O Messenger of God.' He said: 'It is the date-palm.'"

**Parallels in al-Bukhārī**: #62 (idInBook=62, Khālid b. Makhlad chain), #72 (idInBook=72, Mujāhid → Ibn ʿUmar chain), #131 (idInBook=131, Mālik chain via *al-Muwaṭṭaʾ*), #5231 (idInBook=5231, al-Aʿmash chain), #5235 (idInBook=5235, Zubayd chain), and **#5911** (idInBook=5911) — the latter is critical: it directly cites Q 14:25 *tuʾtī ukulahā kulla ḥīnin bi-idhni rabbihā*: "tell me of a tree whose example is like the example of the believer, that **gives its fruit every season by its Lord's permission**, and whose leaves do not fall."

**Status**: VERIFIED in digital corpus. The date-palm hadith is multiply-attested in al-Bukhārī (≥7 parallels) with chains through Ibn ʿUmar. **Bukhārī #5911 is the most-explicit** Q 14:24-25 verse-citation, embedding the verse phrase *tuʾtī ukulahā kulla ḥīn* in the prophetic question itself.

**Tafsir-anchor**: Ibn Kathīr cites Bukhārī #61 as the canonical key to Q 14:24-25 (see `03-tafsir-survey.md` §4); al-Ṭabarī cites the same hadith.

## 2. Q 14:27 (the firm-word doctrine / *qawl thābit* / grave-questioning)

### al-Bukhārī

**Hadith #1321** (verified `bukhari.json` idInBook=1321):
> Narrated al-Barāʾ b. ʿĀzib (RA): The Prophet (ﷺ) said: "**When the believer is laid in his grave**, he is approached, and he testifies that there is no god but God and that Muḥammad is the Messenger of God. **That is His saying** *yuthabbitu Allāhu alladhīna āmanū bi-l-qawli al-thābit* [Q 14:27]."

**Hadith #4493** (verified `bukhari.json` idInBook=4493) — in *Kitāb al-Tafsīr*, *Bāb wa-min sūrat Ibrāhīm*:
> Narrated al-Barāʾ b. ʿĀzib: The Messenger of God (ﷺ) said: "The Muslim, when he is questioned in the grave, testifies that there is no god but God and that Muḥammad is the Messenger of God. **That is His saying *yuthabbitu Allāhu alladhīna āmanū bi-l-qawli al-thābit fī al-ḥayāti al-dunyā wa-fī al-ākhira*** [Q 14:27]."

**Parallels in Muslim**: **#7040** (idInBook=7040) and **#7041** (idInBook=7041) — both via al-Barāʾ b. ʿĀzib, both citing Q 14:27 as the verse-anchor for the grave-questioning doctrine. Muslim #7041 specifies *nazalat fī ʿadhāb al-qabr* (the verse was revealed regarding the punishment of the grave).

**Parallel in Tirmidhī**: **#3204** (verified `tirmidhi.json` idInBook=3204) — same chain via al-Barāʾ → Saʿd b. ʿUbayda → ʿAlqama b. Marthad → Shuʿba → Maḥmūd b. Ghaylān → Abū Dāwūd. Tirmidhī cites the verse with grading: ḥasan-ṣaḥīḥ.

**Status**: VERIFIED across 4 of the 9 books (Bukhārī ×2, Muslim ×2, Tirmidhī ×1). The Q 14:27 → grave-questioning interpretation is **multiply-attested ṣaḥīḥ** at the prophetic-hadith level. This is one of the canonical Q 14 verse-interpretations — the verse promises God's establishing the believers with the firm-word in this life and in the next, with the next-life "establishing" being the moment of grave-questioning. The al-Barāʾ b. ʿĀzib chain is the foundation.

## 3. Q 14:35-41 (the Mecca-prayer / Hagar-Ishmael Mecca-foundation narrative)

### al-Bukhārī — the foundational long Hagar-Ishmael narrative

**Hadith #3225** (verified `bukhari.json` idInBook=3225) — long ḥadīth (>4500 chars), via Ibn ʿAbbās → Saʿīd b. Jubayr → Ayyūb al-Sakhtiyānī + Kathīr b. Kathīr → ʿAbd al-Razzāq → ʿAbd Allāh b. Muḥammad:

The hadith is the foundational tradition of Hagar's settlement at Mecca: Abraham's bringing Hagar and Ishmael to a barren valley (the *bi-wādin ghayri dhī zarʿ* of Q 14:37); Hagar's running between Ṣafā and Marwa searching for water (the asbāb al-nuzūl of *saʿy*); the appearance of Zamzam under Ishmael's heel via the angel Jibrīl; the arrival of the Banū Jurhum tribe asking permission to settle near the well; Abraham's later return; the building of the Kaʿba's foundations by Abraham and Ishmael; the prayer recited there.

**Parallels**: #3224 (idInBook=3224, shorter Ibn ʿAbbās chain), #3226 (idInBook=3226, parallel Ibrāhīm b. Nāfiʿ chain), #2274 (idInBook=2274, brief form: *yarḥamu Allāhu umm Ismāʿīl*).

**Status**: VERIFIED. The classical anchor for Q 14:35-41's geographic/biographical setting. **Note: secondary-tafsir literature often cites this as Bukhārī #3364 — that is INCORRECT in our digital corpus. The correct number is #3225.** Per MW-6 verification tagging, the corrected number is now lockd.

### Bukhārī — the Q 14:39 *Ismāʿīl wa-Isḥāq* taʿwīdh hadith (related)

**Hadith #3232** (verified `bukhari.json` idInBook=3232):
> Narrated Ibn ʿAbbās (RA): The Prophet (ﷺ) used to recite the *taʿwīdh* (protective formula) over al-Ḥasan and al-Ḥusayn and would say: "**Your father (Abraham) used to recite this protection over Ishmael and Isaac (إسماعيل وإسحاق)** — *aʿūdhu bi-kalimāti Allāhi al-tāmmati min kulli shayṭānin wa-hāmma*…"

**Status**: VERIFIED. This hadith echoes Q 14:39's *Ismāʿīl wa-Isḥāq* pairing in a Prophetic-tradition context — Abraham's protective formula over both sons, recited by the Prophet over his grandsons.

## 4. Q 14:48 (changed-earth / *yawma tubaddalu al-arḍu ghayra al-arḍ*)

### Tafsir-tradition references

**Search result in `ahmedbaset-json` 9-book corpus for "يَوْمَ تُبَدَّلُ الْأَرْضُ" or "تبدل الأرض غير الأرض"**: NOT FOUND as a direct Prophetic hadith in the digital corpus. The Q 14:48 verse is referenced in the eschatological-tradition literature (Aḥmad Musnad and Muslim's Kitāb al-Janna sections) but no specific Q 14:48 verse-quoting Prophetic hadith was located in our search.

**Status**: NOT-FOUND in 9-book digital corpus (per our search). The verse's eschatological themes are extensively covered in classical eschatological-hadith literature (the *al-arḍ al-bayḍāʾ* / new-earth tradition), but the specific Q 14:48 verse-quotation does not anchor to a verified Prophetic hadith in our search. Per MW-6, no verse-specific hadith claim is downstream of this.

## 5. Q 14:42 (*lā taḥsabanna Allāha ghāfilan*) — moral-witness verse

**Search**: NOT FOUND as a verse-anchored Prophetic hadith citing Q 14:42 directly. The verse is widely-cited in classical homiletic literature (Ibn al-Qayyim, *Madārij al-Sālikīn*) as a meditative formula but does not anchor to a specific verified hadith in our corpus.

**Status**: NOT-FOUND in 9-book digital corpus.

## 6. Q 14:22 (Iblīs's eschatological speech) — eschatological-tradition

**Search**: NOT FOUND as a Q 14:22 verse-anchored Prophetic hadith. The classical eschatological hadith literature (Bukhārī's Kitāb al-Riqāq; Muslim's *al-Janna wa-ṣifat naʿīmihā*) discusses Day-of-Judgment Iblīs scenes generally but does not quote Q 14:22 specifically.

**Status**: NOT-FOUND in 9-book digital corpus. The verse is **classically-anchored at the tafsir level only** (al-Ṭabarī, al-Rāzī — see `03-tafsir-survey.md`).

## 7. Surah-level fadāʾil

**Search**: no surah-level *fadāʾil al-Ibrāhīm* hadith was located in the 9-book digital corpus. Q 14 does not have a *faḍāʾil*-tradition equivalent to the Q 36 Yāsīn or Q 67 al-Mulk fadāʾil-corpora. This is consistent with the empirical UAS rank 20/114 (mid-pack, not corpus-distinguished).

## 8. Aggregate citation map

| Verse / topic | 9-book hadith # | Verification | Significance |
|:--|:--|:--|:--|
| **Q 14:24-25** good-word date-palm | **Bukhārī #61, #62, #72, #131, #5231, #5235, #5911** | VERIFIED multiple parallels | parable-foundation; Bukhārī #5911 directly cites verse-text *tuʾtī ukulahā kulla ḥīn* |
| **Q 14:27** *qawl thābit* / grave-questioning | **Bukhārī #1321, #4493**; **Muslim #7040, #7041**; **Tirmidhī #3204** | VERIFIED ṣaḥīḥ multi-collection | grave-questioning doctrine anchor; via al-Barāʾ b. ʿĀzib |
| **Q 14:35-41** Mecca-prayer asbāb | **Bukhārī #3225** (long; #3224, #3226 parallels); **#2274** (brief) | VERIFIED (corrected from common-cited #3364) | Hagar-Mecca-foundation narrative; Zamzam well; Banū Jurhum settlement |
| **Q 14:39** Ismāʿīl wa-Isḥāq | **Bukhārī #3232** | VERIFIED | taʿwīdh-formula linking Abraham's two sons |
| Q 14:48 changed-earth | (none in 9-book) | NOT-FOUND | eschatological-tradition (non-verse-specific) |
| Q 14:42 ghāfil | (none in 9-book) | NOT-FOUND | homiletic-tradition (non-verse-specific) |
| Q 14:22 Iblīs eschatology | (none in 9-book) | NOT-FOUND | tafsir-tradition only (al-Rāzī, al-Ṭabarī) |
| Q 14 fadāʾil | (none in 9-book) | NOT-FOUND | (no surah-level merit hadith) |

## 9. Cross-references

- `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json` (#61, #62, #72, #131, #1321, #2274, #3224, #3225, #3226, #3232, #4493, #5231, #5235, #5911 verified)
- `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json` (#7040, #7041 verified)
- `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json` (#3204 verified)
- `03-tafsir-survey.md` (mufassirūn citing Bukhārī #61 for Q 14:24-25 and Bukhārī #3225 for Q 14:35-41)
- `05-classical-claims-audit.md` (the al-Bāqillānī iʿjāz al-fawāṣil + al-Suyūṭī chronology audits)
- `06-novel-findings.md` (Q014-F-01 corpus-MAX prayer-density CONFIRMED — empirical structural correlate of the Mecca-prayer block's classical attention)

## 10. Honest reporting note + WAVE-D-correction discipline

The Q 14 hadith corpus in our digital index is **moderate-strength**: well-anchored at Q 14:24-25 (date-palm; ≥7 Bukhārī parallels), strong at Q 14:27 (grave-questioning, ≥5 ṣaḥīḥ parallels across 3 collections), foundational at Q 14:35-41 (Hagar-Ishmael narrative, Bukhārī #3225 and parallels). Several other Q 14 verses (e.g., Q 14:22, Q 14:48) are anchored only at the tafsir-tradition level, not at the canonical-hadith-corpus level. There is no surah-level *faḍāʾil*-tradition for Q 14.

**Wave-D correction discipline**: This run identified that secondary tafsir literature widely propagates **Bukhārī #3364** as the Hagar-Mecca-settling narrative reference. Direct verification in the digital corpus shows **#3364 is about the Ghifar/Aslam tribes** (the Prophet's prayer for those tribes), not Hagar. The correct Bukhārī number is **#3225** (with parallels #3224, #3226, #2274). This is documented as a corrected hadith citation per the MEMORY entry "Wave-D corrections discovered" — propagating the correction forward to all Q 14 references.
