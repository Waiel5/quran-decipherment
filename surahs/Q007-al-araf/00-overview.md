---
surah: 7
surah_name_ar: الأعراف
surah_name_translit: al-Aʿrāf
surah_name_english: "The Heights / The Ramparts"
file_type: overview
date_last_updated: 2026-05-07
phase: B+
verdict: SCAFFOLD-COMPLETE — 4-file empirical anchors + 5 pre-registered novel tests run; 1 CONFIRMED, 1 DIRECTIONAL, 3 NULL
---

# Q 7 al-Aʿrāf — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 7 | canonical |
| Arabic name | الأعراف | canonical |
| Transliteration | al-Aʿrāf | canonical |
| English meaning | "The Heights" / "The Ramparts" | classical (al-Ṭabarī on 7:46) |
| Verse count | 206 | Hafs-Kufan |
| Position in mushaf | 7 | canonical |
| Type | Late Meccan | per al-Suyūṭī chronology + Tanzil + Nöldeke |
| Position in revelation order (al-Suyūṭī) | 39 of 114 | `data/revelation-order.csv` |
| Nöldeke order / phase | 87 / Late Meccan | `data/revelation-order.csv` |
| Word count (no-tashkeel) | 3,551 | computed (this run) |
| Letter count (no-tashkeel, no-pause) | 14,443 | computed (this run) |
| Unique-root count (QAC) | 477 | computed (this run, `data/morphology/root-index.json`) |
| Length classification | al-sabʿ al-ṭiwāl (the 7 long surahs) | al-Tirmidhī Ḥadīth #3170 (Sunan) [VERIFIED — see §4] |
| Opening formula | المص (alif-lām-mīm-ṣād muqaṭṭaʿāt) — corpus-unique 4-letter set | `quran-text/quran-no-tashkeel.json` Q 7:1 |
| Bismala status | preceded by basmala (counted only in Q 1 per rules-tuple) | rules-tuple default |

## 2. Classical names

- **al-Aʿrāf** (الأعراف) — "The Heights / Ramparts," from Q 7:46–48 (the eponymic eschatological location).
- **al-Mīqāt** — informal classical alias (al-Suyūṭī *al-Itqān*, nawʿ 17, on alternate surah-naming) referencing the Mūsā-mīqāt of Q 7:142–144.

## 3. Opening formula — المص corpus-unique 4-letter muqaṭṭaʿ

Q 7 opens with **المص** (alif-lām-mīm-ṣād), a **4-letter muqaṭṭaʿ that appears NOWHERE ELSE in the corpus**. The 4-letter muqaṭṭaʿāt are limited to Q 7 (المص) and Q 13 (المر = alif-lām-mīm-rāʾ). Q 13's **المر** also has the alif-lām-mīm prefix; Q 7's adds **ṣād** instead of **rāʾ**.

This makes Q 7 a **liminal letter-family member**:
- Shares **alif-lām-mīm prefix** with the ALM cluster (Q 2, 3, 29, 30, 31, 32).
- The **ṣād** terminal is shared with Q 38 (alone, as ص), Q 19 (as part of كهيعص).
- No other 4-letter combination matches.

Empirical position-test (Q007-F-02 below): Q 7 ranks **2/114** on the combined ALM-centroid + ALR-centroid Fisher-Rao proximity (only Q 45 ranks lower). Q 7 is closer to the **ALR cluster centroid** (d=0.841) than to the **ALM cluster centroid** (d=0.908), with gap = 0.067 (within the pre-committed equidistance criterion of 0.10). This is **DIRECTIONAL evidence** for Q 7 as a content-axis liminal letter-family member, despite the corpus-wide muqaṭṭaʿ-content NULL streak (H-NEW-600/610/Q026-F-02/F-04).

## 4. Length and classical sabʿ al-ṭiwāl status

Q 7 is the **6th of the seven long surahs (al-sabʿ al-ṭiwāl)** per the canonical ordering Q 2 → Q 3 → Q 4 → Q 5 → Q 6 → Q 7 → (Q 8+9 conjoined) per al-Tirmidhī Ḥadīth #3170 (the ʿUthmān b. ʿAffān tradition, on Anfāl-Bara'ah-jointness):

> "What was your reasoning with Al-Anfāl — while it is from the Mathānī (Surah with less than one-hundred Āyāt), and Bara'ah while it is from the Mi'īn (Surah with about one-hundred Āyāt), then you put them together... and you placed them with the **seven long (Surahs)**?" [Sunan al-Tirmidhī #3170]

Status of al-sabʿ al-ṭiwāl is also at al-Nasāʾī Sunan #917, #918 ("seven oft-recited; the seven long ones"). Q 7's length (206 verses, 3,551 words) is consistent with this classification — 4th-longest by verse-count among the ṭiwāl, after Q 2 (286), Q 4 (176/wait this is shorter), Q 26 etc; among ṭiwāl by verse-count it ranks: Q 2 (286), Q 4 (176), Q 7 (206), Q 3 (200), Q 5 (120), Q 6 (165), Q 8+9 (75+129=204). Q 7 is among the largest.

## 5. Rhyme structure — extreme monorhyme on -ūn

Final-letter distribution across 206 verses (computed this run, `quran-text/quran-no-tashkeel.json`):

| Letter | Count | % |
|:-:|:-:|:-:|
| ن (nūn) | 192 | 93.2% |
| م (mīm) | 10 | 4.9% |
| ل (lām) | 2 | 1.0% |
| ص (ṣād) | 1 (verse 1, the muqaṭṭaʿ) | 0.5% |
| ۩ (sajda marker on v 206) | 1 | 0.5% |

**Rhyme entropy (Shannon, nats): 0.279**. This is **extreme monorhyme**, the lowest possible practical Shannon entropy for a 206-verse surah. By H-NEW-750 metrics, Q 7's rhyme-axis sig_A = **−2.033** (rank 104/114, anti-iʿjāz-al-fawāṣil — the LOW end). Q 7 belongs to the structural-iʿjāz-by-OUTLIER architecture, NOT iʿjāz-by-rhyme-variety.

## 6. ⭐ Unique structural property — the 7-prophet narrative cycle + المص + Aʿrāf-third-place

Q 7 contains **THREE corpus-unique structural properties**:

1. **المص**: corpus-unique 4-letter muqaṭṭaʿ (no other surah has this combination).
2. **The 7-prophet sequential narrative**: Adam → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb → Mūsā in mushaf-order is the LONGEST contiguous prophet-narrative chain in the corpus (covering vv 11–137, ~110 verses, 53% of the surah).
3. **al-Aʿrāf as third-place**: The orthographic token `الأعراف` is **corpus-hapax (2× both in Q 7, vv 46 & 48)** — see Q007-F-03 CONFIRMED. The semantic-eschatological role ("men on the ramparts who recognize people of Garden and Fire by signs, neither in nor of either") is unique to Q 7's eschatological geography.

The 7-prophet ordering's significance is locked at H-NEW-940 (CONFIRMED Bonferroni-4 H2a: pre-Abrahamic chain Ādam→Nūḥ→Hūd→Ṣāliḥ τ=1.0 across qualifying surahs, p=0.001). Q007-F-05 EXTENDS this by testing whether Q 7's full-7-element ordering is structurally PRIMARY across Q 11, Q 26, Q 21. The verdict is **NULL on the H1 framing** but **POSITIVE on the descriptive observation**: Q 7's Mūsā-LAST placement is structurally distinct from Q 11's Mūsā-prologue and Q 26's Mūsā-prologue (a strong inter-surah signature, not a primacy-confirmation).

## 7. Empirical architectural profile (snapshot)

See `01-empirical-profile.md` for the full integration. Headline:

| Metric | Value | Source |
|:--|:--|:--|
| **UAS rank** | **11/114** | h-new-840.json (computed) |
| Outlier-strength (Δ%ile) | −3.78pp (NULL) | h-new-590.json |
| iʿjāz signature sig_A | −2.033 (rank 104/114, low) | h-new-750.json |
| iʿjāz signature sig_B | −1.474 (rank 101/114, low) | h-new-750.json |
| Mean content distance | 1.039 | h-new-750.json |
| Q6-Q7 canonical adjacency cost | 0.000 (zero residual — content twin) | h-new-720.json |
| Q7-Q8 canonical adjacency cost | 0.212 (top-10 most-expensive) | h-new-720.json |
| FR top-5 nearest | Q 6, Q 10, Q 28, Q 11, Q 40 | h-new-111.json (computed) |
| FR top-5 farthest | Q 92, Q 97, Q 88, Q 80, **Q 55** | h-new-111.json (computed) |

**Architectural type**: **structural-iʿjāz by OUTLIER + ADJACENCY-COST**, NOT iʿjāz-al-fawāṣil. Q 7's UAS rank 11 is driven by the Q7→Q8 transition cost (top-10) and a small outlier component, NOT by rhyme-variety. The extreme monorhyme on -ūn (rhyme entropy 0.279) anchors this as an **anti-iʿjāz-al-fawāṣil profile despite high overall structural significance**.

## 8. Quick content structure

| Block | Verses | Theme |
|:---|:---|:---|
| 1. Prologue | 1–9 | المص opening, kitāb-anzila, eschatology of mizān (scales) |
| 2. Adam–Iblīs | 10–25 | Creation, prostration, refusal, garden-fall |
| 3. Banī Ādam admonitions | 26–36 | "yā banī Ādam" 4× refrain; covering, beauty, prayer, mosque |
| 4. Eschatology + **al-Aʿrāf** | 37–53 | Hellfire, Paradise, **the Heights** (vv 46–49) |
| 5. Cosmological hymn | 54–58 | Allah created the heavens and earth in 6 days |
| 6. Nūḥ cycle | 59–64 | "laqad arsalnā Nūḥan" |
| 7. Hūd cycle (ʿĀd) | 65–72 | "wa-ilā ʿĀd akhāhum Hūdan" |
| 8. Ṣāliḥ cycle (Thamūd) | 73–79 | "wa-ilā Thamūd akhāhum Ṣāliḥan" + nāqa |
| 9. Lūṭ cycle | 80–84 | "wa-Lūṭan idh qāla" |
| 10. Shuʿayb cycle (Madyan) | 85–93 | "wa-ilā Madyan akhāhum Shuʿayban" |
| 11. Theological coda on the destruction-cycles | 94–102 | "tilka al-qurā naquṣṣu ʿalayka" |
| 12. Mūsā vs Pharaoh | 103–137 | Magicians, plagues, drowning |
| 13. Bani Israel + Mīqāt + Calf | 138–171 | Tablets, calf, Sabbath people |
| 14. Mīthāq al-aṣlī (covenant) | 172–174 | Q 7:172 — primordial covenant |
| 15. Parable of the apostate-scholar | 175–177 | "wa-tlu ʿalayhim nabaʾ alladhī ātaynāhu āyātinā" |
| 16. Wisdom + asmāʾ ḥusnā | 178–181 | "wa-li-Llāhi al-asmāʾu al-ḥusnā" (v 180) |
| 17. Eschatology + closing | 182–206 | Final exhortations; v 204 "wa-idhā quriʾa al-Qurʾān fa-stamiʿū" + v 206 sajda |

## 9. Connection to wider findings

- **H-NEW-940** (prophet-cycle order conservation): Q 7 is one of 8 narrative-rich surahs analyzed; Q 7's pre-Abrahamic chain Adam-Nūḥ-Hūd-Ṣāliḥ has τ=1.0 vs canonical (CONFIRMED H2a, Bonferroni-4, p=0.001).
- **H-NEW-90** (parent finding referenced in task brief): Q 7 corpus-MAX prophet-cycle parallelism z=+5.25 (parent-finding metric). **Q007-F-01 attempted independent replication with a different operationalization (4-feature vector / Hamming) and got NULL** — see honest-limits §11 of `06-novel-findings.md` for analysis. The H-NEW-90 finding does not survive this specific operationalization; it may survive others.
- **Q026-F-01** (CONFIRMED): the refrain-cycle 7-prophet structure of Q 26 (Mūsā→Ibrāhīm→Nūḥ→Hūd→Ṣāliḥ→Lūṭ→Shuʿayb). Q 7 has a similar 7-prophet block but **without** the corpus-unique paired-refrain marker; instead, Q 7 uses a different lattice — the `wa-ilā [tribe] akhāhum [prophet]` formula (3× in Q 7, 3× in Q 11, 1× in Q 29; total corpus = 7 occurrences). The Q 7 vs Q 26 contrast: Q 26 carves prophet-cycles by REFRAIN; Q 7 carves them by ʾakhāhum-LATTICE.
- **Cross-finding (NEW)**: The Q 7 ↔ Q 6 canonical-adjacency cost is **0.000** — a perfectly residual-free transition in mushaf order (h-new-720). Q 7 is FR-nearest-neighbor to Q 6 (FR=0.721); the Q6-Q7 transition is the single cheapest non-trivial adjacency in the mushaf-graph. This anchors al-Biqāʿī *Naẓm al-Durar*'s Q 6 → Q 7 → Q 8 munāsabah-triad reading at quantitative law-strength.

## 10. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 7 outlier NULL (delta_pct=−3.78pp, p=0.598).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 7 rhyme entropy 0.279 (extreme monorhyme).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q6-Q7=0.000 (cheapest); Q7-Q8=0.212 (top-10 expensive).
- [[h-new-750|H-NEW-750]] — Q 7 sig_A=−2.033 (rank 104, anti-fawāṣil).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 7 UAS rank **11/114**.
- [[h-new-940-prophet-order-conservation|H-NEW-940]] — Q 7 contributes Adam-Nūḥ-Hūd-Ṣāliḥ τ=1.0 (CONFIRMED).
- [[h-new-90-kahf-narrative-structure|H-NEW-90]] — parent finding for prophet-cycle parallelism z=+5.25 (Q007-F-01 attempts independent replication; gets NULL on this operationalization).
- [[Q006-al-anam|Q 6 al-Anʿām]] — content-twin (FR=0.721, lowest non-mushaf-edge).
- [[Q011-hud|Q 11 Hūd]] — `wa-ilā [tribe] akhāhum` lattice sister.
- [[Q026-al-shuara|Q 26 al-Shuʿarāʾ]] — 7-prophet-cycle sister (different lattice: refrain-cycle).
- [[cross-finding-008|cross-finding-008]] — muqaṭṭaʿāt + book-reference; Q 7:1–2 fits the pattern (المص + kitābun anzila ilayka).

## 11. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md (5 pre-registered tests run: 1 CONFIRMED, 1 DIRECTIONAL, 3 NULL)
- [x] 07-cross-references.md
- [x] JOURNAL.md
