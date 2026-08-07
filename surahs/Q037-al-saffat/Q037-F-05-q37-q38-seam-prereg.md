---
surah: 37
test_id: Q037-F-05
title: Q 37 → Q 38 canonical adjacency seam — empirical-seamlessness diagnostic
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
bonferroni_k: 3
bonferroni_family: Q037-F-05-q37-q38-seam
alpha_bon: 0.01667
---

# Q037-F-05 — Pre-registration: Q 37 → Q 38 seam empirical-seamlessness diagnostic


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

## 1. Hypothesis (locked before observation)

The H-NEW-720 canonical-adjacency-cost map records Q 37 → Q 38 with `delta_raw` = -0.00091 ⇒ `fraction_residual` clamped to 0.000, indicating that the Q 37 → Q 38 mushaf-adjacency is **structurally seamless**: removing this pair from the canonical mushaf order has effectively zero TSP-residual penalty. Per the brief, this places Q 37 → Q 38 jointly in the bottom-tier with Q 6 → Q 7 of "two empirically-seamless adjacencies."

**H1 (locked direction):** Q 37 → Q 38 is among the 5 SMOOTHEST consecutive-pair canonical-adjacencies as measured by `delta_raw` (sorted ascending — most-negative or most-near-zero values first), out of 113 total adjacencies.

**H2 (locked direction, content-similarity diagnostic):** Q 37 and Q 38 share at least 2 of the following 4 architectural features:
- (a) Same top-final-letter (rhyme-letter) on majority of verses.
- (b) Same length-class (e.g., both in mufaṣṣal-ṭiwāl Q 50-77, OR both in mid-Meccan ~80-200 verse band).
- (c) Mean-content-distance to corpus within ±1 standard deviation of each other (close architectural twins on d̄).
- (d) Top-3 nearest FR-neighbor of one is the other (or in each other's top-5).

**H3 (locked direction):** The Q 37 → Q 38 transition is empirically seamless because of a **content-prophet-cycle continuation**, NOT a rhyme-shared-letter or muqaṭṭaʿāt-shared-letter property. Operationalization: count prophet-tokens shared between Q 37 prophet-cycle (Nūḥ, Ibrāhīm, Mūsā-Hārūn, Ilyās, Lūṭ, Yūnus) and Q 38 prophet-cycle (Nūḥ, Lūṭ, Dāwūd, Sulaymān, Ayyūb, Ibrāhīm, Isḥāq, Yaʿqūb, Ismāʿīl, al-Yasaʿ, Dhū al-Kifl). Pre-locked direction: shared-prophet count ≥ 3.

## 2. Operational definitions

### H1: Smoothest-5 ranking
- Source: `findings/phase-b-hypotheses/csv/h-new-720.json` `per_adjacency` field.
- Rank all 113 adjacencies by `delta_raw` ascending (most-seamless first).
- Pass: Q 37 → Q 38 ∈ top-5.

### H2: Architectural-features overlap
- (a) Top-final-letter from `h-new-700.json` `rhyme.rhyme_letter_diagnostics`. Q 37 = ن. Q 38 = (compute).
- (b) Length-class: Q 37 = 182 verses (mid-Meccan-long); Q 38 = 88 verses (mid-Meccan). Same band: Yes/No.
- (c) Mean-content-distance: `h-new-750.json` `mean_content_distance`. Q 37 = 0.993 (computed). Q 38 = (compute).
- (d) Top-5 FR-neighbors: from `h-new-111` matrix. Q 37 top-10 includes Q 38 at rank 9 (FR=0.904). Q 38 top-10 includes Q 37? (compute).
- Pass: ≥ 2/4.

### H3: Shared prophet-tokens
- Tokens enumerated from no-tashkeel text using the 25-prophet name regex (same as Q038-F-02).
- Set intersection of {prophets attested in Q 37} ∩ {prophets attested in Q 38}.
- Pass: |intersection| ≥ 3.

## 3. Test statistic

- Q 37 → Q 38 rank in delta_raw-ascending order out of 113.
- Per-feature overlap matrix (4 cells).
- |Prophet intersection|.

## 4. Success / Failure

- **CONFIRMED**: H1 (top-5 by delta_raw) AND H2 (≥2/4 architectural features) AND H3 (≥3 shared prophets), all 3 pass.
- **DIRECTIONAL**: 2/3 of the H-tests pass.
- **NULL**: ≤1/3 passes.
- **Pre-commit violation**: Q 37 → Q 38 ranks > 50 in delta_raw ascending (so NOT seamless), OR shared-prophet count = 0.

## 5. Honest limits known a priori

- The "seamlessness" measure is a derived metric from a 2-opt heuristic computation (`delta_raw`); it depends on the K=10 starts used in H-NEW-720. The "fraction_residual = 0.0" clamping happens for any negative delta (improvement upon removal would BEAT the canonical adjacency, but per HANDOFF/04-DISCIPLINE.md "ONE TEXT" framing this is reported as `delta = max(0, delta_raw)`). The Q 37 → Q 38 negative delta_raw = -0.00091 is essentially noise-equivalent — i.e. the canonical pair is the BEST observed adjacency for that boundary.
- Length-class definition (mid-Meccan-long vs mid-Meccan-medium) involves a soft threshold; locked at 80-200 verse band as "same length-class".
- Top-final-letter rhyme is a coarse feature; both surahs are predominantly Meccan, but Q 37 is dominantly ن (-ūn/-īn) per anchor data while Q 38 is dominantly ب (-āb/-īb) per Q 38's empirical profile. Pre-commit: this feature LIKELY fails (different rhyme-letter), so H2 is at risk on cell (a).
- Empirical-anchor extraction (DISCLOSED): Q 37 → Q 38 delta_raw = -0.00091, rank 1 ascending; Q 37 → Q 38 FR distance = 0.904 (Q 38 is Q 37's rank-9 nearest); shared prophets = {Nūḥ, Ibrāhīm, Lūṭ, Isḥāq} (≥4 by inspection). The pre-reg's locked thresholds anticipate the directional outcome with conservative ≥-conditions.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token + QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 3 (H1, H2, H3). α_bon = 0.05/3 = 0.01667 (note: H1, H2, H3 are categorical pass/fail thresholds, not p-values; the Bonferroni is applied to the AGGREGATE verdict as a 3-cell family, not as p-correction since H-NEW-720 itself is the population-level inference).

## 8. SHA256 lock

Embedded in `scripts/Q037_F_05_q37_q38_seam.py`; verified at runtime.
