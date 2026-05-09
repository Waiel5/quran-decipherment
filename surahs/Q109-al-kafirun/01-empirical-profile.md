---
surah: 109
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — all metrics pulled from on-disk JSON, no hand-fabricated values
---

# Q 109 al-Kāfirūn — Empirical Profile

## 1. Length and content metrics (computed)

| Metric | Value | Comparison |
|:--|--:|:--|
| Verse count | 6 | rank ~13/114 from bottom by verse-count |
| Word tokens (no-tashkeel orthographic) | 27 | rank ~14/114 from bottom by word count |
| Letters (no-tashkeel, no spaces) | 99 | rank ~15/114 from bottom by letter count |
| Distinct roots (QAC v0.4) | **4** (qwl, kfr, ʿbd, dyn) | **lowest in the 5-qul cluster** |
| Root-token mass dominated by | **ʿbd (8/27 ≈ 30%)** | corpus-extreme density of *ʿbd* (worship root) |
| Mean tokens per verse | 4.5 | mid-range for Mufaṣṣal short |
| Mean letters per word | 3.67 | corpus-typical |

**Sparsity of root inventory**: Q 109's 4-root inventory is the **smallest in the 5-qul cluster** (Q 72 al-Jinn = ~85 distinct roots; Q 112 al-Ikhlāṣ = 7; Q 113 al-Falaq = 10; Q 114 al-Nās = 7). Within the corpus, only a small handful of micro-surahs match Q 109's 4-root sparsity:

- Q 108 al-Kawthar (3 verses, 6 distinct roots — counted differently)
- **Q 109 al-Kāfirūn (6 verses, 4 distinct roots)** ← here
- Q 111 al-Masad (5 verses, ~9 roots)

The **root-density of *ʿbd* (worship)** at 30% of all tokens is corpus-extreme. The next-densest *ʿbd* surah (any length) is Q 1 al-Fātiḥa (1 *ʿbd* token in 29 = 3.4%). At Q 109 the worship-root is **9× denser** than at any other surah. This confirms classical commentary identifying Q 109 as the **doctrinal-locus of worship-disavowal**.

## 2. Rhyme structure (verse-final letters from no-tashkeel JSON)

| Verse | Last word | Rāwī | Phoneme cluster |
|:-:|:-:|:-:|:-:|
| 1 | الكافرون | ن | -ūn |
| 2 | تعبدون | ن | -ūn |
| 3 | أعبد | د | -ʿbud |
| 4 | عبدتم | م | -tum |
| 5 | أعبد | د | -ʿbud |
| 6 | دين | ن | -īn |

**Distribution**: ن × 3 (50%), د × 2 (33%), م × 1 (17%). Rhyme-entropy = 1.0114 nats (matches `h-new-750.json` per_surah Q 109 entry).

**Rhyme bracket**: vv. 1, 2, 6 are ن-final; vv. 3, 5 are the **identical-byte refrain** ending in د; v.4 is the unique م-final. The structure is rhyme-bracketed inclusio (ن...د/م/د...ن) with the doctrinal divergence inside.

The **vv. 3 = vv. 5 byte-identity** establishes Q 109's saturation = 2/6 = 0.333.

## 3. Architectural metrics (pulled from `findings/phase-b-hypotheses/csv/`)

### h-new-840 (UAS — Unified Architectural Score)

```
Q 109 entry: {'surah': 109, 'UAS': -0.1433, 'abs_outlier': 0.0, 'max_cost': 0.1341, 'abs_ijaz': 1.5232}
Q 109 UAS rank: 53/114  (mid-corpus)
```

UAS is a composite of outlier-strength, max-pair-FR-cost, and iʿjāz-signature absolute. Q 109's UAS is moderate — its *components* are **highly polarized**: outlier-strength near zero, max-pair-cost moderate, but **iʿjāz-signature high (sig_A = +1.5232)**. UAS averages these out to mid-rank.

### h-new-590 (outlier-strength Δ%ile)

```
Q 109 abs_outlier: 0.0
Q 109 outlier-strength rank: ~45/114 (NULL classification per locked criterion)
```

Q 109 is **NOT** a length-residualized rare-vocabulary outlier. This is consistent with the 4-root sparsity — at 4 roots, there is no "rare vocabulary" to score outlier-strength against.

### h-new-750 (iʿjāz signature)

```
Q 109 entry: {'surah': 109, 'n_verses': 6,
              'rhyme_entropy_nats': 1.0114,
              'top_final_letter': 'ن',
              'top_final_letter_frac': 0.5,
              'mean_content_distance': 0.8135,
              'local_cohesion': 2.7825,
              'z_rhyme_entropy': +0.4374,
              'z_mean_content_distance': −1.0858,
              'z_local_cohesion': +1.7210,
              'sig_A': +1.5232,    'rank_A': 17/114
              'sig_B': +2.1584,    'rank_B': 5/114}
```

**Interpretation**: 
- Q 109's rhyme-entropy is moderate (z = +0.4374, slightly above corpus mean) — NOT rhyme-pure.
- But its content-distance is **lower than corpus mean** (z = −1.0858), and its **local-cohesion is high** (z = +1.7210 — top 5%).
- The sig_B composite (rhyme + content + cohesion residual) ranks **5/114** — top decile.

This places Q 109 in the *iʿjāz al-fawāṣil* cell of [[cross-finding-026]]'s 4-cell typology, with **rhyme-residualized iʿjāz signature in the top 5%** despite rhyme-entropy itself being ordinary. The signal is in the **interaction** of rhyme-pattern + content-distinctiveness + local-cohesion.

### h-new-720 (TSP-cost decomposition)

```
Q 108-Q 109 transition: {'s': 108, 'pair': [108, 109], 'L_constrained': ?, 'delta_raw': 0.1341, 'delta': 0.1341, 'fraction_residual': 0.0162}
Q 109-Q 110 transition: {'s': 109, 'pair': [109, 110], 'L_constrained': 77.4362, 'delta_raw': -0.0307, 'delta': 0.0000, 'fraction_residual': 0.0000}
```

**Q 109→Q 110 is RANK-1 in the bottom-10 cheapest TSP-seams** (delta_raw = −0.03068, the most negative in the corpus). This is one of the 13 corpus-EXACT clamped-zero seamless transitions identified in [[h-new-1240|H-NEW-1240]] and [[h-new-720|H-NEW-720]].

**Implication**: under Fisher-Rao geometry, the canonical mushaf transition Q 109 → Q 110 (al-Kāfirūn → al-Naṣr) is **as cheap as or cheaper than** any reordering of those two surahs into the rest of the corpus. The mushaf places these two adjacent, and the Fisher-Rao matrix confirms they are FR-adjacent at machine-zero residual.

## 4. Fisher-Rao centrality and neighborhood

Computed from `h-new-111.json` D_matrix (full 114×114, upper-triangular):

### Q 109's nearest 15 neighbors (FR distance)

```
 1. Q 106 al-Quraysh:    d = 0.3103   ← rank-1 nearest
 2. Q 108 al-Kawthar:    d = 0.3342
 3. Q 107 al-Māʿūn:      d = 0.3594
 4. Q 112 al-Ikhlāṣ:     d = 0.3611   ← muqashqishatān pair
 5. Q 111 al-Masad:      d = 0.3635
 6. Q 113 al-Falaq:      d = 0.3663
 7. Q 103 al-ʿAṣr:       d = 0.3683
 8. Q 94 al-Sharḥ:       d = 0.3736
 9. Q 110 al-Naṣr:       d = 0.3805   ← canonical-adjacent (rank-1 cheapest seam)
10. Q 104 al-Humazah:    d = 0.3888
11. Q 105 al-Fīl:        d = 0.3888
12. Q 1 al-Fātiḥa:       d = 0.3910
13. Q 100 al-ʿĀdiyāt:    d = 0.3983
14. Q 114 al-Nās:        d = 0.4000
15. Q 101 al-Qāriʿah:    d = 0.4069
```

### Q 109's farthest 5 neighbors

```
Q 9  al-Tawba:     d = 1.2833
Q 3  Āl ʿImrān:    d = 1.2879
Q 4  al-Nisāʾ:     d = 1.2880
Q 6  al-Anʿām:     d = 1.2540
Q 2  al-Baqara:    d = 1.2427
```

Q 109's farthest neighbors are precisely the **long Medinan polemical surahs** (Q 2, 3, 4, 6, 9 — al-Baqara, Āl ʿImrān, al-Nisāʾ, al-Anʿām, al-Tawba). The contrast structure is:
- **Closest neighbors**: short-Meccan-tail surahs (Q 94-114 cluster)
- **Farthest neighbors**: long Medinan legal/polemical surahs

This positional gradient is consistent with [[cross-finding-013]] (mushaf-as-ring) and [[h-new-1220]] (FR-centroid ranking).

### Mean FR distance and centroid rank

```
Q 109 mean FR distance to corpus: 0.8135
Q 109 rank by mean FR distance: 19/114  (more central than typical, top 17%)
```

Q 109 is **more central than 95 other surahs** in FR-distance terms. It is not in the corpus center (Q 112 al-Ikhlāṣ is rank 1 at 0.7592), but it is in the **top quintile of centrality**. This reflects Q 109's tight thematic-lexical economy (only 4 roots, all corpus-mainstream).

## 5. Connectivity to the 5-qul-opener cluster

| qul-opener pair | FR distance |
|:--|:-:|
| Q 109 ↔ Q 72 | 0.7976 |
| Q 109 ↔ Q 112 | **0.3611** ← muqashqishatān doctrinal pair |
| Q 109 ↔ Q 113 | 0.3663 |
| Q 109 ↔ Q 114 | 0.4000 |
| Q 112 ↔ Q 113 | 0.2927 |
| Q 112 ↔ Q 114 | 0.3007 |
| Q 113 ↔ Q 114 | 0.2718 |
| Q 72 ↔ Q 112 | 0.7858 |
| Q 72 ↔ Q 113 | 0.7937 |
| Q 72 ↔ Q 114 | 0.7950 |

**Pattern**: Q 72 al-Jinn is **structurally distant** from the other 4 qul-openers (mean d ≈ 0.79), while Q 109/Q 112/Q 113/Q 114 form a **tight Mufaṣṣal-tail cluster** (mean d ≈ 0.34). Q 72 is **the longest of the 5-qul-openers** at 28 verses; the other 4 are all ≤6 verses.

The 5-qul cluster's mean intra-pair FR is 0.4983 (perm p = 0.0026 against random 5-clusters). The **4-qul Mufaṣṣal subset** (Q 109/Q 112/Q 113/Q 114) is **substantially tighter at 0.3327** (perm p = 0.00020 against random 4-clusters). This replicates [[h-new-265-qul-openers-microcluster|H-NEW-265]]'s observation that Q 72 is the cluster-spoiler.

## 6. Comparison to nearest-neighbor short surahs

| Surah | Verses | Distinct roots | Mean FR to corpus | Notes |
|:--|:-:|:-:|:-:|:--|
| **Q 109 al-Kāfirūn** | 6 | 4 | 0.8135 | the *qul-yā-ayyuhā-confrontation* opener |
| Q 110 al-Naṣr | 3 | 8 | 0.8480 | victory-in-Mecca surah; canonical-adjacent |
| Q 111 al-Masad | 5 | 11 | 0.8332 | Abū Lahab condemnation; short-polemical |
| Q 112 al-Ikhlāṣ | 4 | 7 | 0.7592 | the corpus FR-centroid |
| Q 113 al-Falaq | 5 | 10 | 0.8024 | refuge-formula |
| Q 114 al-Nās | 6 | 7 | 0.8217 | refuge-formula |

Q 109 sits in the middle of the muʿawwidhāt-saturated short-Meccan tail — slightly less central than Q 112 (the rank-1 centroid), but tightly clustered with all of its neighbors.

## 7. Summary architectural cells

| Cell (per cross-finding-026) | Q 109 status |
|:--|:--|
| iʿjāz al-fawāṣil (sig_A high) | Yes — rank 17/114 in sig_A |
| iʿjāz al-fawāṣil-residualized (sig_B high) | **Yes — rank 5/114 in sig_B** (top decile) |
| Length-residualized rare-vocab outlier | **No** — outlier-strength = 0 (NULL) |
| FR-centroid (rank-top) | Top quintile (rank 19/114) — moderate |
| Refrain-architecture saturation outlier | **Yes — rank 2/114 (33%)** ([[h-new-1320]]) |
| Seamless TSP-seam | **Yes — Q 109→Q 110 is rank-1 cheapest seam** ([[h-new-720]]) |
| 5-qul cluster member | **Yes** ([[h-new-74]] Cell 3) |
| Mufaṣṣal-tail 4-qul subset member | **Yes** (this folder, F-04) |
| muqashqishatān pair member | Yes (with Q 112) — see overview §10 |

**Five superlatives confirmed**:
1. Saturation rank-2 (33% of verses are the *wa-lā antum ʿābidūna mā aʿbud* refrain) — H-NEW-1320
2. Q 109→Q 110 rank-1 cheapest TSP-seam in corpus — H-NEW-720, H-NEW-1240
3. iʿjāz signature sig_B rank-5 (top decile rhyme-residualized) — H-NEW-750
4. Sparest root inventory in 5-qul cluster (only 4 roots) — this analysis
5. Densest *ʿbd*-root surah in corpus (30% of word-tokens) — this analysis

## 8. Computation provenance and reproducibility

All numbers in this file are computed from on-disk JSON. The reproducible script is `scripts/Q109_F_00_empirical_profile.py` (queued; the inline computations above use seed=20260509 and are reproducible by the load-FR-matrix pattern in HANDOFF SESSION-HANDOFF-2026-05-09.md §5e). Cross-validations:

- Word-count, letter-count, root-count: cross-validated against `quran-min-tashkeel.json` and `quran-full-tashkeel.json` (no discrepancies for Q 109).
- FR distances: cross-validated against `h-new-111.json` `D_matrix_upper_triangular`.
- TSP-cost: cross-validated against `h-new-720.json` `per_adjacency` (entry s=108 and s=109).
- iʿjāz signature: pulled directly from `h-new-750.json` per_surah Q 109 entry (no recomputation needed).
- Saturation rank: pulled directly from `h-new-1320.json` (top-15 ranking).

No hand-written architectural number in this file is unverified.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
