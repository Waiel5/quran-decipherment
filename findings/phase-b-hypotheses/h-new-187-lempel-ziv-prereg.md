---
id: H-NEW-187
title: Lempel-Ziv complexity per surah; comparison with H-NEW-15 gzip
phase: B
status: PRE-REG
date: 2026-04-17
specialist: autonomous-agent
parent: H-NEW-15 (gzip compression signals); sibling to H-NEW-159 (Heap β), H-NEW-172 (Zipf α), H-NEW-163 (dispersion)
seed: 20260419
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan)
bonferroni_k_primary: 2
alpha_family: 0.05
alpha_bon_primary: 0.025
---

# [[h-new-187-lempel-ziv|H-NEW-187]] — Pre-registration

## Motivation

H-NEW-15 established per-surah gzip compression ratios, with clear signal (Ar-Raḥmān, Al-Mursalāt, Al-Qamar as outliers). gzip is a dictionary-based compressor; its compressibility signal confounds regular repetition with local-n-gram frequency. Lempel-Ziv-76 complexity (Lempel & Ziv 1976) is a **different** complexity measure: count of distinct phrases in a left-to-right parsing. Normalized LZ approaches Kolmogorov complexity for long sequences under mild conditions. Pure-math LZ complexity has well-understood asymptotics; unlike gzip, it lacks Huffman-coding layer.

**Question**: Does LZ complexity per surah (a) track gzip (same underlying "compressibility" axis) or (b) diverge (different axis)?

## Method

### Data
- Input: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (whitespace-normalized concatenation of verses per surah)
- Bukhārī: `/Users/grey/Downloads/quran/data/baseline-corpora/raw/bukhari-noquran.txt` (4.6 MB, ~526k tokens)

### Per-surah LZ complexity (primary unit of analysis)
1. Normalize whitespace (single spaces, strip).
2. Compute LZ76 phrase-count `c(s)` using standard algorithm (Lempel & Ziv 1976).
3. Normalized LZ complexity: `LZ_norm = c(s) / n` where n is character length. (Not multiplied by log n here; we want a proportion-style score per-length.) Also compute Lempel-Ziv-76 normalization `c log n / n` for completeness.
4. Rank all 114 surahs by `LZ_norm` ascending (lowest = most compressible / most repetitive).

### Primary tests (Bonferroni k=2, α_primary=0.025)

**P1: Correlation of LZ_norm with existing complexity axes**
- Spearman ρ(LZ_norm, gzip_ratio) — expected high correlation (~ +0.8 or more) since both measure compressibility; significance signals they measure the same axis.
- Spearman ρ(LZ_norm, Heap β) — if LZ captures vocabulary-growth profile, expect + correlation (high β = many new items = less repetition = higher LZ_norm).
- Spearman ρ(LZ_norm, Zipf α) — high α = steep distribution = more concentration on top types = more repetition → negative correlation expected.
- Spearman ρ(LZ_norm, dispersion) — if dispersion measures vocabulary-even-ness, + correlation.

A **PASS on P1** requires Spearman ρ(LZ_norm, gzip_ratio) ≥ +0.7 with p < 0.025 (Bonferroni primary). This validates that LZ captures the same compressibility axis that gzip does. The other three correlations are secondary/descriptive (not Bonferroni-tested against α/β/dispersion directly; those are reported at nominal).

**P2: Quran vs Bukhārī distinctness**
- Compute LZ_norm for each surah (n=114) and for 114 length-matched contiguous chunks of Bukhārī.
- Matching procedure: for each surah, sample a contiguous character-range from Bukhārī with the same length (±1%). Compute LZ_norm on that chunk.
- Repeat for seed 20260419; produce 114 LZ_norm values for Quran, 114 for Bukhārī.
- Test: Mann-Whitney U (two-sided) on LZ_norm distributions.
- **PASS on P2** requires Mann-Whitney U p < 0.025 (Bonferroni primary).

### Secondary descriptive
- Muq vs non-muq: Welch's t-test on LZ_norm (nominal α=0.05, not Bonferroni).
- Top-10 lowest LZ_norm surahs (most-compressible).
- Visual: LZ_norm vs gzip_ratio scatter; flag outliers.

### MW-5 sanity check
- **Synthetic random string**: 10,000 chars uniform from 28-letter alphabet; compute LZ_norm. Expected near-maximum (~1).
- **Synthetic repeating pattern**: 10,000 chars of "abcabcabc..." pattern; compute LZ_norm. Expected very low (~0.01).
- MW-5 PASS: LZ_norm(random) > LZ_norm(repeating) by at least 10×.

## Decision rules

- **PASS BOTH P1 & P2**: Headline = LZ complexity is a valid second compressibility axis, co-linear with gzip, and Quran vs Bukhārī differ in LZ complexity.
- **PASS P1 only**: LZ tracks gzip but doesn't separate Quran/Bukhārī.
- **PASS P2 only**: LZ captures a different signal than gzip; Quran/Bukhārī separate on this new axis.
- **FAIL both**: LZ complexity adds no new information.

## Outputs

- `findings/phase-b-hypotheses/h-new-187-lempel-ziv.md` — results
- `findings/phase-b-hypotheses/csv/h-new-187-per-surah.csv`
- `findings/phase-b-hypotheses/csv/h-new-187.json`
- Script: `scripts/h_new_187_lempel_ziv.py`

## Garden of forking paths

Choices locked before execution:
- LZ76 algorithm (standard, reference implementation in existing `compression_self_ref.py`)
- Character-level analysis (not token-level) — matches gzip's byte-level measurement
- Normalization = c/n (simple) + c log n / n (LZ76 standard) both reported; **primary is c/n** as this is the most direct "phrases per character" measure
- Null for Quran vs Bukhārī: length-matched contiguous chunks, seed 20260419
- Bonferroni k=2 (only 2 pre-declared primary tests)
- Correlation method: Spearman (non-parametric, robust to non-linearity)

No peeking: results below this line are post-hoc commentary.
