---
surah: 16
file_type: empirical-profile
date_last_updated: 2026-05-07
---

# Q 16 al-Naḥl — Empirical Profile


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

All values computed from disk; cite paths.

## 1. Basic counts

| Metric | Value | Source |
|:--|:--|:--|
| Verse count | 128 | Hafs-Kufan (`quran-text/quran-no-tashkeel.json`) |
| Token count (no-tashkeel orthographic) | 1,963 | computed `00-overview` |
| Letter count (no-tashkeel, no-spaces) | 7,951 | computed |
| QAC unique-root count | 358 | h-new-126 cell-D |
| Mean verse-length (tokens) | 14.41 | h-new-126 |
| Allah-density per 100 verses | 64.06 | h-new-126 |

## 2. Position metrics

| Metric | Value | Source |
|:--|:--|:--|
| Mushaf-position s | 16 | canonical |
| Tanzil revelation-rank | 70 | `data/revelation-order.csv` |
| Nöldeke revelation-rank | 73 | `data/revelation-order.csv` |
| |chrono displacement| (Tanzil) | **54** | computed |
| |chrono displacement| (Nöldeke) | **57** | computed |
| Distance to Hijra-kink (s=50) | 34 (pre-kink, head-mushaf) | cross-finding-026 |

## 3. Outlier-spectrum (h-new-590)

```
window={Q13..Q19}    d_W = 0.9461
window-minus-Q16     d_W = 0.9482
delta_pct = +0.47pp   classification = WEAK_OUTLIER
p_greater_W = 0.4522 (random within window)
rank in corpus by outlier-strength: 30/114
```

**Q 16 is content-INVISIBLE in its 7-window {Q 13–19}: removing Q 16 leaves the local-window distance essentially unchanged.** This is the structural signature of a "true-isolate" that does NOT manifest as content-distinctness from local neighbors — it manifests as cluster-invisibility (see h-new-126).

## 4. iʿjāz signature (h-new-750)

| Metric | Value | z-score | Rank |
|:--|:--|:--|:--|
| Rhyme entropy (nats) | 0.4552 | −0.57 | rhyme-uniform |
| Top-final-letter | ن | — | — |
| Top-final-letter fraction | 0.859 (110/128) | — | — |
| Mean content distance | 1.0278 | +1.03 | high (corpus 79th-percentile content-distance) |
| Local cohesion | 1.0504 | −0.64 | low (cohesive with mushaf-neighbors) |
| sig_A = z(rhyme) − z(content) | **−1.599** | — | **rank 94/114** |
| sig_B (alternative) | **−1.207** | — | rank 90/114 |

**Q 16 is in the BOTTOM-25% of iʿjāz signature.** The surah is rhyme-uniform AND locally-cohesive — the opposite of high-iʿjāz al-fawāṣil. This is consistent with the late-Meccan declarative-monorhyme regime; Q 16 is *not* doing rhyme-variety work.

## 5. UAS (h-new-840)

| Component | Value |
|:--|:--|
| UAS | 0.5817 |
| abs_outlier (h-590) | 0.470 |
| max_cost (h-720 adjacency) | 0.191 |
| abs_ijaz (h-750) | 1.599 |
| **UAS rank** | **30/114** |

Above corpus-median UAS but well outside top-15. Q 16 is a "mid-architectural-significance" surah — empirically present in many laws but not a primary structural pole.

## 6. FR-distance neighbors (h-new-111)

```
Q 16 nearest 5 (FR distance):
  Q 39 al-Zumar     d = 0.7538   (Meccan, late, *huwa lladhī sakhkhara* niʿmah-language)
  Q 22 al-Ḥajj      d = 0.7559   (CO-ISOLATE — see H-NEW-126)
  Q  6 al-Anʿām     d = 0.7815   (Meccan, niʿmah-catalog also)
  Q 13 al-Raʿd      d = 0.8037   (ALR, mushaf-neighbor)
  Q 29 al-ʿAnkabūt  d = 0.8044   (Meccan, mathāl-style)

Q 16 farthest 5:
  Q 107 al-Māʿūn    d = 1.187    (terminal qiṣār, refrain-style)
  Q  89 al-Fajr     d = 1.191    (terminal qiṣār)
  Q 111 al-Masad    d = 1.195    (anti-Abū Lahab polemic)
  Q  80 ʿAbasa      d = 1.210    (very short Meccan)
  Q  55 al-Raḥmān   d = 1.329    (corpus-max for Q 16; refrain saturation)
```

**Q 22 (al-Ḥajj) — another true-isolate — is Q 16's 2nd-FR-nearest neighbor.** Empirically meaningful: even though both are "true-isolates" (invisible to all 20 cluster taxonomies, h-new-126), they are content-near each other under the FR-roots metric. The 5-isolate cluster has empirical content-cohesion at h-new-126 cell-A (mean root-Jaccard 0.341 vs null 0.129, p ≈ 9 × 10⁻⁴).

## 7. Canonical-adjacency cost (h-new-720)

```
pair (15, 16): delta = 0.1698, fraction_residual = 2.05%
pair (16, 17): delta = 0.1910, fraction_residual = 2.30%
```

Both Q15→Q16 and Q16→Q17 transitions cost a moderate ~2pp of total mushaf-vs-FR-TSP residual. Neither is in the top-10 most-expensive adjacencies (which are dominated by Q 1→Q 2 = 7.5%).

The Q 16 placement is **not free** but not catastrophic: the mushaf "pays" for embedding a no-muqaṭṭaʿāt Meccan-late surah between Q 15 (ALR muqaṭṭaʿāt, mid-Meccan) and Q 17 (no muqaṭṭaʿāt, *subḥāna lladhī asrā*).

## 8. True-isolate cell membership (h-new-126)

Q 16 is a member of the **5 TRUE-ISOLATE core** = {Q 16, 21, 22, 23, 25}. Per h-new-126:
- Cell A (mean root-Jaccard within-cluster): observed 0.341 vs null mean 0.129 (p=9×10⁻⁴, **PASS**)
- Cell B (genre coherence): see h-new-126
- Cell C (rhetorical mode): see h-new-126
- Cell D (per-surah top-extremity axis): for Q 16 = `unique_root_count` (358, **92.5th-percentile, HIGH**)
- 2nd extremity axis: `surah_length` (128 verses, **91.7th-percentile, HIGH**)
- 3rd extremity axis: `root_density` (0.194 unique-roots/token, **10.1st-percentile, LOW** — much repetition is ABSENT)

## 9. Compression-tail position (h-new-660 / cross-finding-026)

```
d̄_content(s=16) ≈ 0.96 − 0.012 · max(0, 16-50) = 0.96 (head, pre-kink)
d̄_rhyme(s=16) ≈ 0.36 + 0.0041 · max(0, 16-50) = 0.36 (head, pre-kink)
d̄_phoneme(s=16) ≈ 0.0013 (head, pre-kink)
```

Q 16 is **firmly in the head-mushaf zone** (s < 50). Per cross-finding-026:
- **Head ṭiwāl pole** (Q 1–17): content-DISPERSED, rhyme-UNIFORM → al-sabʿ al-ṭiwāl. Q 16 fits this pole's profile (rhyme-uniform 85.9%, mean-content-distance high).

## 10. Rhyme — final-letter inventory (n=128)

| Final letter | Count | Fraction |
|:--|:-:|:--|
| ن (nūn) | 109 (110 if sajda-glyph counted with ن) | 85.2% |
| م (mīm) | 16 | 12.5% |
| ر (rāʾ) | 2 | 1.6% |
| ۩ sajda glyph | 1 (after Q 16:50) | — |

**Sajda al-tilāwa marker** at Q 16:50 — one of 14 *sajda-of-recitation* points in the corpus. Verified by ʿUmar's Bukhari 1046 narration (see `04-hadith-corpus.md`).

## 11. Cross-references

- [[h-new-111]] — FR-roots distance (Q 16 nearest = Q 39, 22, 6, 13, 29)
- [[h-new-126]] — TRUE-ISOLATE-CORE membership
- [[h-new-281]] — within-zone Jaccard (true-isolate persistence)
- [[h-new-590]] — outlier spectrum (Q 16 = WEAK_OUTLIER, +0.47pp)
- [[h-new-700]] — phonological compression-tail (Q 16 head-pre-kink)
- [[h-new-720]] — TSP adjacency Q15-Q16-Q17
- [[h-new-750]] — iʿjāz signature (Q 16 sig_A rank 94/114, BOTTOM-25%)
- [[h-new-840]] — UAS rank 30/114
- [[cross-finding-026-iʿjāz-architecture]] — head-ṭiwāl pole assignment
- [[cross-finding-010]] — true-isolate set
- [[Q022-al-hajj]] — Q 16's 2nd-FR-nearest, co-isolate
- [[Q025-al-furqan]] — sister isolate, design-parent of Q016-F-03
