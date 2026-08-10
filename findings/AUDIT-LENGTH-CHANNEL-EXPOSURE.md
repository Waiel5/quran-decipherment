# Audit: how much of the corpus is exposed to the length-channel swing

**Date:** 2026-08-09
**Status:** CANDIDATE LIST — not a defect list. See §4 before citing any row.
**Driver:** [[cross-finding-029-the-deciding-parameter]], anchors 2 and 3.

---

## 1. What made this measurable

Two lanes on the same day found that a verdict can be decided by *which* length variable controls it:

- **H-NEW-3010** — same contrast, p = 0.0006 under log word count, p = 0.027–0.044 under mean verse
  length. A ~70× swing.
- **H-NEW-3040** — verdict *flipped* across eight control settings: 3 PASS, 5 NULL. The channel it
  locked a priori was not the dominant one for its grouping.

So *"residualised on length"* is an underspecified claim, and the project can be asked a mechanical
question: **how many analyses controlled for length on exactly one channel?**

## 2. The census

Scripts under `findings/phase-b-hypotheses/scripts/` and `scripts/` that residualise, stratify, or
length-match, classified by which channels they reference:

| | scripts |
|:--|--:|
| control for length in some form | **158** |
| …using **one** channel only | **120** |
| …using two channels | 30 |
| …using all three | 8 |

Single-channel breakdown: **verse count 77** · word count 40 · mean verse length 3.

## 3. Triage by direction — which way does the error point?

Under-controlling leaves residual confound in the outcome, which **inflates** significance. So the
defect is **LIBERAL: it manufactures passes.** That fixes the triage:

> **A finding that NULLed under a single weak channel is DOUBLY SAFE** — a stronger control would
> only have made it fail harder. **Only passing verdicts are at risk.**

Applying that filter — verse-count-only control *and* a passing verdict — leaves **20 distinct
findings**:

| finding | verdict as published |
|:--|:--|
| `h-new-46-1-chronology-disentangle` | STRONG-PASS (6/7 cells) |
| `h-new-85-oath-openers` | PASS (4 of 5 cells) |
| `h-new-91-rare-root-density` | PARTIAL-PASS |
| `h-new-112-spectral-network` | MARGINAL (1 of 2 cells) |
| `h-new-127-6-jurjani-tier-bridge` | POSITIVE |
| `h-new-140-divine-name-pair-cohesion` | PASS-DIRECTED (post-hoc) |
| `h-new-150-liturgical-hub` | WEAK-LINK |
| `h-new-155-q1-sui-generis` | SUI-GENERIS-CONFIRMED |
| `h-new-170-99name-network` | PASS-STRUCTURE-AND-GHAZALI |
| `h-new-187-lempel-ziv` | PASS (both primary cells) |
| `h-new-195-entropy-per-surah` | PARTIAL-PASS |
| `h-new-264-q1-connects-everything` | CONFIRMED |
| `h-new-270-hud-template-lattice` | PASS-DIRECTED (3/3) |
| `h-new-1380-iblis-pericope-replication` | PASS-DIRECTED-REPLICATION |
| `h-new-1500-christ-pericope-replication` | PASS-DIRECTED |
| `h-new-1520-prophet-vocative-pericope` | PASS-DIRECTED |
| `h-new-1550-oath-opener-cluster` | PASS-DIRECTED |
| `h-new-1750-alhamdu-opener-pericope` | PASS-DIRECTED (FLIP) |
| `h-new-1760-hawamim-opener-pericope` | PASS-DIRECTED (FLIP) |
| `h-new-2300-dual-name-fasila-seal` | EXTENDS H-NEW-2070 |

## 4. These are CANDIDATES, and publishing them as defects would repeat the error they describe

`TIED-OUTCOME-DEFECT` §7.1 states the rule this file is bound by: *a keyword screen produces
candidates; only reading the outcome produces a verdict.* Nothing here has been read. Three specific
reasons a row may be perfectly sound:

1. **Verse count may be the correct and dominant channel for that grouping.** H-NEW-3010's grouping
   happened to be dominated by mean verse length (ρ = +0.55 against +0.07 for verse count) — that is
   a property of *its* grouping, not a general fact. The decisive per-finding question is
   **which channel is dominant for this grouping**, and it is one Spearman correlation to answer.
2. **Six of the twenty are pericope-scale** (`1380`, `1500`, `1520`, `1550`, `1750`, `1760`). At
   pericope scale the natural unit genuinely is the verse, so verse count may be the right control
   rather than a lazy one.
3. **The screen itself is unreliable in both directions.** It matches variable names by regex; a
   script computing mean verse length as `n_words/n_verses` without ever naming it would be
   misclassified as verse-count-only. There will be both false positives and false negatives here —
   the same weakness that made the frontier-map staleness screen non-certifying.

## 5. The check, and it is one line

For any finding on this list, before treating it as either sound or defective:

> Compute Spearman ρ between the grouping variable and **each** of verse count, word count, and mean
> verse length. If the channel actually used is not the one with the largest |ρ|, re-run under the
> dominant channel and report both.

That is the whole test. It requires no re-design, no new pre-registration for the diagnostic itself,
and it answers the question the screen cannot.

## 6. What the census says regardless of any individual row

**Eight scripts out of 158 control on all three channels.** Whatever the per-finding verdicts turn
out to be, the project's default has been to pick one length variable and call it *length* — and two
independent lanes have now shown that choice can carry a verdict on its own. The standing correction
is prospective and already in force in the dispatch briefs: **run all channels, report each, take
the worst as the headline, and name the dominant one.**

Related: [[cross-finding-029-the-deciding-parameter]] · [[UNIT-DRIFT-DEFECT]] ·
[[TIED-OUTCOME-DEFECT]] §7.1 · [[h-new-3010-conditional-register]] · [[h-new-3040-modality-axis]]
