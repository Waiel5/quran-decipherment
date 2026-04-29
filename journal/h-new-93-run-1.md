# Journal — H-NEW-93 run 1

**Date**: 2026-04-17
**Specialist**: h-new-93-specialist (Opus 4.7, 1M context)
**Task**: NM-1 / OQ-3 — pre-register and execute 4-cell test of Q 29 + Q 30 vs other-الم and Meccan non-muqaṭṭāʿat baseline on test / historical-prophecy / Allah-control / eschatological cells.

## Pre-run decisions

- Chose to use **all 60 Meccan non-muqaṭṭāʿat surahs** as baseline (tightening from spec "50 Meccan-stratified"). Rationale: (a) strictly more null observations, (b) removes a seed-dependent sub-sampling analyst DoF, (c) per specialist-judgment-overrides-team-lead protocol with pre-reg lock BEFORE run. Logged in pre-reg garden-of-forking-paths.
- Used QAC morphology v0.4 STEM-ROOT tokens as operationalization (superior to surface-string for root-level matching).
- kwn root was restricted to lemma `kaAna` (past-tense copula) to avoid generic-copula inflation in historical-prophecy cell.
- Cell b reported in 3 forms: full 4-root, glb-only, glb+nSr (the latter two as pre-committed secondary robustness checks).

## Execution

- Wrote pre-reg (`h-new-93-q29-q30-subpattern-prereg.md`) with full Bonferroni YAML per PRE-REG-STANDARD-04.
- Wrote script (`scripts/h_new_93_q29_q30_subpattern.py`).
- Ran script with seed 20260417, 10,000 permutations.
- Computed SHA-256 of pre-reg for tamper-evidence.

## Results

See `h-new-93-q29-q30-subpattern.md` for the full write-up.

Headline: **composite verdict = NULL-full-target-pattern-rejected.**

- Cell (a) TEST: p=0.9353 (REVERSE direction; Q29+30 lower than Meccan)
- Cell (b) HIST full: p=0.2900 (NULL, though visible higher target)
- Cell (c) Allah control: p=0.0638 (CONTROL-CONFIRMED marginal)
- Cell (d) Eschato control: p=0.9338 (CONTROL-CONFIRMED)
- Secondary glb+nSr: p=0.0362 WEAK-PASS-DIRECTED single-test-only (not Bonferroni-survivable)

MW-5 positive control: PASS for cells (a)+(b) (other-الم does NOT show elevation; test has specificity). Cell (c) MW-5 shows other-الم is Allah-denser than Meccan non-muq (Q2 and Q3 are Medinan), which is an expected artifact and does not break the study.

## Honest reflection

I went in with a mild expectation that the hypothesis would find SOMETHING (the thematic eyeball impression seemed strong). It did not. The true signal — a 3-token glb cluster in Q 30 driving the Roman-prophecy — is real but LOCAL (to Q 30), not a SUB-CLASS-DEFINING feature.

The opening of Q 29 ("a-ḥasiba al-nās an yutrakū an yaqūlū āmannā wa-hum lā yuftanūn") is thematically distinctive but produces only 4 ftn tokens in the whole surah, insufficient to lift density above Meccan baseline.

**Lesson for the project**: eyeball-identified opening-theme distinctiveness does NOT imply surah-level lexical-density distinctiveness. Cross-finding-008's residual 2 surahs are best interpreted as "ordinary-Meccan with distinctive openings", NOT a second functional sub-class.

## Potential follow-ups (not executed)

- H-NEW-93.1: narrow-window (v1-3) test using surface strings (different operationalization). LOW PRIORITY.
- H-NEW-93.2: scattered-sub-cluster test — do OTHER muqaṭṭāʿat surahs have test-and-prophecy themes in v1-3 that we missed? Could reconnect to cross-finding-008 residual architecture.

## Discipline checklist

- [x] PRE-REG-STANDARD-04: Bonferroni-4 in YAML frontmatter (bonferroni_k=4, alpha_bon=0.0125, bonferroni_family=h-new-93-sub-pattern)
- [x] Direction pre-registered BEFORE viewing results
- [x] Single-test α=0.05 cap applied (post-hoc-noticed sub-cluster)
- [x] Verdict ceiling = PASS-DIRECTED documented
- [x] Publish NULL with equal prominence as PASS — done in findings file
- [x] MW-5 positive control: PASSES (test has specificity)
- [x] Garden-of-forking-paths: post-hoc eyeball origin DISCLOSED in pre-reg
- [x] Specialist-judgment-overrides-team-lead: "all 60 Meccan non-muq" vs "50 stratified" LOGGED and JUSTIFIED before run
- [x] Pre-reg SHA-256 stored in JSON for tamper-evidence

## Output files

- `findings/phase-b-hypotheses/h-new-93-q29-q30-subpattern-prereg.md`
- `scripts/h_new_93_q29_q30_subpattern.py`
- `findings/phase-b-hypotheses/csv/h-new-93.json`
- `findings/phase-b-hypotheses/h-new-93-q29-q30-subpattern.md`
- `journal/h-new-93-run-1.md` (this file)
