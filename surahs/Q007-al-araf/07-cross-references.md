---
surah: 7
surah_name_ar: الأعراف
file_type: cross-references
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE
---

# Q 7 al-Aʿrāf — Cross-References

This file maps Q 7's relationships to neighboring surahs (Q 6, Q 8), to the destruction-cycle sister surahs (Q 11, Q 26, Q 21), to the muqaṭṭaʿ letter-family clusters (ALM, ALR, ALMR), and to corpus-wide H-NEW findings.

---

## 1. Mushaf-neighbor relationships

### 1.1 Q 6 al-Anʿām → Q 7 al-Aʿrāf

| Metric | Value | Note |
|:---|---:|:---|
| Fisher-Rao distance | **0.721** | **Q 7's nearest non-self FR-neighbor (rank 1)** |
| Canonical-adjacency cost (h-new-720) | **Δ = 0.000** | **Cheapest non-trivial transition in mushaf-graph** |
| Both FR-2-opt and Nöldeke-rev-order place Q 6 → Q 7 contiguously? | YES |
| Both surahs prophet-narrative-rich? | YES (Q 6: 18 prophets named; Q 7: 7 prophet-cycle blocks) |

**Verdict**: Q 6 → Q 7 is the **content-twin transition par excellence**. al-Biqāʿī's Q 6 → Q 7 munāsaba reading is **EMPIRICALLY OPTIMAL** at law-strength.

### 1.2 Q 7 al-Aʿrāf → Q 8 al-Anfāl

| Metric | Value | Note |
|:---|---:|:---|
| Canonical-adjacency cost (h-new-720) | **Δ = 0.212** | **Top-10 most-expensive transition** (~2.6% of total residual) |
| Period transition | Late Meccan → Medinan | structural break |
| Theme transition | Prophet-narrative → battle-judicial | thematic break |

**Verdict**: Q 7 → Q 8 is a **structural discontinuity** — the right-edge of the late-Meccan ṭiwāl block. al-Biqāʿī's *munāsaba* program reads through this discontinuity by treating the "destruction-of-Pharaoh" closure of Q 7:136–137 as a pre-figuration of "destruction-of-Quraysh-disbelievers" in the Battle of Badr (Q 8); the empirical cost is significant, indicating Q 8 IS a thematic break.

---

## 2. Destruction-cycle / prophet-narrative sister surahs

### 2.1 Q 11 Hūd

- **FR distance to Q 7**: 0.764 (rank 4 of nearest neighbors).
- **Shared lattice**: `wa-ilā [tribe] akhāhum [prophet]` formula (3× in Q 11; 3× in Q 7).
- **Shared prophets**: Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb (5/7 of Q 7's prophets).
- **Difference**: Q 11 places Mūsā as PROLOGUE (v 25) before the destruction-cycle; Q 7 places Mūsā as CLIMAX (vv 103–137).
- **Q007-F-01 result**: Q 11 has corpus-MAX feature-uniformity (mean S = 1.000) on the 4-feature vector; Q 7 has 0.667.
- **Q007-F-05 result**: Q 11's restricted prophet-order (with Mūsā-prologue) is NOT a sub-sequence of Q 7's (with Mūsā-final); τ = +0.333.
- Q 11 specialist running in PARALLEL (per coordination notes); their analysis of the akhāhum-lattice should align with this finding.

### 2.2 Q 26 al-Shuʿarāʾ

- **FR distance to Q 7**: not directly computed in this run; per top-10 list, NOT in Q 7's top-10 nearest (so > 0.83).
- **Shared lattice**: NONE — Q 26 uses paired-refrain R1+R2 (Q026-F-01 CONFIRMED) instead of akhāhum-formula.
- **Shared prophets**: Mūsā, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb (6/7 of Q 7's prophets; Adam not in Q 26).
- **Plus**: Ibrāhīm (in Q 26, not in Q 7's destruction-cycle).
- **Difference**: Q 26's Mūsā opens the cycle (vv 10–68, 59 verses long). Q 26's prophet-cycles are SHORTER on the back-end (decreasing-monotone per Q026-F-01 Spearman ρ=−0.839 CONFIRMED).
- **Q007-F-01 result**: Q 26 mean S = 0.786 (rank 2/4 in the comparison set).
- **Q007-F-05 result**: Q 26's restricted prophet-order (Mūsā-front) is NOT a sub-sequence of Q 7's; τ = +0.048.
- Q 26 specialist already done (refrain-cycle CONFIRMED).

### 2.3 Q 21 al-Anbiyāʾ

- **FR distance to Q 7**: 0.824 (rank 9 of nearest neighbors).
- **Shared prophets**: Mūsā, Hārūn, Lūṭ, Nūḥ (4/7 of Q 7's; plus Ibrāhīm-cycle, Dāwūd-Sulaymān, etc.).
- **Difference**: Q 21 is a roster-style prophet-cataloguing surah (15 prophets total, often single-verse mentions); Q 7 has 7 EXTENDED prophet-narratives.
- **Q007-F-01 result**: Q 21 mean S = 0.595 (rank 4/4 in the comparison set).
- **Q007-F-05 result**: Q 21's restricted prophet-order has τ = −0.667 vs Q 7 (strong opposite-direction).

### 2.4 Q 12 Yūsuf — narrative-purity contrast

- **FR distance to Q 7**: not in Q 7's top-10 nearest, but Q 12's top-5 nearest INCLUDES Q 7 (per `Q012-yusuf/01-empirical-profile.md`).
- **Difference**: Q 12 is the ONLY single-continuous-narrative surah (Q012-F-01 CONFIRMED). Q 7 is multi-narrative-block (7 distinct prophet-cycles).
- **Both ALR-cluster-adjacent**: Q 12 is in ALR cluster (Q 10, 11, 12, 14, 15); Q 7 is in ALR-neighborhood per Q007-F-02 (rank 2 on combined ALM-ALR proximity).

---

## 3. Letter-family / muqaṭṭaʿ relationships

### 3.1 ALM cluster (Q 2, 3, 29, 30, 31, 32) — Q 7 prefix-share

- Q 7's المص shares **alif-lām-mīm prefix** with the ALM cluster.
- d(Q 7, ALM-centroid) = 0.908 (Q007-F-02).
- H-NEW-610 ALM-6 cohesion: NULL.

### 3.2 ALR cluster (Q 10, 11, 12, 14, 15) — Q 7 content-overlap

- Q 7 shares CONTENT (prophet-narrative-rich) with ALR per H-NEW-97 (4/5 PROPHET_PERSON name-class).
- d(Q 7, ALR-centroid) = 0.841 (LOWER than ALM, by 0.067).
- Q 7's top-5 FR-nearest includes Q 10 (rank 2), Q 11 (rank 4) — both ALR.

### 3.3 ALMR (Q 13 al-Raʿd) — the OTHER 4-letter muqaṭṭaʿ

- d(Q 7, Q 13) = 0.914 (mid-pack).
- Q 13's المر is the only OTHER 4-letter muqaṭṭaʿ (alif-lām-mīm-rāʾ); Q 7's المص is alif-lām-mīm-ṣād.
- Both share alif-lām-mīm prefix; Q 13 has rāʾ tail (linking to ALR), Q 7 has ṣād tail (linking to Q 38 ص).

### 3.4 Sole-letter relationships

- Q 38 ص (sole ṣād) — Q 7's tail-letter ṣād. Q 7 ↔ Q 38 distance = (not in top-10 or bottom-5 of Q 7's neighbors; mid-pack).
- Q 19 كهيعص — contains ṣād as final letter. Q 7 ↔ Q 19 = (not in top-10).

---

## 4. Eschatological-architecture sister surahs

Q 7's 3-tier eschatological architecture: **covenant (v 172) → al-Aʿrāf-third-place (vv 46–49) → mizān (vv 8–9)**.

- **Mizān** root `wzn`: also at Q 21:47, Q 23:102–103, Q 55:7–9, Q 101:6–9. Q 7's vv 8–9 use it as the FRAMING of the surah's eschatology. (Q 55 and Q 101 are eschatological short surahs.)
- **Covenant** root `mvq` / `Ax*`: Q 5:7, Q 33:7, Q 57:8 (other major covenant verses); Q 7:172 is the *primordial-covenant* verse, distinguishable by `min ẓuhūrihim dhurriyyatahum`.
- **Aʿrāf-third-place**: corpus-hapax to Q 7 (Q007-F-03 CONFIRMED).

---

## 5. Asmāʾ ḥusnā connection

Q 7:180 ("wa-li-Llāhi al-asmāʾu al-ḥusnā fa-dʿūhu bihā") is the **single most important Quranic anchor** for the 99-names doctrine. The supporting hadith (al-Tirmidhī Sunan #3507) is canonical. Q 7 is therefore one of the **canonical asmāʾ-anchor surahs** alongside Q 17:110 ("qul idʿū Allāh aw idʿū al-Raḥmān ayyan-mā tadʿū fa-lahu al-asmāʾu al-ḥusnā") and Q 20:8 / Q 59:24.

---

## 6. Sajda al-tilāwa

Q 7:206 is the **FIRST sajda al-tilāwa** (recitation-prostration) verse in mushaf-order. Total 14 sajdat al-tilāwa per al-Suyūṭī *al-Itqān* nawʿ 78. Q 7's 206-verse position-of-the-sajda is at the very-end (final verse), making it a **closing-sajda** structurally.

The other 13 sajdat al-tilāwa: Q 13:15, Q 16:50, Q 17:109, Q 19:58, Q 22:18, Q 22:77, Q 25:60, Q 27:25, Q 32:15, Q 38:24, Q 41:38, Q 53:62, Q 84:21, Q 96:19. (Q 38 is contested — some count it as required, others not; al-Suyūṭī catalogs both.)

Q 7's closing-sajda is structurally distinctive: it appears AT THE LAST VERSE, not mid-surah like most others. Q 19's sajda (v 58) and Q 96's (v 19) are mid-surah; Q 7's is end-of-surah, making the surah's recitation END in physical prostration.

---

## 7. iʿjāz typology placement

Per the dual-iʿjāz typology (cross-finding-840):
- **Structural-iʿjāz** (al-Bāqillānī iʿjāz al-fawāṣil): high UAS — Q 7 IS in top-15 (rank 11/114).
- **Theological-iʿjāz** (al-Khaṭṭābī iʿjāz al-maʿnā): high *thuluth al-Qurʾān* status, low UAS — Q 7 is NOT in this category.
- **Within structural-iʿjāz, two sub-axes**:
  - Fawāṣil-variety axis: Q 7 LOW (sig_A rank 104).
  - Outlier+adjacency axis: Q 7 SIGNIFICANT (rank 11 by UAS, top-10 expensive Q 7-Q 8 transition).

Q 7 is therefore at **structural-iʿjāz-by-OUTLIER+ADJACENCY**, in contrast to Q 55 al-Raḥmān (structural-iʿjāz-by-REFRAIN+VARIETY). They are the FR-farthest pair (Q 7-Q 55 distance = 1.292), occupying opposite poles of the structural-iʿjāz quadrant.

---

## 8. H-NEW corpus-wide finding integration

| H-NEW | Topic | Q 7 contribution |
|:---|:---|:---|
| H-NEW-90 | Kahf narrative structure (parent finding) | Q 7 reported corpus-MAX prophet-cycle parallelism z=+5.25 (parent metric); Q007-F-01 NULL on independent operationalization (4-feature vector). |
| H-NEW-97 | ALR cluster name-class | Q 7's content-axis is ALR-bias (Q007-F-02 DIRECTIONAL). |
| H-NEW-111 | Fisher-Rao distance matrix | Q 7's nearest 10: Q 6, 10, 28, 11, 40, 27, 23, 16, 21, 2. Q 7's farthest: Q 92, 97, 88, 80, 55. |
| H-NEW-590 | Outlier-strength | Q 7 NULL (Δ%ile = −3.78pp). |
| H-NEW-600 | Letter-family cohesion (full-29) | NULL. |
| H-NEW-610 | ALM-6, ALR-5 cohesion | NULL (both). |
| H-NEW-660 | Compression-tail content law | Q 7 (s=7) is in head-mushaf zone; observed mean_content_distance = 1.039 (above-law). |
| H-NEW-700 | Phonological compression-tail | Q 7 rhyme entropy 0.279 (corpus-near-minimum). |
| H-NEW-720 | Canonical-adjacency cost | Q 6→Q 7 = 0.000 (cheapest); Q 7→Q 8 = 0.212 (top-10 expensive). |
| H-NEW-750 | iʿjāz signature | Q 7 sig_A=−2.033 (rank 104), sig_B=−1.474 (rank 101). Anti-fawāṣil. |
| H-NEW-840 | Unified Architectural Score | Q 7 UAS rank **11/114**. |
| H-NEW-940 | Prophet-order conservation | Q 7 contributes to CONFIRMED H2a (Adam-Nūḥ-Hūd-Ṣāliḥ τ=1.0, p=0.001). |
| Q026-F-01 | Q 26 refrain-cycle | Q 26's lattice is paired-refrain; Q 7's lattice is akhāhum-formula. Different lattices, both empirically distinct. |

---

## 9. Cross-finding placement

- [[cross-finding-008|cross-finding-008]] — muqaṭṭaʿāt + book-reference. Q 7:1–2 (المص + kitābun unzila ilayka) FITS the pattern.
- [[cross-finding-010|cross-finding-010]] — narrative-cluster-and-letter-family. Q 7 is in the prophet-narrative cluster but with the unique 4-letter المص.
- [[cross-finding-740|cross-finding-740]] — iʿjāz-typology dual-axis. Q 7 placed at structural-iʿjāz-by-OUTLIER+ADJACENCY, FR-anti-twin of Q 55.
- [[cross-finding-840|cross-finding-840]] — UAS architecture. Q 7 rank 11.

---

## 10. Wave-1 connection (2026-04-17 architecture)

Per the 4-region architecture (cross-finding-010 / Wave-1 2026-04-17), Q 7 is in the **prophet-narrative late-Meccan ṭiwāl region** (Q 6 → Q 7 → Q 10 → Q 11 → Q 12 → Q 14 → Q 15). This region is FR-coherent (Q 6 ↔ Q 7 = 0.721 anchor; ALR cluster is the dominant feature of the region).

Q 7's specific role within the region: **the destruction-cycle entry-anchor** (the surah where the akhāhum-lattice is most-densely deployed; 3 of the 7 corpus-occurrences of the formula are in Q 7). Q 11 has another 3 occurrences; Q 29 has the 7th. Q 7 + Q 11 are the lattice-anchor pair.

---

## 11. Summary of cross-relationships

Q 7 al-Aʿrāf is structurally embedded in:
- The **late-Meccan ṭiwāl cluster** (mushaf-position 7 of 7 long surahs).
- The **prophet-narrative ALR-adjacent neighborhood** (FR-nearest neighbors are Q 6, Q 10, Q 11, Q 28).
- The **akhāhum-lattice family** (with Q 11 and Q 29).
- The **destruction-cycle parallel-pericope class** (with Q 11, Q 26, Q 21 — different lattices).
- The **structural-iʿjāz-by-OUTLIER quadrant** (UAS rank 11; FR-anti-twin of Q 55).
- The **muqaṭṭaʿāt corpus** as a **transitional 4-letter member** between ALM and ALR clusters.

Q 7's UNIQUE-IN-CORPUS properties:
- المص (corpus-unique 4-letter muqaṭṭaʿ).
- `الأعراف` substantive (corpus-hapax — Q007-F-03 CONFIRMED).
- 7-prophet sequential narrative cycle covering ~62% of the surah.
- 3-tier eschatological architecture (covenant → Aʿrāf → mizān).
- FIRST sajda al-tilāwa in mushaf-order (Q 7:206).
- Mūsā-LAST placement in destruction-cycle (vs Mūsā-prologue in Q 11/Q 26 sisters).

These six unique-in-corpus properties anchor Q 7's structural significance as the **liminal entry-point to the late-Meccan ṭiwāl prophet-narrative phase** of the mushaf.
