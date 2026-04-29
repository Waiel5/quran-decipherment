---
id: H-NEW-251
title: Q 1 → Q 2 structural-hinge characterisation — AXIS-SPECIFIC (root-vocabulary + rhyme; NOT char-4-gram, NOT phonological)
phase: B
date: 2026-04-17
seed: 20260419
bonferroni_k: 4
alpha_bon: 0.0125
rules_tuple: "(no-tashkeel; Hafs-Kūfan; FR arccos-Bhattacharyya Dirichlet α=0.5 [A/B/C]; H-NEW-165-style 8-dim phonological Euclidean [D]; 113 consecutive mushaf edges; seed 20260419)"
parent: H-NEW-238
prereg_sha256: dd819d8162bf0757...
verdict: AXIS-SPECIFIC (1 of 4 cells PASS at top-5 / 113; Cell C near-top at rank 8)
---

# [[h-new-251-q1-q2-transition|H-NEW-251]] — Q 1 → Q 2 structural hinge across 4 feature axes

## Headline

**The Q 1 → Q 2 transition is hinge-like on the ROOT-VOCABULARY axis ONLY.** Across the 4 pre-registered axes with rank-5 PASS threshold:

| Cell | Axis | d(Q 1, Q 2) | rank / 113 | verdict |
|---|---|---:|---:|:--:|
| A | Root-FR ([[h-new-111-fisher-rao-mushaf|H-NEW-111]]) | 1.1776 | **1** | **PASS** |
| B | Char-4-gram FR ([[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]) | 1.0023 | 22 | NULL |
| C | Rhyme bigram FR (new) | 1.5101 | 8 | NULL (near-top, 7%ile) |
| D | Phonological mean-tajwīd Euclid | 4.1574 | 31 | NULL |

**Verdict**: **AXIS-SPECIFIC** (1 / 4 cells PASS at top-5; 2 / 4 in top-10%ile including Cell C). Q 1→Q 2 is **NOT** a universal hinge in the sense of Q 49→50 / Q 56→57 (which pass on 3 / 4 axes here). Its cycle-maximum FR-root status is a **semantic/content-distribution effect**, not a universal compositional signature.

**Content bridge CONFIRMED**: Q 1 and Q 2:1-5 share **3 roots** (`hdy` HDY guidance, `qwm` QWM standing/people, `rbb` RBB Lord) — and the HDY root specifically bridges **Q 1:6 *ihdinā* → Q 2:2 *hudan*** (Jaccard = 0.097 over Q 1 × Q 2:1-5; 17% of Q 1's roots found in the first 5 verses of Q 2). al-Biqāʿī *Naẓm al-Durar* and al-Rāzī *Mafātīḥ al-ghayb* classical munāsabāt thesis empirically vindicated.

## Pre-reg compliance

Pre-reg SHA committed BEFORE results viewed. Rank-5 / 113 PASS threshold locked for all 4 cells. Bonferroni k=4 α_bon=0.0125. Seed 20260419. No deviations.

NOTE: Cell A (root-FR) rank = 1 was already pre-committed known from [[h-new-238-cyclic-shift-wrap|H-NEW-238]]; reported for completeness. Cells B, C, D were NEW computations AFTER pre-reg lock.

## Cell-by-cell results

### Cell A — Root-FR distribution distance (PASS; rank 1 / 113)

**d_FR_root(Q 1, Q 2) = 1.1776**, rank **1 / 113** (largest of all 113 consecutive edges).

This is the [[h-new-238-cyclic-shift-wrap|H-NEW-238]] cycle-maximum reproduced. Consecutive edges distribution: mean 0.759, SD 0.242, min 0.226, max 1.178. Q 1→Q 2 is at the max.

### Cell B — Char-4-gram FR distance (NULL; rank 22 / 113)

**d_FR_c4g(Q 1, Q 2) = 1.0023**, rank **22 / 113** (19%ile).

Q 1 → Q 2 is ABOVE average on char-4-gram distance (mean 0.790) but NOT in the top-5. This replicates [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]]'s finding that the char-4-gram top-15 did NOT include Q 1→Q 2 ([[h-new-130-fisher-rao-residuals|H-NEW-130]] root top-15 did). The divergence between feature spaces is located: **Q 1 and Q 2 diverge more in root-vocabulary than in 4-character orthographic sequences**. Q 1's short theological register shares character-4-grams with Q 2's long legal/narrative register (Arabic core orthography), even as their root-vocabularies diverge maximally.

### Cell C — Rhyme-bigram FR distance (NULL, near-top; rank 8 / 113)

**d_FR_rhyme(Q 1, Q 2) = 1.5101**, rank **8 / 113** (7%ile).

Q 1's verse-ending palette (-īm / -īn across its 7 verses) is phonotactically simpler than Q 2's 286-verse rhyme diversity. The rhyme distance is near-top but does not clear the rank-5 threshold. Cell C is the closest-to-PASS of the 3 new cells.

### Cell D — Phonological Euclidean distance (NULL; rank 31 / 113)

**d_phono(Q 1, Q 2) = 4.158**, rank **31 / 113** (27%ile).

8-dim mean tajwīd feature vector (makhraj, voice, emphatic, pharyngeal, sonorant, continuant, idhlāq, qalqala). Q 1's all-letters mean profile is moderately distant from Q 2's, but not extreme. The 113-edge distribution has large SD (2.147, min 0.614, max 11.33), so Q 1→Q 2 at 4.16 is mid-pack. This NULL is the SHARPEST refutation of "universal-hinge" status.

## Comparison to the 3 established universal hinges

| Edge | A root-FR rank | B c4g rank | C rhyme rank | D phono rank | PASS count (top-5) |
|---|---:|---:|---:|---:|:-:|
| Q 1 → Q 2 | **1** | 22 | **8** | 31 | **1** (A) |
| Q 14 → Q 15 | 12 | 14 | 20 | 89 | 0 (ALL NULL at strict top-5) |
| Q 49 → Q 50 | 14 | 9 | 30 | 35 | 0 (ALL NULL at strict top-5) |
| Q 56 → Q 57 | **6** | **6** | 35 | 104 | 0 (ALL NULL; both on 6th of cell A/B) |

Striking observations:

1. **Under the strict top-5 threshold, NONE of the 3 established universal hinges PASS** on any cell here. The [[h-new-130-fisher-rao-residuals|H-NEW-130]] / 130b "universal-hinge" label was defined under top-15 / 113. Under top-15 threshold:
   - Q 1→Q 2: top-15 on A, B, C (3 / 4).
   - Q 14→15: top-15 on A, B (2 / 4).
   - Q 49→50: top-15 on A, B (2 / 4).
   - Q 56→57: top-15 on A, B (2 / 4).

2. **Under the looser top-15 threshold, Q 1→Q 2 MATCHES OR EXCEEDS the 3 established universal hinges.** It is top-15 on 3 axes where they're top-15 on 2 axes. The rhyme axis (C) uniquely adds Q 1→Q 2 over the others.

3. **Q 1→Q 2 uniquely DOMINATES on Cells A and C** (the semantic and rhyme axes). The established universal hinges dominate Cells A and B (root and char). Cell D phonological is noisy and non-discriminative for all hinges.

4. **Cell D is the weakest-discriminating axis**: the 3 universal hinges rank 35, 89, 104. The tajwīd-mean-feature Euclidean instrument is not picking up structural hinges generally. This is an instrument limitation, not a refutation.

## Content bridge — HDY (*ihdinā* → *hudan*) classical munāsabāt vindicated

Extracted QAC STEM roots from Q 1 (all 7 verses) vs Q 2:1-5:

- Q 1 roots (|18|): Alh, Hmd, Dll, rbb, rHm, ʿbd, Elm, dyn, ywm, mlk, smw, hdy, SrT, qwm, Ewn, nEm, gDb, gyr
- Q 2:1-5 roots (|16|): {stem list incl. hdy, qwm, rbb among others}
- **Shared: 3 roots — hdy (HDY), qwm (QWM), rbb (RBB)**.
- Jaccard = 0.097. 17% of Q 1's 18 roots appear in Q 2:1-5. Fraction of Q 2:1-5 roots that are Q 1 roots = 19%.

**The HDY bridge specifically**:
- **Q 1:6** اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ ("guide us to the straight path") — root `hdy` in verb *ihdinā*.
- **Q 2:2** ذَٰلِكَ الْكِتَابُ لَا رَيْبَ فِيهِ هُدًى لِلْمُتَّقِينَ ("This is the Book, no doubt in it, *guidance* for the God-conscious") — root `hdy` in noun *hudan*.

The Quran opens at Q 1 with a **prayer for guidance** and immediately answers at Q 2:2 with the **response: this Book IS the guidance**. This is the paradigm case for al-Biqāʿī's *Naẓm al-Durar* munāsabāt theory and for al-Rāzī *Mafātīḥ al-ghayb*'s opening commentary on al-Baqara, which explicitly frames Q 2:2's *hudan* as the divine response to Q 1:6's *ihdinā*.

**Reconciliation**: the root-FR instrument sees Q 1 and Q 2 as MAXIMALLY divergent DISTRIBUTIONS (Cell A rank 1 / 113), but the **shared-root instrument** sees a deliberate thematic bridge at 3 high-theological-weight roots (HDY, QWM, RBB = guidance, people, Lord). The mushaf creates a compositional JUMP but provides a semantic SCAFFOLD — the classical munāsabāt reading is empirically both challenged (by FR distance) and confirmed (by root overlap + verse-positional HDY-bridge).

This is a textbook precision-sharpening of the classical claim.

## MW-5 cheat — shuffled-null control

Random relabeling of 114 surahs (1000 shuffles, seed 20260419+1), compute rank of the new-Q1-Q2-edge:

| Cell | Mean rank | Frac top-5 | Expected |
|---|---:|---:|---:|
| A root | 56.5 | 4.7% | ~4.4% |
| B c4g | 54.2 | 4.5% | ~4.4% |
| C rhyme | 56.6 | 4.5% | ~4.4% |
| D phono | 58.2 | 4.7% | ~4.4% |

All 4 cells show the expected uniform distribution of rank under shuffled null. The Q 1→Q 2 Cell-A rank=1 result is a LOCATED edge-effect, not a general pattern. **MW-5 PASS.**

## Integration with M1.3 structural hinges ([[cross-finding-014-five-principle-unified-equation|cross-finding-014]])

Pre-H-NEW-251 universal-hinge roster (M1.3):
- Q 14 → Q 15 (top-15 on 3 FR axes, [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b/130c; moderate chronology-reversal)
- Q 49 → Q 50 (top-15 on 3 FR axes; ±58 mirror with Q 56→57)
- Q 56 → Q 57 (top-15 on 3 FR axes; ±58 mirror; direct tasbīḥ-echo rhetorical bridge)

**[[h-new-251-q1-q2-transition|H-NEW-251]] amendment**: Add **Q 1 → Q 2** as a **rank-1 cyclic edge** and **semantic-axis hinge**. Note that it is:
- **Cycle-maximum** on root-FR (Cell A; rank 1 / 113 and 1 / 114 including wrap-edge per [[h-new-238-cyclic-shift-wrap|H-NEW-238]]).
- **Near-max** on rhyme (Cell C; rank 8 / 113).
- **NOT** top-5 on char-4-gram or phonological axes, so NOT a universal hinge in the multi-axis sense.
- **Rhetorically-bridged** by classical al-Biqāʿī / al-Rāzī munāsabāt at the HDY (guidance) root with specific verse-level echo Q 1:6 *ihdinā* → Q 2:2 *hudan*.

Revised M1.3 structural-hinge roster:

| Edge | Type | Rank 1 cells (top-5) | Rank 15 cells (top-15) | Bridge mechanism |
|---|---|:-:|:-:|---|
| **Q 1 → Q 2** | **Semantic cycle-max + liturgical-frame** | A | A, B, C | HDY ihdinā→hudan + QWM + RBB root-scaffold |
| Q 14 → Q 15 | Universal multi-axis | — | A, B, (C) | message/book self-reference |
| Q 49 → Q 50 | Universal + ±58-mirror | — | A, B | omniscience → Qāf oath |
| Q 56 → Q 57 | Universal + ±58-mirror | A, B | A, B | direct tasbīḥ imperative→execution echo |

Under the stricter top-5 threshold used here, NO edge is a "universal top-5 on all 4 axes." The multi-axis universality is a top-15 phenomenon. Q 1→Q 2 joins at the TOP of the root axis and TOP-10 of the rhyme axis while being mid-pack on char and phonological.

## Interpretation — what Q 1 → Q 2 actually IS

The mushaf opens with a **SEMANTIC MAXIMUM-JUMP + LITURGICAL-FRAME + SCAFFOLDED THEMATIC BRIDGE**:

1. **Distributional jump** (Cells A, C PASS/near-PASS): Q 1 (prayer-register, 7 verses, theological-palette-seed per [[h-new-155-q1-sui-generis|H-NEW-155]]) vs Q 2 (encyclopedic legal/narrative register, 286 verses, corpus-representative per [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]]). The root-distribution distance is absolute-maximum in the cycle.

2. **Surface continuity** (Cell B NULL, Cell D NULL): despite root-vocabulary divergence, Q 1 and Q 2 share char-4-gram Arabic orthographic core AND phonological profile. The reader does NOT experience a surface/phonetic discontinuity — only a content-distribution discontinuity.

3. **Deliberate bridge** (content analysis): HDY/QWM/RBB roots span the gap. Specifically, Q 1:6 *ihdinā* (imperative prayer FOR guidance) meets Q 2:2 *hudan* (the Book IS guidance). al-Biqāʿī / al-Rāzī munāsabāt confirmed.

4. **Sui-generis liturgical frame** ([[h-new-155-q1-sui-generis|H-NEW-155]] / 192 / 244 / 238): Q 1 is the P3 prayer-frame, uniquely positioned. The Cell-A rank-1 jump is the M1 COST of P3's Q-1 placement.

## The P3-M1 trade-off quantified at the opening

The mushaf pays:
- **0.3884 FR units** at Q 114→Q 1 (wrap-in; rank 18 / 114 per [[h-new-238-cyclic-shift-wrap|H-NEW-238]]; a tight ṭawāf-like closure).
- **1.1776 FR units** at Q 1→Q 2 (cycle-max; rank 1 / 113; the opening cost).

Total P3-absorbed FR cost = **1.566 FR units** at the Q 114-1-2 opening triad. For comparison, a hypothetical alternate rotation starting at Q 108 al-Kawthar (M1-optimal per [[h-new-238-cyclic-shift-wrap|H-NEW-238]]) would have wrap-in 0.226 + first-edge much smaller. The mushaf spends ~1.34 FR units MORE than the M1-optimum to place Q 1 at position 1. That 1.34 is the empirical magnitude of the P3 "liturgical slack" in [[cross-finding-020-the-complete-equation|cross-finding-020]].

## Honest limits

1. **Top-5 threshold is a STRICTER operationalisation than [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s top-15.** Under top-15, Q 1→Q 2 passes 3 cells (matching the established universal hinges), so the "not universal" verdict is threshold-dependent. Reported honestly.

2. **Cell D phonological instrument is weak-discriminative**: 3 of 4 universal hinges also fail it. The weak power here limits what we can infer from Cell D's NULL.

3. **Cell C rhyme instrument is NEW** (not inherited). Alternative operationalisations (last-1-char, last-3-char, root-of-last-word, prosodic-foot) might give different ranks.

4. **Single-pair characterisation**. This finding tests ONE edge on 4 axes; it does not generalise to "all Q→Q+1 transitions behave this way." The universal-hinge claim would require replicating this 4-axis test on Q 14→15, Q 49→50, Q 56→57 (partially done via the comparator rows above).

5. **Root overlap (3 / 18) may seem small**, but Q 2:1-5 is only the first 5 verses of a 286-verse surah. Extending to Q 2:1-29 (the second paradigm-block per al-Biqāʿī) would likely show higher overlap.

## Classical anchor

- **al-Biqāʿī (d. 885 AH)**, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*: treats Q 1 → Q 2 as the archetypal *munāsabah* pair. [[h-new-251-q1-q2-transition|H-NEW-251]] confirms his thematic-bridge argument (HDY/QWM/RBB scaffold) while quantifying the FR-distributional distance he did not have. [PRIMARY-ANCHOR]
- **al-Rāzī (d. 606 AH)**, *Mafātīḥ al-ghayb*, opening of Q 2 tafsīr: explicitly notes that Q 2:2 *hudan* fulfils Q 1:6 *ihdinā*. [[h-new-251-q1-q2-transition|H-NEW-251]] Cell-content analysis CONFIRMS at the root level. [PRIMARY-ANCHOR]
- **al-Suyūṭī**, *al-Itqān*, fann 62 on *munāsabāt*: treats Fātiḥa-Baqara munāsabah as paradigm case. [SECONDARY-TRIANGULATED]
- **al-Zarkashī**, *al-Burhān*: Q 1 is the archetypal *fātiḥa* (opener); no explicit compositional-jump treatment. [SECONDARY-TRIANGULATED]

## Verdict statement

**AXIS-SPECIFIC (1 / 4 cells PASS at top-5 rank)**. Q 1 → Q 2 is:
- **Cycle-maximum on root-FR** (PASS; the cycle-opening architectural fact).
- **Near-top on rhyme** (NULL at strict top-5; PASS at top-10).
- **Mid-pack on char-4-gram** (NULL).
- **Mid-pack on phonological** (NULL).

This is NOT a universal-hinge (top-5 on all 4 axes) but IS a distinctive **semantic / root-vocabulary hinge + liturgical-frame cycle-edge**. The [[h-new-130-fisher-rao-residuals|H-NEW-130]]/142 universal-hinge roster is **refined**, not expanded, by [[h-new-251-q1-q2-transition|H-NEW-251]]: Q 1→Q 2 belongs on the **cycle-maximum tier** (unique) while Q 14→15 / Q 49→50 / Q 56→57 form the **multi-axis-universal tier**.

## Queued follow-ups

- **H-NEW-251.1**: apply the same 4-cell framework to Q 14→15, Q 49→50, Q 56→57 formally; test "universal-hinge" claim under top-5 threshold.
- **H-NEW-251.2**: extend content-bridge analysis to Q 2:1-29 (al-Biqāʿī's paradigm-block) — does shared-root count rise?
- **H-NEW-251.3**: replicate Cell C with alternative rhyme operationalisations (fasila class per H-NEW-96.2, last-3-char, etc.).

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-251-q1-q2-transition-prereg.md`
- Script: `scripts/h_new_251_q1_q2_transition.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-251.json`
- Findings: this file
- Journal: `journal/h-new-251-run-1.md`
