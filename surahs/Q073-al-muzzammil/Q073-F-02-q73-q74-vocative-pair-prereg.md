---
surah: 73
test_id: Q073-F-02
title: Q 73 ↔ Q 74 muzzammil/muddaththir vocative-pair cohesion test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q073-F-02-q73-q74-vocative-pair
alpha_bon: 0.0167
---

# Q073-F-02 — Pre-registration: Q 73 + Q 74 muzzammil/muddaththir vocative-pair cohesion test

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction):** The Q 73 ↔ Q 74 surah-pair is empirically cohesive on **at least 2 of the 3 pre-registered axes**:
- Axis A: Fisher-Rao distance (H-NEW-111 root-distribution) is in the **top-15 closest** pair-members for each (mutual top-15 nearest-neighbors).
- Axis B: Mushaf-canonical adjacency cost (H-NEW-720) is **clamped-zero** (delta_raw ≤ 0).
- Axis C: They share an opening-formula structural signature: identical `يا أيها ال[X]` direct-prophetic-vocative pattern, with X being a passive-participle morphological-template-twin.

**H0:** Fewer than 2 of the 3 axes pass.

**Direction:** mutual cohesion + structural kinship (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json`.
- **FR distance (Axis A)**: from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`. Test: rank Q 74 among Q 73's nearest 113, AND rank Q 73 among Q 74's nearest 113. Both must be ≤ 15 for axis pass.
- **Adjacency cost (Axis B)**: from `findings/phase-b-hypotheses/csv/h-new-720.json` `per_adjacency` for `s = 73` (the Q 73→Q 74 transition). PASS if `delta_raw ≤ 0` (clamped-zero seam set).
- **Opening-formula (Axis C)**: regex match for both:
  - Q 73:1 = `يا أيها المزمل`
  - Q 74:1 = `يا أيها المدثر`
  Confirm both surahs open with `يا أيها ال` + a SINGULAR PASSIVE-FORM-V participle (مزمل = mu-zammil ≈ "wrapped", مدثر = mu-ddaththir ≈ "covered"). The participle pair is morphologically isomorphic (same Form-V mu-XaXXiX template) and semantically twinned (both denote "enwrapped in garments").

## 3. Test statistic

- Axis A boolean: rank_73_in_74 ≤ 15 AND rank_74_in_73 ≤ 15
- Axis B boolean: delta_raw(Q 73→Q 74) ≤ 0
- Axis C boolean: opening-formula passive-participle morphological-isomorph match
- Aggregate test: `n_pass_axes ≥ 2` of 3.

## 4. Permutation null

For Axis A (FR-cluster pair-cohesion): null = pick 1000 random surah-pairs and compute the fraction with mutual top-15 status. Bonferroni k=3 ⇒ α_bon = 0.0167.

For Axis B: per H-NEW-720 cumulative_stats, 13 of 113 adjacency pairs are clamped-zero (11.5%). Under the null of random permutation of pair-positions, the marginal probability of any specific adjacency being clamped-zero ≈ 0.115. PASS-DIRECTED if observed.

For Axis C: not a stochastic test — categorical morphological match (the corpus has only Q 73 + Q 74 with this exact passive-participle vocative-prophetic template).

## 5. Success / Failure

- **CONFIRMED**: ≥2 of 3 axes pass; permutation null (Axis A) p ≤ α_bon = 0.0167 OR axis-pass count = 3.
- **DIRECTIONAL**: 2 of 3 axes pass at single-test α=0.05 but Bonferroni-3 fails.
- **NULL**: ≤ 1 axis passes.
- **PRE-COMMIT VIOLATION**: 0 axes pass (the pair has no structural cohesion).

## 6. Honest limits known a priori

- Q 73 ↔ Q 74 are mushaf-adjacent. Mushaf-adjacency is a **strong prior** for FR-proximity per the H-NEW-111 (mushaf is FR-information-geodesic-optimal) result. Some of the cohesion expected on Axes A+B is therefore mediated by the mushaf-architectural prior. **This is acknowledged**: the test is asking whether the cohesion is in the empirical TOP TIER (top-15 / clamped-zero), not whether mushaf-adjacency by itself produces cohesion.
- Axis C is **categorical** (morphological-template match exists corpus-wide?). The Q 73 + Q 74 vocative-passive-participle-prophetic pattern is the ONLY corpus instance of this exact template per pre-flight observation; this is an a-priori categorical verdict, not subject to permutation null. PASS by enumeration.
- The FR data (h-new-111.json) is on a **single feature space** (root-distribution). Independent replication on char-4-gram (h-new-111b) or verse-length (h-new-111c) would be queued as Q073-F-02b.

## 7. Pre-commit attestation

- The Q 73 ↔ Q 74 mushaf-adjacency is canonical knowledge. Their opening-formula identity (یا أیها ال + Form-V passive-participle vocative) is also well-known classical observation (Wansbrough 1977 *Quranic Studies*, p. 75 cite). The test asks the empirical-precision question: are they EMPIRICALLY in the top-tier on FR + adjacency? This is computed for the first time in this specialist run.
- No pre-test peek at h-new-111.json `Q 73 row` or h-new-720.json `s=73`. SHA-lock first, run after.

## 8. Decision rule

1. Compute Axis A from h-new-111.json (decode upper-triangular, get rank).
2. Read Axis B from h-new-720.json `per_adjacency[s=73]`.
3. Confirm Axis C by regex on Q 73:1 + Q 74:1 + manual morphological match.
4. n_pass = sum of the 3 booleans.
5. Apply success matrix.

## 9. Bonferroni declaration

- bonferroni_k = 3 axes.
- bonferroni_family = Q073-F-02-q73-q74-vocative-pair.
- alpha_bon = 0.05 / 3 = 0.0167 per axis.
- Aggregate decision rule: ≥2 axis-passes for DIRECTIONAL; ≥2 with Bonferroni for CONFIRMED; 3/3 = STRONG-CONFIRMED.

## 10. Connection to existing findings

- **H-NEW-111** (mushaf-FR-geodesic-optimal): Q 73 ↔ Q 74 is a mushaf-adjacent pair, locally smooth.
- **H-NEW-720** (canonical-adjacency-cost): Q 73 ↔ Q 74 is candidate-cohesive in the mushaf-2-opt sense.
- **Wansbrough 1977** + classical commentary tradition: Q 73 + Q 74 are recognized as "twin opening-formula early-Meccan revelations". Empirical test of this verbal tradition.
- **Bukhārī Bad' al-Waḥy hadith #4**: connects Q 74:1-5 to first-revelation chronology. Combined with Q 73 (revelation-order #3 per Tanzil + Wikipedia Nöldeke), the pair is also chronologically-twin.
