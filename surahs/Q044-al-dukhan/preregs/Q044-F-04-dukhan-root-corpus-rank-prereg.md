---
prereg_id: Q044-F-04
title: dukhān (d-kh-n) root corpus rank — direction-locked rank-1 for Q 44
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q044-F-04 — *dukhān* root corpus rank

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The root **d-kh-n** (Buckwalter `dxn`, "smoke") attains its **corpus rank-1** in Q 44 al-Dukhān by both raw count and density-per-1000-tokens. This is the direction-locked surah-name-density prediction.

## 2. Null / negation

**H0**: Q 44 is NOT rank-1 by `dxn` count or density.

## 3. Operationalization

- Source: `data/morphology/root-index.json` (QAC v0.4).
- Target key: `dxn`.
- Per-surah token counts: from `quran-text/quran-no-tashkeel.json`.
- Compute count + density rank.

## 4. Direction lock

Pre-committed: **Q 44 rank = 1 by both count and density**.

If observed Q 44 rank > 1: NULL (the surah-name does not entail lexical concentration).

## 5. Bonferroni

Member of Q 44 novel-findings family (k=3 in this batch). α_corrected = 0.0167. Test is exact.

## 6. Success / failure criteria

- **VINDICATED**: Q 44 is rank-1 by both count and density.
- **MIXED**: Q 44 is rank-1 by exactly one of (count, density).
- **NULL**: Q 44 rank > 1 by both.

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q044-F-04.json`: corpus_total, surahs_with_attestation, per_surah_counts, q44_count_rank, q44_density_rank, top-5 ranked by each metric, verdict.

## 9. Rationale

The "smoke" root is rare; the named-surah convention predicts that Q 44 holds the lexical center. This is the opposite direction-lock from Q043-F-08: where Q 43 was predicted NOT-densest (4 attestations, 4 surahs, 1 each), here Q 44 IS predicted densest. The contrast informs the broader question: do named surahs concentrate their eponym?

## 10. Honest limits

- Small-N test; power is moderate.
- The English "smoke" gloss is shorthand; the Arabic *dukhān* in Q 44:10 is interpreted variably (literal vs eschatological omen) — the root-attestation test is purely lexical.
