# H-NEW-94 Run 1 — Journal

**Date**: 2026-04-17
**Agent**: h-new-94-specialist
**Seed**: 20260417
**N_PERM**: 10,000
**Bonferroni**: k=2, α_bon=0.025
**Family**: h-new-94-cluster-empty-zone

## Task
H-NEW-94 — Q 16-25 cluster-empty zone deep-dive. Per H-NEW-89, Q 16-25
is the LARGEST cluster-empty stretch with 8/10 isolates. Two cells:
(A) isolate-count reconciliation; (B) shadow-cluster hunt.

## Pre-reg workflow

1. Read HANDOFF 01, 04, 05 (OQ-2 specifically).
2. Read H-NEW-89 results file — understood the "≥2-surah multi-surah
   cluster" rule is what makes Q 19 (كهيعص) and Q 20 (طه) appear as
   isolates, since they are classical singletons.
3. Read H-NEW-89 script — verified the 11-cluster locked list verbatim.
4. Inspected available morphology data: `data/morphology/surah-root-graph.json`
   provides 1642 distinct roots with per-surah counts.
5. Inspected H-NEW-66 JSON: top-50 verse-pairs available, inter-surah
   twin edge counts computable.
6. Wrote pre-reg with YAML frontmatter including `bonferroni_k: 2`,
   `alpha_bon: 0.025`, explicit direction-lock for Cell B, MW-5
   positive-control specification, garden-of-forking-paths log
   disclosing H-NEW-89 prior.
7. Wrote script implementing root-Jaccard (S1), char 5-gram Dice (S2),
   H-NEW-66 verse-twin edge count (S3), rank-mean aggregated as S_agg.
8. Ran script; elapsed ~0.9s (10K perms on 6441 pairs with pair_index
   lookup; efficient).

## Cell A result

- 21 isolates total (matches H-NEW-89 headline).
- **9 of 10 in Q 16-25** (NOT 8 as H-NEW-89 text stated).
- Only Q 18 al-Kahf is non-isolate in the zone (via C7 Friday).
- H-NEW-89 text error: "Q 16-25 zone (8 of 10 surahs out of 10 in this
  range are isolates)" should read "9 of 10".
- The top-line isolate list in H-NEW-89's findings file lists:
  `{1, 8, 13, 16, 17, 19, 20, 21, 22, 23, 24, 25, 33, 34, 35, 36, 37, 38, 39, 47, 48}`
  — counting {16, 17, 19, 20, 21, 22, 23, 24, 25} gives 9 entries in
  the 16-25 range. The "8 of 10" prose is an off-by-one in the summary.
- Q 19 and Q 20 being singletons is NOT an error — H-NEW-89's own
  caveat §1 explicitly acknowledges this.

## Cell B result

- Observed T (mean S_agg over 45 pairs in Q 16-25) = 5019.4
- Null mean T = 3918.4 (median 4096.0)
- p one-sided upper = 0.168
- Q 16-25 ranks #18 of 105 contiguous 10-surah windows (83rd pctl)
- Bonferroni α=0.025: **NO PASS**
- Direction HIGHER-than-random is CONFIRMED descriptively but NOT
  at Bonferroni or even unadjusted α=0.05.

## MW-5 positive controls — CRITICAL FINDING

Both fail at α=0.05:
- Q 57-64 (musabbiḥāt stretch): p = 0.382
- Q 40-46 (ḥawāmīm): p = 0.179

**Diagnosis**: contiguous-window tests against contiguous-window null
are under-powered for H-NEW-58c-style clusters because:
1. Musabbiḥāt Q 57/59/61/62/64 skip Q 58/60/63 which dilute the
   Q 57-64 window.
2. Null includes many mufaṣṣal windows of comparable internal
   similarity — the ḥawāmīm are internally similar but NOT unique.

Per pre-reg, MW-5 failure → Cell B **NULL-BROKEN**.

## Honest decision

Per discipline §MW-5: "if positive-control fails, the null is broken;
STOP and report NULL-BROKEN." I comply. Cell B cannot be interpreted
as an inferential test. The 83rd-percentile descriptive result is
reported transparently but NOT promoted.

## Thematic observation (post-hoc, descriptive)

The Q 16-25 zone is prophet-narrative + reminder-polemic heavy.
Top-5 similar pairs are Q 16-Q 22, Q 17-Q 25, Q 21-Q 23, Q 16-Q 23,
Q 17-Q 18 — all share creation-sign + prophetic-discourse vocabulary.
The zone lacks a CLASSICAL collective name (no classical "surahs of
Y" cluster covers these 10), hence its H-NEW-89 cluster-emptiness.

## Files written

1. `findings/phase-b-hypotheses/h-new-94-q16-q25-zone-prereg.md` (pre-reg)
2. `scripts/h_new_94_q16_q25_zone.py` (script)
3. `findings/phase-b-hypotheses/csv/h-new-94.json` (results)
4. `findings/phase-b-hypotheses/h-new-94-q16-q25-zone.md` (findings)
5. `journal/h-new-94-run-1.md` (this file)

## Notes for MASTER-LEDGER integration

- H-NEW-89 **reporting correction**: "8 of 10 isolates in Q 16-25"
  should read "9 of 10". Top-line total 21 confirmed. Does not
  alter H-NEW-89 verdict (PASS at 2/3 inferential cells).
- H-NEW-94 itself: Cell A DESCRIPTIVE-COMPLETE; Cell B NULL-BROKEN.
- OQ-2 partial answer: zone is moderately-dense (83rd pctl) but no
  statistically-resolved shadow cluster at this resolution. Future
  work should use non-contiguous null + higher-resolution signatures
  (e.g., opening-formula match vector, divine-name list match vector).

## Self-audit

- ✓ YAML frontmatter has bonferroni_k, bonferroni_family, alpha_bon,
  direction_A, direction_B, acceptance_window (PRE-REG-STANDARD-04).
- ✓ Direction locked BEFORE results viewed (pre-reg written and
  committed before running script).
- ✓ MW-5 positive control specified BEFORE run.
- ✓ MW-5 failure HONESTLY REPORTED even though it costs the test.
- ✓ Garden-of-forking-paths log includes H-NEW-89 prior disclosure.
- ✓ NULL published with same prominence as a PASS would have been.
- ✓ Specialist-judgment override NOT invoked; I followed the task spec.

## What I did NOT do

- I did NOT add a post-hoc second test to "rescue" the MW-5 failure.
  That would be a new H-NEW-94.N pre-reg, not an amendment.
- I did NOT alter H-NEW-89's verdict; only flagged the in-text
  "8 of 10" vs actual "9 of 10" count as a reporting correction.
- I did NOT extend the cluster taxonomy to include singleton
  muqaṭṭāʿat; that was already documented in H-NEW-89's caveats
  and I reported the alternative-rule sensitivity honestly.
