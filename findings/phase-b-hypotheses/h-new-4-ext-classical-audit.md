---
finding_id: h-new-4-ext-classical-audit
phase: B
status: AUDIT-BLOCKER-RESOLVED-OPTION-D
date: 2026-04-13
filed_by: classical-scholar
parent_task: 6 (H-NEW-4 Muqaṭṭaʿāt first-lemma-introduction rate signature)
new_task: 33 (H-NEW-4-EXT, original framing AUDIT-BLOCKED)
ruling: team-lead 2026-04-13 — Option D APPROVED (al-Rāzī ijmāl-tafṣīl at letter-graphemic scale)
sister_audit: findings/phase-b-hypotheses/h-new-11-ext-reprereg.md (Task #36 §2 audit memo)
---

# [[h-new-4-ext-classical-audit|H-NEW-4]]-EXT classical audit — pre-execution data-coherence catch

## Executive verdict

**AUDIT-BLOCKER raised, then resolved via Option D re-operationalization.**

Task #33 was filed downstream of completed task #6 with the framing: "Task #6 established absolute effect; this task adjudicates whether that effect EXCEEDS the universal ḥusn al-ibtidāʾ baseline that al-Suyūṭī (Itqān nawʿ 59) predicts for ALL surahs."

Classical-scholar pre-dispatch review (2026-04-13) found that **the parent task #6 verdict is `REFUTED`, not `established absolute effect`.** Per `findings/phase-b-hypotheses/team-discovery-004.md` line 14:

> verdict: REFUTED

And lines 40-44 document that the [[h-new-4-ext-classical-audit|H-NEW-4]] effect actually reverses sign at cp=500 and cp=1000 — no checkpoint passes Bonferroni, and the direction reverses across checkpoints. The premise of #33 (test whether a confirmed muqaṭṭaʿāt-vs-baseline effect EXCEEDS al-Suyūṭī's universal baseline) is incompatible with a refuted-with-direction-reversal parent.

The AUDIT-BLOCKER was raised in two SendMessage rounds to team-lead. Team-lead's 2026-04-13 ruling: **Option D APPROVED** — re-operationalize at the letter-graphemic scale per al-Rāzī's literal *al-mujmal* doctrine, plugged into the [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] letter-multiset infrastructure that IS confirmed in MASTER §3c.

## The four re-routing options surfaced

| Option | Description | Status |
|---|---|---|
| (a) | Dispatch as-is with full disclosure of parent contradiction | NOT SELECTED — wastes compute on a hypothesis whose premise is false |
| (b) | Reframe to test the sign-reversal phenomenon itself | NOT SELECTED — viable but doesn't engage classical doctrine |
| (c) | Drop [[h-new-4-ext-classical-audit|H-NEW-4]]-EXT entirely | NOT SELECTED — preserves classical signal but loses the al-Rāzī doctrinal anchor |
| (d) | Re-operationalize at letter-graphemic scale per al-Rāzī's literal *al-mujmal* doctrine | **SELECTED 2026-04-13 by team-lead** |

## Option D selection rationale (team-lead 2026-04-13)

Three convergent reasons led to Option D:

1. **Doctrinal precision**: al-Rāzī (*Mafātīḥ al-Ghayb* 7:152-154, Āl ʿImrān commentary) literally calls the muqaṭṭaʿāt *al-mujmal* — the disconnected letters ARE the *ijmāl*; the surah body is the *tafṣīl*. Operationalizing at the letter-graphemic scale matches al-Rāzī's actual language. Operationalizing at the lemma/TTR scale (the original task #33 framing) tests something al-Rāzī never claimed.

2. **Parent-task scale coherence**: parent task #6's REFUTED verdict applies at the lemma/TTR scale. The same audit memo that records the refutation explicitly notes: *"its distinctiveness [the muqaṭṭaʿāt's] is at the letter/phonological level"* — which is the layer al-Rāzī's doctrine actually addresses.

3. **Infrastructure leverage**: the [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] letter-multiset machinery from #44/#64/#65 already exists, has cleared B1+B2 orthogonalization, and is CONFIRMED in MASTER §3c as a sub-word structural-signature detector. Plugging an *ijmāl-thumma-tafṣīl* differential test into that infrastructure is the cleanest possible follow-up — no new pipeline, just a new feature on a validated substrate.

## Defect class

**Same project-level pattern as #36** (sister audit: `[[h-new-11-ext-methodological-null|h-new-11]]-ext-reprereg.md`):

- A re-prereg is filed downstream of a parent finding without first auditing the parent's verdict text.
- The parent contains data that already determines or contradicts the new test.
- If dispatched, the new test would either (a) waste compute on a foregone conclusion, (b) report a "result" that is actually a forking-paths violation, or (c) directly contradict the parent.

#36 was the **nawʿ-citation-defect + binary-direction-defect** flavor. #33 is the **parent-verdict-contradiction** flavor. Both were caught at the classical-scholar pre-execution data-coherence gate before any computational-tester compute was burned.

This pattern justifies promotion to a standing project rule: see MW-8 below.

## MW-tier sub-test tagging applied (Option D framing)

For the new Option D pre-reg (filed separately at `findings/phase-b-hypotheses/h-new-4-ext-d-prereg.md`):

| Source | Citation | MW tier | Status |
|---|---|---|---|
| al-Rāzī *Mafātīḥ al-Ghayb* 7:152-154 (Āl ʿImrān commentary, *al-mujmal* doctrine) | Verbal anchor for muqaṭṭaʿāt = *ijmāl*, body = *tafṣīl* | MW-5 (high-confidence verbal anchor; not yet physically verified at this verse range) | PENDING per AMEND-28 |
| al-Rāzī *Mafātīḥ al-Ghayb* preface to Q 2 | The *al-mujmal* attribution to muqaṭṭaʿāt is in al-Rāzī's preface to al-Baqara | MW-5 | PENDING per AMEND-28 |
| al-Suyūṭī *Itqān* nawʿ 59 (*ḥusn al-ibtidāʾ wa-l-intihāʾ*) | Universal baseline reference (no longer the test target under Option D) | MW-4 | PENDING per AMEND-28 |
| al-Zamakhsharī *Kashshāf* 1:26 (al-Mahdī ed.) | *māddat al-kalām* compositional substrate | MW-4 | PENDING per AMEND-28 |

All citations carry PENDING flags per AMEND-28; team-lead has standing approval for dispatch with MW-3+ disclosed (same pattern as #49 HASHR Phase 2 DEFERRED-EXTERNAL-DEPENDENCY).

## Re-prereg pending

The Option D re-prereg lives in a separate file: `findings/phase-b-hypotheses/h-new-4-ext-d-prereg.md`. Hand-off path: classical-scholar drafts the spec → arabic-specialist supplies letter-multiset extraction (already exists) → computational-tester executes the KL-divergence comparison.

## Reporting commitment

- Both directions publishable.
- If KL_muqaṭṭaʿāt < KL_baseline at p < 0.01: al-Rāzī's *ijmāl-tafṣīl* doctrine receives first-ever empirical support at the letter-graphemic scale.
- If KL_muqaṭṭaʿāt ≈ KL_baseline: null result, al-Rāzī's doctrine joins the demoted-classical-intuition list.
- If KL_muqaṭṭaʿāt > KL_baseline: serious counter-finding, muqaṭṭaʿāt body LESS aligned with their announced letters than length-matched controls.

## Cross-reference

- Sister audit: `findings/phase-b-hypotheses/h-new-11-ext-reprereg.md` (Task #36, AUDIT-BLOCKER + PRE-FALSIFICATION pattern)
- Standing rule: MW-8 (see TEAM-AMENDMENTS-LOG.md, filed concurrently with this memo)
- Option D re-prereg: `findings/phase-b-hypotheses/h-new-4-ext-d-prereg.md`
- Parent task #6 finding file: `findings/phase-b-hypotheses/team-discovery-004.md`

## Authorship and accountability

Filed by classical-scholar, 2026-04-13. Audit catch self-credited; ruling on Option D selection by team-lead 2026-04-13 same date. Re-prereg drafting and dispatch path: classical-scholar → arabic-specialist → computational-tester.
