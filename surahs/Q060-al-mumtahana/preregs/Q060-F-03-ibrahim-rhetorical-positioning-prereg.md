---
surah: 60
test_id: Q060-F-03
title: Q 60:4-6 vs Q 14:35-41 vs Q 21:51-72 — Ibrahim-as-model lexical orthogonality
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q060-F-03-ibrahim-rhetoric
alpha_bon: 0.0167
---

# Q060-F-03 — Pre-registration: Ibrahim presentations are lexically orthogonal across Q 60 / Q 14 / Q 21

## 1. Hypothesis (locked before observation)

**H1 (multi-cell):** The Ibrahim-pericope of Q 60 (vv 3-9, "uswa hasana" Medinan-disownment), Q 14 (vv 34-40, "ājalu mā lakum li-l-aṣnām" Late-Meccan-monotheist-prayer), and Q 21 (vv 50-74, "kasarahā jadhādhā" Late-Meccan-idol-smasher-narrative) deploy **three distinct, mostly-disjoint lexical fingerprints**, each exclusive to its surah's Ibrahim-presentation type.

**Operationalization** — three pre-committed lemma-sets (closed list, locked at this pre-reg's commit-time):

- **Set A (Q 60 disownment-alliance lexicon)**: {أسوة, برآء, بريء, العداوة, البغضاء, مودة, أولياء, تتخذوا, كفرنا, تتولوا}
- **Set B (Q 14 monotheist-prayer lexicon)**: {البلد, آمنا, الأصنام, يقيم الصلاة, الجبلة, مهاجر, الدعاء, اجعل}
- **Set C (Q 21 idol-smasher narrative lexicon)**: {كسر, جذاذا, فتى, بردا, سلاما, كيدا, إفك, آلهة}

**H1a:** Set A occurs preferentially in Q 60's Ibrahim-pericope vs Q 14's and Q 21's pericopes (count A_Q60 > max(A_Q14, A_Q21)).

**H1b:** Set B occurs preferentially in Q 14's pericope vs Q 60's and Q 21's (count B_Q14 > max(B_Q60, B_Q21)).

**H1c:** Set C occurs preferentially in Q 21's pericope vs Q 60's and Q 14's (count C_Q21 > max(C_Q60, C_Q14)).

**H0 (joint):** at least one of the cells fails the dominance condition.

**Direction:** A→Q60, B→Q14, C→Q21 (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json`.
- **Pericope definition**:
  - Q 60 Ibrahim-pericope: vv 3-9 (anchored on Ibrahim mention at v 4).
  - Q 14 Ibrahim-pericope: vv 34-40 (anchored on v 35).
  - Q 21 Ibrahim-pericope: vv 50-74 (anchored on vv 51, 60, 62, 69).
- **Counting rule**: per-substring exact-match count of each lemma in each pericope. Lemma list is closed and pre-committed in §1 above.

## 3. Test statistic

For each Set X ∈ {A, B, C} and each pericope P ∈ {Q60, Q14, Q21}, count(X, P).

For each cell (X target = its predicted dominant pericope), check the predicted-dominance condition.

## 4. Permutation null (alternative-corpus)

For each set, randomly permute the lemma assignment across the 3 pericopes (i.e., shuffle which set is "A" vs "B" vs "C"). Under random labeling, what's the probability that all 3 cells happen to dominate their predicted pericope?

There are 6 = 3! ways to assign 3 sets to 3 pericopes. Under uniform null, only 1 assignment produces full predicted-dominance, so p_max-permutation = 1/6 = 0.167 — UNDERPOWERED for joint-significance under set-permutation alone.

So the FORMAL primary test is observation of joint-dominance directly, with single-test α=0.05 cap and Bonferroni-3 (k=3, α_bon=0.0167) for the per-cell sub-tests.

## 5. Decision rule

- **CONFIRMED**: All 3 cells satisfy predicted-dominance (each Set X has count(X, target P_X) > max counts in other 2 pericopes); each predicted set/pericope cell achieves a strictly-positive count of ≥1 dominance-margin tokens.
- **PARTIAL**: 2 of 3 cells satisfy.
- **NULL**: ≤1 cell satisfies.

This is a descriptive-rhetorical hypothesis; the discrete-count nature limits it to PASS-DIRECTED status pending replication on a distinct lexical dimension.

## 6. Pre-commit violation handling

If any of the lemma sets shows zero presence in its target pericope, the case is filed as a PRE-COMMIT-VIOLATION-DESCRIPTIVE.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, substring-exact, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 3 cells; α_bon = 0.0167 per cell. Joint cell-pass = all 3 dominate.

## 9. Honest limits known a priori

- Lemma-list construction is the most fragile step; lists are LOCKED before run, but choice of words is curatorial. This is INHERENT to balāgha-style lexical-orthogonality tests; the result is ROBUST against the specific list only insofar as the list is canonical (each Set is built from al-Rāzī's *Mafātīḥ al-ghayb* and al-Zamakhsharī's *Kashshāf* commentary on the respective surah, NOT from inspecting the corpus).
- The test is descriptive-rhetorical (PASS-DIRECTED ceiling), NOT statistical-confirmation (CONFIRMED would require independent operationalization).
- If H1a-c all pass, the verdict is "Q 60 / Q 14 / Q 21 are LEXICALLY-ORTHOGONAL Ibrahim-presentations" — three rhetorical modes within the corpus, not redundant.

## 10. Coordination

This test does not duplicate any other Q 60 / Q 14 / Q 21 specialist test.

## 11. SHA256 lock

Computed at completion-time.
