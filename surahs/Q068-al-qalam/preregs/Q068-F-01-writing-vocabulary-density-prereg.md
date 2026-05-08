---
finding_id: Q068-F-01
title: "Q 68 al-Qalam — writing/inscription vocabulary over-density (Ibn ʿAbbās's gloss of ن as functionally announcing al-Qalam)"
date_pre_registered: 2026-05-07
status: PRE-REGISTERED
seed: 20260507
n_perm: 0 (hypergeometric exact, family of 6 roots)
bonferroni_k: 6
bonferroni_family: "Q068-F-01 writing-vocabulary roots {qlm, sTr, ktb, sjl, rqm, lwH}"
alpha_raw: 0.05
alpha_bon: 0.0083333
direction: "POSITIVE — Q 68 expected to over-concentrate at least one writing-vocabulary root after Bonferroni correction; ALSO joint-family test (POSITIVE) for combined writing-vocabulary density"
---

# Q068-F-01 — NŪN-LETTER MUQAṬṬAʿ-CONTENT INTEGRATION

## Hypothesis

**The classical claim** (Ibn ʿAbbās in al-Ṭabarī, *Jāmiʿ al-bayān*, on Q 68:1; al-Suyūṭī, *al-Durr al-manthūr* on Q 68:1) is that the muqaṭṭaʿ-letter ن at Q 68:1 is functionally glossed by *wa-l-qalam* immediately following — i.e., the surah's opening single-letter announces the surah's content theme of writing/inscription.

**The empirical operationalization**: if Ibn ʿAbbās's claim holds at the lexical-density level, then Q 68 should **over-concentrate writing/inscription vocabulary** relative to the corpus, beyond what the surah's length would predict.

## Locked target root family (LOCKED PRE-REG, BEFORE OBSERVATION)

QAC stem-roots:
- **qlm** (qalam, the pen) — corpus-total 4 tokens
- **sTr** (sṭr, sayṭara, satara — to inscribe in lines) — corpus-total 16 tokens
- **ktb** (kataba — to write) — corpus-total 319 tokens
- **sjl** (sajjala, sijill — to record/scroll) — corpus-total 4 tokens
- **rqm** (raqama, marqūm — to inscribe/numerate) — corpus-total 3 tokens
- **lwH** (lawḥ — tablet) — corpus-total 6 tokens

Total writing-vocabulary corpus-tokens: 352 of ~47,822 corpus root-tokens (≈0.74%).

Note: **wḥy** (waḥy / inspiration) is intentionally EXCLUDED — it is a revelation-not-inscription concept, conceptually distinct from the qalam-physical-writing cluster Ibn ʿAbbās's gloss targets. Including it would expand the family beyond the explicit pen/inscription semantic field. **nqs** (engrave/incise) is included only if QAC has tokens for it; pre-check: QAC has 0 tokens, so it is dropped from the test family (no contribution).

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-stem-roots, QAC v0.4 morphological annotations, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

## Null distribution

**Per-root hypergeometric** (Bonferroni-6 family):
- For each root r ∈ {qlm, sTr, ktb, sjl, rqm, lwH}: under the null that the K_r corpus tokens are distributed uniformly across the N corpus root-tokens, how many fall in Q 68's n_68 root-token sample?
- Hypergeometric P(X ≥ k_observed | N, K_r, n_68).
- α_per-test = 0.05 / 6 ≈ 8.33 × 10⁻³.

**Joint-family test (single combined cell)**:
- Combined K = sum(K_r) for r in family.
- Combined k = sum(k_r) observed in Q 68.
- Hypergeometric P(X ≥ k | N, K, n_68) at α = 0.05 (single test, not Bonferroni — this is the family-summary cell).

## Direction (LOCKED)

POSITIVE on both per-root and joint-family levels:
- Q 68 expected to over-concentrate at least one writing-root after Bonferroni-6 correction.
- Q 68 expected to over-concentrate the combined family at raw α = 0.05.

## Success / failure criteria

| Verdict | Per-root level | Joint-family level |
|:--|:--|:--|
| **VINDICATED** | ≥1 root passes p < α_bon | AND joint p < 0.05 |
| **DIRECTIONAL** | ≥1 root passes raw α=0.05, none pass α_bon | OR joint p < 0.05 alone |
| **NULL** | No root passes raw α=0.05 | AND joint p ≥ 0.05 |
| **DIRECTION_REVERSED** | observed total < expected total | (pre-commit violation, published as NULL with prominence per Protocol §1.3) |

## Discriminating context

The classical claim being tested is *not* "Q 68 has more writing-vocabulary than baseline" (that is trivially true — *qalam* and *yasṭurūn* appear in v.1). The claim is the **stronger empirical** version: writing-vocabulary should over-concentrate **beyond the v.1 mention**, throughout the surah body, indicating that the muqaṭṭaʿ-letter functions as a CONTENT-BEACON rather than a LITERARY-ORNAMENT.

Specifically, of the 5 known QAC writing-vocabulary tokens in Q 68 already counted (qlm@v.1, sTr@v.1, sTr@v.15 *asāṭīr*, ktb@v.37, ktb@v.47), only the v.1 ones are part of the opening formula. The v.15, v.37, v.47 occurrences are body-of-surah, and the joint test must register them as over-density.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q068_F_01_writing_vocabulary_density.py`.
- JSON: `csv/Q068-F-01.json`.
- Findings: in `06-novel-findings.md`.
