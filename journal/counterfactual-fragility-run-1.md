---
title: counterfactual-fragility run 1
date: 2026-04-12
agent: counterfactual-fragility-run-1
seed: 20260413
n_samples: 1000
runtime_seconds: 7.8
---

# Counterfactual fragility — run log

## What

Executed pre-registered Test 2 from `findings/TOMORROW-TESTS-PRE-REGISTRATION.md`:
per-word counterfactual fragility of the Quran under morphology-preserving
synonym replacement, vs matched-Arabic baseline. n=1000 positions per
corpus, k=3 synonyms per position, 6-axis chapter fingerprint.

## Key numbers

- Quran mean fragility: 0.0292 (n=985)
- Pooled baseline mean fragility: 0.0564 (n=1779)
- **z = -4.860**
- Verdict: **REVERSE**

## Per-baseline

- bukhari: n=386 mean=0.0188 z=+4.063
- jahiz-hayawan: n=496 mean=0.0152 z=+5.961
- muallaqa-imru-al-qais: n=90 mean=0.3047 z=-8.767
- muallaqa-labid: n=130 mean=0.1844 z=-2.586
- muallaqa-zuhayr: n=79 mean=0.1470 z=-4.627
- muallaqa-antara: n=121 mean=0.0550 z=-4.705
- muallaqa-tarafa: n=162 mean=0.0327 z=-0.786
- muallaqa-harith: n=170 mean=0.0268 z=+0.601
- muallaqa-amr-bin-kulthum: n=145 mean=0.0420 z=-3.252

## Per-axis (Quran / pooled baseline mean normalized Δ)

- rhyme: 0.0304 / 0.0099
- hapax_end: 0.0257 / 0.0278
- divine_name: 0.0150 / 0.0764
- gzip: 0.0197 / 0.0467
- palindrome: 0.0167 / 0.0524
- saj: 0.0675 / 0.1256

## Robustness

Dropping divine-name axis: Quran 0.0320 / baseline 0.0525, z=-5.185

## Notes

- Morphology lookup worked for 995/1000 Quran positions. Rest fell back to shape-bucket sampling from Quran.
- Baseline corpora used: ['bukhari', 'jahiz-hayawan', 'muallaqa-imru-al-qais', 'muallaqa-labid', 'muallaqa-zuhayr', 'muallaqa-antara', 'muallaqa-tarafa', 'muallaqa-harith', 'muallaqa-amr-bin-kulthum'].
- Seed 20260413, deterministic across reruns.

## Outputs

- `findings/phase-b-hypotheses/counterfactual-fragility.md`
- `findings/phase-b-hypotheses/csv/counterfactual-fragility-quran-positions.csv`
- `findings/phase-b-hypotheses/csv/counterfactual-fragility-summary.csv`
