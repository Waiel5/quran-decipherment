---
finding_id: Q024-F-02
title: "Q 24:35 (Light-verse) vs Q 2:255 (Throne-verse) empirical comparison"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 2024
n_perm: 0  # exact comparison, no permutation
direction: descriptive (no direction-of-effect locked)
---

# Q024-F-02 — Q 24:35 vs Q 2:255 empirical comparison

## Hypothesis

The two classical "great verses" (āyat al-nūr at Q 24:35, āyat al-kursī at Q 2:255) differ measurably on (i) light-cluster lexicon density (HYPOTHESIS: Q 24:35 has substantially more light-cluster), (ii) Allāh-density (DESCRIPTIVE comparison; both are Allāh-dense), (iii) divine-attribute density (HYPOTHESIS: Q 2:255 has more *attribute* lexicon: al-Ḥayy, al-Qayyūm, al-ʿAlī, al-ʿAẓīm), (iv) word/letter count, (v) structural position within their parent surahs (HYPOTHESIS: Q 24:35 is at the structural midpoint of Q 24, Q 2:255 is NOT at the structural midpoint of Q 2).

## Rules-tuple

`(no-tashkeel, QAC-stem-roots, no-tashkeel-orthographic for word-counts, basmala-counted-only-in-Q1, Hafs-Kufan)`

## Direction-locked claims

- **Direction A**: Q 24:35 light-cluster count > Q 2:255 light-cluster count.  
  Pre-registered: Q 24:35 expected 14+ light-cluster tokens; Q 2:255 expected 0.
- **Direction B**: Q 24:35 word-position-in-surah ratio (mid-point-of-verse / total-words-of-surah) is closer to 0.5 than Q 2:255's.  
  Pre-registered: |Q24:35 ratio − 0.5| < |Q2:255 ratio − 0.5|.

## Descriptive (no direction)

- Allāh count per verse.
- Distinct roots per verse.
- Word count of each verse.
- Letter count of each verse.
- Lexical overlap (shared roots).

## Success criteria

- **Direction A** confirmed if Q 24:35 light count ≥ 7 and Q 2:255 light count ≤ 2.
- **Direction B** confirmed if Q 24:35 ratio falls within the central third [0.33, 0.67] AND Q 2:255 ratio falls *outside* that range.
- Failure of either direction = NULL on that axis (treat as observed).

## Output files

- Pre-reg: this file.
- Script: `scripts/Q024_F_02_aya_al_nur_vs_aya_al_kursi.py`.
- JSON: `csv/Q024-F-02.json`.
- Findings reported in `06-novel-findings.md`.
