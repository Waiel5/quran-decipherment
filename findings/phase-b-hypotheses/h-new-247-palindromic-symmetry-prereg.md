---
finding_id: h-new-247
title: "Palindromic surah-pair symmetry test (k paired with 115-k)"
specialist: h-new-247-specialist
date_prereg: 2026-04-17
seed: 20260419
parent_finding: cross-finding-013 (mushaf topological ring, CONFIRMED)
sibling_context:
  - h-new-204 (reverse-mushaf boundary-mirror Spearman secondary NULL)
  - h-new-158 (mirror-pair uniqueness; Tier-1 ±58 at Q49→50 / Q56→57)
bonferroni_family: h-new-247-palindromic-symmetry
bonferroni_k: 4
alpha: 0.05
alpha_bon: 0.0125
n_perms: 1000
rules_tuple: "(no-tashkeel, 114 surahs, 57 palindromic pairs {(k, 115-k)}, QAC-STEM roots K=500 via H-NEW-111 D-matrix, Hafs-Kūfan)"
direction_primary: "POSITIVE — across all 4 cells, palindromic-pair summary statistic is MORE structurally-coherent than mean of 1000 random pair assignments."
---

# [[h-new-247-palindromic-symmetry|H-NEW-247]] — Palindromic surah-pair symmetry (k ↔ 115-k) pre-registration

## Motivation

[[cross-finding-013-mushaf-topological-ring|Cross-finding-013]] (2026-04-17) established that the 114-surah mushaf is a
**topological ring** — a structured Hamiltonian cycle in Fisher-Rao
content space with wrap-around closure Q 1 ↔ Q 108-114. H-NEW-204
tested whether the *boundary-magnitude* profile mirrors around the
mushaf midpoint (Spearman d(i,i+1) vs d(115-i, 114-i)) and returned
**NULL** (ρ = -0.051, p = 0.72).

The ring topology however admits a **second-order symmetry hypothesis**:
even if adjacent-pair *magnitudes* are not mirror-correlated, individual
**surahs at positions k and 115-k** might be structurally PAIRED — the
ring-hinge at the mushaf center Q 57 / Q 58 (al-Ḥadīd / al-Mujādila)
sits on the Medinan-frontier and Q 57 opens with the musabbiḥāt
incipit *sabbaḥa li-llāhi mā fī al-samāwāt*. If the mushaf is folded at
this hinge, the Q 1 ↔ Q 114 wrap-around closure generalizes to a full
**palindromic pairing** {(1,114), (2,113), ..., (57,58)}.

This pre-reg tests whether the 57 palindromic pairs show greater
structural similarity than random pairings across 4 independent
feature spaces. A positive result would extend [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s
ring from a 2-point wrap-around to a **full folded structure**. A null
result is consistent with H-NEW-204 (boundary-mirror NULL) and
localizes ring-topology strictly at the terminus-to-origin edge, not
as a global reflective architecture.

## Hypotheses

Four cells are tested at Bonferroni α_bon = 0.05 / 4 = 0.0125.

**Cell (a) — Fisher-Rao proximity.**
H1(a): mean FR distance over the 57 palindromic pairs is LESS than
mean FR distance over 1000 random-pairing draws.
Statistic: S_a = mean over {d_FR(k, 115-k) : k=1..57}. One-sided
lower-tail permutation test.

**Cell (b) — Shared content roots.**
H1(b): mean shared-root count (intersection of top-K_surah roots per
surah) is GREATER for palindromic pairs than random. Statistic: S_b =
mean over pairs of |top-50-roots(S_i) ∩ top-50-roots(S_j)|. One-sided
upper-tail.

**Cell (c) — Muqaṭṭaʿāt concordance.**
H1(c): palindromic pairs are MORE often concordant in muq-presence
(both muq or both non-muq) than random. Statistic: S_c = #
concordant pairs out of 57. One-sided upper-tail.

**Cell (d) — Length-reflection correlation.**
H1(d): surah-length (n_verses) of surah k is CORRELATED with a
reflected-length statistic for surah 115-k. We test whether the
57-pair Spearman correlation between [log n_verses(k)] and
[log n_verses(115-k)] is GREATER than random-pair Spearman. One-sided
upper-tail. (Note: the Quran has a classical length-descending
ordering; a palindromic mirror would require a length *inversion* — so
this specifically tests "longer-pairs-with-shorter" as a directional
pairing signal. We report BOTH raw Spearman and a mean-reflected
Spearman as complementary descriptives, but the pre-registered
inferential statistic is raw Spearman.)

## Pre-committed method

### Data sources (FROZEN)

- FR D-matrix: `findings/phase-b-hypotheses/csv/h-new-111.json`
  `D_matrix_upper_triangular` (K=500 QAC-STEM roots, Dirichlet 0.5,
  L1-normalized, pre-reg sha256 in parent JSON).
- Root counts: re-parse QAC
  `data/morphology/quranic-corpus-morphology-0.4.txt` for per-surah
  top-50-roots lists (STEM tokens only).
- Muqaṭṭaʿāt set: the canonical 29 — {2, 3, 7, 10, 11, 12, 13, 14, 15,
  19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45,
  46, 50, 68}.
- Surah lengths: `quran-text/quran-no-tashkeel.json` (n_verses per
  surah).

### Palindromic pair set (FROZEN)

57 pairs: {(k, 115-k) : k = 1..57} =
(1,114), (2,113), (3,112), ..., (56,59), (57,58).

### Null model (FROZEN, seed 20260419)

For each null draw:
1. Shuffle surahs 1..114 uniformly.
2. Partition into 57 consecutive pairs: (σ(1), σ(2)), (σ(3), σ(4)),
   ..., (σ(113), σ(114)).
3. Compute the cell statistic on this random partitioning.

Repeat N_PERMS = 1000 times (standard for pair-partitioning nulls;
sufficient for α = 0.0125 resolution given p_min = 1/1001 = 0.000999).

### Decision rule (pre-committed)

For each cell: p_perm < α_bon = 0.0125 → PASS.

**Verdict mapping**:
- 0/4 PASS → NULL (palindromic pairing is not structural; consistent
  with H-NEW-204)
- 1/4 PASS → DIMENSION-SPECIFIC partial pass (name the axis)
- 2-3/4 PASS → PASS-DIRECTED (palindromic layer present on
  multiple axes; specify which axes)
- 4/4 PASS → STRONG PASS (full palindromic symmetry confirmed as a new
  structural layer atop the ring topology)

### MW-5 positive/cheat control

Include the mushaf-canonical pairing as one of the 1000 null draws
(explicitly) — confirm its rank matches the analytic observed
statistic. A random draw should yield z near 0 averaged over draws.

### MW-1 length control

Cell (a) Fisher-Rao inherits parent [[h-new-111-fisher-rao-mushaf|H-NEW-111]] MW-1 (L1-normalized
distributions). Cell (b) uses SETS (intersection count) which is
length-insensitive at top-50 resolution. Cell (c) is a binary
concordance (no length dependency). Cell (d) is specifically the
length axis and uses log-transform to dampen the dominant
mushaf-length-descending confound. No further length control required.

### Bonferroni discipline

k = 4 cells, α_bon = 0.0125 per cell. No sub-tests; no additional
secondaries beyond the 4 primary cells. Cross-cell combination
(Stouffer / meta) is NOT pre-registered and will not be reported as
inferential.

## Honest limits (stated before run)

- N = 57 pairs is SMALL — effect-size sensitivity is low. A null result
  does not rule out weak palindromic effects; it only says they are
  not detectable at this N and permutation resolution.
- Directional-reflection is ONE symmetry among many possible (e.g.,
  block-wise palindrome with variable block sizes, halved
  7-surah-tail mirror-to-fātiḥa, etc.). We do not adjudicate
  alternatives in this finding.
- The 4 cells share partially-correlated substrates (FR derives from
  root distributions; shared-root counts also reflect roots). Effective
  independent evidence ≤ 4; no inflated-independence claim made.
- [[cross-finding-013-mushaf-topological-ring|Cross-finding-013]] Layer 2 wrap-around closure already covers (1,114)
  specifically; [[h-new-247-palindromic-symmetry|H-NEW-247]] tests whether this generalizes beyond the
  single terminal pair. One-pair-driving-the-signal checks are
  included as leave-Q1-out sensitivity descriptives (not inferential).

## Deliverables

1. This pre-reg (current file).
2. Script: `scripts/h_new_247_palindromic.py`.
3. Results JSON: `findings/phase-b-hypotheses/csv/h-new-247.json`.
4. Findings markdown:
   `findings/phase-b-hypotheses/h-new-247-palindromic-symmetry.md`.
5. Journal: `journal/h-new-247-run-1.md`.
6. MASTER-LEDGER entry under Wave-5.

## Sign-off

Seed 20260419 locked. Bonferroni k = 4, α_bon = 0.0125. Directional
expectation: POSITIVE palindromic effect on ALL 4 cells. 1000
permutations. D-matrix sha256 inherited from parent [[h-new-111-fisher-rao-mushaf|H-NEW-111]].
