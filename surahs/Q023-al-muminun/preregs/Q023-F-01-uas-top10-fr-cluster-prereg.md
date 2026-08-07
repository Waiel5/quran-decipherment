---
finding_id: Q023-F-01
title: Q 23 UAS rank verification + UAS top-10 cluster Fisher-Rao cohesion vs length-matched corpus null
date: 2026-05-09
seed: 20260509
n_perms: 10000
status: PRE-REGISTERED
rules_tuple: (no-tashkeel, QAC-stem-roots, QAC v0.4, Fisher-Rao K=500 stem-roots Dirichlet alpha=0.5, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan, Mashriqi)
---

# Q023-F-01 — UAS top-10 cluster FR-cohesion (Q 23 within the rank-9 / top-10 set)


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

## 1. Background

[[h-new-840-unified-architectural-score|H-NEW-840]] computes the Unified Architectural Score (UAS) for all 114 surahs as a z-sum of three correlated axes (|outlier-strength|, max canonical-adjacency cost, |iʿjāz signature|). The top-10 UAS surahs are reported as `Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17` per H-NEW-840 `top_15` entries 1-10.

Q 23 al-Muʾminūn is **rank 9** (UAS 2.977) per the existing 01-empirical-profile §1. The session handoff lists Q 23 in the top-10 UAS cluster.

This pre-reg tests whether the **top-10 UAS surahs are mutually closer on Fisher-Rao than a length-matched random sample**.

## 2. Hypothesis

The top-10 UAS surahs `{Q 1, 2, 9, 10, 12, 17, 23, 24, 33, 55}` should be **architecturally distinctive on the root-distribution axis as well**. Since UAS rewards |outlier|, large adjacency cost, and large |iʿjāz signature|, all of which reflect distinctive root-distribution profiles, the top-10 surahs may either:

- (a) be FR-cohesive (mean pairwise FR distance LOWER than length-matched null) → root-distribution cluster
- (b) NOT FR-cohesive → UAS top-10 cluster on different axes (cost, monorhyme, outlier-magnitude) than root-distribution

**Pre-registered DIRECTION**: top-10 UAS surahs are **FR-tighter** than a length-matched corpus null (alternative hypothesis: mean pairwise FR distance LOWER than null).

This is grounded in (i) UAS's |outlier| axis being computed from root-distribution; (ii) the project's earlier H-NEW-1190 sub-cluster work showing that high-outlier surahs concentrate.

**Failure direction**: if observed mean is HIGHER than null (top-10 UAS are FR-dispersed not cohesive), publish as NULL with prominence. A reversed direction is a pre-commit-violation NULL per Protocol §1.8.

## 3. Test statistic and null

**Statistic**: mean pairwise FR distance within the top-10 UAS set:

```
T_obs = mean { D[i,j] : i,j ∈ top10, i != j }
```

where `D` is the 114×114 Fisher-Rao matrix from `findings/phase-b-hypotheses/csv/h-new-111.json` (reconstructed from `D_matrix_upper_triangular`).

**Length-matched null**: for each top-10 surah, identify the set of all corpus surahs (excluding the top-10 itself) whose verse-count is within ±20% of the target. Then sample 10000 random length-matched subsets of size 10 from the corpus, computing the mean pairwise FR distance of each. The null distribution is the resulting 10000-vector.

**Seed**: 20260509.

**p-value**:
- Lower-tailed (pre-registered direction): `p = (#{T_null_i ≤ T_obs} + 1) / (N+1)`.
- Two-tailed for completeness: `min(p_lower, 1-p_lower) * 2`.

## 4. Decision rules

- **PASS-DIRECTED (CONFIRMED)**: lower-tail p ≤ 0.05 AND T_obs < median(T_null). Top-10 UAS cluster is FR-cohesive.
- **NULL**: lower-tail p > 0.05 OR direction reversed. The top-10 UAS cluster is NOT FR-cohesive.
- **PRE-COMMIT VIOLATION**: if direction reversed AND magnitude large (|T_obs − median| > 0.5*stdev), flag explicitly per Protocol §1.8.

Bonferroni note: this is **1 of 3 pre-registered tests** in the Q 23 specialist landing (Q023-F-01, F-02, F-03), so the family-Bonferroni-corrected α is 0.05/3 = 0.0167.

## 5. MW protections

- **MW-1 (instrument)**: Fisher-Rao distance from H-NEW-111 (pre-existing, locked).
- **MW-2 (corpus)**: 10000 permutations.
- **MW-3 (alt models)**: report both length-matched null and a strict-random null (no length-matching).
- **MW-5 (replication)**: at higher seed 20260510 confirm.
- **MW-6 (instrument-control)**: report mean pairwise FR for a random 10-set from corpus.

## 6. Pre-reg lock

This file is locked at SHA256-of-contents. Embedded in the runner script. Verified at runtime.
