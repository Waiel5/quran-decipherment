---
id: H-NEW-740
title: "Pre-reg — Pre-Islamic Arabic poetry control for iʿjāz al-fawāṣil anti-twin signature"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-730 (Quran r=−0.8643 content×rhyme anti-correlation, claimed as empirical signature of al-Bāqillānī iʿjāz al-fawāṣil)
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7 + rules-tuple-shift discipline
seed: 20260444
---

# [[h-new-740-preislamic-poetry-control|H-NEW-740]] — Pre-Islamic Poetry Control: Pre-Registration

## 1. Hypothesis under test

[[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] found that, window-by-window in the mushaf, content-cohesion-distance and rhyme-dispersion-distance are anti-correlated at Pearson r = −0.8643, claimed as the empirical signature of al-Bāqillānī's *iʿjāz al-fawāṣil* — the Quran's "inimitable" simultaneous tightening of meaning and dispersion of sound.

**Critical control**: if the same anti-correlation appears in **pre-Islamic Arabic poetry** (the qaṣīda monorhyme tradition that al-Bāqillānī himself contrasted the Quran against), then the architectural anti-twinning is a **genre-generic property of Arabic verse**, not a Quranic distinction — the iʿjāz claim collapses to genre convention. If the anti-correlation is **absent or weak** in pre-Islamic poetry, the iʿjāz claim is empirically distinguished.

## 2. Pre-registered hypothesis

> **Pre-Islamic monorhyme qaṣīda corpus, analyzed under the same window-level methodology as [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]], will show Pearson r(content × rhyme) ≈ 0 or weakly negative — but NOT as strong as the Quran's r=−0.86.**

The genre prior: the qaṣīda is **monorhyme by convention** — every bayt of a single qaṣīda ends in the same rāwī letter. Within a qaṣīda, rhyme-dispersion ≈ 0; across qaṣīdas, rhyme-dispersion is driven by the editorial choice of rāwī, NOT by content-cohesion. So the predicted anti-correlation should be weak.

## 3. Corpus inspection (locked AFTER inventory)

Files inspected at `/Users/grey/Downloads/quran/data/baseline-corpora/raw/`:

**Pre-Islamic (jāhilī, ~6th-c. CE):**
- `muallaqa-imru-al-qais.txt` (~80 verses, single qaṣīda)
- `muallaqa-tarafa.txt` (~120 verses, single qaṣīda)
- `muallaqa-zuhayr.txt` (~60 verses, single qaṣīda)
- `muallaqa-labid.txt` (~180 verses, single qaṣīda)
- `muallaqa-amr-bin-kulthum.txt` (~100 verses, single qaṣīda)
- `muallaqa-antara.txt` (~75 verses, single qaṣīda)
- `muallaqa-harith.txt` (~170 verses, single qaṣīda)
- `diwan-imru-al-qais.txt` (~2300 lines, organized by qāfiya-section)
- `diwan-antara.txt` (~3000 lines)
- `diwan-labid.txt` (~1640 lines)
- `diwan-tarafa.txt` (~640 lines)
- `diwan-zuhayr.txt` (~520 lines)
- `diwan-harith.txt` (~190 lines, sparse)
- `diwan-amr-ibn-kulthum.txt` (~12 lines, too small)

**Abbasid (~10th-c. CE) — useful as DIFFERENT-ERA comparator (not iʿjāz-claim-relevant):**
- `mutanabbi-diwan.txt` (~995 lines)

**Decision**: use the SEVEN MUʿALLAQĀT plus the SEVEN PRE-ISLAMIC DĪWĀNS (drop diwan-amr-ibn-kulthum.txt as it has only 12 lines of editorial cruft, not actual poetry).

## 4. Methodology — rules-tuple shift documented

This is a CONTROLLED COMPARISON. The rules-tuple necessarily shifts between Quran and poetry because:
- **No QAC-equivalent root annotation** for poetry. Substitute: top-K word-FORM (or shallow stem) frequency vector.
- **Different unit (verse-equivalent) sizes**. Pre-Islamic bayt has two hemistichs (sometimes written one-per-line). Quranic verse is typically 5-30 words.
- **Monorhyme rāwī** is the genre constraint vs. mushaf-level rhyme variety.

Rules-tuple shift items:
| Item | Quran ([[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]) | Poetry ([[h-new-740-preislamic-poetry-control|H-NEW-740]]) | Reason |
|:--|:--|:--|:--|
| Content basis | QAC top-500 ROOT | Top-500 word-FORMS (after light stripping of common particles `و ف ب ل ك`) | No QAC for poetry |
| Smoothing | Dirichlet α=0.5 | Same | Identical |
| Distance | Fisher-Rao (Bhattacharyya) | Same | Identical |
| Rhyme basis | 28-letter verse-final | 28-letter bayt-final | Identical, but bayt-final is by convention monorhyme |
| Unit | 1 surah | 1 "qaṣīda-block" of 30 contiguous bayts within a qāfiya-section | Match Quran median surah size |
| Window K | 15 surahs | 15 qaṣīda-blocks | Identical |
| Number of windows | 100 | as many as fit | Constrained by data |

## 5. Construction of qaṣīda-blocks

For each muʿallaqa: treat the entire poem as ONE qaṣīda-block (since muʿallaqāt are ≈80-180 bayts).
For each dīwān: split into qāfiya-sections (these are explicitly headed `قافية الباء`, `قافية التاء`, etc.); within each section, slice into contiguous 30-bayt blocks (drop trailing block if <15 bayts). Each block inherits the section's rāwī.

This preserves the monorhyme property within each block.

## 6. Pre-committed direction

> r_poetry > r_quran = −0.8643 (Quranic anti-correlation should be the strongest by hypothesis).

More specifically:
- **PASS-CONFIRMS-IʿJĀZ-CLAIM**: r_poetry > −0.4 (poetry shows essentially NO architectural anti-twin; the Quran's r=−0.86 is genre-distinguishing).
- **DIRECTIONAL-CONFIRMS**: −0.6 < r_poetry ≤ −0.4 (poetry shows weak anti-twin; Quran is significantly stronger).
- **FALSIFIES-IʿJĀZ-CLAIM**: r_poetry ≤ −0.6 (poetry shows similar architectural anti-twin; the iʿjāz claim collapses to genre convention).
- **NULL-DUE-TO-DATA-GAP**: too few qaṣīda-blocks (<30) to compute a meaningful 100-window Pearson; report and stop.

## 7. Bonferroni structure

Tests:
1. Pre-Islamic poetry r(content × rhyme) — primary.
2. Spearman ρ on same — robustness.
3. Mutanabbi (post-classical Arabic, secondary control with no iʿjāz-relevance) — sanity.

Bonferroni-3 → α_bon = 0.05/3 = **0.01667**.

## 8. What would FALSIFY the iʿjāz claim

- r_poetry ≤ −0.6 with permutation p ≤ 0.01667.
- This would mean the architectural anti-twin is an Arabic-verse-genre property, not a Quranic distinction.

## 9. What would CONFIRM the iʿjāz claim

- r_poetry > −0.4 (or even > 0) — pre-Islamic qaṣīda corpus does NOT exhibit window-level content-rhyme anti-twin, validating the architectural distinction [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] attributed to the Quran.

## 10. Discipline notes

- **ONE text** discipline applies to the Quran corpus only; the poetry is a SEPARATE corpus and is treated as such.
- **NULL with equal prominence**: if poetry r is similar to Quran r, the iʿjāz claim is FALSIFIED and that finding is reported with equal weight.
- **Rules-tuple shift** is unavoidable here. The shift items are pre-locked above. If after running, residual concern about confounds remains, queue follow-ups rather than reinterpret post-hoc.
- **Permutation null**: shuffle rhyme-positions of qaṣīda-blocks (n_perms = 10000, seed 20260444). Compute Pearson r each shuffle. Empirical p of (r_obs ≤ r_null).
- Single corpus per analysis run; no pooling across pre-Islamic + Mutanabbi (Mutanabbi reported separately).

## 11. Files

- Script: `scripts/h_new_740_preislamic_poetry_control.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-740.json`
- Findings: `findings/phase-b-hypotheses/h-new-740-preislamic-poetry-control.md`
- Journal: `journal/h-new-740-run-1.md`

## 12. Seed

20260444.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
