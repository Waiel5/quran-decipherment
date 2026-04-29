---
id: H-NEW-140.1
title: All-pair de-circularization of H-NEW-140 divine-name pair cohesion
phase: B
status: PRE-REGISTERED (locked before running)
date: 2026-04-17
agent: h96-wrapper
parent: H-NEW-140 (PASS-DIRECTED: 16 classical pairs, aggregate 13.87× enrichment)
audit_flag: audit-037 selection-circularity adversarial critique
seed: 20260417
bonferroni_k: 1
bonferroni_family: h-new-140-1-all-pair
alpha_bon: 0.05
---

# [[h-new-140-1-all-pair-decircularization|H-NEW-140.1]] — All-pair de-circularization

## The circularity concern (audit-037)

[[h-new-140-divine-name-pair-cohesion|H-NEW-140]] tested 16 hand-selected classical pairs against Poisson-independence null and found 13.87× aggregate enrichment. audit-037 flagged: the 16 pairs were selected by CLASSICAL LITERATURE which may itself have been informed by observation of the empirical co-occurrence. This creates selection bias: "classical scholars noticed these pairs co-occurred, hence listed them, hence we're just confirming what they already saw."

## Hypothesis (falsifiable)

Enumerate ALL C(20, 2) = 190 possible pairs from a 20-name list. For each, compute observed verse-level co-occurrence count and Poisson-independence z-score. Rank all 190 pairs by z-score.

**Question**: of the TOP-16 empirically-highest-z pairs, how many match the 16 classical-anchor pairs in [[h-new-140-divine-name-pair-cohesion|H-NEW-140]]?

## Decision rule (pre-committed)

Following team-lead's specification:

- **Match rate > 50%** (≥8 of top-16 classical pairs match top-16 empirical pairs): classical selection is confirmed as tracking the strongest empirical signal. Selection bias exists (classical scholars DID observe) but concern is NEUTRALIZED — selected pairs ARE the empirical winners.
- **30% ≤ match rate ≤ 50%** (5-8 matches): mixed. Classical list tracks empirical signal partially but with non-empirical considerations (theology, rhetoric).
- **Match rate < 30%** (≤4 matches): classical selection reflects OTHER considerations, not just empirical strength. [[h-new-140-divine-name-pair-cohesion|H-NEW-140]] demoted from PASS-DIRECTED to descriptive; the enrichment is real but the pair-selection is theologically motivated.

## Secondary test: leave-one-out sensitivity

After removing the dominant outlier al-ʿAzīz+al-Ḥakīm (z=+43.5, obs=29, exp=0.43):
- Recompute aggregate ratio (parent was 13.87×). Expected: drop, but by how much?
- If aggregate ratio stays >5×: main [[h-new-140-divine-name-pair-cohesion|H-NEW-140]] finding is robust to the outlier.
- If aggregate ratio drops <3×: ʿAzīz+Ḥakīm is carrying the finding and [[h-new-140-divine-name-pair-cohesion|H-NEW-140]] should be reframed as "one pair dominates + others are minor."

## 20-name list (LOCKED before running)

Composed of the 15 unique names in [[h-new-140-divine-name-pair-cohesion|H-NEW-140]]'s 16 pairs:
1. al-Raḥmān (الرحمن)
2. al-Raḥīm (الرحيم)
3. al-ʿAzīz (العزيز)
4. al-Ḥakīm (الحكيم)
5. al-Samīʿ (السميع)
6. al-Baṣīr (البصير)
7. al-Ghafūr (الغفور)
8. al-Tawwāb (التواب)
9. al-ʿAlīm (العليم)
10. al-Ḥalīm (الحليم)
11. al-Shakūr (الشكور)
12. al-Wadūd (الودود)
13. al-Qadīr (القدير)
14. al-Khabīr (الخبير)
15. al-Laṭīf (اللطيف)

Plus 5 canonical Khawātim al-Ḥashr names (Q 59:22-24), which are a second-well-established classical grouping distinct from the pair-list:
16. al-Malik (الملك)
17. al-Quddūs (القدوس)
18. al-Salām (السلام)
19. al-Muʾmin (المؤمن)
20. al-Muhaymin (المهيمن)

This 20-name selection matches team-lead's "20 divine-name list" from [[h-new-140-divine-name-pair-cohesion|H-NEW-140]]; if the original list differs, we re-run with the correct list and mark this as rules-tuple sensitivity.

## Matching rules (locked)

Each name is matched in verse text with tolerance for:
- `الX` form (with definite article) — primary
- `X` form (without definite article, as standalone word) — accepted
- Genitive/case ending suffixes are tolerated (e.g., `العزيزُ`, `عزيزٌ`) but we use the no-tashkeel Quran so this reduces to the simple surface match
- Matching is ANYWHERE-IN-VERSE (matches [[h-new-140-divine-name-pair-cohesion|H-NEW-140]]'s primary operationalization, not fawāṣila-only)

## Classical-pair list (the 16 from [[h-new-140-divine-name-pair-cohesion|H-NEW-140]])

1. al-Raḥmān + al-Raḥīm
2. al-ʿAzīz + al-Ḥakīm
3. al-Samīʿ + al-Baṣīr
4. al-Ghafūr + al-Raḥīm
5. al-Tawwāb + al-Raḥīm
6. al-ʿAzīz + al-Ghafūr
7. al-ʿAzīz + al-ʿAlīm
8. al-ʿAzīz + al-Raḥīm
9. al-ʿAlīm + al-Ḥakīm
10. al-Ḥalīm + al-Ghafūr
11. al-Shakūr + al-Ḥalīm
12. al-Wadūd + al-Ghafūr
13. al-Qadīr + al-ʿAlīm
14. al-Khabīr + al-ʿAlīm
15. al-Laṭīf + al-Khabīr
16. al-Samīʿ + al-ʿAlīm

## Procedure

1. Load no-tashkeel Quran (6,236 verses).
2. For each of 20 names, count occurrences per verse (surface match on both `الX` and `X`-standalone).
3. For each of C(20, 2) = 190 pairs (A, B): observed = count of verses where BOTH A and B appear.
4. Compute expected Poisson-independence E = n_A × n_B / N_verses.
5. Compute z = (observed − E) / sqrt(E) (matches [[h-new-140-divine-name-pair-cohesion|H-NEW-140]] method).
6. Rank 190 pairs by z descending.
7. Compare top-16 empirical pairs to 16 classical pairs (match count).
8. Leave-one-out sensitivity: remove al-ʿAzīz+al-Ḥakīm pair, recompute [[h-new-140-divine-name-pair-cohesion|H-NEW-140]] aggregate (115−29=90 obs? No — aggregate ratio = total_obs / total_expected across 15 remaining pairs).
9. Output to JSON + table.

## Expected outcome (pre-committed)

My prior: the 16 classical pairs likely ARE among the top empirical z-scores because:
- Classical scholars DID observe co-occurrences; their list is empirically grounded
- Some classical pairs involve names with HIGH individual frequency (al-Ghafūr, al-Raḥīm, al-ʿAzīz, al-ʿAlīm) so pair combinations have high obs-vs-expected
- But some classical pairs may NOT be top-empirical (e.g., al-Wadūd+al-Ghafūr = 1 obs) and the ranking may include non-classical pairs with high z by different name-combinations

Predicted match rate: **0.5 - 0.8** (8-13 of 16 matching). Leave-one-out: aggregate ratio likely drops from 13.87× to ~8-10× — still very strong but showing ʿAzīz+Ḥakīm is the dominant contributor.

## Bonferroni

Single test (k=1), alpha=0.05 on the match-rate decision. Leave-one-out is descriptive (no p-value).

## Garden-of-forking-paths

1. 20-name list locked BEFORE running (composition justified above).
2. Matching rule locked BEFORE running (same as [[h-new-140-divine-name-pair-cohesion|H-NEW-140]]).
3. Decision thresholds (50%, 30%) locked BEFORE seeing match rate.
4. Seed 20260417 (no randomness in core test, only for any permutation sub-tests).

## Files

- Pre-reg: this file
- Script: `scripts/h_new_140_1_all_pair.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-140-1.json`
- Findings: `findings/phase-b-hypotheses/h-new-140-1-all-pair-decircularization.md`

## Cross-references

- Parent: [[h-new-140-divine-name-pair-cohesion|H-NEW-140]] (paired-names PASS-DIRECTED)
- Audit flag: audit-037 selection-circularity adversarial critique
- Runtime: <1 minute (simple counting)
