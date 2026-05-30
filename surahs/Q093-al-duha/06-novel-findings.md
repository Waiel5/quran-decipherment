---
surah: 93
surah_name_ar: الضحى
surah_name_translit: al-Ḍuḥā
file_type: novel-findings
date_last_updated: 2026-05-30
phase: B+
verdict: Q093-F-01 — Arm A CONFIRMED (Q93↔Q94 scale-dissociation) + Arm B CONFIRMED (favor→command orphan-recall)
seed: 20260509
n_perm: 10000
---

# Q 93 al-Ḍuḥā — Pre-Registered Novel Findings

One pre-registered two-arm test, run with seed 20260509 and 10,000 permutations, pre-reg SHA-256 locked
before computation and verified at runtime (fail-fast on mismatch).

- **Pre-reg:** `surahs/Q093-al-duha/Q093-F-01-duha-sharh-seam-prereg.md`
- **Pre-reg SHA-256:** `2e384496b1c2e27463135e579918d91f2dc12028276e82f4dc9f08b81be41eed`
- **Script:** `scripts/Q093_F_01_duha_sharh_seam.py` (embeds the SHA as `EXPECTED_SHA`, verifies at
  runtime — printed `SHA OK: 2e384496…b41eed` on the 2026-05-30 re-run)
- **JSON:** `surahs/Q093-al-duha/csv/Q093-F-01.json`
- **Rules-tuple:** `(no-tashkeel, orthographic-token, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

The test was motivated by two close-reading observations promoted to direction-locked hypotheses BEFORE
computation (MW-7): (A) the classically-debated Q 93 ↔ Q 94 single-surah pairing, and (B) the
favor→command triad architecture of the surah body. Both arms passed in the pre-committed direction.

---

## Q093-F-01 Arm A — Q 93 ↔ Q 94 seam scale-dissociation (CONFIRMED)

**Classical anchor.** Ṭāwūs and ʿUmar b. ʿAbd al-ʿAzīz reportedly recited al-Ḍuḥā and al-Sharḥ as *one
surah* in a single rakʿa without an intervening basmala, because Q 94:1 (*alam nashraḥ laka*) reads like a
continuation of Q 93:6 (*alam yajidka yatīman*) — al-Rāzī, *Mafātīḥ al-ghayb*, opening Sūrat al-Sharḥ (on
disk; al-Rāzī himself rejects the identification). The project has instruments at two scales (whole-surah
FR + TSP-seam; boundary-pericope root-Jaccard à la H-NEW-2280). Pre-registered prediction: a
**dissociation** — the pairing is real at the whole-surah scale but weak at the boundary-lexical scale.

**Hypotheses (all direction-locked before computation):**
- **A-H1** Q 94 ∈ Q 93's top-5 FR neighbors.
- **A-H2** Q 93 → Q 94 canonical-adjacency seam ∈ top-15 smoothest of 113.
- **A-H3** boundary-seam root-Jaccard J(Q93→Q94) ≤ corpus mean seam-J at BOTH k=3 and k=5 (dissociation).
- **A-H4** J(Q93→Q94) at k=3 ranks ≤ 90th percentile among the 113 real seams.

**Results (`csv/Q093-F-01.json` → `arm_A`):**

| Cell | Quantity | Value | Pass |
|:--|:--|:--|:--|
| **A-H1** | Q 94 FR rank in Q 93's list | **4 / 113** (FR dist 0.36414) | ✓ (≤5) |
| | (control) Q 92 al-Layl FR rank | 18 / 113 | — |
| | Q 93 mean FR to all 113 | 0.81517 | — |
| **A-H2** | Q 93 → Q 94 TSP seam delta_raw | **−0.01520**, ascending-rank **10 / 113** | ✓ (≤15) |
| **A-H3 (k=3)** | J(Q93→Q94) | **0.0000** vs corpus mean 0.04162 (null 0.03808) | ✓ (≤ mean) |
| **A-H3 (k=5)** | J(Q93→Q94) | **0.0000** vs corpus mean 0.06318 (null 0.05081) | ✓ (≤ mean) |
| **A-H4** | k=3 percentile among 113 real seams | 43.4 (k=5: 24.8) | ✓ (≤90) |

**A passes = 4/4; `pre_commit_violation` = false.**

The close of al-Ḍuḥā (last 3, then 5, verses) and the opening of al-Sharḥ (first 3, then 5, verses) share
**ZERO QAC roots**. The two surahs' only shared root *anywhere* is `rbb` (Lord) — Q 93:3,5,11 vs Q 94:8 —
and it does not fall in either boundary pericope. Yet Q 94 is Q 93's 4th-nearest FR neighbor and the
Q 93 → Q 94 exit-seam is the 10th-smoothest joint in the mushaf.

**Verdict: Arm A CONFIRMED (scale-dissociation).** The classically-claimed Q 93 ↔ Q 94 bond is a
**whole-surah root-distribution effect** (FR rank 4; TSP seam rank 10; corpus pair-rank 128/6441,
`csv/Q093F01-pair-cohesion.json`), NOT a boundary-lexical effect (seam J = 0.0 at both widths). Cohesion
lives at the surah-distribution scale, not the seam-lexis scale — a textbook instance of the
scale-of-aggregation law (cross-finding-025). The pairing is, moreover, **NOT ḥadīth-attested** (no 9-book
narration cites both surahs; `04-hadith-corpus.md` §4): the empirical whole-surah cohesion is an
*independent* corroboration of the scholars' intuition, with no ṣaḥīḥ chain behind it.

---

## Q093-F-01 Arm B — the favor→command orphan-recall (CONFIRMED, deterministic)

**Classical anchor.** Ibn Kathīr (on Q 93:9-11, on disk) reads each future-command as the moral counterpart
of the corresponding past-favor: orphan→do-not-oppress (v 6↔9), lost→do-not-scorn-the-asker (v 7↔10),
poor→proclaim-the-favor (v 8↔11). The pre-registered question: does this triad-answers-triad architecture
leave a *lexical* fingerprint?

**Hypotheses (direction-locked):**
- **B-H1** `wjd` (*wajadaka*) appears in exactly the three favor verses (vv 6, 7, 8) and no other Q 93 verse.
- **B-H2** the favor block {vv 6-8} and command block {vv 9-11} share exactly **one** root, and it is `ytm`.
- **B-H3** corpus census: how many surahs carry `ytm` in ≥2 verses (a same-surah recall)? (reported, not gating)

**Results (`csv/Q093-F-01.json` → `arm_B`):**

| Cell | Quantity | Value | Pass |
|:--|:--|:--|:--|
| **B-H1** | verses with root `wjd` | **[6, 7, 8]** | ✓ (= favor triad, nothing else) |
| **B-H2** | favor∩command root intersection | **{`ytm`}** (size 1) | ✓ (unique bridge = orphan) |
| | favor-block roots (vv 6-8) | {Awy, Dll, Eyl, gny, hdy, wjd, ytm} | — |
| | command-block roots (vv 9-11) | {Hdv, nEm, nhr, qhr, rbb, sAl, ytm} | — |
| **B-H3** | surahs with `ytm` in ≥2 verses | **3** — Q 2 [83,177,215,220], Q 4 [2,3,6,8,10,36,127], **Q 93 [6,9]** | — |
| | total surahs containing `ytm` | 12 | — |

**Verdict: Arm B CONFIRMED (deterministic structural fact).** `wjd` (*wajadaka*) is the three-fold
anaphora unifying the favor triad (vv 6-8, nothing else), and `ytm` (orphan) is the **UNIQUE root bridging
the favor block to the command block** — v 6 (*wajadaka yatīman fa-āwā*) → v 9 (*fa-ammā al-yatīma fa-lā
taqhar*). The other two favor/command pairs Ibn Kathīr names (lost/asker, poor/proclaim) are
positional-thematic with **zero shared root**. The orphan is the surah's single lexical hinge: the only
word that is both the name of a divine favor and the head of a same-surah ethical command. Among the 12
surahs carrying `ytm`, only 3 carry it in ≥2 verses (Q 2, Q 4, Q 93), and Q 93 is the only one realizing a
favor→command recall — the others (Q 2, Q 4) use `ytm` in repeated legal/ethical contexts, not a
favor-then-command arc.

---

## Bonferroni / family summary

Arm A's directional family is {A-H1, A-H2, A-H3(k=3), A-H3(k=5), A-H4}. The deterministic cells
(A-H1, A-H2, A-H3, B-H1, B-H2) consume no α. A-H4 is the single permutation/percentile cell; per the
pre-reg the single-test α = 0.05 applies (no additional permutation multiplicity). Arm B is deterministic.
For the Q 93 surah session Q093-F-01 is the single landed pre-registered test, so no further cross-test
correction is needed.

| Arm / cell | Type | Result | Verdict |
|:--|:--|:--|:--|
| A-H1 | direction-locked | Q 94 FR rank 4/113 | PASS |
| A-H2 | direction-locked | Q93→Q94 seam rank 10/113 | PASS |
| A-H3 (k3, k5) | direction-locked | J = 0.0 ≤ corpus mean both k | PASS |
| A-H4 | permutation/percentile (α=0.05) | k3 pct 43.4 ≤ 90 | PASS |
| **A overall** | — | 4/4, no violation | **CONFIRMED (scale-dissociation)** |
| B-H1 | direction-locked | `wjd` at [6,7,8] only | PASS |
| B-H2 | direction-locked | unique bridge = `ytm` | PASS |
| B-H3 | deterministic census | `ytm` multi-verse in {2,4,93} | (supporting) |
| **B overall** | — | B-H1 ∧ B-H2 | **CONFIRMED** |

## Equal-NULL-prominence note

Both arms passed in the pre-committed direction; there was no direction reversal and no garden-of-forking-
paths shift (the analysis matched the locked pre-reg exactly). Had A-H3 reversed (boundary lexis actually
STRONG) or A-H1/A-H2 reversed, the script would have flagged `pre_commit_violation` and the arm would have
been published as NULL with full prominence. The *honest* NULL embedded inside Arm A's CONFIRMED is the
**boundary-lexical scale itself**: at the seam, the famous pairing is genuinely null (J = 0.0) — the
finding's force is precisely that the cohesion does NOT live where the classical reading (Q 93:6 → Q 94:1)
locates it. The NULL-at-the-boundary is reported with equal prominence to the CONFIRMED-at-the-whole-surah.

## MW protections applied

- **MW-1 (instrument-prior):** FR-rank, TSP-seam-rank, H-NEW-2280 seam-Jaccard, and QAC root-census all
  fixed in the pre-reg before any run.
- **MW-2 (corpus-prior):** A-H4 used the locked H-NEW-2280-style null (10,000 random non-adjacent
  pericope pairings, seed 20260509).
- **MW-3 (alternative-models):** the seam was tested at TWO pericope widths (k=3, k=5); the dissociation
  holds at both (J = 0.0 either way).
- **MW-5 (replication):** A-H1/A-H2/A-H3 and all of Arm B are deterministic and replicable from the
  no-tashkeel JSON + QAC root-index + the cited H-NEW JSON artifacts; A-H4 is seed-locked at 20260509.
  Re-run 2026-05-30 reproduced the JSON byte-for-byte (SHA OK).
- **MW-6 (instrument-control):** A-H4's random non-adjacent pairing is the non-target control; the Q 92
  al-Layl FR rank (18) is the surface-anaphora control showing the oath-frame echo points to a DIFFERENT
  neighbor than the root-distribution bond.
- **MW-7 (post-hoc cap):** both phenomena were close-read-noticed then promoted to direction-locked
  pre-registered tests BEFORE computation; the single-test α=0.05 cap is respected.

## Cross-finding integration

- **cross-finding-025 (formal scale-of-aggregation law)** — Arm A is a new supporting instance: a
  classically-PAIRED unit that is cohesive at the whole-surah-distribution scale (FR rank 4, seam rank 10)
  but lexically NULL at the boundary-pericope scale (J = 0.0). This is the *paired-surah* variant of the
  whole-surah-vs-pericope axis (Q066-F-01 Arm B was the *intra-surah parable-pair* variant).
- **H-NEW-2280 (al-Biqāʿī munāsabah-seam)** — Q 93 → Q 94 is one of the corpus's zero-Jaccard seams
  despite being a smooth whole-surah joint; a sharp instance of the seam-lexical / whole-surah dissociation.
- **H-NEW-111 / H-NEW-720** — Arm A's whole-surah cohesion values are read directly from these locked
  artifacts (Q 94 = 4th FR neighbor; Q 93→Q 94 = rank-10 seamless seam).
- **The orphan-recall (Arm B)** is a candidate corpus-wide structure: the "same root names a divine favor
  AND heads a same-surah command" construction — flagged for a possible corpus-wide H-NEW (a census of
  favor→command lexical recalls across the corpus).

## Honest limits

- Arm A's seam J = 0.0 is on the QAC v0.4 ROOT level; a surface-token or lemma seam metric could register
  the shared *rabbi* (Q 93:11 / Q 94:8) and partially rehabilitate the boundary bond — flagged (and
  consistent with the bidirectional rules-tuple sensitivity in MEMORY), but the dissociation claim is and
  remains ROOT-level (matching H-NEW-2280).
- Arm B's "only the orphan pair is lexically realized" is ROOT-level; the lost/asker and poor/proclaim
  pairs share *thematic* but not *root* material, so a semantic-field instrument would score them as
  related. The deterministic ROOT finding stands.
- The corpus census B-H3 counts `ytm` multi-verse surahs (Q 2, Q 4, Q 93); the *favor→command-recall*
  specialization of Q 93 is a manual reading of those three, not a separate permutation test.
- The supporting artifacts `csv/Q093F01-pair-cohesion.json`, `csv/Q093F02-trio-cohesion.json`,
  `csv/Q093F03-seam-asymmetry.json` (the 2026-05-09 exploratory pair/trio/seam-asymmetry runs) corroborate
  Arm A's whole-surah cohesion at the corpus and mufaṣṣal-pool scales and the Q92|Q93|Q94 seam pattern,
  but are NOT the SHA-locked primary test; only Q093-F-01 (this file) is pre-registered and gating.

---

*Computed 2026-05-30, seed 20260509, 10,000 perms, SHA-locked pre-reg verified at runtime (SHA OK).
Script: `scripts/Q093_F_01_duha_sharh_seam.py`; JSON: `csv/Q093-F-01.json`.*
