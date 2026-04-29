---
id: H-NEW-264
title: Q 1 "connects everything" follow-up — ḥā-mīm subset root-profile test
phase: B
status: PRE-REGISTERED
date: 2026-04-18
specialist: specialist-B (quran-equation-solvers)
seed: 20260420
bonferroni_k: 2
alpha: 0.05
alpha_bonferroni: 0.025
n_perm: 10000
rules_tuple: "(QAC v0.4 STEM roots via surah-root-graph.json; anchor profile = distinct Q 1 roots; target subset fixed as Q 40-46 ḥm muqaṭṭāʿat; null preserves exact period composition and coarse verse-count bins <10/10-29/30-59/60-99/100+; Hafs-Kūfan; basmala-counted-only-in-surah-1)"
parent_findings: [h-new-89 (Q 1 structurally isolated), h-new-155 (Q 1 root dispersion PASS), h-new-193 (verse-level attractor FAIL), h-new-137/138 (terminal-triad closure)]
pre_reg: findings/phase-b-hypotheses/h-new-264-q1-connects-everything-prereg.md
script: scripts/h_new_264_q1_connects_everything.py
output_json: findings/phase-b-hypotheses/csv/h-new-264.json
---

# [[h-new-264-q1-connects-everything|H-NEW-264]] — Q 1 "connects everything" follow-up

## Question

Q 1 al-Fātiḥa is structurally isolated in the [[h-new-89-meta-cluster-network|H-NEW-89]] classical
cluster-membership taxonomy, yet [[h-new-155-q1-sui-generis|H-NEW-155]] showed that its root
vocabulary is unusually dispersed across the corpus. The bounded
question here is narrower than "Q 1 connects everything":

**Does Q 1's ROOT profile connect anomalously to one pre-specified
classical subset of surahs, namely the ḥā-mīm block Q 40-46?**

This is a follow-up on the tension between:

1. **Isolation** at the membership-taxonomy level ([[h-new-89-meta-cluster-network|H-NEW-89]]), and
2. **Dispersion** at the root-profile level ([[h-new-155-q1-sui-generis|H-NEW-155]]).

The test is intentionally conservative:
- one locked subset only,
- one data family only (QAC STEM roots),
- null matched on period and coarse verse-count bins,
- no search over all subsets after viewing outcomes.

## Why Q 40-46?

The ḥā-mīm surahs are an independently-defined classical multi-surah
subset already locked in [[h-new-89-meta-cluster-network|H-NEW-89]] / [[cross-finding-010-extended-network|cross-finding-010]]. They are not
being created ad hoc for this run.

They are chosen here because several earlier project strands kept
surfacing the Q 40-46 region:
- [[h-new-89-meta-cluster-network|H-NEW-89]] / [[h-new-112-spectral-network|H-NEW-112]] treat it as a coherent classical block.
- [[h-new-193-q1-attractors|H-NEW-193]]'s verse-level touched-set included multiple ḥā-mīm surahs,
  even though the primary "Q 1 touches many surahs" hypothesis failed.
- The general "Q 1 connects everything" queue item asked specifically
  whether Q 1 might connect through a non-membership axis to a specific
  surah-cluster.

This run tests that claim directly, on a single locked subset.

## Data

- `data/morphology/surah-root-graph.json`
- `data/revelation-order.csv`
- `quran-text/quran-no-tashkeel.json` (verse-count only, for length bins)

## Anchor profile

Anchor = Q 1 al-Fātiḥa's distinct QAC STEM root set.

Let `R_Q1` be the set of distinct STEM roots appearing in surah 1.

No token-frequency weighting inside Q 1 is used for the primary cell:
the unit is the presence/absence root profile of Q 1.

## Target subset

Locked target subset:

`S_hm = {40, 41, 42, 43, 44, 45, 46}`

No alternative subsets will be promoted to primary if this one fails.

## Matching null

For both inferential cells, the null is built from random 7-surah sets
drawn WITHOUT replacement from the 113 non-Q1 surahs, preserving:

1. exact Meccan/Medinan composition of `S_hm`, and
2. exact coarse verse-count-bin composition of `S_hm`.

Locked verse-count bins:
- `<10`
- `10-29`
- `30-59`
- `60-99`
- `100+`

This is stricter than a plain random-7-surah null and is intended to
reduce trivial confounding from the fact that the ḥā-mīm block is all
Meccan and mid-length.

Seed 20260420. `N = 10000` permutations.

## Inferential cells

### Cell A — Unweighted recall (PRIMARY)

For each surah `s` in `S_hm`, define:

`recall_Q1(s) = |R_Q1 ∩ R_s| / |R_Q1|`

Observed statistic:

`A_obs = mean_{s in S_hm}(recall_Q1(s))`

**Direction**: upper-tail. Q 1 should have higher mean recall inside
Q 40-46 than matched random 7-surah subsets.

### Cell B — IDF-weighted recall (SECONDARY but inferential)

For each root `r`, define:

`idf(r) = log(114 / df(r))`

where `df(r)` is the number of surahs containing root `r`.

For each surah `s` in `S_hm`, define:

`idf_recall_Q1(s) = sum_{r in R_Q1 ∩ R_s} idf(r) / sum_{r in R_Q1} idf(r)`

Observed statistic:

`B_obs = mean_{s in S_hm}(idf_recall_Q1(s))`

**Direction**: upper-tail.

Purpose: ensure any signal is not driven only by the most ubiquitous
Q 1 roots (`Alh`, `rbb`, `rHm`, etc.). If Cell A passes but Cell B
fails, the result is weaker and may reflect only generic theological
vocabulary.

## MW-5 positive control

To confirm the instrument can recover a known cluster-linked profile,
run the same two metrics on:

- anchor surah: **Q 62 al-Jumuʿah**
- subset: **{57, 59, 61, 64}** (musabbiḥāt inner-5 excluding the anchor)

Use the same matched-null logic: preserve exact period and coarse
verse-count-bin composition of the musabbiḥāt control subset.

Expectation: both control p-values < 0.05.

If not, treat the instrument as suspect.

## Bonferroni family

Family = the two inferential cells on the one locked subset.

- `k = 2`
- `alpha_bon = 0.025`

MW-5 is validation only and does not enter the family count.

## Pass / fail criteria

**CONFIRMED**
- Cell A p < 0.025, and
- Cell B p < 0.025, and
- MW-5 positive control passes.

**PARTIAL-UNWEIGHTED-ONLY**
- Cell A p < 0.025, but
- Cell B p >= 0.025, and
- MW-5 passes.

**FAIL**
- Cell A p >= 0.025, regardless of Cell B, with MW-5 passing.

**INSTRUMENT-SUSPECT**
- MW-5 fails.

## Garden-of-forking-paths lock

- Fixed subset: Q 40-46 only.
- Fixed anchor: Q 1 only.
- Fixed data family: QAC STEM roots only.
- Fixed cells: unweighted recall + IDF-weighted recall.
- Fixed null: exact period + coarse length-bin matched random 7-surah sets.
- Fixed bins: `<10`, `10-29`, `30-59`, `60-99`, `100+`.
- Fixed seed: 20260420.
- Fixed permutations: 10,000.
- Fixed direction: upper-tail for both cells.
- No search across all classical clusters will be performed post hoc.

## Honest scope

This pre-reg does **not** test:
- whether Q 1 is uniquely closest to the ḥā-mīm block among all subsets,
- whether other subsets also connect to Q 1,
- phrase-level or char-gram similarity,
- wrap-around closure to the terminal triad (already treated separately
  in [[h-new-137-wrap-around-closure|H-NEW-137]] / [[h-new-138-wrap-around-feature-robustness|H-NEW-138]]).

It tests one bounded claim only:

**Q 1's root profile is anomalously concentrated in the ḥā-mīm subset
relative to a period- and length-matched null.**
