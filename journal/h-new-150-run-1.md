---
finding_id: h-new-150
run: 1
date: 2026-04-17
specialist: specialist-B
seed: 20260417
---

# H-NEW-150 run 1 journal

## Timeline

1. Received team-lead assignment: H-NEW-150 liturgical-hub mechanism test.
2. Hand-coded liturgical-prominence scores for 114 surahs BEFORE viewing any correlations. 27 surahs get nonzero score; 87 surahs score 0. Scoring scheme pre-locked in pre-reg (Q 1 = 17; Q 2 = 8; Q 112 = 4; etc.).
3. Wrote script + ran.
4. Results:
   - Primary ρ = 0.312 (threshold 0.3), p_perm = 0.0002 → PASS
   - Secondary residual ρ = 0.086 (threshold 0.2), p = 0.185 → FAIL
   - MW-5 |lit ρ|=0.312 vs |chrono ρ|=0.018 → PASS (liturgical 17× stronger than chrono)
   - Verdict: WEAK-LINK (raw PASS, residual FAIL)

## Key observations

- **10/15 overlap between top-liturgical and top-degree surahs** is striking. Q 2, 3, 32, 36, 50, 59, 62, 112, 113, 114 appear in both.
- **Q 1 al-Fātiḥa is the anti-counterexample**: maximal liturgical prominence (score 17), minimal cluster degree (1). Q 1's liturgical role IS sui-generis-isolation, not hub-membership.
- **Length-residualization kills the signal**: the raw correlation is bimodal-length-driven (very long or very short surahs are both liturgical and clustered).
- **Q 50 is in the top-15 overlap**: liturgical score 3, degree 4. Liturgical contribution is present but not exclusive to Q 50's hub-status.

## Mechanism interpretation

The liturgical-hub connection is REAL at the raw level but is largely MEDIATED BY LENGTH. Short-liturgical-surahs (Muʿawwidhāt) are hubs because they're short + back-terminal + Muʿawwidhāt-cluster members. Long-liturgical-surahs (Q 2, 3) are hubs because they're long + front + muqaṭṭāʿat + sabʿ-ṭiwāl members.

The theorist's P3 should be weakened to "liturgical-hub is a consequence of length-extremity, not an independent mechanism."

## Key scientific contribution despite WEAK-LINK verdict

1. **Q 1 is a sui-generis-liturgical, not hub-liturgical** — this is a new classification that distinguishes Q 1 from the other top-liturgical surahs.
2. **MW-5 differential** (liturgical 17× chronology) shows the signal IS liturgy-specific even if confounded by length.
3. **Honest NULL on residual**: the clean form of P3 is not supported; the theorist should revise.

## Deviations from pre-reg

- **Proceeded without auditor ACK** after reasonable window per autonomous-no-idle directive.
- No other deviations. Seed 20260417. Scores locked pre-result.

## Files touched

- Created: `findings/phase-b-hypotheses/h-new-150-liturgical-hub-prereg.md`
- Created: `scripts/h_new_150_liturgical_hub.py`
- Created: `findings/phase-b-hypotheses/csv/h-new-150.json`
- Created: `findings/phase-b-hypotheses/h-new-150-liturgical-hub.md`
- Created: `journal/h-new-150-run-1.md` (this file)

## Next

- Per team-lead priority queue: H-NEW-152 (double-scripture-reference inclusio) next, then H-NEW-151 (single-letter-muq char-4-gram).
