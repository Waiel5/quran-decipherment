---
id: H-NEW-540
title: "Mufaṣṣal-awsāṭ (Q 78-92) middle-mufaṣṣal cohesion — is al-Suyūṭī's tripartite division 3-cluster or 2-cluster empirical?"
phase: B
status: PRE-REGISTERED 2026-04-22
date: 2026-04-22
agent: team-lead (inline)
parent_1: H-NEW-500 (mufaṣṣal-qiṣār confirmed at 0.00%ile)
parent_2: al-Suyūṭī *Itqān* nawʿ 19 (classical tripartite)
parent_3: P8 4-region architecture (region-4 boundary question)
seed: 20260517
bonferroni_k: 3
bonferroni_family: h-new-540-mufassal-awsat-middle
alpha_bon: 0.01667
rules_tuple: "(FR from H-NEW-111; PRIMARY 15-set A = {Q 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92} — al-Suyūṭī mufaṣṣal-awsāṭ; compute d̄(A) = mean pairwise; null 10000 random 15-subsets; percentile; MW-5 REPLICATION: d̄(mufaṣṣal-qiṣār Q 93-114 N=22) ≤ 1%ile (should reconfirm H-500); MW-6 NULL: 15 Meccan-mid-length random sample {Q 26, 28, 37, 39, 41, 43, 45, 50, 52, 54, 56, 67, 68, 71, 75} expected null-typical. k=3 Bonferroni.)"
direction: |
  PRIMARY H1: d̄(A) ≤ 5%ile of random-15 null.
  MW-5: d̄(qiṣār-22) ≤ 1%ile (H-500 replication with fresh seed).
  MW-6: d̄(diverse-15) ∈ [30%, 70%] range.
  Aggregate H1 CONFIRMED: al-Suyūṭī tripartite is 3-cluster empirical.
  Aggregate H1 NULL on PRIMARY: tripartite is 2-cluster (ṭiwāl + qiṣār) with awsāṭ transitional.
verdict: PENDING
---

# [[h-new-540-mufassal-awsat-middle|H-NEW-540]] — Mufaṣṣal-awsāṭ middle-cluster test

## 1. Question

[[h-new-500-mufassal-qisar-super-cluster|H-NEW-500]] confirmed *mufaṣṣal-qiṣār* (Q 93-114) as corpus super-cluster at 0.00%ile. al-Suyūṭī *Itqān* nawʿ 19 divides mufaṣṣal into THREE sub-genres:
- *mufaṣṣal al-ṭiwāl* (long): Q ~50-77
- ***mufaṣṣal al-awsāṭ*** (middle): **Q ~78-92** — this test
- *mufaṣṣal al-qiṣār* (short): Q 93-114 (H-500 confirmed)

**Is mufaṣṣal-awsāṭ ALSO empirically cohesive, or is it a transition-zone between ṭiwāl and qiṣār?**

If cohesive: al-Suyūṭī's tripartite is 3-cluster empirical — genre division fully validated.
If NULL: tripartite is 2-cluster (ṭiwāl + qiṣār) empirical — awsāṭ is transitional.

## 2. Protocol

1. **PRIMARY Set A** = {Q 78 al-Nabaʾ, 79 al-Nāziʿāt, 80 ʿAbasa, 81 al-Takwīr, 82 al-Infiṭār, 83 al-Muṭaffifīn, 84 al-Inshiqāq, 85 al-Burūj, 86 al-Ṭāriq, 87 al-Aʿlā, 88 al-Ghāshiyah, 89 al-Fajr, 90 al-Balad, 91 al-Shams, 92 al-Layl}, N=15.

2. d̄(A) = mean pairwise FR over C(15, 2) = 105 pairs.

3. Null: 10000 random 15-subsets of {1..114}.

4. **PRIMARY H1**: d̄(A) ≤ 5%ile.

5. **MW-5 REPLICATION**: d̄(mufaṣṣal-qiṣār Q 93-114, N=22) ≤ 1%ile (fresh seed 20260517+1). Should reconfirm H-500 at 0.00%ile.

6. **MW-6 NULL**: {Q 26, 28, 37, 39, 41, 43, 45, 50, 52, 54, 56, 67, 68, 71, 75}, N=15 Meccan-mid-length sample. Predicted null-typical.

## 3. Pre-committed predictions

| Test | Predicted | Gate |
|:--|:-:|:--|
| PRIMARY d̄(A) awsāṭ | ≤ 5%ile | al-Suyūṭī tripartite 3-cluster |
| MW-5 d̄(qiṣār-22) | ≤ 1%ile | replicate H-500 |
| MW-6 d̄(diverse-15) | [30%, 70%]%ile | null-typical |

**Aggregate H1 CONFIRMED**: all 3 pass.

## 4. Honest limits

1. **Awsāṭ boundary varies by classical source**: some cite Q 79-91 or Q 88-92. I use Q 78-92 (al-Suyūṭī majority).
2. **Awsāṭ contains heterogeneous openings**: 7 oath-openings (Q 79, 81, 85, 86, 89, 91, 92) vs 8 non-oath (Q 78, 80, 82, 83, 84, 87, 88, 90) — split ~half and half.
3. **Q 78 al-Nabaʾ is a boundary surah** — classically flagged as *al-Nabaʾ al-ʿaẓīm*, prominence-tension with strict-awsāṭ.
4. **N=15 subset null** has moderate noise at 5%ile threshold.
5. **FR-roots only.**
6. **MW-6 comparator** may be diverse-enough to null or undercohesive (learned from H-500).

## 5. Classical anchors

**al-Suyūṭī** *Itqān* nawʿ 19: tripartite boundaries approximately Q 50/Q 78/Q 93.

**Shared features of awsāṭ surahs**:
- Heavy oath-opening cluster (Q 79, 81, 85, 86, 89, 91, 92): *wa-al-nāziʿāt, idhā al-shamsu kuwwirat, wa-al-samāʾi dhāti al-burūj, wa-al-samāʾi wa-al-ṭāriq, wa-al-fajr, wa-al-shamsi wa-ḍuḥāhā, wa-al-layli idhā yaghshā*.
- Cosmic-eschatological imagery (Q 79, 81, 82, 84, 88, 89).
- Mid-length verses (denser than qiṣār, shorter than ṭiwāl).

**al-Zarkashī** *Burhān* ch. 2 same tripartite.

**Opposing tradition**: some scholars (al-Ḥuṣrī) treat mufaṣṣal as bipartite (ṭiwāl + qiṣār only), with awsāṭ as disputed middle-range. This test bears on that debate.

## 6. Novel-finding potential

If PRIMARY PASSES:
- al-Suyūṭī tripartite empirically 3-cluster confirmed.
- Awsāṭ as middle cluster joins qiṣār-22 (H-500 0.00%) and possibly ṭiwāl (untested here) as 3-level mufaṣṣal architecture.
- Strengthens [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] candidate into multi-level mufaṣṣal-super-structure.

If PRIMARY NULL:
- al-Suyūṭī tripartite is 2-cluster empirical; awsāṭ is transition-heterogeneity.
- al-Ḥuṣrī-style bipartite is empirically preferred.
- Classical scholarly dispute resolved in favor of bipartite.

Either way, novel finding.

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_540_mufassal_awsat_middle.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-540.json`
- Findings: `findings/phase-b-hypotheses/h-new-540-mufassal-awsat-middle.md`

Pre-reg locked 2026-04-22.
