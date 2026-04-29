# Journal — zipf-per-surah-run-1 (H14)

**Date:** 2026-04-12
**Agent:** zipf-per-surah
**Task:** Test hypothesis H14 from `findings/deep-hypotheses-queue.md`:
per-surah Zipf α heterogeneity and its correlation with revelation
order. H14 predicts Early Meccan α > 1.5 (oracular / concentrated) and
Medinan α ≈ 1.1 (legal / flat).

## 1. Context ingested

Required reading before coding:

- `findings/phase-b-hypotheses/information-theory.md` §4:
  whole-Quran Zipf lemma α = 1.318, R² = 0.975, 4 832 distinct lemmas,
  74 608 tokens. OLS log-log on (rank+1) vs freq, rank 1-based.
- `findings/phase-b-hypotheses/chronological-revelation.md` §3:
  Nöldeke 4-phase verse-length ramp (F = 209.96). This is the existing
  diachronic-signal anchor. Nöldeke phase means `avg_v_letters`:
  18.5 → 38.7 → 66.0 → 79.9.
- `findings/phase-b-hypotheses/cross-textual-baseline.md` §1:
  whole-Quran α (under orthographic-token rule) = 0.97. This is NOT
  comparable to the info-theory lemma α = 1.318 — different rules.
  Cross-baseline's verdict that "Quran Zipf isn't distinctive" is a
  word-token-level claim; it does not falsify the lemma-level claim.
- `findings/deep-hypotheses-queue.md` §H14: the full hypothesis and
  acceptance criterion (|ρ| > 0.3, p < 0.01, length-controlled).
- `docs/methodology.md` §7: rules tuple format.
- `analysis/info_theory_run.py task4_zipf`: exact OLS fit I need to
  replicate for per-surah consistency.

## 2. Design decisions (pre-data)

| Decision | Value | Rationale |
|---|---|---|
| Fit rule | OLS log-log on `log(r+1)` vs `log(freq)` | Match info-theory exactly |
| Min distinct lemmas | 50 | Task spec |
| Bootstrap resamples | 1000 | Standard for percentile CI on small samples |
| Permutation shuffles | 10000 | Task spec + H14 null model (§1.5) |
| Partial correlation control | log(n_tokens) | Length confound is obvious upfront |
| Length bins | 5 quintiles | Standard stratification |
| Seed | 17 | Reproducibility |

I decided upfront to report the length-controlled analysis prominently
because the info-theory write-up explicitly warns that "letter entropy
is not a useful Meccan/Medinan discriminator because length swamps any
genuine signal at this granularity" — I anticipated the same confound
would hit Zipf α.

## 3. Implementation

Pure Python stdlib, single file, no numpy/scipy.
`/Users/grey/Downloads/quran/analysis/zipf_per_surah_run.py`

Key pieces:
- `parse_morphology()` — yields (s, v, w, seg, lemma) from the QAC 0.4
  morphology file, filtering to STEM lines with LEM:.
- `zipf_fit_from_counts()` — OLS log-log slope → α.
- `bootstrap_alpha()` — N resamples with replacement; returns 2.5 / 97.5
  percentiles and median.
- `spearman_rho()` — with tied-rank averaging.
- Permutation p via shuffling the rev-order label vector.
- Residualization on log(n_tokens) for partial correlations.

Total runtime ~3 minutes on my laptop (bootstrap is the bottleneck).

## 4. Sanity check — whole-Quran α

First thing I did after parsing was pool all 74 608 lemma tokens and
refit the whole-Quran α. Got **α = 1.3177, R² = 0.9754, 4 832 distinct
lemmas**. Matches info-theory's published 1.318 to 4 decimals. Pipeline
is confirmed correct.

## 5. First-look surprise

I expected to see some length confound but I was not prepared for
Spearman ρ(α, n_tokens) = **+0.962**. Alpha is almost a deterministic
function of how many tokens the surah has.

Looking at the top 10 α: Al-Baqarah, An-Nisa, Al-Imran, Al-An'am,
Al-Ma'idah, Al-A'raf, At-Tawbah, Yunus, Hud, Yusuf. These are **the ten
longest surahs in the Quran by lemma count**, in almost exactly length
order. Every one has ≥ 1 696 tokens.

Looking at the bottom 10 α: Al-A'la (α=0.29), Al-Balad (0.31), Al-Layl
(0.33), 'Abasa (0.33), At-Takwir (0.35), Al-Buruj (0.38), Al-Ghashiya
(0.40), Al-Inshiqaq (0.41), An-Nazi'at (0.41), An-Naba (0.43). These
are **the short Meccan oath-cluster surahs** — exactly the surahs that
H14 predicted would have α > 1.5. They actually sit at α ≈ 0.3-0.4.

So H14 is wrong not by a little — it is wrong **in direction and by a
factor of 3-5x in magnitude**. The predicted α > 1.5 for oath-cluster
surahs is nowhere in the data.

## 6. Why the H14 intuition was wrong

I initially thought there must be an error in my fit, because the
oracular short surahs are famously rhetorically concentrated. I spent
~15 minutes double-checking the OLS code, verifying the whole-Quran
sanity anchor, and spot-checking a couple of per-surah fits by hand.
No bug.

Then I realized the conceptual issue. H14 conflates two different
distribution properties:

1. **Type-token ratio** — how much repetition there is. Short oracular
   surahs DO have high TTR. Al-Kafirun has 21 tokens and 8 distinct
   types; TTR = 0.38. The chrono-revelation agent already flagged
   ttr_lemma as dropping from 0.72 (Early Meccan) to 0.37 (Late
   Meccan). The concentration is real.

2. **Zipf α** — the slope of log-rank vs log-freq. This measures the
   *tail shape*, not the concentration. For a 20-token surah, the
   frequency distribution is dominated by 1s with a handful of 2s
   (nearly everything is a hapax). The log-log slope is **very
   shallow** because `log(freq)` barely varies across ranks. For a
   5 000-token surah, the frequency distribution has a real tail with
   counts ranging from 1 to ~400+, and the log-log slope is **steep**.

This is a textbook small-sample bias of OLS Zipf fits. The asymptotic
α is recovered only when you have enough tokens to populate the tail.
The whole-Quran α = 1.32 is the **asymptotic** property of the full
corpus; no individual surah can reach it because no individual surah
has enough tokens.

In hindsight this should have been flagged in the H14 design. The
deep-pattern agent who wrote H14 wasn't thinking about finite-sample
OLS bias; they were thinking "concentrated text → high α" which is a
clean intuition at infinite sample but backwards at small sample.

## 7. Insufficient-data inspection

24/114 surahs have < 50 distinct lemmas. Almost all of them are the
exact oracular-oath-cluster surahs H14 predicted to have α > 1.5.
Under the task's ≥ 50 rule I correctly return them as
`insufficient-data`. But as a sanity check I relaxed the threshold to
≥ 10 distinct lemmas and re-fit the 20 surahs that survive. The
resulting α values run **0.13 to 0.53**, with R² values in the 0.4-0.9
range. So even under the relaxed rule there is no surah in the
oracular cluster with α anywhere near the predicted 1.5. The
prediction has zero supporting data at any threshold.

I report this as an explicit §7 supplementary exploration, flagged as
out-of-original-rule.

## 8. Is there any residual signal after length control?

Yes, but small and opposite to H14. Partial Spearman ρ(α, rev_order |
log_tokens) = **+0.397**. Within each of 5 length bins the Spearman ρ
is positive (ranges +0.10 to +0.66, 4/5 bins ≥ +0.15). The direction
is consistently "later revelation → steeper α," i.e. Medinan > Early
Meccan.

Nöldeke phase means (valid surahs only):
- Early Meccan 0.470 → Middle 0.693 → Late 0.783 → Medinan 0.720

This mirrors the `ttr_lemma` U-shape from chrono-revelation exactly
(0.72 → 0.46 → 0.37 → 0.45 in their units, which inverts ours since
higher TTR = more hapaxes = flatter Zipf). The two metrics are telling
the same story, just with opposite direction conventions. The residual
per-surah α signal is not a *new* diachronic finding; it is a
restatement of a known ttr_lemma ramp under a Zipf-fit lens.

## 9. Cross-baseline reconciliation

The task asks whether the finding survives "when the whole-Quran α
recomputed under the same rule comes out to match cross-baseline's
0.97." Answer: it doesn't need to match 0.97 because cross-baseline's
0.97 is a **word-token** rule, not a lemma rule. Under the lemma rule
(same as info-theory and this analysis), the whole-Quran α comes out
to 1.32, not 0.97. These are different rule-tuples and not meant to
agree.

The cross-baseline "Quran Zipf isn't distinctive" verdict is therefore
specifically about *word-token* Zipf. It is silent on *lemma* Zipf. A
proper test requires morphologically tagging the Bukhari/Sira/Jahiz
baselines, which neither cross-baseline nor I have done. This is the
#1 follow-up I flag in the findings file §13.

## 10. Final verdict

**H14 rejected in the direction stated.** The hypothesis is falsified:
- Early Meccan ≠ high α (actually lowest α among phases)
- Medinan ≠ flat α ≈ 1.1 (actually highest α ≈ 0.72)
- Highest-α surahs are NOT the oracular oath-cluster (they are the
  longest Medinan narrative/legal surahs)
- The per-surah α heterogeneity is 96% explained by length (Spearman
  ρ = +0.962)
- Residual length-controlled signal (+0.40) is in the opposite
  direction to H14

**Second-order takeaway:** Zipf α is a tail-shape statistic, not a
concentration statistic. Any hypothesis that treats it as a proxy for
"how repetitive is this text" is mistyping the metric. For a small
surah the right concentration measure is TTR or entropy, not Zipf α.

## 11. Outputs

- `findings/phase-b-hypotheses/zipf-per-surah.md` — full finding writeup
- `findings/phase-b-hypotheses/csv/zipf-per-surah.csv` — per-surah table
- `findings/phase-b-hypotheses/csv/zipf-per-surah-results.json` — JSON summary
- `analysis/zipf_per_surah_run.py` — reproducible script
- `journal/zipf-per-surah-run-1.md` — this file

## 12. Follow-up hypotheses to queue

1. **H14b (directional flip).** Per-surah lemma Zipf α *controlling for
   log(n_tokens)* rises through Nöldeke phases with residual Spearman
   ρ ≥ +0.3. This is the honest restatement of the observed residual
   signal; it should be pre-registered against Bukhari-chunk baselines.
2. **H14c (Zipf α is length-determined in Arabic prose generically).**
   Compute per-chunk α under identical rules on length-stratified
   Bukhari / Sira / Jahiz slices; the curve α-vs-log-length should be
   shared between Quran and baseline. Effect: the per-surah α
   heterogeneity is a generic Arabic property, not Quran-specific.
3. **H14d (pooled per-phase fit).** Pool all lemmas within each
   Nöldeke phase (5k-15k tokens each); fit one α per phase. This
   removes per-surah small-sample noise and gives a clean 4-number
   diachronic Zipf statement under identical sample-size regimes.
4. **H14e (juz' stratification).** Partition the Quran into 30 juz'
   (each ~2 500 lemma tokens) and fit one α per juz'. Reduces the
   length-confound by holding sample-size roughly constant.
5. **H14f (info-theory headline under §1.4 null).** Promote the
   whole-Quran α = 1.32 claim to a §1.4 stringent-null test: morph-tag
   a length-matched Bukhari slice, re-fit α under the lemma rule,
   report delta. THIS is the test that would turn the info-theory §4
   headline into a §3 finding.

## 13. Reflection

I think this run is a useful negative-result data point. H14 was
written by the deep-pattern meta-reasoner as "the single best
Liberman-voice hypothesis" and marked HIGH priority. It turned out to
be wrong in a way that is intellectually informative: the metric was
mistyped. This is exactly the kind of thing a pre-registration and
clean execution should catch — and did.

The small-sample OLS-Zipf bias is a well-known issue in
computational-linguistics literature but it apparently wasn't on the
radar when H14 was designed. Worth a one-paragraph note in
`methodology.md` warning future agents not to use per-surah Zipf α as
a concentration metric.

The silver lining: a clean null result against a HIGH-priority
hypothesis is exactly what the deep-pattern loop needs to recalibrate.
I recommend upgrading H14's status in the queue from "open" to
"tested → rejected with directional evidence," and promoting H14c
(length-matched Bukhari baseline) to the next wave's priority slot.
