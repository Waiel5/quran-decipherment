---
id: H-NEW-134-FORMAL
title: Prophet-named surahs show a conservative surface-form narrative signature beyond name-root enrichment
status: PRE-REGISTERED 2026-04-18
date: 2026-04-18
author: codex
seed: 20260418
permutations: 100000
rules_tuple: (hafs-kufan; no-tashkeel; canonical 114; verse-level surface-token markers; exact slot-matched null by type × verse-count band × muq-status)
bonferroni_family: h-new-134-formal-prophet-named-signature
bonferroni_k: 2
alpha_bon: 0.025
verdict_ceiling: PASS-DIRECTED
---

# [[h-new-134-formal-prophet-named-signature|H-NEW-134]]-FORMAL — PRE-REGISTRATION

## Question

[[h-new-49-1-prophet-enrichment|H-NEW-49.1]] showed that prophet-named surahs are enriched in muqaṭṭaʿāt
openers, but that test remained close to the *name / label* layer.
This follow-up asks a stricter question:

> Do prophet-named surahs also share a reproducible **surface-form
> discourse signature** inside their verses, after controlling for broad
> confounds of revelation type, rough length, and muqaṭṭaʿāt status?

The present test is intentionally **not** a name-root enrichment test.
The primary family uses only verse-level surface markers that can be
counted without any prophet-name lexicon.

## Primary target set (STRICT, locked)

Primary set = the 6 surahs whose canonical title is an explicit prophet /
messenger proper name:

- Q 10 Yūnus
- Q 11 Hūd
- Q 12 Yūsuf
- Q 14 Ibrāhīm
- Q 47 Muḥammad
- Q 71 Nūḥ

This corrects the looser earlier practice of treating Maryam and Luqmān
as if they were "prophet-named". They are NOT in the strict primary set.

## Sensitivity set (EXPANDED PERSON-NAMED, locked)

Secondary sensitivity only:

- strict-6 above, plus
- Q 19 Maryam
- Q 31 Luqmān

This 8-surah set is a **named-human-figure** sensitivity set, not a
"strict prophet" set.

## Why this is a FORMAL test

The main family excludes:

- prophet-name roots
- proper-name lookup
- semantic topic lexicons like Mūsā / Firʿawn / banī-isrāʾīl
- morphological root-space distances

Instead, it uses only **surface discourse particles / verse markers**.

## Locked verse-level features

For each surah, define the fraction of verses containing at least one
instance of the marker.

### Axis A — VOCATIVE share

Fraction of verses containing the standalone token:

- `يا`

Interpretation: overt address density.

### Axis B — NARRATIVE-SEQUENCER share

Fraction of verses containing at least one standalone token from:

- `اذ`
- `واذ`
- `ثم`
- `فلما`
- `لما`

Interpretation: scene-transition / temporal-narrative sequencing density.

### Auxiliary audit (NOT in Bonferroni family) — SPEECH-VERB share

Fraction of verses containing at least one token from:

- `قال`
- `قالوا`
- `قالت`
- `قالا`
- `قيل`
- `قل`
- `قلنا`
- `يقول`
- `يقولون`
- `تقول`
- `نقول`

This is reported as an auxiliary audit because it is less purely formal
than Axes A-B and is closer to lexical content.

## Matching rule (PRIMARY null, locked)

Each strict prophet surah is assigned a slot defined by:

- revelation type: `meccan` / `medinan`
- verse-count band:
  - `100+`
  - `50-99`
  - `20-49`
  - `1-19`
- muqaṭṭaʿāt status: `muq` / `nonmuq`

The strict-6 slot profile is therefore:

- 3 × (`meccan`, `100+`, `muq`)  : Q 10, 11, 12
- 1 × (`meccan`, `50-99`, `muq`) : Q 14
- 1 × (`meccan`, `20-49`, `nonmuq`) : Q 71
- 1 × (`medinan`, `20-49`, `nonmuq`) : Q 47

Permutation null:

1. Remove the target-set members from the control pools.
2. For each permutation draw, sample without replacement the same slot
   profile from the remaining 108 surahs.
3. Compute the mean surah-level feature value across the sampled set.
4. Compare the observed strict-6 mean against the permutation
   distribution using a one-sided upper-tail test.

One-sided p-value:

- `p = (1 + # {perm_mean >= obs_mean}) / (1 + N_perm)`

This is a **conservative null** because it preserves the main broad
confounds already implicated in earlier work:

- Meccan / Medinan
- rough length tier
- muqaṭṭaʿāt status

## Primary inferential family

Bonferroni family `k = 2`:

1. Axis A — VOCATIVE share
2. Axis B — NARRATIVE-SEQUENCER share

Per-axis threshold:

- `alpha_bon = 0.05 / 2 = 0.025`

### Composite verdict (locked)

- 2 / 2 axes pass at `p < 0.025` -> `PASS-DIRECTED`
- 1 / 2 axes pass at `p < 0.025` -> `PARTIAL-PASS-DIRECTED`
- 0 / 2 axes pass -> `NULL`

`STRONG-PASS` is deliberately unavailable here because the axis family was
chosen after a small feasibility screen of nearby surface features.

## Sensitivity analyses (locked, non-family)

### S1 — Expanded 8-surah named-person set

Re-run Axes A-B with the expanded person-named set under the same slot
matching logic using that set's own slot profile.

Purpose: check whether the formal signature extends to the broader
person-named group without affecting the primary strict-6 verdict.

### S2 — Auxiliary speech-verb audit

Re-run the same strict-6 matched null on the SPEECH-VERB share.

Purpose: supportive narrative-dialogue check, not counted in the
Bonferroni family.

## MW-5 positive control (locked)

To validate the slot-matched permutation instrument, build a planted
non-prophet set as follows:

1. For each of the 6 strict slots, among the non-target surahs in that
   slot, choose the surah with the highest
   `VOCATIVE_share + NARRATIVE_SEQUENCER_share`.
2. This yields a deterministic 6-surah planted control with the same slot
   profile as the strict prophet set.
3. Re-run the same permutation null on Axes A-B for that planted set.

Expectation:

- both planted-control p-values should be `< 0.01`

If either planted-control axis fails `< 0.01`, the matching / permutation
instrument is suspect and the main verdict is downgraded to
`INSTRUMENT-BROKEN`.

## Garden-of-forking-paths disclosure

Important honesty note:

- I considered a broader nearby candidate list during feasibility
  inspection, including speech-verb share, ending-entropy, and
  verse-length CV.
- The locked primary family is restricted to the two **least
  semantically-loaded surface markers** that still directly express
  prophet-speech / narrative sequencing form: `يا` and the sequencer set
  `{اذ, واذ, ثم, فلما, لما}`.
- Because of that feasibility exposure, the ceiling remains
  `PASS-DIRECTED`, not `CONFIRMED`.

This is still stricter than the old name-root route because the main
family never checks whether the prophet's name appears.

## Publication commitments

- Publish the strict-6 result regardless of direction.
- Publish the expanded-8 sensitivity regardless of direction.
- Publish the speech-verb auxiliary audit even if null.
- Report observed means, null means, null SD, one-sided p, and
  Bonferroni verdicts.
- Include the SHA-256 of this prereg in the JSON output.

## Files

- Script: `scripts/h_new_134_formal_prophet_named_signature.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-134-formal.json`
- Findings: `findings/phase-b-hypotheses/h-new-134-formal-prophet-named-signature.md`
- Journal: `journal/h-new-134-formal-run-1.md`
