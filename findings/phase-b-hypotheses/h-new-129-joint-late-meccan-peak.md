---
id: H-NEW-129
title: Formal joint Late-Meccan peak across the 5 Pattern-B axes
phase: B
status: NULL-BROKEN (observed 5/5 Late-Meccan peak; primary p=0.0226 > 0.01; MW-5 failed)
prereg: h-new-129-joint-late-meccan-peak-prereg.md
script: scripts/h_new_129_joint_late_meccan_peak.py
json: findings/phase-b-hypotheses/csv/h-new-129.json
date: 2026-04-18
agent: specialist-a
seed: 20260418
n_perm: 10000
bonferroni_family: h-new-129-joint-late-meccan-peak
bonferroni_k: 1
alpha_bon: 0.01
rules_tuple: "(H-NEW-125 per-surah axis values only; 4 locked Nöldeke phases; exact 5-of-5 unique-max joint-hit; 10K phase-label permutations)"
---

# [[h-new-129-joint-late-meccan-peak|H-NEW-129]] — Formal joint Late-Meccan peak across the 5 Pattern-B axes

## Headline

- **Observed pattern**: all 5 locked Pattern-B axes do have their
  unique 4-phase maximum at **Late Meccan**.
- **Primary inferential result**: **NULL** at the preregistered
  threshold. Under the exact 5-of-5 phase-label permutation null,
  `p = 0.0226` (225 of 10,000 permutations also hit 5 of 5), which
  does **not** pass `alpha_bon = 0.01`.
- **MW-5 positive control**: **FAIL**. The known Pattern-A bundle also
  shows observed `5/5` unique maxima at **Medinan**, but the same
  permutation instrument gives `p = 0.0599` (598 of 10,000).
- **Verdict**: **NULL-BROKEN**. Per MW-5, the exact-hit 4-phase test
  cannot be promoted as a valid inferential anchor.

## Result table

| Bundle | Target phase | Observed target-phase peaks | Permutation hits | p one-sided | Pass at 0.01? |
|---|---|---:|---:|---:|:---:|
| Primary Pattern-B (`qul`, `book-ref`, `eschatology`, `muq-cardinality`, `loanwords`) | Late Meccan | **5 / 5** | 225 / 10,000 | **0.0226** | **NO** |
| MW-5 Pattern-A (`Allah`, `legal`, `pronoun`, `mean verse length`, `divine names`) | Medinan | **5 / 5** | 598 / 10,000 | **0.0599** | **NO** |

The naive equal-phase independence reference `1 / 4^5 = 0.00098` is
not the inferential basis and badly understates the empirical null.
Under the actual phase-label permutation, exact 5-of-5 target-phase
hits are much more common.

## Primary observed phase means

| Axis | Early Meccan | Middle Meccan | Late Meccan | Medinan | Unique peak |
|---|---:|---:|---:|---:|---|
| `qul_density` | 1.74 | 4.89 | **8.95** | 4.93 | Late Meccan |
| `book_reference_density` | 3.77 | 11.85 | **26.36** | 18.92 | Late Meccan |
| `eschatological_density` | 6.85 | 17.93 | **31.24** | 28.54 | Late Meccan |
| `muq_cardinality` | 0.02 | 1.10 | **2.29** | 0.25 | Late Meccan |
| `loanword_density` | 33.34 | 75.07 | **135.47** | 130.32 | Late Meccan |

So the descriptive [[h-new-125-chronology-content|H-NEW-125]] Pattern-B statement remains true at the
coarse 4-phase level: all 5 axes peak in Late Meccan.

## Why the verdict is NULL-BROKEN

The problem is **not** that the observed pattern vanished. The problem
is that the chosen statistic is too blunt:

1. It reduces each axis to a binary question: "is the unique maximum
   in the target phase?"
2. It throws away magnitude information. For example, `loanword_density`
   is only slightly higher in Late Meccan than Medinan
   (`135.47` vs `130.32`), and `eschatological_density` is also fairly
   close (`31.24` vs `28.54`).
3. Under phase-label permutation, exact 5-of-5 target-phase hits occur
   often enough that the known MW-5 positive-control bundle does **not**
   clear `p < 0.01`.

Per project discipline, MW-5 failure means the instrument is not
trustworthy for inferential promotion here. This is the same general
failure mode seen in `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]` Cell B: an intuitively
reasonable peak-location statistic can be too permissive under the
actual null once chronology structure and unequal phase sizes are
respected.

## What [[h-new-129-joint-late-meccan-peak|H-NEW-129]] does and does not say

What it does say:

- The 5 Pattern-B axes still show a descriptive **5/5 Late-Meccan**
  co-peak at the original [[h-new-125-chronology-content|H-NEW-125]] 4-phase resolution.
- That exact-hit fact is **not** rare enough under this preregistered
  permutation instrument to count as a formal inferential win.

What it does not say:

- It does **not** overturn [[h-new-125-chronology-content|H-NEW-125]]'s marginal axis results.
- It does **not** overturn `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]`, whose stronger evidence
  came from sub-bin concordance statistics rather than this binary
  exact-hit criterion.
- It does **not** imply the 5 axes covary within Late Meccan; [[h-new-141-pattern-b-within-late-meccan|H-NEW-141]]
  already found that they do not.

## Honest limits

1. The axis bundle was selected from **already-known [[h-new-125-chronology-content|H-NEW-125]]**
   results. Even a pass here would have had a ceiling of
   `PASS-DIRECTED`, not CONFIRMED.
2. The test uses only the **coarse 4-phase** schema. It cannot resolve
   the B6/B7 staircase seen in `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]`.
3. The exact-hit statistic discards margin information and is therefore
   a weak summary of the underlying chronology structure.
4. The permutation null keeps the [[h-new-125-chronology-content|H-NEW-125]] chronology fixed and does
   not test alternate chronologies.

## Bottom line

**[[h-new-129-joint-late-meccan-peak|H-NEW-129]] lands as NULL-BROKEN.** The observed Pattern-B bundle is
still descriptively `5/5` Late-Meccan at four-phase resolution, but
the preregistered exact-hit permutation test fails its own MW-5
positive control and therefore cannot serve as the formal joint anchor
originally hoped for.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-129-joint-late-meccan-peak-prereg.md`
- Script: `scripts/h_new_129_joint_late_meccan_peak.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-129.json`
- Journal: `journal/h-new-129-run-1.md`
