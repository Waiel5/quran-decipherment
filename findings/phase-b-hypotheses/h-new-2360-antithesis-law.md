---
finding_id: H-NEW-2360
title: "Antithesis = minimal shared frame + disjoint content — corpus-wide LAW-PROMOTION test"
phase: B
date: 2026-05-29
author: Waiel Al-Shujaa
seed: 20260509
seed_replication: 20260601
n_perm: 10000
prereg_sha256: 5ecd80edc6983ff62782a849030fb43559ebed798b92c41c5510bc1533d6c252
verdict: "PARTIAL — Sub-test A PRE-COMMIT VIOLATION (content NOT disjoint; reversed at z=+13.0); Sub-test B PASS (shared minimal frame preserved, z=+37.9). The 3-way convergence does NOT promote to a corpus-wide law."
status: NULL-on-headline-claim, full prominence
---

# H-NEW-2360 — Does "antithesis = disjoint content + shared minimal frame" hold corpus-wide?

## Verdict (one line)

**The headline half — "disjoint content" — REVERSES at corpus scale (pre-commit violation,
full prominence). The supporting half — "shared minimal frame" — holds robustly. The 3-way
convergence (Q083-F-01 + Q066-F-01 + H-NEW-2290) is therefore confirmed as REAL FOR ITS THREE
HAND-FOUND CASES but does NOT generalize into a corpus-wide law. It is DEMOTED, not promoted.**

Pre-reg SHA-256 `5ecd80edc6983ff62782a849030fb43559ebed798b92c41c5510bc1533d6c252`, verified at
runtime. Seed 20260509, 10000 perms, Bonferroni k=2 (α_bon=0.025).

## What was tested

A GENERATOR slid non-overlapping W=5 verse-blocks over all 114 surahs (1,452 blocks, 112 surahs
with ≥2 blocks) and flagged every same-surah block-pair as ANTITHETICAL iff one block carries a
locked opposed-field's + pole and the other its − pole (the 8-field antonym lexicon, byte-identical
to the SHA-locked H-NEW-2290 instrument: faith↔disbelief, guidance↔misguidance, paradise↔hellfire,
light↔darkness, reward↔punishment, righteous↔corrupt, good↔foul, life↔death). This yielded
**3,853 antithetical block-pairs** corpus-wide (well above the 30-pair power floor).

For each antithetical pair, two pre-registered, direction-locked observables:

- **Sub-test A (content disjoint)** — content-root Jaccard (block roots MINUS the top-40
  high-frequency frame roots MINUS all field pole-markers), LOCKED to be BELOW a random
  same-surah W-block-pair null (z<0, lower-tail p<α_bon). This is the corpus-scale form of the
  Q083 observation "the two destiny-blocks share almost nothing."
- **Sub-test B (shared minimal frame)** — frame-root overlap (top-40 corpus roots shared between
  the two blocks), LOCKED to be non-zero and NOT depleted vs the same null. This is the corpus-scale
  form of "but they share the bare *kitābun marqūm / mā adrāka* scaffold."

## Results

| Arm | Statistic | Antithetical | Random null | z | Direction |
|:--|:--|--:|--:|--:|:--|
| **A content-Jaccard** | mean Jc | **0.04673** | 0.03913 | **+13.02** | **OVERLAP — REVERSAL** |
| **B frame-overlap** | mean Fo | **6.052** | 4.499 | **+37.93** | preserved (locked) |
| B zero-frame fraction | — | 0.013 | — | — | only 1.3% have no shared frame |

- **Sub-test A FAILED by reversing.** Antithetical block-pairs share *significantly MORE* content
  than random same-surah block-pairs, not less. The locked lower-tail p = 1.0; the reverse
  (upper-tail) direction is overwhelmingly significant. This is a clean **PRE-COMMIT VIOLATION**,
  published here with full prominence.
- **Sub-test B PASSED.** A shared minimal frame is not merely present — antithetical pairs share
  *more* frame than random pairs (z=+37.9), and only 1.3% of antithetical pairs have zero shared
  frame. The "shared scaffold" intuition is robustly correct; it just is not *minimal* relative to
  the rest.

### Robustness — the reversal is total (MW-3)

Every robustness arm reproduces both directions. The reversal of A is not a frame-removal artefact,
not a width artefact, not a frame-size artefact, not a seed artefact:

| Arm | n_anti | A: z (content) | B: z (frame) |
|:--|--:|--:|--:|
| Primary W=5, K=40 | 3853 | **+13.02** | +37.93 |
| R1 W=7 | 2355 | **+12.78** | +28.94 |
| R2 no frame removal | 3853 | **+18.54** | — |
| R3 K=25 | 3853 | — | +37.59 |
| R3 K=60 | 3853 | — | +41.08 |
| R4 replication seed 20260601 | 3853 | **+13.10** | +38.17 |

## Why it reversed — the intelligent reading (not a defeat, a refinement)

The reversal is not noise; it exposes a **scale-and-selection confound** in the original convergence,
and it is internally coherent with everything the project already knows about antithesis.

1. **Block-scale antithesis is a *jadal* (disputation) signature, dominated by faith↔disbelief.**
   Of the 3,853 antithetical pairs, **64% (2,460) are F1 faith↔disbelief**; the census is led by the
   long Medinan disputation surahs — **Q2 al-Baqara alone supplies 906 pairs**, Q3 424, Q4 263, Q9 149;
   56% of all antithetical pairs are Medinan. This is exactly the **H-NEW-2290 result** (antithesis
   concentrates in long surahs, 219/290 verse-pairs were faith↔disbelief). When a surah argues
   *believers-vs-disbelievers* across two of its blocks, both blocks are about the SAME polemical
   subject seen from two sides, so they share the surrounding argument vocabulary — **`wly` (allies),
   `Hkm` (judgment), `gfr` (forgiveness), `xyr`/`Hsn` (good), `qtl` (fighting), `$rk` (associating),
   `nSr` (help), `tbE` (following)** are the top shared content roots. Two sides of one argument
   overlap *more*, not less.

2. **The "disjoint content" intuition only holds for self-contained ESCHATOLOGICAL CATALOGUES**,
   which is precisely the Q83 case (*sijjīn / jaḥīm / maḥjūb* vs *ʿilliyyīn / naʿīm / raḥīq / misk /
   tasnīm / arāʾik* — each side a closed inventory of named, non-overlapping items). But this
   generator shows even the paradise↔hellfire field does NOT separate at corpus scale:
   **F3-only pairs mean Jc = 0.0439 > null 0.0391** — still above random. EVERY field is above the
   null (F1 0.0479, F2 0.0457, F3 0.0486, F5 0.0488, F6 0.0463, F8 0.0457, F4 0.0563, F7 0.0538).
   The disjoint-content pattern does not generalize to ANY antithetical field.

3. **Q083-F-01 was a genuine local outlier, not a sample of a law.** Its blocks (vv 7-17 ↔ 18-28)
   were *hand-selected adjacent, topically-matched destiny-catalogues* of equal length. The generator's
   random null (12.7 shared roots in Q083-F-01's own 11-verse-block null) and this corpus null both
   confirm those specific Q83 blocks are unusually disjoint — but they are a **rare existence-proof of
   maximal muqābala**, not the central tendency. Likewise Q066-F-01's "frame-driven" seal was a single
   *ḍaraba mathalan* exemplar-pair. Three carefully chosen showcase passages are not a corpus law.

This is the **same lesson cross-finding-026 codified for chiasmus**: a device that classical balāgha
prizes (and that exists at near-unique showcase intensity in 1-3 passages — Q2:131-144 for ring,
Q83:7-28 for muqābala) is *rare and local at every scale*, NOT a generalizing structural law. The
convergence I was asked to promote is the muqābala analogue of the chiasmus rarity.

## What survives, exactly

- **CONFIRMED (Sub-test B):** Antithetical blocks DO share a robust high-frequency frame (`Alh, qwl,
  kwn, rbb, ywm, qwm, Eml, ...`). This half of the convergence is corpus-true. But the frame is
  *richer*, not *minimal* — it is the ordinary connective tissue of Quranic Arabic, present at
  *above-random* density precisely because antithetical pairs cluster in long, lexically-dense
  argumentative surahs.
- **REVERSED (Sub-test A):** Antithetical blocks do NOT have disjoint content corpus-wide; they share
  significantly more content than random same-surah blocks, because block-scale antithesis is
  topical disputation, and two sides of one dispute share the dispute's vocabulary.

## Honest limits

- **Block scale ≠ the original verse-pair / hand-block scale.** The three converging cases were at
  the verse-pair (2290) and hand-picked-11-verse-block (Q83) scales. This test moves to fixed W=5/7
  non-overlapping blocks. The reversal is robust across W and is internally consistent with 2290's own
  finding, but I report transparently that the *unit of aggregation* differs from the three precedents.
  The lesson is the unit-sensitivity itself: "disjoint content" was an artefact of hand-selecting
  *length-matched topically-paired catalogues*, which a uniform generator does not reproduce.
- The frame is defined by top-K corpus frequency; the pass of Sub-test B is stable across K∈{25,40,60}.
- The content-Jaccard arm could in principle be re-run at a *cross-surah length-matched topically-paired*
  scale to chase the Q83 phenomenon directly; that would be a different (post-hoc) test and is flagged,
  not run, here (MW-7).

## Integration / classical anchoring

- **Refines, does not overturn, the muqābala tradition.** al-Suyūṭī (*al-Itqān*, nawʿ 59, *ṭibāq* /
  *muqābala*) and the balāgha tradition correctly identify antithesis as a marked figure. This finding
  locates it: at the corpus block scale it is a **Medinan disputation register** (overlapping content,
  shared frame), and the *content-disjoint* form (Q83-type closed-catalogue muqābala) is a rare,
  showcase intensity — not the norm.
- **Demotes the candidate cross-finding law.** MASTER-FINDINGS-LEDGER §10.101 item 2 had logged
  "Antithesis = shared-frame + disjoint-content (NEW candidate law)." This test REJECTS the
  disjoint-content half at corpus scale. The correct cross-finding status is: the convergence is a
  **3-case showcase observation**, not a law; the transferable correction is the *opposite* of what
  the candidate law proposed — **block-scale antithetical pairs are content-OVERLAPPING (jadal), and
  pure-disjoint muqābala is a rare existence-proof (Q83), parallel to the chiasmus rarity of
  cross-finding-026.**
- Joins the project's recurring signature: classical *census/figure-identification* is accurate
  (muqābala is real and marked), but the *generalizing-law* form asserted post-hoc does not survive a
  proper corpus-wide null with a locked direction.

## Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2360-antithesis-law.md` (SHA above)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2360.py` (SHA embedded, runtime-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2360.json`
- This findings file: `findings/phase-b-hypotheses/h-new-2360-antithesis-law.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
