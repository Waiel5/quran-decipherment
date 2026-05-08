---
surah: 21
surah_name_ar: الأنبياء
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE
---

# Q 21 al-Anbiyāʾ — Empirical Profile

## 1. UAS rank

| Metric | Value | Source |
|:--|:--|:--|
| **UAS** | **1.705** | [[h-new-840-unified-architectural-score|H-NEW-840]] |
| **UAS rank** | **16 / 114** | derived (sorted descending) |
| abs_outlier component | 5.710 | H-NEW-840 |
| max_cost component | 0.1776 | H-NEW-840 (the Q 21–Q 22 adjacency) |
| abs_iʿjāz component | 1.865 | H-NEW-840 (= |sig_A|) |

Q 21 is in the **top 14% by UAS** but its composition is *non-canonical*: the high UAS comes from the |iʿjāz| component (because sig_A is extreme-LOW = −1.865, anti-fawāṣil) plus a top-15 right-adjacency cost. Outlier is moderate.

## 2. Outlier-strength (H-NEW-590)

| Metric | Value |
|:--|:--|
| Window | [Q 18, 19, 20, 21, 22, 23, 24] |
| d̄_W (with Q 21) | 0.9819 |
| d̄_W − Q 21 (without) | 1.0005 |
| Δ%ile | **−5.71 pp** |
| p_greater_W | 0.2286 |
| Classification | **WEAK_ANCHOR** |

⭐ Q 21 is **NOT** an outlier — it's a **weak anchor**: removing Q 21 *increases* the window's mean content distance. Q 21 holds its 7-window together (it sits between Q 18 al-Kahf, Q 19 Maryam, Q 20 Ṭā-Hā on the left and Q 22 al-Ḥajj, Q 23 al-Muʾminūn, Q 24 al-Nūr on the right — a heavy prophet-narrative block whose internal cohesion is partially carried by Q 21).

## 3. iʿjāz signature (H-NEW-750)

| Metric | Value | Rank |
|:--|:--|:--|
| `rhyme_entropy_nats` | 0.209 | **100 / 114** (very low) |
| `top_final_letter` | ن | — |
| `top_final_letter_frac` | **0.946** | — |
| `mean_content_distance` | 1.010 | — |
| `local_cohesion` | 1.099 | — |
| `z_rhyme_entropy` | −1.016 | — |
| `z_mean_content_distance` | +0.849 | — |
| `z_local_cohesion` | −0.571 | — |
| **`sig_A` = z(rhyme_entropy) − z(content_distance)** | **−1.865** | **100 / 114** |
| **`sig_B` = z(rhyme_entropy) − z(local_cohesion)** | −1.587 | 104 / 114 |

⭐ Q 21 is **anti-iʿjāz-al-fawāṣil**: rhyme is uniform ON the long-fāṣila ن-ending while content distance is HIGHER than corpus mean. Per [[cross-finding-026-iʿjāz-architecture|cross-finding-026]], Q 21 is in the *anti-iʿjāz* zone of the content × rhyme anti-twin lock.

## 4. Compression-tail position

Q 21 is at s=21, well before the compression-tail kink (s=50). The compression-tail law `d̄_content(s) ≈ 0.96 − 0.012 · max(0, s−50)` predicts d̄_content ≈ 0.96 in the head zone, and Q 21's observed d̄ = 1.010 is slightly above prediction (consistent with WEAK_ANCHOR status — Q 21 is a touch more content-distant than head-zone average).

## 5. Phoneme & rhyme details

- Final-letter monorhyme on **ن** at 94.6 % (106 / 112 verses).
- 6 verses end in م (Q 21:46, 49, 53, 57, 70, 89 are the candidate م-enders by inspection — verified by computation).
- The two-letter alphabet of fāṣila endings (ن + م) is among the corpus-tightest. Compare Q 12 Yūsuf (ن 84%, м 14%, ر 2%, ل 1%).

## 6. Canonical-adjacency costs (H-NEW-720)

| Pair | δ (FR-units) | Fraction of TSP residual | Rank |
|:--|:--|:--|:--|
| Q 20 → Q 21 | 0.0544 | 0.66% | 64 / 113 |
| **Q 21 → Q 22** | **0.1776** | **2.14%** | **16 / 113** |

Q 21 has a **modestly cheap left boundary** (Q 20 Ṭā-Hā transition) but a **costly right boundary** (Q 21 → Q 22). The Q 21–Q 22 cost is the most expensive single-pair cost within the entire Q 16 → Q 27 mushaf segment. See `Q021-F-05` for the joint Q 21 + Q 22 structural test.

## 7. True-isolate cluster context (H-NEW-126)

Q 21 is one of **5 TRUE-ISOLATE surahs**: {Q 16, 21, 22, 23, 25}. Invisible to all 20 cluster-detection systems used in the project. The project's prior synthesis ([[cross-finding-026-iʿjāz-architecture|cross-finding-026]]) does not place Q 21 in any of the 4 named cells; it instead sits on the *Structural-twin-pair-of-one* tail, sharing membership with Q 22 and Q 23.

## 8. Architectural type classification

By H-NEW-840 + H-NEW-750 + H-NEW-590 + H-NEW-720 inputs:
- High UAS (rank 16) → not low.
- |sig_A| high but sig_A *negative* → anti-fawāṣil pole.
- Outlier WEAK_ANCHOR → not a content-outlier.
- Right-adjacency cost rank 16 → moderately costly.

⇒ Architectural cell: **anti-iʿjāz / structural-twin-pair sui-generis (true-isolate)**. Q 21 is the *prophet-cycle-density* archetype with sustained nūn-monorhyme, mid-content-distance, and a costly right-boundary.

## 9. Q 21 nearest- / farthest-neighbor structure on FR-roots

Computed in `scripts/Q021_F_03_isolation_test.py` (top-K=500 STEM roots, Dirichlet α=0.5, L1-normalize, Fisher-Rao distance):

| Metric | Value |
|:--|:--|
| Mean d to corpus | computed in F-03 |
| Mean d to 5 nearest neighbors | computed in F-03 |
| 5 nearest surahs by FR-distance | computed in F-03 |
| 5 farthest surahs | computed in F-03 |
| Q 21 isolation rank (high d to nearest-5 = more isolated) | computed in F-03 |

See `Q021-F-03-isolation-prereg.md` and `csv/Q021-F-03.json`.

## 10. Cross-references to all H-NEW findings touching Q 21

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]]: Q 21 row of 114×114 FR distance matrix (recomputed in `scripts/Q021_F_03_isolation_test.py`).
- [[h-new-590-outlier-spectrum|H-NEW-590]]: Q 21 = WEAK_ANCHOR (Δ%ile = −5.71 pp, p=0.2286).
- [[h-new-700-phonological-compression-tail|H-NEW-700]]: Q 21 nūn-monorhyme 94.6 %, 112 verses.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]]: Q 21 → Q 22 = 2.14 % residual, rank 16 / 113.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]]: Q 21 sig_A = −1.865 (rank 100), sig_B = −1.587 (rank 104).
- [[h-new-840-unified-architectural-score|H-NEW-840]]: Q 21 UAS rank 16 / 114.
- H-NEW-126: Q 21 ∈ 5 true-isolate surahs.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2: Q 21 not in any of the 4 named cells (true-isolate); Wave-D fit is the structural-twin-pair-of-one sui-generis tail.

## 11. Honest limits

- Q 21 outlier-strength p=0.2286 is far from significant — the WEAK_ANCHOR label is a *descriptive* classification, not a statistically-strong claim.
- Rhyme-entropy 0.209 nats is a 2-letter alphabet metric; richer fāṣila analyses (vowel-coda, syllabic) might reveal sub-structure not visible at letter-level.
- The true-isolate label (H-NEW-126) means "invisible to 20 cluster systems"; this is itself a NULL-on-cluster-membership, not a positive signature. Q 21's positive signature is its prophet-catalog density (Q021-F-01) and its costly right-boundary (H-NEW-720), not its outlier-strength.
