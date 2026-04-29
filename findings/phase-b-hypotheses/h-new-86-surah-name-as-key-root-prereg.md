---
id: H-NEW-86
title: Surah-name-as-key-root — comprehensive 114-surah lexical-centrality scan with proper morphological roots
status: PRE-REGISTERED 2026-04-16
spec_locked_at: 2026-04-16 (root assignment locked from Hans-Wehr / standard-Buckwalter mapping BEFORE running tests; assignment recorded in `csv/h-new-86.json` under `surah_root_map` before any p-value is emitted)
parent: H-NEW-49 cell 5 (lexical centrality of name-root, skeleton-match approximation)
bonferroni_family: 2026-04-16-Wave-Surah-Name-Key-Root
bonferroni_k: 114
alpha_bon: 0.05 / 114 = 4.39e-4
rules_tuple: (hafs-kufan; canonical 114; Leeds Quranic Arabic Corpus v0.4 morphology; ROOT field for content roots, LEM field for proper-noun surahs)
seed: 20260417
---

# [[h-new-86-surah-name-as-key-root|H-NEW-86]] — Surah-name-as-key-root, full 114 scan

## Question

For each of the 114 surahs, does the lexical root (or lemma, for proper-noun surahs) of the surah's NAME concentrate inside its own surah at a rate significantly higher than the rest-of-corpus baseline?

## Why this is an extension of [[h-new-49-surah-name-class|H-NEW-49]] cell 5 (NOT a re-run)

[[h-new-49-surah-name-class|H-NEW-49]] cell 5 used a **consonant-skeleton subsequence match** as a rough proxy for root detection. That has known problems: false positives (e.g. ح-ج-ج would catch "ḥujja", "iḥtajja", overcounting); false negatives (the matcher tracks letter ORDER, missing many derived stems where letter-order is preserved but interrupted by vowel-bearers; alif-normalization can hide alif-maqsura distinctions). The Bonferroni was within-cell over `n_testable ≈ 110`.

[[h-new-86-surah-name-as-key-root|H-NEW-86]] fixes the methodology by:
1. Using the **Leeds Quranic Arabic Corpus v0.4 ROOT field** (Buckwalter, gold-tagged) for all content-noun surahs (~95 of 114).
2. Using the **LEM field** for proper-noun surahs whose names are people-tags lacking a triliteral root (Yūsuf, Hūd, Yūnus, Maryam, Luqmān, Nūḥ, Ibrāhīm, Muḥammad). Proper nouns in Leeds are tagged `POS:PN` with a `LEM` but no `ROOT`.
3. Tightening the Bonferroni to **family-of-114** (α_bon = 0.05 / 114 = 4.39e-4) and reporting both raw p and Bonferroni-adjusted at the per-surah level.
4. Adding a per-surah **enrichment ratio** (rate-in-surah / rate-rest-corpus) as the primary effect-size metric.
5. Stratifying results by the [[h-new-49-surah-name-class|H-NEW-49]]-locked taxonomy (PROPHET_PERSON, ANIMAL_OBJECT, etc.) and by muqaṭṭaʿāt-status, to test whether name-root concentration is a STRUCTURAL property of certain surah-types.

## Garden-of-forking-paths disclosure

[[h-new-49-surah-name-class|H-NEW-49]] cell 5 is on disk. I have already seen these top-5 lexical-centrality hits from the cell-5 run (which I am extending):

- Q 12 Yūsuf: 25 / 1795, ratio 529×, p ≈ 3.8e-59
- Q101 al-Qāriʿah: 3 / 36, ratio 3240×, p ≈ 1.2e-10
- Q114 al-Nās: 6 / 20, ratio 92×, p ≈ 4.4e-11
- Q 63 al-Munāfiqūn: 6 / 181, ratio 23×, p ≈ 3.1e-7
- Q  9 al-Tawba: 10 / 2505, ratio 8×, p ≈ 9.0e-7

Plus 7 "ratio = ∞" cases (Q18, Q29, Q46, Q73, Q74, Q83, Q106).

I expect [[h-new-86-surah-name-as-key-root|H-NEW-86]]'s morphological-root method to **REORDER** these and likely PROMOTE some PROPHET_PERSON surahs (because LEM:yuwsuf is a clean surah-12-specific lemma; LEM:nuwH should be Q71-concentrated though present in earlier narrative chapters).

I expect [[h-new-86-surah-name-as-key-root|H-NEW-86]] to **DEMOTE** some [[h-new-49-surah-name-class|H-NEW-49]] cell-5 hits because the skeleton-match was inflating them (e.g., al-Munāfiqūn's root نفق covers "nafaqa" / "infāq" too).

## Procedure (locked)

### Root-mapping table (frozen BEFORE any test)

For each of the 114 surahs, I lock ONE primary identifier:
- **Type ROOT**: a Leeds Buckwalter ROOT string (e.g., `bqr`, `nws`, `rHm`). The test counts all Leeds segments whose ROOT equals this string.
- **Type LEM**: a Leeds Buckwalter LEM string (e.g., `yuwsuf`, `nuwH`). The test counts all Leeds segments whose LEM equals this string.
- **Type NONE**: muqaṭṭaʿāt-letter surahs (Q20 Ṭāhā, Q36 Yāsīn, Q38 Ṣād, Q50 Qāf) — not testable on this axis. 4 surahs.

The full mapping is in `csv/h-new-86-prereg-mapping.json` (will be the same as the script's locked dictionary). Reference: Hans Wehr 4th ed; Lane's Lexicon; Leeds Quranic Arabic Corpus root inventory.

For each name with multiple plausible roots (e.g., al-Insān = أنس / ANS), the mapping picks the Leeds canonical ROOT (Anos / Ans / etc.) used by the Leeds tagger for the surface form of the surah-NAME word — verified by spot-check.

### Per-surah test (Bonferroni-114)

For each testable surah s (110 of them):
1. Count `hits_in[s]` = number of Leeds-tagged tokens in surah s where (ROOT==target if type=ROOT, else LEM==target).
2. Count `hits_rest[s]` = same count over the corpus EXCLUDING surah s.
3. Let `n_in[s]` = total Leeds-tagged TOKENS in surah s (one segment per word counted once at the segment-with-stem level).
4. Let `n_rest[s]` = total Leeds-tagged tokens corpus-rest.
5. **Hypergeometric two-sided test**: P(X ≥ hits_in | total_hits=hits_in+hits_rest, total_tokens, surah_tokens=n_in).
6. Also compute Poisson approximation (sanity check) at λ = hits_total × n_in / n_total.
7. Enrichment ratio = (hits_in / n_in) / (hits_rest / n_rest).

### Token base (locked)

Use Leeds-token base, NOT real-words: for each location `(s,v,w,seg)` with a STEM segment (i.e., not a pure prefix or pure suffix), a token at `(s,v,w)` is counted ONCE for total. Hit counted ONCE if any segment of `(s,v,w)` matches target.

Reason: Leeds total = 77,429 vs anchor real-word = 77,797 (small discrepancy from prefix-only tokens like اَل alone counted differently); the morphology base is the right denominator for morphology-derived hits. Both totals will be reported.

### Bonferroni and verdicts

- **α_bon (per surah)** = 0.05 / 114 = 4.39e-4
- **Verdict per surah**: SIG if p < α_bon; TREND if α_bon ≤ p < 0.05/110; NULL otherwise.
- **Aggregate verdict**: PASS if ≥ 1/3 of testable (≥ 37/110); STRONG-PASS if ≥ 2/3 (≥ 73/110); else EXPLORATORY/NULL.
- Report ALL 114 surahs in the output table regardless of significance.

### Stratifications (pre-committed)

Cross-tabulate pass/fail with:
- **muqaṭṭaʿāt-opener (Y/N)** — 29 vs 81 testable.
- **[[h-new-49-surah-name-class|H-NEW-49]] taxonomy class** (9 classes) — count sigs per class.
- **Proper-noun (LEM type) vs content-noun (ROOT type)** — 8 vs ~102 testable.
- **Surah type (Meccan/Medinan)** from JSON metadata.
- **Surah length quartile** (token count).

For each stratification, report the contingency table; compute Fisher exact (2×2) or χ² (k×2) where applicable. Bonferroni for stratifications: 5 tests × α=0.05 → α_strat_bon = 0.01.

## Pre-committed predictions

1. **Yūsuf (Q12) and Nūḥ (Q71) should be the cleanest LEM hits.** Yūsuf because the cell-5 ratio was already 529×; Nūḥ because the surface form `nuwH` is likely surah-71-concentrated (28 of 28 verses repeat the name).
2. **PROPHET_PERSON class should pass at the highest rate** (proper nouns are inherently surah-discriminative).
3. **DIVINE_ATTRIBUTE class should mostly NULL** because divine attributes are corpus-pervasive (e.g., رحم ROOT appears 339× corpus-wide; al-Raḥmān surah Q55 is a single locus).
4. **EVENT_ESCHATOLOGICAL very-short surahs (Q99, Q101, Q88) should be borderline** — their names use specialized eschatological roots that might appear once in the surah and exactly nowhere else (zero-rest-rate, makes them "infinite ratio" passes).
5. **Aggregate fraction passing**: I predict between 25% and 50% of testable surahs will clear α_bon = 4.39e-4. EXPLORATORY-to-PASS region.

## MW-5 positive control

**MW-5**: LEM:yuwsuf must hit ≥ 25 in Q12 and ≤ 5 outside (this matches [[h-new-49-surah-name-class|H-NEW-49]] cell-5 finding). If this fails, the pipeline is broken. Cell-5 found Yūsuf at p ≈ 1e-59; [[h-new-86-surah-name-as-key-root|H-NEW-86]]'s hypergeometric should give similar order-of-magnitude.

## MW-5 negative control

**MW-5-NEG**: LEM:nuwH should pass Bonferroni-114 (predicted SIG) but its p will be DRAMATICALLY less extreme than Yūsuf because Nūḥ is named in many earlier narrative surahs (Q3, Q4, Q6, Q7, Q9, Q10, Q11, Q21, Q23, Q26, Q29, Q33, Q37, Q42, Q51, Q53, Q54, Q57, Q66, Q69) — the rest-corpus-rate is non-trivial.

## Honest reporting

- Publish full 114-row table with raw p, Bonferroni status, ratio, hits_in, hits_rest, n_in, n_rest.
- Publish stratification 2×2 tables and Fisher p.
- Report ALL Bonferroni-passing surahs (no cherry-pick).
- Report disagreements with [[h-new-49-surah-name-class|H-NEW-49]] cell 5 (any surah that was sig in cell 5 but not in [[h-new-86-surah-name-as-key-root|H-NEW-86]], or vice versa).
- Report any surah where the prereg root-mapping was ambiguous (decision documented inline).

## Files (will be written by script)

- Pre-reg: `findings/phase-b-hypotheses/h-new-86-surah-name-as-key-root-prereg.md` (this file)
- Script: `scripts/h_new_86_surah_name_as_key_root.py`
- JSON output: `findings/phase-b-hypotheses/csv/h-new-86.json`
- CSV table: `findings/phase-b-hypotheses/csv/h-new-86-per-surah.csv`
- Findings: `findings/phase-b-hypotheses/h-new-86-surah-name-as-key-root.md`
- Journal: `journal/h-new-86-run-1.md`

## Integrity

- Root mapping locked in script BEFORE running any test. Mapping printed verbatim in JSON output.
- Bonferroni-114 declared.
- 5 stratifications declared with α_strat_bon = 0.01.
- Two MW-5 controls (positive Yūsuf; subtle Nūḥ).
- All 114 surahs reported regardless of significance.
- Seed 20260417.
