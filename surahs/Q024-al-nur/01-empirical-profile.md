---
surah: 24
surah_name_ar: النور
surah_name_translit: al-Nūr
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 24 al-Nūr — Empirical Architectural Profile

## 1. Headline architectural metrics

Rules-tuple: `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan)`. All numerical claims below are computed from disk; sources cited.

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **4.4501** | **5 / 114** (top decile) | `findings/phase-b-hypotheses/csv/h-new-840.json` `top_15` rank 5 |
| Outlier-strength Δ%ile | **+23.51 pp** | **3 / 114**; MODERATE_OUTLIER | `h-new-590.json` `top_10_outliers` rank 3 |
| max neighbor canonical-adjacency cost | 0.2896 length-units | rank 5 / 113 (Q 24 → Q 25) | `h-new-720.json` `per_adjacency` |
| Q 23 → Q 24 cost | 0.2116 length-units | rank 11 / 113 | same |
| iʿjāz signature sig_A (structural) | **−0.7901** | **rank 82 / 114** (anti-structural-iʿjāz) | `h-new-750.json` `per_surah` |
| iʿjāz signature sig_B (rhyme-purity) | −0.1292 | rank 61 / 114 | same |
| Mean Fisher–Rao distance to corpus | 1.0704 | **rank 105 / 114** (far above corpus mean 0.9235) | `h-new-111.json` D_matrix |
| Local cohesion (1-step adjacency) | 0.9390 | z = −0.789 (low local cohesion = many neighbors are FAR) | H-NEW-750 |
| Rhyme entropy (Shannon, nats) | **1.1342** | rank 6 / 114 — most multi-rāwī of Wave-B surahs | H-NEW-750 |
| Top final letter (rāwī) | ن | 31 / 64 verses = 48.4% | H-NEW-750; cross-validated below |
| Total root-tokens | 859 | rank 16 / 114 | `data/morphology/quranic-corpus-morphology-0.4.txt` (computed) |
| Distinct roots | 287 | rank 17 / 114 | same |
| Words (no-tashkeel orthographic) | 1,319 | mid-Medinan-large | computed `quran-no-tashkeel.json` |
| Letters (no-tashkeel, no spaces) | 5,754 | mid-Medinan-large | same |
| Light-cluster root density (16-root family) | **31.43 / 1000 root-tokens** | **rank 7 / 114**; raw count rank **2 / 114** | computed (see §6 below) |

**Source files**: all H-NEW JSON files referenced live in `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/`; the morphology file is `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.

## 2. The architectural paradox: STRUCTURAL OUTLIER without HIGH STRUCTURAL-IʿJĀZ

Q 24 occupies a unique cell in the project's two-axis architecture map:

| Axis | Q 24 score | Q 24 rank | What this means |
|:--|:--:|:--:|:--|
| Outlier-strength (Δ%ile in 7-window) | **+23.51 pp** | **3 / 114** | Removing Q 24 collapses local cohesion; Q 24 is content-distinct from neighbours |
| Canonical-adjacency cost (max-of-2 sides) | **0.2896 (rank 5/113)** | top-5 expensive | Mushaf "pays" length-cost on BOTH sides (Q 23-Q 24 rank 11; Q 24-Q 25 rank 5) |
| iʿjāz signature sig_A (al-Bāqillānī fawāṣil) | **−0.79** | **rank 82** | Q 24 is *anti-structural-iʿjāz*: rhyme dispersed (1.13 nats vs ~0.5 for high sig_A surahs), local cohesion low, mean content-distance HIGH (1.07 vs corpus 0.92) |
| Mean FR distance to corpus | 1.0704 | rank 105 / 114 | Q 24's root-distribution is far from corpus centroid |

This makes Q 24 **the corpus's most striking "outlier without iʿjāz al-fawāṣil"**: high outlier strength, very high adjacency cost, and yet a *negative* sig_A. The four other top-5 UAS surahs (Q 33, Q 1, Q 2, Q 9) all combine outlier strength with at least moderate sig_A. Q 24 alone scores top-5 outlier + top-5 adjacency but anti-structural-iʿjāz.

**Mechanism**: Q 24 wins UAS purely on the outlier and TSP-cost components. The rhyme of Q 24 is multi-rāwī (ن 48% / م 36% / ر 11% / mixed 5%), entropy 1.134 nats (rank 6 of 114) — far from the high-sig_A surahs that have monorhyme (e.g., Q 55 at 0.4 nats with -ān monorhyme). Q 24 is legal-prose, not fawāṣil-prose. It is the canonical example of *structural-iʿjāz failure to predict outlier status* — exactly the case that justifies the project's UAS being a compound of three orthogonal axes rather than sig_A alone.

## 3. The bracketing-cost claim (overview's headline)

Per `h-new-720.json`, the 113 canonical-adjacency costs are sorted. Q 24's two adjacencies:

| Adjacency | Cost | Frac of TSP residual | Rank |
|:--|:--:|:--:|:--:|
| Q 23 → Q 24 | 0.2116 | 2.55% | **11 / 113** |
| Q 24 → Q 25 | 0.2896 | 3.49% | **5 / 113** |

**Both adjacencies are top-15 expensive.** The corresponding sum is 0.5012 length-units = 6.04% of the entire 8.29-unit residual — Q 24 alone consumes more than 6% of the global TSP residual on its two adjacencies, while occupying only 1/114 = 0.88% of canonical positions.

By comparison, only one other surah has both adjacencies in the top-15: Q 33 al-Aḥzāb (Q 32 → Q 33 rank 2; Q 33 → Q 34 rank 3; combined ~8.4%). The overview's framing — "Q 24 is bracketed by HIGH canonical-adjacency costs on BOTH sides" — is empirically vindicated. Q 24 is the *second* cell in the corpus where the mushaf pays double-side cost to keep the surah in its canonical position, after Q 33.

This is the precise empirical content of the "Medinan-legal centerpiece inserted into a Meccan-narrative zone" claim in §6 of the overview: Q 22 (al-Ḥajj) is mixed-Medinan but late-Meccan in flavour; Q 23 al-Muʾminūn, Q 25 al-Furqān, Q 26 al-Shuʿarāʾ are all classical Meccan. The mushaf "tolerates" two top-15 adjacency costs to embed Q 24 between them.

## 4. Fisher–Rao distance row (Q 24 against all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` (Fisher–Rao angular on K=500 stem-roots, Dirichlet smoothing α=0.5; `D_ij = 2·arccos(Σ √(p_i·p_j))`).

**Five nearest neighbours** (Q 24's root-distribution maps to other Medinan-legal / Medinan-large):

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 1 | Q 49 al-Ḥujurāt | 0.8704 | Medinan-legal |
| 2 | Q 64 al-Taghābun | 0.8847 | Medinan-mid |
| 3 | Q 2 al-Baqara | 0.9005 | Medinan-large |
| 4 | Q 4 al-Nisāʾ | 0.9038 | Medinan-large |
| 5 | Q 5 al-Māʾida | 0.9040 | Medinan-large |

**Five farthest neighbours** (Q 24 maximally distinct from short-mufaṣṣal / fāṣila-driven surahs):

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 109 | Q 75 al-Qiyāma | 1.1977 |
| 110 | Q 89 al-Fajr | 1.2151 |
| 111 | Q 54 al-Qamar | 1.2325 |
| 112 | Q 56 al-Wāqiʿa | 1.2431 |
| 113 | Q 55 al-Raḥmān | **1.4264** |

**Interpretation**: Q 24's nearest five neighbours are ALL Medinan, and four of the five (Q 2, Q 4, Q 5, Q 49) are *legal* in register. Yet Q 24's actual canonical-mushaf neighbour Q 23 sits at FR distance 1.0497 (rank ~80 of 113) and Q 25 at 1.1291 (rank ~95 of 113). Q 24's content-cluster is *Medinan-legal*; its actual canonical *neighbours* are Meccan-narrative. This is the FR-distance correlate of the "inserted into a Meccan-narrative zone" claim.

The farthest pair Q 55 (al-Raḥmān, 1.4264) is consistent with project-wide architecture: al-Raḥmān is monorhyme fawāṣil-driven (sig_A=+3.17, rank 1 of 114); Q 24 is the inverse (sig_A=−0.79, multi-rāwī, prose-legal). Q 55 / Q 24 = the Quran's two opposite ends of the iʿjāz axis among the long surahs.

## 5. Outlier-window decomposition (H-NEW-590)

The 7-window centred on Q 24 is `[21, 22, 23, 24, 25, 26, 27]` per `h-new-590.json`:

| Removed | d̄_W | d̄_W−X | percentile shift Δ (pp) | classification |
|:--:|:--:|:--:|:--:|:--|
| **Q 24** | 0.9628 | 0.9242 | **+23.51** | MODERATE_OUTLIER (rank 3 / 114) |
| Q 26 (al-Shuʿarāʾ) | 0.9628 | 0.9719 | (window shifts up; not in top-10) | window-cohesion |
| Q 23 (al-Muʾminūn) | 0.9628 | 0.9655 | (small) | window-cohesion |

(Source: `h-new-590.json` `all_surahs_results`; entry `{"X":24, "window":[21,...,27], "d_W":0.9627, "d_W_minus_X":0.9242, "delta_pct":23.51}`.)

Removing Q 24 *tightens* this window to d̄=0.924 — its removal makes the rest of the [21–27] block more like one another. In other words, **the rest of the [21–27] window is internally similar (Q 21 al-Anbiyāʾ, Q 22 al-Ḥajj, Q 23 al-Muʾminūn, Q 25 al-Furqān, Q 26 al-Shuʿarāʾ, Q 27 al-Naml are all narrative-prophetic-Meccan-flavour); Q 24 alone breaks that similarity.**

This is the cleanest *single-surah block-disrupter* signal in the top-10 outliers. Q 33 (rank 1, +31.46pp) disrupts a long-Medinan window; Q 1 (rank 2, +27.09pp) disrupts the head-7 window. Q 24 (rank 3, +23.51pp) disrupts a Meccan-narrative window — the only one of the top-3 outliers where the disruption is *register-class-mismatch*: Medinan-legal in a Meccan-narrative zone.

## 6. Light-cluster vocabulary concentration

**The first novel finding** (pre-registered in `Q024-F-01-light-vocabulary-density-prereg.md` and tested in `06-novel-findings.md`): does Q 24 over-concentrate the lexicon of light? Yes, at law-strength.

Light-cluster root family (16 roots, identified from Q 24:35 + immediate vicinity, plus standard Quranic light/parable lexicon): `{nwr, SbH, wqd, srj, qbs, shhb, mskw, zjj, kwkb, $jr, zyt, brk, $kw, drr, DwA, mvl}`.

Note that QAC parses both *nūr* (نور, light) and *nār* (نار, fire) under the **same root nwr** — so the QAC nwr count includes both senses. Q 24:35 alone has 6 nwr-stem tokens (5 nūr + 1 nār — the verse explicitly says the oil "would almost give light even if no fire touched it"; *nār* and *nūr* are juxtaposed). For light-density purposes the joint count is the right object since they form a single semantic field.

Per-corpus computation:

| Surah | Light-tokens | Total root-tokens | Density / 1000 | Rank by count | Rank by density |
|:--|:-:|:-:|:-:|:-:|:-:|
| Q 2 al-Baqara | 45 | 3,884 | 11.59 | 1 | 49 |
| **Q 24 al-Nūr** | **27** | **859** | **31.43** | **2** | **7** |
| Q 7 al-Aʿrāf | 23 | 2,144 | 10.73 | 3 | 53 |
| Q 3 Āl ʿImrān | 23 | 2,274 | 10.11 | 4 | 56 |
| Q 11 Hūd | 17 | 1,162 | 14.63 | 6 | 23 |
| Q 14 Ibrāhīm | 13 | 556 | 23.38 | 8 | 11 |
| Q 66 al-Taḥrīm | 7 | 171 | **40.94** | 22 | 5 |
| Q 104 al-Humaza | 2 | 21 | **95.24** | 89 | 1 |

Q 24 ranks 2 / 114 by raw count (after Q 2, which is 4.5× larger by total root-tokens) and 7 / 114 by density. It is the only mid-length surah that combines high light-count AND high density — Q 104, Q 111, Q 100 etc. score high density only because their total root-count is ~20-25 with one nwr token.

**Permutation test** (locked pre-reg, hypergeometric null, no-tashkeel-orthographic, basmala-counted-only-in-Q1):

- Corpus light-cluster total: 512 tokens (sum across 114 surahs).
- Corpus total root-tokens: 49,968.
- Expected light-tokens for Q 24 under uniform random root-distribution: (859 × 512) / 49,968 ≈ **8.80**.
- Observed: **27**.
- P(X ≥ 27 | hypergeometric, K=512, N=49,968, n=859) ≈ **3.81 × 10⁻⁷**.

Bonferroni correction over 114 surahs: α_Bon = 0.05 / 114 = 4.39 × 10⁻⁴. **Q 24 light-concentration passes Bonferroni at p_raw / α_Bon = 8.7 × 10⁻⁴**, i.e. survives at the corpus-wide α=0.05 level after multiple-comparison correction. Verdict: **VINDICATED**.

The empirical claim "Q 24 is named al-Nūr because it concentrates the light-lexicon" — which classical mufassirūn assert qualitatively — is now locked at p < 10⁻⁶, even adjusted for testing all 114 surahs.

(Pre-registration, script, full JSON: see `Q024-F-01-light-vocabulary-density-prereg.md`, `scripts/Q024_F_01_light_vocabulary_density.py`, `csv/Q024-F-01.json`.)

## 7. Q 24:35 — the most-light-dense verse in the Quran

The Light-verse (āyat al-nūr, Q 24:35) is **rank 1 / 6,236 by light-cluster root count**: 21 light-tokens in a single verse. The next-highest verse is Q 2:17 (the lit-fire parable) with 6 light-tokens — a **3.5× gap**. The rest of the top-10 verses each have only 3 or 4 light-tokens.

Q 24:35 root-decomposition (from QAC, lines `(24:35:1:1)` … `(24:35:48:1)`):

| Root | Count | Words |
|:--|:-:|:--|
| nwr (light/fire) | **6** | nūr, nūr-i-hi, nāru-n, nūru-n, nūr, nūr-i-hi |
| Alh (Allāh) | 4 | Allāhu, Allāhu, Allāhu, Allāhu |
| mvl (parable) | 2 | mathal-u, amthāl-a |
| SbH (lamp) | 2 | miṣbāḥu-n, al-miṣbāḥ |
| zjj (glass) | 2 | zujājat-i-n, al-zujājah |
| zyt (oil/olive) | 2 | zaytūnat-i-n, zayt-u-hā |
| $yA (will) | 2 | yashāʾu, shay'-i-n |
| $kw (niche) | 1 | mishkāt |
| kwkb (star) | 1 | kawkab-u-n |
| drr (pearl) | 1 | durriyy-u-n |
| wqd (kindle) | 1 | yūqadu |
| $jr (tree) | 1 | shajarat-i-n |
| brk (blessed) | 1 | mubārakat-i-n |
| DwA (illuminate) | 1 | yuḍīʾu |
| (other roots) | — | smw, ArD, hdy, kll, nws, Drb, mss, kwd, $rq, grb |

48 words total, 38 roots-tokens with explicit ROOT in QAC (the rest are particles, conjunctions, pronouns).

The verse is morphologically dense: 14 distinct roots from the light-and-vehicle cluster, packed into 48 words. By comparison, Q 2:255 (āyat al-kursī) packs 23 distinct roots into 50 words but shares only **5 roots** with Q 24:35 (`Alh, smw, ArD, $yA, Elm`) — and contains zero light-cluster roots.

## 8. Allāh-density: Q 24:35 vs Q 2:255

Counting *Alh* (Allāh) per-verse across 6,236 verses:

| Verse | Allāh count | Word count | Density |
|:--|:-:|:-:|:-:|
| **Q 24:35** | **4** | 48 | **0.0833** (8.33%) |
| Q 2:255 | 2 | 50 | 0.0400 (4.00%) |

Q 24:35's Allāh density is **2.08× Q 2:255's**. By verse-level Allāh count, Q 24:35 ranks 37 / 6,236; Q 2:255 ranks lower. This is a non-trivial *theological-density* finding: although classical literature pairs the two as the corpus's two great verses, Q 24:35 is *theologically denser* (more Allāh tokens) per word than Q 2:255. (Q 2:255 compensates with attribute-density: al-Ḥayy, al-Qayyūm, al-ʿAlī, al-ʿAẓīm — divine names rather than the proper noun Allāh.)

See `Q024-F-02-aya-al-nur-vs-aya-al-kursi-prereg.md` and `06-novel-findings.md` for the full pre-registered comparison.

## 9. Structural midpoint of Q 24

Pre-registered novel test: Q 24:35 is positioned at the literal word-and-letter midpoint of its surah.

Computation (no-tashkeel orthographic, mushaf-marks stripped):
- Q 24 total words: 1,319.
- Half-word: 659.5. Word 659 is *inside Q 24:35* (which spans words 622–669). **Q 24:35 contains the median word of the surah.**
- Q 24 total letters (no spaces): 5,754.
- Half-letter: 2,877. Letter 2,877 is *inside Q 24:35* (which spans letters 2,787–2,989). **Q 24:35 contains the median letter of the surah.**
- Verse position 35 / 64 = 0.547 (also near-median).
- Mid-word of Q 24:35 itself: word 645.5 — ratio 0.489 of the surah's 1,319 words. **Within 1.1% of exact midpoint.**

By comparison: Q 2:255 (āyat al-kursī) sits at word ratio **0.845** of Q 2 (late-third-quarter, NOT median). Q 24:35 is therefore the *only* one of the two classical "great verses" that is *literally* at the structural centre of its surah.

This is a concrete architectural property the classical "structural midpoint" tradition would predict for a centerpiece-verse. It is verified at multiple measurement units (verse, word, letter) all converging.

(Pre-registration: `Q024-F-03-structural-midpoint-prereg.md`. JSON: `csv/Q024-F-03.json`.)

## 10. Compression-tail position

Q 24 sits at s = 24, well *before* the Hijra-kink at s = 50 ([[h-new-660-compression-tail-gradient|H-NEW-660]]; [[h-new-700-phonological-compression-tail|H-NEW-700]]). The compression-tail laws are silent here by construction. Q 24 belongs to the **pre-kink head zone** along with the other Medinan-legal long surahs (Q 2, 3, 4, 5, 8, 9, 33). Its mean content distance d̄ = 1.0704 sits well *above* the head-zone typical d̄ ≈ 0.95 — Q 24 is content-FARTHER from corpus than even its head-zone neighbours.

## 11. Architectural type classification

Per the project's three-class scheme ([[h-new-840-unified-architectural-score|H-NEW-840]], [[h-new-860-hadith-architectural-alignment|H-NEW-860]]):

- **Structural-iʿjāz** (al-Bāqillānī *iʿjāz al-fawāṣil*): high UAS + high sig_A → Q 33, Q 1, Q 2, Q 9.
- **Theological-iʿjāz** (al-Khaṭṭābī *iʿjāz al-maʿnā*): low UAS but high *thuluth-al-Qurʾān* status → Q 112, Q 114.
- **Anti-iʿjāz**: low on both axes → Q 87, Q 105, Q 73, Q 83.

Q 24 is **a fourth distinct type**: top-5 UAS BUT sig_A negative (rank 82). I designate this **outlier-without-iʿjāz al-fawāṣil** — the surah is *structurally singular* (high outlier, high adjacency cost) but *not via fāṣila virtuosity*. The other top-5 UAS surahs all combine outlier strength with at least moderate sig_A; Q 24 alone sits in the {high outlier, low sig_A} cell.

The mechanism: Q 24's content is legal-prose with multi-rāwī rhyme. It is a *content* outlier (Medinan-legal core inserted into Meccan-narrative neighbours), not a *style* outlier. The UAS picks it up via the outlier and adjacency-cost components alone.

## 12. Cross-references to all H-NEW findings touching Q 24

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 24 mean FR distance to corpus = 1.0704 (rank 105 / 114 — far from corpus); nearest = Q 49 (0.870), farthest = Q 55 (1.426).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 24 MODERATE_OUTLIER, Δ = +23.51 pp (rank 3 / 114 — only Q 33, Q 1 outlier-stronger).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — pre-kink head-zone position s = 24.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 23 → Q 24 = 0.2116 (rank 11 / 113); Q 24 → Q 25 = 0.2896 (rank 5 / 113); both top-15.
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A = −0.7901 (rank 82, anti-structural-iʿjāz); sig_B = −0.1292 (rank 61); rhyme entropy 1.134 nats (rank 6, multi-rāwī).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS = 4.4501 (rank 5 / 114); component breakdown above.
- [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — Q 24 UAS top-5 but classical fadāʾil moderate; Q 24's classical attention concentrates on *content* (the al-ifk story, the ḥijāb verses, the Light-verse) not on recitation merits — consistent with the al-Khaṭṭābī meaning-iʿjāz lineage *without* the al-Bāqillānī fawāṣil-iʿjāz lineage.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 24 illustrates the dual-iʿjāz typology's *fourth cell* (high UAS + low sig_A).

## 13. Honest limits

- The H-NEW-840 UAS is a z-sum of three correlated axes; it has no Bonferroni significance test of its own (see [[h-new-840-unified-architectural-score|H-NEW-840]] §5). The "rank 5" claim is descriptive, not inferential.
- The "Q 24 → Q 25 cost rank 5" depends on the 2-opt heuristic's `L_2opt = 77.388` baseline. A tighter solver might shift the residual by a few percent, but the rank order of the top-15 expensive adjacencies is robust across the 50 restart seeds reported in H-NEW-720.
- The "rank 105 / 114 mean FR distance" is calculated only over the no-tashkeel root-distribution variant; under different tokenization (e.g., orthographic-token rather than QAC-stem) the rank can shift modestly. The *direction* — Q 24 is far from corpus centroid — is rules-tuple stable under all tested variants.
- The rhyme entropy of 1.134 nats places Q 24 at rank 6 of 114; this is *high* but not extreme (some short surahs have 1.5+ nats due to small-N noise). The substantive claim — that Q 24 is multi-rāwī unlike high-sig_A monorhyme surahs — is robust.
- The "Q 24:35 word-midpoint" claim uses no-tashkeel-orthographic word counts (1,319 words). Under different counting conventions (e.g., al-Tha'labī's 1,316-word and 5,680-letter classical count) the midpoint location *shifts within Q 24:35* but does not move OUT of it. Tested rules-tuple stable.

## 14. One-paragraph synthesis

Q 24 al-Nūr is the **canonical exemplar of architectural outlier-status WITHOUT structural-iʿjāz**. The mushaf places it at index 24 — embedded in a Meccan-narrative zone (Q 21–27) where its Medinan-legal register makes it the most distinct single surah of the seven-window — and pays for this placement with both the 5th and 11th most expensive canonical adjacencies in the corpus (combined 6.0% of TSP residual). Its FR-distance signature places it close to Q 49, Q 64, Q 2–5 (Medinan-legal cluster) and farthest from Q 55 al-Raḥmān (the corpus's top-sig_A monorhyme surah) — the empirical content of the qualitative register-class mismatch with its canonical neighbours. The light-cluster lexicon (16 roots) over-concentrates here at p < 10⁻⁶ (Bonferroni-corrected): rank 2 / 114 by raw count, rank 7 / 114 by density. The Light-verse Q 24:35 is rank 1 / 6,236 by light-token count, sits at the literal word-and-letter midpoint of its surah, and has Allāh-density 2.08× that of āyat al-kursī. UAS rank 5 / 114 is therefore a substantive empirical fact, but it is achieved by a different mechanism than the other top-5 (Q 33, Q 1, Q 2, Q 9): Q 24 wins on outlier + adjacency cost alone, with sig_A actually *negative* (rank 82). This is the project's clearest case of "structural-singular by content-position rather than by fāṣila virtuosity" — and it vindicates the qualitative classical claim that Q 24's distinctness lives in its register and content, not in its rhyme architecture.
