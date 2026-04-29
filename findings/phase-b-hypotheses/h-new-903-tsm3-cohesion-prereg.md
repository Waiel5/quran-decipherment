---
id: H-NEW-903
title: "Pre-registered ṬSM-3 cluster cohesion test on Fisher-Rao QAC-stem-roots — direction-locked one-sided permutation"
phase: B+
status: PRE-REGISTERED 2026-04-28
date: 2026-04-28
agent: tsm-3-cluster-investigation
parent_finding_1: H-NEW-901 (HM-7 NULL @ 21.21%ile — strongest classical *fadāʾil* claim DOES NOT translate to FR-roots cohesion)
parent_finding_2: H-NEW-600 (DOUBLE NULL — ALM-6 @ 43.15%ile, ALR-5 @ 56.25%ile NULL)
parent_finding_3: H-NEW-910 (alif-8 NULL @ 25.55%ile — letter/rāwī axis ⊥ content axis)
parent_finding_4: H-NEW-570 (muqaṭṭaʿāt-29 NULL @ 65.62%ile)
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
  H1: d̄(ṬSM-3) < random-3 mean (cohesion direction)
  Equivalent statistic: %ile of d̄(ṬSM-3) in 10000 random-3 subsets of {1..114} ≤ 5%
  Decision rule:
    %ile ≤ 5%   ⇒  CONFIRMED
    5 < %ile ≤ 16.67%  ⇒  DIRECTIONAL (cohesion at uncorrected α=0.05)
    16.67 < %ile ≤ 50%  ⇒  NULL (median or below)
    50 < %ile ≤ 95%  ⇒  NULL (above-median dispersion)
    %ile > 95%  ⇒  FALSIFIED (anti-cohesion, opposite of pre-committed direction)
verdict: PENDING
---

# H-NEW-903 — Pre-registered ṬSM-3 cluster cohesion test

## 1. Question

The ṬSM-3 = {Q 26 al-Shuʿarāʾ, Q 27 al-Naml, Q 28 al-Qaṣaṣ} cluster comprises THREE mushaf-contiguous Meccan surahs sharing the **ṭāʾ-sīn** muqaṭṭaʿāt opener (Q 26 and Q 28 with full ṬSM, Q 27 with the ṬS short form). They open with structurally parallel book-reference verses:

- Q 26:1-2: طسم / *tilka āyātu al-kitābi al-mubīn* — "These are the verses of the Clear Book"
- Q 27:1: طس / *tilka āyātu al-Qurʾāni wa-kitābin mubīn* — "These are the verses of the Qurʾān, and a Clear Book"
- Q 28:1-2: طسم / *tilka āyātu al-kitābi al-mubīn* — "These are the verses of the Clear Book"

This is the strongest verbal-formulaic parallelism among any contiguous muqaṭṭaʿāt cluster — Q 26 and Q 28 share an *identical* opening verse 2, with Q 27 a verbal variant of the same demonstrative formula (cf. [[h-new-57-formulaic-openings|H-NEW-57]] *tilka āyāt* opener, 13/13 muqaṭṭaʿāt-exclusive at p=1.6×10⁻⁹).

[[h-new-901-hm7-cohesion-prereg|H-NEW-901]] tested the strongest classical *fadāʾil* claim (ḥawāmīm-7 = "kernel of the Qurʾān") and reported NULL @ 21.21%ile. [[h-new-600-letter-families|H-NEW-600]] DOUBLE-NULLed ALM-6 and ALR-5. [[h-new-910-alif8-cluster|H-NEW-910]] NULLed the alif-8 rāwī cluster. **All four prior letter-axis cohesion tests have reported NULL.**

H-NEW-903 is the **first muqaṭṭaʿāt-cluster cohesion test where verbal-formulaic parallelism in the opening verses is explicit and identical**, providing a stronger structural hypothesis. Will the ṬSM-3 break the NULL streak?

## 2. Cluster definition (LOCKED)

**ṬSM-3** = {Q 26 al-Shuʿarāʾ, Q 27 al-Naml, Q 28 al-Qaṣaṣ}, K = 3.

The cluster is defined by the shared ṭ-s root muqaṭṭaʿāt-prefix (ṬSM ⊃ ṬS). Q 27's ṬS is the same first two letters as Q 26's and Q 28's ṬSM. The three are mushaf-contiguous (positions 26-27-28, three consecutive surahs).

Source for ṭ-s family: al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 40; al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān* type-2 muqaṭṭaʿāt taxonomy.

## 3. Protocol

### 3.1 PRIMARY test
1. Load Fisher-Rao distance matrix D from `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (114-surah symmetric Fisher-Rao matrix; rules-tuple `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan, K_top_roots=500, dirichlet_alpha=0.5)`).
2. Compute d̄(ṬSM-3) = mean over C(3, 2) = 3 pairs: (Q26,Q27), (Q26,Q28), (Q27,Q28).
3. Build NULL distribution: 10000 random 3-subsets of {1..114}, seed 20260428.
4. PRIMARY %ile = % of null draws with d̄ ≤ d̄(ṬSM-3).

### 3.2 Comparator-NULL prior tests (NOT primary, descriptive only)

For interpretive context, report d̄_obs and %ile alongside ALL prior letter-axis cohesion tests:

| Cluster | K | Source | Prior result |
|:-:|:-:|:-:|:-:|
| muqaṭṭaʿāt-29 | 29 | H-NEW-570 | NULL @ 65.62% |
| ALM-6 | 6 | H-NEW-600 | NULL @ 43.15% |
| ALR-5 | 5 | H-NEW-600 | NULL @ 56.25% |
| HM-7 | 7 | H-NEW-901 | NULL @ 21.21% |
| alif-8 | 8 | H-NEW-910 | NULL @ 25.55% |
| **ṬSM-3** | **3** | **H-NEW-903 (THIS)** | **PENDING** |

These are descriptive comparisons; they are NOT counted in the Bonferroni family. The PRIMARY single-cell test is the ṬSM-3 K=3 cohesion-percentile.

### 3.3 Pre-committed acceptance gates

| %ile band | Verdict |
|:--|:--|
| ≤ 5.00 | CONFIRMED (H1 direction at α=0.05 single-test) |
| 5.00 < ≤ 16.67 | DIRECTIONAL (cohesion at uncorrected α=0.05; not for promotion) |
| 16.67 < ≤ 50.00 | NULL (median or below) |
| 50.00 < ≤ 95.00 | NULL (above-median dispersion) |
| > 95.00 | FALSIFIED (anti-cohesion, pre-commit violation) |

## 4. Bonferroni accounting

k = 1 single primary cell. α = 0.05. The comparator-NULL prior tests are NOT counted in the family because they are PRIOR results (already published) being cited for context, not new tests.

## 5. Hypotheses (predicted directions)

| Source | Predicted direction | Magnitude |
|:--|:--|:--|
| al-Biqāʿī *Naẓm al-durar* family-*munāsaba* (Q 26-27-28 are a narrative-parallel triplet) | cohesion | strong |
| al-Suyūṭī *al-Itqān* nawʿ 40 (muqaṭṭaʿāt clusters) | cohesion | qualitative |
| Verbal-formulaic identity Q 26:2 = Q 28:2 (*tilka āyāt al-kitāb al-mubīn*) | cohesion | strong |
| Mushaf-contiguity + shared Meccan period | cohesion | qualitative |
| [[h-new-901-hm7-cohesion-prereg|H-NEW-901]] HM-7 NULL @ 21.21% | NULL by analogy | strong |
| [[h-new-600-letter-families|H-NEW-600]] DOUBLE NULL | NULL by analogy | strong |
| [[h-new-910-alif8-cluster|H-NEW-910]] alif-8 NULL | NULL by analogy | strong |
| **Cumulative prior: 4 of 4 letter-axis cohesion tests NULL** | NULL | very strong |

The classical scholars + verbal parallelism predict cohesion. The **4-of-4 NULL prior streak** predicts NULL by induction. H-NEW-903 adjudicates.

## 6. Honest limits

1. **FR-roots only.** Verse-level, phonological, or rhyme-level cohesion is NOT covered.
2. **K=3 small-N.** With only 3 pairs, the variance of d̄ is large; power is limited. The percentile resolution at 10000 perms ≈ 0.01pp (good) but the underlying statistic has high stochastic variance.
3. **Verbal-formulaic parallelism in v.1-2 is NOT what FR-roots measures.** The h-new-111 metric measures whole-surah QAC-STEM root distribution. A surah's first two verses contribute ≪1% of its root tokens. We are testing whether opening-formulaic parallelism predicts whole-surah content-distribution similarity. Prior NULLs suggest it does not.
4. **No alternate-rules-tuple cross-check** in this primary cell. A separate Risan-recension or min-tashkeel check could be run as MW-6 secondary.

## 7. Deliverables

- Pre-reg SHA256 to be computed and embedded in run script before execution.
- Run script: `/Users/grey/Downloads/quran/scripts/h_new_903_tsm3_cohesion.py`
- Output JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-903-tsm3-cohesion.json`
- Findings markdown: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-903-tsm3-cohesion.md`

## 8. Direction LOCKED. ONE text. Equal NULL prominence.

Pre-reg locked 2026-04-28 by tsm-3-cluster-investigation agent. SHA256 to be computed and embedded in run script before execution.
