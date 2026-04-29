---
id: H-NEW-570
title: "Muqaṭṭaʿāt-29 content-cluster test — does structural letter-opening axis generalize to FR-content cohesion?"
phase: B
status: PRE-REGISTERED 2026-04-22
date: 2026-04-22
agent: team-lead (inline)
parent_1: H-NEW-130 (muqaṭṭaʿāt hub-architecture CONFIRMED at letter-level)
parent_2: cross-finding-011 (mushaf Fisher-Rao framework)
parent_3: H-NEW-500/540/560 (cluster-detection template)
seed: 20260520
bonferroni_k: 3
bonferroni_family: h-new-570-muqattaat-content-cluster
alpha_bon: 0.01667
rules_tuple: "(FR from H-NEW-111; PRIMARY muqaṭṭaʿāt-29 set M = {Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}; compute d̄(M); null 10000 random 29-subsets; percentile; MW-5 HM-7 cluster {Q 40, 41, 42, 43, 44, 45, 46} ≤5%ile — classical ḥawāmīm should be extreme-cohesive; MW-6 size-matched random non-muqaṭṭaʿāt 29-set null-typical [30%, 70%]. k=3 Bonferroni α_bon=0.01667)"
direction: |
  PRIMARY H1: d̄(M) ≤ 10%ile of random-29 null.
  MW-5: d̄(HM-7 {Q 40-46}) ≤ 5%ile — classical ḥawāmīm cluster confirmation.
  MW-6: d̄(non-muq-29 random) [30%, 70%]%ile range.
  Aggregate H1 CONFIRMED: muqaṭṭaʿāt letter-axis generalizes to content-axis cohesion.
  Aggregate NULL: muqaṭṭaʿāt is a PURE letter-structural feature, orthogonal to content — consistent with H-NEW-130 epistemic humility about muqaṭṭaʿāt meaning.
verdict: PENDING
---

# [[h-new-570-muqattaat-content-cluster|H-NEW-570]] — Muqaṭṭaʿāt-29 content-cluster

## 1. Question

**[[h-new-130-fisher-rao-residuals|H-NEW-130]]** established the 29 muqaṭṭaʿāt-opened surahs as distinctive at **letter-architecture level** (shared initial-letter-sequences, hub-structural role). **But does this letter-level distinctiveness generalize to content-level cohesion?**

If d̄(muqaṭṭaʿāt-29) is corpus-extreme: muqaṭṭaʿāt-architecture produces TWO-AXIS distinctiveness (letter + content).
If NULL: muqaṭṭaʿāt is a PURE letter-structural feature, orthogonal to content-clustering — consistent with [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s epistemic stance that muqaṭṭaʿāt "meaning" is not decipherable from content alone.

**Additionally MW-5 tests** whether the classical ḥawāmīm cluster (Q 40-46, 7 consecutive HM-opened surahs) is a confirmed mini-cluster — a specific classical prediction within muqaṭṭaʿāt.

## 2. Protocol

**PRIMARY Set M = 29 muqaṭṭaʿāt-opened surahs**:
- ALM (6): Q 2, 3, 29, 30, 31, 32
- ALMS (1): Q 7
- ALR (5): Q 10, 11, 12, 14, 15
- ALMR (1): Q 13
- KHYʿṢ (1): Q 19
- ṬH (1): Q 20
- ṬSM (2): Q 26, 28
- ṬS (1): Q 27
- YS (1): Q 36
- Ṣ (1): Q 38
- HM (6): Q 40, 41, 43, 44, 45, 46
- ḤM-ʿSQ (1): Q 42
- Q (1): Q 50
- N (1): Q 68

Total = 29. (All muqaṭṭaʿāt per al-Zamakhsharī/al-Suyūṭī consensus; [[h-new-130-fisher-rao-residuals|H-NEW-130]] source).

1. d̄(M) over C(29, 2) = 406 pairs.
2. Null: 10000 random 29-subsets of {1..114}.
3. **PRIMARY H1**: d̄(M) ≤ 10%ile.

4. **MW-5 HM-7**: {Q 40, 41, 42, 43, 44, 45, 46}, ḥawāmīm-7. Predicted ≤ 5%ile.

5. **MW-6 non-muq-29 random sample**: deterministic pseudo-random 29 from non-muqaṭṭaʿāt {1..114} \ muqaṭṭaʿāt-29 — I'll pick {Q 1, 4, 5, 6, 8, 9, 16, 17, 18, 21, 22, 23, 24, 25, 33, 34, 35, 37, 39, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57}. Predicted [30%, 70%]ile.

## 3. Pre-commits

| Test | Predicted | Gate |
|:--|:-:|:--|
| PRIMARY muqaṭṭaʿāt-29 | ≤ 10%ile | CONFIRM content-axis |
| MW-5 HM-7 ḥawāmīm | ≤ 5%ile | classical mini-cluster |
| MW-6 non-muq-29 random | [30%, 70%]%ile | null-typical |

**Aggregate H1 CONFIRMED**: muqaṭṭaʿāt is DUAL-AXIS structural feature (letter + content).
**Aggregate NULL**: muqaṭṭaʿāt is PURE letter-axis feature.

## 4. Classical-scholarship anchor

**al-Zamakhsharī** *al-Kashshāf ʿan ḥaqāʾiq al-tanzīl* on Q 2:1 (ALM): muqaṭṭaʿāt as *al-ḥurūf al-muqaṭṭaʿa* — "the disjoined letters" — distinctive opening feature.

**al-Suyūṭī** *al-Itqān* nawʿ 40 on muqaṭṭaʿāt: tradition's epistemic humility ("*Allāh aʿlam bi-murādihi*" — God knows its intent best). Classical position is that muqaṭṭaʿāt meaning is non-deciphered.

**al-Rāzī** *Mafātīḥ al-ghayb* vol. 2 on muqaṭṭaʿāt: enumerates 20+ classical opinions without resolution — consistent with "meaning is unknown."

**al-Biqāʿī** *Naẓm al-Durar* attempts to find *munāsaba* between muqaṭṭaʿāt opening and each surah's content — a position that would PREDICT content-axis cohesion within each letter-family (e.g., HM surahs share content themes).

**[[h-new-570-muqattaat-content-cluster|H-NEW-570]] tests al-Biqāʿī's position**: if muqaṭṭaʿāt letter-families share content, d̄(M) should be ≤10%ile and MW-5 HM-7 should be ≤5%ile.

If [[h-new-570-muqattaat-content-cluster|H-NEW-570]] NULL: al-Biqāʿī's content-munāsaba claim is empirically unsupported at whole-surah scale; al-Suyūṭī/al-Rāzī epistemic-humility position is vindicated.

## 5. Honest limits

1. **29 muqaṭṭaʿāt-opened span 10+ letter-sequence types** — content-cohesion across letter-families is a strong expectation.
2. **Q 2 (286 verses) + Q 19 (98 verses) vs Q 68 (52 verses) + Q 50 (45 verses)** — large length-variation within set.
3. **Mostly Meccan (Q 2, Q 3 are Medinan; rest Meccan)** — chronology-mixed.
4. **Includes 3 qiṣaṣ surahs** (Q 11 Hūd, Q 12 Yūsuf, Q 28 al-Qaṣaṣ) — overlapping with narrative-register.
5. **MW-6 random-29 selection pre-committed**.
6. **FR-roots only.**
7. **N=29 large** — percentile resolution ~0.3pp.

## 6. Deliverables

Pre-reg this; script `h_new_570_muqattaat_content_cluster.py`; JSON `csv/h-new-570.json`; findings file.

Pre-reg locked 2026-04-22.
