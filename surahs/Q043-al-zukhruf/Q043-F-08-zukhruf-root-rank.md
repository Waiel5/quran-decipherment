---
finding_id: Q043-F-08
surah: 43
surah_name: al-Zukhruf
file_type: novel-finding
date: 2026-05-10
verdict: NULL_OR_DISCREPANCY (pre-commit honored)
prereg_sha: ed564811745f4261226f7d05bb1acaecb314ec6c4dab0adac099dd2a594c5430
---

# Q043-F-08 — *zukhruf* root corpus rank full inventory


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Verdict

**NULL_OR_DISCREPANCY.** Pre-committed direction was: Q 43 count rank = 1, Q 43 density rank > 1. Observed: Q 43 count rank = **4** (tied last among 4 surahs by alphabetic tiebreak — all 4 have count=1), Q 43 density rank = **1**.

| Prediction | Result |
|:--|:--|
| Total corpus attestations = 4 | **CONFIRMED** (4) |
| Surahs with attestation = 4 | **CONFIRMED** (4) |
| Q 43 count rank = 1 | NULL (count=1 for all 4 surahs; deterministic tiebreak places Q 43 at rank 4) |
| Q 43 density rank > 1 | NULL (Q 43 IS the densest at 1.196 per 1000) |

## Full attestation table

| Surah | Locus | Density per 1000 |
|:--|:--|--:|
| Q 6 al-Anʿām | (6, 112, 12) | 0.327 |
| Q 10 Yūnus | (10, 24, 21) | 0.544 |
| Q 17 al-Isrāʾ | (17, 93, 8) | 0.642 |
| **Q 43 al-Zukhruf** | **(43, 35, 4)** | **1.196** |

## Interpretation

The original pre-reg locked the "surprising direction" (Q 43 NOT densest). The observed result reverses this: Q 43 IS the densest by token-density-per-1000 because Q 43 is the smallest of the 4 attesting surahs by a noticeable margin (836 tokens vs Q 6's 3056). The surface-finding is therefore that the *zukhruf* root, despite being a 4-attestation corpus-rare root, achieves its highest density in the surah named after it — but this is **driven by the denominator** (small surah, single attestation), not by lexical concentration.

The pre-commit is honored: the direction-violation is published as NULL with full prominence. The substantive conclusion is unchanged from Q043-F-04: surah-name-after-root convention is *symbolic* (Q 43 is named for a single verse, not lexical concentration), and the apparent "Q 43 densest" outcome is a denominator artifact.

## Cross-references

- [[Q043-al-zukhruf/Q043-F-04|Q043-F-04]] — earlier pre-reg of the same direction, with corrected interpretation.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — surah-name-after-locus convention.

## Honest limits

- Power is weak (n=4 attestations across the corpus).
- The "rank" metric ties when counts equal; the test's pre-commit was over-specified (count-rank-1 implies a strict winner that doesn't exist).
- Recommended follow-up: re-run as a 4-way count-equality test (which observes count-equal-1 across all 4 surahs and trivially confirms the "symbolic naming" thesis).

## Files

- pre-reg: `preregs/Q043-F-08-zukhruf-root-corpus-rank-prereg.md`
- script: `scripts/Q043_F_08_zukhruf_root_rank.py`
- output: `csv/Q043-F-08.json`
