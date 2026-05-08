---
test_id: Q047-F-01
title: "Muḥammad-naming density — Q 47:2 vs the 4 corpus Muhammad-named contexts"
date_locked: 2026-05-08
seed: 20260508
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q047-F-01-muhammad-naming
alpha_bon: 0.05
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q032-Q047-retry-specialist
parent_findings:
  - h-new-111 (FR distance matrix)
classical_anchors:
  - al-Suyūṭī, *al-Itqān*, nawʿ 17 (asmāʾ al-Nabī in the Qur'ān)
  - Ibn Kathīr, *Tafsīr*, on Q 47:1-2 (the surah named for the Prophet)
---

# Q047-F-01 Pre-registration — Muḥammad-naming density

## Hypothesis

The proper name "Muḥammad" appears in the Qur'ān 4 times (verified on disk):
- Q 3:144 (Uḥud retreat: Muḥammad as one prophet among many)
- Q 33:40 (the seal of the prophets)
- Q 47:2 (those who believe in what was sent down upon Muḥammad)
- Q 48:29 (Muḥammad rasūl Allāh; description of the believers around him)

"Aḥmad" (alternate name, per Q 61:6 prophecy from ʿĪsā) appears 1 time.

**Hypothesis**: The Muḥammad-naming density (occurrences per 1000 words) of Q 47 is the HIGHEST among the 4 Muhammad-naming surahs (Q 3, Q 33, Q 47, Q 48), reflecting that Q 47 is THE Muḥammad-surah (named after him).

Pre-disclosure: each surah has exactly 1 Muhammad-naming. So density depends only on surah word-count. Q 47 (~538 words) is shorter than Q 3 (~3500), Q 33 (~1280), Q 48 (~560), so Q 47 will likely have a HIGH density per-1000-words — but possibly tied with Q 48 which is similar length.

## Pre-committed prediction (DIRECTION LOCKED)

**Direction-locked**: density(Muḥammad in Q 47) > density(Muḥammad in {Q 3, Q 33, Q 48}) — Q 47 ranks #1 among the 4 Muhammad-naming surahs by per-1000-word density.

## Test (Bonferroni-1)

**T1**: density_47 > density_3, density_33, density_48 (strict greater).

Permutation null: among all 114 surahs, what is the empirical CDF of (1 / surah_word_count) × 1000 for surahs with 1 Muhammad-mention? Q 47 must be in the top of the 4-surah comparison set.

α = 0.05 (single test).

## Direction-of-effect lock

Predicted: Q 47 density > all other 3.
If Q 47 is not strictly #1: NULL.

## Success criteria

- VINDICATED: Q 47 strictly #1 in the 4-surah set.
- DIRECTIONAL: Q 47 in top-2.
- NULL: Q 47 not in top-2.

## Garden-of-forking-paths log

- BEFORE running: chose density per 1000 words (not per verse) because verse lengths differ widely.
- BEFORE running: chose strict #1 prediction because Q 47 is *named* for Muḥammad — it should not just be "high" but be THE highest.
- ACKNOWLEDGED ALTERNATIVE: Q 48 is similar length and also has Muhammad rasūl Allāh — the test may produce Q 47 ≈ Q 48 (a near-tie), which would be DIRECTIONAL not VINDICATED.
- BEFORE running: this is technically a deterministic test (1 occurrence each, density depends only on word-count), so the "permutation" is more about the CDF rank.
