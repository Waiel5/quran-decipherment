---
finding_id: Q027-F-10
title: "Internal basmala corpus-uniqueness — direct grep audit"
phase: B+
date: 2026-05-10
status: PRE-REGISTERED
seed: 20260509
n_perm: deterministic
rules_tuple: "(no-tashkeel, orthographic-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi); cross-validated under min-tashkeel + full-tashkeel"
---

# Q027-F-10 — Internal basmala corpus-uniqueness (direct grep audit)

## Hypothesis (locked)

**H1 (locked direction)**: The full basmala phrase *bismi-llāhi al-raḥmāni al-raḥīm* occurs as an **interior-of-verse substring** (i.e., excluding surah-opening basmala-headers in Q 2-Q 8, Q 10-Q 114 which are not numbered as verses under the Hafs-Kufan rule-tuple `basmala-counted-only-in-Q1`) at **exactly ONE non-Q1 location** corpus-wide: **Q 27:30** (Solomon's letter to the Queen of Sabaʾ).

**Falsification condition**: any non-Q1 verse other than Q 27:30 contains the full 6-token substring `بسم الله الرحمن الرحيم` ⇒ H1 FALSIFIED. Any zero hits ⇒ H1 FALSIFIED. Any count > 1 (excluding Q 1:1) ⇒ H1 FALSIFIED.

Locked direction: **corpus-singleton** (count == 1 among non-Q1 verses; count == 2 counting Q 1:1).

## Method

Deterministic substring search (no permutation null — the test is a uniqueness claim, not a frequency-distribution claim).

1. Load `quran-text/quran-no-tashkeel.json`.
2. Define target substring: `بسم الله الرحمن الرحيم` (no-tashkeel orthographic).
3. Iterate over all 6,236 verses; record every verse whose `text` field contains the target as substring.
4. Tally hits and partition into {Q 1:1, non-Q1}.
5. Cross-validate under min-tashkeel and full-tashkeel using the tashkeel-correct variants of the substring.
6. Report verbatim hits + classification.

## Pre-registered success criteria

- **PASS-CONFIRMED**: exactly 2 hits corpus-wide; 1 hit is Q 1:1; 1 hit is Q 27:30.
- **PASS-DIRECTED**: 2 hits, both at expected verses, but tashkeel-variant discrepancy.
- **FALSIFIED**: any deviation from (count == 2 ∧ hits == {Q1:1, Q27:30}).

## Classical anchors

- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on basmala-uniqueness — classical recognition that Q 27:30 is the unique interior reproduction of the basmala formula (the 113-vs-114 surah-basmala-count debate).
- Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 27:30 — narrative discussion of Solomon citing the basmala in his letter.
- al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 27:30 — verbatim basmala identification.

## Garden-of-forking-paths

The test is a deterministic existence/uniqueness check on a fully-specified target substring. No alternative families considered. Rules-tuple is locked (no-tashkeel default; min + full cross-validation). The 6-token target string `بسم الله الرحمن الرحيم` is the canonical Q 1:1 form.

## Relation to prior pre-regs

This formalises and tightens the T1 deliverable from the 2026-05-10 dispatch. It does NOT duplicate Q027-F-02 (which asked: *is the Q 27:30 basmala-slice token-for-token identical to Q 1:1?* — answer CONFIRMED) nor Q027-F-05.a (which asked: *is the verbatim 6-token sequence corpus-wide count == 2?* — answer CONFIRMED with verse hits). Q027-F-10 is the direct-grep formulation, used here as the explicit pre-registered uniqueness-falsification test, with the falsification condition pre-committed: any other non-Q1 verse containing the full substring breaks it.

## Honest limits (pre-committed)

- "Interior-of-verse" is defined by the Hafs-Kufan rule-tuple `basmala-counted-only-in-Q1`. Under a different rule-tuple (basmala counted as v.0 of every surah), the count would be 113 + Q 27:30 = 114. This is a rule-tuple sensitivity, NOT a fact-of-the-text disagreement. Both counts are documented; the default tuple is locked.
- The full 6-token substring `بسم الله الرحمن الرحيم` is the test target. The 2-token shorter substring `بسم الله` is a separate (broader) target tested in Q027-F-05.c (which surfaced Q 11:41 as a third *bismi-llāhi majrāhā* citation). Q027-F-10 is locked to the 6-token form.

## Pre-commit declaration

I, the specialist, commit to running the test on the no-tashkeel corpus, recording verbatim hits, and reporting the result with full prominence whether PASS or FALSIFIED, before computing any p-value or running any auxiliary analysis. The SHA256 of this file is embedded in the runner script for fail-fast verification per INVESTIGATION-PROTOCOL §1.2.
