---
surah: 13
surah_name_ar: الرعد
surah_name_translit: al-Raʿd
file_type: hadith-corpus
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE
---

# Q 13 al-Raʿd — Hadith Corpus

This file inventories Q 13-relevant hadith citations across the 9-book canonical corpus + supplementary collections. All numbers are pulled from `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/*.json` (the `idInBook` field which corresponds to the standard hadith number) and verified by Arabic-text search.

## 1. Q 13:43 — *man ʿindahu ʿilm al-kitāb* / ʿAbd Allāh b. Salām (PRIMARY classical anchor)

### al-Tirmidhī, *Sunan*, K. al-Tafsīr — Bāb wa-min sūrat al-Raʿd

**Hadith #3340** (`tirmidhi.json` idInBook=3340):
> حدثنا علي بن سعيد الكندي، حدثنا أبو محياة، عن عبد الملك بن عمير، عن ابن أخي عبد الله بن سلام، لما أريد عثمان جاء عبد الله بن سلام...
>
> Chain: ʿAlī b. Saʿīd al-Kindī → Abū Muḥayyāh → ʿAbd al-Malik b. ʿUmayr → the nephew of ʿAbd Allāh b. Salām.

The hadith text recounts that when ʿUthmān was besieged, ʿAbd Allāh b. Salām came (to defend him) and was identified as "the one who has knowledge of the Book" referenced in Q 13:43.

**Tirmidhī's grading**: ḥasan (good) but *gharīb* (single-chain, not widely transmitted). Specifically: *hādhā ḥadīthun ḥasan; lā naʿrifuhu illā min ḥadīth ʿAbd al-Malik b. ʿUmayr*.

**Hadith #3900** (`tirmidhi.json` idInBook=3900): a parallel transmission of the same content via a slightly different chain (also via ʿAlī b. Saʿīd al-Kindī → Abū Muḥayyāh Yaḥyā b. Yaʿlā b. ʿAṭāʾ → ʿAbd al-Malik b. ʿUmayr → ibn akhī ʿAbd Allāh b. Salām → ʿAbd Allāh b. Salām).

**Status**: VERIFIED. The Tirmidhī hadith is one of the primary classical anchors for the al-Suyūṭī-Medinan classification of Q 13: ʿAbd Allāh b. Salām was a Medinan Jewish convert; if v. 43 refers to him, the surah (or at least v. 43) is Medinan.

**Critical caveat**: the hadith is *gharīb* (single-chain). Modern hadith critics flag this as a concern: it's not impossible that the Q 13:43 → ʿAbd Allāh b. Salām identification is a later interpretive overlay rather than a stable Prophetic-era tradition. al-Ṭabarī and al-Qurṭubī survey alternative interpretations.

## 2. Q 13:13 — *yusabbiḥu al-raʿdu* / *du'āʾ al-raʿd* (thunder-supplication tradition)

### al-Bukhārī — tasbīḥ-bi-ḥamdihi general phrase

The phrase *subḥān Allāh wa-bi-ḥamdihi* appears in Q 13:13 (as part of *yusabbiḥu al-raʿdu bi-ḥamdihi*). This phrase is a corpus-wide tasbīḥ formula that appears in 4 hadith of Bukhārī alone:

- **Bukhārī #6438** (`bukhari.json` idInBook=6438): Abū Hurayra → Prophet: "*kalimatāni ḥabībatāni ilā al-Raḥmān, khafīfatāni ʿalā al-lisān, thaqīlatāni fī al-mīzān: subḥān Allāh wa-bi-ḥamdihi, subḥān Allāh al-ʿaẓīm*". (Two phrases beloved to the Most Merciful, light on the tongue, heavy in the scale: *subḥān Allāh wa-bi-ḥamdihi*, *subḥān Allāh al-ʿaẓīm*).
- **Bukhārī #6166** (`bukhari.json` idInBook=6166): Abū Hurayra → Prophet: "Whoever says *subḥān Allāh wa-bi-ḥamdihi* a hundred times in a day, his sins are wiped away..."
- **Bukhārī #6167** (`bukhari.json` idInBook=6167): parallel narration via Abū Zurʿa → Abū Hurayra.
- **Bukhārī #7277** (`bukhari.json` idInBook=7277): same content, different chain.

**Muslim parallels**: 7 hadith match the *subḥān Allāh wa-bi-ḥamdihi* phrase including #6677, #6678, #6680, #6745.

**Status**: VERIFIED in `ahmedbaset-json` corpus. These hadith are NOT specifically about Q 13:13 — they cite the *phrase*, which appears in Q 13:13 and elsewhere. The phrase has its own popularity independent of Q 13's revelation context.

### al-Tirmidhī, *al-Daʿawāt* — du'āʾ al-raʿd

There exists a tradition (cited by Ibn Kathīr in his Q 13:13 commentary, and via al-Suyūṭī in *al-Durr al-manthūr*) that "*when the Prophet heard the thunder, he would say: subḥān al-ladhī yusabbiḥu al-raʿdu bi-ḥamdihi wa-l-malāʾikatu min khīfatihi*" — citing Q 13:13 directly as the supplication.

**Search result in our corpus** (`ahmedbaset-json` Tirmidhī search for "يسبح الرعد بحمده" or "سبحان الذي يسبح الرعد"): NO direct match found in the digital corpus. The tradition is cited via secondary-level scholarship (Ibn Kathīr, al-Suyūṭī Durr) but the specific Tirmidhī number, if any, was not located in our search.

**Status**: SECONDARY-TRIANGULATED via Ibn Kathīr + al-Suyūṭī. The specific Tirmidhī hadith number for the *du'āʾ al-raʿd* is flagged as **PENDING — not located in `ahmedbaset-json` digital corpus**. Per MW-6, no nawʿ-number-specific claim is downstream of this.

## 3. Q 13:8 — *taghīḍu al-arḥām* (wombs and divine knowledge)

### al-Dārimī, *Sunan* — interpretation of Q 13:8

`darimi` matches in our corpus (search results pre-test):
- **Dārimī #261** (`darimi.json` idInBook=261): Mujāhid asked about a pregnant woman seeing menstrual blood; Mujāhid cites Q 13:8 *wa-mā taghīḍu al-arḥāmu* — "what the wombs lose" — interpreting the verse as covering pregnancy-bleeding.
- **Dārimī #262, #264, #265**: parallel narrations via ʿIkrima and Mujāhid on the same Q 13:8 interpretation, all citing the verse (*sūrat al-raʿd āyat 8*) by chapter and verse number.

**Status**: VERIFIED. These four Dārimī narrations are explicit Q 13:8 citations in classical exegesis (early-Companion-and-Tābiʿūn-era interpretation transmitted by al-Dārimī). They are not Prophetic hadith but *aqwāl* of Mujāhid and ʿIkrima — *tafsīr al-tābiʿīn*.

## 4. Q 13:11 — *al-muqaqqibāt* (succeeding angels)

### Verbal traditions

The phrase *al-muqaqqibāt* (succeeding angels) is corpus-rare (appears only in Q 13:11, see `02-content-analysis.md` §7). Classical hadith specifically about *muqaqqibāt-as-angels* exist in tafsir-by-tradition collections:

**Search result in `ahmedbaset-json` 9-book corpus for "معقبات" or "المعقبات"**: NO direct match found. The succeeding-angels tradition appears in tafsir-collections (al-Ṭabarī, *Jāmiʿ al-bayān*; Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*) citing Companion-era reports, but does not appear as a self-standing Prophetic hadith in the 9-book corpus per our search.

**Status**: NOT-FOUND in 9-book canonical hadith. The *muqaqqibāt-as-angels* doctrine is from tafsir-tradition (Ibn ʿAbbās via Saʿīd b. Jubayr; Mujāhid; ʿIkrima) cited within tafsir works, NOT from canonical hadith collections. Per MW-6, no canonical-hadith-claim is downstream of this; the doctrine is classically grounded but in the tafsir corpus, not the hadith corpus.

## 5. Q 13:28 — *bi-dhikri Allāhi taṭmaʾinnu al-qulūb*

### Search result

The hearts-at-rest verse is one of the most-quoted single verses in Sufi devotional literature (al-Ghazālī's *Iḥyāʾ ʿulūm al-dīn*, al-Tustarī, al-Qushayrī's *Risāla*). In the 9-book hadith corpus, search for *taṭmaʾinnu al-qulūb* or *تطمئن القلوب* yielded NO direct hadith match.

**Status**: NOT-FOUND in 9-book canonical hadith specifically as *Q 13:28-citation*. The verse's classical fame comes from tafsir + Sufi-devotional reception, not from a Prophetic-hadith citation chain. The Sufi reception is documented in al-Ghazālī, al-Qushayrī, al-Tustarī (see `data/literature/classical-tafsir/classical-on-rad-verse-28.md` for the survey).

## 6. Recitation traditions (no surah-specific virtue hadith located)

Search for *faḍāʾil sūrat al-raʿd* or *fadl Sūrat al-Raʿd* in `ahmedbaset-json` 9-book corpus: NO direct match found. Q 13 al-Raʿd does NOT have a documented *faḍāʾil al-suwar* hadith in the canonical 9-book corpus, comparable to (e.g.) Q 36 Yāsīn, Q 67 al-Mulk, or Q 112 al-Ikhlāṣ.

This is consistent with the empirical UAS rank 21/114 (mid-pack) and the absence of Q 13 from the classical *faḍāʾil al-suwar* anchored surahs (Q 1, 2, 18, 36, 55, 67, 112-114). Q 13's classical importance is in its **specific marquee verses** (Q 13:11 muqaqqibāt, Q 13:13 thunder, Q 13:28 hearts-at-rest, Q 13:31 iʿjāz-singular, Q 13:43 ʿilm al-kitāb), not in surah-level recitation merit.

## 7. Summary table

| Q 13 verse | Hadith collection | ḥadīth # | Status | Theme |
|:-:|:-:|:-:|:-:|:--|
| Q 13:43 | Tirmidhī | **#3340, #3900** | VERIFIED, ḥasan-gharīb | ʿAbd Allāh b. Salām = ʿilm al-kitāb |
| Q 13:8 | Dārimī | #261, #262, #264, #265 | VERIFIED, *tafsīr al-tābiʿīn* | wombs-pregnancy-loss |
| Q 13:13 (phrase) | Bukhārī | #6166, 6167, 6438, 7277 | VERIFIED but PHRASE-LEVEL | subḥān Allāh wa-bi-ḥamdihi |
| Q 13:13 (phrase) | Muslim | #6677, 6678, 6680, 6745, etc. | VERIFIED but PHRASE-LEVEL | tasbīḥ formula |
| Q 13:13 (du'āʾ al-raʿd) | (Tirmidhī?) | NOT-LOCATED | SECONDARY-TRIANGULATED | thunder-supplication |
| Q 13:11 muqaqqibāt | (none in 9-book) | NOT-FOUND | tafsir-tradition only | succeeding-angels |
| Q 13:28 | (none in 9-book) | NOT-FOUND | Sufi-devotional only | hearts-at-rest |
| Q 13 fadāʾil | (none in 9-book) | NOT-FOUND | — | (no surah-level merit hadith) |

## 8. Cross-references

- `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json` (#3340, #3900 verified)
- `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json` (#6166, #6167, #6438, #7277 verified)
- `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json` (#6677, #6678, #6680, #6745 verified)
- `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/darimi.json` (#261, #262, #264, #265 verified)
- `data/literature/classical-tafsir/classical-on-rad-verse-28.md` (Q 13:28 secondary-tafsir survey)
- `03-tafsir-survey.md` (mufassirūn cite the hadiths above as part of their commentary)
- `05-classical-claims-audit.md` (Q 13:43 ʿAbd Allāh b. Salām → chronology audit, with hadith strength explicitly weighed)

## 9. Honest reporting note

The Q 13 hadith corpus in our digital index is **modest by canonical-surah standards**. There is no *faḍāʾil al-Raʿd* hadith equivalent to Q 36 Yāsīn or Q 67 al-Mulk. The two strongest classical anchors are:
1. Tirmidhī #3340/#3900 (Q 13:43 → ʿAbd Allāh b. Salām) — a *ḥasan-gharīb* chain, foundational for the Medinan-classification claim but contestable.
2. Bukhārī/Muslim *subḥān Allāh wa-bi-ḥamdihi* (Q 13:13 phrase appears) — phrase-level, not surah-specific.

The modest hadith profile is consistent with Q 13's empirical UAS mid-pack rank (21/114) and the absence of corpus-level *faḍāʾil-tradition* prominence. Q 13's classical importance is in its **theological-content density** (cosmological signs, iʿjāz declaration, hearts-at-rest motif) and the chronology debate that those marquee verses generate.
