---
finding_id: Q067-F-02
title: "Position s=67 post-Hijra-kink — is Q 67 architecturally distinct from pre-kink surahs?"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 2024
n_perm: 0 (descriptive comparison)
bonferroni_k: 1
alpha_raw: 0.05
direction: "Q 67's mean content distance and rhyme entropy track the post-kink law-prediction — i.e., they are TYPICAL for s=67, NOT enhanced"
---

# Q067-F-02 — Post-Hijra-kink distinctness


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

Q 67 sits at s=67, well past the s=50 Hijra-kink ([[h-new-660-compression-tail-gradient|H-NEW-660]], R²=0.986). The compression-tail laws predict for s=67:

- d̄_content(67) ≈ 0.96 − 0.012·17 = **0.756**
- d̄_rhyme(67) ≈ 0.36 + 0.0041·17 = **0.430**

The PRE-REGISTERED hypothesis: **Q 67's empirical d̄_content and rhyme-entropy are within ±2 standard-errors of the law-prediction** (i.e., Q 67 is a typical post-kink surah, NOT architecturally distinct).

This tests the **null prediction** that Q 67's recitation-tradition prominence does NOT translate to a distinctness in architectural metrics.

## Direction (LOCKED)

The pre-registered direction is **NULL**: Q 67 is expected to track the post-kink law-prediction. A positive finding (Q 67 measurably above or below the law-prediction by >2 SE) would be a positive result for "recitation-tradition predicts architectural distinctness."

## Operationalization

- Pull Q 67's mean_content_distance from `h-new-750.json` `per_surah[surah=67]` (already 0.892).
- Pull Q 67's rhyme_entropy_nats (already 0.770).
- Compute the post-kink-law prediction at s=67 (from H-NEW-660 / H-NEW-700).
- Compare the residual.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`

## Success criteria

- residual within ±2 SE of law-prediction: **VINDICATES typicality** (Q 67 NOT architecturally distinct).
- residual >2 SE above prediction: **DIRECTIONAL** (Q 67 architecturally enhanced).
- residual >2 SE below prediction: **DIRECTIONAL** (Q 67 architecturally depleted).

## Output files

- Pre-reg: this file (`preregs/Q067-F-02-postkink-distinctness-prereg.md`).
- Script: `scripts/Q067_F_02_postkink_distinctness.py`.
- JSON: `csv/Q067-F-02.json`.
- Findings: in `06-novel-findings.md`.
