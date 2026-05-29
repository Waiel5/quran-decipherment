---
surah: 66
surah_name_ar: التحريم
surah_name_translit: al-Taḥrīm
file_type: empirical-profile
date_last_updated: 2026-05-29
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -720 / -750 / -840 (all values cited to path)
---

# Q 66 al-Taḥrīm — Empirical Profile

All values below are read directly from the on-disk artifacts. No value is asserted from memory.
Q 66 is surah-id 66; in the 1-indexed Fisher-Rao matrix it is index 66; in the 0-indexed phoneme
vector list (`h-new-700.json` → phoneme.phoneme_vectors) it is index 65.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`, 6441 pairs),
1-indexed surah IDs. Corpus matrix stats: min 0.2127, max 1.5509, mean 0.9235, median 0.9567.

| Quantity | Value |
|:--|:--|
| Q 66 mean FR to all 113 surahs | **0.9093** (just below corpus mean 0.9235) |
| Nearest neighbor | **Q 110 al-Naṣr** at FR 0.7259 |
| Top-15 FR neighbors | Q 110 (0.726), Q 112 (0.738), Q 98 (0.741), Q 85 (0.745), Q 114 (0.747), Q 64 (0.753), Q 1 (0.755), Q 106 (0.758), Q 95 (0.763), Q 109 (0.770), Q 108 (0.771), Q 111 (0.773), Q 103 (0.775), Q 104 (0.778), Q 61 (0.779) |
| 5 farthest | Q 17 (1.094), Q 12 (1.109), Q 6 (1.111), Q 26 (1.135), Q 55 (1.193) |

**Reading.** Q 66's FR neighborhood is the short-Medinan / short-Meccan tail (Q 110, 112, 98, 64, 1,
61, 109, 108, 111) — short surahs with dense Allāh/believer/judgment vocabulary, NOT the long-narrative
surahs. The 5 farthest are the long Meccan narrative surahs (Q 12 Yūsuf, Q 26 al-Shuʿarāʾ, Q 6 al-Anʿām,
Q 17 al-Isrāʾ) + the FR-isolate Q 55 al-Raḥmān (corpus-farthest, rank 114/114 per H-NEW-1220).

**Prophet-vocative family ranks within Q 66's FR list** (the set {Q 8, 9, 33, 60, 65}):

| Family member | Rank in Q 66's FR list | FR to Q 66 |
|:--|:--|:--|
| Q 60 al-Mumtaḥana | 27 / 113 | 0.8038 |
| Q 49 al-Ḥujurāt (`yā-ayyuhā alladhīna āmanū` sister-cluster) | 32 / 113 | 0.8111 |
| Q 65 al-Ṭalāq | 49 / 113 | 0.8705 |
| Q 33 al-Aḥzāb | 72 / 113 | 0.9609 |

None of the prophet-vocative co-members is a top-15 FR neighbor of Q 66. This is **exactly consistent
with H-NEW-1360** (the *yā-ayyuhā al-nabī* family is whole-surah-NULL; its cohesion is pericope-scale
only, per H-NEW-1520). Q 33 al-Aḥzāb, the family's UAS-rank-1 anchor, is the *fourth-farthest* family
member from Q 66 — the vocative does not impose whole-surah FR proximity.

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

| Quantity | Value |
|:--|:--|
| Window (centered on Q 66) | {Q 63, 64, 65, 66, 67, 68, 69} |
| d̄_W (window with Q 66) | 0.8639 |
| d̄_W−X (window without Q 66) | 0.8635 |
| pct_W | 19.2 |
| pct_W−X | 21.1 |
| **delta_pct** | **−1.90** |
| p_greater_W | 0.808 |
| **classification** | **NULL** |

**Reading.** Removing Q 66 from its 7-surah neighborhood barely changes the window's content-dispersion
(delta_pct = −1.90, p = 0.808). Q 66 is a **cohesion member** of the short-Medinan {Q 63-69} window, not
an outlier — it sits comfortably inside its neighborhood's content-distribution. Contrast Q 1 (+27.09pp
STRONG_OUTLIER) and Q 55 — Q 66 is architecturally "in-block," consistent with its FR mean of 0.9093.

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, Q 66): top final-letter **ن (nūn)**, fraction **0.4167** (5/12 verses).
Project rhyme dispersion-tail law fitted as two-piece-kink-50 (primary_r2 = 0.7886) — Q 66 (s=66 > 50)
sits in the dispersing tail; its nūn-dominance is moderate, not a tight monorhyme.

**Phoneme** (phoneme_vectors index 65, 4-dim density vector):
`[0.02172, 0.04434, 0.02353, 0.10950]`. Project phoneme dispersion-tail law fitted as two-piece-kink-75
(primary_r2 = 0.9457). Q 66 (s=66 < 75) sits before the phoneme-kink, in the low-dispersion regime.
The 4th component (0.1095) is the largest — Q 66's phoneme density is concentrated in its 4th channel,
the highest of its four dimensions.

(Rhyme-entropy and the z-normalized phonological diagnostics are taken from `h-new-750.json`, §4 below.)

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf
order, Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 66:

| Field | Value |
|:--|:--|
| n_verses | 12 |
| rhyme_entropy_nats | **1.2367** |
| top_final_letter | ن |
| top_final_letter_frac | 0.4167 |
| mean_content_distance | 0.9093 |
| local_cohesion | 1.1521 |
| z_rhyme_entropy | +0.8454 |
| z_mean_content_distance | −0.1403 |
| z_local_cohesion | −0.4988 |
| **sig_A** | **+0.9856** (rank **34 / 114**) |
| **sig_B** | **+0.3466** (rank **48 / 114**) |

**Reading.** Q 66's rhyme entropy (1.24 nats, z = +0.85) is *above* corpus average — its fawāṣil are
phonologically more varied than typical, not a tight monorhyme. sig_A rank 34/114 places Q 66 in the
upper-mid band of the al-Bāqillānī *iʿjāz al-fawāṣil* structural-significance axis. local_cohesion 1.152
(z = −0.50) is below average — Q 66 is *less* locally self-cohesive than the median surah, fitting its
thematically-segmented structure (asbāb episode → believer/disbeliever charges → dual-exemplar seal).

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

| Seam | delta_raw | ascending-rank | class |
|:--|:--|:--|:--|
| **Q 65 → Q 66** | **−0.03397** | **5 / 113** | **seamless** (one of the 13 clamped/negative seams) |
| Q 66 → Q 67 | +0.07804 | 67 / 113 | mid-spectrum |

The 13 seamless seams (delta_raw ≤ 0): pairs opening at Q 3, 4, 6, 37, **64, 65**, 72, 73, 86, 91, 93,
105, 109. Q 66 is entered via one of the smoothest joints in the mushaf (Q 65 al-Ṭalāq → Q 66 al-Taḥrīm),
and Q 64 → Q 65 is also seamless — so the run Q 64 → Q 65 → Q 66 is a **double-seamless entry**. The exit
Q 66 → Q 67 al-Mulk is a normal mid-cost transition (the topic shifts from Medinan domestic-legal to
Meccan-style cosmic-sovereignty).

**Classical correlate.** al-Rāzī's munāsaba for Q 65 → Q 66 (both surahs concern aḥkām al-nisāʾ; al-Ṭalāq
opens on divorce-as-prohibition-of-the-lawful, al-Taḥrīm opens on self-prohibition-of-the-lawful) has a
direct empirical correlate in the rank-5 seamless seam. Top-3 most-expensive corpus seams for contrast:
Q 1→Q 2 (0.622), Q 32→Q 33 (0.363), Q 33→Q 34 (0.331).

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method: `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **−1.0521** (rank **77 / 114**) |
| abs_outlier | 1.90 (from H-NEW-590 delta_pct) |
| max_cost | 0.07804 (the Q 66 → Q 67 seam) |
| abs_ijaz | 0.9856 (= sig_A) |

**Reading.** Q 66's UAS rank 77/114 places it in the lower-middle band. Each component is modest: the
outlier strength is near-zero (cohesion member), the max neighbor TSP cost is low (seamless backward
seam pulls the max down to the forward seam, 0.078), and the iʿjāz signature is upper-mid. Q 66 is NOT
a top-UAS architectural hub (top-10 are Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17). Its architectural
interest is **local and structural** (the verbatim twin + the corpus-exclusive antithetical seal-frame),
not whole-surah-dispersion-extreme.

## 7. Lexical counts (computed; `scripts/Q066_F_01_tahrim_seal.py` pipeline + close-read scan)

| Quantity | Value | Note |
|:--|:--|:--|
| Verses | 12 | |
| Words (marks stripped) | 254 | |
| Letters | 1,105 | |
| Distinct QAC roots | 96 | `data/morphology/root-index.json`, 171 root-tokens |
| Longest verse | v 8 (46 words) | the *tawba naṣūḥ* + light-of-believers verse |
| Allāh-substring tokens | 13 | coverage 8/12 verses (66.7%) |
| Verbatim full-verse twin | v 9 ≡ Q 9:73 | one of 11 corpus long-verse twin groups (Q066-F-01 Arm A) |

## 8. Architectural-type classification

- **Outlier axis (H-NEW-590):** in-block COHESION member (NULL outlier) — Q 66 is not dispersion-extreme.
- **iʿjāz axis (H-NEW-750):** upper-mid structural-iʿjāz (sig_A rank 34/114), above-average rhyme entropy.
- **UAS (H-NEW-840):** lower-middle (rank 77/114) — not a structural hub.
- **Net:** Q 66 is a **locally-structured, in-block short-Medinan surah** whose distinctive empirical
  signatures are *micro-structural* (the verbatim verse-twin and the corpus-exclusive antithetical
  exemplar-frame) rather than whole-surah-dispersion features. This matches its content profile: a
  tightly-sequenced domestic-legal-then-exemplar surah, not a sprawling narrative.

## 9. Honest limits

- The phoneme 4-vector dimension labels are not annotated in `h-new-700.json`; only the raw 4-density
  values are reported, so the per-channel interpretation (emphatic/pharyngeal/sibilant/glottal) is left
  un-assigned here to avoid asserting an un-verified mapping.
- H-NEW-590's window for Q 66 is the symmetric ±3 neighborhood {63-69}; the NULL classification is
  window-definition-dependent and would not necessarily hold under a different window scheme.
- FR distances are on QAC-STEM root distributions (not full lemmas or surface tokens); a different
  token-level would shift the neighbor list.

## 10. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 66 row)
- [[h-new-590|H-NEW-590]] — outlier-strength (Q 66 NULL, cohesion member)
- [[h-new-700|H-NEW-700]] — rhyme + phoneme dispersion-tails
- [[h-new-720|H-NEW-720]] — Q 65 → Q 66 seamless seam (rank 5/113)
- [[h-new-750|H-NEW-750]] — iʿjāz signature (sig_A rank 34)
- [[h-new-840|H-NEW-840]] — UAS rank 77/114
- [[h-new-1360|H-NEW-1360]] / [[h-new-1520|H-NEW-1520]] — prophet-vocative family geometry

---

*All numerical values traced to on-disk JSON artifacts as cited. Computed 2026-05-29.*
