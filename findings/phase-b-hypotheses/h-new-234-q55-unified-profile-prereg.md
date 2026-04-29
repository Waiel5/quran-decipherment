---
id: H-NEW-234
title: "Q 55 al-Raḥmān — unified 4-principle analytical portrait (pre-reg)"
phase: B
status: PRE-REG (locked before compute)
date: 2026-04-17
executed_by: h-new-234-specialist
parent: cross-finding-018 (4-principle reduced model M1/M2/M3/M5)
siblings:
  - H-NEW-180 (Q 55 refrain-position geometry CONFIRMED)
  - H-NEW-178 (α,β manifold — Q 55 extreme LOW-α residual)
  - H-NEW-231 (per-surah KL divergence — Q 55 rank 3/114)
  - H-NEW-192 (mushaf position decomposition)
  - cross-finding-018 (4-principle model definitions)
seed: 20260419
rules_tuple: (no-tashkeel, hafs-kufan, Q 55 singular surah, seed 20260419)
bonferroni_k: 4  # one inferential cell per M-principle
alpha_bon: 0.0125
direction: DESCRIPTIVE — no sign pre-committed per cell; cells test whether Q 55 sits at >= p95 or <= p05 extreme (two-sided) on at least one metric in the principle's bundle
verdict: PENDING
---

# [[h-new-234-q55-unified-profile|H-NEW-234]] — Q 55 al-Raḥmān unified 4-principle analytical portrait (pre-reg)

## Motivation

Q 55 al-Raḥmān is observationally extreme on multiple instruments:

- [[h-new-231-kl-divergence-per-surah|H-NEW-231]] KL = 1.650 (rank 3/114; only non-short surah in top-15)
- [[h-new-178-alpha-beta-manifold|H-NEW-178]] (α,β) residual = −0.285 (largest LOW-α outlier in the corpus)
- [[h-new-180-q55-refrain-position-result|H-NEW-180]] refrain geometry CONFIRMED (31 refrains, CV = 0.162, FFT peak
  at period ≈ 2.053, p = 0.0004)
- Classical *ʿarūs al-Qurʾān* (Bride of the Quran) via al-Tirmidhī #3291
- Classical 31-refrain pillar per al-Suyūṭī *Itqān* II.161 and al-Qurṭubī

**Question**: does Q 55 saturate the 4-principle reduced model
([[cross-finding-018-four-principle-reduced-model|cross-finding-018]]) — i.e. is it extreme on ALL of M1/M2/M3/M5 —
or does it cluster on a subset, revealing the model's limits on this
uniquely stylized surah?

**Corollary question**: does the mushaf-rank 55 placement FOLLOW from the
4-principle architecture (e.g. positioned between the eschatological
neighbours Q 54 al-Qamar and Q 56 al-Wāqiʿa as a cosmological-refrain
interlude, or as the mid-ring hinge between M2-Meccan-narrative and
M5-Medinan-legal blocks), or does it require an additional explanation
beyond the model?

## Hypotheses

Four inferential cells, one per principle. Each cell operationalized on a
pre-committed **bundle of per-surah metrics**; Q 55 is EXTREME on the
principle if its percentile is ≤ p05 OR ≥ p95 on ≥ 1 bundle metric with
the direction pre-committed below. Bonferroni-4 applied at α_bon = 0.0125.
All metrics computed identically for all 114 surahs (MW-5 calibration >=
5 surahs trivially satisfied at N=113 sibling sample).

### Cell M1 — Structured Hamiltonian cycle + length-extremity hubs

**Bundle** (per-surah, from existing CSVs):
- **mushaf_position** (direct; rank 55/114)
- **noldeke_order** (classical chronology; from zipf-per-surah.csv →
  Nöldeke rank 43 "Early Meccan" per classical count)
- **FR-wrap-edge**: mean Fisher-Rao distance Q 55 → {Q 1, Q 113, Q 114}
  (from [[h-new-111-fisher-rao-mushaf|h-new-111]].json root-FR matrix if available; else not-computed,
  flagged descriptively)
- **block membership**: mid-mushaf (Q 50–Q 60 region includes the
  ±58 mirror pair Q 49→50 and Q 56→57 per [[cross-finding-018-four-principle-reduced-model|cross-finding-018]])

**Criterion**: Q 55 EXTREME on M1 if (a) mushaf-position is inside a
pre-committed structural-hinge window (Q 49–57; the mid-mushaf ±58
mirror region identified in [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] / [[h-new-148-all-boundary-root-bridges|H-NEW-148]]), OR (b)
Nöldeke-to-mushaf gap |Nöldeke-rank − mushaf-rank| ≥ p95 of the
114-surah distribution.

### Cell M2 — Late-Meccan scripture-announcement, muqaṭṭāʿat-marked

**Bundle** (per-surah):
- **muq_indicator** (binary; Q 55 = NO muqaṭṭāʿat)
- **Nöldeke phase** (from zipf-per-surah.csv; Q 55 = Early Meccan per
  classical, but Islamic-tradition classification varies — "Medinan"
  also attested; we lock on the CSV's period field)
- **qul_density / book-ref density / eschat density** (three Pattern-B
  axes from [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]'s 5-axis bundle; available per-surah if
  [[h-new-125-chronology-content|h-new-125]] and [[h-new-192-mushaf-position-decomposition|h-new-192]] feature tables are loadable)
- **loanword density** (the 5th Pattern-B axis)

**Criterion**: Q 55 EXTREME on M2 if its Pattern-B composite score (mean
z-score across available Pattern-B axes) is ≤ p05 OR ≥ p95. Given Q 55
is non-muq and classically un-muqaṭṭāʿat-marked, the prediction is
M2-TYPICAL rather than M2-EXTREME — a NULL here would CONFIRM that the
Late-Meccan scripture-announcement principle does not uniquely explain
Q 55's distinctiveness.

### Cell M3 — Prosodic distinctiveness (meso-scale-enhanced)

**Bundle** (per-surah):
- **residual_H_cond** ([[h-new-195-entropy-per-surah|H-NEW-195]] per-surah conditional entropy residual)
- **verse-length ACF lag-1 + lag-2** ([[h-new-181-verse-length-acf|h-new-181]]-per-surah.csv)
- **Ljung–Box z-score z_Q** ([[h-new-181-verse-length-acf|h-new-181]]-per-surah.csv; prosodic-memory
  non-randomness)
- **[[h-new-180-q55-refrain-position-result|H-NEW-180]] refrain-geometry score** (Q 55 specific: CV = 0.162,
  p = 0.0001 — computed for refrain-surahs only, used descriptively)

**Criterion**: Q 55 EXTREME on M3 if its verse-length ACF lag-2 is
≥ p95 (near-periodic pillar-signature expected from the 31 refrains
every ~2 verses) OR |residual_H_cond| ≥ p95 (prosodic-template
compression signature).

### Cell M5 — Length-stratification + compositional modes

**Bundle** (per-surah):
- **n_tokens** (length; Q 55 = 352 — short-medium mufaṣṣal)
- **KL divergence** ([[h-new-231-kl-divergence-per-surah|H-NEW-231]]; Q 55 = 1.650)
- **Zipf α** ([[h-new-172-zipf-per-chapter|h-new-172]]-per-surah.csv; length-residualized residual)
- **Heap β** ([[h-new-172-zipf-per-chapter|h-new-172]]-per-surah.csv)
- **(α,β) residual** ([[h-new-178-alpha-beta-manifold|H-NEW-178]]; Q 55 = −0.285)
- **LZ normalized complexity** ([[h-new-187-lempel-ziv|h-new-187]]-per-surah.csv)
- **dispersion** ([[h-new-168-q16-q25-dispersion|h-new-168]]-per-surah-dispersion.csv; [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]])

**Criterion**: Q 55 EXTREME on M5 if ≥ 2 of {KL, (α,β) residual, LZ
norm, dispersion} sit at ≤ p05 OR ≥ p95 given Q 55's length class.

## Synthesis rule (pre-committed)

- **Pattern-B-SATURATED** if Q 55 is EXTREME on ALL 4 cells at
  Bonferroni α_bon = 0.0125
- **Pattern-B-PARTIAL** if EXTREME on 2–3 cells → report subset and
  refine Mode B interpretation
- **Pattern-B-MISS** if EXTREME on ≤ 1 cell → 4-principle model
  insufficient to describe Q 55's distinctiveness; residual field
  updated

The sibling-refrain comparison (Q 77 al-Mursalāt = 10 refrains, Q 26
al-Shuʿarāʾ = 8 refrains) is a DESCRIPTIVE cross-check, not a
separate inferential cell.

## Position-in-mushaf interpretation (descriptive)

Independently of the 4 cells, we test whether rank 55 is PREDICTED by
the compositional-feature regressor ([[h-new-192-mushaf-position-decomposition|H-NEW-192]]'s Ridge LOOCV). Q 55's
prediction residual is reported; if |Δ| ≤ p50 of the 114 residuals, the
mushaf position is well-explained by compositional features; if |Δ| ≥
p90, rank-55 is an M1 structural placement not a compositional
emergent.

The eschatological-neighbor reading (Q 54 al-Qamar apocalypse; Q 55
al-Raḥmān cosmic-reward-and-punishment; Q 56 al-Wāqiʿa judgment-scene)
is a classical al-Biqāʿī *munāsabāt* observation; we report Q 55's root
Fisher-Rao distance to Q 54 and Q 56 (if available from [[h-new-111-fisher-rao-mushaf|h-new-111]].json)
as descriptive triangulation.

## MW-5 sanity

All metrics in the 4 bundles are ALREADY computed for 114 surahs in
prior findings ([[h-new-172-zipf-per-chapter|h-new-172]], [[h-new-178-alpha-beta-manifold|h-new-178]], [[h-new-181-verse-length-acf|h-new-181]], [[h-new-182-phonological-vectors|h-new-182]], [[h-new-187-lempel-ziv|h-new-187]],
[[h-new-195-entropy-per-surah|h-new-195]], [[h-new-231-kl-divergence-per-surah|h-new-231]], [[h-new-168-q16-q25-dispersion|h-new-168]]). Q 55 is ONE of 114 with identical
pipelines. MW-5 trivially satisfied.

## Classical-scholarship bridge

- **al-Suyūṭī *Itqān* II.161** — count of 31 refrains; block partition
  (creation / balance / jinn & men / punishment / two gardens / two
  gardens-below; 8 blocks)
- **al-Tirmidhī #3291** — *ʿarūs al-Qurʾān* (Bride of the Quran)
  designation
- **al-Qurṭubī *al-Jāmiʿ li-aḥkām al-Qurʾān*** — tafsīr of v. 46
  onward parallelism between "two gardens" and "two other gardens"
- **Neuwirth 2010** (*Der Koran als Text der Spätantike*) — al-Raḥmān
  as cosmological hymn with stylized refrain phenomenon
- **al-Biqāʿī *Naẓm al-Durar*** — munāsabāt between Q 54 Qamar and Q 56
  Wāqiʿa through Q 55 as mid-cosmological-pillar

## Garden-of-forking-paths log (pre-compute)

1. **Decision**: 4 cells, one per M-principle. Alternative considered:
   20 single-metric cells with Bonferroni-20 α = 0.0025. Rejected because
   the principal question is about the 4-principle model, not about
   which individual metric.
2. **Decision**: 95th/5th percentile two-sided extremity. Alternative:
   98th/2nd (10-sided sharper). Rejected because 4 cells × Bonferroni-4
   at α = 0.0125 already gives strong adjustment; p05/p95 keeps the
   cells realistic given only N=114 surahs.
3. **Decision**: M2 prediction is TYPICAL (non-muq, non-Pattern-B), so
   an M2 NULL is an INFORMATIVE finding, not a failure.
4. **Decision**: Sibling-refrain (Q 77, Q 26) is descriptive context,
   not a Bonferroni cell; refrain-count is not the axis tested.
5. **Decision**: mushaf-position residual test ([[h-new-192-mushaf-position-decomposition|H-NEW-192]] LOOCV) is
   descriptive, not a Bonferroni cell; it reports compositional-vs-
   structural placement but does not adjudicate the 4-principle model.

## Execution plan

Script: `scripts/h_new_234_q55_profile.py`

1. Load all 8 per-surah CSVs listed in the bundles.
2. Merge into a 114-row master frame keyed by surah_id.
3. For each metric, compute Q 55's percentile (rank/113 across non-Q 55
   surahs, two-sided extremity) and record.
4. Apply cell-level criterion → verdict per cell.
5. Compute Pattern-B-SATURATED / PARTIAL / MISS synthesis.
6. Compute sibling-refrain comparison (Q 77, Q 26, Q 55) on same
   metrics.
7. Write JSON to `csv/h-new-234.json` and per-surah table to
   `csv/h-new-234-profile.csv`.
8. Write findings md + journal.

## Honest limits

1. The metrics share correlated noise (length drives KL, α, β, LZ).
   Multi-metric bundle does NOT give 4 independent axes — at best ~2
   effective axes in M5 (length, refrain-driven idiosyncrasy).
2. M2 bundle depends on per-surah Pattern-B composite existing; if
   [[h-new-125-chronology-content|h-new-125]] per-surah scores not found, we downgrade to muq indicator
   + Nöldeke phase only (2 features).
3. Per-surah Fisher-Rao distances (for the Q 54 / Q 56 neighbor check)
   require [[h-new-111-fisher-rao-mushaf|h-new-111]].json root-FR matrix; if not-parseable, we report
   descriptively without.
4. Classical *ʿarūs al-Qurʾān* is a qualitative accolade; we CANNOT
   test it inferentially without a formal definition; it is cited as
   context.
5. The mushaf-position interpretation (rank 55 as mid-ring hinge) is
   POST-HOC-adjacent — the ±58 mirror pair was independently reported
   ([[h-new-148-all-boundary-root-bridges|H-NEW-148]]), but "rank 55 is special" is not a pre-committed
   hypothesis.

## Queue

- H-NEW-234.1 — formal test of Q 55 as **Pattern-B mode extremum**
  across the full sibling-refrain set (Q 26, Q 77, Q 55, Q 37
  post-hoc) against a null of non-refrain surahs of matched length.
- H-NEW-234.2 — permutation null: randomly swap Q 55 with each of
  {Q 54, Q 56} and measure the global M1 geodesic-length change.
