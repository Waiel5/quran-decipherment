---
id: H-NEW-1350
title: Allāh-token corpus-wide per-verse coverage distribution — Medinan/Meccan separation
date: 2026-05-09
verdict: PASS-DIRECTED
verdict_ceiling: PASS-DIRECTED (single planned test; INDEPENDENT REPLICATION required for promotion)
pre_reg_sha256: b41ee6b93e09a1ab25655a50edb4ad0f6e14198e4a7a12f34d2e8b6a90bd434f
seed: 20260509
n_perm: 10000
p_perm_one_sided: 0.00010
u_observed: 2218.0
u_expected: 1204.0
u_max: 2408
direction_locked: Medinan > Meccan
direction_observed: Medinan > Meccan
rules_tuple: (no-tashkeel, orthographic-token, substring الله, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# H-NEW-1350 — Allāh-token corpus-wide per-verse coverage distribution and Medinan/Meccan separation

## TL;DR

Per-surah per-verse *Allāh* coverage (fraction of verses containing the substring الله) is dramatically higher for Medinan surahs than Meccan: mean 0.622 vs 0.120, median 0.685 vs 0.045. One-sided Mann-Whitney U with 10,000 label permutations gives **p_perm = 0.00010 (0/10000 ≥ observed)**, in the pre-committed direction. The **top-10 surahs by Allāh-coverage are 10/10 Medinan**; the **bottom-10 are 10/10 Meccan**. **Q 58 al-Mujādala is the corpus-MAX (rank 1/114, coverage 1.000)**, confirming and extending Q058-F-01.

**Verdict: PASS-DIRECTED.**

## Pre-registration

- **File**: `findings/phase-b-hypotheses/prereg-h-new-1350-allah-density-corpus.md`
- **SHA256**: `b41ee6b93e09a1ab25655a50edb4ad0f6e14198e4a7a12f34d2e8b6a90bd434f`
- **Direction locked**: Medinan > Meccan
- **Test**: one-sided Mann-Whitney U; 10,000 random shuffles of period labels (preserves 86/28 marginals)
- **Decision rule**: PASS if p_perm ≤ 0.05 (single test; k=1)

## Method

**Instrument**: For each verse `(s,v)`, set `has_allah[s,v] = 1` if the substring الله occurs anywhere in the no-tashkeel text, else 0. Per-surah coverage = (# verses with الله) / (# verses).

**Data sources**:
- Text: `quran-text/quran-no-tashkeel.json`
- Chronology: `data/revelation-order.csv` "period" column (al-Suyūṭī / Tanzil Egyptian Standard + Nöldeke phase); 86 Meccan + 28 Medinan = 114

**Statistic**: Mann-Whitney U with mid-rank tie correction. `U(Medinan vs Meccan)` is the count of Medinan-coverage values strictly exceeding Meccan-coverage values (with ½ credit for ties). Larger U = more extreme in the pre-committed direction.

**Null**: 10,000 random shuffles of the 114-vector of period labels (preserving 86/28 marginals); recompute U on shuffled labels; p_perm = (1 + #{U_perm ≥ U_obs}) / (1 + N_PERM).

## Results

### Primary test (H1: Medinan > Meccan)

| Quantity | Value |
|:--|--:|
| n_meccan | 86 |
| n_medinan | 28 |
| mean Meccan coverage | 0.1204 |
| mean Medinan coverage | 0.6222 |
| median Meccan coverage | 0.0446 |
| median Medinan coverage | 0.6849 |
| U(Medinan vs Meccan) observed | 2218.0 |
| U expected under null | 1204.0 |
| U max possible | 2408 (= 86 × 28) |
| Direction observed | Medinan > Meccan |
| Direction matches pre-reg | ✓ |
| **p_perm (one-sided)** | **0.00010** |
| **#perm ≥ observed (of 10000)** | **0** |

The observed U is 2218 out of a maximum of 2408 — i.e., Medinan surahs out-rank Meccan surahs in 92.1% of all 2408 pairwise comparisons. Under the null, the expected value is 1204; the observed value is +1014 above expectation. 0/10000 random label shuffles produced a U statistic this extreme. The permutation null bottoms out at p ≈ 1/10001 ≈ 10⁻⁴.

### Top-10 by per-verse coverage (descriptive)

| Rank | Surah | n_verses | Allāh-verses | Coverage | Period |
|:--:|:--:|--:|--:|--:|:--|
| 1 | Q 58 al-Mujādala | 22 | 22 | 1.0000 | Medinan |
| 2 | Q 48 al-Fatḥ | 29 | 25 | 0.8621 | Medinan |
| 3 | Q 60 al-Mumtaḥana | 13 | 11 | 0.8462 | Medinan |
| 4 | Q 24 al-Nūr | 64 | 50 | 0.7812 | Medinan |
| 5 | Q 49 al-Ḥujurāt | 18 | 14 | 0.7778 | Medinan |
| 6 | Q 9 al-Tawba | 129 | 100 | 0.7752 | Medinan |
| 7 | Q 4 al-Nisāʾ | 176 | 132 | 0.7500 | Medinan |
| 8 | Q 65 al-Ṭalāq | 12 | 9 | 0.7500 | Medinan |
| 9 | Q 5 al-Māʾida | 120 | 88 | 0.7333 | Medinan |
| 10 | Q 63 al-Munāfiqūn | 11 | 8 | 0.7273 | Medinan |

**10 of 10 top-coverage surahs are Medinan**. The implied 1-tailed hypergeometric probability of drawing 10 Medinan from 28 Medinan + 86 Meccan in 10 draws is C(28,10)/C(114,10) ≈ 4.4×10⁻⁶ — an independent corroboration of the Mann-Whitney result by a completely different statistic.

Q 58 is confirmed as corpus-MAX at coverage = 1.000 (consistent with Q058-F-01's H1 and H2).

### Bottom-10 by per-verse coverage (descriptive)

| Rank | Surah | n_verses | Coverage | Period |
|:--:|:--:|--:|--:|:--|
| 105 | Q 102 al-Takāthur | 8 | 0.0000 | Meccan |
| 106 | Q 103 al-ʿAṣr | 3 | 0.0000 | Meccan |
| 107 | Q 105 al-Fīl | 5 | 0.0000 | Meccan |
| 108 | Q 106 Quraysh | 4 | 0.0000 | Meccan |
| 109 | Q 107 al-Māʿūn | 7 | 0.0000 | Meccan |
| 110 | Q 108 al-Kawthar | 3 | 0.0000 | Meccan |
| 111 | Q 109 al-Kāfirūn | 6 | 0.0000 | Meccan |
| 112 | Q 111 al-Masad | 5 | 0.0000 | Meccan |
| 113 | Q 113 al-Falaq | 5 | 0.0000 | Meccan |
| 114 | Q 114 al-Nās | 6 | 0.0000 | Meccan |

**10 of 10 bottom-coverage surahs are Meccan, all with zero Allāh-coverage**. These are the short late-mushaf surahs (mostly Early Meccan).

### Secondary descriptive: per-word density (NOT part of H1)

| Rank | Surah | Allāh per word | Count | Period |
|:--:|:--:|--:|:--:|:--|
| 1 | Q 112 al-Ikhlāṣ | 0.1333 | 2/15 | Meccan |
| 2 | Q 110 al-Naṣr | 0.1053 | 2/19 | Medinan |
| 3 | Q 58 al-Mujādala | 0.0842 | 40/475 | Medinan |
| 4 | Q 65 al-Ṭalāq | 0.0830 | 24/289 | Medinan |
| 5 | Q 64 al-Taghābun | 0.0785 | 19/242 | Medinan |
| 6 | Q 49 al-Ḥujurāt | 0.0765 | 27/353 | Medinan |
| 7 | Q 61 al-Ṣaff | 0.0708 | 16/226 | Medinan |
| 8 | Q 33 al-Aḥzāb | 0.0683 | 89/1303 | Medinan |
| 9 | Q 8 al-Anfāl | 0.0681 | 85/1248 | Medinan |
| 10 | Q 9 al-Tawba | 0.0665 | 167/2511 | Medinan |

Per-word density has Q 112 al-Ikhlāṣ on top — a 4-verse Meccan creed surah whose *every other content-word is Allāh* (e.g., *qul huwa **llāh**u aḥad / **allāh**u al-ṣamad*). Q 112 inverts the per-verse coverage view: its 4 verses give it limited verse-coverage rank, but per word it is the densest in the corpus. This is a separate phenomenon from the Medinan/Meccan structural pattern H1 captures and is reported here purely descriptively.

## Honest limits and NULL-prominence notes

- **Single-test verdict ceiling**: PASS-DIRECTED. Promotion to CONFIRMED requires independent replication (e.g., a Nöldeke-only chronology variant, a strict-isolated-token detection rule, or a Late-Meccan-only sub-set test).
- **Chronology dependency**: The al-Suyūṭī/Tanzil/Nöldeke binary period split is the standard but not infallible. The result is so extreme (0/10000 perms) that even substantial chronology re-labeling errors should not collapse the signal — but this should be tested explicitly.
- **Substring rule includes prefixed forms**: الله matches *Allāh*, *bi-llāh*, *li-llāh*, *wa-llāh*, *fa-llāh*, *Allāhumma*, etc. The signal is on the *Allāh*-orthographic-skeleton, not strictly on standalone *Allāh* tokens. The strict-isolated-token variant was confirmed for Q 58 in Q058-F-01 (22/22) but not corpus-wide here.
- **Per-word density inversion**: Q 112 outranks Q 58 on per-word density; per-verse coverage and per-word density measure different aspects of the Allāh distribution. H1 is locked to per-verse coverage; the per-word density top-10 is descriptive and serves as a robustness sketch (still 9/10 Medinan).
- **Garden of forking paths**: The direction was pre-locked from al-Suyūṭī's classical Meccan-vs-Medinan markers (*al-Itqān* nawʿ 9-10). This is a pre-existing classical hypothesis, not a post-hoc selection. Direction match is honest.

## Connection to existing findings

- **Q058-F-01**: This test confirms and corpus-contextualizes Q 58's verdict. Q 58 is unambiguously the corpus-MAX (1/114).
- **Cross-finding-008** (muqaṭṭāʿat unique introduction-marker class): The Medinan/Meccan separation on Allāh-coverage is a 2nd-order axis (chronological), orthogonal to muqaṭṭāʿat structure. No collision with cross-finding-008.
- **Cross-finding-012** (Late-Meccan apparatus): Medinan ⊂ later-chronology in al-Suyūṭī's scheme. The Allāh-coverage gradient may also show a Late-Meccan tilt within the Meccan group; pre-registered test of *that* sub-hypothesis is left to a follow-up.
- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 9-10** (Meccan/Medinan markers): This finding empirically corroborates one of al-Suyūṭī's listed Medinan markers — high *Allāh* invocation density — at p_perm = 0.00010 against label-shuffle null.

## Replication candidates (for future sessions)

1. **Nöldeke-only chronology**: re-run with `noldeke_order` and `noldeke_phase` columns instead of "period."
2. **Strict-isolated-token variant**: run with `t == 'الله'` exact-token match (already partially Q 58-confirmed).
3. **Late-Meccan vs Medinan sub-split**: test whether Late-Meccan surahs are intermediate between Early/Middle Meccan and Medinan on Allāh-coverage.
4. **Cross-corpus baseline**: compute the same statistic on pre-Islamic poetry and Bukhari hadith to verify the signal is Quran-specific.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-1350-allah-density-corpus.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-1350.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-1350.json`
- this file: `findings/phase-b-hypotheses/h-new-1350-allah-density-corpus.md`

## One-line summary

Per-verse *Allāh*-coverage is corpus-extreme separated by chronology: mean Medinan 0.622 vs mean Meccan 0.120, U=2218/2408, p_perm=0.00010; top-10 = 10/10 Medinan; bottom-10 = 10/10 Meccan; Q 58 is corpus-MAX at 1.000 (1/114). PASS-DIRECTED.
