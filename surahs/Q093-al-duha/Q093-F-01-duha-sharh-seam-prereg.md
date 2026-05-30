---
surah: 93
surah_name_ar: الضحى
surah_name_translit: al-Ḍuḥā
file_type: prereg
test_id: Q093-F-01
date_locked: 2026-05-30
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-COMPUTATION
---

# Q093-F-01 — Pre-Registration: al-Ḍuḥā ↔ al-Sharḥ seam scale-dissociation + the favor→command orphan-recall

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q093_F_01_duha_sharh_seam.py` and verified at runtime (fail-fast on mismatch).

## Motivation

Q 93 al-Ḍuḥā and Q 94 al-Sharḥ are, across the classical tradition, debated as a **paired or single
unit**. al-Suyūṭī (*al-Itqān*, nawʿ on al-munāsaba bayna al-suwar) and al-Rāzī (*Mafātīḥ al-ghayb*, on
Q 94:1) report the position — attributed to Ṭāwūs and ʿUmar b. ʿAbd al-ʿAzīz — that the two are recited
together as one prayer-unit without a basmala between them, on the strength of their twinned consolation
theme (the *ʿusr/yusr* "with hardship comes ease" of Q 94:5-6 answering the orphan/wanderer/poor triad of
Q 93). The classical *al-ṭibāq*/paired-surah reading thus predicts an unusually tight Q 93 ↔ Q 94 bond.

The project has two relevant instruments that operate at DIFFERENT scales:
1. **Whole-surah scale** — Fisher-Rao root-distribution distance (H-NEW-111) and the TSP-residual
   canonical-adjacency seam-cost (H-NEW-720).
2. **Boundary-pericope scale** — the H-NEW-2280 seam root-Jaccard on the last-k / first-k verses of the
   two surahs (the granularity at which al-Biqāʿī locates *munāsaba*).

cross-finding-025 (scale-of-aggregation law) predicts cohesion is **granularity-dependent**. This test
asks whether the classically-claimed Q 93 ↔ Q 94 pairing manifests at the whole-surah scale, the
boundary-lexical scale, or both — and pre-registers a DISSOCIATION direction.

A second close-reading observation: Q 93's body has a **triadic past-favor block** (vv 6-8, each
`wajadaka X fa-Y`: orphan→sheltered, wandering→guided, poor→enriched) followed by a **triadic
future-command block** (vv 9-11: orphan→do-not-oppress, asker→do-not-repel, blessing→proclaim).
We test whether this favor→command structure leaves a lexical fingerprint and whether it is
corpus-distinctive.

**MW-7 disclosure.** Both phenomena were noticed during close reading of Q 93 BEFORE this pre-reg was
written, but the directional predictions and the permutation null are locked here BEFORE any statistic
is computed in the run script. Per MW-7 the single-test α=0.05 cap is respected; no result is reported
that was not pre-committed in direction.

## Rules-tuple

`(no-tashkeel, orthographic-token, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Verse text from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`. Pause/sajda diacritic
marks stripped before tokenization. Roots from QAC v0.4
(`/Users/grey/Downloads/quran/data/morphology/root-index.json`, `[surah,verse,word]` attestations).
Whole-surah Fisher-Rao distances from `findings/phase-b-hypotheses/csv/h-new-111.json`
(`D_matrix_upper_triangular`, 1-indexed). TSP seam-costs from
`findings/phase-b-hypotheses/csv/h-new-720.json` (`per_adjacency`). Boundary-seam null reproduces the
H-NEW-2280 method (`findings/phase-b-hypotheses/h-new-2280-munasabah-seam.md`).

## Arm A — Q 93 ↔ Q 94 seam scale-dissociation (DIRECTION-LOCKED + PERMUTATION)

**Hypothesis A (pre-committed):** The classically-claimed Q 93 ↔ Q 94 pairing is realized at the
WHOLE-SURAH root-distribution scale (FR proximity + smooth TSP seam) but NOT at the boundary-pericope
lexical scale (seam root-Jaccard does not exceed the corpus seam-null). This is a **dissociation**:
cohesion lives at the surah-distribution scale, not the boundary-lexis scale.

- **A-H1 (whole-surah FR proximity, direction-locked):** Q 94 al-Sharḥ is among Q 93's **top-5 nearest**
  Fisher-Rao neighbors (of 113). **Direction lock: rank(Q94 in Q93's FR list) ≤ 5.**
- **A-H2 (whole-surah TSP seam smoothness, direction-locked):** The Q 93 → Q 94 canonical-adjacency seam
  is among the **top-15 smoothest** of the 113 mushaf seams (ascending delta_raw rank ≤ 15), i.e. a
  near-seamless or seamless joint. **Direction lock: ascending-rank(Q93→Q94 delta_raw) ≤ 15.**
- **A-H3 (boundary-lexical seam, direction-locked DISSOCIATION):** The H-NEW-2280-style boundary-seam
  root-Jaccard between the last-k verses of Q 93 and the first-k verses of Q 94 (k ∈ {3, 5}) is
  **≤ the corpus mean seam root-Jaccard** at the same k. **Direction lock: J_seam(Q93→Q94) ≤
  corpus_mean_seam_J(k) for both k=3 and k=5.** (The dissociation prediction: the boundary lexis is
  WEAK even though the whole-surah seam is smooth.)
- **A-H4 (permutation confirmation of dissociation):** Under the locked H-NEW-2280 null (random
  non-adjacent last/first pericope pairing, seed=20260509, 10000 perms), the Q 93 → Q 94 boundary-seam
  Jaccard does **NOT** rank in the top decile of the corpus seam distribution at k=3.
  **Direction lock: percentile-rank(J_seam(Q93→Q94)) ≤ 90th among the 113 real seams (k=3).**

**A success criterion:** A-H1 ∧ A-H2 ∧ A-H3 ∧ A-H4 all hold → Arm A CONFIRMED (scale-dissociation:
whole-surah pairing real, boundary-lexis weak).
**A partial:** 3/4 → DIRECTIONAL.
**A pre-commit violation / NULL:** if rank(Q94)>5 (A-H1 reversed) OR seam-rank>15 (A-H2 reversed) OR
J_seam > corpus mean at either k (A-H3 reversed — boundary lexis is actually STRONG) → published as
NULL with explicit pre-commit-violation flag and full prominence.

## Arm B — the favor→command orphan-recall (DETERMINISTIC + DIRECTION-LOCKED)

**Hypothesis B (pre-committed):** Q 93's body is built as a triadic past-favor block (vv 6-8) answered by
a triadic future-command block (vv 9-11). The structure is lexically realized by a single bridging root —
`ytm` (yatīm, "orphan") — recurring at v 6 (the first favor) and v 9 (the first command), and by the
anaphoric `wjd` (wajadaka, "He found you") unifying the favor block.

- **B-H1 (favor-block anaphora, direction-locked):** the root `wjd` (w-j-d) appears in **all three**
  favor verses (vv 6, 7, 8) and in **no other Q 93 verse**. **Direction lock: count(wjd in Q93) = 3,
  located exactly at vv 6,7,8.**
- **B-H2 (orphan as the unique bridge, direction-locked):** among the roots appearing in the favor block
  {vv 6,7,8}, exactly **one** root also appears in the command block {vv 9,10,11}, and that root is
  `ytm`, bridging v 6 → v 9. **Direction lock: |R(favor-block) ∩ R(command-block)| = 1 and the shared
  root = ytm.**
- **B-H3 (corpus-distinctiveness of the orphan-recall, direction-locked):** the construction in which
  the SAME root that names a recipient of divine favor recurs as the head of a same-surah imperative
  about that recipient — here `ytm` favor (v 6 *wajadaka yatīman fa-āwā*) → `ytm` command (v 9
  *fa-ammā al-yatīma fa-lā taqhar*) — is rare. We count corpus surahs in which `ytm` appears in BOTH a
  declarative-favor context and an adjacent imperative context within the surah. **Direction lock:
  Q 93's favor→command orphan-recall is among the corpus's distinctive `ytm`-recall surahs (the count
  of surahs with `ytm` in ≥2 verses where one is the surah's own command is SMALL — reported as a
  deterministic corpus census; Q 93 is one of them).**

**B success criterion:** B-H1 ∧ B-H2 both hold → Arm B CONFIRMED (deterministic structural fact).
B-H3 is reported as a deterministic corpus census (supporting context), not a gating permutation test.
**B failure:** B-H1 (wjd ≠ 3 or not at vv6-8) OR B-H2 (bridge count ≠ 1 or ≠ ytm) → Arm B NULL.

## Null distributions

- **Null A (Arm A, A-H4):** the H-NEW-2280 locked null — reuse the 114 real last-pericopes and 114 real
  first-pericopes; pair each draw with a random surah `b ≠ a, b ≠ a+1`; compute J; 10000 perms,
  seed=20260509. The corpus seam-mean and per-seam percentile come directly from the 113 real seams.
- **Arm B** is deterministic (corpus census), no permutation null.

## Bonferroni

Arm A has the multi-cell directional family {A-H1, A-H2, A-H3(k=3), A-H3(k=5), A-H4}. A-H4 is the single
permutation/percentile cell; the others are deterministic direction-locks. For the percentile cell the
single-test α = 0.05 is used (no additional permutation multiplicity). Arm B is deterministic. The
surah-session cross-test summary is reported in 06-novel-findings.md.

## MW protections

- **MW-1 (instrument-prior):** FR-rank, TSP-seam-rank, H-NEW-2280 seam-Jaccard, and QAC root-census all
  fixed here before any run.
- **MW-2 (corpus-prior):** Null A uses 10,000 H-NEW-2280-style permutations.
- **MW-3 (alternative-models):** Arm A tests the seam at TWO pericope widths (k=3, k=5); the
  dissociation must hold at both.
- **MW-5 (replication):** A-H1/A-H2/A-H3 and all of Arm B are deterministic and replicable from the
  no-tashkeel JSON + QAC root-index + the cited H-NEW JSON artifacts; A-H4 is seed-locked at 20260509.
- **MW-6 (instrument-control):** Null A's random non-adjacent pairing is the non-target control.
- **MW-7 (post-hoc cap):** both phenomena were close-read-noticed then promoted to direction-locked
  pre-registered tests BEFORE computation; single-test α=0.05 cap respected.

## Verdict mapping

| Arm | Pass condition | Verdict label |
|:--|:--|:--|
| A | A-H1 ∧ A-H2 ∧ A-H3 ∧ A-H4 | CONFIRMED (scale-dissociation) |
| A | 3/4 | DIRECTIONAL |
| A | A-H1 or A-H2 reversed, or A-H3 reversed (boundary lexis STRONG) | NULL (pre-commit violation, full prominence) |
| B | B-H1 ∧ B-H2 | CONFIRMED (deterministic structural fact) |
| B | either fails | NULL |

Final Q093-F-01 verdict = honest combination of Arm A and Arm B, reported with equal NULL prominence.

*Locked 2026-05-30. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm. — Waiel Al-Shujaa.*
