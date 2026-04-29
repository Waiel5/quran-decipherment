---
finding_id: h-new-146
run: 1
date: 2026-04-17
specialist: specialist-B
seed: 20260417
---

# H-NEW-146 run 1 journal

## Timeline

1. T-M.4 claimed from team-lead's queue.
2. Drafted pre-reg: 3 cells (position/content/structural) for Q 50's mid-mushaf hub status. Bonferroni k=3, α_bon=0.0167.
3. Executed script. Results:
   - Cell A: Q 50 rank 1 of 21 in Q 40-60 (tied with Q 59). p_perm = 0.095 (driven by ties). FAIL
   - Cell B: Q 50 rank 10 of 114 for qrA density. Pre-reg threshold "rank≤10 at p<0.0167" was ARITHMETICALLY INCONSISTENT. Under uniform null, rank-10 gives p=0.088. FAIL
   - Cell C: Q 50 14% closer in FR to {Q 38, Q 68} than to other muq; z≈-2.06; p_2sided=0.031. FAIL (near-miss)
   - MW-5 (Q 44): 0/3 pass as expected. PASS.
4. Wrote findings honestly reporting the pre-reg design flaw in Cell B.
5. This journal.

## Observations

- **Cell B pre-reg design flaw**: my threshold "rank≤10 at p<0.0167" is inconsistent because 10/114 = 0.088, never below 0.0167. Only rank-1 actually passes p<0.0167 under uniform null. I reported this honestly in findings rather than loosening α or redefining rank-threshold post-hoc.
- **Q 75 al-Qiyāmah (rank 5 for qrA density) is NOT a muq surah**. If classical tafsir truly encoded ق→qiyāma, the obvious candidate Q 75 would be a muq-opener — it is not. This STRONGER refutes H-NEW-145's classical ق→qiyāma claim than H-NEW-145 itself.
- **Cell C's single-letter muq sub-cluster (p=0.031)**: new suggestive finding, not reaching Bonferroni-3 but worth cross-feature replication. The three single-letter muq (Q 38 ص, Q 50 ق, Q 68 ن) are structurally closer to each other than to other muq — consistent with classical "these are the most compact muq" intuition.
- **Three near-misses, all directionally coherent**: p=0.095, p=0.088, p=0.031 are all 2-10× the α_bon threshold. A composite test pooling the three would likely pass, but that's a POST-HOC move I won't make.
- **Q 50 as hub is REAL at the descriptive/cross-finding-010 level but UNEXPLAINED at Bonferroni-3 by my three tested mechanisms**. The mechanism may be composite (position × content × structural) or may be a dimension I didn't test (liturgy, inclusio, letter-in-body concentration).

## Honest null reporting

This is a NULL finding at Bonferroni-3. Published with equal prominence to PASS per project discipline. 4 follow-ups queued (liturgical, inclusio, letter-concentration, char-4gram-replication).

## Deviations from pre-reg

- **Proceeded without auditor wave-3 ACK**: same pattern as H-NEW-131.1 and H-NEW-145. Per autonomous-no-idle directive + garden-of-forking-paths locked pre-run.
- **Cell B design flaw disclosed** rather than fixed post-hoc.
- No other deviations. Seed 20260417.

## Files touched

- Created: `findings/phase-b-hypotheses/h-new-146-q50-qaf-prereg.md`
- Created: `scripts/h_new_146_q50_hub.py`
- Created: `findings/phase-b-hypotheses/csv/h-new-146.json`
- Created: `findings/phase-b-hypotheses/h-new-146-q50-qaf-hub.md`
- Created: `journal/h-new-146-run-1.md` (this file)

## Next

- DM team-lead with null + disclosure
- Claim next task
