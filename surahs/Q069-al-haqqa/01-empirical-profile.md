---
surah: 69
surah_name_ar: الحاقة
surah_name_translit: al-Ḥāqqa
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111,590,700,720,750,840,1190,1200,1300,1301}.
---

# Q 69 al-Ḥāqqa — Empirical Architectural Profile

## 1. Headline numbers

| Metric | Value | Source / interpretation |
|:--|:--:|:--|
| Verse count | 52 | Hafs-Kufan |
| Word count (no-tashkeel) | 264 | computed |
| Letter count (no-tashkeel, sans spaces) | 1,133 | computed |
| Avg verse length (letters) | ~21.79 | mid-range |
| Avg verse length (words) | ~5.08 | short-Meccan-tail-typical |
| Top final-letter (canonical ه = ة + ه) | ه | 61.5% (32/52) per `h-new-700.json` |
| Rhyme entropy (nats) | 0.931 | LOW-MEDIAN (z = +0.291 vs corpus, leaning monorhyme) |
| Mean content distance (FR) | 0.9028 | `h-new-750.json` (slightly content-CLOSER than corpus mean 0.9234) |
| Local cohesion (window) | 1.182 | `h-new-750.json` |
| iʿjāz sig_A | +0.495 (rank 49/114) | MIDDLING al-Bāqillānī iʿjāz al-fawāṣil signal |
| iʿjāz sig_B | −0.167 (rank 62/114) | MIDDLING-LOW al-Sakkākī iqāʿ signal |
| UAS | −1.208 (rank 81/114) | LOW unified architectural significance |
| Outlier-strength Δ%ile | −1.67 pp | NULL (window {Q 66-72}; p_greater = 0.8313) |
| Q 68 → Q 69 cost | delta_raw +0.133 / fr_resid 0.016 | smooth (al-Qalam → al-Ḥāqqa) |
| Q 69 → Q 70 cost | delta_raw +0.059 / fr_resid 0.007 | **very smooth** (al-Ḥāqqa → al-Maʿārij; among smoothest mushaf transitions) |
| H-NEW-1190 cluster mushaf-rank | 1/10 | corpus-FIRST mushaf-position member |
| H-NEW-1190 cluster centrality-rank | 10/10 | LEAST-central content-fingerprint within cluster |
| H-NEW-1300 IMPV-qrA distribution | 1 segment (Q 69:19) | eschatological-record-reading pair with Q 17 |
| Nöldeke chronology rank | 38 | Early Meccan (per `data/revelation-order.csv`) |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 69's top-12 nearest in FR space (decoded from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 84 | al-Inshiqāq | 0.6749 | H-NEW-1200 idhā-cosmic-opener |
| 2 | Q 112 | al-Ikhlāṣ | 0.6788 | corpus FR-centroid rank 1 (per H-NEW-1220) |
| 3 | Q 108 | al-Kawthar | 0.6876 | H-NEW-131 short-surah hub |
| 4 | Q 106 | Quraysh | 0.6890 | short-mufaṣṣal |
| 5 | Q 105 | al-Fīl | 0.6918 | short-mufaṣṣal |
| 6 | Q 113 | al-Falaq | 0.6928 | terminal-triad |
| 7 | Q 107 | al-Māʿūn | 0.6935 | short-mufaṣṣal |
| 8 | Q 111 | al-Masad | 0.6951 | short-mufaṣṣal |
| 9 | Q 110 | al-Naṣr | 0.6978 | short-mufaṣṣal |
| 10 | Q 114 | al-Nās | 0.7012 | terminal-triad |
| 11 | Q 101 | al-Qāriʿa | 0.7012 | H-NEW-1190 co-cluster member, content-twin of Q 69 |
| 12 | Q 103 | al-ʿAṣr | 0.7013 | short-mufaṣṣal |

Q 69's FR-neighborhood is **densely concentrated on the terminal short-mufaṣṣal block** (Q 100-114). 10 of the top-12 are from Q 100-114; only Q 84 (the idhā-cosmic-opener) and Q 101 (the cluster co-member) are not from the terminal block. This is highly consistent with H-NEW-1200's finding that the eschatology meta-cluster's *sub-architectural-core* sits in the terminal-tail.

Q 69's mean dist to all 113 = **0.9028** (corpus mean 0.9234). Q 69 is **mildly content-CLOSER** than corpus-typical, ranking ~50/114 from the lowest.

Far end:
- Q 9 al-Tawba: 1.2671 (basmala-less Medinan polemic)
- Q 4 al-Nisāʾ: 1.2549 (long Medinan legal)
- Q 3 Āl ʿImrān: 1.2318 (long Medinan creedal)
- Q 2 al-Baqara: 1.1772 (long Medinan legal)
- Q 5 al-Māʾida: 1.1714 (long Medinan legal)

The far-end is the **uniformly long-Medinan-legal** corpus zone — Q 69's narrative-compressed Early-Meccan eschatology sits in maximum-content-orthogonality to the long-Medinan band.

## 3. H-NEW-1190 cluster centrality decomposition

Computed from `h-new-111.json` (10 cluster members; intra-pairwise FR distances):

| Surah | Mean FR to other 9 cluster members | Centrality rank | Mushaf rank |
|:-:|:-:|:-:|:-:|
| Q 101 | 0.5232 | **1 (most central)** | 9 |
| Q 104 | 0.5262 | 2 | 10 |
| Q 97 | 0.5562 | 3 | 8 |
| Q 86 | 0.5660 | 4 | 6 |
| Q 90 | 0.5842 | 5 | 7 |
| Q 82 | 0.5953 | 6 | 4 |
| Q 83 | 0.6487 | 7 | 5 |
| Q 77 | 0.7032 | 8 | 3 |
| Q 74 | 0.7377 | 9 | 2 |
| **Q 69** | **0.7425** | **10 (least central)** | **1 (first by mushaf)** |

**Striking pattern**: Within-cluster, mushaf-position and content-centrality are anti-correlated at Kendall τ = −0.867 (p_classical = 0.0001 single-test).

**Permutation-null caveat (Q069-F-01 test)**: random 10-surah subsets from the corpus also show strong negative mushaf-position-vs-centrality correlation (null mean τ = −0.645). The observed cluster τ = −0.867 sits at the 79.78th percentile from below — i.e. NOT corpus-distinctive.

**Interpretation**: The cluster's mushaf-vs-centrality anti-correlation reflects **surah-length confounding with both mushaf-position AND FR-distance**. Within H-NEW-1190:
- Q 69 (52v), Q 74 (56v), Q 77 (50v) — the 3 LONGER cluster members at mushaf-positions 1-3 of the cluster
- Q 82 (19v), Q 83 (36v), Q 86 (17v), Q 90 (20v), Q 97 (5v), Q 101 (11v), Q 104 (9v) — the 7 SHORTER cluster members at mushaf-positions 4-10

Longer surahs have more diverse root distributions → higher mean FR distance to anyone; mushaf-position descends with length in the short-Meccan-tail (post-Hijra-kink length-decay per H-NEW-540). The two effects co-confound to produce the observed within-cluster anti-correlation.

**Q 69's "peripheral within-cluster" status is therefore a length-effect, NOT a content-deviation**. Once length-residualized, Q 69 sits in expected position within the cluster.

This is the empirical answer to the prompt's first test: Q 69 is FIRST-by-mushaf and LEAST-central-by-FR within H-NEW-1190, but the anti-correlation is corpus-typical (length-driven), NOT cluster-distinctive. See Q069-F-01.

## 4. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json`:

| Field | Value |
|:--|:--:|
| Window | {Q 66, Q 67, Q 68, Q 69, Q 70, Q 71, Q 72} |
| d_W | 0.8546 |
| d_W − Q 69 | 0.8534 |
| Δ pp | −1.67 |
| pct_W | 16.87 |
| pct_W − Q 69 | 18.54 |
| p_greater_W | 0.8313 |
| Classification | **NULL** |

Q 69 is NOT a content-outlier in its mushaf-window. The neighborhood {Q 66-72} contains al-Mulk + al-Qalam + al-Ḥāqqa + al-Maʿārij + Nūḥ + al-Jinn + al-Muzzammil — a tightly-cohesive Early-Meccan eschatological/prophetic-call cluster, and Q 69 fits in well. This is consistent with the smooth Q 68 → Q 69 → Q 70 transitions.

## 5. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Rank |
|:--|:--:|:--:|:--:|
| Rhyme entropy (nats) | 0.931 | +0.291 | rank ~50/114 (low-end median) |
| Mean content distance | 0.9028 | −0.204 | rank 50/114 (slightly closer-than-mean) |
| Local cohesion | 1.182 | −0.459 | rank 80/114 (low local cohesion) |
| sig_A | +0.495 | — | rank 49/114 (MIDDLING) |
| sig_B | −0.167 | — | rank 62/114 (MIDDLING-LOW) |

Q 69 is MIDDLING on both iʿjāz axes — neither high-iʿjāz nor low-iʿjāz. This contrasts with the H-NEW-1190 cluster's other terminal-tail members (Q 97 al-Qadr, Q 104 al-Humaza) which sit in the LOW-sig_A band: those surahs have very-low rhyme entropy (near-monorhyme) but their short length suppresses local-cohesion. Q 69's larger size (52 verses) gives it more room for rhyme-variation across the closing oath-cluster (vv38-52 shifts from ه to ون / م), which raises sig_A relative to the 5-9-verse cluster members.

## 6. Canonical-adjacency cost (H-NEW-720)

| Boundary | delta_raw | fraction_residual | Note |
|:--|:--:|:--:|:--|
| Q 68 → Q 69 | +0.133 | 0.016 | low (al-Qalam → al-Ḥāqqa; biqāʿī takdhīb-theme bridge per Abū Jaʿfar Ibn al-Zubayr) |
| Q 69 → Q 70 | +0.059 | 0.007 | **very low** (al-Ḥāqqa → al-Maʿārij; eschatological-Day continuation) |

Both seams are well below the corpus median (0.022 fraction_residual). Q 69 → Q 70 is among the 15-20 smoothest mushaf transitions corpus-wide, though NOT in the H-NEW-720 clamped-zero set. The clamped-zero set anchors at Q 73 → Q 74 (the al-Muzzammil → al-Muddaththir near-twin pair), Q 86 → Q 87, Q 91 → Q 92, Q 93 → Q 94, etc., which are the *iconic* short-Meccan twin-pairs.

## 7. UAS decomposition (H-NEW-840)

From `h-new-840.json`:

| Component | Value |
|:--|:--:|
| UAS | −1.208 |
| abs(outlier-strength) | 1.67 |
| max canonical-adjacency cost (entering or leaving Q 69) | 0.133 |
| abs(iʿjāz signature) | 0.495 |
| UAS rank | 81/114 |

Q 69's UAS rank 81/114 is LOW — not a top-15 architectural anchor. Compare:
- Q 33 al-Aḥzāb: UAS = +9.36 (rank 1) — the Prophet's-household legal-architectural hub
- Q 24 al-Nūr: UAS rank ~3 — Nūr-light + legal-architectural twin of Q 33
- Q 1 al-Fātiḥa: UAS rank ~5 — sui-generis liturgical opener
- Q 56 al-Wāqiʿa: UAS rank low-mid, but H-NEW-91 length-controlled outlier
- Q 69 al-Ḥāqqa: UAS rank 81 — **architecturally typical of mid-Early-Meccan eschatology surahs**

The UAS placement is consistent with Q 69 being a *structurally-typical* member of the H-NEW-1190 / H-NEW-1200 eschatology cluster — Q 69's distinctiveness lies NOT in surah-aggregate architecture but in **rhetorical-pattern membership** (the *wa-mā adrāka mā* opener and the *iqraʾū kitābiyah* eschatological imperative).

## 8. H-NEW-1300 IMPV-qrA inventory placement

Q 69:19 contains 1 segment of corpus-IMPV-qrA (out of 6 total corpus-wide). The 6 segments distribute as:
- Q 17:14 — 1 segment (eschatological-pair anchor)
- Q 69:19 — 1 segment (eschatological-pair partner) ← **Q 69's slot**
- Q 73:20 — 2 segments within ONE long verse (recitation-imperative ×2)
- Q 96:1, 96:3 — 2 segments (prophetic-call ×2)

Q 69:19 sits in the "eschatological-record-reading" pair with Q 17:14 (and a stronger architectural-twin Q 17:71 via indicative *yaqraʾūna* — see Q069-F-02).

The H-NEW-1301 follow-up test on the IMPV-qrA cluster's FR-cohesion was NULL-BROKEN (positive control failed) and substantively NULL on both cells — the 4-surah inventory does not form a tight FR cluster on root-distribution. **Q069-F-02 takes a different approach**: instead of testing surah-aggregate cluster cohesion, it tests **verse-pair Jaccard at the QAC-root level** for the Q 17:14 ↔ Q 69:19 pair specifically.

## 9. Architectural type classification

| Axis | Q 69 placement |
|:--|:--|
| Length class | mid-Early-Meccan (n=52, mid-Meccan-mufaṣṣal) |
| Compression-tail position | s=69 > kink-50, INSIDE compression-tail regime |
| iʿjāz typology | MIDDLING on both fawāṣil and iqāʿ axes |
| FR neighborhood | **terminal short-mufaṣṣal block** (Q 100-114 cluster + Q 84 idhā-twin) |
| Outlier-strength | NULL (well-fitted in mushaf-window) |
| Cluster memberships | (1) **H-NEW-1190 *wa-mā adrāka mā* (mushaf-rank 1, centrality-rank 10)**; (2) H-NEW-1200 14-surah eschatology meta-cluster; (3) H-NEW-1300 IMPV-qrA inventory (1 segment, eschatological-record-reading pair) |
| Adjacency role | smooth LEFT seam (Q 68 →); VERY smooth RIGHT seam (→ Q 70) |
| Architectural axis (cluster-internal) | **first mushaf-position trigger** of the *wa-mā adrāka mā* meta-question network — the rhetorical-pattern initiator |

**Architectural verdict**: Q 69 is the **mushaf-FIRST trigger of the Early-Meccan *wa-mā adrāka mā* eschatology cluster**. Its surah-aggregate architecture is corpus-typical (UAS rank 81); its distinctiveness is in initiating a rhetorical pattern (the *adrāka* meta-question) that recurs 9 more times across Q 74-104, AND in carrying the corpus-MIN ʿĀd/Thamūd narrative compression (3 verses, 14 words), AND in carrying one of the 6 IMPV-qrA segments (Q 69:19's eschatological-record-reading imperative).

The surah's **role in the corpus architecture** is not at the surah-aggregate FR level (where it sits typically with the short-mufaṣṣal cluster) but at the **rhetorical-network-trigger level** — Q 69 is the first node in the 10-surah *wa-mā adrāka mā* network and one of two "eschatological IMPV-qrA" verse-twin anchors.

## 10. Cross-references

- [[h-new-111-fisher-rao-mushaf]] — Q 69 FR matrix row.
- [[h-new-590-outlier-spectrum]] — Q 69 NULL outlier on Q 66-72 window.
- [[h-new-700-phonological-compression-tail]] — Q 69 ه-rhyme dominant (61.5%).
- [[h-new-720-canonical-adjacency-cost]] — Q 68 → Q 69 → Q 70 both well below median.
- [[h-new-750-ijaz-signature]] — Q 69 MIDDLING on both axes.
- [[h-new-840-unified-architectural-score]] — Q 69 UAS rank 81/114.
- [[h-new-1190-wa-ma-adraka-cluster]] — Q 69 = mushaf-rank 1, centrality-rank 10.
- [[h-new-1200-short-meccan-eschatology]] — Q 69 in 14-surah eschatology meta-cluster.
- [[h-new-1300-q96-iqra-corpus-distribution]] — Q 69:19 = 1 of 6 IMPV-qrA segments.
- [[h-new-1301-impv-qra-cluster]] — Q 17 ↔ Q 69 eschatological-record-reading pair (verse-twin Q069-F-02).
- `surahs/Q017-al-isra/` — verse-twin partner via Q 17:14 + Q 17:71.
- `surahs/Q068-al-qalam/` (mushaf left-neighbor; not yet specialized).
- `surahs/Q070-al-maarij/` (mushaf right-neighbor; not yet specialized).
- `surahs/Q089-al-fajr/` — ʿĀd+Thamūd compression-tier-2 comparator (Q069-F-03).
