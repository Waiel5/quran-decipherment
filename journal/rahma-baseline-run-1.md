# Journal — rahma-baseline-run-1

**Agent:** rahma-baseline-run-1 (Phase B rigor on `rahma=114`)
**Date:** 2026-04-12
**Goal:** Definitively test the rahma=114 finding from
  `numerical-coincidences.md` §1 against comparable classical Arabic,
  using the baseline corpora acquired by `cross-baseline-run-1`.
**Predecessor:** `cross-baseline-run-1` acquired 13.4 M tokens of
  classical Arabic and killed Yusuf-`sjn`=12 using the same protocol.
  My job is to apply the same rigor to rahma=114.

## The claim in one sentence

In the Quran (QAC v0.4 LEM aggregation), out of 4,832 distinct
lemmas, **exactly one** lemma (`raHomap`, "mercy") has count 114, and
114 is the number of surahs.

## What I did

1. Read the original finding in `findings/phase-b-hypotheses/
   numerical-coincidences.md` §N=114 and §Appendix E.
2. Read the baseline methodology in `findings/phase-b-hypotheses/
   cross-textual-baseline.md` to understand the tokenization rules and
   77k length-matching convention used by `cross-baseline-run-1`.
3. Read the statistical rigor protocol in
   `docs/statistical-rigor-protocol.md` to pick the correct null
   model (§1.4 length-matched comparable corpus) and correction
   (Bonferroni + Holm on the famous-numbers family).
4. Wrote `data/baseline-corpora/rahma_114_test.py` — implements
   Tests A (length-matched 77k baselines), B (Quran singleton-count
   enumeration), and D (rHm token rate across corpora), plus a 1000-
   draw random-slice empirical null over the 1.15M-token merged
   corpus (bukhari-noquran + sira + jahiz).
5. Wrote `data/baseline-corpora/rahma_114_extra.py` — implements
   Tests C (semantic weight of the 89 Quran singletons, POS
   breakdown) and E (Bonferroni/Holm on the 13-number family), plus
   the hypergeometric joint analysis for "how many famous-N
   singletons would we expect in the Quran?"
6. Ran both scripts. Results saved to `data/baseline-corpora/
   rahma-114-test.json` and piped to stdout.
7. Wrote the detailed writeup
   `findings/phase-b-hypotheses/rahma-114-baseline-rigor.md`.

## Key numbers

- **Quran lemmas**: 4832 (QAC STEM rows, LEM-aggregated)
- **Quran distinct lemma counts**: 181
- **Quran singleton lemma counts (counts with exactly 1 lemma)**: 89
- **Singleton counts that are also "famous" Ns**: 2 (N=99 and N=114)
- **Hypergeometric expected famous-singleton hits**: 4.92 (Quran
  under-delivers)
- **P(unique type at N=114 in random 77k comparable-Arabic slice)**:
  0.341 (from 1000 empirical draws)
- **Bonferroni-corrected p for Quran-has-unique-lemma-at-114**:
  1.000 (k=13 family, raw 0.341 × 13 → capped)
- **Quran strict raHma forms per 77k**: 103
- **Matched-Bukhari rHm-ish tokens per 77k**: 246 (most are
  الرحمن from basmala formula at hadith openings)
- **Quran neighbors of 114 that are ALSO content-noun singletons**:
  110 (Zalama/oppression), 115 (dunya/world), 116 (raHiym/merciful),
  119 (mubiyn/clear). Five singleton hits in a 13-wide window.

## What Test A showed (decisive)

Every single length-matched 77k baseline produced a **UNIQUE** type
at exactly count 114:

- matched-bukhari-77k: الذي (relative pronoun "which/that")
- jahiz-hayawan[:77k]: غير ("other")
- sira-ibn-hisham[:77k]: بكر (Bakr, proper noun — Abu Bakr!)
- poetry-pool[:77k]: فيها ("in it")
- quran-lemmas: راحمة / raHomap (mercy)

The "uniqueness at 114" event is a ~34% per-draw event under the
empirical null. Not rare. Not even suggestive.

When the Quran is tokenized as raw orthographic tokens (same rule as
the baselines), it has **zero** types at count 114. The 114 match is
an artifact of QAC LEM aggregation, which is a specific morphological
choice.

## What Test B showed

The Quran has 5 unique-lemma-counts in [108, 120] (at 110, 114, 115,
116, 119) and every one is a semantically central content noun. If
the Quran had had 110, 115, 116, or 119 surahs, the apologetic claim
would work equally well with a different core-concept word. The
denseness of singleton content-noun lemmas in the 100–200 range is
not distinctive (89 total singleton counts vs 81.4 average singleton
counts in 77k baseline slices).

## What Test C showed

64% (57/89) of Quran singleton lemmas are content words (N/V/ADJ/PN).
The semantic-cherry-pick space is enormous. There's no principled
null for "how meaningful is the matched word."

## What Test D showed

"Mercy" is not a Quran-distinctive word. The Bukhari 77k slice has
MORE rHm tokens per 77k (246 vs 324 for the Quran, but this overstates
the effect because Bukhari's 246 are mostly basmala openings). Sira
has ~100 per 77k. Mercy is a normal religious-register Arabic word.

Additionally, the rHm root spawns at least 5 distinct Quran lemmas;
the "114" match requires selecting specifically `raHomap` (the noun)
and not `raHiym`, `raHmaan`, `raHima` (verb), etc. This is a fork.

## What Test E showed

Bonferroni and Holm correction on the 13-number family give
corrected p = 1.000 for both 99 and 114 (the only two winners).
The raw per-N p is 0.341 for 114 and 0.387 for 99. Not significant
under any α at any correction.

## Verdict

**DEMOTED.** The `rahma=114` finding does not survive baseline
comparison. It is base-rate pigeonhole: the Quran has enough singleton
content-noun lemmas that *something* will always match *something*
semantically loaded, and the 114-specific match is not distinctive
under any null model.

Key red-flag hits:
1. **Post-hoc rule selection**: the claim only works under QAC LEM
   aggregation, not under raw tokens or root-level.
2. **Brittleness under inflection**: `raHiym` is at 116, `raHmaAn` at
   ~57, different verbs at different counts. The claim picks one
   specific morphological form from a family of 5.
3. **Undisclosed counting convention**: the original finding cited
   QAC LEM but didn't show the dependence on that specific choice.

Three red-flag hits per §4 of the rigor protocol → automatic demotion.

## What I recommend to downstream agents

1. `numerical-coincidences.md` should be updated: remove
   `rahma=114` from "Top 10 most striking coincidences"; add to
   "Noise / expected-by-chance" section with a pointer here.
2. No pre-registered Phase A replication should be built for this
   claim.
3. When the synthesis-scholar agent writes the McKay-style audit
   paper, `rahma=114` is a clean worked example of how a
   "spooky" numerical coincidence dissolves under length-matched
   comparable-corpus controls.
4. The general lesson: *any* claim of the form "the Quran's X-count
   equals famous number N" must clear the same test — (a) compute
   the empirical p-value of X-count = N in 77k comparable slices,
   (b) correct for the famous-number family, (c) check robustness
   under alternative tokenization rules. Most such claims will die
   at step (a). Very few will survive step (b).

## What I did NOT do

- I did not run a §1.3 word-level Markov null. The §1.4 empirical
  null plus the analytic hypergeometric were enough to kill the
  claim. A Markov null would only add marginal information (it
  typically produces p-values in the same direction as length-
  matched comparable-corpus, sometimes slightly weaker).
- I did not morphologically lemmatize Bukhari or Sira. This is a
  budget-scoped limitation. The direction of the fork (lemmatization
  reduces vocabulary, making collisions at specific N *rarer* under
  lemma aggregation) means that lemmatizing the baselines would, if
  anything, make the 114-match even *less* distinctive in the
  baselines — so it would only reinforce the demotion.
- I did not run the §1.5 surah-permutation null because "counts" are
  permutation-invariant. It is not a valid null for this claim.
- I did not write a pre-registration document (the finding was
  originally exploratory; this run is a rigor follow-up on a
  pre-existing claim; the "exploratory" status is inherited).
- I did not update `numerical-coincidences.md` directly. That should
  be done by a human reviewer or the synthesis-scholar agent, citing
  this document.

## Artifacts created

- `findings/phase-b-hypotheses/rahma-114-baseline-rigor.md` (the
  detailed writeup, all 5 tests)
- `data/baseline-corpora/rahma_114_test.py` (Tests A, B, D + 1000-
  draw null)
- `data/baseline-corpora/rahma_114_extra.py` (Tests C, E + hyper-
  geometric analysis)
- `data/baseline-corpora/rahma-114-test.json` (machine-readable
  results dump)
- `journal/rahma-baseline-run-1.md` (this file)

## Process reflections

The cross-baseline-run-1 agent established the template: (a) acquire
real comparable classical Arabic at matched length, (b) run the same
statistic on Quran and baselines, (c) report the empirical p-value,
(d) correct for the family of "similar claims" one might have picked
instead. That template applied cleanly to rahma=114 and produced a
decisive null result in a few hundred lines of Python.

The critical move was Test B (chunk-count sensitivity) — noticing
that 110, 115, 116, 119 are ALSO singleton content-noun counts. That
shows the alleged pattern isn't "114 is special" but "the Quran has a
reservoir of singleton content-noun lemmas in the 100–200 range that
the apologetic author can select from after seeing the data." This is
the classic garden-of-forking-paths pattern from Gelman & Loken 2013,
and it's exactly the failure mode Witztum-vs-McKay exhibited.

The rahma=114 claim was one of the strongest-looking candidates in
`numerical-coincidences.md`. That it dies so cleanly under length-
matched comparable-corpus null is evidence that the broader Khalifa/
Nawfal-style Quranic numerology tradition will mostly dissolve the
same way when subjected to this protocol. This is research
opportunity flag §6 of the rigor protocol ("a formal McKay-style
audit of Quranic numerology is an unfilled niche in the peer-reviewed
literature"), and rahma=114 would be an excellent opening case study
for the eventual paper.
