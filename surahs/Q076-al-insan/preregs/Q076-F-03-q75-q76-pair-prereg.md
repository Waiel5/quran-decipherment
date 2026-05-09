---
prereg_id: Q076-F-03
surah: 76
title: Q 75 ↔ Q 76 creation-resurrection mushaf-adjacent pair triplet-cohesion
date_locked: 2026-05-09
phase: B+
hypothesis_class: novel
post_hoc: false
direction_locked: Q 75-76 share creation-axis triplet (xlq + Ans + nTf) at corpus-rare level
bonferroni_k: 4
bonferroni_family: Q076-F
alpha_bon: 0.0125
seed: 20260509
n_perm: 10000
verse_numbering: hafs-kufan
orthography: no-tashkeel
null_model: surah-pair distribution-preserving null on root co-occurrence
---

# Q076-F-03 — Q 75 ↔ Q 76 mushaf-adjacent pair: creation-axis triplet cohesion

## Hypothesis

Q 75 al-Qiyāma + Q 76 al-Insān share the creation-resurrection lexical triplet (xlq, Ans, nTf — create, human, sperm-drop) in BOTH surahs simultaneously. Among 113 mushaf-adjacent pairs, we test the corpus-rarity of this triplet co-occurrence pattern.

The classical-balāgha munāsabāt tradition (al-Biqāʿī *Naẓm al-Durar* on Q 75-76; al-Suyūṭī *Asrār Tartīb al-Qurʾān*) treats Q 75 and Q 76 as a deliberate pair: Q 75 establishes the resurrection-axis (lā uqsimu bi-yawm al-qiyāma), Q 76 establishes the original-creation axis (hal atā ʿalā al-insāni ḥīnun min al-dahr) and the eschatological-reward (paradise tableau) consequence. This is a "resurrection-creation-bracket" architectural pattern.

## Operationalization

For each surah s ∈ [1, 114], compute the set of distinct roots from `data/morphology/root-index.json`. For each mushaf-adjacent pair (s, s+1), check if BOTH surahs contain the triplet {xlq, Ans, nTf}.

## Tests

### Cell A — mushaf-adjacent pair triplet co-occurrence rarity

H₀: A random mushaf-adjacent pair has prob ≥ 5% of containing the creation-triplet in BOTH surahs.
H₁: This is < 2% (corpus-rare).

Decision rule: Among all 113 mushaf-adjacent pairs, count how many have triplet-coverage in both. Compute the empirical fraction. Compare against the binomial expectation given each root's per-surah prevalence.

### Cell B — FR-distance pair-cohesion permutation null

H₀: Q 75 ↔ Q 76 FR-distance is not below the 5th percentile of permuted-pair FR-distances.
H₁: Q 75 ↔ Q 76 FR-distance is below the 25th percentile of all 6,441 surah-pair FR-distances.

Decision rule: Compute Q 75 ↔ Q 76 FR-distance from h-new-111. Find its percentile in all C(114,2) = 6,441 pairs. PASS if percentile ≤ 25%.

NOTE: this is a WEAKER cell because the creation-axis hypothesis is lexical not full-FR.

## Pre-decision verdicts

- **CONFIRMED** if both cells PASS
- **PARTIAL** if Cell A PASS, Cell B NULL
- **NULL** if both fail

## Garden-of-forking-paths log

The triplet identity was determined by inspection of the Q 76 root-index for create + human + sperm-drop, then mushaf-wide search. The hypothesis was formed BEFORE the test was run. Cell A is essentially an empirical-search-against-binomial-baseline test; Cell B is a separate FR-cohesion test on the same pair.

## Replication path

Independent replication via Levenshtein-graph community structure (h-new-235) — does Q 75 and Q 76 land in the same community?
