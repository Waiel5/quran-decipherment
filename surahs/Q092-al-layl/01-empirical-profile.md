---
surah: 92
surah_name_ar: الليل
surah_name_translit: al-Layl
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -750 / -720 / -840 / -1820 (every value cited to path)
---

# Q 92 al-Layl — Empirical Profile


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

All values are read directly from on-disk artifacts; none is asserted from memory. Q 92 is surah-id 92;
in the 1-indexed Fisher-Rao matrix it is index 92; in the 0-indexed phoneme-vector list
(`h-new-700.json` → phoneme.phoneme_vectors) it is index 91.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as `D_matrix_upper_triangular` (6441 pairs), 1-indexed surah IDs. Corpus matrix stats:
min 0.2127, max 1.5509, mean 0.9235, median 0.9567.

| Quantity | Value |
|:--|:--|
| Q 92 mean FR to all 113 surahs | **0.8438** (below corpus mean 0.9235 — a content-typical, near-central surah) |
| Nearest neighbor | **Q 111 al-Masad** at FR 0.4060 |
| Top-15 FR neighbors | Q 111 (0.406), Q 108 (0.411), Q 94 (0.412), Q 93 (0.434), Q 104 (0.445), Q 106 (0.445), Q 112 (0.447), Q 113 (0.448), Q 107 (0.453), Q 103 (0.459), Q 105 (0.469), Q 100 (0.472), Q 91 (0.473), Q 95 (0.475), Q 101 (0.477) |
| 5 farthest | Q 5 (1.251), Q 6 (1.252), Q 9 (1.281), Q 3 (1.282), Q 4 (1.299) |

**Reading.** Q 92's FR neighborhood is the **short early-Meccan mufaṣṣal-qiṣār cluster** — Q 111, 108, 94,
93, 91, 95, 100, 101, 103, 104, 107 — short oath/admonition surahs with dense believer/disbeliever/judgment
vocabulary. Q 93 al-Ḍuḥā (rank 4) and Q 91 al-Shams (rank 13) — Q 92's literal mushaf neighbors — are both
top-13 FR neighbors, a rare convergence of canonical-adjacency and content-geometry (most surahs' mushaf
neighbors are NOT among their nearest FR neighbors). The 5 farthest are the long Medinan legal surahs
(Q 4 al-Nisāʾ, Q 3 Āl ʿImrān, Q 9 al-Tawba, Q 6 al-Anʿām, Q 5 al-Māʾida) — the opposite register.

**The Muʿādh recitation cluster.** The four surahs the Prophet named as fit for congregational prayer in
Muslim #942 — Q 91 al-Shams, Q 93 al-Ḍuḥā, Q 92 al-Layl, Q 87 al-Aʿlā — are all near Q 92 in FR space
(Q 93 rank 4, Q 91 rank 13; Q 87 is a near-peer of this cluster). The ḥadīth's liturgical pairing has a
content-geometry correlate. See `04-hadith-corpus.md`.

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

| Quantity | Value |
|:--|:--|
| Window (centered on Q 92) | {Q 89, 90, 91, 92, 93, 94, 95} |
| d̄_W (with Q 92) | 0.49616 |
| d̄_W−X (without Q 92) | 0.49505 |
| pct_W | 0.07 |
| pct_W−X | 0.13 |
| **delta_pct** | **−0.06** |
| p_greater_W | 0.9993 |
| **classification** | **NULL** |

**Reading.** Q 92 is a **deep cohesion member** of the short-Meccan {Q 89–95} window. Removing it barely
moves the window's content-dispersion (delta_pct −0.06, p = 0.9993). The window's own percentile (0.07) is
among the lowest in the corpus — this is one of the **most internally-cohesive 7-surah neighborhoods** in
the mushaf (a block of short oath/eschatology surahs that look alike at the root-distribution level).
Contrast Q 1 (+27.09 pp STRONG_OUTLIER). Q 92's architectural interest is **NOT** dispersion-extremity.

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, Q 92): top final-letter **ي (yāʾ)**, fraction **1.0000 (21/21 verses)**
— a **perfect monorhyme**. Every verse ends in the *-ā* sound written with alif-maqṣūra/yāʾ (*yaghshā,
tajallā, al-unthā, la-shattā, wa-ttaqā, bi-l-ḥusnā, li-l-yusrā, …, yarḍā*). This is the tightest possible
rhyme regime and is **the opposite** of the dispersing-tail prediction (Q 92 has s = 92 > 50, where the
rhyme dispersion-tail law `d̄_rhyme ≈ 0.36 + 0.0041·max(0,s−50)`, primary_r2 = 0.7886, expects *higher*
fawāṣil variety). Q 92 is a clean **counter-instance to the tail at the individual-surah level** — its
monorhyme is total. (The law is a corpus-mean trend, not a per-surah guarantee; Q 92 is on its tight side.)

**Phoneme** (phoneme_vectors index 91, 4-dim density vector): `[0.01592, 0.03503, 0.06051, 0.11146]`.
The phoneme dispersion-tail law is two-piece-kink-75 (primary_r2 = 0.9457); Q 92 (s = 92 > 75) sits in the
dispersing regime. The 4th channel (0.1115) is the largest of its four dimensions.

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order,
Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 92:

| Field | Value |
|:--|:--|
| n_verses | 21 |
| rhyme_entropy_nats | **0.0000** (perfect monorhyme — entropy floor) |
| top_final_letter | ي |
| top_final_letter_frac | 1.0000 |
| mean_content_distance | 0.8438 |
| local_cohesion | **2.1343** |
| z_rhyme_entropy | **−1.3940** |
| z_mean_content_distance | −0.7862 |
| z_local_cohesion | **+0.8385** |
| **sig_A** | **−0.6078** (rank_A 77 / 114; abs-rank 82 / 114) |
| **sig_B** | **−0.5556** (rank_B 66 / 114; abs-rank 88 / 114) |

**Reading.** Q 92 sits at the **rhyme-entropy floor** (0.0 nats, z = −1.39 — among the most monorhymic
surahs in the corpus) yet has **above-average local cohesion** (2.134, z = +0.84 — Q 92's adjacent verses
are MORE self-similar than the median surah). Both signatures are *negative* (sig_A −0.61, sig_B −0.56),
placing Q 92 in the lower band of the al-Bāqillānī *iʿjāz al-fawāṣil* structural axis: a surah whose
phonological binding is achieved by a **single tight rhyme** rather than by an entropy-rich, varied
fawāṣil scheme. This is the **theological-iʿjāz / liturgical** profile (high cohesion, low dispersion-
significance) rather than the structural-hub profile.

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

| Seam | delta_raw | ascending-rank | class |
|:--|:--|:--|:--|
| **Q 91 → Q 92** | **−0.08683** | **1 / 113** | **THE single most seamless seam in the mushaf** |
| Q 92 → Q 93 | +0.06063 | 55 / 113 | mid-spectrum (fraction_residual 0.0073) |

**Reading.** The **al-Shams → al-Layl** transition is the cheapest canonical adjacency in the entire
corpus (rank 1/113, delta_raw = −0.0868, fraction_residual 0.0 — clamped negative). Both are early-Meccan
oath-opening short surahs on **cosmic-pairs → moral-duality** (al-Shams: sun/moon/day/night → *qad aflaḥa
man zakkāhā · wa-qad khāba man dassāhā*; al-Layl: night/day/male-female → *fa-ammā man aʿṭā* / *wa-ammā man
bakhila*). The two surahs share the **oath-of-opposed-pairs-then-soul-bifurcation** template, and the FR
geometry (Q 91 is Q 92's rank-13 neighbor) plus the rhyme (both monorhyme `-ā`) confirm it. The exit
Q 92 → Q 93 is a normal mid-cost seam. Top-3 most-expensive corpus seams for contrast: Q 1→Q 2 (0.622),
Q 32→Q 33 (0.363), Q 33→Q 34 (0.331). **This is the strongest single architectural fact about Q 92's
position** — it is the smoothest joint in the book.

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method: `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **−2.0293** (rank **100 / 114**) |
| abs_outlier | 0.06 (from H-NEW-590 delta_pct) |
| max_cost | 0.06063 (the Q 92 → Q 93 seam; the backward Q 91→Q 92 seam is negative) |
| abs_ijaz | 0.6078 (= |sig_A|) |

**Reading.** UAS rank 100/114 — Q 92 is a **low-architectural-significance surah by the whole-surah
dispersion metric**, consistent with: near-zero outlier strength (deep cohesion member), a low max-neighbor
TSP cost (the strongest seam, Q 91→Q 92, is *negative* so the max collapses to the modest forward seam),
and a below-average iʿjāz signature. Top-10 UAS are Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17. Q 92's interest
is **NOT** whole-surah-dispersion; it is **micro-structural and positional** — the corpus-cheapest seam,
the perfect monorhyme, and the textbook giver/miser muqābala (Q092-F-01).

## 7. Lexical counts + title-density (computed; `scripts/Q092_F_01_*.py`)

| Quantity | Value | Note |
|:--|:--|:--|
| Verses | 21 | |
| Words (marks stripped) | 71 | |
| Letters (non-space) | 314 | |
| Distinct QAC roots | 41 | 48 root-tokens |
| Allāh-substring tokens | **0** | God named once as *rabb* (v20) |
| Longest verse | v 11 (6 words) + v 19 (6 words) | *wa-mā yughnī ʿanhu māluhu* / *wa-mā li-aḥadin ʿindahu* |
| **lyl-root attestations in Q 92** | **1** (v1 *wa-l-layl*) | `data/morphology/root-index.json` |
| **Q 92 rank in lyl-root density** | **48 / 49** | rank-1 = Q 2 al-Baqara (5×); H-NEW-1820 confirmed |

**Title-density-independence (H-NEW-1820).** Q 92 is named al-Layl yet uses `lyl` exactly once and ranks
48th of the 49 surahs containing it. This is one of the most *extreme* confirmations of the law in the
corpus: the eponym is rank-near-last in its own title-root. See Arm C of `06-novel-findings.md`.

## 8. Architectural-type classification

- **Outlier axis (H-NEW-590):** deep in-block COHESION member (NULL) — not dispersion-extreme.
- **iʿjāz axis (H-NEW-750):** lower-band structural-iʿjāz (sig_A −0.61), rhyme-entropy floor + above-average local cohesion → **monorhyme-bound liturgical** profile.
- **Position axis (H-NEW-720):** entered via the **single cheapest seam in the mushaf** (Q 91→Q 92, rank 1/113).
- **UAS (H-NEW-840):** low (rank 100/114) — not a structural hub.
- **Net:** Q 92 is a **liturgical, monorhyme-bound, deep-cohesion early-Meccan oath surah** whose
  empirical distinctiveness is *positional* (corpus-cheapest seam) and *micro-rhetorical* (the perfect
  monorhyme and the frame-driven giver/miser muqābala), NOT whole-surah-dispersion.

## 9. Honest limits

- The phoneme 4-vector channel labels are not annotated in `h-new-700.json`; only raw densities are
  reported, so per-channel (emphatic/pharyngeal/sibilant/glottal) interpretation is left un-asserted.
- H-NEW-590's window for Q 92 is the symmetric ±3 {89–95}; the NULL classification is window-dependent.
- FR distances are on QAC-STEM root distributions; a lemma or surface token-level would shift the neighbor list.
- The rhyme is "perfect" only at the final-grapheme level (yāʾ/alif-maqṣūra of the `-ā` ending); a strict
  phonemic analysis would group these as a single rhyme-vowel, which is exactly what the frac = 1.0 captures.

## 10. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 92 row; mean 0.8438, nearest Q 111)
- [[h-new-590|H-NEW-590]] — outlier-strength (Q 92 NULL, deep cohesion member of {89–95})
- [[h-new-700|H-NEW-700]] — rhyme (perfect ي monorhyme) + phoneme dispersion-tails
- [[h-new-720|H-NEW-720]] — **Q 91 → Q 92 cheapest seam in the mushaf (rank 1/113)**
- [[h-new-750|H-NEW-750]] — iʿjāz signature (rhyme-entropy floor, above-average local cohesion)
- [[h-new-840|H-NEW-840]] — UAS rank 100/114
- [[h-new-1820-title-density-independence-formal|H-NEW-1820]] — Q 92 rank 48/49 in lyl
- [[h-new-2360-antithesis-law|H-NEW-2360]] — giver/miser muqābala overlap (Q092-F-01)

---

*All numerical values traced to on-disk JSON artifacts as cited. Computed 2026-05-30 by Waiel Al-Shujaa.*
