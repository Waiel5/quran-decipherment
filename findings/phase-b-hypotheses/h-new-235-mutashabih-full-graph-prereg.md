---
id: H-NEW-235
title: "Mutashābih full verse-graph: modularity + mushaf-alignment"
parent: H-NEW-210
date: 2026-04-17
seed: 20260419
bonferroni_k: 2
alpha_bon: 0.025
rules_tuple: [no-tashkeel, hafs-kufan, char-based-levenshtein, seed=20260419]
corpus: quran-text/quran-no-tashkeel.json
---

# [[h-new-235-mutashabih-full-graph|H-NEW-235]] — Pre-Registration

## Motivation

[[h-new-210-mirror-verses|H-NEW-210]] delivered top-50 Levenshtein mirror-verses but was saturated at Lev-distance 0 (~398 cross-surah pairs with ratio < 0.30, all of the top-50 byte-identical). The pre-reg there was deliberately narrow. [[h-new-235-mutashabih-full-graph|H-NEW-235]] scales to the **full verse-graph**:

- **Nodes** = 6,236 verses.
- **Edges** = verse-pairs with normalized-Levenshtein similarity > 0.7 (= ratio < 0.3; identical [[h-new-210-mirror-verses|H-NEW-210]] threshold).
- Full cross-product (~19M pairs) is intractable at exact Levenshtein; use **character-4-gram inverted-index blocking** to retrieve ~100K candidate pairs, then compute exact Levenshtein (rapidfuzz) on the candidate set only.

al-Kirmānī's *al-Burhān fī Mutashābih al-Qurʾān* (~800 pages of systematic near-repeat cataloging), al-Ghiznawī, al-Iskāfī *Durrat al-Tanzīl* are the classical anchors.

## Hypotheses

- **H1** (pair-graph modularity): the edges cluster into non-trivial communities, Q_observed > 0.3, and Q_observed > Q_null (edge-rewired degree-preserving null, 100 iterations).
- **H2** (mushaf-structure alignment): edges are non-randomly distributed with respect to the mushaf's structural partition. Specifically, edges cluster within-surah and within-juzʾ significantly above random.

## Primary tests (Bonferroni k=2, α_bon = 0.025)

- **T1**: `modularity_observed > 0.3` AND `(modularity_observed − mean_null_modularity) / std_null_modularity > z*(α=0.025, one-sided) = 1.96`.
- **T2**: edge-community alignment with mushaf structure. Three sub-measures (within-surah edge-fraction, within-juzʾ edge-fraction, within-mufaṣṣal edge-fraction) each compared against edge-rewired null; MW-7 says family-level Bonferroni applies, so T2 passes if ANY sub-measure has z > 1.96 AND the combined z (via Stouffer) > 1.96.

## Direction / decision rule

- **PASS** if BOTH T1 passes AND T2 passes.
- **PASS-DIRECTED** if T1 passes and T2 partial (e.g. within-surah only).
- **NULL-CONSISTENT** if neither passes.

## Secondary descriptive questions (not Bonferroni-budgeted)

- S1: community count and size distribution (Louvain resolution=1.0, default).
- S2: topical content of the 5 largest communities.
- S3: do any edges form "long-arc cross-surah links" matching [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s ring topology (i.e. Q 1–10 ↔ Q 100–114 type edges)? This is descriptive.
- S4: top-5 highest-similarity verse-pairs BEYOND [[h-new-210-mirror-verses|H-NEW-210]] top-50 (i.e. ranks 51+).

## Null-model design

- **For T1**: degree-preserving edge rewiring (Maslov–Sneppen); 100 iterations; compute Louvain modularity each.
- **For T2**: edge-rewired null holds degree-sequence constant and reshuffles edges, so within-partition edge-fraction has a null distribution.
- **Cheat control (MW-5)**: shuffle verse-to-surah labels (1 iteration, seed-shift); re-compute within-surah fraction. Should collapse toward chance.

## Garden of forking paths — locked BEFORE run

- Blocking: character-4-grams; candidate threshold = pairs sharing ≥ 2 distinct 4-grams.
- Similarity threshold: 0.7 (= ratio < 0.3, identical to [[h-new-210-mirror-verses|H-NEW-210]]).
- Min verse length: 10 characters (matches [[h-new-210-mirror-verses|H-NEW-210]]).
- Community detection: Louvain (python-louvain), resolution=1.0, random_state=20260419.
- Null: 100 edge-rewirings via NetworkX `double_edge_swap` (nswap = 10 × |E|).
- Mushaf partition: surah ID, juzʾ (1..30 mapped from surah/verse), and "mufaṣṣal" (Q 49+ per al-Suyūṭī short-mufaṣṣal span conservative).
- Time cap: 30 minutes total wall-time; if exceeded, document restriction and re-use whatever candidate set has completed.

## Honest limits

- Levenshtein is a surface-character metric; semantic mutashābih (different words, same meaning) is NOT captured.
- Candidate-block approach may miss pairs with < 2 shared 4-grams (very short verses or heavy re-ordering); these are documented as a known blind-spot.
- Byte-identical pairs dominate the graph; any modularity claim must be interpreted against this fact.

## Deliverables

- `[[h-new-235-mutashabih-full-graph|h-new-235]]-mutashabih-full-graph-prereg.md` (this file)
- `[[h-new-235-mutashabih-full-graph|h-new-235]]-mutashabih-full-graph.md` (findings)
- `scripts/h_new_235_mutashabih_graph.py`
- `journal/h-new-235-run-1.md`
- Ledger entry Wave-4 section.
