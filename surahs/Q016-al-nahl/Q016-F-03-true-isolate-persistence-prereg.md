---
finding_id: Q016-F-03
title: True-isolate persistence of Q 16 across 8 alternative similarity instruments
phase: B+
status: PRE-REGISTERED (locked before computation)
date: 2026-05-07
specialist: Q016-al-nahl-specialist
seed: 20260507
n_perm: 10000
bonferroni_family: Q016-F-03-true-isolate-instruments
bonferroni_k: 8
alpha_bon: 0.00625
direction: one-sided LOWER on "mean similarity to nearest 3 surahs" (Q 16 LOW = isolated)
success_criterion: ≥6 of 8 instruments place Q 16 in the bottom-quartile (rank ≤ 28/114) of mean-top-3-neighbor similarity. STRICT: 6/8 with all individual permutation p ≤ α_bon = 0.00625.
failure_criterion: <4/8 instruments place Q 16 in bottom-quartile.
rules_tuple: "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
script: surahs/Q016-al-nahl/scripts/Q016_F_03_true_isolate_persistence.py
output_json: surahs/Q016-al-nahl/csv/Q016-F-03.json
parent_oq: OQ-2 (Q 16-25 cluster-empty zone)
parent_finding: H-NEW-126 (true-isolate core {Q 16, 21, 22, 23, 25})
design_parent: Q025-F-01 (same 8-instrument battery; design re-used identically)
---

# Q016-F-03 — True-isolate persistence (pre-reg)

## 1. Hypothesis

H-NEW-126 identified Q 16 as a member of the 5-surah true-isolate core {Q 16, 21, 22, 23, 25}. This test asks whether Q 16's isolate-ness is **instrument-fragile** or **instrument-robust**.

**Pre-committed direction**: under each of 8 alternative similarity instruments, Q 16's mean similarity to its 3 nearest non-self neighbors places Q 16 in the bottom-quartile (rank ≤ 28/114).

## 2. Why this is the right question

OQ-2 status is "ANSWERED via H-NEW-168 concentrator-mode" for the **Q 16-25 zone as a whole**, but the per-surah question — *is Q 16 specifically still an isolate after we change instruments?* — has not been bounded. Q016-F-03 closes that.

The 8-instrument battery DESIGN is shared with Q025-F-01 (specialist-coordinated; non-overlapping Q-target). This is mirrored implementation, NOT a duplicate of the lead-test (which targets Q 25).

## 3. The 8 instruments (battery shared with Q025-F-01)

For each instrument, build a 114×114 surah-similarity matrix; for each surah s compute `mean_top3_sim(s)` = mean similarity to its 3 most-similar non-self surahs. **Lower values = more isolated.**

1. **I1 — root-Jaccard** (QAC v0.4 stems): Jaccard of unique-root sets per surah.
2. **I2 — content-cosine** (no-tashkeel orthographic tokens, IDF-weighted): standard TF-IDF cosine.
3. **I3 — char-trigram-Dice**: Dice coefficient on character 3-gram sets (no-tashkeel concatenated surah text).
4. **I4 — Fisher-Rao distance** on QAC-root probability vectors (read from h-new-111 D matrix). SIMILARITY = `1 / (1 + d_FR)`.
5. **I5 — rhyme final-letter cosine**: per-surah final-letter probability vector, cosine similarity.
6. **I6 — root Zipf-overlap**: weight each shared root by `1 / log(1 + corpus_freq)` (rare roots count more), Jaccard-style normalization.
7. **I7 — divine-name overlap**: per-surah count vector over the 99 names of Allah (`data/asma-al-husna.txt`), Jaccard on attested-name sets.
8. **I8 — character-5-gram NCD-proxy**: 1 − Dice of character 5-gram sets (no-tashkeel).

For each instrument, compute Q 16's `mean_top3_sim` rank, and a permutation null on the rank under random-relabeling of the 114 surah identities (10000 perms).

## 4. Bonferroni accounting

k = 8 instruments → α_bon = 0.05 / 8 = 0.00625.

## 5. Acceptance / failure window

- ≥ 6/8 instruments place Q 16 in bottom-quartile (rank ≤ 28) AND each passes per-instrument permutation null at α_bon ⇒ **CONFIRMED isolate-persistence**.
- 4–5/8 ⇒ **DIRECTIONAL**.
- < 4/8 ⇒ **NULL / RULES-TUPLE-FRAGILE**.

## 6. Direction is locked LOW

Pre-committed: Q 16 has LOW `mean_top3_sim`. Reverse direction (Q 16 in TOP quartile) is a pre-commit violation (PRE-REG-STANDARD-01).

## 7. MW protections

- MW-1: all 8 instruments specified above.
- MW-2: per-instrument 10000-permutation null on the rank-statistic.
- MW-3: 8-instrument family inherently spans distinct mathematical instruments.
- MW-5 (positive-control): the ḥawāmīm cluster {Q 40-44} should NOT be in the bottom-quartile of `mean_top3_sim` for I1 (root-Jaccard) and I2 (content-cosine), since H-NEW-126 MW-5 already established it FIRES at α=0.05 on root-Jaccard cluster cohesion.
- MW-6: bottom-quartile threshold is corpus-relative.
- MW-7: the rank ≤ 28 threshold is PRE-REGISTERED.

## 8. Garden-of-forking-paths log

- Identical to Q025-F-01 garden-of-forking-paths log (8 not 5 or 10; nearest-3 not 1 or 5; bottom-quartile not bottom-decile). Inherited from the design parent.
- **Departure from Q025-F-01**: target surah is Q 16 (not Q 25). All other parameters identical.

## 9. Files

- Pre-reg: `surahs/Q016-al-nahl/Q016-F-03-true-isolate-persistence-prereg.md`
- Script: `surahs/Q016-al-nahl/scripts/Q016_F_03_true_isolate_persistence.py`
- Output: `surahs/Q016-al-nahl/csv/Q016-F-03.json`

*PRE-REG LOCKED 2026-05-07.*
