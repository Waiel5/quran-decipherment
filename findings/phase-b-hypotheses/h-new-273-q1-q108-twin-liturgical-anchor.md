---
id: H-NEW-273
title: Q1<->Q108 twin liturgical-anchor test
phase: B
status: PASS-NARROW — exact matched-null hit on one speech-act axis; contrast pair does not generalize
date: 2026-04-18
specialist: codex
seed: 20260418
rules_tuple: "(QAC v0.4 STEM roots via surah-root-graph.json; imperative density via imperatives-per-surah.csv; divine-reference root set {Alh,rbb,rHm}; surah score sqrt(divine_share * imperative_density); exact matched-null over Early-Meccan pairs with target verse bins {5-7,3-4})"
bonferroni: k=1 alpha=0.05 family=h-new-273-q1-q108-twin-liturgical-anchor
pre_reg: findings/phase-b-hypotheses/h-new-273-q1-q108-twin-liturgical-anchor-prereg.md
prereg_sha256: a7d159419d9e33825345abd5a6b02647169c9c4d6f9347079c0621e0eabd9827
script: scripts/h_new_273_q1_q108_twin_liturgical_anchor.py
output_json: findings/phase-b-hypotheses/csv/h-new-273.json
verdict: PASS-NARROW — under the locked score T(Q1,Q108)=S(Q1)+S(Q108), with S(s)=sqrt(divine-share x imperative-density), Q1+Q108 ranks 1st of 32 exact-matched Early-Meccan pairs and clears the one-sided exact null at p=0.03125. But the obvious refuge-pair contrast Q113+Q114 does not pass (p=0.1071), so this is not promoted as a generic liturgical-pair detector.
---

# [[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]] — Q1<->Q108 twin liturgical-anchor test

## Headline

This run deliberately avoids re-testing the already-landed wrap-around
distance claim. It asks a narrower question:

> if we score surahs only by the conjunction of
> 1. divine-reference root share and
> 2. imperative density,
> does `Q1 + Q108` stand out among short Early-Meccan matched pairs?

**Answer: yes, but only narrowly.**

Using the locked surah score

- `S(s) = sqrt(D(s) * I(s))`
- `D(s) = share of QAC STEM-root tokens in {Alh, rbb, rHm}`
- `I(s) = imperative tokens per verse`

the target pair `Q1 + Q108` is the **top-ranked matched pair** under the
exact Early-Meccan `{5-7, 3-4}`-verse null:

- observed pair score = **0.5172**
- null mean = `0.1811`
- null SD = `0.1513`
- descriptive `z = +2.22`
- exact upper-tail `p = 0.03125`
- rank = **1 / 32**

That is a real hit on this one axis. It is **not** a broad upgrade,
because the same metric does **not** recover the obvious refuge-pair
contrast `Q113 + Q114` (`p = 0.1071`).

## Locked result

### Primary target

Matched null:

- both surahs `Early Meccan`
- one surah in the `5-7`-verse bin
- one surah in the `3-4`-verse bin
- exact enumeration, no Monte Carlo

Target components:

| Surah | Divine share `D(s)` | Imperative density `I(s)` | Surah score `S(s)` |
|---|---:|---:|---:|
| Q1 al-Fatihah | **0.3043** | 0.1429 | **0.2085** |
| Q108 al-Kawthar | 0.1429 | **0.6667** | **0.3086** |

Pair score:

| Pair | Score |
|---|---:|
| **Q1 + Q108** | **0.5172** |

Exact null summary:

| Quantity | Value |
|---|---:|
| Null pair count | 31 |
| Null mean | 0.1811 |
| Null SD | 0.1513 |
| Exact upper-tail p | **0.03125** |
| Descending rank | **1 / 32** |

Top competing null pairs:

| Rank | Pair | Score |
|---|---|---:|
| 2 | Q108 + Q114 | 0.4530 |
| 3 | Q1 + Q112 | 0.4322 |
| 4 | Q108 + Q113 | 0.4241 |
| 5 | Q112 + Q114 | 0.3680 |
| 6 | Q112 + Q113 | 0.3391 |

So the signal is not that Q1 or Q108 are isolated winners separately.
It is that the exact `Q1 + Q108` pairing sits at the top of this small,
strictly matched pair space.

## Descriptive contrast

I also ran the same score on the refuge pair `Q113 + Q114` under its own
matched Early-Meccan `{5-7, 5-7}` null.

| Pair | Score | Exact upper-tail p | Rank |
|---|---:|---:|---:|
| Q113 + Q114 | 0.2598 | 0.1071 | 3 / 28 |

This does **not** pass. That matters.

It means the present metric is **not** behaving like a general
"liturgical pair" detector. It is picking up one narrower complement:

- Q1 contributes the strongest divine-reference side in the short
  Early-Meccan pool
- Q108 contributes the strongest imperative side in the `3-4`-verse pool

That is why the final label is `PASS-NARROW`, not `CONFIRMED`.

## Interpretation

On this bounded speech-act axis, the pair behaves exactly like a twin
anchor construction would suggest:

- **Q1** is high because it is saturated with `Alh / rbb / rHm`, even
  though it contains only one imperative.
- **Q108** is high because it pairs one divine-reference root with an
  unusually dense imperative profile (`fa-salli ... wanhar` over only
  three verses).

The geometric mean is doing useful work here. It suppresses:

- surahs with strong divine-reference mass but little imperative force
- surahs with strong imperative force but no divine-reference mass

The target pair survives exactly because **both** members have **both**
ingredients, but with different emphases.

## What this does not show

This run does **not** show that:

- Q1 and Q108 are the generic liturgical pair of the Quran
- the metric explains the wrap-around architecture
- liturgy caused the mushaf ordering
- Q113+Q114 or other classical recitation pairs should also pass

The contrast result explicitly blocks that overreach.

## Honest limits

1. **Metric-family selection was bounded, not blind.** I scoped a small
   set of candidate operationalizations before locking this first landed
   one. So this is a disciplined first-pass, not an audit-clean
   discovery-blind prereg.

2. **Small exact null.** The target null has only 31 alternative pairs.
   That makes the p-value discrete and limits resolution.

3. **Three-root divine lexicon only.** `{Alh, rbb, rHm}` is a
   deliberately tight set. A broader divine lexicon could change the
   ranking.

4. **Imperatives are pulled from the repo-wide extractor.** That
   includes `qul` imperatives and all QAC `IMPV` tags equally; this is a
   grammatical, not semantic, imperative measure.

5. **Contrast non-pass matters.** Because `Q113 + Q114` does not pass,
   the finding should be read as one narrow pair-specific hit, not as a
   general model of liturgical pairing.

## Bottom line

`[[h-new-273-q1-q108-twin-liturgical-anchor|H-NEW-273]]` lands a **bounded positive**:

**Under one exact matched-null speech-act score, `Q1 + Q108` is the top
short Early-Meccan pair at `p = 0.03125`.**

That is enough to say the twin-anchor idea has **one honest textual
foothold** beyond the already-known distance structure.

It is **not** enough to say the construct is generic or solved in full.
