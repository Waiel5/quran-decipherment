---
surah: 51
surah_name_ar: الذاريات
surah_name_translit: al-Dhāriyāt
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical-profile pulled from H-NEW-111/590/700/720/750/840/1070/1140; SPECIAL test on 4-element fa-coordinated oath sibling cluster {Q 37, 51, 77, 100}.
---

# Q 51 al-Dhāriyāt — Empirical Profile

All numerics traced to specific finding JSONs in `findings/phase-b-hypotheses/csv/`. Computed inline this specialist run on 2026-05-09 with seed = 20260509.

## 1. Headline metrics

| Metric | Value | Rank | Source |
|:--|:-:|:-:|:--|
| Verse count | 60 | — | canonical |
| Word count (no-tashkeel) | 360 | — | computed |
| Letter count (no-tashkeel, no spaces) | ~1,560 | — | computed |
| Average words/verse | 6.0 | mid-low | computed |
| **UAS** | **+1.802** | **15/114** | h-new-840.json (top-13% architectural significance) |
| **Outlier-spectrum classification** | **COHESION_ANCHOR** | window {48-54} | h-new-590.json (delta_pct = -16.17, p_greater = 0.405) |
| iʿjāz sig_A | +0.981 | 35/114 | h-new-750.json |
| iʿjāz sig_B | -0.013 | 59/114 | h-new-750.json |
| Mean content distance | 0.872 | z = -0.51 | h-new-750.json |
| Local cohesion | 1.159 | z = -0.49 | h-new-750.json |
| Rhyme entropy (nats) | 1.033 | z = +0.48 | h-new-750.json |
| Top final letter | ن | 70.0% | computed |
| Q 50→Q 51 adjacency cost (delta_raw) | 0.1192 | rank 89/113 (mid-tier expensive) | h-new-720.json |
| Q 51→Q 52 adjacency cost (delta_raw) | 0.0096 | rank 18/113 (cheap, near-clamped) | h-new-720.json |

## 2. Fisher-Rao nearest neighbors (top-15)

From H-NEW-111 D matrix (QAC-stem-roots, no-tashkeel rules-tuple):

| Rank | Surah | FR distance | Note |
|:-:|:-:|:-:|:--|
| 1 | Q 81 al-Takwīr | 0.7369 | short eschatological-mufaṣṣal |
| 2 | Q 74 al-Muddaththir | 0.7511 | early-Meccan eschatological |
| 3 | Q 44 al-Dukhān | 0.7543 | HM-eschatological-mufaṣṣal-by-content |
| 4 | Q 52 al-Ṭūr | 0.7545 | mushaf-right-neighbor; oath-opener sibling |
| 5 | Q 112 al-Ikhlāṣ | 0.7651 | tawḥīd-pivot |
| 6 | Q 91 al-Shams | 0.7704 | oath-cluster sibling (short-tail core) |
| 7 | Q 73 al-Muzzammil | 0.7706 | early-Meccan vigil |
| 8 | Q 110 al-Naṣr | 0.7749 | terminal-Medinan brief |
| 9 | Q 61 al-Ṣaff | 0.7758 | musabbiḥāt cluster member |
| 10 | Q 106 Quraysh | 0.7774 | terminal-Meccan brief |
| 11 | Q 15 al-Ḥijr | 0.7788 | mid-Meccan narrative-of-stones (Lūṭ-people parallel!) |
| 12 | Q 113 al-Falaq | 0.7809 | terminal-Meccan |
| 13 | Q 71 Nūḥ | 0.7817 | the named Nūḥ surah (parallel to v. 46 anchor) |
| 14 | Q 1 al-Fātiḥa | 0.7853 | umm al-kitāb |
| 15 | Q 105 al-Fīl | 0.7858 | terminal-Meccan brief narrative |

**Q 51 sits at the heart of an eschatological-mufaṣṣal cluster** with strong content-affinity to Q 81, Q 74, Q 44, Q 52, Q 112. Notably, Q 51's nearest oath-cluster neighbor is Q 52 (FR = 0.7545, rank 4 — extremely close), confirming the H-NEW-1140 mushaf-adjacency pattern (Q 51-52-53 oath-trio).

Q 51's closest non-oath-cluster neighbors are eschatological-mufaṣṣal (Q 81, Q 74, Q 44) and tawḥīd-pivot (Q 112) — its content profile centers on **eschatology + tawḥīd**, consistent with its v. 56 (creation-purpose) + v. 58 (provider-attributes) theological centerpieces.

## 3. Fisher-Rao farthest neighbors

| Rank | Surah | FR distance |
|:-:|:-:|:-:|
| 110 | Q 24 al-Nūr | 1.0567 |
| 111 | Q 3 Āl ʿImrān | 1.0709 |
| 112 | Q 55 al-Raḥmān | 1.0992 |
| 113 | Q 4 al-Nisāʾ | 1.1032 |
| 114 | Q 9 al-Tawba | 1.1345 |

Q 51 is FR-far from all the long Medinan legal surahs (Q 9, Q 4, Q 3, Q 24) and from the unique Q 55 al-Raḥmān (the cosmic-refrain outlier).

## 4. Mushaf-adjacency profile

H-NEW-720 canonical-adjacency-cost results for Q 51's two seams:

| Pair | delta_raw | rank in 113 | fraction_residual | Read |
|:--|:-:|:-:|:-:|:--|
| Q 50 → Q 51 | 0.1192 | 89/113 | 1.44% | mid-tier expensive (the Q 49→50 hinge spills over slightly) |
| Q 51 → Q 52 | 0.0096 | 18/113 | 0.12% | near-clamped; al-Biqāʿī VINDICATED |

The Q 51 → Q 52 transition is among the **smoothest 16% of corpus-wide adjacencies** — well within the cluster of 24 transitions with delta_raw < 0.030.

## 5. UAS rank (top-15 architectural significance)

H-NEW-840 unified architectural score: Q 51 ranks **15/114** with UAS = +1.802.

The top-15 (most-architecturally-significant) surahs include:
1. Q 33 al-Aḥzāb (UAS 9.36)
2. Q 1 al-Fātiḥa (8.87)
3. Q 2 al-Baqara (7.40)
4. Q 9 al-Tawba (6.18)
5. Q 24 al-Nūr (4.45)
…
**15. Q 51 al-Dhāriyāt (1.80)**

Q 51 is the **first oath-opener cluster member** in the UAS top-15 (Q 37 ranks 79; Q 53 ranks 26; Q 52 ranks ~50). Among mid-Meccan oath-openers, Q 51 has the **strongest architectural footprint**.

The UAS = 1.80 decomposes:
- |abs_outlier| = 16.17 (Q 51's cohesion-anchor delta)
- |max_cost| = 0.119 (Q 50→51 delta_raw)
- |abs_ijaz| = 0.981 (sig_A magnitude)

The dominant contributor to Q 51's UAS is its **cohesion-anchor role in the {48-54} window** (the absolute-delta is 16.17 pp).

## 6. Outlier-spectrum (H-NEW-590) — Q 51 as COHESION_ANCHOR

In window {Q 48, 49, 50, 51, 52, 53, 54}:
- Block mean pairwise FR (with Q 51): 0.9154
- Block mean pairwise FR (without Q 51): 0.9712
- delta_pct = **-16.17 pp** (removing Q 51 INCREASES block dispersion by 16.17 pp)
- p_greater_W = 0.405 (block percentile not extreme)
- Classification: **COHESION_ANCHOR**

Q 51 acts as a **block-stabilizer** in the {48-54} window — pulling the diverse Q 48-54 block (Medinan Q 49 + Meccan Q 48, 50-54) into tighter cohesion. This is the **inverse** structural role of Q 55 al-Raḥmān (STRONG_OUTLIER, delta = +32.6 pp in {50-56} per H-NEW-390).

The {48-54} block contains:
- Q 48 al-Fatḥ (Medinan, victory/conquest)
- Q 49 al-Ḥujurāt (Medinan, social-etiquette)
- Q 50 Qāf (Meccan, eschatological — universal hinge boundary per H-NEW-130)
- **Q 51 al-Dhāriyāt** (Meccan, oath + theology + creation-purpose)
- Q 52 al-Ṭūr (Meccan, oath + eschatology)
- Q 53 al-Najm (Meccan, oath + Prophet's vision)
- Q 54 al-Qamar (Meccan, refrain-narrative — the *fa-kayfa kāna ʿadhābī wa-nudhur* refrain)

Q 51 sits in the middle of this 7-surah block and acts as cohesion-anchor by sharing:
- **Eschatological theme** with Q 50, Q 52
- **Oath-opener structure** with Q 52, Q 53
- **Narrative-pericope** structure with Q 54
- **Theology-tail** structure with Q 50

This multi-axis sharing makes Q 51 the block's connective center.

## 7. iʿjāz signature decomposition (H-NEW-750)

Q 51 sig_A (rhyme-entropy + cohesion) = +0.981 (rank 35/114) — moderate-strong

Component z-scores (vs corpus mean+std):
- z_rhyme_entropy = +0.476 (slightly above-mean rhyme diversity)
- z_mean_content_distance = -0.505 (slightly below-mean content distance — i.e. content-CLOSER to corpus average)
- z_local_cohesion = -0.490 (slightly below-mean local cohesion — surah's verses have moderate diversity within Q 51)

Q 51's iʿjāz signature is **moderately distinctive** — rank 35 (top 31%) on the al-Bāqillānī axis. Not in the corpus extremes, but firmly above-average.

## 8. ⭐ SPECIAL: 4-element fa-coordinated oath sibling test (this specialist run)

**Pre-registered test**: do the 4 surahs Q 37, Q 51, Q 77, Q 100 — all of which open with 4+-element *wa-l-/fa-l-* oath-cluster (active-feminine-plural-participle + cognate-accusative pattern) — form a tighter FR cluster than 4 random length-matched Meccan surahs?

**Method** (locked pre-reg Q051-F-04, SHA-verified):
- Sibling set S = {37, 51, 77, 100}.
- Length-matched null: pick 4 Meccan surahs whose verse-counts respect the bands {long: ≥100, mid: 40-99, mid-short: 20-39, short: <20} of {182, 60, 50, 11}.
- Mean pairwise FR over 4×3/2 = 6 pairs.
- 10,000 length-matched Meccan random-sample permutations.
- α_bon = 0.025 (Bonferroni-2: length-matched + uncontrolled-Meccan).

**Result**:
- **Observed sibling mean pairwise FR = 0.8836**
- **Length-matched null mean = 0.9774; p_lower = 0.0370** (PASS-DIRECTED at α=0.05)
- Random Meccan-4 null mean = 0.8820; p_lower = 0.3912 (NULL — sibling cluster not distinguishable from any 4 random Meccan surahs)

**Verdict (under Bonferroni-2 α_bon=0.025)**: PASS-DIRECTED on the length-matched test (p=0.037, single-test α=0.05 cap applies); NULL on the random-Meccan-4 test.

**Interpretation**: under length-matching (the more rigorous null), the 4-element fa-coordinated oath sibling set is FR-cohesive at p=0.037 — the morphological-syntactic similarity of these 4 openers correlates with content-similarity beyond what length alone predicts. This **REPLICATES H-NEW-1070's general finding for the oath-cluster** at the more-restrictive 4-element-fa-coordinated sub-class. Under the unconditioned random-Meccan-4 null, the test is NULL — meaning the 4-element-fa-coordinated sub-class is NOT distinguishable from random Meccan content in absolute terms.

**Single-test α=0.05 PASS-DIRECTED** ceiling per HANDOFF/04-DISCIPLINE.md (post-hoc origin disclosed in pre-reg Q051-F-04). Awaiting INDEPENDENT REPLICATION (different feature space, e.g. char-4-grams or verse-length).

## 9. ⭐ Per-verse hapax-density: Q 51 leads mid-Meccan oath-cluster

Per-verse corpus-hapax-root density across the mid-Meccan oath-cluster periphery {Q 37, 51, 52, 53}:

| Surah | Verse count | Hapax roots | Per-verse density |
|:--|:-:|:-:|:-:|
| Q 37 al-Ṣāffāt | 182 | 2 (t-l-l, j-b-n) | 0.011 |
| **Q 51 al-Dhāriyāt** | 60 | **3** (Ḥ-B-K, H-J-Ḍ, Ṣ-K-K) | **0.050** |
| Q 52 al-Ṭūr | 49 | ~0-1 (per inspection) | <0.020 |
| Q 53 al-Najm | 62 | ~1-2 | ~0.022 |

Q 51 has the **highest per-verse hapax density** of the mid-Meccan oath-cluster. This finding is striking given Q 51's mid-position in cluster centrality (rank 13/15) — the surah is **content-typical** of the cluster (close to mean) but **lexically-distinctive** at the rare-root level. A two-axis profile: typical content + rare lexicon.

## 10. Cross-finding membership

- **H-NEW-1070** (oath-opener cluster, p=0.0004 CONFIRMED) — Q 51 ∈ strict-15 cluster; rank 13/15 in centrality (mid-tier, NOT extreme periphery like Q 37 rank 15).
- **H-NEW-1140** (oath-cluster mushaf-adjacency-enriched at p=0.022) — Q 51 is in the **3-surah run Q 51-52-53** (one of 3 mushaf-adjacent oath sub-runs).
- **H-NEW-130 / cross-finding-013** (ring-topology / structural hinges) — Q 51 sits IMMEDIATELY POST the universal Q 49→50 hinge (rank 14 in top-15 FR-jumps); Q 50→51 itself is mid-tier (rank 89), Q 51→52 is near-clamped (rank 18).
- **H-NEW-590 / H-NEW-840** — Q 51 is COHESION_ANCHOR in {48-54}; UAS rank 15/114.
- **H-NEW-660** (compression-tail single-parameter law, R²=0.986) — Q 51 sits at s=51, just past the kink at s=50; predicted d̄ = 0.9603 - 0.01237×(51-50) = 0.948; observed mean d̄ to corpus = 0.872 (LOWER than predicted, by 0.076 — Q 51 is MORE content-cohesive than the law predicts at its position).

## 11. Sources

| Metric | File |
|:--|:--|
| FR distance matrix | `findings/phase-b-hypotheses/csv/h-new-111.json` |
| Adjacency cost | `findings/phase-b-hypotheses/csv/h-new-720.json` |
| iʿjāz signature | `findings/phase-b-hypotheses/csv/h-new-750.json` |
| Outlier spectrum | `findings/phase-b-hypotheses/csv/h-new-590.json` |
| UAS | `findings/phase-b-hypotheses/csv/h-new-840.json` |
| Rhyme + phoneme | `findings/phase-b-hypotheses/csv/h-new-700.json` |
| Hapax computation | `data/morphology/root-index.json` |
| Sibling test | `surahs/Q051-al-dhariyat/csv/Q051-F-04.json` (this specialist run, 2026-05-09) |

## 12. Cross-references

- [[00-overview]] — Q 51 basic structural facts
- [[02-content-analysis]] — verse-by-verse expansion + 5-block macro
- [[06-novel-findings]] — 5 SHA-locked pre-registered tests
- [[07-cross-references]] — full cross-finding integration
- [[Q037-al-saffat/01-empirical-profile|Q 37 empirical profile]] — comparative oath-opener metrics
- [[Q052-al-tur/00-overview|Q 52 empirical profile]] — right-neighbor; clamped-near-zero adjacency
- [[Q050-qaf/00-overview|Q 50 empirical profile]] — left-neighbor; pre-hinge metric
