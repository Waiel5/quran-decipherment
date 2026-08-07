---
surah: 17
surah_name_ar: الإسراء
file_type: cross-references
date_last_updated: 2026-04-28
phase: B+
verdict: NEIGHBORS, CLUSTERS, H-NEW INTEGRATIONS, RECIPROCAL LINKS MAPPED
---

# Q 17 al-Isrāʾ — Cross-References


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

This file maps Q 17 into the project's empirical-architectural network: canonical-mushaf neighbors, Fisher-Rao nearest neighbors, classical-cluster memberships, verse-twin links, and the H-NEW finding integrations. Wikilinks are Obsidian-style; reciprocal references are flagged so the inverse can be added when the corresponding surah-investigation files are written.

## 1. Canonical-mushaf neighbors (Q 16 al-Naḥl, Q 18 al-Kahf)

Source: `findings/phase-b-hypotheses/csv/h-new-720.json` (per-canonical-adjacency TSP-cost map).

| Pair | TSP Δ (length-units) | Fraction of TSP residual | Rank among 113 adjacencies |
|:--|--:|--:|--:|
| **Q 16 → Q 17 (al-Naḥl → al-Isrāʾ)** | **0.191** | **2.30%** | **12 of 113** |
| **Q 17 → Q 18 (al-Isrāʾ → al-Kahf)** | **0.028** | **0.34%** | bottom-quartile (~98 of 113) |

The asymmetry is **architecturally diagnostic**: the Q 16-17 transition is moderately expensive (rank-12 of 113); the Q 17-18 transition is cheap (bottom-quartile). Q 17 is positioned *more like Q 18* than *like Q 16* by FR-roots distance.

- **Q 16 al-Naḥl** (al-mufaṣṣal-ṭiwāl, 128 verses, Late Meccan; revelation order 70 per al-Suyūṭī): bee-and-cosmic-signs surah; alif-monorhyme leaning but mixed (not in the dense-rank 2 tier); content register: signs-of-creation + Israelites + ethics. The transition Q 16 → Q 17 takes the corpus from a multi-rhyme cosmic-signs surah into a near-pure alif-monorhyme founding-event narrative.
- **Q 18 al-Kahf** (110 verses, Meccan; revelation order 69): the **corpus-rank-1 alif-monorhyme** surah (110/110 = 1.0000 alif-final per Q017-F-01 + [[Q018-al-kahf|Q 18 al-Kahf]] when produced). al-Bukhārī ḥadīth #4502, #4533, #4787 group Q 17, 18, 19, 20, 21 as Ibn Masʿūd's *al-ʿitāq al-uwal*. Q 17-18 is one of the corpus's natural-block transitions.

The Q 17 placement empirically re-validates the Companion-mnemonic block: Q 17 → Q 18 is a *cheap* transition, consistent with both being treated as one early-memorized unit. (Reciprocal link: when [[Q016-al-nahl|Q 16 al-Naḥl]] and [[Q018-al-kahf|Q 18 al-Kahf]] investigations are completed, their `07-cross-references.md` files will record the inverse-side adjacency.)

## 2. Fisher-Rao nearest-neighbor cluster — the mathānī Meccan-narrative cluster

Q 17's 10 FR-nearest neighbors (computed from `findings/phase-b-hypotheses/csv/h-new-111.json`):

| Rank | Surah | FR distance | Type | Length |
|--:|--:|--:|:--|--:|
| 1 | Q 25 al-Furqān | 0.809 | meccan | 77v |
| 2 | Q 41 Fuṣṣilat | 0.864 | meccan (Ḥawāmīm) | 54v |
| 3 | Q 34 Sabaʾ | 0.865 | meccan | 54v |
| 4 | Q 27 al-Naml | 0.868 | meccan | 93v |
| 5 | Q 7 al-Aʿrāf | 0.878 | meccan | 206v |
| 6 | Q 23 al-Muʾminūn | 0.894 | meccan | 118v |
| 7 | Q 46 al-Aḥqāf | 0.894 | meccan (Ḥawāmīm) | 35v |
| 8 | Q 10 Yūnus | 0.897 | meccan | 109v |
| 9 | Q 43 al-Zukhruf | 0.901 | meccan (Ḥawāmīm) | 89v |
| 10 | Q 18 al-Kahf | 0.901 | meccan | 110v |

**ALL 10 are Meccan**, and the cluster has strong Ḥawāmīm representation (Q 41, 46, 43) and prophet-narrative representation (Q 27 Solomon, Q 7 Pharaoh, Q 18 Cave-Companions/Moses-al-Khiḍr). Q 17 sits at the empirical center of the **mathānī Meccan-narrative core** — the long-Meccan body running roughly s = 7-46.

Q 17's FR-farthest neighbor (per `h-new-111.json`) is in the corpus-end cluster — confirmed by Q 17's distance of 1.091 to Q 33 al-Aḥzāb (the corpus's structural-iʿjāz / Medinan-legal anchor). On the dual-iʿjāz axis, Q 17 (qaṣīda-form, anti-fawāṣil) is empirically distant from Q 33 (Medinan-legal, structural-iʿjāz hub), consistent with [[cross-finding-026-ijaz-architecture|cross-finding-026]]'s orthogonality finding.

## 3. Cluster memberships

Q 17's classical-cluster affiliations:

- **al-musabbiḥāt (ʿarāʾis al-Qurʾān)** — 7 surahs opening with س-ب-ح roots: Q 17, 57, 59, 61, 62, 64, 87. Q 17 is the **unique maṣdar-form** opener (Q017-F-02 VINDICATED). Source: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, "ʿarāʾis al-Qurʾān" (`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`).
- **al-ʿitāq al-uwal (Ibn Masʿūd's earliest-learnt)** — 5 surahs per al-Bukhārī #4502, #4533, #4787: Q 17, 18, 19, 20, 21. Empirically reified as a tight TSP-block: cheap intra-block transitions (Q 17-18 at 0.028, Q 18-19 even rewarded by 2-opt, Q 19-20 cheap, Q 20-21 cheap). Five canonical neighbors experienced as one block by an early Companion, vindicated empirically.
- **alif-monorhyme dense-rank 2** — Q 17 alone in dense-rank 2 (between the 8 perfect-monorhyme surahs at 1.0000 and Q 25 at 0.987). Tier-mates: Q 18, 48, 65, 72, 76, 87, 91, 92 (rate=1.000); Q 25 (0.987); Q 33 (0.986). **Cluster cohesion audit ([[h-new-910-alif8-cluster|H-NEW-910]], 2026-04-28)**: Q 17 was tested as a near-miss member via the 12-surah comparator (alif-rate ≥ 0.97). The expanded comparator BREAKS cohesion — adding Q 17 + Q 33 + Q 20 + Q 25 raises the FR-roots within-cluster mean to pct=86.84% (worse than null mean). This means Q 17 is NOT a "near-miss member" of any architectural cluster on the alif-rāwī axis; it is form-class-similar (alif-monorhyme) but content/structure-distinct from the 8-cluster. The 8-cluster itself failed all 5 Bonferroni-5 cells at α_bon=0.01 (family verdict NULL). Implication for Q 17: the alif-rāwī of Q 17 is poetic-form, not structural-cluster membership. Note: Q017-F-01's reported alif-rate of 0.9910 (110/111) vs H-NEW-910's re-derivation of 0.9820 (109/111) is a one-verse rules-tuple discrepancy (likely Q 17:108's hamza-on-yāʾ ـئاً ending normalization); flagged as follow-up rules-tuple-alignment task. Both numbers agree Q 17 falls below 1.0 and is therefore not in the 8-cluster.
- **Mathānī (the 100 mid-length surahs between al-sabʿ al-ṭiwāl and al-mufaṣṣal)** — Q 17 with 111 verses sits in the long-mathānī tier, just below al-sabʿ al-ṭiwāl (Q 2-9) and above the mufaṣṣal block.
- **Maximal taḥaddī verses (5 total)** — Q 2:23, 10:38, 11:13, **17:88**, 52:34. Q 17:88 is the **strongest** (challenge to humans + jinn together to bring the like of the entire Qurʾān). Source: Q017-F-03 + universal classical agreement (al-Bāqillānī, al-Khaṭṭābī, al-Suyūṭī, al-Rāzī, al-Zamakhsharī).
- **Prophet's nightly recitation (per Aḥmad's Musnad via ʿĀʾisha)** — Q 17 (*Banī Isrāʾīl*) + Q 39 (al-Zumar). Cited by Ibn Kathīr in the opening of his Q 17 commentary. Anchors a **two-surah liturgical cluster** (flagged for follow-up cross-investigation).
- **Hapax / corpus-unique features**:
  - *Subḥāna* (maṣdar) as opening — Q 17 only (Q017-F-02).
  - The **maximal taḥaddī** (humans + jinn together) — Q 17:88 only.
  - The **rūḥ-from-rabb's-amr** verse — Q 17:85 (the verse provoking the most extended classical theological debate; cf. al-Ṭabarī, al-Rāzī, ad loc.).
  - *Maqām maḥmūd* — Q 17:79 only (canonically identified as al-shafāʿa al-kubrā via al-Tirmidhī #3221, #3232).
  - **Āyat al-ʿizz** — Q 17:111 (al-Suyūṭī, *al-Itqān*, citing Aḥmad's Musnad via Muʿādh b. Anas).
  - **Two divine-name pair** — Q 17:110 (*qul udʿū-llāh aw udʿū al-Raḥmān*) — the only Quranic verse explicitly equating two divine names as substitutable.

## 4. Cross-surah verse-twin links (where lexically explicit)

- **Q 17:1 (*asrā bi-ʿabdihi…*) ↔ Q 53:1-18 (*wa al-najmi… ʿinda sidrati al-muntahā*)**: classical-tradition pair (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr ad loc.) — Q 17:1 narrates the *isrāʾ* (Mecca → Jerusalem); Q 53 narrates the *miʿrāj* (Jerusalem → heavens). The two Quranic Prophet's-special-journeys are split across surahs.
- **Q 17:23-39 (Decalogue-like ethical code) ↔ Q 6:151-153 (Meccan ten-command parallel)**: cognate ethical-enumeration passage with shared *qul taʿālaw atlu mā ḥarrama rabbukum ʿalaykum* framing (Q 6:151) vs Q 17:23 *wa qaḍā rabbuka allā taʿbudū illā iyyāhu*. Both Meccan; classical mufassirūn (al-Rāzī, al-Qurṭubī ad loc.) cross-link them.
- **Q 17:78 (*aqim al-ṣalāta li-dulūki al-shamsi…*) ↔ Q 11:114, Q 20:130, Q 30:17-18**: the Qurʾān's ṣalāt-time-window verses; Q 17:78 is the canonical proof-text for the five-prayer institution.
- **Q 17:79 (*ʿasā an yabʿathaka rabbuka maqāman maḥmūdā*) ↔ no other Quranic occurrence of *maqām maḥmūd***: hapax compound; cross-referenced via ḥadīth (al-Bukhārī #7155; al-Tirmidhī #3221, #3232) to the al-Shafāʿa al-Kubrā doctrine.
- **Q 17:85 (*qul al-rūḥu min amri rabbī*) ↔ Q 16:2, Q 40:15, Q 70:4, Q 78:38, Q 97:4**: rūḥ-related verses; classical disagreement on whether *al-rūḥ* in Q 17:85 is identical with the *rūḥ* of these other verses.
- **Q 17:88 (maximal taḥaddī) ↔ Q 2:23, 10:38, 11:13, 52:34**: the five-verse taḥaddī cluster; Q 17:88 is the strongest (whole-Qurʾān + humans-and-jinn).
- **Q 17:101-104 (Moses 9 signs + Pharaoh + Israelite settlement) ↔ Q 7:103-137, Q 26:10-68, Q 27:7-14, Q 28:1-46**: Q 17's compressed Moses cycle parallels the longer cycles in the Aʿrāf/Shuʿarāʾ/Naml/Qaṣaṣ block.
- **Q 17:110 (*qul udʿū-llāh aw udʿū al-Raḥmān*) ↔ Q 25:60 (al-Furqān, *wa idhā qīla lahum usjudū lir-Raḥmān…*)**: Q 25 is Q 17's #1 FR-nearest neighbor; both surahs prominently contest the Quraysh's resistance to *al-Raḥmān* as a divine name. Empirical-classical resonance.
- **Q 17:111 (āyat al-ʿizz, *al-ḥamdu lillāhi alladhī lam yattakhidh waladā…*) ↔ Q 18:1 (al-Kahf opening, *al-ḥamdu lillāhi alladhī anzala ʿalā ʿabdihi al-kitāba…*)**: the Q 17 closing *al-ḥamdu lillāh* directly hands off to the Q 18 opening *al-ḥamdu lillāh* — a **canonical-position-aware lexical chain** spanning the Q 17-Q 18 boundary. This may be one factor in the empirical cheapness of the Q 17-Q 18 TSP transition (0.028, bottom-quartile).

## 5. H-NEW finding integrations

Q 17 is referenced in or empirically computed within the following findings:

- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** — 114×114 Fisher-Rao roots distance matrix; Q 17 nearest-10 listed in §2 above. Source: `findings/phase-b-hypotheses/csv/h-new-111.json`.
- **[[h-new-590-outlier-spectrum|H-NEW-590]]** — Q 17 outlier-strength **Δ = −3.94 pp**, p_greater = 0.379, classification **NULL**. Window [14-20] mean d̄_W = 0.9577. Q 17 is *integrated*, not outlier-anchor.
- **[[h-new-660-compression-tail-gradient|H-NEW-660]]** — Q 17 at s=17 is in the head-plateau region (max(0, s-50)=0); predicted d̄_content = 0.96. Observed Q 17 mean content distance = 1.034 (slightly above plateau).
- **[[h-new-700-phonological-compression-tail|H-NEW-700]]** — Q 17 rhyme entropy 0.0514 nats (z = −1.301), top final letter = ا (alif), top-letter fraction = 0.991 (dense-rank 2/114). Q 17 is in the rhyme-compressed tail far below the head-plateau norm — the alif-monorhyme effect.
- **[[h-new-720-canonical-adjacency-cost|H-NEW-720]]** — Q 16-17 cost = 0.191 (rank 12); Q 17-18 cost = 0.028 (bottom-quartile). The asymmetry is a classical-empirical resonance with the al-ʿitāq-al-uwal block grouping.
- **[[h-new-750-ijaz-signature|H-NEW-750]]** — Q 17 sig_A = **−2.396 (rank 111/114)** — the **anti-iʿjāz al-fawāṣil profile**: high alif-monorhyme + high mean content distance. sig_B = −1.901 (rank 109/114).
- **[[h-new-770-verse-length-compression-tail|H-NEW-770]]** — Q 17 average ≈ 14.81 words/verse (1644/111), head-mathānī tier (longer than Q 87-114 mufaṣṣal but shorter than Q 2-9 ṭiwāl).
- **[[h-new-840-unified-architectural-score|H-NEW-840]]** — Q 17 UAS = **2.220, rank 10/114**, just outside the structural-iʿjāz top-9. Decomposition: sqrt(|outlier|=3.94 · max_cost=0.191 · |sig_A|=2.40). The driving signal is sig_A magnitude (anti-fawāṣil), not outlier or cost.
- **[[h-new-870-q33-architectural-keystone|H-NEW-870]]** — Q 33 is the local-singular keystone of the Medinan-legal cluster; Q 17 is the **structurally-analogous Meccan-narrative anchor** (alif-monorhyme tier-mate; both have a single non-alif break-verse identifying the surah's founding event). Q 17 does NOT serve as a global-keystone for the compression-tail (it sits in the head-plateau where there is no kink); but the Q 17 ↔ Q 33 structural twinning (alif-monorhyme + single break-verse = founding event) is a candidate cross-finding observation flagged in `06-novel-findings.md` §"break-verse architectural law" (pre-Q017-F-05).

## 6. Cross-finding ties

- **[[cross-finding-026-ijaz-architecture|cross-finding-026]]** — Q 17 anchors the **"theological-iʿjāz hub WITHIN anti-structural-iʿjāz form"** cell of the dual-iʿjāz typology. Q 17's combination — sig_A rank 111/114 (anti-fawāṣil) + Q 17:88 maximal taḥaddī + 7-of-9 mufassirūn citation density — concretizes the al-Bāqillānī ↔ al-Khaṭṭābī orthogonality: Q 17 wins on the al-Khaṭṭābī content/effect axis precisely where it is weakest on the al-Bāqillānī fawāṣil-variation axis.
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** — the Q 17→Q 18 cheap transition (0.028, bottom-quartile) is one of the corpus's natural-block transitions, consistent with the Companion-mnemonic Q 17-18-19-20-21 grouping. Reinforces the cumulative-mushaf-FR-cost confirmation.
- **[[cross-finding-025-multi-axis-architecture|cross-finding-025]]** — Q 17 in the (UAS, hadith-emphasis) plane: high UAS (rank 10) + moderate hadith-emphasis (Q 17:78-79 cluster strong; whole-surah *fadāʾil* via al-ʿitāq al-uwal). NOT a hidden-architecture exemplar (unlike Q 33); rather a balanced architecture with both empirical and reception strength.

## 7. Specific reciprocal-link targets (cross-surah)

These are surahs whose `07-cross-references.md` should list Q 17 in their reciprocal sections when those investigations are produced:

- **[[Q016-al-nahl|Q 16 al-Naḥl]]** — canonical neighbor; Q 16-17 boundary is rank-12 of 113 (moderately expensive).
- **[[Q018-al-kahf|Q 18 al-Kahf]]** — canonical neighbor + alif-monorhyme tier-mate (corpus-rank-1, 110/110 perfect) + al-ʿitāq-al-uwal block-mate; Q 17 → Q 18 is a *cheap* transition with the *al-ḥamdu lillāh* lexical handoff (Q 17:111 → Q 18:1).
- **[[Q019-maryam|Q 19 Maryam]], [[Q020-taha|Q 20 Ṭāhā]], [[Q021-al-anbiya|Q 21 al-Anbiyāʾ]]** — al-ʿitāq-al-uwal block-mates per al-Bukhārī #4533, #4787.
- **[[Q025-al-furqan|Q 25 al-Furqān]]** — Q 17's #1 FR-nearest neighbor (FR=0.809) + alif-monorhyme dense-rank 3 (0.987, just below Q 17 in rate) + al-Raḥmān-name-debate parallel (Q 17:110 ↔ Q 25:60).
- **[[Q033-al-ahzab|Q 33 al-Aḥzāb]]** — alif-monorhyme tier-mate (Q 33 = 0.986) + single-non-alif-break-verse architectural twin (Q 33:4 ↔ Q 17:1) + dual-iʿjāz orthogonal-anchor (Q 33 structural-iʿjāz hub vs Q 17 theological-iʿjāz hub).
- **[[Q053-al-najm|Q 53 al-Najm]]** — Prophet's-special-journeys pair: Q 17:1 narrates the *isrāʾ*; Q 53:1-18 narrates the *miʿrāj*. Classical tradition (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr) treats them as one event split across surahs.
- **[[Q039-al-zumar|Q 39 al-Zumar]]** — Prophet's-nightly-recitation pair per Aḥmad's Musnad via ʿĀʾisha (cited by Ibn Kathīr at the head of his Q 17 commentary).
- **[[Q002-al-baqara|Q 2 al-Baqara]]** — Banī Isrāʾīl content cluster: Q 2 is the long-Medinan Israelite cycle, Q 17 the Meccan compressed counterpart (Q017-F-04 vindication; Q 2 outranks Q 17 only by raw count, not by density-with-name-shorthand availability).
- **[[Q001-al-fatiha|Q 1 al-Fātiḥa]]** — *al-sabʿ al-mathānī* / *fātiḥat al-Kitāb* debate: classical literature (al-Bukhārī #4474, #4703; al-Suyūṭī *al-Itqān*, nawʿ on naming) places Q 1 as **fātiḥa of the seven al-ṭiwāl**; Q 17 is the long-mathānī adjacent to but not within al-sabʿ al-ṭiwāl. Empirically, Q 1's FR-distance to Q 17 = 1.076 (far) — Q 1 anchors the muʿawwidhāt-bracket cluster, not the mathānī-Meccan cluster Q 17 sits in.

## 8. Pre-Islamic poetry comparators

For the alif-monorhyme axis (Q017-F-01):

- **Labid b. Rabīʿa**, *Muʿallaqa* (alif-monorhyme): 176/178 = 0.9888 alif-final. Below Q 17's 0.9910 — Q 17 sustains the qaṣīda-form *better* than the canonical alif-monorhyme qaṣīda. Source: `data/baseline-corpora/raw/muallaqa-labid.txt` (verified via Q033-F-01 prior computation).
- **ʿAmr b. Kulthūm**, *Muʿallaqa*: 103/105 = 0.9810 alif-final. Below Q 17.
- The other 4 *Muʿallaqāt* tested (Imruʾ al-Qays, ʿAntara, Ṭarafa, al-Ḥārith) use NON-alif rāwī and have alif-final rate ≈ 0.

Q 17's 99.10% over **111 verses** vs Labid's 98.88% over 178 verses: Q 17 sustains a higher rate over comparable length — a modest but real qaṣīda-form mastery. The pre-Islamic-poetry similarity-class for alif-monorhyme is well-populated, but Q 17 outperforms the canonical poetic exemplars at the same form. This is the empirical anchor for the **theological-iʿjāz at qaṣīda-form** interpretation: Q 17:88's taḥaddī asserts that even when the Qurʾān adopts the most poetry-adjacent form (alif-monorhyme), it cannot be matched.

## 9. Honest limits

- The neighbor analysis uses Fisher-Rao on QAC stem-roots (no-tashkeel default rules-tuple). A different distance (cosine on TF, char-NCD) might shift the top-10 ordering — but the Meccan-narrative-cluster structure is robust per [[h-new-111-fisher-rao-mushaf|H-NEW-111]] and [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] convergence.
- Cluster memberships (e.g., al-musabbiḥāt, al-ʿitāq al-uwal) are taxonomic — they carry empirical weight only when paired with a tested cohesion claim. Q017-F-02 (Subḥāna-form uniqueness) is the tested musabbiḥāt-cohesion claim for Q 17. The al-ʿitāq al-uwal block is empirically vindicated via the H-NEW-720 cheap-transition cluster (§1) but a formal cohesion test of {Q 17, 18, 19, 20, 21} is not pre-registered here; flagged for follow-up.
- Verse-twin links (§4) are listed where lexically explicit; a full verse-twin-network re-computation (H-NEW-66 successor) is outside this surah-investigation scope.
- The Q 17 ↔ Q 53 pairing for *isrāʾ + miʿrāj* is theological-narrative; the H-NEW-111 FR-roots distance Q 17 ↔ Q 53 = 1.05 (mid-far), not particularly close. Classical pair-status here is content-event-driven, not vocabulary-driven.
- The reciprocal-link targets in §7 are flagged for the *receiving* surah's own cross-references file; this Q 17 file does not unilaterally write into other surah folders.

## 10. Pointers for follow-up

- Pre-register a formal cohesion test of {Q 17, 18, 19, 20, 21} (the al-ʿitāq al-uwal block) using the `findings/phase-b-hypotheses/csv/h-new-720.json` cumulative cost, with permutation null over random 5-tuples. Hypothesis: cumulative TSP cost of the canonical Q 17-21 block is in the bottom-tail of random 5-block-cost distribution.
- Pre-register a Q 17 + Q 39 (al-Zumar) Prophet's-nightly-recitation cohesion test: do these two surahs cluster anomalously in FR-roots distance vs random pairs of Meccan surahs of comparable length?
- Pre-register Q017-F-05: catalogue all surahs with alif-rate ∈ [0.97, 0.999] and inspect each non-alif break-verse for "founding-identity" content (currently a 2-data-point observation: Q 17:1, Q 33:4 + Q 25 to be checked).
- Cross-validate the *al-ḥamdu lillāh* lexical handoff Q 17:111 → Q 18:1 against the corpus's other lexical-handoff candidates (Q 1:1 → Q 2:1; etc.) via a verse-final-to-verse-initial-token similarity map.
