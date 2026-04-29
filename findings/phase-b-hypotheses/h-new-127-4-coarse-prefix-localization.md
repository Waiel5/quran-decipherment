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
journal: journal/h-new-127-4-run-1.md
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; coarse label axis = first hyphen-delimited token of sinai_genre; Kruskal-Wallis H; outer null permutes coarse labels across surahs preserving coarse class counts; 114 surahs)"
verdict: POSITIVE
---

# [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] - coarse-prefix localization of locked per-surah compression class structure

## Result

This bounded follow-up reran the [[h-new-127-3-compression-class-mapping|H-NEW-127.3]] omnibus on the same locked
per-surah compression observable, but with a mechanically coarsened label
axis:

- `z_s = -gzip_z` from `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`
- coarse class = literal first hyphen-delimited token of `sinai_genre`
- no manual pooling beyond that prefix extraction

Observed omnibus statistic:

- `H = 71.07800475268436`
- `df = 17`
- coarse-class null mean `H = 17.029654925287037`
- coarse-class null sd `H = 4.801648532033274`
- `n_perm_ge_obs = 0 / 20000`
- upper-tail permutation `p = 0.00004999750012499375`
- number of coarse classes `= 18`
- verdict: **POSITIVE**

## Interpretation

The [[h-new-127-3-compression-class-mapping|H-NEW-127.3]] class structure does compress to a coarse axis. The
positive full-taxonomy result is not just an artifact of many fine-grained
labels. Even after collapsing each locked `sinai_genre` label to its first
hyphen-delimited token, the compression scores remain sharply stratified
under the preregistered label-shuffle null.

In plain terms: the OQ-20 class-mapping signal survives coarse-prefix
localization rather than collapsing.

## Coarse Class Counts And Descriptive `z_s`

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
| narrative | 18 | 2.845644 | 2.166478 |
| exhortative | 5 | 2.224889 | 2.788437 |
| hymn | 2 | 3.449974 | 3.449974 |
| scripture | 15 | 4.458118 | 4.280898 |
| historical | 3 | 2.235459 | 4.546412 |
| hybrid | 1 | 6.305419 | 6.305419 |
| legal | 13 | 7.845357 | 7.823913 |

## Scope

- All 114 surahs were included.
- The compression scores were not recomputed.
- The only transformation was first-token extraction on the locked
  `sinai_genre` field.
- The null shuffled coarse labels across surahs while preserving the exact
  observed coarse class counts.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-127-4-coarse-prefix-localization-prereg.md`
- Script: `scripts/h_new_127_4_oq20_coarse_prefix_localization.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-4.json`
- Journal: `journal/h-new-127-4-run-1.md`

## Verdict

**POSITIVE**: the [[h-new-127-3-compression-class-mapping|H-NEW-127.3]] OQ-20 class structure compresses to a
mechanically coarsened first-token genre axis rather than depending on the
full fine-grained label inventory.
