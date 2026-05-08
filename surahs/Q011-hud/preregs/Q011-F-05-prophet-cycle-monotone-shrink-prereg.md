---
surah: 11
test_id: Q011-F-05
title: Q 11 prophet-narrative-block monotone shrinkage with cycle-index
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_family: Q011-F-05
bonferroni_k: 1
alpha_bon: 0.05
n_perm: 10000
---

# Q011-F-05 — Pre-registration: Q 11 prophet-cycle compression

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, direction LOCKED):** Within Q 11's 7 prophet-narrative blocks,
the **per-block verse-count shrinks monotonically** with cycle-index
(Spearman ρ < 0 between cycle-index and verse-count). This is a within-surah
analog of the H-NEW-660 corpus-wide compression-tail law and the
Q026-F-01-style intra-surah-compression observation.

**H0:** Spearman ρ ≥ 0 (no shrinkage, or growth) within Q 11.

**Direction:** ρ NEGATIVE (LOCKED) — earlier blocks longer, later blocks shorter.

## 2. Operational definition

- **Q 11 prophet-blocks** (cycle-index 1..7), bounds locked from
  `surahs/Q011-hud/00-overview.md` §8 and inherited from H-NEW-270 prereg
  + al-Biqāʿī's *Naẓm al-Durar* segmentation:

  | Cycle-index | Prophet | Verses |
  |:--:|:--:|:--:|
  | 1 | Nūḥ | 25–49 (25 vv) |
  | 2 | Hūd | 50–60 (11 vv) |
  | 3 | Ṣāliḥ | 61–68 (8 vv) |
  | 4 | Ibrāhīm + Lūṭ joint | 69–83 (15 vv) |
  | 5 | Shuʿayb | 84–95 (12 vv) |
  | 6 | Mūsā compressed | 96–99 (4 vv) |
  | 7 | Pedagogical refrain (post-cycle) | 100–108 (9 vv) |

  Note: the Q 11 sequence has 7 distinct destruction-pericope blocks, NOT
  7 distinct prophets — Ibrāhīm and Lūṭ are jointly indexed as block-4 per
  al-Biqāʿī's segmentation (Lūṭ's people are introduced via the angels' visit
  to Ibrāhīm). The 7th block is the pedagogical-refrain coda treated as the
  cycle-coda.

- **Test**: Spearman ρ between cycle-index (1..7) and verse-count (25, 11, 8,
  15, 12, 4, 9).
- **Permutation null**: 10,000 random orderings of the 7 verse-counts
  assigned to cycle-index 1..7; Spearman ρ_perm computed under each;
  p_lower = fraction of perms with ρ_perm ≤ ρ_obs.
- Seed 20260507.

## 3. Test statistic

Spearman ρ. Permutation p (one-tailed lower).

## 4. Success / Failure

| Outcome | Verdict |
|:--|:--|
| ρ ≤ −0.6 AND p ≤ 0.05 | **CONFIRMED** |
| ρ < 0 AND 0.05 < p ≤ 0.15 | DIRECTIONAL |
| ρ ≥ 0 OR p > 0.15 | NULL |
| ρ strongly POSITIVE (p ≥ 0.95) | Pre-commit violation; NULL with full prominence |

## 5. Bonferroni context

- 1 cell. α=0.05.
- Independent test, no family k>1.

## 6. Honest limits known a priori

- N=7 ordered points: Spearman test has limited power; under perfect
  monotone shrinkage ρ = −1, perm p ≈ 1/5040 ≈ 0.0002.
- Block-bound choices: the {Ibrāhīm + Lūṭ joint} block-4 vs {Ibrāhīm alone +
  Lūṭ alone} as separate blocks-4-and-5 is an analytical choice. Under
  separate-blocks (8-block split), the boundary 69-77 (Ibrāhīm) at 9 vv and
  78-83 (Lūṭ) at 6 vv shifts the cycle-index sequence. The pre-locked
  segmentation is the al-Biqāʿī-anchored 7-block version.
- The 7th block (pedagogical-refrain) is **not a prophet narrative** — its
  inclusion as cycle-end coda is a substantive choice. Excluded version
  (6-block): N=6, ρ_perm-distribution narrower; this is queued as a
  rules-tuple-sensitivity follow-up. Q011-F-05 locks the 7-block version
  (with coda) as the primary test.

## 7. Rules-tuple

`(no-tashkeel, verse-count, al-Biqāʿī-anchored-block-bounds, 7-block-with-coda, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. SHA256 lock

Computed at run-time. Embedded in `scripts/Q011_F_05_prophet_cycle_monotone_shrink.py`.
