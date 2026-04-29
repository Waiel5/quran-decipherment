---
finding_id: Q067-F-03
title: "Q 67:1, Q 67:3-4 — corpus-singleton phrase signature audit"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 2024
n_perm: 0 (exact-match corpus search)
bonferroni_k: 3
alpha_raw: 0.05
alpha_bonferroni: 1.67e-2
direction: "POSITIVE — Q 67:1 *bi-yadihi al-mulk* and Q 67:3 *fa-rjiʿi al-baṣar* are corpus-singletons; Q 67:3 *sabʿa samāwātin ṭibāqan* is a corpus-pair (with Q 71:15)"
---

# Q067-F-03 — Corpus-singleton phrase signature

## Hypothesis

Three Q 67 phrases identified by classical exegetical literature as distinctive should empirically prove to be:
- **direction A**: *بيده الملك* (bi-yadihi al-mulk) is a corpus-singleton (1 occurrence at Q 67:1).
- **direction B**: *فارجع البصر* (fa-rjiʿi al-baṣar with fāʾ-prefix) is a corpus-singleton at Q 67:3.
- **direction C**: *سبع سماوات طباقا* (sabʿa samāwātin ṭibāqan) is a corpus-pair (Q 67:3 + Q 71:15).

## Direction (LOCKED)

All three directions are POSITIVE — the phrases ARE expected to have low corpus-frequency. A NULL would be: any of the three has more than the predicted occurrences.

## Operationalization

Substring search across all 6,236 verses of `quran-text/quran-no-tashkeel.json`:
- count occurrences of *بيده الملك*
- count occurrences of *فارجع البصر*
- count occurrences of *سبع سماوات طباقا*

## Rules-tuple (LOCKED)

`(no-tashkeel, orthographic-token, exact substring match, basmala-not-counted-in-Q67, Hafs-Kufan, mushaf-order)`

## Success criteria

| Direction | Predicted occurrences | Verdict if matched |
|:--|:--|:--|
| A: *bi-yadihi al-mulk* | exactly 1 (Q 67:1) | **CONFIRMED** |
| B: *fa-rjiʿi al-baṣar* | exactly 1 (Q 67:3) | **CONFIRMED** |
| C: *sabʿa samāwātin ṭibāqan* | exactly 2 (Q 67:3, Q 71:15) | **CONFIRMED** |

## Failure criteria

- A or B occurs >1: NULL on uniqueness claim.
- C occurs ≠ 2: NULL on corpus-pair claim.

## Output files

- Pre-reg: this file (`preregs/Q067-F-03-corpus-singleton-phrases-prereg.md`).
- Script: `scripts/Q067_F_03_corpus_singleton_phrases.py`.
- JSON: `csv/Q067-F-03.json`.
- Findings: in `06-novel-findings.md`.
