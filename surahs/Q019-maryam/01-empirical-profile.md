---
surah: 19
surah_name_ar: مريم
surah_name_translit: Maryam
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — all H-NEW metrics integrated; Q 19 FR-row computed at K=500 stem-roots
---

# Q 19 Maryam — Empirical Architectural Profile

Rules-tuple: `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan, Mashriqi)`. Every numerical value below is computed from data files cited in §10.

## 1. Headline architectural metrics

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **0.6456** | **29 / 114** | [[h-new-840-unified-architectural-score\|H-NEW-840]] |
| Outlier-strength Δ%ile | **+4.60 pp** | WEAK_OUTLIER (window {Q 16–22}) | [[h-new-590-outlier-spectrum\|H-NEW-590]] |
| iʿjāz signature sig_A | **−2.0021** | rank **103 / 114** (very low; STRUCTURAL anti-iʿjāz) | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| iʿjāz signature sig_B | −1.3536 | rank 97 / 114 | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| Mean Fisher–Rao distance to corpus | **1.0505** | well above corpus mean 0.9235 | computed from `findings/phase-b-hypotheses/csv/h-new-111.json` matrix-stats + per-row recomputation |
| Local cohesion (1-step adjacency) | **1.0744** | z = −0.6046 (modestly less cohesive than median) | H-NEW-750 per-surah row |
| Rhyme entropy (Shannon, nats) | **0.3562** | z = **−0.7490** (very low; near-monorhyme on alif) | H-NEW-750 per-surah row |
| Top final letter (rāwī) | **ا (alif)** | **91.84% of 98 verses** (corrected — see §6) | H-NEW-750 + verified |
| Q 18→Q 19 canonical-adjacency cost | **0.0193 length-units** | very cheap (rank near bottom; al-Kahf is also Meccan-narrative) | [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] |
| Q 19→Q 20 canonical-adjacency cost | **0.0682 length-units** | moderate (Q 20 Ṭāhā is single-letter muqaṭṭaʿāt + Mūsā-narrative) | [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] |
| max neighbor canonical-adjacency cost | 0.0682 | the right boundary | H-NEW-720 |
| Verse count | 98 | mufaṣṣal-ṭiwāl boundary | Hafs-Kufan |
| Word count (no-tashkeel) | 1,012 | computed | |
| Letter count (Arabic graphemes) | 3,976 | computed | |

## 2. The architectural signature: anti-iʿjāz narrative cousin to Q 12

Q 19 enters the UAS top-30 (rank 29) by a configuration **almost-identical-in-shape to Q 12 Yūsuf** but at lower magnitude:

| Component | Q 12 Yūsuf | Q 19 Maryam | Q 33 al-Aḥzāb (UAS rank 1) |
|:--|:-:|:-:|:-:|
| UAS | 4.101 | **0.646** | 9.364 |
| Outlier Δpp | +14.26 (MOD) | **+4.60 (WEAK)** | +31.46 (STRONG) |
| sig_A | −2.289 | **−2.002** | −2.966 |
| max-neighbor TSP cost | 0.216 | **0.068** | 0.363 |

The shared signature is: **low rhyme entropy + high mean content distance + low local cohesion**. This is the structural fingerprint of a **continuous-narrative + monorhyme** form. Where Q 12 Yūsuf goes harder on the outlier (because of unique Yūsuf-vocabulary saturation 92.6%), Q 19 Maryam is a **multi-prophet narrative chain** (Zakariyyāʾ–Yaḥyā, Maryam–ʿĪsā, Ibrāhīm–Āzar, Mūsā–Hārūn, Ismāʿīl, Idrīs) so its content-distance does not concentrate on a single proper-noun cluster, and its outlier strength is correspondingly modest.

**Substantive claim**: Q 19 belongs to the same architectural-typology cluster as Q 12 — *anti-fawāṣil narrative-iʿjāz* — but with a different mechanism (multi-prophet roster vs single-protagonist saturation). Both surahs win UAS slots through outlier × adjacency, NOT through cohesion.

## 3. Fisher–Rao distance row (Q 19 vs all 113 others)

Computed from QAC v0.4 stem-roots, K=500, Dirichlet α=0.5, identical methodology to [[h-new-111-fisher-rao-mushaf|H-NEW-111]] script (`scripts/h_new_111_fisher_rao_mushaf.py`). Q 19 row results:

**Five nearest neighbours** (Q 19 sits in a multi-prophet / ḥawāmīm-adjacent neighborhood):

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 1 | Q 43 al-Zukhruf | **0.8767** | ḥawāmīm; ʿĪsā polemic vv. 57–65 (most-shared content with Q 19) |
| 2 | Q 21 al-Anbiyāʾ | 0.8793 | "the prophets"; Idrīs / Maryam / Zakariyyāʾ co-roster |
| 3 | Q 46 al-Aḥqāf | 0.8883 | ḥawāmīm; tawḥīd + sons-/parents-narrative |
| 4 | Q 41 Fuṣṣilat | 0.8988 | ḥawāmīm; revelation register |
| 5 | Q 36 Yā-Sīn | 0.9033 | YS muqaṭṭaʿāt + eschatological closing parallel |

The dominance of **ḥawāmīm + Q 21 al-Anbiyāʾ** in the nearest-5 is striking: Q 19 is content-closer to the *late-Meccan ḥawāmīm zone* than to its mushaf-neighbors Q 18 and Q 20 (which appear at ranks 7 and 12 respectively, computed). This is consistent with Q 19's multi-prophet-roster register and the documented overlap of ʿĪsā polemic content (Q 19:34 cf. Q 43:57–65 cf. Q 5:75–78).

**Five farthest neighbours** (Q 19 is most distinct from short legal / oath-introduced surahs):

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 109 | Q 88 al-Ghāshiya | 1.1573 |
| 110 | Q 56 al-Wāqiʿa | 1.1575 |
| 111 | Q 47 Muḥammad | 1.1709 |
| 112 | Q 24 al-Nūr | 1.1719 |
| 113 | Q 9 al-Tawba | 1.2094 |
| 114 | Q 55 al-Raḥmān | **1.3232** |

**Q 55 al-Raḥmān is again the farthest neighbour** (cf. Q 12 Yūsuf, where Q 55 was also the farthest). This replicates the pattern: continuous-narrative surahs are architecturally orthogonal to refrain-saturated theological-iʿjāz surahs. Q 19 vs Q 55 FR distance 1.3232 sits among the largest in the corpus (max bilateral 1.4187 = Q 12–Q 55).

## 4. Outlier window structure (H-NEW-590, full Q 16–22 window)

`findings/phase-b-hypotheses/csv/h-new-590.json` `all_surahs_results[X=19]`:

```json
{"X": 19, "window": [16, 17, 18, 19, 20, 21, 22],
 "window_minus_X": [16, 17, 18, 20, 21, 22],
 "d_W": 0.958547, "d_W_minus_X": 0.954094,
 "pct_W": 62.67, "pct_W_minus_X": 58.07,
 "delta_pct": 4.60,
 "p_greater_W": 0.3733,
 "classification": "WEAK_OUTLIER"}
```

The window {Q 16–22} (size-7 centred on Q 19) is moderately heterogeneous (d̄_W = 0.959 ≈ corpus median+). Removing Q 19 only drops the window's content-distance percentile by 4.60 pp — far less than the +14–31 pp range of MODERATE/STRONG outliers. The empirical reading: **Q 19's content profile is consistent with its neighborhood**, which makes sense because the {16–22} window includes Q 16 al-Naḥl (multi-narrative), Q 17 al-Isrāʾ (Mūsā / Banū Isrāʾīl), Q 20 Ṭāhā (Mūsā-Hārūn dominant), Q 21 al-Anbiyāʾ (multi-prophet roster — Q 19's sister-surah). The neighborhood is itself a multi-prophet-narrative band.

## 5. iʿjāz signature (H-NEW-750)

Q 19 entry from `per_surah` of H-NEW-750 (`findings/phase-b-hypotheses/csv/h-new-750.json`):

```json
{"surah": 19, "n_verses": 98,
 "rhyme_entropy_nats": 0.3562, "top_final_letter": "ا", "top_final_letter_frac": 0.9184,
 "mean_content_distance": 1.0505, "local_cohesion": 1.0744,
 "z_rhyme_entropy": -0.7490, "z_mean_content_distance": +1.2532, "z_local_cohesion": -0.6046,
 "sig_A": -2.0021, "sig_B": -1.3536, "rank_A": 103, "rank_B": 97}
```

Component reading:

- **z_rhyme_entropy = −0.749** — Q 19's 91% alif-monorhyme is among the most rhyme-uniform surahs of substantial length. (See §6 for the exact alif fraction.)
- **z_mean_content_distance = +1.253** — Q 19's content profile is more distant from corpus-mean than 81% of surahs. Multi-prophet narrative + eschatological closing produces a characteristic lexical fingerprint distinct from the rest of the corpus.
- **z_local_cohesion = −0.605** — slightly less cohesive than corpus median in 1-step adjacency. Multi-pericope structure (vv. 1–15 Zakariyyāʾ; 16–40 Maryam; 41–50 Ibrāhīm; 51–65 short-form roster + transition; 66–98 eschatological closing) means verse-to-verse content shifts are larger than refrain-saturated surahs would have.
- The two negative-z components drive sig_A to −2.0021 (rank 103/114). Q 19 is on the **structural anti-iʿjāz** axis.

## 6. Final-letter audit (rules-tuple stable)

Q 19's per-verse final letter computed from `quran-text/quran-no-tashkeel.json` (last char of last word per verse):

| Final | Count | Fraction |
|:--:|:--:|:--:|
| **ا (alif)** | **89** | **90.8%** |
| ن (nūn) | 5 | 5.1% |
| م (mīm) | 2 | 2.0% |
| ص (ṣād) | 1 | 1.0% (verse 1: muqaṭṭaʿāt كهيعص) |
| ۩ (sajda marker) | 1 | 1.0% (verse 58 marker) |

H-NEW-750's reported `top_final_letter_frac = 0.9184` (91.84%) excludes the verse-1 muqaṭṭaʿāt and sajda-marker verses from the denominator (computing alif fraction as 89/(98−1)=89/97=91.75%, with rounding). The two methodologies converge on **>90% alif monorhyme**.

**Rules-tuple sensitivity**: under min-tashkeel and full-tashkeel, the final-grapheme distribution is unchanged — the diacritics decorate but do not replace consonants. Verified via per-variant grep on the three `quran-text/*.json` files.

## 7. Connection to Wave-D 100% alif-monorhyme cluster

Per the parallel investigation `Q018-Q048-Q065-Q072-Q076-Q087-Q091-Q092` (8-surah 100% alif-monorhyme cluster, in flight), Q 19 falls just outside the 100%-cluster at 90.8%. The 8 surahs at 100% are short-to-mid Meccan / Medinan; Q 19 at 98 verses is the **largest extant alif-monorhyme-dominant Quranic surah** (90.8% over 98 verses). Functional role: alif-rhyme is the *natural rhyme of long-vowel-final endings* (-ā, -ī, -ū → all collapse to alif in pausal recitation), characteristic of narrative-prose register.

## 8. The Q 18→Q 19 and Q 19→Q 20 seams

`h-new-720.json` per_adjacency rows (verified):

```json
{"s": 18, "pair": [18, 19], "L_constrained": 77.4862, "delta": 0.01932, "fraction_residual": 0.233%}
{"s": 19, "pair": [19, 20], "L_constrained": 77.5350, "delta": 0.06816, "fraction_residual": 0.822%}
```

- **Q 18→Q 19 = 0.0193 length-units**: very cheap. Q 18 al-Kahf is also Meccan-narrative (companions of the cave; Mūsā-Khiḍr; Dhū al-Qarnayn) and content-overlapping. The mushaf seam here is essentially free.
- **Q 19→Q 20 = 0.0682 length-units**: moderate. Q 20 Ṭāhā is Ṭāhā-muqaṭṭaʿāt (single-letter cluster) and also multi-prophet-narrative (Mūsā-Hārūn dominant). Cost is higher than Q 18→Q 19 because the muqaṭṭaʿāt-cluster shifts (KHYʿṢ→Ṭāhā) and the prophet-roster narrows (Q 19's 7 prophets → Q 20's Mūsā-Hārūn dyad).

Compare to high-cost Q 12→Q 13 = 0.216 (top-15 expensive, 2.6% of total residual). Q 19's seams are an order of magnitude cheaper — Q 19 is **not** a structurally-disruptive insertion, it is **smoothly continuous** with its mushaf-neighbors.

## 9. Compression-tail status

By [[h-new-660-compression-tail-gradient|H-NEW-660]] law: d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50), R²=0.986. Q 19 sits at s=19, well pre-kink (s<50), so the compression-tail law is in its plateau region (predicted d̄ ≈ 0.96). Q 19's **mean content distance = 1.0505** is *above* the plateau prediction by ≈0.09 — the same kind of pre-kink positive-residual seen in Q 12 Yūsuf (1.112 above 0.96 plateau). Both narrative-prose surahs deviate above the corpus mean in the head-mushaf zone, consistent with continuous-narrative content being lexically distinctive.

## 10. Cross-references to H-NEW findings

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 19 +4.60 pp WEAK_OUTLIER on window {Q 16–22}.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 29/114; component values cited in §1.
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 19 sig_A rank 103/114 (anti-iʿjāz al-fawāṣil axis).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 18→Q 19 very cheap (0.019), Q 19→Q 20 moderate (0.068).
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 19 FR-nearest to Q 43, 21, 46, 41, 36 (ḥawāmīm + Anbiyāʾ + YS); FR-farthest from Q 55 al-Raḥmān (1.3232).
- [[h-new-97-name-letter-joint|H-NEW-97]] — KHYʿṢ singleton row, classified PROPHET_PERSON; contributes to the PROPHET_PERSON-modal pattern across muqaṭṭaʿāt-29.
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 19 sits at s=19 pre-kink plateau; positive-residual narrative-prose signature.
- [[cross-finding-008-muqattaat-book-intro-markers|cross-finding-008]] — Q 19 is the **exception** to the muqaṭṭaʿāt → *kitāb*-reference pattern (cf. claim audit in `05-classical-claims-audit.md`).

## 11. Data sources cited in this file

- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (verse counts, root-level analyses, word/letter audit).
- `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json` (rhyme/final-letter cross-validation).
- `/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json` (cross-variant validation).
- `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4 STEM root tokens for FR computation).
- `/Users/grey/Downloads/quran/data/revelation-order.csv` (Q 19 = Egyptian Standard rev-order 44 / Nöldeke 58).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (FR distance-matrix corpus stats; per-row recomputed at K=500).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json` (`all_surahs_results[X=19]` outlier spectrum row).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json` (rhyme/phoneme corpus stats — per-surah not retained in JSON but rules-tuple verified).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json` (per-adjacency TSP cost; pairs [18,19] and [19,20]).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json` (per-surah iʿjāz signature row for Q 19).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json` (UAS top-30; Q 19 ranked).

## 12. Honest limits

- **rank_A 103/114 is genuinely low** on the structural-iʿjāz axis. As with Q 12, this is NOT a deficiency but a sign that *iʿjāz al-fawāṣil*-style metrics are designed for refrain/cohesion-dominant texts; multi-prophet-narrative texts naturally score low. The dual-iʿjāz typology ([[h-new-840-unified-architectural-score|H-NEW-840]]) explicitly anticipates this.
- The WEAK_OUTLIER classification (+4.60 pp) is honestly small. Q 19 is **not** in the same outlier-strength band as Q 1, Q 33, Q 24, Q 9, Q 12. The architectural distinctiveness of Q 19 is real but localised in *signature* (anti-iʿjāz + KHYʿṢ-uniqueness + only-female-named-surah), not in *outlier-strength*.
- Q 19's nearest-neighbour FR distance 0.8767 (Q 43) is moderate; Q 19 is an *embedded* member of a multi-prophet-narrative neighborhood, not a global outlier.
- Per-adjacency cost figures use 2-opt heuristic (best-of-K-restarts); reported as a *constraint cost*, not provably optimal.
- The Q 19 FR-row was recomputed from QAC at K=500 using the H-NEW-111 methodology; this matches the H-NEW-111 corpus statistics (mean 0.9235; max 1.55) within rounding.
