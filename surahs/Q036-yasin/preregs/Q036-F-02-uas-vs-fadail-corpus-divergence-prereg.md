---
finding_id: Q036-F-02
title: "Q 36 in the corpus-wide UAS-vs-fadāʾil divergence cell — comparison to Q 112 al-Ikhlāṣ"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 20260428
n_perm: 10000
bonferroni_k: 1
alpha_raw: 0.05
direction: locked direct comparison
---

# Q036-F-02 — Q 36 in the UAS-vs-fadāʾil-divergence corpus typology, with explicit comparison to Q 112


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

Per [[h-new-860-hadith-architectural-alignment|H-NEW-860]], the corpus exhibits a class of "most-striking divergence" surahs where hadith-fadāʾil tracks high (10/10) but UAS rank tracks low/mid: Q 112 (UAS 109/114, fadāʾil 10/10), Q 67 (UAS 102/114, fadāʾil 10/10), **Q 36** (UAS 35/114, fadāʾil 10/10).

We test:
- (2a) Q 36 sits in the UAS-vs-fadāʾil-divergence cell (UAS rank > 25 + fadāʾil = 10).
- (2b) Q 36's UAS rank is **higher** than Q 112's and Q 67's (less-divergent), placing Q 36 in the **mild-divergence** sub-cell vs Q 112's **extreme-divergence** sub-cell.
- (2c) Among 10/10-fadāʾil surahs (Q 1, 2, 36, 67, 112), Q 36 ranks 4 of 5 by UAS — separating the structural-iʿjāz tier (Q 1 rank 2, Q 2 rank 3) from the meaning-iʿjāz tier (Q 67 rank 102, Q 112 rank 109), with **Q 36 nearer the meaning-iʿjāz tier despite mid-pack UAS**.

## Locked metric

UAS rank from `findings/phase-b-hypotheses/csv/h-new-840.json` `all_uas` table; fadāʾil rubric from `findings/phase-b-hypotheses/csv/h-new-860.json` per-surah rubric.

## Rules-tuple

`(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)` — UAS pipeline already locked at H-NEW-840.

## Direction (LOCKED)

The direction is direct comparison; no permutation null required for the descriptive ranking. The test is whether the H-NEW-860 typology is consistent with Q 36's empirical profile.

## Success criteria

- (2a) Q 36 in the UAS-vs-fadāʾil-divergence cell: **CONFIRMED** if UAS rank > 25 AND fadāʾil = 10.
- (2b) Q 36 UAS-rank-better-than-Q-112-and-Q-67: **CONFIRMED** if Q 36 UAS rank < Q 112 UAS rank AND Q 36 UAS rank < Q 67 UAS rank.
- (2c) Q 36 in the meaning-iʿjāz cluster: **CONFIRMED** if Q 36's nearest fadāʾil-10-peer by FR distance is Q 67 (the corpus's other meaning-iʿjāz long-Meccan), NOT Q 1 or Q 2 (the structural-iʿjāz tier).

## Failure criteria

- (2a) FAILED if Q 36 UAS rank < 25 OR fadāʾil < 10.
- (2b) FAILED if Q 36 UAS rank > Q 112 OR Q 36 UAS rank > Q 67.
- (2c) FAILED if Q 36's nearest fadāʾil-10-peer is Q 1 or Q 2.

## Discriminating cross-check

If (2c) succeeds, the project's dual-iʿjāz typology is empirically supported at the surah-pair level. If (2c) fails (Q 36 nearest to Q 1 or Q 2 by FR), the meaning-iʿjāz cluster does not include Q 36 — Q 36 is then re-classified as structural-iʿjāz-affiliated.

## Output files

- Pre-reg: `preregs/Q036-F-02-uas-vs-fadail-corpus-divergence-prereg.md`
- Script: `scripts/Q036_F_02_uas_vs_fadail_corpus_divergence.py`
- JSON: `csv/Q036-F-02.json`
- Findings: `06-novel-findings.md` Q036-F-02.
