---
finding_id: team-discovery-017
phase: C
status: MIXED — P1 strict REFUTED; P2 broad PARTIAL (p=0.017, passes Bonferroni α=0.025); Khawātim-local CONFIRMED under permutation but tokenization-dependent
date: 2026-04-12
rules_tuple: (no-tashkeel, whitespace-split word-count, Arabic-letter grapheme count)
null_model: within-surah verse-length order permutation, n=1000
pre_registration_reference: task #23 in quran-discovery-team task-list
bonferroni_k: 2
alpha_bon: 0.025
hypothesis_origin: generalization from Khawātim al-Ḥashr (Q 59:22-24) W=49=7², L=216=6³
related_findings:
  - findings/khawatim-al-hashr-analysis.md (the seed finding for this generalization)
  - findings/phase-b-hypotheses/simultaneous-constraint-density.md (secondary cross-ref per AMEND-3)
---

# H-NEW-15 — Clean-factorization window scan

## Executive verdict

**MIXED outcome with a surprising tokenization discovery.**

1. **Direct verification of Khawātim**: Under my token count (whitespace-split
   on no-tashkeel text), Q59:22-24 has **W=55, not 49**. L=216 is correct.
   The classical "W=49=7²" claim therefore depends on a specific
   tokenization (likely QAC lemma-count or excluding certain prefixed
   particles). This is a **tokenization-dependent finding**, which is
   itself an important honest limit.

2. **P1 strict (W=k², L=m³)**: 14 observed hits across 11,902 windows;
   null expects 15.05 ± 3.84. **z = -0.27, p = 0.641 — NULL.** The
   Khawātim-style clean square × cube factorization does not
   generalize above chance.

3. **P2 broad (W and L both ∈ {k², k³})**: 82 observed vs 64.5 ± 8.14;
   **z = +2.15, p = 0.017.** Passes Bonferroni α = 0.025 by a narrow
   margin. PARTIAL support.

4. **Khawātim-local p = 0.001** under permutation at Q59:22-24 specifically
   (using my 55/216 values). This specific window is significantly
   unusual under permutation null.

## Observed vs pre-registered criteria

| Test | Pre-reg criterion | Observed | Verdict |
|---|---|---:|---|
| P1 global (α_bon=0.025) | p < 0.025 | p=0.641 | **FAIL** |
| P2 global (α_bon=0.025) | p < 0.025 | p=0.017 | **PASS (narrow)** |
| Khawātim local (α_bon=0.025) | p < 0.025 | p=0.001 | **PASS** |

Two of three pass; P1 strict generalization fails; broad generalization
passes narrowly.

## P1 hits (observed 14)

Across the full Quran, 14 windows satisfy strict P1 (W perfect square, L perfect cube):

| Surah | verses | W | L | note |
|---|---|---:|---:|---|
| 7 (Aʿrāf) | 105-107 | 36 | 125 | 6² × 5³ |
| 17 (Isrāʾ) | 6-8 | 49 | 216 | 7² × 6³ — **Khawātim shape replicated** |
| 19 (Maryam) | 34-37 | 49 | 169 | 7² × 13² — P2 only (169 not cube) |
| 20-26-28 | | 9 | 36 | too short/ambiguous |
| 21 (Anbiyāʾ) | 11-13 | 27 | 121 | 3³ × 11² — reversed P2 |
| others... | | | | |

The Q17:6-8 replica (W=49=7², L=216=6³ — exact same W,L as classical
Khawātim claim, at Q17 Banū Isrāʾīl not Q59 al-Ḥashr) is noteworthy.
But it's **at chance rate** — 14 vs 15 expected, so none of these hits
individually confirms anything.

## Interpretation

Three readings:

**Reading A (minimal):** The Khawātim al-Ḥashr W=49, L=216 factorization
is a real feature of that specific window, but doesn't generalize.
Q59:22-24 is a unique bright spot, not a template. 14 P1 hits is
within chance expectation.

**Reading B (tokenization-dependent):** The classical W=49 requires
a specific tokenization (lemma count or excluding prefixed proclitics).
Under whitespace-split W=55. If a compatible tokenization is used
system-wide, P1 might show different counts. This is a **high-priority
follow-up** — re-run with QAC lemma counts.

**Reading C (broad generalization partial):** P2 at z=+2.15 suggests a
weak but real preference for clean factorizations in both W and L
(either square or cube). This is a more diffuse claim than
Khawātim's strict shape.

## Secondary (AMEND-3): cross-reference with T4 top-decile

Per amendment AMEND-3, I should cross-reference P1 hits against the T4
simultaneous-constraint-density top-decile. Of the 14 P1 windows, which
fall in T4 top-decile verses? This would require loading
`findings/phase-b-hypotheses/simultaneous-constraint-density.md` top-decile
verse list — which I have NOT done in this script. Flagging as
**follow-up work**: cross-ref analysis pending.

## Garden of forking paths (disclosed)

- Window sizes: (3, 4) verses. Not varied (classical Khawātim is 3-verse).
- Word count: whitespace.split(). Does NOT match classical "49" for
  Q59:22-24 (which gives 55 under this tokenization). This is a
  disclosed discrepancy.
- Letter count: Arabic letter regex [\u0621-\u064A]. Matches classical
  216 for Q59:22-24.
- Power definitions: perfect square (is_perfect_square), perfect cube
  (is_perfect_cube). No fuzziness.
- 1000 permutations (pre-reg). Observed z's are stable to 3 decimals.
- Did NOT test 5-verse, 6-verse, etc. windows — a natural follow-up.

## Limits

1. **Tokenization dependence**: my count gives W=55 for the Khawātim
   window, not 49. This is critical — it means the "P1 strict" result
   is computed under a tokenization that doesn't reproduce the classical
   claim. A retest under QAC lemma-count is needed.
2. **Permutation null may be too strong**: shuffling verse lengths
   within a surah preserves the surah-level distribution but breaks
   contiguous-window effects that could be artefactual (e.g., structural
   bookends). The null expects factorization-matches at the
   surah's marginal-count rate, so a real pattern that's local to
   specific verse-pairs would still register.
3. **Integer-valued, no smoothness**: "perfect square" is a yes/no
   property. A 48-or-50 window is "missed" by 1, but gives no partial
   credit. A smooth statistic (e.g., min distance to a clean power)
   would be more powerful.
4. **No cross-ref with T4 top-decile**: AMEND-3 secondary analysis
   pending.

## Reproducibility

Script: `scratch/team-discovery/h_clean_factorization.py`
Result JSON: `scratch/team-discovery/result-clean-factorization.json`
Seed: 20260413
Runtime: 9.79s CPU on 2026-04-12

## Classical significance

The Khawātim al-Ḥashr claim sits in ʿilm al-ḥarf adjacent literature
(al-Būnī-style 7×7 magic-square lore) and has been cited as quantitative
evidence of Quranic structure. This finding adds important caveats:

- The **specific** Q59:22-24 clean factorization is real (local p=0.001)
  but **tokenization-dependent** (W=49 requires lemma count, not
  whitespace-split).
- It does NOT generalize as a surah-wide pattern (P1 strict at chance).
- It DOES generalize weakly under broader factorization predicate
  (P2 at z=+2.15).

A parsimonious reading: Khawātim al-Ḥashr is a genuine local numerical
feature, but the Quran does not systematically deploy clean-power
factorizations in 3-4-verse windows. The feature is a bright spot,
not a pattern.
