---
finding_id: H-NEW-2220
title: Corpus-wide pericope-scale ring-composition sweep — chiastic-pericope generator
file_type: pre-registration
date_registered: 2026-05-29
phase: B+
status: LOCKED-BEFORE-RUN
seed: 20260509
n_perms: 10000
n_perms_refinement: 200000
rules_tuple: (no-tashkeel, QAC-triliteral-root, root-sets, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
extends: cross-finding-025-formal (scale-of-aggregation pericope-flip law), Q002-F-07, H-NEW-2030
---

# H-NEW-2220 — The corpus-wide pericope ring-composition GENERATOR

## 1. Motivation and the gap this closes

Q002-F-07 found **one** statistically-significant ring pericope (Q 2:131–144, the
Abraham/qibla block, ring-Jaccard = 0.25513, z = +3.688, p = 0.010 under a 10,000-perm
within-window verse-order shuffle null; control window Q 2:100–113 NULL at p = 0.285).
H-NEW-2030 had already refuted whole-surah rings (Farrin Q 2, Cuypers Q 5 NOT supported;
corpus mean z = −0.205, surahs are *progressive* not *concentric*). Together these
established the **6th scale-of-aggregation flip** (cross-finding-025-formal): ring
structure NULLs at whole-surah scale and PASSES at the pericope/block scale.

But Q002-F-07 tested exactly ONE pre-named window. The open question is **corpus-wide**:
> Is the Q 2:131–144 ring a near-unique curiosity, or is pericope-scale ring-composition
> a *generalised* feature of the Quran's compositional grammar — present in many surahs,
> concentrated where the literary tradition (refrain-surahs, prophet-cycles, narrative)
> expects it?

This pre-registers a **generator** that slides pericope windows across **every** surah,
scores each for chiastic/ring symmetry against the same proper permutation null Q002-F-07
used, and produces the **corpus-wide roster** of ring-bearing pericopes.

The prior corpus-wide sub-surah scan (`findings/phase-c-structures/chiastic-audit.md` §5)
slid every contiguous 5..15-verse window (family = 57,996 overlapping windows) but used a
**weak null (50 shuffles/window)** with parametric-z extrapolation and an
autocorrelation-inflated family. It found **4 Bonferroni-survivors (z > 4.78)**:
Q 2:131–144 (z=+9.69), Q 54:21–30 (Thamud, z=+6.46), Q 80:1–9 (rebuke, z=+6.09),
Q 18:83–91 (Dhul-Qarnayn, z=+5.19). This generator re-derives the roster with (a) a
proper 10,000-perm permutation null, (b) a non-redundant stride-based family, and
(c) a high-perm Bonferroni refinement.

## 2. Hypotheses (DIRECTION LOCKED — written BEFORE any computation)

### H1 — corpus has MORE rings than the single Q2 case (primary)
Across the pre-registered window grid, **≥ K = 4 pericope windows** clear the
Bonferroni-corrected significance threshold for the family of windows tested.
- **Direction LOCKED: HIGH.** Canonical verse order is more ring-shaped (higher paired
  mirror-Jaccard) than within-window shuffles, for ≥4 windows after family correction.
- **K = 4 baseline derivation (locked):** the chiastic-audit found exactly 4
  Bonferroni-survivors over its (weaker-null, inflated) family. A *proper* permutation
  null on a *non-redundant* family should recover **at least** those same real rings.
  K=4 is therefore the conservative replication floor. ≥4 ⇒ H1 PASS (rings generalise).
- **NULL condition:** < 4 windows survive Bonferroni. If only the Q 2-region window(s)
  survive, the Q 2 ring is **near-unique** — published with full prominence as a NULL for
  generalisation (a corpus with only the one Q2 ring would itself be a substantive finding
  bounding the scale-of-aggregation law's reach).

### H2 — ring pericopes are NOT uniformly distributed (concentration)
Bonferroni-surviving + raw-α=0.05 ring windows **concentrate** in narrative/long surahs,
operationalised two pre-committed ways:
- **H2a (length):** the median surah-length (verse-count N) of ring-bearing surahs is
  **greater** than the corpus median surah-length, tested by a Mann-Whitney one-sided
  comparison of {N of ring-bearing surahs} vs {N of non-ring surahs}. Direction LOCKED:
  ring-bearing surahs are LONGER.
- **H2b (early-mushaf):** ring-bearing surahs concentrate at mushaf positions **s ≤ 50**
  (the ṭiwāl/early block), tested as a one-sided binomial: of the ring-bearing surahs,
  the fraction with s ≤ 50 exceeds the corpus baseline fraction (50/114 = 0.439).
  Direction LOCKED: enriched at s ≤ 50.
- H2 PASS requires **both** H2a (p < 0.05) and H2b (p < 0.05). Either failing ⇒ H2 PARTIAL;
  both failing ⇒ H2 NULL (rings are uniformly scattered).

### H3 — the generator replicates Q002-F-07 exactly (MW-5 self-check, locked)
The window Q 2:131–144 evaluated by this generator's pipeline reproduces Q002-F-07's
ring score 0.25513 (± 1e-4) and z = +3.688 (± 0.05) under seed 20260509 / 10,000 perms.
- **FAIL-FAST condition:** if the generator does NOT reproduce Q002-F-07 within tolerance,
  the pipeline is mis-implemented and the whole run is VOID (not published).

## 3. Metric (MW-1 locked)

For a contiguous window of N verses v_1..v_N with QAC-triliteral-root sets R(v_i):
```
ring(window) = (1/floor(N/2)) * sum_{i=1..floor(N/2)} Jaccard(R(v_i), R(v_{N+1-i}))
Jaccard(A,B) = |A ∩ B| / |A ∪ B|  (0 if both empty)
```
Identical to the chiastic-audit §1 metric and to Q002-F-07's `ring_score`. For odd N the
exact-centre verse is excluded from all pairs (floor(N/2) pairs), which is correct for a
chiasm (the centre is the pivot, not a mirror partner).

Roots are read from `data/morphology/root-index.json` (root → list of [surah, verse, word]),
giving R(v) = set of triliteral roots attested in verse v. (Verses with no QAC root, e.g.
pure muqaṭṭaʿāt or particle-only verses, have R = ∅.)

## 4. Window grid (PRE-REGISTERED, locked)

- **Widths W = {5, 7, 9, 11, 13}** — all ODD, so each window has a clean centre verse
  (chiasm pivot). This spans the pericope band the literary tradition uses (5–13 verses).
- **Stride = ceil(W/2)** per width — ~50% overlap. This is a *non-redundant* sweep that
  covers the whole corpus while sharply reducing the autocorrelation that inflated the
  chiastic-audit's 57,996-window family. Windows start at verse-index 0, step by stride,
  last window right-anchored to surah end.
- Surahs with N < W contribute no windows for that width.
- **Family size F is the exact count of windows actually scored** (computed = 6,165 from
  the locked grid; verified at runtime and embedded in output). Bonferroni uses this F.
- **MW-3 robustness (secondary, not the primary family):** the top ~30 stride-grid hits
  are re-scored under a full **stride-1** sliding scan in their host surah to confirm the
  ring is not a stride-alignment artefact; reported but NOT added to the Bonferroni family.

## 5. Null model & significance (MW-2)

- **Primary null (protocol-locked):** within-window verse-order permutation — shuffle the
  N root-sets of the window, recompute ring(), 10,000 times, seed = 20260509 (a fresh
  `random.Random(20260509)` re-seeded per window so the run is order-independent and
  fully reproducible). One-sided empirical p = (#shuffles ≥ obs + 1)/(10,000 + 1).
  Permutation z = (obs − mean_null)/sd_null.
- **Raw-α roster (the task's literal ask):** a window is a *candidate ring* if it beats the
  **95th percentile of its shuffles** (empirical p < 0.05). Under the global null the
  expected count is 0.05 × F ≈ **308** windows — so the raw roster is NOT itself evidence;
  it is the candidate pool. Enrichment of the raw roster over 308 is reported descriptively.
- **Bonferroni family correction:** α_bonferroni = 0.05 / F = 0.05/6165 = **8.11×10⁻⁶**.
  The 10,000-perm empirical p-floor is 1/(10,001) = 9.999×10⁻⁵ **> α_bonferroni**, so an
  empirical p alone **cannot** clear Bonferroni at 10k perms. Two pre-committed resolutions:
  1. **Gaussian-tail Bonferroni (matches the chiastic-audit convention):** a window is a
     **Bonferroni-survivor** if its permutation z exceeds the Gaussian threshold for
     α_bonferroni over family F: **z > 4.311** (one-sided). This is the H1 decision rule.
  2. **High-perm empirical refinement (MW-2 strengthening):** every window with z > 4.311
     (and every window with raw empirical p = p-floor) is re-run at **200,000 perms**
     (seed 20260509) so its empirical p can actually reach α_bonferroni; a window is a
     **confirmed empirical Bonferroni-survivor** if its 200k-perm p < 8.11×10⁻⁶.
  H1 is adjudicated on rule (1) (Gaussian-z, family-corrected, replicating the audit's
  convention); rule (2) is the corroborating empirical confirmation.

## 6. MW protections

- **MW-1:** ring metric + window grid + null all locked above, pre-run.
- **MW-2:** 10,000-perm primary null (200× the audit's 50); 200,000-perm refinement for
  the survivor sub-roster.
- **MW-3:** stride-grid (primary) vs stride-1 sliding (robustness) on the top hits;
  both odd-width grid AND the audit's reported windows checked.
- **MW-5:** H3 is an explicit cross-pipeline replication of Q002-F-07 (fail-fast).
- **MW-6 (instrument-control):** a **per-width random-window control** — for each width,
  draw the SAME number of windows from random surah+start positions and report their
  raw-roster rate; it must be ≈ 0.05 (calibration check that the null is well-formed).
  Additionally, the centre-verse exclusion is verified by construction.
- **MW-7:** any window NOT in the chiastic-audit's known set that survives Bonferroni is
  treated as post-hoc-noticed and held to the z > 4.311 family-corrected bar (already the
  H1 rule), with the 200k-perm empirical confirmation required before any strong claim.

## 7. Failure / NULL conditions (equal prominence)

- **H1 NULL:** < 4 Bonferroni-survivors. If only Q 2-region survives ⇒ "Q 2 ring is
  near-unique"; published with full prominence.
- **H2 NULL:** ring-bearing surahs neither longer (H2a fails) nor early-concentrated
  (H2b fails) ⇒ rings are uniformly scattered.
- **H3 FAIL:** Q 2:131–144 not reproduced ⇒ run VOID, nothing published.
- **Pre-commit violation:** if any observed effect runs *opposite* to a LOCKED direction
  (e.g. ring-bearing surahs are SHORTER, or LATE-concentrated), it is published as NULL
  with an explicit pre-commit-violation flag — never massaged.

## 8. Relation to the scale-of-aggregation law (cross-finding-025-formal)

If H1 PASSES with ≥4 generalised rings, this is the **7th-and-beyond evidence** for the
pericope-flip law: it shows the Q 2:131–144 flip (NULL whole-surah → PASS pericope) is not
a one-off but the visible tip of a corpus-wide regularity — content structure is
**pericope-scoped, not surah-scoped**. If H1 is NULL (near-unique Q 2 ring), it BOUNDS the
law: ring-composition flips for Q 2 specifically but does not generalise, which would be a
genuine limit on the law's structural-rhetorical arm. Either verdict is a first-class
finding; the direction is locked before observation.

## 9. Honesty notes

- The metric detects **lexical** mirror-symmetry (shared roots across mirror positions).
  It will preferentially flag **refrain-driven** inclusios (Q 54, Q 55, Q 77) where an
  identical refrain bookends a unit — this is real ring/inclusio structure but is
  *structural* more than strict semantic chiasmus. The roster will label refrain-anchored
  vs root-thematic rings descriptively; the statistic does not distinguish them and we do
  not claim it does.
- A high raw-roster count (≈300+) is the NULL expectation, not a result. Only the
  Bonferroni layer carries the H1 verdict.
- This is a content-root test; it neither confirms nor refutes the *interpretive*
  thematic-chiasm readings of Farrin/Cuypers (which, per Sinai 2017, are not falsifiable
  as posed). It tests the falsifiable lexical-mirroring form.

*Direction locked 2026-05-29 by Waiel Al-Shujaa, before any computation. Seed 20260509.
Bismillāhi al-Raḥmāni al-Raḥīm.*
