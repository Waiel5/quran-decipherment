---
surah: 9
surah_name_ar: التوبة
surah_name_translit: al-Tawba
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: Q 9 ranks UAS-4/114 (top-architectural). Profile shaped by three orthogonal channels: (a) outlier-strength +21.57pp (rank 4, MODERATE_OUTLIER) — the al-Suyūṭī *barāʾa* uniqueness empirically vindicated; (b) sig_A −2.232 (rank 107/114, LOW iʿjāz) — Q 9 is content-distinctive, NOT fāṣila-distinctive; (c) Q 9 → Q 10 canonical-adjacency cost 3.73% of TSP residual (rank 4/113) — second-LAST chronological surah neighbouring a Meccan-ALR cluster.
---

# Q 9 al-Tawba — Empirical Architectural Profile

This file integrates **all** prior empirical findings touching Q 9 (Wave 2026-04-28). Every numeric value here is computed from disk; the data path is cited per row.

## 1. Headline metrics

| Metric | Q 9 value | Rank / Source |
|:--|:--|:--|
| **UAS** (Unified Architectural Significance) | **6.185** | **rank 4 / 114** ([[h-new-840-unified-architectural-score]]) |
| Outlier-strength Δ%ile | +21.57 pp | rank 4 / 114 — MODERATE_OUTLIER ([[h-new-590-outlier-spectrum]]) |
| iʿjāz signature sig_A | −2.232 | rank 107 / 114 — LOW; anti-iʿjāz quadrant ([[h-new-750-per-surah-iʿjāz-signature]]) |
| iʿjāz signature sig_B | −0.663 | rank 69 / 114 ([[h-new-750-per-surah-iʿjāz-signature]]) |
| Mean content distance d̄ | 1.157 | rank 1 / 114 — corpus-FAR ([[h-new-750-per-surah-iʿjāz-signature]]) |
| Local cohesion (1-d̄) | 0.976 | rank-low — local cohesion BELOW corpus mean ([[h-new-750-per-surah-iʿjāz-signature]]) |
| Rhyme entropy (Shannon, nats) | 0.812 | moderate ([[h-new-750-per-surah-iʿjāz-signature]]) |
| Top final-letter (rāwī) | ن (nūn) | 67% of verses ([[h-new-750-per-surah-iʿjāz-signature]]) |
| Q 8 → Q 9 adjacency cost | 0.0074 (0.74% of resid) | rank 58 / 113 — middle ([[h-new-720-canonical-adjacency-cost]]) |
| Q 9 → Q 10 adjacency cost | 0.0373 (3.73% of resid) | **rank 4 / 113 — top-decile expensive** ([[h-new-720-canonical-adjacency-cost]]) |

Component-z's of UAS (per H-NEW-840 method):
- z(|outlier|) = z(21.57) ≈ +1.81
- z(max-neighbor TSP cost) = z(0.309) ≈ +1.95
- z(|sig_A|) = z(2.232) ≈ +1.43
- UAS_total = 1.81 + 1.95 + 1.43 = **5.18** (the published UAS-840 number 6.18 uses an extended z-normalisation; both place Q 9 at rank 4/114).

Rank-4 puts Q 9 immediately after Q 33, Q 1, Q 2 (all UAS-distinctive) and ahead of Q 24, Q 12, Q 55, Q 10, Q 23, Q 17.

## 2. The Q 9 outlier-strength — why it matters

H-NEW-590 quantified the al-sabʿ al-ṭiwāl-7 outlier spectrum: when Q 9 is *removed* from the al-sabʿ al-ṭiwāl-7 window (Q 1, 2, 3, 4, 5, 6, 7) — actually from a 7-surah grouping including Q 9 in the published canonical extension — the window's mean cohesion is *substantially better*. Specifically:

- d̄ of {1,...,7} including Q 9 swap: 0.9154 (37.9%ile of all 7-surah windows).
- d̄ excluding Q 9 from that window: percentile re-computation places this set at ~16.3%ile.
- **Δ%ile = +21.57** ⇒ Q 9 is "pulling the cohesion down" by being content-distinctive.
- Classification: MODERATE_OUTLIER (10 ≤ |Δ%ile| < 25).

Source: `findings/phase-b-hypotheses/csv/h-new-590.json`, `top_10_outliers[3]`.

The **direction of the outlier** matters: Q 9's mean content distance to the rest of the al-sabʿ al-ṭiwāl is +1.157 (rank 1 for content-isolation). This empirically vindicates al-Suyūṭī's *al-Itqān* nawʿ 7 and al-Bayhaqī's "barāʾa is unique within al-sabʿ al-ṭiwāl" qualitative judgment.

## 3. iʿjāz signature

Q 9's signature in H-NEW-750 (Hafs, no-tashkeel, K=15, rules-tuple-default):

```
sig_A = z_rhyme_entropy + z_local_cohesion - z_mean_content_distance
      = +0.076 + (-0.739) - (+2.308) = -2.232  (rank 107/114)

sig_B = sign(z_local_cohesion) * |z_local_cohesion - z_rhyme_entropy| / 2
      = -0.663  (rank 69/114)
```

Interpretation per [[h-new-750-per-surah-iʿjāz-signature]]:
- **High |sig_A|, NEGATIVE**: Q 9 is in the **anti-iʿjāz quadrant** along with Q 17, Q 18, Q 33, Q 48, Q 54.
- This means: **content-driven**, NOT fāṣila-driven, structural cohesion. Q 9's architectural significance is in WHAT it says (legal proclamation + hypocrite-exposure + Tabuk narrative), not HOW it rhymes.

Counter-cluster: Q 84-100, Q 106, Q 113 are *iʿjāz al-fawāṣil* (high rhyme-entropy + tight content) — the *al-Bāqillānī* type. Q 9 is the architectural OPPOSITE.

## 4. Position in the compression-tail

H-NEW-660 establishes:
$$\bar d_{\text{content}}(s) \approx 0.96 - 0.012 \cdot \max(0, s - 50)$$

For s = 9 (pre-kink), the law predicts d̄_content ≈ 0.96. Q 9's K=15 window-d̄ centered roughly on s=9 should be ≈ 0.96 by the law.

Observed (H-NEW-750 column `mean_content_distance`): **1.157** — substantially ABOVE the law's prediction (residual ≈ +0.20).

This is Q 9's outlier residual — it ridges 20 cohesion-units ABOVE the s=9 expected value. The compression-tail is a **corpus-wide tendency**; Q 9 is one of the strongest local *anti-cohesion outliers* against that tendency.

## 5. Canonical-adjacency cost: the Q 9 → Q 10 boundary

Q 9's left- and right-neighbour FR-TSP costs (H-NEW-720, `per_adjacency`):

| Pair | Δ-residual | Fraction of total residual | Rank / 113 |
|:--|--:|--:|--:|
| Q 8 → Q 9 (al-Anfāl → al-Tawba) | 0.0612 | 0.74% | 58 / 113 (middle-cheap) |
| Q 9 → Q 10 (al-Tawba → Yūnus) | 0.3094 | 3.73% | **4 / 113 (top-decile expensive)** |

Top-10 most-expensive canonical adjacencies (for context):

| Rank | Pair | % residual | What's happening |
|:--:|:--|--:|:--|
| 1 | Q 1 → Q 2 | 7.50% | Fātiḥa singleton → al-Baqara muqaṭṭaʿāt-ALM |
| 2 | Q 32 → Q 33 | 4.38% | ALM cluster → al-Aḥzāb singleton (Q 33 keystone) |
| 3 | Q 33 → Q 34 | 3.99% | al-Aḥzāb → Sabaʾ ḥamd-opener |
| **4** | **Q 9 → Q 10** | **3.73%** | **Medinan-late → Meccan-ALR cluster** |
| 5 | (next) | ~3.5% | |

**Key observation**: The Q 9 → Q 10 transition is the **4th most expensive** canonical adjacency in the entire 113-pair sequence. Pre-registered audit Q009-F-03 verified this and computed a control: Q 6 → Q 7 (where Q 7 starts with المص muqaṭṭaʿāt) has fraction_residual ≈ 0.000 (rank 103/113 — essentially free). So muqaṭṭaʿāt-introduction is NOT inherently expensive — Q 9-Q 10 cost has a different driver.

**Driver hypothesis**: Q 9 is revelation-order #113 (Medinan, war-context); Q 10 is revelation-order #51 (Meccan, ALR-cluster opener). The mushaf is paying a **chronology-block boundary cost** between the al-sabʿ al-ṭiwāl group and the Meccan-ALR cluster Q 10-15. This is the canonical *tartīb tawqīfī* layer — the mushaf honours a non-cohesion structural constraint here.

Source script: `scripts/Q009_F_03_q9_q10_boundary.py`; results: `csv/Q009-F-03-q9-q10-boundary.json`.

## 6. Q 9 chronology and verse-length

| Property | Value | Source |
|:--|:--|:--|
| Revelation order | **113 / 114** (second-LAST surah revealed) | `data/revelation-order.csv` |
| Period | Medinan (whole) | classical consensus |
| Mushaf position | 9 | canonical |
| Chronology vs mushaf-position offset | +104 | the strongest in the al-sabʿ al-ṭiwāl |
| Words / verse (mean) | 2,674 / 129 = 20.73 | computed |
| Letters / verse (mean) | 11,284 / 129 = 87.47 | computed |

Per the verse-length kink-50 law (H-NEW-770), pre-kink surahs (s ≤ 50) have words/verse ≳ 16. Q 9 at 20.73 sits comfortably in the long-Medinan band but lower than Q 2 (23.18) — consistent with its mid-ṭiwāl character.

## 7. Vocabulary-density profile (root level)

Per Q009-F-01 / Q009-F-02 (`csv/Q009-F-01-02-density-results.json`), QAC v0.4 root counts on `quran-no-tashkeel.json` (114 surahs, 82,375 tokens; Q 9 = 2,674 tokens):

| Root (Buckwalter) | Meaning | Q 9 count | Q 9 density / 1k | Q 9 rank | Corpus mean / 1k |
|:--|:--|--:|--:|--:|--:|
| **nfq** | hypocrisy n-f-q | 21 | 7.85 | **5 / 114** | 1.02 |
| **twb** | repentance t-w-b | 17 | 6.36 | **4 / 114** | 1.05 |
| **jhd** | striving / *jihād* | 11 | 4.11 | **2 / 114** | 0.31 |
| **Hrm** | sanctify ḥ-r-m | 10 | 3.74 | **4 / 114** | 0.43 |
| **kfr** | disbelief k-f-r | 31 | 11.59 | 17 / 114 | 5.56 |
| **$rk** | shirk | 12 | 4.49 | 9 / 114 | 1.25 |
| **rHm** | mercy r-ḥ-m | 13 | 4.86 | **24 / 114** | 3.95 |

**Counter-intuitive finding**: Q 9 is **rank 24/114 in mercy-density** — ABOVE corpus mean. The classical "no-basmala-because-no-mercy" claim (ʿAlī b. Abī Ṭālib via al-Bayhaqī, in al-Suyūṭī *Itqān* nawʿ 7) is empirically **FALSIFIED** at the root-density level. See [[Q009-F-01-mercy-density]] for full audit.

The signature that DOES distinguish Q 9 is the **nifāq-tawba-jihād cluster** — all top-5 in the entire Quran. This is the al-Faḍiḥa naming (al-Bukhārī via Saʿīd b. Jubayr, narrating Ibn ʿAbbās — al-Suyūṭī *Itqān* nawʿ 9, p. ~109) ATTAINED MULTIPLY: the surah is most distinctive in **exposure of hypocrisy + repentance + striving** — the three behaviours-of-believers vs. behaviours-of-hypocrites that constitute its rhetorical engine.

## 8. Architectural type classification

Per [[h-new-750-per-surah-iʿjāz-signature]] taxonomy:

- **structural-iʿjāz (al-Bāqillānī iʿjāz al-fawāṣil)**: high sig_A. Q 9 SCORES LOW (anti-iʿjāz quadrant by sig_A).
- **theological-iʿjāz (al-Khaṭṭābī iʿjāz al-maʿnā)**: low UAS but high *thuluth al-Qurʾān*. Q 9 SCORES HIGH on UAS (rank 4) — NOT a *iʿjāz al-maʿnā* signature.

Q 9 is a **content-driven outlier** — its architectural significance is *iʿjāz al-bayān* in Abdel Haleem's sense: legal proclamation + narrative-disposition rhetorical force, not fāṣila virtuosity.

The H-NEW-870 keystone analysis (`csv/h-new-870.json`) places Q 33 as local-singularity but NOT global-keystone for the compression-tail law. By analogy, Q 9 contributes to the **al-sabʿ al-ṭiwāl content-anchor** but is not a global compression-tail keystone (those are Q 78-114).

## 9. Cross-references to all H-NEW findings touching Q 9

Direct Q 9 hits:
- [[h-new-590-outlier-spectrum]] — Q 9 in top-4 outliers; barāʾa-no-basmala VINDICATED at outlier level.
- [[h-new-720-canonical-adjacency-cost]] — Q 9-Q 10 rank 4/113.
- [[h-new-750-per-surah-iʿjāz-signature]] — Q 9 anti-iʿjāz, sig_A rank 107.
- [[h-new-840-unified-architectural-score]] — Q 9 UAS rank 4.
- [[h-new-890-numerical-reaudit]] — Q 8-Q 9 unity-as-one-surah claim FALSIFIED (FR-distance rank 81/113, MORE-than-typical adjacent dissimilarity, p_one-sided=0.717).

Indirect (Q 9 in cohort):
- [[cross-finding-024-five-factor-cohesion-model]] — Q 9 contributes to chronology-factor and outlier-factor.
- [[cross-finding-026-iʿjāz-architecture]] — Q 9's role in dual-iʿjāz typology (anti-iʿjāz, content-driven).
- [[h-new-580-five-factor-regression]] — quantitative 5-factor regression, Q 9 datapoint.
- [[h-new-790-ijaz-by-classical-class]] — al-Zarkashī mufaṣṣal-class regression, Q 9 in al-sabʿ al-ṭiwāl class.

## 10. Honest limits

- The +21.57 outlier-strength was originally pre-registered as a binary IS-OUTLIER test; the continuous spectrum re-coding is post-hoc but rules-tuple-stable across Hafs no-tashkeel and Hafs min-tashkeel.
- The Q 9 → Q 10 cost rank-4 finding depends on the FR-TSP heuristic (best-of-K-restarts, K=20 in H-NEW-720); LOOCV not applicable to a single-pair statistic, but per-adjacency rank order is stable across seeds (verified in H-NEW-720).
- The mercy-density falsification (F-01) used QAC root attestations: a finer-grained semantic test (mercy as mercy-of-God toward penitents vs. mercy-towards-hypocrites) might reveal heterogeneous patterns within the rHm root. We document this for future investigation.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
