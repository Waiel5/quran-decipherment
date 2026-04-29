---
id: H-NEW-790
title: "Pre-reg — Per-classical-class iʿjāz-signature comparison"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-730 + cross-finding-026 — iʿjāz signature differs across classical surah-classes
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260447
---

# [[h-new-790-ijaz-by-classical-class|H-NEW-790]] — iʿjāz Signature by Classical Class: Pre-Registration

## 1. Hypothesis

[[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] established window-level iʿjāz signature = z(d̄_rhyme) − z(d̄_content). Per-surah analog: for each surah s in mushaf-position, the iʿjāz-signature of its surrounding K=15 window. Test whether classical surah-categorical attributes (Meccan/Medinan, muqaṭṭaʿāt-opened/not, length-class) systematically align with iʿjāz-signature-magnitude.

## 2. Test design

For each surah s, compute its per-surah iʿjāz-signature as the iʿjāz-signature of the K=15 window centered on s (i.e., window covers Q s-7 to Q s+7, edge-clipped).

Compare iʿjāz-signature distributions across classes:
1. **Meccan vs Medinan** (Welch's t-test, two-sided)
2. **Muqaṭṭaʿāt-opened vs not** (Welch's t-test)
3. **Mufaṣṣal-qiṣār Q 78-114 vs ṭiwāl Q 1-9** (Welch's t-test)
4. **Prophet-named (Yūsuf, Hūd, Ibrāhīm, Yūnus, Maryam, Muḥammad, Nūḥ) vs not** (Welch's t-test)

### Permutation null
Shuffle iʿjāz-signature among 114 surahs (10000 perms, seed 20260447). Empirical p of observed group-mean-differences.

## 3. Pre-committed direction

- Mufaṣṣal-qiṣār ≫ ṭiwāl (since iʿjāz-signature peaks at Q 93-114 per [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]).
- Meccan generally higher than Medinan (since Medinan ṭiwāl in Q 57-66 and post-Medinan are mid-range).
- Muqaṭṭaʿāt may have lower-than-average signature (muqaṭṭaʿāt are scattered in Q 2-46 region).
- Prophet-named direction not pre-committed (mostly Meccan, mostly muqaṭṭaʿāt-opened).

## 4. Pre-committed thresholds

- **STRICT PASS**: 4 tests, Bonferroni-4 α=0.0125 — at least 3 of 4 tests must pass.
- **DIRECTIONAL**: at least 2 of 4 pass at α=0.05.

## 5. Files

- Script: `scripts/h_new_790_ijaz_by_classical_class.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-790.json`
- Findings: `findings/phase-b-hypotheses/h-new-790-ijaz-by-classical-class.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
