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
journal: journal/h-new-127-6-run-1.md
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = jurjani_predicted_asyndeton_tier; Kruskal-Wallis H; outer null permutes tier labels across surahs preserving tier counts; 114 surahs)"
verdict: POSITIVE
---

# [[h-new-127-6-jurjani-tier-bridge|H-NEW-127.6]] - Jurjani-tier bridge for locked per-surah compression z-scores

## Result

This bounded follow-up tested whether the locked three-tier
`jurjani_predicted_asyndeton_tier` field stratifies the already-locked OQ-20
compression observable:

- `z_s = -gzip_z` from `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`
- tier axis = `jurjani_predicted_asyndeton_tier` from
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`
- omnibus test = Kruskal-Wallis `H`
- outer null = label shuffle preserving the observed tier counts

Observed omnibus statistic:

- `H = 58.10449819832883`
- `df = 2`
- tier-shuffle null mean `H = 2.0003330416326`
- tier-shuffle null sd `H = 1.9403209385747953`
- `n_perm_ge_obs = 0 / 20000`
- upper-tail permutation `p = 0.00004999750012499375`
- verdict: **POSITIVE**

## Interpretation

The OQ-20 compression observable aligns strongly with the locked Jurjani-tier
bridge. The stratification is not marginal and it is directionally ordered:

- `LOW` tier is the most compressible
- `MED` tier is intermediate
- `HIGH` tier is the least compressible

That monotone `LOW > MED > HIGH` pattern holds on both mean and median `z_s`.
So the earlier OQ-20 class structure does not collapse when projected onto this
three-level classical bridge.

The interpretive caution is narrow but important: the tier field is a locked
bridge encoded in the TSV, not a direct Neuwirth/Sinai source variable. The
result therefore supports alignment with that classical-scholar asyndeton
mapping, not an independent historical proof of the mapping itself.

## Tier Counts And Descriptive `z_s`

| Tier | `n` | Mean `z_s` | Median `z_s` |
|---|---:|---:|---:|
| HIGH | 65 | -1.759456 | -2.752020 |
| MED | 32 | 4.161802 | 3.733956 |
| LOW | 17 | 6.299057 | 5.117084 |

## Scope

- All 114 surahs were included.
- The compression scores were not recomputed.
- The tier labels were read exactly from the locked TSV.
- No relabeling, pooling, or continuity-file edits were performed.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-127-6-jurjani-tier-bridge-prereg.md`
- Script: `scripts/h_new_127_6_oq20_jurjani_tier_bridge.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-6.json`
- Journal: `journal/h-new-127-6-run-1.md`

## Verdict

**POSITIVE**: the locked OQ-20 compression observable stratifies sharply by the
locked `jurjani_predicted_asyndeton_tier` axis, with a monotone
`LOW > MED > HIGH` ordering in compressibility.
