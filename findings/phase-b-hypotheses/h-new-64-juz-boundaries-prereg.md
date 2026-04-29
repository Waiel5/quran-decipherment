---
id: H-NEW-64
title: Do canonical juzʾ (30-part) boundaries correspond to natural structural breaks?
phase: B
status: PRE-REGISTERED
date: 2026-04-15
agent: h-new-64-specialist
seed: 20260416
rules_tuple: (no-tashkeel; canonical 1..114 mushaf order; whitespace tokenization on Arabic text; verse-id = 1-indexed within surah; basmala-counted-only-in-surah-1)
parent: project_quran_decipherment
related: H-NEW-43 (verse-length FFT), H-NEW-46 (muqaṭṭaʿāt vs surah length), H-NEW-58 (surah-pair twinning)
test_family: 4-axis structural-break test against random-boundary null
multi_test_correction: Bonferroni over 4 axes + 1 joint test (k = 5; α_bon = 0.01)
---

# [[h-new-64-juz-boundaries|H-NEW-64]] — Pre-registration: Juzʾ Boundaries vs Structural Breaks

## Motivation

The Quran is traditionally divided into 30 ajzāʾ (parts) for monthly recitation
(one juzʾ per night of Ramaḍān). Each juzʾ is roughly 207 verses (6,236 / 30).
The juzʾ boundaries are EDITORIAL — added by later scribal/recitational
tradition — and famously CUT ACROSS surahs (e.g., juzʾ 2 starts mid-Q2 at v142;
juzʾ 30 starts at the head of Q78 but most starts are intra-surah).

Question: do these editorial boundaries correspond to NATURAL structural breaks
in the text (topic shifts, rhyme changes, narrative pivots, length
discontinuities), or are they purely length-uniform cuts placed without regard
to text-internal structure?

A PASS would constitute evidence that the juzʾ tradition encodes something
beyond simple length-balancing — a hint that the partitioners knew the text
well enough to favor natural seams. A NULL would suggest the juzʾ are purely
length-driven.

## Data and locking

- Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Loader: `/Users/grey/Downloads/quran/analysis/tools/loader.py`
- Verse counts: `/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv`
- Total verses (Hafs/Kufan, including basmala only as Q1:1): 6,236
- 30 juzʾ ⇒ 29 internal boundaries

### LOCKED canonical 30-juzʾ start list (al-Suyūṭī standard convention)

| juzʾ | starts at | | juzʾ | starts at |
|---|---|---|---|---|
| 1 | Q 1:1   | | 16 | Q 18:75 |
| 2 | Q 2:142 | | 17 | Q 21:1  |
| 3 | Q 2:253 | | 18 | Q 23:1  |
| 4 | Q 3:93  | | 19 | Q 25:21 |
| 5 | Q 4:24  | | 20 | Q 27:56 |
| 6 | Q 4:148 | | 21 | Q 29:46 |
| 7 | Q 5:82  | | 22 | Q 33:31 |
| 8 | Q 6:111 | | 23 | Q 36:28 |
| 9 | Q 7:88  | | 24 | Q 39:32 |
| 10 | Q 8:41 | | 25 | Q 41:47 |
| 11 | Q 9:93 | | 26 | Q 46:1  |
| 12 | Q 11:6 | | 27 | Q 51:31 |
| 13 | Q 12:53 | | 28 | Q 58:1  |
| 14 | Q 15:1 | | 29 | Q 67:1  |
| 15 | Q 17:1 | | 30 | Q 78:1  |

The 29 INTERNAL boundaries (between consecutive juzʾ) lie at the start of
juzʾ 2 through juzʾ 30. Each boundary is mapped to a 1-indexed global verse
position p ∈ {1, ..., 6236}; the boundary "cuts" between verse p−1 and verse p.

## Pre-registered axes (LOCKED)

For each boundary at global verse position p, with window-half-width w = 10
verses, we compute four structural-break statistics comparing the
"before window" V_{p-w..p-1} to the "after window" V_{p..p+w-1}:

### Axis A — Topic shift (lexical Jaccard divergence)

D_A(p) = 1 − |T_before ∩ T_after| / |T_before ∪ T_after|

where T_before, T_after are the sets of normalized whitespace-tokenized words
in the respective windows. Higher = bigger topic shift.

### Axis B — Rhyme-class shift

For each verse, extract the LAST whitespace token of the verse text (after
stripping pause markers and the sajda symbol ۩). Take its rightmost
2-character grapheme cluster as a "rhyme bucket" (Arabic letters only). For a
window, compute the multiset of rhyme buckets, then compute total-variation
distance:

D_B(p) = (1/2) Σ_b |freq_before(b) − freq_after(b)|

### Axis C — Narrative-pivot (proper-noun / capitalised-name change rate)

The Arabic JSON has no capitalisation. Use the closed list of proper nouns
LOCKED here, derived from a fixed set of Quranic prophet/people/place names
(transcribed in Arabic skeleton):

Prophets: محمد، آدم، نوح، إبراهيم، إسماعيل، إسحاق، يعقوب، يوسف، موسى، هارون،
داود، سليمان، عيسى، يحيى، زكريا، أيوب، يونس، شعيب، صالح، هود، لوط، إدريس،
ذو الكفل، إلياس.

People/groups: بنو إسرائيل، فرعون، عاد، ثمود، قريش، القارون، السامري، يأجوج،
مأجوج.

Places: مكة، بكة، يثرب، المدينة، طور، سيناء، مصر، بابل، الكعبة، البيت العتيق.

(Stored as a normalized-skeleton lookup set; substring match on no-tashkeel.)

For windows W_before and W_after, count proper-noun token occurrences
n_before, n_after; then

D_C(p) = |n_before − n_after| / (n_before + n_after + 1)

(Smoothed Laplace denominator to avoid 0/0 in name-free windows.)

### Axis D — Length discontinuity

For each verse compute its token count L_v (whitespace split). For the window
let mean lengths be μ_before, μ_after. Then

D_D(p) = |μ_before − μ_after| / (max(μ_before, μ_after) + 1)

## Joint statistic and ranking

Each axis is z-normalised against the random-boundary null distribution
(see below): z_X(p) = (D_X(p) − null_mean_X) / null_sd_X.

Joint statistic: S_joint(p) = z_A(p) + z_B(p) + z_C(p) + z_D(p).

Aggregate over the 29 juzʾ boundaries: SUM_X = Σ_p z_X(p).

## Null model (random within-corpus boundaries, LOCKED)

For each of N_perm = 1000 trials:
- Draw 29 boundary positions uniformly from the set of "valid" positions:
  POS_VALID = global verse positions p ∈ {2, …, 6235} such that p does NOT
  coincide with a SURAH start (i.e., the verse at p is NOT verse-id 1 of any
  surah). This makes the null FAIR — the random boundaries cannot land on
  the natural surah seams.
- Compute SUM_X for each axis under the random boundaries.
- Random RNG: Python `random` with seed 20260416, single global seed for the
  whole script.

P-value for axis X = (1 + #{trials with SUM_X ≥ observed_SUM_X}) / (N_perm + 1)

## MW-5 positive control (LOCKED)

Surah boundaries — i.e., the 113 internal seams between consecutive surahs —
ARE natural structural breaks by construction. As a positive control we run
the SAME pipeline on a randomly sampled set of 29 surah-boundary positions
(seed 20260416, no replacement). Predict: SUM_X for at least 3 of 4 axes
should EXCEED juzʾ-boundary SUM_X (i.e., surah boundaries are bigger natural
breaks than juzʾ boundaries). If the surah-positive-control fails to exceed
random null, the entire pipeline is invalid.

## Pre-registered PASS criteria

α_Bonf = 0.05 / 5 = **0.01** (4 axes + 1 joint test).

- A1 PASS if observed SUM_A > 99th percentile of null distribution.
  (Equivalently, p_A < 0.01 in 1000-permutation test.)
- A2 PASS if observed SUM_B > 99th percentile of null distribution.
- A3 PASS if observed SUM_C > 99th percentile of null distribution.
- A4 PASS if observed SUM_D > 99th percentile of null distribution.
- JOINT PASS if observed Σ SUM_X > 99th percentile of null Σ SUM_X.

GLOBAL VERDICT:
- STRONG-PASS: ≥ 2 axes pass AND joint passes.
- WEAK-PASS: exactly 1 axis or only joint passes.
- NULL: no axis passes and joint does not pass.

NULL is published with identical prominence (per project policy).

## Per-boundary "naturalness" ranking (descriptive, no test)

Report the 29 juzʾ boundaries ranked by S_joint(p), highlighting:
- The 5 MOST-natural boundaries (highest S_joint).
- The 5 LEAST-natural boundaries (lowest S_joint, possibly negative).
- Surah-aligned vs intra-surah boundary breakdown:
  - 7 of the 29 starts (juzʾ 14, 15, 17, 18, 26, 29, 30) coincide with surah
    starts (Q 15:1, Q 17:1, Q 21:1, Q 23:1, Q 46:1, Q 67:1, Q 78:1).
  - 22 of 29 are intra-surah cuts.
  - Predict: surah-aligned juzʾ boundaries should rank higher in S_joint than
    intra-surah ones (sub-test, not in main Bonferroni budget; reported as
    descriptive observation).

## Garden-of-forking-paths log (BEFORE run)

- Window size w = 10 verses on each side: chosen ex ante as a balance between
  local context and statistical stability. Sensitivity at w = 5 and w = 20
  reported but not Bonferroni-tested.
- Topic-shift metric: Jaccard chosen over cosine on TF-IDF because the
  no-tashkeel tokenization is unstable across morphological variants and we
  want a robust set-overlap measure that doesn't require a domain-specific
  IDF baseline.
- Rhyme bucket: rightmost 2-character grapheme cluster of the last token. The
  classical fasila rhyme is more nuanced (final vowel + consonant), but the
  no-tashkeel data lacks vowels; this is the best proxy.
- Proper-noun list: closed and locked; substring matching may miss some
  context-bound proper noun usages but won't false-positive at high rates.
- Length-discontinuity: token count not character count, since tokens correlate
  better with semantic units.
- Null fairness: the "avoid surah boundaries" constraint is critical. A
  random-boundary null that includes surah seams would bias the test in
  juzʾ's favor (since juzʾ boundaries hit some surah seams).
- Window edge-handling: if a window crosses corpus boundary (very early or
  very late), the window is truncated; this affects only the first and last
  juzʾ boundaries and is documented in the script.

## Specifically pre-disqualified post-hoc choices

- Cannot change w after seeing data.
- Cannot reweight axes after seeing data.
- Cannot exclude particular juzʾ boundaries from SUM_X.
- Cannot switch null from random-within-corpus to a different null.

## Deliverables

- Script: `scripts/h_new_64_juz_boundaries.py`
- JSON dump: `findings/phase-b-hypotheses/csv/h-new-64.json`
  (per-boundary axis scores, null distributions, p-values, ranking,
  positive-control results)
- Findings: `findings/phase-b-hypotheses/h-new-64-juz-boundaries.md`
- Journal: `journal/h-new-64-run-1.md`
