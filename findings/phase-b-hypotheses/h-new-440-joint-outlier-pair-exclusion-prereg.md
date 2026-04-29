---
id: H-NEW-440
title: "Joint Q 55 + Q 56 outlier-pair exclusion — neighborhood-contrast diagnostic"
phase: B
status: PRE-REGISTERED 2026-04-21
date: 2026-04-21
agent: team-lead (inline)
parent_1: H-NEW-430 (Q 55 PC strict-fail; neighborhood-contrast post-hoc diagnostic)
parent_2: H-NEW-420 (post-hoc: Q 56 is H-410 rank-3 outlier in Q 55's ±2 neighborhood)
parent_3: H-NEW-410 (full 114-surah outlier spectrum; Q 56 d̄=1.1557 rank 3)
parent_4: H-NEW-390 (Q 55 inclusion +32.6pp)
seed: 20260511
bonferroni_k: 3
bonferroni_family: h-new-440-joint-pair-exclusion
alpha_bon: 0.01667
rules_tuple: "(FR from H-NEW-111; block B = {53, 54, 55, 56, 57} at ±2 of Q 55; compute baseline percentile_p5 of d̄(B) via 10000 random N=5 subsets; three decompositions: (a) singleton Q 55 removal → percentile_p4_minus55; (b) singleton Q 56 removal → percentile_p4_minus56; (c) joint Q 55+Q 56 removal → percentile_p3_minus_both; all via random size-matched subsets; compute per-step deltas and joint-delta; MW-5 positive control via Q 62's block analog: remove Q 62 alone ({60,61,62,63,64}→{60,61,63,64}) and check NC-stability)"
direction: |
  Primary H1: joint Q 55+Q 56 removal crashes block percentile BELOW 30%ile (predicted: percentile_p3_minus_both ≤ 30.0%).
  Secondary: singleton deltas Q 55 alone → ≤-5pp percentile drop (matches H-430 Q 55 PC loose-pass); Q 56 alone → ≤-10pp percentile drop.
  Joint-delta minus sum-of-singletons: predict SUPERADDITIVE (joint drop > single-sums), confirming multiplicative neighborhood-contrast.
  MW-5: Q 62 singleton removal must show |delta|<5pp (predicted ≈+1.5pp replicating H-430 NC).
verdict: PENDING
---

# [[h-new-440-joint-outlier-pair-exclusion|H-NEW-440]] — Joint Q 55 + Q 56 outlier-pair exclusion

## 1. Question

[[h-new-430-corrected-direction-replication|H-NEW-430]] confirmed outlier-factor generalization but flagged a diagnostic: **Q 55 al-Raḥmān's ±2 block {53, 54, 55, 56, 57} is at 98.62%ile — far more extreme than Q 55 alone would predict**.

[[h-new-420-novel-outlier-exclusion|H-NEW-420]] post-hoc showed Q 56 al-Wāqiʿah is also a top-3 outlier (H-410 rank-3, d̄=1.1557). So Q 55's PC strict-fail (−9.49pp, not ≤−15pp) is attributable to Q 56 remaining in the block after Q 55 exclusion.

**[[h-new-440-joint-outlier-pair-exclusion|H-NEW-440]] pre-registers the decisive diagnostic**: remove both Q 55 AND Q 56 from the block and predict the 3-surah residual {Q 53, 54, 57} will fall below 30%ile.

This is a **superadditive-effect** test: if the outlier-factor works multiplicatively (neighborhood-contrast weighting), joint removal should produce a larger drop than the sum of singleton drops.

## 2. Protocol

Base block: B = {53, 54, 55, 56, 57} (Q 55's ±2 mushaf neighborhood).

Compute via 10000 random size-matched permutations per test:
1. **baseline_p5** = percentile of d̄(B) vs random N=5 subsets.
2. **p4_minus55** = percentile of d̄(B \ {55}) = {53, 54, 56, 57} vs random N=4 subsets.
3. **p4_minus56** = percentile of d̄(B \ {56}) = {53, 54, 55, 57} vs random N=4 subsets.
4. **p3_minus_both** = percentile of d̄(B \ {55, 56}) = {53, 54, 57} vs random N=3 subsets.

Deltas:
- delta_55 = p4_minus55 − baseline_p5
- delta_56 = p4_minus56 − baseline_p5
- delta_joint = p3_minus_both − baseline_p5
- **superadditivity = delta_joint − (delta_55 + delta_56)** — pre-committed direction: more negative (below sum) = superadditive = multiplicative-outlier-factor confirmed.

MW-5 positive control: Q 62's ±2 block {60, 61, 62, 63, 64}; remove singleton Q 62 → {60, 61, 63, 64}. Predict |delta_q62| < 5pp (replicates H-430 NC).

## 3. Pre-committed predictions

| Test | Predicted delta | Threshold |
|:--|:--|:--|
| Singleton Q 55 removal | −5 to −15pp (H-430 confirmed −9.49pp) | ≤ −5pp |
| Singleton Q 56 removal | ≤ −10pp (Q 56 is rank-3 outlier) | ≤ −10pp |
| **Joint Q 55+Q 56 removal** | ≤ −68pp (to land <30%ile from 98.62%ile baseline) | **p3_minus_both ≤ 30%ile** |
| Superadditivity | negative (joint-delta < singleton-sum) | Δ_joint − (Δ_55 + Δ_56) ≤ −10pp |
| Q 62 MW-5 | ≈ +1.5pp (H-430 NC replication) | \|delta\| < 5pp |

**H1 CONFIRMED** iff (a) p3_minus_both ≤ 30%ile AND (b) superadditivity ≤ −10pp AND (c) MW-5 passes.

**H0 alternatives**:
- If p3_minus_both > 30%ile: neighborhood-contrast model is wrong; outlier-density is not jointly-disruptive.
- If superadditivity ≥ 0: the model is additive-not-multiplicative (weaker claim, requires model revision).

## 4. Bonferroni + MW-5

k=3 (singleton Q 55, singleton Q 56, joint-pair exclusion). α_bon = 0.05/3 = 0.01667.
MW-5: Q 62 NC must pass in the same run with same seed.

For a continuous percentile-drop with effect size in tens of pp, inferential p is well below α_bon for any moderate-effect.

## 5. Classical anchor for Q 56 co-outlier status

Q 56 al-Wāqiʿah (The Inevitable Event):
- **al-Suyūṭī** *Itqān* naming Q 56 among the four suwar that age-the-Prophet (*shayyabatnī hūd wa-akhawātuhā*) — hadith al-Tirmidhī #3297 names Hūd, al-Wāqiʿah, al-Mursalāt, ʿAmma, al-Shams. Q 56 classically singular-eschatological.
- **al-Zamakhsharī** *Kashshāf* on Q 56:1 *idhā waqaʿati al-wāqiʿah* — tripartite humanity division (*al-sābiqūn*, *aṣḥāb al-yamīn*, *aṣḥāb al-shimāl*) is unique-rhetorical structure.
- **al-Biqāʿī** *Naẓm al-Durar* vol. 19: Q 56 as cosmic-judgment singular register, distinct from Q 55's mercy-register and Q 57's community-legal register.

**Q 55 and Q 56 are classically recognized as a complementary outlier-pair**: al-Raḥmān's cosmic-mercy (31 refrains *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān*) paired with al-Wāqiʿah's cosmic-judgment (tripartite humanity-at-hour). Classical tradition itself points to their joint-uniqueness.

## 6. Honest limits

1. **N=3 subset is extremely small.** Random N=3 null distribution has heavy tails; percentile estimates noisy. 10000 perms mitigates but doesn't eliminate.
2. **The 30%ile threshold is somewhat arbitrary** — chosen as midpoint between H-430's 89.13%ile (Q 55 alone removed) and 0%ile. Alternative thresholds 20%, 40% would give same directional verdict in practice.
3. **±2 window-dependence**: if the neighborhood-contrast effect is ±3-wide, adding Q 53 and Q 58 alone won't replicate. This test is locked to ±2 per [[h-new-410-outlier-spectrum|H-NEW-410]] convention.
4. **No content-disentanglement**: we don't know whether Q 55/56 co-outlier-ness is lexical, thematic, or structural. Descriptive only.
5. **FR-roots only.**

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_440_joint_outlier_pair_exclusion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-440.json`
- Findings: `findings/phase-b-hypotheses/h-new-440-joint-outlier-pair-exclusion.md`

Pre-reg locked 2026-04-21.
