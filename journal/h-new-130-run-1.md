# Journal — H-NEW-130 run 1

**Date**: 2026-04-17
**Specialist**: specialist-a (team quran-equation-solvers)
**Task**: T-G — Fisher-Rao mushaf-geodesic RESIDUALS analysis
**Seed**: 20260417
**Parent**: H-NEW-111 / cross-finding-011

## Sequence

1. **Orientation.** Read HANDOFF/04-DISCIPLINE.md, h-new-111 findings, cross-finding-011, h-new-111 pre-reg, team config, h-new-111.json structure.

2. **Pre-commit of boundary set B (NO D-matrix distances viewed at this stage).**
   Computed B deterministically from classical length-category canon
   (Ibn Nadīm / Zarkashī / Suyūṭī tradition), Meccan-Medinan `period` column,
   Nöldeke `noldeke_phase` column, and muqaṭṭāʿat canon (29 surahs, 9
   letter-sets). Result: |B| = 54 of 113 pairs = 47.8%.

3. **Specialist-judgment override.** Team-lead prompt specified threshold
   "≥60% vs null ~10%". The pre-commit revealed that the null expectation
   is 47.8% (not 10%), so the 60% threshold is too weak for α_bon = 0.0167.
   Under the correct hypergeometric null (N=113, K=54, n=15), α=0.0167
   corresponds to k ≥ 12 (80% threshold, hypergeom p = 0.00732).

4. **Amendment is a TIGHTENING** (80% > 60%), so self-verifies per the
   project's Bonferroni-asymmetry rule. Locked in pre-reg BEFORE computing
   distances.

5. **DM auditor** with transparency request. No response received before
   execution window; pre-reg path + SHA-256 commit ensures immutability
   even if auditor later requests tightening (which is still self-verifying).

6. **Script written**: `scripts/h_new_130_fisher_rao_residuals.py`.
   - Load D-matrix from h-new-111.json
   - Compute d_i = D[i, i+1] for i=1..113
   - Primary: hypergeometric test on top-15 ∩ B
   - Secondary A: B-vs-notB mean-distance permutation (10K perms, seed+1)
   - Secondary B: synthetic sort-by-verse-count ordering for MW-5 discriminativeness

7. **Execution.** Ran once, deterministic, seed 20260417.

## Results

- **Primary**: |M ∩ B| = **15 of 15**. Hypergeometric p = 4.78 × 10⁻⁶.
  Passes α_bon = 0.0167 by 3,493×.
- **Secondary A**: T = +0.2443 (B-pairs have larger mean Fisher-Rao distance).
  p_two_sided = 1.0 × 10⁻⁴. Passes α_bon.
- **Secondary B / MW-5**: synthetic top-15 shares 0 pairs with mushaf top-15,
  hits B at 0/15. Discriminative. MW-5 fires.

## Robustness bracket (descriptive, post-primary)

Dropping boundary-types reveals the period axis is dominant. Full B
passes at k=15/p=4.8e-6, period-only B passes at k=12/p=1.75e-7,
classical+muq-only B gets k=7/p=0.086 (N.S.). The finding is real and
pre-registered under full B; the mechanism is Meccan/Medinan axis
dominance. Reported honestly in findings file.

## Honest flags

- 15/15 is a ceiling result; no way to distinguish "exceptional alignment"
  from "100% ceiling on boundary-concentration". Future runs with
  K > 15 (e.g., top-25) would probe whether the alignment weakens
  smoothly or drops off sharply — queued as descriptive follow-up.
- The PASS depends on including Nöldeke-phase and period in B. A reader
  who considers Nöldeke reconstruction too speculative for inclusion
  can use the robustness bracket.
- Independent replication required before CONFIRMED. Queue H-NEW-130b
  using H-NEW-111b's char-4-gram D-matrix.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-130-prereg.md`
- Script: `scripts/h_new_130_fisher_rao_residuals.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-130.json`
- Findings: `findings/phase-b-hypotheses/h-new-130-fisher-rao-residuals.md`

## Time

Pre-reg + script + run + findings: single session, 2026-04-17.

## Team communication

- Pre-reg DM to auditor sent before execution.
- Report to team-lead pending (upon completion of this journal).
