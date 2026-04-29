---
id: H-NEW-134
title: Minimum Spanning Tree of the Fisher-Rao surah graph
phase: B
status: EXPLORATORY-POST-HOC (inline descriptive analysis; primary-claim single-test α=0.05 cap)
date: 2026-04-17
parent_data: findings/phase-b-hypotheses/csv/h-new-111.json
seed: 20260417
rules_tuple: (114 surahs Hafs-Kūfan; K=500 top QAC roots; Dirichlet-0.5 smoothing; Fisher-Rao arccos-Bhattacharyya; MST via Kruskal)
verdict: EXPLORATORY-DIRECTIONAL for consecutive-mushaf-MST-enrichment; DESCRIPTIVE for node-property observations
---

# [[h-new-134-formal-prophet-named-signature|H-NEW-134]] — MST of the Fisher-Rao surah graph

## Provenance

Inline-computed by the session-lead integrator (not a dispatched
specialist). Uses the pre-computed [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D-matrix (114×114
Fisher-Rao distances). No new feature extraction.

**Post-hoc origin disclosed**: the analysis was NOT pre-registered
prior to viewing [[h-new-111-fisher-rao-mushaf|H-NEW-111]] results. Single-test α=0.05 cap applies.

## Primary observations

### 1. MST super-hub: Q 108 al-Kawthar (degree 24)

**Q 108 al-Kawthar has MST-degree 24**. The next-highest nodes are
Q 7 al-Aʿrāf (10), Q 112 al-Ikhlāṣ (8), Q 64 al-Taghābun (7). Q 108
is a clear 2.4× outlier.

**Mechanism**: Q 108 is the shortest surah (3 verses, 10 words:
"Innā aʿṭaynāka l-kawthar. Fa-ṣalli li-rabbika wa-nḥar. Inna
shāniʾaka huwa l-abtar."). As such, its root-distribution
concentrates probability on ~10 roots, producing a LOW information
content profile that serves as nearest-neighbor for many other short
mufaṣṣal surahs. Q 108 is the **information-geometric origin of
the short-mufaṣṣal cluster**.

This is a metric-specific property, not a content-design claim.
But the fact that the shortest surah sits in the structural "origin"
position is a non-trivial observation about how the mushaf handles
its extremum.

### 2. MST centroid: Q 36 Yā-Sīn (max-dist 6.201)

**Q 36 Yā-Sīn is the MST centroid** — the surah with the smallest
maximum MST distance to any other surah (6.201). No other surah
has max-dist below ~6.8.

**Tension with [[h-new-82-yasin-heart|H-NEW-82]]**: [[h-new-82-yasin-heart|H-NEW-82]] REFUTED the classical
"Q 36 is heart of the Quran" claim (Tirmidhī ḥadīth graded ḍaʿīf;
empirical centroid on alternative axes = Q 10 Yūnus / Q 57 al-Ḥadīd
/ Q 46 al-Aḥqāf). [[h-new-134-formal-prophet-named-signature|H-NEW-134]]'s MST centroid is Q 36.

**Resolution**: the two findings are metric-sensitive, not
contradictory. Under:
- **Full Fisher-Rao metric + MST-max-distance centrality**: Q 36
- **Alternative aggregation metrics (per [[h-new-82-yasin-heart|H-NEW-82]])**: Q 10 / Q 57 / Q 46

Claim: the "heart of the Quran" designation is NOT uniquely
defensible across metrics, but it is DEFENSIBLE under the specific
Fisher-Rao MST-centroid criterion.

This does NOT restore the Tirmidhī ḥadīth's authenticity (grading
remains ḍaʿīf). It merely notes that classical intuitions sometimes
align with specific statistical operationalizations.

### 3. Consecutive-mushaf MST-adjacency enrichment

**6.2% of consecutive-mushaf pairs are MST-adjacent** (7 of 113).
Random-pair MST-adjacency expectation: 113 / (114×113/2) ≈ 1.75%.

**Enrichment ratio: 3.5×**. Rough binomial test under random-edge
null: p = C(113, 7) × (1.75%)^7 × (98.25%)^106 — small-count; under
permutation null this would be moderately significant but well
short of extreme p. Single-test α=0.05 cap.

**What this adds to [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]**: the Fisher-Rao geodesic
optimality (L_mushaf/L_2opt = 1.107) is NOT driven by consecutive
surahs being MST-neighbors (which they mostly aren't). Instead, it's
driven by consecutive surahs being CLOSE IN FISHER-RAO DISTANCE
without necessarily being MST-adjacent.

**The mushaf follows a "near-neighbor path" that loosely tracks
the MST but does not strictly follow it.** Most consecutive-surah
edges are weighted-short in Fisher-Rao space even when they're
not MST edges.

### 4. Structural isolations confirmed via MST

Multiple surahs with KNOWN structural distinctiveness are MST LEAVES
(degree 1):

- **Q 1 al-Fātiḥa** — leaf (confirms sui generis from different angle)
- **Q 62 al-Jumuʿa** — leaf (despite cluster-network degree 4-5;
  confirms [[h-new-112-spectral-network|H-NEW-112]]'s refinement that Q 62 is spectral PEAK of
  back-Medinan community, NOT bridging between communities)
- **Q 55 al-Raḥmān** — leaf (consistent with [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] anti-geodesic
  refrain structure)
- **Q 50 Qāf** — leaf (despite [[cross-finding-010-extended-network|cross-finding-010]]'s upper-mid hub
  status in cluster-network)
- **Q 59 al-Ḥashr** — leaf (despite Khawātim-density rank 1 per
  [[h-new-95-khawatim-extension|H-NEW-95]])
- **Q 114 al-Nās** — leaf

**Interpretation**: CLUSTER-NETWORK hubness ≠ CONTENT-NEIGHBORHOOD
hubness. A surah can be structurally-central in taxonomic clustering
(many shared classifications) while being CONTENT-DISTINCTIVE
(far from content-neighbors in Fisher-Rao space). The two are
genuinely orthogonal axes.

### 5. MST diameter

Q 33 al-Aḥzāb (Medinan, 73 verses) ↔ Q 30 al-Rūm (Late-Meccan, 60
verses). MST path weight: 11.688.

These two surahs are on OPPOSITE ends of the MST — the maximally-
content-separated surah pair. Both are chronologically Late-Meccan/
Medinan, but they represent OPPOSITE thematic poles in root-content.

## MST degree distribution

| Degree | Count |
|---:|---:|
| 1 (leaves) | 72 |
| 2 | 16 |
| 3 | 15 |
| 4 | 7 |
| 7 | 1 (Q 64) |
| 8 | 1 (Q 112) |
| 10 | 1 (Q 7) |
| 24 | 1 (Q 108) |

The distribution is **heavy-tailed** (one super-hub + 3 sub-hubs
+ long tail of leaves). This is characteristic of SCALE-FREE-like
structure, though a formal test is needed.

## Top-15 MST hubs

| Rank | Q | Name | Degree | Role |
|---:|---:|---|---:|---|
| 1 | 108 | al-Kawthar | 24 | Super-hub, short-mufaṣṣal origin |
| 2 | 7 | al-Aʿrāf | 10 | Long-Meccan narrative hub |
| 3 | 112 | al-Ikhlāṣ | 8 | Back-terminal invocation hub |
| 4 | 64 | al-Taghābun | 7 | Musabbiḥāt extension hub |
| 5-7 | 111, 103, 78 | al-Masad, al-ʿAṣr, al-Nabaʾ | 4 each | Mufaṣṣal secondary |
| 8-11 | 63, 23, 6, 2 | | 4 each | Mid-corpus secondary |
| 12-15 | 110, 105, 102, 100 | | 3 each | Q 108-connected secondary |

## Caveats

1. **Single metric**: this is Fisher-Rao arccos-Bhattacharyya on top-500 roots. Different metrics or feature spaces could produce different MSTs (robustness-across-distance-metric test queued).
2. **Post-hoc**: not pre-registered. Descriptive observations.
3. **Q 108 super-hub is partly mechanical**: shortest-surah effect. A length-normalized MST would show a different picture.
4. **Q 36 centroid claim does NOT restore Tirmidhī ḥadīth authenticity**: classical hadith-grading remains independent.

## Queued follow-ups

- H-NEW-134.1: length-normalized MST (mitigate Q 108 artifact)
- H-NEW-134.2: robustness across Fisher-Rao, Hellinger, KL, JS distances
- H-NEW-134.3: MST comparison between mushaf order and Nöldeke order (which better preserves MST-path?)
- H-NEW-135 (proposed): MST on VERSE-level (sub-surah fractal extension)

## Connections to prior findings

- Extends [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] (Fisher-Rao geodesic optimality)
- Orthogonalizes [[cross-finding-010-extended-network|cross-finding-010]] (cluster-network hubness vs content-neighborhood hubness)
- Partial metric-specific rehabilitation of classical Q 36 centrality claim (does NOT override [[h-new-82-yasin-heart|H-NEW-82]])
- Consistent with [[h-new-89-meta-cluster-network|H-NEW-89]] / [[h-new-112-spectral-network|H-NEW-112]] Q 62 characterization (community-peak, not cluster-bridge)
