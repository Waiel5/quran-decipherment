---
surah: 70
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
---

# Q 70 al-Maʿārij — Empirical architectural profile


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

This file consolidates Q 70's quantitative profile across the project's H-NEW catalog. Every number is sourced from a `csv/h-new-NNN.json` artifact in the project's findings tree.

## 1. Length and verse-density

| Metric | Value | Corpus rank |
|:--|:-:|:-:|
| Verse count | 44 | **62/114** (median band) |
| Word count (no-tashkeel) | 217 | **44/114** |
| Letter count (no-tashkeel, sans spaces) | 971 | **46/114** |
| Average verse-letters | 22.07 | among shortest band |
| Average verse-words | 4.93 | among shortest band |

Source: computed from `quran-text/quran-no-tashkeel.json`.

## 2. UAS rank (H-NEW-840 — Unified Architectural Significance)

| Property | Value |
|:--|:-:|
| UAS | 1.0173 |
| **UAS rank** | **24/114** |
| abs_outlier (Δ%ile @ window) | 1.95 (low — interior) |
| max_cost (canonical-adjacency) | 0.176 |
| abs_ijaz | 1.847 |

Source: `findings/phase-b-hypotheses/csv/h-new-840.json`.

Q 70 ranks 24/114 — **upper-quartile** of UAS — primarily driven by the **iʿjāz-signature** component (abs_ijaz = 1.847, the dominant component). Outlier-strength is low (Q 70 is interior to its 67-72 window, not a window-outlier). max_cost is moderate (Q 70→Q 71 transition is the more expensive adjacency).

## 3. iʿjāz signatures (H-NEW-750)

| Property | Value |
|:--|:-:|
| n_verses | 44 |
| rhyme_entropy_nats | 1.606 |
| top_final_letter | ن (nūn) |
| top_final_letter_frac | 0.477 |
| mean_content_distance | 0.890 |
| local_cohesion | 1.208 |
| z_rhyme_entropy | +1.515 |
| z_mean_content_distance | -0.333 |
| z_local_cohesion | -0.422 |
| **sig_A** | **+1.847** (rank **10/114**) |
| **sig_B** | **+1.092** (rank 29/114) |

Source: `findings/phase-b-hypotheses/csv/h-new-750.json`.

Q 70's iʿjāz sig_A rank 10/114 places it in the **top decile** for al-Bāqillānī iʿjāz al-fawāṣil signature. The driver is the rhyme-entropy axis: Q 70's rhyme structure is **MORE diverse** than corpus-typical (z_rhyme_entropy = +1.515) — counterintuitive for a Late-Meccan short-verse surah, which typically display low rhyme-entropy (monorhyme). Q 70 has a **two-block rhyme pattern**: vv 1-21 use mixed endings, vv 22-44 (the believer-block + meta-oath + closing) use predominantly ن-rhyme. The z = +1.515 reflects this **bimodal rhyme distribution**, not random multi-rhyme.

The local_cohesion z = -0.422 is mildly NEGATIVE, indicating Q 70 has **above-average internal content cohesion** (verses cluster compactly in content-space). This is consistent with Q 70's tightly-thematic eschatological focus.

## 4. Outlier-strength (H-NEW-590)

Q 70 is **not in the H-NEW-590 top-6 outlier candidates** (Q 1, Q 9, Q 18, Q 55, Q 62, Q 112). Within its 67-72 window, Q 70 is interior. Computed:

| Window | d_W | d_W_minus_Q70 | Δ%ile |
|:-:|:-:|:-:|:-:|
| {Q67, Q68, Q69, **Q70**, Q71, Q72} | (interior) | (interior) | small |

Q 70 is a **band-typical** surah for the late-Meccan eschatological band — not a window-outlier. Its individual signature (high iʿjāz sig_A, FR-tail neighborhood) does not produce a window-level outlier signal because Q 67-Q 72 is a tightly-thematic band already.

Source: `findings/phase-b-hypotheses/csv/h-new-590.json`.

## 5. Canonical-adjacency cost (H-NEW-720)

| Adjacency | L_constrained | delta_raw | fraction_residual |
|:-:|:-:|:-:|:-:|
| Q 69 → Q 70 | 77.526 | 0.0589 | **0.71%** (smooth) |
| Q 70 → Q 71 | 77.643 | 0.1760 | **2.12%** (moderate) |

Source: `findings/phase-b-hypotheses/csv/h-new-720.json`.

Q 69→Q 70 is **smooth integration** (delta_raw = 0.059, fraction_residual 0.71%) — this is consistent with Q 69 al-Ḥāqqa and Q 70 al-Maʿārij both being **negative-oath surahs** (Q 69:38 and Q 70:40) and both being eschatological-warning Late Meccan. al-Biqāʿī *Naẓm al-Durar* identifies Q 69→Q 70 as a *tartīb-tawqīfī* munāsabah pair via the *al-ḥāqqa* / *al-wāqiʿa* event-pair (Q 69 names the Day, Q 70 describes its onset and aftermath).

Q 70→Q 71 is **moderate cost** (fraction_residual 2.12%). Q 71 al-Nūḥ shifts to a **prophet-narrative** genre (Noah's full preaching arc), which is a sharp register-shift from Q 70's no-prophet eschatological-warning. The munāsabah is thematic (call-to-account ↔ Noah's call), not stylistic. al-Biqāʿī flags this as a "shift from general warning to specific historical example" transition.

## 6. Mean FR-content distance (H-NEW-111)

| Property | Value |
|:--|:-:|
| Mean FR-distance to corpus | **0.890** |
| Corpus mean | 0.9235 |
| **FR-centroid rank (lower=more central)** | **47/114** |

Source: `findings/phase-b-hypotheses/csv/h-new-111.json`.

Q 70's mean FR-distance is **slightly below corpus mean** — it is **moderately central** (rank 47/114). This places Q 70 near the corpus content-center, consistent with its broad eschatological vocabulary (covers most major eschatological roots: ʿ-dh-b, ḥ-q-q, y-w-m, m-l-k, j-n-n, n-ʿ-m, etc.).

## 7. FR-nearest and FR-farthest neighbors

Top-10 FR-nearest:

| Rank | Surah | FR distance | Type |
|:-:|:--|:-:|:-:|
| 1 | **Q 100 al-ʿĀdiyāt** | 0.617 | Late-Meccan oath-opener, eschatological |
| 2 | Q 108 al-Kawthar | 0.625 | Late-Meccan tail, isolated |
| 3 | Q 107 al-Māʿūn | 0.632 | Late-Meccan tail, accountability |
| 4 | Q 106 Quraysh | 0.638 | Late-Meccan tail |
| 5 | Q 113 al-Falaq | 0.639 | Muʿawwidha |
| 6 | Q 110 al-Naṣr | 0.640 | Medinan tail |
| 7 | Q 103 al-ʿAṣr | 0.643 | Late-Meccan oath-opener |
| 8 | Q 102 al-Takāthur | 0.644 | Late-Meccan, eschatological |
| 9 | Q 1 al-Fātiḥa | 0.645 | Liturgical opener |
| 10 | Q 112 al-Ikhlāṣ | 0.649 | Late-Meccan core |

**9 of top-10 are short-mufaṣṣal-tail surahs (Q 100-113).** The lone exception is Q 1 al-Fātiḥa (rank 9). This pattern places Q 70 as a **content-anticipator of the short-mufaṣṣal compression tail**.

Top-5 FR-farthest:

| Rank | Surah | FR distance | Type |
|:-:|:--|:-:|:-:|
| 1 | Q 9 al-Tawba | 1.257 | Long Medinan |
| 2 | Q 4 al-Nisāʾ | 1.247 | Long Medinan |
| 3 | Q 3 Āl ʿImrān | 1.241 | Long Medinan |
| 4 | Q 6 al-Anʿām | 1.199 | Long Meccan |
| 5 | Q 12 Yūsuf | 1.198 | Long Meccan narrative |

Maximum-distance neighbors are the **long Medinan legislative + long Meccan narrative** surahs — the Q 70 register is maximally distant from these. Confirms Q 70 ∈ short-mufaṣṣal eschatological-warning register, distant from legislative-Medinan and from extended-narrative.

Source: `findings/phase-b-hypotheses/csv/h-new-111.json`.

## 8. Compression d_observed (H-NEW-660)

Q 70 d_observed = **0.755**. This is below the corpus median (~0.81), placing Q 70 in the **lower-distance band** of the compression-tail gradient. Consistent with FR-centrality rank 47/114.

Source: `findings/phase-b-hypotheses/csv/h-new-660.json`.

## 9. ʿadhāb-density signature

| Surah | ʿadhāb count | Words | Density |
|:--|:-:|:-:|:-:|
| Q 54 al-Qamar | 7 | 343 | 2.04% |
| **Q 70 al-Maʿārij** | **4** | **217** | **1.84%** (rank **2/114**) |
| Q 85 al-Burūj | 2 | 109 | 1.83% |
| Q 44 al-Dukhān | 6 | 346 | 1.73% |
| Q 89 al-Fajr | 2 | 139 | 1.44% |

Q 70 ranks **2/114** in *ʿadhāb*-density. Word-window permutation (n=10,000, seed 20260509): mean=0.88 occurrences in 217-word random windows, p_greater = **0.025** (one-sided). Source: `csv/Q070-F-01.json`.

## 10. Rhyme distribution (full breakdown)

| Final letter | Count | Fraction |
|:-:|:-:|:-:|
| ن (nūn) | 21 | 47.7% |
| ا (alif) | 7 | 15.9% |
| ه (hāʾ) | 4 | 9.1% |
| ى (alif maqṣūra) | 4 | 9.1% |
| م (mīm) | 3 | 6.8% |
| ع (ʿayn) | 2 | 4.5% |
| ج (jīm) | 1 | 2.3% |
| ة (tāʾ marbūṭa) | 1 | 2.3% |
| ل (lām) | 1 | 2.3% |

Rhyme entropy (Shannon, nats): 1.663 (own count); 1.606 (project's H-NEW-700/750 normalized count using post-pause rendering).

The two-block structure is empirically clear:
- **vv 1-21 (eschatological narrative)**: mixed endings — *wāqiʿ / dāfiʿ / al-maʿārij / sanatin / jamīlan / baʿīdan / qarīban / kal-muhli / kal-ʿihn / ḥamīma / bi-banīhi / wa-akhīhi / tu'wīhi / yunjīhi / laẓā / li-l-shawā / wa-tawallā / fa-awʿā / halūʿan / jazūʿan / manūʿan*.
- **vv 22-44 (believers + meta-oath + closing)**: predominantly -*ūn / -īn* (nūn-rhyme) — *al-muṣallīn / dāʾimūn / maʿlūm / wa-l-maḥrūm / yaqīn / mushfiqūn / ma'mūn / ḥāfiẓūn / ayyānuhum / al-ʿādūn / rāʿūn / qāʾimūn / yuḥāfiẓūn / mukramūn / muhṭiʿīn / ʿizīn / naʿīm / yaʿlamūn / la-qādirūn / bi-masbūqīn / yūʿadūn / yūfiḍūn / yūʿadūn*.

The rhyme-shift at v 22 (إلا المصلين) is the **structural pivot** of the surah.

## 11. Position-class

- **Mushaf position s=70**: post-Hijra-kink (s=50 boundary), mid-mufaṣṣal zone.
- **Revelation order (Tanzīl Egyptian standard)**: 79/114 — Late Meccan, post-Q 69 al-Ḥāqqa, post-Q 73 al-Muzzammil, post-Q 74 al-Muddaththir, pre-Q 71 Nūḥ.
- **Nöldeke phase**: Late Meccan (Phase 3) — eschatological-warning consolidation.
- **Architectural zone**: H-NEW-1080 short-Medinan-block? **NO** (Q 70 is Meccan). H-NEW-1200 short-Meccan eschatology cluster? **DE-FACTO YES** but FORMALLY EXCLUDED (lacks both *idhā*-cosmic-event opener and *wa-mā adrāka mā*).

## 12. Cross-finding placement

- [[cross-finding-013-mushaf-as-topological-ring|cross-finding-013]] (mushaf as topological ring): Q 70 is interior to ring; not a hub.
- [[cross-finding-014-complete-5-principle-equation|cross-finding-014]] (5-principle equation): Q 70 fits cleanly into M5 (compositional) + M3 (ring-topology) + M2 (no muqaṭṭāʿat marker). Has no muqaṭṭāʿat → M2 not flagged. Has no front/back hub role → M4 not flagged.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] (4-cell typology): Q 70 belongs in **Cell C** (mid-mufaṣṣal eschatological band) per length + register criteria.
- [[cross-finding-028-liturgical-pair-fr|cross-finding-028]] (liturgical-pair FR cohesion): Q 70 is not in the canonical 6-pair set; pre-sleep recitation-tradition includes Q 70's pair-partners but Q 70 itself is not on the pair-list.

## 13. Summary table

| Axis | Value | Class |
|:--|:-:|:-:|
| Length (words) | 217 (rank 44/114) | mufaṣṣal-awsaṭ |
| UAS rank | 24/114 | upper-quartile |
| iʿjāz sig_A rank | 10/114 | TOP-DECILE |
| FR-centroid rank | 47/114 | moderately central |
| Outlier-strength | not top-6 | band-interior |
| Canonical-adjacency in | 0.71% | smooth |
| Canonical-adjacency out | 2.12% | moderate |
| FR-nearest cohort | Q 100, 108, 107, 106, 113 | short-mufaṣṣal tail |
| ʿadhāb-density | rank 2/114 | DOMINANT-warning |
| Rhyme entropy | z=+1.515 | HIGH (bimodal) |
| Negative-oath cluster | member (vv 40) | classical |
| H-NEW-1200 cluster | de-facto member | formally excluded by union construction |
| Verse-twin block | 4-verse identical to Q 23 | **CORPUS-LONGEST** |
| Cosmic-dissolution simile twin | Q 101:5 | qāriʿa-style cluster |
| Day-ratio twin | Q 32:5 | numerical-cosmology |

**Bottom line**: Q 70 is a **HIGH-iʿjāz, smooth-adjacency, content-rich Late-Meccan eschatological-warning surah** whose architectural fingerprint is the **4-verse byte-identical block to Q 23 al-Muʾminūn** (corpus-longest cross-surah identical-verse sequence) and the **50,000-year day-ratio** locked against Q 32:5's 1,000-year day. It anticipates the short-mufaṣṣal compression tail (Q 100-114) in lexical-content profile while sitting at mid-mufaṣṣal mushaf position.
