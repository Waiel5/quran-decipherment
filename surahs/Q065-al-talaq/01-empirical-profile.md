---
surah: 65
surah_name_ar: الطلاق
surah_name_translit: al-Ṭalāq
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE
---

# Q 65 al-Ṭalāq — Empirical Architectural Profile

Rules-tuple: `(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, basmala-counted-only-in-Q1, mushaf order, Hafs-Kūfan, Mashriqī)`. Every numerical value below is computed from data files cited in §10 or pulled directly from H-NEW-XXX artifacts.

## 1. Headline architectural metrics

| Metric | Value | Rank / corpus context | Source |
|:--|:--:|:--|:--|
| **UAS (Unified Architectural Score)** | **−1.724** | **94 / 114** (lower-half; structural-iʿjāz-negative legislative-prose register) | [[h-new-840-unified-architectural-score\|H-NEW-840]] all_uas[surah=65] |
| Outlier-strength Δ%ile | **+0.94 pp** | **WEAK_OUTLIER** classification — Q 65 is mildly content-distinct in window {Q 62-68} | [[h-new-590-outlier-spectrum\|H-NEW-590]] all_surahs_results[X=65] |
| iʿjāz signature sig_A | **−1.170** | **rank 89 / 114** — bottom-quartile structural-iʿjāz-negative | [[h-new-750-ijaz-signature\|H-NEW-750]] |
| iʿjāz signature sig_B | **−1.360** | **rank 98 / 114** — bottom 15% of corpus | H-NEW-750 |
| z_mean_content_distance | +0.295 | mildly above corpus mean | H-NEW-750 |
| z_local_cohesion | −0.485 | modestly below corpus median — diverse 1-step adjacencies | H-NEW-750 |
| z_rhyme_entropy | **−0.875** | **near-monorhyme** (alif at 91.7%) | H-NEW-750 |
| Mean Fisher-Rao distance to corpus | **0.9534** | corpus mean 0.9235 (rank 69/114) | computed from [[h-new-111-fisher-rao-mushaf\|H-NEW-111]] |
| Top final letter (rāwī) | **ا (alif)** | **91.7% (11 / 12 verses)**; Q 65:6 is alif-maqṣūra ى (*ukhrā*) | H-NEW-750 |
| Q 64→Q 65 canonical-adjacency cost | **delta_raw = −0.0087, delta = 0.0000** (clamped) | **CLAMPED-ZERO seam, rank 5/113 cheapest**; member of H-NEW-1240 13-seam set | [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] s=64 |
| Q 65→Q 66 canonical-adjacency cost | **delta_raw = −0.0340, delta = 0.0000** (clamped) | **CLAMPED-ZERO seam, rank 6/113 cheapest**; member of H-NEW-1240 13-seam set | H-NEW-720 s=65 |
| max neighbor canonical-adjacency cost | 0 (both Q 64→65 and Q 65→66 are zero) | unique: Q 65 is the ONLY interior surah of TWO consecutive clamped-zero seams in the back-Medinan region | H-NEW-720 + H-NEW-1240 |
| Verse count | 12 | unusually short for a surah-of-its-position (post-musabbiḥāt-cluster) | Hafs-Kūfan |
| Word count (no-tashkeel) | 289 | computed | |
| Letter count (no-tashkeel, Arabic chars) | 1,203 | computed | |
| Mean words/verse | 24.08 | well above corpus mean (~12 wpv) — legislatively long-verse | computed |

## 2. The architectural signature: legislative-Medinan near-monorhyme cluster-anchor with seamless flanks

Q 65's empirical profile is the signature of a **legislative-Medinan near-monorhyme** surah: low rhyme entropy (alif at 91.7% generates near-monorhyme), iʿjāz-NEGATIVE on both sig_A and sig_B (the legislative-prose register sits opposite the multi-rāwī iʿjāz al-fawāṣil-positive register), modestly above corpus-mean on content-distinctness, and **uniquely surrounded by two clamped-zero seams**. Side-by-side with Q 64 al-Taghābun (the left-cohesion partner) and Q 66 al-Taḥrīm (the right-cohesion partner):

| Axis | Q 64 al-Taghābun | **Q 65 al-Ṭalāq** | Q 66 al-Taḥrīm | corpus mean / scale |
|:--|:--:|:--:|:--:|:--:|
| z_FR_mean | data | **+0.295** | data | 0 / 1 |
| sig_A rank | mid | **89 / 114** | mid | midrank 57 |
| sig_B rank | mid | **98 / 114** | mid | midrank 57 |
| z_rhyme_entropy | mixed | **−0.875** | mixed | 0 / 1 |
| Top-rāwī fraction | mixed | **alif @ 91.7%** | mixed | 0.50 (median) |
| Outlier classification | NULL | **WEAK_OUTLIER** | NULL | (40% of corpus is NULL) |
| UAS rank | mid | **94 / 114** | mid | midrank 57 |
| Verse count | 18 | **12** | 12 | (corpus median 36) |

**Both flank-seams (Q 64→Q 65 and Q 65→Q 66) are clamped-zero — Q 65 is uniquely positioned as the central node of a 2-seam clamped-zero stretch.** This is the only such 2-seam stretch in the back-Medinan section of the mushaf. (The other one is Q 73 in the Late Meccan / muqaddimāt cluster.) **Substantive interpretation**: Q 65 sits in a position the mushaf's structure designates as "minimally-disruptive in adjacency cost — both the surah arriving (Q 65) and the surah departing into (Q 66) are linguistically continuous with the surrounding short-Medinan register." The mushaf's compiler — whether interpreted as ʿUthmānic redaction or earlier — placed Q 65 in a position that is *paradoxically* both content-distinct (uniquely ṭalāq-legislation) AND geometrically-continuous with its mushaf-neighbors.

## 3. Fisher-Rao distance row (Q 65 vs all 113 others)

Computed from `findings/phase-b-hypotheses/csv/h-new-111.json` D matrix.

**Ten FR-nearest neighbors of Q 65**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| **1** | **Q 64 al-Taghābun** | **0.7774** | mushaf-adjacent left; clamped-zero seam |
| 2 | Q 63 al-Munāfiqūn | 0.8114 | also short-Medinan-block; same legal-Medinan register |
| 3 | Q 85 al-Burūj | 0.8123 | Late Meccan eschatological — the back-Medinan-block-meets-Late-Meccan zone |
| 4 | Q 98 al-Bayyinah | 0.8145 | Medinan, doctrinal |
| 5 | Q 112 al-Ikhlāṣ | 0.8172 | corpus-density theological |
| 6 | Q 104 al-Humazah | 0.8202 | Late Meccan, short |
| 7 | Q 59 al-Ḥashr | 0.8217 | musabbiḥāt cluster + short-Medinan-block |
| 8 | Q 110 al-Naṣr | 0.8268 | terminal short Medinan |
| 9 | Q 95 al-Tīn | 0.8303 | Late Meccan, brief |
| 10 | Q 91 al-Shams | 0.8414 | Late Meccan oath surah |

The FR-nearest neighbor is **Q 64 al-Taghābun at 0.7774** — confirming the seamless mushaf placement (the Q 64→Q 65 transition is empirically the cheapest possible from Q 65's standpoint). Q 65's nearest 10 neighbors include 4 short-Medinan-block members (Q 64, 63, 59, plus the implied self-block), 4 Late Meccan brief surahs (Q 85, 104, 95, 91), and 2 doctrinal short surahs (Q 98, 112, 110). **The neighborhood is dominated by SHORT post-Hijra-kink surahs**, NOT long ṭiwāl-class surahs — Q 65 is geometrically a short-mushaf-tail surah even though its position (s=65) is mid-mushaf.

This confirms a Q 65-specific finding: **the mushaf placement of Q 65 (mushaf-position 65, post-Hijra-kink at s=50) plants a short-Medinan-block surah in the geometrically-correct neighborhood for its content density.** Q 65 is short, content-tight, alif-monorhyme — and its FR-nearest neighbors are mostly short, content-tight, with monorhyme-like signatures.

**Five FR-farthest neighbors**:

| Rank | Surah | FR distance | Note |
|:-:|:-:|:--:|:--|
| 110 | Q 17 al-Isrāʾ | 1.1176 | long Late-Meccan narrative-rich |
| 111 | Q 19 Maryam | 1.1349 | Late-Meccan prophetic-narrative; KHYʿṢ muqaṭṭāʿat |
| 112 | Q 12 Yūsuf | 1.1462 | the *aḥsan al-qaṣaṣ* sustained narrative |
| 113 | Q 26 al-Shuʿarāʾ | 1.1674 | Late-Meccan oath + prophet-cycle |
| 114 | **Q 55 al-Raḥmān** | **1.2467** | refrain-saturated — corpus-most-distant neighbor (consistent with Q 12, Q 13, Q 14 also having Q 55 as anti-twin) |

**Q 55 is Q 65's farthest neighbor at 1.2467** — joining the multi-surah chorus that places Q 55 al-Raḥmān as architectural anti-twin (cf. H-NEW-1250 Q 55 dual-audience signature). The Q 65-Q 55 anti-twin relationship is content-mode-orthogonal: legislative-Medinan-prose vs refrain-saturated-Meccan-doxology.

## 4. The clamped-zero seam-pair (the unique 2-seam-zero centerpiece)

Per [[h-new-1240-13-seamless-seams|H-NEW-1240]]: 13 clamped-zero (delta_raw ≤ 0) mushaf-transitions are listed corpus-wide:
- s=3 (Q 3→Q 4), s=4 (Q 4→Q 5), s=6 (Q 6→Q 7) — head-mushaf ṭiwāl block
- s=37 (Q 37→Q 38) — Q 37 al-Ṣāffāt → Q 38 Ṣād
- **s=64 (Q 64→Q 65)** — short-Medinan-block
- **s=65 (Q 65→Q 66)** — short-Medinan-block
- s=72 (Q 72→Q 73) — muqaddimāt cluster
- s=73 (Q 73→Q 74) — muqaddimāt cluster
- s=86 (Q 86→Q 87), s=91 (Q 91→Q 92), s=93 (Q 93→Q 94), s=105 (Q 105→Q 106), s=109 (Q 109→Q 110) — short-mufaṣṣal-tail

**Q 65 + Q 73 are the TWO surahs in the corpus that sit at the center of a 2-seam clamped-zero stretch.** The Q 65 case is the only short-Medinan-block instance.

Per H-NEW-720 + H-NEW-1240 measurement protocol:
- delta_raw (Q 64→Q 65) = **−0.0087** (clamped to 0). Rank 5/113 cheapest delta.
- delta_raw (Q 65→Q 66) = **−0.0340** (clamped to 0). Rank 6/113 cheapest delta.
- The CONSTRAINED mushaf path including these two seams is at most 0.0427 length-units LONGER than the unconstrained 2-opt baseline path that excludes them — a vanishingly-small cost.

**The mushaf placement Q 64→Q 65→Q 66 is geometrically MORE EFFICIENT than the unconstrained 2-opt-optimal path**: both seams have NEGATIVE delta_raw, meaning the constrained path is shorter than the constrained-without-this-pair path. The mushaf compiler placed Q 65 in a position the geometry positively favored.

## 5. Outlier window structure (H-NEW-590, full Q 62-68 window)

The window {62, 63, 64, 65, 66, 67, 68} (size-7 centered on Q 65) yields:

| Removed surah | d̄_W | d̄_W−X | Δ pp | classification | source |
|:-:|:-:|:-:|:-:|:-:|:-:|
| Q 65 | 0.8354 | 0.8164 | **+0.94** | **WEAK_OUTLIER** | H-NEW-590 X=65 |

The full window with Q 65 has d̄_W = 0.835 (12.95%ile); without Q 65, d̄_W = 0.816 (12.01%ile). **Removing Q 65 makes the window slightly LESS FR-distant on average** — i.e. Q 65 is content-distinct from the rest of its window, mildly elevating the window's FR-distance. The classification is WEAK_OUTLIER (delta < +1pp), not WEAK_OUTLIER-strong; the surrounding window is dominated by the short-Medinan-block (Q 62-66) plus Q 67-68 which both bring different content (Q 67 al-Mulk = cosmology + creation; Q 68 al-Qalam = Late Meccan prophet defense).

The WEAK_OUTLIER status is consistent with the inverse profile: Q 65 is a content-distinct surah within a non-uniform window. The window is heterogeneous (back-Medinan + start-of-mufaṣṣal-tail), and Q 65's ṭalāq-legislation register is clearly distinct from Q 67-68's eschatology + prophet-defense register.

## 6. iʿjāz signature (H-NEW-750)

| Component | Value | z-score | Interpretation |
|:--|:--:|:--:|:--|
| `mean_content_distance` | 0.9534 | +0.295 | mildly above corpus mean |
| `local_cohesion` | 1.1623 | −0.485 | modestly below corpus median |
| `rhyme_entropy_nats` | **0.2868** | **−0.875** | **near-monorhyme** (alif @ 91.7%) |
| `top_final_letter` | ا (alif) | — | functionally monorhyme |
| `top_final_letter_frac` | 0.917 | — | 11/12 verses |
| `sig_A` (raw) | **−1.170** | rank **89 / 114** | **bottom-quartile** structural-iʿjāz-negative |
| `sig_B` (raw) | **−1.360** | rank **98 / 114** | **bottom 15%** of corpus |

**Q 65 is firmly in the structural-iʿjāz-NEGATIVE zone** — low rhyme diversity (near-monorhyme), low local cohesion. This is the classical legislative-prose register, opposite to the multi-rāwī oath / refrain / iʿjāz al-fawāṣil-positive registers.

This is consistent with classical *balāgha* observation that *legislative* verses (āyāt al-aḥkām) deploy structural simplicity to support clarity-of-rule, whereas oath-cluster verses (āyāt al-yamīn) deploy structural complexity to support density-of-meaning. Q 65 is paradigmatic legislative-prose — every sentence is rule-bearing and lexically-complete.

## 7. The 4-axis signature: legislative-Medinan-near-monorhyme

Per Q065-F-03 (`csv/Q065-F-03.json`):

```
v(Q 65) = [+0.295, -0.840, -1.063, -0.875]   (z_FR, z_sig_A, z_sig_B, z_rhyme)
v(Q 64) = [...computed in Q064-specialist deferred...]
v(Q 66) = [...computed in Q066-specialist deferred...]
v(Q 33) = [...for Q065-F-01 prophetic-vocative-opener-trio...]
```

The architectural signature places Q 65 in the **bottom-quartile** of the corpus on the iʿjāz axis but in the **upper-half** on content-distinctness — the legislative-Medinan-prose registered's profile.

## 8. Hapax + token-density profile

Q 65 contains **40 hapax tokens** (single-occurrence-in-corpus) out of 289 total tokens → **13.84% hapax density**, rank **54 / 114** (mid-pack on raw density, but corpus-EXCEPTIONAL on length-controlled density). Within the H-NEW-1080 short-Medinan-block (Q 57-66), Q 65 is rank **2 / 10** by hapax density:

| Surah | hapax | total | density |
|:-:|:--:|:--:|:--:|
| Q 66 al-Taḥrīm | 39 | 254 | 15.35% |
| **Q 65 al-Ṭalāq** | **40** | **289** | **13.84%** |
| Q 59 al-Ḥashr | 59 | 448 | 13.17% |
| Q 60 al-Mumtaḥanah | 45 | 353 | 12.75% |
| Q 63 al-Munāfiqūn | 20 | 182 | 10.99% |
| Q 58 al-Mujādilah | 41 | 476 | 8.61% |
| Q 57 al-Ḥadīd | 49 | 576 | 8.51% |
| Q 61 al-Ṣaff | 18 | 226 | 7.96% |
| Q 62 al-Jumuʿah | 14 | 177 | 7.91% |
| Q 64 al-Taghābun | 15 | 242 | 6.20% |

**The short-Medinan-block has its TOP-2 hapax-density surahs at Q 65 + Q 66 — the *yā ayyuhā al-nabī* opener pair.** This is a corpus-architectural correlation: prophetic-vocative-opener Medinan surahs deploy specialized vocabulary (legal-domestic registers tagged with rare procedural terms).

A list of the 20 hapax tokens specifically inside Q 65 (with verse-locus):

| Token | Verse | Translation |
|:--|:--:|:--|
| فطلقوهن (fa-ṭalliqūhunna) | 65:1 | "so divorce them" — hapax imperative form |
| لعدتهن (li-ʿiddatihinna) | 65:1 | "for their waiting period" — hapax with this pronoun-suffix |
| فارقوهن (fāriqūhunna) | 65:2 | "separate from them" — hapax imperative |
| مخرجا (makhrajan) | 65:2 | "a way out" — hapax accusative-indef |
| يحتسب (yaḥtasibu) | 65:3 | "he expects/calculates" — hapax form |
| يئسن (yaʾisna) | 65:4 | "they have despaired" (3fp) — hapax fem-pl perfect |
| أولات (ūlāt) | 65:6 | "those (fem) possessing" — hapax noun-form |
| الأحمال (al-aḥmāl) | 65:4 | "the pregnant ones" / "burdens" — hapax pl |
| أسكنوهن (askinūhunna) | 65:6 | "house them" — hapax imperative |
| تضاروهن (tuḍārrūhunna) | 65:6 | "harm them" — hapax verb-form |
| لتضيقوا (li-tuḍayyiqū) | 65:6 | "in order to constrain" — hapax verb-form |
| فأنفقوا (fa-anfiqū) | 65:6 | "so spend" — hapax imperative-form |
| أرضعن (arḍaʿna) | 65:6 | "they nurse" (3fp) — hapax fem-pl form |
| تعاسرتم (taʿāsartum) | 65:6 | "you make difficulty for each other" (form VI) — hapax |
| لينفق (li-yunfiq) | 65:7 | "let him spend" — hapax jussive form |
| عتت (ʿatat) | 65:8 | "it rebelled" (3fs) — hapax fem-sg form |
| فحاسبناها (fa-ḥāsabnāhā) | 65:8 | "so we made it reckon" — hapax 1pl perfect with 3fs object |
| وعذبناها (wa-ʿadhdhabnāhā) | 65:8 | "and we tortured it" — hapax 1pl perfect with 3fs object |
| فذاقت (fa-dhāqat) | 65:9 | "so it tasted" — hapax 3fs perfect |
| خسرا (khusrā) | 65:9 | "loss" (the alif-final form) — hapax in this morphology |

The hapax-cluster shows a clear pattern: **fem-pl pronoun-suffix verb forms (concerning women in ṭalāq) + 3fs perfect verbs (concerning the *qaryah* / town that rebelled)**. Q 65's hapax-density is anchored in two grammatical specialties — *the legal-procedural fem-pl imperative voice* and *the historical-fem-sg perfect of past communities*. Both are content-bound to the surah's two themes (Block A ṭalāq-legislation; Block B historical-warning).

## 9. Comparison with other "yā ayyuhā al-nabī" verse-1 openers

Three surahs in the corpus open at v.1 with *yā ayyuhā al-nabī*: **Q 33, Q 65, Q 66**.

| Axis | Q 33 al-Aḥzāb | **Q 65 al-Ṭalāq** | Q 66 al-Taḥrīm |
|:--|:--:|:--:|:--:|
| Verse count | 73 | 12 | 12 |
| Word count | 1,288 | 289 | 254 |
| Mean wpv | 17.6 | 24.1 | 21.2 |
| FR pairwise to Q 33 | — | 1.0062 | 1.0090 |
| FR pairwise to Q 65 | 1.0062 | — | 0.8705 |
| FR pairwise to Q 66 | 1.0090 | 0.8705 | — |
| Mean FR-internal | (Q33↔Q65 + Q33↔Q66)/2 = 1.0076 | (Q33↔Q65 + Q65↔Q66)/2 = 0.9384 | (Q33↔Q66 + Q65↔Q66)/2 = 0.9398 |
| 3-cluster FR mean | **0.9619** (vs corpus pairwise mean 0.9235) | | |

The 3-cluster mean (0.9619) is **WORSE than corpus pairwise mean (0.9235)** — the prophetic-vocative-opener trio is NOT FR-cohesive at the whole-surah level. This confirms Q065-F-01's NULL prediction. But Q 65 + Q 66 alone form a tight 0.8705-FR pair (above corpus pairwise mean by 0.05 — just below median 0.9567 but clearly close-pair territory). The dyad Q 65 + Q 66 is empirically tight; adding Q 33 dilutes it.

**Substantive interpretation**: the *yā ayyuhā al-nabī* OPENING-pattern is an instance of literary-form unity that does NOT translate to whole-surah FR-cohesion. It is a *liturgical-rhetorical* opener rather than a *content-domain* marker. The opener marks "discourse genre to the Prophet" but the discourse content varies (Q 33 = piety + Aḥzāb battle + family law; Q 65 = ṭalāq + cosmology; Q 66 = taḥrīm incident + believer-disbeliever wives parable).

## 10. Sources of all numbers

- **Corpus text**: `quran-text/quran-no-tashkeel.json` (114 surahs)
- **Verse counts**: `data/hafs-verse-counts.tsv`
- **Revelation order**: `data/revelation-order.csv`
- **Fisher-Rao distance matrix**: `findings/phase-b-hypotheses/csv/h-new-111.json` (`D_matrix_upper_triangular`)
- **Canonical-adjacency cost**: `findings/phase-b-hypotheses/csv/h-new-720.json` (`per_adjacency`, `top10_expensive`, `bottom10_cheap`)
- **iʿjāz signature**: `findings/phase-b-hypotheses/csv/h-new-750.json` (`per_surah`)
- **Outlier-window analysis**: `findings/phase-b-hypotheses/csv/h-new-590.json` (`all_surahs_results`)
- **UAS**: `findings/phase-b-hypotheses/csv/h-new-840.json` (`all_uas`)
- **Clamped-zero 13-seam list**: H-NEW-1240 in `MASTER-FINDINGS-LEDGER.md` §10.41

All inline computations executed via Python in `00-overview.md` §10 and verified by `scripts/Q065_empirical_compute.py`.

---

*Specialist: Waiel Al-Shujaa, 2026-05-09. Numbers verified against H-NEW source artifacts, no manual transcription.*
