---
surah: 2
surah_name: al-Baqara
file_type: novel-finding
test_id: Q002-F-08
date_last_updated: 2026-05-29
phase: B+
verdict: H1 (monopoly) NULL/FALSIFIED — Q4 & Q24 also hold 2 of top-10; H2 (plurality) VINDICATED — Q2 holds the most (3); MW-7 Q2 is unique holder of 3+
prereg_sha: 595773500202c587c8732a118aec2782cfc5704178f77602143d3980ae03ea83
---

# Q002-F-08 — Does al-Baqara MONOPOLISE the corpus's longest verses?


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

## Target claim

Deep-close-read brief T4: is Q 2 the ONLY surah holding 2-or-more of the corpus's
TOP-10 longest verses? This is the concentration/monopoly analogue of the al-sabʿ
al-ṭiwāl long-legal-verse hypothesis (Q002-F-05 locked Q 2:282 as the rank-1 longest
verse; this test asks whether al-Baqara DOMINATES the long-verse tail).

## Pre-registration

`Q002-F-08-longest-verse-monopoly-prereg.md`
(SHA256 `595773500202c587c8732a118aec2782cfc5704178f77602143d3980ae03ea83`).
Direction LOCKED: H1 — Q 2 holds ≥ 2 of the top-10 AND no other surah holds ≥ 2
(strict monopoly). H2 — Q 2 holds the MOST top-10 long verses of any surah (strict
plurality). MW-3: repeat by letter count. MW-7: if H1 fails, test "Q 2 unique holder
of 3+" as a flagged post-hoc refinement.

## Empirical result

From `csv/Q002-F-08.json` (no-tashkeel, sajda-stripped, whitespace words, all 6,236
verses). The corpus top-10 longest verses by word count:

| Rank | Verse | Words | Letters | Content |
|:--|:--|:--|:--|:--|
| 1 | **Q 2:282** | 129 | 551 | debt-contract (āyat al-dayn) |
| 2 | Q 4:12 | 88 | 299 | inheritance shares |
| 3 | Q 24:31 | 78 | 350 | women's modesty |
| 4 | Q 73:20 | 78 | 329 | night-prayer easing |
| 5 | Q 24:61 | 76 | 315 | rules of hospitality |
| 6 | Q 3:154 | 75 | 291 | Uḥud aftermath |
| 7 | **Q 2:102** | 74 | 308 | Hārūt/Mārūt & sorcery |
| 8 | **Q 2:196** | 73 | 290 | ḥajj/ʿumra procedure |
| 9 | Q 4:11 | 71 | 271 | inheritance shares |
| 10 | Q 33:53 | 70 | 294 | Prophet's-household etiquette |

Per-surah count of top-10 long verses (word count):

| Surah | Top-10 long verses | Count |
|:--|:--|:--|
| **Q 2** | 2:282, 2:102, 2:196 | **3** |
| Q 4 | 4:12, 4:11 | 2 |
| Q 24 | 24:31, 24:61 | 2 |
| Q 73 | 73:20 | 1 |
| Q 3 | 3:154 | 1 |
| Q 33 | 33:53 | 1 |

## Verdict

- **H1 (monopoly) — NULL / FALSIFIED (pre-commit honoured).** Q 2 is NOT the only
  surah holding ≥ 2 of the top-10: **Q 4 holds 2** (4:11, 4:12, both inheritance) and
  **Q 24 holds 2** (24:31, 24:61). The strict monopoly hypothesis is falsified and
  published with full prominence as a pre-committed NULL.

- **H2 (plurality) — VINDICATED.** Q 2 holds **3** of the top-10 — strictly more than
  any other surah (next is 2). Q 2 is the unambiguous plurality-holder of the corpus's
  longest verses.

- **MW-7 refinement (flagged α = 0.05 single-test):** Q 2 is the **UNIQUE holder of
  3-or-more** of the top-10. No other surah reaches 3. This is the honest refined form
  of the monopoly intuition — al-Baqara monopolises the *extreme* tail (3+), it does not
  monopolise the merely-very-long tail (2+).

## MW-3 rules-tuple stability (letter count)

Re-running with the top-10 defined by LETTER count rather than word count:

| Surah | Top-10 long verses (by letters) | Count |
|:--|:--|:--|
| **Q 2** | (4 verses) | **4** |
| Q 24 | 2 | 2 |
| Q 73, Q 4, Q 33, Q 3 | 1 each | 1 |

Under letter count Q 2 holds **4** of the top-10 (even more dominant), Q 24 holds 2,
and Q 4 drops to 1. **H1 (monopoly) is NULL under both metrics** (Q 24 still holds 2);
**H2 (plurality) is VINDICATED and strengthens** under letter count (Q 2's lead widens
from 3-vs-2 to 4-vs-2). The plurality verdict is rules-tuple-stable; the monopoly NULL
is rules-tuple-stable.

## N-sweep robustness (MW-2 surrogate)

The deterministic count is stable across thresholds: at top-10/15/20 by word count,
Q 2's argmax-plurality holds throughout (Q 2 leads at every N). See `csv/Q002-F-08.json`
keys `words_top15`, `words_top20`.

## Interpretation

al-Baqara does NOT monopolise the corpus's long-verse tail — long legal/procedural
verses are a Medinan-wide phenomenon (Q 4 inheritance, Q 24 social law, Q 33 household
law all contribute). What Q 2 monopolises is the **most extreme** tail: it is the only
surah with 3+ of the absolute longest verses, anchored by the 4.33σ-isolated debt-verse
2:282 (Q002-F-05). This refines the al-sabʿ al-ṭiwāl picture: the "Seven Long" share
the long-verse register, but al-Baqara holds the apex of it. The honest headline is
**plurality + extreme-tail-uniqueness, NOT monopoly**.

## Honest limits

- Word/letter counts are tokenisation-dependent (whitespace split + sajda strip). The
  rank-1 verse (2:282) is robust; the rank-9/10 boundary is sensitive to ±1-word
  tokenisation choices (e.g. Q 33:53 at rank 10 with 70 words could swap with the next
  verse under clitic-splitting). The 2+/3+ verdicts are robust to this because the
  Q 2 / Q 4 / Q 24 holdings are well-separated from the boundary.
- "Top-10" is an arbitrary cut; the N-sweep (10/15/20) confirms the plurality is not a
  cut-point artefact.

## Cross-references

- [[Q002-F-05-q2-282-length|Q002-F-05]] — Q 2:282 rank-1, z=+12.31, gap 4.33σ.
- [[h-new-770-verse-length-compression-tail]] — verse-length compression law (Medinan
  long-verse regime).
- [[h-new-660-compression-tail-gradient]] — content compression gradient.

## Status

H1 (monopoly) NULL/FALSIFIED — pre-commit honoured. H2 (plurality) VINDICATED,
rules-tuple-stable across word + letter counts. MW-7: Q 2 unique holder of 3+ (flagged).
