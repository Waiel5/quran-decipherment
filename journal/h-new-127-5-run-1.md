---
finding_id: h-new-127-5
title: "H-NEW-127.5 coarse-class one-vs-rest localization of locked compression structure"
phase: B
status: NULL (0 familywise-significant coarse classes; best = legal, |Δ| = 7.608650, p_maxT = 0.401280)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-4
pre_reg: findings/phase-b-hypotheses/h-new-127-5-coarse-class-localization-prereg.md
pre_reg_sha256: b124c2d260060c3caa0698441655960f81e74c8734f890d6b740f188731e0f2f
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; coarse label axis = first hyphen-delimited token of sinai_genre; 18 fixed one-vs-rest coarse-class cells; two-sided localization statistic T_c = |mean(z_s in c) - mean(z_s outside c)|; outer label-shuffle null preserves coarse class counts; familywise maxT correction across all 18 cells; 114 surahs)"
verdict: NULL
---

# H-NEW-127.5 - run log

## Command

```bash
python3 scripts/h_new_127_5_oq20_coarse_class_localization.py
```

## Exact outputs

| Quantity | Value |
|---|---:|
| Surahs | 114 |
| Coarse classes | 18 |
| Familywise-significant coarse classes | 0 |
| Familywise-null mean maxT | 7.732622326915629 |
| Familywise-null sd maxT | 2.57387060549878 |
| Familywise-null `q95` | 12.81451653787599 |
| Familywise-null `q99` | 13.722123868712181 |
| Best positive class | legal |
| `legal` mean `z_s` | 7.845356744698053 |
| `legal` one-vs-rest `Δ` | 7.608650012785614 |
| `legal` raw `p` | 0.00004999750012499375 |
| `legal` corrected `p_maxT` | 0.40127993600319983 |
| Best negative class | admonition |
| `admonition` mean `z_s` | -5.5014532339616915 |
| `admonition` one-vs-rest `Δ` | -6.723773984605927 |
| `admonition` raw `p` | 0.04704764761761912 |
| `admonition` corrected `p_maxT` | 0.5643717814109295 |
| Verdict | NULL |

## Notes

- Observable reused exactly from H-NEW-127.4: `z_s = -gzip_z`
- Coarse classes reused exactly from H-NEW-127.4: literal first hyphen-delimited
  token of locked `sinai_genre`
- Localization was preregistered as two-sided one-vs-rest mean differences with
  familywise maxT across all 18 classes
- No coarse class survived corrected inference
- No continuity, handoff, or ledger files were edited

## Artifacts

- Prereg: `findings/phase-b-hypotheses/h-new-127-5-coarse-class-localization-prereg.md`
- Script: `scripts/h_new_127_5_oq20_coarse_class_localization.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-5.json`
- Finding: `findings/phase-b-hypotheses/h-new-127-5-coarse-class-localization.md`
