---
finding_id: Q084-F-03
title: Q 84:7-15 book-hand antithesis-diptych — shared-anchor muqābala cohesion vs length-matched null
phase: B+
date_locked: 2026-05-30
seed: 20260509
n_perm: 10000
bonferroni_k: 1
alpha_bon: 0.05
status: LOCKED-BEFORE-COMPUTATION
script: surahs/Q084-al-inshiqaq/scripts/Q084_F_03_book_hand_antithesis.py
parent_findings: H-NEW-2250, H-NEW-1510, Q066-F-01
---

# Q084-F-03 — Pre-Registration: the book-hand antithesis-diptych (Q 84:7-15)

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q084_F_03_book_hand_antithesis.py` and verified at runtime (fail-fast on mismatch).

## Motivation

Q 84's central judgment scene is built as a two-arm antithesis (a *muqābala*) of the two
fates at the Reckoning:

- **Arm A — the right-hand party (vv 7-9):** `fa-ammā man ūtiya kitābahu bi-yamīnih` →
  `fa-sawfa yuḥāsabu ḥisāban yasīrā` → `wa-yanqalibu ilā ahlihi masrūrā`. The book is given
  to the **right hand**; the reckoning is **easy**; the man **returns joyful to his family**.
- **Arm B — the behind-the-back party (vv 10-15):** `wa-ammā man ūtiya kitābahu warāʾa ẓahrih`
  → `fa-sawfa yadʿū thubūrā` → `wa-yaṣlā saʿīrā` → `innahu kāna fī ahlihi masrūrā` →
  `innahu ẓanna an lan yaḥūr` → `balā inna rabbahu kāna bihi baṣīrā`. The book is given
  **behind the back**; he **calls for destruction**; **burns in the blaze**; he **had been
  joyful among his family**; thought he would **never return**; his Lord was **watching**.

Classical balāgha treats this as a deliberate *muqābala* of antithetical fates. al-Rāzī
(*Mafātīḥ al-ghayb*, on Q 84:7-12) and al-Zamakhsharī (*al-Kashshāf*, on Q 84:7) read the two
arms as a matched opposition (`bi-yamīnih` ↔ `warāʾa ẓahrih`; `ḥisāban yasīrā` ↔ `yadʿū thubūrā`;
`masrūrā` returning ↔ `masrūrā` past-and-doomed). The rhetorical signature of *muqābala* is
that the two antithetical members **reuse the same anchor lexemes with reversed valence** —
the opposition is built ON shared vocabulary, not by switching to disjoint vocabulary.

This pre-reg promotes the qualitative *muqābala* reading into a falsifiable corpus test:
**do the two arms of the Q 84 judgment-diptych share anchor-roots at a rate exceeding what
two adjacent same-surah verse-blocks of matched length share by chance?**

## Rules-tuple

`(no-tashkeel, QAC-v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Roots from QAC v0.4 (`data/morphology/quranic-corpus-morphology-0.4.txt`,
`ROOT:` field on segment records). Verse text reference
`quran-text/quran-no-tashkeel.json`. Arm membership LOCKED below.

## Locked arm definitions

- **Arm A** = verses {7, 8, 9} (the right-hand fate).
- **Arm B** = verses {10, 11, 12, 13, 14, 15} (the behind-back fate).
- The boundary v9|v10 is the surah's syntactic pivot: v7 `fa-ammā man ūtiya kitābahu bi-yamīnih`
  vs v10 `wa-ammā man ūtiya kitābahu warāʾa ẓahrih` — the two `ammā` protases that open the
  antithesis. Arm A runs to the end of the first apodosis cluster (v9, *masrūrā*); Arm B is the
  second protasis through its full apodosis cluster (vv 10-15).

## Test statistic

S_obs = |roots(Arm A) ∩ roots(Arm B)| — the count of anchor-roots SHARED across the two
antithetical arms (the *muqābala* mirror anchors). Reported alongside the cross-arm
root-Jaccard J(A,B) = |A∩B| / |A∪B| for context.

## Direction (LOCKED before observation)

The *muqābala* hypothesis predicts the two arms are lexically **mirrored** — they reuse shared
anchor-roots with reversed valence. **Direction lock: S_obs > null mean (the two arms share
MORE anchor-roots than length-matched random verse-block pairs).**

Counter-direction (S_obs < null mean — the two arms share FEWER roots than chance, i.e. the
antithesis is built by lexical disjunction rather than shared-anchor reversal) = NULL,
published with full prominence as a pre-commit violation.

## Null distribution

**Null (seed 20260509, 10,000 perms):** the antithesis is a same-surah, adjacent-block
structure, so the null must control for (i) block lengths and (ii) same-surah adjacency.
Draw 10,000 random adjacent verse-block pairs from the flat 6,236-verse corpus: pick a random
contiguous window of `len(Arm A) + len(Arm B) = 9` verses that lies wholly within a single
surah, split it at the same internal offset (first 3 verses = pseudo-Arm-A, next 6 = pseudo-Arm-B),
compute |roots(block1) ∩ roots(block2)|. The p-value is the fraction of null draws with
S_null ≥ S_obs. p_perm = (#{S_null ≥ S_obs} + 1) / (N_perm + 1).

This null holds block-lengths (3 and 6) and within-surah adjacency fixed, so it tests
specifically whether the Q 84 diptych's cross-arm anchor-sharing is elevated above the
baseline cross-block sharing of any two adjacent 3+6 verse blocks in the corpus.

## Success / failure criteria

- S_obs > null mean AND p_perm < α_Bonf=0.05 → **PASS-DIRECTED** (the antithesis-mirror is
  statistically elevated shared-anchor cohesion).
- S_obs > null mean AND p_perm ≥ 0.05 → **DIRECTIONAL** (correct direction, not significant).
- S_obs < null mean → **NULL (pre-commit violation)**, full prominence.

## Bonferroni

Q084-F-03 is a single permutation cell (k=1). α_corrected = 0.05. (The surah-session
cross-test Bonferroni over {F-01, F-02, F-03} is reported in 06-novel-findings.md; F-01 and
F-02 are deterministic corpus-exact counts and do not consume permutation-α.)

## MW protections

- **MW-1 (instrument-prior):** arm definitions, statistic S, root source, null all fixed here.
- **MW-2 (corpus-prior):** 10,000 length-matched within-surah adjacent-block permutations.
- **MW-3 (alternative-models):** report both S (count) and J (Jaccard); report the cross-arm
  mirror-root identities for transparency.
- **MW-5 (replication):** re-run at seed 20260511 reported in the findings file.
- **MW-6 (instrument-control):** the same-surah adjacent-block null IS the non-target control
  (any 3+6 block pair, not the specific antithesis).
- **MW-7 (post-hoc cap):** the antithesis was noticed in close reading; it is promoted to a
  pre-registered, direction-locked test here BEFORE computation, respecting the single-test
  α=0.05 cap.

## Connection to existing findings

- **H-NEW-2250** (idhā-cascade) leaves Q 84 as an explicit open question (its Limit 2): the
  grammatical idhā-detector fragments Q 84's opening. Q084-F-03 addresses Q 84's OTHER major
  structure — the judgment-diptych — at the cohesion-scale that H-NEW-1510 established works
  for thin markers.
- **H-NEW-1510** (pericope-scale root-Jaccard cohesion) is the methodological parent: same
  QAC-root, same length-matched permutation-null machinery.
- **Q066-F-01 Arm B** (al-Taḥrīm dual-exemplar antithesis) is the structural sibling: there the
  antithetical frame bound the two parable-halves MORE than the thematic pair; here we test
  whether Q 84's antithesis is likewise built on a shared-anchor frame.

*Locked 2026-05-30. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
