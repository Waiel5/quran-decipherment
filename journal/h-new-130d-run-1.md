# Journal — H-NEW-130d run 1 (integration)

**Date**: 2026-04-17
**Specialist**: specialist-a
**Task**: T-L.1 + T-L.2 + T-L.3 integration after T-L (H-NEW-130c) completion
**Type**: Post-hoc descriptive integration. No new pre-reg (each sub-task is either trivial or already-answered or exploratory-integration).
**Seed**: 20260417 (inherited from parent analyses)

## Sequence

1. Completed T-L (H-NEW-130c, TRIPLE-REPLICATION-CONFIRMED).
2. Evaluated remaining sub-tasks T-L.1, T-L.2, T-L.3.
3. **T-L.1 (reverse mushaf)**: trivial by metric symmetry. Verified programmatically: forward-top-15 == reverse-top-15 unordered pairs at 15/15 intersection. Non-trivial variant (length-sort) already answered in H-NEW-130's MW-5 (0/15 shared — mushaf-specific).
4. **T-L.2 (universal hinges)**: already answered as Secondary B of H-NEW-130c. {Q 14→15, Q 49→50, Q 56→57}. Cross-referenced into integration.
5. **T-L.3 (wrap-around interaction)**: computed d(Q 114, Q 1) on 3 feature spaces; ranked against 113 forward-consecutive pairs. Result: wrap-around is CONTINUITY, not HINGE, on all 3 spaces. Especially extreme on verse-length (rank-1 smallest of all candidate edges).

## Key empirical result (T-L.3)

| Feature | d(Q114, Q1) | Rank among forward pairs |
|---|---:|:-:|
| Root | 0.388 | 97 of 113 |
| Char-4-gram | 0.423 | 98 of 113 |
| Verse-length | 0.083 | 113 of 113 (smallest) |

The wrap-around edge would CLOSE the mushaf smoothly, supporting cross-finding-013's topological-ring claim. The ring-closure is geodesically-efficient, not a structural boundary.

## Verdict

- T-L.1: TRIVIAL (by metric symmetry)
- T-L.2: CATALOGED (3 universal hinges; pre-committed ≥3 met)
- T-L.3: EXPLORATORY-POST-HOC observation consistent with cross-finding-013

Integration finding H-NEW-130d filed. No new inferential claim; descriptive synthesis.

## T-L.4 (cross-corpus) deferred

Cross-corpus test requires: (a) a matched-length non-Quranic corpus (Bukhārī available at 526K tokens vs Quran 78K); (b) segmentation into 114 "chapter-equivalents"; (c) definition of a Bukhārī-specific "structural-boundary set B" — which is either CIRCULAR (match Quranic boundaries; trivial) or IMPOSSIBLE (Bukhārī has no muqaṭṭāʿat, no mushaf-order, no chronology). Plus: what does it MEAN for Bukhārī to have a "mushaf-like ordering"? Bukhārī is a hadith collection organized by legal topic, not a revealed text with canonical order.

The meaningful cross-corpus test would be: does ANY reasonable ordering of 114 Bukhārī chapter-equivalents produce top-15 boundary-coincidence? A HARD NEGATIVE RESULT here would be strongest — if Bukhārī cannot produce boundary-concentration under any ordering, the Quranic finding is corpus-specific.

I'm recommending T-L.4 be dispatched as a **separate, complex task** to a new specialist with proper pre-registration (what Bukhārī chapter segmentation? what boundary-type definition? what ordering?). Out of scope for a same-session autonomous iteration.

## Files

- H-NEW-130d findings: `findings/phase-b-hypotheses/h-new-130d-reverse-universal-wraparound.md`
- Journal: this file
- No new script (analysis is ad-hoc integration over existing H-NEW-111/111b/111c D-matrices)

## Team communication

- Will DM team-lead with T-L.1/2/3 summary + T-L.4 deferral rationale.
- Will NOT mark T-L.4 in-progress since it's a separate pre-reg-requiring task.
