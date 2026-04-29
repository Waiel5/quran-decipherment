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
journal: journal/h-new-127-8-run-1.md
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = coarse_prefix(sinai_genre); control axis = neuwirth_phase; Kruskal-Wallis H on raw z_s; outer null shuffles coarse-prefix labels only within phase blocks, preserving observed coarse-prefix counts inside each phase; 114 surahs)"
verdict: NULL
---

# [[h-new-127-8-coarse-prefix-phase-aware-control|H-NEW-127.8]] - phase-aware control for the coarse-prefix OQ-20 omnibus

## Result

This bounded follow-up asked whether the positive [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] coarse-prefix
OQ-20 omnibus survives a chronology-aware null using only locked repository
fields:

- `z_s = -gzip_z` from
  `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`
- coarse class = literal first hyphen-delimited token of `sinai_genre`
- control axis = `neuwirth_phase`
- omnibus test = global Kruskal-Wallis `H` across the 18 coarse-prefix classes
- outer null = shuffle coarse-prefix labels only within each observed phase
  block, preserving the observed coarse-prefix counts inside that phase

Observed controlled omnibus statistic:

- `H = 71.07800475268436`
- `df = 17`
- within-phase coarse-prefix null mean `H = 65.61431664326021`
- within-phase coarse-prefix null sd `H = 4.475338665218389`
- `n_perm_ge_obs = 2253 / 20000`
- upper-tail permutation `p = 0.11269436528173592`
- verdict: **NULL**

## Interpretation

The honest read is that the positive [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] coarse-prefix omnibus does
not survive this stricter phase-aware control. The descriptive coarse-prefix
ordering is unchanged from [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]], but once the null is forced to respect
the observed `neuwirth_phase` composition, the observed omnibus is no longer
unusual enough to clear `alpha = 0.05`.

So the distributed coarse-prefix OQ-20 structure looks substantially
phase-mediated under the locked taxonomy. This does not mean the coarse-prefix
axis is meaningless; it means the earlier unrestricted omnibus is not cleanly
separable from chronology/phase structure by this bounded control.

## Coarse Prefix Counts And Descriptive `z_s`

These descriptives are unchanged from [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]]; the change here is
inferential, not descriptive, because the null is now conditioned on phase.

| Coarse class | `n` | Mean `z_s` | Median `z_s` |
|---|---:|---:|---:|
| admonition | 2 | -5.501453 | -5.501453 |
| address | 3 | -3.403308 | -4.844804 |
| prophetic | 1 | -3.660324 | -3.660324 |
| creedal | 1 | -3.506909 | -3.506909 |
| apotropaic | 2 | -3.404142 | -3.404142 |
| oath | 16 | -3.134281 | -3.305636 |
| eschatological | 15 | -2.592464 | -2.535729 |
| hymnic | 4 | -1.588095 | -1.546167 |
| liturgical | 1 | -0.849270 | -0.849270 |
| polemical | 10 | 0.388717 | -0.604060 |
| tripartite | 2 | 1.158047 | 1.158047 |
| exhortative | 5 | 2.224889 | 2.788437 |
| historical | 3 | 2.235459 | 4.546412 |
| narrative | 18 | 2.845644 | 2.166478 |
| hymn | 2 | 3.449974 | 3.449974 |
| scripture | 15 | 4.458118 | 4.280898 |
| hybrid | 1 | 6.305419 | 6.305419 |
| legal | 13 | 7.845357 | 7.823913 |

## Phase-Control Diagnostics

- Phase blocks: `10`
- Informative phase blocks with at least two coarse classes present: `5`
- Frozen single-class phase blocks: `5`
- Surahs in informative blocks: `109`
- Surahs in frozen blocks: `5`

Informative phase blocks:

| Phase | `n` | Coarse-prefix counts |
|---|---:|---|
| Medinan-long | 21 | exhortative 3, historical 2, legal 13, polemical 3 |
| Medinan-short | 2 | hymnic 1, polemical 1 |
| early-Meccan | 48 | address 3, admonition 2, apotropaic 2, creedal 1, eschatological 12, exhortative 1, historical 1, hymn 2, hymnic 2, oath 15, polemical 6, prophetic 1 |
| late-Meccan | 22 | exhortative 1, narrative 9, scripture 12 |
| middle-Meccan | 16 | eschatological 2, hymnic 1, narrative 8, oath 1, scripture 2, tripartite 2 |

Frozen single-class phase blocks:

| Phase | `n` | Coarse-prefix counts |
|---|---:|---|
| early-Meccan/Medinan-disputed | 1 | eschatological 1 |
| late-Meccan/Medinan-border | 1 | scripture 1 |
| late-Meccan/Medinan-hybrid | 1 | hybrid 1 |
| late-Meccan/middle-Meccan | 1 | narrative 1 |
| liturgical-opening | 1 | liturgical 1 |

This is a substantive control rather than a degenerate one: almost the entire
corpus (`109 / 114` surahs) remains inside informative blocks where label
shuffling can actually occur.

## Scope

- All 114 surahs were included.
- The compression scores were not recomputed.
- The coarse-prefix labels were generated exactly as in [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]].
- The phase labels were read exactly from the locked TSV.
- No relabeling, pooling, or continuity-file edits were performed.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-127-8-coarse-prefix-phase-aware-control-prereg.md`
- Script: `scripts/h_new_127_8_oq20_coarse_prefix_phase_control.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-8.json`
- Journal: `journal/h-new-127-8-run-1.md`

## Verdict

**NULL**: the [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] coarse-prefix OQ-20 omnibus does not remain
significant once the null is constrained to preserve the observed phase
composition.
