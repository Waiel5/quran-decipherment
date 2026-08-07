---
id: H-NEW-113
title: Letter-Position-within-Verse Distribution — Pre-Registration
phase: B
date: 2026-04-17
agent: h-new-113-specialist
status: PRE-REGISTERED
parent_family: H-NEW-45 / H-NEW-46 (muqaṭṭāʿat surah-level structural-marker findings)
corpus_anchor: 6,236 verses / 77,797 tokens / 330,709 letter-graphemes / Hafs-Kūfan
rules_tuple:
  orthography: no-tashkeel (canonical letter-grapheme corpus)
  tokenization: character-level (letters only)
  basmala_policy: basmala-counted-only-in-surah-1 (default JSON state)
  letter_normalization: |
    28-letter Arabic alphabet. Pre-i'jām-respecting normalization:
    hamza-bearing {أ, إ, آ, ٱ} → ا;
    ة → ه (tā' marbūṭa convention);
    ى → ي (alif-maqṣūra);
    ؤ → و; ئ → ي;
    recitation marks {ۖ ۗ ۘ ۙ ۚ ۛ ۜ ۞ ۩}, spaces, standalone ء: EXCLUDED
bonferroni_k: 3
bonferroni_family: h-new-113-letter-position
alpha_bon: 0.0167
direction_primary: muqaṭṭāʿat-14 position-distribution DIFFERENT from complement-14 at KS p<0.0167 (2-sided)
direction_secondary_rr10: RR_bin10 > 1 for muqaṭṭāʿat (verse-final fawāṣila-enrichment hypothesis, 1-sided)
direction_secondary_initial: muqaṭṭāʿat over-represented as verse-initial letter (1-sided), p<0.0167 after excluding muqaṭṭāʿat-opened-surah first-verses (circularity exclusion)
acceptance_window: |
  Primary (KS): PASS if p < 0.0167 (Bonferroni-corrected); NULL otherwise.
  Secondary rr10: report RR_bin10 with bootstrap 95% CI; PASS-directional if RR>1 and p<0.0167.
  Secondary initial: exact-binomial or χ² after circularity exclusion; PASS-directional if muqaṭṭāʿat-initial fraction > null expectation at p<0.0167.
seed: 20260417
---

# [[h-new-113-letter-position|H-NEW-113]] — Letter-Position-within-Verse Distribution (pre-registration)


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Hypothesis

The 14 muqaṭṭāʿat letters {ا ل م ص ر ك ه ي ع ط س ح ق ن} and the 14 complement letters {ب ت ث ج خ د ذ ز ش ض ظ غ ف و} occupy DIFFERENT normalized-position distributions within verses.

**Motivation**: [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] and [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] established that muqaṭṭāʿat letters are structural markers at the SURAH level (surah-position clustering, length-skew, cardinality decline). Two plausible verse-level positional signatures:

1. **Verse-initial over-representation**: mirroring their surah-opener function, muqaṭṭāʿat letters may cluster at early positions within verses.
2. **Verse-final over-representation**: as rhyme/fawāṣila anchors, muqaṭṭāʿat letters may dominate verse-final positions (the ون/ين/ار/ال fawāṣil strongly draw on the 14 set).

Either signature (or both) would extend the muqaṭṭāʿat-as-structural-marker thesis from the surah level to the verse level.

## Test cells

### Cell 1 — Primary: KS distributional difference

1. For each of the 6,236 verses, normalize the verse text (see rules_tuple), yielding a letter-only string of length L.
2. For each letter occurrence at character-index i (0-indexed), compute normalized position `p = (i + 0.5) / L ∈ (0, 1)`.
3. Aggregate all positions for all muqaṭṭāʿat-14 letter occurrences → set P_muq (expected ~247K observations given frequency skew).
4. Aggregate all positions for all complement-14 letter occurrences → set P_comp (expected ~82K).
5. Two-sample Kolmogorov–Smirnov test (two-sided): P_muq vs P_comp.
6. **Pass rule**: KS p < α_bon = 0.0167 → primary DISTRIBUTIONAL-DIFFERENCE confirmed.

Also report the KS statistic D (max |F_muq(x) - F_comp(x)|), the location x* of the max, and signed direction there.

### Cell 2 — Secondary: Per-bin relative risk (verse-final enrichment)

Bin the interval [0, 1] into 10 equal-width bins (0.0-0.1, 0.1-0.2, ..., 0.9-1.0).

For each letter ℓ, compute `density_ℓ(bin_b) = count(ℓ in bin_b) / count(ℓ total)`. This controls for the H-NEW-45.1 letter-frequency confound (ρ = -0.54): ratios are frequency-normalized.

Aggregate:
- `density_muq(bin_b) = sum_{ℓ ∈ MUQ} count(ℓ in bin_b) / sum_{ℓ ∈ MUQ} count(ℓ total)`
- `density_comp(bin_b) = sum_{ℓ ∈ COMP} count(ℓ in bin_b) / sum_{ℓ ∈ COMP} count(ℓ total)`
- `RR(bin_b) = density_muq(bin_b) / density_comp(bin_b)`

**Primary RR cell**: RR(bin 10) [i.e., positions 0.9-1.0, verse-final].
**Direction**: RR_bin10 > 1 (muqaṭṭāʿat enriched at verse-final), 1-sided.
**Null**: bootstrap resampling of verses (5,000 resamples, seed 20260417), construct 95% CI for RR_bin10. PASS-directional if lower-CI > 1 and associated p < 0.0167.

Also report RR(bin 1) and the full 10-bin RR vector for inspection (no additional formal tests).

### Cell 3 — Secondary: Verse-initial excess (circularity-controlled)

**Exclusion**: remove verse 1 of the 29 muqaṭṭāʿat-opened surahs (and ONLY verse 1, which by construction starts with the muqaṭṭāʿa block). These excluded verses are listed in the output JSON.

For the remaining verses:
- `n_init_muq` = verses whose first letter ∈ MUQ
- `n_init_comp` = verses whose first letter ∈ COMP
- `n_total` = n_init_muq + n_init_comp (verses starting with one of the 28 letters; should equal ~ all remaining verses since we normalize)

**Null expectation**: the frequency-weighted expectation under random letter choice is `E[muq-initial] = freq_muq / (freq_muq + freq_comp)`, where freq_X is the total letter count in the corpus for set X AFTER excluding the 29 opener verses.

**Test**: exact binomial: observed muq-initial fraction vs expected under frequency null.

**Direction**: muqaṭṭāʿat over-represented at verse-initial position (observed > expected), 1-sided.

**Pass rule**: 1-sided binomial p < 0.0167.

This controls for the frequency confound: if muqaṭṭāʿat letters are verse-initial at exactly their corpus frequency, the test returns NULL (correct behavior — no verse-initial SIGNAL, only background frequency).

## Frequency-confound control (LOCKED before run)

**MW-1 compliance**: all three cells are frequency-normalized by design:
- Cell 1 compares DISTRIBUTIONS (cumulative density functions) which are invariant to total counts.
- Cell 2 uses RATIOS of per-letter densities, not raw counts.
- Cell 3 uses the frequency-weighted binomial expectation as null.

This directly addresses the Spearman ρ = -0.54 muqaṭṭāʿat-frequency-skew from H-NEW-45.1. Length is also not a free variable: positions are NORMALIZED per verse.

## MW-5 positive control

**Known rhyme letters** (classical fawāṣila ون, ين, ار, ال, ام): expect strong verse-final enrichment for ن, م, ر, ل in the RR vector. Specifically, for each of {ن, م, ر, ل} individually, bin-10 density should exceed uniform-expectation (0.1) by a large margin. If this FAILS (no verse-final enrichment for ن or م), the position-binning instrument is broken; declare INSTRUMENT-FAIL.

## Garden-of-forking-paths log

1. **Novel-test disclosure**: this test has NOT been run in the project before. No previous finding examines verse-internal letter position for the muqaṭṭāʿat split. This is [[h-new-113-letter-position|H-NEW-113]]'s first look. Direction is pre-registered.

2. **Bonferroni k=3**: the 3 pre-committed cells (KS, RR_bin10, initial). Cell 2 reports the full 10-bin RR vector descriptively but only RR_bin10 is counted in the family. Cell 3's exclusion is a single well-defined operation (the 29 opener-verse-1 set); no mid-flight choice.

3. **Two competing directional hypotheses** (verse-initial vs verse-final). Both are plausible; both are pre-committed with independent α_bon. The KS primary is AGNOSTIC to direction (2-sided) because the design could manifest at any part of the CDF. If KS passes and RR_bin10 passes, that's the verse-final signature. If KS passes and Cell 3 passes, that's the verse-initial signature. If only KS passes, the signature is at interior positions (unusual but reportable).

4. **Frequency-normalization is THE control** (locked before run). Alternative designs considered:
   - OLS regression with letter-frequency as offset — rejected because KS does not accept offsets.
   - Match by letter-pair (e.g., compare ا vs و individually) — rejected because it dilutes the MUQ-vs-COMP contrast.
   - Compare RAW COUNTS at bin 10 — REJECTED because it confounds the frequency skew.
   The chosen controls (CDFs, per-letter density ratios, binomial frequency-weighted null) all return correct NULL under the "no positional signal beyond frequency" scenario. This is verified conceptually: if I shuffle letters within each verse (destroying positional structure but preserving per-verse multiset and overall counts), Cells 1 and 2 should return NULL; the frequency-weighted binomial in Cell 3 should also be unaffected.

5. **Letter-normalization is LOCKED**: the hamza-family → ا, ة → ه, ى → ي mapping is the pre-i'jām Hijazi-script-respecting convention (consistent with [[h-new-60-muqattaat-dotless-preference|H-NEW-60]] dotless-preference finding, where hamza-bearing letters were treated as ا-family). Total letter count under this normalization ≈ 329,131 (vs canonical 330,709, a 0.5% difference from standalone hamza exclusion; acceptable because standalone ء is a letter-orthographic edge case and not in the 28-alphabet).

6. **The 14-vs-14 split is NOT letter-frequency-ranked**: [[h-new-47-muqattaat-frequency-cutoff|H-NEW-47]] confirmed that muqaṭṭāʿat ≠ top-14-by-frequency. Therefore, frequency normalization cannot cause ARTIFICIAL differences between the sets via the split's definition — they could still differ in position-within-verse.

## Outputs

1. Pre-reg: `findings/phase-b-hypotheses/h-new-113-letter-position-prereg.md` (this file)
2. Script: `scripts/h_new_113_letter_position.py`
3. JSON: `findings/phase-b-hypotheses/csv/h-new-113.json` — includes 28×10 per-letter position density matrix
4. Findings: `findings/phase-b-hypotheses/h-new-113-letter-position.md`
5. Journal: `journal/h-new-113-run-1.md`

## Acceptance window

- KS p < 0.0167 → PASS primary (distributional difference)
- RR_bin10 CI excludes 1 with RR>1 AND p < 0.0167 → PASS secondary (verse-final enrichment)
- Initial-binomial p < 0.0167 (1-sided, muq-excess) → PASS secondary (verse-initial enrichment)
- MW-5 positive control FAIL → INSTRUMENT-FAIL; no verdict
- All primary + secondaries NULL → NULL (no verse-level positional signature for the 14-vs-14 split beyond frequency)

Report each cell's result with equal prominence.
