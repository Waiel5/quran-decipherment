---
id: H-NEW-331
title: "al-Musabbiḥāt content-axis cohesion test — do the 7 surahs opening with tasbīḥ cluster content-wise?"
phase: B
status: PRE-REGISTERED 2026-04-19
date: 2026-04-19
agent: team-lead (inline; ID 331)
parent_1: H-NEW-330 (al-ḥāmidāt NULL)
parent_2: H-NEW-321 (Q 1-Q 27 Basmala NULL)
parent_3: H-NEW-310 (muq singleton letter-cluster NULL)
seed: 20260430
bonferroni_k: 2
bonferroni_family: h-new-331-al-musabbihat-cohesion
alpha_bon: 0.025
n_perm: 10000
rules_tuple: "(7 classical al-musabbiḥāt surahs = {Q 17, 57, 59, 61, 62, 64, 87}; Fisher-Rao root distance matrix from H-NEW-111; primary statistic = mean pairwise FR within 7-surah set; null = 10000 random 7-surah draws; direction one-sided: classical set < null; MW-5 control = ḥawāmīm 6-subset {40,41,43,44,45,46}; seed 20260430)"
direction: "Cell A: classical al-musabbiḥāt d̄ < null 2.5%ile; Cell B: MW-5 ḥawāmīm 6-subset d̄ < null 2.5%ile"
verdict: PENDING
---

# [[h-new-331-al-musabbihat-cohesion|H-NEW-331]] — al-Musabbiḥāt content-axis cohesion test

## 1. Question

Seven surahs open with tasbīḥ (praise-of-God):
- Q 17 al-Isrāʾ: *subḥāna alladhī asrā* (past tense of root سبح with prefix)
- Q 57 al-Ḥadīd: *sabbaḥa li-Llāhi* (perfect III)
- Q 59 al-Ḥashr: *sabbaḥa li-Llāhi*
- Q 61 al-Ṣaff: *sabbaḥa li-Llāhi*
- Q 62 al-Jumuʿa: *yusabbiḥu li-Llāhi* (imperfect III)
- Q 64 al-Taghābun: *yusabbiḥu li-Llāhi*
- Q 87 al-Aʿlā: *sabbiḥ isma rabbika* (imperative II)

Classical scholarship groups these as *al-musabbiḥāt*. Do they show content-axis cohesion under Fisher-Rao root distance?

Builds on [[h-new-330-al-hamidat-cohesion|H-NEW-330]]'s NULL for al-ḥāmidāt with **higher N=7** (vs [[h-new-330-al-hamidat-cohesion|H-NEW-330]]'s N=5), providing better statistical power.

## 2. Hypothesis

**H1 (musabbiḥāt content-cohesive)**: d̄(7-set) < null 2.5%ile (p < α_bon = 0.025).

**H0 (phrase-opening ≠ content-cluster)**: consistent with [[h-new-310-singleton-fr-rank1|H-NEW-310]]/321/330 pattern.

Pre-committed direction: classical set d̄ < null mean, p < α_bon.

## 3. Protocol

1. Load Fisher-Rao distance matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (reused).
2. Classical set S = {Q 17, 57, 59, 61, 62, 64, 87}; compute mean pairwise FR distance d̄_obs.
3. Null: 10,000 random 7-surah draws from {1..114}; compute d̄_null for each.
4. p = fraction of nulls with d̄_null ≤ d̄_obs.
5. MW-5: ḥawāmīm 6-subset {40, 41, 43, 44, 45, 46} — known content-cohesive per al-Rāzī classical tradition.

## 4. Bonferroni + MW-5

k = 2 cells, α_bon = 0.025.

## 5. Pre-committed expectations

Modal expectation: NULL, consistent with [[h-new-310-singleton-fr-rank1|H-NEW-310]]/321/330 pattern.

IF PASS: would be SURPRISING positive finding — classical al-musabbiḥāt grouping has empirical content cohesion. Would refine the "phrase-sharing ≠ content-sharing" pattern from [[h-new-321-q1-q27-basmala-echo|H-NEW-321]]/330.

Specifically interesting: al-musabbiḥāt form a classical *series* (sequential sequence in mushaf: Q 57-59-61-62-64-87 is nearly contiguous within Medinan-back block). Mushaf-adjacency bias could push them toward cohesion even if phrase-sharing alone doesn't.

If ḥawāmīm MW-5 passes strict Bonferroni this time (N=6 vs N=5 in [[h-new-330-al-hamidat-cohesion|H-NEW-330]]), it validates my prior framing that [[h-new-330-al-hamidat-cohesion|H-NEW-330]]'s MW-5 failure was N-power related, not pipeline.

## 6. Honest limits

1. **N=7 still small** — null variance could be high.
2. **Classical list slightly variable** — some include Q 59 only, some add Q 65. I use standard 7-surah list per al-Suyūṭī *Itqān*.
3. **Mushaf-adjacency confound**: 5 of 7 musabbiḥāt are in Medinan-back block (Q 57, 59, 61, 62, 64 all within Q 57-64). This could create spurious cohesion via block-adjacency rather than phrase-opening.
4. **FR-roots only** — metric choice.

## 7. Classical anchor

- al-Suyūṭī *Itqān* — classifies 7 musabbiḥāt as opening-formula group
- al-Zarkashī *al-Burhān* — lists the tasbīḥ-opening surahs
- al-Qurṭubī *al-Jāmiʿ li-Aḥkām al-Qurʾān* — discusses musabbiḥāt sequence as thematically linked

## 8. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_331_al_musabbihat_cohesion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-331.json`
- Findings: `findings/phase-b-hypotheses/h-new-331-al-musabbihat-cohesion.md`

Pre-reg locked 2026-04-19.
