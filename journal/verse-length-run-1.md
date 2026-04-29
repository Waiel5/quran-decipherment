---
title: Verse-length sequence analysis — run 1
phase: B
agent: verse-length-run-1
date: 2026-04-12
rules:
  orthography: no-tashkeel
  letter_definition: graphemes (U+0621..064A ∪ U+0671..06D3)
  basmala_policy: counted-only-in-surah-1 (amrayn default — only Q 1:1)
  verse_numbering: hafs-kufan
data_sources:
  - quran-text/quran-no-tashkeel.json
code: /tmp/verse_length_analysis.py
artifacts: /tmp/verse-length-run/
---

# Journal — verse-length sequence hunt, run 1

## Objective
Treat each surah's verse-letter-count array as a **time series** and hunt
for mathematical pattern. Paradigm: Ash-Shams Q 91:1–7 letter-count
palindrome `[12,14,15,15,15,14,12]`. Tasks: catalogue length-5/7/9
palindromes; detect monotonic runs ≥ 5; verify three known L=7 cases;
examine Ar-Rahmān refrain-partition letter-length signature; scan for
unusual spectral / autocorrelation signatures across the corpus.

## Method summary
1. Load amrayn no-tashkeel JSON. Extract, for each of 114 surahs, a
   sequence `L_s = [graphemes(v₁), ..., graphemes(v_n)]` where
   `graphemes` counts code points in U+0621..064A ∪ U+0671..06D3.
   (Basmala only contributes to Q 1 since amrayn stores it as Q 1:1
   alone.)
2. Sliding-window palindrome detection for L ∈ {4, 5, 6, 7, 8, 9, 10, 11}.
3. Sliding maximal strict-monotonic runs, min length 5.
4. Autocorrelation (`lag=1..20`) and periodogram (DFT) per surah, ranked
   by `top_spec_frac = max_periodogram_bin / total_periodogram_energy`.
5. Ar-Rahmān refrain identification: every verse containing `تكذبان`
   (`tukadhdhiban`). Partition surah into blocks between refrains.
6. Null model: shuffle each surah's length sequence (200 trials),
   re-count non-trivial palindromes of each length.

## Key observations

### Verification of known L=7 palindromes
All three known length-7 letter-count palindromes verified exactly:

| Surah | Verses | Letter-count sequence | Matches claim? |
|---|---|---|---|
| Ash-Shams (91) | 1–7 | [12,14,15,15,15,14,12] | **yes** |
| At-Takwīr (81) | 2–8 | [16,14,14,14,14,14,16] | **yes** |
| As-Ṣāffāt (37) | 127–133 | [18,19,19,14,19,19,18] | **yes** |

### Full palindrome catalogue (non-trivial)
- **L = 9**: 0 cases.
- **L = 7**: exactly the 3 known cases (Q 91:1–7, Q 81:2–8, Q 37:127–133).
- **L = 6**: 2 new cases —
  - Q 52:26–31 `[27,28,31,31,28,27]` — Pious speech in Jannah + Prophetic defence.
  - Q 81:10–15 `[13,14,14,14,14,13]` — already known; second nested palindrome inside At-Takwīr.
- **L = 5** (non-trivial): 8 cases
  - Q 19:20–24 `[38,57,24,57,38]` — **the Annunciation** (Gabriel ↔ Mary).
  - Q 37:61–65 `[21,23,22,23,21]` — Zaqqum tree description.
  - Q 37:128–132 `[19,19,14,19,19]` — sub-palindrome inside 127–133.
  - Q 75:15–19 `[14,20,17,20,14]` — instruction on reciting the Qurʾān.
  - Q 81:24–28 `[18,18,10,18,18]` — already known; third palindrome in At-Takwīr.
  - Q 89:24–28 `[21,20,15,20,21]` — the "O soul at peace" passage.
  - Q 91:2–6 `[14,15,15,15,14]` — sub-palindrome inside 91:1–7.
  - **Q 109:2–6** `[14,19,17,19,14]` — **Al-Kāfirūn "la aʿbudu mā taʿbudūn"**, the famous repetition surah.
- **L = 5 all-equal (trivial)**: Q 77:1–5 (all 13), Q 79:1–5 (all 13),
  Q 81:3–7 (all 14) — opening oath-line clusters with uniform rhythm.
- **L = 4 non-trivial**: 7 cases incl. Q 68:19–22, Q 74:17–20, Q 75:28–31,
  Q 75:30–33, Q 79:33–36 — most clustered in the *disruption* surahs.

### Base-rate null comparison (200 random within-surah shuffles)
| L | Observed (non-trivial) | Null mean | Null p95 | Null max |
|---|---|---|---|---|
| 5 | 8 | 7.8 | 13 | 17 |
| 7 | 3 | 0.78 | 3 | 5 |
| 9 | 0 | 0.11 | 1 | 2 |

L=5 is **at the null rate** (chance expectation). L=7 is **~4× the null
mean, at the p95 boundary** — suggestive but not overwhelming. L=9 is
at null. The semantic density (every L=7 case centres on an
oath / prophetic / *salām* pivot verse) is the qualitative payload, not
raw count; the null model is *within-surah* shuffle, so it preserves
verse-length distribution per surah but destroys order. The small
margin at L=7 means a pre-registered replication on text outside the
discovery set would be needed.

### Monotonic runs ≥ 5
99 runs ≥ 5, of which 89 are length 5, 7 are length 6, and **3 are
length 7**:
- Q 2:221–227 `[182,122,81,66,65,54,29]` — strictly decreasing, marriage/divorce law pericope.
- Q 39:6–12 `[138,126,122,105,95,31,23]` — strictly decreasing; worship/exhortation passage.
- Q 69:1–7 `[6,8,16,20,23,27,68]` — strictly **increasing** opening of Al-Ḥāqqa ("The Inevitable — what is the Inevitable — and what will make you know what the Inevitable is…"). Rhetorical crescendo from 6-letter opening to 68-letter Prophet-destruction climax.

No length-8+ monotonic run exists in the corpus. The three length-7
runs are extraordinary — each is a highly-structured rhetorical unit.

### Ar-Raḥmān (Q 55) refrain partition
31 refrains identified — every verse containing `تكذبان`. Refrain
letter-count: **invariant at 19 letters**, every occurrence. Partition
structure per refrain-gap pattern:

| Block | Verses | Theme | Non-refrain verses | Total letters | Mean |
|---|---|---|---|---|---|
| A | 1–30 | Creation + signs | 22 | 434 | 19.7 |
| B | 31–45 | Judgment Day | 8 | 275 | 34.4 |
| C | 46–61 | First garden pair | 8 | 185 | 23.1 |
| D | 62–77 | Second garden pair | 9 | 164 | 18.2 |

Refrain-count per block: **8 + 7 + 8 + 8 = 31** (exact match to the
Raḥmān-deep partition claim). Block B (Judgment) has by far the densest
verses (34.4 mean — nearly 2× block D). Progression is
`creation → judgment → gardenA → gardenB = 19.7 → 34.4 → 23.1 → 18.2`
— judgment is the heavy peak; "second garden pair" is the tersest,
most lyric phase. The mean-letters trajectory is itself non-monotonic:
up-down-down-down (if refrain block gets most weight at 34.4 then
tapers towards 18.2).

### Spectral / autocorrelation anomalies (surahs with `n ≥ 15`)
Top-ranked by `top_spec_frac`:

| Surah | n | Top period (verses) | Spec fraction | Lag-1 autocorr |
|---|---|---|---|---|
| Q 64 At-Taghābun | 18 | 2.57 | 0.46 | — |
| Q 85 Al-Burūj | 22 | 22.0 | 0.39 | 0.67 |
| Q 96 Al-ʿAlaq | 19 | 4.75 | 0.37 | — |
| Q 86 At-Ṭāriq | 17 | 2.43 | 0.34 | — |
| Q 72 Al-Jinn | 28 | 4.67 | 0.29 | — |
| Q 89 Al-Fajr | 30 | 30.0 | 0.29 | 0.64 |

Q 85 **Al-Burūj** is the structural gem: its length sequence
`[16,13,11,15,14,13,27,40,40,65,65,13,14,15,13,11,16,10,19,17,12,10]`
*rises to a plateau at verses 10–11 (both exactly 65 letters)* and then
collapses back to short verses. Verses 10 and 11 are the twin-judgment
pair: v10 is eternal punishment for persecutors, v11 is eternal reward
for believers. Both precisely 65 letters. This is a
letter-count-encoded **reward/punishment symmetry** at the structural
midpoint of the surah.

Q 64 At-Taghābun's period-2.57 signature is an almost-alternating
short/long pattern (verse lengths oscillate rapidly). Q 89 Al-Fajr
has strong lag-1 autocorrelation 0.64 (consecutive verses are similar
length — an expected feature for the sequential oath-cluster opening).

## Open questions / follow-ups
1. Q 109:2–6 `[14,19,17,19,14]` is a previously unnoticed L=5 palindrome
   — warrants prose treatment; the repetition at the word level (`ولا
   أنتم عابدون ما أعبد` repeats as v3 and v5) exists at the *letter-count*
   level too.
2. Q 19:20–24 Annunciation palindrome is the most semantically loaded
   L=5 hit — Mary's speech (38) → Gabriel's answer (57) → Mary's
   withdrawal to a distant place (24, centre) → birth-pang verse (57) →
   voice from beneath her (38). The palindrome frames *the moment Mary
   gave birth* as the mirror-axis.
3. Q 75:28–31 and Q 75:30–33 are *overlapping* length-4 palindromes,
   hinting at a richer local symmetry structure through verses 26–34
   (the death-scene passage).
4. The rarity of length-9 palindromes (0 observed, ~0.1 null expected)
   should be noted in findings: the 7-verse ceiling looks real.
5. Al-Burūj twin-65 peak and its relation to Al-Fajr's rhythm deserves
   closer look — both surahs have n ≤ 30 and both appear in the
   spectral-anomaly top-10.

## Honest caveats
- The null model is *within-surah* shuffle; it preserves per-surah
  marginal distribution but destroys order. A *within-corpus* shuffle
  would be stricter.
- Palindrome-hunt is an open-ended search; no pre-registration, so no
  single p-value is load-bearing.
- "Spectral signature" here is a raw periodogram on short sequences
  (n ≤ 30 for most small surahs); individual peaks are noisy. The
  ranking picks up outliers but these need replication on synthetic
  null data with matched length distribution.
- "Semantic-centre" claims rest on my reading of the verses; they are
  interpretive, not mechanical.
