---
surah: 31
surah_name_ar: لقمان
surah_name_translit: Luqmān
surah_name_english: "Luqmān"
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD — empirical profile complete; full investigation written 2026-05-09
specialist: Q031-luqman-specialist
---

# Q 31 Luqmān — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 31 | canonical |
| Arabic name | لقمان | named after the eponymous wisdom-figure first appearing at v.12 |
| Transliteration | Luqmān | canonical |
| English meaning | "Luqmān" — proper name; a non-prophet sage | classical |
| Verse count | 34 | Hafs-Kūfan (`data/hafs-verse-counts.tsv`) |
| Position in mushaf | 31 | canonical |
| Type | Late-Meccan | al-Suyūṭī, *al-Itqān*, nawʿ 1 |
| Position in revelation order | 57 of 114 | Tanzil Egyptian Standard, `data/revelation-order.csv` |
| Nöldeke order | 82 | Wikipedia Nöldeke leg, `data/revelation-order.csv` |
| Nöldeke phase | Late Meccan | as above |
| Word tokens (no-tashkeel, orthographic-token) | 551 | computed from `quran-text/quran-no-tashkeel.json` (basmala-counted-only-in-Q1) |
| Letter graphemes (no-tashkeel, no spaces) | 2,172 | computed |
| Avg verse length (graphemes) | 63.9 | computed |
| Avg verse length (words) | 16.2 | computed |
| Top verse-final letter (rāwī) | ر (rāʾ) | 47.1% of 34 verses (`h-new-750.json`) |
| Rhyme entropy (nats) | 1.291 | HIGH — non-monorhyme; multi-letter rhyme palette (z = +0.94) |
| Mean content distance (FR) | 0.948 | very near corpus mean 0.924 (`h-new-750.json`) |
| Local cohesion | 1.060 | slightly low (`h-new-750.json`) |
| iʿjāz sig_A (al-Bāqillānī fawāṣil axis) | +0.698 (rank 43/114) | mid-positive |
| iʿjāz sig_B (al-Sakkākī iqāʿ axis) | +0.319 (rank 49/114) | mid-positive |
| UAS | −1.171 (rank 80/114) | LOW unified architectural significance |
| Outlier-strength Δ%ile | +2.14 pp | WEAK_OUTLIER (window {Q 28-34}); p_greater = 0.31 |
| Q 30 → Q 31 cost | δ = +0.0376 (fraction_residual 0.45%) | low — ALM neighbor smooth (`h-new-720.json`) |
| Q 31 → Q 32 cost | δ = +0.1005 (fraction_residual 1.21%) | modest |
| Opening | الم — *tilka āyātu al-kitābi al-ḥakīm — hudan wa-raḥmatan li-l-muḥsinīn* | book-introduction-formula opener (cross-finding-008 cohort) |

## 2. Classical name and the eponymous sage

The surah is named **Luqmān** after the wisdom-figure introduced at v.12 (*wa-laqad ātaynā Luqmāna al-ḥikma*). The Arabic name is rendered as a non-Arab proper noun; the surah-name is one of a small handful named after a **non-prophet** human figure — beside the prophet-named surahs (Yūnus, Hūd, Yūsuf, Ibrāhīm, Muḥammad, Nūḥ, Maryam — a notable case as a woman) and other titles named for objects/concepts.

Classical exegesis disputes whether Luqmān himself was a prophet (*nabī*) or a sage (*ḥakīm*) but agrees the surah crystallizes his moral discourse. Majority Sunni view (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr): Luqmān is a *ḥakīm* (sage), not a prophet — Allah granted him *al-ḥikma* (wisdom) but did not appoint him as messenger. Minority report (preserved by al-Ṭabarī as one of the catalogued opinions): Luqmān was a prophet. The Quranic text grants him ḥikma, paternal didacticism, and a personal voice — but does not call him *nabī* or *rasūl*. This is the classical "Luqmān-as-prophet?" debate; see §3 in `05-classical-claims-audit.md` for the empirical adjudication.

The historical referent: classical sources (al-Ṭabarī ad loc.; Ibn Kathīr) record traditions identifying Luqmān as a Nubian or Ethiopian slave, an unusually long-lived sage of Banū Isrāʾīl epoch, sometimes synonymized with the figure Aesop in cross-cultural treatments (Ibn Kathīr explicitly disclaims the Aesop equation). The Quranic narrative does not anchor him to a particular tribe or epoch — he is presented purely as *ḥakīm* (a wise one).

## 3. Opening formula — ALM + book-introduction couplet

Q 31:1-3 (no-tashkeel):

| v | Text | Gloss |
|:-:|:--|:--|
| 1 | الم | *Alif Lām Mīm* (muqaṭṭaʿāt) |
| 2 | تلك آيات الكتاب الحكيم | *These are the verses of the Wise Book* |
| 3 | هدى ورحمة للمحسنين | *A guidance and a mercy for the doers of good* |

The opening is the **book-introduction-formula cohort** of cross-finding-008 (CONFIRMED at p = 3 × 10⁻¹² for the broader 24/29 muqaṭṭaʿāt-→book-reference enrichment; H-NEW-53/56/57). Q 31 belongs to the inner ALM-book-reference triad **{Q 2, Q 3, Q 31}** which open with the explicit *tilka āyātu al-kitāb* / *dhālika l-kitāb* couplet (per Q032-F-03, the **other three ALM surahs** {Q 29, Q 30, Q 32} lack this exact couplet at the opener and are the "ALM-exception" subset).

Distinctive: Q 31:2 says *al-kitāb al-ḥakīm* (the Wise Book) — the adjectival *ḥakīm* anticipates the surah's eponymous sage Luqmān (v.12 *al-ḥikma*). The classical *iʿjāz* tradition (al-Bāqillānī, al-Suyūṭī *Itqān* nawʿ 67-68 on naming) reads this as the classic *al-tasmiyya* — "the surah is named after what its principal pericope concerns" — *al-kitāb al-ḥakīm* introduces Luqmān-the-sage who delivers wisdom. al-Biqāʿī, *Naẓm al-Durar*, makes this exact connection: ḥikma in the opening adjective → ḥikma in the eponymous figure → didactic pericope vv.12-19.

## 4. The Luqmān pericope (vv.12-19) — the structural core

Q 31's defining structural feature is the **8-verse Luqmān-to-his-son didactic pericope** at vv.12-19. This is one of the few corpus locations where a non-prophet character delivers a sustained moral discourse. The classical didactic-corpus reads it as 8 *waṣāyā* (commendations, "advice-aphorisms"):

| v | Topic |
|:-:|:--|
| 12 | Allah granted Luqmān *al-ḥikma* — frame: *uškur li-llāh* (be thankful) |
| 13 | Luqmān's address to his son: *yā bunayya, lā tushrik bi-llāh* — DO NOT associate-partners |
| 14 | (parenthetical-Quranic frame): Allah's commendation of dutifulness toward parents (*biwālidayhi*) |
| 15 | (parenthetical): conditional disobedience to parents only when they command shirk |
| 16 | *yā bunayya* — even a mustard-seed weight in a rock or in heavens-and-earth is brought-forth by Allah |
| 17 | *yā bunayya* — establish ṣalāh, command good, forbid evil, endure with patience |
| 18 | DO NOT turn the cheek away in pride or walk in arrogance (*marḥā*) |
| 19 | walk modestly (*waqṣid*), lower the voice (*waghḍuḍ min ṣawtika*); the most disagreeable voice is the donkey's |

The 8 verses divide into a **frame–address triad** (vv.12–13: divine grant of ḥikma + Luqmān's first prohibition: *lā tushrik*) — **parenthetical Quranic interpolation** (vv.14–15: parental-duty couplet, in the divine voice not Luqmān's) — **direct didactic 4-piece** (vv.16–19: four *yā bunayya* / imperative-style pieces). The interpolation at vv.14–15 is one of the corpus's most striking *iltifāt*-class voice-shifts: the narrator pauses Luqmān's speech, intercalates a divine-voice commendation of parental duty, then resumes in v.16 with another *yā bunayya*. al-Suyūṭī (*Itqān*, nawʿ 35 on *al-iltifāt*) and al-Zarkashī (*Burhān*, nawʿ 53 on *iltifāt*) both note this pericope as a textbook case of voice-shift.

**Empirical observation**: the vocative *yā bunayya* (singular father-to-son) appears **9 times in the corpus** (filtered to exclude *banī isrāʾīl* and *banī ādam* plural-vocatives), distributed across **5 surahs**:

| Surah | Occurrences | Context |
|:--|:-:|:--|
| Q 2:132 | 1 | Yaʿqūb to his sons (collective) |
| Q 11:42 | 1 | Nūḥ calling his disbeliever-son to board the ark |
| Q 12 | 3 (vv.5, 67, 87) | Yaʿqūb to Yūsuf (5); Yaʿqūb to all his sons (67); Yaʿqūb to his sons (87) |
| **Q 31** | **3** (vv.13, 16, 17) | **Luqmān to his son (didactic pericope)** |
| Q 37:102 | 1 | Ibrāhīm to Ismāʿīl (sacrifice-vision) |

Q 31 holds **3/9 = 33%** of the corpus's pure-singular *yā bunayya* vocatives, **tied with Q 12** (the Yūsuf-cycle). Q 31 is **not** a corpus-monopoly on this construction — but is **co-equal** with Q 12 as the densest didactic-vocative concentration. In 8 verses Q 31 packs 3 occurrences (density 0.375/verse); Q 12 spreads 3 across 111 verses (density 0.027/verse). On per-verse density, Q 31's Luqmān-pericope is **~14× denser** in *yā bunayya* than Q 12. This is tested formally in `06-novel-findings.md` Q031-F-01.

## 5. Macro-structure (4 thematic blocks)

Q 31 organizes into 4 macro-blocks (per al-Biqāʿī *Naẓm* + classical block-reading):

| Block | vv. | Length | Theme |
|:--|:-:|:-:|:--|
| **A** | **1-11** | **11** | **ALM frame + scripture self-reference + contrast believer/scoffer** |
| **B** | **12-19** | **8** | **THE LUQMĀN PERICOPE — 8 *waṣāyā* of a non-prophet sage** |
| **C** | **20-30** | **11** | **Cosmological signs (sun/moon/sea/ink) + rebuke of obstinate rejection** |
| **D** | **31-34** | **4** | **Mortality + the five *mafātīḥ al-ghayb* (last verse: knowledge of the Hour, rain, womb-contents, tomorrow's deeds, place of death)** |

Block-D's closing v.34 is a corpus-key listing of the **five keys of the unseen** (*mafātīḥ al-ghayb*), which classical theology (al-Bukhārī, *Tawḥīd*; al-Ṭabarī ad loc.) treats as the irreducible fivefold limit on human knowledge. The verse ends *inna llāha ʿalīmun khabīr* — closing with two divine epithets (*ʿalīm* + *khabīr*) that reinforce the unseen-knowledge frame.

al-Biqāʿī's *munāsaba* reading of Q 31's block structure: **Block A** sets the wisdom-of-the-Book frame; **Block B** instantiates wisdom in a human-paradigm case (Luqmān); **Block C** gives wisdom-bearing cosmic-signs (the sun, moon, sea-ink-trees-pens metaphor at v.27); **Block D** caps the surah on the limits of human wisdom against divine omniscience. The 4-block arc moves from divine wisdom-gift → human exemplar → cosmic-witness → eschatological-limit.

## 6. The cosmic-signs block (vv.20-30) — *al-mawjāt* and the ink-of-the-sea

vv.27-28 contain one of the corpus's most celebrated rhetorical figures:

> *wa-law anna mā fī al-arḍi min shajaratin aqlāmun wa-l-baḥru yamudduhu min baʿdihi sabʿatu abḥurin mā nafidat kalimātu llāhi…*
>
> "If all the trees on earth were pens, and the sea, with seven seas after it (yet to be added), [were ink], the words of Allah would not be exhausted…"

Classical *iʿjāz al-tashbīh* literature (al-Jurjānī, *Asrār al-balāgha*; al-Zamakhsharī, *Kashshāf*) cite this as a paradigmatic *tashbīh murakkab* (compound simile) of the divine word's inexhaustibility. The verse's twin (using identical metaphor) appears at **Q 18:109** (*qul law kāna al-baḥru midādan li-kalimāti rabbī…*). Q 31:27 is the **expanded** version (adding "trees as pens" and "seven additional seas"). This is one of the corpus's MUTASHĀBIH-pair anchors (verse-twin network H-NEW-66 — see `07-cross-references.md`).

vv.20-26 stage the rebuke-of-obstinate-rejection block: those who dispute about Allah without knowledge, those who follow what they found their fathers upon — paralleling Q 2:170, Q 5:104, Q 7:28 (the *vājidhīn* parental-imitation anchor pattern, classical *muḥkam-mutashābih* doctrine).

## 7. Mortality + last knowledge — vv.33-34 closing

The final two verses are eschatologically decisive:

- **v.33**: address to mankind (*yā ayyuhā al-nās*) — fear God, fear the Day when no parent suffices for child, no child for parent — the *deceiver* deceives you by means of God.
- **v.34**: **the five mafātīḥ al-ghayb**:
  1. knowledge of the **Hour** (al-sāʿa)
  2. **rain-knowledge** (yunazzilu al-ghayth)
  3. **womb-contents** (mā fī al-arḥām)
  4. **tomorrow's deeds** (mā tadrī nafsun mādhā taksibu ghadan)
  5. **place of death** (bi-ayyi arḍin tamūt)

This v.34 is the foundational text for the classical *mafātīḥ al-ghayb* doctrine. al-Bukhārī (*Tawḥīd* 4778) records the ḥadīth of Jibrīl asking the Prophet about the Hour — the Prophet recites Q 31:34 in response. al-Ṭabarī, al-Rāzī (*Mafātīḥ al-ghayb*, the very title of his tafsir is taken from this verse), al-Qurṭubī all treat v.34 as the locus classicus of unseen-limits theology. al-Biqāʿī's munāsaba reading at the Q 31 → Q 32 transition: Q 31 ends on the limits of human knowledge, Q 32 opens (ALM + *tanzīl al-kitāb*) on the divine response — the Book is the antidote to the ghayb-gap. (See Q 32 specialist `00-overview-comprehensive.md` §4.3.)

## 8. The 6 ALM-cluster surahs and Q 31's position

Q 31 is one of **6 ALM-opened surahs** in the corpus: {Q 2, Q 3, Q 29, Q 30, Q 31, Q 32}. By revelation chronology (Tanzil/Nöldeke), these split into:

| Surah | Mushaf | Tanzil (rev order) | Nöldeke order | Phase |
|:--|:-:|:-:|:-:|:--|
| Q 29 al-ʿAnkabūt | 29 | 85 | 81 | Late Meccan |
| Q 30 al-Rūm | 30 | 84 | 74 | Late Meccan |
| **Q 31 Luqmān** | **31** | **57** | **82** | **Late Meccan** |
| Q 32 al-Sajda | 32 | 75 | 70 | Late Meccan |
| Q 2 al-Baqara | 2 | 87 | 91 | Medinan |
| Q 3 Āl ʿImrān | 3 | 89 | 97 | Medinan |

**All 4 mid-mushaf ALM surahs (Q 29, 30, 31, 32) are Late Meccan; the 2 long ALM surahs (Q 2, 3) are Medinan.** Within the 4 Late-Meccan ALMs, Q 31 sits at Tanzil-order 57 (earliest) and Nöldeke order 82 (latest). The Tanzil/Nöldeke disagreement on Q 31's exact rank is mild but visible — see Q031-F-04 in `06-novel-findings.md` for the stratification analysis.

In FR (Fisher-Rao root-distribution) space (`h-new-111.json`), the ALM-cluster pairwise distances are:

| Pair | FR | Note |
|:--|:--:|:--|
| (Q 2, Q 3) | 0.6309 | tightest pair (long Medinan twins) |
| (Q 2, Q 29) | 0.8489 | |
| (Q 3, Q 29) | 0.8420 | |
| (Q 29, Q 30) | 0.9153 | |
| (Q 29, Q 31) | 0.8963 | |
| (Q 29, Q 32) | 0.9383 | |
| (Q 30, Q 31) | 0.9089 | mushaf-adjacent |
| (Q 30, Q 32) | 0.9272 | |
| **(Q 31, Q 32)** | **0.9095** | **mushaf-adjacent** |
| (Q 2, Q 30) | 0.9732 | |
| (Q 2, Q 31) | 0.9770 | |
| (Q 3, Q 30) | 0.9841 | |
| (Q 3, Q 31) | 0.9961 | |
| (Q 2, Q 32) | 1.0515 | |
| (Q 3, Q 32) | 1.0860 | |

Mean ALM-cluster pairwise FR = **0.9257** (essentially indistinguishable from the corpus FR-mean 0.9234 — i.e. **the ALM-cluster as a whole is NOT FR-cohesive at the root-distribution level**, replicating the established letter-axis ⊥ content-axis falsification of al-Biqāʿī's muqaṭṭaʿāt-munāsaba claim — see Q032-F-03 NULL).

## 9. FR-neighborhood of Q 31

Q 31's nearest 12 surahs in Fisher-Rao root-distribution space (decoded from `h-new-111.json D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 45 | al-Jāthiya | 0.7685 | ḥawāmīm cluster, Late Meccan, knowledge-emphasis |
| 2 | Q 64 | al-Taghābun | 0.7743 | musabbiḥāt cluster (yusabbiḥu opener), monotheistic-frame |
| 3 | Q 22 | al-Ḥajj | 0.7991 | mixed Meccan-Medinan, eschatological-cosmic |
| 4 | Q 62 | al-Jumuʿah | 0.8313 | Medinan, **the META-cluster meta-hub** (cross-finding-009) |
| 5 | Q 35 | Fāṭir | 0.8455 | Late Meccan, divine-creator emphasis |
| 6 | Q 13 | al-Raʿd | 0.8505 | early Medinan, ALR opener |
| 7 | Q 112 | al-Ikhlāṣ | 0.8555 | tawḥīd quintessential |
| 8 | Q 1 | al-Fātiḥa | 0.8559 | umm al-kitāb |
| 9 | Q 61 | al-Ṣaff | 0.8630 | musabbiḥāt cluster |
| 10 | Q 96 | al-ʿAlaq | 0.8664 | first revelation, *aqlām/ʿallam* knowledge-opener |
| 11 | Q 91 | al-Shams | 0.8694 | oath-cluster |
| 12 | Q 14 | Ibrāhīm | 0.8700 | ALR cluster, prophet-named |

Q 31's mean FR-distance to the other 113 surahs is **0.948**, just above the corpus FR-mean 0.924 — Q 31 is **slightly content-distinct** but **not** an extreme outlier. Notable: Q 31's nearest neighbor is Q 45 (al-Jāthiya, the *ḥawāmīm* member with strong knowledge-emphasis), and the top-12 includes the meta-hub Q 62 (rank 4), Q 1 (rank 8), and Q 112 (rank 7). Q 31's ALM-cluster siblings appear LATER in the ranking: Q 32 at rank ~30, Q 30 at rank ~32, Q 29 at rank ~26, Q 2 at rank ~63, Q 3 at rank ~66 (i.e. **Q 31 is closer in FR space to many non-ALM surahs than to its own ALM-cluster**).

This is one of the strongest single-surah pieces of evidence for the established **muqaṭṭaʿāt letter-axis ⊥ content-axis** finding (cross-finding-006 + Q032-F-03 NULL): even the surah whose structural-opening signature most explicitly invokes the muqaṭṭaʿāt-cohort identity (Q 31's *tilka āyātu al-kitāb*) is content-FR closer to non-ALM surahs than to its ALM siblings.

## 10. Adjacency context — the Q 30 → Q 31 → Q 32 mushaf-segment

From `h-new-720.json` (canonical-adjacency-cost spectrum):

| Boundary | δ_raw | fraction_residual | Note |
|:--|:--:|:--:|:--|
| Q 29 → Q 30 | +0.0293 | 0.0035 | low |
| Q 30 → Q 31 | +0.0376 | 0.0045 | low — Late-Meccan ALM smooth |
| Q 31 → Q 32 | +0.1005 | 0.0121 | **modest — book-ref → ALM-exception transition** |
| Q 32 → Q 33 | +0.3631 | 0.0438 | **TOP-3 expensive corpus-wide** (al-Biqāʿī-validated structural break; cross-finding-026 §13.5) |

Q 31 sits in a **smooth interior** of the Late-Meccan ALM block: its left-seam (Q 30→Q 31) and right-seam (Q 31→Q 32) are both well below the corpus-median residual (~0.02). The expensive seam comes one position later at Q 32→Q 33, where the ALM-cluster definitively terminates and Q 33 al-Aḥzāb opens a new structural region (long Medinan legal-narrative).

By the empirically-seamless (clamped-zero) corpus catalog from h-new-720 (13 pairs total per H-NEW-1240): Q 31 is **NOT** in the seamless set. The 13 clamped-zero pairs are: {Q 91→92, Q 4→5, Q 6→7, Q 3→4, Q 65→66, Q 109→110, Q 73→74, Q 105→106, Q 86→87, Q 93→94, Q 64→65, Q 72→73, Q 37→38}. Q 31's seams are inexpensive but not optimal-equivalent — they are **constructive low-cost transitions** within the Late-Meccan ALM segment.

## 11. iʿjāz signature

| Component | Value | z-score | Note |
|:--|:--:|:--:|:--|
| Rhyme entropy (nats) | 1.291 | +0.944 | HIGH — multi-letter rhyme palette |
| Top final-letter ر (rāʾ) | 47.1% | — | not monorhyme; ر coexists with م (24%), ن (21%), د (~6%), ظ (~3%) |
| Mean content distance | 0.948 | +0.246 | mid-corpus |
| Local cohesion | 1.060 | −0.624 | slightly low |
| sig_A (al-Bāqillānī fawāṣil) | +0.698 | rank 43/114 | mid-positive |
| sig_B (al-Sakkākī iqāʿ) | +0.319 | rank 49/114 | mid-positive |
| UAS | −1.171 | rank 80/114 | LOW |

Q 31 has **moderate-mid iʿjāz signature** (top quartile on neither axis, but positive on both). Its high rhyme-entropy (palette of 5+ verse-final letters with ر dominating) is unusual for a 34-verse Late-Meccan surah — mid-Meccan surahs typically converge on monorhyme. The non-monorhyme reflects Q 31's **structural diversity** (4 thematic blocks, 3 voice-registers: divine, Luqmān-quoted, eschatological-warning).

UAS rank 80/114 places Q 31 in the **bottom third** of the unified architectural significance ranking (`h-new-840.json`). This is consistent with Q 31's role: it is a **content-rich didactic compendium**, not a structurally-extraordinary surah. The structural-iʿjāz weight has been used elsewhere in the corpus (Q 1, Q 33, Q 9, Q 12, Q 55, Q 62, Q 112-114 are the high-UAS clusters — Q 31 is not in these).

## 12. Architectural type classification

| Axis | Q 31 placement |
|:--|:--|
| Length class | Late-Meccan mid-corpus (n=34, 64 graphemes/verse) |
| Compression-tail position | s=31 < kink-50, OUTSIDE compression-tail regime |
| iʿjāz typology | mid-positive on both axes; non-monorhyme |
| FR neighborhood | Late-Meccan eschatological-cosmic mix (Q 45, Q 22, Q 35) + meta-hub-adjacent (Q 62) + tawḥīd-anchor adjacent (Q 112, Q 1, Q 96) |
| Outlier-strength | WEAK |
| Cluster memberships | (1) cross-finding-008 muqaṭṭaʿāt → book-introduction (CONFIRMED at p=3×10⁻¹²) — Q 31 is a **clear-cohort member** with the explicit *tilka āyātu al-kitāb* couplet; (2) the 6-surah ALM-cluster — Q 31 is a Late-Meccan-core member; (3) the inner ALM-book-reference triad {Q 2, Q 3, Q 31} (NOT in the ALM-exception subset {Q 29, Q 30, Q 32}); (4) Late-Meccan eponymous-named non-prophet wisdom-figure (corpus-singleton — no other surah named for a non-prophet sage) |
| Adjacency role | smooth-low-cost RIGHT seam (→Q 32, δ=0.1005); smooth-low-cost LEFT seam (Q 30→, δ=0.0376); LEFT-OF the corpus-TOP-3 expensive Q 32→Q 33 seam |

**Architectural verdict**: Q 31 is the **Late-Meccan didactic-wisdom compendium** of the corpus — eponymously named for a non-prophet sage, structurally organized around a single 8-verse moral-pericope, embedded in a 4-block arc that runs from book-self-reference through human exemplar through cosmic-signs to eschatological-knowledge limits. Its empirical signature is **mid-everything** — Q 31 is not a structural-iʿjāz outlier; the surah's distinctiveness lives at the **content-thematic level** (the Luqmān pericope is a corpus-singleton in genre), not at the orthographic-structural level.

This is consistent with H-META-1's classifier prediction (item #5 in MASTER-FINDINGS-LEDGER §3): a Late-Meccan, Tanzil/Nöldeke-mid-Meccan, ALM-opened, named-for-a-figure, structural-content-blend surah of moderate length is predicted to score CONFIRMED on aesthetic-rhetorical balagha axes (block-level munāsaba, voice-shift iltifāt, scholastic eponymy) while NOT scoring on numerological-symmetry axes (no clean abjad-sum, no mathematical letter-multiset structure beyond what its ALM-cohort membership already accounts for). This prediction is empirically borne out below in the per-test verdicts of `06-novel-findings.md`.

## 13. Cross-references

- [[h-new-111-fisher-rao-mushaf]] — Q 31 FR-row, ALM-cluster pairwise, content-axis-not-cohesive evidence.
- [[h-new-590-outlier-spectrum]] — Q 31 WEAK_OUTLIER (Δ%ile = +2.14, p_greater = 0.31) on window {Q 28-34}.
- [[h-new-700-phonological-compression-tail]] — Q 31 ر-rāwī dominant (47.1%) but non-monorhyme; outside the compression-tail regime.
- [[h-new-720-canonical-adjacency-cost]] — Q 31's seams are smooth-low-cost; LEFT of the TOP-3 expensive Q 32→Q 33 seam.
- [[h-new-750-ijaz-signature]] — Q 31 sig_A=+0.70 (rank 43); sig_B=+0.32 (rank 49); mid-positive on both axes.
- [[h-new-840-unified-architectural-score]] — Q 31 UAS rank 80/114 (LOW).
- [[cross-finding-008]] — Q 31 is a clear muqaṭṭaʿāt → book-introduction cohort member with the explicit couplet at v.2.
- [[cross-finding-013]] — Q 31 is in the structured-mushaf-ring; the Q 31 → Q 32 transition is one rung INSIDE the major Q 32 → Q 33 hinge.
- [[surahs/Q032-al-sajda]] — mushaf-immediate-neighbor with deep ALM-exception analysis (specialist ran 2026-05-08).
- [[surahs/Q030-al-rum]] — mushaf-left-neighbor; Late-Meccan ALM with TEST/PROPHECY (Byzantium-prophecy) anchor.
- [[surahs/Q029-al-ankabut]] — Late-Meccan ALM-exception (no book-ref opener); H-NEW-93 NULL on the 2-surah sub-class.
- [[surahs/Q037-al-saffat]] — co-bunayya-vocative location (Q 37:102 Ibrāhīm to Ismāʿīl); see Q031-F-01 cohort analysis.
- [[surahs/Q012-yusuf]] — co-equal yā-bunayya density (3/9); Yūsuf-cycle Yaʿqūb father-voice.
