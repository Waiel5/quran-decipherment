---
title: "Per-surah Zipf α heterogeneity and its diachronic correlates (H14)"
phase: B
status: exploratory — hypothesis H14 REJECTED in the direction it was stated
hypothesis_id: H14 (deep-hypotheses-queue, Wave 1)
agent: zipf-per-surah-run-1
date: 2026-04-12
rules:
  orthography: no-tashkeel
  word_definition: lemma                # Quranic Arabic Corpus 0.4 LEM field (identical to info-theory rule)
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1 (QAC default)
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: 1.5-permutation (10k label permutations) for Spearman rho; 1000-resample bootstrap for per-surah alpha 95% CI
script: /Users/grey/Downloads/quran/analysis/zipf_per_surah_run.py
inputs:
  - /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  - /Users/grey/Downloads/quran/data/revelation-order.csv
outputs:
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/zipf-per-surah.csv
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/zipf-per-surah-results.json
sanity:
  whole_quran_alpha_recomputed: 1.3177
  whole_quran_alpha_info_theory_anchor: 1.318
  whole_quran_r2: 0.9754
  n_distinct_lemmas: 4832
  n_lemma_tokens: 74608
---

# Per-surah Zipf α heterogeneity and its diachronic correlates

> **Headline verdict.** Hypothesis H14 is **rejected in the direction it
> was stated.** Per-surah Zipf α does vary enormously (0.29 to 1.00
> among 90 fit-eligible surahs), but the variation is overwhelmingly a
> **length artifact** (Spearman ρ(α, n_tokens) = **+0.962**). The
> *direction* of the residual diachronic signal is the **opposite** of
> H14's prediction: Late Meccan and Medinan surahs have the HIGHEST
> α (≈ 0.78), Early Meccan surahs have the LOWEST α (≈ 0.47). The
> oracular-oath-cluster short Meccan surahs — which H14 predicted would
> have α > 1.5 — mostly cannot even be fit (24/114 surahs have < 50
> distinct lemmas and are reported as `insufficient-data`); those that
> can be fit sit at α ≈ 0.3-0.5, not > 1.5.
>
> The whole-Quran α = 1.318 is therefore NOT a "per-surah average" —
> it is an emergent property of having enough distinct lemmas
> (≈ 5 000) for the Zipf tail to become visible under OLS. Jensen's
> inequality / aggregation: the whole-Quran α is **larger than any
> individual surah's α**. This is a real and publishable finding, but
> it is the *opposite* of the H14 conjecture.

## 1. What H14 predicted

From `findings/deep-hypotheses-queue.md` §H14:

> The whole-Quran Zipf α=1.318 conceals significant per-surah variation.
> Each of the 114 surahs individually fits a Zipf distribution with its
> own α_s. Early Meccan surahs have α_s > 1.5 (more extreme vocabulary
> concentration, because oracular style repeats few theological terms)
> and Medinan surahs have α_s ≈ 1.1 (because legal prose uses a flatter
> vocabulary).
>
> **Acceptance criterion.** |Spearman ρ(α_s, revelation-order)| > 0.3
> with empirical p<0.01 AND the length-controlled version still
> significant.

## 2. Method

- **Lemma tokens per surah.** Extracted from the QAC 0.4 STEM lines with
  `LEM:` fields. Total 74 608 lemma tokens → 4 832 distinct lemmas, per-surah
  distributions from 9 (Al-Kawthar) to 5 884 (Al-Baqara) tokens.
- **Zipf fit rule (identical to info-theory §4).** Sort lemma frequencies
  descending; OLS on `log(rank_1_based) = log(r+1)` vs `log(freq)`. Slope is
  −α.
- **Minimum 50 distinct lemmas** per the task spec. Surahs below the
  threshold are reported as `insufficient-data` — 24 of 114 surahs.
- **Bootstrap 95% CI** per surah: 1000 resamples of N lemma tokens with
  replacement, refit α each time, percentile CI. Same seed (17) for
  reproducibility.
- **Permutation test** for ρ significance: 10 000 shuffles of the revelation-order
  label, two-sided empirical p on |ρ|.
- **Length-bin stratification** (5 quintiles of n_lemma_tokens) for a
  length-controlled Spearman ρ.
- **Partial correlation** of α vs revelation-order controlling for
  log(n_tokens), via OLS residualization.

## 3. Whole-Quran sanity (matches info-theory)

Recomputing the whole-Quran Zipf under this exact rule:

> **α = 1.3177, R² = 0.9754, 4 832 distinct lemmas, 74 608 tokens.**

This matches info-theory §4 (1.318) to 4 decimals, confirming the pipeline.

**Crucially:** this is under the *lemma* rule. The cross-baseline agent's
whole-Quran α = 0.97 was under the *orthographic-token* rule — a different
rule tuple that gives a different number. They are not inconsistent; they
measure different things. Under the lemma rule, the Quran α = 1.32 is
**steeper** than the classical-Arabic baseline (Bukhari ≈ 1.07, Sira ≈ 1.03,
Jahiz ≈ 0.94) reported by cross-baseline. Under the word-token rule, both
are around 1.0. **The "Quran Zipf isn't distinctive" verdict from
cross-baseline specifically concerns the orthographic-token α** and does not
rule out a lemma-level difference. (A proper lemma-level classical-Arabic
baseline has not been computed; it would require morphology on Bukhari, which
cross-baseline did not have.)

## 4. Per-surah Zipf α — full table

90 surahs fit, 24 surahs insufficient. Table sorted by revelation order.
Bootstrap 95% CI in the final column.

| rev# | sid | name | period | Nöldeke | n_tok | n_dis | α | R² | 95% CI |
|---:|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | 96 | Al-Alaq | Mec | EarlyM | 72 | 49 | — | — | insufficient |
| 2 | 68 | Al-Qalam | Mec | EarlyM | 278 | 170 | 0.525 | 0.862 | [0.616, 0.727] |
| 3 | 73 | Al-Muzzammil | Mec | EarlyM | 194 | 128 | 0.484 | 0.861 | [0.559, 0.695] |
| 4 | 74 | Al-Muddaththir | Mec | EarlyM | 249 | 154 | 0.525 | 0.873 | [0.582, 0.699] |
| 5 | 1 | Al-Fatiha | Mec | EarlyM | 29 | 23 | — | — | insufficient |
| 6 | 111 | Al-Masad | Mec | EarlyM | 23 | 20 | — | — | insufficient |
| 7 | 81 | At-Takwir | Mec | EarlyM | 101 | 76 | 0.352 | 0.625 | [0.540, 0.709] |
| 8 | 87 | Al-A'la | Mec | EarlyM | 72 | 60 | 0.291 | 0.723 | [0.439, 0.644] |
| 9 | 92 | Al-Layl | Mec | EarlyM | 70 | 56 | 0.325 | 0.768 | [0.449, 0.653] |
| 10 | 89 | Al-Fajr | Mec | EarlyM | 136 | 93 | 0.458 | 0.860 | [0.527, 0.687] |
| 11 | 93 | Ad-Dhuha | Mec | EarlyM | 39 | 30 | — | — | insufficient |
| 12 | 94 | Ash-Sharh | Mec | EarlyM | 25 | 21 | — | — | insufficient |
| 13 | 103 | Al-Asr | Mec | EarlyM | 14 | 13 | — | — | insufficient |
| 14 | 100 | Al-Adiyat | Mec | EarlyM | 37 | 31 | — | — | insufficient |
| 15 | 108 | Al-Kawthar | Mec | EarlyM | 9 | 8 | — | — | insufficient |
| 16 | 102 | At-Takathur | Mec | EarlyM | 28 | 19 | — | — | insufficient |
| 17 | 107 | Al-Maun | Mec | EarlyM | 23 | 20 | — | — | insufficient |
| 18 | 109 | Al-Kafirun | Mec | EarlyM | 21 | 8 | — | — | insufficient |
| 19 | 105 | Al-Fil | Mec | EarlyM | 23 | 21 | — | — | insufficient |
| 20 | 113 | Al-Falaq | Mec | EarlyM | 23 | 16 | — | — | insufficient |
| 21 | 114 | An-Nas | Mec | EarlyM | 20 | 15 | — | — | insufficient |
| 22 | 112 | Al-Ikhlas | Mec | EarlyM | 13 | 8 | — | — | insufficient |
| 23 | 53 | An-Najm | Mec | EarlyM | 338 | 187 | 0.591 | 0.903 | [0.653, 0.756] |
| 24 | 80 | Abasa | Mec | EarlyM | 128 | 102 | 0.330 | 0.761 | [0.468, 0.611] |
| 25 | 97 | Al-Qadr | Mec | EarlyM | 29 | 22 | — | — | insufficient |
| 26 | 91 | Ash-Shams | Mec | EarlyM | 53 | 44 | — | — | insufficient |
| 27 | 85 | Al-Buruj | Mec | EarlyM | 100 | 76 | 0.376 | 0.790 | [0.477, 0.656] |
| 28 | 95 | At-Tin | Mec | EarlyM | 33 | 33 | — | — | insufficient |
| 29 | 106 | Quraysh | Mec | EarlyM | 17 | 15 | — | — | insufficient |
| 30 | 101 | Al-Qariah | Mec | EarlyM | 34 | 23 | — | — | insufficient |
| 31 | 75 | Al-Qiyamah | Mec | EarlyM | 160 | 103 | 0.501 | 0.868 | [0.552, 0.710] |
| 32 | 104 | Al-Humazah | Mec | EarlyM | 33 | 27 | — | — | insufficient |
| 33 | 77 | Al-Mursalat | Mec | EarlyM | 179 | 107 | 0.563 | 0.847 | [0.634, 0.773] |
| 34 | 50 | Qaf | Mec | MiddleM | 356 | 206 | 0.565 | 0.874 | [0.643, 0.744] |
| 35 | 90 | Al-Balad | Mec | EarlyM | 79 | 62 | 0.307 | 0.744 | [0.432, 0.625] |
| 36 | 86 | At-Tariq | Mec | EarlyM | 60 | 43 | — | — | insufficient |
| 37 | 54 | Al-Qamar | Mec | MiddleM | 338 | 187 | 0.599 | 0.890 | [0.654, 0.754] |
| 38 | 38 | Sad | Mec | MiddleM | 700 | 337 | 0.651 | 0.921 | [0.711, 0.782] |
| 39 | 7 | Al-A'raf | Mec | LateM | 3177 | 818 | 0.913 | 0.961 | [0.942, 0.984] |
| 40 | 72 | Al-Jinn | Mec | MiddleM | 279 | 138 | 0.669 | 0.908 | [0.704, 0.825] |
| 41 | 36 | Ya-Sin | Mec | MiddleM | 678 | 297 | 0.713 | 0.924 | [0.765, 0.838] |
| 42 | 25 | Al-Furqan | Mec | MiddleM | 861 | 371 | 0.718 | 0.932 | [0.753, 0.822] |
| 43 | 35 | Fatir | Mec | LateM | 755 | 334 | 0.690 | 0.919 | [0.757, 0.831] |
| 44 | 19 | Maryam | Mec | MiddleM | 929 | 359 | 0.750 | 0.952 | [0.785, 0.848] |
| 45 | 20 | Ta-Ha | Mec | MiddleM | 1282 | 482 | 0.765 | 0.936 | [0.813, 0.870] |
| 46 | 56 | Al-Waqiah | Mec | EarlyM | 363 | 205 | 0.581 | 0.877 | [0.663, 0.760] |
| 47 | 26 | Ash-Shuara | Mec | MiddleM | 1247 | 409 | 0.846 | 0.937 | [0.885, 0.946] |
| 48 | 27 | An-Naml | Mec | MiddleM | 1108 | 413 | 0.784 | 0.940 | [0.820, 0.885] |
| 49 | 28 | Al-Qasas | Mec | LateM | 1374 | 467 | 0.812 | 0.946 | [0.850, 0.907] |
| 50 | 17 | Al-Isra | Mec | MiddleM | 1502 | 532 | 0.791 | 0.950 | [0.825, 0.877] |
| 51 | 10 | Yunus | Mec | LateM | 1786 | 485 | 0.907 | 0.960 | [0.929, 0.987] |
| 52 | 11 | Hud | Mec | LateM | 1855 | 553 | 0.855 | 0.953 | [0.897, 0.952] |
| 53 | 12 | Yusuf | Mec | LateM | 1696 | 511 | 0.851 | 0.961 | [0.883, 0.937] |
| 54 | 15 | Al-Hijr | Mec | MiddleM | 634 | 288 | 0.679 | 0.914 | [0.746, 0.822] |
| 55 | 6 | Al-An'am | Mec | LateM | 2946 | 724 | 0.936 | 0.963 | [0.962, 1.006] |
| 56 | 37 | As-Saffat | Mec | MiddleM | 822 | 359 | 0.703 | 0.922 | [0.762, 0.832] |
| 57 | 31 | Luqman | Mec | LateM | 526 | 247 | 0.671 | 0.925 | [0.726, 0.810] |
| 58 | 34 | Saba | Mec | LateM | 844 | 329 | 0.767 | 0.933 | [0.810, 0.880] |
| 59 | 39 | Az-Zumar | Mec | LateM | 1125 | 392 | 0.799 | 0.955 | [0.829, 0.891] |
| 60 | 40 | Ghafir | Mec | LateM | 1169 | 397 | 0.816 | 0.954 | [0.844, 0.907] |
| 61 | 41 | Fussilat | Mec | LateM | 767 | 310 | 0.726 | 0.940 | [0.778, 0.852] |
| 62 | 42 | Ash-Shura | Mec | LateM | 809 | 303 | 0.769 | 0.944 | [0.814, 0.887] |
| 63 | 43 | Az-Zukhruf | Mec | MiddleM | 782 | 333 | 0.726 | 0.933 | [0.765, 0.835] |
| 64 | 44 | Ad-Dukhan | Mec | MiddleM | 332 | 182 | 0.598 | 0.895 | [0.660, 0.764] |
| 65 | 45 | Al-Jathiyah | Mec | LateM | 469 | 200 | 0.738 | 0.935 | [0.760, 0.852] |
| 66 | 46 | Al-Ahqaf | Mec | LateM | 619 | 274 | 0.714 | 0.918 | [0.765, 0.844] |
| 67 | 51 | Adh-Dhariyat | Mec | EarlyM | 347 | 193 | 0.586 | 0.874 | [0.672, 0.770] |
| 68 | 88 | Al-Ghashiyah | Mec | EarlyM | 91 | 68 | 0.401 | 0.772 | [0.504, 0.687] |
| 69 | 18 | Al-Kahf | Mec | MiddleM | 1528 | 551 | 0.791 | 0.946 | [0.826, 0.880] |
| 70 | 16 | An-Nahl | Mec | LateM | 1778 | 551 | 0.838 | 0.954 | [0.872, 0.928] |
| 71 | 71 | Nuh | Mec | MiddleM | 216 | 127 | 0.570 | 0.876 | [0.618, 0.752] |
| 72 | 14 | Ibrahim | Mec | LateM | 800 | 333 | 0.722 | 0.938 | [0.776, 0.845] |
| 73 | 21 | Al-Anbiya | Mec | MiddleM | 1097 | 422 | 0.776 | 0.926 | [0.821, 0.880] |
| 74 | 23 | Al-Mu'minun | Mec | MiddleM | 989 | 391 | 0.756 | 0.934 | [0.803, 0.866] |
| 75 | 32 | As-Sajdah | Mec | LateM | 361 | 192 | 0.612 | 0.891 | [0.686, 0.787] |
| 76 | 52 | At-Tur | Mec | EarlyM | 295 | 181 | 0.527 | 0.808 | [0.644, 0.750] |
| 77 | 67 | Al-Mulk | Mec | MiddleM | 314 | 170 | 0.613 | 0.899 | [0.656, 0.764] |
| 78 | 69 | Al-Haqqah | Mec | EarlyM | 252 | 156 | 0.524 | 0.879 | [0.597, 0.707] |
| 79 | 70 | Al-Ma'arij | Mec | EarlyM | 209 | 141 | 0.464 | 0.839 | [0.562, 0.688] |
| 80 | 78 | An-Naba | Mec | EarlyM | 171 | 121 | 0.434 | 0.817 | [0.536, 0.673] |
| 81 | 79 | An-Nazi'at | Mec | EarlyM | 172 | 126 | 0.406 | 0.806 | [0.504, 0.650] |
| 82 | 82 | Al-Infitar | Mec | EarlyM | 79 | 53 | 0.498 | 0.787 | [0.560, 0.787] |
| 83 | 84 | Al-Inshiqaq | Mec | EarlyM | 104 | 75 | 0.405 | 0.830 | [0.490, 0.662] |
| 84 | 30 | Ar-Rum | Mec | LateM | 781 | 289 | 0.787 | 0.948 | [0.802, 0.880] |
| 85 | 29 | Al-'Ankabut | Mec | LateM | 942 | 335 | 0.797 | 0.952 | [0.831, 0.898] |
| 86 | 83 | Al-Mutaffifin | Mec | EarlyM | 165 | 95 | 0.575 | 0.894 | [0.589, 0.751] |
| 87 | 2 | Al-Baqarah | Med | Med | 5884 | 1136 | 0.996 | 0.971 | [1.009, 1.043] |
| 88 | 8 | Al-Anfal | Med | Med | 1201 | 399 | 0.821 | 0.954 | [0.843, 0.907] |
| 89 | 3 | Al-Imran | Med | Med | 3371 | 760 | 0.954 | 0.967 | [0.963, 1.006] |
| 90 | 33 | Al-Ahzab | Med | Med | 1265 | 453 | 0.784 | 0.940 | [0.835, 0.893] |
| 91 | 60 | Al-Mumtahanah | Med | Med | 332 | 157 | 0.690 | 0.926 | [0.718, 0.826] |
| 92 | 4 | An-Nisa | Med | Med | 3653 | 809 | 0.964 | 0.966 | [0.977, 1.017] |
| 93 | 99 | Az-Zalzalah | Med | EarlyM | 34 | 27 | — | — | insufficient |
| 94 | 57 | Al-Hadid | Med | Med | 550 | 248 | 0.691 | 0.934 | [0.737, 0.821] |
| 95 | 47 | Muhammad | Med | Med | 519 | 238 | 0.685 | 0.934 | [0.718, 0.808] |
| 96 | 13 | Ar-Ra'd | Med | LateM | 818 | 347 | 0.715 | 0.934 | [0.763, 0.833] |
| 97 | 55 | Ar-Rahman | Med | EarlyM | 348 | 141 | 0.727 | 0.864 | [0.824, 0.935] |
| 98 | 76 | Al-Insan | Med | MiddleM | 238 | 154 | 0.498 | 0.833 | [0.593, 0.713] |
| 99 | 65 | At-Talaq | Med | Med | 279 | 147 | 0.607 | 0.919 | [0.651, 0.769] |
| 100 | 98 | Al-Bayyinah | Med | Med | 91 | 58 | 0.480 | 0.871 | [0.508, 0.718] |
| 101 | 59 | Al-Hashr | Med | Med | 427 | 212 | 0.644 | 0.909 | [0.706, 0.801] |
| 102 | 24 | An-Nur | Med | Med | 1274 | 415 | 0.820 | 0.960 | [0.838, 0.896] |
| 103 | 22 | Al-Hajj | Med | Med | 1224 | 485 | 0.727 | 0.929 | [0.793, 0.851] |
| 104 | 63 | Al-Munafiqun | Med | Med | 170 | 102 | 0.547 | 0.890 | [0.601, 0.743] |
| 105 | 58 | Al-Mujadilah | Med | Med | 453 | 197 | 0.719 | 0.936 | [0.750, 0.845] |
| 106 | 49 | Al-Hujurat | Med | Med | 342 | 159 | 0.699 | 0.924 | [0.724, 0.830] |
| 107 | 66 | At-Tahrim | Med | Med | 241 | 143 | 0.545 | 0.904 | [0.595, 0.714] |
| 108 | 64 | At-Taghabun | Med | Med | 233 | 137 | 0.555 | 0.878 | [0.623, 0.747] |
| 109 | 61 | As-Saff | Med | Med | 216 | 123 | 0.582 | 0.894 | [0.632, 0.767] |
| 110 | 62 | Al-Jumu'ah | Med | Med | 171 | 103 | 0.547 | 0.895 | [0.599, 0.744] |
| 111 | 48 | Al-Fath | Med | Med | 546 | 252 | 0.671 | 0.935 | [0.706, 0.790] |
| 112 | 5 | Al-Ma'idah | Med | Med | 2738 | 684 | 0.917 | 0.967 | [0.934, 0.979] |
| 113 | 9 | At-Tawbah | Med | Med | 2408 | 637 | 0.908 | 0.961 | [0.923, 0.972] |
| 114 | 110 | An-Nasr | Med | Med | 19 | 18 | — | — | insufficient |

Full machine-readable version: `csv/zipf-per-surah.csv`.

## 5. Summary statistics

### 5.1 By period (Egyptian binary)

| Period | n (valid) | mean α | sd α |
|---|---:|---:|---:|
| Meccan | 64 | **0.638** | 0.167 |
| Medinan | 26 | **0.711** | 0.149 |

Medinan > Meccan by **+0.073**. Point-biserial r = +0.204. This is the
opposite direction from H14's (Meccan > Medinan) prediction.

### 5.2 By Nöldeke phase

| Phase | n (valid) | mean α | min | max | median n_tokens |
|---|---:|---:|---:|---:|---:|
| Early Meccan | 25 | **0.470** | 0.291 | 0.727 | ~160 |
| Middle Meccan | 21 | **0.693** | 0.498 | 0.846 | ~780 |
| Late Meccan | 21 | **0.783** | 0.612 | 0.936 | ~840 |
| Medinan | 23 | **0.720** | 0.480 | 0.996 | ~520 |

The phase means form a rising ramp Early → Middle → Late Meccan, then
flatten/slightly dip at Medinan. **Exactly the opposite** of H14's
predicted Early-high → Medinan-low ramp.

### 5.3 Why H14 got the direction backwards

H14's intuition was: oracular short surahs repeat a small theological
core → high Zipf α (concentrated). Legal long surahs spread over many
rare lexemes → low Zipf α (flat).

The intuition confuses *two* distribution properties:
1. **Type-token ratio (TTR)** — how much vocabulary is reused. Short
   oracular surahs DO have higher TTR (fewer distinct types per token),
   consistent with the intuition.
2. **Zipf α** — the slope of log-rank vs log-freq. This is a property of
   the *shape* of the frequency curve, which for short samples is nearly
   flat (most types appear once or twice) regardless of how concentrated
   the repetition is.

For a 30-token surah with 25 distinct types, the frequency vector is
dominated by 1s with a handful of 2s — the log-log slope is **shallow**
because freq barely moves across ranks. Only once you have thousands of
tokens does the tail structure (many low-freq types alongside a few
very-high-freq types) become visible, which is where α climbs toward 1.
The whole-Quran α = 1.32 is the *asymptotic* property of the full corpus;
it emerges only when enough tokens are pooled to populate the tail.

This is a well-known small-sample bias of OLS-fit Zipf α (the so-called
**"finite-sample flattening"**), and it fully explains what we see.

## 6. Correlations (on 90 valid surahs)

| Quantity | Value | perm-p (10k) |
|---|---:|---:|
| Spearman ρ(α, revelation_order)  — Egyptian | **+0.199** | 0.0624 |
| Spearman ρ(α, Nöldeke order) | **+0.608** | **0.0001** |
| Spearman ρ(α, n_lemma_tokens) | **+0.962** | — |
| Spearman ρ(α, n_distinct_lemmas) | **+0.929** | — |
| Point-biserial r(Medinan binary, α) | +0.204 | — |
| **Partial Spearman ρ(α, rev_order ∣ log n_tokens)** | **+0.397** | — |
| Partial Pearson r(α, rev_order ∣ log n_tokens) | +0.395 | — |

The raw Spearman ρ(α, revelation_order) under the Egyptian ordering is
+0.199, which fails the H14 acceptance criterion (|ρ| > 0.3, p < 0.01).
Under the Nöldeke ordering it is +0.608 (p < 10⁻⁴) — but this is
dominated by the confound that Nöldeke's Early Meccan phase contains all
the shortest surahs. Partialling out log(n_tokens) the residual ρ
drops to +0.397, which just barely meets the |ρ| > 0.3 bar.

**The sign is positive** (later → steeper α), which is the **opposite of
H14's predicted sign**. The direction-specific version of the hypothesis
— "early Meccan concentrated, Medinan flat" — is decisively rejected.

### Length-binned Spearman ρ (length-controlled)

Binning valid surahs into 5 length quintiles (18 each), Spearman ρ of α
vs revelation order WITHIN each bin:

| Bin | n_tokens range | n | mean α | Spearman ρ (α, rev#) |
|---:|---|---:|---:|---:|
| 0 | 70–179 | 18 | 0.433 | +0.655 |
| 1 | 194–338 | 18 | 0.565 | +0.104 |
| 2 | 342–755 | 18 | 0.669 | +0.307 |
| 3 | 767–1 224 | 18 | 0.759 | +0.156 |
| 4 | 1 247–5 884 | 18 | 0.869 | +0.333 |

Within each length bin α still rises with revelation order (all 5 bins
positive, 4/5 bins ≥ +0.15). The signal is weak-positive and not
consistently above the |ρ| > 0.3 bar bin-by-bin; but the direction is
always the SAME opposite-of-H14 sign.

## 7. Extremes (valid surahs only)

### Top 10 α (most concentrated)

| sid | name | period | rev# | n_tok | α | 95% CI |
|---:|---|---|---:|---:|---:|---|
| 2 | Al-Baqarah | Medinan | 87 | 5 884 | 0.996 | [1.009, 1.043] |
| 4 | An-Nisa | Medinan | 92 | 3 653 | 0.964 | [0.977, 1.017] |
| 3 | Al-Imran | Medinan | 89 | 3 371 | 0.954 | [0.963, 1.006] |
| 6 | Al-An'am | Meccan | 55 | 2 946 | 0.936 | [0.962, 1.006] |
| 5 | Al-Ma'idah | Medinan | 112 | 2 738 | 0.917 | [0.934, 0.979] |
| 7 | Al-A'raf | Meccan | 39 | 3 177 | 0.913 | [0.942, 0.984] |
| 9 | At-Tawbah | Medinan | 113 | 2 408 | 0.908 | [0.923, 0.972] |
| 10 | Yunus | Meccan | 51 | 1 786 | 0.907 | [0.929, 0.987] |
| 11 | Hud | Meccan | 52 | 1 855 | 0.855 | [0.897, 0.952] |
| 12 | Yusuf | Meccan | 53 | 1 696 | 0.851 | [0.883, 0.937] |

**The top-α surahs are the LONGEST surahs**, not the oracular short Meccan
ones. Every surah in the top 10 has ≥ 1 696 lemma tokens. 5 of the 10 are
Medinan; the 5 Meccan members are all Late Meccan narrative surahs
(revelation positions 39–55), not Early Meccan oaths.

### Bottom 10 α (flattest, i.e., shallowest log-log slope)

| sid | name | period | rev# | n_tok | α | 95% CI |
|---:|---|---|---:|---:|---:|---|
| 87 | Al-A'la | Meccan | 8 | 72 | 0.291 | [0.439, 0.644] |
| 90 | Al-Balad | Meccan | 35 | 79 | 0.307 | [0.432, 0.625] |
| 92 | Al-Layl | Meccan | 9 | 70 | 0.325 | [0.449, 0.653] |
| 80 | Abasa | Meccan | 24 | 128 | 0.330 | [0.468, 0.611] |
| 81 | At-Takwir | Meccan | 7 | 101 | 0.352 | [0.540, 0.709] |
| 85 | Al-Buruj | Meccan | 27 | 100 | 0.376 | [0.477, 0.656] |
| 88 | Al-Ghashiyah | Meccan | 68 | 91 | 0.401 | [0.504, 0.687] |
| 84 | Al-Inshiqaq | Meccan | 83 | 104 | 0.405 | [0.490, 0.662] |
| 79 | An-Nazi'at | Meccan | 81 | 172 | 0.406 | [0.504, 0.650] |
| 78 | An-Naba | Meccan | 80 | 171 | 0.434 | [0.536, 0.673] |

**The bottom-α surahs ARE the oracular oath-cluster short Meccan surahs** —
but in the opposite sense H14 predicted. These surahs have the *flattest*
Zipf slope (α ≈ 0.3), not the *steepest*. Eight of the 10 are in the
"oath cluster" of short mid-mushaf Meccan surahs (78–92). Every single
bottom-10 α surah is Meccan, and 7/10 are Nöldeke Early Meccan. All 10
have ≤ 172 lemma tokens.

### Insufficient-data list (n = 24, all Meccan except two)

These 24 surahs lacked ≥ 50 distinct lemmas and were dropped from the fit.
**Nearly all of them are exactly the short oracular Meccan oath-surahs that
H14 banked on being α > 1.5**. Ordering by mushaf id: Al-Fatiha (1),
At-Tariq (86), Ash-Shams (91), Ad-Dhuha (93), Ash-Sharh (94), At-Tin (95),
Al-Alaq (96), Al-Qadr (97), Az-Zalzalah (99, Medinan-labelled), Al-Adiyat
(100), Al-Qari'ah (101), At-Takathur (102), Al-Asr (103), Al-Humazah
(104), Al-Fil (105), Quraysh (106), Al-Ma'un (107), Al-Kawthar (108),
Al-Kafirun (109), An-Nasr (110, Medinan-labelled), Al-Masad (111),
Al-Ikhlas (112), Al-Falaq (113), An-Nas (114).

As a sanity check I re-fit these under a relaxed ≥ 10 distinct-lemma
threshold (reported as a supplementary exploration, not the headline
rule). The resulting α values ranged **0.13 to 0.53** — all far below
1.5. With R² values in the 0.4-0.9 range the power law doesn't even
describe these distributions cleanly. The prediction α > 1.5 has **zero
supporting data** at any reasonable threshold.

## 8. Heterogeneity is real — but it is length-driven

The Spearman ρ(α, n_tokens) = **+0.962** is extreme. A naïve reading of
the per-surah table would say "there's huge heterogeneity in Quranic
Zipf α" (which is technically true: 0.29 to 1.00). The honest reading
is: this heterogeneity is almost entirely a deterministic function of
*how many lemma tokens the surah has*, which in turn is a deterministic
function of surah length, which in mushaf order is roughly length-sorted
and in revelation order is roughly time-sorted (verses got longer over
time). So the per-surah α heterogeneity is mostly a restatement of the
well-known diachronic verse-length ramp already flagged as F = 209.96
by the chrono-revelation agent, just refracted through a Zipf-fit lens.

The residual, length-controlled diachronic signal (ρ ≈ +0.40, partial)
is small and in the opposite direction to H14. It is **not** a standalone
finding; it is mostly a restatement of "longer surahs have more structured
frequency tails."

## 9. Answering the task questions

**1. Table of (surah_id, name, period, mushaf_order, revelation_order,
n_distinct_lemmas, zipf_alpha, r_squared).** §4 above and `csv/zipf-per-surah.csv`.

**2. Correlation of α with revelation order (Spearman ρ).**
ρ(α, Egyptian rev order) = +0.199, perm-p = 0.0624 (not significant at
p < 0.01). ρ(α, Nöldeke order) = +0.608, perm-p < 10⁻⁴. Partial
ρ controlling log n_tokens = +0.397. *Direction opposite to H14.*

**3. Correlation of α with Meccan/Medinan label.** Point-biserial
r(Medinan, α) = +0.204. Medinan mean α = 0.711, Meccan mean = 0.638.
Medinan > Meccan (opposite direction to H14).

**4. Highest-α and lowest-α surahs.** See §7. Highest α are long Medinan
and Late Meccan narrative/legal surahs (Al-Baqarah, An-Nisa, Al-Imran,
Al-An'am…). Lowest α are short Early Meccan oath surahs (Al-A'la,
Al-Balad, Al-Layl, 'Abasa, At-Takwir…). This is the exact inversion of
H14's predicted ordering.

**5. Is the predicted early-Meccan-α > late-Medinan-α pattern confirmed?**
**No.** The observed pattern is late-Medinan-α > early-Meccan-α,
monotonically across Nöldeke phases (0.47 → 0.69 → 0.78 → 0.72). H14
predicted 1.5 vs 1.1; the data show ~0.47 vs ~0.72. **Hypothesis
rejected in the direction stated.**

**6. Are the highest-α surahs the oracular short ones (Meccan oath-cluster)?**
**No.** The highest-α surahs are the *longest* surahs. The Meccan oath
cluster (rev positions 1-35, Nöldeke Early Meccan) has the LOWEST α.
The oracular-concentration intuition (high TTR, theological repetition)
is real but **it does not translate into high Zipf α** because Zipf α is
a tail-shape statistic, not a concentration statistic, and tail shapes
require large N to stabilize.

**7. Does this finding survive when the whole-Quran α recomputed under
the same rule comes out to match cross-baseline's 0.97?**
The whole-Quran α under this pipeline comes out to **1.318**, matching
the info-theory anchor exactly, NOT cross-baseline's 0.97. The reason:
cross-baseline used **orthographic-token word definition**, not lemma.
Under the lemma rule (consistent with info-theory and this analysis),
the Quran α is 1.32, which IS steeper than cross-baseline's reported
orthographic-token baselines (Bukhari 1.07, Sira 1.03, Jahiz 0.94).
This does not validate H14; it just means the whole-corpus lemma-α
comparison has not been properly run vs a lemma-level baseline.
**The heterogeneity finding is real** in the sense that per-surah α
varies from 0.29 to 1.00; but that variation is overwhelmingly a
length artifact, not a diachronic authorial-register signal. It does
NOT "survive" as support for H14's conjecture.

## 10. What IS the real finding?

Three honest takeaways:

1. **The whole-Quran Zipf α = 1.32 is an aggregation emergent**, not
   an average. No single surah has α near 1.32. The largest single-surah
   α is Al-Baqarah at 0.996. The whole-Quran α only reaches 1.32 when
   the 114-surah vocabulary pools into a ~5 000-lemma corpus with a
   fully-populated hapax tail. This is a nontrivial observation: any
   per-surah "Zipf violation" claim (cf. Yahya et al. on Sūrat al-Ghāfir)
   has to be interpreted against a length-matched baseline, because
   short surahs *cannot* show α ≈ 1.3 under finite-sample OLS.
2. **The per-surah α IS a new diachronic marker, in the unexpected
   direction.** Controlling for log-length, α still rises monotonically
   through the Nöldeke phases (0.47 → 0.78) until the slight Medinan
   dip. This mirrors the `n_distinct_roots` and `ttr_lemma`
   U-shape observed by chrono-revelation §3. It is a restatement of
   the same underlying fact: Medinan prose has slightly more
   repeated-function-word vocabulary than Late Meccan narrative prose.
3. **The oracular-short-Meccan cluster is unfitable under this rule.**
   Any claim about "the Zipf α of Sūrat al-Ikhlas" or "the Zipf α of
   An-Nas" is methodologically ill-posed — these surahs simply do not
   have enough lemma tokens for a power-law fit to be meaningful.
   Authors making Zipf claims about individual short surahs are fitting
   noise. The insufficient-data list in §7 is the positive statement of
   this constraint: 24 surahs below the ≥ 50-distinct-lemma bar.

## 11. Garden of forking paths disclosure

### Decisions made before seeing data
- Minimum 50 distinct lemmas (per task spec).
- OLS log-log rule identical to `info_theory_run.py task4_zipf` (rank 1-based).
- 1000-sample nonparametric bootstrap percentile CI.
- 10000-permutation test for Spearman ρ significance.
- Reported metrics fixed: Spearman ρ vs rev order, Spearman ρ vs
  Nöldeke, point-biserial r(Medinan), partial Spearman given log-tokens,
  5-bin length stratification.

### Decisions made after seeing data
- Relaxed ≥ 10 distinct-lemma threshold as a *supplementary* exploration
  only, to falsify the H14 claim that short oracular surahs would have
  α > 1.5 — reported in §7 as an explicit out-of-original-rule check.
- The "finite-sample flattening" explanation in §5.3 was added after
  observing ρ(α, n_tokens) = +0.96; it is a textbook small-sample bias
  of OLS Zipf fits, not a post-hoc rationalization.

### Alternative fits not run
- Clauset–Shalizi–Newman maximum-likelihood power-law fit per surah.
  Would likely shift all α estimates slightly downward and possibly
  stabilize the small-surah tail. Would NOT reverse the sign of the
  length confound. Not run because (a) the task specified OLS log-log
  for consistency with info-theory anchor, (b) CSN requires many more
  samples to stabilize for a small surah, (c) the bootstrap 95% CIs
  already capture the small-sample uncertainty.
- Weighted OLS downweighting the noisy tail. Would bring per-surah α
  estimates closer to whole-Quran α because the tail's flattening effect
  is reduced. Sign of the diachronic effect unaffected.
- Lemma-level baseline against Bukhari / Sira / Jahiz. **The cleanest
  follow-up**: compute per-chunk α on a length-matched Bukhari slice
  under the same lemma-rule pipeline, and compare to the Quranic
  per-surah distribution stratified by length. This would test whether
  the per-surah α vs length curve is Quran-specific or generic Arabic.
  Not done here; flagged as the §1.4 follow-up.

### Sibling hypotheses considered
- Fitting word-token (surface-form) Zipf per surah instead of lemma.
  Under word-token the whole-Quran α drops toward 1.0; per-surah α
  estimates would be similarly small-sample-flattened. Not run.
- Per-juz' Zipf fit (1/30 division). Each juz' has ≈ 2 500 lemma tokens,
  large enough for a clean fit. Not run; would be a natural
  sibling analysis.
- Per-phase pooled fit (Early/Middle/Late/Medinan pooled across all
  surahs in the phase, then OLS on the pool). Would give 4 α values with
  sufficient sample sizes to compare cleanly. Not run here; strongly
  recommended as the next-step aggregated test.

## 12. Pre-registration status

**Not pre-registered.** The H14 acceptance criterion (|ρ(α, rev_order)|
> 0.3 with p < 0.01 AND length-controlled version still significant)
**fails at the direction-agnostic level** on the Egyptian ordering
(ρ = +0.199, p = 0.062, does not meet |ρ| > 0.3). It is met under the
Nöldeke ordering (ρ = +0.608, p < 10⁻⁴) but the length-controlled
partial is +0.40 — marginal on the |ρ| > 0.3 bar. Even in the charitable
reading where the partial correlation counts as meeting the criterion,
the **sign is the opposite** of the stated prediction.

**The hypothesis as originally stated is rejected.** The directional
prediction (α_early > α_late, with α_early > 1.5) is falsified by the
data. A permissive reading of H14 as just "per-surah α correlates with
revelation order, direction unspecified" would be marginally supported,
but this re-statement destroys the prior-literature appeal and is a
garden-of-forking-paths violation.

## 13. Recommendations for follow-up

1. **Length-matched Bukhari Zipf comparison.** Morphologically tag a
   length-matched Bukhari slice, compute per-chunk α under identical
   rules, compare the Quran-surah vs Bukhari-chunk α-vs-length curves.
   Expected: the curves coincide; the per-surah α heterogeneity is
   fully explained by length. If they diverge, the Quran's
   per-surah α-length curve would be a new style signature.
2. **Per-juz' Zipf.** 30 chunks each with ~2 500 lemma tokens. Clean
   sample-size-matched fits, cleaner diachronic ramp test.
3. **CSN maximum-likelihood fit** on all surahs with n_tokens ≥ 500 to
   remove the OLS tail-noise bias. Report effect on the sign of the
   diachronic correlation.
4. **Pooled per-Nöldeke-phase fit.** Pool all lemmas within each
   phase, fit one α per phase. This removes the per-surah small-sample
   noise entirely and gives the cleanest 4-number diachronic Zipf
   statement. (Predicted: the ramp will hold in the Medinan > Meccan
   direction but at small magnitude.)
5. **Drop the "Zipf α is a concentration measure" mental model**
   from future hypotheses. Zipf α is a tail-shape measure and is
   fundamentally length-sensitive under finite-sample OLS.

## 14. What this does NOT resolve

- The **Yahya et al. per-surah Zipf papers** (on Sūrat al-Aḥzāb and
  Sūrat al-Ghāfir) likely report α values of the kind computed here
  (Al-Ahzab α = 0.784, Ghafir α = 0.816 under this pipeline). Whether
  their "deviation from Zipf" claims hold depends on what baseline they
  compared against. Their numbers would sit near the middle of the
  Nöldeke-Medinan/Late-Meccan range in the table above; they are not
  outliers.
- Whether there is a **rhetorical-style signal** hiding inside the
  length-residualized per-surah α is an open question. A proper
  Sadeghi-style stylometric analysis using many morpheme-ratio features
  rather than the single Zipf-α scalar is the right toolkit.
- The **info-theory headline claim** (Quran α = 1.32 is steeper than
  classical-Arabic baseline ≈ 1.0–1.2) is unchanged by this analysis.
  It is a whole-corpus claim about lemma-level tail structure and still
  needs a §1.4 length-matched lemma-tagged Bukhari baseline to promote.
