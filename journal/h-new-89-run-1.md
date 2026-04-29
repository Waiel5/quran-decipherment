---
id: H-NEW-89-run-1
date: 2026-04-15
agent: h-new-89-specialist
status: COMPLETED
---

# H-NEW-89 — Meta-Cluster Network Synthesis (Run 1)

## Process

1. Reviewed existing cluster findings: H-NEW-58c (musabbiḥāt p=0.0001),
   H-NEW-67 (al-sabʿ al-ṭiwāl p=0.0001), H-NEW-63 (Khawātim ext),
   H-NEW-68 prereg (Friday cluster), H-NEW-58b (auto-discovered taxonomy),
   cross-finding-008 (muqaṭṭāʿat as book-intro markers).
2. Locked 11 cluster systems from cited finding files BEFORE running
   any computation. List captured verbatim in pre-reg.
3. Pre-registered 4 metrics (M1 descriptive, M2-M4 inferential),
   Bonferroni-4, α_bon=0.0125, N_PERM=10K, seed=20260416.
4. Wrote and ran `scripts/h_new_89_meta_cluster_network.py`.
5. Wrote findings file + cross-finding-009 + journal.

## Results

- 1 surah at degree 4: **Q 62 al-Jumuʿah** (unique meta-hub)
- 3 surahs at degree 3: Q 2, Q 3, Q 59
- 7 surahs at degree 2
- 82 surahs at degree 1
- 21 surahs at degree 0 (isolates)

| Cell | p | Pass at α=0.0125 |
|---|---:|:---:|
| M2 variance | 0.998 (REVERSE) | NO |
| M3 hub-zone position | 0.0040 | YES |
| M4 isolate count | 1.0×10⁻⁴ | YES |

Verdict: PASS (2/3 inferential cells significant).

## Surprises / honest disclosures

- **M2 reverse direction**: Pre-reg expected variance ENRICHMENT;
  observed variance UNDER-DISPERSION. Mechanism: classical clusters
  are placed CONTIGUOUSLY in the muṣḥaf (mufaṣṣal Q 49-114, ḥm Q
  40-46, etc.), which smooths the degree distribution rather than
  concentrating it. Logged transparently.
- **Q 62 as 4-cluster hub** was a PRIOR candidate from H-NEW-63 noting
  Q 62's "triply-structured" status. Adding the mufaṣṣal cluster
  bumps Q 62 to degree 4 (the unique highest in the corpus).
- **Front-back hub-pair architecture** was an emergent observation
  (Q 2-3 share 3 clusters; Q 59-62 share clusters; the two pairs
  share NO clusters). Not pre-registered; logged as post-hoc
  observed-fact in findings file.

## Garden-of-forking-paths log (declared in pre-reg)

- 11 clusters chosen (not 8 minimum) for full coverage.
- Top-decile hubs (K=11), not arbitrary cutoff.
- Membership-permuted null (preserves cardinalities, randomizes IDs).
- Q 9 reading for al-sabʿ al-ṭiwāl (al-Suyūṭī primary).
- Pure الر for C2 (Q 13 المر excluded; conservative).
- mufaṣṣal at Q 49-114 (matches H-NEW-45.2 dead-zone test).
- Variance as M2 metric (matches null structure exactly).

## Cross-finding promotion

This finding warrants cross-finding-009 (Meta-Cluster Network of
the Quran). Written and filed. Q 62 al-Jumuʿah's unique 4-cluster
hub status integrates findings across:
- H-NEW-58c (musabbiḥāt)
- H-NEW-63 (Khawātim extended)
- H-NEW-67 (al-sabʿ al-ṭiwāl)
- H-NEW-68 (Friday liturgy pre-reg)
- cross-finding-008 (muqaṭṭāʿat synthesis)

## Files written

- `findings/phase-b-hypotheses/h-new-89-meta-cluster-network-prereg.md`
- `scripts/h_new_89_meta_cluster_network.py`
- `findings/phase-b-hypotheses/csv/h-new-89.json`
- `findings/phase-b-hypotheses/h-new-89-meta-cluster-network.md`
- `findings/cross-finding/cross-finding-009-meta-cluster-network.md`
- `journal/h-new-89-run-1.md` (this file)

## Reproducibility

- Seed 20260416, N_PERM=10K, deterministic on rerun.
- All cluster definitions hard-coded in script; no external CSV
  dependency for membership lists.
- elapsed 0.9s on local machine.
