---
hypothesis_id: H-NEW-93
title: "Q 29 al-ʿAnkabūt + Q 30 al-Rūm TEST-AND-PROPHECY muqaṭṭāʿat sub-pattern"
run_date: 2026-04-17
author: h-new-93-specialist
status: LARGELY-NULL (with 1 narrow single-test WEAK-PASS-DIRECTED on ghalaba+naṣr)
data_variant: no-tashkeel
rules_tuple: (hafs-kūfan; no-tashkeel; QAC v0.4 STEM-ROOT tokens)
seed: 20260417
perms: 10000
bonferroni_k: 4
alpha_bon: 0.0125
alpha_single_cap: 0.05
verdict_ceiling: PASS-DIRECTED
independent_replication: NOT ATTEMPTED (not warranted — finding is largely NULL)
composite_verdict: NULL-full-target-pattern-rejected
---

# [[h-new-93-q29-q30-subpattern|H-NEW-93]] — RESULT: Q 29 + Q 30 do NOT form a coherent TEST-AND-PROPHECY sub-pattern

## TL;DR

The pre-registered 4-cell test of whether Q 29 al-ʿAnkabūt + Q 30 al-Rūm form a coherent TEST-AND-PROPHECY sub-class of muqaṭṭāʿat surahs (distinct from the dominant "book-introduction" function of the other 27) **FAILS** at the primary hypothesis level:

- **Cell (a) TEST-of-believers density**: **NULL** (p = 0.9353 two-sided; Q29+30 density actually *lower* than Meccan baseline — 4.14‰ vs 5.05‰)
- **Cell (b) HISTORICAL-PROPHECY density (4-root full)**: **NULL** at α=0.05 (p = 0.2900 two-sided; Q29+30 visibly *higher* at 51.5‰ vs 29.3‰, but n=2 drives high variance)
- **Cell (c) Allah-density control**: **CONTROL-CONFIRMED** (p = 0.0638; no significant difference)
- **Cell (d) Eschatological density control**: **CONTROL-CONFIRMED** (p = 0.9338; no difference)
- **MW-5 positive-control**: all pass — other-الم surahs (Q 2, 3, 31, 32) are NOT elevated on test/prophecy markers

**Composite verdict**: `NULL-full-target-pattern-rejected`.

One narrow secondary result survives single-test α=0.05 but NOT Bonferroni-4: restricted-cell-(b) with only **glb + nSr** roots (ghalaba + naṣr) gives p=0.0362 two-sided (target 9.82‰ vs Meccan 1.84‰). This is a WEAK-PASS-DIRECTED at single-test-cap only.

## Honest publication with equal prominence

Per discipline file §honesty-over-cheerleading: this NULL is published with SAME prominence as PASS findings. The EYEBALL impression that Q 29 + Q 30 share a "test-and-prophecy" theme is NOT supported by pre-committed root-density testing at the Bonferroni-corrected level.

## Full results table

### Primary 4 cells (Bonferroni-4, α_bon = 0.0125; single-test α = 0.05)

| Cell | Roots | Target (Q29+30) ‰ | Meccan non-muq ‰ | p two-sided | Direction | Verdict |
|------|-------|-------------------|------------------|-------------|-----------|---------|
| (a) TEST | ftn, blw, mHn, Sbr | 4.14 | 5.05 | 0.9353 | REVERSE | NULL |
| (b) HIST-PROPHECY full | glb, nSr, kwn(past), ywm | 51.54 | 29.30 | 0.2900 | higher | NULL |
| (c) Allah control | Alh | 57.82 | 22.68 | 0.0638 | higher | CONTROL-CONFIRMED |
| (d) Eschato control | Axr, bEv, Hsb, jzy | 10.32 | 11.39 | 0.9338 | ≈ equal | CONTROL-CONFIRMED |

### Secondary (not Bonferroni-family; exploratory robustness)

| Cell | Roots | Target ‰ | Meccan ‰ | p two-sided | Verdict |
|------|-------|----------|----------|-------------|---------|
| (b-narrow) glb only | glb | 2.84 | 0.38 | 0.0672 | NULL (near single-test) |
| (b-narrow) glb + nSr | glb, nSr | 9.82 | 1.84 | 0.0362 | **WEAK-PASS-DIRECTED-single-test-only** |

### Target vs other-الم group (Q 2, 3, 31, 32) comparisons

None reach α=0.05 two-sided:

| Cell | Target ‰ | Other-الم ‰ | p two-sided |
|------|----------|-------------|-------------|
| (a) TEST | 4.14 | 4.89 | 0.6680 |
| (b) HIST full | 51.54 | 38.00 | 0.4577 |
| (c) Allah | 57.82 | 66.02 | 0.8685 |
| (d) Eschato | 10.32 | 9.69 | 0.9323 |
| (b) glb + nSr | 9.82 | 3.14 | 0.2069 |

### MW-5 positive-control (other-الم vs Meccan non-muq)

All PASS (other-الم group is NOT elevated on test/prophecy markers vs Meccan baseline, confirming the test has specificity):

| Cell | Other-الم ‰ | Meccan ‰ | p two-sided | MW-5 pass? |
|------|-------------|----------|-------------|-----------|
| (a) TEST | 4.89 | 5.05 | 0.9765 | YES |
| (b) HIST full | 38.00 | 29.30 | 0.5711 | YES |
| (d) Eschato | 9.69 | 11.39 | 0.8203 | YES |

(Cell (c) Allah: MW-5 p = 0.0335 — other-الم is significantly Allah-denser than Meccan non-muq baseline; explained by the fact that Q 2 and Q 3 are technically MEDINAN surahs yet included in "other-الم" comparison. This MW-5 warning does NOT invalidate cells (a), (b), (d).)

## Detailed per-surah breakdown

```
Surah    | (a) TEST ‰ | (b) HIST full ‰ | glb only ‰ | glb+nSr ‰ | (c) Allah ‰ | (d) Eschato ‰
Q29 ʿAnk |   6.38     |    46.25        |   0.00     |   6.38    |   70.18     |   11.16
Q30 Rūm  |   1.89     |    56.82        |   5.68     |  13.26    |   45.45     |    9.47
--- other-الم ---
Q2  Baq  |   4.38     |    31.15        |   0.26     |   4.63    |   74.41     |    9.53
Q3  ʿIm  |   5.28     |    39.14        |   0.88     |   7.92    |   94.55     |   13.63
Q31 Luq  |   5.68     |    14.20        |   0.00     |   0.00    |   90.91     |   11.36
Q32 Saj  |   4.22     |    67.51        |   0.00     |   0.00    |    4.22     |    4.22
```

**Key observation**: Q 32 al-Sajda has the HIGHEST historical-prophecy-full density (67.5‰) in the entire 6-surah الم cluster, driven by `kwn` copula tokens. This complicates the "Q 29+30 are unique" narrative.

## What the data DOES support (secondary, exploratory)

The narrow signal on `glb + nSr` (ghalaba + naṣr) is the ONE cell where Q 29+30 show a noticeable single-test effect (9.82‰ vs Meccan 1.84‰, p=0.0362). This is driven almost entirely by:

- **Q 30:2-3** "ghulibat al-Rūm ... wa-hum min baʿdi ghalabihim sa-yaghlibūn" (the Romans-defeat-then-victory prophecy). 3 glb tokens in Q 30 alone account for most of the lift.
- **Q 29** uses the lexical-family sparingly (0 glb tokens; 4 nSr tokens).

So the apparent "historical-prophecy signal" REDUCES to Q 30's unique Roman-prophecy pericope plus generic naṣara-root usage — NOT a structural pattern across both surahs.

**The Q 29 TEST theme** (opening with "a-ḥasiba al-nās ... lā yuftanūn") appears in verse 2-3 but does NOT produce above-baseline density across the whole surah: the ftn root occurs only 4 times in Q 29 (rate 6.4‰, below Meccan mean 5.0‰ for test-family).

## Conclusion

The eyeball hypothesis that Q 29 + Q 30 form a distinct "test-and-prophecy" sub-class of الم muqaṭṭāʿat surahs is **NOT supported** by pre-registered root-density testing. The thematic headline of each surah (testing for Q 29; Roman prophecy for Q 30) does NOT translate into corpus-wide elevated root densities relative to Meccan non-muqaṭṭāʿat baseline.

### Revised interpretation

Cross-finding-008 already notes that Q 29 and Q 30 are the 2 genuine exceptions to the book-reference pattern. [[h-new-93-q29-q30-subpattern|H-NEW-93]] shows that their OPENING thematic distinctiveness (clearly visible in v1-3) does NOT propagate into a surah-wide lexical signature that distinguishes them from ordinary Meccan surahs. Possible explanations:

1. **Surface-thematic uniqueness without depth-lexical signature**: the testing/Roman-prophecy themes are concentrated in each surah's opening pericope but the rest of the surah returns to generic Meccan content. This is plausible given that most surahs of this length (~60-85 verses) are thematically multi-focal.

2. **Narrow-window signal, not surah-level signal**: a restricted v1-3 or v1-10 test MIGHT show the pattern. This would require a NEW pre-reg (H-NEW-93.1).

3. **True null — the eyeball pattern is noise**: Q 29 and Q 30 are simply two surahs with topically distinctive openings that do not constitute a second "functional sub-class" of muqaṭṭāʿat.

The Occam-preferred reading under honest-discipline is **(3) true NULL**. Cross-finding-008 stands with 27/29 as a single-sub-class finding; the residual 2 remain "ordinary-Meccan-like surahs that happen to open with distinctive themes".

## Linkage to open questions

- **OQ-3 (Q 29 + Q 30 sub-pattern)**: moved from OPEN to **ANSWERED NULL** at the pre-committed operationalization. A narrow-window follow-up (H-NEW-93.1) is queued but not yet warranted.
- **Cross-finding-008 architecture**: NO CHANGE. The 27/29 book-introducer pattern remains as the dominant functional signature; the 2 exceptions are NOT a coherent second sub-class at the surah-level-density axis.

## Queued follow-ups (not executed)

- **H-NEW-93.1**: narrow-window (v1-3 or v1-5) test-and-prophecy density using surface strings (not roots) — different operationalization. LOW PRIORITY given primary NULL.
- **H-NEW-93.2**: cross-listed "test of believers" and "historical victory" verse-catalogue — are there OTHER surahs whose v1-3 hit the test/prophecy theme? If so, is there a scattered sub-cluster invisible to the Q 29/30-only test?

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-93-q29-q30-subpattern-prereg.md`
- Script: `scripts/h_new_93_q29_q30_subpattern.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-93.json`
- Journal: `journal/h-new-93-run-1.md`
