---
id: H-NEW-274
run: 1
date: 2026-04-18
agent: codex
verdict: PASS-HOLDOUT-STRONGER
---

# H-NEW-274 run 1 — journal

## Goal

Take the empirical-vs-classical reassignment question flagged by H-NEW-232,
H-NEW-252, and H-NEW-165.2, but keep the scope aggressively bounded.

The narrow task was:

**Does replacing only the two disputed classical accepted-cluster entries
(`YS`, `HMASQ`) with their empirical nearest-cluster assignments produce a
materially stronger singleton-layer account on locked holdout spaces?**

No broader cluster-table family search was included.

## Locked setup used

- discovery source only: `findings/phase-b-hypotheses/csv/h-new-232.json`
- empirical replacements derived only from discovery:
  - `YS -> HM`
  - `HMASQ -> TSM`
- holdout spaces only:
  - `h-new-252.json -> joint_results`
  - `h-new-165-2.json -> watson_modern_voice`
  - `h-new-165-2.json -> strict_pharyngeal_split`
  - `h-new-165-2.json -> holes_glottal_ha_ayn`
- primary test:
  exact one-sided binomial on discordant singleton-space cells
- materiality rule:
  `delta >= 6`, `worsened = 0`, `p < 0.025`

## Work performed

1. Read the parent artifacts and confirmed the repeated disagreement pattern:
   `YS -> HM`, `HMASQ -> TSM`.
2. Wrote a prereg that locked a strict discovery/holdout split and banned
   alternate replacement-table families.
3. Implemented `scripts/h_new_274_empirical_vs_classical_singleton_reassignment.py`.
4. Ran the script once.
5. Used the landed JSON to write the findings note and this journal.

Command used:

```bash
python3 scripts/h_new_274_empirical_vs_classical_singleton_reassignment.py
```

## Result

The first-pass bounded test was already decisive.

- holdout classical = **32/40**
- holdout empirical = **40/40**
- delta = **+8**
- discordant cells = **8**
- improved = **8**
- worsened = **0**
- exact one-sided `p = 0.00390625`
- verdict = **PASS-HOLDOUT-STRONGER**

Per holdout space:

| Space | Classical | Empirical | Delta |
|---|---:|---:|---:|
| H-NEW-252 joint | 8/10 | 10/10 | +2 |
| H-NEW-165.2 Watson | 8/10 | 10/10 | +2 |
| H-NEW-165.2 strict pharyngeal | 8/10 | 10/10 | +2 |
| H-NEW-165.2 Holes glottal | 8/10 | 10/10 | +2 |

Distance margins also stayed positive in every holdout:

- `YS` empirical-over-classical mean margin = **1.2025**
- `HMASQ` empirical-over-classical mean margin = **2.7064**

## Interpretation kept tight

This run does not claim that a wide empirical rewrite of the singleton table has
been proven. It claims something narrower:

**for the exact two disputed rows that kept recurring across parent findings,
the empirical replacement table beats the inherited classical table cleanly on
the locked holdout geometries.**

That was enough for a clean first pass, so I stopped there.

## Files landed

- Pre-reg: `findings/phase-b-hypotheses/h-new-274-empirical-vs-classical-singleton-reassignment-prereg.md`
- Script: `scripts/h_new_274_empirical_vs_classical_singleton_reassignment.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-274.json`
- Findings: `findings/phase-b-hypotheses/h-new-274-empirical-vs-classical-singleton-reassignment.md`
- Journal: this file
