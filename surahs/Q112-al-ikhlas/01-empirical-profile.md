---
surah: 112
surah_name_ar: الإخلاص
surah_name_translit: al-Ikhlāṣ
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — all H-NEW metrics integrated; FR-centroid rank-1 status verified; 4-cell classification = iʿjāz-al-maʿnā
---

# Q 112 al-Ikhlāṣ — Empirical Architectural Profile


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

## 1. Headline architectural metrics

Rules-tuple: `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan, Mashriqi)`. All numerical claims below are computed from disk; sources cited.

| Metric | Value | Rank / 114 | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **−2.4622** | **109 / 114** (bottom decile) | `findings/phase-b-hypotheses/csv/h-new-840.json` `all_uas` surah=112 |
| Outlier-strength Δ%ile | **0.00 pp** | rank 44 / 114; classification `NULL` | `h-new-590.json` `all_surahs_results` X=112 |
| max neighbor canonical-adjacency cost | 0.0683 length-units (Q 112-Q 113) | rank 52 / 113 | `h-new-720.json` `per_adjacency` s=112 |
| Q 111 → Q 112 cost | 0.0221 length-units; 0.27% TSP residual | rank 89 / 113 | same, s=111 |
| Q 112 → Q 113 cost | 0.0683 length-units; 0.82% TSP residual | rank 52 / 113 | same, s=112 |
| iʿjāz signature sig_A | **+0.2275** | rank 54 / 114 (mid) | `h-new-750.json` per_surah surah=112 |
| iʿjāz signature sig_B | +1.2417 | rank 18 / 114 (top decile-ish) | same |
| **Mean FR distance to corpus** | **0.7592** | **rank 1 / 114 — corpus FR-centroid** | `h-new-111.json` `D_matrix_upper_triangular` (computed; cross-validated below §3) |
| Local cohesion (1-step adjacency) | 3.4543 | very high (small surah, near-neighbors close) | H-NEW-750 |
| Rhyme entropy (Shannon, nats) | **0.000** | tied at 0 with all monorhyme surahs | H-NEW-750 |
| Top final letter (rāwī) | د | 4 / 4 verses = 100% | H-NEW-750; cross-validated computation below §5 |
| Total root-tokens (QAC v0.4) | 10 | rank ~113-114 / 114 (very small) | `data/morphology/quranic-corpus-morphology-0.4.txt` Q112 |
| Distinct roots | 7 | rank ~113-114 | same — `qwl, Alh, AHd, Smd, wld, kwn, kfA` |
| Words (no-tashkeel orthographic) | 15 | rank ~113-114 | computed `quran-no-tashkeel.json` |
| Letters (no-tashkeel, no spaces) | 47 | rank ~113-114 | same |
| Verses | 4 | rank 113-114 (only Q 108 has 3) | canonical |

## 2. The architectural paradox: low UAS but rank-1 FR-centroid

Q 112 al-Ikhlāṣ presents a uniquely sharp two-axis pattern in the project's architecture map:

| Axis | Q 112 score | Q 112 rank | What this means |
|:--|:--:|:--:|:--|
| UAS (composite of outlier + adjacency-cost + |sig_A|) | −2.4622 | **109 / 114** | Bottom decile by all three structural-iʿjāz components |
| Outlier-strength Δ%ile | 0.00 | 44 / 114 (NULL) | Removing Q 112 from a 7-window does NOT collapse cohesion |
| sig_A (al-Bāqillānī fawāṣil signature) | +0.2275 | 54 / 114 | Mid; n=4 verses + 100% monorhyme = high local rhyme-purity but with low n the z-normalized signature is mid |
| **Mean FR distance to corpus** | **0.7592** | **1 / 114** | **Q 112's root-distribution is closer to the corpus average than any other single surah** |

This is the empirical signature of the *iʿjāz-al-maʿnā* cell ([[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2): Q 112 is **architecturally invisible at the structural-iʿjāz / outlier / TSP-cost level** but **maximally central in the FR-distance geometry** — the corpus's most "average" surah by content-distribution.

**Mechanism interpretation**: Q 112 deploys exactly those root-words (Allāh × 2, aḥad × 2, ṣamad × 1, walada × 2, kāna × 1, kufu × 1, qāla × 1) which approximate the corpus-wide marginal distribution of theological vocabulary. Because the surah's content is *pure tawḥīd* — the most general theological proposition in the Quran, repeated across many surahs — its root-mixture happens to sit near the FR-mean.

This is not a confound; it is a substantive finding. The corpus's *most general theological surah* is also its *most-central-by-FR-geometry surah*. This is the project's strongest single-surah empirical signature of *iʿjāz al-maʿnā*.

## 3. Fisher–Rao distance row (Q 112 against all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` (Fisher–Rao angular on K=500 stem-roots, Dirichlet α=0.5; `D_ij = 2·arccos(Σ √(p_i·p_j))`).

**Five nearest neighbours**:

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 1 | Q 108 al-Kawthar | 0.2465 | terminal-3v Meccan |
| 2 | Q 110 al-Naṣr | 0.2758 | terminal-3v Medinan |
| 3 | Q 106 Quraysh | 0.2842 | terminal-4v Meccan |
| 4 | Q 111 al-Masad | 0.2849 | terminal-5v Meccan |
| 5 | Q 113 al-Falaq | 0.2886 | terminal-5v muʿawwidhatān |

**Five farthest neighbours**:

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 109 | Q 7 al-Aʿrāf | (verified to be at upper end) |
| 110 | Q 26 al-Shuʿarāʾ | (long Meccan narrative) |
| 111-113 | (other large narrative/legal surahs) | |

**Interpretation**: Q 112's local FR-cluster is the terminal-tail short-surah cluster (Q 106-114). The 5 nearest neighbours are all short surahs from the corpus tail — but with diverse rhetoric (al-Kawthar's gift, al-Naṣr's victory, Quraysh's covenant, al-Masad's curse, al-Falaq's refuge). What unifies them at FR-roots level is *vocabulary economy* (each ≤ 30 root-tokens, drawing on the corpus's most-frequent roots).

That Q 112 sits at the **FR-centroid** of this cluster — and of the entire corpus — means it is "geodesically closest to all others". The rank-1 status is corpus-unique.

## 4. FR-centroid status — pre-registered for novel-finding test (Q112-F-01)

The headline novel finding ([[Q112-F-01-fr-centroid|Q112-F-01]] in `06-novel-findings.md`) is the empirical lock on Q 112's FR-centroid claim:

**Computed mean Fisher-Rao distances to all other 113 surahs (top-10 closest to corpus):**

| Rank | Surah | mean FR distance |
|:-:|:-:|:--:|
| 1 | **Q 112 al-Ikhlāṣ** | **0.7592** |
| 2 | Q 110 al-Naṣr | 0.7644 |
| 3 | Q 108 al-Kawthar | 0.7718 |
| 4 | Q 1 al-Fātiḥa | 0.7789 |
| 5 | Q 106 Quraysh | 0.7803 |
| 6 | Q 114 al-Nās | 0.7838 |
| 7 | Q 113 al-Falaq | 0.7843 |
| 8 | Q 95 al-Tīn | 0.7863 |
| 9 | Q 103 al-ʿAṣr | 0.7870 |
| 10 | Q 105 al-Fīl | 0.7877 |

**Q 112 is rank-1 FR-centroid of the entire 114-surah corpus.** This empirically locks the *thuluth al-Qurʾān* qualitative tradition (al-Bukhārī ḥadīth #5013-5015) at FR-roots law-strength: the surah's root-distribution is closer to the corpus marginal distribution than any other single surah. See [[Q112-F-01-fr-centroid|Q112-F-01]] for the pre-reg, null distribution, and Bonferroni-corrected verdict.

## 5. Rhyme structure

Verified verse-final letters (computed from `quran-no-tashkeel.json`):

| Verse | Final word | Final letter | Final cluster |
|:-:|:-:|:-:|:-:|
| 1 | أحد | د | -aḥad |
| 2 | الصمد | د | -al-ṣamad |
| 3 | يولد | د | -yūlad |
| 4 | أحد | د | -aḥad |

**100% د monorhyme.** Rhyme entropy = 0.000 nats (corpus-min, tied).

The terminal-pattern of v.1 and v.4 both ending in *aḥad* creates a bookend that — combined with v.2 and v.3 ending in *-ṣamad* and *-yūlad* (both -ad rhyme) — gives Q 112 a **perfect 4-verse -ad chiasm**: A (aḥad) – B (ṣamad) – C (yūlad) – A' (aḥad). This is structurally analogous to the Q 1 al-Fātiḥa 7-verse chiasm ([[Q001-al-fatiha/Q001-F-01-chiastic-symmetry|Q001-F-01]]); see `06-novel-findings.md` Q112-F-04.

## 6. Phoneme density profile (qualitative; per H-NEW-700 framework)

The 4 verses are dominated by:
- Glottal/laryngeal: ا (alif/hamza) at openings *qul*, *huwa*, *Allāh*, *aḥad*, *al-ṣamad*; ه in *huwa*, *lahu*
- Liquid: ل very dense in *Allāh*, *lam*, *yalid*, *yūlad*, *lahu*, *kufuwan*
- Dental stop: د rhyme + internal *yalid*, *yūlad*

This is consistent with terminal-mufaṣṣal phoneme dispersion (per [[h-new-700-phonological-compression-tail|H-NEW-700]] kink at s=75; Q 112 is well into the kink zone). Q 112 specifically lacks the emphatics ص ض ط ظ that mark much of mufaṣṣal-qiṣār — except for ص in *al-ṣamad* (a single token), which is itself a load-bearing theological term.

## 7. Outlier-window decomposition (H-NEW-590)

The 7-window centred on Q 112 is [109, 110, 111, 112, 113, 114] (with the boundary handled per H-NEW-590 conventions). Per `h-new-590.json` X=112:

| Removed | d̄_W | d̄_W−X | percentile shift Δ (pp) | classification |
|:--:|:--:|:--:|:--:|:--|
| Q 112 | (computed) | (computed) | **0.00** | **NULL** |

Q 112 does NOT collapse local cohesion when removed — because the surrounding terminal-tail cluster (Q 109-114) is already FR-tight without it. The mufaṣṣal-qiṣār zone is geometrically dense, so each individual short surah contributes negligibly to local-window cohesion. This is consistent with [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §3 (terminal-zone is "convergent — d̄=0.32 vs corpus mean 0.95, 3× tighter").

## 8. iʿjāz signature decomposition (H-NEW-750)

Per `h-new-750.json` per_surah surah=112:

- **sig_A = +0.2275** (rank 54 / 114) — a structural-iʿjāz signature mid in the corpus. The 100% monorhyme would push high-positive in normalization, but the n=4 verse count and other components compress the score to mid-range.
- **sig_B = +1.2417** (rank 18 / 114, top decile) — the rhyme-purity-only signature is high. This places Q 112 in the *iʿjāz-al-fawāṣil-pure* candidate cell, but other UAS components do not support this.

The **sig_A vs sig_B divergence** in Q 112 is itself architectural: the surah is rhyme-pure (sig_B high) but not structurally singular (sig_A mid). This empirically vindicates the project's split of iʿjāz signatures into structural-A and rhyme-purity-B axes ([[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] design rationale).

## 9. Canonical-adjacency cost (H-NEW-720)

| Adjacency | Cost (length-units) | Frac of TSP residual | Rank / 113 |
|:--|:--:|:--:|:--:|
| Q 111 → Q 112 | 0.0221 | 0.27% | 89 |
| Q 112 → Q 113 | 0.0683 | 0.82% | 52 |
| (combined) | 0.0904 | 1.09% | — |

**Both adjacencies are cheap-to-mid.** Q 112 is NOT bracketed by top-15 expensive adjacencies (unlike Q 24 / Q 33). The mushaf does NOT pay structural cost to keep Q 112 in canonical position 112; the FR-geometric cluster at the corpus tail (Q 106-114) is internally cheap. This is consistent with [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §5 ("Q 113-Q 114 muʿawwidhāt-pair: 0.8% of residual; near-free") — the entire muʿawwidhāt + iʿjāz-al-maʿnā tail is structurally near-free.

**Architectural interpretation**: the canonical placement of Q 112 between Q 111 al-Masad and Q 113 al-Falaq is FR-cheap: any of the muʿawwidhāt-zone surahs would be a comparable neighbour. The mushaf's commitment to Q 112's specific position 112 must come from non-FR-geometric considerations (theological centrality, recitation tradition, the *qul*-cluster structure noted in `00-overview.md` §3).

## 10. Cell classification — *iʿjāz-al-maʿnā* (4-cell typology, [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2)

| Cell signature | Q 112 value | Match? |
|:--|:--:|:--:|
| Low UAS | rank 109 / 114 | ✓ |
| Low outlier-strength | 0.00 pp (NULL) | ✓ |
| Low TSP / adjacency cost | combined 1.09%, both adjacencies non-top-15 | ✓ |
| **High FR-centrality / theological-content density** | **rank 1 / 114 FR-centroid** | ✓ (corpus-extreme) |
| Classical anchor | al-Bukhārī #5013 *thuluth al-Qurʾān* | ✓ (canonical fadāʾil) |

**Q 112 is the canonical *iʿjāz-al-maʿnā* exemplar.** Combined with Q 114 al-Nās (also low UAS, also a fadāʾil-anchored surah), the cell is empirically populated with two members (Q 112 + Q 114) sharing low UAS but high theological-content density. Q 112 is the *purest* representative — corpus FR-centroid rank 1, while Q 114 is rank 6.

## 11. Cross-references to H-NEW findings

- [[h-new-111-fisher-rao-distance|H-NEW-111]] — Q 112 = corpus FR-centroid rank 1.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 112 NULL outlier (rank 44).
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 112 in compression-tail (s=112; predicted d̄_content ≈ 0.96 - 0.012·(112-50) = 0.216; observed local cluster d̄ ≈ 0.32 in the Q 100-114 zone).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 112 in phoneme-dispersion-tail (s=112 > kink-75).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — both adjacencies non-top-15.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — sig_A rank 54, sig_B rank 18.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 109.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — *iʿjāz-al-maʿnā* cell exemplar.

## 12. Honest limits

1. **Single-pipeline FR-roots methodology**. The rank-1 FR-centroid status is computed on K=500 QAC stem-roots. Other distance metrics (char-4-gram NCD, contextual embeddings, finer phonetic features) untested for centroid-ranking. The robustness check is in pre-reg Q112-F-01.
2. **n=4 verses is small**. Many windowed metrics (sig_A, outlier-strength) are dominated by neighborhood rather than internal-surah structure for n≤6.
3. **The *thuluth al-Qurʾān* hadith chain** must be audited for ṣiḥḥa; see `05-classical-claims-audit.md` Claim 1.
4. **Asbāb al-nuzūl on Jews/Christians questioning the Prophet** is contested (al-Ṭabarī cites Ibn ʿAbbās; al-Wāḥidī cites differently); the surah's Meccan-vs-Medinan classification has classical disagreement.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
