---
finding_id: h-new-127-6
title: "H-NEW-127.6 Jurjani-tier bridge for locked per-surah compression z-scores"
phase: B
status: POSITIVE (H_obs = 58.104498; p_perm_upper = 0.000050)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-4
pre_reg: findings/phase-b-hypotheses/h-new-127-6-jurjani-tier-bridge-prereg.md
pre_reg_sha256: 481c43e928dd08686ffd70f8ead7373650742b394a1254ae811377d65499d8d1
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = jurjani_predicted_asyndeton_tier; Kruskal-Wallis H; outer null permutes tier labels across surahs preserving tier counts; 114 surahs)"
verdict: POSITIVE
---

# H-NEW-127.6 - run log

## Command

```bash
python3 scripts/h_new_127_6_oq20_jurjani_tier_bridge.py
```

## Exact outputs

| Quantity | Value |
|---|---:|
| Surahs | 114 |
| Tiers | 3 |
| Observed Kruskal-Wallis `H` | 58.10449819832883 |
| Degrees of freedom | 2 |
| Label-shuffle null mean `H` | 2.0003330416326 |
| Label-shuffle null sd `H` | 1.9403209385747953 |
| `n_perm_ge_obs` | 0 / 20000 |
| Permutation `p` | 0.00004999750012499375 |
| Verdict | POSITIVE |

## Tier counts and descriptive `z_s`

| Tier | `n` | Mean `z_s` | Median `z_s` |
|---|---:|---:|---:|
| HIGH | 65 | -1.759455678114288 | -2.7520198492292254 |
| MED | 32 | 4.161802374983721 | 3.7339558731686533 |
| LOW | 17 | 6.299056510716509 | 5.117084293427459 |

## Notes

- Observable reused exactly from the locked compression artifact:
  `z_s = -gzip_z`
- Label axis reused exactly from the locked TSV:
  `jurjani_predicted_asyndeton_tier`
- No pooling, relabeling, or continuity-file edits were performed

## Artifacts

- Prereg: `findings/phase-b-hypotheses/h-new-127-6-jurjani-tier-bridge-prereg.md`
- Script: `scripts/h_new_127_6_oq20_jurjani_tier_bridge.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-6.json`
- Finding: `findings/phase-b-hypotheses/h-new-127-6-jurjani-tier-bridge.md`
