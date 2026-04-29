---
prereg_id: Q045-F-02
title: hawan-as-god twin construction Q 25:43 ↔ Q 45:23 corpus-singleton-pair
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T03:05:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q045-F-02 — *ittakhadha ilāhahu hawāhu* twin

## 1. Hypothesis (direction-locked)

**H1 (twin singleton-pair)**: The exact string *اتخذ إلهه هواه* ("he has taken his passion as his god") appears in **exactly two** verses of the Qurʾān: **Q 25:43** and **Q 45:23**, and only in these two.

**H1b (descriptive lexical signature)**: Q 45:23 expands the construction with a 5-element punitive consequence-chain — *aḍallahu Allāhu ʿalā ʿilm + khatama ʿalā samʿihi wa-qalbihi + jaʿala ʿalā baṣarihi ghishāwa + fa-man yahdīhi min baʿdi llāh* — whereas Q 25:43 closes immediately at *afa-anta takūnu ʿalayhi wakīlan* (rhetorical-question form). The Q 45:23 verse is **substantially longer** in word-count than Q 25:43 (locked threshold: Q 45:23 > 1.7 × Q 25:43 word-count under no-tashkeel, pause-marks-stripped).

## 2. Null

**H0a (for H1)**: the construction appears in ≠2 verses, or in two verses other than {Q 25:43, Q 45:23}.

**H0b (for H1b)**: word-count ratio Q 45:23 / Q 25:43 ≤ 1.7.

## 3. Operationalization

- Tashkeel level: **no-tashkeel** (default rules-tuple).
- Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
- Search method: exact substring match `اتخذ إلهه هواه` against each verse's text field.
- Word-count: split on whitespace after stripping pause-marks `[ۖۚ۞ۗ]`.
- Stability check: re-run with `min-tashkeel` text variant; tashkeel doesn't affect the consonantal substring.

## 4. Direction lock

Pre-committed direction: **count == 2 ∧ verses == {Q 25:43, Q 45:23} ∧ ratio_words(45:23 / 25:43) > 1.7**.

If count != 2 or verse-set wrong: **NULL — twin claim falsified**.
If word-ratio ≤ 1.7: **H1b NULL — direction-locked refinement claim falsified**.

## 5. Bonferroni

k = 2 (H1 + H1b); α_corrected = 0.05/2 = 0.025. Both H1 and H1b are deterministic-string / arithmetic operations on the canonical text — no permutation; reported as exact-match outcomes.

## 6. Success / failure criteria

- **Success (VINDICATED)**: H1 ∧ H1b both pass.
- **PARTIAL**: H1 passes, H1b fails (or vice versa).
- **NULL**: both fail.
- **Precommit violation**: count == 2 but wrong verse-set.

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q045-F-02.json` with: hit-count, verse-list, full-text-of-each-verse, word-counts (no-tashkeel), word-count-ratio, rules-tuple-stability table.

## 9. Motivation

Classical exegetes (al-Ṭabarī, al-Rāzī, Ibn Kathīr, al-Qurṭubī) repeatedly cross-reference Q 25:43 and Q 45:23 as the corpus's two hawan-as-god verses; al-Rāzī, *Mafātīḥ al-ghayb* ad Q 45:23, develops the **expansion-thesis**: Q 45 takes the Q 25 question and supplies the punitive rationale (the senses are sealed). The expansion-thesis is structurally testable: if Q 45:23 is substantially longer and elaborates Q 25:43, this is a verse-twin pattern with a directional dependency. If both verses are equal-length, the classical "expansion" claim is rhetorical not structural. The 1.7× threshold is set to require non-trivial expansion (typical Quranic verse-pair length-ratios under random pairing tend to cluster in [0.5, 2.0] — a 1.7× ratio is in the upper third).
