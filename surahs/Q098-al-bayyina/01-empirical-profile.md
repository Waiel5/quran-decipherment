---
surah: 98
surah_name_ar: البينة
surah_name_translit: al-Bayyina
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -750 / -840 / -720 (all values cited to path); H-NEW-590 data-gap in 00-overview CORRECTED (Q98 IS computed, WEAK_OUTLIER)
---

# Q 98 al-Bayyina — Empirical Profile


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
Q 98 is surah-id 98; in the 1-indexed Fisher-Rao matrix it is index 98; in the 0-indexed phoneme/iʿjāz
per-surah lists (`h-new-700.json` → phoneme.phoneme_vectors; `h-new-700.json` → rhyme_letter_diagnostics)
it is index **97**.

> **Correction to `00-overview.md`.** The overview's §3 anchor table states H-NEW-590 for Q 98 is "NOT
> computed (Q98 not in the 6-candidate set)". This is FALSE on disk: while Q 98 is not one of the 6
> *focal* candidates {1, 9, 18, 55, 62, 112}, `h-new-590.json` → `all_surahs_results` is a full 114-entry
> list and **contains Q 98** (window {95-101}, delta_pct **+0.01**, p_greater_W **0.9997**, classification
> **WEAK_OUTLIER**). The value is real and is the `abs_outlier` term used in Q 98's UAS (H-NEW-840). §2
> below reports the correct figures; the overview's "data-gap" label is retracted here.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`, 6441 pairs),
1-indexed surah IDs. Corpus matrix stats: min 0.2127, max 1.5509, mean **0.923487**, median 0.956707.

| Quantity | Value |
|:--|:--|
| Q 98 mean FR to all 113 surahs | **0.8214** (well below corpus mean 0.9235) |
| Nearest neighbor | **Q 108 al-Kawthar** at FR **0.4951** |
| Top-6 FR neighbors | Q 108 (0.4951), Q 110 (0.4994), Q 112 (0.5076), Q 106 (0.5096), Q 95 (0.5112), Q 113 (0.5139) |
| 5 farthest | Q 3 (1.1388), Q 4 (1.1443), Q 6 (1.1581), Q 12 (1.1649), Q 26 (1.1773) |

**Reading.** Q 98's FR neighborhood is the short-surah cluster (Q 108 al-Kawthar, Q 110 al-Naṣr, Q 112
al-Ikhlāṣ, Q 106 Quraysh, Q 95 al-Tīn, Q 113 al-Falaq) — short, dense, creedal/eschatological surahs, NOT
the long-narrative ones. Its mean FR (0.8214) is markedly below corpus mean (0.9235): Q 98 sits in the
low-dispersion, lexically-compact end of FR space, exactly as its 8-verse / 42-root profile predicts. The
5 farthest are the long Meccan/Medinan narrative-legal surahs (Q 26 al-Shuʿarāʾ, Q 12 Yūsuf, Q 6 al-Anʿām,
Q 4 al-Nisāʾ, Q 3 Āl ʿImrān).

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

`all_surahs_results` entry for X = 98:

| Quantity | Value |
|:--|:--|
| Window (centered on Q 98) | {Q 95, 96, 97, 98, 99, 100, 101} |
| d_W (window with Q 98) | 0.474530 |
| d_W−X (window without Q 98) | 0.438550 |
| pct_W | 0.03 |
| pct_W−X | 0.02 |
| **delta_pct** | **+0.01** |
| p_greater_W | 0.9997 |
| **classification** | **WEAK_OUTLIER** |

**Reading.** This is the corpus's *flattest* outlier-window — Q 98 sits inside a 7-surah neighborhood
(Q 95-101: al-Tīn, al-ʿAlaq, al-Qadr, al-Bayyina, al-Zalzala, al-ʿĀdiyāt, al-Qāriʿa) whose mutual
content-dispersion is already near-minimal (d_W = 0.47, far below the corpus median 0.957). Removing Q 98
barely moves the window dispersion (delta_pct = +0.01, p = 0.9997). The `WEAK_OUTLIER` label here reflects
the *tiny absolute* delta in a *very low-dispersion* window, not a real architectural outlier — Q 98 is a
**cohesion member** of the short-mufaṣṣal {95-101} block. Contrast the corpus extremes Q 33 (+31.46pp) and
Q 1 (+27.09pp STRONG_OUTLIER). Q 98 is architecturally "in-block," consistent with its low FR mean.

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, index 97): `{"surah": 98, "top_letter": "ه", "frac": 1.0,
"n_verses": 8}`. Q 98's final-grapheme is **ه/ة (the tāʾ-marbūṭa / hāʾ rhyme)** in **8/8 verses (frac =
1.0)** — a **PERFECT monorhyme**. Every fāṣila ends on the -iyya / -a(h) syllable: al-bayyina, muṭahhara,
qayyima, al-bayyina, al-qayyima, al-bariyya, al-bariyya, rabbah. Project rhyme dispersion-tail law fitted
two-piece-kink-50 (`h-new-700.json` rhyme.primary_r2); Q 98 (s=98 > 50) sits in the dispersing tail, yet
is a maximally-tight monorhyme — a local counter-current to the s>50 dispersion gradient.

**Phoneme** (phoneme_vectors index 97, 4-dim density vector):
`[0.017327, 0.029703, 0.027228, 0.126238]`. Project phoneme dispersion-tail law fitted two-piece-kink-75
(`h-new-700.json` phoneme.primary_r2 = 0.9457, verdict INTERMEDIATE, β_lin = +0.00089). Q 98 (s=98 > 75)
sits in the dispersing tail. The 4th component (0.1262) dominates — the largest single channel — and is
notably higher than e.g. Q 66's 4th channel (0.1095), consistent with Q 98's dense -iyya/-ah glide-rhyme.

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf
order, Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 98:

| Field | Value |
|:--|:--|
| n_verses | 8 |
| rhyme_entropy_nats | **0.0** (zero — perfect monorhyme) |
| top_final_letter | ه |
| top_final_letter_frac | 1.0 |
| mean_content_distance | 0.821376 |
| local_cohesion | **1.7130** |
| z_rhyme_entropy | **−1.3940** |
| z_mean_content_distance | −1.0077 |
| z_local_cohesion | +0.2649 |
| **sig_A** | **−0.38628** (rank **73 / 114**) |
| **sig_B** | **−1.12911** (rank **88 / 114**) |

**Reading.** Q 98's rhyme entropy is **exactly 0.0 nats** (z = −1.39) — the corpus floor for fawāṣil
variety, because all 8 verse-ends share one rhyme-grapheme. This is the al-Bāqillānī *iʿjāz al-fawāṣil*
axis at its *most monophonic* (the OPPOSITE pole from a high-entropy surah). sig_A rank 73/114 and sig_B
rank 88/114 place Q 98 in the lower band of the structural-significance axis — its iʿjāz interest is NOT
whole-surah-dispersion but the micro-structural monorhyme + the closing antonym muqābala. local_cohesion
1.7130 (z = +0.26) is slightly above median — the 8 verses are reasonably self-cohesive (single coherent
pericope on the People-of-the-Book schism + the believer/disbeliever verdict).

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

`per_adjacency` (113 entries); ascending-rank by delta_raw (rank 1 = smoothest/cheapest seam):

| Seam | delta_raw | fraction_residual | ascending-rank | class |
|:--|:--|:--|:--|:--|
| **Q 97 al-Qadr → Q 98 al-Bayyina** | **+0.02750** | 0.00332 | **27 / 113** | low-cost (smooth entry) |
| **Q 98 al-Bayyina → Q 99 al-Zalzala** | **+0.12653** | 0.01526 | **91 / 113** | mid-to-expensive exit |

**Reading.** Q 98 is *entered* via a low-cost seam from Q 97 al-Qadr (rank 27/113 — both short, both on the
revelation/scripture-descent theme: al-Qadr on the Night the Qurʾān descended, al-Bayyina on the Messenger
bringing the purified scrolls). It *exits* into Q 99 al-Zalzala via a more expensive seam (rank 91/113 —
the topic pivots sharply from the scripture-and-verdict register to the Day-of-the-earthquake eschatology).
Corpus cumulative stats: sum_delta = 9.827, mean_delta = 0.0870, ratio_sum_to_residual = 1.185
(super-additive, cooperative structure). Top-3 most-expensive corpus seams for contrast: Q 1→Q 2 (0.622),
Q 32→Q 33 (0.363), Q 33→Q 34 (0.331).

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method (verbatim from file): `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **−1.6965** (rank **93 / 114**) |
| abs_outlier | 0.01 (= H-NEW-590 delta_pct for Q 98 — confirms Q 98 WAS in the outlier computation) |
| max_cost | 0.12653 (the Q 98 → Q 99 seam — Q 98's most expensive neighbor seam) |
| abs_ijaz | 0.38628 (= |sig_A|) |

**Reading.** Q 98's UAS rank 93/114 places it firmly in the **anti-iʿjāz / low-architectural-significance**
band. Each component is low: outlier strength is essentially zero (in-block cohesion member), the max
neighbor TSP cost is modest (0.127, the forward Q98→Q99 seam), and the iʿjāz signature magnitude is small
(0.386). Q 98 is NOT a structural-iʿjāz hub (top-10 UAS are Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17). Its
architectural interest is **micro-structural** — the corpus-UNIQUE khayr↔sharr al-bariyya antonym muqābala
(Q098-F-01 Arm C), the al-bariyya hapax-pair (Arm B), and the zero-entropy monorhyme — not
whole-surah-dispersion-extremity. The `abs_outlier = 0.01` field is the direct disk-witness that Q 98 was
indeed in H-NEW-590, settling the overview's data-gap question.

## 7. Lexical counts (computed; `scripts/Q098_F_01_bariyya_antithesis.py` pipeline + close-read scan)

| Quantity | Value | Note |
|:--|:--|:--|
| Verses | 8 | `data/hafs-verse-counts.tsv` line 98 = 8 (variant: al-Qurṭubī *tisʿ āyāt* = 9) |
| Words (marks stripped) | 94 | from `quran-text/quran-no-tashkeel.json` Q 98 |
| Letters (no-tashkeel) | 404 | computed |
| Distinct QAC roots | 42 (60 root-tokens) | `data/morphology/root-index.json` |
| byn (title-root) raw count | 2 | raw-count rank **59/71**; normalized-density rank **6/71** (Q098-F-01 Arm A) |
| al-bariyya (برية, root b-r-ʾ) | 2 occurrences, both Q 98:6, 98:7 | corpus hapax-pair (Q098-F-01 Arm B) |
| Allāh-substring tokens | 3 | coverage 3/8 verses (37.5%) |

## 8. Architectural-type classification

- **Outlier axis (H-NEW-590):** in-block COHESION member of the short-mufaṣṣal {95-101} window
  (delta_pct +0.01, WEAK_OUTLIER label in a near-flat window) — NOT dispersion-extreme.
- **iʿjāz axis (H-NEW-750):** lower-band structural-iʿjāz (sig_A rank 73/114, sig_B rank 88/114), with the
  corpus-FLOOR rhyme entropy (0.0 nats, z = −1.39).
- **UAS (H-NEW-840):** anti-iʿjāz band (rank 93/114).
- **Net:** Q 98 is a **lexically-compact, low-FR, in-block short surah** whose distinctive empirical
  signatures are *micro-structural*: a perfect single-grapheme monorhyme, a corpus-exclusive rhyme-word
  (al-bariyya), and the corpus's tightest single-substitution antonym muqābala (khayr↔sharr). It is the
  micro-structural-interest / low-whole-surah-significance pattern, the same profile seen in Q 66 al-Taḥrīm
  (whose verbatim verse-twin is its micro-feature) and Q 109 al-Kāfirūn.

## 9. Honest limits

- The H-NEW-590 `WEAK_OUTLIER` label for Q 98 is generated inside a near-minimal-dispersion window
  (d_W ≈ 0.47); the label is window-definition-dependent and a different window scheme could re-classify it.
  The delta_pct (+0.01) is the load-bearing figure, not the label.
- The phoneme 4-vector dimension labels are not annotated in `h-new-700.json`; only the raw 4-density
  values are reported, so the per-channel interpretation (emphatic/pharyngeal/sibilant/glottal) is left
  un-assigned to avoid asserting an un-verified mapping.
- FR distances are on QAC-STEM root distributions (not full lemmas or surface tokens); a different
  token-level would shift the neighbor list.
- The 94-word / 404-letter / 42-root counts are under the default rules-tuple (mark-stripped, orthographic
  token, no-tashkeel); a 9-āya counting tradition (al-Qurṭubī) would not change letter/word counts, only
  the fāṣila partition.

## 10. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 98 row; mean 0.8214; nearest Q 108)
- [[h-new-590|H-NEW-590]] — outlier-strength (Q 98 WEAK_OUTLIER, delta_pct +0.01, cohesion member)
- [[h-new-700|H-NEW-700]] — rhyme (perfect ه monorhyme, frac 1.0) + phoneme dispersion-tails
- [[h-new-720|H-NEW-720]] — Q 97→Q 98 low-cost entry (rank 27); Q 98→Q 99 mid-expensive exit (rank 91)
- [[h-new-750|H-NEW-750]] — iʿjāz signature (sig_A rank 73, sig_B rank 88; rhyme entropy 0.0)
- [[h-new-840|H-NEW-840]] — UAS −1.6965 rank 93/114 (anti-iʿjāz band)
- [[h-new-1820|H-NEW-1820]] — title-density independence (Q098-F-01 Arm A corrects the rank-1 summary entry)
- [[h-new-2360|H-NEW-2360]] — antithesis = jadal-overlap (Q098-F-01 Arm D verse-pair-scale replication)

---

*All numerical values traced to on-disk JSON artifacts as cited. Computed 2026-05-30.*
