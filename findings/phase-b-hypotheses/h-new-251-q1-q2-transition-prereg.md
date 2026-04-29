---
id: H-NEW-251
title: Q 1 → Q 2 structural-hinge characterisation across 4 feature spaces (Wave-5)
phase: B
parent: H-NEW-238 (cyclic-shift wrap-edge; identified Q 1→Q 2 as rank 114 / 114 cycle-max edge)
related: H-NEW-130 / 130b / 130c / 142 (universal-hinge roster Q 14→15, Q 49→50, Q 56→57)
related_q1: H-NEW-155 (sui-generis-liturgical); H-NEW-192 (position Δ=−104); H-NEW-244 (umm al-kitāb root-PASS / dist-NULL)
date: 2026-04-17
seed: 20260419
bonferroni_k: 4
alpha_bon: 0.0125
rules_tuple: "(no-tashkeel; Hafs-Kūfan; FR arccos-Bhattacharyya Dirichlet α=0.5 over QAC-STEM top-500 roots [Cell A] and char-4-grams [Cell B]; last-word orthographic bigrams over 114 surahs [Cell C]; H-NEW-165-style 9-dim per-surah mean phonological/tajwīd feature vector [Cell D]; seed 20260419)"
specialist: wave-5-q1q2-hinge
status: PRE-REG LOCKED
---

# [[h-new-251-q1-q2-transition|H-NEW-251]] — Pre-registration

## Parent rationale

[[h-new-238-cyclic-shift-wrap|H-NEW-238]] (cyclic-shift wrap-edge) revealed that the canonical **Q 1 → Q 2** transition is the **absolute worst (rank 114/114) edge in the 114-surah Fisher-Rao root-distribution cycle**, with d_FR(Q 1, Q 2) = 1.1776 vs mean 0.7557 (3.1× canonical wrap-in, 5.2× cycle-minimum). [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s top-15 structural-hinge list already ranks Q 1→Q 2 at #1 in root-space but it was NOT in the char-4-gram top-15 ([[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]]). [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]] Cells A+C + [[h-new-192-mushaf-position-decomposition|H-NEW-192]] Δ=−104 + [[h-new-155-q1-sui-generis|H-NEW-155]] converge: Q 1 is distributionally isolated (89th %ile per-verse KL) while Q 2 al-Baqarah is the MOST corpus-representative surah (per-verse KL = 0.00129, rank 1/114). The Q 1→Q 2 junction is a **maximum compositional jump**.

This pre-reg characterises Q 1→Q 2 across **4 independent feature axes** and compares its rank-profile to the 3 established universal hinges (Q 14→15, Q 49→50, Q 56→57).

## Hypothesis (directed)

**H1 (universal-hinge hypothesis)**: The Q 1→Q 2 transition ranks in the **top-5** of the 113 consecutive-mushaf transitions on EACH of 4 feature axes (root-FR, char-4-gram-FR, rhyme-endings, phonological tajwīd features). A positive result adds Q 1→Q 2 to the [[h-new-130-fisher-rao-residuals|H-NEW-130]]/142 universal-hinge roster as a **4th universal hinge** and a **rank-1 cyclic edge**.

**Direction locked BEFORE run**: Q 1→Q 2 will rank ≤ 5/113 (equivalent to top-4.4 percentile) on each cell where "high rank" = large distance / divergence.

## Bonferroni family

k = 4 axes, α_bon = 0.0125 (per-cell). Family = `[[h-new-251-q1-q2-transition|h-new-251]]-q1-q2-transition`.

## Cells

### Cell A — Root-FR distribution distance (primary)

- **Instrument**: Fisher-Rao arccos-Bhattacharyya on L1-normalised Dirichlet α=0.5 smoothed top-500 QAC-STEM root count vectors, inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D-matrix.
- **Test**: rank of d_FR(Q 1, Q 2) among the 113 consecutive mushaf distances {d_FR(Q k, Q k+1) : k=1..113}.
- **PASS**: rank ∈ {1..5} (top-5 / 113).
- **Expected ([[h-new-238-cyclic-shift-wrap|H-NEW-238]] already computed)**: rank 1 / 113, d = 1.1776.

### Cell B — Char-4-gram FR distance

- **Instrument**: Fisher-Rao on char-4-gram distribution per [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] D-matrix.
- **Test**: same rank-test as Cell A, on [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]'s 114×114 char-4-gram D-matrix.
- **PASS**: rank ∈ {1..5} (top-5 / 113).
- **Expected (from [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] top-15)**: Q 1→Q 2 NOT in root top-15-intersection, so rank likely > 5 on char-4-gram. Direction locked positive; honest prediction is Cell B will likely NULL.

### Cell C — Rhyme-ending distance

- **Instrument**: per-surah last-word final-two-character (orthographic bigram) count distribution over the last word of each verse, L1-normalised + Dirichlet α=0.5 smoothed, Fisher-Rao arccos-Bhattacharyya distance.
  - The "final bigram" is computed on the no-tashkeel text as the last 2 Arabic characters of the last orthographic word of each verse.
  - For Q 1 (7 verses) and Q 2 (286 verses), each verse-ending contributes one bigram token.
  - Distribution support = set of all bigrams observed anywhere in the 114 surahs' verse-endings (closed vocabulary).
- **Test**: rank of d_FR(Q 1, Q 2) among 113 consecutive mushaf rhyme-distances.
- **PASS**: rank ∈ {1..5}.
- **Expected**: Q 1's rhyme palette (-īm, -īn, -ūn, -īn, -īn, -īm, -īn) is ḥurūf al-madd extended; Q 2 is predominantly -ūn / -īn. Overlap likely non-trivial; Cell C prediction open.

### Cell D — Phonological (tajwīd) per-surah mean feature vector distance

- **Instrument**: For each of 114 surahs, compute the 9-dim mean phonological feature vector over ALL letters in the no-tashkeel surah text, using the [[h-new-165-phonological-predictor|H-NEW-165]] classical tajwīd feature codebook (makhraj-ordinal 1-8, voice {mahmūsa=0, majhūra=1}, emphatic {tafkhīm=1}, pharyngeal {mustaʿliya ∪ pharyngeal=1}, sonorant {1}, continuant {1}, idhlāq {1}, and fractions emphatic/pharyngeal/sonorant).
- **Distance**: Euclidean distance between 9-dim mean feature vectors (standardised per feature across 114 surahs before Euclidean).
- **Test**: rank of ‖φ(Q 1) − φ(Q 2)‖ among 113 consecutive mushaf phonological distances.
- **PASS**: rank ∈ {1..5}.
- **Expected**: Q 1's 7 theological verses vs Q 2's 286-verse legal/narrative range — phonological profile may diverge (Q 2's emphatic/pharyngeal density from legal Arabic could differ from Q 1's prayer register). Direction locked positive.

## Decision rules (pre-committed)

| Cells PASSING (top-5) | Verdict | Interpretation |
|:-:|:-:|:--|
| 4 of 4 | **Universal-hinge** (Q 1→Q 2 added as 4th universal hinge) | Analogous to Q 14→15 / Q 49→50 / Q 56→57 |
| 3 of 4 | **Strong-hinge** (add as axis-specific hinge) | Universal-hinge-like but not on all axes |
| 2 of 4 | **Moderate-hinge** (axis-specific) | Real but limited; document axes |
| 1 of 4 | **Axis-specific** | Effect is feature-specific |
| 0 of 4 | **NULL** | Q 1→Q 2 is not generally hinge-like; root-FR extreme is feature-artifact |

## Supplementary (descriptive, NOT counted in Bonferroni)

1. **3-hinge comparison**: For each of the 4 cells, report Q 1→Q 2 distance AND Q 14→15, Q 49→50, Q 56→57 distances. Rank all 4 within each cell's distribution.
2. **Content-bridge analysis**: Extract content-root overlap between Q 1 (all 7 verses) and Q 2:1-5. Test whether ihdinā (ه د ي = HDY root) at Q 1:6 echoes hudan (same HDY root) at Q 2:2 — al-Rāzī Mafātīḥ al-ghayb explicit classical claim.
3. **MW-5 cheat**: randomly shuffle the 114 surah labels (seed 20260419+1) and recompute rank of the Q 1-Q 2 original-pair edge in the shuffled-adjacency list — should be uniformly random (expected rank 57, 50%ile). Verifies the effect is a LOCATED edge-effect not a general-pattern.

## MW-5 cheat positive control

Shuffled-null test (above) + confirm [[h-new-238-cyclic-shift-wrap|H-NEW-238]] expected numerical match: d_FR-root(Q 1, Q 2) = 1.1776 (to 4 decimals) reproduced.

## Honest limits pre-declared

- **Single-pair characterisation, not general-pattern**. Q 1→Q 2's rank on 4 axes does not test "all universal hinges are top-5 on 4 axes"; that generalisation would require running this 4-axis test on all known hinges.
- **Cell C rhyme instrument is new**. Not inherited from prior finding; constructed here from first principles. Results conditioned on "last 2 chars of last word" operationalisation.
- **Cell D phonological instrument is adapted from [[h-new-165-phonological-predictor|H-NEW-165]]** (muq-letter-level) to surah-level (all letters in surah). The [[h-new-165-phonological-predictor|H-NEW-165]] feature codebook transfer is pre-committed; no tuning.
- **Post-hoc awareness**: [[h-new-238-cyclic-shift-wrap|H-NEW-238]] already computed Cell A result. Cell A is being REPORTED not DISCOVERED. Cells B, C, D are new and were computed AFTER pre-reg lock.
- **n=1 hinge test**. Q 1→Q 2 is a unique pair; no p-value across pairs is claimed from this finding alone.

## Files (to be produced)

- Pre-reg (this file): `findings/phase-b-hypotheses/h-new-251-q1-q2-transition-prereg.md`
- Script: `scripts/h_new_251_q1_q2_transition.py`
- JSON results: `findings/phase-b-hypotheses/csv/h-new-251.json`
- Findings: `findings/phase-b-hypotheses/h-new-251-q1-q2-transition.md`
- Journal: `journal/h-new-251-run-1.md`
- Hinge-roster update: append to `findings/phase-b-hypotheses/h-new-142-universal-hinges-chrono-rhetorical.md` if verdict = universal-hinge or strong-hinge.
- [[cross-finding-014-five-principle-unified-equation|Cross-finding-014]] update: amend M1.3 structural-hinges section if universal verdict.
- Master ledger: Wave-5 entry.

## Garden-of-forking-paths disclosures

- 4 cells decided at pre-reg time; no mid-run addition of 5th cell.
- Top-5 threshold (rank ≤ 5 / 113) is the universal-hinge-analog operationalisation matching the [[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 practice scaled by 1/3 to be stricter (5/113 ≈ 4.4%ile vs 15/113 ≈ 13%ile). This is a TIGHTENING choice.
- Euclidean distance in Cell D chosen over cosine as pre-committed default (standardised-feature Euclidean gives interpretable "phonological profile deviation"). Cosine not tested.
- Dirichlet α=0.5 chosen to match [[h-new-111-fisher-rao-mushaf|H-NEW-111]]/111b parent family (no α sensitivity sweep).
- Feature-selection for Cell D uses [[h-new-165-phonological-predictor|H-NEW-165]] codebook — no new features engineered.
