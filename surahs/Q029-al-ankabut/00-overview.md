---
surah: 29
surah_name_ar: العنكبوت
surah_name_translit: al-ʿAnkabūt
surah_name_en: The Spider
file_type: overview
date_last_updated: 2026-05-07
phase: B+
verdict: "69-verse late Meccan الم muqaṭṭāʿat surah; opens with the canonical imtihān theme (a-ḥasiba al-nāsu an yutrakū ... lā yuftanūn); semantically eponymous via Q 29:41 spider-parable; first of the 2 ALM-cluster exceptions to cross-finding-008 muq+book-reference pattern"
---

# Q 29 al-ʿAnkabūt — Overview

| Field | Value |
|:--|:--|
| Surah number | 29 |
| Name (Arabic) | سورة العنكبوت |
| Name (translit) | al-ʿAnkabūt |
| Name (English) | The Spider |
| Verses (Hafs-Kufan) | 69 |
| Mushaf position | 29 |
| Revelation order (Egyptian standard) | 85 |
| Revelation order (Nöldeke) | 81 |
| Period | Late Meccan |
| Opening formula | muqaṭṭaʿāt **الم** (Alif-Lām-Mīm) |
| Bismala status | counted-only-in-Q1 (default rules-tuple) |
| Length class | mufaṣṣal-ṭiwāl (medium-long Meccan; 976 QAC-words) |
| Predominant rāwī (final-letter) | nūn (59/69 verses, 86%) — *al-fāṣila al-nūniyya* |

Sources:
- Verse count: `/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv` (line `29\t69`)
- Revelation order: `/Users/grey/Downloads/quran/data/revelation-order.csv` (rev 85, Nöldeke 81, Late Meccan)
- Word count: QAC v0.4 (976 first-token-positions)
- Rhyme final-letter distribution: H-NEW-750 `top_final_letter='ن', top_final_letter_frac=0.855`

## Position in mushaf and immediate neighbors

- **Q 28 al-Qaṣaṣ** (immediately preceding) — Late Meccan; ṬSM (Ṭā-Sīn-Mīm) muqaṭṭāʿat; DOES open with book-reference (Q 28:2-3 *tilka āyātu al-kitābi al-mubīn*).
- **Q 30 al-Rūm** (immediately following) — Late Meccan; ALM muqaṭṭāʿat; ALSO a cross-finding-008 EXCEPTION (no book-reference).

The Q 29 → Q 30 pair constitutes the only ALM-cluster exception-pair. Across the entire 29 muqaṭṭaʿāt-opened surahs, this is the only consecutive-mushaf-position exception-pair.

## Opening verses (Q 29:1-3)

```
الم
أحسب الناس أن يتركوا أن يقولوا آمنا وهم لا يفتنون
ولقد فتنا الذين من قبلهم ۖ فليعلمن الله الذين صدقوا وليعلمن الكاذبين
```

- v1: الم (the muqaṭṭāʿat opener).
- v2: *a-ḥasiba al-nāsu an yutrakū an yaqūlū āmannā wa-hum lā yuftanūn* — "Do people think that they will be left to say 'we believe' and not be tested?"
- v3: *wa-la-qad fatannā al-ladhīna min qablihim; fa-la-yaʿlamanna Allāhu al-ladhīna ṣadaqū wa-la-yaʿlamanna al-kādhibīn* — "We tested those before them, so Allah will know who is truthful and who is lying."

This is the **canonical imtihān (testing) opener** — a definitive declaration of the divine-testing doctrine, anchored at the verb root `ftn` (*yuftanūn*, *fatannā*).

## Closing verse (Q 29:69)

*wa-l-ladhīna jāhadū fīnā la-nahdiyannahum subulanā wa-inna Allāha la-maʿa al-muḥsinīn*

— "And those who strive in Us, We will surely guide to Our paths; and Allah is with the righteous."

This is the corpus-anchor for the *jihād-fī-Allāh* doctrine. The pairing of Q 29:1-3 (testing) with Q 29:69 (striving + guidance) constitutes the surah's frame-bracket — a classical ring-structure observation (al-Biqāʿī).

## The semantic eponym — Q 29:41

*mathalu al-ladhīna ittakhadhū min dūni Allāhi awliyāʾa ka-mathali al-ʿankabūti ittakhadhat baytan; wa-inna awhana al-buyūti la-baytu al-ʿankabūt; law kānū yaʿlamūn*

— "The likeness of those who take protectors besides Allah is like the spider that takes a house; truly, the frailest of houses is the spider's house — if they only knew."

This is the only mention of *ʿankabūt* (spider) in the entire Quran. The lemma `Eankabuwt` is a corpus-confined-to-one-surah hapax (2 tokens, both at Q 29:41). The verb form *>awohan* (made fragile/weakest) is a strict corpus-hapax (1 token total). See [[Q029-F-01-ankabut-parable-hapax-prereg|Q029-F-01]].

## Major thematic blocks (verse-by-verse summary in `02-content-analysis.md`)

| Block | Verses | Theme |
|:--|:--|:--|
| Prologue / imtihān | 1-13 | Testing doctrine + hypocrites + duty to parents |
| Prophet narratives | 14-40 | Nūḥ + Ibrāhīm + Lūṭ + Madyan + ʿĀd + Thamūd + Qārūn-Firʿawn-Hāmān |
| Spider parable + reflection | 41-44 | Idol-worshippers' protectors are like a spider's web |
| Recitation imperative | 45-49 | Salāh; do-not-debate-People-of-Book; the prophet was illiterate |
| Eschatology + meccan critique | 50-58 | Punishment in time; Allah's earth is wide; every soul tastes death |
| Tawḥīd + concluding striving | 59-69 | Birds + ships + sea-shore tawḥīd inconsistency; jihād-fī-Allāh |

## Key architectural signatures

- UAS: +0.158 (rank 44/114 — moderate-high, NOT a top-15 anchor) — `findings/phase-b-hypotheses/csv/h-new-840.json`
- Outlier-strength Δ%ile: **−7.34** (`WEAK_ANCHOR` — Q 29's removal LOWERS window cohesion; Q 29 is content-cohesive within its 7-window neighborhood)
- iʿjāz signature: `sig_A` = -1.218 (rank 90/114), `sig_B` = -1.017 (rank 80/114) — moderate iʿjāz al-fawāṣil profile
- Rhyme entropy: 0.502 nats (z = -0.484, mid-range)
- Mean content-distance d̄: 0.998 (above corpus mean ≈ 0.96, modestly content-broad)
- Local cohesion: 1.127 (z = -0.533, moderate)

Q 29 is **mid-strength architecturally** — UAS rank 44, modest in every individual axis. Its content-cohesion is moderately tight (WEAK_ANCHOR), opposite to Q 30's WEAK_OUTLIER profile.

## Key classical citations (full audit in `05-classical-claims-audit.md`)

- al-Wāḥidī, *Asbāb al-nuzūl* — Q 29:1-3 occasion-of-revelation (al-Shaʿbī's tradition: revealed about persecuted converts in Mecca who fled to Medina under affliction).
- al-Rāzī, *Mafātīḥ al-ghayb* (Q 29:41) — spider-parable analysis as paradigmatic *mathal* (similitude).
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān* — Q 29 chronology + recurrent-test-theme.
- Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm* — Q 29:1-3 + Q 29:69 doctrinal framing of imtihān + jihād.
- al-Biqāʿī, *Naẓm al-durar* — Q 29 → Q 30 munāsabah (test → vindication).

## Cross-finding pointers

- [[cross-finding-008-muqattaat-book-introduction-marker-synthesis|Cross-finding-008]]: Q 29 is the 1st of 2 ALM-cluster exceptions to muq+book-reference.
- [[h-new-93-q29-q30-subpattern|H-NEW-93]] (parent NULL): Q 29 imtihān-density is HIGH (8.20/k vs Meccan 5.05/k) but does not pass Bonferroni-4 alone.
- [[Q005-al-maida/06-novel-findings|Q005-F-05 chronology-architecture dissociation]]: framework that motivates the present revisit.
- [[Q029-F-01-ankabut-parable-hapax-prereg|Q029-F-01]]: VERIFIED PASS-DIRECTED — 2 corpus-hapax in the spider parable.
- [[Q030-al-rum/Q030-F-01-alm-exception-subcluster-prereg|Q030-F-01]] (joint test housed in Q 30 folder): DIRECTIONAL on both axes; Q 29 carries the imtihān loading.

## Honest summary

Q 29 al-ʿAnkabūt is a 69-verse Late Meccan ALM-opened surah whose opener is the canonical imtihān (testing) doctrine and whose semantic eponym is the spider-parable at v 41. Architecturally it is mid-strength (UAS rank 44), with content-cohesive WEAK_ANCHOR profile. Like Q 30, it lacks the cross-finding-008 book-reference pattern in v 1-3. Its eponymous lemma *ʿankabūt* is a corpus-confined-to-one-surah hapax — empirically supporting al-Rāzī's claim that the parable is a uniquely-marked rhetorical device. Pre-registered tests in `06-novel-findings.md` examine the lexical-uniqueness signature; the joint Q 29 + Q 30 sub-cluster test is housed in `Q030-al-rum/Q030-F-01`.
