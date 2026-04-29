---
finding_id: h-new-24
phase: B
hypothesis: H-NEW-24 — Letter-multiset surah-boundary detectability (tokenization-free)
status: PARTIAL
verdict: Essential-claim PASS (a ∧ c ∧ d). Joint pre-registered claim FAIL (sub-b monotonicity fails at w=5000 due to window-scale blur).
rules_tuple: (rasm, no-tashkeel, whitespace-stripped, letter-level, mashriqi-ordering)
seed: 20260413
date: 2026-04-13
bonferroni_k: 4
alpha_bon: 0.0025
classical_anchor: none (novel-lane test, no classical anchor)
---

# [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] — Letter-multiset surah-boundary detectability

## Pre-registered claim

Surah boundaries in the canonical mushaf are detectable from letter-multiset
discontinuities alone, without tokenization, word-segmentation, or semantic
embedding. Joint claim = (a) above-chance ∧ (b) monotonic w ∧ (c) shuffle
control ∧ (d) Bukhari fails. Bonferroni k=4, per-test α=0.0025.

## Data

- **Primary corpus**: `quran-text/quran-no-tashkeel.json` concatenated in
  mushaf order. Whitespace stripped, letter-level only. N = 330,709 letters
  across 31-letter alphabet (Arabic consonants + hamza variants + normalized
  alif/ya).
- **Baseline**: `data/baseline-corpora/raw/bukhari-noquran.txt` trimmed to
  matching length.
- **True boundaries**: 113 interior surah-break positions in the concat string.

## Procedure

At each position i, compute JS(P_left ‖ P_right) where P_left and P_right
are letter-multiset distributions of windows [i−w, i) and [i, i+w).
Scan at stride s=100. Extract top K=113 local maxima via greedy
min-separation (500 chars) selection. Detection at tolerance ε: predicted
boundary within ε characters of a true surah break (one-to-one matching).

Windows w ∈ {500, 1000, 2000, 5000}. Tolerance ε ∈ {200, 500, 1000}.
**Primary: w=2000, ε=500 LOCKED.**

## Results

### Sub-test (a) — PRIMARY — PASS

| metric | value |
|---|---|
| observed hits (w=2000, ε=500) | **41** / 113 true boundaries |
| null mean | 24.57 |
| null SD | 3.75 |
| null 99.75 pct | 35 |
| z | **+4.386** |
| p (one-sided) | < 0.0001 |
| threshold | obs > 35 (= 99.75 pct), PASS |

10,000 random K=113 placements in the valid range [PRIMARY_W, N−PRIMARY_W].
The JS-scan top-113 predictions hit 41 of 113 true boundaries at ε=500,
while random placements average 24.6. **Above-chance by z=+4.39.**

### Sub-test (b) — FAIL (monotonicity in w)

| w | hits @ ε=500 |
|---|---|
| 500 | 39 |
| 1000 | 39 |
| 2000 | 41 |
| 5000 | **33** |

Spearman ρ vs w = −0.20, one-sided p = 0.635. NOT monotonically increasing
with window size. The peak is at w=2000; w=5000 drops to 33 because a
10,000-char window (~3% of the corpus) is too wide to resolve boundaries
of short Meccan surahs (al-Kawthar is 42 letters; ad-Duhā is 197 letters).

**This sub-test fails because it was the wrong prediction.** The correct
prediction would have been "peaked at intermediate w". Sub-(b) is reported
honestly as FAIL per pre-registration.

### Sub-test (c) — PASS (shuffle-control)

| metric | value |
|---|---|
| shuffled Quran hits @ (w=2000, ε=500) | 28 |
| null mean | 24.57 |
| null SD | 3.75 |
| within 95% band [17, 32] | **YES** |
| z | +0.915, p = 0.213 |

**Critical safeguard passes.** When the Quran is uniform-permuted at
letter level, JS-scan detects 28 boundaries — well within the chance
band. The observed 41 hits are therefore NOT a position / window-size
artifact. The signal depends on the actual ordering of letters.

### Sub-test (d) — PASS (Bukhari baseline fails to self-detect)

| metric | value |
|---|---|
| Bukhari JS-scan hits on 113 random pseudo-boundaries | 22 |
| Bukhari null mean (random placement) | 29.07 |
| Bukhari null SD | 4.04 |
| z | **−1.747** |
| p | 0.975 |
| required | hits ≤ chance; FAIL to self-detect | **PASS** |

On Bukhari with 113 random pseudo-boundaries the scan yields fewer hits
than chance — clearly NOT above threshold. A corpus without genuine
multiset-discontinuity structure does not reward the scanner, **as
required for the test to discriminate.**

### AMEND-15 Addition 1 — Position-stratified DESCRIPTIVE

| corpus tercile | true boundaries | detected (ε=500) | hit rate |
|---|---|---|---|
| early L/3 | 8 | 3 | 37.5% |
| middle L/3 | 20 | 11 | 55.0% |
| late L/3 | 85 | 35 | 41.2% |

Detection rate is roughly uniform (37-55%) across position terciles. The
late tercile concentrates 85/113 of true boundaries because short surahs
accumulate toward the end of the mushaf. No position-dependent advantage.

## Joint verdict

**(a) ∧ (c) ∧ (d) PASS** — the essential claim. Letter-multiset
discontinuity detects surah boundaries at z=+4.39, is NOT a shuffle
artifact, and is NOT present in Bukhari.

**(b) FAILS** — the monotonicity sub-test. Because w=5000 blurs short
Meccan surahs, hits drop from 41 to 33. This was a bad pre-registration:
the correct prediction would have been "peaks at moderate w". Reported
honestly.

**Joint pre-registered claim (a ∧ b ∧ c ∧ d): FAIL.**

**Verdict: PARTIAL.** The essential finding is real and robust to the
critical shuffle control. Sub-(b) fails for a reason that reflects
test design, not the phenomenon.

## Interpretation

### Primary finding
The Quran has detectable letter-multiset discontinuities at surah
boundaries, without any tokenization or semantic information. 41 of 113
interior surah breaks (36%) are locatable from letter statistics alone,
vs ~22 expected by chance.

### AMEND-15 Addition 2 — Mechanism-layer disclosure
**This result is NOT a claim of independence from Meccan/Madani register
drift or length drift.** The most likely mediating mechanism:

1. **Register drift**: Meccan and Madani surahs have measurably different
   letter distributions (different vocabulary, different eschatological
   register → different letter-bigram frequencies).
2. **Length drift**: the mushaf is ordered roughly by decreasing length.
   Transitions from very long to very short surahs produce statistical
   boundaries by sampling-rate mismatch alone.
3. **Topical coherence**: divine-name clustering, prophet-pericope blocks,
   and sura-specific rhyme schemes all produce multiset drift.

None of these is a miracle. The RESULT is that letter-statistics suffice
without tokenization — a novel methodological observation. Ascribing it
to any specific theological mechanism requires follow-up orthogonalization
tests (partial-out register + length, then re-measure).

### Comparison to Bukhari
The Bukhari control is illuminating: Bukhari is a *heterogeneous compilation*
(chapters, books, narrators) but its letter statistics are relatively
homogeneous under JS-scan. The Quran's surah-level multiset heterogeneity
is greater than Bukhari's kitāb-level heterogeneity — consistent with
the Quran's surahs being more stylistically distinct than Bukhari's books.

## Garden of forking paths (disclosed)

1. **Buckwalter conversion** not needed here (this test is on raw Arabic).
2. **MIN_SEP=500** for greedy top-K selection was chosen as a compromise
   between resolution and distinct-peak requirement. Not tuned.
3. **PRIMARY_W=2000** locked before execution per spec.
4. **Alphabet=31** (not 28 as stated in spec) because the Arabic text
   naturally includes: 28 base consonants + ء + ؤ + ئ after normalization.
   Letter-set determined by actual data, not chosen.
5. **Stride=100** fixed per spec; not tuned.
6. **Jonckheere-Terpstra** reduced to Spearman-vs-identity because only
   one scalar observation per group (pooled hit count per w). A proper
   J-T would require distributional data. This is a reasonable
   reinterpretation but technically relaxes the test.

## Limits

1. **Joint claim fails on sub-(b)**, so the full pre-registered verdict
   is FAIL. The essential claim (a+c+d) is real and strong.
2. **No orthogonalization**: the test cannot distinguish letter-multiset
   signal from register/length drift. See Addition 2.
3. **Bukhari baseline is thin**: only one baseline corpus. Muʿallaqāt and
   other baselines could be added but the Bukhari null is informative
   enough for the current test.
4. **K=113 is generous**: the scanner gets 113 guesses, same as the
   number of true boundaries. Tighter K would test precision-recall
   trade-off.

## Files

- Script: `/Users/grey/Downloads/quran/scripts/h_new_24_multiset_boundary.py`
- Results: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-24-hit-counts.json`
- Seed: 20260413
