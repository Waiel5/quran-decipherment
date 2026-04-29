---
id: H-NEW-170
title: Full 99-name divine-attribute co-occurrence network analysis
phase: B
status: PRE-REGISTERED (locked before running)
date: 2026-04-17
agent: opus-4.7-autonomous
parents:
  - H-NEW-140 (PASS-DIRECTED; classical paired-names cluster confirmed)
  - H-NEW-95 (Q 59:22-24 rank-1 for 99-name verse density)
seed: 20260419
bonferroni_k: 2
bonferroni_family: h-new-170-99name-network
alpha_bon: 0.025
---

# [[h-new-170-99name-network|H-NEW-170]] — Full 99-name co-occurrence network

## Motivation

[[h-new-140-divine-name-pair-cohesion|H-NEW-140]] confirmed that hand-picked classical pairs form an over-dense
cluster in verse-level co-occurrence (13.87× aggregate enrichment, de-circularized in [[h-new-140-1-all-pair-decircularization|H-NEW-140.1]]). [[h-new-95-khawatim-extension|H-NEW-95]] confirmed that Q 59:22-24 is the rank-1 hot-spot for 99-name verse-density. Both are local findings.

The structural question: **does the full 99-name corpus co-occurrence
matrix form a globally non-trivial network, or is the classical cluster
a small island in an otherwise-independent sea?**

## Data

- Corpus: `quran-text/quran-no-tashkeel.json` (6,236 verses)
- Name list: `data/asma-al-husna.txt` (standard al-Tirmidhī 99-name list)
- Comment lines stripped; 99 names loaded

## Matching rule (locked)

Per [[h-new-140-1-all-pair-decircularization|H-NEW-140.1]] convention, for each name, match any of the following
whole-word forms in verse text (Arabic letter boundaries U+0621-U+064A):
- `الX` (with definite article) — primary form as listed
- `X` (stem without `ال`) — derived by stripping `ال` prefix if present
- For multi-word names (e.g. `مالك الملك`, `ذو الجلال والإكرام`), we require ALL constituent words to co-occur in the same verse (anywhere, no ordering constraint). This is stricter than a raw substring search.

No stemming beyond this. No case-ending tolerance (no-tashkeel text makes this a no-op anyway).

## Build the network

1. Occurrence matrix `M[99, 6236]`, `M[i, v] = 1` iff name i appears in verse v.
2. Marginal `n_i = sum(M[i, :])`; `p_i = n_i / N`.
3. Co-occurrence `C[i, j] = sum_v M[i,v] * M[j,v]` (i != j).
4. Expected under independence `E[i, j] = n_i * n_j / N`.
5. Binomial z-score proxy (phi-like):
   `z[i, j] = (C[i,j] - E[i,j]) / sqrt(E[i,j] * (1 - p_i) * (1 - p_j))`
   Names with E[i,j] = 0 or n_i = 0 are assigned z = 0.
6. Edge kept if z > 2 (standard ~binomial significance threshold, matching the pre-reg threshold "phi > 2").

## Measures

- Number of edges above threshold
- Degree distribution (mean, max, top-5 by degree = "hub names")
- Global clustering coefficient `C_global` (transitivity = 3·triangles / connected-triples) computed on the unweighted graph defined by z>2 edges.

## Null model (permutation)

Shuffle name occurrences across verses, preserving each name's marginal
count `n_i` and each verse's total name-count `sum_i M[i, v]` (double-stochastic marginal preservation is overly strict; we instead preserve row-marginals only, which is a WEAKER null). Concretely, for each name i
independently, randomly choose n_i verses (uniform without replacement)
to place that name. This preserves n_i but breaks inter-name correlation.

Run K = 1000 permutations with seed 20260419, compute clustering coefficient
C_null for each, report mean/std and empirical p-value for observed C_global.

## Decision rules (pre-committed)

- **Primary test 1** (structure): `p(C_global <= C_null) < 0.025` (Bonferroni-corrected alpha for k=2 tests). If passed, the network is MORE structured (more clustered) than the marginal-preserving null.
- **Primary test 2** (Ghazālī alignment): partition the 99 names into al-Ghazālī's three families (Knowing / Willing / Able) per the Maqṣad al-Asnā typology. Compute modularity Q of this partition on the weighted graph (edge weights = max(z, 0)). Compare to modularity of 1000 random 3-partitions of the 99 names. If `p(Q_observed <= Q_random) < 0.025`, Ghazālī's grouping matches empirical clustering.

Both tests use alpha_bon = 0.025 (Bonferroni for k=2).

## Ghazālī family assignment (locked before running)

al-Ghazālī in Maqṣad al-Asnā groups names broadly into:
- **ʿIlm (Knowing)**: names of knowledge, awareness, wisdom
- **Irāda (Willing)**: names of will, love, grace, mercy, creation-as-choice
- **Qudra (Able)**: names of power, dominion, force, action

My assignment (locked; best-faith reading; will be re-examined only for coding errors, not to improve fit):

**ʿIlm (Knowing)** — 16 names:
العليم، الحكيم، السميع، البصير، اللطيف، الخبير، الحسيب، المحصي،
الشهيد، الحفيظ، الرقيب، الحكم، المقيت، الحق، العدل، الواجد

**Irāda (Willing)** — 38 names — names of will/choice/mercy/benefaction:
الرحمن، الرحيم، الملك، القدوس، السلام، المؤمن، المهيمن، الغفار،
الوهاب، الرزاق، الفتاح، الغفور، الشكور، الكريم، المجيب، الواسع،
الودود، الباعث، الولي، الحميد، المحيي، التواب، العفو، الرؤوف،
المقسط، الجامع، النور، الهادي، البديع، الرشيد، الصبور، البر،
مالك الملك، ذو الجلال والإكرام، الوكيل، المجيد، الحليم، الباقي

**Qudra (Able)** — 45 names — names of power/dominion/act:
الله، العزيز، الجبار، المتكبر، الخالق، البارئ، المصور، القهار،
القابض، الباسط، الخافض، الرافع، المعز، المذل، العظيم، العلي،
الكبير، الجليل، القوي، المتين، المبدئ، المعيد، المميت، الحي،
القيوم، الماجد، الواحد، الصمد، القادر، المقتدر، المقدم، المؤخر،
الأول، الآخر، الظاهر، الباطن، الوالي، المتعالي، المنتقم، الغني،
المغني، المانع، الضار، النافع، الوارث

Count check: 16 + 38 + 45 = 99 ✓

## Garden-of-forking-paths

1. Name list locked: al-Tirmidhī 99 as listed in `data/asma-al-husna.txt`.
2. Matching rule locked: whole-word al-form OR stem, multi-word names require all constituents in same verse.
3. z-threshold locked at 2.
4. Null model locked: marginal-preserving name-shuffle, 1000 perms, seed 20260419.
5. Ghazālī partition locked above. If a coding error is found post-hoc, we note it but do NOT re-run to improve fit.
6. Bonferroni k=2 (structure test + Ghazālī modularity test).

## Predicted outcome (bookmaking)

Prior:
- Structure test: very likely PASS. Classical paired-names cluster + musabbiḥāt inertia strongly suggest non-random co-occurrence.
- Ghazālī modularity: uncertain. His partition is medieval-theological; it may or may not track empirical co-occurrence. I expect modest effect (~60-80% probability of pass).
- Top hub names: likely الله + high-frequency classical-pair names (الرحمن، الرحيم، العزيز، الحكيم، العليم).

## Files

- Pre-reg: this file
- Script: `scripts/h_new_170_99name_network.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-170-99name-network.json`
- Findings: `findings/phase-b-hypotheses/h-new-170-99name-network.md`
