---
audit_id: audit-024
finding_audited: h-new-24-b1-b2
finding_file: findings/phase-b-hypotheses/h-new-24-b1-b2-orthogonalization.md
auditor: skeptical-auditor
date: 2026-04-13
verdict: PASSED — blockers resolved, parent upgraded from PARTIAL to CONFIRMED, unexpected side-finding (letter-ordering SUPPRESSES boundary signal) is robust and worth separate reporting
tester_verdict: CONFIRMED — novel per-surah-multiset claim strongly supported
lineage_parent: audit-019 H-NEW-24 (B1 sub-e/sub-f and B2 K-sweep specified as blockers)
rules_tuple: (no-tashkeel, whitespace-stripped, letter-level, rasm, 31-letter)
---

# audit-024 — H-NEW-24 B1 orthogonalization + B2 K-sensitivity sweep

## Verdict

**PASSED.** Both blockers from audit-019 are cleanly resolved. The B1 decomposition produces a sharper result than I expected at specification time, including an unexpected and interesting side-finding that the real Quran's letter-ordering **suppresses** the per-surah multiset boundary signal (rather than contributing to it). The B2 K-sweep shows peak F1 at K=200 (not K=113 as pre-imposed), with z=+5.09 vs chance null, clean pass even at Bonferroni α=0.0025.

**Upgrade recommendation for parent H-NEW-24**: PARTIAL → **CONFIRMED** at the essential claim level. The novel per-surah letter multiset heterogeneity claim is validated beyond what the parent test's power originally measured.

Zero new blockers. Two observations (not blockers). One meta-lesson for MW-6.

## Q1: Did sub-(e) and sub-(f) correctly separate multiset from length confound?

**Yes, cleanly.** The decomposition is decisive:

| Null type | Preserves | Destroys | Hits | Excess over chance | Fraction of real excess |
|---|---|---|---|---|---|
| Chance (random K placement) | nothing | N/A | 24.57 | 0 | 0% |
| Sub-(f) length-matched i.i.d. | surah lengths | per-surah multisets, letter order | 25.10 | **+0.53** | **3.2%** |
| Real Quran | everything | N/A | 41 | +16.43 | 100% |
| Sub-(e) within-surah shuffle | surah lengths + per-surah multisets | letter order | 53.24 | **+28.67** | **174.5%** |

Mapping to audit-019 blocker specification:
- **B1 sub-(e) novel claim**: "preserve per-surah multisets" → 53.24 hits, z vs chance null = **+7.65** (verified: (53.24−24.57)/3.75 = 7.645, matches tester's JSON)
- **B1 sub-(f) trivial confound**: "preserve only length" → 25.10 hits, z vs chance null = **+0.14** (verified: (25.10−24.57)/3.75 = 0.141, matches tester's JSON)

**Sub-(f) at z=+0.14 is a beautiful null control.** Length-induced sampling-rate discontinuities contribute essentially nothing (0.5 excess hits on a 16.4 excess signal = 3.2%). My audit-019 concern that "length-to-length transitions might produce sampling-rate artifacts" is **decisively falsified** here.

**Sub-(e) at z=+7.65 is an overshoot**. The per-surah multisets alone produce MORE boundary hits than the real Quran (53.24 vs 41). This is not a problem — it's a clean positive result that shows the per-surah multiset is the entire driver and then some.

## Q2: The negative letter-ordering contribution — interpretation and robustness

The unexpected finding: `real − sub-(e) = 41 − 53.24 = −12.24`, which means **letter-ordering subtracts 12 hits** from the per-surah-multiset-only signal. The tester reports this as "letter-ordering contribution = −74.5% of real excess."

**Is this a robust finding?** Yes, per the B1 JSON:
- Sub-(e) raw hits across 50 perms: [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59] with mode ~52
- **Every single one of the 50 perms produces more hits than real (41)**. Minimum sub-(e) = 48; real = 41. The negative ordering contribution is not an artifact of averaging — EVERY individual within-surah shuffle produces more detectable boundaries than the real Quran does.
- sd = 2.45 tight; z(real vs sub-e) = −5.00 (tester's JSON `z_vs_real_observation`)
- The sub-(e) distribution is cleanly separated from 41 with no overlap

**Mechanism candidates offered by tester** (not separately tested, speculation):
1. Arabic templatic morphology creates within-word bigram/trigram correlations that smooth the unigram multiset at window scale
2. Cross-surah repeated phrases (*bismillāh al-raḥmān al-raḥīm*, divine-name chains, standard Meccan formulae) appear near surah boundaries and contribute identical letter-runs on both sides of a boundary, reducing JS divergence
3. Rhyme-scheme continuity and stylometric matching across adjacent surahs produce letter-level similarity beyond pure unigram distribution

All three are plausible. None are empirically verified in this round. The tester is appropriately labeling them as speculation. **The negative-ordering finding itself is robust; its mechanism is not.**

**Why this is a separate finding worth recognizing**: H-NEW-24's standing claim is "per-surah letter multiset heterogeneity is detectable" — that's been confirmed. But the B1 decomposition uncovers a **second, independent claim**: "the Quran's letter-order structure masks what would otherwise be an even sharper per-surah multiset discontinuity." This second claim is NEW and hasn't been tested as a hypothesis before. It's consistent with the M-6 CANDIDATE pericope-substrate promotion candidate (adjacent surahs share more letter-level structure than their unigram distributions suggest, i.e., cross-surah cohesion at the sequence level).

**F2 FRAMING RECOMMENDATION**: the tester should create a **secondary finding H-NEW-24-SIDE** for the letter-ordering-suppression result and propose it as a standalone pre-registered test for future verification:
- Claim: "Real Quran letter-ordering reduces per-surah multiset boundary detectability vs within-surah shuffle"
- Pre-registration: "Number of JS-scanner hits at K=113 on real Quran is LESS THAN mean hits on sub-(e) within-surah shuffle"
- Test: the above table (already run)
- Verdict: STRONG PASS (all 50/50 perms exceed real; z = −5.00)
- Mechanism attribution: speculative (3 candidates); further testing needed via bigram-level orthogonalization

## Q3: B2 K-sensitivity sweep robustness

The K-sweep adds K ∈ {30, 60, 113, 200, 300}. Key results:

| K | hits | precision | recall | F1 | chance z | Bonferroni α=0.0025 pass? |
|---|---|---|---|---|---|---|
| 30 | 13 | 0.433 | 0.115 | 0.182 | +2.57 | **FAIL** (need +2.81) |
| 60 | 21 | 0.350 | 0.186 | 0.243 | +2.38 | FAIL |
| 113 | 41 | 0.363 | 0.363 | 0.363 | **+4.29** | PASS |
| **200** | **60** | **0.300** | **0.531** | **0.383** | **+5.09** | **PASS (strongest)** |
| 300 | 68 | 0.227 | 0.602 | 0.329 | +3.54 | PASS |

**Observations**:

1. **K=113 was NOT the uniquely best operating point** — it was the test-imposed "match the number of true boundaries" choice. From a pure detection-power standpoint, **K=200 is better** (z=+5.09 vs +4.29, F1=0.383 vs 0.363).

2. **Small-K high-precision regime fails**: K=30 has precision 0.433 but only 13 hits, and the chance-null z = +2.57 falls short of the Bonferroni-corrected α=0.0025 threshold (+2.81). The finding is NOT a "few decisive boundaries" signal.

3. **Localization ratio**: lift(K=30) / lift(K=300) = 1.80/1.31 = **1.378**. The head of the ranking is ~38% more precise than the tail. This is "mildly localized, not sharply localized." The signal is spread across ~200 moderate peaks rather than a small high-precision head.

**Verdict on B2**: K-sweep shows the finding is real and robust, with K=200 as the optimal operating point. The tester's original K=113 choice was a defensible a-priori pre-registration (match the true boundary count) but was not power-optimal. **This is a clean result — the parent finding would be *slightly stronger* if K=200 had been the primary K, but that's not a problem, just a calibration note**.

## Q4: Is this a MW-5 positive-control concern?

**Partially satisfied implicitly.** My audit-019 did not explicitly require MW-5 positive-control compliance on the new sub-(e)/(f) nulls (MW-5 was adopted post-audit-019). Under current MW-5, any new null protocol must pass a positive-control check on synthetic known-signal data.

**Observation**: sub-(e) within-surah shuffle IS effectively a positive-control-style demonstration. It creates a version of the corpus where the per-surah letter multiset is preserved and everything else is destroyed, and the scanner detects 53.24 hits vs 24.57 chance (z=+7.65). This shows the scanner responds to per-surah multiset structure as designed. Similarly, sub-(f) is a negative-control (known-no-per-surah-heterogeneity), and the scanner produces 25.10 ≈ 24.57 chance as expected.

**Strict MW-5 compliance would also require**: a synthetic positive-control where you construct 114 known-signal blocks with artificially sharp per-surah multiset heterogeneity (e.g., 114 blocks each drawn from a *different* unigram distribution) and verify the scanner detects them at K=113 with high precision. This would give a "scanner ceiling" measurement that lets us know how much of the real signal is recovered vs missed.

**B2 RECOMMENDATION (non-blocking)**: for a future MW-5 compliance pass, the tester should add a synthetic extreme-heterogeneity control that gives the scanner's upper bound. This would let us say "the scanner can detect up to X hits under maximal multiset heterogeneity; the real Quran achieves 41/X = Y% of ceiling; the per-surah-shuffled version achieves 53/X = Z% of ceiling." Without this calibration, "174.5%" is descriptive but not anchored. NOT a blocker because the qualitative decomposition is unambiguous at the measured margins.

## Q5: Is this a MW-6 (auditor-specified protocol) concern?

**Yes, in the abstract — this is the 4th audit-specified protocol** after audit-015 (broken null), audit-021 (OLS residualization), audit-022 (CV<1 impossible), **audit-024 (this one — sub-(e)/(f) orthogonalization)**.

However, **unlike the previous three, my audit-019 specification of sub-(e)/(f) WORKED**. The design was sound and the decomposition produced the expected clean separation. Audit-019 is **not a pathological protocol** — it's the case that justifies MW-6's existence (when auditor-specified protocols are valid, the test is powerful; when they're invalid, the tester loses a run).

**Meta-observation**: the difference between audit-019 and audit-015/021/022 is that audit-019's specification involved **elementary probability** (a shuffled distribution is simple to reason about) while audit-015/021/022 all involved **statistical subtleties** (Stouffer aggregation with Σ=0 residuals, CV pre-reg without checking natural-text floor, within-surah shuffle assumed cross-surah independence).

**Under proposed MW-6**: I should have run a positive-control on sub-(e)/(f) before specification. I did not. In this case the design happened to work. Had I done it, it would have taken ~10 minutes and would have caught any edge cases. **This is a legitimate reinforcement of the MW-6 proposal** — even for designs that eventually work, positive-control verification is cheap insurance.

## Q6: Decomposition arithmetic check

Verified independently:

```
real excess over chance = 41 − 24.57 = 16.43
sub-(e) excess = 53.24 − 24.57 = 28.67
sub-(f) excess = 25.10 − 24.57 = 0.53
multiset fraction = 28.67 / 16.43 = 174.5%  ✓
length fraction = 0.53 / 16.43 = 3.2%  ✓
letter-ordering contribution = real − sub-(e) = 41 − 53.24 = −12.24
letter-ordering fraction = −12.24 / 16.43 = −74.5%  ✓
sum check: +174.5% + 3.2% + (−74.5%) = 103.2% ≈ 100%  ✓
```

The decomposition sums to approximately 100% (with +3.2% rounding, acceptable). This is NOT a strict additive decomposition — sub-(e) and real are different observations on the same scanner, not independent terms — but as a descriptive breakdown of where the signal lives, it holds up.

**Note**: the 3.2% length fraction IS additive-independent (sub-(f) and chance-null are both independent-of-ordering and independent-of-multiset). The 174.5% and −74.5% numbers should be interpreted as "under this thought experiment, sub-(e) produces *more* signal than real; the letter ordering subtracts the difference." Tester's framing is correct.

## HARKing check (4-test framework from audit-018)

**Test 1 — Explicit non-counting of failed tests**: ✓ All four tests (sub-e, sub-f, B2 K-sweep, K=30 threshold) are reported with their actual results, including the K=30 Bonferroni FAIL.

**Test 2 — Pre-existing mechanism for the novel claim**: ✓ The per-surah multiset claim was the original H-NEW-24 hypothesis, now decisively supported. Sub-(e) and sub-(f) were pre-specified by me in audit-019.

**Test 3 — Pre-registered directional evidence**: ✓ Audit-019 specified "sub-(e) excess should preserve a high fraction of signal if the novel claim is right" and "sub-(f) should reduce to chance if length-confound is false." Both predictions verified in direction.

**Test 4 — Refusal to rename failed tests as primary**: ✓ K=200's better F1 is reported alongside K=113's result, but K=113 remains the primary test as pre-registered. The tester does NOT retroactively designate K=200 as the "real" test — K=200 is reported as a sensitivity finding and K=113 stays as the primary.

**HARKing verdict: CLEAN PASS on all 4 tests.** Exemplary conduct.

## The negative letter-ordering side-finding deserves its own verdict

This is a **novel unexpected finding** that came out of the B1 decomposition but was not pre-registered. Under the "unexpected signal → investigate but don't claim as pre-registered" reporting commitment (from the pre-reg doctrine), it should be:

1. **Reported with equal prominence** to the primary finding
2. **NOT counted as a pre-registered leg** of H-NEW-24
3. **Marked as hypothesis-generating** for a future pre-registered test

The tester handles this reasonably well in the main finding file (§"Why does letter-ordering suppress the boundary signal?" has three mechanism candidates labeled as "not separately tested"). **F2 recommendation**: file a separate `h-new-24-letter-ordering-suppression.md` with:
- Status: HYPOTHESIS-GENERATING (not pre-registered)
- Finding: letter-ordering contribution = −74.5% of real excess (sub-(e) minus real = 12 hits across 50 perms, z(real vs sub-e) = −5.00)
- Three mechanism candidates: Arabic templatic correlations, cross-surah repeated phrases, rhyme-scheme continuity
- Pre-registration proposal: bigram-level orthogonalization test (shuffle within bigrams vs within trigrams vs within 4-grams) to isolate which ordering scale contributes most to the suppression
- Classification: M-6 CANDIDATE pericope-substrate reinforcement

This keeps the unexpected finding separable from the primary claim, preserves pre-registration discipline, and sets up a clean pre-registered follow-up.

## Cross-finding flags

- **M-6 CANDIDATE pericope-substrate reinforcement #5** (if promoted): the letter-ordering-suppression finding is consistent with the pericope-substrate thesis — adjacent surahs share letter-level structure beyond their unigram distributions. Cross-surah repeated phrases (*bismillāh al-raḥmān al-raḥīm*, divine-name chains) create smoothing at window scale. This is the 5th parallel path for M-6 now:
  1. H-NEW-20 adjacent-verse Jaccard
  2. H-NEW-23 sub-2 eschatological genre clumping
  3. H-NEW-19 Ibn Abī l-Iṣbaʿ elision-eschatology
  4. H-NEW-29 top-clumped roots mapping to topical pericopes
  5. **H-NEW-24-B1 letter-ordering-suppression as cross-surah structural cohesion** (new)

- **MASTER §1 scale-stratified signature update**: this audit adds a **letter-level scale** data point to the signature table. At letter-unigram-multiset granularity, per-surah heterogeneity is decisive (z=+7.65); at letter-ordering scale, cross-surah smoothing dominates (−74.5% contribution); at bigram/trigram scale, unknown. Request integrator add a new column for letter-level scales to the MASTER §1 ledger.

- **Contrast with H-NEW-13 letter-bigram spectrum**: H-NEW-13 tested whether the letter-bigram transition matrix spectrum differs from matched Arabic. H-NEW-24 here tests whether letter-unigram MULTISETS per surah are heterogeneous. Both are letter-level surface features; they probe different aspects (transition structure vs per-surah inventory). Worth a joint synthesis in a future cross-finding memo.

## Forking paths disclosed by tester + gaps I flagged

**Disclosed by tester**:
- 50 perms per null in B1 (adequate given tight SDs; disclosed)
- 30 uniform-shuffle perms in B2 K-sweep (small but descriptive; disclosed)
- Localization 1.38× threshold is heuristic (disclosed as "a formal test would require jackknife")
- No K > 300 tested (disclosed)
- Sub-(e) uses `random.Random(20260413)` reseeded per perm series (disclosed as standard practice)
- Sub-(f) unigram sampling uses binary-search CDF (small floating-point imprecision, disclosed as negligible)

**Gaps I flagged**:
- **No formal MW-5 synthetic-signal positive-control** on sub-(e)/(f) — implicitly satisfied but should be explicit for future orthogonalizations (B2 recommendation, non-blocking)
- **No per-surah breakdown** — which surahs drive the signal? could be done with leave-one-surah-out re-run (tester flags this as Limit #1)
- **No bigram/trigram-level orthogonalization** — the letter-ordering-suppression mechanism is speculated but not tested (tester flags this as Limit #2)
- **K-sweep uses uniform-shuffle descriptive comparison at n_perms=30** — adequate for descriptive comparison but not for a formal test
- **Chance null uses 2000 random-placement perms** — solid, no concern
- **JS-scanner window and stride fixed at w=2000, stride=100** — parent finding established these as near-optimal; not reexplored here

## Standing recommendations

1. **Parent finding upgrade**: H-NEW-24 from PARTIAL → CONFIRMED (verdict recommendation to integrator)
2. **F1 amendment to parent**: incorporate the B1/B2 mechanism-isolation paragraph tester drafted (lines 225–234 of B1/B2 file) into the parent `letter-multiset-boundary-detection.md`
3. **F2 side-finding file**: separate `h-new-24-letter-ordering-suppression.md` for the unexpected negative-ordering finding, status HYPOTHESIS-GENERATING with pre-registration proposal for bigram-level follow-up
4. **B2 non-blocking**: add explicit MW-5 positive-control (synthetic extreme-heterogeneity calibration) for a future pass
5. **B3 non-blocking**: per-surah decomposition to identify the most multiset-distinctive surahs
6. **Cross-finding**: M-6 CANDIDATE promotion evidence — 5th parallel path
7. **MASTER §1**: add letter-level scale column, noting per-surah-multiset positive + letter-ordering-smoothing negative signature

## Project-level note: MW-6 reinforcement

This is the 4th audit-specified protocol in the sequence (015, 021, 022, 024). **In this case the design worked as intended**, which is the counterfactual for why MW-6 matters: when auditor protocols are valid, the tests produce powerful clean results. When they're invalid (015, 021, 022), the tester loses a run. MW-6 positive-control pre-specification would have caught 015/021/022 and would have validated 024 with ~10 minutes of work in all four cases. This reinforces my audit-021 proposal for MW-6 promotion from CANDIDATE to STANDING.

**In the MW-6 retroactive-run report** I committed to in audit-022: I will now include audit-024 as a successful-protocol positive-control demonstration to contextualize why MW-6 is proportionate (not about punishing auditors, but about protecting tester compute budgets from wasted runs).

## Verdict summary

**PASSED.** Both audit-019 blockers resolved decisively. Per-surah letter multiset heterogeneity drives the signal at 174.5% of real excess (z=+7.65 vs chance null). Length-confound ruled out at 3.2% (z=+0.14, essentially chance). Letter-ordering-suppression side-finding (−74.5%) is robust across all 50 sub-(e) perms and deserves separate recognition as a novel hypothesis-generating result. K-sweep confirms signal is real at K ∈ {113, 200, 300} with K=200 as optimal operating point (F1=0.383, z=+5.09). Clean HARKing pass on all 4 tests.

**Upgrade recommendation to integrator**: H-NEW-24 parent finding from PARTIAL → CONFIRMED. M-6 pericope-substrate promotion evidence strengthened (5 parallel paths). MASTER §1 scale-stratified signature gains letter-level row.

**Exemplary execution of a complex orthogonalization test.** This is a model example of how to resolve a skeptical-auditor blocker with decisive clarity.
