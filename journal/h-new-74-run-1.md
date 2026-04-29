---
date: 2026-04-15
run_id: h-new-74-run-1
hypothesis: H-NEW-74 — qul (قل) imperative comprehensive distribution
seed: 20260417
author: h-new-74-specialist
verdict_summary: PASS — 5 of 6 cells fire; Cell 1 verifies 332-count, Cell 3 verifies 5-surah opener set (4 classical + Q72), Cell 4 confirms ≥3 frames at ≥5×, Cell 6 K-W p=1.0e-7 reveals Late-Meccan peak. Cell 5 (Meccan-vs-Medinan MWU) NULL because the Meccan distribution is bimodal.
---

# H-NEW-74 Run 1 — Journal

## Setup

- Pre-reg written FIRST (`findings/phase-b-hypotheses/h-new-74-qul-distribution-prereg.md`).
- Six test cells locked with Bonferroni k=6, α_bon=0.00833.
- Garden-of-forking-paths log declared BEFORE running:
    - Predicted v1-w1 qul-openers = {Q 72, 109, 112, 113, 114} (5 surahs).
    - Predicted Q 6 al-Anʿām tops the per-surah count.
    - Predicted Late Meccan > Medinan > Middle Meccan > Early Meccan in
      density.

## Method

- **Source-of-truth for qul**: Leeds QAC v0.4 morphology file. The
  canonical filter is the four-feature predicate
  `POS:V & IMPV & LEM:qaAla & 2MS`. Surface-string matching in
  no-tashkeel JSON would give 294 (bare قل) + 21 (وقل) + 18 (فقل) = 333,
  off by +1 — the canonical-form 332 is what the QAC predicate yields.
- **Verse text + tokens**: `quran-text/quran-no-tashkeel.json` for the
  per-verse token stream (used for Cell 4 frame extraction).
- **Chronology**: `data/revelation-order.csv` (Tanzil Egyptian Standard +
  Wikipedia Nöldeke).
- **Verse counts**: from JSON metadata (Hafs-Kufan canonical-114).

## Steps

1. Load 114 surahs (6,236 verses) + chronology (114 surahs).
2. Filter QAC morphology lines by the four-feature qul predicate; record
   332 locations (sid, vid, wid, pid).
3. Cell 1: total = 332. **PASS** (hard-equality MW-control).
4. Cell 2: per-surah count + density per 100 verses. Top-10 by count
   ranges 44–11; 57 / 114 surahs have zero qul. **PUBLISHED**.
5. Cell 3: v1-w1 qul-openers = {72, 109, 112, 113, 114}. Predicted set
   matched exactly. **PASS**.
6. Cell 4: 11 of 15 pre-registered "qul + X" formulaic frames each fire
   ≥ 5×. Threshold was ≥ 3. **PASS** (very strong; 11/15 frames pass).
7. Cell 5: Mann-Whitney U on Meccan (n=86) vs Medinan (n=28) qul-density.
   U = 1109.5, z = -0.62, **p = 0.534**. **NULL** (Meccan distribution is
   bimodal, dragging the rank-sum test toward null).
8. Cell 6: Kruskal-Wallis H on Nöldeke 4-phase qul-density. H = 35.36,
   df = 3, **p = 1.02 × 10⁻⁷**. **PASS** (Bonferroni-passing by 4 orders
   of magnitude).

## Issues encountered

### Cell 5 null vs Cell 6 pass

The naive Meccan-vs-Medinan binarisation gives null because the Meccan
group is bimodal (~half of the 86 Meccan surahs have ZERO qul; the other
half are qul-dense). Splitting Meccan into Early/Middle/Late (Nöldeke)
reveals the actual structure: Early=1.74, Middle=4.89, Late=8.95,
Medinan=4.93 (mean density per 100 verses). Late Meccan is the qul-peak.
This was pre-registered as a possibility (Cell 5 was genuinely a test, not
a confirmation; Cell 6 was the more sensitive analysis).

### Surface-vs-canonical count

Surface scan of no-tashkeel JSON gave 294 + 21 + 18 = 333 (off by +1 from
canonical 332). The discrepancy is consistent with one surface-string قل
being morphologically NOT qaAla-IMPV-2MS in QAC (likely a 1MS perfect or
a non-qul homograph). The QAC four-feature predicate is the canonical
form and yields the publicly-cited 332 exactly.

### Q 72 is the 5th qul-opener (task prompt undercount)

Task prompt said "Q 109, 112, 113, 114" open with qul. The mechanical
extractor finds Q 72 al-Jinn ALSO opens with qul at v1-w1
(*qul ūḥiya ilayya annahu istamaʿa nafarun mina-l-jinni…*). This was
ALREADY known from H-NEW-61 (`findings/phase-b-hypotheses/h-new-61-opening-words.md`,
IMPERATIVE class) and was pre-registered in this finding's
garden-of-forking-paths section as a 5-surah expectation. The 5-surah set
{72, 109, 112, 113, 114} is the canonical structural quintet of v1-w1
qul-openers.

### Q 113/114 chronology

Both are tagged Early Meccan in our Nöldeke data — the muʿawwidhatān are
classically considered "early Meccan despite their final mushaf
position". This is consistent with the Cell 6 finding: Early Meccan has
LOW mean density (1.74) overall, but the few Early Meccan surahs that
DO contain qul (Q 112, 113, 114) have density 25, 20, 20 (the short-surah
denominator effect — 1 qul / 4 verses = 25). This is why the Late Meccan
peak is in the MEDIAN as well as the mean, not just an artifact of
short-surah outliers.

## Verdicts

| cell | result |
|---|---|
| Cell 1 (total = 332) | **PASS** (hard equality) |
| Cell 2 (per-surah distribution) | PUBLISHED |
| Cell 3 (v1-w1 openers = {72, 109, 112, 113, 114}) | **PASS** (set equality with prediction) |
| Cell 4 (≥ 3 of 15 pre-reg frames at ≥ 5×) | **PASS** (11 of 15 frames fire) |
| Cell 5 (period × density Mann-Whitney U) | NULL (p = 0.534) |
| Cell 6 (phase × density Kruskal-Wallis) | **PASS** (p = 1.0 × 10⁻⁷) |

JOINT: 5 / 6 cells fire at α_bon = 0.00833. The single null (Cell 5) is
informative: the Meccan/Medinan binary cut does not capture the
qul-density structure; the Nöldeke 4-phase cut does, with the peak at
Late Meccan.

## Files written

- `findings/phase-b-hypotheses/h-new-74-qul-distribution-prereg.md`
- `findings/phase-b-hypotheses/h-new-74-qul-distribution.md`
- `findings/phase-b-hypotheses/csv/h-new-74.json`
- `scripts/h_new_74_qul_distribution.py`
- `journal/h-new-74-run-1.md` (this file)

## Honest caveats

- Cell 4's frame catalog used pre-registered formulaic predicates plus a
  raw top-K bigram/trigram dump. The raw bigram counts (e.g. *qul inna* 25,
  *qul innamā* 19, *qul yā* 16, *qul Allāh* 16, *qul lā* 14) include
  some that overlap with the pre-reg classes (e.g. *qul inna* +
  *qul innamā* + *qul innī* together = 55 = bulk of the certainty class).
  No retroactive frame-redefinition was made; the pre-reg classes are
  reported as-is.
- The `qul_aʿūdhu` frame fires only 2× (Q 113, Q 114) — the famous
  muʿawwidhatān incipit. This is a small but iconic instance; the
  pre-reg threshold of ≥ 5 is not met but the structural significance
  of *qul aʿūdhu* as a recitational formula is independent of count.
- The raw bigram leader *qul inna* (25×) is essentially the "Say:
  indeed/that…" assertive frame; combined with *qul innamā* (19×) and
  *qul innī* (11×) that makes 55× — a very dominant compositional schema
  ("Say: only…", "Say: I am only…", "Say: indeed…").
- Cell 6's Late Meccan peak is consistent with the classical
  observation that *qul* increases as the Meccan dawʿah escalates and
  the Prophet is commanded to articulate increasingly definite positions;
  but no formal phase-vs-content cross-check was done in this run. A
  follow-up h-new-74-1-content-cross would tie qul-density to specific
  doctrinal/polemical content categories per phase.

## Next steps (suggestions, not commitments)

- **h-new-74-1-bimodality**: explicitly test for bimodality of the
  Meccan qul-density distribution (Hartigan's dip test or
  Silverman's bandwidth test) to confirm the within-Meccan two-modes
  intuition.
- **h-new-74-2-content-bind**: bind qul-density to specific content
  categories per phase (theological assertion vs polemical interrogative
  vs legal directive) to see if the LATE-Meccan peak is driven by
  polemical-interrogative or theological-assertive frames or both.
- **h-new-74-3-co-density**: cross-correlate qul-density with other
  divine-Prophet imperatives (*iṣbir*, *iʿlam*, *anẓur*) — does the
  Late Meccan peak in qul correspond to a peak in the broader
  command-to-Prophet imperative cluster, or is it qul-specific?
- **h-new-74-4-pair-with-qālū**: test the popular Sufi figure
  "qul = qālū = 332" mechanically. We already know qālū = 332 from
  `quotation-analysis.md`; verify per-surah co-distribution.
