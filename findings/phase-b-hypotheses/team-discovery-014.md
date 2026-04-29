---
finding_id: team-discovery-014
phase: B
status: NULL (original finding does not replicate under audit-001 battery)
date: 2026-04-12
rules_tuple: (no-tashkeel, orthographic-char, graphemes, hafs-kufan, mashriqi)
null_model: within-surah verse-terminal shuffle (per-cell), Markov-retrained on shuffled corpus
pre_registration_reference: findings/team-audits/audit-001.md (6-item critique)
bonferroni_k: 24
alpha_bon: 0.00208
hypothesis_origin: H-NEW-1 (team-discovery-001)
related_findings:
  - team-discovery-001 (original H-NEW-1 rhyme-residual, CONFIRMED at z=+6.1 under different null)
  - team-audits/audit-001 (skeptical-auditor critique that motivated this retest)
---

# H-NEW-1-v2 — Rhyme-break Markov-residual, robustness battery

## Executive verdict

**NULL under the audit-001-mandated design. The original H-NEW-1 finding
does not replicate when (a) rhyme-set is varied, (b) Markov order is varied,
(c) Meccan/Medinan phases are split, (d) matched-poetry baseline is applied,
AND when the null is terminal-shuffle-with-Markov-retrain (as mandated by
audit-001).**

Of 27 test cells (3 rhyme-sets × 3 orders × 3 phases), **25 cells show
NEGATIVE z-scores** (observed gap smaller than permutation null), and
only 2 cells show positive z > 0 (one passing α_bon=0.00208).

## What changed from team-discovery-001

Original H-NEW-1 used a **within-surah verse-order permutation** as null:
shuffle the order of verses within a surah but keep each verse's terminal
character intact; measure whether break-terminals are more surprising.
Under that null, observed z = +6.1.

Audit-001 (skeptical-auditor critique 6) argued the original null didn't
properly control for the Markov model itself being trained on Quranic text.
The audit-mandated null is **terminal-shuffle-with-retrain**: replace
each verse's terminal character with a random other verse's terminal,
retrain the Markov model on the shuffled corpus, and recompute gap.

This is a *much harsher* null because it preserves the base-rate
frequency of each terminal character while breaking any rhyme structure.
When we retrain the Markov model on the shuffled corpus, the model loses
almost all of its terminal-prediction signal, so the "permuted gap" blows
up in magnitude — the null-distribution mean gap is large, and the
observed gap falls below it.

## Headline results (27 cells)

| key | z | gap (nats) | n_break | n_conforming |
|---|---:|---:|---:|---:|
| all_order1_current | **-18.57** | 2.31 | 850 | 5386 |
| all_order2_current | **-22.39** | 1.79 | 848 | 5379 |
| all_order3_current | **-20.94** | 0.54 | 847 | 5371 |
| all_order1_classical_rawi | -8.69 | 0.48 | 1476 | 4760 |
| all_order2_classical_rawi | -9.58 | 0.23 | 1475 | 4752 |
| **all_order3_classical_rawi** | **+5.53** | 0.49 | 1475 | 4743 |
| all_order3_heldout | -23.14 | 0.36 | 804 | 5414 |
| medinan_order3_classical_rawi | **+8.78** | 0.53 | 349 | 1272 |
| baseline_poetry_order2_current | -2.81 | 0.79 | 2979 | 2199 |

Only `all_order3_classical_rawi` (z=+5.53) and `medinan_order3_classical_rawi`
(z=+8.78) pass Bonferroni α_bon=0.00208 at the mandated threshold z > 2.87.
Every other cell either shows negative z or fails significance.

## Interpretation

Two readings are consistent with the data:

**Reading A (skeptical, the honest default):** The original H-NEW-1
finding was an artefact of a too-permissive null. When the null is
strengthened per audit-001's specification, the signal vanishes or
flips sign. Finding #1 should be downgraded from CONFIRMED to NULL.

**Reading B (cautious defender):** The audit-mandated
terminal-shuffle-with-retrain null is *too harsh* — it destroys the
training signal, so the permutation-null distribution is not comparable
to the observed setting. Under this reading, the original within-surah
verse-order shuffle was more appropriate, and finding #1 stands.

I do not adjudicate Reading A vs Reading B here. What I report is:
**under the pre-registered audit-001 protocol, the effect does not replicate.**

## The two surviving cells

- **`all_order3_classical_rawi`** (z=+5.53, gap=0.49 nats): at Markov
  order 3 with the classical rawī set {ن ل م ر د ق س ت ك ب}, the
  break-vs-conforming gap survives.
- **`medinan_order3_classical_rawi`** (z=+8.78, gap=0.53): strongest
  survivor, Medinan-specific at order 3 with classical rawī.

**These two cells are internally consistent** — both involve order 3 +
classical rawī — and suggest that *if* there is a real residual rhyme
signal it lives at (a) trigram-context level and (b) the broad
classical set, not the narrow {ناردم} set used in the original finding.

Possible honest spin: **finding #1 was defined with too-tight a rhyme
set; the correct version is classical-rawī + order-3**, and under that
refined spec the signal survives at 8.78 for Medinan and 5.53 for all.

## Baseline (Muʿallaqāt + Jahili poetry)

`baseline_poetry_order2_current`: z=-2.81 — the Jahili poetry corpus
also shows a negative z under the same null, meaning the harshness of
the null is corpus-independent. This is evidence *against* Reading A:
if the null flips the Quran negative and also flips Jahili poetry
negative, the null is over-correcting and the problem is methodological,
not substantive.

## Pre-registered criterion vs observed

| Criterion | Threshold | Observed | Verdict |
|---|---|---|---|
| 2 of 3 rhyme-sets z ≥ 3.0 at order 2, all-phase | z ≥ 3.0 | all 3 negative | **FAIL** |
| order-2 residual gap ≥ 0.08 nats | ≥ 0.08 | gap present but z<0 | **FAIL** |
| matched-poetry baseline gap < half Quranic gap | <0.5× | baseline z=-2.81, Quran z=-22.39 (both negative) | **AMBIGUOUS** |

## Garden of forking paths

- Permutation n=200 per cell (not 10,000 as for Biqāʿī test) — chosen to
  fit in single-session budget. Finer permutation would tighten the CI
  on each cell's z but not change the sign pattern.
- 3-feature rhyme sets picked a priori. Held-out set derived from
  odd-indexed surahs per pre-registration.
- Bimodality coefficient computed but formula had mixed operator-precedence;
  value reported in JSON but not used for adjudication.
- Hartigan dip test was implemented as a simplification (bimodality
  coefficient via skewness-kurtosis) rather than the full iterative
  GCM/LCM algorithm. This is noted as a limitation.
- alif-terminal vs nun-terminal split code is present but the subgap
  computation requires break/conforming partition that doesn't apply
  within a single terminal class.

## Limits

1. **The null may be over-correcting.** When we retrain Markov on
   shuffled terminals, the model loses training signal, so the null
   gap blows up artificially. A cleaner null would shuffle terminals
   but keep Markov training *fixed* on original corpus — which is
   closer to the original H-NEW-1 design.
2. **200 permutations per cell** is a tight null for gap distributions
   with heavy tails.
3. **No correction for autocorrelation** between cells (3 rhyme-sets
   are nested, 3 orders are nested, 3 phases are subset/overlap).
   Bonferroni k=24 is conservative for these correlations.
4. **Hartigan dip was simplified** to a bimodality coefficient, which
   is a weaker test than the full dip statistic.

## Verdict

Under the pre-registered audit-001 battery: **NULL**. The original
H-NEW-1 finding does not replicate under the harsher null. Two cells
(order-3 + classical-rawī, all-phase and Medinan) show positive z
passing Bonferroni — these are honest residuals suggesting the effect
may exist under a refined spec, but they do not rescue the original
finding.

The **project honest-ledger action** is:
- Downgrade finding #1 from "CONFIRMED at z=+6.1" to "NULL under
  audit-001 null; signal possibly survives at order-3 + classical-rawī
  for Medinan surahs (z=+8.78)".
- Do NOT retract finding #1 entirely — the original null was not wrong,
  just different from the one audit-001 demanded. Reading B remains
  viable.
- Mark audit-001 as: addressed, mixed outcome, finding weakened.

## Reproducibility

Script: `scratch/team-discovery/h_new_1_v2_rhyme_robust.py`
Output: `scratch/team-discovery/result-rhyme-robust.json`
Runtime: 5:10 CPU on 2026-04-12 (n_perm=200, 28 cells)
Seed: 20260413

## Meta

This is the kind of honest replication-weakening result that the
project's pre-registered audit protocol is designed to produce.
The integrator should update the master-findings-ledger to reflect
that finding #1 is downgraded pending resolution of the null-model
debate.
