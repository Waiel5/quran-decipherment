---
finding_id: Q024-F-05
title: "Q 24 nūr-root density rank in the corpus"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: 10000
bonferroni_k: 4
alpha_raw: 0.05
alpha_bonferroni: 0.0125
direction: Q 24 rank ≤ 3 by raw nwr-token count AND by density-among-attesting-surahs
---

# Q024-F-05 — *nūr* root density rank in Q 24 vs the corpus

## Hypothesis (LOCKED before observation)

Q 24 al-Nūr is named for the *āyat al-nūr* (Q 24:35) and contains the corpus's most-developed light-parable. The empirical prediction is that Q 24 ranks among the top three of all 114 surahs on the QAC root *nwr* (نور / نار, light / fire — QAC joint lemmatization).

This pre-reg is narrower than Q024-F-01 (which used a 16-root light-cluster). Q024-F-05 isolates the single root *nwr* and tests rank directly, not significance.

## Metrics (LOCKED)

Two parallel metrics are pre-registered. Both must be inspected; the test fails if either direction is violated.

**Metric A — raw *nwr* token count rank.**
- Compute the *nwr* token count per surah using `data/morphology/root-index.json` key `nwr`.
- Rank all 114 surahs descending by count; ties broken alphabetically (lower surah-ID first).
- Q 24 rank-A is the position in this ranking.
- Pre-registered prediction: **rank-A ≤ 3**.

**Metric B — *nwr* density rank among surahs with ≥ 3 *nwr* attestations.**
- Density = `count / total_words` where `total_words` is the per-surah no-tashkeel orthographic-token count (excluding basmala in surahs 2–114, excluding mushaf-marks ۞ ۖ ۗ ۚ ۛ ۜ).
- Filter to surahs with ≥ 3 *nwr* attestations (this excludes the singleton short surahs whose 1-token-in-30-words denominator artificially inflates density).
- Rank descending by density.
- Q 24 rank-B is the position in this filtered ranking.
- Pre-registered prediction: **rank-B ≤ 3**.

The ≥ 3 filter is justified BEFORE observation: any single-attestation in a 23-word surah trivially out-ranks any 9-attestation surah of 1300 words on raw density, even though the latter is structurally embedded in light-vocabulary while the former is incidental. The ≥ 3 floor is the smallest non-trivial repeated attestation.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-stem-roots, QAC v0.4 morphological annotations, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`

Light-and-fire joint lemmatization: the QAC convention groups *nūr* (light) and *nār* (fire) under the same root *nwr*. This pre-reg uses the joint convention. A future variant could split them, but that variant is OUT OF SCOPE for this finding.

## Direction (LOCKED)

The direction is rank-low (i.e., Q 24 in the top-3 most-concentrated by *nwr*). Reversed direction = Q 24 rank > 3 on either Metric A or Metric B = pre-commit violation, NULL.

## Success criteria

- Both Metric A and Metric B ≤ 3: **CONFIRMED**.
- One of Metric A, B ≤ 3; the other 4–7: **DIRECTIONAL** with the failed metric reported.
- Both > 3: **NULL**.

## Failure / NULL criteria

- Either Metric A > 3 or Metric B > 3: NULL with prominence.
- The pre-reg explicitly forbids substituting alternative metrics (e.g., per-letter density, per-verse density) after observation. If the locked metrics fail, the test fails.

## Bonferroni correction

This is one of 4 pre-registered tests in the 2026-05-09 wave (Q024-F-05..F-08). α_corrected = 0.05 / 4 = 0.0125. However, this test is a rank test, not a p-value test; the Bonferroni correction is recorded for the family of 4 but does not modify the rank threshold.

## Honest limits (pre-registered)

- The single-root *nwr* is a narrow definition. The broader light-cluster (16 roots) is Q024-F-01's domain.
- QAC's joint *nūr* / *nār* lemmatization affects this test: Q 24 has 9 *nwr*-tokens of which 2 are *nār* (fire) tokens. If split, Q 24's *nūr*-only count drops to 7; surah rankings would shift modestly.
- Rank ties are broken alphabetically; this is unlikely to affect the rank-3 prediction unless rank 3 / 4 are tied at exactly the same count or density.

## Seed

20260509

## Pre-registration SHA256

Computed at write-time; embedded in `Q024_F_05_nur_root_density_rank.py` and verified at runtime.
