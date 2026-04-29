---
prereg_id: Q043-F-04
title: zukhruf root (z-kh-r-f) — Q 43 named-after-root signature analysis
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T19:20:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q043-F-04 — *zukhruf* root signature

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The root **z-kh-r-f** (Buckwalter `zxrf`) appears in *exactly four* attestations across the entire Quranic corpus, with **exactly one** attestation in Q 43 itself (the surah-name-bearing locus, Q 43:35). The named-after-root signature shows that Q 43 carries the surah-name token but does NOT have lexical-density dominance over the root.

The DIRECTIONAL claim is therefore: **Q 43's `zxrf` root density is NOT the corpus maximum** (a deliberately falsifying-direction-lock against confirmation bias on surah-name claims).

## 2. Null / negation

**H0**: Q 43 has the highest density of the `zxrf` root (the naive "named-after = highest density" assumption).

The pre-committed direction is the **inversion** of the naive hypothesis — to test whether surah-name lexicalization implies lexical concentration.

## 3. Operationalization

- Source: `data/morphology/root-index.json` (QAC v0.4 root-attestation index).
- Target root key: `zxrf` (Buckwalter for z-kh-r-f).
- Per-surah token counts from `quran-text/quran-no-tashkeel.json` (whitespace tokens).
- Compute: per-surah `zxrf` count, per-surah density per 1000 tokens, corpus rank of Q 43.

## 4. Direction lock

Pre-committed direction: **Q 43 rank > 1 by `zxrf` density** (i.e., not the densest).

If observed direction reversed (Q 43 IS rank 1): **the naive hypothesis is confirmed and the surah-name lexicalization implies density dominance** — recorded as a conditional finding, with the original pre-commit honored.

This is a **dual-honored design**: the pre-committed direction is the surprising-direction; whichever way it lands, the empirical signature is recorded honestly.

## 5. Bonferroni

Member of the Q 43 novel-findings family (k=4). α_corrected = 0.0125. Test is exact (count-based), not parametric.

## 6. Success / failure criteria

- **VINDICATED (surprising direction)**: Q 43 rank > 1 by `zxrf` density → the surah-name-as-marker is *symbolic*, not density-driven.
- **NULL** (naive direction): Q 43 rank = 1 → the surah is genuinely the densest in its named-root.
- **Total-attestation invariant**: report total corpus `zxrf` attestations (pre-committed prediction: exactly 4).

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q043-F-04.json`: per-surah `zxrf` count + density, corpus rank of Q 43, total corpus attestations, top-density surahs.

## 9. Rationale

Surah names are conventionally derived from a salient lexical token within the surah. The naive expectation is that the surah named *al-Zukhruf* would have the highest *zukhruf* lexical density — but this is empirically testable. Pre-Islamic poetic-naming conventions (Zuhayr's *al-muʿallaqa* named for prosodic incipit, not lexical center) are inconsistent with density-driven naming. This pre-reg formalizes the test.

## 10. Honest limits

- The `zxrf` root has only 4 attestations corpus-wide; the rank-test is statistically weak (most surahs have count = 0, density = 0). The "rank" therefore lumps many surahs at rank 0; the meaningful rank is *among non-zero-density surahs only*, which is a small set.
- The QAC v0.4 root annotation is the source-of-truth; alternative root-segmentations (e.g., classical *muʿjam* root analysis) are not used.
