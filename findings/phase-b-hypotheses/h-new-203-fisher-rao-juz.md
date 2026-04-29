---
finding_id: h-new-203
title: "Full 30-juzʾ partition against Fisher-Rao structural geometry"
date: 2026-04-17
seed: 20260419
bonferroni_k: 2
alpha_bon: 0.025
verdict: BOUNDARY-ONLY (PASS-DIRECTED, with SIGN-REVERSAL secondary)
parent_findings: [h-new-111, h-new-127, h-new-130, h-new-64]
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)"
---

# [[h-new-203-fisher-rao-juz|H-NEW-203]] — Classical 30-juzʾ boundaries vs Fisher-Rao structure

## One-line summary

The 29 classical juzʾ-internal boundaries land on significantly high Fisher-Rao windowed-jump positions (**T1 p = 0.0004**, z = +3.12, α_bon = 0.025 → PASS). However, juzʾ SEGMENTS are *less* internally coherent than length-matched random contiguous partitions (**T2 z = +3.56, one-sided-lower p ≈ 1.0** → FAIL with sign reversal). Verdict: **BOUNDARY-ONLY**.

## Primary results

### Test 1 (boundary concentration) — PASS

- T1_obs (sum of windowed FR-jumps at 29 juzʾ cuts) = **23.1015**
- Null (10k random 29-cut samples, uniform over 6235 positions): mean = 21.1010, SD = 0.6403
- z = +3.12, p = 0.0004, α_bon = 0.025 → **PASS**
- Surah-seam-matched null (S2 secondary, 7 seam + 22 intra): p = 0.0005, z = +3.22. Effect survives controlling for seam confound.

### Test 2 (segment coherence) — FAIL with SIGN REVERSAL

- T2_obs (mean verse→segment-centroid FR-distance, canonical juzʾ) = **0.77044**
- Null (10k length-multiset-preserving random partitions): mean = 0.75284, SD = 0.00494
- z = **+3.56**, one-sided-lower p = 0.9999 → **FAIL**
- Sign is REVERSED: juzʾ segments are SYSTEMATICALLY LESS coherent than random contiguous partitions with the same length multiset.

## Interpretation

The 30-juzʾ partition **marks boundaries at genuine Fisher-Rao discontinuities** — but the segments it creates are **less topically coherent than random length-matched partitions would be**. This is geometrically consistent: if you place cuts AT the biggest jumps, the segments you create will straddle the high-variance *before* and *after* windows of those jumps, making them less coherent than cuts placed in uniform regions.

In plain terms: **the juzʾ partition operates as a recitation-balance device that happens to snap to local structural discontinuities when convenient (often at surah starts), but it does NOT prioritize maximally-coherent topical segments**. The signal is at the BOUNDARIES, not within the SEGMENTS.

This is different from what [[h-new-64-juz-boundaries|H-NEW-64]]'s axis test would tell you: [[h-new-64-juz-boundaries|H-NEW-64]] used windowed lexical Jaccard, rhyme-TV, proper-noun asymmetry, length shift — all BOUNDARY-LEVEL statistics. It reported STRONG-PASS. [[h-new-203-fisher-rao-juz|H-NEW-203]] confirms boundary-level structure (via the root-distribution FR metric, a different feature space) AND adds the new finding that segment-level coherence does NOT track the juzʾ partition.

## Sanity checks

- MW-5 scrambled corpus: T1_obs - T1_scramble = +1.48 (2.31 null-SD). Instrument IS discriminative.
- 22 of 29 juzʾ boundaries are *not* surah-aligned; the effect is not driven by surah seams alone (matched-null z = +3.22).

## Top per-boundary Fisher-Rao jumps

The juzʾ cuts ranking in the top decile (percentile ≥ 0.90) of all 6235 cuts, by FR jump size:

| juzʾ | pos | percentile | aligned? | notes |
|---|---|---|---|---|
| 29 | Q67:1 (mulk) | 0.988 | ✓ | start of juzʾ taBāraka — mufaṣṣal shift |
| 3  | Q2:253 | 0.984 | — | last pericope of al-Baqara |
| 15 | Q17:1 (isrāʾ) | 0.961 | ✓ | Meccan narrative pivot |
| 5  | Q4:24 | 0.945 | — | legal/marriage block start |
| 13 | Q12:53 | 0.940 | — | within Yūsuf — confession pivot |
| 7  | Q5:82 | 0.925 | — | within al-Māʾida — Christians-Jews |
| 18 | Q23:1 | 0.925 | ✓ | al-Muʾminūn opens |

The only juzʾ cut in the bottom decile is **juzʾ 30 @ Q78:1** (percentile 0.137). This is striking: juzʾ ʿamma starts at al-Naba' but the windowed root-distribution before (end of al-Mursalāt) and after (start of al-Naba') are SIMILAR — both short eschatological surahs. The classical juzʾ ʿamma is defined by *length-class shift* (mufaṣṣal ultra-short) rather than root-level topic shift.

## Per-juzʾ coherence (secondary S3)

Most-coherent juzʾ: 6 (Q4:148–Q5:81), 3, 5, 28, 2 — mostly short Medinan legal blocks.
Least-coherent juzʾ: 27 (Q51:31–Q57), 30 (al-Naba'–al-Nās), 29 (al-Mulk–al-Mursalāt), 19, 23.

Juzʾ 30 being the LEAST coherent is a significant new observation. Juzʾ ʿamma is the most-memorized part of the Quran; the classical tradition treats it as pedagogically unified. But at the root-distribution level, it sweeps through 37 short surahs of wildly varying vocabulary — it is a COLLECTION of micro-units, not a coherent segment.

## Pre-reg compliance

- Seed 20260419 ✓
- Bonferroni k=2, α_bon = 0.025 ✓
- All parameters (W=20, K=500, α_Dirichlet=0.5, n_perm=10000) locked in pre-reg before run ✓
- Pre-reg SHA-256: `479984febf64ea1a903d1e2a753c2332a2ba2dc0c0fbbc4e45fe86f26e7b7423`
- No forking paths deviated from pre-reg.
- Script: `scripts/h_new_203_juz_fisher_rao.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-203.json`

## Verdict

**BOUNDARY-ONLY (PASS-DIRECTED)**: T1 passes at bonferroni-adjusted α; T2 fails with significant sign reversal (filed as SIGN-REVERSAL-EXPLORATORY for follow-up). The 30-juzʾ partition marks information-geometric discontinuities *at its boundaries* but creates segments that are LESS internally coherent than length-matched random partitions — consistent with the recitation-balance hypothesis augmented by opportunistic alignment to natural breaks, NOT with a segment-coherent partition hypothesis.
