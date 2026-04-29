---
id: H-NEW-68
title: Friday-recitation cluster test (Q 18, 32, 62, 76)
phase: B
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (BEFORE running cluster computation against null)
parent: H-NEW-58c (musabbiḥāt cluster confirmed; instrument validated)
bonferroni_family: 2026-04-15-Wave-Friday-Cluster
bonferroni_k: 4  (4 axes; full grid pre-declared; cluster is single 4-surah set)
alpha_bon: 0.0125  (= 0.05 / 4)
seed: 20260416
rules_tuple: (no-tashkeel; whitespace-tokenized; QAC v0.4 STEM-tokens; basmala-only-in-Q1)
---

# [[h-new-68-friday-cluster|H-NEW-68]] — Friday-Recitation Cluster (Pre-registration)

## Question

Are the four classically-Friday-liturgy surahs — Q 18 al-Kahf, Q 32 al-Sajda,
Q 62 al-Jumuʿah, Q 76 al-Insān — a structurally cohesive cluster (above
random null) on multiple axes? Secondarily: is there a specific Q 18 ↔ Q 62
link beyond the cluster average?

## Locked test set — 4 surahs

Locked **before any computation** is run:

1. **Q 18 al-Kahf** — classically recited every Friday by sunnah (multiple
   ḥadīth: "Whoever recites al-Kahf on Friday, light shines for him from
   one Friday to the next"; reported by al-Ḥākim, al-Bayhaqī, al-Albānī
   graded ṣaḥīḥ).
2. **Q 32 al-Sajda** — classically recited at Fajr Friday (Bukhārī 891,
   Muslim 880: the Prophet ﷺ used to recite al-Sajda + al-Insān at Fajr
   Friday).
3. **Q 62 al-Jumuʿah** — literally "the Friday"; recited in Friday Maghrib
   or Friday ʿIshāʾ in some traditions; obviously the eponymous surah.
4. **Q 76 al-Insān** — classically recited at Fajr Friday paired with
   al-Sajda (Bukhārī 891, Muslim 880).

The 4-surah set is locked by classical liturgical usage. No substitutions.

## Locked similarity axes — 4 axes

Locked **before any computation** is run. For the 4-surah cluster compute
on each axis a CLUSTER COHESION SCALAR. Higher cohesion = more similar within
cluster than typical 4-surah subset.

### Axis 1 — Mean pairwise shared-prefix (chars)

For each of C(4, 2) = 6 surah pairs in the cluster, compute the longest
common character prefix of the surah-1's first verse text (no-tashkeel,
basmala excluded for surahs other than Q1; for Q 62 the first verse is
the actual yusabbiḥu… opener since basmala is not in JSON for non-Q1
surahs). Cluster cohesion = MEAN of the 6 pairwise shared-prefix lengths.

Same instrument as [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] (musabbiḥāt cluster, p = 0.0001 confirmed).

### Axis 2 — Mean pairwise lexical Jaccard (over QAC roots)

For each of 6 pairs, compute |R_A ∩ R_B| / |R_A ∪ R_B| over QAC STEM
roots. Cluster cohesion = MEAN of the 6 pairwise Jaccard values.

### Axis 3 — Length-similarity cohesion (verse-count CV)

For the 4 surahs, compute the coefficient of variation (std / mean) of
their verse counts. LOW CV = surahs are length-similar. Cohesion scalar
= 1 / (1 + CV). Higher = more similar.

### Axis 4 — Divine-name density cohesion (CV)

For the 4 surahs, compute the divine-name density per verse (using
existing divine-names-by-verse.csv: name_sum / verse_count per surah).
Coefficient of variation across the 4 values. Cohesion scalar
= 1 / (1 + CV).

## Null distribution

For each axis, draw 10,000 random 4-surah subsets from the 114 surahs,
EXCLUDING any subset that exactly equals the Friday-cluster set.
Each subset's cohesion scalar is computed identically to the observed
cluster.

For each axis, p = (1 + |{null cohesion ≥ observed cohesion}|) / (1 +
N_null). One-sided test: enrichment = "observed cohesion is unusually
HIGH" (more cohesive than random).

Seed for null shuffle: 20260416.

## Bonferroni declaration (locked)

Family size k = 4 (4 axes for the single Friday cluster). α_bon =
0.05 / 4 = 0.0125.

An axis is declared **significant under Bonferroni** iff its one-sided
p ≤ 0.0125.

## PASS criterion (declared before null draw)

The [[h-new-68-friday-cluster|H-NEW-68]] hypothesis is declared **PASS** iff at least 2 of the 4
axes show cluster cohesion enrichment at α_bon = 0.0125.

If 1 axis is significant → MARGINAL.
If 0 axes are significant → NULL.

The cell-level table will be published in full regardless (no cherry-pick).

## Q 18 ↔ Q 62 specific link (secondary, also pre-registered)

In addition to the cluster test, compute the Q 18 ↔ Q 62 pairwise
similarity on the same 4 axes (where applicable: A1 prefix, A2 jaccard;
A3, A4 are cluster-level). Compare against a 10K null of all (i, j) pairs
where i ≠ j, 1 ≤ i, j ≤ 114, excluding the Q 18-Q 62 pair. Bonferroni-2
correction (k=2 axes; α_bon-Q18-Q62 = 0.025).

This is a SECONDARY test pre-registered alongside the cluster test, NOT
a post-hoc inspection. Q 18 + Q 62 are the two surahs with the most
unambiguous Friday-specific tradition (al-Kahf is THE Friday surah; al-
Jumuʿah literally means "Friday").

## Method-witness — MW-5 (musabbiḥāt cluster confirmed)

The shared-prefix cluster instrument (Axis 1) was independently validated
by [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] on the musabbiḥāt cluster (Q 57, 59, 61, 62, 64) yielding
p = 0.0001 against 10K random 5-surah subsets. The same metric definition
is used here. No additional MW-5 needed (instrument already passed on
unrelated cluster).

## Garden-of-forking-paths disclosure

Choices fixed *before* seeing any cluster cohesion number:

- 4-surah cluster (not 3 or 5) chosen because the classical Friday
  liturgy specifically calls for these 4 surahs. Q 18 (whole Friday),
  Q 32 + Q 76 (Fajr Friday paired), Q 62 (the Friday surah). No other
  surah has comparable classical Friday-specific liturgical status.
  Q 87 al-Aʿlā and Q 88 al-Ghāshiya are Friday-prayer recitations in
  some traditions but are not Friday-SPECIFIC (also recited at ʿĪd).
- 4 axes chosen to span: structural-formula (A1 prefix), lexical (A2
  jaccard), prosodic-length (A3 verse-count CV), theological-density
  (A4 divine-name CV). Cluster-level CV chosen for A3, A4 because they
  are properties of the SET, not of pairs. This matches the [[h-new-58c-musabbihat-tense-split|H-NEW-58c]]
  cluster framework.
- Bonferroni k = 4 (one cluster × 4 axes), NOT k = 6 pairs × 4 axes
  = 24. The cluster-cohesion scalar IS one number per axis, not 6
  numbers. The Q18-Q62 secondary test gets its own k=2 Bonferroni and
  is not pooled into k=4.
- Null is "any 4-surah subset" (not adjacency-restricted) because the
  Friday cluster is NON-ADJACENT (Q 18, 32, 62, 76 are spread across
  the muṣḥaf). Adjacency null would be inappropriate.
- Excluded from null: only the EXACT cluster {18, 32, 62, 76}. Subsets
  containing 1, 2, or 3 of the Friday surahs are NOT excluded — this
  matches the [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] convention.
- Cohesion scalar 1/(1+CV) for A3, A4 chosen over alternatives (1-CV,
  exp(-CV)) because it bounds in [0, 1] and behaves smoothly for
  small CV.

## Data + outputs

- Input corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Input morphology: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`
- Input divine-names: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/divine-names-by-verse.csv`
- Script: `/Users/grey/Downloads/quran/scripts/h_new_68_friday_cluster.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-68.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-68-friday-cluster.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-68-run-1.md`

## Status

PRE-REGISTERED 2026-04-15. Spec locked before running cluster-vs-null script.
