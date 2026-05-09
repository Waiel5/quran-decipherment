---
finding_id: Q049-F-03
H-NEW: H-NEW-1262
title: "Q 49→Q 50 universal-hinge confirmation across 4 orthogonal feature spaces (roots, char-4-gram, verse-length, Nöldeke-chronology gap)"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: 0 (corpus enumeration; cross-tabulating per-pair status across 4 feature spaces)
bonferroni_k: 1
bonferroni_family: Q049-F-03-cross-feature
alpha_raw: 0.05
alpha_bon: 0.05
direction: "POSITIVE — Q 49→Q 50 is hypothesized to be a member of the universal-hinge set in ALL FOUR independently-constructed top-15 lists."
rules_tuple: "(QAC-v0.4-roots+char-4-gram+verse-length+Nöldeke-chronology, no-tashkeel, orthographic-token, Hafs-Kufan, mushaf-order, top15 inclusion test)"
---

# Q049-F-03 — Q 49 → Q 50 universal-hinge cross-feature confirmation

## Hypothesis (LOCKED)

The mushaf-order transition Q 49 al-Ḥujurāt → Q 50 Qāf is conjectured to be one of the THREE universal hinges of the Quran (per H-NEW-130, H-NEW-130b, H-NEW-130c, H-NEW-142): the others are Q 14→Q 15 and Q 56→Q 57. A "universal hinge" is a mushaf-order pair (i, i+1) that simultaneously appears in:

1. The top-15 largest **root-distribution Fisher-Rao jumps** (H-NEW-130).
2. The top-15 largest **char-4-gram Fisher-Rao jumps** (H-NEW-130b).
3. The top-15 largest **verse-length-distribution gaps** (H-NEW-130c).

A 4th feature, *Nöldeke-chronology jump magnitude* (H-NEW-142), gives the absolute size of the chronology-reversal at this transition and provides cross-validation.

The test: Q 49→Q 50 is in `in_all_three=True` per H-NEW-130c; its absolute Nöldeke-chronology gap should be ≥ the median of the 113 mushaf-pairs.

## Direction (LOCKED)

POSITIVE — Q 49→Q 50 is hypothesized to be a member of the **all-three-feature-spaces intersection** AND have a Nöldeke-chronology gap of magnitude ≥ 50 positions (vs corpus median ~13).

## Operationalization

1. Load H-NEW-130 (`top15_largest_jumps`), H-NEW-130b (`top15_largest_jumps`), H-NEW-130c (`top15_largest_jumps`) from `findings/phase-b-hypotheses/csv/`.
2. Cross-check Q 49→Q 50 (i=49, j=50) inclusion in each.
3. Read the H-NEW-130c entry for {49,50} `in_all_three` field.
4. Compute Nöldeke-chronology gap for Q 49→Q 50 from the canonical mapping (Nöldeke ranks per al-Suyūṭī/Nöldeke 1860 sequence).

## Pre-committed reference for Nöldeke

Standard Nöldeke 1860 chronological-rank list (al-Suyūṭī *Itqān* nawʿ 1 + Nöldeke *Geschichte des Qorāns*):
- Q 49 al-Ḥujurāt: Nöldeke rank ≈ 106 (Medinan late phase).
- Q 50 Qāf: Nöldeke rank ≈ 34 (mid-Meccan, "second Meccan period" per Nöldeke 1860).

Gap magnitude = |106 - 34| = 72 positions.

## Rules-tuple (LOCKED)

`(QAC-v0.4-roots-from-h-new-111, char-4-gram-from-h-new-111b, verse-length-from-h-new-130c, Nöldeke-chronology-from-canonical, no-tashkeel, mushaf-order)`

## Success criteria (LOCKED)

| Metric | Predicted | Verdict |
|:--|:--|:--|
| Q 49→Q 50 in H-NEW-130 top-15 (root) | YES | (necessary) |
| Q 49→Q 50 in H-NEW-130b top-15 (char-4) | YES | (necessary) |
| Q 49→Q 50 in H-NEW-130c top-15 (verse-len) | YES | (necessary) |
| All three above met | YES | PASS-PRIMARY |
| Nöldeke-chronology gap ≥ 50 positions | YES | PASS-SECONDARY |
| Both PASS | YES | **CONFIRMED-CROSS-FEATURE** |
| Primary fails any of 3 | YES | NULL-PRIMARY |

## Honesty disclosures

- Q 49→Q 50 universal-hinge status was previously identified by H-NEW-130c (`in_all_three=True`). This pre-reg formalizes the cross-feature confirmation at the surah-specialist level and adds the Nöldeke-chronology gap quantification.
- The test is essentially a CROSS-VALIDATION of an already-confirmed finding at the macro level (mushaf-architecture). Verdict ceiling = CONFIRMED (because the test is a pure cross-tabulation against pre-existing macro-level findings, not a novel statistical test).
- Q 49→Q 50 in cross-finding-013 ring-topology context: Q 49 is the LAST major Medinan-period surah before the back-Meccan surahs Q 50-77; the hinge is the Medinan→back-Meccan transition.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q049_F_03_q49_q50_hinge.py`.
- JSON: `csv/Q049-F-03.json`.
- Findings: `06-novel-findings.md` §Q049-F-03.
