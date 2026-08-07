---
surah: 64
surah_name_ar: التغابن
surah_name_translit: al-Taghābun
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{58c, 111, 340, 590, 700, 720, 750, 840, 1080}.
---

# Q 64 al-Taghābun — Empirical Architectural Profile


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

## 1. Headline numbers

| Metric | Value | Source / interpretation |
|:--|:--:|:--|
| Verse count | 18 | Hafs-Kufan |
| Word count (no-tashkeel) | 242 | computed |
| Letter count (no-tashkeel, sans spaces) | 1,091 | computed |
| Avg verse length (letters) | ~60.6 | mid-mufaṣṣal cadence (longer than musabbiḥāt cluster mean) |
| Avg verse length (words) | ~13.4 | legal-Medinan tier (developed-argumentation per verse) |
| Top final-letter | ر / م (TIED at 38.9%) | DUAL-MONORHYME — atypical for short-Medinan |
| Rhyme entropy (nats) | 1.194 | z = +0.768 (HIGH — letter-diverse rhyme) |
| Mean content distance (FR) | 0.875 | z = -0.482 (LOW — Q 64 is content-CLOSE to corpus) |
| Local cohesion (window) | 1.351 | z = -0.228 (Q 64 in tight neighborhood) |
| iʿjāz sig_A | +1.250 (rank 26/114) | HIGH al-Bāqillānī iʿjāz al-fawāṣil signal |
| iʿjāz sig_B | +0.540 (rank 40/114) | moderately high al-Sakkākī iqāʿ |
| UAS | +0.349 (rank 42/114) | mid-range unified architectural significance |
| Outlier-strength Δ%ile | -4.39 pp | NULL outlier (window {Q 61-67}); p_greater = 0.92 |
| Q 63→Q 64 cost | +0.0173 | modest seam |
| Q 64→Q 65 cost | 0.0000 (clamped; delta_raw = −0.00865) | **SEAMLESS** (1 of 13 clamped-zero pairs) |
| Q 65→Q 66 cost | 0.0000 (clamped; delta_raw = −0.0340) | seamless (Q 64-Q 65-Q 66 = 3-surah seamless run) |
| H-NEW-58c imperfect-tense pair-prefix to Q 62 | 37 chars | within-tense PASS; cross-tense to Q 57/59/61 = 0 chars |
| H-NEW-1080 short-Medinan centrality rank | 1/10 | Q 64 is the FR-CENTROID of the qiṣār-Madanī cluster |
| Allah-token count | 20 | density = 8.3% of 242 words (very high; matches Q 59 al-Ḥashr at +5.53 z per H-NEW-254 mufaṣṣal-depletion-ratification analysis) |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 64's top-15 nearest in FR space (decoded from `findings/phase-b-hypotheses/csv/h-new-111.json`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 63 | al-Munāfiqūn | 0.6954 | mushaf-left-neighbor; short-Medinan twin |
| 2 | Q 85 | al-Burūj | 0.6981 | Meccan oath-cosmic / *qad aflaḥa* eschatology |
| 3 | Q 57 | al-Ḥadīd | 0.7220 | musabbiḥa cluster (perfect-tense opener) |
| 4 | Q 61 | al-Ṣaff | 0.7285 | musabbiḥa cluster (perfect-tense) |
| 5 | Q 62 | al-Jumuʿah | 0.7347 | **musabbiḥa pair-mate (imperfect-tense)** |
| 6 | Q 112 | al-Ikhlāṣ | 0.7361 | tawḥīd-creed sister; cross-region twin |
| 7 | Q 58 | al-Mujādila | 0.7391 | short-Medinan block-mate |
| 8 | Q 1 | al-Fātiḥa | 0.7472 | cross-region tawḥīd twin (notable: Q 1 ↔ Q 64 d=0.747) |
| 9 | Q 110 | al-Naṣr | 0.7476 | short-Medinan-victory hymn |
| 10 | Q 95 | al-Tīn | 0.7511 | Meccan oath-creation hymn |
| 11 | Q 91 | al-Shams | 0.7524 | Meccan oath-cosmic |
| 12 | Q 66 | al-Taḥrīm | 0.7529 | short-Medinan block-mate (mushaf-right+2) |
| 13 | Q 59 | al-Ḥashr | 0.7571 | musabbiḥa cluster (Khawātim-anchor) |
| 14 | Q 60 | al-Mumtaḥana | 0.7609 | short-Medinan block-mate |
| 15 | Q 49 | al-Ḥujurāt | 0.7610 | head-of-mufaṣṣal Medinan-legal |

**Pattern**: Q 64's top-15 is a **TRIPLE OVERLAY**:
1. **Short-Medinan block (Q 57-66)**: 7 of top-15 are Q 57-66 cluster members (Q 63, 57, 61, 62, 58, 66, 59, 60). This dominance confirms Q 64's position as the block centroid (Q064-F-02).
2. **Short-Meccan-tail tawḥīd / oath cluster**: 4 of top-15 are Q 85, 95, 91, 110 (Late-Meccan / cosmic-oath / brief-tawḥīd surahs).
3. **Sui-generis tawḥīd hymns**: Q 112 al-Ikhlāṣ (rank 6) and Q 1 al-Fātiḥa (rank 8) — these are corpus-extreme isolates per cross-finding-010 / H-NEW-155 yet appear close to Q 64.

The **Q 1 ↔ Q 64 proximity (d=0.747)** is striking: Q 1 al-Fātiḥa is normally an isolate at the FR centroid layer, with its only close neighbor Q 108 al-Kawthar (d=0.338). The fact that Q 64 ranks #8 in Q 1's neighborhood (and Q 1 ranks #8 in Q 64's neighborhood) marks a **cross-region tawḥīd-creedal axis**: Q 1's seven-verse opening prayer + Q 64's eighteen-verse cosmic-tawḥīd survey share root-distribution structure despite being mushaf-distant.

Far end:
- Q 55 al-Raḥmān: 1.181 (the corpus-isolate per cross-finding-027; Q 55 is the FR-FARTHEST surah for almost every other surah).
- Q 12 Yūsuf: 1.098 (long-Meccan-narrative).
- Q 26 al-Shuʿarāʾ: 1.080 (long-Meccan-poet-polemic).
- Q 19 Maryam: 1.078 (long-Meccan-narrative).
- Q 20 Ṭā Hā: 1.066.

The far-end is dominated by long-Meccan narrative surahs — Q 64's compact 18-verse cosmological-tawḥīd survey is structurally orthogonal to extended Meccan storytelling.

## 3. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json`:

| Field | Value |
|:--|:--:|
| Window | {Q 61, Q 62, Q 63, Q 64, Q 65, Q 66, Q 67} |
| d_W | 0.799 |
| d_W − Q 64 | 0.817 |
| Δ pp | **−4.39** (Q 64 ADDS cohesion to its window) |
| pct_W | 7.76 |
| pct_W − Q 64 | 12.15 |
| p_greater_W | 0.9224 |
| Classification | **NULL outlier** (negative direction = Q 64 is cohesion-additive, not distinctive) |

The NEGATIVE Δ pp is the architectural signature of a **CLUSTER CENTROID**: Q 64's removal makes its 7-surah window LESS cohesive (window-percentile rises from 7.76 to 12.15). This empirically mirrors Q064-F-02's finding that Q 64 is rank 1/10 most-central in the H-NEW-1080 short-Medinan block.

## 4. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Note |
|:--|:--:|:--:|:--|
| Rhyme entropy (nats) | 1.194 | +0.768 | HIGH (dual-monorhyme on ر / م — letter-diverse) |
| Top final-letter | ر | 0.389 | not dominant |
| Mean content distance | 0.875 | -0.482 | LOW (Q 64 content-CLOSE to corpus) |
| Local cohesion | 1.351 | -0.228 | LOW (= Q 64 in TIGHT neighborhood) |
| **sig_A** (al-Bāqillānī iʿjāz al-fawāṣil composite) | +1.250 | rank **26/114** | HIGH |
| **sig_B** (al-Sakkākī iqāʿ composite) | +0.540 | rank **40/114** | moderately high |

Q 64 is moderately HIGH on both iʿjāz axes — a notable contrast with Q 37 al-Ṣāffāt (rank 83/70 LOW). The high sig_A rank reflects Q 64's combination of (a) high rhyme entropy (LETTER-DIVERSE rhyme = al-Bāqillānī's *fawāṣil-mukhtalifa* signature), (b) low mean content distance (= Q 64 is integrated in corpus structure), (c) low local cohesion (= Q 64 sits in a TIGHTER-than-average local cluster). al-Bāqillānī's iʿjāz al-fawāṣil claim (the verse-endings have aesthetic-prosodic intentionality) is empirically MORE INSTANTIATED in Q 64 than in 73% of the corpus.

## 5. Canonical-adjacency cost (H-NEW-720)

| Boundary | delta_raw | fraction_residual | Note |
|:--|:--:|:--:|:--|
| Q 63 → Q 64 | +0.144 | 0.0173 | modest (al-Munāfiqūn → al-Taghābun: hypocrites-to-eschatology pivot) |
| Q 64 → Q 65 | -0.00865 | **0.0000 (clamped)** | **SEAMLESS** (1 of 13 corpus clamped-zero adjacencies) |
| Q 65 → Q 66 | -0.0340 | 0.0000 (clamped) | seamless |

The clamped-zero set (delta_raw ≤ 0): {Q 91→Q 92, Q 4→Q 5, Q 6→Q 7, Q 3→Q 4, **Q 65→Q 66**, Q 109→Q 110, Q 73→Q 74, Q 105→Q 106, Q 86→Q 87, Q 93→Q 94, **Q 64→Q 65**, Q 72→Q 73, Q 37→Q 38} = **13 pairs** total.

**Q 64→Q 65 + Q 65→Q 66 are CONSECUTIVE seamless adjacencies** — the corpus's only **3-surah seamless run within the short-Medinan-block**. al-Suyūṭī's *qiṣār al-Madanī* classification gains an empirical inner-architecture: the Q 64-Q 65-Q 66 triple forms the **architectural inner core** of the short-Medinan cluster, with the outer-ring members (Q 57-63, Q 65 connecting to inner via Q 64) being thematically bridged through the inner triple.

## 6. Comparison with sister musabbiḥāt (H-NEW-58c)

| Surah | Tense form | Q 64 FR-distance | Pair-prefix to Q 64 (chars) | Top final |
|:-:|:--|:--:|:--:|:-:|
| Q 57 al-Ḥadīd | perfect (sabbaḥa) | 0.7220 | 0 (cross-tense) | ر |
| Q 59 al-Ḥashr | perfect (sabbaḥa) | 0.7571 | 0 (cross-tense) | ن |
| Q 61 al-Ṣaff | perfect (sabbaḥa) | 0.7285 | 0 (cross-tense) | ن |
| Q 62 al-Jumuʿah | imperfect (yusabbiḥu) | **0.7347** | **37 (within-tense PASS)** | ن |
| **Q 64 al-Taghābun** | imperfect (yusabbiḥu) | — | — | **ر / م** |

Notice the **decoupling**: at the SHARED-PREFIX-CHARACTER metric (H-NEW-58c), Q 62-Q 64 pair has 37 chars while Q 64-Q 57/59/61 has 0 chars (sharp tense binary). At the FR-DISTRIBUTION metric, the perfect-tense triple cluster around Q 64 with FR ∈ [0.72, 0.76] (Q 57=0.72, Q 61=0.73, Q 62=0.73, Q 59=0.76) — i.e. **the FR-axis does NOT preserve the H-NEW-58c sharp prefix-binary**. This is the expected outcome: prefix-character metric is a SURFACE-SYMBOL test (binary at the opening), while FR is a FULL-DISTRIBUTION test (averaged over the whole surah). The two metrics measure different aspects of the cluster.

The empirical picture: H-NEW-58c's tense-binary is a SURFACE-FORM signature, but the inner musabbiḥāt's content-DISTRIBUTION is more uniform than the surface signature suggests. This is consistent with classical observation: the perfect/imperfect tasbīḥ is a *grammatical* rather than a *thematic* binary.

## 7. H-NEW-58c imperfect-tense pair (Q064-F-01 RESULT)

Q064-F-01 (DIRECTIONAL):

| Diagnostic | Value | Interpretation |
|:--|:--:|:--|
| Q 64 mean dist to other 4 inner musabbiḥāt | 0.7356 | very low (well below corpus mean 0.985) |
| Random-4-subset null mean | 0.8744 | corpus baseline |
| **perm-p (D_musabb ≤ random)** | **0.0001** | PASS (well below α_bon = 0.01667) |
| Within-cluster mean (intra) | 0.7704 | cluster cohesion |
| Q 64 row-mean to other 4 | 0.7356 | LOWER than intra ⇒ Q 64 is CENTROID |
| Q 64 cluster-rank | **1/5 (most central)** | Q 64 is MORE central than the cluster's own centroid |
| D(Q 62, Q 64) pair-distance | 0.7347 | bottom 15.6% of all 6,441 pairs |
| Pair pct-rank | 15.57% | DIRECTIONAL (fails ≤5% Bonferroni window) |

H1 PASSES at perm-p = 0.0001 (highly significant). H3 PASSES (Q 64 is rank 1/5 most-central within cluster). H2 fails strict Bonferroni (15.6% > 5%) but is direction-correct. Overall verdict: **DIRECTIONAL** (2 of 3 PASS).

## 8. H-NEW-1080 short-Medinan-block centrality (Q064-F-02 RESULT)

Q064-F-02 (CONFIRMED):

| Diagnostic | Value | Interpretation |
|:--|:--:|:--|
| Q 64 mean dist to other 9 block members | 0.7409 | very low |
| Random-9-subset null mean | 0.8748 | corpus baseline |
| **perm-p (D_block ≤ random)** | **0.0000** | strong PASS |
| Q 64 centrality rank within block | **1/10** | most-central |
| H2 rank-≤-5 PASS | yes | PASS |

Both H1 and H2 PASS at α_bon = 0.025. Q 64 is the **FR-CENTROID of the entire H-NEW-1080 short-Medinan-block**. This is a structural fingerprint that elevates Q 64 from "10-cluster member" to "10-cluster gravitational anchor."

## 9. Architectural type classification

| Axis | Q 64 placement |
|:--|:--|
| Length class | mid-mufaṣṣal (n=18, in al-mufaṣṣal al-mathānī range) |
| Compression-tail position | s=64 > kink-50, INSIDE compression-tail regime |
| iʿjāz typology | HIGH-iʿjāz (rank 26/114 sig_A; rank 40/114 sig_B) |
| FR neighborhood | TRIPLE-OVERLAY: short-Medinan block (Q 57-66) + Late-Meccan oath-tawḥīd (Q 85, 91, 95) + sui-generis tawḥīd hymns (Q 1, Q 112) |
| Outlier-strength | NULL — Q 64 is COHESION-ADDITIVE to its window |
| Centroid status | Rank 1/5 within H-NEW-58c musabbiḥāt cluster; Rank 1/10 within H-NEW-1080 short-Medinan block |
| Cluster memberships | (1) musabbiḥāt cluster (Q 57, 59, 61, 62, 64, full 7-list with Q 17, Q 87); (2) short-Medinan-block (Q 57-66); (3) imperfect-tense musabbiḥāt pair with Q 62; (4) Khawātim-echo at closing (Q 64:18 *al-ʿAzīz al-Ḥakīm*) |
| Adjacency role | seamless RIGHT seam (→Q 65); modest LEFT seam (Q 63→); 3-surah seamless run with Q 65, Q 66 |

**Architectural verdict**: Q 64 is the **FR-CENTROID of the short-Medinan-block** AND a **dual-cluster bridge** (musabbiḥāt-imperfect-pair partner of Q 62; short-Medinan inner-core member). It is structurally one of the most-INTEGRATED surahs in the corpus — high centrality, low isolation, seamless right adjacency, high iʿjāz signature, and a rare CORPUS-EXACT-HAPAX root in its eponym (g-b-n at Q 64:9).

## 10. Cross-references

- [[h-new-111-fisher-rao-mushaf]] — Q 64 FR row (top neighbors Q 63, Q 85, Q 57, Q 61, Q 62).
- [[h-new-590-outlier-spectrum]] — Q 64 NULL outlier (delta_pct = −4.39 cohesion-additive).
- [[h-new-700-phonological-compression-tail]] — Q 64 dual ر / م rhyme; LETTER-DIVERSE rhyme entropy.
- [[h-new-720-canonical-adjacency-cost]] — Q 64→Q 65 clamped-zero seamless; Q 64-Q 65-Q 66 = 3-surah seamless run.
- [[h-new-750-ijaz-signature]] — Q 64 sig_A rank 26 (HIGH).
- [[h-new-840-unified-architectural-score]] — Q 64 UAS rank 42/114 (mid-range).
- [[h-new-58c-musabbihat-tense-split]] — Q 64 imperfect-tense pair-mate of Q 62.
- [[h-new-340-musabbihat-block-subset]] — Q 64 in inner-5 cluster at FR 8.1%ile.
- [[h-new-1080-short-medinan-block]] — Q 64 is rank 1/10 centroid of the 10-surah cluster.
- [[h-new-95-khawatim-extension]] — Q 64:18 closes with *al-ʿAzīz al-Ḥakīm* (2 of 8 Khawātim names — closing-fawāṣila Khawātim-echo).
- `surahs/Q057-al-hadid/` (musabbiḥa cluster sister; specialist exists).
- `surahs/Q063-al-munafiqun/` (mushaf-left-neighbor; not yet specialized).
- `surahs/Q065-al-talaq/` (mushaf-right-neighbor; not yet specialized).
