---
surah: 30
test_id: Q030-F-05
title: Q 30 cognitive-imperative interrogative density (afa-lā tatafakkarūn / taʿqilūn)
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 1
alpha_bon: 0.05
hypothesis_anchor: al-Rāzī (*Mafātīḥ al-ghayb* on Q 30 — recurrent *afalā tatafakkarūn / āyāt li-l-mutaffakkirīn / āyāt li-l-ʿālimīn*)
verdict_ceiling: PASS-DIRECTED
---

# Q030-F-05 — Pre-registration: Q 30 cognitive-imperative density

## 1. Hypothesis (LOCKED before observation)

**H1:** Q 30's per-word density of cognitive-imperative interrogatives + cognitive-verb forms (frozen marker set below) ranks in the **TOP 3 surahs corpus-wide**.

**H0:** Q 30 ranks below top-3.

**Direction:** Q 30 in top-3 (LOCKED).

## 2. Operational definition (frozen marker set)

Surface-form regex (no-tashkeel text), word-boundary matched:
- Cognitive interrogatives: `أفلا يتفكرون`, `أفلا تتفكرون`, `أفلا يعقلون`, `أفلا تعقلون`, `أفلا يسمعون`, `أفلا تسمعون`, `أفلا يبصرون`, `أفلا تبصرون`, `أفلا ينظرون`, `أفلا تنظرون`
- Cognitive verb forms (3rd person + 2nd person plural): `يتفكرون`, `تتفكرون`, `يعقلون`, `تعقلون`
- Negated cognitive: `لا يعقلون`, `لا يتفكرون`

Per-surah:
- `cog_count` = total regex matches across all verses.
- `cog_rate` = cog_count / total_words.

## 3. Test statistic

- **Primary**: rank of Q 30's `cog_rate` in 114-surah list. Pass = rank ≤ 3.
- **Secondary** (descriptive only, not part of pass/fail): rank of Q 30's absolute `cog_count`.

## 4. Bonferroni

k=1. α=0.05. For the primary rank-statistic, achieving rank ≤ 3 / 114 under uniform-null has p = 3/114 ≈ 0.026.

## 5. Success / Failure

| Outcome | Verdict |
|:--|:--|
| Q 30 rank ≤ 3 / 114 | **PASS-DIRECTED** |
| Q 30 rank 4-10 / 114 | **DIRECTIONAL** |
| Q 30 rank > 10 | **NULL** |

## 6. Rules-tuple

`(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, hafs-kufan, mashriqi)`.

## 7. SHA256 lock

Embedded in `scripts/Q030_F_05_cognitive_imperatives.py`.

## 8. Honest a-priori limits

- Marker-set is curated; biased toward forms that appear frequently in late-Meccan rhetorical contexts. Other "cognitive" markers (`مذكرون`, `يفقهون`, `يعتبرون`) are deliberately excluded to keep the set tight; an expanded set is a follow-up question.
- Tiny short surahs (Q 88, Q 100) can dominate the rate-rank by accident of small-denominator. The ranks of these surahs are reported transparently.
- Q 30's claim is the iʿjāz al-ghayb pericope (Q 30:2-5) PLUS recurrent cognitive-imperative interjections; this test addresses ONLY the cognitive-imperative half.
