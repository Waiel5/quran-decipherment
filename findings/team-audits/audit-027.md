---
audit_id: audit-027
target_finding: h-new-31-incipit-time-space
target_file: findings/phase-b-hypotheses/incipit-time-space.md
target_author: computational-tester
auditor: skeptical-auditor
phase: B
date: 2026-04-13
verdict: NEEDS REVISION — primary PASSED-AS-NULL is clean, but Sub(a) SPACE "publishable" framing requires demotion to exploratory under within-sub(a) multiple-testing accounting
bonferroni_k_declared: 3
bonferroni_k_true: 9 (3 Fisher direction-tests within sub-a × 3 sub-tests)
---

# audit-027 — H-NEW-31 time/space/cosmos incipit asymmetry

## Executive verdict

**NEEDS REVISION.** Primary pre-registered joint test FAILS cleanly and honestly (1/3 sub-tests pass; tester correctly joint-fails). SPACE Fisher p = 0.0146 is a real directional finding but the finding document frames it as "Publishable SPACE result" and "passes the pre-registered test" at Bonferroni α = 0.0167. **This framing is wrong: true Bonferroni across the sub(a) Fisher family × 3 sub-tests is k = 9, α = 0.00556.** SPACE does NOT beat k=9. The correct framing is: primary pre-reg fails joint; SPACE is an *exploratory* directional signal at nominal p = 0.0146 requiring external replication (task #82 H-NEW-31.1 already registered).

Integrator has already registered H-NEW-31 as **Tier-B PARTIAL** and opened H-NEW-31.1 (held-out apocalyptic-oracular control) and H-NEW-31.2 (7-class OATH scheme) as follow-ups, and has rejected AMEND-22 (class-scheme re-operationalization). Integrator handling is correct; only the finding-doc framing needs F-level repair.

Positive structural aspects:
- Clean pre-registration of direction (Meccan > Medinan for TIME, Medinan > Meccan for SPACE)
- Tester explicitly labels the Early-Meccan TIME-concentration observation as "NOT pre-registered — cannot claim significance without replication" (Limits #4)
- Joint verdict correctly declared FAIL per 3/3-required rule
- Forking paths disclosed, including tested-but-not-changed marker-priority reorder
- Three classical-scholar follow-ups flagged

## HARKing 4-test

| Test | Verdict | Evidence |
|---|---|---|
| 1. Non-counting of failed sub-tests | **PASS** | Finding doc explicitly lists (b) and (c) as FAIL. Joint FAIL declared. |
| 2. Pre-existing mechanism | **PASS** | al-Suyūṭī *Itqān* nawʿ 59 + Ibn ʿAshūr muqaddima cited up-front. |
| 3. Pre-registered direction | **PASS with F-level framing fix needed** | TIME direction (Meccan > Medinan) was pre-registered and observed-reverse — correctly declared FAIL. SPACE direction (Medinan > Meccan) was pre-registered and passed nominally. Early-Meccan TIME observation explicitly flagged as not pre-registered. |
| 4. Refusal to rename | **PASS** | No retrofit to "Early Meccan time asymmetry thesis". Tester honestly preserves original "Late Meccan" pre-reg claim as refuted. |

**HARKing 4/4 CLEAN PASS.** This is computational-tester's standard signature for honestly-reported Tier-B PARTIAL findings.

## Blocking revisions

### B1 — Within-sub(a) Bonferroni undercount (SPACE framing)

The declared `bonferroni_k: 3` applies to the three sub-tests (a, b, c). But sub(a) itself contains **three directional Fisher tests** (TIME, COSMOS, SPACE). A full multiple-testing correction across the pre-registered family is therefore k = 9, α = 0.00556 (not α = 0.0167).

Observed SPACE p = 0.0146 → **does NOT beat k = 9 α = 0.00556.** The correct claim is:

- SPACE is an *exploratory directional signal* at uncorrected p = 0.0146.
- Under full family-wise Bonferroni k = 9, SPACE does not achieve significance.
- The Tier-B PARTIAL designation from integrator is correct because this signal is flagged for held-out replication via H-NEW-31.1.

**Required F-level edits in `incipit-time-space.md`:**

1. Replace "Sub (a) PASSES on SPACE at α=0.0167" with "Sub (a) SPACE achieves nominal p = 0.0146, which beats within-sub(a) α = 0.0167 but does NOT beat full-family k=9 α = 0.00556."
2. Replace the Joint Verdict table's "PASS (p=0.0146)" for sub-(a) with "NOMINAL — fails full-family Bonferroni."
3. Replace "Publishable SPACE result, null on TIME" in the final verdict paragraph with: "Exploratory directional SPACE signal (needs external replication via H-NEW-31.1); pre-registered joint fails; TIME direction reversed."
4. Update the frontmatter `status:` line from "PARTIAL — SPACE confirmed (Medinan concentration), TIME reversed" to "PARTIAL — SPACE nominal directional signal (p=0.0146, fails full Bonferroni k=9), TIME reversed, joint FAIL."

### B2 — MW-5 disclosure missing from finding-doc body

Current text says "Marker dictionaries built without classical-scholar review — might miss key TIME/SPACE stems" (Limits #2). This is a **MW-5 disclosure trigger**: the markers were proposer-chosen without classical-scholar cross-check, which is exactly the issue MW-5 (standing since audit-017) mandates. Per MW-5, the finding-doc should explicitly state that marker-dictionary pre-registration was *not* routed through classical-scholar before run, and classical-scholar verification is flagged for follow-up (which it is, items 1–3 of "Classical-scholar followup needed"). Make the MW-5 acknowledgment explicit rather than burying it in Limits.

### B3 — Clarify relationship to rejected AMEND-22

Per MASTER-FINDINGS-LEDGER.md line 446, AMEND-22 (7-class OATH expansion) was REJECTED because class-scheme expansion is prohibited as MW-2 amendment and has been redirected to H-NEW-31.2 as independent follow-up. The finding doc should note in its closing paragraph that:
- The 6-class scheme is *locked* for H-NEW-31.
- The 7-class OATH scheme lives in H-NEW-31.2 with fresh Bonferroni accounting and independent classical pre-reg.
- H-NEW-31.1 (held-out apocalyptic-oracular control) provides the *replication path* for the SPACE directional signal.

This gives the reader a clean three-step breadcrumb: exploratory H-NEW-31 → replication H-NEW-31.1 → operational-variant H-NEW-31.2.

## Framing items (F-level, non-blocking beyond B1)

### F1 — Early-Meccan TIME reversal should name a testable alternative

The finding doc notes that 9 of 14 TIME-incipits are Early Meccan (Q 81, 82, 84, 99 archetypes) but correctly refuses to post-hoc-rename. A **clean downstream task** would be: file a new hypothesis (H-NEW-31.3 or similar) with *pre-registered direction* "TIME-incipit concentrates in Early Meccan Nöldeke phase" tested on a held-out corpus (e.g., Muʿallaqāt apocalyptic-oracular fragments already in `data/baseline-corpora/raw/`). This isolates the Early-Meccan signal from the rejected Late-Meccan pre-reg.

(Non-blocking because integrator's H-NEW-31.1 apocalyptic-oracular held-out task already handles this path implicitly. But naming the direction explicitly would help.)

### F2 — Nöldeke phase source should be cited

`data/revelation-order.csv` provides the Nöldeke phase column. The finding doc should cite the edition/source of the Nöldeke chronology (there are multiple reconstructions: Nöldeke 1860, Blachère, Egyptian Standard). Currently it's referenced as "Nöldeke chronology" without edition identifier. Minor provenance gap.

## n-consistency check

- 114 surahs total → Meccan 86 + Medinan 28 = 114. OK.
- TIME 14 = Meccan 10 + Medinan 4. OK.
- SPACE 22 = Meccan 12 + Medinan 10. OK.
- All class totals reconcile across the period × class contingency table.
- Phase totals: Early 48 + Middle 21 + Late 21 = 90 Meccan (but frontmatter/"86 Meccan") — **discrepancy flagged**. The JSON shows 86 Meccan at period level but 48+21+21=90 at phase level. This is a 4-surah inconsistency.

Wait — reading more carefully: the Jonckheere-Terpstra table says "Medinan 24" but elsewhere Medinan is 28. And Early+Middle+Late = 90 vs Meccan total 86. Two inconsistencies:

1. JT phase table Medinan = 24 but period table Medinan = 28 (4 missing)
2. Early + Middle + Late = 90 but Meccan total = 86 (4 extra)

These may cancel (4 Meccan phase-misclassified as Medinan OR 4 Medinan phase-overlapping?) but the direction is unclear. **B4 (new blocking): tester should reconcile the phase counts to match period counts, or explain the 4-surah discrepancy explicitly.**

### B4 — Phase-count vs period-count n reconciliation

The Jonckheere-Terpstra phase-level counts (Early 48 + Middle 21 + Late 21 + Medinan 24 = 114) do not match the period-level counts (Meccan 86 + Medinan 28 = 114). Specifically, Meccan at phase level is 48+21+21 = 90, but Meccan at period level is 86; Medinan at phase level is 24 but period level is 28. The 4-surah swing between Meccan and Medinan assignments between the two tables requires either:

(a) A correction to one table (likely the Nöldeke phase-assigned edition treats 4 surahs differently from the Egyptian Standard period-assignment), OR
(b) An explicit note that the JT test uses Nöldeke phase assignment while the Fisher tests use Egyptian-Standard period assignment, with the cross-table divergence documented.

This is a structural auditability issue — a reader reproducing the numbers would be unable to unify the two counts without this disclosure.

## What survives / what doesn't

Survives cleanly:
- Primary pre-registered joint verdict FAIL (3-of-3 required, only 1 passes)
- TIME reversal honestly reported (no direction flip)
- Early-Meccan observation flagged as not-pre-registered
- Muqaṭṭaʿāt and basmala skipping correctly implemented
- Marker-priority alternative orderings tested in a disclosed sensitivity check

Requires F-level revision:
- SPACE "publishable" → "nominal / exploratory signal, pending H-NEW-31.1 replication"
- Framing of the joint table PASS label for (a) → NOMINAL
- MW-5 disclosure made explicit

Requires B-level revision:
- Phase-count vs period-count n-inconsistency (4-surah swing)

## Integrator implications

- **Tier-B PARTIAL designation stays** — this audit does not downgrade further. Under within-sub(a) Bonferroni the effect is "exploratory" rather than "confirmed", but it is still directionally present and pre-registered, and replication via H-NEW-31.1 is the correct next step.
- **H-NEW-31.1 priority should flag as SPACE-directional replication** (task #82). The held-out apocalyptic-oracular control is the correct adversarial check.
- **H-NEW-31.2 (task #83)** continues as independent 7-class OATH-expansion study with fresh pre-reg.
- **No M-framework implications** — incipit-classification is not part of any motif framework yet. Could feed M-6 (pericope-substrate) downstream if held-out replication confirms.

## MW-6 check

MW-6 (auditor-specified-protocol positive control) triggered only when auditor specifies a protocol that later breaks. Not triggered here — pre-registration and execution are tester-internal.

## Reproducibility

- Script: `scripts/h_new_31_incipit_class.py` — reviewed, clean
- Output: `findings/phase-b-hypotheses/csv/h-new-31.json` — arithmetic verified
- Seed: 20260413 — declared and honored
- Fisher exact, Jonckheere-Terpstra, shuffle null all reproducible from script

## Verdict summary

**NEEDS REVISION** (4 blocking items: B1 within-sub(a) Bonferroni, B2 MW-5 disclosure, B3 AMEND-22 relationship note, B4 phase-count reconciliation). HARKing 4/4 PASS. Primary pre-reg FAIL correctly declared. SPACE signal survives as exploratory only, pending H-NEW-31.1 replication. Tier-B PARTIAL stays.
