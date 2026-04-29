---
finding_id: h-meta-2-null-comparator
phase: C
status: BOTH_DISQUALIFIED (pre-registered outcome — Markov-surprise family needs a third null spec)
date: 2026-04-13
seed: 20260413
pre_registration_reference: scripts/h_meta_2_null_comparator.py (header-locked)
bonferroni_k: 2 (per null spec; calibration window [0.005, 0.02] at α_nominal=0.01)
script: scripts/h_meta_2_null_comparator.py
output_json: findings/phase-c-structures/csv/h-meta-2-null-comparator.json
---

# H-META-2 — Null-model comparator for the Markov-surprise family

## Executive verdict

**BOTH_DISQUALIFIED.** Both null specifications used throughout the Markov-surprise family of tests (H-NEW-1, H-NEW-1-v2, and derivatives) fail pre-registered calibration on independent classical Arabic corpora. Neither can be relied on for the Markov-surprise family in future work.

Pre-registered fourth-branch verdict reached per header-locked decision table: *"BOTH_DISQUALIFIED → Markov-surprise family needs a third null spec."*

## Pre-registered design (header-locked in script before data loaded)

**Null-A (ORIGINAL, team-discovery-001 primary):** label-permutation on verse-class (break vs conform) × residual-Markov-surprise. Markov model stays fixed; labels shuffled; residual mean difference recomputed.

**Null-B (AUDIT, h_new_1_v2_rhyme_robust):** Markov-trained surrogate. Character-level permutation across verses within pool, re-fit the Markov model on the permuted data, recompute gap.

**Independent corpora (locked before null-spec application):**
- PRIMARY: al-Mutanabbī Dīwān (strict-rhymed classical poetry, 919 lines loaded)
- SECONDARY: al-Jāḥiẓ *Kitāb al-Ḥayawān* (classical prose, partial sajʿ, 61,064 segments → subsampled to 3,000)

**Pre-registered acceptance windows:**
- Calibration (H-META-2-a): null passes if Type-I reject rate at nominal α=0.01 (two-sided) falls in **[0.005, 0.02]** over B=1000 random rhyme-set draws.
- Power (H-META-2-b): null with smaller |recovered_z − planted_σ| deviation at σ ∈ {0.5, 1.0, 2.0} is preferred.

**Pre-registered decision table** (in script header):
- Exactly one null calibrates on both → NULL_A_PREFERRED or NULL_B_PREFERRED
- Both calibrate on both → tie-break on power-deviation
- Neither calibrates → **BOTH_DISQUALIFIED; family needs a third null spec**

## Results — calibration (H-META-2-a, B=1000)

### Mutanabbī

| Null | Reject rate @ α=0.01 | In-window [0.005, 0.02]? | Mean z | SD z | Max \|z\| |
|---|---:|:-:|---:|---:|---:|
| Null-A (label-perm) | **0.693** | ✗ | −1.15 | 5.11 | 14.30 |
| Null-B (Markov-retrain) | **0.620** | ✗ | −2.26 | 4.88 | 17.41 |

### Jāḥiẓ

| Null | Reject rate @ α=0.01 | In-window [0.005, 0.02]? | Mean z | SD z | Max \|z\| |
|---|---:|:-:|---:|---:|---:|
| Null-A (label-perm) | **0.651** | ✗ | −0.76 | 5.26 | 16.83 |
| Null-B (Markov-retrain) | **0.720** | ✗ | −3.62 | 4.48 | 14.64 |

Both nulls over-reject at **30–70× the nominal α rate** on both independent corpora. The z-score SD is ~5× what a well-calibrated null should produce (SD z should be ~1 for calibrated z). Mean z drifts negative — the null is biased toward over-inflating test-statistic magnitudes.

Both disqualified on both corpora. Pre-registered calibration gate failed 4/4.

## Results — power recovery (H-META-2-b)

Planted-signal effect size σ ∈ {0.5, 1.0, 2.0} via per-verse-end-character flip probability at break-class verses; rhyme set بتدرسقكلمن (5 letters) pinned.

### Mutanabbī — deviation of recovered_z from planted_σ

| Planted σ | Null-A recovered z | Null-B recovered z | Dev(A) from σ | Dev(B) from σ |
|---:|---:|---:|---:|---:|
| 0.5 | −7.92 | −2.74 | 7.42 | 2.24 |
| 1.0 | −7.21 | −2.18 | 6.21 | 1.18 |
| 2.0 | −5.80 | −2.26 | 3.80 | 0.26 |

### Jāḥiẓ

| Planted σ | Null-A recovered z | Null-B recovered z | Dev(A) from σ | Dev(B) from σ |
|---:|---:|---:|---:|---:|
| 0.5 | −5.47 | **+4.74** | 4.97 | 4.24 |
| 1.0 | −4.12 | **+4.83** | 3.12 | 3.83 |
| 2.0 | −3.07 | **+6.69** | 1.07 | 4.69 |

**Null-B on Jāḥiẓ recovers the planted signal with the WRONG SIGN** (positive z where a negative planted effect was injected). This is not just mis-calibration — it is directionally wrong. The Markov-retrain null on short-rhyme-set Jāḥiẓ segments picks up the sign of the Markov-model refit noise, not the planted effect.

Null-A is directionally correct but magnitudes-off by 3–7σ at small planted effects. Null-B is directionally correct on Mutanabbī (always negative matching planted), but magnitudes are far below planted (at σ=1 planted Null-B recovers only |z|=2.2, effectively under-powering).

Neither null would reliably detect or correctly magnitude a true 1σ structural signal on either independent corpus.

## Interpretation

The Markov-surprise family's two workhorse nulls both break on independent classical Arabic:

1. **Null-A (label-permutation with fixed Markov model):** massively over-rejects because residualization is computed once on full data; under shuffled labels, the residual variance structure is wrong, producing artificially narrow null distributions and inflated z.

2. **Null-B (character-permutation + Markov retrain):** over-rejects on Mutanabbī with sign preserved, but on Jāḥiẓ flips sign. The retrain step on short sample sizes picks up refit variance that dominates the planted signal.

This means every Markov-surprise family test result — including H-NEW-1 (verse-ending consonant Markov-residual, COMPLETED) and H-NEW-1-v2 (rhyme-break Markov residual with robustness checks, COMPLETED) — has been reported with a null-model whose Type-I rate at α=0.01 is actually ~0.65. **Their published z-scores are not reliable.**

A third null spec is required. Candidates for Phase-D or follow-up work:
- **Null-C (matched-pair bootstrap):** resample matched-length matched-script character pairs from the same corpus, rebuilding empirical surprisal from bootstrap draws.
- **Null-D (rate-matched parametric):** fit a first-order Markov on the full pool, then parametrically simulate break/conform distributions from that model, no refitting.
- **Null-E (segment-shuffle with fixed overall bigram distribution):** preserve marginal statistics while destroying position-conditional structure.

None of these are pre-registered; proposing them for hypothesis-generator to formalize.

## Impact on existing findings

| Finding | Null used | Status after H-META-2 |
|---|---|---|
| H-NEW-1 | Null-A | Z-score interpretation weakened; raw descriptive comparison preserved |
| H-NEW-1-v2 (6-axis robustness) | Null-A + Null-B | Both nulls mis-calibrated; six robustness axes all affected |
| Any H-NEW using residual-Markov-surprise | Null-A | Same |

Note: **the descriptive finding** (Quran verse-endings have different Markov-surprise profile than matched-Arabic) likely stands as a real pattern — z-magnitudes are unreliable but the rank-order of Quran vs baselines is observable without null-based significance. But any publication-grade claim tied to specific α-levels should be re-run under a calibrated null.

## Routing

- **Integrator:** file H-META-2 under §3d STAGED subsection alongside H-NEW-34.1. When auditor releases, migrate to §3c team-discovery as a methodological finding (not a Quran finding).
- **Hypothesis-generator:** task intake — propose Null-C/D/E spec for Markov-surprise family.
- **Ledger:** H-NEW-1 and H-NEW-1-v2 main findings flagged with a ⚠️ note referencing this H-META-2 result. Descriptive patterns preserved; z-magnitude claims flagged.
- **H-META-1 cross-reference:** H-META-2's result is *methodological mis-calibration of a null spec*, whereas H-META-1's result is *predictable signature of claim metadata*. Independent findings; both stand.

## Limits

1. **B=1000 calibration draws.** Pre-registered as sufficient; gives SE on reject-rate ≈ √(0.65·0.35/1000) ≈ 0.015. The observed rates (0.62–0.72) are ~30σ outside the nominal 0.01, so B is not the bottleneck.

2. **Rhyme-set construction.** Random 5-letter subsets of the 28-letter Arabic alphabet. Different rhyme-set sizes (3 or 7) might produce different calibration profiles — not pre-registered.

3. **Jāḥiẓ subsampled to 3000 segments** for compute. With full 61k segments, the Null-B sign-flip on Jāḥiẓ might disappear or worsen — sample-size sensitivity untested.

4. **Two corpora is the minimum.** A third independent corpus (e.g. Bukhari, Muʿallaqāt) would strengthen the disqualification, but for the pre-registered decision table only the first two are binding.

5. **No Phase-C re-run of H-NEW-1 family under a calibrated null is attempted here.** That is a follow-up task, not this one.

## Garden of forking paths (disclosed)

- Pre-registration locked in the script header (lines 1-53) before any corpus load or null-spec application.
- Calibration window [0.005, 0.02] locked a priori (2× tolerance around nominal α=0.01).
- B=1000 draws pre-specified, not adjusted to observed calibration rate.
- No post-hoc re-examination of which null is "less bad" — pre-registered decision-table only has three branches, and BOTH_DISQUALIFIED is one of them.
- Jāḥiẓ subsample size 3000 pre-specified.

## Reproducibility

- Script: `scripts/h_meta_2_null_comparator.py` (header-locked pre-registration)
- Seed: 20260413
- Output JSON: `findings/phase-c-structures/csv/h-meta-2-null-comparator.json`
- Run time: ~26 minutes (single-threaded Python, 61k Jāḥiẓ load + 1000+200 calibration draws per null per corpus + 3 power cells per corpus per null)
