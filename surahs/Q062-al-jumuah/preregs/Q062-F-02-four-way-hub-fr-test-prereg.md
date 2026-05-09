---
surah: 62
test_id: Q062-F-02
title: 4-way tied top-hub set {Q 62, 112, 113, 114} pairwise FR distance test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 4
bonferroni_family: Q062-specialist
alpha_bon: 0.0125
parent_finding: cross-finding-010 audit-035 dedup 4-way tied hub set
---

# Q062-F-02 — Pre-registration: 4-way hub FR-distance pairwise test

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** Q 62's mean Fisher-Rao content-distance to {Q 112, Q 113, Q 114} is SMALLER than Q 62's overall corpus-mean FR distance — i.e. Q 62 is preferentially close to the terminal-triad relative to the corpus baseline.

**H1b (two-tailed observational):** Q 62's mean FR distance to {Q 112, Q 113, Q 114} is **larger than** the within-{Q 112, Q 113, Q 114} pairwise mean — i.e. the 4-way audit-035 hub TIE is *structural-cluster-degree* in the 18-cluster taxonomy and NOT a 4-element FR-content cluster.

**H1c (descriptive):** Q 62's FR-rank-1 nearest surah is from the terminal-mufaṣṣal short-surah cohort (Q 95-114 zone).

**H0 (joint):** Q 62's mean FR distance to {Q 112, Q 113, Q 114} is ≥ Q 62's corpus mean OR ≤ within-triad mean.

**Direction:** Q 62 is FR-pulled toward the terminal triad (LOCKED) but is NOT a co-equal triad member (LOCKED).

## 2. Operational definition

- **FR distance source**: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular` (114×114 upper triangular, 6,441 pairs; SHA-256 verified at run-time).
- **Hub set**: {Q 112 al-Ikhlāṣ, Q 113 al-Falaq, Q 114 al-Nās} — the post-dedup co-degree-4 partners of Q 62 per cross-finding-010 audit-035 amendment.
- **Test statistics**:
  - mean_q62_to_hub = (D(62, 112) + D(62, 113) + D(62, 114)) / 3
  - mean_within_hub = (D(112, 113) + D(112, 114) + D(113, 114)) / 3
  - mean_q62_corpus = average of D(62, s) over s ∈ {1..114}\{62}
  - ratio = mean_q62_to_hub / mean_within_hub

## 3. Test cells

- **Cell A**: H1a (mean_q62_to_hub < mean_q62_corpus). Descriptive-deterministic (no permutation).
- **Cell B**: H1b (mean_q62_to_hub > mean_within_hub). Descriptive-deterministic.
- **Cell C**: H1c (Q 62's FR-rank-1 nearest is in {Q 95-114}). Descriptive-deterministic.
- **Cell D (joint diagnostic)**: ratio interpretation — if ratio > 1.5, cluster-degree-not-FR-content reading is supported.

## 4. Permutation null (deferred)

This pre-reg is descriptive-deterministic (FR matrix is fixed, not stochastic). The relevant permutation null lives in H-NEW-89 / H-NEW-112 parent tests. The audit-035 dedup framework is the binding null-context. No new permutation is run; the test is a structural look-up under a single rule-tuple.

## 5. Success / Failure

- **CONFIRMED-PARTIAL**: Cell A + Cell B + Cell C all hold; ratio > 1.5 supports the "structural-cluster-degree, not FR-content" reading.
- **CONFIRMED-FULL**: All cells hold AND ratio ≤ 1.5 (Q 62 is ALSO FR-content-close to the triad — would be a SURPRISE not predicted by audit-035).
- **PARTIAL**: 2 of 3 cells hold.
- **NULL**: 0 or 1 cells hold; the audit-035 4-way hub tie does not extend to FR-content geometry.

## 6. Honest limits known a priori

- **Single-rule-tuple test**: FR matrix is computed under one specific embedding (root-distribution-with-Hellinger metric per H-NEW-111). Other rule-tuples (char-4-gram per H-NEW-111b; verse-length per H-NEW-111c) are NOT examined here; queue as Q062-F-02.1 / .2 if needed.
- **The 4-way tie is itself rule-tuple-dependent** (per audit-035 dedup). Under the pre-dedup 20-cluster reading, Q 62 was the unique hub at degree 4. The current pre-reg uses the post-dedup framing as the binding spec.
- **N=3 in the hub triad is small**; the FR-content distinctness conclusion is statistical only by ratio inspection, not by formal hypothesis test.
- Because this is a deterministic look-up cell, no α-correction is meaningful at the cell level; family-wise correction rolls into the Q062 specialist Bonferroni-4 outer cap.

## 7. Falsification

If Q 62's mean FR to {112, 113, 114} ≈ within-triad mean (ratio < 1.3), the audit-035 4-way tie would be FR-content-substantiated, not just structural-cluster-degree. This would be a significant finding in the opposite direction of the predicted reading and would strengthen audit-035 beyond its current operational reading.

## 8. Cross-references

- Parent: cross-finding-010 audit-035 dedup amendment (`findings/cross-finding/cross-finding-010-extended-network.md`).
- Pre-decessor: H-NEW-89 META-cluster network (Q 62 as 4-cluster meta-hub).
- Sibling: H-NEW-112 spectral analysis (Q 62 as back-Medinan community spectral peak, v_2 = 0.068 rank 109/114).
- HANDOFF/01-WHAT-WE-KNOW.md "META-CLUSTER NETWORK".

## 9. Replication

- Script: `surahs/Q062-al-jumuah/scripts/Q062_F_all_tests.py` function `q062_f_02`.
- Output: `surahs/Q062-al-jumuah/csv/Q062-F-02.json`.
- FR matrix SHA-256 captured into the JSON at run-time.
