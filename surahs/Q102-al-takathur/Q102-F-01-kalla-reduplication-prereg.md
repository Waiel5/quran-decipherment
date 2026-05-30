---
surah: 102
surah_name_ar: التكاثر
surah_name_translit: al-Takāthur
file_type: prereg
test_id: Q102-F-01
date_locked: 2026-05-30
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-COMPUTATION
---

# Q102-F-01 — Pre-Registration: al-Takāthur's rebuke-*kallā* triple-run + the single-particle refrain

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q102_F_01_kalla_reduplication.py` and verified at runtime (fail-fast on mismatch).

## Motivation

Q 102 al-Takāthur (8 verses, Early Meccan, revelation-order #16 per `data/revelation-order.csv`)
carries a striking surface feature: three consecutive verses each open with the rebuke-particle
*kallā* (كلَّا, "Nay! By no means!"), the first two of which are near-verbatim threats differing by
a single connective particle:

- v 3: *kallā sawfa taʿlamūn* ("Nay! you shall come to know")
- v 4: *thumma kallā sawfa taʿlamūn* ("then, nay! you shall come to know")
- v 5: *kallā law taʿlamūna ʿilma al-yaqīn* ("Nay! if you knew with the knowledge of certainty…")

Two project anchors converge here:

1. **The rebuke-*kallā* census (H-NEW-2160 / H-NEW-2230 / §10.80).** al-Suyūṭī (*al-Itqān fī ʿulūm
   al-Qurʾān*, nawʿ 40, citing al-Dānī *al-Muktafā*) holds that the rebuke-particle *kallā* occurs **33
   times**, concentrated in the latter (mufaṣṣal) half. The project's QAC-lemma disambiguation
   (`findings/phase-b-hypotheses/h-new-2230-qac-lemma-numerical-rerun.md`, claim 7) CONFIRMED the count
   = 33 exactly (POS:AVR LEM `kal~aA`) and recorded the per-surah distribution as including **Q102(3)**.
   We re-verify Q102's 3 *kallā* tokens are genuine POS:AVR (not the *kullan/kilā* quantifier homograph
   that contaminates raw substring counts) and that they sit in three consecutive verses.

2. **The refrain / reduplication axis (H-NEW-2310).** al-Ṭabarī (*Jāmiʿ al-bayān*, on Q 102:4) states
   the explicit balāgha rationale for the v3/v4 doubling: *"wa-karrara qawlahu (kallā sawfa taʿlamūn)
   marratayn, li-anna al-ʿArab idhā arādat al-taghlīẓ fī al-takhwīf wa-l-tahdīd karrarū al-kalimata
   marratayn"* — "He repeated the saying twice, because the Arabs, when they wish to intensify a
   warning and a threat, repeat the word twice." We test whether this near-verbatim adjacent threat
   doubling is corpus-distinctive.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes/word-tokens, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`
plus, for the *kallā* part-of-speech disambiguation: `(QAC v0.4, POS:AVR, LEM kal~aA)`.

Verse text from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (pause/sajda diacritic
marks ۖ ۚ ۗ ۛ ۙ ۘ ۞ etc. stripped before tokenization; word = whitespace-delimited orthographic token).
*kallā* part-of-speech / lemma from QAC v0.4 morphology
(`/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`).

## Arm A — corpus-unique 3-consecutive-verse rebuke-*kallā* run (CONFIRMATORY + DIRECTION-LOCKED)

**Hypothesis A (pre-committed):** Among all 114 surahs, Q 102 is the UNIQUE carrier of a run of **3
consecutive verses** that each contain a genuine rebuke-*kallā* (POS:AVR, LEM `kal~aA`). Every other
surah has a maximum consecutive-*kallā* run of ≤ 2.

- **A-H1 (verification):** Q 102 has exactly 3 rebuke-*kallā* tokens (POS:AVR LEM `kal~aA`), located in
  verses 3, 4, 5 — i.e. a consecutive run of length 3.
- **A-H2 (corpus-census):** the total corpus rebuke-*kallā* count is 33 (replicating H-NEW-2230 /
  al-Dānī); none of the 33 first-half (Q 1–18) tokens are the rebuke particle (homograph-clean).
- **A-H3 (direction-locked, the gating claim):** the maximum consecutive-verse rebuke-*kallā* run
  length, computed per surah across the whole corpus, is **3 for Q 102 and ≤ 2 for every other surah**
  — Q 102 is the sole maximum. **Direction lock: Q 102's run (=3) STRICTLY EXCEEDS every other surah's
  run.**

**A success criterion:** A-H1 ∧ A-H2 ∧ A-H3 all hold → Arm A CONFIRMED (deterministic corpus-singleton).
**A failure / pre-commit violation:** if any other surah also has a run ≥ 3 (A-H3 ties or reverses), or
if Q 102's count ≠ 3 (A-H1 fails), or the census ≠ 33 (A-H2 fails) → published as NULL with explicit
pre-commit-violation flag.

## Arm B — the single-particle near-verbatim adjacent refrain (CONFIRMATORY + DIRECTION-LOCKED)

**Hypothesis B (pre-committed):**

- **B-H1 (corpus-exclusivity):** the ordered adjacent verse-pair (v_n = *kallā sawfa taʿlamūn*,
  v_{n+1} = *thumma kallā sawfa taʿlamūn*) — i.e. two consecutive verses whose mark-stripped texts are
  IDENTICAL except that the second is the first with a single prefixed connective particle (*thumma*) —
  is corpus-EXCLUSIVE to Q 102:3-4. **Direction lock: count of such single-particle-differentiated
  adjacent refrain pairs in the corpus = 1 (Q 102 only).**

- **B-H2 (refrain-bare-threat singleton):** the bare threat-clause string *sawfa taʿlamūn* standing
  alone as the predicate of a *kallā*-rebuke verse (the entire post-*kallā* verse content = *sawfa
  taʿlamūn*) occurs corpus-wide only at Q 102:3 and Q 102:4. **Direction lock: count = 2, both in
  Q 102.** (The 9 other *sawfa/sa-taʿlamūn*-bearing verses embed it in longer clauses; Q 102 is the
  only place the threat is left bare and reduplicated.)

- **B-H3 (permutation null-control on the refrain rarity):** Construct a length-matched permutation
  null (seed 20260509, 10000 perms): over all corpus adjacent verse-pairs (v_n, v_{n+1}) within a
  surah, count how many are "single-particle near-twins" (normalized edit = exactly one whole-token
  insertion/deletion AND the longer is the shorter plus one leading particle from the closed set
  {ثم, و, ف, بل, او}). Compare the observed corpus count of such adjacent near-twin pairs (deterministic)
  to a null in which the per-surah verse texts are randomly re-paired within length-strata. **Direction
  lock: the observed adjacent single-particle near-twin structure is RARER / more concentrated than a
  random re-pairing would produce (the Quran's adjacent refrains are deliberate, not chance
  collisions).** Because Arabic text cannot be meaningfully permuted token-internally, B-H3 is a
  descriptive-combinatorial control: we report the deterministic corpus count of single-particle
  adjacent near-twin pairs and the chance-collision baseline; B is graded on B-H1 ∧ B-H2 (both
  deterministic); B-H3 is supporting context, not a gating permutation test.

**B success criterion:** B-H1 (count=1) ∧ B-H2 (count=2, both Q102) → Arm B CONFIRMED.
**B partial:** exactly one of B-H1 / B-H2 holds → DIRECTIONAL.
**B failure / pre-commit violation:** if B-H1's adjacent single-particle refrain pair exists elsewhere
(count > 1), or B-H2's bare-threat count ≠ 2 → published as NULL with explicit pre-commit-violation flag.

## Null distributions

- **Null A (Arm A context):** none required — A is a deterministic corpus census (run-length over the
  POS:AVR *kallā* token set). The "control" is the per-surah run-length distribution itself (reported
  in full).
- **Null B (Arm B B-H3):** length-stratified random re-pairing of within-surah adjacent verses,
  seed=20260509, 10000 perms; reported as supporting context for the rarity of single-particle adjacent
  near-twins. p_perm = (#{null count ≥ obs} + 1) / (N_perm + 1) reported for completeness only.

## Bonferroni

Test family Q102-F-01 has k = 0 gating permutation cells (both arms are deterministic corpus censuses;
B-H3 is reported as supporting context only and does not consume α). No permutation-α is consumed.
For the wider Q 102 surah-session this is the single landed test, so no cross-test correction is needed.
If B-H3 were promoted to a gating test, α_corrected = 0.05 / 1 = 0.05.

## MW protections

- **MW-1 (instrument-prior):** run-length over POS:AVR *kallā*, the single-particle near-twin rule, and
  the bare-threat string are all defined HERE before any run.
- **MW-2 (corpus-prior):** Null B uses 10,000 length-stratified permutations (supporting context).
- **MW-3 (alternative-models):** A reports the full per-surah run-length distribution (not just Q 102);
  B reports both the strict single-particle-near-twin count and the bare-threat count.
- **MW-5 (replication):** A-H1/A-H2/A-H3, B-H1, B-H2 are all deterministic and fully replicable from the
  no-tashkeel JSON + QAC morphology file. B-H3 seed-locked at 20260509.
- **MW-6 (instrument-control):** Arm A's per-surah run distribution is itself the non-target control
  (the 113 other surahs); B-H3's length-stratified re-pairing is the non-target control.
- **MW-7 (post-hoc cap):** the *kallā* triple-run and the single-particle refrain were noticed during
  close reading of Q 102; both are promoted to PRE-REGISTERED direction-locked tests HERE before any
  computation, so the single-test cap is respected and not exceeded.

## Verdict mapping

| Arm | Pass condition | Verdict label |
|:--|:--|:--|
| A | A-H1 ∧ A-H2 ∧ A-H3 (Q 102 sole max-run = 3, others ≤ 2; census 33; homograph-clean) | CONFIRMED (deterministic corpus-singleton) |
| A | another surah ties or exceeds run = 3 | NULL (pre-commit violation, full prominence) |
| B | B-H1 (count=1) ∧ B-H2 (count=2) | CONFIRMED |
| B | 1 of 2 | DIRECTIONAL |
| B | refrain pair exists elsewhere | NULL (pre-commit violation, full prominence) |

Final Q102-F-01 verdict = honest combination of Arm A and Arm B, reported with equal NULL prominence.

*Locked 2026-05-30. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
