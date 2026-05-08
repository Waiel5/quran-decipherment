---
finding_id: Q028-F-02
title: TSM-cluster Moses-content twin-pair similarity (Q 26 ↔ Q 28 vs Q 20 controls)
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q028-novel-findings
alpha_bon: 0.01
direction: ONE-SIDED-UPPER
status: PRE-REGISTERED
specialist: Q028-al-qasas-specialist
verdict: TBD
---

# Q028-F-02 — TSM-cluster Moses-content twin-pair similarity pre-reg

## 1. Hypothesis

Q 26 al-Shuʿarāʾ (opens ṬSM) contains an extended Moses-Pharaoh narrative at vv. 10-67. Q 28 al-Qaṣaṣ (opens ṬSM) contains the Moses-Madyan-Pharaoh-exodus narrative at vv. 3-43. Q 20 Ṭā-Hā (opens ṬH) contains the largest Moses narrative in the corpus, vv. 9-98.

If the muqaṭṭaʿāt-letter-set is a content-axis correlate (the al-Biqāʿī / al-Suyūṭī classical claim that letter-clusters share content), Q 26's and Q 28's Moses narratives should be more similar to each other than either is to Q 20's Moses narrative — because Q 26 + Q 28 share the ṬSM letter-set while Q 20 carries the unrelated ṬH set.

**Note**: prior project work has falsified Biqāʿī's full muqaṭṭaʿāt-letter-cluster content-cohesion claim 4× ([[h-new-720-canonical-adjacency-cost]] / Wave-FALSIFIED §3.7). This pre-reg therefore expects the prediction to **FAIL** under the default rules-tuple — but adversarial-flag-friendly: a NULL outcome here will further consolidate the existing falsification record under the specific TSM Moses-narrative configuration. **The pre-committed direction is the al-Biqāʿī CLAIM (Q26-Q28 closer than to Q20)**; we test whether the existing falsification generalises here. Either result is publishable.

## 2. Pre-committed primary contrast (locked direction)

Let `M_s` = the QAC stem-root TF distribution over the surah-`s` Moses-narrative block:
- `M_26` = Q 26:10-67 (58 verses)
- `M_28` = Q 28:3-43 (41 verses)
- `M_20` = Q 20:9-98 (90 verses)

Define cosine similarity on the TF-vectors over the **shared root vocabulary** of the three blocks (union of all roots that appear in any of the three blocks).

**H1 (locked, one-sided upper-tail)**:
`cos(M_26, M_28) > max(cos(M_26, M_20), cos(M_28, M_20))`

**H2 (locked)**: difference `cos(M_26, M_28) − mean(cos(M_26, M_20), cos(M_28, M_20)) ≥ 0` AND p_perm < α_Bonferroni.

## 3. Direction-locking

H1 direction = TSM-pair > TSM-vs-ṬH-pair. Reverse = pre-commit violation, published as NULL with full prominence (consistent with Wave-FALSIFIED §3.7).

## 4. Method

- Source for content: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (orthographic surface tokens) — primary.
- Optional cross-validation: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` for QAC stem-root TF if available; otherwise use orthographic-surface-form-collapsed (strip Arabic prefixes و ف ل ب ال).
- Cosine similarity on TF-vectors over union vocabulary.
- Permutation null: shuffle the role-labels of the three blocks 10 000 times AND test whether the observed contrast is upper-tail (i.e., is `cos(M_26, M_28) − mean(cos(M_26, M_20), cos(M_28, M_20))` greater than 95 % of the random-relabelling distribution?).
- Secondary null: random-3-block-with-same-verse-counts from the corpus; how often does a TSM-style triple show up by chance?

## 5. Test family + Bonferroni

Family: Q028-novel-findings, k = 5. α_Bonferroni = 0.01.

## 6. Acceptance / failure

- **PASS** (vindicates al-Biqāʿī claim under TSM Moses-pair): H1 + H2 both hold AND p_perm < 0.01.
- **NULL** (consolidates Wave-FALSIFIED §3.7): H1 reverses or H2's p_perm ≥ 0.05.
- **DIRECTIONAL**: 0.01 ≤ p < 0.05.

## 7. MW protections

- MW-1: block lengths reported, length-residualised cosines as secondary.
- MW-2: 10 000-permutation null.
- MW-3: TF vs TF-IDF, orthographic-surface vs root-collapsed (sensitivity).
- MW-5: positive-control on a known-content-cohesive pair (Q 12 Yūsuf-block-A vs Q 12 Yūsuf-block-B should be high; trivially passes).
- MW-6: instrument-control = compare to randomly-paired blocks.
- MW-7: not invoked.

## 8. Honest expectation

The project's prior consolidated finding is that muqaṭṭaʿāt letter-cluster ≠ content-cluster (4 prior NULLs). This test pre-registers the al-Biqāʿī direction NOT to advocate for it, but to:
1. provide an explicit specific TSM-Moses-pair test that prior work didn't cover specifically;
2. publish the result with equal NULL prominence regardless of direction.

If H1 reverses (i.e., Q 20 is closer to Q 26 or Q 28 than they are to each other) we report this as further consolidation of the muqaṭṭaʿāt ⊥ content axis.

## 9. Pre-reg SHA

To be SHA-256-hashed at file-lock time and embedded in the runner script.
