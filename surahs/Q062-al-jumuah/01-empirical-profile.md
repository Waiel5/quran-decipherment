---
surah: 62
surah_name_ar: الجمعة
surah_name_translit: al-Jumuʿah
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{89, 95, 111, 112, 340, 400, 590, 700, 720, 750, 840}.
---

# Q 62 al-Jumuʿah — Empirical Architectural Profile

## 1. Headline numbers

| Metric | Value | Source / interpretation |
|:--|:--:|:--|
| Verse count | 11 | Hafs-Kūfan |
| Word count (no-tashkeel) | 184 | computed |
| Letter count (no-tashkeel) | 778 | computed |
| Avg verse length (words) | 16.7 | medium-Medinan didactic |
| Top final letter | ن | 72.7% (`h-new-700.json` rhyme_letter_diagnostics surah=62) |
| Rhyme entropy (nats) | 0.586 | z = −0.33 (moderate near-monorhyme) |
| Mean content distance (FR) | 0.8380 | z = −0.84 (`h-new-750.json` surah=62) — content-CLOSE |
| Local cohesion (window) | 1.3399 | z = −0.24 |
| iʿjāz sig_A | +0.511 (rank 48/114) | middle-pack al-Bāqillānī iʿjāz al-fawāṣil |
| iʿjāz sig_B | −0.576 (rank 68/114) | slightly below middle al-Sakkākī iqāʿ |
| UAS | −1.759 (rank 95/114) | LOW unified architectural significance |
| Outlier-strength Δ_pp | −1.82 pp | NULL (window {Q 59-65}; p_greater = 0.9444) |
| Q 61→Q 62 cost (delta_raw) | +0.0704 / fraction 0.0085 | low — Ṣaff→Jumuʿa smooth |
| Q 62→Q 63 cost (delta_raw) | +0.0038 / **fraction 0.0005** | **near-seamless seam** (rank ~2/113 cheapest) |
| FR-rank-1 nearest surah | **Q 112 al-Ikhlāṣ at d = 0.6160** | corpus's primary FR neighbor |
| 4-cluster degree (H-NEW-89) | **4 (unique pre-dedup; 4-way tie post-dedup with Q 112/113/114)** | musabbiḥāt + Friday + Khawātim-extended + mufaṣṣal |
| Spectral v_2 (H-NEW-112) | 0.0682 (rank 109/114 asc) | **back-Medinan community PEAK** |
| Cluster-network weighted degree | 73.0 / 21 neighbors | (h-new-112.json) |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 62's top-10 nearest in FR space (computed from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 112 | al-Ikhlāṣ | **0.6160** | corpus-anchor unique-FR-pull; refines audit-035 |
| 2 | Q 110 | al-Naṣr | 0.6353 | post-conquest 3-verse; semantic-sister |
| 3 | Q 95 | al-Tīn | 0.6496 | oath-cluster + brief-cosmic |
| 4 | Q 1  | al-Fātiḥa | 0.6500 | Q 1's own FR-rank-1 nearest is Q 108; Q 62 is in Q 1's top-10 |
| 5 | Q 114 | al-Nās | 0.6560 | Muʿawwidhatān terminal |
| 6 | Q 108 | al-Kawthar | 0.6573 | Q 1's own rank-1 neighbor (3-verse miniature) |
| 7 | Q 91 | al-Shams | 0.6585 | 7-oath cosmic |
| 8 | Q 102 | al-Takāthur | 0.6603 | terminal-tail brief polemic |
| 9 | Q 107 | al-Māʿūn | 0.6698 | terminal-tail communal-ethics brief |
| 10 | Q 111 | al-Masad | 0.6738 | terminal-tail (Abū Lahab denunciation) |

**Q 62's FR-neighborhood is dominated by terminal-mufaṣṣal short surahs.** This is empirically striking and not predicted by the cluster-network framing: although Q 62 is a 184-word Medinan didactic, its Fisher-Rao content geometry pulls toward the 3-7-verse terminal-tail block (Q 95-114). Out of 113 candidate neighbors, 8 of Q 62's top-10 are post-Q 90; only Q 1 (rank 4) and effectively no top-10 surah comes from the mid-mushaf or the short-surah Meccan-Mecca-blessing zone (no Q 36, 67, 78). **Q 62's mean FR distance to {Q 112, 113, 114} = 0.652** vs Q 62's overall corpus-mean **0.838** — Q 62 IS preferentially close to the terminal triad.

But the within-{Q 112, 113, 114} mean is **0.290** (the triad is itself extremely tight), so Q 62 is **2.25× more distant from the triad than the triad is internally** (Q062-F-02).

**Architectural interpretation**: Q 62 sits at the *edge* of the terminal-tail FR-cluster basin, NOT inside it. Its mid-Medinan-back mushaf placement places it administratively in the musabbiḥāt-block, but its content-fingerprint reaches into the terminal-tail. The 4-way cluster-degree tie {Q 62, 112, 113, 114} is **STRUCTURAL-CLUSTER-DEGREE in the 18-cluster taxonomy, NOT FR-content cluster co-membership** — refining the audit-035 reading (Q062-F-02 confirmed-partial verdict).

Far end (Q 62's FR-FARTHEST):
- Q 55 al-Raḥmān: 1.166 (the 31-refrain *ʿarūs al-Qurʾān* anti-twin)
- Q 9 al-Tawba: 1.093 (basmala-less Medinan polemic)
- Q 26 al-Shuʿarāʾ: 1.089 (long oath-prophet-cycle Meccan)
- Q 4 al-Nisāʾ: 1.054 (long Medinan legal)
- Q 3 Āl ʿImrān: 1.046 (long Medinan with ālm and Khawātim-source-zone)

## 3. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json` (X=62):

| Field | Value |
|:--|:--:|
| Window | {Q 59, 60, 61, 62, 63, 64, 65} |
| d_W (window mean dist) | 0.776 |
| d_W − Q 62 | 0.777 |
| Δ pp | **−1.82** |
| pct_W | 5.56 |
| pct_W − Q 62 | 7.38 |
| p_greater_W | 0.9444 |
| Classification | **NULL** |

**Q 62 is NOT a content outlier**; in fact removing Q 62 SLIGHTLY WORSENS the window cohesion (+1.82pp dispersion). This empirically replicates **H-NEW-400** (Q 62 is a cohesion-EXEMPLAR of the musabbiḥāt-block, not a disruptor — distinguishing it from Q 55's +32.6pp outlier-disruption). The classical "4-cluster meta-hub" designation captures *liturgical prominence* via Friday-prayer institution, NOT content-axis uniqueness.

## 4. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Rank |
|:--|:--:|:--:|:--:|
| Rhyme entropy (nats) | 0.586 | −0.333 | (moderate-low entropy = moderate-near-monorhyme) |
| Mean content distance | 0.838 | −0.843 | (notably content-CLOSE) |
| Local cohesion | 1.340 | −0.243 | (slightly below middle) |
| sig_A (al-Bāqillānī iʿjāz al-fawāṣil) | +0.511 | — | rank 48/114 (middle-pack) |
| sig_B (al-Sakkākī iqāʿ) | −0.576 | — | rank 68/114 (slightly below middle) |

Q 62 is **middle-pack on both iʿjāz axes**. This is consistent with its UAS-low status (rank 95/114) and outlier-NULL classification. Q 62 is structurally distinguished by **liturgical-cluster-degree** (cross-finding-009 / H-NEW-89) and **Khawātim-echo composite quotation** (Q062-F-01), NOT by iʿjāz al-fawāṣil dominance. This contrasts with Q 14 Ibrāhīm (sig_A rank 14/114 top-15) and Q 55 al-Raḥmān (sig_A rank 114/114 corpus-MIN refrain-driven outlier).

## 5. Canonical-adjacency cost (H-NEW-720)

| Boundary | delta_raw | fraction_residual | Note |
|:--|:--:|:--:|:--|
| Q 61 → Q 62 | +0.0704 | 0.0085 | low — Ṣaff→Jumuʿa smooth (perfect→imperfect musabbiḥāt boundary) |
| Q 62 → Q 63 | **+0.0038** | **0.0005** | **near-seamless** — anchor of the classical Q 62+Q 63 Friday-Ẓuhr recitation pair |
| Q 63 → Q 64 | (per h-new-720) | (low) | Munāfiqūn → Taghābun musabbiḥāt-imperfect re-entry |

The **Q 62 → Q 63 fraction-residual = 0.0005** ranks among the cheapest seams in the entire mushaf — empirically validating the al-Biqāʿī *Naẓm al-Durar* munāsabah claim that Q 62 (cosmic-glorification + Friday institution) flows directly into Q 63 al-Munāfiqūn (denouncing the hypocrites *who fled the Friday assembly* per Q 62:11 asbāb-ul-nuzūl). The two surahs are **structurally adjacent at the content-fingerprint level** to a degree exceeded by only ~10 surah-pairs corpus-wide.

## 6. H-NEW-89 META-cluster degree

Q 62's pre-dedup degree-4 hub status (`findings/phase-b-hypotheses/csv/h-new-89.json` observed.degree_by_surah["62"] = 4):

| Cluster system | Members | Q 62 inclusion |
|:--|:--|:-:|
| C5_musabbiḥāt | {Q 57, 59, 61, **62**, 64} | ✓ |
| C7_Friday | {Q 18, 32, **62**, 76} | ✓ |
| C8_Khawātim_extended | {Q 59, **62**} | ✓ |
| C11_mufaṣṣal | {Q 49, ..., **62**, ..., 114} | ✓ |

**Q 62 is the unique pre-dedup degree-4 hub.** Under audit-035 dedup (cluster-system definitions overlap at ~20% rate), the degree-4 status becomes a 4-way TIE with {Q 112, Q 113, Q 114}. Q062-F-02 surfaces that this 4-way tie is structural-cluster-degree co-membership in the 18-cluster taxonomy, NOT FR-content cluster co-membership.

## 7. H-NEW-112 spectral profile

Q 62's spectral characterization (`findings/phase-b-hypotheses/csv/h-new-112.json` `Q62_characterization`):

| Field | Value |
|:--|:-:|
| v_2 (Fiedler) | 0.0682 |
| Rank ascending | 109 / 114 |
| Sign | + |
| Community assignment | 3 (back-Medinan) |
| Weighted degree | 73.0 |
| Number of neighbors | 21 |

**Q 62 is the BACK-MEDINAN community PEAK in the cluster-network graph** — the spectral *centroid* of community-3, NOT a connecting bridge. v_2 = 0.0682 places Q 62 at rank 109/114 ascending — only 5 surahs are higher in the Fiedler-positive band, and Q 62's weighted degree 73.0 makes it the heaviest-degree node in community-3. The 21 cluster-network neighbors include Q 18 + Q 32 (Friday-cluster cousins), Q 49-67 (mufaṣṣal-ṭiwāl band), and the closest Khawātim-extended partner Q 59 (weight 3 — the strongest single-edge in Q 62's neighborhood, reflecting joint-membership in both C5 and C8).

H-NEW-112 verdict: **1 of 2 inferential cells PASS at α_bon = 0.025**. Cell-2 (Fiedler community-structure) PASSES p = 0.004 via length; Cell-1 (25-component topology mismatch) NULL. The audit-035 amendment tightened k=3 → k=2 mid-flight (self-verifying Bonferroni-tightening per project asymmetry rule).

**Spectral interpretation**: cross-finding-009's "Q 62 as 4-cluster meta-hub" framing is REFINED to "Q 62 as back-Medinan community NUCLEUS" — not a bridge, but the centroid of the back-Medinan cluster-graph community.

## 8. Architectural type classification

| Axis | Q 62 placement |
|:--|:--|
| Length class | medium-Medinan-back (n=11 verses, 184 words; middle of mufaṣṣal-ṭiwāl Q 49-77) |
| Compression-tail position | s=62 > kink-50, INSIDE compression-tail regime (laws apply) |
| iʿjāz typology | MIDDLE on both fawāṣil and iqāʿ axes |
| FR neighborhood | TERMINAL-TAIL pulled (Q 112, 110, 95, 1, 114, 108, 91, 102, 107, 111 all top-10) |
| Outlier-strength | NULL (cohesion-exemplar) |
| Cluster memberships | (1) musabbiḥāt-imperfect-pair with Q 64 (H-NEW-58c); (2) C7_Friday liturgical-cluster (4-surah {Q 18, 32, 62, 76}); (3) Khawātim-extended (Q 59 + Q 62, H-NEW-95); (4) mufaṣṣal (66-surah Q 49-114) |
| Adjacency role | smooth LEFT (Q 61→), near-seamless RIGHT (→Q 63 fraction-residual 0.0005) |
| Spectral role | back-Medinan community PEAK (v_2 rank 109/114; H-NEW-112) |

**Architectural verdict**: Q 62 is the **structural NUCLEUS of the back-Medinan liturgical-cluster community**, with content-fingerprint that paradoxically pulls toward the terminal-mufaṣṣal qiṣār-tail. It is the unique 4-cluster meta-hub by classical-grouping count, the back-Medinan spectral peak by graph-Laplacian analysis, and the canonical Friday-recitation eponym. Its content-fingerprint is mainstream (UAS rank 95, outlier NULL), making it a **cluster-structural-prominent but content-mainstream surah** — a rare combined typology.

## 9. Cross-references

- [[h-new-89-meta-cluster-network|H-NEW-89]] — Q 62 unique pre-dedup degree-4 hub.
- [[h-new-95-khawatim-extension|H-NEW-95]] — Q 62:1 4-name composite Khawātim-echo.
- [[h-new-111-fisher-rao-mushaf]] — Q 62 FR-rank-1 nearest = Q 112 al-Ikhlāṣ at d=0.6160.
- [[h-new-112-spectral-network|H-NEW-112]] — Q 62 back-Medinan community spectral peak.
- [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] — Q 62 imperfect-tense pair with Q 64.
- [[h-new-340-musabbihat-block-subset|H-NEW-340]] — {Q 57, 59, 61, 62, 64} 8.1%ile most-cohesive classical grouping tested.
- [[h-new-400-q62-outlier-candidate|H-NEW-400]] — Q 62 NOT outlier (cohesion-exemplar).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 62 Δ_pp = −1.82 NULL.
- [[h-new-700-phonological-compression-tail]] — Q 62 ن-rhyme 72.7%.
- [[h-new-720-canonical-adjacency-cost]] — Q 62→Q 63 fraction-residual 0.0005.
- [[h-new-750-ijaz-signature]] — Q 62 sig_A rank 48, sig_B rank 68 (middle-pack).
- [[h-new-840-unified-architectural-score]] — Q 62 UAS rank 95/114.
- [[cross-finding-009-meta-cluster-network]] — Q 62 4-cluster meta-hub.
- [[cross-finding-010-extended-network]] — audit-035 dedup 4-way tie {Q 62, 112, 113, 114}.
- `surahs/Q063-al-munafiqun/` — adjacency partner; classical Q 62 + Q 63 Friday-Ẓuhr pair.
- `surahs/Q064-al-taghabun/` — H-NEW-58c imperfect-pair partner.
- `surahs/Q059-al-hashr/` — Khawātim-source surah.
