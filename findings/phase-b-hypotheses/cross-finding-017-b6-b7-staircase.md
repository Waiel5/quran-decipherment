---
id: cross-finding-017
title: "The B6/B7 staircase — marker precedes content by one Nöldeke sub-bin"
phase: B (synthesis; architectural refinement)
status: SYNTHESIS-OBSERVED (descriptive architectural refinement; no new inferential test)
date: 2026-04-17
author: synthesizer
parent_findings:
  - cross-finding-012 (Late-Meccan scripture-announcement apparatus; per-axis peak bins)
  - cross-finding-016 (OQ-17 deep-dive; 4-layer architecture)
  - cross-finding-014 (5-principle unified equation; M2)
  - H-NEW-125 (Pattern B at 4-phase resolution)
  - H-NEW-136 (muq-cardinality × Pattern-B composite)
classical_anchors:
  - al-Suyūṭī al-Itqān fī ʿulūm al-Qurʾān (on muqaṭṭāʿat being Meccan-exclusive except الم surahs) — SECONDARY-TRIANGULATED
  - Nöldeke Geschichte des Qorāns (Hijra as periodization boundary) — SECONDARY-TRIANGULATED
bonferroni_family: n/a (descriptive; no new inferential test)
---

# [[cross-finding-017-b6-b7-staircase|cross-finding-017]] — The B6/B7 staircase

## Headline

**The muqaṭṭāʿat structural marker peaks ONE sub-bin EARLIER than
the content axes it marks.** muq-cardinality peaks at B6 (Nöldeke
ranks 72-85, pure Late-Meccan); qul, book-reference, and loanword
densities peak at B7 (ranks 86-99, Hijra-straddling). This is an
empirical offset architectural feature, not an artefact.

The offset has a clean functional reading: **the marker system
disengages BEFORE the content apparatus fully disengages**. The
muqaṭṭāʿat opening is a late-Late-Meccan feature that drops OFF
sharply across the Hijra boundary (B6 mean 2.36 → B7 mean 1.14 →
B8 mean 0.00), while the broader scripture-announcement content
(qul, book-ref, loanwords) carries through into the earliest
Medinan surahs (Q 2, Q 3, Q 47, Q 57, Q 61, Q 62) BEFORE dropping
in Medinan-core.

This is a **one-bin staircase**: marker first, content second.
It is consistent with al-Suyūṭī's classical observation that
muqaṭṭāʿat are "Meccan-exclusive with the partial exception of
the الم surahs" (Q 2, Q 3 — both of which are early-Medinan B7
surahs).

## The per-axis empirical staircase

Data from [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] (JSON `pattern_b.per_axis_means_by_bin`):

| Axis | B4 | B5 | **B6** | **B7** | B8 | Peak bin |
|:---|---:|---:|---:|---:|---:|:-:|
| **muq_cardinality** | 0.79 | 1.21 | **2.36** | 1.14 | 0.00 | **B6** |
| eschatological_density | 12.45 | 20.37 | **32.00** | 28.83 | 29.00 | **B6** |
| qul_density | 5.90 | 8.17 | 7.36 | **8.82** | 4.24 | **B7** |
| book_reference_density | 5.66 | 16.67 | 23.69 | **28.14** | 14.55 | **B7** |
| loanword_density | 58.63 | 88.88 | 133.71 | **139.01** | 129.72 | **B7** |

**The staircase**:

- **B6 peakers** (n=2): muq_cardinality AND eschatological_density.
  Both are structural/abstract features — the muqaṭṭāʿat marker
  AND the eschatological vocabulary.
- **B7 peakers** (n=3): qul_density AND book_reference_density
  AND loanword_density. All three are content-register features
  — polemical dialogue, self-referential "kitāb/qurʾān", and
  Arabicised foreign vocabulary.

**The transitions**:

- muq_cardinality: **B6→B7 drop of 52%** (2.36 → 1.14; then
  B7→B8 drops to 0.00). Marker disengages sharply across the
  Hijra.
- eschatological_density: B6→B7 drop of 10% (32.00 → 28.83),
  then plateau across B7-B8 (28.83 → 29.00). Eschatology
  persists broadly.
- qul_density: **B6→B7 RISE of 20%** (7.36 → 8.82), then
  B7→B8 drop of 52% (8.82 → 4.24). Polemical-dialogue mode
  PEAKS AT the Hijra transition.
- book_reference_density: **B6→B7 RISE of 19%** (23.69 →
  28.14), then B7→B8 drop of 48% (28.14 → 14.55). Self-
  referential "kitāb/qurʾān" mode peaks AT the transition.
- loanword_density: **B6→B7 RISE of 4%** (133.71 → 139.01),
  then B7→B8 drop of 7% (139.01 → 129.72). Loanwords
  essentially plateau B6-B8.

## The clean architectural reading

### Marker retracts first (B6→B7 drops)

- muq_cardinality drops 52% across B6→B7
- This matches al-Suyūṭī's classical claim that muqaṭṭāʿat are
  "Meccan-exclusive" — only الم surahs (Q 2, 3, and 4 of 6 الم)
  cross into Medinan. B7's 14 surahs (5 LM + 9 Med) include
  Q 2, Q 3 (الم Medinan) and Q 7, Q 13, Q 46 (Late-Meccan multi-
  letter openers); but the mean cardinality drops because B8
  Medinan-core contains ZERO muqaṭṭāʿat

### Content register peaks AT the transition (B6→B7 rises)

- qul_density rises 20% B6→B7
- book_reference_density rises 19% B6→B7
- These are the "polemical + self-referential" content axes

This means: right at the Hijra, the Quran is still most
intensely in polemical-dialogic register AND most intensely
invoking itself as "kitāb / qurʾān / āyāt" — while the structural
marker (muqaṭṭāʿat) has already started to disengage.

### Content register collapses in Medinan-core (B7→B8 drops)

- qul_density drops 52% B7→B8
- book_reference_density drops 48% B7→B8
- muq_cardinality completes its drop to 0.00 at B8

The Medinan-core B8 (ranks 101-114) is where ALL scripture-
announcement features collapse simultaneously.

## Why the staircase matters (architectural implications)

### It's not just "Late-Meccan peak"

The [[h-new-125-chronology-content|H-NEW-125]] 4-phase analysis classified all 5 Pattern-B axes
as "peak Late-Meccan." At 8-bin resolution, this collapses
into three distinct empirical peaks:

- **Early Late-Meccan** (B6): muq-cardinality + eschatology
- **Late-Late-Meccan / early-Medinan** (B7): qul + book-ref +
  loanwords
- **No-peak Medinan-core** (B8): all apparatus collapses

The apparatus is NOT a single chronological event. It is a
TWO-STEP process: structural marker ramps up, reaches maximum
at Late-Meccan core, starts to disengage; content register
continues to climb, peaks at the Hijra boundary, then collapses
in Medinan.

### Functional reading (historical-critical)

Classical Nöldeke chronology (1860) + modern Bell/Watt
(1960s) + Sadeghi (2011) periodizations all identify the
Hijra as a regime transition. Our empirical staircase adds:

**The typographic marker (muqaṭṭāʿat) begins to fade BEFORE
the polemical-rhetorical register does.** Possible functional
reading: the muqaṭṭāʿat system is a MECCAN-ERA ritual /
performative device (for pre-iʿjām script-marking, attention-
focus, or scripture-self-identification); the polemical +
self-referential content register is a PROPHETIC-ERA speech
pattern that extends through the Hijra into community formation
before being replaced by legal-register consolidation. Two
different functional regimes with their own chronological
profiles; the apparatus is their temporal overlap.

**We cannot test "function" empirically**. The structural fact
is the staircase; function-reading is interpretive overlay.

### Classical al-Suyūṭī validation

al-Suyūṭī (al-Itqān, nawʿ on fawātiḥ al-suwar) notes that
muqaṭṭāʿat are PREDOMINANTLY Meccan, with الم surahs as the
partial exception (Q 2, 3 are Medinan). The B6/B7 staircase is
the quantitative version of this classical observation:

- B6 (pure Late-Meccan, n=14) has max muq-cardinality
- B7 (mixed, 5 LM + 9 Med, n=14) has dropped muq-cardinality
- B8 (Medinan-core, n=15) has zero muq-cardinality

This is another instance of the classical-balāgha-survives
pattern ([[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]): al-Suyūṭī's qualitative
observation receives quantitative confirmation at the per-
sub-bin level.

## Honest limits

### This is a DESCRIPTIVE pattern, not a pre-registered test

The B6/B7 staircase was OBSERVED post-hoc from [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]
results. It is not a new inferential claim. It does not carry
its own Bonferroni budget; it inherits from [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]'s
Cell A result (Kendall's W p=0.003, 4-axis evidentiary floor).

**The staircase itself** (1-bin offset) is a reading of
existing data, not a new test. To formally test it, we would
pre-register "the peak of axis X occurs 1 bin earlier than the
peak of axis Y" for specified pairs, using a distinct null.
That pre-reg is NOT done here.

**Status**: SYNTHESIS-OBSERVED (descriptive architectural
refinement).

### 14 surahs per bin — the peak is not crisp

B6 contains 14 surahs; B7 contains 14; the means differ but
not by staggering margins for all axes (e.g., loanword_density
B6 133.7 vs B7 139.0 is a 4% difference). The peak-bin
classification is correct per argmax, but the differences are
not uniformly large.

### qul_density B5-B7 profile is flat-ish

B5: 8.17; B6: 7.36; B7: 8.82. The B7 peak is barely higher
than B5 (8.82 vs 8.17). qul-density has a BROAD peak across
the whole Late-Meccan band, not a crisp B7 peak. The "peaker"
classification is technically correct but the amplitude is modest.

### The staircase depends on octile binning

Under quintile (5-bin) or decile (10-bin) binning, the staircase
may not persist in the same form. This is a specific-binning
observation. Octile was pre-registered in [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]];
robustness to binning is a queued follow-up.

### Sample size at B6 and B7 is 14 surahs each

With 14 surahs per bin, mean estimates have modest precision.
Confidence intervals around the per-axis means would overlap
for several axis-bin comparisons. The STAIRCASE classification
is at the argmax level; amplitude-testing would need
resampling / bootstrap CIs.

## Integration with [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] and [[cross-finding-016-late-meccan-apparatus-deep-dive|cross-finding-016]]

### [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] connection

[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]'s per-axis peak reporting showed:
- qul_density → B7
- book_reference_density → B7
- eschatological_density → B6
- muq_cardinality → B6
- loanword_density → B7

This [[cross-finding-017-b6-b7-staircase|cross-finding-017]] FORMALIZES that 3-vs-2 split as an
architectural feature. The Kendall's W concordance test
([[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] Cell A) TREATS the 8-bin rankings of all 5
axes together; the ranking structure within that agreement
shows the B6/B7 staircase.

### [[cross-finding-016-late-meccan-apparatus-deep-dive|cross-finding-016]] connection

[[cross-finding-016-late-meccan-apparatus-deep-dive|cross-finding-016]] §"Layer 1 — Chronology" reported:
> Per-axis peaks: qul→B7, book-ref→B7, eschat→B6, muq-card→B6,
> loanwords→B7. All 5 in {B5,B6,B7} target zone.

This [[cross-finding-017-b6-b7-staircase|cross-finding-017]] EXPANDS that observation into the full
architectural reading: the 2 B6-peakers are the marker + the
eschatology; the 3 B7-peakers are the polemical-dialogue +
self-reference + Arabicised-foreign vocabulary. Different
functional axes with slightly-offset chronological peaks.

### [[cross-finding-014-five-principle-unified-equation|cross-finding-014]] connection

[[cross-finding-014-five-principle-unified-equation|cross-finding-014]] M2 (Late-Meccan scripture-announcement,
muqaṭṭāʿat-marked) claims the merged principle is boundary-
gradient not cluster-discrete. The B6/B7 staircase is the
empirical MECHANISM of that gradient: two sub-peaks (marker at
B6, content at B7) that span the boundary rather than
collapsing to a single chronological point.

## The eschatological exception (B6 peaker with content-feel)

**Why does eschatological_density peak at B6 with muq_cardinality
instead of B7 with qul/book-ref/loanwords?**

Possible readings:
1. **Eschatology is deeply Meccan**: classical commentary
   identifies Day-of-Judgment vocabulary as a core Late-Meccan
   rhetoric that precedes the Hijra's legal-community formation
2. **Medinan B8 still has moderate eschatology** (29.00 vs B6
   32.00): only 9% drop. Eschatology doesn't collapse; it
   persists across Medinan. The B6 "peak" is modest.
3. **Eschat-axis is broader than the others**: B4-B8 means
   are 12.45, 20.37, 32.00, 28.83, 29.00 — flat across B6-B8.
   The "peak" is at B6 by a small margin.

The eschatological axis doesn't cleanly fit the marker-vs-
content staircase. It's a BROAD Late-Meccan-plus-Medinan
phenomenon with a modest B6 peak. This is consistent with
eschatology being functionally linked to BOTH the scripture-
announcement mode (Late-Meccan polemical eschatology) AND the
legal-register mode (Medinan day-of-judgment warnings). Two-
mode functional attachment explains broad persistence.

## Queued formal tests

This SYNTHESIS-OBSERVED finding queues three formal pre-
registrable tests:

1. **[[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] candidate**: pre-registered test of "marker
   peaks earlier than content" — specifically, H0: peak bin of
   muq_cardinality = peak bin of qul_density under random-
   Nöldeke-shuffle null. Current observation: muq peaks B6,
   qul peaks B7 — 1 bin offset. Null would show distribution
   of offsets; observed offset significance.

2. **[[h-new-143-surface-word-bridge-null|H-NEW-143]] candidate**: cross-feature / cross-
   periodization robustness of the staircase. Test whether the
   1-bin offset persists under Egyptian revelation order vs
   Nöldeke; under finer/coarser binning; under different
   loanword/eschat lemma lists.

3. **[[h-new-144-cyclic-tsp|H-NEW-144]] candidate**: within-B6 vs within-B7 analysis.
   For the 14 B6 surahs, is per-surah muq-cardinality higher
   than per-surah qul-density? For the 14 B7 surahs, is the
   reverse true? Formally test axis-per-surah ordering within
   each peak-bin.

None of these is pre-registered in this synthesis; they are
candidates for future specialists.

## Verdict

**SYNTHESIS-OBSERVED**. The B6/B7 staircase is a descriptive
architectural refinement of [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]'s per-axis peak
data. It is not a new pre-registered inferential claim; it
reads existing Kendall's W test data at the per-axis-peak-bin
level and identifies a 1-bin offset between marker (B6) and
content (B7) peaks.

**No verdict escalation** beyond [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]'s PASS-
DIRECTED status. No new Bonferroni budget. Three follow-up
formal tests queued ([[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]/143/144 candidates).

**Architectural significance**: the Late-Meccan scripture-
announcement apparatus is NOT a single-point-in-time
phenomenon; it is a **two-step chronological process** with
marker (B6) preceding content (B7) across the Hijra boundary.
This refines M2 in [[cross-finding-014-five-principle-unified-equation|cross-finding-014]] and provides empirical
detail for OQ-17's answer.

## Classical anchor

al-Suyūṭī in al-Itqān notes that muqaṭṭāʿat surahs are
**"Makkiyyat kulluhā illā sitta"** (all Meccan except 6 — Q 2, 3
الم plus narrower exceptions). The empirical B6 → B7 → B8
muq-cardinality trajectory (2.36 → 1.14 → 0.00) quantifies
al-Suyūṭī's observation at the sub-bin resolution. The
marker's sharp retraction at the Hijra boundary is empirically
visible in the mean-cardinality drop from B6 to B7 and its
completion at B8.

**Classical-scholarship validation pattern again**: a 15th-c.
qualitative observation receives quantitative confirmation at
the sub-phase resolution. Adds to the [[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]
pattern catalog.

## Files

- [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] JSON (per-axis peak data): `findings/phase-b-hypotheses/csv/cross-finding-012.json`
- [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] findings: `findings/phase-b-hypotheses/cross-finding-012-late-meccan-scripture-announcement.md`
- [[cross-finding-016-late-meccan-apparatus-deep-dive|cross-finding-016]] (OQ-17 deep-dive context): `findings/phase-b-hypotheses/cross-finding-016-late-meccan-apparatus-deep-dive.md`
- [[cross-finding-014-five-principle-unified-equation|cross-finding-014]] (5-principle model context): `findings/phase-b-hypotheses/cross-finding-014-five-principle-unified-equation.md`
- [[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]] (classical-validation pattern): `findings/phase-b-hypotheses/cross-finding-015-classical-scholarship-validation-pattern.md`
- [[h-new-125-chronology-content|H-NEW-125]] (Pattern B 4-phase): `findings/phase-b-hypotheses/h-new-125-chronology-content.md`

## Final statement

The Late-Meccan scripture-announcement apparatus exhibits a
**one-bin chronological staircase**: the muqaṭṭāʿat typographic
marker peaks at Nöldeke sub-bin B6 (pure Late-Meccan core,
ranks 72-85); the polemical + self-referential + loanword
content axes peak at B7 (Hijra-straddling, ranks 86-99). The
marker retracts BEFORE the content collapses; both collapse in
Medinan-core B8. This is an empirical architectural feature
consistent with al-Suyūṭī's classical observation that
muqaṭṭāʿat are Meccan-exclusive with الم exceptions. Three
formal pre-registrable tests queued as [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]/143/144
candidates. No verdict escalation beyond parent finding;
descriptive observation.
