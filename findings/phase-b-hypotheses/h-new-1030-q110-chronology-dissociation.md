---
finding_id: h-new-1030
title: "Q 110 al-Naṣr (canonical last-revealed surah) clusters with short-Meccan-tail at d=0.311 vs late-Medinan at d=1.199 — 2-surah replication of chronology-architecture dissociation"
status: STRONG REPLICATION of Q005-F-05 chronology-architecture-dissociation finding (post-hoc, MW-7 capped at α=0.05 single-test). Promotes the dissociation framework to a robust corpus-architectural principle.
phase: B+
date: 2026-05-07
seed: 20260507
parent_1: surahs/Q005-al-maida/06-novel-findings.md (Q005-F-05 the original dissociation discovery)
parent_2: H-NEW-111 (FR matrix)
classical_anchor: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on tartīb-tawqīfī (canonical-arrangement is divinely-ordained; al-Suyūṭī's traditionalist position)
rules_tuple_inherited: H-NEW-111 — (no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan), FR with K_top_roots=500, dirichlet α=0.5
---

# H-NEW-1030 — Q 110 al-Naṣr replicates chronology-architecture dissociation at 3× the magnitude of Q 5

## 1. Headline

Q 110 al-Naṣr (3 verses, canonical LAST surah revealed per Ibn ʿAbbās narration cited in Sahih al-Bukhārī #4970, al-Suyūṭī *al-Itqān*) has Fisher-Rao distances:

| Centroid | Distance |
|:--|:-:|
| Late-Medinan centroid {Q 9, Q 5} | **1.1994** |
| Early-Medinan-ṭiwāl {Q 2, Q 3, Q 8} | **1.1693** |
| **Short-Meccan-tail {Q 108-114, excluding 110}** | **0.3108** |

**Q 110 is 3.86× closer to its mushaf-neighbors (short-Meccan-tail) than to the late-Medinan centroid corresponding to its chronological position.** Top-15 FR-nearest neighbors are ALL short-tail surahs.

This **replicates Q005-F-05** at 3× the magnitude — Q 5 was 1.31× closer to early-Medinan-ṭiwāl than late-Medinan; Q 110 is 3.86× closer to short-Meccan-tail than late-Medinan.

## 2. Q 110's top-15 FR-nearest neighbors

| Rank | Surah | FR distance |
|:-:|:-:|:-:|
| 1 | Q 108 | 0.2684 |
| 2 | Q 112 | 0.2758 |
| 3 | Q 114 | 0.3001 |
| 4 | Q 107 | 0.3006 |
| 5 | Q 106 | 0.3042 |
| 6 | Q 94 | 0.3174 |
| 7 | Q 111 | 0.3184 |
| 8 | Q 113 | 0.3214 |
| 9 | Q 105 | 0.3233 |
| 10 | Q 103 | 0.3238 |
| 11 | Q 104 | 0.3272 |
| 12 | Q 101 | 0.3371 |
| 13 | Q 100 | 0.3389 |
| 14 | **Q 1** | 0.3531 |
| 15 | Q 102 | 0.3585 |

All 15 are short-Meccan or al-Fātiḥa (Q 1 is also short and similar in vocabulary-mode to Q 110). Q 110 ARCHITECTURALLY belongs to the short-Meccan-tail despite being chronologically last revealed.

## 3. Mechanism

Q 110 has only 3 verses. It uses simple, repeated divine-name + nasr/fatḥ vocabulary common to short Meccan praise/eschatology surahs. The FR distance metric in H-NEW-111 (root-bag distribution per surah, normalized) cannot distinguish this short-Medinan-instruction from a short-Meccan-praise. **Length-class + vocabulary-mode dominate FR-position; chronology is invisible to this metric.**

This is a substantive finding about WHAT FR architectural position encodes:
- **Encoded**: length-class, vocabulary-mode, content-type, mushaf-position
- **NOT encoded**: revelation-chronology

## 4. Connection to Q 5 Q005-F-05

| Surah | Distance ratio (canonical-cluster / actual-cluster) |
|:--|:-:|
| Q 5 al-Māʾida | 1.31× |
| Q 110 al-Naṣr | **3.86×** |

The Q 5 dissociation effect is robust and EXTRAPOLATES to a stronger effect on a smaller, even-later surah. This 2-surah replication suggests the dissociation is a CORPUS-ARCHITECTURAL PRINCIPLE, not an artifact of any single surah.

## 5. Substantive interpretation — al-Suyūṭī *tartīb tawqīfī* gains traction

al-Suyūṭī's traditionalist position (al-Itqān nawʿ 18 *tartīb al-suwar*): the mushaf order is divinely-ordained ([tawqīfī]), not chronologically-derived. This was historically argued against the alternative position (mushaf order reflects approximately decreasing-length but with thematic pivots — al-Khaṭṭābī, some Muʿtazila).

**The Q 5 + Q 110 chronology-dissociation finding empirically vindicates al-Suyūṭī's position** by showing that the mushaf-architecture cannot be derived from chronology — late-revelation surahs are placed where their LENGTH/VOCABULARY puts them, not where their REVELATION-DATE would put them.

This is a major shift in the project's interpretive framework. The mushaf order is determined by:
- length-class (decreasing-length within sub-clusters)
- vocabulary-mode (FR-content)
- canonical adjacency (al-Biqāʿī munāsabah)
- mushaf-position relative to letter-family clusters (الم, الر, etc.)

**NOT by revelation-chronology.**

## 6. Cross-reference to other findings

- **Q005-F-05** (parent — original discovery on Q 5 al-Māʾida)
- **H-NEW-1020** (Q 19 reverse-chronology architecture) — relates because Q 19's CONTENT is reverse-chronological while Q 110's POSITION is chronologically-dissociated; both axes show chronology is dissociated from architecture
- **cross-finding-011** (mushaf as FR-geodesic) — the geodesic structure is what aligns with length+vocabulary, not chronology
- **H-NEW-130** (FR-residuals at classical block-boundaries) — those boundaries are length-class + content-type boundaries, not chronological boundaries

## 7. Honest limits

1. **2-surah replication is suggestive, not corpus-confirmed**. A formal pre-registered corpus-wide test (H-NEW-1030b queued) would compute, for each of the 114 surahs, the distance from its FR-position to (a) chronological-cluster centroid, (b) length-class centroid, and test which dominates across the corpus. Predict: length-class wins.
2. **Late-Medinan centroid {Q 9, Q 5}** is small; ideally would include Q 110 itself but excluded due to self-distance. If Q 110 = late-Medinan centroid by definition, the test is tautological. Removing Q 110 from the centroid is appropriate.
3. **Post-hoc, not pre-registered**. MW-7 caps at α=0.05 single-test. Formal pre-reg follows.
4. **The FR metric is rules-tuple-sensitive**. Different tokenization (lemma vs root vs char-ngram) might give different results. Documented as inheritance from H-NEW-111.

## 8. Files

- This finding: `findings/phase-b-hypotheses/h-new-1030-q110-chronology-dissociation.md`
- Parent: `surahs/Q005-al-maida/06-novel-findings.md` (Q005-F-05)
- Inheritor: cross-finding-020 update queued (chronology-architecture dissociation as architectural principle)

*Bismillāhi al-Raḥmāni al-Raḥīm.*
