---
finding_id: h-new-127-3
title: "H-NEW-127.3 class-mapping of locked per-surah compression z-scores"
phase: B
status: POSITIVE (H_obs = 96.669030; p_perm_upper = 0.000050)
date: 2026-04-19
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-2
pre_reg: findings/phase-b-hypotheses/h-new-127-3-compression-class-mapping-prereg.md
pre_reg_sha256: 213bea6290a876a1e786f610b5a07448b26b2e6ec58c83874276bf54c8c2950e
journal: journal/h-new-127-3-run-1.md
seed: 20260419
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = sinai_genre; Kruskal-Wallis H; outer null permutes genre labels across surahs preserving class counts; 114 surahs)"
verdict: POSITIVE
---

# [[h-new-127-3-compression-class-mapping|H-NEW-127.3]] - class-mapping of locked per-surah compression z-scores

## Result

This is the full 114-surah class-mapping follow-up after [[h-new-127-2-oq20-family-rerun|H-NEW-127.2]].
I used the repository-locked per-surah compression scores `z_s = -gzip_z`
from `csv/compression_self_ref_results.json` and the locked `sinai_genre`
column from `neuwirth-sinai-genre-labels.tsv`.

Observed omnibus statistic:

- `H = 96.669030`
- `df = 54`
- label-shuffle null mean `H = 53.974756`
- label-shuffle null sd `H = 6.097342`
- upper-tail permutation p `= 0.0000499975`
- `n_perm_ge_obs = 0 / 20000`
- verdict: **POSITIVE**

## Scope

- 114 surahs were included.
- The exact locked genre taxonomy was used as-is.
- No label pooling was applied.
- The null only shuffled genre labels across surahs while preserving the
  observed class counts.

## Interpretation

The compression scores are not randomly distributed across the locked
genre axis. The omnibus result is strong enough to clear the `0.05`
threshold by a wide margin.

The label set is sparse, with many singleton or near-singleton genres, so
this should be read as an exact label-shuffle finding rather than a claim
that the fine-grained taxonomy is high-power. The permutation result is
still decisive under the preregistered null.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-127-3-compression-class-mapping-prereg.md`
- Script: `scripts/h_new_127_3_oq20_class_mapping.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127-3.json`
- Journal: `journal/h-new-127-3-run-1.md`

## Verdict

**POSITIVE**: the locked per-surah compression z-scores stratify by the
locked `sinai_genre` labels under the label-shuffle Kruskal-Wallis test.

