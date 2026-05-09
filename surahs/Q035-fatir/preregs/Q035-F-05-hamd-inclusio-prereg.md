---
surah: 35
test_id: Q035-F-05
title: Q 35 within-surah al-ḥamdu li-llāh inclusio — v.1 ↔ v.34 dual-anchor test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q035-F-05-hamd-inclusio
alpha_bon: 0.025
---

# Q035-F-05 — Pre-registration: Q 35 within-surah al-ḥamdu inclusio test

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction):** Q 35 contains EXACTLY 2 instances of *al-ḥamdu li-llāh* (الحمد لله) in surface-form — v.1 (cosmological-frame) and v.34 (paradise-dwellers' exclamation). This pair-count is **structurally rare** in the corpus.

**H2 (one-tailed, locked direction):** Among surahs with ≥2 *al-ḥamdu li-llāh* surface-form occurrences, Q 35 is in the **TOP-5 by count** of within-surah ḥamd repetition.

**H0 (joint):** there are ≥3 surahs with 2+ al-ḥamdu li-llāh occurrences AND Q 35 is not in the top-5.

**Direction:** Q 35 is structurally rare in the corpus for within-surah al-ḥamd duality (H1 + H2).

## 2. Operational definition

- **Source**: `quran-text/quran-no-tashkeel.json`.
- **Phrase**: regex `\bالحمد لله\b` (al-ḥamdu li-llāh, surface-form).
- **Count per surah**: total occurrences across all verses in each surah.

## 3. Test statistic

- n_q35_hamd = count of *al-ḥamdu li-llāh* in Q 35 (expected = 2: v.1, v.34).
- corpus_distribution = {surah: count_of_al_ḥamd_li_llāh}.
- top5 = top-5 surahs by within-surah al-ḥamd count.

## 4. Permutation null

For H1: report exact count and verse-locations.

For H2: rank Q 35 in the corpus-wide distribution. Assumed: most surahs have 0; a few have 1 (the 5 al-ḥamd openers); only a few have 2+. Q 35 in top-5 implies structural rarity.

## 5. Success / Failure

- **CONFIRMED**: n_q35_hamd ≥ 2 AND Q 35 is in TOP-5 by count.
- **DIRECTIONAL**: H1 passes alone.
- **NULL**: n_q35_hamd < 2.
- **Pre-commit violation**: n_q35_hamd = 1 (only one occurrence, contradicting brief observation of v.1 + v.34).

## 6. Honest limits known a priori

- **Pre-flight observation**: at session start I empirically observed n_q35_hamd = 2 (v.1 + v.34). Per HANDOFF/04-DISCIPLINE.md, post-hoc origin disclosed: verdict ceiling = **PASS-DIRECTED** until INDEPENDENT REPLICATION on a distinct data dimension.
- **Other surahs with multiple al-ḥamdu li-llāh**: possible candidates include Q 6 al-Anʿām (opens with it; may have additional internal occurrences), Q 18 al-Kahf (opens; may have additional). The test will reveal the corpus distribution.
- **Inclusio reading**: the v.1 al-ḥamd is divine-cosmic-attribute frame; the v.34 al-ḥamd is paradise-dwellers' exclamation. The two anchors form a within-surah inclusio bracketing the ENTIRE eschatological argument. This is the architectural significance.
- **Independent replication**: would require testing OTHER al-ḥamd-anchored surahs for similar within-surah duality patterns. The Q 35 case is uniquely structurally interpretable because the v.34 occurrence is dramatized speech-act of the saved.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (H1 + H2). α_bon = 0.025.

## 9. Coordination

This test is unique to Q 35.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q035_F_05_hamd_inclusio.py`, verified at runtime.
