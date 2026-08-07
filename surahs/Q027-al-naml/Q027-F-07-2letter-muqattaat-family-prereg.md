---
finding_id: Q027-F-07
title: 2-letter muqaṭṭaʿ family — joint multi-axis cohesion of {Q 20 ṬH, Q 27 ṬS, Q 36 YS} vs random muqaṭṭaʿāt 3-tuples
date_preregistered: 2026-05-07
phase: B+
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q027-F-05..F-09
alpha_bon: 0.01
acceptance_window: see §6
---

# Q027-F-07 — 2-Letter Muqaṭṭaʿ Family Joint Cohesion


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 0. Origin and prior context

The Quran has 29 muqaṭṭaʿāt-opened surahs. Among these, **exactly 3 surahs open with a 2-letter muqaṭṭaʿ**:
- **Q 20 طه (ṬH)**
- **Q 27 طس (ṬS)**
- **Q 36 يس (YS)**

Each of the three letter-pairs is corpus-unique (no other surah opens with ṬH, ṬS, or YS). All 3 are mid-to-late Meccan; all 3 are sustained-narrative or theological-emphasis surahs.

The complementary axis to Q026-F-02 (which tested ṬSM-cluster cohesion within 3 ṬSM-cluster sister surahs and returned NULL) is the **2-letter-singleton family**. This is structurally orthogonal: ṬSM-cluster shares letter-strings; 2-letter-family shares letter-string structure (length-2). F-07 tests whether the 2-letter family is empirically cohesive on multi-axis architectural metrics, vs random 3-tuples drawn from the 29 muqaṭṭaʿāt-opened set.

This test coordinates with prior Q020 + Q036 specialists at the **DIFFERENT-FAMILY-axis**, not within the TSM/ḥawāmīm-axis from Q026-F-02.

## 1. Hypothesis (locked before observation)

**H1 (composite)**: The 3-tuple {Q 20, Q 27, Q 36} is **structurally cohesive** vs random 3-tuples drawn from the 29 muqaṭṭaʿāt-opened surahs. Cohesion is operationalized as a **joint score**:

S(tuple) = α · (mean pairwise FR distance, lower=cohesive) + β · (sig_A spread, lower=cohesive) + γ · (UAS spread, lower=cohesive) + δ · (1 - rhyme-top-letter agreement)

with all coefficients pre-committed equal-weighting (α = β = γ = δ = 0.25); each component is z-normalized over the 29-tuple permutation distribution.

**H1**: S({Q 20, Q 27, Q 36}) < random 3-tuple mean S; one-sided lower-tail. Pre-committed prediction direction: cohesive (lower S).

**H0**: S = random 3-tuple null distribution.

## 2. Operational definitions

The 29 muqaṭṭaʿāt-opened surahs are: Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68. (Source: classical Quranic-sciences canon, e.g., al-Suyūṭī *al-Itqān* nawʿ 43.)

For each 3-tuple T = {a, b, c}:
- **mean_FR(T)** = mean over the 3 pair distances of FR-roots distance (from `findings/phase-b-hypotheses/csv/h-new-111.json`, `D_matrix_upper_triangular`).
- **sig_A_spread(T)** = max(sig_A) − min(sig_A) over a, b, c (from `h-new-750.json`).
- **UAS_spread(T)** = max(UAS) − min(UAS) (from `h-new-840.json`).
- **rhyme_top_letter_agreement(T)** = max-class-share of top-rhyme-letter across a, b, c. Three values ∈ {1/3, 2/3, 3/3}; we use (1 − max-share) as the "disagreement" component.

For each component, we z-score over the population of (29 choose 3) = 3654 3-tuples; then take the equally-weighted mean. The joint score S is one-tailed lower (cohesive) for the target 2-letter tuple.

## 3. Test statistics

- **stat_join** = S({Q 20, Q 27, Q 36}).
- **null distribution** = {S(T) : T ∈ (29 choose 3) tuples}.
- **p_perm** = #(S_random ≤ stat_join) / (29 choose 3).
- **stat_indiv per axis** (for transparency, NOT the primary test):
  - mean_FR rank percentile within (29 choose 3).
  - sig_A_spread rank percentile.
  - UAS_spread rank percentile.
  - rhyme-letter-agreement rank percentile.

## 4. Direction (LOCKED before observation)

- H1: stat_join in bottom 30%ile of the 3654 random tuple distribution (i.e., p_perm ≤ 0.30 directionally; p_perm < 0.01 for Bonferroni-pass).
- The reverse direction (top 30%ile = anti-cohesive) is a **pre-commit violation** — would publish as NULL with full prominence.

## 5. Permutation null

- Population: full (29 choose 3) = 3654 tuples — exact enumeration, no sampling needed.
- Seed 20260507 reserved for any tie-breaks or replication.
- For each tuple, compute mean_FR, sig_A_spread, UAS_spread, (1 − rhyme-letter-agreement); z-score across the 3654-population per axis; mean of 4 z-scores = S(T).
- p_perm = (#(S_random ≤ S_target) + 1) / (3654 + 1).

## 6. Bonferroni and acceptance

- bonferroni_k = 5 (Q027-F-05..F-09 family); α_bon = 0.01.
- Per-axis sub-tests within F-07 are NOT corrected (they are diagnostics of the joint score, not independent claims).
- **Acceptance windows** (LOCKED before observation):
  - **CONFIRMED** = stat_join in bottom 1%ile (p_perm < 0.01) AND ≥ 3 of 4 component axes individually in bottom 30%ile.
  - **DIRECTIONAL** = stat_join in bottom 5%ile, OR ≥ 3 of 4 components in bottom 30%ile.
  - **NULL** = stat_join above 30%ile AND ≤ 2 of 4 components in bottom 30%ile.
  - **PRE-COMMIT VIOLATION** = stat_join in top 30%ile.

## 7. Rules-tuple

`(no-tashkeel, QAC-stem-roots for FR; raw rhyme top-letter from h-new-700; UAS from h-new-840; sig_A from h-new-750; basmala-counted-only-in-Q1; Hafs-Kufan; Mashriqi)`. Letter-family enumeration uses canonical 29-set (al-Suyūṭī *al-Itqān* nawʿ 43).

## 8. Anti-hallucination

- FR D-matrix: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`.
- iʿjāz signatures: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json`.
- UAS: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json`.
- Rhyme top-letter: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json`.
- 29-muqaṭṭaʿāt list: classical canon; cross-validated via H-NEW letter-family pages.

## 9. Honest a-priori limits

- The "cohesion" framework is multi-dimensional; the equal-weighting choice is a-priori (no post-hoc reweighting allowed). A different weighting could shift verdicts.
- Q026-F-02 NULL on TSM-cluster cohesion was at the SAME-LETTER-STRING axis (Q 26, Q 28 share ṬSM); F-07 is at the LENGTH-2 STRUCTURE axis (Q 20 has ṬH, Q 27 has ṬS, Q 36 has YS — different letter-pairs). These are DIFFERENT and ORTHOGONAL hypotheses; F-07 may PASS or NULL independently of Q026-F-02 NULL.
- The 29-tuple population is a fixed combinatorial space; the percentile estimate is exact.
- Rhyme top-letter agreement is a discrete variable (3 surahs → ∈{1/3, 2/3, 3/3}); the "(1 − max-share)" component is coarse. We report it as a diagnostic.
- Mean pairwise FR distance has natural variance across 3-tuples; the standard rank-percentile approach captures this faithfully.

## 10. Cross-references

- [[Q026-al-shuara/Q026-F-02-tsm-cluster-cohesion-prereg.md|Q026-F-02]] — TSM-cluster cohesion (NULL).
- [[Q020-ta-ha]] — sister 2-letter ṬH.
- [[Q036-yasin]] — sister 2-letter YS.
- [[h-new-600-letter-families]] — 29-set letter-family precedent.

## 11. Garden-of-forking-paths log

- The 4-component composite + equal weighting is a-priori; locked before computation.
- The 30%/1% acceptance bands are pre-committed before observation.
- The 29-tuple enumeration is exhaustive — no sampling-bias concern.
- The hypothesis direction is "cohesive" (lower S) — locked. The reverse direction would be a pre-commit violation.
- Choice of 4 axes (FR, sig_A, UAS, rhyme-top) reflects the 4 main architectural metrics in the project (compression-tail's d̄_content, iʿjāz signature, UAS composite, rhyme dispersion). A 5th axis (e.g., verse count uniformity) is NOT included to avoid post-hoc family expansion.
