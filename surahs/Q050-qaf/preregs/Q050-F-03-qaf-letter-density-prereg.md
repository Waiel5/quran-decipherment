---
finding_id: Q050-F-03
title: "Q 50 letter-ق density: rate of qāf per total letters in Q 50 vs corpus and singleton-letter-cohort"
date_pre_registered: 2026-05-07
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q050-F-03-qaf-density
alpha_raw: 0.05
alpha_bon: 0.0167
direction: "POSITIVE — Q 50 has a per-letter qāf-rate exceeding 95% of length-matched random Quran-verse-window samples; AND Q 50's qāf rate exceeds Q 38's ṣād rate AND Q 68's nūn rate when each is compared to its own letter-class corpus null."
rules_tuple: "(no-tashkeel, grapheme-counting, mushaf-marks-stripped, basmala-not-counted-in-Q50/Q38/Q68, Hafs-Kufan, mushaf-order)"
---

# Q050-F-03 — letter-ق density audit (with singleton-letter cohort replication)

## Hypothesis (LOCKED)

The Razi-classical-commentary file (`/Users/grey/Downloads/quran/data/literature/classical-tafsir/razi-muqattaat-surah-qaf.md`) reports that Q 50 has 57 qāf letters and the same count appears in Q 42, summing to 114 = total surah count. The same file states `Surah 50 (qaf, z=+4.68)` in the per-surah enrichment ratio. This pre-reg locks a fresh empirical test of the per-letter density.

The pre-registered direction is:
- **A**: Q 50's qāf-rate (count(ق) / total_letter_count) exceeds 95% of N=10000 random length-matched (45 verse) windows from the rest-of-corpus.
- **B**: Q 38's ṣād-rate exceeds 95% of N=10000 random length-matched (88 verse) windows from rest-of-corpus.
- **C**: Q 68's nūn-rate exceeds 95% of N=10000 random length-matched (52 verse) windows from rest-of-corpus.

The Q 50 / Q 38 / Q 68 cohort is the project's "singleton-letter" muqaṭṭaʿāt subset. The cohort-replication test asks whether ALL THREE singleton-letter surahs have host-letter-density signatures. If yes, this is a *form-class* finding for the cohort; if only Q 50 passes, the host-letter-density is a Q-50-specific feature.

## Direction (LOCKED)

POSITIVE for all three sub-tests. NULL = Q-host-letter-rate at or below 50th percentile.

## Operationalization

For each surah X ∈ {50, 38, 68}:

1. Compute X's host-letter rate: `count(host_letter_in_X) / total_letter_count_in_X`.
2. For each of N=10000 random iterations (seeded), sample a contiguous-verse window from the rest-of-Quran (114 surahs minus X) of length K(X) = total_verses_in_X. Compute the host-letter rate in that window.
3. Empirical p = (number of nulls ≥ X's rate + 1) / (N + 1).

(Null windows that span surah-boundaries are allowed; we treat the full corpus as a flat sequence of verses.)

## Letters

- Q 50 host letter: ق (qāf, U+0642).
- Q 38 host letter: ص (ṣād, U+0635).
- Q 68 host letter: ن (nūn, U+0646).

## Rules-tuple (LOCKED)

`(no-tashkeel, grapheme-counting, mushaf-marks-stripped ۚ ۖ ۗ ۛ ۜ ۠ ۩ ۭ, basmala-not-counted-in-Q50/Q38/Q68, Hafs-Kufan, mushaf-order)`

Letter count = sum of Arabic-alpha graphemes (excluding spaces, punctuation, mushaf-marks) in the corpus text.

The basmala at the start of each surah (except Q 1, Q 9) is OMITTED before counting (consistent with the project's default rule); the muqaṭṭaʿāt-letters of verse 1 ARE counted (they ARE part of the canonical text).

## Bonferroni

3 sub-tests in family. α_bon = 0.05/3 = 0.0167.

## Success criteria

| Test | p (Bon-corrected) | Verdict |
|:--|:--|:--|
| Q 50 ق-rate | < 0.0167 | **A-CONFIRMED** |
| Q 38 ص-rate | < 0.0167 | **B-CONFIRMED** |
| Q 68 ن-rate | < 0.0167 | **C-CONFIRMED** |

If all 3 pass: COHORT-CONFIRMED (singleton-letter surahs all show host-letter density).
If only A passes: Q-50-SPECIFIC (only Q 50 has the density signature).
If 2 pass: PARTIAL.
If 0 pass: NULL.

## Honest acknowledgment

The Razi-classical file already reports `z=+4.68` for Q 50 qāf, derived under a previous project pipeline. This pre-reg replicates the test under the LOCKED rules-tuple specified here, with explicit Bonferroni-3 correction across the singleton-letter cohort. The aggregate muqaṭṭaʿāt-density chi² claim of `χ² = 228.78, p < 10⁻¹⁵` is a SEPARATE finding (corpus-aggregate) and is NOT this test.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q050_F_03_qaf_letter_density.py`.
- JSON: `csv/Q050-F-03.json`.
- Findings: `06-novel-findings.md` §Q050-F-03.
