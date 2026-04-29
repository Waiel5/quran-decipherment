---
finding_id: h-new-221
title: Cross-feature replication of H-NEW-212 under NCD (non-parametric compression distance)
status: CONFIRMED
date: 2026-04-17
seed: 20260419
permutations: 10000
bonferroni_k: 3
alpha_bon: 0.01667
parent_lineage: [H-NEW-169, H-NEW-212, cross-finding-011]
---

# [[h-new-221-ncd-alt-chronology|H-NEW-221]] — NCD cross-feature replication

## Result (one line)

**Mushaf rank 1 of 5 under NCD-lzma; all three pre-registered chronology
tests (Egyptian 1924, Bell 1937, Blachère 1947) PASS Bonferroni α=0.01667
with p=1e-4 (perm min).** Non-parametric evidence that the mushaf
organizing-principle is code-independent.

## Numbers

| Ordering        | L_NCD      | z vs null | p (1-sided lower) |
|-----------------|-----------:|----------:|------------------:|
| **mushaf**      |  86.286128 |   −15.730 | 0.0001            |
| noldeke_1860    |  90.232081 |   −10.710 | 0.0001 (ref)      |
| egyptian_1924   |  90.671995 |   −10.150 | 0.0001 **PASS**   |
| blachere_1947   |  90.749216 |   −10.052 | 0.0001 **PASS**   |
| bell_1937       |  90.914767 |    −9.842 | 0.0001 **PASS**   |

Null (10K uniform perms, seed 20260419): mean 98.651, sd 0.786, min 95.424.
All five orderings are already ≤ null min — the null cannot resolve p below
1e-4 (floor of `(0+1)/(10000+1)`).

Mushaf is **4.39–4.63 NCD units shorter** than the three chronologies
(5.02–5.89 null-SDs below them).

## Verdicts

- `family_any_pass` = **true** (all 3 in fact pass)
- `mushaf_still_wins_over_all_3_chronologies` = **true**
- `shortest_name` = `mushaf`
- `mushaf_rank_among_5` = **1**

## Cross-feature concordance

- [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] (Fisher-Rao QAC-STEM) leaderboard:
  `[mushaf, noldeke_1860, bell_1937, egyptian_1924, blachere_1947]`
- [[h-new-221-ncd-alt-chronology|H-NEW-221]] (NCD-lzma) leaderboard:
  `[mushaf, noldeke_1860, egyptian_1924, blachere_1947, bell_1937]`
- Identical? no — but **top two (mushaf, noldeke_1860) are preserved**;
  differences are only in the middle of the pack.
- Spearman ρ between leaderboard positions: **+0.70**.

## Why this matters

[[cross-finding-011-mushaf-fisher-rao-confirmed|Cross-finding-011]] + [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] showed the mushaf-beats-chronology result
under TWO parametric Fisher-Rao feature spaces (QAC-STEM K=500;
char-4gram K=2000). Both rely on smoothed probability vectors → angular
distance — a specific statistical geometry.

[[h-new-221-ncd-alt-chronology|H-NEW-221]] replicates the same 3-chronology family under a NON-PARAMETRIC
information-theoretic distance that requires no tokenization, no
smoothing, no K-hyperparameter. The signal survives.

That the identical leaderboard ordering of the **winners** (mushaf > Nöldeke)
is preserved across parametric (Fisher-Rao stems, Fisher-Rao char-4grams)
AND non-parametric (NCD-lzma) feature spaces is evidence that whatever
organizes the mushaf is not an artefact of any particular tokenization or
vectorization — it shows up in raw byte-compression too.

## Files

- script: `scripts/h_new_221_ncd_alt_chronology.py`
- pre-reg: `findings/phase-b-hypotheses/h-new-221-ncd-alt-chronology-prereg.md`
  (SHA-256 logged in JSON)
- output: `findings/phase-b-hypotheses/csv/h-new-221.json`
- D-matrix: `findings/phase-b-hypotheses/csv/h-new-169-ncd-matrix.npy` (inherited)
