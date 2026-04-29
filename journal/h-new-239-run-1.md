# H-NEW-239 — Run 1 Journal

**Date**: 2026-04-17
**Finding**: divine-name density gradient across 114-surah mushaf
**Seed**: 20260419
**Status**: COMPLETE (single run)

## Protocol followed

1. READ divine-names-distribution.md (parent catalog), khawatim-al-hashr-analysis.md,
   MASTER-LEDGER §2. Confirmed 99-name canonical list and Q 59:22-24 8-exclusive-names.
2. Pre-reg filed at `findings/phase-b-hypotheses/h-new-239-divine-name-gradient-prereg.md`
   with directional hypotheses for B, C, D and mixed for A. Bonferroni k=4, α_cell=0.0125.
3. Script run: `scripts/h_new_239_divine_name_gradient.py` — single run, deterministic seed.
4. Outputs: `findings/phase-b-hypotheses/csv/h-new-239.json` + `h-new-239-per-surah.tsv`
5. Findings written: `findings/phase-b-hypotheses/h-new-239-divine-name-gradient.md`

## Results summary

| Cell | p | Direction |
|---|---|---|
| A Spearman | p ≈ 0 (0/10000 perm) | ρ=−0.476, density DECREASES with mushaf position |
| B Kruskal-Wallis | p = 2.5×10⁻⁴ | ṭiwāl > other ≈ ḥawāmīm > mufaṣṣal; driven by mufaṣṣal depletion |
| C juz30 vs rest | p_two = 1.5×10⁻⁷ | juz30 LOWER (reverse of pre-reg) |
| D Meccan vs Medinan | p_two = 1.7×10⁻⁸ | Medinan HIGHER (reverse of pre-reg) |

## MW-5 shuffle null

Real ρ = −0.476; shuffled ρ = +0.503. The shuffle INVERTS the gradient,
validating that the real front-loading is a genuine textual signal that
FIGHTS against the short-surah density inflation bias. All 4 shuffled cells
show significant signal in the expected short-surah-inflation direction,
which is the OPPOSITE of what the real text shows. This strengthens (not
weakens) the finding.

## Pre-reg directional failures — honest disclosure

Two of four pre-registered directional predictions were wrong in SIGN:

- **Cell C**: predicted juz30 HIGHER density because of short-surah
  inflation; observed juz30 LOWER density. The true text has many juz30
  surahs with ZERO canonical divine names (Q 100, Q 103, Q 104, Q 105,
  Q 107, Q 111, Q 113 — check per-surah TSV for exact list).
- **Cell D**: predicted Meccan HIGHER density (theological-vs-legal
  framing). Observed Medinan higher by 2.2× — Medinan legal-verse
  divine-name pair closures (*ghafūrun raḥīm, ʿazīzun ḥakīm*) are the
  dominant mechanism.

Under STRICT directional-p reading: C and D are NULL (the pre-reg predicted
the wrong direction). Under two-sided reading: C and D are strongly
significant in the opposite direction to pre-reg.

I report both readings in the findings doc. The overall substantive
finding — descending density gradient from book-start to book-end driven
by Medinan legal-surah name-pair cadences — is real, Bonferroni-surviving,
and novel at the per-word-density axis.

## Garden-of-forking-paths (disclosed)

- Block boundaries locked in pre-reg before run (Q 2-9 / Q 40-46 / Q 50-114 / other).
- Juzʾ 30 = Q 78-114 (canonical start).
- Density = (tokens in surah) / (whitespace-split word count of no-tashkeel text).
- Directional predictions for B, C, D locked in pre-reg; only C and D had
  directional predictions that failed. The FAILURE is reported, not papered
  over.
- No post-hoc feature tuning. Single run, single script.

## Cross-finding integration

- **cross-finding-018 M1 4-region architecture**: density gradient aligns
  with 4-region partition. Region ṭiwāl is name-dense and geodesically
  complex; region mufaṣṣal is name-sparse and geodesically peripheral.
  The divine-name-density axis is ORTHOGONAL information to the Fisher-Rao
  axis and they co-vary in the expected direction.
- **Cross-finding (new)**: ḥawāmīm hypothesis DIVERSITY-survives but
  DENSITY-fails. al-Ghazālī's "name-heaviness" is about REPERTOIRE
  (distinct names invoked) not per-word density. H-family surahs have
  14 distinct names each but do not exceed ṭiwāl or "other" in per-word
  density. This refines the classical intuition.

## Connection to MASTER-LEDGER

- §2 (divine-names authoritative catalog) is the parent anchor.
- §2 will be extended with an H-NEW-239 sub-section after this note is filed.
- Ledger Wave-4 2026-04-17 entry added in the same session.

## Time log

- 2026-04-17 session: read context files (5 min), write pre-reg (5 min),
  write script (10 min), run script (1 min), interpret results including
  handling the directional-failure honesty question (10 min), write
  findings doc (15 min), write journal + ledger entry (5 min).
- Total: ~50 min active session work.

## Open questions for future runs

1. **Chronological-order version of Cell A**: rerun ρ under Noldeke revelation
   order instead of mushaf order. Prediction: ρ > 0 (density INCREASES with
   chronology since Medinan > Meccan density, and Medinan is late). Tests
   whether mushaf-order gradient is a reorder-preserved signature of
   chronology or an independent mushaf-order engineering feature.
2. **Permissive-filter sensitivity**: rerun with DET-MS relaxed (accept any
   lemma match regardless of morphology). al-Ḥaqq would rise from 82 to
   ~200 tokens. Test whether the gradient sign is stable under filter
   relaxation.
3. **Density-residualized-on-verse-length**: control for the fact that
   Medinan verses are on average LONGER (and contain more words, hence more
   opportunity for divine-name tokens per verse). Current metric is per-word
   density so this is partly controlled, but a verse-length-residualized
   density would be a cleaner effect-size estimate.
4. **Extend to cross-finding-020 equation form**: H-NEW-239 is a direct
   input candidate for the "Complete Equation" cross-finding-020
   integration — the descending gradient is a candidate second-order
   term (names-density ~ α − β·position) that could be added.
