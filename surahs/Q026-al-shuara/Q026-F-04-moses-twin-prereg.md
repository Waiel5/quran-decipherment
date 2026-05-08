---
finding_id: Q026-F-04
title: Pharaoh-Moses structural twin — Q 26 vs Q 28 (both ṬSM) vs Q 20 (ṬH)
date_preregistered: 2026-05-07
phase: B+
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q026-F-01..F-05
alpha_bon: 0.01
acceptance_window: see §6
---

# Q026-F-04 — Moses-Pharaoh sequence structural twin

## 1. Hypothesis (locked before observation)

**H1**: The Moses-Pharaoh narratives in Q 26 (vv 10-67) and Q 28 (vv 3-43) — both opened by the muqaṭṭaʿ ṬSM — are MORE similar to each other on root-cosine distance than EITHER is to the Moses narrative in Q 20 (vv 9-79; opened by ṬH). I.e., the muqaṭṭaʿ-letter-set predicts narrative-similarity within shared content.

**H0**: The three Moses-narratives are equidistant; muqaṭṭaʿ-cluster does not predict narrative similarity.

## 2. Operational definition

- M26 = Q 26 verses 10-67 (Moses-Pharaoh narrative, including refrain).
- M20 = Q 20 verses 9-79 (Moses narrative).
- M28 = Q 28 verses 3-43 (Moses-Pharaoh narrative).
- Per-block TF vector over QAC stem-roots (length-normalized).
- Distances: `d(M26, M28)`, `d(M26, M20)`, `d(M28, M20)` — root-cosine distances (1 − cos).

## 3. Test statistic

- `D_TSM = d(M26, M28)` (the predicted-closer pair).
- `D_HEAD_26 = d(M26, M20)`, `D_HEAD_28 = d(M28, M20)`.
- Test: `D_TSM < min(D_HEAD_26, D_HEAD_28)` → "TSM-pair is closer".
- Symmetry-margin: `Margin = min(D_HEAD_26, D_HEAD_28) − D_TSM` (positive = TSM-prediction direction).

## 4. Direction (LOCKED)

- Margin > 0 (TSM-pair closer than either is to Q 20).
- One-sided upper-tail; α_bon = 0.01.

## 5. Permutation null

Seed 20260507. Permutation null: relabel the verse-blocks among (M26, M28, M20) randomly via 10000 random partitions of the union-vocabulary, preserving each block's total root-token count. Compute the analog Margin under the null. p_perm = (1 + #(margin_perm ≥ margin_obs)) / (1 + 10000).

## 6. Acceptance

- **CONFIRMED** = Margin > 0 AND p_perm < 0.01.
- **DIRECTIONAL** = Margin > 0 AND p_perm in [0.01, 0.05].
- **NULL** = Margin ≤ 0 OR p_perm ≥ 0.05.
- **PRE-COMMIT VIOLATION** = Margin strongly negative (M20 closer to one of M26/M28 than M26 is to M28); flag publishing as NULL.

## 7. Rules-tuple

`(no-tashkeel, QAC-stem-roots, length-normalized-TF, Hafs-Kufan, Mashriqi)`.

## 8. Anti-hallucination

QAC roots: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`. Verse-text: `quran-text/quran-no-tashkeel.json`.

## 9. Honest a-priori limits

- This test is structurally hard: muqaṭṭaʿāt content-*munāsaba* has been NULL 4 times in prior project work (full-29, ḥawāmīm-7, ALM-6, ALR-5 letter families). H1 is therefore a genuine prior-defying claim.
- The H-NEW-111 FR-distance row already shows: `d(Q26, Q28) = 0.954`, `d(Q26, Q20) = 0.956`, `d(Q28, Q20) = 0.895`. Q 28 is *closer* to Q 20 than to Q 26 by FR-roots. So at the whole-surah level, the TSM-twin hypothesis is FALSIFIED. The narrative-block test is whether the Moses-content slice changes that picture.
- A NULL or pre-commit violation here will be **reported with full prominence** as fifth confirmation of muqaṭṭaʿ-content-orthogonality.
- Block boundaries are taken from classical commentaries (al-Rāzī, Ibn Kathīr verse-by-verse) and are themselves a rules-tuple choice; widening or narrowing by ±5 verses is documented as a sensitivity check.
