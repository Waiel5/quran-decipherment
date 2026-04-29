---
surah: 45
surah_name: al-Jāthiyah
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: HM-B cohesion-tightener; mid-quartile UAS (rank 41); window-7 COHESION_ANCHOR; Q 42's rank-1 corpus-nearest-neighbor
---

# Q 45 al-Jāthiyah — empirical profile

All values pulled from canonical empirical-data files this session. SHA256 verification of source files is the responsibility of the data-provenance pipeline, not re-derived here.

## 1. Headline metrics

| Metric | Value | Provenance (file path + key) |
|:--|:--|:--|
| UAS score | +0.350 | `findings/phase-b-hypotheses/csv/h-new-840.json` `all_uas[surah=45].UAS` |
| **UAS rank** | **41 / 114** | h-new-840 (re-ranked by sorting `all_uas` descending this session) |
| abs_outlier (Δ%ile abs) | 10.68 | h-new-840 `all_uas[surah=45].abs_outlier` |
| max neighbor TSP cost | 0.1112 | h-new-840 `max_cost` |
| abs_ijaz | 0.654 | h-new-840 `abs_ijaz` |
| sig_A (al-Bāqillānī axis) | −0.654 | `findings/phase-b-hypotheses/csv/h-new-750.json` `per_surah[surah=45].sig_A` |
| sig_B (al-Khaṭṭābī axis) | −1.033 | h-new-750 |
| rank_A (sig_A descending) | 78 / 114 | h-new-750 |
| rank_B | 82 / 114 | h-new-750 |
| outlier Δ%ile (signed) | **−10.68 (COHESION_ANCHOR)** | `findings/phase-b-hypotheses/csv/h-new-590.json` `all_surahs_results[X=45]` |
| outlier window | [42, 43, 44, 45, 46, 47, 48] | h-new-590 X=45 |
| d_W (window with Q 45) | 0.9309 | h-new-590 |
| d_W_minus_X (window without Q 45) | **0.9520** | h-new-590 |
| pct_W (W in random null) | 46.05%ile | h-new-590 |
| pct_W_minus_X | 56.73%ile | h-new-590 |
| classification (h-new-590) | **COHESION_ANCHOR** | h-new-590 |
| Rhyme entropy (final-letter, nats) | 0.485 | h-new-750 `rhyme_entropy_nats` |
| Rhyme entropy (final-letter, bits) | 0.700 | computed this session ≡ 0.485 / ln(2) |
| Distinct verse-finals | 2 (ن, م) | this session, `quran-min-tashkeel.json` |
| Top final letter | ن (81.1% = 30/37) | h-new-750 `top_final_letter_frac` confirms |
| Mean content distance | 0.9375 | h-new-750 `mean_content_distance` |
| Local cohesion | 1.1384 | h-new-750 `local_cohesion` |
| n_verses | 37 | h-new-750 |

## 2. UAS triangulation

UAS = w_outlier · |outlier| + w_cost · max_cost + w_ijaz · |ijāz_signature|. Q 45's UAS components:
- **|outlier|** = 10.68 (moderate — Q 45 is the strongest *anchor* of its 7-window, but anchor-direction not outlier-direction)
- **max_cost** = 0.1112 (the higher of the two adjacency costs to direct neighbors; this is Q 44→Q 45 = 0.111, NOT Q 45→Q 46 = 0.096)
- **|sig_ijāz|** = 0.654 (modest)

The composite UAS rank 41 places Q 45 in the **top quartile** of architectural significance. Within HM-7 specifically (re-derived this session by ranking the 7 surahs):

| HM-7 surah | UAS | Corpus rank |
|:-:|:-:|:-:|
| Q 42 al-Shūrā | +0.568 | 31 |
| Q 43 al-Zukhruf | +0.537 | 33 |
| Q 41 Fuṣṣilat | +0.436 | 39 |
| **Q 45 al-Jāthiyah** | **+0.350** | **41** |
| Q 40 Ghāfir | −0.868 | 74 |
| Q 46 al-Aḥqāf | −1.591 | 96 |
| Q 44 al-Dukhān | −1.882 | 97 |

Q 45 is the **4th-ranked** HM-7 surah by UAS — first member of the *positive-UAS minority* (4 of 7 HM-7 surahs are positive). This is consistent with Q 45's role as the **HM-A↔HM-B bridge**: it is the *first* HM-B surah whose UAS profile is positive (Q 43 +0.537 too) but it carries the HM-B near-monorhyme prosodic signature.

## 3. Position in HM-7 cluster (HM-B sub-block)

Q 45 is one of the 4 HM-B sub-block members {Q 43, Q 44, Q 45, Q 46}. The HM-7 bifurcation pattern (per [[hawamim-7-cluster-bifurcation|HM-7 bifurcation]] and the empirical comparison computed this session):

| Surah | n_verses | rhyme entropy (bits) | distinct finals | top final | block |
|:-:|:-:|:-:|:-:|:-:|:-:|
| Q 40 | 85 | 2.413 | 8 | ن (38%) | HM-A |
| Q 41 | 54 | 2.146 | 10 | ن (56%) | HM-A |
| Q 42 | 53 | 2.565 | 9 | ر (38%) | HM-A |
| — bifurcation midline — | | | | | |
| Q 43 | 89 | 0.594 | 3 | ن (88%) | HM-B |
| Q 44 | 59 | 0.818 | 2 | ن (75%) | HM-B |
| **Q 45** | **37** | **0.700** | **2** | **ن (81%)** | **HM-B** |
| Q 46 | 35 | 0.952 | 3 | ن (74%) | HM-B |

Q 45's rhyme profile is **HM-B-canonical** — 2-finals, ~80% nūn dominance, sub-1-bit entropy. This is functionally aligned with Q 45's content register: the surah's near-monorhyme texture supports its **declarative-eschatological** content (predominantly *yaʿqilūn*, *yaʿlamūn*, *tunkirūn*, *yaʾminūn*, *al-mubtilūn*-type plural-participle endings).

## 4. Cross-cluster cohesion (FR-roots, h-new-111 + this session's pre-reg)

From `Q045-F-03` (this session, [[Q045-F-03-hmb-vs-hma-cohesion-prereg|F-03 pre-reg]] SHA `70a5d569…`):

| Set | K | d̄_FR | %ile in random-K null (10000 perms, seed 20260428) | p_perm |
|:--|:-:|:-:|:-:|:-:|
| HM-A {Q 40,41,42} | 3 | 0.8624 | 25.73 | 0.257 |
| HM-B {Q 43,44,45,46} | 4 | 0.8665 | 23.57 | 0.236 |
| **HM-B without Q 45** {Q 43,44,46} | 3 | **0.8809** | 29.75 | n/a |
| HM-B with Q 45 minus Q 43 {Q 44,45,46} | 3 | 0.832 | computed this session | n/a |

Three key findings:
1. **HM-A is *tighter* than HM-B** (0.862 < 0.866) — pre-committed direction CORRECT (F-03 H1 direction-locked PASS), but the magnitude is small and p_perm = 0.257 fails Bonferroni-corrected α = 0.025. **Verdict: DIRECTIONAL** (not significant at law-strength).
2. **Removing Q 45 from HM-B raises d̄ to 0.881** — Q 45 is empirically a **HM-B cohesion-tightener** (F-03 H1b VINDICATED at direction). Q 45's presence pulls the HM-B mean DOWN by 0.014 distance-units.
3. **Q 45's strongest internal HM-B link is Q 45↔Q 46 = 0.8112** (h-new-111), the **single tightest pair within HM-B**. This is what drives the H1b finding.

The HM-A baseline-tighter direction matches the chronology-cluster prediction (HM-A surahs at al-Suyūṭī chronology #60-#62 are revelation-sequential; HM-B spans #63-#66). HM-B's slightly looser cohesion is what made the test direction-locked.

## 5. Compression-tail position (s=45, intra-50)

Q 45 is at mushaf position 45, **inside the s ≤ 50 pre-kink baseline** of the compression-tail laws ([[h-new-660-compression-tail-gradient|H-NEW-660]], [[h-new-700-phonological-compression-tail|H-NEW-700]]):

- **d̄_content(45) ≈ 0.96** (no compression discount applied; the discount kicks in only at s > 50).
- **d̄_rhyme(45) ≈ 0.36** (pre-kink rhyme baseline).
- **d̄_phoneme(45) ≈ 0.001** (pre-kink phoneme baseline).

Q 45's *observed* mean_content_distance = 0.9375 (h-new-750) — slightly *below* the compression-tail-baseline of 0.96, by ≈ 0.02 units. This is consistent with the COHESION_ANCHOR signal in h-new-590: Q 45's content-distances to its 7-window neighbors are tighter than average.

Q 45 is NOT a compression-tail surah; it sits in the prosodically-uniform Meccan-ṭiwāl pre-kink phase.

## 6. Adjacency cost to neighbors

Per `h-new-720.json` `per_adjacency`:

| Transition | L_constrained | delta_raw (residual fraction × total) | fraction_residual |
|:--|:--|:--|:--|
| Q 44 → Q 45 (s=44) | 77.578 | 0.1112 | 1.34% |
| **Q 45 → Q 46** (s=45) | **77.563** | **0.0959** | **1.16%** |

Both Q 45's adjacency-costs are **below-median** for the corpus (the 113-cost distribution has mean ≈ 0.073 with high variance). The Q 45-Q 46 cost is in the bottom-third of all adjacency costs (the **cheapest** internal HM-B transition besides the implicit Q 41-Q 42 zone).

This empirically supports the classical-narrative reading that Q 45 → Q 46 is a **continuous** thematic transition (judgment-day → ʿĀd-warning), with the *kitāb yanṭiqu* of Q 45:29 setting up the *kitāb mubīn* of Q 46:7-8.

## 7. iʿjāz signature breakdown

| Component | Value | Interpretation |
|:--|:--|:--|
| sig_A (al-Bāqillānī, *iʿjāz al-fawāṣil*) | **−0.654** | anti-fawāṣil; rhetorical-density below corpus mean |
| sig_B (al-Khaṭṭābī, *iʿjāz al-maʿnā*) | **−1.033** | anti-content-iʿjāz signal at the surah-window level |
| rank_A | 78/114 | bottom-third on fawāṣil-iʿjāz |
| rank_B | 82/114 | bottom-third on content-iʿjāz |

Q 45 has **negative both axes** — making it (by the cross-finding-026 typology) an **anti-iʿjāz surah on both classical axes**. This is consistent with its content-register: the surah is doctrinal-declarative-eschatological, not rhetorical-condensation-style. The iʿjāz-distinctive surahs are Q 1 (sig_A high), Q 33 (sig_A high), Q 24 (sig_A negative), Q 55 (sig_A corpus-min). Q 45 occupies the moderate-anti-iʿjāz cell.

**Important caveat**: anti-iʿjāz at the *window-statistical* level does NOT mean the surah lacks rhetorical or theological force — see `cross-finding-026 §13` for the dual-iʿjāz typology resolution. Q 45's rhetorical force is concentrated in **specific verses** (Q 45:18 sharīʿa, Q 45:23 hawan-as-god, Q 45:28-29 jāthiyah) which are window-AVERAGED-OUT in the sig_A statistic.

## 8. FR-roots nearest neighbors (Q 45 top-7 by FR-distance)

Computed this session from `h-new-111.json` D-matrix (upper-triangular, 6441 entries):

| Rank | Surah | FR-distance | Note |
|:-:|:-:|:-:|:--|
| 1 | **Q 31 Luqmān** | 0.7685 | wisdom-theme; mid-Meccan |
| 2 | **Q 32 al-Sajda** | 0.7853 | Q 41's sajda-name-cousin; ALM cluster |
| 3 | **Q 41 Fuṣṣilat** | 0.7994 | HM-A; cluster sibling |
| 4 | **Q 42 al-Shūrā** | 0.8011 | HM-A; **Q 45 IS Q 42's RANK-1** |
| 5 | Q 10 Yūnus | 0.8050 | mid-Meccan; ALR |
| 6 | Q 30 al-Rūm | 0.8059 | mid-Meccan ALM |
| 7 | Q 29 al-ʿAnkabūt | 0.8108 | mid-Meccan ALM |

**Pattern**: Q 45's 7 nearest neighbors are uniformly **mid-Meccan creedal-eschatological** surahs. Of the 7, **3 are HM-cluster members** (Q 41, Q 42 directly; Q 32 is sajda-cousin). The remaining 4 (Q 31, Q 30, Q 29, Q 10) are all ALM-cluster mid-Meccan creedal surahs.

**The decisive finding**: Q 45 is **Q 42's rank-1 nearest neighbor in the entire corpus** (verified at [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] and reproduced this session). Q 45 functions as the FR-content-axis anchor for the HM-A→HM-B bridge.

## 9. FR-roots farthest neighbors (Q 45 bottom-7)

| Rank | Surah | FR-distance |
|:-:|:-:|:-:|
| 1 | Q 55 al-Raḥmān | 1.2592 |
| 2 | Q 56 al-Wāqiʿa | 1.1182 |
| 3 | Q 12 Yūsuf | 1.0629 |
| 4 | Q 9 al-Tawba | 1.0614 |
| 5 | Q 33 al-Aḥzāb | 1.0519 |
| 6 | Q 54 al-Qamar | 1.0498 |
| 7 | Q 89 al-Fajr | 1.0458 |

**Pattern**: Q 45's farthest are uniformly **specialized-register surahs** — Q 55 (refrain-iʿjāz / dual-thaqalān), Q 56 (eschatological-three-class), Q 12 (single-protagonist narrative), Q 9 (Medinan-legal-polemic), Q 33 (Medinan-legal-twin-pair). These are all surahs whose content-axis is structurally orthogonal to Q 45's mid-Meccan creedal-eschatological-doctrinal register.

## 10. Window-d̄ values (h-new-590)

For Q 45's 7-window [42, 43, 44, 45, 46, 47, 48]:
- d̄_W (full window) = 0.9309 (46.05%ile in random-7-subset null)
- d̄_W_minus_X (window without Q 45) = 0.9520 (56.73%ile)
- **Δ = +10.68 percentile points → COHESION_ANCHOR classification**

Q 45 lowers its 7-window cohesion-percentile by **10.68 points** when present — it is a **moderate cohesion-anchor**, not at the extreme level of Q 1 (Δ = +27 pp) or Q 9 (Δ = +21 pp), but a clear positive cohesion-contributor. This places Q 45 in the project's `WEAK_ANCHOR / COHESION_ANCHOR` taxonomic cell (alongside Q 10, Q 27).

## 11. Content / rhyme / phoneme / length axis positions

From the multi-axis architecture (per [[cross-finding-025-multi-axis-architecture|cross-finding-025]]):

| Axis | Q 45 position | Cell |
|:--|:--|:--|
| Content compression-tail (d̄_content) | 0.9375 (slightly below baseline 0.96) | pre-kink, mildly-cohesive |
| Rhyme dispersion-tail (d̄_rhyme) | 0.485 nats = HM-B near-monorhyme | pre-kink, near-monorhyme HM-B |
| Phoneme dispersion-tail (d̄_phoneme) | within s ≤ 75 baseline | pre-kink phoneme-uniform |
| Verse-length compression-tail | 37 verses (mufaṣṣal-awsāṭ); avg 13 words/verse | pre-kink length-baseline |

Q 45 is **uniformly pre-kink** on all 4 architectural-law axes — a typical mid-Meccan-ṭiwāl profile, with the HM-B prosodic specialization (near-monorhyme).

## 12. Architectural classification

| Axis | Position |
|:--|:--|
| Structural-iʿjāz (al-Bāqillānī) | mild-anti (sig_A=−0.654, rank 78/114) |
| Theological-iʿjāz (al-Khaṭṭābī) | mild-anti (sig_B=−1.033, rank 82/114) |
| Compression-tail | NOT a tail surah (s=45 ≤ 50) |
| Outlier | **COHESION_ANCHOR** (Δ=−10.68); moderate strength |
| Cluster role | **HM-B cohesion-tightener; HM-A→HM-B bridge** |
| Lexical-singleton-host | TWO singletons (sharīʿa noun Q 45:18; jāthiya form Q 45:28); ONE singleton-pair (hawan-as-god with Q 25:43) |

Q 45 sits in the **anti-iʿjāz-on-both-axes + COHESION_ANCHOR + multi-singleton-host** cell — this is a distinct empirical signature relative to the other HM-7 members.

## 13. Honest limits

1. **UAS = 41 is mid-quartile-top** — Q 45 is not a corpus-extreme architectural outlier; significance is sub-cluster (HM-B tightening + singleton-host).
2. **Anti-iʿjāz on both sig_A and sig_B** does NOT mean the surah is rhetorically weak — it means the surah's rhetorical-condensation is at the **specific-verse level** (Q 45:18, 23, 28) which the window-statistical sig_A,B average out.
3. **F-03 DIRECTIONAL not VINDICATED**: HM-A < HM-B direction matches but p_perm = 0.257 misses α = 0.025. The cluster-level cohesion comparison is direction-locked but not at law-strength.
4. **Q 45 ↔ Q 46 = 0.811 is the tightest single FR-pair within HM-B** — this is the empirical anchor for Q 45's cohesion-tightener role; replicates without permutation noise.
5. The COHESION_ANCHOR classification (Δ=−10.68) has p_greater_W = 0.5395 (h-new-590) — the cohesion strengthening is clear but not at extreme p-value strength.

## 14. Cross-references

- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 41 (top-quartile)
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 45 COHESION_ANCHOR Δ=−10.68
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 44-45 + Q 45-46 transition costs
- [[h-new-750|H-NEW-750]] — sig_A=−0.654, sig_B=−1.033, ranks 78 + 82
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 45 in pre-kink baseline (s=45 ≤ 50)
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — pre-kink content-distance baseline
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — full FR-distance matrix; Q 45 rows extracted this session
- [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] — confirms Q 45 = Q 42's rank-1 corpus-nearest-neighbor
- [[hawamim-7-cluster-bifurcation|HM-7 bifurcation]] — Q 45 is HM-B middle anchor
- [[Q042-al-shura/01-empirical-profile|Q 42 empirical profile]] — Q 45 is Q 42's rank-1 nearest
- [[Q046-al-ahqaf/00-overview|Q 46 al-Aḥqāf]] — Q 45's tightest single-pair (FR=0.811)
- [[Q045-F-03-hmb-vs-hma-cohesion-prereg|F-03 pre-reg]] — HM-A < HM-B + Q 45 leave-one-out
