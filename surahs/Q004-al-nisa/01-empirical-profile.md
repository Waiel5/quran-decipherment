---
surah: 4
surah_name_ar: النساء
surah_name_translit: al-Nisāʾ
file_type: empirical-profile
date_last_updated: 2026-05-29
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -720 / -750 / -840 (all values cited to path)
---

# Q 4 al-Nisāʾ — Empirical Profile

All values below are read directly from the on-disk artifacts. No value is asserted from memory. Q 4 is
surah-id 4; in the 1-indexed Fisher-Rao matrix it is index 4; in the 0-indexed phoneme vector list
(`h-new-700.json` → phoneme.phoneme_vectors) it is index 3.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`, 6441 pairs),
1-indexed surah IDs. Corpus matrix stats: min 0.2127, max 1.5509, mean 0.9235, median 0.9567.

| Quantity | Value |
|:--|:--|
| Q 4 mean FR to all 113 surahs | **1.1375** (well ABOVE corpus mean 0.9235 — long surah, FR-distant) |
| Nearest neighbour | **Q 2 al-Baqara** at FR 0.7546 |
| Top-8 FR neighbours | Q 2 (0.755), Q 5 (0.778), Q 3 (0.793), Q 33 (0.837), Q 9 (0.842), Q 24 (0.904), Q 8 (0.907), Q 48 (0.912) |
| 5 farthest | Q 54 (1.331), Q 77 (1.336), Q 89 (1.339), Q 56 (1.346), Q 55 (1.551) |
| Q 3 (prev) rank in Q 4's FR list | 3/113 (FR 0.7931) |
| Q 5 (next) rank in Q 4's FR list | 2/113 (FR 0.7784) |

**Reading.** Q 4's FR neighbourhood is the long-Medinan-legal cluster: Q 2, Q 5, Q 3, then the women's/social
surahs Q 33 al-Aḥzāb and Q 24 al-Nūr, then Q 9 al-Tawba. This is the empirical signature of a legal-social
surah — its nearest neighbours after the al-ṭiwāl head are the two great women's/household surahs (Q 33, Q 24),
not the narrative or eschatological surahs. The 5 farthest are short Meccan oath surahs (Q 54 al-Qamar, Q 77
al-Mursalāt, Q 89 al-Fajr, Q 56 al-Wāqiʿa) + the FR-isolate Q 55 al-Raḥmān (corpus-farthest at 1.551).

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

| Quantity | Value |
|:--|:--|
| Window (centered on Q 4) | {Q 1, 2, 3, 4, 5, 6, 7} |
| d̄_W (window with Q 4) | 0.9154 |
| d̄_W−X (window without Q 4) | 0.9126 |
| pct_W | 37.9 |
| pct_W−X | 36.82 |
| **delta_pct** | **+1.08** |
| **classification** | **WEAK_OUTLIER** |

**Reading.** Removing Q 4 from the {Q1-7} window barely changes its dispersion (delta_pct +1.08) — Q 4 is a
WEAK_OUTLIER (a near-neutral member). It is neither a strong cohesion-binder (like Q 3 at −15.28) nor a strong
outlier (like Q 1 at +27.09): Q 4 sits comfortably inside the long-surah head, slightly raising its dispersion
when present. This is consistent with its FR profile (3rd-nearest to Q 3, 2nd-nearest to Q 5 — an interior
member) and its doubly-seamless seams.

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, Q 4): top final-letter **ا (alif)**, fraction **0.9602** (169/176 verses)
— a near-monorhyme. This is the defining empirical signature of al-Nisāʾ. Among all *al-sabʿ al-ṭiwāl*
{2,3,4,5,6,7,9}, Q 4 is the ONLY alif-dominant surah; the other six are nūn-dominant (Q004-F-06 Arm A). Among
≥100-verse surahs, Q 4's 96.0% concentration is rank 4 (behind Q 17 at 99.1%, Q 18 at 99.1%, Q 23 at 96.6%).
Project rhyme dispersion-tail law is two-piece-kink-50 (primary_r2 = 0.7886); Q 4 (s=4 < 50) is before the
rhyme kink, in the tight-rhyme regime.

**Phoneme** (phoneme_vectors index 3, 4-dim density vector):
`[0.02039, 0.03674, 0.03435, 0.11070]`. Project phoneme dispersion-tail law is two-piece-kink-75
(primary_r2 = 0.9457); Q 4 (s=4 < 75) is in the low-dispersion regime. The 4th component (0.1107) is by far
the largest.

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order,
Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 4:

| Field | Value |
|:--|:--|
| n_verses | 176 |
| rhyme_entropy_nats | **0.1989** (very low — near-monorhyme) |
| top_final_letter | ا |
| top_final_letter_frac | 0.9602 |
| mean_content_distance | 1.1375 |
| local_cohesion | 1.2033 |
| z_rhyme_entropy | **−1.0339** (far below average — suppressed fawāṣil variety) |
| z_mean_content_distance | **+2.1124** (most-FR-distant tier) |
| z_local_cohesion | −0.4291 |
| **sig_A** | **−3.1463** (rank **113 / 114** — second-lowest) |
| **sig_B** | **−1.4630** (rank **100 / 114**) |

**Reading.** Q 4 is an al-Bāqillānī *iʿjāz al-fawāṣil* MINIMUM: its rhyme entropy is 0.199 nats (z = −1.03),
because 96% of its verses end in the same letter. Combined with the most-extreme content-distance tier
(z = +2.11), sig_A collapses to **rank 113/114** — only one surah scores lower on the fawāṣil-variety axis.
This is the empirically-grounded refinement of al-Bāqillānī: al-Nisāʾ's iʿjāz, whatever its nature, is NOT in
verse-ending variety — it is a deliberate near-monorhyme legal surah.

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

| Seam | delta_raw | ascending-rank | class |
|:--|:--|:--|:--|
| **Q 3 → Q 4** | **−0.04662** | **4 / 113** | **seamless** |
| **Q 4 → Q 5** | **−0.06571** | **2 / 113** | **seamless** (one of the 2 smoothest joints in the muṣḥaf) |

Q 4 is entered AND exited via seamless seams — a **doubly-seamless interior member** of the al-ṭiwāl head.
Q 4 → Q 5 (delta_raw −0.0657) is the **2nd-smoothest seam in the entire corpus** (only one joint is smoother).
For contrast, the corpus's most expensive seam is Q 1 → Q 2 (+0.622). The block {Q2,Q3,Q4,Q5} is the rank-1
smoothest contiguous 4-surah block in the muṣḥaf (Q003-F-01 Arm A). **Classical correlate:** al-Rāzī/al-Biqāʿī's
munāsaba for the al-ṭiwāl head — the shared Medinan legal-creedal-social vocabulary makes the Q 3-Q 4-Q 5 run
adjacency-cheap.

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method: `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **+0.8778** (rank **26 / 114**) |
| abs_outlier | 1.08 (from H-NEW-590 delta_pct magnitude — small) |
| max_cost | **0.00000** (BOTH Q 4 seams are negative, so the max neighbour cost clamps to 0) |
| abs_ijaz | **3.1463** (= |sig_A| — the dominant component) |

**Reading.** Q 4's UAS rank 26/114 (upper-quartile) is driven almost ENTIRELY by its |iʿjāz| component
(|sig_A| = 3.15, the corpus's 2nd-largest magnitude). Its outlier component is small (1.08) and its
max-neighbour-TSP-cost is **exactly 0.0** — both seams are seamless, so the max-statistic clamps to zero
(Q 4 is one of very few surahs with a zero max-cost). Q 4 is an architectural standout on the
**iʿjāz-signature axis** (specifically as a fawāṣil-variety EXTREME), not on the outlier or seam axes. Its
high UAS comes from the *magnitude* of its sig_A deviation (the near-monorhyme), not from being a
high-structural-iʿjāz surah — |sig_A| is large because sig_A is very NEGATIVE.

## 7. Lexical counts (computed; `scripts/Q004_F_06_alif_monorhyme.py` pipeline)

| Quantity | Value | Note |
|:--|:--|:--|
| Verses | 176 | Hafs-Kūfan; carries the last-revealed verse (Q 4:176, kalāla; Bukhārī #4174) |
| Words (marks stripped) | 3,763 | |
| Letters | 16,332 | |
| Distinct QAC roots | 462 | `data/morphology/root-index.json`, 2,462 root-tokens |
| Opening | *yā-ayyuhā al-nās* (universal vocative) | shared with Q 2:21, Q 22:1, etc. |
| Rhyme rāwī | **ا (alif) 96.0%** | the lone alif-monorhyme among al-ṭiwāl |

## 8. Architectural-type classification

- **Outlier axis (H-NEW-590):** WEAK_OUTLIER (delta_pct +1.08) — near-neutral interior member of the head.
- **iʿjāz axis (H-NEW-750):** fawāṣil-variety MINIMUM (sig_A rank 113/114, rhyme entropy z −1.03) — the
  near-monorhyme alif.
- **Seam axis (H-NEW-720):** doubly-seamless (Q3→Q4 rank 4, Q4→Q5 rank 2) — max neighbour cost 0.0.
- **UAS (H-NEW-840):** upper-quartile (rank 26/114), driven by the |sig_A| magnitude.
- **Net:** Q 4 is the **near-monorhyme legal surah of the al-ṭiwāl head** — FR-distant, doubly-seamless,
  and a fawāṣil-variety extreme. Its architectural distinctiveness is its alif-monorhyme (a whole-surah
  phonological signature), unique among the long surahs.

## 9. Honest limits

- The Q004-F-06 Arm C NULL (Q 4's 96.0% is NOT a length-stratified extreme — Q 17, Q 18, Q 23 exceed it) means
  the alif-monorhyme should be read as "notable and unique-among-al-ṭiwāl" (Arm A) but NOT as "the corpus's
  most-concentrated long-surah rhyme." See `06-novel-findings.md`.
- UAS rank 26/114 reflects the *magnitude* of sig_A's deviation (a very negative sig_A), not high
  structural-iʿjāz — the UAS uses |sig_A|, so a fawāṣil-variety minimum scores high on |iʿjāz|. This is a
  known sign-ambiguity of the UAS composite and is flagged here.
- The H-NEW-590 window for Q 4 is the symmetric ±3 {1-7}; the WEAK_OUTLIER classification is
  window-definition-dependent.
- FR distances are on QAC-STEM root distributions; a lemma/surface metric would shift the neighbour list.

## 10. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 4 row); nearest = Q 2 (0.755); neighbours include Q 33, Q 24
- [[h-new-590|H-NEW-590]] — Q 4 WEAK_OUTLIER (delta_pct +1.08)
- [[h-new-700|H-NEW-700]] — alif rhyme 96.0% (lone alif-monorhyme among al-ṭiwāl)
- [[h-new-720|H-NEW-720]] — Q 3→Q 4 seamless (rank 4); Q 4→Q 5 seamless (rank 2); doubly-seamless
- [[h-new-750|H-NEW-750]] — sig_A rank 113/114 (fawāṣil-variety minimum); rhyme entropy 0.199 (z −1.03)
- [[h-new-840|H-NEW-840]] — UAS +0.8778 (rank 26/114); |sig_A|-driven; max-cost 0.0

---

*All numerical values traced to on-disk JSON artifacts as cited. Computed 2026-05-29.*
