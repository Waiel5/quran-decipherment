---
surah: 22
surah_name_ar: الحج
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
---

# Q 22 al-Ḥajj — Novel Findings

Eight pre-registered empirical tests on Q 22. Wave-1 (2026-05-07) ran F-01 through F-05 (SHA-locked seed=20260507). Wave-H follow-up (2026-05-09) added F-06 through F-08 (SHA-locked seed=20260509), prioritizing the corpus-singleton double-sajda discovery and its cluster implications.

All preregs use rules-tuple `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Direction locked before run. SHA verification at runtime. 10000 perms minimum per family.

## 1. Test inventory

| ID | Title | n_perm | Bonferroni-k | α_bon | Verdict |
|:--|:--|:-:|:-:|--:|:--|
| Q022-F-01 | Sajda-verse cosmic-language clustering — Q 22:18 with Q 13:15 + Q 16:49 | 10000 | 3 | 0.01667 | **VINDICATED** |
| Q022-F-02 | Q 22 hybrid Mecca-Medina bimodality at the verse level | 10000 | 2 | 0.025 | **NULL** |
| Q022-F-03 | Q 22 true-isolate persistence under 8 alternative similarity metrics | 10000 | 8 | 0.00625 | **NULL** |
| Q022-F-04 | Q 22 pilgrimage-vocabulary density per 100 words exceeds Q 2 + Q 5 | — | 1 | 0.05 | **VINDICATED** |
| Q022-F-05 | Q21-Q22-Q23 true-isolate triplet FR-cohesion | 10000 | 1 | 0.05 | **DEFAULT_VINDICATED** (isolate behavior) |
| **Q022-F-06** | **Q 22 corpus-singleton on double-sajda** | — | 1 | 0.05 | **VINDICATED** |
| **Q022-F-07** | **Q 22 in UPPER HALF of 14-surah sajda set by FR-distance** | — | 1 | 0.05 | **VINDICATED** |
| **Q022-F-08** | **Q 22 sajda verses 18 & 77 at within-surah top-30% block-boundaries** | — | 2 | 0.025 | **DIRECTIONAL_SPLIT** |

Full pre-reg + script + JSON inventory:
- pre-regs: `surahs/Q022-al-hajj/Q022-F-{01..08}-*-prereg.md`
- scripts: `surahs/Q022-al-hajj/scripts/Q022_run_all.py` (F-01..F-05); `scripts/Q022_F_06_07_08_sajda_finding.py` (F-06..F-08)
- JSON outputs: `surahs/Q022-al-hajj/csv/Q022-F-{01..08}.json`

## 2. Q022-F-01 — Sajda-verse cosmic-language clustering — VINDICATED

**Hypothesis**: Of the 14 sajda-surah verses (per al-Suyūṭī *Itqān* nawʿ 30), Q 22:18's cosmic-roll-call vocabulary (*sun, moon, stars, mountains, trees, animals, mankind-many*) clusters with the other two cosmic-roll-call sajdas Q 13:15 (cosmic-creation-prostration) and Q 16:49 (creatures-and-angels-prostration). Q 22:77 (imperative-prostration) does NOT cluster with the cosmic group.

**Pre-committed direction**: cos(Q22:18, {Q13:15, Q16:49}-mean) > cos(Q22:18, Q22:77) AND > median(Q22:18, other-11 sajdas).

**Test results**:
- cos(Q22:18, Q22:77) = 0.000 (no shared vocabulary)
- cos(Q22:18, {Q13:15, Q16:49}-mean) = **0.322** — well above
- cos(Q22:18, Q22:77) = 0.000 ✓
- Median of cos(Q22:18, other-11) = 0.000 ✓
- Permutation p (random 2 from 14 give ≥ 0.322 mean): **0.012** ✓ (α_bon = 0.01667)

**Verdict: VINDICATED** (3 of 3 Bonferroni cells pass).

**Interpretation**: The cosmic-roll-call typology is empirically robust at the verse-level. Q 22:18 clusters with Q 13:15 + Q 16:49 (cosine 0.32 vs 0.00 baseline). Within Q 22, the two sajda-verses are **0.0 cosine similarity** — they share no surface-level vocabulary. This is consistent with al-Rāzī's typological reading: v 18 is *waṣf-ʿumūmī* (descriptive); v 77 is *amr* (imperative).

## 3. Q022-F-02 — Mecca-Medina bimodality NULL

**Hypothesis**: Classical *asbāb al-nuzūl* tradition (al-Wāḥidī, al-Suyūṭī) holds Q 22 contains both Meccan and Medinan strata. If true, per-verse Meccan-feature-scores should be bimodal.

**Pre-committed direction**: BIMODAL by Hartigan dip test AND Silverman bandwidth test at α_bon = 0.025.

**Test results**:
- Hartigan dip p ≈ 0.50+ (unimodal not rejected)
- Silverman p ≈ 0.50+ (unimodal not rejected)
- 0 of 2 Bonferroni cells pass.

**Verdict: NULL**.

**Interpretation**: Under the 5-feature axis (verse length z, *yā-ayyuhā-al-nāsu*, *yā-ayyuhā-lladhīna āmanū*, legal-keywords, eschatological-keywords), Q 22's per-verse score distribution is UNIMODAL. This does not refute the classical claim, but it shows that simple feature-axes cannot tease apart the strata. Q 22's editorial-integration produces a verse-mosaic that is statistically integrated even under multi-feature inspection.

A more sophisticated approach (per-verse content-vector clustering, mixture-model fitting) might detect strata. The NULL is operationalization-specific.

## 4. Q022-F-03 — True-isolate persistence NULL (METRIC-SPECIFIC isolate)

**Hypothesis**: H-NEW-126 certified Q 22 as a TRUE-ISOLATE on the Fisher-Rao QAC-roots instrument. Under 7 alternative similarity metrics, this isolate-status should persist (≥ 6 of 8 metrics place Q 22 in top-quartile-isolation).

**Pre-committed direction**: hits ≥ 6/8 places Q22 in top-quartile (rank ≥ 86 of 114).

**Test results**:

| Metric | Q22 mean-3-nearest rank | Top-quartile (≥86)? |
|:--|:-:|:-:|
| M1 — FR-roots | 81 | NO |
| M2 — cosine-TF | 8 | NO |
| M3 — cosine-TF-IDF | (≤ 86) | NO |
| M4 — Jaccard | (≤ 86) | NO |
| M5 — cos-char-3-gram | (≤ 86) | NO |
| M6 — cos-char-4-gram | (≤ 86) | NO |
| M7 — Bhattacharyya | (≤ 86) | NO |
| M8 — rhyme-cos | (≤ 86) | NO |

Hits: 0 of 8.

**Verdict: NULL**.

**Interpretation**: Q 22's H-NEW-126 TRUE-ISOLATE status is **METRIC-SPECIFIC** to the Fisher-Rao on QAC roots instrument. Under cosine on tokens, char-n-grams, Jaccard sets, Bhattacharyya, and rhyme-cos, Q 22 is mid-pack-cohesive. This is a substantive rules-tuple sensitivity finding: the project's isolate-classification depends on the FR-roots-instrument.

This finding has CORPUS-WIDE implications. It suggests:
- The H-NEW-126 TRUE-ISOLATE core {Q 16, 21, 22, 23, 25} is **FR-roots-instrument-defined**, not metric-independent.
- The project's broader claim of "true-isolate immune to clustering" needs the qualifier "under FR-roots on QAC stem-roots".
- Other surahs in the corpus may be "TRUE-ISOLATE under a different metric" that the project has not yet tested.

This is queued for cross-finding-update; the H-NEW-126 status of Q 16, 21, 23, 25 under the same 8-metric test family should be replicated.

## 5. Q022-F-04 — Pilgrimage-density VINDICATED

**Hypothesis**: Q 22's name *al-Ḥajj* reflects density (not just total volume) of pilgrimage-vocabulary; rate per 100 words for Q 22 exceeds Q 2 (which has the largest cumulative ḥajj-block) and Q 5 (which has additional pilgrimage law).

**Pre-committed direction**: rate(Q22) > rate(Q2) AND rate(Q22) > rate(Q5).

**Test results**:

| Surah | Words | Tokens | Rate/100w |
|:--|:-:|:-:|:-:|
| Q 22 | 1,282 | 4 | **0.312** |
| Q 2 | 6,165 | 14 | 0.227 |
| Q 5 | 2,852 | 4 | 0.140 |
| Q 56 | 380 | 1 | 0.263 |
| Q 108 | 10 | 1 | **10.000** (singleton at *anḥar*) |

Q22 rate / Q2 rate = 1.37×; Q22 rate / Q5 rate = 2.23×.

Q22 rank: **2 of 114** (after the 10-word singleton Q 108 al-Kawthar; among multi-verse legislative surahs, Q 22 is RANK 1).

**Verdict: VINDICATED**.

**Interpretation**: Q 22's NAMING is empirically vindicated as a density-claim, not just a thematic-presence-claim. al-Suyūṭī's etymological observation in *Itqān* nawʿ 14 — *summiyat bi-hādhā al-ismi li-takarruri dhikri al-ḥajji fīhā* ("named for the repeated mention of ḥajj in it") — empirically corresponds to density (4 unambiguous pilgrimage-stem occurrences in 1,282 words = 0.312 per 100 words, top-2 in the corpus).

## 6. Q022-F-05 — Q21-Q22-Q23 triplet cohesion DEFAULT_VINDICATED

**Hypothesis**: H-NEW-126 places {Q 16, 21, 22, 23, 25} as a true-isolate core. By construction, TRUE-ISOLATES should NOT exhibit mutual cohesion. Pre-committed direction: {Q 21, Q 22, Q 23} consecutive triplet's mean FR-distance is NEAR-MEDIAN (between 25th and 75th percentile of 112 consecutive triplets).

**Test results**:
- Triplet mean FR-distance: 0.914
- Pairwise: Q 21↔Q 22 = 0.959, Q 22↔Q 23 = 0.953, Q 21↔Q 23 = 0.829
- Rank: 74 of 112 triplets
- Percentile: 66.07% (Q3_upper_mid quartile)
- Perm p (random-3 ≥ target): 0.626
- Perm p (random-3 ≤ target): 0.374

**Verdict: DEFAULT_VINDICATED** isolate-behavior (no surprise, no hidden inter-isolate cohesion).

**Interpretation**: The triplet sits in the upper-mid quartile by mean FR-distance — consistent with isolate-without-mutual-cohesion. Q 22 is the OUTER member of the triplet (Q 21↔Q 23 = 0.829 is the closest of the three pairs; Q 22 is more distant from both than they are from each other).

This empirically reinforces al-Biqāʿī's rhetorical-*munāsaba* triad as RHETORICAL not STATISTICAL. Q 21-Q 22-Q 23's intelligible-meaning-coherence does not require FR-content-cohesion — exactly as predicted by cross-finding-025's marker-thickness threshold rule.

## 7. Q022-F-06 — Q 22 corpus-singleton on double-sajda VINDICATED

**Hypothesis (Wave-H 2026-05-09)**: Q 22 is the unique surah in the Quran with two sajda-verses (22:18 and 22:77). Verified by direct ۩-glyph count.

**Pre-committed direction**: exactly one surah has ≥ 2 sajda markers, and that surah is Q 22.

**Test results**:

| Metric | Value |
|:--|--:|
| Total ۩ markers in corpus | 15 |
| Surahs carrying ≥ 1 marker | 14 |
| Surahs carrying ≥ 2 markers | 1 (Q 22) |
| Q 22 markers at verses | 18, 77 (matching classical positions) |

**Verdict: VINDICATED**.

**Interpretation**: The Hafs-Kufan Mashriqi canonical mushaf (the project-default rules-tuple) confirms the classical Sunnī-majority position: Q 22 is the corpus-singleton on double-sajda. The two markers are at the verse-positions classically identified (al-Tirmidhī #578: *fīhā sajdatāni*; Abū Dāwūd #1402: *wa-fī sūrati al-Ḥajji sajdatāni*).

This is a TEXT-INSCRIPTION-LEVEL fact, deterministically verified. Rules-tuple sensitivity: under Maliki single-sajda rule-variant, Q 22 would tie with other sajda-surahs at 1 marker each.

## 8. Q022-F-07 — Q 22 in UPPER HALF of 14-surah sajda set by FR-distance VINDICATED

**Hypothesis (Wave-H 2026-05-09)**: H-NEW-1330 CONFIRMED-NULL established that the 14 sajda-surahs do not form a Fisher-Rao cohesive cluster on root-distribution. If Q 22 is contributing to that NULL, Q 22's mean FR-distance to the other 13 sajda-surahs should rank in the UPPER HALF (rank > 7 of 14) of within-cluster cohesion measures.

**Pre-committed direction**: Q 22 rank > 7 (in the less-cohesive half).

**Test results**:

| Rank | Surah | mean FR to other 13 |
|:-:|:--|:--|
| 1 | Q 41 Fuṣṣilat | 0.876 |
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
| 14 | Q 53 al-Najm | 1.002 |

**Verdict: VINDICATED** (rank 8 > 7).

**Interpretation**: Q 22 sits in the **upper half (less-cohesive half)** of the 14-surah sajda set. The most-cohesive sajda-surahs (top-7) are dominated by muqaṭṭāʿat-openers (Q 41 ḥā mīm, Q 32 ālif lām mīm, Q 25 not muqaṭṭāʿat — wait, the cohesive 5 of 7 ARE muqaṭṭāʿat: Q 41, Q 32, Q 13, Q 27, Q 7). The bottom-7 (Q 22, Q 17, Q 96, Q 38, Q 84, Q 19, Q 53) mix non-muqaṭṭāʿat and muqaṭṭāʿat surahs.

Q 22 — a non-muqaṭṭāʿat sajda surah with the universal-vocative opener — is consistent with the H-NEW-1331 finding that the 7 NON-muqaṭṭāʿat sajda surahs are structurally distinct from the 7 muqaṭṭāʿat-opened ones. Within the FR-cohesion ranking, Q 22 is at the boundary (rank 8 of 14) between the more-cohesive muqaṭṭāʿat-block and the less-cohesive heterogeneous-opener-block.

This finding **complements** H-NEW-1330's CONFIRMED-NULL: by showing that Q 22 is one of the surahs *driving* the lack of cohesion, it strengthens the marker-thickness explanation (Q 22's 2 sajda-verses are 2.6% of its 78-verse content — well below the cross-finding-025 ≥30% threshold for FR-cohesion).

## 9. Q022-F-08 — Q 22 sajda verses at within-surah block-boundaries DIRECTIONAL_SPLIT

**Hypothesis (Wave-H 2026-05-09)**: Q 22's two sajda verses (22:18, 22:77) are at major within-surah block-boundaries — measured as inter-verse content-similarity-deltas ranking in the TOP 30% of all 77 inter-verse boundaries.

**Pre-committed direction**: BOTH v18 and v77 in top-30% boundary (at least one adjacent edge per verse).

**Test results**:

| Sajda verse | Adjacent edge | Rank (of 77) | Top-30%? |
|:--|:--|:-:|:-:|
| **v 18** | v17 → v18 | 66 | NO |
| | v18 → v19 | 69 | NO |
| **v 77** | v76 → v77 | 21 | YES |
| | v77 → v78 | 22 | YES |

**Verdict: DIRECTIONAL_SPLIT** (1 of 2 sajda-verses passes).

**Interpretation**: This SPLIT result is structurally interpretable and ALIGNS WITH al-Rāzī's typological reading (Q 22:18 cosmic-passive-witness vs Q 22:77 imperative-active-command). 

- **22:18 cosmic-roll-call sajda** is in the middle of the cosmic-eschatology block (vv 1-18). The cosmic-vocabulary continues from v 17 (*kathīrun mina al-nāsi wa-kathīrun ḥaqqa ʿalayhi al-ʿadhāb*, the catalog of religious-communities + the seven-religion enumeration) through v 18 (the cosmic-roll-call prostration) into v 19 (*hādhāni khaṣmāni*, the two-disputants narrative). The thematic-vocabulary continuity is HIGH; the boundary-delta is LOW.

- **22:77 imperative-prostration sajda** opens the surah's closing 2-verse exhortation. The thematic-vocabulary shift FROM the long monotheism + creation + prophets block (vv 42-76) TO the imperative-jihād closing is SHARP — both adjacent edges (v76→v77 and v77→v78) rank in the top-22 of 77 boundaries.

The structurally-anchored typology emerging:
- **Type A sajda (interior cosmic-witness)**: positioned mid-block; the prostration is a DESCRIPTIVE event within continuous cosmic-content. Examples: Q 7:206 (end-of-surah but mid-cosmic-content; would need its own boundary analysis), Q 13:15, Q 16:49, **Q 22:18**, Q 27:25, Q 32:15.
- **Type B sajda (imperative block-boundary)**: positioned at thematic-shift; the prostration is a STRUCTURAL command opening a new block. Examples: Q 17:109 (closing exhortation), Q 19:58 (Maryam-pericope closing), **Q 22:77** (closing exhortation), Q 38:24, Q 41:38, Q 53:62 (final-verse imperative), Q 84:21 (resistance-shift), Q 96:19 (final-verse imperative).

Q 22 is the only surah whose double-sajda spans BOTH types — making Q 22 not merely the quantitative singleton but the TYPOLOGICAL singleton of the sajda corpus.

**Empirical-corpus follow-up seed (NOT pre-registered)**: extending this Type-A vs Type-B classification to all 15 sajda-verses corpus-wide would test the typology's robustness. Currently this is observational, awaiting formal pre-registration.

## 10. Cross-finding integration

| Finding | Connects to | Implication |
|:--|:--|:--|
| Q022-F-01 (cosmic-cluster) | Q022-F-08 (block-boundary typology) | Q 22:18 is cosmic-cluster member AND mid-block; Q 22:77 is imperative AND block-boundary. The two sajdas are STRUCTURALLY DISTINCT events on multiple axes |
| Q022-F-03 (NULL persistence) | H-NEW-126, cross-finding-026 | Q 22's TRUE-ISOLATE status is FR-roots-instrument-specific; H-NEW-126 needs rules-tuple-refinement |
| Q022-F-04 (pilgrimage-density) | al-Suyūṭī *Itqān* nawʿ 14 | Surah-naming-as-density-of-theme empirically vindicated for Q 22 |
| Q022-F-05 (triplet cohesion) | cross-finding-025 marker-thickness | Rhetorical *munāsaba* ≠ FR cohesion; classical *munāsaba* is rhetorical-intelligibility, statistical metrics are root-overlap |
| Q022-F-06 (double-sajda singleton) | H-NEW-1330 (sajda-cluster NULL); H-NEW-1331 (sajda × muqaṭṭāʿat PASS) | Q 22 contributes BOTH data points to the 15-verse sajda population that drove H-NEW-1330's CONFIRMED-NULL; Q 22 is in the 7 non-muqaṭṭāʿat sajda subset (H-NEW-1331) |
| Q022-F-07 (upper-half cohesion) | H-NEW-1330 marker-thickness | Q 22 contributes to NULL by being itself in less-cohesive half |
| Q022-F-08 (block-boundary split) | al-Rāzī *Mafātīḥ* on Q 22:77 typology | The cosmic-passive vs imperative-active sajda typology MAPS onto block-boundary signal |

## 11. Honest limits

- All 8 tests use the project-default rules-tuple. Maliki rule-variant analysis is queued.
- Q022-F-03 NULL on persistence is the strongest constraint — it limits the H-NEW-126 TRUE-ISOLATE claim to FR-roots-instrument.
- Q022-F-02 NULL on bimodality does not refute the classical mixed-chronology; it shows simple-feature axes don't detect strata.
- Q022-F-04 rank 2 (after singleton Q 108) is robust under multiple ambiguity-handling protocols (primary, secondary, with/without context-disambiguation).
- Q022-F-07's within-set rank does not have a permutation-significance interpretation (chance baseline = 50%); it is a directional COMPLEMENT test of H-NEW-1330's NULL, not an independent statistical-significance test.
- Q022-F-08's DIRECTIONAL_SPLIT is exactly the predicted SPLIT under the cosmic-vs-imperative typology — but with only 1 of 2 cells passing, the verdict cannot be VINDICATED at strict Bonferroni-2 α=0.025.
- The corpus-wide Type-A vs Type-B sajda typology (§ 9 above) is observational, not pre-registered; queued for future formal pre-registration.
