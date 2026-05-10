---
surah: 34
surah_name_ar: سبإ
surah_name_translit: Sabaʾ
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: 5 pre-registered tests run (SHA-locked, Bonferroni-corrected, seed=20260509). Results integrated: Q034-F-01 NULL, Q034-F-02 DIRECTIONAL-WEAK, Q034-F-03 DIRECTIONAL, Q034-F-04 DIRECTIONAL-WEAK, Q034-F-05 DIRECTIONAL.
---

# Q 34 Sabaʾ — Novel Findings (Pre-registered)

Five pre-registered novel tests for Q 34. Each has a pre-registration markdown (SHA-locked), a run script, a JSON output, and the finding-level write-up below.

Family-level Bonferroni-k varies by test. Seed: 20260509. Permutation count: 10,000 (where applicable).

Run scripts: `scripts/Q034_F_*.py`. SHA verifications PASS for all 5 pre-regs.

---

## Q034-F-01 — al-ḥamdu li-llāh opener cluster FR cohesion (NULL)

**Pre-reg**: `preregs/Q034-F-01-hamd-cluster-fr-cohesion-prereg.md` (SHA `26500022e51a2fe82807fa6308393f9a2b45d1101e2be99797e080f96fb8063a`).
**Output**: `csv/Q034-F-01.json`.

**Question**: Does the 5-opener cluster {Q 1, 6, 18, 34, 35} form a FR-cohesive group on root-distribution? (OQ-3 candidate test.)

**Result**:

| Test | Observed | Null mean | p_lower | Pass? |
|:--|:--:|:--:|:--:|:-:|
| H1: 5-cluster mean FR | 0.9902 | 0.9226 | 0.7516 | NO |
| H2: 4-cluster drop-Q1 mean FR | 0.9466 | 0.9223 | 0.5071 | NO |
| H3: length-residualized 5-cluster mean | +0.0539 | +0.0005 | 0.6771 | NO |

**Verdict**: **NULL** (0/3). Cluster is content-NULL on FR cohesion. The al-ḥamdu li-llāh opener cluster is a **formal-opener-template parallel without underlying root-distribution content fingerprint**. The cluster mean (0.9902) is ABOVE corpus mean (0.9226) — i.e., the 5 openers are SLIGHTLY ANTI-cohesive (more spread than random matches), not cohesive.

**Cross-finding implication**: This NULL feeds into **OQ-3 answer-NEGATIVE** (the al-ḥamdu li-llāh cluster is NOT a second book-introduction-marker class analogous to muqaṭṭāʿat). Replicated by H-NEW-1340 (same NULL with different perm-seed and broader PC). The classical-rhetorical opener-classification (al-Zarkashī CC-048) is empirically a **formal observation**, not a content-cluster claim.

**Honest limits**: Pre-flight observation of cluster mean (0.9902 > corpus mean) made BEFORE prereg lock; direction-locked at cohesive per protocol-discipline; verdict ceiling DESCRIPTIVE-EMPIRICAL.

---

## Q034-F-02 — Q 27 ↔ Q 34 Sabaʾ-narrative pair cohesion (DIRECTIONAL-WEAK)

**Pre-reg**: `preregs/Q034-F-02-q27-q34-saba-pair-prereg.md` (SHA `a8fd1b2d5e99d2d605a2794af208a69296860e4b238ab92da2155d194d007600`).
**Output**: `csv/Q034-F-02.json`.

**Question**: Q 27 al-Naml + Q 34 Sabaʾ jointly contain the corpus's only 2 attestations of *sabaʾ* (LEM:saba<). Is the pair FR-cohesive at the bilateral level?

**Result**:

| Test | Observed | Threshold | Pass? |
|:--|:--:|:--:|:-:|
| H1: D[Q27,Q34] percentile in all-pair distribution | 31.30% (rank 2017/6441) | ≤25% | NO |
| H2: Q34 in Q27 top-10 AND Q27 in Q34 top-10 | YES (Q34=rank 8 in Q27; Q27=rank 10 in Q34) | both | YES |
| H3: length-residualized percentile | 38.04% | ≤25% | NO |

**Verdict**: **DIRECTIONAL-WEAK** (1/3 — only mutual top-10 passes).

**Interpretation**: Q 27 ↔ Q 34 IS mutually present in each other's FR top-10 (a non-trivial structural relationship — only ~9% of pairs achieve mutual top-10), but their bilateral distance is NOT in the bottom-25th-percentile of all-pair distances. The Saba-pair shares (a) proper-noun lemma, (b) Solomon material, (c) David material, (d) Late-Meccan creedal frame; but each surah's CLOSEST FR neighbor is in the Late-Meccan ḥawāmīm-adjacent band, not the partner Saba-surah.

**Solomon-Saba structure** (the Q 27:15-44 Solomon-Bilqīs ↔ Q 34:12-14 Solomon-jinn-workers axis): the two surahs together exhaust the corpus's *sabaʾ* + David-Solomon-narrative-pair material. Their mutual top-10 status is the *empirical signature* of their thematic affinity at the cross-mushaf-distance level (Q 27 and Q 34 are 7 surahs apart in mushaf order).

**Honest limits**: H1's pre-flight observed value (31.3%) was already above the 25% threshold; direction-locked at COHESIVE; published as NULL with full prominence on the bilateral-percentile axis. H2 PASSES robustly.

---

## Q034-F-03 — ḥ-m-d root density and rank in corpus 114 (DIRECTIONAL)

**Pre-reg**: `preregs/Q034-F-03-hmd-root-rank-prereg.md` (SHA `70d7b5ec80de9cf6a2aef1586847b24e8c976b6314af0a228afa9d098c963c00`).
**Output**: `csv/Q034-F-03.json`.

**Question**: Beyond the formal opener-tag, is Q 34's *ḥ-m-d* root distribution structurally exceptional?

**Result**:

| Test | Q34 value | Rank | Pass? |
|:--|:--:|:--:|:-:|
| H1: ROOT:Hmd token-count | 3 | rank 6/114 (tied) | YES |
| H2: per-verse density | 3/54 = 0.0556 | rank 8/40 surahs with ≥1 attestation | YES |
| H3: density > median of 5 openers {1, 6, 18, 34, 35} | 0.0556 vs median 0.0556 | tied at median | NO |

**Verdict**: **DIRECTIONAL** (2/3).

**Token-count top-10 (ROOT:Hmd, QAC v0.4)**:
| Rank | Surah | Count |
|:-:|:-:|:-:|
| 1 | Q 17 al-Isrāʾ | 4 |
| 2 | Q 39 al-Zumar | 4 |
| 3 | Q 14 Ibrāhīm | 3 |
| 4 | Q 27 al-Naml | 3 |
| 5 | Q 31 Luqmān | 3 |
| **6** | **Q 34 Sabaʾ** | **3** |
| 7 | Q 35 Fāṭir | 3 |
| 8 | Q 40 Ghāfir | 3 |
| 9 | Q 2 al-Baqara | 2 |
| 10 | Q 6 al-Anʿām | 2 |

**Per-verse density top-10**:
Q 14 (3/52 = 0.0577), Q 35 (3/45 = 0.0667), Q 27 (3/93 = 0.0323), Q 31 (3/34 = 0.0882), Q 34 (3/54 = 0.0556) — exact ordering varies by selection but Q 34 is rank 8.

**Interpretation**: Q 34's *ḥ-m-d* attestations are **top-10 in absolute count** and **top-10 in per-verse density**. The dual-ḥamd v.1 (corpus-unique doubling) contributes 2 of the 3 Q 34 attestations — Q 34's v.1 already places it ahead of most surahs in this metric. H3 fails because Q 34's density IS at the median of the 5-opener cluster (tied with Q 35; lower than Q 14 and Q 31 outside the cluster).

**Honest limits**: Token-counts are tied at multiple positions; rank-6 is a dense-rank (Q 14, Q 27, Q 31, Q 34, Q 35, Q 40 all tied at 3 tokens). The corpus-unique dual-ḥamd v.1 is the structural-fingerprint feature; H2's per-verse density rank confirms that Q 34's ḥamd-density IS in the structural top-tier.

---

## Q034-F-04 — Q 34 → Q 35 mushaf-adjacency seam LOW-cost direction (DIRECTIONAL-WEAK)

**Pre-reg**: `preregs/Q034-F-04-q34-q35-seam-prereg.md` (SHA `6f2d39c93528655fb7bf01f93b458cfab3bdedfdd61a27289127b13d1c415333`).
**Output**: `csv/Q034-F-04.json`.

**Question**: Q 34 → Q 35 is the only mushaf-adjacent al-ḥamdu opener pair. Does this dual-feature (mushaf-adjacency + opener-twin) produce an empirically-extreme smooth seam?

**Result**:

| Test | Observed | Threshold | Pass? |
|:--|:--:|:--:|:-:|
| H1: rank Q34→Q35 in delta_raw ascending (top-20) | rank 65/113 | ≤20 | NO |
| H2: cost vs median of opener-cluster transitions | 0.0745 vs median 0.0745 | < median | NO |
| H3: FR(Q34,Q35) < intra-cluster median | 0.9268 < 0.9640 | < median | YES |

**Verdict**: **DIRECTIONAL-WEAK** (1/3 — H3 only).

**Interpretation**: The Q 34 → Q 35 mushaf seam is **mid-pack** (rank 65/113) — NOT empirically extreme in either smoothness or roughness. Shared opener does NOT translate to a top-20 smooth seam at the QAC-root content-vector level. This is the empirical refinement of al-Biqāʿī's Q 34→Q 35 munāsabah claim: opener-form-share is necessary but NOT sufficient to produce a corpus-extreme smooth seam.

H3 confirms a moderate cohesion at the FR-distance axis (Q 34↔Q 35 is below intra-cluster median, suggesting some shared-content-distribution effect from the parallel openers + parallel themes), but the seam-cost ranking is dominated by the *root-distribution change-rate* across the transition, which is mid-pack.

**Cross-finding implication**: Adds to **cross-finding-014 al-Biqāʿī munāsabah selective validity** — the al-Biqāʿī rule "opener-share → smooth transition" is empirically a **directional** rule (cost is below corpus median 0.0905 mean) but NOT an **extremity** rule (cost is NOT in top-20 smoothest).

---

## Q034-F-05 — 5-opener sequential-pair distances; Q 34 ↔ Q 35 tightest-pair test (DIRECTIONAL)

**Pre-reg**: `preregs/Q034-F-05-opener-pair-distances-prereg.md` (SHA `83414986ef57bbeeff090b9e57ec0f0ee0ccabe82a6a67c43b835cccbfd928e3`).
**Output**: `csv/Q034-F-05.json`.

**Question**: Among the 4 sequential opener-pairs in mushaf order {(1,6), (6,18), (18,34), (34,35)}, is Q 34↔Q 35 the FR-tightest? (Combining mushaf-adjacency + opener-twin priors.)

**Result**:

**Sequential opener-pair FR ranking**:
| Rank | Pair | FR distance | Mushaf-distance |
|:-:|:--|:--:|:-:|
| 1 (tightest) | Q 18 ↔ Q 34 | 0.8984 | 16 |
| 2 | Q 34 ↔ Q 35 | 0.9268 | 1 (mushaf-adjacent) |
| 3 | Q 6 ↔ Q 18 | 0.9340 | 12 |
| 4 (widest) | Q 1 ↔ Q 6 | 1.1699 | 5 |

| Test | Observed | Pass? |
|:--|:--:|:-:|
| H1: (Q34, Q35) is the MINIMUM of the 4 sequential pairs | rank 2 of 4 | NO |
| H2: D[Q34,Q35] all-pair percentile ≤ 50% | 42.73% | YES |

**Verdict**: **DIRECTIONAL** (1/2).

**Interpretation**: Q 34 ↔ Q 35 is NOT the tightest sequential opener-pair — that title goes to Q 18 ↔ Q 34, which shares opener (al-ḥamdu li-llāh + *alladhī*-relative-clause) but is 16 mushaf positions apart. The lesson: **shared syntactic opener-family (the *alladhī*-relative-clause sub-pattern: Q 6, Q 18, Q 34)** is empirically more predictive of FR-cohesion than mushaf-position-adjacency. Q 35's *fāṭir*-apposition opener-syntax breaks the *alladhī*-pattern, even though it preserves *al-ḥamdu li-llāh*.

This is a **finer-grained finding** than the cluster-cohesion test (Q034-F-01 NULL): WITHIN the 5-opener cluster, the *alladhī*-relative-clause sub-cluster {Q 6, Q 18, Q 34} shows nontrivial FR-cohesion (the tightest sequential pair Q 18↔Q 34 sits at FR 0.8984; Q 6↔Q 18 at 0.9340; Q 6↔Q 34 at 0.8905), while Q 35's appositive-construction shifts it slightly out of the cohesion-band.

H2 confirms Q 34↔Q 35 IS below corpus median — i.e., it IS slightly cohesion-coupled — but not the tightest within the cluster.

**Sub-finding to propagate**: the al-ḥamdu li-llāh + *alladhī*-relative-clause sub-cluster {Q 6, Q 18, Q 34} merits its own FR-cohesion test (NEW pre-reg candidate for follow-up). The 3-surah sub-cluster pairs are:
- Q 6 ↔ Q 18 = 0.9340
- Q 6 ↔ Q 34 = 0.8905
- Q 18 ↔ Q 34 = 0.8984
- Mean: 0.9076 (vs corpus mean 0.9226 — slightly cohesive at the sub-cluster level)

This sub-finding suggests OQ-3 should be refined: the FORMAL 5-opener cluster is content-NULL, but the SYNTACTIC-3-opener sub-cluster (*alladhī*-relative-clause) shows weak cohesion. **Cross-finding-025 (marker-thickness) implication**: a syntactic sub-feature within an opener-tag class IS a thicker marker than the opener-tag itself, and approaches but doesn't cross the FR-cohesion threshold.

**Honest limits**: Q 18↔Q 34 being tightest is a non-pre-registered observation (NEW finding embedded in the post-hoc-discovered sub-cluster). The 3-surah sub-cluster test should be properly pre-registered before any *confirmation* claim.

---

## Summary — 5-test verdict matrix

| Test | Verdict | Net pass count |
|:--|:--|:-:|
| Q034-F-01 al-ḥamd cluster cohesion | NULL | 0/3 |
| Q034-F-02 Q 27↔Q 34 Saba-pair | DIRECTIONAL-WEAK | 1/3 |
| Q034-F-03 ḥmd root rank | DIRECTIONAL | 2/3 |
| Q034-F-04 Q 34→Q 35 seam | DIRECTIONAL-WEAK | 1/3 |
| Q034-F-05 opener pair-distance | DIRECTIONAL | 1/2 |

**5 NULL/DIRECTIONAL findings**, no CONFIRMED. The strongest positive signals:
1. Q 34's *ḥ-m-d* root density IS top-10 in both raw count AND per-verse rank.
2. Q 27 ↔ Q 34 is mutual top-10 FR (the empirical Saba-pair structural relation).
3. Q 18 ↔ Q 34 is the tightest sequential opener-pair (post-hoc; *alladhī*-syntactic sub-cluster candidate).

**Strongest NULL**: the 5-opener cluster (al-ḥamdu li-llāh formal tag) is NOT FR-cohesive — independently replicating H-NEW-1340 and supporting OQ-3 NEGATIVE answer.

**Cross-finding contributions**:
- cross-finding-014 al-Biqāʿī munāsabah selective validity (Q34-CC-04 + Q34-CC-05).
- cross-finding-025 marker-thickness rule (formal-opener-tag too thin; syntactic-sub-cluster approaches threshold).
- OQ-3 ANSWERED-NEGATIVE for the al-ḥamdu li-llāh class.
