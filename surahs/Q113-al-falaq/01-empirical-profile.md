---
surah: 113
surah_name_ar: الفلق
surah_name_translit: al-Falaq
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — all H-NEW metrics integrated; iʿjāz-al-fawāṣil-pure cell confirmed
---

# Q 113 al-Falaq — Empirical Architectural Profile


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

## 1. Headline metrics

Rules-tuple: `(no-tashkeel, QAC-stem, K500, Hafs-Kufan, Mashriqi, basmala-counted-only-in-Q1)`. All values computed from disk; sources cited.

| Metric | Value | Rank / 114 | Source |
|:--|:--:|:--:|:--|
| **UAS** | −0.2938 | 57 / 114 (mid) | `h-new-840.json` `all_uas` surah=113 |
| Outlier-strength Δ%ile | 0.00 pp (NULL) | 45 / 114 | `h-new-590.json` X=113 |
| Q 112 → Q 113 adjacency cost | 0.0683 (0.82%) | 52 / 113 | `h-new-720.json` |
| Q 113 → Q 114 adjacency cost | 0.0623 (0.75%) | 56 / 113 | `h-new-720.json` |
| **iʿjāz sig_A** | **+1.8900** | **7 / 114** (top decile) | `h-new-750.json` per_surah |
| **iʿjāz sig_B** | **+3.2433** | **2 / 114** (rank-2) | same |
| Mean FR distance to corpus | **0.7843** | **7 / 114** (FR-centroid top decile) | `h-new-111.json` (computed) |
| Local cohesion | 3.5214 | very high | `h-new-750.json` |
| Rhyme entropy (nats) | 1.0549 | mid-high (vs Q 112 = 0.0; vs corpus median ~0.6) | same |
| Top final letter | د (40%) — tied with ق (40%); ب (20%) | bi-modal | computed |
| Total root-tokens | 11 | bottom-decile | `morphology` Q113 |
| Distinct roots | 10 | bottom-decile but high distinct-rate | same |
| Words (no-tashkeel) | 23 | bottom-decile | `quran-no-tashkeel.json` |
| Letters (no-tashkeel) | 73 | bottom-decile | same |
| Verses | 5 | bottom-15 | canonical |

## 2. Architectural cell: *iʿjāz-al-fawāṣil-pure*

Q 113 is a member of the **iʿjāz-al-fawāṣil-pure** cell of [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2. Cell criteria + Q 113 values:

| Cell criterion | Q 113 value | Match? |
|:--|:--:|:-:|
| High iʿjāz sig_A | rank 7 / 114 | ✓ (top decile) |
| Moderate outlier-strength | rank 45 (NULL classification) | ~ (cell allows moderate; 45 is below median but classification is NULL) |
| Low TSP / adjacency cost | combined 1.57%, both adjacencies non-top-15 | ✓ |
| Classical anchor | al-Bāqillānī *iʿjāz al-fawāṣil* + muʿawwidhatān fadāʾil | ✓ |

Cell members per cross-finding-026: **Q 86, 89, 100, 106, 113**. Q 113 is the cell's *muʿawwidhatān-link* — its membership ties the *iʿjāz-al-fawāṣil-pure* cell to the *fadāʾil*-anchored muʿawwidhatān recitation tradition.

**sig_B rank 2 / 114** is corpus-extreme: Q 113's mean content distance + local cohesion combine to a sig_B near corpus-max. Only Q 106 ranks higher on sig_B.

## 3. FR-distance neighbours (Q 113 against 113 others)

Computed from `h-new-111.json`:

**Five nearest neighbours**:

| Rank | Surah | FR distance | Class |
|:-:|:-:|:--:|:--|
| 1 | Q 108 al-Kawthar | 0.2371 | terminal-3v |
| 2 | **Q 114 al-Nās** | **0.2718** | **muʿawwidhatān-pair** |
| 3 | Q 106 Quraysh | 0.2761 | terminal-4v |
| 4 | Q 112 al-Ikhlāṣ | 0.2886 | cluster-sibling |
| 5 | Q 94 al-Sharḥ | 0.2901 | terminal-8v |

Q 113's nearest neighbour Q 108 (0.2371) is closer than its canonical-pair Q 114 (0.2718) — yet Q 113 is canonically paired with Q 114 (the muʿawwidhatān). The FR-geometric cluster is broader than the classical muʿawwidhatān pair; Q 108 al-Kawthar is FR-closest. **This is the empirical signature that the muʿawwidhatān is a *content-thematic* pair, not the FR-geometric tightest pair.**

Q 113 → Q 114 distance = 0.2718 = Q 113's **#2** nearest. Q 114 → Q 113 = Q 114's **#1** nearest. Their pairing is FR-asymmetric: Q 114 is closer to Q 113 than Q 113 is to Q 114 (Q 113 has Q 108 closer).

## 4. FR-centroid status

Mean FR distance Q 113 → corpus = 0.7843, **rank 7 / 114**. Top decile but not corpus-extreme.

For comparison:
- Q 112 al-Ikhlāṣ rank 1 (mean=0.7592) — corpus FR-centroid
- Q 110 al-Naṣr rank 2 (mean=0.7644)
- Q 108 al-Kawthar rank 3 (mean=0.7718)
- Q 1 al-Fātiḥa rank 4 (mean=0.7789)
- Q 106 Quraysh rank 5 (mean=0.7803)
- Q 114 al-Nās rank 6 (mean=0.7838)
- **Q 113 al-Falaq rank 7 (mean=0.7843)**

Q 113 sits with its cluster-sibling Q 114 in adjacent FR-centrality ranks (6 and 7), behind Q 112 (rank 1). This is consistent with the muʿawwidhāt-3 (Q 112+113+114) being a tight FR-central trio.

## 5. Rhyme structure (verified)

Final-letter distribution:

| Verse | Final word | Final letter | Rhyme cluster |
|:-:|:-:|:-:|:-:|
| 1 | الفلق | ق | -al-falaq |
| 2 | خلق | ق | -khalaq |
| 3 | وقب | ب | -waqab |
| 4 | العقد | د | -al-ʿuqad |
| 5 | حسد | د | -ḥasad |

**Distribution**: ق × 2 (40%), د × 2 (40%), ب × 1 (20%). H-NEW-750's "top final letter: د (40%)" is via tiebreak. The surah is **bi-modal-rhyme** (ق + د).

Rhyme entropy = 1.0549 nats. This is **not** a high-entropy mixed-rhyme; it is moderate-rhyme-with-2-dominant clusters. The high sig_A (rank 7) emerges from the combination of moderate-rhyme-entropy with the surah's high local-cohesion and short-length normalization.

## 6. Phoneme density (qualitative)

Q 113's phonemic profile features:
- Velar/uvular stop: ق dominant (الفلق, خلق) — 5 ق tokens in the surah
- Sibilant: س in *aʿūdhu*, *sharr*-cluster — *sharr* repeated 4× in vv.2-5
- Pharyngeal: ع in *aʿūdhu*, *al-ʿuqad*
- Glottal: ا extensively
- Nasal: ن in *l-naffāthāt*

The sibilant *sharr* (شر) repetition is the surah's most prominent phonemic-marker — 4 attestations in 5 verses, anchoring the evil-refuge-formula. See `02-content-analysis.md` for the typology.

## 7. Outlier-window decomposition (H-NEW-590)

Per `h-new-590.json` X=113: Δ%=0.00, classification NULL. The 7-window centred on Q 113 [110, 111, 112, 113, 114] is internally tight; removing Q 113 does NOT collapse cohesion. This is consistent with the muʿawwidhāt-tail being FR-tight without depending on Q 113's specific contribution.

## 8. iʿjāz signature decomposition

- **sig_A = +1.8900, rank 7 / 114** — top-decile *iʿjāz al-fawāṣil*. The signature combines: moderate rhyme entropy (1.05 nats; corpus has heavily skewed distribution) + corpus-mean-distance (z=−0.96) + local cohesion (z=+1.18 high).
- **sig_B = +3.2433, rank 2 / 114** — rhyme-purity-centric signature. Only Q 106 Quraysh (sig_B=3.43) ranks higher.

The high sig_A and sig_B together place Q 113 firmly in the iʿjāz-al-fawāṣil-pure cell. This is consistent with classical *iʿjāz al-fawāṣil* scholarship (al-Bāqillānī *al-Iʿjāz al-Qurʾān*; al-Suyūṭī *al-Itqān*) treating the muʿawwidhatān as exemplars of refrain-iʿjāz: each verse begins with *min sharri* (*from the evil of...*) — a 4× refrain in 4 evil-typology verses, with rhyme-cluster shifts at each typology-step.

## 9. Canonical-adjacency cost (H-NEW-720)

| Adjacency | Cost (length-units) | Frac of TSP residual | Rank / 113 |
|:--|:--:|:--:|:--:|
| Q 112 → Q 113 | 0.0683 | 0.82% | 52 |
| Q 113 → Q 114 | 0.0623 | 0.75% | 56 |
| (combined) | 0.1306 | 1.57% | — |

Both adjacencies are mid (rank 52 / 56). Neither is top-15 expensive — Q 113 is NOT bracketed (i.e., not in the *Structural-twin-pair* cell). The mushaf does not pay structural cost to keep Q 113 in canonical position 113; the muʿawwidhatān-pair is internally cheap.

This is consistent with [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §5 ("Q 113-Q 114 muʿawwidhāt-pair: 0.8% of residual; near-free"). The pair is geometrically near-optimal for FR-distance — the canonical placement is structurally cheap.

## 10. Cross-references to H-NEW findings

- [[h-new-111-fisher-rao-distance|H-NEW-111]] — FR-centroid rank 7; nearest = Q 108 (0.2371).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — NULL outlier (rank 45).
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 113 in compression-tail (s=113).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 113 in phoneme-dispersion-tail.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — both adjacencies mid; pair is FR-cheap.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — sig_A rank 7, sig_B rank 2.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 57.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2 — *iʿjāz-al-fawāṣil-pure* cell.

## 11. Honest limits

1. **n=5 verses** is small; sig_A / sig_B are computed at this small sample, with z-normalization sensitivity.
2. The "muʿawwidhatān pair" classical naming is *content-thematic* (parallel *qul aʿūdhu* opening) — empirically, Q 113's nearest FR neighbour is Q 108, not Q 114. The classical pair is not the FR-tightest pair.
3. The bi-modal-rhyme structure (ق + د tied at 40%) means the "top final letter" assignment is tiebreak-dependent.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
