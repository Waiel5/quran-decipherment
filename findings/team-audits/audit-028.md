---
audit_id: audit-028
target_finding: classical-iltifat-catalog
target_file: findings/phase-b-hypotheses/classical-iltifat-catalog.md
target_author: classical-scholar
auditor: skeptical-auditor
phase: B
date: 2026-04-13
verdict: PASSED WITH MINOR REVISIONS (n-count discrepancy; syn-tag discrepancy)
note: deliverable-type audit (not a hypothesis-test audit) — evaluating catalog provenance and downstream-tagging integrity
---

# audit-028 — classical iltifāt catalog (deliverable)

## Executive verdict

**PASSED WITH MINOR REVISIONS.** This is a classical-scholarship deliverable, not a hypothesis-test finding. Evaluation criteria are: (a) classical-source attribution integrity, (b) provenance-tag honesty, (c) downstream-propagation hygiene, (d) arithmetic self-consistency.

On (a), (b), (c) this catalog sets the gold standard for the project: the 2026-04-12 AMEND-12 retag memo is a model MW-5-compliant verbatim-confidence pass. The classical-scholar has (1) pre-emptively retracted nawʿ-number claims after noticing contradictions across journal files, (2) explicitly forbidden downstream papers from emitting specific nawʿ numbers until physical verification closes, (3) distinguished HIGH/MEDIUM/LOW confidence layers on typology / per-surah aggregation / syn-tagged entries separately, and (4) withdrawn the Arabic phrase *yunshiṭu l-sāmiʿa wa-yujaddidu nashāṭah* from publication. This is textbook anti-fabrication discipline.

On (d), there are **two arithmetic discrepancies** that warrant minor revision before integrator propagates this catalog further.

## Blocking revisions

### B1 — N-surah and event-count off-by-one(-ish)

Catalog self-reports (line 34 + line 105-107):
- "45 surahs, 117 events"
- "Mean count per catalogued surah: 2.6"

Direct row-count from the TSV block (lines 57-102):
- **46 rows** (surahs 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 50, 55, 56, 67, 76, 114)
- **122 events** (sum of counts column)
- Mean = 2.65

Discrepancy: **1 extra surah and 5 extra events** vs declared header.

Downstream finding `h-new-2-iltifat-catalog-rho.md` reports "43 out of 45 catalog surahs" and then explicitly excludes 3 (surahs 5, 9, 13), which gives 45 − 3 ≠ 43 (would be 42), but 46 − 3 = 43 which matches. **So downstream script actually read 46, not 45.** The catalog header count is wrong relative to the TSV block; the downstream consumer is self-consistent with the TSV block.

**Required fix:** update the catalog frontmatter / body to state "46 surahs, 122 events, mean 2.65 per catalogued surah." Alternatively, if 45/117 was meant to reflect a de-duplicated count (two rows for the same surah merged?), call out the methodology explicitly; otherwise, correct the header.

### B2 — syn-tagged entry count

Catalog §6 and frontmatter both state "21 of 45 catalog surahs carry `source_tag = syn`." Counting from the TSV block, the entries tagged `syn` are: 9, 13, 18, 22, 24, 26, 28, 29, 31, 32, 34, 37, 40, 41, 43, 50, 55, 56, 67, 114. That is **20 surahs, not 21.**

Combined with the total n-count issue above, the ratios should be re-reported as "20 of 46" rather than "21 of 45." Minor but needs to match.

(If I've miscounted the syn tags and there's actually a 21st, the catalog should show it explicitly — but I see only 20 in the block as written.)

## Non-blocking strengths (worth noting for the integrator's ledger)

1. **MW-5 compliance modeled**: proactive acknowledgment that marker-dictionaries / nawʿ-number recall were proposer-generated without a physically-verified edition in hand.

2. **Verbatim-confidence layering is correct**:
   - HIGH: cross-source stable balāgha typology
   - MEDIUM: per-surah aggregation (working-notes distillation)
   - LOW: Zarkashī-only exemplars, syn-tagged entries, the *tansheeṭ al-sāmiʿ* Arabic phrase
   - PENDING: nawʿ numbers themselves

3. **Downstream-caveat frontmatter** explicitly instructs downstream findings to re-tag or drop nawʿ numbers until Phase-2 physical verification completes. This is the correct shield against "Burhān nawʿ 51 Ḥashr fabrication"-class propagation failures.

4. **NaN-not-zero instruction for missing surahs** (§2 "Zero ≠ absent") is the correct statistical treatment.

5. **Full-vs-Z+S-only sensitivity protocol** pre-specified in §6. This is exactly the two-mode protocol that H-NEW-2 × iltifat-rho (line 80-88) then uses — and notably, the effect *strengthens* on the high-rigor subset, which is a favorable sensitivity outcome.

6. **Pre-registration of ρ sign BEFORE join** (§4.3) is the right discipline.

## Downstream-consumer check

Checked `h-new-2-iltifat-catalog-rho.md`:
- Cites catalog as MEDIUM classical-synthesis rigor ✓
- Uses NaN-respected join (excludes non-catalog surahs, not imputes zero) ✓
- Runs two-mode sensitivity (full n=43 + syn-dropped n=25) ✓
- Effect strengthens on high-rigor subset (ρ magnitude up) — catalog quality not artifact ✓
- Reports REVERSE-SIGN PRE-REG REFUTED verdict honestly — no sign flipping ✓

Downstream propagation is clean.

## Nawʿ-PENDING handling check

Cross-reference with downstream finding lines:
- `h-new-2-iltifat-catalog-rho.md` frontmatter: `rigor_tag: classical-synthesis-anchored # NOT Suyūṭī-direct` ✓
- No direct emission of "nawʿ 47" or "nawʿ 56" as standalone claims; body text uses "classical doctrine" framing ✓

The retag guardrails are being respected by the one downstream finding I spot-checked. Integrator should spot-check the remaining downstream users (H-CLASSIC-37, M-6 CANDIDATE validation leg) when their full finding-docs are filed.

## MW-framework assessments

**MW-5**: This catalog is itself a canonical exemplar of MW-5 discipline (disclosure-to-auditor of verbatim-confidence status). The AMEND-12 retag memo is the cleanest MW-5 compliance seen in the project to date.

**MW-6**: Not triggered (auditor-specified protocol not relevant — this is a classical-scholarship deliverable).

**M-5 (classical-doctrine decomposition)**: This catalog *feeds* potential M-5 instances downstream — the six-type Zarkashī typology is itself a decomposition of classical doctrine into testable sub-claims. Not a new M-5 instance on its own.

**M-6 CANDIDATE (pericope-substrate)**: Listed as downstream validation leg. Catalog integrity is a prerequisite for M-6 validation. Minor arithmetic fixes (B1, B2) should propagate there before M-6 CANDIDATE → CONFIRMED.

## Classical-source integrity

Zarkashī's *Burhān* has 47 anwāʿ total (Abū l-Faḍl Ibrāhīm 1957 edition). The previously-attributed "nawʿ 47" would be the terminal chapter, implausible for iltifāt. Classical-scholar correctly retracted. 

Suyūṭī's *Itqān* has 80 anwāʿ in the standard division; "nawʿ 56" vs "nawʿ 58" vs other numbers across the project's own documentation is internally contradictory. Classical-scholar correctly retracted.

Ibn al-Athīr *Mathal Sāʾir* is listed as secondary cross-check only — appropriate.

The six-type typology itself is cross-source stable (Zarkashī + Suyūṭī + Ibn al-Athīr + Abdel Haleem 1992 BSOAS + Sohaib Saeed) — HIGH confidence is correct.

## HARKing 4-test (adapted for deliverable-type audit)

| Test | Verdict | Evidence |
|---|---|---|
| 1. Non-counting of weaknesses | **PASS** | All LOW-confidence entries explicitly flagged at four layers (§1-§6 + frontmatter). |
| 2. Pre-existing mechanism | **PASS** | Six-type typology is ancient balāgha tradition, not invented for this project. |
| 3. Direction-locked protocol | **PASS** | §4.3 pre-registration-of-ρ-sign rule is baked in. |
| 4. Refusal to rename/retrofit | **PASS** | Retracted nawʿ-47/56 claims rather than re-framing. Withdrew the Arabic phrase rather than salvaging. |

## Verdict summary

**PASSED WITH MINOR REVISIONS.** Catalog is an exemplary MW-5-compliant classical-scholarship deliverable. Two minor arithmetic discrepancies (B1 n=46/122 not 45/117; B2 syn=20/46 not 21/45) require a header update. Downstream propagation to h-new-2-iltifat-catalog-rho.md is clean.

Recommended integrator action: accept catalog as-is pending classical-scholar's ~5-minute header fix; do not block downstream findings on this audit.

## Reproducibility

- Row-count + event-count script: `python3 -c` inline (see audit-028 execution log via skeptical-auditor work journal)
- Cross-referenced files: `MASTER-FINDINGS-LEDGER.md`, `h-new-2-iltifat-catalog-rho.md`
- Verbatim-confidence layering verified against journal/balagha-run-1.md:57, docs/master-index.md:20 divergence (flagged in catalog frontmatter itself)
