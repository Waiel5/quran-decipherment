---
finding_id: h-new-127-7
title: "H-NEW-127.7 phase-aware control for the Jurjani-tier bridge"
phase: B
status: NULL (H_obs = 58.104498; p_perm_upper = 0.094495)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-6
pre_reg: findings/phase-b-hypotheses/h-new-127-7-jurjani-tier-phase-aware-control-prereg.md
pre_reg_sha256: 9dc8ba8bdc0c3be82c3083f2ec993ad8b982038fcd14ece2857ff688454d7721
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = jurjani_predicted_asyndeton_tier; control axis = neuwirth_phase; Kruskal-Wallis H on raw z_s; outer null shuffles tier labels only within phase blocks, preserving observed tier counts inside each phase; 114 surahs)"
verdict: NULL
---

# H-NEW-127.7 - run log

## Command

```bash
python3 scripts/h_new_127_7_oq20_jurjani_tier_phase_control.py
```

## Exact outputs

| Quantity | Value |
|---|---:|
| Surahs | 114 |
| Tiers | 3 |
| Phase blocks | 10 |
| Informative phase blocks | 5 |
| Observed Kruskal-Wallis `H` | 58.10449819832883 |
| Degrees of freedom | 2 |
| Within-phase null mean `H` | 53.011575118215276 |
| Within-phase null sd `H` | 3.7769254988374317 |
| `n_perm_ge_obs` | 1889 / 20000 |
| Permutation `p` | 0.09449527523623819 |
| Verdict | NULL |

## Tier counts and descriptive `z_s`

| Tier | `n` | Mean `z_s` | Median `z_s` |
|---|---:|---:|---:|
| HIGH | 65 | -1.759455678114288 | -2.7520198492292254 |
| MED | 32 | 4.161802374983721 | 3.7339558731686533 |
| LOW | 17 | 6.299056510716509 | 5.117084293427459 |

## Phase-control notes

- The control used raw locked `z_s`; no residualization or refitting was added.
- Tier labels were shuffled only inside each observed `neuwirth_phase` block.
- Five phase blocks were informative and five were frozen single-tier blocks.
- The inferential claim failed under this stricter null even though the
  descriptive tier ordering stayed monotone `LOW > MED > HIGH`.

## Artifacts

- Prereg: `findings/phase-b-hypotheses/h-new-127-7-jurjani-tier-phase-aware-control-prereg.md`
- Script: `scripts/h_new_127_7_oq20_jurjani_tier_phase_control.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-7.json`
- Finding: `findings/phase-b-hypotheses/h-new-127-7-jurjani-tier-phase-aware-control.md`
