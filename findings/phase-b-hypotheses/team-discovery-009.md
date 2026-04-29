---
finding_id: team-discovery-009
phase: B
status: REFUTED (pre-registered direction) / NOTABLE ANTI-SIGNAL
date: 2026-04-12
rules_tuple: (no-tashkeel, orthographic-token & lemma, QAC roots, counted-only-in-surah-1, hafs-kufan, mashriqi)
null_model: within-pair random side-assignment (10,000 permutations) + binomial p=0.5
bonferroni_k: 3 (binomial, frac-yes perm, mean-delta perm)
pre_registration: scratch/team-discovery/h_new_kirmani_directionality.py (seed 20260413)
classical_claim: al-Kirmānī (d. ~500 AH), *al-Burhān fī mutashābih al-Qurʾān*
author: computational-tester
---

# H-NEW-18 — al-Kirmānī directionality of mutashābih pairs

## Classical claim

al-Kirmānī's *al-Burhān fī mutashābih al-Qurʾān* argues that when two mutashābih verses differ (here: in length), the variation is **not arbitrary**: the LONGER variant lives in the surah whose thematic fabric requires the extra material. If true, the longer variant's host surah should be more saturated in the shared roots than the shorter variant's host — the surah "needs" the extra elaboration because it is already densely committed to those roots.

## Operationalization

For each pair in the 265-entry *mutashābih* catalog where:
  - `len1 ≠ len2` (directional pair)
  - pair spans two different surahs
  - shared root-set `R = roots(v1) ∩ roots(v2)` has `|R| ≥ 2`

compute R-density in each host surah:
  `density(S, R) = |tokens ∈ S with root ∈ R| / |tokens ∈ S|`

Directional prediction: `density(S_long, R) > density(S_short, R)`.

Null: within-pair random side assignment (10,000 permutations).

## Result — REFUTED in pre-registered direction

| Quantity | Value |
|---|---|
| Usable pairs | 73 (from 265 total; 192 same-length or same-surah) |
| Fraction supporting al-Kirmānī (yes) | 32/73 = **43.8%** |
| Binomial one-sided p (≥ 50%) | **0.879** |
| Mean density delta (long − short) | **−0.0199** |
| Permutation z (frac_yes) | −1.06 |
| Permutation z (mean_delta) | **−2.43** |
| Permutation p (mean_delta) | 0.992 (right-tail) |

The pre-registered direction is **refuted**. 41 of 73 pairs run **opposite** to al-Kirmānī's prediction.

## Anti-signal (reported for completeness)

The mean-delta permutation z is **−2.43**, corresponding to a two-sided p ≈ 0.015. Under Bonferroni k=3, this sits at α_bon = 0.0167 — *just* significant two-sided.

Interpretation: the data shows a weak but real *anti*-Kirmānī signal — the LONGER mutashābih variant tends to sit in the surah with LOWER shared-root density. This is not a pre-registered finding and should not be treated as one.

## Sympathetic reading (not a claim)

One could salvage al-Kirmānī by flipping the operationalization:

> A surah that has *already densely* covered a set of roots doesn't need the longer elaboration at the mutashābih moment. A surah that uses those roots *sparsely* elsewhere benefits from the fuller statement.

Under this flipped logic, the observed negative sign is consistent with al-Kirmānī's *spirit* (intentional directionality) while contradicting the simple "longer goes with denser" literal reading. But this is post-hoc and would need a separate pre-registration to test.

## Verdict

- Pre-registered al-Kirmānī thesis (longer = denser host): **REFUTED**, p=0.879.
- Opposite direction (longer = sparser host): significant at raw p=0.015, marginal at Bonferroni-k3.
- The weak anti-signal is notable but not claimable as a pre-registered finding.

## Limits

1. Only 73 usable pairs — low power.
2. "Host surah R-density" is one of several possible operationalizations; lexical-thematic need could also be measured via root-cooccurrence graph centrality, tafsir-annotated theme tags, or the Bazargan-style structural fingerprint.
3. The mutashābih catalog itself has selection effects (which pairs were flagged as "similar enough" by the upstream tool).
4. `|R| ≥ 2` filter may bias toward short shared sets where signal is noisy.

## Garden of forking paths (disclosed)

- Chose `|R| ≥ 2` threshold a priori (before looking at results).
- Excluded same-surah pairs a priori (host-identity makes test undefined).
- Three tests reported (binomial, frac-yes perm, mean-delta perm) with Bonferroni k=3 applied a priori. No post-hoc selection.
- Did NOT change the operationalization after seeing the negative result — the flipped reading is disclosed as *speculative*, not claimed.

## Files

- Script: `scratch/team-discovery/h_new_kirmani_directionality.py`
- Output: `scratch/team-discovery/result-kirmani-directionality.json`
- Input: `findings/phase-b-hypotheses/mutashabih-pairs.csv`
- Morphology: `data/morphology/quranic-corpus-morphology-0.4.txt`
