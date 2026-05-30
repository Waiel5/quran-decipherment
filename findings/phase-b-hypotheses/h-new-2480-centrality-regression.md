---
finding_id: H-NEW-2480
title: "Cycle-centrality ~ private-vocabulary regression — the cross-finding-027 mechanism is CONFIRMED in its discriminating (length-controlled) form, while the raw length effect REVERSES"
phase: B+
status: MIXED — H3 mechanism CONFIRMED (partial ρ=−0.498, p=0.0025, Bonferroni-3); H1 raw NULL; H2 raw length REVERSAL (pre-commit violation, full prominence)
date: 2026-05-30
author: Waiel Al-Shujaa
extends: "H-NEW-2430 (eponymous-surah cycle-centrality law) + cross-finding-027 (eponymy-independence law) + Q071-F-01 + Q020-F-06"
prereg_sha256: a861d7cdccbe21333d771eb48b1a29542daa92db947f51a2053f7357ad56cffb
seed: 20260509
n_perm: 10000
bonferroni: "headline k=3 (pooled H1/H2/H3); α = 0.05/3 = 0.0167"
rules_tuple: "(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# H-NEW-2480 — Cycle-centrality ~ private-vocabulary regression (direct mechanism test)

## Question

cross-finding-027 (the eponymy-independence law) and its stronger pillar
H-NEW-2430 assert a *mechanism*, not just an observation: **elaboration ⇒ lexical
periphery.** The proposed driver of a prophet-cycle pericope's low
mean-pairwise-Jaccard centrality is its **private-vocabulary mass** — roots it
introduces that no sibling retelling shares. H-NEW-2430 stated this descriptively
and flagged it (cross-finding-027 §Open-follow-ups #2; ledger §10.126
queued-target #2) as needing a **direct regression**, and specifically a test
that **distinguishes private-vocabulary from a pure length effect.** This is that
test.

## Pre-registration

- Pre-reg `prereg-h-new-2480-centrality-regression.md`, SHA-256
  `a861d7cdccbe21333d771eb48b1a29542daa92db947f51a2053f7357ad56cffb` (embedded in
  the run script, verified at runtime — run passed).
- **Direction LOCKED NEGATIVE** for all three hypotheses (private, length, and the
  length-controlled partial). Any positive result with reversed-direction p<0.05 =
  pre-commit violation, published with full prominence.
- Instrument: mean-pairwise QAC-v0.4-ROOT Jaccard centrality (medoid sense),
  extraction identical to H-NEW-2430; Spearman + partial-Spearman; pairing-shuffle
  permutation null, 10000 perms, seed 20260509; headline Bonferroni k=3
  (α=0.0167).
- N = **30 pericopes across 6 cycles** (Nūḥ 6, Ibrāhīm 6, Hūd 5, Maryam 5, Yūnus 4,
  Mūsā-control 4). Boundaries + figure-markers verified on disk at runtime.
- **MW-5 replication passed at runtime:** Nūḥ Q71 rank 5/6 + centroid Q 7:59-64;
  Mūsā Q20 hub-strength 0.2340 — both reproduce H-NEW-2430 exactly.

## Variables (locked, computed per pericope)

- **centrality** — mean of Jaccard(R(p), R(q)) over the other pericopes q of the
  same cycle (R = distinct root-type set, verse-union).
- **private_root_count** — root-TYPES in p attested in NO other pericope of the
  same cycle.
- **length** — root-TOKEN count (roots WITH multiplicity); the pre-registered size
  control.
- secondary descriptor: **private_fraction** = private_root_count / |R(p)|.

## Results — the headline (pooled, N=30)

| # | Test | Spearman ρ | perm p (locked-neg) | Verdict |
|:-:|:--|:-:|:-:|:--|
| **H1** | centrality ~ private_root_count (RAW) | **+0.176** | 0.824 | **NULL** (locked-negative not confirmed) |
| **H2** | centrality ~ length (root-tokens, RAW) | **+0.400** | 0.984 | **REVERSAL** — reversed-dir p=0.0165<0.05 (pre-commit violation) |
| **H3** | centrality ~ private \| length (PARTIAL) | **−0.498** | **0.0025** | **MECHANISM CONFIRMED** (Bonferroni-3) |

Supporting structure:

- **Collinearity** ρ(private_root_count, length) = **+0.910** — private-count and
  length are nearly redundant raw, the source of the suppression below.
- **Symmetric partial** ρ(centrality, length \| private) = **+0.590** (reversed-dir
  p=0.9997) — at fixed private-vocabulary, length pushes centrality UP.
- **Standardized OLS** (descriptive, MW-3): β_z(private) = **−1.18**,
  β_z(length) = **+1.37** — the two collinear predictors carry large,
  **opposite-signed** partial coefficients (a textbook suppressor pair).
- **Length-free corroboration:** raw Spearman ρ(centrality, **private_fraction**)
  = **−0.531** — when private vocabulary is measured as a *proportion* (intrinsically
  length-normalised), the locked NEGATIVE relation appears with NO partialling at
  all, independently confirming H3.

## Interpretation — a suppressor structure, and a sharpened mechanism

The raw and partial correlations point opposite ways because **private-root-count
and length are 91% collinear**, yet they push centrality in *opposite* directions:

- **Length, holding private-density fixed, RAISES centrality.** A longer retelling
  carries more of the cycle's shared CORE roots (`flk`/`grq`/`njw` for Nūḥ; the
  burning-bush lexicon for Mūsā) in absolute terms; with more shared roots its
  pairwise intersections grow, lifting absolute Jaccard. This is why H2 reverses
  and why the long Mūsā/Ibrāhīm cores (Q20:9-36 cent 0.234; Q21:51-70 cent 0.200)
  sit high while the terse single-verse Maryam/Yūnus allusions (Q23:50, Q68:48-50;
  cent ≈ 0.07–0.10) sit low. **Absolute lexical overlap scales with size.**
- **Private vocabulary, holding length fixed, LOWERS centrality** — exactly the
  cross-finding-027 mechanism. Two pericopes of equal length: the one that spends
  its roots on cycle-shared material is central; the one that spends them on
  scene-private material (idol-names, genealogies, the palm-tree, daʿwa-formulae)
  is peripheral. Partial ρ = −0.498 (p=0.0025) and the length-free private-fraction
  ρ = −0.531 both isolate this.

So the H-NEW-2430 descriptive story ("largest eponymous pericopes rank worst")
was reading a **real signal through a confound**: the eponymous surahs are both
long AND private-vocabulary-dense, and it is the *density* (private fraction), not
the raw size, that drives them to the periphery. The corrected, mechanism-precise
statement is:

> **At fixed pericope length, private-vocabulary density is negatively associated
> with cycle-centrality (partial ρ = −0.50, p = 0.0025). Raw size is, if anything,
> positively associated with centrality. The "elaboration ⇒ periphery" mechanism
> is real but operates through private-vocabulary DENSITY, not through length per
> se.**

This both **confirms** cross-finding-027's mechanism (in its discriminating form)
and **corrects** its loose wording: the law's earlier phrase "private-vocabulary
**mass**, monotone in pericope size" conflated two opposite-signed effects. The
mass (raw count) is confounded; the operative quantity is the *fraction*.

## H2 REVERSAL — published with full prominence

The pre-registered H2 locked centrality NEGATIVELY to length. The observed raw
relation is **strongly POSITIVE** (ρ=+0.400, reversed-direction permutation
p=0.0165 < 0.05). This is a **pre-commit violation** and is reported as such, not
massaged. Its cause is now understood (absolute lexical overlap scales with size;
see above) and it does NOT damage the parent mechanism — on the contrary, the
fact that length and private-density are opposite-signed is what makes the
length-control in H3 essential and the mechanism non-trivial. The H2 reversal is a
genuine, publishable empirical fact about cycle-pericope lexical overlap:
**within a prophet-cycle, longer retellings are more lexically central, not less.**

## Per-cycle direction tallies (secondary, MW-7-capped)

n ≤ 6 per cycle → Spearman unstable; reported as direction-tallies, not p-values.

| Cycle | n | ρ(cent, private) | ρ(cent, length) |
|:--|:-:|:-:|:-:|
| Nūḥ | 6 | **−0.551** | +0.143 |
| Ibrāhīm | 6 | **−0.257** | +0.200 |
| Hūd | 5 | +0.700 | +0.600 |
| Maryam | 5 | **−0.872** | −0.821 |
| Yūnus | 4 | +0.200 | +0.200 |
| Mūsā | 4 | +0.800 | +0.800 |

3/6 cycles show the locked-negative raw private sign; only 1/6 shows negative raw
length — consistent with the pooled picture (raw private weakly positive, raw
length positive) and consistent with the suppressor reading: the cycles where raw
private goes positive (Hūd, Mūsā, Yūnus) are precisely the ones whose private and
length co-move most tightly, so the raw private sign tracks the positive length
effect. The pooled length-controlled partial is the correct estimand; these
small-n raw cycle correlations are descriptive only.

## Relation to prior findings

- **H-NEW-2430 / cross-finding-027**: the parent law (eponymy ≠ centrality; 0/5
  eponymous surahs are their cycle centroid) is UNTOUCHED — it is a rank fact, not
  a regression. H-NEW-2480 tests and **confirms the proposed mechanism in its
  discriminating (length-controlled) form** while **correcting the wording** from
  "private-vocabulary mass, monotone in size" to "private-vocabulary DENSITY at
  fixed size." The eponymous surahs are peripheral because they are private-dense,
  not merely because they are big.
- **H-NEW-2320/2330 (hapax + burstiness)**: H-NEW-2480 is the regression face of
  that — private-density IS within-cycle burstiness, and it is now shown to
  predict periphery beyond length.
- **Q020-F-06 (Mūsā Q20 hub)**: consistent. Q20:9-36 is long (105 tokens) AND
  moderately private-dense; the positive length effect dominates for it, leaving it
  near-central (rank 2/4) — exactly what the suppressor model predicts.

## Honest limits

- **N=30, 6 cycles.** The pooled partial (ρ=−0.498, p=0.0025) is robust to the
  10000-perm null and corroborated by the length-free private-fraction (ρ=−0.531),
  but per-cycle n≤6 cannot independently confirm the partial; cycle tallies are
  descriptive.
- **H1/H2 are about RAW associations and are confounded by 91% collinearity.** The
  scientifically meaningful estimand is the partial / the fraction; the raw H1 NULL
  and H2 REVERSAL are reported for full transparency, not because they refute the
  mechanism.
- **Suppression is real but interpretable.** The opposite-signed OLS coefficients
  (−1.18 / +1.37) are large; with collinearity this high, individual coefficient
  magnitudes are unstable. The *signs* and the *partial-Spearman / private-fraction*
  results are the stable, reported facts.
- **One instrument.** QAC ROOT-Jaccard, locked for comparability. A lemma or
  orthographic-token lens could shift private counts; bidirectional rules-tuple
  sensitivity flagged, MW-7-capped, not run.
- **Mūsā included as ordinary (non-eponymous) pericopes** (MW-6): the
  centrality~private-density relation is a general pericope property, not an
  eponymy artefact — the Mūsā control cycle behaves like the rest under the
  suppressor model.

## Verdict

**The cross-finding-027 mechanism is CONFIRMED in its discriminating, length-
controlled form** (partial ρ = −0.498, p = 0.0025 ≤ Bonferroni-3; private-fraction
ρ = −0.531). Private-vocabulary DENSITY drives pericopes to the lexical periphery
of their prophet-cycle, independent of length. The **raw private-count H1 is NULL**
and the **raw length H2 REVERSES** (longer ⇒ more central; pre-commit violation
published with full prominence) — both because private-count and length are 91%
collinear and length carries a positive sign. The mechanism is real; its earlier
"private-vocabulary mass, monotone in size" wording is corrected to
"private-vocabulary density at fixed length."

## Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2480-centrality-regression.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2480.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2480.json`
- This finding: `findings/phase-b-hypotheses/h-new-2480-centrality-regression.md`

---

## Ledger-ready entry (for MASTER-FINDINGS-LEDGER.md §10.127 — DO NOT auto-insert)

> ## §10.127 H-NEW-2480 (pre-registered) — Cycle-centrality ~ private-vocabulary regression: the cross-finding-027 mechanism is CONFIRMED in its length-controlled form; raw length effect REVERSES
>
> Direct regression test of the cross-finding-027 / H-NEW-2430 mechanism (*elaboration ⇒ lexical periphery*), the queued §10.126 target #2. For all **30 pericopes across 6 prophet-cycles** (Nūḥ, Ibrāhīm, Hūd, Maryam, Yūnus + the Mūsā control cycle), regressed mean-pairwise QAC-ROOT-Jaccard **centrality** on **private-root-count** (roots in no sibling pericope) and on **length** (root-tokens). Pre-reg SHA-256 `a861d7cd…56cffb`, seed 20260509, 10000-perm pairing-shuffle null, headline Bonferroni k=3 (α=0.0167); MW-5 reproduced Nūḥ Q71 rank 5/6 + Mūsā Q20 hub 0.234. **Direction LOCKED NEGATIVE.** **Result (a textbook suppressor structure — private-count and length are 91% collinear with OPPOSITE-signed partial effects):** **H1 raw centrality~private = +0.176 → NULL** (locked-negative not confirmed at raw level); **H2 raw centrality~length = +0.400, reversed-dir p=0.0165 → REVERSAL** (pre-commit violation, full prominence: within a cycle, *longer* retellings are *more* lexically central, because absolute shared-CORE overlap scales with size); **H3 partial centrality~private | length = −0.498, p=0.0025 → MECHANISM CONFIRMED** (Bonferroni-3). Independently corroborated: length-free **private-FRACTION** has raw Spearman **−0.531** with centrality, and standardized OLS gives β_z(private)=−1.18 vs β_z(length)=+1.37. **Interpretation:** the *elaboration ⇒ periphery* mechanism is real but operates through private-vocabulary **DENSITY at fixed length**, NOT through raw size — correcting cross-finding-027's loose phrase "private-vocabulary **mass**, monotone in pericope size," which conflated two opposite-signed effects. The parent eponymy ≠ centrality law (0/5) is untouched; eponymous surahs are peripheral because they are private-DENSE, not merely big. **This CONFIRMS the cross-finding-027 mechanism (length-controlled form) and sharpens its wording.** Files: `findings/phase-b-hypotheses/{prereg-,}h-new-2480-centrality-regression.md`, `scripts/h-new-2480.py`, `csv/h-new-2480.json`.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
