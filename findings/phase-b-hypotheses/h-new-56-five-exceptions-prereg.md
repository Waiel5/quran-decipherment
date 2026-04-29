---
id: H-NEW-56
title: Five-exception analysis of muqaṭṭaʿāt-opened surahs lacking kitāb/qurʾān in v1-3
phase: B
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (BEFORE running expanded-marker hypergeometric)
parent: H-NEW-53 (24/29 narrow PASS at p ≈ 10⁻¹²)
bonferroni_family: 2026-04-15-Wave-Muqattaat-Five-Exceptions
bonferroni_k: 3
alpha_bon: 0.0167
rules_tuple: (no-tashkeel; substring search on verses 1-3; standard Arabic forms of roots k-t-b, q-r-ʾ, q-l-m, s-T-r, dh-k-r, A-y-A, n-w-r, k-l-m, h-d-y, w-H-y/n-z-l)
seed: 20260416
---

# [[h-new-56-five-exceptions|H-NEW-56]] — Five-Exception Analysis (Pre-registration)

## Question

[[h-new-53-muqattaat-book-reference|H-NEW-53]] found 24/29 muqaṭṭaʿāt-opened surahs reference kitāb/qurʾān in v1-3 (p ≈ 10⁻¹²).
The 5 exceptions are Q 19 (Maryam), Q 29 (al-ʿAnkabūt), Q 30 (al-Rūm), Q 42 (al-Shūrā), Q 68 (al-Qalam).

**Three sub-questions:**

1. (**Descriptive**) What thematic / chronological / structural feature distinguishes the 5 exceptions from the 24?
2. (**Compensating-marker test**) Do the 5 exceptions contain SEMANTICALLY ADJACENT writing/revelation markers (qalam, satr, dhikr, āyāt, nūr, kalām, hudā, wahy/anzal) in v1-3?
3. (**Extended-marker hypergeometric**) If we EXPAND the marker set, what is P(X ≥ k_observed) under random selection? Does the muqaṭṭaʿāt → revelation-marker enrichment STRENGTHEN, WEAKEN, or VANISH?

## Pre-registered tests (3-cell family)

### Cell 1 — Compensating writing-cluster (kitāb / qurʾān / qalam / satr)

Add q-l-m (qalam, pen) and s-T-r (satr, line/inscription) to the narrow set.
Pre-committed expectation: Q 68 will be RECLASSIFIED as PASS (because v1 = "wa-l-qalam wa mā yasṭurūn"). Other 4 exceptions unchanged.
Test: hypergeometric P(X ≥ k_writing | n=29, K=K_writing, N=114).

### Cell 2 — Full extended-marker set (10-marker)

Markers: kitāb, qurʾān, qalam, satr, dhikr, āyāt, nūr, kalām, hudā, wahy/anzal/nazzala.
Pre-committed expectation: count rises from 24 → 27 (Q 19 via dhikr v2; Q 42 via yūḥī v3; Q 68 via qalam/yasṭurūn v1). Q 29 and Q 30 remain exceptions even under the full 10-marker set.
Test: hypergeometric P(X ≥ k_ext | n=29, K=K_ext, N=114).

### Cell 3 — Per-exception thematic classification

For each of Q 19, 29, 30, 42, 68, classify the v1-3 thematic opener into one of:
- prophetic-narrative (e.g., zakariyyā / Mary)
- existential-test (e.g., faith without trial)
- historical-eschatological (e.g., Roman defeat)
- cosmic-revelation (e.g., wahy formula)
- oath-based (e.g., qasam by qalam)

Pre-committed claim: the 5 exceptions are HETEROGENEOUS in opener-type — no single mechanism explains all 5. If they cluster on a single feature (e.g., all Late Meccan, all in a single Nöldeke window, or all share a single literary genre), report that as a positive finding. If heterogeneous, report honestly.

## Decision rules

- Cell 1 / Cell 2 PASS if Bonferroni-corrected p < 0.0167 (α/3).
- Cell 3 is descriptive; its "PASS" is honest disclosure of whether 1, 2, 3, 4, or 5 of the exceptions cluster on a single feature.

## Garden-of-forking-paths disclosure

The [[h-new-53-muqattaat-book-reference|H-NEW-53]] specialist already noted in [[h-new-53-muqattaat-book-reference|H-NEW-53]].md that:
- Q 68 has qalam + satr in v1 (semantically adjacent).
- Q 19 has dhikr in v2 + Kitāb-reference appearing at v12 ("yā Yaḥyā khudh al-kitāb…") and v16 ("wa-dhkur fī al-kitāb Maryam…").
- Q 42 has wahy (yūḥī) in v3 and "qurʾānan ʿarabiyyan" in v7.
- Q 29 v2 = test/fitnah theme (NO compensating revelation marker visible).
- Q 30 v2 = "ghulibat al-rūm" (Romans defeated; NO compensating revelation marker).

Pre-committed honest claim: even under the most generous extended-marker definition, **at least 2 surahs (Q 29, Q 30) will remain genuine exceptions**. The [[h-new-56-five-exceptions|H-NEW-56]] spec accepts this and tests the strength of the EXTENDED enrichment (which is weaker than narrow because the K (positives in baseline) grows).

## Data + outputs

- Input: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`, `/Users/grey/Downloads/quran/data/revelation-order.csv`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-56.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-56-five-exceptions.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-56-run-1.md`

## Status

PRE-REGISTERED 2026-04-15.
