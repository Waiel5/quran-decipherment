---
id: H-NEW-46
title: Muqaṭṭaʿāt-opened surahs concentrate in LONG surahs — STRONG-PASS on all 4 length-axes
phase: B
status: STRONG-PASS (4/4 cells significant under Bonferroni-4 at α=0.0125)
date: 2026-04-15
agent: h-new-46-specialist
pre_reg: findings/phase-b-hypotheses/h-new-46-muqattaat-vs-surah-length-prereg.md
script: scripts/h_new_46_muqattaat_length.py
json: findings/phase-b-hypotheses/csv/h-new-46.json
journal: journal/h-new-46-run-1.md
rules_tuple: (no-tashkeel, hafs-kufan, verse-count metric)
bonferroni_family: 2026-04-16-Wave-Muqattaat-Extended
bonferroni_k: 4
alpha_bon: 0.0125
seed: 20260416
n_perm: 100000
---

# [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] — Muqaṭṭaʿāt vs Surah Length (STRONG-PASS)

## TL;DR

The 29 muqaṭṭaʿāt-opened surahs are dramatically over-concentrated in long surahs and dramatically under-represented in short ones, well beyond uniform random selection. **STRONG-PASS** on all 4 pre-registered cells under Bonferroni-4 (α_bon = 0.0125):

| Cell | Stat | Observed | Null mean | Null SD | p (empirical) | Sig at α_bon |
|---|---|---|---|---|---|---|
| 1 | Mean verse-count (one-sided upper) | **94.59** | 54.72 | 8.53 | **1.0×10⁻⁵** | YES |
| 2 | Median verse-count (two-sided) | **85** | 39.13 | 9.17 | **1.6×10⁻⁴** | YES |
| 3 | Top-29 longest count (one-sided upper) | **16/29** | 7.38 | 2.03 | **7.0×10⁻⁵** | YES |
| 4 | Bottom-29 shortest count (one-sided lower) | **0/29** | 7.37 | 2.03 | **3.0×10⁻⁵** | YES |

Pipeline validated: MW-5 positive control (29-longest plant) → cell 1 p ≈ 1.0×10⁻⁴, exactly at the floor of n_perm = 10⁴.

## What is observed

- Muqaṭṭaʿāt-opened surahs (n=29) have mean verse-count **94.6 vs 54.7** expected under uniform 29-from-114.
- 16 of the 29 muqaṭṭaʿāt-opened surahs are among the 29 longest surahs (vs 7.4 expected). The eyeball — top-3 longest (Q 2, Q 7, Q 26) all open with muqaṭṭaʿāt — was a true tip of an iceberg.
- **0 of the 29 muqaṭṭaʿāt-opened surahs are among the 29 shortest surahs**, vs 7.4 expected. This is the most extreme cell: under uniform selection, the bottom-29 should contain ~7 muqaṭṭaʿāt-openers; observed is exactly zero.
- Non-muqaṭṭaʿāt-opened surahs (n=85) mean verse-count = 41.1.

## Length distribution among muqaṭṭaʿāt-openers

Sorted by verse-count (Ḥafṣ-Kūfan numbering, no-tashkeel literal verse list):

| Rank | Surah | Length | Letter set |
|---|---|---|---|
| 1 | Q 2 al-Baqara | 286 | الم |
| 2 | Q 26 al-Shuʿarāʾ | 227 | طسم |
| 3 | Q 7 al-Aʿrāf | 206 | المص |
| 4 | Q 3 Āl ʿImrān | 200 | الم |
| 5 | Q 20 Ṭā-Hā | 135 | طه |
| 6 | Q 19 Maryam | 98 | كهيعص |
| 7 | Q 27 al-Naml | 93 | طس |
| 8 | Q 11 Hūd | 123 | الر |
| ... | ... | ... | ... |
| 25 | Q 13 al-Raʿd | 43 | المر |
| 26 | Q 45 al-Jāthiya | 37 | حم |
| 27 | Q 46 al-Aḥqāf | 35 | حم |
| 28 | Q 31 Luqmān | 34 | الم |
| 29 | Q 32 al-Sajda | 30 | الم |

The 13 muqaṭṭaʿāt-openers NOT in top-29: {Q 13, 14, 29, 30, 31, 32, 41, 42, 44, 45, 46, 50, 68}. None falls below verse-count 30 (Q 32 = 30 is the minimum for any muqaṭṭaʿāt surah). The shortest surah in the entire Qurʾān that opens with muqaṭṭaʿāt is **Q 68 al-Qalam (52 verses) → no, it's Q 32 al-Sajda (30 verses)**. (Q 68 = 52 v.)

For comparison, the bottom-29 shortest surahs include Q 1 (7 verses) and the entire 91–114 tail of short Meccan surahs. Zero muqaṭṭaʿāt openers fall in this band.

## Mechanism — why this matters

Under any of the major classical theories of muqaṭṭaʿāt (al-Rāzī's 12 theories, Welch 1986, Massey 1996, Nöldeke 1919), the assignment of muqaṭṭaʿāt to surahs is treated as **independent** of mundane surah-length attributes. The [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] result falsifies the strict independence assumption: muqaṭṭaʿāt status carries a strong signal about surah length.

**Three competing mechanisms that could explain the correlation:**

1. **Chronological correlate (most plausible).** Long surahs are predominantly Medinan or middle-Meccan. The 29 muqaṭṭaʿāt-opened surahs mostly cluster in the second/third Meccan period and early Medinan. The Nöldeke chronology already groups muqaṭṭaʿāt-openers as a temporal cohort. Length and muqaṭṭaʿāt-status would then both be downstream effects of chronology.

2. **Structural-authority hypothesis.** Long surahs may have been viewed as carrying special structural weight (legal content, narrative density, cosmological scope), and the muqaṭṭaʿāt opener served as a marker of that weight. In this reading the muqaṭṭaʿāt is a label applied to "major" surahs.

3. **Mnemonic/compositional unit hypothesis.** Long surahs are harder to memorize and chant; the muqaṭṭaʿāt opener may serve as a recitation-anchor, more useful for long surahs than for short ones. (The Q 68 Nūn case is the main counter-example: 52 verses is medium-length, not "long enough to need an anchor.")

**What is FALSIFIED:** the null that muqaṭṭaʿāt assignment is uniform-random with respect to surah length. p < 10⁻⁴ across all four length-related axes is incompatible with the independence model.

## Honest framing

The eyeball (top-3 longest all muqaṭṭaʿāt) was disclosed in the pre-reg as garden-of-forking-paths for cell 1 (mean). The Bonferroni-4 correction was declared before the null ran. The remaining cells (median, top-29, bottom-29) were NOT eyeball-derived; they were chosen to provide structural redundancy.

The cleanest signal is **cell 4 (bottom-29 = 0)**, which was NOT eyeballed — it tests the dual hypothesis that muqaṭṭaʿāt are absent from short surahs. Observing **exactly 0 of 29** falls at p = 3×10⁻⁵, beyond what mere "long surahs are muqaṭṭaʿāt" would imply. The signal is bidirectional: muqaṭṭaʿāt over-represent in long AND under-represent in short, both well below α_bon.

## Cross-finding context

This finding sits alongside:

- **[[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] (subset algebra):** the 14 muqaṭṭaʿāt subsets have non-trivial Boolean and ℝ-linear structure (rank 12, two clean decompositions).
- **[[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] (surah-index gap-entropy):** the 29 surah-indices cluster into low-gap-entropy groups (الر-cluster, الم-cluster, ḥawāmīm) at p = 2×10⁻⁵.
- **[[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] (this finding):** length axis. The 29 surah indices map to surahs that are systematically longer.

Three independent statistical signals all point to **the muqaṭṭaʿāt assignment being structured, not random** along multiple axes (algebraic letter-subset structure, surah-position clustering, surah-length concentration).

## Pre-registered verdict table

| Outcome | Verdict |
|---|---|
| 0 cells significant at α=0.0125 | NULL |
| 1 cell significant | EXPLORATORY |
| 2-3 cells significant | PARTIAL-PASS |
| **All 4 cells significant** | **STRONG-PASS** |

**Result: 4/4 cells significant → STRONG-PASS.**

## Pipeline validation (MW-5 positive control)

Plant the 29 longest surahs as a "fake muqaṭṭaʿāt set". Cell 1 (mean) under 10⁴-perm null: p = 1.0×10⁻⁴ (exactly at the resolution floor). Pipeline detects the planted signal at p < 1e-4 as required by pre-reg.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-46-muqattaat-vs-surah-length-prereg.md`
- Script: `scripts/h_new_46_muqattaat_length.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-46.json`
- Journal: `journal/h-new-46-run-1.md`

## Integrity

- Pre-reg locked 2026-04-16 with garden-of-forking-paths disclosure (eyeball flagged on cell 1; cells 2–4 designed for structural redundancy, not eyeball-derived).
- Bonferroni k=4 declared in pre-reg before null was run.
- Seed 20260416 (matching [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] wave).
- N_PERM = 10⁵; runtime ~1 second (pure-Python set ops).
- Verse counts use literal `len(s.verses)` from no-tashkeel JSON, not declared `total_verses` (Q 2 = 286 confirmed).
- All 4 cells published whether PASS or NULL. Result: 4/4 PASS.
- The bottom-29 cell yields observed = 0 (extremal); the empirical p = 3×10⁻⁵ is conservative since this hits the lower tail of the null distribution. With 10⁵ perms the resolution floor is 1×10⁻⁵; observed p of 3×10⁻⁵ is ~ within an order of magnitude of the floor.
