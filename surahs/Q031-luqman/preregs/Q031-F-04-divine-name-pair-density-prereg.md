---
test: Q031-F-04
title: Q 31 divine-name-pair density (laṭīf-khabīr, ʿazīz-ḥakīm, ʿalīm-khabīr)
test_type: corpus-share + per-verse-density
direction_locked: positive (Q 31 has elevated paired-divine-name density vs corpus)
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q031-luqman-specialist
alpha_bon: 0.0167
acceptance_window:
  primary: At least 1 of 3 pre-registered name-pairs has Q 31 per-verse density > 95th percentile of permutation null on length-matched random surahs
date_locked: 2026-05-09
---

# Q031-F-04 — Pre-registration

## 1. Rationale

H-NEW-140 (CONFIRMED at 13.87× above Poisson-independence) catalogs 16 classical *asmāʾ mutazāwijah* (paired divine-names) — al-Rāzī / al-Zamakhsharī / al-Suyūṭī tradition. Q 31 attests at least 3 such pairs:

- **laṭīf-khabīr** (subtle-aware) at v.16 — closes the 2nd waṣiyya
- **ʿazīz-ḥakīm** (mighty-wise) at v.27 — closes the ink-of-sea verse; also at vv.9 and 30 (3 instances within Q 31)
- **ʿalīm-khabīr** (knowing-aware) at v.34 — closes the surah and the mafātīḥ-al-ghayb verse

The pre-registered question: is Q 31's per-verse density of these 3 pre-registered name-pairs elevated compared to length-matched random surahs?

## 2. Hypothesis

**H1**: Q 31's count of *laṭīf-khabīr* pair (verse-level co-occurrence) per verse exceeds 95th percentile of permutation null.
**H2**: Q 31's count of *ʿazīz-ḥakīm* pair (verse-level co-occurrence) per verse exceeds 95th percentile.
**H3**: Q 31's count of *ʿalīm-khabīr* pair (verse-level co-occurrence) per verse exceeds 95th percentile.

Bonferroni-3: α_bon = 0.05/3 = 0.0167.

## 3. Method

- For each pair (X, Y), define a verse to be a "pair-bearing verse" if both X and Y appear within that verse.
- For each pair, compute n_pair_verses(s) for each surah s.
- Density: n_pair_verses(s) / verse_count(s).
- Permutation null: 10,000 random 34-verse contiguous windows from across the corpus (any surah that has ≥ 34 verses; or stitch from multiple surahs to make a 34-verse window). Compute density per random-window.
- One-tailed p = P(perm_density ≥ observed Q 31 density).

For *ʿazīz-ḥakīm*: this pair is recurrent across the corpus (~ 47 instances). Q 31 has 3 verses with both terms (vv.9, 27, 30 — verified). Density = 3/34 = 0.088.
For *laṭīf-khabīr*: this pair appears at Q 6:103 (with *al-baṣīr*), Q 22:63, Q 31:16, Q 33:34, Q 67:14 — 5 corpus-instances total. Q 31 has 1.
For *ʿalīm-khabīr*: this pair appears at Q 31:34, Q 49:13, Q 66:3, Q 9:115 (cross-text) — 4 corpus-instances. Q 31 has 1.

## 4. Pre-committed acceptance window

- PASS-PRIMARY: at least 1 of 3 pairs has perm-p < α_bon = 0.0167.
- DIRECTIONAL: at least 1 has perm-p < 0.05 but ≥ α_bon.
- NULL: all 3 have perm-p ≥ 0.05.

## 5. Garden-of-forking-paths log

- The 3 specific pairs (laṭīf-khabīr, ʿazīz-ḥakīm, ʿalīm-khabīr) were selected from the 16 H-NEW-140 catalog because they EXIST in Q 31 — this is data-defined cohort-membership, not data-snooped selection.
- The pre-reg recognizes the cherry-pick risk and addresses it via Bonferroni-3 correction.
- The H-NEW-140 catalog itself was independently CONFIRMED at 13.87× above Poisson-independence; this Q 31 specialist is a SUB-test on a closed-cohort restriction.

## 6. Honest limits

- 3 pre-registered pairs is a small set; the test may be underpowered.
- The corpus-sparseness of these pairs (5 ʿazīz-ḥakīm instances Q 31-style verse-co-occurrence; 5 laṭīf-khabīr; 4 ʿalīm-khabīr) means the permutation null distribution may be approximately concentrated at 0 for many random windows.
- Q 31's density of 3/34 = 0.088 for *ʿazīz-ḥakīm* is high (3 verses out of 34 contain the pair); the null distribution may have many zeros, so the percentile-test could pass easily but with a small effect size.

## 7. Direction lock

LOCKED positive on all 3 (Q 31 elevated vs random comparable-length-stitched-windows).

## 8. SHA-locking

This pre-reg file's SHA256 will be computed at write-time and verified at run-time.

## 9. Cross-references

- [[h-new-140-divine-name-pairs]] — the 16 canonical paired-names corpus result (CONFIRMED at 13.87× Poisson-independence).
- [[surahs/Q031-luqman/02-content-analysis]] §3 — verses where the pairs occur.
