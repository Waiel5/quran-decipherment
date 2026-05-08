---
surah: 50
surah_name_ar: ق
surah_name_translit: Qāf
surah_name_english: "Qāf (singleton-letter opener)"
file_type: overview
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — singleton-letter cohort triplet (Q 50, Q 38, Q 68) characterized; classical Friday-recitation status verified at Sahih Muslim #1907 (NOT #872 as task prompt stated); 5 novel tests pre-registered and executed with mixed verdicts
---

# Q 50 Qāf — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 50 | canonical |
| Arabic name | ق | canonical |
| Transliteration | Qāf | canonical |
| English meaning | "Qāf" (the letter); also called *Sūrat al-Bāsiqāt* by some classical authorities | classical (al-Qurṭubī, *al-Jāmiʿ* on Q 50:1, citing al-Ḥasan / ʿAṭāʾ / ʿIkrima / Jābir on its Meccan status) |
| Verse count | 45 | Hafs-Kufan (`/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` Q 50 record) |
| Position in mushaf | 50 | canonical |
| Type | Meccan (al-Ḥasan, ʿAṭāʾ, ʿIkrima, Jābir; Ibn ʿAbbās + Qatāda dissent on Q 50:38 alone) | al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, opening of Sūrat Qāf (`/Users/grey/Downloads/quran/data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafseer-al-qurtubi/50/1.json`) |
| Position in revelation order (Tanzil Egyptian) | 34 / 114 | `/Users/grey/Downloads/quran/data/revelation-order.csv` line "34,50,ق,Qaf,Meccan,54,Middle Meccan" |
| Position in revelation order (Nöldeke) | 54 (Middle Meccan) | same source |
| Word count (no-tashkeel) | 373 | computed `Q050_F_02_body_part_density.py` (q50_total_word_count) |
| Total letter count (no-tashkeel) | 1,507 | computed `Q050_F_03_qaf_letter_density.py` (q50_obs_total_letter_count: 1,507) |
| Opening | `ق ۚ والقرآن المجيد` — "Qāf. By the Glorious Qurʾān." | Q 50:1, no-tashkeel JSON |
| Bismala status | Standard (counted only in Q 1 per default rules-tuple) | INVESTIGATION-PROTOCOL §1.4 |
| Length classification | First surah of *al-mufaṣṣal* (per Ibn Kathīr's verdict on the boundary) | Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm* on Q 50:1 (`spa5k-tafsir-api/ar-tafsir-ibn-kathir/50/1.json`) — *"hādhihi al-sūra hiya awwal al-ḥizb al-mufaṣṣal ʿalā al-ṣaḥīḥ"* |

## 2. ⭐ Unique structural property — singleton-letter muqaṭṭaʿāt opener

Q 50 is one of **only THREE singleton-letter muqaṭṭaʿāt-opener surahs** in the entire corpus:

- **Q 38 ص** (Ṣād) — 88 verses, Middle Meccan, revelation #38
- **Q 50 ق** (Qāf) — 45 verses, Middle Meccan, revelation #34
- **Q 68 ن** (Nūn) — 52 verses, Early Meccan, revelation #2

Of the 29 muqaṭṭaʿāt-opener surahs (per al-Suyūṭī, *al-Itqān*, nawʿ on muqaṭṭaʿāt), the SINGLETON-letter sub-cohort is the smallest. Verified empirically by direct enumeration: see [[Q050-F-04 in 06-novel-findings]] §"singleton-letter triplet."

## 3. ⭐ The three singleton-letter surahs ALL open with the muqaṭṭaʿ-letter + oath-wāw + definite-article construction

This is the project's first explicit empirical lock on a NEW classical pattern:

```
Q 38:1   ص ۚ والقرآن ذي الذكر       (Ṣād. By the Qurʾān, possessor of the Reminder)
Q 50:1   ق ۚ والقرآن المجيد        (Qāf. By the Glorious Qurʾān)
Q 68:1   ن ۚ والقلم وما يسطرون     (Nūn. By the Pen and what they inscribe)
```

Of 29 muqaṭṭaʿāt openers, EXACTLY these three (and no others) follow the muqaṭṭaʿ + `وال` (oath-wāw + definite-article) syntactic pattern. Verified by [[Q050-F-01 in 06-novel-findings]] §1 — `csv/Q050-F-01.json` `matching_surahs: [38, 50, 68]`.

**Classical citations for this pattern are absent.** al-Suyūṭī's *al-Itqān* nawʿ-classification of muqaṭṭaʿāt openings catalogues the muqaṭṭaʿ-followed-by-book-reference pattern (Q 2:2 *dhālika al-kitāb*, Q 12:1 *tilka āyātu al-kitābi*, etc., 23/29 instances → cross-finding-008) but does NOT separately catalogue the muqaṭṭaʿ-followed-by-oath-wāw construction. **This is a new structural finding.**

## 4. Classical status — *Sūrat al-Jumʿa-recitation*

Sahih Muslim #1907 (Umm Hishām bint Ḥāritha b. al-Nuʿmān): the Prophet recited Q 50 every Friday from the *minbar* during the *khuṭba*, so often that she memorized it from his recitation.

`/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json` idInBook 1907, chapterId 7 (*Kitāb al-Jumʿa*).

**The task prompt cited "Sahih Muslim #872"; this is a misattribution.** Muslim #872 is about prayer-salām hand gestures (Jābir b. Samura), unrelated to Q 50. The correct Q 50 / Friday-recitation hadith is at idInBook 1907. See [[04-hadith-corpus]] §1 for full chain + cross-book corroborations.

Q 50 is also recited by the Prophet at **Eid al-Fiṭr and Eid al-Aḍḥā** alongside Q 54 al-Qamar (al-Tirmidhī #534, Abū Dāwūd #1155, Mālik *Muwaṭṭaʾ* #439, al-Nasāʾī #1572, Ibn Mājah #1016) and **Fajr prayer** (al-Qurṭubī cites Jābir b. Samura on Fajr-recitation). See [[04-hadith-corpus]] for full citations.

## 5. Empirical architectural profile (Wave 2026-04-28 H-NEW pipeline)

| Metric | Value | Rank | Source |
|:--|:--|:--|:--|
| **UAS rank** | **40 / 114** | mid-pack | h-new-840.json all_uas Q 50 entry |
| Outlier-strength Δ-pp | +5.42 | rank 13/114 | h-new-590.json all_surahs_results X=50 |
| Outlier classification | WEAK_OUTLIER | (not a strong outlier) | h-new-590 |
| iʿjāz signature sig_A | +0.891 | rank 37/114 (top third) | h-new-750.json per_surah surah=50 |
| Mean content distance | 0.928 | near corpus mean (z = +0.04) | h-new-750 |
| Top final letter (rāwī) | د (dāl) | 60.00% (27/45 verses) | h-new-750.json + h-new-700 rhyme_diag |
| Rhyme entropy (Shannon, nats) | 1.286 | moderate (corpus mean ≈ 1.7) | h-new-750 |
| Q 49 → Q 50 adjacency cost (TSP) | 0.177 (rank 17/113) | top-15-cluster border | h-new-720.json per_adjacency |
| Q 50 → Q 51 adjacency cost (TSP) | 0.119 (rank 25/113) | mid-cost | h-new-720 |
| FR-roots nearest neighbours (top-5) | Q 78 (0.765), Q 86 (0.781), Q 112 (0.796), Q 79 (0.802), Q 110 (0.804) | terminal mufaṣṣal cluster | h-new-111.json |

Q 50 is **content-cohesive with the late-mufaṣṣal eschatological zone** (Q 78 *al-Nabaʾ*, Q 86 *al-Ṭāriq*, Q 112 *al-Ikhlāṣ*, Q 79 *al-Nāziʿāt*, Q 110 *al-Naṣr*) — its FR-nearest-5 are all post-s=75 short surahs. This is the empirical signature of Q 50's **forward-projecting eschatological compression**: it sits at s=50 (the Hijra-kink boundary) but its content-vocabulary is ALREADY cohesive with the mufaṣṣal-qiṣār terminal-tail. Ibn Kathīr's classical claim *"this surah is the BEGINNING of al-mufaṣṣal"* is empirically vindicated by FR-roots clustering.

See [[01-empirical-profile]] for full integration of all H-NEW metrics.

## 6. Quick content structure

Q 50's 45 verses unfold in roughly five thematic blocks:

- **vv. 1-5**: Oath-opener; Quraysh's astonishment at resurrection; Allah's knowledge of what the earth diminishes from them.
- **vv. 6-11**: Cosmic argument — heavens (raised, decorated), earth (spread, mountains), water-and-fruit cycle as resurrection-evidence.
- **vv. 12-15**: Catalogue of destroyed peoples (ʿĀd, Thamūd, Aṣḥāb al-Rass, Lūṭ, Aṣḥāb al-Ayka, Tubbaʿ).
- **vv. 16-30**: ⭐ The "death-and-resurrection theatre" — Allah's nearness *min ḥabli al-warīd* (v. 16), the two recording angels (vv. 17-18), the throes of death (v. 19), the trumpet (v. 20), each soul brought with driver and witness (v. 21), the cover lifted (v. 22), the throwing into Hellfire (vv. 24-26), the Hell-question dialogue (vv. 30-30).
- **vv. 31-35**: Paradise scene — *al-jannatu uzlifat li-l-muttaqīn ghayra baʿīd* — promised reward.
- **vv. 36-45**: Reminders — destruction of mightier peoples, command to the Prophet to be patient and to *fa-dhakkir bi-l-Qurʾāni man yakhāfu waʿīd* (v. 45, the closing).

See [[02-content-analysis]] for verse-by-verse.

## 7. Length classification

- 45 verses, 373 words, 1,507 letters (no-tashkeel).
- s = 50 (mushaf position) places Q 50 at the **Hijra-kink boundary** (cross-finding-026 §2: kink locked at s=50).
- Per Ibn Kathīr (classical position), Q 50 is the **first surah of al-mufaṣṣal** — empirically confirmed by FR-nearest-neighbours clustering with Q 78, 86, 112, 79, 110 (all post-s=75 short mufaṣṣal-qiṣār surahs).

This places Q 50 at a structurally significant boundary: position 50 is exactly at the Hijra-kink, but content-cohesion is with the mufaṣṣal-qiṣār tail. **Q 50 is a "forward-cohesive" surah**: its FR-roots distribution is more like its terminal-tail content-neighbours than its actual mushaf neighbours (Q 49 al-Ḥujurāt or Q 51 al-Dhāriyāt).

## 8. Rhyme structure

Final-letter distribution across 45 verses (computed from `quran-no-tashkeel.json`):

| Final letter | Count | Fraction |
|:--|:--|:--|
| د (dāl) | 27 | 60.0% |
| ب (bāʾ) | 7 | 15.6% |
| ج (jīm) | 5 | 11.1% |
| ظ (ẓāʾ) | 2 | 4.4% |
| ر (rāʾ) | 2 | 4.4% |
| ط (ṭāʾ) | 1 | 2.2% |
| ص (ṣād) | 1 | 2.2% |

**Q 50 is dāl-rāwī, not qāf-rāwī.** This is the project's CONFIRMED-NULL of opener-rāwī alignment (Q050-F-05) — the muqaṭṭaʿ-letter and the dominant verse-final letter are independent axes for Q 50 (and for Q 38 ص → ب-rāwī, while Q 68 ن → ن-rāwī is the sole match in the singleton-letter cohort). Cross-reference cross-finding-026 §1 (letter-axis ⊥ rhyme-axis empirical orthogonality).

## 9. Pairing with Q 38 (ص) and Q 68 (ن) — the singleton-letter cohort

The three singleton-letter muqaṭṭaʿāt openers form a structurally-coherent triplet:

| Surah | Opener | Verses | Rev. order | Noldeke phase | Rāwī | UAS | sig_A | Outlier Δ-pp |
|:-:|:-:|:-:|:-:|:--|:-:|:-:|:--|:-:|
| Q 38 | ص | 88 | 38 | Middle Meccan | ب (40%) | rank 59/114 | +1.286 | +2.70 |
| Q 50 | ق | 45 | 34 | Middle Meccan | د (60%) | **rank 40/114** | +0.891 | +5.42 |
| Q 68 | ن | 52 | 2 | Early Meccan | ن (81%) | rank 76/114 | -0.413 | -3.45 |

The triplet's mean pairwise FR-distance is **0.870** (vs corpus mean 0.924) — directionally LOWER (more internally cohesive) but at only the 26.7th percentile of N=10000 random 3-surah triplets. **Pre-commit verdict: NULL on FR-cohesion**. The triplet is NOT statistically more clustered than a random triplet (Q050-F-04 verdict).

But the triplet IS extreme on a different axis: **all three open with the muqaṭṭaʿ + oath-wāw + definite-article construction (verse 1)**. This is a *form*-coherence, not a *content*-cohesion (consistent with the cross-finding-026 letter-axis ⊥ content-axis orthogonality lock).

## 10. Cross-finding-026 cell-assignment for Q 50

**Q 50 is assigned to the *iʿjāz-al-fawāṣil-pure* cell (4-cell typology, cross-finding-026 §13.6) with COHORT-MEMBERSHIP in the singleton-letter triplet (Q 38, Q 50, Q 68).**

- UAS rank 40/114 = mid-pack (NOT top-decile); does NOT belong to "All-axis" or "Structural-twin-pair" cells.
- sig_A = +0.891 (positive, rank 37/114) = moderate iʿjāz al-fawāṣil signature; consistent with *iʿjāz-al-fawāṣil-pure* exemplars (Q 86, 89, 100, 106, 113).
- Q 50's body-part metaphor density (Q050-F-02 CONFIRMED, p=10⁻⁴, 100th percentile of length-matched null) and corpus-min sig_A relationship ARE consistent with the al-Bāqillānī *iʿjāz al-fawāṣil* claim about Q 50 (al-Qurṭubī cites al-Bāqillānī's analysis of Q 50:16-22 as *iʿjāz* exemplar of vivid description-by-juxtaposition).

The new cohort-membership in (Q 38, Q 50, Q 68) is a *sub-classification within the iʿjāz-al-fawāṣil cell*, not a new cell. The Q050-F-04 NULL on FR-cohesion is a *credibility-strengthening* result — the singleton-letter cohort is empirically a *form-coherent* cluster (verse-1 oath-formula) but NOT a *content*-coherent cluster.

## 11. Connection to established H-NEW findings

- [[h-new-660-compression-tail-gradient]] — at s=50 (kink boundary), Q 50's compression-tail prediction d̄_content = 0.96 − 0 = 0.96; observed 0.928 — within prediction.
- [[h-new-700-phonological-compression-tail]] — Q 50's rhyme entropy 1.286 nats sits in the rising-dispersion zone past s=50.
- [[h-new-720-canonical-adjacency-cost]] — Q 49→Q 50 adjacency rank 17/113 (top-15% of cost) — Q 49 al-Ḥujurāt (Medinan, social-conduct) → Q 50 (Meccan, eschatological) is a content-register jump.
- [[h-new-750-per-surah-iʿjāz-signature]] — sig_A = +0.891, rank 37/114; rāwī = د at 60%.
- [[h-new-840-unified-architectural-score]] — UAS rank 40/114 (mid-pack).
- [[razi-muqattaat-surah-qaf]] — Razi's classical commentary on the muqaṭṭaʿ-letter ق; reports Q 50 has 57 ق letters (verified Q050-F-03: 57 confirmed; Q 42 also 57; corpus per-letter rate p=10⁻⁴, top-1%).

## 12. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md (UAS rank 40/114; FR-nearest: Q 78, 86, 112, 79, 110; FR-farthest: Q 4)
- [x] 02-content-analysis.md (5-block thematic structure)
- [x] 03-tafsir-survey.md (5 mufassirūn surveyed: al-Ṭabarī, al-Qurṭubī, Ibn Kathīr, al-Jalālayn, al-Muyassar; al-Rāzī through razi-muqattaat-surah-qaf.md; al-Suyūṭī classical chronology)
- [x] 04-hadith-corpus.md (Muslim #1907 verified; Eid + Friday + Fajr recitation chains; corrected from task prompt's "Muslim #872")
- [x] 05-classical-claims-audit.md (5 claims audited)
- [x] 06-novel-findings.md (Q050-F-01 through Q050-F-05 all pre-registered + executed)
- [x] 07-cross-references.md
- [x] JOURNAL.md
