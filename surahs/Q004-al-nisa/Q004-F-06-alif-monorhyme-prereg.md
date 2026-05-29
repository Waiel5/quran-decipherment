---
surah: 4
surah_name_ar: النساء
surah_name_translit: al-Nisāʾ
file_type: prereg
test_id: Q004-F-06
date_locked: 2026-05-29
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-COMPUTATION
---

# Q004-F-06 — Pre-Registration: the al-Nisāʾ alif-monorhyme anomaly (is Q4 the lone alif-rhyme long-surah, and is its rhyme concentration extreme for its length?)

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q004_F_06_alif_monorhyme.py` and verified at runtime (fail-fast on mismatch).

## Motivation

The seven long surahs (*al-sabʿ al-ṭiwāl*) are overwhelmingly nūn-rhymed — al-Bāqillānī's *iʿjāz al-fawāṣil*
(the inimitability of the verse-endings) treats the long-Medinan fāṣila as predominantly the *-ūn/-īn*
nominal/verbal-suffix nūn. On close reading, Q 4 al-Nisāʾ is the conspicuous exception: its verse-endings are
dominated not by nūn but by **alif** (ا), to a degree (visually) approaching a monorhyme. This is striking
because Q 4 is a 176-verse legal surah — the alif-ending is the *-an*/*-hā*/dual-and-broken-plural ending and
the long *qaṣīda*-style *rawī* of alif, which one expects in short oath-surahs (Q 91 al-Shams, Q 92 al-Layl),
NOT in a long legal surah.

H-NEW-700 (`rhyme.rhyme_letter_diagnostics`) records each surah's dominant final-letter and its fraction.
H-NEW-750 records the rhyme-entropy and the al-Bāqillānī structural-significance signature sig_A. This pre-reg
promotes the close-reading observation into two falsifiable, direction-locked corpus claims.

## Rules-tuple

`(min-tashkeel for rhyme final-letter, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Rhyme dominant-final-letter and fraction read from
`findings/phase-b-hypotheses/csv/h-new-700.json` (`rhyme.rhyme_letter_diagnostics`). sig_A and rhyme_entropy
read from `findings/phase-b-hypotheses/csv/h-new-750.json` (`per_surah`). No value asserted from memory.

## Definitions

- *al-sabʿ al-ṭiwāl* = the seven long surahs {Q2, Q3, Q4, Q5, Q6, Q7, Q9} (the classical roster, taking Q9
  al-Tawba as the seventh per al-Suyūṭī, *al-Itqān*; Q8+Q9 sometimes counted together — the alternative roster
  {2,3,4,5,6,7,(8+9)} is tested as a robustness variant in Arm A note).
- *long surah* (length-stratified null, Arm C) = surah with n_verses ≥ 100.
- dominant-final-letter fraction = `frac` field of `rhyme_letter_diagnostics`.

## Arm A — Q4 is the unique alif-rhyme long surah (DETERMINISTIC, DIRECTION-LOCKED)

**Hypothesis A (pre-committed):** Among *al-sabʿ al-ṭiwāl* {Q2,Q3,Q4,Q5,Q6,Q7,Q9}, Q 4 al-Nisāʾ is the
**only** surah whose dominant final-letter is **alif** (ا); all six others are nūn (ن).

- **A-H1 (direction-locked):** count of alif-dominant surahs in {2,3,4,5,6,7,9} = **exactly 1** (= Q4); the
  other six are nūn-dominant.

**A success:** A-H1 holds → Arm A CONFIRMED (deterministic).
**A failure / direction violation:** Q4 is nūn-dominant, OR ≥2 alif-dominant surahs in the roster → Arm A NULL.

## Arm B — Q4's rhyme is a structural-iʿjāz minimum (DETERMINISTIC, DIRECTION-LOCKED)

**Hypothesis B (pre-committed):** Q 4's near-monorhyme suppresses fāṣila variety, so its al-Bāqillānī
structural-iʿjāz signature sig_A (which rewards rhyme-entropy) is among the corpus minima.

- **B-H1 (direction-locked):** Q 4's sig_A rank (descending; 1 = highest sig_A) is in the **bottom 3** of 114
  (rank ≥ 112), AND its rhyme_entropy_nats is below the corpus mean (z_rhyme_entropy < 0).

**B success:** sig_A rank ≥ 112 ∧ z_rhyme_entropy < 0 → Arm B CONFIRMED.
**B failure / direction violation:** sig_A rank < 112 OR z_rhyme_entropy ≥ 0 → Arm B NULL.

## Arm C — is Q4's rhyme concentration extreme GIVEN its length? (PERMUTATION, seed 20260509, 10000 perms)

A short oath-surah can trivially hit 100% monorhyme on a handful of verses. The non-trivial claim is that a
**176-verse** surah holding 96% single-rhyme is extreme. Arm C tests Q4's `frac` against a length-stratified
null built from the long surahs.

- **Null C:** the pool = all surahs with n_verses ≥ 100 (the long-surah stratum), EXCLUDING Q4. seed=20260509,
  10000 perms. Each perm: draw one pool surah uniformly at random and record its `frac`. (Because the stratum
  is small, the permutation is a bootstrap-resample of the long-surah `frac` distribution; the p-value is the
  fraction of draws with `frac` ≥ Q4's `frac`.)
- **C-H1 (direction-locked):** Q4's `frac` is in the **upper tail** of the long-surah `frac` distribution:
  p_perm = (#{pool_frac ≥ obs} + 1)/(N+1). **Direction: Q4 is HIGH-concentration relative to long surahs.**
  Pass at α = 0.05 requires Q4 in the top ~5% of the length-stratified distribution.

**C success:** p_perm < 0.05 → Q4's concentration is extreme for its length-stratum.
**C honest-limit pre-commitment:** the long-surah stratum contains Q17 (0.991) and Q18 (0.991) and Q23 (0.966),
which exceed Q4 (0.960). Therefore Q4 is NOT expected to be the stratum maximum; if Q4 falls OUTSIDE the top
5% (p_perm ≥ 0.05) the arm is reported as NULL/DIRECTIONAL with full prominence — the alif-monorhyme is then
"notable but not a length-stratified extreme." This failure mode is pre-committed.

## Bonferroni

Test family Q004-F-06 has k = 1 permutation cell (Arm C). Deterministic cells (A-H1, B-H1) do not consume α.
α_corrected = 0.05 / 1 = 0.05.

## MW protections

- **MW-1 (instrument-prior):** alif-vs-nūn definition, sig_A rank threshold, and length-stratified `frac` null all fixed here before any run.
- **MW-2 (corpus-prior):** Arm C uses 10,000 length-stratified resamples.
- **MW-3 (alternative-models):** Arm A note tests the {2,3,4,5,6,7,8+9} alternative ṭiwāl roster; Arm B uses an independent instrument (sig_A) from Arm A.
- **MW-5 (replication):** Arms A, B deterministic; Arm C seed-locked at 20260509.
- **MW-6 (instrument-control):** Arm C's length-stratification (n_verses ≥ 100) is the non-target control against the trivial short-surah-monorhyme confound.
- **MW-7 (post-hoc cap):** the alif-rhyme observation is from close reading; promoted to direction-locked pre-registered tests here before computation. Arm C's honest-limit (Q17/Q18/Q23 exceed Q4) is pre-committed, capping the over-claim.

## Verdict mapping

| Arm | Pass condition | Verdict label |
|:--|:--|:--|
| A | A-H1 (Q4 unique alif in ṭiwāl) | CONFIRMED (deterministic) |
| B | sig_A rank ≥ 112 ∧ z_rhyme_entropy < 0 | CONFIRMED |
| C | p_perm < 0.05 | CONFIRMED (length-stratified extreme) |
| C | p_perm ≥ 0.05 | NULL/DIRECTIONAL (notable-not-extreme), full prominence |
| any | direction reversed | NULL (pre-commit violation, full prominence) |

Final Q004-F-06 verdict = honest combination of Arms A, B, C, reported with equal NULL prominence.

*Locked 2026-05-29. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
