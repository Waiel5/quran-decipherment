---
surah: 34
test_id: Q034-F-02
title: Q 27 al-Naml + Q 34 Sabaʾ — Sabaʾ-narrative pair cohesion test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q034-F-02-saba-pair
alpha_bon: 0.01667
---

# Q034-F-02 — Pre-registration: Q 27 ↔ Q 34 Sabaʾ-narrative pair cohesion

## 1. Hypothesis (locked before observation)

Q 27 al-Naml and Q 34 Sabaʾ are the corpus's only 2 surahs containing the proper noun *sabaʾ* (LEM:saba<, POS:PN, per QAC v0.4 morphology). Q 27:22 contains the hoopoe-bird's report from Sabaʾ; Q 34:15 contains the eponymous Sabaean kingdom narrative. The pair is conjectured to be **Fisher-Rao closer-than-random** at the bilateral pair level.

**H1 (locked direction, FR distance):** D[Q 27, Q 34] is among the bottom-25th-percentile of all 6,441 surah-pair distances (i.e., closer than 75% of pairs). Pass at α = 0.05/3 = 0.01667.

**H2 (locked direction, mutual top-K):** Q 27 and Q 34 are mutually in each other's top-K nearest neighbors at K=10. Pass: BOTH true (Q 34 ∈ Q 27 top-10 AND Q 27 ∈ Q 34 top-10).

**H3 (locked direction, length-residualized closeness):** After residualizing pairwise FR distances on |log(VC_i) − log(VC_j)|, the Q 27 ↔ Q 34 residual is in the bottom-25th-percentile of all-pair residuals.

## 2. Operational definitions

### Data
- FR matrix: `findings/phase-b-hypotheses/csv/h-new-111.json`.
- Verse counts: `data/hafs-verse-counts.tsv`.

### H1: bilateral percentile
- Compute D[Q 27, Q 34] = D[26, 33] (0-indexed).
- Compute percentile of this value among all 6,441 D[i, j] for i < j.
- Pass: percentile ≤ 25 (i.e., among the bottom-25% of pairwise distances).

### H2: mutual top-10
- Compute Q 27's top-10 FR neighbors.
- Compute Q 34's top-10 FR neighbors.
- Check: Q 34 ∈ Q 27 top-10 AND Q 27 ∈ Q 34 top-10.

### H3: length-residualized
- Same regression as Q034-F-01 H3.
- Compute residual for the Q 27 ↔ Q 34 pair.
- Compute percentile of this residual.
- Pass: percentile ≤ 25.

## 3. Test statistic

- D[27, 34] (raw FR distance).
- D[27, 34] percentile.
- Q 34 rank in Q 27 neighbors; Q 27 rank in Q 34 neighbors.
- Length-residualized percentile.

## 4. Success / Failure criteria

| Cells passing | Verdict |
|:--|:--|
| 3/3 H1+H2+H3 | CONFIRMED |
| 2/3 | DIRECTIONAL |
| 1/3 | DIRECTIONAL-WEAK |
| 0/3 | NULL |

## 5. Honest limits known a priori

- The pair shares the *sabaʾ* proper-noun lemma — but *sabaʾ* appears 1× in each. The contribution of this single lemma to FR distance is bounded; H1's positive test would require shared CONTENT-DISTRIBUTION, not just shared lemma.
- Both surahs are Late Meccan; both contain prophet-narrative material (Solomon prominent in both); both contain the ḥamd-formula (Q 27:15 *qālā al-ḥamdu li-llāh*, Q 34:1 opening *al-ḥamdu li-llāh*). Multiple shared content-features, so positive cohesion is plausible.
- Empirical-anchor disclosure: I observed during pre-reg construction that D[Q 27, Q 34] = 0.8661 (31.3rd percentile — above the 25th-percentile threshold). Q 34 is rank 8 in Q 27 neighbors; Q 27 is rank 10 in Q 34 neighbors (BOTH top-10 — H2 pre-passes).
- Per HANDOFF/04-DISCIPLINE.md, locked direction even though H1 and H3 are tightly bracketed at the threshold; verdict ceiling is **DESCRIPTIVE-EMPIRICAL** under transparent post-hoc disclosure (any borderline-passing cell will be reported with full caveats).

## 6. Rules-tuple

`(no-tashkeel, orthographic-token + QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`.

## 7. Bonferroni

k = 3 (H1, H2, H3). α_bon = 0.01667 per test for H1, H3. H2 is binary-categorical (pass = both top-10) and not p-corrected.

## 8. SHA256 lock

Embedded in `scripts/Q034_F_02_q27_q34_saba_pair.py`; verified at runtime.
