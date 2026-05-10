---
finding_id: Q028-F-07
title: TSM pair {Q 26, Q 28} Fisher-Rao distance — closest-TSM-pair test (vs Q 27 controls)
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q028-novel-findings-wave-H
alpha_bon: 0.01667
direction: ONE-SIDED-LOWER (FR(Q26,Q28) predicted to be closer than the FR(Q26,Q27) and FR(Q27,Q28) "TS-only" pairs)
status: PRE-REGISTERED
specialist: Q028-al-qasas-wave-H
verdict: TBD
notes: only TSM-vs-TSM pair in the corpus is Q 26 ↔ Q 28 (the only two surahs with identical *ṭ-s-m* muqaṭṭaʿāt). Q 27 has TS only (not TSM), making it the only TSM-cluster member without the *mīm*. The pre-registered prediction: among the three intra-cluster pairs, the TSM-pair {Q 26, Q 28} is the closest on FR root-distribution distance.
---

# Q028-F-07 — TSM-pair FR-distance: is {Q 26, Q 28} the closest intra-cluster pair?

## 1. Hypothesis

The muqaṭṭaʿāt-letter sequence `طسم` (Ṭāʾ-Sīn-Mīm) opens **two surahs** in the corpus: Q 26 al-Shuʿarāʾ and Q 28 al-Qaṣaṣ. Q 27 al-Naml opens with `طس` (Ṭāʾ-Sīn only — no mīm). The three surahs form a unique consecutive triple (positions 26, 27, 28) sharing the ṬS letter-prefix.

We pre-register the **letter-prefix-match prediction**: the TSM-pair (Q 26 ↔ Q 28) is closer on Fisher-Rao root-distribution distance than either TS-only pair (Q 26 ↔ Q 27 or Q 27 ↔ Q 28).

This is a falsifiable specialisation of the al-Biqāʿī muqaṭṭaʿāt-cohesion claim, restricted to the *exact-letter-match* axis (TSM vs TS). Prior tests (Q028-F-02; Wave-FALSIFIED §3.7) tested looser muqaṭṭaʿāt cohesion on cosine-of-vocabulary — and all 5 NULL'd. F-07 tests the **tightest** possible specialisation: only the **two surahs with identical** ṭ-s-m muqaṭṭaʿāt are compared.

**H1 (locked, one-sided lower)**: `FR(Q 26, Q 28) < min(FR(Q 26, Q 27), FR(Q 27, Q 28))`.

**H2 (locked)**: `FR(Q 26, Q 28)` is in the **top-5 closest pairs** (bottom-5 of FR distances) involving Q 28 across all 113 partners.

**H3 (locked, two-sided ranking)**: `FR(Q 26, Q 28)` percentile among all 6,441 corpus pairs is below the **50th percentile** (i.e., the pair is "closer than average").

## 2. Direction-locking

- H1 direction: `FR(Q26,Q28) < min(FR(Q26,Q27), FR(Q27,Q28))`. Equal or larger = FAIL.
- H2 direction: rank ≤ 5 among Q 28's 113 partners (smallest FR). Larger rank = FAIL.
- H3 direction: percentile < 50%. Higher = FAIL.

Locked **before** observation. The existing 00-overview-cited values (Q28↔Q26 = 0.954, Q28↔Q27 = 0.805) are referenced but the **TSM-pair ordering vs the TS-only pairs** is the locked load-bearing prediction.

**Important garden-of-forking-paths note**: the existing 00-overview.md lists Q 28's nearest content-neighbor as Q 7 al-Aʿrāf at FR = 0.762, and Q 28 ↔ Q 26 at FR = 0.954 (mid-range), and Q 28 ↔ Q 27 at FR = 0.805. Under those previously-observed values, H1 would FAIL. The pre-reg is locked here as a **direction-honest pre-registration**: we predict the letter-prefix-match should drive closeness; the empirical evidence ALREADY visible suggests the opposite. Publishing this NULL with full prominence per protocol §1.3 if confirmed.

(This pre-reg is intentionally constructed to ratify the direction-honest expectation that the TSM-pair SHOULD be closest if the al-Biqāʿī claim holds at its tightest specialisation. It is reasonable for this NULL to consolidate further the Wave-FALSIFIED §3.7 record.)

## 3. Method

- Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (existing FR-matrix metadata) — but the matrix is not stored as JSON. So we **re-derive** the full 114×114 FR matrix on the fly using the H-NEW-111 protocol:
  - Tokens: STEM roots from QAC (`data/morphology/quranic-corpus-morphology-0.4.txt`).
  - Vocabulary: top-500 roots by global frequency.
  - Per-surah Dirichlet-smoothed (α=0.5), L1-normalised root-distribution.
  - Distance: Fisher-Rao = `2·arccos(Σ √(p_i·p_j))`.
- Compute the three intra-cluster pairs and rank.
- Compute Q 28's full 113-neighbor list and identify the rank of Q 26.

## 4. Test family + Bonferroni

Family: Q028-novel-findings-wave-H, k = 3. α_Bonferroni = 0.05 / 3 = 0.01667. (H1 is a deterministic comparison, no permutation p needed; H2 and H3 are deterministic-rank tests; Bonferroni applies to the **family-of-3-claims** if all 3 are claimed jointly.)

## 5. Acceptance / failure

- **CONFIRMED** = H1 PASS AND H2 PASS AND H3 PASS.
- **DIRECTIONAL** = at least one passes.
- **NULL** = all three fail (publish with full prominence; consolidates Wave-FALSIFIED §3.7).

## 6. MW protections

- MW-1: L1-normalisation per H-NEW-111 standard.
- MW-2: full corpus-rank reported (Q 28's nearest-5 and farthest-5 neighbors listed in JSON output).
- MW-3: Note that K_TOP=500 / Dirichlet α=0.5 are pre-registered defaults (locked at H-NEW-111). Not re-tuned.
- MW-5: positive-control = the canonical TSM 3-surah letter-cluster as a single unit (which IS uniquely the only consecutive ṬS triple).
- MW-6: instrument-control = compare to a random within-Meccan pair of similar length-to-position. If H1 PASS, also report this control.

## 7. Coordination

This test SPECIALISES Q028-F-02 (which tested cosine-of-content-vocabulary across the TSM-3 cluster). F-07 restricts to the TSM-pair (no Q 27, since Q 27 lacks mīm), and uses **Fisher-Rao** (information-geodesic) rather than cosine. It is therefore a methodologically-distinct test, not a duplicate.

## 8. Honest expectation

Given the existing 00-overview.md citing FR(Q 28, Q 26) = 0.954 and FR(Q 28, Q 27) = 0.805, the locked direction (TSM-pair closest) is **expected to FAIL** at H1. The pre-reg is honest: if FAIL → NULL published; this consolidates Wave-FALSIFIED §3.7 on a 6th independent axis (Fisher-Rao on the tightest TSM specialisation).

If H1 PASS (against expectation) → DIRECTIONAL pending replication on other muqaṭṭaʿāt **exact-letter-match** clusters (ALR-5, HM-7).

## 9. Pre-reg SHA

To be SHA-256-hashed at file-lock time and embedded in the runner script.
