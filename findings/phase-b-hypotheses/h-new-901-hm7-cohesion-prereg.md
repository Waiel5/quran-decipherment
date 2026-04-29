---
id: H-NEW-901
title: "Pre-registered ḥawāmīm-7 cluster cohesion test on Fisher-Rao QAC-stem-roots — direction-locked one-sided permutation"
phase: B+
status: PRE-REGISTERED 2026-04-28
date: 2026-04-28
agent: hawamim-7-cluster-synthesis
parent_finding_1: H-NEW-570 (muqaṭṭaʿāt-29 NULL @ 65.62%ile; HM-7 sub-cluster reported @ 20.90%ile in MW-5 sub-test, partial-NULL)
parent_finding_2: H-NEW-600 (DOUBLE NULL — ALM-6 @ 43.15%ile and ALR-5 @ 56.25%ile NULL — al-Biqāʿī family-munāsaba framework FALSIFIED at FR-roots scale)
parent_finding_3: H-NEW-97 (ALR PROPHET_PERSON p_mc=0.0059 — name-class signal localised, NOT FR-roots whole-surah)
seed: 20260428
n_perms: 10000
bonferroni_k: 1
alpha: 0.05
rules_tuple: |
  (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
  Fisher-Rao distance matrix from H-NEW-111 / QAC-STEM root tokens / QAC v0.4 /
  K_top=500 / Dirichlet α=0.5 / mushaf order
direction: |
  ONE-SIDED, locked BEFORE observation:
  H1: d̄(HM-7) < random-7 mean (cohesion direction)
  Equivalent statistic: %ile of d̄(HM-7) in 10000 random-7 subsets of {1..114} ≤ 5%
  Decision rule:
    %ile ≤ 5%   ⇒  CONFIRMED
    5 < %ile ≤ 16.67%  ⇒  DIRECTIONAL (cohesion at uncorrected α=0.05)
    16.67 < %ile ≤ 50%  ⇒  NULL (median or below)
    50 < %ile ≤ 95%  ⇒  NULL (above-median dispersion)
    %ile > 95%  ⇒  FALSIFIED (anti-cohesion, opposite of pre-committed direction)
verdict: PENDING
---

# H-NEW-901 — Pre-registered ḥawāmīm-7 cluster cohesion test

## 1. Question

The ḥawāmīm-7 = {Q 40, 41, 42, 43, 44, 45, 46} cluster comprises ALL 7 surahs in the Quran whose opening muqaṭṭaʿāt is حم. They are mushaf-position-contiguous (40-46), all classified Meccan, and they share the strongest classical *fadāʾil* citation among letter-families (Ibn ʿAbbās's *li-kulli shayʾin lubābun, wa-lubābu al-Qurʾāni al-ḥawāmīm* — "everything has a kernel, and the kernel of the Qurʾān is the ḥawāmīm"; cited Ibn Kathīr opening of Sūrat Ghāfir; al-Suyūṭī *al-Itqān* nawʿ 17).

[[h-new-570-muqattaat-content-cluster|H-NEW-570]] reported HM-7 at 20.90%ile in its MW-5 sub-test of letter-family cohesion (interpreted as partial-NULL). [[h-new-600-letter-families|H-NEW-600]]/610 then DOUBLE NULL'd ALM-6 (43.15%ile) and ALR-5 (56.25%ile), demonstrating that even the strongest classical-and-empirical priors do NOT translate into whole-surah FR-roots cohesion. The classical *al-ḥawāmīm dībāj al-Qurʾān* tradition has not yet been tested in a dedicated, direction-locked, single-Bonferroni-cell pre-registration. H-NEW-901 closes that gap.

This is a parallel test to H-NEW-600's protocol on the third-largest single-letter muqaṭṭaʿāt family (HM, n=7).

## 2. Cluster definition (LOCKED)

**HM-7** = {Q 40 Ghāfir / al-Muʾmin, Q 41 Fuṣṣilat, Q 42 al-Shūrā, Q 43 al-Zukhruf, Q 44 al-Dukhān, Q 45 al-Jāthiyah, Q 46 al-Aḥqāf}, K = 7.

All 7 share the حم opening; Q 42 has a unique two-verse muqaṭṭaʿāt (حم at v.1 + عسق at v.2); the other 6 have single-verse حم. For the purposes of letter-family cohesion the surah is included in HM by virtue of v.1 = حم. (Q 42's second muqaṭṭaʿāt would also place it in a ḤMʿSQ singleton family per [[h-new-97-name-letter-joint|H-NEW-97]] taxonomy.)

Source: al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 40; al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān* type-2 ([[h-new-130-fisher-rao-residuals|H-NEW-130]] / [[h-new-97-name-letter-joint|H-NEW-97]] taxonomy).

## 3. Protocol

### 3.1 PRIMARY test
1. Load Fisher-Rao distance matrix D from `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (114-surah symmetric Fisher-Rao matrix; rules-tuple `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan, K_top_roots=500, dirichlet_alpha=0.5)`).
2. Compute d̄(HM-7) = mean over C(7, 2) = 21 pairs.
3. Build NULL distribution: 10000 random 7-subsets of {1..114}, seed 20260428.
4. PRIMARY %ile = % of null draws with d̄ ≤ d̄(HM-7).

### 3.2 Sub-block secondary diagnostics (NOT primary; reported for transparency)
- HM-A {Q 40, 41, 42}, K=3: report d̄ and %ile in random-3 null (same seed stream offset)
- HM-B {Q 43, 44, 45, 46}, K=4: report d̄ and %ile in random-4 null (same seed stream offset)

These are SECONDARY (descriptive); they are NOT counted in the Bonferroni family. The PRIMARY single-cell test is the HM-7 K=7 cohesion-percentile.

### 3.3 Pre-committed acceptance gates
| %ile band | Verdict |
|:--|:--|
| ≤ 5.00 | CONFIRMED (H1 direction at α=0.05 single-test) |
| 5.00 < ≤ 16.67 | DIRECTIONAL (cohesion at uncorrected α=0.05 with Bonferroni-3 reservation; not for promotion) |
| 16.67 < ≤ 50.00 | NULL (median or below) |
| 50.00 < ≤ 95.00 | NULL (above-median dispersion) |
| > 95.00 | FALSIFIED (anti-cohesion, pre-commit violation) |

## 4. Bonferroni accounting

k = 1 single primary cell. α = 0.05.

The two SECONDARY sub-block diagnostics (HM-A, HM-B) are NOT counted in the family because:
- They are descriptive (not hypothesis-decisional).
- They are POST-HOC labelled (HM-A vs HM-B emerged from prior empirical entropy bifurcation observation, not from pre-test cohesion hypothesis).
- They are flagged MW-7 capped if quoted as inferential.

## 5. Hypotheses

| Source | Predicted direction | Magnitude |
|:--|:--|:--|
| Ibn ʿAbbās *al-ḥawāmīm dībāj al-Qurʾān* (al-Suyūṭī *Itqān* nawʿ 17) | cohesion (≤ 50%ile) | qualitative |
| al-Zarkashī *al-Burhān* on letter-family clusters | cohesion | qualitative |
| al-Bāqillānī on muqaṭṭaʿāt | not-determined | — |
| al-Biqāʿī *Naẓm al-durar* family-*munāsaba* | cohesion | strong |
| Ibn Masʿūd in Ibn Kathīr opening of Sūrat Ghāfir (*idhā waqaʿta fī Āl Ḥā Mīm fa-qad waqaʿta fī rawḍātin*) | cohesion | strong |
| [[h-new-570-muqattaat-content-cluster|H-NEW-570]] §5 (HM-7 sub-test 20.90%ile) | weak partial cohesion | weak |
| [[h-new-600-letter-families|H-NEW-600]] DOUBLE NULL (ALM-6, ALR-5) | NULL by analogy | strong |

The classical scholarship + al-Biqāʿī predict cohesion. The recent [[h-new-600-letter-families|H-NEW-600]] DOUBLE NULL predicts NULL by extension. H-NEW-901 adjudicates between these.

## 6. Honest limits

1. **FR-roots only.** Verse-level, phonological, or rhyme-level cohesion is NOT covered by this pre-reg. The empirical bifurcation between HM-A (high rhyme entropy) and HM-B (near-monorhyme) is captured separately in the per-surah empirical profiles.
2. **K=7 small-N**. Percentile resolution at 10000 perms ≈ 0.01 absolute pp (good).
3. **Q 42 ḤM-ʿSQ split-muqaṭṭaʿāt.** Q 42 is treated as HM-family member by virtue of v.1 = حم (its second-verse عسق places it as a singleton in a separate family, but is not pre-registered as exclusion criterion).
4. **PRIOR**: [[h-new-570-muqattaat-content-cluster|H-NEW-570]] reports HM-7 at 20.90%ile in a different rules-tuple variant. H-NEW-901 uses the strict default tuple.
5. **Sub-block diagnostics** are descriptive only; promotion-grade interpretation is gated by pre-registered HM-7 PRIMARY result.

## 7. Deliverables

- This pre-reg locked 2026-04-28; sha256 embedded in run script.
- Run script: `/Users/grey/Downloads/quran/scripts/h_new_901_hm7_cohesion.py`
- Output JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-901-hm7-cohesion.json`
- Findings markdown: published as integrated section §5 of `/Users/grey/Downloads/quran/surahs/hawamim-7-cluster-synthesis.md`.

## 8. Direction LOCKED. ONE text. Equal NULL prominence.

Pre-reg locked 2026-04-28. SHA256 to be computed and embedded in run script before execution.
