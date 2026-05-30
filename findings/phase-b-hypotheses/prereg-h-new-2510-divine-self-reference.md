---
finding_id: H-NEW-2510
title: Divine-self-reference density corpus map + the tawḥīd-declaration verse class
date: 2026-05-30
seed: 20260509
n_perm: 10000
phase: B+
specialist: divine-self-reference-generator
status: PRE-REGISTERED
direction_locked: |
  Divine-self-reference density is NON-uniform across the 6236 verses, and the
  corpus-top-density verses concentrate in recognized tawḥīd-declaration /
  self-disclosure / theophany contexts (NOT random). The top of the ranking is
  occupied by the recognized tawḥīd-declaration class (Q20:14, Q2:255 āyat
  al-kursī, Q112 al-Ikhlāṣ, the *innī anā* burning-bush verses) rather than by a
  random scatter of verses.
bonferroni_k: 1
bonferroni_family: "single corpus-wide concentration test (H1)"
alpha_bon: 0.05
---

# H-NEW-2510 — Divine-self-reference density corpus map

## 0. Provenance / parent finding

This GENERALIZES **Q020-F-05** (MASTER-FINDINGS-LEDGER §10.120): within Ṭā-Hā,
Q 20:14 (*innanī anā Allāhu lā ilāha illā anā fa-ʿbudnī wa-aqim al-ṣalāta
li-dhikrī*) is the **rank-1 divine-self-reference verse** (density 0.5455 under the
original noisy regex proxy; p_perm = 0.0015; seed 20260507; file
`surahs/Q020-ta-ha/csv/Q020-F-05.json`). Q020-F-05 was a *within-surah* test on a
regex proxy. H-NEW-2510 (a) re-grounds the metric in the **QAC v0.4 morphology**
(person/number features, not noisy regex), (b) scores **all 6236 verses**, and
(c) tests whether the corpus-top divine-self-disclosure verses form the
recognized **tawḥīd-declaration class**.

## 1. Background — classical anchor

The Quran's first-person divine voice (*tawḥīd* self-disclosure) is a recognized
theological and rhetorical category. The *kalimat al-tawḥīd* / *lā ilāha illā…*
formula and the burning-bush *innī anā* (Q 20:14; Q 27:9; Q 28:30) are the
paradigmatic divine self-affirmations. Classical *iʿjāz al-maʿnā* (al-Khaṭṭābī)
locates the theological weight of the Quran in such self-disclosure verses — Q 112
al-Ikhlāṣ is *thuluth al-Qurʾān* "a third of the Quran" (al-Bukhārī, ḥadīth
#5013–5015; Muslim #811) precisely as a tawḥīd-declaration; āyat al-kursī (Q 2:255)
is "the greatest verse of the Quran" (Muslim #810, Ubayy b. Kaʿb tradition). This
test asks whether a purely morphological density metric — built with no knowledge
of which verses are "famous" — independently surfaces this class.

## 2. Operationalization (LOCKED)

### 2.1 Canonical sources & rules-tuple

- Corpus structure + word counts + person features: **QAC v0.4**
  `data/morphology/quranic-corpus-morphology-0.4.txt` (Buckwalter; segments grouped
  to 77,429 words / 6,236 verses).
- Cross-check text: `quran-text/quran-no-tashkeel.json`.
- Rules-tuple: `(no-tashkeel, QAC-morphology-segment, words-as-denominator,
  basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.
- Denominator = QAC **word** count of the verse (orthographic words, not segments;
  prefixes/suffixes do not inflate the denominator). Basmala counted as verses only
  where QAC counts it (Q 1:1); it is NOT a separate verse in Q 2–114 in QAC, matching
  the rules-tuple.

### 2.2 Divine-self-reference token set (QAC-grounded)

A QAC **segment** is a divine-self-reference token if it matches any of:

1. **Divine name** *Allāh*: `POS:PN` with `LEM:{ll~ah` (proper noun "Allāh").
2. **ilāh / tawḥīd-noun**: any segment with `LEM:<ila`h` (the noun *ilāh* "god",
   ROOT Alh) — captures *lā **ilāha** illā…*.
3. **Standalone 1st-person pronoun**: `POS:PRON` with `1S` (*anā*) or `1P` (*naḥnu*).
4. **Clitic 1st-person pronoun**: any segment carrying `PRON:1S` or `PRON:1P`
   (the suffixes *-nī / -ī / -nā* "Me / My / Us / Our").
5. **Restrictive particle of the tawḥīd formula** *illā*: `LEM:<il~aA` when it
   stands immediately after an `<ila`h` segment (the *illā* of *lā ilāha illā*),
   counted once per tawḥīd-formula occurrence.

Numerator = count of matching segments in the verse.
**density(verse) = numerator / QAC-word-count(verse)**.

This is the faithful QAC re-grounding of the Q020-F-05 numerator
(الله / إله / أنا / هو / ـني), with two principled upgrades: (i) clitic 1S/1P are
caught by the morphology tag rather than a noisy `endswith ني` proxy; (ii) the
*huwa* (3MS) token of *lā ilāha illā **huwa*** is captured ONLY through the
tawḥīd-formula gate (see Metric-A vs Metric-B below), not as a free 3MS pronoun
(which would over-count every human "he").

### 2.3 The divine-vs-human disambiguation rule (FLAGGED, LOCKED)

First-person tokens in the Quran are uttered by Allah AND by humans (prophets,
disbelievers, hypocrites, jinn, angels). A bare 1S/1P token is NOT intrinsically
divine. We do NOT hand-label each verse's speaker (subjective). Instead we
pre-register **two parallel metrics** and lock **Metric-A as PRIMARY**:

- **Metric-A — LEXICAL / speaker-agnostic (PRIMARY).** Counts only tokens 1–5
  above. Of these, tokens 1, 2, 5 (*Allāh*, *ilāh*, tawḥīd-*illā*) are
  **intrinsically divine-referential** regardless of speaker. Tokens 3–4 (bare
  1S/1P) are speaker-ambiguous and contribute uniform noise across all 6,236
  verses — exactly as in Q020-F-05. The metric is honest about this: the *signal*
  that lifts a verse to the top is dominated by stacking the unambiguous
  divine-name + tawḥīd-formula tokens together with first-person divine pronouns
  in a SHORT verse (high density). A long human-narrated 1S passage cannot reach
  the top because it lacks the *Allāh*/tawḥīd anchors.

- **Metric-B — DIVINE-GATED (ROBUSTNESS).** Bare 1S/1P tokens (3–4) are counted
  ONLY in verses that pass an automatic **divine-speech gate**: the verse contains
  the divine name *Allāh* (token 1) OR the tawḥīd-formula (token 2 + token 5). In
  gated verses ALL self-reference tokens count; in non-gated verses only the
  unambiguous tokens 1, 2, 5 count. This removes human-narrated 1S mass at the cost
  of also removing un-anchored divine 1st-person ("*We sent it down*" without the
  name). We report Metric-B's top-20 and the Spearman correlation A↔B as a
  robustness check. **Direction and the primary verdict are read off Metric-A.**

Both metrics are computed identically on the observed corpus and on every
permutation, so the disambiguation rule cannot be tuned post-hoc.

## 3. Hypotheses (DIRECTION-LOCKED)

- **H1 (PRIMARY — concentration / non-uniformity).** The distribution of Metric-A
  density across 6,236 verses is significantly MORE concentrated than a
  verse-internal word-shuffle null predicts: the observed **max density** and the
  observed **top-20 mean density** both exceed their null distributions
  (one-sided, upper tail). Direction: observed > null.

- **H2 (PRIMARY — class membership).** The corpus top-20 Metric-A verses are
  ENRICHED for the pre-named tawḥīd-declaration anchor set
  **A = {Q20:14, Q27:9, Q28:30, Q2:255, Q112:1, Q112:2}** relative to a random draw
  of 20 verses (≥3 of the 6 anchors, or anchors' mean rank in the top decile).
  Direction: enrichment > chance.

- **Reported (descriptive, not a pass/fail gate):** Q20:14's **corpus rank** under
  Metric-A (it was rank-1 within Ṭā-Hā; where does it land among all 6,236?).

## 4. Null model (LOCKED)

**Per-verse word-shuffle null**, matching Q020-F-05's family: pool all QAC words of
the corpus, shuffle, re-assign to verses preserving each verse's word-count, recount
densities under the IDENTICAL token rules. This preserves the corpus word-bag and
each verse's length, and destroys the *placement* of divine-self-reference tokens.
Seed = 20260509; n_perm = 10000. Test statistics: (a) max density, (b) top-20 mean
density. p_perm = (#{null ≥ observed} + 1) / (n_perm + 1).

A second, stricter **within-verse positional null is not needed** — the word-shuffle
already breaks the co-location of *Allāh* + tawḥīd + 1st-person that produces the
tawḥīd-declaration signal.

## 5. Pre-committed thresholds

- **H1 PASS** iff both p_perm(max) ≤ 0.05 AND p_perm(top-20 mean) ≤ 0.05.
- **H2 PASS** iff ≥ 3 of the 6 anchor verses appear in the corpus top-20 OR the 6
  anchors' mean corpus-rank ≤ 624 (top decile of 6236).
- **VERDICT = CONFIRMED** iff H1 PASS AND H2 PASS.
- **VERDICT = DIRECTIONAL** iff exactly one of H1/H2 passes.
- **VERDICT = NULL** iff neither passes, OR if the top of the ranking is dominated
  by non-self-disclosure verses (direction reversed). A reversed/NULL result is
  published with FULL prominence per Protocol §1.3.

## 6. MW protections

- MW-1 (instrument-prior): token set + denominator + null fixed here, pre-run.
- MW-2 (corpus-prior): 10,000-perm permutation null.
- MW-3 (alternative-models): Metric-A vs Metric-B (two operationalizations).
- MW-6 (instrument-control): the word-shuffle null IS the matched control (same
  word-bag, same lengths).
- MW-7 (post-hoc cap): the anchor set A is named HERE, before computing.

## 7. Honest limits (pre-stated)

- Metric-A includes speaker-ambiguous bare 1S/1P (uniform noise). The top of the
  ranking is driven by the *Allāh*/tawḥīd anchors co-located with 1st-person in
  short verses; this is a property of the metric, stated openly.
- The QAC 3MS *huwa* of *lā ilāha illā huwa* is counted only via the tawḥīd gate,
  so āyat al-kursī's *huwa* anchors are credited but a free narrative "he" is not.
- A high density is *consistent with* a verse being a tawḥīd-declaration; it is not
  a theological claim about miracle-status (Protocol §10, out of scope).
- Verse-count / word-count conventions follow QAC; minor divergences from other
  recensions' verse-splitting do not affect the ranking materially (single text).
