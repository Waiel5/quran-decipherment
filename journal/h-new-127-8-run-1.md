---
finding_id: h-new-127-8
title: "H-NEW-127.8 phase-aware control for the coarse-prefix OQ-20 omnibus"
phase: B
status: NULL (H_obs = 71.078005; p_perm_upper = 0.112694)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-4
pre_reg: findings/phase-b-hypotheses/h-new-127-8-coarse-prefix-phase-aware-control-prereg.md
pre_reg_sha256: 7ab0e799fa04d701e77141782df35d20b975043f1dfd80a6cbcf9e890976afa9
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = coarse_prefix(sinai_genre); control axis = neuwirth_phase; Kruskal-Wallis H on raw z_s; outer null shuffles coarse-prefix labels only within phase blocks, preserving observed coarse-prefix counts inside each phase; 114 surahs)"
verdict: NULL
---

# H-NEW-127.8 - run log

## Command

```bash
python3 scripts/h_new_127_8_oq20_coarse_prefix_phase_control.py
```

## Exact outputs

| Quantity | Value |
|---|---:|
| Surahs | 114 |
| Coarse classes | 18 |
| Phase blocks | 10 |
| Informative phase blocks | 5 |
| Surahs in informative blocks | 109 |
| Observed Kruskal-Wallis `H` | 71.07800475268436 |
| Degrees of freedom | 17 |
| Within-phase null mean `H` | 65.61431664326021 |
| Within-phase null sd `H` | 4.475338665218389 |
| `n_perm_ge_obs` | 2253 / 20000 |
| Permutation `p` | 0.11269436528173592 |
| Verdict | NULL |

## Phase-control notes

- The control used raw locked `z_s`; no residualization or refitting was added.
- Coarse-prefix labels were shuffled only inside each observed `neuwirth_phase`
  block.
- Five phase blocks were informative and five were frozen single-class blocks.
- The control remained substantive because `109 / 114` surahs were inside
  informative blocks.
- The inferential claim failed under this stricter null even though the
  descriptive coarse-prefix stratification from H-NEW-127.4 stayed unchanged.

## Strongest descriptive coarse classes

Top positive mean `z_s` classes:

- `legal`: `n = 13`, mean `z_s = 7.845356744698053`
- `hybrid`: `n = 1`, mean `z_s = 6.305418732080939`
- `scripture`: `n = 15`, mean `z_s = 4.458117593488252`

Top negative mean `z_s` classes:

- `admonition`: `n = 2`, mean `z_s = -5.5014532339616915`
- `prophetic`: `n = 1`, mean `z_s = -3.660324210769529`
- `creedal`: `n = 1`, mean `z_s = -3.50690906346523`

## Artifacts

- Prereg: `findings/phase-b-hypotheses/h-new-127-8-coarse-prefix-phase-aware-control-prereg.md`
- Script: `scripts/h_new_127_8_oq20_coarse_prefix_phase_control.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-8.json`
- Finding: `findings/phase-b-hypotheses/h-new-127-8-coarse-prefix-phase-aware-control.md`
