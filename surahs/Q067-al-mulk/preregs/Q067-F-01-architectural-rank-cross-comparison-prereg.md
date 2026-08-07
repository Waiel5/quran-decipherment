---
finding_id: Q067-F-01
title: "Q 67 architectural rank vs. Q 36, Q 112, Q 18 — does grave-protection / heart-of-Quran / thuluth-al-Quran tradition predict empirical UAS?"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 2024
n_perm: 0 (cross-comparison; no permutation null needed)
bonferroni_k: 4
alpha_raw: 0.05
alpha_bonferroni: 1.25e-2
direction: "high recitation-tradition status should NOT predict high UAS — H1 is NULL alignment (the al-Khaṭṭābī iʿjāz al-maʿnā / al-Bāqillānī iʿjāz al-fawāṣil orthogonality prediction)"
---

# Q067-F-01 — Architectural rank cross-comparison


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Hypothesis

The recitation-tradition surahs Q 67 (grave-protection / al-Mānīʿa), Q 36 (heart-of-Quran), Q 112 (thuluth-al-Quran), Q 18 (Friday recitation) collectively occupy a *theological-iʿjāz* cell in the project's UAS architecture: high-faḍāʾil density with **NULL or LOW UAS rank**, in contrast to the *structural-iʿjāz* cell occupied by Q 33, Q 1, Q 2, Q 9 (top-5 UAS).

This is the Wave-D test of the [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] dual-iʿjāz prediction.

## Direction (LOCKED)

The PRE-REGISTERED direction is: **"the four high-recitation-tradition surahs do NOT cluster at the top of UAS rankings; their median UAS rank is below 50 of 114."**

Specifically: median(rank_Q67, rank_Q36, rank_Q112, rank_Q18) > 50 (i.e., bottom-half-or-mid-UAS).

A reversed direction (median rank ≤ 50, i.e., the four surahs cluster in the top-half) would be a NULL on the orthogonality hypothesis and a positive finding for "recitation-tradition predicts UAS."

## Operationalization

For each of the four surahs, fetch UAS rank from `findings/phase-b-hypotheses/csv/h-new-840.json` `all_uas` field. Sort the 114-surah list by UAS descending; the rank of surah X is its position in this sort (1 = highest UAS).

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`

## Success criteria

- median rank > 50 with all 4 ranks > 30: **VINDICATES theological-iʿjāz/architectural-iʿjāz orthogonality**
- median rank ∈ [30, 50]: **DIRECTIONAL** (mixed support)
- median rank < 30: **NULL** (orthogonality prediction violated; recitation-tradition surahs do cluster at top UAS)

## Failure criteria

- if all 4 surahs are in the top decile of UAS, the orthogonality prediction is FALSIFIED (recitation-tradition predicts architectural-rank).

## Output files

- Pre-reg: this file (`preregs/Q067-F-01-architectural-rank-cross-comparison-prereg.md`).
- Script: `scripts/Q067_F_01_architectural_rank_cross_comparison.py`.
- JSON: `csv/Q067-F-01.json`.
- Findings: in `06-novel-findings.md`.
