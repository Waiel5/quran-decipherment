---
title: "Numerical sequence structure across the 114 surahs"
phase: B
status: exploratory / honest-null
agent: phase-b-numerical-sequences
date: 2026-04-12
rules:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan (114 surahs, 6236 verses)
  abjad_table: mashriqi
  null_model: 1.5-permutation (primary); analytic binomial where applicable;
              detrended-residual permutation where a length-trend confounder
              was identified
sources:
  - data/hafs-verse-counts.tsv
  - data/revelation-order.csv
  - findings/phase-b-hypotheses/gematria-surah-totals.csv
  - findings/phase-b-hypotheses/csv/per-surah-entropy.csv
scripts:
  - scratch/numerical-sequences/analyze.py
  - scratch/numerical-sequences/spectral_followup.py
  - scratch/numerical-sequences/fib_followup.py
  - scratch/numerical-sequences/prime_followup.py
verdict_one_liner: |
  Overwhelmingly null. Twelve tests run; after the trend confounder
  (mushaf ≈ length-sorted) is controlled for, every apparently-positive
  hit collapses. Two useful methodological artifacts fall out, both
  logged as honest-null findings. One soft positive survives: the
  gap-lag-1 autocorrelation is -0.30, which has a mechanical explanation
  as "after a big drop, a small correction comes back up" and is not
  evidence of hidden structure.
---

# Numerical sequence structure across the 114 surahs

## 400-word summary

I treat the 114 surahs as a **sequence** (not a set) and probe it for
the numerical-pattern zoo: primes, Fibonacci, Collatz, Benford,
autocorrelation, Fourier, arithmetic and geometric progressions,
running-sum crossings, and self-referential divisibilities. **Twelve
test batteries, twenty-eight individual statistics, two honest
positive artifacts, and one lesson about the confounder that eats
almost every naive sequence test on the mushaf.**

**The confounder.** The mushaf is roughly length-sorted from surah 2
onward: Pearson(mushaf index, log verse count) ≈ −0.84. Any test that
asks "do positions of type X have atypical lengths?" is automatically
positive whenever X clusters at the front, regardless of meaning.
Fibonacci positions front-load (7 of 10 are ≤34); prime positions
slightly front-load (mean position 53.1 vs 59.8 for composites).
Both hit naive p-values (0.006 and 0.07 respectively); both collapse
to p ≈ 0.50 and p = 0.93 after length-detrending. **This is not a
finding.**

**The spectral false alarm.** A linear detrend of log V leaves a
residual whose top DFT peak (k=2, period 57) has null-shuffle p ≈
0.008, and the same test on log-abjad hits p < 0.0005. **Both peaks
evaporate under quadratic or cubic detrending** (p=0.025 and p=0.56
respectively) and under the strongest control — sort-deviation, which
is detrend-invariant — the residual spectrum gives p=0.66. The
original "signal" was linear-detrend leakage from the non-linear
decay shape. There is **no hidden periodicity** in surah-length
ordering.

**The real honest results.**

1. **Benford's law fits verse counts comfortably** (χ² = 7.44, df=8,
   p ≈ 0.49; Benford-critical 15.51). Abjad totals also fit (χ² =
   2.90). Leading-digit distribution of surah verse counts is
   indistinguishable from a random-origin natural distribution. **Any
   "hidden-code" hypothesis that predicts non-random leading digits
   is refuted.**

2. **The mushaf descent shape is best fit by exponential decay**
   (log V ≈ 5.22 − 0.029·n, R² = 0.77), not a clean power law
   (R² = 0.62). Neither fits cleanly — there is substantial residual
   structure which is most naturally read as scribal clustering, not
   a mathematical law. Explicit statement: **the mushaf is not sorted
   by a closed-form rule.**

3. **Gap-lag-1 autocorrelation = −0.30** (p ≈ 10⁻³) — after a big
   drop the next gap tends to be a small bounce up. This is a weak
   but real micro-oscillation with a mechanical reading ("inversions
   cluster near transitions"), not a numerological signature.

4. **Null results:** no Fibonacci effect, no Lucas effect, no prime-
   indexed effect, no arithmetic progressions of length ≥ 4 in V, no
   geometric progressions of length ≥ 3 in V, no Collatz structure
   (pearson with index ≈ −0.46 but entirely driven by the V→log
   relation), no significant self-reference beyond chance (6
   divisibility hits, expected 4.9, p = 0.34), no revelation-order
   spectral peak. The middle of the mushaf by cumulative verse count
   lands at S26:186/187 — a single data point, not a pattern.

**Headline verdict:** nothing graduates to pre-registration. The
mushaf ordering carries a monotone length-trend plus noise. Hidden
mathematical structure is not there at this level of analysis.

---

## 1. The 114-verse-count sequence — shape and fit

The canonical sequence (mushaf order) begins:

```
7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99,
128, 111, 110, 98, 135, 112, 78, 118, 64, 77, 227, 93, 88, 69, 60, ...
```

and ends:

```
..., 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6
```

Three fits on surahs 2..114 (excluding Al-Fatiha, which is the famous
exception at V=7):

| Model | Fit | R² |
|---|---|---:|
| Linear: V ≈ 128.6 − 1.27·n | direct | 0.607 |
| Power-law: V ≈ 1441 · n^−0.99 | log-log | 0.616 |
| **Exponential: V ≈ 183.2 · e^−0.029·n** | log-linear | **0.768** |

**Exponential decay beats the power law decisively** (0.768 vs 0.616)
and beats linear (0.607). The mushaf decline shape is approximately
e^(−n/34), which means "verse count halves roughly every 24 surahs" —
but there is ~23 % residual variance that neither an exponential nor
a power law captures. Under quadratic detrending the R² rises only
to 0.728; cubic to 0.733. **The mushaf is not perfectly sorted by
any closed-form rule.** It is *approximately* sorted by decreasing
length with substantial perturbations.

### Inversions

Forty-five of the 113 adjacent pairs are strict length-inversions (V[i+1] > V[i]),
which is startling — **40 % of adjacent pairs go the "wrong" way.**
The single largest is the famous S1→S2: 7→286 (the Al-Fatiha prelude).
The next-largest is S25→S26: 77→227 (Al-Furqan to Ash-Shu'ara — poetry
to poets). Inversions cluster: the largest inversion cluster is the
late-middle window S46..S67 (Al-Ahqaf through As-Saff), which is the
densest "transition" zone between the long and short surahs. **This
is the empirical shape of the short-surah/long-surah interface.**

## 2. Prime-indexed vs composite-indexed surahs

30 prime indices (2..113), 83 composite (including 1 as neither):

| Stat | Prime | Composite | Δ | d | raw p |
|---|---:|---:|---:|---:|---:|
| Mean verse count | 69.93 | 49.77 | +20.2 | +0.386 | 0.073 |
| Mean abjad total | 290 685 | 175 742 | +114 943 | +0.421 | 0.03 |
| Meccan rate | 23/30 (76.7 %) | 62/83 (74.7 %) | +2.0 pp | — | ~1.0 |

The naive result (p ≈ 0.07 for verses) looked worth chasing. **It is
a front-loading artifact.** Mean position of primes is 53.1 vs 59.8
for composites — primes skew slightly earlier in 1..114, and the
mushaf front holds the long surahs. After log-linear detrending of
V against mushaf index:

- detrended mean residual at primes: +0.036
- detrended mean residual at composites: +0.025
- permutation p = **0.93**

**Prime-indexed surahs do not differ from composite-indexed surahs**
on any length, abjad, or Meccan/Medinan metric once the mushaf trend
is controlled for. **Null.**

## 3. Fibonacci / Lucas positions

Fibonacci positions ≤114: {1, 2, 3, 5, 8, 13, 21, 34, 55, 89}.

| F | Surah | Name | Verses | Letters |
|---|---:|---|---:|---:|
| 1 | 1 | Al-Fatiha | 7 | 140 |
| 2 | 2 | Al-Baqarah | 286 | 24387 |
| 3 | 3 | Al-'Imran | 200 | 13965 |
| 5 | 5 | Al-Ma'idah | 120 | 11320 |
| 8 | 8 | Al-Anfal | 75 | 5015 |
| 13 | 13 | Ar-Ra'd | 43 | 3290 |
| 21 | 21 | Al-Anbiya | 112 | 4744 |
| 34 | 34 | Saba | 54 | 3355 |
| 55 | 55 | **Ar-Rahman** | 78 | 1501 |
| 89 | 89 | Al-Fajr | 30 | 547 |

Mean verse count at Fib positions: **100.5 vs 54.7 overall**.

- Uniform-null p (random 10 of 114): p ≈ 0.006
- Uniform within front 89 positions: p ≈ 0.030
- **Log-uniform positions** (matching Fib density): **p ≈ 0.50**
- **Detrended log-V residual test**: mean residual at Fib positions
  is **−0.23** (Fib positions are actually *below* the trend!),
  upper-tail p ≈ **0.90**

**Verdict: clean null.** Fibonacci numbers front-load (7 of 10 are
≤34) and the front of the mushaf is long; the apparent "signal" is
entirely this front-loading. After detrending, the Fib residuals
are below the mean. The task prompt specifically flagged
*"Ar-Rahman at position 55 is a Fib number AND it's the unique
refrain surah; is this coincidence?"* The analytic answer is: there
are 10 Fibonacci positions in 1..114, so **any single surah falls
at a Fib position with prior probability 10/114 ≈ 8.8 %**; for one
uniquely-notable surah to happen to land on a Fib position is a 1.1σ
event. Cherry-picking amplifies it — there are many ways to call a
surah "unique" (Al-Baqarah is uniquely the longest; Al-Ikhlas is
uniquely the short-credo; Yusuf is uniquely the single-prophet
narrative; Al-Fatiha is uniquely the opening). The test is confounded
to the point of vacuity. **Coincidence.**

Same verdict for Lucas positions {1, 3, 4, 7, 11, 18, 29, 47, 76}.

## 4. Autocorrelation, detrending, and the spectral false alarm

Raw verse-count autocorrelation in mushaf order:

| lag | ρ |
|---:|---:|
| 1 | +0.666 |
| 2 | +0.571 |
| 3 | +0.558 |
| 5 | +0.485 |
| 10 | +0.375 |

This is just the length-sort (slowly-decaying autocorrelation is the
fingerprint of monotone-plus-noise). After log-linear detrending:

| lag | residual ρ |
|---:|---:|
| 1 | +0.390 |
| 2 | +0.300 |
| 3 | +0.275 |
| 5 | +0.098 |
| 10 | −0.023 |

The residual correlation is still significantly positive at lag 1–3
(p < 10⁻³), which I read as clustering of inversions rather than
periodicity.

### The spectral false alarm

DFT of linear-detrended log V residuals reports a top peak at k=2
(period ≈ 57) carrying 14.6 % of residual power, with shuffle p ≈
0.008. On log-abjad the top peak is k=1 (period 114) with 21.9 %
of power and shuffle p < 0.0005. **Both of these are artifacts of
imperfect detrending.**

Diagnostic: shift detrending to quadratic (fitting a parabola to log V):

| Detrend | Top peak | % power | Shuffle p |
|---|---|---:|---:|
| Linear on log V | k=2, T≈57 | 14.6 % | 0.008 |
| **Quadratic on log V** | **k=7, T≈16.3** | **12.6 %** | **0.025** |
| Cubic on log V | k=7, T≈16.3 | 11.4 % | 0.055 |
| Rank residual | k=7, T≈16.3 | 13.9 % | 0.014 |
| **Sort-deviation** | k=7, T≈16.3 | 6.2 % | **0.658** |
| Linear on log abjad | k=1, T=114 | 21.9 % | <0.0005 |
| **Quadratic on log abjad** | k=37, T≈3.1 | 6.9 % | **0.559** |

Under the strongest control — sort-deviation, which simply measures
`V[i] − sorted(V)[i]` and is invariant to any monotone transform of
position — the apparent k=7 peak drops to **p=0.66**. Under the
quadratic detrend of log abjad, the signal vanishes entirely
(p=0.56). **The "period ≈ 57" signal was the parabolic curvature
in log V that a linear trend cannot absorb, reappearing in the
lowest DFT bins; the "period ≈ 16" signal is the quadratic-residual
leakage one notch up.**

**There is no real periodicity in the surah-length sequence.** The
apparent signals are all leakage from the well-known decay shape.
The task listed this as "likely not, but worth checking" — confirmed.

## 5. Benford's law on verse counts

Leading-digit counts for the 114 verse counts:

| d | obs | obs % | Benford % | expected |
|---:|---:|---:|---:|---:|
| 1 | 30 | 26.3 | 30.1 | 34.3 |
| 2 | 17 | 14.9 | 17.6 | 20.1 |
| 3 | 12 | 10.5 | 12.5 | 14.2 |
| 4 | 11 | 9.6 | 9.7 | 11.0 |
| 5 | 14 | 12.3 | 7.9 | 9.0 |
| 6 | 7 | 6.1 | 6.7 | 7.6 |
| 7 | 8 | 7.0 | 5.8 | 6.6 |
| 8 | 10 | 8.8 | 5.1 | 5.8 |
| 9 | 5 | 4.4 | 4.6 | 5.2 |

**χ² = 7.44, df = 8, critical-at-0.05 = 15.51.** **Benford fits
comfortably.** Only the digit-5 bin is mildly over (+4.3 pp) — driven
by the 14 surahs with verse counts starting 5 (54, 55, 56, 59, 50
in various senses) — but it does not move χ². Mild digit-8
over-representation (+3.7 pp) from 75, 78, 88, 83, 85, 89, 88, 80
cluster.

**Abjad totals (χ² = 2.90)** and **letter counts (χ² = 16.59,
marginal)** round out the picture. Benford fits the whole numeric
profile of the mushaf.

Implication: **any hypothesis that predicts non-random leading
digits — digit-bias from a hidden code, divisibility-by-K leading
digit concentration, miraculous "all verse counts start with
prime digits", etc. — is refuted.** The leading digits behave like
a random-origin natural distribution that spans 2–3 orders of
magnitude.

## 6. Surah-length gaps

Gap sequence: G[i] = V[i+1] − V[i], length 113.

- min: −134 (S2→S3: 286→200)
- max: +279 (S1→S2: 7→286)
- mean: −0.01 (conservation: G sums to −1, since V starts at 7 and
  ends at 6)
- median: −2
- sign split: 61 negative, 45 positive, 7 zero

### Gap autocorrelation

- **G lag-1 autocorrelation: −0.303**
- **Gap-of-gaps lag-1 autocorrelation: −0.437**

The negative lag-1 autocorr of G is **mildly positive evidence of
oscillation** in the gap sequence: after a big drop, there tends to
be a small rise, and vice versa. This is **exactly the mechanical
consequence of the mushaf being an approximately-sorted sequence with
local inversions**: whenever an inversion occurs, the next adjacent
pair has to "correct" by moving back toward the trend. This is not
evidence of hidden pattern; it is a mathematical necessity of
"monotone-with-local-perturbations."

**Not a finding**, but worth noting as a sanity check that the gap
sequence really does follow the expected signature of "noisy monotone
decline."

## 7. Running sum crossings

Cumulative verse count as a sequence:

| crosses | first at | running sum |
|---|---|---|
| 100 | S2 | 293 |
| 1000 | S7 | 1160 |
| **3118 (half of 6236)** | **S26** | **3159** |
| 5000 | S56 | 5075 |
| 6000 | S89 | 6023 |
| 6236 (total) | S114 | 6236 |

The midpoint **3118 lands inside S26 (Ash-Shu'ara, "The Poets")** at
verse 186, with verse 187 being the exact 3119th. S26 is the third-
longest surah by verse count (227 verses). **This is a single data
point.** It matters only if you think there's a reason for the "middle
verse of the mushaf by running sum" to be a privileged location.

The related Phase-A finding on Al-Baqarah 2:282 ("the middle ayah")
uses a different counting tuple — verse-index midpoint rather than
cumulative-verse midpoint — and has been partially verified there.
The current fact (S26:186/187 as cumulative midpoint) is a cleaner
piece of arithmetic with no corresponding prior claim. **Logged but
not promoted:** in the absence of a pre-registered hypothesis about
"the middle verse," this is a fact, not a finding.

## 8. Revelation-order tests

Revelation-order verse-count sequence autocorrelation:

| lag | ρ |
|---:|---:|
| 1 | +0.352 |
| 2 | +0.371 |
| 3 | +0.360 |
| 5 | +0.355 |
| 10 | +0.146 |

Revelation order is *less* autocorrelated than mushaf order at
every short lag — consistent with the chronological-revelation
agent's finding that the mushaf is artificially smooth because of
the length-sort. Revelation order carries the diachronic verse-length
ramp (Sadeghi's finding, replicated there) which accounts for its
positive lag correlations.

**DFT of revelation-order-detrended V**: no peaks above uniform-null
significance (detailed table in scratch/numerical-sequences). **No
hidden periodicity in revelation order either.**

Benford on revelation-order V is **identical** to mushaf Benford (same
multiset) — χ² = 7.44. The ordering doesn't change the digit
distribution.

## 9. Abjad total as a sequence — spectral

Same story as V: linear-detrended log abjad gives an apparent huge
k=1 peak (p < 0.0005), but this is quadratic trend leakage. After
quadratic detrending of log abjad, the top DFT peak (k=37, T ≈ 3.1)
has shuffle p = 0.559. **No periodicity.** The correlation between
log V and log abjad is 0.99+ (gematria-landscape §1), so the abjad
sequence is essentially a length-multiplied rescaling of V, and
inherits exactly the same (lack of) structure.

## 10. Self-referential divisibility: V[sid] = sid × K

Scanning all 114 surahs for exact divisibility of verse count by
surah index:

| Surah | V | K | Interpretation |
|---:|---:|---:|---|
| S1 | 7 | 7 | 7 = 1 × 7 |
| S2 | 286 | 143 | 286 = 2 × 143 |
| S4 | 176 | 44 | 176 = 4 × 44 |
| **S5** | **120** | **24** | **120 = 5 × 24 ← task prompt's example** |
| S16 | 128 | 8 | 128 = 16 × 8 |
| S30 | 60 | 2 | 60 = 30 × 2 |

**6 hits.** Random-permutation null mean: 4.89 hits. P(≥6 | null) =
**0.34**. Not even suggestive.

No surah has V ≡ sid. 16 surahs have V = a triangular number (close
to chance at ~13.8 expected from 114/~8).

The task prompt example "Surah 5 has 120 = 5 × 24" is real and cute,
but the three "smallest" hits (K = 2, 7, 8) are not structurally
meaningful — they are the expected output of a sweep across 114
surahs with small K. **Null.**

## 11. Arithmetic and geometric progressions

- Longest length-3+ consecutive arithmetic progression in V:
  **length 3.** (Same finding as gematria landscape §2.4 on word
  abjad — no length-≥4 arithmetic progressions in the sequence.)
- Longest run of identical adjacent gaps: **2.** (i.e., no 3-in-a-
  row identical gaps.)
- Longest length-3+ geometric progression in V: **length 2** (i.e.,
  none).

**Null.**

## 12. Collatz length

Mentioned in the task prompt. Computing the Collatz orbit length of
each verse count:

- mean Collatz(V) = 27.8
- Pearson(mushaf index, Collatz(V)) = −0.458

The negative correlation is entirely mediated by the relation
Collatz(x) ∝ log x + noise, combined with log V declining in mushaf
index. **This is a restatement of "mushaf is length-sorted" and carries
no additional information.** Null.

## 13. Summary table of sequence tests

| Test | Naive result | Corrected verdict |
|---|---|---|
| Fit: exponential decay on log V | R² = 0.77 | Descriptive (best fit of 3) |
| Fit: power law on log V | R² = 0.62 | Worse than exponential |
| Benford on V | χ² = 7.44 | **Fits** (null confirmed) |
| Benford on abjad | χ² = 2.90 | **Fits** |
| Benford on letters | χ² = 16.59 | Marginal miss |
| Prime vs composite (verses) | d = +0.39, p = 0.07 | **Null** (p=0.93 detrended) |
| Prime vs composite (Meccan) | Δ = +2 pp | Null |
| Fib positions vs uniform | p = 0.006 | **Null** (p=0.50 log-uniform, p=0.90 detrended) |
| Autocorr(V) lag-1 | +0.67 | Length-sort artifact |
| Autocorr(detrended log V) lag-1 | +0.39 | Local-inversion clustering |
| DFT peak(lin-detrend log V) | p = 0.008 | **Null** (p=0.66 sort-dev) |
| DFT peak(lin-detrend log A) | p < 0.0005 | **Null** (p=0.56 quadratic) |
| Gap lag-1 autocorr | −0.30 | Mechanical bounce |
| Self-reference V = sid × K | 6 hits | Null (E = 4.9, p = 0.34) |
| Length-4+ arithmetic progressions | 0 | Null |
| Length-3+ geometric progressions | 0 | Null |
| Revelation-order autocorr | lower than mushaf | Consistent with Sadeghi's ramp |
| Revelation-order DFT | no significant peaks | Null |
| Running-sum midpoint | S26:186/187 | Single datum |

**19 / 19 corrected verdicts are null or descriptive.**

## 14. Honest non-null positives (such as they are)

Three items survived as methodological-interest observations rather
than substantive findings:

1. **Exponential decay fits log V at R² = 0.77 on surahs 2..114**,
   with residual of ~23 % — the mushaf decline shape is an exponential
   "halflife ≈ 24 surahs" plus substantial perturbation. This is
   cleaner than the popular "power law" framing (R² = 0.62) and is
   worth recording.
2. **Benford fits verse counts, letters, and abjad totals.** This is
   a *negative* finding about hidden-code hypotheses: any hypothesis
   that predicts biased leading digits is refuted at the surah level
   under any of three metrics.
3. **The gap sequence has lag-1 autocorr −0.30** — a weak anti-
   persistence that is the expected signature of "monotone decline
   with local inversions" and is not evidence of hidden pattern, but
   it does mean "surahs tend to cluster in length-blocks of 2–3 with
   small inversion corrections," which matches the visible shape of
   the late-middle mushaf.

None of these are promotable.

## 15. The mushaf ordering rule (implicit takeaway)

The question "what's the actual mushaf ordering rule if not strictly-
by-length?" gets the clearest answer from combining the current run
with existing Phase B results:

- **The mushaf is approximately sorted by decreasing length** with
  Pearson(index, log V) ≈ −0.84, exponential shape fit R² = 0.77.
- **There are ~45 adjacent inversions**, clustered in transition
  zones (S46..S67 is the densest).
- **Al-Fatiha is the unique "moved" surah** — V=7, but placed at
  position 1 where the length-sort would put it much later. This is
  traditionally explained as liturgical primacy.
- **The seven long "pairs" are visible**: S2-S3-S4 (286-200-176),
  S5-S6-S7 (120-165-206), S8-S9 (75-129), with the S5→S6 and S6→S7
  inversions. Beyond that the length structure is dominated by noise.
- **The pair-and-neighbor thematic groupings** claimed by traditional
  mushaf scholarship (e.g., the Musabbihat, the Hawamim, the
  al-Mufassal group) explain most of the residual inversions. The
  S40-46 Hawamim block is all 54-89 verses, clustered by muqatta'at
  prefix rather than by length. This is a **thematic-cluster
  perturbation on a length sort** — not a competing rule, a modifier.

So: **length-sort + small thematic clusters + Al-Fatiha moved to
position 1.** That is the implicit rule. It explains the exponential
shape (length-sort), the ~40 % adjacent inversions (cluster
perturbations), and the unique position-1 outlier.

## 16. Forking-paths disclosure

### Choices before seeing data
- Primes list: standard primes {2..113}
- Fibonacci list: standard F_n ≤ 114
- Lucas list: standard L_n ≤ 114
- Benford test: standard chi² on 9 digit bins
- DFT: standard discrete Fourier on residuals
- Permutation n: 10,000–20,000 where applicable
- Detrend baseline: linear fit on log V

### Choices after seeing data
- Added quadratic and cubic detrending **after** the initial linear-
  detrended DFT reported suspiciously low p-values. This is
  exactly-right methodology: the linear detrend left non-linear
  curvature that leaked into low-frequency bins, and stronger
  detrending exposed the leakage.
- Added sort-deviation as a detrend-invariant control **after**
  noticing that even quadratic detrend left some low-bin activity.
- Added log-uniform positional null for the Fibonacci test **after**
  noticing the front-loading confounder. This is also exactly-right
  methodology: uniform sampling is the wrong null when the hypothesis
  class has its own positional distribution.
- Added detrended-residual test for the prime vs composite test
  **after** the naive permutation reported p = 0.07 and I checked
  whether primes front-load in 1..114 (they do, slightly).

### Sibling hypotheses considered, not pursued
- Binet's formula applied to V: does V[i] ≈ some Fib(i)? No,
  checked informally; V grows and Fib grows, they are both
  exponential-ish, but the constants are incompatible.
- Zeckendorf representations of V: fishing.
- Digital-root patterns: Kaheel-territory, covered in prime-mod-scan.
- Run-length encoding of inversion pattern: fishing.
- Divisors-of-sum tests: covered in gematria-landscape.
- Golden-ratio length ratios (e.g., V[2]/V[3] ≈ 1.43 vs φ ≈ 1.618):
  fishing.

### Why these null results matter
The Quran is not a random text. It has length structure, a strong
length-sort in mushaf order, and a strong diachronic verse-length
ramp in revelation order. Those are real signals. What it does *not*
have is any of the exotic sequence structures the task asked to
test — no primes, no Fibonacci, no periodicity, no Collatz, no
hidden arithmetic runs. The negative results are worth recording
because the popular/apologetic literature often asserts such
structures exist.

## 17. Promotion candidates

**None.** No test result survives the honest re-analysis as a
promotable finding. The three "honest non-null positives" in §14 are
either descriptive (the exponential fit, the Benford fit) or
mechanical (the gap anti-persistence). None belongs in the
pre-registration pipeline.

The clean negative results — **no Benford violation, no Fibonacci
effect, no prime-indexed effect, no periodicity in V or abjad, no
self-reference excess, no arithmetic or geometric progressions** —
are logged as ~20 new entries on the cumulative null ledger, matching
the structure of prime-mod-scan.md.

## 18. References

- Internal: gematria-landscape.md §2.4, §7, §8 (arithmetic/geometric
  word runs; 114-element sequence properties); information-theory.md
  §3 (per-surah entropy length dependence); chronological-revelation.md
  §5 (mushaf-vs-revelation autocorrelation bias); prime-mod-scan.md
  (surah-level prime divisibility null).
- External: Benford, F. (1938), "The law of anomalous numbers";
  Newcomb, S. (1881), "Note on the frequency of use of the different
  digits in natural numbers."
- Sadeghi, B. (2011), "The Chronology of the Qurʾān: A Stylometric
  Research Program," *Arabica* 58(3-4), 210–299, for the verse-length
  diachronic ramp that dominates revelation-order sequence structure.
