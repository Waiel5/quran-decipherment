---
surah: 93
surah_name_ar: الضحى
surah_name_translit: al-Ḍuḥā
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -720 / -750 / -840 / -2280 (all values cited to path)
---

# Q 93 al-Ḍuḥā — Empirical Profile

All values below are read directly from the on-disk artifacts. No value is asserted from memory.
Q 93 is surah-id 93; in the 1-indexed Fisher-Rao matrix it is index 93; in the 0-indexed phoneme
vector list (`h-new-700.json` → phoneme.phoneme_vectors) it is index 92.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`, 6441 pairs),
1-indexed surah IDs. Corpus matrix stats: min 0.2127, max 1.5509, mean 0.9235, median 0.9567.

| Quantity | Value |
|:--|:--|
| Q 93 mean FR to all 113 surahs | **0.8152** (well below corpus mean 0.9235) |
| Nearest neighbor | **Q 108 al-Kawthar** at FR 0.3086 |
| Top-15 FR neighbors | Q 108 (0.309), Q 106 (0.353), Q 100 (0.364), **Q 94 (0.364)**, Q 113 (0.367), Q 111 (0.368), Q 105 (0.370), Q 107 (0.375), Q 103 (0.383), Q 112 (0.387), Q 110 (0.391), Q 114 (0.402), Q 104 (0.404), Q 97 (0.408), Q 102 (0.410) |
| 5 farthest | Q 2 (1.249), Q 5 (1.253), Q 4 (1.285), Q 9 (1.292), Q 3 (1.293) |

**Reading.** Q 93's FR neighborhood is the short-Meccan mufaṣṣal-qiṣār tail — its 14 nearest neighbors
are ALL short late-mushaf surahs (Q 94-114 region) plus Q 100 al-ʿĀdiyāt. The 5 farthest are the long
Medinan legal surahs (Q 2, 4, 5, 9, 3). Q 93's mean FR (0.8152) is among the lowest in the corpus — it
is tightly embedded in the short-surah cluster.

**The Q 94 al-Sharḥ pairing (Q093-F-01 Arm A, A-H1).** Q 94 al-Sharḥ is Q 93's **4th-nearest** FR
neighbor (FR 0.3641), inside the top-5. This is the WHOLE-SURAH-scale realization of the classical
Ṭāwūs / ʿUmar-b.-ʿAbd-al-ʿAzīz "one surah" pairing. By contrast Q 92 al-Layl — which shares the surface
oath-frame *wa-l-layl idhā [verb]* (Q 93:2 ↔ Q 92:1) and is chronologically adjacent (#9 → #11) — is only
Q 93's **18th**-nearest FR neighbor (FR 0.4338). The surface-anaphora bond (Q 92) and the
root-distribution bond (Q 94) point to DIFFERENT neighbors.

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

| Quantity | Value |
|:--|:--|
| Window (centered on Q 93) | {Q 90, 91, 92, 93, 94, 95, 96} |
| d̄_W (window with Q 93) | 0.4725 |
| d̄_W−X (window without Q 93) | 0.4806 |
| pct_W | 0.03 |
| pct_W−X | 0.09 |
| **delta_pct** | **−0.06** |
| p_greater_W | 0.9997 |
| **classification** | **NULL** |

**Reading.** Q 93 sits in one of the corpus's tightest content-windows: d̄_W ≈ 0.47 (vs the corpus FR
mean 0.92), i.e. the {Q 90-96} short-Meccan block is extraordinarily self-cohesive. Removing Q 93
changes the window dispersion by −0.06pp (p = 0.9997) — Q 93 is a **deep cohesion member**, not an
outlier. Its FR-mean of 0.8152 and this near-zero outlier-delta agree.

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, Q 93): top final-letter **ي (yāʾ)**, fraction **0.7273** (8/11
verses) — a strong monorhyme. The 8 yāʾ-final verses end on the *-ā/-ay* maqṣūra rhyme (*sajā, qalā, al-ūlā,
fa-tarḍā, fa-āwā, fa-hadā, fa-aghnā* — the long-alif-maqṣūra family) characteristic of the consolation
register; the remaining verses (v 1 *al-ḍuḥā*, vv 9-11 *taqhar/tanhar/fa-ḥaddith*) break it at the
command-block. Q 93 (s=93 > 50) sits in the dispersing rhyme tail per the project rhyme dispersion-tail
law (two-piece-kink-50, primary_r2 = 0.7886), yet its 72.7% monorhyme is well above the tail's average.

**Phoneme** (phoneme_vectors index 92, 4-dim density vector): `[0.02424, 0.03636, 0.01818, 0.09697]`.
The project phoneme dispersion-tail law is two-piece-kink-75 (primary_r2 = 0.9457); Q 93 (s=93 > 75)
sits in the dispersing phoneme regime. The 4th component (0.0970) dominates the four channels.

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf
order, Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 93:

| Field | Value |
|:--|:--|
| n_verses | 11 |
| rhyme_entropy_nats | **0.7595** |
| top_final_letter | ي |
| top_final_letter_frac | 0.7273 |
| mean_content_distance | 0.8152 |
| local_cohesion | **2.3828** |
| z_rhyme_entropy | −0.0186 |
| z_mean_content_distance | −1.0689 |
| z_local_cohesion | +1.1767 |
| **sig_A** | **+1.0503** (rank **32 / 114**) |
| **sig_B** | **+1.1581** (rank **23 / 114**) |

**Reading.** Q 93's local_cohesion is **2.38 (z = +1.18)** — among the HIGHEST in the corpus: the surah's
fawāṣil and content are tightly self-similar (the *-ā/-ay* monorhyme + the repetitive *wajadaka… / ammā…
fa-lā…* parallel constructions). Its mean_content_distance z = −1.07 (it is much closer to other surahs
than average — the short-Meccan-tail effect). sig_A rank 32/114 and sig_B rank 23/114 both place Q 93 in
the **upper third** of the al-Bāqillānī *iʿjāz al-fawāṣil* structural-significance axis — driven by the
high local cohesion and the strong yāʾ monorhyme.

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

| Seam | delta_raw | ascending-rank | class |
|:--|:--|:--|:--|
| Q 92 → Q 93 | +0.06063 | 55 / 113 | mid-spectrum |
| **Q 93 → Q 94** | **−0.01520** | **10 / 113** | **seamless** (one of the 13 clamped/negative seams) |
| Q 94 → Q 95 | +0.04700 | 43 / 113 | mid-spectrum |

The 13 seamless seams (delta_raw ≤ 0), ascending: Q 91→92 (1), Q 4→5 (2), Q 6→7 (3), Q 3→4 (4),
Q 65→66 (5), Q 109→110 (6), Q 73→74 (7), Q 105→106 (8), Q 86→87 (9), **Q 93→94 (10)**, Q 64→65 (11),
Q 72→73 (12), Q 37→38 (13). Q 93 is EXITED via one of the smoothest joints in the mushaf (Q 93 → Q 94).
For contrast the most expensive corpus seams are Q 1→Q 2 (0.622), Q 32→Q 33 (0.363), Q 33→Q 34 (0.331).

**Classical correlate.** The Ṭāwūs / ʿUmar-b.-ʿAbd-al-ʿAzīz "one surah" pairing of al-Ḍuḥā + al-Sharḥ
(al-Rāzī, *Mafātīḥ al-ghayb*, on Q 94:1) has a direct whole-surah correlate: the rank-10 seamless seam.
But see §7 — the boundary-pericope lexical overlap is ZERO, so the seamlessness is a whole-surah
root-distribution effect, not a seam-lexical effect.

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method: `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **−1.4521** (rank **87 / 114**) |
| abs_outlier | 0.06 (from H-NEW-590 delta_pct) |
| max_cost | 0.06063 (the Q 92 → Q 93 seam — the larger of Q 93's two seams) |
| abs_ijaz | 1.0503 (= sig_A) |

**Reading.** Q 93's UAS rank 87/114 places it in the lower band. The driver is the near-zero outlier
strength (deep cohesion member) and the low max-neighbor TSP cost (the Q 93 → Q 94 exit seam is
seamless/negative, so the max defaults to the modest Q 92 → Q 93 entry seam at 0.0606). Only the iʿjāz
component (sig_A +1.05) is in the upper band. Q 93 is therefore **NOT a whole-surah-dispersion hub** (top
UAS are Q 33, 1, 2, 9, 24, ...); its architectural interest is **micro-structural** — the favor→command
orphan-recall (Q093-F-01 Arm B) and the seam scale-dissociation (Arm A) — and **phonological** (the
strong yāʾ monorhyme + high local cohesion).

## 7. Boundary-pericope seam (H-NEW-2280 method; computed in `csv/Q093-F-01.json`)

Reproducing the H-NEW-2280 seam-Jaccard (QAC v0.4 ROOT, first-ROOT-per-segment convention) for the
Q 93 → Q 94 seam:

| k | J(Q93→Q94) | shared roots | corpus mean seam J | null mean | Q93→Q94 percentile |
|:--|:--|:--|:--|:--|:--|
| **3** | **0.0000** | — (none) | 0.0416 | 0.0381 | 43.4 |
| **5** | **0.0000** | — (none) | 0.0632 | 0.0508 | 24.8 |

The close of al-Ḍuḥā (last 3/5 verses) and the opening of al-Sharḥ (first 3/5 verses) share **ZERO QAC
roots**. The only root shared by the two surahs anywhere is `rbb` (Lord) — Q 93:3,5,11 and Q 94:8 — and
it does not fall in the boundary pericopes (Q 93's last verse v 11 carries `Hdv, nEm, rbb`; Q 94's first
verse v 1 carries `$rH, Sdr`; at k=5 the pericopes are {Q93 vv7-11} vs {Q94 vv1-5} and still share none).
**The whole-surah FR proximity (rank 4) and the seamless TSP joint (rank 10) coexist with a boundary
root-Jaccard of exactly 0** — the central dissociation of Q093-F-01 Arm A.

## 8. Lexical counts (computed; `scripts/Q093_F_01_duha_sharh_seam.py` pipeline)

| Quantity | Value | Note |
|:--|:--|:--|
| Verses | 11 | |
| Words (marks stripped) | 40 | |
| Letters | 165 | one of the corpus's shortest surahs by letter-count |
| Distinct QAC roots | 23 | `data/morphology/root-index.json`, 28 root-tokens |
| `wjd` (wajadaka) occurrences | 3 | vv 6, 7, 8 (the favor anaphora; Arm B B-H1) |
| `ytm` (yatīm) occurrences | 2 | vv 6, 9 (the unique favor→command bridge; Arm B B-H2) |
| `rbb` (Lord) occurrences | 3 | vv 3, 5, 11 (the consolation/proclamation refrain) |

## 9. Architectural-type classification

- **Outlier axis (H-NEW-590):** deep in-block COHESION member (NULL outlier; one of the tightest windows in the corpus).
- **iʿjāz axis (H-NEW-750):** upper-third structural-iʿjāz (sig_A rank 32, sig_B rank 23); very high local cohesion (z = +1.18).
- **UAS (H-NEW-840):** lower band (rank 87/114) — not a dispersion hub.
- **Net:** Q 93 is a **tightly-cohesive, monorhymed short-Meccan consolation surah** whose distinctive
  empirical signatures are *micro-structural* (the favor→command orphan-recall) and *seam-dissociative*
  (whole-surah-paired with Q 94 but boundary-lexically null), not whole-surah-dispersion features.

## 10. Honest limits

- The phoneme 4-vector dimension labels are not annotated in `h-new-700.json`; only the raw densities are
  reported, so the per-channel mapping (emphatic/pharyngeal/sibilant/glottal) is left un-assigned here.
- H-NEW-590's window for Q 93 is the symmetric ±3 neighborhood {90-96}; the NULL classification is
  window-definition-dependent.
- FR distances are on QAC-STEM root distributions (not full lemmas or surface tokens); a different
  token-level would shift the neighbor list — but Q 94's top-5 rank is robust given FR 0.364 is far inside
  the top decile.
- The seam root-Jaccard of 0.0 is on the QAC v0.4 ROOT level; a surface-token or lemma seam metric could
  register the shared *rabbi* (Q 93:11 *bi-niʿmati rabbika* / Q 94:8 *wa-ilā rabbika*) — but at the ROOT
  level the boundary pericopes are disjoint, and the dissociation claim is ROOT-level (matching H-NEW-2280).

## 11. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 93 row); Q 94 is 4th-nearest neighbor
- [[h-new-590|H-NEW-590]] — outlier-strength (Q 93 NULL, deep cohesion member of {90-96})
- [[h-new-700|H-NEW-700]] — yāʾ monorhyme 72.7%; phoneme dispersing regime (s>75)
- [[h-new-720|H-NEW-720]] — Q 93 → Q 94 seamless seam (rank 10/113)
- [[h-new-750|H-NEW-750]] — iʿjāz signature (sig_A rank 32, sig_B rank 23); local cohesion z = +1.18
- [[h-new-840|H-NEW-840]] — UAS rank 87/114
- [[h-new-2280|H-NEW-2280]] — al-Biqāʿī munāsabah-seam; Q 93 → Q 94 is a zero-Jaccard seam
- [[cross-finding-025|CF-025]] — scale-of-aggregation; Arm A is a new supporting instance

---

*All numerical values traced to on-disk JSON artifacts as cited. Computed 2026-05-30.*
