---
surah: 84
surah_name_ar: الإنشقاق
surah_name_translit: al-Inshiqāq
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: high structural-iʿjāz (sig_A rank 2/114), UAS rank 25/114, FR-densest neighborhood of the corpus, COHESION member (not outlier)
---

# Q 84 al-Inshiqāq — Empirical Profile

All values are quoted **by value + path**. Rules-tuple for FR/root metrics:
`(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan)`.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

The 114×114 FR distance matrix (`D_matrix_upper_triangular`, entries `[s_i, s_j, d]`, 1-based) gives:

| Metric | Value | Note |
|:--|:--|:--|
| **Q 84 mean FR to all 113 surahs** | **0.8263** | exactly matches `h-new-750.json` `mean_content_distance` = 0.82630 |
| Nearest 5 FR neighbors | Q 103 (0.4830), Q 108 (0.4837), Q 106 (0.4935), Q 100 (0.4938), Q 94 (0.4952) | all juzʾ-30 mufaṣṣal-qiṣār |
| Farthest 3 | Q 3 (1.2005), Q 4 (1.2368), Q 9 (1.2395) | the al-sabʿ al-ṭiwāl legal-narrative giants |
| Q 83 (al-Muṭaffifīn, prev) | FR 0.6522, **rank 33/113** | not a near neighbor |
| Q 85 (al-Burūj, next) | FR 0.5843, **rank 25/113** | closer than the backward neighbor |

**Interpretation.** Q 84's FR mean (0.8263) is well *below* the corpus typical (~0.93–0.96 for the
ṭiwāl), placing it deep in the FR-DENSEST region: its five nearest neighbors are all under 0.50,
all juzʾ-30 short surahs. This is the compression-tail law in action — d̄_content(s) ≈ 0.96 −
0.012·max(0, s−50) ([[h-new-660-compression-tail-gradient]]) predicts low mean-distance for s=84.
Q 84 lives in the cohesive eschatological-creedal short-Meccan cloud, not on a fringe.

## 2. Outlier spectrum (`findings/phase-b-hypotheses/csv/h-new-590.json`, X=84)

| Field | Value |
|:--|:--|
| Window (7-surah, centered) | Q 81-87 |
| d̄_W (with Q 84) | 0.59524 |
| d̄_{W−84} (Q 84 excluded) | 0.59009 |
| pct_W / pct_{W−84} | 0.26 / 0.59 |
| **Δ%ile** | **−0.33** |
| **Classification** | **NULL** (cohesion, not outlier) |

Q 84 is **not** an architectural outlier in its neighborhood. Excluding it barely changes the
window's internal cohesion (Δ%ile = −0.33). This is the honest empirical baseline: whatever is
distinctive about Q 84 (the biplex marker, the k-d-ḥ anchor) lives at the *content-detail* /
*form-pattern* scale, NOT at the surah-aggregate FR-cohesion scale. Compare the corpus outliers
Q 33 (+31.46), Q 1 (+27.09), Q 24 (+23.51), Q 9 (+21.57) (`h-new-590.json` top_10_outliers).

## 3. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`, surah 84)

| Field | Value | Rank |
|:--|:--|:--|
| n_verses | 25 | — |
| rhyme_entropy_nats | **1.79144** | z_rhyme_entropy = +1.850 |
| top_final_letter | ا (alif / −ā) | frac 0.24 |
| mean_content_distance | 0.82630 | z = −0.959 |
| local_cohesion | 1.63755 | z = +0.162 |
| **sig_A** | **+2.80902** | **rank 2/114** |
| **sig_B** | **+2.01204** | **rank 7/114** |

**This is the headline empirical fact about Q 84.** Its iʿjāz signature **sig_A = +2.809 ranks
2nd of 114 surahs** — among the very strongest structural-iʿjāz (*iʿjāz al-fawāṣil*, al-Bāqillānī)
profiles in the corpus. The driver is the combination of (i) **high rhyme entropy** (1.791 nats,
z=+1.85 — Q 84 is a multi-rāwī surah, cycling rhyme-letters rather than monorhyming) with (ii)
**low mean content-distance** (tight content cohesion, z=−0.959). H-NEW-750's 3-type taxonomy places
Q 84-100 in the *iʿjāz al-fawāṣil* family; Q 84 is at its apex on sig_A. The high rhyme entropy is
the signature of the **rhyme-shift architecture**: the surah moves through −aq/−at (vv 1-5),
−h/−ā (vv 6-15), −aq/−aq (vv 16-21), −ūn (vv 20-23), then back to −ā (vv 24-25) — a deliberate
cadential variegation rather than a single end-rhyme.

## 4. Unified Architectural Significance (`findings/phase-b-hypotheses/csv/h-new-840.json`, surah 84)

| Component | Value |
|:--|:--|
| UAS | **+0.92610** |
| **UAS rank** | **25 / 114** |
| abs_outlier (z|outlier|) | 0.330 |
| max_cost (max-neighbor TSP cost) | 0.06458 |
| abs_ijaz (|iʿjāz signature|) | 2.80902 |

Q 84's UAS rank (25/114) is **upper-quartile**, driven almost entirely by the iʿjāz-signature
component (abs_ijaz = 2.809, the same sig_A), since its outlier-strength (0.33) and max-neighbor
TSP-cost (0.065) are both modest. Q 84 is therefore an **iʿjāz-signature-dominant** architectural
surah: structurally significant because of its fawāṣil/rhyme-entropy profile, not because of
graph-position or outlier-strength.

## 5. Canonical-adjacency seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

| Seam | delta_raw | fraction_residual | rank (asc = cheap) |
|:--|:--|:--|:--|
| Q 83 → Q 84 (s=83) | **+0.06459** | 0.00779 | **59/113** (mid-spectrum) |
| Q 84 → Q 85 (s=84) | **+0.00691** | 0.00083 | **17/113** (near-seamless) |

The al-Muṭaffifīn → al-Inshiqāq joint (Q 83→84) is mid-spectrum; the al-Inshiqāq → al-Burūj joint
(Q 84→85) is **near-seamless** (rank 17/113, delta 0.0069) — Q 84 sits very smoothly before Q 85,
consistent with both being short eschatological-Meccan surahs sharing the *al-yawm al-ākhir* +
oath-opening register. (Corpus context: `cumulative_stats` Σdelta = 9.827, mean 0.0870, so Q 84→85
at 0.0069 is ~13× below the mean seam cost.)

## 6. Phonological / rhyme architecture

- **Predominant rāwī:** ا (−ā), top-final-letter frac only **0.24** (`h-new-750.json`) — Q 84 is NOT
  a monorhyme surah; it is among the most rhyme-variegated short surahs (entropy 1.791 nats).
- This high-entropy, multi-rāwī profile is exactly what drives the sig_A = rank-2 structural-iʿjāz
  score. Compare the near-monorhyme bottom-of-corpus surahs whose entropy is far lower.

## 7. Architectural type classification

**iʿjāz al-fawāṣil (structural-iʿjāz), signature-dominant subtype.** Q 84 is:
- NOT an outlier (H-NEW-590 Δ%ile = −0.33, NULL),
- NOT a graph-keystone (max-neighbor TSP-cost 0.065, modest),
- but a TOP-2 fawāṣil-signature surah (sig_A rank 2/114).

This matches the al-Bāqillānī *iʿjāz al-fawāṣil* axis (cadence/rhyme-cell architecture), and is
ORTHOGONAL to the al-Khaṭṭābī *iʿjāz al-maʿnā* axis. Q 84's high structural-iʿjāz coexists with its
modest UAS-graph centrality — the two are different architectural dimensions.

## 8. Compression-tail position (s = 84)

- Content law: d̄_content(84) ≈ 0.96 − 0.012·(84−50) = 0.96 − 0.408 = **0.552** predicted;
  Q 84's *observed mean FR* (0.826) is higher than the bare law-prediction because the law is the
  *windowed* d̄, not the all-pairs mean — but Q 84's nearest-neighbor distances (~0.48–0.50)
  confirm it sits in the dense tail. (The law governs local windows; see
  [[h-new-660-compression-tail-gradient]] / [[h-new-680-multi-k-compression-tail]].)
- Phoneme law kink is at s≈75; Q 84 (s=84) is past it, in the high-phoneme-dispersion zone
  ([[h-new-700-phonological-compression-tail]]).

## 9. Cross-references to H-NEW findings touching Q 84

- [[h-new-111|H-NEW-111]] — FR matrix (Q 84 mean 0.8263; nearest Q 103/108/106).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 84 COHESION member (Δ%ile −0.33, NULL).
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — Q 84 sig_A rank **2/114** (headline).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 84 UAS rank 25/114.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 84→85 near-seamless (rank 17/113).
- [[h-new-1200|H-NEW-1200]] — idhā-cosmic-opener set (Q 84 member).
- [[h-new-1330-sajda-surahs-cluster|H-NEW-1330]] / [[h-new-1510-sajda-pericope-replication|H-NEW-1510]] — sajda set (Q 84:21 pericope #14, 10 roots).
- [[h-new-2250-particle-cascade|H-NEW-2250]] — idhā-cascade juzʾ-30 marker (Q 84 in s=78-93 peak band; Limit 2 flags Q 84's grammatical fragmentation).

## 10. Honest limits

- The FR/iʿjāz metrics are root-distribution-based (QAC v0.4); the surah's distinctiveness at
  the *verse-detail* scale (k-d-ḥ anchor, biplex marker, suspended apodosis) is NOT captured by
  these surah-aggregate numbers — which is exactly why Q 84 reads as a COHESION member (Δ%ile −0.33)
  at the surah scale while carrying corpus-unique features at the verse/form scale.
- sig_A rank 2/114 is a strong claim; it rests on H-NEW-750's pre-registered signature definition
  (z(rhyme_entropy) − z(mean_content_distance) + z(local_cohesion)-style composite). The high rank
  is robust to the high-rhyme-entropy + low-content-distance combination, both independently measured.
