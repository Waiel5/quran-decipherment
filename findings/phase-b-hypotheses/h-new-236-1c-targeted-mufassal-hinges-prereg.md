# [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] — Targeted mufaṣṣal-short hinge injection pre-registration

```yaml
finding_id: h-new-236-1c
title: "Targeted mufaṣṣal-short hinge injection on the top-50 global scaffold — test whether R12a is omitted terminal hinges or a distinct terminal mechanism"
parent: h-new-236-1a (NEAR-GENERATIVE-CLOSURE; top-50 closes L_path + ḥawāmīm, leaves only R12a = mufaṣṣal-short within-block cost-excess)
grandparent: h-new-236-1 -> h-new-236 -> cross-finding-020 (the complete equation)
siblings:
  - H-NEW-255 (Juzʾ 30 mini-geodesic open path; identifies top internal consecutive jumps)
  - H-NEW-130 / 130b / 130c (global hinge architecture)
  - H-NEW-236.1a (top-30 / top-50 hinge extension)
date: 2026-04-18
specialist: autonomous (H-NEW-236.1c)
seed: 20260419
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq constraints + TOP-50-GLOBAL-HINGE-PRESERVATION + TOP-JUZ30-INTERNAL-HINGE-PRESERVATION for m ∈ {5, 10})"
bonferroni_k: 2
alpha_family: 0.05
alpha_bon: 0.025
cells:
  - cell_a_top50_plus_j30_top5: preserve H-NEW-236.1a top-50 global hinges plus the 5 largest internal consecutive jumps inside Q 78-114; direction — materially reduce the remaining mufaṣṣal-short mean-gap vs H-NEW-236.1a top-50 by at least 50%
  - cell_b_top50_plus_j30_top10: preserve H-NEW-236.1a top-50 global hinges plus the 10 largest internal consecutive jumps inside Q 78-114; direction — move empirical L_mufaṣṣal-short inside the simulator 95% CI and thereby close Block-χ² / reach 4-of-4 overall if R12a is pure hinge-truncation
n_simulations: 1000
n_random_null: 1000
```

## 1. Hypothesis

**H0 (distinct terminal mechanism):** the surviving `R12a` residual from
[[h-new-236-1a-extended-hinges|H-NEW-236.1a]] is NOT explained by omitted high-jump edges inside
mufaṣṣal-short. Even after preserving the strongest internal Juzʾ-30
consecutive jumps on top of the successful top-50 scaffold, empirical
`L_mufaṣṣal-short` remains outside the simulated 95% CI and `Block-χ²`
stays outside.

**H1A (parsimonious omitted-hinge explanation):** adding the top-5
internal Juzʾ-30 hinges closes at least 50% of the remaining
`L_mufaṣṣal-short` mean-gap from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50.

**H1B (full omitted-hinge explanation):** adding the top-10 internal
Juzʾ-30 hinges moves empirical `L_mufaṣṣal-short` inside the simulated
95% CI, `Block-χ²` passes, and the full simulator reaches 4/4.

Interpretation rule:
- If cell B reaches 4/4, then `R12a` is best read as a **terminal
  hinge-truncation artifact**, not a distinct M1.4 mechanism.
- If cell A and cell B both materially improve but still fail on
  `L_mufaṣṣal-short`, the terminal block likely carries a **non-hinge
  organizing pressure**.
- If neither cell materially improves, the [[h-new-255-juz30-mini-cycle|H-NEW-255]] internal-jump
  structure is **descriptive only**, not the causal driver of R12a.

## 2. Motivation and parent context

[[h-new-236-1a-extended-hinges|H-NEW-236.1a]] established:

- top-30 and top-50 both move empirical `L_path` **inside** the
  simulated 95% CI.
- top-50 fully closes **ḥawāmīm**.
- the only surviving miss is:

> **R12a = mufaṣṣal-short (Q 78-114) within-block cost-excess**

The decisive pre-run facts already on disk are:

1. **Top-50 contains zero internal mufaṣṣal-short edges.** The first
   such edge is **Q 78→79 at global rank 73**.
2. **[[h-new-255-juz30-mini-cycle|H-NEW-255]]** showed Juzʾ 30 is a **mini-geodesic open path** and
   identified its top internal consecutive jumps:
   `Q 78→79`, `79→80`, `88→89`, `83→84`, `80→81`, `89→90`,
   `84→85`, `98→99`, `82→83`, `97→98`, ...
3. Under [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50, empirical `L_mufaṣṣal-short = 16.514906`
   vs simulator mean `15.619384`, leaving a residual mean-gap of
   **0.895522 FR units**.

This makes the next mechanistic test unusually clean:

- keep the **successful top-50 scaffold fixed**
- add only a **small number of internal Juzʾ-30 hinges**
- ask whether the residual disappears

If it does, OQ-15 is effectively closed by a parsimonious extension of
M1.3. If it does not, the terminal block is governed by something other
than omitted hinge enumeration.

## 3. Locked hinge sets

Base scaffold for **both** cells:

- the **top-50 global consecutive Fisher-Rao hinges** from
  [[h-new-236-1a-extended-hinges|H-NEW-236.1a]], unchanged

Additional internal Juzʾ-30 hinges are locked to the [[h-new-255-juz30-mini-cycle|H-NEW-255]] ranking
of canonical consecutive edges inside Q 78-114:

### Cell A — top-50 + Juzʾ-30 top-5

`(78,79), (79,80), (88,89), (83,84), (80,81)`

### Cell B — top-50 + Juzʾ-30 top-10

Cell A plus:

`(89,90), (84,85), (98,99), (82,83), (97,98)`

All ten added hinges are **within** the mufaṣṣal-short block; none are
cross-block.

Global-rank disclosure (locked pre-run):

| Edge | Global rank |
|---|---:|
| Q 78→79 | 73 |
| Q 79→80 | 75 |
| Q 88→89 | 79 |
| Q 83→84 | 80 |
| Q 80→81 | 81 |
| Q 89→90 | 82 |
| Q 84→85 | 84 |
| Q 98→99 | 85 |
| Q 82→83 | 86 |
| Q 97→98 | 87 |

## 4. Generative procedure (delta from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]])

Start from `scripts/h_new_236_1a_extended_hinges.py`. Locked changes:

1. **Base scaffold**: use the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 hinge set for both
   cells.
2. **Add m internal Juzʾ-30 internal hinges**, where `m ∈ {5, 10}` per
   the locked lists in §3.
3. **Cross-block vs within-block rule unchanged**:
   - cross-block hinges are enforced by initialization order
   - within-block hinges are enforced by hinge-respecting 2-opt
4. **SA schedule unchanged**: `T_HOT=0.05`, `T_COLD=0.001`,
   `SA_ITERS=200`
5. **N_sim=1000**, **N_random=1000**, **seed=20260419**
6. **MW-HINGE**: all simulated orderings must satisfy all preserved
   hinges by construction.

No hotter schedule, no alternative block partition, no top-K sweep
beyond `{5, 10}` is allowed in this run.

## 5. Observables

Primary mechanistic observable:

- **O1 `L_mufaṣṣal-short`** = total Fisher-Rao cost over positions
  Q 78..Q 114

Simulator-health / equation-closure observables:

- **O2 `L_path`**
- **O3 `W_wrap`**
- **O4 `Block-χ²`** over `{ṭiwāl, ḥawāmīm, mufaṣṣal-short}`
- **O5 `L_tail_91_114`**

For continuity with [[h-new-236-generative-simulator|H-NEW-236]] / 236.1 / 236.1a, the headline scorecard
will still be judged on the same 4-observable closure set:

`L_path`, `W_wrap`, `Block-χ²`, `L_tail_91_114`

## 6. Locked interpretation rules

Baseline reference from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50:

- empirical `L_mufaṣṣal-short = 16.514906`
- sim mean `15.619384`
- residual mean-gap `Δ₀ = 0.895522`
- empirical outside simulator 95% CI

For each cell:

| Outcome | Verdict |
|---|---|
| `L_mufaṣṣal-short` inside sim 95% CI AND 4/4 overall PASS | **TERMINAL-HINGE-CLOSURE** |
| `L_mufaṣṣal-short` outside but new gap `≤ 0.5·Δ₀` | **PARTIAL-TERMINAL-CLOSURE** |
| improvement vs top-50 but gap `> 0.5·Δ₀` | **WEAK-TERMINAL-CLOSURE** |
| no material improvement or worse | **R12a-PERSISTS** |

Additional equation-level reading:

- If **cell B** reaches `TERMINAL-HINGE-CLOSURE`, then the project can
  honestly say the causal-generative miss was a **localized omitted-hinge
  enumeration problem**.
- If **cell B** still fails, then the highest-EV next move becomes a
  genuinely different terminal mechanism, not more generic hinge
  extension.

## 7. Bonferroni discipline

`k = 2` (`+5` and `+10` cells), so `α_bon = 0.025` per cell. This
tightens the family relative to an uncorrected two-cell run.

## 8. Honest limits

1. **This is still a hinge-based explanation.** If the run passes, it
   shows the residual can be recovered by a small set of terminal jumps;
   it does not prove those jumps are the only meaningful description of
   Juzʾ 30.
2. **The added edges were selected from a prior finding on the same
   corpus ([[h-new-255-juz30-mini-cycle|H-NEW-255]]).** That is acceptable here because [[h-new-255-juz30-mini-cycle|H-NEW-255]] was
   already landed and the ranking is locked before execution; still, the
   experiment is testing a *specific mechanistic carry-over* from a prior
   descriptive result.
3. **The mini-geodesic result does not imply ring-closure.** [[h-new-255-juz30-mini-cycle|H-NEW-255]]
   explicitly falsified Juzʾ-30 mini-wrap; this run tests omitted internal
   jumps only, not a sub-ring.
4. **A pass at `+10` would still be parsimonious only in a qualified
   sense.** The total preserved hinge count would rise from 50 to 60 out
   of 113 consecutive edges.
5. **A fail would not invalidate [[h-new-255-juz30-mini-cycle|H-NEW-255]].** It would mean the internal
   jumps are real descriptively but insufficient causally for the
   residual under this simulator.

## 9. Deliverables

- `scripts/h_new_236_1c_targeted_mufassal_hinges.py`
- `findings/phase-b-hypotheses/csv/h-new-236-1c.json`
- `findings/phase-b-hypotheses/h-new-236-1c-targeted-mufassal-hinges.md`
- `journal/h-new-236-1c-run-1.md`
- updates to `MASTER-FINDINGS-LEDGER.md`
- updates to `HANDOFF/05-OPEN-QUESTIONS.md`
- updates to `HANDOFF/SESSION-LOG-2026-04-18.md`

Pre-reg locked 2026-04-18. Execution follows.
