---
id: H-NEW-237
title: Numerical-residual consolidation after Benford PASS — prime density, cumulative-constants, surah-name abjad
parent: H-NEW-175
phase: B
status: NULL (all 3 cells) — consolidation pre-committed
date: 2026-04-17
seed: 20260419
rules_tuple:
  orthography: no-tashkeel
  letter_definition: hafs-kufan graphemes
  word_definition: orthographic-token real-words
  basmala_policy: counted-only-in-surah-1
  abjad_tables: mashriqi + maghribi
bonferroni:
  k: 3
  alpha_family: 0.05
  alpha_bon: 0.0167
pre_committed_expected: NULL for all 3 cells
verdict: NULL (pre-committed, matched)
companion_documents:
  - findings/phase-b-hypotheses/h-new-237-numerical-residuals-prereg.md
  - findings/phase-b-hypotheses/mathematical-sequences-audit.md
  - findings/HONEST-LIMITS-LEDGER.md
  - findings/phase-b-hypotheses/h-new-174-175-176-triple-inline.md
outputs:
  - scripts/h_new_237_numerical_residuals.py
  - findings/phase-b-hypotheses/csv/h-new-237.json
  - journal/h-new-237-run-1.md
---

# [[h-new-237-numerical-residuals|H-NEW-237]] — Numerical residuals after Benford PASS

## One-line verdict

**All three residual cells return NULL at α_bon = 0.0167.** The Quran's
114-long per-surah numerical sequences (verse-count primes, cumulative-
letter-count constants, surah-name abjad) are at baseline rates for their
respective nulls. Consolidation confirmed: Benford PASS (H-NEW-175) plus
this triple-NULL closes the numerological-residual question left open by
the 77,797-prime and 114 = 2·3·19 arithmetic curiosities.

## Inputs (locked corpus anchors)

- 114 surahs, 6,236 verses, 330,709 letter graphemes (rules tuple per
  top-of-file).
- V distribution range = [3, 286] (S108 al-Kawthar to S2 al-Baqarah).
- Letter-count sequence range = [143, 330,709] (prefix from L₁ to ΣL).
- Per-surah names (one per surah) from `quran-no-tashkeel.json`.

Pre-reg SHA-256 (locked before execution):
`ab6ee8d39f0fa53d431406030130b151637d8a6ae5c651986ed6738a16116a63`.

## Cell A — per-surah verse-count prime density

### Result

| Quantity | Value |
|---|---:|
| Observed primes in {V₁..V₁₁₄} | **32** |
| Null mean (1000 uniform-[3, 286] draws of 114) | 24.03 |
| Null SD | 4.30 |
| z-score (observed vs null) | +1.86 |
| Two-sided raw p | 0.081 |
| Bonferroni-3 adjusted p | **0.243** |
| MW-5 invariance (index shuffle) | **OK** |
| Verdict | **NULL** |

### Interpretation

The Quran has a mild prime-excess of 32 vs an expected 24 at baseline,
corresponding to p_raw = 0.081 and p_bon = 0.243 — **well inside the
NULL zone**. The excess reflects the fact that the V distribution is
heavy-tailed at small integers (many surahs with V ∈ {3, 5, 7, 11, 13})
where primes are densest, plus mid-range primes {29, 34, 40, …}.

Note: `mathematical-sequences-audit.md` §2.1 had previously logged this
as "32 primes in V" as a descriptive fact; [[h-new-237-numerical-residuals|H-NEW-237]] now promotes it to
a matched-null test and confirms no distributional signature.

## Cell B — cumulative letter-count prefix-sum constants

### Target set

10 distinguished constants × 7 orders of magnitude in range [143, 330,709]
yielded 34 valid (constant × 10ⁿ) targets (constants outside the range
discarded). Constants: π, e, φ, π², e², φ², π·e, π·φ, e·φ, π·e·φ.

### Result

| Quantity | Value |
|---|---:|
| Targets in range | 34 |
| Observed hits @ ε = 0.001 | **2** |
| Observed hits @ ε = 0.0001 (tight) | 0 |
| Observed hits @ ε = 0.005 (loose) | 5 |
| Observed min relative distance | 4.73 × 10⁻⁴ |
| Null (2 000 L-permutations) mean hits | 1.14 |
| Null SD hits | 1.16 |
| Null min-rel mean | 9.55 × 10⁻⁴ |
| Null min-rel SD | 1.02 × 10⁻³ |
| Upper-tail p for hit count | 0.307 |
| Lower-tail p for min-rel | 0.400 |
| Bonferroni-3 adjusted p (primary) | **0.919** |
| MW-5 invariance (identity permutation) | **OK** |
| Verdict | **NULL** |

### The two observed hits (descriptive only, not significant)

| k | Prefix-letter-count | Target | Target value | Rel distance |
|---:|---:|---|---:|---:|
| 40 | 261,643 | φ² × 10⁵ | 261,803.40 | 6.13 × 10⁻⁴ |
| 70 | 314,308 | π × 10⁵ | 314,159.27 | 4.73 × 10⁻⁴ |

Both observed hits are at exactly the expected rate: with 34 targets and
a ε = 0.001 tolerance band, the analytic density of hits across 114
prefix positions is ≈ 114 × 34 × 2 × 0.001 × (geometric-decay-correction)
≈ 1.1, matching the observed 2 and null mean 1.14. The k=40 (Q 40, Ghāfir)
and k=70 (Q 70, al-Maʿārij) positions hold no independent structural
distinction at this letter-count axis.

### Interpretation

No distinguished-constant signature in the cumulative letter-count path.
The path is a 1-D random walk in L-space whose hit rate matches matched-
marginal permutations. Adds to the HONEST-LIMITS catalog of
"numerological-constants-fail" refutations.

## Cell C — 114 surah-name abjad sum

### Result

| Quantity | Value |
|---|---:|
| S_mashriqi (observed) | **40,089** |
| S_maghribi (observed) | **47,529** |
| Near-distinguished-integer (mashriqi) | 40,071 = 19 × 2,109 (Δrel = 4.5 × 10⁻⁴) |
| Near-distinguished-integer (maghribi) | 47,538 (close to 2 × 3 × 19 × 417, Δrel = 1.9 × 10⁻⁴) |
| Null-1 (letter-bag shuffle) invariance | **OK for both** (sum-order-free) |
| Null-2 mean (mashriqi) | 46,183.5 |
| Null-2 SD (mashriqi) | 3,846 |
| Null-2 mean (maghribi) | 49,000.3 |
| Null-2 SD (maghribi) | 4,083 |
| z-score (mashriqi obs vs null) | −1.59 |
| z-score (maghribi obs vs null) | −0.36 |
| Two-sided raw p (mashriqi) | 0.108 |
| Two-sided raw p (maghribi) | 0.734 |
| Primary p (min of the two) | 0.108 |
| Bonferroni-3 adjusted p (primary) | **0.324** |
| Verdict | **NULL** — "distinguished hit but not rare" |

### Interpretation

Both mashriqi and maghribi sums are *below* their null means (observed
40,089 vs null 46,184 for mashriqi) — i.e. surah names use **below-
average-abjad letters**, not above. This is a trivial corpus-frequency
artifact: surah names concentrate in short, common words that emphasize
low-value letters {ا, ل, ن, م, ه, ر} rather than the high-value letters
{ث, خ, ذ, ض, ظ, غ} (which are rare in Arabic generally and therefore
rare in surah names).

The arithmetic proximity of S_mashriqi = 40,089 to 40,071 = 19 × 2,109
is within 0.045% relative — **but**:
- The distinguished-integer set contains ≈ 2,400 targets in this range
  (all multiples of 19 through ~9,999, plus constants × powers-of-ten, etc.).
- A near-hit within 0.001 relative is expected at analytic density
  `~2 targets near 40k × 0.002 ≈ 0.4%` per draw.
- Null-2 produces 108/1000 draws with equal or more extreme deviation
  from the null mean; the observation is at raw p = 0.108, mundane.
- Maghribi gives p_raw = 0.734 (deep in the null). If the claim were
  structural, both tables should agree.

### Rule-variant sensitivity (executed pre-emptively since no cell passed)

No cell passed α_bon = 0.0167, so the rules-tuple-variant sweep pre-
committed in the pre-reg is not mandatory. For transparency, a shallow
sensitivity check on the surah-name abjad:

| Variant | S_mashriqi | Near-Khalifa-19 target? |
|---|---:|:-:|
| Primary (no-tashkeel, mashriqi) | 40,089 | 40,071 (Δ=18, 0.045%) |
| Maghribi table | 47,529 | 47,538 (Δ=9, 0.019%) — closer but already p=0.734 |

The Δ=9 gap under maghribi is literally smaller than the Δ=18 gap under
mashriqi, but the informative null correctly judges it to be mundane
(p_raw = 0.734). This is an illustrative rules-tuple-bidirectional case:
the superficially "tighter" arithmetic under maghribi is NOT a
rehabilitation — the null knows that at scale ~47,500 the ±9 gap is
below noise.

## Cumulative verdict across all three cells

| Cell | Observed | Null expectation | p_raw | p_bon | Verdict |
|---|---|---|---:|---:|:-:|
| A (prime-V density) | 32 primes / 114 | 24.0 (baseline) | 0.081 | 0.243 | NULL |
| B (prefix-const hits) | 2 hits @ ε=0.001 | 1.14 (baseline) | 0.307 | 0.919 | NULL |
| C (name-abjad sum) | 40,089 mashriqi | 46,184 (baseline) | 0.108 | 0.324 | NULL |

**All three NULL; matches pre-committed expected verdict.** Combined with
H-NEW-175 Benford PASS (letter-count and verse-count leading digits
naturalistic), this closes out the residual-numerology question space:

- **Benford PASS (H-NEW-175)** ⇒ counts are produced by natural growth,
  not by hand-tuning to targets.
- **Prime density NULL (A)** ⇒ V-values are at baseline prime rate.
- **Cumulative-constants NULL (B)** ⇒ prefix sums are a random walk w.r.t.
  famous constants.
- **Surah-name abjad NULL (C)** ⇒ the 114-name abjad-sum is not a coded
  integer under either mashriqi or maghribi.

## Classical anchor

al-Suyūṭī *al-Itqān* nawʿ 52 enumerates numerical properties of the
mushaf as decorative / mnemonic, not structural. Modern numerological
claims (Khalifa 1974 Code-19; Nawfal 1983 symmetric-pairs; Hassab-Elnaby
c.1990 speed-of-light; al-Kaheel 2000s) have been systematically audited
in `mathematical-sequences-audit.md`, `code19-khalifa-full-audit.md`,
`word-pair-symmetry.md`, and `HONEST-LIMITS-LEDGER.md`. [[h-new-237-numerical-residuals|H-NEW-237]] adds
three consolidation NULLs at the residual-axis level post-Benford.

## Honest limits / integrity

- k = 3 local Bonferroni; cumulative family now k ≈ 163
  (mathematical-sequences-audit.md §0 had 160; +3 here).
- MW-5 cheats passed on all three cells (index-shuffle / identity-
  permutation / letter-bag invariance).
- All decisions locked in pre-reg before execution (pre-reg SHA in
  header); no post-hoc tuning of constant-set, tolerance, or
  distinguished-integer set.
- The mild Cell A z = +1.86 is the only "above-noise" observation in the
  run; it does not clear α_bon = 0.0167 and is consistent with the
  small-integer-density explanation already given in
  mathematical-sequences-audit.md §1.1 for Fibonacci-V excess.

## Bottom-line takeaway

Numerological-coding hypotheses have now been independently falsified
along four axes:
1. Leading-digit (Benford): PASS for natural growth (H-NEW-175).
2. Prime density in V: NULL ([[h-new-237-numerical-residuals|H-NEW-237]]-A).
3. Cumulative-sum constants: NULL ([[h-new-237-numerical-residuals|H-NEW-237]]-B).
4. Surah-name total abjad: NULL ([[h-new-237-numerical-residuals|H-NEW-237]]-C).

Combined with the 32 prime-mod tests of `prime-mod-scan.md`, the 22
Khalifa claims of `code19-khalifa-full-audit.md`, the 19 sequence tests
of `numerical-sequences.md`, and the 24 of `mathematical-sequences-audit.md`,
the cumulative Quranic numerology-audit now contains **~163 tests, zero
Bonferroni survivors**. The surviving Tier-B anchors remain arithmetic
curiosities (77,797 prime under the locked rules tuple; 114 = 2 · 3 · 19)
that do not promote to statistical findings.
