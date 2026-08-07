---
surah: 30
surah_name_translit: al-Rūm
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: "Q 30 architectural-signature: moderate UAS (-0.244, rank ~74); WEAK_OUTLIER (Δ%ile +3.64); rhyme-consolidated nūn (90%); content-dispersed (sig_A rank 97); content-distance d̄=1.023 above corpus mean. Compression-tail-consistent at s=30."
---

# Q 30 al-Rūm — Empirical Profile


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

This file integrates ALL pre-computed empirical metrics on Q 30 from project artifacts. Every value is cited to its source-file. No values are stated from memory.

## Source files

- H-NEW-111 (FR distance matrix): `findings/phase-b-hypotheses/csv/h-new-111.json`
- H-NEW-590 (outlier-strength): `findings/phase-b-hypotheses/csv/h-new-590.json` (`all_surahs_results` X=30)
- H-NEW-700 (rhyme + phoneme + window-d̄): `findings/phase-b-hypotheses/csv/h-new-700.json`
- H-NEW-720 (TSP-cost adjacency): `findings/phase-b-hypotheses/csv/h-new-720.json` (per_adjacency pair=[29,30] and [30,31])
- H-NEW-750 (iʿjāz signature): `findings/phase-b-hypotheses/csv/h-new-750.json` (per_surah[30])
- H-NEW-840 (UAS): `findings/phase-b-hypotheses/csv/h-new-840.json` (`all_uas` surah=30)

## 1. Unified Architectural Significance (UAS) — H-NEW-840

| Component | Q 30 value | Source path |
|:--|:-:|:--|
| UAS (composite) | **−0.244** | h-new-840 `all_uas` |
| abs_outlier | 3.64 | h-new-840 |
| max_neighbor_TSP_cost | 0.0376 | h-new-840 |
| abs_iʿjāz signature | 1.671 | h-new-840 |

**UAS rank**: ~74 / 114 (NOT in top-15, NOT in bottom-10). Q 30 is an architectural-mediocre surah at the composite-UAS axis: it neither commands an outsize structural identity (like Q 33, 1, 2, 9) nor sits at the corpus FR-centroid (like Q 112). Its iʿjāz-signature magnitude (1.67) is moderately strong, however, contributing structural-iʿjāz weight to the composite.

## 2. Outlier strength — H-NEW-590

```json
{"X": 30, "window": [27, 28, 29, 30, 31, 32, 33],
 "window_minus_X": [27, 28, 29, 31, 32, 33],
 "d_W": 0.9594, "d_W_minus_X": 0.9571,
 "pct_W": 63.34, "pct_W_minus_X": 59.7,
 "delta_pct": +3.64, "p_greater_W": 0.367,
 "classification": "WEAK_OUTLIER"}
```

Removing Q 30 from the 7-window centered at s=30 modestly INCREASES the window's mean content-distance percentile (+3.64pp). This means Q 30 is *very slightly* more cohesive-than-its-neighbors; its presence pulls the window's d̄ DOWN (more cohesive). But the effect is weak (`p_greater_W` = 0.367, NOT significant). Compare to Q 1 (Δ%ile = +27pp, STRONG_OUTLIER) and Q 9 (Δ%ile = +21pp).

## 3. iʿjāz signature — H-NEW-750

```json
{"surah": 30, "n_verses": 60,
 "rhyme_entropy_nats": 0.3887, "top_final_letter": "ن",
 "top_final_letter_frac": 0.900,
 "mean_content_distance": 1.0229, "local_cohesion": 1.0746,
 "z_rhyme_entropy": -0.690, "z_mean_content_distance": +0.981,
 "z_local_cohesion": -0.604,
 "sig_A": -1.671, "sig_B": -1.294,
 "rank_A": 97, "rank_B": 93}
```

**Interpretation**:
- Q 30 has **LOW rhyme entropy** (0.389 nats vs corpus mean ≈ 0.59) — rhyme is highly consolidated.
- Q 30 has **HIGH content distance** (d̄=1.023 vs corpus mean ≈ 0.96) — content vocabulary is broad/dispersed across many roots.
- The combined signature `sig_A = -1.671` (rank 97/114) is a **classical iʿjāz al-fawāṣil profile**: tight rhyme-binding, dispersed content. This matches al-Bāqillānī's "cohesion at the rhyme-word axis" doctrine.
- 90% of Q 30's 60 verses end in nūn — the *al-fāṣila al-nūniyya* uniformity. The non-nūn verses include the 6 in mid-surah that break to a different rāwī (catalogued in `02-content-analysis.md`).

## 4. Compression-tail prediction (H-NEW-660 architectural law)

The compression-tail law: `d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50)`. For s=30 (BEFORE the s=50 kink), the predicted d̄ is **0.96**. Q 30's observed d̄ = 1.023.

**Residual**: +0.063 above the law's prediction. Q 30 is moderately *above* the head-pole baseline — slight content-dispersion relative to law-fit. (For comparison, the 4-region architecture cross-finding-010 places s=30 still in the "head" region of the mushaf.)

## 5. Canonical adjacency — H-NEW-720 TSP-residual

| Pair | L_constrained | δ_raw | fraction_residual |
|:--|:-:|:-:|:-:|
| Q 28 → Q 29 | 77.541 | 0.0746 | 0.0090 |
| Q 29 → Q 30 | 77.496 | 0.0293 | 0.0035 |
| Q 30 → Q 31 | 77.505 | 0.0376 | 0.0045 |

The Q 29 → Q 30 adjacency is **cheap** (rank ~bottom-30 of 113 in TSP-cost) — i.e., the canonical mushaf placement of Q 30 immediately after Q 29 is close to optimal. The Q 30 → Q 31 adjacency is also low-cost. Q 30's local 3-pair neighborhood is a TSP-cheap cluster, consistent with the al-Biqāʿī claim of munāsabah (thematic-flow adjacency).

## 6. Fisher-Rao distance neighbors — H-NEW-111

Pairwise FR distance to ALM-cluster neighbors:

| Pair | FR distance |
|:--|:-:|
| Q 29 ↔ Q 30 | **0.9153** |
| Q 30 ↔ Q 31 | 0.9089 |
| Q 30 ↔ Q 32 | 0.9272 |
| Q 30 ↔ Q 2 | 0.9732 |
| Q 30 ↔ Q 3 | 0.9841 |

Q 30's closest ALM-neighbor in FR-roots space is **Q 31 Luqmān** (0.909), not Q 29 (0.915) — a counter-intuitive observation given the cross-finding-008 narrative that Q 29 + Q 30 share exception-status. Q 30's FR-twin is Q 31 (a non-exception ALM surah). See `Q030-F-04` for full ALM-rank analysis.

Corpus-wide context: Q 30's mean FR-distance to all other 113 surahs is ≈ 0.985 (compared to corpus median 0.957). Q 30 is slightly above-median content-distinctive.

## 7. Phoneme + verse-length compression-tail (H-NEW-700, H-NEW-770)

For s=30 (before s=75 phoneme-kink), the phoneme-tail law predicts baseline d̄_phoneme ≈ 0.001. Surah-internal phoneme spread is consistent with this baseline (Q 30 is not a phoneme-outlier in either direction).

The verse-length compression-tail: Q 30 has 60 verses; mean words/verse ≈ 14.5 (818 words / 60 verses). This is *medium-Meccan* length-class.

## 8. Architectural type classification

Per the dual-iʿjāz typology (cross-finding-026):
- Q 30 sits in the **structural-iʿjāz quadrant** (high |sig_A|, high rhyme-consolidation, dispersed content). It is NOT a theological-iʿjāz anchor like Q 112.
- Q 30 is NOT in the UAS top-10. It is moderate-UAS structural-iʿjāz.

## 9. Cross-references to H-NEW findings touching Q 30

- [[h-new-53-muqattaat-book-reference|H-NEW-53]]: Q 30 is one of the 2/29 muqaṭṭaʿāt-opened surahs lacking book-reference in v 1-3.
- [[h-new-93-q29-q30-subpattern|H-NEW-93]]: parent NULL — Q 30's historical-prophecy density is HIGH (56.8‰ vs Meccan 29.3‰) but doesn't meet Bonferroni-4 alone.
- [[cross-finding-008-muqattaat-book-introduction-marker-synthesis|Cross-finding-008]]: Q 30 = "exception" surah in the muqaṭṭaʿāt + book-reference pattern.
- H-NEW-660 compression-tail: Q 30 d̄=1.023 ≈ law-prediction (residual +0.06).
- H-NEW-770 verse-length kink-50: Q 30 (s=30) sits in head-pole.

## Honest limits

- The "WEAK_OUTLIER" classification is just-above-random; under permutation null p=0.367, this is statistically indistinguishable from null. The interpretation must be modest.
- The `sig_A`-rank 97/114 is real but driven significantly by the high uniformity of nūn-rhyme (which is itself a function of the surah's late-Meccan rhetorical register, not unique to Q 30). Multiple late-Meccan surahs share this feature.
- Q 30's content-distance is moderately above corpus-mean — but only slightly above the compression-tail law's prediction. The interpretation must NOT exaggerate.
