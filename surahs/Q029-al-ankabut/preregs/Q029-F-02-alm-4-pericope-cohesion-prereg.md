---
surah: 29
test_id: Q029-F-02
title: ALM-4 cluster {Q 29, 30, 31, 32} pericope-window root-Jaccard cohesion (first 3 verses)
file_type: pre-registration
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED (single pre-registered test under scale-of-aggregation corollary)
hypothesis_anchor: cross-finding-025 (multi-axis architecture, marker-thickness rule) + scale-of-aggregation corollary formalized in H-NEW-1380 prereg; cross-finding-008 muqaṭṭaʿāt as book-introduction markers; Q030-F-08 PARTIAL verdict at whole-surah scale (Cell A NULL, Cell B length-matched PASS)
direction_of_effect: TIGHTER — the mean pairwise root-Jaccard of the four 3-verse pericopes Q 29:1-3, Q 30:1-3, Q 31:1-3, Q 32:1-3 is greater than the mean of 10,000 length-matched random-pericope draws (one-tailed permutation null)
origin: SESSION-HANDOFF-2026-05-09-PM specialist brief — Q 29 deep-dive T1 (ALM-4 sub-cluster, narrower than Q030-F-08's ALM-6 which mixed Medinan and Late-Meccan members)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  cluster_definition: 4-surahs-opening-with-ALM-among-the-Late-Meccan-ALM-block {Q 29, Q 30, Q 31, Q 32}
  aggregation_scale: PERICOPE (first 3 verses of each surah) — distinguished from whole-surah scale used in Q030-F-08
  pericope_ranges: Q 29:1-3, Q 30:1-3, Q 31:1-3, Q 32:1-3
  detection_rule: pericope = union of QAC v0.4 ROOT-field assignments across verses in the locked range
  root_source: data/morphology/quranic-corpus-morphology-0.4.txt
  null_model: 10,000 length-matched random 4-pericope draws (each of length 3 verses) from the flat verse-index, wraparound disallowed
---

# Q029-F-02 — Pre-registration: ALM-4 pericope-window root-Jaccard cohesion

## 1. Origin

Q030-F-08 tested the full ALM-6 cluster {Q 2, Q 3, Q 29, Q 30, Q 31, Q 32} at WHOLE-SURAH scale on the H-NEW-111 root-distribution instrument. Verdict: PARTIAL — Cell A (uniform null) was NULL (p=0.418) while Cell B (length-matched) was PASS at p=0.0225 — indicating that ALM-6 cohesion is length-confounded at whole-surah scale.

The ALM cluster is internally heterogeneous: Q 2 + Q 3 are Medinan + legal/eschatological; Q 29 + Q 30 + Q 31 + Q 32 are Late-Meccan and form the **chronologically tight 4-surah ALM-sub-cluster** (per al-Suyūṭī chronology and Nöldeke). The hypothesis is that the Late-Meccan ALM-4 sub-cluster, restricted to the surah-opening pericope (first 3 verses), exhibits a tighter cohesion than length-matched controls.

This pre-reg is a direct application of the **scale-of-aggregation corollary** to cross-finding-025 (formalized in H-NEW-1380 prereg, 2026-05-09): a NULL or PARTIAL at whole-surah scale does NOT entail a NULL at pericope scale, and vice-versa. Q038-F-07 / H-NEW-1380 established the same principle for the Iblīs-narrative set (NULL at whole-surah, PASS at pericope).

## 2. Hypothesis

**H1:** The 4 surah-opening pericopes Q 29:1-3, Q 30:1-3, Q 31:1-3, Q 32:1-3 exhibit TIGHTER mean pairwise root-Jaccard similarity than length-matched random-pericope draws.

**H0:** The ALM-4 pericope cluster has mean pairwise root-Jaccard ≤ length-matched random-pericope draws (no cohesion at pericope scale).

**Direction:** mean pairwise root-Jaccard > null mean (LOCKED).

**Test statistic:** mean of all C(4,2) = 6 pairwise root-Jaccard values among the four 3-verse pericopes.

## 3. Cluster definition (locked from corpus surface form)

C = {Q 29 al-ʿAnkabūt, Q 30 al-Rūm, Q 31 Luqmān, Q 32 al-Sajda}.

Verification: each of the 4 surahs opens with the 3-letter token *alif-lām-mīm* at QAC location (s:1:1:1); verses 1-3 of each surah are well-defined under Hafs-Kufan numbering. This is a corpus-EXACT 4-surah sub-cluster: it is the maximal contiguous-position ALM-opening run in the mushaf (Q 29 → Q 30 → Q 31 → Q 32; Q 33 al-Aḥzāb does not open with ALM).

## 4. Pre-registered prediction (direction-locked per cross-finding-025-formal)

Per the scale-of-aggregation corollary, T1 is pre-registered as **PASS-DIRECTED at pericope scale**. The directional prior is grounded in:

1. The Late-Meccan ALM cluster shares the muqaṭṭāʿāt opener (1 lemma overlap by definition: ALM).
2. The Q 29:1, Q 30:1, Q 31:1, Q 32:1 opening verses share the consonantal triplet a-l-m as 3 separate letter-words.
3. Q 30:1-2, Q 31:1-2, Q 32:1-2 share book-reference morphology (*tilka āyātu / dhālika*) — present in 3 of 4 (Q 29 is the cross-finding-008 exception).
4. The 4-surah block is contiguous in mushaf position (28→29→30→31→32 → 33 = the only ALM-quartet streak).

This is the multi-axis correlation required by cross-finding-025 (marker × content × chronology × mushaf-adjacency). Per the scale-of-aggregation law, this is exactly the configuration where pericope-scale PASS is most likely when whole-surah PARTIAL has already been observed.

## 5. Operational definition

- **Pericope** = union of all QAC v0.4 ROOT-field assignments across the locked 3-verse range. For Q 29:1-3 this is {muqaṭṭāʿāt-marker-roots-if-any (typically none) + roots of v2 imtihān content + roots of v3 fatannā content}.
- **Root extraction**: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` v0.4; ROOT field of each morphological segment; a verse's roots = union of its segments' ROOT fields.
- **Pairwise Jaccard**: J(i,j) = |R_i ∩ R_j| / |R_i ∪ R_j|. If both sets empty, J = 0.
- **Mean pairwise Jaccard**: mean over all 6 unordered pairs.

## 6. Permutation null protocol

1. Seed RNG = 20260509 (matches H-NEW-1380 / Q038-F-07 convention for the scale-of-aggregation series).
2. For each of 10,000 permutations:
   - Draw 4 starts uniformly from the flat 6,236-verse index (with constraint that each start + 2 ≤ 6,236 to keep window in-bounds; wraparound disallowed).
   - For each start, take the 3 consecutive verses as a pericope; compute its root-set via QAC.
   - Compute mean pairwise root-Jaccard across the 4 sampled pericope root-sets.
3. p_perm = (count of perm-J ≥ observed-J) / 10,000 (strict one-tailed; same convention as Q038-F-07 / H-NEW-1380).
4. The 4 observed pericopes themselves are excluded from the null draw pool (no overlap with the locked starts s∈{first verse of each of Q 29, Q 30, Q 31, Q 32}).

## 7. Bonferroni

k = 1 (single primary test). α = 0.05.

## 8. Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| p_perm ≤ 0.05 AND J_mean > null mean | **PASS-DIRECTED** |
| p_perm ≤ 0.5 AND J_mean > null mean | **DIRECTIONAL** |
| J_mean ≤ null mean (within 0.5 std) | **NULL** |
| J_mean strictly < null mean − 0.5 std | **PRE-COMMIT-VIOLATION** → published as NULL with prominence |

## 9. MW-1..MW-7 compliance

- **MW-1** (instrument-prior): root-Jaccard + 6-pair mean + length-matched perm null locked above.
- **MW-2** (corpus-prior): 10,000 perms; minimum standard met.
- **MW-3** (alternative-models): NOT triggered — single primary test. If NULL, follow-up TF-IDF root-cosine variant is queued (not part of this pre-reg).
- **MW-4** (over-fitting): no fitted parameter.
- **MW-5** (replication): Q030-F-08 PARTIAL at whole-surah scale is the cross-scale prior; this test is the pericope-scale companion. Substantive replication under alternate seed queued post hoc.
- **MW-6** (instrument-control): pericope-scale null is itself controlled by length-matched random-pericope draws across the corpus (cross-corpus PC not applicable inside the Quran).
- **MW-7** (post-hoc cap): single pre-registered direction; not post-hoc.

## 10. Scale-of-aggregation discipline

Per H-NEW-1380 corollary to cross-finding-025: scale-of-aggregation is a first-class methodological axis. This pre-reg's scale (pericope = first 3 verses) is LOCKED BEFORE OBSERVATION. The discrepancy (if any) between this test's pericope-scale verdict and Q030-F-08's whole-surah verdict is itself a first-class finding, not a contradiction.

## 11. Honest a-priori limits

- Pericope size = 3 verses is short; root-sets per pericope are small (10-20 unique roots each), increasing Jaccard variance.
- Muqaṭṭāʿāt openers themselves carry no QAC ROOT (the letters are tagged as muqaṭṭāʿāt particles without root-features). The cohesion signal must come from v 2-3 content, not from the ALM lemma itself.
- Q 29:1-3 vs Q 30:1-3 vs Q 31:1-3 vs Q 32:1-3 may share book-reference morphology (*tilka āyātu*, *dhālika*, etc.). This is part of the expected signal, not a confound — it is the cross-finding-008 morphological-marker pattern.

## 12. SHA256 lock

Computed at run-time. Embedded in `scripts/Q029_F_02_alm_4_pericope_cohesion.py` as `EXPECTED_SHA`. Run-script verifies before computation; mismatch = fail-fast.

## 13. Anti-flip

Reverse direction (J_mean < null mean − 0.5 std) is NOT a reportable PASS. Publish as NULL with reverse-direction note. The pre-registered direction is one-way.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
