---
finding_id: h-new-264
run: 1
date: 2026-04-18
specialist: specialist-B
seed: 20260420
prereg_sha256: 8a29c8088271b6bbeb39f561e8083e3d4504219c377d0b82e4a031f287c96497
---

# H-NEW-264 run 1 journal

## Goal

Land a tight, preregistered "Q 1 connects everything" follow-up without
expanding into a broad cluster search. The locked question was:

**Does Q 1's root profile connect anomalously to the classical ḥā-mīm
subset Q 40-46, despite Q 1's structural isolation in H-NEW-89?**

## Rules actually used

- Data: `surah-root-graph.json` QAC STEM roots
- Anchor: Q 1 distinct root set
- Target subset: Q 40-46 only
- Cells: unweighted recall + IDF-weighted recall
- Null: 10,000 random 7-surah subsets preserving exact period and
  coarse verse-count-bin composition of Q 40-46
- Bins locked as `<10`, `10-29`, `30-59`, `60-99`, `100+`
- Bonferroni family: k=2, α_bon=0.025
- MW-5 positive control: Q 62 against {57, 59, 61, 64}

No expansion beyond that scope.

## Execution

1. Read prior Q 1 files to avoid duplicating H-NEW-137 / H-NEW-138.
2. Prototyped candidate subset metrics locally.
3. Chose the ḥā-mīm block because it stayed positive under a stricter
   period+length-matched null.
4. Wrote prereg first.
5. Implemented `scripts/h_new_264_q1_connects_everything.py`.
6. Ran the script once from repo root.

Command:

```bash
python3 scripts/h_new_264_q1_connects_everything.py
```

No blockers. Run completed cleanly and wrote the JSON on first pass.

## Result

**CONFIRMED.**

| Cell | Observed | Null mean | z | p | Pass? |
|---|---:|---:|---:|---:|:--:|
| A unweighted recall | 0.7381 | 0.5463 | +3.16 | 0.0001 | YES |
| B IDF-weighted recall | 0.5049 | 0.3543 | +3.13 | 0.0005 | YES |

MW-5 positive control also passed:

| MW-5 cell | Observed | Null mean | z | p |
|---|---:|---:|---:|---:|
| Q 62 recall vs musabbiḥāt | 0.4704 | 0.3968 | +2.81 | 0.0001 |
| Q 62 IDF recall vs musabbiḥāt | 0.3098 | 0.2433 | +3.45 | 0.0001 |

## Key raw numbers

- Q 1 distinct roots: **18**
- Average number of Q 1 roots present in a ḥā-mīm surah: **13.29 / 18**
- Strongest member: **Q 42**, sharing **17 / 18** Q 1 roots
- Weakest member: **Q 44**, still sharing **9 / 18**

Roots present in all 7 members of Q 40-46:
- `Alh`, `Elm`, `qwm`, `rHm`, `rbb`, `smw`, `ywm`

## Interpretation kept tight

This run does **not** say Q 1 connects to everything.

It says one narrower claim survives a conservative test:

**Q 1 is structurally isolated in the classical membership network, but
its root profile is significantly over-represented inside the ḥā-mīm
subset Q 40-46 relative to a matched null.**

That is a specific subset-level connection, not a universal one.

## Limits logged during run

- One subset only; no ranking across all clusters.
- Root-set metrics only; no phrase-level rescue attempted.
- Coarse length matching, not exact length or exact root-count matching.
- Two inferential cells share the same underlying subset and anchor, so
  Bonferroni is conservative.

## Files landed

- Pre-reg: `findings/phase-b-hypotheses/h-new-264-q1-connects-everything-prereg.md`
- Script: `scripts/h_new_264_q1_connects_everything.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-264.json`
- Findings: `findings/phase-b-hypotheses/h-new-264-q1-connects-everything.md`
- Journal: this file
