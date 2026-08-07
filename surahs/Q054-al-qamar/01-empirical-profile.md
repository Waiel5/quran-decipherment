---
surah: 54
surah_name_ar: القمر
surah_name_translit: al-Qamar
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: integrated from h-new-111 / -700 / -750 / -720 / -840 / -2310 / -2470 (all values cited to path); H-NEW-590 Q54 row NOT on disk (flagged)
---

# Q 54 al-Qamar — Empirical Profile


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

All values below are read directly from the on-disk artifacts. No value is asserted from memory. Q 54 is
surah-id 54; in the 1-indexed Fisher-Rao matrix it is surah 54; in the 0-indexed phoneme-vector list
(`h-new-700.json` → phoneme.phoneme_vectors) it is **index 53**.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`), 1-indexed surah IDs.
Corpus matrix stats (recomputed from the triples): min **0.2127**, max **1.5509**, mean **0.9235**, median **0.9567**.

| Quantity | Value |
|:--|:--|
| Q 54 mean FR to all 113 surahs | **0.9899** (above corpus mean 0.9235 — Q 54 is mildly content-distant) |
| Nearest neighbor | **Q 92 al-Layl** at FR **0.833** |
| Top-15 FR neighbors | Q 92 (0.833), Q 77 (0.836), Q 94 (0.841), Q 78 (0.847), Q 105 (0.850), Q 108 (0.851), Q 112 (0.853), Q 74 (0.854), Q 87 (0.857), Q 80 (0.857), Q 110 (0.858), Q 101 (0.858), Q 107 (0.860), Q 113 (0.860), Q 86 (0.861) |
| 5 farthest | Q 4 (1.331), Q 9 (1.326), Q 3 (1.270), Q 2 (1.261), Q 5 (1.242) |

**Reading.** Q 54's FR neighborhood is the **short-Meccan eschatological tail** (Q 92 al-Layl, Q 77 al-Mursalāt,
Q 94 al-Sharḥ, Q 78 al-Nabaʾ, Q 105 al-Fīl, Q 74 al-Muddaththir, Q 87 al-Aʿlā, Q 80 ʿAbasa, Q 86 al-Ṭāriq) —
short surahs with dense Hour/judgment/destruction vocabulary, NOT the long-Meccan prophet-cycle compendia.
The 5 farthest are the long Medinan legal surahs (Q 4 al-Nisāʾ, Q 9 al-Tawba, Q 3 Āl ʿImrān, Q 2 al-Baqara,
Q 5 al-Māʾida). **Critically, Q 54 is FR-distant from the prophet-cycle compendia it shares narrative content
with**: Q 7 al-Aʿrāf, Q 11 Hūd, Q 26 al-Shuʿarāʾ, Q 21 al-Anbiyāʾ are all >1.07 away. Q 54's prophet-cycle is so
radically COMPRESSED (5 pericopes × ~7 verses) that its root-fingerprint sits with the short-Meccan tail, not the
narrative compendia — the empirical refinement of the classical "prophet-cycle compendium" reading (see §8).

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`) — DATA-GAP

`h-new-590.json` carries **only 6 candidate surahs** in `candidate_results` (X = 1, 9, 18, 55, 62, 112) — the
pre-registered outlier-spectrum test was run on a targeted candidate set, **not on all 114 surahs. Q 54 is NOT
among the 6 candidates**, so there is no Q-54 outlier-strength row in `h-new-590.json` on disk.

The value the 00-overview reports (Δ = +3.57 pp WEAK_OUTLIER, window {Q 51-57}, p_greater_W = 0.1037) is **not
verifiable from `h-new-590.json`**. The abs_outlier component of Q 54's UAS *is* on disk, however, as
**abs_outlier = 3.57** in `h-new-840.json` (§6 below) — the +3.57 figure is the magnitude that fed the UAS
computation; the window membership, p-value and WEAK_OUTLIER label are not on disk and are flagged here as a
data-gap (likely from an unsaved all-114 windowing pass). **Honest correction of the 00-overview**: the
"+3.57 pp" magnitude is corroborated by `h-new-840.json`; the surrounding outlier-test detail is not.

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (`rhyme.rhyme_letter_diagnostics`, surah 54): top final-letter **ر (rāʾ)**, fraction **1.0** (55/55 verses),
n_verses **55**. This is a **perfect monorhyme** — corpus-extreme (see Q054-F-04, CONFIRMED). The project rhyme
dispersion-tail law is fitted two-piece-kink-50 (`rhyme.primary_r2`); Q 54 (s=54 > 50) sits just into the
dispersing tail, yet achieves zero rhyme-dispersion — an exception to the tail trend that is itself the finding.

**Phoneme** (`phoneme.phoneme_vectors` index 53, 4-dim density vector):
`[0.01906, 0.05037, 0.04765, 0.09530]`. The phoneme dispersion-tail law is fitted two-piece-kink-75
(`phoneme.primary_r2`). Q 54 (s=54 < 75) sits before the phoneme-kink, in the low-dispersion regime. The 4th
component (0.09530) is the largest of its four channels. (Channel labels are not annotated in `h-new-700.json`;
per-channel interpretation is left un-assigned to avoid an unverified mapping — see §9.)

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`, `per_surah` surah 54)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order,
Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 54:

| Field | Value |
|:--|:--|
| n_verses | 55 |
| rhyme_entropy_nats | **0.0** (exact zero — corpus minimum tier) |
| top_final_letter | ر |
| top_final_letter_frac | 1.0 |
| mean_content_distance | 0.98989 |
| local_cohesion | 0.97731 |
| z_rhyme_entropy | **−1.3940** |
| z_mean_content_distance | +0.6553 |
| z_local_cohesion | −0.7368 |
| **sig_A** | **−2.0493** (rank_A **105 / 114**) |
| **sig_B** | **−2.1308** (rank_B **114 / 114 — CORPUS MINIMUM**) |

**Reading.** Q 54's rhyme entropy is exactly 0.0 (z = −1.39, deep below corpus average) — its fawāṣil are a tight
single-consonant monorhyme, not a varied sajʿ. sig_A rank 105/114 places Q 54 LOW on the al-Bāqillānī *iʿjāz
al-fawāṣil* structural-significance axis; **sig_B rank 114/114 is the CORPUS MINIMUM on the al-Sakkākī *iqāʿ*
(rhythm-variety) axis.** This is the empirical signature of "iʿjāz lives in content-architecture, not in
fawāṣil-rhythm-variety": Q 54's distinction is its refrain-monopoly + compression + opener-structure + asmaic
closure (00-overview §4-6, §12), NOT phonological modulation. It is the corpus's strongest exemplar of
CONTENT-ARCHITECTURAL iʿjāz at the EXPENSE of FORMAL-PROSODIC iʿjāz.

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`, `per_adjacency`)

| Seam (`pair`) | delta_raw | fraction_residual | descending-rank (most-expensive) | class |
|:--|:--|:--|:--|:--|
| **Q 53 → Q 54** | **+0.21006** | **0.0253** | **12 / 113** | **TOP-12 EXPENSIVE seam** |
| Q 54 → Q 55 | +0.02482 | 0.0030 | 88 / 113 | smooth-tier |

The **Q 53 al-Najm → Q 54 al-Qamar seam is one of the corpus's 12 most-expensive canonical adjacencies** — a
content-genre transition (vision-pericope + sajda-closure → cosmic-Hour + 5-nation-destruction-catalog). This
**empirically refutes** the dispatch-brief's "clamped-zero seamless" hypothesis for this seam (Q054-F-03,
pre-commit-violation reported). For contrast, the corpus's most-expensive seams are Q 1 → Q 2 (0.622),
Q 32 → Q 33 (0.363), Q 33 → Q 34 (0.331), Q 9 → Q 10 (0.309), Q 24 → Q 25 (0.290) (`h-new-720.json` top10_expensive).
The forward seam **Q 54 → Q 55 al-Raḥmān is smooth (rank 88/113)**, contrary to a naïve prediction from their very
different opener types — the two refrain-architecture surahs join cheaply.

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`, `all_uas` surah 54)

Method (`h-new-840.json.method`): `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **1.8864** (rank **12 / 114**) |
| abs_outlier | **3.57** (the magnitude flagged in §2) |
| max_cost | **0.21006** (the Q 53 → Q 54 seam) |
| abs_ijaz | **2.04930** (= |sig_A|) |

**Reading.** Q 54's UAS rank 12/114 places it inside the corpus's top-12 architecturally-distinctive cohort. The
`h-new-840.json.top_15` roster is {Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17, 7, **54**, 25, 26, 51}. **The
co-membership of Q 55 al-Raḥmān (rank 7) and Q 26 al-Shuʿarāʾ (rank 14, just outside) with Q 54 is the
load-bearing observation**: all three are the corpus's strict-refrain-bearing surahs (H-NEW-2310 / -1320), and
their joint top-15 UAS placement confirms refrain-architecture as a corpus-distinctive structural mode. Q 54's UAS
is driven by the expensive Q 53→Q 54 seam (max_cost 0.21) and its strong |sig_A| (2.05), not by an outlier
component (3.57 is modest).

## 7. Refrain-architecture metrics (`findings/phase-b-hypotheses/csv/h-new-2310.json`, `h-new-1320.json`, `h-new-2470.json`)

Q 54 is one of the corpus's 5 strict-refrain surahs {Q 26, Q 37, Q 54, Q 55, Q 77}.

- **H-NEW-2310 (refrain census + spacing-regularity).** Q 54's intra-surah refrain
  *wa-laqad yassarnā al-Qurʾāna li-l-dhikr fa-hal min muddakir* repeats **4×** at vv **17, 22, 32, 40** (count
  re-derived at runtime via `assert`, not assumed). On the spacing-regularity inferential test, **Q 54 is a
  NULL**: V_obs = 4.222 vs null-median 40.67 (direction-true, the refrain *is* more regular than chance) but
  **p = 0.0846 misses α** — with only m=4 occurrences across N=55 the test is **underpowered** (H-NEW-2310 §2.1).
  Honest NULL, reported with equal prominence.
- **H-NEW-1320 (refrain-saturation corpus-rank).** Q 54 ranks **5 / 114** by max identical-verse-repeat-count
  (count 4, saturation 0.073, top repeated verse *wa-laqad yassarnā al-Qurʾāna li-l-dhikri fa-hal min muddakir*).
  It is the **tier-2 boundary** of the 3-tier refrain cluster {Q 55 (rank 1, sat 0.397), Q 77 (rank 2, sat 0.200),
  Q 26 (rank 3, sat 0.035)}, with Q 54 + Q 37 entering at the tier-2 edge.
- **H-NEW-2470 (ordering-by-dispersion).** Q 54 carries **13 similar-verse pairs** (double-digit, alongside Q 26
  (104), Q 77 (45), Q 37 (43)). In the named refrain-set concentration test Q 54 **disperses directionally**
  (depletion +0.47) but is far weaker than the Q 55 engine (+11.95) that decisively anchors the law. H-NEW-2470's
  honest verdict: ordering-by-dispersion is a **Q55-anchored refrain-architecture law, not a uniform every-surah
  law**; Q 54 is a directional-only contributor.

## 8. Architectural-type classification

- **Content axis (H-NEW-111):** short-Meccan-eschatological FR neighborhood; FR-distant from prophet-cycle
  compendia despite shared narrative — the compression makes Q 54 content-fingerprint with the short tail.
- **iʿjāz axis (H-NEW-750):** LOW formal-prosodic (sig_A rank 105/114; sig_B rank 114/114 corpus-MIN); zero rhyme
  entropy. CONTENT-ARCHITECTURAL iʿjāz exemplar.
- **Seam axis (H-NEW-720):** entered via a TOP-12 expensive seam (Q 53→Q 54, content-genre transition); exited via
  a smooth seam (Q 54→Q 55).
- **UAS (H-NEW-840):** rank 12/114 — a top-12 structural-distinctive surah, refrain-cohort member.
- **Net:** Q 54 is a **compressed-prophet-cycle, perfect-monorhyme, refrain-architecture surah** whose distinction
  is whole-surah content-architecture (refrain-monopoly + compression + asmaic closure), not phonological variety.

## 9. Honest limits

- **H-NEW-590 Q 54 row is NOT on disk** (only 6 candidates were saved). The +3.57 pp outlier *magnitude* is
  corroborated only via `h-new-840.json` abs_outlier; the window/p-value/WEAK_OUTLIER label are un-verifiable from
  the saved artifact and are flagged as a data-gap, NOT asserted (correction to 00-overview §9).
- The phoneme 4-vector channel labels are not annotated in `h-new-700.json`; the per-channel
  (emphatic/pharyngeal/sibilant/glottal) interpretation is deliberately left un-assigned.
- FR distances are on QAC-STEM root distributions; a lemma- or surface-token level would shift the neighbor list.
- H-NEW-2310's NULL for Q 54 is power-limited (m=4), not a direction reversal — the refrain *is* directionally
  regular; the corpus simply cannot confirm it at α with 4 points.

## 10. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 54 row; nearest Q 92, mean 0.9899)
- [[h-new-590|H-NEW-590]] — outlier-spectrum (Q 54 row NOT on disk — data-gap)
- [[h-new-700|H-NEW-700]] — perfect ر-monorhyme (1.0); phoneme low-dispersion regime
- [[h-new-720|H-NEW-720]] — Q 53→Q 54 TOP-12 expensive seam (rank 12/113); Q 54→Q 55 smooth (88/113)
- [[h-new-750|H-NEW-750]] — sig_A rank 105/114 LOW; sig_B rank 114/114 CORPUS-MIN; rhyme entropy 0.0
- [[h-new-840|H-NEW-840]] — UAS rank 12/114; refrain-cohort with Q 55 + Q 26
- [[h-new-2310|H-NEW-2310]] — yassarnā refrain 4× (vv 17/22/32/40); spacing-regularity NULL (p=0.085, underpowered)
- [[h-new-1320|H-NEW-1320]] — refrain-saturation rank 5/114; tier-2 boundary
- [[h-new-2470|H-NEW-2470]] — ordering-by-dispersion; Q 54 directional-only (+0.47), Q55-anchored law

---

*All numerical values traced to on-disk JSON artifacts as cited. Computed 2026-05-30.*
