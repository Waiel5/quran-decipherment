---
finding_id: h-new-279
run: 1
date: 2026-04-18
specialist: codex
seed: 20260418
---

# H-NEW-279 run 1 journal

## Timeline

1. Read `HANDOFF/05-OPEN-QUESTIONS.md` at OQ-19 and `HANDOFF/03-NEXT-MOVES.md` at NM-37.
2. Read parent code and results around:
   `scripts/h_new_131_q108_supernode.py`,
   `scripts/h_new_131_1_alpha_sweep.py`,
   `findings/phase-b-hypotheses/h-new-134-mst-analysis.md`,
   `journal/h-new-131-run-1.md`,
   `journal/h-new-131-1-run-1.md`.
3. Scoped the metric family before execution. Locked a bounded 5-metric primary family:
   `Fisher-Rao`, `Jensen-Shannon`, `Total variation`, `Euclidean L2`,
   `Cosine-angle`.
4. Explicitly excluded `Hellinger` from the primary family because it is
   monotone-redundant with Fisher-Rao for Kruskal MST purposes.
5. Explicitly excluded `KL` from the primary family because the repo does
   not already lock a symmetric KL convention for this MST line.
6. Wrote pre-reg:
   `findings/phase-b-hypotheses/h-new-279-metric-robustness-mst-prereg.md`.
7. Wrote script:
   `scripts/h_new_279_metric_robustness_mst.py`.
8. Executed the script. Results:
   - Fisher-Rao replication: `Q108 degree = 24` exactly.
   - Jensen-Shannon: `Q108 degree = 24`, rank `1`.
   - Total variation: `Q108 degree = 6`, rank `2`.
   - Euclidean L2: `Q108 degree = 22`, rank `1`.
   - Cosine-angle: `Q108 degree = 21`, rank `1`.
   - Diagnostic Hellinger: `Q108 degree = 24`, rank `1`, and exact MST
     edge-set match with Fisher-Rao.
9. Computed the locked primary verdict:
   `Q108` top-3 on `5/5` primary metrics -> `METRIC-ROBUST HUB`.
10. Wrote JSON:
    `findings/phase-b-hypotheses/csv/h-new-279.json`.
11. Wrote findings file:
    `findings/phase-b-hypotheses/h-new-279-metric-robustness-mst.md`.
12. Wrote this journal.

## Observations / notes

- The biggest substantive update is not that Fisher-Rao replicated. That
  was expected. The important result is that the three additional
  non-redundant metrics do not eject `Q108` from the top tier.
- `TV` is the limiting case. It keeps `Q108` near the top but strips away
  the extreme degree magnitude. That makes the honest headline:
  top-tier rank is robust; super-hub magnitude is not.
- `Euclidean L2` and `cosine-angle` both support the stronger reading much
  more than expected from the H-NEW-131 `TV` result alone. They leave
  `Q108` at degree `22` and `21` respectively.
- The consensus table is informative:
  `Q108` appears top-3 on `5/5` metrics, `Q7` on `4/5`, `Q112` on `3/5`,
  `Q64` on `2/5`. So Q108 is the most stable hub under metric variation in
  this bounded family.

## Deviations from pre-reg

None.

## Files touched

- Created: `findings/phase-b-hypotheses/h-new-279-metric-robustness-mst-prereg.md`
- Created: `scripts/h_new_279_metric_robustness_mst.py`
- Created: `findings/phase-b-hypotheses/csv/h-new-279.json`
- Created: `findings/phase-b-hypotheses/h-new-279-metric-robustness-mst.md`
- Created: `journal/h-new-279-run-1.md`
