---
finding_id: H-NEW-1
title: Rhyme-break verses carry a small but significant residual Markov-surprise after controlling for class alphabet
date: 2026-04-12
rules_tuple:
  orthography: no-tashkeel (primary); min-tashkeel (robustness)
  word_definition: orthographic-token (real_words filter)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
null_model:
  primary: label-permutation on verse-class (break vs conform) × Markov-surprise residual
  stringent: surah-marginal letter distribution (Null B)
acceptance_criterion: Bonferroni-corrected p < 0.005, z >= 3.0 on residual statistic, consistent direction in min-tashkeel robustness check
verdict: PARTIAL
---

## Hypothesis

Let the pre-committed rhyme-conforming alphabet be R = {ن, ا, م, ر, د}. A "rhyme-break" verse is one whose terminal consonant (last letter of last real-word token) is not in R. Under a within-surah first-order Markov model trained on non-terminal consonant transitions, the hypothesis is that **rhyme-break verses carry distinctively high Markov-surprise** — a phonetically-engineered "speed-bump" rather than a random deviation.

The original strong form predicted **bimodality** in the break-class surprise distribution.

## Method

1. Load `quran-no-tashkeel.json`. For each verse, extract the sequence of letter graphemes from its real_words tokens.
2. Per surah, build a first-order Markov chain over letters from sequences **excluding** each verse's terminal letter (so the terminal is not part of the training data).
3. For each verse, compute observed Markov-surprise of the terminal: S = −log P(c_last | c_{last−1}) with add-0.5 smoothing.
4. Classify verses as break (terminal ∉ R) or conform (terminal ∈ R).
5. **Confound control** (added after seeing raw results): compute a *class-uniform baseline* — the average surprise across all letters in the verse's class alphabet, given the same c_{last−1}. Compute residual = observed − class-uniform baseline. This controls for the trivial fact that break-class letters are individually rarer than conform-class letters.
6. Permutation null: shuffle class labels 10,000 times and recompute the mean-residual difference.
7. Robustness: rerun on min-tashkeel orthography.

## Observed vs null

**Raw surprise (unconfounded, for context, NOT the finding):**
- Break N = 850 verses (13.6% of 6,236), mean S = 3.76 nats
- Conform N = 5,386 verses, mean S = 2.51 nats
- Raw diff = 1.25 nats, z = 40.1 under label permutation. **This z is largely a letter-frequency artifact** (break-class letters are rarer by construction).

**Residual-corrected (the actual finding):**
- Break residual: −0.435 nats (observed is ~0.44 nats MORE predictable than a uniform draw from non-rhyme letters — there is within-class preference)
- Conform residual: −0.566 nats (observed is ~0.57 nats more predictable than uniform over R — also within-class preference)
- **Difference of residuals: 0.131 nats** (break verses are *less* within-class-predictable than conform verses)
- Label-permutation null: mean diff ≈ 0, SD = 0.028, **z = 4.73**, empirical p < 10⁻⁴ (0/10,000 permutations at or above observed).
- Robustness: same sign, magnitude 0.108 nats in min-tashkeel.

**Null B (surah-marginal letter distribution):**
- Mean expected break-fraction per surah from non-terminal letter marginal: 66.1%
- Mean observed break-fraction: 22.7%
- Verse-ends are *dramatically* more rhyme-concentrated than the surah's own phonology predicts (−43.4 percentage-point deficit). This is a separate confirmation that rhyme is a deliberate constraint, but not the focus of H-NEW-1.

**Bimodality (key prediction):**
- Break-class bimodality-coefficient = 0.239 (< 0.555 threshold)
- Conform-class BC = 0.462 (also < threshold)
- **Bimodality is REFUTED.** The break-class distribution is unimodal with elevated mean, not a separate mode.

## Verdict: PARTIAL

- **Confirmed**: After controlling for class alphabet, break-class verse-ends are significantly less predictable within their class than conform-class verse-ends (z = 4.73 on residual statistic; robust across orthography; p < 10⁻⁴). The effect is real but small — 0.13 nats ≈ 13% residual surprise gap.
- **Refuted**: The strong form of the hypothesis — that break-verse surprise is **bimodal**, suggesting phonetically-engineered speed-bumps as a distinct mode — does not hold. Break verses are more surprising on average, not qualitatively different.
- **Honest characterization**: rhyme-breaks are modestly less within-class-predictable than rhyme-conforming verse-ends, but the effect is in mean rather than mode. This is consistent with break-verses being content-driven (the rarer terminal is chosen because meaning/syntax forces it) rather than phonetic-speed-bump-driven.

## Garden of forking paths disclosure

### Choices made after seeing the data
- Added class-uniform baseline correction after seeing the raw z=40, because the raw statistic was clearly confounded by letter-frequency differences. This is a *defensive* adjustment that weakens the finding rather than strengthens it — but it was post-hoc and must be disclosed.

### Alternative rule tuples considered
- `orthography = min-tashkeel`: computed (residual diff 0.108 nats — same direction, slightly weaker, reported).
- `letter_definition = with-shadda-doubled`: not run; irrelevant on no-tashkeel.
- Alternative break-class definitions (last-pre-pause, last-root, stricter rhyme set): NOT run; committed to {ن,ا,م,ر,د} pre-inspection.

### Sibling hypotheses
- Null B (surah-marginal test) returned z at least as extreme (observed break-frac 22.7% vs expected 66.1%); this is a **separate** finding about rhyme-concentration, not about Markov surprise.
- Bimodality statistic: failed.

### Why this one and not those
- The residual-corrected statistic was the cleanest remaining test once the letter-frequency confound was disclosed. Raw statistic is misleading; residual statistic survives.

## Seed
`random.seed(20260413)` throughout. Raw result: `scratch/team-discovery/result-001.json`. Residual test: `result-001-residual.json`. Followup: `result-001-followup.json`.
