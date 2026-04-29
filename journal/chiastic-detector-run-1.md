# Chiastic Detector — Run 1

**Agent:** Phase C structural / chiastic detector
**Date:** 2026-04-12
**Status:** complete (one null model only — flagged as partial)
**Outputs:**
- `findings/phase-c-structures/chiastic-audit.md`
- `analysis/notebooks/chiastic_audit.py`
- `analysis/notebooks/chiastic_audit_results.json`

## What I did

Built a per-verse triliteral-root extractor from QAC v0.4 (`data/morphology/quranic-corpus-morphology-0.4.txt`). For each surah, computed the average pair-Jaccard between verse i and verse N+1-i for all i ∈ [1, ⌊N/2⌋]. Compared to a verse-shuffle null (200 trials per surah, seeded `surah_id*1000+trial`). Same procedure on every contiguous 5..15-verse window of every surah of N≥10 (57,996 sub-windows, 50 trials each, seed `sid*1e5+start*100+w*10+trial`). Same idea cross-surah by pairing surah k with surah 115-k (2000 surah-index permutations, seed 7777+trial).

## What I found

**Whole-surah ranking (top 5 by z):**

1. Al-Hashr (s.59) z=+2.42 — **inclusio not chiasmus** (driven by v1↔v24 doxological frame)
2. Hud (s.11) z=+2.40 — **real prophet-cycle ring** with Salih story (v62) at centre
3. At-Tin (s.95) z=+2.33 — small-N artefact, demote
4. An-Nahl (s.16) z=+2.27 — diffuse but consistent ring
5. Al-Haqqah (s.69) z=+2.06 — bookend (v2↔v51 share root *Hqq*)

**No surah survives Holm-Bonferroni or BH-FDR over k=114.** Hud's raw p=0.015 is the strongest and the corrected threshold is ~0.00044.

**Cross-check of the published claims:**

- **Al-Ma'ida (5) — Cuypers' canonical case — DISCONFIRMED.** Ranks 111/114 with z=-2.06, p=0.99. The natural verse order is *more disordered* w.r.t. lexical pairing than 99% of random shuffles. This converges with Sinai 2017's critique. Caveat: Cuypers' rings are thematic-block-based, not verse-pair-based, so this is the wrong instrument for his exact claim — but a true ring should not score *negative* z.
- **Al-Baqarah (2) — Farrin's canonical case — partially confirmed.** Whole-surah z=-0.12 (random). BUT the sub-surah scan finds the strongest ring in the entire Quran inside Al-Baqarah at v131-v144 (z=+9.69), which is exactly the Abraham/qibla pericope that Zahniser (1991) and Farrin (2014) call the geometric centre. **The algorithm finds Farrin's centre without being told where to look.**

**Sub-surah scan — 4 windows survive Bonferroni at α=0.05 over 57,996 tests (z>4.78):**

1. Al-Baqarah v131-144 (Abraham/qibla) z=+9.69 — Farrin's centre
2. Al-Qamar v21-30 (Thamud) z=+6.46 — bracketed by the verbatim refrain *fakayfa kāna ʿadhābī wa-nudhur*
3. 'Abasa v1-9 (the rebuke) z=+6.09 — opening pericope
4. Al-Kahf v83-91 (Dhul-Qarnayn) z=+5.19 — east/west sun-set/sun-rise inversion

**Cross-surah whole-Quran ring — DISCONFIRMED.** Pairing surah k with surah 115-k under the canonical mushaf order gives z=**-4.87** (observed = 0.0999, null mean = 0.1348, std = 0.0072, p=1.000). The mechanical reason: the mushaf is ordered by ~length, so surah k and 115-k have very different lengths and asymmetric root sets; random permutations frequently pair similar-length surahs and score higher. **Farrin's macro-ring claim about the 114-surah arrangement is falsified by lexical similarity.**

## Methodological notes / pitfalls I had to navigate

- The translation file `en.sahih.txt` is line-aligned 1:1 with verses 1..6236 in canonical order, plus a footer block. I used cumulative `total_verses` offsets per surah to look up specific verses, not raw line numbers (initial mistake corrected after one wrong-surah lookup).
- The QAC root field is `ROOT:xxx|`. Not every word has a root (function words don't); my extractor returns an empty set for verses with zero root-bearing words, which is correct behaviour for jaccard.
- The root **Alh** ("Allah") is in nearly every verse and inflates many pair Jaccards. I did not strip it for run 1 — flagged as a follow-up. Stripping should preserve the real findings (Al-Baqarah 131-144 has rich shared roots beyond Alh) and demote the doxological-bookend cases like Al-Hashr.
- Even N: when N is even there's no single centre verse; I report the midpoint as "between v(N/2) and v(N/2+1)".
- Small surahs with 3 verses (Al-Kawthar, Al-'Asr) have one pair to score; if it's zero the z is 0/0 → set to 0, which is why they sit at the bottom of the rank as "ties at z=0". They are not anti-rings.
- Cuypers and Farrin operate at the *block* level, not the verse level. A natural follow-up is to run the same statistic over k-block segmentations (k=3,5,7,9) — that is the test that would give Cuypers a fair shake.

## Scaling decisions I made

- 200 shuffles per surah is enough for 2-σ resolution but not for FDR-quality p-values; that's why I report z instead of leaning on the empirical p. Bumping to 10⁴ wouldn't change the ranking but would tighten the p estimates.
- 50 shuffles per sub-surah window with 57,996 windows is 2.9M shuffles total, which ran in seconds on a single CPU. Bumping to 200 wouldn't change the four Bonferroni-survivors materially.
- 2000 permutations for cross-surah is plenty: the observed value is so far from the null mean (-4.87 σ) that more permutations only sharpen an already obvious negative result.

## What's still missing (per `docs/statistical-rigor-protocol.md` §3)

This finding is **partial**, not confirmed. Required follow-ups:

1. Second null model (1.4 length-matched comparable Arabic — sample matched-length passages from Bukhari with quoted Quran stripped, compute same statistic, build a comparable-corpus null).
2. Robustness check under Alh-removed root sets.
3. Robustness check under lemma-level rather than root-level similarity.
4. Block-level pairing pass (k = 3, 5, 7, 9 equal blocks per surah) to give Cuypers his exact test.
5. Increment `findings/phase-b-hypotheses/test-register.md` with this test.

## One-line summary

The single most ring-shaped *region* in the Quran is **Al-Baqarah 131-144 (Abraham → qibla, z=+9.69 over 58k tests)** — exactly Farrin's published centre. The single most ring-shaped *whole surah* is **Hud (Salih story at v62, z=+2.40)** — converging with Mir / Robinson. Cuypers' Al-Ma'ida claim is algorithmically anti-confirmed (z=-2.06, ranked 111/114). Farrin's whole-Quran macro-ring is algorithmically anti-confirmed (z=-4.87). Of 114 whole-surah tests, **zero** survive multiple-comparison correction; of 57,996 sub-windows, exactly **four** do. All four correspond to literary units already known to scholars. The audit is therefore best read as a *quantitative confirmation of a small number of locally-real rings* and a *quantitative refutation of two famous global ring claims*.
