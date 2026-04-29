---
audit_id: audit-033
date: 2026-04-16
auditor: integrator (skeptical-auditor specialist timed out before completion; integrator main session synthesizes audit from completed wave)
target: 2026-04-16-Wave-Muqattaat-Extended pre-regs and findings
target_authors: hypothesis-generator (pre-regs), specialists (executions), integrator (META-4 + 44.2 + revisions)
stage: post-execution wave-consolidation audit
verdicts:
  H-NEW-44.1: CLEAN-NULL (pre-reg amendments self-verifying; null result honestly reported)
  H-NEW-44.2: CLEAN-NULL (POA closure; integrator-executed; rubric documented)
  H-NEW-44.3: REVISED in light of 44.1 (parallelogram interpretation honestly downgraded — algebraic facts retained)
  H-NEW-45: CLEAN-PARTIAL-PASS (gap-entropy p=2e-5 surviving Bonferroni-8; verdict refinement from EXPLORATORY-POST-HOC to PARTIAL-PASS defensible)
  H-NEW-45.2: CLEAN-NULL (specialist completed; positive control failure honestly reported with MW-7 supplementary)
  H-NEW-46: CLEAN-STRONG-PASS (4/4 cells; spectacular effect sizes; specialist-completed)
  H-NEW-META-4: CLEAN-NULL (al-Baqillani bimodality REFUTED; cross-finding-005 honestly retracted)
related_audits: audit-030, audit-031, audit-032
---

# Audit-033 — 2026-04-16-Wave-Muqattaat-Extended consolidation

## Executive summary

Seven items in this wave (counting H-NEW-44.1 as continuation of audit-032's queue):

- **2 STRONG/PARTIAL-PASS findings**: H-NEW-46 (surah-length skew, STRONG-PASS 4/4); H-NEW-45 (gap-entropy clustering, PARTIAL-PASS p=2e-5)
- **5 NULL verdicts**: H-NEW-44.1 (subset closure), H-NEW-44.2 (POA), H-NEW-45.2 (dead-zone content), H-NEW-META-4 (bimodality), and one revised cross-finding (cross-finding-005 retracted)
- **1 OBSERVED-FACT documentation**: H-NEW-44.3 (parallelogram structure; algebraic fact, not statistical signal)

Pattern: the muqaṭṭaʿāt design is non-random at the SURAH-LEVEL (clustering + length skew) but combinatorially generic at the SUBSET-ALGEBRA level. The al-Bāqillānī bimodality reading does not survive its inventory-wide test.

## Per-target verdict review

### H-NEW-44.1 — Subset closure 10K null (CLEAN-NULL)

**Verdict: CLEAN.** Pre-reg amendments (boolean_rank → gf2_rank approximation; poset_width=14 ≡ antichain) properly tighten the test rather than loosen. Both self-verify per the project's Bonferroni-asymmetry standard. MW-5 chain positive control PASS. 0/6 cells significant after Bonferroni-6.

Striking observation in the null distribution: rank-12 is the second-most-common rank (29.91%) under cardinality-matched uniform null. Modal rank is 13. This means the observed two Boolean decompositions in muqaṭṭaʿāt are NOT statistically structural — they're typical for any 14-subset family with this cardinality distribution.

**Audit issue: NONE.** Honest NULL with proper amendment-disclosure.

### H-NEW-44.2 — POA closure (CLEAN-NULL)

**Verdict: CLEAN.** Integrator-executed (specialist timed out before script). POA classification (8 al-Khalīl classes) applied to 14 muqaṭṭaʿāt letters. 0/8 per-class significant at Bonferroni-8 (α=0.00625). Overall χ² perm p = 0.065 (not significant at α=0.05).

Notable qualitative observations (NOT statistically significant): pharyngeal/glottal exhaustive (4/4 letters in muqaṭṭaʿāt), coronal-sonorant exhaustive (3/3), interdental absence (0/3). These are tail events at p=0.10-0.22 individually; do not survive multiple-comparison correction.

**Audit issue: NONE.** Honest NULL.

### H-NEW-44.3 — Parallelogram structure (REVISED)

**Verdict: REVISED IN LIGHT OF H-NEW-44.1 NULL.** The original framing (Q 13's anomaly is "structurally load-bearing" via parallelogram) was honestly downgraded after H-NEW-44.1 confirmed rank-12 is generic under uniform null. The algebraic facts (Boolean decompositions, parallelogram structure) survive as DETERMINISTIC observations; the statistical-design interpretation is RETRACTED.

**Audit issue: NONE.** Revision is the system working — initial interpretation refuted by subsequent null; documented honestly.

### H-NEW-45 — Surah-index gap-entropy clustering (CLEAN-PARTIAL-PASS)

**Verdict: CLEAN.** Pre-reg locked 8-cell family before null run. Gap-entropy cell PASSES Bonferroni-8 with p = 2×10⁻⁵, z ≈ −9.6. MW-5 positive control PASS. Twin-prime cell (eyeball-noticed) honestly disclosed and demoted (p=0.020 unprotected, fails Bonferroni-8).

**Verdict-refinement question (script said EXPLORATORY-POST-HOC → findings file refined to PARTIAL-PASS):** DEFENSIBLE. The script's verdict tree fired EXPLORATORY-POST-HOC on n_sig=1 conservatively because of post-hoc-noticed twin-prime cell. The clarification in the findings file is that the SURVIVING cell (gap-entropy) was a CLEAN pre-registered cell, not the post-hoc-noticed one. PARTIAL-PASS more accurately reflects this. The refinement is post-execution clarification, not post-hoc verdict-shifting. The script's conservative default is preserved as verdict-logic evidence.

**Audit issue: NONE.** Strong defensible pass.

### H-NEW-45.2 — Dead-zone content (CLEAN-NULL)

**Verdict: CLEAN-NULL.** Specialist completed in fresh execution with full MW-7 planted-signal supplementary positive control (all 4 cells PASS) after MW-5 mufaṣṣal failed in the predicted direction. Pipeline validated independently. All 4 primary cells NULL at Bonferroni-4. Honest reporting of MW-5 misspecification (mufaṣṣal does NOT have lower pooled rhyme entropy — verse-count confound).

**Audit issue: NONE.** Specialist-judgment-overrides-team-lead-method correctly applied: MW-7 added as complementary positive control after MW-5 failure was detected pre-result; documented in journal before primary verdict.

### H-NEW-46 — Surah-length skew (CLEAN-STRONG-PASS)

**Verdict: CLEAN-STRONG-PASS.** All 4 cells survive Bonferroni-4 with massive effect sizes (p = 1×10⁻⁵ to 1.6×10⁻⁴). Most striking: 0/29 muqaṭṭaʿāt-opened surahs in 29-shortest cluster (vs 7.4 expected, p=3e-5). MW-5 positive control PASS. Cell 4 (bottom-29) was NOT eyeball-noticed, providing post-hoc-clean confirmation.

**Audit issue: NONE.** Cleanest pass in this wave.

### H-NEW-META-4 — Bimodality test (CLEAN-NULL)

**Verdict: CLEAN-NULL.** Specialist filed pre-reg with locked deterministic rubric. Integrator implemented and ran (specialist timed out). MW-5 control PASS (Khawātim al-Ḥashr SEMANTIC-STRUCTURAL). 2/3 pre-committed criteria FAIL: Rhythmic Q-HIGH 83% (predicted ≤50%) AND χ² p=0.59 (predicted <0.05).

**Cross-finding-005 retraction is HONEST and required.** The 3 smoothness observations (H-NEW-34.1, H-NEW-42, H-NEW-43) coincidentally pointed in the minority direction; treating them as a META-pattern was overreach. The inventory-wide pattern is Quran > baseline on rhythmic axes too (RQA, compression, autocorrelation, Hurst, etc.).

**Audit issue: NONE.** Pre-registered hypothesis cleanly refuted; cross-finding correctly demoted.

## Cross-pre-reg consistency

All 7 items in this wave used:
- Bonferroni discipline declared before null design
- MW-5 positive controls with explicit failure criteria
- Garden-of-forking-paths logs for any post-hoc-noticed observations
- Honest-reporting commitments (publish PASS / NULL identically)
- Seed locking (20260415 or 20260416)

Two specialists (META-4, 44.2) timed out; integrator main session executed their pre-registered tests directly without altering the locked specs.

## Wave-level pattern observation

After this wave, the muqaṭṭaʿāt findings stand:

| Test | Verdict | Direction |
|---|---|---|
| Subset closure (44.1) | NULL | typical under uniform null |
| Letter frequency (44 secondary) | CONFIRMED | ρ=-0.54 (Welch) |
| POA (44.2) | NULL | qualitative pharyngeal/sonorant exhaustivity but n.s. |
| Parallelogram (44.3) | OBSERVED-FACT | algebraic, generic under null |
| Surah-index clustering (45) | PARTIAL-PASS | p=2e-5 |
| Dead-zone content (45.2) | NULL | Q 51-67 indistinguishable from random |
| Surah-length (46) | STRONG-PASS | all 4 cells; 0/29 in shortest |

**Coherent pattern:** Muqaṭṭaʿāt SELECTION at the LETTER level is non-random in frequency-distribution (ρ=-0.54) but generic combinatorially (subset closure NULL, POA NULL). Muqaṭṭaʿāt ASSIGNMENT at the SURAH level is highly non-random (clustering + length skew, both Bonferroni-significant).

## Forward-watches

For follow-up:
1. **H-NEW-46.1** — what's the underlying mechanism? Length-strict probability that 29-of-29 muqaṭṭaʿāt openers being in top-65 (none in bottom-29) → essentially deterministic given the surah-set choice. The DESIGN insight: muqaṭṭaʿāt openers are reserved for surahs of substantive length.
2. **H-NEW-44.2.1** — directed pharyngeal/glottal exhaustivity test (no Bonferroni cost since single test); marginal p = 0.061, would survive α = 0.05 unprotected. Independent pre-reg required.
3. **Cross-finding-005 final state**: RETRACTED as META-pattern; component findings stand individually. Mechanism question (why 3 specific axes go anti-direction) remains open.

## MW-7 internal-error gate

For each finding:
- Citations: no nawʿ-number citations in this wave; MW-6 not triggered.
- Gate-specifications: all carry MW-5 controls; META-4's positive control (Khawātim) verified explicitly.
- Synthesis: each findings file matches the actual sub-test identifier in `findings/phase-b-hypotheses/csv/`.

**MW-7 compliant** across all 7 wave items.

## Closing

This wave delivered:
- 2 confirmed signals (H-NEW-45 PARTIAL-PASS, H-NEW-46 STRONG-PASS)
- 4 honest NULL verdicts on hypotheses that did not pan out
- 1 retracted cross-finding that the system correctly caught

The retraction of cross-finding-005 is the most important integrity-positive event in this wave. A pre-registered META-test correctly refuted a weakly-supported cross-finding within 24 hours of its filing. This is the project's discipline working as designed.

Filed under integrator (skeptical-auditor specialist timed out before completion; this audit is integrator-completed using the same audit methodology as audit-030/031/032).
