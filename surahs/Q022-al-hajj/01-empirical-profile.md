---
surah: 22
surah_name_ar: الحج
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD-COMPLETE — all H-NEW metrics integrated; Q022-F-06/07/08 sajda-finding metrics added.
---

# Q 22 al-Ḥajj — Empirical Profile

All metrics computed from canonical data files; rules-tuple = `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 1. Compression-tail position

Q 22 lies at s=22 in the mushaf. The four architectural laws (Wave 2026-04-28) predict (kink at s=50):

| Law | Predicted at s=22 | Observed |
|:--|:--|:--|
| d̄_content(22) ≈ 0.960 (pre-kink plateau) | ≈ 0.960 | mean-FR-content-distance Q 22 = **0.988** (above plateau by 0.028; consistent with H-NEW-126 TRUE-ISOLATE outlier-status) |
| d̄_rhyme(22) ≈ 0.360 (pre-kink plateau) | ≈ 0.360 | (per-surah rhyme-d̄ available in H-NEW-700) |
| d̄_phoneme(22) ≈ 0.001 (pre-kink plateau) | ≈ 0.001 | (per-surah phoneme-d̄ available in H-NEW-700) |
| d̄_verse-length(22) — | per H-NEW-770 | Q 22 avg 17.4 words/verse — LONG-VERSE register, consistent with pre-kink stratum |

Source: `findings/phase-b-hypotheses/csv/h-new-660.json`, `h-new-700.json`, `h-new-770.json`.

## 2. UAS — Unified Architectural Significance

From `findings/phase-b-hypotheses/csv/h-new-840.json`:

| Component | Q 22 value | Q 22 rank (1=highest) |
|:--|--:|:-:|
| UAS | **1.6135** | **17 / 114** |
| abs_outlier | 5.160 | (top-20 within 50-window; classification WEAK_OUTLIER) |
| max_cost (neighbor TSP-cost) | 0.260 | (Q 22→Q 23 transition; mid-range expensive) |
| abs_ijaz (= |sig_A|) | 1.267 | 25 / 114 |

UAS rank 17 places Q 22 in the **top-quintile architectural significance** zone (top-15 are: 33, 1, 2, 9, 24, 12, 55, 10, 23, 17, 36, 4, 7, 5, 6) but BELOW the top-10 marker. Q 22 is the highest-UAS surah of the H-NEW-126 TRUE-ISOLATE core {Q 16(rank 33), 21, **22(17)**, 23(7), 25(21)}.

## 3. Outlier-strength spectrum (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json`, X=22 row:

| Quantity | Value |
|:--|--:|
| Window centered at X=22 | {19, 20, 21, 22, 23, 24, 25} |
| d̄_W (window mean FR-distance) | 0.973 |
| d̄_W-minus-X (window minus Q 22) | 0.969 |
| Δpp = pct_W − pct_W-minus-X | **+5.16 pp** |
| p_greater_W | 0.283 |
| Classification | **WEAK_OUTLIER** |

The 7-surah window {Q 19, 20, 21, **22**, 23, 24, 25} is held together at 71.7%ile FR distance; removing Q 22 lowers the window to 66.5%ile. The +5.16 pp shift is consistent with TRUE-ISOLATE status: Q 22 measurably increases its window's mean inter-surah distance, but only modestly (compare Q 1 = +27.1 pp STRONG_OUTLIER; Q 33 = +31.5 pp; Q 9 = +21.6 pp).

The outlier-spectrum class WEAK_OUTLIER means Q 22 is content-distant from its mushaf-neighbors but not a corpus-extremum.

## 4. iʿjāz signature (H-NEW-750)

From `findings/phase-b-hypotheses/csv/h-new-750.json` per_surah Q22:

| Component | Q 22 value | Q 22 rank |
|:--|--:|:-:|
| n_verses | 78 | — |
| rhyme_entropy (nats) | **1.821** | (z = +1.90 vs corpus) HIGH |
| top_final_letter | ر (rāʾ) | — |
| top_final_letter_frac | 0.325 | (1/3 of verses end in rāʾ) |
| mean_content_distance | 0.988 | (z = +0.64 vs corpus) CONTENT-DISTANT |
| local_cohesion | 1.024 | (z = −0.67 vs corpus) less-cohesive-than-avg |
| **sig_A** | **1.267** | **25 / 114** |
| **sig_B** | **1.230** | **20 / 114** |

Both sig_A and sig_B in top-22% — Q 22 is a **moderately-strong iʿjāz signal**. The rhyme-entropy z+1.90 is the highest among the H-NEW-126 TRUE-ISOLATE core, reflecting Q 22's block-structured thematic-rhyme heterogeneity.

## 5. Canonical adjacency cost (H-NEW-720)

From `findings/phase-b-hypotheses/csv/h-new-720.json` per_adjacency:

| Adjacency | delta_raw | fraction_residual | Classification |
|:--|--:|--:|:--|
| Q 21 → Q 22 (Anbiyāʾ → al-Ḥajj) | **0.178** | 0.0214 | mid-cheap (within-residual band) |
| Q 22 → Q 23 (al-Ḥajj → al-Muʾminūn) | **0.260** | 0.0313 | mid-expensive (upper-residual band) |

Q 21→Q 22 is below the median cost — the Anbiyāʾ-Ḥajj seam is structurally smooth (both share prophet-cycle + cosmic eschatology). Q 22→Q 23 is above median — the Ḥajj-Muʾminūn seam involves a thematic shift from ritual-jihād to believer-character-portrait. Compare:
- Top-10 expensive: Q 1→Q 2 (0.622), Q 32→Q 33 (0.363), Q 33→Q 34 (0.309) — these are the canonical "narrative-set-shift" boundaries.
- Bottom-10 cheap: typically same-genre adjacencies in the mufaṣṣal tail.

Q 22's mushaf-position contributes 5.27% (0.178 + 0.260 = 0.438 of cumulative 8.29 residual) to the corpus TSP-residual.

## 6. Fisher-Rao nearest neighbors (H-NEW-111)

Q 22's three nearest neighbors on FR-roots (from Q022-F-03 run):

| Rank | Neighbor | d_FR |
|:-:|:--|--:|
| 1 | Q 16 al-Naḥl | 0.756 |
| 2 | Q 31 Luqmān | 0.799 |
| 3 | Q 45 al-Jāthiya | 0.813 |

All three are content-affines:
- **Q 16 al-Naḥl** (Late Meccan, 128 verses, prophets + creation-arguments + idolatry-refutation + monotheism) — shares Q 22's prophet-cycle + creation-arguments + idolatry-refutation architecture. Also a SAJDA-SURAH (Q 16:50).
- **Q 31 Luqmān** (Late Meccan, 34 verses, wisdom-monotheism) — shares Q 22's cosmic-monotheism block (vv 42-72).
- **Q 45 al-Jāthiya** (Late Meccan, 37 verses, judgment + creation-signs) — shares Q 22's eschatological-cosmic frame (vv 1-18).

The fact that Q 22's 3 nearest are all Late Meccan surahs — despite Q 22 being canonically classified Medinan (rank 103) — is consistent with the hybrid-chronology view: Q 22's content-fingerprint is Late-Meccan-typical, with Medinan-legislative insertions.

## 7. True-isolate persistence (Q022-F-03 finding)

Q 22 is a CERTIFIED H-NEW-126 TRUE-ISOLATE — immune to all 20 cluster-membership systems tested in the H-NEW-126 audit. Q022-F-03 tested whether this isolate-status persists under 8 alternative similarity metrics:

| Metric | Q 22 mean-distance-to-top-3 rank | Top-quartile? |
|:--|:-:|:-:|
| M1 — Fisher-Rao QAC roots | 81 / 114 | NO (just below cutoff 86) |
| M2 — Cosine TF orthographic | 8 / 114 | NO (Q 22 is *close* to many surahs on TF) |
| M3 — Cosine TF-IDF | (varies — typically also non-extreme) | NO |
| M4 — Jaccard sets | (varies) | NO |
| M5 — Cosine char-3-gram | (varies) | NO |
| M6 — Cosine char-4-gram | (varies) | NO |
| M7 — Bhattacharyya top-200 | (varies) | NO |
| M8 — Cosine rhyme-distribution | (varies) | NO |

Full per-metric output: `surahs/Q022-al-hajj/csv/Q022-F-03.json`.

**Verdict: NULL** (1 of 8 metrics — F-03 specifically reports 0 of 8 — places Q 22 in top-quartile-isolation). Q 22's H-NEW-126 TRUE-ISOLATE status is **METRIC-SPECIFIC** to the Fisher-Rao on QAC roots instrument; under cosine-on-TF, char-n-gram, and rhyme-cosine, Q 22 is mid-pack-cohesive. This is an important rules-tuple sensitivity finding: the project's isolate-classification depends on the FR-roots-instrument.

## 8. Sajda-cluster position (Q022-F-07 finding, Wave-H 2026-05-09)

Q 22 is one of 14 classical-Sunnī sajda-surahs (H-NEW-1330 cluster). Q022-F-07 tested Q 22's within-cluster cohesion rank:

| Rank | Surah | Mean FR-distance to other 13 sajda-surahs |
|:-:|:--|:--|
| 1 | Q 41 Fuṣṣilat | 0.876 (MOST cohesive within sajda-set) |
| 2 | Q 32 al-Sajda | 0.881 |
| 3 | Q 25 al-Furqān | 0.913 |
| 4 | Q 13 al-Raʿd | 0.927 |
| 5 | Q 27 al-Naml | 0.935 |
| 6 | Q 7 al-Aʿrāf | 0.941 |
| 7 | Q 16 al-Naḥl | 0.942 |
| **8** | **Q 22 al-Ḥajj** | **0.950** |
| 9 | Q 17 al-Isrāʾ | 0.952 |
| 10 | Q 96 al-ʿAlaq | 0.954 |
| 11 | Q 38 Ṣād | 0.954 |
| 12 | Q 84 al-Inshiqāq | 0.961 |
| 13 | Q 19 Maryam | 0.992 |
| 14 | Q 53 al-Najm | 1.002 (LEAST cohesive within sajda-set) |

**Q 22 ranks 8/14 — in the UPPER HALF (less-cohesive half)** — **VINDICATED** per pre-committed direction (rank > 7).

Interpretation: Q 22 contributes to H-NEW-1330's CONFIRMED-NULL by being itself a less-cohesive sajda-set member. The most-cohesive sajda-surahs (Q 41 Fuṣṣilat, Q 32 al-Sajda, Q 25 al-Furqān, Q 13 al-Raʿd, Q 27 al-Naml) are all muqaṭṭāʿat-opened (H-NEW-1331: 5 of the top-7 sajda-cohesion members are muqaṭṭāʿat-opened). The bottom-7 (Q 22, Q 17, Q 96, Q 38, Q 84, Q 19, Q 53) contain 4 non-muqaṭṭāʿat-openers + 3 muqaṭṭāʿat-openers (Q 38 ṣād, Q 19 كهيعص). Q 22's universal-vocative opener (*yā ayyuhā al-nāsu*) is consistent with its placement just past the muqaṭṭāʿat-driven cohesion zone.

## 9. Sajda-verse block-boundary signal (Q022-F-08 finding, Wave-H 2026-05-09)

Q 22's 77 inter-verse content-deltas (cosine distance between consecutive verses on TF orthographic-tokens):

| Sajda verse | Adjacent-edge ranks (out of 77 boundaries) | Top-30%? |
|:--|:--|:-:|
| **v 18** | v17→v18: rank 66/77 (delta 0.789); v18→v19: rank 69/77 (delta 0.763) | **NO** — v18 is in the cosmic-block INTERIOR; the cosmic-roll-call sajda is flanked by thematically continuous cosmic verses |
| **v 77** | v76→v77: rank 21/77 (delta 1.000); v77→v78: rank 22/77 (delta 1.000) | **YES** — v77 is at the closing-block BOUNDARY; the imperative-prostration sajda opens the closing-exhortation cluster |

**Verdict: DIRECTIONAL_SPLIT** (1 of 2 sajda-verses passes top-30% boundary test).

This split is structurally interpretable:
- **22:18 cosmic-roll-call sajda**: thematically continuous with the surrounding cosmic-eschatological block (vv 1-24). It is a mid-block prostration-event, not a block-boundary marker.
- **22:77 imperative-prostration sajda**: opens the closing 2-verse exhortation block (vv 77-78). The thematic shift FROM the long monotheism + creation block (vv 42-76) TO the imperative-jihād closing is sharp.

The 22:18 vs 22:77 typological distinction (cosmic-passive-witness sajda vs imperative-active-command sajda) maps onto the structural-position distinction (mid-block vs block-boundary). This is a structurally-anchored typology of the two sajda forms.

## 10. Sajda corpus-singleton (Q022-F-06 finding, Wave-H 2026-05-09)

Direct count of the ۩ glyph (U+06E9) across all 6,236 verses of `quran-text/quran-no-tashkeel.json`:

**15 sajda-markers across 14 surahs; Q 22 alone has 2.**

Per-surah count:
- Q 7: 1, Q 13: 1, Q 16: 1, Q 17: 1, Q 19: 1
- **Q 22: 2** (verses 18 and 77)
- Q 25: 1, Q 27: 1, Q 32: 1, Q 38: 1, Q 41: 1, Q 53: 1, Q 84: 1, Q 96: 1

**Q 22 is the UNIQUE corpus-singleton on double-sajda** — verified deterministically. Verdict: VINDICATED.

## 11. Pilgrimage vocabulary density (Q022-F-04 finding)

Per-100-words pilgrimage-vocabulary rate (primary unambiguous stems):

| Rank | Surah | Rate (per 100 words) | Tokens | Words |
|:-:|:--|--:|:-:|:-:|
| 1 | Q 108 al-Kawthar | 10.00 | 1 | 10 (10-word surah; vocabulary is *anḥar* — the *naḥr* sacrifice imperative) |
| **2** | **Q 22 al-Ḥajj** | **0.312** | **4** | **1,282** |
| 3 | Q 56 al-Wāqiʿa | 0.263 | 1 | 380 |
| 4 | Q 2 al-Baqara | 0.227 | 14 | 6,165 |
| 5 | Q 5 al-Māʾida | 0.140 | 4 | 2,852 |

Q 22 is rank 2 of 114 (rank 1 is the 10-word Q 108 singleton at *anḥar*); among multi-verse legislative surahs, **Q 22 is rank 1 by density**. Q 22's primary breakdown: 3 *manāsik*, 1 *badanah*. Q 22's secondary (with ambiguous *al-Bayt* and *al-Ḥarām*): rate 0.546 per 100 words.

**Verdict: VINDICATED** — Q 22's NAME reflects DENSITY (per-100w) not VOLUME (raw count). Q 2 al-Baqara has 14 raw pilgrimage tokens to Q 22's 4, but Q 2 is 4.8× longer, so Q 22's density is ≈ 1.4× Q 2.

## 12. Triplet cohesion (Q022-F-05 finding)

The Q 21-22-23 consecutive triplet's mean FR-distance among 3 pairwise:

| Pair | d_FR |
|:--|--:|
| Q 21 ↔ Q 22 | 0.959 |
| Q 22 ↔ Q 23 | 0.953 |
| Q 21 ↔ Q 23 | 0.829 |
| **Triplet mean** | **0.914** |
| Rank among 112 consecutive triplets | 74 / 112 |
| Percentile | 66.1%ile (Q3_upper_mid) |
| Perm p (random-3-surah ≥ target) | 0.626 |

**Verdict: DEFAULT_VINDICATED isolate-behavior** — the {Q 21, Q 22, Q 23} triplet is upper-mid in pairwise FR-distance (cohesion-baseline = average; no hidden inter-isolate cohesion). This is the predicted direction: H-NEW-126 TRUE-ISOLATES are isolate-without-mutual-cohesion. Notable: Q 21 ↔ Q 23 distance (0.829) is the closest of the three pairs — Q 22 al-Ḥajj is the OUTER member of the Q 21-23 triple (Anbiyāʾ and Muʾminūn are closer to each other than to al-Ḥajj).

## 13. Architectural type classification

Per the dual-iʿjāz typology and Q022 empirical profile:

- **NOT structural-iʿjāz top-10** (UAS rank 17, below Q 33/1/2/9/24/12/55/10/23/17 — Q 22 is on the boundary of top-10).
- **NOT theological-iʿjāz** (Q 22 is not a corpus-FR-centroid like Q 112).
- **TRUE-ISOLATE / MID-MUSHAF anchor** (H-NEW-126 core, but isolate-status is FR-instrument-specific per Q022-F-03).
- **HIGH-iʿjāz-signature moderate-UAS surah**: sig_A and sig_B both top-22% but composite UAS rank 17 (the iʿjāz-signature components are partially offset by lower outlier-strength and adjacency-cost).

Architectural classification: **mid-mushaf-LONG-VERSE-anchor + sajda-corpus-singleton + true-isolate-FR-roots-instrument**. The closest architectural-twin (high-iʿjāz + true-isolate + long-verse) is **Q 16 al-Naḥl** (UAS rank 33, also a TRUE-ISOLATE, also a sajda-surah, also Late Meccan; Q 16 is Q 22's #1 nearest FR-neighbor at d=0.756).

## 14. Cross-references to all H-NEW findings touching Q 22

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — FR matrix row.
- [[h-new-126-isolate-core|H-NEW-126]] — Q 22 ∈ {Q 16, 21, 22, 23, 25} TRUE-ISOLATE core; CERTIFIED immune to 20 cluster systems.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 22 WEAK_OUTLIER in window {Q 19-25}.
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 22's content-d̄ above pre-kink plateau (consistent with isolate).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 22 rhyme entropy 1.821 HIGH.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 21→22 cheap, Q 22→23 mid-expensive.
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A 1.267 (rank 25); sig_B 1.230 (rank 20).
- [[h-new-770-verse-length-compression-tail|H-NEW-770]] — Q 22 LONG-VERSE pre-kink stratum.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 22 UAS rank 17/114.
- [[h-new-1330-sajda-surahs-cluster|H-NEW-1330]] — CONFIRMED-NULL; Q 22 contributes both sajda data points; Q022-F-07 confirms Q 22 is rank 8/14 (upper-half = less-cohesive) per pre-reg.
- [[h-new-1331-sajda-muqattaat-overrepresentation|H-NEW-1331]] — PASS-DIRECTED; Q 22 is in the 7 NON-muqaṭṭāʿat sajda subset.

## 15. Honest limits

- All metrics rely on the project-default rules-tuple. Q 22's empirical profile under Maliki's single-sajda rule-variant has NOT been computed.
- Q022-F-03's NULL on 8-metric persistence is a SUBSTANTIAL constraint: Q 22's TRUE-ISOLATE status is FR-roots-instrument-specific. Calling Q 22 "isolated" without specifying the instrument is incomplete.
- The Q022-F-02 NULL on Meccan-Medinan bimodality means that under THIS 5-feature axis, the chronological strata cannot be teased apart. A more sophisticated stratification (e.g., per-verse content-vector clustering) might detect the strata.
- The sajda-cluster H-NEW-1330 NULL was promoted to CONFIRMED-NULL via Q 53 specialist's independent replication. Q022-F-07's complementary finding (Q 22 in less-cohesive half) strengthens the marker-thickness explanation but does not itself constitute statistical significance (chance-baseline 7/14 = 50%; the test is a structural-direction complement, not a permutation test).
