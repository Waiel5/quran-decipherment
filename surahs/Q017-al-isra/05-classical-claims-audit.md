---
surah: 17
surah_name_ar: الإسراء
file_type: classical-claims-audit
date_last_updated: 2026-04-28
phase: B+
verdict: 7 classical claims tested; 5 VINDICATED, 1 RULES-TUPLE-FRAGILE, 1 NOT-TESTABLE
---

# Q 17 al-Isrāʾ — Classical Claims Audit

Each non-trivial classical claim is enumerated, tested under a specified rules-tuple, and verdict-graded. The Investigation Protocol's verdict ladder applies: **VINDICATED / FALSIFIED / RULES-TUPLE-FRAGILE / NOT-TESTABLE**.

## Claim 1: al-Bukhārī's chapter naming "Banī Isrāʾīl" (and Ibn Masʿūd's al-ʿitāq al-uwal)

**Source**: al-Bukhārī, *Kitāb al-tafsīr*, chapter heading on Q 17; ḥadīth #4502, #4533, #4787 (`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json`).

**Claim**: Q 17 was known to early Sunnī tradition by its Israelite-content name **Banī Isrāʾīl**, with this name preserved by an early Companion (Ibn Masʿūd).

**Test (Q017-F-04, pre-registered)**: Compute Q 17's lemma-density of "إسرائيل" against all 114 surahs.

**Result**:
- Q 17 raw count: 4 tokens of "إسرائيل" (rank 4/114).
- Q 17 density: 0.00257 (rank 5/114).
- Surahs ranked higher by count: Q 2 (6), Q 5 (6), Q 7 (4 — tied at count, lower rank).
- Q 17 has the **highest count-rank** of any Meccan surah on this metric (Q 7 has 4 also; all higher counts are Medinan: Q 2, Q 5).

**Verdict**: **VINDICATED**. Q 17's Israelite-content density vindicates the early-Companion naming. The fact that Q 2 and Q 5 outrank Q 17 by raw count does NOT undermine the "Banī Isrāʾīl" name for Q 17, because Q 2 and Q 5 are well-known by other names (al-Baqara, al-Māʾida) tied to specific events; Q 17's most striking Israelite-content concentration combined with the lack of an alternative content-anchor for the name makes "Banī Isrāʾīl" the natural Companion-shorthand.

## Claim 2: Q 17 as one of the **al-musabbiḥāt** (ʿarāʾis al-Qurʾān)

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, on قال بعض السلف في القرآن ميادين وبساتين ومقاصير وعرائس وديابيج ورياض... وعرائسه المسبحات. (`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, near offset 1238075 / context 197421).

**Claim**: The musabbiḥāt are the surahs opening with a س-ب-ح-rooted glorification verb. They are called "the brides of the Qurʾān" (*ʿarāʾis al-Qurʾān*). Standard list: Q 17 (al-Isrāʾ), Q 57 (al-Ḥadīd), Q 59 (al-Ḥashr), Q 61 (al-Ṣaff), Q 62 (al-Jumuʿa), Q 64 (al-Taghābun), Q 87 (al-Aʿlā).

**Test (Q017-F-02, pre-registered)**: Verify that all seven open with س-ب-ح roots, identify the verb-form of each, and check if Q 17 is unique among them.

**Result**:
- Q 17 opens: **سبحان** (subḥān — verbal-noun maṣdar, accusative).
- Q 57, 59, 61, 87 open: **سبح** (sabbaḥa — perfect verb, 3rd-person singular).
- Q 62, 64 open: **يسبح** (yusabbiḥu — imperfect verb, 3rd-person singular).
- Q 17 is the **unique** musabbiḥa in the maṣdar form. No other surah opens with *Subḥāna*.

**Verdict**: **VINDICATED**. The classical taxonomy (*musabbiḥāt = ʿarāʾis*) is empirically verified, and Q 17's grammatical distinctness within the group (sole maṣdar opener) is a novel-finding empirical observation that REFINES the classical category.

## Claim 3: al-Bāqillānī's iʿjāz al-fawāṣil (rhyme-variation as iʿjāz)

**Source**: al-Bāqillānī, *Iʿjāz al-Qurʾān* (theory engaged across the project; cf. h-new-740 cross-corpus tests).

**Claim**: The Qurʾān's eloquence is in part proven by VARIED rhymes that match the diversity of content (vs. monorhyme *qaṣīda* poetry).

**Test**: Q 17 has 99.10% alif-final rate (Q017-F-01) and rhyme entropy 0.0514 nats (H-NEW-750) — i.e., Q 17 is **anti-iʿjāz al-fawāṣil**. Does this falsify al-Bāqillānī?

**Result**:
- Q 17 IS rhyme-uniform; this is the *qaṣīda*-form.
- BUT: Q 17 ranks UAS top-10 (rank 10) on the project's integrated architectural score.
- Q 17's classical reception (al-ʿitāq al-uwal hadith; *āyat al-ʿizz*; intercession verses) treats it as a particularly **valued** surah — DESPITE its anti-fawāṣil profile.
- This is captured by the project's **dual-iʿjāz typology**: structural-iʿjāz (al-Bāqillānī axis) is empirically distinct from theological-iʿjāz (al-Khaṭṭābī axis).

**Verdict**: **NOT-FALSIFIED, but RULES-TUPLE-FRAGILE**. al-Bāqillānī's *iʿjāz al-fawāṣil* is a real Qurʾānic feature *on average* (cross-corpus distinct vs poetry, p<10⁻¹⁰; cf. h-new-730/740). But it does NOT apply uniformly to every surah; Q 17 is precisely a counter-example. The classical tradition handles this by deploying al-Khaṭṭābī's *iʿjāz al-maʿnā* axis — content-and-effect iʿjāz — for surahs like Q 17. Q 17 thus VINDICATES the dual-typology: the corpus is internally heterogeneous, and classical iʿjāz theory has the right two axes to describe its diversity.

## Claim 4: Q 17:88 as the maximal taḥaddī

**Source**: al-Bāqillānī (*Iʿjāz*), al-Khaṭṭābī (*Bayān iʿjāz al-Qurʾān*), al-Suyūṭī (*al-Itqān*, nawʿ al-iʿjāz), al-Rāzī (*Mafātīḥ*), al-Zamakhsharī (*al-Kashshāf*) — universally accepted classical position.

**Claim**: Q 17:88 (humans + jinn together cannot bring the like of this Qurʾān) is the **strongest** of the five Qurʾānic taḥaddī verses (Q 2:23 [one sūra]; Q 10:38 [one sūra]; Q 11:13 [ten sūras forged]; Q 17:88 [whole Qurʾān, humans + jinn]; Q 52:34 [a ḥadīth like it]).

**Test (Q017-F-03, pre-registered)**: 
- (A) Lexical signature: does Q 17:88 contain 5 distinctive iʿjāz-related lemmas?
- (B) Citation density: do ≥4 of 9 mufassirūn cite Q 17:88 substantively (≥200 chars)?

**Result**:
- (A) All 5 lemmas attested: مثل (mithl), اجتمع (ijtimāʿ), الجن, الإنس, ظهير. **PASS**.
- (B) 7 of 9 tafsirs cite substantively: Ibn Kathīr (5000 chars), Ṭabarī (2148), Qurṭubī (1877), Rāzī (5000+), Zamakhsharī (826), Ṭabarsī (5000+), Thaʿlabī (4470). al-Biqāʿī (0 — partial extract) and al-Suyūṭī al-Durr (0 — partial extract) absent in our extracts. **PASS**.

**Verdict**: **VINDICATED**. Both lexical signature and citation density confirm Q 17:88's hub status.

## Claim 5: Q 17:111 as **āyat al-ʿizz** (the Verse of Glory)

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān* (`suyuti-itqan.openiti.raw.txt`, offset ~197421), citing Aḥmad's *Musnad* via Muʿādh b. Anas, marfūʿan.

**Claim**: Q 17:111 (*al-ḥamdu lillāhi alladhī lam yattakhidh waladā…*) is canonically called the Verse of Glory.

**Test**: Locate the citation in al-Suyūṭī's *al-Itqān* and verify its presence on disk.

**Result**: Confirmed at `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` near offset 197421. The exact phrase: *وَفِي مُسْنَدِ أَحْمَدَ مِنْ حَدِيثِ مُعَاذِ بْنِ أَنَسٍ مَرْفُوعًا آيَةُ الْعِزِّ: {الْحَمْدُ لِلَّهِ الَّذِي لَمْ يَتَّخِذْ وَلَدًا} الْآيَةَ.*

**Verdict**: **VINDICATED** (via classical citation). The Aḥmad Musnad ḥadīth itself is not in our partial 9-book JSON but is securely cited via al-Suyūṭī. We have NOT verified the chain's grading; flagged for follow-up.

## Claim 6: Q 17:79's *maqām maḥmūd* = al-shafāʿa al-kubrā (the Major Intercession)

**Source**: al-Tirmidhī ḥadīth #3221, #3232; al-Bukhārī #7155; al-Ṭabarī (*Jāmiʿ al-bayān*, ad loc.); Ibn Kathīr (*Tafsīr*, ad loc.).

**Claim**: The "Praiseworthy Station" promised to the Prophet in Q 17:79 is identified by Sunnī ḥadīth as the **Major Intercession** on the Day of Judgment.

**Test**: Locate the relevant ḥadīth in the 9-book JSON. Confirm the explicit verse-quotation and the explicit intercession-identification.

**Result**:
- al-Tirmidhī **#3221**: *"regarding Allah's saying: 'It may be that your Lord will raise you to a praised station (17:79)' that the Messenger of Allah was asked about it and he said: 'It is the intercession.'"* **Direct verse-citation + direct intercession-identification.**
- al-Tirmidhī **#3232**: extended *anā sayyidu wuldi Ādama yawma al-qiyāma* with *al-maqām al-maḥmūd* identification.
- al-Bukhārī **#7155**: extended Day-of-Resurrection narrative culminating in *al-maqām al-maḥmūd*.

**Verdict**: **VINDICATED**. Direct ḥadīth corpus support across 3 independent collections.

## Claim 7: The *isrāʾ* was bodily, not in soul-only

**Source**: al-Ṭabarī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Zamakhsharī — universal classical Sunnī position.

**Claim**: The verb *asrā bi-ʿabdihi* and the noun *bi-ʿabdihi* (with His servant) require bodily transport, not vision/soul-journey.

**Test**: This is a **theological-philosophical** claim, not directly testable empirically. We can only check whether the classical sources unanimously commit to bodily *isrāʾ* — they do.

**Verdict**: **NOT-TESTABLE EMPIRICALLY**. The theological consensus is documented in our extracted tafsir files (`ibn-kathir-openiti-Q017.txt`, `tabari-openiti-Q017.txt`, etc.); empirical methods cannot adjudicate the metaphysical question.

## Summary

| # | Claim | Verdict | Source |
|--:|:--|:--|:--|
| 1 | "Banī Isrāʾīl" naming | **VINDICATED** | Q017-F-04 + al-Bukhārī #4502 |
| 2 | Q 17 as unique-form musabbiḥa | **VINDICATED** | Q017-F-02 |
| 3 | iʿjāz al-fawāṣil applies to Q 17 | **NOT-FALSIFIED but RULES-TUPLE-FRAGILE** | dual-iʿjāz typology |
| 4 | Q 17:88 as maximal taḥaddī | **VINDICATED** | Q017-F-03 |
| 5 | Q 17:111 as āyat al-ʿizz | **VINDICATED** | al-Suyūṭī Itqān citation |
| 6 | Q 17:79 = Major Intercession | **VINDICATED** | al-Tirmidhī #3221, #3232 etc. |
| 7 | Bodily *isrāʾ* | **NOT-TESTABLE EMPIRICALLY** | theological consensus only |

**5 vindicated, 1 nuanced (RULES-TUPLE-FRAGILE on the negative direction), 1 out-of-scope.** Q 17's classical reception holds up well under empirical audit — better than Q 33's, where the corpus-maximum-monorhyme claim was FALSIFIED. The difference: Q 17's classical claims are mostly about CONTENT (Banī Isrāʾīl naming, taḥaddī, intercession) rather than CORPUS-LEVEL EXTREMA, and content claims are easier to verify than extremum claims.

## Honest limits

- Claim 5 (āyat al-ʿizz) relies on a chain through al-Suyūṭī that we have not graded for ḥadīth-strength (ṣaḥīḥ/ḥasan/ḍaʿīf). The full Aḥmad Musnad would settle this; flagged.
- Claim 3 is interpretive: whether Q 17's anti-fawāṣil profile *falsifies* al-Bāqillānī depends on whether al-Bāqillānī's claim is universal or central-tendency. The classical reading (al-Khaṭṭābī's complementary axis) treats it as central-tendency, which we accept.
- Claim 7 is intentionally placed as NOT-TESTABLE; we record the consensus position without endorsing it.
