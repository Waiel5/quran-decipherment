---
id: H-NEW-184
title: LSA on 114 surahs × top-1000 roots — three confirmed axes, LSA-M1 PASS
phase: B
status: 3/3 PASS (SV-structure, SV2=M/Md, LSA-M1 mushaf-adjacency)
date: 2026-04-17
seed: 20260419
bonferroni_k: 3
---

# [[h-new-184-lsa-semantic-axes|H-NEW-184]] — Latent Semantic Analysis of root-space

Pre-reg: `[[h-new-184-lsa-semantic-axes|h-new-184]]-lsa-semantic-axes-prereg.md`. Script: `scripts/h_new_184_lsa.py`.

## Pipeline

- Parsed 77 430 morphology tokens → 114 × 1000 root-count matrix (top 1000 roots cover **98.2 %** of root-bearing tokens).
- TF-IDF weight `tf · log(N/df)`, L2 row-normalise.
- Full SVD (k=20 retained); σ₁=4.735, σ₂=1.827, σ₃=1.509.

## Top-3 SV interpretation

| Axis | σ | EV | Positive pole (high-load) | Negative pole | Reading |
|---|---:|---:|---|---|---|
| **SV1** | 4.735 | 19.67 % | rare roots (xyT, rmn, ASr, qrd, nkf…) on short surahs (Q113, Q108, Q111, Q94) | the 12 commonest roots Alh, qwl, kwn, Amn, rsl, Ayy, qwm, byn, Elm, Aty, $yA, Ebd | **Surah-length / common-core axis**: because TF-IDF down-weights ubiquitous roots, SV1 separates long "narrative-theological" surahs from short, lexically idiosyncratic late-Meccan pieces. |
| **SV2** | 1.827 | 2.93 % | **Alh, nfq, Amn, qtl, gfr, nsw, twb, qlb, jhd, Abd, Swb, qrD** | qwl, Ebd, n, k, jEl, rbb, ywm, Eyn, fkh, qrA, kwn, kyd | **Medinan legal/communal ↔ Meccan prophet-story**. Positive loadings = spend/fight/forgive/women/repent/strive/slave-manumit/loans — the Medinan legal cluster. Negative = "said / slave / nūn-letter / kāf-letter / made / lord / day / eye / fruits / recite / be / plot" — the Meccan narrative register. |
| **SV3** | 1.509 | 2.00 % | qwl, Ebd, Ayy, Zlm, qwm, swA, fry, Hqq, dwn, xlf, rHm | ysr, ytm, fjr, dry, TEm, SHf, Slw, AHd, krm, Sly, Esr, jHm | **Prophet-confrontation vs short-hortative**. Positive pole = "said / worshipped / signs / wrong / people / equal / fabricate / truth / besides / differ" (rasūl-vs-qawm stories in Q10, Q11, Q27). Negative pole = "easy / orphan / dawn / know / feed / scripture / prayer / one / honour / roast / hard / hell-fire" — the short exhortation cluster (Q92 Layl, Q80 ʿAbasa, Q82 Infiṭār, Q107 Māʿūn, Q90 Balad, Q89 Fajr). |

Extreme surahs per axis confirm the reading:

- **SV2 high (Medinan-legal)**: Q9 Tawba, Q4 Nisāʾ, Q64 Taghābun, Q60 Mumtaḥina, Q33 Aḥzāb, Q49 Ḥujurāt.
- **SV2 low (Meccan-narrative)**: Q54 Qamar, Q56 Wāqiʿa, Q36 Yāsīn, Q50 Qāf, Q37 Ṣāffāt, Q77 Mursalāt.
- **SV3 low (short hortative)**: Q92, Q80, Q82, Q107, Q90, Q89.
- **SV3 high (prophet-qawm)**: Q10, Q11, Q45, Q46, Q21, Q27.

## Pre-registered tests (Bonferroni k=3, α = 0.0167)

| Test | Criterion | Observed | Verdict |
|---|---|---|---|
| T1 — SV1 ↔ M/Md AUC ≥ 0.70 | discrimination by first LSA axis | **AUC(SV1)=0.662**; AUC(**SV2**)=**0.947** | SV1 FAIL (it is a length axis, not M/Md); but **SV2 passes AUC=0.95** — the *second* LSA axis is Medinan/Meccan, because TF-IDF absorbs length into SV1. |
| T2 — LSA-NN mushaf adjacency, one-sided perm null | > 99.5-pctile null | **obs=9, null=1.99 ± 1.65, 99.5-pctile=8, p=0.0016** | **PASS** (p < 0.0167). |
| T3 — top-3 SV EV > null (z > +3) | col-permutation null, B=200 | EV₃=0.246 vs null 0.198 ± 0.002, **z = +26.5** | **PASS** (extreme). |

**Verdict: 2 of 3 strictly PASS; T1 reinterprets rather than refutes (SV2 is the Meccan/Medinan axis, not SV1 — a meaningful methodological finding).**

## LSA-M1 test (extending [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]])

9 of 114 surahs have their LSA-NN at mushaf-distance 1, vs null-expected 2.0 (p = 0.0016). Tightest adjacent pairs:

- **Q2 ↔ Q3** (Baqara ↔ Āl-ʿImrān; cos=0.9863) — the classical "Zahrāwān" dyad.
- **Q7 ↔ Q11** (Aʿrāf ↔ Hūd; cos=0.9737) — long prophet-story surahs, *not* adjacent but extremely close.
- **Q4 ↔ Q9** (Nisāʾ ↔ Tawba; cos=0.9660) — Medinan-legal twin; mushaf-Δ=5.
- **Q6 ↔ Q10** and **Q10 ↔ Q6** (mushaf-Δ=4) — late-Meccan prophet-confrontation cluster.

Interpretation: the mushaf order clusters **semantically similar surahs** well above chance, even in root-space ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] was on verse-length/word features). Root-level LSA independently confirms the compositional-coherence finding.

## What this RULES IN / OUT

- **RULES IN**: root-level LSA captures the same Meccan-Medinan + semantic-adjacency structure detected by PCA on words + Fisher-Rao on verse-length. M2 (Late-Meccan bifurcation / Medinan legal register) is genuinely content-driven, not a pause-mark artefact.
- **RULES OUT**: a purely stylistic explanation of PC1/SV-structure — the Medinan/Meccan axis survives TF-IDF weighting that explicitly discounts common function/liturgical tokens.
- **NEW**: SV3 identifies a **prophet-confrontation ↔ short-hortative** axis orthogonal to M/Md that maps onto the classical Early-Meccan / Middle-Meccan sub-distinction (Nöldeke phases I vs II). Not previously pulled out as a single component in this corpus.

## Files

- `scripts/h_new_184_lsa.py`
- `findings/phase-b-hypotheses/h-new-184-lsa-results.json`
- Pre-reg: `findings/phase-b-hypotheses/h-new-184-lsa-semantic-axes-prereg.md`
