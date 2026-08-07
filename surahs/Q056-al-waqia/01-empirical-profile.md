---
surah: 56
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE
---

# Q 56 al-Wāqiʿa — Empirical Profile


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

All values computed from on-disk JSON (no memory-quotation). File paths cited.

## 1. UAS (Unified Architectural Significance)

**Source**: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json`

| Component | Value | Rank | Note |
|:--|--:|--:|:--|
| UAS | **−0.9339** | **75/114** | Below corpus median |
| `abs_outlier` (Δ%ile) | 1.33 | low | window 53-59, WEAK_OUTLIER |
| `max_cost` (max-neighbor TSP) | 0.2274 | mid | Q56→Q57 (the Hijra-kink) |
| `abs_ijaz` | 0.0567 | low | sig_A near zero (no strong fawāṣil signature) |

**Interpretation**: Q 56 is **mid-pack on UAS**. It does not occupy a top-decile architectural cell (unlike Q 33, Q 1, Q 24, Q 9, Q 12, Q 55). It is NOT in the *Structural-twin-pair* nor *iʿjāz-al-fawāṣil-pure* cells. It sits closest to the **boundary surahs** of the cross-finding-026 4-cell typology — a Hijra-anchored chronological-ordering surah with significant Q56→Q57 adjacency cost reflecting the Meccan/Medinan transition.

## 2. Outlier-strength spectrum (H-NEW-590)

**Source**: `findings/phase-b-hypotheses/csv/h-new-590.json` → `all_surahs_results` filtered to X=56.

```
window: [53, 54, 55, 56, 57, 58, 59]
window_minus_X: [53, 54, 55, 57, 58, 59]
delta_pct: 1.33
classification: WEAK_OUTLIER
```

Q 56's exclusion from its own window improves cohesion by only +1.33 percentile points. Compare to corpus top:
- Q 33: +31.46 pp (STRONG_OUTLIER, rank 1)
- Q 1: +27.09 pp (STRONG_OUTLIER, rank 2)
- Q 55 (immediate neighbor): +14.26 pp (MODERATE_OUTLIER, rank 6)
- Q 56: +1.33 pp (WEAK_OUTLIER, well outside top 10)

Q 56 is NOT an outlier-anchor surah.

## 3. iʿjāz signature (H-NEW-750)

**Source**: `findings/phase-b-hypotheses/csv/h-new-750.json` per_surah[surah=56].

| Field | Value |
|:--|--:|
| n_verses | 96 |
| rhyme_entropy_nats | 1.2657 (own min-tashkeel count: 1.31; minor counting artifact) |
| top_final_letter | ن |
| top_final_letter_frac | 0.5789 |
| mean_content_distance | 1.0202 |
| local_cohesion | 0.9039 |
| z_rhyme_entropy | 0.898 (above corpus mean — moderate rhyme variety) |
| z_mean_content_distance | 0.955 (above corpus mean — content-distant) |
| z_local_cohesion | −0.837 (below corpus mean — internally cohesive) |
| **sig_A** | **−0.0567** (rank 63/114) |
| **sig_B** | **+0.0612** (rank 58/114) |

Q 56's |sig_A| = 0.057 is near zero — Q 56 is NOT a fāṣila-virtuoso surah. It does NOT fit the *iʿjāz-al-fawāṣil-pure* cell (which requires high positive sig_A). Its rhyme-entropy is moderate (1.27 nats) — significantly higher than Q 55 al-Raḥmān (0.42 nats) but lower than terminal-mufaṣṣal-qiṣār surahs.

Final-letter distribution (own count, no-tashkeel, treating last grapheme):
```
ن: 55  م: 18  ة: 10  ا: 7  د: 3  ب: 1  ء: 1  ل: 1
```
Total: 96. The dominant ن (57.9%) reflects its extensive use of *-ūn / -īn / -ān / -ūma* paradise-and-judgment vocabulary; the م (18.8%) corresponds to *-īm / -ūm* clusters (e.g., *al-jaḥīm*, *al-ḥamīm*, *al-ʿaẓīm*).

## 4. Fisher-Rao distance position (H-NEW-111)

**Source**: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`.

| Metric | Value |
|:--|--:|
| Mean FR-distance | 1.0202 |
| Corpus mean | 0.9235 |
| **Q 56 mean-dist rank** | **92/114** (1=most central) |
| Maximum FR-distance | 1.388 (to Q 9) |
| Minimum FR-distance | 0.814 (to Q 105) |

**Q 56 is content-DISTANT from the corpus centroid** (rank 92/114). It is NOT a centroid surah like Q 112 (rank 1) or Q 36 / Q 67.

### Q 56's nearest-10 FR-neighbors

| Rank | Surah | FR distance |
|:--|:--|--:|
| 1 | Q 105 al-Fīl | 0.8137 |
| 2 | Q 102 al-Takāthur | 0.8212 |
| 3 | Q 78 al-Nabaʾ | 0.8342 |
| 4 | Q 90 al-Balad | 0.8342 |
| 5 | Q 77 al-Mursalāt | 0.8356 |
| 6 | Q 112 al-Ikhlāṣ | 0.8374 |
| 7 | Q 107 al-Māʿūn | 0.8402 |
| 8 | Q 110 al-Naṣr | 0.8411 |
| 9 | Q 96 al-ʿAlaq | 0.8419 |
| 10 | Q 108 al-Kawthar | 0.8420 |

**Striking pattern**: Q 56's nearest neighbors are ALL **terminal mufaṣṣal-qiṣār** surahs (Q 77, 78, 90, 96, 102, 105, 107, 108, 110, 112). Q 56 is structurally a "ṭiwāl-form mufaṣṣal-qiṣār-content" surah — its content-distribution clusters with the short eschatological terminal surahs despite its 96-verse length. This is consistent with its early-Meccan revelation order (#46 of 114).

Q 56's farthest 5: Q 5, Q 2, Q 3, Q 4, Q 9 — **all Medinan ṭiwāl** (legal-narrative-Meccan-history surahs). Q 56's content axis is orthogonal to the Medinan-ṭiwāl content axis.

## 5. Compression-tail position

By the cross-finding-026 §2 law: at s=56 (just past Hijra-kink at s=50):
- Predicted d̄_content = 0.96 − 0.012·max(0, 56−50) = 0.96 − 0.072 = **0.888**
- Predicted d̄_rhyme = 0.36 + 0.0041·max(0, 56−50) = 0.36 + 0.0246 = **0.385**
- Predicted d̄_phoneme = 0.0013 + 0.00089·max(0, 56−75) = 0.0013 (no kink yet)

Observed Q 56 mean_content_distance = 1.020 (residual: +0.13 vs prediction). Q 56 is moderately ABOVE the compression-tail trend at s=56 — consistent with its FR-distant position.

## 6. Canonical adjacency costs (H-NEW-720)

**Source**: `findings/phase-b-hypotheses/csv/h-new-720.json` `per_adjacency`.

| Adjacency | Δ | Fraction of TSP residual |
|:--|--:|--:|
| Q 55 → Q 56 | 0.0949 | 1.14% (rank 39/113 — moderate) |
| Q 56 → Q 57 | **0.2274** | **2.74% (rank 17/113 — top-15-plus)** |

**The Q 56 → Q 57 canonical adjacency is the 17th most expensive in the entire mushaf.** This corresponds to the **Hijra-kink** identified across the project. Q 56 is the last Meccan surah of the Q 36-56 cluster; Q 57 al-Ḥadīd is Medinan. The compression-tail kink at s=50 (cross-finding-026) bracket this transition. Q 56 → Q 57 is empirically a **chronology-cost** boundary (analogous to Q 9 → Q 10 cost = 3.73% rank 4, identified by the Q 9 specialist; cross-finding-026 §13.4).

This is a SIGNIFICANT structural feature: Q 56 occupies the Meccan-Medinan structural pivot.

## 7. Verse-length / words-per-verse profile

96 verses; 380 words (own count, ornament-stripped: 379) → mean = **3.96 words/verse** — extremely short for a long surah. This is comparable to Q 55 al-Raḥmān (4.55 wpv) and consistent with the *idhā*-eschatological cluster's compressed-verse style.

## 8. Architectural-cell classification

By cross-finding-026 §13 4-cell typology:
- NOT *All-axis* (low UAS, low outlier)
- NOT *Structural-twin-pair* (low outlier; only 1 expensive adjacency, not bracketed)
- NOT *Structural-twin-pair-of-one* (Q 55 occupies this; Q 56 lacks Q 55's extreme refrain)
- NOT *iʿjāz-al-fawāṣil-pure* (sig_A = −0.06, near zero)
- NOT *iʿjāz-al-maʿnā extreme* (UAS rank 75, not bottom-tier)
- NOT *iʿjāz-al-maʿnā mild* (no strong *fadāʾil* tradition at the canonical-9-book level, see `04-hadith-corpus.md`)
- NOT *anti-iʿjāz-al-fawāṣil-monolithic-rhyme* (Q 18's cell)

**Proposed cell membership**: **boundary surah / Hijra-kink keystone**. Empirical signature:
- Mid UAS (rank 75)
- Low |sig_A|
- One single dominant expensive adjacency on the FORWARD side (Q56→Q57 = rank 17/113, 2.74% TSP residual)
- Content-distant (rank 92/114) — does NOT cluster with corpus centroid
- Nearest FR-neighbors are ALL terminal-qiṣār — content-axis groups it with short eschatological surahs despite its long form

This may be a **6th cell candidate**: "long-form-mufaṣṣal-qiṣār-content surahs" — a chronological-anchor cell. The single empirical exemplar is Q 56 (Q 55 is its closest rhetorical analogue but has different empirical signature). FLAGGED for cross-finding-029 review (do not promote without independent replication on at least one other surah).

## 9. Cross-references

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 56 mean-dist rank 92/114
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 56 +1.33 pp WEAK_OUTLIER
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 56 in compression-tail at s=56 (just past kink)
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 56→Q 57 = 2.74% TSP residual (rank 17)
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — sig_A=−0.06, sig_B=+0.06
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 75/114
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §5 — Q 56-Q 57 Hijra-kink locus

## 10. Honest limits

- The "boundary surah / Hijra-kink keystone" cell is a single-exemplar hypothesis; not promoted to typology cell without replication.
- Mean FR-distance rank 92/114 reflects a content-distribution that does not match Medinan-ṭiwāl OR mufaṣṣal-ṭiwāl medians; the nearest-10-neighbors clustering with terminal-qiṣār is striking but not separately tested for permutation-significance.
- Local rules-tuple sensitivity: the rhyme-entropy own-count (1.31 nats) differs slightly from h-new-750 (1.266 nats) — likely due to final-letter extraction details (some final letters in min-tashkeel vs no-tashkeel differ). The qualitative ordering is unaffected.
