---
surah: 102
surah_name_ar: التكاثر
surah_name_translit: al-Takāthur
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -720 / -750 / -840 / -1820 (every value cited to path)
---

# Q 102 al-Takāthur — Empirical Profile

All values below are read directly from the on-disk artifacts. No value is asserted from memory.
Q 102 is surah-id 102; in the 1-indexed Fisher-Rao matrix it is index 102; in the 0-indexed phoneme
vector list (`h-new-700.json` → phoneme.phoneme_vectors) it is **index 101**.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`, 6441 pairs),
1-indexed surah IDs. Corpus matrix stats: min 0.212673, max 1.550933, mean **0.923487**, median 0.956707.

| Quantity | Value |
|:--|:--|
| Q 102 mean FR to all 113 surahs | **0.8011** (well below corpus mean 0.9235) |
| Nearest neighbor | **Q 108 al-Kawthar** at FR **0.2937** |
| Top-8 FR neighbors | Q 108 (0.2937), Q 107 (0.3208), Q 106 (0.3388), Q 111 (0.3396), Q 103 (0.3448), Q 100 (0.3465), Q 105 (0.3476), Q 112 (0.3490) |
| 5 farthest | Q 2 (1.234), Q 6 (1.239), Q 9 (1.280), Q 4 (1.289), Q 3 (1.298) |
| Q 101 (prev surah) rank in Q 102's FR list | **13 / 113** (FR 0.3863) |

**Reading.** Q 102's FR neighborhood is the **juzʾ-30 short-Meccan cluster** (Q 100-112) — short, dense,
rebuke/eschatological surahs — NOT the long Medinan-legal surahs. Its five farthest are precisely the
long Medinan/Meccan narrative-legal surahs (Q 2, 3, 4, 6, 9). The mean FR 0.8011 places Q 102 at
z ≈ −1.21 below corpus mean (the z is reported in `h-new-750.json` as `z_mean_content_distance` = −1.208;
§4). The **nearest neighbor Q 108 al-Kawthar (0.2937)** is the project-relevant coincidence: Q 108 is also
the rank-1 surah in Q 102's own title-root *kvr* by per-word density (§6, H-NEW-1820) — the title-root-#1
surah and the content-nearest surah coincide.

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

H-NEW-590's α-tested **candidate set is {1, 9, 18, 55, 62, 112}** — Q 102 is NOT among the six
Bonferroni-protected candidates. **However**, the file's `all_surahs_results` (114 entries) DOES carry a
descriptive Q 102 record (not α-corrected, but computed):

| Quantity | Value |
|:--|:--|
| Window (centered on Q 102) | {Q 99, 100, 101, 102, 103, 104, 105} |
| d̄_W (window with Q 102) | 0.357688 |
| d̄_W−X (window without Q 102) | 0.353610 |
| pct_W | 0.0 |
| pct_W−X | 0.0 |
| **delta_pct** | **0.0** |
| p_greater_W | 1.0 |
| **classification** | **NULL** |

**Reading.** Removing Q 102 from its 7-surah neighborhood {99-105} does not raise the window's
content-dispersion percentile at all (delta_pct = 0.0, p = 1.0). Q 102 is a **deep in-block cohesion
member** of the juzʾ-30 short-Meccan window — its very low window-d̄ (~0.355, far below corpus mean
0.92) confirms it sits inside one of the corpus's tightest content-neighborhoods. It is the *opposite*
of a dispersion-outlier (contrast Q 1 +27.09pp STRONG_OUTLIER, Q 33 +31.46pp). Because Q 102 was not in
the α-protected candidate set, the downstream UAS (`h-new-840.json`) takes its `abs_outlier` as **0.0**
(§6) — consistent with the descriptive NULL here.

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, Q 102): top final-letter **ن (nūn)**, fraction **0.5** (4/8 verses),
n_verses 8. The nūn-tail is the *-ūn / -īn / -īm* family (*taʿlamūn* ×2, *al-yaqīn* ×2, *al-jaḥīm*,
*al-naʿīm*). Project rhyme dispersion-tail law fitted as two-piece-kink-50 (rhyme primary_r2 reported in
`h-new-700.json`); Q 102 (s=102 > 50) sits in the dispersing tail, yet still carries a 50% monorhyme.

**Phoneme** (phoneme_vectors **index 101**, 4-dim density vector):
`[0.0, 0.073171, 0.032520, 0.040650]`. The 1st component is **0.0** (Q 102 carries none of the first
phoneme channel) and the largest is the 2nd (0.0732). Project phoneme dispersion-tail law fitted as
two-piece-kink-75 (phoneme primary_r2 in `h-new-700.json`); Q 102 (s=102 > 75) sits in the phoneme
dispersing-tail regime.

(Rhyme-entropy and the z-normalized phonological diagnostics are taken from `h-new-750.json`, §4 below.)

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Per-surah record for Q 102 (read verbatim from the `per_surah` list):

| Field | Value |
|:--|:--|
| n_verses | 8 |
| rhyme_entropy_nats | **1.039721** |
| top_final_letter | ن |
| top_final_letter_frac | 0.5 |
| mean_content_distance | **0.801123** |
| local_cohesion | **2.769092** |
| z_rhyme_entropy | +0.488704 |
| z_mean_content_distance | **−1.207614** |
| z_local_cohesion | **+1.702733** |
| **sig_A** | **+1.696318** (rank **12 / 114**) |
| **sig_B** | **+2.191437** (rank **4 / 114**, top-4) |

**Reading.** Q 102's defining iʿjāz feature is its **local cohesion (2.769, z = +1.70)** — among the
most self-cohesive short surahs in the corpus, which is exactly what drives its **sig_B rank of 4/114**
(top-4 corpus-wide). Its mean content distance (0.801, z = −1.21) is well below average (it is
*content-close* to the rest of the corpus, not dispersed), and its rhyme entropy (1.04 nats, z = +0.49)
is slightly above average. The high local-cohesion + low content-dispersion is the signature of a dense,
tightly-knit juzʾ-30 rebuke-cluster surah. sig_A rank 12/114 likewise places Q 102 in the top-tier of
the al-Bāqillānī *iʿjāz al-fawāṣil* structural-significance axis.

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

Per-adjacency entries keyed by `pair`; ascending-rank computed over all 113 seams by `delta_raw`.

| Seam | delta_raw | ascending-rank | class |
|:--|:--|:--|:--|
| Q 101 → Q 102 | **+0.02873** | **30 / 113** | low-mid (cheap entry) |
| Q 102 → Q 103 | **+0.04795** | **44 / 113** | mid-spectrum |

**Reading.** Both seams bracketing Q 102 are below-median-cost (ranks 30 and 44 of 113) — Q 102 sits in
a smooth stretch of the mushaf, the dense juzʾ-30 short-surah run where adjacent root-distributions are
cheap to traverse. Neither is among the 13 clamped/seamless seams, but both are well below the corpus's
expensive seams (top-3 for contrast: Q 1→Q 2 = 0.6216, Q 32→Q 33 = 0.3631, Q 33→Q 34). The forward seam
Q 102 → Q 103 (0.04795) is the more expensive of the two and is the value the UAS picks up as `max_cost`
(§6).

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method (verbatim): `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **−0.741237** (rank **67 / 114**) |
| abs_outlier | **0.0** (Q 102 not in H-NEW-590 candidate set → abs_outlier = 0; descriptive NULL anyway, §2) |
| max_cost | 0.047952 (the Q 102 → Q 103 forward seam) |
| abs_ijaz | 1.696318 (= sig_A) |

**Reading.** Q 102's UAS rank 67/114 (mid-band) is **understated**: the `abs_outlier` component is 0.0
because Q 102 was not in H-NEW-590's six-candidate α-tested set, and the TSP `max_cost` is low (smooth
seams). The only component carrying weight is the iʿjāz signature (sig_A = 1.696, top-12). If the
top-4 sig_B (local-cohesion-driven) were the iʿjāz channel in the UAS formula instead of sig_A, Q 102's
score would rank considerably higher. Q 102 is NOT a whole-surah-dispersion architectural hub (top-10 UAS
are Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17); its architectural interest is **micro-structural** — the
corpus-unique 3-consecutive-verse rebuke-*kallā* run and the *thumma*-doubled threat refrain (Q102-F-01,
`06-novel-findings.md`) — and **local** (top-4 cohesion).

## 7. Title-root density (`findings/phase-b-hypotheses/csv/h-new-1820.json`)

Per the title-density-independence law (one of the 4 project pillar laws). Q 102's record:

| Field | Q 102 | Q 108 (for comparison) |
|:--|:--|:--|
| title | al-Takāthur | al-Kawthar |
| root | **kvr** | kvr |
| title_surah_count (root tokens in surah) | 1 | 1 |
| **title_density_rank** | **2** | **1** |
| is_rank_1 | **false** | true |
| rank_1_surah | **108** | 108 |

**Reading.** Q 102 is **rank-2** in its own title-root *kvr* (k-th-r) by per-word density; **rank-1 is
Q 108 al-Kawthar**. H-NEW-1820 is **VINDICATED** here: the eponymous surah is NOT the densest carrier of
its own title-root — the title is a label, not a frequency-peak (title-density independence). The
project-relevant coincidence: the rank-1 *kvr* surah (Q 108) is also Q 102's **nearest FR neighbor**
(0.2937, §1). The shared *kvr* root + the shared juzʾ-30 short-rebuke register bind the two surahs in
both lexical-density and content-geometry space.

## 8. Lexical counts (computed; `scripts/Q102_F_01_kalla_reduplication.py` pipeline + close-read scan)

| Quantity | Value | Note |
|:--|:--|:--|
| Verses | 8 | `data/hafs-verse-counts.tsv` line 102 = 8 |
| Words (marks stripped, no-tashkeel) | **28** | computed from `quran-text/quran-no-tashkeel.json` |
| Letters (no spaces) | **123** | computed |
| Distinct QAC roots | **11** | `data/morphology/quranic-corpus-morphology-0.4.txt` (Q 102): Elm, Eyn, jHm, kvr, lhw, nEm, qbr, rAy, sAl, yqn, zwr |
| rebuke-*kallā* tokens (POS:AVR LEM kal~aA) | **3** (vv 3, 4, 5) | QAC v0.4; of the corpus-33 census (Q102-F-01 Arm A) |
| nūn-rhyme verses | 4 / 8 (50%) | `h-new-700.json` / `h-new-750.json` |

## 9. Architectural-type classification

- **FR axis (H-NEW-111):** content-close (mean 0.8011, z −1.21) — deep juzʾ-30 short-Meccan cluster member.
- **Outlier axis (H-NEW-590):** in-block COHESION member (descriptive NULL, delta_pct 0.0) — not dispersion-extreme.
- **iʿjāz axis (H-NEW-750):** **top-tier** — sig_A rank 12/114, sig_B rank **4/114** (top-4), local-cohesion z +1.70.
- **UAS (H-NEW-840):** mid-band (rank 67/114), **understated** (abs_outlier=0 data-gap).
- **Title-root (H-NEW-1820):** rank-2 in own *kvr* root (VINDICATES title-density independence; rank-1 = Q 108).
- **Net:** Q 102 is a **deep-cohesion, low-dispersion short juzʾ-30 surah** whose distinctive empirical
  signatures are the top-4 local cohesion (sig_B) and the **micro-structural** rebuke-*kallā* triple-run +
  *thumma*-refrain (Q102-F-01). It is content-close and high-cohesion, not a whole-surah-dispersion hub.

## 10. Honest limits

- H-NEW-590's Q 102 record is from the descriptive `all_surahs_results` (114 entries, NOT the six
  α-protected candidates {1,9,18,55,62,112}); its delta_pct=0.0/p=1.0 is reported as an in-block
  cohesion descriptor, not a Bonferroni-protected outlier verdict. The 00-overview's earlier framing of
  Q 102 as a pure "DATA-GAP" is **corrected here**: a computed descriptive NULL record exists on disk.
- The phoneme 4-vector dimension labels are not annotated in `h-new-700.json`; only the raw 4-density
  values are reported, so the per-channel interpretation is left un-assigned to avoid an un-verified mapping.
- FR distances are on QAC-STEM root distributions (not full lemmas or surface tokens); a different
  token-level would shift the neighbor list.
- The UAS understatement (abs_outlier=0) is a known feature of the H-NEW-840 pipeline for non-candidate
  surahs; the sig_B top-4 rank is the more faithful architectural descriptor for Q 102.

## 11. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 102 row; nearest Q 108 0.2937)
- [[h-new-590|H-NEW-590]] — outlier descriptive NULL (Q 102 in-block cohesion member, delta_pct 0.0)
- [[h-new-700|H-NEW-700]] — rhyme ن 50% + phoneme vector idx 101
- [[h-new-720|H-NEW-720]] — Q 101→Q 102 (rank 30) + Q 102→Q 103 (rank 44) seams
- [[h-new-750|H-NEW-750]] — iʿjāz signature (sig_A rank 12, sig_B rank 4 top-4)
- [[h-new-840|H-NEW-840]] — UAS rank 67/114 (understated; abs_outlier=0)
- [[h-new-1820|H-NEW-1820]] — title-root kvr rank-2 (rank-1 = Q 108); title-density independence VINDICATED

---

*All numerical values traced to on-disk JSON artifacts as cited. Computed 2026-05-30.*
