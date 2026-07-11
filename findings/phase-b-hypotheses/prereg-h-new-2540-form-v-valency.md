---
id: H-NEW-2540
title: Form II to Form V as a directed valency-reducing relation
date: 2026-07-11
status: AMENDED-AND-LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
family: MORPH-2026-07-11-A
seed: 20260509
n_permutations: 10000
tests_in_family: 4
alpha_bonferroni: 0.0125
strict_novelty_gate: 0.005
---

# PRE-REGISTRATION — H-NEW-2540 — Does Form II→V reduce overt direct-object realization within roots?

The initial version of this file was committed before the analysis script existed
or was run. The final amended SHA-256 will be embedded as a fixed literal in the
script. Runtime verification must fail if this file changes.

**Pre-run amendment, also committed before corpus computation:** after the first
registration commit, reconciliation with `docs/statistical-rigor-protocol.md` found
that the older project standard requires two null models and a strict novel-result
gate below 0.005. A script skeleton and synthetic self-check existed, but neither
QAC nor EQTB had been read by that script. Sections 5 and 7 now require both a
root-unit sign-flip null and a token-label permutation null for each hypothesis.
Git preserves the initial registration and this stricter amendment separately.

## 1. Formal claim and guardrail

For a root `r`, let `P_r^II` and `P_r^V` be the event predicates realized by
Forms II and V. Classical morphology often relates Form V to a middle,
reflexive, or resultative counterpart of Form II. The narrow empirical prediction
is therefore:

`P(overt direct object | Form II, root r) > P(overt direct object | Form V, root r)`.

This is a **directed, lossy relation**, not an involution. No inverse Form V→II
operation is claimed. A significant corpus tendency is not an isomorphism or a
homomorphism, and lexicalized counterexamples remain counterexamples to any global
semantic law.

The analogous Form III→VI relation is registered as a low-power secondary test.

## 2. What was known before lock

Only feasibility counts were inspected:

- QAC v0.4 has 40 roots attested in both Forms II and V, with 811 tokens across
  those paired roots.
- It has 12 roots attested in both Forms III and VI, with 83 tokens; this family
  is expected to be underpowered.
- No direct-object rate, root-level direction, test statistic, passive-control
  result, or permutation result was inspected before this lock.

## 3. Frozen inputs

1. QAC v0.4 morphology:
   `data/morphology/quranic-corpus-morphology-0.4.txt`
   SHA-256 `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46`.
   It supplies location, root, derivational form, aspect, and explicit passive
   marking.
2. EQTB `Quranic.csv`, acquired through the UD-Quran reproducibility package.
   SHA-256 `a303c24cf51b90f6cd5eb0fb25d6c591977a7797743d16e0dedc76a5af5ae0b7`.
   It supplies dependency edges only. Source and license are recorded in
   `data/syntax/UD-QURAN-SOURCE.md`.

The QAC location is authoritative for root and form because EQTB documents lemma
and morphology corrections of mixed provenance. EQTB is joined by exact segment
location and used only to decide whether a verb heads a direct-object dependency.

## 4. Deterministic extraction

1. Parse every QAC row whose segment tag is `V` and whose feature string contains
   `ROOT:`. Unmarked form is Form I; explicit `(II)`…`(XII)` supplies other forms.
2. Exclude every verb with explicit `PASS`; the primary question concerns active
   derivational valency, not inflectional passive voice.
3. Parse UTF-16 EQTB by `sentence_id` and `token_id`.
4. An overt direct object exists for a verb iff at least one real (non-elided)
   EQTB row in the same sentence has case-insensitive base relation `obj` and
   `ref_token_id` equal to that verb's `token_id`. Relation modifiers after a
   space or `<<...>>` are stripped before comparison. `cog`, `circ`, `obl`, and
   prepositional complements do not count as direct objects.
5. Join QAC verb and EQTB verb by exact location `(s:v:w:segment)`. Synthetic
   EQTB nodes and unmatched locations are excluded and counted.
6. The primary root set contains roots with at least two joined active tokens in
   Form II and at least two in Form V. A full ≥1-token sensitivity is reported but
   cannot replace the primary threshold.

## 5. Registered statistics and locked directions

For each eligible root `r` and form `f`, let `n_rf` be eligible verb tokens and
`y_rf` tokens heading at least one direct object. Define the smoothed rate

`p_rf = (y_rf + 0.5) / (n_rf + 1)`

and harmonic-balance weight

`w_r = 2*n_rA*n_rB / (n_rA + n_rB)`.

The statistic is the weighted within-root rate difference:

`T = sum_r w_r*(p_rA - p_rB) / sum_r w_r`.

### H1 — primary Form II→V contraction

- `A = II`, `B = V`.
- **Locked direction:** `T_II,V > 0`.
- Null A: independently swap the complete II and V outcome/count cells within each
  root with probability 0.5, preserving roots, form sample sizes, object outcomes,
  and the number of paired roots.
- Null B: within each root, preserve `n_II`, `n_V`, and the root's total number of
  object-positive tokens, then randomly reallocate those object labels across the
  root's II+V token slots. This is a conditional token-level independence null and
  does not assume whole form cells are exchangeable.
- 10,000 draws per Monte Carlo null with independent
  `random.Random(20260509)` streams.
- One-sided `p = (1 + #{T_perm >= T_obs}) / 10001` for each Monte Carlo null.
- PASS iff direction is positive and **both** nulls give `p < 0.005`.

### H2 — secondary Form III→VI contraction

- `A = III`, `B = VI`.
- **Locked direction:** `T_III,VI > 0`.
- Same extraction, statistic, and two nulls.
- Because at most 12 paired roots exist, enumerate all `2^R` root-label swaps when
  `R <= 20`; otherwise use the seeded 10,000-swap Null A. Null B uses 10,000
  seeded conditional token reallocations.
- PASS iff direction is positive and both exact/permutation p-values are `< 0.005`.
- A NULL is expected to be potentially power-limited and is still published.

The family contains four registered inferences: H1×{Null A, Null B} and
H2×{Null A, Null B}. Bonferroni gives `alpha_bon = 0.0125`; the project-wide
novelty rule is stricter, so the decision gate is `0.005` for all four.

## 6. Robustness and negative controls

These are reported but do not replace H1/H2:

1. Unsmooth macro-average of root rate differences.
2. Mantel-Haenszel common odds ratio across roots.
3. Full ≥1-token paired-root sensitivity.
4. Leave-one-root-out range for H1.
5. Meccan and Medinan direction split where both forms have data.
6. Explicit `PASS` incidence compared two-sided between paired forms as an
   **orthogonality control**. Middle/reflexive derivation must not be relabeled as
   inflectional passive merely because the English gloss sounds passive.
7. QAC-versus-EQTB agreement on form and root for joined verbs. Agreement below
   95% downgrades any PASS to annotation-sensitive.

## 7. Decision language

- **H1 PASS, H2 PASS:** both directed form families support reduced overt-object
  realization; call this `DUAL-FAMILY SUPPORT`, not a global semantic algebra.
- **H1 PASS, H2 NULL:** `FORM-II→V SUPPORTED; III→VI UNRESOLVED/NULL`.
- **H1 NULL or reversed:** no confirmatory Quran-corpus evidence for the proposed
  Form II→V valency reduction under this instrument. Do not rescue it with the
  secondary or a changed threshold.
- Any result remains an association in this Quran/EQTB annotation. It is not
  Quran-specific without a matched Classical-Arabic control corpus.
- Even a dual PASS is `QURAN-INTERNAL SUPPORT`, not a full cross-corpus Phase-B
  finding under `docs/statistical-rigor-protocol.md` §3, until a matched
  Classical-Arabic dependency-treebank control is registered and passed.

## 8. Required immutable run record

The run must create a new directory under
`findings/phase-b-hypotheses/runs/h-new-2540/<UTC timestamp>/` containing:

- `result.json`
- `manifest.json` with command, Git commit, prereg/script/input SHA-256 values,
  Python version, seed, and platform
- `object-edges-sample.tsv` for blinded/manual annotation checking
- the human-readable finding in the parent findings directory

Nothing in an earlier run directory may be overwritten.
