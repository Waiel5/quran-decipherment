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
journal: journal/h-new-127-7-run-1.md
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = jurjani_predicted_asyndeton_tier; control axis = neuwirth_phase; Kruskal-Wallis H on raw z_s; outer null shuffles tier labels only within phase blocks, preserving observed tier counts inside each phase; 114 surahs)"
verdict: NULL
---

# [[h-new-127-7-jurjani-tier-phase-aware-control|H-NEW-127.7]] - phase-aware control for the Jurjani-tier bridge

## Result

This bounded follow-up asked whether the positive [[h-new-127-6-jurjani-tier-bridge|H-NEW-127.6]] Jurjani-tier
bridge survives a chronology-aware control using only locked repository fields:

- `z_s = -gzip_z` from `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`
- tier axis = `jurjani_predicted_asyndeton_tier`
- control axis = `neuwirth_phase`
- omnibus test = global Kruskal-Wallis `H` across the three tier groups
- outer null = shuffle tier labels only within each phase block, preserving the
  observed tier counts inside that phase

Observed controlled omnibus statistic:

- `H = 58.10449819832883`
- `df = 2`
- within-phase tier-shuffle null mean `H = 53.011575118215276`
- within-phase tier-shuffle null sd `H = 3.7769254988374317`
- `n_perm_ge_obs = 1889 / 20000`
- upper-tail permutation `p = 0.09449527523623819`
- verdict: **NULL**

## Interpretation

The honest read is that the positive [[h-new-127-6-jurjani-tier-bridge|H-NEW-127.6]] Jurjani-tier bridge does not
survive this stricter phase-aware control. The raw tier ordering remains the
same as before, but once the null is forced to respect the observed
`neuwirth_phase` composition, the omnibus no longer clears `alpha = 0.05`.

So the bridge is at least substantially phase-mediated under the locked
taxonomy. This does not prove the tier field is meaningless; it shows that the
earlier positive signal is not cleanly separable from chronology/phase
structure by this bounded control.

## Tier Counts And Descriptive `z_s`

| Tier | `n` | Mean `z_s` | Median `z_s` |
|---|---:|---:|---:|
| HIGH | 65 | -1.759456 | -2.752020 |
| MED | 32 | 4.161802 | 3.733956 |
| LOW | 17 | 6.299057 | 5.117084 |

These descriptives are unchanged from [[h-new-127-6-jurjani-tier-bridge|H-NEW-127.6]]; the change is inferential,
not descriptive, because the null is now conditioned on phase.

## Phase-Control Diagnostics

- Phase blocks: `10`
- Informative phase blocks with at least two tiers present: `5`
- Frozen single-tier phase blocks: `5`
- Surahs in informative blocks: `109`
- Surahs in frozen blocks: `5`

Informative phase blocks:

| Phase | `n` | Tier counts |
|---|---:|---|
| Medinan-long | 21 | LOW 15, MED 6 |
| Medinan-short | 2 | LOW 1, MED 1 |
| early-Meccan | 48 | HIGH 46, MED 2 |
| late-Meccan | 22 | HIGH 4, LOW 1, MED 17 |
| middle-Meccan | 16 | HIGH 13, MED 3 |

Frozen single-tier phase blocks:

| Phase | `n` | Tier counts |
|---|---:|---|
| early-Meccan/Medinan-disputed | 1 | HIGH 1 |
| late-Meccan/Medinan-border | 1 | MED 1 |
| late-Meccan/Medinan-hybrid | 1 | MED 1 |
| late-Meccan/middle-Meccan | 1 | MED 1 |
| liturgical-opening | 1 | HIGH 1 |

## Scope

- All 114 surahs were included.
- The compression scores were not recomputed.
- The tier and phase labels were read exactly from the locked TSV.
- No relabeling, pooling, or continuity-file edits were performed.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-127-7-jurjani-tier-phase-aware-control-prereg.md`
- Script: `scripts/h_new_127_7_oq20_jurjani_tier_phase_control.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-7.json`
- Journal: `journal/h-new-127-7-run-1.md`

## Verdict

**NULL**: the [[h-new-127-6-jurjani-tier-bridge|H-NEW-127.6]] Jurjani-tier bridge does not remain significant once
the null is constrained to preserve the observed phase composition.
