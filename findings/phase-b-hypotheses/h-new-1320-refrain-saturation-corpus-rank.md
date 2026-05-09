---
id: H-NEW-1320
title: Refrain-saturation corpus-rank — Q 55 strict rank-1 + 3-tier refrain cluster
date_locked: 2026-05-09
date_run: 2026-05-09
verdict: PASS-DIRECTED FULL
seed: 20260509
n_perm: 10000
prereg_sha: abc1630142b86b70f7bdec1edc51b2d17c7987d5e776e6bb6d8da069590abec4
prereg_path: findings/phase-b-hypotheses/h-new-1320-refrain-saturation-corpus-rank-prereg.md
script_path: findings/phase-b-hypotheses/scripts/h_new_1320_refrain_saturation.py
output_json: findings/phase-b-hypotheses/csv/h-new-1320.json
---

# H-NEW-1320 — Refrain-saturation corpus-rank — Q 55 rank-1 + 3-tier refrain cluster

## Verdict: PASS-DIRECTED FULL

Both pre-registered cells PASS. The 3-tier refrain cluster {Q 55, Q 77, Q 26} is empirically locked.

| Cell | Result | Pass (α=0.025) |
|:--|--:|:-:|
| A — strict rank-1 + permutation null | Q 55 strict rank-1; p_perm = 0.0000 | **YES ✓** |
| B — Q 26 + Q 77 both top-5 | Q 77 rank-2, Q 26 rank-3 | **YES ✓** |
| MW-5 instrument-control | Null mean max-over-all-surahs = 2.94 | YES ✓ |

## Top-15 ranking by max identical-verse-repeat-count

| Rank | Surah | Repeat count | Saturation | Top repeated verse |
|:-:|:--|:-:|:-:|:--|
| 1 | Q 55 al-Raḥmān | **31** | 0.397 | *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān* |
| 2 | Q 77 al-Mursalāt | 10 | 0.200 | *waylun yawmaʾidhin li-l-mukadhdhibīn* |
| 3 | Q 26 al-Shuʿarāʾ | 8 | 0.035 | *wa-inna rabbaka la-huwa al-ʿazīzu al-raḥīm* |
| 4 | Q 37 al-Ṣāffāt | 4 | 0.022 | *illā ʿibāda Allāh al-mukhlaṣīn* |
| 5 | Q 54 al-Qamar | 4 | 0.073 | *wa-laqad yassarnā al-Qurʾāna li-l-dhikri fa-hal min muddakir* |
| 6 | Q 2 al-Baqara | 2 | 0.007 | *yā banī Isrāʾīla udhkurū niʿmatī…* |
| 7 | Q 5 al-Māʾida | 2 | 0.017 | *wa-lladhīna kafarū wa-kadhdhabū bi-āyātinā ūlāʾika aṣḥābu al-jaḥīm* |
| 8 | Q 7 al-Aʿrāf | 2 | 0.010 | *fa-akhadhathum al-rajfah, fa-aṣbaḥū fī dārihim jāthimīn* |
| 9 | Q 18 al-Kahf | 2 | 0.018 | *thumma atbaʿa sababā* |
| 10 | Q 23 al-Muʾminūn | 2 | 0.017 | *qāla rabbi inṣurnī bi-mā kadhdhabūn* |
| 11 | Q 28 al-Qaṣaṣ | 2 | 0.023 | *wa-yawma yunādīhim fa-yaqūlu ayna shurakāʾiya alladhīna kuntum tazʿumūn* |
| 12 | Q 56 al-Wāqiʿa | 2 | 0.021 | *thullatun min al-awwalīn* |
| 13 | Q 83 al-Muṭaffifīn | 2 | 0.056 | *kitābun marqūm* |
| 14 | Q 84 al-Inshiqāq | 2 | 0.080 | *wa-adhinat li-rabbihā wa-ḥuqqat* |
| 15 | Q 109 al-Kāfirūn | 2 | **0.333** | *wa-lā antum ʿābidūna mā aʿbud* |

## Permutation null result

Under random verse-string redistribution preserving each surah's verse-count (10000 perms, seed=20260509):

- Mean max-over-all-surahs in null: **2.94**
- Observed Q 55 max-repeat-count: **31**
- p (any random surah achieves ≥ 31): **0.00000** (0/10000)
- p (Q 55 specifically achieves ≥ 31): **0.00000** (0/10000)

**Q 55's refrain saturation is roughly 10× the null-expected corpus maximum.** This is a corpus-EXTREME, instrument-controlled, pre-registered, permutation-passed finding.

## The 3-tier refrain cluster

The top-3 refrain-architectured surahs are:

### Tier 1 — Q 55 al-Raḥmān (saturation 0.397)
The *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān* (= "which of your Lord's blessings will you two deny?") refrain repeats 31 times across the surah's 78 verses. This is the **dual-audience structural signature** of cross-finding-027 / H-NEW-1250. The "two" (kumā / dual) addresses jinn + ins — the joint creation announcement frame.

### Tier 2 — Q 77 al-Mursalāt (saturation 0.200)
The *waylun yawmaʾidhin li-l-mukadhdhibīn* (= "woe on that day to the deniers") refrain repeats 10 times across 50 verses. Eschatological-judgment refrain anchoring the day-of-decision narrative. **Connects to H-NEW-1190 wa-mā-adrāka-mā cluster (Q 77 is a member) and H-NEW-1200 short-Meccan-tail eschatology cluster.**

### Tier 3 — Q 26 al-Shuʿarāʾ (saturation 0.035)
The *wa-inna rabbaka la-huwa al-ʿazīzu al-raḥīm* (= "and indeed your Lord — He is the Mighty, the Merciful") closing-formula repeats 8 times across 227 verses. Each occurrence closes a prophet-narrative pericope (Mūsā, Ibrāhīm, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb, Muḥammad implicit-frame). **Q 26 also has the "*inna fī dhālika la-āyatan wa-mā kāna aktharuhum muʾminīn*" pre-formula 8 times paired with the closing.** This is the **prophet-cycle architectural signature** previously surfaced in H-NEW-90 (Q 7 prophet-cycle parallelism z=+5.25) and now extended to Q 26 as the 3rd refrain-tier.

## Saturation outlier — Q 109 al-Kāfirūn

Q 109 al-Kāfirūn ranks #15 by absolute count (only 2) but **#2 by saturation (0.333)**. Its 6-verse short-Meccan structure has 2 of 6 verses (33%) saturated by *wa-lā antum ʿābidūna mā aʿbud*. This is a hyper-compressed declaration-of-distinction refrain. **Queue H-NEW-1321 follow-up** to investigate Q 109 as a saturation-extreme micro-refrain surah relative to Q 55's saturation-extreme macro-refrain surah.

## What survived strict pre-reg

The original handoff §7b query suggested "Q 26, Q 77 candidates." **Both candidates confirmed in the top-3.** No other surah was suggested; none crashed the top-3. The exact ordering Q 55 > Q 77 > Q 26 is the empirical adjudication of the handoff conjecture.

## Interpretation: iʿjāz al-takrīr (eloquence of repetition) extended

Cross-finding-027 framed Q 55 as the corpus-EXACT iʿjāz al-takrīr signature. This finding extends the doctrine to a **3-tier refrain corpus architecture**:

| Surah | Refrain count | Saturation | Function | Audience |
|:--|:-:|:-:|:--|:--|
| Q 55 | 31 | 0.397 | Blessing-acknowledgement-rebuke | Dual (jinn + ins) |
| Q 77 | 10 | 0.200 | Eschatological-judgment-warning | Deniers (3rd person) |
| Q 26 | 8 | 0.035 (count-density) | Prophet-cycle pericope-closer | Prophet (consolation) |

Three distinct refrain functions, three distinct audiences, three distinct rhetorical positions in the corpus. The iʿjāz al-takrīr is not a single architectural feature — it's a **3-tier rhetorical apparatus** with each tier serving a different audience-function pair.

## Connections to existing findings

- **Cross-finding-027** (H-NEW-1250) Q 55 dual-audience signature: this finding extends to a 3-surah architecture.
- **H-NEW-1190** *wa-mā adrāka mā* 10-surah cluster: Q 77 is a member of both H-NEW-1190 AND the new refrain top-3. Refrain architecture bridges the *wa-mā adrāka mā* meta-question structure.
- **H-NEW-1200** short-Meccan-tail eschatology meta-cluster (14 surahs): Q 77 is also a member; Q 26 is NOT (it's mid-mushaf Meccan with prophet-cycle structure).
- **H-NEW-90** Q 7 prophet-cycle parallelism z=+5.25: Q 26's 8-pericope refrain-pair is the 2nd corpus-prominent prophet-cycle closure architecture (Q 7 has 7-prophet parallelism without refrain).
- **Cross-finding-013** ring-topology: Q 55 sits at mushaf 55, Q 77 at 77, Q 26 at 26. The 3-tier cluster is mushaf-distributed (front-mid + mid + back-Meccan-edge), NOT clustered. The refrain architecture is a **trans-positional rhetorical axis**, not a positional-cluster axis.
- **al-Suyūṭī** *al-Itqān fī ʿulūm al-Qurʾān* nawʿ on *takrīr* (verify nawʿ-number against on-disk PDF): classical takrīr taxonomy partially anticipates the 3-tier. al-Zarkashī *al-Burhān* discusses the *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān* refrain function in terms of the conscious-acknowledgement schema.

## Honest limits

- **Single statistic tested**: max identical-verse-repeat-count. Alternative refrain-detection statistics (longest-repeated n-gram; pattern-Markov; intra-surah Levenshtein) untested — could promote or demote the top-3 ordering.
- **Saturation outlier Q 109**: ranks #15 by count but #2 by saturation. The current pre-reg's Cell A is count-based; saturation-based ranking is a separate question requiring its own pre-reg (H-NEW-1321 queued).
- **Verdict ceiling = PASS-DIRECTED**: handoff-origin = single planned test family. INDEPENDENT REPLICATION (different operationalization or different feature space) required for promotion to CONFIRMED. Independent replication candidates: longest-repeated 5-token-window, locality-sensitive-hashing of verses.
- **Tashkeel sensitivity**: tested on no-tashkeel only. Min-tashkeel might collapse some near-identical verses; full-tashkeel might split apart vocally-distinct repeats. H-NEW-1321 follow-up could replicate.
- **Q 26's refrain is technically a paired refrain**: the *wa-inna rabbaka la-huwa al-ʿazīzu al-raḥīm* always pairs with a preceding *inna fī dhālika la-āyatan wa-mā kāna aktharuhum muʾminīn*. The current statistic counts only the closing line (8 occurrences). A paired-refrain count would yield 16 paired-event occurrences — a different ranking.

## Replication seeds (NOT yet locked)

- **H-NEW-1321**: longest-repeated 5-token-window per surah, ranked corpus-wide. PC: H-NEW-1320 result itself (back-test).
- **H-NEW-1322**: saturation-axis re-ranking (max_repeat / verse_count). Q 109 likely rank-1 or rank-2 here.
- **H-NEW-1323**: refrain-pattern Markov detection — does the refrain location structure (interval-between-repetitions) follow Poisson or have rhythmic structure?

## Verdict summary

| Quantity | Value |
|:--|--:|
| Q 55 max_repeat_count (observed) | **31** |
| Q 55 rank | **1/114 strict** |
| Q 77 rank | 2/114 |
| Q 26 rank | 3/114 |
| p_perm (any surah ≥ 31) | **0.00000** |
| Null mean max-over-corpus | 2.94 |
| Cell A pass | ✓ |
| Cell B pass | ✓ |
| MW-5 instrument-control | ✓ |
| **Final verdict** | **PASS-DIRECTED FULL** |

The 3-tier refrain architecture {Q 55, Q 77, Q 26} is empirically locked. Q 55's refrain saturation is ~10× the null-expected corpus maximum. The iʿjāz al-takrīr meta-principle is extended from a single Q 55-specific signature to a 3-surah trans-positional rhetorical apparatus.
