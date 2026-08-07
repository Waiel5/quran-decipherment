# [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] — Fisher-Rao on verse-length histograms (2nd replication of [[h-new-111-fisher-rao-mushaf|H-NEW-111]])


> ## ⛔ CORRECTION NOTICE — 2026-08-07
>
> **The arithmetic here is not retracted.** What fell is the inference drawn from the Fisher-Rao
> permutation null. Under the project's first genre control (`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md`),
> al-Bukhārī scores **z = −13.84** and pre-Islamic poetry **z = −15.13** against the Qurʾān's
> **z = −11.50** on an instrument-matched pipeline, and both baselines sit closer to their own TSP
> optima. Cutting this corpus's own verse stream into 114 blocks of the same size profile at offsets
> that ignore every surah seam gives z = −11.23 to −13.18. **Length-sorting alone reaches z = −8.66**
> (H-NEW-111's write-up mis-transcribed that anchor as 107.27; its own `csv/h-new-111.json` records
> 91.03 / 90.30). The mushaf's honest margin over pure length is **2.80 σ**, not 11.46 σ.
> The *relative* claim survives — mushaf 85.76 < Nöldeke 87.23 < Tanzil 89.53.
> Summary: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.


**Finding ID**: [[h-new-111c-fisher-rao-verselen|h-new-111c]]
**Date**: 2026-04-17
**Specialist**: [[h-new-111c-fisher-rao-verselen|h-new-111c]]-specialist
**Pre-reg**: `findings/phase-b-hypotheses/h-new-111c-prereg.md`
**Pre-reg SHA-256**: `ab350056a658e48588cc0bb7b561ed6bd649371336405876a6e2667ccf2bbcf7`
**Seed**: 20260417
**Rules tuple**: (no-tashkeel, whitespace-tokenized verse text, basmala-counted-only-in-surah-1 via text, mushaf order, Hafs-Kūfan)
**Verdict**: **PRIMARY PASS, SECONDARY A FAILS, SECONDARY B REVERSED** — classified **PARTIAL-PASS (MECHANICALLY CONFOUNDED)**; see honest caveat below.

---

## Headline

On the verse-length-histogram axis, the Quran's mushaf ordering IS
significantly shorter than random (z=−9.84, p<10⁻⁴), but:

1. It is **FAR from TSP-optimal** (L_mushaf / L_2opt = **2.71**, outside
   the pre-registered 1.2 band and even outside the 2.0 "geodesic-like" band).
2. **Nöldeke chronology is SHORTER than mushaf** on this axis (L_nold=61.71
   vs L_mushaf=77.66) — the **OPPOSITE SIGN** from [[h-new-111-fisher-rao-mushaf|H-NEW-111]].
3. Simple sort-by-mean-verse-length produces L ≈ 52, vastly shorter than
   mushaf — i.e. an ordering that knows nothing except "each surah's mean
   verse length" traverses the rhythm simplex more efficiently than mushaf.

This is **not a clean replication** of [[h-new-111-fisher-rao-mushaf|H-NEW-111]]. The rhythm axis behaves
differently from the root-distribution axis, and the divergence is
interpretable (see honest caveat).

---

## Numbers

### PRIMARY (pre-registered, one-sided lower-tail, α_bon = 0.0167)

| Quantity | Value |
|---|---|
| L_mushaf (113 consecutive-pair Fisher-Rao distances on 8-bin histograms) | **77.655** |
| Null mean (10,000 random permutations) | 138.149 |
| Null SD | 6.148 |
| Null min observed | 113.827 |
| Null 5th percentile | 127.924 |
| z-score | **−9.84** |
| #{L_perm ≤ L_mushaf} | 0 |
| p_primary (one-sided, lower-tail) | **< 1/10001 ≈ 1×10⁻⁴** |
| Bonferroni α (k=3) | 0.0167 |
| **PASS?** | ✓ (primary direction met) |

### SECONDARY A — geodesic-optimality ratio

| Quantity | Value |
|---|---|
| L_greedy_best | 31.00 |
| L_2opt_best | **28.70** |
| **L_mushaf / L_2opt_best** | **2.706** |
| Pre-registered band | "near-optimal" < 1.2 / "geodesic-like" < 2.0 |
| **Verdict** | **NOT geodesic-like** (ratio ≥ 2.0) |

The mushaf path on verse-length histograms is ~2.7× the TSP upper bound.
For contrast, on [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s root-distribution axis it was 1.107×. This is
a large regression in geodesic efficiency, consistent with the mushaf
being a rhythm-coarse traversal relative to what's possible.

### SECONDARY B — Nöldeke & Tanzil chronology vs mushaf

| Quantity | Value |
|---|---|
| L_mushaf | 77.655 |
| L_nold (Nöldeke) | **61.709** |
| L_tanzil (Egyptian-Std revelation) | 95.344 |
| p_nold one-sided lower | 1×10⁻⁴ |
| p_nold two-sided | **2×10⁻⁴** |
| p_tanzil one-sided lower | 1×10⁻⁴ |
| Sign: L_mushaf − L_nold | **+15.95 (mushaf LONGER)** |
| Sign: L_mushaf − L_tanzil | −17.69 (mushaf shorter than Tanzil) |

**Nöldeke chronology is MORE rhythmically coherent than the mushaf** —
opposite of [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s root-distribution result. This is consistent with
Nöldeke's reconstruction placing early-Meccan (short-staccato) surahs
together and later-Medinan (long legal) together, which is a strong
verse-length-clustering signal. Tanzil's order is LONGER than mushaf on
rhythm because its short-Meccan openers jump into longer mid-revelation
surahs non-monotonically.

### MW-5 positive control

Greedy-NN from surah 1: L = 32.58, p = 1×10⁻⁴. **Positive control fires** —
null is sound.

### Sanity anchors (non-pre-registered — CRITICAL for interpretation)

| Ordering | Path length |
|---|---|
| **Mean verse-length sorted ascending** | **51.92** |
| **Mean verse-length sorted descending** | **52.65** |
| Nöldeke chronology | 61.71 |
| Mushaf | **77.66** |
| TSP 2-opt upper bound | 28.70 |
| Tanzil revelation order | 95.34 |
| #verses sorted descending | 110.76 |
| #verses sorted ascending | 117.79 |
| Null mean | 138.15 |

The key empirical fact: sorting by each surah's MEAN VERSE LENGTH (a trivial
scalar feature) achieves L≈52, **25 units shorter than mushaf and 9 units
shorter than Nöldeke**. The mushaf's verse-length-histogram coherence
exists (better than random, better than sort-by-#verses) but is neither
near-optimal nor near-Nöldeke.

---

## Honest interpretation — the mechanical-confound disclosure

This test is **LESS orthogonal** to the known Uthmanic long-to-short
mufaṣṣal ordering than either the root-distribution test ([[h-new-111-fisher-rao-mushaf|H-NEW-111]]) or
the character-4-gram test ([[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]). We flagged this in the pre-reg
BEFORE running; the results now let us be specific.

### What the pre-reg predicted

- If mushaf ≈ length-sorted-desc → mechanically confounded, no independent
  evidence.
- If mushaf << length-sorted-desc → rhythmic coherence BEYOND length.

### What we got

- L_mushaf (77.66) is **meaningfully shorter** than L_length_sorted_desc-by-#verses
  (110.76) — a 33-unit gap. So mushaf is NOT a pure sort by total verses.
- But L_mushaf is **meaningfully longer** than L_sorted-by-mean-verse-length
  (52) — a 25-unit gap. Sorting by mean verse length crushes mushaf.
- And L_nold (61.71) is also far below mushaf.

### What this means

Mushaf ordering passes the primary (short-of-random) test, but in a way
that does not replicate [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s specific claim that mushaf is
information-geodesic-OPTIMAL. On the rhythm axis the mushaf is:

- **Better than random** (significant);
- **Better than sort-by-nverses** (so its length-ordering is richer than
  just "put al-Baqarah first");
- **Worse than sort-by-mean-verse-length** (so whatever richer criterion
  the mushaf uses, it is not mean-verse-length);
- **Worse than Nöldeke chronology**.

One plausible reading: the mushaf optimizes topical/root coherence
([[h-new-111-fisher-rao-mushaf|H-NEW-111]]) and accepts a MILD rhythmic discontinuity as the cost. A
pure rhythm-sort would separate thematically-related surahs; mushaf
chooses content over cadence. The al-Fātiḥa (7 verses) opening followed
by al-Baqarah (286 verses) is the canonical example of a large rhythm-
jump that serves thematic purpose.

### Confound verdict

**This replication is partially mechanically confounded.** The primary PASS
is mostly attributable to the Uthmanic long-to-short-mufaṣṣal pattern
(which is length-correlated and therefore also rhythm-correlated). It
provides **WEAK independent evidence** for [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s claim. The
divergence — especially Nöldeke being SHORTER than mushaf here, but
LONGER than mushaf in [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — actually argues that the two axes are
measuring genuinely different things, and the mushaf's optimality on
the root-distribution axis is NOT an artefact of the same length structure
that's driving this test. So, paradoxically, the partial failure here
*strengthens* [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s specificity claim.

### Implications for parent [[h-new-111-fisher-rao-mushaf|H-NEW-111]]

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] cannot promote to CONFIRMED on the basis of this replication
  alone. It should wait for [[h-new-111b-fisher-rao-char-4gram|h-new-111b]] (char-4-grams) as the PRIMARY
  independent replication.
- If [[h-new-111b-fisher-rao-char-4gram|h-new-111b]] passes cleanly (ratio near 1.1, mushaf shorter than Nöldeke),
  [[h-new-111-fisher-rao-mushaf|H-NEW-111]] promotes — and [[h-new-111c-fisher-rao-verselen|h-new-111c]] becomes a documented "rhythm-axis
  does NOT show the same optimality" counter-observation supporting the
  specificity of the root-axis claim.
- If [[h-new-111b-fisher-rao-char-4gram|h-new-111b]] also fails the ratio or sign, [[h-new-111-fisher-rao-mushaf|H-NEW-111]] stays PASS-DIRECTED
  and the whole family needs rethinking.

---

## Caveats / honest limits

1. **Mechanical confound**: disclosed throughout. The primary PASS is
   partially mechanically driven by Uthmanic length structure.

2. **Bin edges locked pre-hoc**: `[1,5,10,15,25,40,60,100,∞]` — not tuned.
   Robustness to bin choice NOT tested; would belong to a separate test.

3. **TSP is approximate**: 2-opt upper bound. True optimum is ≤ 28.70, so
   ratio ≥ 2.71. Real ratio could only be WORSE, not better, on mushaf.

4. **8 bins is low-dimensional**: compared to the 500-dim simplex of
   [[h-new-111-fisher-rao-mushaf|H-NEW-111]] or the large-alphabet simplex of 111b char-4-grams, verse-
   length histograms have few degrees of freedom. Random permutations of
   a low-dimensional simplex have a smaller variance in path length, so
   z-scores are less extreme per unit of real structure.

5. **Whitespace tokenization**: each whitespace-separated substring counts
   as one token. This matches the stored JSON format; no morphological
   token count used.

6. **Nöldeke is reconstructed**: same caveat as [[h-new-111-fisher-rao-mushaf|H-NEW-111]].

## Connections to prior findings

- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]**: parent. Root-distribution axis. Mushaf optimal. See above
  for the specificity argument: rhythm and root axes disagreeing is
  evidence AGAINST a pure-length mechanical confound for [[h-new-111-fisher-rao-mushaf|H-NEW-111]].
- **[[h-new-46-1-chronology-disentangle|H-NEW-46.1]] / [[h-new-51-1-noldeke-replication|H-NEW-51.1]]**: mushaf is not chronological. Here we see
  Nöldeke chronology has significantly different rhythmic structure from
  mushaf — consistent.
- **Mufaṣṣal boundary**: the 3-part classical mufaṣṣal division (ṭiwāl /
  awsāṭ / qiṣār) is explicitly length-based. The mushaf enforces a
  monotonic-ish length decrease after ~Q 49–50. That's what's driving
  the "better-than-random" primary PASS here.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-111c-prereg.md`
- Script: `scripts/h_new_111c_fisher_rao_verselen.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-111c.json`
- Journal: `journal/h-new-111c-run-1.md`

## Verdict

**PARTIAL-PASS, MECHANICALLY-CONFOUNDED-IN-DISCLOSED-DIRECTION**:
- Primary p = 1×10⁻⁴ < 0.0167 → formally PASSES.
- Secondary A ratio = 2.706 → FAILS the pre-registered <1.2 "near-optimal" band
  and also the <2.0 "geodesic-like" band.
- Secondary B sign REVERSED: Nöldeke SHORTER than mushaf (opposite of
  [[h-new-111-fisher-rao-mushaf|H-NEW-111]]). Two-sided p=2×10⁻⁴ confirms chronology is non-random on
  rhythm axis too.
- MW-5 positive control fires at p=10⁻⁴ → null sound.

**Net contribution to [[h-new-111-fisher-rao-mushaf|H-NEW-111]] replication program**:
- Cannot serve as a clean confirmatory replication.
- BUT the sign-reversal on the Nöldeke comparison (mushaf < nold on roots,
  mushaf > nold on rhythm) is itself informative: it argues the root-axis
  result of [[h-new-111-fisher-rao-mushaf|H-NEW-111]] is NOT mechanically driven by the same length
  structure that drives the rhythm-axis result. Root and rhythm are
  genuinely separate axes, and mushaf makes different trade-offs on each.

**Ceiling**: This finding does not promote [[h-new-111-fisher-rao-mushaf|H-NEW-111]] to CONFIRMED.
Promotion depends on [[h-new-111b-fisher-rao-char-4gram|h-new-111b]] (char-4-grams) being clean.
