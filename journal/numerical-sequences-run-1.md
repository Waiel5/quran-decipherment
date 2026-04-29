---
agent: phase-b-numerical-sequences
run: 1
date: 2026-04-12
phase: B
status: complete
output: findings/phase-b-hypotheses/numerical-sequences.md
---

# Journal — numerical-sequences run 1

## Task
Treat the 114 surahs as a sequence (not a set) and look for sequence
structure: primes, Fibonacci, Collatz, Benford, autocorrelation,
DFT, arithmetic/geometric progressions, running-sum crossings,
self-referential divisibilities, and revelation-order equivalents.

## What I did

1. Read master-index, gematria-landscape, information-theory,
   chronological-revelation, and prime-mod-scan for context and
   rules tuple.
2. Loaded: data/hafs-verse-counts.tsv, data/revelation-order.csv,
   findings/phase-b-hypotheses/gematria-surah-totals.csv,
   findings/phase-b-hypotheses/csv/per-surah-entropy.csv.
3. Wrote scratch/numerical-sequences/analyze.py (pure stdlib)
   running 12 task batteries on the 114-length V (mushaf), 114-length
   abjad, and 114-length revelation-order V sequences.
4. Noticed suspiciously-small p-values on the linear-detrended DFT
   (p ≈ 0.008 on V, p < 0.0005 on abjad) and on uniform-null
   Fibonacci (p ≈ 0.006) and prime-indexed (p ≈ 0.07) tests.
5. Wrote three follow-up scripts:
   - spectral_followup.py: quadratic, cubic, rank-residual, and
     sort-deviation detrending on V and abjad.
   - fib_followup.py: log-uniform positional null and detrended-
     residual null for Fibonacci.
   - prime_followup.py: detrended-residual null for prime vs
     composite.
6. All three "significant" naive results collapsed to null under
   correct trend controls.
7. Wrote findings/phase-b-hypotheses/numerical-sequences.md with
   complete YAML frontmatter, 400-word summary, 18 sections covering
   all 12 task items plus the honest-null discussion, spectral
   false-alarm analysis, and forking-paths disclosure.

## Key findings

### Headline result
**19 / 19 corrected verdicts are null or descriptive.** No result
graduates to pre-registration.

### The confounder
The mushaf is approximately length-sorted (Pearson(index, log V)
≈ −0.84). Any positional test on 1..114 that has its own positional
distribution (Fibonacci, primes) will report a false-positive
against a uniform null because the front of the mushaf is length-
heavy.

Fibonacci front-loading:
- 7 of 10 Fib positions are ≤34 (30 % of surahs)
- Uniform-null p: 0.006
- Log-uniform positional null: p = 0.50
- Detrended-residual p: 0.90 (Fib residuals are -0.23, BELOW trend)

Prime front-loading:
- Mean prime position 53.1 vs composite 59.8
- Uniform-null p: 0.07
- Detrended-residual p: 0.93

### The spectral false alarm
DFT on linear-detrended log V hit p ≈ 0.008 at k=2 (period 57).
Same test on log-abjad hit p < 0.0005 at k=1.

After quadratic detrending: peaks shift to k=7 (period 16.3), p =
0.025 (V) and p = 0.56 (abjad).

After cubic detrending: p = 0.055 (V).

After sort-deviation (detrend-invariant): p = 0.66.

The apparent signals are imperfect-detrend leakage from the
non-linear decay shape. **No real periodicity.**

### Null results (recorded)
- Benford fits: verse counts χ² = 7.44 (df 8), abjad χ² = 2.90
- No length-≥4 arithmetic progressions, no length-≥3 geometric
- Collatz correlation is trivially mediated by log V
- Self-reference V = sid × K: 6 hits, expected 4.9, p = 0.34
- No Lucas effect, no Fib effect after control
- Revelation-order autocorr less than mushaf (Sadeghi's ramp)

### Descriptive-only positives
- **Exponential decay best-fit**: log V ≈ 5.22 − 0.029·n, R² = 0.77
  (beats power law R² = 0.62 and linear R² = 0.61). Mushaf halflife
  ≈ 24 surahs.
- **Gap lag-1 autocorr −0.30**: weak anti-persistence, mechanically
  expected from monotone-with-local-perturbations.
- **Running-sum midpoint 3118 lands at S26:186**: single data point.
- **45 adjacent inversions** in V, clustered in S46..S67 transition
  zone.

## Methodological note

The right methodology for front-loaded hypothesis classes (Fibonacci,
log-spaced) is **log-uniform positional null**, not uniform. I added
this control after seeing the naive result. Similarly, the right
methodology for DFT on a strongly-trended sequence is **polynomial
detrending at multiple orders plus a detrend-invariant control
(sort-deviation)**. I added these after seeing the linear-detrend
peak.

These are not post-hoc rescues of a null — they are corrections of
an invalid initial framing that happened to give a false positive.
When the same logic is applied honestly to any other hypothesis in
the mushaf-ordering space, it will immediately expose the same
confound.

## Files touched

- Created: findings/phase-b-hypotheses/numerical-sequences.md
- Created: journal/numerical-sequences-run-1.md (this file)
- Created: scratch/numerical-sequences/analyze.py
- Created: scratch/numerical-sequences/spectral_followup.py
- Created: scratch/numerical-sequences/fib_followup.py
- Created: scratch/numerical-sequences/prime_followup.py
- Created: scratch/numerical-sequences/results.json

## Time
~50 minutes: 10 min read/plan, 15 min main analyze.py run, 10 min
follow-up scripts + interpretation, 15 min writeup.

## Gotchas / lessons
- Never trust a DFT p-value after linear detrending on a sequence
  with visible non-linear trend. Always run quadratic+ and a detrend-
  invariant control.
- Never trust a positional-hypothesis test against a uniform null if
  the hypothesis class has its own positional distribution.
- Front-loading of Fibonacci positions in 1..114 is pathological:
  F_n doubles every 1.44 positions, so 70 % of Fib ≤ N are in the
  bottom third of {1..N}. Any "front-heavy" property of the mushaf
  will hit them spuriously.
- The mushaf is an exponential-decay-plus-clusters-plus-liturgy, not
  a pure length-sort. The three components can't be disentangled with
  sequence statistics alone.

## What's NOT in this report
- No test on individual muqatta'at positions as a sequence (that's
  the muqatta'at agent's territory).
- No test on the Nöldeke 4-phase sequence of means (chrono-revelation
  already covered).
- No shuffled-mushaf baseline on the whole test battery (would be a
  useful addition but wasn't requested).
- No comparable-corpus Benford check (cross-baseline agent).
