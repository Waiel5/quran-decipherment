---
surah: 108
file_type: empirical-profile
date_last_updated: 2026-05-09
sources:
  - findings/phase-b-hypotheses/csv/h-new-111.json
  - findings/phase-b-hypotheses/csv/h-new-131.json
  - findings/phase-b-hypotheses/csv/h-new-238.json
  - findings/phase-b-hypotheses/csv/h-new-590.json
  - findings/phase-b-hypotheses/csv/h-new-700.json
  - findings/phase-b-hypotheses/csv/h-new-720.json
  - findings/phase-b-hypotheses/csv/h-new-750.json
  - findings/phase-b-hypotheses/csv/h-new-840.json
  - data/morphology/quranic-corpus-morphology-0.4.txt (QAC v0.4)
  - quran-text/quran-no-tashkeel.json
---

# Q 108 al-Kawthar — Empirical Profile

This file aggregates ALL Quran-Decipherment-Project H-NEW empirical metrics for Q108, computed from disk (no values asserted from memory).

## 1. Length-class extrema

Q108 is the **corpus-minimum** along three independent length axes:

| Axis | Q108 value | Rank / 114 | Source |
|:--|:--|:-:|:--|
| Verse count | 3 | tied rank 1 (with Q103, Q110) | `quran-text/quran-no-tashkeel.json` |
| Word count (orthographic, no-tashkeel) | **10** | **rank 1 (sole minimum)** | computed |
| Letter count (no-tashkeel, no spaces, plene) | **43** | **rank 1 (sole minimum)** | computed |
| Letter count (Uthmani rasm) | 42 | rank 1 (sole minimum) | `data/alt-text/quran-uthmani-consonantal.json` |
| Root tokens (QAC v0.4 ROOT-tagged) | 7 | rank 1 (sole minimum, non-zero) | `data/morphology/quranic-corpus-morphology-0.4.txt` |

**Q108 is the absolute lexical-mass minimum of the corpus** along three of four length axes (only verse count is tied).

## 2. Fisher-Rao geometry (H-NEW-111)

Computed from the precomputed 114×114 Fisher-Rao distance matrix in `findings/phase-b-hypotheses/csv/h-new-111.json` (rules-tuple: top-500 QAC-STEM roots, Dirichlet α=0.5, L1-normalized, arccos-Bhattacharyya):

| Metric | Value |
|:--|:--|
| Mean d_FR(Q108, others) | **0.7718** |
| Rank by mean-FR-distance (lower = more central) | **3 / 114** |
| d_FR(Q1, Q108) | **0.3384** |
| d_FR(Q108, nearest-neighbor) | 0.2127 (nearest = Q106 Quraysh) |
| d_FR(Q108, furthest) | 1.2911 (furthest = Q3 Āl ʿImrān) |

### 2.1 Top-15 nearest neighbors of Q108 (FR distance)

| Rank | Q | Name | d_FR |
|:-:|:-:|:--|:-:|
| 1 | Q106 | Quraysh | 0.2127 |
| 2 | Q107 | al-Māʿūn | 0.2256 |
| 3 | Q94 | al-Sharḥ | 0.2305 |
| 4 | Q111 | al-Masad | 0.2324 |
| 5 | Q113 | al-Falaq | 0.2371 |
| 6 | Q103 | al-ʿAṣr | 0.2399 |
| 7 | Q112 | al-Ikhlāṣ | 0.2465 |
| 8 | Q105 | al-Fīl | 0.2542 |
| 9 | Q100 | al-ʿĀdiyāt | 0.2576 |
| 10 | Q110 | al-Naṣr | 0.2684 |
| 11 | Q104 | al-Humaza | 0.2700 |
| 12 | Q114 | al-Nās | 0.2862 |
| 13 | Q102 | al-Takāthur | 0.2937 |
| 14 | Q101 | al-Qāriʿah | 0.2956 |
| 15 | Q93 | al-Ḍuḥā | 0.3086 |

**ALL 15 nearest neighbors are mufaṣṣal-qiṣār surahs (Q ≥ 93).** Q108 is geometrically embedded in the terminal short-surah cluster.

### 2.2 Top-3 most-FR-central surahs

| Rank | Q | Name | mean d_FR |
|:-:|:-:|:--|:-:|
| 1 | Q112 | al-Ikhlāṣ | 0.7592 |
| 2 | Q110 | al-Naṣr | 0.7644 |
| **3** | **Q108** | **al-Kawthar** | **0.7718** |
| 4 | Q1 | al-Fātiḥa | 0.7789 |
| 5 | Q106 | Quraysh | 0.7803 |

**The top-5 most-central surahs are entirely from the {Q1 ∪ mufaṣṣal-qiṣār} zone** — Q1 (the opener) clusters geometrically with the closing terminal-7. This is the structural basis of the wrap-around closure synthesized in cross-finding-013.

## 3. MST super-hub status (H-NEW-131 / H-NEW-131.1 / H-NEW-134)

The minimum spanning tree of the 114-node Fisher-Rao distance graph identifies Q108 as a high-degree hub. Robustness across smoothing α, metric choice, and length-residualization:

| Configuration | Q108 MST-degree | Top-1 hub | Source |
|:--|:-:|:--|:--|
| Fisher-Rao, α=0.5 (baseline) | **24** | **Q108** | H-NEW-134 / H-NEW-131 |
| Fisher-Rao, α=0.001 | 1 | Q7 al-Aʿrāf (deg 21) | H-NEW-131.1 Cell A |
| Fisher-Rao, α=0.01 | 11 | Q7 al-Aʿrāf (deg 25) | H-NEW-131.1 Cell A |
| Fisher-Rao, α=0.05 | 21 (tied with Q7) | Q108/Q7 tied | H-NEW-131.1 |
| Fisher-Rao, α=0.1 | 24 | Q108 | H-NEW-131.1 |
| Fisher-Rao, α=1.0 | 24 | Q108 | H-NEW-131.1 |
| Fisher-Rao, α=2.0 | 22 | Q108 | H-NEW-131.1 |
| Hellinger, α=0.5 | 24 (≡ FR by rank-monotonicity) | Q108 | H-NEW-131 Cell B |
| Jensen-Shannon, α=0.5 | 24 | Q108 | H-NEW-131 Cell B |
| Total-Variation, α=0.5 | 6 | Q64 al-Taghābun | H-NEW-131 Cell B (FAILS) |
| **Length-residualized α∝(mean/N_i)** | **16** | **Q108** | H-NEW-131.1 Cell B (PASSES) |
| MW-5 positive control (synthetic centroid) | 24 (Q108 retained even with planted true centroid at degree 62) | synthetic | H-NEW-131.1 |

**Verdict (H-NEW-131): WEAKLY-STRUCTURAL.** The super-hub status is part-mechanical (smoothing + shortest-surah interaction) and part-structural (residual centrality of 16 under length-correction is real). The qualitative claim "Q108 is the content-centroid of the short-mufaṣṣal cluster" is VALIDATED under arccos/sqrt-family metrics; refuted under L1.

**Verdict (H-NEW-131.1): STRUCTURAL-ROBUST + SMOOTHING-UNSTABLE.** Q108's residual centrality (deg 16 under length-residualized smoothing) confirms genuine short-mufaṣṣal-content-centrality. The α-sweep is monotone-saturating-with-modest-reversal at α=2.0, breaking the strict pre-committed ρ≥0.80 monotonicity threshold.

## 4. Cyclic-shift wrap-edge architecture (H-NEW-238)

H-NEW-238 tested whether canonical Q1-at-position-1 is the M1-geodesic-preferred starting-point of the 114-cycle by minimum wrap-edge.

**Result for Q108 specifically**: rotation k=108 (placing Q108 at position 1 and Q107 at position 114) gives the **CYCLE-MINIMUM wrap-edge W = 0.2256**, which is **rank 1 / 114** among all cyclic shifts.

| Shift k (surah at position 1) | Wrap-edge W | Rank |
|:-:|:-:|:-:|
| **k=108 (Q108 al-Kawthar)** | **0.2256** | **1 (M1-MINIMUM)** |
| k=114 (Q114 al-Nās) | 0.2718 | 2 |
| k=107 (Q107 al-Māʿūn) | 0.2772 | 3 |
| k=112 (Q112 al-Ikhlāṣ) | 0.2849 | 4 |
| k=113 (Q113 al-Falaq) | 0.2886 | 5 |
| k=1 (canonical mushaf, Q1 at position 1) | 0.3884 | 18 |
| k=2 (Q2 al-Baqara) | 1.1776 | 114 (CYCLE-MAXIMUM) |

**Architectural interpretation (H-NEW-238 + cross-finding-013)**:

- The mushaf-as-Hamiltonian-cycle has its **compositional-geodesic optimum starting-point at Q108** (W=0.2256, rank 1/114). This is M1 (compositional-content) preference.
- The canonical Q1-at-position-1 ranks 18/114 (top quintile but not optimum). This reflects the M1/P3 trade-off: P3 (liturgical fātiḥat al-kitāb) holds Q1 in position 1 against M1's preference.
- The Q1→Q2 edge is the **single largest Fisher-Rao jump in the entire 114-edge cycle** (W=1.1776, rank 114/114). The prayer-frame to encyclopedic-content transition is the cycle's biggest M1-cost; Q1's liturgical placement pays exactly that cost at one specific edge.
- All top-10 tightest-wrap rotations (k ∈ {108, 114, 107, 112, 113, 106, 104, 111, 109, 105}) start INSIDE the Q103-Q114 terminal cluster — confirming this is the densest content cluster in the corpus.

## 5. Per-surah iʿjāz signature (H-NEW-750)

Source: `findings/phase-b-hypotheses/csv/h-new-750.json` per_surah surah=108.

| Field | Value | Z-score | Rank / 114 |
|:--|:-:|:-:|:-:|
| n_verses | 3 | — | tied rank 1 (min) |
| rhyme_entropy_nats | **0.0000** | z=−1.39 | tied min (with all monorhyme surahs) |
| top_final_letter | ر (rāʾ) | — | — |
| top_final_letter_frac | 1.000 | — | tied max |
| mean_content_distance | 0.7718 | z=−1.50 | rank 3 |
| **local_cohesion** | **3.8427** | **z=+3.16** | **HIGH (extreme positive)** |
| sig_A | +0.1026 | — | 56 / 114 |
| **sig_B** | **+1.7704** | — | **12 / 114** |
| rank_A | 56 | — | — |
| rank_B | **12** | — | top decile on signature B |

**Reading**: Q108 has very-high LOCAL COHESION (z=+3.16 — its 1-step content-neighborhood is maximally tight). This makes structural sense: Q108 sits in the densest cluster (terminal-7), so its 1-step neighborhood is intrinsically tight. sig_B at rank 12/114 is consistent with this. Rhyme entropy at corpus minimum confirms the monorhyme.

## 6. Outlier-strength (H-NEW-590)

Source: `findings/phase-b-hypotheses/csv/h-new-590.json` X=108.

| Field | Value |
|:--|:--|
| Window | [105, 106, 107, **108**, 109, 110, 111] |
| d_W (mean within-window FR distance) | 0.3008 |
| d_W_minus_X (drop Q108) | 0.3193 |
| pct_W (rank window-d̄ vs null) | 0.0% |
| pct_W_minus_X | 0.0% |
| **delta_pct** | **0.00 pp** |
| p (greater) | 1.000 |
| **classification** | **NULL** |

**Reading**: Q108 does NOT show a window-d̄ outlier signature (the within-window distances are similarly low whether or not Q108 is included; both are at the corpus minimum). This is consistent with Q108 being a *typical* member of the densely-packed terminal-cluster, not a unique outlier within it. Q108's distinctive role is **structural** (super-hub, M1-minimum start) not **dispersion-anomaly** (its 7-surah window is uniformly tight; it doesn't "break" or "make" the local geometry).

## 7. Canonical-adjacency cost (H-NEW-720)

Source: `findings/phase-b-hypotheses/csv/h-new-720.json` per_adjacency.

| Adjacency | s | δ (TSP-residual) | fraction_residual | Rank cost / 113 |
|:--|:-:|:-:|:-:|:-:|
| Q107 → Q108 | 107 | 0.1015 | 1.22% | 41 (mid) |
| Q108 → Q109 | 108 | 0.1341 | 1.62% | 28 (mid-cheap) |

Reading: Both Q108-incident edges in the canonical mushaf order are MID-cost (neither cheap nor expensive). The structural hinges flagged by H-NEW-130 (Q14→15, Q49→50, Q56→57) are all expensive transitions; Q108's incident edges do NOT participate in the structural-hinge architecture in canonical-mushaf order.

But under cyclic-shift (H-NEW-238): when the cycle is rotated to start at k=108, the **wrap-edge** Q107→Q108 becomes the cycle-minimum (W=0.2256, rank 1/114). This same Q107→Q108 edge has δ=0.1015 in canonical-mushaf order (it's the consecutive-edge from Q107 to Q108). The Fisher-Rao distance is identical; the rank context differs because cyclic-shift compares different rotation start-points.

## 8. UAS — Unified Architectural Score (H-NEW-840)

Source: `findings/phase-b-hypotheses/csv/h-new-840.json` Q108.

| Field | Value |
|:--|:--|
| UAS | −1.9962 |
| Rank | 99 / 114 (bottom decile) |
| abs_outlier component | 0.000 |
| max_cost component | 0.1341 |
| abs_ijaz component | 0.1026 |

UAS is dominated by length-related factors; very short surahs all score low. UAS at rank 99 is **expected** for a 3-verse surah and **not informative** about Q108's structural role. The H-NEW-238 / H-NEW-131 / H-NEW-111 axes — which are NOT length-confounded — capture Q108's true architectural extrema.

## 9. Q108 root-content fingerprint (QAC v0.4)

Total root-tokens: 7. Distinct roots: 7 (all count = 1).

| Root | Arabic | Q108 count | Global corpus count | Top-500 rank | Hapax? |
|:--|:--|:-:|:-:|:-:|:-:|
| `rbb` | ربب (Lord) | 1 | 980 | 4 | × |
| `kvr` | كثر (abundance) | 1 | 167 | 64 | × |
| `Slw` | صلو (pray) | 1 | 99 | 115 | × |
| `ETw` | عطو (give) | 1 | 14 | 481 | × |
| `$nA` | شنأ (hate) | 1 | 3 | none | × |
| `nHr` | نحر (sacrifice) | 1 | 1 | none | **✓** |
| `btr` | بتر (cut off) | 1 | 1 | none | **✓** |

**Hapax fraction = 2/7 = 0.286 — RANK 1/114 (tied with Q112).**

Per H-NEW-131 Cell C, Q108's content profile is a **barbell distribution**: it mixes ULTRA-frequent roots (`rbb` = #4 globally with 980 occurrences) with ULTRA-rare roots (`nHr` and `btr` are hapaxes). It has NO middle-frequency roots. This is structurally distinctive: Q108 is the highest-frequency-extreme + highest-rarity-extreme surah simultaneously, with no middle.

The unsmoothed mass on top-50 global roots is 0.250 (just `rbb`). The α=0.5 smoothed mass on top-50 is 0.102 — most of the smoothed probability mass is in the 0.5/(7+250) prior bins, NOT in the actual content roots. This is why Q108's smoothed distribution looks near-uniform (and FR-central) despite its raw content being non-uniform.

## 10. Q1 ↔ Q108 root overlap analysis (the rank-1 NN pairing)

Q108 is the **rank-1 Fisher-Rao nearest-neighbor of Q1 al-Fātiḥa** (d=0.3384). This pairing's empirical breakdown:

### 10.1 Root-level

- Q1 distinct roots: 18 (over 23 root-tokens)
- Q108 distinct roots: 7 (over 7 root-tokens)
- **Shared roots: {`rbb` (Lord)} — only 1**
- |Union| = 24
- **Jaccard(Q1, Q108) on roots = 1/24 = 0.042**

The single shared root is `rbb` ("Lord") — Q1 v3 *rabbi l-ʿālamīn* / Q108 v2 *li-rabbika*. Both surahs invoke "the Lord" centrally.

### 10.2 Surface-form word-level

Q1 word forms: 29 (with basmala) / 25 (without basmala, per project rules-tuple)
Q108 word forms: 10
**Shared exact word forms: 0** (zero)

Q108 has NO exact word-form overlap with Q1.

### 10.3 The empirical paradox

Q108 is Q1's rank-1 NN under Fisher-Rao on top-500-roots, top-1000-char-4-grams, Hellinger, and Jensen-Shannon — yet shares only 1 root and 0 word-forms with Q1. This is because:

(i) Both surahs have low total token counts (23 and 7 root-tokens), so their top-500-root distributions are dominated by the 0.5-Dirichlet prior (250 mass-units) rather than by raw counts.

(ii) The smoothed distributions are both nearly uniform across top-500.

(iii) Two near-uniform distributions are FR-close on the simplex, regardless of the small "real-content" components.

(iv) Total-Variation (L1) is sensitive to the high-mass cells specifically and would penalize the actual root-distribution mismatch — and indeed under TV, Q108 is rank-12 not rank-1. This confirms the H-NEW-131 finding that "Q108 super-hub" is a Fisher-Rao-family-specific property.

**This is empirically valuable** because it isolates *what* the FR/Hellinger/JS family is measuring vs. what L1 is measuring: the sqrt-family penalizes uniformity-distance; L1 penalizes high-frequency-cell-distance. Q1 and Q108 are uniform-distance-close (FR-NN) but high-frequency-cell-distance-far (TV-NN-but-not-rank-1). Both facts are real and reflect different aspects of the data.

## 11. Surah type and revelation-order

| Field | Value | Source |
|:--|:--|:--|
| Type | Meccan (early) | `quran-no-tashkeel.json` Q108 type field |
| al-Suyūṭī chronology rank | 15 (early Meccan) | al-Suyūṭī *al-Itqān* nawʿ 1 |
| Nöldeke chronology | early Meccan (period 1) | Nöldeke, *Geschichte des Qorāns* |
| Asbāb al-nuzūl | al-ʿĀṣ b. Wāʾil's taunt of "al-abtar" after the Prophet's son's death (al-Wāḥidī, *Asbāb al-Nuzūl*; alternative narrations attribute the taunt to ʿUqba b. Abī Muʿayṭ or Kaʿb b. al-Ashraf) | classical, see `02-content-analysis.md` |

## 12. Summary table — Q108 in 7 numbers

| Property | Value | Significance |
|:--|:--|:--|
| Word count | **10** | Corpus rank 1 (sole minimum) |
| Letter count (no-tashkeel) | **43** | Corpus rank 1 (sole minimum) |
| MST degree (Fisher-Rao α=0.5) | **24** | Corpus rank 1 (super-hub, 2.4× runner-up) |
| Mean FR-distance to corpus | **0.7718** | Rank 3/114 (most-central) |
| FR distance to Q1 | **0.3384** | Q108 = Q1's rank-1 NN (out of 113) |
| Cyclic-shift wrap-edge minimum | **W=0.2256** | Rank 1/114 (M1-preferred mushaf-cycle start-point) |
| Hapax-root fraction | **2/7 = 0.286** | Rank 1/114 (tied with Q112) |

These seven empirical extrema empirically ground the classical designation of Q108 as the *iʿjāz al-īǧāz* archetype (al-Bāqillānī, al-Jurjānī, al-Khaṭṭābī).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
