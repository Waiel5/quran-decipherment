---
surah: 66
surah_name_ar: التحريم
surah_name_translit: al-Taḥrīm
file_type: prereg
test_id: Q066-F-01
date_locked: 2026-05-29
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-COMPUTATION
---

# Q066-F-01 — Pre-Registration: al-Taḥrīm verbatim verse-twin + antithetical dual-exemplar seal

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q066_F_01_tahrim_seal.py` and verified at runtime (fail-fast on mismatch).

## Motivation

Q 66 al-Taḥrīm has two surface-distinctive structural features that classical scholarship noticed
qualitatively but the project has not yet tested at corpus scale:

1. **A verbatim full-verse twin.** Q 66:9 (`yā ayyuhā al-nabī jāhid al-kuffāra wa-l-munāfiqīna
   wa-ghluẓ ʿalayhim wa-maʾwāhum jahannamu wa-biʾsa al-maṣīr`) is, on inspection, identical to
   Q 9:73. H-NEW-1520 already flagged the Q 9:73-75 × Q 66:9-11 pericope pair as the second-strongest
   prophet-vocative directive pair (J=0.245) and noted the two are "textual near-twins." This pre-reg
   promotes that observation into a falsifiable corpus-rarity claim about the *full-verse* twin.

2. **The antithetical dual-exemplar seal (vv 10-12).** The surah closes with a paired-parable:
   `ḍaraba Allāh mathalan li-lladhīna kafarū` (the wife of Nūḥ + the wife of Lūṭ, v 10) set
   antithetically against `wa-ḍaraba Allāh mathalan li-lladhīna āmanū` (the wife of Firʿawn / Āsiya,
   v 11 + Maryam bint ʿImrān, v 12). al-Qurṭubī (*al-Jāmiʿ li-aḥkām al-Qurʾān*, on v 11, citing Yaḥyā
   b. Sallām) reads the dual-exemplar seal as a direct admonition to ʿĀʾisha and Ḥafṣa — a believing-
   wife exhortation framed by the negative wife-of-prophet exemplars. We test whether this
   antithetical kafarū/āmanū exemplar-frame is corpus-distinctive and whether the two believer-
   exemplars (vv 11, 12) cohere lexically more tightly with each other than with the disbeliever-
   exemplar (v 10).

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes/word-tokens, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Verse text from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
Pause/sajda diacritic marks (ۖ ۚ ۗ ۛ ۙ ۘ ۞ etc.) stripped before tokenization. Word = whitespace-
delimited orthographic token after mark-stripping. Roots from QAC v0.4
(`/Users/grey/Downloads/quran/data/morphology/root-index.json`, `[surah,verse,word]` attestations).

## Arm A — verbatim full-verse twin rarity (CONFIRMATORY)

**Hypothesis A (pre-committed):** Q 66:9 is a member of the small set of corpus *verbatim full-verse
twins* — verses of length ≥10 word-tokens whose mark-stripped text appears identically in ≥2 distinct
verse positions.

- **A-H1:** Q 66:9 (mark-stripped) appears verbatim at exactly one other corpus position, namely Q 9:73.
- **A-H2:** The corpus count of distinct verbatim full-verse-twin GROUPS at length ≥10 tokens is ≤ 20
  (i.e. verbatim long-verse repetition is rare; Q 66:9 is one of a small roster).
- **A-H3 (direction-locked):** Under a length-matched permutation null that shuffles which verses share
  text (see null A below), the observed number of length-≥10 verbatim-twin groups is LOWER than the
  random-collision expectation would be if verses of matched length-distribution were assigned random
  shared-skeletons — i.e. the Quran's verbatim long-verse twins are *deliberate repetitions*, not
  random collisions. **Direction lock: observed verbatim-twin structure is NON-RANDOM (concentrated in
  few exact-repeat groups, not spread as many near-misses).**

  Operationalization of A-H3 null: we cannot permute Arabic text meaningfully, so the null is the
  closed-form / combinatorial baseline — the probability that two independently-drawn corpus verses of
  ≥10 tokens are character-identical by chance. We report the empirical fraction of ≥10-token verse
  pairs that are verbatim-identical and compare to the chance collision rate under a unigram/bigram
  surface model. Direction: observed verbatim-pair rate ≫ chance (repetition is intentional). Because
  this arm is essentially descriptive-combinatorial, A is graded CONFIRMED only on A-H1 ∧ A-H2 (both
  deterministic); A-H3 is reported as supporting context, not a gating permutation test.

**A success criterion:** A-H1 ∧ A-H2 both hold → Arm A CONFIRMED (deterministic corpus fact).
**A failure criterion:** either A-H1 (Q 66:9 has 0 or ≥2 verbatim partners) or A-H2 (>20 groups) fails → Arm A NULL.

## Arm B — antithetical dual-exemplar seal (CONFIRMATORY + DIRECTION-LOCKED)

**Hypothesis B (pre-committed):**

- **B-H1 (corpus-exclusivity of the antithetical frame):** The adjacent antithetical exemplar-frame
  pair — a verse opening `ḍaraba Allāh mathalan li-lladhīna kafarū` immediately followed (next verse)
  by `wa-ḍaraba Allāh mathalan li-lladhīna āmanū` — is corpus-EXCLUSIVE to Q 66:10-11. **Direction lock:
  count of such adjacent kafarū→āmanū exemplar-frame pairs in the corpus = 1 (Q 66 only).**

- **B-H2 (believer-exemplar internal cohesion):** Within the seal triad {v10 (disbeliever exemplars),
  v11 (Āsiya), v12 (Maryam)}, the two believer-exemplar verses (v11, v12) share a higher root-Jaccard
  with each other than either shares with the disbeliever-exemplar verse (v10). **Direction lock:
  J(v11,v12) > J(v10,v11) AND J(v11,v12) > J(v10,v12).** Note v12 lacks the `ḍaraba ... mathalan` frame
  (it is conjoined to v11 by *wa-*), so the frame-roots {ḍ-r-b, m-th-l} are shared by v10,v11 but NOT
  v12 — this BIASES AGAINST B-H2 (the frame would pull v10-v11 together). B-H2 passing despite this
  bias is the informative result.

- **B-H3 (seal cohesion vs corpus baseline):** The mean pairwise root-Jaccard of the believer-exemplar
  pair {v11, v12} exceeds the null distribution of mean root-Jaccard for random same-surah adjacent
  verse pairs drawn length-matched from the corpus. **Permutation null B (seed=20260509, 10000 perms):**
  draw random pairs of corpus verses matched to (n_roots(v11), n_roots(v12)) within ±3 roots; compute
  J; the p-value is the fraction of null draws with J ≥ J(v11,v12). **Direction lock: J(v11,v12) >
  null (TIGHTER).** Bonferroni: this is 1 cell of the family (see below).

**B success criterion:** B-H1 (count=1) ∧ B-H2 (both inequalities) ∧ B-H3 (p < α_corrected) → Arm B CONFIRMED.
**B partial:** 2/3 sub-hypotheses → DIRECTIONAL.
**B failure / pre-commit violation:** if J(v11,v12) < J(v10,v11) or J(v11,v12) < J(v10,v12) (B-H2 direction
reversed) OR J(v11,v12) < null (B-H3 direction reversed) → published as NULL with explicit pre-commit-violation flag.

## Null distributions

- **Null A (Arm A context):** closed-form surface-collision baseline (unigram + bigram) over ≥10-token
  verses; reported as supporting context only.
- **Null B (Arm B B-H3):** length-matched random-verse-pair permutation, seed=20260509, 10000 perms,
  matching window ±3 roots on each member. p_perm = (#{null J ≥ obs} + 1) / (N_perm + 1).

## Bonferroni

Test family Q066-F-01 has k = 1 permutation cell (B-H3). The deterministic cells (A-H1, A-H2, B-H1, B-H2)
are not permutation tests and do not consume α. α_corrected for the single permutation cell = 0.05 / 1 = 0.05.
(For the wider Q 66 surah-session, the cross-test family Bonferroni is reported in 06-novel-findings.md.)

## MW protections

- **MW-1 (instrument-prior):** verbatim-match, antithetical-frame regex, and root-Jaccard all defined here before any run.
- **MW-2 (corpus-prior):** Null B uses 10,000 length-matched permutations.
- **MW-3 (alternative-models):** Arm A reports both deterministic count and surface-collision baseline; B-H2 reports the frame-root bias explicitly.
- **MW-5 (replication):** Arm A and B-H1/B-H2 are deterministic and fully replicable from the no-tashkeel JSON + QAC root-index. B-H3 seed-locked.
- **MW-6 (instrument-control):** B-H3 length-matching is the non-target control.
- **MW-7 (post-hoc cap):** the antithetical-frame and verbatim-twin observations were noticed during close reading; both are promoted to PRE-REGISTERED direction-locked tests here before computation, so the single-test α=0.05 cap is respected and not exceeded.

## Verdict mapping

| Arm | Pass condition | Verdict label |
|:--|:--|:--|
| A | A-H1 ∧ A-H2 | CONFIRMED (deterministic corpus-rarity) |
| B | B-H1 ∧ B-H2 ∧ B-H3 | CONFIRMED |
| B | 2/3 | DIRECTIONAL |
| B | direction reversed on B-H2 or B-H3 | NULL (pre-commit violation, full prominence) |

Final Q066-F-01 verdict = honest combination of Arm A and Arm B, reported with equal NULL prominence.

*Locked 2026-05-29. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
