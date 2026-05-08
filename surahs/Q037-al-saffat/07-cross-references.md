---
surah: 37
surah_name_ar: الصافات
surah_name_translit: al-Ṣāffāt
file_type: cross-references
date_last_updated: 2026-05-08
phase: B+
verdict: Cross-finding integration; mushaf-neighbor links; cluster-membership map.
---

# Q 37 al-Ṣāffāt — Cross-References

## 1. Mushaf-neighbor relationships

### Q 36 Yāsīn (left neighbor)
- al-Biqāʿī Q 36 → Q 37 munāsabah: theological-creational seam (Q 36 closes with resurrection-affirmation; Q 37 opens with cosmic-monotheism + creation-reference at v. 5).
- Empirical: Q 36 → Q 37 fraction_residual = 0.0080 (low; among smoothest-30 adjacencies). VINDICATES al-Biqāʿī.
- FR distance: Q 36 ↔ Q 37 = 0.9002 (Q 36 is Q 37's rank-7 nearest neighbor).
- Q 36 has unique muqaṭṭaʿāt opener (يس); Q 37 has triple-oath opener — FORMAL-CLASS DIFFERENT but content-thematically connected (both are mid-Meccan creedal-narrative compendia).
- **Q 36 specialist file**: not yet created. (Future work.)

### Q 38 Ṣād (right neighbor)
- al-Biqāʿī Q 37 → Q 38 munāsabah: prophet-cycle continuation.
- Empirical: Q 37 → Q 38 fraction_residual = 0.0000 (clamped — SEAMLESS; 1 of 13 such pairs in corpus). VINDICATES al-Biqāʿī at the EXTREME level.
- FR distance: Q 37 ↔ Q 38 = 0.9035 (Q 38 is Q 37's rank-9 nearest; Q 37 is Q 38's rank-9 nearest reciprocally).
- Shared prophets: 4 (Nūḥ, Ibrāhīm, Isḥāq, Lūṭ).
- Q 38 has single-letter muqaṭṭaʿāt (ص); Q 37 has triple-oath. FORMAL-CLASS DIFFERENT.
- See Q037-F-05 for the seam diagnostic.
- **Q 38 specialist file**: `surahs/Q038-sad/` (run 2026-05-07; see Q038-F-01..F-05).

## 2. FR-nearest-neighbor cluster

Q 37's top-10 FR-nearest (from `findings/phase-b-hypotheses/csv/h-new-111.json`):

| Rank | Surah | Name | FR | Cluster role |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 23 | al-Muʾminūn | 0.8391 | UAS top-10; mid-Meccan creedal-narrative |
| 2 | Q 51 | al-Dhāriyāt | 0.8428 | H-NEW-1070 oath-cluster (mid-mushaf periphery, rank 13/15 centrality) |
| 3 | Q 44 | al-Dukhān | 0.8434 | mid-Meccan eschatological |
| 4 | Q 52 | al-Ṭūr | 0.8602 | H-NEW-1070 oath-cluster (rank 12/15 centrality) |
| 5 | Q 43 | al-Zukhruf | 0.8644 | ḥawāmīm cluster |
| 6 | Q 15 | al-Ḥijr | 0.8882 | ALR-5 cluster (prophet-narrative); H-NEW-97 |
| 7 | Q 36 | Yāsīn | 0.9002 | mushaf-left-neighbor |
| 8 | Q 46 | al-Aḥqāf | 0.9014 | ḥawāmīm cluster |
| 9 | Q 38 | Ṣād | 0.9035 | mushaf-right-neighbor; oath-twin to Q 50 |
| 10 | Q 32 | al-Sajda | 0.9059 | mid-Meccan |

**FR-neighborhood signature**: Q 37 sits in the mid-Meccan eschatological-creedal-narrative band, with strong affinities to (a) other oath-openers (Q 51, Q 52), (b) ḥawāmīm cluster members (Q 43, Q 46), (c) prophet-narrative ALR cluster (Q 15), and (d) immediate mushaf neighbors (Q 36, Q 38).

## 3. Cluster memberships

### H-NEW-1070 strict-15 oath-opener cluster (CONFIRMED p=0.0004)
Q 37 is a member: {Q 37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}.

**Q037-F-04 finding**: Q 37 is rank **15/15 in cluster centrality** — the most peripheral member. The cluster has a 2-tier structure (short-tail core Q 91-103 + mid-mushaf periphery Q 37, 51-53).

### Oath-cluster sub-classification (proposed by Q037-F-04 follow-up)
| Tier | Members | Mean intra-tier FR |
|:-:|:--|:--:|
| Core (short-Meccan-tail oath-condition) | Q 85, 86, 89, 91, 92, 93, 95, 100, 103 (9) | ~0.60 |
| Periphery (mid-mushaf oath-narrative) | Q 37, 51, 52, 53, 77, 79 (6) | ~0.85 |

This 2-tier structure is **a NEW corpus-finding** queued for follow-up pre-registration (H-NEW-1070.1).

### Long-Meccan prophet-narrative loose grouping
Q 37 with Q 7, 11, 19, 21, 26, 27, 28, 38 — shared narrative-compendium character. NOT a formal cluster; descriptive-only. Per H-NEW-940 prophet-order conservation: Q 37 is rank 1/8 most-aligned to consensus order.

## 4. H-NEW finding integrations (per surah row)

| Finding | Q 37 datum | Significance |
|:--|:--:|:--|
| H-NEW-111 (FR matrix) | mean dist 0.985 (corpus mean 0.923) | mildly content-distant |
| H-NEW-590 (outlier spectrum) | +3.28 pp WEAK_OUTLIER (window Q 34-40); p=0.61 | not a strong outlier |
| H-NEW-700 rhyme | top-letter ن (0.797); rhyme entropy 0.704 (LOW) | near-monorhyme on -ūn/-īn |
| H-NEW-720 (canonical adjacency) | Q 37→Q 38 fraction_residual = 0.000 (clamped) | seamless seam |
| H-NEW-750 iʿjāz signature | sig_A = -0.809 (rank 83); sig_B = -0.737 (rank 70) | LOW iʿjāz signal on both axes |
| H-NEW-840 UAS | -1.158 (rank 79/114) | LOW unified architectural significance |
| H-NEW-940 prophet-order | Kendall τ = +0.857 (rank 1/8) | most-aligned to consensus order |
| H-NEW-1070 oath-cluster | strict-15 member; rank 15/15 centrality (Q037-F-04) | peripheral cluster member |

## 5. Cross-surah verse-twins (per H-NEW verse-twin network and Q 37 internal patterns)

### Q 37:181 *wa-salāmun ʿalā al-mursalīn* ↔ Q 27:59 *wa-salāmun ʿalā ʿibādihi al-ladhīna iṣṭafā*
The only two corpus verses opening *wa-salāmun ʿalā [X]*. Different addressees (Q 37: messengers; Q 27: chosen servants). Structural-near-twin.

### Q 37:80, 105, 110, 121, 131 (refrain *innā kadhālika najzī al-muḥsinīn*) ↔ Q 12:22 *kadhālika najzī al-muḥsinīn*
The exact-match phrase appears 5× in Q 37 + 1× in Q 12 (Yūsuf, after Yūsuf becomes righteous).

### Q 37:81, 111, 122, 132 (refrain *innahu min ʿibādina al-muʾminīn*) ↔ Q 12:24 *innahu min ʿibādina al-mukhlaṣīn*
The Q 12 form has *al-mukhlaṣīn* (purified) vs Q 37's *al-muʾminīn* (believing) — different morphological-classification of the prophet.

### Q 37:1 *wa-l-ṣāffāti ṣaffā* ↔ Q 78:38 *yawma yaqūmu al-rūḥu wa-l-malāʾikatu ṣaffā*; Q 89:22 *wa-jāʾa rabbuka wa-l-malaku ṣaffan ṣaffā*
The *ṣaffā / ṣaffan ṣaffā* angelic-row image appears in 3 corpus locations; Q 37:1 is the EARLY-mushaf instance.

### Q 37:107 *wa-fadaynāhu bi-dhibḥin ʿaẓīm* — corpus-unique phrase
The single-instance "great sacrifice" ransom-phrase has no Quranic parallel.

## 6. Connection to existing H-NEW + cross-finding files

- [[h-new-1070-oath-opener-cluster]] — Q 37 is the EARLY-MID-mushaf member; Q037-F-04 finds it is the MOST PERIPHERAL.
- [[h-new-940-prophet-order-conservation]] — Q 37 is rank 1/8 most-aligned to consensus order; the Mūsā-Lūṭ inversion is the surah's distinctive feature.
- [[h-new-720-canonical-adjacency-cost]] — Q 37→Q 38 = clamped-zero (1 of 13).
- [[h-new-840-unified-architectural-score]] — Q 37 is mid-low UAS (rank 79/114).
- [[cross-finding-011-mushaf-fisher-rao-confirmed]] — Q 37→Q 38 is one of the corpus's "mushaf-natural" adjacencies (canonical adjacency at-or-better than 2-opt local rearrangement).
- [[cross-finding-019-q50-qaf-composite-hub-exemplar]] — Q 50 al-Qāf is the COMPOSITE-HUB of the singleton-muqaṭṭaʿāt + mufaṣṣal-boundary intersection; Q 37 has neither property (no muqaṭṭaʿāt; mid-mushaf not mufaṣṣal-boundary). Q 37 is in a different architectural mode than Q 50.

## 7. Connections to other surah specialist files

- **Q 12 Yūsuf** (`surahs/Q012-yusuf/`): comparator on prophet-narrative compendium; Q 12 = continuous-narrative-of-one-prophet (UAS rank 6/114; outlier +14.26pp); Q 37 = compilation-of-many-prophets (UAS rank 79/114; outlier +3.28pp). Different narrative architectures within the "prophet-narrative" loose category.
- **Q 38 Ṣād** (`surahs/Q038-sad/`): mushaf-right-neighbor; al-Biqāʿī munāsabah; specialist run 2026-05-07. Q 38 is the prophet-cycle saturation surah (rank 1/114 by prophet-density among n≥50); Q 37 is the prophet-CYCLE compendium (longest oath-opener prophet-cycle). Together they form the **mushaf's prophet-cycle high-density region**.
- **Q 19 Maryam, Q 21 al-Anbiyāʾ, Q 26 al-Shuʿarāʾ**: other prophet-narrative-compendium surahs; all are H-NEW-940 narrative-set members; Q 19 is the corpus's only inverted-order surah (Kendall τ = -0.091); Q 21 is the al-anbiyāʾ-named surah; Q 26 is the *poets* surah with messenger-cycles.
- **Q 50 al-Qāf** (specialist file not yet created): single-letter muqaṭṭaʿāt + oath-by-Quran twin to Q 38; Q 50 has the *kabsh* / Day-of-Judgment imagery shared with Q 37's eschatological middle (vv. 11-74).

## 8. Future-work queue

1. **H-NEW-1070.1** — formal pre-reg of the 2-tier oath-cluster structure (core Q 85-103 + periphery Q 37, 51-53, 77, 79); test if the 2-tier model fits FR-cohesion better than a uniform 15-cluster model.
2. **Q 37 morphological-pattern-cohesion test** — develop a new instrument that captures Q 37:1-3 grammatical-template parallelism (e.g., POS-template overlap, root-pattern signature similarity); re-test the trio cohesion with this instrument; if it confirms cohesion at the morphological level, it would VINDICATE the al-Rāzī / al-Bāqillānī classical reading at the rules-tuple-shifted level.
3. **Q 37 *salām ʿalā* construction independent-replication** — re-run the Q037-F-01 monopoly test on alternative orthographic conventions (Uthmani-consonantal, Mashriqi-vs-Maghribī); verify the 4-of-4 monopoly is rules-tuple-stable; promote PASS-DIRECTED to CONFIRMED.
4. **Q 37 ↔ Q 38 cross-prophet-correlation** — test the hypothesis that the 4 shared prophets (Nūḥ, Ibrāhīm, Isḥāq, Lūṭ) appear in correlated narrative-positions (early-vignette in both surahs). This would refine the "shared prophet-cycle continuation" mechanism.
5. **Yūnus tribe-number hadith verification** — verify the al-Tirmidhī #3313 (idInBook) chain against a verified Dār al-Salām printed-edition; resolve the *ʿan rajulin* weak-link issue; update Claim 7 verdict accordingly.

## 9. Wikilinks summary

- [[surahs/Q037-al-saffat/00-overview|Q 37 overview]]
- [[surahs/Q037-al-saffat/01-empirical-profile|Q 37 empirical profile]]
- [[surahs/Q037-al-saffat/02-content-analysis|Q 37 content analysis]]
- [[surahs/Q037-al-saffat/03-tafsir-survey|Q 37 tafsir survey]]
- [[surahs/Q037-al-saffat/04-hadith-corpus|Q 37 hadith corpus]]
- [[surahs/Q037-al-saffat/05-classical-claims-audit|Q 37 classical claims audit]]
- [[surahs/Q037-al-saffat/06-novel-findings|Q 37 novel findings]]
- [[surahs/Q012-yusuf/00-overview|Q 12 Yūsuf]]
- [[surahs/Q038-sad/00-overview|Q 38 Ṣād]]
- [[h-new-940-prophet-order-conservation|H-NEW-940]]
- [[h-new-1070-oath-opener-cluster|H-NEW-1070]]
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]]
