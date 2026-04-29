---
id: H-NEW-910
title: "Alif-8 cluster pre-registration — does the 100% alif-final-letter cluster {Q 18, 48, 65, 72, 76, 87, 91, 92} cohere on FR-roots, length, chronology, mushaf-position, or 4-axis content/rhyme/phoneme/verse-length?"
phase: B+
status: PRE-REGISTERED — direction locked before observation; SHA256-locked; Bonferroni k=5; α_bon = 0.01
date: 2026-04-28
seed: 20260428
prereg_author: alif8-cluster-specialist
parent_finding: Q033-F-01 (the FALSIFICATION of "Q 33 corpus-MAX alif-monorhyme" that surfaced this 8-surah cluster)
methodological_parent: H-NEW-600 (letter-family double-NULL, the procedural template for cluster-cohesion permutation tests)
n_perms: 10000
bonferroni_k: 5
alpha_bon: 0.01
direction: ALL FIVE LOCKED ONE-SIDED (cohesion = LESS within-cluster mean than random)
---

# H-NEW-910 — Alif-8 cluster pre-registration

## 0. Anti-hallucination + rules-tuple lock

**Default rules-tuple**: `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

**Cluster-definition rules-tuple** (inherited from [[Q033-F-01-alif-monorhyme-prereg|Q033-F-01]]):
`(min-tashkeel, orthographic-token, last-letter-of-verse-after-stripping-final-pause-mark, alif-final-set = {ا, آ, أ, إ, ى, ٰ}, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

The cluster is defined as the surahs whose alif-final-letter rate = **1.0000** under that rules-tuple, verified on `quran-text/quran-min-tashkeel.json`.

**Cluster (locked, N=8)**: `S = {18, 48, 65, 72, 76, 87, 91, 92}` — al-Kahf, al-Fatḥ, al-Ṭalāq, al-Jinn, al-Insān, al-Aʿlā, al-Shams, al-Layl.

**Cluster mushaf positions**: 18, 48, 65, 72, 76, 87, 91, 92 (read as mushaf order).

**Cluster revelation orders** (Egyptian Standard / al-Suyūṭī, from `data/revelation-order.csv`):
- Q 18 → 69, Q 48 → 111, Q 65 → 99, Q 72 → 40, Q 76 → 98, Q 87 → 8, Q 91 → 26, Q 92 → 9.

**Verse-counts** (Hafs-Kufan, from `data/hafs-verse-counts.tsv`):
- Q 18 → 110, Q 48 → 29, Q 65 → 12, Q 72 → 28, Q 76 → 31, Q 87 → 19, Q 91 → 15, Q 92 → 21.

**Pe-Islamic precedent**: Labid (Muʿallaqa, alif-monorhyme) = 0.9888; ʿAmr b. Kulthūm (Muʿallaqa, alif-monorhyme) = 0.9810 — alif-monorhyme is a recognized *qaṣīda*-form in pre-Islamic poetry (per [[Q033-al-ahzab/06-novel-findings|Q033-F-01]] §"poetry control"). The alif-monorhyme architecture is therefore NOT corpus-unique to the Quran. The question this pre-reg addresses: do these 8 alif-monorhyme surahs share more than just the rāwī?

## 1. The five pre-registered hypotheses (Bonferroni-5; α_bon = 0.01; one-sided each; direction LOCKED)

### H1 — FR-roots cohesion (Fisher-Rao distance on QAC stem-root distributions)

- **Statistic**: d̄_FR(S) = mean of pairwise Fisher-Rao distances over the C(8,2) = 28 within-cluster pairs, using `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`.
- **Null**: 10000 random size-8 subsets of the 114 surahs, seed = 20260428.
- **Direction (LOCKED)**: d̄_FR(S) is LESS than the null mean (right-tail percentile ≤ corresponding-α gate).
- **Strict gate**: %ile ≤ 1.00% (PASS at α_bon = 0.01).
- **Directional gate**: %ile ≤ 16.67% (DIRECTIONAL — does not pass H1, but informative).
- **Verdict mapping**:
  - %ile ≤ 1.00%: **VINDICATED** (one of five Bonferroni cells PASSED).
  - 1.00% < %ile ≤ 16.67%: **DIRECTIONAL** (signal in correct direction but sub-α).
  - %ile > 16.67%: **NULL**.

### H2 — Length (verse-count) cohesion

- **Statistic**: chi-squared test of the 8-surah verse-count distribution against the corpus baseline distribution. Verse-count buckets: `[1-20], [21-50], [51-100], [101-200], [201+]` — pre-locked.
- **Cluster verse-counts**: [110, 29, 12, 28, 31, 19, 15, 21] → buckets: 4×[1-20]={12,19,15,...wait re-derive}, 3×[21-50]={29,28,31}+{21}, 1×[101-200]={110}.
- **Direction (LOCKED)**: 8 surahs are concentrated in SHORT-MEDIUM buckets ([1-20] + [21-50] combined > 6 of 8), versus baseline.
- **Test**: chi² goodness-of-fit at α_bon = 0.01.
- **Bonferroni-corrected gate**: p_χ² ≤ 0.01.
- **Verdict mapping**: PASS / DIRECTIONAL / NULL on the same scheme.

### H3 — Chronology cohesion (al-Suyūṭī revelation-order)

- **Statistic**: d̄_rev(S) = mean pairwise |rev(i) − rev(j)| over C(8,2) within-cluster pairs.
- **Null**: 10000 random size-8 subsets of {1..114}, mapping each to its revelation order. Seed = 20260428.
- **Direction (LOCKED)**: d̄_rev(S) is LESS than the null mean (cluster surahs are revealed CLOSER in time than random — consistent with a chronological-cluster hypothesis).
- **Strict gate**: %ile ≤ 1.00%.
- **Verdict mapping**: same scheme.

### H4 — Mushaf-position cohesion

- **Statistic**: d̄_mushaf(S) = mean pairwise |mushaf(i) − mushaf(j)| over 28 pairs.
- **Null**: 10000 random size-8 subsets; mushaf positions are simply 1..114. Seed = 20260428.
- **Direction (LOCKED)**: d̄_mushaf(S) is LESS than the null mean (cluster surahs are spatially CLOSER in mushaf than random).
- **Strict gate**: %ile ≤ 1.00%.
- **Verdict mapping**: same scheme.

### H5 — 4-axis content cohesion (sub-test family of FOUR axes; combined as Bonferroni-within-H5 = 4 sub-cells)

- **Sub-statistics** (from `h-new-700.json` and related artifacts):
  - H5a: mean of `d_observed` content-cohesion proxy (already in [[h-new-660-compression-tail-gradient|H-NEW-660]] window-d̄ space) — but the project has per-surah signatures in [[h-new-700-phonological-compression-tail|H-NEW-700]]. We use `h-new-700.json::rhyme.d_observed` for rhyme-axis, `h-new-700.json::phoneme.d_observed` for phoneme-axis.
  - **Pivot** because 4 single-axis tests would inflate further: we collapse H5 to ONE composite (mean of within-cluster pairwise abs-difference on each axis, summed). This keeps H5 a single Bonferroni-5 cell.
- **Statistic**: d̄_4axis(S) = sum over axes ∈ {content_d̄, rhyme_d̄, phoneme_d̄, verse-len_words} of within-cluster pairwise mean |x_i − x_j| / σ_axis (σ_axis = corpus std of that axis).
- **Implementation note**: per-surah single-value summaries are NOT directly in h-new-700.json (which has window-level d_observed). We will compute per-surah single values from the canonical text:
  - `content`: mean root-FR-distance from the surah to corpus-centroid (h-new-111.json marginal).
  - `rhyme`: per-surah top-letter frac (from h-new-700.json `rhyme_letter_diagnostics`) — but this is exactly the cluster definition (=1.0 for all 8). So we use Shannon-entropy of last-letter distribution instead, computed from min-tashkeel.
  - `phoneme`: emphatic+pharyngeal+sibilant+glottal density per-surah, computed from full-tashkeel.
  - `verse-len`: words-per-verse mean.
- **Direction (LOCKED)**: d̄_4axis(S) LESS than null mean (cluster more-cohesive across all 4 axes combined).
- **Strict gate**: %ile ≤ 1.00%.
- **Verdict mapping**: same scheme.

## 2. Bonferroni-5 family-α structure

| Cell | Hypothesis | α_raw | α_bon (k=5) | Direction |
|:-:|:--|:-:|:-:|:--|
| H1 | FR-roots cohesion | 0.05 | 0.01 | LESS |
| H2 | Verse-count cohesion (chi²) | 0.05 | 0.01 | concentrated short-medium |
| H3 | Revelation-order cohesion | 0.05 | 0.01 | LESS |
| H4 | Mushaf-position cohesion | 0.05 | 0.01 | LESS |
| H5 | 4-axis composite cohesion | 0.05 | 0.01 | LESS |

**Family verdict**:
- **CLUSTER-COHERENT**: ≥ 1 cell at %ile ≤ 1.00%.
- **DIRECTIONAL CLUSTER**: ≥ 3 cells at %ile ≤ 16.67% but no cell ≤ 1.00%.
- **NULL CLUSTER (surface-only)**: no cell ≤ 16.67% across any of H1-H5.
- **Honest reporting**: regardless of family verdict, all 5 cells reported with full effect size + p-value + percentile.

## 3. Pre-committed interpretations

- **If H1 PASSES**: alif-cluster shares root-vocabulary distribution → the rāwī correlates with content. This would CHALLENGE the [[h-new-730-content-rhyme-anticorrelation|iʿjāz anti-twin]] r=-0.86 finding by introducing a small-N sub-cluster where rhyme-axis and content-axis CO-vary at the surah-level.
- **If H2 PASSES**: alif-rāwī is associated with short-medium length surahs (likely true at face value — long surahs tend to use ن/م). This would partly EXPLAIN H1 via length-confound.
- **If H3 PASSES**: alif-rāwī is a chronological-period feature — revealed surahs of the same period cohere on rāwī. This would map to the al-Suyūṭī Meccan/Medinan cohort tradition.
- **If H4 PASSES**: alif-cluster is mushaf-spatially organized — the rāwī is part of mushaf editorial structure (al-Suyūṭī/al-Zarkashī mufaṣṣal tier theory).
- **If H5 PASSES**: cluster is multi-axis-cohesive → alif-rāwī encodes a structural-iʿjāz signature.
- **If ALL NULL**: the alif-monorhyme is a SURFACE phonological feature, like the alif-monorhyme Muʿallaqa (Labid, ʿAmr b. Kulthūm) — a poetic *form* selected without further architectural correlate. This would PARALLEL the [[h-new-600-letter-families|H-NEW-600]] ALR-5/ALM-6 NULL: muqaṭṭaʿāt-letter axis ⊥ content; alif-rāwī axis ⊥ multi-axis structure.

## 4. Failure conditions

- Pre-reg SHA mismatch at runtime → ABORT.
- Cluster-membership rules-tuple cross-check (re-derive the 100%-alif cluster from min-tashkeel) → if cluster ≠ {18, 48, 65, 72, 76, 87, 91, 92}, ABORT (no test runs).
- Direction-of-effect reversal → publish as NULL with explicit pre-commit-violation flag.

## 5. Comparator and sub-tests (POST-HOC, marked carefully)

- **Comparator-16**: include the next 8 surahs at ≥ 0.97 alif-final rate. From the Q033-F-01 ranking, that adds {Q 33, Q 17 (with the rules-tuple-discrepancy logged), Q 25, Q 4 (~0.96), Q 20, Q 53, Q 73, Q 78}. Run H1-H5 on the 16-surah set. Bonferroni-16 ≠ Bonferroni-5; report as DIRECTIONAL/exploratory ONLY (MW-7 single-test α=0.05 ceiling).
- **Sub-cluster-Meccan-short**: {Q 87, 91, 92, 76 (Medinan, but qiṣar-tier neighbor)} — the 4 cluster-members in the corpus-tail (mushaf > 75). Test H1 + H4 only.
- **Rules-tuple-variant**: re-derive cluster under (no-tashkeel, last-letter-after-strip) WITHOUT the dagger-alif. Does the 8-cluster survive?
- All sub-tests are POST-HOC and capped at single-test α=0.05 ceiling per [[INVESTIGATION-PROTOCOL|Protocol]] §1.7 (MW-7).

## 6. Outputs

- Pre-reg file: this document.
- Run script: `/Users/grey/Downloads/quran/scripts/h_new_910_alif8_cluster.py`.
- JSON output: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-910-alif8-cluster.json`.
- Findings markdown: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-910-alif8-cluster.md`.
- Updates to MASTER-FINDINGS-LEDGER, KNOWLEDGE-GRAPH, Q017 cross-references, Q033 06-novel-findings link.

## 7. SHA256 lock-in

This file's SHA256 is computed AFTER its content is finalized and embedded in the run script. The run script verifies the SHA at runtime — fail-fast if mismatched.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
