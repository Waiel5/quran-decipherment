# Graph-Theory Roots — Run 1 Journal

**Agent:** graph-theory (Phase B novelty)
**Date:** 2026-04-12
**Working assumptions:** the Quran is one text; we use root co-occurrence and surah-root bipartite structure as the graph substrate.

## Inputs

- `data/morphology/root-index.json` (1,642 roots → list of (surah, verse, word) — built earlier by root-cartographer)
- `data/morphology/root-stats.csv` (per-root metadata)
- `data/alt-text/risan-quran-json/dist/chapters/{1..114}.json` (for surah names + Meccan/Medinan label)
- `quran-text/quran-no-tashkeel.json` (canonical Quran text)

## Pipeline (all scripts under `/tmp` for this run; outputs to data/ and findings/)

| Stage | Script | Output |
|-------|--------|--------|
| 1. Bipartite graph | `/tmp/graph_build.py` | `data/morphology/surah-root-graph.json`; `/tmp/verse_roots.json` |
| 2. Surah similarity | `/tmp/graph_similarity.py` | `/tmp/surah_similarity.json` |
| 3a. Agglomerative (avg/Jacc) | `/tmp/graph_clustering.py` | `/tmp/surah_clusters.json` |
| 3b. Complete linkage + cosine | `/tmp/graph_clustering2.py` | (printed only) |
| 3c. K-means cosine | `/tmp/graph_kmeans.py` | `/tmp/kmeans_clusters.json` |
| 4. Root co-occurrence | `/tmp/graph_cooccur.py` | `data/morphology/root-cooccurrence-graph.json`; `/tmp/root_cooccur_full.json` |
| 5. Centrality (deg/PR/eig) | `/tmp/graph_centrality.py` | `/tmp/centrality.json` |
| 6a. Label propagation (failed) | `/tmp/graph_community.py` | `/tmp/communities.json` |
| 6b. Louvain | `/tmp/graph_community2.py` | `/tmp/communities_louvain.json` |
| 7. Brandes betweenness | `/tmp/graph_betweenness.py` | `/tmp/betweenness.json` |
| 8. Configuration null (200×) | `/tmp/graph_null.py` | `/tmp/null_results.json` |
| 9. Surah backbone | `/tmp/graph_backbone.py` | `/tmp/surah_backbone.json` |

`networkx` was not installed; everything is pure stdlib (Brandes, Louvain, k-means, label propagation all hand-rolled).

## Decisions and gotchas

1. **Verse coverage.** root-index.json yields 6,214 distinct (surah,verse) pairs out of 6,236. The 22 missing verses are basmala-only or no-content tokens dropped by the QAC morphology. Acceptable; documented.
2. **Bipartite graph counts.** 17,496 (surah,root) edges. surah 1 has 18 distinct roots; surah 2 has 585. Largest by distinct roots: Al-Baqarah 585 → Al-A'raf 477 → An-Nisa 462.
3. **Avg-linkage on Jaccard (clustering attempt 1)** is pathological: it produces a giant blob plus singleton outliers (the very short surahs Al-Masad, Al-Kawthar, etc.) because Jaccard with extremely small sets is volatile. Reported, but a useful clustering needs cosine on TF-IDF weighted vectors. Switched to complete-linkage and to k-means cosine.
4. **Label propagation collapsed** the 608-node co-occurrence graph (w≥5) into one community at iteration 3 — a known LP failure on graphs with strong hubs (Allah's degree = 509 of 608 possible). Fell back to Louvain; that worked, returning 29 communities at modularity Q=0.0812 with semantically interpretable groups.
5. **Configuration-model null** (Stage 8): used the bipartite stub-shuffle preserving (verse degree, root frequency). Slow but tractable: 200 draws in 22 s. All key cohesion metrics deviate at z > 5.
6. **Length-controlled "most unique" surah:** raw avg-Jaccard puts s108 Al-Kawthar first because it's tiny. After regressing avg-Jaccard on log(verse_count) and ranking residuals, the most-unique surah is **s55 Ar-Rahman** at residual −0.076 — substantively meaningful, since Ar-Rahman is famously stylistically distinctive ("Which favors of your Lord will you deny?" refrain). Second-most-unique: s80 'Abasa.

## Prior art (web search)

Two directly relevant papers found:

1. **"A Graph-based Algorithm for Clustering Qur'anic Surahs"** — Tariq et al., Malaysian J. Computer Science (ResearchGate). Graph-based surah clustering.
2. **"Text Classification via Network Topology: A Case Study on the Holy Quran"** — uses network topology features for Quran text classification (presumably Meccan/Medinan).
3. **The Quranic Arabic Corpus Ontology** (corpus.quran.com/ontology.jsp) — manually-curated knowledge graph of 300 Quranic concepts with 350 relations. Different (semantic, hand-built) but adjacent.
4. **"Semantic Graph Knowledge Representation for Al-Quran Verses Based on Word Dependencies"** — RNN+dependency-graph approach.
5. **RPubs: "Quran English Word Network Analysis Using Quanteda"** — exploratory English-translation network using quanteda.

None of the indexed work appears to (a) build the surah-root bipartite graph directly from QAC root data, (b) compute root co-occurrence at the *verse* level with weight filtering and Brandes betweenness, or (c) compare against a configuration-model null. The closest prior work treats surahs as documents with TF-IDF (a common information-retrieval approach). We are doing a stricter graph-theoretic analysis grounded in roots and verses.

## Headline numbers

- **Bipartite graph:** 114 surahs × 1,642 roots, 17,496 edges.
- **Co-occurrence graph (w≥5):** 608 nodes (out of 1,642), 8,556 edges.
- **Most central root** by every centrality measure: Allah (Alh).
- **Most central root *that isn't a top-25-frequency hub*** (i.e. structural bridge): **xlq خلق "create"** (BC = 2412), then **qlb قلب "heart"** (BC = 2049).
- **Most unique surah (length-controlled):** Ar-Rahman (s55), residual −0.0761.
- **Most central surah (raw):** Yunus (s10), avg-Jaccard 0.230.
- **Best Meccan/Medinan recovery:** k-means cosine k=5; cluster C1 is 97% Meccan (61/63), cluster C2 is 89% Medinan (24/27).
- **Configuration-null surprise:** observed sum-of-edge-weights = 211,298 vs null mean 193,119 (z = +36.3); this is the strongest deviation seen.
- **Number of Louvain communities:** 29 (Q = 0.0812).

## Honest negatives

- Agglomerative average-linkage on Jaccard → useless dendrogram dominated by Al-Masad-as-outlier-first-merge.
- Label propagation on the dense co-occurrence graph → one giant community.
- Direct k=2 Meccan/Medinan recovery via *any* unsupervised clustering: the partition is too unbalanced (86 Meccan / 28 Medinan), and the most informative split happens at k=5 instead.
- Top-20 betweenness centrality is dominated by sheer-frequency hubs; the bridge story only emerges after frequency-discount filtering.

## Files written

- `/Users/grey/Downloads/quran/data/morphology/surah-root-graph.json` — bipartite adjacency
- `/Users/grey/Downloads/quran/data/morphology/root-cooccurrence-graph.json` — w≥5 cooc graph
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/graph-theory-roots.md` — the report

## Next steps (not done in this run)

- Weighted Brandes (currently using unweighted shortest paths on the filtered graph; weighted version would weight by 1/w).
- Higher-resolution Louvain (multi-level) — modularity Q=0.08 is quite low, partially because two giant hubs (Allah, qwl) saturate the graph.
- Backbone extraction via disparity filter (Serrano et al. 2009) — the natural way to thin a hub-dominated weighted graph.
- Cross-validate clusters against the Nöldeke / Sadeghi Meccan-period subdivisions (early/middle/late Meccan), not just the binary Meccan/Medinan label. The k=10 cosine clusters look like they may correspond to revelation periods.
