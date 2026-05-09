---
surah: 38
test_id: Q038-F-06
title: ص-letter density rank — Q 38 among 60-100-verse surahs (mid-length band)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q038-F-06-sad-density-rank
alpha_bon: 0.05
---

# Q038-F-06 — Pre-registration: ص-letter density rank in the 60-100 verse band

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, rank-based):** Among the subset of surahs with verse-count in [60, 100], Q 38 Ṣād has **rank 1** (i.e. the strictly HIGHEST per-character ص-letter density). The pre-committed direction is HIGHEST.

This is the Ṣād-analogue of the classical claim that drove the Q 50-Qāf inspection: that single-letter muqaṭṭaʿāt surahs amplify their own letter not merely against a corpus background but **against length-matched peer surahs**. F-03 (locked 2026-05-07) tested the corpus-baseline version and returned DIRECTIONAL. F-06 tests the stricter rank-1 version restricted to the surah's own length-band.

**H0:** Q 38 is at rank ≥ 2 in the [60,100] band; or there exists at least one surah in the band with ص-density strictly higher than Q 38.

**Pre-committed direction (LOCKED):** Q 38 = rank 1 (strictly HIGHEST ص-density per character in [60,100]).

## 2. Operational definition

For every surah s in the corpus:
1. Concatenate all verse text (no-tashkeel).
2. Strip the opening muqaṭṭaʿ token if present (so the test is on the BODY, not on the trivial glyph contribution).
3. Strip whitespace and the project's non-letter codepoints (`۞۩ۭۚۖۗۘۙۜۤ`).
4. Compute `rate_ص(s) = count(ص in body) / |body_letters|`.

Define the **mid-length band** B = `{s : 60 ≤ n_verses(s) ≤ 100}`. Q 38 has 88 verses and is in B.

Compute rank of Q 38 in B by `rate_ص` (descending). Ties broken by raw count.

## 3. Test statistic

- Primary: `rank(Q 38 in B) by rate_ص`.
- Pass: rank == 1.
- Significance under H0 (uniform-shuffle null): probability that a randomly-selected member of B is rank 1 = 1/|B|. With |B| ≈ 20-25, the unconditional probability ≈ 0.04-0.05.
- Permutation p-value: for 10000 random permutations of surah labels within B, what fraction yield a "Q 38 rank 1" assignment? (This is degenerate under label-permutation since rates are surah-fixed; the meaningful significance is the rank itself.)
- Bonferroni: k = 1 (single test, single direction). α = 0.05.

## 4. Success / Failure

- **CONFIRMED**: Q 38 is rank 1 in B by ص-density (strict).
- **DIRECTIONAL**: Q 38 is rank 2 or 3 in B (still in top tier).
- **NULL**: Q 38 is rank ≥ 4 in B.
- **PRE-COMMIT VIOLATION**: Q 38 is rank > |B|/2 (i.e. below median in B). Published with full prominence.

## 5. Honest limits known a priori

- The Q 50-Qāf classical analogue (Q 50 leads in ق-density in its 35-50 verse band) is a precedent; whether the band-restricted version of the claim holds for Q 38 is the open empirical question. F-03 already showed Q 38 ص is at 1.47× corpus baseline, just below the strict-Bonferroni-3 threshold (p=0.053).
- Mid-length surahs (60-100) may include both prophet-cycle Meccan surahs (Q 11, Q 12, Q 15, Q 19, Q 20, Q 21, Q 27, Q 28, Q 37, Q 38, Q 40, Q 41, Q 42, Q 43, Q 44, Q 45, Q 46) and shorter Medinan-mixed surahs. The ص-rate is sensitive to lexical content: words like *الصابرين*, *الصالحات*, *قصص*, *المصورين*, *العصر*, *النصر*, *الإخلاص* will boost ص-density in their host surahs.
- This is a **DIRECTION-LOCKED PRE-COMMIT**. If Q 38 ranks below median, the test is published as a NULL with **explicit pre-commit violation flag**.

## 6. Rules-tuple

`(no-tashkeel, character-graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Muqaṭṭaʿ-stripping done per F-03 protocol.

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q038_F_06_sad_density_rank.py`. Fail-fast on mismatch.
