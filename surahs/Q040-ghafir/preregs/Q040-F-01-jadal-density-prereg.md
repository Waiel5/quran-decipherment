---
prereg_id: Q040-F-01
title: Q 40 *jadal* (dispute) root density vs corpus baseline
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T01:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q040-F-01 — Q 40 *jadal* density

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The frequency of root ج-د-ل (*jadal* / "to dispute") in Q 40, normalized per 1000 words, is **higher** than the corpus mean (excluding Q 40 from the baseline).

## 2. Null

**H0**: Q 40 *jadal*-density is not different from corpus-baseline.

## 3. Operationalization

- Tashkeel level: **no-tashkeel** (per default rules-tuple).
- Root identification: QAC v0.4 root annotations from `data/morphology/quranic-corpus-morphology-0.4.txt`.
- Root: ج-د-ل (Arabic letters: jīm, dāl, lām).
- Per-surah counts: number of QAC tokens with stem-root = ج د ل / total tokens × 1000.
- Test: per-surah z-score against corpus baseline (excluding the surah itself when computing baseline).

## 4. Direction lock

Pre-committed direction: **Q 40 *jadal*-density > corpus mean**.

If observed direction reversed: **NULL with pre-commit violation flag**.

## 5. Bonferroni

This is a single test (k=1); no multiplicity correction needed.

## 6. Success / failure criteria

- **Success (DIRECTIONAL VINDICATION)**: Q 40 z-score > +1.0 (1 SD above baseline).
- **NULL**: Q 40 z-score in [-1.0, +1.0].
- **Pre-commit violation**: Q 40 z-score < -1.0.

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q040-F-01.json` with: surah-Q40 jadal-density, corpus-mean density, SD, z-score, top-5 jadal-densest surahs.

## 9. Notes

The motivation is that Q 40's classical thematic identification (per al-Biqāʿī, *Naẓm al-durar*) is the *jadāl* / disputers theme — the recurring refrain *mā yujādilu fī āyāti llāhi illā…* (Q 40:4, 35, 56). Empirically testing whether root-density matches the classical identification.
