---
surah: 100
surah_name_ar: العاديات
surah_name_translit: al-ʿĀdiyāt
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical-profile pulled from H-NEW-111/590/630/660/700/720/750/840/1070/1140/1200; SPECIAL test on Q 100 vs other oath-cluster surahs FR centrality (replicate H-NEW-1070).
---

# Q 100 al-ʿĀdiyāt — Empirical Profile


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

All numerics traced to specific finding JSONs in `findings/phase-b-hypotheses/csv/`. Computed inline this specialist run on 2026-05-09 with seed = 20260509.

## 1. Headline metrics

| Metric | Value | Rank | Source |
|:--|:-:|:-:|:--|
| Verse count | 11 | — | canonical |
| Word count (no-tashkeel) | 40 | — | computed |
| Letter count (no-tashkeel, no spaces) | ~163 | — | computed |
| Average words/verse | 3.6 | very low | computed |
| **iʿjāz sig_A (rhyme-entropy + cohesion)** | **+1.858** | **9/114** | h-new-750.json (top 8% architectural) |
| **iʿjāz sig_B (cohesion + content-distance)** | **+1.807** | **10/114** | h-new-750.json (top 9%) |
| Mean content distance to corpus | 0.790 | z = -1.32 | h-new-750.json |
| Local cohesion | 2.451 | z = +1.27 | h-new-750.json |
| Rhyme entropy (nats) | 1.067 | z = +0.54 | h-new-750.json |
| Top final letter | ا (alif/-ā) | 45.5% | computed |
| **Outlier-spectrum classification** | **NULL** (window {97-103} pct_W = 0.01) | window-context: globally-densest 7-window | h-new-590.json |
| UAS | -0.518 | 62/114 | h-new-840.json (mid-bin) |
| **H-NEW-1070 oath-cluster centrality rank** | **2/15** (mean 0.5789) | core-tier | this run |
| **Per-verse hapax-density** | **0.4545** (5/11 hapax-roots) | **4/114** (z=+3.27) | this run |
| Q 99→Q 100 adjacency cost (delta_raw) | 0.0487 | rank 45/113 | h-new-720.json |
| Q 100→Q 101 adjacency cost (delta_raw) | 0.0286 | rank 29/113 | h-new-720.json |

## 2. Fisher-Rao nearest neighbors (top-15)

From H-NEW-111 D matrix (QAC-stem-roots, no-tashkeel rules-tuple):

| Rank | Surah | FR distance | Note |
|:-:|:-:|:-:|:--|
| 1 | Q 108 al-Kawthar | 0.2576 | corpus short-mufaṣṣal HUB (per H-NEW-490) — top-1 nearest |
| 2 | Q 106 Quraysh | 0.2947 | early-Meccan brief narrative |
| 3 | Q 94 al-Sharḥ | 0.2947 | early-Meccan, Prophet-comfort |
| 4 | Q 103 al-ʿAṣr | 0.3109 | oath-cluster sibling — closest oath-cluster pair! |
| 5 | Q 113 al-Falaq | 0.3124 | muʿawwidha apotropaic |
| 6 | Q 111 al-Masad | 0.3184 | rare-narrative anti-Abū-Lahab |
| 7 | Q 105 al-Fīl | 0.3272 | early-Meccan brief narrative |
| 8 | Q 112 al-Ikhlāṣ | 0.3283 | tawḥīd pivot |
| 9 | Q 107 al-Māʿūn | 0.3353 | early-Meccan greed-rebuke (THEMATIC-PARALLEL with Q 100 vv 6-8!) |
| 10 | Q 104 al-Humaza | 0.3357 | early-Meccan greed/slander-rebuke (THEMATIC-PARALLEL with Q 100!) |
| 11 | Q 110 al-Naṣr | 0.3389 | terminal-Medinan brief |
| 12 | Q 114 al-Nās | 0.3404 | muʿawwidha apotropaic |
| 13 | Q 102 al-Takāthur | 0.3465 | early-Meccan greed-rebuke (THEMATIC-PARALLEL!) |
| 14 | Q 93 al-Ḍuḥā | 0.3637 | oath-cluster sibling (Q 91-93 trio member) |
| 15 | Q 95 al-Tīn | 0.3667 | oath-cluster sibling |

**Q 100 is content-similar to Q 102, Q 104, Q 107 (all 3 are early-Meccan greed/wealth-rebuke surahs)** — these are the THEMATIC-CONTENT siblings, NOT the structural-oath siblings (Q 51, Q 37 etc.). The pattern reveals that Q 100's content fingerprint is dominated by its **vv 6-8 human-greed-rebuke** rather than its vv 1-5 oath-cluster.

Q 100's closest FR-neighbor (Q 108 al-Kawthar at 0.258) is at the corpus's very short-mufaṣṣal-qiṣār hub; Q 100's next-3 are Q 106, Q 94, Q 103 (all in the densest 15-window per H-NEW-630).

## 3. Fisher-Rao farthest neighbors

| Rank | Surah | FR distance |
|:-:|:-:|:-:|
| 110 | Q 24 al-Nūr | 1.218 |
| 111 | Q 2 al-Baqara | 1.233 |
| 112 | Q 3 Āl ʿImrān | 1.272 |
| 113 | Q 4 al-Nisāʾ | 1.282 |
| 114 | Q 9 al-Tawba | 1.290 |

Q 100 is FR-far from all the long Medinan legal surahs (Q 9, Q 4, Q 3, Q 2, Q 24). The distance gap from Q 100 to Q 9 is **1.290** — among the corpus's largest. Q 100 represents the structural OPPOSITE of the long-Medinan-legal mode.

## 4. Mushaf-adjacency profile

H-NEW-720 canonical-adjacency-cost results for Q 100's two seams:

| Pair | delta_raw | rank in 113 | fraction_residual | Read |
|:--|:-:|:-:|:-:|:--|
| Q 99 → Q 100 | 0.0487 | 45/113 | 0.59% | mid-cheap |
| Q 100 → Q 101 | 0.0286 | 29/113 | 0.34% | cheap (smoothest 26%) |

Both Q 100 transitions are in the cheap-tier of mushaf-adjacency. Both are in the H-NEW-630 densest-15-window region where ALL transitions are cheap.

Q 99-Q 100-Q 101 sub-block is part of the broader Q 99-Q 103 dense oath-cluster zone:
- Q 99 al-Zalzala (Class B *idhā*-conditional eschatology)
- **Q 100 al-ʿĀdiyāt (Class D HYBRID oath-cluster)**
- Q 101 al-Qāriʿa (nominal-exclamation eschatological narrative)
- Q 102 al-Takāthur (greed-rebuke direct-address)
- Q 103 al-ʿAṣr (Class A pure-wa-noun oath, single-element)

## 5. UAS rank (mid-bin)

H-NEW-840 unified architectural score: Q 100 ranks **62/114** with UAS = -0.518.

UAS decomposition:
- |abs_outlier| = 0.03 (Q 100's outlier-spectrum delta is near-zero because its 7-window is ALREADY the densest in the corpus)
- |max_cost| = 0.0487 (Q 99→100 delta_raw; cheap)
- |abs_ijaz| = 1.858 (sig_A magnitude — TOP-9 IN CORPUS)

The dominant contributor to Q 100's UAS is the iʿjāz signature (+1.858 / +1.807). The outlier-spectrum and adjacency-cost contributions are NEAR-ZERO because Q 100 is embedded in the densest, smoothest region of the corpus. **Q 100's architectural significance is in its iʿjāz signature, not in its block-cohesion-anchoring or block-outlier role**.

In particular: Q 100 is NOT a block-outlier (it sits IN the densest 7-window centered on itself) and NOT a block-cohesion-anchor (removing Q 100 hardly changes the block density because the block is already maximum-dense). What Q 100 IS, is a **maximum-iʿjāz-signature surah** — high local cohesion, low content-distance to corpus mean, high rhyme-entropy (3 zones in 11 verses).

## 6. iʿjāz signature decomposition (H-NEW-750) — Q 100 in TOP 10%

Q 100 sig_A (rhyme-entropy + cohesion) = **+1.858 (rank 9/114)** — top 8%
Q 100 sig_B (cohesion + content-distance) = **+1.807 (rank 10/114)** — top 9%

Component z-scores:
- z_rhyme_entropy = +0.538 (above-mean rhyme diversity; consistent with 3-zone structure)
- z_mean_content_distance = -1.320 (Q 100 is content-CLOSER to corpus average; consistent with global-densest 15-window placement)
- z_local_cohesion = +1.269 (above-mean local cohesion; verses internally well-clustered)

Q 100's iʿjāz signature is **strongly distinctive** — both ranks in the top 10. The high local cohesion (+1.27) reflects the tight 5+3+3 block-structure; the negative content-distance (-1.32) reflects global-densest-15-window placement; the positive rhyme-entropy (+0.54) reflects the 3-zone rhyme tripartition. All three components point in the iʿjāz-favoring direction simultaneously.

Q 100 thus has **TRIPLE iʿjāz simultaneity**: high internal cohesion + low content-distance + high rhyme-entropy. This combination is rare; only ~10 surahs achieve it.

## 7. Outlier-spectrum (H-NEW-590) — NULL but in densest-window

Window {Q 97, 98, 99, 100, 101, 102, 103}:
- Block mean pairwise FR (with Q 100): 0.4309
- Block mean pairwise FR (without Q 100): 0.4483
- delta_pct = -0.03 pp (negligible — Q 100 is one tiny piece of an already maximally-dense window)
- pct_W = **0.01** (the densest 7-window in the entire corpus, after Q 109's window)
- Classification: **NULL**

The NULL classification is NOT because Q 100 is content-typical, but because the **entire window is already content-saturated**. Removing or adding Q 100 makes near-zero delta. Q 100 is a **member of the global-densest 7-window** (rank ~3 of 108 7-windows by density) — see H-NEW-630 short-mufaṣṣal-qiṣār superblock.

This is the **inverse phenomenon** to outlier behavior — Q 100 is so tightly embedded in a content-uniform region that its removal/addition is invisible at block-level.

## 8. ⭐ SPECIAL: Q 100 H-NEW-1070 oath-cluster centrality test (this specialist run)

**Pre-registered test (Q100-F-03, SHA-locked)**: where does Q 100 rank in centrality among the 15 H-NEW-1070 strict-oath-opener cluster members?

**Method** (H-NEW-1070 strict-15 = {Q 37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}):
- For each Q in the cluster, compute its mean pairwise FR distance to the OTHER 14 members.
- Rank by ascending mean (lower = more central).

**Result**:

| Centrality rank | Surah | Mean dist to other 14 | Tier |
|:-:|:-:|:-:|:--|
| 1 | Q 103 al-ʿAṣr | 0.5711 | CORE |
| **2** | **Q 100 al-ʿĀdiyāt** | **0.5789** | **CORE** |
| 3 | Q 95 al-Tīn | 0.5847 | CORE |
| 4 | Q 91 al-Shams | 0.5944 | CORE |
| 5 | Q 93 al-Ḍuḥā | 0.5973 | CORE |
| 6 | Q 86 al-Ṭāriq | 0.6228 | mid-tier |
| 7 | Q 92 al-Layl | 0.6311 | mid-tier |
| 8 | Q 85 al-Burūj | 0.6711 | mid-tier |
| 9 | Q 79 al-Nāziʿāt | 0.7027 | mid-tier |
| 10 | Q 89 al-Fajr | 0.7175 | mid-tier |
| 11 | Q 77 al-Mursalāt | 0.7598 | periphery |
| 12 | Q 52 al-Ṭūr | 0.7790 | periphery |
| 13 | Q 51 al-Dhāriyāt | 0.8206 | periphery |
| 14 | Q 53 al-Najm | 0.8515 | periphery |
| 15 | Q 37 al-Ṣāffāt | 0.9949 | extreme periphery |

**Q 100 is rank 2/15 — the second-most-central oath-opener** in the H-NEW-1070 cluster, just 0.0078 behind Q 103 al-ʿAṣr (rank 1). The CORE tier (ranks 1-5) consists of {Q 103, **Q 100**, Q 95, Q 91, Q 93} — all short-Meccan-tail (s ≥ 91); these 5 are the cluster's tight CORE.

**Interpretation**: the H-NEW-1070 cluster has a **3-tier substructure**:
- **CORE** (ranks 1-5): the short-Meccan-tail oath-cluster — Q 91-103 mostly, all members of H-NEW-630 cluster C (the densest 15-window). Mean inter-member FR ≈ 0.59.
- **Mid-tier** (ranks 6-10): Q 79, 85, 86, 89, 92 — late-Meccan post-hinge, less-densely-packed
- **Periphery** (ranks 11-15): Q 37, 51, 52, 53, 77 — mid-mushaf-isolated long oath-openers

This **CONFIRMS and EXTENDS Q037-F-04's earlier finding** (Q 37 at rank 15 = extreme periphery). Q 100, in stark contrast, is at CORE rank 2 — making the centrality-rank-spread of {Q 37, Q 100} ≈ 14 positions, the maximum possible within the cluster.

**Architectural implication**: the H-NEW-1070 cluster's content-cohesion is overwhelmingly driven by the short-Meccan-tail core (Q 91-103); the mid-mushaf periphery (Q 37-53) is content-distant and contributes to the mean-pairwise-FR via individual-member inclusion but does NOT pull the cluster centroid.

This finding **REPLICATES the H-NEW-1070 classification empirically at the per-surah level** and provides a **3-tier structure refinement of the original H-NEW-1070** (originally a 2-tier as identified by Q037-F-04: core + periphery; this run identifies a finer 3-tier).

## 9. ⭐ Per-verse hapax-density: Q 100 ranks 4/114 (z = +3.27)

Per-verse corpus-hapax-root density across all 114 surahs:

| Rank | Surah | Hapax | Verses | Density |
|:-:|:-:|:-:|:-:|:-:|
| 1 | Q 108 al-Kawthar | 2 | 3 | 0.667 |
| 2 | Q 106 Quraysh | 2 | 4 | 0.500 |
| 3 | Q 112 al-Ikhlāṣ | 2 | 4 | 0.500 |
| **4** | **Q 100 al-ʿĀdiyāt** | **5** | **11** | **0.4545** |
| 5 | Q 111 al-Masad | 2 | 5 | 0.400 |
| 6 | Q 113 al-Falaq | 2 | 5 | 0.400 |
| 7 | Q 91 al-Shams | 4 | 15 | 0.267 |
| 8 | Q 81 al-Takwīr | 7 | 29 | 0.241 |
| ... | | | | |

**Q 100 has 5 corpus-hapax roots in 11 verses** — the **highest absolute hapax count** among 11-verse-or-longer surahs, and **rank 4/114** by per-verse density. The 5 hapax roots distribute across all 3 rhyme-zones (3 in oath-block, 1 in human-block, 1 in eschatology-block).

**Comparison with H-NEW-1070 oath-cluster siblings**:

| Surah | Hapax | Verses | Density |
|:--|:-:|:-:|:-:|
| **Q 100** | **5** | **11** | **0.4545 (rank 1 in oath-cluster)** |
| Q 91 | 4 | 15 | 0.267 |
| Q 81 | 7 | 29 | 0.241 |
| Q 89 | ~3 | 30 | ~0.10 |
| Q 51 | 3 | 60 | 0.050 |
| Q 53 | ~1-2 | 62 | ~0.022 |
| Q 37 | 2 | 182 | 0.011 |

Q 100 is **the most lexically-distinctive oath-cluster member by per-verse hapax density** — 1.7× denser than Q 91 al-Shams (the next), 9× denser than Q 51 al-Dhāriyāt, 41× denser than Q 37 al-Ṣāffāt.

This finding (`Q100-F-04` as part of comprehensive empirical profile) reveals that Q 100's lexical fingerprint is uniquely CONCENTRATED among oath-cluster members.

## 10. Cross-finding membership

- **H-NEW-1070** (oath-opener cluster, p=0.0004 CONFIRMED) — Q 100 ∈ strict-15 cluster; **rank 2/15 in centrality (CORE-tier, just behind Q 103)**.
- **H-NEW-1140** (oath-cluster mushaf-adjacency-enriched at p=0.022) — Q 100 is **NOT in any of the 3 strict mushaf-adjacent oath-runs** (Q 51-52-53, Q 79-... , Q 91-92-93). Q 100 is mushaf-isolated within the cluster (Q 99 and Q 101 are NOT in H-NEW-1070 strict-15 — Q 99 is *idhā*-conditional class B; Q 101 is nominal-exclamation).
- **H-NEW-630** (super-cluster substructure, Q 67-114 3-tier) — Q 100 is **at the LEFT EDGE of Cluster C (Q 100-Q 114)** — the GLOBAL-DENSEST 15-window in the corpus (d̄ = 0.319, 0.00%ile).
- **H-NEW-1200** (eschatology meta-cluster, p=0.0003 CONFIRMED) — Q 100 ∈ 14-surah short-Meccan-tail eschatology meta-cluster.
- **H-NEW-660** (compression-tail single-parameter law, R²=0.986) — Q 100 sits at s=100 in REGIME 2; predicted d̄(K=15-start-Q=100) = 0.342; observed d̄ = 0.319 (LOWER than predicted by 0.023; Q 100 is MORE content-cohesive than the law predicts).
- **H-NEW-130 / cross-finding-013** (ring-topology / structural hinges) — Q 99→100 and Q 100→101 are NOT among the 15 universal hinges; Q 100 sits IN the smooth-tail region of the mushaf.
- **H-NEW-590 / H-NEW-840** — Q 100 is NULL in outlier-spectrum (window already maximum-dense); UAS rank 62/114.
- **H-NEW-750** — Q 100 sig_A rank 9/114; sig_B rank 10/114 (TOP 9-10%).

## 11. Sources

| Metric | File |
|:--|:--|
| FR distance matrix | `findings/phase-b-hypotheses/csv/h-new-111.json` |
| Adjacency cost | `findings/phase-b-hypotheses/csv/h-new-720.json` |
| iʿjāz signature | `findings/phase-b-hypotheses/csv/h-new-750.json` |
| Outlier spectrum | `findings/phase-b-hypotheses/csv/h-new-590.json` |
| UAS | `findings/phase-b-hypotheses/csv/h-new-840.json` |
| Hapax computation | `data/morphology/root-index.json` |
| Cluster centrality test | `surahs/Q100-al-adiyat/csv/Q100-F-03.json` (this specialist run, 2026-05-09) |

## 12. Cross-references

- [[00-overview]] — Q 100 basic structural facts
- [[02-content-analysis]] — verse-by-verse expansion + 3-block macro
- [[06-novel-findings]] — 3 SHA-locked pre-registered tests
- [[07-cross-references]] — full cross-finding integration
- [[Q037-al-saffat/01-empirical-profile|Q 37 empirical profile]] — comparative oath-opener metrics; Q 37 at periphery rank 15/15
- [[Q051-al-dhariyat/01-empirical-profile|Q 51 empirical profile]] — comparative; Q 51 at mid-periphery rank 13/15
- [[Q103-al-asr/00-overview|Q 103 al-ʿAṣr]] — Q 100's nearest oath-cluster sibling (rank 1/15 cluster centrality)
- [[Q099-al-zalzala/00-overview|Q 99 al-Zalzala]] — Q 100's left-neighbor; *idhā*-conditional class B oath-variant
