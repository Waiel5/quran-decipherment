---
finding_id: h-new-127-9
title: "H-NEW-127.9 direct phase-structure test for locked per-surah compression z-scores"
phase: B
status: POSITIVE (H_obs = 81.878622; p_perm_upper = 0.000050)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-8
pre_reg: findings/phase-b-hypotheses/h-new-127-9-phase-structure-prereg.md
pre_reg_sha256: 424559a1e84d5768dd78beaf08077811b3f98115970e4e17dc32d13fbcd8d3a6
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = neuwirth_phase; Kruskal-Wallis H; outer null permutes phase labels across surahs preserving class counts; 114 surahs)"
verdict: POSITIVE
---

# H-NEW-127.9 - run log

## Command

```bash
python3 scripts/h_new_127_9_oq20_phase_structure.py
```

## Exact outputs

| Quantity | Value |
|---|---:|
| Surahs | 114 |
| Phases | 10 |
| Observed Kruskal-Wallis `H` | 81.87862170247757 |
| Degrees of freedom | 9 |
| Phase-shuffle null mean `H` | 8.994918270453827 |
| Phase-shuffle null sd `H` | 3.2414620825464104 |
| `n_perm_ge_obs` | 0 / 20000 |
| Permutation `p` | 0.00004999750012499375 |
| Verdict | POSITIVE |

## Phase counts and descriptive `z_s`

| Phase | `n` | Mean `z_s` | Median `z_s` |
|---|---:|---:|---:|
| liturgical-opening | 1 | -0.8492700208984997 | -0.8492700208984997 |
| early-Meccan | 48 | -2.9382451321322227 | -3.3510746187458995 |
| early-Meccan/Medinan-disputed | 1 | -1.3238742581275194 | -1.3238742581275194 |
| middle-Meccan | 16 | 1.0157687127250556 | 0.8635184037711192 |
| late-Meccan/middle-Meccan | 1 | 1.4217784419911357 | 1.4217784419911357 |
| late-Meccan | 22 | 4.435757740435351 | 4.611283679323166 |
| late-Meccan/Medinan-border | 1 | 4.295126775757565 | 4.295126775757565 |
| late-Meccan/Medinan-hybrid | 1 | 6.305418732080939 | 6.305418732080939 |
| Medinan-short | 2 | 0.03652975920407553 | 0.03652975920407553 |
| Medinan-long | 21 | 6.817694050675588 | 5.396568259625289 |

## Notes

- The test used the raw locked `z_s` values without residualization or refit.
- Phase labels were read exactly from the locked TSV and shuffled globally only
  for the null.
- The large chronology ladder is clear: `early-Meccan < middle-Meccan <
  late-Meccan < Medinan-long` on both mean and median `z_s`.
- `Medinan-short` is a small exception cell (`n = 2`) and should not be
  treated as representative of the broader Medinan-long block.

## Artifacts

- Prereg: `findings/phase-b-hypotheses/h-new-127-9-phase-structure-prereg.md`
- Script: `scripts/h_new_127_9_oq20_phase_structure.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-9.json`
- Finding: `findings/phase-b-hypotheses/h-new-127-9-phase-structure.md`
