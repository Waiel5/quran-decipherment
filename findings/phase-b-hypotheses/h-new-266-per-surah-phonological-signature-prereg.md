---
id: H-NEW-266
title: Per-surah phonological signature test
status: PRE-REGISTERED (locked before run)
date_prereg: 2026-04-18
seed: 20260418
bonferroni_family: h-new-266-per-surah-phonological-signature
bonferroni_k: 5
alpha: 0.05
alpha_bon: 0.01
n_perms: 5000
mw5_n_perms: 1000
rules_tuple: (quran-no-tashkeel, 28-letter orthographic normalization, exact surah letter counts preserved, 114 surahs, Hafs-Kufan, seed 20260418)
direction_primary: "POSITIVE — observed per-surah sound-signature dispersion exceeds the exact length-matched random-partition null."
---

# [[h-new-266-per-surah-phonological-signature|H-NEW-266]] — Per-surah phonological signature test (pre-registration)

## Question

Do the 114 surahs exhibit **non-random per-surah sound-signature structure**
on a small, locked family of classical-tajwid-relevant letter-class
densities, beyond what would arise from a random repartition of the same total
letter inventory into the same 114 surah lengths?

This finding is intentionally conservative. It does **not** ask whether any
single surah is "special" in a literary or theological sense. It asks a
bounded empirical question: are surah-level phonological-density profiles more
dispersed than a length-matched null built from the Quran's own aggregate
letter inventory?

## Motivation

Existing phonology findings already show that:

- `[[h-new-165-phonological-predictor|H-NEW-165]]` / `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` recover muqaṭṭaʿāt structure from classical
  tajwid-phonology codebooks.
- `[[h-new-182-phonological-vectors|H-NEW-182]]` builds per-surah phonological vectors and finds nontrivial
  corpus-wide structure.

Those findings operate on broader feature bundles or muqaṭṭaʿāt-specific
questions. `[[h-new-266-per-surah-phonological-signature|H-NEW-266]]` narrows the target: a **small locked family** of
classical-recitation-relevant letter classes, tested directly at the
**per-surah density** level under an exact length-matched null.

## Locked feature family

The family is fixed at 4 class densities plus 1 omnibus summary. All class
members are defined over a **28-letter normalized orthography**:

- alif variants `ٱ أ إ آ` -> `ا`
- hamza-on-seat `ؤ` -> `و`, `ئ` -> `ي`
- tāʾ marbūṭa `ة` -> `ه`
- alif maqṣūra `ى` -> `ي`
- any glyph outside the 28-letter set is dropped from the letter stream

### Locked classes

1. **Core emphatic** = `{ص, ض, ط, ظ}`
   Rationale: the narrow tafkhīm / iṭbāq core, standard in Arabic phonology.

2. **Strict throat** = `{ع, ح, خ, غ}`
   Rationale: halq-oriented guttural class. Glottals `{ء, ه}` are omitted
   deliberately because 28-letter normalization and tāʾ marbūṭa handling make a
   strict glottal analysis less stable in this pipeline.

3. **Sibilant / ṣafīr** = `{س, ز, ص}`
   Rationale: the classical ṣafīr set.

4. **Idghām-sonorant** = `{ي, ر, م, ل, و, ن}`
   Rationale: the classical `يرملون` set is directly tajwid-relevant and is
   also a reasonable sonorant-heavy class (glides, liquids, nasals).

### Overlap disclosure

These classes are **not disjoint**. In particular `ص` belongs to both the
emphatic and ṣafīr classes. This is allowed and disclosed. The goal is not a
partition of the alphabet but a small family of recitation-relevant densities.
No inflated claim of cross-cell independence is made.

## Data and unit of analysis

- Corpus: `quran-text/quran-no-tashkeel.json`
- Unit: surah body as given in the JSON, concatenating all verse texts per
  surah
- N = 114 surahs
- Primary denominator per surah: number of retained normalized 28-letter
  characters in that surah

For each surah `i`, let `d_i(c)` be the retained-letter density of class `c`.
For the whole corpus, let `p(c)` be the global retained-letter density of class
`c`.

## Pre-committed statistics

Five Bonferroni-registered cells:

### Cell A — Omnibus signature dispersion

Statistic:

`S_A = mean_i || d_i - p ||_2`

where `d_i` is the 4-dimensional surah signature vector and `p` is the global
4-dimensional density vector.

Interpretation: average Euclidean distance of surah signatures from the corpus
mean signature.

Direction: one-sided **upper**.

### Cells B-E — Class-specific dispersion

For each locked class `c`, statistic:

`S_c = mean_i | d_i(c) - p(c) |`

Interpretation: average absolute deviation of surah class-density from the
corpus baseline.

Direction: one-sided **upper** for all 4 cells.

Cell mapping:

- Cell B: core emphatic
- Cell C: strict throat
- Cell D: ṣafīr sibilant
- Cell E: idghām-sonorant

## Null model (locked)

### Primary null

Null hypothesis: the observed between-surah dispersion is explainable by
randomly repartitioning the Quran's retained letters into 114 surahs with the
**exact observed surah letter counts preserved**.

Implementation:

1. Normalize the Quran to the locked 28-letter stream.
2. Collapse letters into 6 disjoint categories sufficient for the 4 classes:
   - `sad_shared = {ص}`
   - `emphatic_only = {ض, ط, ظ}`
   - `throat = {ع, ح, خ, غ}`
   - `sibilant_only = {س, ز}`
   - `sonorant = {ي, ر, م, ل, و, ن}`
   - `other = all remaining normalized letters`
3. For each permutation draw, repartition the total category inventory across
   the 114 observed surah lengths using the exact sequential multivariate
   hypergeometric construction.
4. Reconstruct the 4 class densities from those 6-category counts.
5. Compute cells A-E.

This null preserves:

- exact surah length profile
- exact global class totals
- exact covariance induced by the only overlap in the family (`ص` shared by
  emphatic and ṣafīr)

Repeat `N_PERMS = 5000` with seed `20260418`.

## MW-1 length control

Length is controlled at the **primary null** level by preserving the exact
observed retained-letter count of every surah. No additional residualization is
applied.

## MW-5 positive control (locked)

Because the primary null is a repartition null, we include a planted synthetic
positive control that should obviously register non-random per-surah signature
structure if the instrument is working.

Construction:

1. Use the observed 114 surah lengths.
2. Use the observed corpus-wide 6-category probability vector as the baseline.
3. Assign surahs cyclically to 4 synthetic blocks by `(surah_id - 1) mod 4`.
4. For each block, deterministically boost one signature component by
   transferring mass from `other`:
   - block 0: `sad_shared +0.015`, `emphatic_only +0.045`
   - block 1: `throat +0.060`
   - block 2: `sad_shared +0.015`, `sibilant_only +0.045`
   - block 3: `sonorant +0.080`
5. For each surah, convert the block-specific probability vector into integer
   6-category counts by largest-remainder allocation at that surah's exact
   length.
6. Run the same A-E statistics and the same repartition null with
   `MW5_N_PERMS = 1000`.

**MW-5 pass rule**: Cell A must pass at `alpha_bon = 0.01`, and at least 3 of
4 class cells (B-E) must also pass at `alpha_bon = 0.01`. If not,
`[[h-new-266-per-surah-phonological-signature|H-NEW-266]]` is reported as `NULL-BROKEN`.

This MW-5 is explicitly synthetic and only checks instrument sensitivity, not
Arabic realism.

## Bonferroni discipline

Family size `k = 5`:

- A omnibus
- B emphatic
- C throat
- D sibilant
- E sonorant

Per-cell threshold:

`alpha_bon = 0.05 / 5 = 0.01`

No additional inferential cells are allowed in this finding.

## Decision rule

Per cell:

- PASS iff observed statistic > null 95th percentile **and**
  `p_perm < 0.01`
- else NULL

Overall verdict:

- `NULL-BROKEN` if MW-5 fails
- `PASS-DIRECTED` if Cell A passes and MW-5 passes
- `PARTIAL-CLASS-ONLY` if Cell A is NULL but one or more of Cells B-E pass and
  MW-5 passes
- `NULL` otherwise

The primary question is answered by **Cell A**. Cells B-E only localize which
locked densities contribute to the omnibus result.

## Descriptive outputs (not extra inferential cells)

The script may report, descriptively only:

- global class densities
- per-surah observed densities
- per-surah null z-scores and two-sided empirical extremity for each locked
  class
- top positive / negative outlier surahs per class

These descriptive rows are **not** separate hypothesis tests and do not alter
the Bonferroni family.

## Garden-of-forking-paths log

1. **Why these four classes?**
   They are directly classical-recitation-relevant, small, interpretable, and
   already compatible with existing project phonology codebooks. I excluded
   broader place-of-articulation partitions because they would dilute the
   specific "sound-signature" question.
2. **Why omit glottals?**
   In this pipeline, glottal handling is less stable because 28-letter
   normalization collapses seat-hamza variants and maps `ة` to `ه`. The strict
   throat class avoids that ambiguity.
3. **Why dispersion rather than clustering or classification?**
   Dispersion answers the present question most directly and conservatively:
   are surah signatures more heterogeneous than random length-matched
   segmentation?
4. **Why one omnibus + four localizers?**
   The omnibus answers the overall question; the four localizers say where the
   signal sits without expanding to a large feature family.

## Honest limits (stated before run)

- This is still an **orthography-derived** phonological proxy, not a full IPA
  recitation model.
- The null destroys lexical, morphological, and semantic structure. A PASS
  therefore shows only that surah-level sound-class concentrations are stronger
  than random repartition, not that they are independent of lexical content.
- Equal weighting over 114 surahs means very short surahs count the same as
  very long surahs in the dispersion statistic. That is intentional because the
  target is per-surah structure, but it makes the analysis sensitive to the
  short-tail.
- The four cells are correlated; Bonferroni is conservative and no effective-k
  discount is claimed.
- A NULL does not show "no phonological design"; it only shows no detectable
  dispersion excess on this locked 4-class family under this null.

## Deliverables

1. This prereg file.
2. `scripts/h_new_266_per_surah_phonological_signature.py`
3. `findings/phase-b-hypotheses/csv/h-new-266.json`
4. `findings/phase-b-hypotheses/h-new-266-per-surah-phonological-signature.md`
5. `journal/h-new-266-run-1.md`

## Sign-off

Seed locked: `20260418`.
Bonferroni locked: `k = 5`, `alpha_bon = 0.01`.
Feature family locked before run.
