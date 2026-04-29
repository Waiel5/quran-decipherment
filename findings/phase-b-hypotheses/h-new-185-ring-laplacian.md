---
id: h-new-185
title: "Spectral graph Laplacian analysis of the mushaf ring"
phase: B (specialist)
status: WEAK-PASS (gap only); H1a NULL, H1b PASS
date: 2026-04-17
specialist: h-new-185-specialist
seed: 20260419
bonferroni_family: h-new-185-ring-laplacian
bonferroni_k: 2
alpha_bon: 0.025
parent_findings:
  - cross-finding-013 (mushaf = structured Hamiltonian cycle, CONFIRMED)
  - H-NEW-111 (Fisher-Rao D matrix, CONFIRMED)
  - cross-finding-019 (Q 50 Qaf mid-mushaf pivot, exemplar-level)
rules_tuple: "(no-tashkeel, QAC-STEM root tokens K=500, QAC v0.4, Dirichlet-0.5, L1-norm, mushaf ring topology, Hafs-Kufan, Fisher-Rao angular distance)"
verdict_ceiling: "PASS-DIRECTED (gap-only); CONFIRMED requires replication"
---

# [[h-new-185-ring-laplacian|H-NEW-185]] — Spectral graph Laplacian analysis of the mushaf ring

## Headline

The 114-surah mushaf ring weighted by Fisher-Rao distance has a
**spectral gap λ_2 − λ_1 that is 5.9 σ above the random-rewiring null
(p = 0.0001, k=2 Bonferroni)**. The Fiedler partition is sharply
defined: ONE community is the long/structural block Q 13–Q 77, the
OTHER is the bracketing block Q 78–Q 114 ∪ Q 1–Q 12. The Q 1 ↔ Q 114
wrap-around edge is INSIDE the same community (consistent with CF-013
ring topology). However, the Fiedler partition **does NOT align with
the Q 50 pre-registered pivot** (observed sign-flip at Q 12/Q 13 and
Q 77/Q 78; Q 50 is interior to the Q 13–Q 77 community). H1a NULL,
H1b PASS.

## Pre-registered tests and outcomes

| Hyp | Test | p | α_bon | Verdict |
|:---|:---|:---:|:---:|:---:|
| H1a | Fiedler sign-flip within ±5 positions of Q 50 | 0.9628 | 0.025 | **NULL** (strongly null) |
| H1b | Spectral gap Δ = λ_2 − λ_1 > null (upper tail) | 0.0001 | 0.025 | **PASS** (z=+5.89) |

Combined verdict: **WEAK-PASS (gap only)**.

## Spectrum details

- λ_0 = 8.52e-16 (numerical zero; sanity PASS)
- λ_1 = 0.001182 (Fiedler / algebraic connectivity)
- λ_2 = 0.001855
- λ_3 = 0.005518
- Δ = λ_2 − λ_1 = 0.000673
- λ_max = ~2.0 (normalized-Laplacian upper bound)

## Fiedler partition — actual communities

The Fiedler vector has exactly **2 sign-flip positions** on the ring:

- Flip 1: between Q 12 and Q 13
- Flip 2: between Q 77 and Q 78

This carves the ring into two contiguous arcs:

- **Community A (Fiedler < 0, 65 surahs)**: Q 13 ... Q 77
  — the "middle block" containing the Late-Meccan / Medinan
  long-surah corpus. Top community-hub surahs (|v_1| largest):
  Q 45 al-Jāthiyah, Q 44 al-Dukhān, Q 40 Ghāfir, Q 41 Fuṣṣilat,
  Q 51 al-Dhāriyāt, Q 46 al-Aḥqāf, Q 48 al-Fatḥ.
  **These are the Ḥawāmīm + neighbors** — the dense Late-Meccan
  muq-cluster. They form the core of Community A.
- **Community B (Fiedler > 0, 49 surahs)**: Q 78 ... Q 114 ∪ Q 1 ... Q 12
  — the "short-surah bracket" wrapping around the Q 114 → Q 1
  closure. Top hubs: Q 107 al-Māʿūn, Q 108 al-Kawthar, Q 106 Quraysh.

The wrap-around edge Q 114 ↔ Q 1 is INTERNAL to Community B,
consistent with CF-013's finding that this edge is content-short
and represents the ring's closure within a single coherent region.

## Why H1a failed and what it means

Pre-registration predicted the Fiedler sign-flip would land near Q 50
(the CF-019 pivot). Instead it lands at two boundaries that are
**each ~28 ring positions away from Q 50**. The observed minimum
distance-to-Q-50 is **27**, versus null mean of 14.3. The p-value of
0.96 means the Fiedler partition is FURTHER from Q 50 than a random
rewiring would produce. This is an informative null: the Q 50 pivot
is a **local structural hinge** (CF-019 exemplar), not a **global
spectral-bisection point**.

The actual spectral bisection boundaries (Q 12/Q 13 and Q 77/Q 78)
are themselves interpretable:

- **Q 12 → Q 13**: boundary between Yūsuf (narrative block closing
  with Yūsuf-cycle) and al-Raʿd (transition into the mid-mushaf
  Hawāmīm preamble region). Q 13 opens with an ALM-R muqaṭṭaʿ.
- **Q 77 → Q 78**: boundary between al-Mursalāt (last of the early
  eschatological mid-surahs) and al-Nabaʾ (start of Juzʾ 30 ʿamma —
  the classical liturgical short-surah block). **This is a
  classically-recognized structural break**: Juzʾ 30 begins at Q 78.

Neither boundary was pre-specified, so this is descriptive not
inferential. But it is notable that the spectral bisection boundary
at Q 77/Q 78 coincides with the **Juzʾ-30 classical boundary**, a
liturgically-defined mushaf division. That classical-scholarship
alignment is consistent with the project's meta-theme.

## Spectral-gap interpretation (H1b PASS)

Δ_obs = 0.000673 vs null mean 0.000165 (sd 0.000086). The null gap
maxes out at 0.000559 across 10,000 random rewirings — the observed
gap **exceeds every single null value** (0/10,000), giving
p = 1/10001 = 0.0001. z = +5.89.

Meaning: the mushaf's two communities (Ḥawāmīm-core vs wrap-around
bracket) are **substantially more tightly defined** than a random
ring-weight assignment would produce. This is a genuine signature of
global community structure on the mushaf ring, beyond the local
Hamiltonian-cycle optimality established by CF-011/CF-013.

## λ_2 eigenvector centrality (descriptive)

Top-10 surahs by |v_2|:

Q 73 al-Muzzammil, Q 81 al-Takwīr, Q 72 al-Jinn, Q 74 al-Muddaththir,
Q 82 al-Infiṭār, Q 18 al-Kahf, Q 78 al-Nabaʾ, Q 71 Nūḥ,
Q 19 Maryam, Q 22 al-Ḥajj.

This is a mix of:
- Early Meccan muzzammil-muddaththir-Nabaʾ-block (Q 71–82)
- Mid-mushaf narrative-expansion (Q 18 Kahf, Q 19 Maryam, Q 22 Ḥajj)

These are the surahs that carry the SECOND mode of variation after
the Fiedler bisection — they distinguish the narrative/prophetic
material from both the Ḥawāmīm core and the short-surah bracket.

## Honest caveats

1. **WEAK-PASS at raw level; not CONFIRMED**. Only H1b passed. H1a
   NULL is informative but does not advance the pre-registered axis
   claim. Verdict ceiling: PASS-DIRECTED on the spectral-gap claim
   pending char-4-gram replication.
2. **Descriptive post-hoc observation** that the Q 77/Q 78 boundary
   equals Juzʾ 30 start is NOT pre-registered. Flagged for FUTURE
   pre-reg (H-NEW-185b: does the Fiedler bisection boundary align
   with the Juzʾ-30 classical boundary under char-4-gram features?).
3. **Normalization choice**: affinity = 1/(w+ε) is one of several
   reasonable choices; Gaussian affinity with tuned bandwidth σ could
   yield different community definitions. Pre-reg locked 1/(w+ε) to
   avoid forking-path concerns; alternative would be a separate test.
4. **Dependent on [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D matrix** (roots feature, K=500). If
   char-4-gram or verse-length D matrix yields a different Fiedler
   partition, the community structure is feature-specific; if they
   agree, feature-orthogonal.
5. **Inflated-independence**: this analysis is NOT independent of
   CF-013 (same D matrix, same ring). It tests a COMPLEMENTARY
   property of the same structure. Counts as mechanism-clarification,
   not independent replication.

## Connection to the unified model

[[cross-finding-013-mushaf-topological-ring|cross-finding-013]] established the ring's **topological** property
(Hamiltonian cycle, geodesic, wrap-around closure). [[h-new-185-ring-laplacian|H-NEW-185]]
establishes a **spectral** property of the same ring: it has tight
community structure (PASS) with the bisection boundary at Juzʾ 30's
classical start (descriptive). The Fiedler partition does NOT
bisect at the CF-019 Q 50 pivot (pre-reg NULL); the Q 50 hinge is a
local-boundary phenomenon, not a global-bisection phenomenon.

**Refinement to M1**: the mushaf is a structured Hamiltonian cycle
(M1) whose spectrum has an unusually large λ_2 − λ_1 gap, producing
two tightly-defined content-communities:
- The dense Late-Meccan Ḥawāmīm-core block Q 13–Q 77
- The short-surah bracket Q 78–Q 114 + Q 1–Q 12

The latter community INCLUDES al-Fātiḥa (Q 1), confirming Q 1's
content-proximity to the muʿawwidhatān/khawātim documented in
[[h-new-137-wrap-around-closure|H-NEW-137]]/138 (CF-013 Layer 2). Q 1 sits inside the same Fiedler
community as Q 114 — a spectral witness of the wrap-around closure.

## Top-centrality surahs (summary)

| Eigenvector | Top-3 surahs | Interpretation |
|:---:|:---|:---|
| v_1 (Fiedler) | Q 107, Q 108, Q 45 | Community boundary hubs |
| v_2 | Q 73, Q 81, Q 72 | Early-Meccan short-surah block |

## Output files

- `findings/phase-b-hypotheses/h-new-185-ring-laplacian-prereg.md` (pre-reg)
- `scripts/h_new_185_ring_laplacian.py` (analysis)
- `findings/phase-b-hypotheses/csv/h-new-185.json` (full summary + spectrum + null distribution)

## Verdict

**WEAK-PASS (gap only)**. H1b (spectral gap > null) PASSES at
p = 0.0001, z = +5.89. H1a (Fiedler partition aligns with Q 50)
is strongly NULL (p = 0.96). The mushaf ring has tighter-than-random
community structure, but the community bisection does NOT coincide
with the Q 50 mid-mushaf pivot — it coincides instead (descriptive,
not pre-registered) with the Juzʾ-30 classical liturgical boundary
at Q 78. Future replication on char-4-gram features is required
before CONFIRMED upgrade.
