---
surah: 15
surah_name_ar: الحجر
surah_name_translit: al-Ḥijr
file_type: empirical-profile
date_last_updated: 2026-05-08
phase: B+
verdict: COMPLETE
---

# Q 15 al-Ḥijr — Empirical Architectural Profile

Rules-tuple: `(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan, Mashriqi)`. Every numerical value below is computed from data files cited in §10 or pulled directly from H-NEW-XXX artifacts.

## 1. Headline architectural metrics

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **0.439** | **38 / 114** (mid-pack; 18 ranks below Q 14) | [[h-new-840-unified-architectural-score\|H-NEW-840]] all_uas[surah=15] |
| Outlier-strength Δ%ile | **+5.51 pp** | **WEAK_OUTLIER** classification — Q 15 IS a content outlier in window {Q 12-18} | [[h-new-590-outlier-spectrum\|H-NEW-590]] all_surahs_results[X=15] |
| iʿjāz signature sig_A | **−0.765** | **rank 81 / 114** — STRUCTURALLY iʿjāz-NEGATIVE | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| iʿjāz signature sig_B | **−1.087** | **rank 86 / 114** | H-NEW-750 |
| z_mean_content_distance | +0.345 | modestly above corpus mean | H-NEW-750 |
| z_local_cohesion | −0.667 | modestly below corpus median | H-NEW-750 |
| **z_rhyme_entropy** | **−0.421** | **rank ≈ bottom-third** — near-monorhyme on ن | H-NEW-750 |
| Mean Fisher-Rao distance to corpus | **0.9584** | corpus mean 0.9235 | computed from [[h-new-111-fisher-rao-mushaf\|H-NEW-111]] |
| **Top final letter (rāwī)** | **ن (nūn)** | **81.8% of 99 verses** — near-monorhyme | H-NEW-750 |
| Q 14→Q 15 canonical-adjacency cost | **0.1988** | rank ≈ 13 / 113 — top-15 EXPENSIVE | [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] s=14 |
| Q 15→Q 16 canonical-adjacency cost | **0.1698** | rank ≈ 17 / 113 — also expensive | H-NEW-720 s=15 |
| max neighbor canonical-adjacency cost | 0.1988 | the LEFT boundary (Q 14→Q 15) | H-NEW-720 |
| Verse count | 99 | mufaṣṣal-ṭiwāl-class | Hafs-Kufan |
| Word count (no-tashkeel) | 666 | computed | |
| Letter count (no-tashkeel) | 2,891 | computed | |
| Mean words/verse | **6.73** | very short — iterative-narrative pacing | computed |

## 2. The architectural signature: iterative-narrative iʿjāz-NEGATIVE near-monorhyme

Q 15's empirical profile is **the OPPOSITE of Q 14's** on every iʿjāz axis:

| Axis | Q 14 Ibrāhīm | Q 15 al-Ḥijr |
|:--|:--:|:--:|
| UAS rank | 20 / 114 | **38 / 114** |
| Outlier classification | NULL (Δ=−4.28) | **WEAK_OUTLIER (Δ=+5.51)** |
| sig_A rank | **14 / 114** (positive) | **81 / 114** (negative) |
| sig_B rank | 15 / 114 (positive) | 86 / 114 (negative) |
| Top rāwī | د @ 24% (multi-rāwī) | **ن @ 82%** (near-monorhyme) |
| Rhyme entropy z | **+2.07** (corpus-top) | **−0.42** (modestly low) |
| Mean words/verse | 17.0 | **6.7** (rapid-iterative pacing) |
| Q 14→Q 15 seam cost | — | **0.20 EXPENSIVE** |

**The Q 14 → Q 15 transition is the steepest 4-axis architectural drop in the head-mushaf zone**: rhyme-diversity collapses, sig_A flips negative, outlier-classification flips from NULL to WEAK, mean-verse-length quarters. The Q 14→Q 15 canonical-adjacency cost (0.1988, rank ~13/113 top-15 EXPENSIVE) reflects this 4-axis register shift.

**Substantive claim**: Q 15's architectural placement at mushaf-position 15 marks the BOUNDARY of the head-mushaf iʿjāz-positive zone (Q 13/Q 14). Q 15 is the FIRST surah in the iterative-prophet-narrative-monorhyme register that continues through Q 16-Q 19 (each with monorhyme-on-ن or related rāwīs and shorter verses). Q 15's architectural profile fits this iterative-narrative pole, not the head-mushaf high-rhyme-entropy + sig_A-positive pole.

## 3. Fisher-Rao distance row (Q 15 vs all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` D matrix (`D_matrix_upper_triangular`).

**Five FR-nearest neighbours of Q 15**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| **1** | **Q 51 al-Dhāriyāt** | **0.7788** | Late-Meccan iterative-prophet-narrative + cosmology + Lot-narrative parallel |
| 2 | Q 36 Yāsīn | 0.8053 | iterative-narrative + Day-of-Judgment + creation-from-clay-and-fire (Q 36:77-83) |
| 3 | Q 43 al-Zukhruf | 0.8340 | Late-Meccan polemic + iterative cosmological signs |
| 4 | Q 32 al-Sajda | 0.8394 | ALM-cluster; creation-from-clay parallel (Q 32:7-9) |
| 5 | Q 44 al-Dukhān | 0.8433 | Late-Meccan eschatology + warning |

The FR-nearest neighbour is **Q 51 al-Dhāriyāt at 0.7788** — Q 51 also contains a Lot-narrative (Q 51:31-37) and is iterative-prophet-narrative in register. Q 36 Yāsīn is also iterative-narrative + creation-from-clay (Q 36:77-83 parallels Q 15:26-27's *ṣalṣālin min ḥamaʾin masnūn*). Q 32 al-Sajda has the same creation-from-clay parallel.

**Q 15's content-cluster is the iterative-narrative-cosmological cluster** spanning Late-Meccan creation-eschatology surahs. Notably, **none of Q 15's top-5 FR-nearest are mushaf-adjacent** — the FR-nearest neighbours are all in the Q 32-51 mushaf range, NOT in Q 14 or Q 16. Q 15's content-vector is more aligned with the post-Hijra-kink (Late-Meccan-narrative-eschatology) cluster than with its mushaf cohort.

**Five FR-farthest neighbours**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 110 | Q 24 al-Nūr | 1.1091 | Medinan legal-prescriptive (zinā / nūr-mishkāt) |
| 111 | Q 8 al-Anfāl | 1.1148 | Medinan post-Badr legal-narrative |
| 112 | Q 4 al-Nisāʾ | 1.1668 | Medinan family-law |
| 113 | Q 9 al-Tawba | 1.2018 | Medinan legal-uncompromising |
| 114 | **Q 55 al-Raḥmān** | **1.2030** | refrain-saturated nominal-doxological (corpus-most-distant) |

**Q 15's farthest neighbours are Medinan legal surahs + Q 55 al-Raḥmān** — interesting variation from Q 13/Q 14's exclusive Q 55-as-farthest pattern. Q 15's content-vector is FAR from Medinan-legal-prescriptive register; its iterative-narrative-cosmological vocabulary is orthogonal to the Medinan-legal vocabulary.

## 4. Outlier window structure (H-NEW-590, full Q 12-18 window)

The window {12, 13, 14, 15, 16, 17, 18} (size-7 centered on Q 15) yields:

| Removed surah | d̄_W | d̄_W−X | Δ pp | classification | source |
|:-:|:-:|:-:|:-:|:-:|:-:|
| Q 15 | 0.9624 | 0.9572 | **+5.51** | **WEAK_OUTLIER** | H-NEW-590 X=15 |

The full window with Q 15 has d̄_W = 0.962 (65.3%ile); without Q 15, d̄_W = 0.957 (59.8%ile). **Removing Q 15 makes the window LESS FR-distant on average** — i.e. Q 15 is FR-FAR from its mushaf-window neighbours. This is the signature of a **WEAK content outlier**, contrasting with Q 13's NULL (cluster anchor) and Q 14's NULL (cluster anchor).

The outlier-classification reflects that Q 15's content-vector is **closer to the iterative-narrative-cosmological surahs Q 36, 51, 32 than to its mushaf cohort Q 13, 14, 16, 17**. Q 15 is structurally OUT-OF-PLACE with respect to its mushaf neighbours but IN-PLACE with respect to its Late-Meccan-iterative-narrative content cohort.

## 5. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Interpretation |
|:--|:--:|:--:|:--|
| `mean_content_distance` | 0.9584 | +0.345 | modestly above corpus mean |
| `local_cohesion` | 1.0289 | −0.667 | modestly below corpus median |
| `rhyme_entropy_nats` | **0.5376** | **−0.421** | **near-monorhyme on ن at 82%** — modestly low |
| `sig_A` (raw) | **−0.765** | rank **81 / 114** | **structural-iʿjāz-NEGATIVE** |
| `sig_B` (raw) | **−1.087** | rank **86 / 114** |  |

**Q 15 is on the structural-iʿjāz-NEGATIVE side of the al-Bāqillānī axis** — near-monorhyme + content-typical → low sig_A. This puts Q 15 in the *iʿjāz al-fawāṣil-negative* zone, which is the corpus's iterative-narrative-near-monorhyme cluster (cf. Q 12 Yūsuf: sig_A rank 109/114, even more negative; sister near-monorhyme surah).

The Q 15 → Q 12 sig_A signature parallel is informative: both are head-mushaf surahs with **near-monorhyme on ن** (Q 12 at 84%; Q 15 at 82%) and BOTH are sig_A-negative (Q 12 rank 109/114; Q 15 rank 81/114). The narrative-iʿjāz typology has a distinct architectural-axis identity from the rhetorical-iʿjāz-of-fawāṣil (al-Bāqillānī axis).

## 6. The 4-axis signature: NOT a Q 14 twin

Per Q014-F-02:

```
v(Q 15) = [+0.345, -0.549, -0.850, -0.421]   (z_FR, z_sig_A, z_sig_B, z_rhyme)
v(Q 14) = [+0.520, +1.110, +1.144, +2.066]
v(Q 13) = [+0.398, +0.950, +0.868, +1.721]

‖v(15) - v(14)‖ = 3.598   ← Q 15 ≠ Q 14
‖v(15) - v(13)‖ = 3.056   ← Q 15 ≠ Q 13
```

**Q 15 is architecturally NOT a twin of either Q 13 or Q 14**, despite mushaf-adjacency. The 4-axis distance to Q 14 (3.598) is 7.4× the Q 13 ↔ Q 14 twin distance (0.486). The Q 15 signature is iterative-narrative-near-monorhyme; the Q 13/Q 14 signature is didactic-cosmological-prayer-multi-rāwī. The two registers are 4-axis architecturally distant.

## 7. Canonical-adjacency profile (H-NEW-720)

| Pair | TSP-cost (length-units) | Rank /113 | Interpretation |
|:--|:--:|:--:|:--|
| Q 14 → Q 15 | **0.1988** | ≈ 13/113 (top-15 EXPENSIVE) | Ibrāhīm→Ḥijr: didactic-prayer-multi-rāwī (Q 14) → iterative-narrative-near-monorhyme (Q 15); 4-axis register flip |
| Q 15 → Q 16 | **0.1698** | ≈ 17/113 (top-20 EXPENSIVE) | Ḥijr→Naḥl: still iterative-narrative but content-shift to cosmological-grace + bee-parable; another expensive seam |

Q 15 sits between two expensive seams. It is structurally **a transition surah** — entering the head-mushaf iterative-narrative-near-monorhyme zone from the Q 14 didactic-prayer-multi-rāwī zone, and exiting toward the Q 16 cosmological-grace-bee-parable register. The Q 15 zone is NARROW in the mushaf — Q 15 alone holds this specific iterative-narrative-near-monorhyme architectural position; Q 16 shifts again.

## 8. Architectural-cell typology (per cross-finding-026 §13)

By the 7-cell typology in [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.6:

- UAS rank 38/114 — mid-pack, NOT in top-10 *All-axis* / *Structural-twin-pair* cells.
- sig_A z = −0.55 (rank 81) — moderately NEGATIVE on the *iʿjāz al-fawāṣil* axis.
- Rhyme entropy z = −0.42 (rank ≈ 73) — modestly low.
- Outlier strength WEAK_OUTLIER — modest content-distinctness vs mushaf cohort.

| Cell | Q 15 fit? |
|:--|:--|
| All-axis (Q 1) | NO — UAS only 38 |
| Structural-twin-pair (Q 24, 33) | NO — sig_A is moderately negative; not at the negative-tail |
| Structural-twin-pair-of-one (Q 55) | NO — Q 15 is content-typical, not refrain-saturated |
| iʿjāz-al-fawāṣil-pure (Q 86, 89, 100, 106, 113) | NO — Q 15 has sig_A NEGATIVE not POSITIVE |
| iʿjāz-al-maʿnā-extreme (Q 112, 114) | NO — Q 15 is not the FR centroid |
| iʿjāz-al-maʿnā-mild (Q 36, 67, 18) | PARTIAL — Q 15's nearest neighbour is Q 36; both are iterative-narrative-near-monorhyme + sig_A-negative |
| anti-iʿjāz | PARTIAL — Q 15 is sig_A negative + low rhyme-entropy (similar to Q 12 Yūsuf rank 109 sig_A — narrative-iʿjāz signature) |

**Proposed cell (specialist refinement)**: Q 15 fits the **"iterative-narrative-near-monorhyme sig_A-negative" cell**, alongside Q 12 Yūsuf and Q 36 Yāsīn (the other near-monorhyme iterative-narrative head-mushaf surahs). This cell extends the *iʿjāz al-maʿnā-mild* (al-Khaṭṭābī axis) into the iterative-narrative register. The unifying signature is near-monorhyme on ن + iterative-prophet-narrative-or-eschatology + sig_A-negative.

## 9. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 15 WEAK_OUTLIER (X=15, delta_pct=+5.51, p_greater_W=0.3473).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 14→Q 15 expensive (0.199, rank 13); Q 15→Q 16 expensive (0.170, rank 17).
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A=−0.77 rank 81, sig_B=−1.09 rank 86, rhyme entropy z=−0.42.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 38/114, UAS=0.439.
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 15 FR-nearest = Q 51 al-Dhāriyāt (0.779); FR-farthest = Q 55 (1.20).
- [[h-new-97-ALR-prophet-name-cluster]] — Q 15 is in the strict ALR cluster {Q 10, 11, 12, 14, 15}.
- [[cross-finding-008-muqattaat-book-intro-markers]] — Q 15:1 *tilka āyātu al-kitāb wa-qurʾān mubīn* fits the muqaṭṭaʿāt → book-reference pattern (parallel to Q 12:2, 13:1, 14:1).
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13 — proposed "iterative-narrative-near-monorhyme sig_A-negative" cell with Q 15, Q 12, Q 36 as exemplars.
- `surahs/Q014-ibrahim/06-novel-findings.md` Q014-F-02 — Q 14→Q 15 seam established as boundary of head-mushaf iʿjāz-positive zone.

## 10. Data-source paths

- `findings/phase-b-hypotheses/csv/h-new-111.json` (FR D matrix, `D_matrix_upper_triangular`)
- `findings/phase-b-hypotheses/csv/h-new-590.json` (outlier-spectrum, all_surahs_results[X=15])
- `findings/phase-b-hypotheses/csv/h-new-720.json` (per-adjacency, s=14 and s=15)
- `findings/phase-b-hypotheses/csv/h-new-750.json` (per-surah iʿjāz signature[surah=15])
- `findings/phase-b-hypotheses/csv/h-new-840.json` (UAS all_uas[surah=15])
- `quran-text/quran-no-tashkeel.json` (verse text, word/letter counts)
- `data/revelation-order.csv` Q 15 row (Middle Meccan, rev #54 Tanzil / #57 Nöldeke)
- `data/hafs-verse-counts.tsv` line 15 (99 verses)
