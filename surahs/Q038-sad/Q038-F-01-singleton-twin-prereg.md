---
surah: 38
test_id: Q038-F-01
title: Singleton-letter twin pair — Q 38:1 (ص + oath-by-Quran) and Q 50:1 (ق + oath-by-Quran) structural-similarity test
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 3
bonferroni_family: Q038-F-01-singleton-twin-similarity
alpha_bon: 0.01667
---

# Q038-F-01 — Pre-registration: singleton-letter twin pair Q 38:1 and Q 50:1

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** The two opening verses Q 38:1 *ṣ wa-l-Qurʾāni dhī al-dhikr* and Q 50:1 *q wa-l-Qurʾāni al-majīd* are structurally maximal-similarity twins within the corpus on at least one of three locked similarity metrics. They are the only two corpus verses that combine (a) a single-letter muqaṭṭaʿ, (b) immediately followed by an oath swearing by the Qurʾān. The structural twinning predicts elevated pairwise similarity vs. all other corpus verse-pairs.

**H0:** The Q 38:1 ↔ Q 50:1 similarity is no higher than the corpus-wide pairwise verse-similarity null on any metric.

**Direction:** Q 38:1 ↔ Q 50:1 similarity > 99th percentile of all corpus verse-pair similarities, on at least one of three pre-locked metrics (LOCKED).

## 2. Operational definition

**Three similarity metrics (Bonferroni-3, family `Q038-F-01-singleton-twin-similarity`):**

1. **Token-bag cosine** — token-set Jaccard on whitespace-tokenized no-tashkeel verse text after stripping the muqaṭṭaʿ letter itself (keeping only the body of the verse: *wa-l-Qurʾāni dhī al-dhikr* / *wa-l-Qurʾāni al-majīd*).

2. **Root-bag cosine** — QAC v0.4 root tokens after the muqaṭṭaʿ; cosine on root-occurrence vector.

3. **Character 4-gram NCD** — normalized compression distance via zlib on the no-tashkeel verse-body (excluding the muqaṭṭaʿ letter).

**Sample space**: every Quranic verse stripped to its body. For the two target verses Q 38:1 and Q 50:1, the body excludes the leading single-letter muqaṭṭaʿ.

## 3. Test statistic

For each of the three metrics:
- Compute pairwise distance/similarity for all pairs of verses where BOTH have ≥3 tokens after stripping muqaṭṭaʿāt (to avoid degenerate small-N noise on metric-1 and metric-2).
- Compute Q 38:1 ↔ Q 50:1 metric value.
- Compute permutation-rank percentile.
- Pass condition (per metric): Q 38:1 ↔ Q 50:1 is in the **top 1%** of corpus pairs on that metric.

## 4. Success / Failure

- **Strict success (CONFIRMED)**: ≥1 of 3 metrics passes after Bonferroni-3 (α_bon = 0.01667), AND the pair appears in the top-3 of all corpus pairs on at least one metric.
- **Directional**: Q 38:1 ↔ Q 50:1 is in top 5% on at least one metric, but not top 1%.
- **NULL**: Q 38:1 ↔ Q 50:1 lies below the 95th-percentile on all 3 metrics.
- **Pre-commit violation**: Q 38:1 ↔ Q 50:1 is BELOW corpus-mean similarity on all 3 metrics (would falsify the structural-twin hypothesis).

## 5. Honest limits known a priori

- Both verses are short (4 tokens after muqaṭṭaʿ for Q 38:1, 3 tokens for Q 50:1). Short verses produce noisy cosine values; the Bonferroni-3 family aggregates 3 metrics to control for instrument noise.
- The shared root q-r-ʾ (al-Qurʾān) is a high-frequency root, so the elevated similarity could be partly a corpus-prevalent-root artifact. The instrument controls for this by computing percentile rank in the corpus-pairwise distribution, not absolute similarity.
- Q 36:2 and Q 43:2 also begin with *wa-l-Qurʾāni*-oath but in second-position after a muqaṭṭaʿ in v.1 (YS / HM). These are structural-cousins, not twins, since the oath occupies a separate verse from the muqaṭṭaʿ.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token + QAC root, char-4-gram-NCD, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Coordination with Q050-qaf

This test is the Q 38 specialist's complementary half of the Q 38:1/Q 50:1 twin analysis. The Q 050-qaf specialist (Q050-F-01) is expected to run a parallel/complementary test. To avoid duplication: this test is locked to **3 specific similarity metrics applied verse-pair-by-corpus-percentile**. The Q 050 test should focus on a different operationalization (e.g., classical-claim audit of the *qasamīyāt iftitāḥīya* tradition, or different feature-space).

## 8. SHA256 lock

To be computed at run-time. Embedded in `scripts/Q038_F_01_singleton_twin.py`.
