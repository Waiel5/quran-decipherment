---
finding_id: h-new-132
title: "Q7 Al-A'raf vs Q11 Hud prophet-cycle parallelism"
specialist: codex
date_prereg: 2026-04-18
seed: 20260418
bonferroni_k: 2
bonferroni_family: h-new-132-q7-q11-prophet-cycle
alpha_bon: 0.025
alpha_raw: 0.05
direction_primary: "Across the five shared prophet blocks {Noah, Hud, Salih, Lot, Shuayb}, the canonical Q7<->Q11 same-prophet assignment minimizes total PN-stripped Fisher-Rao distance relative to all 5! alternative bijections."
direction_secondary: "Using the same 5x5 distance matrix, row-wise nearest-neighbor recovery from Q7 blocks to Q11 blocks returns all five canonical same-prophet matches more often than expected under label permutation."
positive_control: "PN-only exact-assignment control on the same five windows recovers the canonical mapping; if it fails, the extraction/permutation pipeline is broken."
rules_tuple: "(QAC-v0.4 morphology roots; POS!=PN for primary/secondary, POS=PN lemmas for positive control; Hafs-Kufan verse numbering; basmala counted only in Surah 1; Fisher-Rao arccos-Bhattacharyya on L1-normalized window distributions; exact 5! assignment null)"
verdict_ceiling: "PASS-DIRECTED"
---

# [[h-new-132-prophet-cycle-parallelism|H-NEW-132]] — Q7 Al-A'raf vs Q11 Hud prophet-cycle parallelism

## Question

Do Q 7 al-A'raf and Q 11 Hud instantiate the same shared prophet-cycle in a
formally recoverable way, once we remove the trivial prophet-name signal and
measure only the PN-stripped root-distribution geometry of their corresponding
prophet blocks?

This is a bounded follow-up to the broader prophet-cycle work. It does NOT ask
whether all prophet retellings across the Quran follow one template. It asks a
much narrower question: within the two long Meccan surahs that both contain the
serial run Noah -> Hud -> Salih -> Lot -> Shuayb, do the matched blocks line up
better than alternative cross-surah reassignments?

## Pre-registered windows

The study is restricted to the five shared prophet blocks that form the common
Q7/Q11 cycle core. Moses is EXCLUDED before results because Q 11:96-99 is only
a four-verse coda, not a full parallel block to Q 7:103-160.

### Q7 Al-A'raf windows

- Noah: 7:59-64
- Hud: 7:65-72
- Salih: 7:73-79
- Lot: 7:80-84
- Shuayb: 7:85-93

### Q11 Hud windows

- Noah: 11:25-49
- Hud: 11:50-60
- Salih: 11:61-68
- Lot: 11:77-83
- Shuayb: 11:84-95

These verse spans are frozen from the canonical text after boundary inspection
only. No inter-window similarity matrix was viewed before this pre-reg.

## Data

- Morphology: `data/morphology/quranic-corpus-morphology-0.4.txt`
- Arabic text for boundary sanity only: `quran-text/quran-no-tashkeel.json`

No external corpus, commentary, or manual annotation will be introduced.

## Representation

### Primary / secondary representation

For each of the 10 frozen windows:

1. Parse all morphology rows whose `(surah, verse)` falls inside the window.
2. Keep tokens with a `ROOT:` value and `POS != PN`.
3. Count roots inside the window.
4. Build a shared vocabulary from the union of all roots observed across the 10
   windows.
5. Apply Dirichlet smoothing with `alpha = 0.5` to every root dimension.
6. L1-normalize to a probability vector.
7. Compute Fisher-Rao distance:

`d_FR(p,q) = 2 * arccos(sum_i sqrt(p_i * q_i))`

Lower distance = stronger parallelism.

### Positive-control representation

Repeat the same assignment procedure on PN-only lemma counts:

1. Keep tokens with `POS = PN` and a `LEM:` field.
2. Build per-window lemma-count vectors.
3. L1-normalize with Dirichlet `alpha = 0.5`.
4. Compute Fisher-Rao distances.

This positive control is not substantive evidence. It is a pipeline sanity
check: if the windows do not recover their own prophet labels under PN-only
features, the extraction or permutation machinery is wrong.

## Tests

### Primary test — exact assignment

Let the Q7 windows be ordered as:

`[Noah, Hud, Salih, Lot, Shuayb]`

Let the Q11 windows be ordered in the same canonical order.

Compute the 5x5 PN-stripped Fisher-Rao distance matrix `D`, where `D[i,j]` is
the distance between Q7 prophet-block `i` and Q11 prophet-block `j`.

Observed statistic:

`T_primary = sum_i D[i,i]`

Null:

- Enumerate all `5! = 120` bijections `pi` from the five Q11 blocks to the five
  Q7 rows.
- Compute `T(pi) = sum_i D[i, pi(i)]`.

Exact one-sided p-value:

`p_primary = #{pi : T(pi) <= T_primary} / 120`

The direction is LOWER = better. Canonical mapping passes if `p_primary <
0.025`.

### Secondary test — nearest-neighbor recovery

Using the same PN-stripped matrix `D`:

1. For each Q7 row, identify the Q11 column with minimum distance.
2. Ties are broken by lower Q11 canonical column index.
3. Compute `A_obs = number of rows whose nearest neighbor is the canonical same-prophet column`.

Exact null:

- Under each of the same 120 label permutations `pi`, relabel Q11 columns and
  recompute how many row minima are "correct" under that permuted labeling.

Exact one-sided p-value:

`p_secondary = #{pi : A(pi) >= A_obs} / 120`

Secondary pass requires BOTH:

- `p_secondary < 0.025`
- `A_obs = 5`

This guards against a nominally good assignment sum driven by only a subset of
the rows.

## Positive control

Run the exact-assignment test on PN-only lemma distributions for the same five
windows. The control passes if the canonical mapping is the unique minimum:

- `p_positive_control = 1 / 120`

If this fails, verdict becomes `INSTRUMENT-BROKEN` and the primary/secondary
results are inadmissible.

## Verdict mapping

- `PASS-DIRECTED`: primary passes, secondary passes, positive control passes
- `PARTIAL-PASS`: primary passes, positive control passes, secondary misses
- `NULL`: primary misses but positive control passes
- `INSTRUMENT-BROKEN`: positive control fails

## Garden of forking paths

Frozen before execution:

- Exactly two surahs: Q7 and Q11
- Exactly five shared prophet blocks: Noah, Hud, Salih, Lot, Shuayb
- Moses excluded in advance for asymmetry of window scale
- Exact verse windows above
- Primary features: QAC roots with `POS != PN`
- Positive control: PN lemmas only
- Fisher-Rao metric with Dirichlet `alpha = 0.5`
- Exact 5! permutation null, no Monte Carlo substitution
- Row-wise tie-break for nearest-neighbor = lower canonical Q11 index
- Bonferroni family size `k = 2` for primary + secondary only

Not allowed after results:

- Adding or dropping Lot
- Widening or shrinking any verse window
- Switching to Jaccard, cosine, TF-IDF, edit distance, or embeddings
- Excluding "generic" roots post hoc
- Re-introducing PN tokens into the primary
- Promoting descriptive controls to inferential cells

## Failure modes to report honestly

- Strong positive control + null primary means: the blocks obviously name the
  same prophets, but their PN-stripped narrative vocabulary is not
  assignment-recoverable.
- Primary pass + secondary miss means: there is whole-matrix signal, but not a
  clean 5-of-5 retrieval pattern.
- Lot may be the weak link because Q11's Lot unit is embedded after the
  Abraham-guest transition; that limitation is disclosed in advance and will not
  be repaired post hoc.

## Post-hoc-noticed disclosure

Before writing this pre-reg I inspected the raw Arabic text of Q7:59-93 and
Q11:25-95 only to freeze block boundaries. I did NOT compute or inspect any
cross-window root distances, assignment scores, nearest-neighbor counts, or
permutation results.

## Deliverables

1. This pre-reg
2. `scripts/h_new_132_prophet_cycle_parallelism.py`
3. `findings/phase-b-hypotheses/csv/h-new-132.json`
4. `findings/phase-b-hypotheses/h-new-132-prophet-cycle-parallelism.md`
5. `journal/h-new-132-run-1.md`
