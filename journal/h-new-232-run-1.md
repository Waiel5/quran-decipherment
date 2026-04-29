---
id: H-NEW-232
run: 1
date: 2026-04-17
agent: h-new-232-autonomous
parent: H-NEW-165
seed: 20260419
verdict: PASS-COHERENT
---

# H-NEW-232 run 1 — journal

## Task

Break the LOOCV singleton-barrier of H-NEW-165 by re-framing OQ-1 singletons as a **cross-class nearest-neighbor interpretation** problem rather than a multi-class classification problem. Given the 15-dim classical-tajwīd feature vector locked in H-NEW-165, compute for each of 10 singleton letter-sets its nearest multi-member-cluster centroid and its nearest multi-member surah in z-scored Euclidean space. Compare against a pre-committed classical-tajwīd a-priori profile match per singleton. MW-5 cheat control via label-shuffle permutation null.

## Timeline

1. Read H-NEW-165 findings doc + script to recover the 15-dim feature codebook (the H-NEW-165 JSON was not present on disk — reconstructed feature-matrix directly from the locked codebook in the script).
2. Wrote pre-reg `h-new-232-oq1-singleton-nearest-neighbor-prereg.md` with:
   - YAML frontmatter (id, phase=B, status=prereg, seed=20260419, rules_tuple, bonferroni_k=2, alpha_bon=0.025, verdict=PENDING).
   - Locked Euclidean-on-z-scored-features as the distance metric (declared BEFORE execution).
   - Pre-committed a-priori accepted-cluster sets per singleton based on al-Khalīl/Ibn Jinnī/al-Suyūṭī classical reasoning (5 singletons one-cluster, 5 singletons two-cluster tie-allowed).
   - Primary threshold ≥ 7 / 10 singletons matching; permutation null p < 0.025.
3. Wrote script `scripts/h_new_232_oq1_singleton.py`:
   - Rebuilt the 29×15 design matrix verbatim from H-NEW-165 codebook.
   - Split 19 multi-member + 10 singleton.
   - Z-score using multi-member statistics only.
   - Compute 4 centroids + distance to each singleton.
   - 1000-permutation label shuffle on multi-member surahs as MW-5 cheat control.
4. Executed. Result: 8/10 matches, p = 0.02498, verdict PASS-COHERENT.
5. Wrote findings file with full per-singleton table, coherence assessment, honest limits, joint interpretation with H-NEW-165.
6. Appended H-NEW-232 entry to MASTER-LEDGER Wave-4 section; updated Wave-4 integrity snapshot.

## Key numbers

- Observed matches: 8 / 10 (primary threshold ≥ 7)
- Permutation null mean: 3.66 matches; std: 1.99; max: 9 (one extreme tail)
- ge_count: 24 / 1000
- p = (1+24)/1001 = 0.02498 < α_bon = 0.025 — just inside
- MW-5 shuffled-label null mean corresponds to 36.6% baseline match-rate under tie-allowances; observed 80% is ~2× lift.

## Singleton nearest-cluster table

| Singleton | Surah | NearestMulti-surah | NearestCluster | A-priori set | Match? |
|---|---|---|---|---|---|
| ALMS | Q 7 | Q 2 ALM | ALM | {ALM} | ✓ |
| ALMR | Q 13 | Q 10 ALR | ALR | {ALM, ALR} | ✓ |
| KHYAS | Q 19 | Q 26 TSM | TSM | {HM, TSM} | ✓ |
| TH | Q 20 | Q 26 TSM | TSM | {TSM} | ✓ |
| TS | Q 27 | Q 26 TSM | TSM | {TSM} | ✓ |
| YS | Q 36 | Q 40 HM | HM | {ALM, ALR} | ✗ |
| S | Q 38 | Q 26 TSM | TSM | {TSM} | ✓ |
| HMASQ | Q 42 | Q 26 TSM | TSM | {HM} | ✗ |
| Q | Q 50 | Q 26 TSM | TSM | {HM, TSM} | ✓ |
| N | Q 68 | Q 10 ALR | ALR | {ALM, ALR} | ✓ |

## Interpretation

**8 clean matches**, including:
- Trivial-inclusion: ALMS → ALM, TS → TSM.
- Anchor-letter-shared: TH → TSM via ط, N → ALR via idhlāq.
- Mustaʿliya-pulled: S → TSM, Q → TSM (both accepted a-priori).

**2 informative misses**:
- KHYAS → TSM and HMASQ → TSM form a MIRROR PAIR landing in TSM (exactly reproducing the H-NEW-165 RF-confusion Q19↔Q42). HMASQ miss is a soft disagreement with the classical a-priori HM-anchor; the 5-letter mustaʿliya triad (ع س ق) overrides the HM-shared (ح م) pair in z-space.
- YS → HM is a genuine surprise; suggests س dominates ي in the z-space weighting.

## Coherence assessment

The result is **phonologically coherent** at the multi-member-cluster level for 8/10 singletons and PHONOLOGICALLY INTERPRETABLE for the 2 misses. Not random. The permutation null p = 0.02498 is at the edge of α_bon = 0.025 — signal is real but not overwhelming. Reported honestly as PASS-COHERENT (inside the bar by ~1 permutation) with clear limits.

## Limits (reproduced from findings)

- Interpretive, not decisive. No external ground truth.
- p = 0.02498 is edge-of-bar (differs by 1 tail permutation from failing).
- Tie-allowances softened the primary threshold.
- Euclidean-on-z-scored is one of many possible metrics; sensitivity deferred to H-NEW-232.1.
- Classical-codebook sensitivity (Holes vs Watson vs Ibn Jinnī) propagates from H-NEW-165.

## Files written

- Pre-reg: `findings/phase-b-hypotheses/h-new-232-oq1-singleton-nearest-neighbor-prereg.md`
- Script: `scripts/h_new_232_oq1_singleton.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-232.json`
- Findings: `findings/phase-b-hypotheses/h-new-232-oq1-singleton-nearest-neighbor.md`
- Journal: this file
- MASTER-LEDGER: Wave-4 additions updated with H-NEW-232 entry + snapshot row

## Queued follow-ups

- H-NEW-232.1 distance-metric sensitivity (Mahalanobis w/ pseudoinverse, cosine, feature-importance-weighted Euclidean).
- H-NEW-232.2 phonological codebook sensitivity.
- H-NEW-232.3 deeper investigation of the 2 misses (YS, HMASQ).
- H-NEW-232.4 extend to non-muq surahs for muq/non-muq phonological discrimination.
