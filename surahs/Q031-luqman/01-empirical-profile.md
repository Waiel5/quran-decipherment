---
surah: 31
surah_name_ar: لقمان
surah_name_translit: Luqmān
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111,590,700,720,750,840}.
---

# Q 31 Luqmān — Empirical Architectural Profile

## 1. Headline numbers (rules-tuple: no-tashkeel, orthographic-token, graphemes-no-spaces, basmala-counted-only-in-Q1, hafs-kufan, mashriqi)

| Metric | Value | Source / interpretation |
|:--|:--:|:--|
| Verse count | 34 | Hafs-Kūfan (`data/hafs-verse-counts.tsv`) |
| Word tokens | 551 | computed from `quran-text/quran-no-tashkeel.json` |
| Letter graphemes (no spaces) | 2,172 | computed |
| Avg verse length (graphemes) | 63.9 | computed |
| Avg verse length (words) | 16.2 | computed |
| Top final-letter (rāwī) | ر | 47.1% of 34 verses (`h-new-750.json`) |
| Rhyme entropy (nats) | 1.291 | HIGH — multi-letter palette (z = +0.94) |
| 2nd most-common final-letter | م | ~24% |
| 3rd most-common final-letter | ن | ~21% |
| Mean content distance (FR) | 0.948 | mid-corpus (corpus mean 0.924; `h-new-750.json`) |
| Local cohesion | 1.060 | slightly low |
| iʿjāz sig_A | +0.698 (rank 43/114) | mid-positive (al-Bāqillānī fawāṣil axis) |
| iʿjāz sig_B | +0.319 (rank 49/114) | mid-positive (al-Sakkākī iqāʿ axis) |
| UAS | −1.171 (rank 80/114) | LOW (`h-new-840.json`) |
| Outlier-strength Δ%ile | +2.14 pp (window {Q 28-34}) | WEAK_OUTLIER (`h-new-590.json`) |
| p_greater (perm) | 0.3066 | not significant |
| Q 30 → Q 31 cost δ | +0.0376 | low (fraction_residual 0.45%) |
| Q 31 → Q 32 cost δ | +0.1005 | modest (fraction_residual 1.21%) |
| Tanzil revelation order | 57/114 | `data/revelation-order.csv` |
| Nöldeke order | 82/114 | as above |
| Phase | Late Meccan | both stratifications |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 31's top-15 nearest in FR space (decoded from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 45 | al-Jāthiya | 0.7685 | ḥawāmīm Late Meccan, knowledge-emphasis |
| 2 | Q 64 | al-Taghābun | 0.7743 | musabbiḥāt cluster, monotheist-frame |
| 3 | Q 22 | al-Ḥajj | 0.7991 | mixed Meccan-Medinan, eschatological |
| 4 | Q 62 | al-Jumuʿah | 0.8313 | **the META-cluster meta-hub** (cross-finding-009) |
| 5 | Q 35 | Fāṭir | 0.8455 | Late Meccan, divine-creator emphasis |
| 6 | Q 13 | al-Raʿd | 0.8505 | ALR opener, early Medinan |
| 7 | Q 112 | al-Ikhlāṣ | 0.8555 | tawḥīd quintessential |
| 8 | Q 1 | al-Fātiḥa | 0.8559 | umm al-kitāb |
| 9 | Q 61 | al-Ṣaff | 0.8630 | musabbiḥāt cluster |
| 10 | Q 96 | al-ʿAlaq | 0.8664 | first revelation, *aqlām/ʿallam* knowledge-opener |
| 11 | Q 91 | al-Shams | 0.8694 | oath-cluster |
| 12 | Q 14 | Ibrāhīm | 0.8700 | ALR cluster, prophet-named |
| 13-15 | Q 39, Q 40, Q 6 | (Zumar, Ghāfir, al-Anʿām) | ~0.875-0.885 | additional Late-Meccan / ḥawāmīm neighbors |

Q 31's mean FR-distance to all 113 = 0.948. **The neighborhood is content-thematic Late-Meccan eschatological-cosmic with strong gravity toward the meta-hub Q 62 and toward the *aqlām/ʿallam* knowledge-cluster (Q 96)** — both consistent with Q 31's eponymous-figure-of-wisdom + Book/pen metaphor at v.27.

Far end (Q 31's farthest 5):

| Surah | FR | Note |
|:-:|:--:|:--|
| Q 55 al-Raḥmān | 1.165 | the iʿjāz-anti-twin, refrain-driven |
| Q 26 al-Shuʿarāʾ | 1.108 | long mid-Meccan prophet-narrative-compendium |
| Q 9 al-Tawba | 1.094 | basmala-less Medinan polemic |
| Q 4 al-Nisāʾ | 1.078 | long Medinan legal |
| Q 5 al-Māʾida | 1.074 | long Medinan legal |

**Notable**: in FR space Q 31 is **not** particularly close to its mushaf-immediate ALM-neighbors. Q 32 (al-Sajda) is at FR=0.9095 (rank ~30 in Q 31's row); Q 30 (al-Rūm) is at FR=0.9089 (rank ~32). Both are near Q 31's mean-distance (0.948), not near its top-12. This empirically replicates the **letter-axis ⊥ content-axis** finding at the Q 31 single-surah level: structural-orthographic similarity (the ALM opener + book-ref couplet) does not produce content-thematic similarity in the corpus.

## 3. ALM-cluster pairwise FR matrix

Among the 6 ALM surahs {Q 2, Q 3, Q 29, Q 30, Q 31, Q 32}, all 15 pairwise FR distances:

| Pair | FR | Rank-in-corpus (which-percentile) |
|:--|:--:|:--|
| Q 2–Q 3 | 0.6309 | TIGHTEST (3rd-percentile of all 6,441 corpus pairs) |
| Q 29–Q 31 | 0.8963 | mid-corpus |
| Q 30–Q 31 | 0.9089 | mid-corpus |
| Q 31–Q 32 | 0.9095 | mid-corpus |
| Q 29–Q 30 | 0.9153 | mid-corpus |
| Q 29–Q 32 | 0.9383 | mid-corpus |
| Q 30–Q 32 | 0.9272 | mid-corpus |
| Q 2–Q 29 | 0.8489 | mid-corpus |
| Q 3–Q 29 | 0.8420 | mid-corpus |
| Q 2–Q 30 | 0.9732 | upper-mid |
| Q 2–Q 31 | 0.9770 | upper-mid |
| Q 3–Q 30 | 0.9841 | upper-mid |
| Q 3–Q 31 | 0.9961 | upper-mid |
| Q 2–Q 32 | 1.0515 | upper |
| Q 3–Q 32 | 1.0860 | upper |

Mean ALM-cluster pairwise FR = **0.9257** vs corpus mean = 0.9234. **The 6-surah ALM-cluster is NOT FR-cohesive** — its mean is essentially indistinguishable from any random 6-surah subset. This is the empirical finding that grounds Q032-F-03 NULL (ALM-exception subset is not a content-cluster) and the broader cross-finding-006 architectural reading: muqaṭṭaʿāt are a **letter-distribution / structural-marker** cluster, NOT a content-thematic cluster.

The ONE tight pair (Q 2-Q 3 at FR=0.63) is the long-Medinan twin pair; the other 14 pairs are mid- to upper-mid corpus distances. Q 31's nearest ALM-sibling is **Q 29** (FR=0.8963) — interesting because Q 29 is one of the "ALM-exception" surahs (no book-ref opener), suggesting that the inner-ALM book-ref triad {Q 2, Q 3, Q 31} is **NOT a content-cohesive sub-cluster either**.

## 4. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json` for X=31:

| Field | Value |
|:--|:--:|
| Window | {Q 28, Q 29, Q 30, Q 31, Q 32, Q 33, Q 34} |
| d_W (mean within-window FR) | 0.9685 |
| d_W − Q 31 (window minus Q 31) | 0.9701 |
| pct_W (window in corpus 7-window dist) | 69.34 |
| pct_W − Q 31 | 67.20 |
| Δ pp | **+2.14** |
| p_greater_W | **0.3066** |
| Classification | **WEAK_OUTLIER** |

Q 31 is mildly content-distinct from its mushaf-7-window neighborhood {Q 28-34}, but the perm-p of 0.31 indicates the surah is **not a strong outlier**. The window's percentile (69.3) places it above-corpus-median for cohesion — i.e. {Q 28-34} is a **moderately incohesive band** (a mix of ALM Late-Meccan + Q 28 al-Qaṣaṣ Late Meccan + Q 33 long Medinan al-Aḥzāb + Q 34 Sabaʾ Late Meccan). Q 31's removal barely shifts the cohesion — Q 31 is **mid-window-typical**, not the most distinct member.

## 5. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Note |
|:--|:--:|:--:|:--|
| Rhyme entropy (nats) | 1.291 | +0.944 | HIGH (palette-rhyme, not monorhyme) |
| Mean content distance | 0.948 | +0.246 | mid-corpus |
| Local cohesion | 1.060 | −0.624 | slightly low |
| sig_A | **+0.698** | **rank 43/114** | mid-positive (al-Bāqillānī fawāṣil) |
| sig_B | **+0.319** | **rank 49/114** | mid-positive (al-Sakkākī iqāʿ) |

Q 31 is **mid-positive** on both iʿjāz axes — neither structurally extraordinary nor structurally suppressed. Its high rhyme-entropy (palette of 5 verse-final letters: ر, م, ن, د, ظ) is unusual for a 34-verse Late-Meccan surah; mid-Meccan and Late-Meccan surahs typically tend toward monorhyme. The non-monorhyme reflects Q 31's structural-thematic blend: 4 distinct blocks (frame / Luqmān-pericope / cosmic-signs / mortality-ghayb) with different voice-registers (divine narrator, Luqmān-quoted, cosmic-witness-rhetorical, eschatological-warning) drive different rhyme tendencies.

## 6. UAS (H-NEW-840)

From `h-new-840.json`:

| Field | Value |
|:--|:--:|
| UAS | −1.171 |
| Rank | 80/114 |
| abs_outlier component | 2.14 (small) |
| max_cost component | 0.1005 (small — Q 31→Q 32 seam) |
| abs_ijaz component | 0.698 (mid-positive) |

Q 31 is in the **bottom 30%** of unified architectural significance. The triple-axis composite (outlier-strength + max-adjacency-cost + |iʿjāz signature|) places Q 31 in the **content-driven mid-corpus** band: distinctiveness is content/genre-level, not structural.

The surahs that score HIGHER UAS than Q 31 on triple-intersection (top-15 of UAS): {Q 33, Q 1, Q 9, Q 32 (rank 27), Q 22, Q 12, Q 55, Q 62, Q 33, Q 38, Q 56, Q 67, Q 79, Q 75, Q 110}. Q 31 is **not** in this top tier. The empirical message: Q 31's distinctiveness is **eponymously substantive** (the Luqmān-pericope) rather than **architecturally outlier-driven**.

## 7. Phonological / rhyme axis (H-NEW-700)

From `h-new-750.json` per-surah (which the H-NEW-700 phonological-compression-tail analysis overlays):

- Top verse-final letter: **ر (rāʾ)** at 47.1% (16 of 34 verses end in ر)
- Rhyme entropy: **1.291 nats** (z = +0.94 vs corpus distribution)
- Q 31 is **OUTSIDE the compression-tail regime** (s=31 < kink=50; the H-NEW-700 phonological compression-tail laws apply only for s>50 short-mufaṣṣal surahs)

Detailed final-letter distribution for Q 31's 34 verses:

| Final letter | Count | Frac |
|:-:|:-:|:--|
| ر (rāʾ) | 16 | 47.1% |
| م (mīm) | 8 | 23.5% |
| ن (nūn) | 7 | 20.6% |
| د (dāl) | 2 | 5.9% |
| ظ (ẓāʾ) | 1 | 2.9% |

The 5-letter palette is wider than the corpus median (~3 letters per surah). The ر/م/ن trio together cover 91% of verse-finals — these are the high-frequency *non-emphatic-glide* consonants that classical *fawāṣil* practice favors for rhyme-flexibility.

## 8. Cross-references for empirical anchors

- [[h-new-111-fisher-rao-mushaf]] — FR neighborhood, ALM-cluster pairwise.
- [[h-new-590-outlier-spectrum]] — WEAK_OUTLIER on window {Q 28-34}.
- [[h-new-700-phonological-compression-tail]] — Q 31 outside the s>50 compression-tail regime.
- [[h-new-720-canonical-adjacency-cost]] — smooth seams left and right; expensive seam ONE position later (Q 32→Q 33).
- [[h-new-750-ijaz-signature]] — mid-positive on both fawāṣil + iqāʿ axes; high rhyme-entropy.
- [[h-new-840-unified-architectural-score]] — UAS rank 80/114 (LOW).
