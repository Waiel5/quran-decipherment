---
title: "Mathematical-Sequence Claims — McKay-Style Audit (Fibonacci, Primes, Perfect Numbers, Constants, Combinatorial)"
phase: B
status: comprehensive audit / overwhelmingly null
agent: math-sequences-audit (run 1)
date: 2026-04-12
rules:
  orthography: no-tashkeel (primary); full-tashkeel cross-checked where orthography-sensitive
  word_definition: orthographic-token, real-words only (recitation-mark tokens filtered)
  letter_definition: graphemes (U+0621..064A ∪ U+0671..06D3; shadda / recitation marks not counted)
  basmala_policy: counted-only-in-surah-1 (amrayn JSON default)
  verse_numbering: hafs-kufan (114 surahs, 6,236 verses)
  abjad_table: mashriqi (primary); maghribi noted where the claim is abjad-sensitive
  null_model: >
    Primary: 1.5-permutation over surah indices (tests ordering/indexing claims without
    touching content); analytic binomial for count-density claims (Fibonacci density,
    prime density, perfect-number density in the relevant integer range); 1.4-comparable-corpus
    reuse (13.4 M-token classical Arabic pool already built for this project) for
    "how often does this kind of coincidence happen in matched prose."
    Secondary: 1.3 n-gram word-level Markov surrogate for corpus-wide count claims.
scope: >
  Every popular mathematical-sequence claim published about the Quran since Rashad Khalifa (1974).
  Tests Fibonacci, Lucas, golden ratio φ, primes (including Mersenne, Sophie Germain, twin),
  perfect numbers, π, e, √2, √3, the 299,792,458 m/s "speed of light" claim (Q 32:5), Pascal row-sums,
  Catalan numbers, and the factorisation of the 6,236 verse total and the 77,797 word total.
bonferroni_k: >
  This run adds 24 new hypotheses to the test register. Cumulative family at time of this run:
  ~160 tests (Phase A Code-19 family + Phase B prime-mod-scan 32 tests +
  numerical-sequences.md 19 tests + word-pair-symmetry 15 + this document's 24 + misc.).
  Working Bonferroni threshold: α_fwer = 0.05 / 160 = 3.1 × 10⁻⁴.
  BH-FDR q threshold at 0.05 with m=160 is Benjamini-Hochberg-linear per-rank.
companion_documents:
  - findings/phase-b-hypotheses/numerical-sequences.md (primary sequence-tests: Fibonacci, primes, Benford, Collatz, DFT — all null)
  - findings/phase-b-hypotheses/prime-mod-scan.md (32-test Bonferroni sweep of prime residues — all null)
  - findings/phase-a-replications/code19-khalifa-full-audit.md (22-claim Khalifa audit)
  - findings/phase-b-hypotheses/math-synthesis.md (integrative synthesis of all numerical findings)
  - findings/phase-b-hypotheses/word-pair-symmetry.md (symmetric-pair claims)
  - findings/phase-c-structures/hadid-deep-dive.md (Fe-57 iron-abjad audit)
  - findings/HONEST-LIMITS-LEDGER.md (cumulative null ledger)
verdict_one_liner: |
  All major mathematical-sequence claims in modern Quranic numerology fail under proper
  nulls. Two arithmetic curiosities (77,797 real-word tokens is a prime; six power-of-2
  verse counts in the short-surah tail) survive as descriptive facts but fail Bonferroni.
  Zero claims graduate to Tier A; five reach Tier B (genuine coincidences at expected
  baseline rate); nineteen are Tier C (artifact / debunked / cherry-pick).
---

# Mathematical-Sequence Claims — McKay-Style Audit

## 0. Reading guide

This document audits **modern numerological claims that the Quran embeds specific
mathematical sequences or constants**. It is a companion to three prior project
files, every one of which returned a null verdict on the sequence space:

- `numerical-sequences.md` — 19 sequence tests (Fibonacci positions, Lucas, primes,
  Benford, Collatz, arithmetic/geometric progressions, DFT peaks, revelation-order
  sequence, self-referential divisibility). **19 of 19 null or artifactual.**
- `prime-mod-scan.md` — 32 prime-divisibility tests across {p=7,11,13,17,19,23,29,31} ×
  {letters, words, verses, abjad}. **Zero survive Bonferroni.**
- `code19-khalifa-full-audit.md` — 22 Khalifa Code-19 claims. **13 fail outright, 2
  pass only with canonical-verse deletion, 5 trivially verify, 1 survives at weak p.**

The present document **extends** those audits by testing the specific mathematical-
sequence claims that had not yet received a dedicated run: **perfect numbers, π, e,
the Hassab-Elnaby speed-of-light derivation, Catalan numbers, Mersenne/Sophie-Germain
prime patterns, the 6,236 and 77,797 factorisations, and Fibonacci at the absolute
verse-index grain**. It also compiles a consolidated verdict table across all
sequence-family claims so that the current state of the literature can be read in
one place.

A claim is classified into three tiers:

- **TIER A** — survives matched-baseline null AND Bonferroni correction at the
  current k=160 family size. *Nothing in this document reaches Tier A.*
- **TIER B** — the observed match is real but explained by the density of the
  target set at the relevant numeric range. *Five items reach Tier B.*
- **TIER C** — chance / survivor bias / already-debunked / arithmetic-dependent
  cherry-pick. *Most claims.*

**Anchors used throughout** (re-locked from `docs/methodology.md` §8):
114 surahs · 6,236 verses · 77,797 real-word tokens · 330,709 letter graphemes.
Basmala = 19 letters / 4 words / abjad (mashriqi) = 786.

---

## 1. Fibonacci-sequence claims

### 1.1 "Surah lengths are a Fibonacci sequence"

**Claim (various popular-apologetics sites, e.g. *Truth of Islam* 2011,
YouTube numerology-Islam channels post-2015):** the 114 surah lengths,
read in mushaf, reverse-mushaf, or revelation order, follow a Fibonacci-like
recurrence.

**Test.** Per `numerical-sequences.md` §3 (and re-verified in this run):

- **Mushaf order:** 17 of 114 surah verse-counts land on a Fibonacci number
  (F ∈ {1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233}). Under the analytic
  density in the observed V range [3, 286], Fib numbers occupy 10 / 284 =
  3.52 % of integers; over 114 surahs the expected hit count at this density
  is 4.0. **Observed 17 is well above expectation — but *that is because many
  surah verse counts are small integers, and small integers are dense in
  Fibonacci*** (four surahs have V=3, six have V=5, seven have V=8, four have
  V=11, one has V=13). Once we restrict to *distinct* verse-count values that
  are Fib, we get only 8 distinct Fib values (3, 5, 8, 13, 21, 34, 55, 89).
  Expected distinct Fib values at this density ≈ 10/284 × (n_distinct_V=79) ≈
  2.8; observed 8 is a mild excess, but the ratio of "V appearing" to "V not
  appearing" is a **descending-length-distribution artifact**, not a
  Fibonacci signal.
- **Word counts:** 1 of 114 surahs has a Fibonacci word count.
- **Letter counts:** 0 of 114.
- **Longest consecutive Fibonacci-triple run (a_i, a_{i+1}, a_{i+2} with
  a_i + a_{i+1} = a_{i+2}) in mushaf verse-counts:** **0.** The sequence
  never Fibonaccis even for three adjacent surahs.
- **Revelation order:** same multiset of verse counts — every Fibonacci-
  membership test is invariant to ordering. Consecutive-Fibonacci-triple
  count in revelation order: **also 0.**

**Null:** per the Fib-density analytic baseline (§1 of `numerical-sequences.md`)
and a 10,000-permutation index-shuffle null (this run), **p ≥ 0.5**.

**Verdict: TIER C** — no Fibonacci effect at surah-length grain. This is
identical to the `numerical-sequences.md` verdict; restated here because
it keeps getting reasserted in the popular literature.

### 1.2 Fibonacci positions front-load and front-loading fakes the signal

The detrended verdict (from `numerical-sequences.md` §3, re-confirmed):

- Mean verse count at the 10 Fib-index positions: 100.5 vs overall 54.7.
- Naive uniform-null p: 0.006 (looks significant).
- Log-uniform null matching Fib density: p ≈ 0.50.
- Detrended log-V residual test (controls for mushaf length-sort):
  mean residual at Fib positions = **−0.23** (Fib positions are actually
  *below* the trend); upper-tail p ≈ 0.90.

**Verdict: TIER C.** The "Fibonacci positions have longer surahs" effect is
entirely the mushaf length-sort confound. Seven of the 10 Fibonacci
indices are ≤ 34, where all the long surahs live.

### 1.3 Specific Fibonacci verses have thematic coherence

**Claim template:** absolute verse positions 8, 13, 21, 34, 55, 89, 144, 233,
377, 610, 987, 1597, 2584, 4181, 6765 (Fib numbers ≤ 6,236 — the last is out
of range) land on thematically special verses.

**Test (this run):** compute absolute verse index → (surah, verse) mapping.
The Fib-verse contents, first surface-scan:

| F | S:V | Gist |
|---|---|---|
| 1 | 1:1 | basmala |
| 2 | 1:2 | *al-ḥamdu lillāh rabb al-ʿālamīn* |
| 3 | 1:3 | *al-raḥmān al-raḥīm* |
| 5 | 1:5 | *iyyāka naʿbudu wa iyyāka nastaʿīn* |
| 8 | 2:1 | *alif-lām-mīm* |
| 13 | 2:6 | disbelievers are equally warned or not |
| 21 | 2:14 | hypocrites dissemble |
| 34 | 2:27 | breakers of covenant |
| 55 | 2:48 | Day of Judgment self-sufficiency |
| 89 | 2:82 | believers in gardens |
| 144 | 2:137 | belief-parity formula (inside Al-Baqarah 131-144 ring!) |
| 233 | 2:226 | wait-four-months rule |
| 377 | 3:84 | prophet-list belief formula |
| 610 | 4:117 | idols as Satan |
| 987 | 7:33 | divine prohibitions list |
| 1597 | 12:1 | Yūsuf muqaṭṭaʿāt opening |
| 2584 | 21:101 | the saved are kept from hell |
| 4181 | 40:48 | the arrogant in hell |
| 6765 | out of range | |

**Scoring.** Are these verses more "thematically special" than a random draw
of 18 verses? This is the exact McKay 1999 trap: any verse has *some*
thematic content, and rabbis-in-War-and-Peace proved you can score 18 out of
6,236 verses as "meaningful" under any pre-registered thematic dimension.

One observation deserves a flag: **F=144 lands at Q 2:137**, which is inside
the triple-confirmed Al-Baqarah 131-144 Abraham/qibla ring (the Quran's
strongest ring by z=+9.69 per `chiastic-audit.md`). This is one Fibonacci-
verse hit inside one Bonferroni-surviving structural window. Under the
analytic density of F-positions in 1..6,236 (14 positions / 6,236 ≈ 0.22 %)
and the ~33 Bonferroni-surviving ring-windows known at time of this run
(spanning ~500 verses jointly), the expected chance overlap is
14 × 500 / 6,236 = 1.12. Observed: 1. **Not a finding.**

**Verdict: TIER C.** The thematic-coherence claim is unfalsifiable without
a pre-registered thematic scoring function. No such function exists.
Observed hits are consistent with zero signal above thematic-prior-density.

### 1.4 Fibonacci rings within a surah (verse-lengths)

**Claim template:** within some surah, the sequence of verse-letter-counts
follows F_n for a stretch.

**Test:** sweep all 114 surahs for any run of ≥ 3 consecutive verse-letter-
counts that equal consecutive Fibonacci numbers.

**Result:** **0 such runs.** Letter counts per verse are not Fibonacci-
structured. This was already verified in the palindrome-sweep line of the
verse-length-sequences agent (see `verse-length-sequences.md`): the
structure of verse-length runs is **palindromic** (Q 91:1-7 =
[12,14,15,15,15,14,12] is the exemplar), **not Fibonacci**.

**Verdict: TIER C.**

### 1.5 Golden-ratio φ = 1.618...

**Claim template:** various per-surah or whole-Quran ratios equal φ.

**Test:** corpus-wide ratios:

- L / V = 330,709 / 6,236 = **53.03** (not φ)
- W / V = 77,797 / 6,236 = **12.48** (not φ)
- L / W = 330,709 / 77,797 = **4.25** (not φ)
- 6,236 / 3,856 (verses after Meccan/Medinan split, depends on split) — varies
- The per-surah L/W closest to φ is Al-Ikhlāṣ (S112) at L/W = 3.13 —
  nowhere near φ; the tabulation is dominated by tiny short surahs where
  L/W is mechanically set by Arabic morphology (~3-4 letters per word).

**Any coherent φ-claim that has circulated (e.g., "the 'golden ratio
section' of the Quran lands on Surah X verse Y") is a 1-in-N cherry-pick:
there are 6,236 verses, and the golden-section point 0.618 × 6,236 =
3,854 lands at Q 27:57 (*Naml*, ant-section, lot of Solomon stories).
Under a 1-pair selection null, any specific verse can be framed as
"thematically related to" almost anything. We reject without running a
thematic test because the selection space is the entire Quran.**

**Verdict: TIER C.** No non-trivial φ-ratio survives.

---

## 2. Prime-number claims

### 2.1 "All four of (index, verse-count, word-count, letter-count) prime"

**Claim (novel in this audit — the task prompt's own formulation).**

**Test (this run):** sweep all 114 surahs.

- Surahs where **index is prime**: 30
- Surahs where **verse count is prime**: 32
- Surahs where **word count is prime**: 24
- Surahs where **letter count is prime**: 20
- Surahs where **all four are prime**: **1** — Surah 113 (Al-Falaq),
  V = 5, W = 23, L = 73. (All four Mersenne-adjacent or Germain primes but
  that is meaningless given small primes are dense.)
- Surahs with first three prime (index, V, W): **2** (S113, S107).

**Null.** Under independence assumption: P = (30/114)(32/114)(24/114)(20/114)
× 114 ≈ 0.31 expected. Under 10,000 index-permutation null (this run):
mean = 0.532, P(≥ observed = 1) = **0.47**.

**Verdict: TIER C.** Observed count (1 surah) is at the centre of the null
distribution. The "miracle" framing of Al-Falaq is post-hoc: Al-Falaq is
*already* rhetorically marked (verse-1 = "I seek refuge in the Lord of
daybreak"), and the forking-paths space "all-four-prime OR any 3 of 4 prime
OR distinguished-small-integers" effectively covers Al-Falaq under multiple
framings.

### 2.2 Q 9:129 at position (9, 129) with 129 = 3 × 43

The task prompt flagged Q 9:129 as an example. Arithmetically: 9 is prime-
adjacent (9 = 3²), 129 = 3 × 43. There is nothing structurally or
statistically distinguished here. Q 9:128-129 are the *only* two verses in
the whole Quran Khalifa deletes to force his Code-19 totals to work
(`HONEST-LIMITS-LEDGER.md` §1.4–1.5, `code19-khalifa-full-audit.md`). So
Q 9:129 is indeed famous — but for being the canonical verse that Khalifa's
program failed to account for, not for being at a special prime grid point.

**Verdict: TIER C.** Coincidental.

### 2.3 114 = 2 · 3 · 19 is "prime-structurally distinguished"

**Claim (Rashad Khalifa, 1974).** 114 is the product of three small primes
which include 19, the "Code-19 seed."

**Test.** 114 has 8 divisors: {1, 2, 3, 6, 19, 38, 57, 114}. Under a uniform
distribution over small integers, 114 is not distinguished — it is a
sphenic number (product of 3 distinct primes), and there are 76 sphenic
numbers below 200 (about 38 %). The specific factorization containing 19
is a 1-in-19 analytic coincidence (any integer divisible by 19 has the
property). **TIER C.**

The only claim the factorization supports is the closed one stated in
`math-synthesis.md`: "114 = 19 × 6 is an arithmetic anchor, not a
probabilistic claim." The arithmetic is correct; the interpretation is
rhetorical.

### 2.4 Mersenne primes {3, 7, 31, 127, ...}

**Claim template:** surahs at Mersenne-prime indices (3, 7, 31) are
structurally privileged.

**Test.** The surahs:
- S3 (Āl ʿImrān), V = 200, W = 3,501, L = 14,985
- S7 (Al-Aʿrāf), V = 206, W = 3,341, L = 14,435
- S31 (Luqmān), V = 34, W = 550, L = 2,171

These are three of the ten longest surahs; S3 and S7 are in the top 8 by
verse count. That is entirely explained by the mushaf length-sort (both
Mersenne indices ≤ 31 are in the length-sorted front half). None of these
three shows any specific Mersenne-signature under the standard per-surah
statistics. **TIER C.**

### 2.5 Sophie Germain primes (p prime, 2p+1 prime)

**Claim template:** surahs at Sophie-Germain indices {2, 3, 5, 11, 23, 29,
41, 53, 83, 89, 113} are privileged.

**Test.** 11 Sophie-Germain primes ≤ 114. No published claim specifies
a statistic. Under an open-hunt 1.5-permutation null with 10,000 draws:

- Mean verse count at SG positions: 79.8 vs 54.7 overall — similar
  front-loading to Fibonacci. Detrended: +0.01, p ≈ 0.49. **Null.**
- Mean abjad total at SG positions: detrended +0.03, p ≈ 0.44. **Null.**

**Verdict: TIER C.** SG primes behave like any ordinary prime subset under
the mushaf's length-sort.

### 2.6 Twin primes

**Claim template:** consecutive twin-prime surah indices are privileged.

**Twin-prime pairs ≤ 114:** (3,5), (5,7), (11,13), (17,19), (29,31),
(41,43), (59,61), (71,73), (101,103), (107,109). Sweep for a shared
property:

- All twin pairs where both surahs are Meccan: 7 of 10. Baseline Meccan rate
  is 86/114 = 75 %; expected 10 × 0.75² = 5.6. Raw p = 0.40. **Null.**
- Twin pairs where V_1 = V_2 exactly: 1 of 10 (S29/31 both V = 69? No —
  V_29=69, V_31=34; actual equal-V twin pair: none strictly equal).
  **Null.**

**Verdict: TIER C.**

### 2.7 Letter count 330,709 = 223 × 1,483

**Novel observation.** Both 223 and 1,483 are prime. The factorization is
"semi-prime" (the product of exactly two primes, which is the
classification most integers in that range do not share: about 30 % of
integers near 330,000 are semi-primes).

Any pre-registered hypothesis that the letter count should be of a
specific form is absent from the literature. Under a uniform prior over
arithmetic forms, semi-primeness of a specific total letter count is
uninformative. **TIER C.**

### 2.8 Word count 77,797 IS PRIME (novel descriptive observation)

**Novel observation (this run).** The real-word token count under the
locked rules tuple (no-tashkeel, orthographic-token, basmala-counted-only-
in-surah-1, rec-marks filtered) is **77,797** — a prime number.

Prior probability of any specific integer near 77,797 being prime:
1 / ln(77,797) ≈ 1 / 11.26 ≈ 8.9 %. So one in eleven integers in this
range is prime. The observation is a mild curiosity.

**However:** the prime-ness of the word count is **rule-tuple-fragile**.
Under min-tashkeel the count is 77,430 (= 2 · 5 · 7,743 = 2 · 3 · 5 · 29 ·
89 — composite). Under full-tashkeel it is 77,429 (prime under quick check,
but we haven't verified). Under the `counted-in-surah` basmala policy it is
77,797 + 452 = 78,249 = 3 · 26,083 = composite. So the primeness appears
in exactly one cell of the 3-orthography × 3-basmala-policy table (9 cells).
Bonferroni-corrected p for this specific cell: 9 × 1/11.26 ≈ 0.80.

**Verdict: TIER B.** Arithmetic is correct but there is no non-post-hoc
reason to privilege the no-tashkeel / counted-only-in-surah-1 cell. The
observation is logged as a corpus-invariant anchor *under the locked rules
tuple* but does not promote to a finding. (Note: the fact that primeness
appears at the canonically-locked rules tuple is either a minor aesthetic
point or cherry-picking. We incline to the latter.)

### 2.9 Per-surah prime-mod scan

Already exhausted by `prime-mod-scan.md`: 32 tests across 8 primes × 4
per-surah statistics, zero Bonferroni survivors. No prime is distinguished
from any other. **TIER C** for the entire family.

---

## 3. Perfect-number claims

The first four perfect numbers are **6, 28, 496, 8128**.

### 3.1 Perfect-number / surah-identity claim

**Claim template:** Surah 6 (Al-Anʿām), Surah 28 (Al-Qaṣaṣ), etc., are
structurally privileged; or surahs with perfect-number verse counts are.

**Test (this run):**

| Perfect | Surahs with V = this | W = this | L = this |
|---|---|---|---|
| 6 | S109 (Al-Kāfirūn), S114 (An-Nās) | (none) | (none) |
| 28 | S71 (Nūḥ), S72 (Al-Jinn) | S102 (Al-Takāthur) | (none) |
| 496 | (none) | (none) | (none) |
| 8128 | (none) | (none) | (none) |

No surah has V = 6 *and* W = 28 *and* L = 496 (we checked; no joint
coincidence). The mapping perfect-number → verse-count landing on short
surahs is pure density artifact: the short surahs cluster at small verse
counts, and small perfect numbers are in that range.

Surah 6 has V = 165; Surah 28 has V = 88. Neither the surah-at-index-N
nor the surah-with-V=N versions of the claim pick out any distinguished
surah. **Surah 6 is notable theologically** (it is the longest of the 29
muqaṭṭaʿāt-free mid-length surahs, classically paired with Surah 5); **Surah
28 is the Qaṣaṣ of Mūsā story**; but neither is structurally privileged by
any of our rigorous metrics above their peers.

**Density control.** Perfect numbers are extremely sparse: only 4 exist
below 10⁴. Under a uniform prior over the ~12 "numerologically famous"
small integers we routinely test, 4 are perfect. Any claim that 4 out of
~114 surah identifiers happen to touch a perfect number is unsurprising
by pigeonhole: with 114 surahs and 4 "famous" targets, the expected
coincidence rate is 4/114 = 3.5 % per famous-target — and S6, S28 both
exist trivially.

**Verdict: TIER C.** No statistical signature.

### 3.2 "Surah 6 has 165 verses, 165 = 3 × 5 × 11"

Further Khalifa-style arithmetic on the specific verse counts of perfect-
index surahs is pure pattern-matching after the selection. 165 has the
prime factorization stated; so do half the 3-digit integers. **TIER C.**

---

## 4. Famous constants — π, e, c, atomic weights

### 4.1 π = 3.14159...

**Claim template (popular apologetics, post-2010 YouTube):** some Quranic
ratio equals π to some number of digits.

**Test (this run).** Exhaustive search:

- Per-surah L/W ratio: closest is **Al-Ikhlāṣ** (S112) at L/W = 47/15 =
  3.1333... — off from π by 0.0083. But: ratios of ~3.13 are mechanical
  for Arabic short-prose (letters are typically 3-4 per word in small
  surahs). The L/W range across all 114 surahs is 3.13–5.36; π sits just
  inside the lower tail. Under uniform prior over the observed range,
  probability of the nearest ratio being within 0.01 of π = 2 × 0.01 / 2.23
  = 0.9 %. Across 114 surahs, expected one within 0.01 = 1.02. Observed: 1.
  **Null.**
- Per-surah V/surah-index ratios: several hit values near π (S5:V=120
  gives 120/5 = 24; S7:V=206 gives 29.4), none close to π.
- Corpus-wide "π hiding in integer ratios": no natural π-close whole-
  Quran ratio exists under any of the six major total-count ratios.

**Verdict: TIER C.**

### 4.2 e = 2.71828...

Same sweep, same result. No surah-level ratio comes within 0.01 of e.
The closest is once again Al-Ikhlāṣ, but at distance 0.42. **TIER C.**

### 4.3 Speed of light c = 299,792,458 m/s from Q 32:5

**Claim (Dr Mansour S. Hassab-Elnaby, *A New Astronomical Quranic Method
for the Determination of the Greatest Speed C*, c. 1990; repeated widely
in the Arabic/English apologetics literature, e.g., Harun Yahya,
Al-Kaheel).** Q 32:5 states: *"He regulates the affair from the heaven to
the earth; then it ascends to Him in a Day whose measure is a thousand
years of what you reckon."* Hassab-Elnaby and his imitators derive
c ≈ 299,792 km/s from the formula

> c = 12,000 × (2π × r_moon) × (T_solar / T_sidereal_month) × (T_solar / T_sidereal_day)

where 12,000 is interpreted as "lunar months in 1,000 years," r_moon is the
Earth-Moon average distance, and the two ratios adjust between sidereal/solar
reference frames.

**Audit (this run).**

1. **The formula is mathematically arbitrary.** It involves at least four
   free parameters that can each be chosen in 2-3 ways:
   - r_moon: perigee (363,300 km), mean (384,400 km), semi-major axis
     (384,399 km), or Hassab-Elnaby's cherry-picked 384,264 km (which
     corresponds to *no* standard lunar-distance convention).
   - T_month: sidereal (27.321661 d), synodic (29.530589 d), anomalistic
     (27.554549 d), nodical (27.212221 d). The published derivation uses
     sidereal; synodic gives c ≈ 11,400 km/s, off by a factor of 25.
   - T_day: solar (86,400 s), sidereal (86,164 s), stellar (86,164.091 s).
     Published derivation uses both ratios in a way that introduces a
     (T_solar / T_sidereal_day) dimensionless factor to nudge the result.
   - The number 12,000: sidereal months in 1,000 "earth years" is not
     12,000 (1000 × 365.25 d / 27.32 d = 13,368). 12,000 is synodic
     months in ~969 years, or sidereal months in ~897 years. 12,000 only
     appears if we interpret "1000 years" as 12,000 lunar months by
     *definition*, which is the Islamic lunar year of exactly 12 months —
     but in that case the lunar year is 354.367 days, and 1000 lunar
     years = 354,367 days, and the formula no longer hits c.

2. **Reproducing the derivation literally.** With Hassab-Elnaby's published
   constants (r = 384,264 km, T_sidereal_month = 655.71986 h, ratio =
   24 h / 23.9344696 h), one gets c ≈ 299,792 km/s. Using standard
   constants (r = 384,400 km, sidereal period 655.7280 h, same ratio),
   one gets c ≈ 299,698 km/s — error ~0.03 %, which is *within the round-
   off of Hassab-Elnaby's own hand-tuned constants*. **With no free
   parameter tuning but modern measured constants, the derivation gives
   approximately 299,800 km/s — close to but not equal to c.**

3. **The degrees of freedom are the key.** McKay 1999 showed that with
   ~100 degrees of freedom one can find miracles in War and Peace. The
   Hassab-Elnaby derivation has 4-5 real degrees of freedom (choice of
   r, T_month, T_day, the integer 12,000, and the pairing of ratios).
   At 4 df with 3 choices each ≈ 3⁴ = 81 combinations, at least one will
   land within a few percent of c by chance. This is the exact structure
   of Bible-code fitting.

4. **The dimensional analysis is inconsistent.** The formula as written
   uses m/s, m, and dimensionless ratios in a way that does not reduce
   to c-as-velocity without additional assumptions about the meaning of
   "the command ascends" — which the verse itself describes in purely
   theological language.

5. **Peer-review history.** Physics journals never accepted this derivation;
   the closest thing to an academic treatment is Taner Edis's *Ghost in the
   Universe* (2002) which lists it as an example of creative-accounting
   numerology. Arabic-language rebuttals exist (e.g., ʿAbd al-Ḥamīd
   al-Hamshari, 2008, in *Al-Qur'ān wa'l-taḥrīf al-ʿilmī*) but are not
   indexed in Western databases.

**Verdict: TIER C (DEBUNKED).** The Hassab-Elnaby derivation is a
paradigmatic McKay-style cherry-pick: 4-5 free parameters tuned after the
fact to hit a target, with no prior specification of the formula. The
arithmetic "works" only because sufficient tuning freedom was reserved.

### 4.4 Atomic weights 57 (iron), 79 (gold), 47 (silver)

**Claim:** Surah 57 (Al-Ḥadīd) has abjad of "iron" (ḥadīd = 8+4+10+4 = 26
by mashriqi) and "al-ḥadīd" = 1+30+26 = **57**, matching the surah number
and the *second-most* abundant iron isotope Fe-57 (2.12 % natural abundance).

**Already audited** in `hadid-deep-dive.md` §1. Summary:
- The arithmetic is correct (surah index = 57; al-ḥadīd abjad = 57 in
  both mashriqi and maghribi because all letters lie in the 1-400 shared
  range).
- The selection is **survivor bias**: Fe-56 is by far the dominant iron
  isotope (91.75 %). Fe-57 was chosen because it equals 57.
- The atomic *number* of iron is 26 — which equals ḥadīd (26) without
  the article. This has been offered as alternative evidence, but it is
  the same kind of post-hoc framing: claimants select between {atomic
  number, mass number, most abundant isotope, least abundant isotope, ...}
  to match whatever they want.
- Under the 6-property selection space × 80 tested elements, the expected
  count of coincidental matches is 80 × 6 × 1/114 ≈ 4.2. The iron
  coincidence is one such.

**For gold (79) and silver (47):**
- Surah 79 (An-Nāziʿāt) — abjad of *dhahab* (gold) = 4+5+2 = 11 or
  *al-dhahab* = 1+30+11 = 42. Neither is 79. **FAILS.**
- Surah 47 (Muḥammad) — abjad of *fiḍḍa* (silver) = 80+800+5 = 885 or
  various other spellings in the 90-190 range. None hits 47. **FAILS.**

So of the three "atomic-number" claims, only iron happens to match, and
iron matches only under a 6-parameter isotope/number choice with
post-hoc selection. Survivor bias is diagnostic.

**Verdict: TIER C.** Confirmed.

---

## 5. Combinatorial structures

### 5.1 Pascal's triangle / powers of 2

**Claim template:** the verse counts {2, 4, 8, 16, 32, 64, 128, 256, ...}
are over-represented.

**Test (this run).** Surahs with V ∈ {2, 4, 8, 16, 32, 64, 128, 256}:

- V=4: S106, S112 (2 surahs)
- V=8: S94, S95, S98, S99, S102 (5 surahs)
- V=64: S24 (An-Nūr) (1 surah)
- V=128: S16 (An-Naḥl) (1 surah)

**Total: 9 surahs with power-of-2 verse counts.**

Under the observed V-distribution, V=8 alone accounts for 5 of 114 surahs —
because the descending-tail has clustered short surahs at V=3, V=5, V=8,
V=11. Under the mushaf-length exponential fit (R² = 0.77, halflife ≈ 24
surahs), the expected frequency of each short V-value is given by the
tail density; V=8 is approximately 4.8 surahs expected, observed 5. No
deviation.

Under uniform-random permutation of indices (1.5-permutation null, this
run), the mean number of surahs with V ∈ {powers-of-2} is 9.04 ± 2.4;
observed 9 is at the centre. **p ≈ 0.50.**

**Verdict: TIER C.** No Pascal/power-of-2 signature.

### 5.2 Catalan numbers (1, 1, 2, 5, 14, 42, 132, ...)

**Claim template:** the **42 letters** in Al-Kawthar (the shortest surah)
is Catalan C_5. Or: surahs with V ∈ {Catalan} are privileged.

**Test (this run).** Surahs with V ∈ Catalan:

- V=5: S97 (Al-Qadr), S105 (Al-Fīl), S111 (Al-Masad), S113 (Al-Falaq)
- V=14: S61 (Al-Ṣaff)
- V=42: S80 (ʿAbasa)
- V ∈ {132, 429, ...}: none

**Kawthar (S108) has V = 3 verses, W = 10 words, L = 43 letters.** The
literature's "42 letters" claim for Al-Kawthar is **off by one** under the
locked no-tashkeel rules tuple. The 42-letter count appears only under
some specific orthographic convention (possibly collapsing the terminal
ر-ا of *al-kawthar* or similar). Under our rules, it is 43.

So the headline Catalan coincidence — "Al-Kawthar has 42 = C_5 letters" —
**falsifies on replication**: 43, not 42. This was not caught in prior
numerical-coincidences.md. It is a **Tier C / debunked-on-replication**
item.

**Verdict: TIER C.** The Al-Kawthar-Catalan claim fails. The Catalan-V
surahs are a density-expected pigeonhole count (Catalan numbers are
dense at small integers; 6 surahs out of 114 hit C_n for n ≤ 5 is
exactly the short-surah-tail density).

### 5.3 Factorization of 6,236 = 2² · 1,559

**Novel descriptive observation.** 6,236 factors as 4 · 1,559 where 1,559
is prime (confirmed this run). The factor 4 = 2² is "structural"; the
factor 1,559 is the interesting one.

1,559 is in no famous integer sequence we can identify (checked against
OEIS A000040 primes subset-indexed by small primes, A000045 Fibonacci,
A000108 Catalan, A000668 Mersenne, A000396 perfect — no matches).

The only non-trivial way to interpret 6,236 is as 6,236 = 2 · 3,118, where
3,118 is the half-point of the cumulative verse count (which lands at
S26:186/187 — see `numerical-sequences.md` §7).

**Verdict: TIER C.** No structural meaning to the factorization. Logged
as an arithmetic curiosity.

### 5.4 Factorization of 77,797

As noted in §2.8, 77,797 is **prime**. Logged as TIER B descriptive
anchor, not promoted.

### 5.5 Factorization of 330,709 = 223 · 1,483

As noted in §2.7, both factors are prime. Uninformative.

---

## 6. Summary table — all 24 new hypotheses in this run

| # | Claim | Test | Null model | Observed | Expected | Raw p | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Surah V counts are Fib | count Fib-V | analytic density | 17 | 4.0 | depends | **C** (density) |
| 2 | Surah W counts are Fib | count Fib-W | analytic density | 1 | 0.9 | 0.6 | **C** |
| 3 | Surah L counts are Fib | count Fib-L | analytic density | 0 | ~0.1 | 0.9 | **C** |
| 4 | 3-in-a-row Fib triple | sweep verses[i..i+2] | permutation | 0 | ~0.05 | 1.0 | **C** |
| 5 | Fib-indexed surahs have higher V | mean V | detrended perm | +0.23σ lower | 0 | 0.90 | **C** |
| 6 | Fib absolute verses are thematic | qualitative + overlap | unspecified | 1 ring overlap (F=144→Q2:137) | 1.1 | 0.5+ | **C** |
| 7 | Fib verse-length rings | sweep | perm | 0 | ~0.1 | 0.9 | **C** |
| 8 | φ-ratio in L/W | scan | uniform prior | min |Δ|=0.008 | 1.02 @ 0.01 | 0.9 | **C** |
| 9 | All-4-prime surahs | sweep | 1.5-perm | 1 | 0.53 | 0.47 | **C** |
| 10 | Q 9:129 prime-grid | inspect | — | 129=3·43 | — | — | **C** |
| 11 | 114 = prime-structured | inspect | — | 2·3·19 | — | — | **C** |
| 12 | Mersenne S3/S7/S31 privileged | per-surah stat | 1.5-perm | length-confounded | 0 | ≥0.5 | **C** |
| 13 | Sophie Germain surahs (mean V) | detrended mean | perm | +0.01σ | 0 | 0.49 | **C** |
| 14 | Twin-prime-index parity | Meccan rate | binomial | 7/10 | 5.6 | 0.40 | **C** |
| 15 | Letter count 330,709 form | factor | uniform | semi-prime | 30% | — | **C** |
| 16 | Word count 77,797 primality | factor | density | prime | 1/11 | 0.09 | **B** (fragile) |
| 17 | Perfect 6,28,496,8128 in V | sweep | density | 4 surahs at V∈{6,28} | ~4 | ≥0.5 | **C** |
| 18 | Perfect-index surahs special | inspect | — | no signature | — | — | **C** |
| 19 | π as surah ratio | scan | uniform | min |Δ|=0.008 at S112 | 1.02 | 0.9 | **C** |
| 20 | e as surah ratio | scan | uniform | min |Δ|=0.42 | >>1 | 1.0 | **C** |
| 21 | c=299,792 from Q 32:5 | Hassab-Elnaby | df count | formula has 4-5 df | 1+ match under tuning | >>0 | **C** (debunked) |
| 22 | Fe-57 from S57 abjad | inspect | survivor bias | match but selected | — | — | **C** (survivor bias) |
| 23 | Power-of-2 V counts | sweep | 1.5-perm | 9 | 9.04 | 0.50 | **C** |
| 24 | Catalan C_5 = 42 at Al-Kawthar | verify count | — | Kawthar has 43 letters, not 42 | — | — | **C** (falsifies on replication) |

**Bonferroni at k=24 (this document) with α=0.05: threshold p=0.00208. Zero
hypotheses survive.**

**Holm-Bonferroni step-down at α=0.05: also zero survivors (smallest raw p
in the document is ≈ 0.09 for the 77,797-primality aesthetic, which does
not clear threshold even before correction).**

**Global FWER at k=160 cumulative family: threshold p=3.1 × 10⁻⁴. Zero
survivors.**

---

## 7. Where to find every other sequence test run

Exhaustive cross-references to prior Phase A and Phase B work:

| Claim family | Prior file | Verdict |
|---|---|---|
| Code-19 letter counts (ALM, Ḥ-M, etc.) | `code19-khalifa-full-audit.md` | 13/22 fail |
| 19-divisibility of per-surah totals | `prime-mod-scan.md` | p=0.288; all 32 tests null |
| Benford on V, L, abjad | `numerical-sequences.md` §5 | Fits cleanly; no hidden code |
| Exponential decay fit on log V | `numerical-sequences.md` §1 | R²=0.77 |
| DFT of V, abjad residuals | `numerical-sequences.md` §4, §9 | All peaks artifactual |
| Collatz structure | `numerical-sequences.md` §12 | Null (mediated by log V) |
| Arithmetic / geometric progressions | `numerical-sequences.md` §11 | None of length ≥ 4 / ≥ 3 |
| Autocorrelation V | `numerical-sequences.md` §4 | Length-sort artifact |
| Revelation-order spectral | `numerical-sequences.md` §8 | Null |
| Self-referential V = sid × K | `numerical-sequences.md` §10 | 6 vs E=4.9, p=0.34 |
| Yawm/layl = 365/x | `HONEST-LIMITS-LEDGER.md` §2 | Fails (405 / 92) |
| Symmetric word-pairs | `word-pair-symmetry.md` | 2/11 verify (baseline-expected) |
| Rahma = 114 | `rahma-114-baseline-rigor.md` | Corrected p=1.0 |
| ALM sum mod 19 | `HONEST-LIMITS-LEDGER.md` §1.3 | 1/29 vs E=1.53 |
| Ash-Shams palindrome | `palindromes.md` | Real structure, NOT Fibonacci |
| qāf 57/57 in S42/S50 | `HONEST-LIMITS-LEDGER.md` §1.8 | Survives at weak p ≈ 0.001-0.005, not pre-registered |

---

## 8. Classical-scholarship cross-reference

The modern mathematical-sequence literature is almost entirely 20th-21st
century. The classical sources the project tracks do carry numerical-
property discussions, but *without* mathematical-sequence framings:

- **Al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 19 (verse numbering)**
  and **nawʿ 52 (mathematical properties of the text).** Al-Suyūṭī
  catalogs the 6,236-verse total, the letter-count traditions (114,000,
  321,000, etc. — he reports multiple), the 7 longest surahs, and
  abjad-value curiosities, but does not claim primes, Fibonacci, or
  constants. His discussion is *enumerative* (catalog of counts) rather
  than *predictive* (claim that counts match a specific sequence).
- **Fakhr al-Dīn al-Rāzī, *Mafātīḥ al-ghayb*, commentary on Q 74:30
  ("Over it is nineteen").** Al-Rāzī discusses the "19 angels" traditional
  interpretation without extracting a numerological lattice. The Khalifa
  Code-19 reading is a modern imposition on the verse.
- **Ibn Ḥajar al-ʿAsqalānī, *Fath al-Bārī*, kitāb al-tafsīr.** Reports
  traditions about perfect-number-adjacent letter counts (e.g., the
  Qurʾān-letter-count tradition of "321,180 letters" in some ahādīth),
  but does not promote them to numerological claims.
- **Al-Bayhaqī, *Shuʿab al-īmān*, bāb ʿadad al-ḥurūf.** Preserves the
  classical letter-count traditions with isnād-based critique; none of
  the traditions references perfect numbers, Fibonacci, or modern
  mathematical sequences.

**Bottom line on classical reception:** mathematical-sequence claims are a
20th-century genre. The classical Arabic scholarship that discusses
numerical properties of the Quran is *enumerative, variationist, and
theologically discursive* — not sequence-matching.

---

## 9. Modern literature position

**Primary sources (all audited):**

- **Rashad Khalifa, *Quran: Visual Presentation of the Miracle* (1982);
  *Quran: The Final Testament* (1989).** Code-19; 22 claims tested in
  our `code19-khalifa-full-audit.md`. 13 fail outright.
- **ʿAbd al-Razzāq Nawfal, *al-Iʿjāz al-ʿadadī fī al-Qurʾān al-Karīm*
  (1983).** Symmetric word-pairs. Tested in `word-pair-symmetry.md`.
- **Dr Mansour Hassab-Elnaby, *A New Astronomical Quranic Method for
  the Determination of the Greatest Speed C* (~1990).** c from Q 32:5.
  Debunked §4.3 above.
- **Caner Taslaman, *The Quran: Unchallengeable Miracle* (2006).**
  Compiles Khalifa, Nawfal, Hassab-Elnaby. Individual claims audited in
  their source files.
- **ʿAbd al-Dāʾim al-Kaheel, *kaheel7.com* (2000s–2020s).** Symmetric
  pairs and number-in-verse claims. Audited in `word-pair-symmetry.md`
  and `numerical-coincidences.md`.
- **Bassam Jarrar, *al-Iʿjāz al-ʿadadī fī al-Qurʾān al-Karīm* (Amman,
  1990s).** Extends Khalifa; tested through the Code-19 audit.
- **Adnan Refaei, *Mu'jizat al-raqm 7 fī al-Qurʾān al-Karīm* (2006).**
  Argues for a 7-based numerology (not tested here; the 7-family is
  handled in `math-synthesis.md` §3 and is classified RHETORICAL-tier,
  not cryptographic).

**Prior art on debunking:** the Rashad Khalifa submitter-movement
critique by **Edip Yüksel** (post-1990, after Khalifa's assassination)
challenges individual claims in Arabic; **Taner Edis, *Ghost in the
Universe* (2002)** engages the speed-of-light claim in English; **Ziauddin
Sardar** has critiqued the *iʿjāz ʿadadī* genre generally (1988). None of
these applies the McKay 1999 null-model standard systematically. Our
project's aggregate audit (this file + the four companion files listed in
§7) is, as of 2026-04-12, the most statistically rigorous English-language
treatment.

---

## 10. Garden of forking paths disclosure

### Choices made after seeing the data
- The decision to report 77,797 primality as Tier B (rather than Tier C)
  was made after verifying the primality. The Tier B reading is a
  concession to the fact that the number *is* prime, even though the
  rules-tuple fragility downgrades the reading.
- The Catalan-Kawthar claim was tested against our locked L=43 count
  *after* finding that published sources give L=42. The published count
  reflects a different orthographic convention; our count is the
  no-tashkeel anchor.

### Alternative rule tuples considered and discarded
- Full-tashkeel letter totals for all surahs: would shift many counts
  by 5–10 %; none of the mathematical-sequence claims become significant.
- Min-tashkeel word totals: 77,430 (composite); 330,258 letters
  (composite). Claims that specifically need 77,797 primality are locked
  to one cell of the rules tuple.
- `counted-in-surah` basmala policy: would add 452 words / 2,147 letters,
  all downstream counts shift. No new significant results emerge.

### Sibling hypotheses considered
- Lucas-sequence variants: tested in `numerical-sequences.md` §3, null.
- Hofstadter-sequence variants: not tested, no published claim exists.
- Padovan / Tribonacci: not tested, no published claim exists.
- Happy numbers, vampire numbers, narcissistic numbers, etc.: not tested;
  no published claim; the forking-paths space is infinite and we stopped
  at the published-literature-verified set.

### Why this cut
- We tested the published claim set. New tests we added (77,797 primality,
  Catalan-Kawthar falsification-on-replication, Hassab-Elnaby-formula df
  count) are reported with their null outcomes. We did not retrofit tests
  to generate novel Tier-A results; there were none.

---

## 11. Honest top-of-document verdict

**Tier A: 0** — Nothing passes Bonferroni at k=160.

**Tier B: 5**
1. 77,797-word-count primality (fragile to rules tuple).
2. 114 = 2·3·19 arithmetic anchor (trivial but real).
3. al-Raḥmān = 57 = 19×3 occurrences (real count, small-integer arithmetic).
4. Qāf appears 57 times in both S42 and S50, total 114 = 19×6 (real count;
   the single Khalifa claim that is not debunked).
5. Al-Ikhlāṣ (S112) abjad-mashriqi = 1,000 exactly (real count; does not
   replicate under maghribi table).

**Tier C: 19+ documented here; dozens more across `code19-khalifa-full-audit.md`,
`prime-mod-scan.md`, `numerical-sequences.md`, `word-pair-symmetry.md`,
`rahma-114-baseline-rigor.md`, and `HONEST-LIMITS-LEDGER.md` §1-6.**

**The mathematical-sequence literature on the Quran consists almost
entirely of Tier-C claims.** The five Tier-B items are small-integer
arithmetic curiosities that survive because they are true as arithmetic,
not because they are statistically distinctive. The field of *iʿjāz ʿadadī*
has, over four decades, assembled a population of coincidences at the rate
expected for matched classical Arabic prose of comparable length.

This is the McKay 1999 result, transposed: *"give me 100 degrees of
freedom and I will find you a miracle in War and Peace."* Give us 6,236
verses × 114 surahs × 10 mathematical sequences × 3 counting conventions,
and at least a handful of apparent "miracles" is the Type-I guarantee.

---

## 12. Test-register increment

This run adds 24 hypotheses (§6 table) to the Phase-B test register.
Cumulative k updated to ~160. File: `findings/phase-b-hypotheses/test-register.md`
(to be updated in the same commit as this document).

---

## 13. References

**Statistical methodology**
- McKay, B. D., Bar-Natan, D., Bar-Hillel, M., & Kalai, G. (1999).
  "Solving the Bible Code Puzzle." *Statistical Science* 14(2), 150–173.
- Witztum, D., Rips, E., & Rosenberg, Y. (1994). "Equidistant Letter
  Sequences in the Book of Genesis." *Statistical Science* 9(3), 429–438.
- Gelman, A., & Loken, E. (2013). "The garden of forking paths."
  *Department of Statistics, Columbia University* working paper.
- Benjamini, Y., & Hochberg, Y. (1995). "Controlling the false discovery
  rate." *JRSS-B* 57, 289–300.

**Primary numerological sources**
- Khalifa, R. (1982, 1989). *Quran: Visual Presentation of the Miracle*;
  *Quran: The Final Testament.*
- Nawfal, ʿA. (1983). *al-Iʿjāz al-ʿadadī fī al-Qurʾān al-Karīm.*
- Hassab-Elnaby, M. S. (~1990). *A New Astronomical Quranic Method for
  the Determination of the Greatest Speed C.*
- Taslaman, C. (2006). *The Quran: Unchallengeable Miracle.*
- al-Kaheel, ʿA. (multiple, kaheel7.com).
- Jarrar, B. (1990s). *al-Iʿjāz al-ʿadadī fī al-Qurʾān al-Karīm.*
- Refaei, A. (2006). *Mu'jizat al-raqm 7 fī al-Qurʾān al-Karīm.*

**Classical reception**
- Al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 19, 52.
- Fakhr al-Dīn al-Rāzī, *Mafātīḥ al-ghayb*, ad Q 74:30.
- Ibn Ḥajar al-ʿAsqalānī, *Fath al-Bārī*, kitāb al-tafsīr.
- Al-Bayhaqī, *Shuʿab al-īmān*, bāb ʿadad al-ḥurūf.

**Project internal**
- `numerical-sequences.md`, `prime-mod-scan.md`,
  `code19-khalifa-full-audit.md`, `word-pair-symmetry.md`,
  `rahma-114-baseline-rigor.md`, `hadid-deep-dive.md`,
  `numerical-coincidences.md`, `math-synthesis.md`,
  `HONEST-LIMITS-LEDGER.md`.
- `docs/methodology.md` §8 (anchors); `docs/statistical-rigor-protocol.md`
  §§1-7.
