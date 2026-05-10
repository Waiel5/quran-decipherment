---
prereg_id: Q043-F-08
title: zukhruf (z-kh-r-f) corpus rank — full attestation inventory and per-surah rank
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q043-F-08 — *zukhruf* root corpus rank inventory

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The root **z-kh-r-f** (Buckwalter `zxrf`) appears in *exactly 4 attestations* across the entire Quranic corpus, distributed across *exactly 4 surahs* (one attestation each). The corpus-rank of Q 43 by raw count is **tied at 1** with three other surahs. By density-per-1000-tokens, Q 43's rank is **>1** (i.e., not the densest) because Q 43 is one of the larger HM surahs.

This extends Q043-F-04 (which tested the rank-by-density only) by providing the full attestation table and verifying both the count and density rankings.

## 2. Null / negation

**H0**: The `zxrf` root appears in fewer or more than 4 attestations, OR in fewer/more than 4 surahs, OR Q 43 is the unique rank-1 by both count and density.

## 3. Operationalization

- Source: `data/morphology/root-index.json` (QAC v0.4 root-attestation index).
- Target key: `zxrf`.
- Per-surah token counts: from `quran-text/quran-no-tashkeel.json`.
- Compute: per-surah count, density per 1000 tokens, corpus rank by each.

## 4. Direction lock

- Total corpus attestations of `zxrf` = **4** (pre-committed exact).
- Surahs with ≥1 `zxrf` attestation = **4** (pre-committed exact).
- Q 43 count rank = **tied-1**.
- Q 43 density rank = **>1**.

## 5. Bonferroni

Member of Q 43 novel-findings family (k=3 in this batch). α_corrected = 0.0167. Test is exact-count.

## 6. Success / failure criteria

- **VINDICATED**: all four predictions hold exactly.
- **NULL_OR_DISCREPANCY**: any disagreement.

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q043-F-08.json`: corpus_total, surahs_with_attestation (full list), per_surah_counts, per_surah_densities, q43_count_rank, q43_density_rank, top_density_surahs (top-5), verdict.

## 9. Rationale

Surah-name-after-root convention naively suggests the named-after surah has lexical dominance over the root. Q043-F-04 already tested the density-rank prediction; this test inventories the full 4-attestation distribution and verifies that the naming convention is *symbolic* (one-attestation-each) rather than density-driven.

## 10. Honest limits

- Statistical power is weak (n=4 attestations); the test is descriptive-confirmatory.
- Buckwalter spelling assumed; classical *muʿjam* root analysis not cross-checked.
- Variant readings not surveyed.
