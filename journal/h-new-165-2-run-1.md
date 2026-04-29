---
finding_id: h-new-165-2
run: 1
date: 2026-04-18
specialist: codex
seed: 20260419
prereg_sha256: 150c6cd4a3192f15d85cbca373c982e0beaef2fa81d46ed09189c678f4436eba
---

# H-NEW-165.2 run 1 journal

## Goal

Close audit-038's codebook-sensitivity requirement on the OQ-1
muqaṭṭaʿāt phonology result.

The locked question was:

**Do reasonable perturbations of the H-NEW-165 / H-NEW-232 phonological
codebook preserve both the primary cluster-level signal and the
singleton geometry?**

## Rules actually used

- Data: canonical 29 muq surahs, no tashkeel
- Parents: H-NEW-165 cluster predictor + H-NEW-232 singleton
  nearest-centroid propagation
- Codebooks: 4 locked variants only
- V0 baseline H-NEW-165 codebook
- V1 Watson-style modern voicing recode
- V2 strict throat-only pharyngeal recode
- V3 Holes-style `ḥāʾ/ʿayn` glottal makhraj recode
- Models: RF LOOCV + logistic LOOCV
- Singleton checks:
  RF singleton-task ceiling + H-NEW-232 nearest-centroid propagation
- Nulls: 1000 label permutations
- Bonferroni family: `k = 2`, `alpha_bon = 0.025`
- MW-5: `cheat_surah_id` reproduction check

No expansion beyond those locked variants.

## Execution

1. Verified the prereg and parent H-NEW-165 / H-NEW-232 artifacts.
2. Started the production script once from repo root.
3. Hit an existing-output / stale-process blocker from an earlier lane.
4. Identified a stale Python PID still holding the output path.
5. Terminated the stale process and reran the script cleanly.
6. Verified the landed JSON against the findings markdown.
7. Wrote this missing run journal.

Command used for the production rerun:

```bash
python3 scripts/h_new_165_2_codebook_sensitivity.py
```

The rerun completed cleanly and wrote the JSON already on disk.

## Result

**ROBUST.**

### Variant summary

| Variant | RF top-1 | Logistic top-1 | Primary p | Singleton matches | Singleton p | Verdict |
|---|---:|---:|---:|---:|---:|---|
| V0 baseline | 0.6552 | 0.6552 | 0.000999 | 8/10 | 0.02498 | PRESERVED-BOTH |
| V1 Watson voice | 0.6552 | 0.6552 | 0.000999 | 8/10 | 0.02198 | PRESERVED-BOTH |
| V2 strict pharyngeal | 0.6552 | 0.6552 | 0.000999 | 8/10 | 0.02498 | PRESERVED-BOTH |
| V3 Holes makhraj | 0.6552 | 0.6552 | 0.000999 | 8/10 | 0.02398 | PRESERVED-BOTH |

### What stayed invariant

- RF LOOCV ceiling stayed fixed at **19/29 = 0.6552**
- logistic LOOCV stayed fixed at **0.6552**
- all four multi-member classes stayed at per-class recall **1.0**
- RF singleton-task hits stayed at **0/8** in every variant
- nearest-centroid propagation stayed at **8/10** in every variant
- MW-5 `cheat_surah_id` stayed at **0.5172**

### Persistent singleton disagreements

The same two disagreements survive every codebook perturbation:

- **Q 36 YS -> HM**
- **Q 42 HMASQ -> TSM**

Those are the same two tensions already seen in H-NEW-232 and reinforced
by H-NEW-252.

## Interpretation kept tight

This run does **not** show that every phonological recoding would
preserve OQ-1.

It shows a narrower and still important claim:

**the H-NEW-165 / H-NEW-232 OQ-1 signal is stable across the exact
audit-required perturbation family.**

The surviving fragility is not in the codebook. It is in the classical
a-priori accepted-cluster assignment for two singletons.

## Limits logged during run

- Only 4 codebooks were tested.
- Each perturbation is small, touching at most a few letters.
- The a-priori accepted-cluster table itself was inherited from
  H-NEW-232.
- The 8-task RF singleton ceiling remains a methodological limitation,
  not a codebook result.

## Files landed

- Pre-reg: `findings/phase-b-hypotheses/h-new-165-2-codebook-sensitivity-prereg.md`
- Script: `scripts/h_new_165_2_codebook_sensitivity.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-165-2.json`
- Findings: `findings/phase-b-hypotheses/h-new-165-2-codebook-sensitivity.md`
- Journal: this file
