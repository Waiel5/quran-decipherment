---
surah: 90
surah_name_ar: البلد
surah_name_translit: al-Balad
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -720 / -750 / -840 / -2210 (all values cited to path)
---

# Q 90 al-Balad — Empirical Profile


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

All values below are read directly from the on-disk artifacts. No value is asserted from memory.
Q 90 is surah-id 90; in the 1-indexed Fisher-Rao matrix it is index 90; in the 0-indexed phoneme
vector list (`h-new-700.json` → phoneme.phoneme_vectors) it is index 89.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`, 6441 pairs),
1-indexed surah IDs. Corpus matrix stats: min 0.2127, max 1.5509, mean 0.9235, median 0.9567.

| Quantity | Value |
|:--|:--|
| Q 90 mean FR to all 113 surahs | **0.8372** (well below corpus mean 0.9235 — Q 90 is centrally located) |
| Nearest neighbor | **Q 112 al-Ikhlāṣ** at FR 0.3953 |
| Top-15 FR neighbors | Q 112 (0.395), Q 103 (0.411), Q 107 (0.431), Q 108 (0.434), Q 104 (0.436), Q 106 (0.441), Q 111 (0.442), Q 105 (0.445), Q 113 (0.452), Q 101 (0.453), Q 94 (0.468), Q 95 (0.472), Q 110 (0.474), Q 102 (0.482), Q 100 (0.482) |
| 5 farthest | Q 6 (1.234), Q 2 (1.237), Q 4 (1.269), Q 9 (1.279), Q 3 (1.287) |

**Reading.** Q 90's entire top-15 FR neighborhood is the **short-mufaṣṣal qiṣār + muʿawwidhāt tail**
(Q 94–113): short, dense, creedal/eschatological surahs. Its nearest neighbor is **Q 112 al-Ikhlāṣ**
(the corpus FR-centroid per the theological-iʿjāz typology, Protocol §3.4) at FR 0.395 — an exceptionally
tight pairing. The 5 farthest are the long-narrative/legal Medinan-and-Meccan surahs (Q 2, 3, 4, 9, 6).
Q 90's low FR-mean (0.837, ≈4th decile) means it is a *content-central* short surah, not an isolate.

**The *(lā) uqsimu* opener-set is NOT an FR cluster** (the 8-attestation set, surahs {56, 69, 70, 75,
81, 84, 90}):

| uqsimu surah | FR to Q 90 | Rank in Q 90's FR list |
|:--|:--|:--|
| Q 81 al-Takwīr | 0.5872 | 28 / 113 |
| Q 84 al-Inshiqāq | 0.5999 | 30 / 113 |
| Q 75 al-Qiyāma (the co-*surah-initial* opener) | 0.6695 | **37 / 113** |
| Q 70 al-Maʿārij | 0.6800 | 38 / 113 |
| Q 69 al-Ḥāqqa | 0.7171 | 42 / 113 |
| Q 56 al-Wāqiʿa | 0.8342 | 57 / 113 |

None is a top-25 FR neighbor of Q 90 (ranks 28–57). **The oath-form is an opener-grammar axis, not a
content axis** — exactly consistent with the project's letter-axis ⊥ content-axis law. The Q 75 / Q 90
surah-initial *lā uqsimu* doublet (the only two in the corpus) is therefore a *structural* pairing, not
an FR-proximity one (descriptive, MW-7-capped — see `06-novel-findings.md` §2).

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

| Quantity | Value |
|:--|:--|
| Window (centered on Q 90) | {Q 87, 88, 89, 90, 91, 92, 93} |
| d̄_W (window with Q 90) | 0.5469 |
| d̄_W−X (window without Q 90) | 0.5397 |
| pct_W | 0.1 |
| pct_W−X | 0.27 |
| **delta_pct** | **−0.17** |
| p_greater_W | 0.999 |
| **classification** | **NULL** |

**Reading.** The {Q 87–93} window is one of the **lowest-dispersion neighborhoods in the entire corpus**
(pct_W = 0.1 — i.e. only ~0.1% of random windows are *tighter*). These seven short late-Meccan surahs
(al-Aʿlā, al-Ghāshiya, al-Fajr, al-Balad, al-Shams, al-Layl, al-Ḍuḥā) form an exceptionally cohesive
content block. Removing Q 90 *barely* changes the dispersion (delta_pct = −0.17, p = 0.999): Q 90 is a
deep **cohesion member**, not an outlier. Contrast Q 33 (+31.46 STRONG_OUTLIER) and Q 1 (+27.09). Q 90's
architectural interest is therefore micro-structural (its hapax roots, its oath-opener), NOT
whole-surah-dispersion-extreme.

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, Q 90): top final-letter **ه (tāʾ-marbūṭa / hāʾ)**, fraction **0.50**
(10/20 verses). Verified against `quran-min-tashkeel.json`: the surah has a **tripartite rhyme
architecture** —
- **vv 1–7:** -d ending (al-balad, al-balad, walad, kabad, aḥad, lubad, aḥad)
- **vv 8–10:** dual -ayn (ʿaynayn, shafatayn, al-najdayn)
- **vv 11–20:** -aba/-ah, tāʾ-marbūṭa (al-ʿaqaba ×2, raqaba, masghaba, maqraba, matraba, al-marḥama,
  al-maymana, al-mashʾama, mūṣada)

The tāʾ-marbūṭa block (10 verses) is the dominant rhyme; the diagnostic's 0.50 fraction captures it.
Project rhyme dispersion-tail law (two-piece-kink-50, primary_r2 = 0.7886): Q 90 (s=90 > 50) sits deep
in the dispersing tail; its dual-then-monorhyme shift across the three blocks is a *segmented* fawāṣil,
not a single tight monorhyme.

**Phoneme** (phoneme_vectors index 89, 4-dim density vector): `[0.02047, 0.04678, 0.04386, 0.12573]`.
Project phoneme dispersion-tail law (two-piece-kink-75, primary_r2 = 0.9457): Q 90 (s=90 > 75) sits past
the phoneme-kink in the dispersing regime. The 4th component (0.1257) dominates — the highest of Q 90's
four channels (and notably higher than Q 66's 0.1095). (Per-channel labels are not annotated in
`h-new-700.json`; not asserted here.)

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf
order, Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 90:

| Field | Value |
|:--|:--|
| n_verses | 20 |
| rhyme_entropy_nats | **1.1421** |
| top_final_letter | ه |
| top_final_letter_frac | 0.50 |
| mean_content_distance | 0.8372 |
| local_cohesion | 1.7362 |
| z_rhyme_entropy | +0.6741 |
| z_mean_content_distance | **−0.8520** |
| z_local_cohesion | +0.2964 |
| **sig_A** | **+1.5261** (rank **16 / 114**) |
| **sig_B** | **+0.9706** (rank **30 / 114**) |

**Reading.** Q 90's sig_A rank **16/114** places it in the **upper-decile** of the al-Bāqillānī
*iʿjāz al-fawāṣil* structural-significance axis — markedly higher than Q 66 (rank 34). The driver is the
strongly-negative `z_mean_content_distance` (−0.85): Q 90 is much *closer* to the corpus content-centroid
than average (consistent with its low FR-mean 0.837 and its Q 112 nearest-neighbor), while its rhyme
entropy is above average (z = +0.67, the three-block fawāṣil). The combination — content-central +
phonologically-varied — is exactly the structural-iʿjāz profile.

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

| Seam | delta_raw | fraction_residual | ascending-rank | class |
|:--|:--|:--|:--|:--|
| Q 89 → Q 90 | +0.05033 | 0.00607 | 47 / 113 | mid-low (smooth entry) |
| Q 90 → Q 91 | +0.09936 | 0.01198 | 81 / 113 | upper-mid (a content step) |

**Reading.** Q 90 is *entered* via a relatively smooth seam from Q 89 al-Fajr (rank 47/113) — both are
late-Meccan oath surahs, so the topic flows. The *exit* to Q 91 al-Shams is a costlier joint (rank
81/113): although Q 91 is Q 90's 23rd-nearest FR neighbor (FR 0.530), the mushaf-adjacency TSP cost is
mid-high — the transition from al-Balad's social-ethics close (the two companies) to al-Shams's cosmic
oath-cascade is a genuine content step. Top-3 most-expensive corpus seams for contrast: Q 1→Q 2 (0.622),
Q 32→Q 33 (0.363), Q 33→Q 34 (0.331); cheapest: Q 109→Q 110 (−0.031).

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method: `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **−0.4422** (rank **60 / 114**) |
| abs_outlier | 0.17 (from H-NEW-590 delta_pct) |
| max_cost | 0.09936 (the Q 90 → Q 91 seam) |
| abs_ijaz | 1.5261 (= sig_A) |

**Reading.** Q 90's UAS rank 60/114 is mid-band. The components pull in opposite directions: the outlier
strength is near-zero (deep cohesion member → low) and the seam cost is modest, BUT the iʿjāz signature
is upper-decile (rank 16). So Q 90 is **iʿjāz-strong but dispersion-quiet** — its architectural
significance lives in the *fawāṣil/content-centrality* axis, not the outlier/seam axes. It is not a
top-UAS hub (top-10: Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17).

## 7. Lexical + morphological counts (computed; cited to path)

| Quantity | Value | Note / Source |
|:--|:--|:--|
| Verses | 20 | `quran-text/quran-no-tashkeel.json` |
| Words (marks stripped) | 82 | computed |
| Letters | 342 | computed |
| Distinct QAC roots | 45 | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| Root tokens | 52 | same |
| Mean letters/word | 4.17 | computed (342/82) |
| Longest verse | v 17 (9 words, 45 letters) | *thumma kāna mina alladhīna āmanū…* |
| Shortest verse | v 13 (2 words, 6 letters) | *fakk raqaba* |
| **Corpus-hapax roots** | **4** — `kbd` (90:4), `njd` (90:10), `$fh` (90:9), `sgb` (90:14) | Q090-F-01; null-expected 0.42, p=0.0012 |
| Hapax-density rank | 10 / 114 | Q090-F-01 |

The 4 corpus-exclusive roots cluster in the surah's most concrete imagery: `kbd` (toil), `$fh`
(the two lips of the faculties-block), `njd` (the two highways of guidance), `sgb` (the day of hunger
of the ʿaqaba-block). This is the lexical signature of the early-Meccan concrete-imagery register.

## 8. Architectural-type classification

- **Outlier axis (H-NEW-590):** deep in-block COHESION member (NULL outlier; window pct 0.1, one of the
  tightest neighborhoods in the corpus) — Q 90 is *not* dispersion-extreme.
- **iʿjāz axis (H-NEW-750):** **upper-decile structural-iʿjāz** (sig_A rank 16/114), driven by
  content-centrality + varied fawāṣil.
- **UAS (H-NEW-840):** mid-band (rank 60/114) — iʿjāz-strong but outlier/seam-quiet.
- **Net:** Q 90 is a **content-central, iʿjāz-strong, dispersion-quiet short-Meccan surah** whose
  distinctive empirical signatures are *lexical* (the 4 corpus-hapax roots) and *opener-structural*
  (one of only 2 surah-initial *lā uqsimu* openers), NOT whole-surah-dispersion features.

## 9. Honest limits

- The phoneme 4-vector channel labels are not annotated in `h-new-700.json`; the per-channel
  interpretation is left un-assigned.
- The H-NEW-590 window for Q 90 is the symmetric ±3 neighborhood {87–93}; the NULL is window-definition
  dependent.
- FR distances are on QAC-STEM root distributions; a different token-level would shift the neighbor list.
- The hapax-root enrichment (Q090-F-01) is **register-level, not Q 90-exclusive**: the MW-6 control
  Q 91 al-Shams is equally enriched (see `06-novel-findings.md`).

## 10. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 90 row; nearest = Q 112)
- [[h-new-590|H-NEW-590]] — outlier-strength (Q 90 NULL, deep cohesion member of {87–93})
- [[h-new-700|H-NEW-700]] — rhyme (tāʾ-marbūṭa 50%) + phoneme dispersion-tails
- [[h-new-720|H-NEW-720]] — Q 89 → Q 90 (rank 47) / Q 90 → Q 91 (rank 81) seams
- [[h-new-750|H-NEW-750]] — iʿjāz signature (sig_A rank **16/114**, upper-decile)
- [[h-new-840|H-NEW-840]] — UAS rank 60/114
- [[h-new-2210|H-NEW-2210]] — qasam inventory (Q 90 = surah-initial *lā uqsimu*, jawāb la-tawkīd)

---

*All numerical values traced to on-disk JSON / morphology artifacts as cited. Computed 2026-05-30.*
