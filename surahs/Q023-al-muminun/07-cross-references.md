---
surah: 23
surah_name_ar: المؤمنون
surah_name_translit: al-Muʾminūn
file_type: cross-references
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE
---

# Q 23 al-Muʾminūn — Cross-References


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

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

## 1. Canonical neighbours

### 1.1 Q 22 al-Ḥajj (s = 22)

- **Canonical-adjacency cost**: 0.2595 length-units (rank **6 / 113**). The mushaf "pays" 3.13% of its 8.29-unit TSP residual on the Q 22 → Q 23 transition.
- **Pairwise FR distance**: 0.953.
- **Register-class transition**: Q 22 is mixed Meccan-Medinan (ritual-pilgrimage-leaning) → Q 23 is Meccan-narrative-monorhyme. The transition crosses both register and rhyme-class boundaries.
- **Lexical pickup**: corpus-EXACT *flḥ*-pickup at the last-2/first-2 window (Q 22:77 *tufliḥūn* → Q 23:1 *aflaḥa*); no other adjacent pair in the corpus has this. See 05-classical-claims-audit.md Claim 3.
- **Embryology cross-reference**: Q 22:5 is the corpus's other major embryology-passage. Lexical Jaccard with Q 23:12-14 = 0.089, above 95th percentile of length-matched null (Q023-F-03 PASS-DIRECTED).

### 1.2 Q 24 al-Nūr (s = 24)

- **Canonical-adjacency cost**: 0.2116 length-units (rank **11 / 113**). Combined Q 22-Q 23 + Q 23-Q 24 = 0.4711 = 5.68% of TSP residual.
- **Pairwise FR distance**: 1.050.
- **Register-class transition**: Q 23 is Meccan-narrative → Q 24 is Medinan-legal (zinā / qadhf / al-ifk / ḥijāb). Q 24 is the **only Medinan-legal surah inserted into the Meccan-narrative zone** Q 21-27. Q 23 acts as the **Meccan-narrative anchor on the Meccan side of the Q 24 pivot**.
- See [[Q024-al-nur/01-empirical-profile|Q 24]] §3 for the matching analysis from Q 24's side.

### 1.3 Bracketing-cost claim

Q 23 is **one of only two surahs in the corpus with both adjacencies in the top-15 expensive** (with Q 24 itself being the other). This is the descriptive content of "Q 23 is a structural-pivot at the cost of ~6% of TSP residual."

## 2. Cluster memberships

### 2.1 UAS top-10 cluster `{Q 1, 2, 9, 10, 12, 17, 23, 24, 33, 55}`

- Q 23 rank: **9 / 114**, UAS = 2.977.
- Component contributions: |outlier| = 10.91 pp (rank 11 in absolute outlier); max_cost = 0.260 (rank 6); |iʿjāz| = 1.55 (rank 22).
- **Cluster cohesion under FR**: NULL (Q023-F-01 PRE-COMMIT-VIOLATION). The top-10 cluster is multi-axis, not root-distribution-cohesive.
- See [[h-new-840-unified-architectural-score|H-NEW-840]] for the full ranking and [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] for the architectural-type typology.

### 2.2 Pure-monorhyme cluster (entropy < 0.25 nats)

Top-6 purest monorhymes (by rhyme-Shannon-entropy, no-tashkeel final-letter):
1. Q 55 al-Raḥmān (0.066 nats)
2. Q 26 al-Shuʿarāʾ
3. Q 71 Nūḥ
4. Q 105 al-Fīl
5. Q 109 al-Kāfirūn
6. **Q 23** (0.148 nats)

Q 23's nūn-monorhyme (-ūna / -īna) is at the **moderate-pure end of this tier**. Q 55 is the corpus's reference-monorhyme (-ān refrain), with which Q 23 shares the "saturation" strategy but at lower entropy (Q 55 also reaches 96%+ monorhyme but on -ān not -ūn). Q 23 ↔ Q 55 are the corpus's two flagship monorhyme surahs.

### 2.3 The "monorhyme-saturation" architectural type (tentative; see 01-empirical-profile §10)

Surahs that win UAS via adjacency-cost + |outlier| + monorhyme-rhyme-purity, with negative-or-low sig_A score: Q 23 is the canonical example. The hypothesis (to test in future work) is that Q 55, Q 71, Q 79 share this signature.

### 2.4 Meccan-narrative-prophet-cycle FR-cluster (Q 23's nearest five FR neighbours)

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 1 | Q 43 al-Zukhruf | 0.789 | Meccan-narrative-Pharaoh |
| 2 | Q 7 al-Aʿrāf | 0.789 | Meccan-narrative-prophet-cycle |
| 3 | Q 36 Yāsīn | 0.804 | Meccan-narrative-eschatology |
| 4 | Q 21 al-Anbiyāʾ | 0.829 | Meccan-narrative-prophet-cycle |
| 5 | Q 25 al-Furqān | 0.833 | Meccan-narrative-prophet-cycle |

Q 23's content-cluster is the **Meccan-narrative-prophet-cycle family** — but the mushaf does not place Q 23 adjacent to any of its FR-content-nearest surahs. Q 23 is **content-displaced** by ~3-4 positions from Q 21 al-Anbiyāʾ (its content-nearest mushaf-neighbour).

## 3. Cross-surah verse / pericope links

### 3.1 Embryology triplet

| Surah | Verses | Stage-terms |
|:--|:-:|:-:|
| Q 22 al-Ḥajj | 5 | nuṭfa, ʿalaqa, muḍgha, mukhallaqa |
| **Q 23 al-Muʾminūn** | **12-14** | sulāla-ṭīn, nuṭfa, ʿalaqa, muḍgha, ʿiẓām, laḥm, khalqan ākhar |
| Q 75 al-Qiyāma | 37-40 | nuṭfa, maniyy, ʿalaqa, khalq |

Q 23:12-14 is the **most-elaborated embryology pericope** in the corpus (7 stage-references in 3 verses). Q 23 ↔ Q 22 share 7 distinctive tokens (J=0.089, PASS-DIRECTED per Q023-F-03). Q 75 lacks *muḍgha*.

### 3.2 Believer-attributes parallel cluster

Comparator pre-registered set:
- **Q 23:1-11** — corpus-EXACT longest strict-marker run (4 verses 2-5).
- Q 70:22-35 — 14-verse block but strict-marker run only 3 (vv. 32-34); interleaved with eschatological narrative.
- Q 8:2-4 — 3-verse block, no strict-marker.
- Q 9:71 — single-verse believer-believer description.
- Q 25:63-77 — *ʿibād al-Raḥmān* list, 15 verses but uses *yamshūna* / *yabītūna* coordinative-verb pattern instead of strict-relative-pronoun pattern.
- Q 32:15-16 — sajda-block, 2 verses.

The Q 23 vs Q 70 parallel was explicitly drawn by al-Biqāʿī (*Naẓm al-Durar*); empirically, Q 23 holds rank-1 on strict markers, Q 70 holds rank-2.

### 3.3 *yā qawmi aʿbudū llāha* preaching formula

Q 23 uses *yā qawmi aʿbudū llāha mā lakum min ilāhin ghayruhū* at vv. **23, 32** (Nūḥ + the unnamed second prophet). This formula appears across the prophet-cycle surahs:

| Surah | Verse | Prophet |
|:--|:-:|:-:|
| Q 7 al-Aʿrāf | 59, 65, 73, 85 | Nūḥ, Hūd, Ṣāliḥ, Shuʿayb (named lattice) |
| Q 11 Hūd | 50, 61, 84 | Hūd, Ṣāliḥ, Shuʿayb (wa-ilā tribe-akhāhum lattice) |
| Q 23 al-Muʾminūn | 23, 32 | Nūḥ + unnamed (deliberate ambiguity) |

Q 23's prophet-cycle is **more abstract / universalizing** than Q 7's or Q 11's — only one prophet (Nūḥ) is named in the *yā qawmi aʿbudū* formula; the second is the unnamed *fa-arsalnā fīhim rasūlan minhum*. See 02-content-analysis.md §4.7.

### 3.4 *flḥ* corpus-attestations summary

The root *flḥ* appears in the corpus at the following surahs (excluding Q 23): Q 2:5 *ulāʾika humu l-mufliḥūn*, Q 3:104, 130, 200; Q 5:35, 90, 100; Q 7:8, 69, 157; Q 8:45; Q 9:88; Q 16:116; Q 20:64, 69; Q 22:77; Q 24:31, 51; Q 28:67, 82; Q 30:38; Q 31:5; Q 58:22; Q 59:9; Q 62:10; Q 64:16; Q 87:14; Q 91:9. Q 23 has 3 *flḥ*-attestations (vv. 1, 102, 117) — the only surah with a corpus-EXACT triple-anchor inclusio (positive opening + positive mid-late + negative closing). See 06-novel-findings.md §4.

## 4. H-NEW findings touching Q 23 — full list

| Finding | Q 23 datum |
|:--|:--|
| [[h-new-111-fisher-rao-mushaf|H-NEW-111]] | Mean FR distance to corpus = 0.9665 (rank 74 / 114); nearest = Q 43 (0.789); farthest = Q 55 (1.184) |
| [[h-new-590-outlier-spectrum|H-NEW-590]] | Δ_outlier = −10.91 pp; classification = COHESION_ANCHOR; window [20-26] |
| [[h-new-660-compression-tail-gradient|H-NEW-660]] | s = 23 < kink-50; pre-kink head-zone; compression-tail law silent here by construction |
| [[h-new-700-phonological-compression-tail|H-NEW-700]] | Rhyme entropy 0.148 nats (rank 109 / 114); pre-kink position |
| [[h-new-720-canonical-adjacency-cost|H-NEW-720]] | Q 22→Q 23 = 0.2595 (rank 6/113); Q 23→Q 24 = 0.2116 (rank 11/113); combined 5.68% of TSP residual |
| [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] | Q 23 contributes to the global anti-twin lock; its monorhyme + Meccan-narrative content + anti-structural sig_A confirm anti-twin orthogonality |
| [[h-new-740-preislamic-poetry-control|H-NEW-740]] | Q 23 fits the Quran-vs-poetry distinct cluster (its FR-content is closer to other Quran surahs than to pre-Islamic poetry) |
| [[h-new-750-ijaz-signature|H-NEW-750]] | sig_A = −1.55 (rank 93); sig_B = −1.71 (rank 106); rhyme-entropy z = −1.126 |
| [[h-new-840-unified-architectural-score|H-NEW-840]] | UAS = 2.977; rank 9/114; multi-axis-aggregate |
| [[h-new-860-hadith-architectural-alignment|H-NEW-860]] | Q 23 confirms architectural / hadith-attention orthogonality; high UAS + substantial content-attention (Q 23:51 in Muslim 2230, Q 23:60 in Tirmidhī 3259) |

## 5. Cross-finding-syntheses touching Q 23

- [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]: TSP-residual super-additivity holds at Q 22-Q 23 (rank 6) + Q 23-Q 24 (rank 11) ≈ 5.68% of residual.
- [[cross-finding-025|cross-finding-025]]: Q023-F-01 NULL adds another data point to the marker-thickness rule (multi-axis aggregates do not produce FR-cohesion). Now 5 PASS + 5 NULL + 1 PASS-DIRECTED.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]: Q 23 illustrates a tentative **fifth architectural cell** — *purer-than-pure monorhyme* (high UAS + extreme monorhyme + anti-structural sig_A by construction). See 01-empirical-profile.md §10 for the case for this cell.

## 6. Honest limits

- The "Q 23 as buffer between Q 22 Ḥajj and Q 24 Nūr" framing is descriptive: the Q 22-Q 23 and Q 23-Q 24 adjacency-costs are both high, and Q 23's content sits between Meccan-narrative and Medinan-legal. The framing is not a causal inference.
- The "fifth architectural cell" claim (01-empirical-profile §10) needs replication on Q 55, Q 71, Q 79 monorhyme surahs before being elevated to a confirmed type.
- Q023-F-01's PRE-COMMIT-VIOLATION-NULL means the UAS top-10 cluster is not FR-cohesive — but cross-finding-025 already anticipated this for thin/multi-axis-aggregate markers. Q 23's role in cross-finding-025 is as a fresh confirmation of the marker-thickness threshold.
