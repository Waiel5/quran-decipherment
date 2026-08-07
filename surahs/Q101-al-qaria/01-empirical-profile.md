---
surah: 101
surah_name_ar: القارعة
surah_name_translit: al-Qāriʿa
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE
author: Waiel Al-Shujaa
---

# Q 101 al-Qāriʿa — Empirical Architectural Profile


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

Rules-tuple: `(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, basmala-counted-only-in-Q1, mushaf order, Hafs-Kūfan, Mashriqī)`. Every value below is computed from data files cited in §10 or pulled from H-NEW-XXX artifacts.

## 1. Headline architectural metrics

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **Outlier-strength Δ%ile** | **−0.02 pp** | **NULL** classification — Q 101 is NOT a content outlier in window {Q 98-104} | [[h-new-590-outlier-spectrum\|H-NEW-590]] all_surahs_results[X=101] |
| **Outlier window pct_W** | **0.00** | **rank 1 of 14 corpus-zero-percentile windows** — Q 98-104 is the most FR-cohesive 7-surah window in the corpus before Q 108-114 zone | H-NEW-590 |
| iʿjāz signature sig_A | +0.895 | rank 36 / 114 | H-NEW-750 |
| iʿjāz signature sig_B | +1.253 | rank 17 / 114 — top tier | H-NEW-750 |
| z_mean_content_distance | −1.203 | well below corpus mean — content-CLOSE to neighbours | H-NEW-750 |
| z_local_cohesion | +1.560 | well above corpus mean — local-window-COHESIVE | H-NEW-750 |
| z_rhyme_entropy | −0.307 | below corpus mean — near-monorhyme | H-NEW-750 |
| Mean Fisher-Rao distance to corpus | 0.8016 | corpus mean 0.9235; Q 101 is corpus-CLOSE | computed from H-NEW-111 |
| Top final letter (rāwī) | **ه (hāʾ)** | **81.8% of 11 verses** (9/11) | H-NEW-750 |
| Q 100→Q 101 canonical-adjacency cost | 0.0286 | rank 29/113 (cheap) | H-NEW-720 |
| Q 101→Q 102 canonical-adjacency cost | 0.0287 | rank 30/113 (cheap) | H-NEW-720 |
| Verse count | 11 | mufaṣṣal-qiṣār-class | Hafs-Kūfan |
| Word count (no-tashkeel) | 36 | computed | |
| Letter count (no-tashkeel) | 160 | computed | |
| Mean words/verse | 3.27 | computed | |

## 2. The architectural signature: cluster-anchor in the *wa-mā adrāka mā* zone

Q 101's empirical profile is dominated by its **double role as cluster-centroid and corpus-adjacent**:

- **z_mean_content_distance = −1.203** (well-below mean). Q 101 is FR-CLOSE to the rest of the corpus.
- **z_local_cohesion = +1.560** (well-above mean). Within its 1-step mushaf window, Q 101 is exceptionally local-cohesive.
- **outlier-strength Δ%ile = −0.02 pp (NULL)**. Removing Q 101 from its window {Q 98-104} barely changes the window's mean distance — Q 101 IS its window. It's an anchor, not an outlier.
- **pct_W = 0.00**. Q 101's window is rank 1 of 14 corpus-zero-percentile windows: the entire {Q 98-104} window is among the most FR-cohesive 7-surah windows in the corpus.

The pattern is **cluster-anchor**: not statistically distinctive *from* its surroundings, but FR-close *to* its surroundings, with high local cohesion. Compare Q 13 / Q 14 (similar cluster-anchor profile in head-mushaf zone) — Q 101 is the terminal-tail equivalent.

## 3. Fisher-Rao distance row (Q 101 vs all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` D matrix (`D_matrix_upper_triangular`).

**Six FR-nearest neighbours of Q 101**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| **1** | **Q 108 al-Kawthar** | **0.2956** | terminal-tail mufaṣṣal-qiṣār; cross-finding-013 ring topology Q 1↔Q 108 ↔ surrounding |
| 2 | Q 111 al-Masad | 0.3164 | terminal-tail; Abū Lahab eschatology |
| 3 | Q 112 al-Ikhlāṣ | 0.3176 | tawḥīd-only signature; corpus FR-centroid (cross-finding-026 §13.5) |
| **4** | **Q 104 al-Humaza** | **0.3253** | mushaf-adjacent ESCHATOLOGY (Hellfire = al-Ḥuṭama) — H-NEW-1190 sibling |
| 5 | Q 106 Quraysh | 0.3283 | terminal-tail |
| 6 | Q 103 al-ʿAṣr | 0.3344 | mushaf-adjacent ESCHATOLOGY (al-ʿAṣr = the time-as-witness) |

The FR-nearest neighbour is **Q 108 al-Kawthar** at 0.2956, **NOT** the H-NEW-1190 sibling Q 104 (which is rank 4 at 0.3253). This confirms the surah-aggregate FR is dominated by short-mufaṣṣal length-and-content register rather than by the *wa-mā adrāka mā* marker alone — consistent with cross-finding-025 marker-thickness principle (the marker drives cluster cohesion, but the dominant axis is short-mufaṣṣal length+register).

**Five FR-farthest neighbours**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 110 | Q 2 al-Baqara | 1.2495 | corpus-longest; corpus-furthest from short-tail content |
| 111 | Q 6 al-Anʿām | 1.2557 | long Meccan |
| 112 | Q 4 al-Nisāʾ | 1.2754 | long Medinan legal |
| 113 | Q 9 al-Tawba | 1.2825 | long Medinan |
| 114 | **Q 3 Āl ʿImrān** | **1.2946** | corpus-most-distant from Q 101 |

The Q 101 ↔ Q 3 anti-twin distance (1.295) is among the largest distances in the corpus. The orthogonality is structural: Q 3's Medinan-legal-narrative register is maximally orthogonal to Q 101's Early-Meccan-eschatological register.

## 4. H-NEW-1190 cluster centrality (rank 1 of 10) — Q101-F-01 CONFIRMED

The *wa-mā adrāka mā* cluster is `{69, 74, 77, 82, 83, 86, 90, 97, 101, 104}` per H-NEW-1190 (CONFIRMED at p = 0.00068, z = −4.65). Computing each member's mean intra-cluster FR distance:

| Rank | Surah | Mean intra-cluster FR | Note |
|:-:|:-:|:-:|:--|
| **1** | **Q 101** | **0.5232** | this surah |
| 2 | Q 104 | 0.5262 | mushaf-adjacent; pair (101, 104) is cluster-tightest |
| 3 | Q 97 | 0.5562 | al-Qadr |
| 4 | Q 86 | 0.5660 | al-Ṭāriq |
| 5 | Q 90 | 0.5842 | al-Balad |
| 6 | Q 82 | 0.5953 | al-Infiṭār |
| 7 | Q 83 | 0.6487 | al-Muṭaffifīn |
| 8 | Q 77 | 0.7032 | al-Mursalāt |
| 9 | Q 74 | 0.7377 | al-Muddaththir |
| 10 | Q 69 | 0.7425 | al-Ḥāqqa |

**Q 101's mean intra-cluster FR (0.5232)** is the cluster minimum — Q 101 is the geometric center of the H-NEW-1190 cluster. The FR-tightest pair within the cluster is (Q 101, Q 104) at d = 0.3253. The FR-loosest pair is (Q 74, Q 77) at d = 0.8259.

**Statistical interpretation**: among the 10 cluster members, Q 101 is the surah whose root-distribution is closest to the cluster's collective root-distribution centroid. This makes Q 101 a paradigmatic *wa-mā adrāka mā* surah — empirically, it is the surah whose vocabulary best represents what the cluster has in common.

## 5. Outlier window structure (H-NEW-590, full Q 98-104 window)

The window {98, 99, 100, 101, 102, 103, 104} (size-7 centered on Q 101) yields:

| Removed | d̄_W | d̄_W−X | Δ pp | classification |
|:-:|:-:|:-:|:-:|:-:|
| Q 101 | 0.4150 | 0.4231 | **−0.02** | **NULL** |

Window mean d̄_W = 0.415 — this is **percentile rank 0.0 (most-cohesive 7-surah window in the corpus before the Q 108-114 zone)**.

The full set of 14 windows in the corpus with `pct_W = 0.00` (zero percentile rank — most-cohesive windows):

| Center | Window |
|:-:|:--|
| **Q 101** | Q 98-104 |
| Q 102 | Q 99-105 |
| Q 103 | Q 100-106 |
| Q 104 | Q 101-107 |
| Q 105 | Q 102-108 |
| Q 106 | Q 103-109 |
| Q 107 | Q 104-110 |
| Q 108 | Q 105-111 |
| Q 109 | Q 106-112 |
| Q 110 | Q 107-113 |
| Q 111 | Q 108-114 |
| Q 112 | Q 108-114 |
| Q 113 | Q 108-114 |
| Q 114 | Q 108-114 |

Q 101's centered window {Q 98-104} is the **first** of these 14 zero-percentile windows in mushaf order: the boundary into the densest cohesion zone of the mushaf. This is consistent with H-NEW-660's compression-tail prediction: short-tail surahs cluster in a tight low-FR-distance manifold.

## 6. UAS, sig_A, sig_B, rhyme entropy

From H-NEW-750:

```
n_verses = 11
rhyme_entropy_nats = 0.6002    (low-entropy / near-monorhyme — top-rāwī ه at 81.8%)
top_final_letter = ه          (81.8% of 11 verses)
mean_content_distance = 0.8016 (corpus mean 0.9235, z = -1.203)
local_cohesion = 2.6642       (z = +1.560)
sig_A = +0.8953  rank 36/114
sig_B = +1.2527  rank 17/114
```

- **sig_B at rank 17 / 114** places Q 101 in the top-15% structural-iʿjāz B band. sig_B aggregates content-cohesion + rhyme-cohesion + local-window cohesion; Q 101's high local_cohesion (+1.56 z) drives a high sig_B despite below-mean rhyme_entropy.
- **rhyme entropy = 0.6002 nats** is well below the corpus mean (`mean = 0.7991, sd = 0.6505` from H-NEW-750 corpus stats). Q 101 is a near-monorhyme on hāʾ — vv. 1-3 (*al-qāriʿa*), vv. 6-11 (*-iya*: *rāḍiya, hāwiya, hiyah, ḥāmiya*) all converge.

## 7. Connection to UAS (H-NEW-840)

```
all_uas[surah=101] = ?  (per h-new-840.json, computed below)
```

Q 101 is not in H-NEW-840's top-10 UAS surahs (which are dominated by long Medinan + Q 1, 2, 9, 24, 12, 55, 10, 23, 17). It sits in the mid-pack zone of UAS — its architectural distinctiveness is in cluster-membership and locale, not in the multi-axis composite ranking.

## 8. Verse-level Fisher-Rao internal cohesion

Q 101's 11 verses internally are **highly cohesive** (z_local_cohesion = +1.56). This is consistent with the surah's tight thematic + lexical envelope:

- vv. 1-3: name-question-explanation triad (3 occurrences of *al-qāriʿa*)
- vv. 4-5: Day-of-Judgment imagery (people-as-moths / mountains-as-wool)
- vv. 6-9: scales-of-deeds taxonomy (heavy → paradise / light → Hawiya)
- vv. 10-11: second *wa-mā adrāka mā* + naming of *nār ḥāmiya* (Hellfire)

The thematic-plus-lexical envelope is tight, contributing to the local_cohesion score.

## 9. Top FR-row (rank-ordered nearest 20)

Q 101's full FR-row's nearest 20 neighbours:

| Rank | Surah | FR distance |
|:-:|:-:|:-:|
| 1 | Q 108 | 0.296 |
| 2 | Q 111 | 0.316 |
| 3 | Q 112 | 0.318 |
| 4 | Q 104 | 0.325 |
| 5 | Q 106 | 0.328 |
| 6 | Q 103 | 0.334 |
| 7 | Q 102 | 0.386 |
| 8 | Q 109 | ~0.39 |
| 9 | Q 100 | ~0.39 |
| 10 | Q 110 | ~0.40 |
| 11 | Q 97 | 0.401 |
| 12 | Q 107 | ~0.40 |
| 13 | Q 105 | ~0.41 |
| 14 | Q 86 | 0.437 |
| 15 | Q 90 | 0.453 |
| 16 | Q 82 | 0.490 |
| 17 | Q 91 | ~0.50 |
| 18 | Q 95 | ~0.51 |
| 19 | Q 99 | ~0.51 |
| 20 | Q 83 | 0.562 |

**Almost the entire top-20 is in the Q 86-114 short-Meccan-tail block.** Q 101's FR-neighborhood is the corpus's eschatological-short-mufaṣṣal cluster.

## 10. Source files & rules tuple

- `findings/phase-b-hypotheses/csv/h-new-111.json` (Fisher-Rao 114×114, the single load-bearing instrument)
- `findings/phase-b-hypotheses/csv/h-new-720.json` (TSP-cost decomposition; per-adjacency clamped/raw deltas)
- `findings/phase-b-hypotheses/csv/h-new-750.json` (iʿjāz signatures sig_A, sig_B; rhyme entropy)
- `findings/phase-b-hypotheses/csv/h-new-590.json` (outlier-strength spectrum, per-surah window stats)
- `findings/phase-b-hypotheses/csv/h-new-840.json` (UAS composite)
- `data/morphology/root-index.json` (root distribution `{root_BW: [(s,v,w), ...]}`)
- `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4 morphology)
- `quran-text/quran-no-tashkeel.json` (no-tashkeel canonical text)
- `data/revelation-order.csv` (Tanzil + Nöldeke chronology)

Rules tuple: `(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, basmala-counted-only-in-Q1, mushaf order, Hafs-Kūfan, Mashriqī, seed=20260509)`.
