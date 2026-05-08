---
finding: H-NEW-920
specialist: inline (post-subagent-stall recovery)
date: 2026-05-07
seed: 20260507
prereg_sha256: 2bd4c93ee87d0a5fac1c7331d16890966f21d46ad5c94455254bc6a915b32758
---

# H-NEW-920 geodesic-curvature run journal

## Context

Original specialist (agent ID aea86002ddfc7865c) was dispatched 2026-05-07 to pre-register and execute discrete-curvature analysis of the mushaf path. Pre-reg + script were written to disk. The agent then hit "API Error: Stream idle timeout — partial response received" before producing the JSON, findings, journal, or ledger update. Inline-execution recovery ran here.

## Pre-flight reading completed (by original specialist before stall)

- INVESTIGATION-PROTOCOL.md
- quran-investigation/SKILL.md
- h-new-111-fisher-rao-mushaf.md
- cross-finding-011-mushaf-fisher-rao-confirmed.md
- h-new-130-fisher-rao-residuals.md
- h-new-236-1-hinges-constrained-simulator.md (and 236.1a..d cells)
- cross-finding-020-the-complete-equation.md

## Garden-of-forking-paths log

(Locked in pre-reg §2-§5 BEFORE inline-execution.)

- Primary metric: turn_cost = d_in + d_out − d_skip (chosen because FR is metric, so triangle-slack is naturally non-negative and well-defined). Locked.
- Secondary metric: turning_angle (Euclidean-pseudo arccos formula). Computed for diagnostic, NOT used for verdict. Locked.
- Boundary windows: Mufaṣṣal-onset Q 50 ±2, Ḥawāmīm Q 39→40 ±2, Medinan Q 2 ±2. Selected from al-Zarkashī *al-Burhān* nawʿ 1, al-Suyūṭī *al-Itqān* nawʿ 18, and Nöldeke-phase chronology. Locked BEFORE looking at curvature spectrum.
- Bonferroni-3 on H1a sub-cells (B1, B2, B3); JOINT sub-test descriptive at α=0.05 (not Bonferroni-counted as 4th cell per pre-reg §5).
- Direction-of-effect locked: H1b lower-tail one-sided (mushaf SMOOTHER than null). Reverse-direction → PRE-COMMIT VIOLATION published with prominence per Protocol §1.8.
- 10000 perms, seed 20260507. Per-perm seed = 20260507 + r per pre-reg §3.

## Decision points during inline-execution

1. SHA256 of pre-reg verified at runtime (line 47-54 of script, fail-fast on mismatch). Verified: 2bd4c93ee87d0a5fac1c7331d16890966f21d46ad5c94455254bc6a915b32758. Match.
2. Python script was already on disk from the original agent (the only thing that DID land before stall). Read it; verified it implements pre-reg §4 turn-cost formula correctly. Did not modify.
3. Ran inline via Bash. Produced JSON in 47s.
4. Wrote findings markdown.
5. Wrote this journal.

## Honest reporting

- H1a: NULL (0/10 hits in B1∪B2∪B3; perm-p = 1.000 for all four sub-cells).
- H1b: PASS (z = −5.638, p = 0.00000 lower-tail; mushaf 19.5% smoother than random).
- Overall: PASS-DIRECTED (H1b only).

The H1a NULL is significant: it falsifies the pre-committed claim that classical block-boundaries (Mufaṣṣal-onset, Ḥawāmīm-cluster, Medinan-block-onset) are also Fisher-Rao curvature peaks. The empirical curvature peaks land at DIFFERENT positions — predominantly the project's already-discovered TRUE-ISOLATES (Q 16, Q 21, Q 22, Q 23, Q 25 from H-NEW-126) and STRUCTURAL-TWIN-PAIRS (Q 24 + Q 33 from cross-finding-026 §13). This is descriptive (post-hoc, MW-7 capped at single-test α=0.05) and queued for a formal pre-registered follow-up (H-NEW-920b proposed: pre-register the H-NEW-126 + cross-finding-026-§13 sets as B' and re-test).

## Output paths

- Pre-reg: findings/phase-b-hypotheses/h-new-920-geodesic-curvature-prereg.md
- Script: scripts/h_new_920_geodesic_curvature.py
- JSON: findings/phase-b-hypotheses/csv/h-new-920.json
- Findings: findings/phase-b-hypotheses/h-new-920-geodesic-curvature.md
- Journal: this file
- Ledger update: pending (next inline step)

## DATA-GAPs

- No DATA-GAPs for this run. All inputs were already on disk (h-new-111.json complete; pre-reg complete; script complete).

## Subagent-stall context

This was the first inline-execution recovery in the Wave-D series. Multiple parallel agents stalled with "Stream idle timeout" after a brief network event 2026-05-07. The pre-reg files those agents wrote are usable; the executions were interrupted. This run demonstrates that inline recovery from disk-state is straightforward when the pre-reg + script have landed.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
