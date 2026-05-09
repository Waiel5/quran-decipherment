---
id: H-NEW-1350
title: Allāh-token corpus-wide per-verse coverage distribution and Medinan/Meccan separation
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-1350-allah-density-corpus (single pre-registered test)
alpha_bon: 0.05
direction_of_effect: Medinan surahs have HIGHER mean per-verse Allāh-coverage than Meccan surahs (one-sided Mann-Whitney U; Medinan > Meccan)
origin: Q058-F-01 follow-up — Q 58 al-Mujādala just showed 100% verse-coverage on the *Allāh* substring (22/22 verses). Closed-form null = 6.8×10⁻¹³. Open question: what is the corpus distribution of per-surah Allāh-verse-coverage? Is Q 58 the corpus-MAX? Where does each surah rank? Is the coverage distribution related to Meccan/Medinan status?
verdict_ceiling: PASS-DIRECTED (single pre-registered test; INDEPENDENT REPLICATION required for promotion)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  detection_rule: substring الله in verse text (case insensitive — Arabic has no case; whitespace tolerant)
  chronology_source: data/revelation-order.csv ("period" column — al-Suyūṭī / Tanzil Egyptian Standard + Nöldeke phase)
  null_model: shuffle the 114-vector of Meccan/Medinan labels uniformly across 114 surahs, preserving the 86/28 marginal counts
---

# H-NEW-1350 pre-registration

## Origin

This pre-reg is a direct follow-up to Q058-F-01 (Q 58 al-Mujādala *Allāh*-density corpus-EXACT extreme test), which confirmed that Q 58 has 100% per-verse coverage on the *Allāh* substring (22 of 22 verses) and that this is unique in the corpus (next-closest = strictly < 1.0). Q 58 is unambiguously the corpus-MAX on per-verse coverage at length ≥ 5.

The natural next question is corpus-wide: what is the distribution of per-surah *Allāh* verse-coverage? Q 58 is Medinan. If high-*Allāh*-coverage is a Medinan signature, the corpus distribution should show Medinan surahs systematically above Meccan ones. This pre-reg locks the single primary test (Medinan > Meccan on per-verse *Allāh* coverage) before any computation.

## Hypothesis (single primary test)

**H1**: Per-surah per-verse *Allāh*-coverage (= fraction of verses in the surah containing the substring الله) is HIGHER for the 28 Medinan surahs than for the 86 Meccan surahs.

**Test statistic**: one-sided Mann-Whitney U (Medinan > Meccan).

**Null distribution**: 10,000 random permutations of the 114-vector of period labels (86 "Meccan" + 28 "Medinan"), preserving marginals.

**Decision rule**: PASS if p_perm ≤ 0.05 (single test, no Bonferroni since k = 1).

## Direction lock

Direction is LOCKED before computation: **Medinan > Meccan**. The reverse direction (Meccan > Medinan or null) is NOT a reportable PASS — it must be published as NULL, with the observed Mann-Whitney p_perm reported regardless of sign.

The directional prior is grounded in classical observation: Medinan surahs concern community law, treaty, and divine ordinance (the *Allāh* invocation is structurally frequent — cf. al-Suyūṭī, *al-Itqān*, nawʿ 9-10 on Meccan-vs-Medinan markers; Medinan surahs frequently contain *yā ayyuhā alladhīna āmanū* + *Allāh* command clauses). The directional prior is NOT post-hoc: it is a textbook al-Suyūṭī correlate.

## Descriptive output (NOT part of the pre-registered hypothesis)

Beyond H1, the script computes (descriptively, not for hypothesis testing):

1. **Per-surah coverage table** (114 rows): surah id, n_verses, n_verses_with_allah, coverage_fraction, period.
2. **Corpus rank**: sort all 114 surahs by coverage; report top-10 and where Q 58 lands.
3. **Group statistics**: mean / median / std of coverage for Meccan vs Medinan.
4. **Q 58 corpus rank**: confirm Q 58 is the corpus-MAX (consistent with Q058-F-01).

These descriptive outputs do NOT carry their own α — they are summary statistics on the same instrument as H1.

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Tashkeel | no-tashkeel (`quran-text/quran-no-tashkeel.json`) |
| Token level | substring match on grapheme sequence الله (4 chars: ا ل ل ه) |
| Counting unit | verse (binary per-verse: has-substring vs not) |
| Basmala | counted only in Q 1 (Q 1's verse 1 is *bi-smi llāhi*, which contains الله) — consistent with default rules-tuple |
| Reading tradition | Hafs-Kufan (the canonical text we have on disk) |
| Script | Mashriqi |
| Chronology | `data/revelation-order.csv` "period" column (86 Meccan + 28 Medinan) |

**Note on substring detection**: The substring الله matches both the standalone divine name *Allāh* and morphological derivatives whose orthographic skeleton contains الله (e.g., *bi-llāh*, *li-llāh*, *fa-llāh*, *Allāhumma*, *wa-llāh*). This is the SAME rule used in Q058-F-01 and is locked for consistency. A strict-isolated-token variant is included as a robustness check but does not bear on H1.

## Permutation null protocol

1. Compute observed Mann-Whitney U statistic on the real 86 Meccan vs 28 Medinan coverage vectors (one-sided, Medinan > Meccan).
2. Set RNG seed = 20260509.
3. For 10,000 iterations: shuffle the 114-vector of period labels (preserving the 86/28 marginal). Recompute the U statistic on the shuffled labels.
4. p_perm = (1 + count of perm-U ≥ observed-U) / (1 + N_PERM).

This is an exact-style label-permutation test — robust to coverage distribution shape (no normality assumption).

## Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| p_perm ≤ 0.05, direction = Medinan > Meccan | PASS-DIRECTED |
| p_perm > 0.05, direction = Medinan > Meccan | NULL |
| direction = Meccan ≥ Medinan (any p) | NULL (pre-commit-honoring; published with observed p) |

Single test (k=1); no Bonferroni adjustment.

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: Substring detection + verse-coverage statistic locked above. Mann-Whitney U locked. Null model locked.
- **MW-2 (corpus-prior)**: 10,000 permutations; minimum standard met.
- **MW-3 (alternative-models)**: A secondary metric (per-word density instead of per-verse coverage) is computed descriptively but does NOT trigger an additional hypothesis.
- **MW-4 (over-fitting)**: No fitted parameter; the test is non-parametric and uses an integer-count statistic.
- **MW-5 (replication)**: PASS-DIRECTED is the verdict ceiling. Independent replication required for CONFIRMED.
- **MW-6 (instrument-control)**: The shuffled-label null preserves the marginal 86/28 — the same data, the same statistic, but with labels broken. Any genuine Medinan/Meccan signal cannot survive this shuffle.
- **MW-7 (post-hoc cap)**: Single planned test; no post-hoc dimensions.

## Garden-of-forking-paths disclosure

- The Medinan > Meccan direction is the al-Suyūṭī classical prior (community-law surahs invoke *Allāh* more densely). No "Meccan > Medinan" direction was considered or pre-computed.
- The substring rule الله is the same rule used in Q058-F-01. No alternative substring patterns were tested before pre-reg lock.
- The chronology source is `data/revelation-order.csv`. No alternative chronology (Bell 1937, Nöldeke 1860 directly) was considered for this test, though the file already incorporates Nöldeke phase info.
- The test is one-sided (Medinan > Meccan). A two-sided test was NOT considered, because the prior is sign-locked.
- No sub-cluster analysis (e.g., Late-Meccan vs Medinan) is pre-registered. Only the binary period split is tested.

## Connection to existing findings

- **Q058-F-01**: this pre-reg's instrument (per-verse *Allāh* coverage substring rule) is identical to Q058-F-01's H1. The 114-surah coverage vector this script computes is a strict super-set of Q058-F-01's H2 (corpus-uniqueness check at length ≥ 5).
- **Cross-finding-012 Late-Meccan apparatus**: Medinan surahs are a sub-set of the Pattern-B Late-Meccan/Medinan continuum. A PASS here would extend the apparatus to Allāh-density.
- **al-Suyūṭī al-Itqān nawʿ 9-10**: classical Meccan-vs-Medinan markers. If H1 PASSES, this test provides an empirical confirmation of one of the classical markers.

## Anti-flip

The reverse direction (Meccan > Medinan or null) is NOT a reportable PASS. The verdict for any direction not matching the lock is NULL — even if Meccan > Medinan would be "interesting." This is a hard pre-commit.

## Pre-commit attestation

Locked by SHA256. Run script verifies before computation. SHA computed after this file is finalized; embedded in the run script as EXPECTED_SHA. Any mismatch = fail-fast.
