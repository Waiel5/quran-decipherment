---
surah: 54
test_id: Q054-F-02
title: Q 54 al-Qamar prophet-cycle compression vs Q 26 al-Shuʿarāʾ — verses-per-prophet + words-per-prophet null comparison
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q054-F-02-prophet-cycle-compression
alpha_bon: 0.025
---

# Q054-F-02 — Pre-registration: Q 54 vs Q 26 prophet-cycle compression test

## 1. Hypothesis (locked before observation)

**H2a (one-tailed, locked direction; verses-per-pericope cell):** Q 54's mean-verses-per-pericope across its 5 prophet/nation pericopes (Nūḥ vv 9-17, ʿĀd vv 18-22, Thamūd vv 23-32, Lūṭ vv 33-40, āl-Firʿawn vv 41-42) is strictly lower than Q 26 al-Shuʿarāʾ's mean-verses-per-pericope across its 7 prophet pericopes (Mūsā vv 10-68, Ibrāhīm vv 69-104, Nūḥ vv 105-122, Hūd vv 123-140, Ṣāliḥ vv 141-159, Lūṭ vv 160-175, Shuʿayb vv 176-191). **Locked threshold: compression ratio ≥ 2 (i.e., Q 26 mean verses-per-pericope ≥ 2× Q 54 mean).**

**H2b (one-tailed, locked direction; words-per-pericope cell):** Q 54's mean-words-per-pericope is strictly lower than Q 26's, with **locked compression ratio ≥ 2**.

**H0 (joint):** H2a ratio < 2 OR H2b ratio < 2.

**Direction:** Q 54 is structurally MORE compressed than Q 26 by both verse-count and word-count metrics, by ≥ 2× (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **Pericope boundaries** (pre-committed, classical-tradition-anchored, locked here):
  - **Q 54 pericopes** (al-Ṭabarī + al-Rāzī + al-Biqāʿī standard sectioning):
    - Nūḥ: vv 9-17 (9 verses)
    - ʿĀd: vv 18-22 (5 verses)
    - Thamūd: vv 23-32 (10 verses)
    - Lūṭ: vv 33-40 (8 verses)
    - āl-Firʿawn: vv 41-42 (2 verses)
  - **Q 26 pericopes** (al-Ṭabarī + Ibn Kathīr + al-Biqāʿī standard sectioning):
    - Mūsā: vv 10-68 (59 verses)
    - Ibrāhīm: vv 69-104 (36 verses)
    - Nūḥ: vv 105-122 (18 verses)
    - Hūd: vv 123-140 (18 verses)
    - Ṣāliḥ: vv 141-159 (19 verses)
    - Lūṭ: vv 160-175 (16 verses)
    - Shuʿayb: vv 176-191 (16 verses)
- **Verse-count per pericope**: hi - lo + 1.
- **Word-count per pericope**: sum of len(text.split()) over verses lo..hi inclusive (no-tashkeel orthographic tokens; basmala counted only in Q 1).
- **Compression ratio**: Q26_mean / Q54_mean (≥2 is the locked bar).

## 3. Permutation null

**Null model (between-surah resampling):** For each surah, randomly partition its prophet-pericope verse-range (i.e., the union of all pericope-verses in that surah) into a number of contiguous blocks equal to its actual pericope count, then compute mean-verses-per-block and mean-words-per-block under random partition. Compute the ratio Q26_perm_mean / Q54_perm_mean over 10,000 random-partition trials. p-value = probability that random partitions produce a compression ratio ≥ observed.

This null tests whether the OBSERVED 5-vs-7 pericope-count + the OBSERVED total verse/word totals (Q 54: 34 verses across 5 pericopes; Q 26: 182 verses across 7 pericopes) is sufficient to produce the observed compression ratio under random partition, vs. whether the actual classical-tradition-pericope boundaries are uniquely-compressed in Q 54.

n_perm = 10000, seed = 20260509.

## 4. Test statistic

- ratio_v = mean_verses_q26 / mean_verses_q54.
- ratio_w = mean_words_q26 / mean_words_q54.

## 5. Success / Failure

- **CONFIRMED (joint)**: H2a + H2b both pass at α_bon = 0.025.
- **PARTIAL**: 1 of 2 passes.
- **NULL**: 0 of 2 pass.
- **PRE-COMMIT VIOLATION**: ratio < 1 in either cell (i.e., Q 54 LESS compressed than Q 26).

## 6. Honest limits known a priori

- **The pericope-boundary specification IS the test instrument**. Alternative pericope-boundary specifications (e.g., narrowing Q 26 Mūsā to vv 16-68 by excluding the framing prologue) would shift the ratio. The pre-committed boundaries follow al-Ṭabarī + al-Rāzī + al-Biqāʿī classical sectioning, which is the dominant tradition. A sensitivity check using al-Suyūṭī's *al-Itqān* nawʿ 13 (*al-aḥkām al-mansūkha*) sectioning is exploratory-secondary.
- **Q 26 has 7 pericopes; Q 54 has 5 pericopes**. The DIFFERENT pericope-COUNT itself is part of the architectural signature being tested. The compression test isolates **mean per-pericope size** — not total surah size. This makes Q 26's 227-verse vs Q 54's 55-verse asymmetry an INPUT to the compression metric, not a confound.
- **The brief frames Q 26 as the "parallel prophet-cycle"** comparator. This is empirically supported: H-NEW-1230 lists Q 26 as one of 5 refrain-bearing surahs alongside Q 54; Q 26's *wa-inna rabbaka la-huwa al-ʿAzīz al-Raḥīm* refrain is its closing-pericope-marker analogous to Q 54's *fahal min muddakir* + *kayfa kāna ʿadhābī wa-nudhur* dual marker.
- **Verdict ceiling = PASS-DIRECTED**: post-hoc anchor-extraction observed Q 54 mean ≈ 6.8 vs Q 26 mean ≈ 26.0 (compression ratio ≈ 3.8) before pre-reg lock. Per HANDOFF/04-DISCIPLINE.md, single-test α=0.05 cap; PASS-DIRECTED until INDEPENDENT REPLICATION (e.g., word-count or letter-count basis as separate operationalization).

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, classical-tradition-pericope-boundaries, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (H2a verse-count + H2b word-count). α_bon = 0.025.

## 9. Coordination

Q 26 specialist file does not yet exist. No coordination conflict; this is a Q 54-anchored cross-surah comparison.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q054_F_02_prophet_cycle_compression.py`, verified at runtime.
