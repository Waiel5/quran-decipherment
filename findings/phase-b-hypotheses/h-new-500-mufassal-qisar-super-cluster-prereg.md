---
id: H-NEW-500
title: "Mufaṣṣal-qiṣār (Q 93-114) as corpus super-cluster — 22-surah cohesion confirming classical al-Suyūṭī Itqān nawʿ 19 genre classification"
phase: B
status: PRE-REGISTERED 2026-04-22
date: 2026-04-22
agent: team-lead (inline)
parent_1: H-NEW-490 (Q 108 hub discovery: 8/10 top-pairs; Q 1↔Q 112 at 1.82%ile)
parent_2: H-NEW-350 (mufaṣṣal-ṭiwāl tested separately; this tests mufaṣṣal-qiṣār terminal subset)
parent_3: cross-finding-008 precedent method
parent_4: P8 (4-region hub architecture predicts region-4 terminal-mufaṣṣal internal cohesion)
seed: 20260516
bonferroni_k: 3
bonferroni_family: h-new-500-mufassal-qisar-super-cluster
alpha_bon: 0.01667
rules_tuple: "(FR from H-NEW-111; PRIMARY 22-set Q = {Q 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114}; compute d̄(Q) = mean pairwise; null distribution 10000 random 22-subsets of {1..114}; compute percentile; MW-5 INNER 12-set QI = {Q 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114} — the 12 shortest mufaṣṣal-qiṣār; MW-6 COMPARATOR 22-set Cm = random sample of Meccan-mid-length surahs (revelation-type-matched but length-differentiated); k=3 Bonferroni, α_bon = 0.01667)"
direction: |
  PRIMARY H1: d̄(Q) ≤ 5%ile of random-22 null (corpus-extreme).
  MW-5: d̄(QI) ≤ 1%ile of random-12 null (inner-mufaṣṣal-qiṣār should be ULTRA-extreme).
  MW-6: d̄(Cm) ∈ [30%, 70%] percentile range of random-22 null (null-typical even though chronology-matched).
  Aggregate H1 CONFIRMED: PRIMARY + MW-5 + MW-6 all pass.
verdict: PENDING
---

# [[h-new-500-mufassal-qisar-super-cluster|H-NEW-500]] — Mufaṣṣal-qiṣār as corpus super-cluster

## 1. Question

[[h-new-490-tiwal-inner-4|H-NEW-490]] revealed Q 108 al-Kawthar is a hub in the corpus (8/10 tightest pairs). [[h-new-350-al-tiwal-cohesion|H-NEW-350]] separately found that mufaṣṣal-ṭiwāl surahs (~50-93) have cohesion-pattern issues. **Is the entire classical *mufaṣṣal-qiṣār* genre (Q 93-114 per al-Suyūṭī) a coherent empirical cluster?**

Classical scholarship:
- **al-Suyūṭī** *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 19: tripartite mufaṣṣal division:
  - *mufaṣṣal al-ṭiwāl*: Q 50-~83 (long-mufaṣṣal)
  - *mufaṣṣal al-awsāṭ*: Q ~83-~93 (middle-mufaṣṣal)
  - *mufaṣṣal al-qiṣār*: Q ~93-114 (short-mufaṣṣal)
- **al-Zarkashī** *al-Burhān* chapter on corpus-division: similar tripartite.
- Typical markers: high rhyme-density, eschatological/admonition imagery, terminal-imagery, minimal lexicon, liturgical-recitation frequency.

**P8 (4-region hub architecture)** predicts region-4 ≈ mufaṣṣal-qiṣār should be **internally cohesive** — this is the testable prediction.

## 2. Protocol

1. **PRIMARY Set Q** = {Q 93 al-Ḍuḥā, 94 al-Sharḥ, 95 al-Tīn, 96 al-ʿAlaq, 97 al-Qadr, 98 al-Bayyinah, 99 al-Zalzalah, 100 al-ʿĀdiyāt, 101 al-Qāriʿah, 102 al-Takāthur, 103 al-ʿAṣr, 104 al-Humazah, 105 al-Fīl, 106 Quraysh, 107 al-Māʿūn, 108 al-Kawthar, 109 al-Kāfirūn, 110 al-Naṣr, 111 al-Masad, 112 al-Ikhlāṣ, 113 al-Falaq, 114 al-Nās} — N=22.

2. Compute d̄(Q) = mean pairwise FR over C(22,2) = 231 pairs.

3. Null: 10000 random 22-subsets of {1..114}; compute d̄ for each.

4. **PRIMARY H1**: d̄(Q) ≤ 5%ile of null.

5. **MW-5 INNER Set QI** = {Q 103-114} = last 12 surahs (all shortest). Predicted ≤1%ile of random-12 null — since Q 108 hub is in this set and D(Q106,Q108)=0.2127 is corpus minimum.

6. **MW-6 COMPARATOR Cm** = 22 Meccan-mid-length surahs: {Q 26 al-Shuʿarāʾ, 27 al-Naml, 28 al-Qaṣaṣ, 37 al-Ṣāffāt, 38 Ṣād, 39 al-Zumar, 40 Ghāfir, 41 Fuṣṣilat, 42 al-Shūrā, 43 al-Zukhruf, 44 al-Dukhān, 45 al-Jāthiyah, 46 al-Aḥqāf, 50 Qāf, 51 al-Dhāriyāt, 52 al-Ṭūr, 54 al-Qamar, 55 al-Raḥmān, 56 al-Wāqiʿah, 67 al-Mulk, 68 al-Qalam, 71 Nūḥ} — all Meccan mid-length (~30-200 verses), spans various registers (narrative, eschatological, ḥawāmīm, cosmic). Predicted null-typical [30-70%ile].

## 3. Pre-committed predictions

| Test | Predicted | Gate |
|:--|:-:|:--|
| PRIMARY d̄(Q) mufaṣṣal-qiṣār-22 | ≤ 5%ile | corpus-extreme |
| MW-5 d̄(QI) inner-12 | ≤ 1%ile | ULTRA-extreme |
| MW-6 d̄(Cm) Meccan-mid-22 | [30%, 70%]%ile | null-typical |

**Aggregate H1 CONFIRMED**: PRIMARY + MW-5 + MW-6 all pass = classical mufaṣṣal-qiṣār genre-division empirically validated as super-cluster; P8 region-4 prediction confirmed.

**H0 alternatives**:
- PRIMARY fails: mufaṣṣal-qiṣār is NOT a super-cluster at 22-set scale. Q 108 hub-status is local-pair-only.
- MW-5 fails: inner-12 is NOT ULTRA-extreme; Q 108's centrality is overstated.
- MW-6 fails: instrument mis-calibrated — Meccan-mid-length shows unexpected cohesion.

## 4. Classical-scholarship anchors

**al-Suyūṭī** *al-Itqān* nawʿ 19 "fī maʿrifat al-ṭiwāl wa-al-miʾūn wa-al-mathānī wa-al-mufaṣṣal":
- *mufaṣṣal* division-rationale: frequency of basmala-separation (*fāṣilas*) between verses, terminal rhyme-density, Meccan-chronology concentration.
- *al-qiṣār*: short in verse-count AND in individual-verse-length.

**al-Zarkashī** *al-Burhān* vol. 1 ch. 2: same division; notes that mufaṣṣal-qiṣār surahs are the daily-liturgical repertoire (Friday sermon, witr-prayer, travel-recitation).

**Hadith validations**:
- Bukhārī #1049 on mufaṣṣal-qiṣār being the Prophet's preferred witr-prayer material.
- Ibn Māja #1366 on teaching children starting with mufaṣṣal-qiṣār.

**Internal markers suggesting cohesion**:
- Shared oath-openings (*wa-al-fajr, wa-al-shams, wa-al-ʿāṣr, wa-al-ʿādiyāt, wa-al-mursalāt*) in ~7+ surahs.
- Shared *kallā* / *innā anzalnāhu* / *innā aʿṭaynāka* openings.
- Maximum-short-verse-density (often 3-7 words per verse).
- Heavy terminal-rhyme consistency.

**Empirical implication**: if these shared-marker patterns produce FR-cohesion, d̄(Q) should be extremely tight.

## 5. Honest limits

1. **N=22 is large** — percentile estimates noise ~0.5-1pp at extreme tails.
2. **Mufaṣṣal-qiṣār boundary is soft** — classical tradition differs on where mufaṣṣal-qiṣār begins (Q 93 standard, but Q 78 or Q 90 also cited). I use strict Q 93-114 per majority.
3. **Q 96 al-ʿAlaq (first revelation) is chronologically FIRST** — potentially outlier within mufaṣṣal-qiṣār if its content differs.
4. **Q 98 al-Bayyinah is Medinan** (8 verses); it's the only Medinan surah in this set. Possible chronology-outlier.
5. **Q 94 al-Sharḥ is short and Meccan** — but its content (addressing the Prophet's grief-relief) is distinctive.
6. **MW-6 set is large (22)** — may itself contain sub-clusters that create unintended cohesion.
7. **FR-roots only.**
8. **Post-hoc discovery of Q 108 as hub** might have biased my expectation — but the pre-reg PRIMARY is distinct from hub-claim (tests cluster-COHESION not hub-CENTRALITY).

## 6. Novel-finding potential

If PRIMARY + MW-5 + MW-6 all pass:
- **Classical mufaṣṣal-qiṣār genre empirically validated as corpus-largest cohesive cluster** — a 22-surah structural unit.
- **P8 region-4 (terminal mufaṣṣal) internal cohesion** confirmed pre-registered.
- Candidate **[[cross-finding-026-iʿjāz-architecture|cross-finding-026]]**: mufaṣṣal-qiṣār super-cluster as P8 region-4 empirical anchor.
- Q 108's hub-role (H-490) is CONTEXTUALIZED as centroid of a 22-surah cluster.

If PRIMARY fails but MW-5 passes:
- Inner-12 (Q 103-114) is the true cluster; Q 93-102 are "transition-zone" between mufaṣṣal-awsāṭ and mufaṣṣal-qiṣār.
- Classical Q 93 boundary is empirically over-inclusive.

If both fail:
- Mufaṣṣal-qiṣār is a THEMATIC/rhyme-based genre, not a full-content cohesive-cluster.
- Q 108 hub-status (H-490) is LOCAL-pair-only.

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_500_mufassal_qisar_super_cluster.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-500.json`
- Findings: `findings/phase-b-hypotheses/h-new-500-mufassal-qisar-super-cluster.md`

Pre-reg locked 2026-04-22.
