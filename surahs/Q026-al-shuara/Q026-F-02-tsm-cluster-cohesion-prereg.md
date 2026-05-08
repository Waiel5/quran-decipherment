---
finding_id: Q026-F-02
title: TSM-cluster (Q 26, 27, 28) joint cohesion vs random-3-tuples
date_preregistered: 2026-05-07
phase: B+
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q026-F-01..F-05
alpha_bon: 0.01
secondary_bonferroni_k: 4
secondary_alpha: 0.0125
acceptance_window: see §6
---

# Q026-F-02 — TSM-cluster cohesion (Q 26 ṬSM, Q 27 ṬS, Q 28 ṬSM)

## 1. Hypothesis (locked before observation)

**H1**: The triplet (Q 26, Q 27, Q 28) — sharing the ṭ-s-(m) muqaṭṭaʿ letter set — is *jointly more cohesive* on multi-axis features than random 3-tuples drawn from muqaṭṭaʿ-opened surahs.

**H0**: TSM-triplet cohesion is no better than random 3-tuples among the 29 muqaṭṭaʿ-opened surahs.

## 2. Multi-axis cohesion

Four axes (k=4, α_bon = 0.0125 per axis within this finding):
- A1 = pairwise Fisher-Rao distance, mean over 3 pairs (lower = more cohesive). Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json`.
- A2 = absolute spread of `top_final_letter_frac` (rhyme-letter dominance) across the 3 surahs (lower = more cohesive). Source: `h-new-750.json`.
- A3 = absolute spread of `sig_A` (iʿjāz-signature). Source: `h-new-750.json`.
- A4 = absolute spread of UAS. Source: `h-new-840.json`.

For each axis, lower value = more cohesive.

## 3. Comparison set

- The 29 muqaṭṭaʿ-opened surahs: Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68.
- Sample C(29,3) = 3654 random 3-tuples (or all 3654 — exact enumeration is feasible).
- For each tuple, compute the 4-axis values; compute rank percentile of the TSM triplet on each axis (lower percentile = more cohesive).

## 4. Test statistic

For each axis A_i (i=1..4), compute `pct_TSM_i` = the percentile rank of the TSM-triplet cohesion among all 3654 muqaṭṭaʿ-3-tuples (lower = more cohesive).

## 5. Direction (LOCKED)

- A1 (FR mean pairwise): pct_TSM ≤ 5% (top-5% most cohesive).
- A2, A3, A4 (spread axes): pct_TSM ≤ 5%.
- One-sided lower-tail tests; α_bon for axis = 0.05 / 4 = 0.0125; family-α (this test in family of 5) = 0.01 outermost.

## 6. Acceptance

- **CONFIRMED** = ≥ 3 of 4 axes pass at α = 0.0125 (top-5%).
- **DIRECTIONAL** = exactly 2 of 4 axes pass.
- **NULL** = ≤ 1 axis passes.
- **PRE-COMMIT VIOLATION** = TSM is among the LEAST cohesive (pct ≥ 95%) on ≥ 2 axes.

## 7. Rules-tuple

`(no-tashkeel for FR matrix, h-new-* default rules-tuples, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Anti-hallucination

All h-new-*.json paths cited above; computed deterministically.

## 9. Honest a-priori limits

- The 29 muqaṭṭaʿ-opened surahs differ massively in length / chronology; raw FR distances correlate with length to some degree. The h-new-111 FR-distance is L1-normalized + length-controlled (per H-NEW-111 MW-1).
- 3654 enumeration is exact; no Monte Carlo.
- The H-NEW-600 letter-family content-cohesion test was NULL across full-29, ḥawāmīm-7, ALM-6, ALR-5. This test extends to TSM-3 specifically, with a multi-axis (not just content) approach. The multi-axis approach is exploratory but the per-axis directions are pre-committed.
- The full-29 NULL means H1 directional probability is empirically below 50%; this test is genuinely directionally locked against the prior.
