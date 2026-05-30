---
finding_id: H-NEW-2460
title: The minimal-surah structural class + the {Q103,Q108} rā'-twin
file_type: prereg
date_locked: 2026-05-30
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-COMPUTATION
rules_tuple: "(no-tashkeel, orthographic-token, graphemes/letters, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# H-NEW-2460 — Pre-Registration: the minimal-surah structural class and the {Q103,Q108} rā'-twin

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/h-new-2460.py` and verified at runtime (fail-fast on mismatch).

## Motivation

The corpus has a small tail of very short surahs. Sorted by Hafs-Kūfan verse-count, the shortest
are: three 3-verse surahs {Q103 al-ʿAṣr, Q108 al-Kawthar, Q110 al-Naṣr}; two 4-verse surahs
{Q106 Quraysh, Q112 al-Ikhlāṣ}; four 5-verse surahs {Q97 al-Qadr, Q105 al-Fīl, Q111 al-Masad,
Q113 al-Falaq}; and two 6-verse surahs {Q109 al-Kāfirūn, Q114 al-Nās}. (Q1 al-Fātiḥa is 7 verses
and is excluded from the ≤6 frame.)

This finding builds a **generator** over that class — a single pass that catalogs, for every
member, its (a) verse-count tier, (b) rhyme class (perfect-monorhyme final letter or non-mono),
(c) Fisher-Rao mutual distances, and (d) opening/structural shape — and then promotes the
candidate {Q103,Q108} minimal-surah "rā'-twin" (queued as Q103-F-03 in MASTER-FINDINGS-LEDGER
§10.113, Arm A of Q103-F-01) to a direction-locked corpus-wide test.

The pre-existing on-disk anchors (re-read at runtime, not assumed):
1. `h-new-111.json` — 114×114 Fisher-Rao distance matrix on QAC stem-roots (1-indexed).
2. `quran-text/quran-no-tashkeel.json` — verse text (default rules-tuple); verse-finals for rhyme.
3. `h-new-2210.json` — qasam (oath) catalog; only Q103 in the minimal class is a qasam surah.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes/letters, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)`.

Verse-finals: last Arabic-letter of the last whitespace-token of each verse (the strict
last-grapheme rāwī proxy), Arabic-letter set
{ابتثجحخدذرزسشصضطظعغفقكلمنهوياءأإآؤئىة}, pause/sajda marks stripped. Perfect monorhyme = all
verse-finals identical. FR distances from `h-new-111.json` (1-indexed). Verse-counts from the
`total_verses` field of `quran-text/quran-no-tashkeel.json`.

**Class definition (PRE-COMMITTED):**
- **Primary class** = surahs with `total_verses ≤ 4`: {Q103, Q108, Q110, Q106, Q112}.
- **Extended class (reported descriptively)** = `total_verses ≤ 6`: the primary class plus
  {Q97, Q105, Q111, Q113, Q109, Q114}. The ≤6 set has 11 members.
- The **3-verse sub-class** = exactly {Q103, Q108, Q110} (the locked-direction test arena).

---

## Arm A — the {Q103,Q108} rā'-twin within the 3-verse sub-class (DIRECTION-LOCKED)

**Hypothesis A (pre-committed, direction-locked):** Among the three 3-verse surahs
{Q103, Q108, Q110}, the pair {Q103, Q108} is **(i) rhyme-class-matched** (both perfect
rā'-monorhymes, Q110 is not) **AND (ii) FR-closer to each other than either is to the third
member Q110** — i.e. d(Q103,Q108) is the MINIMUM edge of the 3-verse FR triangle.

- **A-H1 (deterministic):** of {Q103, Q108, Q110}, exactly {Q103, Q108} have all verse-finals = ر
  (rā'); Q110 is non-mono.
- **A-H2 (direction-locked):** d(Q103,Q108) < d(Q103,Q110) AND d(Q103,Q108) < d(Q108,Q110)
  — the rhyme-matched pair is also the shortest edge of the 3-node triangle.

**A small-N null (honest, pre-committed):** under random labeling of which of the 3 triangle edges
is smallest, P(a named edge is the minimum) = 1/3 ≈ 0.333. With a 3-member class the locked
direction A-H2 carries at MOST this exact-combinatorial significance (p = 1/3 for the edge being
minimal). This is **underpowered by construction**; A-H2 is therefore reported as an EXACT
corpus-rarity statement (the edge IS or IS NOT the triangle minimum), and we explicitly DECLINE to
claim a small permutation p-value for a 3-node class. The substantive content is the conjunction
A-H1 ∧ A-H2: rhyme-match AND minimal-edge co-occur on the SAME pair.

**A success criterion:** A-H1 ∧ A-H2 → Arm A CONFIRMED (exact corpus fact; power-limited).
**A failure / pre-commit violation:** A-H2 reversed (d(103,108) is NOT the triangle minimum)
→ published NULL with full prominence.

## Arm B — rhyme-class ⊥ FR-proximity (the honest control, DIRECTION-LOCKED)

**Hypothesis B (pre-committed, direction-locked):** rā'-monorhyme membership does NOT by itself
imply FR-proximity. The corpus has exactly **four** strict-final rā'-monorhymes
{Q54 al-Qamar, Q97 al-Qadr, Q103, Q108} (re-derived at runtime). Among the **six** pairs of these
four, the {Q103,Q108} pair is FR-closest, and the long narrative member Q54 al-Qamar is FAR (FR)
from the three short members — demonstrating that rhyme-class is NOT an FR cluster, so the
{103,108} closeness is NOT a mere artifact of shared rhyme.

- **B-H1 (deterministic):** the corpus strict-final rā'-monorhyme set is exactly {54, 97, 103, 108}.
- **B-H2 (direction-locked):** d(Q103,Q108) = min over the six rā'-monorhyme pairs; and
  mean FR(Q54, ·) over {97,103,108} > 0.70 (Q54 is FR-distant from the short rā'-monorhymes),
  while d(103,108) < 0.30. Direction lock: rhyme-mates are NOT generally FR-close.

**B success criterion:** B-H1 ∧ B-H2 → Arm B CONFIRMED (rhyme ⊥ FR; {103,108} closeness is real).
**B failure:** B-H2 reversed → NULL.

## Arm C — minimal-class profile + the FR-centroid extreme (DESCRIPTIVE + DIRECTION-LOCKED)

**Hypothesis C (pre-committed, direction-locked):** the minimal-surah class is, as a body,
FR-CENTRAL — its members sit at the corpus's low end of mean-pairwise-FR (low root-distribution
distinctiveness), reflecting the short surahs' reliance on the corpus's common high-frequency
root vocabulary; and the within-class mean pairwise FR is far below the corpus-wide pairwise mean.

- **C-H1 (descriptive):** catalog, for all 11 ≤6-verse members: verse-tier, rhyme-class
  (perfect-monorhyme letter / non-mono), opening/structural shape, per-surah mean-FR-to-all-113,
  and the full 11×11 within-class FR matrix.
- **C-H2 (direction-locked):** the within-class (≤6) mean pairwise FR is LESS than the
  corpus-wide mean pairwise FR; AND a MAJORITY (≥6/11) of the minimal-class members rank in the
  corpus LOWER HALF (rank ≤ 57/114) by per-surah mean FR (i.e. they are FR-central, not
  FR-peripheral). Direction lock: minimal surahs are FR-central, not FR-distant.

**C success criterion:** C-H1 produced ∧ C-H2 both clauses hold → Arm C CONFIRMED.
**C failure / pre-commit violation:** C-H2 reversed (minimal class is FR-peripheral) → NULL.

---

## Null distributions & power

- **Arm A:** 3-node triangle; exact-combinatorial null P(min-edge = named edge) = 1/3. Honestly
  underpowered — reported as exact corpus fact, NOT as a significant permutation result.
- **Arm B:** deterministic (the rā'-monorhyme set and its 6 pairwise FR values are corpus facts).
- **Arm C-H2 (replication / robustness):** to give Arm C an inferential spine that the
  small 3-node class cannot, we add a corpus-wide permutation control: draw 10,000 random
  size-11 surah subsets (seed 20260509) and record their mean pairwise FR; the observed
  minimal-class mean pairwise FR is compared to this null (one-sided: minimal-class mean < random
  subset mean). This is MW-2 corpus-prior + MW-6 instrument-control: it tests whether the
  minimal class is MORE internally cohesive (lower within-class FR) than a random 11-surah set.
  p_perm = (#{null ≤ obs}+1)/(N+1). Direction-locked: obs < null mean.

## Bonferroni

Permutation cells: exactly **k = 1** (the Arm C-H2 random-subset cohesion test). α_corrected =
0.05 / 1 = 0.05. Arms A and B and the descriptive half of C are deterministic corpus facts and
do not consume α. The Arm A 1/3 exact null is reported as-is (not multiplicity-corrected; it is a
single exact statement and is, by design, above any α threshold — power-limited, not significant).

## MW protections

- **MW-1 (instrument-prior):** class definition (≤4 primary, ≤6 extended), rā'-monorhyme rule,
  FR-rank, triangle-min-edge, and the FR-central direction all fixed here before any run.
- **MW-2 (corpus-prior):** Arm C-H2 uses 10,000 random size-11 subset draws.
- **MW-3 (alternative-models):** two FR readings reported — within-class mean (cohesion) and
  per-surah mean-to-all-113 (centrality); Arm B reports the rhyme-class control.
- **MW-5 (replication):** Arms A, B, C-H1 are deterministic and fully replicable from the
  no-tashkeel JSON + h-new-111.json; C-H2 seed-locked at 20260509.
- **MW-6 (instrument-control):** Arm B is the rhyme⊥FR control (Q54 al-Qamar); C-H2's random
  size-11 subset is the content-blind cohesion control.
- **MW-7 (post-hoc cap):** the {103,108} twin was noticed during Q103's close reading and queued
  (Q103-F-03) BEFORE this run; the single permutation cell respects α=0.05. Arm A is honestly
  flagged as power-limited (1/3 floor) and is NOT inflated to a significance claim.

## Verdict mapping

| Arm | Pass condition | Verdict label |
|:--|:--|:--|
| A | A-H1 ∧ A-H2 (min-edge = {103,108}) | CONFIRMED (exact, power-limited 1/3 floor) |
| A | A-H2 reversed | NULL (pre-commit violation, full prominence) |
| B | B-H1 ∧ B-H2 | CONFIRMED (rhyme ⊥ FR) |
| B | B-H2 reversed | NULL |
| C | C-H1 produced ∧ C-H2 both clauses + p<0.05 | CONFIRMED |
| C | C-H1 ∧ C-H2 directions hold but p≥0.05 | DIRECTIONAL |
| C | C-H2 reversed | NULL (pre-commit violation) |

Final H-NEW-2460 verdict = honest combination of Arms A, B, C, reported with equal NULL
prominence and an explicit small-N power note.

*Locked 2026-05-30. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
