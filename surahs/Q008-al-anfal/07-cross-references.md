---
surah: 8
surah_name_ar: الأنفال
surah_name_translit: al-Anfāl
file_type: cross-references
date_last_updated: 2026-05-09
phase: B+
verdict: Cross-finding integration; mushaf-neighbor links; cluster-membership map; CF-013 ring-topology hinge analysis.
---

# Q 8 al-Anfāl — Cross-References

## 1. Mushaf-neighbor relationships

### Q 7 al-Aʿrāf (left neighbor)
- **Architectural classification**: Late-Meccan ALMṢ-singleton (the only surah opening with المص); 206 verses, longest of the Late-Meccan period.
- **Empirical**: Q 7 → Q 8 fraction_residual = **0.0256, rank 10/113** (top decile most expensive). The transition is a **major chronology-break seam** — the mushaf jumps from Late-Meccan ALMṢ to Medinan post-Hijra in a single adjacency.
- **FR distance**: Q 7 ↔ Q 8 = ~0.96 (Q 7 is NOT in Q 8's top-10 FR-nearest; mid-distant).
- **Munāsabah (al-Biqāʿī)**: Q 7 closes with the Mosaic-narrative-conclusion + the cosmic-witness-verses (vv. 158-206); Q 8 opens with the Madīnan polity-foundation. The thematic-shift is decisive.
- **Q 7 specialist file**: not yet created. (Future work.)

### Q 9 al-Tawba (right neighbor — basmala-asymmetry pair)
- **Architectural classification**: latest-Medinan polemical surah; ONLY surah without basmala-prefix; the al-Fāḍiḥa.
- **Empirical**: Q 8 → Q 9 fraction_residual = **0.0074, rank 58/113** (mid-tier). The transition pays a real but modest TSP cost.
- **FR distance**: Q 8 ↔ Q 9 = **0.911, rank 9** of Q 8's top-10 FR-nearest neighbors. Q 9 is FR-near to Q 8 but NOT closest (Q 3 is rank 1).
- **Adjacent-pair FR rank**: 81/113 (above-median dissimilarity per H-NEW-890 T1).
- **Root-Jaccard**: 0.350; rank 13/113 in adjacent pairs; rank 196/6,441 in all pairs (top 3.0%).
- **Critical finding**: per Q008-F-01 (this surah's specialist test), the **classical Ibn ʿAbbās "Q 8 + Q 9 = one surah" reading is FALSIFIED** on all 3 empirical axes. The basmala-omission is preserved as a thematic-continuity marker (per al-Biqāʿī), not as a unity-claim.
- **Munāsabah (al-Biqāʿī)**: Q 8 establishes the *walāʾ-foundation* (muhājirūn/anṣār); Q 9 opens with *barāʾatun min allāhi wa-rasūlihi* — *walāʾ-disownment*. Foundation → disownment continuity.
- **Q 9 specialist file**: `surahs/Q009-al-tawba/` (parallel surah-pair).

## 2. FR-nearest-neighbor cluster

Q 8's top-10 FR-nearest (from `findings/phase-b-hypotheses/csv/h-new-111.json`):

| Rank | Surah | Name | FR | Cluster role |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 3 | Āl ʿImrān | 0.8073 | Medinan-ṭiwāl Uḥud-narrative twin |
| 2 | Q 22 | al-Ḥajj | 0.8507 | Medinan-late legal/jihād authorization |
| 3 | Q 2 | al-Baqara | 0.8737 | longest Medinan-ṭiwāl (al-sabʿ al-ṭiwāl sister) |
| 4 | Q 48 | al-Fatḥ | 0.8995 | qitāl-cluster centroid (per Q008-F-03) |
| 5 | Q 5 | al-Māʾida | 0.9015 | latest-Medinan legal compendium |
| 6 | Q 4 | al-Nisāʾ | 0.9073 | Medinan-ṭiwāl legal |
| 7 | Q 60 | al-Mumtaḥana | 0.9079 | Medinan walāʾ-disownment |
| 8 | Q 59 | al-Ḥashr | 0.9089 | Medinan Banū al-Naḍīr expedition |
| 9 | Q 9 | al-Tawba | 0.9110 | mushaf-right-neighbor |
| 10 | Q 29 | al-ʿAnkabūt | 0.9112 | Late-Meccan testing-narrative |

**FR-neighborhood signature**: 9/10 of Q 8's top-10 FR-nearest are MEDINAN (Q 3, 22, 2, 48, 5, 4, 60, 59, 9; only Q 29 is Late-Meccan). The Medinan-ṭiwāl legal-political character of Q 8 places it firmly in the Madīnan FR-cluster.

**Notable**: Q 9 is rank 9 (NOT rank 1). The mushaf-adjacent surah is FR-NEAR but NOT FR-NEAREST — see §1 above and `06-novel-findings.md` Q008-F-01.

## 3. Cluster memberships

### al-sabʿ al-ṭiwāl (the seven long surahs) — H-NEW-67
- The classical "seven-long" tradition is split on whether Q 8 is the seventh (with Q 8 + Q 9 read as one surah) OR Q 9 is the seventh OR Q 10 is the seventh (per al-Bāqillānī and varying traditions).
- Empirical: H-NEW-67 confirmed 5 of 7 are in absolute top-7 longest at p = 1×10⁻⁴.
- Q 8 length (75 v, 1,320 w) places it in the long-Medinan-ṭiwāl band but NOT the absolute-top-7. Under the classical Q 8 + Q 9 = one surah reading, the COMBINED 75 + 129 = 204 verses places the pair high in the top-7.
- Per Q008-F-01 the unity-claim is FALSIFIED, so Q 8 alone is the candidate, and it places at rank 9 in absolute-length (not top-7).

### Medinan-ṭiwāl FR-cluster {Q 2, 3, 4, 5, 8, 9, 22}
- Loose grouping based on Q 8's top-10 FR-nearest: 7 of 10 are Medinan-ṭiwāl (Q 2, 3, 4, 5, 8, 9, 22 family).
- Not a formal pre-registered cluster; descriptive based on FR proximity.
- The cluster shares: legal compendium character, post-Hijra context, ~80-300 verse length range, top-10 corpus-mean-FR proximity.

### qitāl-fī-sabīl-Allāh cluster {Q 8, 9, 47, 48, 61}
- Pre-registered (Q008-F-03) thematic cluster anchored on the *qitāl-fī-sabīl-Allāh* motif.
- **Q008-F-03 finding**: cluster-cohesion at GROUP level is **NULL** (D_intra = 0.904; null mean 0.923; p = 0.34); but Q 8 IS closer to the cluster than to the corpus (D_q8_cluster - D_q8_corpus = -0.16).
- Q 8's cluster centrality rank: **3/5** (Q 48 al-Fatḥ centroid; Q 61 al-Ṣaff next; Q 8 third; Q 47 Muḥammad fourth; Q 9 al-Tawba periphery).
- **2-tier substructure suggested** (analogous to H-NEW-1070.1 oath-cluster): qitāl-content-core {Q 8, 47, 48, 61} + Q 9 al-Tawba periphery (the *al-Fāḍiḥa* polemical surah is content-orthogonal even within the qitāl thematic class).
- This finding is queueable as H-NEW-1260 follow-up corpus-wide pre-registration.

## 4. H-NEW finding integrations (per surah row)

| Finding | Q 8 datum | Significance |
|:--|:--:|:--|
| H-NEW-67 al-sabʿ al-ṭiwāl | length rank 9 (absolute) | 7th-or-8th depending on Q 8 + Q 9 reading |
| H-NEW-111 (FR matrix) | mean dist 1.075 (corpus mean 0.923) | content-distinct (z = +1.49) |
| H-NEW-590 (outlier spectrum) | +9.81 pp WEAK_OUTLIER (window Q 5-11); p = 0.62 | not strong outlier |
| H-NEW-700 rhyme | top-letter ن (0.520); rhyme entropy 1.286 (HIGH) | poly-rhyme Medinan-pattern |
| H-NEW-720 (canonical adjacency) | Q 7→Q 8 rank **10/113** (expensive); Q 8→Q 9 rank 58/113 (mid); Q 9→Q 10 rank **4/113** (very expensive) | Q 8 + Q 9 form a Medinan-island flanked by expensive boundaries |
| H-NEW-750 iʿjāz signature | sig_A = -0.557 (rank 75); sig_B = +0.234 (rank 53) | mid-low fawāṣil; near-median iqāʿ |
| H-NEW-840 UAS | +1.0364 (rank **22/114**) | TOP QUINTILE — driven by max_cost (Q 7→Q 8 expensive) |
| H-NEW-890 T1 | rank 81/113; p = 0.717; verdict = NULL | Q 8 + Q 9 unity FALSIFIED |
| H-NEW-1240 (13 seamless seams) | Q 8 → Q 9 NOT in clamped-zero set | Q 8 + Q 9 are NOT seamless-conjoined |
| Q008-F-01 (this specialist) | NULL on all 3 axes | Strong Ibn ʿAbbās falsified |
| Q008-F-02 (this specialist) | CONFIRMED corpus-singleton | Q 8:17 yaqīn-formula 1/6,236 |
| Q008-F-03 (this specialist) | DIRECTIONAL | qitāl-cluster non-cohesive at group level; Q 8 near-cluster |

## 5. Cross-finding integrations

### cross-finding-013 (mushaf as topological ring) — Q 8 + Q 9 hinge
- The CF-013 ring-topology synthesis identifies the mushaf as a structured topological ring with deliberate structural-boundary hinges. The Q 7 → Q 8 transition (rank 10/113) and Q 9 → Q 10 transition (rank 4/113) flanking Q 8 + Q 9 mark a **two-step transition zone** — the mushaf moves from Late-Meccan to Medinan and back to Late-Meccan in 4 surahs (Q 7 → Q 8 → Q 9 → Q 10).
- **Q 8 + Q 9 is a Medinan-island** within the head-mushaf Late-Meccan zone; the basmala-omission preserved between them is the textual signal of this island's continuous-content character.
- **Empirical fact**: this is the ONLY adjacency-pair (s, s+1) in the corpus where the basmala-omission is canonical (Q 1 has basmala as v.1 of itself, not as a separator; the conventional 113 basmalas are at every other surah-start). The basmala-asymmetry is corpus-unique to the Q 8 → Q 9 boundary.
- **CF-013 corollary**: the Q 8 + Q 9 internal seam being mid-tier (rank 58/113) and NOT clamped-zero is consistent with the ring-topology framing — the boundary is preserved as a deliberate continuation-marker rather than seamlessly-merged. The mushaf-tradition's preservation of TWO surahs WITH basmala-omission is a structural signature.

### cross-finding-015 (classical-scholarship validation pattern)
- This Q 8 specialist run **adds 1 to the SURVIVED tally** (Q008-F-02 confirms Q 8:17 yaqīn-formula corpus-singleton, vindicating al-Bāqillānī / al-Rāzī iʿjāz-keystone classical claim).
- This run **adds 1 to the REFUTED tally** (Q008-F-01 falsifies the strong-Ibn ʿAbbās "Q 8 + Q 9 = one surah" reading, though the al-Biqāʿī weaker thematic-continuity reading remains vindicated).
- The pattern persists: classical aesthetic-rhetorical / balāgha claims SURVIVE empirical testing; classical structural-numerological / one-surah-identity claims FAIL.

### cross-finding-026 (iʿjāz architecture §13 4-cell typology)
- Q 8 placement: **structural-distinct + content-distant + UAS top-quintile + sig_A negative** = §13 *outlier-anchor* cell (top-quintile UAS but sig_A negative — outlier-driven, not fawāṣil-driven). This places Q 8 in the **Medinan-legal-hub-at-seam** sub-class within the §13 cell.
- Other §13 cell members: Q 1 al-Fātiḥa (UAS rank 2; sui-generis), Q 9 al-Tawba (UAS top, the al-Fāḍiḥa), Q 33 al-Aḥzāb. Q 8 + Q 9 are CO-MEMBERS of §13 — both are top-quintile UAS Medinan-legal hubs at major architectural seams.

### cross-finding-027 (iʿjāz al-takrīr — refrain-architecture)
- Q 8 is NOT a refrain-bearing surah (per H-NEW-1230 the corpus has 5 refrain-surahs: Q 26, 54, 55, 77, 78). Q 8 has no verbatim-refrain ≥3-occurrences.
- Q 8's iʿjāz-signature is at the **construction-singleton level** (Q 8:17 yaqīn-formula), not at the refrain level. This is a different iʿjāz-mode.

## 6. Sister-surah relationships

### Q 8 + Q 3 (rank 1 FR-nearest): the Badr-Uḥud sister-pair
- Q 3 al-ʿImrān (200 v, Medinan post-Uḥud) is Q 8's FR-rank-1 nearest neighbor.
- Q 3 is the Uḥud-asbāb companion to Q 8's Badr-asbāb. The two surahs are paired by Madinan-battle-narrative typology.
- Specifically: Q 3:121-129 narrates Uḥud (the second-major-battle); Q 8:5-19 narrates Badr (the first). The two surahs together cover the Madīnan-period's two foundational battle-events.
- Hadith-tradition (al-Bukhārī kitāb al-Maghāzī chapter 64) preserves both narratives in the same chapter-cluster.

### Q 8 + Q 47 (rank 4 in qitāl-cluster centrality)
- Q 47 Muḥammad (38 v, Medinan) is named after the Prophet ﷺ; classical *asbāb* connects it to the post-Badr period (some report it as revealed shortly before or after Badr, with the *yawm al-furqān* echo in Q 47:4).
- Q 47:4 contains the parallel *fa-ḍrabū al-riqāb* (strike the necks) command echoing Q 8:12 *aḍribū fawqa al-aʿnāq* (strike above the necks). This is a **command-twin pair**.

### Q 8 + Q 22 (rank 2 FR-nearest): the early-Medinan hajj/jihād authorization pair
- Q 22 al-Ḥajj is classically classified as Late-Meccan-or-early-Medinan (one of the few mixed-attribution surahs); contains the first-explicit qitāl-permission verse (Q 22:39 *udhina li-l-ladhīna yuqātalūna*).
- Q 8 is the post-Badr legal-apparatus surah. Q 22 → Q 8 is the chronological-narrative pair: permission-to-fight (Q 22:39) → first major battle's spoils-distribution (Q 8).
- The FR rank-2 proximity is empirical confirmation of the chronological-narrative pairing.

## 7. Specialist coordination

- **Q 9 al-Tawba** (`surahs/Q009-al-tawba/`): sister surah; PARALLEL to Q 8 in the basmala-asymmetry pair. The Q009-F tests should NOT duplicate Q008-F-01 (this Q 8/Q 9 unity test is HERE, with the empirical adjudication anchor at Q 8 specialist file).
- **Q 47 Muḥammad** (specialist file does not yet exist; queued).
- **Q 48 al-Fatḥ** (specialist file does not yet exist; queued).
- **Q 61 al-Ṣaff** (specialist file does not yet exist; queued).
- **Q 7 al-Aʿrāf** (specialist file does not yet exist; the Q 7 → Q 8 chronology-break seam queued for joint analysis).

## 8. Cross-references (quick links)

- `00-overview.md` (Q 8 basic structural properties).
- `01-empirical-profile.md` (full H-NEW metric integration).
- `02-content-analysis.md` (4-block thematic map).
- `03-tafsir-survey.md` (5 mufassirūn).
- `04-hadith-corpus.md` (verified Bukhārī Maghāzī Badr cluster anchors).
- `05-classical-claims-audit.md` (7 classical claims, 1 FALSIFIED, 4 VINDICATED).
- `06-novel-findings.md` (3 pre-registered tests).
- `JOURNAL.md` (specialist run log).
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]], [[h-new-590-outlier-spectrum|H-NEW-590]], [[h-new-700-phonological-compression-tail|H-NEW-700]], [[h-new-720-canonical-adjacency-cost|H-NEW-720]], [[h-new-750-ijaz-signature|H-NEW-750]], [[h-new-840-unified-architectural-score|H-NEW-840]], [[h-new-890-numerical-reaudit|H-NEW-890]], [[h-new-1240-13-seamless-seams|H-NEW-1240]].
- [[cross-finding-013-mushaf-ring-topology|cross-finding-013]], [[cross-finding-015-classical-scholarship-validation|cross-finding-015]], [[cross-finding-026-ijaz-architecture|cross-finding-026]].
