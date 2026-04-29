---
finding_id: h-classic-45
phase: B
status: PRE-REGISTERED — computational-tester self-pre-reg per PRE-REG-STANDARD-04 + STANDARD-05
pre_registered_by: computational-tester (2026-04-14)
registration_date: 2026-04-14
parent_task: "#96"
spec_source: |
  findings/phase-b-hypotheses/h-classic-44-to-49-spec.md §H-CLASSIC-45 +
  task #96 description (2026-04-14 classical-scholar dispatch)
distinct_from: |
  H-NEW-17 (task #25, loanword density × Nöldeke chronology, classical-scholar
  lane, in-progress, uses Jeffery 1938 loanwords TSV) — H-CLASSIC-45 tests the
  STRUCTURALLY DIFFERENT gharīb-root class (lexicalized hapax ≤5 occurrences)
  against the SAME Nöldeke chronology variable. The two tests can reinforce or
  dissociate: loanwords and gharīb partially overlap but are not identical.
rules_tuple: (no-tashkeel, root-level via QAC, hafs-kufan, mashriqi)
seed: 20260414
sided_test: one-sided (spec: ρ < 0 predicted)
direction_prereg_source: |
  al-Suyūṭī Itqān nawʿ (likely 37 or 38, PENDING physical verify) on gharīb
  al-Qurʾān explicitly predicts early-Meccan elevation; seconded by Nöldeke
  chronology tradition's association of short-oracular early-Meccan surahs
  with archaic lexicon; tertiarily seconded by Jeffery 1938 loanword-
  distribution literature. ≥3 sources agreeing on direction per PRE-REG-
  STANDARD-02 one-sided justification rule.
regime_declaration: |
  H-CLASSIC-45 is a CHRONOLOGY-COVARIATE test (per-surah scalar against
  chronology label). It sits in the regime where Nöldeke chronology has
  been REFUTED at z=-1.XX as a graph-geometric sort key (R-010, MW-1 GATE-B,
  pending #53) but CONFIRMED at the level of single-feature correlations
  (multiple H-NEW tests). A PASS would add to the multi-feature chronology
  signature; a NULL would indicate the gharīb-root class does not track
  chronology even as bulk vocabulary does.
h_meta_1_prior: |
  al-Suyūṭī is a mixed-directionality scholar in the H-META-1 convergence
  tracker — local-scope specific claims confirm, global-symmetry claims
  fail. "gharīb density monotone decreases across 4 periods" is a MONOTONE-
  TREND claim at chronology-resolution, which sits in the MIDDLE of the
  scope taxonomy: not a universal global symmetry, not a hyper-specific
  local claim. Prior is UNCERTAIN. Meta-analyst 2026-04-14 power analysis
  flagged this test as N-OK / DESIGN-OK.
transitive_prior_status: |
  al-Suyūṭī Itqān is the primary source for many of the project's classical-
  claim tests. His local-claim record is mixed (~50-60% confirm), and this
  test is at the CHRONOLOGY-COVARIATE scale. No transitive regime prior from
  H-META-1 applies; this is an independent test of the specific gharīb claim.
z_prior_source: no-direct-prior (first operationalization of al-Suyūṭī gharīb claim in this project)
bonferroni_k_outer: 6
bonferroni_family_outer: h-classic-44-49
bonferroni_k_inner: 1
bonferroni_family_inner: h-classic-45-single-primary
parent_dispatch: 2026-04-14-wave-1-3-meta-analyst
alpha_unadjusted_family: 0.00833
alpha_bon: 0.00833
internal_k: 1
null_publishable: true
positive_publishable: true
---

# H-CLASSIC-45 — al-Suyūṭī gharīb al-Qurʾān: early-Meccan gharīb-density elevation across Nöldeke chronology

## Why this pre-registration exists

al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on *gharīb al-Qurʾān* (rare/
lexically-difficult words; likely nawʿ 37 or 38 — PENDING physical edition
verification) argues that the Quran's rare-lexicon distribution is not random
but concentrates in early-Meccan revelations. The classical frame reflects a
shared tradition (Nöldeke, Bell, Jeffery) that early-Meccan surahs have a
distinctive archaic-oracular vocabulary.

Per PRE-REG-STANDARD-02 one-sided justification: ≥3 independent sources agree
on the direction (al-Suyūṭī explicitly; Nöldeke chronological tradition;
Jeffery loanword-class literature), so a one-sided test is locked.

Per PRE-REG-STANDARD-05 hierarchical Bonferroni: this test has a single
primary statistic (Spearman ρ between Nöldeke period and gharīb density),
so inner k=1, and α_bon = 0.05 / k_outer(6) / k_inner(1) = **0.00833**.

## Pre-registered hypothesis

**H-CLASSIC-45 (locked, one-sided):** Spearman ρ between Nöldeke period (1=Early Meccan, 2=Middle Meccan, 3=Late Meccan, 4=Medinan) and per-surah gharīb-density (gharīb-root-tokens per 100 STEM-bearing tokens) is **NEGATIVE** at p_empirical < α_bon = 0.00833.

**Direction lock**: ρ < 0 (monotone decrease from Early Meccan to Medinan).

**Null model**: permute the Nöldeke period labels across the 114 surahs 10,000 times (seed 20260414); at each permutation recompute Spearman ρ on the same fixed gharīb-density scalar per surah. Empirical p = (1 + #null ρ ≤ observed ρ) / (1 + n_perm).

## Pre-registered operationalization

### Gharīb proxy (LOCKED)

A **gharīb root** is defined as a root whose **total Quranic STEM-bearing
token count is ≤ 5** across the whole corpus. Threshold **5 is LOCKED** per
the classical-scholar spec. Rationale for the locked threshold: the
"lexicalized hapax class" (roots appearing in ≤5 tokens) is the standard
operational definition of extreme rarity in corpus-linguistic hapax
literature and matches the spec verbatim. **No sensitivity sweep on the
threshold is permitted as a verdict-entering statistic.** Sensitivity at
thresholds {3, 10} is a post-hoc robustness diagnostic only.

### Gharīb density (LOCKED)

For each surah S:
```
gharib_density(S) = 100 * (# STEM-bearing tokens in S whose root is gharīb)
                        / (# STEM-bearing tokens in S)
```

Denominator is STEM-bearing tokens (tokens with a ROOT: feature in QAC),
not all orthographic tokens, to match the rules-tuple lock on root-level
counting. Using STEM-bearing tokens as denominator is the standard
normalization for root-level corpus statistics and avoids inflation from
function-word tokens that have no root.

### Nöldeke period labels (LOCKED)

Loaded from `data/revelation-order.csv` column `noldeke_phase`. Mapping:
- Early Meccan → 1 (48 surahs)
- Middle Meccan → 2 (21 surahs)
- Late Meccan → 3 (21 surahs)
- Medinan → 4 (24 surahs)

Total: 114 surahs ✓. Source: Tanzil Egyptian Standard + Wikipedia Nöldeke.
This is the same Nöldeke-phase column used by H-NEW-7 (#12), H-NEW-17
(#25), and other chronology-covariate tests in the project.

### Observed statistic (LOCKED)

```
observed_rho = scipy.stats.spearmanr(noldeke_period, gharib_density).correlation
```

with all 114 surahs. No surahs excluded. If a surah has 0 STEM-bearing
tokens (should not happen — sanity check), assert fails and the script
halts.

### Null model (LOCKED)

```
seed = 20260414
rng = np.random.default_rng(seed)
null_rhos = []
for _ in range(10_000):
    perm = rng.permutation(noldeke_period)
    null_rhos.append(spearmanr(perm, gharib_density).correlation)
empirical_p = (1 + sum(1 for r in null_rhos if r <= observed_rho)) / (1 + 10_000)
```

One-sided lower-tail (direction locked as ρ < 0). Seed LOCKED 20260414.
n_perm LOCKED 10,000.

### Pass rule (LOCKED)

PASS if `empirical_p < 0.00833`.

REVERSE cell: `observed_rho > 0 AND upper-tail empirical_p < 0.00833`.

NULL cell: neither PASS nor REVERSE.

## Pre-registered verdict matrix

| Observed ρ sign | Lower-tail p | Verdict |
|---|---|---|
| < 0 | < 0.00833 | **PASS** — al-Suyūṭī gharīb claim confirmed |
| < 0 | ≥ 0.00833 | **NULL** (trend in direction but insufficient power) |
| ≥ 0 | — | **NULL** or **REVERSE** (see upper-tail) |
| > 0 | upper-tail p < 0.00833 | **REVERSE** — anti-prediction (Medinan more gharīb than early Meccan) |

## Diagnostic reporting (NOT verdict-entering)

The following diagnostics will be computed and reported in the JSON but do
**not** enter the verdict:

1. **Per-period means and SEs**: mean gharīb_density for each of 4 Nöldeke
   periods, with bootstrap CI. Expected shape (pass cell): monotone decrease
   1 > 2 > 3 > 4.
2. **Threshold sensitivity**: recompute gharīb density at thresholds {3, 5,
   10} and report ρ for each. The **primary verdict uses threshold 5 only**.
3. **Length confound check**: per-surah gharīb_density vs per-surah STEM-
   token count (length proxy); Spearman ρ reported. If this correlation is
   strong (|ρ| > 0.5), flag a length confound in the narrative.
4. **Meccan-aggregate-vs-Medinan two-group test**: collapse Meccan (periods
   1-3, 90 surahs) vs Medinan (24 surahs), Mann-Whitney U. Reports the
   simpler binary version of the claim.
5. **Alternative chronology**: re-run ρ against `revelation_order` column
   (1-114 Tanzil canonical revelation sequence) as a higher-resolution
   alternative to the 4-phase Nöldeke bucketing. Diagnostic only.

None of these diagnostics can flip or amend the primary verdict.

## No-fork protections

1. **Gharīb threshold LOCKED at ≤5 total Quranic STEM token occurrences.**
2. **Density normalization LOCKED** as per-100-STEM-token rate, not per-
   100-orthographic-token and not per-verse.
3. **Nöldeke period mapping LOCKED** to 1/2/3/4 for Early/Middle/Late/
   Medinan from `revelation-order.csv`.
4. **Primary statistic LOCKED** as Spearman ρ (not Pearson, not Kendall τ).
5. **Null seed LOCKED 20260414**, n_perm LOCKED 10,000.
6. **α_bon LOCKED 0.00833** (hierarchical: k_outer=6, k_inner=1).
7. **One-sided test LOCKED** (lower-tail, direction ρ < 0).
8. **Denominator LOCKED** as STEM-bearing tokens per surah.
9. **Verdict cell matrix LOCKED** per the PASS/NULL/REVERSE rules above.
10. **All five diagnostic reports are DIAGNOSTIC ONLY** — not verdict-
    entering. No post-hoc switching of primary statistic to any diagnostic.

## Outputs

- JSON: `findings/phase-b-hypotheses/csv/h-classic-45.json`
- Narrative: `findings/phase-b-hypotheses/h-classic-45.md`
- Script: `scripts/h_classic_45_suyuti_gharib.py`

## Data reuse disclosure

- Reuses QAC v0.4 morphology loader pattern from
  `scripts/h_classic_44_zarkashi_regime.py` (adapted to produce token-level
  root lists, not per-surah root sets).
- Reuses `data/revelation-order.csv` for Nöldeke phase labels.
- Reuses `data/morphology/root-stats.csv` `total_occurrences` column as the
  cross-check for the gharīb-threshold computation (primary count done
  from-scratch for provenance; root-stats cross-check in narrative).
- No overlap with H-NEW-17 (task #25) beyond shared Nöldeke labels: H-NEW-17
  uses the Jeffery 1938 loanword TSV as the lexicon-class predictor;
  H-CLASSIC-45 uses the corpus-internal hapax ≤5 definition. The two tests
  are cross-referencable as SIMILAR-SCOPE but methodologically independent.
- Cross-refs: `findings/cross-finding/scholar-convergence-tracker.md` §2
  (al-Suyūṭī row), §5 (chronology-regime prior).

## Pre-execution lock confirmation

This file is committed BEFORE the script is written. Threshold, statistic,
seed, α, one-sided direction, period mapping, and diagnostic-vs-verdict
separation are all LOCKED.
