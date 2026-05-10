---
id: H-NEW-1790
title: Refrain-architecture full corpus inventory — strict (≥3) and broad (≥2) verbatim verse-repetition
date_locked: 2026-05-10
date_run: 2026-05-10
verdict: PASS-DIRECTED FULL
seed: deterministic (no permutation)
prereg_sha: 1687591022153584cf745bd83855fd907387ac0afa2978475131bb1e071dd3e4
prereg_path: findings/phase-b-hypotheses/prereg-h-new-1790-refrain-inventory.md
script_path: findings/phase-b-hypotheses/scripts/h-new-1790.py
output_json: findings/phase-b-hypotheses/csv/h-new-1790.json
---

# H-NEW-1790 — refrain-architecture full corpus inventory

## Verdict: PASS-DIRECTED FULL

Both pre-registered cells pass. The corpus contains EXACTLY 5 surahs with strict refrains (verse appearing verbatim ≥3 times within the same surah). Q 55 al-Raḥmān is corpus-rank-1 by saturation = max_repeat / verse_count (0.397), confirming H-NEW-1320's count-axis rank survives length-normalisation.

| Cell | Result | Pass (α=0.025) |
|:--|--:|:-:|
| A — Q 55 saturation-rank-1 | 0.397, rank 1/114 | **YES ✓** |
| B — N_strict ∈ [5, 15] | 5 strict-refrain surahs | **YES ✓** |

## The corpus-exact 5 strict-refrain surahs

Exactly five surahs in the 114-surah corpus carry at least one verse appearing verbatim ≥3 times within the same surah. This matches H-NEW-1230 exactly. All five are mid-to-late Meccan.

| Surah | Strict refrains | Max count | Saturation | Verses |
|:--|--:|--:|--:|--:|
| Q 55 al-Raḥmān | 1 | 31 | 0.397 | 78 |
| Q 77 al-Mursalāt | 1 | 10 | 0.200 | 50 |
| Q 26 al-Shuʿarāʾ | 5 | 8 | 0.035 | 227 |
| Q 37 al-Ṣāffāt | 4 | 4 | 0.022 | 182 |
| Q 54 al-Qamar | 2 | 4 | 0.073 | 55 |

Every surah outside this set of five has all of its verses appearing at most twice. The corpus is therefore architecturally bimodal: 5 surahs that systematically deploy strict refrains, 109 surahs that do not.

## Top-10 by saturation (Cell A axis)

| Rank | Surah | n_verses | max_rc | Saturation | Top refrain |
|:-:|:--|:-:|:-:|:-:|:--|
| 1 | Q 55 al-Raḥmān | 78 | 31 | **0.397** | *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* |
| 2 | Q 109 al-Kāfirūn | 6 | 2 | 0.333 | *wa-lā antum ʿābidūna mā aʿbud* |
| 3 | Q 103 al-ʿAṣr | 3 | 1 | 0.333 | — (no broad-refrain) |
| 4 | Q 108 al-Kawthar | 3 | 1 | 0.333 | — |
| 5 | Q 110 al-Naṣr | 3 | 1 | 0.333 | — |
| 6 | Q 106 Quraysh | 4 | 1 | 0.250 | — |
| 7 | Q 112 al-Ikhlāṣ | 4 | 1 | 0.250 | — |
| 8 | Q 77 al-Mursalāt | 50 | 10 | 0.200 | *waylun yawmaʾidhin li-l-mukadhdhibīn* |
| 9 | Q 97 al-Qadr | 5 | 1 | 0.200 | — |
| 10 | Q 105 al-Fīl | 5 | 1 | 0.200 | — |

The saturation axis surfaces **two distinct refrain regimes**:

1. **Macro-refrain (long surah, high count, high saturation)**: Q 55 alone. 31 repetitions across 78 verses.
2. **Micro-refrain (very short surah, modest absolute count, high saturation by tiny denominator)**: Q 109 (2/6 = 33%). H-NEW-1320 §saturation-outlier already flagged this.

The intermediate ranks 3-7 are short surahs with no broad-refrain at all; their high saturation is the denominator-artefact `1 / (3 or 4)` — every verse trivially appears at least once, so `max_rc / n_verses = 1/3 = 0.333` for any three-verse surah. These are EXCLUDED from substantive refrain analysis by the count-floor; they are "saturation artefacts," not refrains.

Filtering to surahs whose `max_rc ≥ 2` yields the substantively meaningful saturation top-list, with Q 55 strict rank-1 and Q 109 strict rank-2.

## Top-10 by absolute max-repeat-count (H-NEW-1320 replication)

| Rank | Surah | max_rc | Saturation | Top refrain |
|:-:|:--|:-:|:-:|:--|
| 1 | Q 55 al-Raḥmān | 31 | 0.397 | *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* |
| 2 | Q 77 al-Mursalāt | 10 | 0.200 | *waylun yawmaʾidhin li-l-mukadhdhibīn* |
| 3 | Q 26 al-Shuʿarāʾ | 8 | 0.035 | *fa-ttaqū Allāh wa-aṭīʿūn* (ranking tie with Q 26's *wa-inna rabbaka la-huwa al-ʿazīz al-raḥīm* also at 8 — alphabetical tie-break) |
| 4 | Q 37 al-Ṣāffāt | 4 | 0.022 | *illā ʿibāda Allāh al-mukhlaṣīn* |
| 5 | Q 54 al-Qamar | 4 | 0.073 | *wa-laqad yassarnā al-Qurʾāna li-l-dhikr fa-hal min muddakir* |
| 6 | Q 2 al-Baqara | 2 | 0.007 | *tilka ummatun qad khalat, lahā mā kasabat...* |
| 7 | Q 5 al-Māʾida | 2 | 0.017 | *wa-lladhīna kafarū wa-kadhdhabū bi-āyātinā ūlāʾika aṣḥābu al-jaḥīm* |
| 8 | Q 7 al-Aʿrāf | 2 | 0.010 | *fa-akhadhathum al-rajfah fa-aṣbaḥū fī dārihim jāthimīn* |
| 9 | Q 18 al-Kahf | 2 | 0.018 | *thumma atbaʿa sababā* |
| 10 | Q 23 al-Muʾminūn | 2 | 0.017 | *qāla rabbi inṣurnī bi-mā kadhdhabūn* |

This replicates H-NEW-1320's published top-10 exactly: Q 55 > Q 77 > Q 26 > Q 37 = Q 54 > {Q 2, 5, 7, 18, 23 broad-refrain pool}. The two findings inter-verify.

## Strict-refrain enumeration (every verse repeating ≥3 times)

Total: **14 distinct refrain-verses** across 5 surahs.

### Q 55 al-Raḥmān (1 refrain, count 31)

- *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* — 31× (Q 55:13, 16, 18, 21, 23, 25, 28, 30, 32, 34, 36, 38, 40, 42, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77 — verified verbatim in `quran-text/quran-no-tashkeel.json`)

### Q 77 al-Mursalāt (1 refrain, count 10)

- *waylun yawmaʾidhin li-l-mukadhdhibīn* — 10× (Q 77:15, 19, 24, 28, 34, 37, 40, 45, 47, 49)

### Q 26 al-Shuʿarāʾ (5 strict refrains)

- *fa-ttaqū Allāh wa-aṭīʿūn* — 8× (prophet-imperative formula; appears in Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb pericopes)
- *wa-inna rabbaka la-huwa al-ʿazīzu al-raḥīm* — 8× (closing-formula, prophet-pericope terminator)
- *inna fī dhālika la-āyatan wa-mā kāna aktharuhum muʾminīn* — 6× (pre-closing-formula, paired with above)
- *innī lakum rasūlun amīn* — 5× (prophet-introduction formula)
- *wa-mā asʾalukum ʿalayhi min ajrin in ajriya illā ʿalā rabbi al-ʿālamīn* — 5× (no-payment formula)

**Q 26 is QUINTUPLE-refrain**: 5 distinct refrains, total occurrences = 8 + 8 + 6 + 5 + 5 = **32**, density 32/227 = 0.141. H-NEW-1230 originally identified a quadruple-refrain (27 occurrences); strict-≥3 enumeration here surfaces a 5th refrain (*innī lakum rasūlun amīn* at 5 occurrences). **REFINES H-NEW-1230's quadruple to QUINTUPLE.**

### Q 37 al-Ṣāffāt (4 strict refrains)

- *illā ʿibāda Allāh al-mukhlaṣīn* — 4× (the "except the devoted servants" formula; cross-surah echo at Q 15:40, Q 38:83)
- *innā kadhālika najzī al-muḥsinīn* — 3× (Q 37:80, 105, 110 — the "thus We reward the doers-of-good" formula; cross-surah echo at Q 77:44)
- *innahu min ʿibādinā al-muʾminīn* — 3× (Q 37:81, 111, 132 — the "he is among Our believing servants" formula)
- *wa-taraknā ʿalayhi fī al-ākhirīn* — 3× (Q 37:78, 108, 119 — the "We left him a remembrance in later generations" formula)

**Q 37 is QUADRUPLE-refrain**: 4 distinct refrains, total occurrences = 4 + 3 + 3 + 3 = **13** in 182 verses. The cross-surah echo of *innā kadhālika najzī al-muḥsinīn* into Q 77:44 is a documented prophet-cycle/judgment-day bridge.

### Q 54 al-Qamar (2 strict refrains)

- *wa-laqad yassarnā al-Qurʾāna li-l-dhikri fa-hal min muddakir* — 4× (Q 54:17, 22, 32, 40 — the "We made the Qurʾān easy" formula)
- *fa-kayfa kāna ʿadhābī wa-nudhur* — 3× (Q 54:18, 30, 37 — the "how was My punishment and warning" formula; appears in 3 of the 4 pericopes)

**Q 54 is DUAL-refrain**: total 4 + 3 = 7 occurrences in 55 verses, density 0.127.

## Comparison to H-NEW-1320 3-tier finding

| Finding | Top-3 by absolute count | Refrain-bearing surah count |
|:--|:--|--:|
| H-NEW-1320 | Q 55 (31) > Q 77 (10) > Q 26 (8) | 3 surahs explicitly named in tier |
| H-NEW-1230 | Q 55, Q 77, Q 26, Q 54, Q 37 | 5 (combined-refrain-count basis) |
| **H-NEW-1790** | Q 55 (31) > Q 77 (10) > Q 26 (8) > {Q 37, Q 54} (4) | **EXACTLY 5 strict-refrain surahs** |

H-NEW-1790 confirms BOTH prior findings exactly. The 3-tier H-NEW-1320 architecture {Q 55, Q 77, Q 26} sits inside the 5-tier H-NEW-1230/H-NEW-1790 architecture {Q 55, Q 77, Q 26, Q 37, Q 54}. The corpus has TWO empirically-defined refrain regimes:

- **Core trio (counts 31, 10, 8)**: Q 55, Q 77, Q 26. Audience-distinct, function-distinct, position-distinct rhetorical apparatus.
- **Extended pair (counts 4, 4)**: Q 37, Q 54. Same architectural axis at lower amplitude. Both surahs use multiple refrains in a single pericope-closure pattern.

The new observation here is that **Q 26 carries 5 strict refrains, not 4** — *innī lakum rasūlun amīn* (5×) is added to H-NEW-1230's quadruple. Q 37 also surfaces with 4 strict refrains (not just the *illā ʿibāda Allāh al-mukhlaṣīn* tracked previously).

## Cross-surah refrain-pairs (post-hoc supplement, MW-7 single-test cap)

The inventory surfaces 70 verse-strings appearing in two or more surahs. The most notable are the muqaṭṭaʿāt families (which are not "refrains" in the rhetorical sense but emerge as verbatim cross-surah matches) and a handful of formulaic verses.

### Cross-surah refrain-pairs of substantive interest

| Verse | Surahs | Total | Note |
|:--|:--|:-:|:--|
| *waylun yawmaʾidhin li-l-mukadhdhibīn* | Q 77 (10×), Q 83 (1×) | 11 | H-NEW-1230 already documented; Q 83:10 is a "refrain-spillover" from Q 77 source |
| *wa-yaqūlūna matā hādhā al-waʿd in kuntum ṣādiqīn* | Q 10, 21, 27, 34, 36, 67 | 6 | Eschatological denier-speech, appears once each in 6 surahs |
| *tanzīl al-kitābi min Allāh al-ʿazīzi al-ḥakīm* | Q 39, 45, 46 | 3 | Scripture-revelation-opener family; subset of H-NEW-1170 tanzīl-opener cluster |
| *innā kadhālika najzī al-muḥsinīn* | Q 37 (3×), Q 77 (1×) | 4 | Q 37 internal-refrain bridging to Q 77 single-instance echo |
| *fa-sabbiḥ bi-ismi rabbika al-ʿaẓīm* | Q 56, Q 69 | 3 | Sabbiḥa-opener family (cross-finding-008 hamd/sabbaḥa) |

### Muqaṭṭaʿāt as cross-surah verbatim verses

The corpus's letter-family openers register as cross-surah verbatim matches:
- **ḥā-mīm** (حم): Q 40, 41, 42, 43, 44, 45, 46 — appears as verse 1 of 7 surahs. This is the entire ḥawāmīm family.
- **alif-lām-mīm** (الم): Q 2, 3, 29, 30, 31, 32 — appears as verse 1 of 6 surahs.

These are NOT rhetorical refrains; they are muqaṭṭaʿāt openers. Included here because the verbatim-match procedure is sensitivity-neutral to verse-type. Their cross-surah verbatim status is itself a well-known architectural feature (see H-NEW-610 letter-family-content-NULL replications: Q 39-NULL, Q 14-NULL, etc.) but it does manifest as the largest cross-surah "refrain-pair" cluster by `n_surahs`.

### *wa-yaqūlūna matā hādhā al-waʿd* — 6-surah cross-positional refrain

The question *wa-yaqūlūna matā hādhā al-waʿd in kuntum ṣādiqīn* — "they say: when is this promise [coming] if you are truthful?" — appears as a single verse in Q 10:48, Q 21:38, Q 27:71, Q 34:29, Q 36:48, Q 67:25. **This is a corpus-EXACT 6-surah denier-speech refrain** that none of H-NEW-1230, H-NEW-1320, or H-NEW-1190 (*wa-mā adrāka mā*) previously named. **Genuine new finding**: it's a polemic-discourse-marker — every occurrence is a verbatim quotation of denier-eschatological-skepticism — extending H-NEW-1190's discourse-marker thesis to a 6-surah polemic-question cluster.

The 6 surahs hosting it span:
- **Q 10 Yūnus** (mid-Meccan), **Q 21 al-Anbiyāʾ** (mid-Meccan), **Q 27 al-Naml** (mid-Meccan), **Q 34 Sabaʾ** (mid-Meccan), **Q 36 Yā Sīn** (mid-Meccan), **Q 67 al-Mulk** (late-Meccan).
- All 6 are mid-to-late-Meccan eschatology-and-prophet-cycle surahs. The refrain is the verbatim recurrence of the denier's polemic-question across the polemical-Meccan corpus.

This connects to H-NEW-1190 (*wa-mā adrāka mā* 10-surah cluster) as a sibling discourse-marker — same period, similar 6-10 surah breadth, distinct question-template. Queue H-NEW-1791 to formalise as a separate refrain-family.

## Cell B detail — exact N_strict = 5

| Surah | Strict refrains | Function-type |
|:-:|:-:|:--|
| Q 26 | 5 | prophet-pericope quintuple (intro + body + close + close-meta + no-fee) |
| Q 37 | 4 | prophet-pericope quadruple (intro + reward + status + memorial) |
| Q 54 | 2 | qurʾān-easy + punishment-question dual |
| Q 55 | 1 | dual-audience macro-refrain |
| Q 77 | 1 | eschatological-denier macro-refrain |

The corpus has exactly 5 refrain-bearing surahs by strict (≥3) criterion. The pre-registered window [5, 15] passes at the LOWER edge. **The corpus is sparse in refrain architecture**: ~4.4% of surahs (5/114) carry strict-internal-repetition refrains.

## Honest limits

- **Strict verbatim only**: no near-match, no Levenshtein, no fuzzy. Near-identical verses with single-token differences (e.g., singular vs. plural pronoun) are NOT counted. A future H-NEW-1791 could replicate under Levenshtein-distance ≤ 2 or token-bag identity.
- **Tashkeel sensitivity**: tested on no-tashkeel only. Min-tashkeel might collapse some near-identical verses (different vocalisations of identical consonantal-skeletons); full-tashkeel might split apart visually-identical-but-vocally-distinct repeats. Out-of-scope for this pre-reg.
- **Verdict ceiling = PASS-DIRECTED**: the inventory is deterministic — there's no permutation null. The verdict is the inventory itself; PASS-DIRECTED reflects that the pre-committed Cell A and Cell B both pass. INDEPENDENT REPLICATION under min-tashkeel or under Levenshtein-fuzzy-match required for promotion to CONFIRMED.
- **Q 1:1 cross-surah identity unmasked**: the JSON-text data file's verse-list does NOT include the bismillāh as verse 1 of surahs 2-114. If the bismillāh-counted-everywhere variant is applied, Q 1:1 = each of 112 other surahs' verse 0 (Q 9 excluded) — but this is a metadata-policy artefact, not a rhetorical refrain. The default rules-tuple (basmala-counted-only-in-surah-1) gives the substantively-meaningful inventory.
- **Cross-surah refrain-pair table is post-hoc**: it surfaced 1 substantively-new finding (*wa-yaqūlūna matā hādhā al-waʿd* 6-surah cluster). That follow-on is a discovery; it carries MW-7 single-test α=0.05 cap and is queued for replication as H-NEW-1791.

## Connection to existing findings

- **H-NEW-1230** (existing): 5 refrain-bearing surahs identified via combined-refrain-count. **CONFIRMED at exact set-identity**: {Q 26, Q 37, Q 54, Q 55, Q 77}.
- **H-NEW-1320** (existing): 3-tier refrain architecture {Q 55, Q 77, Q 26} via max-count rank. **REPLICATED**: same ordering Q 55 > Q 77 > Q 26 on both count and saturation axes.
- **Cross-finding-027 / H-NEW-1250** Q 55 dual-audience signature: this finding verifies that Q 55's count-rank-1 also holds as saturation-rank-1 (length-normalised).
- **H-NEW-1190** *wa-mā adrāka mā* 10-surah cross-surah refrain: distinct phenomenon (cross-surah polemic-question vs. intra-surah lafẓī takrār). H-NEW-1790 surfaces a **sibling cross-surah refrain** (*wa-yaqūlūna matā hādhā al-waʿd* 6-surah cluster) under the cross-surah-refrain-pair table.
- **al-Suyūṭī**, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on *takrīr*: the classical takrīr taxonomy distinguishes lafẓī (verbal) from maʿnawī (meaning) repetition. H-NEW-1790 quantifies the lafẓī variety, locating EXACTLY 5 surahs carrying strict lafẓī takrār.
- **al-Zarkashī**, *al-Burhān fī ʿulūm al-Qurʾān*, *al-nawʿ al-tāsiʿ wa-l-arbaʿūn* (the 49th type, *al-takrār*): classical typology of repetition. The empirical inventory tests Zarkashī's category at corpus-distribution strength.
- **al-Zamakhsharī**, *al-Kashshāf*, on Q 55 + Q 26: the qarīna-as-chorus reading is locked at 5-element quintuple-refrain in Q 26 + macro-refrain in Q 55.

## Replication seeds (NOT yet locked)

- **H-NEW-1791**: cross-surah polemic-question 6-surah refrain (*wa-yaqūlūna matā hādhā al-waʿd*). PC: H-NEW-1190 *wa-mā adrāka mā* 10-surah cluster.
- **H-NEW-1792**: refrain inventory under min-tashkeel — same set of 5 strict-refrain surahs, or shift? Tashkeel-sensitivity replication.
- **H-NEW-1793**: refrain inventory under Levenshtein ≤ 2 (near-verbatim) — does Q 54 or Q 37 expand its refrain set under fuzzy match?

## Verdict summary

| Quantity | Value |
|:--|--:|
| N_strict_refrain_surahs | **5** ({26, 37, 54, 55, 77}) |
| Q 55 saturation | **0.397** (rank 1/114) |
| Q 109 micro-saturation | 0.333 (rank 2/114, count=2) |
| Distinct strict-refrain verses corpus-wide | **13** (1+1+5+4+2) |
| Cross-surah verbatim verse-pairs | 70 (incl. 13 muqaṭṭaʿāt-family + 57 rhetorical) |
| Q 26 strict-refrain count | **5** (refines H-NEW-1230 quadruple → QUINTUPLE) |
| New cross-surah finding queued | *wa-yaqūlūna matā hādhā al-waʿd* 6-surah cluster (Q 10, 21, 27, 34, 36, 67) |
| Cell A pass | ✓ |
| Cell B pass | ✓ |
| Final verdict | **PASS-DIRECTED FULL** |

The corpus has EXACTLY 5 refrain-bearing surahs (strict verbatim ≥3 within-surah). Q 55 saturates the architecture at the macro scale (31 occurrences, 78 verses, 39.7% saturation). Q 109 is the corresponding micro-saturation extremum (2 occurrences, 6 verses, 33.3%). The 5-surah strict-refrain set replicates H-NEW-1230 exactly; the 3-tier {Q 55, Q 77, Q 26} architecture of H-NEW-1320 sits as the upper sub-tier of this set. New discovery: Q 26 carries 5 strict refrains, not 4, and a 6-surah cross-surah polemic-question refrain (*wa-yaqūlūna matā hādhā al-waʿd*) surfaces as a sibling architectural feature to H-NEW-1190's *wa-mā adrāka mā* family.
