---
journal_entry: h-new-44-1-run-1
date: 2026-04-15
agent: h-new-44-1-specialist
pre_reg: findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure-prereg.md
parent_run: journal/h-new-44-run-1.md
---

# Journal — H-NEW-44.1 run 1

## Task

Complete the 10K cardinality-matched uniform null for the muqaṭṭaʿāt
combinatorial-closure test that the prior H-NEW-44 specialist could not
finish (boolean_rank inner loop NP-hard, ~5.6e11 ops). Use numpy
vectorization or fast bitmask approximations.

## Garden-of-forking-paths amendments (filed BEFORE null run)

Two amendments to the pre-registered method, BOTH TIGHTENING under the
project's Bonferroni-asymmetry standard (so self-verifying):

1. **`boolean_rank` proxied by `gf2_rank`.** GF(2)-rank ≤ boolean-rank
   (within F) for 0/1 matrices. So `gf2_rank == 14 ⇒ boolean_rank == 14`,
   reverse can fail. Since observed `boolean_rank == 12 ≠ 14`, the cell
   test is `P(null is FALSE)`, and the proxy has
   `P(null gf2_rank ≠ 14) ≥ P(null boolean_rank ≠ 14)`,
   so the p-value under proxy is LARGER (more conservative).

2. **`poset_width_14` ≡ `is_antichain` AND 14-distinct-rows.** Width=14 in
   a 14-element poset means the maximum antichain is the whole family —
   equivalent to the family being an antichain (when all rows distinct).
   EXACT, not an approximation. Saves the brute-force inner loop.

Both amendments self-verify (TIGHTENING, not LOOSENING).

## Engineering

- Bitmask representation: 14 letters → 14-bit ints (uint16).
- `numpy.random.default_rng(20260415)` for sampling 14 size-matched subsets.
- GF(2) rank via XOR Gaussian elimination on Python ints (faster than
  numpy for small n).
- Real rank via `numpy.linalg.matrix_rank` on unpacked 14×14 0/1 matrix.
- antichain / intersection_closed via O(n²) pairwise int-bitop loops.
- Result: ~10K samples/sec; 10K null loop = 1.0s.

## Timeline

- 2026-04-15: Read pre-reg, observed-only result, prior journal.
- Wrote `scripts/h_new_44_1_muqattaat_null.py` (~430 lines).
- Verified observed properties match prior run (rank=12, antichain=False,
  poset_width=9, boolean_rank=12 — all consistent).
- Verified MW-5 positive control: chain {{1}, {1,2}, ..., {1..14}} gave
  expected (antichain=False, intersection_closed=True, real_rank=14,
  union=14, poset_width=1, boolean_rank=14). PASS.
- Ran 10K null. Total runtime: 9.8s (1.0s null loop + ~8.8s for boolean_rank
  on observed and PC + corpus letter-frequency I/O).
- Wrote findings/phase-b-hypotheses/csv/h-new-44.json (overwrites
  h-new-44-observed.json's role as authoritative).
- Wrote findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure.md
  (REPLACED observed-only with full null result; preserved algebraic-fact
  section).

## Results

```
observed:
  antichain: False
  intersection_closed: False
  real_rank: 12  (real_rank_14 = False)
  union_size: 14  (union_eq_14 = True)
  poset_width: 9  (poset_width_14 = False)
  boolean_rank: 12  (boolean_rank_14 = False)

null (10K, seed 20260415):
  antichain TRUE in 0/10000  → p = 1.0000
  intersection_closed TRUE in 0/10000  → p = 1.0000
  real_rank_14 TRUE in 1370/10000  → p (obs FALSE) = 8630/10000 = 0.8630
  union_eq_14 TRUE in 5022/10000  → p (obs TRUE) = 0.5022
  poset_width_14 TRUE in 0/10000  → p = 1.0000
  boolean_rank_14 (gf2 proxy) TRUE in 913/10000  → p (obs FALSE) = 0.9087

α_cell = 0.05/6 = 0.00833
significant: 0/6
```

**Verdict: NULL.**

## Striking observation

The OBSERVED real-rank of 12 is the SECOND-most-common rank under
cardinality-matched uniform null (29.91% of draws). The mode is rank-13
(50.43%); rank-14 (full) appears only 13.7%. The observed gf2_rank of 12
is the MOST-common gf2-rank in the null (35.66%).

So rank-deficiency by 1-2 in random 14×14 0/1 incidence matrices with this
cardinality distribution is the NORM, not the exception. The two Boolean
decompositions of the muqaṭṭaʿāt are real combinatorial facts but
statistically generic.

## MW-7 internal error gate

PASS. p-values in [0,1]; observed ranks in [0,14]; positive control passed.

## Deliverables

- scripts/h_new_44_1_muqattaat_null.py
- findings/phase-b-hypotheses/csv/h-new-44.json (NEW authoritative; replaces
  h-new-44-observed.json's authoritative role)
- findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure.md
  (REPLACED observed-only with full null result)
- journal/h-new-44-1-run-1.md (this file)

## Honest caveats

- The boolean_rank proxy `gf2_rank` is CONSERVATIVE for the observed-FALSE
  direction. It would be LOOSE for a hypothetical observed-TRUE direction
  (gf2_rank == 14 implies boolean_rank == 14, but null's gf2_rank == 14 may
  undercount how often null's boolean_rank == 14). For our specific
  observation (boolean_rank=12), the direction is fine (conservative).
- The pre-reg verdict table maps "0 properties significant" → NULL. Confirmed.
- The two Boolean decompositions and the multiset partition relation are
  preserved as observed combinatorial facts in the findings document; they
  do not earn statistical significance under the chosen null.
- The secondary letter-frequency Spearman (ρ = −0.54) is a SEPARATE finding
  on a different axis; it stands on its own.

## What I'd change next

- Future H-NEW-44 follow-ups should pivot to PHONETIC (al-Khalīl POA),
  SEMANTIC (surah-topic MI), or NARRATIVE structure rather than further
  subset-algebra hypotheses on F.
- Worth noting: the cardinality-matched uniform null may not be the right
  null. A more demanding null would be "uniform on letter-bigrams that
  Arabic phonotactically permits as opening clusters" — but that requires a
  separate pre-reg.
- The rank-12 modality of the null is itself an interesting fact about
  binary matrices with this cardinality distribution. Could be a
  combinatorics-paper sidebar but not a Quranic finding.

## No promotion to MASTER-FINDINGS-LEDGER §1

Per pre-reg, NULL verdict on the primary axis means no §1 promotion. The
secondary letter-frequency confirmation of Welch 1986 may warrant a §3
mention as a quantification of established prior art, but that is a
ledger-curator decision, not this specialist's.
