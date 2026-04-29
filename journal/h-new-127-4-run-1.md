---
finding_id: h-new-127-4
title: "H-NEW-127.4 coarse-prefix localization of locked per-surah compression class structure"
phase: B
status: POSITIVE (H_obs = 71.078005; p_perm_upper = 0.000050)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-3
pre_reg: findings/phase-b-hypotheses/h-new-127-4-coarse-prefix-localization-prereg.md
pre_reg_sha256: 78f491f055f8c6fb2efda12bdc335bf3baf3f8e18c2cd1c158afa4779c752ea7
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; coarse label axis = first hyphen-delimited token of sinai_genre; Kruskal-Wallis H; outer null permutes coarse labels across surahs preserving coarse class counts; 114 surahs)"
verdict: POSITIVE
---

# H-NEW-127.4 - run log

## Command

```bash
python3 scripts/h_new_127_4_oq20_coarse_prefix_localization.py
```

## Exact outputs

| Quantity | Value |
|---|---:|
| Surahs | 114 |
| Coarse classes | 18 |
| Observed Kruskal-Wallis `H` | 71.07800475268436 |
| Degrees of freedom | 17 |
| Label-shuffle null mean `H` | 17.029654925287037 |
| Label-shuffle null sd `H` | 4.801648532033274 |
| `n_perm_ge_obs` | 0 / 20000 |
| Permutation `p` | 0.00004999750012499375 |
| Verdict | POSITIVE |

## Notes

- Observable reused exactly from H-NEW-127.3: `z_s = -gzip_z`
- Label axis was coarsened mechanically to the first hyphen-delimited token
  of the locked `sinai_genre` string
- No pooling, relabeling, or continuity-file edits were performed

## Artifacts

- Prereg: `findings/phase-b-hypotheses/h-new-127-4-coarse-prefix-localization-prereg.md`
- Script: `scripts/h_new_127_4_oq20_coarse_prefix_localization.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-4.json`
- Finding: `findings/phase-b-hypotheses/h-new-127-4-coarse-prefix-localization.md`
