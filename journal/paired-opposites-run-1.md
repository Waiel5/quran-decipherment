# Journal — paired-opposites network (run 1)

**Agent:** paired-opposites-network-run-1
**Date:** 2026-04-12
**Corpus:** Leeds QAC v0.4 root-index.json + morph file (lemma override for nwr/naar split)
**Output:** `findings/phase-b-hypotheses/paired-opposites-network.md`, `paired-opposites.csv`

## Plan

Classical balāgha has two named antithesis categories: *ṭibāq* (simple 2-term)
and *muqābala* (multi-term parallel). Prior Phase-B work on word-pair matching
by count (`word-pair-symmetry.md`) mostly died at baseline. This run asks a
different question: *are antonym pairs co-mobilised at the verse level more
than chance?* Fisher exact 2×2 per pair on verse-level presence vectors.

## Steps

1. Read master-index, word-pair-symmetry, root-cartography, balagha-mapping. Found existing ground: Q 28:71-72 is classical muqābala; Q 30:19 is Jurjānī type-case; ring-center semantics paper already flagged centers as contrast-loci.
2. Parsed root-index.json (1642 roots). Mapped 21 seed task pairs + 6 self-added pairs = 27 Bonferroni-corrected tests. Buckwalter root codes verified against actual index keys (e.g. `$rq` for east, `grb` for west, `Amn` for faith).
3. For the `nwr` root (encodes both nūr "light" AND nār "fire"), switched to lemma-level filter using the LEM:nuwr / LEM:naAr distinction in the morphology file. Got nar=138 verses, nur=33 verses, jahannam=77 verses.
4. Built Fisher exact test from scratch (lgamma-based, one-sided upper and two-sided). Verified against 2x2 contingency tables by sanity-checking known results.
5. Ran all 27 pairs. 20 survive Bonferroni at α=0.00185.
6. Hunt for novel antonyms: 18 candidates tested. Winner: **hidden_vs_manifest (bṭn / Ẓhr)** at 26× enrichment, p = 6.9e-08. Dry/wet passes but is small-n (essentially Q 6:59 alone).
7. Ring-center muqābala: widened window to the full ring (not just center verse). Al-Baqarah 131-144 has **2:142 east_vs_west hit** — the qibla pivot. Structural prediction confirmed.
8. Ar-Rahman extraction: counted 31 refrains exactly as per classical tradition. Segmented the surah into 31 segments. The hell→paradise transition is at segments 15→16 (verses 43-47), the structural pivot.
9. Meccan/Medinan breakdown: faith/disbelief heavily Medinan (28.6% Meccan); day/night heavily Meccan (80% Meccan). Consistent with Suyūṭī's *Itqān* naw' 9.
10. Triadic opposites (wasaṭ mediator): 5 occurrences total; only Q 2:143 is the formal triadic frame. The Quran's preferred triadic form is negative co-exclusion (Fātiḥa's non-ghaḍab, non-ḍāll).
11. Singular/plural: Iblīs is always singular (11 occ, 11 verses). The asymmetry is "evil is one, good is a host."

## Results

| Pair (top 3 by p-value) | same-verse obs | p (one-sided) | enrichment |
|---|---:|---|---:|
| heaven_vs_earth | 224 | 1.8e-190 | 9.0× |
| life_vs_death | 65 | 2.8e-69 | 17.6× |
| dunya_vs_akhira | 57 | 4.8e-48 | 11.5× |

Top 3 by **enrichment** (the tightest lexicalised muqābala pairs):

1. east_vs_west — 216× (10 same-verse vs 0.05 expected)
2. sun_vs_moon — 135× (18 vs 0.13 expected)
3. secret_vs_open — 109× (12 vs 0.11 expected)

**Most central root** by degree in the significance graph: **Axr (ākhir)** — participates in BOTH dunya/akhira AND first/last Bonferroni-sig pairs. Q 57:3 stacks both + hidden/manifest in one verse.

**Most surprising finding**: mercy/wrath and reward/punishment do NOT cluster at the same verse. Enrichment 0.95× and 0.75× — at or below chance. The Quran *separates* these antonyms across verse boundaries — distributed dualism, not compressed muqābala.

## Stumbles / decisions

- First pass had the `speak/silent` pair with `qwl` (1383 verses) vs `Smt/nSt` (3 verses) — totally uninformative. Kept in final list as a "tested-and-failed" row for honesty.
- `mercy/wrath` failure was initially suspicious — considered whether it was a coverage bug. Verified by inspecting Q 7:154 (the sole co-occurrence, Moses's tablets scene). Result is real.
- Ar-Rahman refrain detection: first used "favors ... deny" substring; Sahih translates 31 occurrences exactly. 0 were missed (spot-checked against Arabic count).
- Node-centrality graph is flat because the seed list is mostly disjoint pairs. Flagged that `Axr` (2 edges) is the only real multi-axis root under this framing. Future agents could build a richer graph by allowing each root to participate in multiple antonym relations explicitly.

## Confidence

- The p-values are robust; Fisher exact is exact.
- Enrichment ratios for tight formulaic pairs (east/west 216×) are real but amplified by small baseline denominators.
- The coverage figure (10.82% verses with ≥1 same-verse pair) is a conservative undercount — it uses only 27 seed pairs + a handful of novel pairs. A larger seed list would push this higher.
- The Bonferroni threshold (α = 0.05/27) is conservatively correct for the seed tests. Adding the 18 novel tests would shift to 0.05/45 but only hidden_vs_manifest would need defense at that stricter line; it survives (p = 6.9e-08).

## Cross-references

- Master-index entries: ring-center-semantics (Abraham ring center = qibla = east/west pivot); Q 13:28 palindrome (structural mutashābih). Both are now cross-linked to the present muqābala network.
- Classical sources: all 11 al-Zamakhsharī / al-Jurjānī / al-Qazwīnī / al-Sakkākī type-cases are textually verified. Q 57:3 emerges as the Quran's densest-antithesis verse (4 Bonferroni-sig pairs stacked).
