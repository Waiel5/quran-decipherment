---
id: H-NEW-128
title: Cross-axis distinctive-verse atlas — 13-axis top-100 superverse list + Q 59:22-24 dominance test
phase: B
status: PRE-REGISTERED (locked before any ranks viewed)
date: 2026-04-17
agent: h-new-128-specialist
parent_findings: H-NEW-92 (celebrated-verse single-axis dominance), H-NEW-95 (Khawātim extension Q 59:22-24 rank-1 by 99-name density)
open_question: OQ-8 (cross-axis convergence at specific verses)
bonferroni_k: 4
bonferroni_family: h-new-128-distinctive-verse-atlas
alpha_bon: 0.0125
alpha_family_raw: 0.05
direction_A: "≥1 verse holds rank 1 on ≥3 independent axes simultaneously (perm null p < 0.0125)"
direction_B: "≥20 verses appear in ≥3 top-100-per-axis lists (perm null p < 0.0125)"
direction_C: "descriptive — harmonic-mean-rank superverse top-100 reported"
direction_D: "≥3 of 5 classical celebrated verses {Q 1:1, Q 2:255, Q 24:35, Q 59:22-24, Q 112:1-4} appear in superverse top-100"
seed: 20260417
n_perm: 10000
rules_tuple: (no-tashkeel; whitespace-split tokens; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi abjad not used in this test)
---

# H-NEW-128 — Cross-Axis Distinctive-Verse Atlas (Pre-Registration)

## Motivation

[[h-new-92-light-verse|H-NEW-92]] established that classical "celebrated verses" each dominate a SINGLE axis (Q 24:35 for light, Q 1:1 for divine-name density, Q 2:255 for divine-attribute length, Q 112:1-4 for apophasis compression). [[h-new-95-khawatim-extension|H-NEW-95]] extended this by confirming Q 59:22-24 is the rank-1 3-verse window by 99-name density at p≈10⁻⁴.

OQ-8 asks: **Are there verses that dominate MULTIPLE axes simultaneously?** If so, those would be the empirically-most-distinctive verses in the corpus. This test systematically quantifies that question across 13 pre-committed axes.

## The 13 locked axes (committed before viewing any ranks)

1. **divine_name_density** — count of Allāh + 99-name tokens / verse word count
2. **light_density** — count of tokens from {nwr, DwA, SbH, srj, qbs, nfx, shhb, rmd, Swr, wqd, Dwq, shms, qmr} / verse word count
3. **eschatology_density** — count of tokens matching {yawm, AAxr (ākhirah), qyAm (qiyāmah), jhnm (jahannam), frds (firdaws), Hsb (ḥisāb), jzA (jazāʾ)} / verse word count
4. **book_reference_density** — count of tokens matching {ktb (kitāb), qrA (qurʾān), Ayt (āyāt), nzl (nazala/anzala)} / verse word count
5. **oath_density** — indicator (1/0) for verse-initial "wa-" followed by noun forming an oath (detected via surah-level oath openings from [[h-new-85-oath-openers|H-NEW-85]] oath-items CSV + regex wa- prefix on verse tokens 1)
6. **rare_vocab_density** — count of tokens whose lemma-root appears ≤3× in the whole corpus / verse word count
7. **rhyme_density** — indicator (1/0) for whether the verse's final-word rhyme letter matches its PRECEDING verse's rhyme letter (consecutive-match)
8. **fasila_diversity** — rarity of the verse's terminal rhyme letter within its own surah (1 - frequency_in_surah); higher = rarer/more-diverse
9. **imperative_density** — count of tokens matching {qul (Qul imperative), yA (yā-ayyuha vocative), InA (innā)} + any verse-initial imperative form / verse word count
10. **refrain_closeness** — cosine similarity of verse token bag to the verse's surah's most-repeated verse (refrain detection); if no refrain, distance to mean surah bag
11. **narrative_tense_density** — count of tokens matching {kAn (kāna), qAl (past qāla forms)} / verse word count
12. **short_marker** — indicator (1/0) if verse has <3 tokens
13. **long_marker** — indicator (1/0) if verse has >50 tokens

All 13 axes are positively-oriented (higher score = more distinctive). Ranking is DESCENDING on score; ties broken by verse index (ascending).

## Cells

- **Cell A — Cross-axis rank-1 convergence**: for each axis, identify the rank-1 verse. How many UNIQUE verses hold rank 1 across axes? Does any single verse hold rank 1 on ≥2, ≥3 axes?
- **Cell B — Top-100 intersection atlas**: for each verse, count how many of the 13 top-100-per-axis lists it appears in. Report the distribution. How many verses appear in ≥3, ≥5, ≥8 axis-top-100s?
- **Cell C — Superverse top-100 (harmonic mean rank)**: aggregate rank across axes via harmonic-mean-rank:
  `HMR = K / Σ(1/r_i)` where r_i is the verse's rank on axis i (1-indexed), K = number of axes. Verses ranking outside top-500 on an axis contribute negligibly (assigned rank = 6236). Lower HMR = more distinctive across axes. Top-100 by HMR = "superverse list".
- **Cell D — Classical-celebrated-verse hit rate**: count how many of the 5 benchmark celebrated verses {Q 1:1, Q 2:255, Q 24:35, Q 59:22 (or 23 or 24), Q 112:1 (or 2 or 3 or 4)} appear in the Cell-C superverse top-100. The Q 59:22-24 and Q 112:1-4 clusters count as HIT if ANY verse in them lands in the superverse top-100.

## Null model (for Cells A and B)

Permutation null: for each axis, randomly permute the 6,236 verse scores (preserving per-axis distribution, destroying cross-axis alignment). Re-compute Cell A (max cross-axis rank-1 multiplicity) and Cell B (count of verses in ≥3 top-100s). Repeat 10,000 times with seed 20260417. One-sided p = P(null ≥ observed).

The null preserves each axis's marginal distribution but destroys the cross-axis verse-identity alignment. Under H_0 = "axes are independent", expected Cell A rank-1 multiplicity is concentrated at 1 (each axis has ~1/6236 chance of matching any given other-axis rank-1).

## Bonferroni family

4 tests (A, B, C descriptive, D). α_family = 0.05 ⇒ α_bon = 0.0125 per test.

## Garden-of-forking-paths disclosures

- **The 13 axes are pre-committed**: they derive from [[h-new-92-light-verse|H-NEW-92]]'s 8-axis framework extended with 5 additional axes (rhyme, fasila, imperative, refrain, narrative) to diversify beyond content-density. Further axis additions post-lock are prohibited under PRE-REG-STANDARD-03.
- **Root/lemma operationalization**: for simplicity and reproducibility, root-matching uses consonantal-skeleton substring on the no-tashkeel text (e.g., nūr-family detected via `نور` substring on word). This is approximate and biased toward over-counting (e.g., `نور` would match `منور`). Residual noise is expected; no promotion without cell-C descriptive stability.
- **Harmonic-mean-rank vs sum-of-ranks vs product-of-ranks**: harmonic mean is pre-committed because it rewards verses that are STRONG on some axes and mediocre on others (tolerant of misses), while penalizing any axis where the verse is OUT of top-500. This matches the question "which verses are distinctive on multiple axes simultaneously".
- **Q 59:22-24 / Q 112:1-4 cluster-or-verse matching**: cluster-level hit (any of the verses) is pre-committed for Cell D to avoid arbitrary single-verse cherry-picking.
- **Why not include abjad axis**: abjad is a length-derivative ([[h-new-92-light-verse|H-NEW-92]] noted abjad rank ~ length rank); including it would double-count length effects.
- **Seed 20260417** locked for permutation reproducibility.

## Acceptance windows (pre-committed)

- **A PASS**: p < 0.0125 under perm null AND observed multiplicity ≥3 axes held by a single verse.
- **A FAIL-DIRECTED**: p ≥ 0.0125 OR max multiplicity < 3.
- **B PASS**: p < 0.0125 under perm null AND ≥20 verses in ≥3 top-100s.
- **B FAIL-DIRECTED**: otherwise.
- **C**: descriptive, always reported.
- **D PASS**: ≥3 of 5 celebrated clusters hit superverse top-100.
- **D FAIL-DIRECTED**: ≤2 hit.

## Expected behavior

Under [[h-new-92-light-verse|H-NEW-92]]/95 priors, Q 59:22-24 likely carries divine-name-density + book-reference + eschatology simultaneously (Q 59 is Khawātim-anchor + Medinan prose with heavy theological vocab). If so, it should appear in ≥3 top-100 lists and contribute to Cell A/B PASS. Counter-hypothesis: celebrated verses are single-axis extreme but not cross-axis dominant; the superverse list surfaces SURPRISE candidates from shorter extreme verses (e.g., the oath-openings of short Meccan surahs).

## Outputs

- Script: `scripts/h_new_128_distinctive_verse_atlas.py`
- Data: `findings/phase-b-hypotheses/csv/h-new-128.json` (per-verse 13-axis matrix, per-axis top-100, superverse top-100, Cell A/B/C/D tables)
- Findings: `findings/phase-b-hypotheses/h-new-128-distinctive-verse-atlas.md`
- Journal: `journal/h-new-128-run-1.md`
