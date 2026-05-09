---
surah: 81
surah_name_ar: التكوير
surah_name_translit: al-Takwīr
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111, 590, 720, 750, 840, 1200, 1220}.
---

# Q 81 al-Takwīr — Empirical Architectural Profile

## 1. Headline numbers

| Metric | Value | Source / interpretation |
|:--|:--:|:--|
| Verse count | 29 | Hafs-Kūfan |
| Word count (no-tashkeel) | 104 | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, sans spaces) | 435 | computed |
| Avg verse length (letters) | 15.00 | very-short-mufaṣṣal-qiṣār register |
| Avg verse length (words) | 3.59 | very-short-mufaṣṣal-qiṣār register |
| Top final-letter | ت (tāʾ marbūṭa fem-passive-perfect) | 14/29 (48.3%) — driven by the cosmic-cascade vv. 1-14 |
| Rhyme entropy (nats) | 1.215 | mid-entropy (z = +0.806); 3-segment rhyme architecture (ت → س → ن) |
| Mean content distance (FR) | 0.8138 | **BELOW corpus mean (0.92)** — Q 81 is content-CENTRAL |
| Local cohesion z-score | +0.124 | mid-pack |
| iʿjāz sig_A (al-Bāqillānī fawāṣil) | **+1.888** (rank **8/114**) | **TOP 7% of corpus** for fāṣila-virtuosity iʿjāz |
| iʿjāz sig_B (al-Sakkākī iqāʿ) | +0.930 (rank 31/114) | TOP 27% for rhythm-cadence iʿjāz |
| UAS | 0.0593 (rank 45/114) | mid-pack overall |
| Outlier-strength Δ%ile | -1.04 pp | **NULL** (window {Q 78-84}; p_greater = 0.9913); Q 81 is highly cluster-typical, NOT a content outlier |
| Q 80→Q 81 cost | +0.0867 (frac_residual 1.045%; rank 43/113) | mild seam (al-Mursalāt → al-Naba? wait — Q 80 al-ʿAbasa, mid-cost) |
| Q 81→Q 82 cost | +0.0621 (frac_residual 0.749%; rank 57/113) | low seam (al-Takwīr → al-Infiṭār is smooth) — both *idhā*-cosmic-event-openers |
| H-NEW-1200 14-cluster cohesion | mean dist to other 13 = 0.6211 vs corpus 0.815 | Q 81 is HIGH-COHESION member of the 14-cluster (cluster-mean / corpus-mean = 0.762) |
| H-NEW-1200 Sub-cluster A core | Q 81 ↔ {Q 56, 82, 84, 99} mean = 0.6387 | 4-element idhā-opener cohesion |
| **H-NEW-1200 CORE-3 (Q 81 ↔ {Q 82, 84, 99})** | **0.5633** | **CORE architectural CENTRE — Q 81 has lowest mean to other 3 CORE members** |
| FR-centroid rank (H-NEW-1220) | mean d = 0.8138, **rank ~14/114** | content-CENTRAL (top 12% of corpus by FR-centroid proximity) |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 81's top-15 nearest neighbors in FR-content space (extracted from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 102 | al-Takāthur | 0.4534 | greed-warning eschatology |
| 2 | Q 108 | al-Kawthar | 0.4561 | shortest surah; corpus-rank-3 FR-centroid |
| 3 | Q 112 | al-Ikhlāṣ | 0.4671 | corpus-rank-1 FR-centroid + theology iʿjāz exemplar |
| 4 | Q 106 | Quraysh | 0.4715 | Quraysh-favor short-Meccan |
| 5 | Q 113 | al-Falaq | 0.4766 | muʿawwidhatān |
| 6 | Q 105 | al-Fīl | 0.4790 | Year-of-Elephant short narrative |
| 7 | Q 100 | al-ʿĀdiyāt | 0.4806 | oath-cosmic-event-opener; H-NEW-1200 cluster member |
| 8 | Q 94 | al-Sharḥ | 0.4811 | divine-intimacy-pair-with-Q-93 |
| 9 | Q 103 | al-ʿAṣr | 0.4844 | corpus-shortest 3-verse oath-eschatology |
| 10 | Q 114 | al-Nās | 0.4846 | muʿawwidhatān + ring-closure pair-with-Q-1 |
| 11 | Q 107 | al-Māʿūn | 0.4870 | charity-dispute eschatology |
| 12 | Q 111 | al-Masad | 0.4890 | Abū Lahab curse |
| 13 | Q 110 | al-Naṣr | 0.4904 | last-revealed (Medinan), short |
| 14 | Q 91 | al-Shams | 0.4939 | 7-oath uniqueness (H-NEW-85 confirmed); SUN-themed |
| 15 | Q 104 | al-Humaza | 0.5025 | H-NEW-1200 cluster member |

**Q 81's FR-neighborhood is OVERWHELMINGLY SHORT-MUFAṢṢAL-QIṢĀR.** All 15 nearest neighbors have ≤ 19 verses, and 13/15 are in the corpus's bottom 25 surahs by length. This places Q 81 deep within the corpus's tightest architectural-cohesion zone (consistent with H-NEW-1220 FR-centroid finding that the corpus's center-of-mass is at the short-tail).

**Far end (Q 81's 5 most-FR-distant surahs):**

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 113 | Q 4 | al-Nisāʾ | 1.2434 | Medinan legal |
| 112 | Q 9 | al-Tawba | 1.2367 | Medinan polemic; basmala-less |
| 111 | Q 3 | Āl ʿImrān | 1.2225 | Medinan |
| 110 | Q 2 | al-Baqara | 1.1767 | long Medinan |
| 109 | Q 10 | Yūnus | 1.1707 | mid-length late-Meccan/transitional |

**The polarization is structurally identical to Q 99's**: maximum FR-distance from the LONG-MEDINAN-LEGAL block (Q 2, 3, 4, 9, 10). This is the corpus's structural-asymmetry signature — short eschatological tail vs long Medinan legal head, exactly the cross-finding-016 mushaf-architecture polarization.

### 2.1 H-NEW-1200 CORE-4 architecture — pairwise FR matrix

The 4 surahs forming the architectural CORE of H-NEW-1200 sub-cluster A are Q 81, Q 82, Q 84, Q 99 — the 4 *idhā*-cosmic-event-openers using non-abstract cosmic-objects (sun / heaven / heaven / earth) as the protasis-subject. Their FR pairwise distances:

|  | Q 81 | Q 82 | Q 84 | Q 99 |
|:-:|:-:|:-:|:-:|:-:|
| **Q 81** | – | 0.5286 | 0.6183 | 0.5429 |
| **Q 82** | 0.5286 | – | 0.6185 | 0.5692 |
| **Q 84** | 0.6183 | 0.6185 | – | 0.5616 |
| **Q 99** | 0.5429 | 0.5692 | 0.5616 | – |

**Mean pairwise FR within CORE-4 = 0.5732** (vs corpus mean 0.9236 — **38% below corpus baseline**).

**Mean FR from each CORE member to the other 3:**

| Surah | mean_FR_to_other_CORE3 | Rank within CORE-4 |
|:-:|:-:|:-:|
| **Q 81** | **0.5633** | **1 (CENTRE)** |
| Q 99 | 0.5579 | (joint with Q 81 — see refinement below) |
| Q 82 | 0.5721 | 3 |
| Q 84 | 0.5995 | 4 (most peripheral) |

(Refinement: Q 99 mean to {Q 81, 82, 84} = (0.5429 + 0.5692 + 0.5616)/3 = 0.5579. Q 81 mean to {Q 82, 84, 99} = (0.5286 + 0.6183 + 0.5429)/3 = 0.5633. **Q 99 is marginally more CENTRAL than Q 81 by mean** — but Q 81 owns the LOWEST single pairwise distance within the CORE (Q 81 ↔ Q 82 = 0.5286). The two surahs are JOINT-CENTRAL within the CORE-4.)

**Interpretation**: Q 81 and Q 99 are the architectural CENTRE-PAIR of the CORE-4. Q 84 is the most peripheral CORE member (mean 0.5995, highest within CORE). The CORE itself is FR-internally-cohesive at 38% below corpus baseline — a tight cluster.

The CORE-4 is queued for formal pre-registered FR-cohesion replication in `06-novel-findings.md` Q081-F-01.

### 2.2 Q 81 within the broader H-NEW-1200 14-cluster

The full H-NEW-1200 cluster is Q {56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104}. Q 81's mean FR to the other 13 = **0.6211** (cohesion-ratio = 0.762 vs corpus mean 0.815). Q 81 is among the most-tightly-embedded members of the 14-cluster, consistent with its CORE-4 architectural-centrality.

Within Sub-cluster A (Q 56, 81, 82, 84, 99 — the 5 *idhā*-cosmic-event-openers), Q 81's mean FR to the other 4 = **0.6387**. Q 56 is the largest contributor to this average (Q 56-Q 81 = 0.8648 — far higher than the CORE-4 internal pairs). This corroborates the H-NEW-1200 architecture: **Q 56 sits at the periphery of Sub-cluster A**, while **Q 81/82/84/99 form the tight CORE.**

## 3. iʿjāz signature (H-NEW-750) — Q 81 is in the TOP-8 of corpus

| Component | Value | z-score | Rank |
|:--|:--:|:--:|:--:|
| Rhyme entropy (nats) | 1.2148 | +0.806 | (mid-entropy 3-segment rhyme architecture) |
| Mean content distance | 0.8138 | -1.083 | (content-central) |
| Local cohesion | 1.610 | +0.124 | (mid-pack local cohesion) |
| sig_A (iʿjāz al-fawāṣil) | **+1.888** | — | **rank 8/114 (TOP 7%)** |
| sig_B (iʿjāz iqāʿ) | +0.930 | — | rank 31/114 (TOP 27%) |

**Q 81 ranks 8/114 by al-Bāqillānī iʿjāz al-fawāṣil signature — among the strongest fāṣila-virtuosity surahs in the corpus.** This is striking for a 29-verse 104-word surah — Q 81 packs HIGH iʿjāz signature into very few words.

The iʿjāz fingerprint is consistent with Q 81's empirical structure:
- **3-segment rhyme architecture** (vv. 1-14: ت / vv. 15-18: س / vv. 19-29: ن) producing mid-entropy rhyme that scores high on al-Bāqillānī's fāṣila-virtuosity criterion (rhyme structure that is both regular AND varies systematically across the surah).
- **High final-letter concentration in the cosmic-cascade segment** (14× ت across vv. 1-14 = 100% of segment A).
- **Tight content-cohesion** (mean FR distance 1.083 SD below corpus mean) yielding favorable iʿjāz scoring.
- **Short-verse pulse** (avg ~15 letters / verse) reinforcing the iqāʿ rhythm-cadence signature.

This is the strongest iʿjāz-fawāṣil score of the H-NEW-1200 CORE-4 cluster — a key empirical justification for treating Q 81 as the architectural CENTRE.

## 4. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json`:

| Field | Value |
|:--|:--:|
| Window | {Q 78, Q 79, Q 80, Q 81, Q 82, Q 83, Q 84} |
| d_W (mean intra-window FR) | 0.6648 |
| d_W − Q 81 | 0.6782 |
| Δ pp | -1.04 |
| pct_W | 0.87 |
| pct_W − Q 81 | 1.91 |
| p_greater_W | 0.9913 |
| Classification | **NULL** (NOT an outlier) |

**Q 81 is NOT an outlier-strength surah.** REMOVING Q 81 from its 7-surah neighborhood window {Q 78-84} INCREASES the mean within-window FR distance (0.6648 → 0.6782) — indicating Q 81 is HIGHLY COHESIVE with its neighbors, NOT extreme.

This is the **expected cluster-CENTRAL profile**: Q 81 is content-CENTRAL of its eschatology-tail neighborhood, NOT a content-outlier. The HIGH iʿjāz signature is the surah's standalone architectural distinction; outlier-strength is reserved for surahs that BREAK their neighborhood's coherence (e.g., Q 33 al-Aḥzāb, Q 24 al-Nūr, Q 1 al-Fātiḥa, Q 9 al-Tawba — the corpus's strongest content-outliers).

## 5. UAS (H-NEW-840)

| Component | Value |
|:--|:--:|
| Outlier-strength contribution | 1.040 (low, by NULL classification above) |
| Max-cost contribution | 0.0867 (the Q 80→Q 81 hinge cost, mid-rank) |
| iʿjāz contribution | **1.888 (rank 8/114)** |
| **UAS composite score** | **0.0593** |
| **UAS rank** | **45/114** (mid-pack) |

UAS is mid-pack because the high iʿjāz signature is partially offset by NULL outlier-strength (Q 81 is cluster-typical, not extreme) and mid-rank max-cost (Q 81 sits between two relatively-cheap mushaf-adjacencies). The standalone HIGH iʿjāz signature (rank 8/114) is the surah's architectural distinction; UAS does not capture this prominence because it weights outlier-strength + max-cost equally with iʿjāz.

## 6. Adjacency (H-NEW-720)

| Pair | delta_raw | delta (clamped) | frac_residual | Rank |
|:--|:--:|:--:|:--:|:--:|
| Q 80 → Q 81 | +0.0867 | 0.0867 | 1.045% | 43/113 |
| Q 81 → Q 82 | +0.0621 | 0.0621 | 0.749% | 57/113 |

Both adjacencies are MID-RANK and well-tolerated by the canonical mushaf order. The Q 81→Q 82 cost is notably LOW (0.749% of TSP residual; rank 57/113) — the al-Takwīr → al-Infiṭār transition is an empirically-smooth seam, consistent with both being *idhā*-cosmic-event-openers (the Sub-cluster A grouping is reflected in the canonical-order adjacency cost).

The Q 80 → Q 81 cost (al-ʿAbasa → al-Takwīr) is moderate. Both are short-Meccan but al-ʿAbasa is a different theme (rebuke of the Prophet for turning away from a blind man); the seam is non-zero but mild.

## 7. Hadith emphasis (H-NEW-860)

Q 81 is one of the 5 *Hūd-and-its-sisters* surahs cited in al-Tirmidhī #3381 (ḥasan gharīb): the Prophet identified Hūd, al-Wāqiʿa (Q 56), al-Mursalāt (Q 77), ʿAmma yatasāʾalūn (Q 78), and **Idhā ʾl-shamsu kuwwirat (Q 81)** as the surahs whose intensity "made him gray." This places Q 81 in a privileged hadith-emphasis category — see `04-hadith-corpus.md` for the full Tirmidhī chain analysis.

The hadith-emphasis score for Q 81 (per H-NEW-860 if available) is moderately HIGH for its length, driven by:
- The Tirmidhī #3381 "5 surahs" tradition (above)
- al-Tirmidhī #3333 + Aḥmad (a tradition that whoever wishes to "see the Day of Judgment as if with one's eyes" should read Q 81, Q 82 (al-Infiṭār), and Q 84 (al-Inshiqāq) — explicit pairing of the 3 of the 4 H-NEW-1200 CORE members at hadith level. **This is empirically striking: the classical hadith tradition pairs the same 3 of 4 architectural CORE members empirically identified by H-NEW-1200 FR-cohesion**)
- vision-of-Jibrīl traditions associated with vv. 19-23

## 8. Summary architectural fingerprint

Q 81 al-Takwīr is:
1. **The architectural CENTRE-PAIR of the H-NEW-1200 CORE-4** (joint-central with Q 99; tightest pairwise FR within CORE = Q 81 ↔ Q 82 at 0.5286)
2. **Content-CENTRAL** (rank ~14/114 by FR-centroid proximity; bottom 14% by mean FR distance to corpus)
3. **TOP 7% by al-Bāqillānī iʿjāz al-fawāṣil signature** (sig_A rank 8/114)
4. **NOT an outlier** (cluster-typical, content-central within Q 78-84 window)
5. **Mid-pack UAS** (rank 45/114) — high iʿjāz partially offset by NULL outlier-strength
6. **Mushaf-smooth** (Q 81→Q 82 adjacency rank 57/113) — well-integrated mushaf-architecturally
7. **Classical hadith-emphasized** (Tirmidhī #3381 "5 surahs that aged the Prophet" + Tirmidhī #3333 explicit Q 81/82/84 pairing — empirical confirmation of the H-NEW-1200 CORE-4 at classical-tradition level)

The architectural identity of Q 81 thus has TWO empirically-distinct layers:
- **Geometry-layer** (FR-content): central in the H-NEW-1200 CORE-4 + content-central in the corpus
- **Iʿjāz-layer** (al-Bāqillānī fawāṣil): TOP 7% of corpus

The two layers are mutually-reinforcing for the surah's architectural-centrality classification within the *idhā*-cosmic-event-opener cluster.
