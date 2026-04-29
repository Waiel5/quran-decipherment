---
id: H-NEW-350
title: "al-Ṭiwāl block cohesion — higher-N (8 surahs) test of block-adjacency causal hypothesis"
phase: B
status: PRE-REGISTERED 2026-04-20
date: 2026-04-20
agent: team-lead (inline; ID 350 to skip codex range)
parent_1: H-NEW-340 (N=5 block+formula 8.1%ile directional; strict α_bon failed on power)
parent_2: H-NEW-331 (musabbiḥāt 19.8%ile directional)
seed: 20260502
bonferroni_k: 2
bonferroni_family: h-new-350-tiwal-cohesion
alpha_bon: 0.025
n_perm: 10000
rules_tuple: "(8 classical al-ṭiwāl surahs = {Q 2, 3, 4, 5, 6, 7, 8, 9}; FR root distance matrix from H-NEW-111; primary statistic = mean pairwise FR within 8-surah set; null = 10000 random 8-surah draws; seed 20260502; direction one-sided: classical set d̄ < null)"
direction: "Cell A al-ṭiwāl d̄ < null 2.5%ile AND p_less < α_bon=0.025; Cell B MW-5 late-mufaṣṣal 8-subset {Q 107-114} < null"
verdict: PENDING
---

# [[h-new-350-al-tiwal-cohesion|H-NEW-350]] — al-Ṭiwāl block cohesion test

## 1. Question

[[h-new-340-musabbihat-block-subset|H-NEW-340]] showed N=5 block subsets achieve only DIRECTIONAL cohesion (8-24%ile) — strict α_bon=0.0167 fails due to small-N null variance. At larger N, statistical power improves. **Test the classical sabʿ al-ṭiwāl** (Q 2-Q 9, the 8 longest-early mushaf surahs) — the foundational classical block of the Quran. If block-adjacency is genuinely causal for content cohesion, al-ṭiwāl at N=8 should achieve strict PASS.

## 2. Pre-committed expectations

ṭiwāl are all long (100+ verses each except Q 8 which is 75 verses), Medinan/Late-Meccan mixed, heavy in legal + narrative + theological content. They share:
- Length-register (all 60+ verses)
- Front-of-mushaf position (Q 2-9)
- Mixed Meccan/Medinan (Q 2-5 Medinan; Q 6-7 Meccan; Q 8-9 Medinan)
- al-Biqāʿī treats them as the foundational block

Pre-committed: d̄ < null 2.5%ile AND p < α_bon=0.025. At N=8 with 28 pairs per subset, null variance drops and strict α should be achievable if cohesion is real.

Modal expectation: **PASS at strict Bonferroni** — this is the crucial test of my block-causation hypothesis at proper statistical power.

## 3. Protocol

1. Load [[h-new-111-fisher-rao-mushaf|H-NEW-111]] FR distance matrix (114×114).
2. Al-Ṭiwāl S_T = {Q 2, 3, 4, 5, 6, 7, 8, 9}; compute mean pairwise FR d̄_T.
3. Null: 10000 random 8-surah draws; compute d̄_null.
4. Cell A: p_less(d̄_T); strict pass at α_bon=0.025.
5. Cell B MW-5: Q 107-114 (8 mushaf-last surahs, mufaṣṣal-qiṣār) — another block grouping for control.

## 4. Bonferroni + MW-5

k=2, α_bon=0.025.

## 5. Honest limits

1. **ṭiwāl list varies classically** — some scholars include Q 10 Yūnus instead of Q 8. I use the standard Q 2-9 8-surah list.
2. **Mixed Meccan/Medinan** dilutes chronological cohesion but shouldn't affect content cohesion if block-adjacency is the real driver.
3. **FR-roots only** — metric sensitivity deferred.
4. **Q 1 excluded** — Q 1 is classified sui-generis-liturgical ([[h-new-155-q1-sui-generis|H-NEW-155]]), not part of ṭiwāl in any classical list.

## 6. Classical anchor

- **al-Suyūṭī *Itqān***: discusses sabʿ al-ṭiwāl (the seven long)
- **al-Biqāʿī *Naẓm al-Durar***: treats first-block munāsabāt as foundational
- **al-Zarkashī *al-Burhān***: ṭiwāl as structural mushaf-block

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_350_al_tiwal_cohesion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-350.json`
- Findings: `findings/phase-b-hypotheses/h-new-350-al-tiwal-cohesion.md`

Pre-reg locked 2026-04-20.
