---
id: H-NEW-253
title: "Mode B siblings — 4-cell M-principle portrait applied to all 114 surahs"
phase: B
status: PRE-REG (locked before compute)
date: 2026-04-17
executed_by: h-new-253-specialist
parent: H-NEW-234 (Q 55 unified 4-principle portrait)
siblings:
  - cross-finding-018 (4-principle reduced model M1/M2/M3/M5)
  - H-NEW-178 (α,β manifold)
  - H-NEW-180 (Q 55 refrain-position)
  - H-NEW-231 (per-surah KL divergence)
seed: 20260419
rules_tuple: (no-tashkeel, 114 surahs, 4-cell M-principle portrait from H-NEW-234, seed 20260419)
bonferroni_k: 2
alpha_bon: 0.025
direction: "≥3 sibling candidates expected if Mode B is a replicable category"
verdict: PENDING
---

# [[h-new-253-mode-b-siblings|H-NEW-253]] — Mode B siblings pre-registration

## Motivation

[[h-new-234-q55-unified-profile|H-NEW-234]] established Q 55 al-Raḥmān as a **Pattern-B-PARTIAL** (3/4
cells EXTREME on M1+M3+M5, M2 TYPICAL) exemplar. [[h-new-234-q55-unified-profile|H-NEW-234]]'s sibling
comparison (descriptive only) identified Q 77 al-Mursalāt as a
**half-Mode-B** (M3-ACF-lag-2 extreme, M5 moderate) and Q 26
al-Shuʿarāʾ as a **refrain-interleaved narrative** (not Mode B).

**Question**: beyond Q 55 and Q 77, are there OTHER Mode-B-extremum
surahs in the 114-surah corpus that replicate the M1+M3+M5
extreme-on-≥3-cells profile? If ≥3 candidates exist, Mode B becomes a
**replicable category** (not a Q 55-unique phenomenon); if only Q 55
reaches ≥3 cells, Mode B is **Q 55-unique** and the classical
*ʿarūs al-Qurʾān* designation is **empirically unique** at the
quantitative level.

## Design

Run the same 4-cell M-principle portrait as [[h-new-234-q55-unified-profile|H-NEW-234]] for **all 114
surahs**, counting for each surah how many of the ~20 per-metric tests
fire at the pre-committed two-sided 5%ile threshold (pct ≤ 5 or ≥ 95).
Score each surah by:

- **cell-count**: number of M-cells (among M1, M2, M3, M5) with ≥1
  metric at two-sided 5%ile threshold (same operationalisation as
  [[h-new-234-q55-unified-profile|H-NEW-234]]'s cell verdict logic).
- **extreme-metric count**: total number of metrics (of 20) at the
  5%ile threshold.

Rank surahs by cell-count (primary) and extreme-metric count
(secondary tiebreaker). Top-10 is reported.

## Metrics (20 total, frozen from [[h-new-234-q55-unified-profile|H-NEW-234]])

**M1 — Hamiltonian cycle + length-extremity hubs** (2 metrics):
1. `mushaf_position_is_structural_hinge` (boolean: ∈ {49..57} per
   [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] ±58 mirror-pair window)
2. `mushaf_minus_noldeke` (two-sided)

**M2 — Late-Meccan scripture-announcement** (2 metrics):
3. `is_muq` (muqaṭṭāʿāt marker, boolean)
4. `noldeke_order` (chronology rank, two-sided)

**M3 — Prosodic distinctiveness** (8 metrics):
5. `residual_H_cond` ([[h-new-195-entropy-per-surah|H-NEW-195]])
6. `z_Q_ljung_box` ([[h-new-181-verse-length-acf|H-NEW-181]])
7. `acf_1` ([[h-new-181-verse-length-acf|H-NEW-181]])
8. `acf_2` ([[h-new-181-verse-length-acf|H-NEW-181]])
9. `max_abs_acf` ([[h-new-181-verse-length-acf|H-NEW-181]])
10. `H_unigram` ([[h-new-195-entropy-per-surah|H-NEW-195]])
11. `emphatic` ([[h-new-182-phonological-vectors|H-NEW-182]])
12. `pharyngeal` ([[h-new-182-phonological-vectors|H-NEW-182]])

**M5 — Length-stratification + compositional modes** (8 metrics):
13. `N_tokens` ([[h-new-172-zipf-per-chapter|H-NEW-172]])
14. `kl_from_corpus` (inline recompute, α=0.1 Dirichlet, matches
    [[h-new-231-kl-divergence-per-surah|H-NEW-231]])
15. `zipf_alpha` ([[h-new-172-zipf-per-chapter|H-NEW-172]] fit)
16. `heap_beta` ([[h-new-172-zipf-per-chapter|H-NEW-172]] fit, beta_h159)
17. `alpha_beta_residual` (derived from [[h-new-178-alpha-beta-manifold|H-NEW-178]] fit α=−3.526β+3.689)
18. `lz_norm_log` ([[h-new-187-lempel-ziv|H-NEW-187]])
19. `gzip_ratio` ([[h-new-187-lempel-ziv|H-NEW-187]])
20. `dispersion_h168` ([[h-new-168-q16-q25-dispersion|H-NEW-168]])

All percentile computations use **leave-one-out** per-surah as in
[[h-new-234-q55-unified-profile|H-NEW-234]] (the target surah is excluded from the 113-surah reference
distribution when computing its own percentile).

## Pre-committed inferential cells (Bonferroni k=2, α_bon = 0.025)

- **Cell A — replicable-category count**: count the number of surahs
  with cell-count ≥ 3. **Null hypothesis**: this count = 1 (only
  Q 55). **Alternative**: count ≥ 3 (Mode B is a replicable category).
  Reported as a descriptive count; inferential significance is
  evaluated via **MW-5 random-feature-label permutation** (1000
  permutations, seed 20260419+1): shuffle the cell-assignment of each
  metric across {M1,M2,M3,M5} and re-run the cell-count; the fraction
  of shuffles producing ≥3 surahs at cell-count≥3 is the empirical
  p-value.

- **Cell B — shared-content-profile test**: if ≥3 candidates emerge,
  test whether they share structural features (oath-opener,
  refrain-presence, Q 50–56 eschatological-hub membership). Descriptive
  analysis; no formal p-value (interpretive cell).

## Decision rules

- **If ≥3 candidates with cell-count ≥ 3 at p < 0.025**: Mode B is a
  **REPLICABLE CATEGORY**. Name the candidates. Interpret shared
  content-profile.
- **If exactly 2 (Q 55 + Q 77) with cell-count ≥ 3**: Mode B is a
  **2-EXEMPLAR phenomenon**. Q 55 remains principal exemplar with
  Q 77 sibling.
- **If only Q 55 reaches cell-count ≥ 3**: Mode B is **Q 55-UNIQUE**;
  the classical *ʿarūs al-Qurʾān* designation is empirically unique.

## MW-5 sanity check

Random-feature permutation: shuffle the (principle, metric) labels
1000 times (seed 20260419+1). For each shuffle, recompute cell-count
per surah. The null distribution of "number of surahs at cell-count
≥3" under random cell-assignment should NOT systematically produce
top-5 surah clustering.

## Honest limits (pre-disclosed)

1. **5%ile cutoff is arbitrary**: sensitivity to 10%ile and 1%ile
   cutoffs is deferred to a follow-up (H-NEW-253.1).
2. **Metric bundle is [[h-new-234-q55-unified-profile|H-NEW-234]]-inherited**: 20 metrics across 4 cells
   is not a balanced design (M3 and M5 each have 8 metrics; M1 and M2
   have 2 each). Cell-count verdict is biased toward M3/M5 unless
   normalised. We report BOTH cell-count (majority-vote per cell) AND
   extreme-metric-count (raw bundle count).
3. **Leave-one-out percentile** means each surah's reference
   distribution has n=113 (not n=114). This is consistent with
   [[h-new-234-q55-unified-profile|H-NEW-234]] methodology.
4. **Descriptive sibling analysis** in Cell B (no formal p-value).

## Files (planned)

- Pre-reg: this file.
- Script: `scripts/h_new_253_mode_b_siblings.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-253.json`
- CSV: `findings/phase-b-hypotheses/csv/h-new-253-all-surah-profile.csv`
- Findings: `findings/phase-b-hypotheses/h-new-253-mode-b-siblings.md`
- Journal: `journal/h-new-253-run-1.md`
- MASTER-LEDGER Wave-5 entry.
