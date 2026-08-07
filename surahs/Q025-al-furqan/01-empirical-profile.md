---
surah: 25
surah_name_ar: الفرقان
surah_name_translit: al-Furqān
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
---

# Q 25 al-Furqān — Empirical profile


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

All metrics computed from project-canonical data sources using the default rules-tuple: `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Sources are cited inline.

## 1. Basic counts (computed)

| Metric | Value | Source |
|:--|:--|:--|
| Verse count | 77 | `quran-text/quran-no-tashkeel.json` Q25.total_verses; cross-checked against Hafs-Kufan |
| Word count (no-tashkeel) | 932 | computed from the same file |
| Letter count (no-tashkeel, sans spaces) | 3,914 | computed |
| QAC total tokens | 896 | `data/morphology/quranic-corpus-morphology-0.4.txt` via [[h-new-126-isolate-core|H-NEW-126]] profile_table |
| QAC unique-root count | 250 | same |
| Mean verse-length (words) | 12.10 | computed |
| Mean verse-length (letters, no-space) | 50.83 | computed |
| Root density (unique-roots / total-tokens) | 0.279 | [[h-new-126-isolate-core|H-NEW-126]] profile |
| First word | تبارك (*tabāraka*) | computed; v.1 first orthographic token |
| Allah-density (per-100v) | 10.39 | [[h-new-126-isolate-core|H-NEW-126]] profile |
| al-Raḥmān count | 3 | computed (vv 26, 59, 60, 63; the *raḥmān*-cluster is concentrated in the back third of the surah, especially in the *ʿibād al-Raḥmān* block) |
| Prophet-narrative density (per-100v) | 3.90 | [[h-new-126-isolate-core|H-NEW-126]] profile (the Mūsā/Hārūn/Nūḥ/ʿĀd/Thamūd/Rass references in vv 35-40 + the v 21/49 prophet-defense) |
| Imperative ratio | 5.19 | [[h-new-126-isolate-core|H-NEW-126]] profile |
| Interrogative ratio | 5.19 | same |
| Declarative ratio | 89.61 | same |

## 2. Length classification

77 verses, 932 words. Length-class:
- al-Suyūṭī tier-system (*al-Itqān* nawʿ 1): **mathānī** — second-tier middle-length surahs (Q 11–Q 49), between al-sabʿ al-ṭiwāl (Q 2–Q 9) and al-mufaṣṣal (Q 50–Q 114).
- al-Zarkashī tier-system (*al-Burhān* ch. 8): mathānī overlapping with the upper-mufaṣṣal-boundary.
- Project length-class (compression-tail kink-50 framework): **pre-kink**, s=25 sits well below the s=50 boundary; expected d̄_content ≈ 0.96 per [[h-new-660-compression-tail-gradient|H-NEW-660]].

## 3. Rhyme structure — near-monorhyme on alif (Shannon entropy 0.069 nats)

Per [[h-new-700-phonological-compression-tail|H-NEW-700]] / [[h-new-750-ijaz-signature|H-NEW-750]]:

| Final letter | Count | Fraction |
|:--|:-:|:-:|
| ا (alif) | 76 | 98.7% |
| (other) | 1 | 1.3% |

- **rhyme_entropy_nats**: **0.0693** (h-new-750 per_surah[surah=25]).
- **top_final_letter**: ا (alif).
- **top_final_letter_frac**: 0.987.
- **Rank**: in the near-monorhyme top-decile (alongside Q 53, 91, 92, 103). Distinct from the corpus-mean (≈ 0.85–1.20 nats).

Classical *sajʿ al-muṭarraf* register (Ibn Abī l-Iṣbaʿ *Badīʿ al-Qurʾān*; al-Suyūṭī *al-Itqān* nawʿ 59). The 76 alif-final fawāṣila ride the *-ā / -an* tanwīn-mansub pattern (*nadhīrā, qadīrā, kabīrā, asīrā, qawāmā, athāmā, lizāmā, mahānā, walīyyā, ḥasīrā, ṣadīqā*, etc.) — uniform-final-tanwīn pattern characteristic of mid-Meccan rhetorical-narrative register.

## 4. iʿjāz signature (h-new-750)

| Field | Value |
|:--|:--|
| sig_A | **−1.828** |
| rank_A | **99 / 114** (rank from top; lower-rank = higher sig_A; rank 99 = LOW sig_A) |
| sig_B | **−1.924** |
| rank_B | **111 / 114** (very LOW; bottom-4-percentile) |
| z_rhyme_entropy | −1.268 (low entropy → near-monorhyme) |
| z_mean_content_distance | +0.559 (slightly higher than corpus mean content-distance) |
| z_local_cohesion | −0.655 (slightly more locally cohesive than corpus mean) |
| local_cohesion | 1.037 |
| mean_content_distance | 0.980 |

Q 25's sig_A and sig_B are both strongly NEGATIVE — i.e., Q 25 is FAR from the high-iʿjāz signature surahs (Q 55 al-Raḥmān, Q 33 al-Aḥzāb, Q 100 al-ʿĀdiyāt). This reflects the very-low rhyme entropy (near-monorhyme) combined with mid-content-distance: low fawāṣil-modulation diversity.

**Architectural type classification**: Q 25 is **STRUCTURAL-IʿJĀZ MEDIATING-HIGH** (UAS rank 13/114, top-15) **but with LOW STRUCTURAL-FORM SIGNATURE** (sig_A/B both low). The UAS-rank-13 verdict is driven by:
1. high *abs_ijaz* (1.83) — driven primarily by the absolute magnitude of the negative sig_B (−1.924);
2. high *max_cost* (0.290) — driven by the Q 24 → Q 25 expensive seam;
3. modest *abs_outlier* (0.75 pp) — Q 25 is a weak window-outlier.

The signature is **not** structural-iʿjāz in the al-Bāqillānī *iʿjāz al-fawāṣil* sense (which would require high fawāṣil-modulation diversity, i.e., HIGH positive sig_A). Instead Q 25's UAS comes from an opposite combination — **extreme-low fawāṣil-diversity** (signs/B sign reversed but magnitude high) + **expensive content-genre-transition with its mushaf neighbor**.

This makes Q 25 a project-novel **inverted-iʿjāz exemplar**: high overall architectural significance, low form-modulation diversity. The classical analogue would be al-Khaṭṭābī's *iʿjāz al-maʿnā* (theological-iʿjāz) — Q 25 wins on content-organization and adjacency-positioning, not on rhetorical-form-diversity. See [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] for the iʿjāz-typology framework.

## 5. UAS (h-new-840 — Unified Architectural Score)

| Field | Value |
|:--|:--|
| UAS | **+1.871** |
| Rank | **13 / 114** (top-15 architectural significance) |
| abs_outlier | 0.75 pp |
| max_cost | 0.2896 (length-units; from the Q 24→Q 25 expensive seam) |
| abs_ijaz | 1.828 |

Q 25 sits just outside the Wave 2026-04-28 UAS top-10 ({Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17}). It is in the **TOP-15 tier**. Its UAS is driven by the **expensive Q 24 → Q 25 seam** (max_cost component) + the **absolute-magnitude-large negative sig_B** (abs_ijaz component).

## 6. Outlier-strength spectrum (h-new-590)

Q 25 weak window-outlier in window {Q 22, 23, 24, 25, 26, 27, 28}:
- Δpp = **+0.75** (positive outlier on root-distribution within window)
- classification: **WEAK_OUTLIER** (Δpp < +5 threshold)
- p_greater_W (window-permutation test): high (not significant after Bonferroni for outlier family)

Q 25 is NOT a sharp-outlier surah on the per-window outlier-spectrum. Its **architectural distinctness** comes from the **Q 24→Q 25 transition seam** + the **isolate-cluster membership**, not from a within-window content-anomaly signal.

## 7. Canonical-adjacency cost (h-new-720)

| Pair | delta_raw | fraction_residual | Rank |
|:--|:-:|:-:|:-:|
| **Q 24 → Q 25** | **+0.2896** | **3.49%** | TOP-15 EXPENSIVE (in the upper-decile of 113 mushaf seams) |
| **Q 25 → Q 26** | +0.0553 | 0.67% | CHEAP (mid-low; in the lower-third of 113 mushaf seams) |

The asymmetry is striking: the seam INTO Q 25 from al-Nūr is expensive; the seam OUT of Q 25 into al-Shuʿarāʾ is cheap. This is consistent with:
- Q 24 al-Nūr running on light-and-modesty-law + ifk register — content-fingerprint disjoint from Q 25's revelation-criterion + polemic + ʿibād-al-Raḥmān register.
- Q 25 al-Furqān → Q 26 al-Shuʿarāʾ both running on prophet-typology + polemic-against-disbeliever-objection register — content-fingerprint overlapping.

al-Biqāʿī's Q 24→Q 25→Q 26 tight-triad munāsabah claim is therefore **FALSIFIED at Q 24→Q 25, VINDICATED at Q 25→Q 26**. The rules-tuple-fragility of the *munāsaba* claim is asymmetric.

## 8. Fisher-Rao content-distance (h-new-111)

| Field | Value |
|:--|:--|
| mean FR-distance to other 113 surahs | 0.980 |
| Rank (mean-d-content; lower = more central) | ~76/114 (mid-content-distant) |
| Top-5 nearest FR-content neighbors | Q 23 al-Muʾminūn (twin candidate), Q 26 al-Shuʿarāʾ (mushaf neighbor), Q 16 al-Naḥl (isolate-core peer), Q 21 al-Anbiyāʾ (isolate-core peer), Q 22 al-Ḥajj (isolate-core peer) |
| Furthest FR-content surahs | the short-Meccan tail (Q 108, 111, 112, 113, 114 — too short to share root-distribution density with Q 25) |

The fact that Q 25's nearest FR-content neighbors include 4 of the 5 H-NEW-126 isolate-core members (Q 16, 21, 22, 23) is **internally consistent** with the isolate-core verdict — the core is FR-content-tight at the surah-pair level within the K=10 nearest-neighbor frame, even while being invisible to all 20 cluster-taxonomy systems. This is the [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] result.

## 9. Compression-tail metrics (h-new-660 / h-new-770)

- s = 25 (pre-kink at s=50). Expected d̄_content ≈ 0.96. Observed mean FR-distance to other 113 ≈ 0.980 (slightly higher than predicted by compression-tail-pre-kink).
- s = 25 (pre-kink at s=50). Expected d̄_rhyme ≈ 0.36. Observed (Q 25 alif at 98.7%, entropy 0.069): Q 25 sits FAR BELOW the rhyme-tail prediction — Q 25 is a near-monorhyme outlier on the rhyme-axis, BUT a within-pre-kink-baseline surah on the content-axis. This is the project-canonical compression-tail-non-applicability for mid-mushaf monorhyme surahs.

## 10. Multi-axis structural type — INVERTED IʿJĀZ

Cross-referencing §3–§9, Q 25's architectural type is:

| Axis | Q 25 score | Architectural type |
|:--|:-:|:--|
| UAS | +1.87 (rank 13) | HIGH structural-architectural significance |
| sig_A | −1.83 (rank 99) | LOW al-Bāqillānī-style *iʿjāz al-fawāṣil* (low fawāṣil-modulation diversity) |
| sig_B | −1.92 (rank 111) | very LOW (extreme low rhyme-entropy with high content-cohesion) |
| outlier | +0.75 pp | WEAK outlier (no sharp window-anomaly) |
| max_cost | 0.290 (top-15) | HIGH adjacency-cost-into-surah (expensive seam from Q 24) |
| mean FR distance | 0.980 (rank ≈76) | mid-content-distant |
| local cohesion | 1.04 | moderate-high (locally cohesive) |
| rhyme entropy | 0.069 (rank top-decile low) | near-monorhyme |

**Type label**: **INVERTED-IʿJĀZ + EXPENSIVE-SEAM + NEAR-MONORHYME + LOCALLY-COHESIVE + ISOLATE-CORE-MEMBER**. This is a distinctive 5-axis structural type. Q 25's combination of (low fawāṣil-modulation) + (high overall UAS) + (expensive seam at predecessor boundary) + (high local cohesion) + (twin-isolate-core peer relations) is project-novel.

## 11. Member of 14-surah sajda cluster (h-new-1330 / h-new-1331)

- Q 25 is the **7th** of the 14 sajda surahs in mushaf order (Q 7, 13, 16, 17, 19, 22, **25**, 27, 32, 38, 41, 53, 84, 96).
- Sajdah verse: **Q 25:60** — *wa-idhā qīla lahumu sjudū li-l-Raḥmāni qālū wa-mā l-Raḥmānu a-nasjudu li-mā taʾmurunā wa-zādahum nufūrā* ۩.
- Per [[h-new-1330-sajda-cluster|H-NEW-1330]] CONFIRMED-NULL: 14 sajda-surahs NOT FR-cohesive on root-distribution.
- Per [[h-new-1331-sajda-muqattaat|H-NEW-1331]] PASS-DIRECTED: sajda × muqaṭṭaʿāt over-represented at 1.97× corpus baseline. Q 25 is NOT among the muqaṭṭaʿāt-opened sajda-surahs (Q 25 opens with *tabāraka alladhī*, not muqaṭṭaʿāt).

## 12. Cross-references to H-NEW findings touching Q 25

| Finding | Q 25 role | Verdict / direction |
|:--|:--|:--|
| [[h-new-111-fisher-rao-mushaf|H-NEW-111]] | Standard FR row | Routine; Q 25 included |
| [[h-new-126-isolate-core|H-NEW-126]] | Named member of true-isolate core of 5 | CONFIRMED at H-NEW-126; Q025-F-01 REFINES to "instrument-fragile isolate" |
| [[h-new-168-q16-q25-dispersion|H-NEW-168]] | Member of Q 16-25 concentrator zone | CONFIRMED; resolves OQ-2 |
| [[h-new-281-true-isolate-core-within-zone-jaccard|H-NEW-281]] | Member of within-zone strongest 5-subset | PASS-DIRECTED rank 8/252 |
| [[h-new-285-oq18-within-zone-contrast|H-NEW-285]] | Member of within-zone more-cohesive-half | PASS-DIRECTED rank 12/252, p=0.0476 |
| [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] | Member of within-zone concept/object-named-class | PASS-DIRECTED p=0.00397 (categorical) |
| [[h-new-590-outlier-spectrum|H-NEW-590]] | Weak window-outlier in {22..28} | DIRECTIONAL/WEAK |
| [[h-new-700-phonological-compression-tail|H-NEW-700]] | Near-monorhyme alif at 98.7% | DESCRIPTIVE |
| [[h-new-720-canonical-adjacency-cost|H-NEW-720]] | Q 24→Q 25 top-15 expensive seam | DESCRIPTIVE / structural |
| [[h-new-750-ijaz-signature|H-NEW-750]] | sig_A rank 99, sig_B rank 111 | DESCRIPTIVE |
| [[h-new-840-unified-architectural-score|H-NEW-840]] | UAS rank 13 / 114 (top-15) | DESCRIPTIVE |
| [[h-new-1330-sajda-cluster|H-NEW-1330]] | Member of 14 sajda-surahs (NOT FR-cohesive) | CONFIRMED-NULL |
| [[h-new-1331-sajda-muqattaat|H-NEW-1331]] | NON-muqaṭṭaʿāt sajda-surah | descriptive |
| [[Q067-al-mulk/00-overview|Q 67]] | *tabāraka alladhī* opener-pair partner | NULL structural twin (Q025-F-03 + Q067-F-06) |

## 13. Honest limits

- Single-source FR matrix (h-new-111) — top-5 nearest-FR enumeration is from one rules-tuple only.
- Q 24 → Q 25 expensive seam = ONE rules-tuple (no-tashkeel / orthographic-token / FR-roots); RT-fragility not yet tested at min-tashkeel / phoneme level.
- UAS components are summed-product on z-scored axes; if any single axis dominates, the overall rank can mask the lopsided distribution. Q 25's UAS=1.87 IS dominated by abs_ijaz (the rhyme-entropy and content-cohesion combination producing abs-large sig_B).
- The "instrument-fragility" verdict on H-NEW-126 (Q025-F-01 NULL) is itself instrument-dependent — the 8 alternative instruments are project-canonical but not exhaustive.
- The *tabāraka alladhī* count of 5 corpus-wide is rules-tuple-stable across no-tashkeel and min-tashkeel variants but has not been verified at full-tashkeel level (where reading-vocalization differences could in principle introduce a 6th case).
