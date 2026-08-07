---
surah: 12
surah_name_ar: يوسف
surah_name_translit: Yūsuf
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 12 Yūsuf — Empirical Architectural Profile


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
| **UAS (Unified Architectural Score)** | **4.101** | **6 / 114** | [[h-new-840-unified-architectural-score\|H-NEW-840]] |
| Outlier-strength Δ%ile | **+14.26 pp** | MODERATE_OUTLIER (window {Q 9–15}) | [[h-new-590-outlier-spectrum\|H-NEW-590]] |
| iʿjāz signature sig_A | −2.289 | rank **109 / 114** (very low; STRUCTURAL anti-iʿjāz) | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| iʿjāz signature sig_B | −1.172 | rank 89 / 114 | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| Mean Fisher–Rao distance to corpus | **1.1121** | well above corpus mean 0.9235 | computed from [[h-new-111-fisher-rao-mushaf\|H-NEW-111]] |
| Local cohesion (1-step adjacency) | 0.9723 | z = −0.744 (modestly less cohesive than median) | H-NEW-750 |
| Rhyme entropy (Shannon, nats) | **0.5335** | z = −0.428 (low; near-monorhyme) | H-NEW-750 |
| Top final letter (rāwī) | **ن (nūn)** | **84% of 111 verses** | H-NEW-750 |
| Q 11→Q 12 canonical-adjacency cost | 0.0354 length-units | very low; rank-cluster bottom (cheap transition) | [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] |
| Q 12→Q 13 canonical-adjacency cost | **0.2158 length-units** | rank ≈ 12 / 113 (top-15 expensive) | H-NEW-720 |
| max neighbor canonical-adjacency cost | 0.2158 | the right boundary | H-NEW-720 |
| Verse count | 111 | mid-Meccan length | Hafs-Kufan |
| Word count (no-tashkeel) | 1,912 | computed from `quran-no-tashkeel.json` | |

## 2. The architectural signature: outlier + ALR cluster + structural anti-iʿjāz

Q 12 enters the UAS top-10 (rank 6) by an unusual combination:

1. **MODERATE_OUTLIER (+14.26 pp).** Removing Q 12 from the size-7 corpus-window {Q 9–15} drops mean intra-window content distance percentile from 82.43 to 68.17 ([[h-new-590-outlier-spectrum|H-NEW-590]] `all_surahs_results[X=12]`). Q 12 is content-distinct from the prophet-narrative band Q 9–15 — its uniquely-Yūsuf-saturated vocabulary (root y-s-f at 25/27 ≈ 92.6% of corpus total — see Q012-F-03) sets it apart even from its siblings.

2. **High max-neighbor TSP cost (0.216 length-units).** The Q 12→Q 13 transition is in the corpus's top-15 most-expensive canonical adjacencies. Q 13 al-Raʿd opens with **ALMR** (a different muqaṭṭaʿāt letter-family); the Yūsuf→Raʿd seam is structurally costly. By contrast, the Q 11→Q 12 seam is **almost free** (0.035 length-units, very low rank), because Q 11 Hūd is also ALR and prophet-narrative (cluster member).

3. **Anti-iʿjāz on the structural axis (sig_A rank 109/114).** Q 12 is among the LOWEST surahs in the corpus on the al-Bāqillānī *iʿjāz al-fawāṣil* axis (sig_A = z_local_cohesion + z_neg_mean_content_distance). This is the empirical signature of the **continuous-narrative form**: a sustained narrative arc has high mean content-distance to the rest of the corpus (the lexical world of "well, shirt, cup, dream, prison, ʿaẓīm" is sui generis) and modest local cohesion (the narrative's verse-to-verse adjacency follows story-progression, not refrain).

**Substantive claim**: Q 12 wins UAS rank 6 not via *al-Bāqillānī*-style structural cohesion (which it lacks), but via **content-outlier-strength × canonical-adjacency-cost**. The mushaf "pays" Q 12→Q 13 cost because the narrative content of Yūsuf is sui generis and incompressible to its neighbours.

## 3. Fisher–Rao distance row (Q 12 vs all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` (Fisher–Rao angular on K=500 stem-roots).

**Five nearest neighbours** (Q 12 is closest to *prophet-narrative cluster* surahs):

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 1 | Q 7 al-Aʿrāf | 0.8995 | prophet-narrative; multiple-prophet vignettes |
| 2 | Q 27 al-Naml | 0.9070 | Sulaymān + multiple prophets |
| 3 | Q 28 al-Qaṣaṣ | 0.9133 | Mūsā continuous segments |
| 4 | Q 21 al-Anbiyāʾ | 0.9336 | "the prophets" — multiple |
| 5 | Q 11 Hūd | 0.9638 | ALR cluster + multiple prophets |

The 1-step neighbour Q 11 sits at rank 5 of nearest. The other ALR-cluster members behave as expected: Q 6 al-Anʿām (rank 6, 0.965), Q 10 Yūnus (rank ~9), Q 14 Ibrāhīm and Q 15 al-Ḥijr at greater distance. **Q 12's content-distance signature places it precisely in the prophet-narrative cluster, even though that cluster is NOT united by FR-cohesion (H-NEW-610 found ALR-5 at 56.25%ile NULL on whole-surah cohesion).**

**Five farthest neighbours** (Q 12 is most distinct from short doxological / oath-introduced surahs):

| Rank | Surah | FR distance |
|:-:|:-:|:--:|
| 109 | Q 104 al-Humaza | 1.2237 |
| 110 | Q 92 al-Layl | 1.2259 |
| 111 | Q 90 al-Balad | 1.2289 |
| 112 | Q 97 al-Qadr | 1.2298 |
| 113 | Q 56 al-Wāqiʿa | 1.2417 |
| 114 | Q 80 ʿAbasa | 1.2437 |
| 115 | Q 88 al-Ghāshiya | 1.2616 |
| 116 | Q 55 al-Raḥmān | **1.4185** |

**Q 55 al-Raḥmān is Q 12's most distant surah in the entire corpus** (FR = 1.4185, well above the bilateral max 1.4187). This is the empirical content of the dual-iʿjāz typology: Q 55 is *theological-iʿjāz* (refrain-saturated, nominal-doxological), Q 12 is *narrative-iʿjāz* (verb-driven, sequential, single-protagonist). The two surahs are architecturally near-orthogonal.

## 4. Outlier window structure (H-NEW-590, full Q 9–15 window)

The window {9, 10, 11, 12, 13, 14, 15} (size-7 centred on Q 12) yields:

| Removed surah | d̄_W | d̄_W−X | Δ pp | classification |
|:--:|:--:|:--:|:--:|:--|
| Q 9 al-Tawba | 0.992 | (loosened) | + (anchor side) | recall: Q 9 is itself a STRONG_OUTLIER in another window |
| **Q 12 Yūsuf** | 0.992 | 0.972 | **+14.26** | MODERATE_OUTLIER |
| (others) | — | — | smaller | mixed |

Source: `findings/phase-b-hypotheses/csv/h-new-590.json` `all_surahs_results[X=12]`.

The window itself is high-d̄ (0.992 ≈ corpus median+), meaning the prophet-narrative band Q 9–15 is internally fairly heterogeneous. Q 12's removal tightens the window, identifying Q 12 as the within-band outlier. This is consistent with overview §4: *Q 12 alone is a single continuous narrative; the other ALR cluster members interleave narrative with theological commentary.*

## 5. iʿjāz signature (H-NEW-750)

Q 12 entry from `per_surah` of H-NEW-750:

```json
{"surah": 12, "n_verses": 111,
 "rhyme_entropy_nats": 0.5335, "top_final_letter": "ن", "top_final_letter_frac": 0.8378,
 "mean_content_distance": 1.1121, "local_cohesion": 0.9723,
 "z_rhyme_entropy": -0.4279, "z_mean_content_distance": +1.8614, "z_local_cohesion": -0.7436,
 "sig_A": -2.2893, "sig_B": -1.1715, "rank_A": 109, "rank_B": 89}
```

Component reading:

- **z_mean_content_distance = +1.86** — Q 12 has the **9th-highest mean FR distance to the rest of the corpus** of any surah. Continuous narrative produces a lexical fingerprint that is content-distinct from creedal, eschatological, legal, hymnic registers.
- **z_local_cohesion = −0.74** — Q 12 is mildly *less* cohesive than the corpus median in 1-step adjacency. Verses progress through narrative time, not theme-clusters.
- The two together drive sig_A to −2.29 (rank 109/114). Q 12 is on the **structural anti-iʿjāz** axis: it does NOT exhibit *iʿjāz al-fawāṣil*-style refrain-cohesion; that is not how a story works.
- **rhyme_entropy = 0.534 nats**, **top_final_letter ن at 84% of verses**. The four lowest-rhyme-entropy ALR-cluster members are: Q 12 (0.534) < Q 14 (n.k.) < Q 11 (n.k.) < Q 10 (n.k.); among muqaṭṭaʿāt-29, Q 12 has the lowest rhyme entropy. This is a direct consequence of continuous-narrative form: the imperfective verb suffix -ūn(a) / -īn(a) recurs heavily, and the dialogue-frame `qāla...` produces nominative agentive endings.

## 6. Final-letter audit (rules-tuple stable across all 3 tashkeel variants)

Q 12's per-verse final letter computed from `quran-min-tashkeel.json` (rhyme analysis variant, per protocol §2.1):

| Final | Count | Fraction |
|:--:|:--:|:--:|
| ن (nūn) | 93 | 84.0% |
| م (mīm) | 15 | 13.5% |
| ر (rāʾ) | 2 | 1.8% |
| ل (lām) | 1 | 0.9% |

**Rules-tuple sensitivity**: under no-tashkeel and full-tashkeel, the final-grapheme distribution is identical (rhyme-final letters are unchanged across tashkeel variants — the diacritics decorate but do not replace consonants). Verified by per-variant grep on the three `quran-text/*.json` files.

The **84% nūn-dominance** is what "near-monorhyme" looks like quantitatively. By comparison: Q 55 al-Raḥmān has its 31× refrain *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* in -ān endings, but Q 55's overall rhyme entropy is *higher* than Q 12 because of the alternating refrain/non-refrain structure.

## 7. Connection to ALR muqaṭṭaʿāt cluster

Q 12 is part of the **ALR cluster** (Q 10, 11, 12, 14, 15). Per [[h-new-97]], the ALR-5 set has 4/5 prophet-name-class membership (Yūnus, Hūd, Yūsuf, Ibrāhīm — Q 15 al-Ḥijr is the exception), p=0.006 against the random-5-from-114 null.

But per [[h-new-610-letter-families|H-NEW-610]] / [[h-new-600-letter-families|H-NEW-600]], the ALR-5 is **NULL on whole-surah FR cohesion at 56.25%ile**. The cluster is empirically united by **NAME-CLASS** (4 prophets) but NOT by content-cohesion at FR-roots scale.

Q 12's role inside the ALR cluster is thus distinctive: it is the sole **single-protagonist continuous-narrative** member; the other ALR cluster members (Q 10, 11, 14, 15) interleave the named-prophet's narrative with theological excursions, polemics, and audience addresses (see classical-claim #3 audit in `05-classical-claims-audit.md` for quantification).

## 8. The Q 12 → Q 13 seam (structurally expensive transition)

`h-new-720.json` per_adjacency:

```json
{"s": 11, "pair": [11, 12], "L_constrained": 77.502, "delta": 0.0354, "fraction_residual": 0.426%}
{"s": 12, "pair": [12, 13], "L_constrained": 77.683, "delta": 0.2158, "fraction_residual": 2.602%}
```

The Q 12→Q 13 transition consumes **2.602% of the entire 8.29-unit TSP residual**, which places it in the top-15 most-expensive single adjacencies in the mushaf. The cause: Q 13 al-Raʿd opens with **ALMR** (different letter-family from ALR) and immediately shifts to celestial / dhikr theology. Q 13 sits in an *adjacent-but-different* letter-family with a sharply different content profile.

By contrast, the Q 11→Q 12 seam costs only 0.035 units (0.42%), among the cheapest in the corpus: same letter-family (ALR), same prophet-narrative register, sequential placement. The mushaf accepts a high right-seam cost to achieve the cheap left-seam continuation.

## 9. Cross-references to H-NEW findings

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 12 +14.26 pp MODERATE_OUTLIER.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 6/114; component values cited in §1.
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 12 is *anti-iʿjāz al-fawāṣil* (sig_A rank 109).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 11→Q 12 cheap, Q 12→Q 13 expensive.
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 12 is FR-nearest to Q 7, 27, 28, 21, 11 (prophet-narrative cluster); FR-farthest from Q 55 al-Raḥmān.
- [[h-new-97]] — ALR-cluster prophet-person 4/5, p=0.006.
- [[h-new-610-letter-families|H-NEW-610]] — ALR-5 NULL on whole-surah cohesion at 56.25%ile.
- [[cross-finding-008-muqattaat-book-intro-markers|cross-finding-008]] — Q 12 is prototypical muqaṭṭaʿāt → book-reference (`tilka āyātu al-kitābi al-mubīn`).
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 12 sits at s=12, pre-kink (s<50), so the compression-tail law is in its plateau region; Q 12's d̄ = 1.112 is well above the post-kink trajectory.

## 10. Data sources cited in this file

- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (verse counts, root-level analyses).
- `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json` (rhyme/final-letter audit).
- `/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json` (cross-variant validation).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (FR distance matrix).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json` (outlier spectrum, Q 9–15 window).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json` (rhyme/phoneme distributions).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json` (per-adjacency TSP cost; pairs [11,12] and [12,13]).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json` (per-surah iʿjāz signature).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json` (UAS top-15; Q 12 is rank 6).

## 11. Honest limits

- **rank_A 109/114 is genuinely low** on the structural-iʿjāz axis. This is NOT a deficiency but a sign that *iʿjāz al-fawāṣil*-style metrics are designed for refrain/cohesion-dominant texts; continuous-narrative texts naturally score low. The dual-iʿjāz typology ([[h-new-840]]) explicitly anticipates this orthogonality.
- The MODERATE_OUTLIER classification (+14.26 pp) is real but not a STRONG_OUTLIER (Q 1 +27 / Q 33 +31 / Q 24 +23 / Q 9 +21 are higher). The substantive content-distinctness of Yūsuf is real but moderate.
- **Q 12's nearest-neighbour at distance 0.8995 (Q 7) is itself a 0.21 jump from Q 7's nearest-neighbour minimum** in absolute terms — i.e. Q 12 is an *embedded* outlier, not a global one.
- The per-adjacency cost figures use 2-opt heuristic (best-of-K-restarts); reported as a *constraint cost*, not provably optimal.
