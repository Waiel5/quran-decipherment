---
id: H-NEW-1395
title: Ḥawāmīm 7-surah cluster Fisher-Rao cohesion on root-distribution
date_locked: 2026-05-09
phase: B
status: pre-registered
seed: 20260509
n_perm: 10000
---

# H-NEW-1395 — Pre-registration

## Hypothesis (DIRECTION-LOCKED before observation)

**H1**: The 7 consecutive ḥawāmīm-opener surahs C = {Q 40, 41, 42, 43, 44, 45, 46} are FR-COHESIVE on QAC root-distribution, i.e. mean intra-cluster Fisher-Rao distance d̄(C) is in the LOW tail of two independent null distributions.

Direction: d̄(C) ≤ null d̄ (one-tailed, lower).

## Theoretical motivation

The ḥawāmīm form the corpus-EXACT consecutive 7-block sharing a muqaṭṭaʿāt opening (حم). Classical scholars (Ibn Masʿūd via al-Suyūṭī *al-Itqān* nawʿ 17; Ibn ʿAbbās via Abū ʿUbayd *Faḍāʾil al-Qurʾān*) treat the ḥawāmīm as a thematic unit (*dībāj al-Qurʾān*, "the brocade of the Qurʾān"). Lessons from H-NEW-1301 (IMPV-qrA cluster, PC failed) and from cross-finding-025 (marker-thickness rule) caution: muqaṭṭaʿāt-axis cohesion does NOT automatically imply FR-root-distribution cohesion. This test asks whether HM-7 specifically meets the FR-axis threshold.

## Pre-committed measurement protocol

- Tashkeel: no-tashkeel (rules-tuple §1.4 default).
- Token: QAC stem-root (per H-NEW-111 protocol).
- Distance: Fisher-Rao on root-probability vectors as in H-NEW-111.
- Reading: Hafs-Kufan.
- Basmala: counted only in Q 1.

**Test statistic**: d̄(C) = mean of all C(7,2) = 21 pairwise FR distances from H-NEW-111 D-matrix.

## Null distributions (Bonferroni family k=2 cells)

**Cell A — uniform 7-of-114 null**: 10,000 random 7-tuples from {1..114}; compute d̄; report p_A = #{null ≤ obs} / 10000.

**Cell B — length-matched null**: 10,000 random 7-tuples whose summed verse-count is within ±20% of HM-7's total (Q 40-46 verse total = 85+54+53+89+59+37+35 = 412). Report p_B.

α corrected: 0.05 / 2 = **α_Bonf = 0.025**.

## MW-5 replication / positive-control (PC)

PC pool: H-NEW-1190 cluster (used as positive control by Wave-H precedent; matches H-NEW-1340 PC discipline).

Operationalization: take a sub-sample of 4 surahs from H-NEW-1190's 10-member adraka-mā cluster {Q 69, 74, 77, 82, 83, 86, 90, 97, 101, 104}. Sampled via random.Random(SEED).sample(pool, 4) for determinism. PC d̄ should be in lower tail of uniform-7 null (one-tailed p_PC ≤ 0.05) to validate the FR-cohesion instrument on a known cohesive cluster.

If PC fails: result published as NULL-BROKEN (instrument unreliable on this PC); main verdict deferred.

## Verdicts

| Outcome | Cells | PC | Verdict |
|:--|:--|:--|:--|
| Both A and B pass at α=0.025 | A ✓, B ✓ | PC ✓ | PASS-DIRECTED |
| A passes, B fails | A ✓, B ✗ | PC ✓ | DESCRIPTIVE-ONLY (length-confounded) |
| A fails, B passes | A ✗, B ✓ | PC ✓ | PARTIAL |
| Both fail | A ✗, B ✗ | PC ✓ | NULL |
| PC fails | — | PC ✗ | NULL-BROKEN |

## Pre-commit violations and stop conditions

- If d̄(C) > null mean of either cell (i.e., HIGHER mean distance than random): pre-commit violation → publish as NULL with explicit reverse-direction note.
- If MW-5 PC sub-sample is changed after observation: violation; mark RETRACTED.
- Sub-sample of H-NEW-1190 is fixed by seed; no re-rolling.

## Constants

```
SEED   = 20260509
N_PERM = 10_000
CLUSTER = [40, 41, 42, 43, 44, 45, 46]
ADRAKA  = [69, 74, 77, 82, 83, 86, 90, 97, 101, 104]
PC_K    = 4
LENGTH_TOLERANCE = 0.20
```

## Data dependencies

- `findings/phase-b-hypotheses/csv/h-new-111.json` — 114×114 FR-roots distance matrix
- `quran-text/quran-no-tashkeel.json` — verse counts for length-matched cell B

## Output schema

`findings/phase-b-hypotheses/csv/h-new-1395.json`:
```
{
  "id": "H-NEW-1395",
  "title": "...",
  "prereg_sha": "<computed at runtime>",
  "seed": 20260509,
  "n_perm": 10000,
  "cluster": [40..46],
  "obs": float,
  "cell_A": {"p": ..., "null_mean": ..., "null_p5": ..., "pass": bool},
  "cell_B": {"p": ..., "null_mean": ..., "null_p5": ..., "pass": bool, "n": int},
  "MW5_PC":  {"subsample": [...], "pc_obs": ..., "p_pc": ..., "pass": bool},
  "verdict": "...",
  "alpha_bonf": 0.025
}
```

## Honest limits

1. The ḥawāmīm share a single-letter-axis marker (حم). Per cross-finding-025, a single thematic marker is necessary-not-sufficient for FR-cohesion. This is a TEST of that boundary on a known canonical sub-cluster.
2. Q 41 is named *Fuṣṣilat* (NOT ḥā-mīm-X), reflecting that classical tradition itself sometimes treats HM as a heading rather than the surah's identity. The cluster definition is mushaf-positional + muqaṭṭaʿāt-marker.
3. H-NEW-570 already found HM-7 at 20.90%ile FR-cohesion (moderate-only). H-NEW-1395 is the formal direction-locked Bonferroni-corrected test of that finding.

*Locked 2026-05-09. Direction one-tailed lower. SHA to be computed and embedded post-write.*
