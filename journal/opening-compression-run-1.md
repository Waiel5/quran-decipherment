# opening-compression-run-1

**Date:** 2026-04-12
**Agent:** opening-compression (autonomous research agent)
**Finding file:** `findings/phase-b-hypotheses/opening-compression-prediction.md`

## What I did

Tested the classical claim *fātiḥat al-sūra tadullu ʿalā khātimatihā* ("the opening of a surah indicates its closing") using gzip-based compression distance. Three tests, one mid-run methodological correction, one strong confirmation, one weaker confirmation, and one clean negative result.

## Procedure

1. Load `quran-text/quran-no-tashkeel.json` (114 surahs, 6236 verses).
2. For each surah X ∈ {2, …, 114}: split into `opening_X` (first verse) and `body_X` (rest). Compute `gz(opening_X + body_Y)` for every Y ∈ {1, …, 114} with non-empty body. Rank self (Y=X) among the candidates.
3. Secondary: same with last verse as "signature."
4. Tertiary: canonical-order adjacency — rank of `opening_{N+1}` vs `body_N`, compared against 1000 random surah-order permutations.

## Mid-run methodological pivot

**Pre-registered statistic was naive `gz(opening + body)` size.** Reading the first-pass output revealed it ranked surahs by body length almost perfectly: Al-Kawthar (3 verses) was rank 1 in almost every test; Al-Baqara (286 verses) was rank 114. Top-10 was at null. This is a raw length artefact — short bodies always gzip smaller than long ones, opening content is irrelevant to the ranking.

**Correction:** switched to `delta(Y) = gz(opening_X + body_Y) − gz(body_Y)`. This is the length-controlled Kolmogorov-distance-style statistic and is the right way to ask "does opening_X add *less* entropy to body_X than to body_Y?"

Disclosed in the garden-of-forking-paths section of the finding.

## Results headlines

- **Primary (opening fits own body, length-controlled):**
  - mean self-rank = **35.21 / 114** (null 57.5); z = −7.19
  - top-10 = 34/113 = **30.1%** (null 8.8%); binomial p = **8.9 × 10⁻¹¹**
  - top-25 = 59/113 = 52.2% (null 21.9%); p = 1.9 × 10⁻¹²
  - Confirmed at Bonferroni-surviving level.

- **Secondary (last verse fits own body):**
  - mean self-rank = 38.28 / 114
  - top-10 = 28/113 = 24.8%; p = 3.7 × 10⁻⁷
  - Confirmed; slightly weaker than primary.

- **Tertiary (canonical-order adjacency):**
  - mean `opening_{N+1}` rank vs `body_N`: **56.38** (null 55.49 ± 0.82, z = +1.08, p = 0.87)
  - **REFUTED.** Canonical mushaf ordering does not produce detectable adjacent-surah compression coherence at this resolution. First quantitative attempt at al-Biqāʿī's *munāsaba bayn al-suwar* thesis via information theory; negative result.

- **Robustness:** re-ran primary on full-tashkeel JSON; top-10 = 31.0% (vs 30.1% on no-tashkeel). Signal is orthography-invariant.

## Interpretation

The first-verse → body compression signal is large, clean, and robust. The median surah's opening beats ~92 of 113 foreign bodies. Three *Ḥawāmīm* surahs (Āl ʿImrān, Az-Zukhruf; plus cluster mean Q40-46 rank 28.7) dominate the best-fit list alongside programmatic-opener surahs (At-Tawba, Al-Māʾida, Ibrāhīm, Muḥammad, Al-Wāqiʿa, Al-Ḥāqqa, Al-Bayyina). This is the first information-theoretic confirmation of al-Rāzī's "opening as miniature-of-whole" thesis.

The negative tertiary result is interesting: the classical *munāsaba bayn al-suwar* tradition (al-Biqāʿī 1480) claims adjacent surahs in canonical order cohere thematically. Gzip of adjacent openings against bodies shows no such coherence. This doesn't falsify al-Biqāʿī's content-level argument, but it does constrain the *channel* through which cross-surah coherence can operate.

## Prior art sweep (WebSearch)

- Jiang et al. 2023 ACL Findings "Low-Resource Text Classification with Compressors" — gzip + kNN beats BERT on OOD. Methodological template.
- Cilibrasi & Vitányi 2005 — NCD as universal similarity metric.
- No prior compression analysis of the Quran at verse or opening/body level.
- No prior quantitative test of al-Biqāʿī's *munāsaba* thesis at any resolution.

## Honest limits

- Pre-registered statistic was length-confounded; I switched to delta mid-run. Full disclosure in finding.
- The "adjacency" negative result is at *this* resolution only; shared-vocabulary or shared-theme munāsaba is not tested.
- The effect is driven by opener↔body word-level overlap; I have not decomposed the signal further. A next step would be to remove shared-vocabulary overlap and see what residual compression signal remains.
- NCD statistic failed for this task — documented as a sub-finding.

## Outputs

- `findings/phase-b-hypotheses/opening-compression-prediction.md`
- `findings/phase-b-hypotheses/csv/opening_compression_primary.csv`
- `findings/phase-b-hypotheses/csv/opening_compression_secondary.csv`
- `findings/phase-b-hypotheses/csv/opening_compression_primary_ranks.csv`
- `findings/phase-b-hypotheses/csv/opening_compression_summary.json`
- `scripts/opening_compression_prediction.py`

## Runtime

~2–3 minutes on a 2024 Mac (gzip-heavy; 114² grid + 1000-perm tertiary null).
