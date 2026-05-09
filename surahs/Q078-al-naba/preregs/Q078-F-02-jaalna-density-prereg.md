---
surah: 78
test_id: Q078-F-02
title: Q 78 jaʿala (j-ʿ-l) corpus-density rank + wa-jaʿalnā streak test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q078-F-02-jaalna-density
alpha_bon: 0.025
---

# Q078-F-02 — Pre-registration: jaʿala corpus density + consecutive streak

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction):** Q 78 has CORPUS-EXTREME jaʿala-root density per word, ranking in TOP-5 of all surahs ≥50 root-tokens. DIRECTION: top-5.

**H2 (one-tailed, locked direction):** Q 78 has at least one consecutive-verse streak of *wa-jaʿalnā* / *wa-jaʿala* of length ≥3. DIRECTION: streak ≥ 3.

**H0 (joint):** H1 fails (rank > 5) OR H2 fails (no streak ≥3).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **Root distribution**: from `data/morphology/quranic-corpus-morphology-0.4.txt` per surah.
- **jaʿala root**: QAC root code `jEl` (j-ʿ-l).
- **Density**: count(jEl in surah) / total root-tokens(surah).
- **Eligibility filter**: surahs with ≥50 total root-tokens (excludes very-short surahs from rate-comparison).
- **Verse-streak**: regex `وجعلنا|وجعل` matched at the verse level; count maximum consecutive run.

## 3. Test statistic

- H1: q78_rate, q78_rank in eligible-surahs ranked by rate descending.
- H2: q78_max_streak.

## 4. Permutation null

H1 is rank-based (no permutation). H2 is corpus-formula structural (no permutation needed; corpus-EXACT count of surahs with streak ≥3 is the comparator).

α_bon = 0.025.

## 5. Success / Failure

- **CONFIRMED**: both H1 (top-5) AND H2 (streak ≥3) pass.
- **DIRECTIONAL**: only H1 OR only H2 passes.
- **NULL**: neither passes.

## 6. Honest limits known a priori

- Pre-flight observation: q78_rate = 0.0382, rank 2/88 (post-eligibility-filter); max_streak = 3 at vv9-11 (pre-flight observation).
- Per HANDOFF/04-DISCIPLINE.md, single-test α=0.05 cap applies due to post-hoc origin; verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION on a distinct data dimension.
- The "≥50 root-tokens" eligibility-filter is a length-control (excludes short-surah noise). Without the filter, very-short-surahs with 1 jEl token at high rate would dominate.

## 7. Rules-tuple

`(no-tashkeel, QAC-root, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (H1 + H2). α_bon = 0.025.

## 9. Coordination

No prior surah specialist has tested Q 78 jaʿala density. No duplication.

## 10. SHA256 lock

Computed at write-time; embedded into `scripts/Q078_F_02_jaalna_density.py`; verified at runtime.
