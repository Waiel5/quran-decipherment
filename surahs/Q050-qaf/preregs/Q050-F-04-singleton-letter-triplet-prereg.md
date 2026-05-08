---
finding_id: Q050-F-04
title: "Q 50 / Q 38 / Q 68 singleton-letter-triplet joint multi-axis profile vs random 3-surah triplets"
date_pre_registered: 2026-05-07
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q050-F-04-singleton-triplet
alpha_raw: 0.05
alpha_bon: 0.05
direction: "POSITIVE — the singleton-letter triplet (Q 50, Q 38, Q 68) has a joint multi-axis profile (FR-distance variance, outlier-strength sum, sig_A sum, sig_A spread) that is more extreme than 95% of N=10000 random 3-surah-triplets from the corpus."
rules_tuple: "(no-tashkeel, QAC-stem-roots, basmala-not-counted-elsewhere, Hafs-Kufan, mushaf-order, all metrics from H-NEW pipeline as published)"
---

# Q050-F-04 — Singleton-letter-triplet joint signature

## Hypothesis (LOCKED)

The singleton-letter muqaṭṭaʿāt opener subset is exactly THREE surahs:
- Q 38 ص (ṣād)
- Q 50 ق (qāf)
- Q 68 ن (nūn)

This subset has never been individually mathematically characterized in the project. The hypothesis: under a joint multi-axis profile, the triplet (Q 38, Q 50, Q 68) is more "tightly grouped" or more "internally distinct" than a random 3-surah triplet.

## Test statistic (LOCKED)

We define the "singleton-letter signature" S(triplet) as:

```
S = mean_pairwise_FR(triplet)                  ← internal-cohesion (lower = more internally cohesive)
```

A LOW S means the triplet's three surahs are FR-roots-CLOSE to each other (cluster-like).
A HIGH S means they are FR-roots-DISTANT (anti-cluster).

The pre-registered direction is **LOW S** — i.e., the singleton-letter triplet should be more INTERNALLY COHESIVE than 95% of random 3-surah triplets, despite their different chronological positions (Q 68 = revelation #2 early-Meccan; Q 38 = #38 middle-Meccan; Q 50 = #34 middle-Meccan per Tanzil Egyptian standard).

The DIRECTIONAL pre-commit is LOW S (cluster-like). If S is HIGH (anti-cluster), this is a pre-commit violation reported as NULL.

## Null model

For N=10000 iterations (seed 20260507):
1. Pick a random 3-surah triplet from the 114-surah corpus.
2. Compute S = mean_pairwise_FR for that triplet using h-new-111 distance matrix.
3. Form null distribution of S values.

Empirical p_low = (# null S ≤ S_singleton + 1) / (N + 1).

## Secondary test (descriptive only, no Bonferroni)

Report the (Q 38, Q 50, Q 68) values of:
- mean_content_distance (from h-new-750)
- sig_A (from h-new-750)
- abs_outlier (from h-new-590)
- top_final_letter (rāwī)
- mean rhyme_entropy

These are descriptive triplet-profile data only. The pre-commit for the primary verdict is the FR-cohesion test.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-stem-roots, basmala-not-counted-elsewhere, Hafs-Kufan, mushaf-order, all metrics from H-NEW pipeline as published)`

Source: h-new-111.json D_matrix_upper_triangular for FR distances; h-new-750.json per_surah for sig_A, mean_content_distance; h-new-590.json all_surahs_results for delta_pct.

## Success criteria

| p_low (1-sided, low-S) | Verdict |
|:--|:--|
| p_low < 0.05 | **CONFIRMED** (singleton-letter triplet is internally cohesive at FR-roots level) |
| 0.05 ≤ p_low < 0.10 | DIRECTIONAL |
| p_low ≥ 0.10 AND p_high < 0.10 | **PRE-COMMIT VIOLATION** → published as NULL with full prominence |
| else | NULL |

## Failure criteria

If the singleton-letter triplet's mean pairwise FR-distance is in the upper half of the null distribution → NULL with explicit pre-commit-violation flag (per INVESTIGATION-PROTOCOL §1.3 and §1.8).

## Honest priors

- Prior MUQAṬṬAʿĀT-CONTENT-MUNĀSABA findings (H-NEW-610 letter-families) returned NULL on whole-surah FR cohesion across muqaṭṭaʿāt sub-clusters. This pre-reg risks a similar NULL.
- Counter-prior: the SINGLETON-letter cohort is the SMALLEST muqaṭṭaʿāt sub-cluster (n=3), with the most extreme letter-isolation; if any sub-cluster shows joint cohesion, it is the most likely.
- Cross-finding-027 FALSIFIED a 5th iʿjāz cell candidate for Q 55. The 4-cell typology (cross-finding-026 §13) does NOT yet have a "singleton-letter cohort cell" — this test could yield evidence for or against expanding the typology.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q050_F_04_singleton_letter_triplet.py`.
- JSON: `csv/Q050-F-04.json`.
- Findings: `06-novel-findings.md` §Q050-F-04.
