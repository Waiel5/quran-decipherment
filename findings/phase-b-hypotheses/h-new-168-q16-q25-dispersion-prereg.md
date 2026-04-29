---
id: H-NEW-168
title: Q 16-25 isolate-core on H-NEW-163 dispersion axis — TEMPLATE vs CONCENTRATOR classification
phase: B
status: PRE-REGISTERED
date: 2026-04-17
seed: 20260419
parent: H-NEW-163 (TEMPLATE/CONCENTRATOR compositional-modes via dispersion)
related: H-NEW-94 (Q 16-25 cluster-empty zone NULL-BROKEN on shadow-shape-similarity),
         cross-finding-010 (Q 16, 21, 22, 23, 25 TRUE-ISOLATE-CORE)
bonferroni_k: 1
bonferroni_family: h-new-168-isolate-core-dispersion
alpha_bon: 0.05
direction: "one-sided — isolate-core Q 16-25 window mean-dispersion BELOW median (concentrator-mode)"
rules_tuple: "(no-tashkeel; QAC-STEM morphology-0.4 roots; dispersion_s = mean_{r∈stems(s)} (count_surahs_containing(r)/114); 10-surah contiguous windows; 10,000 permutations)"
---

# [[h-new-168-q16-q25-dispersion|H-NEW-168]] — Q 16-25 dispersion re-investigation

## Motivation

- [[cross-finding-010-extended-network|cross-finding-010]] identified Q 16, 21, 22, 23, 25 as TRUE-ISOLATE-CORE (immune to 20 cluster definitions)
- [[h-new-94-q16-q25-zone|H-NEW-94]] NULL-BROKEN on shadow-shape-similarity (MW-5 failed)
- [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] identified TEMPLATE-MODE (high-dispersion, stems widely shared) vs CONCENTRATOR-MODE (low-dispersion, stems concentrated in self)
- Question: where does the Q 16-25 cluster-empty zone SIT on the dispersion spectrum?

## Pre-committed prediction

**Direction (one-sided, pre-committed)**: If the Q 16-25 zone is isolate-core because its stems are surah-specific (not widely shared with the rest of the corpus), then under [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]]'s framework it should be CONCENTRATOR-MODE — i.e., the 10-surah-window mean dispersion should be **BELOW the corpus median of 10-surah windows**.

Null: window-mean dispersion equals the median of all 105 contiguous 10-surah windows.

## Method

1. Build QAC-STEM root set per surah (replicates [[h-new-155-q1-sui-generis|H-NEW-155]]/163 morphology pipeline).
2. Compute dispersion_s = mean over stems of (count_surahs_containing(stem) / 114) for each of 114 surahs.
3. Extract dispersion + rank for Q 16, 17, 18, 19, 20, 21, 22, 23, 24, 25.
4. Window-mean dispersion for Q 16-25 = mean of the 10 per-surah dispersions.
5. Null: 105 contiguous 10-surah windows across the mushaf; compute window-mean dispersion for each.
6. One-sided p = fraction of null windows with mean-dispersion ≤ Q 16-25 window mean.
7. Decision rule: α_bon = 0.05 (k=1, one-sided). PASS → CONCENTRATOR-MODE CONFIRMED.
8. **Permutation null (secondary)**: 10,000 random 10-surah (non-contiguous) samples for robustness.

## Cells

- **Cell A (primary)**: Q 16-25 window-mean-dispersion percentile vs 105 contiguous-window null; one-sided lower-tail p.
- **Cell B (secondary)**: 10,000-permutation random 10-surah null.
- **Cell C (pairwise internal overlap)**: for each of C(10,2) = 45 pairs in Q 16-25, compute Jaccard(stems_i, stems_j). Compare mean pairwise Jaccard to null of 45 random surah pairs' Jaccard. High → internally-similar (concentrators of shared content). Low → internally-diverse (concentrators of different content).

## MW-5 controls

- **MW-5a (template control, positive)**: Q 1 should appear in top-decile of individual-surah dispersion (expected rank ≤ 12/114 under [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] QAC-STEM; the rougher-stemmer rank was 3/114).
- **MW-5b (concentrator control, positive)**: Q 2 should appear in bottom-decile (expected rank ≥ 103/114 under both stemmers).
- **MW-5c (null calibration)**: Permutation null mean should be ≈ corpus median dispersion; SD > 0.

If MW-5a OR MW-5b fails → INSTRUMENT-BROKEN (pipeline suspect; verdict voided).

## Verdict table

| Cell A | Cell B | Cell C | Interpretation |
|:-:|:-:|:-:|---|
| PASS (p<0.05) | PASS | high Jaccard | concentrator-mode, internally-similar (shared-theme isolate cluster) |
| PASS | PASS | low Jaccard | concentrator-mode, internally-diverse (each surah its own concentrator) |
| PASS | FAIL | — | weakly-concentrator (contiguous-window artifact) |
| FAIL | FAIL | — | NULL — Q 16-25 NOT a concentrator zone on this axis |
| FAIL | PASS | — | NULL-ROBUSTNESS-FAIL — finding is not direction-stable |

## Bonferroni

k = 1 primary Cell A; Cells B, C are secondary / descriptive. α_bon = 0.05.

## Garden-of-forking-paths log

Committed BEFORE running:
- Stemmer: QAC-STEM (same as [[h-new-155-q1-sui-generis|H-NEW-155]], NOT the rougher stemmer [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] used for all-surah ranking). This may move Q 1 rank. [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]]'s own ranking is descriptive — using QAC-STEM here is the PRIMARY-ACCURACY choice.
- Window: exact Q 16-25 (per task spec), ten surahs.
- Null type: both contiguous-window (primary — controls for positional-neighbor artifact) and permutation (secondary — controls for compositional-mode probability).
- Direction: BELOW-median, one-sided. Chosen because isolate-core surahs by definition contain material unique to themselves — should be concentrators.
- Pairwise metric: Jaccard (standard overlap coefficient); could use Overlap-coefficient or raw-intersection — pre-committed to Jaccard for symmetry.
- Alpha: 0.05 one-sided (k=1).
- Tightening: if Cell A p < 0.025, self-tightening Bonferroni applies (no ratification needed per FEEDBACK).
- If result direction REVERSED (Q 16-25 is HIGH-dispersion): report as REFUTES-ISOLATE-CONCENTRATOR (serious finding; indicates isolate-core pattern is NOT about vocabulary concentration, opens new hypothesis).

## Files

- Script: `scripts/h_new_168_q16_q25_dispersion.py`
- Log: `/tmp/h168.log`
- JSON: `findings/phase-b-hypotheses/csv/h-new-168.json`
- Result markdown: `findings/phase-b-hypotheses/h-new-168-q16-q25-dispersion.md`
