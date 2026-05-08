---
finding_id: Q025-F-04
title: *Qālū / qāla* polemic-quotative density of Q 25 vs corpus
phase: B+
status: PRE-REGISTERED (locked before computation)
date: 2026-05-07
specialist: Q025-al-furqan-specialist
seed: 20260507
n_perm: 10000
bonferroni_family: Q025-F-04-qalu-density
bonferroni_k: 2
alpha_bon: 0.025
direction: one-sided HIGHER — Q 25's *qāla/qālū/yaqūlūna*-density (per-100-verses) places Q 25 in the TOP quartile of the corpus
success_criterion: BOTH cells pass at p ≤ α_bon
rules_tuple: "(no-tashkeel, orthographic-token, regex-graphemic-match, Hafs-Kufan, Mashriqi)"
script: surahs/Q025-al-furqan/scripts/Q025_F_04_qalu_density.py
output_json: surahs/Q025-al-furqan/csv/Q025-F-04.json
---

# Q025-F-04 — *Qālū* polemic density (pre-reg)

## Hypothesis

Q 25:7-9 is a paradigmatic *qālū* polemic block: the disbelievers' objections (*wa-qālū mā li-hādhā al-rasūli yaʾkulu al-ṭaʿāma...*) followed by *unẓur kayfa ḍarabū laka al-amthāl* (the divine refutation). Q 25 returns repeatedly to *qālū* + objection / *qul* + reply structure (vv. 7, 8, 21, 32, 41, 60, 63 etc.).

**Pre-committed direction**: Q 25's per-verse density of inflected *qwl*-root narrating-disbelievers verbs places Q 25 in the TOP quartile (rank ≤ 28/114) of the corpus.

## Two test cells

**Cell A — *qālū* / *qālat* / *qāla* count per 100 verses**: orthographic-token regex matching the surface forms `قال`, `قالت`, `قالوا`, `قلن`, `قلتم`, `قلت` (all perfect-tense *qwl* form-I verbs) **occurring in disbeliever-attribution contexts** (defined operationally as: the regex `(و)?قالوا|قال (الذين كفروا|الظالمون|المشركون)` matched against verse text). Direction: TOP quartile rank.

**Cell A2 — broader *qwl* density**: count of any orthographic token starting with `قال` or `يقول` (the QAC root frq=qwl form-I imperfect/perfect, surface match) per 100 verses, regardless of subject. Direction: TOP quartile rank. 

(Cell A2 is the broader, less-judgment-laden version of A; A is the targeted polemic version. We pre-register both because the targeted cell is operationally fragile but more theoretically meaningful.)

## Bonferroni accounting

k = 2 cells. α_bon = 0.025.

## Acceptance / failure

- BOTH cells pass at p ≤ α_bon (one-sided UPPER) ⇒ **PASS-DIRECTED**.
- 1/2 cells pass ⇒ **DIRECTIONAL**.
- 0/2 ⇒ **NULL**.

## Direction is locked HIGH

Direction: Q 25 in top-quartile. Reversed (Q 25 in bottom-quartile) is a pre-commit violation.

## MW protections

- MW-1 (instrument-prior): the regex pattern is locked above pre-reg lock.
- MW-2 (corpus-prior): permutation null = random shuffles of which surah owns which 100-verse-density value (corpus-prior); one-sided p_upper.
- MW-5 (positive-control): Cell A2 should also place narrative-rich Q 12 Yūsuf (which has ~26 *qāla*-counts per 100v) in the top-decile. If Q 12 is NOT in the top-decile of A2 density, instrument is NULL-BROKEN.
- MW-6 (instrument-control): the broader Cell A2 spans the natural family A is drawn from.
- MW-7 (post-hoc cap): direction was committed before observation.

## Garden-of-forking-paths log

- The Cell-A regex is judgment-driven: not all `قال` are polemic (e.g., narrating Mūsā or Yūsuf speaking in their stories is also `قال`). The Cell-A2 regex is content-blind. Pre-registering both protects against retroactively choosing the more flattering one.
- "Top quartile" is the same definitional threshold as Q025-F-01.

## Files

- Pre-reg: `surahs/Q025-al-furqan/Q025-F-04-qalu-polemic-density-prereg.md`
- Script: `surahs/Q025-al-furqan/scripts/Q025_F_04_qalu_density.py`
- Output: `surahs/Q025-al-furqan/csv/Q025-F-04.json`

*PRE-REG LOCKED 2026-05-07.*
