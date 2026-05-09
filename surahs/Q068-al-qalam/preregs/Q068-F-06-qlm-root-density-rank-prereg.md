---
finding_id: Q068-F-06
title: "Q 68 al-Qalam — *qlm* root density rank in corpus (title-density audit)"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: 0 (exact corpus enumeration; hypergeometric backup)
bonferroni_k: 1
bonferroni_family: "Q068-F-06 (single test on qlm-density rank)"
alpha_raw: 0.05
alpha_bon: 0.05
direction: "POSITIVE — Q 68 expected to be in TOP-3 surahs by *qlm* root density per 1000 QAC root-tokens"
---

# Q068-F-06 — *qlm* ROOT DENSITY CORPUS RANK (TITLE-DENSITY AUDIT)

## Hypothesis

Q 68 is named *Sūrat al-Qalam* (the pen). Classical naming conventions (al-Suyūṭī, *al-Itqān*, nawʿ 17 on surah-naming via *ism al-ʿalam*) hold that surah-names typically derive from a distinctive lexical item in the surah body. If the naming convention holds at the empirical-density level, then Q 68 should be in the **TOP-3** of all 114 surahs ranked by *qlm* root density (per 1000 QAC root-tokens).

This is the **title-density-rank** operationalization. The pre-reg locks "TOP-3" rather than "RANK-1" because the *qlm* root has only 4 corpus-total tokens (across 4 surahs: Q 3, Q 31, Q 68, Q 96), making density inherently small-N and rank-volatile.

## Locked operationalization

For each surah s ∈ {1, ..., 114}:
- Extract QAC stem-root tokens from `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.
- Count `n_s` = total root-tokens in surah s.
- Count `k_s` = root-tokens with ROOT:qlm.
- Density: `dens_s = (k_s / n_s) * 1000` (per 1000 root-tokens).
- Rank all 114 surahs by dens_s descending.
- Locate Q 68's rank.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

## Null distribution

This is a **corpus-EXACT enumeration**, not a permutation test. The rank is a fact about the data, not a draw from a null. However, for interpretive context:
- Hypergeometric P(Q 68 has ≥ k_68 qlm-tokens | corpus K=4, n_68 root-tokens): probability of Q 68 being at least as qlm-dense as observed under uniform-distribution null.

## Direction (LOCKED)

POSITIVE: Q 68 expected to be in TOP-3 by qlm-density.

A reversed direction (Q 68 NOT in top-3) would be a pre-commit violation, published as NULL with prominence per Protocol §1.3.

## Success / failure criteria

| Verdict | Criterion |
|:--|:--|
| **VINDICATED-RANK-EXACT** | Q 68 is RANK-1 by qlm-density |
| **VINDICATED-TOP-3** | Q 68 is RANK 2 or RANK 3 |
| **DIRECTIONAL** | Q 68 is RANK 4 or below but in top-decile (rank ≤ 11) |
| **NULL** | Q 68 below top-decile |
| **DIRECTION_REVERSED** | Q 68 has 0 qlm tokens |

## Pre-committed interpretive context

The classical title-density expectation assumes the name reflects high-density usage. For Q 68:
- Q 68:1 has the single *qalam* token (in the oath formula).
- This is 1 token in 508 surah-internal QAC tokens.
- Q 96 has *qalam* in v.4 (*alladhī ʿallama bi-l-qalam*) within 111 surah-internal QAC tokens — Q 96 should therefore have HIGHER density.

If the result is "Q 96 rank-1, Q 68 rank-2" — this is **VINDICATED-TOP-3** but ALSO reveals a fascinating structural pattern: the chronological-#1 surah (Q 96) has the higher *qalam* density than the title-eponymous surah (Q 68). This is the *qalam-chronology-paired* observation also tested in Q068-F-07.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q068_F_06_qlm_density_rank.py`.
- JSON: `csv/Q068-F-06.json`.
- Findings: in `06-novel-findings.md`.
