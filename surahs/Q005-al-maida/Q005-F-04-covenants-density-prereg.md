---
finding_id: Q005-F-04
prereg_date: 2026-05-07
prereg_type: per-surah covenant-vocabulary density rank
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q005 deep-dive (F-01..F-05)
alpha_bon: 0.01
rules_tuple: "(no-tashkeel, QAC-ROOT tokens, QAC v0.4, basmala-counted-only-in-surah-1, Hafs-Kufan, Mashriqi)"
---

# Q005-F-04 — Multiple-covenants vocabulary density

## 1. Background

al-Rāzī (*Mafātīḥ al-ghayb*, on Q 5:1, 5:7, 5:12-14, 5:70) identifies Q 5 as the surah of *multiple-covenants*: Q 5:1 is the general "wafāʾ bi-l-ʿuqūd" (fulfill the contracts); Q 5:7 the Muslim community's mīthāq; Q 5:12 the Israelite mīthāq with twelve naqībs; Q 5:14 the Christian mīthāq; Q 5:70 a re-affirmation of the Israelite mīthāq.

Empirical question: among the 5 Medinan-legal surahs {Q 2, 3, 4, 5, 9}, is Q 5's covenant-vocabulary density per 100 words *in the top 3*?

## 2. Frozen covenant root family (QAC v0.4 ROOT)

| Concept | Root |
|:--|:--|
| mīthāq / wāthaqa | `wvq` |
| ʿahd / promise-covenant | `Ehd` |
| ʿaqd / contract (Q 5:1) | `Eqd` |
| naqḍ / breaking | `nqD` |

(akhadhnā / akhadha — root `Ax*` — is excluded because it is too broad: the "taking" verb is not a covenant-specific marker except in fixed phrases like *akhadhnā mīthāqa*; isolating those phrases requires bigram lookups outside the QAC root-index protocol.)

## 3. Hypothesis (DIRECTION-LOCKED)

**H1 (primary)**: Q 5 covenant-density (covenant-root tokens / 100 words) ranks in the **top 3** corpus-wide (114 surahs).

**H1' (secondary)**: Q 5 covenant-density ranks **#1** within the 5-surah Medinan-legal cluster {Q 2, 3, 4, 5, 9}.

## 4. Null

**H0**: Q 5 covenant-density ranks below position 3 corpus-wide AND below #2 in the 5-surah cluster.

## 5. Method

1. Per surah, sum tokens of the 4 covenant roots from QAC v0.4.
2. Density(s) = 100 × tokens(s) / words(s) using `quran-no-tashkeel.json` whitespace word counts.
3. Rank densities. Record Q 5's rank corpus-wide and within {Q 2, 3, 4, 5, 9}.
4. Permutation null: shuffle the 4-root token-counts across the 114 surah-positions (preserving each surah's word count), recompute Q 5's rank, repeat 10000× under seed 20260507.

## 6. Pre-committed thresholds

| Outcome | Verdict |
|:--|:--|
| Q 5 corpus-rank ≤ 3 AND p_perm < α_bon = 0.01 | VINDICATED al-Rāzī multi-covenant density claim |
| Q 5 corpus-rank ≤ 3 but p_perm ≥ α_bon | DIRECTIONAL |
| Q 5 corpus-rank > 3 | NULL |

## 7. Garden-of-forking-paths log

- Roots frozen before running. The Q 5 wvq=6 count is known from the QAC root-index pre-flight (file `/tmp/q5_roots.json` per inspection); this is a *pre-flight calibration* not a result-observation. The corpus-wide ranks ARE NOT yet observed.
- The "top 3" corpus-wide gate is the primary; "rank-1 within Medinan-5" is a secondary check independent of the corpus-wide perm-null.

## 8. Pre-commit locked.
