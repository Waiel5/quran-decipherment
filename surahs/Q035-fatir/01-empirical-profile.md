---
surah: 35
surah_name_ar: فاطر
surah_name_translit: Fāṭir
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD — 5 H-NEW metrics extracted; 4 internal-computed metrics; cross-finding integration written 2026-05-09
---

# Q 35 Fāṭir / al-Malāʾika — Empirical Architectural Profile


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

This file integrates Q 35's empirical readings across the project's H-NEW metric suite. All numbers are direct extractions from the canonical JSON outputs in `findings/phase-b-hypotheses/csv/`. No new computation here unless explicitly noted.

## 1. Locked basic metrics

| Quantity | Value | Source |
|:--|:--:|:--|
| Surah ID | 35 | canonical |
| Verse count | 45 | Hafs-Kufan |
| Word count (orthographic, no-tashkeel) | 844 | computed `quran-no-tashkeel.json` |
| Letter count (no spaces, no marks) | 3,238 | computed |
| Root-token count (QAC v0.4) | 507 | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| Distinct roots | 230 | same |
| Avg verse word-length | 18.76 words | 844 / 45 |
| Avg verse letter-length | 71.96 letters | 3,238 / 45 |
| Mushaf position | 35 | canonical |
| Revelation order (al-Suyūṭī, *al-Itqān*) | 43 of 114 | mid-to-late Meccan |
| Type | Late Meccan | classical |
| Top-K (500) root coverage fraction | 0.940 | `h-new-111.json` `per_surah_topk_coverage[35]` |

## 2. H-NEW-840 — Unified Architectural Score (UAS)

| Quantity | Value | Notes |
|:--|:--:|:--|
| UAS | **0.0173** | corpus mean ≈ 0; SD-1 normalized |
| UAS rank | **47/114** | mid-pack |
| Component: abs_outlier (Δ%ile from H-NEW-590) | 6.68 | weak-outlier strength |
| Component: max_cost (top mushaf-adjacency cost) | 0.1993 | Q 35 → Q 36 cost (rank 101/113) |
| Component: abs_ijaz (avg of |sig_A|, |sig_B|) | 0.283 | above-corpus-median al-Bāqillānī fawāṣila iʿjāz |

**Reading**: Q 35 is **mid-pack architectural** under the unified score. It is **not** in the structural-iʿjāz top-9 (Q 33, 1, 2, 9, 24, 12, 55, 10, 23 are the top-9). The above-mean iʿjāz signature (sig_A) is offset by a weakish outlier-strength and a moderate max-cost asymmetry.

## 3. H-NEW-590 — Outlier-Spectrum Δ%ile

| Quantity | Value | Notes |
|:--|:--:|:--|
| Window | [32, 33, 34, 35, 36, 37, 38] | symmetric ±3 around Q 35 |
| Window-with-Q35 mean content distance | 0.9658 | Fisher-Rao mean over window verses |
| Window-without-Q35 mean content distance | 0.9592 | leave-one-out |
| Δ percentile-rank (with - without) | **+6.68 pp** | mild-positive |
| p_greater_W (right-tail) | 0.3245 | NULL — NOT a strong outlier |
| Classification | **WEAK_OUTLIER** | per H-NEW-590 categorization |

**Reading**: Q 35 mildly increases its 7-window's mean content distance (i.e. Q 35 is mildly content-distinct from Q 32-38), but at p = 0.32 the effect is not statistically significant. Q 35 is **integrated** in its mid-Meccan band — neither a strong outlier (like Q 55 al-Raḥmān at z = -17.77) nor a strong anchor.

## 4. H-NEW-720 — Canonical Adjacency Cost

| Pair | delta_raw | fraction_residual | Rank |
|:--|:--:|:--:|:--:|
| **Q 33 → Q 34** (al-Aḥzāb → Sabaʾ) | 0.331082 | 3.99% | 110/113 (top-5 expensive) |
| **Q 34 → Q 35** (Sabaʾ → Fāṭir) | **0.074532** | **0.90%** | **65/113** (mid-pack) |
| **Q 35 → Q 36** (Fāṭir → Yāsīn) | **0.199311** | **2.40%** | **101/113** (top-15 expensive) |

**Reading — the cost-asymmetry**: 

- **Q 34 → Q 35** is *mid-pack* despite the shared al-ḥamdu li-llāh opener. A naive expectation would be: shared opener → smooth transition. The empirical result rejects this naïve reading: shared opener does NOT imply low transition cost. The cost-mid-pack reading aligns with the al-ḥamdu cluster's group-level NULL on FR-cohesion (see `06-novel-findings.md` Q035-F-01).
- **Q 35 → Q 36** is in the top-15 most-expensive transitions (rank 101/113). Q 36 Yāsīn opens with the muqaṭṭāʿat *Yā Sīn*, then immediately pivots to the eschatological-resurrection arc. The content-discontinuity Q 35 → Q 36 reflects the structural pivot: Q 35 closes on cosmic-forbearance (v.45 *innamā yuʾakhkhirhum ilā ajalin musamman*); Q 36 opens with the muqaṭṭāʿat + Quran-oath (*wa-l-Qurʾāni l-ḥakīm innaka la-min al-mursalīn*).
- The asymmetry (cheap-into-Q35, expensive-out-of-Q35) places Q 35 as a **mid-Meccan content-pivot point** despite its surface mid-rank UAS profile.

## 5. H-NEW-750 — iʿjāz Signature

| Quantity | Value | Notes |
|:--|:--:|:--|
| Verse count | 45 | |
| Rhyme entropy (Shannon, nats) | 1.187 | above corpus median (median ≈ 1.0) |
| z(rhyme entropy) | +0.756 | mildly multi-tonal |
| Top final letter | ر (rāʾ) | divine-attribute fawāṣila pattern (-īr/-ūr) |
| Top final letter fraction | 64.4% | dominant but not monorhyme |
| Mean content distance (FR) | 0.9714 | above corpus mean 0.9235 |
| z(mean content distance) | +0.473 | mildly distinct content |
| Local cohesion | 1.0097 | corpus baseline |
| z(local cohesion) | -0.693 | LOW intra-surah cohesion |
| sig_A (al-Bāqillānī fawāṣila iʿjāz) | **+0.283** | rank 53/114 (above median) |
| sig_B (rhyme-purity iʿjāz) | +0.064 | rank 57/114 (near median) |

**Reading**: Q 35's iʿjāz profile is **multi-tonal-rhyme + content-distinctive + low-cohesion** — a "cosmological-survey" surah with diverse divine-attribute fawāṣila and dispersive content. This contrasts with Q 36 Yāsīn's near-monorhyme + high-cohesion profile and with Q 55 al-Raḥmān's strict-refrain monorhyme (the fa-bi-ayyi structure).

The 7 of 45 verse-finals that match 99-Names cluster (Q 35:11 *yasīr*, v.18 *al-maṣīr*, v.26 *nakīr*, v.28 *ghafūr*, v.30 *shakūr* (also v.34, 36 carry the same), v.34 *shakūr*, v.38 *al-ṣudūr* etc.) are concentrated in the cosmological-and-eschatological middle blocks (vv. 18-32, 33-45). See `02-content-analysis.md` §3 for the verse-by-verse fāṣila divine-name catalog.

## 6. H-NEW-111 — Fisher-Rao Mushaf-Geodesic

`h-new-111.json` D-matrix (Fisher-Rao angular distance, 500 root-token features, Dirichlet α=0.5).

### Q 35 nearest 12 surahs (FR distance ascending)

| Rank | Surah | FR distance | Theme |
|:-:|:-:|:--:|:--|
| 1 | Q 22 al-Ḥajj | 0.8312 | pilgrimage + cosmic-creation argument |
| 2 | Q 14 Ibrāhīm | 0.8368 | prophetic-suffering + tawḥīd |
| 3 | Q 13 al-Raʿd | 0.8420 | thunder + cosmic-signs + creation |
| 4 | Q 31 Luqmān | 0.8455 | wisdom + cosmic-creation |
| 5 | Q 63 al-Munāfiqūn | 0.8530 | (anomaly: Medinan; close on root-vector?) |
| 6 | Q 45 al-Jāthiyah | 0.8554 | cosmological signs + judgment |
| 7 | Q 42 al-Shūrā | 0.8586 | consultation + divine attributes |
| 8 | Q 62 al-Jumuʿah | 0.8621 | Friday + musabbiḥāt (Medinan) |
| 9 | Q 64 al-Taghābun | 0.8667 | mutual-loss + musabbiḥāt (Medinan) |
| 10 | Q 46 al-Aḥqāf | 0.8690 | jinn + revelation-confirmation |
| 11 | Q 67 al-Mulk | 0.8691 | sovereignty + creation-argument |
| 12 | Q 57 al-Ḥadīd | 0.8694 | iron + musabbiḥāt + Medinan |

**Reading**: Q 35's FR neighborhood is the **post-prophetological cosmic-creation cluster** (Q 13, 14, 22, 31, 42, 45, 46) — surahs that argue the divine-attribute case via cosmic-signs (creation, alternation, ships, fertility). Several Medinan musabbiḥāt (Q 62, 64, 57) are also close, reflecting shared divine-attribute density.

### Q 35 farthest 5 surahs

| Rank from far | Surah | FR distance | Why distant |
|:-:|:-:|:--:|:--|
| 1 (farthest) | Q 55 al-Raḥmān | 1.2709 | strict-refrain monorhyme + cosmic-eschatological inventory |
| 2 | Q 26 al-Shuʿarāʾ | 1.1680 | extended prophet-cycle + refrain |
| 3 | Q 12 Yūsuf | 1.1334 | name-monopoly narrative |
| 4 | Q 56 al-Wāqiʿah | 1.1093 | eschatological-categories + 3-fold judgment-day classes |
| 5 | Q 20 Ṭāhā | 1.0977 | Mosaic-narrative + muqaṭṭāʿat |

**Note (interesting connection)**: Q 35 Fāṭir is FR-far from Q 56 al-Wāqiʿah, BUT Q 56 also has a 3-tier classification of Resurrection-Day (*al-sābiqūn al-sābiqūn / aṣḥāb al-yamīn / aṣḥāb al-shimāl*). Both surahs deploy 3-tier human-classification rhetoric, but with **different vocabulary**: Q 35 uses *ẓālim li-nafsih / muqtaṣid / sābiq bi-l-khayrāt* (the inheritors-of-the-Book frame); Q 56 uses *aṣḥāb al-yamīn / al-shimāl / al-sābiqūn* (the Resurrection-Day frame). These are **content-twins**, NOT vocabulary-twins (high FR distance reflects vocabulary-divergence, not theme-divergence). This is a thematic-not-lexical parallel — a known limitation of Fisher-Rao on roots: it captures vocabulary-overlap, not deep-thematic-twins.

### Mean FR distance to corpus

- Q 35 mean FR distance to all 113 others: **0.9714**
- Corpus mean: 0.9235
- Q 35 rank: ~70/114 (above-median dispersion).

## 7. H-NEW-700 — Phonological Compression-Tail

Q 35 is **pre-kink** (s < 50), so it sits in the head-mushaf zone where the compression-tail gradient does not yet apply. Q 35 specifically:
- Final-letter ر-dominant (64.4%) — not a typical compression-tail signature.
- Verse-length avg ≈ 19 words — much longer than mufaṣṣal short surahs.

The compression-tail gradient (Q 49+ steep rise) places Q 35 at **gradient onset**: the rising pre-Hijra-kink shoulder. Q 35's relative position in the gradient is "pre-onset" — the phonological pivots have not yet activated.

## 8. H-NEW-660 — Compression-Tail Gradient (cross-axis)

`h-new-660.json` confirms the kink position; Q 35 sits in the head-band {1-49} alongside Q 34 and Q 36.

## 9. Length-class architectural classification

By al-Zarkashī mufaṣṣal hierarchy:
- al-sabʿ al-ṭiwāl (longest 7): Q 2, 3, 4, 5, 6, 7, 9 (or 10) — Q 35 is NOT in this set.
- al-miʾūn (≥100 verses): Q 35 has 45 verses — NOT in this set.
- al-mathānī: surahs 50-150 verses or "duplicated" — Q 35 (45 v.) is BORDERLINE just below.
- mufaṣṣal (Q 49+): Q 35 is BEFORE the mufaṣṣal break.

Empirically, Q 35 sits in the **mid-Meccan post-prophetological band** (Q 30-46): the band that argues the tawḥīd case via cosmic-signs after the major Mosaic + Abrahamic narratives are largely complete (those concentrate Q 7, Q 11, Q 12, Q 18-21, Q 26-28).

## 10. Multi-axis architectural fingerprint

| Axis | Q 35 measurement | Cluster-membership |
|:--|:--|:--|
| al-ḥamdu li-llāh opener | YES (1 of 5) | {Q 1, 6, 18, 34, 35} (CC-048 confirmed; H-NEW-NEW Q035-F-01) |
| Late-Meccan (Pattern-B) | YES (Nöldeke-rank 86-99, "Hijra-straddling") | cross-finding-012 confirmed cluster |
| Active-participle opener | UNIQUE in al-ḥamdu cluster | (only Q 35 uses *fāṭir + jāʿil*; others use *alladhī*) |
| 3-fold hierarchy v.32 | UNIQUE in corpus | Q035-F-02 |
| al-malāʾika v.1 opener | UNIQUE in corpus | Q035-F-03 |
| Two al-ḥamdu li-llāh statements | Q 35 (v.1, v.34) | Q035-F-05 (within-surah inclusio) |
| Mushaf-adjacent al-ḥamdu pair | Q 34 → Q 35 (only consecutive al-ḥamdu) | Q035-F-04 (transition cost) |
| Sūrat al-Malāʾika dual-name | YES (both Fāṭir AND al-Malāʾika canonical) | classical |
| FR-cluster: post-prophetological cosmological | YES (top-12 FR-neighbors all from band) | H-NEW-111 |
| Outlier-strength | +6.68 pp WEAK_OUTLIER (NULL p=0.32) | H-NEW-590 |
| UAS rank | 47/114 mid-pack | H-NEW-840 |
| iʿjāz sig_A rank | 53/114 above-median | H-NEW-750 |

## 11. Headline architectural reading

**Q 35 is a MID-MECCAN COSMOLOGICAL-SURVEY SURAH that performs four distinct structural roles**:

1. **Cluster-member** — the Meccan terminal node of the 5-surah al-ḥamdu li-llāh opener cluster (with Q 34 immediately preceding it as the only mushaf-adjacent partner).
2. **Pivot-point** — content-cheap into (Q 34 → Q 35 mid-pack), content-expensive out of (Q 35 → Q 36 top-15).
3. **Hierarchy-statement** — carries the corpus-unique 3-fold *ẓālim/muqtaṣid/sābiq* hierarchy (v.32), the structural anchor of much classical exegesis.
4. **Angels-named** — the only surah-1-verse to mention *al-malāʾika* explicitly, motivating the dual-name tradition (Fāṭir / al-Malāʾika).

The architectural reading is consistent: Q 35 is a mid-band Meccan cosmological-survey + 3-fold-classification surah that anchors a small structural set (the al-ḥamdu cluster's terminal Meccan member, the angels-named opener, the 3-fold hierarchy node). It is NOT a top-tier UAS outlier; its distinctiveness is in its **specific structural anchorings**, not in extreme architectural metrics.

## 12. Cross-references

- `00-overview.md` for narrative-structural overview.
- `02-content-analysis.md` for verse-by-verse + 4-block content map.
- `06-novel-findings.md` for the 5 pre-registered tests (Q035-F-01 through Q035-F-05).
- [[Q006-al-anam/00-overview|Q 6 al-Anʿām]], [[Q018-al-kahf/00-overview|Q 18 al-Kahf]], [[Q034-saba/00-overview|Q 34 Sabaʾ]] — al-ḥamdu li-llāh cluster co-members.
- [[Q036-yasin/00-overview|Q 36 Yāsīn]] — immediate mushaf successor; Q 35 → Q 36 expensive transition.
- [[Q056-al-waqia/00-overview|Q 56 al-Wāqiʿah]] — content-twin for the 3-tier human-classification rhetoric (different vocabulary).
