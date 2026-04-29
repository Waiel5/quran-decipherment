---
finding_id: h-new-277
run: 1
date: 2026-04-18
specialist: codex
seed: 20260418
prereg_sha256: e129780c4794e5bc4a017ec35a812cbea2775666719b4b8b93383a97aacff101
---

# H-NEW-277 run 1 journal

## Goal

Run a mechanistic child test of H-NEW-267:

**Does the Late-Meccan -> Medinan lexical frontier survive after
removing the five broadest mass-shift roots from the root space?**

## Scope kept tight

I only touched the five owned files:

- `findings/phase-b-hypotheses/h-new-277-hijra-frontier-broad-root-ablation-prereg.md`
- `scripts/h_new_277_hijra_frontier_broad_root_ablation.py`
- `findings/phase-b-hypotheses/csv/h-new-277.json`
- `findings/phase-b-hypotheses/h-new-277-hijra-frontier-broad-root-ablation.md`
- `journal/h-new-277-run-1.md`

No unrelated files were edited.

## Locked design

- Parent instrument: exact H-NEW-267 scorer, split rule, and null logic
- Frozen excluded roots:
  `Alh`, `Amn`, `qwl`, `rbb`, `Ayy`
- Primary family:
  train A -> test B AUC, train B -> test A AUC, split-weight rho
- Primary null:
  3000 label shuffles on the Late-Meccan/Medinan pool
- MW-5:
  same ablated root space on the broader Meccan-vs-Medinan split
- Bonferroni family:
  `k = 3`, `alpha_bon = 0.0166667`

## Execution

1. Read the H-NEW-267 script and JSON to freeze the child design.
2. Wrote the prereg first.
3. Implemented the ablated-root variant of the parent script.
4. Ran the production script once from repo root.
5. Read the JSON and wrote the finding and this journal.

Command:

```bash
python3 scripts/h_new_277_hijra_frontier_broad_root_ablation.py
```

The production run completed cleanly on the first pass.

## Result

**PASS-DIRECTED.**

### Primary family

| Cell | Observed | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---|
| Train A -> test B AUC | **1.000000** | 0.700000 | **0.000333** | **PASS** |
| Train B -> test A AUC | **1.000000** | 0.696970 | **0.000333** | **PASS** |
| Split-weight rho | **0.452289** | 0.103089 | **0.000333** | **PASS** |

### MW-5

| Cell | Observed | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---|
| Train A -> test B AUC | **0.897010** | 0.659551 | **0.000999** | PASS |
| Train B -> test A AUC | **0.855482** | 0.667774 | **0.000999** | PASS |
| Split-weight rho | **0.509789** | 0.092749 | **0.000999** | PASS |

## Key comparison to parent

- H-NEW-267 rho: `0.457673`
- H-NEW-277 rho: `0.452289`
- support roots: `434 -> 429`
- held-out gaps:
  `0.105421 -> 0.072133` and `0.090290 -> 0.083068`

The margin shrank somewhat, but the inferential conclusion did not.

## Interpretation kept tight

This run does not say those five roots are unimportant.

It says something narrower:

**the Hijra lexical frontier remains fully recoverable after removing the
five broadest mass-shift roots, so the parent result is not reducible to
those roots alone.**

## Files landed

- Pre-reg: `findings/phase-b-hypotheses/h-new-277-hijra-frontier-broad-root-ablation-prereg.md`
- Script: `scripts/h_new_277_hijra_frontier_broad_root_ablation.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-277.json`
- Findings: `findings/phase-b-hypotheses/h-new-277-hijra-frontier-broad-root-ablation.md`
- Journal: this file
