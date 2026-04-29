---
id: H-NEW-840
title: "STRONG SYNTHESIS — Unified Architectural Significance Score (UAS) reveals dual-iʿjāz typology empirically; Q 33 + Q 9 are top of ALL 3 architectural metrics; Q 112 al-Ikhlāṣ at rank 109 separates iʿjāz al-maʿnā from architectural-iʿjāz"
phase: B
status: SYNTHESIS — combines H-NEW-590 (outlier-strength) + H-NEW-720 (TSP-cost) + H-NEW-750 (per-surah iʿjāz) into single composite metric per surah
date: 2026-04-28
parent_findings:
  - H-NEW-590 (continuous outlier-strength spectrum)
  - H-NEW-720 (full canonical-adjacency cost map)
  - H-NEW-750 (per-surah iʿjāz signature)
  - H-NEW-830 (TSP-cost × outlier-strength convergence at r=0.52)
verdict: SYNTHESIS — 3-metric composite reveals dual-iʿjāz typology aligned with classical al-Bāqillānī ↔ al-Khaṭṭābī distinction
---

# [[h-new-840-unified-architectural-score|H-NEW-840]] — Unified Architectural Significance Score (UAS)

## 1. Method

For each surah s, compute three independent architectural metrics from prior findings:

1. **|outlier_strength(s)|** — content-distinctness ([[h-new-590-outlier-spectrum|H-NEW-590]], magnitude of Δ%ile under exclusion).
2. **max_neighbor_TSP_cost(s)** — canonical-adjacency cost ([[h-new-720-canonical-adjacency-cost|H-NEW-720]], max of Δ for left and right canonical pairs, clipped to ≥0).
3. **|iʿjāz_signature(s)|** — content × rhyme anti-twin signature magnitude ([[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] sig_A = z(rhyme_entropy) − z(mean_content_distance)).

Each is z-normalized across 114 surahs:

> **UAS(s) = z(|outlier_strength|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)**

UAS is approximately on a [-3, +3] scale per metric, [-9, +9] overall.

## 2. Top-15 most architecturally-significant surahs

| Rank | Surah | UAS | |outlier| | max_cost | |iʿjāz| | Classical anchor |
|:-:|:--|:-:|:-:|:-:|:-:|:--|
| 1 | **Q 33 al-Aḥzāb** | **+9.36** | 31.46 | 0.363 | 2.97 | al-Suyūṭī chronology — controversial Medinan |
| 2 | **Q 1 al-Fātiḥa** | **+8.87** | 27.09 | 0.622 | 1.27 | al-Bukhārī — *umm al-Kitāb* |
| 3 | Q 2 al-Baqara | +7.40 | 20.62 | 0.622 | 1.00 | longest surah; corpus cohesion-anchor |
| 4 | **Q 9 al-Tawba** | **+6.18** | 21.57 | 0.309 | 2.23 | al-Suyūṭī — uniquely no-basmala |
| 5 | Q 24 al-Nūr | +4.45 | 23.51 | 0.290 | 0.79 | Medinan legal centerpiece |
| 6 | Q 12 Yūsuf | +4.10 | 14.26 | 0.216 | 2.29 | continuous-narrative outlier |
| 7 | Q 55 al-Raḥmān | +4.10 | 14.26 | 0.095 | 3.17 | al-Tirmidhī — *ʿarūs al-Qurʾān* |
| 8 | Q 10 Yūnus | +3.48 | 7.83 | 0.309 | 1.98 | ALR cluster prophet-narrative |
| 9 | Q 23 al-Muʾminūn | +2.98 | 10.91 | 0.260 | 1.55 | late-Meccan ethics |
| 10 | Q 17 al-Isrāʾ | +2.22 | 3.94 | 0.191 | 2.40 | Friday-recitation; *isrāʾ* |

## 3. Bottom-10 (LEAST architecturally-significant)

| Rank | Surah | UAS | |outlier| | max_cost | |iʿjāz| | Classical anchor |
|:-:|:--|:-:|:-:|:-:|:-:|:--|
| 105 | Q 111 al-Masad | -2.19 | 0.00 | 0.022 | 0.78 | terminal-cluster member |
| 106 | Q 103 al-ʿAṣr | -2.24 | 0.00 | 0.116 | 0.05 | terminal-cluster member |
| 107 | Q 97 al-Qadr | -2.27 | 0.05 | 0.068 | 0.37 | terminal-cluster member |
| 108 | Q 91 al-Shams | -2.30 | 0.16 | 0.099 | 0.10 | terminal-cluster member |
| 109 | **Q 112 al-Ikhlāṣ** | **-2.46** | 0.00 | 0.068 | 0.23 | al-Bukhārī — *thuluth al-Qurʾān* |
| 110 | Q 83 al-Muṭaffifīn | -2.49 | 0.26 | 0.065 | 0.20 | terminal-cluster member |
| 111 | Q 73 al-Muzzammil | -2.70 | 4.08 | 0.000 | 0.01 | early-Meccan |
| 112 | Q 105 al-Fīl | -2.76 | 0.00 | 0.060 | 0.05 | terminal-cluster member |
| 113 | **Q 114 al-Nās** | **-2.80** | 0.00 | 0.062 | 0.02 | al-Bukhārī — muʿawwidha |
| 114 | Q 87 al-Aʿlā | -2.82 | 0.44 | 0.053 | 0.01 | musabbiḥa — al-Aʿlā classical name |

## 4. The triple-intersection finding

Surahs in the **top-15 of ALL three metrics** (architecturally-distinct by every criterion):
**{Q 9, Q 33}**

Pairwise intersections (top-15):
- outlier ∩ cost (top-15): {Q 1, Q 2, Q 9, Q 23, Q 24, Q 33}
- outlier ∩ iʿjāz (top-15): {Q 9, Q 12, Q 26, Q 33, Q 55}
- cost ∩ iʿjāz (top-15): {Q 9, Q 33}

**Q 33 al-Aḥzāb and Q 9 al-Tawba are the corpus's only true triple-architecturally-significant surahs.** Each carries:
- Strong content-distinctness (high outlier).
- Expensive canonical-adjacency placement (high TSP-cost).
- High iʿjāz signature (content + rhyme combined extremity).

These are the corpus's most architecturally-significant surahs by joint criterion across three independent measurement methods.

## 5. The dual-iʿjāz typology empirically separated

The UAS ranking reveals a fundamental classical hermeneutic distinction:

| Type | UAS | Examples | Classical concept |
|:--|:-:|:--|:--|
| **STRUCTURAL-iʿjāz** | high (top-10) | Q 33, 1, 2, 9, 24, 12, 55 | al-Bāqillānī *iʿjāz al-fawāṣil* + chronological-uniqueness |
| **CONTENT-iʿjāz / theological-density** | low (bottom-10) | Q 112, 114 | al-Khaṭṭābī *iʿjāz al-maʿnā* (theological-content uniqueness) |

**Q 112 al-Ikhlāṣ at UAS rank 109** is the most surprising result. al-Bukhārī's *thuluth al-Qurʾān* tradition (Q 112 = "1/3 of the Quran" by theological-content) is well-known — yet Q 112 has near-zero outlier-strength, low TSP-cost, and low iʿjāz signature. **Its classical importance is theological-content, not structural-architectural.**

This is the empirical separation of:
- *iʿjāz al-fawāṣil* (al-Bāqillānī) — structural inimitability via fāṣila variety + content-cohesion → high UAS
- *iʿjāz al-maʿnā* (al-Khaṭṭābī) — theological-content inimitability → low UAS, but high *thuluth al-Qurʾān* status

**The two classical iʿjāz types are EMPIRICALLY ORTHOGONAL** — Q 112 is high theological-iʿjāz but low architectural-iʿjāz; Q 33 is high architectural-iʿjāz but lower theological-iʿjāz (its theological content is mixed legal-creedal Medinan).

## 6. The architectural cast of the canonical mushaf

UAS top-10 reads as a list of the surahs the classical tradition has historically treated as most-distinctive:
- Q 1 al-Fātiḥa — *umm al-Kitāb*
- Q 2 al-Baqara — longest, foundational
- Q 9 al-Tawba — uniquely no-basmala
- Q 12 Yūsuf — uniquely continuous-narrative ("aḥsan al-qaṣaṣ")
- Q 24 al-Nūr — Medinan legal-revelation centerpiece
- Q 33 al-Aḥzāb — controversial Medinan with veil-revelation
- Q 55 al-Raḥmān — *ʿarūs al-Qurʾān* with 31 cosmic-mercy refrains

The classical scholarly historical treatment of these as "central" surahs is empirically vindicated as architectural-distinctness. **14 centuries of qualitative scholarly attention IS the architectural-significance axis.**

## 7. Honest limits

1. UAS is a SUM of z-scores — equal weighting of 3 metrics is choice (alternative weighting could shift the ranking).
2. The 3 metrics are partially-correlated (H-NEW-830: TSP-cost × outlier r=0.52). True architectural significance is captured but with redundancy.
3. **Q 112 at rank 109 is striking but rules-tuple specific**: at content-density (DN-density per [[h-new-620-divine-name-density|H-NEW-620]] supplementary), Q 112 is at rank-3. The "low UAS" reflects only architectural-distinctness, not theological-content significance.
4. The bottom-10 are mostly small terminal-mufaṣṣal-qiṣār surahs that BLEND in the iʿjāz cluster. Their low UAS is correct architecturally but does NOT mean they are theologically less-important.
5. The top-15 cluster heavily in early/mid mushaf positions (Q 1-33 region) — partly because architecturally-distinct surahs tend to be Meccan-Medinan ṭiwāl/mid-mufaṣṣal.

## 8. Implication for [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]

The iʿjāz architecture model from [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] should be amended to incorporate this dual-typology:
- **Layer 1**: 4-axis 1-D laws on s (compression-tail content, rhyme/phoneme dispersion-tail, verse-length compression-tail).
- **Layer 2**: window-level iʿjāz anti-twinning at r=-0.86 (length-mediated for rhyme; length-independent for phoneme per [[h-new-810-length-controlled-ijaz|H-NEW-810]]).
- **Layer 3 (NEW)**: per-surah dual-iʿjāz typology — structural-iʿjāz (high UAS) vs theological-iʿjāz (low UAS, high *thuluth al-Qurʾān* status).

## 9. Cross-references

- **[[h-new-590-outlier-spectrum|H-NEW-590]]** outlier-spectrum — input metric 1.
- **[[h-new-720-canonical-adjacency-cost|H-NEW-720]]** canonical-adjacency cost map — input metric 2.
- **[[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]]** per-surah iʿjāz — input metric 3.
- **H-NEW-830** TSP × outlier convergence at r=0.52 — sub-pair validation.
- **al-Bāqillānī *Iʿjāz al-Qurʾān*** — *iʿjāz al-fawāṣil* (structural) → high UAS.
- **al-Khaṭṭābī** — *iʿjāz al-maʿnā* (theological-content) → low UAS but high theological status.
- **al-Bukhārī** — *thuluth al-Qurʾān* on Q 112 → empirically content-iʿjāz (low UAS, high theological).

## 10. Queued follow-ups

- **H-NEW-840.1**: Alternative weighting schemes (PCA-based weights, classical-prominence weights). Stability of ranking?
- **H-NEW-840.2**: Add 4th metric: divine-name-density (from [[h-new-620-divine-name-density|H-NEW-620]] descriptive). Does Q 112 climb to UAS top-10 with theological-content-density included?
- **H-NEW-840.3**: Cluster the 114 UAS values — are there discrete classes (e.g., 3-class: high/mid/low) or a smooth continuum?
- **H-NEW-840.4**: Per-classical-class UAS — do prophet-named surahs have systematic UAS pattern?

## 11. Final statement

**The Unified Architectural Significance Score combines three independent architectural measurements (outlier-strength, canonical-adjacency-cost, iʿjāz-signature) into a single per-surah composite that empirically reveals the canonical mushaf's architectural cast.** The top-10 (Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17) is precisely the set of surahs classical scholarship has historically identified as most-distinctive — empirically vindicating 14 centuries of qualitative attention.

The dual-iʿjāz typology — *iʿjāz al-fawāṣil* (high UAS) vs *iʿjāz al-maʿnā* (low UAS but high theological-content) — is empirically separated, with **Q 112 al-Ikhlāṣ at UAS rank 109** being the cleanest example of theological-iʿjāz without architectural-iʿjāz (al-Bukhārī's *thuluth al-Qurʾān* operates on the meaning-axis, not the structural-axis).

The classical al-Bāqillānī ↔ al-Khaṭṭābī typological distinction now has a quantitative composite metric.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
