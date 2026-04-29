---
id: H-NEW-340
title: "al-Musabbiḥāt block-only subset cohesion test — disentangles block-adjacency from tasbīḥ-formula as causal factor"
phase: B
status: PRE-REGISTERED 2026-04-20
date: 2026-04-20
agent: team-lead (inline; ID 340 to skip codex range)
parent: H-NEW-331 (full 7-surah musabbiḥāt at 19.8%ile, directional cohesive but underpowered)
seed: 20260501
bonferroni_k: 3
bonferroni_family: h-new-340-musabbihat-block-subset
alpha_bon: 0.0167
n_perm: 10000
rules_tuple: "(3 subsets: A=musabbiḥāt Medinan-back-block {Q 57, 59, 61, 62, 64}; B=musabbiḥāt non-block pair {Q 17, 87}; C=MW-5 ḥawāmīm 5-subset {Q 40, 41, 43, 44, 45} as pure-block-no-tasbīḥ control; FR root distance matrix from H-NEW-111; 10000-perm random-sample null; one-sided p_less < α_bon)"
direction: "Cell A (block+formula) d̄ < null 1.67%ile AND PASS; Cell B (formula-no-block) small-N descriptive only; Cell C (block-no-formula) comparison case"
verdict: PENDING
---

# [[h-new-340-musabbihat-block-subset|H-NEW-340]] — musabbiḥāt block-only subset — disentangling block vs formula

## 1. Question

[[h-new-331-al-musabbihat-cohesion|H-NEW-331]] found full 7-surah musabbiḥāt at 19.8%ile (directional cohesion). 5 of 7 are in Q 57-64 Medinan-back block. Is **block-adjacency** the causal factor for content cohesion, or does the **tasbīḥ-formula** itself also contribute?

Pre-committed strategy: restrict to the pure-block subset {Q 57, 59, 61, 62, 64} (block + formula) and compare against pure-block-no-formula control {Q 40, 41, 43, 44, 45} (ḥawāmīm).

## 2. Hypothesis

**H1 (block is causal factor)**: d̄(musabbiḥāt block-subset) ≈ d̄(ḥawāmīm) — both cohesive, both at similar percentiles.

**H0 (formula contributes)**: d̄(musabbiḥāt block-subset) < d̄(ḥawāmīm) significantly.

Pre-committed direction: Cell A block+formula PASS at α_bon=0.0167 (stricter k=3 Bonferroni).

## 3. Protocol

- Cell A: mean pairwise FR within musabbiḥāt Medinan-back block {57, 59, 61, 62, 64}
- Cell B: d(Q 17, Q 87) — single pair, mushaf-far, both musabbiḥāt. Descriptive only.
- Cell C: ḥawāmīm pure-block-no-formula {40, 41, 43, 44, 45}
- All vs 10,000-perm random-sample null of matching N=5

## 4. Bonferroni

k=3, α_bon = 0.0167.

## 5. Pre-committed expectations

- Cell A: STRONG cohesion expected (block+formula stacked); predict percentile ≤ 5%ile
- Cell B: single-pair no-statistical-inference
- Cell C: comparable to Cell A if block is causal; inferior to Cell A if formula contributes

## 6. Decision rules

| Cell A | Cell C | Verdict |
|---|---|---|
| PASS < 1.67%ile | PASS or similar-pct | **BLOCK-DRIVES-COHESION** (formula-only additional effect uncertain) |
| PASS | FAIL | **BLOCK-AND-FORMULA-BOTH-CONTRIBUTE** |
| FAIL | FAIL | **UNDERPOWERED-AT-N5** (N=5 null variance too high) |

## 7. Classical anchors

- al-Biqāʿī *Naẓm al-Durar* — adjacency-munāsabāt as causal organizing principle
- al-Suyūṭī *Itqān* — fawātiḥ as morphological classification layer
- al-Rāzī *Mafātīḥ al-ghayb* vol 27 — ḥawāmīm theological cohesion

## 8. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_340_musabbihat_block_subset.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-340.json`
- Findings: `findings/phase-b-hypotheses/h-new-340-musabbihat-block-subset.md`

Pre-reg locked 2026-04-20.
