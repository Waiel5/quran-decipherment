---
finding_id: H-NEW-1770
type: pre-registration
date_locked: 2026-05-10
phase: B
status: PRE-REGISTERED
seed: 20260509
rules_tuple: (no-tashkeel, char-Levenshtein, graphemes, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)
data_source: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
parent_findings:
  - H-NEW-66 (verse-pair structural twin network; top-1 5-gram Jaccard)
  - H-NEW-167 (graph-theoretic properties of top-1 verse-twin graph; near-forest, 0 triangles)
  - H-NEW-201 (PageRank on verse-twin graph)
  - H-NEW-273 (Q1 ↔ Q108 twin liturgical anchor)
---

# Pre-Registration — H-NEW-1770 Corpus-Wide Verse-Twin Graph Deep Analysis (char-Levenshtein, threshold 0.70)

## 1. Background and motivation

H-NEW-66 and H-NEW-167 built the verse-twin graph under **top-1 5-gram-Jaccard** construction — each verse's nearest neighbour by raw substring overlap. That construction is architecturally anti-clustering (one out-edge per node), and H-NEW-167 found it to be a near-forest with 0 triangles, 1,293 components, max degree 31 (Q 55:13 — the *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* refrain).

H-NEW-1770 reconstructs the graph under a **different similarity instrument and different topology rule**:

- **char-Levenshtein normalized similarity** (substring-edit-distance based, not n-gram overlap)
- **Threshold 0.70**, not top-1 — a verse can have arbitrarily many twins
- Edges are undirected; the graph admits dense sub-clusters where top-1 forbids them
- Twin pericopes (surah-pair edge bundles) are first-class objects

This is a substantively different geometric view of the same verbal-resemblance phenomenon. The H-NEW-167 top-1 graph cannot fire on the litanic-refrain hub-spoke structure beyond degree = 31 (the refrain count); a threshold graph can saturate the full refrain-block as a clique. We expect Q 55, Q 26, Q 77 refrain-verses to become full cliques and dominate the high-degree tail. The novel test is whether HUBS BEYOND known refrains emerge — and whether the surah-pair edge-bundle distribution recovers known parallel-pericope pairs (the Q 6:151-152 / Q 17:31-32 commandment-doublet, the Madanī formulae across Q 2-5, the Pharaoh-magicians narrative).

## 2. Hypothesis (PRE-COMMIT)

**Primary hypothesis H1 (hub-leaf asymmetry, direction-locked):**
The char-Levenshtein verse-twin graph at threshold ≥ 0.70 shows non-uniform structure. Specifically:
- **H1a**: the top-10 hub verses each have ≥ 5 twin-links (degree ≥ 5)
- **H1b**: the bottom quartile (≥ 1,559 verses) have 0 twin-links (degree = 0, isolates)

Direction: hubs ≥ 5; bottom quartile = 0. Both directions locked before computing.

**Secondary hypothesis H2 (twin-pericope inter-surah clustering):**
At least **5 surah-pairs (i, j)** with i ≠ j exhibit ≥ 3 inter-surah twin-verse-links between them (the surah-pair-twin-edge-count). Direction-locked: ≥ 5 such pairs.

## 3. Decision rule (PRE-COMMIT)

| Outcome | H1a (top-10 deg ≥ 5) | H1b (bottom quartile = isolate) | H2 (≥ 5 pairs with ≥ 3 twin-edges) | Verdict |
|---|---|---|---|---|
| All three fire | ✓ | ✓ | ✓ | **PASS — non-uniform-twin-graph CONFIRMED** |
| 2 of 3 fire | mixed | mixed | mixed | **DIRECTIONAL** |
| ≤ 1 fires | — | — | — | **NULL** |

Bonferroni: 3 simultaneous direction-locked sub-claims at family-α = 0.05, α_per_test = 0.0167. Permutation null for H1a and H1b: random-rewire of the same edge-set across the 6,236 verses while preserving node degree, n_perm = 10,000 (degree-preserving null). For H2: count of surah-pairs with ≥ 3 twin-edges in observed vs degree-preserving null.

## 4. Methodology (LOCKED)

### 4.1 Corpus and rules-tuple

- Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (Hafs-Kūfan, no-tashkeel orthography)
- Basmala-handling: only the Q 1:1 basmala counts as a verse; the Q 2-Q 114 surah-opening basmalas are NOT verses (consistent with Hafs verse-numbering — they are present as part of v.1 only in Q 9 where there is no basmala)
- 6,236 verses, exactly as in H-NEW-66 / H-NEW-167
- Whitespace collapsed; no further normalization beyond no-tashkeel

### 4.2 Similarity instrument (LOCKED)

For each ordered pair (i, j) with i < j and surah(i) ≠ surah(j):
- Compute char-level Levenshtein edit distance `lev(text_i, text_j)` (insertions + deletions + substitutions, unit cost)
- Compute normalized similarity `sim(i, j) = 1 - lev(text_i, text_j) / max(len(text_i), len(text_j))`
- Edge added iff `sim(i, j) ≥ 0.70`

**Adjacency exclusion**: only inter-surah pairs are tested (consistent with H-NEW-66's "different-surah" framing for verse-twin-network claims). This is a deliberate choice: intra-surah refrain repetition is a separate phenomenon (H-NEW-1320 refrain saturation) and the surah-pair twin-edge bundle (H2) requires inter-surah by construction. Intra-surah twin-link counts are computed as a **secondary descriptive layer** but do NOT enter H1/H2 verdicts.

### 4.3 Computational strategy (efficient + correct)

Exact pairwise Levenshtein on ~19.4M pairs is feasible but slow (≈ 6h on a single core). Use length-prefiltering: only compute Levenshtein when `|len(text_i) - len(text_j)| / max_len ≤ 0.30` (a necessary condition for sim ≥ 0.70). This drops roughly 60-80% of candidate pairs cheaply. The remaining ~4-8M comparisons run in minutes with the standard `Levenshtein` python C-extension.

Verify: any candidate pair excluded by length-prefilter mathematically cannot achieve sim ≥ 0.70 because `sim ≤ 1 - |Δlen| / max_len`. The exclusion is sound (zero false negatives).

### 4.4 Graph construction

- Nodes: 6,236 verses indexed (surah, ayah)
- Edges: undirected, weight = sim, edge ⟺ sim ≥ 0.70 AND surah(i) ≠ surah(j)
- Build adjacency list; compute degree per node
- Identify connected components; LCC size; degree distribution

### 4.5 Top-10 hubs

Rank nodes by degree (twin-link count). Report:
- (surah, ayah)
- exact Arabic text (no-tashkeel)
- degree
- top-3 twin-targets per hub

### 4.6 Top-10 surah-pairs

For each pair (s1, s2) with s1 < s2: count edges (i, j) with surah(i) = s1, surah(j) = s2.
Rank surah-pairs by edge count.
Report top-10 (s1, s2) pairs + edge-counts + a sample twin (highest-sim edge).

### 4.7 Average twin-degree per surah

For each surah s: mean over its verses of inter-surah degree.
Report top-10 and bottom-10 surahs by mean twin-degree.

## 5. Permutation null (MW-2)

Degree-preserving rewire null (configuration model):
1. Take the observed degree sequence on 6,236 nodes
2. Generate 10,000 random graphs with the same degree sequence, respecting the inter-surah-only constraint
3. For each: compute (a) max degree, (b) count of isolates, (c) count of surah-pairs with ≥ 3 inter-surah-edges
4. Compute one-tailed p-value:
   - H1a: P(max-deg_null ≥ max-deg_obs)
   - H1b: P(isolate-count_null ≥ isolate-count_obs)
   - H2: P(rich-surah-pair-count_null ≥ rich-surah-pair-count_obs)

Seed = 20260509.

## 6. Honest disclosures (pre-committed)

- Threshold 0.70 is the LOCKED choice; sensitivity at thresholds 0.60 and 0.80 is REPORTED but not part of primary verdict
- Inter-surah-only is the LOCKED adjacency rule; intra-surah edges are described separately
- Refrain-verses (Q 55 *fa-bi-ayyi ālāʾi*, Q 26 *kadhdhabat* + variants, Q 77 *waylun yawmaʾidhin*) are **expected** to dominate the top-10 hubs by construction; the novel question is what NON-refrain verses appear in the top-10
- Equal NULL prominence: if H1a fails (no hub reaches degree 5), the finding is published as NULL with explicit pre-commit-honoring statement; the alternative interpretation (the corpus has no verbal-resemblance hub structure beyond classical refrain knowledge) is then the published thesis

## 7. Cross-references (anchor priors)

- H-NEW-66 (top-1 5-gram-Jaccard verse-twin graph; intra-surah 3.76× enrichment over null)
- H-NEW-167 (top-1 graph topology — near-forest, max-deg 31, 0 triangles, MW-5 PASS)
- H-NEW-201 (PageRank on verse-twin graph; refrain-hubs dominate)
- H-NEW-273 (Q 1 ↔ Q 108 liturgical anchor pair; threshold-based identification)
- H-NEW-1320 (refrain saturation; per-surah)
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, fann 62 (munāsabāt al-āyāt — relevant to twin-pericope clustering)
- al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar* (verse-by-verse parallel-passage identification)
- Yaḥyā Mīr ʿAlam, *Mawsūʿat al-qaḍāyā al-mufaṣṣala fī mutashābih al-Qurʾān* (modern compendium of Quranic verse-twins)

## 8. Reproducibility

- Pre-reg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/prereg-h-new-1770-verse-twin-graph.md`
- Script: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/scripts/h-new-1770.py`
- JSON output: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-1770.json`
- Finding: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-1770-verse-twin-graph-deep.md`
- Pre-reg SHA-256 embedded in script header; script fails fast on mismatch.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
