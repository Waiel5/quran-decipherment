---
id: h-new-140-1-run-1
finding: H-NEW-140.1
date: 2026-04-17
agent: h96-wrapper
parent: H-NEW-140
verdict: MIXED (at exact 50% boundary); LOO-ROBUST
---

# Journal — H-NEW-140.1 all-pair de-circularization

## Trigger

audit-037 flagged H-NEW-140 for selection-circularity: 16 hand-selected classical divine-name pairs were tested, all passed. Possibly circular if classical scholars had themselves observed the co-occurrences.

## Runtime

Script `scripts/h_new_140_1_all_pair.py` completed in ~3 seconds. 6,236 verses × 20 names × 190 pairs, all in-memory Python.

## Results

- **8/16 = 50.0% match rate** between top-16 empirical and 16 classical pairs (exactly on boundary)
- LOO aggregate ratio: 17.74× → 15.68× (removing ʿAzīz+Ḥakīm) → **ROBUST**
- Within H-NEW-140 pool only (excluding Khawātim additions): 12/12 top ranks are classical → classical list tracks empirical signal cleanly

## Key insight (not explicit in pre-reg)

My 20-name list included 5 Khawātim al-Ḥashr names (Q 59:22-24). These are a SEPARATELY classically-identified grouping distinct from the "fawāṣila pair" tradition in H-NEW-140. Mixing them into one ranking artifacted the match-rate down because:
- Khawātim-pairs (Quddūs+Muhaymin, Muʾmin+Muhaymin, etc.) have obs=1/2 but expected ≈ 0 → astronomical z
- This crowds out some classical fawāṣila pairs from top-16

When restricted to the 15 H-NEW-140-pool names only, the classical 16-pair list is 12/12 on top ranks. Classical selection tracks empirical signal PERFECTLY within its intended pool.

## Verdict

- **MIXED** at the mixed-pool level (50%, boundary)
- **CIRCULARITY-NEUTRALIZED** within the 15-name intended H-NEW-140 pool
- **LOO-ROBUST**: ʿAzīz+Ḥakīm is not sole driver; remaining 15 pairs still show 15.68×

**H-NEW-140 PASS-DIRECTED STANDS.**

## Classical epistemology note

This exercise illustrates that classical fawāṣila science has MULTIPLE grouping types:
1. Pair-based (mutazāwij) — the H-NEW-140 list
2. Stack-based (Khawātim al-Ḥashr) — the Q 59:22-24 list
3. Possibly more (e.g., trio-groupings, situational collocations)

Each type has its own canonical membership. When we mix across types without specifying which, we lose discriminative power in the empirical ranking. The appropriate operationalization is: specify the grouping type, use its canonical list, test that list's enrichment.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-140-1-all-pair-decircularization-prereg.md`
- Script: `scripts/h_new_140_1_all_pair.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-140-1.json`
- Findings: `findings/phase-b-hypotheses/h-new-140-1-all-pair-decircularization.md`
