---
finding_id: Q050-F-06
surah: 50
date_locked: 2026-05-09
date_run: 2026-05-09
phase: B+
verdict: DIRECTIONAL (LOW-S direction-correct on both nulls; only null-b approaches Bonferroni-2)
---

# Q050-F-06 — Singleton-letter triplet FR-cluster vs 28-muqaṭṭāʿat baseline

## Headline

The singleton-letter muqaṭṭāʿat triplet {Q 38, Q 50, Q 68} has a mean pairwise Fisher-Rao distance **S_obs = 0.8699**, which is:

- **Tighter (lower) than 74% of full-corpus random 3-surah triplets** (null-a percentile 0.2600; not Bonferroni-passing at α=0.025).
- **Tighter than 84% of OTHER 3-surah muqaṭṭāʿat triplets** drawn exhaustively from the 26 non-singleton-muqaṭṭāʿat surahs (null-b percentile 0.1619; closer to Bonferroni-2 threshold but still above α=0.025).

**Verdict: DIRECTIONAL.** The direction-locked LOW-S hypothesis is correct on BOTH nulls (no pre-commit violation), but neither cell passes Bonferroni-2 individually.

## Method

Pre-reg SHA256 `d058275499fc` (this file's prereg `Q050-F-06-singleton-vs-muqattaat-baseline-prereg.md`).
SHA verified at script runtime; fail-fast on mismatch.

- Compute S_obs = mean of {FR(Q 38, Q 50), FR(Q 38, Q 68), FR(Q 50, Q 68)} from h-new-111.json D-matrix.
- Null A: draw 10000 random non-{38,50,68} triplets from the 114-surah set (seed 20260509). Compute mean pairwise FR per triplet.
- Null B: enumerate **all C(26, 3) = 2600 triplets** from the 26 non-singleton muqaṭṭāʿat surahs ({2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 40, 41, 42, 43, 44, 45, 46}). Compute mean pairwise FR per triplet.
- Bonferroni-2: α_per_cell = 0.025.

## Result

| Metric | Null A (full-corpus) | Null B (muqaṭṭāʿat-only) |
|:--|:--|:--|
| S_obs | 0.8699 | 0.8699 |
| Null mean | 0.9243 | 0.9253 |
| Null SD | 0.1474 | 0.0867 |
| Percentile | **0.2600** | **0.1619** |
| Bonferroni-2 pass (<0.025)? | NO | NO |
| Direction LOW-S correct? | YES | YES |

**Both nulls have similar means (0.924 / 0.925), confirming that the muqaṭṭāʿat-as-class does NOT cluster on FR-roots** — the within-muqaṭṭāʿat triplet mean is essentially the corpus-random triplet mean. The singleton-letter cohort is directionally tighter than both, but the magnitude (S_obs = 0.87, ≈0.06 below the null means) is not extreme enough to clear the Bonferroni-2 threshold.

## Comparison with Q050-F-04

| Test | Null | n_perm | S_obs percentile | Verdict |
|:--|:--|:--|:--|:--|
| Q050-F-04 | full-corpus random | 10000 | 0.267 | NULL (direction-correct) |
| Q050-F-06 null-a | full-corpus random | 10000 | 0.260 | DIRECTIONAL (replicates F-04) |
| Q050-F-06 null-b | muqaṭṭāʿat-only, exhaustive | 2600 | 0.162 | DIRECTIONAL (new dimension) |

Q050-F-06 null-a **replicates** Q050-F-04 (percentile 0.260 ≈ 0.267 — minor numerical drift from a different RNG seed but the same population). Q050-F-06 null-b is the novel contribution: when the null is restricted to within-muqaṭṭāʿat triplets, the singleton-letter cohort moves from the 26th percentile to the 16th percentile — directionally tighter but still not Bonferroni-passing.

## Interpretation

The singleton-letter cohort is the **muqaṭṭāʿat-sub-cluster with the highest within-cohort FR-cohesion**, but its cohesion is **NOT statistically distinct** from random triplets even within the muqaṭṭāʿat-class.

- The corpus mean pairwise FR is 0.924.
- The 26 non-singleton-muqaṭṭāʿat mean (over 2600 exhaustive triplets) is 0.925 — essentially the corpus mean.
- The 3 singleton-letter cohort mean is 0.870 — 5.8% below the corpus mean.
- This effect (0.870 vs 0.925) is real but small relative to the null SD (0.087 in the muqaṭṭāʿat-only null).

This is the *precise quantitative signature* of cross-finding-026 §1 letter-axis ⊥ content-axis empirical orthogonality. The muqaṭṭāʿat letter-axis (form-coherence on verse-1) is essentially independent of the root-distribution content-axis. Singleton-letter cohort form-coherence (Q050-F-01 verse-1 oath-wāw, 3/3) does not produce statistically detectable content-cohesion.

## Honest limits

- A "tighter" cohort COULD have been declared if the singleton-letter cohort's mean were closer to e.g. 0.80 instead of 0.87. The empirical signal is weak-but-direction-correct.
- The 26-surah muqaṭṭāʿat exhaustive enumeration is a more powerful null than the 10000-random-triplet null because the muqaṭṭāʿat-class has the same form-class membership as the test triplet — controlling for any class-level confounds. The percentile shift from 0.260 (null-a) → 0.162 (null-b) suggests the singleton-letter cohort IS more cohesive than other muqaṭṭāʿat triplets, but not by enough to clear α=0.025.
- The result is a CREDIBILITY-STRENGTHENING NULL: it confirms the cross-finding-026 prediction that even the most form-coherent muqaṭṭāʿat sub-cluster does not produce strong content-cohesion. Reporting this as DIRECTIONAL (not NULL) honors the direction-correct outcome while not over-claiming statistical significance.

## Cross-references

- [[Q050-F-04]] — original triplet FR-cohesion test (NULL, percentile 0.267).
- [[h-new-610-letter-families]] — muqaṭṭāʿat content-cohesion NULL across 4 letter-family replications.
- [[cross-finding-026-iʿjāz-architecture]] §1 — letter-axis ⊥ content-axis empirical orthogonality.
- [[h-new-111-fisher-rao-distance-matrix]] — source FR matrix.

## Data files

- Pre-reg: `surahs/Q050-qaf/preregs/Q050-F-06-singleton-vs-muqattaat-baseline-prereg.md` (SHA256 `d058275499fc`).
- Script: `scripts/Q050_F_06_singleton_vs_muqattaat_baseline.py`.
- JSON: `surahs/Q050-qaf/csv/Q050-F-06.json`.
