---
id: H-NEW-1340
title: al-ḥamdu li-llāh opener 5-surah cluster Fisher-Rao cohesion
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: H-NEW-1340-hamdu-lillah-cluster
alpha_bon: 0.025
direction_of_effect: The 5 surahs opening with *al-ḥamdu li-llāh* {Q 1, 6, 18, 34, 35} have a mean intra-cluster Fisher-Rao distance lower than 95% of length-matched random 5-surah samples
origin: handoff/05-OPEN-QUESTIONS OQ-3 candidate (book-introduction marker network completeness — al-ḥamdu li-llāh opener cluster as second-class introduction-marker candidate alongside muqaṭṭāʿat)
verdict_ceiling: PASS-DIRECTED (single planned pre-registered test; INDEPENDENT REPLICATION required for promotion)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  cluster_definition: 5-surahs-with-opening-formula-al-hamdu-lillah
  null_model: random-5-surah-samples-from-114-uniform-and-length-matched
---

# H-NEW-1340 pre-registration

## Origin

OQ-3 (HANDOFF/05-OPEN-QUESTIONS) raises: "Are there other introduction-marker classes besides muqaṭṭāʿat? *al-ḥamdu li-llāh* openers (Q 1, 6, 18, 34, 35) are a candidate." This pre-reg locks the structural-cohesion test on that specific 5-surah cluster.

## Hypothesis

The 5 surahs opening *al-ḥamdu li-llāh* {Q 1 al-Fātiḥa, Q 6 al-Anʿām, Q 18 al-Kahf, Q 34 Sabaʾ, Q 35 Fāṭir} form a Fisher-Rao cohesive cluster on the H-NEW-111 root-distribution instrument.

## Cluster verification (locked)

Verified manually:
- Q 1:1 — *bi-smi llāhi al-raḥmāni al-raḥīm* / Q 1:2 — *al-ḥamdu li-llāhi rabbi al-ʿālamīn*
- Q 6:1 — *al-ḥamdu li-llāhi alladhī khalaqa al-samāwāti wa-l-arḍa wa-jaʿala al-ẓulumāti wa-l-nūr*
- Q 18:1 — *al-ḥamdu li-llāhi alladhī anzala ʿalā ʿabdihi al-kitāba wa-lam yajʿal lahu ʿiwajā*
- Q 34:1 — *al-ḥamdu li-llāhi alladhī lahu mā fī al-samāwāti wa-mā fī al-arḍi wa-lahu al-ḥamdu fī al-ākhirati*
- Q 35:1 — *al-ḥamdu li-llāhi fāṭiri al-samāwāti wa-l-arḍi jāʿili al-malāʾikati rusulan*

Note: Q 1's opening *al-ḥamdu li-llāh* is at v 2 (after the basmala v 1). All others have it at v 1 directly (since their basmalas are not counted as separate verses). Following the cross-finding-008 muqaṭṭāʿat tradition (basmala-counted-only-in-Q1), the comparable position is "the first content-bearing verse" — Q 1:2 in Q 1, Q N:1 in others.

## Test design

### Cell A (uniform null)

Compute mean pairwise FR among {1, 6, 18, 34, 35} = 10 pairs. Permutation null: 10000 random 5-of-114 samples from full corpus (including Q 1 since cluster contains Q 1).

**Direction-locked**: intra-cluster mean ≤ permutation null 5th percentile.

PASS if p_perm ≤ 0.025; NULL otherwise.

### Cell B (length-matched control)

Same test restricting null to 5-surah samples whose total verse-count is within ±20% of observed (Q 1=7; Q 6=165; Q 18=110; Q 34=54; Q 35=45 → total ≈ 381 verses).

PASS if p_perm ≤ 0.025; NULL otherwise.

### Bonferroni

k = 2 (Cell A + Cell B). α_bon = 0.025 per cell.

### MW-5 positive control

Use H-NEW-1190 *wa-mā adrāka mā* sub-sample (5-of-10 deterministic via seed=20260509). H-NEW-1190 confirmed FR-cohesive at p=0.00068. PC must pass at p ≤ 0.05.

### Acceptance windows

| Cell A | Cell B | PC | Verdict |
|:-:|:-:|:-:|:--|
| ✓ | ✓ | ✓ | PASS-DIRECTED |
| ✓ | ✗ | ✓ | DESCRIPTIVE-ONLY (length-confound) |
| ✗ | ✓ | ✓ | PARTIAL |
| ✗ | ✗ | ✓ | NULL |
| any | any | ✗ | NULL-BROKEN |

### Garden-of-forking-paths

Origin disclosed: handoff/05-OPEN-QUESTIONS OQ-3 candidate. No FR-matrix value loaded for the cluster yet. Direction locked. The 5-surah list is the canonical *al-ḥamdu li-llāh* opener list (a fact about the corpus, not a post-hoc selection). No alternative cells.

### A-priori expectation

The 5 surahs span a wide spectrum: Q 1 (very short Meccan), Q 6 (very long Meccan), Q 18 (long Meccan), Q 34 (mid Meccan), Q 35 (mid Meccan). All Meccan; chronology spans Early to Late. The *al-ḥamdu li-llāh* opener is a thinner marker than muqaṭṭāʿat (single phrase vs whole-verse + 13+ correlated axes). **Prediction per cross-finding-025**: this should follow the marker-thickness rule — if the 5 surahs share content beyond the opener (e.g., creation-cosmology, scripture-self-reference), they should cohere; if not, NULL.

The *al-ḥamdu li-llāh* opener pairs with content in 3 of 5 cases:
- Q 6: *al-ḥamdu li-llāhi alladhī khalaqa al-samāwāti...* — creation-cosmology
- Q 18: *al-ḥamdu li-llāhi alladhī anzala ʿalā ʿabdihi al-kitāba...* — scripture-self-reference (Pattern-B Late-Meccan)
- Q 34: *al-ḥamdu li-llāhi alladhī lahu mā fī al-samāwāti...* — possession-cosmology
- Q 35: *al-ḥamdu li-llāhi fāṭiri al-samāwāti...* — origination-cosmology

So 4 of 5 (excluding Q 1 which is liturgical-frame) carry creation-cosmology framing. **If shared creation-cosmology drives root-distribution, expect PASS; if not, NULL.**

### Anti-flip

Reverse direction (cluster mean ≥ 95th percentile) is NOT a reportable PASS. Publish as NULL with reverse-direction note.

## Connection to existing findings

- **OQ-3 (open question)**: this directly tests the "second introduction-marker class" candidate. PASS would extend cross-finding-008 to a 2nd marker class; NULL would suggest the muqaṭṭāʿat is unique in its marker-architecture role.
- **Cross-finding-025**: tests the marker-thickness rule on a fresh cluster. The *al-ḥamdu li-llāh* opener is a 3-word phrase + 1-verse co-locator — thicker than sajda-trigger (single verse mid-surah) but thinner than muqaṭṭāʿat (whole-verse + 13 correlated axes).
- **Cross-finding-012 Late-Meccan apparatus**: 4 of 5 cluster members are Late Meccan; Q 1 is sui-generis. Cluster sits on the Late-Meccan side of cross-finding-012's Pattern-B distribution.
- **Inline-q1-nearest-neighbors finding (handoff)**: Q 1 al-Fātiḥa is content-NN of Q 108 (FR=0.338). If Q 1 is in {Q 1, 6, 18, 34, 35} cluster, the cluster might pull on Q 1 toward longer surahs. Test whether Q 1 is the cluster outlier.

## Pre-commit attestation

Locked by SHA256. Run script verifies before loading FR matrix.
