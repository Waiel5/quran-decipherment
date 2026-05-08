---
surah: 6
test_id: Q006-F-04
title: Q 6 ↔ Q 21 architectural antipodal-pair — FR-distance vs corpus mean
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 1
bonferroni_family: Q006-F-04-antipodal
alpha_bon: 0.05
direction_locked: ABOVE-CORPUS-MEAN (genre-separation)
---

# Q006-F-04 — Pre-registration: Q 6 ↔ Q 21 architectural antipodal-pair

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** The Fisher-Rao distance between Q 6 (list-form prophet-MAX) and Q 21 (narrative-form prophet-MAX) is **GREATER than the corpus pairwise mean FR-distance**. The two surahs share architectural function (prophet-completeness) but realize it in different RHETORICAL GENRES — list-form *al-ḥujja* genealogical roll-call (Q 6:83-87) vs. narrative-form prophet-cycle (Q 21:48-91). Genre-separation predicts FR-distance ABOVE corpus-mean despite shared lexical content.

**Direction:** ABOVE corpus-mean (LOCKED). The genre-separation hypothesis predicts that despite shared canonical-prophet content, the surahs' overall lexical fingerprint is DIVERGED.

**H0:** d(Q6, Q21) ≤ corpus-mean.

**Pre-commit violation:** d(Q6, Q21) BELOW corpus-mean by ≥ 1 standard deviation. (This would mean shared content overrides genre, refuting the genre-separation hypothesis.)

## 2. Operational definition

**Distance:** Fisher-Rao distance from H-NEW-111 (`findings/phase-b-hypotheses/csv/h-new-111.json`) on QAC v0.4 STEM-roots, top-K=500, Dirichlet α=0.5, L1-normalize. The matrix is pre-computed.

**Corpus reference:** all 6,441 pairwise upper-triangular FR-distances in the H-NEW-111 matrix. Compute corpus mean and standard deviation.

**Cell A:** d(Q6, Q21) — single observed value.
**Cell B:** rank of d(Q6, Q21) within Q 6's 113 distances to other surahs (rank 1 = closest, rank 113 = farthest).
**Cell C:** rank of d(Q6, Q21) within Q 21's 113 distances to other surahs.

Bonferroni k=1 (single primary cell A; B and C are descriptive supplements).

## 3. Test statistic / Success / Failure

- **CONFIRMED:** d(Q6, Q21) > corpus-mean AND d(Q6, Q21) > corpus-median.
- **DIRECTIONAL:** d(Q6, Q21) > corpus-mean but ≤ corpus-mean + 0.5 SD.
- **NULL:** d(Q6, Q21) ≤ corpus-mean.
- **Pre-commit violation:** d(Q6, Q21) ≤ corpus-mean − 1 SD.

## 4. Garden-of-forking-paths log (BEFORE observation)

The Q 21 specialist (Q021-F-01 NULL, Q021-F-02 NULL) established Q 21's prophet-order is NOT closer to other narrative-cycle surahs in aggregate. The author observed in preliminary read of h-new-111 that Q 6's nearest 5 neighbors are {Q 7, Q 10, Q 16, Q 39, Q 2} — i.e., predominantly long-Meccan polemic surahs, not narrative-prophet-cycle surahs. This is a pre-observation; the pre-reg locks the direction-locked corpus-mean comparison ANYWAY.

The hypothesis is: genres separate Q 6 from Q 21 even though both have "prophet-completeness" as architectural function. The locked direction is ABOVE corpus-mean; this is the genre-separation prediction.

If d(Q6, Q21) is BELOW corpus-mean — meaning the two prophet-completeness surahs ARE close — the verdict is NULL/PRE-COMMIT VIOLATION and we publish that as the finding (shared content does override genre).

## 5. Honest limits known a priori

- FR-distance on STEM-roots top-K=500 is one operationalization. Char-4-gram NCD or word-level cosine could give different rankings.
- Both surahs are mid-late Meccan; their neighborhood is naturally long-Meccan polemic. The corpus-mean baseline includes ALL 114 surahs (not length-matched).
- Genre-separation is a theoretical framing; the empirical test is just direction-locked FR-distance vs. corpus-mean.

## 6. Rules-tuple

`(no-tashkeel, QAC-STEM-root, top-500-Dirichlet-alpha=0.5, L1-normalize, Fisher-Rao, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at pre-reg-completion. Embedded into `surahs/scripts/Q006_F_04_antipodal.py`.
