---
surah: 29
surah_name_translit: al-ʿAnkabūt
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: "Q 29 architectural-signature: UAS rank 44 (moderate); WEAK_ANCHOR (Δ%ile −7.34, content-cohesive); rhyme nūn 86%; mid-tail content-distance (d̄=0.998); iʿjāz al-fawāṣil moderate (sig_A rank 90)"
---

# Q 29 al-ʿAnkabūt — Empirical Profile

This file integrates pre-computed empirical metrics on Q 29 from project artifacts.

## Source files

- H-NEW-111 (FR distance matrix): `findings/phase-b-hypotheses/csv/h-new-111.json`
- H-NEW-590 (outlier-strength): `findings/phase-b-hypotheses/csv/h-new-590.json` (X=29)
- H-NEW-700 (rhyme + phoneme): `findings/phase-b-hypotheses/csv/h-new-700.json`
- H-NEW-720 (TSP-cost): `findings/phase-b-hypotheses/csv/h-new-720.json` (pair=[28,29] and [29,30])
- H-NEW-750 (iʿjāz signature): `findings/phase-b-hypotheses/csv/h-new-750.json` (per_surah[29])
- H-NEW-840 (UAS): `findings/phase-b-hypotheses/csv/h-new-840.json`

## 1. Unified Architectural Significance — H-NEW-840

| Component | Q 29 value | Source |
|:--|:-:|:--|
| UAS (composite) | **+0.158** | h-new-840 `all_uas` |
| abs_outlier | 7.34 | h-new-840 |
| max_neighbor_TSP_cost | 0.0746 | h-new-840 |
| abs_iʿjāz signature | 1.218 | h-new-840 |

**UAS rank**: **44 / 114**. Q 29 is a moderate-architectural-significance surah — neither in the top-15 (Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17 etc.) nor in the bottom-10. It contributes a moderate-iʿjāz-signature plus moderate-outlier-anchor strength.

## 2. Outlier strength — H-NEW-590

```json
{"X": 29, "window": [26, 27, 28, 29, 30, 31, 32],
 "window_minus_X": [26, 27, 28, 30, 31, 32],
 "d_W": 0.9455, "d_W_minus_X": 0.9606,
 "pct_W": 54.4, "pct_W_minus_X": 61.74,
 "delta_pct": -7.34, "p_greater_W": 0.456,
 "classification": "WEAK_ANCHOR"}
```

Removing Q 29 from the 7-window centered at s=29 INCREASES the window's mean content-distance percentile (the window becomes more dispersed without Q 29). Equivalently: Q 29 is content-COHESIVE within its mushaf-neighborhood — its presence holds the window together. **Q 29 is a WEAK_ANCHOR**, opposite to Q 30's WEAK_OUTLIER profile.

This is a notable Q 29 vs Q 30 dissociation:
- Q 29: WEAK_ANCHOR (Δ%ile = −7.34) — content-cohesive.
- Q 30: WEAK_OUTLIER (Δ%ile = +3.64) — content-dispersive.

The two surahs serve OPPOSITE structural roles in their shared 7-window neighborhood.

## 3. iʿjāz signature — H-NEW-750

```json
{"surah": 29, "n_verses": 69,
 "rhyme_entropy_nats": 0.5023, "top_final_letter": "ن",
 "top_final_letter_frac": 0.855,
 "mean_content_distance": 0.998, "local_cohesion": 1.127,
 "z_rhyme_entropy": -0.484, "z_mean_content_distance": +0.734,
 "z_local_cohesion": -0.533,
 "sig_A": -1.218, "sig_B": -1.017,
 "rank_A": 90, "rank_B": 80}
```

**Interpretation**:
- Q 29 has moderate-low rhyme entropy (0.502 nats; z=-0.484) — rhyme moderately consolidated (less than Q 30's 0.389).
- 86% of Q 29's 69 verses end in nūn (vs Q 30's 90%).
- Content distance d̄ = 0.998 — moderately above corpus mean (0.96).
- `sig_A` rank 90/114 — Q 29 is a structural-iʿjāz signature surah, slightly less extreme than Q 30 (rank 97).

## 4. Compression-tail prediction (H-NEW-660)

For s=29 (head-pole, s ≤ 50), predicted d̄_content = 0.96. Observed d̄ = 0.998. Residual: +0.038 (slightly above law-prediction).

## 5. Canonical adjacency — H-NEW-720

| Pair | δ | fraction_residual |
|:--|:-:|:-:|
| Q 28 → Q 29 | 0.0746 | 0.0090 |
| Q 29 → Q 30 | 0.0293 | 0.0035 |

Q 28 → Q 29 is more expensive than Q 29 → Q 30. The Q 29 → Q 30 adjacency is content-cheap (the muqaṭṭāʿat shared opener Q 28 ṬSM → Q 29 ALM may be partly responsible for the higher Q 28 → Q 29 cost).

## 6. Fisher-Rao distance neighbors — H-NEW-111

Pairwise FR distance to ALM-cluster:

| Pair | d_FR |
|:--|:-:|
| **Q 29 ↔ Q 30** | **0.9153** |
| Q 29 ↔ Q 31 | 0.8963 |
| Q 29 ↔ Q 32 | 0.9382 |
| Q 29 ↔ Q 2 | 0.8489 |
| Q 29 ↔ Q 3 | 0.8420 |

Q 29's CLOSEST FR-neighbor in ALM cluster is Q 3 (0.842), then Q 2 (0.849), then Q 31 (0.896). Q 30 (0.915) is RANK-7-of-15 in the within-ALM frame. **Q 29's content-FR-twin is NOT Q 30; it's Q 3.**

This is consistent with the [[Q030-F-04-architectural-twin-prereg|Q030-F-04]] finding that Q 29 + Q 30 are NOT a content-cohesion-twin pair despite their shared book-reference-exception status.

## 7. Architectural type classification

Per the dual-iʿjāz typology:
- Q 29 sits in the structural-iʿjāz quadrant but at moderate strength (UAS +0.158, sig_A rank 90).
- The WEAK_ANCHOR classification places Q 29 in the LOW-OUTLIER-STRENGTH cohort.

## 8. Cross-references to H-NEW findings

- [[h-new-53-muqattaat-book-reference|H-NEW-53]]: Q 29 = 1 of 2 ALM-cluster exceptions to book-reference pattern.
- [[h-new-93-q29-q30-subpattern|H-NEW-93]]: parent NULL. Q 29 imtihān-density is 8.20/k (well above Meccan baseline 5.05).
- [[cross-finding-008-muqattaat-book-introduction-marker-synthesis|Cross-finding-008]]: anchor finding for Q 29's exception-status.
- H-NEW-660 compression-tail: Q 29 d̄ near law-prediction at head-pole.

## Honest limits

- The WEAK_ANCHOR classification has p_greater_W = 0.456 — statistically indistinguishable from null. The interpretation must be modest.
- The Q 29 vs Q 30 anchor-vs-outlier asymmetry is REAL at the descriptive level but neither passes a permutation null at p<0.05.
- The 86% nūn-rhyme is a Late-Meccan default, not unique to Q 29.
