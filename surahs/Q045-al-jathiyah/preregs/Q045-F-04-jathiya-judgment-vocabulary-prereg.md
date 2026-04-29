---
prereg_id: Q045-F-04
title: Q 45 al-Jāthiyah judgment-vocabulary density vs other judgment-themed surahs
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T03:15:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q045-F-04 — Q 45 judgment-vocabulary density rank

## 1. Hypothesis (direction-locked)

**H1 (descriptive ranking)**: Q 45 al-Jāthiyah is in the **top quartile** (rank ≤ 28 / 114) of the corpus by combined judgment-vocabulary density (per 1000 QAC tokens), where the judgment-cluster is the locked a-priori inventory below.

**H1b (within-eschatological-comparison)**: Q 45 ranks in the **top decile (≤ 11/114)** by judgment-density relative to the comparable-length filter (n_verses ∈ [25, 60]).

## 2. Null

**H0a**: Q 45 rank > 28/114.
**H0b**: Q 45 rank > 11/114 within the n_verses ∈ [25, 60] subset.

## 3. Operationalization — JUDGMENT-CLUSTER LOCKED A-PRIORI

The judgment-cluster is locked here BEFORE the count is run:

| Buckwalter root | Arabic | Gloss |
|:--:|:--:|:--|
| jzy | ج-ز-ي | recompense / requite |
| jvw | ج-ث-و | kneel / cluster on knees |
| Hsb | ح-س-ب | reckon / account |
| Hkm | ح-ك-م | judge / rule |
| qDy | ق-ض-ي | decree / fulfil |
| dyn | د-ي-ن | religion / judgment-debt |
| sAE | س-ع-ة (variant) | the Hour |
| qwm | ق-و-م (الساعة) | (qiyāma) standing-up |
| btl | ب-ط-ل | proven-vain / nullified |
| xsr | خ-س-ر | loss |
| xtm | خ-ت-م | sealed |
| ntq | ن-ط-ق | speak (judgment-book speaks) |
| nsx | ن-س-خ | record (we transcribed) |

13 roots. **This list is locked**.

- Source corpus: QAC v0.4 (`/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`).
- Per-surah token-counts: from QAC, count total tokens (segment 1 entries) and tokens whose ROOT field matches any of the 13 cluster roots.
- Per-surah judgment-density: tokens-in-cluster / total-tokens × 1000.
- Rank Q 45 in the all-114 list.
- Apply the n_verses ∈ [25, 60] subset filter using `/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv` (or fallback to `quran-no-tashkeel.json` `total_verses`); rank Q 45 within the filtered list.

## 4. Direction lock

Pre-committed direction: Q 45 ranks high on judgment-density.

If Q 45 rank > 28: **H1 NULL**.
If Q 45 rank > 11 in filtered subset: **H1b NULL**.
If Q 45 in *bottom* quartile (rank > 86): **PRECOMMIT_VIOLATION** (the surah is named after the judgment-day kneeling — top is expected).

## 5. Bonferroni

k = 2 (H1 + H1b); α_corrected = 0.05/2 = 0.025.

## 6. Success / failure criteria

- **VINDICATED**: H1 ∧ H1b both pass.
- **PARTIAL-VINDICATION**: H1 passes (top-25%); H1b fails (not top-decile in length-filtered).
- **NULL**: H1 fails.
- **Precommit violation**: Q 45 in bottom-quartile.

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q045-F-04.json` with: per-cluster-root counts in Q 45, total cluster-token count, Q 45 density, Q 45 corpus-rank, Q 45 length-filtered-rank, top-10 judgment-densest surahs.

## 9. Motivation

Q 45's distinctive name — *al-Jāthiyah*, "the kneeling" — refers to Q 45:28 *wa-tarā kulla ummatin jāthiya*, the eschatological scene where every nation kneels before its book of deeds. al-Ṭabarī, *Jāmiʿ al-bayān* ad Q 45:28, treats this as the surah's *maqṣūd*. Empirically: does the surah's lexical density actually concentrate judgment-vocabulary, or is the *jāthiya*-naming a single-verse salience feature that does not extend to the surah's vocabulary signature? The 13-root cluster is comprehensive enough to capture both eschatological-scene roots (jvw, sAE, qwm) and judgment-act roots (jzy, Hkm, qDy, Hsb, dyn, xsr, btl) and the Q 45-specific *seal-the-senses + book-speaks* roots (xtm, ntq, nsx).

## 10. Honest pre-commit caveats

- The cluster-root list is project-specific; alternative inventories could shift Q 45's rank by 5-10 positions. The pre-locked list is conservative (excludes some peripheral roots like `Erq` (sweat), `vqf` (heavy-burden), etc.).
- Density-vs-count: density-per-1000 is the locked metric (matches Q024-F-01, Q040-F-01 conventions); raw-count rank reported as descriptive sub-statistic.
- Length-filter [25, 60] is set wide enough to include Q 45 (37 verses) and a substantial reference set of comparable surahs; this is locked BEFORE the rank is observed.
- The QAC's `jvw` root for *jāthiya* is checked at parse-time (ج-ث-و); if QAC actually uses a different Buckwalter encoding (e.g., `jvy` or `jvA`) the parser tries these alternates and reports which key matched.
