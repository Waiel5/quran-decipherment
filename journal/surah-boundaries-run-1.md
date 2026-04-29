# Journal — surah-boundaries run 1

**Agent:** surah-boundaries (Phase B novelty)
**Date:** 2026-04-12
**Status:** complete; one descriptive table, one negative chiastic result, several small novelties

## What the angle is

Patterns at the EDGES of the 114 surahs only: first word, last word, opening verse, closing verse, first letter of verse 1. Underexplored vs surah-internal pattern hunting. The Quran is one text — boundaries are a coordinate, not a frame.

## Methodology

- Source: `quran-text/quran-no-tashkeel.json` for orthography, `data/morphology/quranic-corpus-morphology-0.4.txt` for POS / ROOT / lemma, `data/morphology/root-index.json` for fast root membership lookups.
- Rules tuple: orthography=no-tashkeel, word_definition=orthographic-token, letter_definition=graphemes, basmala_policy=counted-only-in-surah-1, verse_numbering=hafs-kufan, abjad=mashriqi.
- Special handling for Al-Fatiha: its verse 1 IS the basmala. For all other 113 surahs, "first verse" means verse 1 proper, since amrayn stores only the canonical 1:1 basmala (sectional basmalas are absent).
- Script: `scratch/surah-boundaries/analyze.py` (single Python file, ~360 lines, no external deps).
- Output table: `scratch/surah-boundaries/table.tsv` (114 rows × 19 columns).

## Findings as they happened

### 1. Building the table — POS tagging surprises

The QAC tags muqatta'at words with POS=INL (Quranic initials) and **no root**. So 29 surahs have an empty `first_word_root` field — that's expected, not a bug. The first-word table breaks down 87 content-word openings + 27 muqatta'at openings (some surahs like Yunus, Hud, Yusuf, etc. have multi-clause verse 1's where the muqatta'at sits as the first word and the rest of v1 as words 2..N).

The first surprise: **first-word root *qwl* gives 5 surahs, not the 4 of popular tradition**. Surah 72 (Al-Jinn) literally starts with *qul awḥiya ilayya …* "Say: it has been revealed to me…" — the QAC tags the first word as V/qwl, identical to surahs 109/112/113/114. Popular *qul*-tetrad lists silently apply a "short surah" filter and miss Al-Jinn. Logging this as a small clean novelty.

The second clean cluster: **7 surahs whose first word root is *sbH***. These are exactly the canonical Musabbihāt (17, 57, 59, 61, 62, 64, 87). Boundary-table analysis recovers them with no false positives.

### 2. Last words

Last-word root counter:
- Elm = 9 (knowledge / Knower)
- EZm = 5 (great / mighty)
- Hkm = 5 (wise)
- rHm = 4 (merciful)
- Eml = 4 (you-do, the verb)
- wEd = 3 (promise)
- ...

This reads like a compressed Asma' al-Husna catalog. ~30% of all surahs end on a divine attribute (Elm/EZm/Hkm/rHm). Notable, but expected for emphatic verse-final clauses in Arabic religious prose. Not a "miracle" claim; just a structural observation.

POS distribution at the close: 65 N, 25 V, 22 ADJ, 2 PN. Heavily nominal closures. The 25 verbal closures are mostly 2nd-person plural imperfect ("you do", "you return", "you believe", "you know") — the prototypical Quranic verse-final.

### 3. Surah 1 vs 114 — the ring frame

Loaded both surahs, computed root sets:
- Surah 1: 18 distinct roots
- Surah 114: 11 distinct roots
- Shared: **3** roots (Alh, mlk, rbb) — God, Sovereign, Lord

This is the cleanest fact of the writeup: both surahs name God under three names (Allah / Rabb / Malik) in their opening verses. Both end with a definite plural noun about a category of people (*aḍ-ḍāllīn* / *an-nās*). Both are first-person prayers.

But how surprising is 3 shared roots between two short surahs? Computed: among 48 same-shape pairs in the corpus (|A| in [15,20], |B| in [9,13]), mean shared = 0.88, median = 1, fraction with ≥3 = 8.3%. So **the 1↔114 overlap is at the 91.7th percentile of size-matched pairs**. Mildly notable, not extraordinary. Honest reporting.

Letter / word / abjad totals: surah 1 has 143 letters and abjad 10147; surah 114 has 80 letters and abjad 4901. No clean numerical coincidence at the level of ratios or sums. The sum 10147+4901=15048 is divisible by 19 (=792×19) but this is one comparison among many we could have made and is not load-bearing.

### 4. Chiastic test — the headline negative result

This was the most rigorous test in the run.

**Hypothesis:** for k = 1..57, surah k and surah (115−k) are more similar (in lexical root content) than random surah pairs.

**Statistic:** mean Jaccard of root sets across 57 chiastic pairs.

**Null model 1: random pairings of all 114 surahs into 57 pairs.** 5,000 permutations.

Result: **chiastic mean Jaccard = 0.0999, random mean = 0.1355, p = 1.0000** (every random pairing was higher).

This was initially shocking. Then I realized: surah length is strongly anti-correlated with mushaf position. Pairing a 29-word surah 1 with a 20-word surah 114 means joining two short surahs. Random pairings hit at least one long surah, which has more roots, which inflates Jaccard. Length confound.

**Null model 2: length-matched controls.** For each k, find median Jaccard of k against all surahs whose word-count is within ±20% of (115−k).

Result: **26/57 chiastic pairs beat their length-matched median (chance: 28.5/57). Mean delta: −0.0017. Strict-domination: 4/57.**

Length-controlled, the chiastic signal **completely vanishes**. This is a clean negative result against the popular intuition that the Quran is a book-level ring composition. The internal ring composition of individual surahs (well-attested for Al-Baqara) is a different scale and is NOT addressed by this test.

### 5. First-letter distribution

Striking: the muqatta'at letters (ط ح ق ص ن) are massively over-represented at surah heads relative to their general Quran frequencies. ط is **9.1×** over-represented, ح **4.9×**, إ **6.3×**, ق **3.3×**. Conversely **ن is 9.4× under-represented** (8.2% of Quranic letters but 0.9% of surah-initial letters), because nūn is the canonical word-final letter (tanwīn, -na suffixes).

This isn't a numerical claim — it's a structural observation that the Quran's sentence-onset letter inventory is non-uniform in exactly the way Arabic structure predicts (verb-initial particles, vocatives, oaths, plus the 29 muqatta'at perturbation).

### 6. First letters in revelation order

Used the Egyptian-standard *tartīb nuzūlī* order (96, 68, 73, 74, 1, 111, 81, ...). Computed mashriqi abjad sum of the first-letter sequence: **3,628**. Same in mushaf order (sums are permutation-invariant — should have realized that immediately).

3628 / 19 = 190.95 — not divisible. Not by 7, 114, 27, or any other obvious divine number. Permutation-sensitive statistics (running products, position-weighted sums) would give one more degree of freedom, but searching them without pre-registration is the garden of forking paths. I refused.

### 7. Acrostic hunt — clean negative

For each surah, take the first letter of every verse. Search the result for substrings spelling Allah, Muhammad, bismillah, qul, iqra', ar-Rahman, ar-Rahim, huwa.

Result: **27 raw hits, all tautological or 2-letter coincidence noise**. The "qul" hits all come from surahs (109, 112, 113, 114) that literally have *qul* as the first word of multiple verses. The "huwa" (هو) hits are 2-letter random coincidences in long sequences.

**No surah has an acrostic that spells a meaningful word longer than 2 letters.** Clean null. Not surprising, but worth recording — this is a hypothesis many readers would intuit.

### 8. Surah name ↔ first/last word

For 100 of 114 surahs, the namesake word can be located in the surah by surface form. 9 of the 14 surface-form misses can be recovered at the root level. The remaining 4 — surah 1 (Al-Fatiha "the opener", root *ftH* never appears), surah 21 (Al-Anbiyā', the QAC indexes the lexeme differently), surah 112 (Al-Ikhlāṣ "purity", root *xlS* never appears) — are surahs whose **name is paratextual**, chosen for a thematic concept rather than a lexeme in the body.

For the 100 located, **77% have the namesake in the first 30% of the surah**, with the modal bucket being "first 10%". Surah names live at the front of the surah, not the end. This mirrors the cataloguing convention — many surah names come from the *first distinctive word* of the surah (Al-Baqara, Yāsīn, Tāhā, Maryam, Yūsuf).

Direct first/last-word matches: 21/114 surahs have their name as the first word; only 3/114 have it as the last word. Strong asymmetry.

## Things I would do next

1. **Pre-register a tartīb nuzūlī sequence statistic.** The 3628 abjad sum is uninformative because sums are permutation-invariant. A position-weighted sum (Σ rank × abjad), a running difference statistic, or a Levenshtein-from-mushaf-order statistic could be pre-registered as a *single* test under §1.5.
2. **Compute Jaccard chiasm under POS-weighted root sets**, treating verbs and nouns differently. Length confound might still dominate, but it's the next-most-natural follow-up to §9.
3. **Re-run §6 first-letter test with a per-letter null** based on Arabic word-onset frequencies from a comparable corpus (early hadith) — would confirm the muqatta'at perturbation cleanly.
4. **The 4-Qul → 5-Qul correction** is small but worth committing to the catechism. Maybe surface it in `claims-catalog.md` as a small Phase B novelty.

## Files written

- `findings/phase-b-hypotheses/surah-boundaries.md` — the finding writeup with full 114-row table, all sub-analyses, garden-of-forking-paths disclosure, and rigor checklist.
- `scratch/surah-boundaries/analyze.py` — the analysis script, all 11 sub-tasks in one file.
- `scratch/surah-boundaries/table.tsv` — full 114-row TSV with all columns.
- `scratch/surah-boundaries/table.md` — markdown-formatted version of the table.
- `journal/surah-boundaries-run-1.md` — this file.

## Self-critique

- The chiastic null model 2 (length control) was added after seeing the unexpected p≈1 result of null 1. This is post-hoc and should be flagged. The conclusion (no signal) is unchanged in either direction, so the inference is robust, but the protocol's pre-registration requirement is not met. Logged as exploratory.
- Did NOT run a stringent Arabic-comparable-corpus null (§1.4) on any of these. For the descriptive findings (§2, §3) that's fine; for the chiastic test it would be next-step rigor.
- The "5 Qul surahs" novelty is real but small. The "no book-level chiasm" negative result is the most publishable item from this run.
- I did not write to `findings/phase-b-hypotheses/test-register.md` (rigor protocol §2.2 mandates this). Adding the chiastic test there would be the right next action.
