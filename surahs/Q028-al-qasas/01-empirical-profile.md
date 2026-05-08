---
surah: 28
surah_name_ar: القصص
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: integrated
---

# Q 28 al-Qaṣaṣ — Empirical profile

All values computed from on-disk JSON; cross-verified against `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-{111,590,700,720,750,840}.json`.

## 1. UAS triple (H-NEW-840)

| Component | Value | Source |
|:--|--:|:--|
| **UAS** | **−0.041** | h-new-840.json `all_uas` Q 28 |
| Rank | **50/114** | sorted desc by UAS |
| abs_outlier | 1.84 | from H-NEW-590 |
| max_cost | 0.0746 | from H-NEW-720 (Q 28→Q 29) |
| abs_iʿjāz | 1.794 | from H-NEW-750 sig_A magnitude |

Architectural-type classification: **moderate / unremarkable** by aggregated UAS. The three components disagree slightly — Q 28 has below-average iʿjāz al-fawāṣil (large negative sig_A) and unremarkable outlier-strength.

## 2. Outlier-strength spectrum (H-NEW-590)

`/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json` `all_surahs_results` Q 28:

- Window: [25, 26, 27, 28, 29, 30, 31] (window-7 centered roughly on Q 28).
- d̄_W = 0.9499.
- d̄_W − Q 28 = 0.9557.
- pct_W = 57.08; pct_W − Q 28 = 58.92.
- Δ%ile = **−1.84pp** → **NULL classification** (neither outlier nor anchor).
- p_perm = 0.4292 (n.s.).

Q 28 is **not** a window-distinguishing element for its mid-mushaf-zone — its content profile is consistent with its neighbors Q 25-31.

## 3. iʿjāz signature (H-NEW-750)

`/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json` `per_surah` Q 28:

| Field | Value |
|:--|--:|
| n_verses | 88 |
| top_final_letter | **ن** (nūn) |
| top_final_letter_frac | **0.9205** |
| rhyme_entropy_nats | 0.3635 |
| mean_content_distance | 1.0308 |
| local_cohesion | 1.1063 |
| z_rhyme_entropy | −0.7358 |
| z_mean_content_distance | +1.0586 |
| z_local_cohesion | −0.5612 |
| **sig_A** | **−1.7944** (rank 98/114) — LOW iʿjāz al-fawāṣil |
| sig_B | −1.2970 (rank 94/114) |

The sig_A and sig_B both fall in the bottom quartile, consistent with Q 28's near-monorhyme nūn-ending pattern (a Mosesic / prophet-narrative surah feature shared with Q 12, Q 27, Q 26).

## 4. Compression-tail position (H-NEW-660 / H-NEW-700)

Q 28 sits at position s=28, well before the s=50 Hijra-kink:

- Predicted d̄_content under H-NEW-660 fitted equation: 0.96 (no kink correction applies for s ≤ 50).
- Observed d̄_content = 1.0308 → +0.07 above the head-mushaf zone trend; mild content-distinctness.
- Predicted d̄_rhyme under H-NEW-700 (two-piece-kink-50 model): 0.36 (head zone).
- Observed rhyme entropy 0.3635 nats → near-baseline expectation for head-mushaf zone.

Q 28 is **on-trend** for its mushaf-position; nothing about its compression-tail behavior is anomalous.

## 5. Phoneme density (H-NEW-700 layer)

[Not computed in H-NEW-700 at the per-surah granularity for Q 28 specifically; the phoneme dispersion-tail fit is corpus-wide R²=0.946. Q 28 falls within head-zone band; deeper per-phoneme analysis deferred to a future agent.]

## 6. Canonical-adjacency costs (H-NEW-720)

`/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json` `per_adjacency`:

| Pair | L_constrained | Δ_raw | fraction_residual |
|:--|--:|--:|--:|
| Q 27 → Q 28 | 77.526 | 0.0592 | 0.71% |
| Q 28 → Q 29 | 77.541 | 0.0746 | 0.90% |

Both adjacencies are **low-residual** (i.e., the canonical Q 27→Q 28→Q 29 sequence is near TSP-optimal — Q 27 and Q 28 are close in content-space, and Q 28 and Q 29 al-ʿAnkabūt are also close). Neither pair appears in the H-NEW-720 top-10 expensive list.

## 7. FR-distance landscape (H-NEW-111)

Q 28's full FR-distance row (extracted from `D_matrix_upper_triangular`):

**Closest 10 surahs to Q 28** (FR distance, ascending):
1. **Q 7 al-Aʿrāf** — 0.762 (Mosesic surah; longest single-block Mosesic narrative outside Q 20)
2. **Q 27 al-Naml** — 0.805 (TSM-sister; Mosesic-prophetic mix)
3. **Q 10 Yūnus** — 0.843 (Mosesic + Yūnus)
4. Q 6 al-Anʿām — 0.844
5. Q 11 Hūd — 0.853
6. Q 41 Fuṣṣilat — 0.853
7. Q 40 Ghāfir — 0.855 (Pharaoh-context)
8. Q 46 al-Aḥqāf — 0.873
9. Q 23 al-Muʾminūn — 0.879
10. Q 18 al-Kahf — 0.879

**Farthest 5 from Q 28**:
- Q 82 al-Infiṭār — 1.169
- Q 88 al-Ghāshiya — 1.187
- Q 80 ʿAbasa — 1.188
- Q 56 al-Wāqiʿa — 1.205
- **Q 55 al-Raḥmān — 1.353** (the rāwī-fixed pinnacle)

**Mean FR-distance to other 113**: **1.031** — slightly above corpus mean. Q 28 is moderately content-distinct.

**Critical observation for Q028-F-02**:
- Q 28 ↔ **Q 26** = 0.954 (mid-range)
- Q 28 ↔ **Q 27** = **0.805** (close)
- Q 28 ↔ **Q 20** = 0.895
- Q 26 ↔ Q 27 = 0.959
- Q 26 ↔ Q 20 = 0.956
- Q 27 ↔ Q 20 = 0.928

Q 28 is **closer to Q 27 (0.80) than to Q 26 (0.95) or Q 20 (0.90)**. The TSM-pair Q 26-Q 28 has FR-distance 0.954 — *higher* than either Q 26-Q 20 (0.956) or Q 28-Q 20 (0.895). This is consistent with the F-02 cosine result (where Q 28-Q 20 cosine 0.82 exceeds Q 26-Q 28 cosine 0.67).

## 8. Architectural-type classification

| Axis | Q 28 verdict |
|:--|:--|
| Structural-iʿjāz (al-Bāqillānī) | **moderate** — UAS −0.04, rank 50/114; not in top quintile |
| Theological-iʿjāz (al-Khaṭṭābī) | **HIGH ANCHOR** — Q 28:88 *kullu shayʾin hālikun illā wajhah* is one of the premier iʿjāz-of-meaning verses (al-Rāzī commentary cite); see `05-classical-claims-audit.md` §C-3 |
| Anti-iʿjāz | not applicable |
| Compression-tail | **on-trend** — head-mushaf zone, no anomaly |
| Outlier | **NULL** — neither cohesion-anchor nor outlier |
| Letter-family | **TSM** — third member of Q 26-27-28 cluster |
| Content-cluster | **Mosesic-prophet-narrative** (closest neighbors are Q 7, 10, 11, 18, 27 — all prophet-narrative surahs) |

## 9. Sanity / replication notes

- All h-new-* JSONs accessed via the prereg-locked SHAs in their respective files. Q 28's row in each is internally consistent.
- The fact that Q 28's nearest FR-neighbor is Q 7 (not Q 27 the immediate ṬS-sister) is an important architectural fact: **content-cluster ≠ letter-cluster** — exactly the conclusion of `[[h-new-720]]` Wave-FALSIFIED §3.7. Q 28's content-pull is toward Q 7 (al-Aʿrāf, large Mosesic) more than toward its ṬSM-letter-mate Q 26.
- However, the second-closest neighbor IS Q 27 (TSM-sister), so the letter-cluster effect is non-zero but secondary to content.

## 10. Cross-references to H-NEW network

- [[h-new-111-fisher-rao-distance-matrix|H-NEW-111]] — Q 28 nearest = Q 7 (0.76).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 28 Δ%ile −1.84pp NULL.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 28 nūn-rhyme 92.0%, on-trend for head-zone.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 27→Q 28 residual 0.71%, Q 28→Q 29 residual 0.90%.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — Q 28 sig_A −1.79, rank 98/114.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 28 UAS rank 50/114.
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 28 sits in head-mushaf zone, pre-Hijra-kink.
- [[h-new-770-verse-length-compression-tail|H-NEW-770]] — average verse length 1438/88 = 16.34 words/verse — head-zone consistent.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 28 fits structural-iʿjāz / theological-iʿjāz dual-axis.
