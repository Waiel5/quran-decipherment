---
surah: 30
test_id: Q030-F-08
title: ALM-cluster 6-surah Fisher-Rao cohesion (sub-set of muqaṭṭāʿat, narrower than HM 7-cluster)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
alpha_bon: 0.025
verdict_ceiling: PASS-DIRECTED (single planned pre-registered test; independent replication required for promotion)
hypothesis_anchor: cross-finding-008 muqaṭṭāʿat are book-introduction markers; H-NEW-1395 HM-7 NULL refines this to "ALM sub-cluster may still cohere" since HM was the failed wider muqaṭṭāʿat sub-cluster
direction_of_effect: The 6 surahs opening with ALM {Q 2, 3, 29, 30, 31, 32} have a mean intra-cluster Fisher-Rao distance lower than 95% of length-matched random 6-surah samples
origin: SESSION-HANDOFF-2026-05-09-PM session task — Q 30 deep-dive T3 (the ALM-cluster cohesion test, complementary to H-NEW-1395 HM NULL)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  cluster_definition: 6-surahs-opening-with-ALM-muqattaat {Q 2, Q 3, Q 29, Q 30, Q 31, Q 32}
  null_model: random-6-surah-samples-uniform-and-length-matched
---

# Q030-F-08 — Pre-registration: ALM 6-surah cluster Fisher-Rao cohesion

## 1. Origin

The classical muqaṭṭaʿāt cluster is a 29-surah set sharing the disconnected-letter opener. Cross-finding-008 establishes muqaṭṭaʿāt as book-introduction markers across multiple structural axes. H-NEW-1395 NULLed the 7-surah HM/ḥawāmīm sub-cluster on FR-roots cohesion (CONFIRMED-NULL via valid PC).

This pre-reg targets the 6-surah ALM sub-cluster {Q 2, Q 3, Q 29, Q 30, Q 31, Q 32} — the LARGEST single-letter-string sub-cluster of muqaṭṭaʿāt. ALM is the most-attested muqaṭṭaʿāt opener and is split across both Medinan (Q 2, Q 3) and Late-Meccan (Q 29-32) periods.

The hypothesis is: ALM, as a NARROWER and more LETTER-STRING-IDENTICAL sub-cluster than HM, MAY cohere on FR-roots even though HM did not. The competing hypothesis is: muqaṭṭaʿāt cohesion is a muqaṭṭaʿāt-axis-only phenomenon (cross-finding-025 marker-thickness rule), independent of the specific letter-string, and ALM will likewise NULL.

## 2. Hypothesis

**H1:** The 6 surahs opening *الم* {Q 2, Q 3, Q 29, Q 30, Q 31, Q 32} form a Fisher-Rao cohesive cluster on the H-NEW-111 root-distribution instrument.

**H0:** The ALM cluster is NOT FR-cohesive (its mean intra-cluster distance is no lower than a random length-matched 6-surah sample).

**Direction:** intra-cluster mean ≤ permutation null 5th percentile (LOCKED).

## 3. Cluster definition (locked from corpus surface form)

C = {Q 2 al-Baqara, Q 3 Āl ʿImrān, Q 29 al-ʿAnkabūt, Q 30 al-Rūm, Q 31 Luqmān, Q 32 al-Sajda}.

All 6 verified by hand against `data/morphology/quranic-corpus-morphology-0.4.txt`:
- Q 2:1, Q 3:1, Q 29:1, Q 30:1, Q 31:1, Q 32:1 — each is the 3-letter token *alif-lām-mīm* with QAC location-tuples `(s:1:1:1)`.

This is a corpus-EXACT 6-surah cluster (no other surah opens with ALM-only; Q 13 opens with ALMR — DISTINCT 4-letter string; Q 7 opens with ALMS — DISTINCT 4-letter string; both excluded from this pre-reg).

## 4. Test design

### Cell A (uniform null)

Compute mean pairwise FR among the 6 cluster surahs (C(6,2) = 15 pairs). Permutation null: 10,000 random 6-of-113 samples from corpus excluding Q 1 (matching H-NEW-111 canonical null treatment).

**Direction-locked**: intra-cluster mean ≤ permutation null 5th percentile.

PASS if p_perm ≤ 0.025 (Bonferroni-2); NULL otherwise.

### Cell B (length-matched control)

Same test restricting null to 6-surah samples with total verse-count within ±20% of observed (Q 2=286, Q 3=200, Q 29=69, Q 30=60, Q 31=34, Q 32=30 → total = 679 verses).

PASS if p_perm ≤ 0.025; NULL otherwise.

### Bonferroni

k = 2 (Cell A + Cell B). α_bon = 0.025 per cell.

### MW-5 positive control

Use H-NEW-1190 *wa-mā adrāka mā* 6-of-10 sub-sample (deterministic with seed = 20260509). H-NEW-1190 confirmed FR-cohesive at p = 0.00068; sub-sample retains FR-cohesion in prior tests (H-NEW-1340 PC passed at p = 0.021). PC must pass at p ≤ 0.05.

### Acceptance windows

| Cell A | Cell B | PC | Verdict |
|:-:|:-:|:-:|:--|
| ✓ | ✓ | ✓ | PASS-DIRECTED |
| ✓ | ✗ | ✓ | DESCRIPTIVE-ONLY (length-confound) |
| ✗ | ✓ | ✓ | PARTIAL |
| ✗ | ✗ | ✓ | NULL (PC valid) |
| any | any | ✗ | NULL-BROKEN |

### Garden-of-forking-paths

- Origin disclosed: SESSION-HANDOFF-2026-05-09-PM specialist brief (this task).
- No FR-matrix value loaded for the ALM cluster yet (pre-commit).
- Direction locked (cluster ≤ 5th percentile null).
- Cluster identity is corpus-EXACT (the 6 ALM-openers are a definitional fact about the surface form, not a post-hoc selection).
- No alternative cells beyond A and B.
- No rules-tuple variants.

### A-priori expectation

ALM is the LONGEST-DURATION single-string muqaṭṭaʿāt opener (Medinan + Late Meccan span). Per cross-finding-025 marker-thickness rule, a thin opener (3 letters of v 1) without strong content-correlated features would NULL on FR-roots.

**Counter-prediction**: ALM may cohere if the 6 surahs share a specific content-tendency beyond the opener. Empirical inputs:
- Q 2 + Q 3: Medinan, long, legal-eschatological-narrative mix. Book-reference present.
- Q 29 + Q 30: Late Meccan, medium, narrative-prophecy mix. NO book-reference (the exception pair).
- Q 31 + Q 32: Late Meccan, short, wisdom + sajda-marker mix. Book-reference present.

The 6 surahs span 3 distinct content-clusters. **A-priori prediction is mixed-NULL-leaning**: the surface ALM string is letter-string-identical but content-period-spread, and the cross-finding-025 rule predicts NULL absent multi-axis correlation.

Q030-F-04 already measured d(Q29, Q30) = 0.9153 within an ALM sub-set and found Q 29-Q 30 was rank 7/15 (NOT a tight pair). The 6-cluster mean is expected to be MODEST.

### Anti-flip

Reverse direction (cluster mean ≥ 95th percentile = anti-cohesion) is NOT a reportable PASS. Publish as NULL with reverse-direction note.

## 5. Rules-tuple

Matches H-NEW-111 canonical settings (orthographic-token, no-tashkeel, QAC root distribution, basmala-counted-only-in-Q1, hafs-kufan).

## 6. SHA256 lock

Computed at run-time. Embedded in `scripts/Q030_F_08_alm_cluster_fr_cohesion.py`. Verified by `verify_sha()` before computation.

## 7. Connection to existing findings

- **Cross-finding-008** (muqaṭṭāʿat as book-introduction markers): the ALM cluster is the largest single-string sub-set. If PASS, the marker-network extends to root-distribution; if NULL, the marker is letter-axis-only.
- **H-NEW-1395 HM-7 NULL** (CONFIRMED): the parallel 7-surah HM sub-cluster did NOT cohere on FR-roots, replicating the marker-thickness rule. The present ALM test asks: does the SAME marker-axis-only pattern hold for ALM, OR does ALM (being more letter-string-identical and including Medinan members) deviate?
- **Q030-F-04** (intra-ALM 15-pair within-cluster ranking): Q 29-Q 30 was rank 7/15 = JUST below median; not a tight pair. The full-cluster mean test is broader and may detect cohesion that pairwise tests missed (if the pattern is across the cluster, not concentrated in one pair).
- **Cross-finding-025 marker-thickness rule**: ALM is a 1-verse 3-letter marker — the thinnest muqaṭṭaʿāt opener. Per the rule, NULL is expected; PASS would CHALLENGE the rule.
- **H-NEW-1340 al-ḥamdu li-llāh NULL**: a separate 5-surah opener cluster also NULLed. Adds prior weight to the NULL prediction.

## 8. Pre-commit attestation

Locked by SHA256 hash. Run script verifies before loading FR matrix.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
