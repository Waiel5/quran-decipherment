---
finding_id: Q018-F-03
title: "Q 18 alif-monorhyme final-letter dominance + final-verse closure on alif"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 18003
n_perm: 10000
bonferroni_k: 2
alpha_raw: 0.05
alpha_bonferroni: 0.025
direction: positive (Q 18 alif-frac > corpus mean); v.110 ends in alif (point-test)
---

# Q018-F-03 — Q 18 alif-monorhyme final-letter saturation + v.110 alif-closure

## Hypothesis

Q 18 al-Kahf's final-letter distribution is dominated by alif. The pre-registered hypotheses:

- **Cell A (LOCKED)**: Q 18's alif-final-fraction (alif as last letter of verse, after stripping mushaf marks and final-tashkeel-marks) is ≥ 0.95 (95%), and the binomial p-value vs corpus-mean alif-fraction is p < α_Bonferroni = 0.025.
- **Cell B (LOCKED)**: Q 18:110 (the final verse) ends in alif as its last verbatim letter.

This is the verification of the H-NEW-750 reported `top_final_letter_frac = 0.9909` for Q 18. It is also the empirical floor for the project's "100% alif-monorhyme cluster" claim — under the locked rules-tuple Q 18 is 99.09% (109/110), NOT 100%. The single non-alif verse is v. 13 (*hudan*, ending in alif maqṣūra ى, not alif ا).

## Operational definition

For Cell A:
- Read `quran-text/quran-min-tashkeel.json` (minimal-tashkeel — primary substrate for rhyme analysis per protocol).
- For each verse v of Q 18:
  - Strip mushaf marks (regex `[۞۩ۚۖۗۛۧۜ]`).
  - Identify last orthographic word.
  - Strip remaining tashkeel marks from last word.
  - Take the last letter (graphemically).
- Tally alif (ا) vs other letters.
- Compute alif-fraction.

For corpus-mean: compute alif-fraction across all 114 surahs (same procedure).

For Cell B:
- Inspect Q 18:110 last word's last letter directly.

## Null distribution

Cell A: under H0, Q 18's alif-fraction matches corpus-mean alif-fraction. Compute binomial p-value for observed alif-count given n=110 trials and p=corpus-alif-fraction.

Cell B: deterministic (single observation).

## Direction (LOCKED)

- Cell A: alif-fraction > corpus-mean alif-fraction (one-tailed positive).
- Cell B: v.110 last letter == alif (point-prediction).

Pre-commit violation: if Cell A alif-fraction < corpus-mean (i.e., Q 18 has *fewer* alif endings than corpus average), report as NULL.

## Success criteria

- Cell A: p_binomial < α_Bon = 0.025 AND alif-fraction ≥ 0.95: **CONFIRMED Cell A**.
- Cell A: 0.025 < p < 0.05 OR alif-fraction in [0.90, 0.95): **DIRECTIONAL**.
- Cell A: alif-fraction < corpus-mean: NULL with pre-commit-violation flag.
- Cell B: v.110 last letter == alif: **CONFIRMED Cell B**.
- Cell B: v.110 last letter != alif: NULL.

Combined: CONFIRMED if both cells.

## Rules-tuple

`(min-tashkeel, orthographic-word, last-letter-after-strip-mushaf-and-tashkeel, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## Note on the "100% alif-monorhyme cluster" claim

The H-NEW-750 alif-monorhyme cluster `[18, 48, 65, 72, 76, 87, 91, 92]` is described as "100% alif-monorhyme" in some classical sources. Empirically:
- Q 48: 100% alif (29/29 verses).
- Q 65: 91.67% alif (11/12 verses).
- Q 72: 100% alif (28/28 verses).
- Q 76: 100% alif (31/31 verses).
- Q 87: top-letter is **yāʾ** at 94.74%, NOT alif.
- Q 91: 100% alif (15/15 verses).
- Q 92: top-letter is **yāʾ** at 100%, NOT alif.

So the project-internal "8-surah 100% alif-monorhyme cluster" claim is **rules-tuple fragile**: under the H-NEW-750 final-letter convention, only Q 48, 72, 76, 91 are strict 100% alif; Q 18 is 99.09%; Q 65 is 91.67%; Q 87 and Q 92 are *yāʾ*-monorhyme not alif-monorhyme. This is documented in `05-classical-claims-audit.md` Audit 5 and in Q018-F-03's honest limits.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q018_F_03_alif_monorhyme.py`.
- JSON: `csv/Q018-F-03.json`.
- Findings: `06-novel-findings.md` Q018-F-03 section.
