---
surah: 54
test_id: Q054-F-05
title: Q 54 al-Qamar *wa-laqad* opener density — corpus-rank-1 among Meccan surahs
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q054-F-05-walaqad-density
alpha_bon: 0.025
---

# Q054-F-05 — Pre-registration: Q 54 al-Qamar *wa-laqad* opener density test

## 1. Hypothesis (locked before observation)

**H5a (one-tailed, locked direction; absolute density cell):** Q 54 has 11 verses opening with the literal token *wa-laqad* (ولقد) — counted by the regex `^ولقد\s` (verse-initial). **Locked threshold: per-100-verse density of *wa-laqad*-opener verses in Q 54 is corpus rank-1 OR rank-2 across all 114 surahs.**

**H5b (one-tailed, locked direction; refrain-paired-density cell):** Of Q 54's 11 *wa-laqad*-opener verses, ≥ 6 are immediately associated with a refrain-line (either ending in *fahal min muddakir* or being the verse immediately preceding a *yassarnā* or *fa-kayfa kāna ʿadhābī wa-nudhur* refrain). **Locked: ≥ 6/11 *wa-laqad* openings serve refrain-rhythm scaffolding role.**

**H0 (joint):** H5a fails (Q 54 not rank ≤ 2 in *wa-laqad* density per-100-verses) OR H5b fails (< 6/11 refrain-paired).

**Direction:** Q 54 is a *wa-laqad*-opener-saturated surah whose *wa-laqad*s are integrated with its dual-refrain architecture (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **wa-laqad opener regex**: literal verse-initial substring `ولقد ` (with trailing whitespace; verse text starts with this).
- **Per-100-verse density**: count_walaqad_openers / total_verses × 100.
- **Refrain-pair association**: a *wa-laqad* opener is "refrain-paired" if (a) the same verse ends in *fahal min muddakir*, OR (b) the immediately following verse contains *fa-kayfa kāna ʿadhābī wa-nudhur* / *fa-dhūqū ʿadhābī wa-nudhur* / *yassarnā al-Qurʾāna li-l-dhikri*.

## 3. Permutation null

**Null model (length-weighted opener-distribution):** Under the null, the corpus-total *wa-laqad* opener tokens are distributed across surahs proportional to verse-count. p-value (H5a) = probability that a random length-weighted draw places ≥ Q54_count in Q 54.

**Null model (rotation, for H5b):** For each rotation of Q 54's verse-position-vector, recompute number of *wa-laqad* opens that align (within ±1 verse) with refrain-locations. p-value = probability that random rotation produces ≥ 6 refrain-paired *wa-laqad*s.

n_perm = 10000, seed = 20260509.

## 4. Test statistic

- For H5a: per-100-verse-density of *wa-laqad* openers in Q 54 + corpus-rank.
- For H5b: count of refrain-paired *wa-laqad*-openers in Q 54.

## 5. Success / Failure

- **CONFIRMED (joint)**: H5a + H5b both pass at α_bon = 0.025.
- **PARTIAL**: 1 of 2 passes.
- **NULL**: 0 of 2 pass.

## 6. Honest limits known a priori

- **Pre-flight observation**: 11 *wa-laqad*-opener verses in Q 54's 55 verses = 20.0% density. Empirical: 107 corpus-total *wa-laqad*-opener verses (per pre-flight scan). Q 54 holds 11/107 = 10.3% of corpus *wa-laqad* tokens despite being 55/6236 = 0.88% of corpus verses. This is a **~12× over-representation** relative to its verse-share.
- **Verdict ceiling = PASS-DIRECTED**: post-hoc-noticed protocol applies. Independent replication candidate: re-run on alternative orthographic conventions (Uthmani-consonantal); or re-run with the broader *qad* particle (without *wa-l-* prefix) to see if the density-finding generalizes.
- **The *wa-laqad* particle is one of the corpus's strongest **affirmation-frame openers** (al-Suyūṭī *al-Itqān* nawʿ 60 on *al-iʿtirāḍ wa-l-qasam*). The *wa-* + *l-* + *qad* compound functions as a confirmatory + emphatic + perfective opener that classical balāgha treats as the most certainty-saturated affirmation form. Q 54's saturation of this opener correlates with the surah's content (5 destruction-events being affirmed as historical-fact + pre-judgment-day evidence).
- **Refrain-pairing operationalization is the test instrument**: the locked ±1 verse window assumes that the refrain function is local. A wider window (±3 verses) would capture a different fraction of pairings; a stricter window (only the same verse) would dramatically under-count. The ±1 window is the classical-tradition-anchored unit (matching al-Biqāʿī's verse-pair *waṣl* analysis).

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, regex-verse-initial, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (H5a density + H5b refrain-pair). α_bon = 0.025.

## 9. Coordination

No other surah specialist has run a *wa-laqad* density test. No duplication.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q054_F_05_walaqad_density.py`, verified at runtime.
