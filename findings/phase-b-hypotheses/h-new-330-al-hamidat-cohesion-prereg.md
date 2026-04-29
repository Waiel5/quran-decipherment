---
id: H-NEW-330
title: "al-Ḥāmidāt content-axis cohesion test — do the 5 surahs opening with al-ḥamdu li-Llāh cluster content-wise?"
phase: B
status: PRE-REGISTERED 2026-04-19
date: 2026-04-19
agent: team-lead (inline; ID 330 chosen to skip codex sequential range)
parent_1: H-NEW-321 (Q 1 ↔ Q 27 Basmala echo NULL)
parent_2: H-NEW-111 (Fisher-Rao root distance matrix)
related: H-NEW-310 (muq singleton letter-cluster-vs-content orthogonality)
seed: 20260429
bonferroni_k: 2
bonferroni_family: h-new-330-al-hamidat-cohesion
alpha_bon: 0.025
n_perm: 10000
rules_tuple: "(5 classical al-ḥāmidāt surahs = {Q 1, 6, 18, 34, 35}; Fisher-Rao root distance matrix from H-NEW-111; primary statistic = mean pairwise FR distance within the 5-surah set; null = 10000 random draws of 5 surahs from the 114; direction one-sided: classical set mean < random-set mean; seed 20260429)"
direction: "Cell A: observed mean pairwise FR distance in al-ḥāmidāt < null mean (classical set is content-cohesive); Cell B: observed < 2.5th percentile of null distribution"
verdict: PENDING
---

# [[h-new-330-al-hamidat-cohesion|H-NEW-330]] — al-Ḥāmidāt content-axis cohesion test

## 1. Question

Five surahs open with the formulaic phrase **al-ḥamdu li-Llāh**:
- Q 1:2 *al-ḥamdu li-Llāhi rabbi al-ʿālamīn*
- Q 6:1 *al-ḥamdu li-Llāhi alladhī khalaqa al-samāwāti wa-l-arḍ*
- Q 18:1 *al-ḥamdu li-Llāhi alladhī anzala ʿalā ʿabdihi al-kitāb*
- Q 34:1 *al-ḥamdu li-Llāhi alladhī lahu mā fī al-samāwāti wa-mā fī al-arḍ*
- Q 35:1 *al-ḥamdu li-Llāhi fāṭir al-samāwāti wa-l-arḍ*

Classical scholarship groups them as *al-muḥammadāt* or *al-ḥāmidāt* (praise-opened). This is a well-known classical grouping. Do these 5 surahs show CONTENT-AXIS COHESION under Fisher-Rao root distance — i.e., are they closer to each other than random 5-surah samples?

## 2. Hypothesis

**H1 (classical grouping is content-cohesive)**: observed mean pairwise FR distance within {Q 1, 6, 18, 34, 35} < 2.5th percentile of null distribution over 10,000 random 5-surah draws.

**H0 (classical grouping is phrase-specific not content-clustering)**: consistent with [[h-new-321-q1-q27-basmala-echo|H-NEW-321]]. The shared *al-ḥamd* formula is phrase-level; surah contents differ (Q 1 is prayer; Q 6 is theology/prophets; Q 18 has Kahf narratives; Q 34 is Sabaʾ; Q 35 is Fāṭir).

Pre-committed direction: mean pairwise FR in classical set < random null mean, p < α_bon = 0.025.

## 3. Protocol

1. Load Fisher-Rao distance matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (114×114, reused).
2. Classical set S = {Q 1, Q 6, Q 18, Q 34, Q 35}; compute mean pairwise FR distance d̄_obs.
3. Null: draw 10,000 random 5-surah samples from {1..114}; compute d̄_null for each.
4. p = fraction of null draws with d̄_null ≤ d̄_obs.
5. MW-5 positive control: known content-cohesive group — muʿawwidhatān (Q 113+Q 114; augment with al-Ikhlāṣ Q 112 to make a 3-set, then pad with 2 random short-mufaṣṣal for 5-total). Actually for clean MW-5, let me use the **ḥawāmīm 7-surah block {Q 40-46}** — drop 2 to make 5 = {Q 40, Q 41, Q 43, Q 44, Q 45}. This block is classically content-cohesive (al-Rāzī discusses ḥawāmīm theological density). Expected d̄ < null.

## 4. Bonferroni + MW-5

k = 2 cells: Cell A (al-ḥāmidāt cohesion); Cell B (MW-5 ḥawāmīm control).

MW-5 PASS expected: ḥawāmīm 5-subset d̄ should be in bottom 5% of random-5-subset null.

## 5. Pre-committed expectations

Given [[h-new-321-q1-q27-basmala-echo|H-NEW-321]]'s NULL (phrase-sharing ≠ content-sharing for Q 1/Q 27), I expect [[h-new-330-al-hamidat-cohesion|H-NEW-330]] to also return NULL. The 5 al-ḥāmidāt surahs have diverse content profiles:
- Q 1: 7-verse prayer (compact, high-density theological vocabulary)
- Q 6: 165-verse theology + prophets
- Q 18: 110-verse narratives (Kahf, Khidr, Dhū al-Qarnayn)
- Q 34: 54-verse Sabaʾ history
- Q 35: 45-verse creation + reward-punishment

Modal expectation is that mean pairwise distance will be near or slightly below null mean (some weak affinity via shared *ḥamd* + *Rabb* vocabulary, but overridden by length and topic differences).

PASS would be a STRIKING positive finding that classical *al-ḥāmidāt* grouping has empirical content cohesion.

## 6. Honest limits

1. **Single set of 5 surahs** — no multiple-set robustness.
2. **Classical list is slightly variable** — some scholars include Q 23, Q 29. I use the CLEAR-OPENING-FORMULA subset (Q 1, 6, 18, 34, 35).
3. **Fisher-Rao on QAC-STEM roots** — one content metric.
4. **MW-5 on ḥawāmīm expected PASS** — if it fails, instrument is broken.

## 7. Classical-scholarship anchors

- **al-Suyūṭī *Itqān*** discusses surah-opening categories including the *al-ḥāmidāt*.
- **al-Zarkashī *al-Burhān fī ʿUlūm al-Qurʾān*** on fawātiḥ al-suwar (surah-openings), including the 5 *al-ḥamd*-opening types.
- **al-Suyūṭī *al-Iḍāʾa fī ʿUmūm al-Riwāya*** on opening formula classifications.

## 8. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_330_al_hamidat_cohesion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-330.json`
- Findings: `findings/phase-b-hypotheses/h-new-330-al-hamidat-cohesion.md`

Pre-reg locked 2026-04-19. Execution follows.
