---
surah: 19
surah_name_ar: مريم
surah_name_translit: Maryam
surah_name_english: Mary
file_type: overview
date_last_updated: 2026-04-28
phase: B+
verdict: WAVE-D-LAUNCH — full template + 4 pre-regs scaffolded; specialist runs PENDING
---

# Q 19 Maryam — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 19 | canonical |
| Arabic name | مريم | canonical |
| Transliteration | Maryam | canonical |
| English meaning | "Mary" (mother of ʿĪsā / Jesus) | classical |
| Verse count | **98** | Hafs-Kufan; verified from `quran-text/quran-no-tashkeel.json` |
| Position in mushaf | 19 | canonical |
| Type | **Meccan** (middle-Meccan per Nöldeke; period 4 / Egyptian Standard rev-order 44) | classical (al-Suyūṭī) + `data/revelation-order.csv` |
| Position in revelation order (Egyptian Standard) | **44 of 114** | `data/revelation-order.csv` |
| Position in revelation order (Nöldeke) | **58 of 114** (Middle Meccan) | `data/revelation-order.csv` |
| Word count (no-tashkeel) | **1,012** | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, Arabic graphemes) | **3,976** | computed from `quran-text/quran-no-tashkeel.json` |
| Opening | **كهيعص** (KHYʿṢ) — 5-letter muqaṭṭaʿāt | canonical |

## 2. Classical names

- **Maryam** (مريم) — "Mary," named after Maryam bint ʿImrān, mother of ʿĪsā (Jesus).
- This is the **only surah in the Quran named after a personal female figure**. Q 4 al-Nisāʾ ("the Women") is collective; Q 58 al-Mujādila ("she who contends") is participial. (See `05-classical-claims-audit.md` claim #2.)

## 3. Opening formula — UNIQUE 5-letter muqaṭṭaʿāt

Q 19 opens with **كهيعص** (KHYʿṢ — *kāf hāʾ yāʾ ʿayn ṣād*). This is **the unique 5-letter muqaṭṭaʿāt set in the entire 29-surah muqaṭṭaʿāt-opened corpus**. (Verified against the canonical 29-set: 3 surahs at 1 letter, 10 at 2, 13 at 3, 2 at 4 (ALMS in Q 7 and ALMR in Q 13), and **Q 19 alone at 5**.)

Within [[h-new-97-name-letter-joint|H-NEW-97]] (the surah-name-class × muqaṭṭaʿāt-letter joint distribution test), Q 19's KHYʿṢ row is its own singleton cluster, classified PROPHET_PERSON (because the surah is Maryam-named). Q 19 contributes 1 of the 7 PROPHET_PERSON-named muqaṭṭaʿāt surahs alongside the 4-of-5 ALR cluster (Q 10, 11, 12, 14) and Q 3 Āl ʿImrān (ALM).

## 4. Length classification — mufaṣṣal-ṭiwāl boundary

98 verses, 1,012 words. By al-Zarkashī's mufaṣṣal-tier scheme this is at the boundary between mufaṣṣal-ṭiwāl ("long detailed") and the mid-Meccan storytelling band. By position s = 19, Q 19 sits in the head-mushaf zone, well pre-Hijra-kink (s = 50).

## 5. Rhyme structure — 90.8% alif monorhyme

Final-letter distribution across 98 verses (computed from `quran-text/quran-no-tashkeel.json`, last char of last word per verse):

| Final | Count | Fraction |
|:--:|:--:|:--:|
| **ا** (alif) | **89** | **90.8%** |
| ن (nūn) | 5 | 5.1% |
| م (mīm) | 2 | 2.0% |
| ص (ṣād) | 1 | 1.0% (verse 1, the muqaṭṭaʿāt) |
| ۩ (sajda marker) | 1 | 1.0% (verse 58 — sajda verse marker) |

**Q 19 is in the candidate alif-monorhyme cluster** (cf. Wave-D parallel investigation `Q018-Q048-Q065-Q072-Q076-Q087-Q091-Q092` 100% alif-rhyme cluster; Q 19 falls just outside that 100%-cluster at 90.8%, but as a long-Meccan eschatological surah it is the closest non-100% alif-dominant surah of consequential length). This rhyme uniformity supports the "rhythmic refrain" classical characterisation.

## 6. Empirical architectural profile (headline)

See `01-empirical-profile.md` for full integration. Headline:

- **UAS = 0.6456**, rank **29 / 114** ([[h-new-840-unified-architectural-score|H-NEW-840]])
- **Outlier-strength Δ%ile = +4.60 pp** — WEAK_OUTLIER on window {Q 16–22} ([[h-new-590-outlier-spectrum|H-NEW-590]]). Notably *not* a STRONG / MODERATE outlier despite its narrative density.
- **iʿjāz signature sig_A = −2.0021**, rank **103 / 114** — like Q 12 Yūsuf (rank 109), Q 19 is on the **structural anti-iʿjāz** axis. Continuous-narrative + alif-monorhyme produces low rhyme entropy and high mean content distance, the same signature as Q 12.
- **iʿjāz sig_B = −1.3536**, rank 97 / 114 ([[h-new-750-ijaz-signature|H-NEW-750]])
- **Mean Fisher-Rao distance to corpus = 1.0505** (computed at K=500 stem-roots from QAC) — well above corpus mean 0.9235.
- **Q 18 → Q 19 canonical-adjacency cost: 0.0193** length-units (very cheap; Q 18 al-Kahf shares Meccan-narrative register).
- **Q 19 → Q 20 canonical-adjacency cost: 0.0682** length-units (moderate; Q 20 Ṭāhā is single-letter muqaṭṭaʿāt, Mūsā-narrative — partial register-overlap).

## 7. Quick content structure

Per verse-by-verse audit in `02-content-analysis.md`:

- **vv. 1**: muqaṭṭaʿāt **كهيعص** (5-letter, unique).
- **vv. 2–15**: Zakariyyāʾ–Yaḥyā narrative (annunciation of Yaḥyā to old Zakariyyāʾ; 3-day silence sign).
- **vv. 16–40**: **Maryam narrative** — birth-of-ʿĪsā, palm tree, infant-Jesus speaking from cradle (vv. 30–33). Contains the heart of the surah.
- **vv. 41–50**: **Ibrāhīm–Āzar dialogue** — son confronts father over idolatry; 5× refrain *yā abati*.
- **vv. 51–53**: Mūsā + Hārūn brief mention.
- **vv. 54–55**: Ismāʿīl.
- **vv. 56–57**: Idrīs (one of only 2 Quranic mentions of Idrīs; the other is Q 21:85).
- **vv. 58**: prostration verse (sajda marker) — common-ancestor verse.
- **vv. 59–65**: warning to later generations; *ṣalāh* / *zakāh* / *ṣabr*.
- **vv. 66–98**: Long *yawma yu-* eschatological closing — reckoning, Hell, Paradise, monotheism polemic against "Allah took a son" (vv. 88–95).
- **v. 97**: ⭐ ***fa-innamā yassarnāhu bi-lisānika li-tubashshira bihi al-muttaqīn wa-tunḏira bihi qawman luddā*** — the language-facilitation closing. Twin of Q 44:58 (different terminal clause).
- **v. 98**: closing — destruction of prior generations.

## 8. The Maryam story (vv. 16–40) — Quranic centerpiece

Q 19's Maryam pericope (vv. 16–40) is the **single most extensive narrative treatment of Maryam in the Quran**, even though Maryam is named more times in Q 3 Āl ʿImrān and Q 5 al-Māʾida. The Q 19 pericope contains:

- Maryam's withdrawal to "an eastern place" (v. 16).
- The angelic annunciation of ʿĪsā (vv. 17–21).
- The labor pains and palm-tree miracle (vv. 22–26).
- Her family's accusation and the **infant-ʿĪsā cradle-speech** (vv. 27–33) — *innī ʿabdu llāh ātāniya l-kitāb*.
- The polemical closing about ʿĪsā as "son of Allah" claim (vv. 34–40).

Maryam **token concentration** in Q 19 is, surprisingly, only **3/34 = 8.8%** of corpus mentions (Q 5 leads at 10/34 = 29.4%; Q 3 second at 7/34 = 20.6%). This is **not** the Yūsuf-Q12 pattern of name-saturation (95.2%). Q 19's distinctness lies in the *narrative-pericope concentration* (vv. 16–40), not in name-token frequency. (Pre-registered novel test Q019-F-01 will verify this honestly.)

## 9. Asbāb al-nuzūl: the Najāshī recitation

Classical asbāb-al-nuzūl tradition associates Q 19 with the **second hijra to Abyssinia** (~615 CE) and Jaʿfar b. Abī Ṭālib's recitation of the Maryam pericope before the **Najāshī** (Negus). The tradition is preserved in al-Thaʿlabī's *al-Kashf wa-l-bayān* (raw extract: `data/literature/classical-tafsir/raw/thaclabi-openiti-Q019.txt`, lines around offset 2231 — the Najāshī raised himself from his throne when the ʿĪsā-Maryam passage was recited). Audited in `05-classical-claims-audit.md` claim #4.

## 10. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 19 +4.60 pp WEAK_OUTLIER
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 29/114
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 19 sig_A rank 103/114 (anti-iʿjāz axis like Q 12)
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 18→Q 19 cheap (0.019), Q 19→Q 20 moderate (0.068)
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 19 FR-nearest to Q 43, 21, 46, 41, 36 (ḥawāmīm + prophet-narrative)
- [[h-new-97-name-letter-joint|H-NEW-97]] — KHYʿṢ singleton row, PROPHET_PERSON class
- [[cross-finding-008-muqattaat-book-intro-markers|cross-finding-008]] — Q 19 muqaṭṭaʿāt does NOT immediately followed by *al-kitāb*-reference (cf. Q 12, 13, 14); instead `dhikru raḥmati rabbika ʿabdahu zakariyyā` — a unique muqaṭṭaʿāt-followed-by-*dhikr*-formula pattern
- [[Q003-al-imran/00-overview|Q 3 Āl ʿImrān]] — Maryam-narrative twin
- [[Q012-yusuf/00-overview|Q 12 Yūsuf]] — eponymity comparator (continuous-narrative prophet-named)
- [[Q018-al-kahf/00-overview|Q 18 al-Kahf]] — left-neighbour
- [[Q020-taha/00-overview|Q 20 Ṭāhā]] — right-neighbour
- [[Q021-al-anbiya/00-overview|Q 21 al-Anbiyāʾ]] — multi-prophet-roster comparator (Idrīs co-mention)

## 11. Investigation status (Wave D launch)

- [x] 00-overview.md
- [x] 01-empirical-profile.md (UAS 29/114; FR-nearest Q43/21/46/41/36; outlier WEAK +4.60pp)
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md (≥6 mufassirūn — Tabari, Qurtubi, Razi, Zamakhshari, Ibn Kathir, Suyuti-Durr, Tabarsi, Thaʿlabi, Biqaʿi extracts on disk)
- [x] 04-hadith-corpus.md (9-book survey; Bukhari #3290 Maryam-best-of-women; Najashi cluster 16+ Bukhari; Darimi #2074 Q 19:71 ʿArḍ tradition)
- [x] 05-classical-claims-audit.md (5 claims pre-registered)
- [x] 06-novel-findings.md (4 pre-registered novel tests scaffolded — runs PENDING)
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [ ] 4 pre-reg files locked + SHA256 → `preregs/`
- [ ] 4 scripts → `scripts/` with SHA-verification
- [ ] 4 JSON outputs → `csv/`
