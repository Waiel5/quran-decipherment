---
finding_id: h-new-146
title: "Q 50 al-Qāf as mid-mushaf hub — position, content, liturgical, and muq structural profile"
specialist: specialist-B (quran-equation-solvers)
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 3
bonferroni_family: h-new-146-q50-hub
alpha_bon: 0.0167
alpha_raw: 0.05
parent_findings: [cross-finding-010 (mid-mushaf hub), h-new-145 (muq code decoding), h-new-89 (meta-cluster), h-new-134 (MST)]
rules_tuple: "(Hafs-Kūfan; no-tashkeel; QAC v0.4; 114 surahs)"
pre_reg_standard: PRE-REG-STANDARD-04
---

# [[h-new-146-q50-qaf-hub|H-NEW-146]] — Q 50 al-Qāf mid-mushaf hub investigation

## Motivation

[[cross-finding-010-extended-network|Cross-finding-010]]'s extended 4-region hub architecture identifies Q 50 as
the UPPER-MID hub of the Quran (along with Q 2-3 front, Q 59-62
back-upper, Q 112-114 back-terminal). Q 50 is one of only 4 hub-region
surahs.

What makes Q 50 a hub? Three candidate explanations:

1. **Position**: Q 50 sits exactly at mushaf-position 50/114 (44%, near
   the mushaf's middle). A mid-position surah is "equidistant from both
   ends" and may function as a pivot.
2. **Content**: Q 50's opening oath "ق وَٱلْقُرْآنِ الْمَجِيدِ" (by the
   glorious Qurʾān) and closing "فَذَكِّرْ بِٱلْقُرْآنِ" (remind by the
   Qurʾān) form a book-reference frame — Q 50 is a QURAN-reflexive surah.
3. **Single-letter muq ق**: [[h-new-145-muq-code-decoding|H-NEW-145]] REFUTED the classical ق→qiyāma
   interpretation (Q 50 rank 21/29 for qwm+qrA root density). So what
   IS ق-distinctive about Q 50?

This pre-reg tests three falsifiable aspects of Q 50's hub status.

## Hypotheses

### Cell A — Position: mushaf-mid centrality (TEST 1 of 3)

Under [[cross-finding-010-extended-network|cross-finding-010]]'s cluster-network, Q 50 has degree ≥ 4 (mid-hub).
Is Q 50 the UNIQUE mid-position hub, or is it part of a broader mid-
mushaf phenomenon?

**H_A_0**: Q 50's cluster-network degree is NOT distinctive among mid-
position surahs (Q 40-60 range).

**H_A_1**: Q 50 has cluster-network degree strictly greater than the
mean degree of Q 40-60 surahs.

Compute cluster-network degree for all Q 40-60 (21 surahs). Rank Q 50.
PASS: Q 50 is in the top-3 of the 21 Q 40-60 surahs at p < 0.0167 by
permutation null (shuffle degrees across Q 40-60; measure rank).

### Cell B — Content: Qurʾān-reflexivity density (TEST 2 of 3)

Q 50's opening and closing verses both reference the Qurʾān (v1:
"wa-l-qurʾāni al-majīd"; v45: "fa-dhakkir bi-l-qurʾāni man yakhāfu
waʿīd"). Is Q 50 unusually Qurʾān-reflexive?

Operationalize: count QAC STEM root tokens of `qrA` (قرأ) in Q 50; divide
by nverses (45). Compare to all 114 surahs.

**H_B_0**: Q 50's qrA density is NOT in the top-10 of 114 surahs.

**H_B_1**: Q 50's qrA density IS in the top-10 of 114 surahs.

PASS: Q 50's qrA density-rank ≤ 10/114 at p < 0.0167 under null that Q 50
is a random surah (hypergeometric on "top-10 of 114").

### Cell C — Muq-cluster membership (TEST 3 of 3)

Q 50's single-letter muq ق is classically linked to qiyāma ([[h-new-145-muq-code-decoding|H-NEW-145]]
REFUTED this). Alternative: Q 50 might be DISTINCT from other single-letter
muq surahs (Q 38 ص, Q 68 ن) in Fisher-Rao root distribution.

**H_C_0**: Q 50's Fisher-Rao distance to the other 2 single-letter-muq
surahs (Q 38, Q 68) is NOT different from its mean distance to all other
28 muq surahs.

**H_C_1**: Q 50's FR distance to {Q 38, Q 68} is DIFFERENT (either
significantly smaller = single-letter muq forms a content-cluster; OR
significantly larger = Q 50 is distinctive even among single-letter muq).

Compute from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s D-matrix: mean FR(Q 50, {Q 38, Q 68}) vs mean
FR(Q 50, other 28 muq surahs). 2-sided test via permutation: shuffle
which 28 muq surahs are the "singletons" and recompute; how often does
the observed difference arise by chance? 10,000 permutations.

PASS: p_perm 2-sided < 0.0167.

## Bonferroni

- Family = [[h-new-146-q50-qaf-hub|h-new-146]]-q50-hub
- k = 3
- α_bon = 0.05 / 3 = 0.0167
- Cell A (1-sided upper-tail rank test), Cell B (1-sided upper-tail
  density rank), Cell C (2-sided permutation)

## MW-5 positive control

Use a known-non-hub surah (Q 44, mid-position, not a hub per
[[cross-finding-010-extended-network|cross-finding-010]] extended). Run all three cells on Q 44 instead of
Q 50. Expected: Q 44 fails all three cells. If Q 44 passes any, instrument
broken.

## Garden of forking paths

- **Q 40-60 bracket for Cell A**: defined as Q 50 ± 10 surahs. Alternatives
  rejected pre-result: Q 30-70 (too wide, dilutes mid-position signal),
  Q 45-55 (too narrow, only 11 surahs).
- **qrA root only for Cell B**: chosen as the direct "Qurʾān" root per
  classical lexicon. Alternatives rejected pre-result: qwm (too broad,
  includes non-resurrection senses), ktb (covers kitāb but is a broader
  writing concept — tested separately in cross-finding-008).
- **Fisher-Rao source from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]**: same rules-tuple as parent findings.
  No re-derivation.
- **Top-3 threshold for Cell A**: corresponds to the meaningful hub-tier.
  Top-1 is too strict (n=21); top-5 is too loose.
- **Top-10 threshold for Cell B**: ~9% — matches "distinctively high"
  without over-narrowing. Alternatives rejected: top-5 (n=5/114 = 4%;
  near-singleton), top-20 (17%; too permissive).
- **Cell C 2-sided**: no theoretical reason to predict direction; classical
  tafsir is neutral between single-letter-muq-clustering and Q 50-
  distinctiveness.

## Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_146_q50_hub.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-146.json`
- Findings: `findings/phase-b-hypotheses/h-new-146-q50-qaf-hub.md`
- Journal: `journal/h-new-146-run-1.md`

## Pre-committed acceptance matrix

| Cells passed | Verdict |
|---|---|
| 3 of 3 | FULL-HUB-EXPLANATION — position + content + structural distinctiveness together explain Q 50's hub status |
| 2 of 3 | PARTIAL-EXPLANATION — two factors contribute; one dimension is null |
| 1 of 3 | WEAK-HUB — one factor dominates; Q 50's hub status is single-channel |
| 0 of 3 | UNEXPLAINED — Q 50 is a hub by some criterion we haven't operationalized |
| MW-5 fails | INSTRUMENT-BROKEN |

Null and pass published with equal prominence.
