---
surah: 1
test_id: Q001-F-03
file_type: novel-finding
date_locked: 2026-04-28
date_run: 2026-04-28
verdict: NULL
prereg_sha: 55bfd37747f5db86a1af15e854dab28eaab67563d8c3bc17c83f21c28e94fa1e
---

# Q001-F-03 — Q 1 rhyme-entropy vs short-surah baseline

## 1. Pre-registered hypothesis (two-tailed)

Q 1's rhyme-entropy (0.683 nats) is materially different from the short-surah corpus distribution.

Pre-reg: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/Q001-F-03-rhyme-entropy-vs-7-verse-prereg.md`

## 2. Result

| Statistic | Value |
|:--|--:|
| Q 1 rhyme entropy | 0.6829 nats |
| Set A (n_verses ≤ 10), excl Q 1 | 18 surahs |
| Mean | 0.4450 |
| Population SD | 0.4467 |
| z (Q 1) | +0.533 |
| Permutation p (two-tailed) | 0.79 |

**Verdict: NULL.** Q 1's rhyme entropy is well within the short-surah distribution. The high standard deviation (0.45) reflects the bimodality of short-surah rhyme — some short surahs are rhyme-monotonic (entropy ≈ 0), others are mid-entropy. Q 1 is mid.

## 3. Set B — exact 7-verse comparison

| Surah | Rhyme entropy |
|:--|--:|
| Q 1 al-Fātiḥa | 0.6829 |
| Q 107 al-Māʿūn | 0.4101 |

Only TWO surahs in the entire mushaf have exactly 7 verses (Hafs-Kufan): Q 1 and Q 107. Comparison is descriptive only — N=2 is below any inferential threshold.

That said, it is interesting: Q 1 is rhyme-richer (more entropy) than its only verse-count twin. The two are also thematically opposite — Q 1 is the prayer of every prayer; Q 107 is the rebuke of those who fail to pray ("Have you seen the one who denies the Recompense? That is the one who repulses the orphan…"). This is a striking thematic mirror at the verse-count = 7 level, but no statistical claim is supported.

## 4. Honest limits

- Set A baseline (n ≤ 10) is somewhat arbitrary; pre-registered.
- The set is dominated by Q 87-114 mufaṣṣal-qiṣār surahs, where rhyme is the ARCHITECTURAL primary axis. Q 1's rhyme-entropy lying in this distribution doesn't isolate Q 1; it tells us Q 1 BEHAVES PHONOLOGICALLY like a mufaṣṣal-qiṣār surah, not like a long ṭiwāl surah.
- This connects with the H-NEW-840 observation that Q 1's UAS-rank is 2 partly because of its outlier-strength in CONTENT (low mean-distance to corpus), not its rhyme-distinctness. Rhyme is not where Q 1's distinctiveness sits.

## 5. Cross-references

- Empirical profile says Q 1 has rhyme entropy 0.683 (rank-z within short surahs ≈ +0.5 — middle).
- The distinctiveness of Q 1 is in CONTENT-cohesion (mean_content_distance = 0.7789, rank-4 most central), NOT in rhyme.
- This empirically separates the two iʿjāz axes for Q 1 specifically: Q 1 is **structurally distinctive** (UAS rank 2) and **content-central** (rank 4), but **phonologically typical** of short surahs. The al-Bāqillānī *iʿjāz al-fawāṣil* claim does not particularly distinguish Q 1.

## 6. Output files

- Script: `/Users/grey/Downloads/quran/scripts/Q001_F_03_rhyme_entropy_short.py`
- JSON: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/csv/Q001-F-03.json`
- Pre-reg: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/Q001-F-03-rhyme-entropy-vs-7-verse-prereg.md`
