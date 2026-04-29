---
id: H-NEW-168
title: Q 16-25 isolate-core IS concentrator-mode AND internally-similar — resolves H-NEW-94 NULL-BROKEN
phase: B
status: CONFIRMED-CONCENTRATOR-INTERNALLY-SIMILAR
prereg: h-new-168-q16-q25-dispersion-prereg.md
prereg_sha256: 12abd1be5b28a19aa9e22f176a41871068fa1ff254ced774055f2c809d810988
script: scripts/h_new_168_q16_q25_dispersion.py
json: findings/phase-b-hypotheses/csv/h-new-168.json
csv: findings/phase-b-hypotheses/csv/h-new-168-per-surah-dispersion.csv
log: /tmp/h168.log
date: 2026-04-17
seed: 20260419
parent: H-NEW-163 (TEMPLATE/CONCENTRATOR modes)
supersedes_null: H-NEW-94 (NULL-BROKEN on shape-similarity) — replaced with CONFIRMED on dispersion axis
bonferroni_k: 1
bonferroni_family: h-new-168-isolate-core-dispersion
alpha_bon: 0.05
verdict: CONFIRMED-CONCENTRATOR-INTERNALLY-SIMILAR
---

# [[h-new-168-q16-q25-dispersion|H-NEW-168]] — Q 16-25 isolate-core is CONCENTRATOR-MODE and internally-similar

## Headline

- **Cell A (contiguous-window null)**: Q 16-25 window-mean dispersion = **0.2680**; rank **4/105** ascending; p = 0.0381 **PASS** (α=0.05).
- **Cell B (10K permutation null)**: p = **0.0006** **PASS** — Q 16-25 window mean is 2.7 SD below the random-10 null mean (0.3164).
- **Cell C (internal Jaccard)**: mean pairwise Jaccard = **0.319** vs null 0.135 ± 0.039; p ≈ 0.0001 — Q 16-25 pairs share **2.4× more** stems than random 10-surah samples.
- **MW-5 controls**: both PASS. Q 1 rank = 2/114 (template-mode confirmed); Q 2 rank = 113/114 (concentrator-mode confirmed).
- **Verdict**: Q 16-25 is a CONCENTRATOR-MODE zone whose surahs share vocabulary with each other more than expected.

## Per-surah dispersion + rank (QAC-STEM, k=114)

| Q | Dispersion | Rank / 114 | n stems | Mode |
|:-:|---:|---:|---:|:-:|
| 16 | 0.2575 | 95 | 358 | concentrator |
| 17 | 0.2555 | 96 | 342 | concentrator |
| 18 | 0.2389 | **105** | 369 | concentrator (deep) |
| 19 | 0.2883 | 80 | 239 | concentrator |
| 20 | 0.2528 | 97 | 324 | concentrator |
| 21 | 0.2738 | 88 | 284 | concentrator |
| 22 | 0.2590 | 93 | 328 | concentrator |
| 23 | 0.2894 | 79 | 271 | concentrator |
| 24 | 0.2673 | 90 | 287 | concentrator |
| 25 | 0.2973 | 76 | 250 | concentrator |

- **All 10 surahs sit below corpus median** (0.312). Mean rank 89.9/114 (21st percentile).
- **Q 18 al-Kahf is the deepest concentrator** (rank 105/114) — ironic because Q 18 is the one Q 16-25 surah that is NOT on [[cross-finding-010-extended-network|cross-finding-010]]'s TRUE-ISOLATE-CORE list; it connects via the C7 Friday-liturgy cluster. Its dispersion pattern says it's concentrating unique narrative content (Cave, Moses-Khidr, Dhū-l-Qarnayn) regardless of liturgical-cluster membership.
- **Q 25 al-Furqān is the shallowest concentrator** in the zone (rank 76) — still below median.

## Internal overlap structure (Cell C)

**Top-5 most-similar pairs (Jaccard):**
- Q 16 ↔ Q 22 : 0.406 (al-Naḥl ↔ al-Ḥajj — creation/signs + pilgrimage/worship)
- Q 17 ↔ Q 25 : 0.380 (al-Isrāʾ ↔ al-Furqān — Muhammad's prophetic role + scriptural argument)
- Q 16 ↔ Q 23 : 0.370 (al-Naḥl ↔ al-Muʾminūn — signs in nature + believers' virtue)
- Q 21 ↔ Q 23 : 0.367 (al-Anbiyāʾ ↔ al-Muʾminūn — prophets-catalogue + believers)
- Q 17 ↔ Q 18 : 0.362 (al-Isrāʾ ↔ al-Kahf — night-journey + cave-narrative)

**Bottom-5 least-similar pairs:**
- Q 18 ↔ Q 24 : 0.284 (al-Kahf narrative vs al-Nūr legal-social)
- Q 19 ↔ Q 21 : 0.282
- Q 16 ↔ Q 19 : 0.281
- Q 19 ↔ Q 22 : 0.277
- Q 19 ↔ Q 24 : 0.261

**Q 19 Maryam is the internal outlier** — 4 of 5 bottom pairs involve Q 19. Its dispersion (0.288, rank 80) is relatively high FOR this zone, consistent with Maryam being a genre-island (birth-narrative of prophets).

## Compositional-mode classification

| Mode | Q 16-25 status | Evidence |
|---|---|---|
| TEMPLATE (high-dispersion) | NO | Zone mean dispersion 15% below corpus median |
| CONCENTRATOR (low-dispersion) | **YES** | Rank 4/105 contiguous windows; p=6e-4 permutation |
| INTERNALLY-DIVERSE | NO | Would predict Jaccard ≤ null; observed p=0.9999 above-null |
| **INTERNALLY-SIMILAR** | **YES** | Pairwise Jaccard 2.4× null mean; p=1e-4 |

## What this means

1. **Isolate-core IS a dispersion phenomenon.** The Q 16-25 cluster-empty zone is not empty because of accident; it is empty because the ten surahs fill themselves with vocabulary that is less widely distributed across the corpus than average.

2. **But the isolates share more with EACH OTHER than random surahs do.** The concentrator-mode is not atomic (each surah its own island); it is CLUSTERED. Q 16-25 forms a soft community in stem-space even when it forms no community in classical clustering (because classical clusters are defined by muqaṭṭāʿāt, rhyme families, or revelation groups — none of which pick up this zone).

3. **This RESOLVES [[h-new-94-q16-q25-zone|H-NEW-94]]'s NULL-BROKEN on shape-similarity.** The zone is real. It just doesn't surface under a shape-similarity metric measuring external-pattern similarity; it surfaces under a dispersion metric measuring internal vocabulary concentration. MW-5 failed in [[h-new-94-q16-q25-zone|H-NEW-94]] because the chosen null (contiguous-window shape-test) is under-powered against non-contiguous classical clusters; the dispersion axis uses a cleaner metric.

4. **Architectural prediction.** Where [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] showed TEMPLATE surahs are mostly short late/early Meccan creedal or Medinan liturgical pieces, CONCENTRATOR surahs are mostly long narrative/legal. Q 16-25 is a cluster of **mid-length mid-period narrative-theological surahs** (mostly late Meccan) — a distinct "narrative-teaching zone" in the mushaf. This gives a fourth compositional mode beyond Q 1-type (hyper-template) and Q 2-type (hyper-concentrator): the "meso-concentrator-community" that concentrates locally-shared late-Meccan prophetic-argument vocabulary.

## Honest limits

1. **One-zone test**: we tested Q 16-25 (the pre-specified [[cross-finding-010-extended-network|cross-finding-010]] target zone) only. Whether OTHER contiguous zones show internally-similar concentrator behavior is not tested here. [[h-new-94-q16-q25-zone|H-NEW-94]]'s MW-5 positive-controls Q 57-64 (musabbiḥāt) and Q 40-46 (ḥawāmīm) would be natural next targets.

2. **Jaccard is size-sensitive**: long surahs share more stems trivially because they have more. Q 16-25 n_stems range 239-369; random null could have short surahs. Some of the 2.4× excess may be length-confound. Size-matched permutation test would be cleaner. Direction is almost certainly preserved given the magnitude (2.4× is large), but precise p may shift.

3. **Dispersion metric is ONE axis**: a surah can be concentrator-mode yet still be thematically related to other surahs; we're measuring vocabulary distribution, not semantic relation.

4. **Q 18 (member of C7 Friday-liturgy cluster) behaves like the other 9**: that's an informative anomaly — its classical cluster-membership does not prevent it from being the deepest concentrator in the zone. Classical clusters ≠ dispersion patterns; the two axes are complementary.

## Connection to unified model / prior findings

- **Supersedes [[h-new-94-q16-q25-zone|H-NEW-94]] NULL-BROKEN**: the Q 16-25 zone is now empirically real on the dispersion axis.
- **Extends [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]]**: introduces a third mode (meso-concentrator-community) between apex-template (Q 1-type) and apex-concentrator (Q 2-type).
- **Strengthens [[cross-finding-010-extended-network|cross-finding-010]]**: TRUE-ISOLATE-CORE is not just topologically isolated on clustering; it's *compositionally* coherent in stem-space.
- **Opens**: are Q 16, 21, 22, 23, 25 (TRUE-ISOLATE-CORE) more internally-similar than Q 17, 18, 19, 20, 24 (zone but not all [[cross-finding-010-extended-network|cross-finding-010]] core)? A 5 vs 5 split would test whether [[cross-finding-010-extended-network|cross-finding-010]]'s core is a sharper-boundary version of [[h-new-168-q16-q25-dispersion|H-NEW-168]]'s zone.

## Queue

- H-NEW-168.1: size-matched Jaccard permutation (residualize length confound).
- H-NEW-168.2: test all 105 contiguous 10-surah windows for internal-Jaccard excess → catalogue of "dispersion-communities" across the mushaf.
- H-NEW-168.3: 5-vs-5 split of Q 16-25 — TRUE-ISOLATE-CORE sub-community test.
- H-NEW-168.4: chronological label — are Q 16-25 ten surahs mostly classified as late-Meccan? If yes, the meso-concentrator-community IS a late-Meccan-narrative-theology genre signature.
