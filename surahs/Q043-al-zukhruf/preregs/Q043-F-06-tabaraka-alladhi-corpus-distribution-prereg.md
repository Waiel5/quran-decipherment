---
prereg_id: Q043-F-06
title: *tabāraka alladhī* corpus-attestation distribution — 5-locus map
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q043-F-06 — *tabāraka alladhī* 5-locus distribution

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The phrase **تبارك الذي** (*tabāraka alladhī*) appears in *exactly five* attestations across the entire Quranic corpus, at exactly the loci:
- Q 25:1
- Q 25:10
- Q 25:61
- Q 43:85
- Q 67:1

Per the Q025-F-02 finding (handoff §10.44), this is the corpus-canonical *tabāraka alladhī* set. Q 43:85 is the 3rd-position attestation (chronologically by mushaf order: Q 25, Q 25, Q 25, Q 43, Q 67).

## 2. Null / negation

**H0**: Q 43:85 is *not* a *tabāraka alladhī* locus, OR the corpus attestation total differs from 5.

## 3. Operationalization

- Source: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- Search pattern: literal string `تبارك الذي` (without diacritics).
- Enumerate all (surah, verse) loci.

## 4. Direction lock

Pre-committed: **exactly 5 attestations at exactly the listed loci**.

## 5. Bonferroni

Single exact-locus test; α = 0.05 (no family).

## 6. Success / failure criteria

- **VINDICATED**: observed_loci == expected_loci (set-equality).
- **NULL_OR_DISCREPANCY**: any other outcome.

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q043-F-06.json`: total_attestations, attestation_loci, expected_loci, verdict.

## 9. Rationale

The *tabāraka alladhī* formula is one of the corpus's signature opener-class incantations (Q 25:1, Q 67:1 are surah-openers). The Q 25-cluster (vv 1, 10, 61) is dense; Q 43:85 is an internal closing-doxology (verse 85 of 89). Locking the 5-locus set verifies the cross-finding from Q 25 and provides the empirical baseline for any further structural analysis (e.g., whether the 5 loci share verse-level FR cohesion).

## 10. Honest limits

- The min-tashkeel and full-tashkeel variants may produce identical results (the phrase is consonantal-stable); tested under no-tashkeel default only.
- The Hafs-Kufan reading is assumed canonical; variant readings (e.g., Warsh) are not surveyed.
