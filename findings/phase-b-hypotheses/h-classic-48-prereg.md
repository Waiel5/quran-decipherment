---
finding_id: h-classic-48
phase: B
status: PRE-REGISTERED — computational-tester self-pre-reg per PRE-REG-STANDARD-04
pre_registered_by: computational-tester (2026-04-12)
registration_date: 2026-04-12
parent_task: #99
spec_source: findings/phase-b-hypotheses/h-classic-44-to-49-spec.md §H-CLASSIC-48
extends: h-new-35 (task #69, COMPLETED 2026-04-13) — H-NEW-35 ran weighted-mean ρ(k) corpus-level Fisher z-diff; H-CLASSIC-48 adds per-surah |ρ_1| distribution + KS test vs n_verses-matched baseline spans
rules_tuple: (no-tashkeel, hafs-kufan, character-length-cleaned-verse, orthographic-token, mashriqi)
seed: 20260414
sided_test: two-sided (KS test is two-sided by construction; al-Sakkākī's qualitative claim is direction-unspecified — could be alternation OR sustained pattern)
direction_prereg_source: al-Sakkākī Miftāḥ al-ʿUlūm pp. 527-540 (PENDING physical verify) tanāsub al-īqāʿ; "non-zero" prediction does not commit to sign
baselines: [bukhari-noquran (hadith-report split), jahiz-hayawan (sentence split)]
bonferroni_k: 6   # within H-CLASSIC-44..49 family
alpha_bon: 0.0083   # = 0.05 / 6
null_publishable: true
positive_publishable: true
---

# H-CLASSIC-48 — al-Sakkākī Miftāḥ īqāʿ verse-length autocorrelation distributional test

## Why this pre-registration exists

Task #69 H-NEW-35 (COMPLETED 2026-04-13) ran the within-surah verse-length
autocorrelation primary at the corpus level: it computed a single
weighted-mean ρ(1) across all 114 surahs (= 0.137), tested it against a
phase-shuffle null (z = +13.13, PASS), and ran a Fisher z-diff vs
corpus-level baseline ρ(1) values. The Fisher z-diff against Jāḥiẓ
returned z = −0.67 (FAIL — Quran ρ(1) ≈ Jāḥiẓ ρ(1) at corpus level).
Joint verdict: MIXED.

H-CLASSIC-48 deepens the test in three orthogonal ways that the
classical-scholar spec explicitly flags as *additions* to H-NEW-35:

1. **Per-surah resolution** instead of corpus-level scalar. Compute ρ_k
   for k ∈ {1, 2, 3} INDIVIDUALLY for each of the 114 surahs (filtered
   to n_verses ≥ 10 → 95 surahs survive). The resulting **distribution
   of |ρ_1|** preserves heterogeneity that the corpus-level scalar
   destroys.

2. **n_verses-matched baseline spans** instead of corpus-level baseline
   ρ. Each Quranic surah of length n is matched to a baseline span of
   length n drawn from the same baseline corpus, producing a
   distribution of baseline |ρ_1| values with the same sample-size
   profile as the Quran distribution.

3. **Kolmogorov-Smirnov test** between the two distributions instead of
   Fisher z-diff between two scalars. KS is sensitive to differences in
   shape, spread, modes, and tails — not just means. **The two
   distributions could differ even if their means match.**

The H-NEW-35 corpus-level result does NOT predetermine H-CLASSIC-48's
distributional outcome. They are statistically and theoretically
distinct tests.

## Pre-registered hypotheses

**H-CLASSIC-48-PRIMARY (locked, two-sided):** the per-surah |ρ_1|
distribution of Quranic surahs (n=88 surahs with n_verses ≥ 10) differs
from the per-span |ρ_1| distribution of n_verses-matched spans drawn
from the WORST baseline corpus (Bukhari hadith-reports OR Jāḥiẓ
sentences, whichever yields the LARGEST KS p-value — i.e., the baseline
the Quran is hardest to distinguish from). Two-sample KS p < α_bon =
0.0083.

**H-CLASSIC-48-SECONDARY (per-surah permutation gate):** for each of 88
qualifying surahs, the within-surah permutation null at lag k=1 yields
the surah's |ρ_1| 99th-percentile threshold. Count the number of
surahs whose observed |ρ_1| exceeds the threshold. Under the null
hypothesis of length-independence, this count should be ≈ 1% × 88 =
0.88 surahs. We pre-register **k_excess ≥ 5** (~5x baseline) as
significant.

**H-CLASSIC-48-TERTIARY (multi-lag descriptive):** ρ_k for k ∈ {1, 2, 3}
distributions reported per surah; the proportion of surahs with
**any** lag-k significant in the per-surah permutation null is
reported descriptively. Not Bonferroni-counted.

## Pre-registered acceptance matrix (Bonferroni k=6 within H-CLASSIC-44..49 family, α_bon = 0.0083)

| Outcome                                                                                                     | Verdict                       |
|-------------------------------------------------------------------------------------------------------------|-------------------------------|
| PRIMARY KS p < 0.0083 vs WORST baseline AND SECONDARY k_excess ≥ 5                                         | **PASS — al-Sakkākī īqāʿ confirmed at distributional level** |
| PRIMARY KS p < 0.0083 vs WORST baseline AND SECONDARY k_excess < 5                                         | **PARTIAL — distributional difference present but per-surah signals are weak** |
| PRIMARY KS p ≥ 0.0083 vs WORST baseline AND SECONDARY k_excess ≥ 5                                         | **PARTIAL — per-surah signals exist but distribution matches baseline** |
| PRIMARY KS p ≥ 0.0083 AND SECONDARY k_excess < 5                                                            | **NULL — al-Sakkākī īqāʿ falsified at verse-length distributional scale** |
| Either baseline corpus is degenerate (insufficient spans) and the OTHER baseline shows PRIMARY p < 0.0083  | **PARTIAL — single-baseline confirmation; degenerate baseline disclosed** |

## No-fork protections

1. **Per-surah filter LOCKED**: only surahs with n_verses ≥ 10 enter
   the primary distribution (matches spec). 26 surahs excluded
   (Q 87-114 minus a few longer ones); the surviving 88 are
   pre-committed BEFORE the script runs. Excluded surahs are NOT
   reported as a separate test.

2. **Lag set LOCKED to {1, 2, 3}**: spec specifies these three lags.
   No post-hoc sweep over k ∈ {4, 5, ...}. Lags 4+ may be reported
   descriptively but cannot rescue a failed primary.

3. **PRIMARY uses WORST baseline (highest p), not best (lowest p)**:
   this enforces the strictest interpretation. If the worst baseline
   passes, both pass. If only the best baseline passes, the verdict is
   PARTIAL with single-baseline disclosure. **This rule is locked
   before the script runs to prevent best-of-baselines cherry-picking.**

4. **n_verses-matched span construction LOCKED**: for each qualifying
   Quranic surah of length n, draw the FIRST contiguous span of length n
   from the baseline corpus's sentence-length sequence at a starting
   index determined by the seed-RNG (sampling without replacement
   across surahs). This is deterministic given the seed.

5. **Two-sided KS LOCKED**: spec explicitly notes "KS is two-sided by
   construction; al-Sakkākī's qualitative claim is direction-
   unspecified". No post-hoc one-sided test substitution.

6. **Permutation null seed**: 20260414, 10,000 within-surah shuffles
   per surah for the SECONDARY test. Seed locked.

7. **Baseline corpora LOCKED to bukhari-noquran (hadith-report split)
   + jahiz-hayawan (sentence split)**. Spec also mentions Mutanabbī
   could be considered, but is not in the spec for H-CLASSIC-48.
   No baseline swap.

## Pre-registered operationalization

1. **Tokenization**: per-verse character count of cleaned Arabic letters
   (`[\u0621-\u064A]` regex). Identical to H-NEW-35.

2. **Verse extraction**: load `quran-text/quran-no-tashkeel.json`,
   iterate surahs in mushaf order. For each surah build the integer
   sequence of per-verse character counts.

3. **Per-surah filter**: keep surahs with len(seq) ≥ 10. Exclude the
   rest from primary. Expected: 88 surahs survive (will verify and
   report exact count).

4. **Per-surah ρ_k computation**: for each k ∈ {1, 2, 3}, compute
   Pearson r(seq[:-k], seq[k:]). Take |ρ_k|.

5. **Quran |ρ_1| distribution**: list of 88 |ρ_1| values, one per
   qualifying surah.

6. **Baseline span extraction**:
   - **Bukhari**: load `data/baseline-corpora/raw/bukhari-noquran.txt`,
     split on `حدثنا|أخبرنا|وحدثنا|وأخبرنا` (hadith-report markers),
     compute character-length per report → integer sequence of report
     lengths. (Same method as H-NEW-35.)
   - **Jāḥiẓ**: load `data/baseline-corpora/raw/jahiz-hayawan.txt`,
     split on `[.!?؟۔\n]+|\s{2,}` (sentence markers), compute
     character-length per sentence → integer sequence. (Same method as
     H-NEW-35.)

7. **Baseline span sampling**: for each qualifying Quranic surah of
   length n, sample a contiguous span of length n from the baseline
   sequence. Sampling is **non-overlapping**: maintain a list of
   available starting indices, use seeded random.choice to pick a
   start, then mark indices [start, start+n) as used. If a baseline
   sequence has insufficient remaining indices for the next surah,
   mark the corpus as DEGENERATE for that run and disclose. (Bukhari
   has ~16,698 reports and Jāḥiẓ has ~48,936 sentences per H-NEW-35;
   sum of qualifying-surah-lengths is ~5,800 verses, so both should
   have plenty of room.)

8. **Baseline |ρ_1| computation**: for each sampled span, compute
   |ρ_1| of the length sequence. Build the baseline distribution of
   88 |ρ_1| values per baseline.

9. **Two-sample KS test**: scipy.stats.ks_2samp(quran_abs_rho1,
   baseline_abs_rho1) for each baseline. Take the LARGER of the two
   p-values as the "worst baseline" PRIMARY p-value.

10. **Per-surah permutation null (SECONDARY)**: for each of 88 surahs,
    shuffle its verse-length sequence 10,000 times (seeded), compute
    |ρ_1| each time, take the 99th percentile. Count surahs whose
    observed |ρ_1| exceeds their per-surah 99th percentile.

11. **Multi-lag descriptive (TERTIARY)**: for each lag k ∈ {1, 2, 3},
    repeat the per-surah permutation null and count exceedances.
    Reported as a 3-row table; not Bonferroni-counted.

## Outputs

- **JSON**: `findings/phase-b-hypotheses/csv/h-classic-48.json`
- **Narrative**: `findings/phase-b-hypotheses/h-classic-48.md`
- **Script**: `scripts/h_classic_48_sakkaki_iqa.py`

## Compute estimate

- Per-surah ρ_k: O(n) per surah × 88 surahs × 3 lags = trivial.
- Baseline span extraction + ρ_k: trivial (88 spans per baseline).
- Per-surah permutation null: 88 surahs × 10,000 shuffles × O(n) per
  shuffle. For largest surah (n ≈ 286), this is ~250M ops. Estimated
  **~30-60 seconds** in pure Python.
- KS test: trivial via scipy.
- **Total wall time: < 2 minutes.**

## Seed

`20260414` — same as H-NEW-35 / [[h-new-38-directed-pmi|H-NEW-38]] family. Reused to maintain
audit trail consistency. NB: per-test deterministic — different tests
use different RNG sub-streams driven by independent random.Random
instances.

## Bonferroni accounting

- **k = 6** within the H-CLASSIC-44..49 family per spec.
- **α_bon = 0.0083** (= 0.05 / 6).
- The per-surah permutation null SECONDARY uses an empirical 99th
  percentile (α = 0.01 per surah) — this is a separate gate, not in
  the Bonferroni family.
- Per spec, H-CLASSIC-48 tests ONE primary hypothesis (KS distributional
  difference). The SECONDARY/TERTIARY are descriptive controls.

## Reverse-finding routing

H-CLASSIC-48 is two-sided: there is no "reverse direction" because the
KS test treats both tails symmetrically. A significant KS result with
Quran |ρ_1| distribution shifted LOWER than baseline (i.e., Quran has
LESS verse-length autocorrelation than matched Arabic) would still be
a PASS, with the interpretation that "al-Sakkākī's īqāʿ exists in
Arabic prose generally and the Quran does NOT have more of it than
matched baseline" — i.e., the falsification of the *novelty* claim,
which is a publishable distributional finding.

## Dispatch chain

1. computational-tester → authors this pre-reg (this file). **DONE.**
2. computational-tester → authors `scripts/h_classic_48_sakkaki_iqa.py`
   per the operationalization above.
3. computational-tester → executes the script, writes JSON + narrative.
4. skeptical-auditor → audits compliance with this pre-reg.
5. integrator → integrates verdict into MASTER ledger.

## Pre-execution lock confirmation

This file is committed BEFORE the script is written. Any subsequent
deviation must be documented as a disclosed-not-amended deviation in
the narrative, NOT a silent post-hoc edit to this pre-reg. The seed,
lag set, baseline list, KS test, Bonferroni k, α_bon, per-surah
filter (n ≥ 10), and worst-baseline-wins rule are LOCKED.

## Data reuse disclosure

- Reuses `len_letters`, `pearson_r`, `autocorr`, surah loader, and
  `sentence_lens_from_text` from `scripts/h_new_35_length_autocorr.py`.
- Reuses `quran-text/quran-no-tashkeel.json`,
  `data/baseline-corpora/raw/bukhari-noquran.txt`,
  `data/baseline-corpora/raw/jahiz-hayawan.txt`.
- Does NOT reuse statistical machinery from any other H-NEW finding;
  KS test is fresh via scipy.stats.ks_2samp.
- H-NEW-35 weighted-mean ρ(k) values are NOT inputs to H-CLASSIC-48;
  per-surah ρ_k is recomputed independently.
