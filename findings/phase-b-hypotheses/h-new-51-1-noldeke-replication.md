---
id: H-NEW-51.1
title: Muqaṭṭaʿāt Cardinality vs Nöldeke Chronological Order — DIRECTIONAL-REVERSE replication
phase: B
status: DIRECTIONAL-REVERSE on H-NEW-51 prediction; SUBSTANTIVE pattern reinforced
date: 2026-04-16
agent: integrator (main session)
parent: H-NEW-51 (cardinality-position decline in mushaf order)
chronology_source: Nöldeke (per Tanzil + Wikipedia compilation), data/revelation-order.csv
seed: 20260416
n_perm: 100,000
verdict: DIRECTIONAL-REVERSE (with substantive pattern reinforcement)
rules_tuple: (hafs-kufan; Nöldeke chronological order)
---

# [[h-new-51-1-noldeke-replication|H-NEW-51.1]] — Nöldeke Chronological Replication of [[h-new-51-cardinality-position-decline|H-NEW-51]] (RESULT)

## Headline

**Pre-registered prediction (one-sided lower)**: cardinality should DECREASE with Nöldeke chronological order, replicating the [[h-new-51-cardinality-position-decline|H-NEW-51]] mushaf-order result.

**Result**: ρ(Nöldeke, cardinality) = **+0.5374** — POSITIVE direction, OPPOSITE to prediction. Permutation p = 0.0033 (two-sided), p = 0.998 (one-sided lower as predicted).

**Strict pre-reg verdict**: DIRECTIONAL-REPLICATION FAILS. The predicted direction (decline) does not hold under chronology.

**Substantive observation**: cardinality is MONOTONICALLY related to surah position under either ordering, with opposite signs reflecting the opposite directions of the two orderings.

## The data

29 muqaṭṭaʿāt-opened surahs sorted by Nöldeke chronological order:

| Nöldeke order | Mushaf | Subset | Cardinality |
|---|---|---|---|
| 18 | Q 68 | ن | **1** ← earliest revealed muqaṭṭaʿāt |
| 53 | Q 44 | حم | 2 |
| 54 | Q 50 | ق | **1** |
| 55 | Q 20 | طه | 2 |
| 56 | Q 26 | طسم | 3 |
| 57 | Q 15 | الر | 3 |
| 58 | Q 19 | كهيعص | 5 |
| 59 | Q 38 | ص | **1** |
| 60 | Q 36 | يس | 2 |
| ... | ... | ... | ... |
| 87 | Q 7 | **المص** | **4** ← late |
| 88 | Q 46 | حم | 2 |
| 90 | Q 13 | **المر** | **4** ← latest |
| 91 | Q 2 | الم | 3 |
| 97 | Q 3 | الم | 3 (Medinan) |

The 3 single-letter muqaṭṭaʿāt {ن, ق, ص} are EARLIEST-revealed (Nöldeke 18, 54, 59).

The 2 four-letter muqaṭṭaʿāt {المص, المر} are LATEST-revealed (Nöldeke 87, 90).

The medinan الم instances are at Nöldeke 91, 97 (very latest).

## Three correlations and the partial

| Correlation | Value |
|---|---|
| ρ(Nöldeke, cardinality) | **+0.54** |
| ρ(Nöldeke, length) | +0.05 (tiny) |
| ρ(length, cardinality) | +0.23 |

Partial ρ(Nöldeke, cardinality | length) = **+0.54** (essentially unchanged from raw)

So the Nöldeke→cardinality association is INDEPENDENT of length (length is not a confounder for the chronology relationship, unlike for the mushaf relationship).

## Permutation null test

100,000 permutations, seed 20260416. Shuffle cardinalities among the 29 muqaṭṭaʿāt-opened surahs; recompute ρ(Nöldeke, cardinality).

| Statistic | Value |
|---|---|
| Observed ρ | +0.5374 |
| Null mean ρ | +0.0011 |
| p_one_sided_upper (ρ ≥ obs) | 0.00167 |
| p_one_sided_lower (ρ ≤ obs, AS PRE-REGISTERED) | 0.99834 |
| p_two_sided | 0.00334 |

## Interpretation

**The directional-replication of [[h-new-51-cardinality-position-decline|H-NEW-51]] FAILS** because mushaf order and Nöldeke chronological order are ANTI-CORRELATED for the 29 muqaṭṭaʿāt-opened surahs:

- Q 68 ن is at the END of the mushaf (mushaf rank 68/114) but EARLY in chronology (Nöldeke 18)
- Q 2 الم is at the START of the mushaf (rank 2/114) but LATE in chronology (Nöldeke 91)

The cardinality decreases with mushaf position AND increases with chronology — these are CONSISTENT findings about the same underlying pattern, viewed through opposite orderings.

## What this DOES tell us

The muqaṭṭaʿāt design exhibits a **temporal-progression pattern**: the muqaṭṭaʿāt opening became MORE COMPLEX over the revelation period.

| Period | Muqaṭṭaʿāt cardinality |
|---|---|
| Earliest (Nöldeke 18-60) | mostly 1-2 letter (3 of 3 singletons fall here) |
| Middle (Nöldeke 60-80) | mostly 2-3 letter |
| Late (Nöldeke 80-100) | mostly 3-4 letter (both 4-letter subsets here) |

The 5-letter كهيعص (Q 19, Nöldeke 58) is an early-mid outlier; 5-letter حمعسق (Q 42, Nöldeke 83) is a late outlier. So 5-letter is split.

Mechanism candidates:

1. **Revelatory-elaboration hypothesis**: as the revelation progressed, muqaṭṭaʿāt designs grew more letter-elaborate. The single-letter ن (Q 68) and ق (Q 50) appeared first as simpler signals; longer letter-clusters like المص and المر appeared later.

2. **Mushaf-design hypothesis**: in canonical mushaf compilation, the longest surahs (predominantly Medinan / late-revealed) were placed first; this NATURALLY puts the more-elaborate muqaṭṭaʿāt openers at the start.

3. **Both**: revelatory progression PLUS mushaf compilation choice JOINTLY produce the cardinality-position pattern. Both axes show monotonic structure with cardinality.

## Reconciliation with [[h-new-51-cardinality-position-decline|H-NEW-51]]

| Finding | Verdict | Mechanism reading |
|---|---|---|
| [[h-new-51-cardinality-position-decline|H-NEW-51]] (mushaf order) | PASS-DIRECTED p=2e-5 partial | cardinality decreases with mushaf position |
| [[h-new-51-1-noldeke-replication|H-NEW-51.1]] (Nöldeke order) | DIRECTIONAL-REVERSE | cardinality INCREASES with chronology |

These are CONSISTENT, not contradictory. They jointly support: **muqaṭṭaʿāt cardinality has a strong monotonic relationship with surah position under multiple orderings.**

The DIRECTION depends on the ordering's relationship to revelatory chronology. Mushaf ≈ inverse chronology for this subset, so mushaf-decrease ≈ chronology-increase.

## What status does [[h-new-51-cardinality-position-decline|H-NEW-51]] now hold?

Per the project's discipline:
- [[h-new-51-cardinality-position-decline|H-NEW-51]] was PASS-DIRECTED (post-hoc, p=2×10⁻⁵ partial in mushaf order)
- [[h-new-51-1-noldeke-replication|H-NEW-51.1]] was queued as INDEPENDENT REPLICATION on a distinct dimension (chronology vs mushaf)
- The directional replication FAILS strictly (predicted decrease in chronology, observed increase)
- The substantive replication SUCCEEDS (pattern exists in both orderings, in opposite directions)

**Honest verdict**: [[h-new-51-cardinality-position-decline|H-NEW-51]] status REMAINS PASS-DIRECTED. The replication did not strictly support the predicted direction; the substantive pattern is reinforced but the upgrade to CONFIRMED requires a NEW independent dimension (e.g., al-Suyūṭī chronology, or Bāzargān chronology, or a content-based ordering).

H-NEW-51.2 queued: replicate using al-Suyūṭī chronology (which differs from Nöldeke for some surahs) for triangulation.

## Honest caveats

- The Nöldeke chronology is contested and dataset-dependent. The Tanzil Egyptian Standard + Wikipedia compilation is one of several valid orderings.
- [[h-new-51-1-noldeke-replication|H-NEW-51.1]] was pre-registered as a DIRECTIONAL replication; the result is a directional reversal but with consistent magnitude pattern. The "substantive replication" framing is HONEST but does NOT rescue the strict directional pre-reg.
- The temporal-elaboration mechanism interpretation is supported by the data but not pre-registered.
- The single-letter cluster {ن, ق, ص} being chronologically earliest is a striking pattern that classical scholarship has noted qualitatively; the project provides quantitative support.

## Cross-finding context

[[h-new-51-cardinality-position-decline|H-NEW-51]] + [[h-new-51-1-noldeke-replication|H-NEW-51.1]] jointly indicate:
- The 14 muqaṭṭaʿāt subsets were not assigned to surahs randomly; their cardinality has a temporal-progression relationship
- Both mushaf order and revelation order encode this relationship (in opposite signs)
- The pattern is CONSISTENT with revelatory elaboration hypothesis (muqaṭṭaʿāt grew more complex over time)

## Integrity

- Pre-registration was specific (one-sided lower direction) per [[h-new-51-cardinality-position-decline|H-NEW-51]] protocol.
- Result is reported AS-IS: directional reversal.
- Substantive observation is reported transparently as a separate observation, NOT as a pre-registered confirmation.
- 100K permutations; seed 20260416.
- Closed-form Spearman + permutation null.
