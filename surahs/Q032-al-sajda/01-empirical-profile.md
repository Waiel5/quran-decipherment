---
surah: 32
surah_name_ar: السجدة
surah_name_translit: al-Sajda
file_type: empirical-profile
date_last_updated: 2026-05-10
phase: B+
---

# Q 32 al-Sajda — Empirical Profile

## 1. Headline architectural signature

| Metric | Q 32 value | Rank / interpretation | Source |
|:--|:--|:--|:--|
| UAS (Unified Architectural Significance) | 0.7522 | rank 27/114 (top-quartile structural-iʿjāz) | `findings/phase-b-hypotheses/csv/h-new-840.json` |
| Outlier-strength Δ%ile | −1.36 | NULL classification, window {Q 29..35} | `h-new-590.json` |
| iʿjāz sig_A | −0.350 | rank 70 (mild theological-iʿjāz lean) | `h-new-750.json` |
| iʿjāz sig_B | −1.322 | rank 95 (rhyme-axis suppressed) | `h-new-750.json` |
| Mean FR content distance d̄ | 0.8890 | below corpus mean 0.9235 | `h-new-750.json` |
| Local cohesion | 1.0546 | mid-quartile | `h-new-750.json` |
| Rhyme entropy (nats) | 0.389 | z = −0.690 (near-monorhyme) | `h-new-750.json` |
| Top rāwī | ن (≈ 90%) | dominant nūn-rhyme | `h-new-750.json` |
| Words (no-tashkeel) | 378 | mufaṣṣal-ṭiwāl / awsāṭ boundary | computed |
| Verses | 30 | matches Q 67 al-Mulk verse-count exactly | `data/hafs-verse-counts.tsv` |

## 2. Canonical-adjacency costs

| Seam | TSP cost δ | Rank | Interpretation | Source |
|:--|:--:|:--:|:--|:--|
| Q 31 → Q 32 | 0.1005 | mid-pack | structurally continuous (ALM → ALM) | `h-new-720.json` |
| Q 32 → Q 33 | **0.3631** | **rank 3** | TOP-3 expensive seam corpus-wide (4.4% of L_mushaf) | `h-new-720.json` |

The Q 32 → Q 33 break is one of the project's three documented major structural breaks (after Q 1 → Q 2 at 7.4% of L_mushaf). al-Biqāʿī (*Naẓm al-Durar*) reads the Q 32 → Q 33 transition as a deliberate thematic-pivot from the *cosmic-tanzīl* of Q 32 to the *prophetic-personal-address* of Q 33 — the empirical break vindicates the al-Biqāʿī reading.

## 3. Fisher-Rao neighborhood

From `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`, Q 32's nearest 10 FR-neighbors (in QAC stem-root distribution):

| Rank | Neighbor | FR distance | Cluster anchor |
|:--:|:--:|:--:|:--|
| 1 | Q 67 al-Mulk | 0.7534 | al-Munjiya nightly pair (Tirmidhī #2975) |
| 2 | Q 41 Fuṣṣilat | 0.7684 | ḤM-7 muqaṭṭaʿāt cluster member (post-Hijra theological) |
| 3 | Q 76 al-Insān | 0.8395 | Friday-fajr pair (Bukhārī #870/#1037) |
| 4 | Q 19 Maryam | (close) | prophet-history register |
| 5 | Q 35 Fāṭir | (close) | late-Meccan ālāʾ-cluster |
| ... | ... | ... | ... |

Top-3 are NOT mushaf-adjacent (Q 31 and Q 33 are not in top-3). The two liturgical-pair partners Q 67 and Q 76 are FR-#1 and FR-#3 respectively — direct empirical anchor for cross-finding-028.

## 4. Architectural type classification

**Structural-iʿjāz (top-quartile) + nightly-liturgy + Friday-liturgy anchor + structural-break terminus.**

- UAS rank 27 places Q 32 above the median in iʿjāz al-fawāṣil scoring but not in the top-10 group.
- The dual-liturgical anchoring (FR-#1 = Q 67 nightly partner; FR-#3 = Q 76 Friday-fajr partner) is corpus-unique: no other surah is dual-paired in both nightly and Friday-fajr practice.
- The Q 32 → Q 33 structural break makes Q 32 the *terminus* of the mid-Meccan ALM block before the Medinan-Aḥzāb cycle begins.

## 5. Compression-tail position

Per H-NEW-660 compression-tail law: d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50). Q 32 sits BELOW s=50 → predicted d̄ ≈ 0.96 (head-cohort plateau). **Observed d̄ = 0.889 (below the prediction by ~0.07).** Q 32 is modestly more content-cohesive than the head-cohort plateau — consistent with its tight liturgical FR neighborhood.

## 6. Compression-tail rhyme law

Per H-NEW-700 rhyme-dispersion-tail: d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50). Q 32 → predicted d̄_rhyme ≈ 0.36 (pre-Hijra-kink baseline). **Observed rhyme-entropy z = −0.69 (rank 91+/114)** — Q 32's monorhyme ن-pattern places it BELOW the rhyme-dispersion baseline, consistent with the prediction direction but with substantial individual-surah variance.

## 7. Cross-finding integration

| H-NEW finding / cross-finding | Q 32's role | Verdict for Q 32 |
|:--|:--|:--|
| H-NEW-111 (Fisher-Rao mushaf-order) | dual-anchor for cross-finding-028 | CONFIRMED via cross-finding-028 |
| H-NEW-590 (outlier spectrum) | NULL classification, in-window | not a content outlier |
| H-NEW-660 (compression-tail) | head-cohort plateau member (below s=50) | slightly more cohesive than predicted |
| H-NEW-700 (rhyme-tail) | pre-Hijra monorhyme baseline | confirmed direction |
| H-NEW-720 (canonical-adjacency cost) | Q 32→Q 33 rank-3 expensive | CONFIRMED structural break |
| H-NEW-750 (iʿjāz signature) | sig_A −0.35; sig_B −1.32 | rhyme-suppressed; mild theological lean |
| H-NEW-840 (UAS) | rank 27/114 | top-quartile structural-iʿjāz |
| cross-finding-008 (muqaṭṭāʿat introduction-markers) | ALM-opener | consistent with muqaṭṭāʿat-as-marker function |
| cross-finding-025 (marker-thickness rule) | ALM-4 fails FR-cohesion despite 4 shared features | replicates Cell B-cohesion-not-achievable-from-shared-letters |
| cross-finding-028 (liturgical-pair FR-cohesion) | P2 + P6 anchor | CONFIRMED at aggregate scale; PARTIAL on strict per-pair 1σ |
| Q022-F-01 (cosmic-sajda cluster) | Q 32:15 NOT in cosmic cluster | refines sajda-typology |

## 8. Honest interpretation

Q 32's empirical signature is **moderate-to-strong but not extreme** on any single axis:
- UAS rank 27 (not top-10).
- d̄_content 0.889 (below corpus mean, but not below 0.85).
- Rhyme monolithic (predictable for short Meccan with ن-rāwī).

What makes Q 32 architecturally distinguished is the **conjunction of three signatures**: dual-liturgical anchor + rank-3 structural break + ALM-cluster terminus. No other corpus surah carries all three.

## 9. Honest limits

- The "dual-liturgical anchor" status depends on hadith-corpus completeness; only the al-Bukhārī (Friday-fajr) and al-Tirmidhī (al-Munjiya) attestations are tested. Other surahs may have hadith-attested liturgical pairings that are simply less well-documented.
- The Q 32 → Q 33 structural break is one of three; the other two (Q 1 → Q 2; one more between Q 33 → Q 34 per `h-new-720.json`) are even more extreme. Q 32's break is part of a small set, not a unique feature.
- The FR-#1 neighbor (Q 67) being the al-Munjiya partner is a strong signal; however the partner-prediction is post-hoc relative to H-NEW-111 (which was direction-locked to mushaf-order, not pair-prediction). The pair-cohesion is captured at the cross-finding-028 aggregate level.
