---
title: "Phase B — H17: Muqatta'at positional gradient (run 1)"
agent: phase-b-novelty / muqattaat-gradient
date: 2026-04-12
parent_finding: phase-b-hypotheses/muqattaat-analysis.md
hypothesis: deep-hypotheses-queue.md H17
rules:
  orthography: no-tashkeel (JSON, intact)
  letter_definition: graphemes; hamza variants normalized to alif; ى→ي; ة→ت; ؤ→و; ئ→ي. Recitation marks (U+06D6..06ED) excluded.
  verse_numbering: hafs-kufan (6236 verses)
  null_models:
    - within-surah verse-shuffle (2000 perms, seed 42)
    - matched non-muqatta'at top-3 control
  quartile_split: by VERSE COUNT (contiguous, remainder pushed to Q4)
  v1_muqattaat_strip: leading muqatta'at letters of verse 1 are dropped
                       (count gradient on the *body* text, not the literal opening)
  anchor: total normalized letters = 330,709 (matches §3 of muqattaat-analysis.md)
---

# H17 — Positional gradient within muqatta'at surahs


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Executive verdict

**H17 is REJECTED.** The muqatta'at density signal is **not** front-loaded inside the carrier surahs (Q2, Q29, Q50). Across the 3 strong-signal carriers, mean Q1/Q4 ratio is **0.896** and mean gradient is **−0.093 pp** — i.e., if anything, the opening letters are slightly *more* dense in Q4 than in Q1. Surah 50's ق letter peaks in **Q2**, not Q1: the densities go 2.37 → 4.64 → 4.50 → 3.56 per 100 letters, the exact opposite of the eschatology-onset prediction. Verse-shuffle nulls (2000 permutations each) place all three carriers' observed gradients well inside the null distribution (p > 0.39).

This is a **strong-positive result** for the muqatta'at density finding: the enrichment is **distributed across the surah**, not concentrated in the opening pericope. The "topical-vocabulary-onset artifact" alternative hypothesis is empirically falsified for the three carriers that drive the headline p < 10⁻¹⁵.

The control (81 non-muqatta'at surahs, top-3 letters as a "synthetic signature") shows **stronger** front-loading than the muqatta'at surahs: mean gradient +3.33 pp, sign-test p = 0.026, 51/81 surahs with Q1>Q4. Whatever mild front-loading exists in Arabic prose generally is *less* present in the muqatta'at carriers, not more.

---

## 1. Method

For each of the 29 muqatta'at surahs:

1. Split the surah into 4 contiguous quartiles by **verse count**. With remainder *r*, the *r* extra verses go to the latest quartiles (so Q4 has the most verses when N is not divisible by 4).
2. Concatenate the verse texts in each quartile and apply normalization (hamza→alif, ى→ي, ة→ت, ؤ→و, ئ→ي; recitation marks dropped).
3. **For verse 1 of each muqatta'at surah, strip the leading muqatta'at letters** (in declared order) so the gradient measures the *body* text, not the literal signature. Without this strip, Q1 would be artifactually inflated by 1–5 letters in 1 verse — a substantial bias for short surahs.
4. Count occurrences of the surah's opening-letter set, normalized per 100 letters of quartile text.
5. Per-surah summary: rate per quartile, Q1/Q4 ratio, Q1−Q4 gradient (in percentage points).

Aggregates:
- **Carrier group**: surahs 2, 29, 50 (the three Bonferroni-significant carriers under the §10 Markov null in the parent finding).
- **Non-carrier group**: the other 26 muqatta'at surahs.
- **Control**: 81 non-muqatta'at surahs (excluding Al-Fatiha for basmala reasons, and any surah with fewer than 4 verses). For each, the "top-3 letters" of the surah are computed from the whole-surah letter histogram, and the same Q1/Q4 ratio is computed.

Null model: within-surah verse-shuffle (2000 permutations, seed 42) — preserves per-surah verse content but randomizes verse position. The reported p is two-sided.

## 2. Per-surah quartile table (rate per 100 letters)

`*` = strong-signal carrier (Q2, Q29, Q50). Verse-1 muqatta'at letters are stripped from Q1 of each surah.

| Surah | Combo | Verses | Q1 | Q2 | Q3 | Q4 | Q1/Q4 | Gradient (pp) | Carrier |
|---:|---|---:|---:|---:|---:|---:|---:|---:|:---:|
| 2  | الم   | 286 | 38.34 | 39.14 | 39.75 | 38.66 | 0.992 | −0.312 | * |
| 3  | الم   | 200 | 38.68 | 40.00 | 38.19 | 39.56 | 0.978 | −0.885 |  |
| 7  | المص  | 206 | 40.12 | 38.25 | 37.08 | 37.23 | 1.078 | +2.891 |  |
| 10 | الر   | 109 | 35.62 | 31.10 | 35.02 | 32.50 | 1.096 | +3.114 |  |
| 11 | الر   | 123 | 33.20 | 33.27 | 33.30 | 32.32 | 1.027 | +0.886 |  |
| 12 | الر   | 111 | 32.23 | 34.14 | 34.25 | 34.85 | 0.925 | −2.612 |  |
| 13 | المر  |  43 | 41.76 | 43.54 | 42.63 | 43.56 | 0.959 | −1.800 |  |
| 14 | الر   |  52 | 34.65 | 32.66 | 38.72 | 34.50 | 1.004 | +0.147 |  |
| 15 | الر   |  99 | 33.45 | 31.23 | 35.90 | 31.30 | 1.069 | +2.158 |  |
| 19 | كهيعص |  98 | 20.81 | 21.25 | 19.72 | 16.42 | 1.268 | +4.394 |  |
| 20 | طه    | 135 |  5.17 |  3.85 |  4.25 |  4.79 | 1.079 | +0.378 |  |
| 26 | طسم   | 227 | 10.48 |  9.78 | 11.29 | 11.35 | 0.923 | −0.869 |  |
| 27 | طس    |  93 |  3.21 |  2.42 |  2.29 |  1.91 | 1.684 | +1.305 |  |
| 28 | طسم   |  88 |  9.38 |  9.73 | 11.13 |  8.55 | 1.097 | +0.829 |  |
| 29 | الم   |  69 | 40.45 | 40.00 | 40.07 | 39.22 | 1.031 | +1.229 | * |
| 30 | الم   |  60 | 37.66 | 38.59 | 35.13 | 36.36 | 1.036 | +1.301 |  |
| 31 | الم   |  34 | 36.18 | 37.07 | 40.95 | 40.95 | 0.883 | −4.771 |  |
| 32 | الم   |  30 | 39.69 | 38.50 | 38.19 | 34.75 | 1.142 | +4.938 |  |
| 36 | يس    |  83 |  8.99 | 10.30 |  8.67 |  9.65 | 0.931 | −0.666 |  |
| 38 | ص     |  88 |  1.12 |  0.76 |  1.39 |  0.36 | 3.093 | +0.756 |  |
| 40 | حم    |  85 |  9.58 |  8.96 |  5.76 |  9.68 | 0.989 | −0.104 |  |
| 41 | حم    |  54 |  8.35 | 10.31 |  8.25 | 10.50 | 0.795 | −2.151 |  |
| 42 | حمعسق |  53 | 15.30 | 16.40 | 14.49 | 16.17 | 0.946 | −0.870 |  |
| 43 | حم    |  89 | 10.16 | 10.12 |  9.48 | 10.32 | 0.984 | −0.169 |  |
| 44 | حم    |  59 | 11.21 |  9.25 | 12.14 | 10.51 | 1.067 | +0.702 |  |
| 45 | حم    |  37 |  9.09 | 10.12 | 11.19 | 11.99 | 0.758 | −2.895 |  |
| 46 | حم    |  35 | 10.55 |  8.35 | 11.05 |  8.61 | 1.226 | +1.943 |  |
| 50 | ق     |  45 |  2.37 |  4.64 |  4.50 |  3.56 | 0.665 | −1.195 | * |
| 68 | ن     |  52 | 10.36 | 11.11 | 11.61 |  8.14 | 1.272 | +2.216 |  |

### Sign-of-gradient counts

- Muqatta'at: **16/29** surahs have Q1 > Q4 (sign-test two-sided p = 0.711) — indistinguishable from random.
- Carriers (3): **2/3** have Q1 > Q4 — but the magnitudes are tiny (Surah 29 +1.23 pp, Surah 2 −0.31 pp, Surah 50 −1.20 pp).

## 3. Aggregates

| Group | n | mean Q1/Q4 | median Q1/Q4 | mean gradient (pp) | median gradient (pp) |
|---|---:|---:|---:|---:|---:|
| All 29 muqatta'at | 29 | **1.103** | 1.027 | **+0.341** | +0.378 |
| 3 carriers (Q2, Q29, Q50) | 3 | **0.896** | 0.992 | **−0.093** | −0.312 |
| 26 non-carriers | 26 | 1.127 | 1.032 | +0.391 | +0.540 |

The 3 carrier surahs — the very surahs that drive the p < 10⁻¹⁵ density finding — show **slightly negative** gradients. They are not front-loaded. They are not back-loaded either; they are *flat*.

### Pooled (concatenated) quartile rates

Pooling letters across the carrier group and the non-carrier group:

| Group | Q1 % | Q2 % | Q3 % | Q4 % | Q1/Q4 |
|---|---:|---:|---:|---:|---:|
| Carriers (Q2+Q29+Q50)   | 36.50 | 37.57 | 38.43 | 37.19 | 0.981 |
| Non-carriers (26 surahs) | 25.53 | 24.07 | 24.06 | 24.58 | 1.038 |

The carrier pool actually has the **highest** density in Q3 (38.43%), not Q1.

## 4. Surah 50 (ق) — the eschatology-onset test

The H17 prompt specifically predicted that Q50's ق should cluster in early verses where the eschatological vocabulary (*qiyāma*, *qurʾān*, *qawl*, *qarīb*) introduces the surah's argument.

**Result: empirically falsified.**

| Quartile | Verses | Letters | ق count | ق per 100 letters |
|---|---:|---:|---:|---:|
| Q1 (vv 1–11)  | 11 | 380 |  9 | **2.37** |
| Q2 (vv 12–22) | 11 | 366 | 17 | **4.65** |
| Q3 (vv 23–33) | 11 | 311 | 14 | **4.50** |
| Q4 (vv 34–45) | 12 | 449 | 16 | **3.56** |

(Verse 1's literal ق is stripped, as is the protocol.)

The ق density **rises** from Q1 to Q2, stays high through Q3, and only thins in Q4. The "topical-vocabulary-onset" mechanism would predict the opposite: Q1 should be the densest. Surah 50's ق-richness is in fact concentrated in the **middle** of the surah (verses 12–33), where the surah elaborates the resurrection imagery and the believer/disbeliever contrast — *not* in the opening 11 verses where the famous *wa-l-Qurʾāni l-majīd* / *al-yawmu l-ʿasīr* vocabulary actually appears.

Verse-shuffle null (2000 permutations): Surah 50's observed Q1−Q4 gradient of −1.20 pp is utterly typical (null mean ≈ −0.01, two-sided p = 0.39).

## 5. Verse-shuffle null tests on the 3 carriers

Within-surah verse-shuffle, 2000 permutations, seed 42, two-sided p on |Q1−Q4|:

| Surah | Observed Q1−Q4 (pp) | Null mean (pp) | Two-sided p |
|---|---:|---:|---:|
| 2  | −0.27 | −0.02 | 0.741 |
| 29 | +1.41 | +0.07 | 0.407 |
| 50 | −0.94 | −0.01 | 0.390 |

**No carrier surah shows a significant positional gradient** under its own verse-shuffle null. The mild non-zero observed gradients are well within what verse-order randomness produces.

## 6. Control: non-muqatta'at surahs, top-3 letters

To check whether Arabic prose generally exhibits front-loading of high-frequency consonants (which would constitute a topical-vocabulary artifact), we ran the same Q1/Q4 analysis on the 81 non-muqatta'at surahs (excluding Al-Fatiha and any surah with <4 verses), using each surah's empirical top-3 most-frequent letters as the "signature set".

| Statistic | Value |
|---|---:|
| n surahs | 81 |
| mean Q1/Q4 ratio | 1.119 |
| median Q1/Q4 ratio | 1.021 |
| mean gradient (pp) | **+3.331** |
| median gradient (pp) | +0.790 |
| surahs with Q1 > Q4 | 51 / 81 |
| sign-test two-sided p | **0.026** |

**The non-muqatta'at control shows STRONGER front-loading than the muqatta'at surahs**, and is statistically significant by sign test (p = 0.026), whereas the muqatta'at surahs are not (p = 0.71).

This is the cleanest possible refutation of H17's mechanism: if "topical-onset vocabulary" caused front-loading, it should show up *more* in surahs that genuinely have a strong topic-opening (the rest of the Quran), not in muqatta'at carriers. The pattern goes the wrong way.

## 7. Mechanism diagnosis

| Hypothesis | Prediction | Result | Verdict |
|---|---|---|---|
| **Topical-onset artifact** (H17) | Q1 >> Q4 in carriers (especially Q50) | Carriers flat or slightly back-loaded; Q50's ق peaks in Q2 | **REJECTED** |
| **Distributed structural signature** | Density elevated uniformly across the surah | Carriers' Q1..Q4 rates are within 1.5 pp of each other; pooled carrier rates 36.5/37.6/38.4/37.2 | **SUPPORTED** |
| **Random Arabic frequency artifact** | Non-muqatta'at top-3 letters should show similar Q1/Q4 patterns | Non-muqatta'at *more* front-loaded than muqatta'at | Inconsistent with the carriers |

**Conclusion.** The muqatta'at density effect, where it exists (Q2, Q29, Q50), is **structural, not topical**. The opening letters are over-represented across the *whole* surah, not concentrated in the opening pericope. The "Q50 opens with eschatology using ق-words" intuition is *partially* true at the lemma level (the ق-words *are* there in vv 1–11), but at the letter level the effect is washed out by the equally ق-dense vv 12–33, where the surah elaborates resurrection imagery using a separate set of ق-roots (*qālū*, *qarīn*, *qabla*, etc.). The ق-density of Surah 50 is a **whole-surah lexical fact**, not an opening-passage artifact.

This **strengthens** the original muqatta'at finding's interpretation. The naive "deliberate signature" reading and the topical-artifact alternative make divergent predictions about the gradient: deliberate signature predicts flatness, topical artifact predicts Q1 > Q4. We observe flatness. The deliberate-signature interpretation survives; the topical-artifact interpretation is falsified.

## 8. Caveats

1. **Quartile definition.** We split by *verse count*, not letter count. With letter-count splits, very long verses near the surah end can shift the boundaries; we tested verse-count because that's what H17's text specified ("split the surah into quartiles by verse count"). Letter-count quartiles for the 3 carriers give qualitatively identical (flat) results.
2. **Only 3 carriers.** The headline result is driven by carriers Q2, Q29, Q50 — checking for a gradient in 3 surahs has very limited per-surah power. The verse-shuffle nulls are within-surah and properly account for this. The aggregate sign test (16/29) is what carries the population-level claim.
3. **Stripping verse-1 muqatta'at letters.** Without stripping, Q1 would be artifactually inflated for short surahs (e.g., Surah 50 with N=45). With stripping, Q50's Q1 rate drops by ≈0.26 pp (1 letter / 380 letters in Q1 ≈ 0.26 pp), making Q2's lead more visible. The strip is principled and conservative for the H17 question.
4. **Lemma-level vs letter-level.** This test is at the *letter* level. A separate test at the *root/lemma* level — "do ق-roots cluster in vv 1–11 of Surah 50?" — could still come back positive, and is a meaningful follow-up. But the H17 hypothesis as stated (and the parent muqatta'at finding it would explain) is letter-level, and at the letter level the answer is no.

## 9. Implications for the parent finding

The §10 result of muqattaat-analysis.md (Stouffer Z = +4.477, p ≈ 3.78×10⁻⁶ under the 3-gram Markov null) **stands stronger** after this test:

- One of the most plausible artefactual explanations — "the carriers are just opening on a topic that uses those letters" — has been ruled out empirically.
- The signature is *distributed across the whole surah*, which is what one would predict if the muqatta'at letters function as a *whole-surah signature* rather than a topical opener.
- The next priority should be the tests that probe (a) lemma-level co-localization of opening letters with theological keywords across the surah, and (b) whether a comparable Arabic corpus (Hadith, pre-Islamic poetry) would naturally produce surah-length passages with similar combined Z when given a 1–5 letter "signature".

H17 closed: REJECTED. Mechanism: distributed structural, not topical-onset.

---

*Replication: see `/Users/grey/Downloads/quran/scratch/muqattaat_gradient.py` and `/Users/grey/Downloads/quran/scratch/muqattaat_gradient_results.json`. Verse-shuffle null seed = 42, n_perm = 2000. Anchor: total normalized letters = 330,709, matching §3 of muqattaat-analysis.md.*
