---
finding_id: h-new-131
run: 1
date: 2026-04-17
specialist: specialist-B
seed: 20260417
---

# H-NEW-131 run 1 journal

## Timeline

1. Received T-H assignment from team-lead: investigate whether Q 108's MST-degree 24 (per H-NEW-134) is mechanical smoothing artifact or structural.
2. Read parent H-NEW-134 descriptive analysis at `findings/phase-b-hypotheses/h-new-134-mst-analysis.md` and parent method at `scripts/h_new_111_fisher_rao_mushaf.py`.
3. Checked `csv/h-new-111.json` for D-matrix structure (6,441 upper-triangular entries on 114 nodes = correct).
4. Drafted pre-reg with Bonferroni k=3 initially covering {Cell A α=0.01, Cell B JS, Cell B TV}. Direction locked BEFORE execution per PRE-REG-STANDARD-04.
5. DM'd auditor for pre-reg review.
6. While waiting, wrote script, syntax-checked, and ran a Cell-C dry-run to confirm QAC pipeline reads Q 108 correctly (7 STEM root tokens, distinct list matches expected text al-Kawthar 108:1-3).
7. Auditor (audit-036) reviewed pre-reg: CLEAN-WITH-ONE-RECOMMENDED-AMENDMENT. Recommended amendment: relabel Cell A as descriptive-robustness (not inferential Bonferroni slot), reducing effective Bonferroni k from 3 to 2. This is a TIGHTENING amendment per `feedback_bonferroni_tightening_vs_loosening` — self-verifying.
8. Applied amendment to pre-reg YAML and Bonferroni-accounting section and to script docstring + JSON output `bonferroni` field. ACK'd auditor.
9. Executed script. Results:
   - Sanity replication of H-NEW-134 MST: Q 108 deg 24 (exact match)
   - Cell A (α=0.01, FR): Q 108 deg 11 → WEAKLY-SURVIVE
   - Cell B cross-metric (α=0.5): FR=24, Hellinger=24 (≡ FR by rank-monotonicity, verified), JS=24, TV=6 → PASS (2/3 ≥ 15)
   - Cell C: Q 108 root-barbell: rbb (rank 4, 980 corpus), kvr (64, 167), Slw (115, 99), ETw (481, 14), nHr (hapax). Top-50 mass fraction 0.1024 smoothed, 0.2500 unsmoothed.
10. Wrote findings file `findings/phase-b-hypotheses/h-new-131-q108-supernode.md`.
11. This journal.
12. About to DM team-lead with results.

## Observations / notes

- The Hellinger=FR consistency check returned `True` exactly (MST edges identical). This confirms the pipeline is correct and rules out metric-implementation bugs. It was a good hygiene choice to include this as a belt-and-braces consistency check.
- The Jensen-Shannon MST turned out to give Q 108 degree **identically 24** — same as FR and Hellinger. The three arccos/sqrt-family metrics agree exactly at the MST-edge level for Q 108's neighborhood. This is informative: JS is NOT monotone-equivalent to FR in general (they differ on how they treat mixing distributions), yet on THIS DATA at α=0.5 they produce identical MSTs. Worth noting but no formal claim.
- Total-variation MST gives Q 108 degree 6 (rank-2 hub, behind Q 64 at 7). Clear metric-family split: sqrt-family vs L1.
- The α=0.01 result is the most informative of the run. Q 7 (al-Aʿrāf) becomes the top hub with degree 25, surpassing even Q 108's α=0.5 degree. Q 2 (al-Baqara) second at 16. Q 108 third at 11. The entire MST topology reorganizes: under near-no-smoothing, long Meccan narrative surahs dominate as centrality hubs (genuine content-breadth) rather than short Dirichlet-dominated surahs.
- Q 108's root profile is a genuine BARBELL: ~#4-frequency root (rbb) next to multiple corpus-hapax (nHr, btr). This is thematically apt — "Lord" next to a sacrifice verb that occurs nowhere else in the Quran — but suggests caution about calling Q 108 "average" or "central" in any generic sense.

## Deviations from pre-reg

None. Amendment applied pre-execution per audit-036 recommendation. Direction locked. Seed 20260417 honored. All deliverables at pre-registered paths.

## Files touched

- Created: `findings/phase-b-hypotheses/h-new-131-prereg.md`
- Created: `scripts/h_new_131_q108_supernode.py`
- Created: `findings/phase-b-hypotheses/csv/h-new-131.json`
- Created: `findings/phase-b-hypotheses/h-new-131-q108-supernode.md`
- Created: `journal/h-new-131-run-1.md` (this file)
