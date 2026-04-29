---
journal_entry: h-new-44-run-1
date: 2026-04-15
agent: h-new-44-specialist (specialist timed out at ~70min; integrator completed observed-only)
pre_reg: findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure-prereg.md
---

# Journal — H-NEW-44 run 1

## Task

Execute pre-registered 6-property combinatorial closure test on the 14 muqaṭṭaʿāt subsets plus letter-frequency Spearman correlation.

## Timeline

- 2026-04-15 ~5pm: h-new-44-specialist launched. Wrote script `scripts/h_new_44_muqattaat_closure.py` (516 lines, exact Fraction-based real rank, exhaustive combinations-based boolean_rank).
- Running 10,000 null samples: inner loop bottlenecked by boolean_rank (NP-hard, exponential in k). Specialist timed out at ~70 min having completed only ~500 null samples.
- Integrator dispatched parallel Bash runs of the same script from main session; 4 duplicate processes confirmed still running in ~50-90min range. Killed them.
- Integrator rewrote as `scripts/h_new_44_muqattaat_closure_fast.py` with bitmask representation. Still O(2^14) inner in poset_width + exhaustive boolean_rank → still too slow.
- Integrator wrote `scripts/h_new_44_observed_only.py` for the observed-family-only 6-property evaluation + secondary ρ. Completed in 2.2s (observed boolean_rank_within_F = 12).
- Identified the two exact Boolean decompositions and one multiset partition relation from the observed incidence matrix using fraction-field Gaussian elimination with augmented identity tracking.

## Observed facts

```json
{
  "antichain": false,
  "intersection_closed": false,
  "real_rank": 12,
  "gf2_rank": 12,
  "boolean_rank_within_F": 12,
  "union_size": 14,
  "poset_width": 9,
  "unique_subsets": 14,
  "spearman_rho_is_muq_vs_freq_rank": -0.5409
}
```

Kernel of incidence matrix has dim = 14 − 12 = 2. The two kernel vectors correspond to:
1. `ص + الم − المص = 0`  ↔  المص = ص ∪ الم
2. `طس + المر − الر − طسم = 0`  ↔  {ط,س} ⊎ {ا,ل,م,ر} = {ا,ل,ر} ⊎ {ط,س,م} as multisets

A third equivalent Boolean decomposition follows from kernel vector 1 under substitution: **المر = الم ∪ الر** (from the kernel vector طس - الر - طسم + المر = 0 rewritten with the الم ⊂ المر inclusion).

Actually let me re-verify: given the fraction-Gaussian output, the exact two kernel vectors are:
- v1: طس + المر − الر − طسم = 0
- v2: ص + الم − المص = 0

The المر = الم ∪ الر boolean fact is NOT directly a kernel vector — it follows from the fact that المر − الم − الر = {م,ر} − {م} − {ر} + ... No, let me recompute: 
- الم = {ا,ل,م} → vector (1,0,0,1,0,0,0,1,0,0,0,0,0,0) in letter-order ا-ح-ر-س-ص-ط-ع-ق-ك-ل-م-ن-ه-ي
- الر = {ا,ل,ر} → (1,0,1,0,0,0,0,0,0,1,0,0,0,0)
- الم + الر = (2,0,1,0,0,0,0,0,0,2,1,0,0,0)
- المر = {ا,ل,م,ر} → (1,0,1,0,0,0,0,0,0,1,1,0,0,0)
- الم + الر ≠ المر (first component is 2 vs 1)

So **المر = الم ∪ الر holds as a BOOLEAN equation but NOT as a linear-over-ℝ equation.** The boolean_rank = 12 is driven by both Boolean decompositions (1 and the المر-one), but the linear rank = 12 is driven by a different pair of relations. The real rank deficiency is from v1 and v2 above.

Separately, the boolean_rank_within_F result returned 12, indicating at least 2 boolean-redundant members. From the enumerative check:
- المص = ص ∪ الم (Boolean)
- المر = الم ∪ الر (Boolean)

These two boolean decompositions make 2 members redundant, giving boolean_rank ≤ 12.

So in summary: the OBSERVED family has:
- 2 Boolean decompositions: المص = ص ∪ الم, and المر = الم ∪ الر
- 2 linear dependencies over ℝ: (طس + المر = الر + طسم), and (ص + الم = المص)

The first ℝ-linear dep is orthogonal to the Boolean deps (involves a multiset-partition not a subset inclusion); the second ℝ-linear dep is just a 0-1 version of the first Boolean dep.

## Null (deferred)

The 10K cardinality-matched uniform null is not yet run. Compute complexity of boolean_rank is O(sum_k C(14,k) × 2^k) ≈ 56M ops per call, times 10K calls ≈ 5.6e11 ops. Requires a numpy-vectorized or C-level implementation. Queued as H-NEW-44.1.

## Deliverables

- findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure.md (OBSERVED-ALGEBRAIC-FACT)
- findings/phase-b-hypotheses/csv/h-new-44-observed.json
- scripts/h_new_44_observed_only.py
- scripts/h_new_44_muqattaat_closure_fast.py (pending H-NEW-44.1 vectorization)
- scripts/h_new_44_muqattaat_closure.py (original specialist output, kept for audit-trail)
- journal/h-new-44-run-1.md (this file)

## Honest caveats

- Primary 6-property vs uniform null not computed → no statistical verdict against pre-reg verdict table.
- Observed facts are deterministic and independently verifiable from the 14 canonical muqaṭṭaʿāt subsets; do not depend on tashkeel or abjad conventions.
- The cross-surah narrative interpretations (Q 7 ← Q 38 ⊎ Q 2-cluster etc.) are direct readings of Boolean decompositions, not speculative tafsīr overlay.
- No promotion to §1 or §3 of MASTER-FINDINGS-LEDGER permitted without H-NEW-44.1 null landing.
