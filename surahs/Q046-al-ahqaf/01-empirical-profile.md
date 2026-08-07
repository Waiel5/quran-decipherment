---
surah: 46
surah_name: al-Aḥqāf
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: HM-B closer; mild anti-iʿjāz; bottom-quartile UAS; near-monorhyme
---

# Q 46 al-Aḥqāf — empirical profile


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

All metrics extracted from project-pre-computed empirical artifacts in `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/`. Each value is provenance-cited.

## 1. Headline metrics

| Metric | Value | Provenance |
|:--|:--|:--|
| UAS rank | **91 / 114** | `h-new-840.json` |
| UAS score | **−1.591** | h-new-840 (entry: `{"surah":46,"UAS":−1.5907,"abs_outlier":2.34,"max_cost":0.0959,"abs_ijaz":0.3835}`) |
| |outlier| (abs Δ%ile) | 2.34 | h-new-840.all_uas |
| Δ%ile (signed) | **−2.34 (NULL)** | h-new-590 (`p_greater_W = 0.5271`) |
| max neighbor TSP cost | 0.0959 (= Q 45→Q 46) | h-new-840 |
| |iʿjāz signature| | 0.384 | h-new-840 |
| sig_A (al-Bāqillānī axis) | **−0.384** | h-new-750 |
| sig_B (al-Khaṭṭābī proxy) | **−0.769** | h-new-750 |
| Rhyme entropy (final-letter) | **0.952 bits** | this session, min-tashkeel; matches `findings/cross-finding/csv/hawamim-7-cluster-bifurcation.json` |
| Top rāwī | ن (74.3%, 26/35) | this session |
| Distinct rhyme letters | **3** (ن=26, م=8, ر=1) | this session |
| Top 2-char rhyme suffixes | -ūn (13), -īn (13), -īm (7) | this session, regex on min-tashkeel |
| Top 3-char rhyme stem | -mīm / -ūn / -īn alternation | this session |
| Verses (Hafs-Kufan) | 35 | `quran-text/quran-no-tashkeel.json` |
| Words (no-tashkeel) | 676 | this session |
| Letters (no-tashkeel) | 2,698 | this session |
| Distinct roots in Q 46 (QAC) | 177 | `data/morphology/quranic-corpus-morphology-0.4.txt` (this session) |
| Words/verse (mean) | 19.3 | computed |
| QAC tokens with roots | 405 of 1,043 morphology lines | computed this session |
| Length class | mufaṣṣal-ṭiwāl (35 verses) | per `data/hafs-verse-counts.tsv` |

## 2. Position in HM-7 cluster (HM-B closer)

Q 46 is the **closing surah** of the HM-7 cluster {Q 40-46} and, within HM-7, falls in the **HM-B sub-block** {Q 43, 44, 45, 46}. The empirical bifurcation finding ([[hawamim-7-cluster-bifurcation]]) places Q 46 in the **near-monorhyme** half of HM-7:

| Surah | H (bits) | distinct finals | top final % | role |
|:-:|:-:|:-:|:-:|:-:|
| Q 40 | 2.413 | 8 | ن (38%) | HM-A opener |
| Q 41 | 2.146 | 10 | ن (56%) | HM-A |
| Q 42 | 2.565 | 9 | ر (38%) | HM-A apex |
| Q 43 | 0.594 | 3 | ن (88%) | HM-B opener |
| Q 44 | 0.818 | 2 | ن (75%) | HM-B (shortest) |
| Q 45 | 0.700 | 2 | ن (81%) | HM-B |
| **Q 46** | **0.952** | **3** | **ن (74%)** | **HM-B closer** |

**Position summary**: Q 46 is the highest-entropy member of HM-B but still 1.2 bits below HM-A's lowest (Q 41 = 2.15). The 3-final pattern with explicit م-final co-rāwī (8/35 = 23%) distinguishes Q 46 from the strict 2-final monorhymes Q 44 / Q 45.

## 3. FR-roots distance — Q 46's neighbors

Reconstructed from `h-new-111.json` `D_matrix_upper_triangular` (this session, 6,441 pair entries → full 114×114 matrix).

### 3a. Q 46 nearest 7 FR neighbors

| Rank | Surah | FR-distance |
|:-:|:-:|:-:|
| 1 | **Q 41 Fuṣṣilat** | **0.7254** |
| 2 | Q 32 al-Sajda | 0.7916 |
| 3 | Q 34 Sabaʾ | 0.8058 |
| 4 | Q 45 al-Jāthiyah | 0.8112 |
| 5 | Q 40 Ghāfir | 0.8184 |
| 6 | Q 51 al-Dhāriyāt | 0.8188 |
| 7 | Q 36 Yā Sīn | 0.8218 |

**Pattern**: Q 46's FR-nearest neighbor corpus-wide is **Q 41 Fuṣṣilat** (FR=0.7254) — striking because Q 41 is in HM-A (the *opposite* prosodic sub-block). The content-axis links Q 46 to Q 41 across the HM-A/HM-B prosodic divide. This **confirms** at the surah-pair level the [[hawamim-7-cluster-bifurcation]] finding that the HM-A/HM-B split is **prosodic only, not content** — Q 46 (HM-B) is closest to Q 41 (HM-A) at the FR-roots content axis. Of Q 46's top-7 neighbors, **5 of 7 are HM-7 internal** (Q 41, 32, 34, 45, 40) plus Q 36 Yā Sīn — almost the entire neighborhood is muqaṭṭaʿāt-class.

### 3b. Q 46 farthest 5 FR neighbors

| Rank | Surah | FR-distance |
|:-:|:-:|:-:|
| 1 | Q 55 al-Raḥmān | 1.2741 |
| 2 | Q 56 al-Wāqiʿa | 1.0681 |
| 3 | Q 9 al-Tawba | 1.0527 |
| 4 | Q 33 al-Aḥzāb | 1.0505 |
| 5 | Q 80 ʿAbasa | 1.0468 |

**Pattern**: Q 46's farthest neighbors are (i) the 31-fold-refrain surah Q 55, (ii) Medinan-legal corpus-extremes Q 9 and Q 33, (iii) short Meccan eschatological refrains Q 56 and Q 80. The FR-content axis cleanly separates Q 46 from the Medinan-legal extreme and from Q 55's iʿjāz al-takrīr typology.

### 3c. Sister-surah specific FR distances

| Pair | FR-distance | Notes |
|:--|:-:|:--|
| Q 46 ↔ Q 41 | 0.7254 | nearest-neighbor; HM-A (cross-block) |
| Q 46 ↔ Q 45 | 0.8112 | preceding mushaf neighbor; HM-B sibling |
| Q 46 ↔ Q 47 | **0.9905** | **following mushaf neighbor; non-HM Medinan; near corpus mean** |
| Q 46 ↔ Q 11 (Hūd) | 0.8518 | Hūd-narrative twin |
| Q 46 ↔ Q 7 (al-Aʿrāf) | 0.8709 | Hūd-narrative twin |
| Q 46 ↔ Q 26 (al-Shuʿarāʾ) | 1.0172 | Hūd-narrative twin (FAR — al-Shuʿarāʾ is short-narrative-rich) |
| Q 46 ↔ Q 72 (al-Jinn) | 0.8854 | jinn-listening twin |

**The Q 46 ↔ Q 47 FR-distance of 0.9905** is striking: it is **higher** than Q 46 ↔ any HM-7 sibling, **higher** than Q 46 ↔ either Hūd-twin (Q 7, Q 11), and **higher** than Q 46 ↔ Q 72 (jinn-twin). The mushaf-canonical neighbor of Q 46 is the FR-roots-FAR neighbor — empirically confirming the **HM-cluster-exit at Q 46→Q 47** as a content-discontinuity, even though the TSP-cost rank is only moderate (rank 42/113).

## 4. Canonical-adjacency cost

Per `h-new-720.json`:

| Adjacency | δ-cost | rank / 113 | fraction of TSP residual |
|:--|:-:|:-:|:-:|
| Q 44 → Q 45 | 0.1112 | 30 | 1.34% |
| **Q 45 → Q 46** | **0.0959** | **37** | **1.16%** |
| **Q 46 → Q 47** | **0.0873** | **42** | **1.05%** |
| Q 47 → Q 48 | 0.0332 | 79 | 0.40% |

**Audit of the user-prompt claim "Q 46 → Q 47 is HIGH canonical-adjacency-cost transition per h-new-720"**:
- Empirically rank **42 / 113** is *upper-third* but NOT *high* in the strict sense.
- Top-10 expensive adjacencies include Q 1-Q 2 (rank 1, 7.5%), Q 32-Q 33 (rank 2, 4.4%), Q 33-Q 34 (rank 3, 4.0%), Q 9-Q 10 (rank 4, 3.7%), Q 24-Q 25 (rank 5, 3.5%); Q 46-Q 47's 1.05% is **3.5× cheaper than the median top-10**.
- **Verdict: the user-prompt characterisation is REFINED to "moderate cost; upper third (rank 42/113), not top-tier"**. The boundary-cost framing is real but the magnitude is mild.
- The Q 45→Q 46 cost (rank 37/113) is **higher** than Q 46→Q 47 (rank 42/113) — the *internal* HM-B step into Q 46 is empirically more expensive than the *exit* from HM-7. This counter-intuitive finding is worth pre-registering as Q046-F-04 (see [[06-novel-findings]]).

## 5. Outlier-strength (h-new-590)

```
{"X": 46, "window": [43, 44, 45, 46, 47, 48, 49],
 "window_minus_X": [43, 44, 45, 47, 48, 49],
 "d_W": 0.9328, "d_W_minus_X": 0.9396,
 "pct_W": 47.29, "pct_W_minus_X": 49.63,
 "delta_pct": -2.34, "p_greater_W": 0.5271,
 "classification": "NULL"}
```

**Q 46 is NULL on outlier-strength** (Δ%ile = −2.34, p=0.527; classification NULL). Removing Q 46 from its 7-window {Q 43-49} *decreases* the cohesion percentile by only 2.34 pp — the surah is INTEGRATED with its neighbors, not anchoring nor outlier.

Compare windows:
- Q 45 (preceding): Δ%ile = −10.68, classification COHESION_ANCHOR — Q 45 strongly increases cohesion of its window (anchoring).
- Q 46: NULL.
- Q 47 (following): Δ%ile = +5.20, classification WEAK_OUTLIER — Q 47 is mild outlier (its removal *decreases* cohesion by 5.2 pp).

The signed pattern across the boundary (Q 45 ANCHOR → Q 46 NULL → Q 47 WEAK_OUTLIER) is consistent with a **cluster-edge soft-transition**, not a sharp boundary.

## 6. iʿjāz signature breakdown (h-new-750)

```
{"surah":46,"n_verses":35,
 "rhyme_entropy_nats":0.6597,
 "top_final_letter":"ن","top_final_letter_frac":0.7429,
 "mean_content_distance":0.9421,"local_cohesion":1.1001,
 "z_rhyme_entropy":-0.1993,"z_mean_content_distance":0.1842,
 "z_local_cohesion":-0.5696,
 "sig_A":-0.3835,"sig_B":-0.7689,
 "rank_A":72,"rank_B":73}
```

- **sig_A = −0.384** (rank 72/114): mild **anti**-iʿjāz-al-fawāṣil — slightly above-mean rhyme uniformity (z_rhyme_entropy=−0.20) combined with slightly-higher-than-mean content distance (z=+0.18). Q 46 is mildly off the al-Bāqillānī ideal of variable-fawāṣil + tight-content.
- **sig_B = −0.769** (rank 73/114): mild **anti**-al-Khaṭṭābī — rank 73 by the project's secondary axis.
- **|iʿjāz| = 0.384** (modest); does NOT contribute meaningfully to UAS.

The combined profile (low |outlier|, low |iʿjāz|, low max-cost) places Q 46 firmly in the **architecturally-quiet** quadrant. Q 46 is the *non-distinctive* HM-7 closer.

## 7. Compression-tail position (s=46, intra-50)

Per [[h-new-660-compression-tail-gradient|H-NEW-660]] and [[h-new-700-phonological-compression-tail|H-NEW-700]] kink-laws:

- s = 46 is **intra-50** → pre-kink baseline applies.
- d̄_content(46) ≈ 0.96 (no compression discount yet).
- d̄_rhyme(46) ≈ 0.36 (pre-kink baseline).
- d̄_phoneme(46) ≈ 0.001 (pre-kink, kink at s=75).

Q 46 is **NOT a compression-tail surah**. Its observed window-d̄ (per h-new-700: pre-kink window) aligns with the s ≤ 50 baselines. The mild near-monorhyme (entropy 0.952 bits = z=−0.20 below corpus mean) is below-baseline-rhyme-dispersion but well within the prosodically-uniform Meccan-ṭiwāl phase.

## 8. Architectural classification

| Axis | Position |
|:--|:--|
| Structural-iʿjāz (al-Bāqillānī) | mild **anti** (sig_A=−0.38; UAS rank 91) |
| Theological-iʿjāz (al-Khaṭṭābī) | not in *thuluth al-Qurʾān* tradition; Q 46:35 *ūlū al-ʿazm* doctrinal anchor |
| Compression-tail | NOT a tail surah (s=46 ≤ 50) |
| Outlier | NULL (Δ=−2.34, p=0.527) |
| Cluster role | **HM-B closer; HM-7 final member; boundary surah to non-HM Medinan** |
| Eponym strength | **CORPUS HAPAX** (Hqf root: 1/1 attestations in Q 46:21) |

## 9. Honest limits

1. **UAS=91 is below median** — Q 46 is not a standalone architectural outlier. Significance is sub-cluster (HM-B closer; HM-7 bookend) and lexical (Hqf hapax eponym).
2. **Δ=−2.34 with p=0.527 is NULL** — outlier-strength signal is essentially zero.
3. **iʿjāz |sig|=0.38** is mid-bottom magnitude.
4. The Q 46→Q 47 boundary cost rank is **42/113**, NOT in the top-10. The user-prompt's "HIGH canonical-adjacency-cost transition" framing was overstated; the empirical fact is **moderate-upper-third cost**.
5. Verse-by-verse word-level rhyme distribution (full -ūna / -īna / -īma triple-suffix mapping) computed at orthographic level only; phonological reduction (per h-new-700 reduced-rāwī classes) NOT recomputed in this session.
6. The Q 46 ↔ Q 41 FR-distance of 0.7254 (corpus-rank 1 for Q 46) is at the **HM-A side of the bifurcation**. This is consistent with [[hawamim-7-cluster-bifurcation]] confirming the prosody-axis ⊥ FR-content-axis orthogonality.

## 10. Cross-references

- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]] — Q 46 = HM-B member; cross-block FR-nearest is HM-A
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 91/114
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 46 NULL (Δ=−2.34, p=0.527)
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — pre-kink position (s=46)
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 45→46 rank 37; Q 46→47 rank 42
- [[h-new-750|H-NEW-750]] — sig_A=−0.38, sig_B=−0.77, ranks 72-73
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — FR neighbors derived
- [[Q040-ghafir/01-empirical-profile|Q 40 empirical-profile]] — HM-A opener (cross-block reciprocal)
- [[Q041-fussilat/01-empirical-profile|Q 41 Fuṣṣilat]] — Q 46's FR-nearest neighbor (HM-A)
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 46 cell membership (anti-iʿjāz / consolidated-monorhyme)
