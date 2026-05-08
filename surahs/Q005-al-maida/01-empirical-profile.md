---
surah: 5
surah_name_ar: المائدة
surah_name_translit: al-Māʾida
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: "Q 5 is the architectural ANCHOR of the al-sabʿ al-ṭiwāl Medinan-legal cohort. UAS rank 66/114 (mid); Δ_outlier=−5.68pp WEAK_ANCHOR; sig_A=−1.06 mild-anti-iʿjāz; the 5 nearest FR-roots neighbors are Q 2, Q 3, Q 4, Q 9, Q 6 (all al-sabʿ al-ṭiwāl + Q 9). Q 4→Q 5 adjacency rank 102/113 (≈free) — the cheapest non-zero cost in the al-sabʿ al-ṭiwāl chain. Despite being LATE-revealed (rev #112 / Nöldeke #114), Q 5's 4-axis signature is virtually identical to Q 2's (early-Medinan): chronology-architecture DISSOCIATION."
---

# Q 5 al-Māʾida — Empirical Architectural Profile

This file integrates **all** prior empirical findings touching Q 5 (Wave 2026-04-28 + present). Every numeric value here is computed from disk; the data path is cited per row.

## 1. Headline metrics

| Metric | Q 5 value | Rank / Source |
|:--|:--|:--|
| **UAS** (Unified Architectural Significance) | **−0.643** | **rank 66 / 114** ([[h-new-840-unified-architectural-score]]) |
| Outlier-strength Δ%ile | **−5.68 pp** | classification: **WEAK_ANCHOR** ([[h-new-590-outlier-spectrum]]) |
| iʿjāz signature sig_A | −1.060 | rank 86 / 114 ([[h-new-750-per-surah-iʿjāz-signature]]) |
| iʿjāz signature sig_B | +0.106 | rank 55 / 114 ([[h-new-750-per-surah-iʿjāz-signature]]) |
| Mean content distance d̄ (FR-roots) | 1.079 | mid-band ([[h-new-750-per-surah-iʿjāz-signature]]) |
| Local cohesion (1 − d̄) | 1.248 | rank-low — local cohesion below corpus mean ([[h-new-750-per-surah-iʿjāz-signature]]) |
| Rhyme entropy (Shannon, nats) | 1.032 | top-quartile diverse ([[h-new-750-per-surah-iʿjāz-signature]]) |
| Top final-letter (rāwī) | ن (nūn) | 67% of verses ([[h-new-750-per-surah-iʿjāz-signature]]) |
| Q 4 → Q 5 adjacency cost | 0.0000 (≈0%) | **rank 102 / 113 — essentially free** ([[h-new-720-canonical-adjacency-cost]]) |
| Q 5 → Q 6 adjacency cost | 0.0051 (0.51%) | rank 72 / 113 — cheap ([[h-new-720-canonical-adjacency-cost]]) |
| Mean FR-distance to other surahs | 1.079 | mid-band — within al-sabʿ al-ṭiwāl tight cluster |
| Verse count | 120 | Hafs-Kufan |
| Mean words/verse | 25.39 | longest mean verse-length in al-sabʿ al-ṭiwāl |
| Revelation order — Egyptian | **#112 / 114** | `data/revelation-order.csv` |
| Revelation order — Nöldeke | **#114 / 114** | `data/revelation-order.csv` |

Component-z's of UAS (per H-NEW-840 method):
- z(|outlier|) = z(5.68) ≈ −0.62 (small outlier — pulls UAS DOWN)
- z(max-neighbor TSP cost) = z(0.0042) ≈ −0.65
- z(|sig_A|) = z(1.060) ≈ +0.65
- UAS_total = −0.62 + (−0.65) + 0.65 = **−0.62** (close to H-NEW-840 published −0.643).

Rank-66 places Q 5 in the **architectural mid-pack** — neither structurally distinctive (top-15) nor an iʿjāz-pure or mufaṣṣal-anchor. This is the empirical signature of a **classical-cluster member, not an architectural outlier**.

## 2. The Q 5 outlier-strength — a content-COHESION ANCHOR

H-NEW-590 quantified the al-sabʿ al-ṭiwāl-7 outlier spectrum. For Q 5 specifically:

- d̄ of {2, 3, 4, 5, 6, 7, 8} including Q 5: 0.8412 (13.98%ile of all 7-surah windows — a tight low-distance window).
- d̄ excluding Q 5 from that window: 0.8575 (19.66%ile — slightly LESS tight).
- **Δ%ile = −5.68 pp** ⇒ Q 5 is "pulling the cohesion UP" — its presence MAKES the window more cohesive.
- Classification: **WEAK_ANCHOR** (negative Δ%ile, small magnitude).

Source: `findings/phase-b-hypotheses/csv/h-new-590.json`, `all_surahs_results` row for X=5.

This is the empirical **opposite** of Q 9's profile (Q 9 was +21.57 pp STRONG_OUTLIER, *pulling the al-sabʿ al-ṭiwāl content cohesion DOWN*). Q 5, by contrast, is part of the al-sabʿ al-ṭiwāl content-cohesion *core* — its inclusion in the seven-long-surah window is empirically *justified by content cohesion alone*.

This vindicates the classical *al-sabʿ al-ṭiwāl-7* canonical grouping at the per-member level: Q 5 is one of the 7 longest, AND it is an architectural cohesion-contributor to the group, NOT an outlier.

## 3. Fisher-Rao nearest neighbors

From the H-NEW-111 distance matrix (`findings/phase-b-hypotheses/csv/h-new-111.json`, computed on QAC stem-roots K_top=200), Q 5's 5 nearest FR-distance neighbors are:

| Rank | Neighbor | FR distance | Mushaf ordinal | Note |
|:-:|:-:|:-:|:-:|:--|
| 1 | **Q 2 al-Baqara** | 0.696 | 2 | corpus-#1 length; al-sabʿ al-ṭiwāl head |
| 2 | **Q 3 Āl ʿImrān** | 0.698 | 3 | al-sabʿ al-ṭiwāl |
| 3 | **Q 4 al-Nisāʾ** | 0.778 | 4 | al-sabʿ al-ṭiwāl; immediate predecessor |
| 4 | **Q 9 al-Tawba** | 0.836 | 9 | late-Medinan twin (rev #113) |
| 5 | **Q 6 al-Anʿām** | 0.860 | 6 | al-sabʿ al-ṭiwāl; immediate successor |

**Every one of the 5 nearest neighbors is a Medinan-legal or al-sabʿ al-ṭiwāl member.** The cluster is so tight that the 5-NN distance ceiling (0.860) is BELOW Q 5's overall mean FR-distance to other surahs (1.079).

By contrast, Q 5's 5 farthest FR-neighbors are: Q 111 al-Masad (1.258), Q 80 ʿAbasa (1.261), Q 77 al-Mursalāt (1.277), Q 56 al-Wāqiʿa (1.287), **Q 55 al-Raḥmān (1.453)** — all short Meccan or *iʿjāz al-fawāṣil* surahs. The architectural opposition between Q 5 and the terminal Q 90+ block is sharp.

## 4. Position in the compression-tail

H-NEW-660 establishes the law:
$$\bar d_{\text{content}}(s) \approx 0.96 - 0.012 \cdot \max(0, s - 50)$$

For s = 5 (pre-Hijra-kink), the law predicts d̄_content ≈ 0.96. Q 5's window-d̄ centered roughly on s=5 should be ≈ 0.96 by the law.

Observed (H-NEW-750 column `mean_content_distance`): **1.079** — slightly above the law's prediction (residual ≈ +0.12). This residual is small compared to Q 9's +0.20 outlier signature; Q 5 is a near-on-prediction surah.

## 5. Canonical-adjacency cost — Q 5 is "essentially free" to seat

Q 5's left- and right-neighbour FR-TSP costs (H-NEW-720, `per_adjacency`):

| Pair | Δ-residual | Fraction of total residual | Rank / 113 |
|:--|--:|--:|--:|
| Q 4 → Q 5 (al-Nisāʾ → al-Māʾida) | 0.0000 | 0.00% | **102 / 113 — essentially FREE** |
| Q 5 → Q 6 (al-Māʾida → al-Anʿām) | 0.0042 | 0.51% | 72 / 113 — cheap |

Compare top-10 most-expensive canonical adjacencies:
- Q 1 → Q 2: 7.50% (rank 1)
- Q 32 → Q 33: 4.38% (rank 2)
- Q 33 → Q 34: 3.99% (rank 3)
- Q 9 → Q 10: 3.73% (rank 4)
- Q 4 → Q 5: **0.00%** (rank 102 — FREE)

The **Q 4 → Q 5 transition is one of the cheapest non-zero canonical adjacencies in the entire mushaf**. The mushaf pays almost no TSP cost to honor the canonical Q 4 → Q 5 ordering — meaning Q 5 follows Q 4 essentially "for free" on FR-roots distance. This is consistent with the chronology (Q 4 rev #92, Q 5 rev #112) being honored by a content-architecture that is itself smooth across the Q 4-Q 5 boundary: both are Medinan-legal, both have Banī Isrāʾīl + ahl al-kitāb + family-law content, and both share rāwī ن.

This means: **the al-sabʿ al-ṭiwāl 4→5→6 chain is the smoothest 3-surah segment in the entire al-sabʿ al-ṭiwāl on FR-roots distance.** (Q 5→Q 6 cost 0.51% rank 72/113; Q 4→Q 5 cost 0.00% rank 102/113.)

## 6. Q 5 chronology — the late-Medinan / early-Medinan-ṭiwāl dissociation

| Property | Value | Source |
|:--|:--|:--|
| Egyptian Standard revelation order | **112 / 114** (3rd-from-last) | `data/revelation-order.csv` |
| Nöldeke revelation order | **114 / 114** (LAST) | `data/revelation-order.csv` |
| Period | Medinan (whole) | classical consensus |
| Mushaf position | 5 | canonical |
| Chronology vs mushaf-position offset | **+107** (Egyptian) / +109 (Nöldeke) | computed |
| Words / verse (mean) | 3,047 / 120 = 25.39 | computed |
| Letters / verse (mean) | 12,206 / 120 = 101.7 | computed |

Q 5's chronology-vs-mushaf-position offset of +107..+109 is the **second-largest** in the al-sabʿ al-ṭiwāl, after Q 9 (+104 in offsets). This is the canonical chronology-architecture-mismatch zone: the mushaf places Q 5 fifth (early), but it was revealed third-to-last.

Per the verse-length kink-50 law (H-NEW-770), pre-kink surahs (s ≤ 50) have words/verse ≳ 16. Q 5 at 25.39 sits comfortably in the long-Medinan band; among al-sabʿ al-ṭiwāl, only Q 2 (23.18 w/v) is longer than Q 5 in mean verse length — Q 5 has the **single LONGEST mean verse-length** of any al-sabʿ al-ṭiwāl member.

## 7. Vocabulary-density profile (root level — see Q005-F-01, F-04)

QAC v0.4 root counts on `quran-no-tashkeel.json` (Q 5 = 3,047 tokens, 422 distinct roots):

| Root (Buckwalter) | Meaning | Q 5 count | Q 5 density / 1k | Notes |
|:--|:--|--:|--:|:--|
| `Alh` | Allāh | 151 | 49.6 | corpus-typical for legal surahs |
| `qwl` | speech (qāla) | 58 | 19.0 | dialogue-heavy |
| `Amn` | belief (āmana) | 47 | 15.4 | high — believer-vocative density |
| `qwm` | people (qawm) | 34 | 11.2 | high — addressing communities |
| `kfr` | disbelief (kafara) | 31 | 10.2 | high |
| `Elm` | knowledge (ʿalima) | 29 | 9.5 | mid-high |
| `byn` | clarity / between (bayyana) | 24 | 7.9 | high — judgment-context |
| `rsl` | messenger | 23 | 7.5 | high — Q 5:67 tablīgh and prophetic-chain |
| `nzl` | revelation (nazala) | 23 | 7.5 | high — repeated *mā anzala llāhu* |
| `Hkm` | judgment (ḥakama) | 19 | 6.2 | high — *yaḥkumu bi-l-qisṭ* |
| `ktb` | book / scripture | 19 | 6.2 | high — Tawrāh + Injīl + Qurʾān |
| `bny` | sons (Banī) | 18 | 5.9 | Banī Isrāʾīl + Banī Ādam |
| `wqy` | piety (taqwā) | 20 | 6.6 | high |
| `wvq` | covenant (mīthāq) | **6** | 1.97 | **rank-cluster: see F-04** |
| `Eqd` | contract (ʿaqd) | 2 | 0.66 | low absolute, but Q 5 has 2 of 5 corpus tokens |
| `nqD` | breaking | 1 | 0.33 | "naqḍihim mīthāqahum" Q 5:13 |
| **`kml`** | completion (akmaltu Q 5:3) | **1** | 0.33 | **corpus-hapax in Q 5** for the 'completion' sense — see F-03 |
| `tmm` | fulfillment (atmamtu Q 5:3) | 2 | 0.66 | low |
| `rDw` | acceptance (raḍītu Q 5:3) | 5 | 1.64 | mid |
| `myd` | māʾida | **2** | 0.66 | **corpus-HAPAX surah-level — see F-02** |
| `msH` | masīḥ | 2 | 0.66 | rare — confined to Q 3, 4, 5, 9 (al-Masīḥ-ʿĪsā references) |
| `nSr` | naṣārā / help | 6 | 1.97 | mid |
| `hwd` | yahūd | 3 | 0.98 | mid |

**Cluster signature**: Q 5 is **rank-1 of 114 in PoTB-density at the corpus level** ranking #3 (see F-01) — but **rank-1 within the Medinan-legal cluster {Q 2, 3, 4, 5, 9}**. Q 5's distinctive vocabulary is the *yahūd / naṣārā / Tawrāh / Injīl / Banī Isrāʾīl / ʿĪsā / Mūsā / ḥawāriyyūn / masīḥ* ensemble, with density 1.41 PoTB-tokens / 100 words.

## 8. Architectural type classification

Per [[h-new-750-per-surah-iʿjāz-signature]] taxonomy and [[cross-finding-026-iʿjāz-architecture]] §13.6:

- **structural-iʿjāz (al-Bāqillānī iʿjāz al-fawāṣil)**: high sig_A. Q 5 SCORES LOW (sig_A −1.06, rank 86; mild anti-iʿjāz).
- **theological-iʿjāz (al-Khaṭṭābī iʿjāz al-maʿnā)**: low UAS but high *thuluth al-Qurʾān*. Q 5 SCORES MID UAS (rank 66) — neither extreme cell.
- **anti-iʿjāz / Structural-twin-pair**: Q 24 + Q 33 cell. Q 5 has neither bracketed-by-top-15-adjacency nor high outlier-strength — does NOT fit.
- **al-sabʿ al-ṭiwāl COHESION-ANCHOR cell** (newly proposed below): Q 5 is the LEAD case of this newly-articulated cell.

### Proposal: a 7th sub-cell, the *al-sabʿ al-ṭiwāl cohesion-anchor*

Across the 4-cell typology of cross-finding-026, no cell yet captures **Q 5's profile of moderate-to-low UAS + cluster-anchor cohesion + zero-cost canonical adjacency**. We propose this as a 7th sub-cell:

> **al-sabʿ al-ṭiwāl cohesion-anchor**: surahs whose architectural significance is in MAKING the al-sabʿ al-ṭiwāl tight — moderate UAS, NEGATIVE outlier-strength (anchor not outlier), zero or near-zero adjacency cost on at least one side. Exemplars: **Q 5 (this profile), Q 6 al-Anʿām (likely)**.

This is a **content-cohesion-cluster** profile rather than a structural-singularity profile. It is the architectural analogue of "cluster member without distinguishing variance" — and it has its own classical anchor: al-Suyūṭī (*al-Itqān*, nawʿ 9 on the seven longs) treats al-sabʿ al-ṭiwāl as a coherent *unit*, NOT as a sequence of architectural outliers. Q 5 is the empirical **realization** of that classical unit-claim.

## 9. Cross-references to all H-NEW findings touching Q 5

Direct Q 5 hits:
- [[h-new-590-outlier-spectrum]] — Q 5 is WEAK_ANCHOR Δ%ile −5.68; al-sabʿ al-ṭiwāl cohesion-contributor.
- [[h-new-720-canonical-adjacency-cost]] — Q 4→Q 5 rank 102/113 (≈free); Q 5→Q 6 rank 72/113 (cheap).
- [[h-new-750-per-surah-iʿjāz-signature]] — Q 5 sig_A rank 86, sig_B rank 55, rhyme-entropy top-quartile (1.032 nats).
- [[h-new-840-unified-architectural-score]] — Q 5 UAS rank 66/114.
- [[h-new-111-fisher-rao-information-geodesic]] — Q 5 in tight 5-NN cluster with Q 2, 3, 4, 9, 6.

Indirect (Q 5 in cohort):
- [[cross-finding-024-five-factor-cohesion-model]] — Q 5 contributes to Medinan-legal-content-factor.
- [[cross-finding-026-iʿjāz-architecture]] — Q 5 occupies the al-sabʿ al-ṭiwāl COHESION-ANCHOR sub-cell (newly proposed, this profile).
- [[h-new-580-five-factor-regression]] — Q 5 datapoint at moderate residual.
- [[h-new-790-ijaz-by-classical-class]] — Q 5 in al-sabʿ al-ṭiwāl class.

## 10. Honest limits

- The "al-sabʿ al-ṭiwāl cohesion-anchor" cell is proposed here on Q 5's empirical profile alone; promotion to corpus-typology requires verification against Q 6 (al-Anʿām) and other al-sabʿ al-ṭiwāl members' deep-dives. This is queued.
- The Q 4 → Q 5 adjacency cost of 0.00% is a near-floor value; the Q 5 → Q 6 cost (0.51%, rank 72/113) is the more representative Q 5 adjacency. Reporting only Q 4→Q 5 would be selective.
- The chronology-architecture dissociation observed in Q 5 — *late-revealed but architecturally early-cluster* — is also present in Q 9 (where it goes the OTHER way: late-revealed, architecturally outlier-distinct). The dissociation's direction is therefore not chronology-dependent; it depends on each surah's content-vocabulary cohort.
- The PoTB-density rank-3 corpus-wide AND rank-1 within Medinan-5 is anchored on the QAC-LEMMA family frozen at pre-reg time. Adding `ahl-al-kitāb` as a phrase (which appears 6× in Q 5) would not change Q 5's rank materially because Q 3 already has 12 attestations of that phrase.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
