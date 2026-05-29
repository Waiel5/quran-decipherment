---
finding_id: H-NEW-2360
title: "Antithesis = minimal shared frame + disjoint content — corpus-wide law-promotion test"
phase: B
date_locked: 2026-05-29
author: Waiel Al-Shujaa
seed: 20260509
n_perm: 10000
status: PRE-REGISTERED (locked before computation)
---

# H-NEW-2360 — Pre-Registration

## 0. Provenance and motivation (the 3-way convergence being promoted)

THREE independent prior findings each established the SAME structural observation about
Quranic antithesis (*muqābala* / *ṭibāq*):

1. **Q083-F-01** (MASTER-FINDINGS-LEDGER §10.99): the two 11-verse blocks of Q 83
   (vv 7-17 *sijjīn*/*fujjār* ↔ vv 18-28 *ʿilliyyīn*/*abrār*) share only **3 roots**
   (`ktb, rqm, dry` = the bare *kitābun marqūm / mā adrāka* FRAME) versus a random
   block-pair null mean of 12.7 shared roots; the two destiny-vocabularies are **perfectly
   disjoint** (zero leakage). The muqābala is a minimal shared scaffold + disjoint content.

2. **Q066-F-01** (MASTER-FINDINGS-LEDGER §10.98): the antithetical *ḍaraba Allāh mathalan
   li-lladhīna kafarū → …āmanū* seal of Q 66:10-11 is **frame-driven, not theme-driven**
   (the lexical cohesion is carried by the shared frame, not by a believer-women content
   overlap; J(v11,v12) < J(v10,v11)).

3. **H-NEW-2290** (MASTER-FINDINGS-LEDGER §10.94): the corpus-wide verse-pair antithesis
   generator (8-field locked antonym lexicon) found that antithesis is a **contrast device**
   (one verse carries a field's + pole, the adjacent verse its − pole) — i.e. opposed content
   poles, NOT high cross-verse overlap.

**Convergent claim (the candidate law):** Quranic antithesis is structurally
**"disjoint content + shared minimal frame"** — the two opposed blocks share a small,
high-frequency function/anchor scaffold but their content-lexicons are MORE disjoint than
random same-surah block-pairs.

This pre-registration is the **LAW-PROMOTION test**: does the Q066/Q083/2290 pattern hold
**corpus-wide across antithetical block-pairs**, or is it limited to the three hand-found
cases?

## 1. Rules-tuple (locked)

`(no-tashkeel, QAC v0.4 STEM-ROOT tokens, content-root set per block, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`

- Text: `quran-text/quran-no-tashkeel.json` (114 surahs, 6236 verses).
- Roots: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4), ROOT: field on STEM
  segments, Buckwalter transliteration.
- A block's root set = union of all STEM-segment ROOT codes over its constituent verses.

## 2. The opposed-field lexicon (LOCKED — reused verbatim from the SHA-locked H-NEW-2290 lexicon)

The 8 opposed semantic fields, each (POSITIVE pole spec, NEGATIVE pole spec). Buckwalter QAC
root codes; lemma-restricted entries tag a pole only on the listed lemma. Locked typo no-ops
(`Srk`, `>jr`) are retained verbatim from the H-NEW-2290 lock so the lexicon is byte-identical
to the already-published instrument.

- **F1_faith**: + {`Amn`} / − {`kfr`, `nfq`, `Srk`}
- **F2_guidance**: + {`hdy`} / − {`Dll`}
- **F3_paradise_hellfire**: + lemma{`jnn`→`jan~ap`} / − {`jHm`,`sEr`,`sqr`,`lZy`} ∪ lemma{`Hmm`→`Hamiym`, `nwr`→`naAr`, `Hwy`→`haAwiyap`}
- **F4_light_dark**: + lemma{`nwr`→`nuwr`,`m~uniyr`} / − lemma{`Zlm`→`Zuluma`t`}
- **F5_reward_punish**: + {`vwb`,`>jr`} ∪ lemma{`jzy`→`jazaY`,`jazaA^'`} / − lemma{`Eqb`→`Ea`qibap`,`EiqaAb`,`EuqobaY`}
- **F6_righteous_corrupt**: + {`SlH`,`brr`} / − {`fsd`} ∪ lemma{`swA`→`suw^'`,`say~i}ap`,`say~i_#aAt`}
- **F7_good_foul**: + {`Tyb`} / − {`xbv`}
- **F8_life_death**: + {`Hyy`} / − {`mwt`}

These 8 fields collectively cover the requested oppositions: believers↔disbelievers (F1),
guidance↔misguidance (F2), paradise↔hellfire (F3), light↔darkness (F4), reward↔punishment (F5),
righteous↔corrupt / abrār↔fujjār (F6), good↔foul (F7), life↔death (F8).

**Pole-marker roots (the field-defining roots) are EXCLUDED from content-Jaccard** so that the
test measures background-content disjointness, not the trivial fact that the two blocks differ
in their pole-markers.

## 3. The frame (LOCKED): high-frequency anchor/function roots

The "frame" = the top-K most frequent QAC STEM-roots corpus-wide, **K = 40** (locked).
These are the function/anchor scaffold (`Alh, qwl, kwn, rbb, Amn, Elm, qwm, Aty, kfr, byn,
$yA, rsl, ArD, ywm, Ayy, smw, kll, E*b, Eml, jEl, rHm, rAy, ktb, hdy, Zlm, nfs, qbl, nzl,
*kr, Hqq, k*b, jyA, Ebd, Ax*, xlq, wqy, Axr, Amr, nws, bEd`). The exact list is computed at
runtime from the QAC file (top-40 by token frequency) and frozen in the JSON output; the
computed list is direction-irrelevant scaffolding (it does not depend on the antithesis labels).

- **Frame roots** = top-40 corpus roots.
- **Content roots** of a block = block root set MINUS frame roots MINUS pole-marker roots of
  ANY field.

## 4. The generator (LOCKED)

Block width **W = 5 verses** (locked; an odd width matching the H-NEW-2220 pericope scale).
For each surah with ≥ 2·W verses:

1. Slide non-overlapping consecutive W-verse blocks (block 0 = vv 1..W, block 1 = vv W+1..2W, …;
   a trailing remainder of < W verses is dropped).
2. Compute each block's **field-pole profile**: for each field F, does the block carry the +
   pole (any + marker present) and/or the − pole?
3. A **same-surah block-pair (Bi, Bj), i<j** is an **ANTITHETICAL PAIR** iff there exists a
   field F such that one block carries F's + pole and the OTHER block carries F's − pole
   (cross-block contrast), AND neither block carries BOTH poles of that same field internally
   in a way that cancels the contrast (i.e. the cross-block + / − assignment is unambiguous:
   we require (`+`∈Bi and `−`∈Bj and not(`+`∈Bj and `−`∈Bi)) OR the symmetric case; a pair
   with mutual + and − on the same field in both blocks is NOT counted, to keep the contrast
   well-defined).
4. The set of all such antithetical pairs across all surahs = the GENERATOR OUTPUT.

This is the same antithetical-contrast definition as H-NEW-2290 (one pole vs opposite pole)
lifted from the verse-pair scale to the W=5 block scale.

## 5. Structural-signature observables (per antithetical pair)

For each antithetical pair (Bi, Bj):

- **content-Jaccard** `Jc = |Ci ∩ Cj| / |Ci ∪ Cj|` where Ci, Cj are the CONTENT-root sets
  (§3 definition: frame- and pole-marker-roots removed). If union is empty, the pair is
  excluded from the Jaccard arm (no content to compare).
- **frame-overlap count** `Fo = |Fi ∩ Fj|` where Fi, Fj are the FRAME-root sets of the two
  blocks (frame roots present in each block).

## 6. The two pre-registered sub-tests (Bonferroni family k = 2, α_bon = 0.025)

### Sub-test A — CONTENT IS DISJOINT (direction LOCKED: antithetical < random; z < 0)

- **Statistic**: mean content-Jaccard over all antithetical pairs, `Jbar_anti`.
- **Null**: the baseline distribution of mean content-Jaccard for **random same-surah
  W-block-pairs**. Concretely: build the full population of same-surah non-overlapping
  W-block-pairs (the same population the antithetical pairs are drawn FROM). For each of
  10000 permutations, draw a random subset of the SAME SIZE as the antithetical-pair set,
  uniformly without replacement from this same-surah-block-pair population, and compute its
  mean content-Jaccard. This is a label-free, surah-structure-preserving null: it asks "is the
  content-Jaccard of antithetical pairs lower than a random equal-size sample of same-surah
  block-pairs?"
- **LOCKED PREDICTION**: `Jbar_anti` is BELOW the null mean — `z = (Jbar_anti − null_mean)/null_sd < 0`,
  one-sided lower-tail `p = P(null ≤ Jbar_anti) < 0.025`.
- **Reversal** (`Jbar_anti ≥ null_mean`, especially upper-tail significant) = PRE-COMMIT
  VIOLATION, published as NULL with full prominence.

### Sub-test B — A SHARED MINIMAL FRAME EXISTS (direction LOCKED: frame-overlap non-zero / above pure-disjointness)

- **Statistic**: mean frame-overlap `Fbar_anti` over all antithetical pairs.
- **Null**: the SAME random same-surah W-block-pair null (mean frame-overlap of a random
  equal-size sample). Additionally, a **pure-disjointness floor**: the fraction of antithetical
  pairs with `Fo = 0` (zero shared frame). The convergence claim is that antithetical blocks
  retain a shared frame, i.e. `Fbar_anti > 0` and the zero-frame fraction is small.
- **LOCKED PREDICTION**: `Fbar_anti > 0` (non-zero shared frame in the mean), AND `Fbar_anti`
  is NOT BELOW the random null by a significant margin — i.e. one-sided lower-tail
  `p_lower = P(null ≤ Fbar_anti)` is NOT < 0.025 (the frame is preserved, not stripped). The
  positive-direction pass condition: `Fbar_anti > 0` AND zero-frame-fraction < 0.5 AND frame is
  not significantly depleted vs random (`p_lower ≥ 0.025`).
- This sub-test is what distinguishes "disjoint content + SHARED frame" (the law) from "fully
  disjoint blocks" (no frame). A finding of `Fbar_anti ≈ 0` would REFUTE the "minimal shared
  frame" half of the convergence.

### Joint verdict logic

- **LAW-STRENGTH (corpus-wide)**: Sub-test A PASS (content significantly disjoint, z<0,
  p<α_bon) AND Sub-test B PASS (shared frame preserved, non-zero, not depleted). The
  three-case convergence generalizes to a corpus-wide law.
- **PARTIAL**: exactly one sub-test passes.
- **NULL / REVERSED**: Sub-test A fails or reverses (the headline claim — disjoint content —
  does not generalize). Published with full prominence; the 3-way convergence is then
  demoted to three isolated cases, NOT a law.

## 7. Robustness (MW-3 alternative-models; reported, not gated)

- **R1 — block width W = 7** (re-run the whole generator + both sub-tests at W=7).
- **R2 — content-Jaccard WITHOUT frame removal** (raw content disjointness including frame, to
  show the effect is not an artefact of frame removal).
- **R3 — frame size K = 25 and K = 60** (re-derive frame, re-run sub-test B; the shared-frame
  result should be stable to the frame cutoff).
- **R4 — replication seed 20260601** (sub-test A null re-drawn; z-sign must persist).

## 8. MW protections

- **MW-1 (instrument-prior)**: content-Jaccard, frame-overlap, the 8-field lexicon, frame=top-K,
  W, the null, and both directions are all fixed in THIS file before any computation.
- **MW-2 (corpus-prior)**: 10000-perm permutation null.
- **MW-3 (alternative-models)**: §7 R1-R4.
- **MW-5 (replication)**: §7 R4 (second seed).
- **MW-6 (instrument-control)**: the null is a same-surah random block-pair sample — the natural
  control for "is antithesis special among same-surah block-pairs?"
- **MW-7 (post-hoc cap)**: no post-hoc claims promoted without the locked sub-tests passing.

## 9. Failure conditions (explicit)

- If `Jbar_anti ≥ null_mean` (content NOT disjoint, or even MORE overlapping): Sub-test A NULL /
  REVERSED → the 3-case convergence does NOT generalize; published as NULL, the candidate law is
  REJECTED at corpus scale.
- If `Fbar_anti ≈ 0` / zero-frame-fraction ≥ 0.5 / frame significantly depleted: Sub-test B fails
  → "shared minimal frame" half does not hold; the law would be "disjoint content" only.
- If the generator finds < 30 antithetical pairs corpus-wide: flagged LOW-POWER; verdict caps at
  DIRECTIONAL regardless of p.

## 10. Seed / perms / correction (locked)

- Seed = **20260509** (primary), replication seed **20260601**.
- n_perm = **10000**.
- Bonferroni family **k = 2**, **α_bon = 0.025**.

Pre-registration locked 2026-05-29. SHA-256 of this file is embedded in
`scripts/h-new-2360.py` and verified at runtime (fail-fast on mismatch).
