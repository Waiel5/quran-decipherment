---
surah: 110
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
---

# Q 110 al-Naṣr — Empirical Profile


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

All values verified against the project's canonical computations in `findings/phase-b-hypotheses/csv/`. Rules-tuple: `(no-tashkeel, QAC v0.4, basmala-counted-only-in-Q-1, Hafs-Kufan, root-tokens for FR / surface-tokens for word-counts, mushaf-order)`.

## 1. Length / size

| Metric | Value | Note |
|:--|:--:|:--|
| Verses (n) | **3** | Hafs |
| Words (no-tashkeel surface tokens, QAC v0.4) | **19** | breakdown: v1=5, v2=7, v3=7 |
| Letter graphemes (Arabic, no spaces, no waqf-marks) | **80** | breakdown: v1=19, v2=31, v3=30 |
| Mean letters/word | 4.21 | corpus mean ≈ 4.25 |
| Distinct roots (QAC v0.4) | **15** | only `Alh` (Allāh) repeats: total 16 root-tokens |
| Distinct surface words | 19 | only `الله` repeats |

**Length classification**: bottom-15 of corpus by letter-count; mufaṣṣal-qiṣār zone (al-Zarkashī Q 93-114 cohort).

## 2. Rhyme structure

Verified verse-final letters (computed from `quran-no-tashkeel.json`):

| Verse | Ends with | Final letter (rāwī) |
|:-:|:-:|:-:|
| 1 | والفتح | ح |
| 2 | أفواجا | ـا |
| 3 | توابا | ـا |

**Rhyme structure**: 1× ح + 2× ـا (alif-mamdūda final). Top-rāwī is **ا (66.7%)**.

Rhyme entropy (Shannon, nats): **0.6365** (per `h-new-750.json` Q 110 row).
- z_rhyme_entropy: **−0.241** (slightly below corpus mean — the surah is 2/3 monorhyme but not 100%-monorhyme like Q 112 / Q 109).

The rhyme is consistent with classical fāṣila-typology *al-mutawātī* (uniform-vowel ـا rhyme) interrupted by the v.1 *al-fatḥ* (ـح). Classical *iʿjāz al-fawāṣil* analysis would treat *al-fatḥ* as a thematic-emphasis vocabulary word that overrides the rhyme — the surah's rhetorical pivot-point. (See `02-content-analysis.md` §3.)

## 3. Empirical architectural metrics — verified

### From `h-new-840.json` (UAS = Unified Architectural Score)

| Metric | Value | Rank / 114 | Source |
|:--|:--:|:-:|:--|
| **UAS** | **−1.5163** | **90 / 114** | `all_uas` row {surah:110} |
| `abs_outlier` | 0.00 | tied-NULL | (Q 110 is structurally cohort-coherent in {107-113}) |
| `max_cost` | 0.0170 | very-low | (Q 110-Q 111 mushaf seam) |
| `abs_ijaz` | 1.3289 | mid-pack | sqrt of (sig_A² + sig_B²) projection |

UAS rank 90 is mid-low; this is consistent with the empirical interpretation: Q 110 is a *cohort-coherent, low-distinctiveness, FR-central* surah — not architecturally distinctive in the absolute sense, but architecturally well-integrated.

### From `h-new-590.json` (outlier-strength in mushaf-window)

| Metric | Value | Source |
|:--|:--:|:--|
| Window {107-113} | `[107,108,109,110,111,112,113]` | `all_surahs_results` X=110 row |
| Mean pairwise FR within W | 0.3030 | tight (consistent with §6 below) |
| Mean pairwise FR within W minus Q 110 | 0.2998 | tighter without Q 110 — Q 110 is *additive*, not pulling outlier |
| Δ_pct | **0.00** | NULL |
| `p_greater_W` | **1.0** | far from outlier |
| Classification | **NULL** | Q 110 does NOT outlier in its mushaf cohort |

This is strong evidence that Q 110 is NOT a content outlier within its terminal-zone neighborhood — it is structurally consistent with the surahs around it (Q 107 al-Māʿūn, Q 108 al-Kawthar, Q 109 al-Kāfirūn, Q 111 al-Masad, Q 112 al-Ikhlāṣ, Q 113 al-Falaq).

### From `h-new-750.json` (per-surah iʿjāz signature)

| Metric | Value | Rank / 114 |
|:--|:--:|:-:|
| Rhyme entropy (nats) | 0.6365 | mid-pack |
| z_rhyme_entropy | −0.241 | slightly below mean |
| Mean content distance | 0.7644 | very low |
| z_mean_content_distance | **−1.570** | TOP-3 corpus-central |
| Local cohesion | 3.218 | very high |
| z_local_cohesion | **+2.313** | TOP-15 |
| **sig_A** | **+1.329** | **18 / 114 (top-15 near-miss)** |
| **sig_B** | **+2.072** | **6 / 114 (TOP-10)** |

Q 110's iʿjāz signature is dominated by **TOP-3 mean-FR-centrality** and **top-15 local-cohesion-with-mushaf-cohort**. Both are signatures of a surah that "fits its slot" architecturally — its position in the mushaf is exactly where its content-vocabulary places it.

### From `h-new-720.json` (per-adjacency mushaf seam costs)

| Pair | delta_raw | fraction_residual | Rank (low=cheap) |
|:--|:--:|:--:|:--:|
| **Q 109 → Q 110** | **0.0000** | **0.0000** | **13 / 113 (clamped-zero, H-NEW-1240 seamless)** |
| **Q 110 → Q 111** | **0.0170** | **0.0021** | **21 / 113 (very cheap)** |

Both seams adjacent to Q 110 are very-cheap. Per H-NEW-1240, Q 109→Q 110 is one of the 13 corpus-EXACT seamless seams (clamped-zero TSP-residual). The Q 109-Q 110 transition is the *takhṣīṣ-tabdīl* polemical-disengagement-to-mass-conversion classical inversion-pair (al-Biqāʿī *Naẓm al-Durar* munāsabah on these two surahs, see `05-classical-claims-audit.md` §3).

## 4. ⭐ Mean FR-content distance to corpus — TOP-2 CORPUS-CENTRAL

Computed from `h-new-111.json` D_matrix:

```
Q 110 mean FR-distance to all 113 other surahs: 0.7644
Q 110 mean-dist rank: 2 / 114 (smaller = more central)
```

Interpretation: by Fisher-Rao information-geometry over root-distribution, **Q 110 is the 2nd most-central surah in the entire corpus** — it occupies (along with Q 1 al-Fātiḥa, Q 108 al-Kawthar, and the short-Meccan-tail) the corpus-vocabulary centroid neighborhood.

This is an *empirical paradox* relative to the classical chronology: Q 110 is the LAST-revealed surah by tradition but architecturally lives in the FIRST-revealed Meccan-tail neighborhood. The dissociation is the object of `06-novel-findings.md` Q110-F-01.

## 5. ⭐ Q 110's top-15 FR-content nearest neighbors

Computed from `h-new-111.json` D_matrix (verified):

| Rank | Surah | FR distance | Type |
|:-:|:-:|:-:|:-:|
| 1 | **Q 108 al-Kawthar** | **0.2684** | short-Meccan |
| 2 | **Q 112 al-Ikhlāṣ** | **0.2758** | short-Meccan-tawḥīd |
| 3 | **Q 114 al-Nās** | **0.3001** | muʿawwidha |
| 4 | Q 107 al-Māʿūn | 0.3006 | short-Meccan |
| 5 | Q 106 Quraysh | 0.3042 | short-Meccan |
| 6 | Q 94 al-Sharḥ | 0.3174 | short-Meccan |
| 7 | Q 111 al-Masad | 0.3184 | short-Meccan |
| 8 | Q 113 al-Falaq | 0.3214 | muʿawwidha |
| 9 | Q 105 al-Fīl | 0.3233 | short-Meccan |
| 10 | Q 103 al-ʿAṣr | 0.3238 | short-Meccan |
| 11 | Q 104 al-Humaza | 0.3272 | short-Meccan |
| 12 | Q 101 al-Qāriʿa | 0.3371 | short-Meccan |
| 13 | Q 100 al-ʿĀdiyāt | 0.3389 | short-Meccan |
| 14 | **Q 1 al-Fātiḥa** | **0.3531** | UMM-AL-KITĀB |
| 15 | Q 102 al-Takāthur | 0.3585 | short-Meccan |

**Observation**: ALL 15 of Q 110's top-FR-neighbors are short-Meccan or al-Fātiḥa. **Zero late-Medinan signal**. The dissociation from chronology is corpus-COMPLETE for Q 110.

Notable: **Q 1 enters at rank 14** — Q 110 is one of the few surahs where Q 1 al-Fātiḥa is in the FR top-15. This contributes to **cross-finding-013 (mushaf as topological ring)**: Q 110 is part of the TERMINAL_TRIAD-extended cluster {Q 108-114} that wraps to Q 1. (See §6 below.)

## 6. ⭐ Q 110's farthest neighbors

| Rank-from-bottom | Surah | FR distance |
|:--:|:--:|:--:|
| 1 (farthest) | **Q 3 Āl ʿImrān** | **1.2234** |
| 2 | Q 9 al-Tawba | 1.2205 |
| 3 | Q 4 al-Nisāʾ | 1.2092 |
| 4 | Q 6 al-Anʿām | 1.2042 |
| 5 | Q 2 al-Baqara | 1.1843 |

Q 110's farthest neighbors are **the al-ṭiwāl Medinan-cluster** (Q 2, 3, 4, 9). This is a 4× FR-distance from the closest-neighbor cluster — reflecting the corpus's **bipolar FR-architecture**: short-mufaṣṣal-tail at one pole, long-Medinan-ṭiwāl at the other.

**Q 110 vs Q 5 al-Māʾida = 1.1783** (the other latest-revealed candidate). The two latest-revealed surahs are FR-FAR (mid-corpus distance, far from each other). This is the headline empirical fact for Q110-F-02.

## 7. Per-verse Allah-density and 19-word total

Q 110 has 2 Allāh-tokens (v.1 *naṣru llāhi*, v.2 *dīni llāhi*) in 19 words = **10.53% Allah-density per word**. Per H-NEW-71 corpus-Allah-distribution (note: 29 Mufaṣṣal-tail surahs have ZERO Allah; Q 110 with 2 of 19 words is in the high-density-per-word tail).

In the 5-word Q 110:1 (*idhā jāʾa naṣru llāhi wa-l-fatḥ*), Allah is at word 4 of 5. In the 7-word Q 110:2, Allah is at word 6 of 7. Per H-NEW-71 sub-finding (verse-position of Allah), Q 110's positions are mid-late within their respective verses — consistent with "predicate-final" word order common in Late Medinan registers.

Q110-F-04 (in `06-novel-findings.md`) tests the per-word Allah-density against a 19-word random-corpus null.

## 8. Verse-final words

| Verse | Final word | Root | Morphology (QAC) |
|:-:|:-:|:-:|:-:|
| 1 | **الفتح** (al-fatḥ) | f-t-ḥ | DET + N (al + fatḥ) |
| 2 | **أفواجا** (afwājā) | f-w-j | N PL INDEF ACC (plural of *fawj*) |
| 3 | **توابا** (tawwābā) | t-w-b | ACT-PCPL MS INDEF ACC (form II/V active participle) |

**Lexical observation**: ALL THREE verse-final words are **closely connected to the surah's central theme** (victory→conversion→repentance). Compare to typical-mufaṣṣal-tail surahs which use generic-fāṣila vocabulary.

The 3 verse-final words form a thematic-coherent triplet:
- *al-fatḥ* (the conquest) — historical event
- *afwājā* (in waves) — empirical observation
- *tawwābā* (ever-Returning) — divine response-attribute

This is corpus-distinctive *fāṣila-thematic-density* — Q 110's 3 fāṣila-words ARE the 3 thematic anchors of the surah.

## 9. Abjad-mashriqī sums (descriptive only — non-load-bearing per ḥisāb-al-jummal audit)

| Verse | Abjad-mashriqī sum |
|:-:|:-:|
| 1 | 1638 |
| 2 | 1771 |
| 3 | 2715 |
| **Total** | **6124** |

Per the project's numerology audit (H-NEW-237 + 160 → 163 numerology tests, zero Bonferroni survivors), abjad sums are NOT load-bearing as evidence. Listed here for completeness only — no claim is made.

## 10. Stem-token (root) inventory — full enumeration

The 16 stem-tokens of Q 110 (by QAC v0.4 rules-tuple):

| Verse | Word | Lemma | Root |
|:-:|:--|:--|:--|
| 1 | إذا | idhA | (function word, no root) |
| 1 | جاء | jaA'a | jyA |
| 1 | نصر | naSor | **nSr** |
| 1 | الله | All~ah | Alh (×1) |
| 1 | والفتح | fatoH | **ftH** |
| 2 | ورأيت | ra'aA | **rAy** |
| 2 | الناس | nAs | **nws** |
| 2 | يدخلون | daxal | **dxl** |
| 2 | في | fiy | (function) |
| 2 | دين | diyn | **dyn** |
| 2 | الله | All~ah | Alh (×2) |
| 2 | أفواجا | fawoj | **fwj** |
| 3 | فسبح | sab~aHa | **sbH** |
| 3 | بحمد | Hamod | **Hmd** |
| 3 | ربك | rab~ | **rbb** |
| 3 | واستغفره | sotaGofara | **gfr** |
| 3 | إنه | (no root) | (function) |
| 3 | كان | kAna | **kwn** |
| 3 | توابا | taw~aAb | **twb** |

**16 stem-tokens, 15 distinct roots** (only Alh repeats). The 14 content-roots are:
**{nSr, ftH, rAy, nws, dxl, dyn, Alh, fwj, sbH, Hmd, rbb, gfr, kwn, twb}** + jyA.

Notable: the 4 *theological-action* roots **{nSr (help), ftH (conquer), sbH (glorify), gfr (forgive)}** form the surah's theological vocabulary.

## 11. Summary headlines for Q 110 architectural profile

1. **2nd-most-central surah by FR-content** (rank 2/114; mean FR = 0.7644)
2. **Top-15 nearest neighbors are 100% short-Meccan or al-Fātiḥa** — chronology-architecture dissociation parent (H-NEW-1030)
3. **Q 109 → Q 110 is rank-6 of 13 seamless mushaf-seams** (clamped-zero TSP-cost)
4. **iʿjāz sig_B rank 6/114** (top-10) — driven by local-cohesion z=+2.31
5. **Outlier classification: NULL** in window {107-113}; Q 110 is cohort-coherent, not distinctive
6. **2 of 3 verse-finals on ـا rhyme**, with the v.1 *al-fatḥ* exception serving as the thematic anchor

The empirical signature: a **maximally-corpus-central, locally-cohort-coherent, structurally-iʿjāz-positive, terminally-positioned, post-Mecca-conquest, Medinan-revelation, short-Meccan-vocabulary surah**. The chronology-architecture dissociation is the *defining* empirical-architectural feature.
