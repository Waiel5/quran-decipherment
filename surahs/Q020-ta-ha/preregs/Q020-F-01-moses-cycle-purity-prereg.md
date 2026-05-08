---
finding_id: Q020-F-01
title: Q 20 Ṭā Hā Moses-cycle purity — Moses-narrative-marker fraction is corpus-MAX
date: 2026-05-07
seed: 20260507
phase: B+
specialist: Q020-ta-ha-specialist
test_family: Q020-Q026-Q028 Moses-cycle-purity (joint cross-prophet axis; Q020 lead)
bonferroni_k: 4
bonferroni_family: "Q020-Moses-purity-vs-{Q26,Q28,Q7} comparators (corpus-rank + 3 head-to-head ranks)"
alpha_bon: 0.0125
direction_locked: greater (frac_moses_marker_verses(Q20) > {Q26, Q28, Q7})
status: PRE-REGISTERED
---

# Q020-F-01 — Moses-cycle purity (corpus-MAX rank)

## Hypothesis (direction-locked)

Q 20 Ṭā Hā has a corpus-MAXIMUM fraction of Moses-narrative-marker verses among ALL 114 surahs.

`marker(verse) = TRUE if verse contains ANY of:` (no-tashkeel orthographic match, whole-word boundaries)
- موسى (mūsā) — protagonist
- فرعون (firʿawn) — antagonist
- هارون (hārūn) — brother
- بني اسراءيل / بني إسرائيل (banī isrāʾīl) — ethnos
- السامري (al-sāmirī) — episode-specific antagonist (Q 20 only)
- فرعۥن variants — none.
- العصا / عصا (ʿaṣā with mūsā/her in window — staff)
- اليد / البيضاء (white-hand, in mūsā context)

Definition is fixed BEFORE running on `quran-no-tashkeel.json`.

## Pre-committed thresholds

- **PASS (CONFIRMED)**: Q 20 `frac_moses_marker_verses` is the SINGLE-HIGHEST among all 114 surahs AND ≥ 0.55. Comparator surahs (Q 7 al-Aʿrāf, Q 26 al-Shuʿarāʾ, Q 28 al-Qaṣaṣ) ranks recorded.
- **DIRECTIONAL**: Q 20 ranks 1-3 but < 0.55, OR ranks 1 with frac < 0.55.
- **NULL**: Q 20 ranks > 3.
- **PRE-COMMIT VIOLATION**: Q 20 ranks > 3 AND a comparator surah (Q 7/26/28) ranks #1.

Bonferroni-4 corrected α = 0.0125 for the joint hypothesis (Q20 vs {Q7,Q26,Q28} pairwise + corpus-rank).

## Null model

Permutation null: marker-set is fixed. For each of 10000 permutations, the 135 verses of Q 20 are reassigned to a random 135-verse contiguous window in the full Quran corpus (rotational shift); marker-fraction recomputed. p_perm = fraction of shifted windows with marker-fraction ≥ Q 20 actual.

(Bonferroni multiple-comparison protection at 4 cells; this null is the test's primary p-value.)

## Rules-tuple

`(no-tashkeel, orthographic-token whole-word, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## Honest limits

- Marker set is curated (lexical pattern). A more conservative root-based set (root م-و-س + ف-ر-ع + ه-ر-ن) would yield similar but not identical numbers.
- "banī isrāʾīl" without context could be theological reference rather than narrative; we accept all matches (raises baseline for comparators too).
- Window-length confound: Q 20 is 135 verses; comparators range from 88 (Q 28) to 227 (Q 26). Rank is purity-fraction, length-invariant.
