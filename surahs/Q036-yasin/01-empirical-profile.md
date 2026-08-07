---
surah: 36
surah_name_ar: يس
surah_name_translit: Yāsīn
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 36 Yāsīn — Empirical Architectural Profile


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

## 1. Headline architectural metrics

Rules-tuple: `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)`. All numerical claims below are computed from disk; sources cited.

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **0.5040** | **35 / 114** (mid-pack) | `findings/phase-b-hypotheses/csv/h-new-840.json` `all_uas[surah=36]` |
| Outlier-strength Δ%ile | **−6.17 pp** | rank 22 / 114 by abs delta; **WEAK_ANCHOR (negative)** | `h-new-590.json` `all_surahs_results[X=36]` |
| Q 35 → Q 36 canonical-adjacency cost (Δ_constrained) | 0.1993 | rank **13 / 113** (top-15 expensive) | `h-new-720.json` `per_adjacency` |
| Q 36 → Q 37 cost | 0.0662 | rank 54 / 113 (mid) | same |
| iʿjāz signature sig_A (structural) | **−0.7238** | rank **80 / 114** (anti-structural-iʿjāz) | `h-new-750.json` `per_surah[surah=36]` |
| iʿjāz signature sig_B (rhyme-purity) | **−1.0711** | rank **85 / 114** (anti-rhyme-purity) | same |
| Mean Fisher–Rao distance to corpus | 0.9430 | rank 64 / 114 (median band; corpus mean 0.9235) | computed from `h-new-111.json` D_matrix |
| Local cohesion (1-step adjacency) | 1.1218 | z = −0.540 (low local cohesion = neighbors are FAR) | H-NEW-750 |
| Rhyme entropy (Shannon, nats) | **0.4765** | z = −0.531 (near-monorhyme on -ūn/-īn) | H-NEW-750 |
| Top final letter (rāwī) | ن (nūn) | 70 / 83 verses = **84.34%** | H-NEW-750; cross-validated `quran-text/quran-no-tashkeel.json` |
| Total root-tokens | 438 | rank 39 / 114 | computed `data/morphology/quranic-corpus-morphology-0.4.txt` |
| Distinct roots | 211 | rank ~40 / 114 | same |
| Words (no-tashkeel orthographic) | 754 | mid-mufaṣṣal-ṭiwāl | computed `quran-text/quran-no-tashkeel.json` |
| Letters (no-tashkeel, no spaces) | 3,092 | mid-mufaṣṣal-ṭiwāl | same |
| Verse count | 83 | rank 41 / 114 (mid-length) | `data/hafs-verse-counts.tsv` |
| H-NEW-127 verse-order optimality | z = −2.82, p = 0.0046 | **CONFIRMED** at Bonferroni-5 α = 0.01 | `findings/phase-b-hypotheses/h-new-127-verse-fisher-rao-fractal.md` |
| H-NEW-82 "heart" multi-axis test | rank ≥ 16 on all axes; **0/6 PASS** | **NULL** | `findings/phase-b-hypotheses/h-new-82-yasin-heart.md` |

**Source files**: all H-NEW JSON files referenced live in `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/`; the morphology file is `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.

## 2. The architectural paradox: HIGH HADITH-FADĀʾIL SCORE without HIGH UAS

Q 36 is the corpus's most-celebrated **liturgical-fadāʾil** surah at the popular level, yet it is empirically a mid-pack architectural surah:

| Axis | Q 36 score | Q 36 rank | What this means |
|:--|:--:|:--:|:--|
| Hadith fadāʾil emphasis (rubric 0-10) | **10** | tied with Q 1, Q 2, Q 67, Q 112 (all 10/10) | Classical liturgical attention is corpus-maximum (`h-new-860.json`). |
| UAS (structural-iʿjāz proxy) | 0.5040 | 35 / 114 | Mid-pack; well below the structural-iʿjāz top-9. |
| Outlier-strength Δ%ile | −6.17 pp | WEAK_ANCHOR (negative) | Q 36 is *integrated* in its [33-39] window, not architecturally distinct. |
| sig_A (al-Bāqillānī fawāṣil) | −0.7238 | 80 / 114 | Anti-structural-iʿjāz: rhyme dispersed (0.477 nats but only 84% nūn-final = mixed -ūn/-īn/-ān nūn-end), mean content distance MID (0.943 vs corpus 0.924), local cohesion z = −0.540. |
| FR mean distance | 0.9430 | 64 / 114 | Q 36 is *near corpus median*, not on either extreme of the FR axis. |

**This is the project's single largest hadith-vs-architecture divergence in raw rubric terms** — `h-new-860.json`'s "most-striking divergences" list pairs Q 112 al-Ikhlāṣ (UAS rank 109/114, fadāʾil 10/10) with Q 36 Yāsīn (UAS rank 35/114, fadāʾil 10/10) and Q 67 al-Mulk (UAS rank 102/114, fadāʾil 10/10). All three are theological-iʿjāz / liturgical-iʿjāz surahs in al-Khaṭṭābī's *iʿjāz al-maʿnā* lineage, and all three are mid-or-low on the al-Bāqillānī *iʿjāz al-fawāṣil* structural axis.

**Mechanism**: Q 36's content is mid-Meccan resurrection-and-prophet-rejection in compact narrative form. The rhyme is near-monorhyme (-ūn/-īn nūn-final 84%) but not extreme like Q 55 (-ān monorhyme ≈ 95%) or the 8 perfect 100% alif-monorhyme surahs. Mean content distance 0.943 is *just above* corpus mean (0.924) — Q 36 is *not* a content outlier. The mushaf "tolerates" a top-15 entry-cost (Q 35→Q 36 rank 13/113) and an unremarkable exit-cost. This is the empirical content of the Wave-D Q 36 launch's headline finding: **Q 36's liturgical centrality does not translate into structural-architectural distinction**.

## 3. The H-NEW-82 binding prior — Q 36 is NOT the empirical "heart"

[[h-new-82-yasin-heart|H-NEW-82]] (`findings/phase-b-hypotheses/h-new-82-yasin-heart.md`) pre-registered 6 axes for "heart of the Qurʾān" as a multi-axis quantitative claim:

| Axis | Q 36 rank | Q 36 score | Empirical rank-1 surah |
|:--|:-:|:-:|:--|
| A1 mushaf-position-median | 43 | dist −21.5 | Q 57 al-Ḥadīd |
| A2 verse-count-median | 88 | dist −43.0 (Q 36 has 83, median 40) | Q 75 al-Qiyāma |
| A3 letter-count-median | 76 | dist −1615 (Q 36 has ~3092, median 1477) | Q 54 al-Qamar |
| A4 lexical-centroid (mean root-Jaccard) | **18** | 0.1982 | Q 10 Yūnus |
| A5 eigenvector-centrality | 27 | 0.1259, p_perm = 0.2383 | Q 10 Yūnus |
| A6 theme-centroid (cosine) | **16** | 0.9748 | Q 46 al-Aḥqāf |

Pre-registered PASS criterion: rank 1 on ≥ 3 axes OR top-5 on ≥ 5 axes. **Q 36 attains 0/6 axes top-5 and 0/6 axes rank-1**. Verdict: **NULL**.

MW-5 instrument check passes: Q 1 and Q 114 both rank in bottom half on all 6 axes; the test is honest. The classical hadith claim (Tirmidhī global #28750, *gharīb*; al-Albānī ḍaʿīf jiddan / mawḍūʿ via Hārūn Abū Muḥammad) is **not corroborated by any of the 6 statistical axes**.

The most-Q-36-friendly axes are A4 (lexical centroid, rank 18) and A6 (theme centroid, rank 16) — Q 36 is *moderately* content-central, but Q 10, Q 40, Q 39, Q 29, Q 42 (lexical) and Q 46, Q 23, Q 25, Q 57, Q 30 (theme) all out-rank it.

The empirical content centroid of the mushaf is the **al-Ḥawāmīm cluster (Q 40-46)** at theme level and **Q 10 Yūnus** at lexical-centrality level. The empirical positional median is **Q 57 al-Ḥadīd**. The empirical FR-distance centroid is **Q 112 al-Ikhlāṣ** (rank 1 by minimum mean FR distance, computed from `h-new-111.json` D-matrix).

**Q 36 is the *liturgical* heart, not the *structural* heart.**

## 4. Fisher–Rao distance row (Q 36 against all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular` (Fisher–Rao angular on K=500 stem-roots, Dirichlet smoothing α=0.5; `D_ij = 2·arccos(Σ √(p_i·p_j))`).

**Five nearest neighbours**:

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 1 | Q 25 al-Furqān | 0.7778 | Meccan, scripture-announcement, prophet-narrative |
| 2 | Q 43 al-Zukhruf | 0.7873 | Meccan, ḥawāmīm, prophet-narrative + idolatry-polemic |
| 3 | Q 67 al-Mulk | 0.7940 | Meccan, eschatological-cosmic, *al-Munjiya* |
| 4 | Q 23 al-Muʾminūn | 0.8045 | Meccan, prophets + signs + resurrection cycle |
| 5 | Q 15 al-Ḥijr | 0.8053 | Meccan, prophet-rejection narratives |

**Five farthest neighbours**:

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 109 | Q 8 al-Anfāl | 1.1081 | Medinan-legal, battle |
| 110 | Q 33 al-Aḥzāb | 1.1171 | Medinan-legal, household + battle |
| 111 | Q 4 al-Nisāʾ | 1.1384 | Medinan-legal, family law |
| 112 | Q 9 al-Tawba | 1.1861 | Medinan-legal, hypocrites/apostasy |
| 113 | Q 55 al-Raḥmān | **1.1951** | Meccan but extreme-monorhyme fawāṣil-driven |

**Interpretation**: Q 36's nearest five neighbours are **all Meccan and prophet-narrative-and-scripture-announcement-saturated**. The cluster is the project's "mid-Meccan resurrection-and-prophet-rejection" pole, with Q 25, Q 43, Q 67, Q 23 sitting at Q 36's empirical content-cluster center. Q 36's actual canonical-mushaf neighbour Q 35 (Fāṭir) sits at FR distance 0.9431 (rank ~64 of 113) and Q 37 (al-Ṣāffāt) at 0.9002 (rank ~46 of 113); both are mid-distance from Q 36 — Q 36 is content-adjacent to Q 25, Q 43, Q 67 *more* than to its actual canonical neighbours, by a margin of 0.15-0.16 FR units. This is a milder cousin of the Q 24 / Q 33 "content-class mismatch with canonical-neighbours" pattern.

The farthest pair Q 55 (al-Raḥmān, 1.1951) is consistent with project-wide architecture: al-Raḥmān is monorhyme fawāṣil-driven (sig_A=+3.17, rank 1 of 114); Q 36 is anti-fawāṣil but at a milder magnitude (sig_A=−0.72, rank 80) than Q 55's symmetric extreme. Q 4, Q 9, Q 33 are Medinan-legal and content-far from any Meccan-narrative surah by construction.

**Q 36's FR-pole**: of the 5 nearest, **Q 67 al-Mulk** is the project's other 10/10 fadāʾil surah in this neighborhood (rank 3 nearest to Q 36 at 0.794). The two recitation-loaded Meccan surahs — Q 36 *qalb al-Qurʾān* and Q 67 *al-Munjiya* — are FR-content-neighbors at the corpus level, not just liturgical co-promotion. See `07-cross-references.md`.

## 5. Outlier-window decomposition (H-NEW-590)

The 7-window centred on Q 36 is `[33, 34, 35, 36, 37, 38, 39]` per `h-new-590.json`:

| Removed | d̄_W | d̄_W−X | percentile shift Δ (pp) | classification |
|:--:|:--:|:--:|:--:|:--|
| **Q 36** | 0.9718 | 0.9880 | **−6.17** | **WEAK_ANCHOR (negative)** (rank 22/114 by abs delta) |

(Source: `h-new-590.json` `all_surahs_results`; entry `{"X":36, "window":[33,...,39], "d_W":0.9718, "d_W_minus_X":0.9880, "delta_pct":-6.17, "p_greater_W":0.2902, "classification":"WEAK_ANCHOR"}`.)

Removing Q 36 *raises* this window's mean distance by 0.016 — meaning Q 36's removal makes the rest of the [33-39] block *more* distinct from each other (the window opens up). In other words, **Q 36 acts as a content-cohesion-INCREASER for its 7-window**: the rest of the [33-39] zone (Q 33 al-Aḥzāb, Q 34 Sabaʾ, Q 35 Fāṭir, Q 37 al-Ṣāffāt, Q 38 ص, Q 39 al-Zumar) is internally a mixed Medinan-then-mid-Meccan-then-prophet-narrative span; Q 36 sits in the middle of that span and shares roots with multiple sub-clusters, "binding" the window.

This is the **opposite** of the Q 24 / Q 33 / Q 1 outlier-disruptor signature. Q 36 is the project's clearest **window-binder** in the top-50-mushaf zone: *not* a structural disrupter, but a structural integrator. The hadith-tradition centrality (*qalb al-Qurʾān*) maps onto an empirical role of *content-bridge* across heterogeneous neighbors, not the multi-axis "median-of-everything" reading H-NEW-82 falsified.

## 6. The 35→36 canonical-adjacency cost (rank 13/113)

Per `h-new-720.json` `per_adjacency`, the Q 35 → Q 36 transition is the 13th most-expensive of 113 adjacencies (delta = 0.1993, fraction-of-residual 2.40%). The Q 36 → Q 37 transition is rank 54 (delta = 0.0662, fraction 0.80%). **Q 36 is asymmetric: expensive to enter (top-15), cheap-to-mid to leave (mid-pack)**.

The cost rank 13 is consistent with a sharp transition between Q 35 Fāṭir (Meccan, but with creator-of-pairs / divine-attribute-emphasis content) and Q 36 Yāsīn (Meccan, narrative + eschatological). The mushaf "pays" some structural cost to put Q 36 here — but only on the entry side, and at rank 13 not the rank 5 or 11 of Q 24 al-Nūr's bracketing.

This cost-rank profile (one top-15 adjacency on the entry side; mid-pack on the exit side) is shared by Q 10 Yūnus (Q 9→Q 10 rank 4, Q 10→Q 11 rank ~80) and Q 50 ق (Q 49→Q 50 rank ~50, Q 50→Q 51 rank ~30). Q 36 fits into this **chronology-or-content-block-hinge** pattern at moderate magnitude.

## 7. Verse-level optimality — the H-NEW-127 result

Q 36 is one of the **5 surahs pre-registered for verse-level Fisher-Rao optimality** in [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] (`findings/phase-b-hypotheses/h-new-127-prereg.md` line 90 and corresponding findings file). The result for Q 36:

- **z = −2.82**, **permutation p = 0.0046** (10K perms, seed locked).
- Bonferroni-5 threshold α = 0.01; Q 36 PASSES.
- Verdict (per finding file): CONFIRMED — Q 36's verse-order is information-geodesically optimal at the verse scale, not just the surah scale.

This is a non-trivial empirical fact: at the verse-by-verse internal scale, Q 36's actual verse-order is closer to TSP-optimal-on-Fisher-Rao than 99.5% of random verse-permutations. The 4 of 5 surahs that PASS in H-NEW-127 are Q 2, Q 7, Q 12, Q 36. Q 55 al-Raḥmān is the FAILURE case (z = +5.39, REVERSED — al-Raḥmān's 31-refrain interleaving structure rewards permutations that cluster the refrain).

**The verse-level result is independent of the surah-level UAS rank 35/114.** Q 36 is verse-internally architectural even though it is mid-pack on the surah-level UAS.

## 8. Compression-tail position

Q 36 sits at s = 36, well *before* the Hijra-kink at s = 50 ([[h-new-660-compression-tail-gradient|H-NEW-660]]; [[h-new-700-phonological-compression-tail|H-NEW-700]]). The compression-tail laws are silent here by construction (slope-zero head zone). Q 36 belongs to the **mid-Meccan head-zone band** along with Q 10, Q 11, Q 12, Q 17, Q 18, Q 19, Q 20. Its mean content distance d̄ = 0.943 sits *just above* the head-zone typical d̄ ≈ 0.92-0.95 — Q 36 is content-MID for its head-zone position.

## 9. Architectural type classification

Per the project's three-class scheme ([[h-new-840-unified-architectural-score|H-NEW-840]], [[h-new-860-hadith-architectural-alignment|H-NEW-860]]):

- **Structural-iʿjāz** (al-Bāqillānī *iʿjāz al-fawāṣil*): high UAS + high sig_A → Q 33, Q 1, Q 2, Q 9.
- **Theological-iʿjāz / meaning-iʿjāz** (al-Khaṭṭābī *iʿjāz al-maʿnā*): low-or-mid UAS but high *thuluth-al-Qurʾān* / *qalb al-Qurʾān* / *al-Munjiya* status → Q 112, Q 114, **Q 36**, Q 67.
- **Anti-iʿjāz**: low on both axes → Q 87, Q 105, Q 73, Q 83.
- **Outlier-without-iʿjāz al-fawāṣil** (the Wave-B Q 24 cell): top-5 UAS via outlier + adjacency-cost, anti-fawāṣil.

Q 36 is **the canonical exemplar of the meaning-iʿjāz cell**: high hadith-fadāʾil score (10/10 — corpus-max tied with Q 1, Q 2, Q 67, Q 112), mid-pack UAS (35/114), anti-fawāṣil sig_A (rank 80/114), positive verse-level FR optimality (H-NEW-127 PASS), but NOT a multi-axis "heart" by H-NEW-82's quantitative test.

The mechanism: Q 36's value to classical liturgical practice is **theological** (compact resurrection-pericope + *kun fa-yakūn* climax + *qalb al-Qurʾān* hadith-warrant) and **liturgical** (recitation-on-the-dying tradition + Friday-evening tradition + *fadāʾil*-collection citation). It is NOT a structural-fāṣila virtuoso. The dual-iʿjāz typology in [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] is precisely the framework that resolves this: Q 36 wins on the al-Khaṭṭābī axis where it is mid on the al-Bāqillānī axis.

## 10. The kun-fayakūn corpus instance count (Q036-F-03 anchor)

The phrase *kun fa-yakūn* (كن فيكون) appears at exactly **8 verses** in the corpus (orthographic-exact match `كن فيكون`, computed `quran-text/quran-no-tashkeel.json`):

| # | Reference | Class |
|:-:|:--|:--|
| 1 | Q 2:117 | Medinan, creation-of-heavens-and-earth |
| 2 | Q 3:47 | Medinan, ʿĪsā-conception-by-Maryam |
| 3 | Q 3:59 | Medinan, ʿĪsā-as-Ādam-parallel |
| 4 | Q 6:73 | Late-Meccan, *al-ḥaqq*-discourse |
| 5 | Q 16:40 | Late-Meccan, theodicy-of-judgment |
| 6 | Q 19:35 | Mid-Meccan, ʿĪsā-as-servant-of-God |
| 7 | **Q 36:82** | **Mid-Meccan, resurrection-sealing-argument** |
| 8 | Q 40:68 | Late-Meccan, life-and-death-decree |

**Q 36:82 is the 7th of 8 corpus instances** (chronologically by mushaf order; revelation-order #41 places it between Q 19 (rev #44) and Q 40 (rev #60)). Critically, **Q 36:82 is the only *kun fa-yakūn* verse positioned at the rhetorical CLIMAX of its surah** — it appears as the second-to-last verse, sealing the resurrection argument. The 6 other instances are mid-surah didactic-doctrinal statements; Q 36:82 is the only *peroratio* placement.

This is the empirical content of the classical exegetical observation (al-Rāzī, *Mafātīḥ al-ghayb*, Q 36:82 commentary; al-Zamakhsharī, *al-Kashshāf*, Q 36:82 — see `03-tafsir-survey.md` §3) that Q 36 is "constructed around" the *kun fa-yakūn* climax. The position (verse 82 of 83) is structurally peroratio. See `06-novel-findings.md` Q036-F-03 for the pre-registered position-density-of-*kun-fa-yakūn* test.

## 11. Cross-references to all H-NEW findings touching Q 36

- [[h-new-82-yasin-heart|H-NEW-82]] — Q 36 NULL on 6/6 "heart" axes; binding prior. The empirical content centroid is Q 10 (lexical) / Q 46 (theme) / Q 57 (positional) / Q 112 (FR-distance).
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 36 mean FR distance to corpus = 0.9430 (rank 64/114); nearest = Q 25 (0.778), farthest = Q 55 (1.195).
- [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] — Q 36 verse-level FR optimality CONFIRMED at z = −2.82, p = 0.0046 (Bonferroni-5 PASS). One of 4 PASS surahs out of 5 pre-registered.
- [[h-new-134-mst-analysis|H-NEW-134]] — partial metric-specific rehabilitation of Q 36 centrality at MST-distance level (does NOT override H-NEW-82 NULL).
- [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] — YS-letter-centroid maps to ḤM-cluster centroid; classically-plausible alternate interpretation under "heart of the Qurʾān" framing.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 36 WEAK_ANCHOR (negative), Δ = −6.17 pp; window-binder, not window-disrupter.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — pre-kink head-zone position s = 36; near-monorhyme on -ūn/-īn (84% nūn-final).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 35 → Q 36 = 0.1993 (rank 13/113); Q 36 → Q 37 = 0.0662 (rank 54/113); asymmetric expensive-to-enter cheap-to-leave.
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A = −0.7238 (rank 80, anti-structural-iʿjāz); sig_B = −1.0711 (rank 85, anti-rhyme-purity); rhyme entropy 0.477 nats (z = −0.531, near-monorhyme).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS = 0.5040 (rank 35/114); component breakdown: abs_outlier = 6.17, max_cost = 0.1993, abs_ijaz = 0.724.
- [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — Q 36 hadith-fadāʾil 10/10 (top tier, *qalb al-Qurʾān*) but UAS rank 35 — listed as a "most-striking divergence" in H-NEW-860's verdict-block.
- [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] — surah-internal verse-level information-geodesic optimality CONFIRMED.
- [[cross-finding-014-five-principle-unified-equation|cross-finding-014]] — Q 36 listed as a residual (R3: "Q 36 MST centroid"); single metric-specific observation noted, NOT promoted to law.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 36 = canonical exemplar of the **meaning-iʿjāz / theological-iʿjāz cell** of the dual-iʿjāz typology.

## 12. Honest limits

- The "rank 35/114" UAS claim is descriptive, not inferential. The H-NEW-840 UAS is a z-sum of three correlated axes; it has no Bonferroni significance test of its own (see [[h-new-840-unified-architectural-score|H-NEW-840]] §5).
- The H-NEW-82 NULL verdict is **rules-tuple-stable across 6 axes** but is restricted to the operationalisations the pre-reg locked. The operationalisations explicitly excluded by H-NEW-82 (resurrection-pericope-length, recitational-frequency-weighted-centrality, information-density-per-word) are not addressed by that prior. Q036-F-01 in `06-novel-findings.md` re-tests one of those (recitational-frequency-weighted-centrality) under independent locked pre-reg.
- The "Q 35→Q 36 cost rank 13" depends on the 2-opt heuristic's `L_2opt` baseline. A tighter solver might shift the residual by a few percent, but the rank order of the top-15 expensive adjacencies is robust across the 50 restart seeds reported in H-NEW-720.
- The "Q 36 mean FR distance 0.943, rank 64" is calculated only over the no-tashkeel root-distribution variant; under different tokenization the rank can shift modestly. The *direction* — Q 36 is near corpus median — is rules-tuple stable under all tested variants.
- The rhyme entropy 0.477 nats places Q 36 mid-pack; this is *near-monorhyme* but not extreme. The substantive claim — that Q 36 is dominantly nūn-final but mixed -ūn/-īn/-ān-end — is robust.
- The 84.34% nūn-final figure (`h-new-750.json`) is rules-tuple stable across no-tashkeel and min-tashkeel variants (computed). Under full-tashkeel some -ūna ↔ -ūn variation exists at pause; not material to the rank.
- The H-NEW-127 result is **only one of 5 surahs tested in that pre-reg**; it is not a cross-corpus law. The verse-level optimality is a per-surah CONFIRMED observation, not a universal claim.

## 13. One-paragraph synthesis

Q 36 Yāsīn is the **canonical exemplar of meaning-iʿjāz / theological-iʿjāz without high structural-iʿjāz**. The mushaf places it at index 36 — embedded in a mid-Meccan zone (Q 33-39) where it is the *least* outlier-disrupting surah of its 7-window (Δ = −6.17 pp WEAK_ANCHOR), acting as a **content-bridge** across heterogeneous neighbors rather than a content-disrupter — and pays a top-15 entry-cost (Q 35→Q 36 rank 13/113, 2.40% of TSP residual) for this position with a cheap-to-mid exit. Its FR-distance signature places it close to Q 25, Q 43, Q 67, Q 23, Q 15 (Meccan, prophet-narrative + scripture-announcement + eschatological-cosmic) and farthest from Q 55 al-Raḥmān (the corpus's top-sig_A monorhyme surah) — content-pole for the prophet-narrative-and-resurrection axis. UAS rank 35/114 places Q 36 firmly mid-pack, well below the structural-iʿjāz top-9. The classical *qalb al-Qurʾān* claim was empirically tested and falsified at multi-axis quantitative form by [[h-new-82-yasin-heart|H-NEW-82]] (0/6 axes top-5; the empirical positional median is Q 57, the lexical centroid is Q 10, the theme centroid is Q 46, the FR centroid is Q 112). What survives is the **classical-liturgical-theological centrality**: Q 36 is among the corpus-max 10/10 fadāʾil surahs in the project's hadith-rubric ([[h-new-860-hadith-architectural-alignment|H-NEW-860]]), and it ranks rank 35 on UAS — the project's single largest hadith-vs-architecture divergence in raw rubric terms after the muʿawwidhāt. **Q 36 is the *liturgical* heart, NOT the *structural* heart**, and the dual-iʿjāz typology of [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] is precisely the framework that vindicates Q 36's qualitative classical reception while honoring the multi-axis quantitative NULL.
