# [[h-new-229-mirror-pair-structure-across-chronologies|H-NEW-229]] — Mirror-pair structure across chronologies (PRE-REGISTRATION)

**Finding ID**: [[h-new-229-mirror-pair-structure-across-chronologies|h-new-229]]
**Date**: 2026-04-17
**Seed**: 20260419
**Bonferroni k**: 1 (single discrete descriptive test)
**Specialist**: autonomous agent
**Parent**: [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] (±58 mirror at Q 49→50 / Q 56→57 under Nöldeke); [[h-new-158-mirror-pair-uniqueness|H-NEW-158]] (mirror-pair uniqueness, Nöldeke-specific). [[h-new-158-mirror-pair-uniqueness|H-NEW-158]] honest limit #1 explicitly calls out the Nöldeke-specificity as an open question.

## Hypothesis

The ±58 mushaf-pair chronology-reversal mirror at Q 49→50 and Q 56→57 identified under **Nöldeke 1860** is **either** (A) a Nöldeke-specific artifact (no mirror-pair structure appears at the top-2 magnitudes under Bell, Blachère, Egyptian), **or** (B) a robust architectural feature of the canonical mushaf (mirror-pair of equal |Δ| at top-2 magnitudes, or very near it, appears under multiple chronologies).

## Method (frozen BEFORE results viewed)

1. For each chronology C ∈ {Nöldeke, Bell, Blachère, Egyptian} compute, for each of the 113 consecutive mushaf pairs (i, i+1) where i=1..113:
   `Δ_C(i) = chrono_rank_C(i+1) − chrono_rank_C(i)`
2. Rank the 113 pairs by `|Δ_C|` descending.
3. Report the top-6 magnitudes per chronology.
4. **Primary descriptive test**: Are the top-2 |Δ_C| magnitudes EQUAL (tie at top-2) and OPPOSITE in sign under each chronology C?
   - Under Nöldeke, top-2 are |Δ|=108 (Q 110→111) and |Δ|=78 (Q 97→98); they are NOT tied. The pre-existing [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] "top-2 mirror" framing is imprecise — the actual mirror is at **ranks 5-6**, not ranks 1-2, and concerns only the |Δ|=58 pairs.
   - We therefore test a more faithful **primary**: under each chronology C, does the specific **{Q 49→50, Q 56→57}** mushaf-pair-pair exhibit:
     - (a) EQUAL |Δ_C| at both pairs (±0 tolerance), AND
     - (b) OPPOSITE signs (one negative, one positive), AND
     - (c) Magnitude |Δ_C| ≥ the median |Δ_C| across all 113 pairs (i.e., non-trivial, above-median magnitude)?
5. **Secondary descriptive diagnostic**: For each chronology, how many DISTINCT |Δ_C| values exhibit mirror structure (both signs present among pairs sharing that magnitude)? What is the LARGEST mirrored |Δ_C|? At which mushaf-pair(s)?
6. **Tertiary descriptive diagnostic**: Does ANY chronology have a mirror pair at |Δ| ≥ 50 involving the Q 49→50 and Q 56→57 boundaries specifically?

## Data sources

- **Nöldeke 1860**: `data/revelation-order.csv` column `noldeke_order`.
- **Egyptian 1924**: `data/revelation-order.csv` column `revelation_order` (Tanzil Egyptian Standard).
- **Bell 1937**: hard-coded dict from `scripts/h_new_212_alt_chronology_fisher_rao.py` (source: French Wikipedia "Sourate" chronology table). Surah 15 imputed rank 52; ties s81/s82 rank 15 broken by mushaf-order ascending (inherited pre-reg §5).
- **Blachère 1947**: hard-coded dict from `scripts/h_new_212_alt_chronology_fisher_rao.py`. Tie s80/s84 rank 24 broken by mushaf-order ascending (inherited pre-reg §5).

## Decision rule

- **Mirror IS a Nöldeke-artifact** iff the primary test passes for Nöldeke ONLY and fails for all three of {Egyptian, Bell, Blachère}.
- **Mirror IS a robust architectural feature** iff the primary test passes for Nöldeke AND ≥1 of {Egyptian, Bell, Blachère}.
- **Mirror is an architecturally universal feature** iff the primary test passes for ALL FOUR chronologies.

## Garden-of-forking-paths log

Choices committed BEFORE observing non-Nöldeke results:

1. **113 consecutive pairs, not 114**: Q 1→2 through Q 113→114. Standard across [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]/158.
2. **Signed Δ via rank subtraction**: `Δ(i) = rank(i+1) − rank(i)`. A negative Δ means the next surah is chronologically EARLIER.
3. **Ties in raw chrono-rank**: inherited from [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] tie-breaking rule (mushaf-order secondary ascending). This does change Bell rank for s81/s82 and Blachère rank for s80/s84 but does not affect Q 49→50 or Q 56→57 directly.
4. **"Mirror" definition**: strict — equal |Δ| and opposite signs, 0 tolerance. No "near-mirror" generous allowance.
5. **Primary is on THE SPECIFIC {Q 49→50, Q 56→57} pair**, not "top-2 mirror anywhere". This is the correction [[h-new-158-mirror-pair-uniqueness|H-NEW-158]] already flagged.
6. **Non-trivial magnitude threshold**: ≥ median |Δ_C| (across 113 pairs). With 113 pairs, median is a well-defined sample-statistic per chronology. This prevents trivial "mirror at |Δ|=1" false positives.
7. **Bonferroni k=1**: single descriptive tuple, 4 cells are reported but the decision rule is a 4-way cell pattern not 4 independent tests.
8. **Seed 20260419**: no randomization used; seed retained for reproducibility of any follow-up shuffling (not in this test).
9. **No permutation null here**: the question is structural-descriptive (does pattern hold under alt chronology?), not inferential-significance. If any cell shows mirror pattern, a permutation p-value would be a follow-up, not gating for this pre-reg.

## Outputs

- `findings/phase-b-hypotheses/csv/h-new-229.json` — full numerical result.
- `findings/phase-b-hypotheses/h-new-229-mirror-pair-structure-across-chronologies.md` — writeup.
- `journal/h-new-229-run-1.md` — run log.
- `scripts/h_new_229_mirror_across_chronologies.py` — reproducible script.

## Pre-reg integrity

SHA-256 of this pre-reg file emitted to stderr by the script and stored in the output JSON.
