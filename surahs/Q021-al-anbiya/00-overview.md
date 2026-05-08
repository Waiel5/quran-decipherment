---
surah: 21
surah_name_ar: الأنبياء
surah_name_translit: al-Anbiyāʾ
surah_name_english: The Prophets
file_type: overview
date_last_updated: 2026-05-07
phase: B+
verdict: SCAFFOLD — full 8-file deep-dive built; 5 pre-registered novel tests run
---

# Q 21 al-Anbiyāʾ — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 21 | canonical |
| Arabic name | الأنبياء | canonical |
| Transliteration | al-Anbiyāʾ | canonical |
| English meaning | "The Prophets" | classical |
| Verse count | 112 | Hafs-Kufan (`quran-text/quran-no-tashkeel.json`) |
| Position in mushaf | 21 | canonical |
| Type | Meccan (middle-Meccan, per al-Suyūṭī) | classical |
| Position in revelation order (al-Suyūṭī) | 73 of 114 | al-Suyūṭī, *al-Itqān*, nawʿ 1 |
| Word count (no-tashkeel) | 1,236 | computed from `quran-no-tashkeel.json` |
| Letter count (non-space, no-tashkeel) | 5,156 | computed |
| Distinct STEM roots (QAC v0.4) | 284 | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| Mean words/verse | 11.04 | computed |
| Range words/verse | 5 – 26 | computed |
| Opening | اقترب للناس حسابهم وهم في غفلة معرضون — "The reckoning has drawn near for mankind, while they turn away in heedlessness." | direct (no muqaṭṭaʿāt) |
| Bismala status | counted as separator only (not as v.1 in Hafs-Kufan numbering for non-Q1 surahs) | canonical |

## 2. Classical names

- **al-Anbiyāʾ** (الأنبياء) — "The Prophets" (canonical name; from the dense prophet-cycle in vv. 48–91).
- No widely-attested alternative name in the major mufassirūn surveyed (al-Ṭabarī, Ibn Kathīr, al-Qurṭubī, al-Zamakhsharī, al-Rāzī).

## 3. Opening formula — direct eschatological warning, NO muqaṭṭaʿāt

Q 21 opens with `iqtaraba li-l-nāsi ḥisābuhum` ("The reckoning has drawn near for mankind"). This is one of the few mid-Meccan surahs that opens **directly with eschatological warning** — no muqaṭṭaʿāt, no *al-ḥamd*, no *sabbaḥa*, no *qul* imperative. The closest opening cognate in the corpus is Q 54:1 *iqtarabati al-sāʿatu* ("the Hour has drawn near") — a direct cross-reference noted by al-Biqāʿī.

## 4. ⭐ Unique structural property — TRUE-ISOLATE (per H-NEW-126)

Q 21 is one of the **5 TRUE-ISOLATE surahs** {Q 16, 21, 22, 23, 25} per H-NEW-126 — surahs that are invisible to all 20 cluster-detection systems used in the project. Q 21 sits inside a contiguous run (Q 21–Q 23) of three consecutive true-isolates, sharing the property with the immediately-following Q 22 al-Ḥajj and Q 23 al-Muʾminūn.

Within this true-isolate cluster, Q 21 is also distinguished as the corpus's **densest pure-prophet-catalog**: 14 distinct canonical prophets named in 41 verses (vv. 48–91), an average of one new prophet every 3 verses. The catalog is structurally unlike any other prophet-cycle in the Quran.

## 5. Length classification

112 verses, 1,236 words, 5,156 letters. Mid-corpus length-class. Position s=21 places Q 21 in the head-zone (pre-Hijra-kink at s=50).

## 6. Rhyme structure

Final-letter distribution across 112 verses:
- **ن (nūn): 106 verses (94.6%)** — extreme dominance
- م (mīm): 6 verses (5.4%)

**Rhyme entropy (Shannon, nats): 0.209** (per H-NEW-750 row; rank 100 / 114 — among the most rhyme-uniform surahs in the corpus). Q 21 is in the bottom-15 for rhyme-variety.

This is consistent with the prophet-catalog form — sustained narrative on -ūn / -īn endings creates monorhyme. Compare Q 12 Yūsuf (also a prophet narrative, also near-monorhyme on ن at 84%).

## 7. Empirical architectural profile

See `01-empirical-profile.md`. Headline:

- **UAS rank**: **16 / 114** ([[h-new-840-unified-architectural-score|H-NEW-840]]; UAS = 1.705)
- **Outlier-strength**: Δ%ile = **−5.71 pp** ("WEAK_ANCHOR" — Q 21 *strengthens* its window when present, not weakens it; not a content-outlier) ([[h-new-590-outlier-spectrum|H-NEW-590]])
- **iʿjāz sig_A**: −1.865 (rank 100 / 114) — VERY LOW, anti-fawāṣil
- **Rhyme entropy**: 0.209 nats (rank 100 / 114 — bottom-15 rhyme-variety)
- **Mean content distance** (FR-roots, no-tashkeel): 1.010
- **Local-cluster cohesion** (5-window centered on Q 21): 1.099
- **Q 20–Q 21 canonical-adjacency cost**: 0.0544 (rank 64 / 113 — modest)
- **Q 21–Q 22 canonical-adjacency cost**: 0.1776 (rank 16 / 113 — top-15 expensive, see [[h-new-720-canonical-adjacency-cost|H-NEW-720]])

**Q 21 is rhyme-uniform, content-anchor (not outlier), iʿjāz-low, with a costly right-boundary to Q 22.** UAS rank 16 / 114 is mid-top because outlier and adjacency-cost compensate for low sig_A.

## 8. Quick content structure

Six narrative blocks, plus eschatological framing:

- **vv. 1–10**: opening warning — *iqtaraba li-l-nāsi*; mocking tone of disbelievers; reminder of destroyed prior peoples.
- **vv. 11–18**: more destroyed-civilization motif; God's wisdom, justice.
- **vv. 19–25**: angelology (vv. 19–20); cosmological *tawḥīd*-argument (v. 22 *law kāna fī-himā āliha illā Allāh la-fasadatā*); the architectural verse Q 21:25 — "no prophet was sent before you except that We revealed: there is no god but Me, so worship Me" — TAWḤĪD-AS-PROPHET-CYCLE-CORE.
- **vv. 26–29**: angels are not God's children; servants honored.
- **vv. 30–33**: ⭐ COSMOLOGICAL CLUSTER — heavens-and-earth-were-joined-then-separated (v. 30); mountains as stabilizers (v. 31); sky as protected canopy (v. 32); sun, moon, day, night each in their orbit (v. 33). Famous classical iʿjāz-passage (al-Bāqillānī, al-Rāzī, al-Qurṭubī).
- **vv. 34–47**: human mortality; weighing-of-deeds; reminder of judgment.
- **vv. 48–91**: ⭐ THE PROPHET CATALOG — 14 named prophets in 41 verses:
  - vv. 48–50: Mūsā + Hārūn → al-Furqān
  - vv. 51–73: Ibrāhīm cycle (idol-shattering, fire trial), Lūṭ, Isḥāq + Yaʿqūb
  - vv. 76–77: Nūḥ
  - vv. 78–82: Dāwūd + Sulaymān (judgment-of-the-flock; the wind, jinn under Sulaymān; the dive of the marine-jinn)
  - vv. 83–84: Ayyūb (the calamity-and-restoration)
  - v. 85–86: Ismāʿīl, Idrīs, Dhū-l-Kifl
  - vv. 87–88: Dhū-l-Nūn (Yūnus) — *lā ilāha illā anta subḥānaka*
  - vv. 89–90: Zakariyyā + Yaḥyā
  - v. 91: Maryam + ʿĪsā (without naming ʿĪsā: "she who guarded her chastity… We made her and her son a sign for the worlds")
- **vv. 92–112**: closing — eschatological signs (vv. 96–97: Yaʾjūj wa-Maʾjūj); inheritance of the earth by the righteous (v. 105 quoting al-Zabūr); Q 21:107 *wa-mā arsalnāka illā raḥmatan li-l-ʿālamīn* (universal-mercy verse); final prayer.

## 9. Connection to true-isolate cluster {Q 16, 21, 22, 23, 25}

Per H-NEW-126, Q 21 is invisible to all 20 cluster-detection systems. Yet it sits inside a 3-consecutive run of true-isolates (Q 21–Q 22–Q 23), and the run extends backward to Q 16 (al-Naḥl) and forward to Q 25 (al-Furqān) with only short non-isolate gaps. This is the densest true-isolate concentration in the mushaf.

The Q 21 + Q 22 adjacency is the project's first jointly-characterized true-isolate adjacent-pair. See `Q021-F-05-true-isolate-adjacency.md` for the joint test.

## 10. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 21 Δ%ile = −5.71 pp, WEAK_ANCHOR.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 21 nūn-monorhyme 94.6%.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 21–Q 22 rank 16 / 113 (2.14% of TSP residual).
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — Q 21 sig_A rank 100 / 114.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 21 UAS rank 16 / 114.
- H-NEW-126 — Q 21 in the 5 TRUE-ISOLATE surahs {Q 16, 21, 22, 23, 25}.
- [[cross-finding-026-iʿjāz-architecture]] — Q 21 fits the *Structural-twin-pair-of-one* sui-generis tail (low sig_A + outlier-anchor + costly right-boundary).

## 11. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md (5 mufassirūn surveyed)
- [x] 04-hadith-corpus.md (3 hadith citations VERIFIED)
- [x] 05-classical-claims-audit.md (5 classical claims audited)
- [x] 06-novel-findings.md (5 pre-registered tests)
- [x] 07-cross-references.md
- [x] JOURNAL.md
