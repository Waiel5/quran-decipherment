---
finding_id: Q026-F-05
title: Q 26 verse-length shortness vs corpus baseline and pre-Islamic poetry
date_preregistered: 2026-05-07
phase: B+
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q026-F-01..F-05
alpha_bon: 0.01
acceptance_window: see §6
---

# Q026-F-05 — Q 26 verse-length shortness

## 1. Hypothesis (locked before observation)

**H1.a**: Q 26 has *shorter mean tokens-per-verse* than the corpus mean (one-sided lower-tail; permutation null over 10000 surah-relabelings).

**H1.b**: Q 26's mean-tokens-per-verse signature is **distinct from** pre-Islamic poetry baseline (al-Muʿallaqāt) — the Quran's anti-poetry coda asserts a genre distinction that should hold under length statistics.

**H0**: Q 26 mean-tokens-per-verse is corpus-mean ± noise; H1.b: Q 26 indistinguishable from poetry.

## 2. Operational definition

- `mean_tpv(Q 26)` = total tokens / total verses (no-tashkeel orthographic, ws-split).
- Corpus baseline: `corpus_mean_tpv` = total Quran tokens / 6236 verses.
- Pre-Islamic poetry baseline: `poetry_mean_tpv` from the 7 al-Muʿallaqāt — proxy "verse" = a hemistich (since classical verse ≈ 2 hemistichs but tokens-per-hemistich is a closer comparable to Quran-verse). Baseline data: `/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-*.txt` and `baseline-stats.csv`.
- For poetry baseline we use the file-level token counts and divide by visible-line count.

## 3. Test statistic

- `rank_q26_tpv` among 114 surahs (1 = shortest).
- `z_q26_corpus` = (mean_tpv(Q26) − corpus_mean) / SD_per_surah.
- `z_q26_poetry` = (mean_tpv(Q26) − poetry_mean) / poetry_SD.

## 4. Direction (LOCKED)

- H1.a: rank_q26 in bottom 50% (rank ≤ 57) AND z_q26_corpus < 0.
- H1.b: |z_q26_poetry| > 0; direction **POETRY-LONGER** (Q 26 SHORTER than poetry).

## 5. Permutation null (for H1.a)

Seed 20260507; 10000 perms shuffling surah-token-counts to surah-verse-counts; count #(perm-rank ≤ obs-rank); p_perm.

For H1.b: the al-Muʿallaqāt are 7 fixed corpora; we compute the 7-mean and 7-SD; one-sample z (Q 26 vs poetry mean).

## 6. Acceptance

- **CONFIRMED** = both H1.a (rank ≤ 57) AND H1.b (|z| > 1.0 in committed direction).
- **DIRECTIONAL** = one of the two passes.
- **NULL** = neither passes.
- **PRE-COMMIT VIOLATION** = rank > 90 (Q 26 LONGER than corpus median) — flag.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token-ws-split, no-pause-marker-strip, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Anti-hallucination

Files: `quran-text/quran-no-tashkeel.json`, `data/baseline-corpora/baseline-stats.csv`, `data/baseline-corpora/raw/muallaqa-*.txt`.

## 9. Honest a-priori limits

- Classical Arabic poetry (qaṣīda) has fixed metrical line-length; the al-Muʿallaqāt are extreme cases of long monorhyme verses. Q 26's coda contains the explicit anti-poetry stance (vv 224-227); the empirical test is whether the genre-claim is operationally cashable as a length-distribution distinction.
- "Hemistich" vs "full bayt" is a non-trivial choice; we compute both and document the more conservative.
- A short mean-tpv for Q 26 also matches the H-NEW-770 verse-length compression-tail: but Q 26 is at s=26 (head zone), so the tail-law predicts MEDIUM mean-tpv. Q 26 being SHORTER than the s=26 predicted value would be a tail-law deviation — a separate insight from §3.1.
- Verse-counts include the muqaṭṭaʿ "ṭسم" verse 1 (length 1 token). This deflates the surah-mean. We report both with-v1 and without-v1.
