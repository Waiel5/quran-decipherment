---
id: H-NEW-71
title: Comprehensive distribution analysis of the word "Allah" (الله) across the Quranic corpus — position-in-verse, position-in-surah, density, chronology
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (locked BEFORE running any inferential analysis; allowed pilot to verify counting rule produces ~2700 tokens consistent with project memory)
phase: B
agent: h-new-71-specialist
parent_lineage: extends H-NEW-59 (which counted Allah=2538 under the 99-names substring rule); H-NEW-71 isolates Allah ALONE and analyzes positional distribution in depth
bonferroni_family: 2026-04-15-Wave-H-NEW-71-Allah-Distribution
bonferroni_k: 7
alpha_bon: 0.05 / 7 ≈ 0.007143
rules_tuple: (no-tashkeel; word-token match of {الله, لله, اللهم, آلله} + locked proclitic-prefix set; hafs-kufan; canonical-114; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)
seed: 20260417
primary_data: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
chronology_data: /Users/grey/Downloads/quran/data/revelation-order.csv
---

# [[h-new-71-allah-distribution|H-NEW-71]] — Comprehensive Distribution Analysis of "Allah" (الله)

## Questions

1. **Total count.** How many tokens of the divine name "Allah" appear in the corpus? (project memory says ~2700; H-NEW-59 substring-conflated count is 2538.)
2. **Per-surah density.** Which surahs have the highest/lowest density of "Allah" (per word, per verse)?
3. **Surahs WITHOUT Allah.** Are there any surahs with ZERO occurrences of "Allah"? Which?
4. **Verse-position structure.** Does "Allah" occur preferentially at certain word-positions within verses (start vs middle vs end vs penult — i.e., fāṣila-adjacent)?
5. **Surah-position structure.** Within each surah, does "Allah" cluster in opening, middle, or closing verses?
6. **Density crown verses.** Which verses have the highest "Allah"-tokens per word?
7. **Cross with chronology.** Does Allah-density vary monotonically across Nöldeke phases (Early/Middle/Late Meccan vs Medinan)?

## Garden-of-forking-paths disclosure (BEFORE running)

Pre-existing knowledge:

- H-NEW-59 already counted Allah at 2538 tokens / 1730 verses / 84 surahs under the 99-name substring rule (which deliberately undercounts by not handling all proclitic prefixes uniformly).
- Project memory ("estimated ~2700 occurrences") aligns with the more inclusive form-set used here; pilot run confirms n=2704 under the locked rule below.
- 84 surahs (per H-NEW-59) means **30 surahs have no الله in the H-NEW-59 substring sense**. The novel question for Cell 6 is whether the more permissive form-set still leaves any surahs at zero, and which.
- It is widely known anecdotally that several short Mufaṣṣal surahs (e.g., al-Fīl, al-Quraysh, al-Kāfirūn, al-Aṣr) do not contain "Allāh" by name. The pre-registered Cell 6 test is whether the SET of zero-Allah surahs is non-trivially structured (e.g., concentrated in a chronological window, or correlated with surah-length).
- "Allah" appearing as a final fāṣila word is a known phenomenon (e.g., Q 2:284 ends *... wa-llāhu ʿalā kulli shayʾin qadīr*). The pre-registered Cell 4 tests whether Allah is over- or under-represented at verse-final position vs interior.
- Q 1 (al-Fātiḥa), under the no-tashkeel basmala-as-v1 convention, includes "الله" in v1 (basmala) and "لله" in v2; this is a known seed verse.
- Q 24 (al-Nūr) v35 (the Light Verse) and Q 2 (al-Baqara) v255 (Āyat al-Kursī) and Q 59:22-24 (Khawātim al-Ḥashr) are all known high-Allah-density passages that will likely surface in Cell 5.

These known facts DO NOT bias inferential cells because:
- All test statistics are mechanically defined from the locked counting rule.
- Bonferroni-corrected α is set BEFORE seeing per-cell results.
- MW-5 positive controls (Cell 1, the "Q1 must contain ≥1 Allah-token" check) protect the extractor.

## Locked counting rule (binding, frozen here)

A word-token `w` (from a whitespace-split verse, with no tashkeel) **counts as an Allah-token** if and only if:

1. `w == 'الله'` (bare), OR
2. `w == 'لله'` (preposition lām + Allah, with alif elision), OR
3. `w == 'اللهم'` (vocative form, n=5), OR
4. `w == 'آلله'` (interrogative-alif + Allah, n=2 in pilot), OR
5. `w == prefix + 'الله'` where `prefix ∈ {'و','ف','ب','ت','أب','أف','أو','وت','فت','فب'}` (locked proclitic set), OR
6. `w == prefix + 'لله'` where `prefix ∈ {'و','ف'}` (locked proclitic set; we explicitly exclude `ل` because that would double-count the form-2 case).

**Excluded categories (locked):**
- Verb-stems containing `لله` as part of a stem + object pronoun (e.g., يضلله = yuḍlil-hu = "he leads him astray"). Under the locked rule this token has prefix `يض` which is NOT in the allowed set, so it is correctly excluded.
- Pronominal `ـه` suffixes attached to non-Allah verb stems.
- The single edge case `يضلله` at Q 6:39 is the only token in the corpus that would be falsely included by an over-permissive substring search; the locked rule excludes it.

The pilot count under this rule is **n = 2,704 Allah-tokens** in the 6,236-verse corpus.

## Locked verse-position taxonomy

For a verse with `wc` words and an Allah-token at 1-indexed word-position `p` (1..wc):
- **OPEN**: p ≤ ⌈wc / 4⌉ (first quarter)
- **MID**: ⌈wc / 4⌉ < p ≤ ⌈3*wc / 4⌉ (middle half)
- **CLOSE**: p > ⌈3*wc / 4⌉ (last quarter, includes fāṣila word)
- **FASILA_EXACT**: p == wc (last word, fāṣila position) — measured separately as a strict subset of CLOSE.

## Locked surah-position taxonomy

For a surah with `n_v` verses and an Allah-bearing verse at 1-indexed verse-position `j` (1..n_v):
- **S_OPEN**: j ≤ ⌈n_v / 4⌉
- **S_MID**: ⌈n_v / 4⌉ < j ≤ ⌈3*n_v / 4⌉
- **S_CLOSE**: j > ⌈3*n_v / 4⌉

For each Allah-token (not just each Allah-bearing verse), assign its surah-position based on the verse-id.

## Locked muqaṭṭaʿāt set

```
MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
              36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}  # n = 29
```

## Locked Nöldeke phase mapping

From `data/revelation-order.csv`, four phases:
- Early Meccan
- Middle Meccan
- Late Meccan
- Medinan

Each surah maps to exactly one phase.

## Pre-registered test cells (Bonferroni k=7, α_bon ≈ 0.007143)

### Cell 1 — Per-surah descriptive table + MW-5 control
Build a 114-row table with per-surah Allah counts, density, position breakdowns. **MW-5 positive control**: Q 1 (al-Fātiḥa) must contain ≥ 1 Allah-token (basmala v1 = `بسم الله الرحمن الرحيم`). PASS = MW-5 detected.

### Cell 2 — Zero-Allah surahs enumerated
Enumerate the set of surahs with 0 Allah-tokens. Test: is the count of zero-Allah surahs significant relative to a length-aware null? Null: assume Allah-tokens are uniformly distributed across the 6236 verses; compute the expected probability that a surah of size `n` has zero Allah-bearing verses (negative binomial-like), and then count how many surahs have zero observed vs expected. PASS = observed zero-count differs from expected at p < α_bon (two-sided exact test).
- This cell is novel and the pre-registered direction is: observed > expected (i.e., zero-Allah surahs are more clustered in short surahs than uniform-random).

### Cell 3 — Verse-position distribution test (OPEN/MID/CLOSE)
Among all 2704 Allah-tokens, compute observed (OPEN, MID, CLOSE) counts. Null: verse-position is uniform across the 4 quartiles, i.e., expected (OPEN:MID:CLOSE) = (1/4 : 1/2 : 1/4). χ² goodness-of-fit, df=2.
- α_bon = 0.007143. PASS = χ² p < α_bon.
- Pre-registered prediction: CLOSE will be over-represented (Allah at verse-end / fāṣila position is a known stylistic pattern).

### Cell 3a — Fāṣila-exact test (subset of CLOSE)
For all Allah-tokens, compute the fraction at exact verse-final position (p == wc). Null: under uniform distribution within a verse, p(token at exact final) = 1/wc averaged over the relevant verses. Compute weighted expected count; test observed vs expected by a two-sided binomial test against the pooled expected probability.
- This is reported INSIDE Cell 3's Bonferroni allotment (no extra k).

### Cell 4 — Surah-position distribution test
Same structure as Cell 3 but at the surah scale (S_OPEN/S_MID/S_CLOSE). χ² goodness-of-fit vs uniform (1/4:1/2:1/4).
- α_bon = 0.007143. PASS = p < α_bon.
- Pre-registered prediction: undirected (could be either; classical claim is that "Medinan surahs frame doctrinal points with Allah-mention at openings AND closings"; we test the gross distribution).

### Cell 5 — Density-crown verses (top-K + MW-5 controls)
Rank all 6236 verses by `(Allah-tokens) / (word-count)` descending. Report top-30. **MW-5 controls**: 
- Q 2:255 (Āyat al-Kursī) must appear in top 50 (it has multiple Allah / huwa-Allah / li-llāh tokens).
- At minimum one verse from Q 24:35-37 (Light verse cluster) must appear in top 100.
- Verses from Q 59:22-24 must appear in the top 50 (Khawātim cluster).
- PASS = at least 2 of 3 MW-5 anchors detected in their stated rank windows.

### Cell 6 — Surah density ranking + length control
Rank all 114 surahs by `(total Allah-tokens) / (total words)` descending. Report top-15 and bottom-15. Spearman ρ between density and (a) verse count, (b) word count.
- α_bon = 0.007143 for the ρ-significance test.
- Pre-registered prediction (NOT a strong directional claim; both directions plausible): density may correlate negatively with surah length (because short Mufaṣṣal surahs are theme-tight), or positively (because Medinan legal surahs are long AND Allah-dense).

### Cell 7 — Chronology cross (Nöldeke 4-phase Kruskal-Wallis)
Compute per-surah Allah-density. Group by Nöldeke phase. Test: Kruskal-Wallis H over the 4 phases.
- α_bon = 0.007143. PASS = H-test p < α_bon.
- Pre-registered prediction: Medinan > Late Meccan > Middle Meccan > Early Meccan in density (legal-doctrinal Medinan surahs invoke Allah more frequently per word than mystical-eschatological Early Meccan surahs).

### Cell 7a — Muqaṭṭaʿāt cross (descriptive)
Inside Cell 7's Bonferroni allotment, also report Mann-Whitney U on muqaṭṭaʿāt vs non-muqaṭṭaʿāt surah-density. Pre-registered direction: muq > non-muq in density (most muq surahs are long Medinan-or-Late-Meccan with high Allah-density).

## MW-5 positive controls summary

- **Cell 1**: Q 1:1 contains "الله" (basmala). Direct verification of extractor.
- **Cell 5**: Q 2:255, Q 24:35-37 cluster, Q 59:22-24 must surface in top density windows.

If Cell 1 fails, ALL other cells are invalidated.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| Cell 1 fails | EXTRACTOR_BROKEN (invalidate all) |
| Cell 2 sig | zero-Allah surahs cluster in short Mufaṣṣal (or wherever) |
| Cell 3 sig | verse-position is non-uniform (likely CLOSE-loaded) |
| Cell 4 sig | surah-position is non-uniform |
| Cell 5 MW-5 anchors recovered | density-crown method validated |
| Cell 6 ρ sig | length-density correlation found |
| Cell 7 H sig | chronology phase predicts Allah-density |

## Honest caveats

- The locked counting rule is a **proclitic-aware whole-token rule**, not a morphological lemma rule. It will undercount any case where Allah appears as a constituent of a longer compound that wasn't in the locked prefix list. Pilot inspection of all `الله`/`لله` ending tokens captured 2,704 of 2,705 substring-bounded forms; only `يضلله` (Q 6:39, verb يُضلِلْه) is excluded — correctly.
- Verse-position and surah-position taxonomies are defined on QUARTILES (locked above). A bigram-aware position would give a finer test but is deferred to a follow-up.
- Cell 2's "uniform Allah distribution null" is a STRONG strawman; the real Quran is highly heterogeneous. We use it deliberately because any zero-Allah surah is interpretable against a uniform baseline as "atypically Allah-free".
- Cell 7 Kruskal-Wallis treats Nöldeke phases as a 4-level factor; chronology assignments are themselves contested but we use the project's locked file `data/revelation-order.csv`.
- This finding inherits from the previously-published H-NEW-59 99-names work (which establishes Allah's count at 2538 under a tighter rule). [[h-new-71-allah-distribution|H-NEW-71]] is therefore NOT independent of H-NEW-59 in the M-9 sense; per project policy `endorsement_count` does not increment merely from rule-tuple variation.

## Integrity

- Counting rule, taxonomies, k=7 Bonferroni, all cells, and MW-5 controls locked HERE.
- Seed 20260417.
- Author: [[h-new-71-allah-distribution|h-new-71]]-specialist.
- Pre-reg written 2026-04-15 BEFORE running the analysis script.
