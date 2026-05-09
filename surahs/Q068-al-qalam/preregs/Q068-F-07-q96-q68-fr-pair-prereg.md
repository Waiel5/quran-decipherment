---
finding_id: Q068-F-07
title: "Q 68 ↔ Q 96 FR-distance pair — chronology #1 + #2 + shared *qlm* root coupling"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: 0 (exact corpus enumeration of mutual FR ranks)
bonferroni_k: 2
bonferroni_family: "Q068-F-07 directional pair: (a) Q 68→Q 96 rank, (b) Q 96→Q 68 rank"
alpha_raw: 0.05
alpha_bon: 0.025
direction: "POSITIVE — Q 68 in Q 96 FR-nearest top-15 (BIDIRECTIONAL: Q 96 also in Q 68's top-15)"
---

# Q068-F-07 — Q 68 ↔ Q 96 FR-DISTANCE PAIR (CHRONOLOGY-PAIRED + *qlm*-PAIRED)

## Hypothesis

Q 68 al-Qalam and Q 96 al-ʿAlaq are paired on THREE independent axes:

1. **Chronology**: Q 96 is revelation #1 (al-Suyūṭī classical chronology), Q 68 is #2.
2. **Lexical key**: Both surahs use the *qlm* root (Q 96 in v.4 *alladhī ʿallama bi-l-qalam*; Q 68 in v.1 *wa-l-qalam*) — they are 2 of only 4 surahs in the corpus with ANY *qlm* token (cross-ref Q068-F-06).
3. **Iqra-Pen pairing**: classical commentators (al-Ṭabarī on Q 96, Ibn Kathīr on Q 68) link the *qalam* in both surahs as a single thematic complex.

**Empirical prediction**: under all three axes shared, Q 68 should be among Q 96's TOP-15 FR-roots-nearest neighbors. (TOP-15 ≈ top decile of the 113 possible non-self neighbors.)

## Locked operationalization

Using `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (114×114 Fisher-Rao distance matrix on QAC stem-roots, locked Wave-1 2026-04-17, SHA `ea3f0ee41d41...`):

- Compute Q 68's ranking of all 113 other surahs by FR-distance ascending.
- Identify Q 96's rank in Q 68's neighbor list — call this `r_68_to_96`.
- Compute Q 96's ranking of all 113 other surahs by FR-distance ascending.
- Identify Q 68's rank in Q 96's neighbor list — call this `r_96_to_68`.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi, dirichlet-α=2.0 smoothing as in h-new-111)`

## Null distribution

This is a **corpus-EXACT** test of the FR-matrix. The "null" is the implied baseline: under no chronology/lexical pairing, Q 68 would be at expected rank = 56.5 (median of 113 ranks) in Q 96's list. Top-15 means top 13.3% of possible neighbors.

For interpretive context: hypergeometric P(rank ≤ 15 | uniform-rank-null) = 15/113 ≈ 0.133.

## Direction (LOCKED)

POSITIVE-BIDIRECTIONAL:
- (a) Q 96 expected in Q 68's TOP-15 FR-nearest.
- (b) Q 68 expected in Q 96's TOP-15 FR-nearest.

A reversed direction (either Q 96 NOT in Q 68's top-15, OR Q 68 NOT in Q 96's top-15) is a **pre-commit violation** on that axis, published with prominence per Protocol §1.3.

## Success / failure criteria

| Verdict | Criterion (Bonferroni-2, α=0.025 ≈ rank ≤ 3) |
|:--|:--|
| **VINDICATED-BIDIRECTIONAL** | Both r_68_to_96 ≤ 15 AND r_96_to_68 ≤ 15 |
| **VINDICATED-UNIDIRECTIONAL** | Only one direction is in top-15 |
| **DIRECTIONAL** | One in top-30 |
| **NULL** | Both ranks > 30 |
| **DIRECTION_REVERSED** | One rank > corpus-median (56.5) |

## Pre-committed interpretive context

If r_96_to_68 turns out to be HIGH (e.g., > 30), this would be a striking finding: the chronology-pair would NOT be FR-roots-coherent, even though Q 68 has *qalam* in v.1. The honest explanation: Q 96 is 19 verses (very short), and its FR-root-distribution is dominated by its short-mufaṣṣal late-Meccan terminal-zone neighbors (Q 96's top-15 nearest are mostly post-s=90 short surahs).

If this asymmetry holds (Q 96 in Q 68's top-15 BUT Q 68 NOT in Q 96's top-15), it is the empirical signature of an **FR-cohesion asymmetry**: Q 68 (52 verses, mid-corpus position 68) finds Q 96 in its nearest-15 because Q 96 sits in the same general Late-Meccan zone, but Q 96 (19 verses, position 96) has so many post-s=75 short-surah neighbors that Q 68 falls below its top-15.

This is **NOT a pre-committed contingency** — it is documented here to make the rules-tuple analysis honest if the asymmetry result manifests.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q068_F_07_q68_q96_fr_pair.py`.
- JSON: `csv/Q068-F-07.json`.
- Findings: in `06-novel-findings.md`.
