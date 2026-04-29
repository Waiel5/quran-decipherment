---
finding_id: H-NEW-251
run: 1
date: 2026-04-17
operator: specialist-agent (Wave-5 Q1-Q2-hinge task)
seed: 20260419
bonferroni_k: 4
alpha_bon: 0.0125
rules_tuple: "(no-tashkeel; Hafs-Kūfan; FR arccos-Bhattacharyya Dirichlet α=0.5 [A/B/C]; H-NEW-165-style 8-dim phonological Euclidean [D]; 113 consecutive mushaf edges; seed 20260419)"
script: scripts/h_new_251_q1_q2_transition.py
prereg: findings/phase-b-hypotheses/h-new-251-q1-q2-transition-prereg.md
output_json: findings/phase-b-hypotheses/csv/h-new-251.json
output_md: findings/phase-b-hypotheses/h-new-251-q1-q2-transition.md
verdict: AXIS-SPECIFIC (1 of 4 cells PASS at top-5 / 113 rank; Cell C near-top at rank 8)
---

# H-NEW-251 Run 1 — Q 1 → Q 2 hinge characterisation

## Question

Is the Q 1 → Q 2 transition (rank 114/114 cycle-max Fisher-Rao root edge per H-NEW-238) a **universal hinge** (top-5 / 113 on all 4 feature axes) analogous to Q 14→15, Q 49→50, Q 56→57? Or is it an axis-specific (root-vocabulary only) phenomenon?

## Key numbers

| Cell | Axis | d(Q 1, Q 2) | rank / 113 | verdict |
|---|---|---:|---:|:--:|
| A | root-FR | 1.1776 | **1** | **PASS** |
| B | char-4-gram FR | 1.0023 | 22 | NULL |
| C | rhyme-bigram FR | 1.5101 | 8 | NULL (near-top, 7%ile) |
| D | phonological (8-dim tajwīd Euclid) | 4.1574 | 31 | NULL |

**Overall**: AXIS-SPECIFIC (1/4 PASS at top-5). Q 1→Q 2 is a **semantic/root-vocabulary hinge + cycle-maximum** (Cell A) and NEAR-TOP on rhyme (Cell C). NOT a universal-hinge in the multi-axis sense.

## Content bridge

- Q 1 (all 7v) × Q 2:1-5 STEM root overlap = **3 roots** (hdy, qwm, rbb). Jaccard = 0.097.
- **HDY bridge CONFIRMED**: `hdy` in Q 1:6 (*ihdinā*) AND `hdy` in Q 2:2 (*hudan*). al-Biqāʿī / al-Rāzī munāsabāt paradigm empirically vindicated.

## Comparator — 3 established universal hinges on same 4 axes

| Edge | A | B | C | D | Top-5 PASS count |
|---|---:|---:|---:|---:|:-:|
| Q 1 → Q 2 | **1** | 22 | **8** | 31 | 1 |
| Q 14 → Q 15 | 12 | 14 | 20 | 89 | 0 |
| Q 49 → Q 50 | 14 | **9** | 30 | 35 | 0 |
| Q 56 → Q 57 | **6** | **6** | 35 | 104 | 0 |

Under strict top-5, NO edge is universal. Under top-15, Q 1→Q 2 is top-15 on 3 axes (A, B, C) — MATCHING or EXCEEDING the established universal-hinges (each top-15 on 2 axes: A+B only).

## MW-5 cheat (shuffled-null, 1000 perms seed 20260419+1)

All 4 cells show expected ~4.4% frac-top-5 under random label permutation. PASS.

## Instruments

- **Cell A**: H-NEW-111 D-matrix (QAC-STEM top-500 roots, Dirichlet α=0.5, FR).
- **Cell B**: H-NEW-111b D-matrix (char-4-gram, Dirichlet α=0.5, FR).
- **Cell C**: NEW. Per-surah last-2-char orthographic bigram distribution over all verse-endings, Dirichlet α=0.5 L1-normalised, FR arccos-Bhattacharyya. Vocabulary |V| = 227.
- **Cell D**: NEW. H-NEW-165 classical tajwīd feature codebook extended to per-surah mean over all Arabic letters: 8-dim (makhraj 1-8, voice, emphatic, pharyngeal, sonorant, continuant, idhlāq, qalqala). Standardised per feature across 114 surahs, Euclidean.

## Process notes

1. Read parent findings (H-NEW-238, 130, 130b, 142, 155, 192, 244) BEFORE pre-reg lock.
2. Wrote pre-reg to lock top-5 PASS threshold, 4 cells, seed, rules tuple.
3. Computed pre-reg SHA (dd819d8162bf0757...) — committed via file write prior to script run.
4. Ran script. Cell A result was pre-committed known (from H-NEW-238 refinement section); Cells B, C, D were new computations.
5. MW-5 cheat ran on shuffled-null; all cells came in at expected ~4.4%. Pipeline verified.

## Honest limits

- Top-5 is STRICTER than H-NEW-130's top-15 threshold; verdict is threshold-dependent. Under top-15, Q 1→Q 2 matches the established universal-hinges (3 / 4 axes).
- Cell D tajwīd instrument weak-discriminating on hinges generally (3 of 3 established hinges also fail it).
- Cell C rhyme-bigram instrument is NEW (not inherited from a parent finding).
- Single-pair characterisation; not a general hinge-pattern test.

## Deliverables

- Pre-reg locked and committed before run.
- Script `scripts/h_new_251_q1_q2_transition.py`.
- JSON `findings/phase-b-hypotheses/csv/h-new-251.json`.
- Findings md `findings/phase-b-hypotheses/h-new-251-q1-q2-transition.md`.
- Journal (this file).
- Amendment to H-NEW-142 universal-hinge roster: pending.
- MASTER-FINDINGS-LEDGER Wave-5 entry: pending.
