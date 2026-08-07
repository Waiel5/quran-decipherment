---
surah: 3
surah_name_ar: آل عمران
surah_name_translit: Āl ʿImrān
file_type: empirical-profile
date_last_updated: 2026-05-29
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -720 / -750 / -840 (all values cited to path)
---

# Q 3 Āl ʿImrān — Empirical Profile


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

All values below are read directly from the on-disk artifacts. No value is asserted from memory. Q 3 is
surah-id 3; in the 1-indexed Fisher-Rao matrix it is index 3; in the 0-indexed phoneme vector list
(`h-new-700.json` → phoneme.phoneme_vectors) it is index 2.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`, 6441 pairs),
1-indexed surah IDs. Corpus matrix stats: min 0.2127, max 1.5509, mean 0.9235, median 0.9567.

| Quantity | Value |
|:--|:--|
| Q 3 mean FR to all 113 surahs | **1.0943** (well ABOVE corpus mean 0.9235 — long surahs are FR-distant) |
| Nearest neighbour | **Q 2 al-Baqara** at FR 0.6309 |
| Top-8 FR neighbours | Q 2 (0.631), Q 5 (0.698), Q 4 (0.793), Q 8 (0.807), Q 6 (0.822), Q 39 (0.829), Q 16 (0.833), Q 40 (0.833) |
| 5 farthest | Q 107 (1.312), Q 77 (1.314), Q 80 (1.317), Q 56 (1.344), Q 55 (1.459) |
| Q 2 (prev) rank in Q 3's FR list | **1/113** (FR 0.6309) |
| Q 4 (next) rank in Q 3's FR list | **3/113** (FR 0.7931) |

**Reading.** Q 3's FR neighbourhood is exactly the al-sabʿ-al-ṭiwāl / long-Medinan-legal cluster:
its four nearest neighbours are Q 2, Q 5, Q 4, Q 8 — the head of the muṣḥaf. The Q 2–Q 3 FR distance
(0.6309) is one of the smallest long-surah pair-distances in the corpus, the empirical correlate of the
classical *al-Zahrāwān* ("two luminous ones") pairing. The 5 farthest are short Meccan oath/eschatology
surahs (Q 107 al-Māʿūn, Q 77 al-Mursalāt, Q 80 ʿAbasa, Q 56 al-Wāqiʿa) and the corpus FR-isolate Q 55
al-Raḥmān — the maximal content-register contrast.

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

| Quantity | Value |
|:--|:--|
| Window (centered on Q 3) | {Q 1, 2, 3, 4, 5, 6, 7} |
| d̄_W (window with Q 3) | 0.9154 |
| d̄_W−X (window without Q 3) | 0.9462 |
| pct_W | 37.9 |
| pct_W−X | 53.18 |
| **delta_pct** | **−15.28** |
| **classification** | **COHESION_ANCHOR** |

**Reading.** Removing Q 3 from the {Q1-7} window *raises* the window's content-dispersion percentile from
37.9 to 53.18 (delta_pct −15.28). Q 3 is a **cohesion anchor** — it pulls the long-surah head together. This
is the second-strongest cohesion-anchor signal in the head-block. Contrast Q 1 al-Fātiḥa, which is the
window's STRONG_OUTLIER (delta_pct +27.09): Q 1 sticks OUT of the long-surah head, while Q 3 binds it. Q 3's
cohesion role is consistent with its FR profile (nearest to Q 2, Q 4, Q 5 — it sits at the centroid of the
al-ṭiwāl cluster).

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, Q 3): top final-letter **ن (nūn)**, fraction **0.6091** (120/197
rhyme-bearing verses; the muqaṭṭaʿāt verse and 2 others lack a standard final-letter coda). Project rhyme
dispersion-tail law is two-piece-kink-50 (primary_r2 = 0.7886); Q 3 (s=3 < 50) is before the rhyme kink, in
the tighter-rhyme regime. Among ≥100-verse surahs, Q 3 has the SECOND-LOWEST rhyme concentration (0.609,
ahead only of Q 11 at 0.455) — Āl ʿImrān is rhythmically the most *varied* of the long surahs, the opposite
of its neighbour Q 4 (alif at 0.960).

**Phoneme** (phoneme_vectors index 2, 4-dim density vector):
`[0.01602, 0.03697, 0.03123, 0.10604]`. Project phoneme dispersion-tail law is two-piece-kink-75
(primary_r2 = 0.9457); Q 3 (s=3 < 75) is in the low-dispersion regime. The 4th component (0.1060) is by far
the largest — the same channel that dominates most surahs.

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order,
Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 3:

| Field | Value |
|:--|:--|
| n_verses | 200 |
| rhyme_entropy_nats | **1.2489** |
| top_final_letter | ن |
| top_final_letter_frac | 0.6091 |
| mean_content_distance | 1.0943 |
| local_cohesion | 1.1957 |
| z_rhyme_entropy | +0.8676 (above average — varied fawāṣil) |
| z_mean_content_distance | **+1.6855** (FR-distant — drives sig_A down) |
| z_local_cohesion | −0.4395 |
| **sig_A** | **−0.8179** (rank **84 / 114**) |
| **sig_B** | **+0.4281** (rank **45 / 114**) |

**Reading.** Q 3's rhyme entropy (1.25 nats, z = +0.87) is *above* corpus average — its verse-endings are
phonologically MORE varied than typical (consistent with its low 60.9% mono-rhyme concentration). But its
mean_content_distance z = **+1.69** (it is FR-far from the corpus) pulls sig_A down to rank 84/114. This is the
defining feature of long sui-generis surahs on the al-Bāqillānī axis: high fawāṣil-variety can be offset by
extreme content-distinctiveness. sig_B (rank 45/114) is upper-mid.

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

| Seam | delta_raw | ascending-rank | class |
|:--|:--|:--|:--|
| Q 2 → Q 3 | +0.01646 | 20 / 113 | smooth (below median 0.0621) |
| **Q 3 → Q 4** | **−0.04662** | **4 / 113** | **seamless** (one of the smoothest joints in the muṣḥaf) |

The block {Q2, Q3, Q4, Q5} has mean internal seam **−0.03196** — **rank 1/111** among all contiguous
4-surah blocks (Q003-F-01 Arm A). The smoothest-6 4-blocks are:
{2-5} (−0.0320), {4-7} (−0.0270), {3-6} (−0.0233), {91-94} (−0.0138), {84-87} (−0.0035), {109-112} (+0.0028).
The top THREE are all overlapping windows within al-sabʿ al-ṭiwāl. **Classical correlate:** al-Suyūṭī's
al-ṭiwāl grouping and al-Zarkashī/al-Biqāʿī's munāsaba for the muṣḥaf-head have a direct quantitative
correlate — the long-surah head is the most adjacency-cheap run in the corpus, because the seven long surahs
share a near-identical Medinan legal-creedal-narrative root-vocabulary.

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method: `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **+0.4517** (rank **37 / 114**) |
| abs_outlier | 15.28 (from H-NEW-590 delta_pct magnitude) |
| max_cost | 0.01646 (the Q 2 → Q 3 seam; Q 3 → Q 4 is negative so clamps below) |
| abs_ijaz | 0.8179 (= |sig_A|) |

**Reading.** Q 3's UAS rank 37/114 places it in the upper-third — driven almost entirely by its large
|outlier| component (15.28, the cohesion-anchor magnitude). The neighbour-TSP-cost is small (its expensive
side, Q 2→Q 3, is only 0.016, and Q 3→Q 4 is seamless). The iʿjāz component is mid (|sig_A| 0.82). Q 3 is an
architectural hub primarily on the **content-cohesion axis** (it binds the long-surah head), not on the
fawāṣil or seam axes.

## 7. Lexical counts (computed; `scripts/Q003_F_01_tiwal_block.py` pipeline)

| Quantity | Value | Note |
|:--|:--|:--|
| Verses | 200 | Hafs-Kūfan |
| Words (marks stripped) | 3,501 | |
| Letters | 14,985 | |
| Distinct QAC roots | 439 | `data/morphology/root-index.json`, 2,274 root-tokens |
| Opening | muqaṭṭaʿāt الم + creed | shared ALM-family with Q 2, 29, 30, 31, 32 |
| Rhyme rāwī | ن (nūn) 60.9% | least-concentrated of the long surahs |

## 8. Architectural-type classification

- **Outlier axis (H-NEW-590):** strong COHESION_ANCHOR (delta_pct −15.28) — Q 3 binds the long-surah head.
- **iʿjāz axis (H-NEW-750):** mid-low sig_A (rank 84/114), but with ABOVE-average rhyme entropy; the low rank
  is driven by extreme content-distance (z +1.69), not by monotone rhyme.
- **UAS (H-NEW-840):** upper-third (rank 37/114), driven by the cohesion-anchor component.
- **Net:** Q 3 is a **content-cohesion hub of the al-sabʿ-al-ṭiwāl head** — FR-nearest to al-Baqara, the
  interior hinge of the corpus's smoothest 4-surah run, and the binding member of the long-surah window. Its
  architectural interest is whole-surah-cohesion, not micro-structural.

## 9. Honest limits

- The H-NEW-590 window for Q 3 is the symmetric ±3 neighbourhood {1-7}; the COHESION_ANCHOR classification is
  window-definition-dependent. Under a different window scheme the delta_pct magnitude would shift.
- The Q003-F-01 Arm C NULL (block-smoothness not beyond chance once 111-block multiplicity is controlled)
  means the block's GLOBAL-min status (Arm A) should NOT be over-read as a statistically surprising
  signature — see `06-novel-findings.md`.
- FR distances are on QAC-STEM root distributions; a lemma- or surface-level metric would shift the neighbour
  list (though the Q 2 / Q 4 / Q 5 proximity is robust to token-level by the shared al-ṭiwāl vocabulary).
- The rhyme diagnostic counts 197 rhyme-bearing verses (not 200) because the muqaṭṭaʿāt verse and 2 others
  lack a standard final-letter coda; the 60.9% is over rhyme-bearing verses.

## 10. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 3 row); nearest = Q 2 (0.631)
- [[h-new-590|H-NEW-590]] — Q 3 COHESION_ANCHOR (delta_pct −15.28)
- [[h-new-700|H-NEW-700]] — nūn rhyme 60.9% (least-concentrated long surah)
- [[h-new-720|H-NEW-720]] — {2,3,4,5} rank-1 smoothest 4-block; Q 3→Q 4 seamless (rank 4/113)
- [[h-new-750|H-NEW-750]] — sig_A rank 84/114 (content-distance-driven)
- [[h-new-840|H-NEW-840]] — UAS +0.4517 (rank 37/114)

---

*All numerical values traced to on-disk JSON artifacts as cited. Computed 2026-05-29.*
