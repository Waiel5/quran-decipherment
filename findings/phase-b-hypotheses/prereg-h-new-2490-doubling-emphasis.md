---
finding: H-NEW-2490
title: The ADJACENT DOUBLING-FOR-EMPHASIS device (taʾkīd bi-l-tikrār) — corpus census + genre-concentration test
author: Waiel Al-Shujaa
date: 2026-05-30
phase: B
status: PRE-REGISTERED (locked before computation)
seed: 20260509
nperm: 10000
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi); morphology lens = QAC v0.4 segment-level for connective/core separation
---

# H-NEW-2490 — Adjacent doubling-for-emphasis (taʾkīd bi-l-tikrār) census

## 0. Provenance and relation to prior findings

This finding extends the project's **repetition scale-ladder** at its tightest, most
semantically-constrained rung:

```
H-NEW-2100 / 2140 (refrain saturation)
  → H-NEW-2310 (metronomic refrain-spacing)        [byte-exact cross-verse refrain]
  → H-NEW-2350 (exact cross-surah verse twin)
  → H-NEW-2380 (near cross-surah verse twin, edit mechanisms)
  → Q094-F-01 (the corpus-tightest adjacent couplet, edit-distance 1)   §10.118
  → H-NEW-2450 (adjacent near-verbatim reprise census; ANY edit-mechanism)  §10.125
  → H-NEW-2490 (THIS): adjacent DOUBLING-FOR-EMPHASIS — the directional REASSERTION subset
```

**The seed** (from MASTER-FINDINGS-LEDGER §10.114 Q102-F-01 B-H1 and §10.125
H-NEW-2450): the *thumma*-doubled adjacent threat-refrain is a 3-member family
`{Q75:34-35, Q78:4-5, Q102:3-4}`. Verified directly from
`quran-text/quran-no-tashkeel.json`:

| pair | verse i | verse i+1 | relation |
|:--|:--|:--|:--|
| Q75:34-35 | أولى لك فأولى | ثم أولى لك فأولى | i+1 = [thumma] + i |
| Q78:4-5 | كلا سيعلمون | ثم كلا سيعلمون | i+1 = [thumma] + i |
| Q102:3-4 | كلا سوف تعلمون | ثم كلا سوف تعلمون | i+1 = [thumma] + i |

In all three, the **second verse's token sequence equals [connective `thumma`] +
the first verse's token sequence, with zero further change**. This is the textbook
rhetorical *taʾkīd bi-l-tikrār* (emphatic reassertion by repetition).

### Why this is a DISTINCT finding from H-NEW-2450

H-NEW-2450 cast the widest net: ANY adjacent pair with low character-edit distance,
under any mechanism (parallel-template slot-swap, rhyme-driven fāṣila re-tuning,
connective re-anchoring). Its roster of 33 (≤6 char-edit) is dominated by
**parallel templates** (two structurally-twinned but *content-different* verses,
e.g. swapping one noun) and **rhyme re-tunings**. Those are NOT doublings-for-emphasis.

H-NEW-2490 requires the strict, directional, semantic relation of **reassertion**:

> Verse/clause B is verse/clause A REPEATED — same lexical core, in the same order —
> differing ONLY by an emphatic **connective** (`thumma` / `fa` / `wa`) prepended or
> attached, and OPTIONALLY at most **one** minimal in-place core change (a
> person/number inflection of an already-shared root, or a tense particle swap
> `sawfa`↔`sa-`). No new content tokens are introduced.

A "parallel-template noun swap" (different content word) is NOT a doubling. A
"rhyme-driven final-word swap" (different rhyme word) is NOT a doubling. The
discriminator is **lexical-core containment**: B contains A's lexical core verbatim
(or with ≤1 inflectional change), the only addition being a connective.

## 1. The DEVICE — formal definition (LOCKED)

### 1.1 Tokenization / instrument (MW-1)

- Text: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- Pause/waqf/codex glyphs U+06D6..U+06ED stripped before tokenizing (the H-NEW-2380/2450 lesson).
- Morphology lens: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4),
  used to **separate connective morphemes from the lexical core**. A "connective"
  is a `POS:CONJ` segment OR a `POS:SUP` (`sa`) particle when it is a SEGMENT-1
  PREFIX. The three named emphatic connectives are `wa` (و), `fa` (ف), `thumma` (ثم).
- A verse's **lexical core** = its orthographic token sequence with any leading
  connective stripped (standalone `ثم`, or a `fa`/`wa` prefix grapheme removed from
  the first token using QAC segment boundaries).

### 1.2 The doubling predicate D(A, B) (LOCKED, directional)

For an ordered pair of verses (A=verse i, B=verse i+1), or an ordered clause-pair
within one verse, define **B doubles A** iff ALL hold:

1. **Substantive**: A has ≥ 2 lexical-core tokens (excludes 1-word verses).
2. **Connective gate**: B (or A — the device is symmetric in WHICH member carries the
   connective) begins with exactly one emphatic connective `∈ {wa, fa, thumma}`
   that the other member does not, OR the two members carry *different* leading
   connectives of this set. The leading connective is the ONLY licensed structural
   difference.
3. **Core containment**: after stripping each member's leading connective, the two
   lexical cores are EQUAL, OR differ by exactly **one** minimal in-place change:
   - a substitution where both tokens share the same QAC ROOT (inflectional shift,
     e.g. `taʿlamūn`↔`yaʿlamūn`), **or**
   - a `sawfa`↔`sa-` future-particle swap (`sawfa taʿlamūn` ↔ `sa-taʿlamūn`).
   No insertion/deletion of a *content* token is allowed; no different-root
   substitution is allowed.

The connective TYPE recorded for each hit is the distinguishing connective
(`thumma` / `fa` / `wa` / `bare`, where `bare` = identical cores with NO connective
difference, i.e. a pure verbatim doubling — reported but flagged, expected count 0
adjacent per H-NEW-2450's "0 exact-verbatim adjacencies").

### 1.3 Two grains (both reported)

- **VERSE-grain**: adjacent same-surah verse pairs (i, i+1) only. 113 cross-surah
  junctions EXCLUDED (one canonical text; cross-surah is H-NEW-2350/2380's domain).
- **CLAUSE-grain (within-verse)**: a verse split on its internal connectives; if two
  consecutive clauses satisfy D, it is a within-verse doubling (e.g. the seed
  Q75:34 *awlā laka* / *fa-awlā* is itself a within-verse fa-doubling of *awlā*).
  Clause-grain is reported as a CENSUS (descriptive roster), not used in the locked
  null test (its segmentation has researcher degrees of freedom; flagged MW-7).

## 2. HYPOTHESES — direction LOCKED before observation

Family of k=1 confirmatory test (H1). H2 is a descriptive census, NOT a second
confirmatory cell, so the confirmatory family is k=1 and α = 0.05. (If H1 and H2
were BOTH confirmatory the family would be k=2, α=0.025; we pre-commit H1 as the
SOLE confirmatory test, H2 reported descriptively with its own one-sided p for
transparency. This is the conservative reading — see §4.)

### H1 (PRIMARY, confirmatory, LOCKED DIRECTION)

> **The adjacent doubling-for-emphasis device is GENRE-CONCENTRATED in the
> eschatological/warning register (juzʾ-ʿamma, mushaf id 78–114, the short-Meccan
> threat-passages) ABOVE the corpus baseline.**

Statistic: per-surah **doubling rate** = (# adjacent verse-pairs satisfying D) /
(# substantive adjacent verse-pairs). Δ = mean_rate(juzʾ-ʿamma 78–114) −
mean_rate(rest 1–77).

- **Direction LOCKED**: Δ > 0 (juzʾ-ʿamma rate STRICTLY GREATER than the rest).
- Null: label-permutation — randomly relabel which surahs are "juzʾ-ʿamma" (preserving
  count n_amma), recompute Δ, 10000 perms, seed 20260509.
- **PASS** iff Δ > 0 AND p_one-sided < 0.05.
- **REVERSED → NULL with full prominence** iff Δ ≤ 0 (juzʾ-ʿamma rate ≤ rest). This is
  a pre-commit violation and will be published as NULL, no massaging.
- **NULL (held, n.s.)** iff Δ > 0 but p ≥ 0.05.

Robustness (MW-5 replication): re-run null with seed 20260519. Robustness (MW-3
alternative genre cut): also report the Meccan-vs-Medinan split (`type` field) as a
secondary, non-confirmatory genre axis.

### H2 (SECONDARY, descriptive census — NOT confirmatory)

The full corpus roster of every adjacent verse-pair satisfying D, with connective
type (`thumma` / `fa` / `wa` / `bare`), region, juzʾ-ʿamma flag, and the single
licensed change (if any). Plus the within-verse clause-doubling roster. Plus the
connective-type distribution (thumma vs fa vs wa vs bare). The seed family
`{Q75:34-35, Q78:4-5, Q102:3-4}` MUST appear as a validity check (fail-fast if any
seed is absent from the verse-grain roster).

## 3. SUCCESS / FAILURE CRITERIA (LOCKED)

- **VINDICATED**: H1 PASS (Δ>0, p<0.05) AND all 3 seeds present AND ≥2 connective
  types represented.
- **PARTIAL**: H1 holds direction but n.s., OR census delivered but H1 n.s.
- **REVERSED / NULL (full prominence)**: H1 Δ ≤ 0. Published as NULL; the doubling
  device is NOT genre-concentrated (it is corpus-spread or anti-concentrated).
- **DATA-GAP**: any seed absent → halt, debug the predicate, do NOT proceed.

## 4. Bonferroni / multiple-comparison accounting

- Confirmatory family: k = 1 (H1 only). α = 0.05.
- H2 is descriptive (census + distribution); any p reported there is informational,
  capped at single-test α=0.05 under MW-7 (post-hoc cap) and NOT used for the verdict.
- The Meccan/Medinan robustness axis is a secondary lens (MW-3), reported with its
  own raw + α=0.05 p, not pooled into the confirmatory family.

## 5. MW protections

- **MW-1 instrument-prior**: predicate D, connective set {wa,fa,thumma}, QAC-segment
  core-stripping, and the ≤1-minimal-change rule are ALL fixed here, before any run.
- **MW-2 corpus-prior**: 10000-perm label-permutation null.
- **MW-3 alternative-models**: juzʾ-ʿamma cut AND Meccan/Medinan cut both reported.
- **MW-4 over-fitting**: no fitted parameters (the bands are integers locked here).
- **MW-5 replication**: second seed (20260519) for the null.
- **MW-6 instrument-control**: the H-NEW-2450 roster (≤3 char-edit) is the
  super-set; D is a strict subset — report how many of 2450's low-edit pairs are
  rejected by D (they should be the parallel-template / rhyme-swap pairs), as a
  cross-check that D is genuinely SELECTING reassertions, not all look-alikes.
- **MW-7 post-hoc cap**: clause-grain census and all H2 numbers carry single-test α.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)` for the text; QAC v0.4 segment-level morphology as the
connective/core-separation lens. Deviation from default: the morphology lens is
introduced ONLY to separate connectives from cores (it does not change the
underlying canonical text). Cross-validated against raw-orthographic prefix
detection (fa/wa attached graphemes) as a robustness check.

## 7. Classical grounding (cite scholar + work + passage)

- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 60** (al-badīʿ): lists
  **al-Takrār (Repetition)** among the rhetorical devices
  (`data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`,
  extracted text line ~3560: ">l-Takr~r (Repetition)"); and the discussion (≈line
  11094) that a statement free of repetition is "superior" except where repetition
  serves a rhetorical function — exactly the *taʾkīd* (emphatic) function tested here.
- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*** — the chapter on *al-taʾkīd*
  (confirmation/emphasis) and on *al-tikrār*: repetition with a connective
  (`thumma`/`fa`) is the canonical means of *taʾkīd lafẓī* (verbal emphatic
  reassertion). (`data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf`.)

## 8. Honesty notes

- This is COMPOSITIONAL repetition in ONE canonical text — NOT qirāʾāt or naskh.
- The clause-grain segmentation has researcher degrees of freedom → descriptive only.
- The ≤1-minimal-change rule is the single most consequential design choice; it is
  fixed here and justified by the seed Q102 family (which has 0 changes) and the
  natural extension to person-shift twins like Q102:3↔Q78:4 (taʿlamūn/yaʿlamūn).
- Direction of H1 is locked: juzʾ-ʿamma > rest. A reversal is a real finding (the
  device would be corpus-spread, not eschatology-bound) and will be published as NULL.
