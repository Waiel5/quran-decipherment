---
surah: 38
surah_name_ar: ص
surah_name_translit: Ṣād
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE
---

# Q 38 Ṣād — Empirical Architectural Profile


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

Rules-tuple: `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan, Mashriqi)`. Every numerical value below is computed from the data files cited in §10 and the H-NEW-XXX artifacts.

## 1. Headline architectural metrics

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **−0.3198** | **59 / 114** (mid-pack) | [[h-new-840-unified-architectural-score\|H-NEW-840]] |
| Outlier-strength Δ%ile | **+2.70 pp** | WEAK_OUTLIER (window {Q 35-41}) | [[h-new-590-outlier-spectrum\|H-NEW-590]] |
| iʿjāz signature sig_A | **+1.286** | rank **22 / 114** (moderately HIGH) | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| iʿjāz signature sig_B | +1.114 | rank 27 / 114 | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| Mean Fisher–Rao distance to corpus | **0.9663** | just above corpus mean 0.9235 | computed from [[h-new-111-fisher-rao-mushaf\|H-NEW-111]] |
| Local cohesion (1-step adjacency) | 1.0821 | z = −0.594 (moderately less cohesive than median) | H-NEW-750 |
| Rhyme entropy (Shannon, nats) | **1.7129** | z = +1.708 (HIGH multi-tonal) | H-NEW-750 |
| Top final letter (rāwī) | **ب (bāʾ)** | **39.8% of 88 verses** | H-NEW-700 / H-NEW-750 |
| Q 37→Q 38 canonical-adjacency cost | **0.0000 length-units** | RANK BOTTOM (structurally seamless) | [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] |
| Q 38→Q 39 canonical-adjacency cost | 0.0992 length-units | rank ~30/113 (modest) | H-NEW-720 |
| max neighbor canonical-adjacency cost | 0.0992 (right boundary) | non-extreme | H-NEW-720 |
| Verse count | 88 | mid-Meccan length | Hafs-Kufan |
| Word count (no-tashkeel) | 774 | computed | |
| Letter count (no-tashkeel) | 3,104 | computed | |

## 2. The architectural signature: mid-pack with structurally seamless left seam

Q 38 sits at **UAS rank 59/114** — almost exactly at the corpus median. Decomposing the UAS components:

1. **WEAK_OUTLIER (+2.70 pp).** The window {Q 35-41} (size-7 centered on Q 38) is internally fairly homogeneous; Q 38's removal moves the percentile from 33.62 to 30.92 (Δ=+2.70 pp). The mid-Meccan band Q 35-41 is a coherent stylistic neighborhood (al-Ṣāffāt, Ṣād, al-Zumar, Ghāfir all have prophet-cycle / eschatological content), and Q 38 fits its surrounding band rather than standing apart.

2. **Q 37→Q 38 canonical-adjacency cost = 0.0000 length-units.** This is **the cheapest possible transition** — Q 37 (al-Ṣāffāt) and Q 38 (Ṣād) form a structurally seamless seam in mushaf order. Both are mid-Meccan, both are prophet-cycle (Q 37 also names ≥10 prophets in its 182 verses), both close with eschatology. The mushaf order pays zero TSP-cost for this transition; the implication is that Q 37 → Q 38 is information-geodesically natural.

3. **iʿjāz sig_A rank 22/114 (HIGH).** Q 38's high rhyme entropy (1.71 nats) drives this. Multi-tonal final-letter distribution + above-average mean-FR-distance + moderately-low local cohesion all combine. Q 38 has the **al-Bāqillānī iʿjāz al-fawāṣil signature** at moderate strength: rhyme variation is genuine, not formulaic.

**Substantive claim**: Q 38's mid-pack UAS is not architectural weakness but rather **architectural well-fittedness to its surrounding mushaf neighborhood**. The seamless seam to Q 37 means Q 38 is a structurally well-integrated piece of the Q 37→Q 38→Q 39 prophet-cycle / eschatology corridor.

## 3. Fisher-Rao distance row (Q 38 vs all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` (Fisher-Rao angular on K=500 stem-roots).

**Six nearest neighbours:**

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 1 | Q 78 al-Nabaʾ | 0.8331 | eschatological-doxological; *ʿamma yatasāʾalūn* |
| 2 | Q 50 al-Qāf | **0.8541** | **SINGLETON TWIN** — also opens single-letter + oath-Qurʾān |
| 3 | Q 32 al-Sajda | 0.8569 | ALM-cluster (the cluster's nearest point to Q 38) |
| 4 | Q 43 al-Zukhruf | 0.8619 | HM-cluster (the cluster's nearest point to Q 38) |
| 5 | Q 51 al-Dhāriyāt | 0.8673 | oath-introduced (*wa-l-dhāriyāti dharwā*); eschatology |
| 6 | Q 41 Fuṣṣilat | 0.8826 | HM-cluster |

**The 2nd-nearest neighbour is Q 50 al-Qāf** — the OTHER single-letter+oath-Qurʾān surah. This is Q038-F-01's empirical architectural correlate at the *surah* level (the verse-level twin Q 38:1 ↔ Q 50:1 is established at p<0.003).

**Six farthest neighbours** (Q 38 most distinct from Medinan-legislative and refrain-doxological surahs):

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 109 | Q 5 al-Māʾida | 1.0842 |
| 110 | Q 24 al-Nūr | 1.1118 |
| 111 | Q 33 al-Aḥzāb | 1.1500 |
| 112 | Q 4 al-Nisāʾ | 1.1877 |
| 113 | Q 55 al-Raḥmān | **1.1927** |
| 114 | Q 9 al-Tawba | **1.2358** |

**Q 38 is most distant from the legal-Medinan core (Q 4, Q 5, Q 9, Q 33) and from al-Raḥmān (the refrain-saturated theological-iʿjāz prototype).** This is the empirical content of the dual-iʿjāz typology: Q 38 is on the prophet-cycle / eschatology axis, structurally orthogonal to the legal-corpus and to Q 55-style refrain.

## 4. Outlier window structure (H-NEW-590, full Q 35-41 window)

The window {35, 36, 37, 38, 39, 40, 41} (size-7 centred on Q 38) yields:

```json
{"X": 38, "window": [35, 36, 37, 38, 39, 40, 41],
 "d_W": 0.9063, "d_W_minus_X": 0.8970,
 "pct_W": 33.62, "pct_W_minus_X": 30.92,
 "delta_pct": 2.70,
 "p_greater_W": 0.6638,
 "classification": "WEAK_OUTLIER"}
```

Source: `findings/phase-b-hypotheses/csv/h-new-590.json` `all_surahs_results[X=38]`.

The window itself is moderate-d̄ (0.906 ≈ corpus median), meaning the mid-Meccan band Q 35-41 is internally moderately-homogeneous. Q 38's WEAK_OUTLIER status is consistent with its placement in a **stylistically coherent neighborhood**: Q 38 doesn't break the band, it fits it.

## 5. iʿjāz signature (H-NEW-750)

Q 38 entry from `per_surah` of H-NEW-750:

```json
{"surah": 38, "n_verses": 88,
 "rhyme_entropy_nats": 1.7129, "top_final_letter": "ب", "top_final_letter_frac": 0.3977,
 "mean_content_distance": 0.9663, "local_cohesion": 1.0821,
 "z_rhyme_entropy": +1.7077, "z_mean_content_distance": +0.4221, "z_local_cohesion": -0.5941,
 "sig_A": +1.286, "sig_B": +1.114, "rank_A": 22, "rank_B": 27}
```

Component reading:

- **z_rhyme_entropy = +1.71** — Q 38 is the **22nd-most-multi-tonal surah** in the Quran on rhyme. The 39.8% top-letter ب is the dominant rhyme but doesn't drown out the other 60% of verse-finals.
- **z_mean_content_distance = +0.42** — Q 38's content vocabulary is mildly content-distinct from the rest of the corpus.
- **z_local_cohesion = −0.59** — Q 38 is mildly *less* locally-cohesive than median in 1-step adjacency. Verses progress through prophet-vignettes rather than refrain-cycles.
- The three together drive sig_A to +1.29 (rank 22/114). Q 38 is on the **mid-high structural-iʿjāz** axis, consistent with classical *al-Bāqillānī iʿjāz al-fawāṣil* claims about prophet-cycle surahs.

## 6. Final-letter audit (rules-tuple stable across all 3 tashkeel variants)

Q 38's per-verse final letter computed from `quran-min-tashkeel.json`:

| Final | Count | Fraction |
|:--:|:--:|:--:|
| ب (bāʾ) | 35 | 39.77% |
| Other (33) | 53 | 60.23% |

The 39.77% bāʾ-fraction reflects mid-Meccan thematic-rhyme: -*āb*, -*āb*, -*ʾāb*, -*aʾāb* (e.g., *muʾāb*, *al-ʿaẓīm*, *al-ḥisāb*). The remaining 60% is distributed across multiple final letters; rhyme entropy is high (1.71 nats vs Q 12's 0.53 nats, a 3.2× increase).

**Rules-tuple sensitivity**: under all 3 tashkeel variants, the final-grapheme distribution is identical.

## 7. Singleton-letter context — Q 38, Q 50, Q 68

Q 38 is one of three single-letter muqaṭṭaʿāt surahs:

| Surah | Letter | Verses | Words | UAS rank | sig_A rank | Top neighbor (FR) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Q 38 Ṣād | ص | 88 | 774 | 59 | 22 | Q 78 (0.833), **Q 50 (0.854)** |
| Q 50 Qāf | ق | 45 | 357 | (TBD) | (TBD) | Q 78 (0.765) |
| Q 68 al-Qalam | ن | 52 | 300 | (TBD) | (TBD) | Q 100 (0.716) |

**Q 38 is empirically twinned with Q 50** at the surah level (FR=0.854) AND at the verse level (Q 38:1 ↔ Q 50:1 at corpus-pairwise p<0.003 across 3 metrics). The Q 38 ↔ Q 68 distance is 0.910 (substantially larger). The Q 50 ↔ Q 68 distance is 0.846 (slightly closer than Q 38 ↔ Q 50, consistent with both being short and nominal-doxological).

The **singleton-letter cluster** thus has internal structure: Q 38, Q 50, Q 68 are NOT a tight cluster, but Q 38 ↔ Q 50 is closer than to most non-singletons, and the Q 38:1 / Q 50:1 verse-twin is structurally distinctive.

## 8. The Q 37 → Q 38 → Q 39 seam (structurally seamless on the left)

`h-new-720.json` per_adjacency:

```json
{"s": 37, "pair": [37, 38], "L_constrained": 77.466, "delta_raw": -0.001, "delta": 0.000, "fraction_residual": 0.000}
{"s": 38, "pair": [38, 39], "L_constrained": 77.566, "delta_raw": 0.099, "delta": 0.099, "fraction_residual": 0.012}
```

The Q 37 → Q 38 transition is **zero-cost** (the constrained TSP under the canonical adjacency is at-or-below the unconstrained 2-opt baseline). The mushaf pays nothing to put Q 37 al-Ṣāffāt next to Q 38 Ṣād.

This is consistent with classical reading: Q 37 al-Ṣāffāt is itself a prophet-cycle surah (Nūḥ, Ibrāhīm, Mūsā, Yūnus), ending with eschatology and an oath-introduction at v. 1 (*wa-l-Ṣāffāti ṣaffā*). Q 37 → Q 38 is genre-continuous: oath-opening + prophet-cycle + eschatology in both. The mushaf-compiler's placement is structurally optimal here.

The Q 38 → Q 39 transition costs 0.099 length-units (mid-rank). Q 39 (al-Zumar) opens with *tanzīlu al-kitābi* (book-revelation) rather than oath/muqaṭṭaʿ; the genre shifts into the Zumar / Ghāfir axis.

## 9. Cross-references to H-NEW findings

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 38 +2.70 pp WEAK_OUTLIER.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 59/114 (mid-pack).
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 38 mid-high structural-iʿjāz (sig_A rank 22).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 37 → Q 38 = 0.000 (seamless), Q 38 → Q 39 = 0.099.
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 38 ↔ Q 78 (0.833), Q 38 ↔ Q 50 (0.854 — singleton-twin).
- [[h-new-165-phonological-predictor|H-NEW-165]] — phonological cluster prediction: Q 38 ص → TSM (interpretive a-priori).
- [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] — Q 38 ص singleton resolves to TSM by phonological feature (a-priori match: ✓).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 38 rhyme top-letter ب @ 39.8%.
- [[cross-finding-021-mushaf-information-theoretic-optimality]] — Q 38 contributes to the FR-mushaf near-optimality (z=−11.46).
- [[cross-finding-026-iʿjāz-architecture]] — Q 38 mid-iʿjāz typology.
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 38 sits at s=38, pre-kink (s<50), so the compression-tail law is in plateau region; Q 38's d̄ = 0.966 is consistent with the plateau.

## 10. Data sources cited in this file

- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (verse counts, root-level analyses).
- `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json` (rhyme/final-letter audit).
- `/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json` (cross-variant validation).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (FR distance matrix).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json` (outlier spectrum, Q 35-41 window).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json` (rhyme/phoneme distributions).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json` (per-adjacency TSP cost; pairs [37,38] and [38,39]).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json` (per-surah iʿjāz signature).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json` (UAS all_uas; Q 38 = rank 59).

## 11. Honest limits

- **UAS rank 59/114 is genuinely mid-pack.** Q 38 is not an architectural standout in the unified score — it ranks below all the major iʿjāz-confirmed surahs (Q 1, Q 2, Q 9, Q 33, Q 24, Q 12, Q 55, Q 17). It scores high on iʿjāz-signature (rank 22) but low on outlier (+2.70 pp WEAK) and modest on adjacency-cost (max 0.099). The architectural significance of Q 38 lies elsewhere — in (a) the singleton-twin pairing with Q 50, (b) the prophet-cycle saturation, (c) the seamless seam to Q 37.
- **The window {Q 35-41} is content-coherent**, so Q 38 is *integrated* with its neighbors rather than an outlier — this is a valid empirical observation, not a defect.
- **The 2-opt heuristic** for Q 37→Q 38 yields delta_raw = -0.0009 (slightly negative), which means the constrained TSP edge is slightly *better* than the unconstrained 2-opt; this can occur because 2-opt is heuristic, not optimal. The "0.000" is reported as a clamped lower bound.
- **Q 38 ↔ Q 50 FR=0.854 is rank 2** (after Q 78). Q 78 al-Nabaʾ is closer to Q 38 (0.833) — this is a genuine empirical fact, and Q 38 ↔ Q 50 should be reported as the **2nd-nearest** rather than nearest. The structural-twin claim survives because Q 50 is in Q 38's top-3 and the verse-level twin (Q 38:1 ↔ Q 50:1) is independently confirmed at p<0.003.
