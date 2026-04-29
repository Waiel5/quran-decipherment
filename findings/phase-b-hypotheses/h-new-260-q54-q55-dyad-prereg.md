---
id: H-NEW-260
title: "Q 54 + Q 55 dyad deep-dive — empirical Mode-B mirror-pair coherence"
phase: B
status: PRE-REG (locked before compute)
date: 2026-04-17
executed_by: h-new-260-specialist
parent: H-NEW-253 (Mode-B siblings; Q 54 emerged as Q 55's closest mirror-pair)
siblings:
  - H-NEW-234 (Q 55 unified 4-principle portrait; Q 54-55-56 neighbor comparison)
  - H-NEW-180 (Q 55 refrain geometry; period-2 pillar)
  - H-NEW-181 (per-surah verse-length ACF)
  - H-NEW-111 (root-Fisher-Rao distance matrix)
  - cross-finding-018 (4-principle reduced model)
seed: 20260419
rules_tuple: (no-tashkeel, hafs-kufan, 2-surah dyad + 113 adjacent-pair baselines, seed 20260419)
bonferroni_k: 3
alpha_bon: 0.01667
direction:
  - Cell A (joint ACF): dyad-fingerprint coherence — concatenated Q 54+Q 55 verse-length ACF at lag-1 OR lag-2 expected to show period-2-structure signature ABOVE the adjacent-pair baseline distribution (|ACF|_joint outlier ≥ p95 of 113 adjacent pairs).
  - Cell B (content-root Jaccard): Q 54 ∩ Q 55 content-root overlap (Jaccard over stemmed roots) ABOVE the median adjacent-pair Jaccard; pre-committed direction = UPPER tail.
  - Cell C (Fisher-Rao mirror asymmetry): d(Q 54, Q 55) and d(Q 55, Q 56) should DIFFER (non-equal) at 2-sided permutation p < 0.01667 under adjacent-pair shuffle — qualitative mirror-vs-closure distinction.
verdict: PENDING
classical_anchors:
  - al-Biqāʿī Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar (Q 54→55 munāsabah: moon-splitting apocalypse Q 54:1 resolved in mercy-repetition fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān)
  - al-Rāzī Mafātīḥ al-ghayb vol 29 on the Q 54-55 transition (eschatological signal → mercy-address)
  - al-Suyūṭī al-Itqān fann 62 munāsabāt (Q 54-55-56 as eschatology-mercy-judgment triple)
---

# [[h-new-260-q54-q55-dyad|H-NEW-260]] — Q 54 + Q 55 dyad deep-dive pre-registration

## Motivation

[[h-new-253-mode-b-siblings|H-NEW-253]] established the following surprising post-hoc observation:
Q 55 al-Raḥmān is **uniquely saturating** on the Mode-B fingerprint
(7/7 self-match; Q 2 = 4/7 next; all others ≤ 3/7). Among all 114
surahs, Q 54 al-Qamar uniquely emerged as Q 55's **structural mirror-
pair within the restricted M1+M3+M5-no-M2 cell-criterion** (cf.
[[h-new-253-mode-b-siblings|H-NEW-253]] finding §"Restricted Q 55-type score"):

- **Q 54**: M1 hinge-window + M3 refrain (*fa-hal min muddakir*)
  with ACF-lag-1 = −0.10 (ANTI-periodic), M5 via heap_β extremum.
- **Q 55**: M1 hinge-window + M3 refrain (*fa-bi-ayyi ālāʾi…*) with
  ACF-lag-2 = +0.31 (period-2 PILLAR), M5 via 5 refrain-compression
  metrics.

Both in the Q 49-57 hinge-window. Both refrain-driven. **Opposite
prosodic directions** (anti-periodic vs period-2 pillar). al-Biqāʿī
reads the Q 54-55 transition as a munāsabah: apocalyptic lunar
signal (Q 54:1) answered by the mercy-response refrain of Q 55.

**Question**: Is the Q 54+Q 55 dyad a genuine architectural dyad
(joint fingerprint coherence, content overlap, distinct-from-Q-55-56
mirror) — or is it a length-and-adjacency artifact that Q 55's unique
identity carries alone? This is a deep-dive, identified
post-hoc by [[h-new-253-mode-b-siblings|H-NEW-253]], and is pre-committed here BEFORE the
compute phase.

## Design

### Cell A — Joint verse-length ACF coherence

Concatenate Q 54's 55 verses and Q 55's 78 verses into a single
133-verse sequence in mushaf order. Compute:
- Joint sequence ACF at lag-1, lag-2, lag-3 (verse-length letters, no-tashkeel).
- Record max|ACF|_joint across lags 1..3.

**Baseline**: for each adjacent pair (Q k, Q k+1) for k=1..113, perform the
identical concatenation + ACF computation with both surahs having ≥5 verses.
Empirical rank of Q 54+Q 55 max|ACF|_joint within 113 baselines is our test.

**Pre-committed direction**: Q 54+Q 55 dyad max|ACF|_joint ≥ **p95**
of adjacent-pair baseline distribution → PASS.

### Cell B — Content-root Jaccard coherence

Using the QAC STEM-root field (same as [[h-new-111-fisher-rao-mushaf|H-NEW-111]]), compute the set of
distinct roots in Q 54 (R_54) and Q 55 (R_55).

- Observed metric: Jaccard(R_54, R_55) = |R_54 ∩ R_55| / |R_54 ∪ R_55|.
- Also report normalised overlap = |R_54 ∩ R_55| / min(|R_54|, |R_55|).

**Baseline**: Jaccard(R_k, R_{k+1}) for k=1..113.

**Pre-committed direction**: Q 54-55 Jaccard ≥ **p95** of the
adjacent-pair baseline distribution → PASS.

### Cell C — Fisher-Rao mirror-vs-closure distinction

Using the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] root-FR distance matrix D (K=500, Dirichlet α=0.5):
- d_A = d(Q 54, Q 55)
- d_B = d(Q 55, Q 56)

**Pre-committed direction**: |d_A − d_B| is "qualitatively distinct"
if it exceeds the 113-pair adjacent-baseline median-absolute-pairwise-
|ΔD| — i.e., if the Q 54-55-56 triple has a non-symmetric Fisher-Rao
footprint around Q 55 at p < 0.01667 under a 10000-permutation
bootstrap of adjacent-triple-ΔD values.

Formally: null distribution is Δ_k = |d(Q_k, Q_{k+1}) − d(Q_{k+1}, Q_{k+2})|
for k=1..112. Observed Δ_55 = |d_54-55 − d_55-56|. p-value = rank of Δ_55
in the 112-baseline distribution (upper tail).

**Interpretation**: if d_A > d_B, Q 54 is semantically FARTHER from
Q 55 than Q 56 is — consistent with Q 54 being an apocalyptic signal
that is closed by Q 55's mercy-address (Q 54 → Q 55 is a larger semantic
MOVE than Q 55 → Q 56). If d_A < d_B, Q 54 is CLOSER (triple is front-
loaded). If Δ_55 is within the middle of the distribution, no
distinction.

## Bonferroni

3 pre-committed cells × α_bon = 0.01667 (from 0.05/3).
This is STRICTER than [[h-new-253-mode-b-siblings|H-NEW-253]]'s α_bon = 0.025.

## MW-5 sanity

5 random adjacent pairs (from seed 20260419+2, excluding Q 54-55) must
NOT produce the Q 54-55 dyad signature — i.e., their max|ACF|_joint
and Jaccard should NOT both be at p95 of the baseline distribution.
This is a sanity check that the Cell A + Cell B signature is
Q-54-55-specific, not generic.

## Decision rules

- **3/3 PASS at α_bon = 0.01667**: Q 54-55 is a GENUINE Mode-B
  mirror-pair; first dyad-level architectural signature in the
  project.
- **2/3 PASS**: partial corroboration; report failing axis honestly.
- **0-1/3 PASS**: Q 54-55 dyad is a length-adjacency artifact; Q 55's
  individual uniqueness remains but the dyad claim collapses.

## Honest limits (pre-disclosed)

1. **Single adjacent-dyad examination**: Q 54-55 is tested only.
   Generalisation requires H-NEW-260.1 (candidate dyads: Q 97-98
   Juzʾ 30 boundary, Q 113-114 muʿawwidhatān).
2. **Verse-length letter-count is a simple prosodic proxy**; richer
   meso-scale prosody (IPA, syllable count) is deferred.
3. **Content-root Jaccard is a bag-of-roots metric**; syntactic
   and thematic overlap not captured.
4. **Fisher-Rao on root distribution (K=500, α=0.5)** is the
   [[h-new-111-fisher-rao-mushaf|H-NEW-111]] instrument; char-4-gram and verse-length variants
   deferred to H-NEW-260.2.
5. **Q 55's individual uniqueness ([[h-new-253-mode-b-siblings|H-NEW-253]], 7/7) is established**;
   this test adds a DYAD-LEVEL claim, orthogonal.
6. **Adjacent-pair baseline requires both surahs ≥5 verses**; pairs
   with tiny surahs (e.g., Q 107-108, Q 108-109) may have unstable
   ACF.
7. **MW-5 (5 random pairs) is a diagnostic only** — not a formal
   null distribution.

## Rules tuple

(no-tashkeel, hafs-kufan, 2-surah dyad + 113 adjacent-pair baselines, seed 20260419)

## Files (planned)

- Pre-reg: this file.
- Script: `scripts/h_new_260_q54_q55_dyad.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-260.json`
- CSV: `findings/phase-b-hypotheses/csv/h-new-260-adjacent-pair-baselines.csv`
- Findings: `findings/phase-b-hypotheses/h-new-260-q54-q55-dyad.md`
- Journal: `journal/h-new-260-run-1.md`
- MASTER-LEDGER Wave-5 entry.
