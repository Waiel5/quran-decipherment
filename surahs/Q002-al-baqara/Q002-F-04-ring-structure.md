---
surah: 2
surah_name: al-Baqara
file_type: novel-finding
test_id: Q002-F-04
date_last_updated: 2026-04-28
phase: B+
verdict: NULL — verse-token-level chiastic mirroring is NOT empirically present
prereg_sha: 3eca733aa682e9e2e114fb8a62e464b3797b00ca099eb0baacb202644ef44127
---

# Q002-F-04 — Q 2 ring-structure detection (verse-token level)

## Target claim

Farrin 2010 (*Surat al-Baqara: A Structural Analysis*) and Cuypers 2015 (*The Composition of the Quran*) — Q 2 has nine-section ring composition with verse 143 (qibla-change, "Muslims as a middle nation") as the central pivot; symmetric-pair verses share themes (1 ↔ 286, 2 ↔ 285, ...).

## Pre-registration

`Q002-F-04-ring-structure-prereg.md` (SHA256 3eca733aa682e9e2e114fb8a62e464b3797b00ca099eb0baacb202644ef44127). Direction-LOCKED: ring_score_canonical > 95th percentile of 10,000 verse-shuffle nulls.

## Empirical result

From `csv/Q002-F-04.json`:

### Verse-pair test (143 symmetric pairs)

| Statistic | Value |
|:--|:--|
| ring_score canonical | 0.0789 |
| Null mean (10,000 shuffles, seed 20260428) | 0.0830 |
| Null SD | 0.00277 |
| z-score | **−1.45** |
| One-sided p (canonical > null) | **0.9301** |

**The canonical order has LOWER ring-score than ~93% of random shuffles.** This is not just NULL — it is mildly ANTI-ring (z = −1.45, but not significantly so).

### Block-pair test (Farrin 9-block, 4 symmetric pairs)

| Statistic | Value |
|:--|:--|
| ring_score canonical | 0.5286 |
| One-sided p (out of 10,000 perms) | **0.6079** |

NULL also at the coarser block level.

### MW-6 control: Q 3 Āl ʿImrān

| Statistic | Value |
|:--|:--|
| Q 3 ring_score canonical | 0.0827 |
| Q 3 one-sided p | **0.8288** |

Q 3 also returns NULL — confirming the *metric* is sound (it returns NULL when ring-structure is not expected) but no empirical signal exists for verse-token-level chiastic mirroring in either Q 2 or Q 3.

## Verdict — NULL

The classical Farrin/Cuypers ring-structure claim does NOT have an empirical correlate at the **verse-token level** OR the **block-token level**. Pre-commit honoured.

## Honest interpretation

This NULL does NOT falsify Farrin's or Cuypers's thematic-ring claim. The reasons:

1. **Their claim is THEMATIC, not LEXICAL.** "Faith vs. unbelief" (their proposed sections 1 ↔ 9) does not require shared vocabulary. The two themes can be mirror-images at the meaning-level while having entirely different word-tokens.

2. **Token-set cosine ignores syntactic + semantic structure.** Two passages that thematically mirror each other (e.g. "those who believe..." vs "those who disbelieve...") will have OPPOSITE vocabulary, dragging cosine DOWN, not up.

3. **The 9-block boundaries we used are an approximation** of Farrin's analytical sections; small differences in boundaries could swing the test.

The truly fair test of Farrin's claim requires:
- Hand-coded thematic similarity matrix (not lexical).
- Or LLM-derived semantic embeddings (which would import a non-Arabic model bias).
- Or a syntactic-pattern detector (e.g. iltifāt-mirroring per Abdel Haleem 1992).

These are out-of-scope for the present empirical pipeline. We thus mark this NULL as **resolution-limited** — Farrin/Cuypers's THEMATIC ring claim survives, but the LEXICAL reduction of it is empirically NULL.

## What we DID find (block-level cohesion structure)

Per `Q002_C_audit_helpers.py` output, the 8-block scheme from §00-overview shows:

| Block | Verses | Internal-cohesion (mean cos) | Mean cos to other blocks |
|:--|:--|:--|:--|
| A | 1-39 | 0.0679 | 0.2308 |
| B | 40-103 | 0.0951 | 0.2300 |
| C | 104-141 | 0.0892 | 0.2492 |
| D | 142-176 | 0.0963 | 0.2335 |
| E | 177-242 | **0.1120** (highest) | 0.2040 |
| F | 243-260 | 0.1094 | 0.2185 |
| G | 261-283 | 0.1117 | 0.2033 |
| H | 284-286 | 0.0883 | **0.1720** (lowest) |

- **Block E (legal core, vv. 177-242)** has the highest internal cohesion — the legal verses cluster tightly in their own vocabulary.
- **Block H (khawātim, vv. 284-286)** is most distant from the rest — confirming the "summary / closure" character noted in the hadith tradition.
- **Block A (opening, vv. 1-39)** is internally most heterogeneous — opening creedal-narrative deliberately spans multiple registers.

## Cross-references

- [[h-new-111-fisher-rao-mushaf]] — root-level distance.
- [[Q002-al-baqara/02-content-analysis]] — block thematic content.
- Farrin 2010 PDF: `data/literature/farrin-cuypers/2010-farrin-surat-al-baqara-structural-analysis.pdf`.
- Cuypers 2015 PDF: `data/literature/farrin-cuypers/2015-cuypers-composition-of-the-quran-rhetorical-analysis.pdf`.

## Status

NULL on verse-token AND block-token chiastic mirroring. Resolution-limited (thematic claim NOT falsified). Pre-commit honoured.
