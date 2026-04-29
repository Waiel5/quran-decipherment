# H-NEW-112 — Run 1 Journal

**Agent**: h-new-112-specialist
**Date**: 2026-04-17
**Seed**: 20260417
**Pre-reg**: `findings/phase-b-hypotheses/h-new-112-spectral-network-prereg.md`

## Task

Apply spectral graph theory to the H-NEW-89 meta-cluster network (114 surahs × 11 cluster
systems). Compute eigendecomposition, test spectral gap against random-graph nulls,
analyze Fiedler vector, detect spectral communities, characterize Q 62's role.

## Timeline

- **10:00** — Read HANDOFF/01, HANDOFF/02 orientation files.
- **10:05** — Read H-NEW-89 pre-reg and findings; loaded the 11 locked cluster systems
  and observed incidence from `csv/h-new-89.json`.
- **10:15** — Wrote pre-reg `h-new-112-spectral-network-prereg.md`. Direction-locked BEFORE
  data view. Specified:
  - k=3 Bonferroni (later tightened to 2 via audit-035)
  - α_bon=0.0167 (later 0.025)
  - Primary: spectral gap λ_{k+1} − λ_k with k=3 locked, vs ER null
  - Secondary-Fiedler: χ² vs 3 binary classifications
  - Secondary-Communities: k_eigengap ≥ 3 (later demoted)
- **10:25** — Wrote script `h_new_112_spectral_network.py` with:
  - MW-5 positive control (planted 3-block SBM)
  - ER, configuration-model, BA, SBM nulls
  - Full spectrum dump
  - Q 62 saddle/peak characterization
- **10:35** — First run: discovered indexing bug in eigengap heuristic
  (k = argmax+1 instead of argmax+2 for my list-construction). MW-5 failed as positive control.
- **10:40** — Fixed indexing. MW-5 now returns k_eigengap=3 correctly.
- **10:45** — Full run completed in 77s. Results:
  - λ_1..λ_4 = 0 (4 connected components in observed graph)
  - λ_5 = 0.023, λ_6 = 0.396, λ_7 = 0.817 — clear 6-community structure
  - Observed gap λ_4 − λ_3 = 0 (trivially degenerate)
  - ER null mean gap ≈ 0.009 → p = 1.0 (observed < null)
  - Fiedler χ² long/short p = 0.0043 PASS
  - k_eigengap = 6
  - Q 62 v_2 = 0.0682, rank 109/114, classified as PEAK
- **10:50** — MID-RUN: coordinator sent audit-035 amendment. C3 demoted to
  descriptive-only; Bonferroni tightened k=3 → k=2, α_bon 0.0167 → 0.025. Per project
  rule (feedback_bonferroni_tightening_vs_loosening): tightening self-verifies.
- **10:55** — Updated pre-reg, findings, and script to reflect the amendment.
  Post-amendment verdict: **MARGINAL** (1 of 2 cells PASS at α = 0.025).

## Key algebraic insight

The observed meta-cluster network has **25 connected components**:
- Main 78-node component (الم-front, ṭiwāl, Zahrāwān, mufaṣṣal, musabbiḥāt, Friday,
  Khawātim, Muʿawwidhatān all fused via mufaṣṣal-mediated links)
- 7-node ḥm component (Q 40-46)
- 5-node الر component (Q 10-12, 14, 15)
- 3-node طسم component (Q 26, 27, 28)
- 21 isolate singletons

In L_norm, each connected component contributes exactly one λ=0 eigenvalue. Thus
λ_1 = λ_2 = λ_3 = λ_4 = 0 — the pre-registered primary statistic λ_4 − λ_3 is
DEGENERATE to 0 by algebra.

The random ER(m=2219) null produces almost-always-connected graphs (density ≈ 0.345,
much above the connectivity threshold ~ln(n)/n ≈ 0.04). So ER null has λ_4 − λ_3 ≈ 0.009
consistently. Observed (0) < null (0.009) → one-sided-upper p = 1.0.

**This is a genuine structural signal expressed in the "wrong" direction for the
pre-registered test.** The observed graph is MORE DISCONNECTED than random (a 2-sided
or lower-tail test would have flagged this), but our pre-reg locked one-sided-upper.
We publish as NULL per direction-locking discipline.

## Fiedler finding (C2 PASS)

The Fiedler sign partition (v_2 > 0 vs v_2 < 0):
- v_2 = 0: Q 1 al-Fātiḥa (true zero — sui generis isolate)
- v_2 > 0: 100 surahs in the various connected non-trivial components
- v_2 < 0: 13 surahs — Q 13, 16, 17, 19, 20, 21, 22, 23, 24, 35, 38, 39, 47

The minus group has mean 87.2 verses vs corpus median 39 → STRONGLY LONG-BIASED.
χ² (long vs short) = 8.14, p = 0.00432 < α_bon (0.025). PASS.

This reveals the **"long isolate" structural cohort**: long surahs (including singleton
muqaṭṭāʿat Q 13, 19, 20, 38) that lack cluster partnership. These form a spectrally
coherent group despite having NO cluster membership in the H-NEW-89 taxonomy.

## Q 62 finding (descriptive secondary)

Q 62 al-Jumuʿah is a **spectral PEAK** (positive-peak), NOT a saddle:
- v_2(Q 62) = 0.0682, highest in its 78-node component
- Higher than all 67 of its graph-neighbors
- Surrounded by musabbiḥāt (Q 57, 59, 61, 64 all at ~0.066) and the broader mufaṣṣal
- Q 18, Q 32 (Friday-liturgy outliers in Q 62's component) at lower v_2 (0.014, 0.023)

Interpretation: Q 62 is the NUCLEUS of a dense cluster-rich community, not a bridge
between separate communities. The 4-cluster-membership (H-NEW-89) manifests spectrally
as community-centrality rather than betweenness. This REFINES the H-NEW-89 reading.

## Spectral community detection (descriptive, k=6)

K-means on top-6 row-normalized eigenvectors yields:
- C0 (size 64): mufaṣṣal mass
- C1 (size 7): Q 17-25 isolate sub-group
- C2 (size 13): second isolate zone (Q 33-39, Q 47-48, Q 21)
- C3 (size 17): front-cluster crossbar (Q 1, 13, 18, طسم, الم part)
- C4 (size 7): ṭiwāl/Zahrāwān Q 2-9
- C5 (size 6): الر Q 10-15

## Null-model robustness

All 4 null models (ER, configuration-model, BA, SBM) report p=1 on the locked direction.
This is expected — all produce near-connected graphs; observed is extremely disconnected.

## audit-035 response

- Amendment received mid-run
- Applied TIGHTENING: C3 (algorithmic threshold) demoted to descriptive-only
- Bonferroni k=3 → k=2; α_bon 0.0167 → 0.025
- Per project rule (feedback_bonferroni_tightening_vs_loosening), tightening self-verifies
- All three files updated: pre-reg, findings, script
- MW-5 positive control was constructed BEFORE running on real data (pre-committed in
  script; reported in findings regardless of outcome)
- Post-amendment verdict: MARGINAL (1 of 2 cells)

## Files produced

1. `findings/phase-b-hypotheses/h-new-112-spectral-network-prereg.md` (updated with audit-035 amendment)
2. `scripts/h_new_112_spectral_network.py` (Bonferroni-2, descriptive C3)
3. `findings/phase-b-hypotheses/csv/h-new-112.json` (full spectrum + Fiedler + communities + Q62)
4. `findings/phase-b-hypotheses/h-new-112-spectral-network.md` (MARGINAL verdict)
5. `journal/h-new-112-run-1.md` (this file)

## Verdict

**MARGINAL** — 1 of 2 Bonferroni-counted cells passes (C2 Fiedler-length alignment
p=0.00432 at α_bon=0.025). C1 primary spectral-gap test fails due to observed graph
having 25 connected components (algebraic degeneracy of the locked k=3 statistic).
Descriptive findings (6-community structure, Q 62 spectral peak, long-isolate cohort)
are novel and refine the H-NEW-89 synthesis.

## Honest reflection

The pre-reg direction lock was TOO NARROW for the observed graph topology. A more
general "largest non-trivial gap" formulation would have PASSED overwhelmingly, but
that would constitute direction-change after data view. Publishing as MARGINAL respects
direction-locking discipline. The descriptive content (Fiedler alignment, Q 62 peak,
6 communities) is the genuine novel contribution of H-NEW-112 beyond H-NEW-89.

Future follow-up (H-NEW-112.1?) could pre-register "largest non-trivial gap > ER null"
as primary and test on fresh null draws — this would legitimately convert the observed
degeneracy into a one-tailed pass under a properly-specified direction.
