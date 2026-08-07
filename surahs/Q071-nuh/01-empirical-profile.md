---
surah: 71
surah_name_ar: نوح
surah_name_translit: Nūḥ
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: "Q 71 = short alif-monorhyme Meccan petition-narrative; mid-low architectural significance (UAS rank 84/114); FR-peripheral to its own narrative cycle."
---

# Q 71 Nūḥ — Empirical Profile


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

All values are read from on-disk artifacts and cited by file + key. Rules-tuple
(default): `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1,
Hafs-Kūfan, Mashriqi)`. Root analysis uses QAC v0.4 ROOT.

## 1. Size and composition

| Metric | Value | Source |
|---|---|---|
| Verses | 28 | `data/hafs-verse-counts.tsv` line 71 |
| Words (no-tashkeel, waqf stripped) | 227 | computed (`scripts/Q071_F_01_nuh_cycle_centroid.py` pipeline) |
| Letters (no-tashkeel, excl. spaces) | 965 | computed |
| QAC morphological segments | 380 | `data/morphology/quranic-corpus-morphology-0.4.txt` (s==71) |
| Distinct QAC roots | 87 | same |
| Mean letters/word | 4.25 | 965 / 227 |
| Mean words/verse | 8.11 | 227 / 28 |

Q 71 is a short, dense surah: 87 unique roots in 28 verses gives high root-density
per verse, but its absolute root-mass (87) is small relative to the long surahs that
host the other Nūḥ pericopes (Q 11:25-49 alone = 124 roots).

## 2. Fisher-Rao distance profile (H-NEW-111)

Source: `findings/phase-b-hypotheses/csv/h-new-111.json`, key `D_matrix_upper_triangular`
(stored as `[surah_i, surah_j, distance]` triples, 1-based).

| Metric | Value |
|---|---|
| FR mean to all 113 surahs | **0.8793** |
| (cross-check) `h-new-750.json` `mean_content_distance` | 0.87925 (agrees) |
| Top-3 nearest | Q 112 (0.6954), Q 110 (0.7000), Q 91 (0.7059) |
| Top-5 nearest | + Q 105 (0.7157), Q 63 (0.7260) |
| Top-3 farthest | Q 9 (1.1481), Q 55 (1.1334), Q 4 (1.1296) |

**Key structural fact — the Nūḥ-host surahs are FAR from Q 71:**

| Host surah | FR distance | Rank in Q 71's 113-list |
|---|---|---|
| Q 7 al-Aʿrāf | 1.0014 | 93/113 |
| Q 11 Hūd | 1.0141 | 94/113 |
| Q 23 al-Muʾminūn | 0.9314 | 79/113 |
| Q 26 al-Shuʿarāʾ | 1.0650 | 102/113 |
| Q 54 al-Qamar | 0.9597 | 87/113 |

At whole-surah scale the cycle is INVISIBLE — Q 71 sits near short creedal Meccan
surahs, not near the long mixed-genre surahs that contain its own story. This is the
whole-surah-scale corroboration of the Q071-F-01 centroid NULL (the cycle only
appears when you zoom to pericope scale, per H-NEW-2260).

## 3. Canonical-adjacency cost (H-NEW-720)

Source: `findings/phase-b-hypotheses/csv/h-new-720.json`, key `per_adjacency`.

| Seam | delta_raw | fraction_residual | ascending-rank (1=cheapest) |
|---|---|---|---|
| Q 70 → Q 71 | +0.17597 | 0.02122 | **96/113 (relatively expensive)** |
| Q 71 → Q 72 | +0.04082 | 0.00492 | 40/113 (mid-cheap) |

The Q 70→71 joint is one of the more expensive consecutive seams (rank 96/113):
Q 70 al-Maʿārij (Early Meccan, eschatological *sāʾala sāʾilun*) → Q 71 Nūḥ (Middle
Meccan, dedicated narrative) crosses a Nöldeke phase boundary (#42 → #51). The
Q 71→72 joint (to al-Jinn, Middle Meccan #62) is far smoother — an intra-phase seam.

## 4. iʿjāz signature (H-NEW-750)

Source: `findings/phase-b-hypotheses/csv/h-new-750.json`, key `per_surah` (surah==71).

| Component | Value | Rank |
|---|---|---|
| sig_A (structural-fawāṣil signature) | −0.0694 | 64/114 |
| sig_B | −0.9128 | 77/114 |
| rhyme_entropy_nats | 0.4904 | (z = −0.506) |
| top_final_letter | ا (alif) | frac 0.8571 (24/28 verses) |
| mean_content_distance | 0.87925 | (z = −0.437) |
| local_cohesion | 1.21962 | (z = −0.407) |

Q 71 is a strong **alif-monorhyme** surah: 24 of 28 verses end in long-ā
(…-ārā / …-āran patterns: *alīmā*, *mubīnā*, *firārā*, *isrārā*, *ghaffārā*,
*midrārā*, *anhārā*, *waqārā*, *aṭwārā*, *sirājā*, *nabātā*, *ikhrājā*, *fijājā*,
*kibārā*, *kubbārā*, *ḍalālā*, *anṣārā*, *diyārā*, *kaffārā*, *tabārā* …). The low
rhyme entropy (0.49 nats, z = −0.51) reflects this monorhyme dominance. The negative
sig_B (rank 77/114) places Q 71 in the lower-middle band of the structural-iʿjāz
spectrum — consistent with a short narrative surah rather than a fawāṣil-virtuosic
one.

## 5. Unified Architectural Significance (H-NEW-840)

Source: `findings/phase-b-hypotheses/csv/h-new-840.json`, key `all_uas` (surah==71).

| Component | Value |
|---|---|
| UAS | **−1.3242 (rank 84/114)** |
| abs_outlier | 1.8200 |
| max_cost | 0.17597 (= the Q 70→71 seam) |
| abs_ijaz | 0.06937 (= |sig_A|) |

Q 71 is a **mid-low UAS surah** (rank 84/114). It is neither a structural-iʿjāz hub
(top UAS: Q 33, 1, 2, 9 …) nor an extreme theological-iʿjāz minimal surah (bottom
UAS: Q 112, 114 …). Its architectural significance is dominated by its abs_outlier
component (1.82), not by its iʿjāz signature.

## 6. Outlier-strength (H-NEW-590) — DATA GAP

Source: `findings/phase-b-hypotheses/csv/h-new-590.json`, key `candidates`.

H-NEW-590 tested only 6 candidate surahs: {1, 9, 18, 55, 62, 112}. **Q 71 was not a
tested candidate**, so there is NO H-NEW-590 Δ%ile value for Q 71. Flagged as
NULL-DATA-GAP per the anti-hallucination rule; the abs_outlier=1.82 value in
H-NEW-840 is the closest available outlier proxy.

## 7. Position in the compression-tail laws (Wave 2026-04-28)

Q 71 (s=71) sits in the mufaṣṣal tail (s>50), where the architectural laws predict:
- d̄_content(71) ≈ 0.96 − 0.012·(71−50) = 0.96 − 0.252 = **0.708** (law prediction).
- Observed FR-mean = 0.8793. The observed value sits ABOVE the content-tail
  prediction — Q 71 is more content-distinctive (FR-distant) than the smooth tail
  law would forecast at s=71, consistent with its dedicated single-prophet
  vocabulary (the five idols, cosmological signs). This is a per-surah residual
  observation, not a re-derivation of the law.
- d̄_rhyme(71) ≈ 0.36 + 0.0041·(71−50) = **0.446** (rhyme-tail law); Q 71's strong
  alif-monorhyme (entropy 0.49 nats) is consistent with the dispersion regime.

## 8. Root inventory highlights (QAC v0.4)

The conserved Nūḥ-cycle flood-core roots present in Q 71 (from the H-NEW-2260 shared
sets and verified here): `grq` (غرق, drowning, v 25), `qwm` (قوم, the people),
`rsl` (رسل, sent), `rbb` (ربّ, Lord — petition vocative), `Ebd` (عبد, worship),
`gfr` (غفر, forgiveness, vv 7,10,28), `nSr` (نصر, helpers/Nasr-idol homograph),
`Dll` (ضلل, going astray). Notably **ABSENT** from Q 71: `flk` (فلك, ark) and `njw`
(نجو, deliverance) — the two roots that most tightly bind the SHORT retellings
(Q 7, 11, 23, 26) to each other. Q 71 narrates the drowning (`grq`) but never names
the ark or the act of salvation — a lexical reason it is peripheral to its own cycle
(see `06-novel-findings.md` Q071-F-01).

## 9. Cross-references

- [[h-new-2260-prophet-cycle-pericope|H-NEW-2260]] — Nūḥ cycle PASS; Q 71 least-central pericope.
- [[h-new-111|H-NEW-111]] — FR matrix (Q 71 row).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 70→71 expensive, Q 71→72 mid.
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A/sig_B, alif-monorhyme.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 84/114.
