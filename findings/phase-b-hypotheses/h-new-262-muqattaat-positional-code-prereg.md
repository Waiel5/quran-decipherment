---
id: H-NEW-262
title: Muqatta'at positional code — per-letter muq-opened vs non-muq-opened surah test
phase: B
date: 2026-04-18
agent: autonomous
status: PRE-REGISTERED
corpus_anchor: 6,236 verses / 329,131 normalized letters / 29 muq-opened surahs / 85 non-muq-opened surahs
rules_tuple:
  orthography: no-tashkeel via analysis.tools.loader.load_quran
  basmala_policy: default canonical JSON state (counted only in surah 1 by construction)
  letter_definition: character-level 28-letter normalization
  position_stat: (i + 0.5) / verse_length
  normalization: |
    hamza-bearing {أ, إ, آ, ٱ} -> ا;
    ة -> ه;
    ى -> ي;
    ؤ -> و;
    ئ -> ي;
    spaces, standalone ء, and recitation marks {ۖ ۗ ۘ ۙ ۚ ۛ ۜ ۞ ۩} excluded
bonferroni_k: 14
bonferroni_family: h-new-262-letterwise-muq-positional-code
alpha_bon: 0.0035714285714285713
direction_primary: for each muqatta'at letter, occurrences lie later within verses in muq-opened surahs than in non-muq-opened surahs
seed: 20260418
---

# [[h-new-262-muqattaat-positional-code|H-NEW-262]] — Muqatta'at positional code (pre-registration)

## Question

For each of the 14 muqaṭṭaʿat letters
`{ا, ل, م, ص, ر, ك, ه, ي, ع, ط, س, ح, ق, ن}`,
does the same letter occupy later normalized positions within verses
when it appears inside the 29 muq-opened surahs than when it appears
inside the 85 non-muq-opened surahs?

This is a same-letter contrast. It therefore controls the obvious
frequency confound automatically: `ن` is compared to `ن`, `ق` to `ق`,
and so on.

## Direction lock

The directional hypothesis is **later-position / more verse-final** in
muq-opened surahs.

Rationale locked before the production run:

1. [[h-new-113-letter-position|H-NEW-113]] found corpus-wide verse-final enrichment for the
   muqaṭṭaʿat set relative to the complement set.
2. The older muq positional-gradient work rejected front-loading inside
   carrier surahs, which weakens an "opening-bias" story and makes a
   fāṣila / terminal-position reading the more plausible directional
   alternative.
3. The task explicitly asks for pre-registered directions, so the main
   inferential family must use a signed test rather than a purely
   two-sided omnibus statistic.

## Primary family

For each letter `L` in the 14-letter muqaṭṭaʿat set:

1. Load the canonical Quran with `load_quran("no-tashkeel")`.
2. Normalize each verse using the locked 28-letter map above.
3. For every occurrence of `L` at index `i` in a normalized verse of
   length `N`, assign normalized position
   `p = (i + 0.5) / N`.
4. Split all such positions into:
   - `P_muq(L)`: positions from the 29 muq-opened surahs
   - `P_non(L)`: positions from the 85 non-muq-opened surahs
5. Run a one-sided Mann-Whitney U test:
   `H1(L): P_muq(L) > P_non(L)` in stochastic-order terms.

### Primary decision rule

- Letter-level support for `L`: `p_one_sided_greater(L) < alpha_bon`
  with `alpha_bon = 0.05 / 14 = 0.0035714286`.
- Broad positional-code support for the 14-letter family requires:
  - positive control PASS, and
  - at least 3 letters surviving Bonferroni-14 in the pre-registered
    direction.

If only 1-2 letters survive, report the result as
**letter-specific / mixed**, not as a broad 14-letter positional code.

## Secondary descriptive outputs

These are reported for interpretation but do **not** enter the
Bonferroni family:

1. Two-sided KS test per letter.
2. Mean and median position in each partition.
3. Bin-10 density (`p >= 0.9`) and the relative risk
   `RR_bin10 = density_muq / density_non`.
4. Exploratory reverse-direction p-value from one-sided
   Mann-Whitney `alternative="less"`.

## Positive control

Using the exact same normalization and position-binning instrument,
pooled across the whole corpus:

- Rhyme letters `ن`, `ر`, `ي` should each have bin-10 density `> 0.13`.
- Prefix-heavy letters `ا`, `ل` should each have bin-10 density `< 0.10`.

If any of these five inequalities fail, declare `INSTRUMENT-FAIL` and
do not promote any inferential conclusion.

## Locked exclusions / non-exclusions

1. **No special stripping of muqatta'at opener blocks.** The analysis
   uses the canonical text exactly as loaded, then normalizes
   characters only. This keeps the task aligned with the repo's
   canonical text pipeline and avoids introducing a second analytic
   fork over which opening letters to strip in Surah 42 and similar
   cases.
2. **No word-level filtering.** The unit is letter occurrence, not
   token or root.
3. **No frequency matching across different letters.** The design is
   same-letter by construction, so extra matching is unnecessary.

## Garden-of-forking-paths log

1. **Two candidate primaries were considered**: per-letter two-sided KS
   and per-letter one-sided Mann-Whitney. The task's requirement to
   pre-register directions makes the one-sided same-letter shift test
   the correct primary; KS is retained as descriptive.
2. **Later-position direction is locked.** An earlier-position
   hypothesis was considered and rejected because it conflicts with the
   prior verse-final enrichment signal and the non-front-loaded carrier
   profile already on record.
3. **Bonferroni family is exactly 14.** No extra family slots are spent
   on KS, reverse-direction probes, or positive-control inequalities.
4. **No resampling threshold tuning.** There is no permutation or
   bootstrap threshold to select in this run; the test is deterministic
   given the canonical corpus and the locked normalization.

## Outputs

1. Script: `scripts/h_new_262_muqattaat_positional_code.py`
2. JSON: `findings/phase-b-hypotheses/csv/h-new-262.json`
3. Findings: `findings/phase-b-hypotheses/h-new-262-muqattaat-positional-code.md`
4. Journal: `journal/h-new-262-run-1.md`

Null and pass will be reported with equal prominence.
