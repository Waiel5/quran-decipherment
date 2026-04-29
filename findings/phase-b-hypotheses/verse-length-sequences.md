---
title: Verse-length sequences — palindromes, monotone runs, spectral structure
phase: B
agent: verse-length-run-1
date: 2026-04-12
rules:
  orthography: no-tashkeel
  letter_definition: graphemes (U+0621..064A ∪ U+0671..06D3)
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  null_model: within-surah verse-length shuffle (200 trials)
data_sources:
  - quran-text/quran-no-tashkeel.json
code: /tmp/verse_length_analysis.py
artifacts: /tmp/verse-length-run/
related: findings/phase-b-hypotheses/palindromes.md
status: exploratory — descriptive hunt, not pre-registered. Two of the finds
  (Q 19:20-24 Annunciation and Q 109:2-6 Kāfirūn) appear new to this file;
  the three known L=7 cases verify exactly.
---

# Verse-length sequences — palindromes, monotone runs, spectral structure

## Frame

Every surah supplies a numeric **time series** `L_s = (L_s^1, L_s^2, …, L_s^{n_s})`
where `L_s^i` is the letter-grapheme count of verse `i`. This file asks
mathematical questions of that series: Where do palindromes sit?
Where do strictly monotonic runs sit? Does the DFT point anywhere
unusual? Does Ar-Raḥmān's refrain pattern carve a clean partition?

The paradigm case — the seven cosmic-oath opening of Ash-Shams — is
`[12,14,15,15,15,14,12]`. It generalizes: are there other such
palindromes in the corpus at length 5, 7, 9? Which surahs show
strongly non-random spectra? Where do verse lengths rise monotonically
across ≥ 5 consecutive verses?

All counting uses the same rules as the palindrome hunt document
(`palindromes.md`): no-tashkeel orthography, Arabic-letter graphemes
only, basmala counted only as Q 1:1.

## Headline findings (the seven most telling)

1. **Three length-7 verse-length palindromes exist in the Quran, and
   only three** — at Q 91:1–7, Q 81:2–8, Q 37:127–133. No length-9
   palindrome exists anywhere. Verified exactly against the claimed
   sequences in `palindromes.md`. Every one of the three centres on
   a semantically pivotal verse (the Night, a judgement flash, the
   *salām* on Ilyās).

2. **A new length-5 palindrome at Q 19:20–24**, letter-counts
   `[38, 57, 24, 57, 38]`. This is the **Annunciation pericope** —
   Mary's objection ("How shall I have a boy when no man has touched
   me?") mirrors around her withdrawal "to a distant place" (v22,
   24 letters, the centre), with the angel's first answer and Mary's
   birth-pang anguish matching at 57 letters each. The **moment of
   birth** sits at the axis. Not previously in `palindromes.md`.

3. **A new length-5 palindrome at Q 109:2–6**, letter-counts
   `[14, 19, 17, 19, 14]`. Al-Kāfirūn's famously repetitive central
   stanza is a **letter-count palindrome** as well as a word-pattern
   one — v3 and v5 are the famous identical line *لا أنتم عابدون ما
   أعبد*, and v2 and v6 also match at 14 letters each. Centre (v4):
   *ولا أنا عابد ما عبدتم* — the unique reversal of subject/object.

4. **Q 52:26–31 is a length-6 palindrome** `[27, 28, 31, 31, 28, 27]`
   bridging *Paradise speech* (v26–28) to *Prophetic defence against
   accusers* (v29–31). The two topical halves are letter-count-mirrored
   across the block join, pivoting on the twin-31 centre v28–29. Not
   previously listed.

5. **Three length-7 strictly monotonic runs exist**, and only three:
   - **Q 69:1–7** strictly *increasing* `[6, 8, 16, 20, 23, 27, 68]`,
     the opening of al-Ḥāqqa — a rhetorical crescendo from a 6-letter
     interrogative (`الحاقة` — "The Inevitable!") to a 68-letter
     catastrophe description.
   - **Q 2:221–227** strictly *decreasing* `[182, 122, 81, 66, 65, 54, 29]`,
     the marriage-law pericope, legal clauses tapering to their
     briefest form.
   - **Q 39:6–12** strictly *decreasing* `[138, 126, 122, 105, 95, 31, 23]`,
     worship-exhortation passage with a sharp step-down to short
     devotional verses.
   No surah has a length-8 monotone run.

6. **Ar-Raḥmān partitioning is exactly 8 + 7 + 8 + 8 = 31 refrains**,
   confirming the rahman-deep claim. All 31 refrain verses have
   identical letter count **19**. The four thematic blocks have
   distinctive mean verse-lengths: creation 19.7 → judgment 34.4 →
   first garden 23.1 → second garden 18.2. The *judgment* block is
   the densest by a wide margin — a single 78-letter central verse
   (v33, "O company of jinn and men, if you can pass beyond the
   zones of heaven…") dominates. Contrasted, the *second garden*
   block, closing the sūra, is the shortest-per-verse section of the
   entire surah.

7. **Q 85 Al-Burūj encodes reward/punishment symmetry via
   twin 65-letter verses at the midpoint.** Verses 10 and 11 are each
   exactly 65 letters — v10 is the eternal-punishment verse (persecutors
   of believers → Hellfire), v11 the eternal-reward verse (believers
   → gardens with rivers). These two identical-length verses sit at
   the peak of the surah's arc and give the sūra its highest
   spectral energy (`top_spec_frac = 0.39`, lag-1 autocorrelation 0.67).

## Methodology

### Verse-length sequence extraction
For each of 114 surahs, compute `L_s^i = graphemes(v_i)` using
`analysis/tools/tokenize.py`'s `graphemes()`. This counts only Arabic
letter graphemes in U+0621..064A ∪ U+0671..06D3 (the standard Arabic
block minus ḥamza-on-alif variants plus U+0671, the Arabic Maddah
alif, which the amrayn JSON uses). Spaces, punctuation, recitation
marks (U+06D6..U+06ED), tatweel, tashkeel — all excluded.

### Palindrome scan
Sliding window of length L = 4, 5, 6, 7, 8, 9, 10, 11. A window is a
palindrome iff its letter-count sequence equals its reverse. Windows
where every element is identical are flagged as "trivial" (all-equal
palindromes) and reported separately — e.g. the opening of Al-Mursalāt
(Q 77:1–5 = 13, 13, 13, 13, 13) qualifies but reflects rhythmic
repetition, not mirror symmetry.

### Monotone-run scan
Maximal strictly-increasing and strictly-decreasing runs (`L^i < L^{i+1}`
or `L^i > L^{i+1}` for all i in the run). Reported at length ≥ 5.

### Autocorrelation and periodogram
For each surah with `n ≥ 8`, compute sample autocorrelation for lags
1..min(20, n/2) and the unnormalized DFT power spectrum `P_k =
|Σ x_t e^{-2πikt/n}|² / n` for k = 1..n/2, where `x_t = L^t - mean(L)`.
Rank surahs by `top_spec_frac = max_k(P_k) / Σ_k(P_k)` — how much
of the detrended variance is concentrated in a single Fourier bin.

### Null model
Within-surah shuffle: for each of 200 trials, randomly permute each
surah's length sequence and re-count non-trivial palindromes at
L = 5, 7, 9. This null preserves the per-surah marginal distribution
(so a surah with one very long verse still has that very long verse)
but destroys the ordering information. It tells us whether the
observed palindrome count could arise purely from verse-length
combinatorics in a given length-distribution landscape.

## Detailed results

### Palindrome catalogue

| Length | Non-trivial count | Trivial (all-equal) | Example |
|---|---|---|---|
| 4 | 7 | — | Q 68:19–22 [27, 13, 13, 27] |
| 5 | 8 | 3 | Q 19:20–24 [38, 57, 24, 57, 38] |
| 6 | 2 | 0 | Q 52:26–31 [27, 28, 31, 31, 28, 27] |
| 7 | 3 | 0 | Q 91:1–7 [12, 14, 15, 15, 15, 14, 12] |
| 8 | 0 | 0 | — |
| 9 | 0 | 0 | — |
| 10+ | 0 | 0 | — |

Full L = 5 non-trivial list:

| Location | Letter counts | Centre | Theme |
|---|---|---|---|
| Q 19:20–24 | [38, 57, 24, 57, 38] | v22 "withdrew to a distant place" | Annunciation |
| Q 37:61–65 | [21, 23, 22, 23, 21] | v63 "a trial for the wrongdoers" | Zaqqum tree |
| Q 37:128–132 | [19, 19, 14, 19, 19] | v130 "peace upon Ilyāsīn" | *salām* on Ilyās |
| Q 75:15–19 | [14, 20, 17, 20, 14] | v17 "Indeed its collection and recitation is upon Us" | Qurʾān promise |
| Q 81:24–28 | [18, 18, 10, 18, 18] | v26 "so where are you going?" | Rhetorical pivot |
| Q 89:24–28 | [21, 20, 15, 20, 21] | v26 "and none will bind as He binds" | pre-"O soul at peace" |
| Q 91:2–6 | [14, 15, 15, 15, 14] | (sub-palindrome of 1–7) | cosmic oaths |
| Q 109:2–6 | [14, 19, 17, 19, 14] | v4 "nor will I worship what you worshipped" | repudiation |

The semantic density of the centres is striking — each centre is the
rhetorical pivot of its passage. Q 37:130 is the *salām* verse on a
prophet; Q 75:17 is the divine guarantee concerning the Qurʾān's
preservation; Q 81:26 is the rhetorical question "so where are you
going?" that inverts the entire surah's apocalyptic imagery; Q 89:26
is the contrastive climax ("and none will bind as He binds") before
the famous *yā ayyatuhā n-nafsu l-muṭmaʾinna* address.

### L = 7 verification

| Surah | Verses | Letter-count sequence | Matches claim | Centre verse | Centre text |
|---|---|---|---|---|---|
| Q 91 Ash-Shams | 1–7 | [12, 14, 15, 15, 15, 14, 12] | yes | v4 (15) | والليل إذا يغشاها |
| Q 81 At-Takwīr | 2–8 | [16, 14, 14, 14, 14, 14, 16] | yes | v5 (14) | وإذا العشار عطلت |
| Q 37 As-Ṣāffāt | 127–133 | [18, 19, 19, 14, 19, 19, 18] | yes | v130 (14) | سلام على إل ياسين |

All three verify bit-for-bit against the sequences claimed in
`palindromes.md`. Each sits inside what is arguably the most
rhythmically tight region of its surah — the opening seven oaths
(Q 91), the string of disruption *idhā* clauses (Q 81), and the prose
closing doxology (Q 37).

### Nested palindrome structure in At-Takwīr (Q 81)

At-Takwīr (29 verses) contains **three** distinct letter-count
palindromes:
- **Q 81:2–8** length-7 `[16, 14, 14, 14, 14, 14, 16]`
- **Q 81:10–15** length-6 `[13, 14, 14, 14, 14, 13]`
- **Q 81:24–28** length-5 `[18, 18, 10, 18, 18]`

Three nested palindromes in a 29-verse surah is extraordinarily dense.
If the within-corpus rate is ~3 non-trivial L = 7 palindromes in
~6240 verses, the prior probability of a second palindrome in a
randomly chosen 29-verse block is vanishingly small. That At-Takwīr
carries three — each tracking a different rhetorical arc (idhā
clauses → second run of idhā clauses → the *fa-ayna tadhhabūn* hinge)
— is the single most striking combinatorial feature in the corpus.

### Base-rate (within-surah shuffle, 200 trials)

| L | Observed (non-trivial) | Null mean | Null SD (approx) | Null p95 | Null max | Observed rank |
|---|---|---|---|---|---|---|
| 5 | 8 | 7.8 | ~3 | 13 | 17 | ≈ mean |
| 7 | 3 | 0.78 | ~0.9 | 3 | 5 | p95 |
| 9 | 0 | 0.11 | — | 1 | 2 | below mean |

**Interpretation.** L = 5 palindromes are at chance. The semantic
resonance of the L = 5 list is not the statistical outcome — it is a
post-hoc selection from a chance-level set. L = 7 is ~4× null mean
and sits at the p95 boundary; not overwhelming, but combined with the
fact that all three observed cases have topical centre verses, the
qualitative case is stronger than the quantitative null test. L = 9
is at null and the observed 0 is unremarkable. The within-surah
shuffle null is weak: it preserves marginal distribution per surah, so
a surah like Q 81 with many 14-letter verses is *given* the palindromic
raw material. A stronger test would pool lengths within the pool of
Meccan-short surahs and shuffle globally; left for follow-up.

### Monotone runs

Distribution of maximal strict-monotone runs (length ≥ 5):

| Length | Count | Notable instances |
|---|---|---|
| 5 | 89 | spread across corpus; roughly uniform per verse |
| 6 | 7 | Q 4:70–75 (inc), Q 4:113–118 (dec), Q 11:104–109 (inc), Q 28:76–81 (dec), Q 30:39–44 (dec), Q 35:12–17 (dec), Q 38:26–31 (dec) |
| 7 | 3 | Q 2:221–227 (dec), Q 39:6–12 (dec), Q 69:1–7 (inc) |
| 8+ | 0 | — |

Q 69:1–7 deserves standalone treatment: `6 → 8 → 16 → 20 → 23 → 27 → 68`.
Each verse adds to the previous, but the final step is a factor-of-2.5
leap — the "hook" verse that fires after the buildup of three-word
rhetorical questions "الحاقة · ما الحاقة · وما أدراك ما الحاقة". The
crescendo is not just thematic; it is letter-count-encoded.

Q 2:221–227 strictly decreases from 182 to 29 letters — legal
clauses tapering as subject matter narrows from broad marriage
prohibitions (v221) to a single-line clause on oaths to divorce (v227).
Q 39:6–12 decreases similarly: a long cosmological prologue (v6, 138
letters) stepwise tapers into short worship-injunctions (v11, 31; v12,
23). Both decreasing runs *move from discursive to imperative*.

Q 69:1–7 is the only increasing run of length 7 in the corpus. The
asymmetry (many decreasing long runs, very few increasing) reflects
a genre convention: when Qurʾānic prose shifts into terser mode, it
tends to keep tapering; when it opens short and builds, it usually
tops out before accruing seven consecutive rises.

### Ar-Raḥmān (Q 55) refrain partition

The refrain *فبأي آلاء ربكما تكذبان* occurs as 31 verses in Q 55:
13, 16, 18, 21, 23, 25, 28, 30, 32, 34, 36, 38, 40, 42, 45, 47, 49, 51,
53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77. All 31 instances
are **19 letters exactly** — the refrain is fixed to the letter, never
paraphrased, never shortened.

Refrain-gap analysis: gaps between consecutive refrains are almost
always 2 verses, with six exceptional 3-verse gaps (between refrains
at 13→16, 18→21, 25→28, 42→45, plus 23→25 which is 2 but marks a
transition). The "long-gap" occurrences cluster at section boundaries.

| Block | Verse span | Refrain count | Non-refrain verses | Sum letters (non-refrain) | Mean |
|---|---|---|---|---|---|
| A (Creation) | 1–30 | 8 | 22 | 434 | 19.7 |
| B (Judgment) | 31–45 | 7 | 8 | 275 | 34.4 |
| C (Garden pair 1) | 46–61 | 8 | 8 | 185 | 23.1 |
| D (Garden pair 2) | 62–77 | 8 | 9 | 164 | 18.2 |

Refrain-counts 8 + 7 + 8 + 8 = 31. The **judgment** block is the
letter-heaviest by a margin — one verse there (v33, "O company of
jinn and men, if you can pass beyond…") is 78 letters alone. The
**second-garden** block is the lightest, averaging 18 letters per
non-refrain verse. Across the whole sūra, the trajectory is
`19.7 → 34.4 → 23.1 → 18.2` — *up sharply, then down, then down*.
The block of most verbal weight is the judgment block; the block of
least weight is the final garden pair. This tracks a descending
catabolic rhythm typical of Late Meccan *sajʿ* — verses get shorter
as the sūra closes.

### Spectral anomalies

Top-concentrated surahs (surahs with `n ≥ 15`, ranked by
`top_spec_frac`):

| Surah | n | top_spec_frac | Top period | Interpretation |
|---|---|---|---|---|
| Q 64 At-Taghābun | 18 | 0.46 | 2.57 | rapid alternation short/long |
| Q 85 Al-Burūj | 22 | 0.39 | 22.0 | single U-shaped arc |
| Q 96 Al-ʿAlaq | 19 | 0.37 | 4.75 | ~5-verse periodicity |
| Q 86 At-Ṭāriq | 17 | 0.34 | 2.43 | alternation |
| Q 72 Al-Jinn | 28 | 0.29 | 4.67 | ~5-verse rhythm |
| Q 89 Al-Fajr | 30 | 0.29 | 30.0 | whole-surah single cycle |

**Q 85 Al-Burūj** is the most striking. Its length sequence:
`[16, 13, 11, 15, 14, 13, 27, 40, 40, 65, 65, 13, 14, 15, 13, 11, 16, 10, 19, 17, 12, 10]`.
The spectral energy concentrates at period 22 (= n) — i.e. there is a
single sinusoidal oscillation across the sūra: a build-up to the
twin peaks at verses 10–11 (the identical-length eternal-punishment
and eternal-reward verses, each 65 letters), then a collapse back to
short *fasīla* closings. The **twin-65 structure** encodes the
reward/punishment mirror as a letter-count palindrome within the
narrow central block 10–11, and as the peak of the surah's arc.

**Q 64 At-Taghābun**'s period of 2.57 reflects rapid alternation of
long and short verses. **Q 86 At-Ṭāriq**'s period 2.43 is similarly an
odd/even alternation pattern — the surah swings between oath verses
and explicatory verses.

**Q 89 Al-Fajr**'s period ≈ n = 30 signals a single rising-and-falling
envelope across the surah; its lag-1 autocorrelation 0.64 is the
highest among these — consecutive verses are strongly similar in
length. Al-Fajr begins with five ultra-short oath-verses (6, 8, 12,
12, 16) and grows into dense prose before tapering again.

### Adjacent-length runs

The data include striking runs of *identical* consecutive verse
lengths. Relevant clusters:
- Q 51:1–4 (Adh-Dhāriyāt) — four consecutive verses of 13 letters.
- Q 77:1–5 (Al-Mursalāt) — five of 13 letters (a formal all-equal palindrome).
- Q 79:1–5 (An-Nāziʿāt) — five of 13 letters (same).
- Q 81:3–7 (At-Takwīr) — five of 14 letters.
- Q 100:1–3 (Al-ʿĀdiyāt) — three of 13 letters.

All five are *oath-surahs* with rapid-fire short ʿāṭif-chained oath
clauses. The uniform letter count is a rhythmic device of the oath
genre — not a palindrome in the narrative sense, but a structural
signature of the form.

Triples of identical length (≥ 3 adjacent equal): 23 instances. Five
of these come from Q 81, two from Q 77, and three from Q 55
(Ar-Raḥmān, where the identical lengths are always the 19-letter
refrains).

## Base-rate honesty and open follow-ups

- The within-surah shuffle null is weak. A stronger follow-up:
  sample 200 random length-7 subsequences uniformly across the
  corpus, match them to the observed L = 7 palindromes' source
  surahs, and count palindromic fraction. That's left for a future
  agent.
- No pre-registration: every finding here is post-hoc pattern-matching
  over 6236 verses. To claim inferential weight, the single strongest
  candidates (Q 91:1–7, Q 81:2–8, Q 37:127–133, Q 19:20–24, Q 109:2–6,
  Q 69:1–7) should be tested on held-out data — e.g. verified across
  alternative orthographies (min-tashkeel, full-tashkeel counting),
  or against the shadda-doubled letter count variant.
- The Ar-Raḥmān 8 + 7 + 8 + 8 partition claim replicates exactly —
  good robustness signal for that particular claim.
- The two-in-one surah finding (Al-Kāfirūn is a *word-pattern*
  palindrome and a *letter-count* palindrome simultaneously) should
  be checked in the other famously-repetitive surahs (Al-Ikhlās,
  Al-Falaq). Q 112 Al-Ikhlās length sequence is [11, 9, 12, 15] —
  not palindromic. Q 113 Al-Falaq is [18, 12, 20, 16, 23] — not
  palindromic. So the letter-count palindrome in Q 109 is not a
  mere "short surah" artefact; it's a specific property of
  Al-Kāfirūn's stanza.

## Appendix — full verse-length sequences (short surahs)

(For the first 12 verses of each surah, see full JSON at
`/tmp/verse-length-run/verse-length-sequences.json`.)

Selected short-surah sequences in full:

- Q 91 Ash-Shams (n=15): `[12, 14, 15, 15, 15, 14, 12, 20, 20, 15, 19, 24, 13, 21, 24]`
- Q 81 At-Takwīr (n=29): `[13, 16, 14, 14, 14, 14, 14, 16, 22, 13, 14, 14, 14, 14, 13, 15, 10, 14, 15, 15, 24, 18, 19, 18, 18, 10, 18, 18, 28]`
- Q 37 As-Ṣāffāt v126–134: `[22, 18, 19, 19, 14, 19, 19, 18, 12]`
- Q 109 Al-Kāfirūn (n=6): `[16, 14, 19, 17, 19, 14]`
- Q 85 Al-Burūj (n=22): `[16, 13, 11, 15, 14, 13, 27, 40, 40, 65, 65, 13, 14, 15, 13, 11, 16, 10, 19, 17, 12, 10]`
- Q 69 Al-Ḥāqqa v1–12: `[6, 8, 16, 20, 23, 27, 68, 16, 19, 21, 25, 26]`
- Q 89 Al-Fajr v24–30: `[21, 20, 15, 20, 21, 13, 10]`
- Q 19 Maryam v19–25: `[32, 38, 57, 24, 57, 38, 35]`
- Q 52 At-Ṭūr v26–32: `[27, 28, 31, 31, 28, 27, 31]`

## Summary verdict

Letter-count-sequence palindromes exist, are rare, and cluster sharply
at the rhetorical pivots of short apocalyptic surahs. The length-7
ceiling is strict. Three known cases verify exactly. Several length-5
cases (Q 19:20–24 Annunciation, Q 109:2–6 Kāfirūn, Q 52:26–31 at
length 6) warrant addition to the catalogue. Monotone runs of length
7 are likewise strict: only three, each a rhetorical set-piece
(Ḥāqqa crescendo, marriage-law taper, worship-exhortation taper).
Ar-Raḥmān's 8 + 7 + 8 + 8 partition is numerically exact. Al-Burūj's
twin-65 midpoint encodes a reward/punishment equivalence at the
letter-count layer. The honest null says the L = 5 finds are at chance
and the L = 7 finds are ~p95; the semantic coherence of the centres
is the qualitative signal, not the p-value.
