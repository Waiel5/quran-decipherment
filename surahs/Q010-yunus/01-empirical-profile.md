---
surah: 10
surah_name: Yūnus
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — all H-NEW metrics integrated
---

# Q 10 Yūnus — Empirical architectural profile


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

## 1. Headline metrics (all from `findings/phase-b-hypotheses/csv/`)

| Metric | Value | Source | Interpretation |
|:--|:-:|:--|:--|
| UAS rank | **8 / 114** | `h-new-840.json` top_15 | top-decile architectural significance |
| UAS score | 3.479 | `h-new-840.json` | composite z-sum |
| Outlier strength Δ | **−7.83 pp** | `h-new-590.json` bottom_10_anchors[1] | **WEAK_ANCHOR** — exclusion of Q 10 weakens cohesion structure by ≈7.83pp |
| Outlier classification | WEAK_ANCHOR | `h-new-590.json` | mild cohesion-positive contributor |
| iʿjāz signature sig_A | −1.978 | `h-new-750.json` per_surah | rank 102/114 — VERY LOW window-level iʿjāz |
| iʿjāz signature sig_B | −1.412 | `h-new-750.json` per_surah | rank 99/114 — also low |
| Rhyme entropy (nats) | 0.358 | `h-new-700.json` (per_surah equivalent) | very low — near-monorhyme |
| Top final letter | ن (nūn) | computed from min-tashkeel | 89.9% of verse-finals |
| Mean content distance | 1.048 | `h-new-750.json` | z=+1.23 above corpus mean — content-distinct |
| Local cohesion | 1.029 | `h-new-750.json` | z=−0.67 below mean — verse-block cohesion is tight |
| **Q9-Q10 TSP cost** | **0.309** | `h-new-720.json` per_adjacency s=9 | **rank 4/113 most-expensive** = 3.73% of total residual |
| **Q10-Q11 TSP cost** | **0.030** | `h-new-720.json` per_adjacency s=10 | very cheap (rank ~80) |
| Position s | 10 | canonical | head-mushaf zone (pre-Hijra-kink at s=50) |
| d̄_content position | 0.96 + |10−50|×0 = 0.96 | H-NEW-660 law (s≤50 plateau) | within-plateau |

## 2. UAS decomposition

UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|sig_A|), per H-NEW-840 method.

For Q 10 (`h-new-840.json` top_15 entry rank 8):
- |outlier| = 7.83
- max_neighbor_TSP_cost = 0.30938 (Q9-Q10)
- |sig_A| = 1.9778

The dominant contributor is **canonical-adjacency cost** (the Q9-Q10 transition). The iʿjāz contribution is moderate-negative (its absolute value is high in the wrong direction — Q 10 has VERY LOW iʿjāz). The outlier contribution is moderate.

This is a different UAS-profile from Q 33 (rank 1, dominated by outlier-strength) or Q 12 (rank 6, dominated by outlier + canonical-cost). **Q 10's architectural significance is dominated by the chronology-block boundary it sits on.**

## 3. Fisher-Rao neighborhood (from `h-new-111.json`)

### Q 10 nearest 8 neighbors (FR-stem-roots distance)

| Rank | Surah | Distance | Note |
|:-:|:-:|:--:|:--|
| 1 | **Q 6 al-Anʿām** | 0.7396 | late-Meccan theological-polemic |
| 2 | **Q 7 al-Aʿrāf** | 0.7416 | late-Meccan; prophet-narratives + polemic |
| 3 | Q 27 al-Naml | 0.7919 | prophet-narrative (Sulaymān, Mūsā) |
| 4 | Q 29 al-ʿAnkabūt | 0.7927 | early/mid-Meccan; prophet-narratives + polemic |
| 5 | Q 39 al-Zumar | 0.8003 | tawḥīd-polemic |
| 6 | Q 40 Ghāfir | 0.8033 | ḥawāmīm; tawḥīd-polemic + Mūsā-Pharaoh |
| 7 | Q 45 al-Jāthiyah | 0.8049 | ḥawāmīm; tawḥīd-polemic |
| 8 | **Q 11 Hūd** | 0.8052 | ALR-cluster sibling |

**Critical empirical finding**: Q 10's nearest 7 neighbors are NOT the ALR cluster — they are the **late-Meccan theological-polemic group** (Q 6, 7, 27, 29, 39, 40, 45). The ALR sibling Q 11 enters only at rank 8. Q 12 Yūsuf is at distance 1.006 (rank ~30+). The cluster is letter-class-defined, not content-defined — confirming H-NEW-600 NULL.

### Q 10 farthest 5

| Surah | Distance | Note |
|:--|:--:|:--|
| Q 55 al-Raḥmān | 1.361 | iʿjāz-of-fawāṣil specialist |
| Q 80 ʿAbasa | 1.256 | mufaṣṣal-qiṣār |
| Q 56 al-Wāqiʿa | 1.240 | post-Hijra-kink; eschatological |
| Q 88 al-Ghāshiya | 1.231 | mufaṣṣal-qiṣār |
| Q 94 al-Sharḥ | 1.228 | mufaṣṣal-qiṣār |

The farthest set is mufaṣṣal-qiṣār (Q 55, 80, 88, 94) — the iʿjāz-peak zone. Q 10 sits empirically at the OPPOSITE end of the iʿjāz axis.

## 4. iʿjāz signature analysis (`h-new-750.json` per_surah)

```
{
  "surah": 10, "n_verses": 109,
  "rhyme_entropy_nats": 0.3578,
  "top_final_letter": "ن",
  "top_final_letter_frac": 0.8991,
  "mean_content_distance": 1.0483,
  "local_cohesion": 1.0290,
  "z_rhyme_entropy": -0.7460,
  "z_mean_content_distance": +1.2318,
  "z_local_cohesion": -0.6664,
  "sig_A": -1.9779,
  "sig_B": -1.4125,
  "rank_A": 102,
  "rank_B": 99
}
```

sig_A = z_rhyme_entropy − z_mean_content_distance + z_local_cohesion (per H-NEW-750 spec).

Decomposition for Q 10:
- z_rhyme_entropy = −0.746 (low entropy contribution, strongly anti-iʿjāz: low rhyme variety)
- z_mean_content_distance = +1.232 (high content distance: content is "outside-the-corpus" — but for sig_A this is anti-iʿjāz because iʿjāz al-fawāṣil rewards LOW content-distance combined with HIGH rhyme-variety)
- z_local_cohesion = −0.666 (highly cohesive locally — verses cluster tightly)

Q 10 is empirically **anti-iʿjāz** at the window level: low rhyme variety + high content-distance. This is consistent with: **near-monorhyme on -ūn/-īn + content-block-distinctness from corpus norm**. It is the "monolithic-discourse" type — verbally uniform within, content-uniform within, content-distinct from outside.

This is the same anti-iʿjāz signature as Q 17, 18, 33, 48, 54 (per H-NEW-750 bottom-10 sig_A list).

## 5. Compression-tail position (H-NEW-660, H-NEW-700, H-NEW-770)

s = 10 → in the **pre-kink plateau** for all four laws:
- d̄_content(s=10) ≈ 0.96 (plateau before kink at s=50)
- d̄_rhyme(s=10) ≈ 0.36
- d̄_phoneme(s=10) ≈ 0.001 (plateau before kink at s=75)
- d̄_verse-length(s=10) ≈ plateau

Q 10 is FAR from the iʿjāz peak (Q 78-114 mufaṣṣal-qiṣār), and FAR from the content-cohesion-densest zone (Q 100-114). Its empirical signature is **head-mushaf, ALR-cluster, theological-polemic, anti-iʿjāz, weak-anchor, chronology-block-boundary**.

## 6. Canonical-adjacency analysis (from `h-new-720.json`)

### Q9-Q10 = chronology-block boundary

Q 9 al-Tawba is the **last-revealed surah** (revelation-order 113). Q 10 is **revelation-order 51 (late Meccan)**. The transition Q 9 → Q 10 in the canonical mushaf is a **sharp chronological discontinuity** — moving from absolute-final Medinan revelation back to late-Meccan content.

Empirically: Q9-Q10 cost = 0.309 = 3.73% of TSP residual = **rank 4/113 most-expensive transition**. Only Q1-Q2 (al-Fātiḥa→al-Baqara, 7.5%), Q32-Q33 (4.4%), and Q33-Q34 (4.0%) cost more.

Q 9's specialist investigation found that Q9-Q10 high cost is associated with Q 9's chronology-block-singular outlier signature (per Q9 specialist's pre-reg). The Q 10 side of the boundary is the WEAK_ANCHOR side — Q 10 itself does not contribute to the cost asymmetrically; the cost is generated by Q 9's content-distinctness from the entire late-Meccan ALR-Yūnus-Hūd-Yūsuf area that follows it.

### Q10-Q11 = within-cluster transition

Q10-Q11 cost = 0.030 (~rank 80). This is among the cheaper canonical transitions, consistent with Q 10 → Q 11 being a within-ALR-cluster move.

### Asymmetry as finding

The contrast (Q9-Q10 = 0.309; Q10-Q11 = 0.030) is itself empirically remarkable: Q 10 has a **10×-asymmetric** transition profile. Coming-in is expensive; going-out is cheap. Q 10 is structurally "easier to leave than to enter" — appropriate for its role as the late-Meccan theological-polemic anchor that opens the ALR cluster.

## 7. Vocabulary distinctness check

Spot-checks of Q 10's content-distinctness via:
- mean_content_distance to corpus = 1.048 (z=+1.23, top-30%ile of distinctness)
- local_cohesion = 1.029 (z=−0.67) — Q 10's verses are tightly bound INSIDE the surah even as the surah is content-distinct from outside
- top final letter ن at 89.9% — the highest near-monorhyme rate in the head-mushaf zone

**Pattern**: Q 10 is **uniformly different**. Not heterogeneous (not anti-cohesive); but distinct as a discursive block from the corpus mean. This is the late-Meccan theological-polemic register's signature.

## 8. Cross-references to H-NEW findings touching Q 10

| Finding | What it says about Q 10 |
|:--|:--|
| [[h-new-111-fisher-rao]] | nearest 7 neighbors are theological-polemic (Q 6, 7, 27, 29, 39, 40, 45) NOT ALR siblings |
| [[h-new-590-outlier-spectrum]] | Q 10 = WEAK_ANCHOR Δ=−7.83pp |
| [[h-new-600-letter-families]] | ALR-5 NULL at 56.25%ile — Q 10 sits in this NULL cluster |
| [[h-new-97]] | ALR-PROPHET_PERSON 4/5 — Q 10 is ALR + named-after-prophet |
| [[h-new-720-canonical-adjacency-cost]] | Q9-Q10 = rank 4 (3.73% of residual); Q10-Q11 = cheap |
| [[h-new-750-per-surah-iʿjāz-signature]] | sig_A = −1.98 (rank 102/114, anti-iʿjāz) |
| [[h-new-840-unified-architectural-score]] | UAS rank 8 |
| [[h-new-660-compression-tail-gradient]] | s=10 within pre-kink plateau |
| [[cross-finding-008]] | Q 10 = ALR + *al-kitāb al-ḥakīm* — prototypical book-reference opening |

## 9. Honest limits

- **Rules-tuple sensitivity**: All metrics are computed under the default tuple (no-tashkeel, orthographic-token, QAC-stem-roots for FR, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi). Under min-tashkeel rhyme analysis, the 89.9% nūn dominance is robust; under root-level lemma counting, content-distinctness may shift.
- **The Q9-Q10 boundary cost is computed from a single 2-opt heuristic with K-restarts**: K=`h-new-720.json` n_starts. Different K could shift the absolute cost slightly, but the rank (top-5) is stable.
- **Q 10's UAS rank 8 is partly driven by the Q9-Q10 boundary** which is a NEIGHBOR's effect, not Q 10's own cohesion property. This is intrinsic to the UAS metric design.
- **The "anti-iʿjāz" classification means low fawāṣil-variety + high content-distance** — it does NOT mean Q 10 has theological deficiencies. Per the dual-iʿjāz typology (al-Khaṭṭābī vs al-Bāqillānī), Q 10 may carry HIGH theological-iʿjāz despite low structural-iʿjāz.
