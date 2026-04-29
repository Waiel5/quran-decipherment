---
id: Q019-F-01
title: Maryam token-concentration (vs Yūsuf-Q12 92.6% comparator) — Maryam ranks 4th not 1st (DIRECTION-LOCKED)
phase: B+
date: 2026-04-28
agent: Q019-maryam-specialist (Wave-D)
test: corpus-wide proper-noun token concentration percentile + Fisher-Rao rank
rules_tuple: (no-tashkeel, orthographic-token, exact-substring "مريم", basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
seed: 20260428
bonferroni_k: 4
bonferroni_family: Q019-novel-findings
alpha_bon: 0.0125
---

# Q019-F-01 — Pre-registration

## Hypothesis (DIRECTION-LOCKED)

**H1 (anticipated NULL)**: Q 19 Maryam's *Maryam-token concentration* is **NOT rank-1 in the corpus**. The Yūsuf-Q12 model (proper-noun-token saturation = 92.6% of corpus *yūsuf* tokens in Q 12 alone) does NOT generalize to Q 19. Pre-flight scan showed Q 5 al-Māʾida leads at 29.4%; Q 19 ranks ~4th.

**Direction**: Predicted FALSIFICATION of the Yūsuf-Q12 model for Q 19. The pre-reg captures this *honestly*: I observed the data BEFORE writing this pre-reg (during data exploration in `02-content-analysis.md`), so this is best classified as a **CONFIRMATORY pre-reg of an already-observed direction** under MW-7 (post-hoc cap = single-test α=0.05 ceiling unless replication exists).

**Predicted ranks** (locked):
- Q 5 al-Māʾida: rank 1 in Maryam-token absolute count
- Q 3 Āl ʿImrān: rank 2
- Q 4 al-Nisāʾ: rank 3
- **Q 19 Maryam: rank 4**, with concentration ≈ 8.8% of corpus total

## Null distribution

Permutation: redistribute Maryam tokens uniformly at random across the 12 surahs that contain ≥1 Maryam token, weighting by surah length. 10,000 perms, seed 20260428.

Test statistic: rank-position of Q 19 in the Maryam-token frequency table.

Under permutation null, the probability of Q 19 ranking ≤ 4 is computable via the multinomial-permutation distribution.

## Direction of effect

**Q 19 rank > 1** (i.e., Q 19 is NOT the rank-1 surah by Maryam-token count).

This is a **falsification-prediction**: standard Yūsuf-Q12 model predicts rank-1 for the eponym; we predict rank ≥ 2.

## Bonferroni correction

α = 0.05 / 4 = **0.0125** (Q019-novel-findings family of 4 tests).

## Success / failure criteria

- **PASS** = Q 19 rank > 1 (Yūsuf-model FALSIFIED for Q 19)
- **FAIL** = Q 19 rank = 1 (Yūsuf-model VINDICATED for Q 19)

## Secondary tests

- (a) Q 19's Maryam-pericope (vv. 16–40) length percentile in corpus distribution of "named-figure narrative pericopes". Compare to Yūsuf-pericope length in Q 12 (vv. 4–101 = 98 verses).
- (b) FR-distance Q 19 ↔ Q 5, Q 3, Q 4 (the three Maryam-richer surahs): are Q 5/Q 3/Q 4 the Q 19 FR-nearest neighbors? (Pre-flight: Q 19 FR-nearest is Q 43, Q 21, Q 46, Q 41, Q 36 — NOT Q 5/Q 3/Q 4. Predicted: Q 5/Q 3/Q 4 in Q 19's *FR-mid-range*, not FR-near.)

## MW-1..MW-7 protections

- MW-1: substring count rule pre-specified.
- MW-2: 10K perms locked.
- MW-3: 2 secondary tests locked.
- MW-4: not applicable (no fitted parameters).
- MW-5: replicate at K=1000 stem-roots (vs default K=500); replicate using QAC LEM:maryam if found in QAC index.
- MW-6: control = randomly-shuffled corpus assignment.
- MW-7: post-hoc cap respected — verdict cap at single-test α=0.05.

## Garden-of-forking-paths log

- Originally considered (Yūsuf-Q12-style) hypothesis: "Q 19 Maryam-token-concentration ≥ 90%". After pre-flight scan revealed Q 5 leads at 29.4%, the directional prediction was REVERSED to "Q 19 NOT rank-1". This is honestly-reported.
- The reversed prediction is locked here BEFORE final run + replication.

## SHA256

To be computed at runtime by `scripts/Q019_F_01_maryam_token_concentration.py` and verified.
