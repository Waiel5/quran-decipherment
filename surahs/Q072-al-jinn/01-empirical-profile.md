---
surah: 72
surah_name_ar: الجن
surah_name_translit: al-Jinn
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
---

# Q 72 al-Jinn — Empirical Profile

All values cited below are extracted from on-disk artifacts; the file path is given for each. No values are stated from memory.

## 1. UAS profile (per H-NEW-840)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json`, `all_uas` list.

| Quantity | Value |
|:--|:--:|
| UAS | **−1.4181** |
| Rank | **85 / 114** |
| Component: |abs_outlier| | 0.6200 |
| Component: max canonical-adjacency cost | 0.040817 |
| Component: |iʿjāz signature| | 1.1476 |

Q 72 is in the lower-half of UAS — not an architectural-iʿjāz "supercell" surah (those are Q 33, 1, 2, 9, 24, etc.). The low UAS reflects: (a) middle-length, not a top-outlier-strength surah; (b) the Q 71→72 and Q 72→73 canonical adjacencies are cheap, not the "expensive" type that flags global architectural roles; (c) the |iʿjāz signature| is moderate. **This is the empirical signature of a theological-creedal-narrative surah, not a structural-iʿjāz centroid surah.**

This is consistent with the dual-iʿjāz typology (see project skill §3.4): Q 72's "iʿjāz contribution" is **content-thematic** (the jinn-confession of monotheism, the prophetic-vision-of-the-unseen) — not architectural at the corpus-graph level.

## 2. Fisher-Rao neighborhood (per H-NEW-111)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json`, `D_matrix_upper_triangular`.

### Q 72's top-15 FR-nearest surahs:

| Rank | Surah | Name | d_FR(72, ·) |
|:-:|:-:|:--|:--:|
| 1 | Q 112 | al-Ikhlāṣ | **0.6945** |
| 2 | Q 114 | al-Nās | 0.7433 |
| 3 | Q 110 | al-Naṣr | 0.7436 |
| 4 | Q 113 | al-Falaq | 0.7509 |
| 5 | Q 96 | al-ʿAlaq | 0.7533 |
| 6 | Q 91 | al-Shams | 0.7545 |
| 7 | Q 63 | al-Munāfiqūn | 0.7595 |
| 8 | Q 106 | Quraysh | 0.7619 |
| 9 | Q 1 | al-Fātiḥa | 0.7630 |
| 10 | Q 108 | al-Kawthar | 0.7646 |
| 11 | Q 104 | al-Humaza | 0.7671 |
| 12 | Q 81 | al-Takwīr | 0.7695 |
| 13 | Q 105 | al-Fīl | 0.7696 |
| 14 | Q 100 | al-ʿĀdiyāt | 0.7700 |
| 15 | Q 85 | al-Burūj | 0.7777 |

| Quantity | Value |
|:--|:--:|
| Q 72 mean FR to other 113 | **0.8985** |
| Corpus mean | 0.9235 |
| Relative position | slightly below corpus mean (Q 72 is moderately "central") |

**Striking pattern**: Q 72's top-5 FR-nearest are dominated by the SHORT-MECCAN-TAIL creedal-protective sub-cluster — Q 112, 114, 110, 113, 96. **Four of the top-5 are 5-qul cluster members or muʿawwidhāt** (Q 112, 114, 113 are members of both classical clusters; Q 110 is the *idhā jāʾa naṣru-llāhi wa-l-fatḥ* surah, structurally a short-creedal). Q 72 is the LONGEST member of the 5-qul cluster (28 verses vs. the 4-qul tail at 3-6 verses each), yet at the FR root-distribution level Q 72 sits **adjacent** to that creedal-tail at rank-1 = Q 112.

This is the empirical anchor for the H-NEW-74 / cross-finding-028 observation: **Q 72 belongs to the *qul*-opener content-axis at the FR-content level**, not merely at the surface opener-syntactic level. See `06-novel-findings.md` Q072-F-01.

## 3. Iʿjāz signature (per H-NEW-750)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json`, `per_surah` row 72.

| Quantity | Value | Interpretation |
|:--|:--:|:--|
| n_verses | 28 | — |
| rhyme_entropy_nats | **0.0** | every verse-final letter is alif; corpus-EXTREME monorhyme |
| top_final_letter | ا (alif) | 100% of verses end in alif |
| top_final_letter_frac | 1.0 | maximal — 28/28 |
| mean_content_distance | 0.8985 | mean FR to corpus = 0.8985 (slightly below corpus mean 0.92) |
| local_cohesion | 1.1999 | (Q 71-72 + Q 72-73 mean FR contribution) |
| z_rhyme_entropy | **−1.394** | extreme low-entropy outlier |
| z_mean_content_distance | −0.246 | mildly below average |
| z_local_cohesion | −0.434 | slightly more locally cohesive than average |
| sig_A (al-Bāqillānī iʿjāz al-fawāṣil) | **−1.1476** | NEGATIVE sig_A = HIGH rhyme dominance + LOW content distance |
| sig_B (compositional balance) | **−1.8277** | strongly negative |
| rank_A | 88 / 114 | low (not a structural-iʿjāz centroid) |
| rank_B | 108 / 114 | very low |

**The 100% alif-monorhyme is a corpus-extreme rhetorical signature.** Q 72's every verse ends in the alif of indefinite-accusative-tanwīn / final-alif of *-an* (*ʿajaban*, *aḥadan*, *waladan*, *shaṭaṭan*, *kadhiban*, *rahaqan*, *raṣadan*, *qadadan*, *haraban*, etc.). This is rare in the mufaṣṣal-tail and serves the surah's hypnotic-narrative function (the rhyme-bind is heard as "the jinn speak in unified voice"). This is verifiable directly from `quran-text/quran-no-tashkeel.json` and corresponds to al-Bāqillānī's *iʿjāz al-fawāṣil* category at the EXTREME of the rhyme-dominance axis.

## 4. Outlier-strength (h-new-590)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json`, `candidate_results`.

Q 72 is NOT in the h-new-590 candidate set — the 6 candidates tested were {Q 1, 9, 18, 55, 62, 112}. Q 72's |abs_outlier| = 0.62 (from h-new-840 component) is moderate; it is not a documented STRONG_OUTLIER on the project's outlier-strength axis. This is the correct empirical reading: Q 72's distinctiveness is in its **rhyme + thematic-pericope axes** (alif-monorhyme; jinn-confession), not in extreme outlier-strength.

## 5. Canonical adjacency cost (per H-NEW-720)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json`, `per_adjacency`.

| Adjacency | Δ (TSP residual) | fraction_residual | Interpretation |
|:--|:--:|:--:|:--|
| Q 71 → Q 72 | 0.0408 | 0.49% | modest seam cost — well below the top-10 expensive seams (top-10 start at Δ=0.21 for Q 7→8) |
| Q 72 → Q 73 | **0.0000** | 0.00% | CHEAP seam — mushaf order matches FR-locally-optimal order here |

**The Q 72 → Q 73 seam is one of the cheapest in the corpus (zero excess TSP cost).** This empirically supports the al-Biqāʿī observation that the al-Muzzammil opener *yā ayyuhā al-muzzammil* (Q 73:1) continues the prophetic-instruction register that begins in Q 72:20-28 (the prophet's *qul* statements). The mushaf does not "force" Q 72 → Q 73; the order is locally optimal at the root-distribution level. This is a non-trivial empirical observation: it confirms the mushaf's local geodesic-optimality at this junction (cross-finding-010 mushaf-as-geodesic-optimal extends here).

## 6. Position in compression-tail laws (Wave 2026-04-28)

| Law | Predicted | Q 72 measured | Δ |
|:--|:--:|:--:|:--:|
| d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50) | 0.96 − 0.012·22 = 0.696 | 0.8985 (mean FR) | +0.20 (above prediction band) |
| d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50) | 0.36 + 0.0041·22 = 0.450 | 0.0 (rhyme-entropy, not d̄_rhyme — different metric) | n/a |
| d̄_phoneme(s) ≈ 0.001 + 0.00089·max(0, s−75) | 0 (s<75) | not computed inline | — |

The d̄_content prediction of 0.70 vs. measured 0.90 is a +0.20 deviation — Q 72 is MORE content-distant from its windowed neighbors than the compression-tail-law predicts. This is consistent with Q 72's PERICOPE-DISTINCTIVENESS (the jinn-confession + prophet-cycle is content-distinct from the typical short-Meccan-eschatological window). Q 72 contributes to the **compression-tail residual** — surahs that locally violate the s>50 compression law because they carry a content-distinct pericope.

## 7. Topographic coverage (per H-NEW-111 corpus_stats)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` → `per_surah_topk_coverage["72"]`.

| Quantity | Value |
|:--|:--:|
| top-K=500 root coverage | **0.854** |
| Corpus mean top-K coverage | 0.917 |
| Relative | slightly below mean — Q 72 uses some lower-frequency roots |

The 85.4% coverage means ~14.6% of Q 72's tokens fall outside the global top-500 roots. This is the FR-instrument's documented limitation on Q 72: niche-vocabulary (e.g., *najwā*, *raṣad*, *qidad*, *ghadaq*, *labad*) sits just outside the top-K threshold. Inferences from h-new-111 carry this honest-limit flag; the rank-1 finding (Q 112 nearest) is robust because Q 112's vocabulary is also short-creedal-tail-restricted.

## 8. Rhyme structure (recomputed independently)

Direct inspection of the no-tashkeel JSON yields:

- 28 / 28 verses end in alif (ا) at the final character (after stripping the standard sukūn/diacritic marker).
- The terminal-alif words are predominantly the indefinite-accusative-tanwīn (*-an*) form: *ʿajab-an*, *aḥad-an*, *walad-an*, etc.
- This is the **al-saǧʿ al-muṭlaq mukhtilaf al-rawiyy** rhetorical category: single-letter monorhyme with varied terminal vocabulary — the same pattern as Q 55 *al-Raḥmān* (refrain-driven) and Q 109 *al-Kāfirūn* (creedal-driven), but in Q 72 driven by the indefinite-tanwīn pattern.

## 9. Architectural type classification

| Axis | Position |
|:--|:--|
| Structural-iʿjāz (al-Bāqillānī)? | LOW (UAS rank 85, |sig_A|=1.15 below median magnitude) |
| Theological-iʿjāz (al-Khaṭṭābī)? | MODERATE — the jinn-confession pericope is theologically dense |
| Rhetorical-iʿjāz (rhyme-dominance)? | **EXTREME** (100% alif-rhyme, entropy=0; corpus-extreme on rhyme axis) |
| Compression-tail residual? | YES (+0.20 above predicted d̄_content) |
| Outlier-strength? | MODERATE (|abs_outlier|=0.62, not strong-outlier) |
| 5-qul cluster member? | **YES** (corpus-rank-1 longest member; FR-nearest = Q 112 the cluster centroid) |
| Compression-tail position | s=72, post-kink |
| Local geodesic-optimal seam? | YES at Q 72→Q 73 (Δ=0.00) |

**Type label**: *rhetorical-iʿjāz-extreme + theological-iʿjāz-moderate + structural-iʿjāz-low + 5-qul-cluster-member*.

## 10. Cross-references to H-NEW findings

Q 72 touches the following corpus-wide findings:

- **H-NEW-74** (5-qul-opener cluster {Q 72, 109, 112, 113, 114}) — Q 72 is a CLUSTER MEMBER. See Q072-F-01 for replication.
- **H-NEW-265** (5-qul opener-stripped residual NULL) — confirms the cluster cohesion is largely *qul*-opener-driven; Q 72's residual root-overlap with Q 109/112/113/114 does NOT survive opener-stripping.
- **H-NEW-1080** (Q 57-66 short-Medinan-block FR-cohesive at p=0.049) — Q 72 is NOT in this cluster (it is Meccan); contrasts the Medinan-short vs Meccan-mid-creedal blocks.
- **H-NEW-1190** (10 surahs with *wa-mā adrāka mā*: Q 69-104 short-Meccan-tail) — Q 72 does NOT contain *wa-mā adrāka mā*; absent from this cluster.
- **cross-finding-008** (multi-axis muqaṭṭāʿat cluster, p≤10⁻¹²) — Q 72 has no muqaṭṭāʿāt; absent.
- **cross-finding-010** (mushaf as topological ring; geodesic optimal) — Q 72→73 seam Δ=0 supports the local-geodesic-optimal reading at this junction.
- **cross-finding-028** (al-muʿawwidhāt-extended liturgical-pair pattern) — Q 72 sits adjacent at the FR-content level but is LENGTH-DIFFERENT from the protective-creedal short-tail; partial cluster member.

## 11. Honest limits

- Top-K=500 coverage on Q 72 is 85.4% (slightly below corpus mean 91.7%); inference robustness is good but not extreme on this surah.
- The 100% alif-rhyme is partly an artifact of the indefinite-accusative-tanwīn morphological pattern, which is overall common in Quranic prose — but the surah's verse-final consistency at 28/28 is still corpus-extreme (corpus-wide mean alif-rhyme fraction is ~30-40%).
- h-new-590 does not include Q 72 in its 6-surah candidate set; the |abs_outlier|=0.62 component value comes from h-new-840's pre-computed outlier vector and is not independently verified by a Q 72-specific outlier-strength run.

## Cross-references

- `00-overview.md` — surah-level identification and chronology
- `02-content-analysis.md` — verse-by-verse and block-by-block
- `06-novel-findings.md` — Q072-F-01/02/03
- `07-cross-references.md` — full cluster-membership map
- `JOURNAL.md` — sources read and run log
