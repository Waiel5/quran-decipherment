---
surah: 20
surah_name_ar: طه
surah_name_translit: Ṭā-Hā
file_type: prereg
test_id: Q020-F-06
date_locked: 2026-05-30
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-PERMUTATION-NULL
---

# Q020-F-06 — Pre-Registration: Ṭā-Hā as the burning-bush prototype of the Mūsā pericope cycle

**LOCKED BEFORE THE PERMUTATION NULL IS RUN.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q020_F_06_musa_hub.py` and verified at runtime (fail-fast on mismatch).

## Motivation

H-NEW-2260 (`findings/phase-b-hypotheses/h-new-2260-prophet-cycle-pericope.md`) established that the
**Mūsā burning-bush / Pharaoh-commissioning cycle PASSES at pericope scale** (mean pairwise root-Jaccard
J_obs = 0.2168, null mean 0.1056, **z = +3.34, p_perm = 0.0017**, Bonferroni-PASS at α = 0.0167) — the
single strongest of the three prophet-cycles tested. The cycle's four locked pericopes are:

- **Q 20:9-36** (Ṭā-Hā — 28 verses, the longest and most detailed retelling)
- **Q 27:7-14** (al-Naml — 8 verses)
- **Q 28:29-35** (al-Qaṣaṣ — 7 verses)
- **Q 79:15-26** (al-Nāziʿāt — 12 verses)

H-NEW-2260 reported only the **cycle-level mean** and the single strongest *pair* (Q 27 × Q 28, J = 0.363).
It did NOT answer the Ṭā-Hā-specific question this surah investigation owns:

> **Is the Ṭā-Hā burning-bush pericope (Q 20:9-36) — the cycle's longest, most-detailed member —
> a genuine lexical HUB of the cycle: does it cohere with the other three retellings ABOVE a
> length-matched random-pericope baseline?**

This promotes the Ṭā-Hā role in the Mūsā cycle from "largest member" to a falsifiable, direction-locked
per-pericope cohesion claim, and tests the H-NEW-2260 refinement ("cohesion is content-anchored, not
automatic") at the level of the single Ṭā-Hā pericope.

## Rules-tuple

`(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Identical to H-NEW-2260 for comparability. Roots from
`/Users/grey/Downloads/quran/data/morphology/root-index.json` (`[surah,verse,word]` attestations).
Pericope root-set = union of all QAC roots attested in the pericope's verse range. Verse text /
pericope-boundary existence verified against
`/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` at runtime (`verify_boundaries()`).

## Arm A — Ṭā-Hā signature-root completeness (DETERMINISTIC-DESCRIPTIVE, MW-7-CAPPED)

**Observation promoted to a deterministic descriptive claim (not a gating permutation cell):**
Q 20:9-36 carries the **most complete burning-bush episode-signature-root set** of any cycle member.

- **A-H1 (deterministic):** of the six H-NEW-2260-named Mūsā episode-signature roots
  `{byD (white hand), ESw (staff), Twy (the valley Ṭuwā), Ans (perceived fire), *hb (go [to Pharaoh]),
  dbr (turning away)}`, Q 20:9-36 contains the **maximum count** among the four cycle pericopes.
- **A-H2 (deterministic):** the Ṭā-Hā-anchored conserved core (roots in Q 20:9-36 ∩ all three other
  cycle members) is non-empty and includes the narrative-frame roots.

**A is graded on A-H1 ∧ A-H2 (both deterministic corpus facts).** Because the signature-root *list* was
imported from the prior H-NEW-2260 finding (not chosen after viewing Q 20's roots), A is reported under
the MW-7 single-test cap as a descriptive corpus fact, NOT as a statistical-surprise claim.

## Arm B — Ṭā-Hā hub-strength vs length-matched random-pericope null (CONFIRMATORY, DIRECTION-LOCKED)

**Hypothesis B (pre-committed, direction inherited from H-NEW-2260 parent = TIGHTER):**
The mean pairwise root-Jaccard of the Ṭā-Hā pericope (Q 20:9-36) to the OTHER THREE Mūsā-cycle pericopes
— its **hub-strength** `H(Q20) = mean{ J(Q20,Q27), J(Q20,Q28), J(Q20,Q79) }` — EXCEEDS the distribution
of hub-strengths obtained when the Ṭā-Hā pericope is replaced by a length-matched random corpus pericope.

- **B-H1 (direction-locked):** `H(Q20) > null_mean` (z > 0). **DIRECTION LOCK: TIGHTER.** A z ≤ 0 (Ṭā-Hā
  hub-strength at or below the random-pericope expectation) is a **pre-commit violation**, published as
  NULL with full prominence per PRE-REG-STANDARD-04.
- **B-H2 (significance):** `p_perm ≤ α_corrected` (see Bonferroni below).

**Permutation null B (seed 20260509, 10,000 perms):** keep the three partner pericopes {Q 27:7-14,
Q 28:29-35, Q 79:15-26} fixed; replace the Ṭā-Hā pericope by a random contiguous verse-window drawn from
the corpus whose verse-length is matched to 28 within ±3 verses (the Q 20:9-36 length); recompute
H = mean{ J(rand, Q27), J(rand, Q28), J(rand, Q79) }. The window must not overlap any of the four cycle
pericopes (excluded). p_perm = (#{null H ≥ H(Q20)} + 1) / (N_perm + 1).

## Pre-committed verdict mapping

| Arm / cell | Pass condition | Verdict label |
|:--|:--|:--|
| A (A-H1 ∧ A-H2) | both deterministic facts hold | CONFIRMED (deterministic descriptive) |
| B (B-H1 ∧ B-H2) | z > 0 AND p_perm ≤ α_corrected | CONFIRMED |
| B | z > 0 AND p_perm > α_corrected | DIRECTIONAL |
| B | z ≤ 0 (direction reversed) | NULL (pre-commit violation, full prominence) |

Final Q020-F-06 verdict = honest combination of Arm A and Arm B, reported with equal NULL prominence.

## Bonferroni

Test family Q020-F-06 has **k = 1 permutation cell** (B). α_corrected = 0.05 / 1 = 0.05. The deterministic
cells (A-H1, A-H2) are corpus facts and do not consume α. (For the wider Q 20 surah session, the six
landed tests Q020-F-01..F-06 are tabulated in `06-novel-findings.md`; F-06 is the only newly-run
permutation cell of this session — F-01..F-05 were run and SHA-locked in the 2026-05-07 session.)

## Null distribution

- **Null B:** length-matched (±3 verses on the 28-verse Q 20:9-36 length) random contiguous-verse-window
  null, excluding windows overlapping any of the four cycle pericopes; seed 20260509; 10,000 perms.
  p_perm = (#{null H ≥ obs} + 1) / (N_perm + 1).

## MW protections

- **MW-1 (instrument-prior):** hub-strength metric (mean ROOT-Jaccard to fixed partners), signature-root
  set (imported verbatim from H-NEW-2260), and direction (TIGHTER) all fixed here before the null is run.
- **MW-2 (corpus-prior):** Null B uses 10,000 length-matched permutations.
- **MW-3 (alternative-models):** Arm A (deterministic signature completeness) and Arm B (permutation
  hub-strength) triangulate the Ṭā-Hā-prototype claim on two independent instruments; the per-pair
  Jaccards are also reported descriptively so the hub-ranking among the four members is transparent.
- **MW-5 (replication):** Arm A is deterministic and fully replicable from the no-tashkeel JSON + QAC
  root-index; Arm B seed-locked at 20260509. H-NEW-2260 is the cycle-level replication anchor.
- **MW-6 (instrument-control):** Null B's length-matched, cycle-non-overlapping random-window pool is the
  non-target control.
- **MW-7 (post-hoc cap):** the signature-root list is imported from the prior finding (no Q-20-specific
  cherry-picking); Arm A is reported under the single-test descriptive cap. The hub-strength direction is
  the parent finding's locked direction, decided independent of Q 20's specific Jaccard values.

## Honest limits (locked before run)

- The hub-strength metric ranks Ṭā-Hā among the four members descriptively; whether Ṭā-Hā is the
  numerical maximum hub is NOT the locked hypothesis (Arm B tests only that Ṭā-Hā coheres ABOVE the
  random baseline, direction TIGHTER). The descriptive hub-ranking is reported MW-7-capped.
- ROOT-Jaccard is the single locked lens (for H-NEW-2260 comparability). A lemma or orthographic-token
  lens could shift the value (rules-tuple sensitivity is bidirectional); flagged as a follow-up.
- Pericope boundaries are the H-NEW-2260-locked scholar-conventional blocks; a different defensible
  segmentation could shift J at the margin.
- N = 4 cycle pericopes (3 partners for the hub). Power is limited; the permutation null is exact under
  the model but the claim rests on a single cycle.

*Locked 2026-05-30. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
