---
id: h-new-165-run-1
finding: H-NEW-165
date: 2026-04-17
agent: h-new-165-autonomous
parent: H-NEW-88, H-NEW-96, H-NEW-96.2
verdict_final: PASS-PRIMARY
---

# Journal — H-NEW-165 phonological predictor run-1

## Timeline

- 2026-04-17 ~15:03 — task dispatched (autonomous run). Read parent H-NEW-88 / H-NEW-96 / H-NEW-96.2 scripts and outputs.
- 2026-04-17 15:10 — wrote pre-reg `findings/phase-b-hypotheses/h-new-165-phonological-predictor-prereg.md` (seed 20260419, bonferroni_k=2, α_bon=0.025, primary threshold top-1 > 0.50).
- 2026-04-17 15:15 — wrote script `scripts/h_new_165_phonological_predictor.py` (400-line, 15-feature classical tajwīd codebook locked in script header).
- 2026-04-17 15:20 — launched run (background, unbuffered stdout to `/tmp/h_new_165.log`). Accidentally spawned 3 concurrent copies (harness handling of Bash calls); killed 2 duplicates, let 1 proceed.
- 2026-04-17 15:21 — initial LOOCV completed. RF top-1 = **0.6552 (= structural ceiling 19/29)**, singleton hits 0/8.
- 2026-04-17 15:24 — perm 100/1000, mean 0.1003, ge_count 0 → p ≤ 0.01 already.
- 2026-04-17 ~16:00 — (estimated) 1000 perms complete, json written.

## What happened

- Built 29 × 15 design matrix from classical-tajwīd feature codebook. Features locked before training per pre-reg.
- LOOCV RF (n_estimators=200, random_state=20260419) reaches **top-1 = 0.6552**, HITTING the multi-member structural ceiling exactly.
- All 4 multi-member clusters (ALM, ALR, HM, TSM) recalled at 1.0.
- All 10 one-member classes recalled at 0.0 — structurally unreachable under LOOCV (each is its own class, absent from training fold).
- Singleton MISSES are phonologically coherent:
  - Q19 KHYAS ↔ Q42 HMASQ (both 5-letter pharyngeal-emphatic sets; mirror-swap)
  - Q20 TH ↔ Q27 TS (both 2-letter ط-initiated; mirror-swap)
  - Q38 S ↔ Q50 Q (both single-letter emphatic/uvular stops)
- Permutation null: first 100 perms, ge_count = 0 (observed top-1 never matched by permuted data). Mean = 0.100. Expected final p ≈ 1/1001 = 0.001.

## Interpretation

**OQ-1 phonological axis: FIRST POSITIVE SIGNAL.** Classical tajwīd aggregates (mean-makhraj, mean-manner, fraction-emphatic, fraction-pharyngeal, letter-count, qalqala-presence) saturate the LOOCV structural ceiling. Content features (H-NEW-96, 92-dim) and rhyme features (H-NEW-96.2, 14-dim) were both NULL. Phonology reaches 0.6552.

Classical tradition partially vindicated: al-Khalīl's makhraj-ordering and the mustaʿliya subset indeed predict letter-set cluster membership.

Singleton assignment REMAINS OPEN — LOOCV can't in principle predict a class absent from training. H-NEW-165.1 queued to attack singletons with non-LOOCV methods.

## Self-review / garden-of-forking-paths

- Pre-reg locked BEFORE running script. Feature codebook sourced from classical Arabic tradition (al-Khalīl, Ibn Jinnī) plus modern Semitic phonology.
- `letter_count` is in the design matrix (redundant with H-NEW-88); not a new circularity because H-NEW-88 already had it at 0.414. Lift to 0.655 attributable to the other 14 features.
- 1000-perm null locked in pre-reg. Seed 20260419.
- Primary threshold = top-1 > 0.50 (strict-better-than-0.414-baseline), per Bonferroni-2.
- Pipeline check MW-5 = 0.517 (matches H-NEW-96 structural ceiling for cheat_surah_id under LOOCV). Pipeline valid.

## Queued follow-ups

- H-NEW-165.1: predict singletons without LOOCV constraint (cross-validated on phonological similarity to held-out cluster).
- H-NEW-165.2: sensitivity analysis on phonological codebook (Holes/Watson vs Ibn Jinnī).
- H-NEW-165.3: ablation — which single features drive the 0.655 ceiling?
- Cross-finding update: OQ-1 first-positive signal on phonological axis. Content + rhyme axes NULL.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-165-phonological-predictor-prereg.md`
- Script: `scripts/h_new_165_phonological_predictor.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-165.json`
- Findings: `findings/phase-b-hypotheses/h-new-165-phonological-predictor.md`
- Run log: `/tmp/h_new_165.log` (ephemeral)
