# Journal — H-NEW-130b run 1

**Date**: 2026-04-17
**Specialist**: specialist-a (team quran-equation-solvers)
**Task**: T-G2 — char-4-gram cross-feature replication of H-NEW-130
**Seed**: 20260417
**Parent (primary test)**: H-NEW-130
**Parent (D-matrix source)**: H-NEW-111b

## Sequence

1. Received team-lead approval for H-NEW-130b replication path after H-NEW-130 PASS-DIRECTED (audit-036 CLEAN).
2. Inspected h-new-111b.json schema — same D_matrix_upper_triangular flat format as h-new-111.json.
3. Wrote pre-reg with EVERYTHING FROZEN from H-NEW-130 except feature space: |B|=54, K_top=15, threshold ≥12, Bonferroni-3. Novel secondary B cell (cross-feature overlap) replaces MW-5 as an explicit Bonferroni slot; MW-5 is now inherited from H-NEW-130 methodology.
4. DM'd auditor FYI; pre-reg SHA locked on disk.
5. Wrote script as thin wrapper reusing H-NEW-130's `build_boundary_set()`, `load_verse_counts()`, `hypergeom_sf()`, `secondary_A()` via import from `scripts/h_new_130_fisher_rao_residuals.py`. This ensures the boundary-set is provably identical (no copy-paste drift).
6. Executed deterministically seed 20260417.

## Results

### Primary: hypergeometric
- |M_char ∩ B| = 15 of 15 (identical to parent root result)
- Hypergeom p = 4.78 × 10⁻⁶
- Threshold ≥12 satisfied at k=15

### Primary robustness: permutation null
- 10K random 15-pair selections
- n_ge_observed=1, p = 0.00010
- Matches hypergeometric within MC noise (hypergeom tail at k=15 is 9.2e-7; 10K perms cannot resolve that, the 1/10001 hit is the MC floor)

### Secondary A: concentration
- T = +0.2566 (parent had +0.2443)
- p = 0.00010 (parent had 0.0001)
- Sign positive. PASS.

### Secondary B: cross-feature top-15 overlap
- 10 of 15 shared between root and char-4-gram top-15 sets
- Hypergeom(113, 15, 15) null expected overlap: 1.99
- p = 1.15 × 10⁻⁷
- PASS

### MW-5: discriminativeness
- Synthetic sort-by-length top-15 shares 0 of 15 with char-4-gram top-15
- Synthetic top-15 hits B at 0/15
- PASS (identical to parent's MW-5 result)

## Verdict

REPLICATION-CONFIRMED. H-NEW-130 promotes PASS-DIRECTED → CONFIRMED.

## Honest observations

1. **15/15 is the hypergeometric ceiling.** Both feature spaces hit it. We cannot distinguish "exactly this good" from "better than the instrument can measure." A top-25 follow-up would probe the shape of the decline.

2. **5-pair difference between feature spaces is structurally interpretable.** Char-4-gram picks up register-shifts in Q 21–35 that roots miss; roots pick up Q 1 (al-Fātiḥa isolation) and sabʿ al-ṭiwāl canonical end that char-4-grams miss. These are complementary views of the same underlying structural architecture.

3. **Period-axis dominance inherited from parent.** Under a drop-period+phase bracket, the primary falls (same as parent). The finding is real and pre-registered under full B; its mechanism is primarily Meccan/Medinan interleaving. Honest reading applies to both feature spaces.

4. **Shared-corpus limitation.** This is cross-feature replication, not cross-corpus. A stronger-still test would require another ancient Arabic religious corpus — out of scope here.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-130b-prereg.md`
- Script: `scripts/h_new_130b_fisher_rao_residuals_char4gram.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-130b.json`
- Findings: `findings/phase-b-hypotheses/h-new-130b-fisher-rao-residuals-char4gram.md`
- Parent primary: H-NEW-130 findings + JSON
- Parent D-matrix: H-NEW-111b JSON

## Team communication

- Pre-reg FYI DM to auditor (before execution).
- Will DM team-lead with PROMOTION-RECOMMENDATION: upgrade H-NEW-130 from PASS-DIRECTED to CONFIRMED.
- Will DM integrator asking them to update MASTER-LEDGER and cross-finding-011 addendum.
