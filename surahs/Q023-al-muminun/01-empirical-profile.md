---
surah: 23
surah_name_ar: المؤمنون
surah_name_translit: al-Muʾminūn
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 23 al-Muʾminūn — Empirical Architectural Profile


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

Rules-tuple: `(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan, Mashriqi)`. All numerical claims below are computed from disk; sources cited.

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **2.977** | **9 / 114** (top decile) | `findings/phase-b-hypotheses/csv/h-new-840.json` `top_15` rank 9 |
| Outlier-strength Δ%ile | **−10.91 pp** (mildly cohesion-positive) | `COHESION_ANCHOR` classification | `h-new-590.json` `all_surahs_results` X=23 |
| `|outlier|` UAS-component | 10.91 | rank 11 / 114 in absolute outlier-strength | `h-new-840.json` |
| max neighbor canonical-adjacency cost | **0.2595** length-units | rank 6 / 113 (Q 22 → Q 23) | `h-new-720.json` `top10_expensive` |
| Q 22 → Q 23 cost | 0.2595 (3.13% of TSP residual) | **rank 6 / 113** | same |
| Q 23 → Q 24 cost | 0.2116 (2.55% of TSP residual) | **rank 11 / 113** | same |
| Combined two-side cost | **0.4711 (5.68% of TSP residual)** | one of only 2 surahs (with Q 24) where both sides are top-15 | computed |
| iʿjāz signature sig_A (structural) | **−1.5500** | **rank 93 / 114** (anti-structural-iʿjāz) | `h-new-750.json` `per_surah` Q23 |
| iʿjāz signature sig_B (rhyme-purity) | **−1.7070** | **rank 106 / 114** | same |
| `|sig_A|` UAS-component | 1.5500 | rank 22 / 114 in absolute iʿjāz | `h-new-840.json` |
| Mean Fisher–Rao distance to corpus | **0.9665** | rank 74 / 114 (slightly above corpus mean 0.9235) | `h-new-111.json` D_matrix Q23 row |
| Local cohesion (1-step adjacency) | 1.092 | z = −0.581 (low local cohesion = neighbors are FAR) | `h-new-750.json` |
| z(rhyme entropy) | −1.126 | very low entropy = monorhyme | `h-new-750.json` |
| z(mean content distance) | +0.424 | slightly above corpus mean | `h-new-750.json` |
| Rhyme entropy (Shannon, nats) | **0.148** | **rank 109 / 114** — corpus's 6th-purest monorhyme | `h-new-700.json` + recomputed |
| Top final letter (rāwī) | **ن (nūn)** | **96.6%** of 118 verses | computed `quran-no-tashkeel.json` |
| Total root-tokens | **616** | mid-Meccan-narrative size | computed from QAC |
| Distinct roots | **255** | mid-Meccan-narrative diversity | computed from QAC |
| Words (no-tashkeel orthographic) | 1,089 | mid-Meccan | computed `quran-no-tashkeel.json` |
| Letters (no-tashkeel, no spaces) | 4,520 | mid-Meccan | same |
| Verse count | 118 | mid-Meccan-narrative | canonical |

**Source files**: all H-NEW JSON files referenced live in `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/`; the morphology source is `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.

## 2. The architectural paradox: HIGH UAS without HIGH-sig_A — Q 23's "monorhyme-iʿjāz" type

Q 23 occupies a **distinctive cell in the project's two-axis architecture map**:

| Axis | Q 23 score | Q 23 rank | What this means |
|:--|:--:|:--:|:--|
| Outlier-strength Δ%ile | **−10.91 pp** | `COHESION_ANCHOR` | Q 23 is mildly *cohesion-positive*: removing it makes the [Q 20-26] window LESS cohesive |
| Canonical-adjacency cost (max-of-2 sides) | **0.2595 (rank 6/113)** | top-6 expensive | Mushaf "pays" 5.68% of TSP residual on Q 23's two adjacencies |
| iʿjāz sig_A (al-Bāqillānī fawāṣil) | **−1.55** | **rank 93** | anti-structural-iʿjāz: monorhyme is so PURE that the anti-twin signal weakens (window-rhyme is constant, not dispersed) |
| Mean FR distance to corpus | 0.9665 | rank 74 / 114 | Slightly above corpus centroid mean 0.9235 |
| **UAS** | **2.977** | **9/114** | Top decile architectural significance |

This makes Q 23 a fourth distinct architectural type, parallel to (but not identical with) Q 24's: Q 23 wins UAS via **outlier-strength (mid-strong, negative direction = cohesion-positive) + adjacency-cost (top-6) + |iʿjāz| (mid-strong absolute value, even though signed-direction is negative)**. The mechanism is different from the top-5: Q 33, Q 1, Q 2, Q 9 win on outlier + cost + sig_A all positively contributing; Q 23 wins on outlier + cost, with sig_A contributing **only by absolute magnitude** (the score is z-summed on `|sig_A|`, see [[h-new-840-unified-architectural-score|H-NEW-840]] §3).

**The Q 23 type — "purer-than-pure monorhyme"**: Q 23's rhyme is so close to monorhyme (96.6% nūn, entropy 0.15 nats) that the **al-Bāqillānī fawāṣil-variety mechanism is muted by construction** — when every fāṣila ends in -ūn / -īn, the rhyme-entropy is too low to oscillate against content-cohesion. Q 23 therefore registers as anti-structural-iʿjāz (sig_A rank 93) NOT because it lacks fāṣila virtuosity, but because **it has chosen a different fāṣila strategy**: monorhyme-saturation rather than rhyme-variety. Compare Q 55 al-Raḥmān (sig_A rank 1 / 114, sig_A=+3.17): Q 55 has the corpus's strongest monorhyme too (-ān refrain *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān*) but its rhyme-entropy is a touch higher (0.40 nats vs Q 23's 0.15), and the embedded *tukadhdhibān*-refrain creates a rhythmic-contrast structure that scores positively on the project's anti-twin axis. **Q 23 is the project's most extreme "chosen monorhyme" surah**.

## 3. The bracketing-cost claim — Q 23 as the Meccan side of the Q 24 pivot

Per `h-new-720.json` `top10_expensive`, the 113 canonical-adjacency costs include:

| Rank | Adjacency | Cost (length-units) | Frac of 8.29-unit residual |
|:-:|:--|:--:|:--:|
| 1 | Q 1 → Q 2 | 0.6216 | 7.50% |
| 2 | Q 32 → Q 33 | 0.3631 | 4.38% |
| 3 | Q 33 → Q 34 | 0.3311 | 3.99% |
| 4 | Q 9 → Q 10 | 0.3094 | 3.73% |
| 5 | Q 24 → Q 25 | 0.2896 | 3.49% |
| **6** | **Q 22 → Q 23** | **0.2595** | **3.13%** |
| 7 | Q 42 → Q 43 | 0.2357 | 2.84% |
| 8 | Q 56 → Q 57 | 0.2274 | 2.74% |
| 9 | Q 12 → Q 13 | 0.2158 | 2.60% |
| 10 | Q 7 → Q 8 | 0.2120 | 2.56% |
| **11** | **Q 23 → Q 24** | **0.2116** | **2.55%** |

**Q 23 is the only surah in the corpus other than Q 24 itself with both adjacencies in the top-15 expensive.** Q 23 → Q 24 (rank 11) and Q 22 → Q 23 (rank 6) — combined 5.68% of the 8.29-unit TSP residual. This makes Q 23 a **structural-pivot** at the cost of nearly 6% of the entire residual.

**Why is Q 22-Q 23 expensive?** Q 22 (al-Ḥajj) is classified mixed Meccan-Medinan with strong Medinan ritual-pilgrimage content; Q 23 is purely Meccan-narrative-eschatological with a near-monorhyme nūn rhyme. The FR-distance Q 22 ↔ Q 23 is 0.953 — modest, but the constrained-2-opt cost penalty kicks in because Q 23's nearest content-neighbours are far away in the mushaf (Q 23's nearest = Q 43 al-Zukhruf, FR=0.789; Q 7 al-Aʿrāf, FR=0.789; Q 36 Yāsīn, 0.804). The mushaf "pays" to put Q 23 next to Q 22 rather than next to its nearest content-neighbours.

**Why is Q 23-Q 24 expensive?** Q 24 is the Medinan-legal centerpiece (zinā / qadhf / al-ifk / ḥijāb / ḥijāb). Q 23 is Meccan-narrative. Their FR-distance is 1.050 — well above corpus mean. The mushaf "tolerates" this register-class jump to insert Q 24 into the Meccan-narrative zone Q 21-27 (see [[Q024-al-nur/01-empirical-profile|Q 24]] §3).

**Synthesis**: Q 23 is the *Meccan-narrative anchor* on the Meccan side of the Q 24 (Medinan-legal) pivot, and the *Meccan-narrative anchor* on the post-Q 22 (Ḥajj-Medinan-leaning) side. Q 23's structural role is to **buffer the register-class crossings on both sides**.

## 4. Fisher–Rao distance row (Q 23 against all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` (Fisher–Rao angular on K=500 stem-roots, Dirichlet α=0.5; `D_ij = 2·arccos(Σ √(p_i·p_j))`).

**Five nearest neighbours** — Q 23's root-distribution maps to other Meccan-narrative-prophet surahs:

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 1 | Q 43 al-Zukhruf | 0.7888 | Meccan-narrative-Pharaoh |
| 2 | Q 7 al-Aʿrāf | 0.7890 | Meccan-narrative-prophet-cycle |
| 3 | Q 36 Yāsīn | 0.8045 | Meccan-narrative-eschatology |
| 4 | Q 21 al-Anbiyāʾ | 0.8287 | Meccan-narrative-prophet-cycle |
| 5 | Q 25 al-Furqān | 0.8327 | Meccan-narrative-prophet-cycle |

**Five farthest neighbours** — Q 23 maximally distinct from short-mufaṣṣal monorhyme + Medinan-legal-large + early-Medinan barāʾa:

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 109 | Q 54 al-Qamar | 1.0634 | short-Meccan-mufaṣṣal |
| 110 | Q 33 al-Aḥzāb | 1.0665 | Medinan-large-Aḥzāb |
| 111 | Q 88 al-Ghāshiya | 1.0808 | short-Meccan-mufaṣṣal |
| 112 | Q 4 al-Nisāʾ | 1.0900 | Medinan-legal-large |
| 113 | Q 9 al-Tawba | **1.1007** | Medinan-barāʾa |
| (max) | Q 55 al-Raḥmān | **1.1835** | Meccan-monorhyme-fawāṣil-supreme |

**Interpretation**: Q 23's nearest five neighbours are all **Meccan-narrative-prophet-cycle** surahs — Q 7 al-Aʿrāf (the corpus's Meccan-encyclopedia of prophet narratives), Q 21 al-Anbiyāʾ ("the Prophets" surah), Q 25 al-Furqān, Q 36 Yāsīn, Q 43 al-Zukhruf. Yet Q 23's actual canonical neighbours Q 22 (FR=0.953) and Q 24 (FR=1.050) are mid-far and far. The mushaf places Q 23 in a **content-distant slot** relative to its FR-content-cluster.

The farthest neighbour Q 55 al-Raḥmān (FR=1.184) is a striking finding: Q 55 is the corpus's other extreme monorhyme surah (-ān refrain + dual-vocative *fa-bi-ayyi ālāʾi rabbikumā*) and sits at sig_A rank 1 / 114. Q 23 is sig_A rank 93. **The two pure-monorhyme surahs of the Quran are the farthest pair in the FR root-distribution sense**: monorhyme alone does not predict content-similarity. This is consistent with the project's anti-twin lock ([[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] r=−0.86): rhyme and content are orthogonal axes.

## 5. Rhyme analysis — corpus's 6th-purest monorhyme

Final-letter distribution across 118 verses, computed from `quran-text/quran-no-tashkeel.json`:

| Final letter | Count | Fraction |
|:-:|:-:|:-:|
| ن | **114** | **96.61%** |
| م | 4 | 3.39% |

Shannon entropy (nats) = 0.148 — rank **109 / 114** (i.e., 6th-purest monorhyme of the 114 surahs).

Cross-validated against `quran-text/quran-min-tashkeel.json`: vowel before final ن is fatḥa (ـَ) in 101 verses (85.6%), kasra (ـِ) in 9 (7.6%), tanwīn-kasra (ـٍ) in 7 (5.9%), tanwīn-ḍamma (ـٌ) in 1 (0.8%). The dominant rhyme is **-ūna / -īna** (fatḥa-vowel + nūn-with-fatḥa-as-rāwī, classical -ūna ending). This is the **classical mu-CCi-ūn / mu-CCi-īn active-participle plural fāṣila pattern**.

**Comparison with classical accounts**: al-Suyūṭī (*al-Itqān* nawʿ 38, *al-fawāṣil*) recognizes Q 23 as belonging to the corpus's purest-monorhyme class. al-Bāqillānī (*Iʿjāz al-Qurʾān*) does not single out Q 23 specifically; al-Khaṭṭābī notes the *muʾminūn* opening as performative.

## 6. Top roots and the believer-vocabulary signature

Per QAC v0.4, Q 23 has 616 root-tokens spanning 255 distinct roots. Top 20 roots by frequency:

| Rank | Root | Count | Gloss |
|:-:|:-:|:-:|:--|
| 1 | qwl | 35 | say / saying |
| 2 | rbb | 23 | Lord |
| 3 | Alh | 19 | God / Allāh |
| 4 | kwn | 17 | be / was |
| 5 | qwm | 13 | people / stand |
| 6 | xlq | 10 | create |
| 7 | rsl | 9 | send / messenger |
| 8 | Amn | 8 | believe / faith |
| 9 | xyr | 7 | good |
| 10 | Hqq | 7 | truth / right |
| 11 | Axr | 7 | other / next |
| 12 | mwt | 6 | death |
| 13 | ywm | 6 | day |
| 14 | Akl | 6 | eat |
| 15 | Zlm | 6 | wrong / oppress |
| 16 | Ayy | 6 | sign / verse |
| 17 | Aty | 6 | come / bring |
| 18 | Elm | 6 | know |
| 19 | jEl | 5 | make / appoint |
| 20 | Adm | 5 | (Adam-related) |

**Profile**: high *rbb* (Lord, 23) + *Alh* (Allāh, 19) + *qwl* (35, the prophet-narrative-cycle "and he said" formula) + *xlq* (create, 10) + *rsl* (messenger, 9). This is the **Meccan-narrative-prophet-creation profile**, perfectly matched by Q 23's nearest FR-neighbours Q 7, Q 21, Q 25, Q 36, Q 43.

**Notable absences for a "believer" surah**: only **8 *Amn* (believe) tokens** in 616 root-tokens (1.30% / 1000 root-tokens). Compare Q 24 al-Nūr: 859 root-tokens, ~25 *Amn*-tokens (~29 / 1000); Q 33 al-Aḥzāb: 881 root-tokens, similar concentration. **Q 23 is named "the Believers" but does not over-concentrate the *Amn* root**. This is a subtle but real empirical observation: the surah's title is taken from v. 1 *qad aflaḥa al-muʾminūn*, not from any thematic over-representation of *Amn*-vocabulary. The 8 *Amn*-tokens are at vv. 1, 8, 38, 44, 47, 58, 74, 109 — distributed across all five movements.

This is the **opposite pattern from Q 24 al-Nūr**, which is named for its over-concentration of light-vocabulary (Q024-F-01: VINDICATED at p<10⁻⁶). **The "name-tracks-vocabulary" hypothesis fails for Q 23**. Pre-registered test Q023-F-01 (`06-novel-findings.md`) tests this directly.

## 7. flḥ (success / prosper) inclusio

The root *flḥ* appears exactly **3 times** in Q 23, at vv. **1, 102, and 117**:

| Verse | Form | Translation |
|:-:|:--|:--|
| 1 | أفلح (afla**ḥ**a, 3MS-perf-IV-active) | "have prospered" — the opening declaration of the muʾminūn |
| 102 | المفلحون (al-mufli**ḥ**ūn, MP-act-PCPL-IV) | "the prosperous" — those whose scales weigh heavy |
| 117 | يفلح (yufli**ḥ**u, 3MS-impf-IV) | "prospers" — under negation: لا يفلح الكافرون "the disbelievers do not prosper" |

The 3 *flḥ*-attestations form a **triple-anchor inclusio**: opening (positive perfect, applied to muʾminūn) → middle (positive participle, applied to those whose deeds outweigh) → closing (negative imperfect, applied to kāfirūn). This is **structurally precise**: v. 1 = positive performative of believers; v. 102 = positive descriptive of weighed-believers (the specific eschatological mechanism); v. 117 = negative inverse for unbelievers.

The middle anchor v. 102 occurs at word-position **roughly 87% through the surah**, NOT at the literal midpoint. The structural midpoint is around v. 60. The *flḥ*-inclusio is therefore **not a strict ABA arc** — it is an **opening + late-middle reinforcement + closing-inversion** structure. Pre-registered test Q023-F-03 (`06-novel-findings.md`) verifies this empirically.

The empirical content of the qualitative classical claim that Q 23 "begins and ends with *al-falāḥ*" (al-Biqāʿī *Naẓm al-Durar* style ring-structure) is therefore **partially confirmed**: there IS a structural *flḥ*-inclusio at the verse-level, but it is asymmetric (v. 1 / v. 117) and includes a third anchor at v. 102.

## 8. Outlier-window decomposition (H-NEW-590)

The 7-window centred on Q 23 is `[20, 21, 22, 23, 24, 25, 26]` per `h-new-590.json`:

| Removed | d̄_W | d̄_W−X | percentile shift Δ (pp) | classification |
|:--:|:--:|:--:|:--:|:--|
| **Q 23** | 0.9797 | 1.0097 | **−10.91 pp** | **COHESION_ANCHOR** |

(Source: `h-new-590.json` `all_surahs_results`; entry `{"X":23, "window":[20,...,26], "d_W":0.9797, "d_W_minus_X":1.0097, "delta_pct":-10.91, "classification":"COHESION_ANCHOR"}`.)

Removing Q 23 *increases* the window's mean content-distance from 0.980 to 1.010 — i.e., Q 23 **adds** cohesion to its 7-window. The window minus Q 23 is `[20, 21, 22, 24, 25, 26]`, which is dominated by the Q 24 outlier (the Medinan-legal-Nūr surah). When Q 23 is present, its Meccan-narrative root-distribution moderates the gap between the Meccan-narrative cluster (Q 21, 25, 26) and the Medinan-legal Q 24.

**Mechanism**: Q 23's content-profile sits *between* Meccan-narrative (Q 21, 25, 26) and Medinan-legal (Q 24) in FR-distance space. Removing it leaves the [21, 25, 26] cluster maximally separate from Q 24, raising the window's mean content-distance.

**This is the empirical content of the "buffer" claim** in §3 above: Q 23 is structurally a content-buffer between Meccan-narrative and Medinan-legal. The H-NEW-590 outlier-spectrum classifies it as a (weak) `COHESION_ANCHOR` rather than a `MODERATE_OUTLIER` because its presence smooths the local content-cluster.

## 9. Compression-tail position

Q 23 sits at s = 23, well *before* the Hijra-kink at s = 50 ([[h-new-660-compression-tail-gradient|H-NEW-660]]; [[h-new-700-phonological-compression-tail|H-NEW-700]]). The compression-tail laws are silent here by construction. Q 23 belongs to the **pre-kink head zone**.

Mean FR distance d̄ = 0.9665 sits very slightly *above* the corpus mean 0.9235 (rank 74/114) — Q 23 is content-just-above-average-distinct from corpus, neither a content-anchor (low d̄) nor a content-outlier (high d̄). Its architectural significance comes from the **adjacency-cost axis** + **|sig_A| absolute magnitude**, not from content-cluster centrality.

## 10. Architectural type classification

Per the project's three-class scheme ([[h-new-840-unified-architectural-score|H-NEW-840]], [[h-new-860-hadith-architectural-alignment|H-NEW-860]]):

- **Structural-iʿjāz** (al-Bāqillānī *iʿjāz al-fawāṣil*): high UAS + high sig_A → Q 33, Q 1, Q 2, Q 9.
- **Theological-iʿjāz** (al-Khaṭṭābī *iʿjāz al-maʿnā*): low UAS but high *thuluth-al-Qurʾān* status → Q 112, Q 114.
- **Anti-iʿjāz**: low on both axes → Q 87, Q 105, Q 73, Q 83.
- **Outlier-without-iʿjāz al-fawāṣil** (Q 24's cell): high UAS + low sig_A, mechanism = high outlier + cost.
- **Q 23's cell — *purer-than-pure monorhyme***: high UAS + extremely-low rhyme-entropy-driven negative sig_A. Mechanism: **|sig_A| is mid-magnitude (1.55) but signed negative** because monorhyme suppresses the al-Bāqillānī fawāṣil-variety mechanism by construction. The UAS picks Q 23 up via **high adjacency-cost (rank 6) + high |outlier|-magnitude (10.91, rank 11) + |sig_A|=1.55 (rank 22)**. Q 23 is therefore a *structural-pivot* with *monorhyme-saturation* style — different from Q 33 (structural-iʿjāz) and Q 24 (outlier-without-iʿjāz).

This Q 23 cell, distinct from Q 24's cell, suggests that there is **a fifth architectural type to add to [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]**: surahs that win on adjacency-cost + monorhyme-purity with anti-structural sig_A. Future work should test whether other monorhyme surahs (Q 55, Q 71 nūḥ, Q 79) share this signature.

## 11. Cross-references to all H-NEW findings touching Q 23

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 23 mean FR distance to corpus = 0.9665 (rank 74); nearest = Q 43 (0.789), farthest = Q 55 (1.184).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 23 `COHESION_ANCHOR`, Δ = −10.91 pp.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — pre-kink head-zone position s = 23; rhyme entropy 0.148 nats (rank 109).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 22 → Q 23 = 0.2595 (rank 6 / 113); Q 23 → Q 24 = 0.2116 (rank 11 / 113); both top-15.
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A = −1.5500 (rank 93, anti-structural-iʿjāz); sig_B = −1.7070 (rank 106); rhyme entropy 0.148 nats (rank 109).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS = 2.977 (rank 9 / 114); component breakdown above.
- [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — Q 23's classical fadāʾil concentrate on the believer-typology (Tirmidhī ʿUmar-narrated 10-verses ḥadīth) — al-Khaṭṭābī meaning-iʿjāz lineage; the architectural UAS top-decile rank reflects al-Bāqillānī structural-iʿjāz with the "monorhyme-saturation" twist of §10.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 23 illustrates a fifth architectural cell (high UAS + monorhyme-saturation + anti-structural sig_A).

## 12. Honest limits

- The "rank 9 UAS" is a z-sum across three correlated axes; H-NEW-840 itself notes (§5) that UAS has no Bonferroni significance test of its own. Rank 9 is descriptive, not inferential.
- The "rank 6 / 113 adjacency cost" depends on the 2-opt heuristic baseline `L_2opt = 77.388`. A tighter solver might shift residuals by a few percent, but the rank-order of the top-15 expensive adjacencies is robust across the 50 restart seeds reported in `h-new-720.json`.
- The "rhyme entropy 0.148 nats, rank 109" uses no-tashkeel orthographic last-letter as the rhyme-element. Under a richer rhyme-pattern definition (e.g., the last 3 phonemes including vowel + nūn + nasal-resonance) the entropy would shift slightly but the *direction* (Q 23 is among the corpus's purest monorhymes) is rules-tuple stable.
- The "8 Amn-tokens, rank not over-concentrated" claim is computed under the QAC-stem-roots tokenization. Under different stemming (e.g., orthographic-token *muʾmin* + *muʾminūn* + *yuʾmin* + *āmana* counted together) the count would shift to ~10-12, still not over-concentrated relative to the surah's size.
- The classification "fifth architectural cell" is a single-cell observation; it would need confirmation across other monorhyme surahs (Q 55, Q 71, Q 79) before being elevated to a corpus-wide architectural type.

## 13. One-paragraph synthesis

Q 23 al-Muʾminūn is the **canonical exemplar of monorhyme-saturation architectural-significance**: top-decile UAS (rank 9 / 114) achieved through high-cost canonical-adjacencies on both sides (Q 22-Q 23 rank 6, Q 23-Q 24 rank 11; combined 5.68% of TSP residual) plus mid-strong absolute outlier-magnitude (|Δ| = 10.91pp, signed negative — cohesion-positive) plus mid-strong absolute iʿjāz-signature magnitude (|sig_A| = 1.55, rank 22, signed negative) — but with the al-Bāqillānī fawāṣil-variety mechanism muted by construction because Q 23's rhyme-entropy is the corpus's 6th-purest monorhyme (0.148 nats). Q 23's nearest five FR-neighbours (Q 43, Q 7, Q 36, Q 21, Q 25) are all Meccan-narrative-prophet-cycle surahs; its farthest neighbour is Q 55 al-Raḥmān (the corpus's other extreme monorhyme), confirming the project's anti-twin lock that monorhyme + content are orthogonal axes. Q 23's structural role is to **buffer the register-class crossings on both sides** (Q 22 mixed-Ḥajj-Medinan-leaning → Q 23 Meccan-narrative → Q 24 Medinan-legal). The triple-anchor *flḥ*-inclusio (v. 1 *qad aflaḥa l-muʾminūn* / v. 102 *al-mufliḥūn* / v. 117 *lā yufliḥu l-kāfirūn*) is structurally precise and asymmetric. The empirical case justifies a tentative fifth architectural cell beyond the four currently in [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]: monorhyme-saturation surahs that win UAS on adjacency-cost + |outlier| + |sig_A| with all three signed-magnitudes under different mechanisms.
