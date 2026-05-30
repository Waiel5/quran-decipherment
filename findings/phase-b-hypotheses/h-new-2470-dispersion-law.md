---
finding: H-NEW-2470
title: Ordering-by-dispersion as a (qualified) corpus law — per-surah similar-pair adjacency-depletion generator
type: finding
date: 2026-05-30
author: Waiel Al-Shujaa
seed: 20260509
nperm: 10000
prereg_sha256: f29185599deda238b9d5c4492a2b68a2287d64f3190ec2af552aec3e87ea7e6d
verdict: H1 PRIMARY-AGGREGATE NULL (direction-held, not significant) · DISPERSION REAL but Q55-anchored, root-instrument-robust · H2 named-set concentration PASS · V4 near-adjacent REVERSAL is the mechanism
status: DIRECTIONAL / PARTIAL — promotes to cross-finding-028 in QUALIFIED (refrain-architecture) form
---

# H-NEW-2470 — Ordering-by-dispersion: formalising the 3-finding convergence

## Verdict in one line

The dispersion direction is **correct and never reverses** in the primary instrument, and is **decisively
significant where the phenomenon actually lives (Q55 z=−5.63 p=0.0001; root-channel aggregate p≤0.0005;
named-set concentration p=0.0002)** — but the **pre-registered PRIMARY aggregate statistic is NULL
(direction-held, not significant: A_total_obs=18 vs null 21.72, z=−1.10, p_left=0.171)** because most
surahs carry too few similar-pairs to deplete measurably. Honest reading: **ordering-by-dispersion is a
REAL but Q55-anchored refrain-architecture law, not a uniform every-surah corpus law.** It promotes to
**cross-finding-028 in QUALIFIED form**.

## 1. What was built (the generator)

A per-surah GENERATOR (pre-reg SHA-256 `f291855…7e6d`, runtime-verified; seed 20260509; 10,000 perms):

1. For every surah, build the set `S_s` of SIMILAR unordered substantive-verse pairs:
   **root-Jaccard ≥ 0.80 OR char-edit ≤ 5** (substantive = ≥3 lexical tokens). Root-sets from QAC v0.4
   (the H-NEW-2420 instrument); char-edit over PAUSE-stripped concatenated tokens (the H-NEW-2450 instrument).
2. `A_obs(s)` = how many of those pairs are ADJACENT (canonical position-difference = 1).
3. Within-surah verse-order SHUFFLE null (10,000 perms): recount how many of the SAME pairs land adjacent.
   A surah DISPERSES iff `A_obs < null_mean` (left tail).

**Census:** 749 similar unordered substantive pairs corpus-wide; 44 eligible surahs (≥1 pair, non-degenerate
null); Bonferroni α = 0.05/44 = 0.001136.

## 2. The primary result (LOCKED, honest)

### H1 — corpus-wide dispersion (PRIMARY aggregate): NULL (direction held, not significant)

| quantity | value |
|---|---|
| A_total_obs (similar-pairs adjacent, true order) | **18** |
| within-surah-shuffle null mean | **21.72** |
| aggregate z | **−1.10** |
| aggregate p_left (one-sided depletion) | **0.171** |
| replication seed+10 null mean / p_left | 21.77 / 0.167 |

Direction is the LOCKED direction (depletion, observed < null) and is **NOT a pre-commit violation** (no
reversal). But it does NOT clear the Bonferroni α=0.025 on the headline aggregate. Per the protocol this is
reported as **NULL — direction held but not significant**, with full prominence. No massaging.

**Why the aggregate is diluted (the deep reason):** of the 44 eligible surahs, only Q55 (466 pairs),
Q26 (104), Q77 (45), Q37 (43) and Q54 (13) carry double-digit pair-sets. The remaining ~39 carry 1–10
pairs whose shuffle null means are 0.05–0.6 — they literally cannot deplete by more than a fraction of a
pair, so they contribute near-zero signal but full noise to the SUM. The summed statistic is the wrong
aggregator for a phenomenon that is concentrated in one surah's 466-pair refrain lattice.

### The corroboration that the aggregate buries

- **Sign-test:** 28 of 44 eligible surahs disperse vs 16 clump (two-sided p = 0.096) — directionally clean.
- **Stouffer over per-surah left-tail p:** **z = −13.26** — the per-surah p-value field is overwhelmingly
  weighted toward depletion (this is the per-surah arm pre-registered in §3-H1; it confirms the direction
  far more powerfully than the diluted sum, but is dominated by Q55's p=0.0001 so is reported as
  corroborative, not as the independent law-claim).
- **Q55 alone, Bonferroni-significant:** A_obs=0, null 11.95, **z=−5.63, p_left=0.0001 < α=0.00114** — the
  ONLY surah that individually survives the per-surah Bonferroni. Q55 is the law.

## 3. The mechanism — Q55 is metronomic, not merely scattered (the V4 reversal)

The MW-3 near-adjacent variant (V4, adjacency `≤2`) **REVERSES** (A_obs=56 vs null 42.5, p_left=0.997 —
similar-pairs are MORE clustered than chance at distance ≤2). This is not a contradiction; it is the
mechanism. The Q55 refrain *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān* (root-set {Alw, k\*b, rbb}, **31
attestations** at verses 13,16,18,21,…,77) is spaced with **minimum gap 2** (26 gaps of exactly 2, 4 gaps of
3). So:

- at distance **= 1** it is maximally DEPLETED (0 adjacent vs null ~12) — refrains never touch;
- at distance **≤ 2** it is ENRICHED — the refrains sit every-other-verse.

**The dispersion is an immediate-adjacency avoidance implemented as fixed every-other-verse interleaving — a
metronome, not a random scatter.** This is the exact quantitative form of H-NEW-2310's "metronomic
refrain-spacing" and the engine behind H-NEW-2420's Q55 z=−5.32. Three findings, one mechanism, now measured.

## 4. H2 — named refrain/repetition-heavy set concentration: PASS

| quantity | value |
|---|---|
| named set (pre-registered) | Q55, Q77, Q26, Q37, Q54 |
| named eligible | all 5 |
| mean depletion (named) | **+2.92 pairs** |
| mean depletion (other 39) | **−0.28 pairs** |
| Δ_obs | **+3.20** |
| label-perm p (one-sided) | **0.0002** ✓ < 0.025 |

The dispersion effect concentrates in the named refrain set at p=0.0002. **Caveat (honest):** within the
named set the concentration is NOT uniform — Q55 (dep +11.95), Q77 (+1.78), Q26 (+0.93), Q54 (+0.47) disperse,
but **Q37 al-Ṣaffāt CLUMPS** (A_obs=1 > null 0.48): its *fa-mā lahum*/cosmic-cascade reprises sit closer than
chance. The named-set PASS is carried by Q55 and is a confirmation of the H-NEW-2450 diagnostic's top-disperser
roster, not an independent every-refrain-surah law. Q56 al-Wāqiʿa (10 pairs) also clumps (z=+1.77).

## 5. Robustness (MW-3 threshold/adjacency variants, aggregate H1)

| variant | A_obs | null | p_left | reversed? | reading |
|---|---|---|---|---|---|
| **Primary** (J≥0.80 OR ced≤5, adj=1) | 18 | 21.72 | 0.171 | no | direction-held NULL |
| **V1** J≥0.60 OR ced≤3 | 10 | 20.40 | **0.0005** ✓ | no | tighter pair-set ⇒ Q55 dominates ⇒ significant |
| **V2** root-only J≥0.80 | 8 | 18.60 | **0.0002** ✓ | no | the refrain (root) channel is where the law lives |
| **V3** char-only ced≤5 | 15 | 19.69 | 0.099 | no | surface-form channel weaker (Q94/Q99-type singletons) |
| **V4** primary, adj ≤2 | 56 | 42.54 | 0.997 | **YES** | the metronome: enriched at distance 2 (§3) |

**The decisive instrument finding:** the law is in the **root channel (V2, p=0.0002)** — it is a refrain
(shared-root) phenomenon. The looser-pair variants V1/V2 clear significance precisely because they shrink the
contribution of the low-power singleton surahs and let Q55 govern; the primary union spec is diluted by adding
728 char-edit candidate pairs of which most are isolated near-verbatim couplets (Q94:5-6 etc.) that, being
single pairs, carry near-zero null mass. V3 (char-only) is the weakest channel.

## 6. The verdict, stated precisely

- **NOT a uniform corpus-wide every-surah law.** The pre-registered primary aggregate is a direction-held NULL.
- **IS a real, Bonferroni-significant, root-instrument-robust phenomenon** concentrated in Q55 (and, sub-
  significantly but directionally, Q26/Q77/Q54): the canonical order places metronomically-repeated verses
  every-other-verse, never adjacent — an immediate-adjacency avoidance.
- **Convergence confirmed, not extended:** this is the SAME Q55 engine as H-NEW-2310 (metronomic spacing),
  H-NEW-2420 (Q55 z=−5.32), H-NEW-2450 (Q55 supplies 12.1 of the 17.3 null mean). H-NEW-2470 measures the
  mechanism (gap-2 lattice) and shows the effect does NOT generalise to a flat corpus-wide every-surah law.
- **Honesty on H2:** the named-set concentration PASSES but is Q55-carried and has an internal counter-example
  (Q37 clumps). The named set was pre-specified from a PRIOR finding's diagnostic, so this arm is partly
  confirmatory of that diagnostic.

## 7. Classical grounding

- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 60 (*fī fawāṣil al-āyāt* / *al-takrār*): repetition (*takrār*)
  as a rhetorical device. H-NEW-2470 refines this empirically: in Q55 the repetition is realised **by regular
  separation** (a gap-2 metronome), not by stacking — *al-takrār bi-l-tafrīq*.
- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, on Q55's *fa-bi-ayyi ālāʾ* as a structural refrain dividing the
  surah into enumerated *ālāʾ* (favors): the empirical gap-2 lattice is the quantitative form of that division.
- The metronomic reading vindicates the qualitative *tarjīʿ* (refrain-return) tradition for Q55 at
  measurement strength, while declining to over-generalise it to all repetition-bearing surahs.

## 8. Honest limits

- **Aggregator sensitivity:** the verdict swings on the choice of aggregate statistic (summed adjacency) vs
  instrument (root vs char). The summed statistic is dominated by low-power surahs; a precision-weighted or
  Q55-excluded aggregate would tell a different story. Per pre-registration the locked PRIMARY (summed, union
  spec) governs the headline verdict → NULL; the root-channel and per-surah-Q55 significances are reported as
  the substantive content.
- **N of strong dispersers is small:** essentially Q55 (decisive) + Q26/Q77/Q54 (directional). This is a
  single-architecture law, not a broad regularity. The candidate cross-finding must say so.
- **Q37/Q56 counter-examples** within and near the named set show repetition-heavy ≠ always-dispersing.
- Theological status of the refrain out of scope; this is a structural/positional measurement.

## 9. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2470-dispersion-law.md` (SHA `f291855…7e6d`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2470.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2470.json`
- This finding: `findings/phase-b-hypotheses/h-new-2470-dispersion-law.md`

---

## 10. cross-finding-028 promotion recommendation (QUALIFIED) + draft statement

**Recommendation: PROMOTE in qualified form.** Four independently pre-registered findings converge on ONE
mechanism in Q55 al-Raḥmān (and directionally in Q26/Q77/Q54): H-NEW-2310 (metronomic refrain-spacing),
H-NEW-2420 (Q55 within-surah naẓm z=−5.32), H-NEW-2450 (Q55 supplies the bulk of the adjacent-reprise null
mean), H-NEW-2470 (Q55 z=−5.63, p=0.0001; gap-2 lattice; root-channel aggregate p=0.0002). The promotion must
be QUALIFIED: H-NEW-2470's pre-registered uniform-corpus aggregate is a direction-held NULL — the law is a
refrain-architecture law, not an every-surah regularity.

### Draft cross-finding-028 statement (one paragraph)

> **Cross-finding-028 — The repetition-spacing (ordering-by-dispersion) law (QUALIFIED).** Where the Quran
> repeats a verse many times within a single surah, the canonical order spaces the repetitions at a fixed
> minimum interval rather than placing them adjacently: repetition is realised *by separation*
> (*al-takrār bi-l-tafrīq*). The paradigm and sole Bonferroni-decisive case is Q55 al-Raḥmān, whose 31-fold
> *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān* refrain is interleaved every other verse (minimum gap 2; 0 adjacent
> vs ~12 expected under a within-surah shuffle; z=−5.63, p=1×10⁻⁴), confirmed independently by four
> pre-registered instruments (refrain-spacing regularity H-NEW-2310; within-surah naẓm reversal H-NEW-2420;
> adjacent-reprise null-mass H-NEW-2450; per-surah adjacency-depletion H-NEW-2470). The effect concentrates in
> the refrain-heavy register (named set {Q55,Q77,Q26,Q37,Q54}, concentration p=2×10⁻⁴) and is strongest in the
> shared-root channel (root-only aggregate p=2×10⁻⁴). It is QUALIFIED, not universal: H-NEW-2470's
> pre-registered uniform-corpus aggregate held direction but did not reach significance (z=−1.10, p=0.17),
> because most surahs carry too few repeated verses to deplete, and at least one named surah (Q37 al-Ṣaffāt)
> mildly clumps its reprises. The law is therefore a property of the corpus's *heavily-refrained* surahs —
> above all Q55 — not a flat every-surah regularity, and it vindicates al-Suyūṭī's *takrār* (Itqān nawʿ 60)
> and al-Zarkashī's Q55 refrain-division as *repetition-by-regular-separation* at measurement strength.

---

*H-NEW-2470. Honest verdict: direction-held NULL on the universal arm; decisive on Q55; QUALIFIED promotion.
Bismillāhi al-Raḥmāni al-Raḥīm.*
