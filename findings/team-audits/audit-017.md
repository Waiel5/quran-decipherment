---
audit_id: audit-017
target_finding: team-discovery-016 (H-NEW-13 bigram spectrum)
auditor: skeptical-auditor
date: 2026-04-12
verdict: PASSED AS NULL (primary); SIDE-FINDING CORRECTLY NOT CLAIMED (needs pre-registered retest)
parent_finding: task #20, pure novelty (computational-tester origination)
cc: integrator
---

# Audit-017 — H-NEW-13 bigram spectrum + Bukhari side-finding

## Verdict: PASSED AS NULL (primary); Bukhari side-finding correctly quarantined pending pre-registered retest

Primary hypothesis (Quran bigram spectrum distinctive vs matched Arabic) is cleanly null across all four pre-registered criteria. Honest report. The Bukhari |λ_2|=0.265 side-finding is correctly treated as unpre-registered — tester did not claim it as a finding and explicitly proposed a pre-registered retest on Muslim/Tirmidhī. This is exactly the discipline garden-of-forking-paths requires. No blockers on the primary; two items flagged on the side-finding before it gets promoted.

## Why this null is interpretable

The test has five matched baselines (Bukhari, Sīra, Jāḥiẓ, Mutanabbī, Muʿallaqāt) covering prose-formal, prose-narrative, prose-literary, and poetry. Quran sits inside the 0.15-0.18 band with four of five. This is not a null from an underpowered instrument — it's a null from a corpus that genuinely does not differ from matched Arabic at this layer.

**Implicit positive control present:** Bukhari's outlier status (|λ_2|=0.265, 2.5σ above non-Bukhari mean) shows the instrument CAN detect a genuine corpus-specific signal when one exists. This is exactly the positive-control principle I introduced in audit-015, here satisfied serendipitously by the Bukhari result. The instrument is calibrated; the Quran result is real null.

## Blockers on primary: none

## Blockers on side-finding (before any claim)

**SB1. Pre-registered retest on ≥2 independent ḥadīth corpora.** Tester proposed Muslim and Tirmidhī. I would add Nasāʾī to reach three independent ḥadīth collections, since the hypothesis ("ḥadīth-register slow-mixing") predicts a shared property, not a Bukhari-specific one. If 3/3 ḥadīth corpora return |λ_2| > 0.20 while non-ḥadīth stays below 0.20, it's a robust register signature. If 1/3 or 2/3, it's a corpus-specific accident or Bukhari-specific compositional quirk.

**SB2. Isnād-strip variant.** If the slow-mixing is driven by formulaic isnād (ḥaddathanā X qāla…), stripping isnāds from the corpus should push |λ_2| back toward the 0.15-0.18 band. This is the mechanism test, and it dissociates "ḥadīth-register phonotactics" (general) from "isnād formulaics" (specific). Both are real signatures if they hold, but they're different claims.

**SB3. Corpus-size control.** Bukhari is 2M chars vs Mutanabbī's 35K. Size alone should tighten eigenvalue estimates (more data → less noise), not shift them. But Sīra at 1M and Jāḥiẓ at 1.4M are comparable-size non-ḥadīth controls and they sit in-band — so size is not the confound. Worth checking with a 35K-subsample of Bukhari to be rigorous.

## Non-blocking methodological improvements (flagged by tester)

**N1. Bootstrap CI on |λ_2|.** Tester's Limit 2. Without it, "Bukhari Δ = -0.089 vs Quran" is a point estimate. Bootstrap-resample character sequences 1000× per corpus; report 95% CI on |λ_2|. This is cheap and quantifies the outlier claim properly.

**N2. NumPy full eigendecomposition.** Tester's Limit 1. Power iteration with deflation can miss complex-conjugate pairs of equal magnitude. For the 30×30 transition matrix, `np.linalg.eigvals` is O(n³) = 27k ops, trivial cost. Re-run and report the full eigenvalue spectrum — not just |λ_2|. This also gives the spectral gap more robustly.

**N3. Tatweel filter on Muʿallaqāt.** Tester's disclosure already handles this correctly (core-letter L1 is ~0.23, not 0.42). Tatweel filter should be folded into the preprocessing pipeline for all future char-level tests to avoid this forking-path question recurring.

None of N1-N3 are blockers; they would strengthen the finding and should be incorporated into any formal SB1-SB3 retest.

## Classical-framing note

Tester correctly connects to ʿIlm al-ḥarf: "unigram letter frequency is distinctive; bigram transition dynamics are not." This adds a data point to the emerging pattern that **the Quran's distinctiveness lives at some layers (unigram frequency, adjacent-verse lexical cohesion, cross-surah seam) but not at others (bigram Markov dynamics, long-range intra-surah bracket)**. This is the scale-stratified signature I flagged in audit-016 as a §1 candidate. Bigram spectrum now joins intra-surah bracketing as a confirmed "not at this layer" negative.

**MASTER:scale-stratified-signature** §1 candidate update (if integrator adopts):
- Distinctive at: unigram letter freq, adjacent-verse root-Jaccard, cross-surah seam root-Jaccard
- Not distinctive at: bigram Markov spectrum (this finding), intra-surah first↔last root-Jaccard (audit-016)

Four data points now, two on each side. The pattern is coherent and worth formal registration.

## Meta-pattern notes

**M-1 (surah-outlier registry):** not applicable — this is a whole-corpus test.

**M-2 (corpus-wide-continuous signature):** implicit negative — Quran's |λ_2| being mid-range across baselines means whatever corpus-wide signature exists at bigram level is shared with classical Arabic, not Quran-specific. Doesn't disqualify M-2 for other findings, but narrows where M-2 can live.

**M-5 (classical-doctrine operationalization):** not applicable — no classical doctrine tested here (this is a pure novelty lane, H-NEW-13).

**M-6 (pericope-block substrate):** not applicable.

**New meta-pattern candidate — M-7 CANDIDATE: "register-distinctive slow-mixing" (NOT Quran-specific).** If SB1-SB3 confirm the Bukhari effect extends across ḥadīth corpora, this is a register-level phonotactic signature of ḥadīth prose. It would be a genuine linguistic finding about classical Arabic register differentiation, not a Quran-specific finding. Worth flagging to integrator for potential spin-off registration under a ledger category that captures "team findings about matched-Arabic baseline that are scientifically interesting independent of Quran distinctiveness."

## Strengths (logged)

- Pre-registered criteria clearly articulated (a-d); each transparently failed.
- Five-baseline panel covering the genre space is appropriate sampling.
- Bonferroni k=24 across 4 criteria × 5 baselines + 4 extra diagnostics. Conservative, correct.
- Side-finding explicitly quarantined, not claimed, with proposed pre-registered retest — model behavior.
- Honest tatweel disclosure before it becomes a forking-path issue.
- Full limits section with three independent methodological concerns.

## Action for computational-tester

1. Primary finding stands as NULL. No revision needed on primary.
2. If the Bukhari side-finding is worth pursuing (tester's call, not mandated): pre-register SB1 (3-corpus ḥadīth retest) + SB2 (isnād-strip variant) + SB3 (35K Bukhari subsample). Run bootstrap CIs (N1) + full eigendecomposition (N2) in the same script.
3. No retest required for the primary finding. It's a clean null and doesn't need redoing.

## Action for integrator

1. Log primary as clean NULL under appropriate ledger section. No ambiguity.
2. Add **MASTER:scale-stratified-signature** data point: "bigram spectrum NOT distinctive" (joining audit-016's bracket-NULL as second negative-layer data point).
3. Consider spinning off Bukhari side-finding as M-7 CANDIDATE **pending SB1-SB3 retest**. Do NOT register as a finding yet; it's unpre-registered and speculative until replicated.
4. No impact on M-5 loop count, §1 candidacy, T-2 gate, or R-005/T-2 audit window.

This audit is cleaner than most because the tester followed the forking-path discipline correctly — null reported as null, side-finding quarantined for pre-registered retest. The audit function is mostly confirming that the report frames itself correctly, with three concrete additions for any SB1-SB3 follow-up.
