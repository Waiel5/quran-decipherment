---
surah: 34
surah_name_ar: سبإ
surah_name_translit: Sabaʾ
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111, 130, 590, 700, 720, 750, 840}.
---

# Q 34 Sabaʾ — Empirical Architectural Profile


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
| Verse count | 54 | Hafs-Kūfan |
| Word count (no-tashkeel, basmala-excluded) | 887 | computed |
| Letter count (no-tashkeel, Arabic-letters-only, basmala-excluded) | 3,594 | computed |
| Avg verse length (letters) | 66.6 | medium-long Late-Meccan |
| Avg verse length (words) | 16.4 | medium-long Late-Meccan |
| Top final-letter | ن (nūn) | 40.7% of 54 verses (`h-new-700.json`) |
| Rhyme entropy (nats) | 1.5596 | rank 86/114 — mid-high (NOT near-monorhyme) |
| Mean content distance (FR) | 0.9877 | `h-new-750.json`; rank 82/114 |
| Local cohesion (window) | 1.0815 | `h-new-750.json`; rank 33/114 |
| iʿjāz sig_A | 0.7962 | rank 75/114 — MID al-Bāqillānī iʿjāz al-fawāṣil signal |
| iʿjāz sig_B | 0.8351 | rank 80/114 — MID al-Sakkākī iqāʿ signal |
| UAS | 1.6049 | rank **18/114** — UPPER-tier unified architectural significance |
| Outlier-strength delta_pct | -4.70 pp | NULL (window {Q 31-37}); p_greater = 0.3061 |
| Q 33 → Q 34 cost | +0.3311 (frac_residual 0.0399) | rank **111/113** — VERY rough seam (Medinan→Late-Meccan) |
| Q 34 → Q 35 cost | +0.0745 (frac_residual 0.0090) | rank **65/113** — moderate (NOT clamped-zero seamless) |
| H-NEW-130 Q 33-34 in boundary set | YES | period_Medinan_to_Meccan; phase_Medinan_to_Late_Meccan |
| H-NEW-130 Q 34-35 in boundary set | NO | no structural-boundary marker |
| sabaʾ proper-noun count (LEM:saba<) | 1 (Q 34:15) | corpus-total 2 (other in Q 27:22) |
| al-ḥamdu li-llāh opener | YES | 1 of 5 in {Q 1, 6, 18, 34, 35} |
| Dual-ḥamd verse | Q 34:1 | corpus-UNIQUE (only verse with 2 occurrences of *al-ḥamd*) |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 34's top-10 nearest in FR space (decoded from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 41 | Fuṣṣilat | 0.8021 | Late-Meccan ḥawāmīm cluster |
| 2 | Q 46 | al-Aḥqāf | 0.8058 | Late-Meccan ḥawāmīm cluster |
| 3 | Q 32 | al-Sajda | 0.8232 | Mid-Meccan الم creedal-narrative |
| 4 | Q 36 | Yāsīn | 0.8331 | Mid-Meccan single-letter muqaṭṭāʿat |
| 5 | Q 10 | Yūnus | 0.8548 | Late-Meccan الر prophet-narrative |
| 6 | Q 25 | al-Furqān | 0.8599 | Late-Meccan creedal |
| 7 | Q 67 | al-Mulk | 0.8622 | Late-Meccan kingdom-theology |
| 8 | Q 45 | al-Jāthiyah | 0.8648 | Late-Meccan ḥawāmīm cluster |
| 9 | Q 17 | al-Isrāʾ | 0.8654 | Late-Meccan creedal |
| 10 | Q 27 | al-Naml | 0.8661 | **Sabaʾ-narrative pair (mutual top-10)** |

Q 34's FR-neighborhood is **Late-Meccan-creedal-omniscience-band**: 4 of the top-10 are ḥawāmīm-adjacent (Q 41, Q 46, Q 45, indirectly Q 25/Q 17), 1 is the Sabaʾ-narrative pair (Q 27), and the rest are creedal-narrative Late-Meccan companions. Q 34 mean distance to all 113 = **0.9877** (slightly above corpus mean 0.9226 — Q 34 is mildly content-distinct).

**Far end (Q 34's most-distant neighbors):**
- Q 9 al-Tawbah: ~1.16+ (basmala-less Medinan polemic)
- Q 33 al-Aḥzāb: 1.1154 (the immediate-mushaf-left-neighbor; rank 109 of 113 — among Q 34's MOST-distant neighbors)
- Q 1 al-Fātiḥa: 1.0354 (despite shared al-ḥamdu li-llāh opener, content-distant)

**Notable**: the al-ḥamdu li-llāh cluster {Q 1, 6, 18, 34, 35} is NOT FR-cohesive at the group level. Q 34's distances to its supposed cluster-mates:
- Q 1: 1.0354 (distant)
- Q 6: 0.8905 (moderate — Q 6 is Q 34's rank ~14)
- Q 18: 0.8984 (moderate — Q 18 is Q 34's rank ~15)
- Q 35: 0.9268 (moderate — Q 35 is Q 34's rank ~28, NOT immediate)

The cluster mean within-pair FR = **0.9902** vs corpus all-pair mean 0.9226 — the al-ḥamdu li-llāh cluster is **anti-cohesive** (per Q034-F-01).

## 3. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json` `all_surahs_results`:

| Field | Value |
|:--|:--:|
| Window | {Q 31, 32, 33, **34**, 35, 36, 37} |
| d_W (window dispersion) | 0.9687 |
| d_W − Q 34 | 0.9826 |
| pct_W | 69.39 |
| pct_W − Q 34 | 74.09 |
| delta_pct | **−4.70** (NEGATIVE) |
| p_greater_W | 0.3061 |
| Classification | **NULL** |

Q 34 is **NOT a content-outlier** — removing Q 34 from its 7-surah window slightly INCREASES the dispersion (delta_pct = −4.70). Q 34 is content-similar to its neighborhood (driven by the Q 32, Q 36, Q 41-46 ḥawāmīm-adjacent block). Q 34 is one of the more *content-cohesive-with-its-mushaf-neighborhood* members of the late-Meccan band, not an outlier.

## 4. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Rank |
|:--|:--:|:--:|:--:|
| Rhyme entropy (nats) | 1.5596 | +1.430 | rank 86/114 (HIGHER than median = more diverse) |
| Mean content distance | 0.9877 | +0.634 | rank 82/114 |
| Local cohesion | 1.0815 | -0.595 | rank 33/114 |
| sig_A (rhyme-content anti-correlation) | 0.7962 | — | rank 75/114 (MID) |
| sig_B (iqāʿ rhythmic-semantic) | 0.8351 | — | rank 80/114 (MID) |

Q 34 is **MID** on both iʿjāz axes. al-Bāqillānī's iʿjāz al-fawāṣil reading (which the corpus-anti-twin-correlation r ≈ -0.86 instantiates) places Q 34 in the middle band. This is consistent with the surah being a **late-Meccan creedal-narrative compendium with mid-density rhetorical structure**, not a fawāṣil-engineered showcase like Q 55 al-Raḥmān (anti-twin extreme) or Q 91 al-Shams (high-iʿjāz density).

## 5. Canonical-adjacency cost (H-NEW-720)

| Boundary | delta_raw | fraction_residual | Rank | Note |
|:--|:--:|:--:|:--:|:--|
| Q 33 → Q 34 | +0.3311 | 0.0399 | **111/113** | VERY rough — Medinan-Late-Meccan period boundary; one of the LEAST-smooth adjacencies in the entire mushaf |
| Q 34 → Q 35 | +0.0745 | 0.0090 | **65/113** | moderate; NOT clamped-zero seamless despite shared opener |

**Q 33 → Q 34 is rank 111 of 113** — only Q 9 → Q 10 (the basmala-less Medinan-Late-Meccan polemic-narrative seam) and Q 5 → Q 6 (very-long-Medinan to long-Late-Meccan) are rougher. The Q 33 → Q 34 roughness is driven by:
- **Period boundary**: Q 33 is Medinan (Hijri-period 5+; battle of the Trench, family-of-the-Prophet legislation), Q 34 is Late-Meccan (pre-Hijri; eschatology + tawḥīd polemic).
- **Genre boundary**: Q 33 is legal/social (marriage rules, ḥijāb, adoption-rules); Q 34 is creedal-narrative (Sabaʾ-flood + universal prophecy).
- **Length asymmetry**: Q 33 = 73 verses (long-Medinan); Q 34 = 54 verses (medium-Late-Meccan).
- H-NEW-130 confirms: Q 33-34 IS in the structural boundary set (period_Medinan_to_Meccan + phase_Medinan_to_Late_Meccan).

**Q 34 → Q 35 is rank 65 of 113** — moderate. Despite the shared al-ḥamdu li-llāh opener, the seam is NOT clamped-zero (delta_raw = +0.0745 > 0; fraction_residual = 0.0090). This empirically demonstrates that **opener-form parallelism does not guarantee FR seamlessness**: Q 34 and Q 35 share opening template but their content distributions diverge enough that the canonical adjacency is improvable by ~0.9% under 2-opt local search. H-NEW-130 places NO structural-boundary marker between Q 34 and Q 35; the seam is moderate-but-not-trivial. See Q034-F-04 for the full seam diagnostic.

## 6. Architectural-significance ranking (H-NEW-840)

UAS (unified architectural score) for Q 34:

| Field | Value |
|:--|:--:|
| UAS | 1.6049 |
| Rank | **18/114** (upper tertile) |
| abs_outlier component | 4.700 |
| max_cost component | 0.331 (Q 33 → Q 34 cost) |
| abs_ijaz component | 0.7962 |

Q 34 sits in the UPPER 16% of UAS rank — driven primarily by the **max_cost** component (0.331 = the rough Q 33 → Q 34 seam). Q 34 is structurally significant chiefly via its **anomalous mushaf-position** (sandwiched between Medinan-legal Q 33 and Late-Meccan-creedal Q 35), not via content-outlier or iʿjāz-signature properties. This is consistent with H-NEW-130's classification of Q 33-34 as a structural-boundary hinge.

## 7. Phonological / rhyme profile (H-NEW-700)

| Field | Value |
|:--|:--:|
| Top final-letter | ن (nūn) |
| Top final-letter fraction | 22/54 = 40.74% |
| Rhyme entropy (nats) | 1.5596 |
| Phonological-class | mid-rhyme (NOT near-monorhyme) |

Q 34's rhyme profile is **moderate** — 40.7% nūn-final is well below the project's near-monorhyme threshold (≥80% same-letter). The rhyme entropy 1.56 nats is rank 86/114, indicating Q 34 has MORE rhyme diversity than the median surah. This contrasts with the al-ḥamdu li-llāh cluster's other long member Q 6 al-Anʿām (165 verses, also moderate-rhyme) and is unlike short-mufaṣṣal monorhyme surahs.

The dominant fawāṣil patterns in Q 34:
- *-īr* / *-ūr* (the dominant ن-stem ending — *al-khabīr*, *al-shakūr*, *al-baṣīr*, *al-ghafūr*, *al-kabīr*, *al-ḥakīm*) — abjective-divine-name rhymes
- *-ūn / -īn* (the muḥsinūn / kāfirūn / ẓālimūn cluster) — eschatological-judgment endings
- *-īd / -īm* (al-ḥamīd / al-raḥīm)

This abjective-divine-name fawāṣila pattern is consistent with the surah's omniscience-tawḥīd theme — verse-endings reinforce divine attributes.

## 8. Q 27 ↔ Q 34 Sabaʾ-narrative-pair structure

| Diagnostic | Value | Interpretation |
|:--|:--:|:--|
| Q 27 ↔ Q 34 FR | 0.8661 | rank 31.3 percentile in all-pair distribution (more-similar-than-median) |
| Q 34 rank in Q 27 neighbors | 8/113 | top-10 |
| Q 27 rank in Q 34 neighbors | 10/113 | top-10 |
| Mutual top-10 | YES | structurally significant pair-relation |
| sabaʾ proper-noun count | 1 each | exhausting corpus-total of 2 |

Q 27 + Q 34 jointly contain the **only 2 corpus instances** of the proper noun *sabaʾ*. Their mutual top-10 FR position (Q 34 = Q 27's rank-8 neighbor; Q 27 = Q 34's rank-10 neighbor) is **non-trivial**: under random matching, only ~9% of surah pairs achieve mutual top-10 status. The pair is **moderately-cohesive** at the bilateral level (each one's top-10 set contains the other), but neither is the other's *closest* neighbor — the Late-Meccan creedal-narrative band (Q 41, Q 46, Q 32, Q 36) is closer for both.

The Q 27/Q 34 pair shares:
- **The proper-noun fingerprint**: only sabaʾ-PN attestations.
- **Solomon material**: Q 27:15-44 (Solomon-Bilqīs) and Q 34:12-14 (Solomon's jinn-workers + termite-death).
- **David material**: Q 27:15-16 (David-Solomon birds-tongue) and Q 34:10-11 (David-iron-mountain-praising).
- **Late-Meccan creedal frame**: both pre-Hijri; both polemic against Meccan polytheists; both eschatology-adjacent.

See Q034-F-02 for the full pair-cohesion diagnostic and Q034-F-03 for the David-Solomon material-density test.

## 9. Cluster memberships

### al-ḥamdu li-llāh opener cluster (FORMAL only — content-NULL)

Q 34 is one of 5 surahs whose first verse begins with *al-ḥamdu li-llāh*: {Q 1, 6, 18, 34, 35}. Empirical cohesion test (Q034-F-01):

| Diagnostic | Value | Interpretation |
|:--|:--:|:--|
| Within-cluster mean FR | 0.9902 | ABOVE corpus mean 0.9226 |
| Permutation p (cohesive) | 0.7514 | NULL (NOT cohesive) |
| Permutation p (anti-cohesive) | 0.2486 | not significantly anti-cohesive |
| 4-cluster (drop Q 1) mean | 0.9466 | still ABOVE corpus mean |
| Length-residualized 5-cluster mean residual | +0.0539 | positive = above-expected distance |

**The al-ḥamdu li-llāh opener cluster is content-NULL on FR cohesion.** This is OQ-3 candidate ANSWERED-NULL (per Q034-F-01). The cluster is a formal-template parallel without underlying content fingerprint — it does NOT function as a second book-introduction-marker class analogous to muqaṭṭāʿat. The strongest sub-pattern is the **heaven-and-earth motif**: 4 of 5 (Q 6, 34, 35; Q 18 indirectly via *kitāb*) reference *al-samāwāt wa-l-arḍ* (or *kitāb*) in the opening verse. Q 34's distinctive feature within this cluster is the **dual-ḥamd v.1** (corpus-unique).

### Eponymous-locale-name cluster

Q 34 is the corpus's only **eponymously-locale-named** surah where the locale-narrative occupies a dedicated multi-verse block (vv. 15-19). Comparison:
- Q 17 al-Isrāʾ (event-named, not locale; the night-journey is mentioned in v.1 only)
- Q 18 al-Kahf (the Cave story is one of 4 narrative blocks; al-Kahf is the place but the title-phrase is descriptive of the Companions-of-the-Cave, not the locale-as-such)
- Q 105 al-Fīl (event-named — "the Elephant" is the army; not a locale)

Q 34 Sabaʾ is the unique structural type: **kingdom-name-titled surah with multi-verse kingdom-narrative block**.

### Late-Meccan creedal-narrative band (FR-derived)

Q 34's top-10 FR neighbors place it in a tight Late-Meccan creedal-narrative band. The band overlaps substantially with the ḥawāmīm cluster (Q 40-46) and the Late-Meccan الر cluster (Q 10-15). This is the dominant content-cluster Q 34 actually belongs to per FR distance.

## 10. Cross-references

- [[h-new-111-fisher-rao-mushaf]] — Q 34 FR matrix row.
- [[h-new-130-fisher-rao-residuals]] — Q 33-34 boundary IN structural-boundary set.
- [[h-new-590-outlier-spectrum]] — Q 34 NULL (delta_pct = −4.7).
- [[h-new-700-phonological-compression-tail]] — Q 34 ن-final 40.7%.
- [[h-new-720-canonical-adjacency-cost]] — Q 33→Q 34 rank 111/113; Q 34→Q 35 rank 65/113.
- [[h-new-750-ijaz-signature]] — Q 34 MID on sig_A and sig_B.
- [[h-new-840-unified-architectural-score]] — Q 34 UAS rank 18/114.
- `surahs/Q027-al-naml/` (Sabaʾ-narrative-pair partner; specialist file exists).
- `surahs/Q033-al-ahzab/` (mushaf-left-neighbor; specialist file exists).
- `surahs/Q035-al-fatir/` (mushaf-right-neighbor; not yet specialized — future work).
