---
id: H-NEW-550
title: "Mufaṣṣal-ṭiwāl (Q 50-77) cohesion — completing al-Suyūṭī tripartite empirical test"
phase: B
status: PRE-REGISTERED 2026-04-22
date: 2026-04-22
agent: team-lead (inline)
parent_1: H-NEW-540 (awsāṭ confirmed 0.00%)
parent_2: H-NEW-500 (qiṣār confirmed 0.00%)
parent_3: al-Suyūṭī *Itqān* nawʿ 19 tripartite
seed: 20260518
bonferroni_k: 3
bonferroni_family: h-new-550-mufassal-tiwal-completion
alpha_bon: 0.01667
rules_tuple: "(FR from H-NEW-111; PRIMARY 28-set T = {Q 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77} al-Suyūṭī mufaṣṣal-ṭiwāl; compute d̄(T); null 10000 random 28-subsets; percentile; MW-5 REPLICATE: d̄(awsāṭ Q 78-92 N=15) ≤ 1%ile (H-540 replication); MW-6 NULL: 28 RANDOM diverse non-mufaṣṣal surahs deliberately selected for corpus-diversity; k=3 Bonferroni α_bon=0.01667)"
direction: |
  PRIMARY H1: d̄(T) ≤ 5%ile of random-28 null.
  GRADIENT prediction: d̄(T) in [0.70, 0.90] — between awsāṭ (0.62) and corpus median (0.96), per progressive-tightening pattern.
  MW-5: d̄(awsāṭ) ≤ 1%ile (H-540 replication).
  MW-6: d̄(diverse-28) in [30%, 70%] range.
  Aggregate H1 CONFIRMED: al-Suyūṭī tripartite 3/3 empirically validated.
verdict: PENDING
---

# [[h-new-550-mufassal-tiwal-completion|H-NEW-550]] — Mufaṣṣal-ṭiwāl tripartite completion test

## 1. Question

[[h-new-500-mufassal-qisar-super-cluster|H-NEW-500]] confirmed qiṣār (Q 93-114) and [[h-new-540-mufassal-awsat-middle|H-NEW-540]] confirmed awsāṭ (Q 78-92) as corpus-extreme-cohesive clusters at 0.00%ile. **Does mufaṣṣal-ṭiwāl (Q 50-77) also confirm as al-Suyūṭī's third sub-genre?**

If yes at ≤5%ile: al-Suyūṭī tripartite empirically 3/3 validated; P8 region-4 extends to entire mufaṣṣal {Q 50-114, 65 surahs}.
If NULL: ṭiwāl is empirically heterogeneous; classical ṭiwāl-qiṣār boundary is looser than qiṣār-awsāṭ.

## 2. Protocol

PRIMARY Set T = Q 50-77 (28 surahs): {al-Qāf, al-Dhāriyāt, al-Ṭūr, al-Najm, al-Qamar, al-Raḥmān, al-Wāqiʿah, al-Ḥadīd, al-Mujādilah, al-Ḥashr, al-Mumtaḥanah, al-Ṣaff, al-Jumuʿa, al-Munāfiqūn, al-Taghābun, al-Ṭalāq, al-Taḥrīm, al-Mulk, al-Qalam, al-Ḥāqqah, al-Maʿārij, Nūḥ, al-Jinn, al-Muzzammil, al-Muddaththir, al-Qiyāmah, al-Insān, al-Mursalāt}.

Note the set spans Meccan (Q 50-56, 67-75 ±) AND Medinan (Q 57-66). This is a **register-heterogeneous set** by chronology.

1. d̄(T) over C(28,2)=378 pairs.
2. Null: 10000 random 28-subsets.
3. **PRIMARY H1**: d̄(T) ≤ 5%ile.

4. **MW-5 REPLICATION**: d̄(awsāṭ Q 78-92, N=15) ≤ 1%ile.

5. **MW-6 DIVERSE-28**: random diverse corpus sample = {Q 1, 2, 3, 12, 18, 19, 20, 22, 24, 26, 28, 30, 33, 36, 37, 38, 40, 42, 45, 47, 48, 49, 79, 85, 90, 96, 99, 110}. Non-mufaṣṣal-ṭiwāl; mix of genres. Predicted null-typical.

## 3. Pre-committed predictions

| Test | Predicted | Gate |
|:--|:-:|:--|
| PRIMARY d̄(T) ṭiwāl-28 | ≤ 5%ile, gradient d̄ ∈ [0.70, 0.90] | CONFIRM |
| MW-5 d̄(awsāṭ-15) | ≤ 1%ile | H-540 replicate |
| MW-6 d̄(diverse-28) | [30%, 70%] | null-typical |

**Aggregate H1 CONFIRMED**: tripartite 3/3. Upgrade [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] to include full 65-surah mufaṣṣal.

## 4. Honest limits

1. **Ṭiwāl is Meccan+Medinan heterogeneous** — predicted looser than awsāṭ due to chronology-mixing.
2. **Q 57-66 are Medinan musabbiḥāt+community-legal block** — partially cohesive within-block (cross-finding-008) but heterogeneous relative to Meccan Q 50-56, 67-77.
3. **Boundary (Q 50 start)** per al-Suyūṭī majority; disputed.
4. **N=28 large** — percentile resolution ~0.5pp at extreme.
5. **MW-6 is larger diverse set; informed by H-500/H-540 comparator-failure lessons**.
6. **FR-roots only.**

## 5. Classical anchor

al-Suyūṭī *Itqān* nawʿ 19 ṭiwāl boundary: ~Q 49/50 start, Q 77 end. Internal heterogeneity acknowledged — classical tradition notes ṭiwāl spans Meccan-Medinan but shares "extended mufaṣṣal-separation" (high *fāṣila*-density between verses).

al-Zarkashī *Burhān* vol. 1 ch. 2: agrees.

**Expected mechanism**: ṭiwāl cohesion would reflect shared mid-length-surah register (30-100 verses typical), eschatological and liturgical themes, even though chronology mixes.

## 6. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_550_mufassal_tiwal_completion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-550.json`
- Findings: `findings/phase-b-hypotheses/h-new-550-mufassal-tiwal-completion.md`

Pre-reg locked 2026-04-22.
