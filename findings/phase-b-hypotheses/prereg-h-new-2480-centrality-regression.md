---
finding_id: H-NEW-2480 (PRE-REGISTRATION)
title: "Cycle-centrality ~ private-vocabulary regression — direct test of the cross-finding-027 elaboration⇒periphery mechanism"
phase: B+
status: PRE-REGISTERED (locked BEFORE computation)
date: 2026-05-30
author: Waiel Al-Shujaa
extends: "H-NEW-2430 (eponymous-surah cycle-centrality law) + cross-finding-027 (eponymy-independence law) + Q071-F-01 + Q020-F-06"
seed: 20260509
n_perm: 10000
rules_tuple: "(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# H-NEW-2480 (PRE-REGISTRATION) — Cycle-centrality ~ private-vocabulary regression

## Motivation

cross-finding-027 (the eponymy-independence law) and its stronger pillar H-NEW-2430
assert a MECHANISM, not just a correlation: **elaboration ⇒ lexical periphery.**
The claim is that a pericope's mean-pairwise root-Jaccard centrality WITHIN its
prophet-cycle is driven DOWN by its **private-vocabulary mass** — roots it
introduces that no other retelling in the same cycle shares (scene-specific
vocatives, idol-names, daʿwa-formulae, genealogies). The H-NEW-2430 finding
asserts this descriptively (Maryam 89 roots → rank 4/5; Nūḥ 87 → 5/6; the
12-root Yūnus allusion → 2/4) and explicitly flags it as an OPEN FOLLOW-UP
(cross-finding-027 §"Open follow-ups" #2; ledger §10.126 queued-target #2):

> "Test the mechanism directly: is cycle-centrality-rank predicted by (pericope
> private-root-count)? (the H-NEW-2430 data suggest a strong monotone relation —
> formalize as a regression)."

This pre-reg formalizes that test as a regression over ALL cycle-pericopes,
pooled and per-cycle, and — critically — DISTINGUISHES the private-vocabulary
effect from a pure length effect (a long pericope mechanically has more roots,
and more chances to have private ones). If the effect is only length, the
cross-finding-027 mechanism is mis-stated.

## Unit of analysis

Each PERICOPE across the prophet-cycles defined in H-NEW-2430. The regression is
NOT about eponymy — it is about whether private-vocabulary predicts centrality
for EVERY pericope. Therefore ALL cycle members are units, eponymous or not, and
the Mūsā cycle (a documented H-NEW-2430 control cycle: 4 pericopes, NO eponymous
surah) is INCLUDED as a sixth cycle of ordinary pericopes.

Cycles + pericopes (boundaries identical to H-NEW-2430 / Q071-F-01 / Q020-F-06,
verified on disk at runtime):

- **NŪḤ** (6): Q7:59-64, Q11:25-49, Q23:23-30, Q26:105-122, Q54:9-17, Q71:1-28
- **IBRĀHĪM** (6): Q6:74-83, Q14:35-41, Q19:41-50, Q21:51-70, Q26:69-104, Q37:83-113
- **HŪD** (5): Q7:65-72, Q11:50-60, Q26:123-140, Q46:21-26, Q54:18-21
- **MARYAM** (5): Q3:35-47, Q19:16-34, Q21:91, Q23:50, Q66:12
- **YŪNUS** (4): Q10:98, Q21:87-88, Q37:139-148, Q68:48-50
- **MŪSĀ** (4, H-NEW-2430 control cycle): Q20:9-36, Q27:7-14, Q28:29-35, Q79:15-26

Total **N = 30 pericopes** across **6 cycles**.

## Variables (defined BEFORE computation)

For each pericope p in cycle C, on QAC v0.4 ROOT annotation (no-tashkeel verse-union):

- **R(p)** = the SET of distinct root-types attested in p (verse-union; the same
  set H-NEW-2430 used for Jaccard).
- **centrality(p)** = mean over the (|C|−1) other pericopes q in the SAME cycle of
  Jaccard(R(p), R(q)) = |R(p)∩R(q)| / |R(p)∪R(q)|. (Medoid-sense centrality,
  identical instrument to H-NEW-2430.)
- **private_root_count(p)** = | { r ∈ R(p) : r ∉ R(q) for every other q in cycle C } |
  — root-TYPES in p that appear in NO other pericope of the same cycle.
- **length(p)** = **root-token count** = total number of ROOT-annotated tokens in
  p (WITH multiplicity; a root counted once per word-occurrence carrying it).
  This is the pre-registered "length". (unique_root_type_count = |R(p)| is also
  recorded as a secondary descriptor but length := root-token count for the
  partial-correlation control.)

## Hypotheses & LOCKED direction

**H1 (primary, the cross-finding-027 mechanism):**
centrality is **NEGATIVELY** correlated with private_root_count — more private
vocabulary ⇒ more peripheral. **DIRECTION LOCKED NEGATIVE.** Spearman ρ(centrality,
private_root_count) < 0.

**H2 (length confound):** centrality is also negatively correlated with length
(root-token count). DIRECTION LOCKED NEGATIVE (a longer pericope is mechanically
more peripheral). This is the rival explanation.

**H3 (the discriminating test — does private-vocab survive a length control?):**
The partial Spearman correlation ρ(centrality, private_root_count | length) is
still NEGATIVE and non-trivial. If H3 holds, the cross-finding-027 mechanism is
vindicated as MORE than a length artefact. If the partial correlation collapses
to ≈0 (or flips sign) once length is controlled, the mechanism is RE-STATED as a
pure length effect (private-vocab adds nothing beyond size) — reported with full
prominence as a partial demotion of the stated mechanism.

## Statistical method

- **Spearman ρ** (rank correlation; robust, no linearity assumption) for H1, H2.
- **Permutation null (MW-2):** shuffle the PAIRING — permute the
  private_root_count (resp. length) vector against the fixed centrality vector,
  10000 permutations, seed 20260509. One-sided p in the LOCKED (negative)
  direction: p = (#{ρ_perm ≤ ρ_obs} + 1)/(n_perm + 1). Pooled permutation shuffles
  the global 30-vector; per-cycle permutation shuffles within each cycle's
  members (small-n, reported but MW-7-capped).
- **Partial Spearman (H3):** rank-transform centrality, private_root_count, length;
  partial correlation via the standard residual formula
  ρ_xy.z = (ρ_xy − ρ_xz·ρ_yz) / sqrt((1−ρ_xz²)(1−ρ_yz²)). Permutation null for the
  partial: permute private-rank residuals against centrality residuals (10000 perms,
  same seed). Also report partial ρ(centrality, length | private_root_count) for
  symmetry (which of the two confounded predictors is primary).
- **OLS sanity (MW-3 alternative model):** standardized OLS of centrality on
  z(private_root_count) and z(length) jointly, report both coefficients + signs.
  Descriptive only (n=30, two predictors); the Spearman/partial is the headline.

## Bonferroni / multiple-comparison family

The headline family is k=3 cells: {pooled H1, pooled H2, pooled H3-partial}.
α_corrected = 0.05/3 = 0.0167. Per-cycle correlations (6 cycles) are a SECONDARY
exploratory family (k=6, α=0.0083), MW-7-capped (n per cycle ≤6 → Spearman
unstable; reported as direction-tallies, not as confirmatory p-values).

## Success / failure criteria (LOCKED)

- **H1 CONFIRMED** iff pooled Spearman ρ(centrality, private_root_count) < 0 AND
  pooled permutation p ≤ 0.0167 (Bonferroni-3).
- **H1 NULL** iff p > 0.0167 in the locked direction.
- **H1 REVERSAL (pre-commit violation, full prominence)** iff ρ > 0 AND the
  reversed-direction permutation p < 0.05 — published as FALSIFIED-MECHANISM.
- **Mechanism VINDICATED (H3)** iff partial ρ(centrality, private | length) < 0
  AND partial permutation p ≤ 0.0167 — private-vocab predicts periphery BEYOND
  size.
- **Mechanism = LENGTH-ARTEFACT (H3 collapse)** iff partial ρ(centrality,
  private | length) is ≥ −0.05 (collapses toward 0 or flips) while ρ(centrality,
  length | private) stays strongly negative — the cross-finding-027 wording
  ("private-vocabulary mass") is then demoted to "pericope size", reported with
  full prominence as a mechanism RE-STATEMENT.
- Per-cycle tallies are descriptive (how many of 6 cycles show the locked negative
  sign for private_root_count); MW-7-capped, not pass/fail.

## MW protections

- MW-1 instrument-prior: Spearman + partial-Spearman + anchor-shuffle null all
  fixed here, before computation.
- MW-2 corpus-prior: 10000-perm pairing-shuffle null.
- MW-3 alternative models: Spearman (headline) + OLS standardized (sanity) + the
  partial in both directions.
- MW-4 over-fitting: no fitted hyper-parameters; rank statistics.
- MW-5 replication: NŪḤ Q71 rank (5/6) and Mūsā Q20 hub-strength (~0.234) must
  reproduce the stored H-NEW-2430 values at runtime (assert).
- MW-6 instrument-control: the Mūsā control cycle is included as ordinary
  pericopes (not eponymous) — it tests whether the centrality~private relation is
  a general pericope property, not an eponymy artefact.
- MW-7 post-hoc cap: per-cycle small-n correlations capped to direction-tallies.

## Rules-tuple

`(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`. Bidirectional sensitivity: a lemma or orthographic-token
lens could shift private-root counts (e.g. derived forms collapsing to one root);
flagged, MW-7-capped, not run. The QAC-ROOT lens is locked for comparability with
H-NEW-2430.

## Equal NULL prominence

A NULL pooled H1, a length-artefact H3 collapse, or a REVERSAL are each published
with the same prominence as a confirmation. The cross-finding-027 mechanism is on
trial here; an honest demotion strengthens the law's eventual statement.

## Files (to be produced)

- This pre-reg (SHA-256 locked, embedded in script, verified at runtime).
- Script: `findings/phase-b-hypotheses/scripts/h-new-2480.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2480.json`
- Finding: `findings/phase-b-hypotheses/h-new-2480-centrality-regression.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
