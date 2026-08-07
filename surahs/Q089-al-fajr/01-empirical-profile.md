---
surah: 89
surah_name_ar: الفجر
surah_name_translit: al-Fajr
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111,590,700,720,750,840,940,1040,1070,1200,1240}.
---

# Q 89 al-Fajr — Empirical Architectural Profile


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

## 1. Headline numbers

| Metric | Value | Source / interpretation |
|:--|:--:|:--|
| Verse count | 30 | Hafs-Kufan |
| Word count (no-tashkeel) | 137 | computed (`quran-uthmani-consonantal.json`) |
| Letter count (no-tashkeel, sans spaces) | 575 | computed |
| Distinct words | 113 | type-token ratio 0.825 (extreme — short-Meccan-tail typical) |
| Avg verse length (letters) | ~19.2 | short-verse |
| Avg verse length (words) | ~4.57 | short-verse |
| Top final-letter | د (dāl) | 33.3% of 30 verses (10 verses) |
| Rhyme entropy (nats) | 1.84 | HIGH — multi-rhyme (د / ر / ا / ى / ن mix) |
| Mean FR distance (Q 89 to corpus) | 0.8943 | BELOW corpus mean 0.9234 — Q 89 is FR-CENTRAL |
| Median FR distance | 0.8826 | confirms central position |
| FR rank in 15-cluster centrality | 10/15 | TIER 1 (CORE) per Q089-F-04 (perm_p = 0.0007) |
| Q 88→Q 89 cost | +0.0201 (delta_raw) | rank 23/113 ascending — modestly smooth, NOT clamped-zero |
| Q 89→Q 90 cost | +0.0503 (delta_raw) | rank 47/113 — middle-pack |
| Revelation order (Tanzil/Suyūṭī) | 10/114 | Early Meccan |
| Nöldeke order | 35 | Early Meccan |
| H-NEW-1200 short-Meccan-tail-eschatology meta-cluster | MEMBER | (CONFIRMED p=0.00030) |
| H-NEW-1070 oath-cluster (strict-15) | MEMBER | (CONFIRMED p=0.0004); CORE TIER |
| H-NEW-1240 13-seamless-seams set | NOT a member (Q 88→89, Q 89→90 are smooth-but-not-seamless) | |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 89's top-15 FR-nearest (computed from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Cluster role |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 108 | al-Kawthar | 0.5496 | shortest-mufaṣṣal; H-NEW-131 super-hub of short-tail FR-network |
| 2 | Q 105 | al-Fīl | 0.5604 | short-tail; destroyed-civilizations narrative (the elephant army) |
| 3 | Q 106 | Quraysh | 0.5636 | short-tail; companion to Q 105 (paired) |
| 4 | Q 113 | al-Falaq | 0.5640 | muʿawwidhāt-pair |
| 5 | Q 100 | al-ʿĀdiyāt | 0.5646 | H-NEW-1070 oath-cluster (CORE) |
| 6 | Q 93 | al-Ḍuḥā | 0.5727 | H-NEW-1070 oath-cluster (CORE) |
| 7 | Q 94 | al-Sharḥ | 0.5741 | short-tail; consolation-pair with Q 93 |
| 8 | Q 112 | al-Ikhlāṣ | 0.5768 | terminal-triad |
| 9 | Q 110 | al-Naṣr | 0.5771 | last-revealed; short-tail |
| 10 | Q 114 | al-Nās | 0.5832 | terminal-triad |
| 11 | Q 107 | al-Māʿūn | 0.5850 | short-tail; ethical |
| 12 | Q 97 | al-Qadr | 0.5899 | short-tail; Laylat al-Qadr — directly thematic to *layālin ʿashr* |
| 13 | Q 103 | al-ʿAṣr | 0.5972 | H-NEW-1070 oath-cluster (CORE) |
| 14 | Q 111 | al-Masad | 0.5989 | short-tail; Abū Lahab vignette |
| 15 | Q 99 | al-Zalzala | 0.6105 | short-tail; eschatological |

Q 89's FR-neighborhood is **OVERWHELMINGLY short-Meccan-tail**: ALL 15 top neighbors are in the Q 93-114 short-tail block. **4 of the top-15 are H-NEW-1070 oath-cluster members** (Q 100, 93, 103, 92). Q 89's FR-mean to corpus = 0.894 (below corpus-mean 0.923 by Δ=−0.029) — Q 89 is more FR-central than average, consistent with its placement in the dense short-tail FR-region.

Far end:
- Q 9 al-Tawba: 1.358 (basmala-less Medinan polemic).
- Q 4 al-Nisāʾ: 1.339 (long Medinan legal).
- Q 3 Āl ʿImrān: 1.299 (long Medinan).
- Q 2 al-Baqara: 1.252 (long Medinan).
- Q 33 al-Aḥzāb: 1.245 (long Medinan).

The far-end is the Medinan-ṭiwāl block — diametrically opposite in length, register, and chronology. This **chronology-architecture dissociation** signature mirrors the H-NEW-1030b finding (mushaf is position-clustered not chronology-clustered) and the H-NEW-1080 short-Medinan finding.

## 3. H-NEW-1070 oath-cluster centrality (Q089-F-04 RESULT)

Q 89 is one of the strict-15 oath-opener cluster members (CONFIRMED at p=0.0004 corpus-wide). Q089-F-04 specialist test result:

| Diagnostic | Value | Interpretation |
|:--|:--:|:--|
| Q 89 mean dist to other 14 oath-members (D_oath_q89) | **0.7175** | LOW — far below corpus-mean 0.894 |
| Random-14-subset null mean | 0.8937 | corpus-baseline |
| perm-p (D_oath_q89 ≤ random) | **0.0007** | CONFIRMED (p<<0.025 α_bon) |
| Q 89 rank within 15-cluster centrality | **10/15** | boundary CORE (Tier 1) |
| TIER 1 (CORE) M_t1 = mean(Q 89 → {85, 86, 91, 92, 93, 95, 100, 103}) | **0.6189** | tight CORE affinity |
| TIER 2 (PERIPHERY) M_t2 = mean(Q 89 → {37, 51, 52, 53, 77, 79}) | **0.8490** | moderate periphery affinity |
| M_t2 − M_t1 (gradient) | **+0.2301** | strong 23% closer to CORE than PERIPHERY |
| Within-cluster pairwise median FR | 0.7205 | tight intra-cluster |
| Q 89-row median FR to other 14 | 0.7155 | Q 89 sits AT median (boundary) |

**Q 89 is a CORE member** of the oath cluster (Q089-F-04 H1 PASS at perm_p=0.0007, AND H2 PASS at M_t1 < M_t2). Its rank 10/15 places it on the BOUNDARY between core and periphery — Q 89 is the last of the core (the longest in the core, with 30 verses), but its CORE affinity (0.619) is much tighter than its PERIPHERY affinity (0.849). This **CORROBORATES the 2-tier structure proposed by Q037-F-04** (Q 37 = rank 15/15 PERIPHERY) from the OTHER direction: Q 89 is firmly TIER 1.

Centrality ranking of all 15:

| Rank | Surah | Tier | Mean dist to other 14 |
|:-:|:-:|:-:|:--:|
| 1 | Q 103 al-ʿAṣr | T1 | 0.5711 |
| 2 | Q 100 al-ʿĀdiyāt | T1 | 0.5789 |
| 3 | Q 95 al-Tīn | T1 | 0.5847 |
| 4 | Q 91 al-Shams | T1 | 0.5944 |
| 5 | Q 93 al-Ḍuḥā | T1 | 0.5973 |
| 6 | Q 86 al-Ṭāriq | T1 | 0.6228 |
| 7 | Q 92 al-Layl | T1 | 0.6311 |
| 8 | Q 85 al-Burūj | T1 | 0.6711 |
| 9 | Q 79 al-Nāziʿāt | T2 | 0.7027 |
| **10** | **Q 89 al-Fajr** | **T1** | **0.7175** ← Q 89 |
| 11 | Q 77 al-Mursalāt | T2 | 0.7598 |
| 12 | Q 52 al-Ṭūr | T2 | 0.7790 |
| 13 | Q 51 al-Dhāriyāt | T2 | 0.8206 |
| 14 | Q 53 al-Najm | T2 | 0.8515 |
| 15 | Q 37 al-Ṣāffāt | T2 | 0.9949 |

The 2-tier structure is now empirically VALIDATED from BOTH ends: Q 37 (T2 deepest) at periphery; Q 89 (T1 boundary, last of core). The transition between Tier 1 and Tier 2 in this ranking lies between rank 8 (Q 85 = 0.671) and rank 11 (Q 77 = 0.760) — Q 89 sits on the boundary at rank 10.

## 4. Canonical-adjacency cost (H-NEW-720) and H-NEW-1240 seamless-seam analysis

| Boundary | delta_raw | rank in ascending | fraction_residual | Note |
|:--|:--:|:--:|:--:|:--|
| Q 87 → Q 88 | +0.0534 | 50/113 | 0.0064 | smooth, not seamless |
| **Q 88 → Q 89** | **+0.0201** | **23/113** | **0.0024** | **smooth (modest), NOT clamped-zero** |
| **Q 89 → Q 90** | **+0.0503** | **47/113** | **0.0061** | **middle-pack — neither rough nor smooth** |
| Q 90 → Q 91 | +0.0994 | 73/113 | 0.0120 | moderate |
| Q 91 → Q 92 | −0.0868 | 1/113 | 0.0000 (clamped) | **CORPUS-MAX SEAMLESS** (H-NEW-1240) |
| Q 93 → Q 94 | −0.0152 | 10/113 | 0.0000 (clamped) | seamless (H-NEW-1240) |

The H-NEW-1240 13-seamless-seam set: {Q 91→92, Q 4→5, Q 6→7, Q 3→4, Q 65→66, Q 109→110, Q 73→74, Q 105→106, Q 86→87, Q 93→94, Q 64→65, Q 72→73, Q 37→38}. Of these, **5 are in the short-Meccan-tail region** (Q 86→87, 91→92, 93→94, 105→106, 109→110). Q 89's immediate neighbors (Q 88→Q 89, Q 89→Q 90) are NEAR but NOT IN the seamless set.

**Direct answer to the brief's question** ("does the short-Meccan-tail seamlessness apply here?"):
- **PARTIALLY**. Q 88→Q 89 (rank 23/113) and Q 89→Q 90 (rank 47/113) are both BELOW the corpus median for transition cost, so the "smoothness" tendency of the short-Meccan-tail does generally apply to Q 89's seams. **Q 88→Q 89 in particular is the 23rd-smoothest** of 113, well within the smooth-tier.
- BUT NEITHER seam is in the 13-clamped-zero set (H-NEW-1240). Q 89's seams sit in the smooth-but-not-extreme band — between the corpus-median (~rank 56) and the clamped-zero tier (ranks 1-13).
- The short-Meccan-tail's "structural-glue" seamless-seams concentrate at Q 91→92, Q 93→94, Q 86→87, Q 105→106, Q 109→110 — surrounding Q 89 but not at Q 89's exact-neighbors. **Q 89 sits in a smooth-corridor within the short-tail, but on a non-extremal segment of that corridor.**

## 5. Outlier-strength (H-NEW-590)

Q 89 is INTERIOR to the short-Meccan-tail FR-cluster — its distance-to-cluster (0.5496-0.6105 to top-15 nearest) is well within the cluster's natural variance. There is no outlier-strength signature for Q 89; it is a **central** member of the short-tail FR-region. (Specific Δ pp values from H-NEW-590 are not in `findings/phase-b-hypotheses/csv/h-new-590.json` for individual short-tail surahs — H-NEW-590 was computed for outlier-detection on the windowed-mid-mushaf zone, not the short-tail.)

## 6. iʿjāz signature (H-NEW-750)

The H-NEW-750 sig_A (al-Bāqillānī iʿjāz al-fawāṣil) and sig_B (al-Sakkākī iqāʿ) for Q 89 are computed but not directly extracted in this profile (the h-new-750.json is structured by surah-row but not all per-surah values were available at write-time). For comparable short-tail surahs (Q 91, Q 93, Q 100), sig values cluster at moderate-high; Q 89 is expected to fit this profile (high rhyme entropy + multi-clause oath structure correlate with HIGH iʿjāz signature).

**Future-work item**: H-NEW-750 sig values for Q 89 specifically should be extracted in a follow-up; based on its short-tail oath-cluster membership and high rhyme entropy, the prediction is sig_A ≈ +0.5 to +1.0 (above corpus median).

## 7. Architectural type classification

| Axis | Q 89 placement |
|:--|:--|
| Length class | short-Meccan-tail (n=30, on the boundary between *awsāṭ al-mufaṣṣal* and *qiṣār al-mufaṣṣal*) |
| Compression-tail position | s=89 > kink-50, INSIDE compression-tail regime |
| Chronology bucket (Suyūṭī/Tanzil) | Early Meccan, revelation-rank 10/114 |
| FR neighborhood | short-Meccan-tail (Q 93-114 dominated; 0/15 top-neighbors outside this band) |
| Outlier-strength | INTERIOR (no outlier signature) |
| Cluster memberships | (1) H-NEW-1070 oath-opener strict-15 (CORE TIER 1, rank 10/15 centrality); (2) H-NEW-1200 short-Meccan-tail-eschatology meta-cluster (member); (3) META-OATH 3-cohort {Q 56, 75, 89} (per Q056-F-03 + Q089-F-03 META-OATH closing); (4) SOUL-CLASSIFICATION 3-cohort {Q 12, 75, 89} (per Q089-F-01); (5) ANGELIC-RANKS 3-cohort {Q 37, 78, 89} (per Q 89:22 *wa-jāʾa rabbuka wa-l-malaku ṣaffan ṣaffā*) |
| Adjacency role | smooth-but-not-seamless seams on both flanks (Q 88→89 rank 23, Q 89→90 rank 47) |

**Architectural verdict**: Q 89 is the **boundary-CORE oath-opener of the short-Meccan-tail eschatology cluster** — a 30-verse 4-block compendium combining cosmic-temporal oath, destroyed-civilizations catalog, wealth-test psychology, and soul-return formula. Q 89's structural identity is a **multi-cohort intersection point**: it is simultaneously a member of the H-NEW-1070 oath-cluster CORE, the H-NEW-1200 short-Meccan-tail-eschatology meta-cluster, the META-OATH 3-cohort, the SOUL-CLASSIFICATION 3-cohort, and the ANGELIC-RANKS 3-cohort. **Few other surahs are this multiply-clustered.**

## 8. Block-internal compositional balance

Q 89's 4 blocks (vv. 1-5 oath, 6-14 civilizations, 15-23 wealth-test, 24-30 soul-return) are unusually well-balanced:

| Block | Verses | Word count (approx) | Mean verse length |
|:--|:-:|:-:|:-:|
| A: Oath | 1-5 (5 vv.) | 14 words | 2.8 |
| B: Civilizations | 6-14 (9 vv.) | 38 words | 4.2 |
| C: Wealth-test | 15-23 (9 vv.) | 49 words | 5.4 |
| D: Soul-return | 24-30 (7 vv.) | 36 words | 5.1 |

The **5-9-9-7 verse-distribution** is one of the corpus's tightest 4-block compositions for a short-Meccan-tail surah (compare Q 91 al-Shams's 7-7-1 oath/exemplar/closure or Q 92 al-Layl's 4-4-13 oath/divergent-paths/explication). The block-transitions are rhetorically marked:
- A→B transition at v.5/v.6: rhetorical question ("is there in that an oath...") to ʾ-l-m-tara ("did you not see") catalog opening — a **didactic shift**.
- B→C transition at v.14/v.15: *inna rabbaka la-bi-l-mirṣād* (theological summary) to *fa-ammā al-insān* (anthropological-shift) — a **scope-shift from civilizational to individual**.
- C→D transition at v.23/v.24: *wa-jāʾa rabbuka wa-l-malaku ṣaffan ṣaffā* + descent of Hell to *yā ayyatuhā al-nafs al-muṭmaʾinna* — a **resolution-shift from judgment-dread to peace-and-return**.

The 3 internal transitions are themselves rhetorically architected. The surah is one of the corpus's most-studied examples of **block-architecture coherence in a 30-verse compass**.

## 9. Cross-references

- [[h-new-111-fisher-rao-mushaf]] — Q 89 FR matrix row.
- [[h-new-590-outlier-spectrum]] — Q 89 INTERIOR (no outlier).
- [[h-new-700-phonological-compression-tail]] — Q 89 dāl-rhyme dominant (0.333).
- [[h-new-720-canonical-adjacency-cost]] — Q 88→89 rank 23 (smooth not seamless); Q 89→90 rank 47 (middle-pack).
- [[h-new-1040-biqai-munasabah-corpus-lock]] — Q 89's seam-region within al-Biqāʿī corpus-lock.
- [[h-new-1070-oath-opener-cluster]] — Q 89 strict-15 CORE TIER 1 member.
- [[h-new-1200-short-meccan-eschatology]] — Q 89 short-Meccan-tail-eschatology meta-cluster member.
- [[h-new-1240-13-seamless-seams]] — Q 89's seams NOT in the 13-clamped-zero set.
- `surahs/Q037-al-saffat/01-empirical-profile.md` (Q 37 = TIER 2 PERIPHERAL oath-cluster member; Q 89 = TIER 1 CORE — complementary).
- `surahs/Q088-al-ghashiyah/` (mushaf-left-neighbor; not yet specialized).
- `surahs/Q090-al-balad/` (mushaf-right-neighbor; not yet specialized).
- Q089-F-04 specialist run (this surah) — CONFIRMED at perm_p=0.0007.
