---
id: H-NEW-62
title: Comprehensive Analysis of Surah Closing Verses (ḥusn al-intihāʾ audit)
phase: B
status: PRE-REGISTERED
date: 2026-04-15
agent: h-new-62-specialist
seed: 20260416
rules_tuple: (no-tashkeel; canonical 1..114 mushaf order; LAST verse = highest verse-id per surah; ASCII-tokenized whitespace splitting on Arabic text)
parent: H-NEW-57 (formulaic openings; mirror analysis for endings)
related: al-suyuti-husn-ibtida (REFUTED for openings as a broad pattern)
test_family: descriptive census + closed-form binomial / hypergeometric on enrichment
multi_test_correction: Bonferroni across pre-registered test families (k = 7 families)
---

# [[h-new-62-closings|H-NEW-62]] — Pre-registration: Surah Closings (ḥusn al-intihāʾ)

## Motivation

Classical Arabic balāgha (rhetoric) recognizes ḥusn al-intihāʾ ("excellence of the
ending") as a major rhetorical category, parallel to ḥusn al-ibtidāʾ (excellence of
the opening). Within the Quran-decipherment project the prior probe of openings
(al-suyuti-husn-ibtida) was REFUTED as a broad pattern (see findings folder). The
mirror question — do CLOSINGS show non-trivial structure — has not been tested
comprehensively. This pre-reg locks the taxonomy and tests BEFORE viewing data.

## Data and locking

- Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Closing verse for surah s = the verse with the HIGHEST verse-id in s.
  - Trivially, every surah has a closing verse (114 total).
- Surah class metadata: `/Users/grey/Downloads/quran/data/revelation-order.csv`
  (Meccan vs Medinan, mushaf and Nöldeke order).
- Muqaṭṭaʿāt-opened surahs: the 29 standard list
  {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40,
   41, 42, 43, 44, 45, 46, 50, 68}.
- Prophet-named surahs (header literal contains a recognized prophet's name):
  {10 Yūnus, 11 Hūd, 12 Yūsuf, 14 Ibrāhīm, 47 Muḥammad, 71 Nūḥ}.
- Tokenization: whitespace split on the no-tashkeel Arabic text.

The author has NOT inspected the 114 closing strings before writing this file.
The closing-class taxonomy below is fixed AT THIS COMMIT TIME.

## Pre-registered closing-theme taxonomy (LOCKED)

Each closing verse is assigned the FIRST matching class (priority order top-down).
Multi-label flags are recorded but the primary class is the highest-priority hit.
Patterns are evaluated as case-insensitive Arabic substring matches on the
whitespace-normalized no-tashkeel string.

1. **PRAYER** (duʿāʾ) — explicit petition / plea form. Triggers (any of):
   - imperative addressed to Allah: starts with `رب` ("Rabbi …") or contains
     `ربنا` followed within 6 tokens by an imperative-like verb stem (اغفر، ارحم،
     انصرنا، تقبل، اهدنا، انت مولانا، آتنا، اجعل، لا تؤاخذنا، لا تحملنا).
   - contains imperative `اهدنا` or `انصرنا` or `اغفر لنا` or `تقبل منا` or
     `ربنا اغفر`.
2. **GLORIFICATION/TASBĪḤ** — explicit praise/exaltation formula. Triggers:
   - contains `سبحان` or `سبح` (root s-b-ḥ) within the closing.
   - contains `الحمد لله` or trailing `العالمين` after `رب`.
   - contains `تبارك` (root b-r-k, "blessed is …").
3. **TAKBĪR / NAME-OF-GOD-EMPHATIC** — closes with one of the two-attribute
   divine-name pairs typical of fawāṣil. Triggers: closing two-token suffix
   matches one of the canonical paired-attributes set:
   {الحكيم العليم, العليم الحكيم, الغفور الرحيم, الرحيم الغفور, العزيز الحكيم,
    الحكيم العزيز, السميع البصير, البصير السميع, العزيز الرحيم, الرحيم العزيز,
    الغفور الودود, الودود الغفور, التواب الرحيم, الرحيم التواب, الرءوف الرحيم,
    الرحيم الرءوف, الغفور الحليم, الحليم الغفور, الواسع العليم, العليم الواسع,
    العزيز الغفور, الغفور العزيز, الرحمن الرحيم, الرحيم الرحمن, البر الرحيم}.
4. **OMNI-COMPETENCE / QADĪR** — formulaic statement of God's power. Triggers:
   - contains `على كل شيء قدير` or trailing `قدير` preceded by `شيء`.
   - contains `بكل شيء عليم` or `بكل شيء محيط`.
5. **WARNING / THREAT** (waʿīd) — eschatological/punitive register. Triggers:
   - contains any of {`النار`, `جهنم`, `العذاب`, `عذاب`, `يوم القيامة`, `يوم الدين`,
     `يصلى`, `يصلون`, `الكافرين`, `الظالمين`, `يخسرون`, `الخاسرين`, `بئس`}.
6. **PROMISE / REWARD** (waʿd) — paradisical/reward register. Triggers:
   - contains any of {`الجنة`, `جنات`, `النعيم`, `الفائزين`, `المفلحون`,
     `يفلحون`, `أجر`, `أجرا`, `حسنا`, `الصالحين`, `المحسنين`}.
7. **STATEMENT-OF-BELIEF / TAWḤĪD** — declarative creedal statement. Triggers:
   - contains `لا اله الا` or `لا إله إلا` (no-tashkeel: `لا اله الا`).
   - closing with creedal-third-person assertion `هو الله`, `هو الواحد`,
     `هو القهار`, `هو الحق`.
8. **COMMAND-TO-PROPHET / QUL** — instruction to messenger. Triggers:
   - starts with `قل` token, OR contains `يا أيها النبي`/`يا أيها الرسول`,
     OR the pre-final clause includes `فقل`.
9. **BENEDICTION / SALAM** — peace formula closure. Triggers:
   - contains `سلام` or `الصلاة والسلام`.
10. **NARRATIVE-CLOSURE** (descriptive about prior community / story summary) —
    fallback bucket. Triggers: contains any past-tense narrative verb stem
    {`كان`, `كانوا`, `قال`, `قالوا`, `أرسلنا`, `جعلنا`, `خلقنا`, `أنزلنا`}
    AND none of classes 1–9 fired.
11. **OTHER / DESCRIPTIVE** — residual bucket if no class above fires.

The taxonomy is ordered. PRAYER outranks GLORIFICATION outranks TAKBĪR-PAIR …
outranks OTHER. This deterministic ordering is locked.

## Pre-registered tests (LOCKED, k = 7 family Bonferroni)

1. **T1 (length distribution).** Closing-verse token-length vs surah-mean
   token-length. Predict: NULL (closings have same length as surah mean).
   Test: paired Wilcoxon signed-rank, two-sided, on (closing_len –
   surah_mean_len) across 114 surahs. Report median diff and 95% bootstrap CI.
2. **T2 (closing word distribution).** Last-token (rightmost whitespace token of
   closing verse) frequency table. Compute Shannon entropy H_close vs entropy
   of last tokens of ALL verses (entropy of last tokens of every verse).
   Predict: H_close < H_all (closing words are MORE concentrated than generic
   verse-final words). Test: bootstrap over verse-resampling, 5000 reps.
3. **T3 (paired-attribute fawāṣil at closing).** Count surahs whose closing
   verse ends with one of the 25 paired-attribute couplets in TAKBĪR class.
   Compare against expected count under random selection of any verse from the
   same surah (Monte Carlo, 5000 surah-internal permutations, seed 20260416).
4. **T4 (qadīr/omni-competence formula).** Count surahs whose closing verse
   contains `على كل شيء قدير`. Hypergeometric vs Quran-wide rate of that
   substring at any verse. MW-5 corollary: classical observation expects
   prayer-formula concentration at closings (e.g., Q 1, Q 2:286, Q 3:194).
5. **T5 (Meccan vs Medinan closing-class distribution).** χ² on contingency
   table (closing-class × surah-period). Predict: Medinan tilts toward
   PRAYER + STATEMENT-OF-BELIEF; Meccan tilts toward WARNING.
6. **T6 (muqaṭṭaʿāt vs non-muqaṭṭaʿāt closing-class).** Same χ² on
   muqaṭṭaʿāt-opened (29) vs non-muqaṭṭaʿāt (85). No directional prediction.
7. **T7 (twin-closings).** Pairs of surahs whose closing verses share a
   ≥4-token contiguous suffix. Count and Bonferroni against random pairings
   (5000 permutations). Predict: enrichment over random.

α = 0.05 / 7 = **0.00714** for each family.

## Garden-of-forking-paths log (BEFORE run)

- Tokenization choice: whitespace split on no-tashkeel. NOT lemmatized,
  NOT root-collapsed. Locked to keep formulas literal.
- Last-verse choice: if closing verse spans multiple sajda-style fragments,
  the JSON gives one verse-string; we treat the whole string as the closing.
- "Prophet-named" set: only the six surahs whose header literally names a
  prophet (10, 11, 12, 14, 47, 71). NOT a reading of muqaṭṭaʿāt or contents.
- Twin-closings: 4-token threshold chosen ex ante to avoid trivial 1–2 word
  matches like `الرحيم` alone. Reported but flagged for sensitivity at 3-token.
- All test counts are LOWER-BOUNDED (literal substring matching). Variant
  spellings, archaic orthography, or rare graphemes may undercount.

## Pre-registered "PASS" criteria

- T1 PASS if Wilcoxon signed-rank p < α and median |diff| > 1 token.
- T2 PASS if bootstrapped H_close − H_all < 0 with 99.286% CI excluding zero.
- T3 PASS if observed paired-attribute closings exceed Monte-Carlo p < α.
- T4 PASS if hypergeometric p < α for `على كل شيء قدير` enrichment at closings.
- T5 PASS if χ² p < α with informative residuals.
- T6 PASS if χ² p < α.
- T7 PASS if observed twin-pair count exceeds random p < α.

NULL is published with identical prominence (per project policy).

## Deliverables

- Script: `scripts/h_new_62_closings.py`
- JSON dump: `findings/phase-b-hypotheses/csv/h-new-62.json`
  (rows: surah_id, surah_name, period, muqattaat, prophet_named,
  closing_verse_id, closing_text, closing_tokens, last_token, primary_class,
  multi_class_flags, surah_mean_len, twin_partners)
- Findings: `findings/phase-b-hypotheses/h-new-62-closings.md`
- Journal: `journal/h-new-62-run-1.md`

