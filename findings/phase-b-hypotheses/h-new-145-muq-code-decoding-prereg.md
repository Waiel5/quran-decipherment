---
finding_id: h-new-145
title: "Muqaṭṭāʿat letter-sets as CODE — attempted decoding of surah metadata"
specialist: specialist-B (quran-equation-solvers)
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 4
bonferroni_family: h-new-145-muq-code
alpha_bon: 0.0125
alpha_raw: 0.05
rules_tuple: "(14 distinct muq letters across 29 surahs; 14 distinct letter-sets; Hafs-Kūfan; no-tashkeel)"
pre_reg_standard: PRE-REG-STANDARD-04
parent_findings: [h-new-88 (metadata→letter-set RF 41.4%), cross-finding-006 (muqaṭṭāʿat multi-axis)]
related: [h-new-44 (combinatorial closure), h-new-45 (surah-index number theory), h-new-46 (length skew), h-new-51 (cardinality-position decline)]
---

# [[h-new-145-muq-code-decoding|H-NEW-145]] — Muqaṭṭāʿat letter-sets as CODE: decoding attempt

## Motivation

The 14 muqaṭṭāʿat letter-sets opening 29 surahs (e.g., الم at Q 2; ق at Q 50)
are a 1,400-year interpretive puzzle. [[h-new-88-letter-set-predictor|H-NEW-88]] showed that SURAH METADATA
can predict LETTER-SET at ~2× majority-class baseline (41.4% RF top-1,
p=0.002) — i.e., surahs with similar content+position tend to get similar
letter-sets. This establishes that letter-set assignment is NOT random.

This finding now asks the REVERSE direction: can we DECODE metadata FROM
the letter-set? If muq is a code in the literal sense (a compressed
encoding of information about the surah), then specific letters or
letter-set properties should be MECHANICALLY MAPPABLE to specific
surah-metadata fields.

Five Cells, four with inferential slots (Bonferroni k=4, α_bon=0.0125).

## Canonical data

29 muq surahs and their 14 distinct letter-sets:

| Letter-set | Surahs | Arabic |
|---|---|---|
| ALM (6) | Q 2, 3, 29, 30, 31, 32 | الم |
| HM (6) | Q 40, 41, 43, 44, 45, 46 | حم |
| ALR (5) | Q 10, 11, 12, 14, 15 | الر |
| TSM (2) | Q 26, 28 | طسم |
| ALMS (1) | Q 7 | المص |
| ALMR (1) | Q 13 | المر |
| KHYAS (1) | Q 19 | كهيعص |
| TAH (1) | Q 20 | طه |
| TAS (1) | Q 27 | طس |
| YS (1) | Q 36 | يس |
| SAD (1) | Q 38 | ص |
| HMASQ (1) | Q 42 | حم·عسق |
| Q (1) | Q 50 | ق |
| N (1) | Q 68 | ن |

14 distinct letters total (nuṣṣ ḥurūf al-muʿjam = "half the alphabet"):
{A (alif), L (lām), M (mīm), R (rā), ṢĀD, SĪN, K (kāf), HĀ, Y (yā), ʿAYN,
ṬĀ, ḤĀ, Q (qāf), N (nūn)}.

## Hypotheses

### Cell A — cardinality-mod-K vs surah-metadata (TEST 1 of 4)

Letter-set cardinality ∈ {1, 2, 3, 4, 5}. For each of four pre-committed
metadata axes, test Pearson correlation between cardinality and
metadata:

1. verse count
2. Nöldeke chronology rank
3. position in mushaf (i.e., surah number)
4. cardinality-mod-3 vs verse-count-mod-3

The first three are continuous correlation tests (existing literature —
[[h-new-51-cardinality-position-decline|H-NEW-51]] already found cardinality ↔ position Spearman ρ=−0.66, so that
is NOT counted as fresh; it's baked in). The NEW test is #4: is there a
`hash(cardinality) == hash(verse-count)` modular relationship that would
look CODE-LIKE?

**Inferential slot**: cardinality-mod-3 and verse-count-mod-3 produce
equal values more often than random. Null = 29 surahs, uniform
distribution over {0, 1, 2}. Expected match rate under null = 1/3. Test
= 2-sided exact under hypergeometric-like null. PASS: match rate > 0.55
at p < 0.0125.

Other mod choices rejected pre-result: mod-2 (too coarse — 50% match by
chance), mod-5 (too fine — most single-letter sets crash to same), mod-7
(arbitrary).

### Cell B — per-letter binary features × metadata (TEST 2 of 4)

For each of 14 letters, define a binary indicator: does it appear in the
surah's letter-set? (e.g., Q 2 has A=1, L=1, M=1, all other=0.) This gives
a 29×14 binary matrix.

For EACH letter × 3 metadata axes (verse count, chronology, surah-name-
class), compute Spearman ρ between letter-presence and metadata. This is
14×3 = 42 tests. To avoid 42-test Bonferroni explosion, I pre-commit a
RESTRICTED TEST SET: 5 specific hypotheses motivated by classical tafsir
and preliminary pattern inspection:

1. **letter M presence** ↔ longer surah (M is the most-included letter;
   [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] found muq surahs are longer). Spearman ρ > 0.
2. **letter H presence (either HĀ or ḤĀ — but [[h-new-88-letter-set-predictor|H-NEW-88]] data uses HĀ in
   TAH+KHYAS, ḤĀ in HM+HMASQ; I treat them separately)**:
   - **ḤĀ presence** ↔ Medinan-bias (HM surahs Q 40-46 form a late-Meccan
     cluster per tradition)? Spearman ρ vs chronology.
3. **letter SAD presence** ↔ "ṣabr/ṣalāḥ" theme — operationalized as
   "theme-keyword frequency" is not available directly; instead, check
   whether SAD-bearing surahs {7, 19, 38} are enriched for patience-
   theme verses. Hypergeometric test.
4. **letter Q presence** ↔ eschatology theme (classical: Q=qiyāma or
   qurʾān per Ibn ʿAbbās — SEE CELL D). Q appears in {42, 50}. Test:
   hypergeometric enrichment of eschatology-class within Q-surahs.
5. **letter N presence** ↔ narrative theme (N = nūn = whale/inkwell; Q 68
   is The Pen and narrative of Yūnus' whale). Single-surah singleton
   test — descriptive only.

Since 1, 2, 4 are Spearman/hypergeometric correlations with null distributions,
they count as inferential. 3 is a hypergeometric test. 5 is descriptive
(n=1 can't be tested).

**Inferential slot** for Cell B = {test 1 (M ↔ length), test 2 (ḤĀ ↔
Medinan), test 3 (SAD ↔ patience-theme), test 4 (Q ↔ eschatology)} but
Bonferroni-internally these 4 sub-tests have α_family = 0.0125 total, so
α_within = 0.003125 (very strict). PASS at Cell B level = ≥ 2/4 sub-tests
pass at α_within.

### Cell C — RF reverse-decoding (TEST 3 of 4)

Train a random-forest classifier on the 29×14 binary letter-presence
matrix as FEATURES; target = a SPECIFIC metadata field (one model per
target). LOOCV.

Three targets (all pre-committed, pre-result):
1. **Length-bin** (surah's verse-count into 3 quantiles: short/mid/long).
   Chance baseline = 1/3.
2. **Chronology-bin** (Meccan-phase per Nöldeke: early-Meccan /
   middle-Meccan / late-Meccan / Medinan — 4 bins). Chance = 1/4 for
   balanced bins (actual imbalanced; compute per-bin majority baseline).
3. **Name-class** (7 classes per [[h-new-49-surah-name-class|H-NEW-49]]: PROPHET_PERSON, BOOK_REF,
   GEOGRAPHIC, DIVINE_NAME, NATURE/COSMOS, NUMERIC, OTHER). Chance = 1/7.

**Inferential slot** at Cell C = at least one of {1, 2, 3} has LOOCV top-1
accuracy significantly above majority-class baseline via permutation null
(1,000 shuffles of letter-presence matrix rows). PASS: any of the 3 has
p_perm < 0.0125.

### Cell D — classical singleton-interpretation thematic enrichment (TEST 4 of 4)

Three specific classical tafsir claims:

1. **ص (Q 38) ↔ ṣabr (patience)**: test whether Q 38 has ABOVE-MEDIAN
   occurrences of root ṣbr (ص-ب-ر) per verse, using QAC-STEM root tokens.
2. **ق (Q 50) ↔ qiyāma (resurrection) OR qurʾān**: test whether Q 50 has
   above-median verse-density of roots {qwm (ق-و-م, resurrection-cognate)
   AND/OR qrʾ (ق-ر-ء, qurʾān)}.
3. **ن (Q 68) ↔ nūn (whale OR inkwell)**: test whether Q 68 contains the
   literal token نون or references the whale-narrative (Yūnus) per root
   ywns / nws.

All three tests are binary ABOVE-MEDIAN checks across the 29 muq surahs.
Under null (random which muq surah has above-median density of the cognate
root), P(each specific surah above-median) = (29-15)/29 ≈ 0.48. For 3/3
to all pass under null: 0.48^3 ≈ 0.11 (loose), but the cognate-rooted
assertion is stronger than random. Tighter null: for each cell, is the
observed surah in the TOP-5 of the 29 muq surahs for that root density?
P(top-5 under null) = 5/29 ≈ 0.17; P(all 3 in top-5) = 0.17^3 ≈ 0.005.

**Inferential slot** at Cell D = ≥ 2 of 3 cognate roots place the labeled
surah in TOP-5 of 29 muq surahs for that root's density. Expected under
null = 3 × 0.17 = 0.51 of 3 cognates on average; observing 2+ has exact
binomial p under n=3, p=0.17 of 0.077 — not BY ITSELF Bonferroni-passable.

Tighten: if 3/3 (all three classical singleton interpretations confirm),
binomial-exact p under n=3, p=0.17 = 0.005, below α_bon=0.0125. PASS
condition = 3/3 (not 2/3).

## MW-5 positive control — shuffled letter-set null

Before running inferential tests, shuffle the 29 surah→letter-set
assignments uniformly at random (fix the multiset of letter-sets, shuffle
which surah gets which). Re-run Cells A (mod-3 match), B (4 sub-tests),
and C (RF on each target), and D's top-5 enrichment. Under this null,
ALL cells should fail (p > 0.05 for each).

PASS: shuffled-null Cells A/B/C/D all fail their PASS thresholds.

FAIL (instrument-broken): if shuffled-null somehow passes any cell, the
test design is flawed.

## Bonferroni accounting

- Family = [[h-new-145-muq-code-decoding|h-new-145]]-muq-code
- k = 4 (Cell A mod-3 / Cell B-composite / Cell C-composite / Cell D-composite)
- α_bon = 0.05 / 4 = 0.0125
- Within Cell B: 4 sub-tests each at α=0.0125/4 = 0.003125 (family-level
  composite)
- Within Cell C: 3 targets; PASS if any passes at α_bon=0.0125
- Within Cell D: 3 cognate roots; PASS if 3/3 in top-5 (exact binomial)

## Garden of forking paths

- **Mod-3 over mod-K**: chosen as the minimum-mod where random match
  rate (1/3 = 33%) is distinguishably below 50%, giving test power.
  Mod-2 rejected (too coarse), mod-5/7 rejected (arbitrary + single-letter
  sets collapse to same residue).
- **Spearman ρ > 0 vs > 0.3**: used > 0 (sign test) because n=29 is small
  and the sign is more robust than magnitude. Magnitude threshold ρ > 0.3
  rejected pre-result (would require large-sample power we don't have).
- **14-letter choice**: the 14 classical muq letters, period. Not
  alphabet-28, not graphically-dotless-vs-dotted subset. Anchored to
  the [[h-new-60-muqattaat-dotless-preference|H-NEW-60]] confirmed 11/14 dotless-preference finding and classical
  "half the alphabet" claim.
- **Target choice for Cell C**: 3 pre-committed metadata axes. Alternatives
  rejected pre-result: pharyngeal/non-pharyngeal binary (done in [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]]),
  letter-frequency rank (done in [[h-new-47-muqattaat-frequency-cutoff|H-NEW-47]]), abjad-value sum (superseded
  by [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] number-theory study).
- **Cell D top-5 threshold**: chosen as ~17% (5/29) — matches "strong but
  not extreme" enrichment. Alternatives rejected: top-3 (too strict for
  n=29), top-10 (too loose — 34% false-positive rate).
- **Binomial-exact p in Cell D**: exact rather than normal approx because
  n=3 is tiny.

## Pre-committed acceptance matrix

| Cells passed | Final verdict |
|---|---|
| ≥ 3 of 4 | STRONG-DECODING — muq letter-sets carry decodable metadata |
| 2 of 4 | PARTIAL-DECODING — some metadata encoded, not all |
| 1 of 4 | WEAK-SIGNAL — isolated correlation, likely noise |
| 0 of 4 | NULL — letter-sets are NOT a decodable metadata code (consistent with "mysterious opening" traditional reading) |
| MW-5 shuffled-null pass | INSTRUMENT-BROKEN — results held in abeyance |

## Data sources

- Quran: `quran-text/quran-no-tashkeel.json`
- Morphology: `data/morphology/quranic-corpus-morphology-0.4.txt`
- Chronology: `data/revelation-order.csv` (Nöldeke column)
- Classical cross-refs: `findings/classical-cross-references.md`

## Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_142_muq_code_decoding.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-145.json`
- Findings: `findings/phase-b-hypotheses/h-new-145-muq-code-decoding.md`
- Journal: `journal/h-new-145-run-1.md`

Null and pass published with equal prominence. Runtime target < 5 min.

Note on ID: using [[h-new-145-muq-code-decoding|H-NEW-145]] rather than T-M.3-internal ID to place this
in the H-NEW catalog namespace per project convention.
