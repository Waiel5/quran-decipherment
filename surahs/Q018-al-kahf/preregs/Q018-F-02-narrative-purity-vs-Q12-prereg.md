---
finding_id: Q018-F-02
title: "Q 18 narrative-purity rank vs Q 12 — multi-narrative vs single-narrative archetypes"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 18002
n_perm: 0
bonferroni_k: 1
alpha_raw: 0.05
direction: Q 18 has HIGH narrative-purity (top quartile), but LOWER than Q 12 (single-narrative archetype)
---

# Q018-F-02 — Narrative-purity rank: Q 18 vs Q 12

## Hypothesis

Q 12 Yūsuf is the corpus's single-narrative archetype (rank 1/114 by narrative-purity per Q012-F-01 CONFIRMED). Q 18 al-Kahf is the corpus's four-narrative archetype. The pre-registered hypothesis:

- **Direction A (LOCKED)**: Q 18 ranks in the **top 25% of corpus** on the narrative-purity index from Q012-F-01 (i.e., rank ≤ 28/114).
- **Direction B (LOCKED)**: Q 18 ranks **lower than Q 12** on the same index.

The intuition: 4-narrative is still narrative-rich (top quartile expected) but lower than the single-protagonist single-narrative continuous-arc of Q 12.

## Operational definition

Use the Q012-F-01 narrative-purity index, locked at:

**Narrative-marker set** (Arabic, no-tashkeel, word-boundary regex):
- Speech reporters: قال، قالت، قالوا، قلنا، قل
- Sequence connectives: فلما، ولما، إذ، إذا، ثم، بينما
- Existence/state: كان، وكان
- Motion/event verbs: جاء، جاءت، جاءوا، ذهب، ذهبوا، أتى، أتوا
- Visual narrative: رأى، رأيت، رأوا
- Sending/dispatching: أرسل، بعث

**Per-surah metrics**:
1. `frac_narrative_verses` = (verses containing ≥1 marker) / (total verses)
2. `marker_density_per_word` = (total marker tokens) / (total words)
3. `narrative_purity_score` = 0.5 · frac_narrative_verses + 0.5 · (marker_density / 0.30)

This pre-reg uses **the EXACT same definition** as Q012-F-01 — no modifications. We replicate the Q012-F-01 ranking and ask Q 18's rank.

## Test statistic

- **Primary**: Q 18's rank on `frac_narrative_verses` (1 = highest in corpus).
- **Secondary**: Q 18's rank vs Q 12's rank.

## Success / Failure

- **Direction A succeeds**: Q 18 rank ≤ 28/114 on `frac_narrative_verses`.
- **Direction B succeeds**: Q 18's rank > Q 12's rank (i.e., Q 12 is more narrative-pure).
- **Combined CONFIRMED**: both directions succeed.
- **NULL**: Q 18 rank > 28 OR Q 18 ≥ Q 12 in narrative-purity.

## Rules-tuple

`(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` — IDENTICAL to Q012-F-01.

## SHA256 lock

Computed at runtime, embedded in JSON output.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q018_F_02_narrative_purity.py`.
- JSON: `csv/Q018-F-02.json`.
- Findings: `06-novel-findings.md` Q018-F-02 section.
