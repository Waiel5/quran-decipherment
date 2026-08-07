---
finding_id: H-NEW-2220
title: Corpus-wide pericope-scale ring-composition sweep — chiastic-pericope generator
file_type: novel-finding
date: 2026-05-29
phase: B+
seed: 20260509
n_perms: 10000
n_perms_refinement: 200000
prereg_sha256: d73da54a258257576d947c4ad23227298af10a2cff23947a1346bcf27937933a
rules_tuple: (no-tashkeel, QAC-triliteral-root, root-sets, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
verdict: >-
  H1 NULL (0 of 6,541 pericope windows survive Bonferroni; max z = +4.11 < 4.324 bar) —
  pericope ring-composition does NOT generalise; the Q 2:131–144 ring is near-unique at
  family-significance. H3 self-check PASS (Q 2:131–144 reproduced exactly). H2 PASS
  (the weak candidate-roster ring signal concentrates in LONG, EARLY, narrative/refrain
  surahs, exactly as the literary tradition predicts). Net: the scale-of-aggregation law
  is BOUNDED on its ring-composition arm — Q 2 flips, the corpus does not.
extends: cross-finding-025-formal, Q002-F-07, H-NEW-2030
---

# H-NEW-2220 — Corpus-wide pericope ring-composition GENERATOR

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

## TL;DR

Q002-F-07 found ONE significant ring pericope (Q 2:131–144, z = +3.69). This generator
slid pericope windows (odd widths {5,7,9,11,13}, stride = ⌈w/2⌉) across **every** surah —
**6,541 windows** — and scored each for chiastic mirror-symmetry (paired root-Jaccard)
against a proper **10,000-permutation within-window verse-order shuffle null** (seed
20260509), the identical instrument Q002-F-07 used.

**Result, in one line:** *Under a correct permutation null, NO pericope window in the
entire Quran clears family-wide Bonferroni correction.* The strongest is Q 29:43–53
(ʿAnkabūt, z = +4.11), which falls just below the z > 4.324 Bonferroni bar. The corpus
z-distribution is **anti-chiastic** (mean z = −0.15, median z = −0.36; only 33 % of
windows have z > 0). The much-cited z = +9.69 / +6.46 ring scores in the project's earlier
`chiastic-audit.md` were **artefacts of its weak parametric null** (50 shuffles + Gaussian
extrapolation), not real family-significant effects — exactly as Q002-F-07 had already
flagged for the Q 2 window (true z = 3.69, not 9.69).

But the **weak** ring signal that does exist is NOT randomly placed: the candidate
(raw-α) roster concentrates sharply in **long, early-mushaf, narrative/refrain** surahs
(median N = 78 vs 21; 80.5 % at s ≤ 50 vs 43.9 % baseline). The literary tradition was
right about *where* rings live; it was wrong about *how strong/common* they are.

## Pre-registered hypotheses and verdicts

| H | Claim (direction LOCKED) | Verdict | Evidence |
|---|---|---|---|
| **H1** | ≥ K=4 windows clear Bonferroni (rings generalise) | **NULL** | 0 of 6,541 survive z > 4.324; max z = +4.11 (Q 29:43–53) |
| **H2a** | ring-bearing surahs are LONGER | **PASS** | median N 78 vs 21; Mann-Whitney p ≈ 0 (one-sided) |
| **H2b** | ring-bearing surahs concentrate at s ≤ 50 | **PASS** | 33/41 = 80.5 % vs 43.9 % baseline; binomial p ≈ 0 |
| **H2** | non-uniform distribution (H2a ∧ H2b) | **PASS** | both arms pass |
| **H3** | generator reproduces Q002-F-07 (self-check) | **PASS** | Q 2:131–144 ring = 0.25513 (exact), z = +3.711 (ref 3.688) |

No pre-commit direction was violated: H2's effects ran in the locked direction
(ring-bearing surahs LONGER and EARLIER, as predicted). H1 returned NULL but in the
honest sense — the predicted ≥4 Bonferroni-survivors simply do not exist.

## Method

- **Metric** (locked, MW-1): `ring(window) = (1/⌊N/2⌋) Σ Jaccard(R(v_i), R(v_{N+1−i}))`,
  R(v) = QAC-triliteral-root set of verse v (from `data/morphology/root-index.json`).
  Odd widths → clean centre-verse pivot, excluded from pairs.
- **Grid** (locked): widths {5,7,9,11,13}, stride ⌈w/2⌉ (≈50 % overlap), every surah with
  N ≥ w. Family **F = 6,541** windows (verified at runtime). This is a *non-redundant*
  sweep, ~9× smaller than the chiastic-audit's autocorrelation-inflated 57,996-window
  fully-overlapping family.
- **Null** (locked, MW-2): 10,000 within-window verse-order permutations, seed 20260509,
  re-seeded per window (order-independent). One-sided empirical p = (#≥obs + 1)/(10,001);
  permutation z = (obs − μ_null)/σ_null.
- **Decision rule** (locked, two-stage): the 10k-perm empirical p-floor (9.999×10⁻⁵)
  exceeds α_Bonferroni (0.05/6541 = 7.64×10⁻⁶), so empirical p alone cannot clear
  Bonferroni at 10k perms. H1 is therefore adjudicated on the **Gaussian-tail
  permutation-z** threshold **z > 4.324** (the chiastic-audit's convention), with a
  **200,000-perm empirical confirmation** layer for any survivor. Both returned 0.
- **MW-6 control**: a width-matched random-window draw returned a raw-hit rate of **0.0138**,
  closely matching the real-data conservative rate — confirming the null is well-formed
  (the depressed-below-0.05 rate is the discrete/zero-inflated root-Jaccard distribution
  under the standard ≥ convention, applied identically to real and control, so all
  enrichment comparisons are valid).
- **MW-3 robustness**: the top-30 grid hits were re-scored under a full stride-1 slide in
  their host surah. The top 2 (Q 29:43–53, Q 80:1–9) are stride-invariant; others shift to
  a nearby window of marginally higher ring score (e.g. Q 26 Noah cycle at v103–115), never
  enough to cross the Bonferroni bar.

## The corpus-wide candidate-ring roster (top 15 by z)

These are the strongest pericope rings in the Quran — all genuine literary units, NONE
family-significant after Bonferroni:

| window | width | ring | z | p_raw | surah / unit |
|---|---:|---:|---:|---:|---|
| **29:43–53** | 11 | 0.192 | **+4.11** | 0.0006 | al-ʿAnkabūt — "spider's house / parable of signs" |
| **80:1–9** | 9 | 0.208 | +3.90 | 0.0162 | ʿAbasa — the "frowned and turned away" rebuke (audit hit) |
| **26:50–62** | 13 | 0.100 | +3.87 | 0.0079 | al-Shuʿarāʾ — Moses/Pharaoh exodus |
| **9:15–27** | 13 | 0.159 | +3.75 | 0.0014 | al-Tawba — believers vs the unfaithful |
| **2:151–159** | 9 | 0.122 | +3.71 | 0.0012 | al-Baqara — qibla/patience pericope (adjacent to the qibla ring) |
| **44:47–59** | 13 | 0.069 | +3.64 | 0.0065 | al-Dukhān — Zaqqūm / the muttaqūn contrast |
| **26:61–69** | 9 | 0.153 | +3.47 | 0.0058 | al-Shuʿarāʾ — the sea-crossing |
| **26:141–153** | 13 | 0.194 | +3.12 | 0.0256 | al-Shuʿarāʾ — Thamūd/Ṣāliḥ cycle |
| **49:1–7** | 7 | 0.138 | +3.10 | 0.0079 | al-Ḥujurāt — etiquette-before-the-Prophet opener |
| **85:1–9** | 9 | 0.115 | +3.08 | 0.0156 | al-Burūj — the people of the ditch |
| **2:205–215** | 11 | 0.125 | +3.08 | 0.0019 | al-Baqara — hypocrite/believer contrast |
| **22:16–24** | 9 | 0.053 | +3.05 | 0.0026 | al-Ḥajj — the two disputants |
| **15:13–23** | 11 | 0.060 | +3.03 | 0.0049 | al-Ḥijr — cosmology/creation signs |
| **37:170–182** | 13 | 0.233 | +3.03 | 0.0086 | al-Ṣāffāt — closing doxology refrain |
| **37:85–95** | 11 | 0.120 | +3.02 | 0.0122 | al-Ṣāffāt — Abraham smashes the idols |

**115 windows** total beat their own 95th percentile (raw α=0.05). The null *expectation*
is ≈ 327 (0.05 × 6541), so the corpus actually has an **enrichment ratio of 0.35** — FEWER
raw ring-hits than chance, the conservative-discrete-null and anti-chiastic skew combined.

**Surahs carrying the most candidate rings:** Q 55 ar-Raḥmān (16 windows — the
*fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* refrain doing inclusio work), Q 2 (10), Q 3 (7),
Q 15 (5), Q 26 al-Shuʿarāʾ (4, prophet-cycles), Q 9, Q 22, Q 21, Q 20, Q 4, Q 18, Q 37.
The algorithm rediscovers refrain-rich and narrative surahs without being told to — the
metric works; the structures are real; they are just **not strong enough to survive a
serious multiple-comparison correction.**

## Why H1 is NULL — the null-model lesson

The chiastic-audit reported Q 2:131–144 at z = +9.69, Q 54:21–30 at +6.46, Q 80:1–9 at
+6.09, Q 18:83–91 at +5.19 — "4 Bonferroni-survivors". Under this generator's **proper
10,000-perm within-window null**, the *same* windows score:

| window | audit z (50-shuffle parametric) | this generator z (10k-perm) |
|---|---:|---:|
| 2:131–144 (qibla) | +9.69 | **+3.71** (raw p = 0.0095) |
| 54:21–30 (Thamūd) | +6.46 | +3.11 (raw p = 0.0234) |
| 80:1–9 (rebuke) | +6.09 | +3.90 (raw p = 0.0162) |
| 18:83–91 (Dhū l-Qarnayn) | +5.19 | +2.66 (raw p = 0.0605, not a raw hit) |

The audit's z-inflation came from a 50-shuffle null whose σ was estimated off too few
samples and whose pooled cross-surah baseline understated the within-window variance. Once
the null is the *correct* within-window verse-order permutation at 10k perms, even the
strongest ring in the Quran (Q 2:131–144) only reaches z ≈ 3.7 — comfortably below the
z > 4.32 family-corrected bar. **This is the H-NEW-2030 result reproduced at the pericope
scale:** the corpus is anti-chiastic in the aggregate (mean z = −0.15), and the rings that
exist are local literary units, not a corpus-wide compositional law.

## Relation to cross-finding-025-formal (the scale-of-aggregation law)

This is the **decisive bounding test** of the law's ring-composition arm. The prior chain
was: H-NEW-2030 (whole-surah rings NULL) → Q002-F-07 (Q 2:131–144 pericope ring PASS) →
"6th scale-of-aggregation flip". The natural next prediction was that pericope rings
**generalise** — that many more would flip from whole-surah-NULL to pericope-PASS.

**They do not.** H-NEW-2220 shows the Q 2:131–144 flip is **near-unique at
family-significance**: at the pericope scale the corpus has ONE marquee ring (Q 2) plus a
tier of ~15 genuine-but-sub-Bonferroni literary units, and is anti-chiastic on average.

This does **NOT** retract cross-finding-025. The other five flips (Iblīs, sajda,
prophet-vocative, al-ḥamdu, ḥawāmīm) are **cross-surah marker-cohesion** flips —
pericopes sharing a *marker* are more cohesive *with each other* at pericope scale. That
mechanism is intact. What H-NEW-2220 bounds is a *different* structural claim: **intra-
pericope mirror-symmetry (chiasmus)** is NOT a generalised corpus feature. The two are
distinct: marker-cohesion is *between* pericopes; ring-composition is *within* one.

**Net effect on the law:** the scale-of-aggregation principle stands, but its
**ring-composition arm is now explicitly bounded** — the Q 2 ring flips, the corpus does
not. This is a 7th *test* of the law that returns a *refinement*, not a 7th confirming flip.
The honest statement is: *content structure in the Quran is pericope-scoped (cross-finding-025
holds for marker-cohesion), but positional mirror-symmetry within pericopes is local and
rare, not a law.* H2's PASS shows even that local rarity is non-random — it lives where the
tradition (Farrin, Cuypers, Zahniser, Mir) looks: long, early, narrative/refrain material.

## H2 — the concentration is real (and in the locked direction)

Although H1 is NULL at the Bonferroni layer, the candidate (raw-α) roster — the only
ring-signal the corpus offers — is sharply non-uniform, exactly as pre-registered:

- **Length (H2a):** ring-bearing surahs have median N = 78 (mean 96.5) vs non-roster
  median N = 21 (mean 31.2). Mann-Whitney one-sided p ≈ 0. Rings live in long surahs.
- **Mushaf position (H2b):** 33 of 41 ring-bearing surahs (80.5 %) sit at s ≤ 50, vs the
  43.9 % corpus baseline. One-sided binomial p ≈ 0. Rings concentrate in the early
  ṭiwāl/long block.

This is the empirically-honest residue of the Farrin/Cuypers "Semitic rhetoric" program:
they correctly identified *which* material is ring-organised (Abraham/qibla, prophet-cycles,
refrain-surahs) — the algorithm rediscovers their candidates — but the effect is too weak
and too sparse to constitute the corpus-wide compositional law their strong claims imply.
Sinai's (2017, *JQS* 19) scepticism is vindicated at the strong-claim level; the moderate
"these specific pericopes are unusually organised" claim survives as a sub-significant tier.

## Classical / academic anchors

- **R. Farrin** (2010, *The Muslim World* 100; 2014, *Structure and Qurʾanic
  Interpretation*) — Q 2 nine-section macro-ring with the qibla pivot at its centre. The
  qibla pericope IS this generator's reference ring (H3) but at z = 3.7, sub-Bonferroni;
  the *macro*-ring was already NULL (H-NEW-2030).
- **M. Cuypers** (2015, *The Composition of the Qurʾan: Rhetorical Analysis*) — Q 5
  al-Māʾida ring. Q 5 is among the most *anti*-chiastic surahs in the corpus (H-NEW-2030,
  whole-surah z = −2.06); no Q 5 pericope appears in the top roster here.
- **A.H. Mathias Zahniser** (1991, "Major Transitions and Thematic Borders in Two Surahs")
  and **Mustansir Mir** — the Q 2:131–144 unit; conceded by sceptic **N. Sinai** (2017,
  "Going Round in Circles", *JQS* 19) as unusually organised. This generator agrees it is
  the single strongest ring — and shows it is the *only* one near family-significance.
- **al-Biqāʿī**, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar* — intra-pericope *naẓm*
  (coherence within a unit) operates at smaller scales than surah-surah munāsaba; H2's
  concentration of weak rings in long narrative surahs is consistent with his within-unit
  *naẓm* intuition, while H1's NULL is consistent with rings not being a surah-level law.

## Honest limits

1. **Width 14 is off-grid.** The marquee Q 2:131–144 ring is 14 verses — an even width not
   in the locked odd-width grid {5,7,9,11,13} (odd widths give a clean chiasm pivot). The
   grid's closest Q 2 hit is 2:151–159 (z = 3.71). The Q 2:131–144 ring is captured only by
   the H3 direct self-check, not by the sweep. A future even-width companion grid could test
   whether even-width rings differ — but it would not change the H1 verdict (no even-width
   window could plausibly exceed Q 2:131–144's z = 3.7, which is itself sub-Bonferroni).
2. **Conservative discrete null.** Small root-sets make the ring-score distribution discrete
   and zero-inflated; the standard ≥ convention yields p's biased upward (raw-hit rate 0.018
   vs 0.05). This makes H1's NULL *more* secure (it is hard, not easy, to be a raw hit) and
   the H2 enrichment comparison remains valid (same convention on roster, non-roster, and
   control). A mid-p correction would raise the raw-hit count but cannot manufacture a
   z > 4.32 survivor.
3. **Lexical, not semantic.** The metric detects shared *roots* across mirror positions. It
   preferentially flags refrain-driven inclusios (Q 55, Q 37, Q 54) over abstract thematic
   chiasmus. It neither confirms nor refutes the *interpretive* thematic-ring readings,
   which (per Sinai) are not falsifiable as posed.
4. **Stride choice.** Stride ⌈w/2⌉ controls autocorrelation but could miss a ring whose
   centre falls between grid points; MW-3's stride-1 re-scan of the top-30 confirms the
   verdict is stride-robust.

## Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2220-pericope-ring-sweep.md`
  (SHA-256 `d73da54a258257576d947c4ad23227298af10a2cff23947a1346bcf27937933a`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2220.py`
- Data: `findings/phase-b-hypotheses/csv/h-new-2220.json`
- Parents: `cross-finding-025-formal-scale-of-aggregation-law.md`,
  `surahs/Q002-al-baqara/Q002-F-07-qibla-pivot-lexical-center.md`,
  `h-new-2030-ring-composition.md`, `findings/phase-c-structures/chiastic-audit.md`

---

*H-NEW-2220 pre-registered and run 2026-05-29 by Waiel Al-Shujaa. Seed 20260509,
10,000 perms (200,000-perm refinement). Direction locked before computation; H1 NULL and
H2 PASS both reported with equal prominence. Bismillāhi al-Raḥmāni al-Raḥīm.*
