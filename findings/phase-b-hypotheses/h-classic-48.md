---
finding_id: h-classic-48
phase: B
status: PARTIAL — per-surah signals exist (14/95 surahs exceed within-surah permutation null, ~16x baseline) but the per-surah |ρ_1| distribution is statistically indistinguishable from Jāḥiẓ (KS p=0.79), and significantly LOWER than Bukhari (Quran 0.189 vs Bukhari 0.293, KS p=1.8e-6 in the OPPOSITE-from-spec direction). Worst-baseline-wins primary FAILS.
verdict_date: 2026-04-12
parent_task: #99
pre_reg: findings/phase-b-hypotheses/h-classic-48-prereg.md
script: scripts/h_classic_48_sakkaki_iqa.py
data: findings/phase-b-hypotheses/csv/h-classic-48.json
seed: 20260414
extends: h-new-35 (#69 COMPLETED 2026-04-13)
classical_anchor: al-Sakkākī Miftāḥ al-ʿUlūm pp. 527-540 tanāsub al-īqāʿ (PENDING physical verify)
bonferroni_k: 6
alpha_bon: 0.0083
---

# H-CLASSIC-48 — al-Sakkākī Miftāḥ īqāʿ verse-length distributional test

## TL;DR

**PARTIAL.** Two findings, neither aligned with the spec's PASS rule:

1. **Per-surah signals exist**: 14 of 95 qualifying surahs (n_verses ≥
   10) have |ρ_1| exceeding their own within-surah permutation 99th
   percentile — about 16× the chance baseline of 1%. This is genuine.

2. **The Quran |ρ_1| distribution is indistinguishable from Jāḥiẓ
   prose** at this resolution (KS D=0.095, p=0.79), and the Quran's
   distribution is statistically *lower* than Bukhari hadith reports
   (KS D=0.379, p=1.8e-6). Worst-baseline-wins primary therefore
   FAILS.

The spec asked: "are Quranic per-surah |ρ_1| values distributionally
distinct from matched-Arabic baseline?" The honest answer is: **only
versus Bukhari, and in the OPPOSITE direction from what the spec
operationalized as al-Sakkākī's claim.** Quranic verse-length
autocorrelation is real (sub-secondary), but it is NOT distinctive of
Quranic prose vs Jāḥiẓ at the 95-vs-95 sample size.

This **converges with H-NEW-35's MIXED finding** at higher resolution:
H-NEW-35 found weighted-mean Quran ρ(1) ≈ Jāḥiẓ ρ(1) at the corpus
level. H-CLASSIC-48 confirms this convergence persists at the
per-surah distributional level — it is not an artifact of corpus-level
averaging.

## Pre-registered test (verbatim, no amendments)

The pre-reg locked:
- **Per-surah filter**: n_verses ≥ 10. Result: 95 of 114 surahs
  qualify. (Pre-reg estimated 88; correction noted before script run,
  not after observing results.)
- **Lag set**: k ∈ {1, 2, 3}.
- **Baselines**: Bukhari-noquran (hadith-report split) + Jāḥiẓ
  (sentence split). LOCKED, no swap.
- **Worst-baseline-wins**: PRIMARY KS p uses the LARGEST p among
  COMPUTED baselines (the baseline Quran is hardest to distinguish
  from). LOCKED before run.
- **Two-sided KS**: locked per spec.
- **Sample method**: n_verses-matched non-overlapping span draws from
  baseline corpus, seeded.
- **Per-surah permutation null**: 10,000 within-surah shuffles per
  surah, count surahs exceeding their per-surah 99th percentile.
- **k_excess threshold**: SECONDARY pre-registered as ≥ 5 (i.e., 5×
  the chance baseline of ~1 surah).
- **Bonferroni k=6** within H-CLASSIC-44..49 family, α_bon = 0.0083.

## Result

### Primary (per-surah |ρ_1| KS distributional test, worst-baseline-wins)

| baseline | n_quran | n_baseline | KS D | KS p | direction | passes α_bon? |
|----------|---------|------------|------|------|-----------|---------------|
| Bukhari hadith reports | 95 | 95 | **0.379** | **1.8e-6** | Quran < Bukhari | YES (in OPPOSITE direction) |
| Jāḥiẓ Ḥayawān | 95 | 95 | 0.095 | **0.7903** | indistinguishable | NO |

**Worst-baseline-wins**: max(p) is Jāḥiẓ at p = **0.7903**. Required
p < 0.0083. **PRIMARY FAILS.**

The Bukhari KS comparison is striking but in the unwanted direction:
Quranic surahs have LOWER per-surah |ρ_1| than length-matched
Bukhari hadith-report spans. This is consistent with H-NEW-35's
observation that Bukhari has strong negative ρ(1) (alternating
isnad-matn lengths) — over short matched spans, that produces high
absolute values. But it does NOT support al-Sakkākī's *Quran is
distinctively rhythmic* reading.

### Distributional descriptives

| corpus | mean |ρ_1| | sd | median |ρ_1| |
|--------|--------------|-----|----------------|
| Quran (95 surahs) | 0.1890 | 0.147 | 0.1647 |
| Jāḥiẓ (95 spans) | 0.1718 | 0.144 | 0.1484 |
| Bukhari (95 spans) | 0.2933 | 0.147 | 0.2870 |

The Quran |ρ_1| distribution sits 10% above Jāḥiẓ on average — a
real but small directional effect. KS sample size (95 vs 95) does not
have power to detect a difference at this magnitude with α = 0.0083.
**Not enough surahs.** Pre-reg disclosed this is a structural
limitation: the Quran has only 114 surahs, of which 95 are long enough
to compute a meaningful ρ_1.

The Quran ρ_1 sign breakdown is **74 positive, 21 negative** (sign
test vs 50/50: p ≈ 1.4e-8). The bulk of the 21 negative cases are
short Medinan/transitional surahs where the verse-length sequence has
mood pivots that drive sign-flipping. Sign-test alone would PASS, but
it isn't the pre-registered primary.

### Secondary (per-surah within-surah permutation null at lag 1)

- **N_PERM** = 10,000 shuffles per surah.
- **n_exceed_lag1 = 14 / 95 surahs** exceed their per-surah 99th
  percentile. Chance baseline: ~0.95 surahs (1% × 95). Observed
  excess: ~14.7×. **k_excess threshold ≥ 5: PASS.**

The 14 exceeding surahs (sorted by observed |ρ_1|):

| Surah | name | n_verses | |ρ_1| obs | 99 pct null | revelation period |
|-------|------|----------|----------|-------------|---|
| 85 | al-Burūj | 22 | 0.649 | 0.505 | Meccan (oath/eschat) |
| 78 | al-Nabaʾ | 40 | 0.576 | 0.386 | late Meccan (eschat) |
| 51 | al-Dhāriyāt | 60 | 0.564 | 0.324 | Meccan (oath/eschat) |
| 56 | al-Wāqiʿa | 96 | 0.407 | 0.252 | Meccan (eschat) |
| 14 | Ibrāhīm | 52 | 0.380 | 0.347 | Meccan (mid) |
| 52 | al-Ṭūr | 49 | 0.356 | 0.335 | Meccan (oath/eschat) |
| 38 | Ṣād | 88 | 0.353 | 0.281 | Meccan |
| 30 | al-Rūm | 60 | 0.329 | 0.318 | Meccan (mid) |
| 20 | Ṭā Hā | 135 | 0.289 | 0.215 | Meccan |
| 7 | al-Aʿrāf | 206 | 0.272 | 0.176 | late Meccan |
| 16 | al-Naḥl | 128 | 0.269 | 0.226 | late Meccan/transition |
| 18 | al-Kahf | 110 | 0.257 | 0.236 | Meccan |
| 4 | al-Nisāʾ | 176 | 0.220 | 0.186 | Medinan |
| 2 | al-Baqara | 286 | 0.165 | 0.147 | Medinan |

**The exceeding-surah list is dominated by Meccan oath / eschatological
surahs** (al-Burūj, al-Nabaʾ, al-Dhāriyāt, al-Wāqiʿa, al-Ṭūr). These
are exactly the surahs that classical balāgha singles out for *īqāʿ*
in the strict sense — short, formulaic, rhythmically dense. The two
long Medinan surahs (al-Baqara and al-Nisāʾ) likely make the list
through high N alone (286 and 176 verses respectively give the
permutation null very tight 99th percentiles).

This is a real, classically-anchored signal — but it is local to a
specific cluster of surahs, not a global property of the Quran.

### Tertiary (descriptive multi-lag)

| lag | n_exceed / 95 |
|-----|---------------|
| 1 | 14 |
| 2 | 7 |
| 3 | 6 |

Decay is monotonic at the per-surah-exceedance level (14 > 7 > 6),
which weakly supports the al-Sakkākī rhythmic-memory-decays-with-lag
intuition for the subset of surahs where the signal exists. Not
Bonferroni-counted.

### Final verdict

**PARTIAL — per-surah signals exist but distribution matches baseline.**

This is the third row of the pre-registered acceptance matrix:
"PRIMARY KS p ≥ 0.0083 vs WORST baseline AND SECONDARY k_excess ≥ 5".
Routing is literal — no post-hoc reframing.

## What this rules in and rules out

**Rules in**: There is a *cluster* of 14 specific surahs (mostly
Meccan oath/eschatological) where verse-length autocorrelation is
strong enough to reject the within-surah permutation null at the 99th
percentile. al-Sakkākī's *īqāʿ* exists in the Quran in a localized,
genre-bound way, not as a universal property of all surahs.

**Rules out (provisionally)**: The strong universalist reading —
*every Quranic surah has rhythmic-memory autocorrelation that
distinguishes it from Arabic prose* — is not supported. Quran's
per-surah |ρ_1| distribution is statistically indistinguishable from
Jāḥiẓ Ḥayawān at the 95-vs-95 sample size. Either (a) Jāḥiẓ has
similar īqāʿ, or (b) the effect is too small to detect with 95
surahs. This is the same convergence H-NEW-35 found at the corpus
scale — and H-CLASSIC-48 shows it persists at the per-surah
distributional scale.

**Bukhari is the wrong baseline for this test**: Bukhari hadith-report
spans have systematically HIGHER |ρ_1| than the Quran. This reflects
the negative ρ(1) (alternating isnad/matn lengths) H-NEW-35 already
documented. In matched short spans, alternation produces high |ρ_1|.
Future H-CLASSIC-48-like tests should consider Mutanabbī Dīwān or
Ibn Hishām Sīra (continuous prose) as more diagnostic baselines.

## Why this is not REVERSE

The Bukhari KS test passes with p=1.8e-6 in the direction "Quran has
LOWER |ρ_1| than Bukhari spans". Could this be filed as
`h-classic-48-reverse-suppression.md`?

**No.** The pre-reg locks worst-baseline-wins, not best-baseline-wins.
The Jāḥiẓ result (worst, p=0.79) is the binding constraint. The
Bukhari direction is a separate narrative observation about the
*alternation pattern in hadith editorial order*, which H-NEW-35
already filed as a side-finding (Bukhari ρ(1) = -0.152). Re-filing
H-CLASSIC-48 as a reverse finding because of the Bukhari leg would be
forking via cherry-picked baseline — explicitly prohibited by no-fork
protection §3.

## Methodological notes

### Why the worst-baseline-wins rule matters

Without it, this test would have shown a "passing" KS p < 0.0083
against Bukhari and that would be the reported outcome. The Quran
result (mean |ρ_1| = 0.189) is BELOW Bukhari (0.293) and ABOVE
Jāḥiẓ (0.172). The pre-reg's locking the worst (max-p) baseline as
the binding test prevents the FALSE POSITIVE that would arise from
"any baseline with significant difference passes".

This is a structural feature of cross-corpus secondary tests: if you
allow best-of-N baselines, you implicitly run N comparisons and need
N-fold Bonferroni correction. Worst-of-N is a single test under
H₀ "all baselines match Quran".

### Why 95 surahs is too few for KS @ α=0.0083

The KS critical D-value at α = 0.0083 with n1=n2=95 is approximately:
  D_crit = c(α) × √((n1+n2)/(n1×n2)) ≈ 1.628 × √(190/9025) ≈ 0.236.

Observed Quran-vs-Jāḥiẓ D = 0.0947, well below 0.236. Even if Quran
were 20% higher than Jāḥiẓ on average, D ≈ 0.15-0.18 would still not
cross 0.236. The 95-surah corpus is **structurally underpowered** to
detect the effect size we see at this α-level. This is a real limit
of the Quran-as-test-corpus, not a methodological defect.

### Sample-size sensitivity (not pre-registered, descriptive only)

If the same effect (mean |ρ_1| difference of +0.017) held at n=500
matched spans per side, the KS test would likely cross α=0.0083.
But that would require either (a) treating each verse pair as
independent, which it is not, or (b) re-running on a larger corpus
with intra-Quranic structure, which doesn't exist. The 95-surah
limit is a hard ceiling.

## Compute log

- Quran per-surah ρ_k: ~0.05 sec.
- Baseline span sampling + ρ_k: ~0.1 sec per baseline.
- Per-surah permutation null lag-1 (10,000 shuffles × 95 surahs):
  ~22 sec.
- Tertiary lag-2 + lag-3 (1,000 shuffles × 95 surahs × 2 lags):
  ~5 sec.
- KS tests via scipy: trivial.
- **Total wall time: ~30 sec.** Well under the pre-reg's 2-minute
  estimate.

## Pre-reg compliance

PRE-REG-STANDARD-04. All locked parameters honored:
- Seed 20260414 ✓ (sub-streams +0/+1/+2/+11/+12 for baseline-bukhari /
  baseline-jahiz / lag1-perm / lag2-perm / lag3-perm)
- n_verses ≥ 10 filter ✓ (95 surahs survive; pre-reg estimate 88
  was corrected to 95 BEFORE script run)
- Lag set {1, 2, 3} ✓ (no post-hoc sweep over k=4,5,...)
- Two-sided KS ✓ (no one-sided substitution)
- Worst-baseline-wins ✓ (Jāḥiẓ p=0.79 is the binding p, not Bukhari
  p=1.8e-6)
- 10,000 within-surah shuffles per surah ✓
- Bonferroni k=6, α_bon = 0.0083 ✓
- Verdict matrix applied literally (PARTIAL row matched, not PASS,
  not NULL) ✓
- Baselines not swapped (Bukhari + Jāḥiẓ as locked, not swapped for
  Mutanabbī or Sīra despite Bukhari direction issue) ✓

Disclosed deviations:
- **Pre-reg estimated 88 qualifying surahs; actual is 95.** Correction
  was made to the pre-reg file BEFORE the script ran (the verbatim
  filter "n_verses ≥ 10" was unchanged; only the count estimate
  changed). This is a pre-execution numeric correction, not a
  post-hoc forking path.
- No other deviations.

## No-fork protections honored

All 7 pre-registered no-fork protections were honored:

1. **Per-surah filter LOCKED**: n_verses ≥ 10 only, 95 surahs survive.
   No tweaking to ≥ 8 or ≥ 12 to optimize.
2. **Lag set LOCKED**: only {1, 2, 3} reported in primary; lags 4+
   not run.
3. **PRIMARY uses worst baseline**: Jāḥiẓ p=0.7903 binds, not
   Bukhari p=1.8e-6.
4. **Span sampling deterministic** under seed 20260414+sub-stream.
5. **Two-sided KS LOCKED**: no one-sided test substitution.
6. **Permutation null seed**: 20260414+2 for lag-1, 20260414+11/+12
   for lag-2/lag-3.
7. **Baselines not swapped**: Bukhari + Jāḥiẓ as locked.

## Coordination with H-NEW-35

H-NEW-35 (#69) reported MIXED:
- Sub-(a) Quran weighted ρ(1) z=+13.13 vs phase-shuffle null PASS.
- Sub-(b) strict-monotone decay FAIL (lag 4→5 inversion); loose
  ρ(1) > ρ(5) PASS.
- Sub-(c) corpus-level Fisher z-diff vs Bukhari and Jāḥiẓ FAIL
  (Quran ρ(1) ≈ Jāḥiẓ ρ(1)).

H-CLASSIC-48 deepens H-NEW-35 sub-(c) by moving from a corpus-level
Fisher z-diff (which compares two scalars) to a per-surah
distributional KS test (which compares two distributions of N=95).
**The verdict is consistent**: Quranic verse-length autocorrelation is
indistinguishable from Jāḥiẓ at both scales. The per-surah resolution
adds nuance: 14 specific Meccan eschatological/oath surahs DO have
exceptional within-surah signal even though the global distribution
matches Jāḥiẓ.

H-NEW-35 and H-CLASSIC-48 should be cited together: the pair gives a
"corpus level + distributional level" cohesive verdict. Neither test
overturns the other.

## Follow-up hypotheses

**H-CLASSIC-48.1** (queued): test the 14 exceeding surahs as a
genre-bound hypothesis. Pre-register: "Meccan oath/eschatological
surahs (Q 51, 52, 56, 78, 85 + comparators) have higher per-surah
|ρ_1| than non-oath Meccan surahs of comparable length." This requires
a pre-committed surah-period classification (per al-Suyūṭī or
Nöldeke), not post-hoc selection from the 14.

**H-CLASSIC-48.2** (queued): re-run the KS test against Mutanabbī
Dīwān (poetry, more directly comparable to Quranic short surahs at
verse-line level) and Ibn Hishām Sīra (continuous narrative prose) as
better-matched baselines than Bukhari hadith reports.

## Files

- Script: `scripts/h_classic_48_sakkaki_iqa.py`
- Output: `findings/phase-b-hypotheses/csv/h-classic-48.json`
- Pre-reg: `findings/phase-b-hypotheses/h-classic-48-prereg.md`
- Seed: 20260414

## Reproducibility

```bash
cd /Users/grey/Downloads/quran
python3 scripts/h_classic_48_sakkaki_iqa.py
# Wall time ~30 sec. Output:
#   findings/phase-b-hypotheses/csv/h-classic-48.json
#   stderr → progress and verdict log
```

Seed 20260414 makes the run fully deterministic. Sub-streams are
seeded as SEED+0 (Bukhari spans), SEED+1 (Jāḥiẓ spans), SEED+2 (lag-1
permutation), SEED+11 (lag-2 perm), SEED+12 (lag-3 perm).
