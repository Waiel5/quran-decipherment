---
finding_id: h-new-155
title: "Q 1 al-Fātiḥa sui-generis-liturgical classification — vocabulary dispersion test"
specialist: specialist-B (quran-equation-solvers)
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 2
bonferroni_family: h-new-155-q1-sui-generis
alpha_bon: 0.025
alpha_raw: 0.05
parent_findings: [h-new-150 (Q 1 anti-counterexample: max-liturgy min-cluster-degree), h-new-89 (Q 1 structurally isolated), scratch Q 1 nearest-neighbors]
rules_tuple: "(114 surahs Hafs-Kūfan; QAC v0.4 STEM roots; Q 1 vocabulary = distinct STEM roots in Q 1)"
pre_reg_standard: PRE-REG-STANDARD-04
---

# [[h-new-155-q1-sui-generis|H-NEW-155]] — Q 1 al-Fātiḥa sui-generis-liturgical classification

## Motivation

[[h-new-150-liturgical-hub|H-NEW-150]] found that Q 1 al-Fātiḥa has the MAXIMAL liturgical
prominence (recited in every prayer cycle) but the MINIMAL cluster-
network degree (1). This breaks the "liturgical-hub" pattern that holds
for Q 2, 3, 50, 59, 62, 112-114 (all high-liturgical AND high-cluster-
degree).

**Hypothesis**: Q 1 is a DIFFERENT KIND of liturgical-central surah —
"sui-generis-liturgical" rather than "hub-liturgical". Operationally:
Q 1's vocabulary is DISPERSED across the corpus (every other surah
echoes Q 1), while hub-liturgical surahs have their vocabulary
CONCENTRATED in specific clusters.

If true, Q 1 acts as a "seed" or "index" whose content spreads
throughout the Quran, whereas Q 2 or Q 112 act as "nodes" with strong
but localized connections.

## Hypotheses

### Cell A — Q 1 vocabulary DISPERSION (PRIMARY 1/2)

**H_0**: The distinct STEM roots appearing in Q 1 (~20 roots across 7
verses) are DISTRIBUTED ACROSS THE CORPUS similarly to any randomly-
selected 7-verse window of the same vocabulary size.

**H_1**: Q 1's distinct roots appear in MORE surahs (higher "dispersion")
than a random 7-verse-window-matched null.

**Statistic**: "dispersion" = fraction of 114 surahs that contain at
least ONE of Q 1's distinct STEM roots.

Null: sample 10,000 random 7-verse windows from the corpus; for each,
compute the window's distinct roots and the fraction of 114 surahs
echoing at least one.

**PASS**: observed Q 1 dispersion > 95th percentile of null, p < 0.025.

### Cell B — Q 1 vs Q 2 vs Q 112 DISPERSION comparison (PRIMARY 2/2)

Q 2 and Q 112 are high-liturgical AND high-cluster-degree — "hub-
liturgical" archetypes. Q 1 is the sui-generis-candidate.

Compare dispersion per 7-verse-vocabulary-matched subset:
- Q 1's 7 verses → distinct roots → dispersion
- First 7 verses of Q 2 → dispersion (matched sample; first 7 is
  canonical cut given Q 2's 286 verses)
- All of Q 112 (4 verses; pad with v1 of Q 113 for matched length)
  OR use Q 112's 4 actual verses (no padding)

Locked comparison: Q 1 (7 verses, ~20 roots) vs Q 2:1-7 (7 verses, ~30
roots) vs Q 112+113:1-2 (7 verses total, padded).

**H_0**: Q 1 dispersion is NOT distinctively higher than Q 2 and Q 112
dispersion normalized by vocabulary size.

**H_1**: Q 1 has HIGHER DISPERSION PER ROOT than Q 2 AND Q 112.

**Test**: per-root dispersion = (for each root in a surah's
vocabulary, count surahs where root appears) / vocab_size. Average
across roots. Compare.

PASS: Q 1's average-dispersion-per-root > Q 2's AND > Q 112's, with
randomized-matched-length permutation p < 0.025.

## MW-5 positive control

Use Q 12 Yūsuf as known-CONCENTRATED-vocabulary surah ([[h-new-86-surah-name-as-key-root|H-NEW-86]] found
Q 12's eponymous name-root has 532× enrichment). Q 12's vocabulary
should have LOWER dispersion than random. If Q 12 fails this
expectation, pipeline broken.

## Method

### Data
- QAC v0.4 STEM root tokens per verse.
- Corpus of (sid, vid) → set of distinct STEM roots.

### Procedure
1. Extract Q 1's distinct root set: R_Q1.
2. For each root r ∈ R_Q1: count n_surahs_containing_r.
3. Dispersion_Q1 = avg over r ∈ R_Q1 of (n_surahs_containing_r / 114).
4. Null: sample 10,000 random 7-verse windows. For each window, compute
   its distinct root set and average dispersion.
5. p = fraction of null windows with dispersion ≥ Q 1's.

Cell B: same procedure for Q 2:1-7 and Q 112+113:1-2, compare.

MW-5: Q 12 all-verses dispersion vs random null.

## Garden of forking paths

- **Dispersion = fraction-of-surahs-containing, not count-of-occurrences**:
  captures how WIDELY the root appears, not how INTENSELY.
- **Q 1 entire vs 7-verse-window**: Q 1 is 7 verses, so its full
  vocabulary = 7-verse window naturally.
- **Matched-length 7-verse windows** for null: matches Q 1's verse count.
- **Q 2:1-7 and Q 112+113:1-2** for Cell B: locked sample cuts.
- **Direction positive** (Q 1 > null, Q 1 > Q 2/112): theoretically
  motivated by [[h-new-150-liturgical-hub|H-NEW-150]]'s anti-counterexample.
- **10K null samples**: standard for p ~ 0.025.
- **Bonferroni k=2** over Cells A and B; MW-5 is validation not inference.

## Pre-committed acceptance matrix

| Cell A | Cell B | Verdict |
|---|---|---|
| PASS | PASS | SUI-GENERIS-CONFIRMED — Q 1 is empirically distinct as a high-dispersion liturgical-central surah |
| PASS | FAIL | HIGH-DISPERSION-ONLY — Q 1 dispersed but not distinctively more than Q 2/112 |
| FAIL | PASS | DIFFERENTIAL — Q 1 distinctive relative to Q 2/112 but not vs random |
| FAIL | FAIL | NULL — Q 1's sui-generis-liturgical hypothesis not supported at this axis |

## Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_155_q1_sui_generis.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-155.json`
- Findings: `findings/phase-b-hypotheses/h-new-155-q1-sui-generis.md`
- Journal: `journal/h-new-155-run-1.md`

Runtime <1 min.
