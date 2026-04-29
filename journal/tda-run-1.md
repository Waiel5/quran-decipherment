# tda-run-1 — journal

**Date:** 2026-04-13
**Test:** T5 (TOMORROW-TESTS-PRE-REGISTRATION.md §5) — Topological Data
Analysis of verse-embedding manifold
**Seed:** 20260413
**Output:** `findings/phase-b-hypotheses/tda-manifold.md`
**Verdict:** NULL (pre-registered criterion 4/4 inside within-90pct)

## Methodology in one screen

1. Load Quran from `quran-text/quran-no-tashkeel.json` (SHA-256
   253f72f3…35918a). Apply counted-only-in-surah-1 rule for basmala.
   Result: 6,236 verse strings.
2. Build four matched baselines (Bukhari-noquran, Sīra Ibn Hishām, Jāḥiẓ
   al-Ḥayawān, Muʿallaqāt). Split each by Arabic sentence punctuation
   targeting mean Quranic verse char-length (65). Deterministic sample of
   6,236 units per baseline (Muʿallaqāt exhausted at 770).
3. Encode all texts with
   `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (384-dim,
   L2-normalized). Tashkeel stripped from baselines so the encoder sees
   the same orthographic regime.
4. Persistent homology via `ripser` (Vietoris-Rips, Euclidean metric on
   unit sphere, maxdim=1). Subsample to n=2,000 per the pre-registration's
   authorized fork (full 6,236-point V-R OOM'd).
5. Bottleneck distances (`persim`) between every pair of H1 persistence
   diagrams. Compare Quran-vs-baseline against the within-baseline null
   (k=6 pairs).

## Key numbers (H1)

| Corpus | n features | max lifespan | Σ lifespan/1k pts |
|---|---|---|---|
| Quran | 1,650 | 0.159 | 19.12 |
| Jāḥiẓ | 2,622 | 0.150 | **33.55** |
| Sīra | 1,578 | 0.136 | 16.48 |
| Muʿallaqāt | 443 (n=770) | 0.128 | 15.32 |
| Bukhari | 1,281 | 0.115 | 12.15 |

Quran ranks **2nd of 5** in persistent-loop density, below Jāḥiẓ.

Bottleneck: max Quran-vs-baseline = 0.0409 (vs Jāḥiẓ). Within-baseline
max = 0.0483 (Bukhari ↔ Jāḥiẓ). Quran's distances all below within-90pct
(0.0449) — the pre-registered NULL zone.

## What I did NOT do (scope discipline)

- Did not modify monograph, `THE-MAN-AT-THE-CENTER.md`,
  `TOMORROW-TESTS-PRE-REGISTRATION.md`, or verse-commentary files.
- Did not tune encoder, distance, or subsample after seeing results.
- Did not run Arabic-monolingual or OpenAI alternatives (OpenAI key absent;
  AraBERT flagged for future work only).

## Forks actually taken

- Subsample n=2,000 (pre-authorized in the task spec).
- H2 skipped (compute-infeasible on 2,000-point V-R).
- 5 corpora total (pre-registration mentioned "Bukhari, Jahiliyya poetry,
  Muʿallaqāt, Jāḥiẓ"; we used Bukhari-noquran + Sīra + Jāḥiẓ + Muʿallaqāt
  — Sīra was the substitute for generic "Jahiliyya prose").

## Files written

- `findings/phase-b-hypotheses/tda-manifold.md`
- `scratch/tda/tda_run.py`
- `scratch/tda/tda_results.json`
- `scratch/tda/{quran,bukhari-noquran,sira-ibn-hisham,jahiz-hayawan,muallaqat}_emb.npy`
- `scratch/tda/{corpus}_dgm_H0.npy` and `_dgm_H1.npy`
- `scratch/tda/stdout.log`
- `scratch/tda/tda_log.txt`

## Master-index update

Added row to Test-5 line in `docs/master-index.md` (phase-b section).
