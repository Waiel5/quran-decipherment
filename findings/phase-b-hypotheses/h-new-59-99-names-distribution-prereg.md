---
id: H-NEW-59
title: Comprehensive distribution analysis of the 99 divine names (al-asmāʾ al-ḥusnā) across surahs
phase: B
status: PRE-REGISTERED 2026-04-15
agent: h-new-59-specialist
spec_locked_at: 2026-04-15 (BEFORE running counting script; the 8-Khawātim exclusivity is established at MASTER-LEDGER §2 and this analysis confirms it as MW-5 positive control)
bonferroni_family: 2026-04-15-Wave-H-NEW-59-Divine-Names-Distribution
bonferroni_k: 6
alpha_bon: 0.00833  # 0.05 / 6
rules_tuple: (no-tashkeel; word-segment substring search of definite-singular form ال + name; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)
primary_data: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json (114 surahs, 6236 verses)
canonical_99_list: /Users/grey/Downloads/quran/data/asma-al-husna.txt (al-Tirmidhī #3507, al-Walīd ibn Muslim narration)
seed: 20260415
---

# H-NEW-59 — Comprehensive 99-Names Distribution Analysis

## Question

The classical Tirmidhī list of 99 divine names is a **hadith construct** (al-Walīd ibn Muslim narration). The pre-existing project finding (`divine-names-distribution.md`, 2026-04-12) established with morphology-driven QAC counting that ~58 of 99 names appear as DET-MS in the Quran and 8 names are exclusive to Q 59:22-24 (Khawātim al-Ḥashr).

H-NEW-59 EXTENDS this with a **substring-based replication** (rule-tuple variant) plus four NOVEL questions:

1. **Per-name distribution table** under no-tashkeel substring matching: tokens, distinct surahs, top-surah, exclusivity-class (1-surah, 2-surah, 3-surah, etc.).
2. **Surah-exclusive names**: how many of the 99 divine names appear in only 1 surah of the corpus?
3. **Fātiḥa as encoding**: how many of the 99 names appear in Q 1? Does Q 1 systematically over-represent the divine-name space relative to a random 7-verse window?
4. **Top-K divine-name density verses**: across all 6236 verses, which have the highest density (names / words)?
5. **Surah ranks by total divine-name density**: replicate the rank order from `divine-names-distribution.md` under the new tuple.
6. **Muqaṭṭaʿāt vs non-muqaṭṭaʿāt divine-name density**: does the muqaṭṭaʿāt set predict divine-name density per surah? (cross-finding-006 9th axis test).

## Garden-of-forking-paths disclosure

Pre-existing knowledge before locking the spec:

- The 8 Khawātim al-Ḥashr names exclusivity is ALREADY ESTABLISHED in MASTER-LEDGER §2 and `divine-names-distribution.md`. Cell-1 functions here as MW-5 positive control.
- The 50% density of Q 59:23 is ALREADY ESTABLISHED. Cell-4 includes it as MW-5 positive control.
- The Fātiḥa contains "الله, الرحمن, الرحيم, الملك" (counting "مالك" as al-Malik variant) — at least 4 of 99 names; the question is whether 4 is statistically high for a 7-verse window.
- The cross-finding-006 multi-axis muqaṭṭaʿāt picture has 8 axes. H-NEW-59 may add a 9th axis (divine-name density) but is pre-registered as a directed two-sided test (no prior commitment to direction; if anything, the Khawātim al-Ḥashr in Q 59 — a non-muqaṭṭaʿāt surah — argues AGAINST muqaṭṭaʿāt enrichment for divine names).

Honest protection: the 6 cells are locked BEFORE running the script. Cells 2 and 6 are the principal novel hypotheses; cells 1, 4, 5 partly replicate prior work under a NEW rule-tuple (substring-based, no morphology dependency).

## Locked methodology

### Canonical 99-name list

Locked to `/Users/grey/Downloads/quran/data/asma-al-husna.txt` (al-Tirmidhī list). Each name is searched as the **definite-singular form** (ال + stem), without tashkeel. Variants tested:

- Primary form: `الـ + name` (e.g., الرحمن, القدوس, السلام).
- For names that may appear with proclitic prefixes (و, ف, ب, ل, ك): substring search counts these as occurrences provided the stem is bounded by a non-letter character on the right OR is a complete word.
- For "الله", count direct lemma; for "الرحمن", count direct lemma.
- Exception names (Mālik al-Mulk, Dhū al-Jalāl wa-l-Ikrām): treated as multi-word phrases requiring exact substring match.
- The two ambiguous cases noted in the QAC pre-existing work (al-ʿAzīz/al-Malik in Sūrat Yūsuf referring to the governor) are NOT excluded under the substring rule (this is a deliberate rule-tuple difference; we report and flag the false-positive count separately).

### Per-name metrics

For each name N:
- `tokens[N]` = total substring occurrences in the Quran corpus
- `verses[N]` = number of distinct verses containing ≥1 occurrence of N
- `surahs[N]` = number of distinct surahs containing ≥1 occurrence of N
- `top_surah[N]` = surah with most occurrences (ties broken by surah index ascending)
- `exclusivity_class[N]` = surahs[N] (1 = surah-exclusive, 2 = bi-surah, etc.)

### Density per verse and per surah

- `verse_density(v)` = (number of distinct divine-name occurrences in v) / (word count of v)
- `surah_density(s)` = (sum of divine-name tokens across all verses of s) / (sum of word counts across s)

### Muqaṭṭaʿāt set (locked from [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]])

```
MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
              36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}  # n = 29
```

Non-muqaṭṭaʿāt surahs: the remaining 85.

## The 6 pre-registered cells

### Cell 1 — Per-name table (descriptive replication + MW-5 positive control)

Compute the full 99-row table.

**MW-5 lock-in (rule-tuple-aware):** under the locked SUBSTRING tuple (no morphology, no semantic disambiguation), the 8 Khawātim names are predicted to BEHAVE DIFFERENTLY than under the morphology-strict tuple of `divine-names-distribution.md`. Specifically:

- al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir, al-Bāriʾ, al-Muṣawwir (6 of 8) — predicted SURAH-EXCLUSIVE to Q 59 (these have no plausible non-divine substring co-occurrence).
- al-Quddūs — predicted to be 1-2 surah (Q 59 plus possibly Q 62:1 if "al-Malik al-Quddūs" recurs there).
- al-Salām — predicted to be MULTI-SURAH under substring (because السلام is the most common Arabic noun for "peace/greeting/safety" and appears across legal/narrative contexts not as divine name).

PASS = (a) at least 6/8 Khawātim are surah-exclusive to Q 59, AND (b) the 2 expected non-exclusivities (al-Quddūs, al-Salām) are EXPLAINED by either a known divine-name parallel-verse (al-Quddūs at Q 62:1) or by clear non-divine substring usage (al-Salām in "dār al-salām" / greeting). FAIL = unexpected non-Q59 surah for any of the strict 6.

This rule-tuple-aware MW-5 protects the test from a brittle morphology dependency while still validating that the substring rule is sane.

### Cell 2 — Number of surah-exclusive names

Test statistic: K = count of names with exclusivity_class = 1 (appear in only 1 surah).
Direction: descriptive (no null). Report alongside top-1-surah identity.
Pre-committed disclosure: the 8 Khawātim are guaranteed to be in K (MW-5 control). Question: how many MORE are exclusive?

### Cell 3 — Fātiḥa-as-encoding test

Test statistic: F = number of distinct 99-list names appearing in Q 1 (verses 1-7).
Null model: random sample of 7 consecutive verses from the 6236-verse corpus (sliding-window null, all 6230 windows). Compute the distribution of F under the null and report Q1's percentile.
Direction: one-sided (Fātiḥa expected to OVER-represent divine names; classical claim is that Fātiḥa "summarizes the Quran").
Pass = Q1's F is in the top 1% of the null distribution at α_bon = 0.00833.

### Cell 4 — Top-K verse-density ranking

Compute verse_density(v) for all 6236 verses. Report top-20.
**MW-5 control:** Q 59:23 must appear in the top-3 (already established at 50% density).
Pre-committed: report top-20 with surah, verse, word-count, names-found, density.

### Cell 5 — Surah density ranking

Compute surah_density(s) for all 114 surahs. Report top-20.
Replicate prior `divine-names-distribution.md` ordering under the new tuple.
**MW-5 control:** Q 59 (al-Ḥashr) must appear in top-5.

### Cell 6 — Muqaṭṭaʿāt vs non-muqaṭṭaʿāt divine-name density

Test statistic: difference in mean surah_density between the 29 muqaṭṭaʿāt-opened surahs and the 85 non-muqaṭṭaʿāt-opened surahs.
Null model: 100,000 permutations of the 114 surah labels, keeping the {29, 85} split.
Direction: two-sided (no prior commitment; Q 59 lives in the non-muqaṭṭaʿāt set).
Pass at α_bon = 0.00833 if |z| > 2.64 OR p_perm < 0.00833.

## Bonferroni family

k = 6. α_bon = 0.05 / 6 ≈ 0.00833. Cells 1, 4, 5 are descriptive/MW-5 controls (no Bonferroni slot consumed). Cells 2, 3, 6 are inferential (3 tests but family-of-6 to absorb the 3 descriptive cells against a sceptical reviewer).

## Pre-committed honesty controls

- Seed = 20260415. Re-run must reproduce results bit-identically.
- Garden-of-forking-paths declared above.
- MW-5 positive control: 8 Khawātim names (Cell 1) and Q 59:23 (Cell 4) and Q 59 (Cell 5).
- All raw counts published in `csv/h-new-59.json` regardless of cell verdict.
- The full per-name table published in the findings file regardless of which cells pass.

## Outputs

1. `/Users/grey/Downloads/quran/scripts/h_new_59_divine_names_distribution.py` — the script
2. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-59.json` — raw per-name table + cell results
3. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-59-99-names-distribution.md` — findings file
4. `/Users/grey/Downloads/quran/journal/h-new-59-run-1.md` — run journal

## Cross-references

- MASTER-LEDGER §2 (the canonical 99-name list and 8 Khawātim exclusivity)
- `divine-names-distribution.md` (the pre-existing morphology-based analysis under a different tuple)
- cross-finding-006 (multi-axis muqaṭṭaʿāt design; Cell 6 is a candidate 9th axis)
- [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] / [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] (locked muqaṭṭaʿāt set)
- H-META-1 item 5 (substance-type reliability moderator: substring-based descriptive cataloguing is in the structural-formal lane, base rate ~72% confirmation)
- M-9 (convergence-does-not-multiply): the 8 Khawātim exclusivity is ONE finding attested two ways (morphology + substring), not 2 independent findings.
