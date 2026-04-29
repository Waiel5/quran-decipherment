---
id: H-NEW-480
title: "Medinan social-legal 9-clique cohesion — is {Q 2, 3, 4, 5, 24, 33, 48, 49, 64} a genuine cluster?"
phase: B
status: PRE-REGISTERED 2026-04-21
date: 2026-04-21
agent: team-lead (inline)
parent_1: H-NEW-460 (post-hoc identification of Medinan-social-legal cluster from top-5 nearest-neighbors of Q 24 and Q 33)
parent_2: cross-finding-008 (musabbiḥāt cluster as precedent — show method works)
parent_3: H-NEW-340 (musabbiḥāt 5-block at 8.1%ile)
seed: 20260514
bonferroni_k: 3
bonferroni_family: h-new-480-medinan-legal-9clique
alpha_bon: 0.01667
rules_tuple: "(FR from H-NEW-111; PRIMARY 9-set A = {Q 2, 3, 4, 5, 24, 33, 48, 49, 64} identified from H-NEW-460 top-5-neighbor analysis; compute d̄(A) = mean pairwise FR; null distribution: 10000 random 9-subsets of {1..114}; compute percentile of observed d̄; MW-5 CLUSTER 9-set B = random 9-subset of musabbiḥāt + mufaṣṣal-ṭiwāl {Q 50, 54, 57, 59, 61, 64, 67, 76, 78}; predicted moderate-cohesion; MW-6 NULL 9-set C = 9 random surahs spanning chronology + register {Q 1, 12, 36, 38, 55, 67, 90, 101, 114}; predicted null-typical; k=3 Bonferroni, α_bon = 0.01667)"
direction: |
  PRIMARY H1: d̄(A) ≤ 10%ile of random-9 null (corpus-extreme cohesion).
  MW-5: d̄(B) ≤ 25%ile (moderate-cohesion sanity — different cluster, cohesion-detectable).
  MW-6: d̄(C) ∈ [30%, 70%] percentile range (null-typical — instrument doesn't over-flag arbitrary 9-sets).
  Aggregate H1 CONFIRMED: PRIMARY + MW-5 + MW-6 all pass.
verdict: PENDING
---

# [[h-new-480-medinan-legal-9clique|H-NEW-480]] — Medinan social-legal 9-clique cohesion

## 1. Question

[[h-new-460-q24-q33-hijab-pair|H-NEW-460]] discovered (post-hoc, α=0.05 cap) that Q 24 and Q 33 both cluster with a set of Medinan social-legal surahs at top-5-nearest-neighbor rank. The union of their top-5 lists yields 9 unique surahs:

**Set A = {Q 2, Q 3, Q 4, Q 5, Q 24, Q 33, Q 48, Q 49, Q 64}**

All are Medinan. All engage community-ethical-legal register. **Does this set form a genuine empirical cluster (corpus-extreme cohesion) or is the nearest-neighbor pattern an artifact of individual proximity without whole-set cohesion?**

Pre-registered falsification: compare d̄(A) = mean pairwise FR distance against 10000 random 9-subset null. If ≤10%ile, cluster is genuine and pre-registered.

## 2. Protocol

1. Extract 9-set A distances from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] matrix; compute d̄(A) = mean over C(9,2) = 36 pairs.
2. Null: 10000 random 9-subsets of {1..114}; compute d̄ for each.
3. percentile(d̄(A)) in null.
4. **PRIMARY H1**: d̄(A) ≤ 10%ile.

5. **MW-5 POSITIVE CLUSTER CONTROL (Set B)**: 9 surahs from musabbiḥāt + mufaṣṣal-ṭiwāl = {Q 50, Q 54, Q 57, Q 59, Q 61, Q 64, Q 67, Q 76, Q 78}. This set mixes eschatological-warnings (Q 50, Q 54, Q 67, Q 76, Q 78) with musabbiḥāt-community (Q 57, Q 59, Q 61, Q 64) — should be moderately cohesive (~20-25%ile). Tests that the metric detects DIFFERENT cluster structures.

6. **MW-6 NULL CONTROL (Set C)**: 9 deliberately-diverse surahs = {Q 1, Q 12, Q 36, Q 38, Q 55, Q 67, Q 90, Q 101, Q 114}. Mix of sui-generis (Q 1), monograph (Q 12), Meccan ḥawāmīm (Q 38, 40s-adjacent), Q 55 outlier, terminal-mufaṣṣal. Should NOT cluster (predict ~40-60%ile = null-typical).

## 3. Pre-committed predictions

| Test | Predicted | Gate |
|:--|:-:|:--|
| PRIMARY d̄(A) Medinan-legal | ≤ 10%ile | PASS |
| MW-5 d̄(B) musabbiḥāt+mufaṣṣal | ≤ 25%ile | moderate-cohesion |
| MW-6 d̄(C) diverse-9 | 30-70%ile range | null-typical |

**Aggregate H1 CONFIRMED**: PRIMARY + MW-5 + MW-6 all pass.

**H0 alternatives**:
- PRIMARY fails: 9-set is not corpus-extreme cohesive; individual proximity ≠ cluster.
- MW-5 fails (much lower than 25%): musabbiḥāt+mufaṣṣal set is MORE cohesive than Medinan-legal (surprising but interpretable).
- MW-6 fails (extreme low or high): instrument calibration issue.

## 4. Classical-scholarship anchor

The proposed 9-surah set corresponds to the classical genre of ***āyāt al-aḥkām***  (verses-of-rulings):

- **al-Qurṭubī** *al-Jāmiʿ li-aḥkām al-Qurʾān* — organizes commentary specifically by ruling-verse density; Q 2, 3, 4, 5, 24, 33 are primary sources (al-Shanqīṭī's *Aḍwāʾ al-bayān* estimates ~60% of legal verses originate in these).
- **al-Jaṣṣāṣ** *Aḥkām al-Qurʾān* vol. 1-5: focuses on legal-ruling derivation from Q 2, 3, 4, 5 (Ḥanafī-jurisprudential).
- **al-Shāfiʿī** *Aḥkām al-Qurʾān* (compiled by al-Bayhaqī): treats Q 24 and Q 33 as family-law-specific legal anchors.

**Q 48 al-Fatḥ** (added to set via Q 33's top-5): Medinan, al-Ḥudaybiyya-treaty — contains legal-treaty precedent, fits community-legal register.
**Q 49 al-Ḥujurāt** (added via Q 24's top-5): Medinan, social-conduct-etiquette legislation.
**Q 64 al-Taghābun** (added via Q 24's top-5): Medinan, musabbiḥāt + eschatological-balance — legal-ethical overlap.

The 9-set spans: **foundational legal (2, 3, 4, 5), family-law (24, 33), legal-treaty (48), community-etiquette (49), eschatological-legal-ethics (64)**.

If empirically cohesive, this set is a data-driven confirmation of the classical ***āyāt al-aḥkām*** genre as whole-surah category.

## 5. Honest limits

1. **9-set identified POST-HOC from H-460 top-5 neighbors** — garden-of-forking-paths concern. Mitigation: pre-registered ≤10%ile threshold is a STRICT test; individual proximity ≠ whole-set cohesion.
2. **All 9 are Medinan** — chronology-artifact possible. MW-5 Set B is mixed Meccan-Medinan, providing some discrimination.
3. **Set size 9 is small** — null distribution heavy-tailed. 10000 perms mitigates.
4. **FR-roots only.**
5. **Bonferroni k=3 at α_bon=0.01667** — effect size ~10%ile is well-defined regardless of permutation noise.
6. **Classical scholarship citation relies on Jaṣṣāṣ/Shāfiʿī/Qurṭubī** — general genre-level, not specific passage-citation for each of the 9 surahs.

## 6. Novel-finding potential

If PRIMARY passes:
- Empirical confirmation that ***āyāt al-aḥkām*** is a data-driven genre at whole-surah level (not just verse-level).
- Refinement of [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] outlier-factor: Type-A ROBUST outliers Q 24 and Q 33 are members of a broader 9-surah chronology-homogeneous cohesive cluster.
- **Candidate new [[cross-finding-025-multi-axis-architecture|cross-finding-025]]: *āyāt al-aḥkām* = empirically-cohesive Medinan-legal-cluster at FR ≤10%ile**.

If PRIMARY fails:
- Individual-proximity ≠ cluster-cohesion; the nearest-neighbor method is not suitable for cluster detection.
- Classical *aḥkām* genre is topic-level, not whole-surah-level — consistent with H-460 finding.

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_480_medinan_legal_9clique.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-480.json`
- Findings: `findings/phase-b-hypotheses/h-new-480-medinan-legal-9clique.md`

Pre-reg locked 2026-04-21.
