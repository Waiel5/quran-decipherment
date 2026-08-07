---
id: H-NEW-2600
title: The muṭāwaʿa lattice — a complete derivational-form × object-realization map, with causative reverse-controls
date: 2026-08-07
status: LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
family: MORPH-2026-08-07-A
seed: 20260509
n_permutations: 10000
confirmatory_inferences: 10
alpha_bonferroni: 0.005
corrected_novelty_gate: 0.005
raw_p_gate: 0.0005
---

# PRE-REGISTRATION — H-NEW-2600 — Does the object-realization contrast hold across the whole derivational lattice, and does it REVERSE for the causatives?

This file is written and committed **before the analysis script exists** and before any
form pair other than II/V and III/VI has been computed. The final SHA-256 is embedded as
a fixed literal in `scripts/h-new-2600.py` and verified at runtime.

## 1. Why this test exists — the gap in H-NEW-2540

H-NEW-2540 established that within a root, Form II heads an overt dependency-object more
often than Form V (MH-OR 21.08), and Form III more often than Form VI (MH-OR 22.53).

**H-NEW-2540 had no directional control.** It tested two form pairs, both predicted to
show reduction, and both did. That design cannot distinguish "the instrument measures
derivational valency" from "the instrument reports a positive T for almost any form pair"
— which could arise from a generic confound such as token frequency, verse position, root
productivity, or an artifact of the EQTB `Obj` annotation policy.

**This test supplies the missing falsification control.** Classical ṣarf assigns Forms II
and IV a *causative/factitive* function relative to Form I — the opposite of muṭāwaʿa. If
the instrument is measuring valency, then I→II and I→IV must show T **negative**. If they
also come out positive, H-NEW-2540 is an artifact and this pre-registration says so in
advance.

**A reversal on the causative arms is the outcome that would retire H-NEW-2540.** That is
the point of running it.

### Citation honesty

The muṭāwaʿa doctrine (Form VII as the *muṭāwiʿ* of Form I; Form V of Form II; Form VI of
Form III) and the causative function of Forms II and IV are standard, uncontroversial
classical Arabic morphology. **No classical grammar primary source is present in this
repository** (`data/literature/` holds tafsīr, ḥadīth and modern secondary literature only;
verified 2026-08-07). I therefore state the doctrine as textbook consensus and deliberately
give **no passage citation**, rather than invent one. If a grammar primary source is later
acquired, the doctrinal claims here should be cited to it properly.

## 2. What was known before lock

- H-NEW-2540's results for II→V and III→VI only (published, `h-new-2540-form-v-valency.md`).
- **No other ordered form pair has been computed at any point.** No T, no root count, no
  direction, no p-value has been inspected for I/VII, I/VIII, IV/VII, I/II, I/IV, or any
  other pair.
- QAC feasibility counts were not inspected for the new pairs before this lock.

## 3. Frozen inputs

Identical to H-NEW-2540, verified at runtime by SHA-256:

1. QAC v0.4 `data/morphology/quranic-corpus-morphology-0.4.txt`
   `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46`
2. EQTB `Quranic.csv` (UD-Quran reproducibility package, CC BY 4.0)
   `a303c24cf51b90f6cd5eb0fb25d6c591977a7797743d16e0dedc76a5af5ae0b7`
3. `data/revelation-order.csv`
   `74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7`

Extraction, join, passive exclusion, statistic and nulls are **inherited verbatim** from
H-NEW-2540 §4–§5 and must not be re-specified. QAC location is authoritative for root and
form. Explicit `PASS` verbs are excluded. Lineage agreement below 100% aborts the run.

## 4. Statistic

Unchanged from H-NEW-2540: `p_rf = (y_rf + 0.5)/(n_rf + 1)`,
`w_r = 2 n_rA n_rB/(n_rA + n_rB)`, `T = Σ w_r (p_rA − p_rB)/Σ w_r`.

Eligibility: roots with ≥2 joined active tokens in **each** of the two forms.

Both nulls from H-NEW-2540 §5 are run for every confirmatory pair. Null A (root-cell
sign-flip) uses `random.Random(20260509)`, or **exact enumeration when R ≤ 20**. Null B
(within-root token-label reallocation, margin-preserving) uses `random.Random(20260510)`.

Because Null A's sign-flip distribution is symmetric about zero while the smoothed
statistic carries a bias when `n_A ≠ n_B`, **Null B is the primary null for every arm**
and Null A is reported alongside. The unsmoothed macro difference and the
Mantel-Haenszel odds ratio are reported for every pair as smoothing-free estimators.

## 5. Locked directional hypotheses

### Confirmatory family — muṭāwaʿa arms (locked POSITIVE)

- **P1. I → VII** (*faʿala* → *infaʿala*). `T > 0`. The canonical muṭāwiʿ of the
  ṣarf tradition. **The strongest novel prediction in this file.**
- **P2. I → VIII** (*faʿala* → *iftaʿala*). `T > 0`. Form VIII is frequently muṭāwiʿ but
  also carries reflexive-benefactive and lexicalized senses, so a weaker prediction.
- **P3. IV → VII** (*afʿala* → *infaʿala*). `T > 0`.

### Confirmatory family — causative reverse-controls (locked NEGATIVE)

- **N1. I → II** (*faʿala* → *faʿʿala*, factitive/intensive). `T < 0`.
- **N2. I → IV** (*faʿala* → *afʿala*, causative). `T < 0`.

### Replication arms — NOT novel confirmations

- **R1. II → V** and **R2. III → VI**. Same data as H-NEW-2540, so these are consistency
  checks only. They are excluded from the Bonferroni family and **may not be cited as
  independent support**. If either fails to reproduce, the run is broken and everything
  here is void.

The confirmatory family is P1, P2, P3, N1, N2 × {Null A, Null B} = **10 inferences**.
Bonferroni α_bon = 0.05/10 = 0.005. The project novelty rule is stricter, so the **raw
decision gate is 0.0005** and the corrected gate is 0.005.

One-sided p in the locked direction:
`p = (1 + #{T_perm ≥ T_obs})/(n+1)` for positive arms,
`p = (1 + #{T_perm ≤ T_obs})/(n+1)` for negative arms.

PASS iff the sign matches the lock **and** both raw p-values are `< 0.0005`.

## 6. Exploratory lattice map

Separately from the confirmatory family, compute T for **every** ordered form pair with
≥5 eligible roots and report it as a descriptive matrix with per-cell Bonferroni over the
number of eligible cells. This is a **map, not a set of hypotheses**; no cell in it may be
reported as a confirmed finding. Its purpose is to show whether positive T is pervasive
(bad — suggests artifact) or structured along the muṭāwaʿa relation (good).

## 7. Decision language

- **P1–P3 positive AND N1–N2 negative:** `LATTICE-STRUCTURED`. The instrument tracks
  derivational valency with the sign predicted by classical morphology in both directions.
  This substantially strengthens H-NEW-2540.
- **P1–P3 positive AND N1 or N2 also positive:** `INSTRUMENT-CONFOUNDED`. The measure
  returns positive T irrespective of the derivational relation. **H-NEW-2540 is then
  downgraded to artifact-suspected** and this file's §1 commits me to saying so.
- **P1 NULL:** the canonical muṭāwiʿ pair fails. Report as NULL with full prominence and do
  not rescue it with P2/P3.
- **Any arm reversed:** pre-commit violation, published as NULL with full prominence.
- All verdicts remain **dependency-annotation-limited** and **Quran-internal**, exactly as
  H-NEW-2540 §7. No cross-corpus claim is made without a matched Classical-Arabic control.

## 8. Required run record

`findings/phase-b-hypotheses/runs/h-new-2600/<UTC timestamp>/` containing `result.json` and
`manifest.json` (command, git commit, all input SHA-256, Python version, platform, seeds).
Nothing in an earlier run directory may be overwritten. The runner emits no interpretive
prose; the finding is written afterwards.
