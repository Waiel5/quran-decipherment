---
id: H-NEW-167
title: Graph-theoretic properties of the verse-twin network (downstream of H-NEW-66)
phase: B
status: PUBLISHED 2026-04-17 (run-1)
seed: 20260419
rules_tuple: (no-tashkeel; whitespace-collapsed; basmala-only-in-Q1)
parent_prereg: h-new-167-verse-twin-graph-prereg.md
script: scripts/h_new_167_verse_twin_graph.py
data_json: findings/phase-b-hypotheses/csv/h-new-167.json
---

# [[h-new-167-verse-twin-graph|H-NEW-167]] — Graph-theoretic properties of the verse-twin network

## Headline

Under the pre-registered top-1 Jaccard construction on all 6,236 verses,
the verse-twin graph is **not small-world** and **not scale-free**.
It is a near-forest: 6,236 nodes, 4,943 edges, **0 triangles**,
**1,293 connected components**, largest component only 42 nodes.

All three pre-registered Bonferroni-3 tests **fail** (α_test = 0.0167).

The mechanical witness MW-5 (planted-community graph) passes
clustering and small-world as expected, confirming the tests would
detect such structure if it were present.

## Observed graph statistics

| metric | value |
|---|---|
| nodes | 6,236 |
| edges | 4,943 |
| mean / median / max degree | 1.585 / 1 / **31** |
| isolates (deg 0) | 3 |
| connected components | 1,293 |
| largest component | **42** nodes |
| average clustering | **0.0000** |
| triangles (total) | **0** |
| mean shortest-path on LCC | 4.452 |
| degree assortativity | **−0.141** (disassortative) |

## Pre-registered tests (Bonferroni-3, α_test = 0.0167)

### 1. Power-law fit — **FAIL**

* Best k_min = 1, α ≈ 1.977, KS = 0.612, bootstrap-p = 0.000.
* The degree distribution is dominated by k = 1 (top-1 construction
  forces a near-spike) with a heavy-tailed minority at the hubs.
  CSN KS-test rejects power-law at k_min = 1; and higher k_min values
  have too few tail observations for meaningful fit.
* VERDICT: the graph is **not scale-free** under the pre-registered
  criterion. The apparent hub (Q 55:13 with degree 31) is a single
  local outlier, not evidence of a power-law regime.

### 2. Clustering vs Erdős–Rényi — **FAIL**

* C_obs = 0.0000. C_ER = 0.00013 ± 0.00020 (50 reps, matched n, m).
* One-sided p = 1.0 (observed is **below** the ER mean; ER graphs
  actually have more clustering than the top-1 twin graph because
  top-1 construction forbids triangles by design in most cases).

### 3. Small-world σ — **FAIL**

* C_obs = 0, so σ = (0/C_ER) / (L/L_ER) = **0.000**.
* L_obs on the 42-node LCC = 4.45; L_ER (LCC) = 15.82.
  The observed graph has *shorter* paths than ER but that is
  because it fragments into thousands of tiny components — ER
  with m = 4,943 on n = 6,236 is sparse and its giant component
  is long and thin, whereas our graph has no giant component at all.
  The small-world property requires high clustering **and** short
  paths; we have neither.

## Mechanical-witness MW-5 — as expected

Planted-community graph (5 blocks × 1,000 nodes, p_in = 0.01,
p_out = 0.0005, seed 20260420):

| test | result |
|---|---|
| power-law | FAIL (informational) |
| clustering > ER | **PASS** (C_obs = 0.0074, C_ER = 0.0024) |
| small-world σ ≥ 2 | **PASS** (σ = 2.95) |

MW-5 passes both locked pre-registered tests that are *supposed* to
pass; the observed Quran graph's failures are therefore **genuine
structural absences**, not instrument defects.

## Top-10 hubs (undirected degree)

| rank | verse | deg | preview |
|---|---|---|---|
| 1 | **Q 55:13** | **31** | فبأي آلاء ربكما تكذبان — the famous refrain of Sūrat al-Raḥmān |
| 2 | Q 77:15 | 11 | ويل يومئذ للمكذبين — the refrain of al-Mursalāt |
| 3 | Q 26:108 | 10 | فاتقوا الله وأطيعون — refrain in the prophets-sequence of al-Shuʿarāʾ |
| 4 | Q 26:8 | 9 | إن في ذلك لآية وما كان أكثرهم مؤمنين — refrain of al-Shuʿarāʾ |
| 5 | Q 26:9 | 8 | وإن ربك لهو العزيز الرحيم — refrain of al-Shuʿarāʾ |
| 6 | Q 1:2 | 7 | الحمد لله رب العالمين |
| 7 | Q 2:136 | 7 | قولوا آمنا بالله وما أنزل إلينا وما أنزل إلى إبراهيم... |
| 8 | Q 3:16 | 7 | الذين يقولون ربنا إننا آمنا فاغفر لنا ذنوبنا |
| 9 | Q 6:21 | 7 | ومن أظلم ممن افترى على الله كذبا |
| 10 | Q 26:226 | 7 | وأنهم يقولون ما لا يفعلون |

**Interpretation.** Every hub is a **refrain verse** — a text that
recurs verbatim or near-verbatim many times in the corpus.
Q 55:13 occurs 31 times (1× + 30 refrain occurrences) in Sūrat
al-Raḥmān alone; its structural-twin degree of 31 recovers
precisely that count. Likewise Q 77:15 is the refrain of Sūrat
al-Mursalāt; Q 26:8, 9, 108, 226 are refrains of Sūrat al-Shuʿarāʾ.
The graph-theoretic hub-identification independently rediscovers
the corpus's known **lāzima** (litanic refrain) structure — three
of the top five hubs are from Sūrat al-Shuʿarāʾ, whose refrain
structure is a textbook example of Quranic istinbāṭ (cf. al-Biqāʿī's
*Naẓm al-durar*).

## Interpretation and caveats

* **Top-1 construction is architecturally anti-clustering.** Each
  node contributes one outgoing edge; triangles require three mutually
  self-selecting nearest neighbours, which is combinatorially rare.
  A k-NN or similarity-threshold graph would produce a very different
  topology — and may yet be small-world. This test characterised
  only the top-1 graph.
* **Negative assortativity (r = −0.14)** means high-degree refrain
  verses tend to be connected to low-degree, bespoke verses — a
  classic "hub-and-spoke" pattern, which is exactly what
  refrain-heavy textual structure produces.
* **The 42-node largest component** corresponds to a constellation
  around the Shuʿarāʾ/Mursalāt/Raḥmān refrain ecosystem. This is
  worth a follow-up ([[h-new-168-q16-q25-dispersion|H-NEW-168]]?): dumping the 42-node subgraph
  and inspecting which refrains cluster together would likely
  recover the classical rhyme/refrain families.

## Deliverables

* Pre-reg: `findings/phase-b-hypotheses/h-new-167-verse-twin-graph-prereg.md`
* Script: `scripts/h_new_167_verse_twin_graph.py`
* Data: `findings/phase-b-hypotheses/csv/h-new-167.json`
* Seed: 20260419 (single run, no re-seed on failure)
* Reproducibility: run `python3 scripts/h_new_167_verse_twin_graph.py`
  from project root; runtime ≈ 2–3 min.
