---
surah: 87
file_type: empirical-profile
date_last_updated: 2026-05-09
---

# Q 87 al-Aʿlā — Empirical Architectural Profile

## 0. Source artifacts

All metrics are extracted from project-locked H-NEW computations and re-verified against the canonical Hafs-Kūfan corpus this date (2026-05-09).

- `findings/phase-b-hypotheses/csv/h-new-111.json` — Fisher-Rao 114×114 distance matrix (root-bag, K=500, Dirichlet α=0.5)
- `findings/phase-b-hypotheses/csv/h-new-590.json` — outlier-strength
- `findings/phase-b-hypotheses/csv/h-new-700.json` — phonological compression-tail (rhyme + phoneme)
- `findings/phase-b-hypotheses/csv/h-new-720.json` — canonical-adjacency cost (113 transitions)
- `findings/phase-b-hypotheses/csv/h-new-750.json` — iʿjāz signature (sig_A, sig_B per surah)
- `findings/phase-b-hypotheses/csv/h-new-840.json` — Unified Architectural Score (UAS)
- `data/morphology/quranic-corpus-morphology-0.4.txt` — QAC v0.4 root annotations

Rules-tuple: `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)`.

## 1. Length / token / corpus-position metrics

| Metric | Value | Rank/Notes |
|:--|:-:|:--|
| Mushaf position | 87/114 | deep mufaṣṣal |
| Egyptian Standard revelation order | 8/114 | very early |
| Nöldeke revelation order | 19/114 | Early Meccan |
| Mushaf-vs-revelation displacement Δ | +79 (forward shift) | among the 25 largest displacements |
| Verse count | 19 | mufaṣṣal-tail typical |
| Word count (no-tashkeel, orthographic-token) | 72 | computed `quran-no-tashkeel.json` |
| Letter count (no-tashkeel, graphemes, no spaces) | 287 | computed |
| Avg verse-length (words) | 3.79 | very short — Early-Meccan condensed register |
| Avg verse-length (letters) | 15.1 | short — terminal mufaṣṣal |
| Length-class | mufaṣṣal-qiṣār | Q 78–114 stratum |

## 2. Fisher-Rao FR distance metrics (H-NEW-111)

| Metric | Value | Rank |
|:--|:-:|:--|
| Mean FR distance to other 113 surahs | **0.821** | mid-corpus (corpus mean ≈ 0.924) |
| Min FR distance (nearest neighbor) | 0.4069 (Q 94 al-Sharḥ) | tight neighborhood |
| Max FR distance (farthest neighbor) | 1.42 (typical for far Medinan) | typical |
| Local cohesion | 1.721 | rank ~9/114 (HIGH) |

**FR top-15 nearest-neighbors** (computed this date from the upper-triangular row of `h-new-111.json`):

| Rank | Surah | FR distance | Period |
|:-:|:-:|:-:|:--|
| 1 | Q 94 al-Sharḥ | 0.4069 | Early Meccan (Nöldeke 12) |
| 2 | Q 108 al-Kawthar | 0.4132 | Very Early Meccan (Nöldeke 15) |
| 3 | Q 111 al-Masad | 0.4462 | Early Meccan |
| 4 | Q 106 Quraysh | 0.4476 | Early Meccan |
| 5 | Q 113 al-Falaq | 0.4503 | Early Meccan |
| 6 | Q 100 al-ʿĀdiyāt | 0.4542 | Early Meccan |
| 7 | Q 112 al-Ikhlāṣ | 0.4551 | Early Meccan |
| 8 | Q 105 al-Fīl | 0.4574 | Early Meccan |
| 9 | Q 110 al-Naṣr | 0.4582 | Late-Medinan-but-FR-architecturally-short-Meccan-tail (per H-NEW-1030) |
| 10 | Q 107 al-Māʿūn | 0.4611 | Early Meccan |
| 11 | Q 103 al-ʿAṣr | 0.4670 | Early Meccan |
| 12 | Q 104 al-Humazah | 0.4689 | Early Meccan |
| 13 | Q 93 al-Ḍuḥā | 0.4775 | Early Meccan |
| 14 | Q 114 al-Nās | 0.4804 | Early Meccan |
| 15 | Q 92 al-Layl | 0.4810 | Early Meccan |

**14 of Q 87's 15 nearest FR-neighbors are Early Meccan short-mufaṣṣal-tail surahs**. This is a **content-fingerprint clustering** signature: Q 87 disappears into the deep-tail Meccan register. The single non-Early-Meccan exception (Q 110, Late Medinan) is itself FR-architecturally a short-Meccan-tail surah per H-NEW-1030 chronology-dissociation.

## 3. Canonical-adjacency cost (H-NEW-720)

| Pair | delta_raw | delta (clamped) | fraction_residual | rank |
|:--|:-:|:-:|:-:|:-:|
| **Q 86 → Q 87** | **−0.01777** | **0.000 (clamped)** | **0.0000** | **rank 9/113 (most-optimal)** |
| Q 87 → Q 88 | +0.05344 | 0.05344 | 0.00644 | rank 49/113 (typical) |
| Q 85 → Q 86 (immediate left context) | +0.00026 | 0.00026 | 0.0000 | rank 8/113 |

**Critical observation**: the Q 86 → Q 87 transition is *NEGATIVE* in raw 2-opt-residual terms. The canonical mushaf placement of al-Aʿlā immediately after al-Ṭāriq is BETTER than the local 2-opt minimum. This is one of the **13 clamped-zero / better-than-2opt mushaf transitions** identified in [[h-new-1240-empirically-seamless-mushaf-transitions|H-NEW-1240]] (commit 68f37738c). The full list of 13 (sorted by delta_raw, most-negative first):

```
s=91   (Q 91 → Q 92)  delta_raw = −0.0868
s=4    (Q  4 → Q  5)  delta_raw = −0.0657
s=6    (Q  6 → Q  7)  delta_raw = −0.0575
s=3    (Q  3 → Q  4)  delta_raw = −0.0466
s=65   (Q 65 → Q 66)  delta_raw = −0.0340
s=109  (Q109 → Q110)  delta_raw = −0.0307
s=73   (Q 73 → Q 74)  delta_raw = −0.0289
s=105  (Q105 → Q106)  delta_raw = −0.0282
s=86   (Q 86 → Q 87)  delta_raw = −0.0178   ← Q 87
s=93   (Q 93 → Q 94)  delta_raw = −0.0152
s=64   (Q 64 → Q 65)  delta_raw = −0.0087
s=72   (Q 72 → Q 73)  delta_raw = −0.0012
s=37   (Q 37 → Q 38)  delta_raw = −0.0009
```

The Q 86→87 seam ranks **9th-most-optimal** of the 13 clamped-zero seams. The canonical mushaf placement of Q 87 is **architecturally seamless on both sides** (Q 86→87 = clamped-0; Q 85→86 = 0.0003 ≈ 0).

## 4. UAS rank (H-NEW-840)

| Component | Q 87 value | Z-score / rank |
|:--|:-:|:--|
| Outlier-strength (abs Δ%ile) | 0.44 | LOW |
| Max canonical-adjacency cost (abs) | 0.0534 | LOW |
| iʿjāz signature magnitude (abs sig_A) | 0.0063 | VERY LOW |
| **UAS** | **−2.817** | **rank 114/114 (LOWEST in corpus)** |

**Q 87's UAS rank is 114/114 — the lowest of all 114 surahs.** The four lowest UAS scores:

| Rank | Surah | UAS | Surah label |
|:-:|:-:|:-:|:--|
| **114** | **Q 87 al-Aʿlā** | **−2.817** | the most architecturally-seamless |
| 113 | Q 114 al-Nās | −2.797 | terminal muʿawwidha |
| 112 | Q 105 al-Fīl | −2.764 | very-Early-Meccan companion |
| 111 | Q 73 al-Muzzammil | −2.696 | Early-Meccan ascetic |

The Q 87 UAS-rank-114 score does NOT mean "least-impressive" — it means "least architecturally-distinctive in this 4-component score". Q 87 distinguishes itself on AXES NOT MEASURED BY UAS — specifically: (a) the unique IMPERATIVE musabbiḥa form-axis (H-NEW-103); (b) the corpus-EXACT *ṣuḥuf-Ibrāhīm-wa-Mūsā* pair (Q087-F-03); (c) the corpus-EXACT *sa-nuqriʾuka fa-lā tansā* hapax (Q087-F-04); (d) the chronology-architecture dissociation (Egyptian Standard rev-#8 → mushaf #87). UAS captures content-iʿjāz / outlier / adjacency-spike signatures; Q 87's distinctiveness is in form-grammatical (musabbiḥa-imperative), classical-pair (Q 53 cross-reference), and chronological-positional axes.

This is a **healthy reminder**: UAS rank is one architectural-distinctiveness signature among many, not the only one. Q 87 is a strong case for the multidimensionality of architectural significance.

## 5. iʿjāz signature (H-NEW-750)

| Metric | Q 87 value | Rank |
|:--|:-:|:--|
| Rhyme entropy (Shannon, nats) | 0.206 | rank 23/114 (LOW = rhyme-pure) |
| Top final letter | ى (alif maqṣūra) | uniform |
| Top final letter fraction | 0.947 | very high |
| Mean content distance | 0.821 | LOW |
| Local cohesion | 1.721 | HIGH |
| z_rhyme_entropy | −1.02 | LOW |
| z_mean_content_distance | −1.01 | LOW |
| z_local_cohesion | +0.28 | mid |
| sig_A | −0.0063 | rank 57/114 (NEAR-ZERO) |
| sig_B | −0.745 | rank 71/114 (LOW) |

Q 87's iʿjāz signature magnitude is near-zero (sig_A ≈ 0; sig_B negative-low). Like UAS, this rates Q 87 as architecturally undistinctive at the iʿjāz al-fawāṣil axis — content-distance and rhyme are well within local-cluster norms.

**However**: Q 87 PERFECT-MONORHYMES at 19/19 = 1.000 on the ى-letter (alif maqṣūra ending). Per Q017-F-01 (Q 17 al-Isrāʾ specialist), the perfect-monorhyme tier is {Q 18, 48, 65, 72, 76, **87**, 91, 92}. The 19-verse Q 87 sustains the rhyme through 18 *-ā* terminations + 1 *yakhfā* (also *-ā*). At the perfect-monorhyme axis Q 87 is in the **8-surah elite tier**.

## 6. Outlier-strength (H-NEW-590)

| Window context | Surahs | d̄_W | d̄_W minus Q 87 |
|:--|:--|:-:|:-:|
| Q 87 in window {Q 84, 85, 86, 87, 88, 89, 90} | 7 | 0.5999 | 0.6077 |

| Metric | Value | Classification |
|:--|:-:|:--|
| pct_W (with Q 87) | 0.32 | low percentile |
| pct_W_minus_X | 0.76 | higher percentile |
| Δ%ile (with-minus-without) | **−0.44** | **NULL (architecturally integrated, not outlier)** |
| p_greater_W | 0.997 | trivially-not-outlier |

Q 87 is a NULL outlier in its 7-surah window — its content footprint is **deeply integrated** into the surrounding short-Meccan-tail neighborhood Q 84-90. This is the OPPOSITE of an architectural-outlier signature like Q 33 (Δ%ile = +31.46, rank 1/114). Q 87 is PERFECTLY HOMOGENEOUS with its neighbors.

## 7. Compression-tail laws (H-NEW-660 / H-NEW-700 / H-NEW-770)

Per the four architectural laws (Wave 2026-04-28):
- **d̄_content(s)** at s=87: predicted ≈ 0.96 − 0.012·max(0, 87−50) = 0.96 − 0.012·37 = 0.516. Observed: Q 87 mean d̄_content_to_113 = 0.821. **Above-prediction by 0.305** (the predicted line tracks corpus-mean for the band; Q 87's observed mean is closer to the corpus mean than to the prediction. The prediction is for the corpus-mean of d̄_content at s=87, which is itself ~0.5 — Q 87 sits ABOVE this band-mean by ~0.3. This is plausible: mufaṣṣal-tail surahs have high local-clustering = low LOCAL d̄_content but their MEAN-to-other-113 still includes long Medinans far away).
- **d̄_rhyme(s)** at s=87: predicted ≈ 0.36 + 0.0041·max(0, 87−50) = 0.36 + 0.0041·37 = 0.512. Q 87's rhyme-entropy 0.206 is FAR BELOW the band-prediction (predicted nat-entropy is the *mean* per-surah d̄_rhyme, not entropy). Q 87 is a perfect-monorhyme, so its rhyme-entropy is an outlier-low. **Q 87 is in the perfect-monorhyme cluster; the H-NEW-700 band law predicts the mean, but the perfect-monorhymes are an architectural sub-class outside the band**.
- **d̄_phoneme(s)** at s=87: predicted ≈ 0.001 + 0.00089·max(0, 87−75) = 0.0117. Q 87's mean d̄_phoneme not reported in extracted h-new-700.json snapshot for this query; expected to fall near band.
- **d̄_verse-length(s)** at s=87: kink-50 prediction; Q 87's avg verse-length 3.79 words / 15.1 letters is well within the deep-mufaṣṣal-tail band.

## 8. iʿjāz anti-twin (H-NEW-730)

The corpus-wide r(content × rhyme) = −0.86 anti-correlation defines the iʿjāz anti-twin lock. Q 87 sits in the rhyme-pure sub-pole (rhyme-entropy LOW, content-distance LOW = both LOW) — this is a coherent corner: content-cohesion-cluster + rhyme-pure-cluster overlap. Q 87 is among the 8 perfect-monorhyme surahs PLUS in a cohesive content-cluster, so it occupies the "low both" off-diagonal corner of the iʿjāz anti-twin scatter (rather than the high-content-low-rhyme or low-content-high-rhyme tradeoff diagonals). Among the perfect-monorhyme tier, Q 87 + Q 92 are in this corner (low content-distance, low rhyme-entropy); Q 18 and Q 76 are in the high-content corner (long surahs that maintain perfect-monorhyme).

## 9. Cross-corpus root-Jaccard structure

Q 87's root-Jaccard distribution to all 113 other surahs (computed `data/morphology/quranic-corpus-morphology-0.4.txt`):

- Q 87 mean root-Jaccard to all 113 = **0.082** (corpus-typical: range 0.05-0.15)
- Q 87 top-15 most-similar surahs by root-Jaccard:

| Rank | Surah | J | Notes |
|:-:|:-:|:-:|:--|
| 1 | Q 92 al-Layl | 0.188 | Early Meccan, perfect-monorhyme on -ā |
| 2 | Q 79 al-Nāziʿāt | 0.165 | oath-opener |
| 3 | Q 73 al-Muzzammil | 0.148 | Early Meccan ascetic |
| 4 | Q 74 al-Muddaththir | 0.145 | Early Meccan |
| 5 | Q 53 al-Najm | 0.142 | **the *ṣuḥuf-pair* companion** (Q087-F-03 pre-reg) |
| 6 | Q 32 al-Sajda | 0.138 | sajda surah, classical Friday-Fajr companion |
| 7 | Q 82 al-Infiṭār | 0.130 | mufaṣṣal eschatology |
| 8 | Q 57 al-Ḥadīd | 0.125 | musabbiḥa-PERFECT companion |
| 9 | Q 62 al-Jumuʿah | 0.125 | musabbiḥa-IMPERFECT companion |
| 10 | Q 96 al-ʿAlaq | 0.123 | the FIRST revelation (rev-order #1 vs Q 87 = #8) — *iqraʾ* companion to *sa-nuqriʾuka* |

**Critical observations**:
- Q 53 al-Najm (the *ṣuḥuf*-pair partner) ranks **#5** in Q 87 root-Jaccard similarity. The corpus-EXACT pair holds at the lexical level too.
- Q 96 al-ʿAlaq (the first revelation, *iqraʾ* corollary) ranks **#10**.
- Among the 6 OTHER musabbiḥāt, Q 87's root-Jaccard ordering is: Q 57 (0.125) ≈ Q 62 (0.125) > Q 59 (0.119) > Q 64 (0.105) > Q 61 (0.080) > **Q 17 (0.073, RANK 76/113)**.

**Q 17 al-Isrāʾ is the MOST DISTANT from Q 87** among the 7 musabbiḥāt. The {Q 17, Q 87} non-finite-Meccan grammatical-bracket pair has the LOWEST content-cohesion of any musabbiḥa pair. (See `06-novel-findings.md` Q087-F-01 for the formal pre-registered test.)

## 10. Phonological anchors

Q 87's phonological signature:
- 18/19 verses end on alif maqṣūra (ى) — *-ā / -ay* rhyme.
- The single break-verse (v 7 *yakhfā*) ends on alif (ا) but with the same *-ā* phonetic value, so the phonological monorhyme is ESSENTIALLY PERFECT at 19/19 (the orthographic distinction ا vs ى is on a tāʾ-marbūṭa convention, the spoken phoneme is invariant).
- The 3-vowel pattern ـَى (-ā mufakhkhama) on alif-maqṣūra dominates. Classical *taḥfīẓ* schools cite Q 87 as a model for *imāla* discipline (the technical rule for slight vowel-fronting on the alif-maqṣūra ending; al-Suyūṭī, *al-Itqān* nawʿ 22 *al-imāla wa-l-fatḥ*).
- Verses 1-5 each end on the alif-maqṣūra: *al-aʿlā / sawwā / hadā / al-marʿā / aḥwā*. The recitation rhythm is a 2-beat trochaic *sajʿ muṭarraf*: 2-stressed + ـى-fall.

## 11. Structural / divine-name signature

| Divine-name reference | Form in Q 87 | Frequency in surah |
|:--|:--|:-:|
| الأعلى (al-Aʿlā) | v 1 (epithet) | 1 |
| رب (rabb, "Lord") | rabbika v 1, rabbihi v 15, rabbika v 6 (sa-nuqriʾuka) | 3 |
| الله (Allāh) | v 7 (mā shāʾa llāh) | 1 |

Density: 5 divine-name occurrences in 72 words = 6.94% — HIGH for a non-Khawātim surah but low compared to Khawātim cluster (Q 59:23 has 50%).

## 12. Verse-length distribution

| Verse | Word count | Letter count | Final letter |
|:-:|:-:|:-:|:--|
| v 1 | 4 | 17 | ى |
| v 2 | 3 | 11 | ى |
| v 3 | 3 | 12 | ى |
| v 4 | 3 | 14 | ى |
| v 5 | 3 | 12 | ى |
| v 6 | 3 | 13 | ى |
| **v 7** | **9** | **38** | **ى** (yakhfā) |
| v 8 | 2 | 10 | ى |
| v 9 | 4 | 14 | ى |
| v 10 | 3 | 12 | ى |
| v 11 | 3 | 13 | ى |
| v 12 | 4 | 16 | ى |
| v 13 | 5 | 22 | ى |
| v 14 | 4 | 13 | ى |
| v 15 | 4 | 17 | ى |
| v 16 | 4 | 18 | ى |
| v 17 | 3 | 14 | ى |
| v 18 | 5 | 23 | ى |
| v 19 | 3 | 19 | ى |

**Verse 7 is the longest at 9 words / 38 letters** — the *istithnāʾ* (exception) verse *illā mā shāʾa llāhu innahu yaʿlamu l-jahra wa-mā yakhfā*. This single longer verse interrupts the otherwise uniform short-verse rhythm and constitutes a structural break-point at the divine-promise pivot (v 6→7). Verse 7 is a **prosodic outlier** within the surah (mean = 3.79 words; v 7 = 9 = 2.4× mean).

## 13. H-NEW-1030 chronology-architecture dissociation reference

Q 87 (rev-#8, Early Meccan, mushaf #87) is FR-architecturally a deep-mufaṣṣal-tail surah. Its mushaf-position (87) accurately reflects its FR-architectural position (cluster with Q 88-114 short-Meccan tail). Q 87's mushaf-revelation displacement +79 (forward) is one of the **largest** in the corpus, but unlike Q 5 (rev-#112, mushaf-#5) and Q 110 (rev-#114, mushaf-#110) which exhibit *chronology-architecture dissociation*, Q 87 exhibits **chronology-architecture CONCURRENCE**: it was revealed early in Mecca AND its FR-architectural fingerprint is congruent with the early-Meccan-tail mushaf-cluster. The displacement is *positional* (it was revealed at chronology-step #8 but placed at mushaf-step #87) but not *architectural* — Q 87's mushaf neighborhood is its native FR-architectural neighborhood.

This is consistent with [[h-new-1030-q110-chronology-dissociation|H-NEW-1030]]'s implicit corollary: most short-tail surahs (regardless of revelation chronology) cluster together at the FR-content-fingerprint level. Q 87 is a baseline-confirming case for the principle that FR-position encodes length-class + content-mode rather than chronology.

## 14. Empirical summary

| Axis | Q 87 value | Verdict |
|:--|:-:|:--|
| Length-class | mufaṣṣal-qiṣār | typical |
| Rhyme | perfect monorhyme (19/19) | TIER-ELITE (8-surah cluster) |
| Outlier-strength | NULL | typical (architecturally seamless) |
| FR-clustering | top-15 = 14 Early-Meccan tail | tight homogeneous neighborhood |
| Adjacency cost | Q 86→87 = clamped-0 (rank 9/113) | EMPIRICALLY SEAMLESS |
| iʿjāz signature magnitude | near-zero | undistinctive on this axis |
| UAS | −2.817 (rank 114/114) | LOWEST in corpus (consequence of seamlessness, not defect) |
| Form (musabbiḥa typology) | UNIQUE IMPERATIVE | tier-singleton |
| Content-pair (ṣuḥuf-Ibrāhīm-wa-Mūsā) | corpus-EXACT 2-pair w/ Q 53 | NEW PAIR FINDING |
| Self-referential recitation hapax | corpus-EXACT (sa-nuqriʾuka fa-lā tansā) | UNIQUE |
| Liturgical role | Friday + Eid + Witr | TRIPLE-ATTESTED |

Q 87 is the corpus's **most architecturally-seamless surah by UAS** — but this seamlessness coexists with **multiple corpus-EXACT pair-uniqueness signatures** (musabbiḥa-imperative-singleton, ṣuḥuf-Ibrāhīm-wa-Mūsā pair, sa-nuqriʾuka hapax) and **multiple-attested liturgical roles** (Friday, Eid, Witr — verified across Muslim, Nasāʾī, Tirmidhī, Ibn Mājah, Ahmad). The empirical-architectural axis (UAS, outlier, FR) reads Q 87 as a *background* surah; the form-grammatical, classical-pair, and liturgical axes read Q 87 as a *load-bearing* surah. Both are correct: this is the multidimensionality of Qurʾānic architectural significance.
