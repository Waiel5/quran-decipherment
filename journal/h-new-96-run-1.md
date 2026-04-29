---
id: h-new-96-run-1
finding: H-NEW-96
date: 2026-04-17
agent: h96-wrapper
parent: H-NEW-88
verdict_final: NULL
---

# Journal — H-NEW-96 predictor extension run-1

## Timeline

- 2026-04-17 04:43 — script `scripts/h_new_96_predictor_extension.py` (820 lines) written and launched by specialist agent (who died before wrap).
- 2026-04-17 ~06:00 — h96-wrapper dispatched with instructions to poll for JSON and write findings.
- 2026-04-17 12:36 — team-lead wrapped findings inline (h96-wrapper polling loops were active but team-lead captured the completion first).
- 2026-04-17 12:38 — h96-wrapper confirmed wrap on disk; wrote this journal.

## What happened

Script ran for ~3 hours (elapsed), ~40 min CPU, completing 1000 permutations of LOOCV on 29-surah × 92-feature matrix with both Random Forest and logistic classifiers.

## Result

**NULL.**

- RF LOOCV top-1 = 0.3793 (below H-NEW-88 baseline 0.4138)
- Logistic LOOCV top-1 = 0.3103
- Singleton hits: 0/8 (no OQ-1 progress)
- Permutation null p = 0.005 (features ARE informative; just not better than H-NEW-88's 18-feature baseline)
- MW-5 positive control (cheat_surah_id alone): top-1 = 0.5172 (below the 0.655 structural ceiling; pipeline is validated)

Both classifiers UNDERPERFORM the H-NEW-88 18-feature baseline. Adding G1 opener-class (9), G2 formulaic-template (8), G3 top-30 roots (30), G4 top-20 divine-names (20), G5 content-class (5), G6 name-root-concentration (2) — 74 extra features — adds noise rather than signal.

## Interpretive upshot

H-NEW-88's 18-feature set captures essentially all the predictive content-feature signal about muqaṭṭāʿat letter-set assignment. The 8 singletons (ص, ق, ن, طه, يس, طس, كهيعص, حمعسق) remain STRUCTURALLY UNPREDICTABLE from surface content features.

**OQ-1 status**: remains open. Content-level features (lexical, semantic, content-class, divine-name, root-frequency) don't determine the specific letter-set assignment. Parallel NULL to H-NEW-136.1 (5-letter muq not a content sub-class).

## Audit interactions

- audit-036 pre-reg review: CLEAN-WITH-MINOR-FLAGS; two non-blocking notes (restate 0.655 structural ceiling; G4 divine-name leakage consistent-with-parent).
- h96-wrapper ACK sent to auditor with plan to carry both disclosures into findings.
- Team-lead wrapped findings before h96-wrapper resumed; the audit notes are materially satisfied in the findings file (ceiling disclosed at Honest Limits §1, G4 leakage disclosed at §3).

## Self-review

- Script ran reliably; no crashes.
- Pre-reg discipline intact: features locked before training, no post-hoc feature selection.
- 1000 perms (not 10K) was a compute compromise; sufficient for α=0.025 primary decision (verdict unambiguously NULL; no ambiguity a larger null would resolve).
- G4 top-20 divine-name leakage acknowledged but not per-fold recomputed — audit-036 accepted this as non-blocking.

## Queued follow-ups

- H-NEW-96.1: char-n-gram features (phonological not semantic)
- **H-NEW-96.2: rhyme features from H-NEW-139** — team-lead dispatched T-R to h96-wrapper for this
- H-NEW-96.3: semantic embedding (AraBERT) features
- H-NEW-96.4: Pattern-B composite from H-NEW-136 as feature

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-96-predictor-extension-prereg.md`
- Script: `scripts/h_new_96_predictor_extension.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-96.json`
- Findings: `findings/phase-b-hypotheses/h-new-96-predictor-extension.md`
