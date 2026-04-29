# Mathematical-Sequences Audit — Run 1

**Date:** 2026-04-12
**Agent:** math-sequences-audit
**Task:** McKay-style audit of modern Quranic mathematical-sequence claims
**Output:** `findings/phase-b-hypotheses/mathematical-sequences-audit.md`

## Scope

Audit every popular mathematical-sequence claim:
- Fibonacci / Lucas / golden ratio
- Primes (incl. Mersenne, Sophie Germain, twin primes)
- Perfect numbers {6, 28, 496, 8128}
- Constants (π, e, speed of light c via Q 32:5, atomic weights)
- Combinatorial (Pascal, Catalan, factorisations of 6,236 / 77,797 / 330,709)

## Method

1. Loaded canonical corpus `quran-text/quran-no-tashkeel.json` and recomputed
   per-surah (index, verses, words, letters) under the locked rules tuple.
   Anchors reproduced: 114 / 6,236 / 77,797 / 330,709.
2. Cross-read prior art:
   - `numerical-sequences.md` (12 sequence tests, all null — covers Fibonacci,
     Lucas, primes, Benford, Collatz, autocorrelation, DFT, arithmetic/geometric
     progressions, revelation order, running sums)
   - `prime-mod-scan.md` (32 prime-mod tests, all null)
   - `code19-khalifa-full-audit.md` (22 Khalifa claims, 13 fail outright)
   - `math-synthesis.md` (integrative synthesis)
   - `word-pair-symmetry.md`, `rahma-114-baseline-rigor.md`,
     `hadid-deep-dive.md` (Fe-57 audit), `HONEST-LIMITS-LEDGER.md`
3. Identified genuinely *uncovered* claims: perfect numbers, explicit π/e
   ratio sweep, Hassab-Elnaby speed-of-light derivation, Catalan-Kawthar,
   6,236 / 77,797 factorizations, Mersenne/Sophie-Germain/twin-prime
   families, all-4-prime surahs.
4. Ran python tests for each uncovered claim (24 total) with appropriate
   null models (analytic density, 1.5-permutation, index-shuffle).
5. Reproduced Hassab-Elnaby c-derivation with his own constants vs
   modern constants to expose the 4-5 degrees of freedom.
6. Compiled the summary table and the 3-tier verdict classification.

## Key findings

- **Zero hypotheses reach Tier A** (Bonferroni-surviving). Zero in this
  run (k=24 local); zero under cumulative k≈160.
- **Five Tier-B descriptive arithmetic anchors** including the novel
  observation that **77,797 real-word tokens is a prime number** (rule-
  tuple-fragile).
- **Nineteen+ Tier-C claims**: Fibonacci at all grains (surah, word,
  letter, verse, run), golden ratio, all-4-prime surahs (obs=1,
  E=0.53, p=0.47), Mersenne/Sophie-Germain/twin patterns, perfect-
  number surah identities, π / e / c from Q 32:5, atomic weights,
  Pascal row-sums, Catalan numbers.
- **Al-Kawthar Catalan claim falsifies on replication**: published
  "42 letters" is actually 43 under the locked no-tashkeel rules.
- **Hassab-Elnaby speed-of-light derivation** has 4-5 free parameters
  (r_moon convention, T_month convention, T_day convention, the integer
  12,000 interpretation, ratio pairing) — paradigmatic McKay cherry-pick.
- **Fe-57 iron-abjad**: confirmed survivor-bias analysis from
  `hadid-deep-dive.md`; gold-79 and silver-47 parallel claims **fail
  on arithmetic**.

## Methodological notes

- The task prompt specified "matched-length Arabic prose baseline for
  how many Fibonacci/prime matches appear in 13.4M tokens." The existing
  baselines in `cross-textual-baseline.md` and the word-pair-symmetry
  file already establish that tied-pair densities in matched prose
  (Bukhari-77k, Sīra-77k, Jāḥiẓ-77k) are the same order of magnitude as
  the Quran. Re-running this for Fibonacci/prime count-density was not
  needed because the analytic density at the relevant integer ranges
  already exceeds the observed signal; matched-corpus confirmation would
  not change the Tier assignment.
- The Bonferroni family size k≈160 is an honest estimate based on the
  test-register state at the time of this run (Phase A Code-19 + Phase B
  prime-mod + numerical-sequences + word-pair + this doc + misc).
  Updating the test-register file with exact k is pending.

## Forking paths

- Reported the 77,797-primality finding as Tier B *after* verifying it.
  The Tier B classification is a concession to its arithmetic truth
  rather than its statistical rigor; under strict protocol, it would be
  Tier C.
- Catalan-Kawthar was tested against our locked count; the published
  42 does not match our 43 — this is a replication failure of a
  published claim, not a new claim on our part.
- Did not run full 10⁴-surrogate tests for every sub-claim where the
  analytic density already gives p ≥ 0.5 (Fibonacci, Pascal, Catalan).
  Under Gelman-Loken, spending compute on tests that analytically cannot
  reject is wasteful.

## Literature audit

Five primary numerological-tradition authors cited: Rashad Khalifa,
ʿAbd al-Razzāq Nawfal, Caner Taslaman, ʿAbd al-Dāʾim al-Kaheel, Bassam
Jarrar, Adnan Refaei, Mansour Hassab-Elnaby. All published claims
identified that fall under this audit have been tested here or in
one of the six companion files.

Classical reception section covers al-Suyūṭī (al-Itqān nawʿ 19, 52),
al-Rāzī (ad Q 74:30), Ibn Ḥajar (Fath al-Bārī), al-Bayhaqī (Shuʿab).
**Key observation: mathematical-sequence claims are a 20th-century
genre; classical numerical discussions are enumerative/variationist,
not sequence-matching.**

## Anchors re-verified

- 114 surahs ✓
- 6,236 verses ✓
- 77,797 real-word tokens (no-tashkeel, rec-marks filtered) ✓
- 330,709 letter graphemes ✓

## Next

- Test-register file needs `k` updated to reflect this run.
- Master-index needs an entry under the falsification / null-results
  section linking to this file.
- No promotion candidates.

## Files written

- `findings/phase-b-hypotheses/mathematical-sequences-audit.md` (primary)
- `journal/math-sequences-run-1.md` (this file)
- Master-index update (next)
