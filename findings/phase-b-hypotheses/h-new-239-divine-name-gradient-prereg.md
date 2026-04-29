---
finding_id: h-new-239-divine-name-gradient
phase: B
status: pre-registered
date: 2026-04-17
agent: phase-b-specialist
parent_anchor: MASTER-FINDINGS-LEDGER §2 (divine-names authoritative catalog)
seed: 20260419
bonferroni_k: 4
alpha_bon: 0.0125
verdict: PENDING
rules_tuple:
  orthography: no-tashkeel
  name_list: 99 canonical al-Tirmidhi names (al-Walid b. Muslim list, per MASTER-LEDGER §2)
  name_identification: definite-singular Quranic attestation per divine-names-distribution methodology
  word_definition: whitespace-split tokens of no-tashkeel surah text
  verse_numbering: hafs-kufan (6236 verses)
  data_source_names: findings/phase-b-hypotheses/divine-names-by-verse.csv (per-verse canonical name annotations)
  data_source_text: quran-text/quran-no-tashkeel.json
  data_source_chronology: data/revelation-order.csv
direction: |
  - Cell A (Spearman mushaf-position vs per-surah name-density): NOT pre-committed (descriptive).
    Sign of rho reported with magnitude and two-sided permutation p.
  - Cell B (Kruskal-Wallis across ṭiwāl/ḥawāmīm/mufaṣṣal/other blocks): DIRECTIONAL hypothesis —
    ḥawāmīm (Q 40-46, the H-family) expected to be name-heavy; Q 59 Khawātim al-Ḥashr
    within mufaṣṣal expected to pull mufaṣṣal mean up. Post-hoc Dunn pairwise reported.
  - Cell C (Juzʾ 30 mean density vs Juzʾ 1-29 mean density): DIRECTIONAL —
    Juzʾ 30's 37 short surahs contain many full-basmala and short-formula refrains
    → Juzʾ 30 expected HIGHER per-word density.
  - Cell D (Medinan vs Meccan): DIRECTIONAL — Medinan legal-heavier,
    Meccan theological-heavier → Meccan expected higher name-density on per-word basis
    (confirmatory of divine-names-distribution §1 observation #4 inverted for density-per-word).
cells:
  A: spearman_pos_density
  B: kw_block_means
  C: juz30_vs_rest
  D: meccan_vs_medinan
bonferroni:
  k: 4
  alpha_family: 0.05
  alpha_per_cell: 0.0125
negative_controls:
  MW-5: shuffled name-assignments (permute divine-name tokens across verses preserving per-verse counts)
        → all four cells expected to go to null; confirm gradient destruction.
honest_limits: |
  - Morphological definition of "name" is the same as divine-names-distribution (DET-MS,
    ambiguous-name context window). Sensitivity analysis under permissive filter deferred.
  - al-Malik and al-Mulk share roots; some names bleed. Flagged per the parent agent.
  - Mushaf position is not chronological position — Cell A is about BOOK-ORDER, not revelation-order.
    A future sibling test could redo Cell A using Noldeke chronological order.
  - Per-surah word count = whitespace-split tokens of the no-tashkeel text; this slightly
    differs from the morphology-word counts used in divine-names-distribution §5. Both are
    defensible; locking to whitespace here for reproducibility.
garden_of_forking_paths: |
  - Block boundaries locked BEFORE run: ṭiwāl = Q 2-9 (the Seven Long plus Q 8-9 per classical
    convention: Q 2, 3, 4, 5, 6, 7, 8, 9); ḥawāmīm = Q 40-46; mufaṣṣal = Q 50-114;
    "other" = Q 1 + Q 10-39 + Q 47-49. Choice follows Zarkashī *al-Burhān* conventional division.
    Q 1 (al-Fatiha) classed as "other" despite being opening; sensitivity check moves it to mufaṣṣal.
  - Cell C juz' 30 definition: Q 78:1 start through Q 114 end.
  - Density metric: (tokens-of-99-canonical-names-in-surah) / (whitespace-words-in-surah).
    Alternative (names per verse) reported as secondary; primary test uses per-word.
  - Diversity metric: count of DISTINCT canonical names occurring in surah.
    Reported as secondary; Cell A/B primary tests use density.
  - Cell A spearman p: 10000-permutation two-sided test.
  - Cell B Kruskal-Wallis from scipy; Dunn post-hoc with Bonferroni within-cell.
  - Cells C, D: Mann-Whitney U, two-sided.
expected_outcomes:
  A: sign unclear; prior expectation slight NEGATIVE (density higher at book-end = Juzʾ 30 pull)
  B: ḥawāmīm and mufaṣṣal means > ṭiwāl and other
  C: juz30 > rest (per-word density), strong
  D: meccan > medinan (per-word density), moderate
classical_anchor: al-Ghazali *al-Maqsad al-Asna* three-family (jalāl/jamāl/kamāl) theological decomposition.
  H-NEW-170 validated this partition. H-NEW-239 extends to mushaf-position gradient.
cross_refs:
  - MASTER-FINDINGS-LEDGER §2 divine-names canonical data
  - findings/phase-b-hypotheses/divine-names-distribution.md (parent catalog)
  - findings/khawatim-al-hashr-analysis.md (Q 59:22-24 peak)
  - findings/cross-finding/cross-finding-018-four-principle-reduced-model.md (M1 block structure)
  - findings/phase-b-hypotheses/h-new-203-prereg.md (juz' partition prior art)
---

# [[h-new-239-divine-name-gradient|H-NEW-239]] — Divine-name density gradient across the 114-surah mushaf

## Question

Does the density and diversity of the 99 canonical divine names systematically
change with mushaf position? In particular, do block-level concentrations
(ṭiwāl / ḥawāmīm / mufaṣṣal) or the Juzʾ-30 tail show detectable peaks?

## Background

Project has previously established:

- 99 canonical names catalog anchored in MASTER-LEDGER §2.
- 8 names exclusive to Khawātim al-Ḥashr (Q 59:22-24).
- Q 59:23 = rank #1 verse-level density (50%), and the Ism al-Aʿẓam composite
  ranks Q 59:22-24 in its top 3.
- Medinan short-surah density peaks (65 at-Ṭalāq, 60 al-Mumtaḥana, 59 al-Ḥashr)
  per divine-names-distribution §5.

No prior test directly measures the per-surah density gradient across all 114
positions with the block-partition null. [[h-new-239-divine-name-gradient|H-NEW-239]] fills this gap.

## Pre-registered tests

4 cells, Bonferroni k=4, α_family = 0.05 → α_per_cell = 0.0125.

| Cell | Test | Metric | Direction |
|---|---|---|---|
| A | Spearman(mushaf_position, name_density) | ρ, permutation two-sided p | mixed |
| B | Kruskal-Wallis across {ṭiwāl, ḥawāmīm, mufaṣṣal, other} | H, p | directional (ḥawāmīm peak) |
| C | MW-U juz'30 vs juz'1-29 per-surah density | U, p | directional (juz'30 higher) |
| D | MW-U Meccan vs Medinan per-surah density | U, p | directional (Meccan higher) |

## Negative control

MW-5: permute divine-name token assignments across the 6,236 verses while
preserving per-verse count. Re-aggregate to per-surah density. Rerun all 4
cells on shuffled assignment. Expected: all cells null. Confirms that the
signal (if any) is due to the actual textual placement, not count totals.

## Deliverables

- `scripts/h_new_239_divine_name_gradient.py`
- `findings/phase-b-hypotheses/csv/h-new-239.json` (per-surah table + cell results)
- `findings/phase-b-hypotheses/h-new-239-divine-name-gradient.md`
- MASTER-LEDGER Wave-4 2026-04-17 entry
- `journal/h-new-239-run-1.md`
