---
finding_id: h-new-127-3
title: "H-NEW-127.3 class-mapping of locked per-surah compression z-scores"
phase: B
status: POSITIVE (H_obs = 96.669030; p_perm_upper = 0.000050)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-2
pre_reg: findings/phase-b-hypotheses/h-new-127-3-compression-class-mapping-prereg.md
pre_reg_sha256: 213bea6290a876a1e786f610b5a07448b26b2e6ec58c83874276bf54c8c2950e
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = sinai_genre; Kruskal-Wallis H; outer null permutes genre labels across surahs preserving class counts; 114 surahs)"
verdict: POSITIVE
---

# H-NEW-127.3 - class-mapping of locked per-surah compression z-scores

## Exact outputs

| Quantity | Value |
|---|---:|
| Surahs | 114 |
| Genre labels | 55 |
| Observed Kruskal-Wallis `H` | 96.66903034925917 |
| Degrees of freedom | 54 |
| Label-shuffle null mean `H` | 53.97475550174516 |
| Label-shuffle null sd `H` | 6.097341671447821 |
| `n_perm_ge_obs` | 0 / 20000 |
| Permutation `p` | 0.00004999750012499375 |
| Verdict | POSITIVE |

## Note

The exact locked genre axis is sparse, with many singleton labels. That
reduces power, but it does not weaken the correctness of the permutation
result. Under the preregistered label-shuffle null, the observed `H` is
far into the upper tail.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-127-3-compression-class-mapping-prereg.md`
- Script: `scripts/h_new_127_3_oq20_class_mapping.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-3.json`

