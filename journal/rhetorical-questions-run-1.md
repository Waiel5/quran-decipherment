---
title: Rhetorical Questions — Run 1 Journal
agent: rhetorical-questions-run-1
date: 2026-04-12
---

# Journal: rhetorical-questions-run-1

## Data sources
- Quranic Arabic Corpus morphology v0.4 (Dukes) at
  `/data/morphology/quranic-corpus-morphology-0.4.txt`.
  The corpus provides POS tags including `INTG` (interrogative) with
  sub-distinction between standalone particles (*hal*, *mā*, *kayfa*,
  …) and the prefix hamza `أ-` interrogative.
- Quran Arabic text at `/quran-text/quran-no-tashkeel.json` (6236 verses).
- Rhyme fasila data at `/findings/phase-b-hypotheses/saj-fasila-per-verse.csv`.
- Ring-center identifications at `/findings/phase-c-structures/ring-center-semantics.md`.

## Method

1. **Extraction.** Parsed the morphology file for all tokens tagged
   `POS:INTG` and bucketed by (surah, ayah). Collected 946 INTG tokens
   across 830 verses.
   - 507 hamza-prefix `أ-` tokens
   - 439 standalone particles by lemma: `maA` 95, `hal` 93, `kayof` 80,
     `man` 37, `>aY~` 35, `>an~aY` 27, `maA*aA` 26, `kam` 20,
     `>ayon` 12, `mataY` 9, `>ay~aAn` 5.

2. **Formula detection.** Wrote a word-level pattern matcher over the
   segmented morphology. Each word in a verse has segments with features
   (hamza-INTG prefix, fa-SUP/CONJ, wa-CONJ, lā-NEG, lam-NEG, verb root).
   Detected classical formulas:
   - *a-fa-lā + Verb* — word has hamza-INTG + fa-SUP + lā-NEG; next word
     (or same word's verb) gives the target root.
   - *a-lam + V:rāʾ* — hamza-INTG + lam-NEG + next-word-root = `rAy`/`r>y`.
   - *a-wa-lam yara* — hamza-INTG + wa-CONJ + lam-NEG + `rAy`.
   - *hal yastawī* — INTG lemma `hal` + next verb root `swy`.
   - *a-fa-man* — hamza + fa + INTG man in same word.
   - *mā lakum / mā lahum* — INTG mā followed by `li + pronoun`.
   - *hal + min* — INTG hal followed by `min`.
   - Plus bare lemma counts for each particle.

3. **Type classification.** Rule-based 7-bucket classifier:
   - `ask-the-prophet (real Q)`: verse contains `V:sAl` + 2MS pronoun ("yas'alūnaka").
   - `prophet-speaking (challenge)`: verse opens with `V:qwl IMPV` ("qul …").
   - `rhetorical-negation (inkārī)`: contains hamza-INTG + lā-NEG or lam-NEG.
   - `rhetorical-affirmation (taqrīrī)`: opens with hamza-INTG, no negation.
   - `hal-rhetorical`, `kayfa-reproach-or-wonder`: by lemma.
   - `other-question`: default.

4. **Ring-center overlap.** Took the 5 ring centers from the Phase C
   findings (Baqarah 137-138/143, Qamar 25-26, ʿAbasa 5, Kahf 87, Hud 62)
   and checked INTG presence.

5. **Rhyme-break correlation.** Used the saj' agent's fasila CSV; a verse
   is a "rhyme-breaker" if its fasila-2 differs from the surah's modal
   fasila-2 (only for surahs where modal share ≥40%). 2×2 contingency
   with Q-verse membership.

6. **Al-Rahman patch.** Direct text scan for the refrain
   *فبأي آلاء ربكما تكذبان* surfaced 31 verses; only 16 were INTG-tagged
   in the morphology. Patched the remaining 15 into the CSV with an
   explicit `rhetorical-reproach (corpus-undertagged)` label.

## Key findings

- **Total Q-verses: 830 raw, 845 after patch** (~13.5% of Quran).
- **Most common formula**: verse-initial hamza-INTG (218 verses), then
  bare `mā` (95), `hal` (93), `kayfa` (80).
- **Most common composite formula**: *kayfa + Verb* (79), *a-lam + V*
  other than tara (51), **a-lam tara / a-wa-lam yara (53 combined)**,
  **a-fa-lā + V family (45 distinct verses)**.
- **Ring-center correlation**: 3 of 5 ring centers (Q 2:138, Q 54:25,
  Q 11:62) host a rhetorical question. All three are accusations in a
  prophet-rejection context.
- **Rhyme-break correlation**: NULL. O/E = 1.01 (229 observed vs 227.3
  expected). Q-verses and rhyme-breaks are independent.
- **Densest surah by Q-rate**: Al-Mulk (67) at 43.3%, then Al-Rahman (55)
  at 39.7% after patch.
- **Longest Q-chains**: Al-Mulk 67:16-22 and An-Naml 27:59-65, both 7
  consecutive Q-verses.
- **Counterfactuals**: `law` 176 verses, `laʿalla` 123 verses — companion
  modalities to the question.

## Data quality issue caught

The Al-Rahman refrain mis-tag (15/31 iterations tagged `N` instead of
`INTG`) is worth reporting upstream. This is a genuine Dukes v0.4
corpus issue. Any INTG-based analysis of Al-Rahman that doesn't patch
will under-count by 48%.

## Runtime / reproducibility

All analysis in Python 3, no external packages beyond stdlib (scipy was
absent — we hand-computed the O/E ratio). Scripts at `/tmp/rq/`
(ephemeral). CSVs produced:
- `rhetorical-questions-per-verse.csv` (845 rows)
- `rhetorical-questions-per-surah.csv` (114 rows)

## Caveats

- The heuristic 7-bucket classifier puts 447/830 verses in the
  "other-question" default bucket. Better classification requires human
  gold-labeling or a more sensitive rule set.
- The ring-center p ≈ 0.012 is one-shot, un-adjusted, and exploratory.
  Not pre-registered.
- The *yasʾalūnaka* real-question pattern is under-counted because
  many such verses *paraphrase* the original question in declarative form
  ("they ask you about the new moons…"), which puts no INTG in the
  Arabic even though a question is being reported. The explicit-INTG
  subset is only 8 verses.

## What I would do next

1. Have a human classify the 447 "other-question" verses by Suyūṭī's
   taxonomy (taqrīr, inkār, tawbīkh, taʿajjub, tahdīd, takdhīb,
   istikhbār-ḥaqīqī). Replace the rule-based bucket.
2. Pre-register the ring-center question-correlation as a formal test
   across not just the 5 Bonferroni-surviving rings but the top-20
   z-tier (gives n≥20 for a proper chi-square).
3. Audit the corpus against a second morphology source (e.g. LeDonne
   / Tanzil-with-Corpus-diff) to find other systematic mis-tags.
4. Study the "question-chain" as a literary form in its own right: are
   there exactly two length-7 chains, or is this a one-off? What's the
   distribution of chain lengths? How do they correlate with pericope
   boundaries?
5. Test whether *a-fa-lā + V* at verse-close predicts Meccan origin
   more than Medinan (a likely finding, given that Meccan is more
   argumentative).
