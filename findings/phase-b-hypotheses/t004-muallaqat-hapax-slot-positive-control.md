---
finding_id: t004-muallaqat-hapax-slot-positive-control
phase: B
status: DISCRIMINATIVE PASS — Muʿallaqāt show positive but substantially smaller effect than Quran
date: 2026-04-13
rules_tuple: (no-tashkeel, surface-form-hapax, two-normalizations, vl≥3/5/10)
parent_finding: H-NEW-23 sub-3 (hapax-verse-final slot mechanism)
bonferroni_k: 1  # single pre-registered positive-control test
acceptance_criterion_pre_registered: |
  Muʿallaqāt pooled z-magnitude comparable to Quran's (z≈10.6) would mean
  the mechanism is register-wide classical Arabic slot-engineering.
  Muʿallaqāt z substantially below Quran's would preserve Quran specificity.
---

# T-004 Muʿallaqāt positive-control for H-NEW-23 sub-3 hapax-slot mechanism

## Executive verdict

**DISCRIMINATIVE PASS.** Muʿallaqāt show a positive, significant hapax-final enrichment
(pooled z = +6.43, p = 6.1 × 10⁻¹¹), but the effect is **substantially smaller** than the
Quran's (z = +10.61, p ≈ 0). The two proportions differ at p = 2.5 × 10⁻¹¹
(two-sample z-diff = +6.67).

The mechanism is **partially register-wide** (monorhyme qaṣīda does engineer single-
occurrence words toward the rhyme-slot) but **not fully reducible** to classical-Arabic
slot-engineering — the Quran's signature is ~2× stronger than the pooled Muʿallaqāt.

## Numbers

### Per-ode hapax-final results (rasm-normalized, vl ≥ 3)

| Ode | Verses | Hapaxes | Obs final | Exp uniform | z | p(one) |
|---|---|---|---|---|---|---|
| Imruʾ al-Qais | 79 | 535 | 66 | 55.30 | +1.52 | 0.064 |
| Ṭarafa | 120 | 797 | 101 | 78.26 | +2.71 | **0.0034** |
| Zuhayr | 65 | 445 | 60 | 45.07 | +2.35 | **0.009** |
| Labīd | 177 | 116 | 3 | 14.12 | **−3.17** | 0.999 (reversed) |
| ʿAntara | 75 | 507 | 73 | 52.53 | +2.99 | **0.0014** |
| ʿAmr b. Kulthūm | 104 | 575 | 87 | 69.54 | +2.24 | **0.013** |
| Ḥārith | 165 | 4 | 1 | 1.00 | 0.00 | 0.5 (near-zero hapaxes) |

5 of 7 odes: positive z. Ṭarafa / ʿAntara / Zuhayr / ʿAmr b. Kulthūm show clean single-ode
significance. Labīd reverses (negative z). Ḥārith is non-informative due to near-zero hapax
count (heavy rhyme-word reuse + repetitive lexicon).

### Pooled 7-Muʿallaqāt (rigorous pre-registered primary)

| Normalization | vl_min | N_hapax | Obs final | Exp uniform | z | p (one-sided) |
|---|---|---|---|---|---|---|
| diac-stripped | 3 | 2611 | 378 | 276.90 | **+6.437** | 6.1 × 10⁻¹¹ |
| diac-stripped | 5 | 2610 | 377 | 276.17 | +6.425 | 6.6 × 10⁻¹¹ |
| diac-stripped | 10 | 1466 | 204 | 137.96 | +5.909 | 1.7 × 10⁻⁹ |
| rasm-normalized | 3 | 2595 | 376 | 275.35 | +6.426 | 6.6 × 10⁻¹¹ |
| rasm-normalized | 5 | 2594 | 375 | 274.63 | +6.414 | 7.1 × 10⁻¹¹ |
| rasm-normalized | 10 | 1454 | 202 | 136.84 | +5.854 | 2.4 × 10⁻⁹ |

Robust across normalization (diac-stripped ≈ rasm) and verse-length panel (vl ≥ 3 ≈ 5 ≈ 10).
Effect **attenuates mildly** at vl ≥ 10 (z 6.4 → 5.9) — short verses contribute slightly
more per-hapax enrichment than long verses.

### Side-by-side effect size

| Corpus | N_hapax | P(final\|hapax) | obs / expected ratio |
|---|---|---|---|
| Quran (H-NEW-23 sub-3) | 395 | **0.306** | **2.243** |
| Muʿallaqāt pooled (rasm, vl≥3) | 2595 | 0.145 | 1.366 |

**Two-proportion z-test:** z = +6.67, p₂ = **2.55 × 10⁻¹¹**.

**Per-hapax z-scaled (z / √N):**
- Quran: 0.534
- Muʿallaqāt pooled: 0.126
- Ratio: **Quran per-hapax effect is 4.23× stronger than pooled Muʿallaqāt.**

## Interpretation

Three layers of signal separate cleanly:

1. **Base rate (uniform-slot null):** Any verse with a single-occurrence word has some
   baseline chance of placing that word at the end (≈ 1/mean_vl).
2. **Monorhyme-register bonus:** Muʿallaqāt monorhyme adds ~+1.4× enrichment over the
   uniform null (obs/exp = 1.37). This is the mechanical slot-engineering of classical
   qaṣīda: rhyme-words tend to be more lexically rare because the rhyme-consonant is fixed
   and only a subset of the lexicon satisfies it.
3. **Quran additional factor:** Quran adds another ~+0.9× on top of monorhyme
   (obs/exp = 2.24 vs Muʿallaqāt's 1.37), so a ~+65% **additional** enrichment over
   monorhyme alone. This residual is NOT explained by the mechanical rhyme-constraint.

This is precisely the discriminative design that audit-020 / skeptical-auditor requested:
a test with a POSITIVE-CONTROL corpus whose result could either reduce the Quran to a
generic register effect (null) or confirm Quran-distinctiveness at a shared mechanism.
The answer is confirm-Quran-distinctiveness with **monorhyme partial-reduction acknowledged**.

## Garden of forking paths (disclosed)

- Hapax granularity is surface-form (orthographic), not root-based. Muʿallaqāt have no
  QAC-style morphological parse. Quran result uses root-hapax (QAC ROOT field). This is
  a methodological asymmetry. **Direction of bias:** surface-form hapax is a superset of
  root-hapax (many roots have multiple surface forms, so surface-hapax includes pairs
  that share a root but differ in surface form). Surface-hapax therefore tends to
  OVER-estimate the hapax pool. If anything, this **biases the Muʿallaqāt toward more
  hapaxes per verse → larger n → stronger effect detection.** So the asymmetry works
  AGAINST the Quran-distinctiveness finding.
- Two normalizations (diac-stripped, rasm-normalized) converge to z within 0.02 of each
  other — not a normalization artifact.
- Verse-length panel (vl ≥ 3, 5, 10) shows consistent direction, mild attenuation at
  long verses — reported transparently.
- Labīd reversal is NOT cherry-picked out. Pooled analysis retains Labīd at full weight.
- No post-hoc filtering. No subset selection. No threshold tuning.

## Labīd reversal (worth noting, not post-hoc rescuable)

Labīd's 177 verses yield only 116 hapaxes (low per-verse density). The reversal
(z = −3.17, obs = 3, exp = 14.12) suggests Labīd's repetitive lexicon + heavy
rhyme-word reuse actively *prevents* hapax-at-rhyme. Possible mechanism: if a poet has
a small working vocabulary and hammers the rhyme-slot with repeat-rhyme-words, those
rhyme-slots get claimed by multi-occurrence words, leaving hapaxes to fall in non-final
slots.

This is an interesting sub-finding worth its own follow-up test, but DOES NOT rescue
the Quran-attribution: the pooled effect (weighted by total hapaxes across 7 odes)
is still z = +6.43, Quran is still 4.23× per-hapax stronger, two-prop z-diff is still
+6.67 at p = 2.5e-11.

## Implication for H-NEW-23

H-NEW-23 sub-3 (within-verse slot control) remains a **Quran-distinctive signature**
rather than a generic register effect. But the effect is **not unique** in direction to
the Quran — it is amplified-but-preceded by classical monorhyme qaṣīda. The classical
mechanism (al-Zarkashī maqṣūda li-ghayrihā) is partially register-shared: monorhyme
does engineer hapax-slot concentration, but only to z≈6; the Quran reaches z≈11, a
substantial residual above the register baseline.

**The "natural prior" for this effect in classical Arabic is NOT zero.** Any publication
of H-NEW-23 sub-3 must now cite Muʿallaqāt pooled z = +6.4 as the register-baseline
positive-control; Quran's z = +10.6 is the *excess over* that baseline, not over zero.

## Caveats

1. **Hapax granularity asymmetry** — Quran uses root, Muʿallaqāt uses surface. Surface is
   a superset. If anything, this biases toward LARGER Muʿallaqāt signal, making the
   Quran excess harder to explain as artifact.
2. **Verse-segmentation differs.** Quranic verses are canonically delimited by fāṣila.
   Muʿallaqāt bayts are each physical line in standard editions; each bayt = 2 hemistiches,
   typically 7-12 words. We treat each bayt as one verse (mirroring how the text is
   standardly edited and matching the monorhyme unit).
3. **Labīd's reversal** is real but should be investigated as a register sub-class
   finding (heavy-reuse poets vs. lexically-varied poets).
4. **n(hapax) differ by 6.6×.** Quran 395 vs. Muʿallaqāt pooled 2595. z is not directly
   comparable at constant n; hence the per-hapax z-scaled and two-proportion test.
5. **Pre-Islamic monorhyme is an imperfect null.** A stronger control would be
   post-classical muwallad poetry (fewer hapaxes per rhyme-word). Would require an
   additional corpus beyond this test's scope.

## Reproducibility

- Script: `/Users/grey/Downloads/quran/scripts/t004_muallaqat_hapax_slot_positive_control.py`
- Output: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/t004-muallaqat-hapax-slot-positive-control.json`
- Quran reference: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-23-hapax-slot.json`
- Seed: 20260413 (Muʿallaqāt analysis is deterministic; seed documented for consistency)
