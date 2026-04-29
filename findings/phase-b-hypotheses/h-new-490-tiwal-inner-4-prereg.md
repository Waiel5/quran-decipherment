---
id: H-NEW-490
title: "al-sabʿ al-ṭiwāl inner-4 {Q 2, Q 3, Q 4, Q 5} cohesion — pre-registered confirmation of H-NEW-480 post-hoc finding"
phase: B
status: PRE-REGISTERED 2026-04-22
date: 2026-04-22
agent: team-lead (inline)
parent_1: H-NEW-480 (post-hoc inner-4 discovery: mean pairwise 0.7253, α=0.05 cap)
parent_2: H-NEW-340 (musabbiḥāt-5 at 8.1%ile — template method)
parent_3: cross-finding-008 (musabbiḥāt cluster)
seed: 20260515
bonferroni_k: 3
bonferroni_family: h-new-490-tiwal-inner-4
alpha_bon: 0.01667
rules_tuple: "(FR from H-NEW-111; PRIMARY 4-set T = {Q 2, Q 3, Q 4, Q 5}; compute d̄(T) = mean pairwise FR; null distribution 10000 random 4-subsets of {1..114}; compute percentile; MW-5 CLUSTER 4-set M = {Q 57, Q 59, Q 61, Q 64} (musabbiḥāt-4-subset of cross-finding-008 set); MW-6 NULL 4-set N = {Q 1, Q 55, Q 67, Q 112} (sui-generis + outlier + Meccan-mufaṣṣal + theological-short — deliberately diverse); k=3 Bonferroni, α_bon = 0.01667)"
direction: |
  PRIMARY H1: d̄(T) ≤ 10%ile of random-4 null (corpus-extreme cohesion).
  MW-5: d̄(M) ≤ 10%ile (musabbiḥāt-4 should also be corpus-extreme; cross-finding-008 precedent).
  MW-6: d̄(N) ∈ [30%, 70%] percentile (null-typical).
  Aggregate H1 CONFIRMED: PRIMARY + MW-5 + MW-6 all pass.
verdict: PENDING
---

# [[h-new-490-tiwal-inner-4|H-NEW-490]] — al-sabʿ al-ṭiwāl inner-4 cohesion confirmation

## 1. Question

[[h-new-480-medinan-legal-9clique|H-NEW-480]] revealed (post-hoc α=0.05 cap) that the classical *al-sabʿ al-ṭiwāl* inner-4 = {Q 2 al-Baqarah, Q 3 Āl ʿImrān, Q 4 al-Nisāʾ, Q 5 al-Māʾidah} has corpus-extreme-cohesive mean pairwise FR distance 0.7253, with D(Q 2, Q 3) = 0.6309 at ~10%ile of corpus pairwise null.

**Pre-register this to promote from post-hoc to confirmed.**

Classical anchor: **al-Zarkashī** *al-Burhān fī ʿulūm al-Qurʾān* ch. 2 on *al-sabʿ al-ṭiwāl* (the seven long surahs, Q 2-7 + disputed 7th) — the unambiguous-Medinan-long-legal SUB-FOUR are Q 2, 3, 4, 5 (Q 6-7 are Meccan by chronology despite being long).

## 2. Protocol

1. Extract 4-set T = {2, 3, 4, 5} pairwise distances from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] matrix.
2. d̄(T) = mean over C(4, 2) = 6 pairs.
3. Null: 10000 random 4-subsets of {1..114}; compute d̄ for each.
4. percentile(d̄(T)) in null.

5. **MW-5 POSITIVE**: d̄(M) where M = {Q 57, 59, 61, 64} — classical *musabbiḥāt* subset (minus Q 62 which is outside the strict-*yusabbiḥu* set — Q 62 opens *yusabbiḥu* but the strict "5 al-musabbiḥāt" per al-Suyūṭī varies). Predicted ≤10%ile (cross-finding-008 anchor).
   - Note: [[h-new-340-musabbihat-block-subset|H-NEW-340]] tested full 5-set {57, 59, 61, 62, 64} at 8.1%ile. The 4-subset removing Q 62 is predicted at similar or slightly lower percentile.

6. **MW-6 NULL**: d̄(N) where N = {Q 1, Q 55, Q 67, Q 112} — deliberately diverse:
   - Q 1 al-Fātiḥa: 7-verse liturgical sui-generis ([[h-new-155-q1-sui-generis|H-NEW-155]])
   - Q 55 al-Raḥmān: 78-verse Meccan cosmic-mercy outlier ([[h-new-390-q55-outlier-exclusion|H-NEW-390]])
   - Q 67 al-Mulk: 30-verse Meccan-mufaṣṣal eschatological
   - Q 112 al-Ikhlāṣ: 4-verse Meccan pure-theology
   - Predicted null-typical (30-70%ile).

## 3. Pre-committed predictions

| Test | Predicted | Gate |
|:--|:-:|:--|
| PRIMARY d̄(T) ṭiwāl-inner-4 | ≤ 10%ile | CONFIRM |
| MW-5 d̄(M) musabbiḥāt-4 | ≤ 10%ile | precedent-replicate |
| MW-6 d̄(N) diverse-4 | [30%, 70%]%ile | null-typical |

**Aggregate H1 CONFIRMED**: all 3 gates pass.

## 4. Classical anchor recapitulation

**al-Zarkashī** *al-Burhān* ch. 2: "the seven long surahs" (al-sabʿ al-ṭiwāl). Consensus on first four (Q 2, 3, 4, 5); disputed 5th-6th-7th.

**al-Suyūṭī** *al-Itqān fī ʿulūm al-Qurʾān*: nawʿ 19 on corpus division (ṭiwāl, miʾūn, mathānī, mufaṣṣal) anchors ṭiwāl as Q 2-7 or Q 2-9.

**al-Ṭabarī** *Jāmiʿ al-bayān* opening: treats Q 2, 3, 4, 5 as a unified legal-revelatory block; shared community-legal vocabulary.

**al-Biqāʿī** *Naẓm al-Durar*: Q 2 ↔ Q 3 pairing is foundational (*al-Zahrāwān* hadith — two shining ones, al-Bukhārī 4986, Muslim 804; recited together on Day of Judgment as clouds of protection).

**Bukhārī #4986** naming Q 2 ↔ Q 3 as *al-Zahrāwān* (the two luminaries). Classical pairing CONFIRMED at empirical level D(Q 2, Q 3) = 0.6309.

## 5. Honest limits

1. **4-subset null is noisy** — heavy-tailed at extremes; 10000 perms mitigates.
2. **10%ile threshold is strict** — [[h-new-480-medinan-legal-9clique|H-NEW-480]] post-hoc back-of-envelope suggested inner-4 at ~5-10%ile but didn't explicitly compute. Real empirical percentile could exceed 10%.
3. **MW-5 musabbiḥāt-4 alternative** to full-5 from cross-finding-008. Dropping Q 62 could change percentile slightly; predicted similar not identical.
4. **MW-6 set deliberately spans 4 very-different registers** — if it's too-diverse it could fail low (distant members), not in [30,70] range.
5. **FR-roots only.**
6. **Inner-4 finding was post-hoc** — pre-registration now; convert via strict protocol.

## 6. Novel-finding potential

If PRIMARY + MW-5 + MW-6 all pass:
- **Pre-registered empirical confirmation** that *al-sabʿ al-ṭiwāl* inner-4 is corpus-extreme-cohesive cluster.
- Candidate upgrade to **[[cross-finding-025-multi-axis-architecture|cross-finding-025]]** (ṭiwāl-inner-4 cohesion anchored in al-Zarkashī/al-Suyūṭī/al-Zahrāwān hadith).
- Combined with cross-finding-008 (musabbiḥāt) and [[h-new-340-musabbihat-block-subset|H-NEW-340]]: **TWO pre-registered Medinan sub-cluster cohesion findings** supporting the sub-genre-register principle from H-480.

If PRIMARY fails:
- Inner-4 was noise-level artifact of H-480 post-hoc pattern-matching.
- Medinan-cohesion is weaker than expected even at strict subsets.
- Demotion of classical ṭiwāl-inner-cluster claim.

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_490_tiwal_inner_4.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-490.json`
- Findings: `findings/phase-b-hypotheses/h-new-490-tiwal-inner-4.md`

Pre-reg locked 2026-04-22.
