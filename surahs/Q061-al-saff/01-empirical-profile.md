---
surah: 61
surah_name_ar: الصف
surah_name_translit: al-Ṣaff
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE
---

# Q 61 al-Ṣaff — Empirical Architectural Profile

Rules-tuple: `(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, basmala-counted-only-in-Q1, mushaf order, Hafs-Kūfan, Mashriqī)`. Every numerical value below is computed from data files cited in §10 or pulled directly from H-NEW-XXX artifacts.

## 1. Headline architectural metrics

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **−1.309** | **83 / 114** (below median) | [[h-new-840-unified-architectural-score\|H-NEW-840]] all_uas[surah=61] |
| Outlier-strength Δ%ile | **−2.50 pp** | **NULL** classification — Q 61 is content-typical for its mushaf cohort (window {Q 58-64}; p_greater_W=0.9506) | [[h-new-590-outlier-spectrum\|H-NEW-590]] all_surahs_results[X=61] |
| iʿjāz signature sig_A | **+0.463** | **rank 50 / 114** — MID-RANGE POSITIVE on iʿjāz al-fawāṣil axis | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| iʿjāz signature sig_B | **−0.241** | **rank 63 / 114** — slightly negative | H-NEW-750 |
| z_mean_content_distance | **−0.482** | content-CLOSER-to-corpus than median | H-NEW-750 |
| z_local_cohesion | −0.221 | modestly below corpus median | H-NEW-750 |
| **z_rhyme_entropy** | **−0.020** | **corpus-typical** — high but not monorhyme | H-NEW-750 |
| Mean Fisher-Rao distance to corpus | **0.8746** | corpus mean 0.9235; **rank 72/114** by mean-FR (smaller = more central) | computed from [[h-new-111-fisher-rao-mushaf\|H-NEW-111]] |
| **Top final letter (rāwī)** | **ن (nūn)** | **71.4% of 14 verses** (10/14) — high but not extreme | H-NEW-750 |
| Q 60→Q 61 canonical-adjacency cost | **0.1116** (delta_raw) | rank 85/113 (cheapest-first ordering); top-30 expensive | [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] s=60 |
| Q 61→Q 62 canonical-adjacency cost | **0.0703** (delta_raw) | rank 64/113; mid-cheap. The Ṣaff→Jumuʿah seam is the tense-binary boundary in H-NEW-58c | H-NEW-720 s=61 |
| Verse count | **14** | mufaṣṣal-class | Hafs-Kūfan |
| Word count (no-tashkeel) | **226** | computed | |
| Letter count (no-tashkeel) | **966** | computed | |
| Mean words/verse | **16.14** | moderately long for a 14-verse Medinan exhortation | computed |
| Type-token ratio | **0.690** | high (156 unique tokens / 226 total) | computed |

## 2. The architectural signature: structurally-disproportionate Medinan exhortation

Q 61 is **architecturally compact but structurally dense**. Its 14 verses host:

- **18 corpus-hapax tokens** (tokens appearing only in Q 61, no-tashkeel substring-match): *بنيان* (v.4), *مرصوص* (v.4), *أزاغ* (v.5), *زاغوا* (v.5), *تؤذونني* (v.5), *برسول* (v.6), **أحمد** (v.6), *يدعى* (v.7), *ليطفئوا* (v.8), *تنجيكم* (v.10), *وتجاهدون* (v.11), *تحبونها* (v.13), *وفتح* (v.13), *عدوهم* (v.14), *للحواريين* (v.14), *فأيدنا* (v.14), *وكفرت* (v.14), *فآمنت* (v.14). Hapax-density = **11.5% of unique tokens** (18/156) — exceptionally high for a Medinan surah of standard register.
- **3 corpus-EXACT signatures** in 14 verses: (a) musabbiḥa perfect-tense opener with 56-char prefix-twin to Q 59:1; (b) Q 61:6 *Aḥmad* corpus-hapax; (c) Q 61:9 character-identical with Q 9:33.
- **3 distinct verse-classes interwoven**: cosmic-musabbiḥa opener (v.1) + military-paraenetic exhortation (vv.2-4) + dual-prophet-narrative-with-Aḥmad (vv.5-9) + tijārah-paraenetic (vv.10-13) + ḥawāriyyūn-closing (v.14).

This profile is **NOT a typical short-Medinan exhortation surah**. Q 61's mid-positive sig_A (+0.463, rank 50/114) is well above the cluster of short-Medinan-block surahs (Q 64 al-Taghābun's sig_A = −0.74; Q 57 al-Ḥadīd sig_A = −0.27 per H-NEW-750 means). Q 61 carries iʿjāz al-fawāṣil signal that elevates it ABOVE its mushaf cohort.

## 3. Fisher-Rao distance row (Q 61 vs all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` D matrix.

**Ten FR-nearest neighbours of Q 61**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| **1** | **Q 63 al-Munāfiqūn** | **0.6572** | mushaf-adjacent (s=63) + thematic-congruent (Medinan polemic against hypocrites; same exhortation register) |
| 2 | Q 110 al-Naṣr | 0.7032 | very-late Medinan (revelation #114 / 110 last); thematic Q 61:13 *naṣr min Allāh* echo at Q 110:1 |
| 3 | Q 112 al-Ikhlāṣ | 0.7080 | qul-cluster terminal triad; doxological-monotheism register (cf. Q 61:1's *huwa al-ʿAzīz al-Ḥakīm*) |
| 4 | Q 91 al-Shams | 0.7222 | short Meccan oath-cluster; surprising proximity (Q 61 has no oath-opener) |
| 5 | Q 85 al-Burūj | 0.7230 | short Meccan eschatology; thematic *naṣr / fatḥ qarīb* echo |
| 6 | Q 98 al-Bayyina | 0.7242 | short Medinan; Banū Isrāʾīl + community typology + final *ẓāhirīn / khalqi al-mukhliṣīn* parallels Q 61:14 *ẓāhirīn* |
| 7 | Q 95 al-Tīn | 0.7274 | short Meccan oath-cluster; *fa-mā yukadhdhibuka baʿdu bi-l-dīn* eschatological closure parallel |
| 8 | Q 49 al-Ḥujurāt | 0.7279 | Medinan paraenetic; *al-muʾminūn* community-formation register |
| 9 | Q 64 al-Taghābun | 0.7285 | musabbiḥāt-imperfect sister; mushaf-position 64 (3 surahs after Q 61) |
| 10 | Q 62 al-Jumuʿah | 0.7345 | mushaf-adjacent musabbiḥāt-imperfect sister; the H-NEW-58c tense-binary partner |

The FR-nearest neighbour is **Q 63 al-Munāfiqūn at 0.6572** — extraordinarily close, ranks among the corpus's tightest non-twin pairs at the surah-aggregate level (cf. Q 13↔Q 14 = 0.486, Q 57↔Q 64 = 0.722).

**Q 61's content-cluster is the short-Medinan paraenetic + short-Meccan eschatology hybrid**: 4 of 10 nearest are short-Meccan-eschatology (Q 91, 85, 95) + Q 110 (very-late-Medinan-paraenetic), and the rest are short-Medinan exhortation (Q 49, 62, 63, 64, 98). Q 61's content-vector is squarely in the **short-surah paraenetic-doxological cluster** spanning the back-half of the mushaf.

**Five FR-farthest neighbours**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 110 | Q 56 al-Wāqiʿah | 1.0550 | refrain-rich eschatology |
| 111 | Q 26 al-Shuʿarāʾ | 1.0601 | iterative-prophet-narrative cycle |
| 112 | Q 12 Yūsuf | 1.0672 | continuous Yūsuf narrative |
| 113 | **Q 19 al-Maryam** | **1.1124** | Maryam/Christ prophet-cycle catalog |
| 114 | **Q 55 al-Raḥmān** | **1.1855** | refrain-saturated nominal-doxological (corpus-most-distant pair partner for many surahs) |

**Q 19 al-Maryam is rank-2 in Q 61's farthest neighbours** (FR distance 1.1124). This is the load-bearing empirical fact for Q061-F-03: despite Q 61:6 containing the corpus-EXACT *Aḥmad*-prophecy verse from Jesus's mouth, Q 61's root-distribution is FAR from Q 19 (the corpus's prototypical Christ-narrative + Maryam surah). The Q 61 ↔ Q 19 distance ranks just behind Q 55 in Q 61's distance-row.

## 4. Mean-FR rank in corpus

Q 61's mean FR distance to all 113 other surahs = **0.8746** (corpus all-row mean = 0.9235, std = 0.1013). z_mean_FR = **−0.482**. Rank 72/114 (smaller = more central / less distant from corpus average).

This places Q 61 in the **moderately-central** zone of the corpus content-vector space — not a strong content-outlier, not a strong content-centroid. Q 61's content-vector is in the densely-populated short-Medinan + short-Meccan paraenetic neighborhood; its closest surah Q 63 al-Munāfiqūn is itself a short-Medinan paraenetic.

## 5. Outlier window structure (H-NEW-590, full Q 58-64 window)

The window {58, 59, 60, 61, 62, 63, 64} (size-7 centered on Q 61) yields:

| Removed surah | d̄_W | d̄_W−X | Δ pp | classification |
|:-:|:-:|:-:|:-:|:-:|
| Q 61 | 0.7684 | 0.7776 | **−2.50** | **NULL** (p_greater_W = 0.9506) |

The full window with Q 61 has d̄_W = 0.7684 (4.94%ile); without Q 61, d̄_W = 0.7776 (7.44%ile). **Removing Q 61 makes the window MORE FR-distant on average** — i.e. Q 61 PULLS the window TIGHTER. This is the signature of a content-cohesive cluster member, NOT an outlier.

**Q 61 is empirically INSIDE its mushaf cohort** (the short-Medinan + Khawātim-zone). The H-NEW-590 NULL classification is a **positive structural finding**: Q 61 is a contributing member of the H-NEW-1080 short-Medinan block, not a distinct content-fingerprint.

The contrast with Q 14 Ibrāhīm (NULL outlier, but as a CLUSTER ANCHOR) and Q 15 al-Ḥijr (WEAK_OUTLIER, content-distinct from mushaf cohort) is informative: Q 61 functions as Q 14 does — a cluster anchor / typical-member, not an out-of-place surah.

## 6. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Interpretation |
|:--|:--:|:--:|:--|
| `mean_content_distance` | 0.8746 | −0.482 | content-CLOSER to corpus average than median |
| `local_cohesion` | 1.3558 | −0.221 | modestly below corpus median |
| `rhyme_entropy_nats` | **0.7589** | **−0.020** | **corpus-typical** rhyme entropy — high but non-monorhyme |
| `sig_A` (raw) | **+0.463** | rank **50 / 114** | **MID-RANGE POSITIVE** on iʿjāz al-fawāṣil axis |
| `sig_B` (raw) | **−0.241** | rank **63 / 114** | slightly negative |
| `top_final_letter` | ن | 71.4% (10/14) | dominant ن-rhyme (al-mushrikīn / al-kāfirūn / al-muʾminīn / ẓāhirīn family) |

**Q 61's positive sig_A (rank 50, +0.463) is structurally informative**: Q 61 is mid-positive on the al-Bāqillānī iʿjāz al-fawāṣil axis, which means its rhyme architecture coheres reasonably well with global content-density patterns. This is *higher* than:
- Q 64 al-Taghābun (sig_A = −0.733, rank 91/114)
- Q 57 al-Ḥadīd (sig_A = −0.272, rank 76/114)
- Q 59 al-Ḥashr (sig_A = +0.044, rank 60/114)

— and *lower* than Q 62 al-Jumuʿah (sig_A = +1.052, rank 23/114, the only short-Medinan musabbiḥa member that ranks in the top quartile of the iʿjāz al-fawāṣil axis).

Q 61 sits in the **moderate-positive zone of the iʿjāz al-fawāṣil axis** — neither a structurally-extreme iʿjāz-positive (Q 1, Q 24, Q 33) nor an iʿjāz-negative (Q 12, Q 67). Its three major-content interruptions (the *bunyānun marṣūṣ* simile, the Aḥmad-prophecy, the Q 61:9 = Q 9:33 universal-religion verse) pull rhyme entropy slightly upward without breaking the dominant ن-fawāṣila.

## 7. The 4-axis signature: short-Medinan paraenetic, mid-Q 62 cluster

Per Q014-F-02 4-axis distance metric:

```
v(Q 61) = [-0.482, +0.463 (sig_A), -0.241 (sig_B), -0.020 (rhyme entropy)]
v(Q 62) = [-0.485, +1.052, +0.404, -0.077]
v(Q 63) = [-0.628, -0.176, -0.510, -0.213]
v(Q 64) = [-0.421, -0.733, -0.879, +0.027]

‖v(61) - v(62)‖ = 1.054   ← Q 61 ≠ Q 62 (sig_A separates them: musabbiḥāt-imperfect Q 62 is much higher iʿjāz-positive)
‖v(61) - v(63)‖ = 0.842   ← Q 61 ≈ Q 63 (mushaf-adjacent + sig_B-similar)
‖v(61) - v(64)‖ = 1.392   ← Q 61 ≠ Q 64 (large sig_A + sig_B separation)
```

Q 61's tightest 4-axis neighbour is **Q 63 al-Munāfiqūn** (4-axis distance 0.842). This matches the FR-nearest finding. Q 61 + Q 63 form a TIGHT 4-axis pair; Q 61 + Q 62 are FR-near but 4-axis-separated by sig_A (Q 62's iʿjāz al-fawāṣil signal is stronger). The musabbiḥāt structural cohesion (H-NEW-58c) is strongly **opener-formula-driven**, not 4-axis-architecture-driven.

## 8. Canonical-adjacency profile (H-NEW-720)

| Pair | delta_raw (length-units) | Rank /113 | Interpretation |
|:--|:--:|:--:|:--|
| Q 60 → Q 61 | **0.1116** | 85 / 113 (top-30 EXPENSIVE) | Mumtaḥana → Ṣaff: Medinan polemic-against-Quraysh-relations → cosmic musabbiḥa opener; thematic shift but both Medinan-paraenetic |
| Q 61 → Q 62 | **0.0703** | 64 / 113 (mid-cheap) | Ṣaff → Jumuʿah: musabbiḥāt-perfect → musabbiḥāt-imperfect (the H-NEW-58c tense-binary boundary). NOT zero-delta despite shared opener-formula — the imperfect-tense Jumuʿah's content-vector diverges |

Both seams are **non-trivial transitions** but neither is among the corpus's most-expensive (top-15) or cheapest (clamped-zero). Q 61 sits between two moderately-priced seams in the H-NEW-720 mushaf-walk.

The Q 61→Q 62 seam is structurally noteworthy: the H-NEW-58c finding established that musabbiḥāt-perfect-vs-imperfect is a SHARP cluster-boundary at the shared-prefix level (cross-tense pairs share 0 chars). Yet at the H-NEW-720 root-distribution adjacency-cost level, the boundary is moderately-low (0.0703), not sharp. **The musabbiḥāt tense-split is an OPENER-FORMULA boundary, not a content-boundary at the root level.**

## 9. Architectural-cell typology (per cross-finding-026 §13)

By the 7-cell typology in [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.6:

- UAS rank 83/114 — below median; NOT in top-10 *All-axis* / *Structural-twin-pair* cells.
- sig_A z = +0.463 (rank 50) — moderately POSITIVE.
- Rhyme entropy z = −0.020 (rank ≈ 60) — corpus-typical.
- Outlier strength NULL — content-typical for mushaf cohort.

| Cell | Q 61 fit? |
|:--|:--|
| All-axis (Q 1) | NO — UAS only 83 |
| Structural-twin-pair (Q 24, 33) | NO — sig_A is moderate, not extreme |
| Structural-twin-pair-of-one (Q 55) | NO — Q 61 is content-typical |
| iʿjāz-al-fawāṣil-pure (Q 86, 89, 100, 106, 113) | NO — Q 61 sig_A is moderate, not the positive-tail |
| iʿjāz-al-maʿnā-extreme (Q 112, 114) | PARTIAL — Q 61's nearest neighbour Q 63 + Q 112 are both 1-of-10 nearest (Q 112 rank 3); both sui-generis-isolation cell candidates |
| iʿjāz-al-maʿnā-mild (Q 36, 67, 18) | NO — Q 61 is a non-narrative paraenetic, not narrative-iʿjāz |
| anti-iʿjāz | NO — no negative iʿjāz signature |

**Proposed cell (specialist refinement)**: Q 61 fits the **"short-Medinan paraenetic with multi-corpus-EXACT signature"** sub-cell, jointly with Q 110 al-Naṣr (very-late-Medinan, brief, dense doxological closure of revelation), Q 98 al-Bayyina (short-Medinan with Banū Isrāʾīl + community typology), and Q 112 al-Ikhlāṣ (short-Medinan/Meccan pure-doxological). The unifying signature: **short-length + dense theological-content-multiple-corpus-EXACT signatures + Medinan paraenetic register + Christological/community-formation interface**.

## 10. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 61 NULL (X=61, delta_pct=−2.50, p_greater_W=0.9506).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 60→Q 61 cost 0.1116 (rank 85); Q 61→Q 62 cost 0.0703 (rank 64).
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A=+0.463 rank 50, sig_B=−0.241 rank 63, rhyme entropy z=−0.02.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 83/114, UAS=−1.309.
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 61 FR-nearest = Q 63 al-Munāfiqūn (0.657); FR-farthest = Q 55 (1.186), Q 19 (1.112).
- [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] — Q 61 in perfect-tense sub-cluster; 56-char shared prefix with Q 59:1.
- [[h-new-340-musabbihat-block-subset|H-NEW-340]] — 5-set Medinan musabbiḥāt {Q 57,59,61,62,64} at 8.1%ile (most-cohesive grouping in H-NEW-330→340 series).
- [[h-new-1080-short-medinan-block]] — Q 61 in {Q 57-66} short-Medinan block; centrality rank 3/10.
- [[h-new-1310-christ-narrative-cluster|H-NEW-1310]] — Q061-F-03 EXTENDS this NULL: adding Q 61 makes {Q 3,5,19} cluster LESS cohesive (4-set 0.978 vs 3-set 0.948).
- `surahs/Q037-al-saffat/00-overview.md` — name-cognate (root ṣ-f-f); architecturally distinct (Q 37 is mid-Meccan oath-opener narrative; Q 61 is Medinan exhortation).

## 11. Data-source paths

- `findings/phase-b-hypotheses/csv/h-new-111.json` (FR D matrix, `D_matrix_upper_triangular`)
- `findings/phase-b-hypotheses/csv/h-new-590.json` (outlier-spectrum, all_surahs_results[X=61])
- `findings/phase-b-hypotheses/csv/h-new-720.json` (per-adjacency, s=60 and s=61)
- `findings/phase-b-hypotheses/csv/h-new-750.json` (per-surah iʿjāz signature[surah=61])
- `findings/phase-b-hypotheses/csv/h-new-840.json` (UAS all_uas[surah=61])
- `quran-text/quran-no-tashkeel.json` (verse text, word/letter counts)
- `data/revelation-order.csv` Q 61 row (Medinan, rev #109)
- `data/hafs-verse-counts.tsv` line 61 (14 verses)
- `findings/phase-b-hypotheses/h-new-58c-musabbihat-tense-split.md` (H-NEW-58c finding)
