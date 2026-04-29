---
id: H-NEW-42
title: Reverse-Direction Structural Fragility — result
phase: B
status: NULL-BROKEN (per MW-5 direct-Muʿallaqāt positive control) with EXPLORATORY-REVERSE observation
date: 2026-04-15
agent: h-new-42-specialist (run-1)
pre_reg: findings/phase-b-hypotheses/h-new-42-reverse-direction-fragility-prereg.md
amendments_applied: [42-A, 42-B, 42-C]
bonferroni_family: 2026-04-15-Fresh-Wave-3
alpha_bon: 0.0167
alpha_cell: 5.566666...e-3
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
primary_corpus: quran-text/quran-no-tashkeel.json
raw_json: findings/phase-b-hypotheses/csv/h-new-42.json
script: scripts/h_new_42_reverse_fragility.py
seed: 20260415
runtime_seconds: 4006
---

# [[h-new-42-reverse-direction-fragility|H-NEW-42]] — Reverse-Direction Structural Fragility (result)

## Verdict

**NULL-BROKEN** by the strict MW-5 positive-control criterion applied to the direct (unpartitioned) Muʿallaqāt-vs-Jāḥiẓ comparison. Under this gate, no Quran claim is interpretable.

A secondary result is that, ignoring the positive-control gate, the Quran's forward-minus-reverse fragility is **LESS** than all three baselines — i.e., OPPOSITE to the pre-registered direction. Per PRE-REG-STANDARD-01, this cannot be upgraded without an independent follow-up pre-reg (H-NEW-42.1); it is filed as **EXPLORATORY-REVERSE**.

## Result table

| Corpus | Null mean fragility | Null std | Quran delta | One-sided p (Quran > baseline) | α_cell = 5.57e-3 |
|---|---|---|---|---|---|
| Quran | **2.78e-4** (mean), 4.46e-5 (median) | — | — | — | — |
| Bukhārī (partitioned) | 3.50e-4 | 6.41e-5 | Quran − Bukh = **−7.3e-5** | 0.871 | does NOT pass |
| Jāḥiẓ (partitioned) | 3.28e-4 | 5.81e-5 | Quran − Jāḥ = **−5.0e-5** | 0.795 | does NOT pass |
| Muʿallaqāt (partitioned) | 3.39e-4 | 6.28e-5 | Quran − Muʿ = **−6.1e-5** | 0.828 | does NOT pass |

Quran fragility is LOWER than every baseline; the pre-registered one-sided p-value is near 0.8–0.9 for all three, consistent with the reverse-direction signal.

## MW-5 positive control

The pre-reg specified: Muʿallaqāt (rhymed poetry, strongly order-constrained) should show fragility > Jāḥiẓ (prose). Two natural operationalisations diverge:

| Comparison | Muʿallaqāt fragility | Jāḥiẓ fragility | Muʿ > Jāḥ? |
|---|---|---|---|
| Direct (7 real Muʿallaqāt, verse-level) | **1.33e-5** | 3.28e-4 (partitioned) | **FAIL** |
| Partitioned (both split into 114 Quran-length-matched pseudo-surahs) | 3.39e-4 | 3.28e-4 | PASS (barely) |

The direct comparison FAILS the MW-5 expectation because real Muʿallaqāt poems are very short (avg ~70 verses), and the 6-axis fragility score is length-normalised by 1/√n; short signals produce small Δ regardless of structure. This is a pre-registered-threshold failure, not a latent-signal failure. Per the strict MW-5 gate, the verdict is **NULL-BROKEN**.

The partitioned comparison passes the MW-5 expectation but by a tiny margin (3.39e-4 vs 3.28e-4). It does not dissolve the NULL-BROKEN status because both the pre-reg and amendment 42-A enforce the stricter reading: positive control must pass unambiguously.

## Synthetic positive control

Forward-ordered Quran vs verse-shuffled Quran (within-surah): shuffled mean fragility = 2.86e-4 vs forward = 2.78e-4, delta = -7.8e-6. The shuffle provides a LESS strict expectation than Muʿallaqāt and is within 3% of forward — suggesting the 6-axis fingerprint is not especially sensitive to verse-order changes in the Quran.

## The EXPLORATORY-REVERSE observation

Under the assumption that the pipeline is sound (partitioned positive control passed, synthetic control consistent), the signed result is that **Quran reverses more gracefully than Bukhārī, Jāḥiẓ, or Muʿallaqāt**. Three readings:

1. **Pipeline weakness (most likely).** The f₂ axis was substituted from transformer embeddings to a char-trigram Jaccard proxy due to unavailable local model (per amendment 42-C garden-of-forking-paths entry). This weakens semantic-drift sensitivity, which is the most order-sensitive axis by construction. Under-captured f₂ could invert the apparent direction of the whole Δ-comparison. A re-run with true Arabic embeddings (H-NEW-42.2, queued) is the appropriate disambiguation.

2. **Symmetry / ring-structure.** Classical al-Biqāʿī *Naẓm al-Durar* documents verse-by-verse forward *munāsaba* (coherence) — but Cuypers (2007) and Farrin (2014) document RING structure in the Quran (center-symmetric). A ring-structured surah would be LESS fragile to reversal than a linear-progression surah because the same structure survives from the other end. The Quran having lower-than-prose reversal fragility could be interpreted as supporting intermediate ring-like structure more than linear-argument structure. Classical balāgha has both positions (al-Biqāʿī linear vs Cuypers/Farrin ring).

3. **Length-normalisation artefact.** The fragility score divides by √n_verses. Short surahs with zero-variance fingerprints (Q 106 Quraysh, Q 108 Kawthar, Q 112 Ikhlāṣ — all report fragility = 0.0) drag the Quran mean DOWN relative to baselines that have no surah-length equivalent of 3–4 verse sequences. 114-pseudo-surah baselines were constructed with Quran-length-matching, but the ultra-short Quran surahs may still shift the distribution asymmetrically.

All three readings are plausible; this finding cannot distinguish among them without a re-run.

## Most and least fragile surahs (for reference; under disqualified null)

Most fragile (top 3): **Q 111 (al-Masad, 5 verses, Δ=4.71e-3), Q 110 (al-Naṣr, 3 verses, Δ=2.41e-3), Q 95 (al-Tīn, 8 verses, Δ=1.94e-3).**

Least fragile (top 3, all Δ=0.0): **Q 106 (Quraysh), Q 108 (al-Kawthar), Q 112 (al-Ikhlāṣ).**

Interpretation caveat: these are the extremes under the (disqualified) length-normalised score. The zero-fragility cluster for Q 106 / 108 / 112 is an artefact of verses being so short that all 6 fingerprint axes are constant-valued (one rhyme-class, zero divine-names, etc.), giving F(S) = F(S') by construction.

## Integrity-layer compliance

| Check | Status |
|---|---|
| Pre-reg locked 2026-04-15 | YES |
| Amendments 42-A, 42-B, 42-C applied pre-execution | YES |
| Muʿallaqāt pool SHA-256 logged | YES (`d97ce767…7e0300`) |
| Bukhārī/Jāḥiẓ SHA-256 logged | YES |
| Quran JSON SHA-256 logged | YES |
| Direction pre-registered, sign-flip not upgraded | YES — EXPLORATORY-REVERSE per PRE-REG-STANDARD-01 |
| Bonferroni k=3, α_bon=0.0167 declared before null | YES |
| f₂ proxy substitution disclosed via garden-of-forking-paths | YES (embedded in pre-reg as GoFP entry 2026-04-15) |
| MW-5 positive control specified and checked | YES (direct FAIL, partitioned PASS) |
| MW-7 internal-error gate | PASS |

## Reconciliation with other findings

- **[[h-new-34-1-under-dispersion|H-NEW-34.1]] reverse-signal (verse-final abjad under-dispersion)** — direction sign-consistent with this result: Quran is LESS dispersed / LESS fragile than prose across the axis probed. Two independent axes (abjad-residue under verse-final-word shuffling vs. 6-axis-fingerprint under verse-order reversal) both point to Quran being *smoother* than matched Arabic, not more structured. Cross-reference: `findings/phase-b-hypotheses/h-new-34-1-under-dispersion.md`.
- **[[h-new-43-verse-length-fft|H-NEW-43]] verse-length FFT null** — direction-consistent: Quran's AR(1) fit to verse-length is 15–20× better (closer to white noise) than Bukhārī/Jāḥiẓ/Muʿallaqāt. Again the Quran is less spectrally structured than prose at that axis.
- The emerging pattern across [[h-new-34-1-under-dispersion|H-NEW-34.1]] / [[h-new-42-reverse-direction-fragility|H-NEW-42]] / [[h-new-43-verse-length-fft|H-NEW-43]] is that the Quran is *smoother and less rhythmically/positionally structured than matched-Arabic baselines* at three orthogonal probes. This is either (a) an artefact of length-normalisation across three different axes, or (b) a substantive signal that the Quran's compositional register is deliberately *less* rhythmically-regular than prose or poetry — a specific expectation of the "unique literary register" (naẓm) tradition. Route to synthesis-layer meta-analyst for cross-finding cluster ruling.

## Follow-up pre-regs

- **H-NEW-42.1** — independent pre-reg to test the REVERSE direction (Quran LESS fragile than baselines). Required by PRE-REG-STANDARD-01 before any upgrade of this direction. Not yet filed.
- **H-NEW-42.2** — rerun with true Arabic transformer embeddings for f₂ (requires local model download). Queued pending model availability.
- **H-NEW-42.3** — ring-structure vs linear-progression decomposition of the fragility-axis-wise Δ; would test reading (2) above against the length-normalisation reading (3).

## Prior art

- Cuypers, M. (2007) *Le Festin*, Lethielleux — ring structure in Sūrat al-Māʾida; documents reading where reverse and forward are symmetry-bound
- Farrin, R. (2014) *Structure and Qur'anic Interpretation* — chapter-level concentric structure
- al-Biqāʿī, *Naẓm al-Durar* — 22-volume linear-forward munāsaba (MW-6 VERIFIED as corpus)
- No published statistical test of reverse-direction structural fragility against matched-Arabic baselines. Closest published work is autocorrelation-only (H-NEW-35 length autocorrelation).

## Honest summary

The test is NULL-BROKEN. The pre-registered direction (Quran MORE fragile) does not hold; the Quran is directionally LESS fragile than all three baselines, which is the OPPOSITE signed observation. This cannot be promoted to a finding under the pre-reg. The observation is queued as EXPLORATORY-REVERSE and routed to H-NEW-42.1 (new pre-reg, reversed-direction hypothesis) for rigorous confirmation.

The emerging triple ([[h-new-34-1-under-dispersion|H-NEW-34.1]] + [[h-new-42-reverse-direction-fragility|H-NEW-42]] + [[h-new-43-verse-length-fft|H-NEW-43]] all showing Quran-smoother-than-prose) is now the highest-priority meta-analysis target.
