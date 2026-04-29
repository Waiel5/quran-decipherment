---
id: H-NEW-271-1
title: 1-D mean_manner singleton propagation follow-up to H-NEW-271
phase: B
status: MULTI-DIM-REQUIRED-AT-SINGLETONS
date: 2026-04-19
executed_by: codex
parent_1: H-NEW-271
parent_2: H-NEW-232
open_question: OQ-1 at the singleton layer under 1-D collapse
seed: 20260419
prereg: h-new-271-1-manner-singleton-prereg.md
prereg_sha256: 181ae76964eb29eb9aadeda06ce4fe7108de15c17d83922b68c89099b0c7465f
bonferroni_k: 2
alpha_bon: 0.025
rules_tuple: "(29 canonical muq surahs; locked H-NEW-271 codebook; singleton propagation restricted to mean_manner only; z-scored against the 19 multi-member surahs only; 1-D Euclidean nearest-centroid; nearest multi-member surah reported descriptively; H-NEW-232 accepted-cluster sets reused verbatim; 1000-label-shuffle null on the 19 multi-member surahs; seed 20260419)"
verdict: MULTI-DIM-REQUIRED-AT-SINGLETONS
---

# [[h-new-271-1-manner-singleton|H-NEW-271.1]] - 1-D mean_manner singleton propagation follow-up

## Headline

**MULTI-DIM-REQUIRED-AT-SINGLETONS.**

- The locked [[h-new-271-muq-minimal-phon-family|H-NEW-271]] codebook, collapsed to the single `mean_manner` axis,
  preserves only **5 / 10** singleton matches against the [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] a-priori
  accepted-cluster sets.
- Permutation null: 1000 label shuffles over the 19 multi-member surahs give
  null mean = **3.758** and `p_perm = 0.41` (`410 / 1000` ge-count).
- The 1-D collapse is therefore **not** inferentially stronger than chance
  under the locked shuffle null.
- Compared with [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]], this is a drop from **8 / 10** to **5 / 10**.

## Singleton table

| Singleton | Surah | Nearest multi-surah | Nearest cluster | [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] accepted | Match? |
|---|---:|---:|---|---|---|
| ALMS | 7 | 26 | TSM | {ALM} | NO |
| ALMR | 13 | 40 | HM | {ALM, ALR} | NO |
| KHYAS | 19 | 26 | TSM | {HM, TSM} | YES |
| TH | 20 | 26 | TSM | {TSM} | YES |
| TS | 27 | 26 | TSM | {TSM} | YES |
| YS | 36 | 26 | TSM | {ALM, ALR} | NO |
| S | 38 | 26 | TSM | {TSM} | YES |
| HMASQ | 42 | 26 | TSM | {HM} | NO |
| Q | 50 | 26 | TSM | {HM, TSM} | YES |
| N | 68 | 40 | HM | {ALM, ALR} | NO |

Nearest multi-member surah and nearest centroid cluster coincide for all 10
singletons in this 1-D collapse, so the singleton-layer geometry is simple but
coarse: the issue is not centroid-vs-neighbor ambiguity, it is the loss of
cluster-specific structure under the 1-D reduction.

## Interpretation

The surviving structure is a narrow TSM pull:

- `KHYAS`, `TH`, `TS`, `S`, and `Q` still land on the [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]-accepted side.
- `ALMS`, `ALMR`, `YS`, `HMASQ`, and `N` do not.

That is enough to show some residual ordering in the 1-D axis, but not enough
to preserve the [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] singleton topology. The 1-D collapse keeps a coarse
phonological gradient, yet it loses the finer ALM / ALR / HM discrimination
that made [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] reach 8 / 10.

The null is also not favorable to a strong residual claim. A 5 / 10 hit rate is
only modestly above the shuffle mean of 3.758, and the permutation tail is far
from the Bonferroni bar.

## Honest limit

This follow-up does **not** rescue the singleton layer at the [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] level.
The correct comparison is not "does anything survive at all?" but "does the
collapsed axis still carry the same singleton-layer structure?" The answer here
is no.

## Verdict

**MULTI-DIM-REQUIRED-AT-SINGLETONS**

- `Cell A` fails: 5 / 10 is below the locked nontrivial bar of 6 / 10, and
  `p_perm = 0.41` is not significant.
- `Cell B` fails: 5 / 10 is also below the [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] baseline of 8 / 10.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-271-1-manner-singleton-prereg.md`
- Script: `scripts/h_new_271_1_manner_singleton.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-271-1.json`
- Journal: `journal/h-new-271-1-run-1.md`

