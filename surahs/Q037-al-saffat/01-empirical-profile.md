---
surah: 37
surah_name_ar: الصافات
surah_name_translit: al-Ṣāffāt
file_type: empirical-profile
date_last_updated: 2026-05-08
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111,590,700,720,750,840,940,1070}.
---

# Q 37 al-Ṣāffāt — Empirical Architectural Profile


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
| Verse count | 182 | Hafs-Kufan |
| Word count (no-tashkeel) | 881 | computed |
| Letter count (no-tashkeel, sans spaces) | 3,915 | computed |
| Avg verse length (letters) | ~21.5 | short-verse (oath-opener stylistic class) |
| Avg verse length (words) | ~4.84 | short-verse |
| Top final-letter | ن (nūn) | 79.7% of 182 verses (`h-new-700.json`) |
| Rhyme entropy (nats) | 0.704 | LOW — near-monorhyme on -ūn / -īn |
| Mean content distance (FR) | 0.9933 | `h-new-750.json` |
| Local cohesion (window) | 1.0655 | `h-new-750.json` |
| iʿjāz sig_A | -0.809 (rank 83/114) | LOW al-Bāqillānī iʿjāz al-fawāṣil signal |
| iʿjāz sig_B | -0.737 (rank 70/114) | LOW al-Sakkākī iqāʿ signal |
| UAS | -1.158 (rank 79/114) | LOW unified architectural significance |
| Outlier-strength Δ%ile | +3.28 pp | WEAK_OUTLIER (window {Q 34-40}); p_greater = 0.6144 |
| Q 36→Q 37 cost | +0.0080 (delta_raw +0.0662) | low — Yāsīn → Ṣāffāt smooth |
| Q 37→Q 38 cost | 0.000 (clamped; delta_raw -0.000911) | seamless (1 of 13 clamped-zero pairs) |
| Q 38→Q 39 cost | +0.0120 (delta_raw +0.0992) | modest |
| H-NEW-940 prophet-order Kendall-τ | +0.857 (rank 1/8) | most-aligned to consensus order |
| H-NEW-1070 oath-cluster centrality rank | 15/15 (peripheral) | Q 37 is the WEAKEST member of the oath cluster on FR centrality |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 37's top-10 nearest in FR space (decoded from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 23 | al-Muʾminūn | 0.8391 | mid-Meccan creedal-narrative twin |
| 2 | Q 51 | al-Dhāriyāt | 0.8428 | oath-opener cluster (H-NEW-1070) |
| 3 | Q 44 | al-Dukhān | 0.8434 | mid-Meccan eschatological |
| 4 | Q 52 | al-Ṭūr | 0.8602 | oath-opener cluster (H-NEW-1070) |
| 5 | Q 43 | al-Zukhruf | 0.8644 | ḥawāmīm cluster |
| 6 | Q 15 | al-Ḥijr | 0.8882 | ALR cluster, prophet-narrative |
| 7 | Q 36 | Yāsīn | 0.9002 | mushaf-left-neighbor |
| 8 | Q 46 | al-Aḥqāf | 0.9014 | ḥawāmīm cluster |
| 9 | Q 38 | Ṣād | 0.9035 | **mushaf-right-neighbor (the seamless seam)** |
| 10 | Q 32 | al-Sajda | 0.9059 | mid-Meccan |

Q 37's FR-neighborhood is **content-thematic mid-Meccan**: 4 of the top-10 are oath-cluster members (Q 51, Q 52) or near-oath (Q 44, Q 43), 2 are mushaf-immediate-neighbors (Q 36, Q 38), and 2 are creedal-narrative cousins (Q 23, Q 15). Q 37 mean distance to all 113 = 0.9853 (just below corpus mean 0.9234 — Q 37 is slightly content-distinct but not extreme).

Far end:
- Q 55 al-Raḥmān: 1.2391 (the iʿjāz-anti-twin / *ʿarūs al-Qurʾān* refrain-driven outlier).
- Q 9 al-Tawba: 1.1624 (basmala-less Medinan polemic).
- Q 4 al-Nisāʾ: 1.1226 (long Medinan legal).

## 3. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json`:

| Field | Value |
|:--|:--:|
| Window | {Q 34, Q 35, Q 36, Q 37, Q 38, Q 39, Q 40} |
| d_W | 0.917 |
| d_W − Q 37 | 0.909 |
| Δ pp | +3.28 |
| pct_W | 38.56 |
| pct_W − Q 37 | 35.28 |
| p_greater_W | 0.6144 |
| Classification | WEAK_OUTLIER |

Q 37 is mildly content-distinct from its mid-Meccan neighborhood, but the perm-p of 0.61 indicates the surah is **not** a strong outlier. The cluster Q 34-40 is itself a moderately-cohesive segment (mufaṣṣal-ṭiwāl candidates per H-NEW-540).

## 4. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Rank |
|:--|:--:|:--:|:--:|
| Rhyme entropy (nats) | 0.7036 | -0.120 | (low entropy = near-monorhyme) |
| Mean content distance | 0.993 | +0.689 | (slightly content-distant) |
| Local cohesion | 1.066 | -0.617 | (low local cohesion) |
| sig_A | -0.809 | — | rank 83/114 (LOW) |
| sig_B | -0.737 | — | rank 70/114 (LOW) |

Q 37 is LOW on both iʿjāz axes. al-Bāqillānī's iʿjāz al-fawāṣil reading (which the corpus-anti-twin-correlation r = -0.86 instantiates) places Q 37 in the LOW-iʿjāz-signature band. This is consistent with the surah being a **prophet-narrative-vignette compilation** rather than a structurally-innovative iʿjāz showcase.

## 5. Canonical-adjacency cost (H-NEW-720)

| Boundary | delta_raw | fraction_residual | Note |
|:--|:--:|:--:|:--|
| Q 36 → Q 37 | +0.0662 | 0.0080 | low (Yāsīn-Ṣāffāt smooth — al-Biqāʿī Q 36→Q 37 munāsabah) |
| Q 37 → Q 38 | -0.000911 | 0.0000 (clamped) | **SEAMLESS** (1 of 13 clamped-zero adjacencies) |
| Q 38 → Q 39 | +0.0992 | 0.0120 | modest |

The clamped-zero set (delta_raw ≤ 0): {Q 91→Q 92, Q 4→Q 5, Q 6→Q 7, Q 3→Q 4, Q 65→Q 66, Q 109→Q 110, Q 73→Q 74, Q 105→Q 106, Q 86→Q 87, Q 93→Q 94, Q 64→Q 65, Q 72→Q 73, **Q 37→Q 38**}. **13 pairs**, not 2 as the brief states. Q 37 → Q 38 is the LEAST-improved (smallest absolute negative delta) of the 13 — i.e. the canonical adjacency is just-barely better than 2-opt's best alternative.

## 6. H-NEW-940 prophet-order alignment

Q 37 prophet-order (left-to-right by first-occurrence in QAC v0.4 PN-lemmas):
**Nūḥ → Ibrāhīm → Isḥāq → Mūsā → Hārūn → Ilyās → Lūṭ → Yūnus**

Kendall-τ to H-NEW-940 consensus = **+0.857** (RANK 1/8 of the H-NEW-940 narrative-surah-set).

The order is a chronological-typological progression with **one inversion**: Lūṭ (chronologically pre-Mūsā as Abraham's nephew) appears AFTER Mūsā-Hārūn and Ilyās. The inversion is thematic-rhetorical (the destruction-narratives are clustered AFTER the affirmation-narratives), not chronologically-confused.

Per H-NEW-940 H2a (CONFIRMED at p=0.001 Bonferroni-4): the pre-Abrahamic chain Ādam → Nūḥ → Hūd → Ṣāliḥ is conserved; Q 37 contains only Nūḥ from this set so the conservation is trivially satisfied. The Q 37-distinctive feature is that it carries the *latest* Mūsā→Lūṭ inversion in the H-NEW-940 corpus.

## 7. H-NEW-1070 oath-opener cluster membership (Q037-F-04 RESULT)

Q 37 is one of the strict-15 oath-opener cluster members (CONFIRMED at p=0.0004 corpus-wide). However, Q037-F-04 (this surah's specialist test) finds:

| Diagnostic | Value | Interpretation |
|:--|:--:|:--|
| Q 37 mean dist to other 14 oath-members | 0.9949 | essentially equal to its corpus-mean (0.9853) |
| Random-14-subset null mean | 0.9931 | near-identical |
| perm-p (D_oath ≤ random) | 0.5479 | NULL (no preferential affinity) |
| Q 37 rank within 15-cluster centrality | **15/15** | Q 37 is the WEAKEST member |
| Within-cluster pairwise median FR | 0.7205 | tight intra-cluster |
| Q 37-row median FR to others | 1.0223 | Q 37 above median (peripheral) |

**Q 37 is a PERIPHERAL member** of the oath cluster. The cluster's tight cohesion (intra median 0.72) is driven by the short-Meccan-tail core {Q 91-103} (top-5 most-central: Q 103, Q 100, Q 95, Q 91, Q 93 — all short-cosmic-condition openers). Q 37's mid-mushaf, narrative-heavy character makes it the LEAST-central oath-member.

This is consistent with the H-NEW-1070 framing: the cluster is FR-cohesive corpus-wide AT THE GROUP LEVEL, but individual members vary in centrality. Q 37 sits at the EARLY-mushaf, NARRATIVE-RICH boundary of the cluster — its membership is via *opening-form parallel*, not via *content-fingerprint similarity* with the short-tail oath members.

## 8. Architectural type classification

| Axis | Q 37 placement |
|:--|:--|
| Length class | mid-Meccan (n=182, longest in the head-mushaf) |
| Compression-tail position | s=37 < kink-50, OUTSIDE compression-tail regime (laws apply for s>50) |
| iʿjāz typology | LOW-iʿjāz on both fawāṣil and iqāʿ axes |
| FR neighborhood | mid-Meccan eschatological-narrative (Q 23 / Q 44 / Q 51 / Q 52) |
| Outlier-strength | WEAK |
| Cluster memberships | (1) H-NEW-1070 oath-opener (peripheral, rank 15/15); (2) prophet-narrative-corpus loose grouping with Q 7, Q 11, Q 19, Q 21, Q 26, Q 38 |
| Adjacency role | seamless RIGHT seam (→Q 38); smooth LEFT seam (Q 36→) |

**Architectural verdict**: Q 37 is the **mid-Meccan prophet-cycle compendium** of the corpus — a narrative-heavy oath-opener whose membership in formal clusters is more *structural-typological* than *content-fingerprint*.

## 9. Cross-references

- [[h-new-111-fisher-rao-mushaf]] — Q 37 FR matrix row.
- [[h-new-590-outlier-spectrum]] — Q 37 weak outlier on Q 34-40.
- [[h-new-700-phonological-compression-tail]] — Q 37 ن-rhyme dominant (0.797).
- [[h-new-720-canonical-adjacency-cost]] — Q 37→Q 38 clamped-zero seamless.
- [[h-new-750-ijaz-signature]] — Q 37 LOW on both axes.
- [[h-new-840-unified-architectural-score]] — Q 37 UAS rank 79/114.
- [[h-new-940-prophet-order-conservation]] — Q 37 rank 1/8 most-aligned.
- [[h-new-1070-oath-opener-cluster]] — Q 37 strict-15 member (peripheral).
- `surahs/Q036-yasin/` (mushaf left-neighbor; not yet specialized).
- `surahs/Q038-sad/` (mushaf right-neighbor; specialist run 2026-05-07).
