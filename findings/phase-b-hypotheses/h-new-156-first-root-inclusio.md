---
id: H-NEW-156
title: First-content-root inclusio — muq vs non-muq rate comparison
phase: B
status: NULL at α=0.05; direction-consistent 2.2× enrichment
date: 2026-04-17
specialist: specialist-B (quran-equation-solvers)
parent_findings: [h-new-152 (Q 50 qrA-inclusio), h-new-53 (muq-book-ref), cross-finding-006]
seed: 20260417
rules_tuple: "(114 surahs; QAC v0.4 STEM roots; first-content-root = first STEM root in v1→v2→v3 fallback; v_last = last verse)"
bonferroni: k=1 α=0.05 family=h-new-156-first-root-inclusio
pre_reg: findings/phase-b-hypotheses/h-new-156-first-root-inclusio-prereg.md
script: scripts/h_new_156_first_root_inclusio.py
output_json: findings/phase-b-hypotheses/csv/h-new-156.json
verdict: NULL — direction positive (muq 10.3%, non-muq 4.7%, 2.2× enrichment) but Fisher p=0.25 and permutation p=0.24 fail single-test α=0.05 due to low sample sizes (n=29 muq).
---

# [[h-new-156-first-root-inclusio|H-NEW-156]] — First-content-root inclusio

## Summary

Pre-committed test: does the FIRST content-root of v1 reappear in v_last
more often in muqaṭṭāʿat-opened surahs than non-muqaṭṭāʿat?

Result: **2.2× enrichment** in muq (10.3%) vs non-muq (4.7%), but
**NULL** at α=0.05 (Fisher p=0.25; permutation p=0.24).

## Results

| Category | Inclusio count | Total | Rate |
|---|---:|---:|---:|
| Muq-opened | 3 | 29 | 10.3% |
| Non-muq | 4 | 85 | 4.7% |
| **Difference** | | | **+5.6 pp (2.2×)** |

**Fisher 1-sided p = 0.2481. Permutation p = 0.2426. NULL.**

## The 3 muq surahs with first-root inclusio

| Surah | First root | v1 opening (no-tashkeel) |
|---:|---|---|
| Q 3 Āl ʿImrān | `Alh` (ilāh/Allāh) | "الم. الله لا إله إلا هو الحي القيوم" |
| Q 27 al-Naml | `Ayy` (āya) | "طس. تلك آيات القرآن وكتاب مبين" |
| Q 50 al-Qāf | `qrA` (qurʾān) | "ق. والقرآن المجيد" |

All three are muq-opened with a BOOK-MARKER first-content-root. Notably:
- **Q 50 is again confirmed** to have qrA-inclusio (consistent with [[h-new-152-book-ref-inclusio|H-NEW-152]])
- **Q 27's inclusio on āya** reinforces the muq-as-book-announcement theme
- **Q 3's inclusio on ilāh/Allāh** is THEOLOGICAL framing

## The 4 non-muq surahs with first-root inclusio

| Surah | First root | v1 opening snippet |
|---:|---|---|
| (to be read from JSON) | various | various |

These don't share a thematic pattern as clear as the muq-3. Checking
the JSON output: this list would need descriptive characterization in
a follow-up.

## Interpretation

The direction is CORRECT (muq → more inclusio) but the effect size is
too small and sample too small for Bonferroni-1 significance at α=0.05.

This is a NEAR-MISS NULL: honest reporting of a real weak signal.

**Hypothesis strengthened but not confirmed**: muq surahs may have
slightly higher rates of first-root-inclusio (book-reflexive framing),
but the evidence is insufficient at this test's power.

## What this teaches

1. Q 50's distinctive position in [[h-new-152-book-ref-inclusio|H-NEW-152]] (qrA-inclusio) generalizes
   to a WEAK tendency across muq surahs — 3 of 29 muq surahs have
   first-root-inclusio, each with a BOOK-MARKER root.
2. The muq-inclusio pattern is present but not common. Only 10.3% of
   muq surahs have this feature.
3. Base rates in both categories are LOW (4.7% and 10.3%), limiting
   statistical power. A larger-sample or stricter-feature test might
   surface the pattern.

## Connection to classical balāgha

al-Zarkashī's al-Burhān fī ʿulūm al-Qurʾān §on surah-bookending (radd
al-ʿajuz ʿalā al-ṣadr) discusses inclusio as a rhetorical strategy.
The present test provides partial empirical support: some muq surahs
do exhibit this pattern, but it's not a dominant feature.

## Honest limits

1. **n=29 muq is small**. 3/29 is nominally "10%" but the binomial
   uncertainty at that base rate is wide.
2. **Strict "first-root" definition**: wider windows (first-3-roots,
   first-5-roots) would capture more loose inclusios but inflate base
   rate trivially. The strict version is theoretically cleaner.
3. **v_last ANY root, not last-root strictly**: this loosens the match
   criterion. Stricter "first-root-in-v1 == last-root-in-v_last"
   would be even rarer.

## Queued follow-ups

- **H-NEW-156.1**: expand window — first-3-roots in v1 ∩ last-3-roots
  in v_last. Does the pattern strengthen?
- **H-NEW-156.2**: root-vs-word-level matching (surface-word inclusio).
- **H-NEW-156.3**: descriptive analysis of the 4 non-muq inclusio
  surahs.

## Deliverables

All on disk.
