---
finding_id: Q027-F-12
title: "Solomon-Sabaʾ pericope cohesion: Q 27:22-44 ↔ Q 34:15-19 — NULL-DIRECTIONAL"
phase: B+
date: 2026-05-10
status: NULL-DIRECTIONAL
prereg_sha: f1e2468b954fa93fbdc3e86e12d0d164f1482d564090551566f309387062bd1f
n_perm: 10000
seed: 20260509
verdict: NULL-DIRECTIONAL — direction matches (J_obs > null_mean) but p_perm = 0.146 does not reach the pre-registered ≤ 0.05 PASS threshold
---

# Q027-F-12 — Solomon-Sabaʾ pericope cohesion (cross-finding-025-formal application): NULL-DIRECTIONAL

## Headline

The two corpus-attested Solomon-Sabaʾ narrative pericopes — **Q 27:22-44** (Hudhud's Sabaʾ report + Solomon's letter + Bilqīs's throne-bringing, 23 verses) and **Q 34:15-19** (Sabaʾ's gardens, dam-burst, divine retribution, 5 verses) — exhibit **modest but not Bonferroni-strong root-Jaccard cohesion** at the pericope-scale:

- **J_obs = 0.1200** (15 shared QAC-stem-roots / 125 union roots)
- **J_null_mean = 0.0679 ± 0.0445** (10,000 length-matched random pericope-pairs, seed 20260509)
- **z = +1.17**
- **p_perm (one-sided upper) = 0.1460**

The locked direction (J_obs > null_mean) is matched, but the pre-registered PASS-CONFIRMED threshold (p_perm ≤ 0.05) is **not met**. The pre-registered PASS-DIRECTED threshold (p_perm ≤ 0.10) is also not met. Verdict: **NULL-DIRECTIONAL** — direction matches, but the pericope-pair lies within ~85th percentile of length-matched random pairs, not the upper 10%.

## Numerical result

| Quantity | Value |
|:--|:--|
| Pericope A | Q 27:22-44 (23 verses) |
| Pericope A unique stem-roots | 96 |
| Pericope B | Q 34:15-19 (5 verses) |
| Pericope B unique stem-roots | 44 |
| Shared roots | **15** |
| Union roots | 125 |
| **J_obs (root-Jaccard)** | **0.1200** |
| Null mean (10,000 length-matched perms) | 0.0679 |
| Null std | 0.0445 |
| **z-score** | **+1.17** |
| **p_perm (one-sided upper)** | **0.1460** |
| Direction match (locked: J_obs > null_mean) | ✓ |
| Verdict | **NULL-DIRECTIONAL** |

### Per-verse-normalized concordance (aux statistic)

The 5 verses of pericope B each share substantial root-overlap with pericope A:

| Verse | Roots in B verse | Overlap with R_A | Fraction |
|:--|:-:|:-:|:-:|
| Q 34:15 | 13 | 4 | 0.308 |
| Q 34:16 | 16 | 4 | 0.250 |
| Q 34:17 | 4 | 2 | 0.500 |
| Q 34:18 | 10 | 3 | 0.300 |
| Q 34:19 | 14 | 8 | **0.571** |
| **Mean** | **— ** | **—** | **0.386** |

This per-verse concordance is high (mean 0.39); aux read **suggests** that the pericope-B verses individually have strong root-affinity to pericope-A's vocabulary, but the asymmetric pericope sizes (23 vs 5 verses) inflate the union denominator in the headline Jaccard, dampening the signal. The aux-statistic is reported for transparency but is NOT pre-registered direction-locked.

## Shared QAC-stem-roots (15)

`$kr` (dhikr/remembrance), `$yA` (will/wish/thing), `Amn` (faith/believe), `Zlm` (wrongdoing/dark), `bEd` (after), `jEl` (make/place), `jnn` (jinn/garden), `kfr` (disbelieve/cover), `kll` (all/every), `kwn` (be), `nfs` (soul), `qry` (town/village), `qwl` (say), `rbb` (Lord), `rsl` (messenger/send).

These are largely **theological-narrative core vocabulary**, not Solomon-specific. Several Solomon/Sabaʾ-narrative-specific lexical markers (`sbʾ` = Sheba, `hdhd` = hoopoe, `bls` = Bilqīs name not explicitly stated, etc.) appear in only one of the two pericopes. Q 34:15-19 references Sabaʾ as a kingdom-name without re-naming Solomon directly (Solomon is named in Q 34:12-14 just before the pericope window); Q 27:22-44 names Hudhud and Sabaʾ both. The shared-root inventory is **theological-narrative substrate**, not Solomon-narrative-specific.

## Interpretation: what this means for cross-finding-025-formal

[[cross-finding-025-formal-scale-of-aggregation-law|cross-finding-025-formal]] (2026-05-09 PM) established that **thin** thematic markers (Iblīs, sajda, prophet-vocative) flip from whole-surah NULL to pericope-scale PASS at z = +2.7 to +6.4. The pre-registered prediction for Q027-F-12 was that the **thick** Solomon-Sabaʾ marker would also PASS at pericope scale (pre-committed direction-tighter: PASS-CONFIRMED at p ≤ 0.05).

This pre-commit is NOT met. The pericope-pair cohesion is directionally correct (J_obs > null_mean, z = +1.17) but lies at the 85th percentile, not in the strict-PASS upper tail.

**Three honest readings**:

1. **Marker thickness ≠ automatic pericope-PASS strength**. The triple-flip cases (Iblīs, sajda, prophet-vocative) cluster many short pericopes from many surahs; the *n* of pairs (≥ 78 in H-NEW-1520) provides statistical power. Q027-F-12 is a **single pericope-pair** (n=1 pair-statistic vs 10,000 null pairs). The null variance is wide (std = 0.045 — almost half the observed J_obs), making any single observation hard to discriminate.

2. **The Q 27 Solomon-narrative is dispersed across additional pericopes**. Q 27:15-44 spans the full Solomon-Bilqīs cycle (30 verses); Q 27:22-44 captures only the second half (Hudhud's report through pavilion-of-glass). Pericope B (Q 34:15-19) describes the *post-Solomonic* Sabaʾ kingdom after the dam-burst. The two pericopes' narrative-windows are connected by historical-continuity (the same kingdom) but cover different narrative-phases — explaining why theological-substrate vocabulary dominates the shared-root list over Solomon-specific lexicon.

3. **Pericope-scale flip evidence is heterogeneous at the thick-marker end**. Q027-F-08 (Wave-2) already showed whole-surah Q 27 ↔ Q 34 FR-distance 0.866 vs Q 27 ↔ Q 38 0.991 with aux_p ≈ 0.146 — exactly the same magnitude of directional-but-not-significant signal. Q027-F-12 corroborates the Q027-F-08 reading **at the pericope scale**: the Solomon-Sabaʾ-narrative-clustering exists, but it's a moderate-effect-size, not a strong-clustering signal.

## What this contributes to cross-finding-025-formal

Q027-F-12 is published as **honest NULL-DIRECTIONAL** with full prominence per INVESTIGATION-PROTOCOL §1.3. Its negative evidence is informative:

- **Cross-finding-025-formal's pericope-scale flip is NOT a universal law**. Thick markers can produce modest-but-not-strong cohesion at pericope scale; the strong PASS-DIRECTED cases (z > 2.7) appear to require either (i) many pericope-pairs aggregated, or (ii) markers that are tighter at the pericope window (e.g., a specific imperative-clause cluster).
- The Solomon-narrative is a **content-rich but lexically-dispersed** marker — it spans many roots, many sub-narratives, and many surahs; this dispersion dilutes the pericope-scale cohesion signal.
- A future test could aggregate multiple Solomon-related pericope-pairs (Q 27 × Q 34, Q 27 × Q 38, Q 21 × Q 38, Q 27 × Q 21) for an n-pair-aggregated statistic — but this would constitute a different pre-registered test.

## Cross-references

- [[cross-finding-025-formal-scale-of-aggregation-law|cross-finding-025-formal]] — parent principle; Q027-F-12 is the Solomon-Sabaʾ thick-marker application, with honest NULL-DIRECTIONAL outcome.
- [[Q027-F-08-solomon-narrative-twin-prereg|Q027-F-08]] — companion whole-surah test; aux p_two_sided ≈ 0.146 matched magnitude.
- [[h-new-1380-iblis-pericope-replication|H-NEW-1380]] — pericope-flip PASS (Iblīs, z = +4.76).
- [[h-new-1510-sajda-pericope-replication|H-NEW-1510]] — pericope-flip PASS (sajda, z = +2.69).
- [[h-new-1520-prophet-vocative-pericope|H-NEW-1520]] — pericope-flip PASS (prophet-vocative, z = +6.41).
- al-Biqāʿī, *Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar*, on Q 27-Q 34 munāsabah (qualitative classical claim — pericope-scale empirical signal is moderate, not strong).
- al-Rāzī, *Mafātīḥ al-ghayb*, on Q 34:15 (cross-references the Q 27 Sabaʾ narrative).

Output: `csv/Q027-F-12.json`.
