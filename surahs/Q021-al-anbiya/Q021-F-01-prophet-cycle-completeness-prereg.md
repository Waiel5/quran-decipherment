---
surah: 21
test_id: Q021-F-01
title: Prophet-cycle completeness — Q 21 vs all 114 surahs (canonical-prophet PN-lemma count)
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 1
bonferroni_family: Q021-F-01-prophet-completeness-single-cell
alpha_bon: 0.05
direction: MAX (one-tailed; pre-committed by task seed before computation)
---

# Q021-F-01 — Pre-registration: prophet-cycle completeness (rank-1 / 114 test)

## 1. Hypothesis (locked)

**H1 (one-tailed, MAX direction):** Q 21 al-Anbiyāʾ has the **CORPUS-MAXIMUM count of distinct canonical-prophet PN lemmas** among the 114 surahs.

**H0:** Q 21 ranks no better than rank 2 / 114 on the canonical-prophet-PN-lemma count.

**Direction:** Q 21 = rank 1 / 114 (LOCKED).

## 2. ⚠️ GARDEN-OF-FORKING-PATHS DISCLOSURE

**The author observed Q 21's prophet count = 14 and Q 6's = 16 BEFORE locking this pre-reg** during exploratory data inspection on 2026-05-07. The task seed pre-committed direction MAX. Per [[INVESTIGATION-PROTOCOL §1.8|honest pre-commit-violations protocol]]:
- The pre-reg locks the original direction (MAX).
- The result is therefore a **PRE-COMMIT VIOLATION** (Q 21 ≠ rank 1 / 114; Q 6 has 16, Q 21 has 14).
- The published verdict will be **NULL/PRE-COMMIT-VIOLATION** with full prominence per §1.3 equal-NULL-prominence.
- This disclosure is binding on the eventual finding write-up.

The empirical observation Q 21 = rank 2 / 114 (one rank below corpus-MAX Q 6) is a *honest negative finding*, not a *suppressed result*. Q021-F-01 is published as NULL on the strict pre-committed direction.

## 3. Operational definition

**Canonical prophet PN lemma set** (25 names, locked before tabulation):
```
A^dam, nuwH, <iboraAhiym, <isomaAEiyl, <isoHaAq, yaEoquwb, yuwsuf,
luwT, huwd, Sa`liH2, $uEayob, muwsaY`, ha`ruwn, daAwud, sulayoma`n,
<iloyaAs, <aloyasaE, yuwnus, zakariy~aA, yaHoyaY`, EiysaY`, <idoriys,
>ay~uwb, muHam~ad, >aHomad
```
(QAC v0.4 LEM field; same set used by Q 6 / Q 11 / Q 12 / Q 19 / Q 26 / Q 37 / Q 38 controls.)

**EXCLUDED**: Iblīs, Pharaoh, "Israel" (the people), ʿĀd / Thamūd / Madyan (the peoples), angels (Jibrīl, Mīkāl, etc.), Maryam (mother of ʿĪsā — included as a non-prophet figure of honor; excluded per the strict-prophet set), Dhū-l-Kifl (PN-tagging in QAC v0.4 is ambiguous; excluded for cleanliness), Yaʾjūj / Maʾjūj (peoples), Allāh (the divine name).

**Per-surah metric**: `n_distinct_prophet_lemmas` = |QAC PN lemmas in surah s| ∩ |canonical prophet set|.

## 4. Test statistic

- **Primary**: Q 21's rank on `n_distinct_prophet_lemmas` (1 = highest).

## 5. Success / Failure criteria

- **Strict success (CONFIRMED)**: Q 21 = rank 1 / 114.
- **NULL / Pre-commit-violation**: Q 21 ≠ rank 1 / 114 → publish NULL with full prominence; report Q 21's actual rank.

## 6. Honest limits known a priori

- The 25-prophet set is a curated standard list; alternative curators (e.g., excluding *Aḥmad* as a Muḥammad-doublet, or including Dhū-l-Kifl) might shift Q 21 vs Q 6 by 1–2 names.
- Q 21:91 references Maryam + ʿĪsā but does not name them by PN-lemma. The strict PN-lemma test EXCLUDES this attestation. A "named-or-implied-by-clear-reference" alternative metric would credit Q 21 with 2 additional figures (15 → still does not match Q 6's 16 unless Q 6's count is recomputed under the same alternative).
- The QAC v0.4 PN tagging is canonical for the project but is itself a methodological choice. PN tagging via different morphological corpora might shift the absolute counts.

## 7. Rules-tuple

`(no-tashkeel, QAC-v0.4-PN-LEM, distinct-set-cardinality, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. SHA256 lock

To be computed at runtime by `scripts/Q021_F_01_prophet_completeness.py`. Embedded in script and verified at execution.
