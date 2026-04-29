---
id: H-NEW-43
title: Corpus-Wide Verse-Length FFT
status: EXECUTED (amendments 43-A, 43-B applied)
verdict: NULL-BROKEN (AR(1) null disqualified by Ljung-Box lag-10)
registered: 2026-04-15
executed: 2026-04-15
bonferroni_family: 2026-04-15-Fresh-Wave-3
bonferroni_k_inner: 13
alpha_cell_inner: 1.28e-3
alpha_bon_outer: 0.0167
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
seed: 20260415
n_surrogates: 10000
primary_corpus: quran-text/quran-no-tashkeel.json
amendments_applied:
  - 43-A (inner k=13, alpha_cell=1.28e-3) already the in-script value; no effect on outcome
  - 43-B (AR(1) Ljung-Box lag-10 gate)
---

# [[h-new-43-verse-length-fft|H-NEW-43]] — Corpus-Wide Verse-Length FFT — Results

## Pre-reg and amendments

See `findings/phase-b-hypotheses/h-new-43-verse-length-fft-prereg.md`, §AMENDMENTS (post-audit-032, 2026-04-15). Both amendments are pre-execution, tightening-only.

- **43-A**: alpha_cell = 1.28e-3 (Bonferroni inner k=13 = 3 directed + 10 undirected). Already the value used; no effect on outcome.
- **43-B**: AR(1) fit residuals MUST pass Ljung-Box at p>0.05 at lag 10. If fail → NULL-BROKEN. No post-hoc switch to AR(2).

## Verdict

**NULL-BROKEN.**

### AR(1) fit diagnostic (Quran, primary)

- phi = 0.1276, sigma_eps = 30.156 on per-surah-demeaned L (N=6,236).
- **Ljung-Box Q(lag=10, df=9) = 59.99, p = 1.35e-9.**
- Pre-committed threshold: p > 0.05. Observed p ≪ 0.05 by nine orders of magnitude.

**Decision (amendment 43-B):** AR(1) residuals are NOT white noise. The AR(1) model does not capture the serial-correlation structure of the verse-length signal. Under the pre-committed amendment, the AR(1) null is disqualified. No post-hoc switch to AR(2) is permitted within this test.

The primary spectral test therefore yields **NULL-BROKEN** — not because of a positive-control failure, but because the red-noise null model is demonstrably wrong for this signal.

### Positive control (MW-5): PASS (unaffected)

Sinusoid injected at f0=0.01 into AR(1)-matched red noise detected at z=33.90, p<1e-4. The periodogram and surrogate machinery are correct. What is disqualified is the *applicability* of AR(1) as a null for this particular signal, not the pipeline implementation.

### Baseline AR(1) diagnostics

| corpus | AR(1) phi | Ljung-Box Q (lag 10) | p | pass? |
|---|---:|---:|---:|:---:|
| Quran       | 0.128 |    59.99 | 1.35e-9   | no |
| Bukhari     | 0.166 | 1,149.83 | 8.19e-242 | no |
| Jahiz       | 0.215 |   693.63 | 1.62e-143 | no |
| Muallaqat*  | 0.720 |   936.94 | 6.76e-196 | no |

(*Muallaqat is periodic-tiled 8× from 792 verses; strong serial correlation is an artefact of tiling.)

All four corpora reject AR(1)-whiteness. The Quran's rejection is orders of magnitude less severe (Q≈60 vs Q≈700–1,150 for prose/poetry) — consistent with the Quran being closer to AR(1)-white than matched-Arabic — but "closer" is not "close enough" under the pre-committed threshold.

## Peak tables (reported for transparency; NOT used for verdict because null disqualified)

### Top-10 undirected peaks

| rank | k | period (verses) | freq | amplitude | z (vs AR(1)) | p | at alpha_cell=1.28e-3? |
|-----:|----:|---:|---:|---:|---:|---:|:---:|
| 1 | 71 | 87.83 | 0.01139 | 7,267.6 | 5.05 | 2.4e-3 | no |
| 2 | 287 | 21.73 | 0.04602 | 6,725.5 | 4.65 | 3.6e-3 | no |
| 3 | 472 | 13.21 | 0.07569 | 6,608.9 | 4.64 | 3.5e-3 | no |
| 4 | 970 | 6.43 | 0.15555 | 6,341.7 | 5.04 | 2.7e-3 | no |
| 5 | 2563 | 2.43 | 0.41100 | 6,225.7 | 7.52 | 1.0e-4 | yes (under disqualified null) |
| 6 | 114 | 54.70 | 0.01828 | 6,191.1 | 4.12 | 5.4e-3 | no |
| 7 | 291 | 21.43 | 0.04667 | 6,163.9 | 4.22 | 5.4e-3 | no |
| 8 | 545 | 11.44 | 0.08740 | 5,922.3 | 4.23 | 6.5e-3 | no |
| 9 | 630 | 9.90 | 0.10102 | 5,771.4 | 4.14 | 6.1e-3 | no |
| 10 | 168 | 37.12 | 0.02694 | 5,714.7 | 3.81 | 8.9e-3 | no |

These z-scores are computed under the disqualified AR(1) null. They are reported for transparency but do NOT contribute to any PASS/NULL decision because the null failed its pre-committed goodness-of-fit threshold.

### Directed-frequency cells (1/7, 1/14, 1/21, 1/34, 1/57)

| name | target f | target k | k* argmax | period | amp | z (window-corrected) | p | at alpha_cell? |
|---|---:|---:|---:|---:|---:|---:|---:|:---:|
| 1/7 manzil     | 0.1429 | 891 | 970 | 6.43  | 6,341.7 | 0.17 | 3.65e-1 | no |
| 1/14           | 0.0714 | 445 | 472 | 13.21 | 6,608.9 | 0.52 | 2.51e-1 | no |
| 1/21 Fibonacci | 0.0476 | 297 | 287 | 21.73 | 6,725.5 | 0.81 | 1.80e-1 | no |
| 1/34 Fibonacci | 0.0294 | 183 | 168 | 37.12 | 5,714.7 | 0.46 | 2.65e-1 | no |
| 1/57 bipartite | 0.0175 | 109 | 114 | 54.70 | 6,191.1 | 1.21 | 1.13e-1 | no |

All directed frequencies are null even under the now-disqualified AR(1) reference. No pre-registered classical rhythm (manzil 1/7, bipartite 1/57, Fibonacci 1/21 or 1/34) emerges.

## Interpretation of NULL-BROKEN

A NULL-BROKEN verdict means **this particular test cannot answer the original question**. It does NOT say there is or is not rhythmic structure in the Quran verse-length series. The finding is purely that:

1. The AR(1) red-noise null, pre-committed as the primary null, is a poor fit to the Quran verse-length residuals (p≈1e-9 against whiteness).
2. Under the pre-committed integrity standard (amendment 43-B), we do not rescue this by switching to AR(2) inside this test.
3. Any future [[h-new-43-verse-length-fft|H-NEW-43]].x that uses AR(2), higher-order AR, or a non-parametric (block-bootstrap, phase-randomisation) null must be separately pre-registered.

Honest reading: AR(1) is empirically too simple for this signal. Something beyond single-lag serial correlation is present. Whether it is the pre-registered classical rhythms, general non-stationarity across surahs, a per-surah serial-correlation structure not removed by per-surah demean, or something else, is not determinable within this pre-reg.

The exploratory k=2563 peak (period≈2.43 verses, z=7.52 under AR(1)) does not carry weight under the amended verdict: the reference null is wrong, so its z-score is not interpretable. It remains a candidate for follow-up under a properly specified null.

## Pre-committed verdict rows

| row | met? |
|---|:---:|
| Positive control not detected → NULL-BROKEN | no (PASS) |
| AR(1) Ljung-Box lag-10 p ≤ 0.05 → NULL-BROKEN (amendment 43-B) | **YES** |
| ≥1 directed hit at alpha_cell=1.28e-3 → DIRECTED-PASS | moot |
| ≥3 undirected peaks at alpha_cell AND > baseline max → EXPLORATORY-PASS | moot |
| 0 peaks at alpha_cell → NULL | moot |

**Controlling row: amendment 43-B Ljung-Box failure → NULL-BROKEN.**

## Integrity

Full periodogram (amplitudes and null-99th percentiles across all retained bins) at `findings/phase-b-hypotheses/csv/h-new-43-periodogram.csv`. Full JSON (peak tables, AR(1) diagnostics including Ljung-Box, baselines, positive control) at `findings/phase-b-hypotheses/csv/h-new-43.json`. Script at `scripts/h_new_43_verse_length_fft.py`. Seed 20260415. Amendments 43-A and 43-B applied before viewing any numeric result.

## Follow-up recommendation (NOT a re-verdict)

A separate pre-reg H-NEW-43.2 could propose:
- AR(p) null with p selected by AIC on residuals, with its own Ljung-Box gate.
- Non-parametric phase-randomisation null (preserves full power spectrum shape).
- Block-bootstrap with block length matched to per-surah autocorrelation decay.

Any of these would be a different test and MUST be pre-registered before execution with its own Bonferroni family accounting.
