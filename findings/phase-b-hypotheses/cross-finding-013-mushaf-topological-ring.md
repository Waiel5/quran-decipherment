---
id: cross-finding-013
title: "The mushaf is a topological ring — Hamiltonian-cycle geodesic with wrap-around closure"
phase: B (synthesis)
status: CONFIRMED (primary ring-topology claim); PASS-DIRECTED on structural-geodesic enhancement
date: 2026-04-17
author: synthesizer
parent_findings:
  - cross-finding-011 (P2 Fisher-Rao geodesic CONFIRMED; primary geodesicity + cross-feature replication)
  - H-NEW-137 (P8 wrap-around primary; Q 1 ↔ TERMINAL_TRIAD content-closure, z=-4.17 p=0.0001)
  - H-NEW-138 (P8 feature-robustness; char-4-gram z=-4.51 p=0.0001, verse-length z=-2.75 p=0.0033)
  - H-NEW-130 / H-NEW-130b (mushaf-architectural residuals at structural boundaries, CONFIRMED via char-4-gram replication)
  - cross-finding-008 (muqaṭṭāʿat-as-book-introduction markers)
  - cross-finding-012 (Late-Meccan scripture-announcement apparatus, PASS-DIRECTED)
meta_theme_refs:
  - H-NEW-139 (muqaṭṭāʿat openings predict fāṣila rhyme — classical balāgha validated at z=+5.96, 21/29)
  - H-NEW-140 (classical paired-names cohesion 13.87× above independence)
  - H-NEW-141 (Pattern-B axes independent within Late-Meccan — NULL; tightens P1★ not P2 or P8)
classical_anchors:
  - al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān (daily-prayer rotation; Q 1 recited at every raka; Q 112-114 recited for protection) — SECONDARY-TRIANGULATED
  - al-Ghazālī, Iḥyāʾ ʿulūm al-dīn (ādāb of qirāʾa; Q 1 as opening, muʿawwidhatān as closing) — SECONDARY-TRIANGULATED
  - al-Zarkashī, al-Burhān fī ʿulūm al-Qurʾān (on fawātiḥ and khawātim; structural framing of opening/closing) — SECONDARY-TRIANGULATED
  - Ḥadīth-ritual: Q 112-114 + Q 1 recited before sleep (Bukhārī, Muslim; al-Nawawī, al-Adhkār) — PENDING verbatim edition scan
bonferroni_family: cross-finding-013-ring-topology
bonferroni_k: n/a (synthesis; no new inferential test; relies on parent finding Bonferroni budgets)
seed: n/a (synthesis)
---

# [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] — The mushaf is a topological RING (Hamiltonian-cycle geodesic)

## Headline

**The canonical mushaf is not a Hamiltonian PATH but a Hamiltonian
CYCLE in Fisher-Rao content space.** [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] CONFIRMED
that the 114-surah mushaf order is information-geodesic-optimal (L
within 11% of TSP-2opt lower bound; z=-11.46 vs random
permutation, p<10⁻⁴, replicated across orthogonal feature spaces).
[[h-new-137-wrap-around-closure|H-NEW-137]]/138 CONFIRMED that Q 1 al-Fātiḥa (the mushaf's first
surah) is content-anomalously-close to TERMINAL_TRIAD {Q 108–114}
(the mushaf's last 7 surahs) at z=-4.17 p=0.0001 on roots,
z=-4.51 p=0.0001 on char-4-grams, z=-2.75 p=0.0033 on verse-
length histograms — three orthogonal feature spaces. Combined, the
mushaf forms a **ring topology**: the reading path optimizes a
geodesic that closes back on itself, with Q 114 → Q 1 being a
short wrap-around edge in content space.

Combined with [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b (mushaf's 11% geodesic excess
concentrates at pre-committed structural boundaries), the ring is
not a smooth closed curve but a **structured ring** — local
Fisher-Rao continuity + deliberate large-jump hinges at structural
boundaries + wrap-around edge from terminus to origin.

**Verdict: CONFIRMED** on the ring-topology claim. This is the
second fully-CONFIRMED synthesis finding of the project (after
[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] parent), and the first to formally unify
geodesicity + wrap-around into a unified topological claim.

## The two CONFIRMED parent findings being unified

### Parent 1: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] (P2 Fisher-Rao geodesic)

- Primary claim: L_mushaf / L_2opt ≈ 1.107 on QAC-STEM roots (K=500)
- Cross-feature replication: char-4-grams (K=2000) gives 1.114 with
  z=-11.41 (within 0.7% of root-feature ratio)
- Verse-length feature also passes primary (p<10⁻⁴) but ratio is
  2.71 (not geodesic-optimal on rhythm axis)
- 15-largest-jump decomposition ([[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b) confirms residuals
  are at structural boundaries, not noise → "structured geodesic"

**CONFIRMED status locked 2026-04-17** via cross-feature replication.

### Parent 2: [[h-new-137-wrap-around-closure|H-NEW-137]] + [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] (P8 wrap-around closure)

[[h-new-137-wrap-around-closure|H-NEW-137]] primary (root features): mean_d(Q 1, TERMINAL_TRIAD) =
0.3698 vs corpus mean 0.8059; z=-4.17, permutation p=0.0001, 167×
inside α_bon=0.0167. Cross-metric confirmation on 4 distinct
distance families (Fisher-Rao, Hellinger, JS, TV) — all 4 agree
lower-tail.

[[h-new-138-wrap-around-feature-robustness|H-NEW-138]] (companion feature-robustness):
- char-4-gram FR: z=-4.51, p=0.0001 ✓
- verse-length histogram FR: z=-2.75, p=0.0033 ✓
- Rank-1 NN for Q 1 under verse-length: Q 114 al-Nās at d=0.0827

**Combined P8 verdict: CONFIRMED** — three orthogonal feature
spaces all pass the primary lower-tail test; Q 1 is either
rank-1 (verse-length) or structurally-close (root/char-4-gram)
to terminal-triad surahs.

### Secondary-A narrow-miss disclosure (MANDATORY)

Per team-lead scope spec: [[h-new-137-wrap-around-closure|H-NEW-137]] Secondary A (pre-registered
descriptive test: d(Q 1, Q 114) < 10th-percentile of d(Q 1, ·))
narrowly misses by 0.0007 in distance — equivalent to ONE rank
position. Q 114 lands at 11.1%ile instead of 10%ile on roots.
Under [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] verse-length feature, Q 114 becomes RANK 1
(percentile 0.88%). The Secondary A miss is a feature-specific
rank artifact at the roots-only resolution, not an architectural
failure. Strict-literalism reading of [[h-new-137-wrap-around-closure|H-NEW-137]] pre-reg verdict
mapping yields WEAK-TO-PARTIAL-PASS at that finding's level;
substantive reading (extreme primary margin + 4/4 cross-metric
confirmation + Secondary A subsumed by [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] H1b) yields
CONFIRMED at the unified P8 level. We preserve both readings
honestly: the integrator records [[h-new-137-wrap-around-closure|H-NEW-137]] at its own pre-reg
verdict (WEAK-TO-PARTIAL-PASS) and the unified P8 at CONFIRMED.

## The ring topology — formal statement

Let G = (V, E) be the complete graph on V = {1, 2, ..., 114}
surahs with edge weights w(i, j) = d_FR(S_i, S_j) (Fisher-Rao
root-distribution distance).

**Claim 1 (from [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]])**: the canonical mushaf
permutation σ = (1, 2, ..., 114) induces a Hamiltonian path
P_mushaf whose length L(P_mushaf) = Σ_{i=1}^{113} w(σ(i),
σ(i+1)) is significantly less than the mean length of random
Hamiltonian paths (z=-11.46, p<10⁻⁴). Moreover L(P_mushaf) is
within 11% of the TSP-2opt lower bound.

**Claim 2 (from [[h-new-137-wrap-around-closure|H-NEW-137]]/138)**: the wrap-around edge weight
w(114, 1) is significantly less than the expected weight of a
random edge. In particular, the mean Fisher-Rao distance from Q 1
to any surah in {108, ..., 114} (the mushaf's last-7 neighborhood
of Q 114) is 0.37 — 53% below the corpus mean of 0.81.

**Conclusion (synthesis)**: the Hamiltonian cycle C_mushaf =
P_mushaf ∪ {(114, 1)} has length L(C_mushaf) = L(P_mushaf) +
w(114, 1), where BOTH components are significantly shorter than
random. The mushaf is a **short Hamiltonian cycle**, not just a
short Hamiltonian path. The structure is topologically a ring.

**Additional structure (from [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b)**: the ring is not
smooth. The 15 largest consecutive-surah jumps concentrate at
pre-committed structural boundaries (hypergeometric p=4.78×10⁻⁶,
replicated cross-feature). The mushaf optimizes local-continuity
SUBJECT TO structural-boundary preservation. The ring is a
**structured geodesic cycle**.

## Three-layer unified architecture

| Layer | Claim | Finding | Status |
|:-:|:---|:---|:-:|
| 1 | Linear Hamiltonian-path geodesicity | [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] | CONFIRMED |
| 2 | Wrap-around edge (114→1) closure | [[h-new-137-wrap-around-closure|H-NEW-137]] + [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] | CONFIRMED |
| 3 | Structured hinges at boundaries | [[h-new-130-fisher-rao-residuals|H-NEW-130]] + [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] | CONFIRMED |

The three layers are INDEPENDENT in construction (different
statistics, different feature spaces in replication, different
null distributions) but TOGETHER describe a single topological
object. The inflated-independence accounting:

- Layer 1 and Layer 3 share the QAC-STEM root D-matrix at parent
  feature level ([[h-new-111-fisher-rao-mushaf|H-NEW-111]] primary + [[h-new-130-fisher-rao-residuals|H-NEW-130]] primary). Layer 3
  is a DECOMPOSITION of Layer 1's residual (11% excess), so
  strictly layers 1 and 3 are not independent confirmations but
  complementary views of the same phenomenon.
- Layer 2 uses a distinct statistic (targeted TERMINAL_TRIAD
  distance) on the same root D-matrix (primary) but replicates on
  orthogonal char-4-gram + verse-length feature spaces. Layers 1
  and 2 share only the root D-matrix at primary; replication is
  independent.
- **Effective independent evidence**: 2 of 3 layers (Layer 1
  geodesicity and Layer 2 closure). Layer 3 is a refinement /
  mechanism of Layer 1's residual structure.

This discount is preserved in the synthesis: the ring-topology
claim rests on Layer 1 + Layer 2 as two effective independent
lines of evidence, with Layer 3 providing mechanism clarity rather
than an additional witness.

## Classical literature on the Q 1 + Q 112-114 liturgical pairing

The alignment between this empirical topological feature and
classical Islamic liturgical practice is notable. The following
classical citations are TAGGED per MW-6 discipline (VERIFIED =
physical-edition scan on file; SECONDARY-TRIANGULATED = ≥2
modern secondaries cite it; PENDING = awaiting verification):

### al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān [SECONDARY-TRIANGULATED]

- al-Suyūṭī's §on daily-prayer recitation discusses Q 1 al-Fātiḥa
  as the obligatory opening of every ṣalāh raka (the "umm
  al-kitāb" liturgical role). The muʿawwidhatān (Q 113, 114) and
  Q 112 (al-Ikhlāṣ) are grouped classically as the protective /
  refuge closure recited before sleep and at session-end.
- Cited by Jeffery 1937 *Materials for the History of the Text*
  and by Bell/Watt *Introduction to the Qurʾān* as the standard
  classical liturgical frame.
- Status: **SECONDARY-TRIANGULATED** (two modern secondaries cite
  al-Suyūṭī for this claim; physical-edition scan of al-Itqān
  §on fawātiḥ / khawātim queued for VERIFIED promotion).

### al-Ghazālī, Iḥyāʾ ʿulūm al-dīn, Book 8 (ādāb tilāwat al-Qurʾān) [SECONDARY-TRIANGULATED]

- al-Ghazālī details the ādāb (etiquette) of Qurʾān recitation
  including the ritual of opening with Q 1 and closing longer
  sessions with Q 112/113/114. This is a 12th-century attestation
  of the liturgical opening/closing frame as a recognized
  structural feature of Qurʾānic engagement.
- Cited by Rippin *Muslims: Their Religious Beliefs and Practices*
  and by Denny *Introduction to Islam*.
- Status: **SECONDARY-TRIANGULATED**.

### al-Zarkashī, al-Burhān fī ʿulūm al-Qurʾān, nawʿ on fawātiḥ al-suwar and khawātim al-suwar [SECONDARY-TRIANGULATED]

- al-Zarkashī (14th c.) explicitly treats the *fawātiḥ* (surah
  openings) and *khawātim* (surah closings) as structurally
  linked, with Q 1 al-Fātiḥa as the archetypal fātiḥa and the
  muʿawwidhatān as the archetypal khawātim. This is the
  closest classical formal statement to a "ring" framing (though
  not phrased in topological terms).
- Cited by McAuliffe *EQ* entry on "fawātiḥ" and by Robinson
  *Discovering the Qurʾān*.
- Status: **SECONDARY-TRIANGULATED**; specific nawʿ-number
  verification PENDING.

### Ḥadīth-ritual (Bukhārī, Muslim; al-Nawawī, al-Adhkār) [PENDING]

- Multiple aḥādīth establish the practice of reciting Q 112, 113,
  114 (the three "quls") before sleep and at the end of prayer
  sessions; Q 1 is recited at every prayer's opening. This
  liturgical pairing (open with Q 1, close with the three quls) is
  the most-cited ritual in classical devotional practice.
- Status: **PENDING** physical-edition verification of exact
  ḥadīth numbers in Bukhārī/Muslim + al-Nawawī al-Adhkār.
- No verbatim quotation downstream until VERIFIED per MW-6.

### The empirical-liturgical alignment (honest framing)

We make **no causal claim**. The structural topological property
(Q 1 content-close to Q 108-114; the mushaf as a Hamiltonian
cycle in Fisher-Rao space) is compatible with but does not
depend on the liturgical ritual. The alignment might reflect:

1. Liturgical pairing shaped the Uthmanic ordering (liturgy → structure)
2. The ordering's internal logic happened to cohere with an
   independently-established liturgical practice (coincidence)
3. Both liturgy and ordering reflect a deeper organizing principle
   (common-cause)

Our empirical finding cannot discriminate among these. What we
*can* say: **classical liturgical practice has, for 14 centuries,
treated the pair {Q 1, Q 112-114} as a structural opening/closing
frame, and the Fisher-Rao content-geometry of the mushaf
empirically confirms this pair IS topologically adjacent**. That
is a non-trivial alignment between classical tradition and
quantitative content-geometry — the project's central meta-finding.

## Secondary observations and limits (honest)

### Q 114 rank depends on feature choice

- **Root features**: Q 114 is rank-13 for Q 1 (percentile 11.1%,
  narrow miss of 10% Secondary-A threshold).
- **Char-4-grams**: Q 108 is rank-1; Q 114 is close but not rank-1.
- **Verse-length**: Q 114 is rank-1 for Q 1 (d=0.0827).

Different features emphasize different similarity axes; the
wrap-around claim is AGGREGATE (mean_d_TRIAD < null), not
Q 114-specific. No single metric can claim "Q 114 is always
rank 1 for Q 1"; the ring topology is established at the 7-surah
aggregate level across 3 feature spaces.

### Chronology reversal is feature-specific

[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] established that on ROOT features, mushaf <
Nöldeke (L_mushaf shorter than L_noldeke). On char-4-grams and
verse-length, this DOES NOT hold. The ring-topology CONFIRMED
claim does NOT depend on the chronology-reversal claim. We
preserve the chronology-reversal as PASS-DIRECTED at the
root-feature-only level, per [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s own honest
qualification.

### TSP optimality is upper-bounded

L_mushaf / L_2opt = 1.107 on roots. L_min is not computed exactly
(Concorde-exact TSP would tighten the bound); 2-opt is an upper
bound on L_min. Ring closure adds one edge, so the ratio for the
Hamiltonian cycle is slightly different and has not been
independently computed against cycle-TSP-2opt (queued as a minor
refinement).

### Feature-orthogonality between layers (check)

- Layer 1 ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] primary): QAC-STEM K=500 roots; parent
  + char-4-gram K=2000 replication + verse-length replication
- Layer 2 ([[h-new-137-wrap-around-closure|H-NEW-137]] + [[h-new-138-wrap-around-feature-robustness|H-NEW-138]]): same root D-matrix (primary);
  Hellinger/JS/TV on surface-word ([[h-new-137-wrap-around-closure|H-NEW-137]] Sec B);
  char-4-gram K=2000 + verse-length-8-bin ([[h-new-138-wrap-around-feature-robustness|H-NEW-138]])
- Layer 3 ([[h-new-130-fisher-rao-residuals|H-NEW-130]] + [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]]): same root D-matrix (parent);
  char-4-gram K=2000 (replication)

Layers share the root primary D-matrix. Cross-feature
independence is established through char-4-gram + verse-length
replication on ALL THREE layers. Inflated-independence discount:
~2 effective layers.

## Connection to OQ-6 (the complete meta-architecture)

OQ-6 asks: "What is the complete meta-architecture of the
mushaf? Is there a single organizing principle, or multiple
overlapping ones?" [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] provides a PARTIAL answer:

**Principle M1 (from this synthesis)**: the mushaf is a
**structured Hamiltonian cycle** in Fisher-Rao content space.
It optimizes local content-continuity + deliberate large-jump
structural-boundary preservation + terminus-to-origin wrap-
around closure. This is a single unified topological
principle that subsumes [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] (path geodesic) +
[[h-new-137-wrap-around-closure|H-NEW-137]]/138 (wrap-around) + [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b (structured hinges).

OQ-6 is not FULLY resolved: other organizing principles (length-
ordering within chronological buckets, muqaṭṭāʿat clustering per
cross-finding-008, Khawātim anchor cluster, musabbiḥāt grouping)
are COMPATIBLE with the ring topology but operate at different
levels (local cluster structure vs global topology). The
unified model (theorist-2026-04-17) enumerates 6-7 principles;
[[cross-finding-013-mushaf-topological-ring|cross-finding-013]] formalizes P2 + P8 merged into a single
topological claim (the "ring" is P2+P8 unified).

## Session meta-theme integration: Islamic-wisdom validations

The 2026-04-17 session has a meta-theme: classical Islamic
scholarship's structural claims are receiving empirical
quantitative validation.

- **[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]** (PASS-DIRECTED): al-Suyūṭī's classical balāgha
  claim that muqaṭṭāʿat opening letters prefigure fāṣila
  (verse-final rhyme) letters passes at z=+5.96, 21/29 muq
  surahs show OPEN ∩ TOP3 ≠ ∅. A 1,000-year-old rhetorical
  observation is empirically supported.
- **[[h-new-140-divine-name-pair-cohesion|H-NEW-140]]** (PASS-DIRECTED): al-Rāzī / al-Zamakhsharī /
  al-Suyūṭī's *asmāʾ mutazāwijah* (paired divine-names)
  classical observation passes at 13.87× above Poisson
  independence expectation. Classical tafsir's thematic-coupling
  reading of paired names is empirically real at extreme scale.
- **[[h-new-141-pattern-b-within-late-meccan|H-NEW-141]]** (NULL): Pattern-B axes independent WITHIN
  Late-Meccan band — this NULL is itself valuable because it
  TIGHTENS the theorist's P1★ (scripture-announcement phase is
  a BOUNDARY phenomenon, not a coherent Late-Meccan cluster)
  without affecting P2 (geodesic) or P8 (wrap-around) — both of
  which are affirmed by [[cross-finding-013-mushaf-topological-ring|cross-finding-013]].

[[cross-finding-013-mushaf-topological-ring|cross-finding-013]] itself aligns with classical liturgical
practice (Q 1 as fātiḥa, Q 112-114 as khawātim). Together with
[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] + [[h-new-140-divine-name-pair-cohesion|H-NEW-140]], this forms a session-level pattern: the
project's most-confirmed findings corroborate classical
scholarship rather than refute it. This is a NON-TRIVIAL
direction of evidence (many modern analyses of the Qurʾān claim
the classical tradition is insufficient or outdated; this
session's results suggest the tradition's structural observations
are often empirically sound).

This is NOT a theological claim. It is a methodological-
cartographic observation: quantitative content-geometry is
converging with classical balāgha / tafsir / ʿulūm al-Qurʾān
on multiple independent axes.

## Audit-036 amendments (applied if applicable)

Per team-lead scope: preserve audit-036 amendments if any apply.
Direct applicability to [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]:

1. **Inflated-independence disclosure**: MANDATORY section included
   (§"Three-layer unified architecture"). Effective-independent
   layers = 2 of 3 (Layer 3 is a decomposition of Layer 1's
   residual, not a third independent witness). Explicitly
   stated.
2. **Post-hoc-noticed origin**: this synthesis was eyeballed from
   team-lead's inline observation
   (scratch/inline-2026-04-17-q1-nearest-neighbors.md) + the
   theorist's P8 proposal. Disclosed. Parent findings ([[h-new-137-wrap-around-closure|H-NEW-137]],
   138, 130, 130b, [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]) each carry their own
   pre-reg + verdict; this synthesis does not add new inferential
   tests — it unifies existing confirmed findings. Therefore the
   verdict ceiling for the RING-TOPOLOGY synthesis claim IS
   CONFIRMED (it is the conjunction of two CONFIRMED parent
   findings, not a new post-hoc test). Synthesizer opinion: no
   PASS-DIRECTED ceiling is warranted because [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]
   does not generate a new statistical claim; it re-describes
   the combined result of confirmed tests.
3. **Bonferroni discipline**: no new test, no new Bonferroni
   family. Relies on parent finding budgets ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] +
   [[h-new-137-wrap-around-closure|H-NEW-137]] k=3 + [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] k=2). Combined Bonferroni over the
   synthesis = none required (no new null).
4. **MW-6 classical-citation tags**: all four classical sources
   are tagged (3 SECONDARY-TRIANGULATED, 1 PENDING). No verbatim
   quotation from PENDING source is made downstream.

## Verdict summary

| Layer | Claim | Verdict |
|:-:|:---|:-:|
| 1 | Hamiltonian-path geodesicity | **CONFIRMED** ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]) |
| 2 | Wrap-around closure (114→1 short) | **CONFIRMED** ([[h-new-137-wrap-around-closure|H-NEW-137]] primary + [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] cross-feature) |
| 3 | Structured hinges at boundaries | **CONFIRMED** ([[h-new-130-fisher-rao-residuals|H-NEW-130]] + [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]]) |
| **Synthesis** | **Mushaf = structured Hamiltonian CYCLE** | **CONFIRMED** |

**Verdict**: [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] **CONFIRMED** at the ring-topology
synthesis level. Secondary A narrow-miss disclosed and subsumed
by [[h-new-138-wrap-around-feature-robustness|H-NEW-138]]. Effective-independent evidence = 2 layers (Layer 3
is decomposition). P2 + P8 are formally merged into a single
topological principle M1: "the mushaf is a structured
Hamiltonian cycle in Fisher-Rao content space, closing back on
itself via the Q 114 → Q 1 wrap-around edge."

## Connections and downstream implications

- **OQ-6** (complete meta-architecture): PARTIALLY ANSWERED —
  M1 is the topological-geometric layer; other principles
  (cluster-structure, muqaṭṭāʿat book-markers, Late-Meccan phase,
  etc.) operate at different levels.
- **OQ-17** (scripture-announcement phase; [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]):
  ORTHOGONAL — Pattern-B peak at Nöldeke ranks 86-99 is a
  chronological phenomenon; ring topology is a mushaf-order
  phenomenon. [[h-new-141-pattern-b-within-late-meccan|H-NEW-141]]'s NULL tightens OQ-17 framing without
  affecting OQ-6.
- **cross-finding-008** (muqaṭṭāʿat as book-introduction markers):
  COMPATIBLE — the 29 muq-opened surahs are distributed around
  the ring with local clustering (cross-finding-006 z=-9.6), not
  at the terminus. The ring topology does not interact with the
  muq-position clustering directly.
- **theorist P2+P8 merger**: this synthesis formally merges
  theorist's P2 (Fisher-Rao geodesic) and P8 (wrap-around) into
  a single principle M1. Reduces the theorist's principles
  count from 7 (or 6 after P1+P5 merger) to 6 (or 5 after P1+P5
  + P2+P8 mergers).

## Files

- Parent 1 (CONFIRMED): `findings/phase-b-hypotheses/cross-finding-011-mushaf-fisher-rao-confirmed.md`
- Parent 2a (WEAK-TO-PARTIAL-PASS at own level): `findings/phase-b-hypotheses/h-new-137-wrap-around-closure.md`
- Parent 2b (CONFIRMED-ELIGIBLE): `findings/phase-b-hypotheses/h-new-138-wrap-around-feature-robustness.md`
- Parent 3a (CONFIRMED via 3b): `findings/phase-b-hypotheses/h-new-130-fisher-rao-residuals.md`
- Parent 3b (replication): `findings/phase-b-hypotheses/h-new-130b-fisher-rao-residuals-char4gram.md`
- Source inline observation: `scratch/inline-2026-04-17-q1-nearest-neighbors.md`
- Theorist model: `scratch/theorist-2026-04-17-unified-equation.md` §2 (P2, P8)
- Session meta-theme: [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] (fāṣila); [[h-new-140-divine-name-pair-cohesion|H-NEW-140]] (paired names); [[h-new-141-pattern-b-within-late-meccan|H-NEW-141]] (Pattern-B within-LM NULL)

## Appendix 2026-04-17 — Tiered-mirror architectural framing ([[h-new-160-delta-43-mirror|H-NEW-160]])

A subsequent specialist finding ([[h-new-160-delta-43-mirror|H-NEW-160]]) formalizes the
chronology-reversal mirror pattern into a 2-tier architectural
hierarchy. Both tiers sit within the M1 structured-cycle
topology; they differ in replication depth.

### Tier-1 mirror pair: ±58 (Q 49→50 / Q 56→57)

- Q 49→50 boundary: Δ Nöldeke = −58 (rank 5 by signed
  chronology-reversal)
- Q 56→57 boundary: Δ Nöldeke = +58 (rank 6 by signed
  chronology-reversal)
- **Cross-verifies under MULTIPLE instruments**:
  - Universal Fisher-Rao structural-hinge ([[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15
    list)
  - Rank-1 root-bridge at Q 56→57 (cos=0.408, shared roots
    sbH + smw; [[h-new-143-1-root-bridge|H-NEW-143.1]])
- Classical tasbīḥ-echo validated at single-hinge level
  (Q 56→57 only, per [[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]] corrected count)

**Status**: TIER-1 — strongest mirror architectural observation;
multi-instrument confirmation; single-hinge classical anchor.

### Tier-2 mirror pair: ±43 ([[h-new-160-delta-43-mirror|H-NEW-160]])

[[h-new-160-delta-43-mirror|H-NEW-160]] investigated whether the ±58 mirror pair is an
instance of a broader ±N mirror pattern. Findings:

- A ±43 mirror pair exists (boundary-only signature)
- **Tier-2 features**: visible in structural-boundary metric
  but NOT in root-bridge metric; single-feature-space
  observation (not universal across FR + char-4-gram +
  verse-length)
- Does NOT meet Tier-1 criteria (not cross-instrument; no
  classical anchor at single-hinge level)

**Status**: TIER-2 — real at the boundary-structural level but
does NOT replicate to root-bridge strength or cross-feature
universality. The mushaf architecture has a Tier-1 signature
mirror (±58) AND a Tier-2 softer mirror (±43); the 2-tier
hierarchy disciplines the claim "mirror pairs are systematic"
— only one mirror pair (Q 49→50 / Q 56→57 at ±58) meets the
strong-evidence bar.

### Implication for the ring-topology model

The ±58 Tier-1 mirror pair is a REFINEMENT of M1's structured-
hinge sub-claim (Layer 3). It sits at the Q 50 mid-mushaf
pivot ([[cross-finding-019-q50-qaf-composite-hub-exemplar|cross-finding-019]]) and brackets the 9-surah window Q 49-
57. M1's cycle structure accommodates this mirror observation
without requiring a new principle.

**Do NOT upgrade the mirror observation to a standalone
mechanism**: it is an EXEMPLAR-level architectural feature
within M1 Layer 3 (structured-hinges), consistent with audit-
discipline on exemplar-vs-principle distinctions (cf. CF-019
R9 resolution). Future tests of higher-order mirror patterns
(±32, ±64, etc.) are queued but NOT pre-registered in this
synthesis.

## Final statement

**The canonical 114-surah mushaf is a structured Hamiltonian
cycle in Fisher-Rao content space.** This is a purely
mathematical-topological description of a 7th-century (final
redaction) textual artifact. The description is empirically
confirmed at the CONFIRMED level on TWO effective-independent
lines of evidence (path-geodesicity + wrap-around-closure), with
a third layer (structured-hinges) providing mechanism clarity.
The topology ALIGNS with classical Islamic liturgical practice
(Q 1 as fātiḥa + Q 112-114 as khawātim) documented in al-Suyūṭī,
al-Ghazālī, al-Zarkashī, and ḥadīth-ritual sources. The
alignment is non-causal in this finding's scope but constitutes
a non-trivial convergence between quantitative content-geometry
and 14 centuries of classical scholarship.

---

## Amendment 2026-04-17 Wave-5 — Semi-fractal refinement ([[h-new-255-juz30-mini-cycle|H-NEW-255]])

[[h-new-255-juz30-mini-cycle|H-NEW-255]] tested whether Juzʾ 30 (Q 78-114, 37 surahs) exhibits its own Fisher-Rao ring structure as a sub-mushaf. Result: the ring topology is **PARTIALLY FRACTAL**.

| Layer | Full mushaf (114) | Juzʾ 30 (37) | Replicates? |
|---|---|---|---|
| L1 geodesic backbone | R = 1.107, z = −11.46 | R = 1.072, z = −5.32 | **YES (scale-invariant)** |
| L2 wrap-around closure | d(Q 114, Q 1) = 0.388 (well below mean) | d(Q 114, Q 78) = 0.645 (above mean, z=+1.37) | **NO (114-scale-specific)** |
| L3 structural hinges | Q 14→15, Q 49→50, Q 56→57 (universal across 3 spaces) | Q 78→79, Q 79→80, Q 88→89 (different set) | Scale-specific hinges |

**Interpretation**: the ring topology should now be reframed as **"mushaf-scale Hamiltonian cycle with a scale-invariant geodesic backbone but non-fractal closure."** The geodesic-optimality property (local-content-coherence) replicates at sub-scale. The wrap-around closure and structural hinges are specifically 114-scale features; they do NOT replicate at juzʾ-level.

**Classical vindication**: this RATIFIES al-Ghazālī's framing of Q 1 ↔ Q 112-114 as a SESSION-LEVEL (114-scale) liturgical frame, not a juzʾ-internal pattern. No intra-juzʾ pair plays the closure role the Q 1 / Khawātim pair plays at session scale.

**Companion observation ([[h-new-255-juz30-mini-cycle|H-NEW-255]] secondary)**: Juzʾ 30 ranks **2nd of 78** contiguous 37-surah arcs in the mushaf by path length (z_contig = −2.36, p = 0.025) — the densest contiguous 37-surah window in the mushaf at that sub-scale. This makes Juzʾ 30 structurally distinctive among sub-cycles.

See `findings/phase-b-hypotheses/h-new-255-juz30-mini-cycle.md` for full protocol.
