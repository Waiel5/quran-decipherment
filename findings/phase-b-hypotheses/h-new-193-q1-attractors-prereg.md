---
id: H-NEW-193
title: Q 1 al-Fātiḥa's 7 verses as individual attractors in verse-twin network
phase: B
status: PRE-REGISTERED
date: 2026-04-17
specialist: specialist-B (quran-equation-solvers)
seed: 20260419
bonferroni_k: 2
alpha: 0.05
alpha_bonferroni: 0.025
n_null: 10000
rules_tuple: "(Hafs-Kūfan 6236 verses; text = quran-no-tashkeel.json; char-trigrams over normalized-Arabic with internal whitespace removed; Jaccard similarity)"
parent_findings: [h-new-155 (Q 1 sui-generis-liturgical, p=0.0013), h-new-163 (Q 1 #3 in dispersion ranking)]
pre_reg: findings/phase-b-hypotheses/h-new-193-q1-attractors-prereg.md
script: scripts/h_new_193_q1_attractors.py
output_json: findings/phase-b-hypotheses/csv/h-new-193.json
---

# [[h-new-193-q1-attractors|H-NEW-193]] — Q 1 al-Fātiḥa's 7 verses as individual attractors

## Hypothesis

If Q 1 al-Fātiḥa functions as a "theological palette" for the corpus, then
each of its 7 verses should individually attract twin-verses — verses
scattered across DIFFERENT surahs whose character-trigram Jaccard
similarity to the Q 1 verse is in the top-10.

Phrased differently: Q 1's 7 verses, treated as 7 query-seeds in a
character-trigram nearest-neighbor search, should collectively "touch"
MORE distinct surahs in the top-10 than random 7-verse sets.

## Method

1. Load the 6236 verses from `quran-text/quran-no-tashkeel.json`.
2. Normalize each verse text: strip tashkeel-marks (already no-tashkeel)
   plus remove internal whitespace and Quranic pause marks (ۛ ۖ ۗ ۚ ۘ ۙ ۜ ۞ ۩)
   to produce a continuous character string.
3. For each verse, extract the set of character-trigrams.
4. For each of Q 1's 7 verses (surah=1, verse=1..7, matching `quran-no-tashkeel.json`
   indexing which uses basmala as verse 1 in Hafs-Kūfan), compute Jaccard
   similarity to all 6236 verses. Exclude self-match (same surah+verse).
5. Rank the top-50 nearest neighbors per Q 1 verse. Record top-10 and
   top-50 distinct-surah counts.
6. **Primary outcome**: count the DISTINCT surahs appearing in the union
   of the top-10 neighbors across Q 1's 7 verses (direction: HIGHER
   than null).
7. **Secondary outcome**: average top-10 Jaccard similarity across Q 1's
   7 verses (direction: HIGHER than null — Q 1 verses are "closer" to
   their twins than random seeds are to theirs).

## Null distribution

Seed 20260419. For each of N=10000 permutations:
- Sample 7 verses uniformly at random WITHOUT replacement from the 6236
  corpus verses, EXCLUDING the 7 Q 1 verses themselves.
- For each sampled seed-verse, compute Jaccard similarity to all 6236
  other verses, get top-10 neighbors (excluding self).
- Record primary (distinct-surah count across union) and secondary
  (average top-10 Jaccard) for the sampled 7-tuple.

p-value = fraction of null tuples whose primary (or secondary) statistic
meets-or-exceeds Q 1's observed statistic.

Because N=10000 requires O(N * 7 * 6236) Jaccard comparisons, a
precomputed all-pairs top-10 table (per-verse top-10 neighbors by
Jaccard) enables O(1) lookup per random-sample verse.

## MW-5 control

A random 7-verse set (sampled with seed 20260419+offset) should touch
FEWER distinct surahs than Q 1. If the random sample shows
distinct-surah count ≥ Q 1's value, flag as MW-5 FAIL — the effect is
not Q-1-specific.

Concretely: take the MEDIAN of the null distribution as the MW-5
control anchor. Q 1 must exceed the null median by ≥ 1σ (roughly
translates to p < 0.16 two-sided, or "directionally passes" under MW-5).

## Bonferroni

k = 2 outcomes (primary distinct-surahs; secondary average similarity).
α_bon = 0.05 / 2 = 0.025. A pass requires the primary p-value
< 0.025 under the pre-registered direction.

## Direction lock

Both directions locked POSITIVE (Q 1 > null) BEFORE execution.

## Pass / Fail conditions

**PASS** (attractors CONFIRMED): primary p < 0.025 AND secondary
p < 0.025 AND MW-5 control shows random-sample < Q 1.

**PARTIAL**: only primary passes.

**FAIL**: primary p ≥ 0.025 (Q 1's 7 verses do NOT collectively attract
more distinct surahs than random).

## Garden-of-forking-paths log

- Fixed: char-trigrams over no-tashkeel normalized text (whitespace
  stripped, pause marks stripped). Char-trigrams chosen because they
  capture both morphological stems AND short function-words without
  requiring a tokenizer.
- Fixed: Jaccard similarity (symmetric, no TF weighting — so no bias
  from verse-length).
- Fixed: top-10 primary, top-50 secondary-report.
- Fixed: exclude self-match (same surah+verse id).
- Fixed: seed 20260419.
- Fixed: 10000 null permutations.
- Fixed: sample 7-verse tuples WITHOUT replacement, EXCLUDING Q 1's
  7 verses themselves from the null pool.
- Fixed: Q 1 uses verses 1-7 as given in `quran-no-tashkeel.json`
  (Hafs-Kūfan numbering; basmala is verse 1). The task header noted
  "excluding basmala" but the task also specifies "7 individual
  verses"; we follow [[h-new-155-q1-sui-generis|H-NEW-155]]'s precedent of using Q 1:1-7 (verses
  as numbered in Hafs). Sensitivity: also report primary with
  verses 2-7 ONLY (6-verse variant) — if the main result inverts
  under this variant, that is a disclosure.

## Expected behavior under null

Naive expectation: 7 random verses × 10 neighbors = 70 neighbors;
with some overlap, null-median distinct-surahs is likely somewhere in
the 25-50 range for a 114-surah corpus. Q 1 — if a "palette" — should
exceed this.
