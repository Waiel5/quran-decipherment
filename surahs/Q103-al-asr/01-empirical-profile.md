---
surah: 103
surah_name_ar: العصر
surah_name_translit: al-ʿAṣr
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -720 / -750 / -840 / -2210 / -2340 (all values cited to path)
---

# Q 103 al-ʿAṣr — Empirical Profile


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
Q 103 is surah-id 103; in the 1-indexed Fisher-Rao matrix it is index 103; in the 0-indexed
text list (`quran-text/quran-no-tashkeel.json`) it is index 102.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`, 6441 pairs),
1-indexed surah IDs. Corpus matrix stats: min 0.2127, max 1.5509, mean 0.9235, median 0.9567.

| Quantity | Value |
|:--|:--|
| Q 103 mean FR to all 113 surahs | **0.787** (far below corpus mean 0.9235) |
| Nearest neighbor | **Q 108 al-Kawthar** at FR **0.2399** (rank 1) |
| Top-15 FR neighbors | Q 108 (0.240), Q 106 (0.263), Q 111 (0.280), Q 112 (0.291), Q 94 (0.293), Q 95 (0.297), Q 113 (0.298), Q 107 (0.299), Q 100 (0.311), Q 104 (0.312), Q 105 (0.312), Q 110 (0.324), Q 101 (0.334), Q 114 (0.338), Q 102 (0.345) |
| 5 farthest | Q 2 (1.239), Q 6 (1.245), Q 4 (1.270), Q 9 (1.281), Q 3 (1.288) |

**Reading.** Q 103's FR neighborhood is **the entire short-Meccan mufaṣṣal-qiṣār tail** — its top-15
neighbours are Q 94-114 almost without exception (al-Kawthar, Quraysh, al-Masad, al-Ikhlāṣ, al-Sharḥ,
al-Tīn, al-Falaq, al-Māʿūn, al-ʿĀdiyāt, al-Humaza, al-Fīl, al-Naṣr, al-Qāriʿa, al-Nās, al-Takāthur). All
fifteen lie below FR 0.345 — a tight cluster of short Allāh/judgment-dense surahs. The 5 farthest are
the long Medinan surahs (Q 2, 3, 4, 9) plus Q 6 al-Anʿām — the maximal lexical-distribution contrast.
Q 103's mean FR of 0.787 reflects membership in the densest, most-self-similar corner of the corpus.

**Minimal-surah neighbours (the three 3-verse surahs):**

| 3-verse surah | Rank in Q 103's FR list | FR to Q 103 | rā'-monorhyme? |
|:--|:--|:--|:--|
| Q 108 al-Kawthar | **1 / 113** | **0.2399** | YES (Arm A) |
| Q 110 al-Naṣr | 12 / 113 | 0.3238 | NO (ح/ا/ا finals) |

Q 108 is Q 103's single closest surah; Q 110 (also 3 verses, but NOT a rā'-monorhyme) is rank 12. The
minimal-surah twin is specifically the **rā'-rhyming pair {103, 108}**, not the whole 3-verse cohort
(Q103-F-01 Arm A). Note the reciprocal is asymmetric: Q 103 is only rank 6 in Q 108's FR list (Q 108's
own nearest neighbour is Q 106 al-Quraysh at 0.2127), so this is a one-directional rank-1 tie.

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

| Quantity | Value |
|:--|:--|
| Window (centered on Q 103) | {Q 100, 101, 102, 103, 104, 105, 106} |
| d̄_W (window with Q 103) | 0.3302 |
| d̄_W−X (window without Q 103) | 0.3371 |
| pct_W | 0.0 |
| pct_W−X | 0.0 |
| **delta_pct** | **0.0** |
| p_greater_W | 1.0 |
| **classification** | **NULL** |

**Reading.** The window {100-106} is one of the *most cohesive content-neighbourhoods in the entire
corpus* — d̄_W = 0.330 (vs corpus mean 0.9235), so its percentile is pinned at 0.0. Removing Q 103
changes nothing (delta_pct = 0.0); Q 103 is a perfect **cohesion member**, not an outlier. This is the
short-Meccan mufaṣṣal block where every surah is near every other surah in root-distribution. Contrast
Q 1 (+27.09pp STRONG_OUTLIER): Q 103 is the opposite — maximally "in-block."

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, Q 103): top final-letter **ر (rā')**, fraction **1.0** (3/3 verses)
— a **perfect monorhyme**. Project rhyme dispersion-tail law fitted as two-piece-kink-50 (primary_r2
0.7886); Q 103 (s=103 > 50) sits deep in the dispersing tail of the law, yet is itself a *tight*
monorhyme — a reminder that the law is a *mean* gradient, not a per-surah determinant. Only 15 of 114
surahs are perfect monorhymes (rhyme_entropy 0.0); Q 103 is one, and shares its rā' final with Q 54,
Q 97, and Q 108.

**Phoneme** (phoneme_vectors index 102, 4-dim density vector):
`[0.06849, 0.05479, 0.09589, 0.05479]`. The **3rd component (0.0959) is the largest** — and it equals
the H-NEW-2340 heavy-istiʿlāʾ density (§7 below), identifying the 3rd channel as the emphatic/istiʿlāʾ
density dimension. Project phoneme dispersion-tail law fitted as two-piece-kink-75 (primary_r2 0.9457);
Q 103 (s=103 > 75) is in the dispersing regime. Its emphatic channel is the highest of its four — Q 103
is phonetically "heavy" in the istiʿlāʾ dimension.

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf
order, Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 103:

| Field | Value |
|:--|:--|
| n_verses | 3 |
| rhyme_entropy_nats | **0.0** (perfect monorhyme — corpus floor) |
| top_final_letter | ر |
| top_final_letter_frac | 1.0 |
| mean_content_distance | 0.7870 |
| local_cohesion | **3.0697** |
| z_rhyme_entropy | −1.3940 |
| z_mean_content_distance | −1.3467 |
| z_local_cohesion | **+2.1120** |
| **sig_A** | **−0.0473** (rank **61 / 114**) |
| **sig_B** | **+0.7180** (rank **38 / 114**) |

**Reading.** Q 103's rhyme entropy is the **minimum possible (0.0)** — a perfect rā'-monorhyme (z =
−1.39, far below average rhyme variety). Its `local_cohesion` 3.070 (z = +2.11) is **rank 10/114** by
descending cohesion (top decile) — the surah is extremely self-similar verse-to-verse, which for a
3-verse surah reflects its tight oath→claim→exception unity and shared morphology (three form-VI/IV
verbs *āmanū / ʿamilū / tawāṣaw*, three ṣād-roots). sig_A −0.0473 (rank 61/114) is dead-centre on the
al-Bāqillānī *iʿjāz al-fawāṣil* axis — the perfect monorhyme (low entropy) and high cohesion roughly
cancel. sig_B +0.7180 (rank 38/114) is upper-mid.

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

| Seam | delta_raw | ascending-rank | fraction_residual |
|:--|:--|:--|:--|
| Q 102 → Q 103 | +0.04795 | 44 / 113 | 0.00578 |
| Q 103 → Q 104 | +0.11570 | 88 / 113 | 0.01395 |

**Reading.** Both seams are cheap (the whole short-Meccan tail is FR-dense, so transitions cost little).
The backward seam Q 102 al-Takāthur → Q 103 al-ʿAṣr (rank 44/113) is cheaper than the forward seam
Q 103 → Q 104 al-Humaza (rank 88/113). Topically this is coherent: al-Takāthur (rivalry-in-worldly-
accumulation as ruin) flows naturally into al-ʿAṣr (humankind in loss except the believers) — both are
admonitions on misspent life — whereas al-Humaza (the backbiting wealth-hoarder) is a sharper tonal
shift. For contrast, the corpus's most-expensive seam is Q 1 → Q 2 (0.622); Q 103's seams are ≈ 1/13
and ≈ 1/5 of that.

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method: `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **−2.2439** (rank **106 / 114**) |
| abs_outlier | 0.0 (from H-NEW-590 delta_pct) |
| max_cost | 0.11570 (the Q 103 → Q 104 seam) |
| abs_ijaz | 0.04734 (= |sig_A|) |

**Reading.** Q 103 sits in the **bottom-9 of the UAS** (rank 106/114) — the protocol §3.3 bottom-10 list
names Q 103 explicitly. All three UAS components are minimal: zero outlier-strength (perfect cohesion
member), a cheap max-seam, and a near-zero sig_A (the monorhyme/cohesion cancellation). By the project's
whole-surah-dispersion instruments Q 103 is architecturally *quiet*. Its empirical interest is
**micro-structural and phonological** — the minimal-surah rā'-twin, the #2 emphatic density, and the
minimal tripartite qasam skeleton — NOT whole-surah dispersion. This is the structural-vs-theological
iʿjāz orthogonality (al-Bāqillānī vs al-Khaṭṭābī): a meaning-revered surah that is structurally low-UAS.

## 7. Emphatic-iconicity (`findings/phase-b-hypotheses/csv/h-new-2340.json`; seed 20260509, 10000 perms)

istiʿlāʾ (heavy) letter set = {خ ص ض ط ظ غ ق} (Buckwalter "S D T Z q g x").

| Field | Value |
|:--|:--|
| Q 103 heavy_density | **0.0959** |
| Rank among top_heavy_surahs | **#2 / 114** (behind Q 113 al-Falaq 0.1212; ahead of Q 86 al-Ṭāriq 0.0827) |
| adhab_density (ʿadhāb-vocabulary) | 0.0 |
| Independent recompute (this profile) | 7 heavy letters / 73 total = 0.0959 ✓ exact match |
| Heavy-letter breakdown | **ص ×5**, خ ×1, ق ×1 — **ṣād-dominant** |

**Reading.** Q 103 is the corpus's **2nd-densest surah in emphatic (istiʿlāʾ) letters**, and the load is
overwhelmingly **ṣād**: 5 of 7 heavy tokens. Those ṣāds are the surah's lexical spine — al-ʿa**Ṣ**r
(time), al-**Ṣ**āli**Ḥ**āt (righteous deeds), al-**Ṣ**abr (patience). The corpus-level iconicity
hypothesis (heavy-letter density ↔ ʿadhāb/punishment vocabulary) was **NULL in H-NEW-2340** (ρ = 0.0232,
p = 0.405), and Q 103's own adhab_density is 0.0 — so the emphasis here is **lexical-spine-driven, not
punishment-theme-driven**. This is the basis of Q103-F-01 Arm B (DIRECTIONAL: obs > null, z = +1.83,
p_perm = 0.070, does not clear α = 0.05).

## 8. Qasam inventory (`findings/phase-b-hypotheses/csv/h-new-2210.json`; seed 20260509, 10000 perms)

| Field | Value |
|:--|:--|
| Cluster kind | wāw-qasam (single oath, n_stacked 1, n_openings 1) |
| Sworn object | ʿaṣr (Buckwalter EaSor / ESr), semantic class **temporal** |
| jawāb marker | inna/anna (v 2, word 1) |
| **qasam → jawāb verse-distance** | **1** (the minimal value; 11 of 44 corpus clusters share dist 1) |
| Exception particle | *illā* at 103:3:1:1 (QAC POS:EXP) — the istithnāʾ opening v 3 |

**Reading.** Q 103 is a textbook minimal qasam: a single wāw-oath on a temporal object, answered one
verse later by the *inna al-insāna la-fī khusr* claim, then qualified by the *illā* exception. Among the
corpus's 44 qasam-clusters (28 wāw-oaths, 9 tā-oaths, 8 *uqsimu* 1st-person, per H-NEW-2210 counts), the
distance-1 jawāb is the tightest tier — and Q 103 realises the full oath→claim→exception arc in exactly
three verses. This anchors Q103-F-01 Arm C (CONFIRMED).

## 9. Lexical / morphological counts (computed; QAC v0.4 surah-103 lines)

| Quantity | Value | Note |
|:--|:--|:--|
| Verses | 3 | |
| Words (marks stripped) | 14 | v1=1, v2=4, v3=9 |
| Letters | 73 | v1=6, v2=15, v3=52 |
| Distinct QAC roots | 9 | ʿ-ṣ-r (ESr), ʾ-n-s (Ans), x-s-r (xsr), ʾ-m-n (Amn), ʿ-m-l (Eml), ṣ-l-ḥ (SlH), w-ṣ-y (wSy, ×2), ḥ-q-q (Hqq), ṣ-b-r (Sbr) |
| Root-tokens | 10 (w-ṣ-y appears twice: *tawāṣaw bi-l-ḥaqq* + *tawāṣaw bi-l-ṣabr*) | |
| ṣād-bearing roots | 3 of 9 (ʿ-Ṣ-r, Ṣ-l-ḥ, Ṣ-b-r) | drives the istiʿlāʾ density |
| Perfect monorhyme | ر, 3/3 | rhyme_entropy 0.0 |

## 10. Architectural-type classification

- **Outlier axis (H-NEW-590):** in-block COHESION member (NULL, delta_pct 0.0) — maximally non-extreme.
- **iʿjāz axis (H-NEW-750):** mid sig_A (rank 61/114), but extreme on two sub-components — *minimum*
  rhyme entropy (perfect monorhyme) and *top-decile* local cohesion (rank 10/114).
- **UAS (H-NEW-840):** bottom band (rank 106/114) — "anti-iʿjāz" by the dispersion instruments.
- **Phonology (H-NEW-2340):** #2 in corpus emphatic density (ṣād-driven).
- **Rhetoric (H-NEW-2210):** minimal-distance wāw-qasam with full oath→jawāb→istithnāʾ arc.
- **Net:** Q 103 is a **maximally-compressed, FR-dense, phonologically-heavy, perfectly-monorhymed
  short-Meccan surah** whose architectural distinctiveness is *micro-structural* (the minimal-surah
  rā'-twin with Q 108, the ṣād-iconicity, the minimal qasam skeleton) rather than whole-surah-dispersion.

## 11. Honest limits

- The phoneme 4-vector channel labels are not annotated in `h-new-700.json`; the identification of the
  3rd channel as the istiʿlāʾ dimension rests on its numerical equality with the H-NEW-2340 heavy-density
  (0.0959), which is strong but not a documented schema label.
- With only 3 verses, no within-surah permutation can resolve (3! = 6); all per-surah significance here
  is either deterministic corpus-rarity or corpus-level (not within-surah) permutation.
- H-NEW-590's window for Q 103 is the symmetric ±3 neighbourhood {100-106}; the NULL is
  window-definition-dependent — though here the whole window is so FR-dense that the result is robust.
- FR distances are on QAC-STEM root distributions; with only 9 distinct roots, Q 103's FR vector is
  sparse, so its neighbour ranks are sensitive to the top-K coverage (0.9 for Q 103 per `h-new-111.json`).

## 12. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 103 row; rank-1 neighbour Q 108)
- [[h-new-590|H-NEW-590]] — outlier-strength (Q 103 NULL, cohesion member of {100-106})
- [[h-new-700|H-NEW-700]] — rhyme (perfect rā'-monorhyme) + phoneme (emphatic-channel-high)
- [[h-new-720|H-NEW-720]] — Q 102→Q 103 (rank 44) and Q 103→Q 104 (rank 88) seams
- [[h-new-750|H-NEW-750]] — iʿjāz signature (rhyme entropy 0.0, local cohesion rank 10)
- [[h-new-840|H-NEW-840]] — UAS rank 106/114 (bottom band)
- [[h-new-2210|H-NEW-2210]] — minimal wāw-qasam, jawāb distance 1
- [[h-new-2340|H-NEW-2340]] — #2 emphatic-istiʿlāʾ density (0.0959, ṣād-driven)

---

*All numerical values traced to on-disk JSON / morphology artifacts as cited. Computed 2026-05-30.*
