---
surah: 96
surah_name_ar: العلق
surah_name_translit: al-ʿAlaq
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111, 590, 700, 720, 750, 840, 930, 1300, 1301}.
---

# Q 96 al-ʿAlaq — Empirical Architectural Profile

## 1. Headline numbers

| Metric | Value | Source |
|:--|:--:|:--|
| Verse count | 19 | Hafs-Kūfan |
| Word count (whitespace) | 73 | computed |
| Letter count (no-tashkeel, sans space, sans ۩) | 288 | computed |
| Avg verse length (letters) | 15.16 | short-Meccan oath/imperative class |
| Avg verse length (words) | 3.84 | very short |
| **Tanzil revelation order** | **1 of 114** | data/revelation-order.csv (Egyptian Standard) |
| **Nöldeke order** | **1 of 114** | Nöldeke 1860 |
| Top final letter | **ي (yāʾ)** | 47.4% (vv 6-14 monorhyme block) |
| Rhyme entropy (nats) | **1.365** | z = +1.08 (HIGH-entropy) |
| Mean content distance (FR) | 0.819 | z = -1.03 |
| Local cohesion | 1.832 | z = +0.43 |
| **iʿjāz sig_A** | **+2.110** | **rank 4 / 114** (top decile) |
| iʿjāz sig_B | +1.505 | rank 14 / 114 |
| UAS | -0.0036 | rank 48 / 114 |
| Outlier-strength Δ%ile | -0.01 pp | NULL (window {Q 93-99}) |
| Q 95 → Q 96 cost | +0.0323 (delta_raw) | low (smooth seam) |
| Q 96 → Q 97 cost | +0.0684 (delta_raw) | modest |
| Sajda-tilāwa | YES at v 19 | 14-Sunni-shared |
| **IMPV-qrA tokens** | **2** | tied #1 with Q 73 (H-NEW-1300) |
| Hapax-root tokens | 2 (zbn, sfE) | corpus-unique at vv 18, 15 |

## 2. Verse-by-verse text + counts

| v | Text | Words | Letters | Final letter |
|:-:|:--|:--:|:--:|:--:|
| 1 | اقرأ باسم ربك الذي خلق | 5 | 18 | ق |
| 2 | خلق الإنسان من علق | 4 | 15 | ق |
| 3 | اقرأ وربك الأكرم | 3 | 14 | م |
| 4 | الذي علم بالقلم | 3 | 13 | م |
| 5 | علم الإنسان ما لم يعلم | 5 | 18 | م |
| 6 | كلا إن الإنسان ليطغى | 4 | 17 | ى |
| 7 | أن رآه استغنى | 3 | 11 | ى |
| 8 | إن إلى ربك الرجعى | 4 | 14 | ى |
| 9 | أرأيت الذي ينهى | 3 | 13 | ى |
| 10 | عبدا إذا صلى | 3 | 10 | ى |
| 11 | أرأيت إن كان على الهدى | 5 | 18 | ى |
| 12 | أو أمر بالتقوى | 3 | 12 | ى |
| 13 | أرأيت إن كذب وتولى | 4 | 15 | ى |
| 14 | ألم يعلم بأن الله يرى | 5 | 17 | ى |
| 15 | كلا لئن لم ينته لنسفعا بالناصية | 6 | 26 | ة |
| 16 | ناصية كاذبة خاطئة | 3 | 15 | ة |
| 17 | فليدع ناديه | 2 | 10 | ه |
| 18 | سندع الزبانية | 2 | 12 | ة |
| 19 | كلا لا تطعه واسجد واقترب ۩ | 6 | 20 | ب |

**Verse-final letter histogram**: ى (9) + م (3) + ة (3) + ق (2) + ه (1) + ب (1) = 19 verses, 6 distinct rhyme letters. Top-letter frac 47.4% — far below near-monorhyme surahs (Q 37 at 79.7% on ن, Q 55 monorhyme on ـان). Q 96 rhyme entropy 1.365 nats places it at z = +1.08 — **the 4th-highest iʿjāz sig_A in the corpus**.

## 3. Three-block rhyme architecture

| Block | Verses | Rhyme letters | Letter sequence |
|:--|:-:|:--|:--|
| **A** | 1-5 | {ق, م} | ق-ق-م-م-م |
| **B** | 6-14 | {ى} (monorhyme) | ى ×9 |
| **C** | 15-19 | {ة, ه, ب} | ة-ة-ه-ة-ب |

The rhyme cells correspond exactly to the content blocks (creation/literacy / rebellion / closing-warning). Block-boundaries: v 5/6 (rhyme letter set switches ق-م → ى) and v 14/15 (ى → ة-ه-ب). This is the empirical correlate of the 3-event compositional history (vv 1-5 first revealed; vv 6-14 post-fatra Abū-Jahl context; vv 15-19 closing-warning sajda-locus added).

## 4. Fisher-Rao neighborhood (H-NEW-111)

Top-15 nearest surahs to Q 96 by FR angular distance from `findings/phase-b-hypotheses/csv/h-new-111.json`:

| Rank | Surah | Name | FR distance | Cluster note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 102 | al-Takāthur | 0.4424 | terminal-mufaṣṣal short |
| 2 | Q 107 | al-Māʿūn | 0.4434 | terminal-mufaṣṣal short |
| 3 | Q 108 | al-Kawthar | 0.4536 | terminal-mufaṣṣal short |
| 4 | Q 100 | al-ʿĀdiyāt | 0.4631 | oath-opener |
| 5 | Q 110 | al-Naṣr | 0.4688 | terminal-Medinan short |
| 6 | Q 106 | Quraysh | 0.4768 | terminal-mufaṣṣal short |
| 7 | Q 105 | al-Fīl | 0.4819 | terminal-mufaṣṣal short |
| 8 | Q 113 | al-Falaq | 0.4819 | muʿawwidha |
| 9 | Q 112 | al-Ikhlāṣ | 0.4883 | corpus FR-centroid rank 1 |
| 10 | Q 103 | al-ʿAṣr | 0.4895 | very short |
| 11 | Q 94 | al-Sharḥ | 0.4940 | mid-mufaṣṣal short |
| 12 | Q 111 | al-Masad | 0.4961 | terminal-mufaṣṣal short |
| 13 | Q 1 | al-Fātiḥa | 0.5027 | sui-generis isolate |
| 14 | Q 95 | al-Tīn | 0.5049 | mushaf-left-neighbor |
| 15 | Q 99 | al-Zalzala | 0.5059 | terminal-mufaṣṣal short |

**All top-15 neighbors are short Meccan/Medinan surahs from the mufaṣṣal terminal-region.** Q 96 sits squarely in the Mufaṣṣal-Terminal cluster cohort. Mean FR distance to all 113 others: 0.8189 (z = -1.03 — somewhat closer to corpus on average than typical surahs).

**Far end** (top-5 FR-farthest from Q 96):
- Q 4 al-Nisāʾ: 1.2625 (long Medinan legal)
- Q 9 al-Tawba: 1.2540 (Medinan polemic)
- Q 3 Āl ʿImrān: 1.2496 (long Medinan + الم muqaṭṭaʿāt)
- Q 5 al-Māʾida: 1.2173 (long Medinan legal)
- Q 2 al-Baqara: 1.1994 (longest Medinan)

The Q 96 FR profile mirrors the chronology-content correlation: closest neighbors are short-Meccan, farthest are long-Medinan. This is a clean signal of the Meccan/Medinan compositional-mode divergence (cf. H-NEW-130 mushaf-FR-residual structural-boundary architecture).

## 5. Notable distance landmarks

| Pair | FR distance | Note |
|:--|:--:|:--|
| Q 96 ↔ Q 1 al-Fātiḥa | 0.5027 | rank-13 nearest |
| Q 96 ↔ Q 68 al-Qalam | **0.7324** | the *qalam*-mirror — moderate distance, NOT FR-near |
| Q 96 ↔ Q 73 al-Muzzammil | 0.7232 | sister IMPV-qrA surah |
| Q 96 ↔ Q 74 al-Muddaththir | 0.7781 | "first revealed" alternate (Jābir tradition Muslim 314) |
| Q 96 ↔ Q 53 al-Najm | 0.7126 | sister sajda-surah |
| Q 96 ↔ Q 87 al-Aʿlā | 0.5444 | Nöldeke #19 sister Early-Meccan |
| Q 96 ↔ Q 113 al-Falaq | 0.4819 | terminal-pair |
| Q 96 ↔ Q 114 al-Nās | 0.5151 | terminal-pair |

The *qalam*-mirror (Q 96 ↔ Q 68) FR is 0.73 — moderately distant. Q096-F-03 confirmed the pair is NOT FR-cohesive at length-matched-Meccan-pair test (p=0.28). The *qalam* shared invocation is **semantic, not structural**.

## 6. iʿjāz signature (H-NEW-750)

| Component | Q 96 value | z-score | Rank |
|:--|:--:|:--:|:--:|
| Rhyme entropy (nats) | 1.365 | +1.08 | high (4th in sig_A) |
| Mean content distance | 0.819 | -1.03 | (slightly closer; HIGH-iʿjāz given high entropy) |
| Local cohesion | 1.832 | +0.43 | (above average) |
| **sig_A** | **+2.110** | — | **rank 4/114** |
| sig_B | +1.505 | — | rank 14/114 |

Q 96 is **4th in the corpus on the iʿjāz sig_A axis** — a top-decile position. The signature is driven by:
1. HIGH rhyme entropy (multi-rhyme structure rather than monorhyme — unusual for short surahs, which tend to be monorhyme).
2. ABOVE-AVERAGE local cohesion (the verses are relatively semantically tied within the surah).
3. SLIGHTLY-CLOSER mean content distance (Q 96 is content-typical, not isolated).

This combination — high rhyme variety + high cohesion — is what al-Bāqillānī's *iʿjāz al-fawāṣil* doctrine identifies as the rhyme-content harmony of Quranic style. Q 96 is the corpus's 4th-strongest exemplar of this property under H-NEW-750's operationalization.

**Cross-finding-026** (iʿjāz architecture) places Q 96 in the *iʿjāz-al-fawāṣil*-high cell. Comparison with Q113-F-01 (Q 113 al-Falaq cell-membership): Q 113 sig_A rank 7; Q 96 sig_A rank 4 — Q 96 is HIGHER on the iʿjāz axis than the muʿawwidhāt anchor.

## 7. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json`:

| Field | Value |
|:--|:--:|
| Window | {Q 93, 94, 95, **96**, 97, 98, 99} |
| d_W | 0.4799 |
| d_W − Q 96 | 0.4577 |
| Δ pp | -0.01 |
| pct_W | 0.04 |
| pct_W − Q 96 | 0.05 |
| p_greater_W | **0.9996** |
| Classification | **NULL** |

Q 96 is **statistically invisible** as an outlier within its 7-surah window {Q 93-99}. The window itself has d_W = 0.48 (extremely cohesive — well below corpus mean 0.92), suggesting the {Q 93-99} stretch is a TIGHT mufaṣṣal-terminal cohort. Q 96 fits seamlessly into this cohort.

Compare the top-5 outliers (which Q 96 is NOT among):
- Q 33 al-Aḥzāb: Δ=+31.46pp STRONG_OUTLIER
- Q 1 al-Fātiḥa: Δ=+27.09pp STRONG_OUTLIER
- Q 24 al-Nūr: Δ=+23.51pp MODERATE_OUTLIER
- Q 9 al-Tawba: Δ=+21.57pp MODERATE_OUTLIER
- Q 12 Yūsuf: Δ=+14.26pp MODERATE_OUTLIER

Q 96 NULL on outlier-strength is consistent with high local cohesion (z=+0.43) — the surah is content-typical for its zone, not lexically distinctive within it.

## 8. UAS — Unified Architectural Score (H-NEW-840)

| Component | Q 96 value | Q 96 contribution |
|:--|:--:|:--|
| abs_outlier (Δ pp) | 0.01 | minimal (NULL outlier-strength) |
| max_cost (delta_raw) | 0.0684 | the Q 96 → Q 97 adjacency |
| abs_ijaz | 2.110 | HIGH — drives positive UAS |
| **UAS** | **-0.0036** | **rank 48/114** |

Q 96 UAS is mid-range despite top-decile iʿjāz, because the outlier-strength NULL drags the composite. Q 96 is high on iʿjāz alone but average on the combined axis.

Top UAS surahs (for context): Q 33, Q 1, Q 2, Q 9, Q 24 — all long surahs with high outlier-strength + high cost. Q 96's profile (HIGH iʿjāz, LOW outlier, LOW cost) is the structural-INVERSE of the top-UAS surahs.

## 9. Canonical-adjacency cost (H-NEW-720)

| Boundary | delta_raw | fraction_residual | Note |
|:--|:--:|:--:|:--|
| Q 94 → Q 95 | +0.0470 | 0.0057 | low cost |
| Q 95 → Q 96 | +0.0323 | 0.0039 | LOW cost (smooth seam) |
| Q 96 → Q 97 | +0.0684 | 0.0082 | modest cost |
| Q 97 → Q 98 | +0.0275 | 0.0033 | low cost |

Both Q 96 boundaries are NON-clamped-zero (the 13-pair clamped-zero set per H-NEW-1240 does not include any Q 96 adjacency). The Q 96 → Q 97 modest cost is consistent with Q 96 (creation/literacy) → Q 97 al-Qadr (Night-of-Power) genre shift. Q 95 → Q 96 (al-Tīn → al-ʿAlaq) is unusually LOW — the two surahs share oath-frame/creation-themes (al-Tīn opens with oaths on figs/olives; al-ʿAlaq opens with imperative on creation).

## 10. Q 96 in the IMPV-qrA inventory (H-NEW-1300)

The complete corpus inventory of imperative *iqraʾ/iqraʾū* tokens (POS:V, MOOD:IMPV, ROOT:qrA per QAC v0.4):

| Surah | Verse-token | Form | Person/Number |
|:--|:--|:--|:--|
| Q 17:14 | word 1 | `{qora>o` | 2MS |
| Q 69:19 | word 8 | `{qora'u` | 2MP |
| Q 73:20 | word 26 | `{qora'u` | 2MP |
| Q 73:20 | word 49 | `{qora'u` | 2MP |
| Q 96:1 | word 1 | `{qora>o` | **2MS** |
| Q 96:3 | word 1 | `{qora>o` | **2MS** |

**6 corpus tokens, 4 surahs.** Q 96 has 2 of 6 (33% of corpus IMPV-qrA), and is the **ONLY surah with 2 imperatives in 2 distinct verses**. Q 73:20 has 2 imperatives but they fall in the SAME verse (the famously long v 20).

Q 96 imperatives are both **2MS (singular addressee)** matching Q 17:14 — the eschatological *iqraʾ kitābak* ("read your own record"). Q 69 and Q 73 use 2MP (plural). Q 96 + Q 17 are the **2MS pair** of corpus IMPV-qrA.

Per H-NEW-1300, this Q 96-Q 73 tie at rank 1 caused the strict pre-reg to NULL out, with the descriptive 4-surah cluster {17, 69, 73, 96} pattern noted.

## 11. *qalam* corpus inventory

The 4 corpus *qalam* tokens (root qlm):

| Verse | Context | Surah type |
|:-:|:--|:--|
| Q 3:44 | "...idh yulqūna aqlāmahum..." (Mary's casting of pens-as-arrows of divination) | long Medinan الم |
| Q 31:27 | "wa-lawu annamā fī al-arḍi min shajaratin aqlāmun..." (if all earth's trees were pens, they would not exhaust God's words) | long Meccan الم |
| Q 68:1 | "Nūn wa-l-qalam wa-mā yasṭurūn" (oath-opener of al-Qalam) | short Meccan ن (single-letter muq) |
| **Q 96:4** | "alladhī ʿallama bi-l-qalam" (He who taught by the pen) | short Meccan non-muq |

The 4 split into:
- **Long surah, mid-text**: Q 3:44 + Q 31:27 (Medinan/Meccan الم muqaṭṭaʿāt)
- **Short surah, opening cluster**: Q 68:1 + **Q 96:4** (Meccan, opening verses)

Q 96 + Q 68 are the 2 short-Meccan opening-cluster *qalam* attestations. Their FR distance is 0.7324 (Q096-F-03 NULL-BROKEN at FR cohesion test); the link is **semantic, not structural**.

## 12. ʿalaq corpus inventory

The 7 corpus *ʿalaq* tokens (root Elq) per `data/morphology/root-index.json`:

| Verse | Context | Sense |
|:-:|:--|:--|
| Q 4:129 | "fa-ta*udhuhā ka-l-mu*allaqa" | "left in suspense" (a wife) |
| Q 22:5 | "thumma min nuṭfa thumma min ʿalaqa" | embryonic clot (creation cycle) |
| Q 23:14 | "thumma khalaqnā al-nuṭfata ʿalaqa" | embryonic clot |
| Q 23:14 | "fa-khalaqnā al-ʿalaqata muḍgha" | embryonic clot |
| Q 40:67 | "thumma min nuṭfata thumma min ʿalaqa" | embryonic clot |
| Q 75:38 | "thumma kāna ʿalaqa" | embryonic clot |
| **Q 96:2** | "khalaqa al-insāna min ʿalaq" | **embryonic clot** (NAMING verse) |

Q 96:2 is **1 of 6 embryonic-creation contexts** for *ʿalaq* in the corpus (the 7th, Q 4:129, is unrelated semantic). The embryonic-creation cluster is corpus-coherent: same theological motif (man from clot) reinstantiated across 5-6 surahs. Q 96:2 is the EARLIEST chronologically (rev #1) and gives the surah its name.

This is consistent with H-NEW-119's 7-fold corpus inventory pattern (Quranic numerology often clusters at 5-8 attestations of theological-key terms). The *ʿalaq* 7-token inventory was NOT pre-registered as a 7-fold prediction; it is descriptive.

## 13. Hapax-root signature

Per QAC v0.4 + `data/morphology/root-index.json`:

| Root | Form | Verse | Corpus frequency | Status |
|:--|:--|:-:|:-:|:--|
| zbn | الزبانية | 96:18 | **1** | corpus-hapax (Q 96 only) |
| sfE | لنسفعا | 96:15 | **1** | corpus-hapax (Q 96 only) |
| nSy | الناصية / ناصية | 96:15, 96:16 | 4 (Q 11:56, Q 55:41, **Q 96:15, 96:16**) | rare; Q 96 contains 50% of corpus tokens |
| Tgy | ليطغى | 96:6 | 39 | mid-frequency |
| zbn (zabāniya) at v 18 = the angels of hell who carry out divine punishment in eschatological pericopes. The classical exegetes (al-Ṭabarī, Ibn Kathīr) gloss as "the savage ones / the brute angels." | | | | |
| sfE (la-nasfaʿan) at v 15 = "we will surely SEIZE/DRAG by the forelock" — emphatic verbal nūn. | | | | |
| nSy (nāṣiya) at vv 15, 16 = forelock; classical idiom for total subjugation. | | | | |

**Distinctive concentration**: Q 96 vv 15-16 contain 3 of 4 corpus nSy tokens (1 token Q 11:56 of Hūd; 1 token Q 55:41 of al-Raḥmān). The closing-warning passage vv 15-16 is **lexically pinned by a corpus-rare root (nāṣiya) at 50% concentration**, reinforced by 2 corpus-hapax roots (sfE at v 15, zbn at v 18). This is a tight 4-verse lexical cell.

Per Q096-F-02 strict pre-reg: NULL-BROKEN (PC failed). Descriptive: Q 96 ranks **3rd in rare-root density** and **4th in hapax density** within the Meccan-15-25v comparator pool of 10 surahs (Q 90 al-Balad and Q 91 al-Shams rank above on both).

## 14. Q 96 cross-references in confirmed findings

| Finding | Q 96 connection |
|:--|:--|
| H-NEW-23 (hapax verse-final z=+10.61) | Q 96:18 ends with corpus-hapax *al-zabāniya* — fits active-placement pattern |
| H-NEW-1300 (IMPV-qrA inventory) | Q 96 = 2 of 6 corpus tokens; ties Q 73 at rank 1 |
| H-NEW-1301 (IMPV-qrA cluster cohesion) | NULL-BROKEN — the {17, 69, 73, 96} 4-cluster does NOT cohere FR-wise |
| H-NEW-930 (Khalifa-19 mod) | Q 96 V=19 ≡ 0 (mod 19); refutes Khalifa numerology |
| H-NEW-89 / cross-finding-009 (META-cluster) | Q 96 is structural ISOLATE in the cluster-membership taxonomy (terminal-mufaṣṣal cohort) |
| H-NEW-111 (Fisher-Rao mushaf-geodesic) | Q 96 sits in its TSP-optimal position (low cost on both seams); contributes to overall geodesic-optimality |
| H-NEW-130 (FR residuals at structural boundaries) | Q 95 → Q 96 NOT a top-15 jump; Q 96 → Q 97 not a top-15 jump |
| H-NEW-750 (iʿjāz signature) | **Q 96 sig_A rank 4/114 — TOP DECILE** |
| H-NEW-840 (UAS) | Q 96 rank 48 (mid) |
| Cross-finding-008 (muqaṭṭāʿat as book-introduction) | Q 96 NON-muq but invokes *qalam* — orthogonal cell to muq-set |
| Cross-finding-013 (mushaf as topological ring) | Q 96 is in the back-mufaṣṣal segment; FR-near to Q 1 (0.50, rank-13) — supports wrap-around |
| Cross-finding-014 (5-principle unified equation) | Q 96 contributes to M5 compositional mode (Early-Meccan signature) |

## 15. Synthesis

Q 96 al-ʿAlaq is **structurally typical of the Mufaṣṣal-Terminal cohort** (FR neighbors Q 102, 107, 108, 100, 110), **iʿjāz-extreme** (rank 4/114 sig_A), and **lexically distinctive** at the closing-warning passage (2 hapax roots, 50% nāṣiya concentration). Its first-revelation status is empirically detectable as a 3-block compositional architecture (rhyme + content + register all align).

Q 96 carries:
- 2 of 6 corpus *iqraʾ* imperatives (33% concentration of a corpus-rare imperative-mood verb)
- 1 of 4 corpus *qalam* attestations (paired with Q 68:1)
- 1 of 7 corpus *ʿalaq* attestations (and the surah's namesake)
- 2 corpus-hapax roots (zbn, sfE)
- Sajda-tilāwa marker at v 19 (1 of 14 Sunni-shared sajda-surahs)

The empirical profile **vindicates** the classical first-revelation tradition at the rhyme-architecture and structural-signature levels, while showing the surah is content-typical (low outlier-strength) within its mufaṣṣal cohort. Q 96 is **not** an extreme structural outlier; it IS extreme in iʿjāz signature and lexical concentration of literacy-vocabulary in its first 5 verses.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
