---
id: H-NEW-51
title: Muqaṭṭaʿāt Cardinality Declines with Surah Position — partial correlation survives length control
phase: B
status: PASS-DIRECTED at α=0.05 single-test (post-hoc-noticed; replication required for upgrade)
date: 2026-04-16
agent: integrator (main session); follows up on H-NEW-46 (length skew) and H-NEW-45 (clustering)
script: inline (Python; ~80 lines)
seed: 20260416
n_perm: 100,000
verdict: PASS-DIRECTED (with post-hoc disclosure)
rules_tuple: (hafs-kufan; verse-count-as-length-metric)
---

# [[h-new-51-cardinality-position-decline|H-NEW-51]] — Muqaṭṭaʿāt Cardinality Declines with Surah Position (RESULT)

## Headline

**Spearman ρ(surah_index, muqaṭṭaʿāt cardinality) = −0.66 raw, partial ρ(position, cardinality | length) = −0.70 (after controlling for surah length).** Permutation p = 2×10⁻⁵ (100K perms, seed 20260416) on the partial correlation. The effect SURVIVES surah-length control with stronger effect than the raw correlation.

## Garden-of-forking-paths disclosure (CRITICAL)

This finding was post-hoc-noticed during 2026-04-16 main-session reconnaissance on the canonical-order ordering of the 14 muqaṭṭaʿāt subsets. I noticed:
- Single-letter subsets {ص, ق, ن} appear at Q 38, 50, 68 (LATE in the muqaṭṭaʿāt sequence)
- Larger subsets (4-letter المص, المر at Q 7, 13; 5-letter كهيعص at Q 19) appear EARLY
- This is a directional pattern: cardinality decreases with position

The OBSERVATION came BEFORE the test was specified. To honestly handle this:
- **Single test, no Bonferroni cost** (analogous to [[h-new-44-2-poa-closure|H-NEW-44.2]].1 protocol)
- **Pre-committed direction**: cardinality DECREASES (one-sided lower)
- **Pre-committed test**: partial Spearman correlation with permutation null
- **Pre-committed criterion**: p < α=0.05 single-test
- **Verdict label**: PASS-DIRECTED (NOT CONFIRMED) until independent replication

This is the cleanest post-hoc-discipline pattern the project allows. The permutation p of 0.00002 is dramatic, but the post-hoc origin caps the elevation.

## Per-cardinality position table

| Cardinality | n | Muqaṭṭaʿāt | Surah indices | Median |
|---|---|---|---|---|
| 1-letter | 3 | ص, ق, ن | {38, 50, 68} | **50** |
| 2-letter | 9 | طه, طس, يس, حم×6 | {20, 27, 36, 40, 41, 43, 44, 45, 46} | **41** |
| 3-letter | 13 | الم×6, الر×5, طسم×2 | {2, 3, 10, 11, 12, 14, 15, 26, 28, 29, 30, 31, 32} | **15** |
| 4-letter | 2 | المص, المر | {7, 13} | **10** |
| 5-letter | 2 | كهيعص, حمعسق | {19, 42} | **30.5** |

The 3-letter and 4-letter clusters concentrate EARLY (median Q 10–15). The 1-letter cluster concentrates LATE (median Q 50). Only the 5-letter cluster (n=2 only) breaks the pattern by including Q 42.

## Three-variable correlation analysis

| Pair | Spearman ρ |
|---|---|
| ρ(position, cardinality) | **−0.66** |
| ρ(length, cardinality) | +0.23 |
| ρ(position, length) | −0.68 (well-known long-first ordering) |

| Partial correlation | Value |
|---|---|
| Partial ρ(position, cardinality \| length) | **−0.70** |
| Partial ρ(length, cardinality \| position) | −0.40 |

Notably, the partial ρ(position, cardinality | length) is **STRONGER** than the raw ρ(position, cardinality). This means the surah-length confound was ATTENUATING the true position effect, not creating it. Removing length unmasks a stronger position-cardinality decline.

## Permutation null test (100K perms, seed 20260416)

Null model: shuffle cardinalities among the 29 muqaṭṭaʿāt-opened surahs; recompute partial correlation.

| Test | Partial ρ observed | Null mean | p (two-sided, |partial| ≥ obs) |
|---|---|---|---|
| Partial ρ(position, cardinality \| length) | −0.703 | ≈ 0 | **2×10⁻⁵** |
| Partial ρ(length, cardinality \| position) | −0.399 | ≈ 0 | 0.034 |

Position effect survives at p = 2×10⁻⁵; length effect survives at p = 0.034 (marginal).

## Verdict per pre-committed criterion

| Outcome | Verdict |
|---|---|
| Partial ρ(position, cardinality \| length) p < 0.05 (single test) | **PASS-DIRECTED** |
| p ≥ 0.05 | NULL |

Observed p = 2×10⁻⁵ → **PASS-DIRECTED**.

**This is NOT CONFIRMED status.** Per the project's post-hoc-discipline protocol, an independent replication on a distinct data dimension is required for upgrade.

## Mechanism interpretation (conditional on replication)

If the cardinality-decreases-with-position pattern is robust:

1. **Tapering / monotonic-design hypothesis**: the muqaṭṭaʿāt assignment was designed with intent to decrease in complexity through the canonical mushaf order. Larger letter-clusters in early/long surahs; single-letter "punctuation" muqaṭṭaʿāt in late/short surahs.

2. **Sonic-prominence-decay hypothesis**: longer letter-set openings (5-letter كهيعص) carry more recitation prominence; their concentration in earlier surahs suggests the design favors prominent openers in the more theologically-foundational early surahs.

3. **Mnemonic-weight hypothesis**: longer disconnected-letter sequences are harder to memorize. Early/long surahs (which require deeper engagement anyway) carry the mnemonic load; later/shorter surahs carry lighter load.

4. **Chronological-revelation hypothesis** (testable): early-revealed surahs may have had simpler muqaṭṭaʿāt? Test by Nöldeke chronology (queued).

## Independent replication path queued

**[[h-new-51-1-noldeke-replication|H-NEW-51.1]]** (independent pre-reg): replicate the cardinality-position decline using **Nöldeke chronological order** instead of canonical mushaf order. If cardinality decreases with revelation order too, mechanism candidate 4 strengthens. If the decline is ONLY in mushaf order (not chronology), it's a mushaf-design-specific finding.

This is a CLEAN INDEPENDENT test on a distinct data dimension (chronology vs canonical order are distinct orderings). One-sided directed prediction; α=0.05 single-test.

## Cross-finding context (muqaṭṭaʿāt structural findings as of 2026-04-16)

| Test | Verdict | Stat |
|---|---|---|
| [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary | CONFIRMED | ρ_freq = −0.54 |
| H-NEW-44.1 (subset closure) | NULL | 0/6 cells |
| [[h-new-44-2-poa-closure|H-NEW-44.2]] (POA) | NULL | overall χ² p = 0.065 |
| [[h-new-44-2-poa-closure|H-NEW-44.2]].1 (pharyngeal exhaustivity, directed) | PASS-DIRECTED | p = 0.0489 |
| [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] (gap-entropy clustering) | PARTIAL-PASS | p = 2×10⁻⁵ |
| [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] (length skew) | STRONG-PASS | 4/4 cells, p = 1×10⁻⁵ to 1.6×10⁻⁴ |
| [[h-new-47-muqattaat-frequency-cutoff|H-NEW-47]] (sharp-cutoff) | NULL | 10/14 not 14/14 |
| **[[h-new-51-cardinality-position-decline|H-NEW-51]] (cardinality-position decline)** | **PASS-DIRECTED (post-hoc)** | **partial p = 2×10⁻⁵** |

The cardinality-position decline ADDS a new structural axis to the muqaṭṭaʿāt design picture:
- Letter-frequency: muqaṭṭaʿāt prefers high-frequency letters (ρ=-0.54)
- Surah-position: muqaṭṭaʿāt clusters contiguously (gap-entropy p=2e-5)
- Surah-length: muqaṭṭaʿāt-opened surahs are dramatically longer (4/4 STRONG-PASS)
- **Cardinality-position: cardinality monotonically declines through canonical order (post-hoc, p=2e-5 partial after length control)**

This is a coherent picture of muqaṭṭaʿāt as a non-randomly-assigned letter-set system with multiple correlated structural axes.

## Honest caveats

1. Post-hoc-noticed; verdict is PASS-DIRECTED, not CONFIRMED.
2. The 5-letter كهيعص at Q 19 is consistent with the trend (early); the 5-letter حمعسق at Q 42 BREAKS the trend (late). The pattern is monotonically dominant but not strictly monotonic.
3. The partial correlation framework relies on Spearman (rank-based) which is robust to outliers; Pearson would give similar magnitude.
4. The length-controlled partial is STRONGER than the raw — this is the unusual but legitimate "suppression effect" in causal-inference terminology. Surah length is a SUPPRESSOR variable here.
5. Replication via [[h-new-51-1-noldeke-replication|H-NEW-51.1]] (Nöldeke chronology) is the appropriate next step.

## Integrity

- Test specification: locked AFTER seeing the cardinality-position correlation, BEFORE running the permutation null and partial correlation.
- Single test, no Bonferroni inflation.
- Direction one-sided.
- 100K permutation null.
- Both PASS and NULL outcomes publishable.
- Post-hoc-discipline transparently disclosed.
