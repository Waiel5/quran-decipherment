---
test_id: Q002-F-04
title: Q 2 ring-structure (chiastic) test against shuffle null
target_claim: Farrin 2010 (*Surat al-Baqara: A Structural Analysis*) and Cuypers 2015 (*The Composition of the Quran*) — Q 2 has nine-section ring composition with verse 143 as central pivot; verse 1 mirrors verse 286, verse 2 mirrors verse 285, etc.
date_locked: 2026-04-28
phase: B+
status: PRE-REGISTERED
seed: 20260428
---

# Pre-registration — Q002-F-04: Q 2 ring-structure detection

## 1. Hypothesis (LOCKED)

**H1**: Q 2 verse-by-verse cosine similarities (on no-tashkeel word-token sets, 1-hot) show CHIASTIC mirroring measurably above a shuffled-null baseline. Specifically:

`ring_score(Q 2) = mean over i ∈ {1..142} of cos(verse_i, verse_(287-i))`

is higher than the 95th-percentile of `ring_score` computed on 10,000 random permutations of Q 2's verse order.

**H0**: ring_score is at or below the 95th percentile of the null.

**Direction (LOCKED)**: HIGHER ring_score in canonical order than null (ring structure → high similarity in symmetric pairs).

## 2. Operationalisation

- **Vector**: each verse → set of unique no-tashkeel word-tokens (whitespace-split, sajda/punct stripped).
- **Cosine**: |A∩B| / sqrt(|A|·|B|).
- **Symmetric pairs**: (1, 286), (2, 285), ..., (143, 144). For 286 verses, the central pivot verse 143 (or 143-144) per Farrin's analysis.
- **Pair count**: i = 1 to 143, paired with 287-i. Note: i=143 → 144 (central pair).
- **Ring score**: arithmetic mean of cosine over 143 pairs.

## 3. Null distribution

- Permutation null: shuffle the 286 verses' indices (seed=20260428), compute ring_score on the shuffled order. Repeat 10,000 times.
- Compute one-sided p-value: P(ring_score_shuffled ≥ ring_score_canonical).
- Pre-registered α = 0.01 (within Bonferroni family of 5 Q 2 tests).

## 4. Alternative model (MW-3)

Also compute on lemma-level (root-trigram) using QAC roots from `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` if computationally feasible. Otherwise use word-token only.

## 5. Success criteria

- **VINDICATED**: p < 0.01 (Bonferroni-tight) — supports Farrin/Cuypers ring-structure claim.
- **DIRECTIONAL**: p < 0.05.
- **NULL**: p ≥ 0.05 — NULL on quantitative ring-structure at verse-pair level.
- **PRE-COMMIT VIOLATION**: ring_score < 5th percentile of null (would indicate ANTI-ring structure).

## 6. Honest limit (a priori)

This test's resolution is at the verse-token level, NOT thematic level. Farrin and Cuypers operate at the THEMATIC-block level (9 sections, not 143 pairs). A NULL on this test does not falsify their thematic-ring claim; it only falsifies a verse-token-level mirror. To verify the thematic claim properly would require a hand-coded thematic similarity matrix.

We thus also report: **block-pair score** = mean cos(block_a, block_(10-a)) for a ∈ {1..4}, using the 9-block scheme from §00-overview. This gives a coarser-grained test that better matches the Farrin/Cuypers level of claim.

## 7. MW-1..7

- **MW-1**: cosine + 1-hot tokenization LOCKED.
- **MW-2**: 10,000 perms = ≥ 10000 minimum.
- **MW-3**: 2 model variants (verse-pair, block-pair).
- **MW-4**: no fitted parameters.
- **MW-5**: re-run with seed=42 secondary.
- **MW-6**: control: run the same test on Q 3 Āl ʿImrān (200 verses, no classical ring-structure claim of Farrin's strength) — if Q 3 also passes, the ring-detection metric is non-specific.

## 8. Output paths

- Script: `/Users/grey/Downloads/quran/scripts/Q002_F_04_ring_structure.py`
- JSON: `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/csv/Q002-F-04.json`
- Findings: `/Users/grey/Downloads/quran/surahs/Q002-al-baqara/Q002-F-04-ring-structure.md`

*Locked 2026-04-28.*
