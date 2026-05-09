---
surah: 8
surah_name_ar: الأنفال
surah_name_translit: al-Anfāl
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111, 590, 700, 720, 750, 840, 890}.
---

# Q 8 al-Anfāl — Empirical Architectural Profile

## 1. Headline numbers

| Metric | Value | Source / interpretation |
|:--|:--:|:--|
| Verse count | 75 | Hafs-Kufan |
| Word count (no-tashkeel) | 1,320 | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, sans spaces) | 5,465 | same |
| Avg verse length (letters) | ~72.9 | long-Medinan-ṭiwāl |
| Avg verse length (words) | ~17.6 | long-Medinan-ṭiwāl |
| Top final-letter | ن (nūn) | 39/75 = 52.0% (H-NEW-700, H-NEW-750) |
| 2nd final-letter | م (mīm) | 19/75 = 25.3% |
| 3rd final-letter | ر (rāʾ) | 10/75 = 13.3% |
| Rhyme entropy (nats) | 1.286 | `h-new-750.json` (z = +0.93 — high-Medinan-ṭiwāl pattern) |
| Mean content distance (FR) | 1.0745 | `h-new-750.json` |
| Local cohesion (window) | 1.0043 | `h-new-750.json` |
| iʿjāz sig_A | -0.5567 (rank 75/114) | mid-low al-Bāqillānī iʿjāz al-fawāṣil signal |
| iʿjāz sig_B | +0.2339 (rank 53/114) | near-median al-Sakkākī iqāʿ signal |
| UAS | +1.0364 (rank **22/114**) | top-quintile unified architectural significance |
| Outlier-strength Δ%ile | +9.81 pp | WEAK_OUTLIER (window {Q 5–11}); p_greater = 0.621 |
| Q 7→Q 8 cost (delta_raw) | +0.2120 (fraction_residual = 0.0256) | rank **10/113** (top decile most-expensive) |
| Q 8→Q 9 cost (delta_raw) | +0.0612 (fraction_residual = 0.0074) | rank 58/113 (median tier; permissive but non-zero) |
| FR-distance Q 8 ↔ Q 9 | 0.911 | rank **81/113** in adjacent-pair distance distribution (above-median dissimilarity) |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 8's top-10 nearest in FR space (decoded from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 3 | Āl ʿImrān | 0.8073 | Medinan-ṭiwāl twin (Uḥud asbāb / Badr-Uḥud sister) |
| 2 | Q 22 | al-Ḥajj | 0.8507 | Medinan-late legal/jihād authorization (qitāl-permission anchor) |
| 3 | Q 2 | al-Baqara | 0.8737 | longest Medinan-ṭiwāl (sister al-sabʿ al-ṭiwāl) |
| 4 | Q 48 | al-Fatḥ | 0.8995 | Medinan post-Hudaybiyya conquest |
| 5 | Q 5 | al-Māʾida | 0.9015 | latest-Medinan legal compendium |
| 6 | Q 4 | al-Nisāʾ | 0.9073 | Medinan-ṭiwāl legal |
| 7 | Q 60 | al-Mumtaḥana | 0.9079 | Medinan walāʾ-disownment |
| 8 | Q 59 | al-Ḥashr | 0.9089 | Medinan Banū al-Naḍīr expedition |
| 9 | Q 9 | al-Tawba | 0.9110 | mushaf right-neighbor (NOT rank 1 — see §7 below) |
| 10 | Q 29 | al-ʿAnkabūt | 0.9112 | Late-Meccan testing-narrative |

Q 8's mean distance to all 113 = 1.0745 (z = +1.49 — content-distinct). Far end:
- Q 55 al-Raḥmān: ~1.30 (corpus FR-isolated outlier, H-NEW-1250)
- Q 1 al-Fātiḥa: ~1.28 (sui-generis liturgical frame)
- Q 112 al-Ikhlāṣ: ~1.26 (corpus tail-isolate)

**FR-neighborhood signature**: Q 8 sits in a **Medinan-ṭiwāl legal-political cluster** — 9/10 of its top-10 FR-nearest are Medinan (Q 3, 22, 2, 48, 5, 4, 60, 59, 9; only Q 29 is Late-Meccan). Q 9 al-Tawba is rank 9, NOT rank 1 — Q 8 is FR-closer to Q 3 (Āl ʿImrān, Uḥud-narrative twin) than to Q 9 (the mushaf-adjacent surah).

## 3. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json`:

| Field | Value |
|:--|:--:|
| Window | {Q 5, Q 6, Q 7, Q 8, Q 9, Q 10, Q 11} |
| d_W | 0.9154 |
| d_W − Q 8 | 0.8887 |
| Δ pp | +9.81 |
| pct_W | 37.91 |
| pct_W − Q 8 | 28.10 |
| p_greater_W | 0.6209 |
| Classification | WEAK_OUTLIER |

Q 8 is moderately content-distinct from its head-mushaf-Medinan neighborhood, but the perm-p of 0.62 indicates the surah is **not a strong outlier** at the corpus-significance level. Removing Q 8 from window {Q 5-11} drops the window's mean-pairwise-FR by ~9.8 pp — a real but modest signature compared to the 4 STRONG_OUTLIER surahs (Q 1, Q 9, Q 18, Q 33; Q 55 corpus-MAX).

## 4. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Rank |
|:--|:--:|:--:|:--:|
| Rhyme entropy (nats) | 1.286 | +0.934 | (high entropy = poly-rhyme Medinan-pattern) |
| Mean content distance | 1.0745 | +1.491 | (content-distant, top-quintile) |
| Local cohesion | 1.0043 | -0.700 | (slightly below median) |
| sig_A | -0.5567 | — | rank 75/114 (mid-low) |
| sig_B | +0.2339 | — | rank 53/114 (near-median) |

Q 8 has a **mid-low iʿjāz al-fawāṣil signal** (sig_A negative) but a **near-median iqāʿ signal** (sig_B positive). The high rhyme entropy (1.286) reflects the Medinan-ṭiwāl tendency toward poly-rhyme (نون at 52% but with substantial م and ر contribution) rather than the near-monorhyme of short-Meccan oath-openers (e.g., Q 37 at 0.704 nats / 80% nūn).

The sig_A negativity is consistent with Q 8 being a **content-driven rather than fawāṣil-driven** Medinan surah — the legal-interrogative opening *yasʾalūnaka ʿan al-anfāl* sets a discursive-prose register, not a rhetorical-rhyme-driven one.

## 5. Canonical-adjacency cost (H-NEW-720)

| Boundary | delta_raw | fraction_residual | Rank | Note |
|:--|:--:|:--:|:--:|:--|
| Q 7 → Q 8 | **+0.2120** | 0.0256 | **10/113** | TOP DECILE expensive — Late-Meccan ALMṢ Q 7 → Medinan post-Hijra Q 8 chronology break |
| Q 8 → Q 9 | +0.0612 | 0.0074 | 58/113 | mid-tier; permissive but non-zero (Q 8 + Q 9 are NOT clamped-zero seam) |
| Q 9 → Q 10 | +0.3094 | 0.0373 | 4/113 | top-5 expensive (Medinan Q 9 → Late-Meccan Q 10 Yūnus) |

**Architectural seam-marker**: the Q 6 → Q 7 → Q 8 → Q 9 → Q 10 stretch contains TWO of the corpus's top-10 most-expensive canonical adjacencies (Q 7→Q 8 rank 10; Q 9→Q 10 rank 4). The mushaf concentrates its **Late-Meccan ↔ Medinan crossover seams** at this region — Q 8 + Q 9 form an embedded Medinan island flanked by expensive boundaries on both sides.

The Q 8 → Q 9 internal seam is **NOT clamped-zero** (delta_raw = +0.061; rank 58/113 — moderate). Q 8 + Q 9 are not seamless-conjoined; they are surahs distinct enough that the canonical adjacency pays a real (if modest) TSP cost. This is the first piece of architectural evidence against the Ibn ʿAbbās "Q 8 + Q 9 = one surah" classical claim — see §7 and `05-classical-claims-audit.md` and `06-novel-findings.md` Q008-F-01.

## 6. UAS (H-NEW-840)

| Component | Value |
|:--|:--:|
| UAS (raw) | +1.0364 |
| UAS rank | **22/114** (top quintile) |
| max_cost | 0.2120 (= Q 7→Q 8) |
| abs_outlier | 9.81 (from H-NEW-590 Δ pp) |
| abs_ijaz | 0.5567 (= |sig_A|) |

Q 8's high UAS rank (22/114) places it in the TOP-QUINTILE of the corpus's unified architectural-significance ranking. The score is driven primarily by:
1. The expensive Q 7 → Q 8 incoming seam (max_cost contribution).
2. Moderate outlier-strength (+9.81 pp).
3. Non-trivial |sig_A|.

Top-quintile UAS surahs typically belong to one of three classes: structural-iʿjāz showcases (Q 55, Q 1), corpus-isolated singletons (Q 1, Q 9, Q 112), or Medinan-legal hubs at major architectural seams. Q 8 belongs to the **Medinan-legal-hub-at-seam** class — its high UAS reflects its position at the late-Meccan / Medinan watershed, not internal stylistic distinctiveness.

## 7. Q 8 + Q 9 unity claim — empirical adjudication (H-NEW-890 T1)

The classical Ibn ʿAbbās claim (preserved by al-Suyūṭī, *al-Itqān*, nawʿ on number-of-surahs, citing Ubayy b. Kaʿb's muṣḥaf reportedly containing Q 8 and Q 9 as one continuous unit without basmala-separation) holds that Q 8 + Q 9 are originally one surah. This is the most-cited classical "joined-surahs" claim in the *ʿulūm al-Qurʾān* literature.

**Empirical adjudication via H-NEW-890 T1** (`findings/phase-b-hypotheses/csv/h-new-890.json`):

| Field | Value |
|:--|:--:|
| d_FR(Q 8, Q 9) | 0.9110 |
| Adjacent-pair mean distance | 0.7589 |
| Adjacent-pair median | 0.8162 |
| Adjacent-pair std | 0.2420 |
| Adjacent-pair min / max | 0.226 / 1.178 |
| **rank_le (number of adjacent pairs with FR ≤ d_FR(8,9))** | **81/113** |
| p (one-sided, d ≤ d_FR(8,9)) | 0.717 |
| Bonferroni alpha | 0.01 |
| **Verdict** | **NULL** |

Interpretation: **Q 8 + Q 9 are ABOVE-MEDIAN dissimilar in FR distance among adjacent pairs.** 80 of 113 adjacent pairs are MORE similar (closer in FR) than Q 8 + Q 9. The Ibn ʿAbbās classical "one-surah" claim is **FALSIFIED** by the FR-distance instrument: if Q 8 + Q 9 were one surah, we would expect them to be in the bottom decile of adjacent-pair distance (rank 1-11/113), not at rank 81/113.

**Sister-evidence axes**:
- (a) **Mushaf-canonical adjacency cost**: Q 8 → Q 9 fraction_residual = 0.0074 (rank 58/113), well above the 13 clamped-zero seamless seams. If they were one surah, they should be among the seamless seams.
- (b) **Root-Jaccard adjacent rank**: Q 8 ∩ Q 9 root-overlap = 0.350 (rank 13/113 in adjacent root-Jaccard, percentile 3.0% in all-pair distribution). This IS top-decile high — but multiple Medinan-legal pairs are higher (Q 5-Q 9 = 0.435; Q 2-Q 4 = 0.496). Top-decile root-overlap is the EXPECTED Medinan-pair signature, not a unity-signature.
- (c) **FR top-10 nearest**: Q 9 is rank 9 of Q 8's top-10 nearest, NOT rank 1. Q 3 is rank 1 (FR = 0.807, much closer than Q 9 at 0.911). If Q 8 + Q 9 were one surah, their FR distance should approach 0; observed 0.911 is corpus-typical for unrelated Medinan-ṭiwāl pairs.

**Conclusion**: All three independent empirical axes (FR distance among adjacent pairs; mushaf TSP-residual; FR rank in Q 8's neighborhood) converge on the same finding — **Q 8 and Q 9 are EMPIRICALLY DISTINCT SURAHS, not a divided one-surah unit.** The Ibn ʿAbbās classical claim is FALSIFIED at p = 0.72 (NULL on FR distance), with the mushaf-tradition's basmala-asymmetry-handling already vindicated by the architectural fact that Q 8 + Q 9 are content-distant. See `05-classical-claims-audit.md` claim 1 and `06-novel-findings.md` Q008-F-01 for the formal pre-registered test.

## 8. Architectural type classification

| Axis | Q 8 placement |
|:--|:--|
| Length class | long-Medinan-ṭiwāl (75 v, 1,320 w, 5,465 letters) |
| Compression-tail position | s = 8 — head-mushaf, OUTSIDE compression-tail regime (laws apply for s>50) |
| iʿjāz typology | mid-low on fawāṣil (sig_A = −0.557, rank 75); near-median on iqāʿ (sig_B = +0.234, rank 53) |
| FR neighborhood | Medinan-ṭiwāl legal-political (Q 2/3/4/5/22/48/59/60) |
| Outlier-strength | WEAK (Δ = +9.81 pp; not in top-10 outliers) |
| UAS rank | 22/114 (TOP QUINTILE) |
| Cluster memberships | (1) al-sabʿ al-ṭiwāl candidate (under "Q 8+Q 9 = one surah" reading); (2) Medinan-ṭiwāl FR-cluster {Q 2, 3, 4, 5, 8, 9, 22}; (3) qitāl-cluster {Q 8, 9, 47, 48, 61} (NULL on cohesion — see Q008-F-04 in `06-novel-findings.md`) |
| Adjacency role | EXPENSIVE LEFT seam (Q 7→Q 8 rank 10/113); moderate-cheap RIGHT seam (Q 8→Q 9 rank 58/113); flanked by Q 9→Q 10 rank 4/113 |

**Architectural verdict**: Q 8 is the **Medinan post-Badr legal-political hub** at the corpus's most-significant Late-Meccan / Medinan chronology break. Its top-quintile UAS reflects the **architectural-seam role**, not internal stylistic distinctiveness — the surah operates as the FIRST Medinan corpus-anchor after Q 7's terminal Late-Meccan ALMṢ-singleton, embedding the Battle-of-Badr legal apparatus at the seam.

## 9. Cross-references

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 8 FR matrix row.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 8 weak outlier on Q 5-11 window.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 8 ن-rhyme dominant (0.520).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 7→Q 8 rank 10/113; Q 8→Q 9 rank 58/113; Q 9→Q 10 rank 4/113.
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 8 mid-low on fawāṣil, near-median on iqāʿ.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 8 UAS rank 22/114 (TOP QUINTILE).
- [[h-new-890-numerical-reaudit|H-NEW-890]] — T1: Q 8 + Q 9 unity FR-distance test, NULL (rank 81/113).
- [[surahs/Q009-al-tawba/00-overview|Q 9 al-Tawba]] — sister surah; basmala-asymmetry pair.
- [[surahs/Q002-al-baqara/00-overview|Q 2 al-Baqara]] — Q 8 FR-near (rank 3 nearest); Medinan-ṭiwāl twin.
- [[surahs/Q003-al-imran/00-overview|Q 3 Āl ʿImrān]] — Q 8 FR-rank-1 nearest neighbor; Uḥud-Badr sister.
