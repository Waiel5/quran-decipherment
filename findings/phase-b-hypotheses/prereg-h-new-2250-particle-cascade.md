---
id: H-NEW-2250
title: Particle-cascade structures — verse-initial fa- / thumma- / wa-idhā chains
type: pre-registration
date: 2026-05-29
author: Waiel Al-Shujaa
status: LOCKED (pre-observation)
seed: 20260509
n_perm: 10000
bonferroni_family: 3 (fa- / thumma- / idhā-conditional)
---

# Pre-registration — H-NEW-2250: Particle-Cascade Structures

## 0. One-line statement

Build a GENERATOR that enumerates every **maximal run** of consecutive verses
sharing the same **verse-initial particle**, for three particle families —
(a) `fa-` (فَ) sequential-narration prefix, (b) `thumma` (ثُمَّ) temporal-succession
conjunction, (c) the `idhā` (إِذَا / وَإِذَا) eschatological conditional-temporal head.
This goes **beyond** verse-initial anaphora (H-NEW-2140, identical-word runs):
here the run is defined by a shared *grammatical particle class* at the verse head,
detected from QAC part-of-speech tags, not by surface-identical opening word.

## 1. Background / relation to prior findings

- **H-NEW-2140** (§10.77): verse-initial *anaphora* runs (identical opening WORD,
  ≥3 consecutive). Found 64 runs; two corpus-extreme 9-runs (Q 26:23-31 *qāla*,
  Q 52:35-43 *am*). Notably it already surfaced **Q 81:2-8 وإذا (length-7)** as a
  notable run. H-NEW-2250 generalises from surface-word identity to
  particle-CLASS identity, which (i) can MERGE adjacent verses that share a
  particle class but differ in the following word, and (ii) lets us isolate the
  three classical "cascade" devices by grammatical function.
- **H-NEW-1320 / H-NEW-1790** (refrains): cascades are the consecutive-verse,
  fixed-head analogue of distributed refrains.
- **H-NEW-1870** (pronominal-narrative law): `fa-` and `thumma` cascades are the
  connective skeleton of the Quran's narrative mode.

## 2. Data sources (all on disk; cite paths)

- Verse text & ordering: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
  (114 surahs, 6236 verses, Hafs-Kufan).
- Verse-initial particle POS: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`
  (QAC v0.4, Buckwalter). The **first word** of each verse is location `(s:v:1:*)`;
  its first segment token `(s:v:1:1)` carries any proclitic prefix.

## 3. Detection rules (rules-tuple) — LOCKED

Rules-tuple: `(QAC-v0.4 POS tags, verse-initial = word-index 1, basmala excluded
as a verse only in Q1 per Hafs convention but basmala is its own verse 1:1 and
carries no fa/thumma/idhā head so handling is moot, Hafs-Kufan, Mashriqi)`.

A verse `(s,v)` is assigned at most ONE family head, decided on word-1 segments:

- **fa-** : segment `(s:v:1:1)` is a `fa` prefix — tag form `PREFIX|f:*+`
  (any subtype: REM / CONJ / RSLT / CAUS / SUP). This is the verse-initial
  sequential connective *fa-*.
- **thumma** : segment `(s:v:1:1)` is the standalone conjunction `vum~a`
  (`STEM|POS:CONJ|LEM:vum~`) — i.e. word-1 IS *thumma*.
- **idhā-conditional** (the eschatological "when…" head): word-1's STEM is the
  time-adverb `<i*aA` (`POS:T|LEM:<i*aA`), whether or not a `wa`/`fa` proclitic
  precedes it on the same word. This is the **semantically-correct** definition of
  the conditional cascade, because the "when the sun is folded up…" sense is
  carried by *idhā* regardless of the connecting *wa-*. (A verse like Q 81:1 begins
  with bare *idhā*; Q 81:2-8 with *wa-idhā* — both belong to the same cascade.)
  - **Sub-report (strict literal):** I will ALSO separately enumerate runs of
    the literal surface form `wa-idhā` (segment `(s:v:1:1)` = `w:` prefix AND
    `(s:v:1:2)` STEM = `<i*aA`) for the conjunction-purists. This sub-report is
    descriptive, NOT part of the Bonferroni family.

A **maximal run** = a maximal block of ≥3 consecutive verses *within one surah*
all sharing the same family head. Runs do not cross surah boundaries. Run length
= number of verses. Coordinates = `s:v_start–v_end`.

(`thumma` and `fa-` are mutually exclusive on word-1; if a verse begins
`fa-idhā` the `idhā`-STEM rule fires for the idhā family AND the `fa-` prefix
fires for the fa- family — such a verse is rare and will be flagged; for run
construction each family is scanned independently, so a `fa-idhā` verse can
legitimately participate in both a fa-run and an idhā-run. This is documented,
not hidden.)

## 4. Hypotheses — DIRECTION LOCKED

### Primary (pre-registered, direction-locked)
**H1 (eschatological-genre density).** The `idhā`-conditional family's
verse-initial head is an ESCHATOLOGICAL-GENRE marker. Its **density**
(idhā-headed verses per verse) in **juzʾ 30 / short-mufaṣṣal (surahs s ≥ 78)** is
**ABOVE the corpus mean**, and significantly so.
- **Direction LOCKED: density(s≥78) > density(corpus).** Higher in juzʾ-30.
- Statistic: `Δ = density(s≥78) − density(s<78)`. Predict Δ > 0.
- Null: permutation. Randomly relabel which verses are "idhā-headed" by shuffling
  the idhā-head indicator across all 6236 verse slots (preserving the total count
  of idhā-heads), 10,000 perms, seed 20260509; recompute Δ each time; p = fraction
  of permuted Δ ≥ observed Δ (one-sided, locked direction).
- **REVERSAL RULE:** if observed Δ ≤ 0 (density is NOT higher in juzʾ-30), the
  primary hypothesis is published as **NULL with full prominence / pre-commit
  reversal**, regardless of any cascade-run findings.

### Secondary (descriptive enumeration — the GENERATOR deliverable)
**H2.** Enumerate every maximal run (≥3) for all three families corpus-wide, with
length and coordinates. This is a census, not a significance test, but I
pre-commit to reporting ALL runs (no cherry-picking) and to ranking by length.

### Bonferroni family
Three particle families are tested for the density-concentration question.
The locked PRIMARY significance test is H1 on the **idhā** family only (the one
with a direction-locked genre prediction). For completeness I will ALSO run the
same juzʾ-30-density permutation test on the **fa-** and **thumma-** families
(no direction locked for those — two-sided, reported as exploratory). Because
3 families enter the density-test family, **Bonferroni k=3, α_cell = 0.05/3 =
0.0167**. H1 (idhā) is declared significant only if its one-sided p < 0.0167.

## 5. Success / failure criteria

- **CONFIRMED (directed):** idhā Δ > 0 AND one-sided perm-p < 0.0167 (Bonferroni-3).
- **DIRECTIONAL:** idhā Δ > 0 but 0.0167 ≤ p < 0.05.
- **NULL:** idhā Δ > 0 but p ≥ 0.05 (no concentration), OR
- **NULL / PRE-COMMIT REVERSAL:** idhā Δ ≤ 0 (wrong direction) — published with
  full prominence.
- The GENERATOR census (H2) is delivered regardless of H1 outcome.

## 6. MW protections

- MW-1 (instrument-prior): detection rules fixed above before any run.
- MW-2 (corpus-prior): 10,000-perm permutation null.
- MW-3 (alternative-models): density tested with the juzʾ-30 cut (s≥78) as
  pre-registered; robustness re-run with the alternative short-mufaṣṣal cut
  (s≥94, al-Aʿlā-onward "mufaṣṣal qiṣār") reported as a secondary lens.
- MW-5 (replication): second seed 20260511 for the null; result must agree.
- MW-6 (instrument-control): the fa- and thumma- families serve as
  non-eschatological-genre controls — if idhā concentrates in juzʾ-30 but fa/thumma
  do NOT, the genre-specificity is supported.
- MW-7 (post-hoc cap): no post-hoc claims promoted above α=0.05.

## 7. Output files

- This pre-reg (SHA-locked).
- Script: `findings/phase-b-hypotheses/scripts/h-new-2250.py` (embeds SHA, verifies at runtime).
- JSON: `findings/phase-b-hypotheses/csv/h-new-2250.json`.
- Findings: `findings/phase-b-hypotheses/h-new-2250-particle-cascade.md`.

## 8. Equal NULL prominence pledge

If H1 reverses or fails, the finding is published as NULL with the same
prominence as a confirmation. The cascade census is the honest deliverable
either way.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
