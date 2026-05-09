---
surah: 68
surah_name_ar: القلم
surah_name_translit: al-Qalam
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: All H-NEW metrics integrated; Q 68 = mid-corpus position, cohesion-anchor side (-3.45 outlier-Δ), forward-cohesive to mufaṣṣal-qiṣār tail, ن-rāwī at 80.8%.
---

# Q 68 al-Qalam — Empirical Profile

## 1. Pre-computed H-NEW metrics

### UAS — Unified Architectural Score

`/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json` Q 68 entry:

| Metric | Value | Rank | Notes |
|:--|:--|:--|:--|
| **UAS** | **-1.0074** | 86 / 114 | bottom-third architectural significance |
| abs_outlier | 3.45 | rank 88/114 | cohesion-anchor side (negative Δ) |
| max_cost | 0.1328 | mid-cost adjacency | Q 68→Q 69 boundary |
| abs_ijaz | 0.4131 | rank 74/114 | moderate iʿjāz signature |

Q 68 is NOT in the structural-iʿjāz top-decile (which is Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17 — all UAS > 4). Q 68's mid-pack rank places it in the **iʿjāz-al-fawāṣil-pure / theological-iʿjāz boundary zone** of the 4-cell typology (cross-finding-026 §13.6).

### Outlier strength (H-NEW-590)

`/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json` X=68:

| Metric | Value |
|:--|:--|
| Window (7-surah) | [65, 66, 67, 68, 69, 70, 71] |
| d_W (window mean content distance) | 0.8830 |
| d_W_minus_X (window without Q 68) | 0.8899 |
| pct_W | 25.10 |
| pct_W_minus_X | 28.55 |
| **Δ_pct (Q 68's outlier strength)** | **-3.45** |
| Classification | **NULL** (neither strong outlier nor strong anchor) |

Q 68's effect on its 7-surah neighborhood window is mildly cohesion-anchoring (removing Q 68 makes the window slightly MORE diverse, but only by 3.45 percentile points). Not a STRONG_OUTLIER (≥ 5pp threshold) and not a WEAK_ANCHOR (≤ -5pp threshold). The classification is **NULL** — Q 68 is a regular member of its neighborhood, neither pulling it together nor breaking it apart.

### Iʿjāz signature (H-NEW-750)

`/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json` per_surah Q 68:

| Metric | Value | z-score |
|:--|:--|:--|
| n_verses | 52 | — |
| rhyme_entropy_nats | **0.4896** | z = -0.508 (low) |
| top_final_letter | ن | — |
| top_final_letter_frac | **0.8077 (42/52)** | — |
| mean_content_distance | 0.9139 | z = -0.094 (near mean) |
| local_cohesion | 1.2053 | z = -0.426 |
| **sig_A** | **-0.4131** | rank 74/114 |
| **sig_B** | **-0.9339** | rank 78/114 |

The **sig_A = -0.413** (negative) places Q 68 *below* corpus median on the structural-iʿjāz axis. This is consistent with Q 68's classification as a **theological-iʿjāz-leaning** rather than structural-iʿjāz surah (cross-finding-026 §13.6). The negative sig_A is paired with a high ن-rāwī fraction (80.8%), giving Q 68 a *form-strong, structure-weak* signature.

### TSP-adjacency cost (H-NEW-720)

`/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json` per_adjacency:

| Adjacency | δ_raw | Rank | Notes |
|:--|:--|:--|:--|
| Q 67 → Q 68 | 0.0962 (s=67) | low-cost | Q 67 al-Mulk → Q 68 al-Qalam is a relatively cheap transition |
| Q 68 → Q 69 | 0.1328 (s=68) | mid-cost | Q 68 al-Qalam → Q 69 al-Ḥāqqa moderate |

Neither adjacency is in the top-10-expensive (which contains Q 1-Q 2 at 0.621, Q 32-Q 33 at 0.371, Q 33-Q 34 at 0.336). The Q 67-Q 68-Q 69 transition is **not** a major TSP-residual zone.

### FR-roots nearest neighbors (H-NEW-111)

From the 114×114 FR matrix (`h-new-111.json` SHA `ea3f0ee41d41...`), Q 68's top-15 FR-nearest:

| Rank | Surah | Name | FR distance | Notes |
|:--|:--|:--|:--|:--|
| 1 | Q 100 | al-ʿĀdiyāt | 0.7156 | short Meccan terminal-tail |
| 2 | Q 52 | al-Ṭūr | 0.7175 | mid-corpus Late-Meccan |
| 3 | Q 105 | al-Fīl | 0.7257 | short Meccan terminal-tail |
| 4 | Q 93 | al-Ḍuḥā | 0.7276 | short Meccan terminal-tail |
| 5 | Q 108 | al-Kawthar | 0.7320 | shortest surah (3 verses) |
| 6 | **Q 96** | **al-ʿAlaq** | **0.7324** | **chronology-pair (revelation #1)** |
| 7 | Q 113 | al-Falaq | 0.7327 | muʿawwidhāt |
| 8 | Q 112 | al-Ikhlāṣ | 0.7381 | corpus FR-centroid |
| 9 | Q 102 | al-Takāthur | 0.7385 | short Meccan |
| 10 | Q 110 | al-Naṣr | 0.7388 | last revealed surah |
| 11 | Q 70 | al-Maʿārij | 0.7395 | mushaf-neighbor +2 |
| 12 | Q 114 | al-Nās | 0.7468 | muʿawwidhāt |
| 13 | Q 94 | al-Sharḥ | 0.7489 | iqraʾ-companion pair |
| 14 | Q 106 | Quraysh | 0.7492 | short Meccan |
| 15 | Q 1 | al-Fātiḥa | 0.7531 | umm al-Kitāb |

**Q 68's neighborhood is the mufaṣṣal-qiṣār terminal-tail cluster**. Of the top-15, 11 are short Meccan terminal-tail surahs (post-s=90), Q 96 is the chronology-pair, Q 52 is mid-corpus Late-Meccan, Q 70 is the mushaf-adjacent surah, Q 1 is the umm al-Kitāb. This is the **forward-cohesion pattern**: Q 68 (52 verses, position 68 mid-corpus) projects FR-vocabulary forward into the terminal-tail.

### FR-roots farthest neighbors (sample)

By the same matrix, Q 68's FR-farthest are dominated by long Medinan surahs (Q 2 al-Baqara, Q 4 al-Nisāʾ, Q 5 al-Māʾida, Q 9 al-Tawba) — the legal-discourse zone, where the root-distribution is heavily weighted to legal/social terms absent from Q 68's eschatological-rhetorical vocabulary.

## 2. Forward-cohesion signature (cross-Q 50 pattern)

Q 68 shares a **forward-cohesion pattern** with Q 50 Qāf (its singleton-letter cohort member). Both surahs have FR-nearest-5 dominated by post-s=75 short surahs rather than their actual mushaf-neighbors:

| Surah | Position | Mushaf-neighbors (s-1, s+1) | FR-nearest top-5 |
|:--|:--|:--|:--|
| Q 50 | 50 | Q 49 al-Ḥujurāt, Q 51 al-Dhāriyāt | Q 78, 86, 112, 79, 110 |
| Q 68 | 68 | Q 67 al-Mulk, Q 69 al-Ḥāqqa | Q 100, 52, 105, 93, 108 |

Both surahs jump *forward* in mushaf-position by 25-50 places to find their FR-nearest cluster. This pattern is **NOT** characteristic of long Medinan surahs (which cluster locally with mushaf-neighbors) but IS characteristic of mid-corpus muqaṭṭaʿāt-singleton-letter openers. Candidate cross-finding: "forward-cohesion is a singleton-letter-cohort property" — but the cohort is only N=3, so this is a flagged observation rather than a corpus-wide claim.

## 3. Rhyme structure — ن-rāwī at 80.8% (CONSPICUOUS)

`h-new-750.json` reports Q 68's final-letter distribution (from `h-new-700.json` rhyme diagnostics):

| Final letter | Count | Fraction |
|:--|:--|:--|
| ن | 42 | 80.77% |
| Others | 10 | 19.23% |

The 80.8% ن-rāwī rate is **the corpus-default rāwī density at a high quantile** (corpus mean ≈ 60-70% for ن-rāwī surahs). Q 68's rhyme entropy of 0.490 nats is consequently LOW (corpus mean ≈ 1.0-1.7 nats for typical surahs).

**Singleton-letter cohort opener-rāwī alignment** (Q050-F-05): Q 68 is the ONE cohort member where opener-letter = dominant rāwī (ن→ن). Q 50 (ق→د) and Q 38 (ص→ب) are non-matched. The 1/3 cohort match rate is consistent with corpus-frequency-baseline (ن is the corpus-default rāwī; matching it is a frequency-baseline artifact rather than a meaningful opener-rāwī alignment, per Q050-F-05 interpretation).

## 4. Compression-tail laws — Q 68's predicted vs observed d̄

From the 4 architectural laws (Wave 2026-04-28):

| Law | s=68 prediction | Q 68 observed | Residual |
|:--|:--|:--|:--|
| d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50) | 0.96 − 0.012·18 = **0.744** | **0.9139** (window-d̄) | +0.170 (above predicted; weak compression-tail effect at s=68) |
| d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50) | 0.36 + 0.0041·18 = 0.4338 | rhyme entropy 0.490 nats | within prediction range |

The +0.170 residual on the content law indicates Q 68's content-distance is HIGHER than the compression-tail prediction at s=68 — i.e., Q 68 is LESS compressed than its mushaf position predicts. Combined with the forward-cohesion signature (FR-nearest are terminal-tail surahs), this is consistent with Q 68 being a **misplaced-compression** surah: its content-vocabulary is terminal-tail-like, but its mushaf position is mid-corpus.

## 5. Letter counts and tashkeel sensitivity (Q068-F-02)

`csv/Q068-F-02.json`:

- Total Arabic letters (no-tashkeel) in Q 68 body: 1,289
- ن letters in Q 68 body: 131
- Q 68 ن-rate: **0.1016 (10.16%)**
- Corpus-rest ن-rate: 0.0824 (8.24%)
- **Rate ratio**: 1.234 (Q 68 has 23% more ن than the rest of the corpus)
- Permutation null p (one-sided): 0.069 (DIRECTIONAL)
- Binomial null p (one-sided): 0.008 (SIGNIFICANT under binomial baseline)

The DIRECTIONAL verdict reflects the difference between permutation-null (which preserves Q 68's local-corpus structure) and binomial-null (which assumes letter-level independence). The honest report: Q 68 has elevated ن at the **letter-density level**, consistent with the muqaṭṭaʿ-ن self-reference hypothesis, but the elevation does not reach the strict 5% Bonferroni-permutation threshold.

## 6. Cohort positioning — singleton-letter muqaṭṭaʿāt

| Surah | Opener | Verses | Rev. order | Noldeke | Rāwī | UAS | sig_A | Outlier Δ |
|:-:|:-:|:-:|:-:|:--|:-:|:-:|:--|:-:|
| Q 38 | ص | 88 | 38 | Middle Meccan | ب (40%) | rank 59/114 | +1.286 | +2.70 |
| Q 50 | ق | 45 | 34 | Middle Meccan | د (60%) | rank 40/114 | +0.891 | +5.42 |
| **Q 68** | **ن** | **52** | **2** | **Early Meccan** | **ن (81%)** | **rank 86/114** | **-0.413** | **-3.45** |

Q 68 is the **outlier** of the cohort: smallest UAS, lowest sig_A, only cohesion-anchor-side outlier-Δ. Q 38 and Q 50 are Middle Meccan; Q 68 is Early Meccan (revelation #2). This chronological positioning explains Q 68's structural difference from Q 38/Q 50: Q 68 belongs to the *iqraʾ-qalam* Early Meccan thematic phase, not to the Middle Meccan cosmic-resurrection phase of Q 38/Q 50.

## 7. Cross-finding integrations

- **[[h-new-660-compression-tail-gradient]]**: Q 68's content-d̄ residual = +0.170 above s=68 prediction (anti-compression).
- **[[h-new-700-phonological-compression-tail]]**: Q 68's rhyme entropy 0.490 nats is LOW (high ن-rāwī concentration).
- **[[h-new-111-fisher-rao-mushaf]]**: Q 68 sits in the mid-corpus FR-roots position with forward-cohesion to terminal-tail.
- **[[h-new-590-outlier-strength]]**: Q 68 = NULL classification (Δ=-3.45, neither STRONG_OUTLIER nor WEAK_ANCHOR).
- **[[h-new-750-per-surah-ijaz-signature]]**: sig_A = -0.413, sig_B = -0.934 (both negative; below corpus median).
- **[[h-new-840-unified-architectural-score]]**: UAS rank 86/114; bottom-third.
- **[[cross-finding-008]]**: Q 68 is a muqaṭṭaʿāt-opener; the 23/29 *muqaṭṭaʿ + book-reference* pattern does NOT apply (Q 68 follows the 3/29 *muqaṭṭaʿ + oath-wāw + al-* pattern with Q 38 and Q 50; cross-finding-008 complementary minor pattern).
- **[[cross-finding-014]]**: candidate addition — Q 68 ↔ Q 96 directionally-asymmetric FR-pair (chronology-pair, qlm-paired, rank 6 from Q 68's side, rank 46 from Q 96's side).
- **[[cross-finding-026-ijaz-architecture]]**: Q 68 = theological-iʿjāz-leaning cell (low UAS, low sig_A, high rāwī concentration). Singleton-letter cohort double-replication NULL on FR-cohesion confirms §1 letter-axis ⊥ content-axis at the cohort scale.
